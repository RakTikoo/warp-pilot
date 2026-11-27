#!/usr/bin/env python3
"""
g56_admission.py -- Gate-56 laptop admission control:
the gate's endpoint read (the screen-1347 SET read +
worst-null at its NEC argmin + dense peak) run from a
minimal mirror. The root is G56_WP (the mirror tree on
whichever machine runs this). Output JSON on stdout.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g56_lib as G  # noqa: E402

WP = os.environ.get('G56_WP', '/home/hatch/workspace/warp-pilot')
conf = json.load(open(f'{WP}/phase418/results/p418_confirmation.json'))
cbj = conf['criterion_best_joint']
cfg = {'muN': cbj['config']['muN'], 'muM': cbj['config']['muM'],
       'K_B': 17, 'vN': cbj['config']['vN'],
       'vM': cbj['config']['vM'], 'K_S': 9,
       'vS': cbj['config']['vS_scaled']}
rec = G.set_read_g56(cfg)
pt = G.point_read_g56(cfg, rec['nec_argmin_pt'])
pk = G.peak_g56(cfg['vS'], cfg['K_S'])
out = {'joint': rec['joint'], 'nec_min': rec['nec_min'],
       'dec_min': rec['dec_min'], 'wec_min': rec['wec_min'],
       'sec_min': rec['sec_min'], 'rho_min': rec['rho_min'],
       'nec_argmin_r': rec['nec_argmin_r'],
       'typeI_fraction': rec['typeI_fraction'],
       'worst_null_exact': pt['worst_null']['value'],
       'peak_dense20001': pk['dense20001']}
print(json.dumps(out, indent=1))
