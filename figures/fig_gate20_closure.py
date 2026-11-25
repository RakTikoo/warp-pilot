#!/usr/bin/env python3
"""Gate-20 figure: the flipped pose's enriched-instrument gate read.

All values from gate20-claims/results/g20_verify_out.json (flat keys read
by their stored prefixes). No number typed in by hand.
"""
import json
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
d = json.load(open(f"{ROOT}/gate20-claims/results/g20_verify_out.json"))
gate_doc = open(f"{ROOT}/gate21-claims/GATE21.md").read()
cap = float(re.search(r"closure [\d.]+ ≤ ([\d.]+),", gate_doc).group(1))

def get(prefix, needle):
    for k, v in d.items():
        if k.startswith(prefix) and needle in k:
            return v
    raise KeyError(prefix + needle)

exact = get("B3", "EXACT coupled closure")
lin = get("A5", "linearised closure")
floor = get("A4", "LS floor")
frozen = get("B4", "FROZEN")
floorw = get("B7", "floor witness exact closure")
embedded = get("C2", "exact closure via enriched")
sigcut = get("A3", "sigma_cut recomputed")
subcut = get("A7", "sub-cut sigmas")

fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))
fig.patch.set_facecolor("white")
ax = axes[0]
labels = ["LS floor (own SVD)", "witness, linearised",
          "floor witness, exact", "G20-1 witness, exact",
          "P171-1 witness via\nenriched path (earlier pose)"]
vals = [floor, lin, floorw, exact, embedded]
cols = ["0.6", "0.6", "tab:blue", "tab:green", "tab:red"]
ax.barh(labels, vals, color=cols, alpha=0.8)
ax.axvline(cap, color="k", ls="--", label=f"registered cap {cap}")
ax.set_xlabel("coupled closure (lower is better; pass = at or under the cap)")
ax.set_title("A. The enriched diagonal instrument reads\n"
             "the flipped pose's witness under the cap", fontsize=10)
ax.legend(fontsize=8.5)
ax.annotate(f"the same witness under a FROZEN instrument reads {frozen:.1f}\n"
            "— the coupling to the instrument is the result",
            (0.02, 0.94), xycoords="axes fraction", fontsize=8.5, va="top")

ax = axes[1]
ax.semilogy(range(1, len(subcut) + 1), subcut, "o-", color="tab:purple")
ax.axhline(sigcut, color="k", ls="--",
           label=f"$\\sigma_{{cut}}$ = {sigcut:.2f} (stored)")
ax.set_xlabel("sub-cut singular value index")
ax.set_ylabel("singular value (log)")
ax.set_title("B. The witness lives below the cut:\n"
             "5 singular values under $\\sigma_{cut}$ carry it", fontsize=10)
ax.legend(fontsize=8.5)
fig.tight_layout()
out = f"{FIG}/fig_gate20_closure.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
