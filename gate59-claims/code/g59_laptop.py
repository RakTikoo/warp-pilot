#!/usr/bin/env python
"""g59_laptop.py -- Gate-59 laptop corroboration (NOT a deciding
read). Runs the gate's own implementation (g59_lib) of the
Phase 431 admission object -- Phase 410 Fit A's t = 0 read
against the stored T_req targets -- on the laptop pool.
Prints a JSON record to stdout.
"""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/spark/work/g59root')
import g59_lib as G  # noqa: E402

ROOT = '/home/spark/work/g59root'


def avecs(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


tg = json.load(open(f'{ROOT}/p410_targets.json'))
XS = [np.array(s['point']) for s in tg['sitesA']]
TG = [np.array(s['That']) for s in tg['sitesA']]
fa = json.load(open(f'{ROOT}/p410_fitA_primary.json'))
pv = np.array(fa['pvecs']); av = avecs(fa['avecs'])
mm = np.full(len(pv), float(fa['m']))
Rs_p, _ = G.site_residuals(pv, av, mm, XS, TG, path='pair')
Rs_f, _ = G.site_residuals(pv, av, mm, XS, TG, path='field')
print(json.dumps({
    'object': 'Gate-59 admission corroboration: Fit A t=0 read, '
              'gate lib (g59_lib) on the laptop pool',
    'numpy': np.__version__,
    'Rs_pair': Rs_p, 'maxR_pair': max(Rs_p),
    'Rs_field': Rs_f, 'maxR_field': max(Rs_f)}))
