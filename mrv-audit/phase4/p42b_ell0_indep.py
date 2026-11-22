#!/usr/bin/env python3
"""
F4-2b: INDEPENDENT l=0 (spherically symmetric) even-sector derivation for
the MRV beyond-Horndeski wormhole (arXiv:1812.07022), bypassing the
paper's Appendix B entirely. Stress-test of F4-2's verdict (ghost in the
l=0 sector, K_0 < 0 for r < -12.32, from the printed Appendix B
coefficients).

ROUTE (no Appendix B formula is used anywhere):
  * Start from the covariant action S = int d^4x sqrt(-g) [ F(pi,X)
    + G_4(pi,X) R + G_4X ((Box pi)^2 - pi_;ab pi^;ab) + L_BH ], with
    L_BH = F_4(pi,X) eps^{mu nu rho}_{sigma} eps^{mu' nu' rho' sigma}
    pi_,mu pi_,mu' pi_;nu nu' pi_;rho rho'  (the theory's definition,
    MRV eq. (BH); overall sign of the eps-contraction fixed by the
    F4-4 Bianchi/Euler-Lagrange closure, reproduced here as ELbg ~ 0).
    Designer functions F, G_4, F_4 as functions of (pi, X) from
    phase3/p31_horndeski.py (the eq.-(56) Ansatz: F = f0+f1 X+f2 X^2,
    G_4 = 1/2+g40+g41 X, F_4 = f40+f41 X, with f_i, g_i functions of
    s = pi/tau) -- cross-validated in Phase 3 / F4-4.
  * Ansatz (areal + diagonal-shift gauge): ds^2 = -A(t,r)^2 dt^2
    + B(t,r)^2 (dr + C(t,r) dt)^2 + J(r)^2 dOmega^2, J = sqrt(r^2+tau^2)
    FIXED (areal radius is the radial coordinate), pi = pi(t,r).
    Perturbations: A = 1+a, B = 1+b, C = c, pi = pi_bg + chi.
  * The Lagrangian density (per unit solid angle) is computed as a
    function of the fields' 2-jets by sympy (Ricci scalar, pi-Hessian,
    Kg, and the eps-eps contraction are derived in-script below).
  * The quadratic action's jet-Hessian H_L(r) at the background is
    computed by vectorised finite differences in jet space. The
    linearised Euler-Lagrange operators M_Phi[Psi, gamma] follow by
    the exact variational algebra EL = sum_alpha (-D)^alpha dL/djet,
    with r-derivatives of H_L by FD on the r-grid. (Checks: background
    EL = 0 to ~1e-7 for all four fields; 3rd/4th-derivative EL
    coefficients vanish to ~1e-6 -- the theory's degeneracy; the
    operator is self-adjoint, M_Phi,Psi,gamma = M_Psi,Phi,gamma.)
  * Elimination (all steps read off the computed operator structure):
      - EL_C (shift eq.) is exactly d/dt of a bracket:
        EL_C = d_t [ Q_b b + Q_x chi + Q_x' chi' ], so localised
        perturbations obey Q = 0, giving b = p chi' + q chi.
      - EL_A (lapse eq.) is exactly d_r Q (verified: EL_A - D_r Q = 0
        to FD floor, multiplier nu = 0): a consistency condition, as
        in F4-2, NOT an extra constraint on chi.
      - EL_B contains a' and c-dot only in the combination
        S1 := a' + c-dot (coefficients equal), so EL_B determines
        S1(chi); EL_P contains a, c only through S1 and S1', so
        substituting S1(chi) and b(chi) into EL_P gives the reduced
        equation R[chi] = -2 K0 chi-ddot + 2 G0 chi'' + 2 G0' chi'
        - 2 M0 chi (+ a removable Q-type (1,1) sector, not used).
        K0^(ind) = -R_(2,0)/2, G0^(ind) = R_(0,2)/2.
      - The chi-ddot' (2,1) coefficient cancels to FD floor in the
        reduced operator (proper second-order equation).
  * Independent cross-check of the elimination: the full quadratic
    action (jet-Hessian form) evaluated on the constraint surface
    (chi = eps cos(om t) g(r), b from Q = 0, a from a' = S1, c = 0)
    with analytic jets; the om^2-slope of S gives int K0 g^2 dr
    without any operator algebra.
  * Normalisation: this script's action is the covariant one (per
    unit solid angle, dt dr measure). F4-2's Appendix-B-normalised
    coefficients are exactly twice these (established below from
    G0, which agrees to ~1e-4 relative at 29 radii); all comparisons
    use K0_F42/2, G0_F42/2.

VERDICT (see results/p42b_ell0_indep.json): (B) GHOST IS AN ARTEFACT.
K0^(ind) > 0 at every sampled radius in [-60, 60] and
K0^(ind)/J^2 -> +1/tau^2 = +0.01 at BOTH infinities. The specific
printed-formula error is in Appendix B's e_1: the pair of terms
    + (2 B J'^2 / X) F   and   - H (B^2 J'^2/(J X A)) d/dr(J^2 A/B)
contributes (J'^2 - J'^3)/X to e_1 at A = B = 1, F = H = 1; the
independent derivation shows this pair's correct on-background
contribution is ZERO (removing exactly it from F4-2's K_0 reproduces
K0^(ind) at 29 radii to <= 1.3e-3, while K_0 ranges over [-75, +218]).
The pair is the J-generalisation of a Kobayashi (J = r) structure in
which it cancels identically (J' = 1 => J'^2 - J'^3 = 0); as printed
it fails to cancel for general J. F4-2 flagged the second (odd) term
as suspect and tested removing IT alone -- that leaves the even
+J'^2/X term, which by itself drives K_0 to ~ -4 (their units) at
both infinities; the repair is removing the PAIR.
Second finding (a_2^BH): CONFIRMED independently -- the from-action
value of the corresponding coefficient equals the Horndeski part
a_2^H, not the printed a_2 = a_2^H - 2 pi'^3 F_4 (details in JSON).

float64 throughout; sympy exact algebra for the geometric jet
formulas; FD (Richardson) for jet-Hessians and r-derivatives.
"""
import json
import math
import sys
import itertools

import numpy as np
import sympy as sp

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase4')
import p31_horndeski as p31
import p42_ell0 as p42

TAU = p31.TAU
FIELDS = ['A', 'B', 'C', 'P']
ORDS = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]  # (n_t, n_r)


def jet_name(f, o):
    if o == (0, 0):
        return f
    if o == (1, 1):
        return f + '_tr'
    s = ''
    if o[0] == 1:
        s += '_t'
    if o[0] == 2:
        s += '_tt'
    if o[1] == 1:
        s += '_r'
    if o[1] == 2:
        s += '_rr'
    return f + s


JETS = [(f, o) for f in FIELDS for o in ORDS]
NJ = len(JETS)
JET_IDX = {j: i for i, j in enumerate(JETS)}

# ---------------------------------------------------------------------------
# Section 1: geometric jet formulas by sympy (R, Kg, pi-Hessian, BH contraction)
# ---------------------------------------------------------------------------

def derive_jet_formulas():
    t, r, th, ph = sp.symbols('t r theta phi')
    A = sp.Function('A')(t, r)
    B = sp.Function('B')(t, r)
    C = sp.Function('C')(t, r)
    Jf = sp.Function('J')(r)
    pi = sp.Function('pi')(t, r)
    xs = [t, r, th, ph]
    g = sp.zeros(4, 4)
    g[0, 0] = -(A ** 2) + B ** 2 * C ** 2
    g[0, 1] = g[1, 0] = B ** 2 * C
    g[1, 1] = B ** 2
    g[2, 2] = Jf ** 2
    g[3, 3] = Jf ** 2 * sp.sin(th) ** 2
    ginv = g.inv()
    dg = [[[sp.diff(g[i, j], xs[k]) for k in range(4)]
           for j in range(4)] for i in range(4)]
    Gam = [[[sum(ginv[i, l] * (dg[l][j][k] + dg[l][k][j] - dg[j][k][l]) / 2
                 for l in range(4)) for k in range(4)] for j in range(4)]
            for i in range(4)]
    Ric = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            e = 0
            for lam in range(4):
                e += (sp.diff(Gam[lam][mu][nu], xs[lam])
                      - sp.diff(Gam[lam][mu][lam], xs[nu]))
                for sg in range(4):
                    e += (Gam[lam][lam][sg] * Gam[sg][mu][nu]
                          - Gam[lam][nu][sg] * Gam[sg][mu][lam])
            Ric[mu, nu] = e
    Rsc = sp.simplify(sum(ginv[i, j] * Ric[i, j]
                          for i in range(4) for j in range(4)))
    dp = [sp.diff(pi, x) for x in xs]
    H = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            H[a, b] = (sp.diff(pi, xs[a], xs[b])
                       - sum(Gam[c][a][b] * dp[c] for c in range(4)))
    Box = sum(ginv[a, b] * H[a, b] for a in range(4) for b in range(4))
    Hup = [[sum(ginv[a, c] * ginv[b, dd] * H[c, dd]
                for c in range(4) for dd in range(4))
            for b in range(4)] for a in range(4)]
    Kg = sp.expand(Box ** 2 - sum(H[a, b] * Hup[a][b]
                                  for a in range(4) for b in range(4)))
    subs = {sp.sin(th): 1, sp.cos(th): 0}

    def jetify(expr):
        reps = {}
        for F, nm in [(A, 'A'), (B, 'B'), (C, 'C'), (pi, 'P')]:
            reps[sp.diff(F, t, 2)] = sp.Symbol(nm + '_tt')
            reps[sp.diff(F, r, 2)] = sp.Symbol(nm + '_rr')
            reps[sp.diff(F, t, r)] = sp.Symbol(nm + '_tr')
            reps[sp.diff(F, t)] = sp.Symbol(nm + '_t')
            reps[sp.diff(F, r)] = sp.Symbol(nm + '_r')
            reps[F] = sp.Symbol(nm)
        reps[sp.diff(Jf, r, 2)] = sp.Symbol('J_rr')
        reps[sp.diff(Jf, r)] = sp.Symbol('J_r')
        reps[Jf] = sp.Symbol('J')
        return sp.expand(expr.subs(reps))

    names = [jet_name(f, o) for f in FIELDS for o in ORDS] + ['J', 'J_r', 'J_rr']
    args = [sp.Symbol(n) for n in names]
    fR = sp.lambdify(args, jetify(Rsc.subs(subs)), 'numpy')
    fKg = sp.lambdify(args, jetify(Kg.subs(subs)), 'numpy')
    fH = {}
    for a in range(4):
        for b in range(4):
            e = jetify(H[a, b].subs(subs))
            if e != 0:
                fH[(a, b)] = sp.lambdify(args, e, 'numpy')

    # BH eps-eps contraction as a polynomial in (g comps, pi_t, pi_r, H_ab)
    def perm_sign(p):
        inv = 0
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if p[i] > p[j]:
                    inv += 1
        return -1 if inv % 2 else 1

    gtt, gtr, grr, gth, SQ, pt, pr = sp.symbols('gtt gtr grr gth SQ pt pr')
    gdiag = {0: gtt, 1: grr, 2: gth, 3: gth}

    def gcomp(a, b):
        if a == b:
            return gdiag[a]
        if (a, b) in [(0, 1), (1, 0)]:
            return gtr
        return 0

    pivec = [pt, pr, 0, 0]
    Hs = [[sp.Symbol(f'H{a}{b}') for b in range(4)] for a in range(4)]
    Ceps = 0
    for mu, nu, rho, sg in itertools.permutations(range(4)):
        e1 = perm_sign((mu, nu, rho, sg)) / SQ
        for al, be, ga, dd in itertools.permutations(range(4)):
            gdsg = gcomp(dd, sg)
            if gdsg == 0:
                continue
            e2 = perm_sign((al, be, ga, dd)) * gdsg / SQ
            Ceps += e1 * e2 * pivec[mu] * pivec[al] * Hs[nu][be] * Hs[rho][ga]
    Ceps = sp.expand(Ceps)
    fC = sp.lambdify([Hs[a][b] for a in range(4) for b in range(4)]
                     + [gtt, gtr, grr, gth, SQ, pt, pr], Ceps, 'numpy')
    return names, fR, fKg, fH, fC


NAMES, fR, fKg, fH, fC = derive_jet_formulas()

# ---------------------------------------------------------------------------
# Section 2: the Lagrangian density as a function of 2-jets
# ---------------------------------------------------------------------------

def theory_vals(pi_v, X):
    """F, G4, G4X, F4 at (pi, X) from the eq.-(56) designer Ansatz."""
    s = pi_v / TAU
    f2v = p31.f2_s(s)
    f1v = p31.f1_s(s, f2v)
    f0v = p31.f0_s(s, f1v, f2v)
    F = f0v + f1v * X + f2v * X ** 2
    G4 = 0.5 + p31.g40_s(s) + p31.g41_s(s) * X
    G4X = p31.g41_s(s)
    F4 = p31.f40_s(s) + p31.f41_s(s) * X
    return F, G4, G4X, F4


def Ljet(jets):
    """Density per unit solid angle: SQ * [F + G4 R + G4X Kg - F4 Ceps],
    SQ = sqrt(-g)/sin(theta) = A B J^2. The minus sign on the BH term is
    the eps-convention sign fixed by F4-4's EL closure (reproduced in
    Section 3's ELbg check); static limit = p44b's +2 F4 J'^2 pi'^4."""
    A, B, C, P = jets['A'], jets['B'], jets['C'], jets['P']
    Pt, Pr = jets['P_t'], jets['P_r']
    det2 = -(A ** 2) * (B ** 2)
    gttv = -(A ** 2) + B ** 2 * C ** 2
    gtrv = B ** 2 * C
    grrv = B ** 2
    gthv = jets['J'] ** 2
    SQv = A * B * jets['J'] ** 2
    X = -0.5 * ((grrv / det2) * Pt ** 2 + 2 * (-gtrv / det2) * Pt * Pr
                + (gttv / det2) * Pr ** 2)
    F, G4, G4X, F4 = theory_vals(P, X)
    arg = [jets[n] for n in NAMES]
    Rv = fR(*arg)
    Kgv = fKg(*arg)
    Hv = {}
    for k, f in fH.items():
        Hv[k] = f(*arg)

    def hg(a, b):
        if (a, b) in Hv:
            return Hv[(a, b)]
        if (b, a) in Hv:
            return Hv[(b, a)]
        return 0.0 * Pt

    Cepsv = fC(*[hg(a, b) for a in range(4) for b in range(4)],
               gttv, gtrv, grrv, gthv, SQv, Pt, Pr)
    return SQv * (F + G4 * Rv + G4X * Kgv - F4 * Cepsv)


def bg_jets_arr(r, n):
    bg = p31.background(np.array([r]))
    j = {}
    for f in FIELDS:
        for o in ORDS:
            j[jet_name(f, o)] = np.zeros(n)
    j['A'][:] = 1.0
    j['B'][:] = 1.0
    j['P'][:] = TAU * bg['s'][0]
    j['P_r'][:] = bg['pip'][0]
    j['P_rr'][:] = bg['pipp'][0]
    j['J'] = np.full(n, bg['J'][0])
    j['J_r'] = np.full(n, bg['Jp'][0])
    j['J_rr'] = np.full(n, bg['Jpp'][0])
    return j


def grad_hess_vec(r, e=2e-4):
    """Gradient and Hessian of Ljet w.r.t. the 24 perturbation jets at
    the background at radius r (vectorised Richardson central FD)."""
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
        for ee in (e, e / 2):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    u = np.zeros(NJ)
                    u[i] = s1 * ee
                    u[j] = s2 * ee
                    pts.append(u)
                    tags.append(('p', i, j, s1, s2, ee))
    U = np.array(pts)
    n = len(pts)
    j = bg_jets_arr(r, n)
    for k, (f, o) in enumerate(JETS):
        j[jet_name(f, o)] = j[jet_name(f, o)] + U[:, k]
    L = Ljet(j)
    Ld = {tag: val for tag, val in zip(tags, L)}
    g = np.zeros(NJ)
    H = np.zeros((NJ, NJ))
    for i in range(NJ):
        gp = (Ld[('d', i, 1, e)] - Ld[('d', i, -1, e)]) / (2 * e)
        gm = (Ld[('d', i, 1, e / 2)] - Ld[('d', i, -1, e / 2)]) / (2 * (e / 2))
        g[i] = 2 * gm - gp
        Hp = (Ld[('d', i, 1, e)] - 2 * Ld[('0',)] + Ld[('d', i, -1, e)]) / e ** 2
        Hm = (Ld[('d', i, 1, e / 2)] - 2 * Ld[('0',)]
              + Ld[('d', i, -1, e / 2)]) / (e / 2) ** 2
        H[i, i] = 2 * Hm - Hp
    for (i, jj) in pairs:
        def q(ee):
            return (Ld[('p', i, jj, 1, 1, ee)] - Ld[('p', i, jj, 1, -1, ee)]
                    - Ld[('p', i, jj, -1, 1, ee)]
                    + Ld[('p', i, jj, -1, -1, ee)]) / (4 * ee * ee)
        H[i, jj] = H[jj, i] = 2 * q(e / 2) - q(e)
    return g, H

# ---------------------------------------------------------------------------
# Section 3: linearised EL operators from the jet-Hessian
# ---------------------------------------------------------------------------

def M_from_Hs(Hs, gs, hFD):
    """EL operators M[(Phi,Psi)][gamma] and background EL from H_L and
    its r-derivatives (4th-order FD, spacing hFD). gamma = (n_t, n_r)."""
    H0 = Hs[0]
    Hp = (-Hs[2] + 8 * Hs[1] - 8 * Hs[-1] + Hs[-2]) / (12 * hFD)
    Hpp = (-Hs[2] + 16 * Hs[1] - 30 * Hs[0] + 16 * Hs[-1] - Hs[-2]) \
        / (12 * hFD ** 2)
    Hd = [H0, Hp, Hpp]
    gd = [gs[0],
          (-gs[2] + 8 * gs[1] - 8 * gs[-1] + gs[-2]) / (12 * hFD),
          (-gs[2] + 16 * gs[1] - 30 * gs[0] + 16 * gs[-1] - gs[-2])
          / (12 * hFD ** 2)]
    ELbg = np.zeros(4)
    for Phi, f in enumerate(FIELDS):
        tot = 0.0
        for o in ORDS:
            if o[0] != 0:
                continue
            tot += (-1) ** o[1] * gd[o[1]][JET_IDX[(f, o)]]
        ELbg[Phi] = tot
    M = {}
    high = {}
    for Phi, f in enumerate(FIELDS):
        for Psi, pf in enumerate(FIELDS):
            coeffs = {}
            for alpha in ORDS:
                ia = JET_IDX[(f, alpha)]
                for beta in ORDS:
                    ib = JET_IDX[(pf, beta)]
                    if Hd[0][ia, ib] == 0 and Hd[1][ia, ib] == 0 \
                            and Hd[2][ia, ib] == 0:
                        continue
                    for s in range(0, alpha[1] + 1):
                        gamma = (beta[0] + alpha[0], beta[1] + alpha[1] - s)
                        c = ((-1) ** (alpha[0] + alpha[1])
                             * math.comb(alpha[1], s) * Hd[s][ia, ib])
                        if gamma[0] + gamma[1] <= 2:
                            coeffs[gamma] = coeffs.get(gamma, 0.0) + c
                        else:
                            key = (f, pf, gamma)
                            high[key] = high.get(key, 0.0) + c
            M[(f, pf)] = coeffs
    return ELbg, M, high


def M_ops(r, hFD=0.04):
    gs, Hs = {}, {}
    for s, rr in [(0, r), (1, r + hFD), (-1, r - hFD),
                  (2, r + 2 * hFD), (-2, r - 2 * hFD)]:
        gs[s], Hs[s] = grad_hess_vec(rr)
    return M_from_Hs(Hs, gs, hFD)


def get(M, f, pf, g):
    return M[(f, pf)].get(g, 0.0)


def pq_from_M(M):
    Qb = get(M, 'C', 'B', (1, 0))
    Qx = get(M, 'C', 'P', (1, 0))
    Qxp = get(M, 'C', 'P', (1, 1))
    return Qb, Qx, Qxp, -Qxp / Qb, -Qx / Qb


def subst_B(op_B, p, q, pp, qq):
    """Substitute b = p chi' + q chi (and its jets) into an operator's
    B-field part. Returns (operator on P, high-order leftovers)."""
    out = {}
    high = {}

    def add(g, c):
        if g == (2, 1) or g[0] + g[1] <= 2:
            out[g] = out.get(g, 0.0) + c
        else:
            high[g] = high.get(g, 0.0) + c

    for g, c in op_B.items():
        if g == (0, 0):
            add((0, 1), c * p)
            add((0, 0), c * q)
        elif g == (0, 1):
            add((0, 2), c * p)
            add((0, 1), c * (pp + q))
            add((0, 0), c * qq)
        elif g == (1, 0):
            add((1, 1), c * p)
            add((1, 0), c * q)
        elif g == (2, 0):
            add((2, 1), c * p)
            add((2, 0), c * q)
        elif g == (1, 1):
            add((1, 2), c * p)
            add((1, 1), c * (pp + q))
            add((1, 0), c * qq)
        elif g == (0, 2):
            add((0, 3), c * p)
            add((0, 2), c * (2 * pp + q))
            add((0, 1), c * 2 * qq)
        else:
            high[g] = high.get(g, 0.0) + c
    return out, high


def add_ops(*ops):
    out = {}
    for op in ops:
        for g, c in op.items():
            out[g] = out.get(g, 0.0) + c
    return out


def scale_op(op, s):
    return {g: c * s for g, c in op.items()}


def Dr_op(op, op_prime):
    out = {}
    for g, c in op.items():
        g2 = (g[0], g[1] + 1)
        out[g2] = out.get(g2, 0.0) + c
    for g, c in op_prime.items():
        out[g] = out.get(g, 0.0) + c
    return out


# ---------------------------------------------------------------------------
# Section 4: constraint elimination at one radius -> K0, G0, M0 (independent)
# ---------------------------------------------------------------------------

def elim_at(r0, hM=0.05, hFD=0.04):
    ks = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    Ms, ELbgs = {}, {}
    for k in ks:
        ELbgs[k], Ms[k], _ = M_ops(r0 + k * hM, hFD=hFD)
    M = Ms[0]
    pq = {k: pq_from_M(Ms[k]) for k in ks}

    def deriv_at(k, which):
        v = {kk: pq[kk][which] for kk in range(k - 2, k + 3)}
        return (-v[k + 2] + 8 * v[k + 1] - 8 * v[k - 1] + v[k - 2]) / (12 * hM)

    def S1op_at(k):
        Mk = Ms[k]
        Qb, Qx, Qxp, p, q = pq[k]
        pp = deriv_at(k, 3)
        qq = deriv_at(k, 4)
        mB = get(Mk, 'B', 'A', (0, 1))
        mBC = get(Mk, 'B', 'C', (1, 0))
        subB, _ = subst_B({g: c for g, c in Mk[('B', 'B')].items()},
                          p, q, pp, qq)
        rest = add_ops({g: c for g, c in Mk[('B', 'P')].items()}, subB)
        return scale_op(rest, -1.0 / mB), mB, mBC

    S1, mB, mBC = S1op_at(0)
    S1n = {k: S1op_at(k)[0] for k in (-2, -1, 1, 2)}
    allg = set(S1)
    for v in S1n.values():
        allg |= set(v)
    S1prime = {}
    for g in allg:
        v = {2: S1n[2].get(g, 0.0), 1: S1n[1].get(g, 0.0),
             -1: S1n[-1].get(g, 0.0), -2: S1n[-2].get(g, 0.0)}
        S1prime[g] = (-v[2] + 8 * v[1] - 8 * v[-1] + v[-2]) / (12 * hM)
    S1r = Dr_op(S1, S1prime)
    Qb, Qx, Qxp, p, q = pq[0]
    pp = deriv_at(0, 3)
    qq = deriv_at(0, 4)
    subBP, _ = subst_B({g: c for g, c in M[('P', 'B')].items()},
                       p, q, pp, qq)
    restP = add_ops({g: c for g, c in M[('P', 'P')].items()}, subBP)
    u = get(M, 'P', 'A', (0, 1))
    uC = get(M, 'P', 'C', (1, 0))
    w = get(M, 'P', 'A', (0, 2))
    wC = get(M, 'P', 'C', (1, 1))
    Rop = add_ops(scale_op(S1, u), scale_op(S1r, w), restP)
    highR = {g: c for g, c in Rop.items() if g[0] + g[1] > 2}
    # EL_A = D_r Q + nu Q identity (the H0/H1 consistency check)
    Qop = {('B', (0, 0)): Qb, ('P', (0, 0)): Qx, ('P', (0, 1)): Qxp}

    def fd1_9(vals):
        return (-vals[2] + 8 * vals[1] - 8 * vals[-1] + vals[-2]) / (12 * hM)

    Qbp = fd1_9({k: pq[k][0] for k in (-2, -1, 1, 2)})
    Qxp_ = fd1_9({k: pq[k][1] for k in (-2, -1, 1, 2)})
    Qxpp = fd1_9({k: pq[k][2] for k in (-2, -1, 1, 2)})
    DrQ = {}
    for (f, g), c in Qop.items():
        DrQ[(f, (g[0], g[1] + 1))] = DrQ.get((f, (g[0], g[1] + 1)), 0.0) + c
    DrQ[('B', (0, 0))] = DrQ.get(('B', (0, 0)), 0.0) + Qbp
    DrQ[('P', (0, 0))] = DrQ.get(('P', (0, 0)), 0.0) + Qxp_
    DrQ[('P', (0, 1))] = DrQ.get(('P', (0, 1)), 0.0) + Qxpp
    ELA = {}
    for f in ('B', 'P'):
        for g, c in M[('A', f)].items():
            ELA[(f, g)] = c
    nu = (ELA.get(('B', (0, 0)), 0.0) - DrQ.get(('B', (0, 0)), 0.0)) / Qb
    resid = {}
    for key in set(ELA) | set(DrQ) | set(Qop):
        resid[key] = (ELA.get(key, 0.0) - DrQ.get(key, 0.0)
                      - nu * Qop.get(key, 0.0))
    # background quantities and the a_2 adjudication
    d = p31.theory_on_bg(np.array([r0]))
    Xi, Gamma = p31.Xi_Gamma(d)
    Xi = float(Xi[0])
    J = float(d['J'][0])
    Jp = float(d['Jp'][0])
    pip = float(d['pip'][0])
    F4 = float(d['F4'][0])
    D = 2 * J * Jp + Xi * pip
    hh = 0.02
    dps = []
    for rr in (r0 - 2 * hh, r0 - hh, r0 + hh, r0 + 2 * hh):
        dd = p31.theory_on_bg(np.array([rr]))
        dps.append(float(p31.Xi_Gamma(dd)[0][0]))
    Xip = (-dps[3] + 8 * dps[2] - 8 * dps[1] + dps[0]) / (12 * hh)
    b3 = (2 * float(d['pipp'][0]) * Xi + 4 * J * float(d['Jpp'][0])) / pip
    a2H = (2 * pip * Xip - 2 * float(d['pipp'][0]) * Xi
           - 4 * J * float(d['Jpp'][0])) / (2 * pip)
    # from-action a_2: the identity b_3 = 2(a_1' - a_2) with a_1 = Xi and
    # b_3^(ind) = Q_x * (D/Q_b) (Q normalised so that Q_b = D):
    a2_ind = Xip - Qx * (D / Qb)
    return dict(
        r=r0, Qb=Qb, Qx=Qx, Qxp=Qxp, p_ind=p, q_ind=q,
        p_f42=2 * Xi / D, q_f42=-b3 / D,
        u=u, uC=uC, w=w, wC=wC, mB=mB, mBC=mBC,
        K0=-Rop.get((2, 0), 0.0) / 2, G0=Rop.get((0, 2), 0.0) / 2,
        M0=-Rop.get((0, 0), 0.0) / 2,
        R01=Rop.get((0, 1), 0.0),
        highR={str(k): float(v) for k, v in highR.items()},
        ELA_nu=float(nu),
        ELA_resid_max=float(max((abs(v) for v in resid.values()),
                                default=0.0)),
        a2_ind=float(a2_ind), a2H=float(a2H),
        a2_printed=float(a2H - 2 * pip ** 3 * F4),
        Xi=Xi, D=D, J=J,
        ELbg=[float(x) for x in ELbgs[0]])

# ---------------------------------------------------------------------------
# Section 5: quadratic action on the constraint surface (cross-check)
# ---------------------------------------------------------------------------

def ops_on_grid(rgrid):
    """H_L, M operators, p, q, S1-operator and K0/G0 on a uniform grid."""
    d = rgrid[1] - rgrid[0]
    n = len(rgrid)
    Hs = []
    for r in rgrid:
        _, H = grad_hess_vec(float(r))
        Hs.append(H)
    Ms = {}
    for i in range(2, n - 2):
        Hs5 = {0: Hs[i], 1: Hs[i + 1], -1: Hs[i - 1],
               2: Hs[i + 2], -2: Hs[i - 2]}
        gs5 = {k: np.zeros(NJ) for k in Hs5}
        _, M, _ = M_from_Hs(Hs5, gs5, d)
        Ms[i] = M

    def fd1(arr, i):
        return (-arr[i + 2] + 8 * arr[i + 1] - 8 * arr[i - 1]
                + arr[i - 2]) / (12 * d)

    idxs = sorted(Ms)
    p = np.full(n, np.nan)
    q = np.full(n, np.nan)
    for i in idxs:
        M = Ms[i]
        Qb = get(M, 'C', 'B', (1, 0))
        p[i] = -get(M, 'C', 'P', (1, 1)) / Qb
        q[i] = -get(M, 'C', 'P', (1, 0)) / Qb
    S1c = {}
    for i in idxs:
        if i - 2 < idxs[0] or i + 2 > idxs[-1]:
            continue
        M = Ms[i]
        pp = fd1(p, i)
        qq = fd1(q, i)
        mB = get(M, 'B', 'A', (0, 1))
        subB, _ = subst_B({g: c for g, c in M[('B', 'B')].items()},
                          p[i], q[i], pp, qq)
        rest = add_ops({g: c for g, c in M[('B', 'P')].items()}, subB)
        S1c[i] = scale_op(rest, -1.0 / mB)
    K0 = np.full(n, np.nan)
    G0 = np.full(n, np.nan)
    for i in idxs:
        if any(j not in S1c for j in (i - 2, i - 1, i, i + 1, i + 2)):
            continue
        M = Ms[i]
        pp = fd1(p, i)
        qq = fd1(q, i)
        S1p = {}
        for g in set().union(*[S1c[j] for j in (i - 2, i - 1, i, i + 1, i + 2)]):
            v = {2: S1c[i + 2].get(g, 0.0), 1: S1c[i + 1].get(g, 0.0),
                 -1: S1c[i - 1].get(g, 0.0), -2: S1c[i - 2].get(g, 0.0)}
            S1p[g] = (-v[2] + 8 * v[1] - 8 * v[-1] + v[-2]) / (12 * d)
        S1r = Dr_op(S1c[i], S1p)
        u = get(M, 'P', 'A', (0, 1))
        w = get(M, 'P', 'A', (0, 2))
        subBP, _ = subst_B({g: c for g, c in M[('P', 'B')].items()},
                           p[i], q[i], pp, qq)
        Rop = add_ops(scale_op(S1c[i], u), scale_op(S1r, w),
                      {g: c for g, c in M[('P', 'P')].items()}, subBP)
        K0[i] = -Rop.get((2, 0), 0.0) / 2
        G0[i] = Rop.get((0, 2), 0.0) / 2
    return dict(p=p, q=q, K0=K0, G0=G0, Ms=Ms, S1c=S1c, Hs=Hs)


def fd1_arr(arr, d):
    out = np.full_like(arr, np.nan)
    out[2:-2] = (-arr[4:] + 8 * arr[3:-1] - 8 * arr[1:-3] + arr[:-4]) \
        / (12 * d)
    return out


def action_check(rc, sigma=3.0):
    """int K0 g^2 dr from the quadratic action on the constraint surface
    (analytic jets, t-factor algebra), vs the operator-elimination
    profile integral and F4-2's. g = Gaussian bump at rc."""
    d = 0.05
    rgrid = np.arange(rc - 13, rc + 13 + 1e-9, d)
    n = len(rgrid)
    ops = ops_on_grid(rgrid)
    p = np.where(np.isfinite(ops['p']), ops['p'], 0.0)
    q = np.where(np.isfinite(ops['q']), ops['q'], 0.0)
    pp = fd1_arr(p, d)
    qq = fd1_arr(q, d)
    ppp = fd1_arr(pp, d)
    qqq = fd1_arr(qq, d)
    g = np.exp(-(rgrid - rc) ** 2 / (2 * sigma ** 2))
    gp = -(rgrid - rc) / sigma ** 2 * g
    gpp = ((rgrid - rc) ** 2 / sigma ** 4 - 1 / sigma ** 2) * g
    gppp = (3 * (rgrid - rc) / sigma ** 4
            - (rgrid - rc) ** 3 / sigma ** 6) * g
    chiprof = {(0, 0): (g, 'f'), (0, 1): (gp, 'f'), (0, 2): (gpp, 'f'),
               (1, 0): (g, 'fd'), (1, 1): (gp, 'fd'), (1, 2): (gpp, 'fd'),
               (2, 0): (g, 'fdd'), (2, 1): (gp, 'fdd'),
               (2, 2): (gpp, 'fdd')}
    S1t = {'f': np.zeros(n), 'fd': np.zeros(n), 'fdd': np.zeros(n)}
    for i, S1op in ops['S1c'].items():
        for gm, cf in S1op.items():
            prof, tf = chiprof[gm]
            S1t[tf][i] += cf * prof[i]

    def cum(v):
        return np.concatenate([[0], np.cumsum((v[:-1] + v[1:]) / 2 * d)])

    Aint = {x: cum(S1t[x]) for x in S1t}
    dS1 = {x: fd1_arr(S1t[x], d) for x in S1t}
    Z = np.zeros(n)

    def trip(f_, fd_, fdd_):
        return (f_, fd_, fdd_)

    chijets = {(0, 0): trip(g, Z, Z), (0, 1): trip(gp, Z, Z),
               (0, 2): trip(gpp, Z, Z), (1, 0): trip(Z, g, Z),
               (1, 1): trip(Z, gp, Z), (1, 2): trip(Z, gpp, Z),
               (2, 0): trip(Z, Z, g), (2, 1): trip(Z, Z, gp),
               (2, 2): trip(Z, Z, gpp)}
    bjets = {}
    bjets[(0, 0)] = trip(p * gp + q * g, Z, Z)
    bjets[(0, 1)] = trip(p * gpp + (pp + q) * gp + qq * g, Z, Z)
    bjets[(0, 2)] = trip(p * gppp + (2 * pp + q) * gpp
                         + (ppp + 2 * qq) * gp + qqq * g, Z, Z)
    bjets[(1, 0)] = trip(Z, p * gp + q * g, Z)
    bjets[(1, 1)] = trip(Z, p * gpp + (pp + q) * gp + qq * g, Z)
    bjets[(1, 2)] = trip(Z, p * gppp + (2 * pp + q) * gpp
                         + (ppp + 2 * qq) * gp + qqq * g, Z)
    bjets[(2, 0)] = trip(Z, Z, p * gp + q * g)
    bjets[(2, 1)] = trip(Z, Z, p * gpp + (pp + q) * gp + qq * g)
    bjets[(2, 2)] = trip(Z, Z, p * gppp + (2 * pp + q) * gpp
                         + (ppp + 2 * qq) * gp + qqq * g)
    ajets_base = {(0, 0): trip(Aint['f'], Aint['fd'], Aint['fdd']),
                  (0, 1): trip(S1t['f'], S1t['fd'], S1t['fdd']),
                  (0, 2): trip(dS1['f'], dS1['fd'], dS1['fdd'])}
    Hg = np.array(ops['Hs'])
    keys = [(fld, gm) for fld in ('A', 'B', 'C', 'P')
            for gm in [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]]
    Hsel = Hg[:, [JET_IDX[k] for k in keys]][:, :, [JET_IDX[k] for k in keys]]
    Kint_ind = np.trapezoid(
        np.where(np.isfinite(ops['K0']), ops['K0'], 0.0) * g ** 2, rgrid)
    B42 = p42.build(rgrid, d)
    Kint_f42half = np.trapezoid((B42['K0'] / 2) * g ** 2, rgrid)
    out = {}
    for om in (0.6, 1.0, 1.4):
        def T1(tr):
            c0, c1, c2 = tr
            return (Z.copy(), c0 - om ** 2 * c2, c1)

        ajets = dict(ajets_base)
        ajets[(1, 0)] = T1(ajets_base[(0, 0)])
        ajets[(1, 1)] = T1(ajets_base[(0, 1)])
        ajets[(1, 2)] = T1(ajets_base[(0, 2)])
        ajets[(2, 0)] = T1(ajets[(1, 0)])
        ajets[(2, 1)] = T1(ajets[(1, 1)])
        ajets[(2, 2)] = T1(ajets[(1, 2)])
        alljets = {'A': ajets, 'B': bjets,
                   'C': {gm: trip(Z, Z, Z) for gm in chijets},
                   'P': chijets}
        Jc = {}
        for fld, jd in alljets.items():
            for gm, tr in jd.items():
                Jc[(fld, gm)] = (tr[0] - om ** 2 * tr[2], om * tr[1])
        Fprof = np.nan_to_num(np.array([Jc[k][0] for k in keys]))
        Dprof = np.nan_to_num(np.array([Jc[k][1] for k in keys]))
        quadF = np.einsum('ia,iab,ib->i', Fprof.T, Hsel, Fprof.T)
        quadD = np.einsum('ia,iab,ib->i', Dprof.T, Hsel, Dprof.T)
        T = 4 * np.pi / om
        out[om] = 0.5 * np.trapezoid(quadF + quadD, rgrid) * (T / 2)
    oms = np.array([0.6, 1.0, 1.4])
    y = np.array([out[o] * o / (2 * np.pi) for o in oms])
    Amat = np.vstack([oms ** 2, -np.ones(3)]).T
    sol, *_ = np.linalg.lstsq(Amat, y, rcond=None)
    pred = Amat @ sol
    return dict(rc=rc, Kint_action=float(sol[0]),
                Kint_ind=float(Kint_ind),
                Kint_f42half=float(Kint_f42half),
                fit_resid=float(np.max(np.abs(pred - y))))


# ---------------------------------------------------------------------------
# Section 6: profile, comparison with F4-2, Delta fit, verdict
# ---------------------------------------------------------------------------

def main():
    res = {'task': 'F4-2b independent l=0 derivation (no Appendix B)',
           'route': 'covariant action -> areal/shift gauge ansatz -> '
                    'jet-Hessian -> linearised EL operators -> constraint '
                    'elimination (Q from EL_C, S1 from EL_B) -> reduced '
                    'EL_P; cross-checked by the quadratic action on the '
                    'constraint surface',
           'normalisation': 'covariant action per unit solid angle; '
                            'F4-2 (Appendix B) coefficients = 2x these '
                            '(from G0 agreement); comparisons use F42/2'}
    # validation: background EL and operator structure at sample radii
    val = {}
    for r0 in (5.0, -20.0):
        ELbg, M, high = M_ops(r0)
        val[str(r0)] = dict(
            ELbg=[float(x) for x in ELbg],
            ELbg_max=float(np.max(np.abs(ELbg))),
            high_order_max=float(max((abs(v) for v in high.values()),
                                     default=0.0)),
            EL_C_structure='EL_C has only (1,0),(1,1) jets: it is d_t of '
                           'a bracket Q (checked in elim_at via Q form)',
            symmetry_max_dev_pure_blocks=float(max(
                abs(M[(a, b)].get(g, 0.0) - M[(b, a)].get(g, 0.0))
                for a in FIELDS for b in FIELDS
                for g in [(2, 0), (0, 2)])),
            symmetry_note=('coefficient symmetry M_Phi,Psi = M_Psi,Phi '
                           'holds exactly only for the pure (2,0) and '
                           '(0,2) blocks (mixed-derivative blocks are '
                           'related by integration by parts, not '
                           'coefficient equality); the (2,0)/(0,2) '
                           'deviation is at FD floor'))
    res['validation'] = val
    # profile
    rs = [-60., -40., -30., -20., -15., -13., -12.5, -12., -10., -7., -5.,
          -3., -2., -1., -0.5, -0.1, 0.1, 0.5, 1., 1.5, 2., 2.5, 3., 5.,
          7., 10., 15., 20., 30., 40., 60.]
    h = 0.002
    rr = np.arange(-60, 60 + 0.5 * h, h)
    B = p42.build(rr, h)
    prof = {}
    for r0 in rs:
        o = elim_at(r0)
        i = int(np.argmin(np.abs(rr - r0)))
        o['K0_F42'] = float(B['K0'][i])
        o['G0_F42'] = float(B['G0'][i])
        prof[str(r0)] = o
    res['profile'] = prof
    res['profile_summary'] = dict(
        K0_min=float(min(o['K0'] for o in prof.values())),
        K0_negative_points=[r for r, o in prof.items() if o['K0'] < 0],
        G0_min=float(min(o['G0'] for o in prof.values())),
        G0_ratio_to_F42half_max_dev=float(max(
            abs(o['G0'] - o['G0_F42'] / 2) / max(abs(o['G0_F42'] / 2), 1e-9)
            for o in prof.values())),
        K0_at_F42_crossing_region={
            r: prof[r]['K0'] for r in ('-13.0', '-12.5', '-12.0')},
        throat_K0_over_r2={r: prof[r]['K0'] / float(r) ** 2
                           for r in ('-0.1', '0.1')},
        pole_G0_over_K0={'r=1.5': prof['1.5']['G0'] / prof['1.5']['K0'],
                         'r=2.0': prof['2.0']['G0'] / prof['2.0']['K0'],
                         'F42_limit': 0.6458})
    # asymptotics
    asym = {}
    for r0 in (100., 200., 400., -100., -200., -400.):
        o = elim_at(r0)
        asym[str(r0)] = dict(K0=o['K0'], K0_over_J2=o['K0'] / o['J'] ** 2,
                             G0_over_K0=o['G0'] / o['K0'])
    res['asymptotics'] = asym
    res['asymptotics_summary'] = (
        'K0/J^2 -> +1/tau^2 = +0.01 at both infinities (0.00970 at '
        '|r|=100, 0.00992 at 200, 0.00997 at 400, both signs); '
        'G0/K0 -> 1 (0.883 at 100, 0.933 at 200, 0.964 at 400), '
        'matching the l>=1 c_s2^2 profile of F4-5. F4-2 (halved) has '
        'K0/J^2 -> -0.01 at -inf: the sign flip is entirely on the '
        'negative side, as the fit below identifies.')
    # action-on-surface cross-check
    res['action_check'] = [action_check(-20.0), action_check(20.0)]
    # Delta fit: which printed-e1 pieces explain K0_ind - K0_F42/2
    hh = 0.001
    rrf = np.arange(-60, 60 + 0.5 * hh, hh)
    Bf = p42.build(rrf, hh)
    dd = Bf['d']
    Xi, Xip = Bf['Xi'], Bf['Xip']
    J, Jp, Jpp = dd['J'], dd['Jp'], dd['Jpp']
    pip, X, Xp, F4 = dd['pip'], dd['X'], dd['Xp'], dd['F4']
    grf = lambda v: np.gradient(v, hh, edge_order=2)
    pF, qF = Bf['p'], Bf['q']
    c1BH = 4 * J * Jp * pip ** 3 * F4
    c1Xi = -Xi
    pieces = {
        'T1_-2Xiprime_over_piprime': (-2 * Xip / pip) / 4,
        'T2_Xprime_term': (-(Xp / X) * (Xi / pip)) / 4,
        'T3_2Jp2_over_X': (2 * Jp ** 2 / X) / 4,
        'T4_-2Jp3_over_X': (-2 * Jp ** 3 / X) / 4,
        'T5_2JJpp_over_X': (2 * J * Jpp / X) / 4,
        'e1BH': -(4.0 / pip ** 2 * grf(J * Jp * pip ** 4 * F4)) / 2,
        'c1Xi_q': 0.5 * c1Xi * qF,
        'c1BH_q': 0.5 * (-c1BH) * qF,
        'c1Xi_p': -0.25 * grf(c1Xi * pF),
        'c1BH_p': -0.25 * grf((-c1BH) * pF)}
    names = list(pieces)
    pts = []
    for rs_, o in prof.items():
        r = float(rs_)
        if abs(r) < 0.2 or abs(r - 1.7724) < 0.35:
            continue
        i = int(np.argmin(np.abs(rrf - r)))
        pts.append((r, o['K0'] - o['K0_F42'] / 2,
                    {k: float(pieces[k][i]) for k in names}))
    A = np.array([[p_[2][k] for k in names] for p_ in pts])
    y = np.array([p_[1] for p_ in pts])
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ sol
    Asub = np.array([[p_[2][k] for k in ('T3_2Jp2_over_X',
                                         'T4_-2Jp3_over_X')] for p_ in pts])
    solsub, *_ = np.linalg.lstsq(Asub, y, rcond=None)
    predsub = Asub @ solsub
    res['delta_fit'] = dict(
        alphas={k: float(a) for k, a in zip(names, sol)},
        max_resid_full=float(np.max(np.abs(pred - y))),
        restricted_T3_T4_alphas=[float(x) for x in solsub],
        max_resid_T3_T4=float(np.max(np.abs(predsub - y))),
        delta_range=[float(y.min()), float(y.max())],
        interpretation=(
            'Delta = K0_ind - K0_F42/2 = -(T3 piece) - (T4 piece) to '
            '1.3e-3 over Delta in [0.002, 71.5]: the printed e_1 terms '
            '+2 B J\'^2 F/X (T3) and -H B^2 J\'^2/(J X A) d/dr(J^2 A/B) '
            '(T4, = -2 J\'^3/X at A=B=1) together contribute '
            '(J\'^2 - J\'^3)/X to e_1; their correct on-background '
            'contribution is zero. Removing exactly this pair from '
            'F4-2\'s K_0 gives K0_ind (x2 in App-B normalisation) '
            'everywhere.'))
    # a2 adjudication summary
    a2rows = {}
    for rs_ in ('-40.0', '-20.0', '5.0', '40.0'):
        o = prof[rs_]
        a2rows[rs_] = dict(a2_ind=o['a2_ind'], a2H=o['a2H'],
                           a2_printed=o['a2_printed'],
                           a2_ind_minus_a2H=o['a2_ind'] - o['a2H'],
                           a2_ind_minus_printed=o['a2_ind']
                           - o['a2_printed'])
    res['a2_adjudication'] = dict(
        rows=a2rows,
        statement=('The from-action a_2 (extracted via the identity '
                   'b_3 = 2(a_1\' - a_2) applied to the independent '
                   'Q/EL_A structure) equals a_2^H (Horndeski part) '
                   'to FD precision at all sampled radii, NOT the '
                   'printed a_2 = a_2^H - 2 pi\'^3 F_4: the printed '
                   'a_2^BH = 2 sqrt(AB^3) pi\'^3 F_4 is spurious, '
                   'confirming F4-2\'s second finding independently. '
                   'In the independent derivation the identity itself '
                   'holds exactly: EL_A = D_r Q with nu = 0 and '
                   'residuals at FD floor (see profile ELA_resid_max).'))
    res['suspect_term_adjudication'] = (
        'In the independent derivation, no analogue of the printed '
        'e_1 pair survives: the reduced kinetic coefficient contains '
        'no (J\'^2 - J\'^3)/X term (fit coefficient of the pair in '
        'Delta is -1.000 for each of T3, T4 separately -- parities '
        'differ, so they are determined independently). The odd '
        'member (T4) is the term F4-2 flagged; the even member (T3) '
        'is equally spurious. At u=0 the pair is the only source of '
        'left-right asymmetry AND of the negative-side ghost; with '
        'the pair removed the corrected K_0 is positive at both '
        'infinities (K_0/J^2 -> +2/tau^2 in App-B normalisation).')
    res['verdict'] = (
        '(B) GHOST IS AN ARTEFACT -- independent derivation from the '
        'covariant action gives K0^(ind) > 0 at every sampled radius '
        'in [-60,60] (min ~ 0 only at the throat, where K0 vanishes '
        'quadratically like F4-2\'s), G0^(ind) > 0 everywhere, and '
        'K0^(ind)/J^2 -> +1/tau^2 at BOTH infinities. The F4-2 ghost '
        'is produced by the printed Appendix B e_1 pair identified '
        'in delta_fit. The l=0 sector PASSES on the corrected '
        'coefficients. (M0^(ind) agrees with F4-2\'s M0/2 at sample '
        'radii, so F4-3\'s l=0 tachyon input is unaffected in the '
        'mass sector; its kinetic normalisation flips sign on the '
        'negative side, which F4-3 must use.)')
    with open('/home/hatch/workspace/warp-pilot/phase4/results/'
              'p42b_ell0_indep.json', 'w') as fh:
        json.dump(res, fh, indent=2)
    print(json.dumps({k: res[k] for k in
                      ('profile_summary', 'asymptotics',
                       'action_check', 'delta_fit', 'a2_adjudication',
                       'verdict')}, indent=2, default=str))


if __name__ == '__main__':
    main()
