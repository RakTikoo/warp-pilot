#!/usr/bin/env python3
"""
g62_check.py -- Gate-62 independent checker.
Reads ONLY the gate's results file and the
stored phase records (no machinery imports,
no re-reads) and verifies the verdict logic
of g62_registration.md SS1 from the numbers.
Writes results/g62_verify.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WP = '/home/hatch/workspace/warp-pilot'
G = json.load(open(os.path.join(HERE, '..', 'results',
                                'g62_results.json')))
checks = {}


def chk(name, ok, detail=''):
    checks[name] = {'pass': bool(ok), 'detail': detail}


A = G['A_base']
chk('A1_base_screen_diff0',
    all(v == 0.0 for v in A['diffs_vs_BASE_REC'].values()),
    'all DECIDING_FIELDS vs p460_lib BASE_REC')
chk('A2_base_worstnull_diff0', A['worst_null_diff'] == 0.0,
    str(A['worst_null']))
chk('A3_base_adversary_diff0', A['adversary_depth_diff'] == 0.0,
    str(A['adversary_depth']))

B = G['B_member']
chk('B1_member_x_matches_stored', G['member_x_matches_stored'])
chk('B2_triple_diff0',
    B['joint_diff_vs_stored'] == 0.0
    and B['worst_null_diff'] == 0.0
    and B['adversary_depth_diff'] == 0.0,
    f"joint {B['joint']} wn {B['worst_null']} adv {B['adversary_depth']}")
chk('B3_six_diff0_and_positive',
    all(v == 0.0 for v in B['six_diffs'].values())
    and all(v > 0.0 for v in B['six_gate'].values()),
    str(B['six_gate']))
chk('B4_pen_diff0', B['pen_diff'] == 0.0, str(B['screen']['pen']))
chk('B5_defended', B['defended'] is True)
chk('B6_frame_invariance',
    all(f['sec_sampled_eq_typeI'] and f['dec_sampled_eq_typeI']
        for f in B['frame_invariance'].values()),
    str(B['frame_invariance']))

D = G['D_set_read']
chk('D1_crosscheck_diff0',
    all(v['diff'] == 0.0 for v in G['D_crosscheck'].values()),
    'gate aux minima vs screen rec minima, 5 channels')
R = G['D_sec_residue']
chk('D2_residue_value_diff0', R['diff'] == 0.0
    and R['gate_value'] == -6.459908493210403e-06,
    str(R['gate_value']))
chk('D3_residue_typeI_and_frameinvariant',
    R['argmin_typeI'] is True
    and D['sec']['set_min_typeI'] == D['sec']['set_min'],
    f"typeI-restricted sec min {D['sec']['set_min_typeI']}")
chk('D4_residue_radius', R['r'] == 17.04878048780488, str(R['r']))
chk('D5_residue_node_label',
    R['node'] == 23 and R['node'] != 25,
    f"gate node index {R['node']} (NODES[25] SEC = "
    f"{R['node25_sec_sampled']}) -- rider G62-R1")

C = G['C_f1']
chk('C1_f1_screen_diff0',
    all(v == 0.0 for v in C['diffs_vs_474_F1_screen'].values()
        if v is not None))
chk('C2_f1_nodesec_diff0',
    all(v == 0.0 for v in C['node_sec_diffs'].values()))
chk('C3_f1_node10dec_diff0', C['node10_dec_diff'] == 0.0
    and C['screen_dec_min_gate'] == C['dec_target'],
    str(C['node10_dec_gate']))
chk('C4_f1_excluded', C['excluded'] is True, str(C['six_on_F1']))

E = G['E_mechanism']
chk('E1_arms_identical',
    all(E['arms_x_identical_fit'].values())
    and all(E['arms_x_identical_confirm'].values()))
chk('E2_lp_vs_exact',
    E['lp_vs_exact']['A-F1'] == 4.46882862712003e-11
    and E['lp_vs_exact_max'] == 8.117984553012553e-11,
    f"max {E['lp_vs_exact_max']}")
chk('E3_member_step_small',
    E['member_dx_max'] == 0.002009452499039281
    and E['member_dx_max'] <= 0.00201 < 0.03,
    str(E['member_dx_max']))

n_pass = sum(1 for c in checks.values() if c['pass'])
verdict = ('PASS WITH RIDER (G62-R1)'
           if n_pass == len(checks) else 'CHECK FAILURE')
out = {'gate': 'Gate-62', 'checks': checks,
       'n_pass': n_pass, 'n_total': len(checks),
       'verdict_from_checks': verdict,
       'rider': ('G62-R1: the residue locus label. The phase '
                 'record (entries 1240/1250, the 474/479 memos) '
                 'names the set SEC argmin "node 25"; in the '
                 'gate\'s own numbers, in the same 0-based NODES '
                 'indexing in which the basin nodes are 8/9/10, '
                 'r = 17.04878048780488 is node index 23 '
                 '(NODES[25], r = 18.414634146341463, carries '
                 'SEC -3.293564937848059e-06 on the member). '
                 'Value, radius, Type-I status and '
                 'frame-invariance of the residue are exact at '
                 'diff 0.0; only the label is restated.')}
with open(os.path.join(HERE, '..', 'results', 'g62_verify.json'),
          'w') as f:
    json.dump(out, f, indent=1)
print(f'{n_pass}/{len(checks)} PASS -> {verdict}')
for k, v in checks.items():
    print(('PASS ' if v['pass'] else 'FAIL ') + k, v['detail'])
