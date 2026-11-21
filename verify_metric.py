"""
verify_metric.py — Warp Pilot Phase 0 judge.

Given a STATIONARY metric on a 3D Cartesian grid (float64), compute:
  * Einstein tensor G_munu and stress-energy T_munu = G_munu / (8 pi)   [G = c = 1]
  * Eulerian orthonormal-frame stress-energy That_ab (ADM tetrad)
  * Hawking-Ellis eigenvalue classification and NEC / WEC / SEC / DEC
    margins for ALL observers (eigenvalue method, NOT Eulerian-only).

This is a Python/NumPy re-implementation of the finite-difference logic
described in Helmerich et al. 2024 (WarpFactory, CQG 41, 095009): metric on a
grid -> finite-difference derivatives -> Christoffel -> Ricci -> Einstein ->
energy conditions. No MATLAB anywhere.

Conventions: signature (-,+,+,+), coordinates (t, x, y, z), stationary
(all t-derivatives zero). Geometric units G = c = 1: T has units 1/length^2.
Convert an energy density in J/m^3 to geometric 1/m^2 by multiplying by
G/c^4 = 8.262e-45 (approx). Mass density kg/m^3 -> geometric: G/c^2 = 7.426e-28 m/kg
times kg/m^3 gives 1/m^2.
"""
import numpy as np

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi


# ----------------------------------------------------------------------------
# Einstein tensor from a metric grid (finite differences, WarpFactory-style)
# ----------------------------------------------------------------------------

def grad_axis(arr, h, axis):
    """4th-order central derivative along `axis` (2nd-order at the 2-cell
    boundary layer, which callers mask out). WarpFactory uses 4th order."""
    base = np.gradient(arr, h, axis=axis, edge_order=2)
    a = np.moveaxis(arr, axis, 0)
    b = np.moveaxis(base, axis, 0)
    if a.shape[0] >= 5:
        b[2:-2] = (a[:-4] - 8.0 * a[1:-3] + 8.0 * a[3:-1] - a[4:]) / (12.0 * h)
    return np.moveaxis(b, 0, axis)


def einstein_from_grid(g, h):
    """g: (nx,ny,nz,4,4) float64 metric. h: uniform grid spacing (float).
    Returns G: (nx,ny,nz,4,4) Einstein tensor (covariant), same units as 1/h^2.
    Assumes stationarity: all partial_t derivatives are zero.
    """
    g = np.asarray(g, dtype=DTYPE)
    assert g.dtype == DTYPE
    nx, ny, nz = g.shape[:3]

    # first derivatives dg[a] = d g / d x^a, a=0..3 (a=0 -> zero)
    dg = [np.zeros_like(g) for _ in range(4)]
    for a, ax in ((1, 0), (2, 1), (3, 2)):
        dg[a] = grad_axis(g, h, ax)

    # NOTE: second derivatives of g enter through gradients of Gamma below;
    # no separate d2g array is needed.
    ginv = np.linalg.inv(g)

    # Christoffel Gamma^a_{bc}
    Gamma = np.zeros(g.shape[:3] + (4, 4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                # 0.5 g^{ad} (d_b g_{dc} + d_c g_{db} - d_d g_{bc})
                term = np.zeros(g.shape[:3] + (4,), dtype=DTYPE)
                for d in range(4):
                    term[..., d] = dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                Gamma[..., a, b, c] = 0.5 * np.einsum('...d,...d->...', ginv[..., a, :], term)

    # Ricci R_{bd} = d_a Gamma^a_{bd} - d_d Gamma^a_{ba}
    #                 + Gamma^a_{ae} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{ba}
    # Derivative terms accumulated one derivative direction at a time
    # (bounds memory: only one dGamma array alive at once).
    Ricci = np.zeros(g.shape[:3] + (4, 4), dtype=DTYPE)
    for e in range(4):
        if e == 0:
            continue  # stationary: d_t Gamma = 0, and neither Ricci term uses e=0 alone
        ax = e - 1
        dGe = grad_axis(Gamma, h, ax)  # dGe[...,a,b,c] = d_e Gamma^a_{bc}
        for b_ in range(4):
            for d_ in range(4):
                # + d_a Gamma^a_{bd} contributes when a == e
                Ricci[..., b_, d_] += dGe[..., e, b_, d_]
                # - d_d Gamma^a_{ba} contributes when d == e, summed over a
                if d_ == e:
                    for a in range(4):
                        Ricci[..., b_, d_] -= dGe[..., a, b_, a]
        del dGe
    for b_ in range(4):
        for d_ in range(4):
            val = Ricci[..., b_, d_]
            for a in range(4):
                for e in range(4):
                    val += (Gamma[..., a, a, e] * Gamma[..., e, b_, d_]
                            - Gamma[..., a, d_, e] * Gamma[..., e, b_, a])
            Ricci[..., b_, d_] = val

    Rscalar = np.einsum('...ab,...ab->...', ginv, Ricci)
    G = Ricci - 0.5 * Rscalar[..., None, None] * g
    return G


# ----------------------------------------------------------------------------
# Eulerian orthonormal frame and Hawking-Ellis energy conditions
# ----------------------------------------------------------------------------

def eulerian_that(g, Tcov):
    """Transform covariant stress-energy Tcov (...,4,4) to the Eulerian
    orthonormal frame defined by the ADM decomposition of g.
    Returns That (...,4,4): That[0,0] = Eulerian energy density,
    That[0,i] = momentum flux, That[i,j] = stresses.
    """
    g = np.asarray(g, dtype=DTYPE)
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...', beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))

    # spatial triad from eigendecomposition of gamma (symmetric pos. def.)
    lam, V = np.linalg.eigh(gamma)          # gamma = V diag(lam) V^T
    # frame matrix E^mu_{hat a}: columns are the orthonormal basis vectors
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DTYPE)
    E[..., 0, 0] = 1.0 / alpha              # e_hat0 = n = (1/alpha, -beta^i/alpha)
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = V[..., :, i] / np.sqrt(lam[..., i])[..., None]
    # That_ab = E^mu_a E^nu_b T_{mu nu}
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    # symmetrise (kill FD asymmetry noise at roundoff level only)
    That = 0.5 * (That + np.swapaxes(That, -1, -2))
    return That


def hawking_ellis_margins(That, do_fallback=True):
    """All-observer energy-condition margins from orthonormal-frame T.

    Returns dict of (...,) arrays:
      rho_eig, p1,p2,p3 (Type I eigen-pressure frame; NaN if not Type I),
      typeI (bool), nec, wec, sec, dec margins (>=0 means satisfied),
      plus sampled-fallback margins for non-Type-I points in nec_s etc.
    Margins are in the same units as That (geometric 1/length^2).
    Method: eigenvalues of the mixed tensor M^a_b = eta^{aa} That_ab.
    For Type I (one timelike eigenvector, real eigenvalues):
      NEC: rho + p_i >= 0 ; WEC: rho >= 0 and NEC ;
      SEC: rho + p_i >= 0 and rho + sum p_i >= 0 ;
      DEC: rho >= 0 and |p_i| <= rho.
    """
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy()
    M[:, 0, :] *= -1.0                       # M^a_b = eta^{aa} That_ab
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale

    # timelike eigenvector test: eta-norm of each eigenvector (columns)
    ev2 = np.abs(evecs) ** 2                  # (Np, comp, eigvec)
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
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)

    # Non-Type-I points: NEC/WEC/SEC/DEC fail by Hawking-Ellis classification
    # (Type II/III/IV cannot satisfy them except measure-zero Type II cases);
    # quantify with dense sampled contractions so the judge returns a scalar
    # margin everywhere. These points are flagged via 'typeI' == False.
    filled = np.zeros(Np, dtype=bool)
    if do_fallback and np.any(~typeI):
        sub = sampled_margins(flat[~typeI].reshape(-1, 4, 4))
        idx = np.where(~typeI)[0]
        nec[idx] = sub['nec_s']; wec[idx] = sub['wec_s']
        sec[idx] = sub['sec_s']; dec[idx] = sub['dec_s']
        filled[idx] = True

    out = {
        'rho_eig': rho.reshape(shp), 'p': ps.reshape(shp + (3,)),
        'typeI': typeI.reshape(shp), 'sampled_filled': filled.reshape(shp),
        'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
        'sec': sec.reshape(shp), 'dec': dec.reshape(shp),
        'rho_euler': That[..., 0, 0],
    }
    return out


def sampled_margins(That, n_dir=162, n_vel=6):
    """All-observer check by dense sampling of observer directions/velocities.
    Used (a) as cross-check of the eigenvalue method and (b) as the margin
    quantifier at non-Type-I points, where NEC/WEC/SEC/DEC fail by the
    Hawking-Ellis classification but a scalar margin is still needed.
    Chunked to bound memory. Returns min NEC/WEC/SEC contractions and a
    DEC margin (min over observers of the future-causality margin of
    Upsilon^a = -T^a_b V^b, normalised)."""
    i = np.arange(n_dir, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n_dir)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    dirs = np.stack([np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)          # (n_dir,3)
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    nec_min = np.empty(Np); wec_min = np.empty(Np)
    sec_min = np.empty(Np); dec_min = np.empty(Np)
    vels = np.linspace(0.0, 0.95, n_vel)
    CH = 8192
    for s0 in range(0, Np, CH):
        F = flat[s0:s0 + CH]
        T00 = F[:, 0, 0]; T0i = F[:, 0, 1:]; Tij = F[:, 1:, 1:]
        tr = np.trace(Tij, axis1=1, axis2=2)
        quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
        nec_min[s0:s0 + CH] = (T00[:, None] + 2.0 * (T0i @ dirs.T) + quad).min(axis=1)
        wm = np.full(F.shape[0], np.inf); sm = np.full(F.shape[0], np.inf)
        dm = np.full(F.shape[0], np.inf)
        Mm = F.copy(); Mm[:, 0, :] *= -1.0       # mixed T^a_b
        for v in vels:
            gam = 1.0 / np.sqrt(1.0 - v * v)
            wec_vals = gam ** 2 * (T00[:, None] + 2.0 * v * (T0i @ dirs.T) + v * v * quad)
            wm = np.minimum(wm, wec_vals.min(axis=1))
            trT = -T00 + tr
            sec_vals = wec_vals - 0.5 * trT[:, None] * gam ** 2 * (v * v - 1.0)
            sm = np.minimum(sm, sec_vals.min(axis=1))
            # DEC: Upsilon = -M . V, V = gam (1, v n)
            V = np.zeros((F.shape[0], n_dir, 4), dtype=DTYPE)
            V[:, :, 0] = gam
            V[:, :, 1:] = gam * v * dirs[None, :, :]
            Ups = -np.einsum('nab,nib->nia', Mm, V)
            q = Ups[:, :, 0] ** 2 - np.sum(Ups[:, :, 1:] ** 2, axis=2)
            nrm = 1.0 + np.sum(Ups ** 2, axis=2)
            val = np.where(Ups[:, :, 0] > 0, q / nrm, -np.abs(q) / nrm - 1.0)
            dm = np.minimum(dm, val.min(axis=1))
        wec_min[s0:s0 + CH] = wm; sec_min[s0:s0 + CH] = sm; dec_min[s0:s0 + CH] = dm
    return {'nec_s': nec_min.reshape(shp), 'wec_s': wec_min.reshape(shp),
            'sec_s': sec_min.reshape(shp), 'dec_s': dec_min.reshape(shp)}


def audit_metric(g, h):
    """Full pipeline: metric grid -> Einstein -> T -> Eulerian That ->
    Hawking-Ellis margins. Returns dict of arrays."""
    G = einstein_from_grid(g, h)
    T = G / EIGHT_PI
    That = eulerian_that(g, T)
    res = hawking_ellis_margins(That)
    res['G'] = G; res['T'] = T; res['That'] = That
    return res


def grid_margins_summary(g, h, mask=None, max_sample=20000):
    """Fast screening summary: scalar min margins over `mask` (default all
    points). Type-I points use eigenvalue margins; non-Type-I masked points
    are sampled on a subset of at most `max_sample` points (screening only —
    finalists get the full audit_metric). Returns dict of floats + That."""
    G = einstein_from_grid(g, h)
    T = G / EIGHT_PI
    That = eulerian_that(g, T)
    flat = That.reshape(-1, 4, 4)
    if mask is None:
        mflat = np.ones(flat.shape[0], dtype=bool)
    else:
        mflat = mask.reshape(-1)
    m = hawking_ellis_margins(That, do_fallback=False)
    tI = m['typeI'].reshape(-1)
    out = {}
    for k in ('nec', 'wec', 'sec', 'dec'):
        vals = m[k].reshape(-1)[mflat & tI]
        out['min_' + k] = float(np.nanmin(vals)) if vals.size else np.inf
    nonI = np.where(mflat & ~tI)[0]
    out['n_nonI_masked'] = int(nonI.size)
    if nonI.size:
        step = max(1, nonI.size // max_sample)
        sub = sampled_margins(flat[nonI[::step]])
        for k, kk in (('nec', 'nec_s'), ('wec', 'wec_s'), ('sec', 'sec_s'), ('dec', 'dec_s')):
            out['min_' + k] = float(min(out['min_' + k], np.min(sub[kk])))
    out['typeI_frac_masked'] = float(np.mean(tI[mflat])) if np.any(mflat) else float('nan')
    out['That'] = That
    out['margins'] = m
    return out


# ----------------------------------------------------------------------------
# Point-wise auditor: Einstein tensor at arbitrary points via nested local
# 4th-order stencils. Independent discretisation from the global grid path
# (no grid-resolution limit; stencil width h is a free accuracy parameter).
# gfunc: (P,3) float64 points -> (P,4,4) metric (stationary).
# ----------------------------------------------------------------------------

def _fd4(func, pts, h, axis):
    """4th-order first derivative of func along spatial `axis` at pts."""
    offs = []
    for k in (-2, -1, 1, 2):
        p = pts.copy(); p[:, axis] += k * h
        offs.append(func(p))
    return (offs[0] - 8.0 * offs[1] + 8.0 * offs[2] - offs[3]) / (12.0 * h)


def _gamma_at(gfunc, pts, h):
    g = gfunc(pts)
    ginv = np.linalg.inv(g)
    dg = [np.zeros_like(g) for _ in range(4)]
    for a in range(3):
        dg[a + 1] = _fd4(gfunc, pts, h, a)
    Gamma = np.zeros(pts.shape[:1] + (4, 4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.zeros(pts.shape[:1] + (4,), dtype=DTYPE)
                for d in range(4):
                    term[..., d] = dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c]
                Gamma[..., a, b, c] = 0.5 * np.einsum('...d,...d->...', ginv[..., a, :], term)
    return Gamma, g, ginv


def einstein_at_points(gfunc, pts, h=0.2, do_fallback=True):
    """Returns (G, That, margins dict) at the given (P,3) points."""
    pts = np.asarray(pts, dtype=DTYPE)
    Gamma, g, ginv = _gamma_at(gfunc, pts, h)

    def gamma_shift(axis, k):
        p = pts.copy(); p[:, axis] += k * h
        return _gamma_at(gfunc, p, h)[0]

    Ricci = np.zeros(pts.shape[:1] + (4, 4), dtype=DTYPE)
    for e in range(3):
        dGe = (gamma_shift(e, -2) - 8.0 * gamma_shift(e, -1)
               + 8.0 * gamma_shift(e, 1) - gamma_shift(e, 2)) / (12.0 * h)
        a_idx = e + 1
        for b_ in range(4):
            for d_ in range(4):
                Ricci[..., b_, d_] += dGe[..., a_idx, b_, d_]
                if d_ == a_idx:
                    for a in range(4):
                        Ricci[..., b_, d_] -= dGe[..., a, b_, a]
    for b_ in range(4):
        for d_ in range(4):
            for a in range(4):
                for e in range(4):
                    Ricci[..., b_, d_] += (Gamma[..., a, a, e] * Gamma[..., e, b_, d_]
                                           - Gamma[..., a, d_, e] * Gamma[..., e, b_, a])
    Rscalar = np.einsum('...ab,...ab->...', ginv, Ricci)
    G = Ricci - 0.5 * Rscalar[..., None, None] * g
    T = G / EIGHT_PI
    That = eulerian_that(g, T)
    margins = hawking_ellis_margins(That, do_fallback=do_fallback)
    return G, That, margins


if __name__ == '__main__':
    # Smoke test: Minkowski must give T = 0 (to FD roundoff) and Type I margins 0.
    N = 12
    ax = np.linspace(-5, 5, N, dtype=DTYPE)
    h = ax[1] - ax[0]
    g = np.zeros((N, N, N, 4, 4), dtype=DTYPE)
    g[..., 0, 0] = -1.0
    for i in range(1, 4):
        g[..., i, i] = 1.0
    r = audit_metric(g, h)
    print('Minkowski max|T| =', np.max(np.abs(r['T'])))
    print('Minkowski TypeI fraction =', np.mean(r['typeI']))
    print('Minkowski NEC margin range =', np.nanmin(r['nec']), np.nanmax(r['nec']))
