#!/usr/bin/env python3
"""
g52_run.py -- Gate-52 controls and deciding reads (VM).
Controls first: the Phase 400 static base and the Gate-50
criterion winner must reproduce their stored values before
any Phase 412 number is believed. Then the deciding reads
for claims (a) and (b). Output:
gate52/results/g52_numbers.json.
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g52_lib as G   # noqa: E402

WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
OUT = f'{WP}/gate52/results/g52_numbers.json'
out = {}


def diff(a, b):
    return float(a - b)


# ================= CONTROLS =================
t0 = time.time()
ctl = {}
# CTL-G52-BASE: Phase 400 static winner (S = 0)
s, R = G.set_read(None, 9)
w = G.INP['winner400']
wn = G.worst_null_certified(
    G.that_at(None, 9, np.array(s['nec_argmin_point'])[None, :])[0])
ctl['BASE'] = {
    'gate': s, 'worst_null_at_argmin': wn,
    'stored': w,
    'diffs': {
        'joint': diff(s['joint'], w['joint']),
        'nec': diff(s['nec']['min'], w['nec_min']),
        'dec': diff(s['dec']['min'], w['dec_min']),
        'wec': diff(s['wec']['min'], w['wec_min']),
        'sec': diff(s['sec']['min'], w['sec_min']),
        'rho': diff(s['rho']['min'], w['rho_min']),
        'worst_null': diff(wn['worst_null'],
                           1.3977194851281464e-06),
    },
    'argmin_r_match': bool(s['nec_argmin_r'] == w['nec_argmin_r']),
    'typeI_match': bool(s['typeI_fraction'] == w['typeI_fraction']),
}
print('CTL BASE done', time.time() - t0, flush=True)

# CTL-G52-CRIT: the Gate-50 criterion winner
s, R = G.set_read(G.SHAPEC_CRIT, 9)
ac = G.INP['conf405']['at_criterion']
wn = G.worst_null_certified(
    G.that_at(G.SHAPEC_CRIT, 9,
              np.array(s['nec_argmin_point'])[None, :])[0])
pr = G.phys_row(G.SHAPEC_CRIT, 9, s['nec_argmin_r'])
ctl['CRIT'] = {
    'gate': s, 'worst_null_at_argmin': wn, 'phys_row': pr,
    'stored': ac,
    'diffs': {
        'joint': diff(s['joint'], ac['joint']),
        'nec': diff(s['nec']['min'], ac['nec_min']),
        'dec': diff(s['dec']['min'], ac['dec_min']),
        'sec': diff(s['sec']['min'], ac['sec_min']),
        'rho': diff(s['rho']['min'], ac['rho_min']),
        'worst_null': diff(wn['worst_null'],
                           ac['worst_null_at_nec_argmin']),
        'worst_null_fib_stored': ac['worst_null_fib'],
        'peak': diff(pr['peak_fine'],
                     float(G.INP['conf405']['criterion_peak'])),
    },
    'argmin_r_match': bool(s['nec_argmin_r'] == ac['nec_argmin_r']),
    'typeI_match': bool(s['typeI_fraction']
                        == ac['typeI_fraction']),
}
out['controls'] = ctl
print('CTL CRIT done', time.time() - t0, flush=True)

# ================= (a) THE P* CANDIDATE (m = 2) =================
a = {}
s, R = G.set_read(G.M2_VS, 9)
conf = G.INP['rungs412']['m2']['confirmation']
wn = G.worst_null_certified(
    G.that_at(G.M2_VS, 9,
              np.array(s['nec_argmin_point'])[None, :])[0])
pr = G.phys_row(G.M2_VS, 9, s['nec_argmin_r'])
a['set'] = s
a['worst_null_at_argmin'] = wn
a['phys_row'] = pr
a['stored_confirmation'] = conf
a['diffs'] = {
    'joint': diff(s['joint'], conf['joint']),
    'nec': diff(s['nec']['min'], conf['nec_min']),
    'dec': diff(s['dec']['min'], conf['dec_min']),
    'wec': diff(s['wec']['min'], conf['wec_min']),
    'sec': diff(s['sec']['min'], conf['sec_min']),
    'rho': diff(s['rho']['min'], conf['rho_min']),
    'typeI_nec_min': diff(s['typeI_nec_min'],
                          conf['typeI_nec_min']),
    'worst_null': diff(wn['worst_null'],
                       conf['worst_null_at_nec_argmin']),
    'worst_null_fib_stored': conf['worst_null_fib'],
    'peak_fine': diff(pr['peak_fine'], conf['peak']),
}
a['argmin_r_match'] = bool(s['nec_argmin_r']
                           == conf['nec_argmin_r'])
a['typeI_match'] = bool(s['typeI_fraction']
                        == conf['typeI_fraction'])
# peak provenance: H2's own peak on the same phys-row form
h2S = G.h2_totals(G.FINE_R)[0]
a['h2_peak_fine'] = float(np.max(np.abs(G.BETA * h2S)))
a['h2_peak_radius'] = float(G.FINE_R[int(np.argmax(
    np.abs(G.BETA * h2S)))])
a['h2_S_at_10'] = float(G.h2_totals(np.array([10.0]))[0][0])
a['winner_S_at_10'] = float(
    G.config_profiles(np.array([10.0]), G.M2_VS, 9)[0][0])
a['target_peak'] = float(G.INP['rungs412']['m2']['target_peak'])
a['peak_minus_target'] = float(pr['peak_fine']
                               - a['target_peak'])
a['peak_minus_h2peak'] = float(pr['peak_fine']
                               - a['h2_peak_fine'])
out['claim_a_m2'] = a
print('claim (a) done', time.time() - t0, flush=True)

# ================= (b) THE CEILING BRACKET (m = 5) =================
b = {}
for tag, vs, K in (('K17', G.M5K17_VS, 17), ('K9', G.M5K9_VS, 9)):
    s, R = G.set_read(vs, K)
    if tag == 'K17':
        conf = G.INP['rungs412']['m5']['confirmation']
    else:
        conf = G.INP['screens412']['523']
    wn = G.worst_null_certified(
        G.that_at(vs, K,
                  np.array(s['nec_argmin_point'])[None, :])[0])
    # worst null also at the DEC argmin point (frame-invariant
    # companion for the Type-I NEC minimum's neighbourhood)
    entry = {
        'set': s, 'worst_null_at_nec_argmin': wn,
        'stored': conf,
        'diffs': {
            'joint': diff(s['joint'], conf['joint']),
            'nec': diff(s['nec']['min'], conf['nec_min']),
            'dec': diff(s['dec']['min'], conf['dec_min']),
            'wec': diff(s['wec']['min'], conf['wec_min']),
            'sec': diff(s['sec']['min'], conf['sec_min']),
            'rho': diff(s['rho']['min'], conf['rho_min']),
            'typeI_fraction': diff(s['typeI_fraction'],
                                   conf['typeI_fraction']),
        },
        'argmin_r_match': bool(s['nec_argmin_r']
                               == conf['nec_argmin_r']),
    }
    if tag == 'K17':
        entry['diffs']['typeI_nec_min'] = diff(
            s['typeI_nec_min'], conf['typeI_nec_min'])
        entry['diffs']['worst_null'] = diff(
            wn['worst_null'], conf['worst_null_at_nec_argmin'])
        entry['worst_null_fib_stored'] = \
            conf['worst_null_fib']
    b[tag] = entry
    print('claim (b)', tag, 'done', time.time() - t0, flush=True)
out['claim_b_m5'] = b

with open(OUT, 'w') as f:
    json.dump(out, f, indent=1)
print('wrote', OUT, 'in', time.time() - t0, 's')
