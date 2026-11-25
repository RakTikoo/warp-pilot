#!/usr/bin/env python3
"""
g34_item3.py -- Gate-34 Item 3: the spinor match,
independently.

C4 control (gate builder on Phase 313's stored winner),
then the gate optimiser (own starts, seed 3401) on the
stored targets: N = 6 reproduction, mode-count sweep
N in {4,5,6,7,8}, Jacobian singular values at the gate
solution, and the target-perturbation ladder.
"""
import json
import numpy as np
import sys
from scipy.optimize import least_squares

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate34/work')
import g34_spinor as SP

M_MASS = 1.0
BAR = 1e-9
OUT = {}

t313 = json.load(open('/home/hatch/workspace/warp-pilot/'
                      'phase313/work/p313_targets.json'))
targets = [(np.array(s['point']), np.array(s['That']),
            float(s['frob'])) for s in t313['sites']]
rho_tgt = [float(np.array(s['That'])[0, 0]) for s in t313['sites']]

# ------------------------------------------------ C4 control
bf = json.load(open('/home/hatch/workspace/warp-pilot/'
                    'phase313/work/p313_joint_bestfit.json'))
pv_bf, chi_bf = [], []
U_check = []
for md in bf['modes']:
    pv = np.array(md['pvec'])
    a = np.array(md['a'])          # [[re,im],[re,im]]
    chi = a[:, 0] + 1j * a[:, 1]
    pv_bf.append(pv); chi_bf.append(chi)
    U, _ = SP.u_spinor(pv, M_MASS, chi)
    U_check.append(np.max(np.abs(
        U - (np.array(md['U'])[:, 0] + 1j * np.array(md['U'])[:, 1]))))
pv_bf = np.array(pv_bf); chi_bf = np.array(chi_bf)
Rs_c4, rhos_c4 = SP.direct_residuals(pv_bf, chi_bf, M_MASS, targets)
dres = max(float(np.max(np.abs(SP.dirac_residual(
    SP.u_spinor(pv_bf[j], M_MASS, chi_bf[j])[0], pv_bf[j], M_MASS))))
    for j in range(len(pv_bf)))
OUT['C4'] = {
    'U_reproduction_max_diff': float(np.max(U_check)),
    'Rs_gate_builder': Rs_c4,
    'Rs_stored': bf['Rs_direct'],
    'Rs_abs_diff': [abs(a - b) for a, b in
                    zip(Rs_c4, bf['Rs_direct'])],
    'rhos_gate_builder': rhos_c4,
    'rhos_stored': bf['rhos_direct'],
    'rhos_abs_diff': [abs(a - b) for a, b in
                      zip(rhos_c4, bf['rhos_direct'])],
    'dirac_residual_max': dres,
    'bar': 1e-11,
    'pass': bool(max(abs(a - b) for a, b in
                     zip(Rs_c4, bf['Rs_direct'])) <= 1e-11
                 and max(abs(a - b) for a, b in
                         zip(rhos_c4, bf['rhos_direct'])) <= 1e-11
                 and dres <= 1e-9)}

# ------------------------------------------------ fit machinery
rng = np.random.default_rng(3401)


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
                        xtol=1e-13, ftol=1e-13, gtol=1e-13)
    pvecs, chis = SP.unpack(sol.x, N)
    Rs, rhos = SP.direct_residuals(pvecs, chis, M_MASS, tgts)
    return {'theta': sol.x, 'maxR': float(np.max(Rs)), 'Rs': Rs,
            'rhos': rhos, 'nfev': int(sol.nfev)}


def run_arm(N, n_starts, tgts, warm=None):
    starts = []
    if warm is not None:
        starts.append(('warm', warm))
    for i in range(n_starts):
        starts.append((f'rand{i}', rand_theta(N)))
    results = []
    best = None
    for name, th0 in starts:
        r = fit(th0, N, tgts)
        results.append({'start': name, 'maxR': r['maxR'],
                        'nfev': r['nfev']})
        if best is None or r['maxR'] < best['maxR']:
            best = r
    return results, best


# ------------------------------------------------ N = 6 reproduction
res6, best6 = run_arm(6, 6, targets)
OUT['N6_reproduction'] = {
    'starts': res6, 'best_maxR': best6['maxR'],
    'best_Rs': best6['Rs'], 'best_rhos': best6['rhos'],
    'rho_targets': rho_tgt,
    'n_starts_at_bar': int(sum(1 for r in res6
                               if r['maxR'] <= BAR))}
theta6 = best6['theta']
pv6, chi6 = SP.unpack(theta6, 6)
OUT['N6_winner'] = {'pvecs': pv6.tolist(),
                    'chis_re': chi6.real.tolist(),
                    'chis_im': chi6.imag.tolist()}

# ------------------------------------------------ mode-count sweep
sweep = {}
for N in (4, 5, 7, 8):
    warm = None
    if N > 6:
        extra_p = []
        extra_c = []
        for _ in range(N - 6):
            d = rng.normal(size=3); d /= np.linalg.norm(d)
            extra_p.append(rng.uniform(0.05, 6.0) * d)
            extra_c.append((rng.normal(size=2)
                            + 1j * rng.normal(size=2)) * 0.01)
        warm = SP.pack(np.vstack([pv6, np.array(extra_p)]),
                       np.vstack([chi6, np.array(extra_c)]))
    resN, bestN = run_arm(N, 4, targets, warm=warm)
    sweep[N] = {'starts': resN, 'best_maxR': bestN['maxR'],
                'n_starts_at_bar': int(sum(
                    1 for r in resN if r['maxR'] <= BAR))}
    print(f'N={N}: best maxR {bestN["maxR"]:.3e}', flush=True)
OUT['sweep'] = {str(k): v for k, v in sweep.items()}
print(f'N=6: best maxR {best6["maxR"]:.3e}', flush=True)

# ------------------------------------------------ Jacobian SVD
def resid_only(th):
    return SP.resid_vec(th, 6, M_MASS, targets)

J = np.zeros((40, len(theta6)))
f0 = resid_only(theta6)
for j in range(len(theta6)):
    h = 1e-6 * max(1.0, abs(theta6[j]))
    th = theta6.copy(); th[j] += h
    J[:, j] = (resid_only(th) - f0) / h
sv = np.linalg.svd(J, compute_uv=False)
OUT['jacobian'] = {'singular_values': sv.tolist(),
                   'rank_at_1e-10': int(np.sum(sv > 1e-10)),
                   'smallest': float(sv[-1]),
                   'smallest_nonzero_class': float(sv[-3]),
                   'condition': float(sv[0] / sv[-1])}

# ------------------------------------------------ perturbation ladder
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
    pert[repr(eps)] = draws
    print(f'eps={eps}: ' + ', '.join(
        f"best {d['best_maxR']:.2e} bar={d['at_bar']}"
        for d in draws), flush=True)
OUT['perturbation'] = pert

print(json.dumps({k: v for k, v in OUT.items()
                  if k != 'N6_winner'}, indent=1)[:3000])
json.dump(OUT, open('/home/hatch/workspace/warp-pilot/gate34/'
                    'results/g34_item3.json', 'w'), indent=1)
