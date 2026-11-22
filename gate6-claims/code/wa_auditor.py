"""
wa_auditor.py — Gate-6 W-A FRESH Einstein + EC auditor for G6-1.
Independent second path vs verify_metric.einstein_at_points:
  * verify_metric: 4th-order FD on metric -> Gamma at shifted points ->
    4th-order FD on Gamma (nested stencils).
  * HERE: 2nd-order central FD for FIRST and SECOND metric derivatives
    (d2 diagonal: (f+ -2f + f-)/h^2; cross: 4-point /4h^2), then
    d(Gamma) computed ALGEBRAICALLY from dg, d2g and d(ginv) =
    -ginv dg ginv. No nested Gamma stencil anywhere.
float64 everywhere. Imports NOTHING from verify_metric.
Metric definition imported from shell.py only (allowed, shared def).
"""
import numpy as np
DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi


def metric_derivs(gfunc, pts, h):
    """Return g (P,4,4), dg[e] (P,4,4) e=1..3 spatial (dg[0]=0),
    d2[e][f] (P,4,4) second spatial derivatives, e,f in 1..3."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = pts.shape[0]
    g0 = gfunc(pts)
    gp = [None]*3; gm = [None]*3
    for a in range(3):
        pp = pts.copy(); pp[:, a] += h
        pm = pts.copy(); pm[:, a] -= h
        gp[a] = gfunc(pp); gm[a] = gfunc(pm)
    dg = [np.zeros_like(g0) for _ in range(4)]
    for a in range(3):
        dg[a+1] = (gp[a] - gm[a]) / (2.0*h)
    d2 = [[np.zeros_like(g0) for _ in range(4)] for _ in range(4)]
    for a in range(3):
        d2[a+1][a+1] = (gp[a] - 2.0*g0 + gm[a]) / (h*h)
    for a in range(3):
        for b in range(a+1, 3):
            ppp = pts.copy(); ppp[:, a] += h; ppp[:, b] += h
            ppm = pts.copy(); ppm[:, a] += h; ppm[:, b] -= h
            pmp = pts.copy(); pmp[:, a] -= h; pmp[:, b] += h
            pmm = pts.copy(); pmm[:, a] -= h; pmm[:, b] -= h
            v = (gfunc(ppp) - gfunc(ppm) - gfunc(pmp) + gfunc(pmm)) / (4.0*h*h)
            d2[a+1][b+1] = v; d2[b+1][a+1] = v
    return g0, dg, d2


def einstein_at(gfunc, pts, h):
    """Einstein tensor G (P,4,4) covariant, stationary metric."""
    g, dg, d2 = metric_derivs(gfunc, pts, h)
    ginv = np.linalg.inv(g)
    # dginv[e] = -ginv dg[e] ginv
    dginv = [np.zeros_like(g) for _ in range(4)]
    for e in range(1, 4):
        dginv[e] = -np.einsum('...ad,...de,...eb->...ab', ginv, dg[e], ginv)
    # Gamma[a,b,c]
    Gamma = np.zeros(g.shape[:1] + (4, 4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.stack([dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                                 for d in range(4)], axis=-1)
                Gamma[..., a, b, c] = 0.5*np.einsum('...d,...d->...', ginv[..., a, :], term)
    # dGamma[e][a,b,c] for spatial e=1..3 (e=0 zero, stationarity)
    dGamma = [np.zeros_like(Gamma) for _ in range(4)]
    for e in range(1, 4):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = np.stack([dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                                   for d in range(4)], axis=-1)
                    dt = np.stack([d2[e][b][..., d, c] + d2[e][c][..., d, b] - d2[e][d][..., b, c]
                                   for d in range(4)], axis=-1)
                    dGamma[e][..., a, b, c] = 0.5*(
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
                    v += Gamma[..., a, a, e]*Gamma[..., e, b_, d_]
                    v -= Gamma[..., a, d_, e]*Gamma[..., e, b_, a]
            Ricci[..., b_, d_] = v
    R = np.einsum('...ab,...ab->...', ginv, Ricci)
    G = Ricci - 0.5*R[..., None, None]*g
    return G, g


def eulerian_that(g, Tcov):
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...', beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DTYPE)
    E[..., 0, 0] = 1.0/alpha
    E[..., 1:, 0] = -beta_up/alpha[..., None]
    for i in range(3):
        E[..., 1:, i+1] = V[..., :, i]/np.sqrt(lam[..., i])[..., None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5*(That + np.swapaxes(That, -1, -2))


def margins_from_that(That):
    """Hawking-Ellis eigenvalue margins, fresh implementation."""
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy(); M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8*scale
    ev2 = np.abs(evecs)**2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k_idx = np.argmax(cand, axis=1)
    ar = np.arange(Np)
    rho = np.where(typeI, -evals[ar, k_idx].real, np.nan)
    mask = np.ones((Np, 4), dtype=bool); mask[ar, k_idx] = False
    ps = np.where(typeI[:, None], evals.real[mask].reshape(Np, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None]+ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None]+ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None]+ps, axis=1),
                                         rho+np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho-np.max(np.abs(ps), axis=1)), np.nan)
    return {'rho': rho, 'p': ps, 'typeI': typeI, 'nec': nec, 'wec': wec,
            'sec': sec, 'dec': dec, 'rho_euler': flat[:, 0, 0]}


def sampled_nec_min(That, n_dir=162):
    """Min over Fibonacci null directions of That_ab k^a k^b, k=(1,n)."""
    flat = np.asarray(That, dtype=DTYPE).reshape(-1, 4, 4)
    i = np.arange(n_dir, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0*(i+0.5)/n_dir)
    th = np.pi*(1.0+5.0**0.5)*i
    dirs = np.stack([np.cos(th)*np.sin(phi), np.sin(th)*np.sin(phi), np.cos(phi)], axis=1)
    T00 = flat[:, 0, 0]; T0i = flat[:, 0, 1:]; Tij = flat[:, 1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
    vals = T00[:, None] + 2.0*(T0i @ dirs.T) + quad
    return vals.min(axis=1)


def audit(gfunc, pts, h):
    G, g = einstein_at(gfunc, pts, h)
    T = G/EIGHT_PI
    That = eulerian_that(g, T)
    m = margins_from_that(That)
    m['That'] = That
    m['sampled_nec'] = sampled_nec_min(That)
    return m
