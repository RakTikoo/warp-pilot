#!/usr/bin/env python3
"""
p1281_assemble.py -- assemble phase128/results/p1281_results.json
from work/p1281_ckpt.jsonl + work/p1281_gate.log. Adds the family-A
read at the best candidate (same z and (A, lam), no fluid) and the
verdict fields under the registered bars. float64.
"""
import json
import sys

import numpy as np

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, W + '/phase119/work')
sys.path.insert(0, W + '/phase101/work')
sys.path.insert(0, W + '/phase79')
sys.path.insert(0, W + '/phase76')
sys.path.insert(0, W + '/phase18')
import p1194_lib as P4  # noqa: E402
import p761_lib as L    # noqa: E402

HINGE_LEGAL = 0.5892857142857143
HINGE_EMAX = 0.9999999999784565

gate = None
for line in open(W + '/phase128/work/p1281_gate.log'):
    if line.startswith('GATEJSON '):
        gate = json.loads(line[len('GATEJSON '):])
assert gate and gate['gate_pass'], 'gate missing/failed'

runs = [json.loads(l) for l in open(W + '/phase128/work/p1281_ckpt.jsonl')
        if l.strip()]
runs = [r for r in runs if 'error' not in r]
assert len(runs) >= 12, len(runs)
runs.sort(key=lambda r: r['start'])
seeds = [r.pop('seed') for r in runs]

key = lambda r: (r['frontier_A'], r['subset_legal'],  # noqa: E731
                 -r['eom_rel_max_nondeg'], -r['eom_rel_med_nondeg'])
best = max(runs, key=key)


def pareto(r):
    return ((r['subset_legal'] >= HINGE_LEGAL
             and r['eom_rel_max_nondeg'] < HINGE_EMAX)
            or (r['subset_legal'] > HINGE_LEGAL
                and r['eom_rel_max_nondeg'] <= HINGE_EMAX))


def joint_pass(r):
    return (r['frontier_A'] > 0 and r['n_nondeg'] >= 28
            and not r['trap_fires'])


any_pass = any(joint_pass(r) for r in runs)
any_par = any(pareto(r) for r in runs)

# family A at best
wall = P4.WallNF(1.1)
wallP = L.Wall(1.1)
PTS = wallP.pts_sub
wall.prof_A, wall.prof_lam = best['A'], best['lam']
famA_r = P4.full_read(wall, PTS, np.asarray(best['z']), None)
famA = dict(z=best['z'], profile_A=best['A'], profile_lam=best['lam'],
            subset_legal=famA_r['subset_legal'],
            eom_rel_max_nondeg=famA_r['eom_rel_max_nondeg'],
            eom_rel_med_nondeg=famA_r['eom_rel_med_nondeg'],
            n_nondeg=famA_r['n_nondeg'], n_deg=famA_r['n_deg'],
            health_ok=famA_r['health_ok'], frontier_A=famA_r['frontier_A'],
            trap_fires=famA_r['trap_fires'],
            Fsum_maxabs=famA_r['Fsum_maxabs'],
            alignment_set=famA_r['alignment_set'],
            max_resid_point=famA_r['max_resid_point'],
            max_resid_in_alignment=famA_r['max_resid_in_alignment'],
            max_resid_decomp=famA_r['max_resid_decomp'],
            n_plateau_kin_live=famA_r['n_plateau_kin_live'])

min_abs_bc = min(r['abs_bc'] for r in runs)
posed = best['n_plateau_kin_live'] > 22  # majority of 44
align_carries = bool(best['alignment_set']
                     and best['max_resid_in_alignment'])
if any_pass:
    verdict = 'JOINT PASS'
elif any_par:
    verdict = 'JOINT (i)+(ii) IMPROVEMENT'
elif align_carries or not posed:
    verdict = 'ESCAPE FAILS (composition form)'
else:
    verdict = 'COMPOSITION WORKS MECHANICALLY, FRONT STANDS'

out = dict(
    item='P128-1 (FU-P1194-1) — compose the two escapes',
    gate=dict(pass_=gate['gate_pass'], worst_err=gate['worst_err'],
              rows=gate['rows'], hinge_alignment_set=gate['hinge_alignment_set'],
              hinge_SF=gate['hinge_SF'], fd_check=gate['fd_check']),
    hinge_best=dict(
        z=[2.756667559450937, -1.498683175695639, 0.7811507949670238,
           0.3385988091052908, 0.870145941019083, 1.222294121969537,
           0.0639057960421364, -0.15512773896022752],
        rho0=0.046611949162594764, subset_legal=HINGE_LEGAL,
        eom_rel_max_nondeg=HINGE_EMAX, eom_rel_med_nondeg=0.22437629566157347,
        n_nondeg=56, n_deg=0, health_ok=False, frontier_A=0.0,
        alignment_set=[44]),
    pose=('phi(r) = wallwide(pi0,shape) + A*W(r)*sin(2 pi (r-10)/lam) '
          'with pi0 = bc/(2(2 xi + b2)) eliminated; guards '
          '|2xi+b2| >= 0.2, pi0 in [0.02,2.9], |bc| >= 0.05'),
    n_starts=len(runs),
    seed_starts=seeds,
    runs=runs,
    best=best,
    family_A_at_best=famA,
    any_joint_pass=bool(any_pass), any_pareto=bool(any_par),
    min_abs_bc_all_runs=float(min_abs_bc),
    boundary_pressed=bool(min_abs_bc <= 0.05 + 1e-9),
    nonflat_majority_at_best=bool(posed),
    verdict=verdict)
with open(W + '/phase128/results/p1281_results.json', 'w') as f:
    json.dump(out, f, indent=1)
print('best start', best['start'], 'legal', best['subset_legal'],
      'emax', best['eom_rel_max_nondeg'], 'emed',
      best['eom_rel_med_nondeg'], 'health', best['health_ok'],
      'frontier', best['frontier_A'], 'align', best['alignment_set'],
      'kin_live', best['n_plateau_kin_live'], 'guards_ok',
      best['guards_ok'], 'min|bc|', min_abs_bc)
print('any_pass', any_pass, 'any_pareto', any_par, 'verdict', verdict)
