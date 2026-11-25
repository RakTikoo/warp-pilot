#!/usr/bin/env python3
"""Gate-25 figure: spinor sourcing -- interference breaks the sign identity.

All values from gate25-claims/results/g25_verify_results.json.
"""
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
d = json.load(open(f"{ROOT}/gate25-claims/results/g25_verify_results.json"))
t1 = d["task1_phase253"]
singles = [m["Tkk_single_renorm_c1"] for m in t1["single_modes"]]
tkk = t1["Tkk_mine"]
rho = t1["rho_mine_T00"]
t3 = d["task3_type_scan"]
t2 = d["task2_phase257"]

fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.6))
fig.patch.set_facecolor("white")
ax = axes[0]
labs = [f"mode {i} alone" for i in range(len(singles))] + \
       ["3-mode superposition"]
vals = singles + [tkk]
cols = ["0.6"] * len(singles) + ["tab:red"]
ax.bar(labs, vals, color=cols)
ax.axhline(0, color="k", lw=1)
ax.set_ylabel("T(k*, k*) at the worst site")
ax.set_title(f"A. Every single mode is >= 0; the superposition\n"
             f"reads {tkk:.2f} at density rho = +{rho:.2f}", fontsize=10)
ax.tick_params(axis="x", labelrotation=18, labelsize=8)

ax = axes[1]
ax.bar(["Phase 257 scan\n(stored claim)", "Gate-25's own draws"],
       [float(t3["claimed_phase"].split("=")[1]),
        t3["fraction"]],
       color=["0.6", "tab:purple"])
ax.set_ylabel("fraction of draws with a complex eigenvalue pair\n(Type-IV tensor)")
ax.set_title("B. Type-IV members are generic, not exotic:\n"
             "complex-pair draws in the stored scans", fontsize=10)
ax.annotate(f"the six-mode match of T_req (panel A's line, other site)\n"
            f"lands at residual {t2['R_vs_Treq_p2502']:.2e} -- and at\n"
            f"NEGATIVE density rho_unit = {t2['rho_unit_mine_div_sumc2']:.4f}: "
            "the match does\nnot inherit the positive density",
            (0.03, 0.97), xycoords="axes fraction", fontsize=8.5, va="top")
fig.tight_layout()
out = f"{FIG}/fig_gate25_spinor.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
