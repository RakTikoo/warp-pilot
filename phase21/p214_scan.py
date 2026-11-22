#!/usr/bin/env python3
"""
p214_scan.py -- P21-4 SCAN: f(T,B) on the shared bed.
Grid (run record, stated before running; FULL care at
superluminal beta, no thinning): per beta in {0.1, 1.1, 1.5}
DIRECT: B1a gamma in 8, B1b gamma in 6, B2 (alpha, gamma)
in 3x5, B3 kappa in 6, GR control = 36 rows/beta.
Every row: binding partial/full/sign/ratio_med + ratio-free
cross-check (asserted), health (Geff>0, finiteness, B-scalar
proxy), full-volume NEC read at h in {0.3, 0.15}
(tol=1.430e-4).  Rows with partial >= 0.50 additionally get
the full-volume ALL-FOUR-EC read at h=0.15.
Gate (p214_gate.json) must have passed.  float64.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase21')
import p214_lib as L   # noqa: E402

HERE = '/home/hatch/workspace/warp-pilot/phase21/results/'
gate = json.load(open(HERE + 'p214_gate.json'))
assert gate['gate_passed'], 'control gate failed -- scan must not run'
B_SIGN = gate['B_sign']

ROWS = []
for g in (-20.0, -5.0, -1.0, -0.2, 0.2, 1.0, 5.0, 20.0):
    ROWS.append(('B1a', g))
for g in (-5.0, -1.0, -0.2, 0.2, 1.0, 5.0):
    ROWS.append(('B1b', g))
for a in (-5.0, 5.0, 20.0):
    for g in (-5.0, -1.0, 0.0, 1.0, 5.0):
        ROWS.append(('B2', (a, g)))
for k in (-20.0, -5.0, -1.0, 1.0, 5.0, 20.0):
    ROWS.append(('B3', k))
ROWS.append(('GR', None))


def main():
    t0 = time.time()
    out = dict(item='P21-4 scan, BBW Eq.(42) published form',
               tol=L.TOL, B_sign=B_SIGN, betas={})
    for beta in L.BETAS:
        tb = time.time()
        Fb = L.binding_fields(beta, B_sign=B_SIGN)
        Fv = {h: L.volume_fields(beta, h, B_sign=B_SIGN)
              for h in (0.3, 0.15)}
        rows = []
        for fam, par in ROWS:
            row = L.binding_row(Fb, fam, par)
            row['par'] = list(par) if isinstance(par, tuple) else par
            row['volume'] = {str(h): L.volume_row(Fv[h], fam, par)
                             for h in (0.3, 0.15)}
            if row['partial'] >= 0.50:
                row['volume_ec_h0.15'] = L.volume_ec_row(
                    Fv[0.15], fam, par)
            rows.append(row)
            print(f"beta={beta} {fam} par={par}: partial="
                  f"{row['partial']:.3f} full={row['full']:.3f} "
                  f"health={row['health_pass']} volviol0.15="
                  f"{row['volume']['0.15']['nec_viol_frac_vol']:.3f}",
                  flush=True)
        out['betas'][str(beta)] = dict(
            n_binding=int(len(Fb['pts'])),
            maxdef=float(Fb['bd']['maxdef']), rows=rows,
            beta_runtime_s=time.time() - tb)
        with open(HERE + 'p214_scan.json', 'w') as fh:
            json.dump(out, fh, indent=2,
                      default=lambda o: bool(o) if isinstance(
                          o, (np.bool_,)) else float(o))
        print(f'beta={beta} done in {time.time() - tb:.0f}s', flush=True)
    out['runtime_s'] = time.time() - t0
    with open(HERE + 'p214_scan.json', 'w') as fh:
        json.dump(out, fh, indent=2,
                  default=lambda o: bool(o) if isinstance(
                      o, (np.bool_,)) else float(o))
    print('scan done', flush=True)


if __name__ == '__main__':
    main()
