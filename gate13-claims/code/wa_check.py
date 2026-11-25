"""
wa_check.py -- Gate-13 W-A checker over results/wa_g131_numbers.json.
Recomputes every bar verdict (a)-(h) and anchor (i)-(v) from the
stored numbers file only.  Run with the programme venv python.
"""
import json

N = json.load(open('/home/hatch/workspace/warp-pilot/gate13/results/wa_g131_numbers.json'))
checks = []


def ck(name, ok, detail=''):
    checks.append({'check': name, 'pass': bool(ok), 'detail': detail})


def fac(v, ref):
    return v / ref


# anchors
ck('anchor_i_minkowski', N['anchor_i_minkowski_maxAbsG'] < 1e-12,
   f"{N['anchor_i_minkowski_maxAbsG']:.3e}")
ck('anchor_ii_rho', N['anchor_ii_max_rho_rel_err'] <= 3e-3,
   f"{N['anchor_ii_max_rho_rel_err']:.3e}")
ck('anchor_ii_p', N['anchor_ii_max_p_abs_err'] <= 3e-7,
   f"{N['anchor_ii_max_p_abs_err']:.3e}")
a3 = N['anchor_iii_control_span']
ck('anchor_iii_typeI', a3['audit']['typeI_frac_sig'] == 1.0)
ck('anchor_iii_outer_wall_factor3',
   1 / 3 <= a3['factors']['outer_wall_vs_stored'] <= 3,
   f"{a3['factors']['outer_wall_vs_stored']:.3f}")
ck('anchor_iii_conservation_factor3',
   1 / 3 <= a3['factors']['conservation_vs_stored'] <= 3,
   f"{a3['factors']['conservation_vs_stored']:.3f}")
ck('anchor_iii_cavity_site_positive', a3['cavity_site_4.53_26dir']['min_dec'] > 0,
   f"{a3['cavity_site_4.53_26dir']['min_dec']:+.4e}")
a4f = N['anchor_iv_control_factor_vs_gate8']
ck('anchor_iv_typeI', N['anchor_iv_control_audit']['typeI_frac_sig'] == 1.0)
ck('anchor_iv_inner_factor3', 1 / 3 <= a4f['inner_wall'] <= 3, f"{a4f['inner_wall']:.3f}")
ck('anchor_iv_outer_factor3', 1 / 3 <= a4f['outer_wall'] <= 3, f"{a4f['outer_wall']:.3f}")
lad4 = N['anchor_iv_control_cavity_ladder']
ck('anchor_iv_cavity_floor_class',
   all(abs(e['min_dec_near_edge_shell_4.6_5']) <= 2.3e-4 and e['typeI_frac'] == 1.0
       for e in lad4.values()),
   'ladder |DEC| <= 2.3e-4, Type-I 1.0 all rungs')
a5 = N['anchor_v_gate11_row']
ck('anchor_v_payload', abs(a5['economics']['payload_relat'] - 0.0955573263)
   / 0.0955573263 <= 1e-4, f"{a5['economics']['payload_relat']:.10f}")
ck('anchor_v_typeI', a5['audit']['typeI_frac_sig'] == 1.0)
ck('anchor_v_region_factors3',
   all(1 / 3 <= v <= 3 for v in a5['factors_vs_gate11_fresh'].values()),
   json.dumps({k: round(v, 3) for k, v in a5['factors_vs_gate11_fresh'].items()}))
ck('anchor_v_sampled_positive', a5['audit']['min_sampled_nec_all_sig'] > 0,
   f"{a5['audit']['min_sampled_nec_all_sig']:+.4e}")
ck('anchor_v_cavity_site', a5['cavity_site_4.53_162dir']['min_dec'] > 0
   and 1 / 3 <= a5['cavity_site_factor_vs_gate11_class'] <= 3,
   f"{a5['cavity_site_4.53_162dir']['min_dec']:+.4e}")

# deciding bars
ea = N['deciding_economics_rel_err']
ck('bar_a_payload_rel_err', ea['payload_vs_claim'] <= 1e-4, f"{ea['payload_vs_claim']:.2e}")
ck('bar_a_Wsum', ea['Wsum_vs_claim'] <= 1e-4, f"{ea['Wsum_vs_claim']:.2e}")
ck('bar_a_heldW_err_class', ea['W_held_max_rel_err'] <= 1e-14,
   f"{ea['W_held_max_rel_err']:.2e}")
s = N['deciding_audit']
ck('bar_b_typeI', s['typeI_frac_sig'] == 1.0, f"{s['typeI_frac_sig']}")
fdec = N['deciding_factors_vs_phase']
ck('bar_c_region_signs', all(s['regions'][r]['worst'] > 0
                             for r in ('payload', 'inner_wall', 'outer_wall', 'exterior')))
ck('bar_c_region_factors3', all(1 / 3 <= v <= 3 for v in fdec.values()),
   json.dumps({k: round(v, 3) for k, v in fdec.items()}))
ck('bar_d_sampled_null', s['min_sampled_nec_all_sig'] > 0,
   f"{s['min_sampled_nec_all_sig']:+.4e} (162 dirs)")
cav = N['deciding_cavity_settlement']
ck('bar_e_flagged_site_positive', cav['site_4.526829_162dir']['min_dec'] > 0,
   f"{cav['site_4.526829_162dir']['min_dec']:+.4e}")
lad = cav['radial_density_ladder']
ck('bar_e_ladder_no_convergent_negative',
   all(e['typeI_frac'] == 1.0 for e in lad.values())
   and max(abs(e['min_dec_near_edge_shell_4.6_5']) for e in lad.values()) <= 4e-6,
   'ladder minima floor class, Type-I 1.0 all rungs')
cw = cav['deciding_set_cavity_region']['worst']
ck('bar_f_floor_statement_data', cw is not None and abs(cw) <= 4e-6,
   f"deciding-set cavity worst {cw:+.4e}: outside 2e-6, inside 4e-6 and Gate-8 -3.7e-6 class")
ch = N['deciding_chains']
ck('bar_f2_chain_scalars_match',
   abs(ch['outer']['lam'] - ch['outer_stored']['lam']) < 1e-9
   and abs(ch['outer']['S_lo_minus1'] - ch['outer_stored']['S_lo_minus1']) < 1e-9
   and abs(ch['outer']['S_hi'] - ch['outer_stored']['S_hi']) < 1e-9,
   f"S_lo-1 {ch['outer']['S_lo_minus1']:+.4e}, S_hi {ch['outer']['S_hi']:+.4e}")
sf2 = N['residual_sensitivity_factors']
ck('bar_f2_margins_stable', all(0.9 <= v <= 1.1 for v in sf2.values()),
   json.dumps({k: round(v, 4) for k, v in sf2.items()}))
g = N['corroboration_row']
ck('bar_g_payload', abs(g['economics']['payload_relat'] - 0.09118184734247374)
   / 0.09118184734247374 <= 1e-4, f"{g['economics']['payload_relat']:.11f}")
ck('bar_g_typeI_regions', g['audit']['typeI_frac_sig'] == 1.0 and all(
    g['audit']['regions'][r]['worst'] > 0
    for r in ('payload', 'inner_wall', 'outer_wall', 'exterior')))
ck('bar_g_cavity_site', g['cavity']['site_4.53_162dir']['min_dec'] > 0,
   f"{g['cavity']['site_4.53_162dir']['min_dec']:+.4e}")
h10 = N['mechanism_alone']['e0.10']['audit']
h075 = N['mechanism_alone']['e0.075']['audit']
ck('bar_h_e010_legal', h10['typeI_frac_sig'] == 1.0 and h10['worst'] > 0
   and h10['min_sampled_nec_all_sig'] > 0,
   f"Type-I {h10['typeI_frac_sig']}, worst {h10['worst']:+.4e}, "
   f"sampled {h10['min_sampled_nec_all_sig']:+.4e}")
fh = h075['regions']['fringe_hi']
ck('bar_h_e0075_fringe_fails', fh['typeI_frac'] < 1.0
   and fh['min_sampled_nec_all'] < 0 and 0.7 <= fh['typeI_frac'] <= 0.95,
   f"fringe_hi Type-I {fh['typeI_frac']:.3f}, sampled {fh['min_sampled_nec_all']:+.4e}")
ck('bar_h_e0075_interior_clean', h075['regions']['interior']['typeI_frac'] == 1.0)

out = {'n_checks': len(checks), 'n_pass': sum(c['pass'] for c in checks),
       'checks': checks}
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate13/results/wa_check.json', 'w'),
          indent=1)
print(f"{out['n_pass']}/{out['n_checks']} PASS")
for c in checks:
    print(('PASS' if c['pass'] else 'FAIL'), c['check'], c['detail'])
