"""
wc_check.py — W-C checker: evaluates Phase-50 Bars 1-4 + the machinery
cross-check from results/wc_g73_numbers.json (checker-over-results per
the optimisation directive). Prints PASS/FAIL per bar with the numbers.
"""
import json

res = json.load(open('/home/hatch/workspace/warp-pilot/gate7/results/wc_g73_numbers.json'))
v1 = res['verdict_h0.0375']
v2 = res['verdict_h0.01875']
sp = res['secondpath_order4_h0.0375']

bars = {}
bars['hash_gate'] = res['step0_hash_gate']['all_match']
bars['fidelity'] = res['step1_fidelity']['pass']

# Bar 1: Type-I fraction 1.000 over significant points, both spacings
bars['bar1'] = all(v[reg]['typeI_frac'] == 1.0 and v[reg]['n_non_typeI'] == 0
                   for v in (v1, v2) for reg in ('all_sig', 'shell'))

# Bar 2: worst margins > 0 both spacings, sign-stable, worst >= 3x FD floor
def bar2(v):
    fl = v['fd_floor_median_abs_nec_nonsig']
    return {k: v['shell'][k] for k in ('nec', 'wec', 'sec', 'dec')}, v['shell']['worst'], fl, v['shell']['worst'] / fl
m1, w1, f1, r1 = bar2(v1)
m2, w2, f2, r2 = bar2(v2)
bars['bar2_detail'] = {'h0.0375': {'margins': m1, 'worst': w1, 'floor': f1, 'worst_over_floor': r1},
                       'h0.01875': {'margins': m2, 'worst': w2, 'floor': f2, 'worst_over_floor': r2}}
bars['bar2'] = all(x > 0 for x in list(m1.values()) + list(m2.values())) and r1 >= 3 and r2 >= 3

# Bar 3: sampled-null NEC min > 0 on the shell, both spacings
bars['bar3_detail'] = {'h0.0375': v1['shell']['sampled_nec_min'],
                       'h0.01875': v2['shell']['sampled_nec_min']}
bars['bar3'] = v1['shell']['sampled_nec_min'] > 0 and v2['shell']['sampled_nec_min'] > 0

# Bar 4: second path (4th-order, h=0.0375) agrees on sign of every deciding margin
spm = {k: sp['shell'][k] for k in ('nec', 'wec', 'sec', 'dec')}
bars['bar4_detail'] = {'margins': spm, 'worst': sp['shell']['worst'],
                       'typeI_frac': sp['shell']['typeI_frac'],
                       'sampled_nec_min': sp['shell']['sampled_nec_min']}
bars['bar4'] = (all(x > 0 for x in spm.values()) and sp['shell']['typeI_frac'] == 1.0
                and sp['shell']['sampled_nec_min'] > 0)

cc = res.get('step3_crosscheck', {})
bars['crosscheck'] = {'his': cc.get('his_interval_value'),
                      'exact_opt_finest_h': cc.get('exact_opt_finest_h'),
                      'rel_dev': cc.get('rel_dev_from_his'),
                      'within_25pct': cc.get('within_25pct')}
bars['crosscheck_pass'] = bool(cc.get('within_25pct'))

bars['VERDICT'] = ('CONFIRMED AT OUR BARS' if all(
    bars[k] for k in ('hash_gate', 'fidelity', 'bar1', 'bar2', 'bar3', 'bar4', 'crosscheck_pass'))
    else 'NOT CONFIRMED — see detail')
print(json.dumps(bars, indent=1, default=float))
