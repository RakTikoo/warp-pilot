"""
wa_profiles.py -- Gate-11 W-A profile construction, written fresh in
this gate.  Only shared DEFINITIONS enter as data/text:

  * the two TOV shell profiles are the programme's root definition
    (shell.py build_shell, as in Gates 7/10): outer (5,10), M=1.9125,
    edgepeaked wd=1.0/floor=0.1, s_rho=1.0, s_P=0.58; inner (2,4),
    M=0.765, the x0.4 copy (wd=0.4, s_rho=0.4, s_P=0.232); Nr=4001.
  * the composed background specification (Phase 41/46 text):
    m = m_i + m_o; b = -1/2 ln(1 - 2m/r); the outer pressure is
    re-integrated against the composed m (zero inside R1_outer,
    Gaussian smoothing s_P,outer), the inner pressure is carried
    standalone; a is integrated inward from
    a(rmax) = 1/2 ln(1 - 2 Mtot/rmax) with
    a' = (m/r^2 + 4 pi r P)/(1 - 2m/r); grid Nr=6001 on [0, 3 R2o].
  * the source-modulated chain specification (Phase 50 pattern as
    generalised by Phases 73/80/88, stated in the phase run records):
    per shell, chain grid dr = 2.5e-4 on [0, hi+1] with r_m inserted
    exactly; span [lo, hi] = [R1 - e W, R2 + e W], W = R2 - R1, with
    e = 0.10 for the narrowed outer shell of G11-1 and e = 0.30
    elsewhere (the span parameterisation is part of the shared
    definition, GATE11.md); rhohat = rho_trial/max(rho_trial) from
    the shell's own spline, clipped >= 0; 12 cubic B-splines on knots
    [lo x3, linspace(lo,hi,10), hi x3];
    g0 = rhohat^q tanh((r_m - r)/0.05) exp(sum_i a_i B_i);
    lambda = -I_in/I_out about r_m; the flux F is the cumulative
    integral of g r^2, reset past r_m; S = 1 - k int(F/r^2) dr with
    k = 1/int(F/r^2) dr over the grid.  Design vector: 14 numbers
    (12 a_i, q, r_m), read as DATA from the phase state files.
  * held-W re-equilibration (Phase 46 protocol):
    beta_s^comp = beta_s^alone exp(a_comp(r_mid,s) - a_alone,s(r_mid,s)).

All representations carry ANALYTIC derivatives (spline derivatives);
no finite differences anywhere in this file.
Run with ~/workspace/warp-pilot/venv/bin/python.  float64 everywhere.
"""
import json
import sys

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import BSpline, CubicSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import shell as _shell_mod  # root TOV profile definition (shared definition only)

F64 = np.float64
SWITCH_W = F64(0.05)
CHAIN_DR = F64(2.5e-4)
P88_STATE = '/home/hatch/workspace/warp-pilot/phase88/results/p882_alone_state.json'
P80_STATE = '/home/hatch/workspace/warp-pilot/phase80/results/p803_alone_state.json'


# ---------------------------------------------------------------- shells
def outer_profile():
    return _shell_mod.build_shell(5.0, 10.0, 1.9125, kind='edgepeaked',
                                  params={'wd': 1.0, 'floor': 0.1},
                                  s_rho=1.0, s_P=0.58, Nr=4001)


def inner_profile():
    return _shell_mod.build_shell(2.0, 4.0, 0.765, kind='edgepeaked',
                                  params={'wd': 0.4, 'floor': 0.1},
                                  s_rho=0.4, s_P=0.232, Nr=4001)


# ------------------------------------------------------- composed background
def _pressure_against(r, rho, m, r_cavity, s_P):
    """TOV pressure integrated inward against a given m(r); zero for
    r < r_cavity; RK2 midpoint steps; Gaussian smoothing; clip >= 0."""
    n = len(r)
    P = np.zeros(n, dtype=F64)

    def slope(rr, mm, rh, pp):
        if rr <= 0.0:
            return 0.0
        return -(rh + pp) * (mm / rr**2 + 4.0 * np.pi * rr * pp) / (1.0 - 2.0 * mm / rr)

    for i in range(n - 2, -1, -1):
        if r[i] < r_cavity:
            continue  # P stays 0 inside the cavity radius
        h = r[i + 1] - r[i]
        k1 = slope(r[i + 1], m[i + 1], rho[i + 1], P[i + 1])
        pmid = P[i + 1] - 0.5 * h * k1
        k2 = slope(0.5 * (r[i] + r[i + 1]), 0.5 * (m[i] + m[i + 1]),
                   0.5 * (rho[i] + rho[i + 1]), pmid)
        P[i] = P[i + 1] - h * k2
    P = np.maximum(P, 0.0)
    if s_P > 0:
        P = np.maximum(_shell_mod.gauss_smooth(P, r[1] - r[0], s_P), 0.0)
    return P


def composed_background(prof_o, prof_i, Nr=6001):
    rmax = 3.0 * prof_o['R2']
    r = np.linspace(0.0, rmax, Nr, dtype=F64)
    m = (np.interp(r, prof_i['r'], prof_i['m'], left=0.0, right=prof_i['M'])
         + np.interp(r, prof_o['r'], prof_o['m'], left=0.0, right=prof_o['M']))
    Mtot = prof_i['M'] + prof_o['M']
    rsafe = np.maximum(r, 1e-12)
    u = 1.0 - 2.0 * m / rsafe
    assert float(np.min(u)) > 0.02, f'composed background too compact: min u {np.min(u)}'
    rho_o = np.interp(r, prof_o['r'], prof_o['rho_trial'], left=0.0, right=0.0)
    P = (np.interp(r, prof_i['r'], prof_i['P'], left=0.0, right=0.0)
         + _pressure_against(r, rho_o, m, prof_o['R1'], prof_o['s_P']))
    aprime = np.where(r > 0, (m / rsafe**2 + 4.0 * np.pi * r * P) / np.maximum(u, 1e-300), 0.0)
    a = np.zeros_like(r)
    a[-1] = 0.5 * np.log(max(1.0 - 2.0 * Mtot / r[-1], 1e-300))
    steps = np.diff(r)
    a[:-1] = a[-1] - np.cumsum((0.5 * (aprime[:-1] + aprime[1:]) * steps)[::-1])[::-1]
    b = np.where(r > 0, -0.5 * np.log(np.maximum(u, 1e-300)), 0.0)
    return {'r': r, 'a': a, 'b': b, 'm': m, 'P': P, 'Mtot': Mtot}


# ------------------------------------------------------------------- chain
def span_of(prof, ext):
    W = prof['R2'] - prof['R1']
    return prof['R1'] - ext * W, prof['R2'] + ext * W


def build_chain(prof, x, ext):
    """Source -> flux -> S chain for one shell at span extension ext.
    Returns the chain grid, S on it, and the bookkeeping scalars
    (lambda, k, balance, endpoint residuals S(lo)-1 and S(hi),
    monotonicity violation)."""
    x = np.asarray(x, dtype=F64)
    coef, q, r_m = x[:12], F64(x[12]), F64(x[13])
    lo, hi = span_of(prof, ext)
    r_top = hi + 1.0
    r = np.arange(0.0, r_top + 1e-12, float(CHAIN_DR), dtype=F64)
    if not np.any(r == r_m):
        r = np.unique(np.sort(np.concatenate([r, [r_m]])))
    rho_spl = CubicSpline(prof['r'], prof['rho_trial'])
    rhohat = np.maximum(rho_spl(r), 0.0) / float(np.max(prof['rho_trial']))
    knots = np.concatenate([[lo] * 3, np.linspace(lo, hi, 10), [hi] * 3])
    rc = np.clip(r, lo, hi)
    basis = np.empty((12, len(r)), dtype=F64)
    for i in range(12):
        unit = np.zeros(12); unit[i] = 1.0
        basis[i] = np.nan_to_num(BSpline(knots, unit, 3, extrapolate=False)(rc))
    g0 = (rhohat ** q) * np.tanh((r_m - r) / SWITCH_W) * np.exp(coef @ basis)
    wgt = g0 * r**2
    i_m = int(np.searchsorted(r, r_m))
    lam = -float(np.trapezoid(wgt[:i_m + 1], r[:i_m + 1])) \
        / float(np.trapezoid(wgt[i_m:], r[i_m:]))
    g = np.where(r < r_m, g0, lam * g0)
    Fcum = cumulative_trapezoid(g * r**2, r, initial=0.0)
    F = np.where(r <= r_m, Fcum, Fcum - Fcum[-1])
    Fr2 = np.where(r > 0, F / np.where(r > 0, r, 1.0)**2, 0.0)
    I = cumulative_trapezoid(Fr2, r, initial=0.0)
    k = 1.0 / float(I[-1])
    S = 1.0 - k * I
    S_spl = CubicSpline(r, S)
    bal = float(np.trapezoid(g * r**2, r))
    bal_ref = float(np.trapezoid(np.abs(g) * r**2, r))
    info = {'lam': float(lam), 'k': float(k),
            'balance_rel': abs(bal) / bal_ref,
            'S_lo_minus1': float(S_spl(lo)) - 1.0,
            'S_hi': float(S_spl(hi)),
            'monotone_violation': float(max(0.0, np.max(np.diff(S)))),
            'lo': float(lo), 'hi': float(hi), 'ext': float(ext),
            'r_m': float(r_m), 'q': float(q)}
    return {'r': r, 'S': S, 'info': info, 'spline': S_spl}


def chain_sfunc(chain):
    spl = chain['spline']
    r_top = float(chain['r'][-1])

    def sfunc(rr):
        rr = np.asarray(rr, dtype=F64)
        rc = np.clip(rr, 0.0, r_top)
        S, S1, S2 = spl(rc), spl(rc, 1), spl(rc, 2)
        # Extension beyond the chain grid: the chain's S reaches 0 at
        # r_top with F(r_top) = 0, hence S'(r_top) = -k F/r^2 = 0 in
        # the continuum chain (and g = 0 there, so S'' = 0 too); the
        # phase's own representation clips S to this endpoint value.
        # The faithful analytic extension is therefore S = S' = S'' = 0
        # for r > r_top (freezing the spline's endpoint derivatives
        # instead would manufacture a spurious constant-V' tail).
        out = rr > r_top
        if np.any(out):
            S = np.where(out, 0.0, S)
            S1 = np.where(out, 0.0, S1)
            S2 = np.where(out, 0.0, S2)
        return S, S1, S2
    return sfunc


def cosine_sfunc(R1, R2):
    L = R2 - R1
    kk = np.pi / L

    def sfunc(rr):
        rr = np.asarray(rr, dtype=F64)
        u = np.clip((rr - R1) / L, 0.0, 1.0)
        inside = (rr >= R1) & (rr <= R2)
        S = np.where(rr < R1, 1.0, np.where(rr > R2, 0.0, 0.5 * (1.0 + np.cos(np.pi * u))))
        S1 = np.where(inside, -0.5 * kk * np.sin(np.pi * u), 0.0)
        S2 = np.where(inside, -0.5 * kk * kk * np.cos(np.pi * u), 0.0)
        return S, S1, S2
    return sfunc


# ------------------------------------------------------------- design data
def outer_vector(ext_key, beta_key):
    d = json.load(open(P88_STATE))
    return np.array(d['spans'][ext_key]['betas'][beta_key]['x'], dtype=F64)


def inner_vector(beta_key):
    d = json.load(open(P80_STATE))
    return np.array(d['shells']['inner'][beta_key]['x'], dtype=F64)


def stored_chain_info(which, ext_key=None, beta_key=None):
    if which == 'outer88':
        d = json.load(open(P88_STATE))
        return d['spans'][ext_key]['betas'][beta_key]['chain']
    d = json.load(open(P80_STATE))
    return d['shells'][which][beta_key]['chain']


# ------------------------------------------------------------- held-W sums
def held_w(comp, prof_o, prof_i, beta_o_alone, beta_i_alone):
    """Phase-46 held-W re-equilibration anatomy on the composed background."""
    rmi = 0.5 * (prof_i['R1'] + prof_i['R2'])
    rmo = 0.5 * (prof_o['R1'] + prof_o['R2'])
    ac_i = float(np.interp(rmi, comp['r'], comp['a']))
    aa_i = float(np.interp(rmi, prof_i['r'], prof_i['a']))
    ac_o = float(np.interp(rmo, comp['r'], comp['a']))
    aa_o = float(np.interp(rmo, prof_o['r'], prof_o['a']))
    beta_i = float(beta_i_alone * np.exp(ac_i - aa_i))
    beta_o = float(beta_o_alone * np.exp(ac_o - aa_o))
    W_i = float(beta_i_alone * np.exp(-aa_i))
    W_o = float(beta_o_alone * np.exp(-aa_o))
    return {'r_mid_inner': rmi, 'r_mid_outer': rmo,
            'a_comp_inner_mid': ac_i, 'a_alone_inner_mid': aa_i,
            'a_comp_outer_mid': ac_o, 'a_alone_outer_mid': aa_o,
            'lapse_factor_inner': float(np.exp(ac_i - aa_i)),
            'lapse_factor_outer': float(np.exp(ac_o - aa_o)),
            'beta_i_alone': float(beta_i_alone), 'beta_o_alone': float(beta_o_alone),
            'beta_i_comp': beta_i, 'beta_o_comp': beta_o,
            'W_i_alone': W_i, 'W_o_alone': W_o,
            'W_i_held': float(beta_i * np.exp(-ac_i)),
            'W_o_held': float(beta_o * np.exp(-ac_o)),
            'W_i_rel_err': float(abs(beta_i * np.exp(-ac_i) - W_i) / W_i),
            'W_o_rel_err': float(abs(beta_o * np.exp(-ac_o) - W_o) / W_o),
            'W_payload_sum': float(W_i + W_o),
            'payload_coord': float(beta_o + beta_i),
            'payload_relat': float((beta_o + beta_i) / (1.0 + beta_o * beta_i)),
            'a_comp_payload': float(np.interp(0.5 * prof_i['R1'], comp['r'], comp['a']))}


# ------------------------------------------------------------ audit points
def fib_sphere(ndir, seed):
    rng = np.random.default_rng(seed)
    i = np.arange(ndir, dtype=F64)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / ndir)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i + rng.uniform(0, 0.3)
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


def fib_sphere_det(ndir):
    i = np.arange(ndir, dtype=F64)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / ndir)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


def registered_points(R2o=10.0):
    """The Phase 46/80/88 registered audit pattern (specification text):
    26 Fibonacci directions (seed 11) x 50 radii = 1300 points."""
    dirs = fib_sphere(26, 11)
    rad = list(np.linspace(0.4, 1.45 * R2o, 42))
    rad += [f * R2o for f in (0.21, 0.29, 0.39, 0.45, 0.51, 0.62, 0.78, 0.95)]
    rad = sorted(set(round(float(v), 6) for v in rad if v > 0.3))
    pts = np.concatenate([dirs * rr for rr in rad])
    return pts, np.array(rad, dtype=F64)


def region_name(rr):
    if rr < 2.0:
        return 'payload'
    if rr <= 4.0:
        return 'inner_wall'
    if rr < 5.0:
        return 'cavity'
    if rr <= 10.0:
        return 'outer_wall'
    return 'exterior'
