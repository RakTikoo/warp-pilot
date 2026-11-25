"""
wa_eval.py — Gate-10 W-A evaluator for the SYMBOLIC radial-reduction path.

Loads the Einstein-tensor expressions derived in wa_symbolic.py
(wa_g_expr.pkl), lambdifies them (CSE, numpy, float64), and evaluates
them with ANALYTIC derivatives of the profile representations:
  * a(r), b(r): cubic splines of the profile grids, differentiated
    with the spline's own analytic derivative;
  * V(r) = beta_o S_o(r) + beta_i S_i(r): each S with analytic
    derivatives (chain-spline derivatives, or closed-form cosine).
No Cartesian finite-difference stencil anywhere in this path.

Eulerian frame, Hawking-Ellis margins and the sampled-null NEC are
fresh implementations here (anchor-validated in wa_run.py).
Conventions shared with the phase record (allowed): significance
threshold max(1e-11, 1e-3*|rho_peak|) (the Phase-80 convention);
162-direction sampled-null cross-check.
Run with ~/workspace/warp-pilot/venv/bin/python. float64 everywhere.
"""
import pickle
import numpy as np

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi
PKL = '/home/hatch/workspace/warp-pilot/gate10/wa_g_expr.pkl'

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
    _cache['atoms'] = atoms
    return fns


def metric_numeric(pts, a_s, b_s, vfunc):
    """Metric g (P,4,4) from the same analytic representations (for the
    Eulerian frame construction). vfunc(r) -> (V, V', V'')."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    rc = np.clip(r, 0.0, a_s.x[-1])
    a = a_s(rc); b = b_s(rc)
    V, _, _ = vfunc(r)
    P = len(pts)
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -np.exp(2 * a)
    g[:, 0, 1] = g[:, 1, 0] = -V
    eb = np.exp(2 * b) - 1.0
    rsafe = np.where(r > 0, r, 1.0)
    n = pts / rsafe[:, None]
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
        g[:, 1 + i, 1 + i] += 1.0
    return g


def einstein_symbolic(pts, a_s, b_s, vfunc):
    """G (P,4,4) covariant from the symbolic expressions + analytic derivs."""
    fns = g_functions()
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    rc = np.clip(r, 0.0, a_s.x[-1])
    rsafe = np.where(r > 0, r, 1.0)
    n = pts / rsafe[:, None]
    a = a_s(rc); ap = a_s(rc, 1); app = a_s(rc, 2)
    b = b_s(rc); bp = b_s(rc, 1); bpp = b_s(rc, 2)
    V, Vp, Vpp = vfunc(r)
    args = (r, n[:, 0], n[:, 1], n[:, 2], a, ap, app, b, bp, bpp, V, Vp, Vpp)
    G = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    for (i, j), fn in fns.items():
        v = np.asarray(fn(*args), dtype=DTYPE)
        v = np.broadcast_to(v, (len(pts),))
        G[:, i, j] = v
        G[:, j, i] = v
    return G


def composed_vfunc(beta_o, sfunc_o, beta_i, sfunc_i):
    def vfunc(r):
        So, Spo, Sppo = sfunc_o(r)
        Si, Spi, Sppi = sfunc_i(r)
        return (beta_o * So + beta_i * Si,
                beta_o * Spo + beta_i * Spi,
                beta_o * Sppo + beta_i * Sppi)
    return vfunc


def zero_vfunc(r):
    r = np.asarray(r, dtype=DTYPE)
    z = np.zeros_like(r)
    return z, z, z


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


def audit(pts, a_s, b_s, vfunc):
    G = einstein_symbolic(pts, a_s, b_s, vfunc)
    g = metric_numeric(pts, a_s, b_s, vfunc)
    That = eulerian_that(g, G / EIGHT_PI)
    m = margins_from_that(That)
    m['That'] = That
    m['G'] = G
    m['sampled_nec'] = sampled_nec_min(That)
    return m


KINDS = ('nec', 'wec', 'sec', 'dec')
REGIONS = ('payload', 'inner_wall', 'cavity', 'outer_wall', 'exterior')


def summarise(m, pts, region_fn):
    """Phase-80 summarise pattern on the symbolic path: regional worst
    over Type-I significant points; typeI_frac + sampled-null over ALL
    significant points carry the failure modes."""
    That = m['That']
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-11, 1e-3 * abs(rho_peak))
    sig = scale > thr
    ti = m['typeI']
    out = {'n_pts': int(len(pts)), 'n_sig': int(np.sum(sig)),
           'rho_peak': rho_peak, 'thr': float(thr),
           'typeI_frac_sig': float(np.mean(ti[sig])) if np.any(sig) else None,
           'n_sig_non_typeI': int(np.sum(sig & ~ti))}
    for k in KINDS:
        v = m[k][sig & ti]
        v = v[~np.isnan(v)]
        out['min_' + k] = float(np.min(v)) if v.size else None
    vals = [out['min_' + k] for k in KINDS if out['min_' + k] is not None]
    out['worst'] = float(min(vals)) if vals else None
    sn = m['sampled_nec'][sig]
    out['min_sampled_nec_all_sig'] = float(np.nanmin(sn)) if sn.size else None
    rr = np.sqrt(np.sum(np.asarray(pts) ** 2, axis=1))
    regs = {}
    for reg in REGIONS:
        sel = sig & np.array([region_fn(x) == reg for x in rr])
        if not np.any(sel):
            continue
        tisel = sel & ti
        entry = {'n_sig': int(np.sum(sel)),
                 'n_non_typeI': int(np.sum(sel & ~ti)),
                 'typeI_frac': float(np.mean(ti[sel]))}
        for k in KINDS:
            v = m[k][tisel]
            v = v[~np.isnan(v)]
            entry['min_' + k] = float(np.min(v)) if v.size else None
        vv = [entry['min_' + k] for k in KINDS if entry['min_' + k] is not None]
        entry['worst'] = float(min(vv)) if vv else None
        entry['worst_kind'] = (min((k for k in KINDS if entry['min_' + k] is not None),
                                   key=lambda k: entry['min_' + k]) if vv else None)
        sreg = m['sampled_nec'][sel]
        entry['min_sampled_nec_all'] = float(np.nanmin(sreg)) if sreg.size else None
        if vv:
            stack = np.stack([np.where(tisel, np.where(np.isnan(m[k]), np.inf, m[k]), np.inf)
                              for k in KINDS])
            entry['worst_r'] = float(rr[np.argmin(np.min(stack, axis=0))])
        regs[reg] = entry
    out['regions'] = regs
    return out
