"""W-C checker: applies the GATE9.md G9-3 bars to W-C's own result
files (results/wc_dyn_tb.json, wc_dyn_jm.json, wc_static.json,
wc_symbol.json) and writes results/wc_g93_numbers.json + a PASS/FAIL
summary. No phase machinery is used; stored values are read only as
comparison data."""
import json, os
GATE = os.path.expanduser('~/workspace/warp-pilot/gate9')
R = os.path.join(GATE, 'results')
tb = json.load(open(os.path.join(R, 'wc_dyn_tb.json')))
jm = json.load(open(os.path.join(R, 'wc_dyn_jm.json')))
st = json.load(open(os.path.join(R, 'wc_static.json')))
sy = json.load(open(os.path.join(R, 'wc_symbol.json')))
checks = {}
def chk(name, ok, detail):
    checks[name] = {'pass': bool(ok), 'detail': detail}
# --- machinery re-gate on T-b ---
p1 = tb['P1_R10']['averaged_fit']['smallest_physical_eigenvalue_min']
p2 = tb['P2_R10']['averaged_fit']['smallest_physical_eigenvalue_min']
chk('regate_P1_R10_within_5pct_of_0.00265284', abs(p1-0.00265284)/0.00265284 < 0.05, p1)
chk('regate_P2_R10_within_5pct_of_0.00087671', abs(p2-0.00087671)/0.00087671 < 0.05, p2)
tb_cross = sum(len(b[f]['physical_eigenvalue_zero_crossings_in_[-5,0]'])
               for b in tb.values() if isinstance(b, dict) and 'averaged_fit' in b
               for f in ('averaged_fit', 'snapshot_fit'))
tb_nneg = sum(b[f]['n_scan_points_lambda_phys_negative']
              for b in tb.values() if isinstance(b, dict) and 'averaged_fit' in b
              for f in ('averaged_fit', 'snapshot_fit'))
chk('regate_Tb_no_zero_crossing', tb_cross == 0 and tb_nneg == 0, {'crossings': tb_cross, 'neg_points': tb_nneg})
tb_detmax = max(b[f]['det_max_abs_over_scan'] for b in tb.values() if isinstance(b, dict) and 'averaged_fit' in b
                for f in ('averaged_fit', 'snapshot_fit'))
tb_rowmax = max(b[f]['null_rowsum_resid_max_over_scan'] for b in tb.values() if isinstance(b, dict) and 'averaged_fit' in b
                for f in ('averaged_fit', 'snapshot_fit'))
tb_align = min(b[f]['null_eigvec_alignment_min'] for b in tb.values() if isinstance(b, dict) and 'averaged_fit' in b
               for f in ('averaged_fit', 'snapshot_fit'))
chk('regate_Tb_gauge_anatomy_structural', tb_detmax < 1e-6 and tb_rowmax < 1e-6 and tb_align > 0.999999,
    {'det_max_abs': tb_detmax, 'rowsum_resid_max': tb_rowmax, 'alignment_min': tb_align})
# --- static sector ---
chk('static_trace_zero_numeric_random_jets', st['trace_numeric_max_random_jets'] < 1e-9,
    st['trace_numeric_max_random_jets'])
chk('static_Tb_control_vs_closed_forms', st['TB_control_max_rel_err_vs_closed'] < 1e-9,
    st['TB_control_max_rel_err_vs_closed'])
chk('static_member_float64_traces', max(st['JM']['delta_b']['max_abs_trace_deltaB_float64'],
                                        st['JM']['delta_P']['max_abs_trace_deltaB_float64']) < 1e-9,
    {'delta_b': st['JM']['delta_b']['max_abs_trace_deltaB_float64'],
     'delta_P': st['JM']['delta_P']['max_abs_trace_deltaB_float64']})
mp_traces = []
for rv, row in st['mp40_probes'].items():
    mp_traces += [abs(float(row['delta_b_trace'])), abs(float(row['delta_P_trace']))]
chk('static_member_mp40_traces_below_1e-25', max(mp_traces) < 1e-25, max(mp_traces))
chk('static_mp40_at_least_6_radii', len(st['mp40_probes']) >= 6, len(st['mp40_probes']))
# member background B spot check vs stored (p711_results.json values)
stored_bg = {'1.05': (-0.39626208550223885, -0.24218667388794768, 0.3192243796950924),
             '2.0': (-0.020487373833253067, -0.008425558680629984, 0.014456466256941532),
             '10.0': (-5.066253534859433e-06, -3.034199390079266e-06, 4.0502264624693505e-06)}
bg_err = 0.0
for rv, svals in stored_bg.items():
    got = st['JM']['background_B'][rv]
    bg_err = max(bg_err, max(abs(g-s)/abs(s) for g, s in zip(got, svals)))
chk('static_member_background_B_vs_stored', bg_err < 1e-6, bg_err)
# --- dynamic sector on the member ---
jm_cross = sum(len(b[f]['physical_eigenvalue_zero_crossings_in_[-5,0]'])
               for b in jm.values() if isinstance(b, dict) and 'averaged_fit' in b
               for f in ('averaged_fit', 'snapshot_fit'))
jm_nneg = sum(b[f]['n_scan_points_lambda_phys_negative']
              for b in jm.values() if isinstance(b, dict) and 'averaged_fit' in b
              for f in ('averaged_fit', 'snapshot_fit'))
chk('dynamic_member_no_zero_crossing_registered_grid', jm_cross == 0 and jm_nneg == 0,
    {'crossings': jm_cross, 'neg_points': jm_nneg})
jm_p2 = jm['P2_R10']['averaged_fit']['smallest_physical_eigenvalue_min']
jm_p1 = jm['P1_R10']['averaged_fit']['smallest_physical_eigenvalue_min']
chk('dynamic_member_P2avg_within_factor2_of_0.00121741', 0.5 < jm_p2/0.00121741 < 2.0, jm_p2)
chk('dynamic_member_P1avg_within_factor2_of_0.00424541', 0.5 < jm_p1/0.00424541 < 2.0, jm_p1)
jm_min_all = min(b[f]['smallest_physical_eigenvalue_min']
                 for b in jm.values() if isinstance(b, dict) and 'averaged_fit' in b
                 for f in ('averaged_fit', 'snapshot_fit'))
chk('dynamic_member_smallest_physical_eigenvalue_positive', jm_min_all > 0, jm_min_all)
jm_detmax = max(b[f]['det_max_abs_over_scan'] for b in jm.values() if isinstance(b, dict) and 'averaged_fit' in b
                for f in ('averaged_fit', 'snapshot_fit'))
jm_rowmax = max(b[f]['null_rowsum_resid_max_over_scan'] for b in jm.values() if isinstance(b, dict) and 'averaged_fit' in b
                for f in ('averaged_fit', 'snapshot_fit'))
chk('dynamic_member_gauge_anatomy_structural', jm_detmax < 1e-6 and jm_rowmax < 1e-5,
    {'det_max_abs': jm_detmax, 'rowsum_resid_max': jm_rowmax})
# --- symbol ---
chk('symbol_gauge_nullspace_exact_5', all(sy['gauge_null_directions_exact']) and len(sy['gauge_null_directions_exact']) == 5,
    sy['gauge_null_directions_exact'])
chk('symbol_rank5_off_cone', sy['points']['w2_k1']['rank'] == 5 and sy['points']['w3_k1']['rank'] == 5,
    {'w2k1': sy['points']['w2_k1']['rank'], 'w3k1': sy['points']['w3_k1']['rank']})
ev1 = sy['points']['w2_k1']['eigenvalues']; ev2 = sy['points']['w3_k1']['eigenvalues']
chk('symbol_physical_eigenvalues_proportional_Q2',
    set(ev1) == {'-9/4', '0'} and set(ev2) == {'-16', '0'},
    {'w2k1': ev1, 'w3k1': ev2})
chk('symbol_on_cone_no_nonzero_eigenvalue', set(sy['points']['w2_k2']['eigenvalues']) == {'0'},
    sy['points']['w2_k2']['eigenvalues'])
chk('symbol_TT_eigenvalue_Q2_factorised',
    sy['sectors_direct']['TT_xy']['eigenvalue'] == '-(-k + w)**2*(k + w)**2/4' and sy['sectors_direct']['TT_xy']['is_eigenvector'],
    sy['sectors_direct']['TT_xy'])
out = {'item': 'G9-3 (W-C) — stability of the conformal joining member interior background',
       'venv_python': '~/workspace/warp-pilot/venv/bin/python',
       'checks': checks,
       'all_pass': all(c['pass'] for c in checks.values()),
       'regate_Tb': {'P1_R10_avg': p1, 'P2_R10_avg': p2,
                     'blocks': {k: {f: {'min_phys': tb[k][f]['smallest_physical_eigenvalue_min'],
                                        'crossings': tb[k][f]['physical_eigenvalue_zero_crossings_in_[-5,0]'],
                                        'det_max': tb[k][f]['det_max_abs_over_scan'],
                                        'rowsum_max': tb[k][f]['null_rowsum_resid_max_over_scan']}
                                   for f in ('averaged_fit', 'snapshot_fit')} for k in tb}},
       'dynamic_member': {'P1_R10_avg': jm_p1, 'P2_R10_avg': jm_p2, 'min_all_blocks': jm_min_all,
                          'blocks': {k: {f: {'min_phys': jm[k][f]['smallest_physical_eigenvalue_min'],
                                             'crossings': jm[k][f]['physical_eigenvalue_zero_crossings_in_[-5,0]'],
                                             'det_max': jm[k][f]['det_max_abs_over_scan'],
                                             'rowsum_max': jm[k][f]['null_rowsum_resid_max_over_scan']}
                                        for f in ('averaged_fit', 'snapshot_fit')} for k in jm}},
       'static_member': {'float64_max_trace_delta_b': st['JM']['delta_b']['max_abs_trace_deltaB_float64'],
                         'float64_max_trace_delta_P': st['JM']['delta_P']['max_abs_trace_deltaB_float64'],
                         'mp40_max_abs_trace': max(mp_traces),
                         'mp40_traces': {rv: {'delta_b': st['mp40_probes'][rv]['delta_b_trace'],
                                              'delta_P': st['mp40_probes'][rv]['delta_P_trace']}
                                         for rv in st['mp40_probes']},
                         'background_B_rel_err_vs_stored': bg_err,
                         'normalisation_factor': st['normalisation_factor_closed_over_mine'],
                         'Tb_control_max_rel_err': st['TB_control_max_rel_err_vs_closed']},
       'symbol': {'gauge_null_exact': sy['gauge_null_directions_exact'],
                  'rank_off_cone': 5, 'physical_eigenvalue_my_normalisation': '-Q^2/4 (x5), Q = w^2 - k^2',
                  'TT_eigenvalue': sy['sectors_direct']['TT_xy']['eigenvalue'],
                  'scalar_sector_eigenvalues': sy['scalar_sector_eigenvalues'],
                  'on_cone_rank': sy['points']['w2_k2']['rank']}}
json.dump(out, open(os.path.join(R, 'wc_g93_numbers.json'), 'w'), indent=1)
for k, v in checks.items(): print(('PASS' if v['pass'] else 'FAIL'), k, '->', v['detail'], flush=True)
print('ALL PASS' if out['all_pass'] else 'SOME FAILED', flush=True)
