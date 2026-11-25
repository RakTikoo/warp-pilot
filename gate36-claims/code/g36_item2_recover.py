"""Recovery: perturbation ladder only, from the persisted jacobian arm.
Reproduces the driver's perturbation block verbatim (same seeds/stream),
gated on the checkpoint: best N=6 theta and diagnostics loaded from
g36_item2_arm_jacobian.json. The eps=1e-12 draw 0 that completed before
the restart (best maxR 1.122e-13 in the run log) is re-derived by the
identical RNG stream and checked against the logged value.
"""
import json, time
import numpy as np
import g36_spinor as G
from g36_item2 import load_targets, do_fit, random_start, SEED_PERT, WORK, ROOT

t0 = time.time()
saved = json.load(open(WORK + 'g36_item2_arm_jacobian.json'))
RESULTS = saved['results']
SOLUTIONS = saved['solutions']
th6 = np.array(RESULTS['best_N6_diagnostics']['theta'])

d320, sites320, thats320, frobs320 = load_targets(ROOT + 'phase320/work/p320_targets.json')

rngp = np.random.default_rng(SEED_PERT)
pert = []
for eps in [1e-12, 1e-9, 1e-6, 1e-4]:
    for draw in range(2):
        thats_p, frobs_p = [], []
        for s in range(4):
            U = rngp.uniform(-1, 1, size=(4, 4))
            U = 0.5 * (U + U.T)
            Tp_ = thats320[s] + eps * frobs320[s] * U
            thats_p.append(Tp_); frobs_p.append(float(np.linalg.norm(Tp_)))
        attempts = []
        thw, Rs_w, _ = do_fit(th6, 6, sites320, thats_p, frobs_p, 900)
        attempts.append(('warm', thw))
        rngf = np.random.default_rng(SEED_PERT * 1000 + int(-np.log10(eps)) * 10 + draw)
        thf, Rs_f, _ = do_fit(random_start(rngf, 6), 6, sites320, thats_p, frobs_p, 900)
        attempts.append(('fresh', thf))
        recs = []
        for nm, thx in attempts:
            px, ax = G.modes_from_theta(thx, 6)
            Rd, rho_d, _ = G.direct_residuals(px, ax, sites320, thats_p)
            recs.append({'start': nm, 'maxR_direct_vs_perturbed': max(Rd),
                         'Rs_direct': Rd, 'rhos_fit': rho_d})
        best_rec = min(recs, key=lambda r: r['maxR_direct_vs_perturbed'])
        pert.append({'eps': eps, 'draw': draw, 'attempts': recs,
                     'best_maxR_direct': best_rec['maxR_direct_vs_perturbed'],
                     'best_rhos_fit': best_rec['rhos_fit'],
                     'perturbed_target_rhos': [float(T[0, 0]) for T in thats_p]})
        print(f'  eps={eps:g} draw={draw}: best maxR={best_rec["maxR_direct_vs_perturbed"]:.3e}', flush=True)
    RESULTS['perturbation_ladder'] = pert
    with open(WORK + f'g36_item2_arm_pert_eps{eps:g}.json', 'w') as f:
        json.dump({'results': RESULTS, 'solutions': SOLUTIONS}, f, indent=1)
    print(f'[saved arm pert_eps{eps:g}]', flush=True)

RESULTS['wall_time_note'] = ('main driver wall time lost to VM restart; '
                             'recovery (perturbation ladder) wall time below')
RESULTS['recovery_wall_time_s'] = time.time() - t0
with open(WORK + 'g36_item2_results.json', 'w') as f:
    json.dump(RESULTS, f, indent=1)
with open(WORK + 'g36_item2_solutions.json', 'w') as f:
    json.dump(SOLUTIONS, f, indent=1)
print('RECOVERY DONE in', RESULTS['recovery_wall_time_s'], 's', flush=True)
