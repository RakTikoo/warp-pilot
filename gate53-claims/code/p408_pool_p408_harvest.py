"""
p408_pool_p408_harvest.py - Phase 392 harvest (SCREENING ONLY, never a
verdict), generalised from p386_stage2x_harvest.py. Usage:
  python p408_pool_p408_harvest.py <spec.json>
spec: {"tag": str, "lib": "p391_12"|"p392_16",
       "candidates": [{"provenance": str, "y": [n],
                       "source_beta_crit_screening": float|null}, ...],
       "y_ref": [n] (control vector re-read and recorded),
       "top_k": int (default 6), "distinct_min": float (default 0.05)}
Every candidate is re-evaluated on the CPU per-candidate-r_m EXTENDED
screening set (single consistent ranking), the distinctness filter
(pairwise ||dy||_inf >= distinct_min over the (c,a) block = all but the
last two coordinates) is applied greedily in ranked order, top <= top_k
kept with sha256(float64 tobytes) hashes. Writes
~/work/p408/state/<tag>_harvest.json.
"""
import os, sys, time, json, hashlib
import numpy as np

POOL = '/home/spark/work/p386/warp-pilot'
P408 = POOL + '/phase408/work'
for p in [P408, POOL, POOL + '/phase386/work', POOL + '/phase251/work',
          POOL + '/phase50', POOL + '/gate6', POOL + '/phase63']:
    sys.path.insert(0, p)
os.environ.setdefault('OMP_NUM_THREADS', '4')
os.environ.setdefault('P386_CONSTR_DR', '2.5e-4')
os.environ.setdefault('P408_CONSTR_DR', '2.5e-4')

spec = json.load(open(sys.argv[1]))
TAG, LIB = spec['tag'], spec.get('lib', 'p386')
TOPK = int(spec.get('top_k', 6))
DMIN = float(spec.get('distinct_min', 0.05))
STATE = '/home/spark/work/p408/state'

if LIB == 'p391_12':
    import p408_pool_p391_screen12 as S12
    scr = S12.make_screen12()
elif LIB == 'p392_16':
    import p408_pool_p408_screen16 as S16
    scr = S16.make_screen16()
else:
    import p386_stage2x_common as C
    scr = C.make_screen()


def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()


cands = []
for c in spec['candidates']:
    cands.append({'provenance': c['provenance'],
                  'y': [float(v) for v in c['y']],
                  'source_beta_crit_screening': c.get('source_beta_crit_screening'),
                  'sha256': sha(c['y'])})

t0 = time.time()
for c in cands:
    y = np.array(c['y'], dtype=np.float64)
    bc = scr.beta_crit(y)
    c['cpu_beta_crit_screening'] = float(bc)
    c['cpu_record'] = scr.record(y)
    print(f"{c['provenance']}: cpu_bc={bc} record={c['cpu_record']}", flush=True)

ranked = sorted(cands, key=lambda c: -c['cpu_beta_crit_screening'])
harvest = []
for c in ranked:
    y = np.array(c['y'], dtype=np.float64)
    ok = True
    for h in harvest:
        dy = np.max(np.abs(y[:-2] - np.array(h['y'], dtype=np.float64)[:-2]))
        if dy < DMIN:
            ok = False
            break
    if ok:
        harvest.append(c)
    if len(harvest) >= TOPK:
        break

y_ref = np.array(spec['y_ref'], dtype=np.float64)
out = {'note': 'SCREENING ONLY (extended set, CPU per-candidate-r_m ranking)',
       'tag': TAG, 'lib': LIB,
       'all_candidates': ranked, 'harvest_top': harvest,
       'y_ref_control': {'y': [float(v) for v in y_ref], 'sha256': sha(y_ref),
                         'cpu_beta_crit_screening': float(scr.beta_crit(y_ref)),
                         'cpu_record': scr.record(y_ref)},
       'wall_s': time.time() - t0}
json.dump(out, open(os.path.join(STATE, f'{TAG}_harvest.json'), 'w'), indent=1)
print(f"HARVEST DONE n={len(harvest)} wall={out['wall_s']:.0f}s", flush=True)
for h in harvest:
    print(f"  {h['cpu_beta_crit_screening']:.5f} {h['sha256'][:8]} {h['provenance']}",
          flush=True)
