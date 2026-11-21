import json
import numpy as np
from stageC_opt import eval_config
i = np.arange(14)
phi = np.arccos(1 - 2 * (i + 0.5) / 14)
th = np.pi * (1 + 5 ** 0.5) * i
dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)
rad = np.linspace(4.0, 23.0, 39)
PTS2 = np.concatenate([dirs * r for r in rad])
rows = []
def run(tag, **kw):
    r = eval_config(pts=PTS2, **kw); r['tag'] = tag; rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", f"({r['worst_kind']} @r={r['worst_radius']:.1f})",
          'nec=', f"{r['nec']:.2e}", 'typeI=', f"{r['typeI_frac_sig']:.3f}", flush=True)

EP = dict(kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2}, sr=2.0, sp=1.16)
COS = dict(shift_kind='cos', ws=[10.0, 20.0])
for M in (2.0, 5.0, 8.0):
    for b in (0.1, 0.3, 0.5, 0.9, 1.1, 1.5):
        if M == 2.0 and b < 0.3: continue
        if M == 8.0 and b not in (0.5, 0.9): continue
        run(f'SL2 M={M} b={b}', M=M, beta_w=b, **COS, **EP)
json.dump(rows, open('results/stageSL2.json', 'w'), indent=1)
print('SL2 DONE')
