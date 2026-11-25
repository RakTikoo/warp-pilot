#!/usr/bin/env python3
"""g16_run.py -- GATE-16 driver: machinery gate, then deciding reads."""
import json
import os
import sys

import numpy as np

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, os.path.join(W, 'gate16/work_a'))
import g16_audit as G  # noqa: E402
import p761_lib as L   # noqa: E402

OUT = os.path.join(W, 'gate16/results/wa_results.json')
res = {}


def save():
    with open(OUT, 'w') as f:
        json.dump(res, f, indent=1)


wall = L.Wall(1.1)
PTS = wall.pts_sub
assert len(PTS) == 56, len(PTS)

# ---------------- STEP 1: machinery gate ----------------
raw = json.load(open(os.path.join(W, 'phase101/results/p1015_partB_raw.json')))
cfgs = [('direct/B76_mu0', raw['direct']['B76_mu0']),
        ('direct/A76_mu0', raw['direct']['A76_mu0'])]
for i, r in enumerate(raw['runs_B']):
    if 'z_full' in r:
        cfgs.append((f'runs_B[{i}]', r))
for i, r in enumerate(raw['runs_A']):
    if 'z_full' in r:
        cfgs.append((f'runs_A[{i}]', r))
rows, worst = [], 0.0
for name, r in cfgs:
    z8 = np.asarray(r['z_full'][:8], dtype=np.float64)
    ct = G.canonical_terms(wall, PTS, z8)
    rel, D = G.rel_stats(ct)
    nd = D >= G.FLOOR
    emax = float(rel[nd].max())
    emed = float(np.median(rel[nd]))
    e1 = abs(emax - r['eom_rel_max_nondeg'])
    e2 = abs(emed - r['eom_rel_med_nondeg'])
    worst = max(worst, e1, e2)
    rows.append(dict(name=name, emax=emax, emed=emed,
                     stored_emax=r['eom_rel_max_nondeg'],
                     stored_emed=r['eom_rel_med_nondeg'],
                     err_max=e1, err_med=e2,
                     pass_=bool(e1 <= 1e-6 and e2 <= 1e-6)))
    print(name, 'emax err', f'{e1:.3e}', 'emed err', f'{e2:.3e}', flush=True)

HINGE_Z = [2.756667559450937, -1.498683175695639, 0.7811507949670238,
           0.3385988091052908, 0.870145941019083, 1.222294121969537,
           0.0639057960421364, -0.15512773896022752]
HINGE_RHO = 0.046611949162594764
ct_h = G.canonical_terms(wall, PTS, np.asarray(HINGE_Z))
idx_h, det_h, _, _ = G.alignment_set(ct_h)
print('hinge alignment set', idx_h, flush=True)
gate_pass = all(r['pass_'] for r in rows) and idx_h == [44]
res['machinery_gate'] = dict(
    rows=rows, worst_err=worst, hinge_alignment_set=idx_h,
    hinge_SF=(det_h[44]['S_F'] if 44 in det_h else None), pass_=gate_pass)
save()
print('MACHINERY GATE', 'PASS' if gate_pass else 'FAIL', 'worst', worst,
      flush=True)
if not gate_pass:
    sys.exit(1)

# ---------------- STEP 2: deciding reads ----------------
def clean(d):
    return d

# (a) hinge best
hinge = G.full_read(wall, PTS, HINGE_Z, (G.W_B, HINGE_RHO))
hinge['target_named'] = G.targeting_read(ct_h, [44, 50, 51, 52])
hinge['target_band'] = G.targeting_read(ct_h, list(range(44, 56)))
res['hinge'] = hinge
save()
print('HINGE', hinge['subset_legal'], hinge['subset_legal_full'],
      hinge['eom_rel_max_nondeg'], hinge['eom_rel_med_nondeg'],
      hinge['health_ok'], hinge['frontier_A'], flush=True)

# (b) P128-1 best: composed escapes, single-sine blend
p1 = json.load(open(os.path.join(W, 'phase128/results/p1281_results.json')))
b1 = p1['best']
wb1 = G.WallBlend(1.1)
wb1.blend_fn = G.sine1(float(b1['A']), float(b1['lam']))
r1 = G.full_read(wb1, PTS, b1['z'], (G.W_B, float(b1['rho0'])))
ct1 = G.canonical_terms(wb1, PTS, np.asarray(b1['z'], dtype=np.float64))
r1['target_named'] = G.targeting_read(ct1, [44, 50, 51, 52])
r1['target_band'] = G.targeting_read(ct1, list(range(44, 56)))
xi, bc, b2, pi0 = [float(b1['z'][i]) for i in range(4)]
r1['Hphi_at_pi0'] = float(-(2 * xi + b2) * pi0 + bc / 2.0)
r1['pi0_from_constraint'] = float(bc / (2 * (2 * xi + b2)))
r1['tFA_at_44'] = float(ct1['t_FA'][44])
res['p1281_best'] = r1
save()
print('P1281', r1['subset_legal'], r1['subset_legal_full'],
      r1['eom_rel_max_nondeg'], r1['eom_rel_med_nondeg'],
      r1['health_ok'], r1['frontier_A'], 'maxpt',
      r1['max_resid_point'], flush=True)

# (c) P128-2 best: K=3 blend
p2 = json.load(open(os.path.join(W, 'phase128/results/p1282_results.json')))
b2 = p2['best']
wb2 = G.WallBlend(1.1)
wb2.blend_fn = G.sineK([float(x) for x in b2['blend']])
r2 = G.full_read(wb2, PTS, b2['z'], (G.W_B, float(b2['rho0'])))
ct2 = G.canonical_terms(wb2, PTS, np.asarray(b2['z'], dtype=np.float64))
r2['target_named'] = G.targeting_read(ct2, [44, 50, 51, 52])
r2['target_band'] = G.targeting_read(ct2, list(range(44, 56)))
res['p1282_best'] = r2
save()
print('P1282', r2['subset_legal'], r2['subset_legal_full'],
      r2['eom_rel_max_nondeg'], r2['eom_rel_med_nondeg'],
      r2['health_ok'], r2['cr2_min'], r2['cr2_max'], r2['frontier_A'],
      'maxpt', r2['max_resid_point'], flush=True)

# (d) P128-2 targeted candidate (start 5): the migration read
tg = p2['targeted_candidate']
wb3 = G.WallBlend(1.1)
wb3.blend_fn = G.sineK([float(x) for x in tg['blend']])
r3 = G.full_read(wb3, PTS, tg['z'], (G.W_B, float(tg['rho0'])))
ct3 = G.canonical_terms(wb3, PTS, np.asarray(tg['z'], dtype=np.float64))
r3['target_named'] = G.targeting_read(ct3, [44, 50, 51, 52])
r3['target_band'] = G.targeting_read(ct3, list(range(44, 56)))
res['p1282_targeted'] = r3
save()
print('P1282T', r3['subset_legal'], r3['subset_legal_full'],
      r3['eom_rel_max_nondeg'], r3['eom_rel_med_nondeg'],
      r3['health_ok'], r3['frontier_A'], 'maxpt',
      r3['max_resid_point'], 'named opp', r3['target_named']['n_opposed'],
      flush=True)

# ---------------- comparisons on the gate's own reads ----------------
def cmp_(r, h):
    return dict(
        d_legal_subset=r['subset_legal'] - h['subset_legal'],
        d_legal_full=r['subset_legal_full'] - h['subset_legal_full'],
        d_eom_max=r['eom_rel_max_nondeg'] - h['eom_rel_max_nondeg'],
        d_eom_med=r['eom_rel_med_nondeg'] - h['eom_rel_med_nondeg'],
        pareto_clause1=bool(r['subset_legal'] >= h['subset_legal']
                            and r['eom_rel_max_nondeg'] < h['eom_rel_max_nondeg']),
        pareto_clause2=bool(r['subset_legal'] > h['subset_legal']
                            and r['eom_rel_max_nondeg'] <= h['eom_rel_max_nondeg']))

res['comparisons'] = dict(
    p1281_vs_hinge=cmp_(r1, hinge), p1282_vs_hinge=cmp_(r2, hinge))
save()
print('DONE', flush=True)
