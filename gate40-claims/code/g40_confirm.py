#!/usr/bin/env python3
"""Gate-40 confirmation stage (runs after g40_audit):
1. Stationary scaled reads at constant mu (bottom identity): for each
   subset {M, SNM} and mu in {1.075, 1.1125, 1.15, 1.225, 1.30}:
   NEC/DEC minima of the centre scaled by constant mu.
2. Waveform facts at phi=pi for the champion (mu, mu_dot, mu_ddot).
3. For the 12 candidates (from the gate's own J=128 audits): adversary
   polish (C2) at the NEC-worst and DEC-worst instants, and the exact
   pointwise worst-null at each such instant's SET NEC argmin.
Outputs ../results/g40_confirm.json."""
import json
import os
import sys
import numpy as np
sys.path.insert(0, '.')
import g40_lib as G
from g40_members import FAMILY374, bottom_mu

conf = json.load(open('../../phase344/results/p344_confirmation.json'))
a2 = [c for c in conf['confirmations'] if c['point'] == 'A2'][0]
cen = G.Centre(a2['vS'], a2['vN'], a2['vM'])

L364 = -2.169047936502377e-4
TOL = 1.0e-6
out = {}

# 1. stationary scaled reads
scaled = {}
for sub_name, subset in (('M', {'M'}), ('SNM', {'S', 'N', 'M'})):
    for mu in (1.075, 1.1125, 1.15, 1.225, 1.30):
        mem = {'name': f'scaled_{sub_name}_{mu}', 'subset': subset,
               'a': 0.0, 'T': None, 'Om': 1.0, 'D': 0.75, 'm': 0.75}
        o = G.set_read(cen, mem, 0.0, mu_const=mu)
        scaled[f'{sub_name}@{mu}'] = {'nec': o['nec']['min'],
                                      'dec': o['dec']['min'],
                                      'rho_min': o['rho']['min']}
        print('scaled', sub_name, mu, o['nec']['min'], o['dec']['min'], flush=True)
out['stationary_scaled'] = scaled

# 2. waveform facts for the champion at phi = pi
champ = [m for m in FAMILY374 if m['name'] == 'SNM_a0.15_T640_D0.750_m0.88'][0]
mu, mud, mudd = G.member_mu(champ, np.pi)
out['champion_at_pi'] = {'mu': mu, 'mu_dot': mud, 'mu_ddot': mudd,
                         'bottom_mu_registered': bottom_mu(champ)}

# 3. candidates from the gate's J=128 audits
cands = []
for mem in FAMILY374:
    a = json.load(open(f"../results/parts/{mem['name']}@J128.json"))
    if a['L_worst'] >= L364 + TOL:
        cands.append((mem, a))
out['n_candidates_gate'] = len(cands)
print('gate candidates:', len(cands), flush=True)

confirms = {}
for mem, a in cands:
    entry = {}
    for tag, phi in (('nec_worst', a['nec_worst_phi']),
                     ('dec_worst', a['dec_worst_phi'])):
        o, aux = G.set_read(cen, mem, phi, want_aux=True)
        pol = G.adversary_polish(cen, mem, phi, aux)
        wn_pol, wn_scan = G.worst_null(aux['nec_argmin_That'])
        entry[tag] = {
            'phi': phi,
            'set_nec': o['nec']['min'], 'set_dec': o['dec']['min'],
            'nec_argmin_typeI': o['nec_argmin_typeI'],
            'polish_worst_nec': pol['worst_nec'] if pol else None,
            'polish_pass_bar': (pol['worst_nec'] > G.BAR_DEPTH) if pol else None,
            'worst_null': wn_pol, 'worst_null_scan': wn_scan,
            'worst_null_minus_set_nec': wn_pol - o['nec']['min']}
        print(mem['name'], tag, 'polish', entry[tag]['polish_worst_nec'],
              'wn-set', entry[tag]['worst_null_minus_set_nec'], flush=True)
    confirms[mem['name']] = entry
out['confirmations'] = confirms

json.dump(out, open('../results/g40_confirm.json', 'w'), indent=1)
print('DONE')
