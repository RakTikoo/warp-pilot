#!/usr/bin/env python3
"""
p412_fit.py -- the ladder's own cost law
(registration SS5): spend(P) = M0 - joint at
the criterion (control) and every searched
rung; fit spend = A * P^p over the rungs with
spend > 0 (log-log least squares); report A,
p, the fit's implied zero-crossing peak, and
the measured bracket side by side. Run after
the ladder completes.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/phase412/work')
import p412_lib as L  # noqa: E402

rungs = json.load(open(f'{WP}/phase412/results/p412_rungs.json'))
state = json.load(open(f'{WP}/phase412/results/p412_state.json'))

rows = [{'label': 'criterion (control CTL-412-CRIT)',
         'peak': float(L.CRIT), 'joint': L.G50_JOINT,
         'legal': True}]
for key in sorted(rungs, key=lambda k: rungs[k]['mult']):
    r = rungs[key]
    if r['winner'] is None:
        continue
    rows.append({'label': f"m={r['mult']} (K{r['winner_K']})",
                 'peak': r['target_peak'],
                 'joint': r['winner']['joint'],
                 'legal': r['legal']})
for r in rows:
    r['spend'] = L.M0 - r['joint']

fit_pts = [r for r in rows if r['spend'] > 0]
x = np.log([r['peak'] for r in fit_pts])
y = np.log([r['spend'] for r in fit_pts])
p_exp, logA = np.polyfit(x, y, 1)
A = float(np.exp(logA))
p_exp = float(p_exp)
cross = float((L.M0 / A) ** (1.0 / p_exp)) if A > 0 else None

out = {
    'M0': L.M0,
    'rows': rows,
    'fit_points': [r['label'] for r in fit_pts],
    'fit': {'A': A, 'p': p_exp,
            'implied_zero_crossing_peak': cross,
            'implied_zero_crossing_mult': (cross / L.CRIT
                                           if cross else None)},
    'prior_gate50': {'A': 8.69e-07, 'p': 2.10,
                     'implied_zero_crossing_peak':
                         float((L.M0 / 8.69e-07) ** (1 / 2.10))},
    'ladder_outcome': state.get('ladder_outcome'),
}
with open(f'{WP}/phase412/results/p412_fit.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
