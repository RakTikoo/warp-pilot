#!/usr/bin/env python3
"""
p1194_halfA.py -- P119-4 half (a): non-flat profile escape.
Usage: p1194_halfA.py LO HI  (start-index range [LO,HI) to run)
Prints one compact JSON line per start to stdout (plus an FD
line and the hinge-seeded initial read). float64.
"""
import json
import sys
import time

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase119/work')
import p1194_lib as P4  # noqa: E402
import p1015_lib as H   # noqa: E402
import p761_lib as L    # noqa: E402

W = '/home/hatch/workspace/warp-pilot'
LO_I, HI_I = int(sys.argv[1]), int(sys.argv[2])

wallP = L.Wall(1.1)
PTS = wallP.pts_sub
G_SUB = wallP.kern(PTS)['g']
SCALE = P4.ec_scale(wallP, PTS)
wall = P4.WallNF(1.1)

# ---- FD verification of the NF profile jets (before any read) ----
prof = P4.NFProfile(0.34, 0.87, 0.15, 3.0)
rr = np.linalg.norm(PTS, axis=1)
h = 1e-6
d1_fd = (prof.cs(rr + h) - prof.cs(rr - h)) / (2 * h)
d2_fd = (prof.d1(rr + h) - prof.d1(rr - h)) / (2 * h)
e1 = np.max(np.abs(prof.d1(rr) - d1_fd)) / np.max(np.abs(prof.d1(rr)))
e2 = np.max(np.abs(prof.d2(rr) - d2_fd)) / np.max(np.abs(prof.d2(rr)))
print('FDCHECK ' + json.dumps(dict(d1_rel=float(e1), d2_rel=float(e2),
                                   pass_=bool(e1 < 1e-6 and e2 < 1e-6))),
      flush=True)

B76 = json.load(open(W + '/phase76/results/p761_B_1.1.json'))
B79 = json.load(open(W + '/phase79/results/p791_b_B_1.1.json'))
Z_B = np.array(B76['joint_best']['z'][:7]); RHO_B = float(B76['joint_best']['z'][7])
Z_B79 = np.array(B79['joint_best']['z'][:7]); RHO_B79 = float(B79['joint_best']['z'][8])
HINGE = P4.HINGE_Z; RHO_H = P4.HINGE_RHO


def starts():
    out = []
    for A, lam in ((0.15, 3.0), (-0.15, 3.0), (0.25, 4.5),
                   (0.10, 2.5), (-0.25, 5.0)):
        out.append(np.concatenate([HINGE, [A, lam, RHO_H]]))
    out.append(np.concatenate([Z_B, [0.0, 0.20, 3.5, RHO_B]]))
    out.append(np.concatenate([Z_B79, [-0.5, 0.20, 3.0, RHO_B79]]))
    rng = np.random.default_rng(11941)
    while len(out) < 14:
        zz = rng.uniform(P4.LO8, P4.HI8)
        out.append(np.concatenate([zz, [float(rng.uniform(-0.35, 0.35)),
                                        float(rng.uniform(2.0, 6.0)),
                                        float(rng.uniform(0, 0.05))]]))
    return out


STARTS = starts()
LO = np.concatenate([P4.LO8, [-0.35, 2.0, 0.0]])
HI = np.concatenate([P4.HI8, [0.35, 6.0, 0.05]])


def resid(v):
    z8 = v[:8]
    wall.prof_A, wall.prof_lam = float(v[8]), float(v[9])
    return P4.residuals_gen(wall, PTS, G_SUB, SCALE, z8,
                            (P4.W_B, float(v[10])))


def readv(v):
    z8 = v[:8]
    wall.prof_A, wall.prof_lam = float(v[8]), float(v[9])
    return P4.full_read(wall, PTS, z8, (P4.W_B, float(v[10])))


def trim(r, v, extra):
    out = dict(z=[float(x) for x in v],
               subset_legal=r['subset_legal'],
               eom_rel_max_nondeg=r['eom_rel_max_nondeg'],
               eom_rel_med_nondeg=r['eom_rel_med_nondeg'],
               n_nondeg=r['n_nondeg'], n_deg=r['n_deg'],
               health_ok=r['health_ok'], frontier_A=r['frontier_A'],
               trap_fires=r['trap_fires'], Fsum_maxabs=r['Fsum_maxabs'],
               H_min=r['H_min'], PX_min=r['PX_min'],
               alignment_set=r['alignment_set'],
               alignment_detail=r['alignment_detail'],
               max_resid_point=r['max_resid_point'],
               max_resid_in_alignment=r['max_resid_in_alignment'],
               max_resid_decomp=r['max_resid_decomp'],
               n_plateau_kin_live=r['n_plateau_kin_live'])
    out.update(extra)
    return out


if LO_I == 0:
    v0 = STARTS[0]
    r0 = readv(v0)
    print('HINGESEED ' + json.dumps(trim(r0, v0, dict(tag='hinge_seed_initial'))),
          flush=True)

for i in range(LO_I, min(HI_I, len(STARTS))):
    v0 = np.clip(STARTS[i], LO + 1e-9, HI - 1e-9)
    t0 = time.time()
    try:
        sol = least_squares(resid, v0, bounds=(LO, HI),
                            xtol=1e-12, ftol=1e-12, max_nfev=150)
        vf = sol.x
    except Exception as ex:  # noqa: BLE001
        print('RUN ' + json.dumps(dict(start=i, error=str(ex))), flush=True)
        continue
    r = readv(vf)
    cost = float(np.sum(resid(vf) ** 2))
    print('RUN ' + json.dumps(trim(r, vf, dict(
        start=i, cost=cost, seconds=time.time() - t0))), flush=True)
print('DONE', flush=True)
