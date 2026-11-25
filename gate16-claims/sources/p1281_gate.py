#!/usr/bin/env python3
"""p1281_gate.py -- P128-1 machinery gate (run record S1).
Reproduce the seven unique corpus configurations' stored EoM
max/medians within 1e-6 via p1015_lib.canonical_terms, and the
hinge best's alignment set = {44}. Also the NF-profile FD check.
Prints GATEJSON. float64."""
import json
import os
import sys

import numpy as np

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, W + '/phase119/work')
sys.path.insert(0, W + '/phase101/work')
sys.path.insert(0, W + '/phase79')
sys.path.insert(0, W + '/phase76')
sys.path.insert(0, W + '/phase18')
import p1194_lib as P4  # noqa: E402
import p1015_lib as H   # noqa: E402
import p761_lib as L    # noqa: E402

raw = json.load(open(os.path.join(W, 'phase101/results/p1015_partB_raw.json')))
wall = L.Wall(1.1)
PTS = wall.pts_sub
cfgs = [('direct/B76_mu0', raw['direct']['B76_mu0']),
        ('direct/A76_mu0', raw['direct']['A76_mu0'])]
for i, r in enumerate(raw['runs_B']):
    if 'z_full' in r:
        cfgs.append((f'runs_B[{i}]', r))
for i, r in enumerate(raw['runs_A']):
    if 'z_full' in r:
        cfgs.append((f'runs_A[{i}]', r))
assert len(cfgs) == 7, len(cfgs)

rows, worst = [], 0.0
for name, r in cfgs:
    z8 = np.asarray(r['z_full'][:8], dtype=np.float64)
    ct = H.canonical_terms(wall, PTS, z8)
    tot = ct['t_kin'] + ct['t_pxx'] + ct['t_FA'] + ct['t_FB']
    D = (np.abs(ct['t_kin']) + np.abs(ct['t_pxx'])
         + np.abs(ct['t_FA']) + np.abs(ct['t_FB']))
    rel = np.abs(tot) / (D + 1e-12)
    nd = D >= H.FLOOR
    emax = float(rel[nd].max()); emed = float(np.median(rel[nd]))
    e1 = abs(emax - r['eom_rel_max_nondeg'])
    e2 = abs(emed - r['eom_rel_med_nondeg'])
    worst = max(worst, e1, e2)
    rows.append(dict(name=name, emax=emax, emed=emed,
                     stored_emax=r['eom_rel_max_nondeg'],
                     stored_emed=r['eom_rel_med_nondeg'],
                     err_max=e1, err_med=e2,
                     pass_=bool(e1 <= 1e-6 and e2 <= 1e-6)))
    print(name, 'emax err', f'{e1:.3e}', 'emed err', f'{e2:.3e}', flush=True)

ct = H.canonical_terms(wall, PTS, np.asarray(raw['best_B']['z_full'][:8]))
idx, detail, rel, D = P4.alignment_set(ct)
print('hinge alignment set', idx, flush=True)

prof = P4.NFProfile(0.34, 0.87, 0.15, 3.0)
rr = np.linalg.norm(PTS, axis=1)
h = 1e-6
d1_fd = (prof.cs(rr + h) - prof.cs(rr - h)) / (2 * h)
d2_fd = (prof.d1(rr + h) - prof.d1(rr - h)) / (2 * h)
e1f = float(np.max(np.abs(prof.d1(rr) - d1_fd)) / np.max(np.abs(prof.d1(rr))))
e2f = float(np.max(np.abs(prof.d2(rr) - d2_fd)) / np.max(np.abs(prof.d2(rr))))
fd = dict(d1_rel=e1f, d2_rel=e2f, h=h,
          pass_=bool(e1f < 1e-6 and e2f < 1e-6))
print('FDCHECK', json.dumps(fd), flush=True)

gate_ok = all(r['pass_'] for r in rows) and idx == [44] and fd['pass_']
out = dict(gate_pass=bool(gate_ok), worst_err=worst, rows=rows,
           hinge_alignment_set=idx,
           hinge_SF=(detail[44]['S_F'] if 44 in detail else None),
           fd_check=fd)
print('GATEJSON ' + json.dumps(out))
print('GATE', 'PASS' if gate_ok else 'FAIL', 'worst err', worst,
      file=sys.stderr)
sys.exit(0 if gate_ok else 1)
