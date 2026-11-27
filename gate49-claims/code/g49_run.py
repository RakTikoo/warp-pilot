#!/usr/bin/env python3
"""
g49_run.py -- Gate-49 deciding reads (FD machinery):
controls, the Step-1 width curve, the winner and its
clamp, the worst-DEC screen re-read, and the SS7
peak computation. Writes gate49/results/g49_numbers.json.
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g49_lib as G  # noqa: E402

WP = G.WP
OUT = os.path.join(WP, 'gate49', 'results', 'g49_numbers.json')
H = 0.02
res = {'h_production': H}

STORED = {
    'C395_home': {'joint': -2.9809850277749006e-05,
                  'worst_null': -3.0896210095678075e-05,
                  'dec': -1.7766846142506707e-06,
                  'rho': 9.780857711542179e-05, 'typeI_count': 4067},
    'H2_home': {'joint': -1.9422459891767227e-04},
    'W12': {'joint': -2.4728052267161693e-05,
            'worst_null': -2.6607692199924456e-05,
            'dec': -1.314264076501302e-06,
            'rho': 8.886991784762733e-05, 'typeI_count': 4093},
    'W14': {'joint': -2.050976956715771e-05,
            'worst_null': -2.268064550905132e-05,
            'dec': -1.0499634521441515e-06,
            'rho': 8.110300208687759e-05, 'typeI_count': 4097},
}
WIDTH_ROWS = {   # Phase 403 Step-1 stored rows (p403_step1.json)
    16.0: {'joint': -1.7926474820231396e-05,
           'worst_null': -1.970634738825685e-05,
           'dec': -8.669374244657041e-07,
           'rho': 7.431159688949356e-05,
           'nec_argmin_r': 15.78048780487805, 'typeI_count': 4098},
    18.0: {'joint': -1.571426828975267e-05,
           'worst_null': -1.7024653459910547e-05,
           'dec': -7.329e-07, 'rho': 6.833890260716853e-05,
           'nec_argmin_r': 15.878048780487806, 'typeI_count': None},
    20.0: {'joint': -1.3937719627557114e-05,
           'worst_null': -1.5226979395890161e-05,
           'dec': -6.306e-07, 'rho': 6.305840962862893e-05,
           'nec_argmin_r': 15.97560975609756, 'typeI_count': None},
    24.0: {'joint': -1.1284519658283278e-05,
           'worst_null': -1.253403664123716e-05,
           'dec': -4.854e-07, 'rho': 5.418056712213705e-05,
           'nec_argmin_r': 16.170731707317074, 'typeI_count': None},
    28.0: {'joint': -9.38489875115556e-06,
           'worst_null': -1.0545031681497364e-05,
           'dec': -3.878661406092417e-07,
           'rho': 4.705368093035287e-05,
           'nec_argmin_r': 16.365853658536587, 'typeI_count': 4109},
}
WIN_STORED = {'joint': -3.676111526923747e-06,
              'worst_null': -5.24207446894373e-06,
              'dec': -3.809243287998136e-07,
              'rho': 4.705527192329396e-05,
              'typeI_count': 4603,
              'nec_argmin_r': 17.04878048780488,
              'clamped_joint': -3.8110196987227636e-06}


def pose_of_width(W):
    return (15.0 - W / 2.0, 15.0 + W / 2.0)


def read_block(triple, pose, clamp=False):
    out, aux = G.set_read(triple, pose, h=H, clamp=clamp)
    That = aux['That'][int(np.argmin(aux['R']['nec']))]
    qf, qsc = G.worst_null_exact(That)
    blk = {'joint': out['joint'],
           'nec_min': out['nec']['min'], 'dec_min': out['dec']['min'],
           'wec_min': out['wec']['min'], 'sec_min': out['sec']['min'],
           'rho_min': out['rho']['min'],
           'typeI_count': out['typeI_count'],
           'typeI_fraction': out['typeI_fraction'],
           'nec_argmin_r': out['nec_argmin_r'],
           'nec_argmin_point': out['nec_argmin_point'],
           'nec_argmin_typeI': out['nec_argmin_typeI'],
           'dec_argmin_r': out['dec_argmin_r'],
           'dec_argmin_typeI': out['dec_argmin_typeI'],
           'worst_null_at_argmin': qf, 'worst_null_scan': qsc,
           'fd_err_indicator': out['fd_err_indicator']}
    return blk, out, aux


def diffs(blk, stored):
    d = {}
    for k in ('joint', 'worst_null', 'dec', 'rho'):
        sk = {'worst_null': 'worst_null_at_argmin',
              'dec': 'dec_min', 'rho': 'rho_min'}[k] \
            if k != 'joint' else 'joint'
        if stored.get(k) is not None:
            d[k] = blk[sk] - stored[k]
    if stored.get('typeI_count') is not None:
        d['typeI_count'] = blk['typeI_count'] - stored['typeI_count']
    return d


# ---------------- controls
ctrl = {}
blk, _, _ = read_block(G.C395, G.HOME)
ctrl['C395_home'] = {'gate': blk, 'stored': STORED['C395_home'],
                     'diffs': diffs(blk, STORED['C395_home'])}
blk, _, _ = read_block((1.0, 1.0, 1.0), G.HOME)
ctrl['H2_home'] = {'gate_joint': blk['joint'],
                   'stored_joint': STORED['H2_home']['joint'],
                   'diff': blk['joint'] - STORED['H2_home']['joint'],
                   'typeI_count': blk['typeI_count']}
for nm, pose in (('W12', (9.0, 21.0)), ('W14', (8.0, 22.0))):
    blk, _, _ = read_block(G.C395, pose)
    ctrl[nm] = {'gate': blk, 'stored': STORED[nm],
                'diffs': diffs(blk, STORED[nm])}
res['controls'] = ctrl
print('controls done', flush=True)

# ---------------- claim (a): width curve W16..W28
curve = {}
for W, stored in WIDTH_ROWS.items():
    blk, _, _ = read_block(G.C395, pose_of_width(W))
    curve[str(W)] = {'gate': blk, 'stored': stored,
                     'diffs': diffs(blk, stored)}
    print(f'width {W} done', flush=True)
res['width_curve'] = curve

# ---------------- claim (b): the winner at [1, 29]
blk, out_w, aux_w = read_block(G.WINNER, G.POSE_W28)
win = {'gate': blk, 'stored': WIN_STORED,
       'diffs': diffs(blk, {'joint': WIN_STORED['joint'],
                            'worst_null': WIN_STORED['worst_null'],
                            'dec': WIN_STORED['dec'],
                            'rho': WIN_STORED['rho'],
                            'typeI_count': WIN_STORED['typeI_count']})}
# clamped winner
blkc, _, _ = read_block(G.WINNER, G.POSE_W28, clamp=True)
win['clamped'] = {'gate_joint': blkc['joint'],
                  'gate_worst_null': blkc['worst_null_at_argmin'],
                  'stored_joint': WIN_STORED['clamped_joint'],
                  'diff': blkc['joint'] - WIN_STORED['clamped_joint'],
                  'typeI_count': blkc['typeI_count']}
res['winner'] = win
print('winner done', flush=True)

# save the winner read's Type-I points for the polish
ti = aux_w['R']['typeI']
np.savez(os.path.join(WP, 'gate49', 'results', 'g49_winner_set.npz'),
         pts=aux_w['pts'][ti], nec=aux_w['R']['nec'][ti],
         all_pts=aux_w['pts'], all_nec=aux_w['R']['nec'],
         all_typeI=aux_w['R']['typeI'])

# ---------------- claim (e): the SS7 peaks, from profile values
def peak_abs_S_home():
    fr = np.linspace(10.0, 20.0, 20001)
    pts = np.stack([fr, np.zeros_like(fr), np.zeros_like(fr)],
                   axis=1)
    S, _, _ = G.home_values((1.0, 1.0, 1.0), pts)
    i = int(np.argmax(np.abs(S)))
    # golden refinement on |S| around the grid max
    a, b = fr[max(i - 1, 0)], fr[min(i + 1, len(fr) - 1)]
    gr = (np.sqrt(5.0) - 1.0) / 2.0
    def f(r):
        Sv, _, _ = G.home_values((1.0, 1.0, 1.0),
                                 np.array([[r, 0.0, 0.0]]))
        return abs(float(Sv[0]))
    x1, x2 = b - gr * (b - a), a + gr * (b - a)
    f1, f2 = f(x1), f(x2)
    for _ in range(200):
        if f1 < f2:
            a, x1, f1, x2, f2 = x1, x2, f2, b - gr * (b - a), f(b - gr * (b - a))
        else:
            b, x2, f2, x1, f1 = x2, x1, f1, a + gr * (b - a), f(a + gr * (b - a))
    r_star = 0.5 * (a + b)
    return f(r_star), r_star

peakS, r_peak = peak_abs_S_home()
H2_peak = G.BETA * peakS
ss7 = {'H2_peak_gate': H2_peak, 'H2_peak_stored': G.H2_PEAK_STORED,
       'H2_peak_diff': H2_peak - G.H2_PEAK_STORED,
       'peak_radius_home': r_peak,
       'bar': G.DEGEN_BAR, 'bar_is_half_H2_stored': 0.5 * G.H2_PEAK_STORED}
for nm, triple, pose in (('winner', G.WINNER, G.POSE_W28),
                         ('C395_at_W28', G.C395, G.POSE_W28),
                         ('C395_home', G.C395, G.HOME)):
    a, b = pose
    fr = np.linspace(a, b, 20001)
    pts = np.stack([fr, np.zeros_like(fr), np.zeros_like(fr)],
                   axis=1)
    S, _, _ = G.pose_values(triple, pts, pose)
    pk = float(np.max(np.abs(G.BETA * S)))
    ss7[nm] = {'peak_abs_beta_S_gate': pk,
               'ratio_to_H2_stored': pk / G.H2_PEAK_STORED,
               'clearance_vs_bar': pk - G.DEGEN_BAR}
ss7['winner_peak_stored'] = 0.44268227409480604
ss7['winner_peak_diff'] = ss7['winner']['peak_abs_beta_S_gate'] \
    - ss7['winner_peak_stored']
ss7['winner_ratio_identity'] = \
    ss7['winner']['peak_abs_beta_S_gate'] / H2_peak
ss7['muS_winner'] = G.WINNER[0]
res['ss7'] = ss7
print('ss7 done', flush=True)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print('WROTE', OUT)
