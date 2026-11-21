"""
stageB_scan.py — Stage B: 3D grid audits of shell + shift (beta_w = 0.02,
Fuchs value) over profile families and masses. Screening resolution N=41.
Writes results/stageB.json (append-safe: full rewrite each run).
"""
import json, time
import numpy as np
import search_shell as ss

CONFIGS = []
for kind, params in [('constant', {}),
                     ('smoothbox', {'edge': 2.0}),
                     ('smoothbox', {'edge': 3.0}),
                     ('gauss', {'Rm': 15.0, 'wd': 2.5}),
                     ('matched', {'Rs': 15.0, 'wd': 2.5, 'floor': 0.05}),
                     ('matched', {'Rs': 15.0, 'wd': 4.0, 'floor': 0.2}),
                     ('edgepeaked', {'wd': 2.5, 'floor': 0.15})]:
    for sr, sp in [(2.0, 1.16), (1.5, 0.87)]:
        for M in (1.0, 2.0, ss.FUCHS_M_GEOM):
            CONFIGS.append((M, kind, params, sr, sp))

rows = []
t0 = time.time()
for (M, kind, params, sr, sp) in CONFIGS:
    try:
        row = ss.stageB_eval(M, kind, params, sr, sp, beta_w=0.02, N=41)
    except Exception as e:
        print('FAIL', kind, M, repr(e), flush=True)
        continue
    row['params'] = params
    rows.append(row)
    print(f"M={M:.3f} {kind} sr={sr} worst={row['worst']:.3e} "
          f"nec={row['min_nec']:.2e} dec={row['min_dec']:.2e} typeI={row['typeI_frac']:.2f} "
          f"({time.time()-t0:.0f}s)", flush=True)

rows.sort(key=lambda d: -d['worst'])
with open('results/stageB.json', 'w') as fh:
    json.dump(rows, fh, indent=1)
print('STAGE B DONE, best:')
for row in rows[:5]:
    print('  ', row['kind'], row['params'], 'M=', round(row['M_geom'], 3),
          'worst=', f"{row['worst']:.3e}")
