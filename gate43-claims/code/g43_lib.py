#!/usr/bin/env python3
"""
g43_lib.py -- Gate-43 machinery, built for this gate alone.

Purpose: independent re-judgement of the Phase 389 claim
set (the mixed centre on Phase 379's H2 centre). NO phase
code and NO earlier gate code is imported or reused for
any deciding read. The definitions re-implemented here
are the programme's registered ones, taken from the
records (metric ansatz, SET-244 set, SAMPLER-M margins,
scaling forms, clamp construction); the implementation
is this gate's own:

  * profiles: base shapes (beta-profile shift, plateau
    lapse bump, ramped M) + not-a-knot correction splines
    with constant extension outside [10, 20];
  * tensor: the Einstein tensor is computed by
    FORWARD-MODE SECOND-ORDER AUTOMATIC DIFFERENTIATION
    of the metric in the three Cartesian spatial
    coordinates (jets: value / gradient / Hessian),
    then the textbook Christoffel -> Ricci contraction.
    This is structurally distinct from both the lineage's
    hand-derived derivative formulas and Gate-41's
    radial-jet algebra. T = G / (8 pi), stationary.
  * gamma's VALUE is assembled in the definition's
    association, delta_ij + ((M-1) n_i) n_j (the
    Gate-41 C-8 lesson: the Eulerian triad at degenerate
    tangential eigenvalues is sensitive to this ulp).
  * frames/margins: Eulerian ADM frame (eigh triad);
    Hawking-Ellis eigenvalue margins at Type-I points,
    sampled margins (162 Fibonacci directions x
    velocities linspace(0, 0.95, 6)) at non-Type-I
    points; rho = Eulerian T_00.
  * SET-244 = 41 radial midpoint nodes on [10, 20]
    x 162 Fibonacci directions (6642 points).

float64 throughout. VM only (the laptop is not a gate
instrument, per the charge).
"""
import json
import os

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
from scipy.special import beta as beta_fn, betainc

DTYPE = np.float64
BETA = 1.1
EIGHT_PI = 8.0 * np.pi
R_LO, R_HI = 10.0, 20.0
LAM_S = 0.70
WINNER_A = 0.07439108177516472
M_RAMP = (6.0, 8.5, 20.0)          # m0, r1, r2 (A2's ramp)
BAR_DEPTH = -0.0034
MU_H2 = 1.15

WP = os.environ.get('G43_WP', '/home/hatch/workspace/warp-pilot')


# ------------------------------------------------------------ sampler
def fib_dirs(npts):
    i = np.arange(npts, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


R_NODES = 10.0 + (np.arange(41, dtype=DTYPE) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
DIRS642 = fib_dirs(642)
FINE_R = np.linspace(R_LO, R_HI, 401)


# ------------------------------------------------------------ shapes
def _ss5(x):
    return (6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3,
            30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2,
            120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x)


def _U(r, a, b):
    r = np.asarray(r, dtype=DTYPE)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r)
    Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss5(x)
        U[mid] = v
        Up[mid] = vp / (b - a)
        Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp


def _H(t):
    t = np.asarray(t, dtype=DTYPE)
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


def shape_B_plat(r, c=15.0, W=5.0, e=3.0):
    r = np.asarray(r, dtype=DTYPE)
    r1 = c - W
    r2 = c + W
    Hx, Hpx, Hppx = _H((r - r1) / e)
    Hy, Hpy, Hppy = _H((r2 - r) / e)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return B, Bp, Bpp


def S_ab(r, a=2.0, b=2.0):
    r = np.asarray(r, dtype=DTYPE)
    S = np.ones_like(r)
    Sp = np.zeros_like(r)
    Spp = np.zeros_like(r)
    S = np.where(r >= 20.0, 0.0, S)
    m = (r > 10.0) & (r < 20.0)
    if np.any(m):
        u = (r[m] - 10.0) / 10.0
        B = beta_fn(a + 1.0, b + 1.0)
        S[m] = 1.0 - betainc(a + 1.0, b + 1.0, u)
        f = u ** a * (1.0 - u) ** b
        Sp[m] = -f / (10.0 * B)
        fp = (u ** (a - 1.0) * (1.0 - u) ** (b - 1.0)
              * (a * (1.0 - u) - b * u))
        fp = np.where(np.isfinite(fp), fp, 0.0)
        Spp[m] = -fp / (100.0 * B)
    return S, Sp, Spp


# ------------------------------------------------------------ splines
def knots(K):
    return np.linspace(R_LO, R_HI, K)


def _spline(vals, K):
    return CubicSpline(knots(K), np.asarray(vals, dtype=DTYPE),
                       bc_type='not-a-knot')


def _eval_corr(cs, r):
    """(value, d, d2) of a correction spline at radii r;
    constant extension outside [10, 20]."""
    r = np.asarray(r, dtype=DTYPE)
    rc = np.clip(r, R_LO, R_HI)
    d = cs(rc)
    dp = cs.derivative(1)(rc)
    dpp = cs.derivative(2)(rc)
    out = (r < R_LO) | (r > R_HI)
    if np.any(out):
        dp = np.where(out, 0.0, dp)
        dpp = np.where(out, 0.0, dpp)
    return d, dp, dpp


# ------------------------------------------------------------ stored data
def load_a2_vectors():
    conf = json.load(open(f'{WP}/phase344/results/'
                          'p344_confirmation.json'))
    ent = [e for e in conf['confirmations'] if e['point'] == 'A2'][0]
    return (np.array(ent['vS'], dtype=DTYPE),
            np.array(ent['vN'], dtype=DTYPE),
            np.array(ent['vM'], dtype=DTYPE))


def load_a2_vectors_state():
    st = json.load(open(f'{WP}/phase344/results/p344_state_A2.json'))
    fi = st['final_incumbent']
    return (np.array(fi['vS'], dtype=DTYPE),
            np.array(fi['vN'], dtype=DTYPE),
            np.array(fi['vM'], dtype=DTYPE))


def load_h2_vectors():
    conf = json.load(open(f'{WP}/phase379/results/'
                          'p379_confirmation.json'))
    ent = [e for e in conf['confirmations'] if e['centre'] == 'H2'][0]
    return (np.array(ent['vS'], dtype=DTYPE),
            np.array(ent['vN'], dtype=DTYPE),
            np.array(ent['vM'], dtype=DTYPE))


def load_h2_vectors_state():
    st = json.load(open(f'{WP}/phase379/results/p379_state_H2.json'))
    fi = st['final_incumbent']
    return (np.array(fi['vS'], dtype=DTYPE),
            np.array(fi['vN'], dtype=DTYPE),
            np.array(fi['vM'], dtype=DTYPE))


# ------------------------------------------------------------ profiles
def base_profiles(r):
    r = np.asarray(r, dtype=DTYPE)
    S, Sp, Spp = S_ab(r, 2.0, 2.0)
    S, Sp, Spp = LAM_S * S, LAM_S * Sp, LAM_S * Spp
    B, Bp, Bpp = shape_B_plat(r)
    N = 1.0 + WINNER_A * B
    Np = WINNER_A * Bp
    Npp = WINNER_A * Bpp
    m0, r1, r2 = M_RAMP
    U1, U1p, U1pp = _U(r, r1, r2)
    U2, U2p, U2pp = _U(r, 21.0, 24.0)
    M = 1.0 + m0 * (U1 - U2)
    Mp = m0 * (U1p - U2p)
    Mpp = m0 * (U1pp - U2pp)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


def a2_total_profiles(r):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = base_profiles(r)
    vS, vN, vM = load_a2_vectors()
    dS, dSp, dSpp = _eval_corr(_spline(vS, 33), r)
    dN, dNp, dNpp = _eval_corr(_spline(vN, 33), r)
    dM, dMp, dMpp = _eval_corr(_spline(vM, 33), r)
    return (S + dS, Sp + dSp, Spp + dSpp,
            N + dN, Np + dNp, Npp + dNpp,
            M + dM, Mp + dMp, Mpp + dMpp)


def centre_profiles(mu, r):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = a2_total_profiles(r)
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)


def h2_total_profiles(r, clamp=False):
    """Phase 379's H2 incumbent totals: centre(1.15) plus
    its K = 17 correction splines. clamp=True zeroes the
    first/last knots of all three correction vectors
    (Gate-41's end-clamp construction)."""
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = centre_profiles(MU_H2, r)
    vS, vN, vM = load_h2_vectors()
    if clamp:
        vS = vS.copy(); vN = vN.copy(); vM = vM.copy()
        for v in (vS, vN, vM):
            v[0] = 0.0
            v[-1] = 0.0
    dS, dSp, dSpp = _eval_corr(_spline(vS, 17), r)
    dN, dNp, dNpp = _eval_corr(_spline(vN, 17), r)
    dM, dMp, dMpp = _eval_corr(_spline(vM, 17), r)
    return (S + dS, Sp + dSp, Spp + dSpp,
            N + dN, Np + dNp, Npp + dNpp,
            M + dM, Mp + dMp, Mpp + dMpp)


def mixed_profiles(muS, muN, muM, r, clamp=False):
    """Phase 389's per-profile scaling of the H2 totals:
    S -> muS*S, N -> muN*N, M -> 1 + muM*(M - 1),
    derivatives scaled likewise."""
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = h2_total_profiles(
        r, clamp=clamp)
    return (muS * S, muS * Sp, muS * Spp,
            muN * N, muN * Np, muN * Npp,
            1.0 + muM * (M - 1.0), muM * Mp, muM * Mpp)


# ------------------------------------------------------------ jets (AD)
# A jet is a tuple (v, g, h): v (P,), g (P,3), h (P,3,3),
# the value, spatial gradient and spatial Hessian of a
# scalar field at P points.
def j_const(c, P):
    return (np.full(P, float(c), dtype=DTYPE),
            np.zeros((P, 3), dtype=DTYPE),
            np.zeros((P, 3, 3), dtype=DTYPE))


def j_add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def j_sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def j_scale(a, c):
    return (a[0] * c, a[1] * c, a[2] * c)


def j_mul(a, b):
    v = a[0] * b[0]
    g = a[1] * b[0][:, None] + b[1] * a[0][:, None]
    h = (a[2] * b[0][:, None, None] + b[2] * a[0][:, None, None]
         + a[1][:, :, None] * b[1][:, None, :]
         + a[1][:, None, :] * b[1][:, :, None])
    return (v, g, h)


def j_inv(a):
    v = 1.0 / a[0]
    g = -a[1] * (v ** 2)[:, None]
    h = (2.0 * (a[1][:, :, None] * a[1][:, None, :])
         * (v ** 3)[:, None, None]
         - a[2] * (v ** 2)[:, None, None])
    return (v, g, h)


def j_coord(pts, i):
    P = len(pts)
    g = np.zeros((P, 3), dtype=DTYPE)
    g[:, i] = 1.0
    return (pts[:, i].copy(), g, np.zeros((P, 3, 3), dtype=DTYPE))


def j_r(pts):
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    P = len(pts)
    Pm = np.zeros((P, 3, 3), dtype=DTYPE)
    for a in range(3):
        for b in range(3):
            Pm[:, a, b] = ((1.0 if a == b else 0.0)
                           - n[:, a] * n[:, b])
    return (r, n, Pm / r[:, None, None])


def j_radial(F, Fp, Fpp, r, n):
    """Jet of a radial function from (F, F', F'') at radii
    r with unit vectors n."""
    P = len(r)
    Pm = np.zeros((P, 3, 3), dtype=DTYPE)
    for a in range(3):
        for b in range(3):
            Pm[:, a, b] = ((1.0 if a == b else 0.0)
                           - n[:, a] * n[:, b])
    h = (Fpp[:, None, None] * (n[:, :, None] * n[:, None, :])
         + (Fp / r)[:, None, None] * Pm)
    return (np.asarray(F, dtype=DTYPE), Fp[:, None] * n, h)


# ------------------------------------------------------------ tensor
def einstein_from_profiles(pts, pr, beta=BETA):
    """(T, g) at pts from profile arrays pr = (S, Sp, Spp,
    N, Np, Npp, M, Mp, Mpp) evaluated at r = |pts|, via
    forward-mode AD jets of the metric components."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = [
        np.asarray(x, dtype=DTYPE) for x in pr]
    jS = j_radial(S, Sp, Spp, r, n)
    jN = j_radial(N, Np, Npp, r, n)
    jM = j_radial(M, Mp, Mpp, r, n)
    jr = j_r(pts)
    jinv_r = j_inv(jr)
    jn = [j_mul(j_coord(pts, i), jinv_r) for i in range(3)]
    one = j_const(1.0, P)
    zero = j_const(0.0, P)
    jMm1 = j_sub(jM, one)

    # metric component jets, index order (t, x, y, z)
    gj = [[None] * 4 for _ in range(4)]
    gj[0][0] = j_scale(j_mul(jN, jN), -1.0)
    gj[0][1] = gj[1][0] = j_scale(jS, -beta)
    gj[0][2] = gj[2][0] = zero
    gj[0][3] = gj[3][0] = zero
    for i in range(3):
        for j in range(3):
            prod = j_mul(jMm1, j_mul(jn[i], jn[j]))
            # value in the definition's association:
            # delta_ij + ((M-1) * n_i) * n_j
            dij = 1.0 if i == j else 0.0
            val = dij + ((M - 1.0) * n[:, i]) * n[:, j]
            gj[i + 1][j + 1] = (val, prod[1], prod[2])
    # values, first and second spatial derivatives
    gv = np.zeros((P, 4, 4), dtype=DTYPE)
    dg = np.zeros((P, 3, 4, 4), dtype=DTYPE)      # dg[e] = d_e g
    ddg = np.zeros((P, 3, 3, 4, 4), dtype=DTYPE)  # ddg[e,f] = d_e d_f g
    for a in range(4):
        for b in range(4):
            v, g, h = gj[a][b]
            gv[:, a, b] = v
            dg[:, :, a, b] = g
            ddg[:, :, :, a, b] = h
    ginv = np.linalg.inv(gv)
    # d_e ginv = -ginv (d_e g) ginv   (spatial e only)
    dginv = np.zeros((P, 3, 4, 4), dtype=DTYPE)
    for e in range(3):
        dginv[:, e] = -np.einsum('pab,pbc,pcd->pad',
                                 ginv, dg[:, e], ginv)

    def D1(idx, a, b):
        """d_idx g_ab for a metric derivative index
        idx in 0..3 (0 = time, vanishes)."""
        if idx == 0:
            return np.zeros(P, dtype=DTYPE)
        return dg[:, idx - 1, a, b]

    def D2(e_idx, idx, a, b):
        """d_e d_idx g_ab; e is a spatial coordinate
        0..2, idx a metric index 0..3."""
        if idx == 0:
            return np.zeros(P, dtype=DTYPE)
        return ddg[:, e_idx, idx - 1, a, b]

    # Christoffel values and spatial derivatives
    Gam = np.zeros((P, 4, 4, 4), dtype=DTYPE)        # Gam[a,b,c]
    dGam = np.zeros((P, 3, 4, 4, 4), dtype=DTYPE)    # dGam[e,a,b,c]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                # term_d = d_b g_{dc} + d_c g_{db} - d_d g_{bc}
                term = np.zeros((P, 4), dtype=DTYPE)
                for d in range(4):
                    term[:, d] = (D1(b, d, c) + D1(c, d, b)
                                  - D1(d, b, c))
                Gam[:, a, b, c] = 0.5 * np.einsum(
                    'pd,pd->p', ginv[:, a, :], term)
                for e in range(3):
                    dterm = np.zeros((P, 4), dtype=DTYPE)
                    for d in range(4):
                        dterm[:, d] = (D2(e, b, d, c)
                                       + D2(e, c, d, b)
                                       - D2(e, d, b, c))
                    dGam[:, e, a, b, c] = (
                        0.5 * np.einsum('pd,pd->p',
                                        dginv[:, e, a, :], term)
                        + 0.5 * np.einsum('pd,pd->p',
                                          ginv[:, a, :], dterm))
    Ric = np.zeros((P, 4, 4), dtype=DTYPE)
    for b in range(4):
        for d in range(4):
            val = np.zeros(P, dtype=DTYPE)
            for a in range(4):
                if a > 0:
                    val += dGam[:, a - 1, a, b, d]
                if d > 0:
                    val -= dGam[:, d - 1, a, b, a]
            for a in range(4):
                for e in range(4):
                    val += (Gam[:, a, a, e] * Gam[:, e, b, d]
                            - Gam[:, a, d, e] * Gam[:, e, b, a])
            Ric[:, b, d] = val
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * gv
    return G / EIGHT_PI, gv


def metric_from_profiles(pts, pr, beta=BETA):
    """Metric values only (for the FD cross-path)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    S, _, _, N, _, _, M, _, _ = [np.asarray(x, dtype=DTYPE)
                                 for x in pr]
    g = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -beta * S
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + ((M - 1.0) * n[:, i]) * n[:, j])
    return g


def T_at(muS, muN, muM, pts, beta=BETA, clamp=False):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    pr = mixed_profiles(muS, muN, muM, r, clamp=clamp)
    return einstein_from_profiles(pts, pr, beta)


# ------------------------------------------------------------ frames
def eulerian_that(g, Tcov):
    g = np.asarray(g, dtype=DTYPE)
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...',
                                       beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DTYPE)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = (V[..., :, i]
                             / np.sqrt(lam[..., i])[..., None])
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def _sampled_margins(That):
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
    Np = flat.shape[0]
    dirs = fib_dirs(162)
    vels = np.linspace(0.0, 0.95, 6)
    T00 = flat[:, 0, 0]
    T0i = flat[:, 0, 1:]
    Tij = flat[:, 1:, 1:]
    tr = np.trace(Tij, axis1=1, axis2=2)
    quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
    nec_s = (T00[:, None] + 2.0 * (T0i @ dirs.T) + quad).min(axis=1)
    wm = np.full(Np, np.inf)
    sm = np.full(Np, np.inf)
    dm = np.full(Np, np.inf)
    Mm = flat.copy()
    Mm[:, 0, :] *= -1.0
    trT = -T00 + tr
    for v in vels:
        gam = 1.0 / np.sqrt(1.0 - v * v)
        wec_vals = gam ** 2 * (T00[:, None]
                               + 2.0 * v * (T0i @ dirs.T)
                               + v * v * quad)
        wm = np.minimum(wm, wec_vals.min(axis=1))
        sec_vals = wec_vals - 0.5 * trT[:, None] * gam ** 2 * (v * v - 1.0)
        sm = np.minimum(sm, sec_vals.min(axis=1))
        V = np.zeros((Np, 162, 4), dtype=DTYPE)
        V[:, :, 0] = gam
        V[:, :, 1:] = gam * v * dirs[None, :, :]
        Ups = -np.einsum('nab,nib->nia', Mm, V)
        q = Ups[:, :, 0] ** 2 - np.sum(Ups[:, :, 1:] ** 2, axis=2)
        nrm = 1.0 + np.sum(Ups ** 2, axis=2)
        val = np.where(Ups[:, :, 0] > 0, q / nrm,
                       -np.abs(q) / nrm - 1.0)
        dm = np.minimum(dm, val.min(axis=1))
    return nec_s, wm, sm, dm


def margins(That):
    That = np.asarray(That, dtype=DTYPE)
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
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
    ar = np.arange(Np)
    rho = np.where(typeI, -evals[ar, k_idx].real, np.nan)
    mask = np.ones((Np, 4), dtype=bool)
    mask[ar, k_idx] = False
    ps_all = evals.real[mask].reshape(Np, 3)
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
    bad = np.where(~typeI)[0]
    if bad.size:
        ns, ws, ss, ds = _sampled_margins(flat[bad])
        nec[bad] = ns
        wec[bad] = ws
        sec[bad] = ss
        dec[bad] = ds
    return {'typeI': typeI, 'nec': nec, 'wec': wec, 'sec': sec,
            'dec': dec, 'rho_eig': rho}


def flux_q(That):
    F = That[:, 0, 1:]
    fn = np.linalg.norm(F, axis=1)
    nh = np.where(fn[:, None] > 0,
                  F / np.where(fn == 0, 1.0, fn)[:, None], 0.0)
    Tnn = np.einsum('pi,pij,pj->p', nh, That[:, 1:, 1:], nh)
    denom = That[:, 0, 0] + Tnn
    q = np.where(denom > 0,
                 2.0 * fn / np.where(denom == 0, 1.0, denom), np.nan)
    return q, denom


# ------------------------------------------------------------ reads
def set_read_generic(profiles_at_radii, beta=BETA):
    """SET-244 read for any profiles_at_radii(r) -> pr."""
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec',
                           'q', 'denom', 'rho')}
    typeI_pts, typeI_nec = [], []
    for rr in R_NODES:
        pts = DIRS162 * rr
        pr = profiles_at_radii(np.full(len(pts), rr, dtype=DTYPE))
        T, g = einstein_from_profiles(pts, pr, beta)
        That = eulerian_that(g, T)
        m = margins(That)
        q, denom = flux_q(That)
        rec['typeI'].append(m['typeI'])
        rec['nec'].append(m['nec'])
        rec['wec'].append(m['wec'])
        rec['dec'].append(m['dec'])
        rec['sec'].append(m['sec'])
        rec['q'].append(q)
        rec['denom'].append(denom)
        rec['rho'].append(That[:, 0, 0])
        if np.any(m['typeI']):
            typeI_pts.append(pts[m['typeI']])
            typeI_nec.append(m['nec'][m['typeI']])
    R = {k: np.concatenate(v) for k, v in rec.items()}
    qdef = R['denom'] > 0
    qv = R['q'][qdef]

    def st(arr):
        return {'min': float(np.min(arr)),
                'median': float(np.median(arr)),
                'max': float(np.max(arr))}
    i_nec = int(np.argmin(R['nec']))
    i_dec = int(np.argmin(R['dec']))
    i_r, i_d = divmod(i_nec, 162)
    j_r, j_d = divmod(i_dec, 162)
    out = {
        'set': 'SET-244 (41 radial midpoint nodes x 162 Fibonacci dirs)',
        'sampler': 'SAMPLER-M',
        'n_points': int(len(R['typeI'])),
        'typeI_fraction': float(np.mean(R['typeI'])),
        'typeI_count': int(np.sum(R['typeI'])),
        'nec': st(R['nec']), 'wec': st(R['wec']),
        'dec': st(R['dec']), 'sec': st(R['sec']),
        'rho': st(R['rho']),
        'nec_argmin_point': (DIRS162[i_d] * R_NODES[i_r]).tolist(),
        'nec_argmin_r': float(R_NODES[i_r]),
        'dec_argmin_point': (DIRS162[j_d] * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
        'typeI_nec_min': (float(np.min(np.concatenate(typeI_nec)))
                          if typeI_nec else None),
        'q_median_where_defined': (float(np.median(qv))
                                   if qv.size else None),
        'q_max_where_defined': (float(np.max(qv))
                                if qv.size else None),
        'q_share_gt1_among_defined': (float(np.mean(qv > 1.0))
                                      if qv.size else None),
        'denom_nonpos_share': float(np.mean(~qdef)),
    }
    aux = {'R': R,
           'typeI_pts': (np.vstack(typeI_pts) if typeI_pts
                         else np.zeros((0, 3))),
           'typeI_nec': (np.concatenate(typeI_nec) if typeI_nec
                         else np.zeros(0))}
    return out, aux


def set_read(muS, muN, muM, beta=BETA, clamp=False):
    return set_read_generic(
        lambda r: mixed_profiles(muS, muN, muM, r, clamp=clamp),
        beta)


def nec_at(muS, muN, muM, pt, beta=BETA, clamp=False):
    pt = np.asarray(pt, dtype=DTYPE)
    T, g = T_at(muS, muN, muM, pt[None, :], beta, clamp=clamp)
    That = eulerian_that(g, T)
    m = margins(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def worst_null(That):
    """Exact pointwise worst null direction: fib(642) scan
    + Nelder-Mead polish (the registered definition)."""
    def q_of(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)
    vals = np.array([q_of(d) for d in DIRS642])
    n_best = DIRS642[int(np.argmin(vals))]
    th0 = np.arccos(np.clip(n_best[2], -1, 1))
    ph0 = np.arctan2(n_best[1], n_best[0])

    def obj(x):
        th, ph = x
        n = np.array([np.sin(th) * np.cos(ph),
                      np.sin(th) * np.sin(ph), np.cos(th)])
        return q_of(n)
    res = minimize(obj, np.array([th0, ph0]), method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10,
                            'fatol': 1e-14})
    th, ph = res.x
    n_fin = np.array([np.sin(th) * np.cos(ph),
                      np.sin(th) * np.sin(ph), np.cos(th)])
    return n_fin, float(obj(res.x)), float(np.min(vals))


def adversary_polish(muS, muN, muM, aux, beta=BETA, clamp=False):
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
        nec, is_ti, _ = nec_at(muS, muN, muM, pt, beta, clamp=clamp)
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
        nec, is_ti, _ = nec_at(muS, muN, muM, pt, beta, clamp=clamp)
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
        i0 = int(order[0])
        site_pt = pts_ti[i0]
        best_p = None
        source = 'set_argmin_fallback'
    nec_site, is_ti_site, That_site = nec_at(
        muS, muN, muM, site_pt, beta, clamp=clamp)
    r_site = float(np.linalg.norm(site_pt))
    return {'source': source,
            'point': site_pt.tolist(), 'r': r_site,
            'direction': (site_pt / r_site).tolist(),
            'typeI': bool(is_ti_site),
            'in_region_worst_nec_SAMPLER-M': nec_site,
            'rho_t': float(That_site[0, 0]),
            'polish_starts': starts, 'polished': polished,
            'best_polished': best_p}


# ------------------------------------------------------------ cross-checks
def rho_split_closed(pts, pr, beta=BETA):
    """Closed-form density split (the recorded identity):
    16 pi rho = R + Q_K with R = R1 + R2 (308/312 form)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    C = pts[:, 0] / r
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = [
        np.asarray(x, dtype=DTYPE) for x in pr]
    R1 = (2.0 / r ** 2) * (1.0 - 1.0 / M)
    R2 = 2.0 * Mp / (r * M ** 2)
    R = R1 + R2
    alpha2 = N ** 2 + beta ** 2 * S ** 2 * (1.0 - ((M - 1.0) / M) * C ** 2)
    bracket = (-Sp ** 2 * (1.0 - C ** 2) / (2.0 * M)
               - 4.0 * (M - 1.0) * S * Sp * C ** 2 / (r * M ** 2)
               + 2.0 * (M - 1.0) ** 2 * S ** 2 * C ** 2 / (r ** 2 * M ** 2)
               + 2.0 * (M - 1.0) * Mp * S ** 2 * C ** 2 / (r * M ** 3))
    QK = beta ** 2 / alpha2 * bracket
    return (R + QK) / (16.0 * np.pi)


def einstein_fd(pts, prof_fn, h=0.05, beta=BETA):
    """From-scratch 4-D centred-FD Einstein tensor from the
    metric function alone (profile values only). prof_fn:
    pts -> profile arrays. Stationary: t-derivatives 0."""
    pts = np.asarray(pts, dtype=DTYPE)

    def gfun(P):
        return metric_from_profiles(P, prof_fn(P), beta)

    def fd4(func, axis, hh):
        offs = []
        for k in (-2, -1, 1, 2):
            p = pts.copy()
            p[:, axis] += k * hh
            offs.append(func(p))
        return (offs[0] - 8.0 * offs[1] + 8.0 * offs[2]
                - offs[3]) / (12.0 * hh)

    g = gfun(pts)
    ginv = np.linalg.inv(g)
    dg = [np.zeros_like(g) for _ in range(4)]
    for a in range(3):
        dg[a + 1] = fd4(gfun, a, h)
    Gam = np.zeros(pts.shape[:1] + (4, 4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.zeros(pts.shape[:1] + (4,), dtype=DTYPE)
                for d in range(4):
                    term[..., d] = (dg[b][..., d, c]
                                    + dg[c][..., d, b]
                                    - dg[d][..., b, c])
                Gam[..., a, b, c] = 0.5 * np.einsum(
                    '...d,...d->...', ginv[..., a, :], term)

    def gamma_fun(P):
        gg = gfun(P)
        gi = np.linalg.inv(gg)
        dgl = [np.zeros_like(gg) for _ in range(4)]
        for a in range(3):
            pp = []
            for k in (-2, -1, 1, 2):
                q = P.copy()
                q[:, a] += k * h
                pp.append(gfun(q))
            dgl[a + 1] = (pp[0] - 8.0 * pp[1] + 8.0 * pp[2]
                          - pp[3]) / (12.0 * h)
        Gm = np.zeros(P.shape[:1] + (4, 4, 4), dtype=DTYPE)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    term = np.zeros(P.shape[:1] + (4,), dtype=DTYPE)
                    for d in range(4):
                        term[..., d] = (dgl[b][..., d, c]
                                        + dgl[c][..., d, b]
                                        - dgl[d][..., b, c])
                    Gm[..., a, b, c] = 0.5 * np.einsum(
                        '...d,...d->...', gi[..., a, :], term)
        return Gm

    Ric = np.zeros(pts.shape[:1] + (4, 4), dtype=DTYPE)
    for e in range(1, 4):
        dGe = fd4(gamma_fun, e - 1, h)
        for b_ in range(4):
            for d_ in range(4):
                Ric[..., b_, d_] += dGe[..., e, b_, d_]
                if d_ == e:
                    for a in range(4):
                        Ric[..., b_, d_] -= dGe[..., a, b_, a]
    for b_ in range(4):
        for d_ in range(4):
            val = Ric[..., b_, d_]
            for a in range(4):
                for e in range(4):
                    val += (Gam[..., a, a, e] * Gam[..., e, b_, d_]
                            - Gam[..., a, d_, e] * Gam[..., e, b_, a])
            Ric[..., b_, d_] = val
    Rs = np.einsum('...ab,...ab->...', ginv, Ric)
    G = Ric - 0.5 * Rs[..., None, None] * g
    return G / EIGHT_PI
