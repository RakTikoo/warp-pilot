"""
wc_crosscheck.py — W-C anatomy + resolution of the G7-3 machinery
cross-check quantity. The minimum null contraction at the site point is
min over unit n of f(n) = T00 + 2 s.n + n^T P n in the Eulerian frame
(That). f varies on the scale of |T| ~ 1e-4 while its minimum is ~1e-7,
so Fibonacci sampling under-resolves it (P50-1's 20,000-dir sample gave
-1.245e-07; a 5,002-dir sample gives -3.4e-08 at the same h and tensor).
Here the minimum is computed by dense sampling (50,000 dirs) FOLLOWED by
exact local optimisation on the sphere (scipy SLSQP, |n|=1 constraint,
multi-start from the 8 best sampled directions), cross-validated by an
independent Lagrange-multiplier solve: stationary points satisfy
(P - lam I) n = -s with |n| = 1; all real roots lam of the secular
equation are found by scanning + bisection and the global min taken.
float64. Programme venv.
"""
import json, sys
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate7')
import wc_recon as rc
import wc_auditor as au

OUT = '/home/hatch/workspace/warp-pilot/gate7/results/wc_g73_numbers.json'
res = json.load(open(OUT))
x = rc.load_design_vector(rc.DESIGN_PATHS[1])
shell = rc.ProcacciaShellWC(x)
pt = np.array([[0.0, 16.635, 0.0]])


def min_null_exact(That):
    T = That
    T00 = T[0, 0]; s = T[0, 1:]; P = T[1:, 1:]

    def f(n):
        return T00 + 2.0 * s @ n + n @ P @ n

    dirs = au.fib_dirs(50000)
    vals = T00 + 2.0 * (dirs @ s) + np.einsum('ij,jk,ik->i', dirs, P, dirs)
    order = np.argsort(vals)
    best = (float(vals[order[0]]), dirs[order[0]])
    # local optimisation from the 8 best sampled directions
    for j in order[:8]:
        r = minimize(lambda n: f(n), dirs[j], method='SLSQP',
                     constraints={'type': 'eq', 'fun': lambda n: n @ n - 1.0},
                     options={'maxiter': 500, 'ftol': 1e-18})
        n = r.x / np.linalg.norm(r.x)
        v = float(f(n))
        if v < best[0]:
            best = (v, n)
    # independent Lagrange/secular cross-validation:
    # stationary: (P - lam I) n = -s, |n|=1. Scan lam, solve, keep |n|=1 roots.
    w, V = np.linalg.eigh(P)
    sh = V.T @ s
    lam_grid = np.concatenate([
        np.linspace(w.min() - 5.0, w.max() + 5.0, 20001),
        w + np.array([-1e-9, 1e-9])[:, None].ravel() if False else []])
    def n_of_lam(lam):
        d = w - lam
        if np.min(np.abs(d)) < 1e-14:
            return None
        c = -sh / d
        return V @ c
    prev = None
    roots = []
    for lam in lam_grid:
        n = n_of_lam(lam)
        if n is None:
            continue
        g = np.linalg.norm(n) - 1.0
        if prev is not None and prev[1] * g < 0:
            lo, hi = prev[0], lam
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                nm = n_of_lam(mid)
                if nm is None:
                    break
                gm = np.linalg.norm(nm) - 1.0
                if prev[1] * gm <= 0:
                    hi = mid
                else:
                    lo = mid
            nroot = n_of_lam(0.5 * (lo + hi))
            if nroot is not None:
                roots.append(nroot / np.linalg.norm(nroot))
        prev = (lam, g)
    lag_best = None
    for n in roots:
        v = float(f(n))
        if lag_best is None or v < lag_best[0]:
            lag_best = (v, n)
    return best, lag_best


out = {}
for beta in (0.1363, 0.1364):
    gf = shell.metric_factory(beta)
    for h in (0.0375, 0.01875, 0.009375, 0.0046875, 0.00234375):
        G, g = au.einstein2(gf, pt, h)
        That = au.eulerian_that(g, G / au.EIGHT_PI)
        m = au.margins_from_that(That)
        (v_opt, n_opt), lag = min_null_exact(That[0])
        out[f'b{beta}_h{h}'] = {
            'typeI': bool(m['typeI'][0]),
            'min_null_exact_opt': v_opt, 'dir_opt': [float(q) for q in n_opt],
            'min_null_lagrange': (float(lag[0]) if lag else None),
            'min_null_fib50002': float(au.null_min(That, au.fib_dirs(50002))[0]),
            'min_null_fib20000': float(au.null_min(That, au.fib_dirs(20000))[0]),
            'min_null_fib5002': float(au.null_min(That, au.fib_dirs(5002))[0]),
        }
        print(f"b={beta} h={h} typeI={out[f'b{beta}_h{h}']['typeI']} "
              f"exact={v_opt:+.6e} lagrange={out[f'b{beta}_h{h}']['min_null_lagrange']} "
              f"fib50002={out[f'b{beta}_h{h}']['min_null_fib50002']:+.4e} "
              f"fib20000={out[f'b{beta}_h{h}']['min_null_fib20000']:+.4e}", flush=True)
    G4, g4 = au.einstein4(gf, pt, 0.00234375)
    That4 = au.eulerian_that(g4, G4 / au.EIGHT_PI)
    (v4, n4), lag4 = min_null_exact(That4[0])
    out[f'b{beta}_order4_h0.00234375'] = {
        'min_null_exact_opt': v4, 'dir_opt': [float(q) for q in n4],
        'min_null_lagrange': (float(lag4[0]) if lag4 else None)}
    print(f"b={beta} order4 finest exact={v4:+.6e} lagrange={out[f'b{beta}_order4_h0.00234375']['min_null_lagrange']}", flush=True)

res['step3_crosscheck_exact_minnull'] = out
his = -1.30135e-07
v = out['b0.1364_h0.00234375']['min_null_exact_opt']
res['step3_crosscheck']['exact_opt_finest_h'] = v
res['step3_crosscheck']['rel_dev_from_his'] = abs(abs(v) - abs(his)) / abs(his)
res['step3_crosscheck']['within_25pct'] = bool(abs(abs(v) - abs(his)) / abs(his) <= 0.25)
json.dump(res, open(OUT, 'w'), indent=1, default=float)
print('CROSSCHECK exact finest', v, 'rel dev', res['step3_crosscheck']['rel_dev_from_his'],
      'within25 =', res['step3_crosscheck']['within_25pct'], flush=True)
print('DONE', flush=True)
