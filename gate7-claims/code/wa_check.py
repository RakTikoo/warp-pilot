"""
wa_check.py — Gate-7 W-A checker: recomputes the registered
reproduction bars (a)-(e) of GATE7.md from wa_g71_numbers.json
(produced by wa_run_g7.py) and summarises the robustness anatomy
from wa_anatomy.json / wa_tiebreak.json. No new audit numbers.
System python3. Writes results/wa_check.json.
"""
import json

N = json.load(open('/home/hatch/workspace/warp-pilot/gate7/results/wa_g71_numbers.json'))
A = json.load(open('/home/hatch/workspace/warp-pilot/gate7/results/wa_anatomy.json'))
T = json.load(open('/home/hatch/workspace/warp-pilot/gate7/results/wa_tiebreak.json'))

CLAIMED = {  # Phase-50 claimed values, from GATE7.md / p502_memo.md S4
    0.10: {'worst': 1.47e-07, 'core_worst': 2.94e-06, 'core_sampled': 1.75e-06},
    0.09: {'worst': 1.474e-07, 'core_worst': 7.70e-06, 'core_sampled': 6.64e-06},
}
out = {'anchors': {
    'i_minkowski_maxAbsG': N['anchor_i_minkowski_maxAbsG'],
    'i_pass': N['anchor_i_minkowski_maxAbsG'] < 1e-12,
    'ii_max_rho_rel_err': N['anchor_ii_max_rho_rel_err'],
    'ii_max_p_abs_err': N['anchor_ii_max_p_abs_err'],
    'ii_pass': N['anchor_ii_max_rho_rel_err'] <= 3e-3 and N['anchor_ii_max_p_abs_err'] <= 3e-7,
    'iii_typeI': N['anchor_iii_champion_b0.08']['all_sig']['typeI_frac'],
    'iii_worst': N['anchor_iii_champion_b0.08']['all_sig']['worst'],
    'iii_pass': N['anchor_iii_champion_b0.08']['all_sig']['typeI_frac'] == 1.0
                and N['anchor_iii_champion_b0.08']['all_sig']['worst'] > 0}}
for beta, cl in CLAIMED.items():
    s = N[f'deciding_b{beta}']
    a_ = s['all_sig']
    bars = {
        'a_typeI_eq_1': a_['typeI_frac'] == 1.0,
        'b_all_margins_pos': all(a_[k] > 0 for k in ('nec', 'wec', 'sec', 'dec')),
        'c_core_sampled_pos': s['core_sampled_nec_min'] > 0,
        'd_worst_ge_3x_floor': a_['worst'] >= 3 * s['gate_floor'],
        'd_worst_factor3_vs_claim': (1 / 3) <= a_['worst'] / cl['worst'] <= 3,
        'e_core_worst_50pct': 0.5 <= s['core']['worst'] / cl['core_worst'] <= 1.5,
        'e_core_sampled_50pct': 0.5 <= s['core_sampled_nec_min'] / cl['core_sampled'] <= 1.5,
    }
    bars['all_pass'] = all(bars.values())
    out[f'bars_b{beta}'] = {'mine': {'worst': a_['worst'], 'core_worst': s['core']['worst'],
                                    'core_sampled': s['core_sampled_nec_min'],
                                    'gate_floor': s['gate_floor']},
                            'claimed': cl, 'bars': bars}
    print(f"b={beta}: bars {bars}")
out['robustness_summary'] = {
    'b0.10_sig_worst': N['robustness_b0.1']['all_sig']['worst'],
    'b0.10_sig_worst_site': 'DEC at r=10.0 exactly (inside-Spp limit)',
    'b0.10_layer': 'DEC < 0 for 10 < r <~ 10.2 (min -1.33e-05 at r=10.01, -1.12e-05 at 10.02, +8.9e-07 at 10.20)',
    'b0.09_layer': 'DEC < 0 only at r=10.0 (inside limit, -7.54e-07) and r=10.02 (-6.7e-08); positive from r=10.05',
    'tail': 'r>=34.5 margins are nonsignificant-scale (<=3.1e-08) representation-level tail values',
    'FD_corroboration_b0.10_r10.05_worst_pt': T['FD_at_symbolic_worst_r10.05_b0.10']['FD'],
}
print('anchors:', out['anchors'])
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate7/results/wa_check.json', 'w'), indent=1, default=float)
print('CHECK DONE')
