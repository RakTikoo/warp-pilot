"""
x1_de.py — X1 free-form toroidal profiles: differential evolution over
a(s), b(s) spline knots (Track P protocol: screen -> re-randomised
arbiter at h AND h/2 -> fresh-seed finals). beta=0 base first; the shift
ladder is audited afterwards on whatever base survives (profiles are
beta-independent).

Knots s_k = [0, 6, 10, 13, 16, 19, 22, 26, 31, 37, 45].
Genes (17): a_in (shared by knots 0, 6), a at knots 10..37 (8),
            b at knots 10..37 (8).  b(knots 0, 6) = 0 (cavity),
            a(45) = b(45) = 0 (exact flat exterior for s >= 45).
CubicSpline (natural) through the knots; gfunc as in x1_torus.
"""
import json, sys, time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import differential_evolution

import shell as sh
import verify_metric as vm
import x1_torus as x1

DTYPE = np.float64
KNOTS = np.array([0, 6, 10, 13, 16, 19, 22, 26, 31, 37, 45], dtype=DTYPE)
FREE_KNOT_IDX = list(range(2, 10))          # knots 10..37
try:
    RMAJ = float(sys.argv[1]) if len(sys.argv) > 1 else 45.0
except ValueError:
    RMAJ = 45.0   # imported by other scripts with their own argv
SEED_PROFILES = []                          # filled by seed_genes()


def genes_to_profiles(genes):
    a_vals = np.zeros(len(KNOTS)); b_vals = np.zeros(len(KNOTS))
    a_vals[0] = a_vals[1] = genes[0]
    for j, ki in enumerate(FREE_KNOT_IDX):
        a_vals[ki] = genes[1 + j]
        b_vals[ki] = genes[9 + j]
    a_vals[-1] = 0.0; b_vals[-1] = 0.0
    return {'a_s': CubicSpline(KNOTS, a_vals), 'b_s': CubicSpline(KNOTS, b_vals),
            'smax': 45.0, 'M': None, 'delta': None, 'a_in': float(genes[0]),
            'prof': None}


def screen_points(Rmaj, seed, n=200):
    rng = np.random.default_rng(seed)
    smax = 45.0
    s_rand = np.concatenate([
        rng.uniform(6.0, 30.0, int(0.6 * n)),
        rng.uniform(28.0, smax + 4.0, n - int(0.6 * n))])
    phi = rng.uniform(0, 2 * np.pi, len(s_rand))
    th = rng.uniform(0, 2 * np.pi, len(s_rand))
    Rc = Rmaj + s_rand * np.cos(phi)
    pts = [np.stack([Rc * np.cos(th), Rc * np.sin(th),
                     s_rand * np.sin(phi)], axis=1)]
    # structured emphasis on the binding equators phi=0, pi and the poles
    ns = 60
    s_s = rng.uniform(8.0, 34.0, ns)
    phi_s = rng.choice([0.0, np.pi, np.pi / 2, 3 * np.pi / 2], ns)
    th_s = rng.uniform(0, 2 * np.pi, ns)
    Rc = Rmaj + s_s * np.cos(phi_s)
    pts.append(np.stack([Rc * np.cos(th_s), Rc * np.sin(th_s),
                         s_s * np.sin(phi_s)], axis=1))
    return np.concatenate(pts).astype(DTYPE)


def worst_margin(genes, Rmaj, beta, pts, h=0.3):
    tp = genes_to_profiles(genes)
    gf = x1.torus_gfunc(tp, Rmaj, beta)
    _, That, m = vm.einstein_at_points(gf, pts, h=h)
    worst = np.minimum(np.minimum(m['nec'], m['wec']),
                       np.minimum(m['sec'], m['dec']))
    return float(np.min(worst)), float(np.mean(m['typeI']))


def seed_genes():
    """Windowed spherical-profile knot values at several amplitude scales
    and window widths, as DE initial population rows."""
    rows = []
    for M in (2.0, 3.0):
        for delta in (10.0, 15.0, 20.0):
            tp = x1.torus_profiles(M, delta=delta)
            a_k = tp['a_s'](KNOTS); b_k = tp['b_s'](KNOTS)
            for kap in (0.8, 1.0, 1.25):
                g = np.empty(17)
                g[0] = a_k[0] * kap
                g[1:9] = a_k[FREE_KNOT_IDX] * kap
                g[9:17] = b_k[FREE_KNOT_IDX] * kap
                rows.append(g)
    return rows


BOUNDS = [(-0.40, 0.10)] + [(-0.40, 0.10)] * 8 + [(-0.10, 0.40)] * 8


_G = {'pts': None, 'Rmaj': RMAJ, 'beta': 0.0}


def _obj(genes):
    """Module-level (picklable) DE objective: -worst margin on the screen."""
    w, _ = worst_margin(genes, _G['Rmaj'], _G['beta'], _G['pts'], h=0.3)
    return -w


def main():
    t0 = time.time()
    pts_screen = screen_points(RMAJ, seed=111)
    _G['pts'] = pts_screen; _G['Rmaj'] = RMAJ
    print(f'X1 DE base search: Rmaj={RMAJ} aspect={RMAJ/15:.2f}, '
          f'screen pts={len(pts_screen)}', flush=True)

    obj = _obj

    init = np.array(seed_genes())
    # pad init to popsize*17 rows with jittered copies
    pop_target = 2 * 17
    rng = np.random.default_rng(5)
    rows = [init[i % len(init)] for i in range(pop_target)]
    pad = np.array(rows) + rng.normal(0, 0.01, (pop_target, 17))
    pad[0] = init[2]  # clean M=2, delta=15, kap=1 row kept exact-ish
    res = differential_evolution(obj, BOUNDS, maxiter=150, popsize=2,
                                 mutation=(0.3, 1.2), recombination=0.8,
                                 init=pad, polish=False, seed=20261121)
    genes = res.x
    w_screen, tI = worst_margin(genes, RMAJ, 0.0, pts_screen, h=0.3)
    out = {'Rmaj': RMAJ, 'aspect': RMAJ / 15.0, 'beta': 0.0,
           'screen_worst': w_screen, 'screen_typeI': tI,
           'genes': genes.tolist(), 'n_evals': int(res.nfev),
           'elapsed_s': time.time() - t0}
    print('DE done:', json.dumps({k: out[k] for k in
          ('screen_worst', 'screen_typeI', 'n_evals', 'elapsed_s')}),
          flush=True)
    # arbiter: fresh seeds, both resolutions (stencil-artefact rule)
    for seed in (999, 31337):
        pts_a = screen_points(RMAJ, seed=seed, n=320)
        for h in (0.3, 0.15):
            w, tI = worst_margin(genes, RMAJ, 0.0, pts_a, h=h)
            out[f'arbiter_seed{seed}_h{h}'] = {'worst': w, 'typeI': tI}
            print(f'  arbiter seed={seed} h={h}: worst {w:+.4e} '
                  f'TypeI {tI:.3f}', flush=True)
    json.dump(out, open(f'results/x1_de_Rmaj{int(RMAJ)}.json', 'w'),
              indent=1, default=float)
    print('X1 DE DONE', flush=True)


if __name__ == '__main__':
    main()
