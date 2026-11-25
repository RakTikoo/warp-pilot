#!/usr/bin/env python3
"""Gate-37 figure: the identification -- one printed number, and the
residual collapse it explains.

All values from gate37-claims/results/g37_arithmetic.json (exact rational
strings parsed with Fraction; family maxima as stored floats).
"""
import json
from fractions import Fraction

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
d = json.load(open(f"{ROOT}/gate37-claims/results/g37_arithmetic.json"))
rest = d["rest_ellis"]
derived = [float(Fraction(s)) for s in rest["H203_mine_print"]]
implied = [float(Fraction(s)) for s in rest["implied_print_H203"]]
gate0 = d["gate"]["P_full_stored"][0]
gate1 = float(Fraction(d["gate"]["P0_arbitrated"]))
fams = d["family_maxima_stored"]

fig, axes = plt.subplots(1, 3, figsize=(14.6, 4.6))
fig.patch.set_facecolor("white")
ax = axes[0]
comps = ["$T^t{}_t$", "$T^r{}_r$", "$T^\\theta{}_\\theta$"]
x = range(3)
w = 0.36
ax.bar([i - w / 2 for i in x], derived, w, label="derived H{2,0}(3)",
       color="tab:green")
ax.bar([i + w / 2 for i in x], implied, w,
       label="as printed in Decanini-Folacci", color="tab:red", alpha=0.75)
ax.set_xticks(list(x))
ax.set_xticklabels(comps)
ax.set_title("A. One printed number differs:\n"
             "$T^r{}_r$ 80/3 in print, 16 derived", fontsize=10)
ax.legend(fontsize=8.5)

ax = axes[1]
ax.bar(["Ellis gate coefficient\nwith the printed tensor",
        "with the derived tensor"],
       [gate0, gate1], color=["tab:red", "tab:green"], alpha=0.8)
ax.set_title("B. The gate coefficient moves\n203 -> 187 (the target)",
             fontsize=10)

ax = axes[2]
names = list(fams.keys())
before = [fams[k]["phase259_FULL"] for k in names]
after = [fams[k]["arbitrated"] for k in names]
x = range(len(names))
ax.bar([i - w / 2 for i in x], before, w, label="Phase 259 residual (FULL)",
       color="tab:red", alpha=0.75)
ax.bar([i + w / 2 for i in x], after, w,
       label="with the derived tensor (arbitrated)", color="tab:green")
ax.set_yscale("log")
ax.set_xticks(list(x))
ax.set_xticklabels(names, fontsize=8.5)
ax.set_ylabel("max |xi^0 residual| (log)")
ax.set_title("C. The wider-set residuals collapse\n"
             "by 12+ orders of magnitude", fontsize=10)
ax.legend(fontsize=8)
fig.tight_layout()
out = f"{FIG}/fig_gate37_collapse.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
