#!/usr/bin/env python3
"""W-D checker: pass/fail over results/wd_g94_numbers.json against the
G9-4 bars registered in GATE9.md. Run with the programme venv python."""
import json, math
N = json.load(open('/home/hatch/workspace/warp-pilot/gate9/results/wd_g94_numbers.json'))
checks = []
def ck(name, ok): checks.append((name, bool(ok)))
a = N['anchors']
ck('anchor Schwarzschild B=0 (<1e-12)', a['schwarzschild_max_abs_B'] < 1e-12)
ck('anchor MK Bach-flat (<1e-9 abs)', a['MK_max_abs_B'] < 1e-9)
ck('anchor T-b closed forms (<1e-9 rel)', a['Tb_closed_form_max_rel_dev'] < 1e-9)
ck('trace symbolic = 0', N['trace_symbolic'] == '0')
ca = N['clause_a_covariance']
ck('(a) covariance dev < 1e-9 at r0=10 and r0=1000',
   max(ca['max_rel_dev_direct_vs_scaled'].values()) < 1e-9)
cb = N['clause_b_increment']
ck('(b) layer upper endpoint within 5% of 1.00348',
   abs(cb['layer_xb'][1]-1.00348)/1.00348 < 0.05)
ck('(b) dNEC1 min within 5% of -0.016680', abs(cb['dNEC1_min_scaled']+0.016680)/0.016680 < 0.05)
ck('(b) failures confined to NEC1/DECr/DECt', set(cb['failing_combos']) == {'NEC1', 'DECr', 'DECt'})
ck('(b) layer price within factor 2 of 5.83e68', 0.5 < cb['layer_price_ratio']/5.83e68 < 2.0)
cc = N['clause_c_pole']
p1 = float(cc['NEC1_probes_40digit']['e^-1(1-1e-3)']); p2 = float(cc['NEC1_probes_40digit']['e^-1(1-1e-6)'])
ck('(c) probe 1e-3 negative, within factor 3', p1 < 0 and 1/3 < abs(p1/6.58e21) < 3)
ck('(c) probe 1e-6 negative, within factor 3', p2 < 0 and 1/3 < abs(p2/6.65e42) < 3)
ck('(c) pole order 7 +- 1', 6.0 <= cc['pole_order_loglog_fit'] <= 8.0)
ck('(c) price bounds within factor 10 of stored', all(0.1 < f < 10 for f in cc['price_factors_vs_stored']))
ck('(c) price bounds strictly increasing as eps->0', cc['strictly_increasing_as_eps->0'])
cd = N['clause_d_rw_check']
ck('(d) Bach = 0 identically on general RW', cd['bach_all_zero'])
ck('(d) Weyl = 0 identically on general RW (fu)', cd['weyl_all_zero_after_fu'])
for nm, ok in checks: print(('PASS' if ok else 'FAIL'), nm)
print(f"{sum(ok for _, ok in checks)}/{len(checks)} PASS")
assert all(ok for _, ok in checks)
