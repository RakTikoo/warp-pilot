"""
wb_audit.py — GATE-10 W-B pole-inclusive audit of the fresh reconstructions.

Grid (registered in GATE10.md / wb_lib.audit_grid, before running): uniform
in mu = cos th, 161 pts with BOTH pole endpoints exactly, plus bands
th in [pi-0.15, pi] (41 pts) and [0, 0.15] (21 pts). Pole values are
computed AT th = 0 and th = pi as evaluated points.

For each solved coefficient set: per-point stress, Hawking-Ellis type,
worst-observer DEC margin (Eq.(35) form), eigenvalue margins, sampled-null
NEC min and sampled-observer DEC at the binding point, closure max|[h]|
on the audit grid, and an h-ladder (h = 0.02 / 0.01 / 0.005 + 4th-order
h = 0.01) at the binding angle.

Usage: wb_audit.py x lam L   (reads results/wb_solve_x{x}_L{L}.json)
Writes results/wb_audit_x{x}_L{L}.json
"""
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb_lib as W

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")


def audit_point(args):
    """Grid read on the validated analytic-gradient path (wb_validate_fast:
    margins agree with the FD path to <= 5e-9)."""
    x, lam, p, L, th, h, order = args
    r = W.sample_one_fast((x, lam, p, L, float(th), h, order))
    s = W.lanczos(r[1], r[3])
    m, t = W.phi_HE(*s)
    ed = W.eig_data(*s)
    dh = r[0] - r[2]
    return dict(th=float(th), stress=list(s), margin=m, type=t,
                disc=ed["disc"], eig_margin=float(min(ed["margins"])),
                null_min=W.sampled_null_min(*s), max_h=float(np.max(np.abs(dh))))


def main():
    x, lam, L = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
    sol = json.load(open(os.path.join(RESULTS, f"wb_solve_x{x}_L{L}.json")))
    p = [float(v) for v in sol["p"]]
    grid = W.audit_grid()
    t0 = time.time()
    with Pool(2) as pool:
        rows = pool.map(audit_point,
                        [(x, lam, p, L, th, 0.01, 2) for th in grid])
    worst = min(rows, key=lambda r: r["margin"])
    pole = [r for r in rows if abs(r["th"] - np.pi) < 1e-12][0]
    front = [r for r in rows if abs(r["th"]) < 1e-12][0]
    # ladder at the binding angle on the FD path (the re-gate-validated
    # machinery), plus FD reads at both poles at h = 0.01
    def fd_point(th, hh, oo):
        r = W.sample_one((x, lam, p, L, float(th), hh, oo))
        s = W.lanczos(r[1], r[3])
        m, t = W.phi_HE(*s)
        return dict(margin=m, type=t, stress=list(s))
    ladder = {}
    for hh, oo in ((0.02, 2), (0.01, 2), (0.005, 2), (0.01, 4)):
        ladder[f"h{hh}_o{oo}"] = fd_point(worst["th"], hh, oo)
    fd_poles = dict(rear=fd_point(np.pi, 0.01, 2), front=fd_point(0.0, 0.01, 2),
                    bind=fd_point(worst["th"], 0.01, 2))
    # FD closure on a 61-point grid over [0, pi] (both poles included)
    with Pool(2) as pool:
        fd_rows = pool.map(W.sample_one,
                           [(x, lam, p, L, float(th), 0.01, 2)
                            for th in np.linspace(0.0, np.pi, 61)])
    fd_closure = float(max(np.max(np.abs(r[0] - r[2])) for r in fd_rows))
    out = dict(x=x, lam=lam, L=L, n_grid=len(rows),
               worst_margin=worst["margin"], theta_bind=worst["th"],
               pole_margin=pole["margin"], pole_type=pole["type"],
               front_pole_margin=front["margin"], front_type=front["type"],
               all_type_I=bool(all(r["type"] == 1 for r in rows)),
               min_disc=float(min(r["disc"] for r in rows)),
               min_eig_margin=float(min(r["eig_margin"] for r in rows)),
               min_null=float(min(r["null_min"] for r in rows)),
               sampled_dec_at_bind=W.sampled_dec_min(*worst["stress"]),
               max_h_audit_grid=float(max(r["max_h"] for r in rows)),
               ladder=ladder, fd_poles=fd_poles, fd_closure_61=fd_closure,
               rows=rows,
               seconds=time.time() - t0)
    fn = os.path.join(RESULTS, f"wb_audit_x{x}_L{L}.json")
    json.dump(out, open(fn, "w"), indent=1)
    print(f"x={x} L={L}: worst={out['worst_margin']:+.6e} at th={out['theta_bind']:.4f} "
          f"pole={out['pole_margin']:+.6e} front={out['front_pole_margin']:+.6e} "
          f"allI={out['all_type_I']} max_h={out['max_h_audit_grid']:.3e} "
          f"({out['seconds']:.0f}s) -> {fn}", flush=True)


if __name__ == "__main__":
    main()
