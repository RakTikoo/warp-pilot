#!/usr/bin/env python3
"""
g52_admit.py -- Gate-52 laptop admission control. Runs the
gate's own machinery (Cartan tetrad organisation) on the
pool laptop: the static base and the m2 winner SET-244
reads + certified worst-nulls at the argmin points.
Admission is judged against the VM reads in
gate52/results/g52_numbers.json. Deciding reads remain
the VM reads regardless of the outcome.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g52_lib as G   # noqa: E402

out = {}
for tag, vs, K in (('BASE', None, 9), ('M2', G.M2_VS, 9)):
    s, R = G.set_read(vs, K)
    wn = G.worst_null_certified(
        G.that_at(vs, K,
                  np.array(s['nec_argmin_point'])[None, :])[0])
    out[tag] = {
        'joint': s['joint'], 'nec': s['nec']['min'],
        'dec': s['dec']['min'], 'wec': s['wec']['min'],
        'sec': s['sec']['min'], 'rho': s['rho']['min'],
        'typeI_fraction': s['typeI_fraction'],
        'nec_argmin_r': s['nec_argmin_r'],
        'worst_null': wn['worst_null'],
        'worst_null_certified': wn['certified'],
        'worst_null_kkt_residual': wn['kkt_residual'],
    }
    print(tag, 'joint', s['joint'], 'worst_null',
          wn['worst_null'], flush=True)
WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
with open(f'{WP}/gate52/results/g52_admission_laptop.json',
          'w') as f:
    json.dump(out, f, indent=1)
print('wrote admission record')
