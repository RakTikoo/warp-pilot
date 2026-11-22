#!/usr/bin/env python3
"""Gate-6 bundle figures — every figure is generated from the gate's own
result files (gate6/wa_results.json, gate6/wb_g62_numeric.json,
gate6/results/wc_g63_numbers_*.json) or, for G6-4, from the arithmetic
values independently verified in gate6/results/wD_g6_4.md §2.
Run with the programme venv python (system matplotlib is broken):
  ~/workspace/warp-pilot/venv/bin/python make_figures.py
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
G6 = os.path.join(HERE, "..", "..", "gate6")

# ---------- G6-3: bulk-shortcut gains ----------
main = json.load(open(os.path.join(G6, "results", "wc_g63_numbers_main.json")))
rest = json.load(open(os.path.join(G6, "results", "wc_g63_numbers_rest.json")))
cross = sorted(main["cross_throat_cap0455"], key=lambda r: r["za"])
caps = [(c["cap"], c["gain_frac"]) for c in rest["cap_scan_za1"]]
caps += [(0.455, cross[1]["gain_frac"]), (0.46, main["za1_cap046"]["gain_frac"])]
caps = sorted(set(caps))

fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
ax[0].plot([r["za"] for r in cross], [r["gain_frac"] for r in cross], "o-")
for r in cross:
    ax[0].annotate(f"{r['gain_frac']:.3f}", (r["za"], r["gain_frac"]),
                   textcoords="offset points", xytext=(0, 7), ha="center")
ax[0].axhline(0.0002, ls="--", color="grey")
ax[0].annotate("same-sheet control ≈ 0.0002", (1.55, 0.02), color="grey")
ax[0].set_xlabel(r"crossing half-distance $z_a$ ($r_0$)")
ax[0].set_ylabel("fractional gain (cap $y \\leq 0.455\\,r_0$)")
ax[0].set_title("G6-3: cross-throat bulk-shortcut gain")
ax[1].plot([c for c, _ in caps], [g for _, g in caps], "s-")
for c, g in caps:
    ax[1].annotate(f"{g:.3f}", (c, g), textcoords="offset points",
                   xytext=(0, 7), ha="center")
ax[1].set_xlabel(r"depth cap $y$ ($r_0$) at $z_a = 1$")
ax[1].set_ylabel("fractional gain")
ax[1].set_title("Gain grows with cap; infimum not attained\n(lives at the singular boundary $y^* \\approx 0.4675$)")
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g63_bulk_shortcut_gain.png"), dpi=200)
plt.close(fig)

# ---------- G6-1: margin ledger at beta = 0.07 / 0.08 ----------
wa = json.load(open(os.path.join(G6, "wa_results.json")))
kinds = ["nec", "wec", "sec", "dec"]
labels = ["NEC", "WEC", "SEC", "DEC"]
core07 = [wa["main_b0.07_h0.15"]["core"][k] for k in kinds]
core08 = [wa["main_b0.08_h0.15"]["core"][k] for k in kinds]
x = np.arange(len(kinds)); w = 0.38
fig, ax = plt.subplots(figsize=(7.5, 3.8))
ax.bar(x - w/2, core07, w, label=r"$\beta = 0.07$ core worst margins")
ax.bar(x + w/2, core08, w, label=r"$\beta = 0.08$ core worst margins")
ax.set_yscale("log")
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_ylabel("worst margin (geometric units, log scale)")
ax.set_title("G6-1: (10,30) thick shell — Gate-6 core margin ledger (h = 0.15)\n"
             "whole-volume worst SEC +2.59e-07 (exterior tail, r = 37) at both $\\beta$; Type-I 1.000")
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g61_margin_ledger.png"), dpi=200)
plt.close(fig)

# ---------- G6-2: inertness numeric spot checks ----------
wb = json.load(open(os.path.join(G6, "wb_g62_numeric.json")))
fig, ax = plt.subplots(figsize=(5.2, 4.2))
for name, v in wb.items():
    ax.plot(v["pr_canonical"], v["pr_extrap"], "o", label=name)
lims = [-0.15, -0.05]
ax.plot(lims, lims, "--", color="grey", label="canonical $\\Phi=0$ value")
ax.set_xlabel(r"$p_{r,\mathrm{dem}}(r_0)$ — canonical $\Phi = 0$ formula $-F_0/(8\pi r_0^2)$")
ax.set_ylabel(r"$p_{r,\mathrm{dem}}(r_0)$ — $\Phi \neq 0$ series extrapolation")
ax.set_title("G6-2: throat $p_r$ is inert to $\\Phi'$, $F'_0$, $F''_0$\n"
             "(spread $\\leq 3.6\\times10^{-4}$ across the gate's controlled triples)")
ax.legend(fontsize=7)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g62_inertness.png"), dpi=200)
plt.close(fig)

# ---------- G6-4: species pricing (values verified in wD_g6_4.md §2) ----------
fig, ax = plt.subplots(figsize=(7.5, 3.8))
names = ["N required\n(1 m tube, L = ε)", "heuristic cap\nℓ = 1 m", "heuristic cap\nℓ = ε = 0.1 m"]
vals = [1.06e72, 3.83e69, 3.83e67]
ax.bar(names, np.log10(vals), color=["#b03030", "#4070a0", "#4070a0"])
for i, v in enumerate(vals):
    ax.annotate(f"{v:.2g}", (i, np.log10(v)), textcoords="offset points",
                xytext=(0, 5), ha="center")
ax.set_ylabel(r"$\log_{10}$ of field count")
ax.set_title("G6-4: the species escape is priced out — required N vs heuristic caps\n"
             "(shortfalls 2.45 and 4.45 orders; caps heuristic, not theorem)")
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g64_species_pricing.png"), dpi=200)
plt.close(fig)

print("figures written:", sorted(f for f in os.listdir(HERE) if f.endswith(".png")))
