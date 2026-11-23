"""
wc_auditor.py — W-C fresh Gate-7 auditor (Gate-6-standard pattern, written
for this gate; imports nothing from phase/gate scripts or verify_metric).
  * Verdict path: 2nd-order central FD for first AND second metric
    derivatives (diagonal (f+ -2f + f-)/h^2; cross 4-point /4h^2), then
    d(Gamma) computed ALGEBRAICALLY from dg, d2g, d(ginv) = -ginv dg ginv.
    No nested Gamma stencil.
  * Second path: 4th-order direct-d2 (5-point first/second derivative
    stencils; tensor-product for cross terms), d(Gamma) algebraic.
  * Eulerian Hawking-Ellis margins, Type-I classification, sampled-null
    NEC (Fibonacci directions), dense sampled minimum null contraction.
Stationary metrics only (dg[0] = d2[*][0] = 0). float64 everywhere.
Python: programme venv (numpy 2.5.5 / scipy 1.18.1).
"""
import numpy as np

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi


def _einstein_from_derivs(g, dg, d2):
    ginv = np.linalg.inv(g)
    dginv = [np.zeros_like(g) for _ in range(4)]
    for e in range(1, 4):
        dginv[e] = -np.einsum('...ad,...de,...eb->...ab', ginv, dg[e], ginv)
    Gamma = np.zeros(g.shape[:1] + (4, 4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.stack([dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                                 for d in range(4)], axis=-1)
                Gamma[..., a, b, c] = 0.5 * np.einsum('...d,...d->...', ginv[..., a, :], term)
    dGamma = [np.zeros_like(Gamma) for _ in range(4)]
    for e in range(1, 4):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = np.stack([dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                                   for d in range(4)], axis=-1)
                    dt = np.stack([d2[e][b][..., d, c] + d2[e][c][..., d, b] - d2[e][d][..., b, c]
                                   for d in range(4)], axis=-1)
                    dGamma[e][..., a, b, c] = 0.5 * (
                        np.einsum('...d,...d->...', dginv[e][..., a, :], t1)
                        + np.einsum('...d,...d->...', ginv[..., a, :], dt))
    Ricci = np.zeros(g.shape[:1] + (4, 4), dtype=DTYPE)
    for b_ in range(4):
        for d_ in range(4):
            v = np.zeros(g.shape[:1], dtype=DTYPE)
            for a in range(4):
                v += dGamma[a][..., a, b_, d_]
                v -= dGamma[d_][..., a, b_, a]
                for e in range(4):
                    v += Gamma[..., a, a, e] * Gamma[..., e, b_, d_]
                    v -= Gamma[..., a, d_, e] * Gamma[..., e, b_, a]
            Ricci[..., b_, d_] = v
    R = np.einsum('...ab,...ab->...', ginv, Ricci)
    return Ricci - 0.5 * R[..., None, None] * g


def einstein2(gfunc, pts, h):
    """2nd-order direct-d2 Einstein tensor (verdict path)."""
    pts = np.asarray(pts, dtype=DTYPE)
    g0 = gfunc(pts)
    gp = [None] * 3
    gm = [None] * 3
    for a in range(3):
        pp = pts.copy(); pp[:, a] += h
        pm = pts.copy(); pm[:, a] -= h
        gp[a] = gfunc(pp); gm[a] = gfunc(pm)
    dg = [np.zeros_like(g0) for _ in range(4)]
    for a in range(3):
        dg[a + 1] = (gp[a] - gm[a]) / (2.0 * h)
    d2 = [[np.zeros_like(g0) for _ in range(4)] for _ in range(4)]
    for a in range(3):
        d2[a + 1][a + 1] = (gp[a] - 2.0 * g0 + gm[a]) / (h * h)
    for a in range(3):
        for b in range(a + 1, 3):
            ppp = pts.copy(); ppp[:, a] += h; ppp[:, b] += h
            ppm = pts.copy(); ppm[:, a] += h; ppm[:, b] -= h
            pmp = pts.copy(); pmp[:, a] -= h; pmp[:, b] += h
            pmm = pts.copy(); pmm[:, a] -= h; pmm[:, b] -= h
            v = (gfunc(ppp) - gfunc(ppm) - gfunc(pmp) + gfunc(pmm)) / (4.0 * h * h)
            d2[a + 1][b + 1] = v; d2[b + 1][a + 1] = v
    return _einstein_from_derivs(g0, dg, d2), g0


C4 = np.array([1.0, -8.0, 0.0, 8.0, -1.0]) / 12.0
OFF = np.array([-2, -1, 0, 1, 2])


def einstein4(gfunc, pts, h):
    """4th-order direct-d2 Einstein tensor (second path)."""
    pts = np.asarray(pts, dtype=DTYPE)
    g0 = gfunc(pts)
    dg = [np.zeros_like(g0) for _ in range(4)]
    cache = {}
    for a in range(3):
        acc = np.zeros_like(g0)
        for k, o in enumerate(OFF):
            if o == 0:
                continue
            p = pts.copy(); p[:, a] += o * h
            cache[(a, int(o))] = gfunc(p)
            acc += C4[k] * cache[(a, int(o))]
        dg[a + 1] = acc / h
    d2 = [[np.zeros_like(g0) for _ in range(4)] for _ in range(4)]
    for a in range(3):
        fp2 = cache[(a, 2)]; fp1 = cache[(a, 1)]; fm1 = cache[(a, -1)]; fm2 = cache[(a, -2)]
        d2[a + 1][a + 1] = (-fp2 + 16 * fp1 - 30 * g0 + 16 * fm1 - fm2) / (12 * h * h)
    for a in range(3):
        for b in range(a + 1, 3):
            acc = np.zeros_like(g0)
            for ka, oa in enumerate(OFF):
                for kb, ob in enumerate(OFF):
                    if C4[ka] == 0 or C4[kb] == 0:
                        continue
                    p = pts.copy(); p[:, a] += oa * h; p[:, b] += ob * h
                    acc += C4[ka] * C4[kb] * gfunc(p)
            d2[a + 1][b + 1] = acc / (h * h); d2[b + 1][a + 1] = d2[a + 1][b + 1]
    return _einstein_from_derivs(g0, dg, d2), g0


def eulerian_that(g, Tcov):
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


def fib_dirs(n):
    i = np.arange(n, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


def null_min(That, dirs):
    """Min over given unit directions n of That_ab k^a k^b, k=(1,n)."""
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
    T00 = flat[:, 0, 0]; T0i = flat[:, 0, 1:]; Tij = flat[:, 1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
    vals = T00[:, None] + 2.0 * (T0i @ dirs.T) + quad
    return vals.min(axis=1)


def audit(gfunc, pts, h, order=2, chunk=169):
    """Full audit in chunks; returns margins dict + That + sampled_nec (162)."""
    pts = np.asarray(pts, dtype=DTYPE)
    ein = einstein2 if order == 2 else einstein4
    keys = ('rho', 'nec', 'wec', 'sec', 'dec', 'sampled_nec')
    acc = {k: [] for k in keys}
    acc['p'] = []
    acc['typeI'] = []
    acc['That'] = []
    dirs162 = fib_dirs(162)
    for s in range(0, len(pts), chunk):
        sub = pts[s:s + chunk]
        G, g = ein(gfunc, sub, h)
        That = eulerian_that(g, G / EIGHT_PI)
        m = margins_from_that(That)
        for k in ('rho', 'nec', 'wec', 'sec', 'dec'):
            acc[k].append(m[k])
        acc['p'].append(m['p'])
        acc['typeI'].append(m['typeI'])
        acc['That'].append(That)
        acc['sampled_nec'].append(null_min(That, dirs162))
    out = {k: np.concatenate(v) for k, v in acc.items()}
    return out
