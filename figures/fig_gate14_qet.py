#!/usr/bin/env python3
"""Figure: Gate-14 multipartite QET -- delivered energy vs total price.

All values read from the stored Gate-14 numbers file: the deciding rows are
the stored rows with E_net_B < 0 (net delivered energy at the receiving
sector); Pi_sep (total price per unit delivered against the cheapest
uncorrelated / separable preparation) comes from the stored sep_certificate;
price_per_unit_marg (the marginal-preparation convention) from the rows.

Source: gate14-claims/results/g14_numbers.json
Output: fig_gate14_qet.png
"""
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
d = json.load(open(f"{ROOT}/gate14-claims/results/g14_numbers.json"))
rows = d["rows"]
sep = {(c["N"], c["row"][1], c["row"][2]): c["Pi_sep"]
       for c in d["sep_certificate"]}
band = d["price_deciding_range_sep"]

dec = [r for r in rows if r["E_net_B"] < 0]
print(f"{len(dec)} deciding rows (E_net_B < 0); stored sep price band {band}")
pts = []
for r in dec:
    key = (r["N"], r["m"], r["r"])
    pts.append((abs(r["E_net_B"]), sep[key], r["price_per_unit_marg"],
                f"N={r['N']}, k/h={r['r']}"))
    print(f"  row {key}: delivered {abs(r['E_net_B']):.4f}, "
          f"Pi_sep {sep[key]:.3f}, price_marg {r['price_per_unit_marg']:.3f}")

fig, ax = plt.subplots(figsize=(9.2, 5.6))
fig.patch.set_facecolor("white")
ax.axhspan(band[0], band[1], color="#c0392b", alpha=0.13,
           label=f"total price band vs cheapest uncorrelated preparation: "
                 f"{band[0]:.2f}–{band[1]:.2f} per unit delivered")
ax.axhline(1.0, color="#c0392b", ls="--", lw=1.3,
           label="price = 1 (break-even: delivery for free)")
for x, y_sep, y_marg, lab in pts:
    ax.plot([x], [y_sep], "o", ms=9, color="#1a5276",
            label="_nolegend_")
    ax.plot([x], [y_marg], "s", ms=7, mfc="none", color="#888888",
            label="_nolegend_")
    ax.annotate(lab, xy=(x, y_sep), xytext=(6, 7), textcoords="offset points",
                fontsize=9)
ax.plot([], [], "o", color="#1a5276", label="total price per unit (separable bound, $\\Pi_\\mathrm{sep}$)")
ax.plot([], [], "s", mfc="none", color="#888888",
        label="price per unit (marginal convention)")
ax.set_xlabel("net delivered energy at the receiving sector  |E_net,B|  (model units)")
ax.set_ylabel("total price per unit delivered")
ax.set_title("Gate-14: multipartite QET delivers net negative energy — at a price\n"
             "every deciding row costs 5.34–28.17 units per unit delivered: NOT an energy source",
             fontsize=11)
ax.set_xlim(-0.01, 0.53)
ax.set_ylim(0, 30.5)
ax.legend(fontsize=9, loc="lower right")
ax.grid(alpha=0.25)
fig.tight_layout()
out = f"{ROOT}/publication/figures/fig_gate14_qet.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
