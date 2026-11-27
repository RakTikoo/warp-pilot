#!/usr/bin/env python3
"""
g47_lib.py -- Gate-47 FRESH machinery for the independent
re-judgement of Phase 396's claim set.

Independence statement: this module imports NOTHING from any
phase or earlier-gate code (no p316_lib / p389_lib / p394_lib /
p395_lib / p396_lib / g45_lib / verify_metric / p2352_run /
p258_lib). The registered definitions were read from those
files and re-implemented here from scratch:

  * profiles: closed-form base S / N / M per the Gate-47
    registration text, plus not-a-knot CubicSpline corrections
    with constant extension outside [10, 20];
  * tensor path: the metric's first and second SPATIAL
    derivatives are derived SYMBOLICALLY with sympy in
    Cartesian coordinates (functions S(r), N(r), M(r) of
    r = sqrt(x^2+y^2+z^2)), the radial-derivative symbols are
    substituted by plain symbols, and the derivative arrays
    are lambdified (numpy, cse=True). Christoffel / Ricci /
    Einstein assembly is this module's own vectorised numpy
    contraction code (stationary: time derivatives zero);
  * Eulerian frame, Hawking-Ellis margins and the SAMPLER-M
    sampled fallback are re-implemented from the registered
    formulas (sampled_margins replicated from verify_metric.py
    lines 203-251 as instructed);
  * SET-244 read, worst-null (Fibonacci-642 scan + Nelder-Mead
    polish), and a from-scratch 4th-order centred-FD Einstein
    tensor built from the metric function alone (calibration).

float64 throughout. Programme venv.
"""
import json
import os

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize
from scipy.special import beta as _beta_fn, betainc as _betainc

DTYPE = np.float64
BETA = 1.1
EIGHT_PI = 8.0 * np.pi
WP = '/home/hatch/workspace/warp-pilot'
R_LO, R_HI = 10.0, 20.0
FINE_R = np.linspace(R_LO, R_HI, 401)

# ============================================================ directions
def fib_dirs(npts):
    """Fibonacci sphere directions (registered form)."""
    i = np.arange(npts, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)

R_NODES = 10.0 + (np.arange(41, dtype=DTYPE) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
DIRS642 = fib_dirs(642)

# ============================================================ base profiles
def _S_ab(r, a=2.0, b=2.0):
    """S_ab = 1 - betainc(a+1, b+1, u), u=(r-10)/10 on (10,20);
    1 below, 0 above; derivatives per the registered forms."""
    r = np.asarray(r, dtype=DTYPE)
    S = np.ones_like(r); Sp = np.zeros_like(r); Spp = np.zeros_like(r)
    S = np.where(r >= 20.0, 0.0, S)
    m = (r > 10.0) & (r < 20.0)
    if np.any(m):
        u = (r[m] - 10.0) / 10.0
        B = _beta_fn(a + 1.0, b + 1.0)
        S[m] = 1.0 - _betainc(a + 1.0, b + 1.0, u)
        f = u ** a * (1.0 - u) ** b
        Sp[m] = -f / (10.0 * B)
        with np.errstate(divide='ignore', invalid='ignore'):
            fp = (u ** (a - 1.0) * (1.0 - u) ** (b - 1.0)
                  * (a * (1.0 - u) - b * u))
        fp = np.where(np.isfinite(fp), fp, 0.0)
        Spp[m] = -fp / (100.0 * B)
    return S, Sp, Spp

def _H(t):
    t = np.asarray(t, dtype=DTYPE)
    out = np.zeros_like(t)
    out = np.where(t >= 1.0, 1.0, out)
    m = (t > 0.0) & (t < 1.0)
    out = np.where(m, 10.0 * t**3 - 15.0 * t**4 + 6.0 * t**5, out)
    return out

def _Hp(t):
    t = np.asarray(t, dtype=DTYPE)
    out = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 30.0 * t**2 - 60.0 * t**3 + 30.0 * t**4, out)

def _Hpp(t):
    t = np.asarray(t, dtype=DTYPE)
    out = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    return np.where(m, 60.0 * t - 180.0 * t**2 + 120.0 * t**3, out)

_A_LAPSE = 0.07439108177516472

def _bump(r):
    """Plateau bump H((r-10)/3)*H((20-r)/3) (shape_B_plat
    c=15, W=5, e=3) with chain-rule derivatives."""
    r = np.asarray(r, dtype=DTYPE)
    x = (r - 10.0) / 3.0
    y = (20.0 - r) / 3.0
    Hx, Hy = _H(x), _H(y)
    Hpx, Hpy = _Hp(x), _Hp(y)
    Hppx, Hppy = _Hpp(x), _Hpp(y)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / 3.0
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / 9.0
    return B, Bp, Bpp

def _ss(x):
    return (6.0 * x**5 - 15.0 * x**4 + 10.0 * x**3,
            30.0 * x**4 - 60.0 * x**3 + 30.0 * x**2,
            120.0 * x**3 - 180.0 * x**2 + 60.0 * x)

def _U(r, a, b):
    r = np.asarray(r, dtype=DTYPE)
    U = np.zeros_like(r); Up = np.zeros_like(r); Upp = np.zeros_like(r)
    U = np.where(r >= b, 1.0, U)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss(x)
        U[mid] = v; Up[mid] = vp / (b - a); Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp

def base_profiles(r):
    """Registered base (S, S', S'', N, N', N'', M, M', M'')."""
    r = np.asarray(r, dtype=DTYPE)
    S, Sp, Spp = _S_ab(r, 2.0, 2.0)
    S, Sp, Spp = 0.70 * S, 0.70 * Sp, 0.70 * Spp
    B, Bp, Bpp = _bump(r)
    N = 1.0 + _A_LAPSE * B
    Np = _A_LAPSE * Bp
    Npp = _A_LAPSE * Bpp
    U1, U1p, U1pp = _U(r, 8.5, 20.0)
    U2, U2p, U2pp = _U(r, 21.0, 24.0)
    M = 1.0 + 6.0 * (U1 - U2)
    Mp = 6.0 * (U1p - U2p)
    Mpp = 6.0 * (U1pp - U2pp)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp

# ============================================================ corrections
def _knots(K):
    return np.linspace(R_LO, R_HI, K)

def _eval_corr(cs, r):
    """Correction spline value/derivatives with r clipped to
    [10,20] and derivatives zeroed outside (constant extension)."""
    r = np.asarray(r, dtype=DTYPE)
    rc = np.clip(r, R_LO, R_HI)
    d = cs(rc)
    dp = cs.derivative(1)(rc)
    dpp = cs.derivative(2)(rc)
    outside = (r < R_LO) | (r > R_HI)
    if np.any(outside):
        dp = np.where(outside, 0.0, dp)
        dpp = np.where(outside, 0.0, dpp)
    return d, dp, dpp

def _splines3(vS, vN, vM, K):
    xk = _knots(K)
    return (CubicSpline(xk, np.asarray(vS, dtype=DTYPE), bc_type='not-a-knot'),
            CubicSpline(xk, np.asarray(vN, dtype=DTYPE), bc_type='not-a-knot'),
            CubicSpline(xk, np.asarray(vM, dtype=DTYPE), bc_type='not-a-knot'))

def _add_corr(prof9, vS, vN, vM, K, r):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof9
    csS, csN, csM = _splines3(vS, vN, vM, K)
    dS, dSp, dSpp = _eval_corr(csS, r)
    dN, dNp, dNpp = _eval_corr(csN, r)
    dM, dMp, dMpp = _eval_corr(csM, r)
    return (S + dS, Sp + dSp, Spp + dSpp,
            N + dN, Np + dNp, Npp + dNpp,
            M + dM, Mp + dMp, Mpp + dMpp)

# ---- stored vectors (read as DATA from the registered artefacts)
def _load_vectors():
    conf344 = json.load(open(f'{WP}/phase344/results/p344_confirmation.json'))
    ent = [e for e in conf344['confirmations'] if e['point'] == 'A2'][0]
    st344 = json.load(open(f'{WP}/phase344/results/p344_state_A2.json'))['final_incumbent']
    a2_conf = tuple(np.array(ent[k], dtype=DTYPE) for k in ('vS', 'vN', 'vM'))
    a2_state = tuple(np.array(st344[k], dtype=DTYPE) for k in ('vS', 'vN', 'vM'))
    conf379 = json.load(open(f'{WP}/phase379/results/p379_confirmation.json'))
    ent2 = [e for e in conf379['confirmations'] if e['centre'] == 'H2'][0]
    st379 = json.load(open(f'{WP}/phase379/results/p379_state_H2.json'))['final_incumbent']
    h2_conf = tuple(np.array(ent2[k], dtype=DTYPE) for k in ('vS', 'vN', 'vM'))
    h2_state = tuple(np.array(st379[k], dtype=DTYPE) for k in ('vS', 'vN', 'vM'))
    return a2_conf, a2_state, h2_conf, h2_state

A2_CONF, A2_STATE, H2_CONF, H2_STATE = _load_vectors()
A2_K, H2_K, H2_MU = 33, 17, 1.15

def vector_agreement():
    out = {}
    for name, a, b in (('A2', A2_CONF, A2_STATE), ('H2', H2_CONF, H2_STATE)):
        out[name] = {k: float(np.max(np.abs(x - y))) if x.size else 0.0
                     for k, x, y in zip(('vS', 'vN', 'vM'), a, b)}
        out[name]['all_zero'] = bool(all(v == 0.0 for v in out[name].values()
                                         if isinstance(v, float)))
    return out

def a2_totals(r):
    return _add_corr(base_profiles(r), *A2_CONF, A2_K, np.asarray(r, dtype=DTYPE))

def centre_of_a2(mu, r):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = a2_totals(r)
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)

def h2_totals(r, clamp=False):
    r = np.asarray(r, dtype=DTYPE)
    vS, vN, vM = (v.copy() for v in H2_CONF)
    if clamp:
        for v in (vS, vN, vM):
            v[0] = 0.0; v[-1] = 0.0
    return _add_corr(centre_of_a2(H2_MU, r), vS, vN, vM, H2_K, r)

def profiles_scaled(muS, muN, muM, pts, clamp=False):
    """H2 totals with per-profile scaling (registered form)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = h2_totals(r, clamp=clamp)
    return (muS * S, muS * Sp, muS * Spp,
            muN * N, muN * Np, muN * Npp,
            1.0 + muM * (M - 1.0), muM * Mp, muM * Mpp)

def profiles_at_radius(muS, muN, muM, r, clamp=False):
    """Scaled profiles at radii r (1-D array), for physicality."""
    r = np.asarray(r, dtype=DTYPE)
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = h2_totals(r, clamp=clamp)
    return (muS * S, muS * Sp, muS * Spp,
            muN * N, muN * Np, muN * Npp,
            1.0 + muM * (M - 1.0), muM * Mp, muM * Mpp)

# ============================================================ symbolic derivatives
_DERIV_FUNCS = None

def _build_deriv_funcs():
    """Sympy: metric in Cartesian coords with S(r), N(r), M(r);
    differentiate once/twice w.r.t. (x,y,z); substitute the
    radial symbols; lambdify dg (3,4,4) and ddg (3,3,4,4)."""
    global _DERIV_FUNCS
    if _DERIV_FUNCS is not None:
        return _DERIV_FUNCS
    import sympy as sp
    x, y, z = sp.symbols('x y z')
    r = sp.sqrt(x**2 + y**2 + z**2)
    Sf = sp.Function('S')(r); Nf = sp.Function('N')(r); Mf = sp.Function('M')(r)
    beta = sp.Float(1.1)
    coords = [x, y, z]
    n = [x / r, y / r, z / r]
    g = sp.zeros(4, 4)
    g[0, 0] = -Nf**2
    g[0, 1] = g[1, 0] = -beta * Sf
    for i in range(3):
        for j in range(3):
            g[1 + i, 1 + j] = (1 if i == j else 0) + (Mf - 1) * n[i] * n[j]
    dg = [[[sp.diff(g[a, b], c) for b in range(4)] for a in range(4)]
          for c in coords]
    ddg = [[[[sp.diff(dg[ci][a][b], cj) for b in range(4)] for a in range(4)]
            for cj in coords] for ci in range(3)]
    s0, s1, s2, n0, n1, n2, m0, m1, m2 = sp.symbols('s0 s1 s2 n0 n1 n2 m0 m1 m2')
    sym_of = {'S': (s0, s1, s2), 'N': (n0, n1, n2), 'M': (m0, m1, m2)}

    def clean(e):
        # radial derivatives appear as Subs(Derivative(F(xi), xi[, xi]), xi, r)
        repl = {}
        for node in e.atoms(sp.Subs):
            d = node.expr
            if isinstance(d, sp.Derivative):
                fname = d.expr.func.__name__
                order = int(sum(c for _, c in d.variable_count))
                repl[node] = sym_of[fname][order]
        e = e.subs(repl)
        return e.subs({Sf: s0, Nf: n0, Mf: m0})
    dg_s = [[ [clean(e) for e in row] for row in mat] for mat in dg]
    ddg_s = [[[ [clean(e) for e in row] for row in mat]
              for mat in lev] for lev in ddg]
    leftover = set()
    for mat in dg_s:
        for row in mat:
            for e in row:
                leftover |= {str(a) for a in e.atoms(sp.Derivative, sp.Subs)}
    for lev in ddg_s:
        for mat in lev:
            for row in mat:
                for e in row:
                    leftover |= {str(a) for a in e.atoms(sp.Derivative, sp.Subs)}
    if leftover:
        raise RuntimeError(f'unsubstituted derivative atoms remain: {leftover}')
    args = (x, y, z, s0, s1, s2, n0, n1, n2, m0, m1, m2)
    flat_dg = [dg_s[c][a][b] for c in range(3) for a in range(4) for b in range(4)]
    flat_ddg = [ddg_s[c][d][a][b] for c in range(3) for d in range(3)
                for a in range(4) for b in range(4)]
    f_dg = sp.lambdify(args, flat_dg, modules='numpy', cse=True)
    f_ddg = sp.lambdify(args, flat_ddg, modules='numpy', cse=True)
    _DERIV_FUNCS = (f_dg, f_ddg)
    return _DERIV_FUNCS

def _eval_flat(f, P, shape, args):
    vals = f(*args)
    cols = []
    for v in vals:
        v = np.asarray(v, dtype=DTYPE)
        if v.shape == ():
            cols.append(np.full(P, float(v)))
        elif v.shape == (P,):
            cols.append(v)
        else:
            cols.append(np.broadcast_to(v, (P,)).astype(DTYPE))
    arr = np.stack(cols, axis=0)          # (prod(shape), P)
    return np.moveaxis(arr.reshape(shape + (P,)), -1, 0)

# ============================================================ tensor assembly (own)
def metric_from_profiles(pts, prof9):
    pts = np.asarray(pts, dtype=DTYPE)
    S, _, _, N, _, _, M, _, _ = prof9
    r = np.linalg.norm(pts, axis=1)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rsafe[:, None], 0.0)
    P = len(pts)
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + (M - 1.0) * n[:, i] * n[:, j])
    return g

def T_from_profiles(pts, prof9):
    """Einstein tensor / (8 pi) at pts from profile arrays.
    Returns (T, g). Stationary; derivatives from the sympy path."""
    pts = np.asarray(pts, dtype=DTYPE)
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof9
    P = len(pts)
    f_dg, f_ddg = _build_deriv_funcs()
    dargs = (pts[:, 0], pts[:, 1], pts[:, 2],
             S, Sp, Spp, N, Np, Npp, M, Mp, Mpp)
    dgS = _eval_flat(f_dg, P, (3, 4, 4), dargs)       # (P,3,4,4)
    ddgS = _eval_flat(f_ddg, P, (3, 3, 4, 4), dargs)  # (P,3,3,4,4)
    # full derivative arrays: DG[p,e,mu,nu], DDG[p,e,f,mu,nu]; e=0 time (zero)
    DG = np.zeros((P, 4, 4, 4), dtype=DTYPE)
    DG[:, 1:, :, :] = dgS
    DDG = np.zeros((P, 4, 4, 4, 4), dtype=DTYPE)
    DDG[:, 1:, 1:, :, :] = ddgS
    g = metric_from_profiles(pts, prof9)
    ginv = np.linalg.inv(g)
    # A[p,b,c,d] = DG[p,b,d,c] + DG[p,c,d,b] - DG[p,d,b,c]
    A = (np.transpose(DG, (0, 1, 3, 2)) + np.transpose(DG, (0, 3, 1, 2))
         - np.transpose(DG, (0, 2, 3, 1)))
    # Christoffel Gamma^a_{bc} = .5 ginv^{ad} A[p,b,c,d]
    Gam = 0.5 * np.einsum('pad,pbcd->pabc', ginv, A)
    # dginv[e] = -ginv DG[e] ginv
    dginv = -np.einsum('pam,pemn,pnb->peab', ginv, DG, ginv)
    # dA[p,e,b,c,d] = DDG[p,e,b,d,c] + DDG[p,e,c,d,b] - DDG[p,e,d,b,c]
    dA = (np.transpose(DDG, (0, 1, 2, 4, 3)) + np.transpose(DDG, (0, 1, 4, 2, 3))
          - np.transpose(DDG, (0, 1, 3, 4, 2)))
    dGam = (0.5 * np.einsum('pead,pbcd->peabc', dginv, A)
            + 0.5 * np.einsum('pad,pebcd->peabc', ginv, dA))
    # Ricci R_{bd} = dGam[a,a,b,d] - dGam[d,a,b,a] + Gam Gam terms
    Ric = (np.einsum('paabd->pbd', dGam) - np.einsum('pdaba->pbd', dGam)
           + np.einsum('paae,pebd->pbd', Gam, Gam)
           - np.einsum('pade,peba->pbd', Gam, Gam))
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g
    return G / EIGHT_PI, g

def _norm_deriv(arr, P, order):
    """Lambdified Array output layout: sympy Array(dg_s) has shape
    (3,4,4) with scalar inputs -> array (3,4,4,P) for vector inputs
    (trailing broadcast axis). Convert to (P,3,4,4) / (P,3,3,4,4)."""
    arr = np.asarray(arr, dtype=DTYPE)
    if order == 1:
        if arr.shape == (3, 4, 4, P):
            return np.moveaxis(arr, -1, 0)
        if arr.shape == (P, 3, 4, 4):
            return arr
        if arr.shape == (3, 4, 4) and P == 1:
            return arr[None]
    else:
        if arr.shape == (3, 3, 4, 4, P):
            return np.moveaxis(arr, -1, 0)
        if arr.shape == (P, 3, 3, 4, 4):
            return arr
        if arr.shape == (3, 3, 4, 4) and P == 1:
            return arr[None]
    # generic fallback: move the axis of size P to front
    ax = arr.shape.index(P) if P in arr.shape else -1
    return np.moveaxis(arr, ax, 0)

def T_at(muS, muN, muM, pts, clamp=False):
    return T_from_profiles(pts, profiles_scaled(muS, muN, muM, pts, clamp=clamp))

# ============================================================ Eulerian frame + margins (own)
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

def sampled_margins(That, n_dir=162, n_vel=6):
    """Replicated from verify_metric.sampled_margins (registered)."""
    i = np.arange(n_dir, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n_dir)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    dirs = np.stack([np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np_ = flat.shape[0]
    nec_min = np.empty(Np_); wec_min = np.empty(Np_)
    sec_min = np.empty(Np_); dec_min = np.empty(Np_)
    vels = np.linspace(0.0, 0.95, n_vel)
    CH = 8192
    for s0 in range(0, Np_, CH):
        F = flat[s0:s0 + CH]
        T00 = F[:, 0, 0]; T0i = F[:, 0, 1:]; Tij = F[:, 1:, 1:]
        tr = np.trace(Tij, axis1=1, axis2=2)
        quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
        nec_min[s0:s0 + CH] = (T00[:, None] + 2.0 * (T0i @ dirs.T) + quad).min(axis=1)
        wm = np.full(F.shape[0], np.inf); sm = np.full(F.shape[0], np.inf)
        dm = np.full(F.shape[0], np.inf)
        Mm = F.copy(); Mm[:, 0, :] *= -1.0
        for v in vels:
            gam = 1.0 / np.sqrt(1.0 - v * v)
            wec_vals = gam ** 2 * (T00[:, None] + 2.0 * v * (T0i @ dirs.T) + v * v * quad)
            wm = np.minimum(wm, wec_vals.min(axis=1))
            trT = -T00 + tr
            sec_vals = wec_vals - 0.5 * trT[:, None] * gam ** 2 * (v * v - 1.0)
            sm = np.minimum(sm, sec_vals.min(axis=1))
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

def hawking_ellis(That, do_fallback=True):
    That = np.asarray(That, dtype=DTYPE)
    shp = That.shape[:-2]
    flat = That.reshape(-1, 4, 4)
    Np_ = flat.shape[0]
    M = flat.copy(); M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k_idx = np.argmax(cand, axis=1)
    ar = np.arange(Np_)
    rho = np.where(typeI, -evals[ar, k_idx].real, np.nan)
    mask = np.ones((Np_, 4), dtype=bool); mask[ar, k_idx] = False
    ps_all = evals.real[mask].reshape(Np_, 3)
    ps = np.where(typeI[:, None], ps_all, np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    filled = np.zeros(Np_, dtype=bool)
    if do_fallback and np.any(~typeI):
        sub = sampled_margins(flat[~typeI].reshape(-1, 4, 4))
        idx = np.where(~typeI)[0]
        nec[idx] = sub['nec_s']; wec[idx] = sub['wec_s']
        sec[idx] = sub['sec_s']; dec[idx] = sub['dec_s']
        filled[idx] = True
    return {'rho_eig': rho.reshape(shp), 'p': ps.reshape(shp + (3,)),
            'typeI': typeI.reshape(shp), 'sampled_filled': filled.reshape(shp),
            'nec': nec.reshape(shp), 'wec': wec.reshape(shp),
            'sec': sec.reshape(shp), 'dec': dec.reshape(shp),
            'rho_euler': That[..., 0, 0]}

def margins_all(That):
    """HE margins with sampled fallback applied to non-Type-I only
    (the lineage margins_chunked protocol, re-implemented)."""
    m = hawking_ellis(That, do_fallback=False)
    shp = That.shape[:-2]
    flat_t = That.reshape(-1, 4, 4)
    bad = np.where(~m['typeI'].reshape(-1))[0]
    if bad.size:
        sub = sampled_margins(flat_t[bad])
        for k, ks in (('nec', 'nec_s'), ('wec', 'wec_s'), ('sec', 'sec_s'), ('dec', 'dec_s')):
            arr = m[k].reshape(-1); arr[bad] = sub[ks]; m[k] = arr.reshape(shp)
        fl = m['sampled_filled'].reshape(-1); fl[bad] = True
        m['sampled_filled'] = fl.reshape(shp)
    return m

# ============================================================ SET read
def set_read(muS, muN, muM, clamp=False):
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec', 'rho', 'filled')}
    for rr in R_NODES:
        pts = DIRS162 * rr
        T, g = T_at(muS, muN, muM, pts, clamp=clamp)
        That = eulerian_that(g, T)
        m = margins_all(That)
        rec['typeI'].append(m['typeI']); rec['nec'].append(m['nec'])
        rec['wec'].append(m['wec']); rec['dec'].append(m['dec'])
        rec['sec'].append(m['sec']); rec['rho'].append(That[:, 0, 0])
        rec['filled'].append(m['sampled_filled'])
    R = {k: np.concatenate(v) for k, v in rec.items()}

    def st(arr):
        return {'min': float(np.min(arr)), 'median': float(np.median(arr)),
                'max': float(np.max(arr))}
    i_nec = int(np.argmin(R['nec'])); i_dec = int(np.argmin(R['dec']))
    i_r, i_d = divmod(i_nec, 162); j_r, j_d = divmod(i_dec, 162)
    out = {
        'n_points': int(len(R['typeI'])),
        'typeI_fraction': float(np.mean(R['typeI'])),
        'typeI_count': int(np.sum(R['typeI'])),
        'nec': st(R['nec']), 'wec': st(R['wec']), 'dec': st(R['dec']),
        'sec': st(R['sec']), 'rho': st(R['rho']),
        'joint': float(min(R['nec'].min(), R['dec'].min())),
        'nec_argmin_point': (DIRS162[i_d] * R_NODES[i_r]).tolist(),
        'nec_argmin_r': float(R_NODES[i_r]),
        'nec_argmin_typeI': bool(R['typeI'][i_nec]),
        'dec_argmin_point': (DIRS162[j_d] * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
    }
    return out, R

def that_at(muS, muN, muM, pt, clamp=False):
    pt = np.asarray(pt, dtype=DTYPE)
    T, g = T_at(muS, muN, muM, pt[None, :], clamp=clamp)
    return eulerian_that(g, T)[0]

def point_margins(muS, muN, muM, pt, clamp=False):
    That = that_at(muS, muN, muM, pt, clamp=clamp)
    m = margins_all(That[None])
    return {'nec': float(m['nec'][0]), 'wec': float(m['wec'][0]),
            'sec': float(m['sec'][0]), 'dec': float(m['dec'][0]),
            'typeI': bool(m['typeI'][0]), 'rho_euler': float(That[0, 0]),
            'That': That}

def worst_null(That):
    """Exact worst null contraction: fib-642 scan + NM polish."""
    def q_of(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)
    vals = np.array([q_of(d) for d in DIRS642])
    n_best = DIRS642[int(np.argmin(vals))]
    th0 = np.arccos(np.clip(n_best[2], -1, 1)); ph0 = np.arctan2(n_best[1], n_best[0])

    def obj(x):
        th, ph = x
        n = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])
        return q_of(n)
    res = minimize(obj, np.array([th0, ph0]), method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10, 'fatol': 1e-14})
    return float(obj(res.x)), float(np.min(vals))

def worst_null_at(muS, muN, muM, pt, clamp=False):
    That = that_at(muS, muN, muM, pt, clamp=clamp)
    return worst_null(That)

# ============================================================ FD cross-path (calibration)
def metric_only(pts, muS, muN, muM, clamp=False):
    return metric_from_profiles(pts, profiles_scaled(muS, muN, muM, pts, clamp=clamp))

def _fd4(fun, X, h, axis):
    """4th-order centred FD derivative of fun along coordinate axis
    (0=t..3=z) at points X (P,4); stationary: axis 0 gives zeros."""
    if axis == 0:
        return np.zeros_like(fun(X))
    e = np.zeros(4); e[axis] = 1.0
    return (fun(X - 2 * h * e) - 8.0 * fun(X - h * e)
            + 8.0 * fun(X + h * e) - fun(X + 2 * h * e)) / (12.0 * h)

def einstein_fd(pts3, muS, muN, muM, h, clamp=False):
    """From-scratch FD Einstein/(8pi) at 3-points pts3 (P,3),
    metric function alone (profile VALUES only)."""
    pts3 = np.asarray(pts3, dtype=DTYPE)
    X = np.concatenate([np.zeros((len(pts3), 1)), pts3], axis=1)

    def gfun(Xq):
        return metric_only(Xq[:, 1:], muS, muN, muM, clamp=clamp)

    def gamma_fun(Xq):
        g = gfun(Xq)
        ginv = np.linalg.inv(g)
        dg = [_fd4(gfun, Xq, h, e) for e in range(4)]
        Gam = np.zeros((len(Xq), 4, 4, 4), dtype=DTYPE)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    term = np.stack([dg[b][:, d, c] + dg[c][:, d, b] - dg[d][:, b, c]
                                     for d in range(4)], axis=1)
                    Gam[:, a, b, c] = 0.5 * np.einsum('pd,pd->p', ginv[:, a, :], term)
        return Gam
    g = gfun(X); ginv = np.linalg.inv(g)
    Gam = gamma_fun(X)
    dGam = [_fd4(gamma_fun, X, h, e) for e in range(4)]
    Ric = np.zeros((len(X), 4, 4), dtype=DTYPE)
    for b in range(4):
        for d in range(4):
            val = np.zeros(len(X), dtype=DTYPE)
            for a in range(4):
                val += dGam[a][:, a, b, d] - dGam[d][:, a, b, a]
            for a in range(4):
                for e in range(4):
                    val += (Gam[:, a, a, e] * Gam[:, e, b, d]
                            - Gam[:, a, d, e] * Gam[:, e, b, a])
            Ric[:, b, d] = val
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g
    return G / EIGHT_PI, g
