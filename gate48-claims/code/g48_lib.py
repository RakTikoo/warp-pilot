#!/usr/bin/env python3
"""
g48_lib.py -- Gate-48 machinery, written for this gate.

ORGANISATION (used by no earlier read): forward-mode
second-order TAYLOR JETS of the metric in SPHERICAL
coordinates (t, r, theta, phi). The metric components are
built as jet-valued arithmetic expressions in the profile
functions and the coordinate functions; no symbolic
expression is ever formed (contrast Gate-46: sympy symbolic
in spherical coordinates, lambdified; Gate-47: sympy
symbolic in Cartesian with cse), the jets are numeric in
spherical coordinates (contrast Gate-45: AD jets of the
metric in Cartesian coordinates with einsum contractions;
Gate-43: Cartesian analytic loops; the lineage:
hand-derived radial formulas feeding a Cartesian
assembly). Christoffel and Ricci contractions here are
explicit index loops in the spherical basis. The Eulerian
frame is the spherical orthonormal frame (n, r-hat,
theta-hat, phi-hat) of the same metric; margins are the
Hawking-Ellis eigenvalue margins at Type-I points
(frame-invariant), and pointwise deciding values are
exact worst-nulls (frame-invariant). Own profile
assembly from the programme's registered design
definitions and stored vectors (md5-verified artefacts).
No phase or earlier-gate code is imported. float64.
VM only.
"""
import json
import os

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
from scipy.special import betainc

DT = np.float64
BETA = 1.1
LAM_S = 0.70
WINNER_A = 0.07439108177516472
R_LO, R_HI = 10.0, 20.0
MU_H2 = 1.15
WP = os.environ.get('G48_WP', '/home/hatch/workspace/warp-pilot')

# ============================================================ jets
# A jet is (v, d, dd): v (P,), d (P,4) and dd (P,4,4) the
# first/second derivatives wrt (t, r, theta, phi). All
# metric jets have zero t-derivatives (static ansatz).


def jconst(c, P):
    v = np.full(P, float(c), dtype=DT)
    return v, np.zeros((P, 4)), np.zeros((P, 4, 4))


def jvar(idx, vals):
    P = len(vals)
    v = np.array(vals, dtype=DT)
    d = np.zeros((P, 4))
    d[:, idx] = 1.0
    return v, d, np.zeros((P, 4, 4))


def jadd(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]


def jsub(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


def jneg(a):
    return -a[0], -a[1], -a[2]


def jscale(a, c):
    c = np.asarray(c, dtype=DT)
    if c.ndim == 0:
        return a[0] * c, a[1] * c, a[2] * c
    return (a[0] * c, a[1] * c[:, None],
            a[2] * c[:, None, None])


def jmul(a, b):
    v = a[0] * b[0]
    d = a[1] * b[0][:, None] + b[1] * a[0][:, None]
    dd = (a[2] * b[0][:, None, None]
          + b[2] * a[0][:, None, None]
          + np.einsum('pi,pj->pij', a[1], b[1])
          + np.einsum('pi,pj->pij', b[1], a[1]))
    return v, d, dd


def jrecip(a):
    v = 1.0 / a[0]
    d = -a[1] * (v ** 2)[:, None]
    dd = (-a[2] * (v ** 2)[:, None, None]
          + 2.0 * np.einsum('pi,pj->pij', a[1], a[1])
          * (v ** 3)[:, None, None])
    return v, d, dd


def jdiv(a, b):
    return jmul(a, jrecip(b))


# ============================================================ profiles
# Registered design definitions (programme records):
# base shift LAM_S * S_ab(r; 2, 2) incomplete-beta plateau;
# base lapse 1 + WINNER_A * B_plat (c=15, W=5, e=3,
# smootherstep edges); base M 1 + 6 (U(r;8.5,20) -
# U(r;21,24)) quintic-smoothstep ramps; A2 totals = base +
# K=33 not-a-knot correction splines (constant extension
# outside [10, 20]); centre(mu): S -> mu S, N -> mu N,
# M -> 1 + mu (M-1); H2 totals = centre(1.15) of A2 +
# K=17 corrections; per-profile scaling on the totals;
# object corrections are further not-a-knot splines.


def _ss5(x):
    v = 6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3
    vp = 30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2
    vpp = 120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x
    return v, vp, vpp


def _ramp(r, a, b):
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


def _smoother(t):
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
    r = np.asarray(r, dtype=DT)
    Hx, Hpx, Hppx = _smoother((r - (c - W)) / e)
    Hy, Hpy, Hppy = _smoother(((c + W) - r) / e)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return B, Bp, Bpp


def _s_ab(r, a=2.0, b=2.0):
    """1 below 10, 0 above 20, 1 - I_u(a+1, b+1) between,
    u = (r-10)/10. B(a+1,b+1) = B(3,3) = 1/30."""
    r = np.asarray(r, dtype=DT)
    S = np.where(r >= 20.0, 0.0, 1.0)
    Sp = np.zeros_like(r)
    Spp = np.zeros_like(r)
    m = (r > 10.0) & (r < 20.0)
    if np.any(m):
        u = (r[m] - 10.0) / 10.0
        Bf = 1.0 / 30.0
        S[m] = 1.0 - betainc(a + 1.0, b + 1.0, u)
        f = u ** a * (1.0 - u) ** b
        Sp[m] = -f / (10.0 * Bf)
        fp = (u ** (a - 1.0) * (1.0 - u) ** (b - 1.0)
              * (a * (1.0 - u) - b * u))
        Spp[m] = -fp / (100.0 * Bf)
    return S, Sp, Spp


def _corr(vals, K, r):
    """Not-a-knot cubic spline through vals on K knots
    uniform on [10, 20]; constant extension outside
    (end value, zero derivatives). Returns (d, dp, dpp)."""
    r = np.asarray(r, dtype=DT)
    cs = CubicSpline(np.linspace(R_LO, R_HI, K),
                     np.asarray(vals, dtype=DT),
                     bc_type='not-a-knot')
    rc = np.clip(r, R_LO, R_HI)
    d = cs(rc)
    dp = cs.derivative(1)(rc)
    dpp = cs.derivative(2)(rc)
    out = (r < R_LO) | (r > R_HI)
    if np.any(out):
        dp = np.where(out, 0.0, dp)
        dpp = np.where(out, 0.0, dpp)
    return d, dp, dpp


# ------------------------------------------------ stored vectors
def _vecs_conf(path, key, val):
    conf = json.load(open(path))
    ent = [e for e in conf['confirmations'] if e[key] == val][0]
    return tuple(np.array(ent[k], dtype=DT)
                 for k in ('vS', 'vN', 'vM'))


def _vecs_state(path):
    st = json.load(open(path))
    fi = st['final_incumbent']
    return tuple(np.array(fi[k], dtype=DT)
                 for k in ('vS', 'vN', 'vM'))


def load_a2():
    return _vecs_conf(f'{WP}/phase344/results/'
                      'p344_confirmation.json', 'point', 'A2')


def load_a2_state():
    return _vecs_state(f'{WP}/phase344/results/'
                       'p344_state_A2.json')


def load_h2():
    return _vecs_conf(f'{WP}/phase379/results/'
                      'p379_confirmation.json', 'centre', 'H2')


def load_h2_state():
    return _vecs_state(f'{WP}/phase379/results/'
                       'p379_state_H2.json')


# ------------------------------------------------ profile stack
def base_profiles(r):
    r = np.asarray(r, dtype=DT)
    S, Sp, Spp = _s_ab(r)
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


def _add_corr(prof, vecs, K, r):
    out = []
    for i in range(3):
        d, dp, dpp = _corr(vecs[i], K, r)
        out += [prof[3 * i] + d, prof[3 * i + 1] + dp,
                prof[3 * i + 2] + dpp]
    return tuple(out)


def a2_totals(r):
    return _add_corr(base_profiles(r), load_a2(), 33, r)


def _centre(mu, prof):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)


def h2_totals(r):
    prof = _centre(MU_H2, a2_totals(r))
    return _add_corr(prof, load_h2(), 17, r)


def object_profiles(muS, muN, muM, vN, vM, K, r):
    """(S, Sp, Spp, N, Np, Npp, M, Mp, Mpp) at radii r:
    per-profile scaling of H2's totals, plus optional
    (vN, vM) correction splines on K knots (the static
    assembly: muS = 0 gives S identically zero)."""
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = h2_totals(r)
    S, Sp, Spp = muS * S, muS * Sp, muS * Spp
    N, Np, Npp = muN * N, muN * Np, muN * Npp
    M, Mp, Mpp = (1.0 + muM * (M - 1.0), muM * Mp, muM * Mpp)
    if vN is not None:
        d, dp, dpp = _corr(vN, K, r)
        N, Np, Npp = N + d, Np + dp, Npp + dpp
    if vM is not None:
        d, dp, dpp = _corr(vM, K, r)
        M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


# ============================================================ tensor
def _prof_jet(vals, P):
    """Jet of a radial profile: v = f(r), d = f' dr,
    dd = f'' dr dr."""
    f, fp, fpp = vals
    v = np.array(f, dtype=DT)
    d = np.zeros((P, 4))
    d[:, 1] = fp
    dd = np.zeros((P, 4, 4))
    dd[:, 1, 1] = fpp
    return v, d, dd


def metric_jets(muS, muN, muM, vN, vM, K, r, th, ph):
    """Jet-valued metric components in (t, r, th, ph).
    Returns (Gv, Gd, Gdd): Gv (P,4,4); Gd (P,4,4,4) with
    Gd[...,k] = d_k g; Gdd (P,4,4,4,4)."""
    r = np.asarray(r, dtype=DT)
    th = np.asarray(th, dtype=DT)
    ph = np.asarray(ph, dtype=DT)
    P = len(r)
    prof = object_profiles(muS, muN, muM, vN, vM, K, r)
    Sj = _prof_jet(prof[0:3], P)
    Nj = _prof_jet(prof[3:6], P)
    Mj = _prof_jet(prof[6:9], P)
    rj = jvar(1, r)
    # coordinate-function jets
    st = (np.sin(th), _dvec(P, 2, np.cos(th)),
          _ddvec(P, 2, 2, -np.sin(th)))
    ct = (np.cos(th), _dvec(P, 2, -np.sin(th)),
          _ddvec(P, 2, 2, -np.cos(th)))
    sp = (np.sin(ph), _dvec(P, 3, np.cos(ph)),
          _ddvec(P, 3, 3, -np.sin(ph)))
    cp = (np.cos(ph), _dvec(P, 3, -np.sin(ph)),
          _ddvec(P, 3, 3, -np.cos(ph)))
    zero = jconst(0.0, P)
    one = jconst(1.0, P)
    G = [[zero] * 4 for _ in range(4)]
    G[0][0] = jneg(jmul(Nj, Nj))
    bS = jscale(Sj, -BETA)
    G[0][1] = jmul(jmul(bS, st), cp)
    G[1][0] = G[0][1]
    G[0][2] = jmul(jmul(jmul(bS, rj), ct), cp)
    G[2][0] = G[0][2]
    G[0][3] = jneg(jmul(jmul(jmul(bS, rj), st), sp))
    G[3][0] = G[0][3]
    G[1][1] = Mj
    G[2][2] = jmul(rj, rj)
    G[3][3] = jmul(jmul(rj, rj), jmul(st, st))
    Gv = np.zeros((P, 4, 4))
    Gd = np.zeros((P, 4, 4, 4))
    Gdd = np.zeros((P, 4, 4, 4, 4))
    for a in range(4):
        for b in range(4):
            v, d, dd = G[a][b]
            Gv[:, a, b] = v
            Gd[:, a, b, :] = d
            Gdd[:, a, b, :, :] = dd
    return Gv, Gd, Gdd


def _dvec(P, idx, vals):
    d = np.zeros((P, 4))
    d[:, idx] = vals
    return d


def _ddvec(P, i, j, vals):
    dd = np.zeros((P, 4, 4))
    dd[:, i, j] = vals
    return dd


def einstein_from_jets(Gv, Gd, Gdd):
    """T_ab = G_ab / (8 pi) from the metric jets, by
    explicit index loops (spherical basis)."""
    P = Gv.shape[0]
    Hv = np.linalg.inv(Gv)
    # d_k ginv = -ginv (d_k g) ginv
    Hd = -np.einsum('pac,pcdk,pdb->pabk', Hv, Gd, Hv)
    # d_l d_k ginv = -[(d_l ginv)(d_k g) ginv
    #                 + ginv (d_l d_k g) ginv
    #                 + ginv (d_k g)(d_l ginv)]
    Hdd = -(np.einsum('pac,pcdkl,pdb->pabkl', Hv, Gdd, Hv)
            + np.einsum('pacl,pcdk,pdb->pabkl', Hd, Gd, Hv)
            + np.einsum('pac,pcdk,pdbl->pabkl', Hv, Gd, Hd))
    # Christoffel values and first derivatives
    Gam = np.zeros((P, 4, 4, 4))       # Gam[p,a,b,c]
    GamD = np.zeros((P, 4, 4, 4, 4))   # GamD[p,a,b,c,e]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                # A_d = d_b g_dc + d_c g_db - d_d g_bc
                A = (Gd[:, :, c, b] + Gd[:, :, b, c]
                     - Gd[:, b, c, :])          # (P, d)
                Gam[:, a, b, c] = 0.5 * np.einsum(
                    'pd,pd->p', Hv[:, a, :], A)
                for e in range(4):
                    Ae = (Gdd[:, :, c, b, e] + Gdd[:, :, b, c, e]
                          - Gdd[:, b, c, :, e])     # (P, d)
                    GamD[:, a, b, c, e] = 0.5 * (
                        np.einsum('pd,pd->p', Hd[:, a, :, e], A)
                        + np.einsum('pd,pd->p', Hv[:, a, :], Ae))
    # Ricci: R_ab = d_l Gam^l_ab - d_b Gam^l_al
    #              + Gam^l_ls Gam^s_ab - Gam^l_bs Gam^s_al
    R = np.zeros((P, 4, 4))
    for a in range(4):
        for b in range(4):
            acc = np.zeros(P)
            for lam in range(4):
                acc += GamD[:, lam, a, b, lam]
                acc -= GamD[:, lam, a, lam, b]
                for s in range(4):
                    acc += Gam[:, lam, lam, s] * Gam[:, s, a, b]
                    acc -= Gam[:, lam, b, s] * Gam[:, s, a, lam]
            R[:, a, b] = acc
    Rsc = np.einsum('pab,pab->p', Hv, R)
    G = R - 0.5 * Rsc[:, None, None] * Gv
    return G / (8.0 * np.pi), Gv


def eulerian_that_sph(T, Gv, r, th):
    """Eulerian orthonormal That in the spherical frame
    (n, r-hat, th-hat, ph-hat) of the same metric."""
    P = T.shape[0]
    gamma = Gv[:, 1:, 1:]
    ginv = np.linalg.inv(gamma)
    bcov = Gv[:, 0, 1:]
    bup = np.einsum('pij,pj->pi', ginv, bcov)
    alpha2 = -Gv[:, 0, 0] + np.einsum('pi,pi->p', bcov, bup)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    E = np.zeros((P, 4, 4))
    E[:, 0, 0] = 1.0 / alpha
    E[:, 1:, 0] = -bup / alpha[:, None]
    E[:, 1, 1] = 1.0 / np.sqrt(Gv[:, 1, 1])
    E[:, 2, 2] = 1.0 / r
    E[:, 3, 3] = 1.0 / (r * np.sin(th))
    That = np.einsum('pma,pnb,pmn->pab', E, E, T)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def margins(That):
    """Hawking-Ellis eigenvalue margins (documented
    definitions): Type-I iff the mixed tensor has real
    eigenvalues and exactly one timelike eigenvector.
    Type-I: rho = -lambda_t; NEC min(rho + p_i);
    WEC min(rho, NEC); SEC min(NEC, rho + sum p_i);
    DEC min(rho, rho - max |p_i|). NaN off Type-I."""
    That = np.asarray(That, dtype=DT)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy()
    M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] \
        + ev2[:, 3, :]
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
    out = {'typeI': typeI.reshape(shp), 'rho_eig': rho.reshape(shp),
           'ps': ps.reshape(shp + (3,)), 'nec': nec.reshape(shp),
           'wec': wec.reshape(shp), 'sec': sec.reshape(shp),
           'dec': dec.reshape(shp)}
    return out


def fib_dirs(npts):
    i = np.arange(npts, dtype=DT)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


DIRS642 = fib_dirs(642)


def worst_null(That):
    """Exact pointwise worst null direction: fib(642)
    scan + Nelder-Mead polish of q(n) = k^T That k,
    k = (1, n). Returns (n_fin, q_full, q_fib)."""
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


# ============================================================ reads
R_NODES = 10.0 + (np.arange(41, dtype=DT) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)


def _sph_of_cart(pts):
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    th = np.arccos(np.clip(pts[:, 2] / r, -1.0, 1.0))
    ph = np.arctan2(pts[:, 1], pts[:, 0])
    return r, th, ph


def that_at(muS, muN, muM, vN, vM, K, pts):
    """That (spherical Eulerian frame) at Cartesian pts."""
    r, th, ph = _sph_of_cart(pts)
    Gv, Gd, Gdd = metric_jets(muS, muN, muM, vN, vM, K, r, th, ph)
    T, _ = einstein_from_jets(Gv, Gd, Gdd)
    return eulerian_that_sph(T, Gv, r, th)


def point_read(muS, muN, muM, vN, vM, K, pt):
    That = that_at(muS, muN, muM, vN, vM, K,
                   np.asarray(pt, dtype=DT)[None, :])
    m = margins(That)
    wn, q_full, q_fib = worst_null(That[0])
    return {'That': That[0], 'typeI': bool(m['typeI'][0]),
            'rho_eig': float(m['rho_eig'][0]),
            'ps': m['ps'][0].tolist(),
            'nec': float(m['nec'][0]), 'wec': float(m['wec'][0]),
            'sec': float(m['sec'][0]), 'dec': float(m['dec'][0]),
            'rho_that00': float(That[0][0, 0]),
            'worst_null': q_full, 'worst_null_fib': q_fib,
            'worst_null_dir': wn.tolist()}


def set_read(muS, muN, muM, vN, vM, K):
    """SET-244 read (41 radial midpoint nodes x 162
    Fibonacci directions) with this gate's machinery.
    Margins are the eigenvalue margins; minima over
    Type-I points are frame-invariant statistics."""
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec',
                           'rho')}
    pts_all = []
    for rr in R_NODES:
        pts = DIRS162 * rr
        That = that_at(muS, muN, muM, vN, vM, K, pts)
        m = margins(That)
        rec['typeI'].append(m['typeI'])
        rec['nec'].append(m['nec'])
        rec['wec'].append(m['wec'])
        rec['dec'].append(m['dec'])
        rec['sec'].append(m['sec'])
        rec['rho'].append(That[:, 0, 0])
        pts_all.append(pts)
    R = {k: np.concatenate(v) for k, v in rec.items()}
    P = np.vstack(pts_all)
    ti = R['typeI']

    def mn(arr):
        return float(np.nanmin(arr))
    i_nec = int(np.nanargmin(R['nec']))
    i_dec = int(np.nanargmin(R['dec']))
    i_sec = int(np.nanargmin(R['sec']))
    out = {
        'set': 'SET-244 (41 radial midpoint nodes x 162 '
               'Fibonacci dirs)',
        'sampler': 'SAMPLER-M (spherical Eulerian frame; '
                   'eigenvalue margins)',
        'n_points': int(len(ti)),
        'typeI_fraction': float(np.mean(ti)),
        'typeI_count': int(np.sum(ti)),
        'nec_min': mn(R['nec']), 'dec_min': mn(R['dec']),
        'wec_min': mn(R['wec']), 'sec_min': mn(R['sec']),
        'rho_min': float(np.min(R['rho'])),
        'nec_argmin_point': P[i_nec].tolist(),
        'nec_argmin_r': float(np.linalg.norm(P[i_nec])),
        'nec_argmin_typeI': bool(ti[i_nec]),
        'dec_argmin_point': P[i_dec].tolist(),
        'dec_argmin_r': float(np.linalg.norm(P[i_dec])),
        'dec_argmin_typeI': bool(ti[i_dec]),
        'sec_argmin_r': float(np.linalg.norm(P[i_sec])),
        'sec_argmin_typeI': bool(ti[i_sec]),
        'joint_min_nec_dec': float(min(mn(R['nec']),
                                       mn(R['dec']))),
    }
    aux = {'R': R, 'pts': P}
    return out, aux
