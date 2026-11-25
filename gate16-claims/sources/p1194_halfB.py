#!/usr/bin/env python3
"""
p1194_halfB.py -- P119-4 half (b): H_,phi(pi0) = 0 escape.
Constraint by parametrisation: pi0 = bc / (2(2 xi + b2)).
Free vector y = (xi, bc, b2, shape, p1, p2, mu, rho0).
Usage: p1194_halfB.py LO HI (start-index range). Prints one
compact JSON line per start. float64.
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

wall = L.Wall(1.1)
PTS = wall.pts_sub
G_SUB = wall.kern(PTS)['g']
SCALE = P4.ec_scale(wall, PTS)
HINGE = P4.HINGE_Z; RHO_H = P4.HINGE_RHO


def pi0_of(xi, bc, b2):
    return bc / (2.0 * (2.0 * xi + b2))


def y_to_z(y):
    xi, bc, b2, shape, p1, p2, mu = [float(q) for q in y[:7]]
    return np.array([xi, bc, b2, pi0_of(xi, bc, b2), shape, p1, p2, mu])


def project_hinge():
    """Closed-form scaled projection of the hinge z onto the
    constraint set: keep (xi, pi0, shape, p1, p2, mu); solve
    (bc, b2) minimising (bc-bc_h)^2 + (b2-b2_h)^2 subject to
    bc = 2 (2 xi + b2) pi0 (1-D quadratic, solved exactly)."""
    xi, bc_h, b2_h, pi0 = HINGE[0], HINGE[1], HINGE[2], HINGE[3]
    # b2 = bc/(2 pi0) - 2 xi  =>  minimise (bc-bc_h)^2 +
    # (bc/(2 pi0) - 2 xi - b2_h)^2
    a = 1.0 / (2.0 * pi0)
    # b2 = a*bc - 2 xi; minimise (bc-bc_h)^2 + (a*bc - 2 xi - b2_h)^2
    bc = (bc_h + a * (2.0 * xi + b2_h)) / (1.0 + a * a)
    b2 = a * bc - 2.0 * xi
    z = HINGE.copy(); z[1], z[2] = bc, b2
    return z


def starts():
    out = []  # (y vector, branch)
    zp = project_hinge()
    out.append((np.array([zp[0], zp[1], zp[2], zp[4], zp[5], zp[6],
                          zp[7], RHO_H]), 'pos'))
    # positive branch: hinge couplings, bc re-solved at other pi0 targets
    for bc in (1.0, 3.9, 0.5):
        out.append((np.array([HINGE[0], bc, HINGE[2], HINGE[4],
                              HINGE[5], HINGE[6], HINGE[7], RHO_H]), 'pos'))
    out.append((np.array([1.0, 2.0, -1.0, 0.95, 1.0, 0.5, -0.5, 0.03]), 'pos'))
    out.append((np.array([0.3, 1.5, 1.5, 1.05, 2.0, -1.0, 0.8, 0.02]), 'pos'))
    # negative branch: need 2 xi + b2 < 0 for pi0 > 0
    out.append((np.array([0.5, -1.0, -1.9, HINGE[4], HINGE[5], HINGE[6],
                          HINGE[7], RHO_H]), 'neg'))
    out.append((np.array([0.2, -2.0, -1.8, 0.95, 1.0, 0.5, -0.5, 0.03]), 'neg'))
    out.append((np.array([0.8, -0.5, -1.95, 1.05, 2.0, -1.0, 0.8, 0.02]), 'neg'))
    out.append((np.array([0.1, -3.5, -1.2, 0.90, 0.5, 1.5, -1.2, 0.04]), 'neg'))
    rng = np.random.default_rng(11942)
    while len(out) < 14:
        xi = float(rng.uniform(0.0, 2.0)); b2 = float(rng.uniform(-2.0, 2.0))
        s = 2 * xi + b2
        if abs(s) < 0.3:
            continue
        bc = float(rng.uniform(0.1, 3.5)) * (1 if s > 0 else -1)
        pi0 = pi0_of(xi, bc, b2)
        if not (0.05 <= pi0 <= 2.8):
            continue
        out.append((np.array([xi, bc, b2, float(rng.uniform(0.85, 1.15)),
                              float(rng.uniform(-3, 3)),
                              float(rng.uniform(-3, 3)),
                              float(rng.uniform(-3, 3)),
                              float(rng.uniform(0, 0.05))]),
                    'pos' if bc > 0 else 'neg'))
    return out


STARTS = starts()
LO_B = {'pos': np.array([0.0, 0.05, -2.0, 0.85, -3.0, -3.0, -3.0, 0.0]),
        'neg': np.array([0.0, -4.0, -2.0, 0.85, -3.0, -3.0, -3.0, 0.0])}
HI_B = {'pos': np.array([5.0, 4.0, 2.0, 1.15, 3.0, 3.0, 3.0, 0.05]),
        'neg': np.array([5.0, -0.05, 2.0, 1.15, 3.0, 3.0, 3.0, 0.05])}


def resid(y):
    xi, bc, b2 = float(y[0]), float(y[1]), float(y[2])
    s = 2.0 * xi + b2
    pi0 = pi0_of(xi, bc, b2) if abs(s) > 1e-12 else 99.0
    z8 = y_to_z(y)
    base = P4.residuals_gen(wall, PTS, G_SUB, SCALE, z8,
                            (P4.W_B, float(y[7])))
    pen = []
    if abs(s) < 0.2:
        pen.append(100.0 * (0.2 - abs(s)))
    if not (0.02 <= pi0 <= 2.9):
        pen.append(100.0 * (max(0.02 - pi0, pi0 - 2.9) + 0.01))
    return np.concatenate([base, pen]) if pen else base


def read_y(y):
    z8 = y_to_z(y)
    return P4.full_read(wall, PTS, z8, (P4.W_B, float(y[7]))), z8


def trim(r, z8, y, extra):
    out = dict(z=[float(x) for x in z8], y=[float(x) for x in y],
               rho0=float(y[7]),
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
    zp = project_hinge()
    print('PROJECTION ' + json.dumps(dict(
        projected_z=[float(x) for x in zp],
        pi0_check=float(pi0_of(zp[0], zp[1], zp[2])),
        Hphi_at_pi0=float(-(2 * zp[0] + zp[2]) * zp[3] + zp[1] / 2.0))),
        flush=True)
    y0, _br = STARTS[0]
    r0, z0 = read_y(y0)
    print('HINGESEED ' + json.dumps(trim(r0, z0, y0,
                                         dict(tag='hinge_projected_initial'))),
          flush=True)

for i in range(LO_I, min(HI_I, len(STARTS))):
    y0, br = STARTS[i]
    lo, hi = LO_B[br], HI_B[br]
    y0 = np.clip(y0, lo + 1e-9, hi - 1e-9)
    t0 = time.time()
    try:
        sol = least_squares(resid, y0, bounds=(lo, hi),
                            xtol=1e-12, ftol=1e-12, max_nfev=150)
        yf = sol.x
    except Exception as ex:  # noqa: BLE001
        print('RUN ' + json.dumps(dict(start=i, branch=br, error=str(ex))),
              flush=True)
        continue
    r, z8 = read_y(yf)
    cost = float(np.sum(resid(yf) ** 2))
    print('RUN ' + json.dumps(trim(r, z8, yf, dict(
        start=i, branch=br, cost=cost, seconds=time.time() - t0))), flush=True)
print('DONE', flush=True)
