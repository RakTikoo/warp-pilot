"""
metrics.py — Cartesian grid builders for Natario-class warp metrics
(stationary in comoving coordinates X = x - v t, valid for any v).

All float64, geometric units G = c = 1.
"""
import numpy as np

DTYPE = np.float64


def grid_axes(N, L):
    ax = np.linspace(-L, L, N, dtype=DTYPE)
    return ax, ax[1] - ax[0]


def alcubierre_f(r, R, sigma):
    """Alcubierre shape function f(r): 1 inside, 0 outside."""
    return (np.tanh(sigma * (r + R)) - np.tanh(sigma * (r - R))) / (2.0 * np.tanh(sigma * R))


def alcubierre_fprime(r, R, sigma):
    return (sigma * (1.0 / np.cosh(sigma * (r + R)) ** 2
                     - 1.0 / np.cosh(sigma * (r - R)) ** 2) / (2.0 * np.tanh(sigma * R)))


def radii(X, Y, Z):
    return np.sqrt(X ** 2 + Y ** 2 + Z ** 2)


def mesh(N, L):
    ax, h = grid_axes(N, L)
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')
    return (X, Y, Z), h


def alcubierre_grid(N, L, v, R=1.5, sigma=2.0):
    """Comoving Alcubierre: alpha=1, gamma=delta, beta^X = v (1-f(r)).
    Returns g (N,N,N,4,4), h, (X,Y,Z)."""
    (X, Y, Z), h = mesh(N, L)
    r = radii(X, Y, Z)
    f = alcubierre_f(r, R, sigma)
    beta = v * (1.0 - f)                      # shift covector g_tX (gamma=delta)
    g = np.zeros((N, N, N, 4, 4), dtype=DTYPE)
    g[..., 0, 0] = -1.0 + beta ** 2
    g[..., 0, 1] = g[..., 1, 0] = beta
    g[..., 1, 1] = 1.0
    g[..., 2, 2] = 1.0
    g[..., 3, 3] = 1.0
    return g, h, (X, Y, Z)


def vandenbroeck_grid(N, L, v, R=1.5, sigma=2.0, Rb=0.8, sigmab=3.0, Bamp=5.0):
    """Comoving Van den Broeck type: gamma_ij = B(r)^2 delta_ij, alpha=1,
    shift as Alcubierre. B = 1 + Bamp * s(r), s transitions 1->0 at Rb."""
    (X, Y, Z), h = mesh(N, L)
    r = radii(X, Y, Z)
    f = alcubierre_f(r, R, sigma)
    s = alcubierre_f(r, Rb, sigmab)
    B = 1.0 + Bamp * s
    beta_cov = B ** 2 * v * (1.0 - f)         # g_tX = gamma_XX * beta^X
    g = np.zeros((N, N, N, 4, 4), dtype=DTYPE)
    g[..., 0, 0] = -1.0 + B ** 2 * (v * (1.0 - f)) ** 2
    g[..., 0, 1] = g[..., 1, 0] = beta_cov
    g[..., 1, 1] = B ** 2
    g[..., 2, 2] = B ** 2
    g[..., 3, 3] = B ** 2
    return g, h, (X, Y, Z)


def _points_metric(pts, alpha, Om, shift):
    """Assemble ADM-form metric at points: lapse alpha, conformal Om,
    shift covector along x = Om^2 * shift (shift = beta^x contravariant)."""
    P = pts.shape[0]
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -alpha ** 2 + Om ** 2 * shift ** 2
    g[:, 0, 1] = g[:, 1, 0] = Om ** 2 * shift
    g[:, 1, 1] = Om ** 2
    g[:, 2, 2] = Om ** 2
    g[:, 3, 3] = Om ** 2
    return g


def alcubierre_point(pts, v, R=1.5, sigma=2.0):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.sqrt(np.sum(pts ** 2, axis=1))
    f = alcubierre_f(r, R, sigma)
    return _points_metric(pts, np.ones_like(r), np.ones_like(r), v * (1.0 - f))


def vandenbroeck_point(pts, v, R=1.5, sigma=2.0, Rb=0.8, sigmab=3.0, Bamp=5.0):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.sqrt(np.sum(pts ** 2, axis=1))
    f = alcubierre_f(r, R, sigma)
    B = 1.0 + Bamp * alcubierre_f(r, Rb, sigmab)
    return _points_metric(pts, np.ones_like(r), B, v * (1.0 - f))


def generalized_point(pts, v, R_f=1.5, sig_f=2.0, A_a=0.0, R_a=1.5, sig_a=2.0,
                      A_o=0.0, R_o=0.8, sig_o=3.0):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.sqrt(np.sum(pts ** 2, axis=1))
    f = alcubierre_f(r, R_f, sig_f)
    bump = alcubierre_f(r, R_a, sig_a) * (1.0 - alcubierre_f(r, R_a * 0.55, sig_a))
    alpha = 1.0 + A_a * bump
    Om = 1.0 + A_o * alcubierre_f(r, R_o, sig_o)
    return _points_metric(pts, alpha, Om, v * (1.0 - f))


def generalized_grid(N, L, v, R_f=1.5, sig_f=2.0,
                     A_a=0.0, R_a=1.5, sig_a=2.0,
                     A_o=0.0, R_o=0.8, sig_o=3.0):
    """Generalised outside-SSV family (superluminal lens SL-1):
        ds^2 = -alpha(r)^2 dt^2 + Omega(r)^2 [ (dX + v(1-f) dt)^2 + dy^2 + dz^2 ]
    alpha(r) = 1 + A_a * bump_a(r)  (bump = wall-localised tanh window at R_a)
    Omega(r) = 1 + A_o * s_o(r)     (pocket factor, VdB type)
    f = Alcubierre shape at R_f. alpha must stay > 0.05 everywhere.
    Escapes SSV by construction when A_a != 0 (non-unit lapse) and/or
    A_o != 0 (non-flat spatial slices)."""
    (X, Y, Z), h = mesh(N, L)
    r = radii(X, Y, Z)
    f = alcubierre_f(r, R_f, sig_f)
    bump = alcubierre_f(r, R_a, sig_a) * (1.0 - alcubierre_f(r, R_a * 0.55, sig_a))
    # bump ~ 1 in a shell around R_a, 0 deep inside and far outside
    alpha = 1.0 + A_a * bump
    if np.min(alpha) < 0.05:
        raise ValueError('lapse too small')
    Om = 1.0 + A_o * alcubierre_f(r, R_o, sig_o)
    shift = v * (1.0 - f)
    g = np.zeros((N, N, N, 4, 4), dtype=DTYPE)
    g[..., 0, 0] = -alpha ** 2 + Om ** 2 * shift ** 2
    g[..., 0, 1] = g[..., 1, 0] = Om ** 2 * shift
    g[..., 1, 1] = Om ** 2
    g[..., 2, 2] = Om ** 2
    g[..., 3, 3] = Om ** 2
    return g, h, (X, Y, Z)
