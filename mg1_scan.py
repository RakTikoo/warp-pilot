"""
mg1_scan.py — MG-1 Stage 1 scan: f(R) = R + alpha R^2 on the generalised
ansatz. alpha reported dimensionlessly: ahat = alpha * R_*, R_* = max|R|
over sample points of the SAME config at alpha = 0 (GR curvature scale).
A config is interesting only if worst matter margin > 0 AND T_eff NEC < 0
(the geometry must be doing warp work) AND F > 0 everywhere.
"""
import json, time
import numpy as np
import mg1_fr as mg

AHATS = [1e-3, 1e-2, 1e-1, 1.0, 10.0]
AMPS = [(0.0, 0.0), (0.3, 0.0), (-0.3, 0.0), (0.0, 0.3), (0.0, -0.3),
        (0.3, 0.3), (-0.3, -0.3)]
VS = [0.3, 0.9, 1.0, 1.5, 2.0, 3.0]


def run_stage1(R=1.0, DoverR=0.25, eta=0.0, tag='stage1'):
    Delta = DoverR * R
    pts = mg.sample_points(R, Delta)
    rows = []
    t0 = time.time()
    for (aA, aC) in AMPS:
        for v in VS:
            base = mg.audit_config_fast(v, R, Delta, aA, aC, eta, 0.0, pts)
            base['ahat'] = 0.0
            rows.append(base)
            Rstar = base['R_absmax']
            for ah in AHATS:
                alpha = ah / Rstar if Rstar > 0 else 0.0
                r = mg.audit_config_fast(v, R, Delta, aA, aC, eta, alpha, pts)
                r['ahat'] = ah
                r['R_star'] = Rstar
                rows.append(r)
            print(f"amps=({aA},{aC}) v={v} done ({time.time()-t0:.0f}s) "
                  f"GR worst={base['worst_m']:+.3e}", flush=True)
    # negative-alpha diagnostics (flagged unstable: f_RR = 2 alpha < 0)
    for (aA, aC) in [(0.0, 0.0), (0.3, 0.3)]:
        for v in (1.0, 2.0):
            base = [r for r in rows if r['aA'] == aA and r['aC'] == aC
                    and r['v_s'] == v and r['ahat'] == 0.0][0]
            Rstar = base['R_absmax']
            for ah in (-0.1, -1.0):
                r = mg.audit_config_fast(v, R, Delta, aA, aC, eta, ah / Rstar, pts)
                r['ahat'] = ah
                r['R_star'] = Rstar
                r['UNSTABLE_DIAGNOSTIC'] = True
                rows.append(r)
    with open(f'results/mg1_{tag}.json', 'w') as fh:
        json.dump(rows, fh, indent=1)
    print(f'{tag} DONE: {len(rows)} evals in {time.time()-t0:.0f}s')
    return rows


if __name__ == '__main__':
    run_stage1()
