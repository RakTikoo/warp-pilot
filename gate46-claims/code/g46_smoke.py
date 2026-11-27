#!/usr/bin/env python3
"""Gate-46 smoke test: import/lambdify time, trivial limit
(C-1), stored-vector agreement (C-0), one-shell timing."""
import time

import numpy as np

t0 = time.time()
import g46_lib as L  # noqa: E402
import g46_profiles as P  # noqa: E402
print(f'import+lambdify: {time.time() - t0:.1f} s', flush=True)

# C-0: stored vectors, confirmation vs state artefacts
for name, a, b in [('A2', P.load_a2(), P.load_a2_state()),
                   ('H2', P.load_h2(), P.load_h2_state())]:
    d = max(float(np.max(np.abs(x - y))) for x, y in zip(a, b))
    print(f'C-0 {name}: max diff {d}', flush=True)

# C-1: trivial limit S=0, N=1, M=1 (all derivatives zero)
pts = L.DIRS162 * 15.0
z = np.zeros(len(pts))
o = np.ones(len(pts))
pr = (z, z, z, o, z, z, o, z, z)
T = L.T_cart(pts, pr)
print(f'C-1 trivial: max |T| = {np.max(np.abs(T)):.3e}', flush=True)

# one shell at the anchor (394 centre) vs stored shell values
t0 = time.time()
rr = 15.487804878048781
pts = L.DIRS162 * rr
pr = P.scaled_profiles(0.8015689430763502, 1.3179449338854314,
                       3.574968377899082,
                       np.full(len(pts), rr))
T = L.T_cart(pts, pr)
g = L.metric_cart(pts, pr)
That = L.eulerian_that(g, T)
m = L.margins(That)
print(f'shell eval: {time.time() - t0:.1f} s', flush=True)
print('anchor shell nec min:', float(np.min(m['nec'])),
      'stored full-set nec min: -6.812652656191736e-05 @ this shell',
      flush=True)
print('anchor shell rho min:', float(np.min(That[:, 0, 0])),
      'typeI count:', int(np.sum(m['typeI'])), flush=True)
