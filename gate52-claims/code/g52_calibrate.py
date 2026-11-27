#!/usr/bin/env python3
"""
g52_calibrate.py -- Gate-52 calibrations. Run BEFORE any
deciding read; every deciding read is void if a calibration
fails. scipy is imported HERE ONLY (spline cross-check);
the deciding path (g52_lib) never imports it.
Output: gate52/results/g52_calibration.json.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g52_lib as G   # noqa: E402

WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
OUT = f'{WP}/gate52/results/g52_calibration.json'
DT = np.float64
rng = np.random.default_rng(52052)
cal = {}


def rand_pts(n, rlo=10.5, rhi=19.5):
    d = rng.normal(size=(n, 3))
    d /= np.linalg.norm(d, axis=1)[:, None]
    r = rng.uniform(rlo, rhi, n)
    return d * r[:, None]


# ---- CAL-1: gate spline vs scipy CubicSpline (not-a-knot)
from scipy.interpolate import CubicSpline   # noqa: E402
worst = {'v': 0.0, 'd1': 0.0, 'd2': 0.0}
for vec, K in ((G.M2_VS, 9), (G.WIN_VN, 17), (G.A2['vS'], 33),
               (G.M5K17_VS, 17)):
    xk = G.knots(K)
    cs = CubicSpline(xk, vec, bc_type='not-a-knot')
    rr = rng.uniform(10.0, 20.0, 400)
    d, dp, dpp = G.corr(vec, K)(rr)
    worst['v'] = max(worst['v'], float(np.max(np.abs(d - cs(rr)))))
    worst['d1'] = max(worst['d1'],
                      float(np.max(np.abs(dp - cs.derivative(1)(rr)))))
    worst['d2'] = max(worst['d2'],
                      float(np.max(np.abs(dpp - cs.derivative(2)(rr)))))
cal['CAL-1_spline_vs_scipy'] = worst

# ---- CAL-2: jet algebra on an explicit scalar field
# F(x) = sqrt(x^2 + 2 y^2 + z^2 + 1) built from coordinate
# jets by ops; compare v/g/H against the analytic values.
pts = rand_pts(64)
P = len(pts)


def coord_jets(pts):
    out = []
    for i in range(3):
        g = np.zeros((len(pts), 3), dtype=DT)
        g[:, i] = 1.0
        out.append(G.Jet(pts[:, i].copy(), g,
                         np.zeros((len(pts), 3, 3), dtype=DT)))
    return out


xj = coord_jets(pts)
one = G.Jet.const(1.0, P)
F = (xj[0] * xj[0] + (xj[1] * xj[1]).scale(2.0)
     + xj[2] * xj[2] + one).sqrt()
x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
Q = x ** 2 + 2 * y ** 2 + z ** 2 + 1.0
Fv = np.sqrt(Q)
Fg = np.stack([x, 2 * y, z], axis=1) / Fv[:, None]
FH = np.zeros((P, 3, 3))
D = np.array([1.0, 2.0, 1.0])
for i in range(3):
    for j in range(3):
        FH[:, i, j] = (D[i] * (1.0 if i == j else 0.0) / Fv
                       - (D[i] * pts[:, i]) * (D[j] * pts[:, j])
                       / Fv ** 3)
cal['CAL-2_jet_algebra'] = {
    'v': float(np.max(np.abs(F.v - Fv))),
    'g': float(np.max(np.abs(F.g - Fg))),
    'H': float(np.max(np.abs(F.H - FH)))}

# ---- CAL-3: Minkowski (S=0, N=1, M=1) -> That = 0
pts = rand_pts(48)
r = np.linalg.norm(pts, axis=1)
z = np.zeros(len(pts))
o = np.ones(len(pts))
prof = (z, z, z, o, z, z, o, z, z)
Tn, Tr = G.that_cartan(pts, prof)
cal['CAL-3_minkowski_max_abs_That'] = float(
    max(np.max(np.abs(Tn)), np.max(np.abs(Tr))))

# ---- CAL-4: Schwarzschild (m = 0.7) in the ansatz -> That ~ 0
m_s = 0.7
s = 1.0 - 2.0 * m_s / r
sp = 2.0 * m_s / r ** 2
spp = -4.0 * m_s / r ** 3
N = np.sqrt(s)
Np = sp / (2.0 * np.sqrt(s))
Npp = spp / (2.0 * np.sqrt(s)) - sp ** 2 / (4.0 * s ** 1.5)
M = 1.0 / s
Mp = -sp / s ** 2
Mpp = -spp / s ** 2 + 2.0 * sp ** 2 / s ** 3
prof = (z, z, z, N, Np, Npp, M, Mp, Mpp)
Tn, Tr = G.that_cartan(pts, prof)
cal['CAL-4_schwarzschild_max_abs_That'] = float(
    max(np.max(np.abs(Tn)), np.max(np.abs(Tr))))

# ---- CAL-5: tetrad/coframe duality + orthonormality
E, W = G._tetrad_jets(pts, G.config_profiles(r, G.M2_VS, 9))
dual = np.zeros((4, 4))
for a in range(4):
    for b in range(4):
        dual[a, b] = np.max(np.abs(
            sum(W[a][mu].v * E[b][mu].v for mu in range(4))
            - (1.0 if a == b else 0.0)))
profv = G.config_profiles(r, G.M2_VS, 9)
Nv, Mv, Sv = profv[3], profv[6], profv[0]
n = pts / r[:, None]
g = np.zeros((len(pts), 4, 4))
g[:, 0, 0] = -Nv ** 2
g[:, 0, 1] = g[:, 1, 0] = -G.BETA * Sv
gam = np.eye(3)[None] + (Mv - 1.0)[:, None, None] \
    * (n[:, :, None] * n[:, None, :])
g[:, 1:, 1:] = gam
orth = np.zeros((4, 4))
for a in range(4):
    for b in range(4):
        Ea = np.stack([E[a][mu].v for mu in range(4)], axis=1)
        Eb = np.stack([E[b][mu].v for mu in range(4)], axis=1)
        val = np.einsum('pi,pij,pj->p', Ea, g, Eb)
        orth[a, b] = np.max(np.abs(val - G.ETA[a]
                                   * (1.0 if a == b else 0.0)))
cal['CAL-5_duality_max_dev'] = float(np.max(dual))
cal['CAL-5_orthonormality_max_dev'] = float(np.max(orth))

# ---- CAL-6: S=0 Eulerian density vs the closed form
# 16 pi rho = (2/r^2)(1 - 1/M) + 2 M'/(r M^2)   (S = 0)
pts = rand_pts(48)
r = np.linalg.norm(pts, axis=1)
prof = G.config_profiles(r, None, 9)
That = G.that_cartan(pts, prof)[1]
Mv, Mpv = prof[6], prof[7]
rho_cf = ((2.0 / r ** 2) * (1.0 - 1.0 / Mv)
          + 2.0 * Mpv / (r * Mv ** 2)) / (16.0 * np.pi)
cal['CAL-6_rho_closed_form_max_diff'] = float(
    np.max(np.abs(That[:, 0, 0] - rho_cf)))

# ---- CAL-7: worst-null solver
# (i) diagonal tensor: worst null = rho + min p_i exactly
Th = np.diag([0.31, -0.11, 0.05, 0.22]).astype(DT)
res = G.worst_null_certified(Th)
cal['CAL-7_diag'] = {'value': res['worst_null'],
                     'expect': 0.31 - 0.11,
                     'diff': abs(res['worst_null'] - 0.20),
                     'certified': res['certified']}
# (ii) random tensors vs a dense 200k scan
worst_gap = 0.0
cert_all = True
for _ in range(6):
    A = rng.normal(size=(4, 4))
    Th = 0.05 * (A + A.T)
    res = G.worst_null_certified(Th)
    dirs = G.fib_dirs(200000)
    vals = Th[0, 0] + 2.0 * (dirs @ Th[0, 1:]) \
        + np.einsum('ni,ij,nj->n', dirs, Th[1:, 1:], dirs)
    scan = float(np.min(vals))
    worst_gap = max(worst_gap, abs(res['worst_null'] - scan))
    cert_all = cert_all and res['certified'] \
        and res['worst_null'] <= scan + 1e-12
cal['CAL-7_random_vs_dense_scan'] = {
    'max_abs_diff': float(worst_gap), 'certified_all':
    bool(cert_all)}

# ---- CAL-8: profile stack vs stored locals (screen 217)
loc = G.INP['screens412']['217']['local_at_nec_argmin']
rr = np.array([18.170731707317074])
prof = G.config_profiles(rr, G.M2_VS, 9)
names = ('S', 'Sp', 'Spp', 'N', 'Np', 'Npp', 'M', 'Mp', 'Mpp')
cal['CAL-8_profile_locals_screen217'] = {
    nm: float(prof[i][0] - loc[nm])
    for i, nm in enumerate(names)}
# base locals (same screen: N/M are the base's)
prof_b = G.config_profiles(rr, None, 9)
cal['CAL-8_base_locals_screen217'] = {
    nm: float(prof_b[i][0] - loc[nm])
    for i, nm in enumerate(names[3:], start=3)}

# ---- CAL-9: H2 peak value from the totals
h2 = G.h2_totals(np.array([10.0]))
cal['CAL-9_H2_betaS_at_10'] = {
    'value': float(G.BETA * h2[0][0]),
    'stored': G.H2_PEAK_STORED,
    'diff': float(G.BETA * h2[0][0] - G.H2_PEAK_STORED)}
# criterion shape peak (phys row) and its stored value
pr = G.phys_row(G.SHAPEC_CRIT, 9)
cal['CAL-9_criterion_peak'] = {
    'gate_fine': pr['peak_fine'],
    'stored': float(G.INP['conf405']['criterion_peak']),
    'diff': pr['peak_fine']
    - float(G.INP['conf405']['criterion_peak'])}

# ---- CAL-10: frame-rotation orthogonality (A A^T = I) and
# That_reg eigenvalue invariance vs That_nat at Type-I points
pts = rand_pts(48)
r = np.linalg.norm(pts, axis=1)
prof = G.config_profiles(r, G.M2_VS, 9)
E, W = G._tetrad_jets(pts, prof)
n = pts / r[:, None]
gam = np.eye(3)[None] + (prof[6] - 1.0)[:, None, None] \
    * (n[:, :, None] * n[:, None, :])
lam, V = np.linalg.eigh(gam)
W3v = np.transpose(V / np.sqrt(lam)[:, None, :], (0, 2, 1))
T3 = np.zeros((len(pts), 3, 3))
for a in range(3):
    for i in range(3):
        T3[:, a, i] = E[1 + a][1 + i].v
A = np.einsum('pij,pjk,pak->pia', W3v, gam, T3)
cal['CAL-10_rotation_orthogonality'] = float(np.max(np.abs(
    np.einsum('pia,pja->pij', A, A) - np.eye(3)[None])))
Tn, Tr = G.that_cartan(pts, prof)
mn = G.hawking_ellis_margins(Tn)
mr = G.hawking_ellis_margins(Tr)
ti = mn['typeI'] & mr['typeI']
cal['CAL-10_margin_invariance_typeI'] = {
    'n_typeI_both': int(np.sum(ti)),
    'nec_max_diff': float(np.max(np.abs(
        mn['nec'][ti] - mr['nec'][ti]))) if np.any(ti) else None,
    'dec_max_diff': float(np.max(np.abs(
        mn['dec'][ti] - mr['dec'][ti]))) if np.any(ti) else None}

ok = (worst['v'] < 1e-12 and worst['d1'] < 1e-11
      and worst['d2'] < 1e-9
      and cal['CAL-2_jet_algebra']['H'] < 1e-12
      and cal['CAL-3_minkowski_max_abs_That'] < 1e-13
      and cal['CAL-4_schwarzschild_max_abs_That'] < 1e-13
      and cal['CAL-5_duality_max_dev'] < 1e-12
      and cal['CAL-5_orthonormality_max_dev'] < 1e-12
      and cal['CAL-6_rho_closed_form_max_diff'] < 1e-14
      and cal['CAL-7_diag']['diff'] < 1e-10
      and cal['CAL-7_diag']['certified']
      and cal['CAL-7_random_vs_dense_scan']['certified_all']
      and cal['CAL-10_rotation_orthogonality'] < 1e-12
      and cal['CAL-10_margin_invariance_typeI']['nec_max_diff']
      < 1e-15
      and abs(cal['CAL-9_H2_betaS_at_10']['diff']) < 1e-15)
cal['ALL_PASS'] = bool(ok)
with open(OUT, 'w') as f:
    json.dump(cal, f, indent=1)
print(json.dumps(cal, indent=1))
print('ALL_PASS', ok)
