#!/usr/bin/env python3
"""Gate-39 A-1 scan worker: python g39_scan.py <part> <nparts>
Checkpoints per member to gate39/results/g39_scan_part<part>.json."""
import json
import os
import sys
import time

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate39/work')
import g39_lib as G  # noqa: E402
from g39_members import enumerate_members, audit_member  # noqa: E402

BASE = '/home/hatch/workspace/warp-pilot/'
part = int(sys.argv[1]); nparts = int(sys.argv[2])
out_path = BASE + f'gate39/results/g39_scan_part{part}.json'

conf = json.load(open(BASE + 'phase344/results/p344_confirmation.json'))
a2 = [e for e in conf['confirmations'] if e['point'] == 'A2'][0]
centre = G.Centre(a2['vS'], a2['vN'], a2['vM'], 33, m_r2=20.0)

stored = json.load(open(BASE + 'phase364/results/p364_scan.json'))
mems = enumerate_members()
assert {m['id'] for m in mems} == set(stored.keys()), (
    {m['id'] for m in mems} ^ set(stored.keys()))
print(f'name set verified: {len(mems)} members == p364_scan keys', flush=True)

done = {}
if os.path.exists(out_path):
    done = json.load(open(out_path))
for i, mem in enumerate(mems):
    if i % nparts != part:
        continue
    if mem['id'] in done:
        print('skip done', mem['id'], flush=True)
        continue
    t0 = time.time()
    summ, _ = audit_member(centre, mem, 32)
    summ['wall_s'] = time.time() - t0
    done[mem['id']] = summ
    with open(out_path, 'w') as f:
        json.dump(done, f)
    print(f"[{part}] {mem['id']} L_worst={summ['L_worst']:.6e} "
          f"rho={summ['min_rho']:.4e} infl={summ['n_floor_infeasible']} "
          f"({summ['wall_s']:.0f}s)", flush=True)
print('PART DONE', part, flush=True)
