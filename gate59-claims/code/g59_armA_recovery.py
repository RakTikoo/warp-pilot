#!/usr/bin/env python
"""g59_armA_recovery.py -- recovery for g59_armA.py, which
died in a service restart after its search completed and
before it wrote its JSON (disclosed in GATE59_REPORT S10).

Recomputes deterministically: (1) the anatomy at
A_t1_N12; (2) the theta reconstruction and shell check;
(3) the constrained Jacobians at h = 1e-6 and 3e-7 (the
original run's logged sigma_min values are reproduced
below as the check); (4) the decisive warm re-convergence
at N = 12 (search + polish from the stored mating).
The original run's per-start search values survive in
g59_armA.log and are transcribed verbatim into the
record (marked as transcribed). The random-start sizes'
polish outcomes were in memory only and were lost; the
search-pass values stand (see the report).
Writes gate59/results/g59_armA.json.
"""
import json
import sys
import time

import numpy as np
from scipy.optimize import least_squares

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate59/work')
import g59_lib as G  # noqa: E402

RES = f'{WP}/gate59/results'
IU = G.IU

tg = json.load(open(f'{WP}/phase410/work/p410_targets.json'))
XS = [np.array(s['point']) for s in tg['sitesA']]
TG = [np.array(s['That']) for s in tg['sitesA']]
KEYS = [s['key'] for s in tg['sitesA']]
FROBS = np.array([np.linalg.norm(t) for t in TG])


def avecs(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


bj = json.load(open(f'{WP}/phase431/work/p431_best_A_t1_N12.json'))
PV12 = np.array(bj['pvecs']); AV12 = avecs(bj['avecs'])
EB12 = float(bj['info_Ebase'])

out = {'gate': 59,
       'recovery_note': 'g59_armA.py died in a service '
       'restart before writing its JSON; anatomy, Jacobian '
       'and the N=12 warm re-convergence recomputed here; '
       'per-start search values transcribed from '
       'g59_armA.log (the original run).'}

Rs, Ts = G.site_residuals(PV12, AV12, np.full(12, 1.0), XS, TG,
                          path='field')
anat = {}
for si in range(3):
    d = np.abs(Ts[si] - TG[si])
    order = sorted(((float(d[a, b]), f'T{a}{b}') for a, b in IU),
                   reverse=True)
    anat[KEYS[si]] = [{'component': lab, 'abs_residual': v}
                      for v, lab in order]
out['anatomy_gate'] = anat
out['anatomy_Rs'] = Rs


def dirs_from_angles(th, ph):
    return np.stack([np.sin(th) * np.cos(ph),
                     np.sin(th) * np.sin(ph), np.cos(th)], axis=1)


def build_A(theta, N):
    w = float(theta[0]); q = np.exp(w)
    E = np.sqrt(q ** 2 + 1.0)
    blk = theta[1:1 + 6 * N]
    th, ph = blk[:N], blk[N:2 * N]
    av = (blk[2 * N:4 * N] + 1j * blk[4 * N:6 * N]).reshape(N, 2)
    pv = dirs_from_angles(th, ph) * q
    return pv, av, np.full(N, 1.0), E


def resid_A(theta, N):
    pv, av, mm, _ = build_A(theta, N)
    S = G.pair_kernel(pv, av, mm)
    r = np.empty(30)
    for si in range(3):
        T = G.T_pair(S, pv, XS[si], mm=mm)
        d = T - TG[si]
        r[si * 10:(si + 1) * 10] = np.array(
            [d[a, b] for a, b in IU]) / FROBS[si]
    return r


def maxR_of(theta, N):
    pv, av, mm, _ = build_A(theta, N)
    Rs_, _ = G.site_residuals(pv, av, mm, XS, TG, path='pair')
    return max(Rs_)


def theta_from_mating(pv, av, E):
    q = np.sqrt(E ** 2 - 1.0)
    dirs = pv / q
    th = np.arccos(np.clip(dirs[:, 2], -1, 1))
    ph = np.arctan2(dirs[:, 1], dirs[:, 0])
    return np.concatenate([[np.log(q)], th, ph,
                           av.real.ravel(), av.imag.ravel()])


th12 = theta_from_mating(PV12, AV12, EB12)
out['theta_reconstruction_maxR'] = maxR_of(th12, 12)
out['stored_maxR_N12'] = float(bj['maxR'])
radii = np.linalg.norm(PV12, axis=1)
out['shell_radius_spread'] = float(radii.max() - radii.min())
out['shell_q_from_E'] = float(np.sqrt(EB12 ** 2 - 1))


def fd_jac(theta, N, hrel):
    n = len(theta)
    J = np.empty((30, n))
    for j in range(n):
        h = hrel * max(1.0, abs(theta[j]))
        tp = theta.copy(); tp[j] += h
        tm = theta.copy(); tm[j] -= h
        J[:, j] = (resid_A(tp, N) - resid_A(tm, N)) / (2 * h)
    return J


for hrel in (1e-6, 3e-7):
    J = fd_jac(th12, 12, hrel)
    sv = np.linalg.svd(J, compute_uv=False)
    out[f'jac_h{hrel:g}'] = {
        'sigma_min': float(sv[-1]), 'sigma_max': float(sv[0]),
        'rank_tol_1e-10_rel': int(np.sum(sv > 1e-10 * sv[0])),
        'sigma_5_smallest': [float(v) for v in sv[-5:]]}
    print('jac h =', hrel, ' sigma_min =', sv[-1],
          ' sigma_max =', sv[0], flush=True)
out['stored_constrained_jacobian'] = {
    'sigma_min': 0.0005408373155676678,
    'sigma_max': 2851.686640830329, 'rank': 30}
out['original_run_logged_sigma_min'] = {
    'h1e-6': 0.0005408346221368049, 'h3e-7': 0.0005408339163078754}

# warm re-convergence at N = 12 (search + polish)
t0 = time.time()
sol = least_squares(resid_A, th12, args=(12,), method='trf',
                    max_nfev=1200)
v_search = maxR_of(sol.x, 12)
sol2 = least_squares(resid_A, sol.x, args=(12,), method='trf',
                     xtol=1e-13, ftol=1e-13, gtol=1e-13,
                     max_nfev=4000)
v_polish = maxR_of(sol2.x, 12)
out['warm_reconvergence_N12'] = {
    'from_stored_maxR': float(bj['maxR']),
    'after_search_maxR': v_search,
    'after_polish_maxR': v_polish,
    'original_run_logged_search_value': 1.273481e-03,
    'wall_s': time.time() - t0}
print('warm N12: search', v_search, ' polish', v_polish,
      flush=True)

# transcribed per-start values from the original run's log
out['independent_search_transcribed_from_log'] = {
    '12': {'warm_stored': 1.273481e-03, 'rand0': 1.684696e-03,
           'rand1': 1.856004e-03, 'rand2': 1.835436e-03,
           'rand3': 1.868450e-03},
    '8': {'rand0': 1.668893e-03, 'rand1': 1.885602e-03,
          'rand2': 1.781114e-03, 'rand3': 1.848074e-03,
          'rand4': 1.836583e-03, 'rand5': 1.782265e-03},
    '6': {'rand0': 1.725452e-03, 'rand1': 1.932164e-03,
          'rand2': 1.816484e-03, 'rand3': 1.923931e-03,
          'rand4': 1.662092e-03, 'rand5': 1.910115e-03},
    '16': {'rand0': 1.652311e-03, 'rand1': 1.665417e-03,
           'rand2': 1.878546e-03},
    'note': 'search-pass maxR per start, transcribed from '
            'g59_armA.log; size polishes for the random-start '
            'sizes were in memory at the restart and are not '
            're-run (their starts sit 1.65e-3..1.93e-3, far '
            'from the floor basin; the phase\'s own polishes '
            'of like starts stayed >= 1.47e-3).'}
out['stored_size_bests'] = {'6': 0.001323624435513346,
                            '8': 0.00127316549597957,
                            '12': 0.001275415271657572}
out['firstpass_relaxation_from_log'] = {
    'note': 'undertrained 1500-step Adam, NOT converged; '
            'superseded by g59_relax2.json',
    'A3_peak': {'1.01': 5.440144e-03, '1.1': 1.001453e-02,
                '1.35': 2.377511e-03, '1.7': 4.753660e-03,
                '2.2': 1.063093e-02, '3.0': 2.481361e-02,
                '4.3': 5.962166e-02}}

json.dump(out, open(f'{RES}/g59_armA.json', 'w'), indent=1,
          default=str)
print('written g59_armA.json')
