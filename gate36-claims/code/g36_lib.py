#!/usr/bin/env python3
"""
g36_lib.py -- Gate-36 Worker A INDEPENDENT assembly for the
pointwise member (CTRL-T1 / CTRL-T2, Item 1).

Written from the pose definitions in the Gate-36 charge only.
No import of p312_lib, verify_metric, or any gate34/gate35
library for any computation.

Route
-----
* Profiles S(r), N(r), M(r) implemented directly from their
  definitions, with analytic first and second derivatives.
* Einstein tensor: sympy jet assembly in spherical
  coordinates (t, r, theta, phi) with the polar axis along
  the shift direction x-hat.  With x = r cos(theta) the
  Cartesian shift covector g_ti = (-beta*S, 0, 0) pulls back
  to g_tr = -beta*S*cos(theta), g_tth = +r*beta*S*sin(theta),
  and gamma = M dr^2 + r^2 dOmega^2, g_tt = -N(r)^2.
  S, N, M enter as undefined sympy functions of r; the
  inverse metric is written in its analytic ADM form and
  asserted against g symbolically; Christoffel / Ricci /
  Einstein are formed symbolically, profile derivatives are
  substituted by jet symbols, and the result is lambdified.
  T_req = G / (8 pi), transformed spherical -> Cartesian by
  T_cart = J^{-T} T_sph J^{-1}.
* Eulerian frame (That): own ADM tetrad per the registered
  convention -- lapse alpha^2 = -g_tt + beta_cov . beta_up
  with beta_cov = g[0,1:], beta_up = gamma^{-1} beta_cov;
  e_0 = (1/alpha, -beta_up/alpha); spatial triad from
  np.linalg.eigh(gamma), columns V[:,i]/sqrt(lambda_i).
  That_ab = E^mu_a E^nu_b T_mu_nu, symmetrised.
* Cross-check: a fully separate Cartesian finite-difference
  Einstein computation (FD of the numeric metric, Richardson
  extrapolated) -- fd_T_req().
* Worst-null NEC: own fibonacci-sphere scan (642 points)
  plus Nelder-Mead polish on the best seeds.
* Segre / Hawking-Ellis Type-I: own eigenvalue test on
  eta . That.
float64 throughout.
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize
from scipy.special import betainc

BETA = 1.1
A_LAPSE = 0.07439108177516472
EIGHT_PI = 8.0 * np.pi

# ---------------------------------------------------------------- profiles
def S_funcs(r):
    """S = 1 - I_u(3,3), u=(r-10)/10 on [10,20]; 1 below, 0 above.
    Returns (S, S', S'').  B(3,3)=1/30 so
    S' = -u^2 (1-u)^2 / (10 B) = -3 u^2 (1-u)^2,
    S'' = -0.6 u (1-u) (1-2u)  (differentiating S')."""
    r = np.asarray(r, dtype=np.float64)
    S = np.where(r >= 20.0, 0.0, 1.0)
    Sp = np.zeros_like(r); Spp = np.zeros_like(r)
    mid = (r > 10.0) & (r < 20.0)
    if np.any(mid):
        u = (r[mid] - 10.0) / 10.0
        S[mid] = 1.0 - betainc(3.0, 3.0, u)
        Sp[mid] = -3.0 * u**2 * (1.0 - u)**2
        Spp[mid] = -0.6 * u * (1.0 - u) * (1.0 - 2.0 * u)
    return S, Sp, Spp


def _H(t):
    """H(t) = 10t^3-15t^4+6t^5 on (0,1), 0 below, 1 above.
    Returns (H, H', H'')."""
    t = np.asarray(t, dtype=np.float64)
    H = np.where(t >= 1.0, 1.0, 0.0)
    Hp = np.zeros_like(t); Hpp = np.zeros_like(t)
    mid = (t > 0.0) & (t < 1.0)
    if np.any(mid):
        x = t[mid]
        H[mid] = 10*x**3 - 15*x**4 + 6*x**5
        Hp[mid] = 30*x**2 - 60*x**3 + 30*x**4
        Hpp[mid] = 60*x - 180*x**2 + 120*x**3
    return H, Hp, Hpp


def N_funcs(r):
    """N = 1 + A*B(r), B = H((r-10)/3) * H((20-r)/3).
    Returns (N, N', N'')."""
    r = np.asarray(r, dtype=np.float64)
    H1, H1p, H1pp = _H((r - 10.0) / 3.0)
    H2, H2p, H2pp = _H((20.0 - r) / 3.0)
    B = H1 * H2
    Bp = H1p * H2 / 3.0 - H1 * H2p / 3.0
    Bpp = (H1pp * H2 / 9.0 - 2.0 * H1p * H2p / 9.0
           + H1 * H2pp / 9.0)
    return 1.0 + A_LAPSE * B, A_LAPSE * Bp, A_LAPSE * Bpp


def _ss(x):
    """Quintic smoothstep SS(x)=6x^5-15x^4+10x^3 and derivatives."""
    return (6.0*x**5 - 15.0*x**4 + 10.0*x**3,
            30.0*x**4 - 60.0*x**3 + 30.0*x**2,
            120.0*x**3 - 180.0*x**2 + 60.0*x)


def _U(r, a, b):
    """U(r;a,b) = SS((r-a)/(b-a)) on [a,b]; 0 below, 1 above."""
    r = np.asarray(r, dtype=np.float64)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r); Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss(x)
        U[mid] = v
        Up[mid] = vp / (b - a)
        Upp[mid] = vpp / (b - a)**2
    return U, Up, Upp


def M_funcs(r):
    """M = 1 + 4.00*[U(r;9,20.5) - U(r;21,24)]."""
    U1, U1p, U1pp = _U(r, 9.0, 20.5)
    U2, U2p, U2pp = _U(r, 21.0, 24.0)
    return (1.0 + 4.0 * (U1 - U2), 4.0 * (U1p - U2p),
            4.0 * (U1pp - U2pp))


def profiles(r):
    """(S,Sp,Spp, N,Np,Npp, M,Mp,Mpp) at radii r."""
    S, Sp, Spp = S_funcs(r)
    N, Np, Npp = N_funcs(r)
    M, Mp, Mpp = M_funcs(r)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


# ------------------------------------------------------- Cartesian metric
def metric_cart(pt):
    """g_mu_nu (4x4) at one Cartesian point, from the pose."""
    pt = np.asarray(pt, dtype=np.float64)
    r = np.linalg.norm(pt)
    n = pt / r
    (S, _, _, N, _, _, M, _, _) = [float(v[0]) for v in
                                  profiles(np.array([r]))]
    g = np.zeros((4, 4))
    g[0, 0] = -N**2
    g[0, 1] = g[1, 0] = -BETA * S
    g[1:, 1:] = np.eye(3) + (M - 1.0) * np.outer(n, n)
    return g


# ------------------------------------------- sympy spherical Einstein jet
_GF = None


def _build_G_funcs():
    r, th = sp.symbols('r theta')
    beta = sp.symbols('beta')
    Sf = sp.Function('S')(r); Nf = sp.Function('N')(r)
    Mf = sp.Function('M')(r)
    c, s = sp.cos(th), sp.sin(th)
    g = sp.zeros(4, 4)
    g[0, 0] = -Nf**2
    g[0, 1] = g[1, 0] = -beta * Sf * c
    g[0, 2] = g[2, 0] = r * beta * Sf * s
    g[1, 1] = Mf; g[2, 2] = r**2; g[3, 3] = r**2 * s**2
    # Analytic ADM inverse: alpha^2 = N^2 + beta^2 S^2 (cos^2/M + sin^2),
    # shift vector beta^r = -beta S cos/M, beta^th = +beta S sin/r.
    al2 = Nf**2 + beta**2 * Sf**2 * (c**2 / Mf + s**2)
    br, bt = -beta * Sf * c / Mf, beta * Sf * s / r
    gi = sp.zeros(4, 4)
    gi[0, 0] = -1 / al2
    gi[0, 1] = gi[1, 0] = br / al2
    gi[0, 2] = gi[2, 0] = bt / al2
    gi[1, 1] = 1 / Mf - br**2 / al2
    gi[2, 2] = 1 / r**2 - bt**2 / al2
    gi[1, 2] = gi[2, 1] = -br * bt / al2
    gi[3, 3] = 1 / (r**2 * s**2)
    assert sp.simplify(g * gi - sp.eye(4)) == sp.zeros(4, 4)
    coords = [None, r, th, None]
    dg = {}
    for mu in (1, 2):
        for a in range(4):
            for b in range(4):
                dg[(mu, a, b)] = sp.diff(g[a, b], coords[mu])

    def DG(mu, a, b):
        return dg.get((mu, a, b), sp.Integer(0))

    Gam = {}
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                e = 0
                for q in range(4):
                    e += gi[mu, q] * (DG(a, q, b) + DG(b, q, a)
                                      - DG(q, a, b))
                Gam[(mu, a, b)] = e / 2
    dG = {}
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                for cc in (1, 2):
                    dG[(cc, mu, a, b)] = sp.diff(Gam[(mu, a, b)],
                                                 coords[cc])
    Ric = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            e = 0
            for mu in range(4):
                e += dG.get((mu, mu, b, a), 0)
                if b in (1, 2):
                    e -= dG[(b, mu, mu, a)]
                for q in range(4):
                    e += (Gam[(mu, mu, q)] * Gam[(q, b, a)]
                          - Gam[(mu, b, q)] * Gam[(q, mu, a)])
            Ric[a, b] = e
    Rs = sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4))
    G = Ric - Rs * g / 2
    subs = {}
    for nm, f in (('S', Sf), ('N', Nf), ('M', Mf)):
        subs[sp.Derivative(f, (r, 2))] = sp.Symbol(nm + 'pp')
        subs[sp.Derivative(f, r)] = sp.Symbol(nm + 'p')
        subs[f] = sp.Symbol(nm)
    arglist = [r, th, beta] + [subs[k] for k in (
        Sf, sp.Derivative(Sf, r), sp.Derivative(Sf, (r, 2)),
        Nf, sp.Derivative(Nf, r), sp.Derivative(Nf, (r, 2)),
        Mf, sp.Derivative(Mf, r), sp.Derivative(Mf, (r, 2)))]
    out = {}
    for (a, b) in [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2),
                   (2, 2), (3, 3)]:
        out[(a, b)] = sp.lambdify(arglist, G[a, b].subs(subs),
                                  modules='numpy', cse=True)
    return out


def _G_funcs():
    global _GF
    if _GF is None:
        _GF = _build_G_funcs()
    return _GF


def T_and_g_cart(pts):
    """(T_req_cov, g) Cartesian at pts (N,3) from the sympy jet."""
    pts = np.asarray(pts, dtype=np.float64)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    th = np.arccos(np.clip(n[:, 0], -1.0, 1.0))
    ph = np.arctan2(n[:, 2], n[:, 1])
    prof = profiles(r)
    gf = _G_funcs()
    args = [r, th, np.full(P, BETA)] + [np.asarray(v, dtype=np.float64)
                                        for v in prof]
    Ts = np.zeros((P, 4, 4))
    for (a, b), f in gf.items():
        val = np.broadcast_to(np.asarray(f(*args), dtype=np.float64),
                              (P,)) / EIGHT_PI
        Ts[:, a, b] = val; Ts[:, b, a] = val
    st, ct = np.sin(th), np.cos(th)
    sph_, cph = np.sin(ph), np.cos(ph)
    eth = np.stack([-st, ct * cph, ct * sph_], axis=1)
    eph = np.stack([np.zeros(P), -sph_, cph], axis=1)
    J = np.zeros((P, 4, 4))
    J[:, 0, 0] = 1.0
    J[:, 1:, 1] = n
    J[:, 1:, 2] = r[:, None] * eth
    J[:, 1:, 3] = (r * st)[:, None] * eph
    Ji = np.linalg.inv(J)
    T = np.einsum('pia,pij,pjb->pab', Ji, Ts, Ji)
    T = 0.5 * (T + np.swapaxes(T, -1, -2))
    g = np.array([metric_cart(p) for p in pts])
    return T, g


# ------------------------------------------------------------- ADM tetrad
def eulerian_that(g, T):
    """That_ab = E^mu_a E^nu_b T_mu_nu with the registered ADM
    tetrad.  g, T: (...,4,4).  Returns (...,4,4)."""
    g = np.asarray(g, dtype=np.float64)
    T = np.asarray(T, dtype=np.float64)
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    beta_up = np.linalg.solve(gamma, beta_cov[..., None])[..., 0]
    alpha2 = -g[..., 0, 0] + np.sum(beta_cov * beta_up, axis=-1)
    alpha = np.sqrt(alpha2)
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros_like(g)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    # spatial triad: columns V[:,i]/sqrt(lam_i), as 4-vectors
    E[..., 1:, 1:] = V / np.sqrt(lam)[..., None, :]
    That = np.einsum('...ma,...mn,...nb->...ab', E, T, E)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def That_at(pts):
    T, g = T_and_g_cart(pts)
    return eulerian_that(g, T)


# ------------------------------------------------- FD Einstein cross-check
def _gamma_fd(pt, h):
    """Christoffel Gamma^l_{mu nu} at pt by central FD (spatial
    derivatives only; metric stationary)."""
    g0 = metric_cart(pt)
    ginv = np.linalg.inv(g0)
    dg = np.zeros((4, 4, 4))  # dg[k, mu, nu], k = spatial dir 0..2 -> coord k+1
    for k in range(3):
        dp = np.zeros(3); dp[k] = h
        dg[k] = (metric_cart(pt + dp) - metric_cart(pt - dp)) / (2 * h)
    Gam = np.zeros((4, 4, 4))
    for l in range(4):
        for mu in range(4):
            for nu in range(4):
                e = 0.0
                for s in range(4):
                    # d_mu g_{s nu}: nonzero only if mu spatial
                    d1 = dg[mu - 1, s, nu] if mu >= 1 else 0.0
                    d2 = dg[nu - 1, s, mu] if nu >= 1 else 0.0
                    d3 = dg[s - 1, mu, nu] if s >= 1 else 0.0
                    e += ginv[l, s] * (d1 + d2 - d3)
                Gam[l, mu, nu] = 0.5 * e
    return Gam


def _einstein_fd_h(pt, h):
    Gam0 = _gamma_fd(pt, h)
    dGam = np.zeros((3, 4, 4, 4))  # dGam[k, l, mu, nu] = d_k Gamma^l_{mu nu}
    for k in range(3):
        dp = np.zeros(3); dp[k] = h
        dGam[k] = (_gamma_fd(pt + dp, h) - _gamma_fd(pt - dp, h)) / (2 * h)
    Ric = np.zeros((4, 4))
    for mu in range(4):
        for nu in range(4):
            e = 0.0
            for l in range(4):
                # d_lambda Gamma^lambda_{nu mu}: lambda spatial only
                if l >= 1:
                    e += dGam[l - 1, l, nu, mu]
                # - d_nu Gamma^lambda_{lambda mu}
                if nu >= 1:
                    e -= dGam[nu - 1, l, l, mu]
                for s in range(4):
                    e += (Gam0[l, l, s] * Gam0[s, nu, mu]
                          - Gam0[l, nu, s] * Gam0[s, l, mu])
            Ric[mu, nu] = e
    g0 = metric_cart(pt)
    ginv = np.linalg.inv(g0)
    Rs = np.sum(ginv * Ric)
    G = Ric - 0.5 * Rs * g0
    return G / EIGHT_PI


def fd_T_req(pt):
    """Richardson-extrapolated FD T_req at one point, and the
    two raw levels, for the truncation-class comparison."""
    pt = np.asarray(pt, dtype=np.float64)
    T1 = _einstein_fd_h(pt, 2e-3)
    T2 = _einstein_fd_h(pt, 1e-3)
    Text = (4.0 * T2 - T1) / 3.0
    return Text, T1, T2


# ------------------------------------------------------- NEC / Segre reads
def fib_dirs(n=642):
    """Own fibonacci-sphere unit directions."""
    i = np.arange(n, dtype=np.float64)
    ga = np.pi * (3.0 - np.sqrt(5.0))
    y = 1.0 - 2.0 * (i + 0.5) / n
    rad = np.sqrt(np.maximum(0.0, 1.0 - y**2))
    th = ga * i
    return np.stack([np.cos(th) * rad, y, np.sin(th) * rad], axis=1)


def tkk_of_dir(That, d):
    d = np.asarray(d, dtype=np.float64)
    return float(That[0, 0] + 2.0 * That[0, 1:] @ d
                 + d @ That[1:, 1:] @ d)


def worst_null(That):
    """Exact pointwise NEC minimum: fib-642 scan + Nelder-Mead
    polish (angles) from the best scan seeds.  Returns
    (nec_min, kstar_hat (4,), fib642_min)."""
    dirs = fib_dirs(642)
    vals = (That[0, 0] + 2.0 * dirs @ That[0, 1:]
            + np.einsum('ni,ij,nj->n', dirs, That[1:, 1:], dirs))
    fib_min = float(np.min(vals))
    order = np.argsort(vals)[:6]

    def neg_obj(ang):
        th, ph = ang
        d = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph),
                      np.cos(th)])
        return tkk_of_dir(That, d)

    best = (fib_min, dirs[int(order[0])])
    for idx in order:
        d0 = dirs[int(idx)]
        th0 = np.arccos(np.clip(d0[2], -1, 1)); ph0 = np.arctan2(d0[1], d0[0])
        res = minimize(neg_obj, [th0, ph0], method='Nelder-Mead',
                       options={'xatol': 1e-13, 'fatol': 1e-16,
                                'maxiter': 2000})
        if res.fun < best[0]:
            th, ph = res.x
            d = np.array([np.sin(th) * np.cos(ph),
                          np.sin(th) * np.sin(ph), np.cos(th)])
            best = (float(res.fun), d)
    k = np.concatenate([[1.0], best[1]])
    return best[0], k, fib_min


def segre_typeI(That):
    """Own Hawking-Ellis test on eta . That (mixed tensor
    T^a_b = eta^{aa} That_ab): Type I iff the spectrum is
    real, the tensor is diagonalisable, and one eigenvector
    is timelike.  Returns (is_typeI, info dict)."""
    eta = np.diag([-1.0, 1.0, 1.0, 1.0])
    mixed = eta @ That
    w, V = np.linalg.eig(mixed)
    scale = max(1.0, float(np.max(np.abs(w))))
    max_imag = float(np.max(np.abs(np.imag(w)))) / scale
    real_spectrum = max_imag < 1e-10
    info = {'eigs': [[float(z.real), float(z.imag)] for z in w],
            'max_abs_imag_scaled': max_imag}
    if not real_spectrum:
        info['type'] = 'IV (complex pair)'
        return False, info
    # diagonalisable: eigenvectors span (cond finite & rank 4)
    cond = float(np.linalg.cond(V))
    info['evec_cond'] = cond
    if not np.isfinite(cond) or cond > 1e12:
        info['type'] = 'non-diagonalisable'
        return False, info
    timelike = False
    for j in range(4):
        v = np.real(V[:, j])
        nv = float(v @ eta @ v)
        if nv < -1e-12 * float(v @ v):
            timelike = True
    info['timelike_eigenvector'] = bool(timelike)
    isI = bool(timelike)
    info['type'] = 'I' if isI else 'not I (no timelike eigenvector)'
    return isI, info
