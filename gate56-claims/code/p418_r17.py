#!/usr/bin/env python3
"""
p418_r17.py -- Phase 418 supplement, run after
the main driver: (1) the K_S = 17 gate arm at
2x the criterion on the winning base (the
registered Stage-R gate; in the main run the
K_S = 9 pattern consumed the full 300-screen
Stage-R cap before the gate block was reached,
so the gate is run here as stage 'R17' with
its own 200-screen allowance -- the phase
total stays under the registered 2200 total
cap; disclosed in the memo); (2) the SS6
confirmation of screen 1347's configuration,
the criterion search's pure-joint maximum
(stated alongside the score-incumbent per
registration SS4).
"""
import json
import os
import sys

import numpy as np

WP = os.environ.get('P418_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/phase418/work')

import p418_lib as L  # noqa: E402
import p418_search as S  # noqa: E402

S.STAGE_CAPS['R17'] = 200
P2 = 2.0 * L.CRIT

conf = json.load(open(f'{WP}/phase418/results/'
                      'p418_confirmation.json'))
win_cfg = conf['criterion_best']['config']
base = S.base_of(win_cfg)

rows = [json.loads(l) for l in
        open(f'{WP}/phase418/results/p418_screens.jsonl')]
r_rows = [r for r in rows if r['stage'] == 'R']
incR = max((r for r in r_rows if r['feasible']),
           key=lambda r: r['score'])
print('R K9 incumbent: screen', incR['id'], 'joint',
      incR['joint'])

# ---- (1) the K_S = 17 gate at 2x (412's form)
v17a = L.shape_at_knots(incR['vS_scaled'], 9, 17)
v17b = L.shape_at_knots(L.G50_KNOTS, 9, 17)
try:
    S.screen('R17', base, v17a, 17, P2, tag='k17-warm-inc')
    S.screen('R17', base, v17b, 17, P2, tag='k17-warm-g50')
    S.cd_shape('R17', base, v17a, 17, P2)
    inc = S.incumbent('R17', P2)
    if inc is not None:
        S.nm_shape('R17', base, inc['config']['vS_scaled'],
                   17, P2)
except S.CapHit:
    pass
inc17 = S.incumbent('R17', P2)
print('R17 incumbent:', None if inc17 is None else
      (inc17['screen_id'], inc17['joint'], inc17['score']))
S.save_state()

# confirm the 2x best across R + R17 if the gate
# arm beat the K9 incumbent
best2 = incR
if inc17 is not None and inc17['joint'] > incR['joint']:
    best2 = inc17
    out = S.confirm_point(inc17['config'], 'twice_best',
                          do_polish=bool(inc17['joint'] >= 0.0))
    print('CONFR17 joint', out['joint'])
else:
    print('K17 gate did not beat the K9 2x incumbent;',
          'twice_best stands (screen %d)' % incR['id'])

# ---- (2) confirm the criterion pure-joint maximum
rows = [json.loads(l) for l in
        open(f'{WP}/phase418/results/p418_screens.jsonl')]
crit = [r for r in rows if r['feasible']
        and abs(r['target_peak'] - L.CRIT) < 1e-12]
pj = max(crit, key=lambda r: r['joint'])
print('criterion pure-joint max: screen', pj['id'],
      'stage', pj['stage'], 'joint', pj['joint'],
      'score', pj['score'])
out = S.confirm_point(S.cfg_from_screen(pj),
                      'criterion_best_joint', do_polish=True)
print('CONFIRM pure-joint max joint', out['joint'],
      'diff vs screen', out['joint'] - pj['joint'])
print('total screens now', S.n_screens())
