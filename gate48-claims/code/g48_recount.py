#!/usr/bin/env python3
"""
g48_recount.py -- Gate-48's recount of Phase 400's search
record (claim (c)), independent re-reads of the four
non-final stage bests through g48_lib, the penalty
arithmetic audit (claim (d): every stored screen's
penalty fields recomputed from its own vectors), and
the stakes recomputation (claim (e)) on both the stored
margin and the gate's confirmed margin.
Writes gate48/results/g48_recount.json.
"""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate48/work')
import g48_lib as L  # noqa: E402

OUT = '/home/hatch/workspace/warp-pilot/gate48/results/g48_recount.json'
LAM_REG = 0.01            # p338_lib LAM_REG (programme record)
LAM400 = 1.0e-5           # Phase 400 registration SS4


def rough(v):
    v = np.asarray(v, dtype=np.float64)
    if len(v) < 3:
        return 0.0
    d2 = v[:-2] - 2.0 * v[1:-1] + v[2:]
    return float(np.sum(d2 ** 2))


# ------------------------------------------------ recount
recs = [json.loads(line) for line in
        open(f'{L.WP}/phase400/results/p400_screens.jsonl')]
stages = {}
for rec in recs:
    stages.setdefault(rec['tag'].split('_')[0], []).append(rec)
counts = {k: len(v) for k, v in stages.items()}
bests = {}
for k, v in stages.items():
    b = max(v, key=lambda rec: rec['pure_min'])
    bests[k] = {'tag': b['tag'], 'pure_min': b['pure_min'],
                'nec_min': b['nec_min'], 'K': b['K'],
                'muN': b['muN'], 'muM': b['muM']}
# Stage A crossing: running incumbent in file order
a_recs = stages['A']
run = -np.inf
cross_idx = None
at200 = None
for i, rec in enumerate(a_recs):
    run = max(run, rec['pure_min'])
    if cross_idx is None and rec['pure_min'] > 0.0:
        cross_idx = {'a_index_1based': i + 1, 'tag': rec['tag'],
                     'pure_min': rec['pure_min']}
    if i + 1 == 200:
        at200 = {'running_incumbent_at_200': run}
state = json.load(open(f'{L.WP}/phase400/results/p400_state.json'))

# --------------------------------------- penalty audit (d)
max_pen_diff = 0.0
max_pen341_diff = 0.0
for rec in recs:
    tot = rough(rec['vN']) + rough(rec['vM'])
    max_pen_diff = max(max_pen_diff,
                       abs(LAM400 * tot - rec['penalty']))
    max_pen341_diff = max(max_pen341_diff,
                          abs(LAM_REG * tot - rec['pen341']))
anchor_vN = [0.0] * 6 + [-0.02] + [0.0] * 2
pen = {'lam_reg': LAM_REG, 'lam400': LAM400,
       'lam_ratio': LAM400 / LAM_REG,
       'lam_ratio_is_1e-3_exactly': bool(LAM400 == LAM_REG * 1e-3),
       'rough_anchor_vN': rough(anchor_vN),
       'pen341_anchor': LAM_REG * rough(anchor_vN),
       'pen400_anchor': LAM400 * rough(anchor_vN),
       'pen341_anchor_stored': 2.4000000000000004e-05,
       'pen400_anchor_stored': 2.4000000000000003e-08,
       'max_screen_penalty_diff_all_981': max_pen_diff,
       'max_screen_pen341_diff_all_981': max_pen341_diff}

# --------------------------------- stage-best re-reads (c)
rereads = {}
for k in ('A', 'B', 'C', 'D'):
    b = max(stages[k], key=lambda rec: rec['pure_min'])
    out, _ = L.set_read(0.0, b['muN'], b['muM'],
                        np.array(b['vN']), np.array(b['vM']),
                        b['K'])
    rereads[k] = {'tag': b['tag'], 'stored_pure': b['pure_min'],
                  'gate_joint': out['joint_min_nec_dec'],
                  'gate_nec': out['nec_min'],
                  'diff': float(out['joint_min_nec_dec']
                                - b['pure_min']),
                  'typeI_count': out['typeI_count'],
                  'argmin_r': out['nec_argmin_r']}
    print('stage', k, b['tag'], 'stored', b['pure_min'],
          'gate', out['joint_min_nec_dec'], flush=True)

# ------------------------------------------------ stakes (e)
stakes_st = json.load(open(f'{L.WP}/phase400/results/'
                           'p400_stakes.json'))
numbers = json.load(open(f'{L.WP}/gate48/results/g48_numbers.json'))
m_gate = numbers['winner']['gate']['nec']
m_stored = stakes_st['L_new']
stakes = {}
for tr in ('A', 'B'):
    Ac = stakes_st['per_trace'][tr]['A_c']
    p = stakes_st['per_trace'][tr]['p']
    stakes[tr] = {
        'A_c': Ac, 'p': p,
        'muS_star_stored_m': float((m_stored / Ac) ** (1.0 / p)),
        'muS_star_gate_m': float((m_gate / Ac) ** (1.0 / p)),
        'muS_star_stored_record':
            stakes_st['per_trace'][tr]['break_even_muS'],
        'm_req': float(Ac * 0.5 ** p),
        'shortfall_stored_m': float(Ac * 0.5 ** p - m_stored),
        'shortfall_gate_m': float(Ac * 0.5 ** p - m_gate)}
    print('stakes', tr, stakes[tr]['muS_star_gate_m'], flush=True)

res = {'n_screens': len(recs), 'stage_counts': counts,
       'stage_bests': bests, 'stage_A_crossing': cross_idx,
       'stage_A_at_200': at200,
       'state_n_evals': state['n_evals'],
       'state_cap_reached': state['cap_reached'],
       'state_incumbent': {'tag': state['incumbent']['tag'],
                           'pure_min':
                               state['incumbent']['pure_min']},
       'all_screens_have_vectors': bool(all(
           'vN' in r and 'vM' in r and 'penalty' in r
           and 'pen341' in r for r in recs)),
       'penalty_audit': pen, 'stage_best_rereads': rereads,
       'stakes': stakes}
with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print('counts', counts, 'crossing', cross_idx, 'at200', at200)
print('WROTE', OUT)
