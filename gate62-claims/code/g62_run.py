#!/usr/bin/env python3
"""
g62_run.py -- Gate-62 driver: independent
re-judgement of Phase 479's member at the
wide pose. Registration:
work/g62_registration.md (filed before
any Gate-62 computation); charge: ledger
entry 1251.

The gate drives the lineage machinery
itself (p479_lib -> p474_lib -> p460_lib
-> p449_lib; SET-244 / SAMPLER-M,
float64, VM, Phase-166 pin) and computes
the set read (SS G62-D) from the read's
per-point record in its own code.
Results are checkpointed to
results/g62_results.json after each
read.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, os.path.join(WP, 'phase479/work'))

import p479_lib as P  # noqa: E402

L = P.L
DTYPE = P.DTYPE
NODES = [float(r) for r in P.NODES]
OUT = os.path.join(HERE, '..', 'results', 'g62_results.json')

W474B_CHARGED = [0.0, -0.0014031443466063713, 0.0, 0.0,
                 -0.0013795539861294259, 0.0, 0.0,
                 -0.002009452499039281, 0.0]

res = {'gate': 'Gate-62', 'charge_entry': 1251}


def save():
    with open(OUT, 'w') as f:
        json.dump(res, f, indent=1)


def diffs(rec, stored, fields):
    return {k: (abs(rec[k] - stored[k])
                if isinstance(stored[k], (int, float))
                and not isinstance(stored[k], bool)
                else (0.0 if rec[k] == stored[k] else None))
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
    set minimum with its locus."""
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
c479 = json.load(open(os.path.join(
    WP, 'phase479/results/p479_confirmations.json')))
v479 = c479['verdict']
f479 = json.load(open(os.path.join(
    WP, 'phase479/results/p479_fit.json')))
c474 = json.load(open(os.path.join(
    WP, 'phase474/results/p474_confirmations.json')))
f474 = json.load(open(os.path.join(
    WP, 'phase474/results/p474_fit.json')))
res['stored_member_x'] = v479['x']

# ---------- G62-A: the base ----------
x_base = np.zeros(27, dtype=DTYPE)
rec, read, aux, node = P.read_object(x_base, stage='G62-A')
wn, wf, adv = instruments(x_base, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
res['A_base'] = {
    'screen': rec,
    'diffs_vs_BASE_REC': diffs(rec, P.BASE_REC, P.DECIDING_FIELDS),
    'worst_null': wn, 'worst_null_fib': wf,
    'worst_null_diff': abs(wn - P.BASE_WORST_NULL),
    'adversary_depth': adv_depth,
    'adversary_depth_diff': abs(adv_depth - P.BASE_ADV_DEPTH),
    'node': {str(k): v for k, v in node.items()},
}
save()
print('G62-A done: max screen diff',
      max(v for v in res['A_base']['diffs_vs_BASE_REC'].values()
          if v is not None), flush=True)

# ---------- G62-B: the member ----------
x_member = np.zeros(27, dtype=DTYPE)
x_member[9:18] = W474B_CHARGED
res['member_x_gate'] = x_member.tolist()
res['member_x_matches_stored'] = bool(
    x_member.tolist() == v479['x'])
rec, read, aux, node = P.read_object(x_member, stage='G62-B')
wn, wf, adv = instruments(x_member, read, aux)
adv_depth = adv['in_region_worst_nec_SAMPLER-M']
six_gate = P.six_values(node)
six_stored = v479['six']
res['B_member'] = {
    'screen': rec,
    'joint': rec['joint'],
    'joint_diff_vs_stored': abs(rec['joint']
                                - v479['defended_triple']['joint']),
    'worst_null': wn,
    'worst_null_diff': abs(wn - v479['defended_triple']['worst_null']),
    'adversary_depth': adv_depth,
    'adversary_depth_diff': abs(
        adv_depth - v479['defended_triple']['adversary_depth']),
    'pen_diff': abs(rec['pen'] - v479['pen']),
    'six_gate': six_gate,
    'six_stored': six_stored,
    'six_diffs': {k: abs(six_gate[k] - six_stored[k]) for k in six_stored},
    'node': {str(k): v for k, v in node.items()},
    'frame_invariance': {
        str(i): {'sec_sampled_eq_typeI':
                 node[i]['sec'] == node[i]['sec_typeI'],
                 'dec_sampled_eq_typeI':
                 node[i]['dec'] == node[i]['dec_typeI']}
        for i in (8, 9, 10)},
    'defended': bool(rec['joint'] >= 0.0 and wn >= 0.0
                     and adv_depth >= 0.0),
    'deficit6': P.deficit6(node),
}
save()
print('G62-B done: six diffs', res['B_member']['six_diffs'],
      'defended', res['B_member']['defended'], flush=True)

# ---------- G62-D: the gate's own set read of the member ----------
sr = set_read(aux)
res['D_set_read'] = sr
res['D_crosscheck'] = {
    k: {'gate_aux': sr[k]['set_min'],
        'screen_rec': rec[k + '_min'],
        'diff': abs(sr[k]['set_min'] - rec[k + '_min'])}
    for k in ('nec', 'wec', 'dec', 'sec', 'rho')}
res['D_sec_residue'] = {
    'gate_value': sr['sec']['set_min'],
    'phase_value': -6.459908493210403e-06,
    'diff': abs(sr['sec']['set_min'] - (-6.459908493210403e-06)),
    'node': sr['sec']['node'], 'r': sr['sec']['r'],
    'argmin_typeI': sr['sec']['argmin_typeI'],
    'node25_sec_sampled': sr['sec']['node_min'][25],
}
save()
print('G62-D done: sec set min', sr['sec']['set_min'],
      'at node', sr['sec']['node'], 'r', sr['sec']['r'],
      'typeI', sr['sec']['argmin_typeI'], flush=True)

# ---------- G62-C: the non-vacuity control (474's F1) ----------
x_f1 = np.asarray(f474['rungs']['F1']['best']['x'], dtype=DTYPE)
rec1, read1, aux1, node1 = P.read_object(x_f1, stage='G62-C')
stored_f1_screen = c474['confirmations']['F1']['screen']
stored_f1_nodesec = c474['confirmations']['F1']['nodesec']
six_f1 = P.six_values(node1)
res['C_f1'] = {
    'screen': rec1,
    'diffs_vs_474_F1_screen': diffs(rec1, stored_f1_screen,
                                    P.DECIDING_FIELDS),
    'node_sec_gate': {str(i): node1[i]['sec'] for i in (8, 9, 10)},
    'node_sec_stored': {str(i): stored_f1_nodesec[str(i)]['sampled']
                        for i in (8, 9, 10)},
    'node_sec_diffs': {
        str(i): abs(node1[i]['sec']
                    - stored_f1_nodesec[str(i)]['sampled'])
        for i in (8, 9, 10)},
    'node10_dec_gate': node1[10]['dec'],
    'screen_dec_min_gate': rec1['dec_min'],
    'dec_target': -5.375277493220288e-04,
    'node10_dec_diff': abs(node1[10]['dec']
                           - (-5.375277493220288e-04)),
    'six_on_F1': six_f1,
    'excluded': bool(all(six_f1[f'SEC{i}'] >= 0.0 for i in (8, 9, 10))
                     and six_f1['DEC10'] < 0.0),
}
save()
print('G62-C done: node10 DEC', node1[10]['dec'],
      'excluded', res['C_f1']['excluded'], flush=True)

# ---------- G62-E: mechanism consistency (stored records) ----------
e = {'arms_x_identical_fit': {}, 'arms_x_identical_confirm': {},
     'lp_vs_exact': {}}
for rung in ('F0', 'F1', 'F2'):
    e['arms_x_identical_fit'][rung] = bool(
        f479['arms']['A']['rungs'][rung]['best']['x']
        == f479['arms']['B']['rungs'][rung]['best']['x'])
    e['arms_x_identical_confirm'][rung] = bool(
        c479['confirmations']['A'][rung]['x']
        == c479['confirmations']['B'][rung]['x'])
    for arm in ('A', 'B'):
        r1 = f479['arms'][arm]['rungs'][rung]['rounds'][0]
        e['lp_vs_exact'][f'{arm}-{rung}'] = abs(
            r1['lp_t'] - r1['exact_d6'])
e['lp_vs_exact_max'] = max(e['lp_vs_exact'].values())
e['member_dx_max'] = max(abs(v) for v in W474B_CHARGED)
res['E_mechanism'] = e
save()
print('G62-E done: lp_vs_exact_max', e['lp_vs_exact_max'], flush=True)
print('ALL READS COMPLETE', flush=True)
