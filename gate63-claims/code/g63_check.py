#!/usr/bin/env python3
"""
g63_check.py -- Gate-63 independent checker.
Reads ONLY the gate's results file and the
stored phase records (no machinery imports,
no re-reads) and verifies the verdict logic
of g63_registration.md SS1 from the numbers.
Writes results/g63_verify.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(HERE, '..', 'results',
                                'g63_results.json')))
checks = {}


def chk(name, ok, detail=''):
    checks[name] = {'pass': bool(ok), 'detail': detail}


A = G['A_base']
chk('A1_base_screen_diff0',
    all(v == 0.0 for v in A['diffs_vs_475_incumbent_screen'].values()
        if v is not None),
    'all DECIDING_FIELDS vs 475 stored incumbent screen')
chk('A2_base_worstnull_diff0', A['worst_null_diff'] == 0.0,
    str(A['worst_null']))
chk('A3_base_adversary_diff0', A['adversary_depth_diff'] == 0.0,
    str(A['adversary_depth']))
chk('A4_base_nodesec_diff0',
    all(d['sampled'] == 0.0 and d['typeI'] == 0.0
        for d in A['node_sec_diffs_vs_475'].values()),
    'per-node SEC nodes 5..13, sampled and Type-I, vs 475 record')
chk('A5_base_six_diff0',
    all(v == 0.0 for v in A['six_diffs'].values()),
    str(A['six_gate']))
chk('A6_base_six_values',
    A['six_gate'] == {
        'SEC7': -5.368730613015569e-06,
        'SEC10': -6.793448628664004e-06,
        'SEC11': -6.433344854499148e-06,
        'DEC7': 6.896066379048901e-05,
        'DEC10': 2.4658984119428845e-05,
        'DEC11': 1.783454002970248e-05},
    'the six at 7/10/11 fixed by CTL-482-1')

B = G['B_member']
chk('B1_member_x_matches_stored', G['member_x_matches_stored'])
chk('B2_member_knots_charged',
    all(v == 0.0 for v in
        G['member_knots_charged']['knot_diffs'].values())
    and G['member_knots_charged']['n_nonzero'] == 3,
    str(G['member_knots_charged']))
chk('B3_triple_diff0',
    B['joint_diff_vs_stored'] == 0.0
    and B['worst_null_diff'] == 0.0
    and B['adversary_depth_diff'] == 0.0,
    f"joint {B['joint']} wn {B['worst_null']} "
    f"adv {B['adversary_depth']}")
chk('B4_triple_reproduces_incumbent',
    B['joint'] == A['screen']['joint']
    and B['worst_null'] == A['worst_null']
    and B['adversary_depth'] == A['adversary_depth'],
    'the joint was spent nowhere (vs the gate base read)')
chk('B5_six_diff0_and_positive',
    all(v == 0.0 for v in B['six_diffs'].values())
    and all(v > 0.0 for v in B['six_gate'].values()),
    str(B['six_gate']))
chk('B6_six_values',
    B['six_gate'] == {
        'SEC7': 1.7857748749212834e-05,
        'SEC10': 1.7860144271433635e-05,
        'SEC11': 1.7845348315432977e-05,
        'DEC7': 6.902108374779023e-05,
        'DEC10': 2.4644814128023883e-05,
        'DEC11': 1.7845348315432977e-05},
    'SEC11 == DEC11 digit-for-digit included')
chk('B7_pen_diff0', B['pen_diff'] == 0.0, str(B['screen']['pen']))
chk('B8_defended', B['defended'] is True)
chk('B9_frame_invariance',
    all(f['sec_sampled_eq_typeI'] and f['dec_sampled_eq_typeI']
        for f in B['frame_invariance'].values()),
    str(B['frame_invariance']))

C = G['C_failing_set']
chk('C1_tracked_nodes_diff0',
    all(v == 0.0 for d in C['node_diffs_vs_482_AF2'].values()
        for v in d.values()),
    'nodes 5..13, SEC/DEC sampled and Type-I, vs 482 A-F2 record')
chk('C2_basin_lifted_not_cured',
    C['basin']['SEC8'] == -2.3136763326167455e-06
    and C['basin']['SEC9'] == -4.647783392976125e-06,
    f"SEC8 {C['basin']['SEC8']} SEC9 {C['basin']['SEC9']}")
chk('C3_basin_dec_positive',
    C['basin']['basin_dec_all_positive'] is True,
    str({k: C['basin'][k] for k in ('DEC8', 'DEC9', 'DEC10')}))

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
from decimal import Decimal
_dec_headroom = (Decimal('-6.792039324408745e-06')
                 - Decimal('-6.793448628664004e-06'))
chk('D5_headroom_arithmetic',
    _dec_headroom == Decimal('1.409304255259e-09')
    and R['headroom_diff'] < 2e-22,
    f"exact decimal headroom {_dec_headroom} == pre-registered "
    f"1.409304255259e-09; float64 subtraction of the same stored "
    f"operands gives {R['headroom_gate']} (binary residue "
    f"{R['headroom_diff']:.3e}, below the pre-registration's "
    f"last digit)")
chk('D6_other_channels_positive',
    all(D[ch]['set_min'] > 0.0 for ch in ('nec', 'wec', 'dec', 'rho')),
    str({ch: D[ch]['set_min'] for ch in ('nec', 'wec', 'dec', 'rho')}))

E = G['E_mechanism']
chk('E1_arms_identical',
    all(E['arms_x_identical_fit'].values())
    and all(E['arms_x_identical_confirm'].values()))
chk('E2_f0f1_capped_at_node7',
    all(E['round1_exact_d6c'][f'{a}-{r}']
        == 5.368730613015569e-06
        for a in ('A', 'B') for r in ('F0', 'F1')),
    str(E['round1_exact_d6c']))
chk('E3_f2_lp_vs_exact',
    E['lp_vs_exact_F2'] == abs(-1.7845395441136043e-05
                               - (-1.7845348315432977e-05)),
    f"F2 |lp_t - exact_d6c| = {E['lp_vs_exact_F2']}")
chk('E4_member_step_small',
    E['member_dx_max'] == 0.0011990467393266006
    and E['member_dx_max'] <= 0.00120 < 0.03,
    str(E['member_dx_max']))
chk('E5_census', E['census']['n_candidates'] == 10
    and E['census']['n_cluster_feasible'] == 2,
    str(E['census']))

n_pass = sum(1 for c in checks.values() if c['pass'])
verdict = 'PASS' if n_pass == len(checks) else 'CHECK FAILURE'
out = {'gate': 'Gate-63', 'checks': checks,
       'n_pass': n_pass, 'n_total': len(checks),
       'verdict_from_checks': verdict}
with open(os.path.join(HERE, '..', 'results', 'g63_verify.json'),
          'w') as f:
    json.dump(out, f, indent=1)
print(f'{n_pass}/{len(checks)} PASS -> {verdict}')
for k, v in checks.items():
    print(('PASS ' if v['pass'] else 'FAIL ') + k, v['detail'])
