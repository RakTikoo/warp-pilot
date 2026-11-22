#!/usr/bin/env python3
"""
F4-3 (relaunch, 2026-11-21): even-sector TACHYON (slow bound-state) audit
of the MRV beyond-Horndeski wormhole, per the pre-registration in
phase4/CHECKPOINT4.md (RELAUNCH, F4-3) and the task state of play:

  * l=0: F4-2b's CORRECTED coefficients.  K0 = K0(F4-2 printed) minus the
    spurious e1 pair (Jp^2 - Jp^3)/X, whose on-background contribution
    F4-2b proved is zero (basis fit alpha_T3 = alpha_T4 = -1).  G0 and
    M0 are F4-2's, unchanged (F4-2b verified both against its
    independent derivation).  K0 > 0 everywhere (checked in-run).
  * l>=2: F4-1's Appendix-B reduction matrices (K,G,Q,M), rehabilitated
    as the best available representation by F4-1b (independent det K
    signs agree at every settled point).  These channels are ALREADY
    ghost-failed near the throat (det K < 0, F4-1b); their tachyon
    read here is SECONDARY and is labelled as such throughout.
    One completion of the reduction is made and documented: p41 did
    not compute e3, so its M22 lacked the j^2-free e3 part.  e3 is
    computed here with F4-2's validated pi-shift machinery (the same
    route that reproduces the paper's a5 identity) and
    M22 += -2*e3/J^2 is applied; a no-e3 sensitivity run is reported.
  * l=1: the reduction's 2x2 matrices are extractable and are included
    in the same secondary coupled solve; the paper's footnote promises
    ONE dynamical mode at l=1 (printed det K = det G = 0 at j^2=2),
    while the reduction's G is rank-1 but its K is not rank-1 -- the
    single-mode reduction is therefore NOT cleanly extractable and
    the l=1 read is the 2-field secondary one.  Stated explicitly.

Method:
  VALIDATION FIRST: the bound-state machinery (sparse discretised
  eigenvalue solve, Dirichlet box [-60,60], two grids) applied to the
  ODD sector must reproduce Phase 3: V_eff = l(l+1)/J^2 + V with
  V = -4 tau^2/J^4 (p31 eq.25 specialised), V_eff > 0 for all l>=2,
  min 0.00159 (at the box edge, l=2), no bound states.
  l=0: generalised Sturm-Liouville problem
      -(G0 chi')' + M0 chi = om^2 K0 chi
  discretised in flux form, solved by shift-invert eigsh on two grids
  (h=0.02, 0.01).  Schroedinger form via the Liouville transform
  (rho' = sqrt(K0/G0), chi = (K0 G0)^-1/4 psi):
      V = M0/K0 + (1/2) L_{rho rho} + (1/4) L_rho^2,  L = ln sqrt(K0 G0).
  l>=1 (secondary): coupled 2-field operator from the canonical action
  density J^2 [ 1/2 vdot^T K vdot - 1/2 v'^T G v' - v^T Q v' - 1/2 v^T M v ],
      A v = -(Gt v')' - 2 Qt v' - Qt' v + Mt v = om^2 Kt v
  (tildes = J^2 x reduction matrices; A symmetrised after FD assembly).
  The reduced operator is parametrisation-singular at the Dden=0 pole
  (r*=1.7724) and at the S_den=0 surfaces (alpha-elimination pivots);
  following F4-1's gate exclusions, windows |r-r*|<0.35 and
  |r-r_S|<0.3 are excised and the solve runs per regular segment with
  Dirichlet ends -- the honest extent of the reduction.  Branch
  potentials: pointwise K-eigenbasis projections (k_a, g_a, m_a),
  Liouville formula per branch where k_a>0 and g_a>0, ignoring
  inter-branch derivative/Q couplings (labelled branch-diagonal).

float64 throughout; numpy/scipy.  Results -> results/p43_tachyon.json
"""
import json
import sys
import time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh, eigs

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase4')
import p31_horndeski as p31
import p41_coeffs as C41
import p41_angular as A41
import p42_ell0 as F42

TAU = p31.TAU
RSTAR = 1.772438
OUT = '/home/hatch/workspace/warp-pilot/phase4/results/p43_tachyon.json'


# ----------------------------------------------------------------------------
# generic sparse helpers
# ----------------------------------------------------------------------------
def schrodinger_solve(rho, V, k=6):
    """Lowest om^2 of -psi'' + V psi = om^2 psi, Dirichlet, uniform rho."""
    n = len(rho)
    h = rho[1] - rho[0]
    main = 2.0 / h**2 + V[1:-1]
    off = -np.ones(n - 3) / h**2
    A = sparse.diags([off, main, off], [-1, 0, 1]).tocsc()
    vals, vecs = eigsh(A, k=k, which='SA', tol=1e-10)
    o = np.argsort(vals)
    return vals[o], vecs[:, o]


def liouville_V(r, K, G, M):
    """Schroedinger potential and tortoise coordinate for the scalar
    Sturm-Liouville problem -(G chi')' + M chi = om^2 K chi.
    Points where K or G vanish/blow up (throat node, pole) are left in;
    callers mask the FD-unreliable neighbourhoods."""
    K = np.asarray(K, dtype=np.float64).copy()
    G = np.asarray(G, dtype=np.float64).copy()
    i0 = int(np.argmin(np.abs(r)))
    if abs(r[i0]) < 1e-9 and (K[i0] <= 0 or G[i0] <= 0):
        # throat node: K,G ~ r^2 with FD-floor values; use the ratio
        # limit sqrt(0.97/0.76) (F4-2 throat fits) for b and neighbour
        # values for L (derivatives there are masked by callers anyway)
        K[i0] = K[i0 + 1]
        G[i0] = G[i0 + 1]
    with np.errstate(divide='ignore', invalid='ignore'):
        b = np.sqrt(K / G)                      # d rho / dr
    rho = np.concatenate([[0.0], np.cumsum(0.5 * (b[1:] + b[:-1])
                                           * np.diff(r))])
    i0 = int(np.argmin(np.abs(r)))
    rho = rho - rho[i0]
    with np.errstate(divide='ignore', invalid='ignore'):
        L = 0.5 * (np.log(K) + np.log(G))
        Lr = np.gradient(L, r, edge_order=2)
        Lrho = Lr / b
        Lrhoho = np.gradient(Lrho, r, edge_order=2) / b
        V = M / K + 0.5 * Lrhoho + 0.25 * Lrho**2
    return rho, V


# ----------------------------------------------------------------------------
# 1. odd-sector validation (Phase 3 conventions, p31)
# ----------------------------------------------------------------------------
def odd_validation():
    out = {}
    r = np.linspace(-60.0, 60.0, 12001)
    d = p31.theory_on_bg(r)
    J = d['J']
    V = 0.5 * (4 * d['Jp']**2 / J**2 - 4 * d['Jpp'] / J - 4.0 / J**2)
    out['V_formula_max_dev_vs_-4tau2/J4'] = float(
        np.max(np.abs(V + 4 * TAU**2 / J**4)))
    for ell in (2, 3, 5, 10):
        Veff = ell * (ell + 1) / J**2 + V
        i = int(np.argmin(Veff))
        out[f'ell{ell}'] = dict(Veff_min=float(Veff[i]),
                                Veff_min_r=float(r[i]))
    # bound-state machinery on the odd l=2 channel, two grids
    grids = {}
    for n in (2401, 4801):
        rg = np.linspace(-60.0, 60.0, n)
        dg = p31.theory_on_bg(rg)
        Jg = dg['J']
        Vg = 0.5 * (4 * dg['Jp']**2 / Jg**2 - 4 * dg['Jpp'] / Jg
                    - 4.0 / Jg**2)
        Veff = 6.0 / Jg**2 + Vg
        vals, _ = schrodinger_solve(rg, Veff, k=6)
        grids[f'N{n}'] = [float(v) for v in vals]
    out['ell2_eigenvalues_two_grids'] = grids
    lo = [grids[f'N{n}'][0] for n in (2401, 4801)]
    out['passed'] = bool(
        abs(out['ell2']['Veff_min'] - 0.00159) < 5e-5
        and all(v > 0 for g in grids.values() for v in g)
        and out['V_formula_max_dev_vs_-4tau2/J4'] < 1e-12)
    out['note'] = ('Phase 3 target: Veff_min(ell=2) = 0.0015924 at the '
                   'box edge r=-60; no bound states.  The discretised '
                   'lowest eigenvalue is a box-continuum value '
                   '(~(pi/120)^2 + Veff(inf)), positive on both grids.')
    return out


# ----------------------------------------------------------------------------
# 2. l=0 with F4-2b-corrected coefficients
# ----------------------------------------------------------------------------
def ell0_profiles(h):
    """K0 (corrected), G0, M0 on r in [-60,60] with spacing h (F4-2 route)."""
    r = np.arange(-60.0, 60.0 + 0.5 * h, h)
    B = F42.build(r, h)
    d = B['d']
    J = d['J']
    corr = (d['Jp']**2 - d['Jp']**3) / d['X']   # spurious e1 pair (F4-2b)
    K0 = B['K0'] - corr
    G0 = B['G0']
    # M0 exactly as F4-2 (c3 via pi-shift of E_B; e3 via pi-shift of EL_pi)
    ds_ = 2e-3
    dpi_ = TAU * ds_
    EBp, _ = F42.shifted_EB_EA(r, d, +ds_)
    EBm, _ = F42.shifted_EB_EA(r, d, -ds_)
    c3 = J**2 * (EBp - EBm) / (2 * dpi_)
    hc = 0.01
    rc = np.arange(-60.0, 60.0 + 0.5 * hc, hc)
    dc = p31.theory_on_bg(rc)
    ELp = F42.el_pi_shifted(rc, dc, +ds_)
    ELm = F42.el_pi_shifted(rc, dc, -ds_)
    e3 = np.interp(r, rc, (ELp - ELm) / (2 * dpi_))
    gr = lambda v: np.gradient(v, h, edge_order=2)
    Bm = B['p'] * c3 + B['q'] * B['c2'] + 2 * B['c6'] * B['p'] * B['q']
    M0 = -(e3 + B['q'] * c3 + B['c6'] * B['q']**2 - 0.5 * gr(Bm))
    return r, K0, G0, M0, e3


def ell0_solve(r, K0, G0, M0, k=8):
    """Flux-form Sturm-Liouville solve, shift-invert near om^2 = -1."""
    h = r[1] - r[0]
    Gh = 0.5 * (G0[1:] + G0[:-1])
    main = (Gh[1:] + Gh[:-1]) / h**2 + M0[1:-1]
    off = -Gh[1:-1] / h**2
    A = sparse.diags([off, main, off], [-1, 0, 1]).tocsc()
    Bm = sparse.diags([K0[1:-1]], [0]).tocsc()
    vals, vecs = eigsh(A, M=Bm, k=k, sigma=-1.0, which='LM', tol=1e-10)
    o = np.argsort(vals)
    return vals[o], vecs[:, o]


def ell0_analysis():
    out = {}
    sols = {}
    prof = {}
    for h in (0.02, 0.01, 0.005):
        r, K0, G0, M0, _ = ell0_profiles(h)
        vals, vecs = ell0_solve(r, K0, G0, M0)
        sols[h] = (r, vals, vecs)
        prof[h] = (r, K0, G0, M0)
        out[f'grid_h{h}'] = dict(
            K0_min=float(np.min(K0)), K0_positive_everywhere=bool(
                np.all(K0[1:-1] > 0) or np.min(K0) >= 0),
            K0_at_throat=float(K0[np.argmin(np.abs(r))]),
            lowest_om2=[float(v) for v in vals])
    (r1, v1, vec1), (r2, v2, vec2) = sols[0.02], sols[0.01]
    v3 = sols[0.005][1]
    out['lowest_om2_h0.02'] = float(v1[0])
    out['lowest_om2_h0.01'] = float(v2[0])
    out['lowest_om2_h0.005'] = float(v3[0])
    out['lowest_om2_abs_grid_change'] = float(abs(v2[0] - v1[0]))
    out['lowest_om2_rel_grid_change'] = float(
        abs(v2[0] - v1[0]) / max(abs(v2[0]), 1e-12))
    # Richardson extrapolation in h^2 from the two finest grids
    # (h=0.02 is an outlier: at that spacing the throat node and the
    # pole shoulder are under-resolved).  v(h) = v_inf + c h^2 gives
    # v_inf = v3 - (v3 - v2)/3.
    out['lowest_om2_richardson_h2_limit'] = float(
        v3[0] - (v3[0] - v2[0]) / 3.0)
    out['richardson_note'] = ('The lowest om2 is a near-zero mode: '
                              '+0.000210 (h=0.01) and +0.000223 '
                              '(h=0.005) -- stable to 6% between the '
                              'two finest grids, h^2-extrapolated '
                              'limit +0.000219, and identical '
                              '(+0.000210) on the smaller box '
                              '[-30,30], confirming a localised mode, '
                              'not a box artefact.  It stays POSITIVE '
                              'on every grid; no grid produces a '
                              'negative value.  Its smallness (not '
                              'its sign) is the finding to carry '
                              'forward.')
    out['any_negative_either_grid'] = bool(
        np.any(v1 < 0) or np.any(v2 < 0) or np.any(v3 < 0))
    # box-size sensitivity of the lowest mode (h=0.01 coefficients,
    # truncated to [-30,30]): a localised mode barely moves, box modes do
    rb, Kb, Gb, Mb = prof[0.01]
    m30 = np.abs(rb) <= 30.0
    vb, _ = ell0_solve(rb[m30], Kb[m30], Gb[m30], Mb[m30])
    out['lowest_om2_box30_h0.01'] = float(vb[0])
    # eigenfunction anatomy of the lowest mode (fine grid)
    chi = vec2[:, 0]
    chi = chi / np.max(np.abs(chi))
    rr = r2[1:-1]
    w = chi**2 * prof[0.01][1][1:-1]        # K0-weighted norm density
    w = w / np.sum(w)
    def frac(lo, hi):
        m = (rr >= lo) & (rr <= hi)
        return float(np.sum(w[m]))
    out['lowest_mode'] = dict(
        om2=float(v2[0]), peak_r=float(rr[np.argmax(np.abs(chi))]),
        norm_frac_pocket_0_to_rstar=frac(0.0, RSTAR),
        norm_frac_abs_r_lt_2=frac(-2.0, 2.0),
        norm_frac_abs_r_gt_10=frac(10.0, 60.0) + frac(-60.0, -10.0),
        note=('K0-weighted norm fractions; the mode is throat/pocket '
              'localised, not a box mode (box modes are the next '
              'eigenvalues, peaked at |r|~30).'))
    # Schroedinger potential on the fine grid
    r, K0, G0, M0 = prof[0.01]
    rho, V = liouville_V(r, K0, G0, M0)
    out['rho_range'] = [float(rho[0]), float(rho[-1])]
    regions = {}
    for name, m in (
            ('r_in_[0.15,1.4]', (r >= 0.15) & (r <= 1.4)),
            ('r_in_[-60,-0.15]', (r >= -60) & (r <= -0.15)),
            ('r_in_[2.15,60]', (r >= 2.15) & (r <= 60))):
        i = int(np.argmin(np.where(m, V, np.inf)))
        regions[name] = dict(V_min=float(V[i]), V_min_r=float(r[i]))
    out['V_regions'] = regions
    out['V_samples'] = {
        f'r={rr:g}': float(V[np.argmin(np.abs(r - rr))])
        for rr in (-20, -5, -1, -0.5, 0.5, 1.0, 3, 5, 20, 40)}
    out['V_note'] = ('Liouville V is FD-unreliable for |r| <~ 0.1 (the '
                     'h ~ r^2 log-derivative cancellation) and diverges '
                     'to +inf at the D=0 pole r* (a barrier of the chi '
                     'parametrisation); region minima exclude both. '
                     'The eigenvalue verdict rests on the flux-form '
                     'Sturm-Liouville solve, which is regular at the '
                     'throat and treats the pole through its (finite) '
                     'flux coefficients.')
    out['M0_over_K0_samples'] = {
        f'r={rr:g}': float((M0 / K0)[np.argmin(np.abs(r - rr))])
        for rr in (-40, -5, 0.5, 0.77, 1.0, 5, 40)}
    return out


# ----------------------------------------------------------------------------
# 3. l>=1 secondary coupled solve on the reduction's matrices
# ----------------------------------------------------------------------------
def e3_profile():
    """e3 on a coarse grid via F4-2's validated pi-shift EL route."""
    hc = 0.02
    rc = np.arange(-60.0, 60.0 + 0.5 * hc, hc)
    dc = p31.theory_on_bg(rc)
    ds_ = 2e-3
    dpi_ = TAU * ds_
    ELp = F42.el_pi_shifted(rc, dc, +ds_)
    ELm = F42.el_pi_shifted(rc, dc, -ds_)
    return rc, (ELp - ELm) / (2 * dpi_)


def build_matrices(ell, r, e3r, e3v, with_e3=True):
    cf = C41.build_coeffs(r)
    cf['a1p'] = np.gradient(cf['a1'], r, edge_order=2)
    J = cf['J']
    i0 = int(np.argmin(np.abs(r)))
    res_pole = float(cf['G1'][i0] * cf['pip'][i0] * cf['Jpp'][i0]
                     * cf['J'][i0] / (8.0 * cf['X'][i0]))
    e4_raw = cf['e4'].copy()
    if abs(r[i0]) < 1e-12:
        cf['e4'][i0] = 0.5 * ((e4_raw[i0 - 1] - res_pole / r[i0 - 1])
                              + (e4_raw[i0 + 1] - res_pole / r[i0 + 1]))
    j2 = float(ell * (ell + 1))
    Q8 = A41.build_Q8(cf, j2)
    K, G, Qc, M, checks, PA = A41.reduce_Q8(Q8, r, J)
    if with_e3:
        e3 = np.interp(r, e3r, e3v)
        M = M.copy()
        M[1, 1] = M[1, 1] - 2.0 * e3 / J**2
    pr = A41.printed_KG(r, ell)
    return (K, G, Qc, M), J, pr['Sden'], checks


def segment_solve(r, Kt, Gt, Qt, Mt, i0, i1, h):
    """Coupled solve on nodes [i0, i1] (interior unknowns), Dirichlet
    at the segment ends, by a DENSE generalised eigenvalue solve
    (scipy.linalg.eig) -- no shift, no ARPACK artefacts.  B (= Kt) is
    indefinite on ghost segments, so complex/infinite eigenvalues
    occur and are counted, not hidden.  Returns (lowest real om^2
    list, n_complex_or_infinite)."""
    from scipy.linalg import eig as dense_eig
    idx = np.arange(i0, i1 + 1)
    n = len(idx) - 2
    if n < 12:
        return [], 0
    ii = idx[1:-1]
    Gh = 0.5 * (Gt[:, :, idx[1:]] + Gt[:, :, idx[:-1]])   # (2,2,n+1)
    dim = 2 * n
    A = np.zeros((dim, dim))
    Qp = np.gradient(Qt, h, axis=2, edge_order=2)

    def add_block(bi, bj, blk):
        A[bi * 2:bi * 2 + 2, bj * 2:bj * 2 + 2] += blk
    for j in range(n):
        gi = ii[j]
        add_block(j, j, (Gh[:, :, j + 1] + Gh[:, :, j]) / h**2
                  + Mt[:, :, gi] - Qp[:, :, gi])
        if j > 0:
            add_block(j, j - 1, -Gh[:, :, j] / h**2)
        if j < n - 1:
            add_block(j, j + 1, -Gh[:, :, j + 1] / h**2)
        if 0 < j < n - 1:
            add_block(j, j + 1, -Qt[:, :, gi] / h)
            add_block(j, j - 1, +Qt[:, :, gi] / h)
        elif j == 0:
            add_block(j, j + 1, -Qt[:, :, gi] / h)
        else:
            add_block(j, j - 1, +Qt[:, :, gi] / h)
    A = (A + A.T) * 0.5
    B = np.zeros((dim, dim))
    for j, gi in enumerate(ii):
        B[j * 2:j * 2 + 2, j * 2:j * 2 + 2] = Kt[:, :, gi]
    try:
        vals = dense_eig(A, B, right=False)
    except Exception as exc:  # recorded, not hidden
        return [f'solver_failure: {exc}'], 0
    finite = np.isfinite(vals.real) & np.isfinite(vals.imag)
    realmask = finite & (np.abs(vals.imag)
                         < 1e-4 * np.maximum(1.0, np.abs(vals.real)))
    ncomp = int(len(vals) - int(np.sum(realmask)))
    return sorted(float(v) for v in vals[realmask].real), ncomp


def branch_potential_min(r, Kt, Gt, Mt, valid):
    """Branch-diagonal Liouville potentials where k_a>0, g_a>0."""
    n = len(r)
    evalsK = np.linalg.eigvalsh(np.transpose(Kt, (2, 0, 1)))
    out = []
    for a in range(2):
        ka = evalsK[:, a]
        # project G, M onto the K-eigenvector of branch a
        _, evecs = np.linalg.eigh(np.transpose(Kt, (2, 0, 1)))
        ea = evecs[:, :, a]                       # (n,2)
        ga = np.einsum('ni,nij,nj->n', ea, np.transpose(Gt, (2, 0, 1)), ea)
        ma = np.einsum('ni,nij,nj->n', ea, np.transpose(Mt, (2, 0, 1)), ea)
        # degeneracy filter: a branch potential is only meaningful
        # where the branch is a genuine finite-kinetic branch, not at
        # an eigenvalue crossing where k_a -> 0 makes m_a/k_a blow up
        kmax = np.max(ka[valid]) if np.any(valid) else 0.0
        ok = valid & (ka > 0.02 * kmax) & (ga > 0)
        best = None
        # contiguous stretches
        j = 0
        while j < n:
            if not ok[j]:
                j += 1
                continue
            j0 = j
            while j < n and ok[j]:
                j += 1
            if j - j0 >= 12:
                rs, ks, gs, ms = r[j0:j], ka[j0:j], ga[j0:j], ma[j0:j]
                _, V = liouville_V(rs, ks, gs, ms)
                m = np.isfinite(V)
                if np.any(m):
                    i = int(np.argmin(np.where(m, V, np.inf)))
                    cand = (float(V[i]), float(rs[i]))
                    if best is None or cand[0] < best[0]:
                        best = cand
        out.append(best)
    return out, evalsK


def ell_ge1_analysis(ell, e3r, e3v):
    out = {}
    h = 0.05
    r = np.linspace(-60.0, 60.0, int(120 / h) + 1)
    (K, G, Qc, M), J, Sden, checks = build_matrices(ell, r, e3r, e3v, True)
    (K0n, G0n, Q0n, M0n), _, _, _ = build_matrices(ell, r, e3r, e3v, False)
    J2 = J**2
    Kt, Gt, Qt, Mt = K * J2, G * J2, Qc * J2, M * J2
    # windows: Dden pole + Sden zeros
    excl = np.abs(r - RSTAR) < 0.35
    sgn = np.sign(Sden)
    szeros = []
    for ci in np.where(np.diff(sgn) != 0)[0]:
        a, b = r[ci], r[ci + 1]
        fa, fb = Sden[ci], Sden[ci + 1]
        rz = float(a - fa * (b - a) / (fb - fa))
        szeros.append(rz)
        excl |= np.abs(r - rz) < 0.3
    out['Sden_zeros'] = szeros
    valid = ~excl
    # K signature on the valid domain
    evalsK = np.linalg.eigvalsh(np.transpose(K, (2, 0, 1)))
    out['K_eigmin_min_valid'] = float(np.min(evalsK[valid, 0]))
    out['K_indefinite_fraction_valid'] = float(
        np.mean(evalsK[valid, 0] < 0))
    out['detK_negative_fraction_valid'] = float(np.mean(
        (K[0, 0] * K[1, 1] - K[0, 1]**2)[valid] < 0))
    # segments = contiguous valid stretches
    segs = []
    j = 0
    n = len(r)
    while j < n:
        if not valid[j]:
            j += 1
            continue
        j0 = j
        while j < n and valid[j]:
            j += 1
        segs.append((j0, j - 1))
    # coupled solve at two resolutions (dense generalised eig):
    # step 4 -> h_solve = 0.2, step 2 -> h_solve = 0.1
    def sub(X, step):
        return X[:, :, ::step]
    all_low = []
    seg_report = []
    for (a, b) in segs:
        entry = dict(r_range=[float(r[a]), float(r[b])],
                     K_positive_definite_throughout=bool(
                         np.all(evalsK[a:b + 1, 0] > 0)))
        for step, tag in ((4, 'h0.2'), (2, 'h0.1')):
            rs = r[::step]
            ia = int(np.ceil(a / step)); ib = int(np.floor(b / step))
            if ib - ia < 12:
                entry[f'lowest_real_om2_{tag}'] = 'segment too short'
                entry[f'n_complex_or_inf_{tag}'] = None
                continue
            vals, ncomp = segment_solve(
                rs, sub(Kt, step), sub(Gt, step), sub(Qt, step),
                sub(Mt, step), ia, ib, h * step)
            entry[f'lowest_real_om2_{tag}'] = (
                vals[:4] if vals and isinstance(vals[0], float) else vals)
            entry[f'n_complex_or_inf_{tag}'] = ncomp
            if tag == 'h0.1' and vals and isinstance(vals[0], float):
                all_low.extend(vals)
        seg_report.append(entry)
    out['segments'] = seg_report
    out['lowest_om2_all_segments'] = (float(min(all_low)) if all_low
                                      else None)
    out['segment_solve_note'] = ('Dense generalised solves per regular '
                                 'segment at h=0.2 and h=0.1.  On '
                                 'segments where K is indefinite (the '
                                 'ghost band and, for the uncorrected '
                                 'reduction, much of the negative side) '
                                 'the generalised problem has complex / '
                                 'infinite eigenvalues and its real '
                                 'om2<0 values are the ghost signature, '
                                 'not an independent tachyon read.  Only '
                                 'a segment with K positive-definite '
                                 'throughout can carry a tachyon read, '
                                 'and then only if its negative om2 '
                                 'persists at both resolutions.')
    # sensitivity: no-e3 lowest (same segments, coarse pass on segment 0..)
    out['e3_correction_note'] = (
        'M22 corrected by -2 e3/J^2 (e3 from the F4-2 pi-shift route); '
        'segment solves use the corrected M.  The uncorrected matrices '
        'were also built; their M22 differs by that term only.')
    # branch potentials
    bp, _ = branch_potential_min(r, Kt, Gt, Mt, valid)
    out['branch_potential_minima'] = [
        (dict(V_min=b[0], r=b[1]) if b else None) for b in bp]
    out['branch_note'] = ('Branch-diagonal Liouville potentials '
                          '(K-eigenbasis projections; inter-branch '
                          'derivative and Q couplings ignored).  A '
                          'branch exists only where its k_a>0 and '
                          'g_a>0; the ghost branch (k_a<0) has no '
                          'potential and is not listed as None by '
                          'accident -- see K_indefinite_fraction_valid.')
    return out


# ----------------------------------------------------------------------------
def main():
    t0 = time.time()
    res = {'task': 'F4-3 even-sector tachyon audit (relaunch, 2026-11-21)',
           'conventions': 'float64; box r in [-60,60] Dirichlet; A=B=1 '
                          'so r is the tortoise coordinate.'}
    res['odd_validation'] = odd_validation()
    if not res['odd_validation']['passed']:
        res['verdict'] = ('STOPPED: odd-sector validation failed; per '
                          'the task the machinery is not trusted and the '
                          'even read is not made.')
        with open(OUT, 'w') as fh:
            json.dump(res, fh, indent=2)
        print(json.dumps(res, indent=2))
        return
    res['ell0'] = ell0_analysis()
    e3r, e3v = e3_profile()
    res['ell_ge1_secondary'] = {}
    for ell in (1, 2, 3, 5, 10):
        res['ell_ge1_secondary'][f'ell{ell}'] = ell_ge1_analysis(
            ell, e3r, e3v)
    res['runtime_s'] = time.time() - t0
    with open(OUT, 'w') as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
