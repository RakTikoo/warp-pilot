#!/usr/bin/env python3
"""
g41_lib.py -- Gate-41 machinery, written for this gate alone.

Re-judgement of the Phase 379 claim set (ledger entry 964).
NO Phase 344/359/374/379 (or 316/338/341 lineage) code is
imported or reused for any deciding read. What is taken from
the record is only: the claims, the stored parameter vectors
(p344_confirmation.json A2 entry; p379_confirmation.json
incumbents), and the DEFINITIONS of the family and the read
(metric ansatz, profile shapes, SET-244 sampler, SAMPLER-M
margin definitions), which the gate re-implements here from
those definitions.

Family (A2 lineage, stationary):
    g_tt = -N(r)^2,  g_tX = -beta*S(r)  (shift along x only),
    gamma_ij = delta_ij + (M(r)-1) n_i n_j,   beta = 1.1.
Base point A2: S = lamS * S_{2,2} (lamS = 0.70; S_{a,b} the
regularised-incomplete-beta profile on [10, 20]);
N = 1 + A * B_plat(c=15, W=5, e=3), A = 0.07439108177516472;
M = 1 + 6.0 * [U(r; 8.5, 20.0) - U(r; 21, 24)] (U the quintic
smoothstep ramp). A2's totals add its confirmed K = 33
not-a-knot spline corrections (dS, dN, dM), constant-extended
outside [10, 20] with zero derivatives there.
Centre(mu): S -> mu*S, N -> mu*N, M -> 1 + mu*(M-1),
derivatives scaled by mu likewise, applied to A2's TOTALS.
Member(centre, K): centre + additive K-knot not-a-knot
spline corrections.

Tensor: the Einstein tensor is built here by a jet (value /
gradient / Hessian) algebra over the spatial coordinates,
implemented from the chain rule in this file, then the
textbook Christoffel -> Ricci contraction. T = G / (8 pi).
Cross-checks (separate drivers): a 4-D finite-difference
Einstein tensor from the metric function alone, and the
recorded closed-form density split 16 pi rho = R + Q_K.

Reads: SET-244 = 41 radial midpoint nodes on [10, 20] x 162
Fibonacci directions; SAMPLER-M margins = Hawking-Ellis
eigenvalue margins at Type-I points, sampled margins
(162 directions x velocities linspace(0, 0.95, 6)) at
non-Type-I points; rho = Eulerian-frame T_00.
float64 throughout.
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

WP = os.environ.get('G41_WP', '/home/hatch/workspace/warp-pilot')


# ------------------------------------------------------------ sampler
def fib_dirs(npts):
    """Fibonacci sphere directions (the SET-244 definition)."""
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
    """Quintic smoothstep 6x^5-15x^4+10x^3 and derivatives."""
    return (6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3,
            30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2,
            120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x)


def _U(r, a, b):
    """(U, U', U'') of the ramp: 0 below a, 1 above b,
    quintic smoothstep between."""
    r = np.asarray(r, dtype=DTYPE)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r); Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss5(x)
        U[mid] = v; Up[mid] = vp / (b - a); Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp


def _H(t):
    """Quintic H = 10t^3 - 15t^4 + 6t^5 on (0,1), 0/1 outside,
    with first two derivatives."""
    t = np.asarray(t, dtype=DTYPE)
    v = np.where(t >= 1.0, 1.0, 0.0)
    vp = np.zeros_like(t); vpp = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    if np.any(m):
        tm = t[m]
        v[m] = 10.0 * tm ** 3 - 15.0 * tm ** 4 + 6.0 * tm ** 5
        vp[m] = 30.0 * tm ** 2 * (1.0 - tm) ** 2
        vpp[m] = 60.0 * tm * (1.0 - tm) * (1.0 - 2.0 * tm)
    return v, vp, vpp


def shape_B_plat(r, c=15.0, W=5.0, e=3.0):
    """Plateau bump B = H((r-r1)/e) * H((r2-r)/e),
    r1 = c-W, r2 = c+W, and derivatives."""
    r = np.asarray(r, dtype=DTYPE)
    r1 = c - W; r2 = c + W
    Hx, Hpx, Hppx = _H((r - r1) / e)
    Hy, Hpy, Hppy = _H((r2 - r) / e)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return B, Bp, Bpp


def S_ab(r, a=2.0, b=2.0):
    """S_{a,b} = 1 - I_u(a+1, b+1), u = (r-10)/10 on [10, 20];
    1 below, 0 above; derivatives from the beta density."""
    r = np.asarray(r, dtype=DTYPE)
    S = np.ones_like(r); Sp = np.zeros_like(r); Spp = np.zeros_like(r)
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


def _eval_corr(cs, r):
    """Correction spline (value, d, d2) at radii r; constant
    extension outside [10, 20] (end value, zero derivatives)."""
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


def _spline(vals, K):
    return CubicSpline(knots(K), np.asarray(vals, dtype=DTYPE),
                       bc_type='not-a-knot')


# ------------------------------------------------------------ profiles
def base_profiles(r):
    """The A2 base point (no corrections) at radii r:
    (S, Sp, Spp, N, Np, Npp, M, Mp, Mpp)."""
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
    """A2's total profiles (base + confirmed K = 33
    corrections) at radii r."""
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = base_profiles(r)
    vS, vN, vM = load_a2_vectors()
    dS, dSp, dSpp = _eval_corr(_spline(vS, 33), r)
    dN, dNp, dNpp = _eval_corr(_spline(vN, 33), r)
    dM, dMp, dMpp = _eval_corr(_spline(vM, 33), r)
    return (S + dS, Sp + dSp, Spp + dSpp,
            N + dN, Np + dNp, Npp + dNpp,
            M + dM, Mp + dMp, Mpp + dMpp)


def centre_profiles(mu, r):
    """The harvested centre: A2's totals mu-scaled."""
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = a2_total_profiles(r)
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)


def member_profiles(mu, vS, vN, vM, K, r):
    """centre(mu) + additive K-knot correction splines at
    radii r. A None sector adds nothing."""
    return profiles_radial(mu, vS, vN, vM, K, r)


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


def load_379_incumbent(centre):
    conf = json.load(open(f'{WP}/phase379/results/'
                          'p379_confirmation.json'))
    ent = [e for e in conf['confirmations']
           if e['centre'] == centre][0]
    return ent


def mu_of(a, m):
    """374's dwell-bottom expression at w = -1.0 (the
    registered centre definition)."""
    w = -1.0
    return 1.0 + a * (m + (1.0 - m) * w)


MU_H1 = mu_of(0.15, 0.875)         # 1.1125
MU_H2 = mu_of(0.30, 0.75)          # 1.15


# ------------------------------------------------------------ jets
# A jet is (v, g, H): value (P,), spatial gradient (P,3),
# spatial Hessian (P,3,3), for a scalar field of (x,y,z).
def jet_const(c, P):
    return (np.full(P, c, dtype=DTYPE),
            np.zeros((P, 3), dtype=DTYPE),
            np.zeros((P, 3, 3), dtype=DTYPE))


def jet_radial(F, Fp, Fpp, r, n):
    """Jet of a radial function F(r) given value/derivative
    arrays at the points. d_i F = F' n_i;
    d_i d_j F = F'' n_i n_j + (F'/r)(delta_ij - n_i n_j)."""
    P = len(r)
    rs = np.where(r > 0, r, 1.0)
    g = Fp[:, None] * n
    nn = n[:, :, None] * n[:, None, :]
    eye = np.eye(3)[None, :, :]
    H = (Fpp[:, None, None] * nn
         + (Fp / rs)[:, None, None] * (eye - nn))
    return (np.array(F, dtype=DTYPE), g, H)


def jet_n(i, r, n):
    """Jet of the direction component n_i = x_i / r.
    d_k n_i = (delta_ki - n_k n_i)/r;
    d_l d_k n_i = -(1/r^2)[ n_l delta_ki + n_k delta_li
                            + delta_lk n_i - 3 n_l n_k n_i ]."""
    P = len(r)
    rs = np.where(r > 0, r, 1.0)
    v = n[:, i].copy()
    g = np.zeros((P, 3), dtype=DTYPE)
    H = np.zeros((P, 3, 3), dtype=DTYPE)
    for k in range(3):
        dki = 1.0 if k == i else 0.0
        g[:, k] = (dki - n[:, k] * n[:, i]) / rs
        for l in range(3):
            dli = 1.0 if l == i else 0.0
            dlk = 1.0 if l == k else 0.0
            H[:, l, k] = -(n[:, l] * dki + n[:, k] * dli
                           + dlk * n[:, i]
                           - 3.0 * n[:, l] * n[:, k] * n[:, i]
                           ) / rs ** 2
    return (v, g, H)


def jet_add(A, B):
    return (A[0] + B[0], A[1] + B[1], A[2] + B[2])


def jet_scale(A, c):
    return (c * A[0], c * A[1], c * A[2])


def jet_mul(A, B):
    v = A[0] * B[0]
    g = A[1] * B[0][:, None] + B[1] * A[0][:, None]
    H = (A[2] * B[0][:, None, None] + B[2] * A[0][:, None, None]
         + A[1][:, :, None] * B[1][:, None, :]
         + B[1][:, :, None] * A[1][:, None, :])
    return (v, g, H)


# ------------------------------------------------------------ tensor
def einstein_from_profiles(pts, pr, beta=BETA):
    """Einstein tensor / (8 pi) and the metric at pts, from
    profile arrays pr = (S, Sp, Spp, N, Np, Npp, M, Mp, Mpp).
    Metric jets are assembled componentwise; Christoffel and
    Ricci follow the textbook formulas. Stationary: all
    t-derivatives vanish."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    rs = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rs[:, None], 0.0)
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = pr

    jS = jet_radial(S, Sp, Spp, r, n)
    jN = jet_radial(N, Np, Npp, r, n)
    jM = jet_radial(M, Mp, Mpp, r, n)
    jh = (jM[0] - 1.0, jM[1], jM[2])                    # h = M - 1
    jn = [jet_n(i, r, n) for i in range(3)]

    # metric component jets, indices 0..3 (0 = t)
    GJ = [[None] * 4 for _ in range(4)]
    GJ[0][0] = jet_scale(jet_mul(jN, jN), -1.0)
    GJ[0][1] = jet_scale(jS, -beta)
    GJ[1][0] = GJ[0][1]
    for a in (2, 3):
        GJ[0][a] = jet_const(0.0, P)
        GJ[a][0] = GJ[0][a]
    for i in range(3):
        for j in range(3):
            base = jet_const(1.0 if i == j else 0.0, P)
            GJ[i + 1][j + 1] = jet_add(
                base, jet_mul(jh, jet_mul(jn[i], jn[j])))

    g = np.zeros((P, 4, 4), dtype=DTYPE)
    dg = np.zeros((P, 4, 4, 4), dtype=DTYPE)      # dg[:,mu,a,b]
    ddg = np.zeros((P, 4, 4, 4, 4), dtype=DTYPE)  # ddg[:,mu,nu,a,b]
    for a in range(4):
        for b in range(4):
            v, gr, H = GJ[a][b]
            g[:, a, b] = v
            dg[:, 1:, a, b] = gr        # dg[:, k+1] = d_k = gr[:, k]
            ddg[:, 1:, 1:, a, b] = H    # ddg[:, l+1, k+1] = H[:, l, k]
    # The spatial block's VALUE is assembled directly as
    # delta_ij + ((M-1) * n_i) * n_j: the Eulerian frame is
    # taken from eigh(gamma), whose basis inside gamma's
    # degenerate tangential eigenspace is fixed by gamma's
    # exact floating-point entries, so the block is written
    # in this (the definition's) association rather than
    # through the jet product. (Calibration C-4 records the
    # effect: with the jet-product association the sampled
    # margins at isolated non-Type-I points move by ~1e-6.)
    h = M - 1.0
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + (h * n[:, i]) * n[:, j])
    ginv = np.linalg.inv(g)

    # Christoffel Gamma^a_bc = 1/2 g^ad (d_b g_dc + d_c g_db - d_d g_bc)
    Gam = 0.5 * (np.einsum('pad,pbdc->pabc', ginv, dg)
                 + np.einsum('pad,pcdb->pabc', ginv, dg)
                 - np.einsum('pad,pdbc->pabc', ginv, dg))
    # d_e Gamma^a_bc
    dginv = -np.einsum('pam,pemn,pnb->peab', ginv, dg, ginv)
    dGam = 0.5 * (np.einsum('pead,pbdc->peabc', dginv, dg)
                  + np.einsum('pead,pcdb->peabc', dginv, dg)
                  - np.einsum('pead,pdbc->peabc', dginv, dg)
                  + np.einsum('pad,pebdc->peabc', ginv, ddg)
                  + np.einsum('pad,pecdb->peabc', ginv, ddg)
                  - np.einsum('pad,pedbc->peabc', ginv, ddg))
    # Ricci R_bd = d_a Gam^a_bd - d_d Gam^a_ba
    #              + Gam^a_ae Gam^e_bd - Gam^a_de Gam^e_ba
    Ric = (np.einsum('paabd->pbd', dGam)
           - np.einsum('pdaba->pbd', dGam)
           + np.einsum('paae,pebd->pbd', Gam, Gam)
           - np.einsum('pade,peba->pbd', Gam, Gam))
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g
    return G / EIGHT_PI, g


def metric_from_profiles(pts, pr, beta=BETA):
    """Metric only (for the FD cross-check path)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    rs = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rs[:, None], 0.0)
    S, _, _, N, _, _, M, _, _ = pr
    g = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -beta * S
    h = M - 1.0
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + h * n[:, i] * n[:, j])
    return g


def profiles_radial(mu, vS, vN, vM, K, r):
    """Profile arrays as functions of radius alone:
    centre(mu) + the K-knot correction splines."""
    r = np.asarray(r, dtype=DTYPE)
    pr = list(centre_profiles(mu, r))
    vecs = (vS, vN, vM)
    for sec in range(3):
        if vecs[sec] is not None:
            d, dp, dpp = _eval_corr(_spline(vecs[sec], K), r)
            pr[3 * sec] += d
            pr[3 * sec + 1] += dp
            pr[3 * sec + 2] += dpp
    return tuple(pr)


def T_at(mu, vS, vN, vM, K, pts, beta=BETA):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    pr = profiles_radial(mu, vS, vN, vM, K, r)
    return einstein_from_profiles(pts, pr, beta)


# ------------------------------------------------------------ frames/margins
def eulerian_that(g, Tcov):
    """Eulerian orthonormal frame of the ADM decomposition
    of g (the SAMPLER-M frame definition): e_0 = (1/alpha,
    -beta^i/alpha), spatial triad from eigh(gamma)."""
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
    """Sampled margins at non-Type-I points (the SAMPLER-M
    definition): null contractions over 162 Fibonacci
    directions; timelike contractions over velocities
    linspace(0, 0.95, 6); DEC via the normalised
    future-causality margin of Upsilon = -T^a_b V^b."""
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
    Np = flat.shape[0]
    dirs = fib_dirs(162)
    vels = np.linspace(0.0, 0.95, 6)
    T00 = flat[:, 0, 0]; T0i = flat[:, 0, 1:]; Tij = flat[:, 1:, 1:]
    tr = np.trace(Tij, axis1=1, axis2=2)
    quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
    nec_s = (T00[:, None] + 2.0 * (T0i @ dirs.T) + quad).min(axis=1)
    wm = np.full(Np, np.inf); sm = np.full(Np, np.inf)
    dm = np.full(Np, np.inf)
    Mm = flat.copy(); Mm[:, 0, :] *= -1.0
    trT = -T00 + tr
    for v in vels:
        gam = 1.0 / np.sqrt(1.0 - v * v)
        wec_vals = gam ** 2 * (T00[:, None] + 2.0 * v * (T0i @ dirs.T)
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
    """Hawking-Ellis margins: eigenvalue margins at Type-I
    points, sampled margins at non-Type-I points."""
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
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
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
        nec[bad] = ns; wec[bad] = ws; sec[bad] = ss; dec[bad] = ds
    return {'typeI': typeI, 'nec': nec, 'wec': wec, 'sec': sec,
            'dec': dec, 'rho_eig': rho}


# ------------------------------------------------------------ SET read
def set_read(mu, vS, vN, vM, K, beta=BETA):
    """SET-244 read of one member. Returns (summary, aux)."""
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec', 'rho')}
    typeI_pts, typeI_nec = [], []
    for rr in R_NODES:
        pts = DIRS162 * rr
        T, g = T_at(mu, vS, vN, vM, K, pts, beta)
        That = eulerian_that(g, T)
        m = margins(That)
        rec['typeI'].append(m['typeI']); rec['nec'].append(m['nec'])
        rec['wec'].append(m['wec']); rec['dec'].append(m['dec'])
        rec['sec'].append(m['sec']); rec['rho'].append(That[:, 0, 0])
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
    }
    aux = {'R': R,
           'typeI_pts': (np.vstack(typeI_pts) if typeI_pts
                         else np.zeros((0, 3))),
           'typeI_nec': (np.concatenate(typeI_nec) if typeI_nec
                         else np.zeros(0))}
    return out, aux


def nec_at(mu, vS, vN, vM, K, pt, beta=BETA):
    """One-point NEC read + Type-I flag + That."""
    pt = np.asarray(pt, dtype=DTYPE)
    T, g = T_at(mu, vS, vN, vM, K, pt[None, :], beta)
    That = eulerian_that(g, T)
    m = margins(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def worst_null(That):
    """Exact pointwise worst null direction: fib-642 scan +
    Nelder-Mead polish of k^T That k, k = (1, n). Returns
    (polished value, fib-scan value)."""
    def q_of(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)
    vals = np.array([q_of(d) for d in DIRS642])
    n_best = DIRS642[int(np.argmin(vals))]
    th0 = np.arccos(np.clip(n_best[2], -1, 1))
    ph0 = np.arctan2(n_best[1], n_best[0])

    def obj(x):
        th, ph = x
        nn = np.array([np.sin(th) * np.cos(ph),
                       np.sin(th) * np.sin(ph), np.cos(th)])
        return q_of(nn)
    res = minimize(obj, np.array([th0, ph0]), method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10,
                            'fatol': 1e-14})
    return float(obj(res.x)), float(np.min(vals))


def adversary_polish(mu, vS, vN, vM, K, aux, beta=BETA):
    """The target-site polish protocol: the five lowest-NEC
    Type-I SET points are Nelder-Mead polished in (r, th, ph);
    the depth is the best polished Type-I NEC (fallback: the
    SET argmin point)."""
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
        nec, is_ti, _ = nec_at(mu, vS, vN, vM, K, pt, beta)
        return nec if is_ti else nec + 1.0

    order = np.argsort(nec_ti)[:5]
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
        nec, is_ti, _ = nec_at(mu, vS, vN, vM, K, pt, beta)
        polished.append({'start_set_nec': float(nec_ti[i]),
                         'polished_point': pt.tolist(),
                         'polished_r': float(rr),
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
        mu, vS, vN, vM, K, site_pt, beta)
    r_site = float(np.linalg.norm(site_pt))
    return {'source': source,
            'point': site_pt.tolist(), 'r': r_site,
            'typeI': bool(is_ti_site),
            'in_region_worst_nec_SAMPLER-M': nec_site,
            'rho_t': float(That_site[0, 0]),
            'polished': polished, 'best_polished': best_p}


# ------------------------------------------------------------ cross-checks
def rho_split_closed(pts, pr, beta=BETA):
    """The recorded closed-form density split (Phase 308
    formula, as recorded in the programme's anatomy):
        16 pi rho = R + Q_K,
        R = (2/r^2)(1 - 1/M) + 2 M'/(r M^2),
        Q_K = (beta^2/alpha^2)[ -S'^2 (1-C^2)/(2M)
              - 4(M-1) S S' C^2/(r M^2)
              + 2(M-1)^2 S^2 C^2/(r^2 M^2)
              + 2(M-1) M' S^2 C^2/(r M^3) ],
        alpha^2 = N^2 + beta^2 S^2 (1 - ((M-1)/M) C^2),
        C = n_xhat.
    An identity check on the tensor's Eulerian density."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    C = pts[:, 0] / r
    S, Sp, _, N, _, _, M, Mp, _ = pr
    R = (2.0 / r ** 2) * (1.0 - 1.0 / M) + 2.0 * Mp / (r * M ** 2)
    alpha2 = N ** 2 + beta ** 2 * S ** 2 * (1.0 - ((M - 1.0) / M) * C ** 2)
    bracket = (-Sp ** 2 * (1.0 - C ** 2) / (2.0 * M)
               - 4.0 * (M - 1.0) * S * Sp * C ** 2 / (r * M ** 2)
               + 2.0 * (M - 1.0) ** 2 * S ** 2 * C ** 2
               / (r ** 2 * M ** 2)
               + 2.0 * (M - 1.0) * Mp * S ** 2 * C ** 2
               / (r * M ** 3))
    QK = beta ** 2 / alpha2 * bracket
    return (R + QK) / (16.0 * np.pi)


def einstein_fd(pts, prof_fn, h=0.05, beta=BETA):
    """Independent path: 4-D centred finite differences of the
    metric function alone -> Christoffel -> dChristoffel ->
    Ricci -> Einstein/(8 pi). prof_fn(x4) returns g (4,4) at a
    spacetime point x4 = (t, x, y, z); the metric is
    t-independent, so t-differences are exact zeros."""
    pts = np.asarray(pts, dtype=DTYPE)
    out = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    for ip, p in enumerate(pts):
        x0 = np.concatenate([[0.0], p])

        def G(x4):
            return prof_fn(x4)
        g0 = G(x0)
        dg = np.zeros((4, 4, 4)); ddg = np.zeros((4, 4, 4, 4))
        for mu in range(4):
            e = np.zeros(4); e[mu] = h
            gp = G(x0 + e); gm = G(x0 - e)
            dg[mu] = (gp - gm) / (2.0 * h)
            ddg[mu, mu] = (gp - 2.0 * g0 + gm) / h ** 2
            for nu in range(mu + 1, 4):
                f = np.zeros(4); f[nu] = h
                gpp = G(x0 + e + f); gpm = G(x0 + e - f)
                gmp = G(x0 - e + f); gmm = G(x0 - e - f)
                ddg[mu, nu] = (gpp - gpm - gmp + gmm) / (4.0 * h ** 2)
                ddg[nu, mu] = ddg[mu, nu]
        ginv = np.linalg.inv(g0)
        Gam = np.zeros((4, 4, 4))
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    Gam[a, b, c] = 0.5 * sum(
                        ginv[a, d] * (dg[b, d, c] + dg[c, d, b]
                                      - dg[d, b, c])
                        for d in range(4))
        dGam = np.zeros((4, 4, 4, 4))
        dginv = np.zeros((4, 4, 4))
        for e in range(4):
            dginv[e] = -ginv @ dg[e] @ ginv
            for a in range(4):
                for b in range(4):
                    for c in range(4):
                        dGam[e, a, b, c] = 0.5 * sum(
                            dginv[e, a, d] * (dg[b, d, c] + dg[c, d, b]
                                              - dg[d, b, c])
                            + ginv[a, d] * (ddg[e, b, d, c]
                                            + ddg[e, c, d, b]
                                            - ddg[e, d, b, c])
                            for d in range(4))
        Ric = np.zeros((4, 4))
        for b in range(4):
            for d in range(4):
                val = sum(dGam[a, a, b, d] - dGam[d, a, b, a]
                          for a in range(4))
                for a in range(4):
                    for e in range(4):
                        val += (Gam[a, a, e] * Gam[e, b, d]
                                - Gam[a, d, e] * Gam[e, b, a])
                Ric[b, d] = val
        Rs = float(np.einsum('ab,ab', ginv, Ric))
        out[ip] = (Ric - 0.5 * Rs * g0) / EIGHT_PI
    return out
