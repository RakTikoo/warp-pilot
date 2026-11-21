"""
x4_scalar.py — X4: non-minimally coupled scalar (Fewster-Osterbrink /
Fliss et al. seam). Superluminal points MANDATORY (S4).

Theory: S = int sqrt(-g) [ F(phi) R / (16 pi) - 1/2 (dphi)^2 - V ],
F = 1 - 8 pi xi phi^2 (F > 0 required — gravity keeps its sign).
Field equation (standard scalar-tensor form):
    F G_ab = 8 pi T^(min)_ab + (nabla_a nabla_b - g_ab Box) F
so the geometry's demand decomposes as
    8 pi T^(min) = F G_ab - Hess(F) + g_ab Box(F),
where T^(min) is the scalar's own (canonical kinetic + potential)
stress tensor. V drops out of every null contraction, so the crisp
Jordan-frame test is: NEC of T^(min) >= 0 for all null directions
(necessary for canonical scalar + any NEC-legal companion matter).

AUDITS per config (shell family, beta in {0.05 control, 1.1, 1.5}):
  JORDAN: margins of T^(min) (eigenvalue judge on its Eulerian form).
  EINSTEIN FRAME: g_tilde = F g; margins of G[g_tilde]/8pi. If the
  Jordan decomposition legalises the matter but the Einstein-frame
  tensor still violates NEC (it must, for superluminal transport),
  the pass is a frame artefact = NEGATIVE (task rule; Fliss et al.:
  the effective ANEC is restored in the Einstein frame).
  DSNEC: scaling-level gate only — required deficit density D vs
  |xi| phi_max^2 / (delta^-)^2 scale (checkpoint's stated
  proportionality; prefactor/exact normalisation NOT re-derived
  from Fliss et al. — flagged, not hidden).
phi(r): C2 bump in the wall (smootherstep edges), phi0 scanned with
F > 0 enforced. Hess(F) analytic (phi is a prescribed function of
r); Gamma from the auditor's own _gamma_at at the same h.
float64 everywhere.
"""
import json, time
import numpy as np
from scipy.interpolate import CubicSpline

import shell as sh
import verify_metric as vm
from verify_finalist import dense_points

DTYPE = np.float64
R1, R2 = 10.0, 20.0
EIGHT_PI = 8.0 * np.pi


def phi_profile(phi0, Nr=4001, rmax=60.0, kind='bump'):
    r = np.linspace(0.0, rmax, Nr)
    if kind == 'bump':
        prof = sh.smootherstep((r - 6.0) / 4.0) \
            * (1.0 - sh.smootherstep((r - 20.0) / 4.0))
    else:  # 'tail': monotone, one-signed curvature through the wall
        prof = 1.0 / (1.0 + (r / 15.0) ** 2)
    phi = phi0 * prof
    cs = CubicSpline(r, phi)
    return cs, cs.derivative(), cs.derivative(2)


def coupling_terms(gfunc, pts, h, xi, phi0, kind='bump'):
    """Returns F, Hess(F) (P,4,4), Box(F) (P,) at pts."""
    cs, d1, d2 = phi_profile(phi0, kind=kind)
    Gamma, g, ginv = vm._gamma_at(gfunc, pts, h)
    r = np.linalg.norm(pts, axis=1)
    rs = np.where(r > 0, r, 1.0)
    n = pts / rs[:, None]
    rc = np.clip(r, 0.0, 60.0)
    phi = cs(rc); ph1 = d1(rc); ph2 = d2(rc)
    F = 1.0 - EIGHT_PI * xi * phi ** 2
    F1 = -2.0 * EIGHT_PI * xi * phi * ph1            # dF/dr
    F2 = -2.0 * EIGHT_PI * xi * (ph1 ** 2 + phi * ph2)
    P = len(pts)
    dF = np.zeros((P, 4))
    dF[:, 1:] = F1[:, None] * n
    ddF = np.zeros((P, 4, 4))
    # spatial second derivatives: F'' n_i n_j + (F'/r)(delta_ij - n_i n_j)
    coef = np.where(r > 0, F1 / rs, 0.0)
    for i in range(3):
        for j in range(3):
            ddF[:, 1 + i, 1 + j] = F2 * n[:, i] * n[:, j] \
                + coef * ((1.0 if i == j else 0.0) - n[:, i] * n[:, j])
    # Hess_ab = ddF_ab - Gamma^c_ab dF_c (dF_0 = 0: spatial c only
    # contribute, the full einsum handles it)
    Hess = ddF - np.einsum('pabc,pc->pab', Gamma, dF)
    BoxF = np.einsum('pab,pab->p', ginv, Hess)
    return F, Hess, BoxF, g


def margins_of_that(That):
    m = vm.hawking_ellis_margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    sig = scale > 1e-7
    out = {}
    if sig.sum():
        for k in ('nec', 'wec', 'sec', 'dec'):
            out[k] = float(np.min(m[k][sig]))
        out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
        out['typeI_frac'] = float(np.mean(m['typeI'][sig]))
    return out


def run_config(M, beta, xi, phi0, pts, kind='bump'):
    prof = sh.build_shell(R1, R2, M, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [R1, R2])
    h = 0.3
    G, That_req, m_req = vm.einstein_at_points(gf, pts, h=h)
    F, Hess, BoxF, g = coupling_terms(gf, pts, h, xi, phi0, kind)
    if np.min(F) <= 0:
        return {'M': M, 'beta': beta, 'xi': xi, 'phi0': phi0, 'kind': kind,
                'F_min': float(np.min(F)), 'verdict': 'F<=0 excluded'}
    Tmin_cov = (F[:, None, None] * G - Hess
                + BoxF[:, None, None] * g) / EIGHT_PI
    That_min = vm.eulerian_that(g, Tmin_cov)
    jm = margins_of_that(That_min)
    # Einstein frame: g_tilde = F * g
    def gf_tilde(p):
        gg = gf(p)
        rr = np.linalg.norm(p, axis=1)
        cs, _, _ = phi_profile(phi0, kind=kind)
        Fp = 1.0 - EIGHT_PI * xi * cs(np.clip(rr, 0, 60.0)) ** 2
        return Fp[:, None, None] * gg
    _, That_e, _ = vm.einstein_at_points(gf_tilde, pts, h=h)
    em = margins_of_that(That_e)
    return {'M': M, 'beta': beta, 'xi': xi, 'phi0': phi0, 'kind': kind,
            'F_min': float(np.min(F)),
            'GR_req_worst': m_req and float(np.min(
                np.minimum(np.minimum(m_req['nec'], m_req['wec']),
                           np.minimum(m_req['sec'], m_req['dec'])))),
            'jordan_Tmin': jm, 'einstein': em}


def main():
    t0 = time.time()
    pts = dense_points()[::3]          # ~737 pts
    out = {'configs': []}
    # F2 follow-up: monotone tail profile (one-signed F'' in wall)
    for (M, beta) in ((2.0, 0.05), (2.0, 1.1), (2.0, 1.5)):
        for xi, phi0 in ((1.0 / 6.0, 0.3), (0.25, 0.3)):
            row = run_config(M, beta, xi, phi0, pts, kind='tail')
            out['configs'].append(row)
            jt = row.get('jordan_Tmin', {}); et = row.get('einstein', {})
            print(f"TAIL M={M:g} beta={beta} xi={xi:.3f} phi0={phi0}: "
                  f"F_min {row.get('F_min', float('nan')):.3f} | "
                  f"jordan NEC {jt.get('nec', float('nan')):+.2e} | "
                  f"einstein NEC {et.get('nec', float('nan')):+.2e}",
                  flush=True)
    for (M, beta) in ((2.0, 0.05), (2.0, 1.1), (2.0, 1.5), (8.0, 1.5)):
        for xi, phi0 in ((1.0 / 6.0, 0.1), (1.0 / 6.0, 0.3),
                         (0.25, 0.1), (0.25, 0.3)):
            row = run_config(M, beta, xi, phi0, pts)
            out['configs'].append(row)
            jt = row.get('jordan_Tmin', {})
            et = row.get('einstein', {})
            print(f"M={M:g} beta={beta} xi={xi:.3f} phi0={phi0}: "
                  f"F_min {row.get('F_min', float('nan')):.3f} | "
                  f"jordan worst {jt.get('worst', float('nan')):+.3e} "
                  f"(NEC {jt.get('nec', float('nan')):+.2e}) | "
                  f"einstein worst {et.get('worst', float('nan')):+.3e} "
                  f"(NEC {et.get('nec', float('nan')):+.2e})", flush=True)
    out['elapsed_s'] = time.time() - t0
    out['dsnec_note'] = ('Scaling gate: required smeared deficit '
                         'D*delta vs |xi| phi_max^2 / delta^2 — see '
                         'CHECKPOINT; prefactor not re-derived.')
    json.dump(out, open('results/x4_scalar.json', 'w'), indent=1,
              default=float)
    print('X4 DONE', flush=True)


if __name__ == '__main__':
    main()
