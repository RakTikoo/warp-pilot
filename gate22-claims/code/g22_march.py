#!/usr/bin/env python
"""GATE-22 attack lines (b) and (e): fresh-process re-run of the
kappa=0 and director (P-DIR-T2, m=1, kappa=0.3) marches on grids
G1..G4, using the programme's own machinery (phase162 march,
phase167 reads, phase207 T2 engine) but Gate-22's own driver,
gate construction and comparisons. Also (c): the interval-edge
pricing from the director G4 per-instant minima produced here
and the stored Phase 207 G2 minima. GATE-22 internal.
"""
import json, math, sys, time
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase207/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase162/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase167/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase150/work')
import p1621_engine as B          # noqa: E402
import p167_engine as E          # noqa: E402
import p2071_engine as D         # noqa: E402

CK = list(B.CLAUSE_KEYS)
GRIDS = {'G1': (1441, 0.005), 'G2': (2881, 0.0025),
         'G3': (5761, 0.00125), 'G4': (11521, 0.000625)}
BAR = 1e-6
T0 = time.time()
out = {'frame': 'venv python, Phase 166 pin, Gate-19 tensor'}


def run_grid(n_th, h_t, director=False):
    th_f, times, MU, U = B.march(n_th, h_t)
    h_f = th_f[1] - th_f[0]
    MTT = E.mtt_field(U, h_t)
    stride = int(round(0.025 / h_t))
    rows = []
    for si in range(21):
        m = si * stride
        if director:
            rec, _, _, _ = D.instant_read_dir_T2(
                m, times, MU, U, MTT, th_f, h_f, h_t, 1, 0.3)
            rows.append({
                't': rec['t'], 'clause_minima': rec['clause_minima'],
                'mom_worst': max(rec['mom_resid_max'].values()),
                'flare_min': rec['flare_min'],
                'domain_R_min': rec['domain_R_min'],
                'domain_exp2Phi_min': rec['domain_exp2Phi_min']})
        else:
            rec, _, _ = E.instant_read_comp(m, times, MU, U, MTT,
                                            th_f, h_f, h_t)
            rows.append({'t': rec['t'],
                         'clause_minima': rec['clause_minima'],
                         'mom_worst': max(rec['mom_resid_max'].values())})
    return rows


def gate(rows_a, rows_b):
    per = []
    for ra, rb in zip(rows_a, rows_b):
        d = {k: abs(ra['clause_minima'][k] - rb['clause_minima'][k])
             for k in CK}
        per.append({'t': ra['t'], 'per_clause': d,
                    'max': float(max(d.values()))})
    w = max(per, key=lambda a: a['max'])
    return {'value': float(w['max']), 'worst_instant': float(w['t']),
            'per_clause_at_worst': w['per_clause'],
            'per_clause_max': {k: max(p['per_clause'][k] for p in per)
                               for k in CK},
            'per_instant_max': [p['max'] for p in per]}


def rich(d_a, d_b):
    p = math.log2(d_a / d_b)
    return p, d_b * 2.0 ** p / (2.0 ** p - 1.0)


# ---- kappa=0 marches, all four grids --------------------------------
rows0 = {}
for g, (n, h) in GRIDS.items():
    rows0[g] = run_grid(n, h, director=False)
    print(g, 'kappa0 done %.1fs' % (time.time() - T0), flush=True)

# (e) control identity on G2
nec = [r['clause_minima']['NEC_ph'] for r in rows0['G2']]
ts = [r['t'] for r in rows0['G2']]
first_fail = next((t for t, v in zip(ts, nec) if v < -1e-9), None)
out['control_e'] = {
    'first_NEC_ph_failure_t': first_fail,
    'worst_NEC_ph_G2': float(min(nec)),
    'expected_first_fail': 0.400,
    'expected_worst': -0.6297872673028908,
    'worst_abs_diff': abs(min(nec) - (-0.6297872673028908))}

D12 = gate(rows0['G1'], rows0['G2'])
D23 = gate(rows0['G2'], rows0['G3'])
D34 = gate(rows0['G3'], rows0['G4'])
p34, L34 = rich(D23['value'], D34['value'])
p23, L23 = rich(D12['value'], D23['value'])
out['kappa0_gates'] = {
    'D12': D12['value'], 'D12_worst_t': D12['worst_instant'],
    'D23': D23['value'], 'D23_worst_t': D23['worst_instant'],
    'D34': D34['value'], 'D34_worst_t': D34['worst_instant'],
    'D34_per_clause_at_worst': D34['per_clause_at_worst'],
    'D34_per_clause_max': D34['per_clause_max'],
    'p23': p23, 'L23': L23, 'p34': p34, 'L34': L34,
    'stored': {'D12': 5.82636026180694e-6, 'D23': 1.359258471111957e-6,
               'D34': 2.5300142314499396e-7,
               'L34': 3.108629483945071e-7},
    'diffs_vs_stored': {
        'D12': abs(D12['value'] - 5.82636026180694e-6),
        'D23': abs(D23['value'] - 1.359258471111957e-6),
        'D34': abs(D34['value'] - 2.5300142314499396e-7),
        'L34': abs(L34 - 3.108629483945071e-7)}}

# ---- director marches G3, G4 ----------------------------------------
rowsd = {}
for g in ('G3', 'G4'):
    n, h = GRIDS[g]
    rowsd[g] = run_grid(n, h, director=True)
    print(g, 'director done %.1fs' % (time.time() - T0), flush=True)

gd = gate(rowsd['G3'], rowsd['G4'])
worst = min((r['clause_minima'][k], r['t'], k)
            for r in rowsd['G4'] for k in CK)
out['director'] = {
    'gate_dir_G3_G4': gd['value'],
    'gate_dir_worst_t': gd['worst_instant'],
    'gate_dir_per_clause_at_worst': gd['per_clause_at_worst'],
    'gate_dir_equals_kappa0_D34': bool(gd['value'] == D34['value']),
    'gate_dir_absdiff_vs_D34': abs(gd['value'] - D34['value']),
    'worst_clause_min_G4': worst[0], 'worst_clause': worst[2],
    'worst_clause_t': worst[1],
    'stored_worst_clause_min_G4': 0.0045418770853060675,
    'worst_abs_diff_vs_stored': abs(worst[0] - 0.0045418770853060675),
    'momentum_worst_G4': max(r['mom_worst'] for r in rowsd['G4']),
    'flare_min_G4': min(r['flare_min'] for r in rowsd['G4']),
    'domain_R_min_G4': min(r['domain_R_min'] for r in rowsd['G4']),
    'domain_exp2Phi_min_G4':
        min(r['domain_exp2Phi_min'] for r in rowsd['G4']),
    'per_clause_worst_G4': {k: min(r['clause_minima'][k]
                                    for r in rowsd['G4']) for k in CK},
    'NEC_ph_minima_G4': [r['clause_minima']['NEC_ph']
                         for r in rowsd['G4']],
    'NEC_ph_minima_G3': [r['clause_minima']['NEC_ph']
                         for r in rowsd['G3']],
    'instants': [r['t'] for r in rowsd['G4']]}

# ---- pointwise shift-identity check (attack on the "identically
# zero" carrier claim), one G2 instant, t = 0.5 ----------------------
th_f, times, MU, U = B.march(*GRIDS['G2'])
h_f = th_f[1] - th_f[0]
MTT = E.mtt_field(U, GRIDS['G2'][1])
m = int(round(0.5 / GRIDS['G2'][1]))
rec, J, ch_dir, ch_ctrl = D.instant_read_dir_T2(
    m, times, MU, U, MTT, th_f, h_f, GRIDS['G2'][1], 1, 0.3)
cl_dir = B.clauses_of(ch_dir['rho8'], ch_dir['prho8'],
                      ch_dir['pth8'], ch_dir['pph8'])
cl_ctl = B.clauses_of(ch_ctrl['rho8'], ch_ctrl['prho8'],
                      ch_ctrl['pth8'], ch_ctrl['pph8'])
cm = D.c_m_dir_T2(B.AUDIT_TH, J['A'], J['Ah'], 1)
out['shift_identity_G2_t0.5'] = {
    k: float(np.max(np.abs(cl_dir[k] - cl_ctl[k])))
    for k in ['NEC_rho', 'DEC_rho', 'NEC_th']}
out['shift_identity_G2_t0.5']['NEC_ph_shift_vs_kappa_cm_maxdiff'] = \
    float(np.max(np.abs((cl_dir['NEC_ph'] - cl_ctl['NEC_ph'])
                        - 0.3 * cm)))
out['shift_identity_G2_t0.5']['WEC_shift_vs_half_kappa_cm_maxdiff'] = \
    float(np.max(np.abs((cl_dir['WEC'] - cl_ctl['WEC'])
                        - 0.15 * cm)))

# ---- (c) interval edge: decline of the director NEC_ph minimum ----
g4 = out['director']['NEC_ph_minima_G4']
tt = out['director']['instants']
stored207 = json.load(open('/home/hatch/workspace/warp-pilot/phase207/'
                           'results/p2071_results.json'))
# Phase 207 stored director fine per-instant NEC_ph minima (G2)
try:
    d207 = stored207['march_director_fine']
    g2 = [r['clause_minima']['NEC_ph'] for r in d207]
except Exception as e:  # structure differs; report the miss
    g2 = None
    out['edge_note'] = 'P207 stored structure lookup failed: %s' % e


def edge_stats(vals, ts_):
    v = np.array(vals); t = np.array(ts_)
    # secant slopes over the last 0.1 and last 0.2 of the interval,
    # and a least-squares slope over the last five instants
    s_last = (v[-1] - v[-2]) / (t[-1] - t[-2])
    s_01 = (v[-1] - v[-5]) / (t[-1] - t[-5])
    s_02 = (v[-1] - v[-9]) / (t[-1] - t[-9])
    A_ = np.polyfit(t[-5:], v[-5:], 1)
    return {'margin_at_0.5': float(v[-1]),
            'slope_last_step': float(s_last),
            'slope_last_0.1': float(s_01),
            'slope_last_0.2': float(s_02),
            'lsq_slope_last5': float(A_[0]),
            'linear_zero_crossing_from_last_step_slope':
                float(t[-1] + v[-1] / abs(s_last)) if s_last < 0 else None,
            'linear_zero_crossing_from_last_0.1_slope':
                float(t[-1] + v[-1] / abs(s_01)) if s_01 < 0 else None,
            'series_tail': [float(x) for x in v[-9:]]}


out['edge'] = {'G4': edge_stats(g4, tt)}
if g2 is not None:
    out['edge']['G2_P207_stored'] = edge_stats(g2, tt)
out['elapsed_s'] = time.time() - T0

with open('/home/hatch/workspace/warp-pilot/gate22/work/'
          'g22_march_results.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps({k: out[k] for k in
                  ('control_e', 'kappa0_gates', 'director',
                   'shift_identity_G2_t0.5', 'edge')}, indent=1)[:6000])
print('elapsed %.1fs' % out['elapsed_s'])
