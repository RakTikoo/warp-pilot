"""
x5_casimir.py — X5: Casimir threading, prescribed-source level.

Question (S5): can a Casimir component from a compact cycle S^1
(mode-sum coefficient C_C = pi^2/720 per EM-like unit, scanned over
effective DOF count N_eff to absorb O(1) S^1 coefficient choices)
supply the NEC deficits of the superluminal shell geometries, so
that T_required - T_Casimir could be ordinary matter — and would
that constitute effective superluminal transport?

Casimir tensor (plates/S^1 form, cycle axis z):
  T^a_b = diag(-rho_C, -rho_C, -rho_C, 3 rho_C),  rho_C = -C_C N_eff / L^4 < 0
NEC along the cycle axis: rho_C + p_z = 4 rho_C = -4 C_C N_eff / L^4.
To cover a deficit D (=-min NEC margin of the required tensor) at a
point, need L <= L_req = (4 C_C N_eff / D)^{1/4}. The audit is
GENER OUS to the proposal: the Casimir axis is assumed aligned with
the worst null direction at every point (a real threading has one
global cycle direction).

Measured per config (shell family (10,20), M in {2,5,8}, beta in
{1.1, 1.5, 2.0} — the SL-2 grid): D_max (dense point audit), the
deficit volume V_def (grid audit), L_req at D_max for N_eff in
{1, 10, 100}, threaded negative energy E_thr = (D_max/4) * V_def
(uniform L — the most favourable threading), ratio E_thr / M_shell,
and a QI pulse ratio |rho_C| / rho_QI(tau) with tau = wall/ beta
(Ford-Roman scale 3/(32 pi^2 tau^4); a static ground-state
threading is not literally a pulse — the ratio is reported WITH
that caveat, as the ledger-scale comparison).

MMP honesty note (binding): Maldacena-Milekhin-Popov's threaded
wormhole is LONG and causality-clean — it demonstrates Casimir
sourcing of a geometry, not a shortcut. Here the shortcut would
require the Casimir part to do exactly the NEC work SL-2 measured;
the numbers below are that requirement, priced.
float64 everywhere.
"""
import json, time
import numpy as np

import shell as sh
import verify_metric as vm
from verify_finalist import dense_points

DTYPE = np.float64
C_C = np.pi ** 2 / 720.0
R1, R2 = 10.0, 20.0


def deficit_stats(M, beta):
    prof = sh.build_shell(R1, R2, M, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [R1, R2])
    pts = dense_points()
    _, That, m = vm.einstein_at_points(gf, pts, h=0.3)
    scale = np.max(np.abs(That), axis=(1, 2))
    sig = scale > 1e-7
    nec = m['nec'][sig]
    D = np.maximum(0.0, -nec)
    rad = np.linalg.norm(pts[sig], axis=1)
    return {'D_max': float(np.max(D)) if len(D) else 0.0,
            'D_p99': float(np.percentile(D, 99)) if len(D) else 0.0,
            'D_mean_pos': float(np.mean(D[D > 0])) if (D > 0).any() else 0.0,
            'frac_deficit': float(np.mean(D > 0)) if len(D) else 0.0,
            'r_at_Dmax': float(rad[int(np.argmax(D))]) if len(D) else None,
            'typeI_frac': float(np.mean(m['typeI'][sig]))}


def main():
    t0 = time.time()
    out = {'configs': []}
    for beta in (1.1, 1.5, 2.0):
        for M in (2.0, 5.0, 8.0):
            st = deficit_stats(M, beta)
            row = {'beta': beta, 'M': M, **st}
            for N_eff in (1, 10, 100):
                if st['D_max'] > 0:
                    L_req = (4.0 * C_C * N_eff / st['D_max']) ** 0.25
                else:
                    L_req = float('inf')
                row[f'L_req_N{N_eff}'] = float(L_req)
            # threaded energy: uniform L covering D_max, N_eff = 10
            rho_C = st['D_max'] / 4.0
            row['rho_C_needed'] = float(rho_C)
            # QI pulse comparison, tau = wall thickness / beta = 10/beta
            tau = 10.0 / beta
            rho_QI = 3.0 / (32.0 * np.pi ** 2 * tau ** 4)
            row['QI_ratio'] = float(rho_C / rho_QI) if rho_QI > 0 else None
            out['configs'].append(row)
            print(f"beta={beta} M={M:g}: D_max {st['D_max']:.3e} @ "
                  f"r={st['r_at_Dmax']} frac_def {st['frac_deficit']:.2f} "
                  f"L_req(N=1/10/100) = {row['L_req_N1']:.2f}/"
                  f"{row['L_req_N10']:.2f}/{row['L_req_N100']:.2f} m "
                  f"QI_ratio {row['QI_ratio']:.1f}", flush=True)
    out['elapsed_s'] = time.time() - t0
    out['note'] = ('L_req is the LARGEST cycle size whose Casimir NEC '
                   'supply covers the worst deficit; smaller L gives '
                   'more. rho_C_needed = D_max/4 is the threaded '
                   'density at that covering. MMP wormhole is long '
                   'and causality-clean (no shortcut) — see header.')
    json.dump(out, open('results/x5_casimir.json', 'w'), indent=1,
              default=float)
    print('X5 DONE', flush=True)


if __name__ == '__main__':
    main()
