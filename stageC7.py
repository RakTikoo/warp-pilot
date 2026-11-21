import json
import numpy as np
from stageC_opt import eval_config

# extended sample: radii 4..23 step 0.5, 14 dirs
i = np.arange(14)
phi = np.arccos(1 - 2 * (i + 0.5) / 14)
th = np.pi * (1 + 5 ** 0.5) * i
dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)
rad = np.linspace(4.0, 23.0, 39)
PTS2 = np.concatenate([dirs * r for r in rad])

rows = []
def run(tag, **kw):
    r = eval_config(pts=PTS2, **kw); r['tag'] = tag; rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}",
          'typeI=', f"{r['typeI_frac_sig']:.3f}", flush=True)

EP = dict(kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2}, sr=2.0, sp=1.16)
for M in (1.5, 1.2, 1.0, 0.7):
    run(f'M={M} tanh w4 b0.02', M=M, shift_kind='tanh', ws=[15.0, 4.0], **EP)
for b in (0.04, 0.05, 0.07, 0.1):
    run(f'M=1.8 tanh w4 b={b}', M=1.8, beta_w=b, shift_kind='tanh', ws=[15.0, 4.0], **EP)
run('M=1.5 tanh w4 b=0.03', M=1.5, beta_w=0.03, shift_kind='tanh', ws=[15.0, 4.0], **EP)
json.dump(rows, open('results/stageC7.json', 'w'), indent=1)
print('C7 DONE')
