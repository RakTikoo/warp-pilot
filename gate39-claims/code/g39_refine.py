#!/usr/bin/env python3
"""Gate-39 A-2 refinement worker: python g39_refine.py <part> <nparts>
Audits the 5 stored audit_list members at J=64 and J=128.
Checkpoints to gate39/results/g39_refine_part<part>.json."""
import json
import os
import sys
import time

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate39/work')
import g39_lib as G  # noqa: E402
from g39_members import enumerate_members, audit_member  # noqa: E402

BASE = '/home/hatch/workspace/warp-pilot/'
part = int(sys.argv[1]); nparts = int(sys.argv[2])
out_path = BASE + f'gate39/results/g39_refine_part{part}.json'

conf = json.load(open(BASE + 'phase344/results/p344_confirmation.json'))
a2 = [e for e in conf['confirmations'] if e['point'] == 'A2'][0]
centre = G.Centre(a2['vS'], a2['vN'], a2['vM'], 33, m_r2=20.0)

ref364 = json.load(open(BASE + 'phase364/results/p364_refine.json'))
audit_list = ref364['audit_list']['audits']
by_id = {m['id']: m for m in enumerate_members()}
tasks = [(mid, J) for mid in audit_list for J in (64, 128)]
print('tasks', tasks, flush=True)

done = {}
if os.path.exists(out_path):
    done = json.load(open(out_path))
for i, (mid, J) in enumerate(tasks):
    if i % nparts != part:
        continue
    key = f'{mid}@J{J}'
    if key in done:
        print('skip done', key, flush=True)
        continue
    t0 = time.time()
    summ, _ = audit_member(centre, by_id[mid], J)
    summ['wall_s'] = time.time() - t0
    done[key] = summ
    with open(out_path, 'w') as f:
        json.dump(done, f)
    print(f"[{part}] {key} L_worst={summ['L_worst']:.6e} "
          f"NECw={summ['NEC_worst']:.6e} DECw={summ['DEC_worst']:.6e} "
          f"({summ['wall_s']:.0f}s)", flush=True)
print('PART DONE', part, flush=True)
