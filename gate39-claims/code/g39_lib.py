#!/usr/bin/env python3
"""
g39_lib.py -- Gate-39 INDEPENDENT machinery. Written fresh for this gate.
No imports from any phase library or verify_metric. Only numpy/scipy.

Metric (coords t,x,y,z; signature -,+,+,+; G=c=1):
  g_tt = -N(r,t)^2
  g_tX = g_Xt = -beta * S(r,t)        (X = x direction, beta = 1.1)
  gamma_ij = delta_ij + (M(r,t)-1) n_i n_j,  n = x_vec / r

Einstein tensor: assembled from the metric's first/second derivative
tensors dg[e,mu,nu], ddg[e,f,mu,nu] (e,f over t,x,y,z) through the
standard Christoffel -> Ricci algebra, vectorised with einsum.
Scalar profile derivatives enter through the chain rule:
  d_i F = F_r n_i ;  d_i d_j F = F_rr n_i n_j + (F_r/r)(delta_ij-n_i n_j)
  d_t F = F_t ; d_t d_i F = F_rt n_i ; d_t d_t F = F_tt.
Spatial derivatives of gamma use the exact differentiation of
H n_i n_j (H = M-1) with d_k n_i = (delta_ki - n_k n_i)/r.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
from scipy.special import betainc, beta as beta_fn

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi
BETA = 1.1
BAR_DEPTH = -0.0034

WINNER_SPEC = {'shape': 'plat', 'a': 2, 'b': 2,
               'A': 0.07439108177516472, 'c': 15, 'W': 5, 'e': 3.0}
LAMS = 0.70
K_A2 = 33


# ------------------------------------------------------------------ dirs
def fib_dirs(npts):
    i = np.arange(npts, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi), np.cos(phi)], axis=1)


R_NODES = 10.0 + (np.arange(41, dtype=DTYPE) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
DIRS642 = fib_dirs(642)
FINE_R = np.linspace(10.0, 20.0, 401)


# ------------------------------------------------------------------ S_ab
def S_ab(r, a, b):
    r = np.asarray(r, dtype=DTYPE)
    S = np.ones_like(r); Sp = np.zeros_like(r); Spp = np.zeros_like(r)
    S[r >= 20.0] = 0.0
    m = (r > 10.0) & (r < 20.0)
    if np.any(m):
        u = (r[m] - 10.0) / 10.0
        B = beta_fn(a + 1.0, b + 1.0)
        S[m] = 1.0 - betainc(a + 1.0, b + 1.0, u)
        f = u ** a * (1.0 - u) ** b
        Sp[m] = -f / (10.0 * B)
        with np.errstate(divide='ignore', invalid='ignore'):
            fp = (u ** (a - 1.0) * (1.0 - u) ** (b - 1.0)
                  * (a * (1.0 - u) - b * u))
        fp = np.where(np.isfinite(fp), fp, 0.0)
        Spp[m] = -fp / (100.0 * B)
    return S, Sp, Spp


# ------------------------------------------------------- plateau lapse B
def _H(t):
    t = np.asarray(t, dtype=DTYPE)
    out = np.where(t >= 1.0, 1.0, 0.0)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 10.0 * t ** 3 - 15.0 * t ** 4 + 6.0 * t ** 5, out)


def _Hp(t):
    t = np.asarray(t, dtype=DTYPE)
    out = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 30.0 * t ** 2 * (1.0 - t) ** 2, out)


def _Hpp(t):
    t = np.asarray(t, dtype=DTYPE)
    out = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 60.0 * t * (1.0 - t) * (1.0 - 2.0 * t), out)


def shape_B_plat(r, c, W, e):
    r = np.asarray(r, dtype=DTYPE)
    r1 = c - W; r2 = c + W
    x = (r - r1) / e; y = (r2 - r) / e
    Hx, Hy = _H(x), _H(y)
    Hpx, Hpy = _Hp(x), _Hp(y)
    Hppx, Hppy = _Hpp(x), _Hpp(y)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return B, Bp, Bpp


def lapse_funcs_p(spec, r):
    r = np.asarray(r, dtype=DTYPE)
    A = spec['A']
    N = np.ones_like(r); Np = np.zeros_like(r); Npp = np.zeros_like(r)
    if A == 0.0:
        return N, Np, Npp
    B, Bp, Bpp = shape_B_plat(r, spec['c'], spec['W'], spec['e'])
    return 1.0 + A * B, A * Bp, A * Bpp


# ------------------------------------------------------------------ M ramp
def _ss(x):
    return (6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3,
            30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2,
            120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x)


def _U(r, a, b):
    r = np.asarray(r, dtype=DTYPE)
    U = np.zeros_like(r); Up = np.zeros_like(r); Upp = np.zeros_like(r)
    U = np.where(r >= b, 1.0, U)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss(x)
        U[mid] = v; Up[mid] = vp / (b - a); Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp


def M_funcs(r, prof):
    r = np.asarray(r, dtype=DTYPE)
    if prof['kind'] == 'one':
        return np.ones_like(r), np.zeros_like(r), np.zeros_like(r)
    if prof['kind'] == 'ramp':
        m0 = float(prof['m0'])
        U1, U1p, U1pp = _U(r, float(prof['r1']), float(prof['r2']))
        U2, U2p, U2pp = _U(r, 21.0, 24.0)
        return (1.0 + m0 * (U1 - U2), m0 * (U1p - U2p),
                m0 * (U1pp - U2pp))
    raise ValueError(prof['kind'])


# ------------------------------------------------------- spline corrections
def _eval_corr(cs, r):
    r = np.asarray(r, dtype=DTYPE)
    rc = np.clip(r, 10.0, 20.0)
    d = cs(rc); dp = cs.derivative(1)(rc); dpp = cs.derivative(2)(rc)
    out = r < 10.0; over = r > 20.0
    if np.any(out):
        dp = np.where(out, 0.0, dp); dpp = np.where(out, 0.0, dpp)
    if np.any(over):
        dp = np.where(over, 0.0, dp); dpp = np.where(over, 0.0, dpp)
    return d, dp, dpp


class Centre:
    """Phase 344 A2 centre: winner spec, lamS=0.70, M ramp, K=33
    not-a-knot cubic-spline corrections (additive to S, N, M)."""

    def __init__(self, vS, vN, vM, K=33, m_r2=20.0):
        self.vS = np.asarray(vS, dtype=DTYPE)
        self.vN = np.asarray(vN, dtype=DTYPE)
        self.vM = np.asarray(vM, dtype=DTYPE)
        self.K = K
        xk = np.linspace(10.0, 20.0, K)
        self.csS = CubicSpline(xk, self.vS, bc_type='not-a-knot')
        self.csN = CubicSpline(xk, self.vN, bc_type='not-a-knot')
        self.csM = CubicSpline(xk, self.vM, bc_type='not-a-knot')
        self.spec = dict(WINNER_SPEC)
        self.prof = {'kind': 'ramp', 'm0': 6.0, 'r1': 8.5, 'r2': m_r2}

    def base_profiles(self, r):
        """(S0,Sp,Spp, N0,Np,Npp, M0,Mp,Mpp) at radii r (1-D array)."""
        r = np.asarray(r, dtype=DTYPE)
        S, Sp, Spp = S_ab(r, self.spec['a'], self.spec['b'])
        S, Sp, Spp = LAMS * S, LAMS * Sp, LAMS * Spp
        N, Np, Npp = lapse_funcs_p(self.spec, r)
        M, Mp, Mpp = M_funcs(r, self.prof)
        dS, dSp, dSpp = _eval_corr(self.csS, r)
        dN, dNp, dNpp = _eval_corr(self.csN, r)
        dM, dMp, dMpp = _eval_corr(self.csM, r)
        return (S + dS, Sp + dSp, Spp + dSpp,
                N + dN, Np + dNp, Npp + dNpp,
                M + dM, Mp + dMp, Mpp + dMpp)


# ---------------------------------------------------------------- waveform
def _smooth(x):
    return (10.0 * x ** 3 - 15.0 * x ** 4 + 6.0 * x ** 5,
            30.0 * x ** 2 - 60.0 * x ** 3 + 30.0 * x ** 4,
            60.0 * x - 180.0 * x ** 2 + 120.0 * x ** 3)


def dwelling_mu(phi, a, D, m):
    """(mu, mu_phi, mu_phiphi) of the Phase 364 SS2 dwelling waveform.
    Scalar or array phi."""
    phi = np.asarray(phi, dtype=DTYPE)
    ph = (phi + np.pi) % (2.0 * np.pi) - np.pi
    w = np.empty_like(ph); wp = np.zeros_like(ph); wpp = np.zeros_like(ph)
    L = np.pi * (1.0 - D)
    top = np.abs(ph) <= np.pi * D
    w[top] = 1.0
    fall = ph > np.pi * D
    if np.any(fall):
        x = (ph[fall] - np.pi * D) / L
        s, sp, spp = _smooth(x)
        w[fall] = 1.0 - 2.0 * s
        wp[fall] = -2.0 * sp / L
        wpp[fall] = -2.0 * spp / L ** 2
    rise = ph < -np.pi * D
    if np.any(rise):
        x = (ph[rise] + np.pi) / L
        s, sp, spp = _smooth(x)
        w[rise] = -1.0 + 2.0 * s
        wp[rise] = 2.0 * sp / L
        wpp[rise] = 2.0 * spp / L ** 2
    mu = 1.0 + a * (m + (1.0 - m) * w)
    return mu, a * (1.0 - m) * wp, a * (1.0 - m) * wpp


def mu_at(member, phi, mode='dwell'):
    """(mu, mu_dot, mu_ddot) for a member dict at phase phi."""
    Om = member['Om']
    if mode == 'sine':
        a = member['a']
        mu = 1.0 + a * np.cos(phi)
        mud = -a * np.sin(phi) * Om
        mudd = -a * np.cos(phi) * Om ** 2
        return float(mu), float(mud), float(mudd)
    mu, mup, mupp = dwelling_mu(phi, member['a'], member['D'], member['m'])
    return float(mu), float(Om * mup), float(Om ** 2 * mupp)


# ------------------------------------------- modulated profile bundle
# A bundle is a dict F in {S,N,M} -> dict with keys
# v, r, rr, t, tt, rt  (value, d_r, d_rr, d_t, d_tt, d_rt), each (P,).
def bundle_at(centre, r, member, phi, mode='dwell',
              flat=False, mu_override=None):
    r = np.asarray(r, dtype=DTYPE)
    if flat:
        z = np.zeros_like(r); o = np.ones_like(r)
        base = (z.copy(), z.copy(), z.copy(),
                o.copy(), z.copy(), z.copy(),
                o.copy(), z.copy(), z.copy())
    else:
        base = centre.base_profiles(r)
    S0, Sp, Spp, N0, Np, Npp, M0, Mp, Mpp = base
    if mu_override is not None:
        mu, mud, mudd = mu_override
    elif member is None or member.get('a', 0.0) == 0.0:
        mu, mud, mudd = 1.0, 0.0, 0.0
    else:
        mu, mud, mudd = mu_at(member, phi, mode)
    subset = member['subset'] if member is not None else 'NONE'
    out = {}

    def mod(F0, Fp, Fpp, on):
        z = np.zeros_like(r)
        if on:
            return {'v': mu * F0, 'r': mu * Fp, 'rr': mu * Fpp,
                    't': mud * F0, 'tt': mudd * F0, 'rt': mud * Fp}
        return {'v': F0, 'r': Fp, 'rr': Fpp, 't': z, 'tt': z, 'rt': z}

    out['S'] = mod(S0, Sp, Spp, 'S' in subset or subset == 'SNM')
    out['N'] = mod(N0, Np, Npp, 'N' in subset or subset == 'SNM')
    H0 = M0 - 1.0
    if 'M' in subset or subset == 'SNM':
        out['M'] = {'v': 1.0 + mu * H0, 'r': mu * Mp, 'rr': mu * Mpp,
                    't': mud * H0, 'tt': mudd * H0, 'rt': mud * Mp}
    else:
        z = np.zeros_like(r)
        out['M'] = {'v': M0, 'r': Mp, 'rr': Mpp, 't': z, 'tt': z, 'rt': z}
    out['mu'] = mu; out['mu_dot'] = mud; out['mu_ddot'] = mudd
    return out


# ---------------------------------------------------------- tensor algebra
def _scalar_derivs(F, n, r):
    """dF (P,4), ddF (P,4,4) for a radial/time scalar bundle F."""
    P = len(r)
    rsafe = np.where(r > 0, r, 1.0)
    dF = np.zeros((P, 4), dtype=DTYPE)
    dF[:, 0] = F['t']
    dF[:, 1:] = F['r'][:, None] * n
    ddF = np.zeros((P, 4, 4), dtype=DTYPE)
    ddF[:, 0, 0] = F['tt']
    ddF[:, 0, 1:] = F['rt'][:, None] * n
    ddF[:, 1:, 0] = F['rt'][:, None] * n
    Pm = np.eye(3)[None, :, :] - n[:, :, None] * n[:, None, :]
    ddF[:, 1:, 1:] = (F['rr'][:, None, None] * n[:, :, None] * n[:, None, :]
                      + (F['r'] / rsafe)[:, None, None] * Pm)
    return dF, ddF


def einstein_from_bundle(pts, bundle):
    """(Tcov, g) at pts (P,3) from a profile bundle at r=|pts|."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rsafe[:, None], 0.0)
    S, N, M = bundle['S'], bundle['N'], bundle['M']
    H = {'v': M['v'] - 1.0, 'r': M['r'], 'rr': M['rr'],
         't': M['t'], 'tt': M['tt'], 'rt': M['rt']}
    dS, ddS = _scalar_derivs(S, n, r)
    dN, ddN = _scalar_derivs(N, n, r)

    # gamma_ij = delta_ij + H n_i n_j ; derivatives
    Pm = np.eye(3)[None, :, :] - n[:, :, None] * n[:, None, :]  # (P,3,3)
    gam = np.eye(3)[None, :, :] + H['v'][:, None, None] * n[:, :, None] * n[:, None, :]
    dgam = np.zeros((P, 4, 3, 3), dtype=DTYPE)      # [e,i,j]
    ddgam = np.zeros((P, 4, 4, 3, 3), dtype=DTYPE)  # [e,f,i,j]
    # A_kij = d_k(n_i n_j) * r
    A = np.zeros((P, 3, 3, 3), dtype=DTYPE)
    for k in range(3):
        for i in range(3):
            for j in range(3):
                A[:, k, i, j] = ((1.0 if k == i else 0.0) * n[:, j]
                                 + (1.0 if k == j else 0.0) * n[:, i]
                                 - 2.0 * n[:, k] * n[:, i] * n[:, j])
    hovr = H['v'] / rsafe
    for k in range(3):
        dgam[:, k + 1] = (H['r'][:, None, None]
                          * n[:, k][:, None, None] * n[:, :, None] * n[:, None, :]
                          + hovr[:, None, None] * A[:, k])
    dgam[:, 0] = H['t'][:, None, None] * n[:, :, None] * n[:, None, :]
    # spatial-spatial second derivatives (exact differentiation)
    for k in range(3):
        for l in range(3):
            dA = np.zeros((P, 3, 3), dtype=DTYPE)
            for i in range(3):
                for j in range(3):
                    dA[:, i, j] = (
                        Pm[:, l, j] * (1.0 if k == i else 0.0)
                        + Pm[:, l, i] * (1.0 if k == j else 0.0)
                        - 2.0 * (Pm[:, l, k] * n[:, i] * n[:, j]
                                 + n[:, k] * Pm[:, l, i] * n[:, j]
                                 + n[:, k] * n[:, i] * Pm[:, l, j])) / rsafe
            ddgam[:, l + 1, k + 1] = (
                H['rr'][:, None, None] * n[:, l][:, None, None]
                * n[:, k][:, None, None] * n[:, :, None] * n[:, None, :]
                + (H['r'] / rsafe)[:, None, None] * (
                    Pm[:, l, k][:, None, None] * n[:, :, None] * n[:, None, :]
                    + n[:, k][:, None, None] * Pm[:, l, :][:, :, None] * n[:, None, :]
                    + n[:, k][:, None, None] * n[:, :, None] * Pm[:, l, :][:, None, :])
                + (n[:, l] * (H['r'] / rsafe - H['v'] / rsafe ** 2))[:, None, None] * A[:, k]
                + hovr[:, None, None] * dA)
    # mixed time-spatial and time-time gamma derivatives
    for k in range(3):
        val = (H['rt'][:, None, None] * n[:, k][:, None, None]
               * n[:, :, None] * n[:, None, :]
               + (H['t'] / rsafe)[:, None, None] * A[:, k])
        ddgam[:, 0, k + 1] = val
        ddgam[:, k + 1, 0] = val
    ddgam[:, 0, 0] = H['tt'][:, None, None] * n[:, :, None] * n[:, None, :]

    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -N['v'] ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S['v']
    g[:, 1:, 1:] = gam
    ginv = np.linalg.inv(g)

    dg = np.zeros((P, 4, 4, 4), dtype=DTYPE)        # [e,mu,nu]
    ddg = np.zeros((P, 4, 4, 4, 4), dtype=DTYPE)    # [e,f,mu,nu]
    dg[:, :, 0, 0] = -2.0 * N['v'][:, None] * dN
    ddg[:, :, :, 0, 0] = -2.0 * (dN[:, :, None] * dN[:, None, :]
                                 + N['v'][:, None, None] * ddN)
    dg[:, :, 0, 1] = dg[:, :, 1, 0] = -BETA * dS
    ddg[:, :, :, 0, 1] = ddg[:, :, :, 1, 0] = -BETA * ddS
    dg[:, :, 1:, 1:] = dgam
    ddg[:, :, :, 1:, 1:] = ddgam

    return einstein_from_gdg(g, dg, ddg), g


def einstein_from_gdg(g, dg, ddg):
    """Einstein/8pi from g (P,4,4), dg (P,4,4,4) [e,mu,nu],
    ddg (P,4,4,4,4) [e,f,mu,nu]. Standard Christoffel/Ricci algebra."""
    ginv = np.linalg.inv(g)
    T1 = dg + np.einsum('pcdb->pbdc', dg) - np.einsum('pdbc->pbdc', dg)
    Gam = 0.5 * np.einsum('pad,pbdc->pabc', ginv, T1)
    dginv = -np.einsum('pam,pemn,pnb->peab', ginv, dg, ginv)
    dT1 = (ddg + np.einsum('pecdb->pebdc', ddg)
           - np.einsum('pedbc->pebdc', ddg))
    dGam = 0.5 * (np.einsum('pead,pbdc->peabc', dginv, T1)
                  + np.einsum('pad,pebdc->peabc', ginv, dT1))
    Ric = (np.einsum('paabd->pbd', dGam) - np.einsum('pdaba->pbd', dGam)
           + np.einsum('paae,pebd->pbd', Gam, Gam)
           - np.einsum('pade,peba->pbd', Gam, Gam))
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g
    return G / EIGHT_PI


def T_at(centre, pts, member, phi, mode='dwell', flat=False,
         mu_override=None):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    b = bundle_at(centre, r, member, phi, mode, flat=flat,
                  mu_override=mu_override)
    return einstein_from_bundle(pts, b)


# ------------------------------------------------------------- Eulerian
def eulerian_that(g, Tcov):
    g = np.asarray(g, dtype=DTYPE)
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...', beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DTYPE)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = V[..., :, i] / np.sqrt(lam[..., i])[..., None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


# ------------------------------------------------------------- margins
def sampled_margins(That, n_dir=162, n_vel=6):
    dirs = fib_dirs(n_dir)
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    nec_min = np.empty(Np); wec_min = np.empty(Np)
    sec_min = np.empty(Np); dec_min = np.empty(Np)
    vels = np.linspace(0.0, 0.95, n_vel)
    CH = 8192
    for s0 in range(0, Np, CH):
        F = flat[s0:s0 + CH]
        T00 = F[:, 0, 0]; T0i = F[:, 0, 1:]; Tij = F[:, 1:, 1:]
        tr = np.trace(Tij, axis1=1, axis2=2)
        # quad[n,i] = dirs_i . Tij_n . dirs_i (explicit component form)
        Td = np.matmul(Tij, dirs.T)          # [n,j,i] = sum_k Tij_jk dir_ik
        quad = np.sum(Td * dirs.T[None, :, :], axis=1)
        T0d = T0i @ dirs.T
        nec_min[s0:s0 + CH] = (T00[:, None] + 2.0 * T0d + quad).min(axis=1)
        wm = np.full(F.shape[0], np.inf); sm = np.full(F.shape[0], np.inf)
        dm = np.full(F.shape[0], np.inf)
        Mm = F.copy(); Mm[:, 0, :] *= -1.0
        # Md[n,i,a] = sum_b Mm[n,a,b] * Vdir_b, Vdir = (1, v*dirs_i) / gam
        Msp = [Mm[:, a, 1:] @ dirs.T for a in range(4)]  # (Np,n_dir) each
        for v in vels:
            gam = 1.0 / np.sqrt(1.0 - v * v)
            wec_vals = gam ** 2 * (T00[:, None] + 2.0 * v * T0d
                                   + v * v * quad)
            wm = np.minimum(wm, wec_vals.min(axis=1))
            trT = -T00 + tr
            sec_vals = wec_vals - 0.5 * trT[:, None] * gam ** 2 * (v * v - 1.0)
            sm = np.minimum(sm, sec_vals.min(axis=1))
            # Ups^a = -gam * (Mm^a_0 + v * Msp[a]), kept unstacked
            U0 = -gam * (Mm[:, 0, 0][:, None] + v * Msp[0])
            U1 = -gam * (Mm[:, 1, 0][:, None] + v * Msp[1])
            U2 = -gam * (Mm[:, 2, 0][:, None] + v * Msp[2])
            U3 = -gam * (Mm[:, 3, 0][:, None] + v * Msp[3])
            q = U0 ** 2 - U1 ** 2 - U2 ** 2 - U3 ** 2
            nrm = 1.0 + U0 ** 2 + U1 ** 2 + U2 ** 2 + U3 ** 2
            val = np.where(U0 > 0, q / nrm, -np.abs(q) / nrm - 1.0)
            dm = np.minimum(dm, val.min(axis=1))
        wec_min[s0:s0 + CH] = wm; sec_min[s0:s0 + CH] = sm
        dec_min[s0:s0 + CH] = dm
    return {'nec_s': nec_min.reshape(shp), 'wec_s': wec_min.reshape(shp),
            'sec_s': sec_min.reshape(shp), 'dec_s': dec_min.reshape(shp)}


def hawking_ellis_margins(That, do_fallback=True):
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy(); M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k_idx = np.argmax(cand, axis=1)
    ar = np.arange(Np)
    rho = np.where(typeI, -evals[ar, k_idx].real, np.nan)
    mask = np.ones((Np, 4), dtype=bool); mask[ar, k_idx] = False
    ps_all = evals.real[mask].reshape(Np, 3)
    ps = np.where(typeI[:, None], ps_all, np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    filled = np.zeros(Np, dtype=bool)
    if do_fallback and np.any(~typeI):
        sub = sampled_margins(flat[~typeI].reshape(-1, 4, 4))
        idx = np.where(~typeI)[0]
        nec[idx] = sub['nec_s']; wec[idx] = sub['wec_s']
        sec[idx] = sub['sec_s']; dec[idx] = sub['dec_s']
        filled[idx] = True
    return {'rho_eig': rho.reshape(shp), 'p': ps.reshape(shp + (3,)),
            'typeI': typeI.reshape(shp), 'sampled_filled': filled.reshape(shp),
            'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
            'sec': sec.reshape(shp), 'dec': dec.reshape(shp),
            'rho_euler': That[..., 0, 0]}


def margins_chunked(That, chunk=4096):
    m = hawking_ellis_margins(That, do_fallback=False)
    bad = np.where(~m['typeI'])[0]
    if bad.size:
        for s in range(0, bad.size, chunk):
            idx = bad[s:s + chunk]
            sub = sampled_margins(That[idx])
            m['nec'][idx] = sub['nec_s']; m['wec'][idx] = sub['wec_s']
            m['sec'][idx] = sub['sec_s']; m['dec'][idx] = sub['dec_s']
            m['sampled_filled'][idx] = True
    return m


# ------------------------------------------------------------- SET read
def set_read(centre, member, phi, mode='dwell', flat=False,
             mu_override=None, want_aux=True):
    pts_all = (DIRS162[None, :, :] * R_NODES[:, None, None]).reshape(-1, 3)
    T, g = T_at(centre, pts_all, member, phi, mode, flat=flat,
                mu_override=mu_override)
    That_all = eulerian_that(g, T)
    m = margins_chunked(That_all)
    R = {'typeI': m['typeI'], 'nec': m['nec'], 'wec': m['wec'],
         'dec': m['dec'], 'sec': m['sec'], 'rho': That_all[:, 0, 0]}
    typeI_pts = [pts_all[m['typeI']]]
    typeI_nec = [m['nec'][m['typeI']]]

    def st(arr):
        return {'min': float(np.min(arr)), 'median': float(np.median(arr)),
                'max': float(np.max(arr))}
    i_nec = int(np.argmin(R['nec'])); i_dec = int(np.argmin(R['dec']))
    i_r, i_d = divmod(i_nec, 162); j_r, j_d = divmod(i_dec, 162)
    out = {
        'set': 'SET-244 (41 radial midpoint nodes x 162 Fibonacci dirs)',
        'sampler': 'SAMPLER-M', 'n_points': int(len(R['typeI'])),
        'typeI_fraction': float(np.mean(R['typeI'])),
        'typeI_count': int(np.sum(R['typeI'])),
        'nec': st(R['nec']), 'wec': st(R['wec']), 'dec': st(R['dec']),
        'sec': st(R['sec']), 'rho': st(R['rho']),
        'nec_argmin_point': (DIRS162[i_d] * R_NODES[i_r]).tolist(),
        'nec_argmin_r': float(R_NODES[i_r]),
        'dec_argmin_point': (DIRS162[j_d] * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
        'typeI_nec_min': (float(np.min(np.concatenate(typeI_nec)))
                          if typeI_nec else None),
    }
    aux = None
    if want_aux:
        aux = {'R': R, 'That': That_all,
               'typeI_pts': (np.vstack(typeI_pts) if typeI_pts
                             else np.zeros((0, 3))),
               'typeI_nec': (np.concatenate(typeI_nec) if typeI_nec
                             else np.zeros(0)),
               'nec_argmin_That': That_all[i_nec],
               'nec_argmin_index': i_nec}
    return out, aux


def floors_ok(centre, member, phi, mode='dwell'):
    b = bundle_at(centre, FINE_R, member, phi, mode)
    return bool(np.min(b['N']['v']) >= 0.55 and np.min(b['M']['v']) >= 1.0)


def nec_at_point(centre, member, phi, pt, mode='dwell'):
    pt = np.asarray(pt, dtype=DTYPE)
    T, g = T_at(centre, pt[None, :], member, phi, mode)
    That = eulerian_that(g, T)
    m_he = hawking_ellis_margins(That, do_fallback=False)
    m_mc = margins_chunked(That)
    return float(m_mc['nec'][0]), bool(m_he['typeI'][0]), That[0]


def adversary_polish(centre, member, phi, aux, mode='dwell'):
    pts_ti = aux['typeI_pts']; nec_ti = aux['typeI_nec']
    if len(pts_ti) == 0:
        return None
    rr_ti = np.linalg.norm(pts_ti, axis=1)

    def objective(x):
        rr, th, ph = x
        if rr < 10.0 or rr > 20.0:
            return 1.0
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = nec_at_point(centre, member, phi, pt, mode)
        return nec if is_ti else nec + 1.0

    order = np.argsort(nec_ti)[:5]
    starts = [{'set_point': pts_ti[i].tolist(), 'set_r': float(rr_ti[i]),
               'set_nec': float(nec_ti[i])} for i in order]
    polished = []
    for i in order:
        p0 = pts_ti[i]
        r0 = float(np.linalg.norm(p0))
        x0 = np.array([r0, np.arccos(np.clip(p0[2] / r0, -1, 1)),
                       np.arctan2(p0[1], p0[0])])
        res = minimize(objective, x0, method='Nelder-Mead',
                       options={'maxiter': 300, 'xatol': 1e-4, 'fatol': 1e-7})
        rr, th, ph = res.x
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = nec_at_point(centre, member, phi, pt, mode)
        polished.append({'start_set_nec': float(nec_ti[i]),
                         'polished_point': pt.tolist(),
                         'polished_r': float(rr),
                         'polished_objective': float(res.fun),
                         'polished_nec_SAMPLER-M': nec,
                         'polished_typeI': is_ti})
    cand = [p for p in polished if p['polished_typeI']]
    if cand:
        best_p = min(cand, key=lambda p: p['polished_nec_SAMPLER-M'])
        site_pt = np.array(best_p['polished_point'], dtype=DTYPE)
        source = 'polished'
    else:
        i0 = int(order[0]); site_pt = pts_ti[i0]; best_p = None
        source = 'set_argmin_fallback'
    nec_site, is_ti_site, That_site = nec_at_point(
        centre, member, phi, site_pt, mode)
    r_site = float(np.linalg.norm(site_pt))
    return {'source': source, 'point': site_pt.tolist(), 'r': r_site,
            'direction': (site_pt / r_site).tolist(),
            'typeI': bool(is_ti_site),
            'in_region_worst_nec_SAMPLER-M': nec_site,
            'rho_t': float(That_site[0, 0]),
            'polish_starts': starts, 'polished': polished,
            'best_polished': best_p}


def worst_null(That):
    def q_of(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)
    vals = np.array([q_of(d) for d in DIRS642])
    n_best = DIRS642[int(np.argmin(vals))]
    th0 = np.arccos(np.clip(n_best[2], -1, 1))
    ph0 = np.arctan2(n_best[1], n_best[0])

    def obj(x):
        th, ph = x
        n = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph),
                      np.cos(th)])
        return q_of(n)
    res = minimize(obj, np.array([th0, ph0]), method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10, 'fatol': 1e-14})
    th, ph = res.x
    n_fin = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph),
                      np.cos(th)])
    return n_fin, float(obj(res.x)), float(np.min(vals))


# ------------------------------------------------- FD independent path
def metric_of_txyz(centre, member, txyz, mode='dwell'):
    """Metric (P,4,4) at (t,x,y,z) rows, from modulated profiles."""
    txyz = np.asarray(txyz, dtype=DTYPE)
    t = txyz[:, 0]; xyz = txyz[:, 1:]
    r = np.linalg.norm(xyz, axis=1)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, xyz / rsafe[:, None], 0.0)
    Om = member['Om']
    g = np.zeros((len(txyz), 4, 4), dtype=DTYPE)
    # mu varies per point through t: evaluate bundle per distinct phi by
    # grouping on t (FD calls use few distinct t values)
    S = np.zeros(len(txyz)); N = np.zeros(len(txyz)); M = np.zeros(len(txyz))
    for tv in np.unique(t):
        sel = t == tv
        phi = Om * tv
        b = bundle_at(centre, r[sel], member, phi, mode)
        S[sel] = b['S']['v']; N[sel] = b['N']['v']; M[sel] = b['M']['v']
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + (M - 1.0) * n[:, i] * n[:, j])
    return g


def _fd4_4d(func, pts4, h, axis):
    offs = []
    for k in (-2, -1, 1, 2):
        p = pts4.copy(); p[:, axis] += k * h
        offs.append(func(p))
    return (offs[0] - 8.0 * offs[1] + 8.0 * offs[2] - offs[3]) / (12.0 * h)


def _gamma_fd(func, pts4, h):
    g = func(pts4)
    ginv = np.linalg.inv(g)
    dg = [np.zeros_like(g) for _ in range(4)]
    for a in range(4):
        dg[a] = _fd4_4d(func, pts4, h, a)
    Gam = np.zeros(pts4.shape[:1] + (4, 4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.zeros(pts4.shape[:1] + (4,), dtype=DTYPE)
                for d in range(4):
                    term[..., d] = dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                Gam[..., a, b, c] = 0.5 * np.einsum('...d,...d->...', ginv[..., a, :], term)
    return Gam, g, ginv


def einstein_fd(centre, member, pts4, h, mode='dwell'):
    """From-scratch 4D FD Einstein tensor at (t,x,y,z) points.
    Returns (T, g)."""
    func = lambda p: metric_of_txyz(centre, member, p, mode)
    Gam, g, ginv = _gamma_fd(func, pts4, h)

    def gamma_shift(axis, k):
        p = pts4.copy(); p[:, axis] += k * h
        return _gamma_fd(func, p, h)[0]

    Ric = np.zeros(pts4.shape[:1] + (4, 4), dtype=DTYPE)
    for e in range(4):
        dGe = (gamma_shift(e, -2) - 8.0 * gamma_shift(e, -1)
               + 8.0 * gamma_shift(e, 1) - gamma_shift(e, 2)) / (12.0 * h)
        for b_ in range(4):
            for d_ in range(4):
                Ric[..., b_, d_] += dGe[..., e, b_, d_]
                if d_ == e:
                    for a in range(4):
                        Ric[..., b_, d_] -= dGe[..., a, b_, a]
    for b_ in range(4):
        for d_ in range(4):
            for a in range(4):
                for e in range(4):
                    Ric[..., b_, d_] += (Gam[..., a, a, e] * Gam[..., e, b_, d_]
                                         - Gam[..., a, d_, e] * Gam[..., e, b_, a])
    Rs = np.einsum('...ab,...ab->...', ginv, Ric)
    G = Ric - 0.5 * Rs[..., None, None] * g
    return G / EIGHT_PI, g
