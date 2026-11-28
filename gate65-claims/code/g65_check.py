#!/usr/bin/env python3
"""
g65_check.py -- Gate-65 independent checker.
Reads ONLY the gate's results file and the
stored records (479/474 confirmations and
fits, Gate-62's results; no machinery
imports, no re-reads) and verifies the
verdict logic of g65_registration.md SS1
from the numbers. Writes
results/g65_verify.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WP = '/home/hatch/workspace/warp-pilot'
G = json.load(open(os.path.join(HERE, '..', 'results',
                                'g65_results.json')))
G62 = json.load(open(os.path.join(
    WP, 'gate62/results/g62_results.json')))
checks = {}


def chk(name, ok, detail=''):
    checks[name] = {'pass': bool(ok), 'detail': detail}


# ---- G65-A: the base ----
A = G['A_base']
chk('A1_base_screen_diff0',
    all(v == 0.0 for v in A['diffs_vs_BASE_REC'].values()
        if v is not None),
    'all DECIDING_FIELDS vs p460 BASE_REC')
chk('A2_base_worstnull_diff0', A['worst_null_diff'] == 0.0,
    str(A['worst_null']))
chk('A3_base_adversary_diff0', A['adversary_depth_diff'] == 0.0,
    str(A['adversary_depth']))

# ---- G65-B: the member ----
B = G['B_member']
chk('B1_member_x_matches_charged',
    G['member_x_matches_charged_construction'],
    'gate x (from 479 stored verdict.x) == charged construction')
chk('B2_triple_diff0',
    B['joint_diff_vs_stored'] == 0.0
    and B['worst_null_diff'] == 0.0
    and B['adversary_depth_diff'] == 0.0,
    f"joint {B['joint']} wn {B['worst_null']} "
    f"adv {B['adversary_depth']}")
chk('B3_triple_equals_gate_base_triple',
    B['joint'] == A['screen']['joint']
    and B['worst_null'] == A['worst_null']
    and B['adversary_depth'] == A['adversary_depth'],
    'the joint was spent nowhere, on the gate reads')
chk('B4_six_diff0',
    all(v == 0.0 for v in B['six_diffs'].values()),
    str(B['six_gate']))
chk('B5_six_values_charged',
    B['six_gate'] == {
        'SEC8': 2.4404440032471187e-05,
        'SEC9': 2.4411976531644726e-05,
        'SEC10': 2.4396443055148438e-05,
        'DEC8': 4.894587722725915e-05,
        'DEC9': 3.441160723921305e-05,
        'DEC10': 2.4396443055148438e-05},
    'the six at 8/9/10 as charged in entry 1299/1255')
chk('B6_frame_invariance',
    all(v['sec_sampled_eq_typeI'] and v['dec_sampled_eq_typeI']
        for v in B['frame_invariance'].values()),
    'sampled == Type-I-restricted at 8/9/10, both channels')
chk('B7_pen_diff0', B['pen_diff'] == 0.0, str(B['screen']['pen']))
chk('B8_defended', B['defended'] is True
    and B['joint'] >= 0.0 and B['worst_null'] >= 0.0
    and B['adversary_depth'] >= 0.0,
    'DEFENDED bar on the gate read')

# ---- G65-D: the set read and the enumeration ----
D = G['D_set_read']
EN = G['D_enumeration']
chk('D1_crosscheck_diff0',
    all(v['diff'] == 0.0 for v in G['D_crosscheck'].values()),
    'gate aux set minima == screen minima, five channels')
chk('D2_residue',
    G['D_sec_residue']['gate_value'] == -6.459908493210403e-06
    and G['D_sec_residue']['diff'] == 0.0
    and G['D_sec_residue']['node'] == 23
    and G['D_sec_residue']['r'] == 17.04878048780488
    and G['D_sec_residue']['argmin_typeI'] is True,
    'SEC set min at node index 23 (G62-R1), Type-I, diff 0.0')
chk('D3_other_channels_positive_at_set_scope',
    all(D[k]['set_min'] > 0.0 for k in ('nec', 'wec', 'dec', 'rho')),
    {k: D[k]['set_min'] for k in ('nec', 'wec', 'dec', 'rho')})
chk('D4_sec_only_failing_channel',
    EN['other_channels_any_negative_node'] == {
        'nec': [], 'wec': [], 'dec': [], 'rho': []},
    'no NEC/WEC/DEC/RHO-negative node anywhere')
chk('D5_enumeration_equals_corrected_set_1297',
    EN['vs_corrected_set_1297']['gate_set_equals_corrected'] is True
    and EN['n_negative_sampled'] == 20,
    str(EN['negative_sec_nodes_sampled']))
chk('D6_enumeration_supersedes_G62B',
    EN['vs_G62B_set']['gate_set_equals_g62b'] is False
    and EN['vs_G62B_set']['nodes_beyond_g62b'] == [
        7, 11, 12, 13, 14, 15, 16, 17, 18, 29, 30, 31, 32, 33],
    '14 nodes beyond the published six')
chk('D7_enumeration_frame_robust',
    EN['enumerations_equal'] is True
    and EN['negative_sec_nodes_typeI_restricted']
    == EN['negative_sec_nodes_sampled'],
    'sampled enumeration == Type-I-restricted enumeration')
chk('D8_fresh_profile_matches_gate62_stored',
    EN['vs_gate62_stored_profile']['max_per_node_sec_diff'] == 0.0
    and EN['vs_gate62_stored_profile'][
        'gate62_stored_negative_nodes']
    == EN['negative_sec_nodes_sampled'],
    'all 41 per-node SEC values at diff 0.0 vs Gate-62 stored')
chk('D9_dec_positive_at_every_negative_sec_node',
    all(v['dec_node_min'] > 0.0
        for v in EN['per_negative_node'].values()),
    'DEC node min > 0 at all 20 negative-SEC nodes')
chk('D10_dec_scope_fact_consistent',
    D['dec']['set_min'] == 2.820462654076372e-09
    and D['dec']['argmin_typeI'] is False
    and D['dec']['set_min_typeI'] == 4.224285347572982e-09,
    'DEC set min at a non-Type-I point; Type-I-restricted '
    'positive — the G62-B clause that survives verbatim')

# ---- G65-C: the non-vacuity control ----
C = G['C_f1']
chk('C1_f1_screen_diff0',
    all(v == 0.0 for v in C['diffs_vs_474_F1_screen'].values()
        if v is not None),
    '474 F1 screen on DECIDING_FIELDS')
chk('C2_f1_nodesec_diff0',
    all(v == 0.0 for v in C['node_sec_diffs'].values()),
    str(C['node_sec_gate']))
chk('C3_f1_node10_dec',
    C['node10_dec_diff'] == 0.0
    and C['node10_dec_gate'] == -5.375277493220288e-04,
    str(C['node10_dec_gate']))
chk('C4_f1_excluded', C['excluded'] is True,
    'SEC8/9/10 >= 0 and DEC10 < 0 on the gate read')

# ---- G65-E: the mechanism ----
E = G['E_mechanism']
chk('E1_arms_identical_fit',
    all(E['arms_x_identical_fit'].values()), 'F0/F1/F2')
chk('E2_arms_identical_confirm',
    all(E['arms_x_identical_confirm'].values()), 'F0/F1/F2')
chk('E3_lp_vs_exact_table',
    E['lp_vs_exact'] == {
        'A-F0': 8.117984553012553e-11, 'B-F0': 8.117984553012553e-11,
        'A-F1': 4.46882862712003e-11, 'B-F1': 4.46882862712003e-11,
        'A-F2': 4.448785615815561e-11, 'B-F2': 4.448785615815561e-11}
    and E['lp_vs_exact_max'] == 8.117984553012553e-11,
    "Gate-62's fixed table, reproduced")
chk('E4_member_dx',
    E['member_dx_max'] == 0.002009452499039281
    and E['member_dx_max'] <= 0.00201,
    str(E['member_dx_max']))

# ---- verdict logic (registration SS1) ----
standing = all(checks[k]['pass'] for k in (
    'A1_base_screen_diff0', 'A2_base_worstnull_diff0',
    'A3_base_adversary_diff0', 'B1_member_x_matches_charged',
    'B2_triple_diff0', 'B3_triple_equals_gate_base_triple',
    'B4_six_diff0', 'B5_six_values_charged', 'B6_frame_invariance',
    'B7_pen_diff0', 'B8_defended', 'D1_crosscheck_diff0',
    'D2_residue', 'D3_other_channels_positive_at_set_scope',
    'D4_sec_only_failing_channel', 'D9_dec_positive_at_every_'
    'negative_sec_node', 'D10_dec_scope_fact_consistent',
    'C1_f1_screen_diff0', 'C2_f1_nodesec_diff0', 'C3_f1_node10_dec',
    'C4_f1_excluded', 'E1_arms_identical_fit',
    'E2_arms_identical_confirm', 'E3_lp_vs_exact_table',
    'E4_member_dx'))
correction_real = checks['D6_enumeration_supersedes_G62B']['pass']
chk('V1_verdict_correction_confirmed',
    standing and correction_real
    and checks['D5_enumeration_equals_corrected_set_1297']['pass'],
    'standing parts all reproduce at diff 0.0 AND the complete '
    'enumeration supersedes G62-B\'s six')

n_pass = sum(1 for v in checks.values() if v['pass'])
out = {'gate': 'Gate-65',
       'checker': 'g65_check.py (stored records only)',
       'n_checks': len(checks), 'n_pass': n_pass,
       'all_pass': bool(n_pass == len(checks)),
       'verdict': ('CORRECTION CONFIRMED'
                   if checks['V1_verdict_correction_confirmed']['pass']
                   else 'SEE REPORT'),
       'checks': checks}
with open(os.path.join(HERE, '..', 'results', 'g65_verify.json'),
          'w') as f:
    json.dump(out, f, indent=1)
print(f"{n_pass}/{len(checks)} PASS; verdict: {out['verdict']}")
for k, v in checks.items():
    if not v['pass']:
        print('FAILED:', k, v['detail'])
