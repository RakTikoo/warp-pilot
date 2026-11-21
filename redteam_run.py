"""redteam_run.py — full R1 hunts for the frozen configs."""
import json, time
import numpy as np
import redteam as rt

SEEDS = {  # audit-worst locations (r, direction) to seed restarts near
    'finalist_A': [(5.75, (0.3, 0.9, 0.3)), (10.5, (0.0, 1.0, 0.0)),
                   (24.0, (1.0, 0.2, 0.0))],
    'finalist_B2': [(5.75, (0.3, 0.9, 0.3)), (10.5, (0.0, 1.0, 0.0)),
                    (24.0, (1.0, 0.2, 0.0))],
    'frontier_b005': [(12.1, (0.3, 0.9, 0.3)), (5.2, (0.0, 1.0, 0.0)),
                      (7.5, (1.0, 0.2, 0.0))],
}

for name in ('finalist_A', 'finalist_B2', 'frontier_b005'):
    cfg = rt.load_cfg(name)
    out = {'config': name}
    seed_xyz = []
    for (rr, d) in SEEDS[name]:
        d = np.array(d, dtype=float); d /= np.linalg.norm(d)
        seed_xyz.append(rr * d)
    for kind in ('nec', 'wec'):
        t0 = time.time()
        out[kind] = rt.hunt(cfg, kind=kind, n_restarts=192, steps=500, seed=3,
                            seed_xyz=seed_xyz)
        out[kind]['elapsed_s'] = time.time() - t0
        print(name, kind, 'worst:', out[kind]['worst_value'],
              'r:', out[kind]['r'], 'frac_neg:', out[kind]['frac_negative'],
              f"({out[kind]['elapsed_s']:.0f}s)", flush=True)
    json.dump(out, open(f'results/redteam_R1_{name}.json', 'w'), indent=1)
print('R1 DONE')
