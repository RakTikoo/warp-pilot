#!/usr/bin/env python3
"""
g34_item3c.py -- Gate-34 Item 3, stage C: Jacobian
singular values at the gate's N = 6 solution, and the
target-perturbation ladder eps in {1e-12, 1e-9, 1e-6,
1e-4} (relative to per-site |That|_F; symmetric noise
of unit Frobenius norm per site). Refit warm from the
gate winner + one fresh start per draw.
"""
import json
import numpy as np
import sys
from scipy.optimize import least_squares

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate34/work')
import g34_spinor as SP

M_MASS = 1.0
BAR = 1e-9
OUTP = '/home/hatch/workspace/warp-pilot/gate34/results/g34_item3c.json'
OUT = {}

t313 = json.load(open('/home/hatch/workspace/warp-pilot/'
                      'phase313/work/p313_targets.json'))
targets = [(np.array(s['point']), np.array(s['That']),
            float(s['frob'])) for s in t313['sites']]
a3 = json.load(open('/home/hatch/workspace/warp-pilot/gate34/'
                    'results/g34_item3a.json'))
theta6 = np.array(a3['N6_winner']['theta'])

# ------------------------------------------------ Jacobian SVD
f0 = SP.resid_vec(theta6, 6, M_MASS, targets)
J = np.zeros((40, len(theta6)))
for j in range(len(theta6)):
    h = 1e-6 * max(1.0, abs(theta6[j]))
    th = theta6.copy(); th[j] += h
    J[:, j] = (SP.resid_vec(th, 6, M_MASS, targets) - f0) / h
sv = np.linalg.svd(J, compute_uv=False)
OUT['jacobian'] = {
    'singular_values': sv.tolist(),
    'rank_at_1e-8': int(np.sum(sv > 1e-8)),
    'rank_at_1e-10': int(np.sum(sv > 1e-10)),
    'smallest_two': [float(sv[-1]), float(sv[-2])],
    'third_smallest': float(sv[-3]),
    'condition_on_largest_40': float(sv[0] / sv[39])}
json.dump(OUT, open(OUTP, 'w'), indent=1)
print('jacobian:', OUT['jacobian'], flush=True)

# ------------------------------------------------ fits
rng = np.random.default_rng(3403)


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
    return {'maxR': float(np.max(Rs)), 'Rs': Rs, 'rhos': rhos}


pert = {}
for eps in (1e-12, 1e-9, 1e-6, 1e-4):
    draws = []
    for draw in range(2):
        prng = np.random.default_rng(9100 + draw)
        tgts_p = []
        for pt, That, frob in targets:
            noise = prng.uniform(-1, 1, size=(4, 4))
            noise = 0.5 * (noise + noise.T)
            noise = noise / np.linalg.norm(noise) * frob
            tgts_p.append((pt, That + eps * noise, frob))
        r_warm = fit(theta6, 6, tgts_p)
        r_rand = fit(rand_theta(6), 6, tgts_p)
        best = r_warm if r_warm['maxR'] <= r_rand['maxR'] else r_rand
        draws.append({'maxR_warm': r_warm['maxR'],
                      'maxR_rand': r_rand['maxR'],
                      'best_maxR': best['maxR'],
                      'at_bar': bool(best['maxR'] <= BAR),
                      'rhos_at_match': best['rhos'],
                      'rho_targets_perturbed':
                      [float(t[1][0, 0]) for t in tgts_p]})
        print(f'eps={eps} draw{draw}: warm {r_warm["maxR"]:.2e} '
              f'rand {r_rand["maxR"]:.2e}', flush=True)
    pert[repr(eps)] = draws
    OUT['perturbation'] = pert
    json.dump(OUT, open(OUTP, 'w'), indent=1)
print('perturbation done', flush=True)
