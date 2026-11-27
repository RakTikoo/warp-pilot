#!/usr/bin/env python
"""g59_relax2.py -- Gate-59 per-site dictionary relaxation,
converged version (supersedes the relaxation section of
g59_armA.py, whose 1500-step Adam pass did not converge --
reported as such).

Per site, per shell energy E: dictionary = 128 Fibonacci
directions x 2 spin basis (192 modes, m = 1, all at energy
E); amplitudes free per site. Optimisation of
||T(c) - T_target||_F over c in C^192: Adam (1500 steps,
BLAS-shaped contractions) then scipy least_squares
(method trf) with the ANALYTIC Jacobian (dT/du = 2 Re P,
dT/dv = -2 Im P, P_kab = sum_i c*_i S_ikab) on the 10
upper-triangle components.
The feasible set strictly contains the joint problem's
per-site behaviour (amplitudes unshared across sites,
directions dense), so a converged floor here is evidence
about the single-shell family at one site.
Writes gate59/results/g59_relax2.json.
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
N = 192

tg = json.load(open(f'{WP}/phase410/work/p410_targets.json'))
XS = [np.array(s['point']) for s in tg['sitesA']]
TG = [np.array(s['That']) for s in tg['sitesA']]
KEYS = [s['key'] for s in tg['sitesA']]


def fib_dirs(n):
    i = np.arange(n)
    y = 1 - (2 * i + 1) / n
    r = np.sqrt(np.maximum(0.0, 1 - y ** 2))
    ga = np.pi * (3 - np.sqrt(5.0))
    ph = ga * i
    return np.stack([r * np.cos(ph), r * np.sin(ph), y], axis=1)


def dict_basis(E, ndir=96):
    q = np.sqrt(max(E ** 2 - 1.0, 0.0))
    pv, av, mm = [], [], []
    for d in fib_dirs(ndir):
        for s in range(2):
            chi = np.zeros(2, dtype=complex); chi[s] = 1.0
            pv.append(q * d); av.append(chi); mm.append(1.0)
    return np.array(pv), np.array(av), np.array(mm)


class Site:
    """Precomputed BLAS-shaped views of the pair kernel."""

    def __init__(self, S, TGt):
        self.TGt = TGt
        # T: w_{k,ab} = sum_j S_kjab c_j -> (k,a,b,j) reshape
        self.S_T = np.ascontiguousarray(
            S.transpose(0, 2, 3, 1)).reshape(N * 16, N)
        # M: M_kj = sum_ab D_ab S_kjab -> (k,j,ab) reshape
        self.S_M = np.ascontiguousarray(S).reshape(N * N, 16)
        # P: P_{k,ab} = sum_i c*_i S_ikab -> (k,a,b,i) reshape
        self.S_P = np.ascontiguousarray(
            S.transpose(1, 2, 3, 0)).reshape(N * 16, N)

    def T_of(self, c):
        w = (self.S_T @ c).reshape(N, 16)
        return (c.conj() @ w).reshape(4, 4).real

    def resid(self, c):
        d = self.T_of(c) - self.TGt
        return np.array([d[a, b] for a, b in IU])

    def grad(self, c, D):
        M = (self.S_M @ D.reshape(16)).reshape(N, N)
        return 2.0 * (M @ c)

    def jac(self, x):
        c = x[:N] + 1j * x[N:]
        P = (self.S_P @ c.conj()).reshape(N, 4, 4)
        Ju = np.array([[2 * P[k, a, b].real for k in range(N)]
                       for a, b in IU])
        Jv = np.array([[-2 * P[k, a, b].imag for k in range(N)]
                       for a, b in IU])
        return np.concatenate([Ju, Jv], axis=1)

    def resid_x(self, x):
        return self.resid(x[:N] + 1j * x[N:])


def adam(site, steps, seed):
    r = np.random.default_rng(seed)
    c = 0.02 * (r.normal(size=N) + 1j * r.normal(size=N))
    m1 = np.zeros(N, dtype=complex); m2 = np.zeros(N)
    best = (np.inf, c.copy())
    for it in range(1, steps + 1):
        D = site.T_of(c) - site.TGt
        f = float(np.sum(D ** 2))
        if f < best[0]:
            best = (f, c.copy())
        g = site.grad(c, D)
        lr = 0.01 + 0.04 * 0.5 * (1 + np.cos(np.pi * it / steps))
        m1 = 0.9 * m1 + 0.1 * g
        m2 = 0.999 * m2 + 0.001 * np.abs(g) ** 2
        mh = m1 / (1 - 0.9 ** it)
        vh = m2 / (1 - 0.999 ** it)
        c = c - lr * mh / (np.sqrt(vh) + 1e-12)
    return best


def run_site_E(si, E, seed=11):
    pv, av, mm = dict_basis(E)
    S = G.pair_kernel(pv, av, mm)
    site = Site(S, TG[si])
    fbest, cbest = adam(site, 1500, seed)
    x0 = np.concatenate([cbest.real, cbest.imag])
    sol = least_squares(site.resid_x, x0, jac=site.jac,
                        method='trf', max_nfev=300)
    c = sol.x[:N] + 1j * sol.x[N:]
    frob = float(np.linalg.norm(site.T_of(c) - TG[si]))
    return {'site': KEYS[si], 'E': E,
            'adam_frob': float(np.sqrt(fbest)),
            'polished_frob': frob,
            'price_abs_c2': float(np.sum(np.abs(c) ** 2)),
            'c': c, 'site_obj': site}


out = {'gate': 59, 'note': 'converged relaxation; supersedes '
         'the g59_armA.json first-pass relaxation section '
         '(undertrained Adam, not converged)'}
E_list = [1.005852660028616, 1.2, 1.5, 2.0, 3.0, 4.3]
rows3 = []
best3 = None
for E in E_list:
    t0 = time.time()
    r = run_site_E(2, E)
    rows3.append({k: r[k] for k in
                  ('site', 'E', 'adam_frob', 'polished_frob',
                   'price_abs_c2')})
    print(f"A3 E={E}: adam {r['adam_frob']:.4e} polished "
          f"{r['polished_frob']:.4e} price {r['price_abs_c2']:.3f}"
          f" ({time.time() - t0:.0f}s)", flush=True)
    if best3 is None or r['polished_frob'] < best3['polished_frob']:
        best3 = r
out['A3_peak_scan'] = rows3
site = best3['site_obj']
T = site.T_of(best3['c'])
d = np.abs(T - TG[2])
out['A3_best_anatomy'] = [
    {'component': f'T{a}{b}', 'abs_residual': float(d[a, b])}
    for a, b in sorted(IU, key=lambda ab: -d[ab])]
out['A3_best_E'] = best3['E']
others = []
for si in (0, 1):
    for E in (1.005852660028616, best3['E']):
        r = run_site_E(si, E, seed=23)
        others.append({k: r[k] for k in
                       ('site', 'E', 'adam_frob', 'polished_frob',
                        'price_abs_c2')})
        print(f"{KEYS[si]} E={E}: polished "
              f"{r['polished_frob']:.4e}", flush=True)
out['other_sites'] = others
out['joint_fit_site_residuals'] = {
    'A1_joint_argmin': 5.6073686065139795e-05,
    'A2_sec_argmin': 0.00034858841170036796,
    'A3_peak': 0.0012754152716575767}
json.dump(out, open(f'{RES}/g59_relax2.json', 'w'), indent=1,
          default=str)
print('written g59_relax2.json')
