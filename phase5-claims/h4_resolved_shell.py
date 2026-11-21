"""
h4_resolved_shell.py — Phase 5, H4: BACKGROUND-RE-SOLVED SHELL.
(Phase 1 X2 / Lens E reopening.)

Phase 1's X2 SUPERPOSED the verified Finalist A shell onto
Schwarzschild/AdS backgrounds (multiplicative lapse x additive
shift — not solution-generating) and the shell failed monotonically,
already at beta=0 (-9.9e-5 at M_bg=1 vs exactly 0 in flat space).
Here the shell is RE-SOLVED in the background: its profiles are
re-equilibrated in the background's geometry instead of superposed.

Construction (conditions-first, generalising n3_invert.py):
  total static metric
      ds^2 = -e^{2 Phi(r)} dt^2 + dr^2/(1 - 2 m(r)/r) + r^2 dOmega^2
      m(r)   = m_bg(r) + m_sh(r),     Phi(r) = Phi_bg(r) + a_sh(r).
  Backgrounds:
      schw: m_bg = M_bg const, Phi_bg = 1/2 ln(1 - 2 M_bg/r),
            M_bg in {1, 2, 4};  rho_bg = p_bg = 0.
      ads : 1 - 2 m/r = 1 + r^2/L^2, i.e. m_bg = -r^3/(2 L^2),
            Phi_bg = 1/2 ln(1 + r^2/L^2), L = 30;
            rho_bg = -3/(8 pi L^2) < 0, p_bg = +3/(8 pi L^2).
      flat: M_bg = 0 control.
  Prescribed shell eigenvalue fields on areal r: rho*(r) >= 0 with
  Finalist A's edge-peaked shape and p_t*(r) from Finalist A's
  realised profile (build_shell, frozen finalist_A.json), windowed
  by a C^infty bump taper that is 1 on [10, 20] and 0 outside
  [9, 21] (support ~ [10, 20]; the taper eats only the Gaussian-
  smoothing tails, never the edge peaks; C^infty so the taper
  injects no finite-difference artefact of its own — a C^2
  smootherstep window was tried first and produced a spurious
  -1.2e-6 NEC reading at r=21 in the flat control, where the exact
  1D tensor is zero to 1e-11).  Total fields:
      rho_tot = rho_bg + rho*,   p_t,tot = p_bg + s * p_t*.
  m_sh from rho* (m' = 4 pi r^2 rho).  p_r,tot is solved from
  conservation IN THE TOTAL GEOMETRY,
      p_r' = -(rho + p_r) Phi' - (2/r)(p_r - p_t),
      Phi' = (m + 4 pi r^3 p_r) / (r (r - 2 m)),
  integrated OUTWARD from the inner support edge (stable direction,
  n3_invert) with p_r = p_bg at the inner edge; the second boundary
  condition p_r = p_bg at the outer edge (for Schwarzschild p_bg=0:
  exactly the pre-registered p_r(R1) = p_r(R2) = 0) is ONE scalar
  equation for the prescription scale s — solved by secant with a
  bracket-scan fallback (n3_invert pattern).  Realisability is
  reported (shoot residual + exact-Einstein realisation residual),
  never hidden.  Cavity (r < 9) and exterior (r > 21) are exactly
  the background (plus the constant matching offset a_sh(9) in the
  cavity; exterior Phi matched to 1/2 ln(1 - 2 m_tot/rmax) at
  rmax = 60, the exact vacuum/Lambda continuation).

  Moving metric for the judge (Cartesian):
      g_tt = -e^{2 Phi},  g_tx = -S(r) beta,
      gamma_ij = delta_ij + ((1 - 2m/r)^{-1} - 1) n_i n_j,
  S = cosine window on [10, 20], beta in {0, 0.02}.  Judged with
  verify_metric.einstein_at_points + hawking_ellis_margins on the
  TOTAL tensor and (diagnostic) the DIFFERENCE tensor
  (G_tot - G_bg)/8pi in the total Eulerian frame, x2_bg pattern.
  Margin threshold convention copied verbatim from x2_bg.margins_of:
  a point is significant iff max|That| > max(1e-9, 1e-3 |rho_peak|).
  Verdicts are reported PER REGION (cavity r<9, shell 9<=r<=21,
  exterior r>21) at three stencil widths h in {0.3, 0.2, 0.1}: a
  deficit that shrinks toward 0 under h-refinement is FD floor,
  not physics; a deficit constant in h is physics.  For beta=0 the
  exact spherical (1D, FD-free) margins are the ground truth and
  the 3D judge is the cross-check.

LIMIT (stated, per brief): static areal coordinates are singular
at r = 2 M_bg.  All audit radii satisfy r >= 2 M_bg + 1.5, and the
judge's nested stencil reaches at most 4h = 1.2 inward, so no
sampled point or stencil node crosses r = 2 M_bg + 0.3.  The
comparison to X2 is at VERDICT level (pass/fail + margins), not
component level (different slicing: X2 used Painleve-Gullstrand).

Kill criterion (pre-registered in CHECKPOINT5.md, binding): if the
re-solved shell fails at every tested (beta, M_bg) [and the AdS
row] AND the binding-margin anatomy matches the superposition's
(same failure site, same sign, comparable scaling in M_bg), X2's
reopening is CLOSED.  Any pass (all margins > numerical error at
two resolutions, Type I) => CANDIDATE UNDER ATTACK: adversarial
point hunt + second resolution before it is reported as standing.

float64 everywhere.  Python: system python3 (numpy 2.2.6,
scipy 1.14.1).
"""
import json
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')

import shell as sh          # noqa: E402
import verify_metric as vm  # noqa: E402

DTYPE = np.float64
R1, R2 = 10.0, 20.0          # nominal shell support
S_LO, S_HI = 9.0, 21.0       # windowed support (taper edges)
RMAX = 60.0
NR = 6001                    # solve grid, dr = 0.01
EIGHT_PI = 8.0 * np.pi

# ---------------------------------------------------------------------------
# Prescription: Finalist A realised (rho, p_t), windowed to [9, 21]
# ---------------------------------------------------------------------------
_base = sh.build_shell(R1, R2, 2.0, kind='edgepeaked',
                       params={'wd': 3.0, 'floor': 0.2},
                       s_rho=2.0, s_P=1.16, Nr=4001)
_rb = _base['r']
_rho_s = CubicSpline(_rb, _base['rho_ex'])
_pt_s = CubicSpline(_rb, _base['p_t'])


def _bump(u):
    """C^infty smoothstep: 0 for u<=0, 1 for u>=1."""
    u = np.asarray(u, dtype=DTYPE)
    out = np.where(u >= 1.0, 1.0, 0.0)
    mid = (u > 0.0) & (u < 1.0)
    if np.any(mid):
        um = u[mid]
        f1 = np.exp(-1.0 / um)
        f2 = np.exp(-1.0 / (1.0 - um))
        out = out.copy()
        out[mid] = f1 / (f1 + f2)
    return out


def _window(r):
    return _bump((r - S_LO) / (R1 - S_LO)) * _bump((S_HI - r) / (S_HI - R2))


def rho_star(r):
    r = np.asarray(r, dtype=DTYPE)
    return np.maximum(_rho_s(np.clip(r, 0.0, _rb[-1])), 0.0) * _window(r)


def pt_star(r):
    r = np.asarray(r, dtype=DTYPE)
    return _pt_s(np.clip(r, 0.0, _rb[-1])) * _window(r)


# ---------------------------------------------------------------------------
# Backgrounds
# ---------------------------------------------------------------------------
def bg_fields(bg, r):
    """Returns (m_bg, Phi_bg, rho_bg, p_bg) at areal radii r (arrays).
    Phi_bg for 'schw' is only meaningful for r > 2 M_bg."""
    r = np.asarray(r, dtype=DTYPE)
    kind = bg[0]
    if kind == 'flat':
        return (np.zeros_like(r), np.zeros_like(r),
                np.zeros_like(r), np.zeros_like(r))
    if kind == 'schw':
        M = bg[1]
        u = 1.0 - 2.0 * M / np.maximum(r, 1e-12)
        Phi = np.where(r > 2.0 * M, 0.5 * np.log(np.maximum(u, 1e-300)), 0.0)
        return (np.full_like(r, M), Phi, np.zeros_like(r), np.zeros_like(r))
    if kind == 'ads':
        L = bg[1]
        m = -r ** 3 / (2.0 * L * L)
        Phi = 0.5 * np.log(1.0 + (r / L) ** 2)
        rho = np.full_like(r, -3.0 / (EIGHT_PI * L * L))
        p = np.full_like(r, +3.0 / (EIGHT_PI * L * L))
        return m, Phi, rho, p
    raise ValueError(kind)


def bg_Phi(bg, r):
    return bg_fields(bg, r)[1]


def bg_m(bg, r):
    return bg_fields(bg, r)[0]


# ---------------------------------------------------------------------------
# Re-solve the shell in the background
# ---------------------------------------------------------------------------
def _integrate_pr(r, m, rho, pt, p_r_in):
    """Outward RK2 (midpoint) integration of the conservation ODE on
    the shell grid, p_r(r[0]) = p_r_in.  Plain-float loop (shooting
    hot path), following n3_invert._integrate_pr."""
    Nr = len(r)
    rl = r.tolist(); ml = m.tolist(); hl = rho.tolist(); tl = pt.tolist()
    pr = [0.0] * Nr
    pr[0] = p_r_in
    pi4 = 4.0 * np.pi
    for i in range(Nr - 1):
        h = rl[i + 1] - rl[i]
        ri = rl[i]; pp = pr[i]
        uu = ri - 2.0 * ml[i]
        ap = (ml[i] + pi4 * ri ** 3 * pp) / (ri * uu)
        k1 = -(hl[i] + pp) * ap - (2.0 / ri) * (pp - tl[i])
        pm = pp + 0.5 * h * k1
        rm_ = 0.5 * (ri + rl[i + 1]); mm_ = 0.5 * (ml[i] + ml[i + 1])
        rh_ = 0.5 * (hl[i] + hl[i + 1]); pt_ = 0.5 * (tl[i] + tl[i + 1])
        uu = rm_ - 2.0 * mm_
        ap = (mm_ + pi4 * rm_ ** 3 * pm) / (rm_ * uu)
        k2 = -(rh_ + pm) * ap - (2.0 / rm_) * (pm - pt_)
        pr[i + 1] = pp + h * k2
        if not np.isfinite(pr[i + 1]) or abs(pr[i + 1]) > 1e-1:
            pr[i + 1] = np.nan
            break
    return np.array(pr, dtype=DTYPE)


def solve_in_background(bg, shell_on=True):
    """Returns prof dict: solve grid, m_tot, Phi, a_sh, p_r, shooting
    diagnostics, realisation residual, exact static 1D margins."""
    r = np.linspace(0.0, RMAX, NR, dtype=DTYPE)
    m_bg, _, rho_bg, p_bg = bg_fields(bg, r)
    if shell_on:
        rs = rho_star(r); pts_ = pt_star(r)
    else:
        rs = np.zeros_like(r); pts_ = np.zeros_like(r)
    rho_tot = rho_bg + rs
    m_sh = sh.cumint(4.0 * np.pi * r ** 2 * rs, r)
    m_tot = m_bg + m_sh
    u = 1.0 - 2.0 * m_tot / np.maximum(r, 1e-12)
    band_all = (r >= S_LO) & (r <= S_HI)
    umin_band = float(np.min(u[band_all]))

    i_lo = int(np.argmin(np.abs(r - S_LO)))
    i_hi = int(np.argmin(np.abs(r - S_HI)))
    rsh = r[i_lo:i_hi + 1]
    msh_ = m_tot[i_lo:i_hi + 1]
    rhosh = rho_tot[i_lo:i_hi + 1]
    ptsh0 = pts_[i_lo:i_hi + 1]
    ptbg = float(p_bg[i_lo])
    p_in = float(p_bg[i_lo])          # p_r(inner edge) = background value
    p_target = float(p_bg[i_hi])      # p_r(outer edge) = background value

    if shell_on:
        def F(s):
            pr = _integrate_pr(rsh, msh_, rhosh, ptbg + s * ptsh0, p_in)
            return float(pr[-1] - p_target)

        s_sol, Fval, shot = None, None, 'failed'
        x0, x1 = 1.0, 2.0
        f0, f1 = F(x0), F(x1)
        for _ in range(15):
            if np.isfinite(f1) and abs(f1) < 1e-12:
                s_sol, Fval, shot = x1, f1, 'secant'
                break
            if not (np.isfinite(f0) and np.isfinite(f1)) or f1 == f0:
                break
            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
            if abs(x2 - x1) > 60.0:
                break
            x0, f0, x1, f1 = x1, f1, x2, F(x2)
        if s_sol is None:
            grid = np.linspace(-3.0, 40.0, 216)
            vals = np.array([F(x) for x in grid])
            ok = np.isfinite(vals)
            done = False
            for i in range(len(grid) - 1):
                if ok[i] and ok[i + 1] and vals[i] * vals[i + 1] < 0:
                    s_sol = float(brentq(F, grid[i], grid[i + 1],
                                         xtol=1e-13, rtol=1e-12))
                    Fval = F(s_sol); shot = 'brentq-scan'; done = True
                    break
            if not done:
                i = int(np.nanargmin(np.abs(np.where(ok, vals, np.inf))))
                s_sol, Fval = float(grid[i]), float(vals[i])
                shot = 'scan-argmin (NOT realised)'
        pr_sh = _integrate_pr(rsh, msh_, rhosh, ptbg + s_sol * ptsh0, p_in)
    else:
        s_sol, Fval, shot = 0.0, 0.0, 'shell-off'
        pr_sh = np.full_like(rsh, p_in)

    # --- assemble p_r, Phi on the full grid -------------------------------
    p_r = p_bg.copy()
    p_r[i_lo:i_hi + 1] = pr_sh
    _es = np.errstate(all='ignore')
    _es.__enter__()
    Phi_prime = np.zeros_like(r)
    rr = np.maximum(r, 1e-12)
    denom = rr * (rr - 2.0 * m_tot)
    Phi_prime[:] = (m_tot + 4.0 * np.pi * rr ** 3 * p_r) / denom
    Phi_prime[0] = 0.0
    # a_sh: zero derivative in the cavity (Phi' = Phi_bg' there);
    # integrate (Phi' - Phi_bg') inward from rmax with the exact
    # exterior matching Phi(rmax) = 1/2 ln(1 - 2 m_tot(rmax)/rmax).
    _, Phi_bg_grid, _, _ = bg_fields(bg, r)
    if bg[0] == 'schw':
        M = bg[1]
        Phi_bg_prime = np.where(
            r > 2.0 * M,
            M / (rr ** 2 * np.maximum(1.0 - 2.0 * M / rr, 1e-300)), 0.0)
    elif bg[0] == 'ads':
        L = bg[1]
        Phi_bg_prime = (rr / (L * L)) / (1.0 + (rr / L) ** 2)
    else:
        Phi_bg_prime = np.zeros_like(r)
    ash_prime = np.where(r >= S_LO, Phi_prime - Phi_bg_prime, 0.0)
    a_sh = np.zeros_like(r)
    a_sh[-1] = 0.5 * np.log(max(1.0 - 2.0 * m_tot[-1] / r[-1], 1e-300)) \
        - float(bg_Phi(bg, np.array([r[-1]]))[0])
    for i in range(NR - 2, -1, -1):
        a_sh[i] = a_sh[i + 1] - 0.5 * (ash_prime[i] + ash_prime[i + 1]) \
            * (r[i + 1] - r[i])
    Phi = Phi_bg_grid + a_sh

    prof = {'bg': bg, 'r': r, 'm_tot': m_tot, 'm_sh': m_sh, 'Phi': Phi,
            'a_sh': a_sh, 'p_r': p_r, 'rho_tot': rho_tot,
            'pt_tot': (p_bg + (s_sol * pts_ if shell_on else 0.0)),
            's': s_sol, 'shoot_F': Fval, 'shoot': shot,
            'umin_band': umin_band, 'shell_on': shell_on,
            'M_sh': float(m_sh[-1])}

    # --- realisation residual + exact static 1D margins ----------------
    mp = np.gradient(m_tot, r, edge_order=2)
    Pp = np.gradient(Phi_prime, r, edge_order=2)
    rho_ex = np.where(r > 0, mp / (4.0 * np.pi * rr ** 2), rho_tot[0])
    pr_ex = np.where(r > 0, (Phi_prime * rr * (rr - 2.0 * m_tot) - m_tot)
                     / (4.0 * np.pi * rr ** 3), 0.0)
    bp = np.where(r > 0, (mp / rr - m_tot / rr ** 2)
                  / np.maximum(u, 1e-300), 0.0)
    pt_ex = np.where(r > 0, u * (Pp + Phi_prime ** 2 - Phi_prime * bp
                                 + (Phi_prime - bp) / rr) / EIGHT_PI, 0.0)
    _es.__exit__(None, None, None)
    rmin_safe = (2.0 * bg[1] + 0.5) if bg[0] == 'schw' else 0.0
    band = (r >= S_LO - 1) & (r <= S_HI + 1) & (r > rmin_safe)
    sc = max(float(np.max(np.abs(rho_tot[band]))), 1e-12)
    prof['realisation'] = {
        'rho_res': float(np.max(np.abs(rho_ex - rho_tot)[band]) / sc),
        'pr_res': float(np.max(np.abs(pr_ex - p_r)[band]) / sc),
        'pt_res': float(np.max(np.abs(pt_ex - prof['pt_tot'])[band]) / sc)}

    def _margins_1d(mask, drho=0.0, dp=0.0, sig=False):
        """Exact static margins; with (drho, dp) subtracted, the
        DIFFERENCE tensor's margins (shell's own contribution).
        sig=True restricts to radii whose local field scale exceeds
        1e-3 of the band peak (x2 significance convention, 1D form)
        — at the window edges the fields vanish identically and the
        gradient formulas return ~1e-9 noise, not physics."""
        rho1 = rho_ex - drho
        pr1 = pr_ex - dp
        pt1 = pt_ex - dp
        if sig:
            scale = np.maximum(np.abs(rho1),
                               np.maximum(np.abs(pr1), np.abs(pt1)))
            peak = float(np.max(scale[mask])) if mask.sum() else 0.0
            sigmask = mask & (scale > 1e-3 * max(peak, 1e-300))
            if sigmask.sum():
                mask = sigmask
        That1 = np.zeros((int(mask.sum()), 4, 4), dtype=DTYPE)
        That1[:, 0, 0] = rho1[mask]
        That1[:, 1, 1] = pr1[mask]
        That1[:, 2, 2] = pt1[mask]
        That1[:, 3, 3] = pt1[mask]
        m1 = vm.hawking_ellis_margins(That1)
        rb = r[mask]
        d = {k: float(np.min(m1[k])) for k in ('nec', 'wec', 'sec', 'dec')}
        d['nec_r'] = float(rb[int(np.argmin(m1['nec']))])
        d['dec_r'] = float(rb[int(np.argmin(m1['dec']))])
        d['typeI_frac'] = float(np.mean(m1['typeI']))
        return d

    core_m = (r >= R1) & (r <= R2) & (r > rmin_safe)
    band_m = (r >= S_LO) & (r <= S_HI) & (r > rmin_safe)
    prof['static1d_core'] = _margins_1d(core_m)
    prof['static1d_band'] = _margins_1d(band_m)
    prof['static1d_band_sig'] = _margins_1d(band_m, sig=True)
    rho_bg_c = float(rho_bg[0]); p_bg_c = float(p_bg[0])
    prof['static1d_diff_core'] = _margins_1d(core_m, rho_bg_c, p_bg_c)
    prof['static1d_diff_band_sig'] = _margins_1d(band_m, rho_bg_c,
                                                 p_bg_c, sig=True)
    return prof


# ---------------------------------------------------------------------------
# Cartesian metric for the judge
# ---------------------------------------------------------------------------
def make_gfunc(prof, beta):
    bg = prof['bg']
    r = prof['r']
    ash_s = CubicSpline(r, prof['a_sh'])
    msh_s = CubicSpline(r, prof['m_sh'])
    rmax = float(r[-1])

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = len(pts)
        rad = np.linalg.norm(pts, axis=1)
        rs = np.where(rad > 0, rad, 1.0)
        n = pts / rs[:, None]
        rc = np.clip(rad, 0.0, rmax)
        Phi = bg_Phi(bg, rs) + ash_s(rc)
        m = bg_m(bg, rs) + msh_s(rc)
        u = 1.0 - 2.0 * m / rs
        S = sh.shift_S(rad, R1, R2, 'cos', 1.0, [R1, R2]) if beta != 0.0 \
            else np.zeros(P)
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2.0 * Phi)
        g[:, 0, 1] = g[:, 1, 0] = -S * beta
        eb = 1.0 / u - 1.0
        g[:, 1:, 1:] = np.eye(3)[None] \
            + eb[:, None, None] * n[:, :, None] * n[:, None, :]
        return g

    return gfunc


# ---------------------------------------------------------------------------
# Audit (x2_bg pattern; margins_of copied verbatim from x2_bg.py)
# ---------------------------------------------------------------------------
def fib_dirs(n):
    i = np.arange(n)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5.0 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


def sample_points(rmin, ndir=26, nrad=55):
    dirs = fib_dirs(ndir)
    rad = np.linspace(rmin, 30.0, nrad)
    return np.concatenate([dirs * rr for rr in rad]).astype(DTYPE)


def margins_of(That):
    """Verbatim from x2_bg.py (threshold convention stated there)."""
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


REGIONS = {'cavity': lambda rad: rad < S_LO,
           'taper': lambda rad: ((rad >= S_LO) & (rad < R1))
           | ((rad > R2) & (rad <= S_HI)),
           'core': lambda rad: (rad >= R1) & (rad <= R2),
           'shellband': lambda rad: (rad >= S_LO) & (rad <= S_HI),
           'exterior': lambda rad: rad > S_HI}


def _region_dict(m, wall, rad, sel):
    if sel.sum() == 0:
        return None
    idx = np.where(sel)[0]
    j = idx[int(np.argmin(wall[sel]))]
    d = {k: float(np.min(m[k][sel])) for k in ('nec', 'wec', 'sec', 'dec')}
    d['worst'] = float(wall[j])
    d['worst_kind'] = ['nec', 'wec', 'sec', 'dec'][
        int(np.argmin([m['nec'][j], m['wec'][j], m['sec'][j], m['dec'][j]]))]
    d['worst_r'] = float(rad[j])
    d['nec_r'] = float(rad[idx[int(np.argmin(m['nec'][sel]))]])
    d['typeI_frac'] = float(np.mean(m['typeI'][sel]))
    d['n'] = int(sel.sum())
    return d


def region_margins(That, pts):
    """Per-region margins, two statistics: 'sig' = minima over
    globally-significant points (x2_bg threshold convention);
    'raw' = minima over ALL points in the region (strict).  Plus
    the global x2-style summary."""
    m = vm.hawking_ellis_margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9, 1e-3 * abs(rho_peak))
    sig = scale > thr
    rad = np.linalg.norm(pts, axis=1)
    wall = np.minimum(np.minimum(m['nec'], m['wec']),
                      np.minimum(m['sec'], m['dec']))
    out = {'global': margins_of(That), 'regions': {}}
    for name, fn in REGIONS.items():
        out['regions'][name] = {
            'sig': _region_dict(m, wall, rad, sig & fn(rad)),
            'raw': _region_dict(m, wall, rad, fn(rad))}
    return out


def audit(prof, prof_bgonly, beta, pts, h=0.3):
    gf_t = make_gfunc(prof, beta)
    G_t, That_t, _ = vm.einstein_at_points(gf_t, pts, h=h)
    gf_b = make_gfunc(prof_bgonly, 0.0)
    G_b, That_b, _ = vm.einstein_at_points(gf_b, pts, h=h)
    T_diff = (G_t - G_b) / EIGHT_PI
    g_t = gf_t(pts)
    That_d = vm.eulerian_that(g_t, T_diff)
    return {'total': region_margins(That_t, pts),
            'bg_only': region_margins(That_b, pts),
            'diff': region_margins(That_d, pts),
            'bg_max_abs_T': float(np.max(np.abs(That_b)))}


def bg_label(bg):
    if bg[0] == 'flat':
        return 'flat'
    if bg[0] == 'schw':
        return f'schw M={bg[1]:g}'
    return f'ads L={bg[1]:g}'


def rmin_for(bg):
    if bg[0] == 'schw':
        return 2.0 * bg[1] + 1.5
    return 3.0


def _fmt(v):
    return '  None ' if v is None else f'{v:+.3e}'


def _raw(entry, region):
    d = entry['regions'][region]['raw']
    return None if d is None else d['worst']


def _floor_ok(vals):
    """vals: judge-tensor raw worst per region at h = 0.3, 0.2, 0.1.
    OK if positive at the finest h, or a deficit that is demonstrably
    FD floor: shrinks >= 3x from h=0.2 to h=0.1 and |worst(0.1)| is
    at the demonstrated taper/horizon FD-artefact level (<= 5e-7)."""
    if any(v is None for v in vals):
        return True
    if vals[-1] > 0:
        return True
    return (abs(vals[-1]) < 0.34 * abs(vals[-2])
            and abs(vals[-1]) <= 5e-7)


# ---------------------------------------------------------------------------
# Main run
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()
    out = {'task': 'H4 background-re-solved shell (Phase 5)',
           'threshold_convention': 'x2_bg.margins_of: significant iff '
           'max|That| > max(1e-9, 1e-3*|rho_peak|); per-region margins '
           'reported both over significant points (sig) and over all '
           'points (raw, strict); regions: cavity r<9, taper '
           '9<=r<10 and 20<r<=21, core 10<=r<=20, shellband 9<=r<=21, '
           'exterior r>21',
           'coordinate_limit': 'static areal coordinates singular at '
           'r=2M_bg; audit radii >= 2M_bg+1.5, stencil reach 4h<=1.2',
           'support': 'prescription windowed (C^infty bump) to [9,21], '
           '=1 on [10,20]; BCs p_r=p_bg at both window edges '
           '(p_bg=0 for Schwarzschild)',
           'verdict_rule': 'schw: TOTAL tensor judges (background is '
           'vacuum); ads: DIFFERENCE tensor judges the shell (the '
           'background own WEC failure, rho_bg<0, is background). '
           'PASS requires: core [10,20] raw judge margins > 0 at '
           'h=0.3,0.2,0.1 with Type I fraction > 0.99; cavity/taper/'
           'exterior positive or FD-floor (deficit shrinks >=3x from '
           'h=0.2 to 0.1 and |worst(0.1)| <= 5e-7); for beta=0 the '
           'exact 1D spherical margins must confirm (core > 0, band '
           '> -1e-9). A constant-in-h deficit is physics.',
           'configs': {}, 'controls': {}}

    profs = {}
    profs_bg = {}

    def get_prof(bg):
        key = bg_label(bg)
        if key not in profs:
            profs[key] = solve_in_background(bg, shell_on=True)
            profs_bg[key] = solve_in_background(bg, shell_on=False)
            p = profs[key]
            print(f"[{key}] s={p['s']:.4f} shoot={p['shoot']} "
                  f"F={p['shoot_F']:.2e} umin_band={p['umin_band']:.3f} "
                  f"realisation={ {k: f'{v:.1e}' for k, v in p['realisation'].items()} } "
                  f"static1d core NEC={p['static1d_core']['nec']:+.3e} "
                  f"DEC={p['static1d_core']['dec']:+.3e} "
                  f"(dec @r={p['static1d_core']['dec_r']:.1f}) "
                  f"band NEC={p['static1d_band']['nec']:+.3e}")
        return profs[key], profs_bg[key]

    HS = (0.3, 0.2, 0.1)

    # ---------------- controls ----------------
    pf, pfb = get_prof(('flat',))
    pts_f = sample_points(3.0)
    for beta in (0.0, 0.02):
        entry = {}
        for h in HS:
            a = audit(pf, pfb, beta, pts_f, h=h)
            entry[f'h={h}'] = a
            t = a['total']
            print(f"CONTROL flat beta={beta} h={h}: "
                  f"core={_fmt(_raw(t, 'core'))} "
                  f"taper={_fmt(_raw(t, 'taper'))} "
                  f"cavity={_fmt(_raw(t, 'cavity'))} "
                  f"ext={_fmt(_raw(t, 'exterior'))} "
                  f"globalNEC={t['global'].get('nec'):+.3e}")
        out['controls'][f'flat beta={beta}'] = entry
    out['controls']['flat_solve'] = {
        's': pf['s'], 'shoot': pf['shoot'], 'shoot_F': pf['shoot_F'],
        'realisation': pf['realisation'],
        'static1d_core': pf['static1d_core'],
        'static1d_band': pf['static1d_band'],
        'static1d_band_sig': pf['static1d_band_sig']}

    for bg in [('schw', 1.0), ('schw', 2.0), ('schw', 4.0), ('ads', 30.0)]:
        p, pb = get_prof(bg)
        pts = sample_points(rmin_for(bg))
        a = audit(pb, pb, 0.0, pts, h=0.3)
        ah = audit(pb, pb, 0.0, pts, h=0.1)
        out['controls'][f'bg-only {bg_label(bg)}'] = {'h=0.3': a, 'h=0.1': ah}
        print(f"CONTROL bg-only {bg_label(bg)}: max|T| h=0.3 "
              f"{a['bg_max_abs_T']:.3e} -> h=0.1 {ah['bg_max_abs_T']:.3e}; "
              f"bg rho_peak={a['bg_only']['global'].get('rho_peak'):+.3e} "
              f"NEC={a['bg_only']['global'].get('nec'):+.3e}")

    # ---------------- main configurations ----------------
    candidates = []
    for bg in [('schw', 1.0), ('schw', 2.0), ('schw', 4.0), ('ads', 30.0)]:
        p, pb = get_prof(bg)
        pts = sample_points(rmin_for(bg))
        for beta in (0.0, 0.02):
            entry = {'solve': {'s': p['s'], 'shoot': p['shoot'],
                               'shoot_F': p['shoot_F'],
                               'umin_band': p['umin_band'],
                               'realisation': p['realisation'],
                               'static1d_core': p['static1d_core'],
                               'static1d_band': p['static1d_band'],
                               'static1d_band_sig': p['static1d_band_sig'],
                               'static1d_diff_core': p['static1d_diff_core'],
                               'static1d_diff_band_sig':
                                   p['static1d_diff_band_sig']}}
            judge_key = 'diff' if bg[0] == 'ads' else 'total'
            entry['judge_tensor'] = judge_key
            for h in HS:
                a = audit(p, pb, beta, pts, h=h)
                entry[f'h={h}'] = a
                jm = a[judge_key]
                print(f"{bg_label(bg)} beta={beta} h={h} [{judge_key}]: "
                      f"core={_fmt(_raw(jm, 'core'))} "
                      f"taper={_fmt(_raw(jm, 'taper'))} "
                      f"cavity={_fmt(_raw(jm, 'cavity'))} "
                      f"ext={_fmt(_raw(jm, 'exterior'))}")
            # ---- pass assessment -------------------------------------
            # CORE [10,20] (window = 1, the shell proper): raw judge
            # margins > 0 at ALL h, Type I ~ 1.  Cavity / taper /
            # exterior: positive, or a deficit passing the FD-floor
            # test (shrinks >= 3x from h=0.2 to 0.1, |worst(0.1)| <=
            # 5e-7).  A constant-in-h deficit is physics -> fail.
            core_ok = all(
                entry[f'h={h}'][judge_key]['regions']['core']['raw']
                is not None
                and entry[f'h={h}'][judge_key]['regions']['core']['raw']['worst'] > 0
                and entry[f'h={h}'][judge_key]['regions']['core']['raw']['typeI_frac'] > 0.99
                for h in HS)
            floor = {}
            for region in ('cavity', 'taper', 'exterior'):
                vals = [_raw(entry[f'h={h}'][judge_key], region)
                        for h in HS]
                floor[region] = _floor_ok(vals)
            static_ok = True
            if beta == 0.0:
                # FD-free ground truth, on the JUDGE tensor's static
                # analogue (total for schw, difference for ads):
                # core strictly positive; band over significant radii
                # strictly positive.
                if judge_key == 'diff':
                    sc_ = p['static1d_diff_core']
                    sb_ = p['static1d_diff_band_sig']
                else:
                    sc_ = p['static1d_core']
                    sb_ = p['static1d_band_sig']
                static_ok = (
                    all(sc_[k] > 0 for k in ('nec', 'wec', 'sec', 'dec'))
                    and all(sb_[k] > 0
                            for k in ('nec', 'wec', 'sec', 'dec')))
            entry['assess'] = {'core_ok': bool(core_ok),
                               'floor_ok': floor,
                               'static1d_ok': bool(static_ok)}
            passed = core_ok and all(floor.values()) and static_ok
            entry['pass'] = bool(passed)
            if passed:
                candidates.append((bg, beta))
            out['configs'][f'{bg_label(bg)} beta={beta}'] = entry

    # ---------------- red-team candidates ----------------
    out['redteam'] = {}
    for (bg, beta) in candidates:
        p, pb = get_prof(bg)
        judge_key = 'diff' if bg[0] == 'ads' else 'total'
        dirs = fib_dirs(98)
        rad = np.concatenate([np.linspace(rmin_for(bg), 9.0, 12),
                              np.linspace(9.0, 21.0, 97),
                              np.linspace(21.0, 30.0, 19)])
        pts_h = np.concatenate([dirs * rr for rr in rad]).astype(DTYPE)
        rt = {}
        for h in (0.2, 0.1, 0.05):
            a = audit(p, pb, beta, pts_h, h=h)
            rt[f'h={h}'] = a
            jm = a[judge_key]
            print(f"REDTEAM {bg_label(bg)} beta={beta} h={h} [{judge_key}]: "
                  f"core={_fmt(_raw(jm, 'core'))} "
                  f"taper={_fmt(_raw(jm, 'taper'))} "
                  f"cavity={_fmt(_raw(jm, 'cavity'))} "
                  f"ext={_fmt(_raw(jm, 'exterior'))}")
        rt_core = [_raw(rt[f'h={h}'][judge_key], 'core')
                   for h in (0.2, 0.1, 0.05)]
        rt['core_survives'] = bool(all(v is not None and v > 0
                                       for v in rt_core))
        out['redteam'][f'{bg_label(bg)} beta={beta}'] = rt

    out['candidates'] = [f'{bg_label(bg)} beta={beta}'
                         for bg, beta in candidates]
    out['runtime_s'] = time.time() - t0
    with open('results/h4_resolved_shell.json', 'w') as f:
        json.dump(out, f, indent=1, default=float)
    print('candidates:', out['candidates'])
    print(f"wrote results/h4_resolved_shell.json in {out['runtime_s']:.0f}s")


if __name__ == '__main__':
    main()
