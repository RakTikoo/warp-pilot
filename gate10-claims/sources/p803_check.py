"""
p803_check.py — P80-3 checker: recomputes the deciding numbers from
the frozen result JSONs + an independent light recompute of the
deciding row's held-W anatomy and chain balance straight from
p803_lib (not from the audit files). Writes results/p803_check.json.
float64, venv python.
"""
import json, sys
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase80')
import p803_lib as P

RES = '/home/hatch/workspace/warp-pilot/phase80/results'
MARK = 0.0799
checks = {}


def ck(name, ok, detail):
    checks[name] = {'pass': bool(ok), 'detail': detail}


econ = json.load(open(RES + '/p803_economics.json'))
comp = json.load(open(RES + '/p803_composed.json'))
ver = json.load(open(RES + '/p803_verify_o0.06_i0.06.json'))
ver2 = json.load(open(RES + '/p803_verify_o0.06_i0.05.json'))
alone = json.load(open(RES + '/p803_alone_state.json'))

# 1 economics stated for all rows; deciding payloads
ep = {k: v['anatomy']['payload_relat'] for k, v in econ['rows'].items()}
ck('economics_rows', len(ep) == 6, f'payloads={ep}')
ck('deciding_payload_beats_mark',
   ep['o0.06_i0.06'] > MARK and abs(ep['o0.06_i0.06'] - 0.0874508116004831) < 1e-12,
   f"o0.06_i0.06 payload_relat={ep['o0.06_i0.06']:.5f} vs mark {MARK}")
ck('calibration_row_reproduces_P52_3',
   abs(ep['o0.05_i0.05'] - 0.07292) < 5e-5,
   f"o0.05_i0.05 payload={ep['o0.05_i0.05']:.5f} vs P52-3 dual row 0.07292")

# 2 held-W anatomy recomputed from the library
erow = econ['rows']['o0.06_i0.06']
prof_o, prof_i = P.frontier_outer(), P.frontier_inner()
bo, bi, anat, _ = P.held_betas(prof_o, prof_i, 0.06, 0.06)
ck('held_W_recompute', anat['W_i_rel_err'] < 1e-9 and anat['W_o_rel_err'] < 1e-9
   and abs(anat['payload_relat'] - ep['o0.06_i0.06']) < 1e-12,
   f"W rel errs {anat['W_i_rel_err']:.1e}/{anat['W_o_rel_err']:.1e}, "
   f"W sum={anat['W_payload_sum']:.5f}, beta_o={bo:.5f} beta_i={bi:.5f}")
for tag, prof, xx in (('outer', prof_o, erow['x_outer']), ('inner', prof_i, erow['x_inner'])):
    _, ch = P.S_spline(prof, np.array(xx))
    ck(f'chain_{tag}_balanced_monotone',
       ch['balance_rel'] < 1e-12 and ch['monotone_violation'] == 0.0,
       f"balance_rel={ch['balance_rel']:.1e} mono_viol={ch['monotone_violation']} "
       f"lam={ch['lam']:.4f} k={ch['k']:.4f} S_lo-1={ch['S_lo_minus1']:+.1e} S_hi={ch['S_hi']:+.1e}")

# 3 deciding row primary audit (gate-standard)
a15 = comp['rows']['o0.06_i0.06']['audit']['0.15']
regs = a15['regions']
ck('primary_h015_typeI', a15['typeI_frac_sig'] == 1.0,
   f"typeI={a15['typeI_frac_sig']}")
ck('primary_h015_regions_positive_except_cavity_artefact',
   all(regs[r]['worst'] > 0 for r in ('payload', 'inner_wall', 'outer_wall', 'exterior'))
   and regs['cavity']['worst'] < 0 and regs['cavity']['min_sampled_nec_all'] > 0,
   {r: regs[r]['worst'] for r in regs})
ck('primary_h015_sampled_nec_positive', a15['min_sampled_nec_all_sig'] > 0,
   f"sn_all={a15['min_sampled_nec_all_sig']:+.2e}")
ck('conservation_class', comp['rows']['o0.06_i0.06']['conservation']['rel_med'] < 0.02,
   f"rel_med={comp['rows']['o0.06_i0.06']['conservation']['rel_med']:.4f}")

# 4 artefact identity with the cosine control on the same background
cos_cav = comp['cosine_control']['audit']['0.15']['regions']['cavity']['worst']
ck('cavity_artefact_matches_cosine_control',
   abs(cos_cav - regs['cavity']['worst']) / abs(regs['cavity']['worst']) < 0.01,
   f"cosine control cavity worst={cos_cav:+.3e} vs deciding row {regs['cavity']['worst']:+.3e}")

# 5 DEC ladder sign pattern (deciding row)
lad = ver['dec_ladder']
ck('ladder_focused_flips_positive',
   lad['focused']['0.15']['worst'] < 0 < lad['focused']['0.075']['worst']
   and lad['focused']['0.0375']['worst'] > 0
   and all(lad['focused'][h]['typeI_frac_sig'] == 1.0 for h in lad['focused']),
   {h: lad['focused'][h]['worst'] for h in lad['focused']})
ck('ladder_stencil_clear_flips_positive',
   lad['stencil_clear']['0.15']['worst'] < 0 < lad['stencil_clear']['0.075']['worst']
   and lad['stencil_clear']['0.0375']['worst'] > 0,
   {h: lad['stencil_clear'][h]['worst'] for h in lad['stencil_clear']})

# 6 second paths on the deciding row
sp4 = ver['second_path_4th']['0.15']
sp1 = ver['second_path_phase1']
ck('second_path_4th_typeI_and_floor_site_only',
   sp4['typeI_frac_sig'] == 1.0 and sp4['min_sampled_nec_all_sig'] > 0
   and all(sp4['regions'][r]['worst'] > 0 for r in ('payload', 'inner_wall', 'outer_wall', 'exterior'))
   and abs(sp4['regions']['cavity']['worst']) < 2e-6,
   f"4th worst={sp4['worst']:+.2e} cavity={sp4['regions']['cavity']['worst']:+.2e}")
ck('second_path_phase1_typeI_and_floor_site_only',
   sp1['typeI_frac_sig'] == 1.0
   and all(sp1['regions'][r]['worst'] > 0 for r in ('payload', 'inner_wall', 'outer_wall', 'exterior'))
   and abs(sp1['regions']['cavity']['worst']) < 2e-6,
   f"phase1 worst={sp1['worst']:+.2e} cavity={sp1['regions']['cavity']['worst']:+.2e}")
ck('second_row_corroborates',
   ver2['second_path_4th']['0.15']['typeI_frac_sig'] == 1.0
   and ver2['dec_ladder']['stencil_clear']['0.0375']['worst'] > 0,
   f"o0.06_i0.05 payload={ver2['payload_relat']:.5f}")

# 7 alone ceilings as recorded
o7 = alone['shells']['outer']['b0.07']['audit']['0.15']
ck('outer_alone_ceiling_0.06',
   o7['typeI_frac_sig'] < 0.99 and o7['min_sampled_nec_all_sig'] < 0,
   f"outer b0.07 alone: typeI={o7['typeI_frac_sig']:.3f} sn={o7['min_sampled_nec_all_sig']:+.2e} "
   f"(wall region worst={o7['regions']['inner_wall']['worst']:+.2e})")

allpass = all(v['pass'] for v in checks.values())
out = {'item': 'P80-3 checker', 'all_pass': allpass, 'checks': checks}
json.dump(out, open(RES + '/p803_check.json', 'w'), indent=1)
for k, v in checks.items():
    print(('PASS' if v['pass'] else 'FAIL'), k, '—', v['detail'])
print('ALL PASS' if allpass else 'SOME CHECKS FAILED')
