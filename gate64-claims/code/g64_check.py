#!/usr/bin/env python3
"""
g64_check.py -- Gate-64 independent checker.
Reads ONLY the gate's results file and the
stored phase records (no machinery imports,
no re-reads) and verifies the verdict logic
of g64_registration.md SS1 from the numbers.
Writes results/g64_verify.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(HERE, '..', 'results',
                                'g64_results.json')))
checks = {}


def chk(name, ok, detail=''):
    checks[name] = {'pass': bool(ok), 'detail': detail}


# ---- A1: the chain's bottom link (475's incumbent) ----
A1 = G['A1_incumbent']
chk('A1_incumbent_screen_diff0',
    all(v == 0.0 for v in
        A1['diffs_vs_475_incumbent_screen'].values()
        if v is not None),
    'all DECIDING_FIELDS vs 475 stored incumbent screen')
chk('A1_incumbent_worstnull_diff0', A1['worst_null_diff'] == 0.0,
    str(A1['worst_null']))
chk('A1_incumbent_adversary_diff0',
    A1['adversary_depth_diff'] == 0.0, str(A1['adversary_depth']))
chk('A1_incumbent_nodesec_diff0',
    all(d['sampled'] == 0.0 and d['typeI'] == 0.0
        for d in A1['node_sec_diffs_vs_475'].values()),
    'per-node SEC nodes 5..13, sampled and Type-I, vs 475 record')
chk('A1_incumbent_six_diff0',
    all(v == 0.0 for v in A1['six_diffs'].values()),
    str(A1['six_gate']))
chk('A1_incumbent_six_values',
    A1['six_gate'] == {
        'SEC7': -5.368730613015569e-06,
        'SEC10': -6.793448628664004e-06,
        'SEC11': -6.433344854499148e-06,
        'DEC7': 6.896066379048901e-05,
        'DEC10': 2.4658984119428845e-05,
        'DEC11': 1.783454002970248e-05},
    'the six at 7/10/11 fixed by CTL-482-1')

# ---- A2: the base (482's member as 494's base point) ----
chk('A2_held_x_is_482_member',
    G['x482_held_matches_482_member'] is True
    and G['lib_MEMBER_X482_matches_482_member'] is True,
    '494 x482_held and p494_lib MEMBER_X482 both equal 482 stored x')
A2 = G['A2_base']
chk('A2_base_screen_diff0',
    all(v == 0.0 for v in A2['diffs_vs_482_AF2_screen'].values()
        if v is not None),
    'all DECIDING_FIELDS vs 482 stored A-F2 confirmation screen')
chk('A2_base_triple_diff0',
    A2['joint_diff_vs_482_member'] == 0.0
    and A2['worst_null_diff_vs_482_member'] == 0.0
    and A2['adversary_depth_diff_vs_482_member'] == 0.0,
    f"joint {A2['joint']} wn {A2['worst_null']} "
    f"adv {A2['adversary_depth']}")
chk('A2_base_instruments_vs_CTL494_1',
    A2['worst_null_diff_vs_CTL494_1'] == 0.0
    and A2['adversary_depth_diff_vs_CTL494_1'] == 0.0,
    'worst-null and adversary vs 494 CTL-494-1 stored read')
chk('A2_base_pen_setsec_diff0',
    A2['pen_diff_vs_482_member'] == 0.0
    and A2['set_sec_min_diff_vs_482_member'] == 0.0,
    f"pen {A2['pen']} set_sec {A2['set_sec_min']}")
chk('A2_base_ten_diff0',
    all(v == 0.0 for v in A2['ten_diffs_vs_CTL494_1'].values())
    and all(v == 0.0 for v in A2['ten_diffs_vs_MEM_TEN'].values()),
    str(A2['ten_gate']))
chk('A2_base_ten_values',
    A2['ten_gate'] == {
        'SEC7': 1.7857748749212834e-05,
        'SEC8': -2.3136763326167455e-06,
        'SEC9': -4.647783392976125e-06,
        'SEC10': 1.7860144271433635e-05,
        'SEC11': 1.7845348315432977e-05,
        'DEC7': 6.902108374779023e-05,
        'DEC8': 4.844568674442049e-05,
        'DEC9': 3.44601033001249e-05,
        'DEC10': 2.4644814128023883e-05,
        'DEC11': 1.7845348315432977e-05},
    "482's member ten at 7..11 (8/9 negative: the union deficit)")
chk('A2_union_deficit_SEC9',
    A2['deficit10'] == 4.647783392976125e-06
    and A2['deficit10_diff_vs_CTL494_1'] == 0.0
    and A2['ten_gate']['SEC9'] == -4.647783392976125e-06
    and min(A2['ten_gate'].values()) == A2['ten_gate']['SEC9'],
    f"deficit10 {A2['deficit10']}, SEC9 binding")
chk('A2_base_node26_diff0',
    all(v == 0.0 for v in A2['node26_diffs_vs_CTL494_1'].values()),
    str(A2['node26']))

# ---- B: the member ----
B = G['B_member']
chk('B1_member_x_matches_stored', G['member_x_matches_stored'])
chk('B2_member_knots_charged',
    all(v == 0.0 for v in
        G['member_knots_charged']['knot_diffs'].values())
    and G['member_knots_charged']['n_nonzero'] == 2
    and G['member_knots_charged']['nonzero_indices'] == [10, 13],
    str(G['member_knots_charged']))
chk('B3_member_screen_diff0',
    all(v == 0.0 for v in B['diffs_vs_494_AF0_screen'].values()
        if v is not None),
    'all DECIDING_FIELDS vs 494 stored A-F0 confirmation screen')
chk('B4_triple_diff0',
    B['joint_diff_vs_stored'] == 0.0
    and B['worst_null_diff'] == 0.0
    and B['adversary_depth_diff'] == 0.0,
    f"joint {B['joint']} wn {B['worst_null']} "
    f"adv {B['adversary_depth']}")
chk('B5_triple_reproduces_base',
    B['joint'] == A2['joint']
    and B['worst_null'] == A2['worst_null']
    and B['adversary_depth'] == A2['adversary_depth'],
    'the joint was spent nowhere (vs the gate base read)')
chk('B6_ten_diff0_and_positive',
    all(v == 0.0 for v in B['ten_diffs'].values())
    and all(v > 0.0 for v in B['ten_gate'].values()),
    str(B['ten_gate']))
chk('B7_ten_values',
    B['ten_gate'] == {
        'SEC7': 1.7857748749212834e-05,
        'SEC8': 1.7864243400333773e-05,
        'SEC9': 1.7870862171171496e-05,
        'SEC10': 1.7955442310646822e-05,
        'SEC11': 1.7845348315432977e-05,
        'DEC7': 6.902108374779023e-05,
        'DEC8': 4.846795694247877e-05,
        'DEC9': 3.4468113036368415e-05,
        'DEC10': 2.4655507953470573e-05,
        'DEC11': 1.7845348315432977e-05},
    'SEC11 == DEC11 digit-for-digit included; worst union value '
    'is SEC11/DEC11 at node 11')
chk('B8_pen_setsec_diff0',
    B['pen_diff'] == 0.0 and B['set_sec_min_diff'] == 0.0,
    f"pen {B['pen']} set_sec {B['set_sec_min']}")
chk('B9_defended', B['defended'] is True)
chk('B10_frame_invariance',
    all(f['sec_sampled_eq_typeI'] and f['dec_sampled_eq_typeI']
        for f in B['frame_invariance'].values()),
    str(B['frame_invariance']))
chk('B11_deficit10_level',
    B['deficit10'] == -1.7845348315432977e-05,
    f"member deficit10 {B['deficit10']} == -SEC11 (node 11's pair "
    f"sets the level)")

# ---- C: tracked nodes + node 26 ----
C = G['C_tracked']
chk('C1_tracked_nodes_diff0',
    all(v == 0.0 for d in C['node_diffs_vs_494_AF0'].values()
        for v in d.values()),
    'nodes 5..13, SEC/DEC sampled and Type-I, vs 494 A-F0 record')
chk('C2_node26_diff0',
    all(v == 0.0 for v in C['node26_diffs_vs_494_AF0'].values()),
    str(C['node26_gate']))
chk('C3_node26_values',
    C['node26_gate']['sec'] == -6.792039324408745e-06
    and C['node26_gate']['dec'] == 1.1546418980741436e-08
    and C['node26_gate']['dec_typeI'] == 1.5358157534442506e-07,
    'node 26 SEC residue with DEC positive, sampled and Type-I')

# ---- D: the gate's own set read ----
D = G['D_set_read']
chk('D1_crosscheck_diff0',
    all(v['diff'] == 0.0 for v in G['D_crosscheck'].values()),
    'gate aux minima vs screen rec minima, 5 channels')
R = G['D_sec_residue']
chk('D2_residue_value_diff0', R['diff'] == 0.0
    and R['gate_value'] == -6.792039324408745e-06,
    str(R['gate_value']))
chk('D3_residue_locus', R['node'] == 26
    and R['r'] == 19.097560975609756
    and R['argmin_typeI'] is True,
    f"node {R['node']} r {R['r']} typeI {R['argmin_typeI']}")
chk('D4_residue_frameinvariant',
    R['typeI_set_min'] == R['gate_value'],
    f"typeI-restricted sec min {R['typeI_set_min']}")
chk('D5_failing_set_exact',
    R['negative_sec_node_set'] == [6, 12, 13, 20, 26],
    f"gate failing set {R['negative_sec_node_set']} vs claimed "
    f"[6, 12, 13, 20, 26]")
chk('D6_profile_vs_gate63_remaining',
    all(v == 0.0 for v in
        R['profile_vs_gate63']['remaining_five_diffs'].values()),
    'nodes 6/12/13/20/26 SEC identical to Gate-63 member profile')
chk('D7_profile_vs_gate63_lifted',
    R['profile_vs_gate63']['lifted_nodes_all_nonnegative'] is True
    and R['profile_vs_gate63']['cured_8_9_gate_values'] == {
        '8': 1.7864243400333773e-05, '9': 1.7870862171171496e-05},
    str(R['profile_vs_gate63']['lifted_nodes_gate_values']))
chk('D8_other_channels_positive',
    all(D[ch]['set_min'] > 0.0 for ch in ('nec', 'wec', 'dec', 'rho')),
    str({ch: D[ch]['set_min'] for ch in ('nec', 'wec', 'dec', 'rho')}))
chk('D9_failing_set_values',
    {n['node']: n['sec'] for n in R['negative_sec_nodes']} == {
        26: -6.792039324408745e-06,
        20: -6.64725597356898e-06,
        6: -5.927806537606205e-06,
        13: -4.049726337207395e-06,
        12: -2.8994490665248517e-06},
    str(R['negative_sec_nodes']))

# ---- E: mechanism consistency (stored records) ----
E = G['E_mechanism']
chk('E1_arms_identical',
    all(E['arms_x_identical_fit'].values())
    and all(E['arms_x_identical_confirm'].values()))
chk('E2_one_round_each',
    all(n == 1 for per in E['n_rounds'].values()
        for n in per.values()),
    str(E['n_rounds']))
chk('E3_f1f2_lp_exact_digit_for_digit',
    all(E['lp_vs_exact'][f'{a}-{r}'] == 0.0
        for a in ('A', 'B') for r in ('F1', 'F2')),
    str({k: E['lp_vs_exact'][k] for k in ('A-F1', 'A-F2')}))
chk('E4_f0_lp_vs_exact_gap',
    E['lp_vs_exact_F0'] == abs(-1.7857748749212834e-05
                               - (-1.7845348315432977e-05)),
    f"F0 |lp_t - exact_d10| = {E['lp_vs_exact_F0']} "
    f"(the disclosed 1.24e-8 FD-noise-floor gap)")
chk('E5_census', E['census']['n_candidates'] == 6
    and E['census']['n_union_feasible'] == 6,
    str(E['census']))
chk('E6_diagnostic_feasible',
    E['diagnostic_feasible_full'] is True)
chk('E7_reach_arithmetic',
    E['reach_nonzero_cols'] == {
        'SEC7': 9, 'SEC8': 18, 'SEC9': 27, 'SEC10': 18,
        'SEC11': 9, 'DEC7': 9, 'DEC8': 18, 'DEC9': 27,
        'DEC10': 18, 'DEC11': 9, 'JOINT': 0},
    str(E['reach_nonzero_cols']))
chk('E8_joint_row_vacuous',
    E['reach_joint']['identically_zero'] is True
    and E['reach_joint']['max_abs'] == 0.0
    and E['jrow_all_zero'] is True and E['jrow_len'] == 27,
    'the eleventh (joint) constraint row is identically 0.0 in '
    'all 27 columns — measured in advance, binding nowhere')
chk('E9_probe_within_tolerance',
    E['probe_max_abs_err'] == 5.323831386412842e-07
    and E['probe_max_abs_err'] < 1.0e-06,
    f"CTL-494-3 probe ten-row max |err| {E['probe_max_abs_err']}")
chk('E10_member_step_small',
    E['member_dx_max'] == 0.0009057435147531116
    and E['member_dx_max'] <= 0.00091,
    str(E['member_dx_max']))

n_pass = sum(1 for c in checks.values() if c['pass'])
verdict = 'PASS' if n_pass == len(checks) else 'CHECK FAILURE'
out = {'gate': 'Gate-64', 'checks': checks,
       'n_pass': n_pass, 'n_total': len(checks),
       'verdict_from_checks': verdict}
with open(os.path.join(HERE, '..', 'results', 'g64_verify.json'),
          'w') as f:
    json.dump(out, f, indent=1)
print(f'{n_pass}/{len(checks)} PASS -> {verdict}')
for k, v in checks.items():
    print(('PASS ' if v['pass'] else 'FAIL ') + k, v['detail'])
