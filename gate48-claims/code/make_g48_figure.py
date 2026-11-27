#!/usr/bin/env python3
"""Gate-48 bundle figure: the static line of the A2 lineage — Phase
397's Trace-A endpoint, Phase 398's static winner, Phase 400's winner —
with the zero line marked, Phase 400's stage bests in an inset, and
rider G48-E on the figure's face.

Reads ONLY the bundle's own stored records (sources/):
  - sources/g48_numbers.json   Gate-48's deciding reads (endpoint_A,
                               anchor, winner: gate SET-244 nec_min).
  - sources/g48_recount.json   the gate's recount of Phase 400's 981
                               screens (stage_bests, stage_A_crossing).
Writes figures/g48_static_line.png next to this script's bundle root.

The values drawn are the gate's numbers quoted in GATE48.md section 6;
they are asserted before drawing. The zero line is the joint
min(NEC, DEC)'s zero — crossing it is NOT an energy-condition pass:
SEC, outside that joint, remains -2.050292e-4 at the winner (G48-E).
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    with open(os.path.join(ROOT, "sources", name)) as f:
        return json.load(f)


g48 = load("g48_numbers.json")
recount = load("g48_recount.json")

endpoint = g48["endpoint_A"]["set"]["nec_min"]
anchor = g48["anchor"]["set"]["nec_min"]
winner = g48["winner"]["set"]["nec_min"]
sec_winner = g48["winner"]["set"]["sec_min"]
# The gate's deciding reads, as quoted in GATE48.md section 6.
assert abs(endpoint - (-6.587072e-07)) < 5e-13, endpoint
assert abs(anchor - (-2.599171e-07)) < 5e-13, anchor
assert abs(winner - 1.3977194851287427e-06) < 1e-18, winner
assert abs(sec_winner - (-2.050291598674923e-04)) < 1e-15, sec_winner

stage_labels = ["anchor\n(398 winner)", "A", "B", "C", "D", "E"]
stage_vals = [anchor] + [recount["stage_bests"][s]["pure_min"]
                         for s in ["A", "B", "C", "D", "E"]]
expected_stages = [-2.599171e-07, 1.230765e-06, 1.123691e-07,
                   1.308679e-06, 1.311540e-06, 1.397719e-06]
for v, e in zip(stage_vals, expected_stages):
    assert abs(v - e) < 5e-13, (v, e)
crossing = recount["stage_A_crossing"]["pure_min"]
assert abs(crossing - 1.5792476403001996e-07) < 1e-18, crossing

static_labels = ["Phase 397 endpoint\n(ridge terminus, Trace-A)",
                 "Phase 398 winner\n(the static floor)",
                 "Phase 400 winner\nGate-48 verified"]
static_vals = [endpoint, anchor, winner]

xs = list(range(len(static_vals)))
ys = [v * 1e6 for v in static_vals]  # plot in units of 1e-6

fig, ax = plt.subplots(figsize=(10.6, 6.8), dpi=200)
ax.axhline(0.0, color="crimson", lw=1.5, zorder=2)
ax.text(-0.42, -1.10, "0 — the joint min(NEC, DEC)'s zero line\n"
                      "(crossed by the static line; NOT an EC pass —\n"
                      "SEC remains negative, rider G48-E)",
        color="crimson", fontsize=8.8, ha="left", va="bottom")
ax.plot(xs, ys, "-o", color="#1f4e79", lw=2.2, ms=8, zorder=3)
for x, v, y in zip(xs, static_vals, ys):
    ax.annotate(f"{v:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
                xy=(x, y), xytext=(x, y + (0.34 if v < 0 else 0.30)),
                fontsize=10, ha="center", color="#1f4e79",
                fontweight="bold")
ax.set_xticks(xs)
ax.set_xticklabels(static_labels, fontsize=9)
ax.set_ylabel("static joint level  [×10⁻⁶]\n(SET-244, SAMPLER-M, band [10, 20], S ≡ 0)",
              fontsize=10)
ax.set_xlim(-0.45, 2.45)
ax.set_ylim(-1.15, 2.15)
ax.grid(axis="y", color="#cccccc", lw=0.6, zorder=0)
ax.set_title("The static line, A2 lineage — Gate-48 (v1.39.0)\n"
             "Phase 400's winner: +1.397719×10⁻⁶ — the lineage's first non-negative\n"
             "static band level (an internal first; see the claim gate in this bundle)",
             fontsize=11, fontweight="bold")

# Inset: Phase 400's stage bests (the zero crossing lies inside Stage A).
axin = fig.add_axes((0.135, 0.555, 0.325, 0.285))
sxs = list(range(len(stage_vals)))
sys_ = [v * 1e6 for v in stage_vals]
axin.axhline(0.0, color="crimson", lw=1.1)
axin.plot(sxs, sys_, "-o", color="#7a4a00", lw=1.6, ms=4.5)
axin.plot([1], [crossing * 1e6], marker="*", color="crimson", ms=13,
          zorder=4)
axin.set_xticks(sxs)
axin.set_xticklabels(stage_labels, fontsize=6.4)
axin.tick_params(labelsize=6.8)
axin.set_title("Phase 400 stage bests — 981 screens, zero rejected\n"
               "(* first positive screen, Stage A index 15)",
               fontsize=7.6)
axin.grid(axis="y", color="#dddddd", lw=0.5)

rider_e = ("RIDER G48-E (part of G48-A and G48-B wherever their levels are quoted): no member and no EC pass is claimed\n"
           "or implied — the configuration is static (S ≡ 0, warpless) and has no drive content; the quoted level is the\n"
           "lineage's joint min(NEC, DEC), and SEC, outside that joint, is measured at the winner at −2.050292×10⁻⁴, so\n"
           "the full set of energy conditions does not hold at this configuration. Under Phase 397's fitted carried law\n"
           "(an estimate, not a measurement) the margin would buy back the shift only to μ_S* = 0.271 / 0.282, below the\n"
           "0.5 warp criterion; Phase 404's direct measurement supersedes those figures when it lands.")
fence = ("FENCE: band pose [10, 20] only; Phase 356's full-extent caveats travel with every level in this set; the object\n"
         "is static (S ≡ 0); SEC's measured status is on the face of the set (G48-E); no EC pass, no member, no drive implication.")
fig.text(0.065, 0.205, rider_e, fontsize=8.4, color="#7a1f1f", va="top")
fig.text(0.065, 0.062, fence, fontsize=8.4, color="#333333", va="top")
fig.tight_layout(rect=(0, 0.235, 1, 1))
out = os.path.join(ROOT, "figures", "g48_static_line.png")
fig.savefig(out)
print("wrote", out)
for s, v in zip(static_labels, static_vals):
    print(f"  {s.splitlines()[0]:24s} {v:.15e}")
for s, v in zip(stage_labels, stage_vals):
    print(f"  stage {s.splitlines()[0]:16s} {v:.15e}")
print(f"  {'SEC at winner':24s} {sec_winner:.15e}")
