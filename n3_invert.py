"""
n3_invert.py — N3 CONDITIONS-FIRST inversion (spherical core).

Forward construction (build_shell) cages: density from a named weight
family; pressure from the ISOTROPIC TOV solve (p_t slaved, and P
zeroed by hand inside R1). Here the design variables are the
EIGENVALUE FIELDS themselves:

  prescribe  rho*(r) >= 0 and p_t*(r) freely (compact support);
  solve      p_r*(r) from the conservation (Bianchi) identity
               p_r' = -(rho+p_r) a' - (2/r)(p_r - p_t),
               a'   = (m/r^2 + 4 pi r p_r) / (1 - 2m/r),
             integrated OUTWARD from the centre (inward integration
             is unstable: the homogeneous mode grows like r^-2).
             Regularity: p_r(0) = p_t(0) =: p_c. The endpoint
             condition p_r(r_out) = 0 (vacuum outside the support)
             is ONE scalar equation for p_c — solved by shooting
             (brentq). If no p_c in bracket satisfies it, the
             prescription is NOT REALISABLE as a regular static
             spherical geometry: reported, not hidden.
  geometry   m(r) from rho*, b = -1/2 ln(1 - 2m/r), a from a' with
             a(rmax) = 1/2 ln(1 - 2M/rmax) (asymptotic flatness).

Gauge: the pilot ADM ansatz (stationary; shift along x added after,
S = cosine window on [R1, R2]). ADM mass = m(rmax). The realised
static tensor is printed against the prescription (realisation
residual = discretisation honesty), then the MOVING tensor is
judged by the standard point auditor — the prescription never
grades itself.

CONTROL: feeding the inverter a known-realised pair (rho_ex, p_t)
from build_shell must return its metric (a, b) and p_r.
float64 everywhere.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

import shell as sh

DTYPE = np.float64


def _integrate_pr(r, m, rho, pt, pc):
    """Outward RK2 (midpoint) integration of the conservation ODE
    with p_r(0) = pc. Plain-float loop (hot path for shooting)."""
    Nr = len(r)
    rl = r.tolist(); ml = m.tolist(); hl = rho.tolist(); tl = pt.tolist()
    pr = [0.0] * Nr
    pr[0] = pc
    pi4 = 4.0 * np.pi
    for i in range(Nr - 1):
        h = rl[i + 1] - rl[i]
        ri = rl[i]; pp = pr[i]
        if ri <= 1e-12:
            k1 = 0.0
        else:
            uu = 1.0 - 2.0 * ml[i] / ri
            ap = (ml[i] / (ri * ri) + pi4 * ri * pp) / uu
            k1 = -(hl[i] + pp) * ap - (2.0 / ri) * (pp - tl[i])
        pm = pp + 0.5 * h * k1
        rm_ = 0.5 * (ri + rl[i + 1]); mm_ = 0.5 * (ml[i] + ml[i + 1])
        rh_ = 0.5 * (hl[i] + hl[i + 1]); pt_ = 0.5 * (tl[i] + tl[i + 1])
        uu = 1.0 - 2.0 * mm_ / rm_
        ap = (mm_ / (rm_ * rm_) + pi4 * rm_ * pm) / uu
        k2 = -(rh_ + pm) * ap - (2.0 / rm_) * (pm - pt_)
        pr[i + 1] = pp + h * k2
    return np.array(pr, dtype=DTYPE)


def solve_shell(rho_star, pt_star, R1=10.0, R2=20.0, Nr=2001,
                rmax=None, rout=None):
    """rho_star, pt_star: callables r -> array. Returns prof dict +
    shooting diagnostics. Raises ValueError on over-compactness."""
    if rmax is None:
        rmax = 3.0 * R2
    if rout is None:
        rout = rmax
    r = np.linspace(0.0, rmax, Nr, dtype=DTYPE)
    rho = np.maximum(np.asarray(rho_star(r), dtype=DTYPE), 0.0)
    pt = np.asarray(pt_star(r), dtype=DTYPE)
    vol = 4.0 * np.pi * r ** 2
    m = sh.cumint(vol * rho, r)
    M = float(m[-1])
    u = 1.0 - 2.0 * m / np.maximum(r, 1e-12)
    umin = float(np.min(u[1:]))
    if umin <= 0.02:
        raise ValueError(f'too compact: min(1-2m/r)={umin:.3f}')
    iout = int(np.argmin(np.abs(r - rout)))

    scale = max(float(np.max(rho)), 1e-12)
    pt0 = float(pt[0])

    def F(pc):
        return float(_integrate_pr(r, m, rho, pt, pc)[iout])

    # secant shooting from two starts near pt0 (F is smooth, near-
    # linear in pc); fall back to a bracket scan if it stalls.
    pc, Fval, shot = None, None, 'failed'
    x0, x1 = pt0, pt0 + 0.05 * scale
    f0, f1 = F(x0), F(x1)
    for _ in range(10):
        if abs(f1) < 1e-13 * scale:
            pc, Fval, shot = x1, f1, 'secant'
            break
        if f1 == f0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x2 - x1) > 3.0 * scale:
            break
        x0, f0, x1, f1 = x1, f1, x2, F(x2)
    if pc is None:
        # local scan near pt0: pc is a centre value, it must stay
        # near p_t(0) (regularity) — a far-away argmin|F| would dump
        # a spurious central pressure into a near-vacuum interior.
        grid = pt0 + np.linspace(-0.1, 0.1, 21) * scale
        vals = [F(x) for x in grid]
        i = int(np.argmin(np.abs(vals)))
        pc, Fval = float(grid[i]), float(vals[i])
        shot = 'local-scan'
        # polish by secant on the neighbouring pair
        if 0 < i < 20 and vals[i - 1] * vals[i + 1] < 0:
            pc = float(brentq(F, grid[i - 1], grid[i + 1],
                              xtol=1e-13, rtol=1e-11))
            Fval = F(pc); shot = 'brentq-local'
    pr = _integrate_pr(r, m, rho, pt, pc)

    b = np.where(r > 0, -0.5 * np.log(np.maximum(u, 1e-300)), 0.0)
    aprime = np.where(r > 0,
                      (m / np.maximum(r, 1e-12) ** 2 + 4 * np.pi * r * pr)
                      / np.maximum(u, 1e-300), 0.0)
    a = np.zeros_like(r)
    a[-1] = 0.5 * np.log(max(1.0 - 2.0 * M / r[-1], 1e-300))
    for i in range(Nr - 2, -1, -1):
        a[i] = a[i + 1] - 0.5 * (aprime[i] + aprime[i + 1]) * (r[i + 1] - r[i])

    mp = np.gradient(m, r, edge_order=2)
    rho_ex = np.where(r > 0, mp / (4 * np.pi * np.maximum(r, 1e-12) ** 2),
                      rho[0])
    bp = np.where(r > 0, (mp / np.maximum(r, 1e-12)
                          - m / np.maximum(r, 1e-12) ** 2)
                  / np.maximum(u, 1e-300), 0.0)
    app = np.gradient(aprime, r, edge_order=2)
    p_r_ex = (-2 * m / np.maximum(r, 1e-12) ** 3
              + 2 * aprime * u / np.maximum(r, 1e-12)) / (8 * np.pi)
    p_t_ex = u * (app + aprime ** 2 - aprime * bp
                  + (aprime - bp) / np.maximum(r, 1e-12)) / (8 * np.pi)
    p_r_ex = np.where(r > 0, p_r_ex, 0.0)
    p_t_ex = np.where(r > 0, p_t_ex, 0.0)

    return {'r': r, 'a': a, 'b': b, 'aprime': aprime, 'm': m, 'M': M,
            'rho_ex': rho_ex, 'p_r': pr, 'p_t': pt,
            'p_r_exact': p_r_ex, 'p_t_exact': p_t_ex,
            'rho_star': rho, 'pt_star': pt, 'umin': umin,
            'pc': pc, 'shoot_F': Fval, 'shoot': shot,
            'R1': R1, 'R2': R2}


def realisation_residual(prof):
    r = prof['r']
    band = (r >= prof['R1'] - 2) & (r <= prof['R2'] + 12)
    scale = max(np.max(np.abs(prof['rho_star'])), 1e-12)
    return {'rho_res': float(np.max(np.abs(
                prof['rho_ex'] - prof['rho_star'])[band]) / scale),
            'pr_res': float(np.max(np.abs(
                prof['p_r_exact'] - prof['p_r'])[band]) / scale),
            'pt_res': float(np.max(np.abs(
                prof['p_t_exact'] - prof['pt_star'])[band]) / scale)}


def prof_gfunc(prof, beta, R1=10.0, R2=20.0):
    ea = CubicSpline(prof['r'], np.exp(2 * prof['a']))
    eb = CubicSpline(prof['r'], np.exp(2 * prof['b']))
    rmax = float(prof['r'][-1])
    M = float(prof['M'])

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = len(pts)
        r = np.linalg.norm(pts, axis=1)
        rs = np.where(r > 0, r, 1.0)
        n = pts / rs[:, None]
        rc = np.clip(r, 0.0, rmax)
        S = sh.shift_S(r, R1, R2, 'cos', 1.0, [R1, R2])
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        # Exact Schwarzschild continuation beyond the solved
        # domain (the support ends at R2+8 < rmax, so [38, rmax]
        # is already vacuum; the continuation is C1-matched).
        # WITHOUT this, the old clip() froze e^{2a}, e^{2b} at
        # their rmax values — a kink whose FD tensor (~1e-3)
        # masqueraded as a support-tail NEC pocket in run 2's
        # first attack. Artefact class (i) variant: domain-edge
        # mishandling, caught by the attack protocol.
        eav = ea(rc); ebv_full = eb(rc)
        out = r > rmax
        if np.any(out):
            u = 1.0 - 2.0 * M / np.maximum(r[out], 1e-9)
            eav = eav.copy(); ebv_full = ebv_full.copy()
            eav[out] = u
            ebv_full[out] = 1.0 / u
        g[:, 0, 0] = -eav
        g[:, 0, 1] = g[:, 1, 0] = -S * beta
        ebv = ebv_full - 1.0
        g[:, 1:, 1:] = np.eye(3)[None] + ebv[:, None, None] \
            * n[:, :, None] * n[:, None, :]
        return g

    return gfunc


if __name__ == '__main__':
    import verify_metric as vm
    base = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    r = base['r']
    rho_s = CubicSpline(r, base['rho_ex'])
    pt_s = CubicSpline(r, base['p_t'])     # realised p_t of the control
    prof = solve_shell(lambda x: rho_s(np.clip(x, 0, r[-1])),
                       lambda x: pt_s(np.clip(x, 0, r[-1])), Nr=2001)
    rr = prof['r']
    da = float(np.max(np.abs(prof['a'] - np.interp(rr, r, base['a']))))
    db = float(np.max(np.abs(prof['b'] - np.interp(rr, r, base['b']))))
    dpr = float(np.max(np.abs(prof['p_r']
                              - np.interp(rr, r, base['p_r']))))
    print(f'CONTROL (realised pair -> metric): max|da|={da:.2e} '
          f'max|db|={db:.2e} max|dpr|={dpr:.2e} '
          f"(shoot={prof['shoot']}, F={prof['shoot_F']})")
    print('realisation residual:', realisation_residual(prof))
    That = np.zeros((len(rr), 4, 4))
    That[:, 0, 0] = prof['rho_ex']; That[:, 1, 1] = prof['p_r_exact']
    That[:, 2, 2] = prof['p_t_exact']; That[:, 3, 3] = prof['p_t_exact']
    mi = vm.hawking_ellis_margins(That)
    mb = sh.shell_exact_margins(base)
    band = (rr >= 8) & (rr <= 32)
    bandb = (r >= 8) & (r <= 32)
    print('static NEC band 8-32: base '
          f"{float(np.min(mb['nec'][bandb])):+.3e} vs inverted "
          f"{float(np.min(mi['nec'][band])):+.3e}")
