"""
x1_phi_ladder.py — velocity ladder on the best phi-dependent
torus base from x1_phi.py (Rmaj=45): v in {0.02, 1.1, 1.5, 2.0},
fresh-seed audits at h=0.3 and h=0.15 (the X1 protocol).
Usage: python3 x1_phi_ladder.py results/x1_phi_Rmaj45.json
"""
import json, sys, time
import numpy as np

import x1_phi
import verify_metric as vm
from x1_torus import torus_points

DTYPE = np.float64


def main():
    d = json.load(open(sys.argv[1]))
    Rmaj = d['Rmaj']
    genes = np.array(d['genes'])
    out = {'Rmaj': Rmaj, 'rows': []}
    for v in (0.0, 0.02, 1.1, 1.5, 2.0):
        gf = x1_phi.genes_to_gfunc(genes, Rmaj, v)
        row = {'v': v}
        for seed, n in ((555001, 2400), (777001, 2400)):
            pts = torus_points(Rmaj, seed, n_tube=n)
            _, _, m1 = vm.einstein_at_points(gf, pts, h=0.3)
            _, _, m2 = vm.einstein_at_points(gf, pts, h=0.15)
            for hh, mm in (('h0.3', m1), ('h0.15', m2)):
                w = float(np.min(np.minimum(
                    np.minimum(mm['nec'], mm['wec']),
                    np.minimum(mm['sec'], mm['dec']))))
                row[f'seed{seed}_{hh}'] = {
                    'worst': w, 'nec': float(np.min(mm['nec'])),
                    'typeI': float(np.mean(mm['typeI']))}
            print(f'v={v} seed={seed}: worst h0.3 '
                  f"{row[f'seed{seed}_h0.3']['worst']:+.4e} h0.15 "
                  f"{row[f'seed{seed}_h0.15']['worst']:+.4e} "
                  f"TypeI {row[f'seed{seed}_h0.3']['typeI']:.3f}",
                  flush=True)
        out['rows'].append(row)
    json.dump(out, open('results/x1_phi_ladder.json', 'w'), indent=1,
              default=float)
    print('PHI LADDER DONE', flush=True)


if __name__ == '__main__':
    main()
