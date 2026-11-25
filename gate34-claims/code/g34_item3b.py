#!/usr/bin/env python3
"""
g34_item3b.py -- Gate-34 Item 3, stage B: mode-count
sweep N in {4,5,6,7,8} with the gate optimiser (own
starts, seed 3402; tolerances loosened vs stage A to
the protocol's class). Persists incrementally.
Stage A's N=6 winner seeds the N>6 warm starts.
"""
import json
import numpy as np
import sys
from scipy.optimize import least_squares

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate34/work')
import g34_spinor as SP

M_MASS = 1.0
BAR = 1e-9
OUTP = '/home/hatch/workspace/warp-pilot/gate34/results/g34_item3b.json'
OUT = {}

t313 = json.load(open('/home/hatch/workspace/warp-pilot/'
                      'phase313/work/p313_targets.json'))
targets = [(np.array(s['point']), np.array(s['That']),
            float(s['frob'])) for s in t313['sites']]
a3 = json.load(open('/home/hatch/workspace/warp-pilot/gate34/'
                    'results/g34_item3a.json'))
theta6 = np.array(a3['N6_winner']['theta'])
pv6, chi6 = SP.unpack(theta6, 6)

rng = np.random.default_rng(3402)


def rand_theta(N, a_scale=0.03):
    pvecs = []
    for _ in range(N):
        d = rng.normal(size=3); d /= np.linalg.norm(d)
        pvecs.append(rng.uniform(0.05, 6.0) * d)
    chis = (rng.normal(size=(N, 2))
            + 1j * rng.normal(size=(N, 2))) * a_scale
    return SP.pack(np.array(pvecs), chis)


def fit(theta0, N, tgts, max_nfev=2000):
    sol = least_squares(SP.resid_vec, theta0, args=(N, M_MASS, tgts),
                        method='trf', max_nfev=max_nfev,
                        xtol=1e-10, ftol=1e-10, gtol=1e-10)
    pvecs, chis = SP.unpack(sol.x, N)
    Rs, rhos = SP.direct_residuals(pvecs, chis, M_MASS, tgts)
    return {'theta': sol.x, 'maxR': float(np.max(Rs)), 'Rs': Rs,
            'rhos': rhos, 'nfev': int(sol.nfev)}


def run_arm(N, n_starts, warm=None):
    starts = []
    if warm is not None:
        starts.append(('warm', warm))
    for i in range(n_starts):
        starts.append((f'rand{i}', rand_theta(N)))
    results = []
    best = None
    for name, th0 in starts:
        r = fit(th0, N, targets)
        results.append({'start': name, 'maxR': r['maxR'],
                        'nfev': r['nfev']})
        print(f'N={N} {name}: maxR {r["maxR"]:.3e}', flush=True)
        if best is None or r['maxR'] < best['maxR']:
            best = r
    return results, best


sweep = {}
for N in (4, 5, 6, 7, 8):
    warm = None
    if N > 6:
        extra_p, extra_c = [], []
        for _ in range(N - 6):
            d = rng.normal(size=3); d /= np.linalg.norm(d)
            extra_p.append(rng.uniform(0.05, 6.0) * d)
            extra_c.append((rng.normal(size=2)
                            + 1j * rng.normal(size=2)) * 0.01)
        warm = SP.pack(np.vstack([pv6, np.array(extra_p)]),
                       np.vstack([chi6, np.array(extra_c)]))
    n_rand = 8 if N == 6 else 6
    resN, bestN = run_arm(N, n_rand, warm=warm)
    sweep[str(N)] = {
        'starts': resN, 'best_maxR': bestN['maxR'],
        'best_Rs': bestN['Rs'], 'best_rhos': bestN['rhos'],
        'n_starts_at_bar': int(sum(1 for r in resN
                                   if r['maxR'] <= BAR))}
    OUT['sweep'] = sweep
    json.dump(OUT, open(OUTP, 'w'), indent=1)
print('sweep done', flush=True)
