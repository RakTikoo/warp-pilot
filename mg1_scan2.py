"""
mg1_scan2.py — MG-1 stage 2: geometry variations around the stage-1 grid.
Axes: Delta/R in {0.1, 0.5}, eta in {0.1, 0.2}, R=3, extreme amps +-0.5,
finer ahat grid {0.03, 0.3, 3}. Cleaned sample points (r >= 0.1R).
Output: results/mg1_stage2.json
"""
import json
import time
import numpy as np
import mg1_fr as mg

AHATS = [1e-2, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0]
rows = []
t0 = time.time()

def run(v_s, R, Delta, aA, aC, eta, tag):
    pts = mg.sample_points(R, Delta)
    base = mg.audit_config_fast(v_s, R, Delta, aA, aC, eta, 0.0, pts)
    Rs = base['R_absmax']
    base.update(v_s=v_s, R=R, Delta=Delta, aA=aA, aC=aC, eta=eta,
                alpha=0.0, ahat=0.0, stage=tag)
    rows.append(base)
    for ah in AHATS:
        r = mg.audit_config_fast(v_s, R, Delta, aA, aC, eta, ah / Rs, pts)
        r.update(v_s=v_s, R=R, Delta=Delta, aA=aA, aC=aC, eta=eta,
                 alpha=ah / Rs, ahat=ah, R_star=Rs, stage=tag)
        rows.append(r)
    print(f"{tag} v={v_s} R={R} D/R={Delta/R} amps=({aA},{aC}) eta={eta} "
          f"done ({time.time()-t0:.0f}s) GR worst={base['worst_m']:+.3e}", flush=True)

# Delta variations on two amp sets
for Drel in (0.1, 0.5):
    for amps in [(0.0, 0.0), (0.3, -0.3)]:
        for v in (0.9, 1.5):
            run(v, 1.0, Drel, amps[0], amps[1], 0.0, 'delta')
# eta variations
for eta in (0.1, 0.2):
    for v in (0.9, 1.5):
        run(v, 1.0, 0.25, 0.0, 0.0, eta, 'eta')
        run(v, 1.0, 0.25, 0.3, -0.3, eta, 'eta')
# extreme amps
for amps in [(0.5, 0.5), (-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5)]:
    for v in (0.9, 1.5):
        run(v, 1.0, 0.25, amps[0], amps[1], 0.0, 'extreme')
# R=3 spot checks
for v in (0.9, 1.5):
    run(v, 3.0, 0.75, 0.0, 0.0, 0.0, 'R3')
    run(v, 3.0, 0.75, 0.3, -0.3, 0.0, 'R3')
# extra velocities at base geometry
for v in (0.5, 1.2):
    run(v, 1.0, 0.25, 0.0, 0.0, 0.0, 'vextra')
    run(v, 1.0, 0.25, 0.3, -0.3, 0.0, 'vextra')

json.dump(rows, open('results/mg1_stage2.json', 'w'), indent=1)
print(f"stage2 DONE: {len(rows)} evals in {time.time()-t0:.0f}s")
