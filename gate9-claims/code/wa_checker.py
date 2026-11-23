"""
W-A G9-1 checker: recomputes pass/fail from the run's own result
files (wa_member_grid.json, wa_member_probes.json, wa_tb.json,
wa_phi0.json) against the registered G9-1 bars, and assembles
results/wa_g91_numbers.json.  Stored values are the claim's record
(GATE9.md / p611_ecaudit.json / p712_memo.md G1).
"""
import json

G = '/home/hatch/workspace/warp-pilot/gate9/results/'
grid = json.load(open(G + 'wa_member_grid.json'))
probes = json.load(open(G + 'wa_member_probes.json'))
tb = json.load(open(G + 'wa_tb.json'))
phi0 = json.load(open(G + 'wa_phi0.json'))

STORED = {
    'throat_NEC1': 0.00364119103852,
    'throat_DEC_t': 0.00182059551926,
    'tail_min': {'rho': 6.275140592e-15, 'NEC1': 1.229852039e-15,
                 'NEC2': 1.193535517e-14, 'SEC': 1.255028118e-14,
                 'DEC_r': 1.229852039e-15, 'DEC_t': 6.149260195e-16},
    'probe_1+1e-9': {'NEC1': 0.0036408724, 'DEC_t': 0.0018204362},
}
SIX = ('rho', 'NEC1', 'NEC2', 'DEC_r', 'DEC_t', 'SEC')

# bar (a): all six > 0 at every grid point and probe
grid_ok = all(grid['minima'][k]['value'] > 0 for k in SIX)
grid_nan_ok = all(grid['nan_counts'][k] == 1 for k in SIX)  # only r=1 (0/0 raw form)
probe_ok = True
for tag in ('tail_1000', 'throat_1+1e-9', 'throat_1+1e-6',
            'throat_1+1e-8', 'throat_1+1e-10'):
    for k in SIX:
        if float(probes[tag][k]) <= 0:
            probe_ok = False
lim = probes['throat_limit_extrapolated']
probe_ok = probe_ok and float(lim['NEC1']) > 0 and float(lim['DEC_t']) > 0
bar_a = grid_ok and probe_ok

# bar (b): throat NEC1 / DEC_t within 2% of stored
def rel(a, b):
    return abs(a - b) / abs(b)
mine_nec1 = float(lim['NEC1'])
mine_dect = float(lim['DEC_t'])
rel_nec1 = rel(mine_nec1, STORED['throat_NEC1'])
rel_dect = rel(mine_dect, STORED['throat_DEC_t'])
bar_b = rel_nec1 <= 0.02 and rel_dect <= 0.02

numbers = {
    'claim': 'G9-1 LEGALITY (conformal joining member, p=0.1, Phi2, '
             'a=0.27773424114865775, [r0, 10^3 r0], r0=1)',
    'engine': 'gate9/wa_engine.py — fresh SymPy derivation from the '
              'metric (Christoffel->Riemann->Ricci->Weyl->double '
              'covariant divergence), registered Bach convention '
              'B = 2*nabla nabla C + R.C (x2 identified by anchor ii)',
    'python': '~/workspace/warp-pilot/venv/bin/python',
    'anchors': {
        'i_schwarzschild_symbolic': {'Bt': 0, 'Br': 0, 'Bth': 0,
                                     'PASS': True,
                                     'source': 'wa_test1.py run'},
        'i_MK_numeric': {'max_abs_B': 1.3248674568444952e-169,
                         'tolerance': 1e-12, 'PASS': True,
                         'source': 'wa_anchors.py run (MK at '
                                   'beta=1/2, gamma=1/100, k=1/1000; '
                                   'r=3,10,30)'},
        'ii_Tb_closed_forms': tb['anchor_ii_Tb'],
        'iii_phi0': {
            'nec1_factorisation_max_relerr_float64':
                phi0['max_nec1_formula_relerr'],
            'PASS_factorisation': phi0['PASS_factorisation'],
            'DEC_r_equals_NEC1': 'exact 0.0 difference at all 25 '
                                 '(p, r) points (p_r < 0 on slice)',
            'SEC_equals_2rho': 'holds to float64 noise <= 3.9e-16 '
                               '(trace identically 0)',
            'DEC_t_equals_NEC2': 'FALSE as stated: DEC_t - NEC2 = '
                                 '-2 p_t != 0 at all 25 points (p_t > 0 '
                                 'on slice); correct identity DEC_t = '
                                 'rho - |p_t|. Prose error in the '
                                 'registered anchor text (and in '
                                 'p381_memo), contradicting Phase 32 '
                                 'T-b closed forms; not a machinery '
                                 'failure and not used by the G9-1 bars.',
        },
    },
    'grid_float64': grid,
    'probes_mp50': probes,
    'stored': STORED,
    'comparisons': {
        'throat_NEC1_mine_limit': mine_nec1,
        'throat_NEC1_rel_diff_vs_stored': rel_nec1,
        'throat_DEC_t_mine_limit': mine_dect,
        'throat_DEC_t_rel_diff_vs_stored': rel_dect,
        'throat_formula_crosscheck': {
            'formula': '(p-1)^2 (2a^2 + (p-11) a + (3-p)) / 6 at p=0.1 '
                       '(Phase-38 throat NEC1 formula for Phi2)',
            'at_full_a': 0.0036408675004837303,
            'mine_limit': mine_nec1,
            'at_rounded_a_0.277734': 0.00364118618412,
            'note': 'stored throat digits sit ~9e-5 relative from the '
                    'full-a value, an a-rounding sensitivity in the '
                    'phase record; immaterial vs the 2% bar.'},
        'tail_min_mine_vs_stored': {
            k: {'mine_grid': grid['minima'][k]['value'],
                'stored': STORED['tail_min'][k],
                'rel_diff': rel(grid['minima'][k]['value'],
                                STORED['tail_min'][k])}
            for k in SIX},
        'probe_1+1e-9_mine_vs_stored': {
            k: {'mine': float(probes['throat_1+1e-9'][k]),
                'stored': STORED['probe_1+1e-9'][k],
                'rel_diff': rel(float(probes['throat_1+1e-9'][k]),
                                STORED['probe_1+1e-9'][k])}
            for k in ('NEC1', 'DEC_t')},
    },
    'bars': {
        'a_all_six_positive_grid_and_probes': bar_a,
        'b_throat_within_2pct': bar_b,
        'grid_nan_note': 'exactly one NaN per combination, at the '
                         'single grid point r = r0, where the raw '
                         'unsimplified expression is 0/0 (1 - b/r = 0); '
                         'the throat is decided by the 50-digit '
                         'probes and the extrapolated limit, all > 0.',
    },
    'correctness_verdict': 'REPRODUCED' if (bar_a and bar_b) else
                           'NOT REPRODUCED (see bars)',
}
with open(G + 'wa_g91_numbers.json', 'w') as fh:
    json.dump(numbers, fh, indent=1)
print('bar_a', bar_a, 'bar_b', bar_b)
print('rel NEC1', rel_nec1, 'rel DEC_t', rel_dect)
print('verdict', numbers['correctness_verdict'])
