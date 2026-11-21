import json
import numpy as np
from stageC_opt import eval_config
rows = []
def run(tag, **kw):
    r = eval_config(**kw); r['tag'] = tag; rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}",
          'typeI=', f"{r['typeI_frac_sig']:.3f}", 'rho_pk=', f"{r['rho_peak']:.3e}", flush=True)

EP = dict(kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2}, sr=2.0, sp=1.16)
for M in (2.4, 2.2, 2.0, 1.8):
    for w in (5.0, 6.0):
        run(f'M={M} tanh w={w}', M=M, shift_kind='tanh', ws=[15.0, w], **EP)
run('M=2.2 tanh w=4', M=2.2, shift_kind='tanh', ws=[15.0, 4.0], **EP)
run('M=2.0 tanh w=4', M=2.0, shift_kind='tanh', ws=[15.0, 4.0], **EP)
run('M=2.4 tanh w=4 beta=0.03', M=2.4, beta_w=0.03, shift_kind='tanh', ws=[15.0, 4.0], **EP)
run('M=2.7 tanh w=5 beta=0.03', M=2.7, beta_w=0.03, shift_kind='tanh', ws=[15.0, 5.0], **EP)
json.dump(rows, open('results/stageC6.json', 'w'), indent=1)
print('C6 DONE')
