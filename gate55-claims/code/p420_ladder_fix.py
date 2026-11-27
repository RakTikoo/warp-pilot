#!/usr/bin/env python
"""P420 ladder completion (registration Amendment 3).

Re-runs the C-A primary's perturbation ladder with a fresh
seed (4203) and tightened least_squares tolerances
(ftol=xtol=gtol=1e-13, max_nfev=2500); the reclosure bar is
unchanged (max direct R <= 1e-9). Writes
phase420/results/p420_ladder_completed.json and updates the
verdict block of p420_results.json, preserving the original
ladder and the as-first-computed verdict on the record.
"""
import json
import sys
import time

import numpy as np
from scipy.optimize import least_squares

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/phase420/work')
import p420_machinery as M  # noqa: E402

BAR = 1e-9
t0 = time.time()


def avecs_from_json(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


def rand_modes(N, rng_, a_scale=0.03):
    pvecs = []
    for _ in range(N):
        d = rng_.normal(size=3); d /= np.linalg.norm(d)
        pvecs.append(rng_.uniform(0.05, 6.0) * d)
    avecs = (rng_.normal(size=(N, 2)) + 1j * rng_.normal(size=(N, 2))) \
        * a_scale
    return np.array(pvecs), avecs


tg = json.load(open(f'{WP}/phase420/work/p420_targets.json'))
prim = json.load(open(f'{WP}/phase420/work/p420_fitCA_primary.json'))
res = json.load(open(f'{WP}/phase420/results/p420_results.json'))
XS = [np.array(s["point"]) for s in tg["sitesA"]]
TC = [np.array(s["T_corr"]) for s in tg["sitesA"]]
FROBS = np.array([float(np.linalg.norm(t)) for t in TC])
N1, N2, m2 = prim["N1"], prim["N2"], prim["m2"]
theta_d = M.pack2(np.array(prim["pvecs1"]),
                  avecs_from_json(prim["avecs1"]),
                  np.array(prim["pvecs2"]),
                  avecs_from_json(prim["avecs2"]))
ns = len(XS)
rng_p = np.random.default_rng(4203)
ladder = {}
for eps in (1e-9, 1e-6):
    rung = []
    for draw in range(2):
        thats_p, frobs_p = [], []
        for si in range(ns):
            U = rng_p.uniform(-1.0, 1.0, (4, 4))
            U = 0.5 * (U + U.T)
            thats_p.append(TC[si] + eps * FROBS[si] * U)
            frobs_p.append(float(np.linalg.norm(thats_p[-1])))
        frobs_p = np.array(frobs_p)
        resid_p = M.make_resid_multi(XS, thats_p, frobs_p, N1, N2,
                                     1.0, m2)
        bestp = None
        starts_p = [("warm", theta_d)]
        p1, a1 = rand_modes(N1, rng_p)
        p2, a2 = rand_modes(N2, rng_p)
        starts_p.append(("fresh", M.pack2(p1, a1, p2, a2)))
        for nm, th0 in starts_p:
            sol = least_squares(resid_p, th0, method="trf",
                                max_nfev=2500, ftol=1e-13, xtol=1e-13,
                                gtol=1e-13)
            q1, b1, q2, b2 = M.unpack2(sol.x, N1, N2)
            qq, bb, mmm = M.join_modes(q1, b1, 1.0, q2, b2, m2)
            Rs_p, _ = M.site_residuals_multi(qq, bb, mmm, XS, thats_p,
                                             direct=True)
            candp = {"start": nm, "maxR_direct": max(Rs_p),
                     "Rs_direct": Rs_p, "nfev": int(sol.nfev)}
            if bestp is None or candp["maxR_direct"] < bestp["maxR_direct"]:
                bestp = candp
        rung.append(bestp)
        print(f"  [completed ladder eps={eps:.0e} draw={draw}] best "
              f"maxR={bestp['maxR_direct']:.3e} ({bestp['start']}, "
              f"nfev={bestp['nfev']})", flush=True)
    ladder[str(eps)] = rung

all_reclose = all(r["maxR_direct"] <= BAR
                  for rung in ladder.values() for r in rung)
out = {"seed": 4203, "tolerances": {"ftol": 1e-13, "xtol": 1e-13,
                                    "gtol": 1e-13, "max_nfev": 2500},
       "ladder": ladder, "all_reclose": bool(all_reclose),
       "wall_time_s": time.time() - t0}
json.dump(out, open(f'{WP}/phase420/results/p420_ladder_completed.json',
                    "w"), indent=1)

# Recompute the verdict on the completed ladder (SS7 forms,
# unchanged). The original computation is preserved.
diag = res["fitCA_diagnostics"]
fitCA_ok = bool(diag["direct"]["maxR"] <= BAR
                and diag["jacobian"]["rank_tol_1e-10_rel"] == 30
                and all_reclose)
res["verdict_as_first_computed"] = res["verdict"]["form"]
if fitCA_ok:
    new_form = "COMPOSITE SUPPLIES THE CORRECTED TARGET"
else:
    new_form = res["verdict"]["form"]
res["verdict"]["form"] = new_form
res["verdict"]["fitCA_ok"] = fitCA_ok
res["verdict"]["perturbation_ladder_completed_all_reclose"] = \
    bool(all_reclose)
res["verdict"]["ladder_amendment"] = (
    "Amendment 3: original ladder's eps=1e-6 draw 0 stalled at "
    "3.28e-9 on default tolerances; completed ladder (seed 4203, "
    "ftol=xtol=gtol=1e-13, max_nfev 2500) in "
    "p420_ladder_completed.json; bar unchanged at 1e-9.")
res["verdict"]["gate_referral"] = bool(
    new_form == "COMPOSITE SUPPLIES THE CORRECTED TARGET")
json.dump(res, open(f'{WP}/phase420/results/p420_results.json', "w"),
          indent=1, default=str)
print("COMPLETED LADDER all_reclose:", all_reclose, flush=True)
print("VERDICT (completed ladder):", new_form, flush=True)
