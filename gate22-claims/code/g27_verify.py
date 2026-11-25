# GATE-27 — independent re-derivation for the fence-revision gate.
# Pure JSON arithmetic on the stored artefacts of Phases 265/266
# (+ Phase 252's stored margins via Phase 265's CTRL-2 anchor fields).
# No programme engine imported, no march re-run.
import json, math

WP = '/home/hatch/workspace/warp-pilot/'
r265 = json.load(open(WP + 'phase265/results/p2651_results.json'))
r266 = json.load(open(WP + 'phase266/results/p2661_results.json'))
out = {}

C = 5.253378225339471  # c_trim, stored (Phase 248 Part A, frozen)
def a_unclamped(t): return -0.5 - C * t * t
def t_clamp(B): return math.sqrt((B - 0.5) / C)

# ---------- 0. trim-law arithmetic ----------
out['c_trim_stored_in_266'] = r266['c_trim_stored']
out['law_field_266'] = r266['law']
out['t_clamp'] = {str(B): t_clamp(B) for B in (0.8, 1.5, 2.0, 2.5, 3.0, 3.5)}
out['a_at'] = {str(t): a_unclamped(t) for t in
               (0.6, 0.6170149292514079, 0.65625, 0.675, 0.68125, 0.75, 0.76875)}
out['t_where_a_reaches_-3.5'] = math.sqrt(3.0 / C)
out['ordering'] = {'wound_hi': 0.5625, 'clamped_hi': 0.6625, 'unclamped_lo': 0.675,
                   'chain_holds': 0.5625 < 0.6625 < 0.675}

# ---------- 1. Phase 266 certificate, re-derived ----------
wr = r266['window_rows']
rows = {}
for g in ('G3', 'G4', 'G5'):
    for row in wr[g]:
        rows.setdefault(row['t'], {})[g] = row['clause_minima']['NEC_ph']
        rows[row['t']].setdefault('DEC_ph_' + g, row['clause_minima']['DEC_ph'])
        rows[row['t']].setdefault('a_applied_' + g, row['a_applied'])

def richardson(v3, v4, v5):
    d34 = v3 - v4
    d45 = v4 - v5
    if d34 == 0.0 and d45 == 0.0:
        return ('degenerate', None, 0.0, v5, 0.0)
    if d34 * d45 <= 0:
        return ('degenerate', None, max(abs(d34), abs(d45)), v5,
                max(abs(d34), abs(d45)))
    p = math.log2(abs(d34 / d45))
    L = v5 + (v5 - v4) / (2.0 ** p - 1.0)
    return ('monotone', p, abs(L - v5), L, abs(L - v5))

cert = r266['certificate']
stored_pi = {float(t): e['NEC_ph'] for t, e in cert['per_instant'].items()}
table = {}
for t in sorted(rows):
    v3, v4, v5 = rows[t]['G3'], rows[t]['G4'], rows[t]['G5']
    case, p, r_, L, _ = richardson(v3, v4, v5)
    st = stored_pi[min(stored_pi, key=lambda k: abs(k - t))]
    table[str(t)] = {
        'v3': v3, 'v4': v4, 'v5': v5, 'case': case, 'p': p, 'L': L, 'r': r_,
        'stored_L': st.get('L'), 'stored_p': st.get('p'),
        'L_dev': abs(L - st['L']) if st.get('L') is not None else None,
        'a_applied_G5': rows[t]['a_applied_G5'],
        'a_unclamped_check': abs(rows[t]['a_applied_G5'] - a_unclamped(t)),
        'NEC_DEC_identical': all(
            rows[t]['DEC_ph_' + g] == rows[t][g] for g in ('G3', 'G4', 'G5')),
    }
out['p266_richardson'] = table
out['p266_cert_booleans_stored'] = {k: cert[k] for k in
                                    ('CERT1', 'CERT2', 'CERT3', 'CERT4', 'all')}
out['p266_bracket_stored'] = cert['bracket']
out['p266_max_L_dev'] = max(v['L_dev'] for v in table.values()
                            if v['L_dev'] is not None)
out['p266_worst_abs_d34'] = max(abs(v['v3'] - v['v4']) for v in table.values())
out['p266_worst_abs_d45'] = max(abs(v['v4'] - v['v5']) for v in table.values())
out['p266_CTRL1'] = r266['control_CTRL1_standing_reproduction']
tp = r266['tail_pricing']
out['p266_tail'] = {k: tp[k] for k in ('first_exceedance_on_(0.75,1.0]',
                                        'stage_max_on_(0.75,1.0]', 'worst_instant',
                                        'carrier_at_worst', 'relative_at_worst')}

# ---------- 2. Phase 265 B-sweep, re-derived ----------
arms = r265['arms']
arm_sum = {}
for B, arm in arms.items():
    rb = arm.get('refined_bracket') or {}
    arm_sum[B] = {'t_clamp_stored': arm.get('t_clamp'),
                  't_clamp_recomputed': t_clamp(float(B)),
                  'refined_bracket': (rb.get('lo_t'), rb.get('hi_t')),
                  'lo_margin': rb.get('lo_margins', {}).get('NEC_ph'),
                  'hi_margin': rb.get('hi_margins', {}).get('NEC_ph'),
                  'hi_carriers': rb.get('hi_carriers_below_zero')}
out['p265_arms'] = arm_sum
mids = {}
for B in ('1.5', '2.0', '2.5', '3.0', '3.5'):
    lo, hi = arm_sum[B]['refined_bracket']
    mids[B] = (lo + hi) / 2.0
out['p265_midpoints_recomputed'] = mids
out['p265_midpoints_stored'] = r265['bracket_midpoints']['midpoints']
out['midpoint_clamped_to_stopfree'] = mids['3.0'] - mids['2.5']
out['bracket_3.0_equals_3.5'] = (arm_sum['3.0']['refined_bracket'] ==
                                 arm_sum['3.5']['refined_bracket'] and
                                 arm_sum['3.0']['lo_margin'] ==
                                 arm_sum['3.5']['lo_margin'] and
                                 arm_sum['3.0']['hi_margin'] ==
                                 arm_sum['3.5']['hi_margin'])

ft = r265['fixed_t_sensitivity_table']
out['p265_fixed_t_keys'] = sorted(ft.keys()) if isinstance(ft, dict) else type(ft)
out['p265_fixed_t'] = ft

# ---------- 3. c_trim sensitivity pricing (read grade) ----------
# (a) delivery sensitivity at fixed t: margin response per unit applied
# amplitude, from arms that differ ONLY in the amplitude applied at t.
# t = 0.65625: B=2.5 arm applies a=-2.5 (clamped since 0.617015);
# B=3.0 arm applies the unclamped law (clamps only at 0.689844).
def fixed_t_margin(t, B):
    return ft[str(t)]['NEC_ph_min_by_B'][str(B)]
sens = {}
for t in (0.65625, 0.6625, 0.675):
    m25 = fixed_t_margin(t, 2.5)
    m30 = fixed_t_margin(t, 3.0)
    a25, a30 = -2.5, a_unclamped(t)
    sens[str(t)] = {'margin_B2.5': m25, 'margin_B3.0': m30,
                    'a_B2.5': a25, 'a_B3.0': a30,
                    'sensitivity_per_unit_abs_a': (m30 - m25) / (abs(a30) - abs(a25))}
out['sensitivity_from_fixed_t'] = sens

# (b) crossing slope at the certified bracket, from Phase 266 limits
L_lo = table['0.675']['L']; L_hi = table['0.68125']['L']
slope = (L_hi - L_lo) / (0.68125 - 0.675)
out['crossing'] = {'L_lo': L_lo, 'L_hi': L_hi, 'slope_per_unit_t': slope,
                   't_star_linear': 0.675 + (0.0 - L_lo) / slope}

# (c) perturbation response: delta_c shifts a(t) by -delta_c * t^2;
# margin at fixed t responds with the delivery sensitivity (~1.0).
S = 1.0  # conservative round value; measured values in 'sensitivity_from_fixed_t'
tc = out['crossing']['t_star_linear']
rows_c = {}
for frac in (-0.10, -0.05, -0.02, -0.01, 0.01, 0.02, 0.05, 0.10):
    dc = frac * C
    dm = S * dc * tc * tc            # margin shift at fixed t near crossing
    dt = -dm / slope                 # crossing-time shift
    rows_c[f'{frac:+.0%}'] = {'delta_c': dc, 'delta_margin_at_crossing': dm,
                              'crossing_shift': dt}
out['c_trim_perturbation'] = {'assumed_sensitivity': S, 't_cross': tc,
                              'rows': rows_c}
# bracket-endpoint stability band at read grade
out['endpoint_stability'] = {
    'lo_end_margin': L_lo, 'hi_end_margin': L_hi,
    'delta_c_flipping_lo': -L_lo / (S * 0.675 ** 2),
    'delta_c_flipping_hi': -L_hi / (S * 0.68125 ** 2),
    'as_fraction_of_c': {
        'lo': (-L_lo / (S * 0.675 ** 2)) / C,
        'hi': (-L_hi / (S * 0.68125 ** 2)) / C}}

print(json.dumps(out, indent=1, default=str))
json.dump(out, open(WP + 'gate27/work/g27_verify_results.json', 'w'),
          indent=1, default=str)
