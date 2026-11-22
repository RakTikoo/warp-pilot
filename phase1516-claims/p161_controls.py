"""
p161_controls.py — P16-1 attribution controls (frozen/static twins).

1. Static 'gauss' twin of the travelling variant (Rm=15, wd=3.0, beta=0.02):
   is the travelling failure already in the static profile?
2. Frozen slices of travelling L=4 at t=3.33 (its worst instant) and
   L=2 at t=16.67: stationary audit of the exact slice geometry.
3. Frozen slices of breathing d=1.0/T=40 at t=30 and t=26.67 (failing
   instants): stationary audit of the compressed-wall geometry.
4. Static Finalist-A beta scan beta in {0.025, 0.03, 0.04}: where does
   the static family itself break (shift-variant attribution)?
All audits: p74 TD auditor on wrap_stationary, same points/masks as
p161_dynamic (imported), h=0.3 (h=0.15 for the gauss twin).
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase7')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase16')
import shell as sh  # noqa: E402
from p74_auditor import wrap_stationary  # noqa: E402
from p161_dynamic import (audit_instant, finalist_prof, dump, BASE, M_G,  # noqa: E402
                          BETA0)

out = {}

# 1. static gauss twin
prof_g = sh.build_shell(10.0, 20.0, M_G, kind='gauss',
                        params={'Rm': 15.0, 'wd': 3.0},
                        s_rho=BASE['s_rho'], s_P=BASE['s_P'], Nr=4001)
gf_g = sh.shell_point_factory(prof_g, BETA0, 'cos', 1.0, [10.0, 20.0])
out['static_gauss_twin_h03'] = audit_instant(wrap_stationary(gf_g), 0.0, 0.3,
                                             'static gauss twin')
out['static_gauss_twin_h015'] = audit_instant(wrap_stationary(gf_g), 0.0,
                                              0.15, 'static gauss twin h015')
print('gauss twin core worst', out['static_gauss_twin_h03']['core']['worst'],
      'typeI', out['static_gauss_twin_h03']['core']['typeI_frac'], flush=True)

# 2. frozen travelling slices
for Lam, t in ((4.0, 40.0 / 12), (2.0, 5 * 40.0 / 12)):
    Rm = 15.0 + Lam * np.sin(2 * np.pi * t / 40.0)
    prof = sh.build_shell(10.0, 20.0, M_G, kind='gauss',
                          params={'Rm': Rm, 'wd': 3.0},
                          s_rho=BASE['s_rho'], s_P=BASE['s_P'], Nr=4001)
    gf = sh.shell_point_factory(prof, BETA0, 'cos', 1.0, [10.0, 20.0])
    key = f'frozen_travelling_L{Lam:g}_t{t:.2f}_Rm{Rm:.2f}'
    out[key] = audit_instant(wrap_stationary(gf), 0.0, 0.3, key)
    print(key, 'core worst', out[key]['core']['worst'],
          'typeI', out[key]['core']['typeI_frac'], flush=True)

# 3. frozen breathing slices d=1.0
for t in (30.0, 26.666666666666668):
    s = np.sin(2 * np.pi * t / 40.0)
    R1, R2 = 10.0 - s, 20.0 + s
    prof = sh.build_shell(R1, R2, M_G, kind=BASE['kind'],
                          params=dict(BASE['params']), s_rho=BASE['s_rho'],
                          s_P=BASE['s_P'], Nr=4001)
    gf = sh.shell_point_factory(prof, BETA0, 'cos', 1.0, [R1, R2])
    key = f'frozen_breathing_d1_t{t:.2f}_R1{R1:.2f}_R2{R2:.2f}'
    out[key] = audit_instant(wrap_stationary(gf), 0.0, 0.3, key)
    print(key, 'core worst', out[key]['core']['worst'],
          'typeI', out[key]['core']['typeI_frac'], flush=True)

# 4. static beta scan
prof_f = finalist_prof()
for beta in (0.025, 0.03, 0.04):
    gf = sh.shell_point_factory(prof_f, beta, 'cos', 1.0, [10.0, 20.0])
    key = f'static_finalist_beta{beta}'
    out[key] = audit_instant(wrap_stationary(gf), 0.0, 0.3, key)
    print(key, 'core worst', out[key]['core']['worst'],
          'typeI', out[key]['core']['typeI_frac'], flush=True)

dump(out, 'p161_controls.json')
print('done')
