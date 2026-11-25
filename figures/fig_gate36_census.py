#!/usr/bin/env python3
"""Gate-36 figure: the conditioning census -- sigma_min belongs to the
solution found, not to the target.

All values from gate36-claims/results/g36_item3_results.json (the gate's
own censuses E1/E2 and the scale probe E5).
"""
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
d = json.load(open(f"{ROOT}/gate36-claims/results/g36_item3_results.json"))
c1 = [s["sigma_min"] for s in d["E1"]["census"]]
c2 = [s["sigma_min"] for s in d["E2"]["census"]]
warm = min(c1)
print(f"pointwise census n={len(c1)} median={np.median(c1):.4e}; "
      f"weaker census n={len(c2)} median={np.median(c2):.4e}")

fig, ax = plt.subplots(figsize=(9.6, 5.0))
fig.patch.set_facecolor("white")
x1 = np.arange(len(c1))
x2 = np.arange(len(c2))
ax.semilogy(x1, c1, "o", color="tab:blue", ms=7,
            label="pointwise member (Phase 314 target) solutions")
ax.semilogy(x2 + 0.35, c2, "s", color="tab:orange", ms=7,
            label="weaker winner (Phase 312 target) solutions")
wi = int(np.argmin(c1))
ax.annotate(f"Phase 320's solution (warm lineage):\n"
            f"$\\sigma_{{min}}$ = {warm:.3e} -- the thinnest found",
            (wi, warm), textcoords="offset points", xytext=(30, 26),
            fontsize=9, arrowprops=dict(arrowstyle="->"))
ax.axhline(np.median(c1), color="tab:blue", ls="--", lw=1,
           label=f"pointwise median {np.median(c1):.3e}")
ax.axhline(np.median(c2), color="tab:orange", ls="--", lw=1,
           label=f"weaker-target median {np.median(c2):.3e}")
ax.set_xlabel("independent solution found by the gate's ladder")
ax.set_ylabel(r"Jacobian $\sigma_{min}$ of the solution (log)")
ax.set_title("Gate-36's census: every non-warm-lineage solution is >= 9.5x thicker\n"
             "than Phase 320's -- conditioning is a property of the solution found",
             fontsize=10.5)
ax.legend(fontsize=8.5)
fig.tight_layout()
out = f"{FIG}/fig_gate36_census.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
