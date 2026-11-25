"""
wa_check.py — Gate-10 W-A checker: recomputes the G10-1 pass/fail
from results/wa_g101_numbers.json against the bars registered in
GATE10.md. Run: ~/workspace/warp-pilot/venv/bin/python wa_check.py
"""
import json

D = json.load(open('/home/hatch/workspace/warp-pilot/gate10/results/wa_g101_numbers.json'))
checks = []


def ck(name, ok, detail):
    checks.append({'check': name, 'pass': bool(ok), 'detail': detail})


# anchors
ck('anchor_i_minkowski', D['anchor_i_minkowski_maxAbsG'] < 1e-12,
   f"max|G| = {D['anchor_i_minkowski_maxAbsG']:.3e} (bar < 1e-12)")
ck('anchor_ii_rho', D['anchor_ii_max_rho_rel_err'] <= 3e-3,
   f"max rho rel err {D['anchor_ii_max_rho_rel_err']:.3e} (bar 3e-3)")
ck('anchor_ii_p', D['anchor_ii_max_p_abs_err'] <= 3e-7,
   f"max p abs err {D['anchor_ii_max_p_abs_err']:.3e} (bar 3e-7)")
ck('anchor_iii_calibration', D['anchor_iii_payload_rel_err_vs_0.07292'] <= 1e-4,
   f"held payload {D['anchor_iii_calibration']['payload_relat']:.8f} vs 0.07292, "
   f"rel err {D['anchor_iii_payload_rel_err_vs_0.07292']:.2e} (bar 1e-4)")
ctl = D['anchor_iv_control_audit']
ck('anchor_iv_typeI', ctl['typeI_frac_sig'] == 1.0, f"control Type-I {ctl['typeI_frac_sig']}")
fac = D['anchor_iv_control_factor_vs_gate8']
ck('anchor_iv_inner_factor3', 1 / 3 <= fac['inner_wall'] <= 3,
   f"inner factor {fac['inner_wall']:.2f} vs Gate-8 +9.79e-4")
ck('anchor_iv_outer_factor3', 1 / 3 <= fac['outer_wall'] <= 3,
   f"outer factor {fac['outer_wall']:.2f} vs Gate-8 +4.05e-5")
exc = D['anchor_iv_payload_exception']
ck('anchor_iv_payload_at_gate8_site_factor3', 1 / 3 <= exc['factor_at_gate8_site'] <= 3,
   f"payload SEC at Gate-8 site r=1.4317: {exc['this_path_sec_at_gate8_site']:+.4e} "
   f"(factor {exc['factor_at_gate8_site']:.2f} vs +1.09e-4); region worst "
   f"{exc['this_path_payload_region_worst']:+.4e} vs gate-standard control read "
   f"+3.86e-6 — significance-borderline exception, see report")
lad = D['anchor_iv_control_cavity_ladder']
mx = max(abs(e['min_dec_near_edge_shell_4.6_5']) for e in lad.values())
ck('anchor_iv_cavity_floor', mx <= 2.3e-4 and all(e['typeI_frac'] == 1.0 for e in lad.values()),
   f"control cavity shell |DEC| max {mx:.2e} across ladder (Gate-8 floor bound 2.3e-4), Type-I 1.000")

# deciding bars
e = D['deciding_economics_rel_err']
ck('bar_a_economics', e['payload_vs_0.08745'] <= 1e-4 and e['Wsum_vs_0.15931'] <= 1e-3
   and e['W_held_max_rel_err'] <= 1e-12,
   f"payload rel err {e['payload_vs_0.08745']:.2e} (bar 1e-4); W sum rel err "
   f"{e['Wsum_vs_0.15931']:.2e}; held-W err {e['W_held_max_rel_err']:.1e}")
dec = D['deciding_audit']
ck('bar_b_typeI', dec['typeI_frac_sig'] == 1.0, f"deciding Type-I {dec['typeI_frac_sig']}")
PHASE = {'payload': 3.85e-6, 'inner_wall': 1.188e-3, 'outer_wall': 3.20e-5, 'exterior': 1.04e-6}
for reg, pv in PHASE.items():
    w = dec['regions'][reg]['worst']
    ck(f'bar_c_{reg}', w > 0 and 1 / 3 <= w / pv <= 3,
       f"{reg} worst {w:+.4e} vs phase {pv:+.2e} (factor {w/pv:.2f})")
ck('bar_d_sampled_null', dec['min_sampled_nec_all_sig'] > 0,
   f"sampled-null min {dec['min_sampled_nec_all_sig']:+.4e}")
cav = D['deciding_cavity_settlement']
s53 = cav['site_4.53_162dir']['min_dec']
ck('bar_e_cavity_site_clean', s53 >= 0,
   f"analytic DEC at r=4.53 (162 dirs) {s53:+.4e} >= 0 — stronger settlement form (i)")
lad2 = cav['radial_density_ladder']
mx2 = max(abs(x['min_dec_near_edge_shell_4.6_5']) for x in lad2.values())
ck('bar_e_cavity_no_convergent_negative', mx2 <= 5e-7,
   f"deciding cavity ladder shell |DEC| max {mx2:.2e} (floor level; no convergent negative value)")
cor = D['corroboration_row']['audit']
regs_pos = all(cor['regions'][r]['worst'] > 0 for r in ('payload', 'inner_wall', 'outer_wall', 'exterior'))
ck('bar_f_corroboration', cor['typeI_frac_sig'] == 1.0 and regs_pos
   and abs(D['corroboration_row']['economics']['payload_relat'] - 0.08104) / 0.08104 <= 1e-3,
   f"0.08104 row: Type-I {cor['typeI_frac_sig']}, payload "
   f"{D['corroboration_row']['economics']['payload_relat']:.8f}, non-cavity region worsts > 0: {regs_pos}")

npass = sum(c['pass'] for c in checks)
out = {'n_checks': len(checks), 'n_pass': npass, 'all_pass': npass == len(checks), 'checks': checks}
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate10/results/wa_check.json', 'w'), indent=1)
for c in checks:
    print(f"[{'PASS' if c['pass'] else 'FAIL'}] {c['check']}: {c['detail']}")
print(f"{npass}/{len(checks)} PASS")
