#!/usr/bin/env python3
"""Gate-15 figure: the two-mouth shell control + the corrected traveller tides.

Sources (all stored):
  gate15-claims/results/wb2_shell.json  -- shell control S00/alpha0 vs eps
  gate15/G15_2_REJUDGEMENT.md  sec.3     -- the corrected tide table; the
      bundle stores no tide JSON, so the table is extracted from the stored
      rejudgement document by pattern (the INVENTORY G-1 precedent); the
      script fails loudly if the table is absent.
"""
import json
import re

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"

shell = json.load(open(f"{ROOT}/gate15-claims/results/wb2_shell.json"))
cc = shell["corrected_gate_control"]
eps = sorted((float(k.split("=")[1]) for k in cc), reverse=True)
s00 = [cc[f"eps={e}"]["A"]["min_S00_over_alpha0"] for e in eps]
s00t = [cc[f"eps={e}"]["A"]["min_minus_tail_bound"] for e in eps]

doc = open(f"{ROOT}/gate15/G15_2_REJUDGEMENT.md").read()
rows = re.findall(r"\| ([^|]+?) \| ([\d.]+)×10⁻⁶ \| ([\d.]+)×10⁻⁶ \| "
                  r"\*\*([\d.]+)×10⁻⁶\*\* \|", doc)
assert len(rows) == 3, f"tide table extraction failed: {rows}"
D = [r[0].replace("×", "x") for r in rows]
phase = [float(r[1]) * 1e-6 for r in rows]
kernel = [float(r[2]) * 1e-6 for r in rows]
tensor = [float(r[3]) * 1e-6 for r in rows]
mbound = re.search(r"≤ ([\d.]+)×10⁻⁶\s*\nbound HOLDS", doc)
bound = float(mbound.group(1)) * 1e-6

fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))
fig.patch.set_facecolor("white")
ax = axes[0]
ax.semilogx(eps, s00, "o-", label=r"$\hat S^{00}/\alpha_0$ minimum (A = B)")
ax.semilogx(eps, s00t, "s--", label="minus stored tail bound")
ax.set_xlabel(r"shell regulator $\epsilon$")
ax.set_ylabel(r"$\hat S^{00}/\alpha_0$")
ax.set_title("A. Gate-15 shell control: both mouths legal,\n"
             "converged in the regulator", fontsize=10)
ax.legend(fontsize=8.5)

ax = axes[1]
x = np.arange(3)
w = 0.27
ax.bar(x - w, phase, w, label="Phase stored read", color="0.6")
ax.bar(x, kernel, w, label="kernel read", color="tab:red", alpha=0.7)
ax.bar(x + w, tensor, w, label="corrected tensor read", color="tab:green")
ax.axhline(bound, color="k", ls="--",
           label=f"claim bound {bound:.1e} s$^{{-2}}$")
ax.set_xticks(x)
ax.set_xticklabels([f"D = {d}" for d in D])
ax.set_ylabel(r"boosted transverse tide at $\beta$ = 0.9 (s$^{-2}$)")
ax.set_title("B. Traveller tide: the stored read was wrong;\n"
             "the corrected tensor read holds the bound", fontsize=10)
ax.legend(fontsize=8)
fig.tight_layout()
out = f"{FIG}/fig_gate15_tides.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
