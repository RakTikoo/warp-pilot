# GATE-23 independent re-derivation. Pure arithmetic on the stored
# artefacts of Phases 214/234/243. No programme engine is imported;
# no march is run. Writes gate23/work/g23_verify_results.json.
import json, math

WP = '/home/hatch/workspace/warp-pilot/'
BAR = 1e-6
CLAUSES = ['NEC_rho', 'NEC_th', 'NEC_ph', 'WEC', 'DEC_rho', 'DEC_th', 'DEC_ph']
BINDING = ['NEC_ph', 'DEC_ph']
NONBIND = [c for c in CLAUSES if c not in BINDING]

p243 = json.load(open(WP + 'phase243/results/p2431_results.json'))
p234 = json.load(open(WP + 'phase234/results/p2341_results.json'))
p214 = json.load(open(WP + 'phase214/results/p2141_results.json'))

out = {}

def rows_by_t(rows):
    return {round(r['t'], 10): r for r in rows}

W = {g: {pose: rows_by_t(p243['window_rows'][g][pose])
         for pose in ('threech', 'director')}
     for g in ('G3', 'G4', 'G5')}

def richardson(v3, v4, v5):
    # The phase driver's case split (which Gate-23 adopts, see GATE23.md):
    # monotone iff d34*d45 > 0 AND the implied order p is admissible
    # (0.5 <= p <= 6); otherwise the degenerate treatment L := v5,
    # r := max(|d34|, |d45|). The literal-text alternative (monotone
    # formula at inadmissible p) is cross-checked separately below.
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

def evaluate(pose, window, t_lo, t_hi, cert_block):
    per = {}
    for t in window:
        per[t] = {}
        for cl in BINDING:
            v3 = W['G3'][pose][t]['clause_minima'][cl]
            v4 = W['G4'][pose][t]['clause_minima'][cl]
            v5 = W['G5'][pose][t]['clause_minima'][cl]
            per[t][cl] = richardson(v3, v4, v5)
    cert1 = all(per[t][cl]['certified'] for t in window for cl in BINDING)
    cert2 = all(per[t_lo][cl]['L'] >= 0 and per[t_hi][cl]['L'] < 0 and
                W['G5'][pose][t_lo]['clause_minima'][cl] >= 0 and
                W['G5'][pose][t_hi]['clause_minima'][cl] < 0 for cl in BINDING)
    cert3 = all(per[t][cl]['L'] >= 0 and W['G5'][pose][t]['clause_minima'][cl] >= 0
                for t in window if t <= t_lo for cl in BINDING)
    # CERT-4: non-binding clauses > 0 at G5 at every window instant <= t_hi
    nb_min = min(W['G5'][pose][t]['clause_minima'][cl]
                 for t in window if t <= t_hi for cl in NONBIND)
    bars = {}
    bars_ok = True
    for t in (t_lo, t_hi):
        row = W['G5'][pose][t]
        mom = max(abs(x) for x in row['mom_resid_max'].values())
        ok = (mom <= 1e-10 and row['flare_min'] > 0 and
              row['domain_R_min'] > 0 and row['domain_exp2Phi_min'] > 0)
        bars[t] = dict(mom_worst=mom, flare_min=row['flare_min'],
                       domain_R_min=row['domain_R_min'],
                       domain_exp2Phi_min=row['domain_exp2Phi_min'], ok=ok)
        bars_ok = bars_ok and ok
    cert4 = (nb_min > 0) and bars_ok
    # compare against the phase's recorded certificate
    rec = cert_block['per_instant']
    max_dev = 0.0
    for t in window:
        for cl in BINDING:
            rr = rec[str(t)][cl]
            mine = per[t][cl]
            for key, mk in (('v3', None), ('v4', None), ('v5', None)):
                pass
            max_dev = max(max_dev, abs(rr['d34'] - mine['d34']),
                          abs(rr['d45'] - mine['d45']),
                          abs(rr['resid'] - mine['r']),
                          abs(rr['L'] - mine['L']))
            assert rr['certified'] == mine['certified'], (t, cl)
            assert rr['case'] == mine['case'], (t, cl)
    margins = {}
    for comp, fn in (('d34', lambda e: abs(e['d34'])),
                     ('d45', lambda e: abs(e['d45'])),
                     ('r', lambda e: e['r'])):
        worst = max(fn(per[t][cl]) for t in window for cl in BINDING)
        margins[comp] = dict(worst=worst, factor_under_bar=BAR / worst)
    return dict(CERT1=cert1, CERT2=cert2, CERT3=cert3, CERT4=cert4,
                nonbind_G5_min_le_thi=nb_min, bars=bars,
                recorded_CERT=dict(CERT1=cert_block['CERT1'], CERT2=cert_block['CERT2'],
                                   CERT3=cert_block['CERT3'], CERT4=cert_block['CERT4']),
                max_dev_vs_recorded_certificate=max_dev, margins=margins,
                bracket_L={cl: (per[t_lo][cl]['L'], per[t_hi][cl]['L']) for cl in BINDING},
                p_range=(min(per[t][cl]['p'] for t in window for cl in BINDING
                             if per[t][cl]['p'] is not None),
                         max(per[t][cl]['p'] for t in window for cl in BINDING
                             if per[t][cl]['p'] is not None)))

W_new = [0.5, 0.525, 0.55, 0.55625, 0.5625, 0.56875, 0.575, 0.6, 0.625, 0.65]
W_star = [0.45, 0.475, 0.5, 0.50625, 0.5125, 0.51875, 0.525, 0.55, 0.575, 0.6]
out['new_bracket'] = evaluate('threech', W_new, 0.55625, 0.5625,
                              p243['certificate_new_bracket'])
out['tstar'] = evaluate('director', W_star, 0.5, 0.50625,
                        p243['certificate_tstar'])
out['tstar_disposition_recorded'] = p243['tstar_disposition']

# ---- CTRL-1 re-derived from the stored artefacts alone (no fresh march):
# Phase 243's stored G3/G4 window rows vs Phases 234/214's stored rows.
def maxdiff(rows_a, rows_b, tmax=None):
    A, B = rows_by_t(rows_a), rows_by_t(rows_b)
    m = 0.0
    for t, ra in A.items():
        if tmax is not None and t > tmax:
            continue
        if t not in B:
            continue
        rb = B[t]
        for cl in CLAUSES:
            m = max(m, abs(ra['clause_minima'][cl] - rb['clause_minima'][cl]))
    return m

ctrl1 = {}
ctrl1['threech_G4_sampled_vs_P234'] = maxdiff(
    [r for r in p243['window_rows']['G4']['threech'] if r['t'] in
     [x['t'] for x in p234['threech_G4_instants_primary']]],
    p234['threech_G4_instants_primary'], tmax=0.65)
ctrl1['threech_G3_sampled_vs_P234'] = maxdiff(
    p243['window_rows']['G3']['threech'],
    p234['threech_G3_instants_primary'], tmax=0.65)
ctrl1['director_G4_sampled_vs_P214'] = maxdiff(
    p243['window_rows']['G4']['director'],
    p214['director_G4_instants_0_1'], tmax=0.65)
# refined rows: Phase 234 refinement instants vs Phase 243 G4 threech window rows
ref234 = rows_by_t(p234['threech_refinement_instants_primary'])
g4new = rows_by_t(p243['window_rows']['G4']['threech'])
ctrl1['threech_G4_refined_vs_P234'] = max(
    abs(g4new[t]['clause_minima'][cl] - ref234[t]['clause_minima'][cl])
    for t in ref234 for cl in CLAUSES)
out['CTRL1_from_stored_artefacts'] = ctrl1

# ---- CTRL-2 + tail pricing re-derived from Phase 234's stored G3/G4 rows.
g3 = rows_by_t(p234['threech_G3_instants_primary'])
g4 = rows_by_t(p234['threech_G4_instants_primary'])
per_inst = {}
for t in sorted(g4):
    per_inst[t] = max((abs(g3[t]['clause_minima'][cl] - g4[t]['clause_minima'][cl]), cl)
                      for cl in CLAUSES)
stageA = max(v[0] for t, v in per_inst.items() if t <= 0.5)
stageB = max(v[0] for t, v in per_inst.items() if t > 0.5)
first_exc = min(t for t, v in per_inst.items() if t > 0.5 and v[0] > BAR)
worst_t = max((t for t in per_inst if t > 0.5), key=lambda t: per_inst[t][0])
worst_val, worst_cl = per_inst[worst_t]
rel = worst_val / abs(g4[worst_t]['clause_minima'][worst_cl])
out['CTRL2_tail_from_P234_rows'] = {
    'stage_A_max': stageA, 'stage_B_max': stageB,
    'first_exceedance_stage_B': first_exc, 'worst_instant': worst_t,
    'carrier': worst_cl, 'relative_at_worst': rel,
    'per_instant_on_(0.5,0.65]': {str(t): per_inst[t][0] for t in sorted(per_inst)
                                  if 0.5 < t <= 0.65},
    'recorded': dict(stage_A=3.4339573895536546e-07, stage_B=3.4498744435396134e-05,
                     first_exceedance=0.775, worst_instant=1.0, carrier='DEC_th',
                     relative=3.3942464143610627e-06)}

# ---- [0, 0.5] three-channel clause record (attack 4): Phase 234 G4 sampled
# instants on [0, 0.5] — every clause >= -1e-9 at every sampled instant?
rows05 = [r for r in p234['threech_G4_instants_primary'] if r['t'] <= 0.5]
worst05 = {cl: min(r['clause_minima'][cl] for r in rows05) for cl in CLAUSES}
out['threech_G4_on_0_0p5'] = dict(n_instants=len(rows05), worst_per_clause=worst05)

# ---- Literal-reading cross-check: at threech t = 0.5 / 0.525 the
# differences share a sign but imply p < 0 (inadmissible). Apply the
# monotone formula anyway: does the instant still certify, and is
# L still >= 0 (CERT-3 relevant)?
cross = {}
for t in (0.5, 0.525):
    for cl in BINDING:
        v3 = W['G3']['threech'][t]['clause_minima'][cl]
        v4 = W['G4']['threech'][t]['clause_minima'][cl]
        v5 = W['G5']['threech'][t]['clause_minima'][cl]
        d34, d45 = v3 - v4, v4 - v5
        p = math.log2(d34 / d45)
        L = v5 - d45 / (2 ** p - 1)
        r = abs(d45) / (2 ** p - 1)
        cross[f'{t}/{cl}'] = dict(p=p, L_literal=L, r_literal=r,
                                  certified_literal=(r <= BAR and abs(d34) <= BAR
                                                     and abs(d45) <= BAR))
out['literal_reading_crosscheck'] = cross

json.dump(out, open(WP + 'gate23/work/g23_verify_results.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
