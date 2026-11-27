#!/usr/bin/env python3
"""Figure generator for the Gate-54 claims bundle (release v1.45.0).

Reads ONLY the bundled records in ../sources/ (g54_results.json:
Gate-54's own deciding reads) and writes ../figures/g54_channels.png.

Left panel: Gate-54's per-site maximum |channel diff| between the
supplier tensor T_sup and the required tensor T_req over all
NEC/WEC/DEC/SEC eigen-channels, at the eight site reads (Phase 410
claim (b), Gate-54 claim_b), against the quotable bound
<= 1.34e-12 (rider G54-R2).
Right panel: the supplier's density at the same eight reads
(Gate-54 claim_c) -- positive at every read.
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources", "g54_results.json")
OUT = os.path.join(HERE, "..", "figures", "g54_channels.png")

SITES = [
    "A1_joint_argmin",
    "A2_sec_argmin",
    "A3_peak",
    "B_stencil_-1.0",
    "B_stencil_-0.5",
    "B_stencil_+0.0",
    "B_stencil_+0.5",
    "B_stencil_+1.0",
]
LABELS = ["A1", "A2", "A3", "B-1.0", "B-0.5", "B+0.0", "B+0.5", "B+1.0"]
BOUND = 1.34e-12  # rider G54-R2: the quotable decomposition bound

with open(SRC) as f:
    g = json.load(f)

diffs = [g["claim_b"]["per_site"][s]["max_channel_diff"] for s in SITES]
rhos = list(g["claim_c"]["fitA"]["rhos_sup"]) + list(
    g["claim_c"]["fitB"]["rhos_sup"]
)
assert len(rhos) == 8 and all(r > 0 for r in rhos)
assert max(diffs) <= BOUND, max(diffs)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6))

ax = axes[0]
ax.bar(LABELS, diffs, color="#305496")
ax.axhline(BOUND, color="#C00000", linestyle="--", linewidth=1.2)
ax.text(
    7.45,
    BOUND * 1.6,
    "quotable bound 1.34e-12 (G54-R2)",
    color="#C00000",
    ha="right",
    fontsize=8,
)
ax.set_yscale("log")
ax.set_ylim(1e-15, 1e-10)
ax.set_ylabel("max |channel diff|  |T_sup - T_req| (eigen-channels)")
ax.set_title(
    "Gate-54 claim (b): the supplier misses no channel\n"
    "max over NEC/WEC/DEC/SEC channels, per site read",
    fontsize=10,
)

ax = axes[1]
ax.bar(LABELS, rhos, color="#548235")
ax.set_ylabel("supplier density  rho_sup = T_sup[0,0]")
ax.set_title(
    "Gate-54 claim (c): supplier density positive\nat every site read",
    fontsize=10,
)

fig.suptitle(
    "Phase 410 spinor supply of the Phase 405 winner, as re-judged by Gate-54",
    fontsize=12,
)
fig.text(
    0.5,
    0.005,
    "Fences: site mating is not extent coverage. Sourcing is not curing -- the sourced tensor violates SEC as it stands\n"
    "(-2.213557e-4 at A2); NO no-exotic-matter claim attaches to any sourced design. Novelty NONE for the method\n"
    "(Martin-Moruno & Visser 2021, Gate-25). Data: bundled sources/g54_results.json only.",
    ha="center",
    fontsize=8,
)
fig.tight_layout(rect=(0, 0.06, 1, 0.94))
fig.savefig(OUT, dpi=200)
print("wrote", OUT)
print("max channel diff:", max(diffs), "<= bound", BOUND)
print("densities:", rhos)
