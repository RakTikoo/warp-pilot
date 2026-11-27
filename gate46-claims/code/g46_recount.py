#!/usr/bin/env python3
"""
g46_recount.py -- Gate-46 recount of Phase 395's stored box
record (claim (d), stored-record half). Reads
phase395/results/p395_screens.jsonl directly; no tensor
machinery involved.
"""
import json
import os

WP = '/home/hatch/workspace/warp-pilot'
ANCHOR_JOINT = -6.812652656191736e-05

rows = [json.loads(ln) for ln in
        open(f'{WP}/phase395/results/p395_screens.jsonl')
        if ln.strip()]
n = len(rows)
feas = [r for r in rows if r['feasible']]
beat = [r for r in rows if r['joint'] > ANCHOR_JOINT]
worst_dec = min(rows, key=lambda r: r['dec_min'])
sat_05 = [r for r in rows if r['dec_min'] < -0.5]
sat_9999 = [r for r in rows if r['dec_min'] < -0.9999]
stages = {}
for r in rows:
    stages[r['stage']] = stages.get(r['stage'], 0) + 1

out = {
    'n_reads': n,
    'n_feasible': len(feas),
    'n_beat_anchor': len(beat),
    'anchor_joint': ANCHOR_JOINT,
    'worst_dec': {'triple': worst_dec['triple'],
                  'stage': worst_dec['stage'],
                  'dec_min': worst_dec['dec_min'],
                  'joint': worst_dec['joint'],
                  'nec_min': worst_dec['nec_min'],
                  'dec_argmin_r': worst_dec['dec_argmin_r'],
                  'typeI_fraction': worst_dec['typeI_fraction']},
    'n_dec_saturated_below_-0.5': len(sat_05),
    'n_dec_saturated_below_-0.9999': len(sat_9999),
    'stage_counts': stages,
    'best': max(rows, key=lambda r: r['joint'])['triple'],
    'best_joint': max(r['joint'] for r in rows),
}
os.makedirs(f'{WP}/gate46/results', exist_ok=True)
with open(f'{WP}/gate46/results/g46_recount.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
