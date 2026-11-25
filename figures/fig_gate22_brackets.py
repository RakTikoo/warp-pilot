#!/usr/bin/env python3
"""Gate-22 combined set figure (v1.22.0): the sustainment brackets and the
Gate-27 trim law.

Sources (all stored in gate22-claims/results/):
  g23_verify_results.json  (the wound pose's certified bracket)
  g27_verify_results.json  (ordering, stored brackets, the trim law a(t)
                            and its stored evaluations, the crossing)
  g31_results.json         (the Axis A companion bracket)
Jet-scope exhibits only -- no geometry is drawn, by design.
"""
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
R = f"{ROOT}/gate22-claims/results"
g23 = json.load(open(f"{R}/g23_verify_results.json"))
g27 = json.load(open(f"{R}/g27_verify_results.json"))
g31 = json.load(open(f"{R}/g31_results.json"))

fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.8))
fig.patch.set_facecolor("white")

ax = axes[0]
rows = [
    ("wound pose (Gate-23)",
     sorted(float(k) for k in g23["new_bracket"]["bars"]), "tab:blue"),
    ("Axis A companion (Gate-31)", g31["bracket"], "tab:cyan"),
    ("combined class, clamped\n(Gate-26 certificate)",
     g27["p265_arms"]["2.5"]["refined_bracket"], "0.55"),
    ("combined class, UNCLAMPED\n(G27-A lead, Gate-28 fence)",
     g27["p266_bracket_stored"], "tab:green"),
]
for i, (lab, br, c) in enumerate(rows):
    ax.barh(i, br[1] - br[0], left=br[0], height=0.55, color=c, alpha=0.8)
    ax.annotate(f"({br[0]:.5f}, {br[1]:.5f}]", (br[1], i),
                textcoords="offset points", xytext=(5, -3), fontsize=8.5)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows], fontsize=8.5)
ax.set_xlabel("first-crossing time bracket t* (programme units)")
ax.set_title("A. The sustainment line at verdict grade:\n"
             "certified first-crossing brackets", fontsize=10)

ax = axes[1]
c_trim = g27["c_trim_stored_in_266"]
t = np.linspace(0, 0.8, 200)
ax.plot(t, -0.5 - c_trim * t**2, color="tab:green",
        label="stored law: a(t) = -0.5 - c$_{trim}$ t$^2$ (unclamped)")
for ts, av in g27["a_at"].items():
    ax.plot(float(ts), av, "o", color="k", ms=4)
ax.annotate("stored evaluations", (0.63, -2.6), fontsize=8.5)
ts_lin = g27["crossing"]["t_star_linear"]
ax.axvline(ts_lin, color="tab:red", ls="--",
           label=f"linearised crossing t* = {ts_lin:.4f}\n"
                 f"(certified bracket in panel A)")
ax.set_xlabel("t")
ax.set_ylabel("director amplitude a(t)")
ax.set_title("B. Gate-27's stop-free trim law and\n"
             "its stored evaluations", fontsize=10)
ax.legend(fontsize=8)
fig.tight_layout()
out = f"{FIG}/fig_gate22_brackets.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
