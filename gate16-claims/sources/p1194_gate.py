#!/usr/bin/env python3
"""p1194_gate.py -- P119-4 machinery gate (run record S1).
Reproduce the seven unique corpus configurations' stored EoM
max/medians within 1e-6 via p1015_lib.canonical_terms, and the
hinge best's alignment set = {44}. Writes p1194_gate.json."""
import json
import os
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase119/work')
import p1194_lib as P4  # noqa: E402
import p1015_lib as H   # noqa: E402
import p761_lib as L    # noqa: E402

W = '/home/hatch/workspace/warp-pilot'
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

hinge = raw['best_B']
ct = H.canonical_terms(wall, PTS, np.asarray(hinge['z_full'][:8]))
idx, detail, rel, D = P4.alignment_set(ct)
print('hinge alignment set', idx, 'detail', detail, flush=True)
gate_ok = all(r['pass_'] for r in rows) and idx == [44]
out = dict(gate_pass=bool(gate_ok), worst_err=worst, rows=rows,
           hinge_alignment_set=idx, hinge_alignment_detail=detail,
           hinge_SF=(detail[44]['S_F'] if 44 in detail else None))
print('GATEJSON ' + json.dumps(out))
print('GATE', 'PASS' if gate_ok else 'FAIL', 'worst err', worst,
      file=sys.stderr)
sys.exit(0 if gate_ok else 1)
