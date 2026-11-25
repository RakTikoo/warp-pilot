"""
p803_alone.py — P80-3 stage 1: anchors + ALONE source-modulated shells.
For each frontier shell (outer, inner): zero-start screening scores at
beta_alone in {0.05,0.06,0.07,0.08}, then L-BFGS-B polishes
(continuation in beta) maximising the screening score. Every polish
checkpointed to results/p803_alone_state.json on completion.
Full gate-standard alone audits (h=0.3/0.15, full audit_points set)
for the polished vector at each beta -> results/p803_alone.json.
float64, venv python.
"""
import json, os, sys, time
import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase80')
import p803_lib as P
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase41')
import wa_auditor as wa
import shell as sh
from p413_audit import audit_points

RES = '/home/hatch/workspace/warp-pilot/phase80/results'
os.makedirs(RES, exist_ok=True)
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

    # ---- anchors (once) ----
    if 'anchors' not in out:
        def flat(pts):
            pts = np.asarray(pts, dtype=float)
            g = np.zeros((len(pts), 4, 4)); g[:, 0, 0] = -1.0
            for i in range(1, 4):
                g[:, i, i] = 1.0
            return g
        rng = np.random.default_rng(7)
        fpts = rng.normal(size=(60, 3)) * 6.0
        G, _ = wa.einstein_at(flat, fpts, 0.3)
        # Finalist-A anchor (Gate-6 pattern, stored digits +2.141e-07)
        profA = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                               params={'wd': 3.0, 'floor': 0.2},
                               s_rho=2.0, s_P=1.16, Nr=4001)
        gfA = sh.shell_point_factory(profA, 0.0, 'cos', 1.0, [10.0, 20.0])
        ptsA, _ = audit_points(20.0, seed=0)
        sA = P.summarise_gs(gfA, ptsA, 0.3)
        out['anchors'] = {
            'minkowski_max_abs_G': float(np.max(np.abs(G))),
            'finalistA_beta0_h0.3_worst': sA['worst'],
            'finalistA_beta0_typeI_frac_sig': sA['typeI_frac_sig'],
            'finalistA_stored_worst': 2.141e-07,
        }
        save(out, OUT)
        print('anchors:', out['anchors'], flush=True)

    profs = {'outer': P.frontier_outer(), 'inner': P.frontier_inner()}
    for name, prof in profs.items():
        sh_state = state['shells'].setdefault(name, {})
        pts_scr, _ = P.screen_points(prof['R2'])
        bnds = P.bounds_for(prof)
        x_prev = None
        for beta in BETAS:
            key = f'b{beta}'
            if key in sh_state and 'audit' in sh_state[key]:
                x_prev = np.array(sh_state[key]['x'])
                continue
            rec = sh_state.setdefault(key, {})
            x0 = P.zero_start(prof) if x_prev is None else x_prev.copy()
            # zero/continuation-start score (economics of the search, logged)
            gf0 = P.alone_gfunc(prof, beta, x0)
            sc0, info0 = P.screen_score(gf0, pts_scr)
            rec['start_score'] = sc0
            rec['start_info'] = info0
            rec['start_x'] = [float(v) for v in x0]
            save(state, STATE)
            print(f'{name} {key} start score {sc0:+.3e} '
                  f'({time.time()-t0:.0f}s)', flush=True)
            if 'x' not in rec:
                # Fast clone-algebra objective (p803_lib.FastAloneObjective)
                # on the core points; explicit forward-difference jac
                # with step 2e-3 (the default 1.5e-8 step is below the
                # FD auditor's noise — first run's polish stalled at
                # the start score with nfev=30; recorded in run record).
                # Objective points: the P73-1 core mask — audit-set
                # points with r in [R1-0.75, R2]. (A wider set was
                # tried first: its min sat at r=11.53 in the smoothed
                # exterior tail, design-insensitive and an h=0.3
                # stencil artefact — it flips +5.3e-07 at h=0.075
                # while the wall reads +1.5e-04; recorded in the run
                # record. The cavity read is likewise a floor-level
                # background read, ~+9e-07, shape-insensitive.)
                pts_full0, _ = audit_points(prof['R2'], seed=11)
                rr0 = np.sqrt(np.sum(pts_full0 ** 2, axis=1))
                core = pts_full0[(rr0 >= prof['R1'] - 0.75) &
                                 (rr0 <= prof['R2'])]
                rec['obj_npts'] = int(len(core))
                obj = P.FastAloneObjective(prof, beta, core)
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
            # full alone audit at h=0.3/0.15 + h=0.075 ladder (the
            # exterior-tail artefact pattern needs the third rung)
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
    out['elapsed_s'] = time.time() - t0
    save(out, OUT)
    print(f'DONE {out["elapsed_s"]:.0f}s -> {OUT}', flush=True)


if __name__ == '__main__':
    main()
