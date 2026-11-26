#!/usr/bin/env python3
"""
g40_lib.py -- Gate-40 independent machinery, written for this gate.
No imports from any phase library, from Gate-39, or from verify_metric.
Only numpy/scipy.

Metric (coords t,x,y,z; signature -,+,+,+; G = c = 1):
  g_tt = -N(r,t)^2
  g_tx = g_xt = -beta * S(r,t),  beta = 1.1
  gamma_ij = delta_ij + (M(r,t)-1) n_i n_j,  n = x_vec/r

Einstein tensor from the metric's first/second derivative tensors via
the Christoffel -> Ricci algebra, vectorised with einsum.  Radial
scalars: d_i F = F_r n_i, d_i d_j F = F_rr n_i n_j + (F_r/r) P_ij with
P_ij = delta_ij - n_i n_j; d_t F = F_t, d_t d_i F = F_rt n_i.
gamma derivatives use the exact differentiation of H n_i n_j
(H = M-1) with d_k n_i = P_ki / r.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
from scipy.special import betainc, beta as beta_fn

DT = np.float64
EIGHT_PI = 8.0 * np.pi
BETA = 1.1
BAR_DEPTH = -0.0034

SPEC = {'a': 2, 'b': 2, 'A': 0.07439108177516472, 'c': 15, 'W': 5, 'e': 3.0}
LAMS = 0.70


def fib_dirs(npts):
    i = np.arange(npts, dtype=DT)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi),
                     np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


R_NODES = 10.0 + (np.arange(41, dtype=DT) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
DIRS642 = fib_dirs(642)
FINE_R = np.linspace(10.0, 20.0, 401)
SET_PTS = (DIRS162[None, :, :] * R_NODES[:, None, None]).reshape(-1, 3)


# ---------------------------------------------------------------- S shape
def S_ab(r, a, b):
    r = np.asarray(r, dtype=DT)
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


# ------------------------------------------------------------ plateau lapse
def _H(t):
    t = np.asarray(t, dtype=DT)
    out = np.where(t >= 1.0, 1.0, 0.0)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 10.0 * t ** 3 - 15.0 * t ** 4 + 6.0 * t ** 5, out)


def _Hp(t):
    t = np.asarray(t, dtype=DT)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 30.0 * t ** 2 * (1.0 - t) ** 2, 0.0)


def _Hpp(t):
    t = np.asarray(t, dtype=DT)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 60.0 * t * (1.0 - t) * (1.0 - 2.0 * t), 0.0)


def lapse(r):
    r = np.asarray(r, dtype=DT)
    A = SPEC['A']; c = SPEC['c']; W = SPEC['W']; e = SPEC['e']
    r1 = c - W; r2 = c + W
    x = (r - r1) / e; y = (r2 - r) / e
    Hx, Hy = _H(x), _H(y)
    B = Hx * Hy
    Bp = (_Hp(x) * Hy - Hx * _Hp(y)) / e
    Bpp = (_Hpp(x) * Hy - 2.0 * _Hp(x) * _Hp(y) + Hx * _Hpp(y)) / e ** 2
    return 1.0 + A * B, A * Bp, A * Bpp


# ------------------------------------------------------------------- M ramp
def _ss(x):
    return (6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3,
            30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2,
            120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x)


def _U(r, a, b):
    r = np.asarray(r, dtype=DT)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r); Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss(x)
        U[mid] = v; Up[mid] = vp / (b - a); Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp


def M_ramp(r, m0=6.0, r1=8.5, r2=20.0):
    U1, U1p, U1pp = _U(r, r1, r2)
    U2, U2p, U2pp = _U(r, 21.0, 24.0)
    return 1.0 + m0 * (U1 - U2), m0 * (U1p - U2p), m0 * (U1pp - U2pp)


# ------------------------------------------------------------------- centre
def _corr(cs, r):
    r = np.asarray(r, dtype=DT)
    rc = np.clip(r, 10.0, 20.0)
    d = cs(rc); dp = cs.derivative(1)(rc); dpp = cs.derivative(2)(rc)
    off = (r < 10.0) | (r > 20.0)
    if np.any(off):
        dp = np.where(off, 0.0, dp); dpp = np.where(off, 0.0, dpp)
    return d, dp, dpp


class Centre:
    """Phase 344 A2 centre assembled by the gate: winner spec, lamS 0.70,
    M ramp (m0 6.0, r1 8.5, r2 20.0), K=33 not-a-knot spline corrections."""

    def __init__(self, vS, vN, vM, K=33):
        xk = np.linspace(10.0, 20.0, K)
        self.csS = CubicSpline(xk, np.asarray(vS, DT), bc_type='not-a-knot')
        self.csN = CubicSpline(xk, np.asarray(vN, DT), bc_type='not-a-knot')
        self.csM = CubicSpline(xk, np.asarray(vM, DT), bc_type='not-a-knot')

    def base(self, r):
        r = np.asarray(r, dtype=DT)
        S, Sp, Spp = S_ab(r, SPEC['a'], SPEC['b'])
        S, Sp, Spp = LAMS * S, LAMS * Sp, LAMS * Spp
        N, Np, Npp = lapse(r)
        M, Mp, Mpp = M_ramp(r)
        dS, dSp, dSpp = _corr(self.csS, r)
        dN, dNp, dNpp = _corr(self.csN, r)
        dM, dMp, dMpp = _corr(self.csM, r)
        return (S + dS, Sp + dSp, Spp + dSpp,
                N + dN, Np + dNp, Npp + dNpp,
                M + dM, Mp + dMp, Mpp + dMpp)


# ----------------------------------------------------------------- waveform
def _smooth(x):
    return (10.0 * x ** 3 - 15.0 * x ** 4 + 6.0 * x ** 5,
            30.0 * x ** 2 - 60.0 * x ** 3 + 30.0 * x ** 4,
            60.0 * x - 180.0 * x ** 2 + 120.0 * x ** 3)


def dwelling_mu(phi, a, D, m):
    """(mu, mu_phi, mu_phiphi), Phase 364 SS2 dwelling waveform."""
    phi = np.asarray(phi, dtype=DT)
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
    return 1.0 + a * (m + (1.0 - m) * w), a * (1.0 - m) * wp, a * (1.0 - m) * wpp


def member_mu(member, phi, mode='dwell'):
    Om = member['Om']
    if mode == 'sine':
        a = member['a']
        return (1.0 + a * np.cos(phi), -a * np.sin(phi) * Om,
                -a * np.cos(phi) * Om ** 2)
    mu, mup, mupp = dwelling_mu(phi, member['a'], member['D'], member['m'])
    return float(mu), float(Om * mup), float(Om ** 2 * mupp)


# ------------------------------------------------------------------- bundle
def bundle(centre, r, member=None, phi=0.0, mode='dwell', flat=False,
           mu_const=None):
    """Profile bundle: dict F in {S,N,M} -> {v,r,rr,t,tt,rt} at radii r."""
    r = np.asarray(r, dtype=DT)
    if flat:
        z = np.zeros_like(r); o = np.ones_like(r)
        base = (z.copy(), z.copy(), z.copy(), o.copy(), z.copy(), z.copy(),
                o.copy(), z.copy(), z.copy())
    else:
        base = centre.base(r)
    S0, Sp, Spp, N0, Np, Npp, M0, Mp, Mpp = base
    if mu_const is not None:
        mu, mud, mudd = float(mu_const), 0.0, 0.0
    elif member is None or member.get('a', 0.0) == 0.0:
        mu, mud, mudd = 1.0, 0.0, 0.0
    else:
        mu, mud, mudd = member_mu(member, phi, mode)
    subset = member['subset'] if member is not None else set()
    z = np.zeros_like(r)
    out = {}

    def mod(F0, Fp, Fpp, on):
        if on:
            return {'v': mu * F0, 'r': mu * Fp, 'rr': mu * Fpp,
                    't': mud * F0, 'tt': mudd * F0, 'rt': mud * Fp}
        return {'v': F0, 'r': Fp, 'rr': Fpp, 't': z, 'tt': z, 'rt': z}

    out['S'] = mod(S0, Sp, Spp, 'S' in subset)
    out['N'] = mod(N0, Np, Npp, 'N' in subset)
    H0 = M0 - 1.0
    if 'M' in subset:
        out['M'] = {'v': 1.0 + mu * H0, 'r': mu * Mp, 'rr': mu * Mpp,
                    't': mud * H0, 'tt': mudd * H0, 'rt': mud * Mp}
    else:
        out['M'] = {'v': M0, 'r': Mp, 'rr': Mpp, 't': z, 'tt': z, 'rt': z}
    out['mu'] = mu; out['mu_dot'] = mud; out['mu_ddot'] = mudd
    return out


# ------------------------------------------------------------ tensor algebra
def _d_dF(F, n, r):
    P = len(r)
    rsafe = np.where(r > 0, r, 1.0)
    dF = np.zeros((P, 4), dtype=DT)
    dF[:, 0] = F['t']
    dF[:, 1:] = F['r'][:, None] * n
    ddF = np.zeros((P, 4, 4), dtype=DT)
    ddF[:, 0, 0] = F['tt']
    ddF[:, 0, 1:] = F['rt'][:, None] * n
    ddF[:, 1:, 0] = F['rt'][:, None] * n
    Pm = np.eye(3)[None] - n[:, :, None] * n[:, None, :]
    ddF[:, 1:, 1:] = (F['rr'][:, None, None] * n[:, :, None] * n[:, None, :]
                      + (F['r'] / rsafe)[:, None, None] * Pm)
    return dF, ddF


def einstein_gdg(g, dg, ddg):
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


def einstein_at(pts, b):
    pts = np.asarray(pts, dtype=DT)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rsafe[:, None], 0.0)
    S, N, M = b['S'], b['N'], b['M']
    H = {'v': M['v'] - 1.0, 'r': M['r'], 'rr': M['rr'],
         't': M['t'], 'tt': M['tt'], 'rt': M['rt']}
    dS, ddS = _d_dF(S, n, r)
    dN, ddN = _d_dF(N, n, r)
    Pm = np.eye(3)[None] - n[:, :, None] * n[:, None, :]
    gam = np.eye(3)[None] + H['v'][:, None, None] * n[:, :, None] * n[:, None, :]
    # A[k,i,j] = d_k(n_i n_j) * r
    A = np.zeros((P, 3, 3, 3), dtype=DT)
    for k in range(3):
        for i in range(3):
            for j in range(3):
                A[:, k, i, j] = ((1.0 if k == i else 0.0) * n[:, j]
                                 + (1.0 if k == j else 0.0) * n[:, i]
                                 - 2.0 * n[:, k] * n[:, i] * n[:, j])
    dgam = np.zeros((P, 4, 3, 3), dtype=DT)
    ddgam = np.zeros((P, 4, 4, 3, 3), dtype=DT)
    hovr = H['v'] / rsafe
    for k in range(3):
        dgam[:, k + 1] = (H['r'][:, None, None] * n[:, k][:, None, None]
                          * n[:, :, None] * n[:, None, :]
                          + hovr[:, None, None] * A[:, k])
    dgam[:, 0] = H['t'][:, None, None] * n[:, :, None] * n[:, None, :]
    for k in range(3):
        for l in range(3):
            dA = np.zeros((P, 3, 3), dtype=DT)
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
                    + n[:, k][:, None, None] * Pm[:, l, :][:, :, None]
                    * n[:, None, :]
                    + n[:, k][:, None, None] * n[:, :, None]
                    * Pm[:, l, :][:, None, :])
                + (n[:, l] * (H['r'] / rsafe - H['v'] / rsafe ** 2))[:, None, None]
                * A[:, k]
                + hovr[:, None, None] * dA)
    for k in range(3):
        val = (H['rt'][:, None, None] * n[:, k][:, None, None]
               * n[:, :, None] * n[:, None, :]
               + (H['t'] / rsafe)[:, None, None] * A[:, k])
        ddgam[:, 0, k + 1] = val
        ddgam[:, k + 1, 0] = val
    ddgam[:, 0, 0] = H['tt'][:, None, None] * n[:, :, None] * n[:, None, :]

    g = np.zeros((P, 4, 4), dtype=DT)
    g[:, 0, 0] = -N['v'] ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S['v']
    g[:, 1:, 1:] = gam
    dg = np.zeros((P, 4, 4, 4), dtype=DT)
    ddg = np.zeros((P, 4, 4, 4, 4), dtype=DT)
    dg[:, :, 0, 0] = -2.0 * N['v'][:, None] * dN
    ddg[:, :, :, 0, 0] = -2.0 * (dN[:, :, None] * dN[:, None, :]
                                 + N['v'][:, None, None] * ddN)
    dg[:, :, 0, 1] = dg[:, :, 1, 0] = -BETA * dS
    ddg[:, :, :, 0, 1] = ddg[:, :, :, 1, 0] = -BETA * ddS
    dg[:, :, 1:, 1:] = dgam
    ddg[:, :, :, 1:, 1:] = ddgam
    return einstein_gdg(g, dg, ddg), g


def T_at(centre, pts, member=None, phi=0.0, mode='dwell', flat=False,
         mu_const=None):
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    b = bundle(centre, r, member, phi, mode, flat=flat, mu_const=mu_const)
    return einstein_at(pts, b)


# ----------------------------------------------------------------- Eulerian
def eulerian_that(g, Tcov):
    gamma = g[..., 1:, 1:]
    bcov = g[..., 0, 1:]
    ginv = np.linalg.inv(gamma)
    bup = np.einsum('...ij,...j->...i', ginv, bcov)
    al2 = -g[..., 0, 0] + np.einsum('...i,...i->...', bcov, bup)
    al = np.sqrt(np.maximum(al2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DT)
    E[..., 0, 0] = 1.0 / al
    E[..., 1:, 0] = -bup / al[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = V[..., :, i] / np.sqrt(lam[..., i])[..., None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


# ------------------------------------------------------------------ margins
def sampled_margins(That, n_dir=162, n_vel=6):
    dirs = fib_dirs(n_dir)
    flat = np.asarray(That, dtype=DT).reshape(-1, 4, 4)
    Np = flat.shape[0]
    nec = np.empty(Np); wec = np.empty(Np); sec = np.empty(Np); dec = np.empty(Np)
    vels = np.linspace(0.0, 0.95, n_vel)
    CH = 8192
    for s0 in range(0, Np, CH):
        F = flat[s0:s0 + CH]
        T00 = F[:, 0, 0]; T0i = F[:, 0, 1:]; Tij = F[:, 1:, 1:]
        tr = np.trace(Tij, axis1=1, axis2=2)
        Td = np.matmul(Tij, dirs.T)
        quad = np.sum(Td * dirs.T[None], axis=1)
        T0d = T0i @ dirs.T
        nec[s0:s0 + CH] = (T00[:, None] + 2.0 * T0d + quad).min(axis=1)
        wm = np.full(len(F), np.inf); sm = np.full(len(F), np.inf)
        dm = np.full(len(F), np.inf)
        Mm = F.copy(); Mm[:, 0, :] *= -1.0
        Msp = [Mm[:, a, 1:] @ dirs.T for a in range(4)]
        for v in vels:
            gam = 1.0 / np.sqrt(1.0 - v * v)
            wv = gam ** 2 * (T00[:, None] + 2.0 * v * T0d + v * v * quad)
            wm = np.minimum(wm, wv.min(axis=1))
            trT = -T00 + tr
            sv = wv - 0.5 * trT[:, None] * gam ** 2 * (v * v - 1.0)
            sm = np.minimum(sm, sv.min(axis=1))
            U = [-gam * (Mm[:, a, 0][:, None] + v * Msp[a]) for a in range(4)]
            q = U[0] ** 2 - U[1] ** 2 - U[2] ** 2 - U[3] ** 2
            nrm = 1.0 + U[0] ** 2 + U[1] ** 2 + U[2] ** 2 + U[3] ** 2
            val = np.where(U[0] > 0, q / nrm, -np.abs(q) / nrm - 1.0)
            dm = np.minimum(dm, val.min(axis=1))
        wec[s0:s0 + CH] = wm; sec[s0:s0 + CH] = sm; dec[s0:s0 + CH] = dm
    shp = np.asarray(That).shape[:-2]
    return {'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
            'sec': sec.reshape(shp), 'dec': dec.reshape(shp)}


def margins(That):
    That = np.asarray(That, dtype=DT)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy(); M[:, 0, :] *= -1.0
    ev, evec = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(ev.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(ev.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evec) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k = np.argmax(cand, axis=1)
    ar = np.arange(Np)
    rho = np.where(typeI, -ev[ar, k].real, np.nan)
    mask = np.ones((Np, 4), dtype=bool); mask[ar, k] = False
    ps = np.where(typeI[:, None], ev.real[mask].reshape(Np, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    filled = np.zeros(Np, dtype=bool)
    bad = np.where(~typeI)[0]
    if bad.size:
        for s in range(0, bad.size, 4096):
            idx = bad[s:s + 4096]
            sub = sampled_margins(flat[idx])
            nec[idx] = sub['nec']; wec[idx] = sub['wec']
            sec[idx] = sub['sec']; dec[idx] = sub['dec']
            filled[idx] = True
    return {'typeI': typeI.reshape(shp), 'sampled_filled': filled.reshape(shp),
            'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
            'sec': sec.reshape(shp), 'dec': dec.reshape(shp),
            'rho': flat[:, 0, 0].reshape(shp)}


# ------------------------------------------------------------------ SET read
def set_read(centre, member=None, phi=0.0, mode='dwell', flat=False,
             mu_const=None, want_aux=False):
    T, g = T_at(centre, SET_PTS, member, phi, mode, flat=flat,
                mu_const=mu_const)
    That = eulerian_that(g, T)
    m = margins(That)

    def st(a):
        return {'min': float(np.min(a)), 'median': float(np.median(a)),
                'max': float(np.max(a))}
    i_nec = int(np.argmin(m['nec'])); i_dec = int(np.argmin(m['dec']))
    i_r, i_d = divmod(i_nec, 162); j_r, j_d = divmod(i_dec, 162)
    out = {'nec': st(m['nec']), 'wec': st(m['wec']), 'dec': st(m['dec']),
           'sec': st(m['sec']), 'rho': st(That[:, 0, 0]),
           'typeI_fraction': float(np.mean(m['typeI'])),
           'typeI_count': int(np.sum(m['typeI'])),
           'nec_argmin_r': float(R_NODES[i_r]),
           'nec_argmin_point': SET_PTS[i_nec].tolist(),
           'nec_argmin_typeI': bool(m['typeI'][i_nec]),
           'dec_argmin_r': float(R_NODES[j_r]),
           'dec_argmin_point': SET_PTS[i_dec].tolist(),
           'dec_argmin_typeI': bool(m['typeI'][i_dec])}
    if want_aux:
        ti = m['typeI']
        aux = {'That': That, 'm': m,
               'typeI_pts': SET_PTS[ti], 'typeI_nec': m['nec'][ti],
               'nec_argmin_That': That[i_nec], 'nec_argmin_index': i_nec}
        return out, aux
    return out


def floors_ok(centre, member=None, phi=0.0, mode='dwell'):
    b = bundle(centre, FINE_R, member, phi, mode)
    return bool(np.min(b['N']['v']) >= 0.55 and np.min(b['M']['v']) >= 1.0)


def nec_at_point(centre, pt, member=None, phi=0.0, mode='dwell'):
    pt = np.asarray(pt, dtype=DT)
    T, g = T_at(centre, pt[None, :], member, phi, mode)
    That = eulerian_that(g, T)
    m = margins(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


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
        nec, is_ti, _ = nec_at_point(centre, pt, member, phi, mode)
        return nec if is_ti else nec + 1.0

    order = np.argsort(nec_ti)[:5]
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
        nec, is_ti, _ = nec_at_point(centre, pt, member, phi, mode)
        polished.append({'start_set_nec': float(nec_ti[i]),
                         'polished_point': pt.tolist(),
                         'polished_r': float(rr),
                         'polished_nec': nec, 'polished_typeI': bool(is_ti)})
    cand = [p for p in polished if p['polished_typeI']]
    if cand:
        best = min(cand, key=lambda p: p['polished_nec'])
        site = np.array(best['polished_point'], dtype=DT)
        source = 'polished'
    else:
        site = pts_ti[int(order[0])]; best = None
        source = 'set_argmin_fallback'
    nec_site, is_ti, That_site = nec_at_point(centre, site, member, phi, mode)
    return {'source': source, 'point': site.tolist(),
            'r': float(np.linalg.norm(site)), 'typeI': bool(is_ti),
            'worst_nec': nec_site, 'rho_t': float(That_site[0, 0]),
            'polished': polished, 'best_polished': best}


def worst_null(That):
    def q(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)
    vals = np.array([q(d) for d in DIRS642])
    nb = DIRS642[int(np.argmin(vals))]
    x0 = np.array([np.arccos(np.clip(nb[2], -1, 1)), np.arctan2(nb[1], nb[0])])

    def obj(x):
        th, ph = x
        return q(np.array([np.sin(th) * np.cos(ph),
                           np.sin(th) * np.sin(ph), np.cos(th)]))
    res = minimize(obj, x0, method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10, 'fatol': 1e-14})
    return float(obj(res.x)), float(np.min(vals))


# ------------------------------------------------------------- FD path (4D)
def metric_txyz(centre, member, txyz, mode='dwell'):
    txyz = np.asarray(txyz, dtype=DT)
    t = txyz[:, 0]; xyz = txyz[:, 1:]
    r = np.linalg.norm(xyz, axis=1)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, xyz / rsafe[:, None], 0.0)
    Om = member['Om']
    Sv = np.zeros(len(txyz)); Nv = np.zeros(len(txyz)); Mv = np.zeros(len(txyz))
    for tv in np.unique(t):
        sel = t == tv
        b = bundle(centre, r[sel], member, Om * tv, mode)
        Sv[sel] = b['S']['v']; Nv[sel] = b['N']['v']; Mv[sel] = b['M']['v']
    g = np.zeros((len(txyz), 4, 4), dtype=DT)
    g[:, 0, 0] = -Nv ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * Sv
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + (Mv - 1.0) * n[:, i] * n[:, j])
    return g


def _fd(func, pts, h, axis):
    o = []
    for k in (-2, -1, 1, 2):
        p = pts.copy(); p[:, axis] += k * h
        o.append(func(p))
    return (o[0] - 8.0 * o[1] + 8.0 * o[2] - o[3]) / (12.0 * h)


def _gamma_fd(func, pts, h):
    g = func(pts)
    ginv = np.linalg.inv(g)
    dg = [_fd(func, pts, h, a) for a in range(4)]
    Gam = np.zeros(pts.shape[:1] + (4, 4, 4), dtype=DT)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.stack([dg[b][..., d, c] + dg[c][..., d, b]
                                 - dg[d][..., b, c] for d in range(4)], axis=-1)
                Gam[..., a, b, c] = 0.5 * np.einsum('...d,...d->...',
                                                   ginv[..., a, :], term)
    return Gam, g, ginv


def einstein_fd(centre, member, pts4, h, mode='dwell'):
    func = lambda p: metric_txyz(centre, member, p, mode)
    Gam, g, ginv = _gamma_fd(func, pts4, h)

    def gshift(axis, k):
        p = pts4.copy(); p[:, axis] += k * h
        return _gamma_fd(func, p, h)[0]

    Ric = np.zeros(pts4.shape[:1] + (4, 4), dtype=DT)
    for e in range(4):
        dGe = (gshift(e, -2) - 8.0 * gshift(e, -1)
               + 8.0 * gshift(e, 1) - gshift(e, 2)) / (12.0 * h)
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
