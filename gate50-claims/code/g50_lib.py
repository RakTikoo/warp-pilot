#!/usr/bin/env python3
"""
g50_lib.py -- Gate-50 machinery, written for this gate.

ORGANISATION (used by no earlier read): OPERATOR-BASED
SYMBOLIC DIFFERENTIATION of the Cartesian metric field
in the (r, n) algebra, evaluated in float64 for scans
and in 50-digit mpmath at named points. The metric
components are written as expressions in the symbols
(x, y, z, r, S, S', S'', N, N', N'', M, M', M'') and
their spatial derivatives are produced by a derivative
operator D_k = d/dx_k + n_k * D_r (with D_r the total
radial derivative through the profile symbols), applied
symbolically by sympy -- no symbolic metric is ever
inverted (the inverse is the gate's own block formula,
verified numerically), no expression is lambdified from
any phase or earlier gate (contrast Gate-46: sympy
symbolic in spherical coordinates; Gate-47: sympy
Cartesian with cse; Gate-48: forward-mode Taylor jets
in spherical coordinates; Gate-49: brute-force
Cartesian finite differences of the metric field from
stored profile values; Gate-45: AD jets in Cartesian;
Gate-43: Cartesian analytic loops; the lineage:
hand-derived radial formulas feeding a Cartesian
assembly). Profiles are assembled from the programme's
registered design definitions and stored vectors
(md5-verified artefacts in gate50/results/
g50_stored_inputs.json): closed-form base profiles
(the incomplete-beta plateau is the polynomial
I_u(3,3) = 10u^3(1-u)^2 + 5u^4(1-u) + u^5 -- no
special function is evaluated anywhere) and not-a-knot
correction splines whose moment systems are solved by
this file's own solver (cross-checked against scipy's
CubicSpline in the calibration record; scipy is not
imported by the deciding path). The Eulerian frame and
the Hawking-Ellis margins are re-implemented from
their definitions; the pointwise worst null is an
exact secular-equation (trust-region) solve,
cross-checked against a dense scan + polish. No phase
or earlier-gate code is imported. VM is the frame of
record; the laptop admission control is run and
followed (g50_admission.py).
"""
import json
import os

import numpy as np

DT = np.float64
BETA = 1.1
R_LO, R_HI = 10.0, 20.0
LAM_S = 0.70
WINNER_A = 0.07439108177516472
MU_H2 = 1.15
EIGHT_PI = 8.0 * np.pi

WP = os.environ.get('G50_WP', '/home/hatch/workspace/warp-pilot')
INP = json.load(open(f'{WP}/gate50/results/g50_stored_inputs.json'))

A2 = {k: np.array(INP['A2'][k], dtype=DT) for k in ('vS', 'vN', 'vM')}
H2V = {k: np.array(INP['H2'][k], dtype=DT) for k in ('vS', 'vN', 'vM')}
WIN = INP['winner400']
WIN_MUN = float(WIN['muN'])
WIN_MUM = float(WIN['muM'])
WIN_VN = np.array(WIN['vN'], dtype=DT)
WIN_VM = np.array(WIN['vM'], dtype=DT)
SHAPEC_CRIT = np.array(INP['conf405']['shapeC_knots_at_criterion'],
                       dtype=DT)
SHAPEB_CRIT = np.array(INP['shapeB_criterion_vS'], dtype=DT)
CRIT_PEAK = 0.44267424902674035          # stored phys-row peak
SS7_BAR = 0.4426742490267404             # 0.5 * H2 peak (registered)


def knots(K):
    return np.linspace(R_LO, R_HI, K)


# ============================================================ splines
# Not-a-knot cubic spline in moment form. The moment
# system (second derivatives at the knots) is assembled
# and solved here; scipy is never used on this path.
def nak_moments(xk, yk):
    xk = np.asarray(xk, dtype=DT)
    yk = np.asarray(yk, dtype=DT)
    n = len(xk)
    h = np.diff(xk)
    A = np.zeros((n, n), dtype=DT)
    b = np.zeros(n, dtype=DT)
    # not-a-knot at x_1: (M1-M0)/h0 = (M2-M1)/h1
    A[0, 0] = -h[1]
    A[0, 1] = h[0] + h[1]
    A[0, 2] = -h[0]
    # interior
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2.0 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 6.0 * ((yk[i + 1] - yk[i]) / h[i]
                      - (yk[i] - yk[i - 1]) / h[i - 1])
    # not-a-knot at x_{n-2}
    A[n - 1, n - 3] = -h[n - 2]
    A[n - 1, n - 2] = h[n - 3] + h[n - 2]
    A[n - 1, n - 1] = -h[n - 3]
    return np.linalg.solve(A, b)


def nak_eval(xk, yk, M, r):
    """(d, dp, dpp) of the spline at radii r (array);
    constant extension (end value, zero derivatives)
    outside [xk[0], xk[-1]] -- the lineage's registered
    correction-spline convention."""
    xk = np.asarray(xk, dtype=DT)
    yk = np.asarray(yk, dtype=DT)
    r = np.asarray(r, dtype=DT)
    rc = np.clip(r, xk[0], xk[-1])
    i = np.searchsorted(xk, rc, side='right') - 1
    i = np.clip(i, 0, len(xk) - 2)
    h = xk[i + 1] - xk[i]
    A_ = (xk[i + 1] - rc) / h
    B_ = (rc - xk[i]) / h
    d = (A_ * yk[i] + B_ * yk[i + 1]
         + ((A_ ** 3 - A_) * M[i] + (B_ ** 3 - B_) * M[i + 1])
         * h ** 2 / 6.0)
    dp = ((yk[i + 1] - yk[i]) / h
          + h / 6.0 * ((1.0 - 3.0 * A_ ** 2) * M[i]
                       + (3.0 * B_ ** 2 - 1.0) * M[i + 1]))
    dpp = A_ * M[i] + B_ * M[i + 1]
    out = (r < xk[0]) | (r > xk[-1])
    if np.any(out):
        dp = np.where(out, 0.0, dp)
        dpp = np.where(out, 0.0, dpp)
    return d, dp, dpp


class Corr:
    """A correction spline (values + cached moments)."""

    def __init__(self, vals, K):
        self.xk = knots(K)
        self.yk = np.asarray(vals, dtype=DT)
        self.M = nak_moments(self.xk, self.yk)

    def __call__(self, r):
        return nak_eval(self.xk, self.yk, self.M, r)


_CORR_CACHE = {}


def corr(vals, K):
    key = (K, tuple(np.asarray(vals, dtype=DT)))
    if key not in _CORR_CACHE:
        _CORR_CACHE[key] = Corr(vals, K)
    return _CORR_CACHE[key]


# ============================================================ base profiles
# All closed forms are polynomials / piecewise
# polynomials; each returns (f, f', f'') at radii r.
def s_ab(r):
    """1 below 10, 0 above 20, 1 - I_u(3,3) between,
    u = (r-10)/10; I_u(3,3) = 10u^3(1-u)^2 + 5u^4(1-u)
    + u^5 (the regularised incomplete beta at integer
    parameters, a polynomial)."""
    r = np.asarray(r, dtype=DT)
    S = np.where(r >= R_HI, 0.0, 1.0)
    Sp = np.zeros_like(r)
    Spp = np.zeros_like(r)
    m = (r > R_LO) & (r < R_HI)
    if np.any(m):
        u = (r[m] - R_LO) / 10.0
        w = 1.0 - u
        S[m] = 1.0 - (10.0 * u ** 3 * w ** 2 + 5.0 * u ** 4 * w
                      + u ** 5)
        Sp[m] = -3.0 * u ** 2 * w ** 2
        Spp[m] = -0.6 * u * w * (1.0 - 2.0 * u)
    return S, Sp, Spp


def _H(t):
    """Smootherstep and derivatives: 0 below 0, 1 above
    1, 10t^3 - 15t^4 + 6t^5 between."""
    t = np.asarray(t, dtype=DT)
    v = np.where(t >= 1.0, 1.0, 0.0)
    vp = np.zeros_like(t)
    vpp = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    if np.any(m):
        tm = t[m]
        v[m] = 10.0 * tm ** 3 - 15.0 * tm ** 4 + 6.0 * tm ** 5
        vp[m] = 30.0 * tm ** 2 * (1.0 - tm) ** 2
        vpp[m] = 60.0 * tm * (1.0 - tm) * (1.0 - 2.0 * tm)
    return v, vp, vpp


def _plateau(r, c=15.0, W=5.0, e=3.0):
    Ha, Hpa, Hppa = _H((r - (c - W)) / e)
    Hb, Hpb, Hppb = _H(((c + W) - r) / e)
    B = Ha * Hb
    Bp = (Hpa * Hb - Ha * Hpb) / e
    Bpp = (Hppa * Hb - 2.0 * Hpa * Hpb + Ha * Hppb) / e ** 2
    return B, Bp, Bpp


def _ramp(r, a, b):
    """Quintic smoothstep ramp U(r; a, b) and
    derivatives."""
    r = np.asarray(r, dtype=DT)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r)
    Upp = np.zeros_like(r)
    m = (r > a) & (r < b)
    if np.any(m):
        x = (r[m] - a) / (b - a)
        U[m] = 6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3
        Up[m] = (30.0 * x ** 4 - 60.0 * x ** 3
                 + 30.0 * x ** 2) / (b - a)
        Upp[m] = (120.0 * x ** 3 - 180.0 * x ** 2
                  + 60.0 * x) / (b - a) ** 2
    return U, Up, Upp


def base_profiles(r):
    r = np.asarray(r, dtype=DT)
    S, Sp, Spp = s_ab(r)
    S, Sp, Spp = LAM_S * S, LAM_S * Sp, LAM_S * Spp
    B, Bp, Bpp = _plateau(r)
    N, Np, Npp = (1.0 + WINNER_A * B, WINNER_A * Bp,
                  WINNER_A * Bpp)
    U1, U1p, U1pp = _ramp(r, 8.5, 20.0)
    U2, U2p, U2pp = _ramp(r, 21.0, 24.0)
    M = 1.0 + 6.0 * (U1 - U2)
    Mp = 6.0 * (U1p - U2p)
    Mpp = 6.0 * (U1pp - U2pp)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


def _add_corr_arr(prof, vecs, K, r):
    out = []
    for i, key in enumerate(('vS', 'vN', 'vM')):
        d, dp, dpp = corr(vecs[key], K)(r)
        out += [prof[3 * i] + d, prof[3 * i + 1] + dp,
                prof[3 * i + 2] + dpp]
    return tuple(out)


def a2_totals(r):
    return _add_corr_arr(base_profiles(r), A2, 33, r)


def _centre(mu, prof):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)


def h2_totals(r):
    return _add_corr_arr(_centre(MU_H2, a2_totals(r)), H2V, 17, r)


# ------------------------------------------------ profile assemblies
# Each returns (S, Sp, Spp, N, Np, Npp, M, Mp, Mpp) at
# radii r (numpy arrays).
def prof_winner_base(r):
    """Phase 400's winner: H2 totals' N/M rescaled by
    (WIN_MUN, WIN_MUM) + the winner's K=17 corrections;
    S identically zero."""
    _S, _Sp, _Spp, N, Np, Npp, M, Mp, Mpp = h2_totals(r)
    r = np.asarray(r, dtype=DT)
    z = np.zeros_like(r)
    N, Np, Npp = WIN_MUN * N, WIN_MUN * Np, WIN_MUN * Npp
    M, Mp, Mpp = (1.0 + WIN_MUM * (M - 1.0), WIN_MUM * Mp,
                  WIN_MUM * Mpp)
    d, dp, dpp = corr(WIN_VN, 17)(r)
    N, Np, Npp = N + d, Np + dp, Npp + dpp
    d, dp, dpp = corr(WIN_VM, 17)(r)
    M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    return z.copy(), z.copy(), z.copy(), N, Np, Npp, M, Mp, Mpp


def _with_S(base, Sprof):
    return (Sprof[0], Sprof[1], Sprof[2],
            base[3], base[4], base[5],
            base[6], base[7], base[8])


def prof_winner405(r):
    """The Phase 405 winner: winner base + the K=9
    shape spline at its criterion knot vector."""
    r = np.asarray(r, dtype=DT)
    return _with_S(prof_winner_base(r), corr(SHAPEC_CRIT, 9)(r))


def prof_shapeB(r):
    """Stage B's shape at its criterion knot vector on
    the winner base."""
    r = np.asarray(r, dtype=DT)
    return _with_S(prof_winner_base(r), corr(SHAPEB_CRIT, 9)(r))


def prof_winner_at_peak(P):
    """The winner's shape scaled to peak |beta*S| = P
    (S is exactly linear in the knot vector)."""
    fac = float(P) / CRIT_PEAK
    vec = SHAPEC_CRIT * fac

    def f(r):
        r = np.asarray(r, dtype=DT)
        return _with_S(prof_winner_base(r), corr(vec, 9)(r))
    return f


def prof_fixed(muS):
    """Phase 404's fixed shape: S = muS * S_H2 (H2
    totals' S sector) on the winner base."""

    def f(r):
        r = np.asarray(r, dtype=DT)
        h2 = h2_totals(r)
        return _with_S(prof_winner_base(r),
                       (muS * h2[0], muS * h2[1], muS * h2[2]))
    return f


def prof_h2_scaled(muS):
    """H2 totals with the S sector scaled by muS."""

    def f(r):
        r = np.asarray(r, dtype=DT)
        h2 = h2_totals(r)
        return (muS * h2[0], muS * h2[1], muS * h2[2],
                h2[3], h2[4], h2[5], h2[6], h2[7], h2[8])
    return f


# ============================================================ tensor layer
# Metric field (the programme's ansatz, as a definition):
#   g_tt = -N(r)^2,  g_tx = g_xt = -beta*S(r),
#   g_ij = delta_ij + (M(r)-1) n_i n_j,  n = x/r.
# Spatial derivatives are produced by the operator
#   D_k = d/dx_k + n_k * D_r,
#   D_r = d/dr + S' d/dS + N' d/dN + M' d/dM
#              + S'' d/dS' + N'' d/dN' + M'' d/dM'
# applied symbolically (sympy) to the components
# written in the symbols (x, y, z, r, S, Sp, Spp, N,
# Np, Npp, M, Mp, Mpp). The Einstein tensor is then
# assembled by this file's own index contractions.
_TENSOR = {}


def _build_tensor():
    if _TENSOR:
        return _TENSOR
    import sympy as sp
    x, y, z, r = sp.symbols('x y z r')
    SS, Sp, Spp, NN, Np, Npp, MM, Mp, Mpp = sp.symbols(
        'SS Sp Spp NN Np Npp MM Mp Mpp')
    coords = [x, y, z]
    pairs = [(SS, Sp), (NN, Np), (MM, Mp),
             (Sp, Spp), (Np, Npp), (Mp, Mpp)]

    def D(e, k):
        ck = coords[k]
        out = sp.diff(e, ck) + (ck / r) * sp.diff(e, r)
        for a, b in pairs:
            out = out + (ck / r) * sp.diff(e, a) * b
        return out

    beta = sp.Rational(11, 10)
    g = sp.zeros(4, 4)
    g[0, 0] = -NN ** 2
    g[0, 1] = g[1, 0] = -beta * SS
    for i in range(3):
        for j in range(3):
            g[i + 1, j + 1] = ((1 if i == j else 0)
                               + (MM - 1) * coords[i] * coords[j]
                               / r ** 2)
    args = [x, y, z, r, SS, Sp, Spp, NN, Np, Npp, MM, Mp, Mpp]
    exprs = {'g': {}, 'dg': {}, 'ddg': {}}
    gf = {}
    for mu in range(4):
        for nu in range(mu, 4):
            exprs['g'][(mu, nu)] = g[mu, nu]
            gf[(mu, nu)] = sp.lambdify(args, g[mu, nu], 'numpy')
    dgf = {}
    ddgf = {}
    dg = {}
    for k in range(3):
        for mu in range(4):
            for nu in range(mu, 4):
                dg[(k, mu, nu)] = D(g[mu, nu], k)
                exprs['dg'][(k, mu, nu)] = dg[(k, mu, nu)]
                dgf[(k, mu, nu)] = sp.lambdify(
                    args, dg[(k, mu, nu)], 'numpy')
    for k in range(3):
        for l in range(3):
            for mu in range(4):
                for nu in range(mu, 4):
                    e2 = D(dg[(k, mu, nu)], l)
                    exprs['ddg'][(k, l, mu, nu)] = e2
                    ddgf[(k, l, mu, nu)] = sp.lambdify(
                        args, e2, 'numpy')
    _TENSOR.update(gf=gf, dgf=dgf, ddgf=ddgf, args=args,
                   exprs=exprs)
    return _TENSOR


def tensor_funcs_mp():
    """The same derived component expressions lambdified
    for mpmath (scalar evaluation at named points)."""
    if 'mp' not in _TENSOR:
        import sympy as sp
        T = _build_tensor()
        args = T['args']
        mp = {'g': {}, 'dg': {}, 'ddg': {}}
        for kind in ('g', 'dg', 'ddg'):
            for key, e in T['exprs'][kind].items():
                mp[kind][key] = sp.lambdify(args, e, 'mpmath')
        _TENSOR['mp'] = mp
    return _TENSOR['mp']


def _eval_sym(fun, pts, prof):
    """Evaluate a lambdified component over points.
    prof: the 9-tuple of profile arrays at the points'
    radii."""
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    r = np.linalg.norm(pts, axis=1)
    return np.broadcast_to(
        np.asarray(fun(x, y, z, r, *prof), dtype=DT), (len(pts),))


def metric_and_derivs(pts, prof):
    """(g, DG, DDG): g (P,4,4); DG (P,4,4,4) with
    DG[:,e,mu,nu] = d_e g_mu,nu (time row zero);
    DDG (P,4,4,4,4) likewise (any time index zero)."""
    T = _build_tensor()
    P = len(pts)
    g = np.zeros((P, 4, 4))
    DG = np.zeros((P, 4, 4, 4))
    DDG = np.zeros((P, 4, 4, 4, 4))
    for (mu, nu), f in T['gf'].items():
        v = _eval_sym(f, pts, prof)
        g[:, mu, nu] = v
        g[:, nu, mu] = v
    for (k, mu, nu), f in T['dgf'].items():
        v = _eval_sym(f, pts, prof)
        DG[:, k + 1, mu, nu] = v
        DG[:, k + 1, nu, mu] = v
    for (k, l, mu, nu), f in T['ddgf'].items():
        v = _eval_sym(f, pts, prof)
        DDG[:, k + 1, l + 1, mu, nu] = v
        DDG[:, k + 1, l + 1, nu, mu] = v
    return g, DG, DDG


def metric_ginv(g, pts, prof):
    """The gate's block-form inverse of the ansatz
    metric (verified against np.linalg.inv in the
    calibration record):
      gamma^-1 = I - q n n^T,  q = (M-1)/M;
      w = g_t. = (-beta*S, 0, 0);
      alpha^2 = N^2 + w^T gamma^-1 w;
      g^tt = -1/alpha^2,  g^ti = (gamma^-1 w)^i/alpha^2,
      g^ij = gamma^-1_ij - (gamma^-1 w)^i (gamma^-1 w)^j
             / alpha^2."""
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    S, _Sp, _Spp, N, _Np, _Npp, M, _Mp, _Mpp = prof
    q = (M - 1.0) / M
    C = n[:, 0]
    v = BETA * S
    ginv_w = np.zeros((P, 3))
    # (gamma^-1 w)^i = -v (delta_ix - q n_i C)
    ginv_w[:, 0] = -v * (1.0 - q * C * C)
    ginv_w[:, 1] = -v * (-q * n[:, 1] * C)
    ginv_w[:, 2] = -v * (-q * n[:, 2] * C)
    wgw = v * v * (1.0 - q * C * C)
    alpha2 = N ** 2 + wgw
    ginv = np.zeros((P, 4, 4))
    ginv[:, 0, 0] = -1.0 / alpha2
    ginv[:, 0, 1:] = ginv_w / alpha2[:, None]
    ginv[:, 1:, 0] = ginv_w / alpha2[:, None]
    gam_inv = (np.eye(3)[None, :, :]
               - q[:, None, None] * n[:, :, None] * n[:, None, :])
    ginv[:, 1:, 1:] = (gam_inv
                       - (ginv_w[:, :, None] * ginv_w[:, None, :])
                       / alpha2[:, None, None])
    return ginv


def einstein_from_derivs(g, ginv, DG, DDG):
    """G_ab from the metric, its inverse, and its
    first/second spatial derivatives (stationary:
    time derivatives vanish). Textbook index
    contractions, this file's own loops:
      Gam^a_bc = 1/2 g^ad (d_b g_dc + d_c g_db - d_d g_bc)
      Ric_bd = sum_a [d_a Gam^a_bd - d_d Gam^a_ba]
             + sum_ae [Gam^a_ae Gam^e_bd - Gam^a_de Gam^e_ba]
    """
    P = len(g)
    Gam = np.zeros((P, 4, 4, 4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = (DG[:, b, :, c] + DG[:, c, :, b]
                        - DG[:, :, b, c])
                Gam[:, a, b, c] = 0.5 * np.einsum(
                    'pd,pd->p', ginv[:, a, :], term)
    dGinv = np.zeros((P, 4, 4, 4))
    for e in range(4):
        dGinv[:, e] = -np.einsum('pam,pmn,pnb->pab',
                                 ginv, DG[:, e], ginv)
    dGam = np.zeros((P, 4, 4, 4, 4))
    for e in range(4):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = (DG[:, b, :, c] + DG[:, c, :, b]
                          - DG[:, :, b, c])
                    dt = (DDG[:, e, b, :, c] + DDG[:, e, c, :, b]
                          - DDG[:, e, :, b, c])
                    dGam[:, e, a, b, c] = (
                        0.5 * np.einsum('pd,pd->p',
                                        dGinv[:, e, a, :], t1)
                        + 0.5 * np.einsum('pd,pd->p',
                                          ginv[:, a, :], dt))
    Ric = np.zeros((P, 4, 4))
    for b in range(4):
        for d in range(4):
            val = np.zeros(P)
            for a in range(4):
                val += dGam[:, a, a, b, d] - dGam[:, d, a, b, a]
            for a in range(4):
                for e in range(4):
                    val += (Gam[:, a, a, e] * Gam[:, e, b, d]
                            - Gam[:, a, d, e] * Gam[:, e, b, a])
            Ric[:, b, d] = val
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g
    return G


def T_at(pts, prof_fn):
    """(T, g) at Cartesian points for a profile
    assembly prof_fn(radii) -> 9-tuple."""
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    prof = prof_fn(r)
    g, DG, DDG = metric_and_derivs(pts, prof)
    ginv = metric_ginv(g, pts, prof)
    G = einstein_from_derivs(g, ginv, DG, DDG)
    return G / EIGHT_PI, g


# ============================================================ frame layer
def eulerian_that(g, Tcov):
    """Covariant T -> the Eulerian orthonormal frame
    of the ADM decomposition of g (definition:
    gamma = g[1:,1:], beta_cov = g[0,1:], alpha^2 =
    -g_tt + beta.gamma^-1.beta; e_0 = (1/alpha,
    -beta^i/alpha); spatial triad = eigenvectors of
    gamma scaled by 1/sqrt(eigenvalue))."""
    g = np.asarray(g, dtype=DT)
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...',
                                       beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DT)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = (V[..., :, i]
                             / np.sqrt(lam[..., i])[..., None])
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def fib_dirs(npts):
    """The sampler's Fibonacci directions (definition:
    phi = arccos(1 - 2(i+1/2)/n), theta = pi(1+sqrt5)i).
    """
    i = np.arange(npts, dtype=DT)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


def _he_eigen_margins(That):
    """Hawking-Ellis eigenvalue margins (definitions:
    mixed tensor M^a_b = eta^{aa} That_ab; Type I iff
    all eigenvalues real (imag < 1e-8 * scale) and
    exactly one eigenvector timelike (eta-norm of
    |components|^2 < -1e-6); rho = -(timelike
    eigenvalue), p_i the other three;
    NEC = min(rho + p_i), WEC = min(rho, NEC),
    SEC = min(NEC, rho + sum p_i),
    DEC = min(rho, rho - max|p_i|)).
    Returns dict with NaN margins at non-Type-I
    points."""
    That = np.asarray(That, dtype=DT)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np_ = flat.shape[0]
    M = flat.copy()
    M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k_idx = np.argmax(cand, axis=1)
    ar = np.arange(Np_)
    rho = np.where(typeI, -evals[ar, k_idx].real, np.nan)
    mask = np.ones((Np_, 4), dtype=bool)
    mask[ar, k_idx] = False
    ps_all = evals.real[mask].reshape(Np_, 3)
    ps = np.where(typeI[:, None], ps_all, np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1),
                       np.nan)
        wec = np.where(typeI, np.minimum(
            rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(
            np.min(rho[:, None] + ps, axis=1),
            rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(
            rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    return {'typeI': typeI.reshape(shp),
            'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
            'sec': sec.reshape(shp), 'dec': dec.reshape(shp),
            'rho_eig': rho.reshape(shp)}


def sampled_margins(That, n_dir=162, n_vel=6):
    """The sampled fallback at non-Type-I points
    (definitions: NEC from the v->1 contraction over
    fib(n_dir) directions; WEC/SEC minimised over
    velocities linspace(0, 0.95, n_vel) x directions;
    DEC from the future-causality margin of
    Upsilon^a = -T^a_b V^b, normalised by
    1 + |Upsilon|^2)."""
    dirs = fib_dirs(n_dir)
    That = np.asarray(That, dtype=DT)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np_ = flat.shape[0]
    nec_min = np.empty(Np_)
    wec_min = np.empty(Np_)
    sec_min = np.empty(Np_)
    dec_min = np.empty(Np_)
    vels = np.linspace(0.0, 0.95, n_vel)
    CH = 8192
    for s0 in range(0, Np_, CH):
        F = flat[s0:s0 + CH]
        T00 = F[:, 0, 0]
        T0i = F[:, 0, 1:]
        Tij = F[:, 1:, 1:]
        tr = np.trace(Tij, axis1=1, axis2=2)
        quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
        nec_min[s0:s0 + CH] = (T00[:, None]
                               + 2.0 * (T0i @ dirs.T)
                               + quad).min(axis=1)
        wm = np.full(F.shape[0], np.inf)
        sm = np.full(F.shape[0], np.inf)
        dm = np.full(F.shape[0], np.inf)
        Mm = F.copy()
        Mm[:, 0, :] *= -1.0
        for v in vels:
            gam = 1.0 / np.sqrt(1.0 - v * v)
            wec_vals = gam ** 2 * (T00[:, None]
                                   + 2.0 * v * (T0i @ dirs.T)
                                   + v * v * quad)
            wm = np.minimum(wm, wec_vals.min(axis=1))
            trT = -T00 + tr
            sec_vals = wec_vals - 0.5 * trT[:, None] * gam ** 2 \
                * (v * v - 1.0)
            sm = np.minimum(sm, sec_vals.min(axis=1))
            V = np.zeros((F.shape[0], n_dir, 4), dtype=DT)
            V[:, :, 0] = gam
            V[:, :, 1:] = gam * v * dirs[None, :, :]
            Ups = -np.einsum('nab,nib->nia', Mm, V)
            q = Ups[:, :, 0] ** 2 - np.sum(Ups[:, :, 1:] ** 2,
                                           axis=2)
            nrm = 1.0 + np.sum(Ups ** 2, axis=2)
            val = np.where(Ups[:, :, 0] > 0, q / nrm,
                           -np.abs(q) / nrm - 1.0)
            dm = np.minimum(dm, val.min(axis=1))
        wec_min[s0:s0 + CH] = wm
        sec_min[s0:s0 + CH] = sm
        dec_min[s0:s0 + CH] = dm
    return {'nec_s': nec_min.reshape(shp),
            'wec_s': wec_min.reshape(shp),
            'sec_s': sec_min.reshape(shp),
            'dec_s': dec_min.reshape(shp)}


def margins(That):
    """Eigenvalue margins at Type-I points; the
    sampled fallback at the rest (the lineage's
    margins_chunked form, re-implemented)."""
    m = _he_eigen_margins(That)
    shp = m['typeI'].shape
    bad = np.where(~m['typeI'].reshape(-1))[0]
    filled = np.zeros(len(m['typeI'].reshape(-1)), dtype=bool)
    if bad.size:
        flat = np.asarray(That, dtype=DT).reshape(-1, 4, 4)
        sub = sampled_margins(flat[bad])
        for key, skey in (('nec', 'nec_s'), ('wec', 'wec_s'),
                          ('sec', 'sec_s'), ('dec', 'dec_s')):
            arr = m[key].reshape(-1)
            arr[bad] = sub[skey]
            m[key] = arr.reshape(shp)
        filled[bad] = True
    m['sampled_filled'] = filled.reshape(shp)
    return m


def worst_null_exact(That):
    """Exact pointwise worst null: min over unit m of
    rho + 2 F.m + m^T P m for That = [[rho, F^T],
    [F, P]], by the secular equation. Returns
    (q_full, m_best, lambda_star): the minimiser is
    certified by the trust-region KKT conditions
    (P + lambda I) m = -F, |m| = 1, lambda >=
    -lambda_min(P). Frame-invariant."""
    That = np.asarray(That, dtype=DT)
    rho = float(That[0, 0])
    F = That[0, 1:].astype(DT)
    P = That[1:, 1:].astype(DT)
    lam, Q = np.linalg.eigh(P)
    Fh = Q.T @ F

    def m_of(lmbda):
        return -(Q @ (Fh / (lam + lmbda)))

    def gsec(lmbda):
        return float(np.sum((Fh / (lam + lmbda)) ** 2))

    lam_min = float(lam[0])
    scale = max(1.0, abs(lam_min))
    d0 = 1e-9 * scale
    if gsec(-lam_min + d0) <= 1.0:
        # Hard case: F has no usable component in the
        # lam_min eigenspace; lambda* = -lam_min and
        # the minimiser fills that eigenspace to unit
        # norm (masked solve on the other components).
        lstar = -lam_min
        denom = lam + lstar
        mask = denom > 1e-12 * scale
        mh = np.zeros(3)
        mh[mask] = -Fh[mask] / denom[mask]
        m = Q @ mh
        rem = max(0.0, 1.0 - float(m @ m))
        m = m + np.sqrt(rem) * Q[:, 0]
        q = rho + 2.0 * float(F @ m) + float(m @ P @ m)
        return q, m, lstar
    lo = -lam_min + d0
    hi = lo + 1.0
    while gsec(hi) > 1.0:
        hi = lo + 2.0 * (hi - lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if gsec(mid) > 1.0:
            lo = mid
        else:
            hi = mid
    lstar = 0.5 * (lo + hi)
    m = m_of(lstar)
    q = rho + 2.0 * float(F @ m) + float(m @ P @ m)
    return q, m, lstar


def worst_null_scan(That, n_dir=642):
    """fib(n_dir) scan minimum of k^T That k, k = (1, m)
    (the stored worst_null_fib form)."""
    dirs = fib_dirs(n_dir)
    T00 = That[0, 0]
    T0i = That[0, 1:]
    Tij = That[1:, 1:]
    vals = (T00 + 2.0 * (dirs @ T0i)
            + np.einsum('ni,ij,nj->n', dirs, Tij, dirs))
    return float(np.min(vals))


# ============================================================ reads
R_NODES = R_LO + (np.arange(41, dtype=DT) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
FINE_R = np.linspace(R_LO, R_HI, 401)


def set_read(prof_fn):
    """SET-244 read (41 radial midpoint nodes x 162
    Fibonacci dirs), this gate's machinery. Returns
    (summary, aux). Sampled minima are SAMPLER-M
    quantities (the lineage's eulerian_that
    association); deciding values are the
    frame-invariant ones (worst-null, polish,
    Type-I statistics)."""
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec',
                           'rho')}
    typeI_pts, typeI_nec = [], []
    for rr in R_NODES:
        pts = DIRS162 * rr
        T, g = T_at(pts, prof_fn)
        That = eulerian_that(g, T)
        m = margins(That)
        rec['typeI'].append(m['typeI'])
        rec['nec'].append(m['nec'])
        rec['wec'].append(m['wec'])
        rec['dec'].append(m['dec'])
        rec['sec'].append(m['sec'])
        rec['rho'].append(That[:, 0, 0])
        if np.any(m['typeI']):
            typeI_pts.append(pts[m['typeI']])
            typeI_nec.append(m['nec'][m['typeI']])
    R = {k: np.concatenate(v) for k, v in rec.items()}

    def st(arr):
        return {'min': float(np.min(arr)),
                'median': float(np.median(arr)),
                'max': float(np.max(arr))}
    i_nec = int(np.argmin(R['nec']))
    i_dec = int(np.argmin(R['dec']))
    i_r, i_d = divmod(i_nec, 162)
    j_r, j_d = divmod(i_dec, 162)
    out = {
        'set': 'SET-244 (41 radial midpoint nodes x 162 '
               'Fibonacci dirs)',
        'sampler': 'SAMPLER-M',
        'n_points': int(len(R['typeI'])),
        'typeI_fraction': float(np.mean(R['typeI'])),
        'typeI_count': int(np.sum(R['typeI'])),
        'nec': st(R['nec']), 'wec': st(R['wec']),
        'dec': st(R['dec']), 'sec': st(R['sec']),
        'rho': st(R['rho']),
        'nec_argmin_point': (DIRS162[i_d] * R_NODES[i_r]).tolist(),
        'nec_argmin_r': float(R_NODES[i_r]),
        'nec_argmin_typeI': bool(R['typeI'][i_nec]),
        'dec_argmin_point': (DIRS162[j_d] * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
        'typeI_nec_min': (float(np.min(np.concatenate(typeI_nec)))
                          if typeI_nec else None),
        'typeI_dec_min': None,
    }
    # Type-I-only DEC minimum (frame-invariant
    # companion for configs with non-Type-I points).
    dec_ti = np.where(R['typeI'], R['dec'], np.inf)
    out['typeI_dec_min'] = float(np.min(dec_ti))
    aux = {'R': R,
           'typeI_pts': (np.vstack(typeI_pts) if typeI_pts
                         else np.zeros((0, 3))),
           'typeI_nec': (np.concatenate(typeI_nec) if typeI_nec
                         else np.zeros(0))}
    return out, aux


def joint_of(summary):
    return min(summary['nec']['min'], summary['dec']['min'])


def nec_at(prof_fn, pt):
    pt = np.asarray(pt, dtype=DT)
    T, g = T_at(pt[None, :], prof_fn)
    That = eulerian_that(g, T)
    m = margins(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def adversary_polish(prof_fn, aux):
    """In-region Type-I NEC minimisation from the five
    lowest Type-I SET points (Nelder-Mead over
    (r, theta, phi); objective = NEC at Type-I points,
    NEC + 1 elsewhere / outside [10, 20])."""
    from scipy.optimize import minimize
    pts_ti = aux['typeI_pts']
    nec_ti = aux['typeI_nec']
    if len(pts_ti) == 0:
        return None
    rr_ti = np.linalg.norm(pts_ti, axis=1)

    def objective(x):
        rr, th, ph = x
        if rr < 10.0 or rr > 20.0:
            return 1.0
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = nec_at(prof_fn, pt)
        return nec if is_ti else nec + 1.0

    order = np.argsort(nec_ti)[:5]
    starts = [{'set_point': pts_ti[i].tolist(),
               'set_r': float(rr_ti[i]),
               'set_nec': float(nec_ti[i])} for i in order]
    polished = []
    for i in order:
        p0 = pts_ti[i]
        r0 = float(np.linalg.norm(p0))
        x0 = np.array([r0, np.arccos(np.clip(p0[2] / r0, -1, 1)),
                       np.arctan2(p0[1], p0[0])])
        res = minimize(objective, x0, method='Nelder-Mead',
                       options={'maxiter': 300, 'xatol': 1e-4,
                                'fatol': 1e-7})
        rr, th, ph = res.x
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = nec_at(prof_fn, pt)
        polished.append({'start_set_nec': float(nec_ti[i]),
                         'polished_point': pt.tolist(),
                         'polished_r': float(rr),
                         'polished_objective': float(res.fun),
                         'polished_nec_SAMPLER-M': nec,
                         'polished_typeI': is_ti})
    cand = [p for p in polished if p['polished_typeI']]
    if cand:
        best_p = min(cand, key=lambda p: p['polished_nec_SAMPLER-M'])
        site_pt = np.array(best_p['polished_point'], dtype=DT)
        source = 'polished'
    else:
        i0 = int(order[0])
        site_pt = pts_ti[i0]
        best_p = None
        source = 'set_argmin_fallback'
    nec_site, is_ti_site, That_site = nec_at(prof_fn, site_pt)
    return {'source': source,
            'point': site_pt.tolist(),
            'r': float(np.linalg.norm(site_pt)),
            'typeI': bool(is_ti_site),
            'in_region_worst_nec_SAMPLER-M': nec_site,
            'rho_t': float(That_site[0, 0]),
            'polish_starts': starts, 'polished': polished,
            'best_polished': best_p}


def peak_read(prof_fn, radii=None):
    """Peak |beta*S| on the x-axis over `radii`
    (default FINE_R, the phys-row form)."""
    if radii is None:
        radii = FINE_R
    radii = np.asarray(radii, dtype=DT)
    S = prof_fn(radii)[0]
    a = np.abs(BETA * S)
    i = int(np.argmax(a))
    return {'peak_abs_beta_S': float(a[i]),
            'peak_abs_S': float(abs(S[i])),
            'peak_radius': float(radii[i]),
            'S': S, 'radii': radii}
