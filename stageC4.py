import json, time
import numpy as np
from stageC_opt import eval_config
rows = []
def run(tag, **kw):
    r = eval_config(**kw); r['tag'] = tag; rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}",
          'typeI=', f"{r['typeI_frac_sig']:.3f}", 'rho_pk=', f"{r['rho_peak']:.2e}", flush=True)

for M in (2.7, 2.4):
    for wd in (2.0, 2.5, 3.0):
        for fl in (0.15, 0.2):
            run(f'M={M} ep wd={wd} fl={fl}', M=M, kind='edgepeaked',
                params={'wd': wd, 'floor': fl}, sr=2.0, sp=1.16)
json.dump(rows, open('results/stageC4.json', 'w'), indent=1)
ok = [r for r in rows if r['worst'] > 0]
print('C4 DONE; passing:', [(r['tag'], round(r['worst'], 8)) for r in ok])
