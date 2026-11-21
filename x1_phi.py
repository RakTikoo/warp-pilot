"""
x1_phi.py — X1 EXTENSION: cross-section-asymmetric (phi-dependent)
toroidal profiles. The s-only exclusion (Pattern P9) leaves exactly one
corner uncovered: the deficit lives at the inner equator (phi=pi), and
s-only profiles cannot respond at one phi. Here

    a(s,phi) = a0(s) + W(s) [ a1(s) cos phi + a2(s) cos 2phi ]
    b(s,phi) = b0(s) + W(s) [ b1(s) cos phi + b2(s) cos 2phi ]

with a0, b0 the session-2 DE base (17 genes, x1_de layout) and the
corrections carried on 7 free knots s in {8,12,16,20,24,29,35} per
function (28 genes), pinned to zero at s=45 and multiplied by a C2
window W(s) that is exactly 0 for s<=5 and s>=45 (cavity and exterior
stay exactly as the base: flat). cos phi = (Rcyl-Rmaj)/s,
cos 2phi = ((Rcyl-Rmaj)^2 - z^2)/s^2. phi=0 is the OUTER equator,
phi=pi the INNER equator (facing the ring hole): a cos-phi term can
add material response at the inner face and remove it at the outer.

Protocol (Track P, unchanged): DE on an equator-emphasised screen ->
adversarial round on the union of arbiter point sets -> fresh-seed
finals at h=0.3 AND h=0.15 -> velocity ladder on the best base
(incl. S1 superluminal v in {1.1, 1.5, 2.0}). float64 everywhere.
"""
import json, sys, time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import differential_evolution

import shell as sh
import verify_metric as vm
import x1_torus as x1
import x1_de

DTYPE = np.float64
CKNOTS = np.array([5, 8, 12, 16, 20, 24, 29, 35, 45], dtype=DTYPE)
CFREE = list(range(1, 8))            # free correction knots: 8..35
N_CORR = 7
N_GENES = 17 + 4 * N_CORR            # 45


def _corr_spline(vals_free):
    v = np.zeros(len(CKNOTS))
    for j, ki in enumerate(CFREE):
        v[ki] = vals_free[j]
    return CubicSpline(CKNOTS, v)


def _window(s):
    s = np.asarray(s, dtype=DTYPE)
    up = sh.smootherstep((s - 5.0) / 4.0)          # 0 below 5, 1 above 9
    dn = 1.0 - sh.smootherstep((s - 40.0) / 5.0)   # 1 below 40, 0 above 45
    return up * dn


def genes_to_gfunc(genes, Rmaj, beta):
    base = x1_de.genes_to_profiles(genes[:17])
    a0, b0, smax = base['a_s'], base['b_s'], base['smax']
    a1 = _corr_spline(genes[17:24]); a2 = _corr_spline(genes[24:31])
    b1 = _corr_spline(genes[31:38]); b2 = _corr_spline(genes[38:45])

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        Rcyl = np.sqrt(x ** 2 + y ** 2)
        s = np.sqrt((Rcyl - Rmaj) ** 2 + z ** 2)
        sc = np.clip(s, 0.0, smax)
        ssafe = np.where(s > 1e-9, s, 1.0)
        u = (Rcyl - Rmaj) / ssafe
        c1 = u
        c2 = (u ** 2 - (z / ssafe) ** 2)
        W = _window(s)
        a = a0(sc) + W * (a1(sc) * c1 + a2(sc) * c2)
        b = b0(sc) + W * (b1(sc) * c1 + b2(sc) * c2)
        S = sh.shift_S(s, x1.R1, x1.R2, 'cos', 1.0, [x1.R1, x1.R2])
        d = u
        Rsafe = np.where(Rcyl > 1e-12, Rcyl, 1.0)
        ux = np.where(Rcyl > 1e-12, x / Rsafe, 0.0)
        uy = np.where(Rcyl > 1e-12, y / Rsafe, 0.0)
        shat = np.stack([d * ux, d * uy, z / ssafe], axis=1)
        P = pts.shape[0]
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2 * a)
        g[:, 0, 3] = g[:, 3, 0] = -S * beta
        eb = np.exp(2 * b) - 1.0
        for i in range(3):
            for j in range(3):
                g[:, 1 + i, 1 + j] = eb * shat[:, i] * shat[:, j]
            g[:, 1 + i, 1 + i] += 1.0
        return g

    return gfunc


def worst_margin(genes, Rmaj, beta, pts, h=0.3):
    gf = genes_to_gfunc(genes, Rmaj, beta)
    _, That, m = vm.einstein_at_points(gf, pts, h=h)
    worst = np.minimum(np.minimum(m['nec'], m['wec']),
                       np.minimum(m['sec'], m['dec']))
    return float(np.min(worst)), float(np.mean(m['typeI']))


def masked_audit(genes, Rmaj, beta, pts, h):
    """Ladder-style significance-masked audit (verdict numbers)."""
    gf = genes_to_gfunc(genes, Rmaj, beta)
    _, That, m = vm.einstein_at_points(gf, pts, h=h)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-7, 1e-3 * abs(rho_peak))
    sig = scale > thr
    out = {'rho_peak': rho_peak, 'n_sig': int(sig.sum())}
    if sig.sum():
        for k in ('nec', 'wec', 'sec', 'dec'):
            out[k] = float(np.min(m[k][sig]))
        out['worst'] = min(out[k] for k in ('nec', 'wec', 'sec', 'dec'))
        out['typeI_frac_sig'] = float(np.mean(m['typeI'][sig]))
    return out


BOUNDS = (x1_de.BOUNDS + [(-0.15, 0.15)] * (2 * N_CORR)
          + [(-0.15, 0.15)] * (2 * N_CORR))
_G = {'pts': None, 'Rmaj': 45.0, 'beta': 0.0}


def _obj(genes):
    w, _ = worst_margin(genes, _G['Rmaj'], _G['beta'], _G['pts'], h=0.3)
    return -w


def base_genes():
    d = json.load(open('results/x1_de2_Rmaj45.json'))
    return np.array(d['genes'])


def run_de(Rmaj, pts, init_genes, maxiter, seed, label):
    _G['pts'] = pts; _G['Rmaj'] = Rmaj; _G['beta'] = 0.0
    rng = np.random.default_rng(seed)
    pop_target = 2 * N_GENES
    rows = []
    for i in range(pop_target):
        g = np.array(init_genes, dtype=DTYPE)
        g[:17] += rng.normal(0, 0.006, 17)
        g[17:] += rng.normal(0, 0.02, N_GENES - 17)
        rows.append(g)
    rows[0] = np.array(init_genes, dtype=DTYPE)
    rows[1] = np.array(init_genes, dtype=DTYPE)
    rows[1][:17] = base_genes()          # de2 winner with zero corrections
    lo = np.array([b[0] for b in BOUNDS]); hi = np.array([b[1] for b in BOUNDS])
    init = np.clip(np.array(rows), lo, hi)
    t0 = time.time()
    res = differential_evolution(_obj, BOUNDS, maxiter=maxiter, popsize=2,
                                 mutation=(0.3, 1.2), recombination=0.8,
                                 init=init, polish=False, seed=seed)
    el = time.time() - t0
    print(f'[{label}] DE done: nfev={res.nfev} elapsed={el:.0f}s '
          f'obj={res.fun:+.4e}', flush=True)
    return res.x, int(res.nfev), el


def main():
    Rmaj = float(sys.argv[1]) if len(sys.argv) > 1 else 45.0
    t00 = time.time()
    out = {'Rmaj': Rmaj, 'aspect': Rmaj / 15.0, 'extension': 'phi-dependent'}
    # ---- stage 1: DE on screen seed 111
    pts_screen = x1_de.screen_points(Rmaj, seed=111)
    g0 = np.zeros(N_GENES); g0[:17] = base_genes()
    genes, nfev1, el1 = run_de(Rmaj, pts_screen, g0, maxiter=110,
                               seed=20261122, label='stage1')
    w, tI = worst_margin(genes, Rmaj, 0.0, pts_screen, h=0.3)
    out.update({'stage1_screen_worst': w, 'stage1_typeI': tI,
                'stage1_nfev': nfev1, 'stage1_elapsed_s': el1})
    print(f'[stage1] screen worst {w:+.4e} TypeI {tI:.3f}', flush=True)
    # ---- stage 2: adversarial round on union of arbiter sets
    pts_union = np.concatenate([x1_de.screen_points(Rmaj, seed=s,
                                n=200 if s == 111 else 320)
                                for s in (111, 999, 31337)])
    genes2, nfev2, el2 = run_de(Rmaj, pts_union, genes, maxiter=55,
                                seed=777, label='stage2-adv')
    w2, tI2 = worst_margin(genes2, Rmaj, 0.0, pts_union, h=0.3)
    out.update({'stage2_train_worst': w2, 'stage2_typeI': tI2,
                'stage2_nfev': nfev2, 'stage2_elapsed_s': el2,
                'genes': genes2.tolist()})
    print(f'[stage2] train worst {w2:+.4e} TypeI {tI2:.3f}', flush=True)
    # ---- finals: fresh seeds, both resolutions, torus_points arbiters
    for seed in (555001, 777001):
        pts_a = x1.torus_points(Rmaj, seed, n_tube=300)
        for h in (0.3, 0.15):
            wa, ta = worst_margin(genes2, Rmaj, 0.0, pts_a, h=h)
            out[f'final_seed{seed}_h{h}'] = {'worst': wa, 'typeI': ta}
            print(f'  final seed={seed} h={h}: worst {wa:+.4e} '
                  f'TypeI {ta:.3f}', flush=True)
    out['elapsed_s'] = time.time() - t00
    json.dump(out, open(f'results/x1_phi_Rmaj{int(Rmaj)}.json', 'w'),
              indent=1, default=float)
    print('X1 PHI DONE', flush=True)


if __name__ == '__main__':
    main()
