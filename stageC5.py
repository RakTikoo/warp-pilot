import json
import numpy as np
from stageC_opt import eval_config
rows = []
def run(tag, **kw):
    r = eval_config(**kw); r['tag'] = tag; rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}", 'wec=', f"{r['wec']:.2e}",
          'sec=', f"{r['sec']:.2e}", 'dec=', f"{r['dec']:.2e}",
          'typeI=', f"{r['typeI_frac_sig']:.3f}", flush=True)

EP = lambda wd, fl: dict(kind='edgepeaked', params={'wd': wd, 'floor': fl})
for M in (2.55, 2.4):
    run(f'M={M} ep wd3.5 fl0.2', M=M, sr=2.0, sp=1.16, **EP(3.5, 0.2))
    run(f'M={M} ep wd3.0 fl0.3', M=M, sr=2.0, sp=1.16, **EP(3.0, 0.3))
    run(f'M={M} ep wd3.0 fl0.2 tanh4', M=M, sr=2.0, sp=1.16, shift_kind='tanh', ws=[15.0, 4.0], **EP(3.0, 0.2))
    run(f'M={M} ep wd3.0 fl0.2 sr2.5', M=M, sr=2.5, sp=1.45, **EP(3.0, 0.2))
    run(f'M={M} ep wd3.0 fl0.2 sp0.9', M=M, sr=2.0, sp=0.9, **EP(3.0, 0.2))
json.dump(rows, open('results/stageC5.json', 'w'), indent=1)
print('C5 DONE')
