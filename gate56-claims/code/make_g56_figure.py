#!/usr/bin/env python3
"""Figure generator for the Gate-56 claims bundle (release v1.47.0).

Reads ONLY the bundled records in ../sources/ (g56_reads.json:
Gate-56's own deciding reads) and writes
../figures/g56_spend_landscape.png.

Left panel: the criterion spend floor comparison at matched peaks
(Gate-56 claim (b), G56-B) -- the criterion spend (static joint
minus carried joint at the SS7 criterion) on the three bases:
B418 1.254e-9 < Phase 400's base 1.703e-7 < B1 1.086e-5
(stored-joint form, the quotable one under rider G56-R3).
Right panel: the transect landscape (Gate-56 claim (d), G56-D) --
along the 400-base -> B1 transect the static joint rises
monotonically toward B1 while the carried joint peaks in the
interior (mu_M ~ 6.36) and collapses at the B1 end. Gate reads;
the two B1-end carried reads carry the G56-R3 frame-convention
band (their argmins are non-Type-I) and are plotted as read.
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources", "g56_reads.json")
OUT = os.path.join(HERE, "..", "figures", "g56_spend_landscape.png")

with open(SRC) as f:
    g = json.load(f)

sc = g["b_spend_comparison"]
bases = ["B418", "400's base", "B1"]
spends = [sc["SPEND_B418_stored"], sc["SPEND_400_stored"],
          sc["SPEND_B1_stored"]]
assert spends[0] < spends[1] < spends[2]

tr = g["d_transect"]
ts = sorted(tr.keys(), key=float)
tvals = [float(t) for t in ts]
muM = [tr[t]["muM_stored"] for t in ts]
static = [tr[t]["static_gate"] * 1e6 for t in ts]
carried = [tr[t]["carried_gate"] * 1e6 for t in ts]

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))

ax = axes[0]
cols = ["#548235", "#305496", "#C00000"]
ax.bar(range(3), spends, color=cols)
ax.set_yscale("log")
ax.set_xticks(range(3))
ax.set_xticklabels(bases)
ax.set_ylabel("criterion spend (static - carried joint)")
for i, v in enumerate(spends):
    ax.annotate(f"{v:.3e}", (i, v), textcoords="offset points",
                xytext=(0, 4), ha="center", fontsize=8.5)
ax.set_title(
    "Gate-56 claim (b): the criterion spend floor -- B418's\n"
    "spend is ~136x below 400's base and ~8,660x below B1",
    fontsize=10,
)

ax = axes[1]
ax.plot(tvals, static, "o-", color="#305496", label="static joint")
ax.plot(tvals, carried, "s-", color="#548235", label="carried joint")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xlabel("transect t (0 = 400's base, 1 = B1; mu_M 11.34 -> 3.03)")
ax.set_ylabel("joint ($\\times 10^{-6}$)")
ax.legend(fontsize=8.5, loc="lower left")
ax.set_title(
    "Gate-56 claim (d): static rises monotonically to B1;\n"
    "the carried joint peaks in the interior, collapses at B1",
    fontsize=10,
)

fig.suptitle(
    "Phase 418's carrying-aware hunt, as re-judged by Gate-56",
    fontsize=12,
)
fig.text(
    0.5,
    0.005,
    "Fences: band [10, 20] on every figure. NO member, NO EC pass: SEC at the carried point is\n"
    "-5.294469e-4, printed on its face (G56-A). The peak is at the criterion -- H2's own peak halved,\n"
    "by the SS7 definition -- the shape scaled to the criterion target (rider G56-R1). B418 is a\n"
    "CRITERION SPECIALIST: it carries nothing at 2x in the registered search (G56-R2) and 412's P*\n"
    "remains the 2x carrier of record (G56-R5). Non-Type-I sampled joints carry the C-10 band (G56-R3).\n"
    "Data: bundled sources/g56_reads.json only.",
    ha="center",
    fontsize=8,
)
fig.tight_layout(rect=(0, 0.16, 1, 0.94))
fig.savefig(OUT, dpi=200)
print("wrote", OUT)
print("spends:", spends)
print("transect t:", tvals)
print("static:", static)
print("carried:", carried)
