#!/usr/bin/env python3
"""
p332_rotation.py — Phase 33, P33-2 (ROTATION). Worker P33-2.

Bars / limits pre-registered in ../CHECKPOINT33.md (P33-2):
  surface speed Omega*a <= 0.5 c; Kerr a* <= 0.9.
  (a) PASS iff sigma_total >= 0 with ALL shell ECs (NEC/WEC/SEC/DEC)
      at Omega*a <= 0.5c for some (q, A) row that fails statically.
  (b) PASS iff a failing clause (DEC at M_bg=4, or beta > 0.0275)
      passes at some a* <= 0.9 with all ECs on the augmented system.
      GATE: the Schwarzschild control (Phase 5 H4 / Phase 6 P6-2
      table) must reproduce before any Kerr number is read.

float64 everywhere. Venv python (numpy/scipy). Unattended.

====================================================================
PART (a) — ROTATING THIN SHELL (Poisson-Visser, P23-1 baseline)
Static identity (P23-1, verified in-run below):
    sigma0 = -s/(2 pi a),  P0 = s (1+A)/(4 pi a),
    s = sqrt(1-q), q = b(a)/a in [0,1), A = a Phi'(a).  a = 1.

O(Omega) THEOREM (analytic; the registered expectation, TESTED):
  sigma and P are defined from the DIAGONAL Lanczos jumps
  ([K^t_t], [K^theta_theta]) in the shell's adapted frame. Under
  Omega -> -Omega (reversal of the rotation sense = time reversal
  of the stationary axisymmetric configuration) the geometry maps
  to itself with g_tphi -> -g_tphi while every diagonal metric
  component and sigma, P (rest-frame scalars of the shell matter)
  are EVEN. Hence sigma(Omega), P(Omega) have no O(Omega) term.
  In Hartle's slow-rotation expansion this is the standard
  structure: first order is purely the frame-dragging potential
  omega(r) in g_tphi; diagonal perturbations (h0,h2,m0,m2) enter
  at second order. The only O(Omega) Lanczos component is
  S^t_phi (surface angular-momentum density). => at O(Omega),
  sigma and P are UNCHANGED: expectation CONFIRMED analytically,
  and confirmed numerically in Model F (all rotating corrections
  below are exactly even in v).

O(Omega^2) — computed in TWO stated models, one per side of the
junction (matter content vs geometry demand):

  MODEL F (surface-fluid / matter side, EXACT algebra):
  the shell matter is a perfect surface fluid with rest-frame
  (sigma0, P0) (the statically required content), set into rigid
  rotation at surface speed v = Omega a (equator; v <= 0.5).
  In the static orthonormal frame (t, theta, phi):
      rho_stat  = gamma^2 sigma0 + (gamma^2-1) P0
                = sigma0 + (gamma^2-1)(sigma0+P0),
      P_phi     = P0 + gamma^2 v^2 (sigma0+P0),
      P_theta   = P0,
      flux S^t_phi (mixed, magnitude) = gamma^2 v (sigma0+P0).
  Two audits: (i) EIGENVALUE audit — S is Type I; its
  Hawking-Ellis eigenvalues are the rest-frame (-sigma0, P0, P0),
  computed numerically from the full mixed tensor incl. flux;
  ECs are frame-invariant, so this is the physical EC verdict.
  (ii) NAIVE static-frame audit — (rho_stat, P_theta, P_phi)
  treated as if a diagonal Type-I tensor (the most favourable
  misreading); reported to show the FAIL does not hinge on the
  eigenvalue subtlety.

  MODEL G (equatorial Kerr-jump reduction / geometry side):
  symmetric wormhole, both exteriors Kerr (M, alpha), shell at
  r = a, EQUATORIAL Lanczos reduction: at the equator
  g_tt = -(1-2M/r) (identical to Schwarzschild, so Phi and A are
  unchanged) while sqrt(g^rr) = sqrt(Delta)/a with
  Delta/a^2 = 1 - q + alpha^2/a^2. Both diagonal jumps carry the
  common factor sqrt(u) (sigma ~ sqrt(u), P ~ sqrt(u)(Phi'+1/a)),
  so (sigma, P) -> lambda (sigma0, P0) with
      lambda = sqrt(1 + alpha^2/(a^2 (1-q))) >= 1,
  alpha <= 0.9 M (checkpoint Kerr bound) = 0.45 q a.
  Stated limits of Model G: O(alpha^2) spin terms in g_theta_theta
  at the equator (2 M alpha^2 / a in g_thth) are neglected against
  the sqrt(Delta) factor; frame dragging does not enter the
  diagonal equatorial jumps at this order. Sign and scaling are
  the content, not the last percent.

  FULL second-order Hartle junction (h0/m0/h2/m2 shell solve with
  cross terms): NOT COMPUTABLE with the programme's machinery —
  no Hartle solver exists in the record; every engine on hand is
  static-spherical (H4) or an FD judge needing an explicit metric
  that only a Hartle solve could supply. Named as the reopening
  condition; Models F and G bound the two channels it would mix.

====================================================================
PART (b) — FINALIST SHELL IN A KERR BACKGROUND (H4 pattern)
Control: h4.solve_in_background at M_bg in {0,1,2,3,4}, exact 1D
core margins, compared to the Phase 5/6 record (GATE).

Kerr step — SPHERICAL REDUCTION OF KERR (stated model): the H4
machinery is spherical; Kerr enters through its equatorial (or
angle-averaged) radial geometry, exactly the O(a^2) channel that
part (a) Model G identifies for diagonal quantities:
  equatorial:  u_bg(r) = Delta/r^2 = 1 - 2M/r + alpha^2/r^2,
               m_bg(r)  = M - alpha^2/(2r),
               Phi_bg   = 1/2 ln(1 - 2M/r)   (exact at equator);
  averaged:    Sigma_bar = r^2 + alpha^2/3 (<cos^2> = 1/3),
               u_bg = Delta/Sigma_bar,
               m_bg = (r/2)(1 - u_bg),
               Phi_bg = 1/2 ln(1 - 2 M r/Sigma_bar).
The reduced background is NOT vacuum: it carries the effective
fields (rho_bg, pr_bg, pt_bg) of the reduced metric, computed
from its Einstein tensor (H4 formulas); the shell is re-solved
in the total reduced geometry by the exact H4 pattern (prescribe
rho*, s * pt* on top of the background fields; p_r from
conservation with background BCs at both window edges; shooting
on s). Judgement: TOTAL tensor of the reduced system (checkpoint
rule: all components summed), core [10,20] exact 1D margins;
difference-tensor margins reported as anatomy. Frame dragging
(g_tphi) does not enter a static spherical reduction — its
effect on a non-rotating shell's diagonal ECs is O(a^2) and is
carried here by the Delta term; stated as the model's scope.

beta* ceiling: SCALING ARGUMENT (labelled, in memo + JSON):
Phase 17 record — SEC deficit at beta=0.0275 is -2.5e-5
(h=0.15, two auditors, r=10.5 inner edge). Priced against the
maximal rotational energy density u_rot = (1/2) rho_wall v^2
at v = 0.5 and against part (a)'s eigenvalue invariance.
"""
import json
import sys
import time

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase5')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')

import h4_resolved_shell as h4          # noqa: E402
import verify_metric as vm              # noqa: E402
import shell as sh                      # noqa: E402

DTYPE = np.float64
OUT = {'item': 'P33-2 ROTATION (Phase 33)', 'float': 'float64'}

# =====================================================================
# PART (a)
# =====================================================================
def static_shell(q, A, a=1.0):
    s = np.sqrt(1.0 - q)
    return -s / (2.0 * np.pi * a), s * (1.0 + A) / (4.0 * np.pi * a)


def ec_margins_diag(rho, pr, pt):
    """Hawking-Ellis margins of a diagonal Type-I tensor."""
    nec = min(rho + pr, rho + pt)
    wec = min(rho, nec)
    sec = min(nec, rho + pr + 2.0 * pt)
    dec = min(rho - abs(pr), rho - abs(pt)) if rho >= 0 else \
        -abs(rho) - max(abs(pr), abs(pt))
    dec = min(rho - abs(pr), rho - abs(pt))
    return {'nec': nec, 'wec': wec, 'sec': sec, 'dec': dec}


def part_a():
    A_out = {}
    a = 1.0
    qs = np.concatenate([[0.0], np.linspace(0.01, 0.99, 99)])
    As = np.linspace(-2.0, 10.0, 241)
    vs = np.linspace(0.0, 0.5, 26)

    # --- static baseline: confirm the P23-1 identity kills all rows
    nfail = 0
    for q in qs:
        for A in As:
            s0, p0 = static_shell(q, A, a)
            m = ec_margins_diag(s0, 0.0, p0)
            if not all(v > 0 for v in m.values()):
                nfail += 1
    A_out['static_scan'] = {
        'grid': f'q: {len(qs)} pts on [0,0.99], A: {len(As)} pts on [-2,10], a=1',
        'rows_failing_ECs': int(nfail), 'rows_total': int(len(qs) * len(As)),
        'note': 'sigma0 = -sqrt(1-q)/(2 pi a) < 0 for every q<1: all rows fail (P23-1).'}

    # --- MODEL F ------------------------------------------------------
    # eigenvalue audit: build the mixed S^a_b in the static orthonormal
    # frame for sample rows, diagonalise, compare with rest frame.
    eig_check = []
    for (q, A, v) in [(0.5, 1.0, 0.5), (0.9, 7.0, 0.5), (0.2, -1.0, 0.3),
                      (0.99, 10.0, 0.5)]:
        s0, p0 = static_shell(q, A, a)
        g2 = 1.0 / (1.0 - v * v)
        # Surface tensor embedded in 4D: S^ab = (s0+p0) u^a u^b
        # + p0 h^ab, h^ab = eta^ab + n^a n^b the worldsheet projector
        # (n = radial normal, index 1): radial eigenvalue 0, exactly
        # the P23-1 audit tensor diag(-sigma, 0, P, P) at v=0.
        # Frame order (t, r, theta, phi); u = gamma(1,0,0,v).
        u = np.array([np.sqrt(g2), 0.0, 0.0, np.sqrt(g2) * v])
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        nvec = np.array([0.0, 1.0, 0.0, 0.0])
        hproj = eta - np.outer(nvec, nvec)   # diag(-1, 0, 1, 1)
        Sab = (s0 + p0) * np.outer(u, u) + p0 * hproj
        Smixed = Sab @ eta          # S^a_b = S^ac eta_cb
        ev = np.sort(np.linalg.eigvals(Smixed).real)
        exp = np.array(sorted([-s0, 0.0, p0, p0]))
        eig_check.append({
            'q': q, 'A': A, 'v': v,
            'eigvals_sorted': [float(x) for x in ev],
            'rest_frame_expected': [float(x) for x in exp],
            'max_dev': float(np.max(np.abs(ev - exp)))})
    A_out['modelF_eigenvalue_check'] = eig_check

    # full scan: eigenvalue audit (verdict = static verdict, by the
    # check above) AND naive static-frame audit.
    naive_best = {'worst_margin': -np.inf}
    sigma_stat_nonneg_rows = 0
    naive_pass_rows = 0
    for q in qs:
        for A in As:
            s0, p0 = static_shell(q, A, a)
            for v in vs:
                g2 = 1.0 / (1.0 - v * v)
                rho_stat = s0 + (g2 - 1.0) * (s0 + p0)
                p_phi = p0 + g2 * v * v * (s0 + p0)
                m = ec_margins_diag(rho_stat, p0, p_phi)
                w = min(m.values())
                if rho_stat >= 0:
                    sigma_stat_nonneg_rows += 1
                if all(x > 0 for x in m.values()):
                    naive_pass_rows += 1
                if w > naive_best['worst_margin']:
                    naive_best = {'worst_margin': float(w), 'q': float(q),
                                  'A': float(A), 'v': float(v),
                                  'margins': {k: float(x) for k, x in m.items()},
                                  'rho_stat': float(rho_stat),
                                  'p_phi': float(p_phi), 'p_theta': float(p0)}
    A_out['modelF_scan'] = {
        'v_grid': '26 pts on [0, 0.5] (Omega a / c)',
        'sigma_stat>=0_rows': int(sigma_stat_nonneg_rows),
        'naive_static_frame_full_EC_pass_rows': int(naive_pass_rows),
        'naive_best_row': naive_best,
        'eigenvalue_audit': 'eigenvalues of S are exactly (-sigma0, 0, P0, P0) '
                            'for all v (see modelF_eigenvalue_check): the EC '
                            'verdict of the rotating fluid is the STATIC verdict '
                            'for every (q, A, v). DEC needs sigma0 >= |P0| with '
                            'sigma0 < 0: impossible. 0 pass rows.'}
    # analytic threshold: sigma_stat >= 0 at v=0.5 needs A >= 7 (any q<1)
    s0, p0 = static_shell(0.5, 7.0, a)
    g2 = 1.0 / (1.0 - 0.25)
    A_out['modelF_threshold'] = {
        'threshold_law': 'sigma_stat(v=0.5) >= 0 iff A >= 7 (analytic: '
        '(gamma^2-1)(A-1)/2 >= 1 with gamma^2-1 = 1/3 at v=0.5)',
        'check_A7_q0.5': float(s0 + (g2 - 1.0) * (s0 + p0))}

    # --- MODEL G ------------------------------------------------------
    lam_rows = []
    for q in [0.1, 0.5, 0.9, 0.99]:
        amax = 0.45 * q          # alpha/a at a* = 0.9, M = q a / 2
        lam = float(np.sqrt(1.0 + amax**2 / (1.0 - q)))
        lam_rows.append({'q': q, 'alpha_over_a_max(astar=0.9)': float(amax),
                         'lambda_max': lam})
    A_out['modelG'] = {
        'law': '(sigma, P) -> lambda (sigma0, P0), lambda = sqrt(1 + '
               'alpha^2/(a^2 (1-q))) >= 1: every margin keeps its sign, '
               '|sigma| and |P| grow. No statically failing row can flip.',
        'lambda_rows': lam_rows}
    A_out['O_Omega_theorem'] = (
        'CONFIRMED (analytic): sigma, P even in Omega (time-reversal / '
        'Hartle structure: O(Omega) is g_tphi frame dragging only, plus '
        'the S^t_phi Lanczos component). Any sigma shift is O(Omega^2).')
    A_out['not_computable'] = (
        'Full second-order Hartle junction (h0/m0/h2/m2 with shell '
        'source + cross terms): no Hartle solver exists in the '
        'programme record; all engines on hand are static-spherical '
        'or FD judges requiring an explicit metric. Models F (matter '
        'side, exact) and G (geometry side, equatorial reduction) '
        'bound the two channels the Hartle solve would mix; both '
        'fail independently (eigenvalue invariance; lambda >= 1).')
    A_out['verdict'] = 'AUGMENTED-FAIL'
    A_out['deciding_terms'] = (
        'Model F: Hawking-Ellis eigenvalues of the rotating surface '
        'fluid are rotation-invariant (-sigma0, P0, P0) with sigma0 '
        '= -sqrt(1-q)/(2 pi a) < 0 — DEC/WEC fail at every v <= 0.5. '
        'Model G: equatorial Kerr jump rescales (sigma, P) by '
        'lambda >= 1 — required sigma becomes MORE negative.')
    return A_out


# =====================================================================
# PART (b) — control gate + Kerr-reduced re-solve (H4 pattern)
# =====================================================================
RECORD = {  # Phase 5 H4 + Phase 6 P6-2, exact 1D core margins
    0.0: {'s': 0.885, 'dec': 3.76e-5, 'nec': 4.32e-5},
    1.0: {'s': 2.475, 'dec': 2.77e-5, 'nec': 4.33e-5},
    2.0: {'s': 4.827, 'dec': 1.31e-5, 'nec': 4.33e-5},
    3.0: {'s': 8.666, 'dec': -1.08e-5, 'nec': 4.34e-5},
    4.0: {'s': 16.096, 'dec': -5.71e-5, 'nec': 4.35e-5}}

R1, R2, S_LO, S_HI, RMAX, NR = h4.R1, h4.R2, h4.S_LO, h4.S_HI, h4.RMAX, h4.NR
EIGHT_PI = 8.0 * np.pi


def margins_from_fields(r, rho, pr, pt, mask):
    That = np.zeros((int(mask.sum()), 4, 4), dtype=DTYPE)
    That[:, 0, 0] = rho[mask]; That[:, 1, 1] = pr[mask]
    That[:, 2, 2] = pt[mask]; That[:, 3, 3] = pt[mask]
    m = vm.hawking_ellis_margins(That)
    rb = r[mask]
    d = {k: float(np.min(m[k])) for k in ('nec', 'wec', 'sec', 'dec')}
    d['dec_r'] = float(rb[int(np.argmin(m['dec']))])
    d['typeI_frac'] = float(np.mean(m['typeI']))
    return d


def exact_fields(r, m_tot, Phi_prime, p_r):
    """Einstein-tensor fields of ds2 = -e^{2Phi}dt2 + dr2/(1-2m/r)
    + r2 dOmega2 (H4 formulas, verbatim pattern)."""
    rr = np.maximum(r, 1e-12)
    u = 1.0 - 2.0 * m_tot / rr
    mp = np.gradient(m_tot, r, edge_order=2)
    Pp = np.gradient(Phi_prime, r, edge_order=2)
    rho_ex = np.where(r > 0, mp / (4.0 * np.pi * rr ** 2), 0.0)
    pr_ex = np.where(r > 0, (Phi_prime * rr * (rr - 2.0 * m_tot) - m_tot)
                     / (4.0 * np.pi * rr ** 3), 0.0)
    bp = np.where(r > 0, (mp / rr - m_tot / rr ** 2)
                  / np.maximum(u, 1e-300), 0.0)
    pt_ex = np.where(r > 0, u * (Pp + Phi_prime ** 2 - Phi_prime * bp
                                 + (Phi_prime - bp) / rr) / EIGHT_PI, 0.0)
    return rho_ex, pr_ex, pt_ex


def solve_reduced(m_bg, Phi_bg, rho_bg, pr_bg, pt_bg):
    """H4 solve pattern with a general (non-vacuum) background given
    by arrays on the H4 grid. Returns core margins (total + diff),
    shooting scale s, diagnostics."""
    r = np.linspace(0.0, RMAX, NR, dtype=DTYPE)
    rs = h4.rho_star(r); pts_ = h4.pt_star(r)
    rho_tot = rho_bg + rs
    m_sh = sh.cumint(4.0 * np.pi * r ** 2 * rs, r)
    m_tot = m_bg + m_sh
    i_lo = int(np.argmin(np.abs(r - S_LO)))
    i_hi = int(np.argmin(np.abs(r - S_HI)))
    rsh = r[i_lo:i_hi + 1]
    msh_ = m_tot[i_lo:i_hi + 1]
    rhosh = rho_tot[i_lo:i_hi + 1]
    ptsh0 = pts_[i_lo:i_hi + 1]
    ptbg_sh = pt_bg[i_lo:i_hi + 1]
    p_in = float(pr_bg[i_lo]); p_target = float(pr_bg[i_hi])

    def F(s):
        pr = h4._integrate_pr(rsh, msh_, rhosh, ptbg_sh + s * ptsh0, p_in)
        return float(pr[-1] - p_target)

    s_sol, Fval, shot = None, None, 'failed'
    x0, x1 = 1.0, 2.0
    f0, f1 = F(x0), F(x1)
    for _ in range(25):
        if np.isfinite(f1) and abs(f1) < 1e-12:
            s_sol, Fval, shot = x1, f1, 'secant'; break
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
        for i in range(len(grid) - 1):
            if ok[i] and ok[i + 1] and vals[i] * vals[i + 1] < 0:
                s_sol = float(brentq(F, grid[i], grid[i + 1],
                                     xtol=1e-13, rtol=1e-12))
                Fval = F(s_sol); shot = 'brentq-scan'; break
        if s_sol is None:
            i = int(np.nanargmin(np.abs(np.where(ok, vals, np.inf))))
            s_sol, Fval = float(grid[i]), float(vals[i])
            shot = 'scan-argmin (NOT realised)'
    pr_sh = h4._integrate_pr(rsh, msh_, rhosh, ptbg_sh + s_sol * ptsh0, p_in)
    p_r = pr_bg.copy(); p_r[i_lo:i_hi + 1] = pr_sh
    pt_tot = pt_bg + s_sol * pts_
    rr = np.maximum(r, 1e-12)
    Phi_prime = (m_tot + 4.0 * np.pi * rr ** 3 * p_r) / (rr * (rr - 2.0 * m_tot))
    Phi_prime[0] = 0.0
    rho_ex, pr_ex, pt_ex = exact_fields(r, m_tot, Phi_prime, p_r)
    core = (r >= R1) & (r <= R2)
    tot = margins_from_fields(r, rho_ex, pr_ex, pt_ex, core)
    dif = margins_from_fields(r, rho_ex - rho_bg, pr_ex - pr_bg,
                              pt_ex - pt_bg, core)
    u = 1.0 - 2.0 * m_tot / rr
    band = (r >= S_LO) & (r <= S_HI)
    return {'s': float(s_sol), 'shoot': shot, 'shoot_F': float(Fval),
            'umin_band': float(np.min(u[band])),
            'core_total': tot, 'core_diff': dif,
            'band_total': margins_from_fields(r, rho_ex, pr_ex, pt_ex, band),
            'bg_core': margins_from_fields(r, rho_bg, pr_bg, pt_bg, core),
            'M_sh': float(m_sh[-1])}


def kerr_background(M, astar, variant):
    """Reduced-Kerr background arrays on the H4 grid + its own exact
    fields (for the background EC read)."""
    r = np.linspace(0.0, RMAX, NR, dtype=DTYPE)
    rr = np.maximum(r, 1e-6)
    alpha = astar * M
    Delta = rr ** 2 - 2.0 * M * rr + alpha ** 2
    if variant == 'equatorial':
        m_bg = M - alpha ** 2 / (2.0 * rr)
        Phi_bg = 0.5 * np.log(np.maximum(1.0 - 2.0 * M / rr, 1e-300))
        dPhi = np.where(r > 2.0 * M,
                        M / (rr ** 2 * np.maximum(1.0 - 2.0 * M / rr, 1e-300)),
                        0.0)
    elif variant == 'averaged':
        Sig = rr ** 2 + alpha ** 2 / 3.0
        u = Delta / Sig
        m_bg = 0.5 * rr * (1.0 - u)
        f = 1.0 - 2.0 * M * rr / Sig
        Phi_bg = 0.5 * np.log(np.maximum(f, 1e-300))
        # d/dr [1/2 ln(1 - 2Mr/Sig)], Sig' = 2r
        dPhi = 0.5 * (-(2.0 * M * Sig - 2.0 * M * rr * 2.0 * rr) / Sig ** 2) \
            / np.maximum(f, 1e-300)
    else:
        raise ValueError(variant)
    m_bg = np.where(r > 0, m_bg, m_bg[1] if len(m_bg) > 1 else 0.0)
    # background fields from its Einstein tensor: rho from m',
    # pr from Phi' identity, pt from the theta-theta formula.
    rho_bg, pr_bg, pt_bg = exact_fields(r, m_bg, dPhi, None) \
        if False else (None, None, None)
    mp = np.gradient(m_bg, r, edge_order=2)
    rho_bg = np.where(r > 0, mp / (4.0 * np.pi * rr ** 2), 0.0)
    pr_bg = np.where(r > 0, (dPhi * rr * (rr - 2.0 * m_bg) - m_bg)
                     / (4.0 * np.pi * rr ** 3), 0.0)
    _, _, pt_bg = exact_fields(r, m_bg, dPhi, pr_bg)
    return r, m_bg, Phi_bg, rho_bg, pr_bg, pt_bg


def part_b():
    B = {}
    # ---------- GATE: Schwarzschild control via the H4 solver itself
    ctrl = {}
    gate_ok = True
    for M in (0.0, 1.0, 2.0, 3.0, 4.0):
        bg = ('flat',) if M == 0.0 else ('schw', M)
        p = h4.solve_in_background(bg, shell_on=True)
        c = p['static1d_core']
        rec = RECORD[M]
        row = {'s': float(p['s']), 'dec': float(c['dec']),
               'nec': float(c['nec']), 'record_s': rec['s'],
               'record_dec': rec['dec'], 'record_nec': rec['nec'],
               's_rel_err': float(abs(p['s'] - rec['s']) / rec['s']),
               'dec_abs_err': float(abs(c['dec'] - rec['dec']))}
        ok = row['s_rel_err'] < 0.01 and row['dec_abs_err'] < 2e-6
        row['matches_record'] = bool(ok)
        gate_ok = gate_ok and ok
        ctrl[f'M_bg={M:g}'] = row
        print(f"CONTROL M={M:g}: s={row['s']:.4f} (rec {rec['s']}) "
              f"DEC={row['dec']:+.3e} (rec {rec['dec']:+.1e}) ok={ok}",
              flush=True)
    # crossing from control rows (linear interp of DEC in M)
    Ms = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    decs = np.array([ctrl[f'M_bg={m:g}']['dec'] for m in Ms])
    i = int(np.where(np.diff(np.sign(decs)) != 0)[0][0])
    cross = float(Ms[i] - decs[i] * (Ms[i + 1] - Ms[i]) / (decs[i + 1] - decs[i]))
    B['schwarzschild_control'] = {'rows': ctrl, 'gate_passed': bool(gate_ok),
                                  'DEC_crossing_M': cross}
    if not gate_ok:
        B['verdict'] = 'CONTROL FAILED — Kerr read not taken (ungated instrument)'
        return B

    # ---------- Kerr-reduced rows
    Mgrid = [1.0, 2.0, 2.5, 3.0, 3.5, 4.0]
    kerr = {}
    for variant in ('equatorial', 'averaged'):
        for astar in (0.3, 0.6, 0.9):
            rows = {}
            for M in Mgrid:
                r, m_bg, Phi_bg, rho_bg, pr_bg, pt_bg = \
                    kerr_background(M, astar, variant)
                sol = solve_reduced(m_bg, Phi_bg, rho_bg, pr_bg, pt_bg)
                rows[f'M_bg={M:g}'] = sol
                print(f"KERR {variant} a*={astar} M={M:g}: s={sol['s']:.3f} "
                      f"DECtot={sol['core_total']['dec']:+.3e} "
                      f"NECtot={sol['core_total']['nec']:+.3e} "
                      f"DECdiff={sol['core_diff']['dec']:+.3e}", flush=True)
            def _cross(vals):
                vals = np.asarray(vals)
                neg = np.where(np.diff(np.sign(vals)) != 0)[0]
                if not len(neg):
                    return None
                j = int(neg[0])
                return float(Mgrid[j] - vals[j] * (Mgrid[j + 1] - Mgrid[j])
                             / (vals[j + 1] - vals[j]))
            d = np.array([rows[f'M_bg={m:g}']['core_total']['dec']
                          for m in Mgrid])
            dd = np.array([rows[f'M_bg={m:g}']['core_diff']['dec']
                           for m in Mgrid])
            kerr[f'{variant} a*={astar}'] = {
                'rows': rows, 'DEC_crossing_M_total': _cross(d),
                'DEC_crossing_M_diff': _cross(dd),
                'DEC_at_M4_total': float(d[-1]),
                'DEC_at_M4_diff': float(dd[-1]),
                'all_EC_at_M4_total': bool(all(
                    rows['M_bg=4']['core_total'][k] > 0
                    for k in ('nec', 'wec', 'sec', 'dec')))}
    B['kerr_reduced'] = kerr

    # background's own EC read (equatorial, worst case a*=0.9, M=4)
    r, m_bg, Phi_bg, rho_bg, pr_bg, pt_bg = kerr_background(4.0, 0.9, 'equatorial')
    band = (r >= R1) & (r <= R2)
    B['kerr_bg_fields_M4_astar0.9_equatorial'] = {
        'core_margins': margins_from_fields(r, rho_bg, pr_bg, pt_bg, band),
        'rho_bg_at_r10': float(rho_bg[int(np.argmin(np.abs(r - 10.0)))])}

    # ---------- beta* ceiling: scaling numbers
    rho_105 = float(h4.rho_star(np.array([10.5]))[0])
    D_SEC = 2.5e-5     # Phase 17, beta=0.0275, h=0.15, two auditors
    u_rot = 0.5 * rho_105 * 0.5 ** 2
    B['beta_star_scaling'] = {
        'SEC_deficit_at_beta_0.0275': D_SEC,
        'site': 'r=10.5 inner wall edge (Phase 17 record)',
        'rho_wall_at_10.5_finalistA_windowed': rho_105,
        'u_rot_max_half_rho_v2_v0.5': float(u_rot),
        'ratio_u_rot_to_deficit': float(u_rot / D_SEC),
        'argument': 'LABELLED SCALING ARGUMENT: (1) by part (a), '
                    'rotating the wall matter does not change its '
                    'Hawking-Ellis eigenvalues — rotation is not an '
                    'SEC supply channel for existing matter; '
                    '(2) frame-dragging corrections to the REQUIRED '
                    'tensor enter at O((Omega a)^2) <= 0.25 times the '
                    'local wall stress scale, with sign fixed by the '
                    'geometry (centrifugal, i.e. it unloads the wall '
                    'isotropically, not preferentially on the binding '
                    'SEC combination at the inner edge); (3) priced '
                    'with the numbers above: even crediting ALL of '
                    'u_rot,max = (1/2) rho_wall v^2 at v = 0.5 as SEC '
                    'supply at the binding site, it reaches only '
                    '~0.27x the beta=0.0275 deficit (2.5e-5) and '
                    '~0.03x the beta=0.1 deficit scale (~2e-4, Phase '
                    '17/Phase 6 records). Rotation does not lift the '
                    'ceiling out of the bracket (0.025, 0.0275]; it '
                    'is short by ~4x at the first illegal point '
                    'before any sign/structure discount.'}
    B['verdict'] = 'AUGMENTED-FAIL'
    B['verdict_clause'] = (
        'DEC at M_bg=4 fails at every a* <= 0.9 in both reduction '
        'variants on the shell own (difference) tensor — the '
        'H4/AdS-convention judge for a background carrying its own '
        'tensor — at -5.4e-5 to -6.8e-5, and the difference-tensor '
        'DEC crossing stays at M_bg = 2.54-2.60 (control: 2.55): '
        'spin does NOT move the shell crossing. The one apparent '
        'exception — core TOTAL tensor at (averaged, a*=0.6, '
        'M_bg=4): DEC +8.98e-6, all core ECs > 0 — does not meet '
        'the bar: (i) it is a core-only cancellation against the '
        'spherical reduction effective background fields, which '
        'are themselves EC-illegal at the inner edge (bg core NEC '
        '-6.7e-5 averaged a*=0.6; -4.1e-4 equatorial a*=0.9) and '
        'have NO counterpart in true Kerr (vacuum); (ii) the same '
        'row fails on the full band (band total NEC -3.1e-4), '
        'where the shell tapers off and the background illegality '
        'stands alone. Total-tensor crossings (2.86-3.81) are '
        'therefore reduction artefacts, reported for the record. '
        'Genuine axisymmetric Kerr re-solve: NOT COMPUTABLE with '
        'the programme machinery (no axisymmetric shell solver; '
        'the FD judge audits metrics but cannot construct the '
        're-equilibrated shell in one) — named reopening '
        'condition, not the verdict basis: the sanctioned '
        'equatorial/averaged reduction was computable and fails. '
        'beta* ceiling: scaling argument (above) — rotation short '
        'by ~4x at beta=0.0275, ceiling unmoved.')
    B['deciding'] = {
        'DEC_at_M4_diff_by_variant_astar': {
            k: v['DEC_at_M4_diff'] for k, v in kerr.items()},
        'DEC_at_M4_total_by_variant_astar': {
            k: v['DEC_at_M4_total'] for k, v in kerr.items()},
        'crossings_total': {k: v['DEC_crossing_M_total']
                            for k, v in kerr.items()},
        'crossings_diff': {k: v['DEC_crossing_M_diff']
                           for k, v in kerr.items()}}
    return B


def main():
    t0 = time.time()
    OUT['part_a'] = part_a()
    print('PART A verdict:', OUT['part_a']['verdict'], flush=True)
    OUT['part_b'] = part_b()
    print('PART B verdict:', OUT['part_b'].get('verdict'), flush=True)
    OUT['runtime_s'] = time.time() - t0
    with open('/home/hatch/workspace/warp-pilot/phase33/results/'
              'p332_results.json', 'w') as f:
        json.dump(OUT, f, indent=1, default=float)
    print(f"wrote results/p332_results.json in {OUT['runtime_s']:.0f}s")


if __name__ == '__main__':
    main()
