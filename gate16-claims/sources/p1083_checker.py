#!/usr/bin/env python3
"""p1083_checker.py -- independent checker for P108-3.
Recomputes every verdict-carrying number from the raw corpus
(phase101/results/p1015_partB_raw.json) with its own loop-based
set-membership implementation, and compares against
phase108/results/p1083_results.json. Does not import the main
script. Exit code 0 iff all checks pass."""
import sys, json
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase101/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase76')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase18')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase48')
import p1015_lib as H
import p761_lib as L

raw = json.load(open('/home/hatch/workspace/warp-pilot/phase101/results/p1015_partB_raw.json'))
res = json.load(open('/home/hatch/workspace/warp-pilot/phase108/results/p1083_results.json'))
wall = L.Wall(1.1)
pts = wall.pts_sub

SOURCES = {
    'A76_mu0': raw['direct']['A76_mu0'], 'B76_mu0': raw['direct']['B76_mu0'],
    'runs_A0': raw['runs_A'][0], 'runs_A1': raw['runs_A'][1],
    'runs_B0': raw['runs_B'][0], 'runs_B1': raw['runs_B'][1],
    'runs_B2': raw['runs_B'][2],
}
npass = nfail = 0


def check(name, cond):
    global npass, nfail
    if cond:
        npass += 1
    else:
        nfail += 1
        print('FAIL:', name)


def member_set(z, sf_thr, kin_thr):
    ct = H.canonical_terms(wall, pts, np.asarray(z, float))
    out = []
    info = {}
    for i in range(56):
        t = [float(ct['t_kin'][i]), float(ct['t_pxx'][i]),
             float(ct['t_FA'][i]), float(ct['t_FB'][i])]
        D = sum(abs(x) for x in t)
        if D < 1e-9:
            continue
        info[i] = (t, D, abs(sum(t)) / (D + 1e-12))
        mx = max(abs(x) for x in t)
        live = abs(t[2]) >= 1e-6 * mx and abs(t[3]) >= 1e-6 * mx
        same = (t[2] > 0 and t[3] > 0) or (t[2] < 0 and t[3] < 0)
        SF = (abs(t[2]) + abs(t[3])) / D
        if live and same and SF >= sf_thr and abs(t[0]) / D <= kin_thr:
            out.append(i)
    return out, info


check('seven configs in results', len(res['configs']) == 7)
check('best_A duplicate identified',
      res['duplicates_identified']['best_A_equals_runs_A1'] is True
      and raw['best_A']['z'] == raw['runs_A'][1]['z'])
check('best_B duplicate identified',
      res['duplicates_identified']['best_B_equals_runs_B1'] is True
      and raw['best_B']['z'] == raw['runs_B'][1]['z'])
check('no machinery failure recorded', res['machinery_failure_configs'] == [])

for c in res['configs']:
    lab = c['label']
    rec = SOURCES[lab]
    check(f'{lab}: z matches raw', c['z'] == [float(x) for x in rec['z']])
    members, info = member_set(rec['z'], 0.90, 1e-6)
    rels = {i: v[2] for i, v in info.items()}
    emax = max(rels.values())
    emed = float(np.median(list(rels.values())))
    check(f'{lab}: EoM max reproduced within 1e-6',
          abs(emax - rec['eom_rel_max_nondeg']) <= 1e-6
          and abs(c['eom_max_recomputed'] - emax) <= 1e-9)
    check(f'{lab}: EoM median reproduced within 1e-6',
          abs(emed - rec['eom_rel_med_nondeg']) <= 1e-6
          and abs(c['eom_med_recomputed'] - emed) <= 1e-9)
    check(f'{lab}: n_nondeg matches', len(info) == rec['n_nondeg'] == c['n_nondeg'])
    got = [m['idx'] for m in c['alignment_primary']['members']]
    check(f'{lab}: primary set members match', got == members)
    check(f'{lab}: primary set size matches',
          c['alignment_primary']['size'] == len(members))
    for m in c['alignment_primary']['members']:
        t, D, rel = info[m['idx']]
        check(f'{lab}: member {m["idx"]} terms/S_F/residual match',
              abs(m['t_FA'] - t[2]) <= 1e-12 * max(1, abs(t[2]))
              and abs(m['t_FB'] - t[3]) <= 1e-12 * max(1, abs(t[3]))
              and abs(m['S_F'] - (abs(t[2]) + abs(t[3])) / D) <= 1e-9
              and abs(m['residual_rel'] - rel) <= 1e-9)
    imax = max(rels, key=lambda i: rels[i])
    check(f'{lab}: max-residual point idx matches',
          c['max_residual_point']['idx'] == imax)
    check(f'{lab}: max-residual membership flag matches',
          c['max_residual_point']['in_alignment_set_primary'] == (imax in members))
    for key, (sf, kin) in {'SF=0.8_kin=1e-08': (0.80, 1e-8),
                           'SF=0.8_kin=0.0001': (0.80, 1e-4),
                           'SF=0.95_kin=1e-08': (0.95, 1e-8),
                           'SF=0.95_kin=0.0001': (0.95, 1e-4)}.items():
        ms, _ = member_set(rec['z'], sf, kin)
        check(f'{lab}: sensitivity {key} matches',
              res['configs'][res['configs'].index(c)]['sensitivity'][key]['members'] == ms)
    # sign identity (S1): sign(tFA*tFB) == sign(FA*FB) wherever PX != 0
    ct = H.canonical_terms(wall, pts, np.asarray(rec['z'], float))
    ok = all(np.sign(ct['t_FA'][i] * ct['t_FB'][i]) == np.sign(ct['FA'][i] * ct['FB'][i])
             for i in range(56) if ct['PX'][i] != 0)
    check(f'{lab}: sign identity holds at all points', ok and c['sign_identity_holds_all_points'])

live = [c for c in res['configs'] if c['both_force_channels_live']]
check('five live-channel configs (all runs; direct rows mu=0)',
      len(live) == 5 and all(c['label'].startswith('runs_') for c in live))
expected = ('STRUCTURAL FEATURE'
            if live and all(c['alignment_primary']['size'] > 0 for c in live)
            and all(c['max_residual_point']['in_alignment_set_primary'] for c in live)
            else 'OTHER')
check('verdict follows the registered STRUCTURAL FEATURE form',
      res['verdict'] == expected == 'STRUCTURAL FEATURE')
hinge = next(c for c in res['configs'] if c['label'] == 'runs_B1')
check('hinge best set is exactly {44}', [m['idx'] for m in hinge['alignment_primary']['members']] == [44])

print(f'CHECKER: {npass} passed, {nfail} failed')
sys.exit(0 if nfail == 0 else 1)
