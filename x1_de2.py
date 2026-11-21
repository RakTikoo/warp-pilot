"""
x1_de2.py — X1 adversarial round (Track P protocol): DE at Rmaj=45 with
the screen = UNION of the three point sets the first DE was judged on
(seeds 111/999/31337 — the pockets it was caught by are now in training),
initialised at the first DE's winning genes + jitter. If the objective
still saturates negative on ~1000 training points, the tube-symmetric
toroidal exclusion is adversarially confirmed.
"""
import json, time
import numpy as np
from scipy.optimize import differential_evolution

import x1_de

RMAJ = 45.0
pts = np.concatenate([x1_de.screen_points(RMAJ, seed=s,
                        n=200 if s == 111 else 320)
                      for s in (111, 999, 31337)])
x1_de._G['pts'] = pts; x1_de._G['Rmaj'] = RMAJ; x1_de._G['beta'] = 0.0
print(f'adversarial screen: {len(pts)} pts', flush=True)

d = json.load(open('results/x1_de_Rmaj45.json'))
g0 = np.array(d['genes'])
rng = np.random.default_rng(7)
pop = 2 * 17
init = np.tile(g0, (pop, 1)) + rng.normal(0, 0.008, (pop, 17))
init[0] = g0
lo = np.array([b[0] for b in x1_de.BOUNDS]); hi = np.array([b[1] for b in x1_de.BOUNDS])
init = np.clip(init, lo, hi)

t0 = time.time()
res = differential_evolution(x1_de._obj, x1_de.BOUNDS, maxiter=45, popsize=2,
                             mutation=(0.3, 1.2), recombination=0.8,
                             init=init, polish=False, seed=777)
genes = res.x
w, tI = x1_de.worst_margin(genes, RMAJ, 0.0, pts, h=0.3)
out = {'Rmaj': RMAJ, 'train_worst': w, 'train_typeI': tI,
       'genes': genes.tolist(), 'n_evals': int(res.nfev),
       'elapsed_s': time.time() - t0, 'n_train_pts': len(pts)}
print('adversarial DE done:', json.dumps(
    {k: out[k] for k in ('train_worst', 'train_typeI', 'n_evals')}), flush=True)
for seed in (555001, 777001):
    pa = x1_de.screen_points(RMAJ, seed=seed, n=320)
    for h in (0.3, 0.15):
        wa, ta = x1_de.worst_margin(genes, RMAJ, 0.0, pa, h=h)
        out[f'final_seed{seed}_h{h}'] = {'worst': wa, 'typeI': ta}
        print(f'  final seed={seed} h={h}: worst {wa:+.4e} TypeI {ta:.3f}',
              flush=True)
json.dump(out, open('results/x1_de2_Rmaj45.json', 'w'), indent=1, default=float)
print('X1 DE2 DONE', flush=True)
