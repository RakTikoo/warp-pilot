"""
p408_pool_p408_de.py - Phase 392: GPU differential evolution (SCREENING ONLY,
never a verdict), generalised from p386_stage2x_de.py. Usage:
  python p408_pool_p408_de.py <spec.json>
spec: {"tag": str, "lib": "p391_12"|"p392_16", "lo":[n], "hi":[n],
       "seed_ys":[[n],...], "y_ref":[n] (reference vector read at startup
       on the DE union set; also supplies the union-set r_m anchor),
       "cap_min": float, "pop": int (default 64)}
Screening point set: union of repaired_radii_cell switch clusters for
r_m in {12, 14, y_ref r_m, 19, 21, 22.5} x 26 dirs, EXTENDED mask
[2.234381, 27.265413]. Checkpoint every generation to
~/work/p408/state/<tag>_de_state.json + <tag>_de_pop.npz.
DE: best/1/bin, F=0.7, CR=0.9, rng 3863 (386 settings).
"""
import os, sys, time, json
import numpy as np
from concurrent.futures import ThreadPoolExecutor

POOL = '/home/spark/work/p386/warp-pilot'
P408 = POOL + '/phase408/work'
for p in [P408, POOL, POOL + '/phase386/work', POOL + '/phase251/work',
          POOL + '/phase50', POOL + '/gate6', POOL + '/phase63']:
    sys.path.insert(0, p)
os.environ.setdefault('P386_CONSTR_DR', '2.5e-4')
os.environ.setdefault('P408_CONSTR_DR', '2.5e-4')
import p386_screen as S
import p386_gpu as G
import p386_lib
import p2513_lib as H

# --- padded spline stacking (386 stage2x fix, verbatim) -------------------
import torch as _torch


def _stack_exports_padded(builders):
    exps = []
    for name in ('_a', '_m', '_S'):
        raw = [(np.asarray(getattr(b, name).x), np.asarray(getattr(b, name).c))
               for b in builders]
        N = max(len(t) for t, _ in raw)
        ts, cs = [], []
        for t, c in raw:
            if len(t) < N:
                t = np.concatenate([t, np.full(N - len(t), t[-1])])
                c = np.concatenate([c, np.zeros((4, N - 1 - c.shape[1]))], axis=1)
            ts.append(_torch.tensor(t, dtype=G.DT, device=G.DEV))
            cs.append(_torch.tensor(c, dtype=G.DT, device=G.DEV))
        exps.append((_torch.stack(ts), _torch.stack(cs)))
    rmax = _torch.tensor(np.array([float(b.rg[-1]) for b in builders]),
                         dtype=G.DT, device=G.DEV)
    return exps, rmax


G.stack_exports = _stack_exports_padded

spec = json.load(open(sys.argv[1]))
TAG = spec['tag']
LIB = spec.get('lib', 'p386')
LO = np.array(spec['lo'], dtype=np.float64)
HI = np.array(spec['hi'], dtype=np.float64)
ND = len(LO)
CAP_MIN = float(spec.get('cap_min', 150))
POP = int(spec.get('pop', 64))
Y_REF = np.array(spec['y_ref'], dtype=np.float64)
STATE = '/home/spark/work/p408/state'
os.makedirs(STATE, exist_ok=True)
CHUNK = 8
F_MUT, CR = 0.7, 0.9
rng = np.random.default_rng(3863)

if LIB == 'p391_12':
    import p408_pool_p391_lib12 as L12

    def build_one(y):
        return L12.GradedProcaccia12(np.asarray(y, dtype=np.float64),
                                     dr=np.float64(S.DR_SCREEN))
elif LIB == 'p392_16':
    import p408_pool_p408_lib16 as L16

    def build_one(y):
        return L16.GradedProcaccia16(np.asarray(y, dtype=np.float64),
                                     dr=np.float64(S.DR_SCREEN))
else:
    def build_one(y):
        return p386_lib.GradedProcaccia(np.asarray(y, dtype=np.float64),
                                        dr=np.float64(S.DR_SCREEN))

# --- union screening point set (EXTENDED mask) ----------------------------
MASK_LO, MASK_HI = 2.234381410067394, 27.265413445973113
rad_all = [H.repaired_radii_cell(S.R1, S.R2, S.W, rm)
           for rm in (12.0, 14.0, float(Y_REF[-1]), 19.0, 21.0, 22.5)]
rad = np.unique(np.round(np.concatenate(rad_all), 10))
pts_all = np.concatenate([H.DIRS26 * r for r in rad]).astype(np.float64)
radp = np.linalg.norm(pts_all, axis=1)
core = (radp >= MASK_LO) & (radp <= MASK_HI)
PTS = pts_all[core]
print(f'{TAG} DE: lib={LIB} nd={ND} union radii={len(rad)} pts={len(PTS)} '
      f'pop={POP} cap_min={CAP_MIN}', flush=True)


def batched_beta_crit(pop_y):
    N = len(pop_y)
    with ThreadPoolExecutor(max_workers=8) as ex:
        builders = list(ex.map(build_one, [pop_y[i] for i in range(N)]))
    lo = np.full(N, 0.10)
    hi = np.full(N, 0.20)
    bc = np.full(N, np.nan)
    flag = [''] * N

    def legal_batch(idxs, beta):
        out = {}
        barr = None if np.ndim(beta) == 0 else np.asarray(beta, dtype=np.float64)
        for s0 in range(0, len(idxs), CHUNK):
            sub_idx = idxs[s0:s0 + CHUNK]
            sub = [builders[i] for i in sub_idx]
            bsub = beta if barr is None else barr[s0:s0 + CHUNK]
            That = G.gpu_that(sub, PTS, bsub, S.SCREEN_H)
            for j, i in enumerate(sub_idx):
                out[i] = G.two_number_score(That[j], S.R1)[0]
        return out

    idxs = list(range(N))
    ok_lo = legal_batch(idxs, 0.10)
    active = []
    for i in idxs:
        if not ok_lo[i]:
            bc[i] = 0.10
            flag[i] = 'at_or_below_lo'
        else:
            active.append(i)
    if active:
        ok_hi = legal_batch(active, 0.20)
        nxt = []
        for i in active:
            if ok_hi[i]:
                bc[i] = 0.20
                flag[i] = 'at_or_above_hi'
            else:
                nxt.append(i)
        active = nxt
    while active:
        mids = {i: 0.5 * (lo[i] + hi[i]) for i in active if hi[i] - lo[i] > 0.001}
        if not mids:
            break
        gidx = list(mids.keys())
        res = legal_batch(gidx, np.array([mids[i] for i in gidx]))
        for i in gidx:
            if res[i]:
                lo[i] = mids[i]
            else:
                hi[i] = mids[i]
        active = [i for i in active if hi[i] - lo[i] > 0.001]
    for i in range(N):
        if flag[i] == '':
            bc[i] = 0.5 * (lo[i] + hi[i])
            flag[i] = 'bisected'
    brackets = [[None if flag[i] == 'at_or_below_lo' else float(lo[i]),
                 None if flag[i] == 'at_or_above_hi' else float(hi[i])]
                for i in range(N)]
    return bc, brackets, flag


def save_state(gen, pop, fit, br, best_hist, t0, n_evals, done=False):
    st = {'gen': gen, 'elapsed_s': time.time() - t0, 'done': done,
          'pop': pop.tolist(), 'beta_crit': [float(v) for v in fit],
          'brackets': br, 'best_hist': best_hist,
          'best_y': pop[int(np.argmax(fit))].tolist(),
          'best_beta_crit': float(np.max(fit)),
          'n_evals': n_evals,
          'box_lo': LO.tolist(), 'box_hi': HI.tolist(),
          'n_pts': int(len(PTS)), 'lib': LIB, 'tag': TAG,
          'note': 'SCREENING ONLY (GPU DE union extended point set)'}
    tmp = os.path.join(STATE, f'{TAG}_de_state.json.tmp')
    json.dump(st, open(tmp, 'w'), indent=1)
    os.replace(tmp, os.path.join(STATE, f'{TAG}_de_state.json'))
    np.savez(os.path.join(STATE, f'{TAG}_de_pop.npz'), pop=pop, fit=fit)


def main():
    t0 = time.time()
    bc_ref, br_ref, fl_ref = batched_beta_crit(Y_REF[None, :])
    print(f'DE-set y_ref beta_crit_screening={bc_ref[0]} bracket={br_ref[0]} '
          f'flag={fl_ref[0]}', flush=True)
    json.dump({'y_ref_beta_crit_on_de_set': float(bc_ref[0]),
               'bracket': br_ref[0], 'flag': fl_ref[0],
               'n_pts': int(len(PTS)), 'lib': LIB,
               'note': 'SCREENING ONLY'},
              open(os.path.join(STATE, f'{TAG}_de_yref.json'), 'w'), indent=1)

    pop = LO + (HI - LO) * rng.random((POP, ND))
    seeds = [np.array(s, dtype=np.float64) for s in spec['seed_ys']]
    for i, s in enumerate(seeds[:POP]):
        pop[i] = np.minimum(np.maximum(s, LO), HI)
    fit, br, fl = batched_beta_crit(pop)
    n_evals = POP
    best_hist = [{'gen': 0, 'best': float(fit.max()),
                  'bracket': br[int(np.argmax(fit))],
                  'elapsed_s': time.time() - t0}]
    print(f'gen 0 best={fit.max():.5f} ({time.time()-t0:.0f}s)', flush=True)
    save_state(0, pop, fit, br, best_hist, t0, n_evals)
    gen = 0
    while (time.time() - t0) < CAP_MIN * 60:
        gen += 1
        trials = np.empty_like(pop)
        best_i = int(np.argmax(fit))
        for i in range(POP):
            idxs = [j for j in range(POP) if j != i]
            r1, r2 = rng.choice(idxs, 2, replace=False)
            mutant = pop[best_i] + F_MUT * (pop[r1] - pop[r2])
            cross = rng.random(ND) < CR
            cross[rng.integers(ND)] = True
            trials[i] = np.where(cross, mutant, pop[i])
        trials = np.minimum(np.maximum(trials, LO), HI)
        tfit, tbr, tfl = batched_beta_crit(trials)
        n_evals += POP
        better = tfit > fit
        pop[better] = trials[better]
        fit[better] = tfit[better]
        for i in range(POP):
            if better[i]:
                br[i] = tbr[i]
        best_hist.append({'gen': gen, 'best': float(fit.max()),
                          'bracket': br[int(np.argmax(fit))],
                          'elapsed_s': time.time() - t0})
        print(f'gen {gen} best={fit.max():.5f} mean={fit.mean():.5f} '
              f'({time.time()-t0:.0f}s)', flush=True)
        save_state(gen, pop, fit, br, best_hist, t0, n_evals)
    save_state(gen, pop, fit, br, best_hist, t0, n_evals, done=True)
    print(f'DE DONE gens={gen} best={fit.max():.5f} evals={n_evals} '
          f'wall={time.time()-t0:.0f}s', flush=True)


if __name__ == '__main__':
    main()
