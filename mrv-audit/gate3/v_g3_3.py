#!/usr/bin/env python3
"""
Gate-3 worker V3 (VERIFICATION) -- fresh code, float64 only.

Sub-tasks:
 (1a) Odd sector: rebuild the odd-sector effective potential independently
      (geometric formula for V on A=B=1, F=G=H=1 background) and check
      V_eff > 0 for l>=2, min ~ 0.00159 at r=-60 for l=2, no bound states
      (own eigenvalue route: LAPACK tridiagonal solve, two grids).
 (1b) l=0 lowest mode: coefficient VALUES taken as DATA from
      phase4/results/p42b_ell0_indep.json (corrected, independent F4-2b
      values, covariant normalisation) -- the eigenvalue solve is my own:
      a linear finite-element Galerkin discretisation (different from
      F4-3's flux-form sparse shift-invert).  Coefficients are interpolated
      through their smooth reduced forms q_C(r) = C(r) * D(r)^2
      (C = K0, G0, M0), with D(r) = 2 J J' + Xi pi' computed from the
      shared designer definitions; q_C is finite and smooth across the
      D=0 pole at r* = 1.7724, whereas C itself blows up like 1/D^2.
      Two mesh resolutions; convergence reported.
 (2)  GW speed spot (G3-3 on-background half): from the designer functions
      of phase3/p31_horndeski.py (shared definitions ONLY), compute the
      odd-sector calF, calG at radii out to |r| = 1e4 and check
      c_T^2 = calG/calF = 1 at the roundoff floor.

NOT imported: phase4/p43_tachyon.py, phase4/p45_asymptotics.py machinery.
Imported: phase3/p31_horndeski.py designer functions only (per protocol).
"""
import json
import sys

import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.sparse import diags as sp_diags
from scipy.sparse.linalg import eigsh

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
import p31_horndeski as p31  # shared designer definitions only

TAU = 10.0
OUT = '/home/hatch/workspace/warp-pilot/gate3/results/v_g3_3.json'
res = {'worker': 'V3 gate3', 'float': 'float64 throughout'}

# ============================================================================
# (1a) ODD SECTOR -- independent rebuild
# ============================================================================
# Background geometry (analytic): J = sqrt(r^2+tau^2), A = B = 1.
# Odd-sector master equation (MRV eq. 25 specialised to calF=calG=calH=1,
# A=B=1, tortoise coordinate = r itself):
#   -psi'' + V_eff psi = om^2 psi,
#   V_eff = l(l+1)/J^2 + V,
#   V = (1/J) * d/dr[ J' ] ... evaluated here from the geometric combination
#   V = 2 J'^2/J^2 - 2 J''/J - 2/J^2   (the form coded independently below;
#   its closed-form reduction -4 tau^2 / J^4 is checked, not assumed).
def odd_V(r):
    J = np.sqrt(r**2 + TAU**2)
    Jp = r / J
    Jpp = TAU**2 / J**3
    return 2.0 * Jp**2 / J**2 - 2.0 * Jpp / J - 2.0 / J**2

r_box = np.linspace(-60.0, 60.0, 12001)
J_box = np.sqrt(r_box**2 + TAU**2)
V_box = odd_V(r_box)
odd = {}
odd['V_closed_form_max_dev_vs_-4tau2/J4'] = float(
    np.max(np.abs(V_box + 4.0 * TAU**2 / J_box**4)))
odd['per_ell'] = {}
for ell in (2, 3, 5, 10):
    Veff = ell * (ell + 1) / J_box**2 + V_box
    i = int(np.argmin(Veff))
    odd['per_ell'][f'ell{ell}'] = dict(
        Veff_min=float(Veff[i]), Veff_min_r=float(r_box[i]),
        Veff_positive_everywhere=bool(np.all(Veff > 0)))

# Bound-state check: -psi'' + Veff psi = om^2 psi, Dirichlet on [-60,60],
# uniform-grid 3-point Laplacian solved with LAPACK's tridiagonal solver
# (eigh_tridiagonal) -- a different route from F4-3's sparse shift-invert.
def odd_lowest(ell, N):
    r = np.linspace(-60.0, 60.0, N)
    h = r[1] - r[0]
    J = np.sqrt(r**2 + TAU**2)
    Veff = ell * (ell + 1) / J**2 + odd_V(r)
    diag = 2.0 / h**2 + Veff[1:-1]
    off = -np.ones(N - 3) / h**2
    w = eigh_tridiagonal(diag, off, eigvals_only=True,
                         select='i', select_range=(0, 5))
    return w

odd_eigs = {}
for N in (2401, 4801):
    w = odd_lowest(2, N)
    odd_eigs[f'N{N}'] = [float(x) for x in w]
odd['ell2_lowest_eigs_two_grids'] = odd_eigs
odd['ell2_lowest_om2_grid_change'] = float(
    abs(odd_eigs['N4801'][0] - odd_eigs['N2401'][0]))
odd['no_bound_states_ell2'] = bool(odd_eigs['N4801'][0] > 0)
odd['target'] = 'Veff_min(ell=2) = 0.00159 at r=-60; no bound states'
m2 = odd['per_ell']['ell2']['Veff_min']
odd['verdict'] = ('REPRODUCED' if (odd['per_ell']['ell2']['Veff_positive_everywhere']
                  and abs(m2 - 0.00159) < 5e-6 and odd['no_bound_states_ell2'])
                  else 'FAILS')
res['task1a_odd_sector'] = odd

# ============================================================================
# (1b) l=0 LOWEST MODE -- FEM Galerkin solve on F4-2b coefficient DATA
# ============================================================================
with open('/home/hatch/workspace/warp-pilot/phase4/results/p42b_ell0_indep.json') as fh:
    p42b = json.load(fh)
prof = p42b['profile']
rs = np.array(sorted((float(k) for k in prof)))
K_dat = np.array([prof[f'{r:.1f}']['K0'] for r in rs])
G_dat = np.array([prof[f'{r:.1f}']['G0'] for r in rs])
M_dat = np.array([prof[f'{r:.1f}']['M0'] for r in rs])
D_dat = np.array([prof[f'{r:.1f}']['D'] for r in rs])

ell0 = {'data_source': 'phase4/results/p42b_ell0_indep.json profile (31 radii), '
                       'covariant normalisation; K0>0 at all data points: '
                       + str(bool(np.all(K_dat > 0)))}
ell0['K0_min_data'] = float(np.min(K_dat))
ell0['K0_positive_all_data_points'] = bool(np.all(K_dat > 0))
ell0['G0_positive_all_data_points'] = bool(np.all(G_dat > 0))

# D(r) analytic from shared designer definitions; check vs data D values.
dd = p31.theory_on_bg(rs)
Xi_dat, _ = p31.Xi_Gamma(dd)
D_ana_dat = 2.0 * dd['J'] * dd['Jp'] + Xi_dat * dd['pip']
ell0['D_analytic_vs_data_max_rel_dev'] = float(
    np.max(np.abs(D_ana_dat - D_dat) / np.maximum(np.abs(D_dat), 1e-12)))

def D_of_r(r):
    d = p31.theory_on_bg(np.atleast_1d(np.asarray(r, dtype=np.float64)))
    Xi, _ = p31.Xi_Gamma(d)
    return 2.0 * d['J'] * d['Jp'] + Xi * d['pip']

# Smooth reduced coefficients q_C = C * D^2 (finite across the pole).
# Interpolation scheme: natural cubic spline.  (A monotone PCHIP pass was
# tried first and REJECTED on a recorded diagnostic: PCHIP's flattened
# slopes at data extrema corrupt the derivative-sensitive Liouville
# potential built from these coefficients -- V(0.5) = 0.60 vs F4-3's 0.84,
# V(-0.5) = 0.43 vs 0.26 -- while the cubic spline reproduces F4-3's
# V samples to ~1%: V(0.5) = 0.832, V(1) = 2.264, V(-0.5) = 0.262,
# V(5) = 0.084, V(20) = 0.0073.  See results JSON, interp_diagnostic.)
from scipy.interpolate import CubicSpline
qK = CubicSpline(rs, K_dat * D_dat**2)
qG = CubicSpline(rs, G_dat * D_dat**2)
qM = CubicSpline(rs, M_dat * D_dat**2)
ell0['qK_min_on_data'] = float(np.min(K_dat * D_dat**2))
ell0['qG_min_on_data'] = float(np.min(G_dat * D_dat**2))

def coeffs(r):
    # qK, qG are floored at 0: the spline overshoots to ~-1e-5 in
    # |r| < 0.01 where the true q ~ r^2 vanishes; the flooring changes
    # no eigenvalue at the 1e-7 level (checked).
    D = D_of_r(r)
    inv = 1.0 / D**2
    return (np.maximum(qK(r), 0.0) * inv, np.maximum(qG(r), 0.0) * inv,
            qM(r) * inv)

# sanity: interpolation reproduces the data at the nodes exactly
Kn, Gn, Mn = coeffs(rs)
ell0['interp_node_max_rel_dev_K0'] = float(np.max(np.abs(Kn - K_dat) / K_dat))
ell0['interp_node_max_rel_dev_G0'] = float(np.max(np.abs(Gn - G_dat) / G_dat))
ell0['interp_node_max_abs_dev_M0'] = float(np.max(np.abs(Mn - M_dat)))

# Positivity of the interpolated coefficients on a fine grid, and the
# Liouville-potential diagnostic against F4-3's published V samples.
_rf = np.linspace(-60.0, 60.0, 24001)
_Kf, _Gf, _Mf = coeffs(_rf)
ell0['interp_K0_min_fine_grid'] = float(np.min(_Kf))
ell0['interp_G0_min_fine_grid'] = float(np.min(_Gf))
ell0['interp_K0_positive_fine_grid'] = bool(np.all(_Kf > 0))
ell0['interp_G0_positive_fine_grid'] = bool(np.all(_Gf > 0))
_rv = np.linspace(-30.0, 30.0, 6001)
_Kv, _Gv, _Mv = coeffs(_rv)
_Lv = np.log(np.sqrt(_Kv * _Gv))
_fac = np.sqrt(_Gv / _Kv)
_Lrho = _fac * np.gradient(_Lv, _rv)
_Vl = _Mv / _Kv + 0.5 * _fac * np.gradient(_Lrho, _rv) + 0.25 * _Lrho**2
ell0['interp_diagnostic'] = {
    'method': 'Liouville V from the interpolated coefficients vs F4-3 V samples',
    'V_samples_mine': {f'r={rr:g}': float(_Vl[np.argmin(np.abs(_rv - rr))])
                       for rr in (-5, -1, -0.5, 0.5, 1.0, 3, 5, 20)},
    'V_samples_F43': {'r=-5': -0.0016685018600028638, 'r=-1': 0.17298025481214196,
                      'r=-0.5': 0.2630553123627415, 'r=0.5': 0.8412875048441331,
                      'r=1': 2.2694958580197273, 'r=3': 0.7562330581548916,
                      'r=5': 0.08398620455463687, 'r=20': 0.007429552326386509},
}

# --- linear FEM Galerkin:  -(G chi')' + M chi = om^2 K chi, Dirichlet box.
BREAKS = [-60.0, -20.0, -8.0, -3.0, -1.0, -0.3, 0.0, 0.3, 1.0, 1.45,
          1.68, 1.87, 2.1, 3.0, 8.0, 20.0, 60.0]
COUNTS = [10, 12, 15, 14, 12, 10, 10, 14, 10, 8, 8, 10, 15, 12, 10]  # per segment, scale 1

def build_mesh(scale):
    nodes = [BREAKS[0]]
    for a, b, n in zip(BREAKS[:-1], BREAKS[1:], COUNTS):
        seg = np.linspace(a, b, n * scale + 1)[1:]
        nodes.extend(seg.tolist())
    return np.array(nodes)

_GX, _GW = np.polynomial.legendre.leggauss(3)  # 3-pt Gauss on [-1,1]

def fem_solve(nodes):
    n = len(nodes)
    nn = n - 2  # interior unknowns
    A = np.zeros((nn, nn))
    B = np.zeros((nn, nn))
    for e in range(n - 1):
        a, b = nodes[e], nodes[e + 1]
        h = b - a
        xq = 0.5 * (a + b) + 0.5 * h * _GX
        wq = 0.5 * h * _GW
        Kq, Gq, Mq = coeffs(xq)
        # local shape values/derivatives at quad points
        N0 = (b - xq) / h
        N1 = (xq - a) / h
        dN = np.array([-1.0 / h, 1.0 / h])
        Ke = np.zeros((2, 2)); Be = np.zeros((2, 2))
        for qi in range(3):
            Ke += wq[qi] * (Gq[qi] * np.outer(dN, dN)
                            + Mq[qi] * np.outer([N0[qi], N1[qi]], [N0[qi], N1[qi]]))
            Be += wq[qi] * Kq[qi] * np.outer([N0[qi], N1[qi]], [N0[qi], N1[qi]])
        for i in range(2):
            for j in range(2):
                gi, gj = e + i - 1, e + j - 1
                if 0 <= gi < nn and 0 <= gj < nn:
                    A[gi, gj] += Ke[i, j]
                    B[gi, gj] += Be[i, j]
    return A, B

def fem_lowest(scale, k=6):
    nodes = build_mesh(scale)
    A, B = fem_solve(nodes)
    from scipy.sparse import csr_matrix
    vals, vecs = eigsh(csr_matrix(A), M=csr_matrix(B), k=k, sigma=0.0,
                       which='LM', tol=1e-10)
    order = np.argsort(vals)
    return nodes, vals[order], vecs[:, order]

ell0_runs = {}
vecs_by_scale = {}
for scale in (1, 2, 3):
    nodes, vals, vecs = fem_lowest(scale)
    ell0_runs[f'scale{scale}'] = dict(
        n_nodes=int(len(nodes)), n_interior=int(len(nodes) - 2),
        lowest_om2=[float(x) for x in vals])
    vecs_by_scale[scale] = (nodes, vals, vecs)
ell0['fem_runs'] = ell0_runs
w1 = ell0_runs['scale2']['lowest_om2'][0]
w2 = ell0_runs['scale3']['lowest_om2'][0]
ell0['lowest_om2_change_finest_two'] = float(abs(w2 - w1))
ell0['lowest_om2_rel_change_finest_two'] = float(abs(w2 - w1) / abs(w2)) if w2 != 0 else None

# Localisation of the lowest mode (finest mesh): K-weighted norm fractions.
nodes, vals, vecs = vecs_by_scale[3]
chi = np.zeros(len(nodes)); chi[1:-1] = vecs[:, 0]
rstar = 1.772437990426927
frac = {}
tot = 0.0; reg = {'pocket_0_to_rstar': 0.0, 'abs_r_lt_2': 0.0, 'abs_r_gt_10': 0.0}
for e in range(len(nodes) - 1):
    a, b = nodes[e], nodes[e + 1]
    h = b - a
    xq = 0.5 * (a + b) + 0.5 * h * _GX
    wq = 0.5 * h * _GW
    Kq, _, _ = coeffs(xq)
    cq = chi[e] * (b - xq) / h + chi[e + 1] * (xq - a) / h
    dens = float(np.sum(wq * Kq * cq**2))
    tot += dens
    mid = 0.5 * (a + b)
    if 0.0 < mid < rstar: reg['pocket_0_to_rstar'] += dens
    if abs(mid) < 2.0: reg['abs_r_lt_2'] += dens
    if abs(mid) > 10.0: reg['abs_r_gt_10'] += dens
frac = {k: float(v / tot) for k, v in reg.items()}
ell0['lowest_mode_norm_fractions'] = frac
ell0['lowest_mode_peak_r'] = float(nodes[int(np.argmax(np.abs(chi)))])
# --- FEM solver validation on the odd sector (same code path, K=G=1,
# M = V_eff(l=2)): must return the known box value ~ +0.008254.
def _odd_coeffs(r):
    r = np.asarray(r, dtype=np.float64)
    J = np.sqrt(r**2 + TAU**2)
    return np.ones_like(r), np.ones_like(r), 6.0 / J**2 + odd_V(r)
_nodes_v = build_mesh(2)
import scipy.sparse as _sp
def _fem_lowest_with(coeff_fn, nodes, k=4):
    n = len(nodes); nn = n - 2
    A = np.zeros((nn, nn)); B = np.zeros((nn, nn))
    for e in range(n - 1):
        a, b = nodes[e], nodes[e + 1]; h = b - a
        xq = 0.5 * (a + b) + 0.5 * h * _GX; wq = 0.5 * h * _GW
        Kq, Gq, Mq = coeff_fn(xq)
        N0 = (b - xq) / h; N1 = (xq - a) / h
        dN = np.array([-1.0 / h, 1.0 / h])
        Ke = np.zeros((2, 2)); Be = np.zeros((2, 2))
        for qi in range(3):
            Ke += wq[qi] * (Gq[qi] * np.outer(dN, dN)
                            + Mq[qi] * np.outer([N0[qi], N1[qi]], [N0[qi], N1[qi]]))
            Be += wq[qi] * Kq[qi] * np.outer([N0[qi], N1[qi]], [N0[qi], N1[qi]])
        for i in range(2):
            for j in range(2):
                gi, gj = e + i - 1, e + j - 1
                if 0 <= gi < nn and 0 <= gj < nn:
                    A[gi, gj] += Ke[i, j]; B[gi, gj] += Be[i, j]
    vals = eigsh(_sp.csr_matrix(A), M=_sp.csr_matrix(B), k=k, sigma=0.0,
                 which='LM', tol=1e-10)[0]
    return np.sort(vals)
ell0['fem_validation_odd_ell2_lowest'] = float(_fem_lowest_with(_odd_coeffs, _nodes_v)[0])
ell0['fem_validation_target'] = 0.008254

# --- Anatomy of the outcome.
_Kedge, _, _Medge = coeffs(np.array([-60.0, 60.0]))
ell0['continuum_threshold_M0_over_K0_at_box_edges'] = [
    float(_Medge[0] / _Kedge[0]), float(_Medge[1] / _Kedge[1])]
ell0['anatomy'] = (
    'The FEM solve is mesh-converged (lowest om2 = +0.004474 / +0.004468 / '
    '+0.004468 at scales 1/2/3, rel. change 2e-4 between the finest two) and '
    'the solver is validated on the odd sector (0.008290 vs the known '
    '0.008254).  No negative eigenvalue exists in the discretised problem '
    'under ANY interpolation of the data tried (PCHIP on q: +0.004486; '
    'cubic spline on q: +0.004468; Akima: same continuum edge), so the '
    'SIGN content of the claim (no l=0 tachyon; lowest om2 > 0) is '
    'consistent with this path.  But the claimed near-zero throat-localised '
    'mode at +0.00021 does NOT appear: the lowest mode found is a '
    'box-continuum mode (peak at r = -28, 98% of its K0-weighted norm at '
    '|r| > 10), at +0.00447 -- coincident with F4-3\'s SECOND eigenvalue '
    '(+0.00445).  The claimed mode is a near-threshold bound state: its '
    'om2 = +0.00021 sits only ~5e-5 below the continuum threshold '
    'M0/K0 -> ~2.6e-4 at large |r|, so its binding energy (~5e-5) is far '
    'below the interpolation uncertainty of the 31-point coefficient data '
    'allowed as input here (F4-3\'s own dense-coefficient solve moved '
    '0.00075 -> 0.00021 between h = 0.02 and h = 0.01).  MISSING PIECE: '
    'dense corrected coefficient profiles (K0, G0, M0 on a fine grid from '
    'the F4-2b from-action route, or F4-2\'s dense corrected profiles) -- '
    'with those, this same FEM path can settle the value.')
ell0['target'] = 'lowest om2 POSITIVE, ~ +0.00021 (accept within factor 2), throat-localised'
ok_sign = w2 > 0
ok_val = ok_sign and (0.5 * 0.00021 <= w2 <= 2.0 * 0.00021)
ell0['verdict'] = 'REPRODUCED' if ok_val else ('NOT YET' if ok_sign else 'FAILS')
ell0['verdict_note'] = (f'finest-mesh lowest om2 = {w2:+.6f}; sign positive: {ok_sign}; '
                        f'within factor 2 of +0.00021: {ok_val}; the +0.00021 '
                        'throat-localised mode itself is not reproduced from '
                        'the 31-point data -- see anatomy (NOT YET, missing '
                        'piece = dense corrected coefficient profiles)')
res['task1b_ell0_lowest_mode'] = ell0

# ============================================================================
# (2) GW SPEED SPOT -- calF, calG from designer functions to |r| = 1e4
# ============================================================================
def calFG(r):
    r = np.atleast_1d(np.asarray(r, dtype=np.float64))
    s = p31.s_of_r(r)
    J = np.sqrt(r**2 + TAU**2)
    pip = TAU / J
    pip2 = pip**2
    g40 = p31.g40_s(s); g41 = p31.g41_s(s)
    f40 = p31.f40_s(s); f41 = p31.f41_s(s)
    calF = 1.0 + 2.0 * g40 - g41 * pip2
    calG = 1.0 + 2.0 * g40 + g41 * pip2 + 2.0 * f40 * pip2**2 - f41 * pip2**3
    return calF, calG

gw = {}
for sign, tag in ((1.0, 'pos'), (-1.0, 'neg')):
    rr = sign * np.concatenate(([1.0, 2.0, 5.0], np.logspace(1, 4, 121)))
    cF, cG = calFG(rr)
    cT2 = cG / cF
    cT = np.sqrt(cT2)
    gw[tag] = dict(
        max_abs_cT_minus_1=float(np.max(np.abs(cT - 1.0))),
        max_abs_cT2_minus_1=float(np.max(np.abs(cT2 - 1.0))),
        max_abs_calF_minus_1=float(np.max(np.abs(cF - 1.0))),
        max_abs_calG_minus_1=float(np.max(np.abs(cG - 1.0))),
        cT_at_abs1e4=float(cT[-1]), r_max=1e4)
    gw[tag]['worst_r'] = float(rr[int(np.argmax(np.abs(cT - 1.0)))])
gw['target'] = 'max |cT - 1| ~ 7.8e-16 class (<= ~1e-15), F4-5'
gw_max = max(gw['pos']['max_abs_cT_minus_1'], gw['neg']['max_abs_cT_minus_1'])
gw['verdict'] = 'REPRODUCED' if gw_max <= 2e-15 else 'FAILS'
res['task2_gw_speed'] = gw

res['verdicts'] = {
    'task1a_odd_sector': odd['verdict'],
    'task1b_ell0_lowest_mode': ell0['verdict'],
    'task2_gw_speed': gw['verdict'],
}
with open(OUT, 'w') as fh:
    json.dump(res, fh, indent=2)
print(json.dumps(res, fh if False else None, indent=2) if False else json.dumps(res, indent=2))
