#!/usr/bin/env python3
"""Figure: Gate-35 / Phase 314 pointwise member -- density profile and NEC depth.

Every plotted number is read from stored result files, or evaluated with the
programme's own stored Gate-35 evaluator (gate35/work/g35_rho.py), which is
Gate-35's independent rho code for this member. No profile numbers are typed
into this script.

Sources:
  phase314/results/p314_results.json          (headline member, SET-244 reads)
  gate35-claims/results/g35_item1_results.json (continuum adversary: global min)
  gate35/work/g35_rho.py                       (stored evaluator: rho*(r))
Output: fig_gate35_density.png
"""
import json
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
sys.path.insert(0, f"{ROOT}/gate35/work")
import g35_rho  # noqa: E402  (stored Gate-35 evaluator; adds its own lib paths)

p314 = json.load(open(f"{ROOT}/phase314/results/p314_results.json"))
g35 = json.load(open(f"{ROOT}/gate35-claims/results/g35_item1_results.json"))

hm = p314["headline_member"]
prof = hm["profile"]
setr = hm["set"]
depth_polished = hm["depth_SAMPLER-M_polished"]

gmin = g35["search_c"]["global_min"]
regions = g35["floors_d"]["regions"]
r_lo = min(v["range"][0] for v in regions.values())
r_hi = max(v["range"][1] for v in regions.values())

# --- Panel A data: rho*(r) = angular minimum of rho_req, stored evaluator ---
rs = np.linspace(r_lo, r_hi, 201)
rho_star = np.array([g35_rho.rho_star(float(r), n_u=801)[0] for r in rs])
print(f"evaluator check: rho*(argmin r={gmin['r']}) = "
      f"{g35_rho.rho_star(gmin['r'])[0]:.12e} vs stored global min {gmin['rho']:.12e}")
print(f"profile from stored JSON: {prof}; domain [{r_lo}, {r_hi}] from stored region ranges")

fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.5, 4.4),
                               gridspec_kw={"width_ratios": [1.55, 1.0]})
fig.patch.set_facecolor("white")

axA.plot(rs, rho_star * 1e5, color="#1a6b3c", lw=1.8,
         label=r"$\rho^*(r)$ = angular minimum of $\rho_\mathrm{req}$ (stored Gate-35 evaluator)")
axA.axhline(0.0, color="k", lw=0.9)
axA.axhline(gmin["rho"] * 1e5, color="#c0392b", ls="--", lw=1.2,
            label=f"Gate-35 continuum minimum $\\rho^*$ = {gmin['rho']:.4e}")
axA.plot([gmin["r"]], [gmin["rho"] * 1e5], "o", color="#c0392b", ms=7, zorder=5)
axA.annotate(f"minimum at r = {gmin['r']:.0f}, u = {gmin['u']}",
             xy=(gmin["r"], gmin["rho"] * 1e5), xytext=(13.2, 12.5),
             arrowprops=dict(arrowstyle="->", color="#c0392b"), color="#c0392b", fontsize=9)
axA.axhline(setr["rho"]["min"] * 1e5, color="#5555aa", ls=":", lw=1.2,
            label=f"SET-244 sampled minimum (SAMPLER-M) = {setr['rho']['min']:.4e}")
axA.set_xlabel("radius r (geometric units; Gate-35 certified domain)")
axA.set_ylabel(r"$\rho_\mathrm{req}$  [$10^{-5}$, bracket units]")
axA.set_title(f"A. Density is positive throughout the volume\n"
              f"pointwise member: ramp $m_0$ = {prof['m0']:+.2f}, rise [{prof['r1']:.0f}, {prof['r2']:.1f}]",
              fontsize=10.5)
axA.legend(fontsize=8.2, loc="upper right")
axA.grid(alpha=0.25)

# --- Panel B data: the member's energy-condition reads (stored SET-244) ---
labels = ["NEC depth\n(polished,\nSAMPLER-M)", "NEC min\n(SET-244)", "WEC min\n(SET-244)"]
vals = [depth_polished, setr["nec"]["min"], setr["wec"]["min"]]
cols = ["#b8860b", "#c0392b", "#7d3c98"]
bars = axB.bar(labels, np.array(vals) * 1e3, color=cols, width=0.58)
axB.axhline(0.0, color="k", lw=0.9)
for b, v in zip(bars, vals):
    axB.annotate(f"{v:.3e}", xy=(b.get_x() + b.get_width() / 2, v * 1e3),
                 xytext=(0, -14), textcoords="offset points", ha="center",
                 fontsize=9, fontweight="bold")
axB.set_ylim(min(vals) * 1.22e0, max(0.0, max(vals)) + 0.0012)
axB.set_ylabel("energy-condition read  [$10^{-3}$, bracket units]")
axB.set_title("B. The pressures still fail:\nthe member's NEC / WEC depth reads", fontsize=10.5)
axB.grid(alpha=0.25, axis="y")
axB.tick_params(labelsize=8.5)

fig.tight_layout()
out = f"{ROOT}/publication/figures/fig_gate35_density.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
