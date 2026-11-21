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
          'nec=', f"{r['nec']:.2e}", 'typeI=', f"{r['typeI_frac_sig']:.3f}",
          'nsig=', r['n_sig'], flush=True)

EP = dict(kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2}, sr=2.0, sp=1.16)
run('M=2.7 fuchs (control)', M=2.7, **EP)
run('M=1.8 tanh w4 (control-bad)', M=1.8, shift_kind='tanh', ws=[15.0, 4.0], **EP)
for M in (2.7, 2.4, 2.2, 2.0, 1.8, 1.5):
    run(f'M={M} cos[10,20]', M=M, shift_kind='cos', ws=[10.0, 20.0], **EP)
for M in (2.4, 2.0):
    run(f'M={M} quintic[10,20]', M=M, shift_kind='quintic', ws=[10.0, 20.0], **EP)
run('M=2.4 cos beta=0.03', M=2.4, beta_w=0.03, shift_kind='cos', ws=[10.0, 20.0], **EP)
run('M=2.0 cos beta=0.03', M=2.0, beta_w=0.03, shift_kind='cos', ws=[10.0, 20.0], **EP)
json.dump(rows, open('results/stageC8.json', 'w'), indent=1)
print('C8 DONE')
