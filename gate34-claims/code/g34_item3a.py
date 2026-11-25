#!/usr/bin/env python3
"""
g34_item3a.py -- Gate-34 Item 3, stage A: C4 control
(gate builder on Phase 313's stored winner; pairwise
fast path validated against the direct builder) and
the N = 6 reproduction fit with the gate optimiser
(own starts, seed 3401). Persists incrementally.
"""
import json
import numpy as np
import sys
from scipy.optimize import least_squares

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate34/work')
import g34_spinor as SP

M_MASS = 1.0
BAR = 1e-9
OUTP = '/home/hatch/workspace/warp-pilot/gate34/results/g34_item3a.json'
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
    a = np.array(md['a'])
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
# fast path validation: pairwise vs direct at all sites
S_bf = SP.pairwise_S(pv_bf, chi_bf, M_MASS)
fast_diff = 0.0
for pt, That, frob in targets:
    Td = SP.stress_at(pv_bf, chi_bf, M_MASS, pt)
    Tf = SP.T_pairwise(S_bf, pv_bf, pt)
    fast_diff = max(fast_diff, float(np.max(np.abs(Td - Tf))))
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
    'pairwise_vs_direct_max_diff': fast_diff,
    'bar': 1e-11,
    'pass': bool(max(abs(a - b) for a, b in
                     zip(Rs_c4, bf['Rs_direct'])) <= 1e-11
                 and max(abs(a - b) for a, b in
                         zip(rhos_c4, bf['rhos_direct'])) <= 1e-11
                 and dres <= 1e-9 and fast_diff <= 1e-12)}
json.dump(OUT, open(OUTP, 'w'), indent=1)
print('C4:', json.dumps(OUT['C4']), flush=True)

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


def fit(theta0, N, tgts, max_nfev=1200):
    sol = least_squares(SP.resid_vec, theta0, args=(N, M_MASS, tgts),
                        method='trf', max_nfev=max_nfev,
                        xtol=1e-12, ftol=1e-12, gtol=1e-12)
    pvecs, chis = SP.unpack(sol.x, N)
    Rs, rhos = SP.direct_residuals(pvecs, chis, M_MASS, tgts)
    return {'theta': sol.x, 'maxR': float(np.max(Rs)), 'Rs': Rs,
            'rhos': rhos, 'nfev': int(sol.nfev)}


# ------------------------------------------------ N = 6 reproduction
starts = []
best6 = None
for i in range(6):
    r = fit(rand_theta(6), 6, targets)
    starts.append({'start': f'rand{i}', 'maxR': r['maxR'],
                   'nfev': r['nfev']})
    print(f'N=6 rand{i}: maxR {r["maxR"]:.3e}', flush=True)
    if best6 is None or r['maxR'] < best6['maxR']:
        best6 = r
OUT['N6_reproduction'] = {
    'starts': starts, 'best_maxR': best6['maxR'],
    'best_Rs': best6['Rs'], 'best_rhos': best6['rhos'],
    'rho_targets': rho_tgt,
    'n_starts_at_bar': int(sum(1 for r in starts
                               if r['maxR'] <= BAR))}
pv6, chi6 = SP.unpack(best6['theta'], 6)
OUT['N6_winner'] = {'theta': best6['theta'].tolist(),
                    'pvecs': pv6.tolist(),
                    'chis_re': chi6.real.tolist(),
                    'chis_im': chi6.imag.tolist()}
json.dump(OUT, open(OUTP, 'w'), indent=1)
print('N=6 best:', best6['maxR'], flush=True)
