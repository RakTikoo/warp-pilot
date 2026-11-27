#!/usr/bin/env python3
"""
g52_arith.py -- Gate-52 verification of claims (c) and (d)
and of the Phase 412 record's internal arithmetic, from
the stored records (extracted inputs). Pure arithmetic:
no tensor reads. Output: gate52/results/g52_arith.json.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g52_lib as G   # noqa: E402

WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
OUT = f'{WP}/gate52/results/g52_arith.json'
INP = G.INP
out = {}

M0 = 1.3977194851281464e-06
fit = INP['fit412']
rows = fit['rows']

# ---- spends recomputed from M0 and the stored joints
sp = {}
for row in rows:
    sp[row['label']] = M0 - row['joint']
out['spends'] = {
    'recomputed': sp,
    'stored': {row['label']: row['spend'] for row in rows},
    'diffs': {row['label']: sp[row['label']] - row['spend']
              for row in rows},
    'M0': M0,
}
P = {row['label']: row['peak'] for row in rows}
lab = [row['label'] for row in rows]
crit, m2, m5 = lab[0], lab[1], lab[2]

# ---- local exponents
def local_exp(l1, l2):
    return float(np.log(sp[l2] / sp[l1])
                 / np.log(P[l2] / P[l1]))

out['local_exponents'] = {
    'crit_to_2x': local_exp(crit, m2),
    '2x_to_5x': local_exp(m2, m5),
    'gate50_winner_exponent_stored': 2.097,
    'gate50_law_p': 2.10,
}
# Gate-50's own winner spends (its §2(c) table) -> the
# exponent of the law the ladder tests:
g50_spends = {0.05: 1.761e-09, 0.25: 5.147e-08,
              0.4426742490267404: 1.7033427702199027e-07}
out['gate50_law_check'] = {
    'exp_0.05_to_crit': float(
        np.log(g50_spends[0.4426742490267404] / g50_spends[0.05])
        / np.log(0.4426742490267404 / 0.05)),
    'exp_0.25_to_crit': float(
        np.log(g50_spends[0.4426742490267404] / g50_spends[0.25])
        / np.log(0.4426742490267404 / 0.25)),
    'coef_at_crit': float(g50_spends[0.4426742490267404]
                          / 0.4426742490267404 ** 2),
}

# ---- the registered 3-point fit, refit from the spends
lp = np.log([P[l] for l in lab])
ls = np.log([sp[l] for l in lab])
p_fit, lnA = np.polyfit(lp, ls, 1)
A_fit = float(np.exp(lnA))
cross = float((M0 / A_fit) ** (1.0 / p_fit))
out['refit'] = {
    'A': A_fit, 'p': float(p_fit),
    'implied_zero_crossing_peak': cross,
    'stored_A': fit['fit']['A'], 'stored_p': fit['fit']['p'],
    'stored_crossing': fit['fit']['implied_zero_crossing_peak'],
    'A_diff': A_fit - fit['fit']['A'],
    'p_diff': float(p_fit) - fit['fit']['p'],
    'crossing_diff': cross - fit['fit']['implied_zero_crossing_peak'],
    'crossing_below_legal_rung': bool(cross < P[m2]),
    'legal_rung_peak': P[m2],
}

# ---- claim (d): the million-c gap, both exponent anchors
P_STAR = P[m2]
spend_fit_1e6 = A_fit * 1.0e6 ** float(p_fit)
ratio_fit = spend_fit_1e6 / M0
p_loc = out['local_exponents']['2x_to_5x']
spend_loc_1e6 = sp[m5] * (1.0e6 / P[m5]) ** p_loc
ratio_loc = spend_loc_1e6 / M0
out['million_c_gap'] = {
    'peak_orders_above_Pstar': float(np.log10(1.0e6 / P_STAR)),
    'fit_law': {'spend_at_1e6': float(spend_fit_1e6),
                'ratio_to_margin': float(ratio_fit),
                'orders_short': float(np.log10(ratio_fit))},
    'local_exponent_law': {'p_local': p_loc,
                           'spend_at_1e6': float(spend_loc_1e6),
                           'ratio_to_margin': float(ratio_loc),
                           'orders_short':
                           float(np.log10(ratio_loc))},
    'gate50_naive_law': {
        'spend_at_1e6': float(8.69e-07 * 1.0e6 ** 2.10),
        'orders_short': float(np.log10(
            8.69e-07 * 1.0e6 ** 2.10 / M0))},
}

# ---- peak-float provenance (claim (a) ruling inputs)
out['peak_floats'] = {
    'H2_peak_stored': G.H2_PEAK_STORED,
    'half_exact': bool(0.5 * G.H2_PEAK_STORED == G.SS7_BAR),
    'double_exact': bool(2.0 * G.SS7_BAR == G.H2_PEAK_STORED),
    'rung_target': float(INP['rungs412']['m2']['target_peak']),
    'target_equals_H2_peak': bool(
        float(INP['rungs412']['m2']['target_peak'])
        == G.H2_PEAK_STORED),
}

# ---- screens audit (claim (b) record support)
scr = INP['screens412']
stages = {}
for d in scr.values():
    stages.setdefault(d['stage'], []).append(d)
aud = {}
for stg, ds in stages.items():
    aud[stg] = {
        'n': len(ds),
        'max_joint': max(d['joint'] for d in ds),
        'max_joint_id': max(ds, key=lambda d: d['joint'])['id'],
        'incumbent_joint': max(
            (d for d in ds if d['tag'] == 'incumbent'),
            key=lambda d: d['joint'], default=None),
        'all_feasible': all(d['feasible'] for d in ds),
        'any_rejected': any(d['feasible'] is False for d in ds),
    }
    inc = [d for d in ds if d['tag'] == 'incumbent']
    aud[stg]['incumbent_joint'] = (
        inc[-1]['joint'] if inc else None)
    aud[stg]['incumbent_id'] = (inc[-1]['id'] if inc else None)
out['screens_audit'] = aud
out['n_screens_total'] = len(scr)
# seeds at R5 (first three screens of the stage, tag 'seed')
r5 = sorted(stages['R5'], key=lambda d: d['id'])
out['r5_seeds'] = [{'id': d['id'], 'joint': d['joint']}
                   for d in r5[:3]]
# K9/K17 incumbent agreement (stored pair)
j9 = INP['screens412']['523']['joint']
j17 = INP['rungs412']['m5']['K17']['incumbent_joint']
out['m5_pair'] = {
    'K9_incumbent_joint': j9, 'K17_incumbent_joint': j17,
    'abs_agreement': float(abs(j9 - j17)),
    'margins_below_zero_K17': float(abs(j17) / M0),
    'best_pure_joint_screens': {
        'K9': INP['rungs412']['m5']['K9']['best_joint_screen'],
        'K17': INP['rungs412']['m5']['K17']['best_joint_screen']},
}
# rung legality sign agreement: incumbent vs best pure joint
out['rung_sign_agreement'] = {
    'm2': bool(np.sign(INP['rungs412']['m2']['K9']
                       ['incumbent_joint'])
               == np.sign(INP['rungs412']['m2']['K9']
                          ['best_joint_screen'])),
    'm5_K9': bool(np.sign(j9) == np.sign(
        INP['rungs412']['m5']['K9']['best_joint_screen'])),
    'm5_K17': bool(np.sign(j17) == np.sign(
        INP['rungs412']['m5']['K17']['best_joint_screen'])),
}

with open(OUT, 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
