"""Gate-36 Worker B driver: controls CTRL-S1/S2/S3 + Item 2 ladder on the
pointwise (Phase 320) targets, using ONLY g36_spinor.py for computation.
Stored artefacts are read as data. Results persist incrementally per arm.
"""
import json, time, sys
import numpy as np
from scipy.optimize import least_squares
import g36_spinor as G

ROOT = '/home/hatch/workspace/warp-pilot/'
WORK = ROOT + 'gate36/work/'
BAR = 1e-9
SEED_BASE = 3601
SEED_PERT = 3602

RESULTS = {}
SOLUTIONS = {'N6_pointwise': []}


def save_arm(name):
    with open(WORK + f'g36_item2_arm_{name}.json', 'w') as f:
        json.dump({'results': RESULTS, 'solutions': SOLUTIONS}, f, indent=1)
    print(f'[saved arm {name}]', flush=True)


def load_targets(path):
    d = json.load(open(path))
    sites = [np.array(s['point'], dtype=float) for s in d['sites']]
    thats = [np.array(s['That'], dtype=float) for s in d['sites']]
    frobs = [float(np.linalg.norm(T)) for T in thats]
    return d, sites, thats, frobs


def load_bestfit(path):
    d = json.load(open(path))
    p = np.array([m['pvec'] for m in d['modes']], dtype=float)
    a = np.array([[complex(*v) for v in m['a']] for m in d['modes']])
    return d, p, a


def jac_stats(theta, N, sites, thats, frobs, h_rel=1e-6):
    J, sv = G.fd_jacobian(theta, N, sites, thats, frobs, h_rel=h_rel)
    rank = int(np.sum(sv > 1e-10 * sv[0]))
    return {'sv': [float(v) for v in sv], 'sigma_min': float(sv[-1]),
            'sigma_max': float(sv[0]), 'rank_rel_1e-10': rank,
            'shape': list(J.shape)}


def random_start(rng, N):
    mags = rng.uniform(0.05, 6.0, size=N)
    dirs = rng.normal(size=(N, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    p = mags[:, None] * dirs
    a = (rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2))) * 0.03
    return G.theta_from_modes(p, a)


def warm_theta_257(N, rng):
    d = json.load(open(ROOT + 'phase257/work/p257_bestfit.json'))
    ps, as_ = [], []
    for m in d['modes']:
        pv = np.array(m['pvec'], dtype=float)
        E = np.sqrt(np.dot(pv, pv) + 1.0)
        u = np.array([complex(*v) for v in m['u']])
        c = complex(*m['c'])
        a = c * (u[:2] / np.sqrt(E + 1.0))
        ps.append(pv); as_.append(a)
    p = np.array(ps); a = np.array(as_)
    if N > 6:
        extra_p = rng.normal(size=(N - 6, 3)) * 0.5
        extra_a = (rng.normal(size=(N - 6, 2)) + 1j * rng.normal(size=(N - 6, 2))) * 0.003
        p = np.vstack([p, extra_p]); a = np.vstack([a, extra_a])
    elif N < 6:
        p, a = p[:N], a[:N]
    return G.theta_from_modes(p, a)


def do_fit(theta0, N, sites, thats, frobs, max_nfev):
    fun = lambda th: G.resid_vec(th, N, sites, thats, frobs)
    r = least_squares(fun, theta0, method='trf', max_nfev=max_nfev)
    p, a = G.modes_from_theta(r.x, N)
    Rs_pw = G.pairwise_residuals(p, a, sites, thats)
    return r.x, Rs_pw, int(r.nfev)


def main():
    t0 = time.time()
    # ---------------- data ----------------
    d320, sites320, thats320, frobs320 = load_targets(ROOT + 'phase320/work/p320_targets.json')
    b320, p320, a320 = load_bestfit(ROOT + 'phase320/work/p320_joint_bestfit.json')
    d313, sites313, thats313, frobs313 = load_targets(ROOT + 'phase313/work/p313_targets.json')
    b313, p313, a313 = load_bestfit(ROOT + 'phase313/work/p313_joint_bestfit.json')

    # ---------------- CTRL-S3 ----------------
    print('CTRL-S3 ...', flush=True)
    rng = np.random.default_rng(SEED_BASE)
    rand_max = 0.0; rand_max_rel = 0.0
    for trial in range(8):
        N = int(rng.integers(2, 9))
        pp = rng.normal(size=(N, 3)) * 2.0
        aa = (rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2))) * 0.4
        xx = rng.normal(size=3) * 4.0
        Td = G.T_direct_complex(pp, aa, xx); Tp = G.T_pairwise_complex(pp, aa, xx)
        diff = float(np.max(np.abs(Td - Tp)))
        rel = diff / max(float(np.linalg.norm(Td)), 1e-300)
        rand_max = max(rand_max, diff); rand_max_rel = max(rand_max_rel, rel)
    s3 = {'random_sets_max_abs_diff': rand_max, 'random_sets_max_rel_diff': rand_max_rel}
    for tag, (pp, aa, ss) in {'p320_winner': (p320, a320, sites320),
                              'p313_winner': (p313, a313, sites313)}.items():
        mx = 0.0
        for x in ss:
            mx = max(mx, float(np.max(np.abs(G.T_direct_complex(pp, aa, x)
                                             - G.T_pairwise_complex(pp, aa, x)))))
        s3[f'{tag}_max_abs_diff'] = mx
    RESULTS['CTRL_S3'] = s3
    print(' CTRL-S3:', s3, flush=True)
    save_arm('ctrl_s3')

    # ---------------- CTRL-S1 ----------------
    print('CTRL-S1 ...', flush=True)
    Rs, rhos, _ = G.direct_residuals(p320, a320, sites320, thats320)
    th320 = G.theta_from_modes(p320, a320)
    js = jac_stats(th320, 6, sites320, thats320, frobs320)
    RESULTS['CTRL_S1'] = {
        'Rs_direct': Rs,
        'Rs_stored': b320['Rs_direct'],
        'Rs_diff': [abs(x - y) for x, y in zip(Rs, b320['Rs_direct'])],
        'rhos_direct': rhos,
        'rhos_stored': b320['rhos_direct'],
        'rhos_diff': [abs(x - y) for x, y in zip(rhos, b320['rhos_direct'])],
        'jacobian_at_stored_winner': js,
        'jacobian_stored': {'sigma_min': 3.994e-4, 'sigma_max': 3.909e3, 'rank': 40},
    }
    print(' CTRL-S1 Rs:', Rs, 'jac smin/smax/rank:', js['sigma_min'], js['sigma_max'], js['rank_rel_1e-10'], flush=True)
    save_arm('ctrl_s1')

    # ---------------- CTRL-S2 ----------------
    print('CTRL-S2 ...', flush=True)
    Rs313, rhos313, _ = G.direct_residuals(p313, a313, sites313, thats313)
    th313 = G.theta_from_modes(p313, a313)
    js313 = jac_stats(th313, 6, sites313, thats313, frobs313)
    RESULTS['CTRL_S2'] = {
        'Rs_direct': Rs313, 'maxR_direct': max(Rs313),
        'maxR_stored': 3.253e-13, 'maxR_stored_exact': b313['maxR_direct'],
        'rhos_direct': rhos313,
        'jacobian_sigma_min': js313['sigma_min'], 'jacobian_sigma_max': js313['sigma_max'],
        'jacobian_rank_rel_1e-10': js313['rank_rel_1e-10'],
        'jacobian_sv': js313['sv'],
    }
    print(' CTRL-S2 maxR:', max(Rs313), 'sigma_min:', js313['sigma_min'], flush=True)
    save_arm('ctrl_s2')

    # ---------------- Item 2 ladder (pointwise targets) ----------------
    ladder = {}
    plan = [(4, 6, 0, 900), (5, 6, 0, 900), (6, 8, 1, 900), (8, 3, 1, 1300)]
    best = {'theta': None, 'maxR': np.inf, 'N': None}
    for N, n_rand, n_warm, max_nfev in plan:
        starts = []
        rng_w = np.random.default_rng(SEED_BASE + 500 + N)
        todo = []
        for w in range(n_warm):
            todo.append((f'warm{w}', warm_theta_257(N, rng_w)))
        for k in range(n_rand):
            rngk = np.random.default_rng(SEED_BASE * 1000 + N * 100 + k)
            todo.append((f'rand{k}', random_start(rngk, N)))
        for name, th0 in todo:
            th, Rs_pw, nfev = do_fit(th0, N, sites320, thats320, frobs320, max_nfev)
            mx = max(Rs_pw)
            starts.append({'start': name, 'maxR_pairwise': mx,
                           'per_site_R_pairwise': Rs_pw, 'nfev': nfev})
            print(f'  N={N} {name}: maxR={mx:.3e} nfev={nfev}', flush=True)
            if mx <= BAR:
                pp, aa = G.modes_from_theta(th, N)
                Rs_d, _, _ = G.direct_residuals(pp, aa, sites320, thats320)
                if N == 6:
                    SOLUTIONS['N6_pointwise'].append(
                        {'start': name, 'theta': [float(v) for v in th],
                         'maxR_pairwise': mx, 'Rs_direct': Rs_d})
                if max(Rs_d) < best['maxR']:
                    best = {'theta': th, 'maxR': max(Rs_d), 'N': N}
            if N == 6 and mx <= BAR and best['N'] != 6:
                pass
        ladder[f'N{N}'] = {'starts': starts,
                           'n_at_bar': int(sum(1 for s in starts if s['maxR_pairwise'] <= BAR)),
                           'best_maxR_pairwise': min(s['maxR_pairwise'] for s in starts)}
        RESULTS['ladder_pointwise'] = ladder
        save_arm(f'ladder_N{N}')

    # best N=6 solution: prefer best among persisted N=6 solutions (direct maxR)
    cand = SOLUTIONS['N6_pointwise']
    assert cand, 'no N=6 solution at bar'
    cand.sort(key=lambda s: max(s['Rs_direct']))
    best6 = cand[0]
    th6 = np.array(best6['theta'])
    p6, a6 = G.modes_from_theta(th6, 6)
    print('Best N=6 from start', best6['start'], 'maxR direct', max(best6['Rs_direct']), flush=True)

    # ---------------- best-solution diagnostics ----------------
    print('Diagnostics at best N=6 ...', flush=True)
    Rs_d, rhos_fit, Ts_fit = G.direct_residuals(p6, a6, sites320, thats320)
    rhos_tgt = [float(T[0, 0]) for T in thats320]
    seg_fit = [G.segre_type(T)[0] for T in Ts_fit]
    seg_tgt = [G.segre_type(T)[0] for T in thats320]
    diracs = [G.dirac_residual(p6[j], G.spinor_U(p6[j], a6[j])[0]) for j in range(6)]
    a2 = float(np.sum(np.abs(a6) ** 2))

    # D-a: per-site amplitude refits (freeze p and a; per-site multipliers alpha)
    da = []
    aj_norm2 = np.sum(np.abs(a6) ** 2, axis=1)  # per-mode |a_j|^2
    for s in range(4):
        x, That, fb = sites320[s], thats320[s], frobs320[s]
        S_unit = None

        def resid_alpha(y):
            alpha = np.empty(6, dtype=complex)
            alpha[0] = y[0]
            alpha[1:] = y[1:6] + 1j * y[6:11]
            aa = a6 * alpha[:, None]
            Tf = G.T_pairwise(p6, aa, x)
            d = (Tf - That) / fb
            return np.array([d[i, j] for (i, j) in G.UPPER_IDX])

        y0 = np.zeros(11); y0[0] = 1.0; y0[1:6] = 1.0
        r = least_squares(resid_alpha, y0, method='trf', max_nfev=400)
        alpha = np.empty(6, dtype=complex)
        alpha[0] = r.x[0]; alpha[1:] = r.x[1:6] + 1j * r.x[6:11]
        aa = a6 * alpha[:, None]
        Tf = G.T_direct(p6, aa, x)
        R_after = float(np.linalg.norm(Tf - That))
        implied = float(np.sum(aj_norm2 * np.abs(alpha) ** 2))  # = |a|^2 * weighted |alpha|^2
        da.append({'site': s, 'R_after_refit_direct': R_after,
                   'alpha': [[float(v.real), float(v.imag)] for v in alpha],
                   'implied_s2_alpha_route': implied})
    # Leg-3 kstar route (kstar present in p320 targets)
    leg3 = []
    ahat = a6 / np.sqrt(a2)
    for s in range(4):
        ks = np.array(d320['sites'][s]['kstar'], dtype=float)
        Tf_unit = G.T_direct(p6, ahat, sites320[s])
        tkk_unit = float(ks @ Tf_unit @ ks)
        tkk_tgt = float(ks @ thats320[s] @ ks)
        leg3.append({'site': s, 'tkk_target': tkk_tgt, 'tkk_unit': tkk_unit,
                     'implied_s2_kstar': tkk_tgt / tkk_unit})
    diag = {'start': best6['start'], 'theta': [float(v) for v in th6],
            'Rs_direct': Rs_d, 'maxR_direct': max(Rs_d),
            'rhos_fit': rhos_fit, 'rhos_target': rhos_tgt,
            'segre_fit': seg_fit, 'segre_target': seg_tgt,
            'dirac_residuals': diracs, 'abs_a_sq': a2,
            'D_a': da, 'leg3_kstar': leg3}
    RESULTS['best_N6_diagnostics'] = diag
    save_arm('diagnostics')

    # Jacobian at best N=6 + h stability
    print('Jacobian at best N=6 ...', flush=True)
    jb = jac_stats(th6, 6, sites320, thats320, frobs320, h_rel=1e-6)
    jb['sigma_min_h1e-5'] = jac_stats(th6, 6, sites320, thats320, frobs320, h_rel=1e-5)['sigma_min']
    jb['sigma_min_h1e-7'] = jac_stats(th6, 6, sites320, thats320, frobs320, h_rel=1e-7)['sigma_min']
    RESULTS['best_N6_jacobian'] = jb
    print(' jac smin:', jb['sigma_min'], 'h1e-5:', jb['sigma_min_h1e-5'], 'h1e-7:', jb['sigma_min_h1e-7'], flush=True)
    save_arm('jacobian')

    # ---------------- perturbation ladder ----------------
    print('Perturbation ladder ...', flush=True)
    rngp = np.random.default_rng(SEED_PERT)
    pert = []
    for eps in [1e-12, 1e-9, 1e-6, 1e-4]:
        for draw in range(2):
            thats_p, frobs_p = [], []
            for s in range(4):
                U = rngp.uniform(-1, 1, size=(4, 4))
                U = 0.5 * (U + U.T)
                Tp_ = thats320[s] + eps * frobs320[s] * U
                thats_p.append(Tp_); frobs_p.append(float(np.linalg.norm(Tp_)))
            attempts = []
            thw, Rs_w, _ = do_fit(th6, 6, sites320, thats_p, frobs_p, 900)
            attempts.append(('warm', thw, Rs_w))
            rngf = np.random.default_rng(SEED_PERT * 1000 + int(-np.log10(eps)) * 10 + draw)
            thf, Rs_f, _ = do_fit(random_start(rngf, 6), 6, sites320, thats_p, frobs_p, 900)
            attempts.append(('fresh', thf, Rs_f))
            recs = []
            for nm, thx, _ in attempts:
                px, ax = G.modes_from_theta(thx, 6)
                Rd, rho_d, _ = G.direct_residuals(px, ax, sites320, thats_p)
                recs.append({'start': nm, 'maxR_direct_vs_perturbed': max(Rd),
                             'Rs_direct': Rd, 'rhos_fit': rho_d})
            best_rec = min(recs, key=lambda r: r['maxR_direct_vs_perturbed'])
            pert.append({'eps': eps, 'draw': draw, 'attempts': recs,
                         'best_maxR_direct': best_rec['maxR_direct_vs_perturbed'],
                         'best_rhos_fit': best_rec['rhos_fit'],
                         'perturbed_target_rhos': [float(T[0, 0]) for T in thats_p]})
            print(f'  eps={eps:g} draw={draw}: best maxR={best_rec["maxR_direct_vs_perturbed"]:.3e}', flush=True)
        RESULTS['perturbation_ladder'] = pert
        save_arm(f'pert_eps{eps:g}')

    RESULTS['wall_time_s'] = time.time() - t0
    with open(WORK + 'g36_item2_results.json', 'w') as f:
        json.dump(RESULTS, f, indent=1)
    with open(WORK + 'g36_item2_solutions.json', 'w') as f:
        json.dump(SOLUTIONS, f, indent=1)
    print('DONE in', RESULTS['wall_time_s'], 's', flush=True)


if __name__ == '__main__':
    main()
