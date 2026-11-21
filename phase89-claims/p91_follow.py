"""p91_follow.py — P9-1 follow-ups (Failure Protocol):
(1) corrected exact-isolated-shell edge audit (shell centred at
    d*zhat, background off — the first run centred it at the origin
    by mistake, so its points sampled empty space; rerun fixed);
(2) PG-consistent edge worst-point location per h;
(3) areal moving beta=0.02 spot check at h=0.05 (third resolution).
float64, system python3.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase5')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase7')
import h4_resolved_shell as h4      # noqa: E402
from p74_auditor import einstein_at_points_td  # noqa: E402
import p91_chain as base            # noqa: E402  (builders; reruns main? no - see guard)

# p91_chain runs its main body on import; to avoid that, this script
# is only ever run after p91_chain and re-implements the two small
# builders it needs via base's functions with explicit centres.
OUT = '/home/hatch/workspace/warp-pilot/phase9/results/p91_follow.json'
out = {}
t0 = time.time()

dirs = h4.fib_dirs(26)
edge_rad = np.linspace(7.5, 9.2, 18)
edge_rel = np.concatenate([dirs * rr for rr in edge_rad]).astype(np.float64)
edge_r = np.linalg.norm(edge_rel, axis=1)
ZHAT = np.array([0.0, 0.0, 1.0])


def make_pg_centred(d, bg_on):
    centre = d * ZHAT

    def gtfunc(t, pts):
        alpha, W, _, r_rel = base.pg_fields(pts, centre, True, bg_on)
        P = len(pts)
        g = np.zeros((P, 4, 4), dtype=np.float64)
        g[:, 0, 0] = -alpha ** 2 + np.sum(W ** 2, axis=1)
        g[:, 0, 1:] = W; g[:, 1:, 0] = W
        for i in range(3):
            g[:, i + 1, i + 1] = 1.0
        return g
    return gtfunc


for d in (50.0,):
    pts_e = edge_rel + (d * ZHAT)[None, :]
    for name, bg_on in (('pg_isolated_exact_centred', False),
                        ('pg_consistent', True)):
        gt = make_pg_centred(d, bg_on)
        row = {}
        for h in (0.1, 0.05, 0.025):
            _, _, margins = einstein_at_points_td(gt, 0.0, pts_e, h=h, ht=h)
            nec = margins['nec']
            cav = edge_r < 9.0
            j = int(np.argmin(np.where(cav, nec, np.inf)))
            row[f'h={h}'] = {
                'cavity_worst_nec': float(nec[j]),
                'worst_r': float(edge_r[j]),
                'worst_dir': (edge_rel[j] / edge_r[j]).tolist(),
                'interior_r<=8.41_worst_nec': float(np.min(nec[edge_r <= 8.41])),
                'edge_r8.9_worst_nec': float(np.min(nec[np.isclose(edge_r, 8.9, atol=0.051)]))}
            print(f"[{name} d={d:g}] h={h}: cav={row[f'h={h}']['cavity_worst_nec']:+.4e} "
                  f"@r={row[f'h={h}']['worst_r']:.2f} int={row[f'h={h}']['interior_r<=8.41_worst_nec']:+.4e} "
                  f"@8.9={row[f'h={h}']['edge_r8.9_worst_nec']:+.4e}")
        out[f'{name} d={d:g}'] = row
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=1, default=float)

# areal moving h=0.05
pts_rel = h4.sample_points(3.5)
for d in (50.0, 100.0):
    pts = pts_rel + (d * ZHAT)[None, :]
    gt = base.make_areal_moving(0.02, d)
    _, _, regs = base.audit_full(gt, pts, pts_rel, 0.05)
    out[f'areal_moving_h0.05 d={d:g}'] = regs
    print(f"[MOVE areal d={d:g}] h=0.05: cavity NEC={regs['cavity']['nec']:+.4e} "
          f"core NEC={regs['core']['nec']:+.4e} coreTypeI={regs['core']['typeI_frac']:.3f}")
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=1, default=float)

out['runtime_s'] = time.time() - t0
with open(OUT, 'w') as f:
    json.dump(out, f, indent=1, default=float)
print('done', out['runtime_s'])
