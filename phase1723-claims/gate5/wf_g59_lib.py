#!/usr/bin/env python3
"""wf_g59_lib.py -- Gate-5 W-F INDEPENDENT machinery for G5-9 (P19-1).

Written fresh from the claim statement / run-record definitions.
Differences from the phase machinery (the independence):
 * principal sqrt S = sqrt(g^-1 f) via scipy.linalg.sqrtm per point
   (phase used a batched eigendecomposition);
 * Christoffel symbols from 2nd-order central FD of the metric
   (phase verify_metric used 4th-order stencils);
 * Einstein tensor from 2nd-order central FD of Gamma
   (phase used nested 4th-order stencils);
 * divergence nabla^a C_ab assembled directly from its definition
   div_b = d_a C^a_b + Gamma^a_{ad} C^d_b - Gamma^d_{ab} C^a_d;
 * Eulerian tetrad built here from the ADM split;
 * EC margins from my own mixed-tensor eigenvalue code; NEC at
   non-Type-I points by my own Fibonacci null-direction sampling;
   non-Type-I points count as WEC/SEC/DEC violations
   (Hawking-Ellis classification).
Shared DEFINITIONS only (allowed): the stored D1/D0 coefficient
vectors (p191_coeffs.npz), the bed's g-metric factory (shell.py /
p103_lib.bed -- the definition of the g configuration), the volume
point set (phase14 cache pts_v/r_v), the tolerance table
(p143_prep.json), collocation/fresh point seeds as registered in
the P19-1 run record. float64 everywhere.
"""
import sys
import numpy as np
from scipy.linalg import sqrtm

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase10')
import shell as sh          # noqa: E402  (definition of the g bed)

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
I4 = np.eye(4)
EIGHT_PI = 8.0 * np.pi


def dictionary(a3, a4):
    """Hassan-Rosen b_n dictionary (definition, from the claim)."""
    return np.array([12 + 24 * a3 + 24 * a4, -6 - 18 * a3 - 24 * a4,
                     2 + 12 * a3 + 24 * a4, -6 * a3 - 24 * a4,
                     24 * a4], dtype=np.float64)


def g_factory(beta):
    """The Finalist-A shell g metric (definition of the bed)."""
    prof = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    return sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 20.0])


def window_W(r):
    return sh.shift_S(np.asarray(r, dtype=np.float64), 10.0, 20.0,
                      'cos', 1.0, [10.0, 20.0])


# ---------------- f profiles from stored coefficients (definition) ----
def _legendre(u):
    return np.stack([np.ones_like(u), u, 0.5 * (3.0 * u**2 - 1.0)],
                    axis=-1)


def profiles_d1(pts, coeff):
    """D1: A,B,D of (r,u), 54 coeffs, layout p*18 + k*3 + j."""
    pts = np.atleast_2d(np.asarray(pts, dtype=np.float64))
    c = np.asarray(coeff, dtype=np.float64).reshape(3, 6, 3)
    r = np.linalg.norm(pts, axis=1)
    u = np.where(r > 0, pts[:, 0] / np.where(r > 0, r, 1.0), 0.0)
    W = window_W(r)
    k = np.arange(6, dtype=np.float64)
    rad = np.cos(np.outer(r - 9.0, k) * np.pi / 12.0)
    ang = _legendre(u)
    basis = rad[:, :, None] * ang[:, None, :]
    bg = np.array([1.0, 0.0, 1.0])
    vals = np.empty((len(pts), 3))
    for p in range(3):
        vals[:, p] = bg[p] + W * np.einsum('pkj,kj->p', basis, c[p])
    return vals


def profiles_d0(pts, coeff):
    """Radial (Phase-14) profiles: 18 coeffs, layout p*6 + k."""
    pts = np.atleast_2d(np.asarray(pts, dtype=np.float64))
    c = np.asarray(coeff, dtype=np.float64).reshape(3, 6)
    r = np.linalg.norm(pts, axis=1)
    W = window_W(r)
    k = np.arange(6, dtype=np.float64)
    basis = np.cos(np.outer(r - 9.0, k) * np.pi / 12.0)
    bg = np.array([1.0, 0.0, 1.0])
    return bg[None, :] + W[:, None] * (basis @ c.T)


def f_matrix(pts, prof):
    pts = np.atleast_2d(np.asarray(pts, dtype=np.float64))
    A, B, D = prof[:, 0], prof[:, 1], prof[:, 2]
    f = np.zeros((len(pts), 4, 4))
    f[:, 0, 0] = -A
    f[:, 0, 1] = f[:, 1, 0] = -B
    f[:, 1, 1] = D
    f[:, 2, 2] = D
    f[:, 3, 3] = D
    return f


# ---------------- bimetric tensor, my implementation -----------------
def sqrt_principal(M):
    """Principal sqrt of a single 4x4 via scipy sqrtm."""
    out = sqrtm(M.astype(np.complex128))
    return out[0] if isinstance(out, tuple) else out


def e_and_Y(S):
    """Elementary symmetric polys e_0..e_4 of S (batched, complex ok)
    and Y_0..Y_3 via the Cayley-Hamilton recursion."""
    S2 = S @ S
    S3 = S2 @ S
    t1 = np.trace(S, axis1=-2, axis2=-1)
    t2 = np.trace(S2, axis1=-2, axis2=-1)
    t3 = np.trace(S3, axis1=-2, axis2=-1)
    e1 = t1
    e2 = 0.5 * (t1**2 - t2)
    e3 = (t1**3 - 3.0 * t1 * t2 + 2.0 * t3) / 6.0
    e4 = np.linalg.det(S)
    e = np.stack([np.ones_like(e1), e1, e2, e3, e4], axis=-1)
    shp = S.shape
    Y0 = np.broadcast_to(I4.astype(S.dtype), shp).copy()
    Y1 = e1[..., None, None] * I4 - S
    Y2 = e2[..., None, None] * I4 - e1[..., None, None] * S + S2
    Y3 = (e3[..., None, None] * I4 - e2[..., None, None] * S
          + e1[..., None, None] * S2 - S3)
    return e, (Y0, Y1, Y2, Y3)


def C_tensor(g, f, m2, b):
    """C_mn = m2 [ sum_{n=1..4} b_n sym(f.A_n)_mn
                   - 1/2 (sum_n b_n e_n(S)) g_mn ],
    A_n = 1/2 Y_{n-1}(S) S^{-1}, S = sqrt(g^-1 f). Batched over
    points; sqrt per point via scipy."""
    g = np.asarray(g, dtype=np.float64)
    f = np.broadcast_to(np.asarray(f, dtype=np.float64), g.shape)
    P = g.shape[0]
    ginv = np.linalg.inv(g)
    M = ginv @ f
    S = np.empty((P, 4, 4), dtype=np.complex128)
    for i in range(P):
        S[i] = sqrt_principal(M[i])
    e, Y = e_and_Y(S)
    Sinv = np.linalg.inv(S)
    sym_sum = np.zeros((P, 4, 4), dtype=np.complex128)
    for n in range(1, 5):
        A = 0.5 * (Y[n - 1] @ Sinv)
        fA = f.astype(np.complex128) @ A
        sym_sum += b[n] * 0.5 * (fA + np.swapaxes(fA, -1, -2))
    Lfac = e @ np.asarray(b, dtype=np.complex128)
    C = m2 * (sym_sum - 0.5 * Lfac[:, None, None] * g)
    max_imag = float(np.max(np.abs(C.imag))) if P else 0.0
    return C.real, dict(max_imag_C=max_imag,
                        min_Re_evS=float(np.min(
                            np.linalg.eigvals(S).real)) if P else None)


def C_f_tensor(g, f, m2, b):
    """f-sector tensor per the claim: same functional, metrics
    swapped, b reversed."""
    return C_tensor(f, g, m2, np.asarray(b, dtype=np.float64)[::-1].copy())


# ---------------- my Christoffel / Einstein ---------------------------
def gamma_of(gfunc, pts, h):
    """Gamma^a_bc at pts: 2nd-order central FD metric derivatives
    (stationary: t-derivatives vanish)."""
    pts = np.asarray(pts, dtype=np.float64)
    g0 = gfunc(pts)
    ginv = np.linalg.inv(g0)
    dg = np.zeros((len(pts), 4, 4, 4))       # dg[d][mu][nu]
    for a in range(3):
        qp = pts.copy(); qp[:, a] += h
        qm = pts.copy(); qm[:, a] -= h
        dg[:, a + 1] = (gfunc(qp) - gfunc(qm)) / (2.0 * h)
    # Gamma^a_bc = 1/2 g^ad (d_b g_dc + d_c g_db - d_d g_bc),
    # dg[p, x, mu, nu] = d_x g_{mu nu}
    Gam = 0.5 * (np.einsum('pad,pbdc->pabc', ginv, dg)
                 + np.einsum('pad,pcdb->pabc', ginv, dg)
                 - np.einsum('pad,pdbc->pabc', ginv, dg))
    return Gam, g0, ginv


def einstein_of(gfunc, pts, h):
    """Einstein tensor at pts from Gamma and its 2nd-order FD."""
    pts = np.asarray(pts, dtype=np.float64)
    Gam, g0, ginv = gamma_of(gfunc, pts, h)
    Ric = np.zeros((len(pts), 4, 4))
    # R_bd = d_a Gamma^a_bd - d_d Gamma^a_ba + Gamma Gamma terms
    for e in range(3):
        qp = pts.copy(); qp[:, e] += h
        qm = pts.copy(); qm[:, e] -= h
        dG = (gamma_of(gfunc, qp, h)[0]
              - gamma_of(gfunc, qm, h)[0]) / (2.0 * h)   # d_{e+1} Gamma
        a = e + 1
        Ric += dG[:, a, :, :]                    # + d_a Gamma^a_{bd} (a=e+1 term)
        # - d_d Gamma^a_{b a}: only d = a contributes for this e
        Ric[:, :, a] -= np.einsum('paba->pb', dG)
    Ric += np.einsum('paae,pebd->pbd', Gam, Gam)
    Ric -= np.einsum('pade,peba->pbd', Gam, Gam)
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g0
    return G, g0


# ---------------- my Bianchi divergence -------------------------------
def divergence_rel(gfunc, Cfunc, pts, h):
    """rel_b = |nabla^a C_ab| / scale_b at pts, with
    scale = max(sum |three covariant terms|, sum_a |d_a C^a_b|)
    (the relative form stated in the claim record).
    Cfunc(pts) -> (P,4,4) covariant C (m2=1)."""
    pts = np.asarray(pts, dtype=np.float64)
    Gam, g0, ginv = gamma_of(gfunc, pts, h)
    C0 = Cfunc(pts)
    mix0 = np.einsum('pma,pab->pmb', ginv, C0)     # C^a_b
    d_axes = np.zeros((len(pts), 3, 4))            # d_a C^a_b per axis
    for a in range(3):
        qp = pts.copy(); qp[:, a] += h
        qm = pts.copy(); qm[:, a] -= h
        mp = np.einsum('pma,pab->pmb', np.linalg.inv(gfunc(qp)),
                       Cfunc(qp))
        mm = np.einsum('pma,pab->pmb', np.linalg.inv(gfunc(qm)),
                       Cfunc(qm))
        d_axes[:, a, :] = ((mp - mm) / (2.0 * h))[:, a + 1, :]
    term1 = d_axes.sum(axis=1)
    term2 = np.einsum('paad,pdb->pb', Gam, mix0)
    term3 = -np.einsum('pdab,pad->pb', Gam, mix0)
    div = term1 + term2 + term3
    scale = np.abs(term1) + np.abs(term2) + np.abs(term3)
    partial = np.sum(np.abs(d_axes), axis=1)
    scale = np.maximum(scale, partial)
    rel = np.abs(div) / np.maximum(scale, 1e-300)
    return rel, div, scale


# ---------------- my Eulerian frame + EC margins ----------------------
def eulerian_that(g, Tcov):
    """Eulerian orthonormal-frame stress-energy (ADM split, my code)."""
    g = np.asarray(g, dtype=np.float64)
    Tcov = np.asarray(Tcov, dtype=np.float64)
    gam = g[..., 1:, 1:]
    bcov = g[..., 0, 1:]
    ginv_sp = np.linalg.inv(gam)
    bup = np.einsum('...ij,...j->...i', ginv_sp, bcov)
    alpha = np.sqrt(np.maximum(
        -g[..., 0, 0] + np.einsum('...i,...i->...', bcov, bup), 1e-300))
    lam, V = np.linalg.eigh(gam)
    E = np.zeros(g.shape[:-2] + (4, 4))
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -bup / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = V[..., :, i] / np.sqrt(lam[..., i])[..., None]
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def _fib_dirs(n):
    i = np.arange(n, dtype=np.float64)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n)
    th = np.pi * (1.0 + np.sqrt(5.0)) * i
    return np.stack([np.cos(th) * np.sin(phi),
                     np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


def ec_margins(That, n_null=1024):
    """My Hawking-Ellis margins. Type-I: eigenvalue formulas.
    Non-Type-I: NEC by null sampling; WEC/SEC/DEC counted violated
    (margin set to the sampled NEC-like quantifier sign proxy:
    we use -|nec_sampled| - tiny, i.e. strictly negative)."""
    That = np.asarray(That, dtype=np.float64)
    flat = That.reshape(-1, 4, 4)
    Np = len(flat)
    M = flat.copy()
    M[:, 0, :] *= -1.0
    ev, evec = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(ev.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(ev.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evec) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k = np.argmax(cand, axis=1)
    ar = np.arange(Np)
    rho = np.where(typeI, -ev[ar, k].real, np.nan)
    mask = np.ones((Np, 4), dtype=bool)
    mask[ar, k] = False
    ps = np.where(typeI[:, None],
                  ev.real[mask].reshape(Np, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.min(rho[:, None] + ps, axis=1)
        wec = np.minimum(rho, nec)
        sec = np.minimum(nec, rho + np.sum(ps, axis=1))
        dec = np.minimum(rho, rho - np.max(np.abs(ps), axis=1))
    bad = ~typeI
    if np.any(bad):
        sub = flat[bad]
        dirs = _fib_dirs(n_null)
        nec_b = np.empty(len(sub))
        for i0 in range(0, len(sub), 64):
            s = sub[i0:i0 + 64]
            lin = 2.0 * (s[:, 0, 1:] @ dirs.T)
            tmp = np.tensordot(dirs, s[:, 1:, 1:], axes=([1], [1]))
            quad = (tmp * dirs[:, None, :]).sum(-1).T
            vals = s[:, 0, 0][:, None] + lin + quad
            nec_b[i0:i0 + 64] = np.min(vals, axis=1)
        nec[bad] = nec_b
        wec[bad] = np.minimum(nec_b, -1e-12)
        sec[bad] = np.minimum(nec_b, -1e-12)
        dec[bad] = -np.abs(nec_b) - 1e-12
    return dict(nec=nec, wec=wec, sec=sec, dec=dec, typeI=typeI,
                rho=rho, p=ps)


def vol_fracs(margins, r_v, tol):
    w = np.asarray(r_v, dtype=np.float64) ** 2
    w = w / np.sum(w)
    out = {}
    for n in ('nec', 'wec', 'sec', 'dec'):
        out[n] = float(np.sum(w[margins[n] < -tol]))
    out['typeI'] = float(np.sum(w[margins['typeI']]))
    return out
