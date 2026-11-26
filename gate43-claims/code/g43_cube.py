#!/usr/bin/env python3
"""Gate-43 cube (part 2): the gate's own G1 cube,
mu in {0.90, 0.95, 1.00, 1.05, 1.10}^3, one SET-244
read per triple, flushed per read to
gate43/results/g43_cube.jsonl; then the gate's own
quadratic fit over its non-saturated points, the
mu_M identity check, the saturated-corner check and
axis finite differences. Output:
gate43/results/g43_fit.json."""
import json
import os
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate43/work')
import g43_lib as G  # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/gate43/results'
GRID = [0.90, 0.95, 1.00, 1.05, 1.10]
SAT = -0.5     # DEC-pinning criterion: dec_min below this
STORED_SAT = sorted([
    (1.0, 0.9, 0.9), (1.05, 0.9, 0.9), (1.05, 0.9, 0.95),
    (1.05, 0.95, 0.9), (1.1, 0.9, 0.9), (1.1, 0.9, 0.95),
    (1.1, 0.9, 1.0), (1.1, 0.95, 0.9), (1.1, 0.95, 0.95)])
STORED_FIT = {
    'grad': [-0.00010955057573860948, 0.00011146963771141866,
             8.211005563920505e-05],
    'hessian_eigenvalues': [-0.0033301983243515187,
                            -0.0008377994225485973,
                            -6.0639495375965976e-05],
    'max_abs_resid': 2.092730871046218e-05, 'n_points': 116}
STORED_AXES_H05 = {'muS': -0.0001493824291340853,
                   'muN': 0.00015377712657000672,
                   'muM': -3.491179995458802e-05}


def main():
    path = f'{RES}/g43_cube.jsonl'
    done = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    done[tuple(r['triple'])] = r
    with open(path, 'a') as f:
        for a in GRID:
            for b in GRID:
                for c in GRID:
                    t = (a, b, c)
                    if t in done:
                        continue
                    s, _ = G.set_read(a, b, c)
                    r = {'triple': list(t),
                         'nec_min': s['nec']['min'],
                         'dec_min': s['dec']['min'],
                         'rho_min': s['rho']['min'],
                         'joint': float(min(s['nec']['min'],
                                            s['dec']['min'])),
                         'nec_argmin_r': s['nec_argmin_r'],
                         'dec_argmin_r': s['dec_argmin_r'],
                         'typeI_count': s['typeI_count']}
                    f.write(json.dumps(r) + '\n')
                    f.flush()
                    done[t] = r
                    print('CUBE', t, r['joint'], flush=True)
    # ---- saturated corner (gate's own criterion)
    sat = sorted([t for t, r in done.items()
                  if r['dec_min'] < SAT])
    corner = {'gate_saturated_triples': [list(t) for t in sat],
              'matches_stored_9': bool(sat == STORED_SAT),
              'dec_min_range': [
                  float(min(done[t]['dec_min'] for t in sat)),
                  float(max(done[t]['dec_min'] for t in sat))],
              'dec_argmin_r_values': sorted(
                  {done[t]['dec_argmin_r'] for t in sat})}
    print('CORNER', corner, flush=True)
    # ---- mu_M identity from the gate's own rows
    ident = {}
    for mu in (0.95, 1.05, 1.10):
        r1 = done[(1.0, 1.0, mu)]
        r2 = done[(mu, mu, mu)]
        ident[str(mu)] = {
            'joint_diff': abs(r1['joint'] - r2['joint']),
            'nec_diff': abs(r1['nec_min'] - r2['nec_min']),
            'dec_diff': abs(r1['dec_min'] - r2['dec_min']),
            'nec_argmin_r_same': bool(
                r1['nec_argmin_r'] == r2['nec_argmin_r']),
            'dec_argmin_r_same': bool(
                r1['dec_argmin_r'] == r2['dec_argmin_r'])}
    print('IDENTITY', ident, flush=True)
    # ---- axis FDs at h = 0.05 (cross-check)
    axes = {}
    for i, nm in enumerate(('muS', 'muN', 'muM')):
        tp = [1.0, 1.0, 1.0]
        tm = [1.0, 1.0, 1.0]
        tp[i] = 1.05
        tm[i] = 0.95
        axes[nm] = float((done[tuple(tp)]['joint']
                          - done[tuple(tm)]['joint']) / 0.10)
    # ---- quadratic fit over non-saturated points
    pts = []
    val = []
    for t, r in done.items():
        if r['dec_min'] < SAT:
            continue
        x = np.array(t) - 1.0
        pts.append(x)
        val.append(r['joint'])
    X = np.array(pts)
    y = np.array(val)

    def design(X):
        x, yy, z = X[:, 0], X[:, 1], X[:, 2]
        return np.column_stack([
            np.ones(len(X)), x, yy, z, x * x, x * yy, x * z,
            yy * yy, yy * z, z * z])
    A = design(X)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    H = np.array([[2 * coef[4], coef[5], coef[6]],
                  [coef[5], 2 * coef[7], coef[8]],
                  [coef[6], coef[8], 2 * coef[9]]])
    eig = np.linalg.eigvalsh(H)[::-1]
    fit = {'n_points': int(len(y)),
           'grad_at_centre': coef[1:4].tolist(),
           'hessian': H.tolist(),
           'hessian_eigenvalues': eig.tolist(),
           'max_abs_resid': float(np.max(np.abs(resid))),
           'grad_diff_vs_stored': (
               np.array(coef[1:4]) - np.array(STORED_FIT['grad'])
               ).tolist(),
           'stored': STORED_FIT}
    out = {'corner': corner, 'identity': ident,
           'axes_fd_h05': axes,
           'axes_fd_h05_stored': STORED_AXES_H05, 'fit': fit}
    with open(f'{RES}/g43_fit.json', 'w') as f:
        json.dump(out, f, indent=1)
    print('FIT', json.dumps(fit), flush=True)
    print('CUBE DONE', flush=True)


if __name__ == '__main__':
    main()
