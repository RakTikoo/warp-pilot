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

ARM = 'a'
STATE = '/home/spark/work/p408/state'
os.makedirs(STATE, exist_ok=True)
CHUNK = 8
vec = json.load(open(P408 + '/p408_pool_vectors.json'))
spec = json.load(open(P408 + '/p408_spec_a_de.json'))
LIB = spec['lib']
Y_REF = np.array(spec['y_ref'], dtype=np.float64)

def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()

def build_for(lib, y):
    y = np.asarray(y, dtype=np.float64)
    import p408_pool_p408_lib16 as L16
    return L16.GradedProcaccia16(y, dr=np.float64(S.DR_SCREEN))

MASK_LO, MASK_HI = 2.234381410067394, 27.265413445973113
rad_all = [H.repaired_radii_cell(S.R1, S.R2, S.W, rm)
           for rm in (12.0, 14.0, float(Y_REF[-1]), 19.0, 21.0, 22.5)]
rad = np.unique(np.round(np.concatenate(rad_all), 10))
pts_all = np.concatenate([H.DIRS26 * r for r in rad]).astype(np.float64)
radp = np.linalg.norm(pts_all, axis=1)
PTS = pts_all[(radp >= MASK_LO) & (radp <= MASK_HI)]
print(f'gen0check union pts={len(PTS)}', flush=True)
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



staged = json.load(open('/home/spark/work/p408/state/p392_pool_r16_de_state_staged.json'))
items = [('p392_16', np.array(y, dtype=np.float64)) for y in staged['pop']]
res = batched_beta_crit(items)
devs = []
rows = []
for i, ((bc, br, fl), stored_bc, stored_br) in enumerate(zip(res, staged['beta_crit'], staged['brackets'])):
    dev = abs(bc - stored_bc)
    devs.append(dev)
    rows.append({'idx': i, 'reread_bc': bc, 'reread_bracket': br, 'flag': fl,
                 'stored_bc': stored_bc, 'stored_bracket': stored_br, 'abs_dev': dev,
                 'bracket_equal': br == stored_br})
out = {'item': 'Phase 408 Arm A resumption cross-check: independent re-read of all 64 staged members on the resumed DE union instrument (GPU batched, identical set n_pts=3640)',
       'n_pts': int(len(PTS)), 'n_members': 64,
       'best_reread': max(r['reread_bc'] for r in rows),
       'best_stored': staged['best_beta_crit'],
       'best_exact_match': bool(max(r['reread_bc'] for r in rows) == staged['best_beta_crit'] == 0.191015625),
       'max_abs_dev': max(devs), 'n_exact': sum(1 for d in devs if d == 0.0),
       'n_brackets_equal': sum(1 for r in rows if r['bracket_equal']),
       'rows': rows, 'note': 'SCREENING ONLY'}
json.dump(out, open(os.path.join(STATE, 'p408_gen0check_a.json'), 'w'), indent=1)
print(f"GEN0CHECK DONE best={out['best_reread']} maxdev={out['max_abs_dev']} n_exact={out['n_exact']}/64 brackets_equal={out['n_brackets_equal']}/64", flush=True)
