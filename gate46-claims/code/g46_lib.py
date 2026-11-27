#!/usr/bin/env python3
"""
g46_lib.py -- Gate-46 read machinery, written for this gate.

Tensor path: the sympy-derived spherical-coordinate Einstein
tensor (g46_derive.py -> g46_exprs.py), lambdified and
transformed to Cartesian components point by point. No phase
code and no earlier gate code is imported or reused for any
deciding read; the registered definitions (SET-244 grid,
SAMPLER-M, Eulerian frame, Hawking-Ellis margins, fib-642 +
polish worst-null) are re-implemented here from the records.

Frames/margins discipline (Gate-43 C-10): deciding values are
taken at named points or from frame-invariant statistics
(eigenvalue margins at Type-I points, rho, Type-I counts,
exact worst-nulls). Raw sampled minima at non-Type-I points
carry the +-3e-6 frame-convention band and are never deciding
alone.

float64. VM only.
"""
import os
import sys

import numpy as np
import sympy as sp
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g46_profiles as prof  # noqa: E402
from g46_exprs import EXPRS  # noqa: E402

DT = np.float64
BETA = prof.BETA
EIGHT_PI = 8.0 * np.pi

# ------------------------------------------------------------ sampler
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

# ------------------------------------------------------------ tensor (sympy path)
_SYM = sp.symbols('r th ph Sv Spv Sppv Nv Npv Nppv Mv Mpv Mppv')
_TFUNS = {}
for _k, _s in EXPRS.items():
    _TFUNS[_k] = sp.lambdify(_SYM, sp.sympify(_s), 'numpy')


def T_sph(pts, pr):
    """Covariant T in the spherical coordinate basis at pts
    (P, 3) Cartesian, from profile arrays pr at the points'
    radii. Returns (P, 4, 4), coordinate order (t, r, th, ph)."""
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    th = np.arccos(np.clip(pts[:, 2] / r, -1.0, 1.0))
    ph = np.arctan2(pts[:, 1], pts[:, 0])
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = [
        np.asarray(x, dtype=DT) for x in pr]
    args = (r, th, ph, S, Sp, Spp, N, Np, Npp, M, Mp, Mpp)
    T = np.zeros((len(pts), 4, 4), dtype=DT)
    for (a, b), fn in _TFUNS.items():
        val = np.broadcast_to(np.asarray(fn(*args), dtype=DT),
                              (len(pts),))
        T[:, a, b] = val
        T[:, b, a] = val
    return T


def _sph_jacobian(pts):
    """L^a_M = d(coord a)/d(cart M), a in (r, th, ph),
    M in (x, y, z); returns (P, 3, 3)."""
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    sth = np.sqrt(np.maximum(pts[:, 0] ** 2 + pts[:, 1] ** 2, 0.0)) / r
    cth = pts[:, 2] / r
    sph = np.arctan2(pts[:, 1], pts[:, 0])
    cph, sphv = np.cos(sph), np.sin(sph)
    L = np.zeros((len(pts), 3, 3), dtype=DT)
    L[:, 0, 0] = sth * cph
    L[:, 0, 1] = sth * sphv
    L[:, 0, 2] = cth
    L[:, 1, 0] = cth * cph / r
    L[:, 1, 1] = cth * sphv / r
    L[:, 1, 2] = -sth / r
    L[:, 2, 0] = -sphv / (r * sth)
    L[:, 2, 1] = cph / (r * sth)
    return L


def T_cart(pts, pr):
    """Covariant T in Cartesian components (t, x, y, z)."""
    Ts = T_sph(pts, pr)
    L = _sph_jacobian(pts)
    J = np.zeros((len(pts), 4, 4), dtype=DT)
    J[:, 0, 0] = 1.0
    J[:, 1:, 1:] = L
    return np.einsum('pai,pab,pbj->pij', J, Ts, J)


def metric_cart(pts, pr):
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    S, _, _, N, _, _, M, _, _ = [np.asarray(x, dtype=DT) for x in pr]
    g = np.zeros((len(pts), 4, 4), dtype=DT)
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + ((M - 1.0) * n[:, i]) * n[:, j])
    return g


def T_at(muS, muN, muM, pts, clamp=False):
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    pr = prof.scaled_profiles(muS, muN, muM, r, clamp=clamp)
    return T_cart(pts, pr), metric_cart(pts, pr)


# ------------------------------------------------------------ frames
def eulerian_that(g, Tcov):
    """Eulerian orthonormal-frame components of Tcov.
    Tetrad: e_0 = (1/alpha, -beta^up/alpha); spatial triad the
    eigh eigenvectors of gamma, scaled by 1/sqrt(eigenvalue)."""
    g = np.asarray(g, dtype=DT)
    gamma = g[..., 1:, 1:]
    bcov = g[..., 0, 1:]
    ginv = np.linalg.inv(gamma)
    bup = np.einsum('...ij,...j->...i', ginv, bcov)
    alpha = np.sqrt(np.maximum(
        -g[..., 0, 0] + np.einsum('...i,...i->...', bcov, bup),
        1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DT)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -bup / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = V[..., :, i] / np.sqrt(lam[..., i])[..., None]
    That = np.einsum('...ma,...mn,...nb->...ab', E, Tcov, E)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def _sampled_margins(That):
    """SAMPLER-M sampled margins at non-Type-I points:
    162 Fibonacci directions x velocities linspace(0, .95, 6)."""
    flat = np.asarray(That, dtype=DT).reshape(-1, 4, 4)
    Np = flat.shape[0]
    dirs = DIRS162
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
    """Hawking-Ellis eigenvalue margins at Type-I points;
    SAMPLER-M sampled margins at non-Type-I points."""
    That = np.asarray(That, dtype=DT)
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    Mx = flat.copy()
    Mx[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(Mx)
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
    ps = np.where(typeI[:, None],
                  evals.real[mask].reshape(Np, 3), np.nan)
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
        nec[bad] = ns
        wec[bad] = ws
        sec[bad] = ss
        dec[bad] = ds
    return {'typeI': typeI, 'nec': nec, 'wec': wec, 'sec': sec,
            'dec': dec, 'rho_eig': rho}


def worst_null(That):
    """Exact pointwise worst null value: fib(642) scan +
    Nelder-Mead polish over the spatial direction."""
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


# ------------------------------------------------------------ reads
def set_read(muS, muN, muM, clamp=False):
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec', 'rho')}
    for rr in R_NODES:
        pts = DIRS162 * rr
        pr = prof.scaled_profiles(muS, muN, muM,
                                   np.full(len(pts), rr, dtype=DT),
                                   clamp=clamp)
        T = T_cart(pts, pr)
        g = metric_cart(pts, pr)
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
        'nec_argmin_typeI': bool(R['typeI'][i_nec]),
        'dec_argmin_point': (DIRS162[j_d] * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
    }
    return out, R


def that_at(muS, muN, muM, pt, clamp=False):
    pt = np.asarray(pt, dtype=DT)
    T, g = T_at(muS, muN, muM, pt[None, :], clamp=clamp)
    return eulerian_that(g, T)[0]


# ------------------------------------------------------------ FD cross-path
def einstein_fd(pts, prof_fn, h=0.05):
    """From-scratch 4-D centred-FD (4th-order) Einstein tensor
    from the metric function alone (profile values only).
    Stationary. Used only as the C-2 calibration cross-path."""
    pts = np.asarray(pts, dtype=DT)

    def gfun(P):
        return metric_cart(P, prof_fn(P))

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

    def gamma_of(gg, dgl, gi):
        Gm = np.zeros(gg.shape[:1] + (4, 4, 4), dtype=DT)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    term = np.zeros(gg.shape[:1] + (4,), dtype=DT)
                    for d in range(4):
                        term[..., d] = (dgl[b][..., d, c]
                                        + dgl[c][..., d, b]
                                        - dgl[d][..., b, c])
                    Gm[..., a, b, c] = 0.5 * np.einsum(
                        '...d,...d->...', gi[..., a, :], term)
        return Gm

    Gam = gamma_of(g, dg, ginv)

    def gamma_fun(P):
        gg = gfun(P)
        gi = np.linalg.inv(gg)
        dgl = [np.zeros_like(gg) for _ in range(4)]
        for a in range(3):
            offs = []
            for k in (-2, -1, 1, 2):
                q = P.copy()
                q[:, a] += k * h
                offs.append(gfun(q))
            dgl[a + 1] = (offs[0] - 8.0 * offs[1] + 8.0 * offs[2]
                          - offs[3]) / (12.0 * h)
        return gamma_of(gg, dgl, gi)

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
