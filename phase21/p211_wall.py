#!/usr/bin/env python3
"""
p211_wall.py -- P21-1(b) WALL (amended: beta in {0.1, 1.1, 1.5} DIRECT):
Finalist-A shared bed (p103_lib), SMS required-Weyl supply.

Conventions: k4^2 = 8 pi (bed units: That_GR = G/(8 pi)).
SMS: G = k4^2 tau + k5^4 Pi - E,  k5^4 = 6 k4^2 / lam, lam = 1
(wall units) unless stated.  All frame work in the Eulerian
orthonormal frame of verify_metric (That arrays are covariant
orthonormal components; mixed components via eta).

Rows:
 (W0) tau = 0: required E_req = -G.  Audits: (i) trace(E_req)
      relative; supply ratio E_req(k,k)/(k4^2 D) at binding pts
      (== 1 identically, by construction); (ii) div E_req = 0 by
      Bianchi (div Pi = 0), stated as identity.
 (W1) trace-fixing dust: per point, solve the trace condition
      k5^4 rho^2/6 - k4^2 rho - tr(G) = 0 for rho >= 0 (dust
      tau^mu_nu = diag(-rho,0,0,0), tr Pi = rho^2/6).  Where a
      rho >= 0 root exists, E is traceless by construction;
      report: fraction of binding/volume points with a legal
      root (scan-bar analogue: full/partial), E(k,k) supply
      ratio stats, Pi(k,k) sign (Pi-carries check), and the
      (ii) scaling ratio |k4^2 div tau| / |k5^4 div Pi| ~
      lam/(6 rho) (gradient scale cancels), which is the
      divergence-identity residual in units of the RHS scale
      for ANY tau field with these pointwise values varying on
      the wall scale.
float64, system python3.
"""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase10')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase11')
import verify_metric as vm      # noqa: E402
import p103_lib as lib          # noqa: E402
import p111_lib as p111         # noqa: E402
import p61_scan as p61          # noqa: E402

K4 = lib.EIGHT_PI
LAM = 1.0
K5_4 = 6.0 * K4 / LAM
RES = '/home/hatch/workspace/warp-pilot/phase21/results/'
ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def mixed(That_cov):
    """Covariant orthonormal -> mixed: T^a_b = eta^{aa} T_ab."""
    M = That_cov.copy()
    M[..., 0, :] *= -1.0
    return M


def trace_mixed(That_cov):
    M = mixed(That_cov)
    return np.einsum('...ii->...', M)


def null_contract(That_cov, n_hat):
    lin = 2.0 * np.einsum('pi,pi->p', That_cov[:, 0, 1:], n_hat)
    quad = np.einsum('pij,pi,pj->p', That_cov[:, 1:, 1:], n_hat, n_hat)
    return That_cov[:, 0, 0] + lin + quad


def dust_pi_hat(rho):
    """Pi (covariant orthonormal) for dust tau_hat = diag(rho,0,0,0)
    (covariant), tau^mu_nu = diag(-rho,0,0,0): tr Pi_mixed = rho^2/6;
    Pi^mu_nu = diag(-rho^2/12, rho^2/12, rho^2/12, rho^2/12)
    (from p211_throat.pi_mixed with pr=pt=0).  Covariant: t flips."""
    Pi_m = np.zeros((len(rho), 4, 4))
    Pi_m[:, 0, 0] = -rho**2 / 12
    for i in (1, 2, 3):
        Pi_m[:, i, i] = rho**2 / 12
    # covariant from mixed: T_ab = eta_aa T^a_b (no sum): T_00 = -T^0_0
    Pi_cov = Pi_m.copy()
    Pi_cov[:, 0, 0] = -Pi_m[:, 0, 0]
    return Pi_cov


def run_beta(beta):
    bd = lib.bed(beta)
    exp = lib.EXPECTED[beta]
    assert bd['n_bind'] == exp[0], (bd['n_bind'], exp)
    assert abs(bd['maxdef'] - exp[1]) / exp[1] < 0.01
    That = bd['That_GR_b']
    G_cov = K4 * That
    trG = trace_mixed(That) * K4
    # ---- W0: tau = 0, E_req = -G ----
    E_cov = -G_cov
    trE = trace_mixed(E_cov)
    escale = np.max(np.abs(mixed(E_cov)), axis=(1, 2))
    Ek = null_contract(E_cov, bd['n_b'])
    ratio0 = Ek / (K4 * bd['D_that'])
    w0 = dict(traceE_rel_max=float(np.max(np.abs(trE) / escale)),
              traceE_rel_med=float(np.median(np.abs(trE) / escale)),
              supply_ratio_min=float(np.min(ratio0)),
              supply_ratio_med=float(np.median(ratio0)),
              supply_ratio_max=float(np.max(ratio0)))
    # ---- W1: trace-fixing dust at binding points ----
    a = K5_4 / 6.0
    disc = K4**2 + 4 * a * trG
    ok = disc >= 0
    rho_plus = np.where(ok, (K4 + np.sqrt(np.maximum(disc, 0)))
                        / (2 * a), np.nan)
    rho_minus = np.where(ok, (K4 - np.sqrt(np.maximum(disc, 0)))
                         / (2 * a), np.nan)
    # legal root: rho >= 0; prefer the smaller (minus) root when legal
    rho = np.where((rho_minus >= 0), rho_minus,
                   np.where(rho_plus >= 0, rho_plus, np.nan))
    legal = np.isfinite(rho)
    Pi_cov = dust_pi_hat(np.where(legal, rho, 0.0))
    tau_cov = np.zeros_like(That)
    tau_cov[:, 0, 0] = np.where(legal, rho, 0.0)
    E1_cov = K4 * tau_cov + K5_4 * Pi_cov - G_cov
    trE1 = trace_mixed(E1_cov)
    E1k = null_contract(E1_cov, bd['n_b'])
    Pik = null_contract(Pi_cov, bd['n_b'])
    ratio1 = E1k / (K4 * bd['D_that'])
    div_ratio = LAM / (6.0 * np.where(legal, rho, np.nan))
    w1 = dict(frac_legal_root=float(np.mean(legal)),
              frac_full_supply=float(np.mean(
                  legal & (ratio1 >= 1.0))),
              frac_partial_supply=float(np.mean(
                  legal & (ratio1 >= 0.5))),
              traceE1_rel_max_legal=float(np.max(
                  np.abs(trE1[legal]) / escale[legal])) if legal.any()
              else None,
              supply_ratio_med_legal=float(np.nanmedian(
                  np.where(legal, ratio1, np.nan))),
              supply_ratio_min_legal=float(np.nanmin(
                  np.where(legal, ratio1, np.nan))),
              pi_kk_frac_negative=float(np.mean(Pik[legal] < 0))
              if legal.any() else None,
              pi_kk_over_k4D_med=float(np.median(
                  (K5_4 * Pik[legal]) / (K4 * bd['D_that'][legal])))
              if legal.any() else None,
              rho_med_legal=float(np.nanmedian(rho)),
              div_resid_over_RHS_med=float(np.nanmedian(div_ratio)),
              div_resid_over_RHS_min=float(np.nanmin(div_ratio)))
    # ---- volume points: W1 legality + W0 trace ----
    pts_v, r_v = p111.volume_points()
    _, That_v, _ = vm.einstein_at_points(bd['gf'], pts_v, h=0.3)
    Gv = K4 * That_v
    trGv = trace_mixed(That_v) * K4
    trEv = trace_mixed(-Gv)
    esc_v = np.max(np.abs(mixed(-Gv)), axis=(1, 2))
    disc_v = K4**2 + 4 * a * trGv
    okv = disc_v >= 0
    rm_v = np.where(okv, (K4 - np.sqrt(np.maximum(disc_v, 0)))
                    / (2 * a), np.nan)
    rp_v = np.where(okv, (K4 + np.sqrt(np.maximum(disc_v, 0)))
                    / (2 * a), np.nan)
    legal_v = np.where((rm_v >= 0), True, np.where(rp_v >= 0, True,
                                                   False))
    w = r_v**2 / np.sum(r_v**2)
    vol = dict(W0_traceE_rel_med=float(np.median(np.abs(trEv) / esc_v)),
               W1_frac_legal_root=float(np.mean(legal_v)),
               W1_frac_legal_root_r2w=float(np.sum(w[legal_v])))
    return dict(beta=beta, n_bind=bd['n_bind'],
                maxdef=bd['maxdef'], W0=w0, W1=w1, volume=vol)


def main():
    out = dict(item='P21-1(b) wall SMS required-E supply, amended '
                  'beta set {0.1, 1.1, 1.5} DIRECT',
               k4sq=K4, lambda_=LAM, k5_4=K5_4, betas=[])
    for beta in (0.1, 1.1, 1.5):
        res = run_beta(beta)
        out['betas'].append(res)
        print(beta, 'n', res['n_bind'], 'maxdef %.3e' % res['maxdef'],
              'W0 trErel med %.3f' % res['W0']['traceE_rel_med'],
              'W1 legal %.3f' % res['W1']['frac_legal_root'],
              'full %.3f' % res['W1']['frac_full_supply'],
              'divratio med %.3g' % res['W1']['div_resid_over_RHS_med'],
              flush=True)
    with open(RES + 'p211_wall.json', 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    print('wall done')


if __name__ == '__main__':
    main()
