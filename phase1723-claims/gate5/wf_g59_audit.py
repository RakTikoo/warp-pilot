#!/usr/bin/env python3
"""wf_g59_audit.py -- Gate-5 W-F deciding run for G5-9.
Uses ONLY wf_g59_lib machinery + shared definitions (stored coeffs,
bed factory, volume point set, tolerances, registered point seeds).
Writes wf_g59_numbers.json. float64.
"""
import json, sys, time
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate5')
import wf_g59_lib as W

RES19 = '/home/hatch/workspace/warp-pilot/phase19/results/'
RES14 = '/home/hatch/workspace/warp-pilot/phase14/results/'
OUT = '/home/hatch/workspace/warp-pilot/gate5/wf_g59_numbers.json'
M2_GRID = (0.1, 0.3, 1.0, 3.0, 10.0, 30.0)
ROWS = [  # (key in coeffs, beta, pair, kind)
    ('D1_b1.5_(3.0, 0.0)', 1.5, (3.0, 0.0), 'd1'),
    ('D1_b1.1_(3.0, 0.0)', 1.1, (3.0, 0.0), 'd1'),
    ('D1_b1.5_(1.0, 0.0)', 1.5, (1.0, 0.0), 'd1'),
    ('D1_b1.5_(0.0, 0.0)', 1.5, (0.0, 0.0), 'd1'),
    ('D1_b0.1_(3.0, 0.0)', 0.1, (3.0, 0.0), 'd1'),
]
tolmap = {0.1: 1.813458068412236e-06, 1.1: 5.16299634087247e-05,
          1.5: 6.569380798832041e-05}


def pts_seed(seed, n):
    rng = np.random.default_rng(seed)
    d = rng.standard_normal((n, 3))
    d /= np.linalg.norm(d, axis=1)[:, None]
    return d * rng.uniform(9.5, 20.5, n)[:, None]


def prof_of(coeff, kind):
    if kind == 'd1':
        return lambda q: W.profiles_d1(q, coeff)
    return lambda q: W.profiles_d0(q, coeff)


def constraint_block(beta, pair, coeff, kind, label):
    gf = W.g_factory(beta)
    b = W.dictionary(*pair)
    prof = prof_of(coeff, kind)

    def Cfunc(q):
        C, _ = W.C_tensor(gf(q), W.f_matrix(q, prof(q)), 1.0, b)
        return C
    sets = {'coll': pts_seed(191191, 128) if kind == 'd1'
            else pts_seed(143143, 48),
            'phase_fresh': pts_seed(191777, 64),
            'my_fresh': pts_seed(590590, 128)}
    out = {}
    for sname, pts in sets.items():
        for h in (0.3, 0.15):
            rel, _, _ = W.divergence_rel(gf, Cfunc, pts, h)
            out[f'{sname}_{h}'] = dict(
                pooled=float(np.median(rel)),
                t=float(np.median(rel[:, 0])),
                per_comp=[float(x) for x in np.median(rel, axis=0)])
        print(f'  {label} {sname} done', flush=True)
    return out


def main():
    t0 = time.time()
    coeffs = np.load(RES19 + 'p191_coeffs.npz')
    cache = {bt: np.load(RES14 + f'p143_cache_b{bt}.npz')
             for bt in ('0.1', '1.1', '1.5')}
    res = dict(constraint={}, volume={}, identity={})

    # ---------- machinery gate: density identity, my code ----------
    rng = np.random.default_rng(5901)
    gf15 = W.g_factory(1.5)
    pts = pts_seed(5902, 8)
    co = coeffs['D1_b1.5_(3.0, 0.0)']
    g = gf15(pts)
    f = W.f_matrix(pts, W.profiles_d1(pts, co))
    # add generic non-proportional perturbations of f
    worst, worst_norev = 0.0, 0.0
    for trial in range(6):
        b = rng.uniform(-2, 3, 5)
        fp = f.copy()
        if trial > 0:
            pert = rng.uniform(-0.15, 0.15, (len(pts), 4, 4))
            pert = 0.5 * (pert + np.swapaxes(pert, -1, -2))
            fp = f + pert
        for i in range(len(pts)):
            S = W.sqrt_principal(np.linalg.inv(g[i]) @ fp[i])
            eS, _ = W.e_and_Y(S[None])
            Sinv = np.linalg.inv(S)
            eI, _ = W.e_and_Y(Sinv[None])
            lhs = np.sqrt(-np.linalg.det(g[i])) * float(eS[0] @ b)
            rhs = np.sqrt(-np.linalg.det(fp[i])) * float(
                eI[0] @ b[::-1])
            rhs_nr = np.sqrt(-np.linalg.det(fp[i])) * float(
                eI[0] @ b)
            den = max(abs(lhs), 1e-300)
            worst = max(worst, abs(lhs - rhs) / den)
            worst_norev = max(worst_norev, abs(lhs - rhs_nr) / den)
    res['identity'] = dict(density_identity_worst_rel=float(worst),
                           not_reversed_worst_rel=float(worst_norev))
    print('identity worst rel', worst, 'norev', worst_norev, flush=True)

    # C_f action-FD gate (my FD): D_mn = d(sqrt(-f) L_int^f)/d f^mn,
    # L_int^f = m2 * sum_m b_{4-m} e_m(sqrt(f^-1 g)); expect
    # C_f = -2/sqrt(-f) * D (best global scalar fit reported).
    def dens_f(fin, gin, m2, b):
        out = np.empty(len(fin))
        for i in range(len(fin)):
            S = W.sqrt_principal(np.linalg.inv(fin[i]) @ gin[i])
            e, _ = W.e_and_Y(S[None])
            out[i] = np.sqrt(-np.linalg.det(fin[i])) * m2 * float(
                e[0] @ b[::-1])
        return out
    b = W.dictionary(0.7, -0.4)
    m2 = 1.3
    eps = 1e-6
    errs = []
    for i in range(4):
        fi = np.linalg.inv(f[i])
        D = np.zeros((4, 4))
        for mu in range(4):
            for nu in range(mu, 4):
                E = np.zeros((4, 4)); E[mu, nu] += 1
                if mu != nu:
                    E[nu, mu] += 1
                dp = dens_f(np.linalg.inv((fi + eps * E)[None]),
                            g[i][None], m2, b)[0]
                dm = dens_f(np.linalg.inv((fi - eps * E)[None]),
                            g[i][None], m2, b)[0]
                D[mu, nu] = D[nu, mu] = (dp - dm) / (2 * eps)
        Cf, _ = W.C_f_tensor(g[i][None], f[i][None], m2, b)
        pred = -2.0 / np.sqrt(-np.linalg.det(f[i])) * D
        errs.append(float(np.max(np.abs(pred - Cf[0]))
                          / np.max(np.abs(Cf[0]))))
    res['identity']['Cf_action_FD_max_rel'] = float(max(errs))
    print('Cf FD max rel', max(errs), flush=True)

    # ---------- (a)+(b): constraint audits, D1 rows + D0 control ----
    for key, beta, pair, kind in ROWS:
        print(f'constraint {key}', flush=True)
        res['constraint'][key] = constraint_block(
            beta, pair, coeffs[key], kind, key)
    # D0 radial stored in coeffs is the fresh re-solve; also audit it
    print('constraint D0', flush=True)
    res['constraint']['D0_radial_b1.5_30'] = constraint_block(
        1.5, (3.0, 0.0), coeffs['D0_radial_b1.5_30'], 'd0', 'D0')
    json.dump(res, open(OUT, 'w'), indent=2)

    # ---------- (c)+(d): volume EC audits ---------------------------
    Gg_cache = {}
    for key, beta, pair, kind in ROWS:
        print(f'volume {key}', flush=True)
        tol = tolmap[beta]
        cch = cache[str(beta)]
        pts_v, r_v = cch['pts_v'], cch['r_v']
        gf = W.g_factory(beta)
        g_v = gf(pts_v)
        coeff = coeffs[key]
        prof = prof_of(coeff, kind)
        ff = lambda q: W.f_matrix(q, prof(q))
        f_v = ff(pts_v)
        b = W.dictionary(*pair)
        Cf1, _ = W.C_f_tensor(g_v, f_v, 1.0, b)
        Cg1, _ = W.C_tensor(g_v, f_v, 1.0, b)
        if beta not in Gg_cache:
            Gg, _ = W.einstein_of(gf, pts_v, 0.15)
            Gg_cache[beta] = Gg
            print(f'  G_g beta={beta} done ({time.time()-t0:.0f}s)',
                  flush=True)
        Gg = Gg_cache[beta]
        row_out = {}
        for h in (0.3, 0.15):
            Gf, _ = W.einstein_of(ff, pts_v, h)
            print(f'  G_f h={h} done ({time.time()-t0:.0f}s)',
                  flush=True)
            per_m2 = {}
            for m2 in M2_GRID:
                Theta = (Gf + m2 * Cf1) / W.EIGHT_PI
                That_f = W.eulerian_that(f_v, Theta)
                That_g = W.eulerian_that(g_v, Theta)
                mf = W.ec_margins(That_f)
                mg = W.ec_margins(That_g)
                scale = np.abs(Gf) + m2 * np.abs(Cf1)
                rel = np.abs(Gf + m2 * Cf1) / np.maximum(scale, 1e-300)
                mask = scale > 1e-8 * np.max(scale)
                Treq = (Gg + m2 * Cg1) / W.EIGHT_PI
                That_req = W.eulerian_that(g_v, Treq)
                mr = W.ec_margins(That_req)
                per_m2[str(m2)] = dict(
                    theta_f=W.vol_fracs(mf, r_v, tol),
                    theta_g_nec=W.vol_fracs(mg, r_v, tol)['nec'],
                    theta0_dist=float(np.median(rel[mask])),
                    treq=W.vol_fracs(mr, r_v, tol))
            row_out[str(h)] = per_m2
        res['volume'][key] = row_out
        json.dump(res, open(OUT, 'w'), indent=2)
    print('ALL DONE', time.time() - t0, flush=True)


if __name__ == '__main__':
    main()
