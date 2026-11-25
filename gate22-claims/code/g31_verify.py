#!/usr/bin/env python
"""GATE-31 — the gate's own re-derivation. Pure JSON arithmetic
on the stored rows of gate31/work/g31_results.json (the
certification run's per-grid window rows) and on Phase 288's
stored member rows. No programme engine is imported, no march
is re-run, no phase driver or checker is used as evidence.
Pattern: Gates 23/27/28 (arithmetic-level independence).
Writes gate31/work/g31_verify_results.json."""
import json
import math

WP = '/home/hatch/workspace/warp-pilot/'
BAR = 1e-6
CK = ['NEC_rho', 'NEC_th', 'NEC_ph', 'WEC',
      'DEC_rho', 'DEC_th', 'DEC_ph']
BIND = ['NEC_ph', 'DEC_ph']
NONBIND = [c for c in CK if c not in BIND]
T_LO, T_HI = 0.575, 0.58125

res = json.load(open(WP + 'gate31/work/g31_results.json'))
out = {'gate': 'GATE-31 verify (gate arithmetic)'}


def key(t):
    return round(float(t), 6)


rows = {}
for g in ('g3', 'g4', 'g5'):
    rows[g] = {key(r['t']): r for r in res['per_grid_window_rows'][g]}
W = sorted(rows['g5'].keys())
out['window'] = W
assert W == sorted(rows['g3'].keys()) == sorted(rows['g4'].keys())

# NEC_ph = DEC_ph identity on the stored rows (all grids)
ident = 0.0
for g in rows:
    for t, r in rows[g].items():
        ident = max(ident, abs(r['clause_minima']['NEC_ph']
                               - r['clause_minima']['DEC_ph']))
out['nec_dec_ph_identity_max_abs_diff'] = ident


def rich(v3, v4, v5):
    d34 = v3 - v4
    d45 = v4 - v5
    case = 'degenerate'
    p = None
    if d34 * d45 > 0.0:
        p_try = math.log2(d34 / d45)
        if 0.5 <= p_try <= 6.0:
            case = 'monotone'
            p = p_try
    if case == 'monotone':
        L = v5 - d45 / (2.0 ** p - 1.0)
        r = abs(d45) / (2.0 ** p - 1.0)
    else:
        L = v5
        r = max(abs(d34), abs(d45))
    cert = bool(r <= BAR and abs(d34) <= BAR and abs(d45) <= BAR)
    return {'v3': v3, 'v4': v4, 'v5': v5, 'd34': d34, 'd45': d45,
            'case': case, 'p': p, 'L': L, 'r': r, 'certified': cert}


table = {}
for t in W:
    table[t] = {}
    for c in BIND:
        table[t][c] = rich(rows['g3'][t]['clause_minima'][c],
                           rows['g4'][t]['clause_minima'][c],
                           rows['g5'][t]['clause_minima'][c])
out['richardson'] = {str(t): table[t] for t in W}

# Compare against the worker's recorded Richardson table
wtab = {key(e['t']): e for e in res['richardson_table']}
max_dev = 0.0
case_mismatch = []
for t in W:
    for c in BIND:
        w = wtab[t][c]
        m = table[t][c]
        for f in ('v3', 'v4', 'v5', 'd34', 'd45', 'L', 'r'):
            max_dev = max(max_dev, abs(w[f] - m[f]))
        if w['case'] != m['case']:
            case_mismatch.append((t, c, w['case'], m['case']))
        if bool(w['limit_certified']) != m['certified']:
            case_mismatch.append((t, c, 'certified-flag'))
out['worker_table_max_deviation'] = max_dev
out['worker_table_case_mismatches'] = case_mismatch

# CERT conditions, gate-evaluated
cert1 = all(table[t][c]['certified'] for t in W for c in BIND)
cert2 = all(table[T_LO][c]['L'] >= 0.0 and table[T_HI][c]['L'] < 0.0
            and table[T_LO][c]['v5'] >= 0.0
            and table[T_HI][c]['v5'] < 0.0 for c in BIND)
cert3 = all(table[t][c]['L'] >= 0.0 and table[t][c]['v5'] >= 0.0
            for t in W if t <= T_LO + 1e-12 for c in BIND)
cert4_min = {}
cert4 = True
for t in W:
    if t <= T_HI + 1e-12:
        for c in NONBIND:
            v = rows['g5'][t]['clause_minima'][c]
            cert4_min[c] = min(cert4_min.get(c, v), v)
            if not v > 0.0:
                cert4 = False
bars = res['nonclause_bars_g5']
bars_ok = True
for kk, b in bars.items():
    ok = (b['mom_worst'] <= 1e-10 and b['flare_min'] > 0
          and b['domain_R_min'] > 0 and b['domain_exp2Phi_min'] > 0)
    bars_ok = bars_ok and ok and bool(b['pass'])
cert4 = cert4 and bars_ok
out['CERT'] = {'CERT-1': cert1, 'CERT-2': cert2, 'CERT-3': cert3,
               'CERT-4': cert4, 'CERT-4_bars': bars_ok,
               'CERT-4_nonbinding_G5_min_over_window_le_thi':
               cert4_min}
out['worker_CERT'] = {k: res['cert'][k]['pass'] for k in
                      ('CERT-1', 'CERT-2', 'CERT-3', 'CERT-4')}
out['CERT_agree_with_worker'] = bool(
    cert1 == res['cert']['CERT-1']['pass']
    and cert2 == res['cert']['CERT-2']['pass']
    and cert3 == res['cert']['CERT-3']['pass']
    and cert4 == res['cert']['CERT-4']['pass'])

# Window worsts (gate-computed)
worsts = {}
for c in BIND:
    worsts[c] = {
        'max_abs_d34': max(abs(table[t][c]['d34']) for t in W),
        'max_abs_d45': max(abs(table[t][c]['d45']) for t in W),
        'max_r': max(table[t][c]['r'] for t in W),
        'worst_d34_at': max(W, key=lambda t: abs(table[t][c]['d34'])),
        'worst_r_at': max(W, key=lambda t: table[t][c]['r'])}
out['window_worsts_gate'] = worsts
out['window_worsts_worker'] = res['window_worsts']
out['bracket_limits'] = {
    c: {'L_lo': table[T_LO][c]['L'], 'L_hi': table[T_HI][c]['L'],
        'v5_lo': table[T_LO][c]['v5'], 'v5_hi': table[T_HI][c]['v5'],
        'case_lo': table[T_LO][c]['case'],
        'case_hi': table[T_HI][c]['case']} for c in BIND}

# CTRL-3 at t = 0.5 from the stored rows
out['ctrl3_from_rows'] = {
    c: {'d34': table[0.5][c]['d34'], 'd45': table[0.5][c]['d45']}
    for c in BIND}
out['controls_recorded'] = {
    k: (v.get('pass') if isinstance(v, dict) else v)
    for k, v in res['controls'].items()}
out['probe'] = {k: res['probe'][k] for k in
                ('wall_s', 'projected_full_wall_s', 'threshold_s',
                 'fires')}

# Span record, gate-computed from Phase 288's stored rows
p288 = json.load(open(WP + 'phase288/results/p288_results.json'))
span = [r for r in p288['member_instants']
        if float(r['t']) <= 0.575 + 1e-9]
out['span_n_instants'] = len(span)
span_min = {}
for c in CK:
    vals = [(float(r['clause_minima'][c]), float(r['t']))
            for r in span]
    vmin, tmin = min(vals)
    span_min[c] = {'min': vmin, 'at_t': tmin}
out['span_minima_gate'] = span_min
wspan = res['span_record']['per_clause_minima']
span_dev = 0.0
for c in CK:
    span_dev = max(span_dev, abs(wspan[c]['min'] - span_min[c]['min']),
                   abs(wspan[c]['t_at_min'] - span_min[c]['at_t']))
out['span_worker_max_deviation'] = span_dev
out['span_crosscheck_recorded'] = res['span_record']['crosscheck_pass']

json.dump(out, open(WP + 'gate31/work/g31_verify_results.json', 'w'),
          indent=1)
print(json.dumps({k: out[k] for k in
                  ('nec_dec_ph_identity_max_abs_diff',
                   'worker_table_max_deviation',
                   'worker_table_case_mismatches', 'CERT',
                   'CERT_agree_with_worker', 'window_worsts_gate',
                   'bracket_limits', 'ctrl3_from_rows',
                   'span_n_instants', 'span_minima_gate',
                   'span_worker_max_deviation')}, indent=1))
