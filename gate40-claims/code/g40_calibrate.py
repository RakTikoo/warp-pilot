#!/usr/bin/env python3
"""Gate-40 calibration: run BEFORE any deciding read is quoted.
C-1 vectors; C-2 waveform; C-3 stationary anchor; C-4 flat limit;
C-5 mu==1 reduction; C-6 FD independent path; C-7 Phase 364 champions
at their Gate-39 worst instants."""
import json
import sys
import numpy as np
sys.path.insert(0, '.')
import g40_lib as G
from g40_members import ANCHOR, FAMILY364, CHAMPS364

WP = '../../'
res = {}

conf = json.load(open(WP + 'phase344/results/p344_confirmation.json'))
a2 = [c for c in conf['confirmations'] if c['point'] == 'A2'][0]
state = json.load(open(WP + 'phase344/results/p344_state_A2.json'))
fi = state['final_incumbent']

# C-1 vectors
res['C1_vectors_maxdiff'] = float(max(
    np.max(np.abs(np.array(a2[k]) - np.array(fi[k]))) for k in ('vS', 'vN', 'vM')))
cen = G.Centre(a2['vS'], a2['vN'], a2['vM'])

# C-2 waveform vs centred FD (h = 5e-5), registered shapes of 374
ph = np.linspace(-np.pi, np.pi, 4097)
h = 5.0e-5
c2 = {}
for (D, m) in ((0.75, 0.75), (0.75, 0.875)):
    mu, mup, mupp = G.dwelling_mu(ph, 0.30, D, m)
    mu_p, _, _ = G.dwelling_mu(ph + h, 0.30, D, m)
    mu_m, _, _ = G.dwelling_mu(ph - h, 0.30, D, m)
    mu_pp, _, _ = G.dwelling_mu(ph + 2 * h, 0.30, D, m)
    mu_mm, _, _ = G.dwelling_mu(ph - 2 * h, 0.30, D, m)
    fd1 = (mu_mm - 8 * mu_m + 8 * mu_p - mu_pp) / (12 * h)
    fd2 = (-mu_pp + 16 * mu_p - 30 * mu + 16 * mu_m - mu_mm) / (12 * h ** 2)
    c2[f'D{D}_m{m}'] = {
        'mu_phi_err': float(np.max(np.abs(fd1 - mup))),
        'mu_phiphi_err': float(np.max(np.abs(fd2 - mupp))),
        'periodicity': float(np.max(np.abs(
            G.dwelling_mu(ph + 2 * np.pi, 0.30, D, m)[0] - mu))),
        'mu_min': float(np.min(mu)), 'mu_max': float(np.max(mu)),
        'range_expected': [1 + 0.30 * (2 * m - 1), 1.30]}
res['C2_waveform'] = c2

# C-3 stationary anchor
out = G.set_read(cen)
stored = a2['set']
res['C3_anchor'] = {k: {'gate': out[k]['min'],
                        'diff': out[k]['min'] - stored[k]['min']}
                    for k in ('nec', 'wec', 'dec', 'sec', 'rho')}
res['C3_anchor']['typeI_fraction_diff'] = out['typeI_fraction'] - stored['typeI_fraction']
res['C3_anchor']['nec_argmin_r'] = out['nec_argmin_r']
res['C3_anchor']['dec_argmin_r'] = out['dec_argmin_r']

# C-4 flat limit at phi=2.6 inside the falling transition (374 CTL-T3 member)
mem = {'name': 'flat', 'subset': {'S', 'N', 'M'}, 'a': 0.30,
       'T': 320, 'Om': 2 * np.pi / 320, 'D': 0.75, 'm': 0.75}
pts = G.SET_PTS[::37]
T, g = G.T_at(cen, pts, mem, 2.6, flat=True)
res['C4_flat_maxabsT'] = float(np.max(np.abs(T)))
mu, mud, mudd = G.member_mu(mem, 2.6)
res['C4_at_phi'] = {'mu': mu, 'mu_dot': mud, 'mu_ddot': mudd}

# C-5 reduction: anchor member through time-dependent tensor, 32 instants
worst = 0.0
for j in range(32):
    o = G.set_read(cen, ANCHOR, 2 * np.pi * j / 32)
    for k in ('nec', 'wec', 'dec', 'sec', 'rho'):
        worst = max(worst, abs(o[k]['min'] - stored[k]['min']))
res['C5_reduction_maxdiff'] = float(worst)

# C-6 FD independent path: member SNM a0.30 T320 D0.75 m0.75, phis {2.6,3.5},
# radii {12.3,16.2,19.4} on the A2 NEC-argmin direction
mem2 = {'name': 'fd', 'subset': {'S', 'N', 'M'}, 'a': 0.30,
        'T': 320, 'Om': 2 * np.pi / 320, 'D': 0.75, 'm': 0.75}
d = np.array(stored['nec_argmin_point']); d = d / np.linalg.norm(d)
rows = []
for phi in (2.6, 3.5):
    for rr in (12.3, 16.2, 19.4):
        pt = rr * d
        Ta, _ = G.T_at(cen, pt[None, :], mem2, phi)
        p4 = np.array([[phi / mem2['Om'], pt[0], pt[1], pt[2]]])
        Tf, _ = G.einstein_fd(cen, mem2, p4, 0.0125)
        Tf2, _ = G.einstein_fd(cen, mem2, p4, 0.00625)
        A = Ta[0]; F1 = Tf[0]; F2 = Tf2[0]
        big = np.abs(A) >= 1e-6
        rel = float(np.max(np.abs(F1[big] - A[big]) / np.abs(A[big]))) if np.any(big) else 0.0
        small = float(np.max(np.abs(F1[~big] - A[~big]))) if np.any(~big) else 0.0
        spread = float(np.max(np.abs(F1[big] - F2[big]) / np.abs(A[big]))) if np.any(big) else 0.0
        rows.append({'phi': phi, 'r': rr, 'rel': rel, 'small_abs': small,
                     'self_spread': spread})
res['C6_fd'] = {'max_rel': max(r['rel'] for r in rows),
                'max_small_abs': max(r['small_abs'] for r in rows),
                'max_self_spread': max(r['self_spread'] for r in rows),
                'rows': rows}

# C-7 Phase 364 champions at their Gate-39 worst instants
c7 = {}
for mem364 in FAMILY364:
    nm = mem364['name']
    nec_s, phi_n, dec_s, phi_d = CHAMPS364[nm]
    on = G.set_read(cen, mem364, phi_n)
    od = G.set_read(cen, mem364, phi_d)
    c7[nm] = {'nec_at_phi_nec': on['nec']['min'],
              'nec_diff': on['nec']['min'] - nec_s,
              'dec_at_phi_dec': od['dec']['min'],
              'dec_diff': od['dec']['min'] - dec_s,
              'rho_min_at_phi_dec': od['rho']['min']}
res['C7_champs364'] = c7

json.dump(res, open('../results/g40_calibration.json', 'w'), indent=1)
print(json.dumps({k: (v if not isinstance(v, dict) else '...') for k, v in res.items()}, indent=1))
print('C1', res['C1_vectors_maxdiff'])
print('C3 diffs', {k: res['C3_anchor'][k]['diff'] for k in ('nec', 'wec', 'dec', 'sec', 'rho')})
print('C4', res['C4_flat_maxabsT'], res['C4_at_phi'])
print('C5', res['C5_reduction_maxdiff'])
print('C6', res['C6_fd']['max_rel'], res['C6_fd']['max_small_abs'], res['C6_fd']['max_self_spread'])
for nm, v in c7.items():
    print('C7', nm, 'nec_diff %.3e dec_diff %.3e' % (v['nec_diff'], v['dec_diff']))
