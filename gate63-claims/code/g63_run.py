#!/usr/bin/env python3
"""
g63_run.py -- Gate-63 driver: independent
re-judgement of Phase 482's member on the
levelled base (475's incumbent).
Registration: work/g63_registration.md
(filed before any Gate-63 computation);
charge: ledger entry 1278.

The gate drives the lineage machinery
itself (p482_lib -> p475_lib -> p460_lib
-> p449_lib; SET-244 / SAMPLER-M,
float64, VM, Phase-166 pin) and computes
the set read (SS G63-D) from the read's
per-point record in its own code.
Results are checkpointed to
results/g63_results.json after each
read.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, os.path.join(WP, 'phase482/work'))

import p482_lib as P  # noqa: E402

L = P.L
DTYPE = P.DTYPE
NODES = [float(r) for r in P.NODES]
OUT = os.path.join(HERE, '..', 'results', 'g63_results.json')

# the charged member knots (entry 1278)
KNOT_A4 = -0.0006256155864301123   # x27[4]
KNOT_B4 = -0.0010659530055582157  # x27[13]
KNOT_C4 = -0.0011990467393266006  # x27[22]

res = {'gate': 'Gate-63', 'charge_entry': 1278}


def save():
    with open(OUT, 'w') as f:
        json.dump(res, f, indent=1)


def diffs(rec, stored, fields):
    return {k: (abs(rec[k] - stored[k])
                if isinstance(stored.get(k), (int, float))
                and not isinstance(stored.get(k), bool)
                else (0.0 if rec.get(k) == stored.get(k) else None))
            for k in fields}


def instruments(x27, read, aux):
    lev = P.levers_of(x27)
    pt = np.array(read['nec_argmin_point'], dtype=DTYPE)
    wn, wf = L.worst_null449(P.BASE_MUN, P.BASE_MUM, lev, pt)
    adv = L.adversary449(P.BASE_MUN, P.BASE_MUM, lev, aux)
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
tm = c482['the_member']
f482 = json.load(open(os.path.join(
    WP, 'phase482/results/p482_fit.json')))
ctl482 = json.load(open(os.path.join(
    WP, 'phase482/results/p482_controls.json')))
base_six_stored = ctl482['base_six']

res['stored_member_x'] = tm['x']
res['stored_incumbent_adversary_depth'] = inc_adv_depth

# ---------- G63-A: the base (475's incumbent) ----------
x_base = np.zeros(27, dtype=DTYPE)
rec, read, aux, node = P.read_object(x_base, stage='G63-A')
wn, wf, adv = instruments(x_base, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
six_gate_base = P.six_values(node)
res['A_base'] = {
    'screen': rec,
    'diffs_vs_475_incumbent_screen': diffs(
        rec, inc_screen, P.DECIDING_FIELDS),
    'worst_null': wn, 'worst_null_fib': wf,
    'worst_null_diff': abs(wn - inc475['worst_null_at_nec_argmin']),
    'adversary_depth': adv_depth,
    'adversary_depth_diff': (
        abs(adv_depth - inc_adv_depth)
        if inc_adv_depth is not None else None),
    'node': {str(k): v for k, v in node.items()},
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
print('G63-A done: max screen diff',
      max(v for v in res['A_base']['diffs_vs_475_incumbent_screen'].values()
          if v is not None),
      'six diffs', res['A_base']['six_diffs'], flush=True)

# ---------- G63-B: the member ----------
x_member = np.asarray(tm['x'], dtype=DTYPE)
res['member_x_gate'] = x_member.tolist()
res['member_x_matches_stored'] = bool(x_member.tolist() == tm['x'])
res['member_knots_charged'] = {
    'W482A[4]_x27[4]': float(x_member[4]),
    'W482B[4]_x27[13]': float(x_member[13]),
    'W482C[4]_x27[22]': float(x_member[22]),
    'knot_diffs': {
        'A4': abs(float(x_member[4]) - KNOT_A4),
        'B4': abs(float(x_member[13]) - KNOT_B4),
        'C4': abs(float(x_member[22]) - KNOT_C4)},
    'n_nonzero': int(np.count_nonzero(x_member)),
}
rec, read, aux, node = P.read_object(x_member, stage='G63-B')
wn, wf, adv = instruments(x_member, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
six_gate = P.six_values(node)
six_stored = tm['six']
res['B_member'] = {
    'screen': rec,
    'joint': rec['joint'],
    'joint_diff_vs_stored': abs(
        rec['joint'] - tm['defended_triple']['joint']),
    'worst_null': wn,
    'worst_null_diff': abs(
        wn - tm['defended_triple']['worst_null']),
    'adversary_depth': adv_depth,
    'adversary_depth_diff': abs(
        adv_depth - tm['defended_triple']['adversary_depth']),
    'pen_diff': abs(rec['pen'] - tm['pen']),
    'six_gate': six_gate,
    'six_stored': six_stored,
    'six_diffs': {k: abs(six_gate[k] - six_stored[k])
                  for k in six_stored},
    'node': {str(k): v for k, v in node.items()},
    'frame_invariance': {
        str(i): {'sec_sampled_eq_typeI':
                 node[i]['sec'] == node[i]['sec_typeI'],
                 'dec_sampled_eq_typeI':
                 node[i]['dec'] == node[i]['dec_typeI']}
        for i in (7, 10, 11)},
    'defended': bool(rec['joint'] >= 0.0 and wn >= 0.0
                     and adv_depth >= 0.0),
    'deficit6c': P.deficit6c(node),
}
save()
print('G63-B done: six diffs', res['B_member']['six_diffs'],
      'defended', res['B_member']['defended'], flush=True)

# ---------- G63-C: the failing set (tracked nodes) ----------
o_f2 = c482['outputs']['A-F2']['node']
res['C_failing_set'] = {
    'node_diffs_vs_482_AF2': {
        str(i): {ch: abs(node[i][ch] - o_f2[str(i)][ch])
                 for ch in ('sec', 'sec_typeI', 'dec', 'dec_typeI')}
        for i in range(5, 14)},
    'basin': {
        'SEC8': node[8]['sec'], 'SEC9': node[9]['sec'],
        'DEC8': node[8]['dec'], 'DEC9': node[9]['dec'],
        'DEC10': node[10]['dec'],
        'basin_dec_all_positive': bool(
            all(node[i]['dec'] > 0.0 for i in (8, 9, 10))),
    },
}
save()
print('G63-C done: basin SEC8/SEC9', node[8]['sec'], node[9]['sec'],
      'basin DEC all positive',
      res['C_failing_set']['basin']['basin_dec_all_positive'],
      flush=True)

# ---------- G63-D: the gate's own set read of the member ----------
sr = set_read(aux)
res['D_set_read'] = sr
res['D_crosscheck'] = {
    k: {'gate_aux': sr[k]['set_min'],
        'screen_rec': rec[k + '_min'],
        'diff': abs(sr[k]['set_min'] - rec[k + '_min'])}
    for k in ('nec', 'wec', 'dec', 'sec', 'rho')}
headroom_gate = sr['sec']['set_min'] - res['A_base']['screen']['sec_min']
res['D_sec_residue'] = {
    'gate_value': sr['sec']['set_min'],
    'phase_value': -6.792039324408745e-06,
    'diff': abs(sr['sec']['set_min'] - (-6.792039324408745e-06)),
    'node': sr['sec']['node'], 'r': sr['sec']['r'],
    'argmin_typeI': sr['sec']['argmin_typeI'],
    'typeI_set_min': sr['sec']['set_min_typeI'],
    'headroom_gate': headroom_gate,
    'headroom_preregistered': 1.409304255259e-09,
    'headroom_diff': abs(headroom_gate - 1.409304255259e-09),
    'negative_sec_nodes': [
        {'node': i, 'r': NODES[i], 'sec': sr['sec']['node_min'][i]}
        for i in range(len(NODES)) if sr['sec']['node_min'][i] < 0.0],
}
save()
print('G63-D done: sec set min', sr['sec']['set_min'],
      'at node', sr['sec']['node'], 'r', sr['sec']['r'],
      'typeI', sr['sec']['argmin_typeI'],
      'headroom', headroom_gate, flush=True)

# ---------- G63-E: mechanism consistency (stored records) ----------
e = {'arms_x_identical_fit': {}, 'arms_x_identical_confirm': {},
     'lp_vs_exact': {}, 'round1_exact_d6c': {}}
for rung in ('F0', 'F1', 'F2'):
    e['arms_x_identical_fit'][rung] = bool(
        f482['arms']['A']['rungs'][rung]['best']['x']
        == f482['arms']['B']['rungs'][rung]['best']['x'])
    e['arms_x_identical_confirm'][rung] = bool(
        c482['outputs'][f'A-{rung}']['x']
        == c482['outputs'][f'B-{rung}']['x'])
    for arm in ('A', 'B'):
        r1 = f482['arms'][arm]['rungs'][rung]['rounds'][0]
        e['lp_vs_exact'][f'{arm}-{rung}'] = abs(
            r1['lp_t'] - r1['exact_d6c'])
        e['round1_exact_d6c'][f'{arm}-{rung}'] = r1['exact_d6c']
e['lp_vs_exact_F2'] = e['lp_vs_exact']['A-F2']
e['member_dx_max'] = max(abs(v) for v in tm['x'])
e['census'] = c482['candidate_census']
res['E_mechanism'] = e
save()
print('G63-E done: F2 lp_vs_exact', e['lp_vs_exact_F2'],
      'dx_max', e['member_dx_max'], flush=True)
print('ALL READS COMPLETE', flush=True)
