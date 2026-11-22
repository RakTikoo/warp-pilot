"""Dense corrected l=0 profiles from the F4-2b action route (elim_at),
with per-point reliability diagnostics.  Shard worker: each shard
appends JSONL records to work_cert/ell0_shard<k>.jsonl (checkpointed
per point; the done-set is read from ALL shard files, so reruns and
re-gridding never recompute a finished point).

Work order is by priority: inner [-4,4] @ 0.01 (offset +0.0037),
band flanks [1.15,1.65] U [1.90,2.40] @ 0.005, mid [+-4..10] @ 0.05,
outer [+-10..62] @ 0.1.  Diagnostics per point: D (pole denominator,
D(r*)=0), Qb (elimination pivot, ~ D), p_ind vs p_f42 = 2 Xi / D
(their ratio is a constant 0.5/1.5 convention factor on healthy
points; scatter of the ratio flags FD breakdown), ELA_resid_max
(EL_A identity residual; ~1e-4 on healthy points), R01, mB.
"""
import glob
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase4')
import p42b_ell0_indep as p42b   # noqa: E402

OUTDIR = '/home/hatch/workspace/warp-pilot/gate3/work_cert'


def master_grid():
    segs = [np.arange(-4.0, 4.0001, 0.01) + 0.0037,
            np.arange(1.15, 1.6501, 0.005) + 0.0037,
            np.arange(1.90, 2.4001, 0.005) + 0.0037,
            np.arange(-10.0, -3.999, 0.05), np.arange(4.0, 10.001, 0.05),
            np.arange(-62.0, -9.999, 0.1), np.arange(10.0, 62.001, 0.1)]
    return np.unique(np.round(np.concatenate(segs), 6))


def priority_order(grid):
    def key(r):
        a = abs(r)
        if a <= 4.0:
            return (0, a)
        if a <= 10.0:
            return (1, a)
        return (2, a)
    return sorted(grid, key=key)


def main():
    shard = int(sys.argv[1])
    nshards = int(sys.argv[2])
    path = os.path.join(OUTDIR, f'ell0_shard{shard}.jsonl')
    done = set()
    for p in glob.glob(os.path.join(OUTDIR, 'ell0_shard*.jsonl')):
        with open(p) as fh:
            for line in fh:
                try:
                    done.add(json.loads(line)['r'])
                except Exception:  # noqa: BLE001
                    pass
    grid = priority_order(master_grid())[shard::nshards]
    todo = [r for r in grid if float(r) not in done]
    print(f'shard {shard}: {len(todo)} to compute '
          f'({len(grid) - len(todo)} already done)', flush=True)
    t0 = time.time()
    with open(path, 'a') as fh:
        for i, r in enumerate(todo):
            r = float(r)
            try:
                d = p42b.elim_at(r)
                rec = dict(r=r, K0=d['K0'], G0=d['G0'], M0=d['M0'],
                           D=d['D'], Qb=d['Qb'], p_ind=d['p_ind'],
                           p_f42=d['p_f42'], ELA_resid_max=
                           d['ELA_resid_max'], R01=d['R01'],
                           mB=d['mB'])
            except Exception as exc:  # noqa: BLE001
                rec = dict(r=r, error=str(exc))
            fh.write(json.dumps(rec) + '\n')
            fh.flush()
            if (i + 1) % 50 == 0:
                print(f'shard {shard}: {i + 1}/{len(todo)} '
                      f'({time.time() - t0:.0f}s)', flush=True)
    print(f'shard {shard}: DONE in {time.time() - t0:.0f}s',
          flush=True)


if __name__ == '__main__':
    main()
