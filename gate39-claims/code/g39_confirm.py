#!/usr/bin/env python3
"""Gate-39 A-3 confirmation polish + A-4 anatomy checks.
Reads gate39/results/g39_scan.json and g39_refine.json (merged, mine).
Writes gate39/results/g39_confirm.json."""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate39/work')
import g39_lib as G  # noqa: E402
from g39_members import enumerate_members  # noqa: E402

BASE = '/home/hatch/workspace/warp-pilot/'
L_STAT = -2.319453132752996e-4
NEC_STAT = -2.319453132752996e-4
DEC_STAT = -2.2336932044559818e-4

conf = json.load(open(BASE + 'phase344/results/p344_confirmation.json'))
a2 = [e for e in conf['confirmations'] if e['point'] == 'A2'][0]
centre = G.Centre(a2['vS'], a2['vN'], a2['vM'], 33, m_r2=20.0)
by_id = {m['id']: m for m in enumerate_members()}
scan = json.load(open(BASE + 'gate39/results/g39_scan.json'))
refine = json.load(open(BASE + 'gate39/results/g39_refine.json'))

CANDS = ['SNM_a0.30_T160_D0.750_m0.75', 'M_a0.30_T160_D0.750_m0.75',
         'SNM_a0.15_T160_D0.750_m0.75', 'M_a0.15_T160_D0.750_m0.75']

out = {'candidates': CANDS, 'confirmations': {}}
for mid in CANDS:
    mem = by_id[mid]
    r128 = refine['audits'][f'{mid}@J128']
    entry = {}
    for label, phi_key, val_key in (('nec_worst', 'nec_worst_phi', 'NEC_worst'),
                                    ('dec_worst', 'dec_worst_phi', 'DEC_worst')):
        phi = r128[phi_key]
        t0 = time.time()
        sread, aux = G.set_read(centre, mem, phi)
        pol = G.adversary_polish(centre, mem, phi, aux)
        n_fin, wn, wn_fib = G.worst_null(aux['nec_argmin_That'])
        entry[label] = {
            'phi': phi, 't': phi / mem['Om'],
            'set_nec_min': sread['nec']['min'],
            'set_dec_min': sread['dec']['min'],
            'set_rho_min': sread['rho']['min'],
            'set_nec_argmin_r': sread['nec_argmin_r'],
            'polish': pol,
            'polished_depth': pol['in_region_worst_nec_SAMPLER-M'],
            'C2_bar': -0.0034,
            'C2_pass': bool(pol['in_region_worst_nec_SAMPLER-M'] > -0.0034),
            'worst_null': {'direction': n_fin.tolist(), 'value': wn,
                           'fib642_min': wn_fib,
                           'diff_vs_set_nec_min': float(wn - sread['nec']['min'])},
            'wall_s': time.time() - t0}
        print(mid, label, 'phi', phi, 'polished',
              pol['in_region_worst_nec_SAMPLER-M'], 'worst_null', wn,
              flush=True)
    out['confirmations'][mid] = entry

# ---------------- A-4 anatomy
anat = {}
# (i) Arm-1 table: m=0 members
arm1 = []
for mid, summ in scan.items():
    if mid == 'ANCHOR':
        continue
    if summ['member']['m'] == 0.0:
        arm1.append({'member': mid, 'DEC_worst': summ['DEC_worst'],
                     'L_worst': summ['L_worst'],
                     'dec_carries_L_worst': bool(summ['L_worst'] == summ['DEC_worst']),
                     'dec_saturated_le_-0.99': bool(summ['DEC_worst'] <= -0.99)})
anat['arm1_m0_table'] = arm1
anat['arm1_all_dec_saturated'] = bool(all(r['dec_saturated_le_-0.99'] for r in arm1))
anat['arm1_count'] = len(arm1)
# (ii) winners' DEC-worst phases at J=128
anat['winners_dec_worst_phi_J128'] = {
    mid: refine['audits'][f'{mid}@J128']['dec_worst_phi'] for mid in CANDS}
# (iii) T=40 m=0.75 members' L_worst vs L_stat
t40 = {}
for mid, summ in scan.items():
    if mid == 'ANCHOR':
        continue
    mm = summ['member']
    if mm['m'] == 0.75 and abs(mm['Om'] - 2 * np.pi / 40.0) < 1e-12:
        t40[mid] = {'L_worst': summ['L_worst'],
                    'shortfall_vs_L_stat': float(summ['L_worst'] - L_STAT)}
anat['T40_m0.75_L_worst'] = t40
# (iv) bottom-point check: constant-mu stationary reads
bottom = {}
for a, mu_c, tgt in ((0.30, 1.15, -1.854699e-4), (0.15, 1.075, -2.032703e-4)):
    row = {'mu': mu_c, 'target_dec_min': tgt}
    for subset in ('SNM', 'M'):
        mem = {'subset': subset, 'a': a, 'Om': 2 * np.pi / 160.0,
               'D': 0.75, 'm': 0.75, 'id': f'bottom_{subset}_{a}'}
        o, _ = G.set_read(centre, mem, np.pi,
                          mu_override=(mu_c, 0.0, 0.0), want_aux=False)
        row[f'{subset}_dec_min'] = o['dec']['min']
        row[f'{subset}_nec_min'] = o['nec']['min']
        row[f'{subset}_dec_diff_vs_target'] = float(o['dec']['min'] - tgt)
    bottom[f'a{a}'] = row
    print('bottom', a, row, flush=True)
anat['bottom_point_check'] = bottom
out['anatomy'] = anat

with open(BASE + 'gate39/results/g39_confirm.json', 'w') as f:
    json.dump(out, f, indent=1)
print('CONFIRM DONE', flush=True)
