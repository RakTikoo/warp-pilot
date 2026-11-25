"""
p803_inner.py — P80-3 stage 1b: inner shell alone (same protocol as
p803_alone.py, inner shell only; outer b0.08 was abandoned after the
b0.07 full-volume failure showed the alone ceiling at 0.06 — the
b0.08 polish was killed mid-run, its record carries no x).
Writes into the same state/out JSONs. float64, venv python.
"""
import json, os, sys, time
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase80')
import p803_lib as P
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
from p413_audit import audit_points

RES = '/home/hatch/workspace/warp-pilot/phase80/results'
STATE = RES + '/p803_alone_state.json'
OUT = RES + '/p803_alone.json'
BETAS = [0.05, 0.06, 0.07, 0.08]


def load(path, default):
    if os.path.exists(path):
        try:
            return json.load(open(path))
        except Exception:
            pass
    return default


def save(obj, path):
    json.dump(obj, open(path, 'w'), indent=1)


def main():
    t0 = time.time()
    state = load(STATE, {'shells': {}})
    out = load(OUT, {'item': 'P80-3 stage1 alone', 'float': 'float64'})
    prof = P.frontier_inner()
    name = 'inner'
    sh_state = state['shells'].setdefault(name, {})
    bnds = P.bounds_for(prof)
    x_prev = None
    # continuation seed: outer-independent; use b0.05 chain order
    for beta in BETAS:
        key = f'b{beta}'
        if key in sh_state and 'audit' in sh_state[key]:
            x_prev = np.array(sh_state[key]['x'])
            continue
        rec = sh_state.setdefault(key, {})
        x0 = P.zero_start(prof) if x_prev is None else x_prev.copy()
        gf0 = P.alone_gfunc(prof, beta, x0)
        pts_scr, _ = P.screen_points(prof['R2'])
        sc0, info0 = P.screen_score(gf0, pts_scr)
        rec['start_score'] = sc0
        rec['start_info'] = info0
        rec['start_x'] = [float(v) for v in x0]
        save(state, STATE)
        print(f'{name} {key} start score {sc0:+.3e} ({time.time()-t0:.0f}s)', flush=True)
        if 'x' not in rec:
            pts_full0, _ = audit_points(prof['R2'], seed=11)
            rr0 = np.sqrt(np.sum(pts_full0 ** 2, axis=1))
            core = pts_full0[(rr0 >= prof['R1'] - 0.75) & (rr0 <= prof['R2'])]
            obj = P.FastAloneObjective(prof, beta, core)
            rec['obj_npts'] = int(len(core))
            rec['fast_start_score'] = float(obj(x0))
            nfev = [0]
            EPS = 2e-3

            def neg(x):
                nfev[0] += 1
                return -obj(x)

            def neg_jac(x):
                g = np.empty_like(x)
                f0 = obj(x)
                for j in range(len(x)):
                    xp = x.copy()
                    xp[j] = min(x[j] + EPS, bnds[j][1])
                    if xp[j] > x[j]:
                        g[j] = -(obj(xp) - f0) / (xp[j] - x[j])
                    else:
                        xm = x.copy()
                        xm[j] = max(x[j] - EPS, bnds[j][0])
                        g[j] = -(f0 - obj(xm)) / (x[j] - xm[j])
                return g

            res = minimize(neg, x0, method='L-BFGS-B', bounds=bnds,
                           jac=neg_jac,
                           options={'maxiter': 100, 'maxfun': 3000,
                                    'ftol': 1e-13, 'gtol': 1e-10})
            rec['x'] = [float(v) for v in res.x]
            rec['polish_score'] = float(-res.fun)
            rec['nfev'] = int(nfev[0])
            rec['nit'] = int(res.nit)
            rec['success'] = bool(res.success)
            save(state, STATE)
            print(f'{name} {key} polish score {rec["polish_score"]:+.3e} '
                  f'nfev={nfev[0]} ({time.time()-t0:.0f}s)', flush=True)
        x = np.array(rec['x'])
        gf = P.alone_gfunc(prof, beta, x)
        pts_full, _ = audit_points(prof['R2'], seed=11)
        R1p, R2p = prof['R1'], prof['R2']

        def reg_alone(r, R1p=R1p, R2p=R2p):
            return ('payload' if r < R1p else
                    'inner_wall' if r <= R2p else 'exterior')
        rec['audit'] = {}
        for h in (0.3, 0.15, 0.075):
            rec['audit'][str(h)] = P.summarise_gs(gf, pts_full, h,
                                                  region_fn=reg_alone)
        rec['chain'] = {k: gf.chain[k] for k in
                        ('lam', 'k', 'S_lo_minus1', 'S_hi', 'balance_rel',
                         'monotone_violation')}
        save(state, STATE)
        a15 = rec['audit']['0.15']
        print(f'{name} {key} AUDIT h0.15 worst={a15["worst"]:+.3e} '
              f'typeI={a15["typeI_frac_sig"]} sn={a15["min_sampled_nec_all_sig"]:+.3e} '
              f'({time.time()-t0:.0f}s)', flush=True)
        x_prev = x
    out['alone'] = state['shells']
    save(out, OUT)
    print(f'DONE {time.time()-t0:.0f}s', flush=True)


if __name__ == '__main__':
    main()
