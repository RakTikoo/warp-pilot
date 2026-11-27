"""
p408_pool_p408_validate.py - Phase 392 GPU validation (SCREENING ONLY).
Usage: python p408_pool_p408_validate.py <mode>   mode in {a, b}  (C-408-6: a = Arm A spot >=5 incl. staged best_y; b = Arm B full >=20 incl. y_his-equivalent + clipped RW-5 embedding, widened box)
Hybrid GPU evaluator vs pool-CPU clone (p503_lib.fast_audit algebra via
the arm's CPU screen) on the arm's DE union extended point set:
  * p391_12 (C-392-4 carry-over spot re-validation): >= 5 shared
    candidates incl. E2-1;
  * p392_16 (C-392-4c): >= 20 shared candidates incl. the
    y_his-equivalent 30-vector.
Bars (391's): worst margins agree <= 1e-7 absolute at beta = 0.13, 0.145;
beta_crit brackets agree for a 5-candidate subset (GPU union bisection
vs CPU per-candidate-r_m extended set, centres within 0.001).
Writes ~/work/p392/state/p392_validate_<lib>.json. On failure the caller
falls back to the pool-CPU clone for that arm and records it.
Vectors from phase408/work/p408_pool_vectors.json (pool copy).
"""
import os, sys, time, json, hashlib
import numpy as np
from concurrent.futures import ThreadPoolExecutor

POOL = '/home/spark/work/p386/warp-pilot'
P408 = POOL + '/phase408/work'
for p in [P408, POOL, POOL + '/phase386/work', POOL + '/phase251/work',
          POOL + '/phase50', POOL + '/gate6', POOL + '/phase63']:
    sys.path.insert(0, p)
os.environ.setdefault('P386_CONSTR_DR', '2.5e-4')
os.environ.setdefault('P408_CONSTR_DR', '2.5e-4')
os.environ.setdefault('OMP_NUM_THREADS', '2')
import p386_screen as S
import p386_gpu as G
import p2513_lib as H
import p503_lib as L
import torch as _torch


def _stack_exports_padded(builders):
    exps = []
    for name in ('_a', '_m', '_S'):
        raw = [(np.asarray(getattr(b, name).x), np.asarray(getattr(b, name).c))
               for b in builders]
        N = max(len(t) for t, _ in raw)
        ts, cs = [], []
        for t, c in raw:
            if len(t) < N:
                t = np.concatenate([t, np.full(N - len(t), t[-1])])
                c = np.concatenate([c, np.zeros((4, N - 1 - c.shape[1]))], axis=1)
            ts.append(_torch.tensor(t, dtype=G.DT, device=G.DEV))
            cs.append(_torch.tensor(c, dtype=G.DT, device=G.DEV))
        exps.append((_torch.stack(ts), _torch.stack(cs)))
    rmax = _torch.tensor(np.array([float(b.rg[-1]) for b in builders]),
                         dtype=G.DT, device=G.DEV)
    return exps, rmax


G.stack_exports = _stack_exports_padded

MODE = sys.argv[1]
assert MODE in ('a', 'b')
LIB = 'p392_16'
STATE = '/home/spark/work/p408/state'
os.makedirs(STATE, exist_ok=True)
CHUNK = 8
vec = json.load(open(P408 + '/p408_pool_vectors.json'))

import p408_pool_p408_lib16 as LB
import p408_pool_p408_screen16 as SC
BUILD = lambda y: LB.GradedProcaccia16(np.asarray(y, dtype=np.float64), dr=np.float64(S.DR_SCREEN))
scr = SC.make_screen16()
if MODE == 'a':
    spec = json.load(open(P408 + '/p408_spec_a_de.json'))
    named = [('y_his_equiv_A', vec['y_his_equiv_A']),
             ('staged_best_y', vec['staged_best_y'])] + \
            [(f'staged_pop{i+1}', v) for i, v in enumerate(vec['staged_pop_sample'])]
    rng = np.random.default_rng(408)
    n_rand = 0
else:
    spec = json.load(open(P408 + '/p408_spec_b_de.json'))
    named = [('y_his_equiv_B', vec['y_his_equiv_B']),
             ('RW5_emb_clipped', vec['RW5_emb16_clipped']),
             ('RW5_emb_unclipped', vec['RW5_emb16_unclipped']),
             ('artefact_emb16', vec['artefact_emb16'])]
    rng = np.random.default_rng(40816)
    n_rand = 16

LO = np.array(spec['lo'], dtype=np.float64)
HI = np.array(spec['hi'], dtype=np.float64)
Y_REF = np.array(spec['y_ref'], dtype=np.float64)
cands = [(nm, np.array(v, dtype=np.float64)) for nm, v in named]
for i in range(n_rand):
    cands.append((f'rand{i}', LO + (HI - LO) * rng.random(len(LO))))
print(f'validation lib={LIB} candidates={len(cands)}', flush=True)

MASK_LO, MASK_HI = 2.234381410067394, 27.265413445973113
rad_all = [H.repaired_radii_cell(S.R1, S.R2, S.W, rm)
           for rm in (12.0, 14.0, float(Y_REF[-1]), 19.0, 21.0, 22.5)]
rad = np.unique(np.round(np.concatenate(rad_all), 10))
pts_all = np.concatenate([H.DIRS26 * r for r in rad]).astype(np.float64)
radp = np.linalg.norm(pts_all, axis=1)
PTS = pts_all[(radp >= MASK_LO) & (radp <= MASK_HI)]
print(f'union pts={len(PTS)}', flush=True)

ys = [c[1] for c in cands]
with ThreadPoolExecutor(max_workers=8) as ex:
    builders = list(ex.map(BUILD, ys))

out = {'mode': MODE, 'lib': LIB, 'n_candidates': len(cands), 'n_pts': int(len(PTS)),
       'candidate_names': [c[0] for c in cands],
       'candidate_sha256': [hashlib.sha256(y.tobytes()).hexdigest() for y in ys],
       'scores': [], 'note': 'SCREENING ONLY'}
maxdiff = 0.0
for beta in (0.13, 0.145):
    t0 = time.time()
    gpu_worst = []
    for s0 in range(0, len(ys), CHUNK):
        sub = builders[s0:s0 + CHUNK]
        That = G.gpu_that(sub, PTS, float(beta), S.SCREEN_H)
        for j in range(len(sub)):
            gpu_worst.append(G.two_number_score(That[j], S.R1)[1])
    cpu_worst = []
    for b in builders:
        m = L.fast_audit(b.metric_factory(float(beta)), PTS, S.SCREEN_H)
        cpu_worst.append(G.two_number_score(m['That'], S.R1)[1])
    diffs = [abs(float(g) - float(c)) if (g is not None and c is not None)
             else None for g, c in zip(gpu_worst, cpu_worst)]
    finite = [d for d in diffs if d is not None]
    if finite:
        maxdiff = max(maxdiff, max(finite))
    out['scores'].append({'beta': beta, 'cpu_worst': cpu_worst,
                          'gpu_worst': gpu_worst, 'abs_diff': diffs,
                          'max_abs_diff': max(finite) if finite else None,
                          'wall_s': time.time() - t0})
    print(f'beta={beta} max|dWorst|={max(finite) if finite else None} '
          f'wall={time.time()-t0:.1f}s', flush=True)
out['max_abs_diff_overall'] = maxdiff
out['margins_pass'] = bool(maxdiff <= 1e-7)


def gpu_bc(y):
    b = BUILD(y)

    def legal(beta):
        That = G.gpu_that([b], PTS, float(beta), S.SCREEN_H)
        return G.two_number_score(That[0], S.R1)[0]
    if not legal(0.10):
        return 0.10, [None, 0.10], 'at_or_below_lo'
    if legal(0.20):
        return 0.20, [0.20, None], 'at_or_above_hi'
    lo, hi = 0.10, 0.20
    while hi - lo > 0.001:
        mid = 0.5 * (lo + hi)
        if legal(mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), [lo, hi], 'bisected'


out['beta_crit_agreement'] = []
all_agree = True
for name, y in cands[:5]:
    t0 = time.time()
    gbc, gbr, gfl = gpu_bc(y)
    cbc = scr.beta_crit(y)
    crec = scr.record(y)
    agree = bool(abs(float(gbc) - float(cbc)) <= 0.001)
    all_agree = all_agree and agree
    out['beta_crit_agreement'].append(
        {'name': name, 'gpu_bc': float(gbc), 'gpu_bracket': gbr, 'gpu_flag': gfl,
         'cpu_bc': float(cbc), 'cpu_record': crec, 'agree_within_0.001': agree,
         'wall_s': time.time() - t0})
    print(f'bc {name}: gpu={gbc} {gbr} cpu={cbc} {crec} agree={agree}', flush=True)
out['brackets_pass'] = bool(all_agree)
out['pass'] = bool(out['margins_pass'] and out['brackets_pass'])
out['bar'] = 'worst margins agree <= 1e-7; beta_crit brackets agree (centres <= 0.001)'
json.dump(out, open(os.path.join(STATE, f'p408_validate_{MODE}.json'), 'w'), indent=1)
print(f'VALIDATE {LIB} DONE pass={out["pass"]} max_abs_diff={maxdiff}', flush=True)
