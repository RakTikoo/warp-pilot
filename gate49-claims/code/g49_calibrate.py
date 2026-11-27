#!/usr/bin/env python3
"""
g49_calibrate.py -- Gate-49 calibrations of the FD
machinery, run before any deciding read:
  C-0 trivial limit (flat synthetic profiles -> G = 0)
  C-0b Schwarzschild vacuum in this ansatz -> G = 0
  C-1 worst_null_exact self-test vs brute force
  C-2 h-convergence at C395's stored NEC argmin point
      against the stored worst-null (frame-invariant)
Writes gate49/results/g49_calibration.json.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g49_lib as G  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   '..', 'results', 'g49_calibration.json')
res = {}

rng = np.random.default_rng(49)
dirs = rng.normal(size=(14, 3))
dirs /= np.linalg.norm(dirs, axis=1)[:, None]
radii = np.array([2.0, 3.5, 6.0, 9.0, 12.0, 15.0, 17.0, 19.0,
                  22.0, 25.0, 28.0, 11.0, 14.0, 26.0])
pts = dirs * radii[:, None]

# ---- C-0 trivial limit
fn_flat = lambda P: G.metric_field_synthetic(  # noqa: E731
    lambda r: np.zeros_like(r), lambda r: np.ones_like(r),
    lambda r: np.ones_like(r), P)
Gf = G.einstein_fd(fn_flat, pts, 0.02)
res['C0_trivial_max_abs_G'] = float(np.max(np.abs(Gf)))

# ---- C-0b Schwarzschild (m = 0.7) in this ansatz
m_s = 0.7
fn_sch = lambda P: G.metric_field_synthetic(  # noqa: E731
    lambda r: np.zeros_like(r),
    lambda r: np.sqrt(1.0 - 2.0 * m_s / r),
    lambda r: 1.0 / (1.0 - 2.0 * m_s / r), P)
Gs_h = G.einstein_fd(fn_sch, pts, 0.02)
Gs_h2 = G.einstein_fd(fn_sch, pts, 0.01)
Gs_R = (4.0 * Gs_h2 - Gs_h) / 3.0
res['C0b_schwarzschild_max_abs_G_h02'] = float(np.max(np.abs(Gs_h)))
res['C0b_schwarzschild_max_abs_G_rich'] = float(np.max(np.abs(Gs_R)))
res['C0b_rich_err_indicator'] = float(np.max(np.abs(Gs_h2 - Gs_h)) / 3.0)

# ---- C-1 worst_null_exact self-test
worst = 0.0
for trial in range(30):
    A = rng.normal(size=(4, 4)); A = A + A.T
    q1, q2 = G.worst_null_exact(A)
    d = G._fib_dirs(2002)
    qs = A[0, 0] + 2.0 * (d @ A[0, 1:]) \
        + np.einsum('ni,ij,nj->n', d, A[1:, 1:], d)
    worst = max(worst, abs(q1 - q2), abs(q1 - float(qs.min())))
res['C1_worstnull_selftest_max_dev'] = float(worst)

# ---- C-2 h-convergence at C395's stored argmin point
PT_C395 = np.array([-15.383488301698574, 2.2228398846289754,
                    -2.4277326106594397])
STORED_WN = -3.0896210095678075e-05
STORED_NEC = -2.9809850277749006e-05
conv = []
for h in (0.16, 0.08, 0.04, 0.02, 0.01):
    That, err = G.that_at(G.C395, G.HOME, PT_C395, h=h)
    qf, qsc = G.worst_null_exact(That)
    mm = G.margins(That[None])
    conv.append({'h': h, 'worst_null': qf, 'scan': qsc,
                 'diff_vs_stored': qf - STORED_WN,
                 'nec_margin': float(mm['nec'][0]),
                 'nec_diff_vs_stored': float(mm['nec'][0]) - STORED_NEC,
                 'typeI': bool(mm['typeI'][0]),
                 'rho_euler': float(That[0, 0]),
                 'fd_err': err})
res['C2_h_convergence_C395_argmin'] = conv
res['C2_stored'] = {'worst_null': STORED_WN, 'nec': STORED_NEC,
                    'point': PT_C395.tolist()}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
