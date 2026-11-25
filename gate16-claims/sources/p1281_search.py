#!/usr/bin/env python3
"""
p1281_search.py -- P128-1 (FU-P1194-1): compose the two escapes.
H_,phi(pi0) = 0 by parametrisation (pi0 eliminated) ON half (a)'s
non-flat blend profile (WallNF). Free vector
y = (xi, bc, b2, shape, p1, p2, mu, A, lam, rho0).
Usage: p1281_search.py LO HI  (start-index range [LO,HI))
Appends one JSON record per start (seed read + optimised read)
to work/p1281_ckpt.jsonl and prints compact lines. float64.
Pose/seeds: results/p1281_run_record.md S2-S3 (fixed before
numbers).
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import least_squares

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, W + '/phase119/work')
sys.path.insert(0, W + '/phase101/work')
sys.path.insert(0, W + '/phase79')
sys.path.insert(0, W + '/phase76')
sys.path.insert(0, W + '/phase18')
import p1194_lib as P4  # noqa: E402
import p1015_lib as H   # noqa: E402
import p761_lib as L    # noqa: E402

LO_I, HI_I = int(sys.argv[1]), int(sys.argv[2])
CKPT = W + '/phase128/work/p1281_ckpt.jsonl'

wallP = L.Wall(1.1)
PTS = wallP.pts_sub
G_SUB = wallP.kern(PTS)['g']
SCALE = P4.ec_scale(wallP, PTS)
wall = P4.WallNF(1.1)

HINGE = P4.HINGE_Z
RHO_H = P4.HINGE_RHO
HALFA_Z = np.array([1.09396088842477, -0.5286786253298396,
                    -1.4719328625445878, 0.43502659549969874,
                    0.8501116945716124, 0.08238464503952589,
                    -2.1859449891197795, -0.026844566778504827])
HALFA_A, HALFA_LAM, HALFA_RHO = (-0.033678153095735734,
                                 4.640050126789908, 0.04996138256328585)
HALFB_Z = np.array([0.6364774799490114, -0.550546095484792,
                    -1.6603977857177497, 0.7104868883815072,
                    0.87329906344317, 1.7677186914997867,
                    0.016255180150389955, -0.20395940295879322])
HALFB_RHO = 0.04999986064344583


def pi0_of(xi, bc, b2):
    return bc / (2.0 * (2.0 * xi + b2))


def y_to_z(y):
    xi, bc, b2, shape, p1, p2, mu = [float(q) for q in y[:7]]
    return np.array([xi, bc, b2, pi0_of(xi, bc, b2), shape, p1, p2, mu])


def project(z):
    """Closed-form scaled projection (p1194 run record S3 pattern):
    keep (xi, pi0, shape, p1, p2, mu); solve (bc, b2) exactly."""
    xi, bc_h, b2_h, pi0 = z[0], z[1], z[2], z[3]
    a = 1.0 / (2.0 * pi0)
    bc = (bc_h + a * (2.0 * xi + b2_h)) / (1.0 + a * a)
    b2 = a * bc - 2.0 * xi
    zp = np.array(z, dtype=float)
    zp[1], zp[2] = bc, b2
    return zp


def z_to_y(z, A, lam, rho):
    return np.array([z[0], z[1], z[2], z[4], z[5], z[6], z[7],
                     A, lam, rho])


def starts():
    out = []
    zpA = project(HALFA_Z)
    out.append(z_to_y(zpA, HALFA_A, HALFA_LAM, HALFA_RHO))          # 0
    for A, lam in ((0.15, 3.0), (HALFA_A, HALFA_LAM),
                   (-0.15, 3.0), (0.25, 4.5)):
        out.append(z_to_y(HALFB_Z, A, lam, HALFB_RHO))              # 1-4
    zpH = project(HINGE)
    for A, lam in ((0.15, 3.0), (-0.15, 3.0), (0.25, 5.0)):
        out.append(z_to_y(zpH, A, lam, RHO_H))                      # 5-7
    out.append(z_to_y(zpA, 0.15, 3.0, HALFA_RHO))                   # 8
    rng = np.random.default_rng(12811)
    while len(out) < 16:
        xi = float(rng.uniform(0.0, 2.0))
        b2 = float(rng.uniform(-2.0, 2.0))
        s = 2 * xi + b2
        if abs(s) < 0.3:
            continue
        bc = float(rng.uniform(0.1, 3.5)) * (1 if s > 0 else -1)
        pi0 = pi0_of(xi, bc, b2)
        if not (0.05 <= pi0 <= 2.8):
            continue
        out.append(np.array([xi, bc, b2, float(rng.uniform(0.85, 1.15)),
                             float(rng.uniform(-3, 3)),
                             float(rng.uniform(-3, 3)),
                             float(rng.uniform(-3, 3)),
                             float(rng.uniform(-0.35, 0.35)),
                             float(rng.uniform(2.0, 6.0)),
                             float(rng.uniform(0, 0.05))]))         # 9-15
    return out


STARTS = starts()
LO_B = {'pos': np.array([0.0, 0.05, -2.0, 0.85, -3.0, -3.0, -3.0,
                         -0.35, 2.0, 0.0]),
        'neg': np.array([0.0, -4.0, -2.0, 0.85, -3.0, -3.0, -3.0,
                         -0.35, 2.0, 0.0])}
HI_B = {'pos': np.array([5.0, 4.0, 2.0, 1.15, 3.0, 3.0, 3.0,
                         0.35, 6.0, 0.05]),
        'neg': np.array([5.0, -0.05, 2.0, 1.15, 3.0, 3.0, 3.0,
                         0.35, 6.0, 0.05])}


def resid(y):
    xi, bc, b2 = float(y[0]), float(y[1]), float(y[2])
    s = 2.0 * xi + b2
    pi0 = pi0_of(xi, bc, b2) if abs(s) > 1e-12 else 99.0
    z8 = y_to_z(y)
    wall.prof_A, wall.prof_lam = float(y[7]), float(y[8])
    base = P4.residuals_gen(wall, PTS, G_SUB, SCALE, z8,
                            (P4.W_B, float(y[9])))
    # Fixed-shape penalty slots (0.0 when the guard is satisfied):
    # least_squares requires a constant residual length; the
    # half-(b) variable-length form crashes when a trajectory
    # crosses a guard boundary (start 0, first attempt).
    pen = [100.0 * max(0.0, 0.2 - abs(s)),
           100.0 * (max(0.02 - pi0, pi0 - 2.9) + 0.01)
           if not (0.02 <= pi0 <= 2.9) else 0.0]
    return np.concatenate([base, pen])


def anatomy(y):
    """Extra composed-pose anatomy at one configuration."""
    z8 = y_to_z(y)
    wall.prof_A, wall.prof_lam = float(y[7]), float(y[8])
    ct = H.canonical_terms(wall, PTS, z8)
    D = (np.abs(ct['t_kin']) + np.abs(ct['t_pxx'])
         + np.abs(ct['t_FA']) + np.abs(ct['t_FB']))
    imax = int(np.argmax(np.where(D >= H.FLOOR,
                                  np.abs(ct['t_kin'] + ct['t_pxx']
                                         + ct['t_FA'] + ct['t_FB'])
                                  / (D + 1e-12), -1.0)))
    tk, tb, ta = (float(ct['t_kin'][imax]), float(ct['t_FB'][imax]),
                  float(ct['t_FA'][imax]))
    plat = slice(0, 44)
    return dict(
        Hphi_at_pi0=float(-(2 * float(y[0]) + float(y[2])) * float(z8[3])
                          + float(y[1]) / 2.0),
        abs_2xi_b2=float(abs(2 * float(y[0]) + float(y[2]))),
        pi0=float(z8[3]), abs_bc=float(abs(float(y[1]))),
        guards_ok=bool(abs(2 * float(y[0]) + float(y[2])) >= 0.2
                       and 0.02 <= float(z8[3]) <= 2.9
                       and abs(float(y[1])) >= 0.05),
        kin_opposes_FB_at_max=bool(tk * tb < 0),
        tFA_at_max=ta,
        tFA_absmax_plateau=float(np.max(np.abs(ct['t_FA'][plat]))),
        tFA_abs_at_pi0_exact_zero=bool(
            abs(-(2 * float(y[0]) + float(y[2])) * float(z8[3])
                + float(y[1]) / 2.0) < 1e-12),
        max_resid_ties_within_1e9=[int(i) for i in range(56)
                                   if D[i] >= H.FLOOR and abs(
                                       (abs(ct['t_kin'][i] + ct['t_pxx'][i]
                                            + ct['t_FA'][i] + ct['t_FB'][i])
                                        / (D[i] + 1e-12))
                                       - (abs(ct['t_kin'][imax]
                                              + ct['t_pxx'][imax]
                                              + ct['t_FA'][imax]
                                              + ct['t_FB'][imax])
                                          / (D[imax] + 1e-12))) <= 1e-9])


def read_y(y):
    z8 = y_to_z(y)
    wall.prof_A, wall.prof_lam = float(y[7]), float(y[8])
    return P4.full_read(wall, PTS, z8, (P4.W_B, float(y[9]))), z8


def trim(r, z8, y, extra):
    out = dict(z=[float(x) for x in z8], y=[float(x) for x in y],
               A=float(y[7]), lam=float(y[8]), rho0=float(y[9]),
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
               n_plateau_kin_live=r['n_plateau_kin_live'],
               kin_share_former_plateau=r['kin_share_former_plateau'])
    out.update(anatomy(y))
    out.update(extra)
    return out


if LO_I == 0:
    print('SEEDS ' + json.dumps(
        dict(starts=[[float(x) for x in s] for s in STARTS],
             proj_halfA=[float(x) for x in project(HALFA_Z)],
             proj_hinge=[float(x) for x in project(HINGE)])), flush=True)

for i in range(LO_I, min(HI_I, len(STARTS))):
    wall._nf = {}  # bound the WallNF profile-cache growth (OOM guard)
    y0 = STARTS[i]
    br = 'pos' if y0[1] > 0 else 'neg'
    lo, hi = LO_B[br], HI_B[br]
    r_seed, z_seed = read_y(y0)
    seed_rec = trim(r_seed, z_seed, y0, dict(start=i, branch=br,
                                             tag='seed_initial'))
    print('SEED ' + json.dumps(dict(start=i, branch=br,
                                    subset_legal=seed_rec['subset_legal'],
                                    emax=seed_rec['eom_rel_max_nondeg'],
                                    kin_live=seed_rec['n_plateau_kin_live'],
                                    guards_ok=seed_rec['guards_ok'])),
          flush=True)
    y0c = np.clip(y0, lo + 1e-9, hi - 1e-9)
    t0 = time.time()
    try:
        sol = least_squares(resid, y0c, bounds=(lo, hi),
                            xtol=1e-12, ftol=1e-12, max_nfev=150)
        yf = sol.x
    except Exception as ex:  # noqa: BLE001
        rec = dict(start=i, branch=br, error=str(ex), seed=seed_rec)
        with open(CKPT, 'a') as f:
            f.write(json.dumps(rec) + '\n')
        print('RUN ' + json.dumps(dict(start=i, error=str(ex))), flush=True)
        continue
    r, z8 = read_y(yf)
    cost = float(np.sum(resid(yf) ** 2))
    rec = trim(r, z8, yf, dict(start=i, branch=br, cost=cost,
                               seconds=time.time() - t0, seed=seed_rec))
    with open(CKPT, 'a') as f:
        f.write(json.dumps(rec) + '\n')
    print('RUN ' + json.dumps(dict(
        start=i, branch=br, subset_legal=rec['subset_legal'],
        emax=rec['eom_rel_max_nondeg'], emed=rec['eom_rel_med_nondeg'],
        health=rec['health_ok'], frontier=rec['frontier_A'],
        align=rec['alignment_set'], kin_live=rec['n_plateau_kin_live'],
        guards_ok=rec['guards_ok'], abs_bc=rec['abs_bc'],
        cost=cost)), flush=True)
print('DONE', flush=True)
