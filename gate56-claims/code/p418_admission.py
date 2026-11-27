#!/usr/bin/env python3
"""
p418_admission.py -- CTL-418-ADM: the Trace-A
endpoint SET read on the executing machine (run
on the laptop pool mirror; the parent compares
the printed minima against the VM endpoint
record). Uses Phase 389's lib from the WP root
in P389_WP (the endpoint is an ordinary point of
the 389 scaling space, mu_S = 0). Identical in
form to Phases 400/405/406/412/414's admission
controls (registration SS2).
"""
import json
import os
import sys

WP = os.environ.get('P389_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/phase389/work')

import p389_lib as L  # noqa: E402

EP_A = (0.0, 2.386698313835416, 10.718911464156438)

s, _aux = L.set_read389(*EP_A)
out = {'wp': WP,
       'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
       'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
       'rho_min': s['rho']['min'],
       'nec_argmin_r': s['nec_argmin_r'],
       'dec_argmin_r': s['dec_argmin_r']}
print(json.dumps(out, indent=1))
