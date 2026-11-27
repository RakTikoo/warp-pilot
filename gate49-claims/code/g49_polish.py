#!/usr/bin/env python3
"""
g49_polish.py -- Gate-49 re-derivation of Phase 403's
adversary (Type-I) depth at the winner, on gate
machinery: Nelder-Mead minimisation of the Type-I
NEC margin over (r, theta, phi) inside the pose
band, started from the gate's own SET Type-I
points, the phase's stored polished point (stored
artefact data), and a probe grid on the DEC shell.
Plus an h-refinement of the worst-null at the
winner's NEC argmin point. Writes
gate49/results/g49_polish.json.
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g49_lib as G  # noqa: E402

WP = G.WP
OUT = os.path.join(WP, 'gate49', 'results', 'g49_polish.json')
POSE = G.POSE_W28
A, B = POSE
res = {}

z = np.load(os.path.join(WP, 'gate49', 'results',
                         'g49_winner_set.npz'))
pts_ti, nec_ti = z['pts'], z['nec']
res['gate_set_typeI_count'] = int(len(pts_ti))
res['gate_set_typeI_nec_min'] = float(np.min(nec_ti))


def objective(x):
    rr, th, ph = x
    if rr < A or rr > B or th < 0.02 or th > np.pi - 0.02:
        return 1.0
    pt = rr * np.array([np.sin(th) * np.cos(ph),
                        np.sin(th) * np.sin(ph), np.cos(th)])
    nec, is_ti, _, _ = G.nec_typeI_at(G.WINNER, POSE, pt, h=0.02)
    return nec if is_ti else nec + 1.0


def to_sph(p):
    r = float(np.linalg.norm(p))
    return np.array([r, np.arccos(np.clip(p[2] / r, -1, 1)),
                     np.arctan2(p[1], p[0])])


starts = []
order = np.argsort(nec_ti)[:5]
for i in order:
    starts.append(('gate_set', pts_ti[i], float(nec_ti[i])))
starts.append(('phase_stored_polished',
               np.array([9.76767620628728e-06,
                         18.976566052897187,
                         -17.329873019963184]), None))
# probe starts on the DEC shell (r ~ 25.7-25.93)
for th, ph in ((0.6, 0.4), (1.2, 2.2), (1.9, 4.0), (2.6, 5.5),
               (0.9, 3.6)):
    p = 25.8 * np.array([np.sin(th) * np.cos(ph),
                         np.sin(th) * np.sin(ph), np.cos(th)])
    starts.append(('shell_probe', p, None))

polished = []
for name, p0, set_nec in starts:
    x0 = to_sph(np.asarray(p0, dtype=float))
    r0 = minimize(objective, x0, method='Nelder-Mead',
                  options={'maxiter': 300, 'xatol': 1e-4,
                           'fatol': 1e-7})
    rr, th, ph = r0.x
    pt = rr * np.array([np.sin(th) * np.cos(ph),
                        np.sin(th) * np.sin(ph), np.cos(th)])
    nec, is_ti, _, _ = G.nec_typeI_at(G.WINNER, POSE, pt, h=0.02)
    polished.append({'start': name, 'start_set_nec': set_nec,
                     'polished_point': pt.tolist(),
                     'polished_r': float(rr),
                     'polished_nec': nec, 'typeI': bool(is_ti),
                     'objective': float(r0.fun)})
    print(name, '->', nec, flush=True)

cand = [p for p in polished if p['typeI']]
best = min(cand, key=lambda p: p['polished_nec'])
# one tighter pass from the best point
x0 = to_sph(np.array(best['polished_point']))
r1 = minimize(objective, x0, method='Nelder-Mead',
              options={'maxiter': 600, 'xatol': 1e-6,
                       'fatol': 1e-10})
rr, th, ph = r1.x
pt = rr * np.array([np.sin(th) * np.cos(ph),
                    np.sin(th) * np.sin(ph), np.cos(th)])
nec, is_ti, _, _ = G.nec_typeI_at(G.WINNER, POSE, pt, h=0.02)
tight = {'polished_point': pt.tolist(), 'polished_r': float(rr),
         'polished_nec': nec, 'typeI': bool(is_ti)}
if is_ti and nec < best['polished_nec']:
    best = dict(best, **tight)
res['polished_all'] = polished
res['tight_pass'] = tight
res['adversary_depth_gate'] = best['polished_nec']
res['adversary_point_gate'] = best['polished_point']
res['adversary_r_gate'] = best['polished_r']
res['stored_depth'] = -3.928911127808272e-07
res['depth_diff'] = res['adversary_depth_gate'] - res['stored_depth']

# h-refinement of the worst-null at the winner's NEC
# argmin point (the gate read's own argmin point)
num = json.load(open(os.path.join(WP, 'gate49', 'results',
                                  'g49_numbers.json')))
pt_arg = np.array(num['winner']['gate']['nec_argmin_point'])
href = []
for h in (0.04, 0.02, 0.01):
    That, err = G.that_at(G.WINNER, POSE, pt_arg, h=h)
    qf, qsc = G.worst_null_exact(That)
    href.append({'h': h, 'worst_null': qf,
                 'diff_vs_stored': qf - (-5.24207446894373e-06),
                 'fd_err': err})
res['winner_argmin_point'] = pt_arg.tolist()
res['winner_argmin_h_refinement'] = href

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print('DEPTH gate', res['adversary_depth_gate'],
      'stored', res['stored_depth'],
      'diff', res['depth_diff'])
print('href:', href)
