#!/usr/bin/env python3
"""
Gate-3 worker V2 (VERIFICATION) — Claims G3-2 and G3-4b.

Fresh, independent code. It does NOT import phase4/p42_ell0.py or
phase4/p42b_ell0_indep.py (neither their coefficients nor their
elimination machinery). Shared definitions used, per the task:
  * the published designer functions from phase3/p31_horndeski.py
    (background, theory functions on the background, Xi/Gamma/Sigma);
  * the paper's LaTeX source in phase4/papers/mrv_src/ (printed
    formulas for sub-tasks 2 and 3, transcribed here from the .tex).

SUB-TASK 1 (G3-4b) — l=0 kinetic coefficient K0(r) from the covariant
action, by a route different from F4-2b's:
  * Ansatz (exponential lapse/shift variables, areal radius fixed):
        ds^2 = -e^{2 al} dt^2 + e^{2 be} (dr + sh dt)^2
               + J(r)^2 dOmega^2,   J = sqrt(r^2+tau^2),
        pi(t,r) general;  perturbations al, be, sh, chi = pi-pi_bg.
    (F4-2b used A = 1+a, B = 1+b, C = c multiplicative variables and
    sympy-derived jet formulas; here the geometry is recomputed from
    scratch below.)
  * The nonlinear Lagrangian density L(al,be,sh,pi jets) per unit
    solid angle is evaluated directly in float64: metric jets ->
    Christoffel -> Ricci scalar R, pi-Hessian -> Kg = (Box pi)^2 -
    H_ab H^ab, and the beyond-Horndeski eps-eps contraction Ceps
    (overall BH sign -F4*Ceps, the convention fixed by the F4-4
    Bianchi/EL closure recorded in CHECKPOINT4). Designer functions
    F, G4, G4X, F4 are evaluated NONLINEARLY at (pi, X) from the
    eq.-(56) ansatz via p31's f_i/g_i functions of s = pi/tau.
  * The quadratic jet-Hessian H_L(r) of L is obtained by vectorised
    finite-difference probing of L in the 24-dim jet space
    {al,be,sh,pi} x {(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)}
    (Richardson for the diagonal, central for off-diagonal).
  * Linearised Euler-Lagrange operators follow by the standard
    variational algebra EL = sum_alpha (-D)^alpha dL/djet_alpha
    applied to H_L and its r-derivatives (5-point FD).
  * Constraint elimination is read off THIS computed operator
    structure (printed in the JSON):
      - EL_sh is exactly D_t of a bracket Q (only (1,0),(1,1) jets):
        Q = 0 gives be = p chi' + q chi for localised perturbations.
      - EL_be contains the lapse/shift only in the combination
        S1 := al' + sh_t (coefficients of al' and sh_t agree to FD
        noise, as do those of al'' and sh_tr in EL_pi), and is
        algebraic in S1: it determines S1(chi).
      - EL_pi contains al, sh only through S1 and S1'; substituting
        be(chi), S1(chi) gives the reduced scalar equation
        R[chi] = -2 K0 chi_tt + 2 G0 chi_rr + ... ;
        K0 = -R_(2,0)/2, G0 = R_(0,2)/2 (covariant normalisation:
        action per unit solid angle).
    Checks recorded: background EL ~ 0, >2nd-order EL coefficients
    ~ 0, the chi_tt' (2,1) coefficient of R cancels to FD floor,
    coefficient equalities u_al = u_sh, w_al = w_sh, m_al = m_sh.

SUB-TASK 2 (G3-2b) — the printed e1 J'^2 pair vs Kobayashi's frame:
  * Symbolic (sympy): from the printed e1 in the LaTeX (the two
    J'^2 terms inside the bracket, with the 1/(2 sqrt(AB)) prefactor),
    the pair's on-background (A=B=1, F=H=1) value is (J'^2-J'^3)/X,
    identically zero for J = r (J' = 1).
  * Numeric: the printed-coefficient route is recomputed here from
    the LaTeX Appendix B formulas (A=B=1, on-shell) — NOT imported —
    giving K0_printed; removing the pair from e1 gives K0_corr.
    Claim: K0_corr > 0 everywhere sampled and K0_corr/J^2 -> +2/tau^2
    at both infinities (Appendix-B normalisation).

SUB-TASK 3 (G3-2a) — the a2^BH defect at r = 5 (and extra radii):
  from the printed Appendix B formulas recomputed here, the identity
  b3 = 2(a1' - a2) holds with a2 = a2^H and fails by exactly
  -4 pi'^3 F4 with the printed a2 = a2^H - a2^BH included.

float64 / symbolic only. Internal only.
"""
import itertools
import json
import math
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
import p31_horndeski as p31

TAU = p31.TAU
TEX_PATH = ('/home/hatch/workspace/warp-pilot/phase4/papers/'
            'mrv_src/apr-17-19.tex')

# ======================================================================
# Part 0: nonlinear Lagrangian density from jets (own geometry code)
# ======================================================================
# jet index convention: 0 val, 1 d_t, 2 d_r, 3 d_tt, 4 d_tr, 5 d_rr
# (derivative VALUES, not Taylor coefficients)

def _jm(a, b):
    return np.stack([a[0] * b[0],
                     a[1] * b[0] + a[0] * b[1],
                     a[2] * b[0] + a[0] * b[2],
                     a[3] * b[0] + 2 * a[1] * b[1] + a[0] * b[3],
                     a[4] * b[0] + a[1] * b[2] + a[2] * b[1] + a[0] * b[4],
                     a[5] * b[0] + 2 * a[2] * b[2] + a[0] * b[5]])


def _jinv(a):
    iv = 1.0 / a[0]
    iv2 = iv * iv
    return np.stack([iv, -a[1] * iv2, -a[2] * iv2,
                     -a[3] * iv2 + 2 * a[1] ** 2 * iv2 * iv,
                     -a[4] * iv2 + 2 * a[1] * a[2] * iv2 * iv,
                     -a[5] * iv2 + 2 * a[2] ** 2 * iv2 * iv])


def _jexp(a):
    e = np.exp(a[0])
    return np.stack([e, e * a[1], e * a[2], e * (a[3] + a[1] ** 2),
                     e * (a[4] + a[1] * a[2]), e * (a[5] + a[2] ** 2)])


def _theory(pi_v, X):
    """F, G4, G4X, F4 at (pi, X) from the eq.-(56) designer ansatz."""
    sa = np.atleast_1d(pi_v / TAU)
    Xa = np.atleast_1d(X)
    f2v = p31.f2_s(sa)
    f1v = p31.f1_s(sa, f2v)
    f0v = p31.f0_s(sa, f1v, f2v)
    F = f0v + f1v * Xa + f2v * Xa ** 2
    G4 = 0.5 + p31.g40_s(sa) + p31.g41_s(sa) * Xa
    G4X = p31.g41_s(sa)
    F4 = p31.f40_s(sa) + p31.f41_s(sa) * Xa
    shp = np.shape(pi_v)
    return (F.reshape(shp), G4.reshape(shp), G4X.reshape(shp),
            F4.reshape(shp))


def _perm_sign(p):
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
    return -1.0 if inv % 2 else 1.0


_CEPS_TERMS = []
for _mu, _nu, _rho, _sg in itertools.permutations(range(4)):
    for _al, _be, _ga, _de in itertools.permutations(range(4)):
        if _de == _sg or {_de, _sg} == {0, 1}:
            _CEPS_TERMS.append((_mu, _nu, _rho, _sg, _al, _be, _ga, _de,
                                _perm_sign((_mu, _nu, _rho, _sg))
                                * _perm_sign((_al, _be, _ga, _de))))


def L_point(jets, r0):
    """Density per unit solid angle at radius r0 for the jet configs
    in `jets` (dict field -> (6, N) arrays, fields al, be, sh, pi)."""
    al, be, sh, pi = jets['al'], jets['be'], jets['sh'], jets['pi']
    N = al.shape[1]
    A = _jexp(al)
    B = _jexp(be)
    A2 = _jm(A, A)
    B2 = _jm(B, B)
    J = np.sqrt(r0 ** 2 + TAU ** 2)
    Jp = r0 / J
    Jpp = TAU ** 2 / J ** 3
    Jj = np.zeros((6, N))
    Jj[0] = J
    Jj[2] = Jp
    Jj[5] = Jpp
    J2 = _jm(Jj, Jj)
    Z = np.zeros((6, N))
    g = {(0, 0): -A2 + _jm(B2, _jm(sh, sh)), (0, 1): _jm(B2, sh),
         (1, 1): B2, (2, 2): J2, (3, 3): J2.copy()}
    g[(1, 0)] = g[(0, 1)]
    for k in [(0, 2), (0, 3), (1, 2), (1, 3), (2, 0), (2, 1), (3, 0),
              (3, 1), (2, 3), (3, 2)]:
        g[k] = Z
    det = _jm(g[(0, 0)], g[(1, 1)]) - _jm(g[(0, 1)], g[(1, 0)])
    dinv = _jinv(det)
    gi = {(0, 0): _jm(g[(1, 1)], dinv), (1, 1): _jm(g[(0, 0)], dinv),
          (0, 1): -_jm(g[(0, 1)], dinv), (2, 2): _jinv(J2),
          (3, 3): _jinv(J2)}
    gi[(1, 0)] = gi[(0, 1)]
    for k in [(0, 2), (0, 3), (1, 2), (1, 3), (2, 0), (2, 1), (3, 0),
              (3, 1), (2, 3), (3, 2)]:
        gi[k] = Z

    def djet(gj, k):
        if k == 0:
            return np.stack([gj[1], gj[3], gj[4]])
        if k == 1:
            return np.stack([gj[2], gj[4], gj[5]])
        return np.zeros((3, N))

    dg = {(i, j, k): djet(g[(i, j)], k)
          for i in range(4) for j in range(4) for k in range(4)}
    Gam = {}
    for l in range(4):
        for i in range(4):
            for j in range(4):
                acc = np.zeros((3, N))
                for m in range(4):
                    term = dg[(m, j, i)] + dg[(m, i, j)] - dg[(j, i, m)]
                    gm = gi[(l, m)]
                    acc = acc + np.stack([
                        gm[0] * term[0],
                        gm[1] * term[0] + gm[0] * term[1],
                        gm[2] * term[0] + gm[0] * term[2]])
                Gam[(l, i, j)] = 0.5 * acc

    def dGam(Gij, k, idx):
        if k == 0:
            return Gij[1]
        if k == 1:
            return Gij[2]
        if k == 2 and idx in ((3, 2, 3), (3, 3, 2)):
            return -np.ones(N)   # d_theta cot(theta) at theta = pi/2
        if k == 2 and idx == (2, 3, 3):
            return np.ones(N)    # d_theta(-sin theta cos theta) at pi/2
        return np.zeros(N)

    Ric = {}
    for i in range(4):
        for j in range(4):
            acc = np.zeros(N)
            for l in range(4):
                acc = (acc + dGam(Gam[(l, i, j)], l, (l, i, j))
                       - dGam(Gam[(l, i, l)], j, (l, i, l)))
                for m in range(4):
                    acc = (acc + Gam[(l, l, m)][0] * Gam[(m, i, j)][0]
                           - Gam[(l, j, m)][0] * Gam[(m, i, l)][0])
            Ric[(i, j)] = acc
    Rsc = np.zeros(N)
    for i in range(4):
        for j in range(4):
            Rsc = Rsc + gi[(i, j)][0] * Ric[(i, j)]
    dpi = {0: pi[1], 1: pi[2], 2: np.zeros(N), 3: np.zeros(N)}
    ddpi = {(0, 0): pi[3], (0, 1): pi[4], (1, 0): pi[4], (1, 1): pi[5]}
    H = {}
    for a in range(4):
        for b in range(4):
            H[(a, b)] = (ddpi.get((a, b), np.zeros(N))
                         - sum(Gam[(c, a, b)][0] * dpi[c] for c in range(4)))
    Box = sum(gi[(a, b)][0] * H[(a, b)]
              for a in range(4) for b in range(4))
    HH = sum(gi[(a, c)][0] * gi[(b, d)][0] * H[(a, b)] * H[(c, d)]
             for a in range(4) for b in range(4)
             for c in range(4) for d in range(4))
    Kg = Box ** 2 - HH
    Xv = -0.5 * sum(gi[(a, b)][0] * dpi[a] * dpi[b]
                    for a in range(4) for b in range(4))
    F, G4, G4X, F4 = _theory(pi[0], Xv)
    SQ = A[0] * B[0] * J ** 2
    gval = {(a, b): g[(a, b)][0] for a in range(4) for b in range(4)}
    piv = [dpi[0], dpi[1], dpi[2], dpi[3]]
    Ceps = np.zeros(N)
    for (mu, nu, rho, sg, a_, b_, ga, de, sgn) in _CEPS_TERMS:
        Ceps = (Ceps + sgn * gval[(de, sg)] / SQ ** 2
                * piv[mu] * piv[a_] * H[(nu, b_)] * H[(rho, ga)])
    return SQ * (F + G4 * Rsc + G4X * Kg - F4 * Ceps)


def _bg_jets(r0, N):
    bg = p31.background(np.array([r0]))
    jets = {}
    for f in ('al', 'be', 'sh'):
        jets[f] = np.zeros((6, N))
    pj = np.zeros((6, N))
    pj[0] = TAU * bg['s'][0]
    pj[2] = bg['pip'][0]
    pj[5] = bg['pipp'][0]
    jets['pi'] = pj
    return jets


# ======================================================================
# Part 1: jet-Hessian -> EL operators -> elimination (sub-task 1)
# ======================================================================
FIELDS = ['al', 'be', 'sh', 'pi']
ORDS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
ROW = {(0, 0): 0, (1, 0): 1, (0, 1): 2, (2, 0): 3, (1, 1): 4, (0, 2): 5}
JETS = [(f, o) for f in FIELDS for o in ORDS]
NJ = len(JETS)
IDX = {j: i for i, j in enumerate(JETS)}


def jet_hess(r, e=2e-3):
    """Gradient and Hessian of L w.r.t. the 24 perturbation jets."""
    pts = [np.zeros(NJ)]
    tags = [('0',)]
    for i in range(NJ):
        for sgn, ee in [(1, e), (-1, e), (1, e / 2), (-1, e / 2)]:
            u = np.zeros(NJ)
            u[i] = sgn * ee
            pts.append(u)
            tags.append(('d', i, sgn, ee))
    pairs = [(i, j) for i in range(NJ) for j in range(i + 1, NJ)]
    for (i, j) in pairs:
        for s1 in (1, -1):
            for s2 in (1, -1):
                u = np.zeros(NJ)
                u[i] = s1 * e
                u[j] = s2 * e
                pts.append(u)
                tags.append(('p', i, j, s1, s2))
    U = np.array(pts)
    n = len(pts)
    jets = _bg_jets(r, n)
    for k, (f, o) in enumerate(JETS):
        jets[f][ROW[o]] = jets[f][ROW[o]] + U[:, k]
    L = L_point(jets, r)
    Ld = {t: v for t, v in zip(tags, L)}
    g = np.zeros(NJ)
    H = np.zeros((NJ, NJ))
    for i in range(NJ):
        gp = (Ld[('d', i, 1, e)] - Ld[('d', i, -1, e)]) / (2 * e)
        gm = (Ld[('d', i, 1, e / 2)] - Ld[('d', i, -1, e / 2)]) / e
        g[i] = 2 * gm - gp
        Hp = (Ld[('d', i, 1, e)] - 2 * Ld[('0',)]
              + Ld[('d', i, -1, e)]) / e ** 2
        Hm = (Ld[('d', i, 1, e / 2)] - 2 * Ld[('0',)]
              + Ld[('d', i, -1, e / 2)]) / (e / 2) ** 2
        H[i, i] = 2 * Hm - Hp
    for (i, j) in pairs:
        H[i, j] = H[j, i] = (Ld[('p', i, j, 1, 1)] - Ld[('p', i, j, 1, -1)]
                             - Ld[('p', i, j, -1, 1)]
                             + Ld[('p', i, j, -1, -1)]) / (4 * e * e)
    return g, H


def _M_from(Hs, gs, h):
    """EL operators from Hessians/gradients sampled at offsets
    {-2,-1,0,1,2} (dicts keyed by offset) with spacing h."""
    H0 = Hs[0]
    Hp = (-Hs[2] + 8 * Hs[1] - 8 * Hs[-1] + Hs[-2]) / (12 * h)
    Hpp = (-Hs[2] + 16 * Hs[1] - 30 * Hs[0] + 16 * Hs[-1] - Hs[-2]) \
        / (12 * h ** 2)
    Hd = [H0, Hp, Hpp]
    gd = [gs[0],
          (-gs[2] + 8 * gs[1] - 8 * gs[-1] + gs[-2]) / (12 * h),
          (-gs[2] + 16 * gs[1] - 30 * gs[0] + 16 * gs[-1] - gs[-2])
          / (12 * h ** 2)]
    ELbg = np.zeros(4)
    for Phi, f in enumerate(FIELDS):
        tot = 0.0
        for o in ORDS:
            if o[0] != 0:
                continue
            tot += (-1) ** o[1] * gd[o[1]][IDX[(f, o)]]
        ELbg[Phi] = tot
    M = {}
    high = {}
    for Phi, f in enumerate(FIELDS):
        for Psi, pf in enumerate(FIELDS):
            coeffs = {}
            for alpha in ORDS:
                ia = IDX[(f, alpha)]
                for beta in ORDS:
                    ib = IDX[(pf, beta)]
                    if Hd[0][ia, ib] == 0 and Hd[1][ia, ib] == 0 \
                            and Hd[2][ia, ib] == 0:
                        continue
                    for s in range(alpha[1] + 1):
                        gamma = (beta[0] + alpha[0],
                                 beta[1] + alpha[1] - s)
                        c = ((-1) ** (alpha[0] + alpha[1])
                             * math.comb(alpha[1], s) * Hd[s][ia, ib])
                        if gamma[0] + gamma[1] <= 2:
                            coeffs[gamma] = coeffs.get(gamma, 0.0) + c
                        else:
                            key = (f, pf, gamma)
                            high[key] = high.get(key, 0.0) + c
            M[(f, pf)] = coeffs
    return ELbg, M, high


def _get(M, f, pf, g):
    return M[(f, pf)].get(g, 0.0)


def _add_ops(*ops):
    out = {}
    for op in ops:
        for g, c in op.items():
            out[g] = out.get(g, 0.0) + c
    return out


def _scale(op, s):
    return {g: c * s for g, c in op.items()}


def _subst_be(op, p, q, pp, qq, p2=0.0, q2=0.0):
    """Substitute be = p chi' + q chi (and its r/t jets) into an
    operator's be-part; returns the induced operator on pi.
    pp/qq are p'/q', p2/q2 are p''/q''."""
    out = {}

    def add(g, c):
        out[g] = out.get(g, 0.0) + c

    for (nt, nr), c in op.items():
        if nr == 0:
            add((nt, 1), c * p)
            add((nt, 0), c * q)
        elif nr == 1:
            add((nt, 2), c * p)
            add((nt, 1), c * (pp + q))
            add((nt, 0), c * qq)
        elif nr == 2:
            add((nt, 3), c * p)
            add((nt, 2), c * (2 * pp + q))
            add((nt, 1), c * (p2 + 2 * qq))
            add((nt, 0), c * q2)
        else:
            raise ValueError(f'unexpected be jet order {nr}')
    return out


def elim_at(r0, h=None, e=None):
    """K0, G0 at r0 by the route of Part 1. Hessians are computed on
    the shared stencil r0 + m*h, m in [-6, 6]; EL operators at
    offsets k in [-2, 2] are built from them. For |r| > 60 the
    probing step is scaled DOWN as 0.12/|r|: the off-diagonal
    jet-Hessian FD truncation error grows ~ e^2 x (large-r
    coefficient scale) and at fixed e = 2e-3 it corrupts K0/J^2
    at the 1e-3 level by |r| = 400 (measured: e = 2e-3 -> 0.01181,
    e = 2.5e-4 -> 0.01001 at r = 400, h-independent)."""
    if h is None:
        h = 0.05
    if e is None:
        e = 2e-3 if abs(r0) <= 60 else 0.12 / abs(r0)
    Hs_all = {}
    gs_all = {}
    for m in range(-6, 7):
        gs_all[m], Hs_all[m] = jet_hess(r0 + m * h, e=e)
    Ms = {}
    ELbg0 = None
    high0 = None
    for k in range(-2, 3):
        Hs = {s: Hs_all[k + s] for s in (-2, -1, 0, 1, 2)}
        gs = {s: gs_all[k + s] for s in (-2, -1, 0, 1, 2)}
        ELbg, M, high = _M_from(Hs, gs, h)
        Ms[k] = M
        if k == 0:
            ELbg0, high0 = ELbg, high
    pq = {}
    for k, M in Ms.items():
        Qb = _get(M, 'sh', 'be', (1, 0))
        pq[k] = (-_get(M, 'sh', 'pi', (1, 1)) / Qb,
                 -_get(M, 'sh', 'pi', (1, 0)) / Qb, Qb)

    def derivs(k):
        """p', q', p'', q'' at offset k from a cubic fit over the
        five pq samples."""
        xs = np.array(sorted(pq), dtype=np.float64) * h
        out = []
        for which in (0, 1):
            ys = np.array([pq[kk][which] for kk in sorted(pq)])
            cf = np.polyfit(xs, ys, 3)
            d1 = np.polyval(np.polyder(cf, 1), k * h)
            d2 = np.polyval(np.polyder(cf, 2), k * h)
            out.append((d1, d2))
        return out[0][0], out[1][0], out[0][1], out[1][1]

    S1 = {}
    for k, M in Ms.items():
        p, q, _ = pq[k]
        pp, qq, p2, q2 = derivs(k)
        m = _get(M, 'be', 'al', (0, 1))
        rest = _add_ops(dict(M[('be', 'pi')]),
                        _subst_be(dict(M[('be', 'be')]), p, q, pp, qq,
                                  p2, q2))
        S1[k] = _scale(rest, -1.0 / m)

    def fd4(vals):
        return (-vals[2] + 8 * vals[1] - 8 * vals[-1] + vals[-2]) / (12 * h)

    allg = set()
    for v in S1.values():
        allg |= set(v)
    S1p = {g: fd4({k: S1[k].get(g, 0.0) for k in (-2, -1, 1, 2)})
           for g in allg}
    S1r = {}
    for g, c in S1[0].items():
        S1r[(g[0], g[1] + 1)] = S1r.get((g[0], g[1] + 1), 0.0) + c
    for g, c in S1p.items():
        S1r[g] = S1r.get(g, 0.0) + c
    M = Ms[0]
    p, q, Qb = pq[0]
    pp, qq, p2, q2 = derivs(0)
    restP = _add_ops(dict(M[('pi', 'pi')]),
                     _subst_be(dict(M[('pi', 'be')]), p, q, pp, qq,
                               p2, q2))
    u = _get(M, 'pi', 'al', (0, 1))
    uC = _get(M, 'pi', 'sh', (1, 0))
    w = _get(M, 'pi', 'al', (0, 2))
    wC = _get(M, 'pi', 'sh', (1, 1))
    m = _get(M, 'be', 'al', (0, 1))
    mC = _get(M, 'be', 'sh', (1, 0))
    R = _add_ops(restP, _scale(S1[0], u), _scale(S1r, w))
    J = float(np.sqrt(r0 ** 2 + TAU ** 2))
    return dict(
        r=float(r0), J=J,
        K0=float(-R.get((2, 0), 0.0) / 2),
        G0=float(R.get((0, 2), 0.0) / 2),
        M0=float(-R.get((0, 0), 0.0) / 2),
        R_chi_tt_r=float(R.get((2, 1), 0.0)),
        ELbg_max=float(np.max(np.abs(ELbg0))),
        high_order_max=float(max((abs(v) for v in high0.values()),
                                 default=0.0)),
        coeff_equalities=dict(
            u_al_minus_u_sh=float(u - uC), w_al_minus_w_sh=float(w - wC),
            m_al_minus_m_sh=float(m - mC)),
        EL_sh_support={str(g): float(c) for g, c in
                       sorted(_add_ops(M[('sh', 'be')], M[('sh', 'pi')]).items())
                       if abs(c) > 1e-3},
    )


# ======================================================================
# Part 2: printed Appendix B route, transcribed from the LaTeX
# (sub-tasks 2 numeric and 3)
# ======================================================================
def printed_build(r, h):
    """Appendix B coefficients at A = B = 1, on-shell (E_A = E_B = 0,
    F = G = H = 1), from the printed formulas in apr-17-19.tex,
    Appendix B. Returns the coefficients and the reduced
    K0 (printed), K0_corr (e1 pair removed), G0."""
    d = p31.theory_on_bg(r)
    Xi, Gamma = p31.Xi_Gamma(d)
    Sig = p31.Sigma_val(d, Xi, Gamma)
    J, Jp, Jpp = d['J'], d['Jp'], d['Jpp']
    pip, pipp, X, Xp = d['pip'], d['pipp'], d['X'], d['Xp']
    F4 = d['F4']
    gr = lambda v: np.gradient(v, h, edge_order=2)
    Xip = gr(Xi)
    D = 2.0 * J * Jp + Xi * pip
    # printed a1, a2 (Horndeski part and printed, = part - a2^BH),
    # a2^BH = 2 sqrt(A B^3) pi'^3 F4 = 2 pi'^3 F4 at A=B=1
    a1 = Xi
    a2H = (2 * pip * Xip - 2 * pipp * Xi - 4 * J * Jpp) / (2 * pip)
    a2BH = 2 * pip ** 3 * F4
    a2 = a2H - a2BH
    # printed b2, b3, b4 (b3 bracket with E_A = 0, A = B = 1)
    b2 = -2.0 * Xi
    b3 = (2 * pipp * Xi + 4 * J * Jpp) / pip
    b4 = D
    # printed c1 (= -Xi - c1^BH), c2, c6
    c1 = -Xi - 4 * J * Jp * pip ** 3 * F4
    c2 = -J * Jp * Gamma - 2 * J ** 2 * Sig / pip
    c6 = 0.5 * J ** 2 * (Sig + pip * Jp / J * Gamma + Jp ** 2 / J ** 2)
    # printed e1: (1/2)[ -2 Xi'/pi' - (X'/X)(Xi/pi') + 2 J'^2/X
    #   - 2 J'^3/X + 2 J J''/X ] - e1^BH  (the J'^2 pair is the
    #   +2J'^2/X -2J'^3/X inside the bracket; H' = 0, E_A-E_B = 0)
    e1BH = 4.0 / pip ** 2 * gr(J * Jp * pip ** 4 * F4)
    pair = (Jp ** 2 - Jp ** 3) / X   # pair's contribution to e1 itself
    e1 = (0.5 * (-2 * Xip / pip - (Xp / X) * (Xi / pip)
                 + 2 * Jp ** 2 / X - 2 * Jp ** 3 / X + 2 * J * Jpp / X)
          - e1BH)
    e2 = -J ** 2 * Sig / X
    # l=0 elimination via the H1 bracket Q = b2 chi' + b3 chi + b4 H2 = 0
    p = -b2 / b4
    q = -b3 / b4
    Dp = gr(D)
    pp_ = (2 * Xip * D - 2 * Xi * Dp) / D ** 2
    c1p_ = gr(c1)

    def K0_of(e1v):
        return e1v + c1 * q - 0.5 * (c1p_ * p + c1 * pp_)

    G0 = -(e2 + p * c2 + c6 * p ** 2)
    return dict(d=d, Xi=Xi, Xip=Xip, D=D, a1=a1, a2H=a2H, a2=a2,
                a2BH=a2BH, b3=b3, e1=e1, pair=pair,
                K0=K0_of(e1), K0_corr=K0_of(e1 - pair), G0=G0)


def _at(arr, r, r0):
    return float(arr[int(np.argmin(np.abs(r - r0)))])


# ======================================================================
# main
# ======================================================================
def main():
    res = {'task': 'Gate-3 V2 verification of G3-2 and G3-4b',
           'route_subtask1': 'covariant action -> exponential '
                             'lapse/shift areal ansatz -> direct '
                             'nonlinear density evaluation -> FD '
                             'jet-Hessian -> EL operators -> '
                             'elimination read off the computed '
                             'operator structure (EL_sh = D_t Q; '
                             'EL_be algebraic in S1 = al\' + sh_t)',
           'normalisation_subtask1': 'covariant action per unit '
                                     'solid angle (Appendix-B '
                                     'coefficients are 2x these)'}
    # ---------------- sub-task 1 ----------------
    spots = [-60., -40., -20., -15., -12.5, -5., -1., -0.5, -0.1,
             0.1, 0.5, 1., 5., 20., 40., 60.]
    prof = {}
    for r0 in spots:
        prof[str(r0)] = elim_at(r0)
    asym = {}
    for r0 in (100., 200., 400., -100., -200., -400.):
        o = elim_at(r0)
        o['K0_over_J2'] = o['K0'] / o['J'] ** 2
        o['G0_over_K0'] = o['G0'] / o['K0']
        asym[str(r0)] = o
    kmin = min(o['K0'] for o in prof.values())
    res['subtask1_K0_from_action'] = dict(
        profile={k: dict(K0=v['K0'], G0=v['G0'],
                         K0_over_J2=v['K0'] / v['J'] ** 2,
                         G0_over_K0=v['G0'] / v['K0'],
                         R_chi_tt_r=v['R_chi_tt_r'],
                         ELbg_max=v['ELbg_max'],
                         high_order_max=v['high_order_max'],
                         coeff_equalities=v['coeff_equalities'])
                 for k, v in prof.items()},
        all_spot_K0_positive=bool(all(o['K0'] > 0 for o in prof.values())),
        min_spot_K0=float(kmin),
        throat_K0_over_r2={k: prof[k]['K0'] / float(k) ** 2
                           for k in ('-0.1', '0.1')},
        throat_note='K0 vanishes only at the throat, quadratically: '
                    'K0/r^2 at r = -0.1 / +0.1 as tabulated (finite, '
                    'positive); K0 > 0 at every other sampled radius',
        asymptotics={k: dict(K0=v['K0'], K0_over_J2=v['K0_over_J2'],
                             G0_over_K0=v['G0_over_K0'])
                     for k, v in asym.items()},
        asymptotics_claim='K0/J^2 -> +1/tau^2 = +0.01 at BOTH '
                          'infinities (values at |r| = 100, 200, 400 '
                          'approach 0.01 from below, both signs)',
        operator_structure_at_r5=prof['5.0']['EL_sh_support'],
        validations=dict(
            ELbg_max_over_spots=float(max(
                o['ELbg_max'] for o in list(prof.values())
                + list(asym.values()))),
            high_order_max_over_spots=float(max(
                o['high_order_max'] for o in list(prof.values())
                + list(asym.values()))),
            R_chi_tt_r_max_abs=float(max(
                abs(o['R_chi_tt_r']) for o in prof.values()))),
    )
    st1_ok = (res['subtask1_K0_from_action']['all_spot_K0_positive']
              and all(0.009 < asym[s]['K0_over_J2'] < 0.0101
                      for s in asym)
              and all(asym[s]['K0_over_J2'] > 0 for s in asym))
    res['subtask1_K0_from_action']['verdict'] = (
        'REPRODUCED' if st1_ok else 'FAILS')

    # ---------------- sub-task 2, symbolic ----------------
    tex = open(TEX_PATH).read()
    frag1 = r"\frac{2BJ'^2}{X}{\cal F}"
    frag2 = r"{\cal H}\frac{B^2J'^2}{JXA}\frac{\D}{\D r}\left(\frac{J^2A}{B}\right)"
    tex_ns = tex.replace(' ', '')
    frags_present = (frag1.replace(' ', '') in tex_ns
                     and frag2.replace(' ', '') in tex_ns)
    a, b, j, f_, hh_, x = sp.symbols('a b j f h x')
    ap, bp, jp = sp.symbols('ap bp jp')
    dJ2AB = (2 * j * jp * a * b + j ** 2 * ap * b
             - j ** 2 * a * bp) / b ** 2     # d/dr (J^2 A / B)
    pair_bracket = (2 * b * jp ** 2 * f_ / x
                    - hh_ * (b ** 2 * jp ** 2 / (j * x * a)) * dJ2AB)
    pair_e1 = pair_bracket / (2 * sp.sqrt(a * b))
    pair_bg = sp.simplify(pair_e1.subs(
        {a: 1, b: 1, f_: 1, hh_: 1, ap: 0, bp: 0}))
    pair_kob = sp.simplify(pair_bg.subs(jp, 1))
    res['subtask2_symbolic'] = dict(
        latex_fragments_found=bool(frags_present),
        pair_on_background=str(pair_bg),
        pair_on_background_expected='(jp**2 - jp**3)/x',
        matches_expected=bool(sp.simplify(
            pair_bg - (jp ** 2 - jp ** 3) / x) == 0),
        pair_at_Jprime_eq_1=str(pair_kob),
        vanishes_in_Kobayashi_frame=bool(pair_kob == 0),
        note='J = r (Kobayashi frame) has J\' = 1 identically, so '
             'the pair cancels there; for the MRV J = sqrt(r^2+tau^2), '
             'J\' = r/J != 1 and the pair is (J\'^2-J\'^3)/X != 0')

    # ---------------- sub-task 2, numeric printed route ----------------
    h = 0.004
    rgrid = np.arange(-60., 60. + 0.5 * h, h)
    B = printed_build(rgrid, h)
    inner = np.abs(rgrid) < 59.9
    pasym = {}
    for r0 in (100., 200., 400., -100., -200., -400.):
        hh2 = 0.01
        rr = np.arange(r0 - 2., r0 + 2. + 0.5 * hh2, hh2)
        Bb = printed_build(rr, hh2)
        Jv = _at(Bb['d']['J'], rr, r0)
        pasym[str(r0)] = dict(
            K0_printed=_at(Bb['K0'], rr, r0),
            K0_corr=_at(Bb['K0_corr'], rr, r0),
            K0_corr_over_J2=_at(Bb['K0_corr'], rr, r0) / Jv ** 2)
    res['subtask2_printed_route'] = dict(
        K0_printed_samples={f'r={rr}': _at(B['K0'], rgrid, rr)
                            for rr in (-40, -20, 5, 20, 40)},
        K0_corr_min_on_grid=float(np.min(B['K0_corr'][inner])),
        K0_corr_all_positive_on_grid=bool(
            np.all(B['K0_corr'][inner] > 0)),
        K0_corr_samples={f'r={rr}': _at(B['K0_corr'], rgrid, rr)
                         for rr in (-60, -40, -20, -5, 5, 20, 40, 60)},
        asymptotics=pasym,
        asymptotics_claim='K0_corr/J^2 -> +2/tau^2 = +0.02 at both '
                          'infinities (Appendix-B normalisation)')
    st2_ok = (res['subtask2_symbolic']['matches_expected']
              and res['subtask2_symbolic']['vanishes_in_Kobayashi_frame']
              and res['subtask2_printed_route'][
                  'K0_corr_all_positive_on_grid']
              and all(0.019 < v['K0_corr_over_J2'] < 0.0201
                      for v in pasym.values()))
    res['subtask2_verdict'] = 'REPRODUCED' if st2_ok else 'FAILS'

    # ---------------- sub-task 3 ----------------
    rows = {}
    for r0 in (5., -20., 40., -40.):
        hh3 = 0.002
        rr = np.arange(r0 - 3., r0 + 3. + 0.5 * hh3, hh3)
        Bb = printed_build(rr, hh3)
        i = int(np.argmin(np.abs(rr - r0)))
        b3v = float(Bb['b3'][i])
        a1p = float(Bb['Xip'][i])
        resid_H = b3v - 2 * (a1p - float(Bb['a2H'][i]))
        resid_printed = b3v - 2 * (a1p - float(Bb['a2'][i]))
        defect = float(-4 * Bb['d']['pip'][i] ** 3 * Bb['d']['F4'][i])
        rows[str(r0)] = dict(
            b3=b3v, a2H=float(Bb['a2H'][i]), a2_printed=float(Bb['a2'][i]),
            resid_with_a2H=resid_H,
            resid_with_printed_a2=resid_printed,
            minus_4_pip3_F4=defect,
            resid_printed_minus_defect=resid_printed - defect)
    res['subtask3_a2BH_defect'] = dict(
        rows=rows,
        claim='b3 = 2(a1\' - a2) holds with a2 = a2^H and fails by '
              'exactly -4 pi\'^3 F4 with the printed a2^BH included')
    st3_ok = all(abs(v['resid_with_a2H']) < 1e-9
                 and abs(v['resid_printed_minus_defect']) < 1e-9
                 and abs(v['minus_4_pip3_F4']) > 1e-3
                 for v in rows.values())
    res['subtask3_verdict'] = 'REPRODUCED' if st3_ok else 'FAILS'

    res['verdicts'] = dict(
        subtask1_G3_4b_K0_from_action=res['subtask1_K0_from_action']['verdict'],
        subtask2_G3_2_e1_pair=res['subtask2_verdict'],
        subtask3_G3_2_a2BH=res['subtask3_verdict'])
    with open('/home/hatch/workspace/warp-pilot/gate3/results/'
              'v_g3_2.json', 'w') as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps(res['verdicts'], indent=2))
    print(json.dumps(res['subtask1_K0_from_action']['profile'],
                     indent=2))
    print(json.dumps(res['subtask1_K0_from_action']['asymptotics'],
                     indent=2))
    print(json.dumps(res['subtask2_printed_route'], indent=2))
    print(json.dumps(res['subtask3_a2BH_defect'], indent=2))


if __name__ == '__main__':
    main()
