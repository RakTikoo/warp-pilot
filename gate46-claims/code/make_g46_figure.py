#!/usr/bin/env python3
"""Gate-46 bundle figure: the stationary-level lineage progression
through Phase 395's centre (C395), with the end-clamped level marked
and rider G46-E on the figure's face.

Reads ONLY the bundle's own stored records (sources/):
  - sources/g46_numbers.json       Gate-46's deciding reads — the
                                   stored joints of the five lineage
                                   reads (H2S, MIX, SEED, ANCHOR =
                                   Phase 394's centre, CENTRE =
                                   Phase 395's centre).
  - sources/g46_clamp_margins.json the gate's clamped-centre value.
Writes figures/g46_level_progression.png next to this script's bundle
root.

The progression stops at C395, as charged for this release: Phase
396's flagged scaling-surface level belongs to the v1.37.0 claim set
(Gate-47, rider G47-F) and is not drawn here. Rider G46-E and the
section-5 fence are printed on the figure's face.
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


g46 = load("g46_numbers.json")
margins = load("g46_clamp_margins.json")

configs = g46["configs"]
clamped = margins["CENTRE"]["stored_clamped_joint"]
assert abs(clamped - (-3.0189206094012074e-05)) < 1e-18

stages = [
    ("H2 centre\nPhase 379 · Gate-41\n$L_{stat}$(H2)", configs["H2S"]["stored"]["nec"]),
    ("Mixed centre\nPhase 389 · Gate-43", configs["MIX"]["stored"]["nec"]),
    ("Ray point (seed)\nPhase 393", configs["SEED"]["stored"]["nec"]),
    ("Second-region centre\nPhase 394 · Gate-45", configs["ANCHOR"]["stored"]["nec"]),
    ("Widened-box centre\nPhase 395 · Gate-46\nthe standing design centre",
     configs["CENTRE"]["stored"]["nec"]),
]
# The values the figure draws are the stored levels quoted in
# GATE46.md section 5; assert them before drawing.
expected = [-1.9422459891767227e-04, -1.7570735537945242e-04,
            -1.2413718983790085e-04, -6.812652656191736e-05,
            -2.9809850277749006e-05]
for (_, v), e in zip(stages, expected):
    assert abs(v - e) < 1e-17, (v, e)

xs = list(range(len(stages)))
ys = [v * 1e4 for _, v in stages]  # plot in units of 1e-4
clamped_y = clamped * 1e4

fig, ax = plt.subplots(figsize=(10.6, 6.6), dpi=200)
ax.axhline(0.0, color="crimson", lw=1.4)
ax.text(-0.42, 0.055, "0 — an energy-condition pass (not reached)",
        color="crimson", fontsize=9, ha="left", va="bottom")
ax.plot(xs, ys, "-o", color="#1f4e79", lw=2.0, ms=7, zorder=3)
# The clamped level (-3.018921e-5) sits 3.79e-7 below the centre's
# level — indistinguishable at this scale, so it is drawn as a ring
# on the centre point and labelled; the exact value is in the label
# and in G46-C.
ax.plot([xs[-1]], [clamped_y], marker="o", mfc="none", mec="#b06000",
        mew=2.0, ms=15, zorder=4)
for x, (_, v), y in zip(xs, stages, ys):
    ax.annotate(f"{v:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
                xy=(x, y), xytext=(x, y + 0.15), fontsize=9.5,
                ha="center", color="#1f4e79", fontweight="bold")
ax.annotate(f"ring: same centre, end-clamped (G46-C):\n{clamped:.6e} (clamp cost 3.794×10⁻⁷)".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
            xy=(xs[-1], clamped_y), xytext=(3.30, -0.80),
            fontsize=9, ha="center", color="#7a4a00",
            arrowprops=dict(arrowstyle="->", color="#b06000", lw=0.9))
ax.set_xticks(xs)
ax.set_xticklabels([s for s, _ in stages], fontsize=8.5)
ax.set_ylabel("stationary joint level  [×10⁻⁴]\n(SET-244, SAMPLER-M, band [10, 20])",
              fontsize=10)
ax.set_xlim(-0.45, 4.45)
ax.set_ylim(-2.15, 0.42)
ax.grid(axis="y", color="#cccccc", lw=0.6, zorder=0)
ax.set_title("The stationary pressure level, A2 lineage — Gate-46 (v1.38.0)\n"
             "Phase 395's centre: −2.980985×10⁻⁵, gate-verified — the scaling line's\n"
             "standing design centre (Gate-47's naming, v1.37.0)",
             fontsize=11, fontweight="bold")
note = ("NOTE: the progression stops at Phase 395's centre, as charged for this release. Phase 396's further\n"
        "scaling-surface level (−7.431892×10⁻⁶) belongs to the v1.37.0 claim set, where Gate-47 ruled it a\n"
        "scaling-surface level only, not a design improvement (rider G47-F); it is not drawn here.")
rider_e = ("RIDER G46-E (part of G46-A/B/C wherever their levels are quoted): the Phase 395 centre presses the\n"
           "registered extended box's μ_S lower edge (0.601180962300002 vs 0.60, by 0.00118) and nears its μ_N upper\n"
           "edge (1.5934531363763935 vs 1.60, by 0.00655); the centre is the optimum OF THE REGISTERED EXTENDED BOX,\n"
           "and whether the level keeps rising outside the box is unmeasured in this claim set.")
fence = ("FENCE: band pose [10, 20] only; Phase 356's full-extent caveats travel with every level; "
         "every level is negative —\nno EC pass, no member, no drive or transport implication.")
fig.text(0.065, 0.262, note, fontsize=8.6, color="#333333", va="top")
fig.text(0.065, 0.168, rider_e, fontsize=8.6, color="#7a1f1f", va="top")
fig.text(0.065, 0.062, fence, fontsize=8.6, color="#333333", va="top")
fig.tight_layout(rect=(0, 0.285, 1, 1))
out = os.path.join(ROOT, "figures", "g46_level_progression.png")
fig.savefig(out)
print("wrote", out)
for s, v in stages:
    print(f"  {s.splitlines()[0]:24s} {v:.15e}")
print(f"  {'clamped centre':24s} {clamped:.15e}")
