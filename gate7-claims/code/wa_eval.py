"""
wa_eval.py — Gate-7 W-A evaluator for the SYMBOLIC radial-reduction path.

Loads the Einstein-tensor expressions derived in wa_symbolic.py
(wa_g_expr.pkl), lambdifies them (CSE, numpy, float64), and evaluates
them with ANALYTIC derivatives of the profile representations:
  * a(r), b(r): cubic splines of shell.py's stored profiles, differentiated
    with the spline's own analytic derivative (CubicSpline derivative);
  * S(r): cosine on [10,30], differentiated in closed form.
No Cartesian finite-difference stencil anywhere in this path.

Eulerian frame, Hawking-Ellis margins and the sampled-null NEC are
fresh implementations here (anchor-validated in wa_run_g7.py).
Conventions shared with Gate-6 (allowed): significance threshold
max(1e-9*(10/R1)^2, 1e-3*|rho_peak|); 26/52 Fibonacci point sets;
162-direction sampled-null cross-check.
Run with system python3. float64 everywhere.
"""
import pickle
import numpy as np
from scipy.interpolate import CubicSpline

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi
PKL = '/home/hatch/workspace/warp-pilot/gate7/wa_g_expr.pkl'

_cache = {}


def g_functions():
    if 'fns' in _cache:
        return _cache['fns']
    import sympy as sp
    with open(PKL, 'rb') as fh:
        blob = pickle.load(fh)
    atoms = blob['atoms']
    fns = {}
    for (i, j), expr in blob['Gcomp'].items():
        fns[(i, j)] = sp.lambdify(atoms, expr, modules='numpy', cse=True)
    _cache['fns'] = fns
    _cache['g_expr'] = blob['g']
    _cache['atoms'] = atoms
    return fns


def metric_numeric(pts, prof_splines, beta):
    """Metric g (P,4,4) from the same analytic representations (for the
    Eulerian frame construction). prof_splines = (a_s, b_s, S_func)."""
    a_s, b_s, sfunc = prof_splines
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    rc = np.clip(r, 0.0, 90.0)
    a = a_s(rc); b = b_s(rc)
    S, _, _ = sfunc(r)
    P = len(pts)
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -np.exp(2 * a)
    g[:, 0, 1] = g[:, 1, 0] = -beta * S
    eb = np.exp(2 * b) - 1.0
    rsafe = np.where(r > 0, r, 1.0)
    n = pts / rsafe[:, None]
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
        g[:, 1 + i, 1 + i] += 1.0
    return g


def einstein_symbolic(pts, prof_splines, beta):
    """G (P,4,4) covariant from the symbolic expressions + analytic derivs."""
    a_s, b_s, sfunc = prof_splines
    fns = g_functions()
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    rc = np.clip(r, 0.0, 90.0)
    rsafe = np.where(r > 0, r, 1.0)
    n = pts / rsafe[:, None]
    a = a_s(rc); ap = a_s(rc, 1); app = a_s(rc, 2)
    b = b_s(rc); bp = b_s(rc, 1); bpp = b_s(rc, 2)
    S, Sp, Spp = sfunc(r)
    args = (r, n[:, 0], n[:, 1], n[:, 2], a, ap, app, b, bp, bpp, S, Sp, Spp,
            np.full_like(r, float(beta)))
    G = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    for (i, j), fn in fns.items():
        v = np.asarray(fn(*args), dtype=DTYPE)
        v = np.broadcast_to(v, (len(pts),))
        G[:, i, j] = v
        G[:, j, i] = v
    return G


def make_splines(prof):
    return (CubicSpline(prof['r'], prof['a']), CubicSpline(prof['r'], prof['b']))


def cosine_sfunc(R1=10.0, R2=30.0):
    L = R2 - R1
    k = np.pi / L

    def sfunc(r):
        r = np.asarray(r, dtype=DTYPE)
        u = (r - R1) / L
        inside = (r >= R1) & (r <= R2)
        S = np.where(r < R1, 1.0, np.where(r > R2, 0.0, 0.5 * (1.0 + np.cos(np.pi * np.clip(u, 0, 1)))))
        Sp = np.where(inside, -0.5 * k * np.sin(np.pi * np.clip(u, 0, 1)), 0.0)
        Spp = np.where(inside, -0.5 * k * k * np.cos(np.pi * np.clip(u, 0, 1)), 0.0)
        return S, Sp, Spp
    return sfunc


def eulerian_that(g, Tcov):
    """Eulerian orthonormal-frame T from covariant T and metric g.
    Fresh implementation of the standard ADM frame: lapse alpha,
    shift beta^i = gamma^{ij} beta_j, spatial triad from eigh(gamma)."""
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


def margins_from_that(That):
    """Hawking-Ellis margins: eigenvalues of the mixed tensor
    T^a_b = eta^{ac} T_cb in the orthonormal frame (row 0 negated)."""
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
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
    ps = np.where(typeI[:, None], evals.real[mask].reshape(Np, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    return {'rho': rho, 'p': ps, 'typeI': typeI, 'nec': nec, 'wec': wec,
            'sec': sec, 'dec': dec}


def sampled_nec_min(That, n_dir=162):
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
    i = np.arange(n_dir, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n_dir)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)
    T00 = flat[:, 0, 0]; T0i = flat[:, 0, 1:]; Tij = flat[:, 1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
    vals = T00[:, None] + 2.0 * (T0i @ dirs.T) + quad
    return vals.min(axis=1)


def audit_symbolic(pts, prof, beta):
    spl = make_splines(prof) + (cosine_sfunc(prof['R1'], prof['R2']),)
    G = einstein_symbolic(pts, spl, beta)
    g = metric_numeric(pts, spl, beta)
    That = eulerian_that(g, G / EIGHT_PI)
    m = margins_from_that(That)
    m['That'] = That
    m['G'] = G
    m['sampled_nec'] = sampled_nec_min(That)
    return m


def fib_dirs(n):
    i = np.arange(n)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


def fine_pts(R1, R2):
    DIRS = fib_dirs(26)
    rad = np.concatenate([np.arange(0.3 * R1, R1 - 0.74, 1.0),
                          np.arange(R1 - 0.75, R2 + 0.01, 0.5),
                          np.arange(R2 + 1.0, 1.35 * R2 + 0.01, 2.0)])
    pts = np.concatenate([DIRS * rr for rr in rad]).astype(DTYPE)
    return pts, np.linalg.norm(pts, axis=1), rad


def robustness_pts(R1, R2):
    DIRS = fib_dirs(52)
    rad = np.concatenate([np.arange(9.75, 11.50 + 1e-9, 0.125),
                          np.arange(32.0, 40.0 + 1e-9, 0.5)])
    pts = np.concatenate([DIRS * rr for rr in rad]).astype(DTYPE)
    return pts, np.linalg.norm(pts, axis=1), rad


def summarise(m, pts, radp, R1, R2):
    That = m['That']
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / R1) ** 2, 1e-3 * abs(rho_peak))
    out = {'rho_peak': rho_peak, 'n_pts': int(len(pts)), 'thr': thr}
    for reg, mask0 in (('all_sig', np.ones(len(pts), bool)),
                       ('core', (radp >= R1) & (radp <= R2)),
                       ('cavity', radp < R1), ('exterior', radp > R2)):
        mask = mask0 & (scale > thr)
        d = {}
        for k in ('nec', 'wec', 'sec', 'dec'):
            v = m[k][mask]; i = int(np.nanargmin(v)); idx = int(np.where(mask)[0][i])
            d[k] = float(v[i]); d[k + '_r'] = float(radp[idx])
            d[k + '_pt'] = [float(x) for x in pts[idx]]
        d['worst'] = min(d[k] for k in ('nec', 'wec', 'sec', 'dec'))
        d['worst_kind'] = min(('nec', 'wec', 'sec', 'dec'), key=lambda kk: d[kk])
        d['typeI_frac'] = float(np.mean(m['typeI'][mask])) if mask.sum() else float('nan')
        d['n'] = int(mask.sum())
        d['n_non_typeI'] = int((~m['typeI'][mask]).sum())
        out[reg] = d
    cmask = (radp >= R1) & (radp <= R2) & (scale > thr)
    out['core_sampled_nec_min'] = float(np.min(m['sampled_nec'][cmask]))
    i = int(np.argmin(np.where(cmask, m['sampled_nec'], np.inf)))
    out['core_sampled_nec_r'] = float(radp[i])
    out['core_sampled_nec_pt'] = [float(x) for x in pts[i]]
    ns = scale <= thr
    out['n_nonsig'] = int(ns.sum())
    if ns.sum() > 10:
        out['floor_proxy_nonsig_median_abs_nec'] = float(np.nanmedian(np.abs(m['nec'][ns])))
    return out
