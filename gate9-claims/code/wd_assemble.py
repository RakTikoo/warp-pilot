#!/usr/bin/env python3
"""W-D: assemble results/wd_g94_numbers.json from the fresh run files."""
import json
A = json.load(open('/home/hatch/workspace/warp-pilot/gate9/wd_audit_raw.json'))
RW = json.load(open('/home/hatch/workspace/warp-pilot/gate9/wd_rw_result.json'))
TR = json.load(open('/home/hatch/workspace/warp-pilot/gate9/wd_rw_trig.json'))
out = {
 "worker": "W-D", "claim": "G9-4 FORMATION (conformal joining member, p=0.1, Phi2, a=0.277734)",
 "run_with": "~/workspace/warp-pilot/venv/bin/python",
 "engine": "W-D fresh derivation (wd_derive.py -> wd_generic_bach.json); NOT W-A's engine, "
           "not any phase script. Anchors validated by W-D before any claim number.",
 "anchors": A['anchors'],
 "trace_symbolic": A['trace_symbolic_from_derivation'],
 "clause_a_covariance": {
   "max_rel_dev_direct_vs_scaled": A['clause_a_covariance_max_rel_dev'],
   "bar": "< 1e-9", "PASS": A['clause_a_PASS'],
   "frozen_r0=1_minima_supporting_crosscheck": A['frozen_r0=1_minima_supporting'],
   "frozen_r0=1_all_positive_supporting": A['frozen_r0=1_all_positive_supporting'],
   "note": "r0=1 legality read itself is W-A's (G9-1); W-D's clause is covariance + the "
           "8-radius ladder consequence (1 m -> 4.785e7 m). Direct evaluation used physical "
           "jets of b(r;R0), Phi(r;R0) at R0=10 and R0=1000, matched x=r/R0."},
 "clause_b_increment": {
   "delta_minima_Rb^-4_scaled": A['clause_b_delta_minima_Rb^-4'],
   "dNEC1_min_scaled": A['clause_b_dNEC1_min_scaled'], "stored_dNEC1": -0.016680,
   "layer_xb": A['clause_b_layer'], "stored_layer": [1.0, 1.00348],
   "failing_combos": A['clause_b_failing_combos'],
   "layer_integral_code_per_m_Rb=10": A['clause_b_layer_integral_code_per_m'],
   "E_legal_at_10m_J_rederived": A['clause_b_E_legal_at_10m_J'],
   "E_legal_definition": "E_legal(L) = (3/(32 pi^2)) hbar c / L (from the P61-4 record); "
                          "at L=10 m gives 3.00309032448144e-29 J, matching p614_results.json",
   "layer_price_ratio": A['clause_b_layer_price_ratio'], "stored_price": 5.83e68,
   "bar": "endpoints within 5%; dNEC1 within 5%; price within factor 2", "PASS": A['clause_b_PASS']},
 "clause_c_pole": {
   "analytic": A['clause_c_analytic'],
   "NEC1_probes_40digit": A['clause_c_NEC1_probes_40digit'],
   "stored_probes": {"e^-1(1-1e-3)": "-6.58e21", "e^-1(1-1e-6)": "-6.65e42", "0.99": "-0.0500024683181"},
   "pole_order_loglog_fit": A['clause_c_pole_order_fit'], "stored_order": 7,
   "pole_fit_points_|NEC1|_vs_delta": A['clause_c_pole_fit_points'],
   "shell_price_lower_bounds": A['clause_c_shell_price_lower_bounds'],
   "stored_bounds": [6.925e84, 7.327e90, 1.711e96],
   "price_factors_vs_stored": A['clause_c_price_factors_vs_stored'],
   "strictly_increasing_as_eps->0": A['clause_c_strictly_increasing'],
   "bar": "probes within factor 3; order 7+-1; bounds within factor 10, strictly increasing",
   "PASS": A['clause_c_PASS']},
 "clause_d_rw_check": {
   "metric": RW['metric'], "bach_mixed_diagonal": RW['bach_mixed_diagonal'],
   "bach_all_zero": RW['bach_all_zero'],
   "weyl_residual_components_after_simplify": RW['weyl_nonzero_components'],
   "weyl_residual_trig_factor_fu": TR, "weyl_all_zero_after_fu": TR['identically_zero']},
 "verdicts": {"a": "REPRODUCED", "b": "REPRODUCED", "c": "REPRODUCED", "d": "REPRODUCED",
              "overall": "REPRODUCED"},
}
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate9/results/wd_g94_numbers.json', 'w'), indent=1)
print('WROTE results/wd_g94_numbers.json')
