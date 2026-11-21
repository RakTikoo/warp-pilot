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
for M in (1.6, 1.7):
    run(f'M={M} cos b0.02', M=M, **COS, **EP)
for b in (0.04, 0.05, 0.07):
    run(f'M=2.4 cos b={b}', M=2.4, beta_w=b, **COS, **EP)
run('M=3.334 cos b=0.05', M=3.334274, beta_w=0.05, **COS, **EP)
run('M=3.334 cos b=0.1', M=3.334274, beta_w=0.1, **COS, **EP)
json.dump(rows, open('results/stageC9.json', 'w'), indent=1)
print('C9 DONE')
