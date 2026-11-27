#!/usr/bin/env python3
"""
g48_polish.py -- Gate-48's independent re-derivation of
Phase 400's adversary-polished in-region depth at the
winner. Protocol mirrored from the claim (Nelder-Mead
over (r, theta, phi), starts = the five lowest Type-I
SET points of the gate's own SET read, objective = NEC
margin, +1 penalty off Type-I), machinery entirely
g48_lib. Plus a fine radial bracket (the configuration
is static, hence spherically symmetric: the margin is
a function of r alone -- verified at two directions).
Writes gate48/results/g48_polish.json.
"""
import json
import sys

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate48/work')
import g48_lib as L  # noqa: E402

OUT = '/home/hatch/workspace/warp-pilot/gate48/results/g48_polish.json'
conf = json.load(open(f'{L.WP}/phase400/results/'
                      'p400_confirmation.json'))
cand = conf['candidate']
MU = (0.0, cand['muN'], cand['muM'])
VN, VM, K = np.array(cand['vN']), np.array(cand['vM']), 17
STORED_DEPTH = 1.3761826591108812e-06


def nec_pt(pt):
    pr = L.point_read(*MU, VN, VM, K, pt)
    return pr['nec'], pr['typeI']


def objective(x):
    rr, th, ph = x
    if rr < 10.0 or rr > 20.0:
        return 1.0
    if th < 0.05 or th > np.pi - 0.05:
        return 1.0   # coordinate pole guard (spherical chart)
    pt = rr * np.array([np.sin(th) * np.cos(ph),
                        np.sin(th) * np.sin(ph), np.cos(th)])
    nec, is_ti = nec_pt(pt)
    return nec if is_ti else nec + 1.0


out, aux = L.set_read(*MU, VN, VM, K)
R, P = aux['R'], aux['pts']
ti_nec = np.where(R['typeI'], R['nec'], np.inf)
order = np.argsort(ti_nec)[:5]
starts = [{'set_point': P[i].tolist(),
           'set_r': float(np.linalg.norm(P[i])),
           'set_nec': float(R['nec'][i])} for i in order]

polished = []
for i in order:
    p0 = P[i]
    r0 = float(np.linalg.norm(p0))
    x0 = np.array([r0, np.arccos(np.clip(p0[2] / r0, -1, 1)),
                   np.arctan2(p0[1], p0[0])])
    res = minimize(objective, x0, method='Nelder-Mead',
                   options={'maxiter': 300, 'xatol': 1e-4,
                            'fatol': 1e-7})
    rr, th, ph = res.x
    pt = rr * np.array([np.sin(th) * np.cos(ph),
                        np.sin(th) * np.sin(ph), np.cos(th)])
    nec, is_ti = nec_pt(pt)
    polished.append({'start_set_nec': float(R['nec'][i]),
                     'polished_point': pt.tolist(),
                     'polished_r': float(rr),
                     'polished_nec': nec, 'polished_typeI': is_ti,
                     'objective': float(res.fun)})
best = min((p for p in polished if p['polished_typeI']),
           key=lambda p: p['polished_nec'])

# tighter second polish from the protocol polish's end
x0 = np.array([best['polished_r'],
               np.arccos(np.clip(
                   best['polished_point'][2] / best['polished_r'],
                   -1, 1)),
               np.arctan2(best['polished_point'][1],
                          best['polished_point'][0])])
res2 = minimize(objective, x0, method='Nelder-Mead',
                options={'maxiter': 2000, 'xatol': 1e-9,
                         'fatol': 1e-13})
rr2, th2, ph2 = res2.x
pt2 = rr2 * np.array([np.sin(th2) * np.cos(ph2),
                      np.sin(th2) * np.sin(ph2), np.cos(th2)])
nec2, ti2 = nec_pt(pt2)

# radial bracket: margin vs r at two directions
bracket = []
for rr in np.arange(17.30, 18.1001, 0.025):
    row = {'r': float(rr)}
    for name, d in (('x', (1.0, 0.0, 0.0)), ('diag', tuple(np.ones(3) / np.sqrt(3.0)))):
        nec, is_ti = nec_pt(rr * np.array(d))
        row[f'nec_{name}'] = nec
        row[f'typeI_{name}'] = is_ti
    bracket.append(row)
bmin = min(bracket, key=lambda row: row['nec_x'])
max_dir_diff = max(abs(row['nec_x'] - row['nec_diag']) for row in bracket)

res = {'stored_depth': STORED_DEPTH,
       'protocol_polish': {'depth': best['polished_nec'],
                           'point': best['polished_point'],
                           'r': best['polished_r'],
                           'diff_vs_stored': float(
                               best['polished_nec'] - STORED_DEPTH),
                           'starts': starts, 'polished': polished},
       'tight_polish': {'depth': nec2, 'r': float(rr2),
                        'typeI': ti2,
                        'diff_vs_stored': float(nec2
                                                - STORED_DEPTH)},
       'radial_bracket_min': bmin,
       'radial_bracket_max_dir_diff': max_dir_diff,
       'radial_bracket': bracket}
with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print('protocol depth', best['polished_nec'], 'diff',
      best['polished_nec'] - STORED_DEPTH)
print('tight depth', nec2, 'at r', rr2)
print('bracket min', bmin)
print('WROTE', OUT)
