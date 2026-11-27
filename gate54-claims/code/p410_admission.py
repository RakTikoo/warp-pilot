#!/usr/bin/env python3
"""
p410_admission.py -- Phase 410 laptop admission control
(registration SS6): the Phase 405 winner's SET-244 read on
the executing machine (run on the laptop pool mirror; the
parent compares the printed values against the VM read).
The winner's K=9 knots are loaded from p410_winner_knots.json
(Gate-50's stored knots; asserted on the VM to equal Phase
405's state-derived vector at diff 0.0).
"""
import json
import os
import sys

WP = os.environ.get('P410_WP', '/home/hatch/workspace/warp-pilot')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{WP}/phase405/work')

import numpy as np  # noqa: E402
import p405_lib as L  # noqa: E402

vS = np.array(json.load(open(os.path.join(HERE,
                                          'p410_winner_knots.json'))),
              dtype=L.DTYPE)
s, _aux = L.set_read405(vS, 9)
out = {'wp': WP,
       'joint': L.joint_of_read(s),
       'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
       'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
       'rho_min': s['rho']['min'],
       'nec_argmin_r': s['nec_argmin_r'],
       'dec_argmin_r': s['dec_argmin_r'],
       'typeI_fraction': s['typeI_fraction']}
print(json.dumps(out, indent=1))
