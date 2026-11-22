#!/usr/bin/env python3
"""G6-3 W-C: remaining rows, lean version (scan-level optima; the
headline row's convergence was already proven in the main run at
two tolerances to 4e-12). Same ODE code path as wc_g63_solver.py."""
import json
import numpy as np
import wc_g63_solver as W

OUT = "/home/hatch/workspace/warp-pilot/gate6/results/wc_g63_numbers_rest.json"
out = {}
tb1 = 2 * W.ell(1.0)

SCAN = [0.0, -0.05, -0.1, -0.2, -0.35, -0.5, -0.8, -1.2, -1.8, -2.5,
        -3.5, -5.0, -7.0, -10.0, -12.0]


def light_optimum(spl, za, cap, rtol=1e-10, max_step=0.03):
    best = None
    for p0 in SCAN:
        r = W.shoot_brane_to_throat(spl, za, p0, cap=cap, rtol=rtol,
                                    max_step=max_step)
        T = r["T_total"] if r["hit_cap"] else r["T_total_smooth"]
        if np.isfinite(T) and (best is None or T < best[0]):
            best = (T, p0, r)
    T, p0, r = best
    # one small zoom: 5 points within +-25%
    if p0 != 0.0:
        for f in (0.8, 0.9, 1.1, 1.25):
            r2 = W.shoot_brane_to_throat(spl, za, p0 * f, cap=cap,
                                         rtol=rtol, max_step=max_step)
            T2 = r2["T_total"] if r2["hit_cap"] else r2["T_total_smooth"]
            if np.isfinite(T2) and T2 < T:
                T, p0, r = T2, p0 * f, r2
    return {"za": za, "cap": cap, "p0_opt": float(p0), "T_bulk": float(T),
            "z1": (r["z1"] if r["hit_cap"] else None),
            "optimum_type": "cap_ride" if r["hit_cap"] else "smooth_mirror"}


for za in (1.0, 2.0):
    r = light_optimum(W.SPL, za, 0.455)
    lev = W.headline_linear_eval(za, 0.455, r["p0_opt"])
    tb = 2 * W.ell(za)
    out[f"linear_eval_za{za}"] = {
        "p0_opt_scan": r["p0_opt"], "T_spline_scan": r["T_bulk"],
        "T_linear_fields": lev["T_bulk_linear_fields"],
        "gain_linear_fields": (tb - lev["T_bulk_linear_fields"]) / tb,
        "z1": lev["z1"]}
    print("LINEAR", za, lev["T_bulk_linear_fields"],
          out[f"linear_eval_za{za}"]["gain_linear_fields"], flush=True)

caps = []
for cap in (0.20, 0.30, 0.40):
    r = light_optimum(W.SPL, 1.0, cap)
    r.update({"t_brane": tb1, "gain_frac": (tb1 - r["T_bulk"]) / tb1})
    caps.append(r)
    print("CAP", cap, r["T_bulk"], r["gain_frac"], flush=True)
out["cap_scan_za1"] = caps

fd = []
for Y in (0.1, 0.2, 0.3, 0.4, 0.44, 0.45):
    r = W.forced_depth(W.SPL, 1.0, Y)
    if r.get("root_found"):
        r.update({"t_brane": tb1, "gain_frac": (tb1 - r["T_bulk"]) / tb1})
    fd.append(r)
    print("FORCED", Y, r.get("T_bulk"), r.get("gain_frac"), flush=True)
out["forced_depth_za1"] = fd

out["same_sheet"] = W.same_sheet(W.SPL)
print("SAME SHEET", out["same_sheet"], flush=True)
json.dump(out, open(OUT, "w"), indent=1)
print("DONE", flush=True)
