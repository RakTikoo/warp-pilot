#!/usr/bin/env python3
"""
g64_run.py -- Gate-64 driver: independent
re-judgement of Phase 494's member on the
levelled base (482's member as base; the
union {7, 8, 9, 10, 11} cured).
Registration: work/g64_registration.md
(filed before any Gate-64 computation);
charge: ledger entry 1293 (Phase 494
referred on landing).

The gate drives the lineage machinery
itself (p494_lib -> p482_lib -> p475_lib
-> p460_lib -> p449_lib; SET-244 /
SAMPLER-M, float64, VM, Phase-166 pin)
and computes the set read (SS G64-D)
from the read's per-point record in its
own code. Results are checkpointed to
results/g64_results.json after each
read.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, os.path.join(WP, 'phase494/work'))
sys.path.insert(0, os.path.join(WP, 'phase482/work'))

import p482_lib as P  # noqa: E402
import p494_lib as Q  # noqa: E402

L = Q.L
DTYPE = Q.DTYPE
NODES = [float(r) for r in Q.NODES]
OUT = os.path.join(HERE, '..', 'results', 'g64_results.json')

# the charged member knots (entry 1293):
# W494B[1] at y27[10], W494B[4] at y27[13]
KNOT_B1 = -0.0009057435147531116
KNOT_B4 = -0.0008762943517712976

res = {'gate': 'Gate-64', 'charge_entry': 1293}


def save():
    with open(OUT, 'w') as f:
        json.dump(res, f, indent=1)


def diffs(rec, stored, fields):
    return {k: (abs(rec[k] - stored[k])
                if isinstance(stored.get(k), (int, float))
                and not isinstance(stored.get(k), bool)
                else (0.0 if rec.get(k) == stored.get(k) else None))
            for k in fields}


def instruments482(x27, read, aux):
    lev = P.levers_of(x27)
    pt = np.array(read['nec_argmin_point'], dtype=DTYPE)
    wn, wf = L.worst_null449(P.BASE_MUN, P.BASE_MUM, lev, pt)
    adv = L.adversary449(P.BASE_MUN, P.BASE_MUM, lev, aux)
    return wn, wf, adv


def instruments494(y27, read, aux):
    lev = Q.levers_of(y27)
    pt = np.array(read['nec_argmin_point'], dtype=DTYPE)
    wn, wf = L.worst_null449(Q.BASE_MUN, Q.BASE_MUM, lev, pt)
    adv = L.adversary449(Q.BASE_MUN, Q.BASE_MUM, lev, aux)
    return wn, wf, adv


def set_read(aux):
    """The gate's own full SET-244 read from
    the per-point record: per channel, the
    set minimum with locus (node, radius,
    direction index) and Type-I flag of the
    argmin point, plus the Type-I-restricted
    set minimum with its locus, plus the
    full per-node minima profile."""
    R = aux['R']
    n = len(NODES)
    per = R['nec'].reshape(n, -1).shape[1]
    ti = R['typeI'].reshape(n, per)
    out = {'n_nodes': n, 'per_node': int(per)}
    for k in ('nec', 'wec', 'dec', 'sec', 'rho'):
        A = R[k].reshape(n, per)
        i = int(np.argmin(A))
        ni, di = divmod(i, per)
        Am = np.where(ti, A, np.inf)
        j = int(np.argmin(Am))
        nj, dj = divmod(j, per)
        out[k] = {
            'set_min': float(A[ni, di]),
            'node': int(ni), 'r': NODES[ni],
            'dir_index': int(di),
            'argmin_typeI': bool(ti[ni, di]),
            'set_min_typeI': float(Am[nj, dj]),
            'typeI_node': int(nj), 'typeI_r': NODES[nj],
            'typeI_dir_index': int(dj),
            'node_min': [float(v) for v in np.min(A, axis=1)],
        }
    return out


# ---------- stored targets ----------
c475 = json.load(open(os.path.join(
    WP, 'phase475/results/p475_confirmation.json')))
inc475 = c475['incumbent']
inc_screen = inc475['screen']
inc_adv_depth = inc475['adversary']['in_region_worst_nec_SAMPLER-M'] \
    if isinstance(inc475.get('adversary'), dict) else None

c482 = json.load(open(os.path.join(
    WP, 'phase482/results/p482_confirmations.json')))
tm482 = c482['the_member']
o482_f2 = c482['outputs']['A-F2']
ctl482 = json.load(open(os.path.join(
    WP, 'phase482/results/p482_controls.json')))
base_six_stored = ctl482['base_six']

c494 = json.load(open(os.path.join(
    WP, 'phase494/results/p494_confirmations.json')))
tm494 = c494['the_member']
o494_f0 = c494['outputs']['A-F0']
ctl494 = json.load(open(os.path.join(
    WP, 'phase494/results/p494_controls.json')))
fit494 = json.load(open(os.path.join(
    WP, 'phase494/results/p494_fit.json')))
jac494 = json.load(open(os.path.join(
    WP, 'phase494/results/p494_jacobians.json')))
g63 = json.load(open(os.path.join(
    WP, 'gate63/results/g63_results.json')))
g63_profile = g63['D_set_read']['sec']['node_min']

res['stored_member482_x'] = tm482['x']
res['stored_member494_x'] = tm494['x']
res['x482_held_matches_482_member'] = bool(
    tm494['x482_held'] == tm482['x'])
res['lib_MEMBER_X482_matches_482_member'] = bool(
    list(Q.MEMBER_X482) == tm482['x'])
res['stored_incumbent_adversary_depth'] = inc_adv_depth

# ---------- G64-A1: the chain's bottom link (475's incumbent) ----------
x_base482 = np.zeros(27, dtype=DTYPE)
rec, read, aux, node = P.read_object(x_base482, stage='G64-A1')
wn, wf, adv = instruments482(x_base482, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
six_gate_base = P.six_values(node)
res['A1_incumbent'] = {
    'screen': rec,
    'diffs_vs_475_incumbent_screen': diffs(
        rec, inc_screen, P.DECIDING_FIELDS),
    'worst_null': wn, 'worst_null_fib': wf,
    'worst_null_diff': abs(wn - inc475['worst_null_at_nec_argmin']),
    'adversary_depth': adv_depth,
    'adversary_depth_diff': (
        abs(adv_depth - inc_adv_depth)
        if inc_adv_depth is not None else None),
    'node_sec_diffs_vs_475': {
        str(i): {'sampled': abs(node[i]['sec'] - P.INC_NODE_SEC[i]),
                 'typeI': abs(node[i]['sec_typeI'] - P.INC_NODE_SEC[i])}
        for i in range(5, 14)},
    'six_gate': six_gate_base,
    'six_stored_CTL482_1': base_six_stored,
    'six_diffs': {k: abs(six_gate_base[k] - base_six_stored[k])
                  for k in base_six_stored},
}
save()
print('G64-A1 done: max screen diff',
      max(v for v in res['A1_incumbent'][
          'diffs_vs_475_incumbent_screen'].values() if v is not None),
      'six diffs', res['A1_incumbent']['six_diffs'], flush=True)

# ---------- G64-A2: the base (482's member through p494_lib) ----------
y_base = np.zeros(27, dtype=DTYPE)
rec, read, aux, node, node26 = Q.read_object(y_base, stage='G64-A2')
wn, wf, adv = instruments494(y_base, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
ten_gate_base = Q.ten_values(node)
res['A2_base'] = {
    'screen': rec,
    'diffs_vs_482_AF2_screen': diffs(
        rec, o482_f2['screen'], Q.DECIDING_FIELDS),
    'joint': rec['joint'],
    'joint_diff_vs_482_member': abs(
        rec['joint'] - tm482['defended_triple']['joint']),
    'worst_null': wn, 'worst_null_fib': wf,
    'worst_null_diff_vs_482_member': abs(
        wn - tm482['defended_triple']['worst_null']),
    'worst_null_diff_vs_CTL494_1': abs(
        wn - ctl494['CTL-494-1']['worst_null']),
    'adversary_depth': adv_depth,
    'adversary_depth_diff_vs_482_member': abs(
        adv_depth - tm482['defended_triple']['adversary_depth']),
    'adversary_depth_diff_vs_CTL494_1': abs(
        adv_depth - ctl494['CTL-494-1']['adversary_depth']),
    'pen': rec['pen'],
    'pen_diff_vs_482_member': abs(rec['pen'] - tm482['pen']),
    'set_sec_min': rec['sec_min'],
    'set_sec_min_diff_vs_482_member': abs(
        rec['sec_min'] - tm482['set_sec_min']),
    'ten_gate': ten_gate_base,
    'ten_stored_CTL494_1': ctl494['base_ten'],
    'ten_diffs_vs_CTL494_1': {
        k: abs(ten_gate_base[k] - ctl494['base_ten'][k])
        for k in ctl494['base_ten']},
    'ten_diffs_vs_MEM_TEN': {
        f'{ch.upper()}{i}': abs(
            ten_gate_base[f'{ch.upper()}{i}'] - Q.MEM_TEN[(ch, i)])
        for ch in ('sec', 'dec') for i in (7, 8, 9, 10, 11)},
    'deficit10': Q.deficit10(node),
    'deficit10_diff_vs_CTL494_1': abs(
        Q.deficit10(node) - ctl494['base_deficit10']),
    'node': {str(k): v for k, v in node.items()},
    'node26': node26,
    'node26_diffs_vs_CTL494_1': {
        k: abs(node26[k] - ctl494['base_node26'][k])
        for k in ('sec', 'sec_typeI', 'dec', 'dec_typeI')},
}
save()
print('G64-A2 done: deficit10', res['A2_base']['deficit10'],
      'ten diffs', res['A2_base']['ten_diffs_vs_CTL494_1'],
      flush=True)

# ---------- G64-B: the member ----------
y_member = np.asarray(tm494['x'], dtype=DTYPE)
res['member_x_gate'] = y_member.tolist()
res['member_x_matches_stored'] = bool(y_member.tolist() == tm494['x'])
res['member_knots_charged'] = {
    'W494B[1]_y27[10]': float(y_member[10]),
    'W494B[4]_y27[13]': float(y_member[13]),
    'knot_diffs': {
        'B1': abs(float(y_member[10]) - KNOT_B1),
        'B4': abs(float(y_member[13]) - KNOT_B4)},
    'n_nonzero': int(np.count_nonzero(y_member)),
    'nonzero_indices': [int(i) for i in np.nonzero(y_member)[0]],
}
rec, read, aux, node, node26 = Q.read_object(y_member, stage='G64-B')
wn, wf, adv = instruments494(y_member, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
ten_gate = Q.ten_values(node)
ten_stored = tm494['ten']
res['B_member'] = {
    'screen': rec,
    'diffs_vs_494_AF0_screen': diffs(
        rec, o494_f0['screen'], Q.DECIDING_FIELDS),
    'joint': rec['joint'],
    'joint_diff_vs_stored': abs(
        rec['joint'] - tm494['defended_triple']['joint']),
    'worst_null': wn,
    'worst_null_diff': abs(
        wn - tm494['defended_triple']['worst_null']),
    'adversary_depth': adv_depth,
    'adversary_depth_diff': abs(
        adv_depth - tm494['defended_triple']['adversary_depth']),
    'pen': rec['pen'],
    'pen_diff': abs(rec['pen'] - tm494['pen']),
    'set_sec_min': rec['sec_min'],
    'set_sec_min_diff': abs(rec['sec_min'] - tm494['set_sec_min']),
    'ten_gate': ten_gate,
    'ten_stored': ten_stored,
    'ten_diffs': {k: abs(ten_gate[k] - ten_stored[k])
                  for k in ten_stored},
    'node': {str(k): v for k, v in node.items()},
    'node26': node26,
    'frame_invariance': {
        str(i): {'sec_sampled_eq_typeI':
                 node[i]['sec'] == node[i]['sec_typeI'],
                 'dec_sampled_eq_typeI':
                 node[i]['dec'] == node[i]['dec_typeI']}
        for i in (7, 8, 9, 10, 11)},
    'defended': bool(rec['joint'] >= 0.0 and wn >= 0.0
                     and adv_depth >= 0.0),
    'deficit10': Q.deficit10(node),
}
save()
print('G64-B done: ten diffs', res['B_member']['ten_diffs'],
      'defended', res['B_member']['defended'], flush=True)

# ---------- G64-C: tracked nodes + node 26 vs 494's A-F0 record ----------
o_node = o494_f0['node']
res['C_tracked'] = {
    'node_diffs_vs_494_AF0': {
        str(i): {ch: abs(node[i][ch] - o_node[str(i)][ch])
                 for ch in ('sec', 'sec_typeI', 'dec', 'dec_typeI')}
        for i in range(5, 14)},
    'node26_diffs_vs_494_AF0': {
        ch: abs(node26[ch] - o494_f0['node26'][ch])
        for ch in ('sec', 'sec_typeI', 'dec', 'dec_typeI')},
    'node26_gate': node26,
}
save()
print('G64-C done: node26', node26, flush=True)

# ---------- G64-D: the gate's own set read of the member ----------
sr = set_read(aux)
res['D_set_read'] = sr
res['D_crosscheck'] = {
    k: {'gate_aux': sr[k]['set_min'],
        'screen_rec': rec[k + '_min'],
        'diff': abs(sr[k]['set_min'] - rec[k + '_min'])}
    for k in ('nec', 'wec', 'dec', 'sec', 'rho')}
neg_nodes = [i for i in range(len(NODES))
             if sr['sec']['node_min'][i] < 0.0]
res['D_sec_residue'] = {
    'gate_value': sr['sec']['set_min'],
    'phase_value': -6.792039324408745e-06,
    'diff': abs(sr['sec']['set_min'] - (-6.792039324408745e-06)),
    'node': sr['sec']['node'], 'r': sr['sec']['r'],
    'argmin_typeI': sr['sec']['argmin_typeI'],
    'typeI_set_min': sr['sec']['set_min_typeI'],
    'negative_sec_nodes': [
        {'node': i, 'r': NODES[i], 'sec': sr['sec']['node_min'][i]}
        for i in neg_nodes],
    'negative_sec_node_set': neg_nodes,
    'claimed_negative_set': [6, 12, 13, 20, 26],
    'profile_vs_gate63': {
        'remaining_five_diffs': {
            str(i): abs(sr['sec']['node_min'][i] - g63_profile[i])
            for i in (6, 12, 13, 20, 26)},
        'cured_8_9_gate_values': {
            '8': sr['sec']['node_min'][8],
            '9': sr['sec']['node_min'][9]},
        'lifted_nodes_gate_values': {
            str(i): sr['sec']['node_min'][i]
            for i in (14, 15, 19, 21, 24, 25, 27, 31, 32, 33)},
        'lifted_nodes_all_nonnegative': bool(all(
            sr['sec']['node_min'][i] >= 0.0
            for i in (14, 15, 19, 21, 24, 25, 27, 31, 32, 33))),
        'gate63_negative_nodes': [
            i for i in range(len(NODES)) if g63_profile[i] < 0.0],
    },
}
save()
print('G64-D done: sec set min', sr['sec']['set_min'],
      'at node', sr['sec']['node'], 'r', sr['sec']['r'],
      'typeI', sr['sec']['argmin_typeI'],
      'negative nodes', neg_nodes, flush=True)

# ---------- G64-E: mechanism consistency (stored records) ----------
e = {'arms_x_identical_fit': {}, 'arms_x_identical_confirm': {},
     'lp_vs_exact': {}, 'round1_exact_d10': {}, 'n_rounds': {}}
for rung in ('F0', 'F1', 'F2'):
    e['arms_x_identical_fit'][rung] = bool(
        fit494['arms']['A']['rungs'][rung]['best']['x']
        == fit494['arms']['B']['rungs'][rung]['best']['x'])
    e['arms_x_identical_confirm'][rung] = bool(
        c494['outputs'][f'A-{rung}']['x']
        == c494['outputs'][f'B-{rung}']['x'])
    e['n_rounds'][rung] = {
        arm: len(fit494['arms'][arm]['rungs'][rung]['rounds'])
        for arm in ('A', 'B')}
    for arm in ('A', 'B'):
        r1 = fit494['arms'][arm]['rungs'][rung]['rounds'][0]
        e['lp_vs_exact'][f'{arm}-{rung}'] = abs(
            r1['lp_t'] - r1['exact_d10'])
        e['round1_exact_d10'][f'{arm}-{rung}'] = r1['exact_d10']
e['lp_vs_exact_F0'] = e['lp_vs_exact']['A-F0']
e['member_dx_max'] = max(abs(v) for v in tm494['x'])
e['census'] = c494['candidate_census']
e['diagnostic_feasible_full'] = fit494['diagnostic']['feasible_full']
reach = jac494['reach']
e['reach_nonzero_cols'] = {
    k: reach[k]['nonzero_cols'] for k in reach}
e['reach_joint'] = reach['JOINT']
e['jrow_all_zero'] = bool(
    all(v == 0.0 for v in jac494['base']['jrow']))
e['jrow_len'] = len(jac494['base']['jrow'])
probe_errs = jac494['CTL-494-3']['errors']
e['probe_max_abs_err'] = max(
    abs(v['err']) for v in probe_errs.values())
res['E_mechanism'] = e
save()
print('G64-E done: F0 lp_vs_exact', e['lp_vs_exact_F0'],
      'dx_max', e['member_dx_max'],
      'probe max err', e['probe_max_abs_err'], flush=True)
print('ALL READS COMPLETE', flush=True)
