#!/usr/bin/env python3
"""Gate-7 bundle figures - generated only from the gate's own result
files in ../results/ (wa_g71_numbers.json, wa_anatomy.json,
wb_g72_numbers.json, wc_g73_numbers.json). Plain-text labels (no
mathtext) for portability. Run with the programme venv python:
  ~/workspace/warp-pilot/venv/bin/python make_figures.py
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")
KINDS = ["nec", "wec", "sec", "dec"]
LABELS = ["NEC", "WEC", "SEC", "DEC"]

# ---- G7-1: halved-smoothing margins + inner-edge layer ----
wa = json.load(open(os.path.join(RES, "wa_g71_numbers.json")))
an = json.load(open(os.path.join(RES, "wa_anatomy.json")))
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.6))
for j, (key, lab) in enumerate([("deciding_b0.09", "beta = 0.09"),
                                ("deciding_b0.1", "beta = 0.10")]):
    vals = [wa[key]["all_sig"][k] for k in KINDS]
    ax[0].bar(np.arange(4) + (j - 0.5) * 0.38, vals, 0.38, label=lab)
ax[0].set_yscale("log")
ax[0].set_xticks(range(4)); ax[0].set_xticklabels(LABELS)
ax[0].set_ylabel("whole-set worst margin (log scale)")
ax[0].set_title("G7-1 deciding-set margins, 1,404 pts\nType-I 1.000 at both beta", fontsize=10)
ax[0].legend(fontsize=8)
ins = [an["r10_b0.0_Spp-inside"]["dec_min"], an["r10_b0.09_Spp-inside"]["dec_min"],
       an["r10_b0.1_Spp-inside"]["dec_min"]]
outs = [an["r10_b0.0_Spp-outside"]["dec_min"], an["r10_b0.09_Spp-outside"]["dec_min"],
        an["r10_b0.1_Spp-outside"]["dec_min"]]
x = np.arange(3)
ax[1].bar(x - 0.19, ins, 0.38, label="inside R1 probe")
ax[1].bar(x + 0.19, outs, 0.38, label="outside R1 probe")
ax[1].axhline(0, color="black", lw=0.8)
ax[1].set_xticks(x); ax[1].set_xticklabels(["beta=0", "beta=0.09", "beta=0.10"])
ax[1].set_ylabel("DEC minimum")
ax[1].set_title("Inner-edge layer the fine set steps over\nbeta=0.10 inside: -1.29e-05", fontsize=10)
ax[1].legend(fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g71_margin_ledger.png"), dpi=200)
plt.close(fig)

# ---- G7-2: spline-shift finalists ----
wb = json.load(open(os.path.join(RES, "wb_g72_numbers.json")))
p, s = wb["deciding_primary_b0.10_b0.10"], wb["deciding_second_b0.1363_b0.10"]
fig, ax = plt.subplots(figsize=(7.5, 3.6))
names = ["whole-set worst", "core worst", "core sampled NEC min"]
pv = [p["all_sig"]["worst"], p["core"]["worst"], p["core_sampled_nec_min"]]
sv = [s["all_sig"]["worst"], s["core"]["worst"], s["core_sampled_nec_min"]]
x = np.arange(3)
ax.bar(x - 0.19, pv, 0.38, label="primary finalist")
ax.bar(x + 0.19, sv, 0.38, label="second finalist")
ax.set_yscale("log"); ax.set_xticks(x); ax.set_xticklabels(names, fontsize=8)
ax.set_ylabel("margin (log scale)")
ax.set_title("G7-2 spline-shift row at beta = 0.10: both finalists legal\n(deciding set, Type-I 1.000)", fontsize=10)
ax.legend(fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g72_spline_finalists.png"), dpi=200)
plt.close(fig)

# ---- G7-3: Procaccia confirmation ----
wc = json.load(open(os.path.join(RES, "wc_g73_numbers.json")))
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.6))
runs = [("verdict_h0.0375", "h = 0.0375"), ("verdict_h0.01875", "h = 0.01875"),
        ("secondpath_order4_h0.0375", "4th-order")]
for j, (k, lab) in enumerate(runs):
    vals = [wc[k]["all_sig"][kk] for kk in KINDS]
    ax[0].bar(np.arange(4) + (j - 1) * 0.27, vals, 0.27, label=lab)
ax[0].set_yscale("log"); ax[0].set_xticks(range(4)); ax[0].set_xticklabels(LABELS)
ax[0].set_ylabel("worst margin at beta = 0.1363 (log scale)")
ax[0].set_title("G7-3 margins at beta = 0.1363, all paths\nType-I 1.000; worst +3.40e-07", fontsize=10)
ax[0].legend(fontsize=7)
cc = wc["step3_crosscheck"]
o4 = wc["step3_crosscheck_exact_minnull"]["b0.1364_order4_h0.00234375"]["min_null_exact_opt"]
ax[1].bar(["his interval\nvalue", "gate exact\n2nd-order", "gate exact\n4th-order"],
          [abs(cc["his_interval_value"]), abs(cc["exact_opt_finest_h"]), abs(o4)])
ax[1].set_ylabel("|min null contraction| at beta = 0.1364")
ax[1].set_title("Cross-check at his point (0, 16.635, 0)\nreproduced to 0.58% / 0.010%", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g73_procaccia_confirmation.png"), dpi=200)
plt.close(fig)

print("figures written:", sorted(f for f in os.listdir(HERE) if f.endswith(".png")))
