#!/usr/bin/env python3
"""
g35_rho.py -- Gate-35's OWN rho evaluator for the Phase 314 headline member.

Implemented fresh from the Phase 308 split (CHECKPOINT308, printed in full
there). NO import of p312_lib / p314_lib / p308_lib. The (S, N) profile
FUNCTIONS only are taken from the programme's shape layer, as charged:
  S, S'  <- p258_lib.S_ab(r, a=2, b=2)
  N      <- 1 + A * p274_lib.shape_B_plat(r, c=15, W=5, e=3.0)
(WINNER_SPEC verbatim: plat, a=2, b=2, A=0.07439108177516472, c=15, W=5,
e=3.0; beta = 1.1.)

Member: M(r) = 1 + 4.00*[U(r; 9, 20.5) - U(r; 21, 24)], U = quintic
smoothstep SS(x) = 6x^5 - 15x^4 + 10x^3 on the interval, 0 below, 1 above
(analytic M', M'' from SS' = 30x^2(1-x)^2, SS'' = 60x(1-x)(1-2x)).

Split (Phase 308):  16*pi*rho_req = R + Q_K,
  R  = R1 + R2,  R1 = (2/r^2)(1 - 1/M),  R2 = 2 M'/(r M^2)   [direction-free]
  Q_K = (beta^2/alpha^2) * [ -S'^2 (1-u)/(2M)
                             - 4 (M-1) S S' u/(r M^2)
                             + 2 (M-1)^2 S^2 u/(r^2 M^2)
                             + 2 (M-1) M' S^2 u/(r M^3) ],   u = n_xhat^2
  alpha^2 = N^2 + beta^2 S^2 (1 - ((M-1)/M) u).

Structural note: the Q_K numerator is affine in u and alpha^2 is affine in
u, so at fixed r, rho(u) is a ratio of affine functions of u, hence
monotonic in u (derivative of (A+Bu)/(C+Du) has constant sign); the angular
minimum rho*(r) is attained at an endpoint u in {0, 1}. The driver still
runs the registered fine u-scan + golden polish and checks this.
float64 throughout.
"""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase258/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase274/work')
from p258_lib import S_ab            # noqa: E402  (S profile function only)
from p274_lib import shape_B_plat   # noqa: E402  (N shape function only)

DTYPE = np.float64
BETA = 1.1
A_LAPSE = 0.07439108177516472
SIXTEEN_PI = 16.0 * np.pi


# ------------------------------------------------------------------ (S, N)
def profiles_SN(r):
    """(S, S', N) of the Gate-30 winner at radii r (array-like)."""
    r = np.asarray(r, dtype=DTYPE)
    S, Sp, _Spp = S_ab(r, 2, 2)
    B, _Bp, _Bpp = shape_B_plat(r, 15, 5, 3.0)
    N = 1.0 + A_LAPSE * B
    return S, Sp, N


# ------------------------------------------------------------------ M(r)
def _SS(x):
    return 6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3


def _SSp(x):
    return 30.0 * x ** 2 * (1.0 - x) ** 2


def _SSpp(x):
    return 60.0 * x * (1.0 - x) * (1.0 - 2.0 * x)


def _U(r, a, b):
    x = (np.asarray(r, dtype=DTYPE) - a) / (b - a)
    return np.where(x <= 0.0, 0.0,
                    np.where(x >= 1.0, 1.0, _SS(np.clip(x, 0.0, 1.0))))


def _Up(r, a, b):
    x = (np.asarray(r, dtype=DTYPE) - a) / (b - a)
    return np.where((x > 0.0) & (x < 1.0),
                    _SSp(np.clip(x, 0.0, 1.0)) / (b - a), 0.0)


def _Upp(r, a, b):
    x = (np.asarray(r, dtype=DTYPE) - a) / (b - a)
    return np.where((x > 0.0) & (x < 1.0),
                    _SSpp(np.clip(x, 0.0, 1.0)) / (b - a) ** 2, 0.0)


def M_funcs(r):
    """(M, M', M'') of the headline member at radii r."""
    r = np.asarray(r, dtype=DTYPE)
    M = 1.0 + 4.0 * (_U(r, 9.0, 20.5) - _U(r, 21.0, 24.0))
    Mp = 4.0 * (_Up(r, 9.0, 20.5) - _Up(r, 21.0, 24.0))
    Mpp = 4.0 * (_Upp(r, 9.0, 20.5) - _Upp(r, 21.0, 24.0))
    return M, Mp, Mpp


# ------------------------------------------------------------------ split
def rho_split(r, u):
    """rho_req and its split at scalar/array r and u = n_xhat^2.

    Returns dict of arrays (broadcast): rho, R1, R2, QK -- each the actual
    contribution to rho (i.e. already divided by 16*pi) -- plus alpha2, M,
    Mp, S, Sp, N.
    """
    r = np.asarray(r, dtype=DTYPE)
    u = np.asarray(u, dtype=DTYPE)
    S, Sp, N = profiles_SN(r)
    M, Mp, _Mpp = M_funcs(r)
    R1 = (2.0 / r ** 2) * (1.0 - 1.0 / M)
    R2 = 2.0 * Mp / (r * M ** 2)
    alpha2 = N ** 2 + BETA ** 2 * S ** 2 * (1.0 - ((M - 1.0) / M) * u)
    qk_num = (- Sp ** 2 * (1.0 - u) / (2.0 * M)
              - 4.0 * (M - 1.0) * S * Sp * u / (r * M ** 2)
              + 2.0 * (M - 1.0) ** 2 * S ** 2 * u / (r ** 2 * M ** 2)
              + 2.0 * (M - 1.0) * Mp * S ** 2 * u / (r * M ** 3))
    QK = (BETA ** 2 / alpha2) * qk_num
    rho = (R1 + R2 + QK) / SIXTEEN_PI
    return {'rho': rho, 'R1': R1 / SIXTEEN_PI, 'R2': R2 / SIXTEEN_PI,
            'QK': QK / SIXTEEN_PI, 'alpha2': alpha2, 'M': M, 'Mp': Mp,
            'S': S, 'Sp': Sp, 'N': N}


def rho_ru(r, u):
    return rho_split(r, u)['rho']


# ------------------------------------------------------------------ rho*(r)
def _golden_min(f, a, b, tol=1e-13, maxiter=200):
    """Golden-section minimisation of scalar f on [a, b]."""
    gr = (np.sqrt(5.0) - 1.0) / 2.0
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    fc, fd = f(c), f(d)
    for _ in range(maxiter):
        if b - a < tol:
            break
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = f(d)
    x = 0.5 * (a + b)
    return x, f(x)


def rho_star(r, n_u=2001):
    """rho*(r) = min over u in [0,1] of rho(r, u): fine u-scan (n_u points)
    + golden-section polish of the best bracket. Scalar r.
    Returns (rho_star, u_star)."""
    r = float(r)
    us = np.linspace(0.0, 1.0, n_u)
    vals = rho_ru(r, us)
    i = int(np.argmin(vals))
    if i == 0:
        a, b = us[0], us[1]
    elif i == n_u - 1:
        a, b = us[n_u - 2], us[n_u - 1]
    else:
        a, b = us[i - 1], us[i + 1]
    u_pol, v_pol = _golden_min(lambda uu: float(rho_ru(r, uu)), a, b)
    if v_pol <= float(vals[i]):
        return v_pol, u_pol
    return float(vals[i]), float(us[i])
