#!/usr/bin/env python3
"""
g16_check.py -- GATE-16 checker (recovery coordinator, 2026-11-23).

Re-derives every deciding number of the Gate-16 verdicts from the
gate's OWN results (gate16/results/wa_results.json) and compares
against (a) the registered claim values in phase128/CHECKPOINT128.md
and phase128/results/p128{1,2}_results.json (the phase's stored
reads), and (b) the registered bars (Pareto clauses, Frontier A,
vacuity fence). The gate does not pass on the phase's checkers:
this script reads only the gate's results + the stored claim values.

Tolerances: legality fractions are counts/56 (exact, tol 1e-12);
EoM reads tol 2e-6 (the registered machinery tolerance is 1e-6;
the gate's fresh machinery reproduced the corpus at 8.55e-12);
shares quoted rounded in the checkpoint tol 2e-3.
"""
import json
import os
import sys

W = '/home/hatch/workspace/warp-pilot'
G = json.load(open(os.path.join(W, 'gate16/results/wa_results.json')))
P1 = json.load(open(os.path.join(W, 'phase128/results/p1281_results.json')))
P2 = json.load(open(os.path.join(W, 'phase128/results/p1282_results.json')))

checks = []


def ck(name, ok, detail=''):
    checks.append(dict(name=name, pass_=bool(ok), detail=str(detail)))


def close(a, b, tol):
    return a is not None and b is not None and abs(a - b) <= tol


H = G['hinge']
R1 = G['p1281_best']
R2 = G['p1282_best']
RT = G['p1282_targeted']

# ---- machinery gate -------------------------------------------------
mg = G['machinery_gate']
ck('machinery_pass', mg['pass_'] is True)
ck('machinery_worst_err<=1e-6', mg['worst_err'] <= 1e-6, mg['worst_err'])
ck('machinery_7of7_rows', all(r['pass_'] for r in mg['rows'])
   and len(mg['rows']) == 7)
ck('hinge_alignment_is_{44}', mg['hinge_alignment_set'] == [44])
ck('hinge_SF_eq_1', close(mg['hinge_SF'], 1.0, 1e-12), mg['hinge_SF'])

# ---- hinge best, gate's own reads vs registered ---------------------
ck('hinge_subset_legal', close(H['subset_legal'], 0.5892857142857143, 1e-12),
   H['subset_legal'])
ck('hinge_subset_legal_full', close(H['subset_legal_full'],
                                    0.5892857142857143, 1e-12))
ck('hinge_eom_max', close(H['eom_rel_max_nondeg'], 0.9999999999784565, 2e-6),
   H['eom_rel_max_nondeg'])
ck('hinge_eom_med', close(H['eom_rel_med_nondeg'], 0.22437629566157347, 2e-6),
   H['eom_rel_med_nondeg'])
ck('hinge_health_False', H['health_ok'] is False)
ck('hinge_frontier_0', H['frontier_A'] == 0.0)
ck('hinge_n_nondeg_56', H['n_nondeg'] == 56 and H['n_deg'] == 0)
ck('hinge_max_point_44', H['max_resid_point'] == 44)
ck('hinge_health_fails_on_cr2_only',
   H['H_min'] > 0 and H['PX_min'] > 0 and H['cr2_max'] > 1,
   (H['H_min'], H['PX_min'], H['cr2_max']))

# ---- G16-1: composed escapes ----------------------------------------
b1 = P1['best']
ck('g161_z_matches_stored', R1['z'] == b1['z'])
ck('g161_subset_legal', close(R1['subset_legal'], 0.9285714285714286, 1e-12),
   R1['subset_legal'])
ck('g161_subset_legal_full',
   close(R1['subset_legal_full'], 0.9464285714285714, 1e-12),
   R1['subset_legal_full'])
ck('g161_eom_max_vs_phase', close(R1['eom_rel_max_nondeg'],
                                  b1['eom_rel_max_nondeg'], 2e-6),
   R1['eom_rel_max_nondeg'])
ck('g161_eom_max_strictly_below_hinge',
   R1['eom_rel_max_nondeg'] < H['eom_rel_max_nondeg'])
ck('g161_eom_max_move_size',
   close(H['eom_rel_max_nondeg'] - R1['eom_rel_max_nondeg'], 1.9e-5, 5e-6),
   H['eom_rel_max_nondeg'] - R1['eom_rel_max_nondeg'])
ck('g161_median_worsened',
   close(R1['eom_rel_med_nondeg'], 0.47963896879690177, 2e-6)
   and R1['eom_rel_med_nondeg'] > H['eom_rel_med_nondeg'],
   R1['eom_rel_med_nondeg'])
ck('g161_pareto_clause1', G['comparisons']['p1281_vs_hinge']['pareto_clause1'])
ck('g161_pareto_clause2', G['comparisons']['p1281_vs_hinge']['pareto_clause2'])
ck('g161_frontier_0', R1['frontier_A'] == 0.0)
ck('g161_not_a_pass', not (R1['frontier_A'] > 0))
ck('g161_health_False', R1['health_ok'] is False)
ck('g161_health_fails_on_cr2_only',
   R1['H_min'] > 0 and R1['PX_min'] > 0 and R1['cr2_max'] > 1,
   (R1['H_min'], R1['PX_min'], R1['cr2_max']))
ck('g161_alignment_empty', R1['alignment_set'] == [])
ck('g161_trap_not_firing', R1['trap_fires'] is False
   and R1['Fsum_maxabs'] > 1e-9)
ck('g161_max_point_44', R1['max_resid_point'] == 44)
ck('g161_Hphi_at_pi0_exact_zero', R1['Hphi_at_pi0'] == 0.0)
d1 = R1['max_resid_decomp']
ck('g161_tFB_share_0.882', close(d1['shares']['FB'], 0.881882, 2e-3),
   d1['shares']['FB'])
ck('g161_tkin_share_0.118', close(d1['shares']['kin'], 0.118079, 2e-3),
   d1['shares']['kin'])
ck('g161_tFA_at_44_tiny', abs(R1['tFA_at_44']) < 1e-5, R1['tFA_at_44'])
ck('g161_kin_same_sign_as_FB_at_44',
   d1['t_kin'] > 0 and d1['t_FB'] > 0)
ck('g161_n_nondeg_56', R1['n_nondeg'] == 56 and R1['n_deg'] == 0)
ck('g161_Fsum_matches_phase', close(R1['Fsum_maxabs'], b1['Fsum_maxabs'], 1e-9))

# ---- G16-2: sign-targeted blend, best candidate ---------------------
b2 = P2['best']
ck('g162_z_matches_stored', R2['z'] == b2['z'])
ck('g162_subset_legal', close(R2['subset_legal'], 0.7857142857142857, 1e-12),
   R2['subset_legal'])
ck('g162_eom_max_vs_phase', close(R2['eom_rel_max_nondeg'],
                                  b2['eom_rel_max_nondeg'], 2e-6),
   R2['eom_rel_max_nondeg'])
ck('g162_eom_max_move',
   close(H['eom_rel_max_nondeg'] - R2['eom_rel_max_nondeg'], 1.94e-3, 1e-4),
   H['eom_rel_max_nondeg'] - R2['eom_rel_max_nondeg'])
ck('g162_median_improved',
   close(R2['eom_rel_med_nondeg'], b2['eom_rel_med_nondeg'], 2e-6)
   and R2['eom_rel_med_nondeg'] < H['eom_rel_med_nondeg'],
   R2['eom_rel_med_nondeg'])
ck('g162_all_three_coordinates',
   R2['subset_legal'] > H['subset_legal']
   and R2['eom_rel_max_nondeg'] < H['eom_rel_max_nondeg']
   and R2['eom_rel_med_nondeg'] < H['eom_rel_med_nondeg'])
ck('g162_pareto_clause1', G['comparisons']['p1282_vs_hinge']['pareto_clause1'])
ck('g162_pareto_clause2', G['comparisons']['p1282_vs_hinge']['pareto_clause2'])
ck('g162_frontier_0', R2['frontier_A'] == 0.0)
ck('g162_health_False', R2['health_ok'] is False)
ck('g162_health_fails_on_cr2_only',
   R2['H_min'] > 0 and R2['PX_min'] > 0 and R2['cr2_max'] > 1,
   (R2['H_min'], R2['PX_min'], R2['cr2_max']))
ck('g162_cr2_max_value', close(R2['cr2_max'], 1.0027937778741982, 1e-6),
   R2['cr2_max'])
ck('g162_p2_positive', R2['z'][6] > 0, R2['z'][6])
ck('g162_alignment_empty', R2['alignment_set'] == [])
ck('g162_trap_not_firing', R2['trap_fires'] is False)
ck('g162_best_not_targeted_named_1of4',
   R2['target_named']['n_opposed'] == 1, R2['target_named']['n_opposed'])
ck('g162_best_opposed_point_is_44',
   R2['target_named']['detail']['44']['opposed'] is True
   and not any(R2['target_named']['detail'][str(p)]['opposed']
               for p in (50, 51, 52)))
ck('g162_best_max_point_52', R2['max_resid_point'] == 52)
d2 = R2['max_resid_decomp']
ck('g162_kin_pin_at_52_shares',
   close(d2['shares']['kin'], 0.843, 2e-3)
   and close(d2['shares']['FB'], 0.156, 2e-3),
   (d2['shares']['kin'], d2['shares']['FB']))
ck('g162_kin_same_sign_FB_at_52', d2['t_kin'] * d2['t_FB'] > 0)

# ---- G16-2: the migration read (targeted candidate, start 5) --------
tg = P2['targeted_candidate']
ck('g162t_z_matches_stored', RT['z'] == tg['z'])
ck('g162t_subset_legal', close(RT['subset_legal'], 0.5357142857142857, 1e-12),
   RT['subset_legal'])
ck('g162t_eom_max_vs_phase', close(RT['eom_rel_max_nondeg'],
                                   tg['eom_rel_max_nondeg'], 2e-6),
   RT['eom_rel_max_nondeg'])
opp = {int(p) for p, v in RT['target_named']['detail'].items() if v['opposed']}
ck('g162t_opposed_exactly_50_51_52', opp == {50, 51, 52}, opp)
ck('g162t_44_not_opposed',
   RT['target_named']['detail']['44']['opposed'] is False)
ck('g162t_worst_point_migrated_to_44', RT['max_resid_point'] == 44)
dt = RT['max_resid_decomp']
ck('g162t_FB_pin_at_44_shares',
   close(dt['shares']['FB'], 0.854, 2e-3)
   and close(dt['shares']['kin'], 0.064, 2e-3),
   (dt['shares']['FB'], dt['shares']['kin']))
ck('g162t_frontier_0', RT['frontier_A'] == 0.0)

# ---- coverage law, hinge side ---------------------------------------
ck('hinge_named_opposed_50_51_52',
   all(H['target_named']['detail'][str(p)]['opposed'] for p in (50, 51, 52)))
ck('hinge_44_uncovered_kin_dead',
   H['target_named']['detail']['44']['live'] is False
   and abs(H['target_named']['detail']['44']['t_kin']) < 1e-30)

# ---- verdict-form logic ----------------------------------------------
def improvement(r):
    return (r['subset_legal'] >= H['subset_legal']
            and r['eom_rel_max_nondeg'] < H['eom_rel_max_nondeg']) or \
           (r['subset_legal'] > H['subset_legal']
            and r['eom_rel_max_nondeg'] <= H['eom_rel_max_nondeg'])


ck('verdict_g161_joint_improvement', improvement(R1))
ck('verdict_g162_joint_improvement', improvement(R2))
ck('verdict_no_joint_pass_anywhere',
   all(G[s]['frontier_A'] == 0.0
       for s in ('hinge', 'p1281_best', 'p1282_best', 'p1282_targeted')))

npass = sum(c['pass_'] for c in checks)
out = dict(n_checks=len(checks), n_pass=npass, checks=checks)
with open(os.path.join(W, 'gate16/results/g16_check_output.json'), 'w') as f:
    json.dump(out, f, indent=1)
for c in checks:
    print(('PASS' if c['pass_'] else 'FAIL'), c['name'],
          ('| ' + c['detail']) if (c['detail'] and not c['pass_']) else '')
print(f'TOTAL {npass}/{len(checks)} PASS')
sys.exit(0 if npass == len(checks) else 1)
