#!/usr/bin/env python3
"""
p418_controls.py -- Phase 418 controls
(registration SS3). Run on the VM, the frame
of record, BEFORE any search read is believed.
Writes results/p418_controls.json. The laptop
admission (CTL-418-ADM) is p418_admission.py +
the comparison recorded here (the VM endpoint
read is taken in this script).
"""
import json
import os
import sys

import numpy as np

WP = os.environ.get('P418_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/phase418/work')

import p418_lib as L  # noqa: E402
import p405_lib as L405  # noqa: E402
import p400_lib as L400  # noqa: E402

OUT = {'phase': 418, 'frame': 'VM (frame of record)'}
CLS = 1e-17  # the registered diff-0.0 class (SS3)


def five(s):
    return {k: float(s[k]['min'])
            for k in ('nec', 'dec', 'wec', 'sec', 'rho')}


def diffs(got, want):
    return {k: got[k] - want[k] for k in want}


def in_class(d, cls=CLS):
    return all(abs(v) <= cls for v in d.values())


# ---- CTL-418-405WIN (diff 0.0 class)
s, aux = L405.set_read405(L.G50_KNOTS, 9)
got = five(s)
want = dict(L.G50_TG)
want.pop('joint')
d = diffs(got, want)
wn, _ = L405.worst_null_at405(L.G50_KNOTS, 9,
                              np.array(s['nec_argmin_point']))
OUT['CTL-418-405WIN'] = {
    'got': got, 'joint': L.joint_of_read(s),
    'nec_argmin_r': s['nec_argmin_r'],
    'diffs': d, 'in_class': in_class(d),
    'joint_diff': L.joint_of_read(s) - L.J1_400,
    'nec_argmin_r_exact': bool(
        s['nec_argmin_r'] == L.G50_NEC_R),
    'worst_null': wn,
    'worst_null_diff': wn - L.G50_WORST_NULL,
    'typeI_fraction': s['typeI_fraction']}
print('405WIN joint', L.joint_of_read(s), 'in_class',
      in_class(d), 'wn diff', wn - L.G50_WORST_NULL)

# ---- CTL-418-PSTAR (diff 0.0 class)
s, aux = L405.set_read405(L.PSTAR_KNOTS, 9)
got = five(s)
want2 = {'nec': L.J2_400, 'dec': L.J2_400, 'wec': L.J2_400,
         'sec': L.PSTAR_SEC, 'rho': 9.943338788183865e-05}
d = diffs(got, want2)
wn, _ = L405.worst_null_at405(L.PSTAR_KNOTS, 9,
                              np.array(s['nec_argmin_point']))
pk, pkr = L.peak_radius(L.PSTAR_KNOTS, 9)
OUT['CTL-418-PSTAR'] = {
    'got': got, 'joint': L.joint_of_read(s),
    'nec_argmin_r': s['nec_argmin_r'],
    'diffs': d, 'in_class': in_class(d),
    'joint_diff': L.joint_of_read(s) - L.J2_400,
    'nec_argmin_r_exact': bool(
        s['nec_argmin_r'] == L.PSTAR_NEC_R),
    'worst_null': wn,
    'worst_null_diff': wn - L.PSTAR_WORST_NULL,
    'peak': pk, 'peak_radius': pkr,
    'typeI_fraction': s['typeI_fraction']}
print('PSTAR joint', L.joint_of_read(s), 'in_class',
      in_class(d), 'wn diff', wn - L.PSTAR_WORST_NULL)

# ---- CTL-418-B1T1 (the non-carrier control, diff 0.0 class)
s, aux = L.set_read(L.BASEB1, L.B1T1_KNOTS, 17)
got = five(s)
want3 = {'nec': L.B1_T1_JOINT, 'dec': 1.8262980115431423e-09,
         'wec': 1.063262879474143e-07, 'sec': L.B1_T1_SEC,
         'rho': 9.628392607185307e-05}
d = diffs(got, want3)
wn, _ = L.worst_null_at(L.BASEB1, L.B1T1_KNOTS, 17,
                        np.array(s['nec_argmin_point']))
OUT['CTL-418-B1T1'] = {
    'got': got, 'joint': L.joint_of_read(s),
    'nec_argmin_r': s['nec_argmin_r'],
    'diffs': d, 'in_class': in_class(d),
    'joint_diff': L.joint_of_read(s) - L.B1_T1_JOINT,
    'nec_argmin_r_exact': bool(
        s['nec_argmin_r'] == L.B1_T1_NEC_R),
    'worst_null': wn,
    'worst_null_diff': wn - L.B1_T1_WORST_NULL,
    'typeI_fraction': s['typeI_fraction']}
print('B1T1 joint', L.joint_of_read(s), 'in_class',
      in_class(d), 'wn diff', wn - L.B1_T1_WORST_NULL)

# ---- CTL-418-B1STAT (diff 0.0)
s, aux = L.set_read(L.BASEB1, None, 9)
got = five(s)
OUT['CTL-418-B1STAT'] = {
    'got': got, 'joint': L.joint_of_read(s),
    'joint_diff': L.joint_of_read(s) - L.L1_B1,
    'sec_diff': got['sec'] - (-7.149443971550401e-04),
    'exact': bool(L.joint_of_read(s) - L.L1_B1 == 0.0)}
print('B1STAT joint', L.joint_of_read(s), 'diff',
      L.joint_of_read(s) - L.L1_B1)

# ---- CTL-418-400STAT (diff 0.0)
s, aux = L405.set_read405(None, 9)
got = five(s)
d = diffs(got, dict(L405.WIN_TG))
OUT['CTL-418-400STAT'] = {
    'got': got, 'joint': L.joint_of_read(s),
    'diffs': d,
    'exact': bool(all(v == 0.0 for v in d.values()))}
print('400STAT diffs', d)

# ---- CTL-418-PEN
pen_anchor = L400.penalty400(L400.ANCHOR_VN, L400.ANCHOR_VM)
OUT['CTL-418-PEN'] = {
    'LAM400': L.LAM400, 'LAM_REG': L.LAM_REG,
    'ratio_exact': bool(L.LAM400 == L.LAM_REG * 1e-3),
    'penalty400_anchor': pen_anchor,
    'penalty400_anchor_diff_vs_2.4e-8':
        pen_anchor - 2.4e-08}
print('PEN anchor', pen_anchor)

# ---- REP-418-K9 (registered datum)
s0, _ = L.set_read(L.BASE400_K9, None, 9)
s1, _ = L.set_read(L.BASE400_K9, L.G50_KNOTS, 9)
OUT['REP-418-K9'] = {
    'base': {'muN': L.BASE400_K9['muN'],
             'muM': L.BASE400_K9['muM'], 'K': 9,
             'vN': L.BASE400_K9['vN'].tolist(),
             'vM': L.BASE400_K9['vM'].tolist()},
    'static': five(s0), 'static_joint': L.joint_of_read(s0),
    'carried_G50': five(s1),
    'carried_G50_joint': L.joint_of_read(s1),
    'carried_G50_nec_argmin_r': s1['nec_argmin_r'],
    'note': 'The K9 shadow of 400\'s base: a '
            'representation, not the base. SS7\'s '
            'bars are the stored J1_400 / J2_400.'}
print('REP-K9 static', L.joint_of_read(s0),
      'carried', L.joint_of_read(s1))

# ---- CTL-418-ADM: the VM endpoint read (the laptop
# side is p418_admission.py on the pool mirror;
# the comparison is written by p418_adm_compare.py)
sys.path.insert(0, f'{WP}/phase389/work')
import p389_lib as L389  # noqa: E402
s, _aux = L389.set_read389(0.0, 2.386698313835416,
                           10.718911464156438)
OUT['CTL-418-ADM-VM-endpoint'] = {
    'nec_min': s['nec']['min'], 'dec_min': s['dec']['min'],
    'wec_min': s['wec']['min'], 'sec_min': s['sec']['min'],
    'rho_min': s['rho']['min'],
    'nec_argmin_r': s['nec_argmin_r'],
    'dec_argmin_r': s['dec_argmin_r']}
print('ADM VM endpoint nec', s['nec']['min'])

with open(f'{WP}/phase418/results/p418_controls.json',
          'w') as f:
    json.dump(OUT, f, indent=1)
print('WROTE results/p418_controls.json')
