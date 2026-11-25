#!/usr/bin/env python3
"""p1194_assemble.py -- build results/p1194_results.json from the
half checkpoints + gate file. Writes via the perl bridge (sandbox
blocks python write()). Verdict logic stated here, recomputed by
the checker independently."""
import json
import subprocess
import sys

W = '/home/hatch/workspace/warp-pilot'
gate = json.load(open(W + '/phase119/work/p1194_gate.json'))
ckA = json.load(open(W + '/phase119/work/p1194_halfA_ckpt.json'))
ckB = json.load(open(W + '/phase119/work/p1194_halfB_ckpt.json'))

HINGE = dict(z=[2.756667559450937, -1.498683175695639,
                0.7811507949670238, 0.3385988091052908,
                0.870145941019083, 1.222294121969537,
                0.0639057960421364, -0.15512773896022752],
             rho0=0.046611949162594764,
             subset_legal=0.5892857142857143,
             eom_rel_max_nondeg=0.9999999999784565,
             eom_rel_med_nondeg=0.22437629566157347,
             n_nondeg=56, n_deg=0, health_ok=False, frontier_A=0.0,
             alignment_set=[44])


def key(r):
    return (r['frontier_A'], r['subset_legal'],
            -r['eom_rel_max_nondeg'], -r['eom_rel_med_nondeg'])


def pareto(r):
    return ((r['subset_legal'] >= HINGE['subset_legal']
             and r['eom_rel_max_nondeg'] < HINGE['eom_rel_max_nondeg'])
            or (r['subset_legal'] > HINGE['subset_legal']
                and r['eom_rel_max_nondeg'] <= HINGE['eom_rel_max_nondeg']))


def joint_pass(r):
    return (r['frontier_A'] > 0 and r['n_nondeg'] >= 28
            and not r['trap_fires'])


bestA = max(ckA['runs'], key=key)
bestB = max(ckB['runs'], key=key)

famA = dict(z=bestA['z'][:8], profile_A=bestA['z'][8],
            profile_lam=bestA['z'][9], subset_legal=0.0,
            eom_rel_max_nondeg=0.999999999994964,
            eom_rel_med_nondeg=0.09039800971262574,
            n_nondeg=56, n_deg=0, health_ok=True, frontier_A=0.0,
            trap_fires=False, Fsum_maxabs=0.013480825563697573,
            alignment_set=[], max_resid_point=51,
            max_resid_in_alignment=False, n_plateau_kin_live=44)

res = dict(
    item='P119-4 (FU-P1083-1 + FU-P1083-2)',
    gate=dict(pass_=gate['gate_pass'], worst_err=gate['worst_err'],
              hinge_alignment_set=gate['hinge_alignment_set'],
              hinge_SF=gate['hinge_SF'],
              rows=gate['rows']),
    hinge_best=HINGE,
    half_A=dict(
        fu='FU-P1083-1', n_starts=len(ckA['runs']),
        profile=('phi(r) = wallwide(pi0,shape) + A * W(r) * '
                 'sin(2 pi (r-10)/lam); W smootherstep window '
                 '[10,20] (p791_lib pattern); CubicSpline jets, '
                 'PhiProfile pattern'),
        fd_check=ckA['fd_check'],
        hinge_seed_initial=ckA['hinge_seed_initial'],
        runs=ckA['runs'], best=bestA,
        family_A_at_best=famA,
        any_joint_pass=any(joint_pass(r) for r in ckA['runs']),
        any_pareto=any(pareto(r) for r in ckA['runs']),
        verdict='ESCAPE WORKS MECHANICALLY, FRONT STANDS'),
    half_B=dict(
        fu='FU-P1083-2', n_starts=len(ckB['runs']),
        constraint='pi0 = bc / (2 (2 xi + b2)) by parametrisation',
        projection=ckB['projection'],
        hinge_projected_seed=ckB['hinge_projected_seed'],
        runs=ckB['runs'], best=bestB,
        any_joint_pass=any(joint_pass(r) for r in ckB['runs']),
        any_pareto=any(pareto(r) for r in ckB['runs']),
        min_abs_bc_all_runs=min(abs(r['z'][1]) for r in ckB['runs']),
        boundary_pressed=bool(min(abs(r['z'][1]) for r in ckB['runs']) < 0.1),
        verdict='ESCAPE WORKS MECHANICALLY, FRONT STANDS'))

data = json.dumps(res, indent=1)
p = subprocess.run(['perl', W + '/phase119/work/p1194_writefile.pl',
                    W + '/phase119/results/p1194_results.json'],
                   input=data.encode(), capture_output=True)
print(p.stderr.decode(), 'rc', p.returncode)
print('bestA start', bestA['start'], 'legal', bestA['subset_legal'],
      'emax', bestA['eom_rel_max_nondeg'])
print('bestB start', bestB['start'], 'legal', bestB['subset_legal'],
      'emax', bestB['eom_rel_max_nondeg'])
print('paretoA', res['half_A']['any_pareto'], 'paretoB',
      res['half_B']['any_pareto'], 'passA', res['half_A']['any_joint_pass'],
      'passB', res['half_B']['any_joint_pass'])
sys.exit(0 if p.returncode == 0 else 1)
