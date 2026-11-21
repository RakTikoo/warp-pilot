"""
search_super.py — Superluminal lens SL-1 (dedicated, per Rakshit's direction).

Generalised family OUTSIDE Santiago-Schuster-Visser scope:
  lapse alpha(r) = 1 + A_a * wall-bump(r)   (non-unit lapse iff A_a != 0)
  spatial conformal Omega(r) = 1 + A_o * pocket(r)  (non-flat slices iff A_o != 0)
  shift = v (1 - f(r)), Alcubierre shape f.
Control case A_a = A_o = 0 is the Natario class itself (must fail at all v,
per SSV) — included once per velocity as a control, NOT searched.

Screening: N=33 grids, worst all-observer margin in the wall region.
Objective = min(NEC, WEC, SEC, DEC) margins (eigenvalue for Type I,
sampled for non-Type-I; sign is the rigorous content for failures).
Any config with worst > 0 at screening gets refined (N=49/65 + point audit).
"""
import json, time
import numpy as np
import verify_metric as vm
import metrics as mx

rng = np.random.default_rng(20261120)
VS = [0.5, 0.9, 1.0, 1.1, 2.0]


def evaluate(v, cfg, N=33, L=6.0):
    try:
        g, h, (X, Y, Z) = mx.generalized_grid(N, L, v, **cfg)
    except ValueError:
        return None
    r = mx.radii(X, Y, Z)
    mask = (r > 0.3) & (r < 4.5)
    mask[:3] = mask[-3:] = False; mask[:, :3] = mask[:, -3:] = False
    mask[:, :, :3] = mask[:, :, -3:] = False
    summ = vm.grid_margins_summary(g, h, mask=mask)
    worst = min(summ['min_nec'], summ['min_wec'], summ['min_sec'], summ['min_dec'])
    return {'v': v, 'cfg': cfg, 'N': N, 'worst': worst,
            'min_nec': summ['min_nec'], 'min_wec': summ['min_wec'],
            'min_sec': summ['min_sec'], 'min_dec': summ['min_dec'],
            'typeI_frac': summ['typeI_frac_masked']}


def sample_cfg():
    return {'R_f': 1.5,
            'sig_f': float(rng.choice([1.5, 2.0, 3.0])),
            'A_a': float(rng.choice([-0.5, -0.3, 0.3, 0.6, 1.0, 1.5])),
            'R_a': float(rng.choice([1.2, 1.5, 1.8])),
            'sig_a': float(rng.choice([1.5, 2.5])),
            'A_o': float(rng.choice([0.0, 2.0, 5.0, 10.0, 20.0])),
            'R_o': float(rng.choice([0.6, 0.8, 1.1])),
            'sig_o': float(rng.choice([2.0, 4.0]))}


def main(n_per_v=36):
    rows = []
    t0 = time.time()
    for v in VS:
        ctrl = evaluate(v, {'R_f': 1.5, 'sig_f': 2.0, 'A_a': 0.0, 'R_a': 1.5,
                            'sig_a': 2.0, 'A_o': 0.0, 'R_o': 0.8, 'sig_o': 3.0})
        ctrl['control_natario'] = True
        rows.append(ctrl)
        print(f'v={v} CONTROL (Natario) worst={ctrl["worst"]:.3e}', flush=True)
        for i in range(n_per_v):
            cfg = sample_cfg()
            row = evaluate(v, cfg)
            if row is None:
                continue
            rows.append(row)
            if row['worst'] > -0.005:
                print(f'v={v} cfg={cfg} worst={row["worst"]:.3e} '
                      f'typeI={row["typeI_frac"]:.2f} ({time.time()-t0:.0f}s)', flush=True)
        best = max((r for r in rows if r['v'] == v and not r.get('control_natario')),
                   key=lambda d: d['worst'])
        print(f'v={v} BEST worst={best["worst"]:.3e} cfg={best["cfg"]}', flush=True)
    with open('results/stageSL1.json', 'w') as fh:
        json.dump(rows, fh, indent=1)
    print('SL-1 DONE')


if __name__ == '__main__':
    main()
