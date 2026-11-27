#!/usr/bin/env python3
"""
p412_controls.py -- Phase 412 controls
(registration SS3): CTL-412-WIN and
CTL-412-CRIT on the VM. All diffs vs the
stored records must be 0.0 (WIN) / 0.0 class
(CRIT) before any rung is believed.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/phase412/work')
import p412_lib as L  # noqa: E402

out = {}

# ---- CTL-412-WIN: vS = 0 -> the 400 winner
s, aux = L.set_read(None, 9)
tg = L.WIN_TG
win = {
    'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
    'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
    'rho_min': s['rho']['min'],
    'joint': L.joint_of_read(s),
    'nec_argmin_r': s['nec_argmin_r'],
    'typeI_fraction': s['typeI_fraction'],
}
win['diffs'] = {
    'nec': win['nec_min'] - tg['nec'],
    'dec': win['dec_min'] - tg['dec'],
    'wec': win['wec_min'] - tg['wec'],
    'sec': win['sec_min'] - tg['sec'],
    'rho': win['rho_min'] - tg['rho'],
    'joint': win['joint'] - L.M0,
}
pt = np.array(s['nec_argmin_point'], dtype=L.DTYPE)
wn, _fib = L.worst_null_at(None, 9, pt)
win['worst_null_at_argmin'] = wn
win['worst_null_diff'] = wn - L.L.WIN_WORST_NULL
win['pass'] = all(abs(v) == 0.0 for v in win['diffs'].values()) \
    and win['worst_null_diff'] == 0.0
out['CTL-412-WIN'] = win
print('CTL-412-WIN pass:', win['pass'], 'diffs:', win['diffs'],
      'wn diff:', win['worst_null_diff'])

# ---- CTL-412-CRIT: the Gate-50 winner at the
# criterion through the screen path (scale to
# peak, SET read, phys row).
vS_s, _raw = L.scale_to_peak(L.G50_KNOTS, 9, L.CRIT)
s, aux = L.set_read(vS_s, 9)
phys = L.phys_row(vS_s, 9, s['nec_argmin_r'])
pk, pk_r = L.peak_radius(vS_s, 9)
crit = {
    'joint': L.joint_of_read(s),
    'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
    'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
    'rho_min': s['rho']['min'],
    'nec_argmin_r': s['nec_argmin_r'],
    'dec_argmin_r': s['dec_argmin_r'],
    'typeI_fraction': s['typeI_fraction'],
    'peak_physrow': phys['peak_abs_beta_S'],
    'peak_fine': pk, 'peak_radius': pk_r,
}
crit['diffs'] = {
    'joint': crit['joint'] - L.G50_JOINT,
    'sec': crit['sec_min'] - L.G50_SEC,
    'peak': crit['peak_physrow'] - L.G50_PEAK,
}
pt = np.array(s['nec_argmin_point'], dtype=L.DTYPE)
wn, _fib = L.worst_null_at(vS_s, 9, pt)
crit['worst_null_at_argmin'] = wn
crit['pass'] = (crit['diffs']['joint'] == 0.0
                and crit['nec_argmin_r'] == L.G50_NEC_R
                and crit['peak_radius'] == 10.0)
out['CTL-412-CRIT'] = crit
print('CTL-412-CRIT pass:', crit['pass'], 'diffs:', crit['diffs'],
      'nec_r:', crit['nec_argmin_r'], 'peak_r:', crit['peak_radius'],
      'wn:', wn)

with open(f'{WP}/phase412/results/p412_controls.json', 'w') as f:
    json.dump(out, f, indent=1)
print('written results/p412_controls.json')
