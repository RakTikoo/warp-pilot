import json, time
import numpy as np
from stageC_opt import eval_config, PTS
FUCHS_M = 3.334274
rows = []
def run(tag, **kw):
    t0 = time.time()
    r = eval_config(**kw)
    r['tag'] = tag
    rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}",
          'typeI=', r['typeI_frac_sig'], f"({time.time()-t0:.0f}s)", flush=True)

base = dict(kind='smoothbox', params={'edge': 3.0}, sr=2.0, sp=1.16)
for M in (3.0, 2.7, 2.4, 2.1, 1.8):
    run(f'M={M}', M=M, **base)
for bw in (0.03, 0.05, 0.08):
    run(f'beta={bw} M=Fuchs', M=FUCHS_M, beta_w=bw, **base)
# h convergence at Fuchs mass
r = eval_config(M=FUCHS_M, h=0.15, **base); r['tag'] = 'h=0.15 Fuchs'
rows.append(r); print('h=0.15 worst=', f"{r['worst']:.3e}", flush=True)
json.dump(rows, open('results/stageC2.json', 'w'), indent=1)
print('C2 DONE')
