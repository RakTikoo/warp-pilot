"""
x1_ladder.py — X1 velocity ladder (S1): audit the best toroidal base
(from x1_de, or the best prescribed profiles if DE found nothing better)
across v in {0.02, 0.05, 0.1} + S1 grid {0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0}
and Rmaj in {30, 45, 60} (aspect 2, 3, 4), fresh-seed randomised points.
Near-passes (worst > -1e-6) get h=0.15 + a second seed automatically.
Usage: python3 x1_ladder.py [genes_json | prescribed]
"""
import json, sys, time
import numpy as np

import verify_metric as vm
import x1_torus as x1
import x1_de

DTYPE = np.float64
VELS = [0.02, 0.05, 0.1, 0.5, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0]
RMAJS = [30.0, 45.0, 60.0]


def load_base(mode):
    if mode == 'prescribed':
        tp = x1.torus_profiles(2.0, delta=15.0)
        return tp, 'prescribed M=2 Delta=15'
    d = json.load(open(mode))
    genes = np.array(d['genes'])
    return x1_de.genes_to_profiles(genes), f'DE genes from {mode}'


def worst_at(tp, Rmaj, beta, seed, h, n_tube=210):
    gf = x1.torus_gfunc(tp, Rmaj, beta)
    pts = x1.torus_points(Rmaj, seed, n_tube=n_tube)
    _, That, m = vm.einstein_at_points(gf, pts, h=h)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-7, 1e-3 * abs(rho_peak))
    sig = scale > thr
    w = {k: float(np.min(m[k][sig])) for k in ('nec', 'wec', 'sec', 'dec')}
    w['worst'] = min(w.values())
    w['typeI_frac_sig'] = float(np.mean(m['typeI'][sig]))
    w['rho_peak'] = rho_peak
    return w


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'results/x1_de_Rmaj45.json'
    tp, label = load_base(mode)
    print('X1 ladder base:', label, flush=True)
    out = {'base': label, 'rows': []}
    t0 = time.time()
    for Rmaj in RMAJS:
        for v in VELS:
            w = worst_at(tp, Rmaj, v, seed=777, h=0.3)
            row = {'Rmaj': Rmaj, 'aspect': Rmaj / 15.0, 'beta': v, **w}
            if w['worst'] > -1e-6:
                w2 = worst_at(tp, Rmaj, v, seed=31337, h=0.15, n_tube=300)
                row['confirm_h0.15_seed31337'] = w2
                print(f'  NEAR-PASS Rmaj={Rmaj} v={v}: h0.3 {w["worst"]:+.3e}'
                      f' -> h0.15 {w2["worst"]:+.3e}', flush=True)
            out['rows'].append(row)
            print(f'  Rmaj={Rmaj:5.1f} v={v:4.2f}: worst {w["worst"]:+.4e} '
                  f'(NEC {w["nec"]:+.3e}) TypeI {w["typeI_frac_sig"]:.3f}',
                  flush=True)
    out['elapsed_s'] = time.time() - t0
    json.dump(out, open('results/x1_ladder.json', 'w'), indent=1, default=float)
    print('X1 LADDER DONE', flush=True)


if __name__ == '__main__':
    main()
