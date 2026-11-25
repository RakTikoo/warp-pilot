#!/usr/bin/env python3
"""Gate-21 figure: the flipped pose's gate holds at lambda = 0.10 and the
Type-I flip at site 44 kills it by lambda = 0.1452.

Sources (stored):
  gate21-claims/results/g21_verify_out.json   (witness closure, spectrum)
  gate21-claims/results/g21_verify2_out.json  (the flip mechanism per lambda)
The 0.63 cap is extracted from the stored claim record GATE20.md/GATE21
claim text pattern (the same registered cap as Gate-20), never typed.
"""
import json
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
d = json.load(open(f"{ROOT}/gate21-claims/results/g21_verify_out.json"))
d2 = json.load(open(f"{ROOT}/gate21-claims/results/g21_verify2_out.json"))
gate_doc = open(f"{ROOT}/gate21-claims/GATE21.md").read()
cap = float(re.search(r"closure [\d.]+ ≤ ([\d.]+),", gate_doc).group(1))

fm = d2["flip_mechanism"]
lams = sorted(float(k) for k in fm)
q44 = [fm[f"{l:g}"]["q44"] for l in lams]
t44 = [fm[f"{l:g}"]["typeI44"] for l in lams]
closure = d["witness_exact"]["closure"]
lin63 = d["mint063_linearised"]["lin_closure"]

fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6))
fig.patch.set_facecolor("white")
ax = axes[0]
ax.plot(lams, q44, "o-", color="k")
for l, q, t in zip(lams, q44, t44):
    ax.annotate("Type-I at site 44" if t else "site 44 not Type-I",
                (l, q), textcoords="offset points", xytext=(6, 8),
                fontsize=8.5, color="tab:red" if t else "tab:green")
ax.set_xlabel(r"enrichment $\lambda$")
ax.set_ylabel(r"site-44 read $q_{44}$")
ax.set_title("A. The failure mechanism: site 44 flips\n"
             "to Type-I between $\\lambda$ = 0.10 and 0.11", fontsize=10)

ax = axes[1]
ax.bar(["G21-1 witness, exact\nclosure at $\\lambda$ = 0.10",
        "minted-at-cap field,\nlinearised closure"],
       [closure, lin63], color=["tab:green", "0.6"])
ax.axhline(cap, color="k", ls="--", label=f"registered cap {cap}")
ax.set_ylabel("coupled closure")
ax.set_title("B. At $\\lambda$ = 0.10 the exact read holds\n"
             "under the cap (fenced, restated claim)", fontsize=10)
ax.legend(fontsize=8.5)
fig.tight_layout()
out = f"{FIG}/fig_gate21_lambda.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
