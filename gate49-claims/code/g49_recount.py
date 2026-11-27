#!/usr/bin/env python3
"""
g49_recount.py -- Gate-49 recount of Phase 403's
stored search record (bookkeeping on stored bytes),
the gain-decomposition arithmetic, the box-edge
arithmetic, the SS7 construction facts, and an
independent gate-machinery re-read of the stored
worst-DEC screen. Writes gate49/results/g49_recount.json.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g49_lib as G  # noqa: E402

WP = G.WP
OUT = os.path.join(WP, 'gate49', 'results', 'g49_recount.json')
res = {}

rows = []
with open(os.path.join(WP, 'phase403', 'results',
                       'p403_screens.jsonl')) as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))
res['n_rows'] = len(rows)
res['n_feasible'] = int(sum(1 for r in rows if r['feasible']))
res['n_floors_ok'] = int(sum(1 for r in rows if r['floors_ok']))
res['n_dec_saturated'] = int(sum(1 for r in rows
                                 if r['dec_min'] < -0.9999))
worst_dec_row = min(rows, key=lambda r: r['dec_min'])
res['worst_dec'] = {'value': worst_dec_row['dec_min'],
                    'triple': worst_dec_row['triple'],
                    'stage': worst_dec_row['stage'],
                    'stored_claim': -4.32733270543391e-07,
                    'diff': worst_dec_row['dec_min']
                    - (-4.32733270543391e-07)}
HOME_JOINT = -2.9809850277749006e-05
SEED_JOINT = -9.38489875115556e-06
res['n_beat_home'] = int(sum(1 for r in rows
                             if r['joint'] > HOME_JOINT))
res['n_beat_seed'] = int(sum(1 for r in rows
                             if r['joint'] > SEED_JOINT))
win_rows = [r for r in rows
            if r['triple'] == list(G.WINNER)]
res['winner_rows'] = len(win_rows)
if win_rows:
    res['winner_row'] = win_rows[0]
best = max(rows, key=lambda r: r['joint'])
res['best_row_joint'] = best['joint']
res['best_row_triple'] = best['triple']
res['stages'] = sorted(set(r['stage'] for r in rows))
res['stage_counts'] = {s: int(sum(1 for r in rows
                                 if r['stage'] == s))
                       for s in res['stages']}

# SS7 construction facts from the stored record
at_edge = [r for r in rows if r['triple'][0] == 0.5]
res['ss7_construction'] = {
    'n_screens_at_muS_edge_0.5': len(at_edge),
    'peak_values_at_edge': sorted(set(r['peak_abs_beta_S']
                                      for r in at_edge)),
    'bar': G.DEGEN_BAR,
    'best_joint_at_muS_edge': max((r['joint'] for r in at_edge),
                                  default=None),
    'winner_muS': G.WINNER[0],
    'winner_peak_stored': 0.44268227409480604,
    'winner_clearance': 0.44268227409480604 - G.DEGEN_BAR,
    'corner_row_G3': [r for r in rows
                      if r['stage'] == 'G3'
                      and abs(r['triple'][0] - 0.5) < 1e-12
                      and abs(r['triple'][1] - 1.90) < 1e-9][:1],
}

# gain decomposition arithmetic (stored values)
dec = {'C395_home_joint': HOME_JOINT,
       'transport_only_joint': SEED_JOINT,
       'reoptimised_joint': -3.676111526923747e-06}
dec['transport_gain'] = dec['transport_only_joint'] \
    - dec['C395_home_joint']
dec['reoptimisation_increment'] = dec['reoptimised_joint'] \
    - dec['transport_only_joint']
dec['total_gain'] = dec['reoptimised_joint'] - dec['C395_home_joint']
dec['stored'] = {'transport_gain': 2.0424951526593445e-05,
                 'reoptimisation_increment': 5.708787224231813e-06,
                 'total_gain': 2.613373875082526e-05}
dec['diffs'] = {k: dec[k] - dec['stored'][k]
                for k in dec['stored']}
res['decomposition'] = dec

# box-edge arithmetic (claim (d))
res['box_edges'] = {
    'muS_to_lo': G.WINNER[0] - 0.50,
    'muN_to_hi': 1.90 - G.WINNER[1],
    'muM_to_lo': G.WINNER[2] - 1.60,
    'muM_to_hi': 6.50 - G.WINNER[2],
    'stored': {'muS_to_lo': 9.06430415059667e-06,
               'muN_to_hi': 1.9269157599310915e-05}}

# independent re-read of the worst-DEC screen's triple
tri = tuple(worst_dec_row['triple'])
out, aux = G.set_read(tri, G.POSE_W28, h=0.02)
i_dec = int(np.argmin(aux['R']['dec']))
res['worst_dec_reread'] = {
    'triple': list(tri),
    'gate_dec_min': out['dec']['min'],
    'stored_dec_min': worst_dec_row['dec_min'],
    'diff': out['dec']['min'] - worst_dec_row['dec_min'],
    'gate_dec_argmin_typeI': bool(aux['R']['typeI'][i_dec]),
    'gate_joint': out['joint'],
    'stored_joint': worst_dec_row['joint'],
    'joint_diff': out['joint'] - worst_dec_row['joint'],
    'gate_typeI_count': out['typeI_count'],
    'stored_typeI_count': worst_dec_row['typeI_count']}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print(json.dumps({k: res[k] for k in
                  ('n_rows', 'n_feasible', 'n_dec_saturated',
                   'worst_dec', 'n_beat_home', 'n_beat_seed',
                   'winner_rows', 'best_row_joint')}, indent=1))
print('worst-DEC reread:', json.dumps(res['worst_dec_reread'],
                                      indent=1))
