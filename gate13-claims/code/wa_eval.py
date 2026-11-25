"""
wa_eval.py -- Gate-13 W-A evaluator on the symbolic radial-reduction path.

The Einstein-tensor expressions derived in wa_symbolic.py are
lambdified (CSE, numpy, float64) and evaluated with ANALYTIC
derivatives supplied by wa_profiles.py (spline derivatives for a, b
and each shell's S; closed form for the cosine control).  No
Cartesian finite-difference stencil is used for any deciding
quantity (margins, Type-I, sampled-null).

The Eulerian orthonormal frame, the Hawking-Ellis margin extraction
and the 162-direction sampled-null cross-check are implemented fresh
here.  Shared convention (allowed): significance threshold
max(1e-11, 1e-3 |rho_peak|), the Phase-80 convention.

One diagnostic is explicitly NOT a deciding quantity: the
conservation read (covariant divergence of the analytic T field,
estimated by centred differences OF THE ANALYTIC T FIELD ITSELF at
the phase's gate-standard spacing, with Christoffel symbols
evaluated from the analytic metric) -- it exists only to compare
against the phase's stored conservation class in anchor (iii),
whose own value is an FD-representation diagnostic of the same kind.
Run with ~/workspace/warp-pilot/venv/bin/python.  float64 everywhere.
"""
import pickle

import numpy as np

F64 = np.float64
EIGHT_PI = 8.0 * np.pi
PKL = '/home/hatch/workspace/warp-pilot/gate13/wa_g13_expr.pkl'
_cache = {}


def _load():
    if 'fns' in _cache:
        return _cache['fns'], _cache['atoms']
    import sympy as sp
    with open(PKL, 'rb') as fh:
        blob = pickle.load(fh)
    fns = {}
    for key, expr in blob['Gcomp'].items():
        fns[key] = sp.lambdify(blob['atoms'], expr, modules='numpy', cse=True)
    _cache['fns'] = fns
    _cache['atoms'] = blob['atoms']
    return fns, blob['atoms']


def _profiles_at(pts, a_spl, b_spl, vfunc):
    pts = np.asarray(pts, dtype=F64)
    r = np.linalg.norm(pts, axis=1)
    rc = np.clip(r, 0.0, a_spl.x[-1])
    rsafe = np.where(r > 0, r, 1.0)
    n = pts / rsafe[:, None]
    V, V1, V2 = vfunc(r)
    return {'r': r, 'n': n,
            'a': a_spl(rc), 'a1': a_spl(rc, 1), 'a2': a_spl(rc, 2),
            'b': b_spl(rc), 'b1': b_spl(rc, 1), 'b2': b_spl(rc, 2),
            'V': V, 'V1': V1, 'V2': V2}


def metric_at(pts, a_spl, b_spl, vfunc):
    d = _profiles_at(pts, a_spl, b_spl, vfunc)
    P = len(pts)
    g = np.zeros((P, 4, 4), dtype=F64)
    g[:, 0, 0] = -np.exp(2.0 * d['a'])
    g[:, 0, 1] = g[:, 1, 0] = -d['V']
    eb = np.exp(2.0 * d['b']) - 1.0
    n = d['n']
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
        g[:, 1 + i, 1 + i] += 1.0
    return g


def einstein_at(pts, a_spl, b_spl, vfunc):
    fns, _ = _load()
    d = _profiles_at(pts, a_spl, b_spl, vfunc)
    n = d['n']
    args = (d['r'], n[:, 0], n[:, 1], n[:, 2], d['a'], d['a1'], d['a2'],
            d['b'], d['b1'], d['b2'], d['V'], d['V1'], d['V2'])
    G = np.zeros((len(pts), 4, 4), dtype=F64)
    for (i, j), fn in fns.items():
        v = np.broadcast_to(np.asarray(fn(*args), dtype=F64), (len(pts),))
        G[:, i, j] = v
        G[:, j, i] = v
    return G


def combine_vfunc(beta_o, sf_o, beta_i, sf_i):
    def vfunc(rr):
        So, So1, So2 = sf_o(rr)
        Si, Si1, Si2 = sf_i(rr)
        return (beta_o * So + beta_i * Si,
                beta_o * So1 + beta_i * Si1,
                beta_o * So2 + beta_i * Si2)
    return vfunc


def single_vfunc(beta, sf):
    def vfunc(rr):
        S, S1, S2 = sf(rr)
        return beta * S, beta * S1, beta * S2
    return vfunc


def zero_vfunc(rr):
    rr = np.asarray(rr, dtype=F64)
    z = np.zeros_like(rr)
    return z, z, z


# ------------------------------------------------------------- frame/margins
def eulerian_frame_T(g, Tcov):
    """Orthonormal Eulerian T: lapse/shift split of g, spatial triad from
    the eigendecomposition of gamma_ij."""
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha = np.sqrt(np.maximum(
        -g[..., 0, 0] + np.einsum('...i,...i->...', beta_cov, beta_up), 1e-300))
    evals_g, evecs_g = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=F64)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = evecs_g[..., :, i] / np.sqrt(evals_g[..., i])[..., None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def hawking_ellis(That):
    """Eigen-decomposition of T^a_b = eta^{ac} T_cb in the orthonormal
    frame; Type-I iff exactly one eigenvector is timelike (norm < 0)."""
    flat = np.asarray(That, dtype=F64).reshape(-1, 4, 4)
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
    ps = np.where(typeI[:, None], evals.real[mask].reshape(Np, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    return {'rho': rho, 'p': ps, 'typeI': typeI,
            'nec': nec, 'wec': wec, 'sec': sec, 'dec': dec}


def sampled_null_min(That, n_dir=162):
    flat = np.asarray(That, dtype=F64).reshape(-1, 4, 4)
    i = np.arange(n_dir, dtype=F64)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n_dir)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)
    quad = np.einsum('njk,ij,ik->ni', flat[:, 1:, 1:], dirs, dirs)
    vals = flat[:, 0, 0][:, None] + 2.0 * (flat[:, 0, 1:] @ dirs.T) + quad
    return vals.min(axis=1)


def audit(pts, a_spl, b_spl, vfunc):
    G = einstein_at(pts, a_spl, b_spl, vfunc)
    g = metric_at(pts, a_spl, b_spl, vfunc)
    That = eulerian_frame_T(g, G / EIGHT_PI)
    out = hawking_ellis(That)
    out['That'] = That
    out['G'] = G
    out['sampled_nec'] = sampled_null_min(That)
    return out


KINDS = ('nec', 'wec', 'sec', 'dec')
REGIONS = ('payload', 'inner_wall', 'cavity', 'outer_wall', 'exterior')
ALONE_REGIONS = ('interior', 'fringe_lo', 'wall', 'fringe_hi', 'exterior')


def _block(m, pts, sel, ti):
    rr = np.linalg.norm(np.asarray(pts, dtype=F64), axis=1)
    tisel = sel & ti
    e = {'n_sig': int(np.sum(sel)), 'n_non_typeI': int(np.sum(sel & ~ti)),
         'typeI_frac': float(np.mean(ti[sel])) if np.any(sel) else None}
    for k in KINDS:
        v = m[k][tisel]
        v = v[~np.isnan(v)]
        e['min_' + k] = float(np.min(v)) if v.size else None
    vv = [e['min_' + k] for k in KINDS if e['min_' + k] is not None]
    e['worst'] = float(min(vv)) if vv else None
    e['worst_kind'] = (min((k for k in KINDS if e['min_' + k] is not None),
                           key=lambda k: e['min_' + k]) if vv else None)
    sn = m['sampled_nec'][sel]
    e['min_sampled_nec_all'] = float(np.nanmin(sn)) if sn.size else None
    if vv:
        stack = np.stack([np.where(tisel, np.where(np.isnan(m[k]), np.inf, m[k]),
                                   np.inf) for k in KINDS])
        e['worst_r'] = float(rr[np.argmin(np.min(stack, axis=0))])
    return e


def summarise(m, pts, region_fn, regions=REGIONS):
    That = m['That']
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-11, 1e-3 * abs(rho_peak))
    sig = scale > thr
    ti = m['typeI']
    rr = np.linalg.norm(np.asarray(pts, dtype=F64), axis=1)
    reg_of = np.array([region_fn(v) for v in rr])

    out = {'n_pts': int(len(pts)), 'n_sig': int(np.sum(sig)),
           'rho_peak': rho_peak, 'thr': float(thr),
           'typeI_frac_sig': float(np.mean(ti[sig])) if np.any(sig) else None,
           'n_sig_non_typeI': int(np.sum(sig & ~ti))}
    core = _block(m, pts, sig, ti)
    for k in ('min_nec', 'min_wec', 'min_sec', 'min_dec', 'worst', 'worst_kind'):
        out[k] = core[k]
    out['min_sampled_nec_all_sig'] = core['min_sampled_nec_all']
    out['regions'] = {reg: _block(m, pts, sig & (reg_of == reg), ti)
                      for reg in regions if np.any(sig & (reg_of == reg))}
    return out


# ------------------------------------------- conservation diagnostic (only)
def conservation_read(pts, a_spl, b_spl, vfunc, h=0.15):
    """DIAGNOSTIC ONLY (see module docstring).  Covariant divergence
    nabla_a T^a_b of the analytic T field: T and g are evaluated
    analytically at offset points; only the derivatives OF T and OF g
    (for Gamma) use centred differences at spacing h, mirroring the
    phase's gate-standard conservation class (p523 pattern).  The
    relative read is max_b |div_b| / max|T_cov| per point, median
    over points.  No deciding quantity uses this function."""
    pts = np.asarray(pts, dtype=F64)
    P = len(pts)

    def Tmixed(p):
        G = einstein_at(p, a_spl, b_spl, vfunc)
        g = metric_at(p, a_spl, b_spl, vfunc)
        ginv = np.linalg.inv(g)
        Tcov = G / EIGHT_PI
        return np.einsum('...ac,...cb->...ab', ginv, Tcov), Tcov, g, ginv

    Tm, Tcov, g0, ginv0 = Tmixed(pts)
    dg = np.zeros((P, 4, 4, 4), dtype=F64)
    dT = np.zeros((P, 4, 4, 4), dtype=F64)  # dT[e][a][b] = d_e T^a_b
    for ax in range(3):
        off = np.zeros(3); off[ax] = h
        gp = metric_at(pts + off, a_spl, b_spl, vfunc)
        gn = metric_at(pts - off, a_spl, b_spl, vfunc)
        dg[:, ax + 1] = (gp - gn) / (2.0 * h)
        Tp, _, _, _ = Tmixed(pts + off)
        Tn, _, _, _ = Tmixed(pts - off)
        dT[:, ax + 1] = (Tp - Tn) / (2.0 * h)
    Gamma = np.zeros((P, 4, 4, 4), dtype=F64)  # Gamma[a][b][c]
    for a_ in range(4):
        for b_ in range(4):
            for c_ in range(4):
                term = np.stack([dg[:, b_, d, c_] + dg[:, c_, d, b_]
                                 - dg[:, d, b_, c_] for d in range(4)], axis=-1)
                Gamma[:, a_, b_, c_] = 0.5 * np.einsum('...d,...d->...',
                                                       ginv0[:, a_, :], term)
    div = np.einsum('...aab->...b', dT)
    div = div + np.einsum('...aal,...lb->...b', Gamma, Tm)
    div = div - np.einsum('...lab,...al->...b', Gamma, Tm)
    scale = np.maximum(np.max(np.abs(Tcov), axis=(1, 2)), 1e-300)
    rel = np.max(np.abs(div), axis=1) / scale
    return {'n_pts': int(P), 'hdiv': float(h),
            'rel_med': float(np.median(rel)), 'rel_max': float(np.max(rel)),
            'div_abs_med': float(np.median(np.max(np.abs(div), axis=1)))}
