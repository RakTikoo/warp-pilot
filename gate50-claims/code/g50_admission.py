#!/usr/bin/env python3
"""
g50_admission.py -- Gate-50 laptop admission control.
Runs ON THE LAPTOP (frame-of-record candidate): the
gate's own SET-244 reads of the Phase 405 winner and
the Phase 400 base winner, through the same g50_lib
machinery. The VM compares the returned five minima,
Type-I fractions and joints against its own reads
(g50_numbers.json) and rules admission by the
lineage precedent: roundoff agreement -> ADMITTED;
C-10-signature drift on sampled statistics -> NOT
ADMITTED for sampled statistics (deciding reads stay
on the VM either way).
"""
import json
import os
import sys

WP = os.environ.get('G50_WP', os.path.expanduser('~/work'))
sys.path.insert(0, f'{WP}/gate50/work')
import g50_lib as G  # noqa: E402

out = {}
for name, fn in (('winner405', G.prof_winner405),
                 ('base_winner', G.prof_winner_base)):
    s, _aux = G.set_read(fn)
    out[name] = {'joint': G.joint_of(s),
                 'nec_min': s['nec']['min'],
                 'dec_min': s['dec']['min'],
                 'wec_min': s['wec']['min'],
                 'sec_min': s['sec']['min'],
                 'rho_min': s['rho']['min'],
                 'typeI_fraction': s['typeI_fraction'],
                 'nec_argmin_r': s['nec_argmin_r']}
    print(name, out[name]['joint'], flush=True)
json.dump(out, open(f'{WP}/gate50/results/g50_admission_laptop.json',
                    'w'), indent=1)
print('admission reads complete')
