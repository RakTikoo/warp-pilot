import json, time
import numpy as np
from stageC_opt import eval_config
rows = []
def run(tag, **kw):
    r = eval_config(**kw); r['tag'] = tag; rows.append(r)
    print(tag, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}",
          'typeI=', f"{r['typeI_frac_sig']:.3f}", flush=True)

M = 3.0
for wd in (2.0, 2.5, 3.0, 4.0):
    for fl in (0.05, 0.15):
        run(f'matched wd={wd} fl={fl}', M=M, kind='matched',
            params={'Rs': 15.0, 'wd': wd, 'floor': fl}, sr=2.0, sp=1.16)
for edge in (2.5, 3.5, 4.0):
    run(f'smoothbox edge={edge}', M=M, kind='smoothbox', params={'edge': edge}, sr=2.0, sp=1.16)
for wd in (3.0, 4.0, 5.0):
    run(f'gauss wd={wd}', M=M, kind='gauss', params={'Rs': 15.0, 'wd': wd}, sr=2.0, sp=1.16)
run('matched wd=3 fl=0.05 sr2.5', M=M, kind='matched', params={'Rs': 15.0, 'wd': 3.0, 'floor': 0.05}, sr=2.5, sp=1.45)
run('matched wd=3 fl=0.05 sr1.75', M=M, kind='matched', params={'Rs': 15.0, 'wd': 3.0, 'floor': 0.05}, sr=1.75, sp=1.0)
run('edgepeaked wd=2.5', M=M, kind='edgepeaked', params={'wd': 2.5, 'floor': 0.15}, sr=2.0, sp=1.16)
json.dump(rows, open('results/stageC3.json', 'w'), indent=1)
print('C3 DONE; best:', max(rows, key=lambda d: d['worst'])['tag'])
