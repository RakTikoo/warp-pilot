#!/usr/bin/env python3
"""
g56_reads2.py -- Gate-56 reads part 2: the (c) anchor
refinement, the R17 incumbent (screen 1788), claim (d)
(transect re-derivation + screen-cloud recount), and
the two disclosure audits. Merges into
gate56/results/g56_reads.json.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate56/work')
import g56_lib as G  # noqa: E402

OUT = json.load(open(f'{WP}/gate56/results/g56_reads.json'))


def jd(x):
    return json.loads(json.dumps(x, default=lambda o: (
        float(o) if isinstance(o, (np.floating, np.integer))
        else o.tolist() if isinstance(o, np.ndarray)
        else str(o))))


def cfg_of(d):
    return {'muN': float(d['muN']), 'muM': float(d['muM']),
            'K_B': int(d.get('K_B', d.get('K', 17))),
            'vN': d.get('vN'), 'vM': d.get('vM'),
            'K_S': int(d.get('K_S', 9)),
            'vS': d.get('vS_scaled', d.get('vS'))}


conf418 = json.load(open(f'{WP}/phase418/results/p418_confirmation.json'))
state418 = json.load(open(f'{WP}/phase418/results/p418_state.json'))
screens = [json.loads(ln) for ln in
           open(f'{WP}/phase418/results/p418_screens.jsonl')]
by_id = {s['id']: s for s in screens}
J1 = 1.2273852081052888e-06
CRIT = 0.4426742490267404

# ------------------------------------------------ (c) anchor refinement
tw_cfg = cfg_of(conf418['twice_best']['config'])
shell = G.DIRS162 * conf418['twice_best']['nec_argmin_r']
pr = G.profiles_g56(tw_cfg, shell)
T, g = G.T_at_g56(shell, pr)
That = G.eulerian_that_g56(g, T)
m = G.margins_g56(That)
wns = np.array([G.worst_null_exact(That[j])['value']
                for j in range(162)])
stored_wn = conf418['twice_best']['worst_null_at_nec_argmin']
j_star = int(np.argmin(np.abs(wns - stored_wn)))
OUT['c_anchor_refined'] = {
    'identified_dir': j_star,
    'gate_worst_null_there': float(wns[j_star]),
    'stored_worst_null': stored_wn,
    'worst_null_diff': float(wns[j_star] - stored_wn),
    'gate_sampled_nec_there': float(m['nec'][j_star]),
    'stored_joint': conf418['twice_best']['joint'],
    'sampled_nec_diff_there': float(
        m['nec'][j_star] - conf418['twice_best']['joint']),
    'typeI_there': bool(m['typeI'][j_star])}
print('c anchor refined:', jd(OUT['c_anchor_refined']))

# ------------------------------------------------ R17 incumbent (screen 1788)
s1788 = by_id[1788]
rec = G.set_read_g56(cfg_of(s1788))
pt = G.point_read_g56(cfg_of(s1788), rec['nec_argmin_pt'])
OUT['c_r17_incumbent_1788'] = {
    'stored_joint': s1788['joint'], 'tag': s1788['tag'],
    'gate_joint': rec['joint'],
    'joint_diff': rec['joint'] - s1788['joint'],
    'gate_nec_argmin_r': rec['nec_argmin_r'],
    'stored_nec_argmin_r': s1788['nec_argmin_r'],
    'typeI_fraction': rec['typeI_fraction'],
    'worst_null_exact_at_gate_argmin': pt['worst_null']['value'],
    'stored_worst_null': s1788.get('worst_null_at_nec_argmin')}
print('R17 1788: stored', s1788['joint'], 'gate', rec['joint'])

# ------------------------------------------------ (d) transect
trans = state418['transect']
rows = {}
for t, ent in trans.items():
    stat_scr = None
    for s in screens:
        if s['stage'] == 'T' and s['joint'] == ent['static_joint']:
            stat_scr = s
            break
    carr_scr = by_id[ent['carried_best_screen']]
    st = G.set_read_g56(cfg_of(stat_scr))
    ca = G.set_read_g56(cfg_of(carr_scr))
    rows[t] = {
        'muM_stored': ent['base']['muM'],
        'static_screen_id': stat_scr['id'],
        'static_gate': st['joint'],
        'static_stored': ent['static_joint'],
        'static_diff': st['joint'] - ent['static_joint'],
        'carried_screen_id': carr_scr['id'],
        'carried_gate': ca['joint'],
        'carried_stored': ent['carried_best_joint'],
        'carried_diff': ca['joint'] - ent['carried_best_joint'],
        'spend_gate': st['joint'] - ca['joint'],
        'spend_stored': ent['spend'],
        'carried_typeI_fraction': ca['typeI_fraction']}
    print('t', t, 'static diff', rows[t]['static_diff'],
          'carried diff', rows[t]['carried_diff'])
OUT['d_transect'] = rows

# ------------------------------------------------ (d) binning recount
from collections import Counter
stage_counts = Counter(s['stage'] for s in screens)
crit_screens = [s for s in screens
                if s.get('target_peak') == CRIT
                and s.get('peak', 0.0) > 0.0]
feas = [s for s in crit_screens if s.get('feasible')]
bins = {}
for lo, hi in ((3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9),
               (9, 10), (10, 11), (11, 12)):
    sel = [s['joint'] for s in feas if lo <= s['muM'] < hi]
    bins[f'[{lo},{hi})'] = {'n': len(sel),
                            'max': max(sel) if sel else None}
OUT['d_binning'] = {
    'total_screens': len(screens),
    'stage_counts': dict(stage_counts),
    'criterion_screens_with_shape': len(crit_screens),
    'feasible_criterion': len(feas),
    'joint_pos': int(sum(1 for s in feas if s['joint'] > 0)),
    'above_old_bar': int(sum(1 for s in feas
                             if s['joint'] > J1)),
    'bins': bins}
print('binning:', jd(OUT['d_binning']))

# ------------------------------------------------ audit (i): 414 seeds
s414 = [json.loads(ln) for ln in
        open(f'{WP}/phase414/results/p414_screens2.jsonl')]
seed0, seed1 = s414[0], s414[1]
base414 = json.load(open(f'{WP}/phase414/results/p414_base.json'))
b1 = {'muN': base414['muN'], 'muM': base414['muM'], 'K_B': 9,
      'vN': base414['vN'], 'vM': base414['vM'], 'K_S': 9,
      'vS': None}
G50K = [0.40243113547885484, 0.23237610808870765,
        0.10110504581235646, 0.030274386301308052,
        0.021559512630984955, 0.01297222477301449,
        0.007865452045132022, 0.0035285750792539276,
        -0.00043513901545560714]
pk50 = G.peak_g56(G50K, 9)['fine401']['peak']
scaled50 = (np.array(G50K) * (CRIT / pk50)).tolist()
audit_i = {
    'seed0_stored_joint': seed0['joint'],
    'seed1_stored_joint': seed1['joint'],
    'seed0_vS_vs_G50_scaled_maxdiff': float(np.max(np.abs(
        np.array(seed0['vS_scaled']) - np.array(scaled50)))),
    'seed1_vS_vs_seed0_vS_maxdiff': float(np.max(np.abs(
        np.array(seed1['vS_scaled'])
        - np.array(seed0['vS_scaled']))))}
for nm, seed in (('seed0', seed0), ('seed1', seed1)):
    rec = G.set_read_g56(dict(b1, vS=seed['vS_scaled']))
    pt = G.point_read_g56(dict(b1, vS=seed['vS_scaled']),
                          rec['nec_argmin_pt'])
    audit_i[f'{nm}_gate_joint'] = rec['joint']
    audit_i[f'{nm}_gate_joint_diff'] = rec['joint'] \
        - seed['joint']
    audit_i[f'{nm}_gate_worst_null_at_argmin'] = \
        pt['worst_null']['value']
    audit_i[f'{nm}_stored_worst_null'] = seed.get(
        'worst_null_at_nec_argmin')
    print(nm, 'gate joint', rec['joint'], 'stored',
          seed['joint'])
# 418's S-C / S-F screens
sstage = [s for s in screens if s['stage'] == 'S']
audit_i['S_screens'] = {
    s['tag']: {'id': s['id'], 'joint': s['joint']}
    for s in sstage}
for s in sstage:
    if s['tag'] == 'S-C':
        audit_i['SC_vS_vs_414seed0_maxdiff'] = float(
            np.max(np.abs(np.array(s['vS_scaled'])
                          - np.array(seed0['vS_scaled']))))
        audit_i['SC_joint_vs_414seed0'] = \
            s['joint'] - seed0['joint']
    if s['tag'] == 'S-F':
        audit_i['SF_vS_vs_414seed1_maxdiff'] = float(
            np.max(np.abs(np.array(s['vS_scaled'])
                          - np.array(seed1['vS_scaled']))))
        audit_i['SF_joint_vs_414seed1'] = \
            s['joint'] - seed1['joint']
OUT['audit_i_seeds'] = audit_i
print('audit_i:', jd(audit_i))

# ------------------------------------------------ audit (ii): pattern
OUT['audit_ii_pattern'] = {
    'stage_counts_jsonl': dict(stage_counts),
    'stage_counts_state': state418['stage_counts'],
    'total_jsonl': len(screens),
    'state_total_screens_field': state418['total_screens'],
    'cap_total': 2200,
    'G_triggered': state418['G_triggered'],
    'rejects': state418['rejects'],
    'penalised_evals': state418['penalised_evals'],
    'referred_screens': {
        str(i): {'stage': by_id[i]['stage'],
                 'tag': by_id[i]['tag']}
        for i in (1320, 1347, 1648, 1788)}}
print('audit_ii:', jd(OUT['audit_ii_pattern']))

with open(f'{WP}/gate56/results/g56_reads.json', 'w') as fh:
    json.dump(jd(OUT), fh, indent=1)
print('merged into g56_reads.json')
