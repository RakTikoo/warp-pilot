"""
x2_bg.py — X2 (background curvature) + Lens E (expansion), shared engine.

Ansatz: Finalist A shell (spherical profiles a(r), b(r), cosine shift
along x, design beta=0.02) superposed on a background written in
Painleve-Gullstrand / static form:
    g_tt = g_tt^bg(r) * exp(2 a_sh(r))
    g_ti = g_ti^bg(x) - S(r) beta_w (x-hat)_i
    gamma_ij = gamma_ij^bg(x) + (exp(2 b_sh(r)) - 1) n_i n_j
Backgrounds:
  flat : g_tt=-1, g_ti=0, gamma=delta          (control: = Finalist A)
  schw : PG Schwarzschild, mass Mbg (horizon 2Mbg < R1, BH in cavity):
         g_tt = -(1-2Mbg/r), g_ti = sqrt(2Mbg/r) n_i, gamma = delta.
         Vacuum: T_bg = 0 exactly.
  ds   : PG de Sitter (river form), H = const:
         g_tt = -(1 - H^2 r^2), g_ti = -H x_i, gamma = delta.
         T_bg = Lambda term: rho = 3H^2/8pi, p = -rho (NEC saturated,
         SEC violated BY THE BACKGROUND ITSELF — E2 framing; flagged).
  ads  : static AdS, radius L:
         g_tt = -(1 + r^2/L^2), g_ti = 0,
         gamma = delta - (r^2/L^2)/(1 + r^2/L^2) n n.  rho_bg < 0.
The auditor is verify_metric.einstein_at_points (stationary). The dS
river form is stationary and IS de Sitter; a general FLRW instant with
H = H(t0) frozen coincides with it at the snapshot level (Hdot terms
are outside this audit — logged limitation, N3-style snapshot logic).

Diagnostics per config: total-T margins (physical), background-only
margins at the same points, and DIFFERENCE-tensor margins
(T_tot - T_bg in the total metric's Eulerian frame — the shell's own
contribution, diagnostic label). Points: radii 3..30 x 26 Fibonacci
directions (subsampled), h=0.3 screen.
"""
import json, sys, time
import numpy as np
from scipy.interpolate import CubicSpline

import shell as sh
import verify_metric as vm
from verify_finalist import fib_dirs

DTYPE = np.float64
R1, R2 = 10.0, 20.0

_prof = sh.build_shell(R1, R2, 2.0, kind='edgepeaked',
                       params={'wd': 3.0, 'floor': 0.2},
                       s_rho=2.0, s_P=1.16, Nr=4001)
_A = CubicSpline(_prof['r'], _prof['a'])
_B = CubicSpline(_prof['r'], _prof['b'])
_RMAX = float(_prof['r'][-1])


def bg_terms(bg, pts):
    """Returns g_tt_bg (P,), g_ti_bg (P,3), gamma_bg (P,3,3)."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    rs = np.where(r > 0, r, 1.0)
    n = pts / rs[:, None]
    kind = bg[0]
    gam = np.tile(np.eye(3), (P, 1, 1)).astype(DTYPE)
    gti = np.zeros((P, 3), dtype=DTYPE)
    if kind == 'flat':
        gtt = -np.ones(P)
    elif kind == 'schw':
        Mbg = bg[1]
        gtt = -(1.0 - 2.0 * Mbg / rs)
        amp = np.sqrt(2.0 * Mbg / rs)
        gti = amp[:, None] * n
    elif kind == 'ds':
        H = bg[1]
        gtt = -(1.0 - (H * r) ** 2)
        gti = -H * pts
    elif kind == 'ads':
        L = bg[1]
        gtt = -(1.0 + (r / L) ** 2)
        f = ((r / L) ** 2) / (1.0 + (r / L) ** 2)
        gam = gam - f[:, None, None] * n[:, :, None] * n[:, None, :]
    else:
        raise ValueError(kind)
    return gtt, gti, gam


def make_gfunc(bg, beta_w, shell_on=True):
    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = len(pts)
        r = np.linalg.norm(pts, axis=1)
        rs = np.where(r > 0, r, 1.0)
        n = pts / rs[:, None]
        gtt_b, gti_b, gam_b = bg_terms(bg, pts)
        if shell_on:
            rc = np.clip(r, 0.0, _RMAX)
            a = _A(rc); b = _B(rc)
            S = sh.shift_S(r, R1, R2, 'cos', 1.0, [R1, R2])
        else:
            a = np.zeros(P); b = np.zeros(P); S = np.zeros(P)
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = gtt_b * np.exp(2 * a)
        g[:, 0, 1:] = gti_b
        g[:, 0, 1] -= S * beta_w
        g[:, 1:, 0] = g[:, 0, 1:]
        eb = np.exp(2 * b) - 1.0
        g[:, 1:, 1:] = gam_b + eb[:, None, None] * n[:, :, None] * n[:, None, :]
        return g

    return gfunc


def sample_points(seed=2024):
    dirs = fib_dirs(26)
    rad = np.linspace(3.0, 30.0, 55)
    pts = np.concatenate([dirs * r for r in rad])
    return pts.astype(DTYPE)


def margins_of(That):
    m = vm.hawking_ellis_margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9, 1e-3 * abs(rho_peak))
    sig = scale > thr
    out = {'rho_peak': rho_peak, 'n_sig': int(sig.sum())}
    if sig.sum():
        for k in ('nec', 'wec', 'sec', 'dec'):
            out[k] = float(np.min(m[k][sig]))
        out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
        out['typeI_frac_sig'] = float(np.mean(m['typeI'][sig]))
    return out


def audit(bg, beta_w, pts, h=0.3):
    gf_t = make_gfunc(bg, beta_w, shell_on=True)
    G_t, That_t, _ = vm.einstein_at_points(gf_t, pts, h=h)
    gf_b = make_gfunc(bg, 0.0, shell_on=False)
    G_b, That_b, _ = vm.einstein_at_points(gf_b, pts, h=h)
    # difference tensor in the TOTAL Eulerian frame
    T_diff = (G_t - G_b) / vm.EIGHT_PI
    g_t = gf_t(pts)
    That_d = vm.eulerian_that(g_t, T_diff)
    return {'total': margins_of(That_t), 'bg_only': margins_of(That_b),
            'diff': margins_of(That_d),
            'bg_max_abs_T': float(np.max(np.abs(That_b)))}


def validate():
    pts = sample_points()
    print('--- controls ---')
    r = audit(('flat',), 0.02, pts)
    print('flat bg + shell (must reproduce Finalist A, NEC ~ +2.12e-5):',
          json.dumps(r['total'], default=float))
    r = audit(('schw', 4.0), 0.0, pts)
    print('schw Mbg=4, no shell: bg max|T| =', r['bg_max_abs_T'],
          '(vacuum, expect ~1e-8 FD noise)')
    r = audit(('ds', 0.05), 0.0, pts)
    print('dS H=0.05, no shell: bg margins (expect NEC ~ 0 saturated,',
          'rho=3H^2/8pi=2.98e-4):', json.dumps(r['bg_only'], default=float))
    r = audit(('ads', 30.0), 0.0, pts)
    print('AdS L=30, no shell: bg margins (expect rho<0):',
          json.dumps(r['bg_only'], default=float))


if __name__ == '__main__':
    validate()
