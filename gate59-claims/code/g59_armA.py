#!/usr/bin/env python
"""g59_armA.py -- Gate-59 re-check of the Arm A / T_req negative.

(1) Anatomy at the confirmed mating A_t1_N12 (gate's field
    path): per-site residual components.
(2) Constrained Jacobian at the reconstructed registered
    theta (gate's parameterisation build + central FD, the
    phase's recipe h = 1e-6 * max(1, |theta_j|), plus a
    second h for FD stability): sigma_min / sigma_max /
    rank.
(3) Independent joint search in the registered
    parameterisation (gate's residual): warm start from the
    stored mating; fresh random starts at N = 6, 8, 12 and
    a beyond-scope probe at N = 16; the phase's A1/A2
    protocol (search at defaults, cap 1200; polish the
    size best at 1e-13, cap 4000).
(4) Per-site dictionary relaxation: at each site separately,
    a dense fixed dictionary of shell directions (128
    Fibonacci directions x 2 spin basis = 256 modes) with
    FREE per-site amplitudes, amplitudes optimised by Adam
    on ||T - T_target||_F^2, E scanned. This feasible set
    strictly contains the joint problem's per-site
    behaviour (amplitudes unshared, directions dense), so
    its floor is evidence about the shell family itself.
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
BAR = 1e-9
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

out = {'gate': 59}

# ---------- (1) anatomy ----------
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
print('anatomy done', flush=True)

# ---------- parameterisation (registered form, gate's build) ----------
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
    Rs, _ = G.site_residuals(pv, av, mm, XS, TG, path='pair')
    return max(Rs)


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

# ---------- (2) constrained Jacobian ----------
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
    print('jac h =', hrel, ' sigma_min =', sv[-1], flush=True)
out['stored_constrained_jacobian'] = {
    'sigma_min': 0.0005408373155676678,
    'sigma_max': 2851.686640830329, 'rank': 30}

# ---------- (3) independent joint search ----------
rng = np.random.default_rng(20261127)


def rand_theta(N):
    E = float(np.exp(rng.uniform(np.log(1.02), np.log(5.0))))
    q = np.sqrt(E ** 2 - 1)
    th = np.arccos(rng.uniform(-1, 1, N))
    ph = rng.uniform(0, 2 * np.pi, N)
    av = 0.03 * (rng.normal(size=(N, 2))
                 + 1j * rng.normal(size=(N, 2)))
    return np.concatenate([[np.log(q)], th, ph,
                           av.real.ravel(), av.imag.ravel()])


def run_size(N, starts):
    best = None
    recs = []
    for name, th0 in starts:
        t0 = time.time()
        sol = least_squares(resid_A, th0, args=(N,), method='trf',
                            max_nfev=1200)
        v = maxR_of(sol.x, N)
        recs.append({'start': name, 'maxR': v,
                     'wall_s': time.time() - t0})
        if best is None or v < best[1]:
            best = (name, v, sol.x)
        print(f'  N={N} {name}: {v:.6e}', flush=True)
    # polish the size best (A1 pattern)
    sol = least_squares(resid_A, best[2], args=(N,), method='trf',
                        xtol=1e-13, ftol=1e-13, gtol=1e-13,
                        max_nfev=4000)
    v = maxR_of(sol.x, N)
    if v < best[1]:
        best = (best[0] + '+polish', v, sol.x)
    return {'best_start': best[0], 'best_maxR': best[1],
            'starts': recs}


search = {}
search['12'] = run_size(12, [('warm_stored', th12)]
                        + [(f'rand{i}', rand_theta(12))
                           for i in range(4)])
search['8'] = run_size(8, [(f'rand{i}', rand_theta(8))
                           for i in range(6)])
search['6'] = run_size(6, [(f'rand{i}', rand_theta(6))
                           for i in range(6)])
search['16'] = run_size(16, [(f'rand{i}', rand_theta(16))
                             for i in range(3)])
out['independent_search'] = search
out['stored_size_bests'] = {'6': 0.001323624435513346,
                            '8': 0.00127316549597957,
                            '12': 0.001275415271657572}
print('search done', flush=True)

# ---------- (4) per-site dictionary relaxation ----------
def fib_dirs(n):
    i = np.arange(n)
    y = 1 - (2 * i + 1) / n
    r = np.sqrt(np.maximum(0.0, 1 - y ** 2))
    ga = np.pi * (3 - np.sqrt(5.0))
    ph = ga * i
    return np.stack([r * np.cos(ph), r * np.sin(ph), y], axis=1)


def dict_basis(E, ndir=128):
    q = np.sqrt(max(E ** 2 - 1.0, 0.0))
    dirs = fib_dirs(ndir)
    pv, av, mm = [], [], []
    for d in dirs:
        for s in range(2):
            chi = np.zeros(2, dtype=complex); chi[s] = 1.0
            pv.append(q * d); av.append(chi); mm.append(1.0)
    return (np.array(pv), np.array(av), np.array(mm))


def adam_site(si, E, steps=1500, seed=7, c0=None):
    pv, av, mm = dict_basis(E)
    S = G.pair_kernel(pv, av, mm)
    n = len(pv)
    r = np.random.default_rng(seed)
    c = (0.01 * (r.normal(size=n) + 1j * r.normal(size=n))
         if c0 is None else c0.copy())
    m1 = np.zeros(n, dtype=complex); m2 = np.zeros(n)
    best = (np.inf, None)
    for it in range(1, steps + 1):
        T = np.einsum('i,ijab,j->ab', c.conj(), S, c).real
        D = T - TG[si]
        f = float(np.sum(D ** 2))
        if f < best[0]:
            best = (f, c.copy())
        M = np.einsum('ab,kjab->kj', D, S)
        g = 2.0 * (M @ c)
        lr = 0.05 * (0.999 ** it) + 0.002
        m1 = 0.9 * m1 + 0.1 * g
        m2 = 0.999 * m2 + 0.001 * np.abs(g) ** 2
        mh = m1 / (1 - 0.9 ** it)
        vh = m2 / (1 - 0.999 ** it)
        c = c - lr * mh / (np.sqrt(vh) + 1e-12)
    return float(np.sqrt(best[0])), best[1]


relax = {}
E_grid = [1.01, 1.1, 1.35, 1.7, 2.2, 3.0, 4.3]
c_carry = None
rows = []
for E in E_grid:
    v, c_carry = adam_site(2, E, c0=c_carry)
    rows.append({'E': E, 'site': KEYS[2], 'min_frob_resid': v})
    print(f'  relax A3 E={E}: {v:.6e}', flush=True)
relax['A3_peak'] = rows
E_best = min(rows, key=lambda r: r['min_frob_resid'])['E']
for si in (0, 1):
    v, _ = adam_site(si, E_best)
    relax.setdefault('others_at_E_best', []).append(
        {'E': E_best, 'site': KEYS[si], 'min_frob_resid': v})
    print(f'  relax {KEYS[si]} E={E_best}: {v:.6e}', flush=True)
    v2, _ = adam_site(si, EB12)
    relax.setdefault('others_at_E_stored', []).append(
        {'E': EB12, 'site': KEYS[si], 'min_frob_resid': v2})
    print(f'  relax {KEYS[si]} E={EB12}: {v2:.6e}', flush=True)
out['dictionary_relaxation'] = relax
out['joint_site_residuals_stored'] = {
    KEYS[i]: float(Rs[i]) for i in range(3)}

json.dump(out, open(f'{RES}/g59_armA.json', 'w'), indent=1,
          default=str)
print('written g59_armA.json')
