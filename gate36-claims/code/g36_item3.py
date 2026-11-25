"""Gate-36 Worker C: Item 3 - the conditioning question (E1-E5).
Uses ONLY g36_spinor.py for computation. Checkpoints after each experiment.
"""
import json, time, sys, os
import numpy as np
from scipy.optimize import least_squares
import g36_spinor as G

ROOT = '/home/hatch/workspace/warp-pilot/'
WORK = ROOT + 'gate36/work/'
BAR = 1e-9
N = 6

RESULTS = {}
NEW_SOL = {'E1_pointwise_extra': [], 'E2_weaker': [], 'E5_scaled': []}

def ckpt(tag):
    with open(WORK + 'g36_item3_results.json', 'w') as f:
        json.dump(RESULTS, f, indent=1)
    with open(WORK + 'g36_item3_solutions.json', 'w') as f:
        json.dump(NEW_SOL, f, indent=1)
    print(f'[ckpt {tag}]', flush=True)

def load_targets(path):
    d = json.load(open(path))
    sites = [np.array(s['point'], dtype=float) for s in d['sites']]
    thats = [np.array(s['That'], dtype=float) for s in d['sites']]
    frobs = [float(np.linalg.norm(T)) for T in thats]
    return d, sites, thats, frobs

def load_bestfit_theta(path):
    d = json.load(open(path))
    p = np.array([m['pvec'] for m in d['modes']], dtype=float)
    a = np.array([[complex(*v) for v in m['a']] for m in d['modes']])
    return G.theta_from_modes(p, a)

def random_start(rng, N):
    mags = rng.uniform(0.05, 6.0, size=N)
    dirs = rng.normal(size=(N, 3)); dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    p = mags[:, None] * dirs
    a = (rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2))) * 0.03
    return G.theta_from_modes(p, a)

def warm_theta_257(N):
    d = json.load(open(ROOT + 'phase257/work/p257_bestfit.json'))
    ps, as_ = [], []
    for m in d['modes']:
        pv = np.array(m['pvec'], dtype=float)
        E = np.sqrt(np.dot(pv, pv) + 1.0)
        u = np.array([complex(*v) for v in m['u']]); c = complex(*m['c'])
        as_.append(c * (u[:2] / np.sqrt(E + 1.0))); ps.append(pv)
    return G.theta_from_modes(np.array(ps), np.array(as_))

def do_fit(theta0, sites, thats, frobs, max_nfev=900, method='trf', tol=None):
    kw = dict(method=method, max_nfev=max_nfev)
    if tol is not None:
        kw.update(xtol=tol, gtol=tol, ftol=tol)
    fun = lambda th: G.resid_vec(th, N, sites, thats, frobs)
    r = least_squares(fun, theta0, **kw)
    p, a = G.modes_from_theta(r.x, N)
    Rs_d, _, _ = G.direct_residuals(p, a, sites, thats)
    return r.x, Rs_d, int(r.nfev)

def census_entry(name, theta, sites, thats, frobs):
    p, a = G.modes_from_theta(theta, N)
    Rs_d, _, _ = G.direct_residuals(p, a, sites, thats)
    J, sv = G.fd_jacobian(theta, N, sites, thats, frobs, h_rel=1e-6)
    return {'start': name, 'sigma_min': float(sv[-1]), 'sv': [float(v) for v in sv],
            'sigma_max': float(sv[0]), 'maxR_direct': float(max(Rs_d)),
            'Rs_direct': [float(v) for v in Rs_d],
            'abs_a_sq': float(np.sum(np.abs(a) ** 2)),
            'max_abs_p': float(np.max(np.linalg.norm(p, axis=1)))}

def main():
    t0 = time.time()
    _, sites320, thats320, frobs320 = load_targets(ROOT + 'phase320/work/p320_targets.json')
    _, sites313, thats313, frobs313 = load_targets(ROOT + 'phase313/work/p313_targets.json')
    solsB = json.load(open(WORK + 'g36_item2_solutions.json'))['N6_pointwise']
    by_name = {s['start']: np.array(s['theta']) for s in solsB}

    # ---------------- E1: pointwise census ----------------
    print('E1 ...', flush=True)
    e1 = []
    for nm in ['warm0', 'rand2', 'rand0']:
        e = census_entry(nm, by_name[nm], sites320, thats320, frobs320)
        e1.append(e); print(f"  {nm}: smin={e['sigma_min']:.6e} maxR={e['maxR_direct']:.3e}", flush=True)
    n_succ = 3; spent = 0
    while n_succ < 6 and spent < 12:
        k = spent; spent += 1
        rngk = np.random.default_rng(3603 * 1000 + N * 100 + k)
        th, Rs_d, nfev = do_fit(random_start(rngk, N), sites320, thats320, frobs320, 900)
        mx = max(Rs_d)
        print(f"  extra rand{k}: maxR={mx:.3e} nfev={nfev}", flush=True)
        if mx <= BAR:
            nm = f'extra{k}'
            e = census_entry(nm, th, sites320, thats320, frobs320)
            e['nfev'] = nfev; e1.append(e); n_succ += 1
            NEW_SOL['E1_pointwise_extra'].append({'start': nm, 'theta': [float(v) for v in th],
                                                  'Rs_direct': [float(v) for v in Rs_d]})
            print(f"    SUCCESS smin={e['sigma_min']:.6e}", flush=True)
        RESULTS['E1'] = {'census': e1, 'extra_starts_spent': spent}
        ckpt('E1-progress')
    RESULTS['E1'] = {'census': e1, 'extra_starts_spent': spent,
                     'n_success_total': n_succ}
    ckpt('E1')

    # ---------------- E2: weaker-target census ----------------
    print('E2 ...', flush=True)
    e2 = []; n2 = 0
    todo = [('warm0', warm_theta_257(N))] + \
           [(f'rand{k}', random_start(np.random.default_rng(3604 * 1000 + N * 100 + k), N)) for k in range(8)]
    extra = 0
    while True:
        for nm, th0 in todo:
            th, Rs_d, nfev = do_fit(th0, sites313, thats313, frobs313, 900)
            mx = max(Rs_d)
            print(f"  {nm}: maxR={mx:.3e} nfev={nfev}", flush=True)
            if mx <= BAR:
                e = census_entry(nm, th, sites313, thats313, frobs313)
                e['nfev'] = nfev; e2.append(e); n2 += 1
                NEW_SOL['E2_weaker'].append({'start': nm, 'theta': [float(v) for v in th],
                                             'Rs_direct': [float(v) for v in Rs_d]})
                print(f"    SUCCESS smin={e['sigma_min']:.6e}", flush=True)
            RESULTS['E2'] = {'census': e2, 'n_success': n2, 'extra_starts': extra}
            ckpt('E2-progress')
        if n2 >= 3 or extra >= 6:
            break
        todo = [(f'extra{k}', random_start(np.random.default_rng(3604 * 1000 + N * 100 + 100 + k), N))
                for k in range(extra, extra + 3)]
        extra += 3
    RESULTS['E2'] = {'census': e2, 'n_success': n2, 'extra_starts': extra}
    ckpt('E2')

    # ---------------- E3 ----------------
    print('E3 ...', flush=True)
    th320 = load_bestfit_theta(ROOT + 'phase320/work/p320_joint_bestfit.json')
    _, sv_b = G.fd_jacobian(th320, N, sites320, thats320, frobs320, h_rel=1e-6)
    th_pol, Rs_pol, nfev_pol = do_fit(th320, sites320, thats320, frobs320, 2000, tol=1e-15)
    _, sv_a = G.fd_jacobian(th_pol, N, sites320, thats320, frobs320, h_rel=1e-6)
    e3 = {'polish': {'sigma_min_before': float(sv_b[-1]), 'sigma_min_after': float(sv_a[-1]),
                     'theta_displacement': float(np.linalg.norm(th_pol - th320)),
                     'maxR_after_direct': float(max(Rs_pol)), 'nfev': nfev_pol}}
    print('  polish:', e3['polish'], flush=True)
    # dogbox from rand2
    th_db, Rs_db, nfev_db = do_fit(by_name['rand2'], sites320, thats320, frobs320, 900, method='dogbox')
    db = {'success': bool(max(Rs_db) <= BAR), 'maxR_direct': float(max(Rs_db)), 'nfev': nfev_db}
    if db['success']:
        _, sv_db = G.fd_jacobian(th_db, N, sites320, thats320, frobs320, h_rel=1e-6)
        db['sigma_min'] = float(sv_db[-1])
    e3['dogbox_from_rand2'] = db
    print('  dogbox:', db, flush=True)
    # h-stability at best E2 solution
    best_e2 = min(e2, key=lambda e: e['maxR_direct'])
    th_e2 = None
    for s in NEW_SOL['E2_weaker']:
        if s['start'] == best_e2['start']:
            th_e2 = np.array(s['theta'])
    hs = {}
    for h in [1e-5, 1e-6, 1e-7]:
        _, svh = G.fd_jacobian(th_e2, N, sites313, thats313, frobs313, h_rel=h)
        hs[f'h={h:g}'] = float(svh[-1])
    e3['h_stability_weaker_best'] = {'start': best_e2['start'], 'sigma_min_by_h': hs}
    print('  h-stab weaker:', hs, flush=True)
    RESULTS['E3'] = e3
    ckpt('E3')

    # ---------------- E4 ----------------
    print('E4 ...', flush=True)
    def structure(theta, sites, thats, frobs):
        J, sv = G.fd_jacobian(theta, N, sites, thats, frobs, h_rel=1e-6)
        U, S, Vt = np.linalg.svd(J, full_matrices=True)
        v = Vt[-1]; u = U[:, -1]
        per_mode = []
        for j in range(N):
            idx = [3*j, 3*j+1, 3*j+2, 3*N+2*j, 3*N+2*j+1, 5*N+2*j, 5*N+2*j+1]
            per_mode.append(float(np.sum(v[idx] ** 2)))
        classes = {'p': float(np.sum(v[:3*N] ** 2)),
                   'Re_a': float(np.sum(v[3*N:5*N] ** 2)),
                   'Im_a': float(np.sum(v[5*N:7*N] ** 2))}
        per_site = [float(np.sum(u[10*s:10*s+10] ** 2)) for s in range(4)]
        comp = sorted(range(40), key=lambda i: -abs(u[i]))[:3]
        top = [{'flat_index': int(i), 'site': int(i // 10),
                'component_ab': [int(x) for x in G.UPPER_IDX[i % 10]],
                'value': float(u[i]), 'weight': float(u[i] ** 2)} for i in comp]
        return {'sv_tail_last6': [float(x) for x in sv[-6:]],
                'right_vec_per_mode_weight': per_mode,
                'right_vec_class_weight': classes,
                'left_vec_per_site_weight': per_site,
                'left_vec_top3_components': top}
    def target_stats(thats):
        fro = [float(np.linalg.norm(T)) for T in thats]
        allc = np.concatenate([np.abs(T).ravel() for T in thats])
        nz = allc[allc > 0]
        rhos = [float(T[0, 0]) for T in thats]
        return {'per_site_frob': fro, 'dynamic_range_all': float(nz.max() / nz.min()),
                'max_abs_component': float(nz.max()), 'min_nonzero_abs_component': float(nz.min()),
                'rhos': rhos, 'rho_spread_max_over_min': float(max(rhos) / min(rhos))}
    e4 = {'pointwise_warm0': structure(by_name['warm0'], sites320, thats320, frobs320),
          'weaker_best': {'start': best_e2['start'],
                          **structure(th_e2, sites313, thats313, frobs313)},
          'targets_pointwise': target_stats(thats320),
          'targets_weaker': target_stats(thats313),
          'scatter': {'pointwise': [{'start': e['start'], 'sigma_min': e['sigma_min'],
                                     'abs_a_sq': e['abs_a_sq'], 'max_abs_p': e['max_abs_p']} for e in e1],
                      'weaker': [{'start': e['start'], 'sigma_min': e['sigma_min'],
                                  'abs_a_sq': e['abs_a_sq'], 'max_abs_p': e['max_abs_p']} for e in e2]}}
    RESULTS['E4'] = e4
    ckpt('E4')
    print('  E4 done', flush=True)

    # ---------------- E5: scale probe x4 ----------------
    print('E5 ...', flush=True)
    thats4 = [4.0 * T for T in thats320]; frobs4 = [float(np.linalg.norm(T)) for T in thats4]
    th_w = by_name['warm0'].copy(); th_w[3*N:] *= 2.0
    p_w, a_w = G.modes_from_theta(th_w, N)
    Rs_w0, _, _ = G.direct_residuals(p_w, a_w, sites320, thats4)
    starts5 = [('warm_scaled_exact', th_w, 0)]
    cand5 = []
    e_w = census_entry('warm_scaled_exact', th_w, sites320, thats4, frobs4)
    cand5.append(e_w)
    print(f"  warm scaled exact: maxR={max(Rs_w0):.3e} smin={e_w['sigma_min']:.6e}", flush=True)
    for k in range(2):
        rngk = np.random.default_rng(3605 * 1000 + N * 100 + k)
        th, Rs_d, nfev = do_fit(random_start(rngk, N), sites320, thats4, frobs4, 900)
        print(f"  rand{k}: maxR={max(Rs_d):.3e} nfev={nfev}", flush=True)
        if max(Rs_d) <= BAR:
            e = census_entry(f'rand{k}', th, sites320, thats4, frobs4); e['nfev'] = nfev
            cand5.append(e)
            NEW_SOL['E5_scaled'].append({'start': f'rand{k}', 'theta': [float(v) for v in th],
                                         'Rs_direct': [float(v) for v in Rs_d]})
    best5 = min(cand5, key=lambda e: e['maxR_direct'])
    RESULTS['E5'] = {'census': cand5, 'best_start': best5['start'],
                     'best_sigma_min': best5['sigma_min'],
                     'warm_scaled_exact_maxR_before_refit': float(max(Rs_w0))}
    ckpt('E5')
    RESULTS['wall_time_s'] = time.time() - t0
    ckpt('DONE')
    print('DONE in', RESULTS['wall_time_s'], flush=True)

if __name__ == '__main__':
    main()
