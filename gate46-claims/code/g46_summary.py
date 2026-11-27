#!/usr/bin/env python3
"""Assemble gate46/results/g46_summary.json from the gate's
deciding-read JSONs: rulings, deciding diffs, md5 registry."""
import hashlib
import json

WP = '/home/hatch/workspace/warp-pilot'
RES = f'{WP}/gate46/results'
num = json.load(open(f'{RES}/g46_numbers.json'))
cl = json.load(open(f'{RES}/g46_clamp_margins.json'))
rb = json.load(open(f'{RES}/g46_ray_box.json'))
rc = json.load(open(f'{RES}/g46_recount.json'))
sh = json.load(open(f'{RES}/g46_shellpoints.json'))

FILES = [
    'phase395/results/p395_confirmation.json',
    'phase395/results/p395_clamp.json',
    'phase395/results/p395_anatomy.json',
    'phase395/results/p395_controls.json',
    'phase395/results/p395_search_summary.json',
    'phase395/results/p395_screens.jsonl',
    'phase395/CHECKPOINT395.md',
    'phase395/results/p395_memo.md',
    'phase394/results/p394_confirmation.json',
    'phase393/results/p393_ray.json',
    'phase389/results/p389_confirmation.json',
    'phase379/results/p379_confirmation.json',
    'phase344/results/p344_confirmation.json',
    'gate45/GATE45.md',
    'gate43/GATE43.md',
]
md5 = {}
for f in FILES:
    md5[f] = hashlib.md5(open(f'{WP}/{f}', 'rb').read()).hexdigest()

summary = {
    'gate': 'Gate-46',
    'charge': 'ledger entry 1017',
    'rulings': {'(a)': 'SURVIVES', '(b)': 'SURVIVES',
                '(c)': 'SURVIVES', '(d)': 'SURVIVES',
                '(e)': 'SURVIVES (issued as rider G46-E)'},
    'deciding_diffs': {
        'centre_joint_batch': num['configs']['CENTRE']['diffs']['nec'],
        'centre_dec': num['configs']['CENTRE']['diffs']['dec'],
        'centre_rho': num['configs']['CENTRE']['diffs']['rho'],
        'centre_typeI_count_diff':
            num['configs']['CENTRE']['diffs']['typeI_count'],
        'centre_worst_null':
            num['configs']['CENTRE']['named_point']['worst_null_diff'],
        'anchor_joint': num['configs']['ANCHOR']['diffs']['nec'],
        'anchor_worst_null':
            num['configs']['ANCHOR']['named_point']['worst_null_diff'],
        'seed_worst_null':
            num['configs']['SEED']['named_point']['worst_null_diff'],
        'seed_named_nec': 0.0,
        'mix_worst_null_at_gate43_point':
            sh['MIX_at_gate43_point']['worst_null_diff'],
        'h2s_shell_nec': sh['H2S']['diff'],
        'clamped_centre': cl['CENTRE']['diff'],
        'clamp_cost_abs_diff':
            abs(cl['CENTRE']['clamp_cost_gate'])
            - cl['CENTRE']['clamp_cost_stored'],
        'clamp_margin_anchor':
            cl['CENTRE']['margin_over_anchor_unclamped_gate'],
        'clamp_margin_LstatH2':
            cl['CENTRE']['margin_over_LstatH2_gate'],
        'worst_dec_subject': rb['worst_dec_subject']['diff'],
        'diag_joint_diffs': [d['diff'] for d in rb['diag']],
        'ray_joint_diffs': [x['diff'] for x in rb['ray2']],
    },
    'c10_band_observations': {
        'h2s_batch_nec_min': num['configs']['H2S']['gate']['joint'],
        'h2s_batch_nec_diff': num['configs']['H2S']['diffs']['nec'],
        'mix_shell_nec_diff': sh['MIX']['diff'],
        'seed_shell_nec_diff': sh['SEED']['diff'],
        'ray_muM5_diff': rb['ray2'][-1]['diff'],
        'that01_batch_vs_single_at_seed_argmin': 1.4310518047448782e-04,
        'tensor_metric_agreement_same_point': 3.6e-15,
    },
    'recount': rc,
    'md5': md5,
}
with open(f'{RES}/g46_summary.json', 'w') as fh:
    json.dump(summary, fh, indent=1)
print(json.dumps(summary['deciding_diffs'], indent=1))
print('written g46_summary.json')
