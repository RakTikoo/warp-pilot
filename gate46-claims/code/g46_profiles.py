#!/usr/bin/env python3
"""
g46_profiles.py -- Gate-46 profile assembly, written for this gate.

The registered design definitions are re-implemented here from
the programme records (no phase or earlier-gate code is imported):

  * base shift profile: LAM_S * S_ab(r; 2, 2), the incomplete-beta
    plateau on [10, 20];
  * base lapse: 1 + WINNER_A * B_plat(r) (plateau bump, c=15,
    W=5, e=3, smootherstep edges);
  * base M: 1 + 6.0 * (U(r; 8.5, 20) - U(r; 21, 24)), quintic
    smoothstep ramps;
  * A2 totals: base + K=33 not-a-knot correction splines
    (constant extension outside [10, 20]);
  * centre(mu): S -> mu*S, N -> mu*N, M -> 1 + mu*(M-1) on the
    A2 totals; H2 = centre(1.15) + K=17 corrections;
  * per-profile scaling: S -> muS*S, N -> muN*N,
    M -> 1 + muM*(M-1);
  * end-clamp: first/last knots of H2's three correction
    vectors zeroed before the splines are built.

Stored vectors are consumed from the confirmation artefacts
(phase344 A2, phase379 H2) and cross-checked against the state
files. float64. VM only.
"""
import json
import os

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import beta as beta_fn, betainc

DT = np.float64
BETA = 1.1
LAM_S = 0.70
WINNER_A = 0.07439108177516472
R_LO, R_HI = 10.0, 20.0
MU_H2 = 1.15

WP = os.environ.get('G46_WP', '/home/hatch/workspace/warp-pilot')


# ------------------------------------------------------------ shapes
def _ss5(x):
    """Quintic smoothstep and its first two derivatives."""
    v = 6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3
    vp = 30.0 * x ** 4 - 60.0 * x ** 3 + 30.0 * x ** 2
    vpp = 120.0 * x ** 3 - 180.0 * x ** 2 + 60.0 * x
    return v, vp, vpp


def _ramp(r, a, b):
    """U(r; a, b): 0 below a, 1 above b, _ss5 between."""
    r = np.asarray(r, dtype=DT)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r)
    Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss5(x)
        U[mid] = v
        Up[mid] = vp / (b - a)
        Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp


def _smoother(t):
    """H(t) = 10t^3 - 15t^4 + 6t^5 on [0, 1], clamped outside."""
    t = np.asarray(t, dtype=DT)
    v = np.where(t >= 1.0, 1.0, 0.0)
    vp = np.zeros_like(t)
    vpp = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    if np.any(m):
        tm = t[m]
        v[m] = 10.0 * tm ** 3 - 15.0 * tm ** 4 + 6.0 * tm ** 5
        vp[m] = 30.0 * tm ** 2 * (1.0 - tm) ** 2
        vpp[m] = 60.0 * tm * (1.0 - tm) * (1.0 - 2.0 * tm)
    return v, vp, vpp


def _plateau(r, c=15.0, W=5.0, e=3.0):
    r = np.asarray(r, dtype=DT)
    Hx, Hpx, Hppx = _smoother((r - (c - W)) / e)
    Hy, Hpy, Hppy = _smoother(((c + W) - r) / e)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return B, Bp, Bpp


def _s_ab(r, a=2.0, b=2.0):
    """Beta plateau: 1 below 10, 0 above 20,
    1 - I_u(a+1, b+1) between, u = (r-10)/10."""
    r = np.asarray(r, dtype=DT)
    S = np.ones_like(r)
    Sp = np.zeros_like(r)
    Spp = np.zeros_like(r)
    S = np.where(r >= 20.0, 0.0, S)
    m = (r > 10.0) & (r < 20.0)
    if np.any(m):
        u = (r[m] - 10.0) / 10.0
        B = beta_fn(a + 1.0, b + 1.0)
        S[m] = 1.0 - betainc(a + 1.0, b + 1.0, u)
        f = u ** a * (1.0 - u) ** b
        Sp[m] = -f / (10.0 * B)
        fp = (u ** (a - 1.0) * (1.0 - u) ** (b - 1.0)
              * (a * (1.0 - u) - b * u))
        fp = np.where(np.isfinite(fp), fp, 0.0)
        Spp[m] = -fp / (100.0 * B)
    return S, Sp, Spp


# ------------------------------------------------------------ splines
def _corr(vals, K, r):
    """Not-a-knot cubic spline through vals on K knots over
    [10, 20], constant extension outside (derivatives zeroed)."""
    r = np.asarray(r, dtype=DT)
    cs = CubicSpline(np.linspace(R_LO, R_HI, K),
                     np.asarray(vals, dtype=DT), bc_type='not-a-knot')
    rc = np.clip(r, R_LO, R_HI)
    d = cs(rc)
    dp = cs.derivative(1)(rc)
    dpp = cs.derivative(2)(rc)
    out = (r < R_LO) | (r > R_HI)
    if np.any(out):
        dp = np.where(out, 0.0, dp)
        dpp = np.where(out, 0.0, dpp)
    return d, dp, dpp


# ------------------------------------------------------------ stored data
def _vecs_conf(path, key, val):
    conf = json.load(open(path))
    ent = [e for e in conf['confirmations'] if e[key] == val][0]
    return tuple(np.array(ent[k], dtype=DT) for k in ('vS', 'vN', 'vM'))


def _vecs_state(path):
    st = json.load(open(path))
    fi = st['final_incumbent']
    return tuple(np.array(fi[k], dtype=DT) for k in ('vS', 'vN', 'vM'))


def load_a2():
    return _vecs_conf(f'{WP}/phase344/results/p344_confirmation.json',
                      'point', 'A2')


def load_a2_state():
    return _vecs_state(f'{WP}/phase344/results/p344_state_A2.json')


def load_h2():
    return _vecs_conf(f'{WP}/phase379/results/p379_confirmation.json',
                      'centre', 'H2')


def load_h2_state():
    return _vecs_state(f'{WP}/phase379/results/p379_state_H2.json')


# ------------------------------------------------------------ profiles
def base_profiles(r):
    r = np.asarray(r, dtype=DT)
    S, Sp, Spp = _s_ab(r)
    S, Sp, Spp = LAM_S * S, LAM_S * Sp, LAM_S * Spp
    B, Bp, Bpp = _plateau(r)
    N, Np, Npp = 1.0 + WINNER_A * B, WINNER_A * Bp, WINNER_A * Bpp
    U1, U1p, U1pp = _ramp(r, 8.5, 20.0)
    U2, U2p, U2pp = _ramp(r, 21.0, 24.0)
    M = 1.0 + 6.0 * (U1 - U2)
    Mp = 6.0 * (U1p - U2p)
    Mpp = 6.0 * (U1pp - U2pp)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


def _add_corr(prof, vecs, K, r):
    out = []
    for i in range(3):
        d, dp, dpp = _corr(vecs[i], K, r)
        out += [prof[3 * i] + d, prof[3 * i + 1] + dp,
                prof[3 * i + 2] + dpp]
    return tuple(out)


def a2_totals(r):
    return _add_corr(base_profiles(r), load_a2(), 33, r)


def _centre(mu, prof):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)


def h2_totals(r, clamp=False):
    prof = _centre(MU_H2, a2_totals(r))
    vS, vN, vM = load_h2()
    if clamp:
        vecs = []
        for v in (vS, vN, vM):
            w = v.copy()
            w[0] = 0.0
            w[-1] = 0.0
            vecs.append(w)
    else:
        vecs = [vS, vN, vM]
    return _add_corr(prof, vecs, 17, r)


def scaled_profiles(muS, muN, muM, r, clamp=False):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = h2_totals(r, clamp=clamp)
    return (muS * S, muS * Sp, muS * Spp,
            muN * N, muN * Np, muN * Npp,
            1.0 + muM * (M - 1.0), muM * Mp, muM * Mpp)
