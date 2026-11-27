#!/usr/bin/env python3
"""
g45_lib.py -- Gate-45 machinery, written for this gate alone.

Independent re-judgement of the Phase 394 claim set (the
scaling centre seeded at Phase 393's ray point, on Phase
379's H2 totals). No phase code and no earlier gate code is
imported or reused for any deciding read. The registered
definitions are re-implemented here from the records:

  * profiles: beta-profile shift, plateau lapse bump,
    ramped M, plus not-a-knot correction splines with
    constant extension outside [10, 20]; H2 = centre(1.15)
    of the A2 totals + K = 17 corrections; per-profile
    scaling S -> muS*S, N -> muN*N, M -> 1 + muM*(M - 1);
    the end-clamp zeroes the first/last knots of H2's
    three correction vectors before scaling.
  * tensor: forward-mode second-order AD jets of the
    metric in Cartesian spatial coordinates, with the
    Christoffel and Ricci contractions carried out by
    whole-array einsum algebra (a different contraction
    organisation from both the lineage's hand-derived
    radial formulas and Gate-43's loop contractions).
    T = G / (8 pi), stationary.
  * gamma's value is assembled in the definition's
    association, delta_ij + ((M-1) n_i) n_j (the Gate-41
    C-8 / Gate-43 C-10 lesson).
  * frames/margins: Eulerian ADM frame (eigh triad);
    Hawking-Ellis eigenvalue margins at Type-I points,
    SAMPLER-M sampled margins (162 Fibonacci directions x
    velocities linspace(0, 0.95, 6)) at non-Type-I points;
    rho = Eulerian T_00.
  * SET-244 = 41 radial midpoint nodes on [10, 20]
    x 162 Fibonacci directions (6642 points).

float64 throughout. VM only.
"""
import json
import os

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
from scipy.special import beta as beta_fn, betainc

DT = np.float64
BETA = 1.1
EIGHT_PI = 8.0 * np.pi
R_LO, R_HI = 10.0, 20.0
LAM_S = 0.70
WINNER_A = 0.07439108177516472
M_RAMP = (6.0, 8.5, 20.0)
MU_H2 = 1.15

WP = os.environ.get('G45_WP', '/home/hatch/workspace/warp-pilot')


# ------------------------------------------------------------- sampler
def fib_dirs(npts):
    i = np.arange(npts, dtype=DT)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


R_NODES = 10.0 + (np.arange(41, dtype=DT) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
DIRS642 = fib_dirs(642)


# ------------------------------------------------------------- shapes
def _ss5(x):
    return (6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3,
            30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2,
            120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x)


def _U(r, a, b):
    r = np.asarray(r, dtype=DT)
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


def shape_B_plat(r, c=15.0, W=5.0, e=3.0):
    r = np.asarray(r, dtype=DT)
    r1 = c - W
    r2 = c + W
    Hx, Hpx, Hppx = _H((r - r1) / e)
    Hy, Hpy, Hppy = _H((r2 - r) / e)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return B, Bp, Bpp


def S_ab(r, a=2.0, b=2.0):
    r = np.asarray(r, dtype=DT)
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


# ------------------------------------------------------------- splines
def knots(K):
    return np.linspace(R_LO, R_HI, K)


def _spline(vals, K):
    return CubicSpline(knots(K), np.asarray(vals, dtype=DT),
                       bc_type='not-a-knot')


def _eval_corr(cs, r):
    r = np.asarray(r, dtype=DT)
    rc = np.clip(r, R_LO, R_HI)
    d = cs(rc)
    dp = cs.derivative(1)(rc)
    dpp = cs.derivative(2)(rc)
    out = (r < R_LO) | (r > R_HI)
    if np.any(out):
        dp = np.where(out, 0.0, dp)
        dpp = np.where(out, 0.0, dpp)
    return d, dp, dpp


# ------------------------------------------------------------- stored data
def _vecs_from_conf(path, key, val):
    conf = json.load(open(path))
    ent = [e for e in conf['confirmations'] if e[key] == val][0]
    return (np.array(ent['vS'], dtype=DT),
            np.array(ent['vN'], dtype=DT),
            np.array(ent['vM'], dtype=DT))


def _vecs_from_state(path):
    st = json.load(open(path))
    fi = st['final_incumbent']
    return (np.array(fi['vS'], dtype=DT),
            np.array(fi['vN'], dtype=DT),
            np.array(fi['vM'], dtype=DT))


def load_a2_vectors():
    return _vecs_from_conf(f'{WP}/phase344/results/'
                           'p344_confirmation.json', 'point', 'A2')


def load_a2_vectors_state():
    return _vecs_from_state(f'{WP}/phase344/results/p344_state_A2.json')


def load_h2_vectors():
    return _vecs_from_conf(f'{WP}/phase379/results/'
                           'p379_confirmation.json', 'centre', 'H2')


def load_h2_vectors_state():
    return _vecs_from_state(f'{WP}/phase379/results/p379_state_H2.json')


# ------------------------------------------------------------- profiles
def base_profiles(r):
    r = np.asarray(r, dtype=DT)
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


def scaled_profiles(muS, muN, muM, r, clamp=False):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = h2_total_profiles(
        r, clamp=clamp)
    return (muS * S, muS * Sp, muS * Spp,
            muN * N, muN * Np, muN * Npp,
            1.0 + muM * (M - 1.0), muM * Mp, muM * Mpp)


# ------------------------------------------------------------- jets (AD)
# A jet is a tuple (v, g, h): v (P,), g (P,3), h (P,3,3) -- the
# value, spatial gradient and spatial Hessian of a scalar field.
def j_const(c, P):
    return (np.full(P, float(c), dtype=DT),
            np.zeros((P, 3), dtype=DT),
            np.zeros((P, 3, 3), dtype=DT))


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
    g = np.zeros((P, 3), dtype=DT)
    g[:, i] = 1.0
    return (pts[:, i].copy(), g, np.zeros((P, 3, 3), dtype=DT))


def j_r(pts):
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    P = len(pts)
    Pm = np.zeros((P, 3, 3), dtype=DT)
    for a in range(3):
        for b in range(3):
            Pm[:, a, b] = ((1.0 if a == b else 0.0)
                           - n[:, a] * n[:, b])
    return (r, n, Pm / r[:, None, None])


def j_radial(F, Fp, Fpp, r, n):
    P = len(r)
    Pm = np.zeros((P, 3, 3), dtype=DT)
    for a in range(3):
        for b in range(3):
            Pm[:, a, b] = ((1.0 if a == b else 0.0)
                           - n[:, a] * n[:, b])
    h = (Fpp[:, None, None] * (n[:, :, None] * n[:, None, :])
         + (Fp / r)[:, None, None] * Pm)
    return (np.asarray(F, dtype=DT), Fp[:, None] * n, h)


# ------------------------------------------------------------- tensor
def einstein_from_profiles(pts, pr, beta=BETA):
    """(T, g) at pts from profile arrays, via AD jets of the
    metric; Christoffel/Ricci contractions by whole-array
    einsum algebra over the batch."""
    pts = np.asarray(pts, dtype=DT)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = [
        np.asarray(x, dtype=DT) for x in pr]
    jS = j_radial(S, Sp, Spp, r, n)
    jN = j_radial(N, Np, Npp, r, n)
    jM = j_radial(M, Mp, Mpp, r, n)
    jr = j_r(pts)
    jinv_r = j_inv(jr)
    jn = [j_mul(j_coord(pts, i), jinv_r) for i in range(3)]
    one = j_const(1.0, P)
    zero = j_const(0.0, P)
    jMm1 = j_sub(jM, one)

    gj = [[None] * 4 for _ in range(4)]
    gj[0][0] = j_scale(j_mul(jN, jN), -1.0)
    gj[0][1] = gj[1][0] = j_scale(jS, -beta)
    gj[0][2] = gj[2][0] = zero
    gj[0][3] = gj[3][0] = zero
    for i in range(3):
        for j in range(3):
            prod = j_mul(jMm1, j_mul(jn[i], jn[j]))
            dij = 1.0 if i == j else 0.0
            val = dij + ((M - 1.0) * n[:, i]) * n[:, j]
            gj[i + 1][j + 1] = (val, prod[1], prod[2])
    gv = np.zeros((P, 4, 4), dtype=DT)
    dg = np.zeros((P, 3, 4, 4), dtype=DT)        # dg[e] = d_e g
    ddg = np.zeros((P, 3, 3, 4, 4), dtype=DT)    # ddg[e, f]
    for a in range(4):
        for b in range(4):
            v, g, h = gj[a][b]
            gv[:, a, b] = v
            dg[:, :, a, b] = g
            ddg[:, :, :, a, b] = h
    ginv = np.linalg.inv(gv)
    # D[p, idx, a, b] = d_idx g_ab, idx 0..3 (0 = time, zero);
    # DD[p, e, idx, a, b] = d_e d_idx g_ab.
    D = np.concatenate([np.zeros((P, 1, 4, 4), dtype=DT), dg],
                       axis=1)
    DD = np.concatenate(
        [np.zeros((P, 3, 1, 4, 4), dtype=DT), ddg], axis=2)
    dginv = -np.einsum('pab,pebc,pcd->pead', ginv, dg, ginv)
    # term[p, d, b, c] = D_b g_dc + D_c g_db - D_d g_bc
    term = np.zeros((P, 4, 4, 4), dtype=DT)
    for d in range(4):
        for b in range(4):
            for c in range(4):
                term[:, d, b, c] = (D[:, b, d, c] + D[:, c, d, b]
                                    - D[:, d, b, c])
    Gam = 0.5 * np.einsum('pad,pdbc->pabc', ginv, term)
    dterm = np.zeros((P, 3, 4, 4, 4), dtype=DT)
    for d in range(4):
        for b in range(4):
            for c in range(4):
                dterm[:, :, d, b, c] = (DD[:, :, b, d, c]
                                        + DD[:, :, c, d, b]
                                        - DD[:, :, d, b, c])
    dGam = (0.5 * np.einsum('pead,pdbc->peabc', dginv, term)
            + 0.5 * np.einsum('pad,pedbc->peabc', ginv, dterm))
    # R_bd = d_a Gam^a_bd - d_d Gam^a_ba
    #      + Gam^a_ae Gam^e_bd - Gam^a_de Gam^e_ba
    Ric = np.zeros((P, 4, 4), dtype=DT)
    for a in range(1, 4):
        Ric += dGam[:, a - 1, a, :, :]
    for d in range(1, 4):
        sub = np.zeros((P, 4), dtype=DT)
        for a in range(4):
            sub += dGam[:, d - 1, a, :, a]
        Ric[:, :, d] -= sub
    Ric += np.einsum('paae,pebd->pbd', Gam, Gam)
    Ric -= np.einsum('pade,peba->pbd', Gam, Gam)
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * gv
    return G / EIGHT_PI, gv


def metric_from_profiles(pts, pr, beta=BETA):
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    S, _, _, N, _, _, M, _, _ = [np.asarray(x, dtype=DT) for x in pr]
    g = np.zeros((len(pts), 4, 4), dtype=DT)
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -beta * S
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + ((M - 1.0) * n[:, i]) * n[:, j])
    return g


def T_at(muS, muN, muM, pts, beta=BETA, clamp=False):
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    pr = scaled_profiles(muS, muN, muM, r, clamp=clamp)
    return einstein_from_profiles(pts, pr, beta)


# ------------------------------------------------------------- frames
def eulerian_that(g, Tcov):
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


def _sampled_margins(That):
    flat = np.asarray(That, dtype=DT).reshape(-1, 4, 4)
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
        V = np.zeros((Np, 162, 4), dtype=DT)
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
    That = np.asarray(That, dtype=DT)
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


def nec_at(muS, muN, muM, pt, beta=BETA, clamp=False):
    pt = np.asarray(pt, dtype=DT)
    T, g = T_at(muS, muN, muM, pt[None, :], beta, clamp=clamp)
    That = eulerian_that(g, T)
    m = margins(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def worst_null(That):
    """Exact pointwise worst null direction: fib(642) scan
    + Nelder-Mead polish."""
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


# ------------------------------------------------------------- reads
def set_read(muS, muN, muM, beta=BETA, clamp=False):
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec',
                           'rho')}
    for rr in R_NODES:
        pts = DIRS162 * rr
        pr = scaled_profiles(muS, muN, muM,
                             np.full(len(pts), rr, dtype=DT),
                             clamp=clamp)
        T, g = einstein_from_profiles(pts, pr, beta)
        That = eulerian_that(g, T)
        m = margins(That)
        rec['typeI'].append(m['typeI'])
        rec['nec'].append(m['nec'])
        rec['wec'].append(m['wec'])
        rec['dec'].append(m['dec'])
        rec['sec'].append(m['sec'])
        rec['rho'].append(That[:, 0, 0])
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
        'joint': float(min(np.min(R['nec']), np.min(R['dec']))),
        'nec_argmin_point': (DIRS162[i_d] * R_NODES[i_r]).tolist(),
        'nec_argmin_r': float(R_NODES[i_r]),
        'dec_argmin_point': (DIRS162[j_d] * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
        'nec_argmin_typeI': bool(R['typeI'][i_nec]),
    }
    return out, R


# ------------------------------------------------------------- FD cross-path
def einstein_fd(pts, prof_fn, h=0.05, beta=BETA):
    """From-scratch 4-D centred-FD Einstein tensor from the
    metric function alone (profile values only). Stationary."""
    pts = np.asarray(pts, dtype=DT)

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
    Gam = np.zeros(pts.shape[:1] + (4, 4, 4), dtype=DT)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.zeros(pts.shape[:1] + (4,), dtype=DT)
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
        Gm = np.zeros(P.shape[:1] + (4, 4, 4), dtype=DT)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    term = np.zeros(P.shape[:1] + (4,), dtype=DT)
                    for d in range(4):
                        term[..., d] = (dgl[b][..., d, c]
                                        + dgl[c][..., d, b]
                                        - dgl[d][..., b, c])
                    Gm[..., a, b, c] = 0.5 * np.einsum(
                        '...d,...d->...', gi[..., a, :], term)
        return Gm

    Ric = np.zeros(pts.shape[:1] + (4, 4), dtype=DT)
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
