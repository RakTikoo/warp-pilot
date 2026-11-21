"""
trackP.py — Track P: machine-led free-form search over shell profiles.

Density weight and shift profile are PCHIP splines through free knots
(no named shapes). Optimiser: scipy differential_evolution on the
screening sample; arbiter: the point auditor on RE-RANDOMISED dense
point sets the optimiser never saw, at h and h/2 (anti-artefact rules).

Genes (16): 8 density log-knots on [R1,R2]; 6 shift interior knots on
[R1,R2] (endpoints pinned S=1 at R1, S=0 at R2); s_rho; s_P.
Usage: python3 trackP.py <beta> <M> [maxiter]
"""
import json, sys, time
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import differential_evolution
import shell as sh
import trackL as tl

FREE = {'theta_d': None, 'svals': None, 'R1': 10.0, 'R2': 20.0}
NDK = 8   # density knots
NSK = 6   # shift interior knots

_orig_weight = sh.weight
_orig_shift = sh.shift_S


def _free_weight(r, R1, R2, kind, params):
    if kind != 'free':
        return _orig_weight(r, R1, R2, kind, params)
    kr = np.linspace(R1, R2, NDK)
    w = np.exp(FREE['theta_d'])
    f = PchipInterpolator(kr, w, extrapolate=False)
    out = np.zeros_like(r)
    inside = (r >= R1) & (r <= R2)
    out[inside] = np.maximum(f(r[inside]), 0.0)
    return out


def _free_shift(r, R1, R2, kind='free', Rb=1.0, ws=None):
    if kind != 'free':
        return _orig_shift(r, R1, R2, kind, Rb, ws)
    kr = np.linspace(R1, R2, NSK + 2)
    sv = np.concatenate([[1.0], FREE['svals'], [0.0]])
    f = PchipInterpolator(kr, sv, extrapolate=False)
    out = np.where(r <= R1, 1.0, 0.0)
    mid = (r > R1) & (r < R2)
    out[mid] = np.clip(f(r[mid]), 0.0, 1.0)
    return out


sh.weight = _free_weight
sh.shift_S = _free_shift


def screen_points(R1, R2, ndir=12, seed=42):
    rng = np.random.default_rng(seed)
    i = np.arange(ndir)
    phi = np.arccos(1 - 2 * (i + 0.5) / ndir)
    th = np.pi * (1 + 5 ** 0.5) * i
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)
    W = R2 - R1
    # dense coverage INCLUDING the inner-edge band (the first version had
    # a hole at r in (0.6R1, R1+0.3W) and the optimiser hid a DEC spike
    # at r=10.12 in it — see CHECKPOINT Track P log; arbiter caught it)
    rad = list(np.linspace(0.25 * R1, 1.35 * R2, 22))
    rad += [R1 + f * W for f in (0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.65,
                                 0.8, 0.9, 0.97)]
    rad = sorted(set(round(float(r), 6) for r in rad if r > 0.5))
    return np.concatenate([dirs * r for r in rad])


def arbiter_points(R1, R2, ndir=26, seed=999):
    rng = np.random.default_rng(seed)
    i = np.arange(ndir)
    phi = np.arccos(1 - 2 * (i + 0.5) / ndir)
    th = np.pi * (1 + 5 ** 0.5) * i + rng.uniform(0, 0.3)
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)
    W = R2 - R1
    rad = np.linspace(0.25 * R1, 1.35 * R2, 30) + rng.uniform(-0.15, 0.15, 30)
    rad = np.sort(np.concatenate(
        [rad, [R1 + f * W for f in (0.02, 0.05, 0.1, 0.2, 0.35, 0.5, 0.65,
                                    0.8, 0.9, 0.97)]]))
    return np.concatenate([dirs * r for r in rad if r > 0.5])


def set_genes(x):
    FREE['theta_d'] = np.asarray(x[:NDK])
    FREE['svals'] = np.asarray(x[NDK:NDK + NSK])


def genes_from_named(R1, R2):
    """Gene vector approximating the best named beta=0.05 design:
    edgepeaked wd=0.2W floor=0.10 density, cos shift, s_rho=0.2W, s_P=0.116W."""
    W = R2 - R1
    kr = np.linspace(R1, R2, NDK)
    w = sh.weight(kr, R1, R2, 'edgepeaked', {'wd': 0.2 * W, 'floor': 0.10})
    theta = np.log(np.maximum(w, 1e-3))
    ks = np.linspace(R1, R2, NSK + 2)[1:-1]
    sv = 0.5 * (1 + np.cos(np.pi * (ks - R1) / W))
    return np.concatenate([theta, sv, [0.2 * W, 0.116 * W]])


def run(beta, M, R1=10.0, R2=20.0, maxiter=25, seed=1, tag=''):
    FREE['R1'], FREE['R2'] = R1, R2
    pts = screen_points(R1, R2)
    W = R2 - R1
    n_evals = [0]
    t0 = time.time()

    def objective(x):
        set_genes(x)
        n_evals[0] += 1
        try:
            r = tl.eval_shell(R1, R2, M, 'free', {}, float(x[-2]), float(x[-1]),
                              beta, 'free', None, h=0.03 * R1, pts=pts)
            return -r['worst']
        except Exception:
            return 1.0

    bounds = ([(-3.0, 2.0)] * NDK + [(0.0, 1.0)] * NSK
              + [(0.05 * W, 0.4 * W), (0.03 * W, 0.3 * W)])
    x0 = genes_from_named(R1, R2)
    pop = np.tile(x0, (8 * len(bounds), 1))
    rng = np.random.default_rng(seed)
    pop[1:] += rng.normal(0, 0.35, pop[1:].shape)
    pop = np.clip(pop, [b[0] for b in bounds], [b[1] for b in bounds])
    res = differential_evolution(objective, bounds, seed=seed, popsize=8,
                                 maxiter=maxiter, tol=0, mutation=(0.3, 1.2),
                                 recombination=0.8, init=pop, polish=False,
                                 updating='immediate')
    set_genes(res.x)
    scr = tl.eval_shell(R1, R2, M, 'free', {}, float(res.x[-2]),
                        float(res.x[-1]), beta, 'free', None, h=0.03 * R1,
                        pts=pts)
    out = {'beta': beta, 'M_geom': M, 'R1': R1, 'R2': R2,
           'genes': res.x.tolist(), 'n_evals': n_evals[0],
           'screen_worst': scr['worst'], 'screen_kind': scr['worst_kind'],
           'arbiter': []}
    for sd in (999, 31337):
        ap = arbiter_points(R1, R2, seed=sd)
        for h in (0.03 * R1, 0.015 * R1):
            r = tl.eval_shell(R1, R2, M, 'free', {}, float(res.x[-2]),
                              float(res.x[-1]), beta, 'free', None, h=h, pts=ap)
            out['arbiter'].append({'seed': sd, 'h': h, 'worst': r['worst'],
                                   'worst_kind': r['worst_kind'],
                                   'worst_radius': r['worst_radius'],
                                   'nec': r['nec'],
                                   'typeI': r['typeI_frac_sig']})
            print(f"  arbiter seed={sd} h={h}: worst={r['worst']:+.4e} "
                  f"({r['worst_kind']} @r={r['worst_radius']:.2f}) "
                  f"tI={r['typeI_frac_sig']:.3f}", flush=True)
    out['elapsed_s'] = time.time() - t0
    path = f"results/trackP_b{beta}_M{M}{tag}.json"
    json.dump(out, open(path, 'w'), indent=1)
    print(f"TrackP beta={beta} M={M}: screen worst={scr['worst']:+.4e}, "
          f"{n_evals[0]} evals, {out['elapsed_s']:.0f}s -> {path}", flush=True)
    return out


def audit_full(R1, R2, M, beta, x, pts, h):
    """Full per-point audit of a gene vector; returns margins dict."""
    import verify_metric as vm
    import shell as sh
    set_genes(x)
    prof = sh.build_shell(R1, R2, M, kind='free', params={}, s_rho=float(x[-2]),
                          s_P=float(x[-1]), Nr=3001)
    gfunc = sh.shell_point_factory(prof, beta, 'free', 1.0, None)
    G, That, m = vm.einstein_at_points(gfunc, pts, h=h)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / R1) ** 2, 1e-3 * abs(rho_peak))
    m = dict(m)
    m['sig'] = scale > thr
    m['scale'] = scale
    return m


def run_adversarial(beta, M, R1=10.0, R2=20.0, rounds=3, maxiter=15,
                    seed=1, tag='adv'):
    """DE with an adversarially growing training set: every arbiter
    pocket found is added to the objective's sample. Final verdict on
    two fresh seeds the optimiser never saw."""
    FREE['R1'], FREE['R2'] = R1, R2
    W = R2 - R1
    train_pts = screen_points(R1, R2, ndir=18)
    bounds = ([(-3.0, 2.0)] * NDK + [(0.0, 1.0)] * NSK
              + [(0.05 * W, 0.4 * W), (0.03 * W, 0.3 * W)])
    x_best = genes_from_named(R1, R2)
    log = {'beta': beta, 'M_geom': M, 'R1': R1, 'R2': R2, 'rounds': []}
    t0 = time.time()
    n_evals = [0]

    def make_obj(pts):
        def objective(x):
            n_evals[0] += 1
            set_genes(x)
            try:
                r = tl.eval_shell(R1, R2, M, 'free', {}, float(x[-2]),
                                  float(x[-1]), beta, 'free', None,
                                  h=0.03 * R1, pts=pts)
                return -r['worst']
            except Exception:
                return 1.0
        return objective

    for rd in range(rounds):
        rng = np.random.default_rng(seed + rd)
        pop = np.tile(x_best, (6 * len(bounds), 1))
        pop[1:] += rng.normal(0, 0.3 if rd == 0 else 0.15, pop[1:].shape)
        pop = np.clip(pop, [b[0] for b in bounds], [b[1] for b in bounds])
        res = differential_evolution(make_obj(train_pts), bounds, seed=seed + rd,
                                     popsize=6, maxiter=maxiter, tol=0,
                                     mutation=(0.3, 1.2), recombination=0.8,
                                     init=pop, polish=False, updating='immediate')
        x_best = res.x
        # arbiter audit on a fresh seed; harvest failing points
        sd = 999 + 7919 * rd
        ap = arbiter_points(R1, R2, seed=sd)
        m = audit_full(R1, R2, M, beta, x_best, ap, 0.03 * R1)
        worst_all = min(float(np.min(m[k][m['sig']])) for k in ('nec', 'wec', 'sec', 'dec'))
        bad = np.zeros(len(ap), dtype=bool)
        for k in ('nec', 'wec', 'sec', 'dec'):
            bad |= m['sig'] & (m[k] < 2e-6)
        bad |= m['sig'] & (~m['typeI'])
        n_bad = int(np.sum(bad))
        entry = {'round': rd, 'train_pts': int(len(train_pts)),
                 'screen_obj': float(-res.fun), 'arbiter_seed': sd,
                 'arbiter_worst': worst_all, 'n_bad_points': n_bad,
                 'elapsed_s': time.time() - t0}
        log['rounds'].append(entry)
        print(f"  ADV rd{rd}: train={len(train_pts)} pts, obj={-res.fun:+.3e}, "
              f"arbiter worst={worst_all:+.3e}, bad pts={n_bad} "
              f"[{entry['elapsed_s']:.0f}s]", flush=True)
        if n_bad == 0 and worst_all > 0:
            break
        add = ap[bad]
        if len(add) > 400:
            add = add[rng.choice(len(add), 400, replace=False)]
        train_pts = np.concatenate([train_pts, add])
    # final verdict: two fresh seeds, h and h/2
    log['genes'] = x_best.tolist()
    log['final'] = []
    for sd in (555001, 777001):
        ap = arbiter_points(R1, R2, seed=sd)
        for h in (0.03 * R1, 0.015 * R1):
            m = audit_full(R1, R2, M, beta, x_best, ap, h)
            w = min(float(np.min(m[k][m['sig']])) for k in ('nec', 'wec', 'sec', 'dec'))
            tI = float(np.mean(m['typeI'][m['sig']]))
            log['final'].append({'seed': sd, 'h': h, 'worst': w, 'typeI': tI})
            print(f"  FINAL seed={sd} h={h}: worst={w:+.4e} tI={tI:.3f}", flush=True)
    log['n_evals'] = n_evals[0]
    log['elapsed_s'] = time.time() - t0
    path = f"results/trackP_b{beta}_M{M}_{tag}.json"
    json.dump(log, open(path, 'w'), indent=1)
    print(f"TrackP-ADV beta={beta} M={M}: {n_evals[0]} evals -> {path}", flush=True)
    return log


if __name__ == '__main__':
    beta = float(sys.argv[1]); M = float(sys.argv[2])
    mi = int(sys.argv[3]) if len(sys.argv) > 3 else 25
    if len(sys.argv) > 4 and sys.argv[4] == 'adv':
        R1 = float(sys.argv[5]) if len(sys.argv) > 5 else 10.0
        R2 = float(sys.argv[6]) if len(sys.argv) > 6 else 20.0
        run_adversarial(beta, M, R1=R1, R2=R2, maxiter=mi)
    else:
        run(beta, M, maxiter=mi)
