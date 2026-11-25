# GATE-26 independent arithmetic re-derivation of Phase 256's certificate.
# Pure JSON arithmetic on stored rows only. No Phase 256 driver/checker is
# imported; no march is run. Definitions are Phase 256 registration sec.3
# verbatim (Phase 243 pattern), with the Gate-23 sec.1 literal-alternative
# split cross-checked alongside.
import json, math

WP = '/home/hatch/workspace/warp-pilot/'
BAR = 1e-6
CLAUSES = ['NEC_rho', 'NEC_th', 'NEC_ph', 'WEC', 'DEC_rho', 'DEC_th', 'DEC_ph']
BINDING = ['NEC_ph', 'DEC_ph']
NONBIND = [c for c in CLAUSES if c not in BINDING]
W = [0.6, 0.625, 0.65, 0.65625, 0.6625, 0.66875, 0.675, 0.7, 0.725, 0.75]
T_LO, T_HI = 0.65625, 0.6625

p256 = json.load(open(WP + 'phase256/results/p2561_results.json'))
p252 = json.load(open(WP + 'phase252/results/p2522_results.json'))
p252v = json.load(open(WP + 'phase252/results/p2522_verify.json'))
p243 = json.load(open(WP + 'phase243/results/p2431_results.json'))
g23 = json.load(open(WP + 'gate23/work/g23_verify_results.json'))

out = {}

def by_t(rows):
    return {round(r['t'], 10): r for r in rows}

def richardson(v3, v4, v5):
    """Registration sec.3 verbatim: monotone iff d34*d45 > 0 AND
    0.5 <= p <= 6 (admissibility inside the case split); else degenerate."""
    d34 = v3 - v4
    d45 = v4 - v5
    if d34 * d45 > 0:
        p = math.log2(d34 / d45)
        if 0.5 <= p <= 6:
            L = v5 - d45 / (2 ** p - 1)
            r = abs(d45) / (2 ** p - 1)
            return dict(case='monotone', p=p, L=L, r=r, d34=d34, d45=d45,
                        certified=(r <= BAR and abs(d34) <= BAR and abs(d45) <= BAR))
    L = v5
    r = max(abs(d34), abs(d45))
    return dict(case='degenerate', p=None, L=L, r=r, d34=d34, d45=d45,
                certified=(r <= BAR and abs(d34) <= BAR and abs(d45) <= BAR))

def richardson_literal(v3, v4, v5):
    """Literal alternative split: monotone defined by sign alone
    (d34*d45 > 0); admissibility of p checked separately; monotone
    formula applied whenever the sign condition holds."""
    d34 = v3 - v4
    d45 = v4 - v5
    if d34 * d45 > 0:
        p = math.log2(d34 / d45)
        admissible = 0.5 <= p <= 6
        L = v5 - d45 / (2 ** p - 1)
        r = abs(L - v5)
        return dict(case='monotone', p=p, admissible=admissible, L=L, r=r,
                    d34=d34, d45=d45,
                    certified=(r <= BAR and abs(d34) <= BAR and abs(d45) <= BAR))
    L = v5
    r = max(abs(d34), abs(d45))
    return dict(case='degenerate', p=None, admissible=None, L=L, r=r,
                d34=d34, d45=d45,
                certified=(r <= BAR and abs(d34) <= BAR and abs(d45) <= BAR))

# ---------- 1/2/3/7: window Richardson, CERT-1..4, bracket limits, identity
WR = {g: by_t(p256['window_rows'][g]) for g in ('G3', 'G4', 'G5')}
per, per_lit = {}, {}
for t in W:
    per[t], per_lit[t] = {}, {}
    for cl in BINDING:
        v3 = WR['G3'][t]['clause_minima'][cl]
        v4 = WR['G4'][t]['clause_minima'][cl]
        v5 = WR['G5'][t]['clause_minima'][cl]
        per[t][cl] = dict(v3=v3, v4=v4, v5=v5, **richardson(v3, v4, v5))
        per_lit[t][cl] = richardson_literal(v3, v4, v5)

rec = p256['certificate']['per_instant']
max_dev = 0.0
max_dev_r_floatsub = 0.0
for t in W:
    for cl in BINDING:
        rr = rec[str(t)][cl]
        mine = per[t][cl]
        assert rr['case'] == mine['case'], (t, cl)
        assert rr['certified'] == mine['certified'], (t, cl)
        for f in ('v3', 'v4', 'v5', 'd34', 'd45', 'p', 'L', 'resid'):
            max_dev = max(max_dev, abs(rr[f] - mine['r' if f == 'resid' else f]))
        # The recorded 'resid' equals |L - v5| evaluated as a float64
        # subtraction, not the algebraically identical |d45|/(2^p - 1):
        max_dev_r_floatsub = max(max_dev_r_floatsub,
                                 abs(rr['resid'] - abs(mine['L'] - mine['v5'])))

worst = {f: max(abs(per[t][cl][f]) for t in W for cl in BINDING)
         for f in ('d34', 'd45', 'r')}
lit_changes = [(t, cl) for t in W for cl in BINDING
               if per_lit[t][cl]['certified'] != per[t][cl]['certified']
               or per_lit[t][cl]['case'] != per[t][cl]['case']]
out['window_richardson'] = dict(
    per_instant={str(t): per[t] for t in W},
    max_dev_vs_recorded_certificate=max_dev,
    max_dev_r_vs_recorded_if_r_computed_as_float_abs_L_minus_v5=max_dev_r_floatsub,
    r_note=('r here is |d45|/(2^p - 1) per the registration identity; the '
            'recorded resid is |L - v5| in float64 and differs by up to '
            '1.4173059888831791e-16 (at t=0.75). L itself matches the '
            'recorded table at 0.0 deviation at every instant.'),
    worst_abs_d34=worst['d34'], worst_abs_d45=worst['d45'], worst_r=worst['r'],
    factor_under_bar={f: BAR / worst[f] for f in worst},
    p_range=[min(per[t][cl]['p'] for t in W for cl in BINDING),
             max(per[t][cl]['p'] for t in W for cl in BINDING)],
    all_cases=[per[t][cl]['case'] for t in W for cl in BINDING],
    literal_alternative=dict(
        any_certification_changes=bool(lit_changes), changes=lit_changes,
        all_p_admissible=all(per_lit[t][cl]['admissible'] for t in W for cl in BINDING)))

cert1 = all(per[t][cl]['certified'] for t in W for cl in BINDING)
cert2 = all(per[T_LO][cl]['L'] >= 0 and per[T_HI][cl]['L'] < 0 and
            WR['G5'][T_LO]['clause_minima'][cl] >= 0 and
            WR['G5'][T_HI]['clause_minima'][cl] < 0 for cl in BINDING)
cert3 = all(per[t][cl]['L'] >= 0 and WR['G5'][t]['clause_minima'][cl] >= 0
            for t in W if t <= T_LO for cl in BINDING)
nonbind_min = min(WR['G5'][t]['clause_minima'][c]
                  for t in W if t <= T_HI for c in NONBIND)
bars = {}
for t in (T_LO, T_HI):
    row = WR['G5'][t]
    mom_worst = max(abs(x) for x in row['mom_resid_max'].values())
    bars[str(t)] = dict(mom_worst=mom_worst, mom_ok=mom_worst <= 1e-10,
                        flare_min=row['flare_min'], flare_ok=row['flare_min'] > 0,
                        domain_R_min=row['domain_R_min'],
                        domain_R_ok=row['domain_R_min'] > 0,
                        domain_exp2Phi_min=row['domain_exp2Phi_min'],
                        domain_exp2Phi_ok=row['domain_exp2Phi_min'] > 0)
    bars[str(t)]['ok'] = all(bars[str(t)][k] for k in
                             ('mom_ok', 'flare_ok', 'domain_R_ok', 'domain_exp2Phi_ok'))
cert4 = nonbind_min > 0 and all(b['ok'] for b in bars.values())
out['CERT'] = dict(CERT1=cert1, CERT2=cert2, CERT3=cert3, CERT4=cert4,
                    recorded=p256['certificate'].get('booleans',
                             {k: p256['certificate'][k] for k in
                              ('CERT1', 'CERT2', 'CERT3', 'CERT4')
                              if k in p256['certificate']}),
                    nonbind_G5_min_le_thi=nonbind_min, bars=bars)
out['bracket_end_limits'] = dict(
    L_lo=per[T_LO]['NEC_ph']['L'], L_hi=per[T_HI]['NEC_ph']['L'],
    claim_lo=0.05279917238387332, claim_hi=-0.073694680424036624,
    dev_lo=abs(per[T_LO]['NEC_ph']['L'] - 0.05279917238387332),
    dev_hi=abs(per[T_HI]['NEC_ph']['L'] - (-0.073694680424036624)))

# item 7: NEC_ph vs DEC_ph pointwise identity in window rows (all grids)
ident = all(WR[g][t]['clause_minima']['NEC_ph'] == WR[g][t]['clause_minima']['DEC_ph']
            for g in ('G3', 'G4', 'G5') for t in W)
out['nec_dec_identity_window'] = ident

# ---------- 5: tail pricing from stored fresh G3/G4 tail rows
TR = {g: by_t(p256['tail_rows'][g]) for g in ('G3', 'G4')}
tail_per, first_exc, stage = [], None, (0.0, None, None)
for t in sorted(TR['G3']):
    diffs = {c: abs(TR['G3'][t]['clause_minima'][c] - TR['G4'][t]['clause_minima'][c])
             for c in CLAUSES}
    mx = max(diffs.values())
    carrier = max(diffs, key=diffs.get)
    tail_per.append(dict(t=t, per_clause_abs_diff=diffs, max_abs_diff=mx, carrier=carrier))
    if first_exc is None and mx > BAR:
        first_exc = t
    if mx > stage[0]:
        stage = (mx, t, carrier)
rel = stage[0] / abs(TR['G4'][stage[1]]['clause_minima'][stage[2]])
tail_ident = all(TR[g][t]['clause_minima']['NEC_ph'] == TR[g][t]['clause_minima']['DEC_ph']
                 for g in ('G3', 'G4') for t in TR['G3'])
out['tail_pricing'] = dict(per_instant=tail_per, first_exceedance=first_exc,
                           stage_max=stage[0], stage_t=stage[1], carrier=stage[2],
                           relative_at_worst=rel, nec_dec_identity_tail=tail_ident,
                           recorded=dict(first=0.775, max=1.6326915963205124e-05,
                                         t=1.0, carrier='DEC_th',
                                         rel=1.8932984155740035e-06))

# ---------- 4/8: CTRL-2 + item-8 checks from Phase 252 stored rows alone
def smin(row, cl):
    return row['clause_stats'][cl]['min']

samp = p252['reposed_sampled']
last_pass, first_fail, carriers = None, None, None
for row in samp:
    if all(smin(row, c) >= 0 for c in CLAUSES):
        last_pass = row['t']
    elif first_fail is None:
        first_fail = row['t']
        carriers = sorted(c for c in CLAUSES if smin(row, c) < 0)
rb = p252['reposed_bracket']
# ladder replay: start from sampled bracket, apply stored ladder rows in order
lo, hi = last_pass, first_fail
for step in rb['ladder']:
    if step['all_seven_hold']:
        lo = step['t']
    else:
        hi = step['t']
dec = p252['bracket_decomposition']
id_lo = dec['lo']['headline_NEC_ph_min'] + dec['lo']['lift_NEC_ph'] - dec['lo']['composed_NEC_ph_min']
id_hi = dec['hi']['headline_NEC_ph_min'] + dec['hi']['lift_NEC_ph'] - dec['hi']['composed_NEC_ph_min']
c_trim = p252['trim_constants_from_P2482']['c_trim']
t_stop_full = math.sqrt(2.0 / c_trim)
t_stop_rounded = math.sqrt(2.0 / 5.253378)
out['CTRL2'] = dict(
    sampled_bracket=[last_pass, first_fail], first_fail_carriers=carriers,
    ladder_replay_bracket=[lo, hi], stored_refined_bracket=[rb['lo_t'], rb['hi_t']],
    lo_margin_NEC_ph=rb['lo_margins']['NEC_ph'],
    hi_margin_NEC_ph=rb['hi_margins']['NEC_ph'],
    identity_lo=id_lo, identity_hi=id_hi,
    stop_sqrt_2_over_5p253378=t_stop_rounded,
    stop_abs_diff_vs_0p617015=abs(t_stop_rounded - 0.617015),
    stop_sqrt_2_over_full_c_trim=t_stop_full,
    recorded_block=p256['control_CTRL2_stored_rows'])
# item 8
a_05625 = -0.5 - c_trim * 0.5625 ** 2
spot = [c for c in p252v['checks'] if c['name'] == 'holds_at_wound_far_end']
out['item8'] = dict(
    a_at_0p5625_formula=a_05625,
    a_at_0p5625_stored=p252['amplitude_rule']['a_law_at_0p5625'],
    claim_a=-2.162202,
    stop_instant_abs_a_reaches_2p5=t_stop_full,
    stored_t_stop_binds=p252['amplitude_rule']['t_stop_binds'],
    nec_ph_at_0p5625_full_precision_row=None,
    nec_ph_at_0p5625_recorded_detail=(spot[0]['detail'] if spot else None),
    note=('t=0.5625 is not on the 0.025-spaced sampled lattice of '
          'p2522_results.json; the +1.126925 value survives only as the '
          'rounded detail string of the p2522 checker spot check '
          '"holds_at_wound_far_end" (pass=true). No full-precision stored '
          'row exists to recompute it from.'))

# ---------- 6: wound-pose comparison audit (Phase 243 rows + Gate-23 record)
W243 = {g: by_t(p243['window_rows'][g]['threech']) for g in ('G3', 'G4', 'G5')}
wound_L = {}
for t in (0.55625, 0.5625):
    wound_L[str(t)] = richardson(W243['G3'][t]['clause_minima']['NEC_ph'],
                                 W243['G4'][t]['clause_minima']['NEC_ph'],
                                 W243['G5'][t]['clause_minima']['NEC_ph'])['L']
out['comparison_G26B'] = dict(
    wound_L_lo=wound_L['0.55625'], wound_L_hi=wound_L['0.5625'],
    claim_lo=0.004468142716485732, claim_hi=-0.054339801013359036,
    dev_lo=abs(wound_L['0.55625'] - 0.004468142716485732),
    dev_hi=abs(wound_L['0.5625'] - (-0.054339801013359036)),
    gate23_recorded_bracket_L=g23['new_bracket']['bracket_L'],
    same_bar_BAR=BAR, same_binding_clauses=BINDING,
    brackets_disjoint_and_ordered=(0.5625 < 0.65625),
    wound_bracket=[0.55625, 0.5625], combined_bracket=[0.65625, 0.6625])

json.dump(out, open(WP + 'gate26/work/g26_verify_results.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items()
                  if k not in ('window_richardson', 'tail_pricing')}, indent=1))
print('window: max_dev', out['window_richardson']['max_dev_vs_recorded_certificate'],
      'worst', worst, 'factors',
      out['window_richardson']['factor_under_bar'],
      'lit changes', out['window_richardson']['literal_alternative'])
print('tail:', out['tail_pricing']['first_exceedance'], out['tail_pricing']['stage_max'],
      out['tail_pricing']['stage_t'], out['tail_pricing']['carrier'],
      out['tail_pricing']['relative_at_worst'])
