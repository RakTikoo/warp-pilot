#!/usr/bin/env python3
"""Diagnostic 2: stage-by-stage comparison at the SEED
point, batch (162) vs single (1): profiles, T_sph, T_cart,
metric, That."""
import numpy as np

import g46_lib as L
import g46_profiles as P

SEED = (0.9323593026620368, 1.1444417317708335, 2.289013671875)
rr = 12.317073170731707
i_d = 158
pts = L.DIRS162 * rr
pt = pts[i_d]

pr_b = P.scaled_profiles(*SEED, np.full(len(pts), rr))
pr_1 = P.scaled_profiles(*SEED, np.array([np.linalg.norm(pt)]))
for k, (a, b) in enumerate(zip(pr_b, pr_1)):
    print(f'profile[{k}] batch {a[i_d]:.17e} single {b[0]:.17e} '
          f'diff {a[i_d] - b[0]:+.2e}')

Ts_b = L.T_sph(pts, pr_b)[i_d]
Ts_1 = L.T_sph(pt[None, :], pr_1)[0]
print('T_sph max diff:', float(np.max(np.abs(Ts_b - Ts_1))))

Tc_b = L.T_cart(pts, pr_b)[i_d]
Tc_1 = L.T_cart(pt[None, :], pr_1)[0]
print('T_cart max diff:', float(np.max(np.abs(Tc_b - Tc_1))))

g_b = L.metric_cart(pts, pr_b)[i_d]
g_1 = L.metric_cart(pt[None, :], pr_1)[0]
print('metric max diff:', float(np.max(np.abs(g_b - g_1))))

That_b = L.eulerian_that(g_b[None], Tc_b[None])[0]
That_1 = L.eulerian_that(g_1[None], Tc_1[None])[0]
print('That max diff:', float(np.max(np.abs(That_b - That_1))))
d = np.abs(That_b - That_1)
idx = np.unravel_index(np.argmax(d), d.shape)
print('worst That component:', idx, That_b[idx], That_1[idx])
