#!/usr/bin/env python3
"""Gate-12 figure: the Le multipole pin + the endowed shell spectrum.

Drawn entirely from stored Gate-12 results:
  gate12-claims/results/g12_le_numbers.json       (anchors, deciding audit)
  gate12-claims/results/g12_endowed_numbers.json  (spectrum, mp40 strings)
No number is typed in by hand.
"""
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
le = json.load(open(f"{ROOT}/gate12-claims/results/g12_le_numbers.json"))
en = json.load(open(f"{ROOT}/gate12-claims/results/g12_endowed_numbers.json"))

fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))
fig.patch.set_facecolor("white")

# --- A: Le anchors + grid ladder of the deciding audit ---
ax = axes[0]
names = list(le["anchors"].keys())
marg = [le["anchors"][k]["margin"] for k in names]
cols = ["tab:green" if m > 0 else "tab:red" for m in marg]
ax.barh(range(len(names)), marg, color=cols, alpha=0.75)
ax.axvline(0, color="k", lw=1)
lad = le["deciding_audit_x0.7"]["ladder"]
hx = sorted(float(k.split("_")[0][1:]) for k in lad)
hy = [lad[f"h{h:g}_o2"]["margin"] if f"h{h:g}_o2" in lad else
      lad[[k for k in lad if k.startswith(f"h{h:g}")][0]]["margin"] for h in hx]
ax2 = ax.twiny()
ax2.plot(hy, [len(names) + 0.6] * len(hy), "o-", color="tab:blue", ms=5,
         label="x = 0.7 audit, grid ladder")
ax2.set_xlim(ax.get_xlim())
ax2.set_xlabel("ladder margin (same scale)", color="tab:blue", fontsize=8)
ax.set_yticks(list(range(len(names))) + [len(names) + 0.6])
ax.set_yticklabels([k.replace("_", " ") for k in names] +
                   ["x0.7 ladder (h = 0.02/0.01/0.005, o4)"], fontsize=7.5)
ax.set_xlabel("Type-I margin (stored anchors + deciding audit)")
ax.set_title("A. Le multipole shell: stored pole anchors\n"
             "and the (0.7, 0.09) deciding audit's margins", fontsize=10)

# --- B: endowed shell spectrum ---
ax = axes[1]
sp = en["spectrum_mp40"]
w0 = float(sp["w0"]); thr = float(sp["threshold"])
o2_0 = float(sp["omega2_at_0"]); o2_w0 = float(sp["omega2_at_w0"])
xs = [0.0, w0]
ax.semilogy(xs, [abs(o2_0), abs(o2_w0)], "o-", color="k")
for x, v in zip(xs, [o2_0, o2_w0]):
    ax.annotate(f"$\omega^2$ = {v:+.3e}\n({'UNSTABLE' if v < 0 else 'stable'})",
                (x, abs(v)), textcoords="offset points", xytext=(8, 8),
                fontsize=8.5,
                color="tab:red" if v < 0 else "tab:green")
ax.axvline(thr, color="tab:orange", ls="--",
           label=f"stored threshold w = {thr:.4f}")
ax.set_xlabel("surface equation-of-state parameter w")
ax.set_ylabel("|$\\omega^2$| (log)")
ax.set_title("B. Endowed shell spectrum (40-digit reads):\n"
             "$\omega^2 < 0$ at w = 0, $\omega^2 > 0$ at the stored w$_0$",
             fontsize=10)
ax.legend(fontsize=8.5)
fig.tight_layout()
out = f"{FIG}/fig_gate12_pins.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
