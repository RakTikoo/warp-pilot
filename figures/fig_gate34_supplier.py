#!/usr/bin/env python3
"""Gate-34 figure: the positive-density pair's supplier sites and trade curve.

Sources (all stored):
  gate34-claims/results/g34_item1.json   (the gate's re-read of the 4 sites)
  gate34-claims/results/g34_item3a.json  (the N=6 match)
  gate34-claims/results/g34_item3c.json  (the match's Jacobian spectrum)
  phase312/results/p312_results.json     (the 36-member trade curve)
"""
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
i1 = json.load(open(f"{ROOT}/gate34-claims/results/g34_item1.json"))
i3 = json.load(open(f"{ROOT}/gate34-claims/results/g34_item3a.json"))
i3c = json.load(open(f"{ROOT}/gate34-claims/results/g34_item3c.json"))
p312 = json.load(open(f"{ROOT}/phase312/results/p312_results.json"))

sites = i1["gate_sites"]
keys = sorted(sites.keys())
rhos = [sites[k]["rho_req"] for k in keys]
sv = i3c["jacobian"]["singular_values"]
print("sigma ladder length:", len(sv), "sigma_min:", min(sv))

tc = p312["trade_curve"]
xs = [m["min_rho_req"] for m in tc]
ys = [m["depth"] for m in tc]
pos = [m["all_sites_rho_nonneg"] for m in tc]
win = next(m for m in p312["members"] if m["label"] == "ramp_broad_m+1.00")

fig, axes = plt.subplots(1, 3, figsize=(14.6, 4.5))
fig.patch.set_facecolor("white")
ax = axes[0]
ax.bar(keys, rhos, color="tab:green")
ax.axhline(0, color="k", lw=1)
ax.set_ylabel(r"$\rho_{req}$ at the binding site")
ax.set_title("A. The winner's density is positive\nat all four binding sites",
             fontsize=10)

ax = axes[1]
ax.semilogy(range(1, len(sv) + 1), sv, "o-", color="tab:purple", ms=3.5)
ax.set_xlabel("Jacobian singular value index (of 40)")
ax.set_ylabel("singular value (log)")
ax.set_title(f"B. The six-mode match is structural:\n"
             f"full rank, $\\sigma_{{min}}$ = {min(sv):.4f}", fontsize=10)

ax = axes[2]
ax.scatter([x for x, p in zip(xs, pos) if not p],
           [y for y, p in zip(ys, pos) if not p],
           color="0.6", label="site density negative somewhere")
ax.scatter([x for x, p in zip(xs, pos) if p],
           [y for y, p in zip(ys, pos) if p],
           color="tab:green", label="positive at all sites")
ax.scatter([win["set"]["rho"]["min"]], [win["depth_SAMPLER-M_polished"]],
           marker="*", s=260, color="gold", edgecolor="k",
           label="the winner (broad ramp m0 = +1.0)", zorder=5)
ax.axvline(0, color="k", lw=0.8)
ax.set_xlabel("member's minimum site density")
ax.set_ylabel("NEC depth (SAMPLER-M, polished)")
ax.set_title("C. The 36-member trade curve: density\n"
             "is bought, depth is the price", fontsize=10)
ax.legend(fontsize=7.5)
fig.tight_layout()
out = f"{FIG}/fig_gate34_supplier.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
