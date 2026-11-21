"""
n3_de.py — conditions-first DE over prescribed eigenvalue fields.

Genes (22): 10 log-rho knots + 10 tau knots (tau = p_t*/rho*, bounded
[-0.95, 0.95] so the PRESCRIPTION satisfies DEC/NEC margins wherever
it is realised) + s_rho (density smoothing) + w_t (extra tail
window position for p_t* — the Pattern-P8 lever: in the forward
construction the tail pressure was slaved and outlived the density;
here it is prescribed down independently).
Per evaluation: rho* normalised to mass M exactly -> p_t* built ->
p_r solved by conservation (n3_invert) -> metric recovered -> the
MOVING tensor judged by the standard point auditor on a random
screen (the prescription never grades itself). Shooting failure
(no-sign-change with a large gap) is costed as unrealisable.

Usage: python3 n3_de.py BETA M R1 R2 [maxiter]
Finals: re-solve at Nr=4001, fresh-seed audits at h=0.3/0.15, and
audits of the recovered base at the other target velocities
{0.05, 0.1, 0.5, 1.1, 1.5, 2.0} (S7 / N3 spec).
"""
import json, sys, time
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import differential_evolution

import shell as sh
import verify_metric as vm
import n3_invert as n3

DTYPE = np.float64
BETA = float(sys.argv[1]); M_T = float(sys.argv[2])
R1 = float(sys.argv[3]); R2 = float(sys.argv[4])
MAXITER = int(sys.argv[5]) if len(sys.argv) > 5 else 30
RKNOTS = np.array([0.0, 0.13, 0.23, 0.31, 0.41, 0.53, 0.65, 0.77, 0.87, 1.0]) * (R2 + 14.0)
RMAX = R2 + 30.0
N_GENES = 23


def prescription(genes):
    logw = genes[:10]; tau_k = genes[10:20]
    s_rho = genes[20]; w_t = genes[21]
    pch = PchipInterpolator(RKNOTS, logw)
    tau_p = PchipInterpolator(RKNOTS, tau_k)
    lam_tail = genes[22] if len(genes) > 22 else 5.0
    def win(r):
        r = np.asarray(r, dtype=DTYPE)
        return np.where(r <= R2 + 2.0, 1.0,
                        np.exp(-(r - (R2 + 2.0)) / lam_tail))
    wt = lambda r: 1.0 - sh.smootherstep(
        (np.asarray(r, dtype=DTYPE) - w_t) / 4.0)

    def rho_star(r):
        r = np.asarray(r, dtype=DTYPE)
        rr = np.linspace(0.0, RMAX, 1201)
        w = np.exp(pch(rr)) * win(rr)
        if s_rho > 0.05:
            w = sh.gauss_smooth(w, rr[1] - rr[0], s_rho)
            w = np.maximum(w, 0.0)
        norm = sh.cumint(4 * np.pi * rr ** 2 * w, rr)[-1]
        rho_full = M_T * w / max(norm, 1e-300)
        return np.interp(r, rr, rho_full)

    def pt_star(r):
        r = np.asarray(r, dtype=DTYPE)
        return tau_p(np.clip(r, 0, RKNOTS[-1])) * rho_star(r) * wt(r)

    return rho_star, pt_star


def screen_points(seed, n=420):
    rng = np.random.default_rng(seed)
    u = rng.random(n)
    rad = (R2 + 28.0) * np.cbrt(u)
    shell_boost = rng.random(n) < 0.45
    rad[shell_boost] = rng.uniform(R1 - 3.0, R2 + 9.0,
                                   int(shell_boost.sum()))
    # RUN 3 FIX: dedicated tail coverage — run 2's screen hole
    # (knots ended at R2+8, support at R2+14, screens thin past
    # R2+10) hid a -1e-3 NEC pocket in the support tail.
    tail_boost = rng.random(n) < 0.20
    rad[tail_boost] = rng.uniform(R2 + 2.0, R2 + 28.0,
                                  int(tail_boost.sum()))
    d = rng.normal(size=(n, 3)); d /= np.linalg.norm(d, axis=1)[:, None]
    return (rad[:, None] * d).astype(DTYPE)


def audit_worst(prof, beta, pts, h=0.3):
    gf = n3.prof_gfunc(prof, beta, R1, R2)
    _, That, m = vm.einstein_at_points(gf, pts, h=h)
    worst = np.minimum(np.minimum(m['nec'], m['wec']),
                       np.minimum(m['sec'], m['dec']))
    return float(np.min(worst)), float(np.mean(m['typeI']))


_PTS = screen_points(4242)
_G = {'evals': 0}


def _obj(genes):
    _G['evals'] += 1
    try:
        rho_s, pt_s = prescription(genes)
        prof = n3.solve_shell(rho_s, pt_s, R1=R1, R2=R2, Nr=1201,
                              rmax=RMAX, rout=RMAX)
    except Exception:
        return 1.0
    scale = max(float(np.max(prof['rho_star'])), 1e-12)
    w, _ = audit_worst(prof, BETA, _PTS, h=0.3)
    # RUN 2: realisability penalty REMOVED. Run 1 diagnosis: the
    # seed prescription's shooting residual (the forward profiles
    # are not exact conservation solutions) priced the seed out
    # of the population despite its -5.8e-7 raw margin, and the
    # DE optimised the penalty instead of the margin. The
    # recovered metric is judged by its own audit; realisability
    # is reported, not priced.
    return -w + 0.0 * min(abs(prof['shoot_F']) / scale, 0.25)


def seed_genes():
    """Forward construction's realised prescription at this (R1,R2,M)
    as one init row: the DE starts AT the known forward boundary."""
    base = sh.build_shell(R1, R2, M_T, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    r = base['r']
    rho = base['rho_ex']
    w = rho / max(np.max(rho), 1e-300)
    logw = np.log(np.maximum(w, 1e-5))
    from scipy.interpolate import CubicSpline
    lw = CubicSpline(r, logw)
    tau = np.where(rho > 3e-3 * np.max(rho),
                   base['p_t'] / np.maximum(rho, 1e-300), 0.0)
    tau = np.clip(tau, -0.95, 0.95)
    tp = CubicSpline(r, tau)
    g = np.zeros(N_GENES)
    g[:10] = lw(RKNOTS)
    g[10:20] = tp(RKNOTS)
    g[20] = 0.0            # rho* already carries the smoothing
    g[21] = R2 + 8.0       # no extra p_t tail window
    if N_GENES > 22:
        g[22] = 5.0        # soft-tail decay length seed
    return g


BOUNDS = [(-7.0, 0.0)] * 10 + [(-0.95, 0.95)] * 10 \
    + [(0.0, 3.0), (R1, R2 + 8.0), (2.0, 10.0)]


def main():
    t0 = time.time()
    print(f'N3 DE: beta={BETA} M={M_T} ({R1:g},{R2:g}) '
          f'screen={len(_PTS)} pts', flush=True)
    g_seed = seed_genes()
    # pipeline cross-check: seed row must reproduce the forward audit
    w0, tI0 = 0.0, 0.0
    try:
        rho_s, pt_s = prescription(g_seed)
        prof0 = n3.solve_shell(rho_s, pt_s, R1=R1, R2=R2, Nr=2001,
                               rmax=RMAX, rout=RMAX)
        w0, tI0 = audit_worst(prof0, BETA, _PTS, h=0.3)
        print(f'seed (forward prescription): worst {w0:+.4e} '
              f'TypeI {tI0:.3f} shoot={prof0["shoot"]}', flush=True)
    except Exception as e:
        print('seed eval failed:', e, flush=True)
    rng = np.random.default_rng(11)
    pop = 5 * N_GENES
    init = np.tile(g_seed, (pop, 1)).astype(DTYPE)
    init += rng.normal(0, 0.25, init.shape)
    init[:, 10:20] += rng.normal(0, 0.10, (pop, 10))
    lo = np.array([b[0] for b in BOUNDS]); hi = np.array([b[1] for b in BOUNDS])
    init = np.clip(init, lo, hi)
    init[0] = g_seed
    res = differential_evolution(_obj, BOUNDS, maxiter=MAXITER, popsize=5,
                                 mutation=(0.3, 1.2), recombination=0.8,
                                 init=init, polish=False, seed=20261123)
    genes = res.x
    out = {'beta': BETA, 'M': M_T, 'R1': R1, 'R2': R2,
           'screen_worst': float(-res.fun), 'seed_worst': w0,
           'genes': genes.tolist(), 'n_evals': _G['evals'],
           'elapsed_s': time.time() - t0}
    print(f'DE done: screen worst {-res.fun:+.4e} evals {_G["evals"]} '
          f'{out["elapsed_s"]:.0f}s', flush=True)
    # finals: Nr=4001 re-solve, fresh seeds, both resolutions
    rho_s, pt_s = prescription(genes)
    prof = n3.solve_shell(rho_s, pt_s, R1=R1, R2=R2, Nr=4001,
                          rmax=RMAX, rout=RMAX)
    out['shoot'] = prof['shoot']; out['shoot_F'] = prof['shoot_F']
    out['realisation'] = n3.realisation_residual(prof)
    out['M_recovered'] = prof['M']; out['umin'] = prof['umin']
    for seed in (555001, 777001):
        pts = screen_points(seed, n=700)
        for h in (0.3, 0.15):
            w, tI = audit_worst(prof, BETA, pts, h=h)
            out[f'final_seed{seed}_h{h}'] = {'worst': w, 'typeI': tI}
            print(f'  final seed={seed} h={h}: worst {w:+.4e} '
                  f'TypeI {tI:.3f}', flush=True)
    # velocity sweep of the recovered base (N3 spec targets + S7)
    for vb in (0.05, 0.1, 0.5, 1.1, 1.5, 2.0):
        if abs(vb - BETA) < 1e-12:
            continue
        pts = screen_points(777001, n=700)
        w, tI = audit_worst(prof, vb, pts, h=0.3)
        out[f'sweep_beta{vb}'] = {'worst': w, 'typeI': tI}
        print(f'  sweep beta={vb}: worst {w:+.4e} TypeI {tI:.3f}',
              flush=True)
    tag = f'n3_b{BETA}_M{M_T}_{int(R1)}-{int(R2)}_run4'
    json.dump(out, open(f'results/{tag}.json', 'w'), indent=1, default=float)
    np.save(f'results/{tag}_genes.npy', genes)
    print('N3 DE DONE', flush=True)


if __name__ == '__main__':
    main()
