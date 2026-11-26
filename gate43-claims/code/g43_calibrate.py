#!/usr/bin/env python3
"""Gate-43 calibrations. All must pass before any audit
read is believed. Output: gate43/results/
g43_calibration.json (+ g43_calibration_fd.json)."""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate43/work')
import g43_lib as G  # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/gate43/results'
out = {}

# ---- C-0: stored vectors, two artefacts each
for name, a, b in (('A2', G.load_a2_vectors(),
                    G.load_a2_vectors_state()),
                   ('H2', G.load_h2_vectors(),
                    G.load_h2_vectors_state())):
    out[f'C0_{name}'] = {
        'max_diff': float(max(np.max(np.abs(x - y))
                              for x, y in zip(a, b)))}
print('C-0', out['C0_A2'], out['C0_H2'], flush=True)

# ---- C-1: trivial limit
pts = np.array([[12.0, 3.0, 4.0], [15.0, -5.0, 2.0],
                [11.0, 11.0, -6.0]])
P = len(pts)
z = np.zeros(P)
o = np.ones(P)
T, _ = G.einstein_from_profiles(pts, (z, z, z, o, z, z, o, z, z))
out['C1_trivial_max_abs_T'] = float(np.max(np.abs(T)))
print('C-1', out['C1_trivial_max_abs_T'], flush=True)

# ---- C-5: centre(1.0) reduces to A2 totals exactly
rr = np.linspace(9.0, 21.0, 241)
pa = G.a2_total_profiles(rr)
pc = G.centre_profiles(1.0, rr)
out['C5_centre_mu1_max_diff'] = float(max(
    np.max(np.abs(x - y)) for x, y in zip(pa, pc)))
print('C-5', out['C5_centre_mu1_max_diff'], flush=True)

# ---- C-4: A2 anchor SET read
t0 = time.time()
s_a2, _ = G.set_read_generic(G.a2_total_profiles)
out['C4_A2'] = {
    'nec_min': s_a2['nec']['min'],
    'nec_argmin_r': s_a2['nec_argmin_r'],
    'dec_min': s_a2['dec']['min'],
    'dec_argmin_r': s_a2['dec_argmin_r'],
    'wec_min': s_a2['wec']['min'],
    'sec_min': s_a2['sec']['min'],
    'rho_min': s_a2['rho']['min'],
    'typeI_count': s_a2['typeI_count'],
    'stored': {'nec_min': -2.319453132752996e-4,
               'dec_min': -2.233693204455982e-4,
               'rho_min': 8.638077678074035e-5,
               'typeI_count': 3535},
    'diffs': {'nec': s_a2['nec']['min'] - (-2.319453132752996e-4),
              'dec': s_a2['dec']['min'] - (-2.233693204455982e-4),
              'rho': s_a2['rho']['min'] - 8.638077678074035e-5},
    'seconds': time.time() - t0}
print('C-4', out['C4_A2'], flush=True)

# ---- C-3: density-split identity on the A2 SET points
mx = 0.0
for rr_ in G.R_NODES:
    pts = G.DIRS162 * rr_
    pr = G.a2_total_profiles(np.full(len(pts), rr_))
    T, g = G.einstein_from_profiles(pts, pr)
    That = G.eulerian_that(g, T)
    rho_c = G.rho_split_closed(pts, pr)
    mx = max(mx, float(np.max(np.abs(That[:, 0, 0] - rho_c))))
out['C3_rho_split_max_diff'] = mx
print('C-3', mx, flush=True)

# ---- C-9: clamp construction at (1,1,1) vs Gate-41 SS4
s_cl, _ = G.set_read(1.0, 1.0, 1.0, clamp=True)
out['C9_clamp_H2'] = {
    'nec_min': s_cl['nec']['min'],
    'dec_min': s_cl['dec']['min'],
    'rho_min': s_cl['rho']['min'],
    'joint': min(s_cl['nec']['min'], s_cl['dec']['min']),
    'stored_gate41': {'nec_min': -1.956241449779669e-4,
                      'dec_min': -2.087299309761317e-4,
                      'rho_min': 8.793529206482109e-5},
    'diffs': {'nec': s_cl['nec']['min'] - (-1.956241449779669e-4),
              'dec': s_cl['dec']['min'] - (-2.087299309761317e-4),
              'rho': s_cl['rho']['min'] - 8.793529206482109e-5}}
print('C-9', out['C9_clamp_H2'], flush=True)

with open(f'{RES}/g43_calibration.json', 'w') as f:
    json.dump(out, f, indent=1)

# ---- C-2: FD convergence at two mixed-centre points
MIX = (0.9323593026620368, 1.1444417317708335, 1.1445068359375)
fd = {}
test_pts = {
    'nec_argmin': np.array([[-1.9470056065537118,
                             -10.702464686683815,
                             6.28048780487805]]),
    'generic': (G.DIRS162[100] * 15.5)[None, :],
}
for name, pp in test_pts.items():
    pr = G.mixed_profiles(*MIX, np.linalg.norm(pp, axis=1))
    T_ad, _ = G.einstein_from_profiles(pp, pr)
    row = {'T_ad_max_abs': float(np.max(np.abs(T_ad)))}
    for h in (0.1, 0.05, 0.025, 0.0125):
        T_fd = G.einstein_fd(
            pp, lambda P: G.mixed_profiles(
                *MIX, np.linalg.norm(P, axis=1)), h=h)
        row[f'h={h}'] = float(np.max(np.abs(T_fd - T_ad)))
    fd[name] = row
    print('C-2', name, row, flush=True)
with open(f'{RES}/g43_calibration_fd.json', 'w') as f:
    json.dump(fd, f, indent=1)
print('CALIBRATION DONE', flush=True)
