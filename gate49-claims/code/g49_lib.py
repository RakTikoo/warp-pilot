#!/usr/bin/env python3
"""
g49_lib.py -- Gate-49 machinery: INDEPENDENT
RE-JUDGEMENT OF THE PHASE 403 CLAIM SET.

ORGANISATION (used by no earlier deciding read):
brute-force CARTESIAN FINITE-DIFFERENCE differential
geometry. The metric field is assembled pointwise
from the stored profile VALUES only -- no lineage
derivative (S', S'', N', ...) is consumed anywhere
in this file. The Einstein tensor is formed from
centred differences of the metric on Cartesian
stencils at two step sizes with Richardson
extrapolation and a per-point error estimate.
The Eulerian frame and the Hawking-Ellis margins
are re-implemented here from their definitions;
the worst-null is computed by an exact
secular-equation solver for the quadratic on the
sphere, cross-checked against a dense Fibonacci
scan. Earlier organisations, for the record:
lineage = hand-derived radial formulas; Gate-43 =
Cartesian loops; Gate-45 = Cartesian AD jets /
einsum; Gate-46 = sympy symbolic spherical;
Gate-47 = sympy symbolic Cartesian with cse;
Gate-48 = spherical Taylor jets.

The object (definitions shared with the record --
the ansatz and the transport are the claim's own
definitions, re-stated here, not machinery):
  metric (t, x, y, z), stationary:
    g_tt = -N(r)^2,  g_tx = g_xt = -beta * S(r),
    g_ij = delta_ij + (M(r) - 1) n_i n_j,  n = x/r,
    beta = 1.1;  T = G / (8 pi).
  per-profile scaling (389): S -> muS * S,
    N -> muN * N, M -> 1 + muM * (M - 1) applied to
    H2's total profiles.
  pose transport (402 SS3): for pose [a', b'],
    W' = b' - a', lam = 10 / W',
    phi(r) = 10 + (r - a') * lam; the transported
    profile VALUE at pose radius r is the home
    value at phi(r) (values unrescaled); the
    metric at a pose point uses the pose point's
    own direction n.
  SET-244 read: 41 radial midpoint nodes over the
    pose band x 162 Fibonacci directions; joint =
    min(nec_min, dec_min) (402 Amendment 1);
    margins per the Hawking-Ellis definitions with
    the programme's sampled fallback at non-Type-I
    points (162 dirs, velocities linspace(0,.95,6)).

float64. Programme venv. WP root from env G49_WP.
"""
import os
import sys

import numpy as np
from scipy.optimize import brentq

WP = os.environ.get('G49_WP', '/home/hatch/workspace/warp-pilot')
os.environ.setdefault('P394_WP', WP)
os.environ.setdefault('P389_WP', WP)
for _p in (WP, f'{WP}/phase389/work', f'{WP}/phase394/work'):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import p394_lib as L394  # stored profile VALUES only

DTYPE = np.float64
BETA = 1.1
EIGHT_PI = 8.0 * np.pi

C395 = (0.601180962300002, 1.5934531363763935,
        4.887238651223381)
WINNER = (0.5000090643041506, 1.8999807308424006,
          4.892092241322827)
HOME = (10.0, 20.0)
POSE_W28 = (1.0, 29.0)
H2_PEAK_STORED = 0.8853484980534808
DEGEN_BAR = 0.4426742490267404


# ------------------------------------------------ profile value oracle
def home_values(triple, pts, clamp=False):
    """H2-total profile VALUES (S, N, M) at home
    points, under the per-profile scaling `triple`.
    Only components 0, 3, 6 of the lineage assembly
    are read; its derivative components are never
    touched by this gate."""
    pr = L394.profiles_at394(triple[0], triple[1],
                             triple[2],
                             np.asarray(pts, dtype=DTYPE),
                             clamp=clamp)
    return pr[0], pr[3], pr[6]


def pose_values(triple, pts, pose, clamp=False):
    """Transported profile VALUES at pose points:
    the home values at phi(r) along the same
    direction (402 SS3; values unrescaled)."""
    pts = np.asarray(pts, dtype=DTYPE)
    a, b = pose
    lam = 10.0 / (b - a)
    r = np.linalg.norm(pts, axis=1)
    u = 10.0 + (r - a) * lam
    pts_h = pts * (u / r)[:, None]
    return home_values(triple, pts_h, clamp=clamp)


# ------------------------------------------------ the metric field
def metric_from_values(S, N, M, pts):
    """g (...,4,4) from profile values at pts."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=-1)
    n = pts / r[..., None]
    P = pts.shape[:-1]
    g = np.zeros(P + (4, 4), dtype=DTYPE)
    g[..., 0, 0] = -N ** 2
    g[..., 0, 1] = g[..., 1, 0] = -BETA * S
    h = M - 1.0
    for i in range(3):
        for j in range(3):
            g[..., i + 1, j + 1] = (1.0 if i == j else 0.0) \
                + h * n[..., i] * n[..., j]
    return g


def metric_field(triple, pts, pose, clamp=False):
    S, N, M = pose_values(triple, pts, pose, clamp=clamp)
    return metric_from_values(S, N, M, pts)


def metric_field_synthetic(Sf, Nf, Mf, pts):
    """Metric from arbitrary radial functions
    (calibration path: trivial limit, Schwarzschild)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=-1)
    return metric_from_values(Sf(r), Nf(r), Mf(r), pts)


# ------------------------------------------------ FD Einstein tensor
# stencil offsets for centred 2nd-order differences
_OFF = [(0.0, 0.0, 0.0)]
for _a in range(3):
    for _s in (1.0, -1.0):
        _o = [0.0, 0.0, 0.0]; _o[_a] = _s; _OFF.append(tuple(_o))
for _a in range(3):
    for _b in range(_a + 1, 3):
        for _sa in (1.0, -1.0):
            for _sb in (1.0, -1.0):
                _o = [0.0, 0.0, 0.0]
                _o[_a] = _sa; _o[_b] = _sb; _OFF.append(tuple(_o))
OFFSETS = np.array(_OFF, dtype=DTYPE)   # (19, 3)


def _einstein_from_derivs(g0, D, DD):
    """Einstein tensor from the metric and its first
    and second spatial derivatives at each point.
    g0: (...,4,4); D: (...,3,4,4) spatial derivs;
    DD: (...,3,3,4,4). Time derivatives are zero
    (stationary). Pure index algebra, einsum form."""
    shp = g0.shape[:-2]
    ginv = np.linalg.inv(g0)
    # D4[a] = d_a g for a = 0..3 with D4[0] = 0
    D4 = np.zeros(shp + (4, 4, 4), dtype=DTYPE)
    D4[..., 1:, :, :] = D
    DD4 = np.zeros(shp + (4, 4, 4, 4), dtype=DTYPE)
    DD4[..., 1:, 1:, :, :] = DD
    # Christoffel Gam[l, m, n] = 1/2 ginv[l,s] (D4[m] g[s,n]
    #                            + D4[n] g[s,m] - D4[s] g[m,n])
    Gam = 0.5 * (np.einsum('...ls,...msn->...lmn', ginv, D4)
                 + np.einsum('...ls,...nsm->...lmn', ginv, D4)
                 - np.einsum('...ls,...smn->...lmn', ginv, D4))
    # d_a ginv[l,s] = -ginv[l,t] ginv[s,r] D4[a] g[t,r]
    dginv = -np.einsum('...lt,...sr,...atr->...als', ginv, ginv, D4)
    # d_a Gam[l,m,n]
    dGam = 0.5 * (
        np.einsum('...als,...msn->...almn', dginv, D4)
        + np.einsum('...als,...nsm->...almn', dginv, D4)
        - np.einsum('...als,...smn->...almn', dginv, D4)
        + np.einsum('...ls,...amsn->...almn', ginv, DD4)
        + np.einsum('...ls,...ansm->...almn', ginv, DD4)
        - np.einsum('...ls,...asmn->...almn', ginv, DD4))
    # Ricci R[m,n] = d_l Gam[l,n,m] - d_n Gam[l,l,m]
    #              + Gam[l,l,r] Gam[r,n,m] - Gam[l,n,r] Gam[r,l,m]
    Ric = (np.einsum('...llnm->...mn', dGam)
           - np.einsum('...nllm->...mn', dGam)
           + np.einsum('...llr,...rnm->...mn', Gam, Gam)
           - np.einsum('...lnr,...rlm->...mn', Gam, Gam))
    R = np.einsum('...mn,...mn->...', ginv, Ric)
    G = Ric - 0.5 * R[..., None, None] * g0
    return G


def einstein_fd(metric_fn, pts, h):
    """Einstein tensor at pts by centred differences
    of the metric field at step h (2nd order).
    metric_fn: (M,3) -> (M,4,4). Returns G (...,4,4)."""
    pts = np.asarray(pts, dtype=DTYPE)
    shp = pts.shape[:-1]
    flat = pts.reshape(-1, 3)
    npts = len(flat)
    stencil = (flat[:, None, :]
               + h * OFFSETS[None, :, :]).reshape(-1, 3)
    gall = metric_fn(stencil).reshape(npts, 19, 4, 4)
    g0 = gall[:, 0]
    D = np.zeros((npts, 3, 4, 4), dtype=DTYPE)
    DD = np.zeros((npts, 3, 3, 4, 4), dtype=DTYPE)
    # offset index map: 0 centre; 1..6 = +x,-x,+y,-y,+z,-z
    for a in range(3):
        gp = gall[:, 1 + 2 * a]; gm = gall[:, 2 + 2 * a]
        D[:, a] = (gp - gm) / (2.0 * h)
        DD[:, a, a] = (gp - 2.0 * g0 + gm) / h ** 2
    # mixed corners: offsets 7..18 in (a,b) pair order
    # (0,1),(0,2),(1,2); signs (+,+),(+,-),(-,+),(-,-)
    k = 7
    for a in range(3):
        for b in range(a + 1, 3):
            gpp = gall[:, k]; gpm = gall[:, k + 1]
            gmp = gall[:, k + 2]; gmm = gall[:, k + 3]
            DD[:, a, b] = DD[:, b, a] = \
                (gpp - gpm - gmp + gmm) / (4.0 * h ** 2)
            k += 4
    G = _einstein_from_derivs(g0, D, DD)
    return G.reshape(shp + (4, 4))


def T_at(triple, pts, pose, h=0.02, clamp=False,
         richardson=True):
    """Stress tensor T = G/(8pi) at pose points via
    the FD machinery. Returns (T, err) where err is
    the Richardson error indicator max |T(h/2)-T(h)|/3
    over components (None if richardson=False)."""
    pts = np.asarray(pts, dtype=DTYPE)
    fn = lambda P: metric_field(triple, P, pose, clamp=clamp)
    Gh = einstein_fd(fn, pts, h)
    if not richardson:
        return Gh / EIGHT_PI, None
    Gh2 = einstein_fd(fn, pts, h / 2.0)
    TR = (4.0 * Gh2 - Gh) / 3.0 / EIGHT_PI
    err = float(np.max(np.abs(Gh2 - Gh)) / 3.0 / EIGHT_PI)
    return TR, err


# ------------------------------------------------ Eulerian frame (definition)
def eulerian_that(g, T):
    """Eulerian orthonormal-frame That: ADM normal
    frame of g; spatial triad = eigendecomposition
    of gamma (the SAMPLER-M / eulerian_that frame
    association of the record; gamma's tangential
    eigenspace is exactly degenerate, so the triad
    inside it is rounding-determined -- the C-10
    convention). Implemented here from the
    definition."""
    g = np.asarray(g, dtype=DTYPE)
    gamma = g[..., 1:, 1:]
    bcov = g[..., 0, 1:]
    ginv_s = np.linalg.inv(gamma)
    bup = np.einsum('...ij,...j->...i', ginv_s, bcov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...',
                                       bcov, bup)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape, dtype=DTYPE)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -bup / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = V[..., :, i] \
            / np.sqrt(lam[..., i])[..., None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, T)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


# ------------------------------------------------ Hawking-Ellis margins
def _fib_dirs(npts):
    i = np.arange(npts, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


DIRS162 = _fib_dirs(162)

# SET-244 radial nodes at the home pose (control use)
R_NODES_HOME = 10.0 + (np.arange(41, dtype=DTYPE) + 0.5) * (10.0 / 41.0)


def pose_nodes(pose):
    a, b = pose
    return a + (np.arange(41, dtype=DTYPE) + 0.5) * ((b - a) / 41.0)


def sampled_margins(That):
    """The programme's sampled fallback margins at
    non-Type-I points (definition of the read):
    NEC by the (1, n) contraction over 162 dirs;
    WEC/SEC/DEC over velocities linspace(0, .95, 6).
    Re-implemented from the definition."""
    That = np.asarray(That, dtype=DTYPE)
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    dirs = DIRS162
    T00 = flat[:, 0, 0]; T0i = flat[:, 0, 1:]
    Tij = flat[:, 1:, 1:]
    tr = np.trace(Tij, axis1=1, axis2=2)
    quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
    nec_s = (T00[:, None] + 2.0 * (T0i @ dirs.T) + quad).min(axis=1)
    wm = np.full(Np, np.inf); sm = np.full(Np, np.inf)
    dm = np.full(Np, np.inf)
    Mm = flat.copy(); Mm[:, 0, :] *= -1.0
    for v in np.linspace(0.0, 0.95, 6):
        gam = 1.0 / np.sqrt(1.0 - v * v)
        wec_vals = gam ** 2 * (T00[:, None]
                               + 2.0 * v * (T0i @ dirs.T)
                               + v * v * quad)
        wm = np.minimum(wm, wec_vals.min(axis=1))
        trT = -T00 + tr
        sec_vals = wec_vals - 0.5 * trT[:, None] * gam ** 2 \
            * (v * v - 1.0)
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
    """Hawking-Ellis margins from orthonormal-frame
    That (definition): eigenvalues of the mixed
    tensor; Type I iff all eigenvalues real and
    exactly one timelike eigenvector. Type-I
    margins from (rho, p_i); non-Type-I margins
    from the sampled fallback. Returns dict of
    arrays: typeI, nec, wec, sec, dec, rho_eig, p,
    rho_euler."""
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy(); M[:, 0, :] *= -1.0
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
    bad = np.where(~typeI)[0]
    if bad.size:
        ns, ws, ss, ds = sampled_margins(flat[bad])
        nec[bad] = ns; wec[bad] = ws; sec[bad] = ss; dec[bad] = ds
    return {'typeI': typeI.reshape(shp),
            'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
            'sec': sec.reshape(shp), 'dec': dec.reshape(shp),
            'rho_eig': rho.reshape(shp),
            'p': ps.reshape(shp + (3,)),
            'rho_euler': That[..., 0, 0]}


# ------------------------------------------------ worst-null (exact)
def worst_null_exact(That):
    """Exact min over unit n of k^T That k, k = (1, n):
    the quadratic-on-the-sphere (trust-region)
    problem, solved by the secular equation on the
    branch lam > -lam_min(B), with the hard case
    handled by the eigenspace candidate; cross-
    checked against a dense Fibonacci scan + local
    polish. Returns (q_full, q_scan)."""
    That = np.asarray(That, dtype=DTYPE)
    T00 = float(That[0, 0]); f = That[0, 1:].astype(DTYPE)
    B = That[1:, 1:].astype(DTYPE)
    evals, evecs = np.linalg.eigh(B)
    c = evecs.T @ f                      # f in B's eigenbasis
    lam_min = float(evals[0])

    def n_of(lam):
        return -evecs @ (c / (evals + lam))

    def norm2(lam):
        return float(np.sum((c / (evals + lam)) ** 2))

    cands = []
    # regular branch: |n(lam)| = 1 with lam > -lam_min
    lo = -lam_min + 1e-12
    if norm2(lo) > 1.0:
        hi = lo + 1.0
        while norm2(hi) > 1.0:
            hi = lo + 2.0 * (hi - lo)
        lam_star = brentq(lambda L: norm2(L) - 1.0, lo, hi,
                          xtol=1e-15, rtol=1e-14)
        cands.append(n_of(lam_star))
    else:
        # hard case: minimiser in the lam_min eigenspace
        # plus the particular solution at lam = -lam_min
        n_part = -evecs[:, 1:] @ (c[1:] / (evals[1:] + lam_min))
        rem = 1.0 - float(n_part @ n_part)
        if rem >= 0.0:
            for sgn in (1.0, -1.0):
                cands.append(n_part
                             + sgn * np.sqrt(rem) * evecs[:, 0])
        cands.append(n_part / max(np.linalg.norm(n_part), 1e-300))
    # interior stationary point of the equality problem
    # is covered by the secular branch; also test the
    # unconstrained-on-sphere antipode candidates
    best = np.inf; n_best = None
    for n in cands:
        nn = np.linalg.norm(n)
        if nn == 0:
            continue
        n = n / nn
        q = T00 + 2.0 * float(f @ n) + float(n @ B @ n)
        if q < best:
            best, n_best = q, n
    # dense scan cross-check (independent lattice size)
    dirs = _fib_dirs(8192)
    qs = T00 + 2.0 * (dirs @ f) \
        + np.einsum('ni,ij,nj->n', dirs, B, dirs)
    i0 = int(np.argmin(qs))
    q_scan = float(qs[i0])
    # local polish of the scan winner (parabolic steps
    # on the sphere via tangent moves)
    n = dirs[i0].copy()
    step = 0.05
    while step > 1e-13:
        improved = False
        for a in range(3):
            for sgn in (1.0, -1.0):
                t = np.zeros(3); t[a] = sgn * step
                t = t - (t @ n) * n
                nt = np.linalg.norm(t)
                if nt == 0:
                    continue
                cand = n + t
                cand /= np.linalg.norm(cand)
                q = T00 + 2.0 * float(f @ cand) \
                    + float(cand @ B @ cand)
                if q < q_scan:
                    q_scan, n = q, cand
                    improved = True
        if not improved:
            step /= 2.0
    return float(best), float(q_scan)


# ------------------------------------------------ SET-244 read
def set_read(triple, pose, h=0.02, clamp=False,
             richardson=True):
    """Gate-49's SET-244 read at a pose: 41 radial
    midpoint nodes x 162 Fibonacci dirs; T by the FD
    machinery (batched over all stencil points);
    margins by the gate's implementation. Returns
    (out, aux) with aux holding per-point arrays."""
    nodes = pose_nodes(pose)
    pts = np.concatenate([DIRS162 * rr for rr in nodes])
    fn = lambda P: metric_field(triple, P, pose, clamp=clamp)
    Gh = einstein_fd(fn, pts, h)
    if richardson:
        Gh2 = einstein_fd(fn, pts, h / 2.0)
        T = (4.0 * Gh2 - Gh) / 3.0 / EIGHT_PI
        err = float(np.max(np.abs(Gh2 - Gh)) / 3.0 / EIGHT_PI)
    else:
        T = Gh / EIGHT_PI
        err = None
    g = metric_field(triple, pts, pose, clamp=clamp)
    That = eulerian_that(g, T)
    m = margins(That)
    R = {k: m[k] for k in ('typeI', 'nec', 'wec', 'dec', 'sec')}
    R['rho'] = m['rho_euler']

    def st(arr):
        return {'min': float(np.min(arr)),
                'median': float(np.median(arr)),
                'max': float(np.max(arr))}
    i_nec = int(np.argmin(R['nec']))
    i_dec = int(np.argmin(R['dec']))
    i_r, i_d = divmod(i_nec, 162)
    j_r, j_d = divmod(i_dec, 162)
    out = {
        'pose': [float(pose[0]), float(pose[1])],
        'n_points': int(len(R['typeI'])),
        'typeI_fraction': float(np.mean(R['typeI'])),
        'typeI_count': int(np.sum(R['typeI'])),
        'nec': st(R['nec']), 'wec': st(R['wec']),
        'dec': st(R['dec']), 'sec': st(R['sec']),
        'rho': st(R['rho']),
        'joint': float(min(R['nec'].min(), R['dec'].min())),
        'nec_argmin_point': (DIRS162[i_d] * nodes[i_r]).tolist(),
        'nec_argmin_r': float(nodes[i_r]),
        'dec_argmin_point': (DIRS162[j_d] * nodes[j_r]).tolist(),
        'dec_argmin_r': float(nodes[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
        'nec_argmin_typeI': bool(R['typeI'][i_nec]),
        'fd_err_indicator': err,
        'h': h,
    }
    aux = {'R': R, 'That': That, 'pts': pts, 'nodes': nodes,
           'margins_full': m}
    return out, aux


def that_at(triple, pose, pt, h=0.02, clamp=False):
    """That at one named pose point (FD machinery,
    Richardson). Returns (That, err)."""
    pt = np.asarray(pt, dtype=DTYPE).reshape(1, 3)
    T, err = T_at(triple, pt, pose, h=h, clamp=clamp)
    g = metric_field(triple, pt, pose, clamp=clamp)
    return eulerian_that(g, T)[0], err


def nec_typeI_at(triple, pose, pt, h=0.02, clamp=False):
    """(nec margin, typeI) at a named point, gate
    machinery; nec is the eigenvalue margin at
    Type-I points and the sampled margin otherwise."""
    That, err = that_at(triple, pose, pt, h=h, clamp=clamp)
    m = margins(That[None])
    return float(m['nec'][0]), bool(m['typeI'][0]), That, err
