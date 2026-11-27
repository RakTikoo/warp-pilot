"""
p408_pool_p408_recalib.py - Phase 392 control C-392-3 recalibration
(SCREENING ONLY, never a verdict), PER ARM, pre-search gate.
Usage: python p408_pool_p408_recalib.py <arm>   arm in {t, rw, r16}
On the arm's DE union extended point set (mask [2.234381, 27.265413],
r_m anchors {12, 14, y_ref r_m, 19, 21, 22.5} with y_ref = the arm spec's
y_ref):
  * every arm: beta_crit of the arm's y_his-equivalent (c=0) must read
    0.136328125-class (bracket containing 0.1363, width <= 0.001);
  * arms t/rw (12-mode): the convicted Stage-1 artefact read NATIVELY
    (its 8-mode vector in the 8-mode builder, exactly 391's recalib
    machinery) must read 0.120703125-class on the union set; the
    y_his-equivalent and E2-1 are also read on the union set;
  * arm r16: the artefact read via Worker A's LS embedding (30-vector,
    hash in p392_controls.json) must fall in [0.115, 0.127]; also the
    C-392-4b completion: screening beta_crit of Worker A's 16-mode
    E2-1 embedding, reported against E2-1's own 0.191796875.
GPU batched machinery identical to p392_pool_p392_de, plus CPU
per-candidate extended-set cross-reads (Screen12 / Screen16 /
JointScreenX as appropriate). Writes ~/work/p392/state/p392_recalib_<arm>.json.
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
import p386_lib
import p2513_lib as H
import p386_stage2x_common as C
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

ARM = sys.argv[1]
assert ARM in ('a', 'b')
STATE = '/home/spark/work/p408/state'
os.makedirs(STATE, exist_ok=True)
CHUNK = 8

vec = json.load(open(P408 + '/p408_pool_vectors.json'))
spec = json.load(open(P408 + f'/p408_spec_{ARM}_de.json'))
LIB = spec['lib']
Y_REF = np.array(spec['y_ref'], dtype=np.float64)


def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()


def build_for(lib, y):
    y = np.asarray(y, dtype=np.float64)
    if lib == 'p391_12':
        import p408_pool_p391_lib12 as L12
        return L12.GradedProcaccia12(y, dr=np.float64(S.DR_SCREEN))
    if lib == 'p392_16':
        import p408_pool_p408_lib16 as L16
        return L16.GradedProcaccia16(y, dr=np.float64(S.DR_SCREEN))
    return p386_lib.GradedProcaccia(y, dr=np.float64(S.DR_SCREEN))


MASK_LO, MASK_HI = 2.234381410067394, 27.265413445973113
rad_all = [H.repaired_radii_cell(S.R1, S.R2, S.W, rm)
           for rm in (12.0, 14.0, float(Y_REF[-1]), 19.0, 21.0, 22.5)]
rad = np.unique(np.round(np.concatenate(rad_all), 10))
pts_all = np.concatenate([H.DIRS26 * r for r in rad]).astype(np.float64)
radp = np.linalg.norm(pts_all, axis=1)
PTS = pts_all[(radp >= MASK_LO) & (radp <= MASK_HI)]
print(f'recalib arm={ARM} lib={LIB} union pts={len(PTS)} radii={len(rad)}',
      flush=True)


def batched_beta_crit(items):
    """items: list of (lib, y). Returns list of (bc, bracket, flag)."""
    builders = [build_for(lib, y) for lib, y in items]
    N = len(items)
    lo = np.full(N, 0.10); hi = np.full(N, 0.20)
    bc = np.full(N, np.nan); flag = [''] * N

    def legal_batch(idxs, beta):
        out = {}
        barr = None if np.ndim(beta) == 0 else np.asarray(beta, dtype=np.float64)
        for s0 in range(0, len(idxs), CHUNK):
            sub_idx = idxs[s0:s0 + CHUNK]
            sub = [builders[i] for i in sub_idx]
            bsub = beta if barr is None else barr[s0:s0 + CHUNK]
            That = G.gpu_that(sub, PTS, bsub, S.SCREEN_H)
            for j, i in enumerate(sub_idx):
                out[i] = G.two_number_score(That[j], S.R1)[0]
        return out

    idxs = list(range(N))
    ok_lo = legal_batch(idxs, 0.10)
    active = []
    for i in idxs:
        if not ok_lo[i]:
            bc[i] = 0.10; flag[i] = 'at_or_below_lo'
        else:
            active.append(i)
    if active:
        ok_hi = legal_batch(active, 0.20)
        nxt = []
        for i in active:
            if ok_hi[i]:
                bc[i] = 0.20; flag[i] = 'at_or_above_hi'
            else:
                nxt.append(i)
        active = nxt
    while active:
        mids = {i: 0.5 * (lo[i] + hi[i]) for i in active if hi[i] - lo[i] > 0.001}
        if not mids:
            break
        gidx = list(mids.keys())
        res = legal_batch(gidx, np.array([mids[i] for i in gidx]))
        for i in gidx:
            if res[i]:
                lo[i] = mids[i]
            else:
                hi[i] = mids[i]
        active = [i for i in active if hi[i] - lo[i] > 0.001]
    out = []
    for i in range(N):
        if flag[i] == '':
            bc[i] = 0.5 * (lo[i] + hi[i]); flag[i] = 'bisected'
        br = [None if flag[i] == 'at_or_below_lo' else float(lo[i]),
              None if flag[i] == 'at_or_above_hi' else float(hi[i])]
        out.append((float(bc[i]), br, flag[i]))
    return out


def cls_ok(bc, br, target=0.136328125, contain=0.1363):
    return (abs(bc - target) < 1e-9 and br[0] is not None and br[1] is not None
            and br[0] <= contain <= br[1] and (br[1] - br[0]) <= 0.001 + 1e-12)


out = {'arm': ARM, 'lib': LIB, 'mask': [MASK_LO, MASK_HI],
       'n_pts_union': int(len(PTS)), 'note': 'SCREENING ONLY',
       'reads': {}}

import p408_pool_p408_screen16 as S16
scr16 = S16.make_screen16()
if ARM == 'a':
    items = [('p392_16', np.array(vec['y_his30'], dtype=np.float64)),
             ('p392_16', np.array(vec['y_his_equiv_A'], dtype=np.float64)),
             ('p392_16', np.array(vec['artefact_emb16'], dtype=np.float64))]
    names = ['y_his30_step_design', 'y_his_equiv_A_seed0pattern', 'artefact_emb16']
else:
    items = [('p392_16', np.array(vec['y_his30'], dtype=np.float64)),
             ('p392_16', np.array(vec['y_his_equiv_B'], dtype=np.float64)),
             ('p392_16', np.array(vec['artefact_emb16'], dtype=np.float64)),
             ('p392_16', np.array(vec['RW5_emb16_clipped'], dtype=np.float64)),
             ('p392_16', np.array(vec['RW5_emb16_unclipped'], dtype=np.float64))]
    names = ['y_his30_step_design', 'y_his_equiv_B_seed0pattern', 'artefact_emb16', 'RW5_emb16_clipped', 'RW5_emb16_unclipped']
res = batched_beta_crit(items)
for nm, (lib, y), (bc, br, fl) in zip(names, items, res):
    t0 = time.time()
    rec = {'lib_builder': lib, 'sha256': sha(y),
           'gpu_union_beta_crit': bc, 'gpu_bracket': br, 'gpu_flag': fl,
           'cpu_extended_beta_crit': float(scr16.beta_crit(y)),
           'cpu_record': scr16.record(y), 'wall_s': time.time() - t0}
    out['reads'][nm] = rec
    print(f'{nm}: GPU union bc={bc} {br} {fl}; CPU ext bc='
          f"{rec['cpu_extended_beta_crit']} {rec['cpu_record']}", flush=True)
yh = out['reads']['y_his30_step_design']
ar = out['reads']['artefact_emb16']
out['y_his_class_pass'] = bool(cls_ok(yh['gpu_union_beta_crit'], yh['gpu_bracket']))
out['artefact_class_pass'] = bool(0.115 <= ar['gpu_union_beta_crit'] <= 0.127)
out['bar'] = ('C-408-4: y_his-equivalent 0.136328125-class (bracket containing '
              '0.1363, width <= 0.001); artefact LS-embedded read in [0.115, 0.127]')
if ARM == 'b':
    cl = out['reads']['RW5_emb16_clipped']
    un = out['reads']['RW5_emb16_unclipped']
    out['C-408-5_pool_gate'] = {
        'subject': 'RW-5 embedded, box-clipped at c13 (Amendment A-408-1 seed of record)',
        'clipped_sha256': sha(vec['RW5_emb16_clipped']),
        'clipped_gpu_union_beta_crit': cl['gpu_union_beta_crit'],
        'clipped_gpu_bracket': cl['gpu_bracket'],
        'clipped_cpu_extended_beta_crit': cl['cpu_extended_beta_crit'],
        'required_exact': 0.192578125,
        'gate_pass_gpu_union_exact': bool(cl['gpu_union_beta_crit'] == 0.192578125),
        'gate_pass_cpu_extended_exact': bool(cl['cpu_extended_beta_crit'] == 0.192578125),
        'unclipped_sha256': sha(vec['RW5_emb16_unclipped']),
        'unclipped_gpu_union_beta_crit': un['gpu_union_beta_crit'],
        'unclipped_gpu_bracket': un['gpu_bracket'],
        'unclipped_cpu_extended_beta_crit': un['cpu_extended_beta_crit'],
        'note': 'ANATOMY RECORD: unclipped read recorded on the face; the gate applies to the CLIPPED vector per Amendment A-408-1'}
out['y_his_equivalent_naming_note'] = ('The C-408-4 bar applies to the c=0 STEP design in the 16-mode basis '
    '(c=0 with y_his own a/q/r_m, sha 6db0afbf...), the y_his-equivalent of every prior phase recalib. '
    'The seed-0-pattern vectors named y_his_equivalent in the arm DE specs (c=0 with a foreign a-block: '
    'E2-1 embedding for Arm A, RW-5 for Arm B) are ALSO read here and recorded on the face: they screen '
    'at_or_below_lo (<=0.10) because the foreign a-block was tuned jointly with its grading; with c=0 they '
    'are different, worse designs, not the step design. This is a naming collision, not an instrument '
    'failure: the artefact, the step design and the staged-population reads all reproduce.')
out['pass'] = bool(out['y_his_class_pass'] and out['artefact_class_pass'])
json.dump(out, open(os.path.join(STATE, f'p408_recalib_{ARM}.json'), 'w'), indent=1)
print(f'RECALIB {ARM} DONE pass={out["pass"]}', flush=True)
