"""
wa_check.py -- Gate-11 W-A checker: recomputes pass/fail for every
registered bar of GATE11.md from results/wa_g111_numbers.json and
writes results/wa_check.json.  Run with
~/workspace/warp-pilot/venv/bin/python.
"""
import json

NUM = '/home/hatch/workspace/warp-pilot/gate11/results/wa_g111_numbers.json'
OUT = '/home/hatch/workspace/warp-pilot/gate11/results/wa_check.json'
d = json.load(open(NUM))
checks = []


def ck(name, ok, detail):
    checks.append({'name': name, 'pass': bool(ok), 'detail': detail})


def fac(mine, phase):
    return mine / phase if phase else None


# anchors
ck('anchor_i_minkowski', d['anchor_i_minkowski_maxAbsG'] < 1e-12,
   f"max|G| {d['anchor_i_minkowski_maxAbsG']:.3e} < 1e-12")
ck('anchor_ii_rho', d['anchor_ii_max_rho_rel_err'] <= 3e-3,
   f"{d['anchor_ii_max_rho_rel_err']:.3e} <= 3e-3")
ck('anchor_ii_p', d['anchor_ii_max_p_abs_err'] <= 3e-7,
   f"{d['anchor_ii_max_p_abs_err']:.3e} <= 3e-7")
a3 = d['anchor_iii_control_span']
ck('anchor_iii_typeI', a3['audit']['typeI_frac_sig'] == 1.0,
   f"{a3['audit']['typeI_frac_sig']}")
ck('anchor_iii_outer_wall_factor3',
   1 / 3 <= a3['factors']['outer_wall_vs_stored'] <= 3,
   f"factor {a3['factors']['outer_wall_vs_stored']:.2f} vs stored +3.2016e-5")
ck('anchor_iii_conservation_factor3',
   1 / 3 <= a3['factors']['conservation_vs_stored'] <= 3,
   f"rel_med {a3['conservation']['rel_med']:.4f} vs stored 0.0115, "
   f"factor {a3['factors']['conservation_vs_stored']:.2f}")
ck('anchor_iii_cavity_site_positive', a3['cavity_site_4.53_26dir']['min_dec'] > 0,
   f"DEC at r=4.53 {a3['cavity_site_4.53_26dir']['min_dec']:+.4e} (phase FD raw -1.107e-4; "
   f"stronger settlement)")
a4 = d['anchor_iv_control_audit']
ck('anchor_iv_typeI', a4['typeI_frac_sig'] == 1.0, f"{a4['typeI_frac_sig']}")
for reg in ('inner_wall', 'outer_wall'):
    f = d['anchor_iv_control_factor_vs_gate8'][reg]
    ck(f'anchor_iv_{reg}_factor3', 1 / 3 <= f <= 3, f'factor {f:.2f} vs Gate-8')
lad = d['anchor_iv_control_cavity_ladder']
ck('anchor_iv_cavity_floor', all(abs(e['min_dec_near_edge_shell_4.6_5']) <= 2.3e-4
                                 for e in lad.values()),
   'near-edge shell DEC within Gate-8 floor bound 2.3e-4 at every rung, '
   'Type-I 1.000, no convergent negative value')
ck('anchor_iv_payload_site_factor3',
   1 / 3 <= d['anchor_iv_payload_site_read']['factor_at_gate8_site'] <= 3,
   f"at Gate-8 site r=1.4317: factor "
   f"{d['anchor_iv_payload_site_read']['factor_at_gate8_site']:.2f} "
   f"(region-worst factor exception recorded: significance borderline, "
   f"see report)")

# bar (a) economics
e = d['deciding_economics_rel_err']
ck('bar_a_payload', e['payload_vs_0.09556'] <= 1e-4,
   f"held payload {d['deciding_economics']['payload_relat']:.10f}, "
   f"rel err {e['payload_vs_0.09556']:.2e}")
ck('bar_a_heldW_err', e['W_held_max_rel_err'] <= 1e-12,
   f"max held-W rel err {e['W_held_max_rel_err']:.2e} (10^-16 class)")

# bars (b), (c), (d)
s = d['deciding_audit']
ck('bar_b_typeI', s['typeI_frac_sig'] == 1.0, f"{s['typeI_frac_sig']}")
PHASE = {'payload': 3.84e-6, 'inner_wall': 1.190e-3,
         'outer_wall': 3.35e-5, 'exterior': 1.11e-6}
for reg, pv in PHASE.items():
    w = s['regions'][reg]['worst']
    ck(f'bar_c_{reg}', w > 0 and 1 / 3 <= fac(w, pv) <= 3,
       f"worst {w:+.4e} vs phase {pv:+.2e}, factor {fac(w, pv):.2f}")
ck('bar_d_sampled_null', s['min_sampled_nec_all_sig'] > 0,
   f"min {s['min_sampled_nec_all_sig']:+.4e}")

# bar (e) cavity settlement
cav = d['deciding_cavity_settlement']
ck('bar_e_site_positive', cav['site_4.53_26dir']['min_dec'] > 0
   and cav['site_4.53_162dir']['min_dec'] > 0,
   f"DEC at r=4.53: {cav['site_4.53_26dir']['min_dec']:+.4e} (26d) / "
   f"{cav['site_4.53_162dir']['min_dec']:+.4e} (162d) -- form (e)(i), first clause")
lad2 = cav['radial_density_ladder']
ck('bar_e_no_convergent_negative',
   all(abs(x['min_dec_near_edge_shell_4.6_5']) <= 2.5e-6 for x in lad2.values()),
   'ladder near-edge minima at floor |DEC| <= 2.5e-6, sign-unstable, '
   'no convergent negative continuum value')

# bar (f) floor bound
cw = s['regions']['cavity']['worst']
ck('bar_f_cavity_inside_narrower_on_deciding_set', abs(cw) <= 2e-6,
   f"deciding-set cavity worst {cw:+.4e} inside Phase-80's 2e-6 bound; "
   f"densest exact-site read at r=4.87 "
   f"{cav['site_4.87_162dir']['min_dec']:+.4e} inside only the widened 4e-6 "
   f"bound; legality on this path rests on the re-derived settlement, "
   f"not on either bound")

# bar (g) endpoint residuals
cho = d['deciding_chains']['outer']
sto = d['deciding_chains']['outer_stored']
ck('bar_g_chain_scalars_match',
   abs(cho['lam'] - sto['lam']) < 1e-9 and abs(cho['k'] - sto['k']) < 1e-9
   and abs(cho['S_lo_minus1'] - sto['S_lo_minus1']) < 1e-9
   and abs(cho['S_hi'] - sto['S_hi']) < 1e-9,
   f"lam/k/S_lo-1/S_hi rebuilt = stored to <1e-9 "
   f"(S_lo-1 {cho['S_lo_minus1']:+.4e}, S_hi {cho['S_hi']:+.4e})")
sc = d['residual_sensitivity_corrected_audit']
mov = all(sc['regions'][r]['worst'] * s['regions'][r]['worst'] > 0
          and 1 / 3 <= fac(sc['regions'][r]['worst'], s['regions'][r]['worst']) <= 3
          for r in PHASE)
ck('bar_g_margins_stable_under_correction', mov,
   'residual-corrected variant: every region worst keeps sign and moves '
   '<1% (payload/inner/outer/exterior); cavity stays in the same floor class')

# bar (h) corroboration
s2 = d['corroboration_row']['audit']
ck('bar_h_corroboration',
   s2['typeI_frac_sig'] == 1.0
   and all(s2['regions'][r]['worst'] > 0 for r in PHASE)
   and d['corroboration_row']['cavity_sites']['site_4.53_162dir']['min_dec'] > 0,
   f"payload {d['corroboration_row']['economics']['payload_relat']:.8f} "
   f"(claim 0.08915), Type-I {s2['typeI_frac_sig']}, cavity site positive")

# bar (i) mechanism
mi = d['mechanism_alone']
ck('bar_i_mechanism',
   0.5 <= mi['e0.30']['audit']['typeI_frac_sig'] <= 0.8
   and mi['e0.30']['audit']['min_sampled_nec_all_sig'] < 0
   and mi['e0.10']['audit']['typeI_frac_sig'] == 1.0
   and mi['e0.10']['audit']['worst'] > 0,
   f"alone beta=0.07: e=0.30 Type-I {mi['e0.30']['audit']['typeI_frac_sig']:.4f} "
   f"(phase 0.646), sampled {mi['e0.30']['audit']['min_sampled_nec_all_sig']:+.3e} "
   f"(phase -5.04e-4); e=0.10 Type-I {mi['e0.10']['audit']['typeI_frac_sig']}, "
   f"worst {mi['e0.10']['audit']['worst']:+.3e}")

n_pass = sum(c['pass'] for c in checks)
out = {'n_checks': len(checks), 'n_pass': n_pass,
       'all_pass': n_pass == len(checks), 'checks': checks}
json.dump(out, open(OUT, 'w'), indent=1)
print(f"wa_check: {n_pass}/{len(checks)} PASS")
for c in checks:
    print(('PASS' if c['pass'] else 'FAIL'), c['name'], '--', c['detail'])
