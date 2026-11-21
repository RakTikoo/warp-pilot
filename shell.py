"""
shell.py — Spherical matter shells following Fuchs et al. 2024 §3, with
profile freedom Fuchs did NOT use (their trial density was constant and
their smoothing was MATLAB moving-average; here: shaped trial profiles +
Gaussian smoothing, all NumPy, float64, geometric units G = c = 1).

Construction (mirrors Fuchs Eqs. 19-25):
  1. trial density from a weight shape w(r) on [R1, R2], normalised to mass M
  2. Gaussian smoothing of density (span s_rho) and pressure (span s_P),
     renormalising density to keep total mass M
  3. m(r) = int 4 pi r^2 rho dr
  4. pressure: TOV integration inward from P(R_far)=0 over the shell,
     P = 0 inside the cavity (r < R1), then smoothed
  5. b(r): exp(2b) = (1 - 2m/r)^-1 ;  a(r): da/dr = (m/r^2 + 4 pi r P)/(1-2m/r)
     integrated inward from a(r_far) = 0.5 ln(1 - 2M/r_far)

Exact spherical stress-energy (independent of any 3D code):
  rho = m' / (4 pi r^2)
  p_r = [ -2m/r^3 + 2 a' (1-2m/r)/r ] / (8 pi)
  p_t = (1-2m/r) [ a'' + a'^2 - a' b' + (a'-b')/r ] / (8 pi),
  b'  = (m'/r - m/r^2) / (1-2m/r)
"""
import numpy as np
_trapz = np.trapezoid if hasattr(np, 'trapezoid') else np.trapz
from scipy.interpolate import CubicSpline

DTYPE = np.float64


def smootherstep(u):
    u = np.clip(u, 0.0, 1.0)
    return u ** 3 * (10.0 + u * (-15.0 + 6.0 * u))


def weight(r, R1, R2, kind, params):
    w = np.zeros_like(r)
    inside = (r >= R1) & (r <= R2)
    if kind == 'constant':
        w[inside] = 1.0
    elif kind == 'smoothbox':
        e = params.get('edge', 1.0)
        up = smootherstep((r - (R1 - e)) / (2 * e))
        dn = 1.0 - smootherstep((r - (R2 - e)) / (2 * e))
        w = up * dn
    elif kind == 'gauss':
        Rm = params.get('Rm', 0.5 * (R1 + R2)); wd = params.get('wd', 2.0)
        w = np.exp(-((r - Rm) / wd) ** 2) * inside
    elif kind == 'matched':
        Rs = params['Rs']; wd = params.get('wd', 2.0); floor = params.get('floor', 0.05)
        w = (floor + (1 - floor) * np.exp(-((r - Rs) / wd) ** 2)) * inside
    elif kind == 'edgepeaked':
        # density concentrated near BOTH shell edges (where shift/pressure
        # gradients and hoop stress peak), dip in the middle
        Rm = 0.5 * (R1 + R2); wd = params.get('wd', 2.5); floor = params.get('floor', 0.15)
        w = (floor + (1 - floor) * (1 - np.exp(-(((np.abs(r - Rm) - 0.5 * (R2 - R1)) / wd) ** 2)))) * inside
        w = (floor + (1 - floor) * np.exp(-(((np.abs(r - Rm) - 0.42 * (R2 - R1)) / wd) ** 2))) * inside
    else:
        raise ValueError(kind)
    return w


def gauss_smooth(y, dr, width):
    if width <= 0:
        return y.copy()
    k = int(np.ceil(4 * width / dr))
    xs = np.arange(-k, k + 1) * dr
    ker = np.exp(-(xs / width) ** 2); ker /= ker.sum()
    ones = np.ones_like(y)
    num = np.convolve(y, ker, mode='same')
    den = np.convolve(ones, ker, mode='same')
    return num / np.maximum(den, 1e-300)


def cumint(y, x):
    """Cumulative integral int_0^x y dx (trapezoid), cumint[0]=0."""
    out = np.zeros_like(y)
    out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))
    return out


def build_shell(R1, R2, M, kind='constant', params=None, s_rho=0.0, s_P=0.0,
                rmax=None, Nr=4001):
    params = params or {}
    if rmax is None:
        rmax = 3.0 * R2
    r = np.linspace(0.0, rmax, Nr, dtype=DTYPE)
    dr = r[1] - r[0]
    w = weight(r, R1, R2, kind, params)
    vol = 4 * np.pi * r ** 2
    norm = _trapz(vol * w, r)
    rho = M * w / norm
    if s_rho > 0:
        rho = gauss_smooth(rho, dr, s_rho)
        rho = np.maximum(rho, 0.0)
        rho *= M / _trapz(vol * rho, r)     # keep total mass exact
    m = cumint(vol * rho, r)
    u = 1.0 - 2.0 * m / np.maximum(r, 1e-12)
    if np.min(u) <= 0.02:
        raise ValueError(f'shell too compact: min(1-2m/r)={np.min(u):.3f}')

    # --- TOV pressure, integrated inward from rmax (P=0 outside shell) ------
    P = np.zeros_like(r)
    # integrate on the grid from the top down with RK2 (midpoint)
    for i in range(Nr - 2, -1, -1):
        if r[i] < R1:
            P[i] = 0.0
            continue
        def dpdr(rr, mm, rh, PP):
            if rr <= 0:
                return 0.0
            uu = 1.0 - 2 * mm / rr
            return -(rh + PP) * (mm / rr ** 2 + 4 * np.pi * rr * PP) / uu
        hstep = r[i + 1] - r[i]
        k1 = dpdr(r[i + 1], m[i + 1], rho[i + 1], P[i + 1])
        Pm = P[i + 1] - 0.5 * hstep * k1     # P at midpoint (going inward: P increases)
        rm_ = 0.5 * (r[i] + r[i + 1]); mm_ = 0.5 * (m[i] + m[i + 1]); rh_ = 0.5 * (rho[i] + rho[i + 1])
        k2 = dpdr(rm_, mm_, rh_, Pm)
        P[i] = P[i + 1] - hstep * k2
    P = np.maximum(P, 0.0)
    if s_P > 0:
        P = gauss_smooth(P, dr, s_P)
        P = np.maximum(P, 0.0)

    # --- metric functions a(r), b(r) ----------------------------------------
    b = np.where(r > 0, -0.5 * np.log(np.maximum(u, 1e-300)), 0.0)
    aprime = np.where(r > 0, (m / np.maximum(r, 1e-12) ** 2 + 4 * np.pi * r * P) / np.maximum(u, 1e-300), 0.0)
    # a(rmax) = 0.5 ln(1 - 2M/rmax); integrate inward
    a = np.zeros_like(r)
    a[-1] = 0.5 * np.log(max(1.0 - 2 * m[-1] / r[-1], 1e-300))
    for i in range(Nr - 2, -1, -1):
        a[i] = a[i + 1] - 0.5 * (aprime[i] + aprime[i + 1]) * (r[i + 1] - r[i])
    # shift a so that interior is referenced consistently (a is absolute here:
    # boundary condition at rmax fixes it; interior a(R1) is then determined)

    # --- exact spherical stress-energy --------------------------------------
    mp = np.gradient(m, r, edge_order=2)
    rho_ex = np.where(r > 0, mp / (4 * np.pi * np.maximum(r, 1e-12) ** 2), rho[0])
    bp = np.where(r > 0, (mp / np.maximum(r, 1e-12) - m / np.maximum(r, 1e-12) ** 2) / np.maximum(u, 1e-300), 0.0)
    app = np.gradient(aprime, r, edge_order=2)
    p_r = (-2 * m / np.maximum(r, 1e-12) ** 3 + 2 * aprime * u / np.maximum(r, 1e-12)) / (8 * np.pi)
    p_t = u * (app + aprime ** 2 - aprime * bp + (aprime - bp) / np.maximum(r, 1e-12)) / (8 * np.pi)
    p_r = np.where(r > 0, p_r, 0.0); p_t = np.where(r > 0, p_t, 0.0)

    return {'r': r, 'rho_trial': rho, 'P': P, 'm': m, 'a': a, 'b': b,
            'aprime': aprime, 'rho_ex': rho_ex, 'p_r': p_r, 'p_t': p_t,
            'R1': R1, 'R2': R2, 'M': M, 'kind': kind, 'params': params,
            's_rho': s_rho, 's_P': s_P}


def shell_exact_margins(prof):
    """Hawking-Ellis margins of the base shell (no shift) from exact 1D T."""
    import verify_metric as vm
    n = len(prof['r'])
    That = np.zeros((n, 4, 4), dtype=DTYPE)
    That[:, 0, 0] = prof['rho_ex']
    That[:, 1, 1] = prof['p_r']
    That[:, 2, 2] = prof['p_t']
    That[:, 3, 3] = prof['p_t']
    return vm.hawking_ellis_margins(That)


def shift_S(r, R1, R2, kind='fuchs', Rb=1.0, ws=None):
    """Shift transition function S(r): 1 inside, 0 outside (Fuchs §4.1)."""
    r = np.asarray(r, dtype=DTYPE)
    if kind == 'fuchs':
        S = np.zeros_like(r)
        S[r < R1 + Rb] = 1.0
        mid = (r >= R1 + Rb) & (r <= R2 - Rb)
        rr = r[mid]
        f = 1.0 / (np.exp((R2 - R1) * (1.0 / (rr - R2) + 1.0 / (rr - R1))) + 1.0)
        S[mid] = 1.0 - f
        return S
    if kind == 'smoothstep':
        lo, hi = R1 + Rb, R2 - Rb
        return 1.0 - smootherstep((r - lo) / (hi - lo))
    if kind == 'tanh':
        Rm = 0.5 * (R1 + R2) if ws is None else ws[0]
        wdt = 2.0 if ws is None else ws[1]
        return 0.5 * (1.0 - np.tanh((r - Rm) / wdt))
    if kind in ('cos', 'quintic'):
        lo, hi = (R1, R2) if ws is None else ws  # transition window
        u = np.clip((r - lo) / (hi - lo), 0.0, 1.0)
        if kind == 'cos':
            return 0.5 * (1.0 + np.cos(np.pi * u))
        return 1.0 - u ** 3 * (10 - 15 * u + 6 * u ** 2)
    raise ValueError(kind)


def shell_point_factory(prof, beta_w, shift_kind='fuchs', Rb=1.0, ws=None):
    """Returns gfunc(pts (P,3)) -> (P,4,4) for the shell + shift metric,
    using cubic-spline radial profiles (smooth, point-evaluable)."""
    a_s = CubicSpline(prof['r'], prof['a'])
    b_s = CubicSpline(prof['r'], prof['b'])
    rmax = prof['r'][-1]

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, rmax)
        a = a_s(rc); b = b_s(rc)
        S = shift_S(r, prof['R1'], prof['R2'], shift_kind, Rb, ws)
        P = pts.shape[0]
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2 * a)
        g[:, 0, 1] = g[:, 1, 0] = -S * beta_w
        eb = np.exp(2 * b) - 1.0
        rsafe = np.where(r > 0, r, 1.0)
        n = pts / rsafe[:, None]
        for i in range(3):
            for j in range(3):
                g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
            g[:, 1 + i, 1 + i] += 1.0
        return g

    return gfunc


def shell_grid(prof, N, L, beta_w, shift_kind='fuchs', Rb=1.0, ws=None):
    """Cartesian grid metric of shell + interior shift (Fuchs §4 form):
    g_tt = -exp(2a), g_tX = -S(r) beta_w, gamma_ij = delta_ij + (exp(2b)-1) n_i n_j.
    Returns g, h, (X,Y,Z)."""
    import metrics as mx
    (X, Y, Z), h = mx.mesh(N, L)
    r = mx.radii(X, Y, Z)
    a_s = CubicSpline(prof['r'], prof['a'])
    b_s = CubicSpline(prof['r'], prof['b'])
    a = a_s(np.clip(r, 0, prof['r'][-1]))
    b = b_s(np.clip(r, 0, prof['r'][-1]))
    S = shift_S(r, prof['R1'], prof['R2'], shift_kind, Rb, ws)
    g = np.zeros((N, N, N, 4, 4), dtype=DTYPE)
    g[..., 0, 0] = -np.exp(2 * a)
    g[..., 0, 1] = g[..., 1, 0] = -S * beta_w
    eb = np.exp(2 * b) - 1.0
    rsafe = np.where(r > 0, r, 1.0)
    nx, ny, nz = X / rsafe, Y / rsafe, Z / rsafe
    g[..., 1, 1] = 1.0 + eb * nx * nx
    g[..., 2, 2] = 1.0 + eb * ny * ny
    g[..., 3, 3] = 1.0 + eb * nz * nz
    g[..., 1, 2] = g[..., 2, 1] = eb * nx * ny
    g[..., 1, 3] = g[..., 3, 1] = eb * nx * nz
    g[..., 2, 3] = g[..., 3, 2] = eb * ny * nz
    return g, h, (X, Y, Z)
