"""
wa_profiles.py — Gate-10 W-A profile representations.

Everything here is a shared DEFINITION imported as data/text, rebuilt
fresh in this file (no phase73/phase80/phase46 code is imported or
executed; the only programme import is shell.py's build_shell, the
programme's root TOV profile definition, exactly as Gate-7 used it):

  * per-shell TOV profiles: frontier class — outer (5,10) M=1.9125
    edgepeaked wd=1.0/floor=0.1 s_rho=1.0 s_P=0.58; inner (2,4)
    M=0.765 x0.4 copy (wd=0.4, s_rho=0.4, s_P=0.232), Nr=4001
    (Phase 46/80 composition specification).
  * composed background, rebuilt here from the Phase-41/46 spec text:
    m_comp = m_i + m_o; b_comp = -1/2 ln(1-2 m_comp/r); outer TOV
    pressure re-integrated against m_comp (zero inside R1_outer,
    Gaussian-smoothed s_P,outer); inner pressure carried standalone;
    a_comp integrated inward from a(rmax)=1/2 ln(1-2Mtot/rmax) with
    a' = (m/r^2 + 4 pi r P)/(1-2m/r). Nr=6001 on [0, 3*R2o].
  * source-modulated shift chain, rebuilt here from the registered
    specification (phase50 p501_recon pattern as generalised by
    Phase 73/80, stated in p803_lib.py's docstring): per shell,
    chain grid dr=2.5e-4 on [0, hi+1], hi=R2+0.3W, lo=R1-0.3W,
    r_m inserted exactly; rhohat = rho(r)/max(rho) from the shell's
    own rho_trial spline, clipped >= 0; 12 cubic B-splines, knots
    [lo,lo,lo, linspace(lo,hi,10), hi,hi,hi];
    g0 = rhohat^q * tanh((r_m-r)/0.05) * exp(sum a_i B_i);
    lambda = -I_in/I_out; F cumulative, reset past r_m;
    S = 1 - k * int(F/r^2) dr, k = 1/int(F/r^2). Design vector:
    14 numbers (12 a_i, q, r_m), read as DATA from
    ../phase80/results/p803_economics.json.
  * cosine window (the Phase-46 control's S), closed form.
  * held-W re-equilibration (Phase 46 protocol): beta_s^comp =
    beta_s^alone * exp(a_comp(r_mid,s) - a_alone,s(r_mid,s)).

Profile representations evaluated with ANALYTIC derivatives:
a, b, S are cubic splines; their 1st/2nd derivatives are the splines'
own analytic derivatives. No finite differences anywhere.
Run with ~/workspace/warp-pilot/venv/bin/python. float64 everywhere.
"""
import json, sys
import numpy as np
from scipy.interpolate import BSpline, CubicSpline
from scipy.integrate import cumulative_trapezoid

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import shell as sh  # root programme TOV profile definition (shared definition)

DTYPE = np.float64
W_SWITCH = DTYPE(0.05)
DR = DTYPE(2.5e-4)
ECON = '/home/hatch/workspace/warp-pilot/phase80/results/p803_economics.json'


def frontier_outer():
    return sh.build_shell(5.0, 10.0, 1.9125, kind='edgepeaked',
                          params={'wd': 1.0, 'floor': 0.1},
                          s_rho=1.0, s_P=0.58, Nr=4001)


def frontier_inner():
    return sh.build_shell(2.0, 4.0, 0.765, kind='edgepeaked',
                          params={'wd': 0.4, 'floor': 0.1},
                          s_rho=0.4, s_P=0.232, Nr=4001)


# ---------------------------------------------------------------- composed background
def _tov_pressure(r, rho, m, R1_cav, s_P):
    """TOV pressure loop (build_shell pattern): inward from rmax,
    P=0 for r < R1_cav, then Gaussian smoothing + clip."""
    Nr = len(r)
    P = np.zeros_like(r)
    for i in range(Nr - 2, -1, -1):
        if r[i] < R1_cav:
            P[i] = 0.0
            continue
        def dpdr(rr, mm, rh, PP):
            if rr <= 0:
                return 0.0
            uu = 1.0 - 2 * mm / rr
            return -(rh + PP) * (mm / rr ** 2 + 4 * np.pi * rr * PP) / uu
        hs = r[i + 1] - r[i]
        k1 = dpdr(r[i + 1], m[i + 1], rho[i + 1], P[i + 1])
        Pm = P[i + 1] - 0.5 * hs * k1
        rm_ = 0.5 * (r[i] + r[i + 1]); mm_ = 0.5 * (m[i] + m[i + 1])
        rh_ = 0.5 * (rho[i] + rho[i + 1])
        k2 = dpdr(rm_, mm_, rh_, Pm)
        P[i] = P[i + 1] - hs * k2
    P = np.maximum(P, 0.0)
    if s_P > 0:
        P = sh.gauss_smooth(P, r[1] - r[0], s_P)
        P = np.maximum(P, 0.0)
    return P


def build_composed(prof_o, prof_i, Nr=6001):
    """Composed background (a_comp, b_comp) per the Phase-41/46 spec."""
    R1o, R2o = prof_o['R1'], prof_o['R2']
    R1i, R2i = prof_i['R1'], prof_i['R2']
    assert R2i < R1o
    rmax = 3.0 * R2o
    r = np.linspace(0.0, rmax, Nr, dtype=DTYPE)
    m_i = np.interp(r, prof_i['r'], prof_i['m'], left=0.0, right=prof_i['M'])
    m_o = np.interp(r, prof_o['r'], prof_o['m'], left=0.0, right=prof_o['M'])
    m = m_i + m_o
    Mtot = prof_i['M'] + prof_o['M']
    u = 1.0 - 2.0 * m / np.maximum(r, 1e-12)
    assert np.min(u) > 0.02, f'composed too compact: min u={np.min(u)}'
    rho_o = np.interp(r, prof_o['r'], prof_o['rho_trial'], left=0.0, right=0.0)
    P_o = _tov_pressure(r, rho_o, m, R1o, prof_o['s_P'])
    P_i = np.interp(r, prof_i['r'], prof_i['P'], left=0.0, right=0.0)
    P = P_i + P_o
    aprime = np.where(r > 0, (m / np.maximum(r, 1e-12) ** 2
                              + 4 * np.pi * r * P) / np.maximum(u, 1e-300), 0.0)
    a = np.zeros_like(r)
    a[-1] = 0.5 * np.log(max(1.0 - 2 * Mtot / r[-1], 1e-300))
    for i in range(Nr - 2, -1, -1):
        a[i] = a[i + 1] - 0.5 * (aprime[i] + aprime[i + 1]) * (r[i + 1] - r[i])
    b = np.where(r > 0, -0.5 * np.log(np.maximum(u, 1e-300)), 0.0)
    return {'r': r, 'a': a, 'b': b, 'm': m, 'P': P, 'Mtot': Mtot,
            'R1o': R1o, 'R2o': R2o, 'R1i': R1i, 'R2i': R2i}


# ---------------------------------------------------------------- source chain
def shell_span(prof):
    W = prof['R2'] - prof['R1']
    return prof['R1'] - 0.3 * W, prof['R2'] + 0.3 * W


def chain(prof, x):
    """Source->flux->shift chain for one shell (registered spec)."""
    x = np.asarray(x, dtype=DTYPE)
    a_i, q, r_m = x[:12], DTYPE(x[12]), DTYPE(x[13])
    lo, hi = shell_span(prof)
    rmax = hi + 1.0
    r = np.arange(0.0, rmax + 1e-12, float(DR), dtype=DTYPE)
    if not np.any(r == r_m):
        r = np.unique(np.sort(np.r_[r, r_m]))
    rho_s = CubicSpline(prof['r'], prof['rho_trial'])
    rho_max = float(np.max(prof['rho_trial']))
    rhohat = np.maximum(rho_s(r), 0.0) / rho_max
    knots = np.r_[[lo] * 3, np.linspace(lo, hi, 10), [hi] * 3]
    rc = np.clip(r, lo, hi)
    B = np.array([BSpline(knots, np.eye(12)[i], 3, extrapolate=False)(rc)
                  for i in range(12)])
    B = np.nan_to_num(B)
    g0 = (rhohat ** q) * np.tanh((r_m - r) / W_SWITCH) * np.exp(a_i @ B)
    u = g0 * r ** 2
    i_m = int(np.searchsorted(r, r_m))
    I_in = float(np.trapezoid(u[:i_m + 1], r[:i_m + 1]))
    I_out = float(np.trapezoid(u[i_m:], r[i_m:]))
    lam = -I_in / I_out
    g = np.where(r < r_m, g0, lam * g0)
    Fcum = cumulative_trapezoid(g * r ** 2, r, initial=0.0)
    F = np.where(r <= r_m, Fcum, Fcum - Fcum[-1])
    with np.errstate(divide='ignore', invalid='ignore'):
        Fr2 = np.where(r > 0, F / r ** 2, 0.0)
    I = cumulative_trapezoid(Fr2, r, initial=0.0)
    k = 1.0 / float(I[-1])
    S = 1.0 - k * I
    bal = float(np.trapezoid(g * r ** 2, r))
    bal_ref = float(np.trapezoid(np.abs(g) * r ** 2, r))
    return {'r': r, 'S': S, 'lam': float(lam), 'k': float(k),
            'balance_rel': abs(bal) / bal_ref, 'rmax': float(rmax)}


def design_vectors(row_key):
    """Per-shell 14-number design vectors, as DATA from the Phase-80
    economics file."""
    d = json.load(open(ECON))
    row = d['rows'][row_key]
    return (np.array(row['x_outer'], dtype=DTYPE),
            np.array(row['x_inner'], dtype=DTYPE), row)


# ---------------------------------------------------------------- S representations
def src_sfunc(prof, x):
    """Returns (sfunc, chain_dict); sfunc(r) -> (S, S', S'') with the
    spline's own analytic derivatives."""
    ch = chain(prof, x)
    spl = CubicSpline(ch['r'], ch['S'])
    rmax = ch['rmax']

    def sfunc(r):
        r = np.asarray(r, dtype=DTYPE)
        rc = np.clip(r, 0.0, rmax)
        return spl(rc), spl(rc, 1), spl(rc, 2)
    return sfunc, ch


def cosine_sfunc(R1, R2):
    L = R2 - R1
    k = np.pi / L

    def sfunc(r):
        r = np.asarray(r, dtype=DTYPE)
        u = (r - R1) / L
        inside = (r >= R1) & (r <= R2)
        uc = np.clip(u, 0, 1)
        S = np.where(r < R1, 1.0, np.where(r > R2, 0.0, 0.5 * (1.0 + np.cos(np.pi * uc))))
        Sp = np.where(inside, -0.5 * k * np.sin(np.pi * uc), 0.0)
        Spp = np.where(inside, -0.5 * k * k * np.cos(np.pi * uc), 0.0)
        return S, Sp, Spp
    return sfunc


# ---------------------------------------------------------------- held-W economics
def held_betas(comp, prof_o, prof_i, beta_o_alone, beta_i_alone):
    """Dual held-W re-equilibration on the composed background."""
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
    a_pay = float(np.interp(0.5 * prof_i['R1'], comp['r'], comp['a']))
    return {
        'r_mid_inner': rmi, 'r_mid_outer': rmo,
        'a_comp_inner_mid': ac_i, 'a_alone_inner_mid': aa_i,
        'a_comp_outer_mid': ac_o, 'a_alone_outer_mid': aa_o,
        'lapse_factor_inner': float(np.exp(ac_i - aa_i)),
        'lapse_factor_outer': float(np.exp(ac_o - aa_o)),
        'beta_i_alone': beta_i_alone, 'beta_o_alone': beta_o_alone,
        'beta_i_comp': beta_i, 'beta_o_comp': beta_o,
        'W_i_alone': W_i, 'W_o_alone': W_o,
        'W_i_held': float(beta_i * np.exp(-ac_i)),
        'W_o_held': float(beta_o * np.exp(-ac_o)),
        'W_i_rel_err': float(abs(beta_i * np.exp(-ac_i) - W_i) / W_i),
        'W_o_rel_err': float(abs(beta_o * np.exp(-ac_o) - W_o) / W_o),
        'W_payload_sum': float(W_i + W_o),
        'payload_coord': float(beta_o + beta_i),
        'payload_relat': float((beta_o + beta_i) / (1 + beta_o * beta_i)),
        'a_comp_payload': a_pay,
    }


# ---------------------------------------------------------------- point set / regions
def fib_dirs(ndir, seed=0):
    """Registered audit directions (Phase-41/46 pattern, as spec text)."""
    rng = np.random.default_rng(seed)
    i = np.arange(ndir, dtype=DTYPE)
    phi = np.arccos(1 - 2 * (i + 0.5) / ndir)
    th = np.pi * (1 + 5 ** 0.5) * i + rng.uniform(0, 0.3)
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


def audit_points(R2o, seed=11):
    """The Phase 46/80 registered audit pattern: 26 Fibonacci
    directions (seed 11) x 50 radii = 1300 points."""
    dirs = fib_dirs(26, seed)
    rad = list(np.linspace(0.4, 1.45 * R2o, 42))
    rad += [f * R2o for f in (0.21, 0.29, 0.39, 0.45, 0.51, 0.62, 0.78, 0.95)]
    rad = sorted(set(round(float(x), 6) for x in rad if x > 0.3))
    return np.concatenate([dirs * rr for rr in rad]), np.array(rad)


def region_of(r):
    if r < 2.0:
        return 'payload'
    if r <= 4.0:
        return 'inner_wall'
    if r < 5.0:
        return 'cavity'
    if r <= 10.0:
        return 'outer_wall'
    return 'exterior'
