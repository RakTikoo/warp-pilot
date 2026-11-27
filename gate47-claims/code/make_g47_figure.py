#!/usr/bin/env python3
"""Gate-47 bundle figure: the stationary-level lineage progression,
with the G47-F certified/flagged boundary.

Reads ONLY the bundle's own stored records (sources/):
  - sources/g47_numbers.json       Gate-47's deciding reads — the joints
                                   of all six lineage reads (H2, MIX,
                                   SEED, C394, ANCHOR = Phase 395's
                                   centre, CENTRE = Phase 396's centre).
  - sources/g47_clamp_margins.json the gate's clamped-centre value.
  - sources/g47_degeneracy.json    the gate's physicality table (peak
                                   |beta*S| per configuration) and its
                                   one-factor gain attribution.
Writes figures/g47_level_progression.png next to this script's bundle
root.

The certified/flagged boundary (G47-F: a centre is quotable as a
design improvement only while its peak |beta*S| is at least half of
H2's peak), riders G47-E and G47-F, the one-factor attribution, and
the section-5 fence are printed on the figure's face, as charged.
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


g47 = load("g47_numbers.json")
margins = load("g47_clamp_margins.json")
degen = load("g47_degeneracy.json")

reads = g47["reads"]
clamped = margins["clamped_centre_joint"]
assert abs(clamped - g47["clamps"]["CENTRE"]["joint"]) < 1e-18

phys = degen["physicality"]
peak = {k: v["peak_abs_beta_S"] for k, v in phys.items()}
half_h2 = 0.5 * peak["H2"]

stages = [
    ("H2 centre\nPhase 379 · Gate-41\n$L_{stat}$(H2)", reads["H2"]["joint"]),
    ("Mixed centre\nPhase 389 · Gate-43", reads["MIX"]["joint"]),
    ("Ray point (seed)\nPhase 393", reads["SEED"]["joint"]),
    ("Second-region centre\nPhase 394 · Gate-45", reads["C394"]["joint"]),
    ("Widened-box centre\nPhase 395 · Gate-46\ndesign-quotable limit",
     reads["ANCHOR"]["joint"]),
    ("Third-widening centre\nPhase 396 · Gate-47\nsurface level only",
     reads["CENTRE"]["joint"]),
]

xs = list(range(len(stages)))
ys = [v * 1e4 for _, v in stages]  # plot in units of 1e-4
clamped_y = clamped * 1e4

fig, ax = plt.subplots(figsize=(10.6, 6.6), dpi=200)
ax.axhline(0.0, color="crimson", lw=1.4)
ax.text(-0.42, 0.055, "0 — an energy-condition pass (not reached)",
        color="crimson", fontsize=9, ha="left", va="bottom")
# The G47-F certified/flagged boundary, between C395 and C396: C396's
# peak |beta*S| (0.354) falls below half of H2's peak (0.885); C395's
# (0.532) clears it. Centres left of the line are design-quotable;
# C396 is a scaling-surface level only.
ax.axvline(4.5, color="#7a1f1f", lw=1.3, ls="--", zorder=1)
ax.text(4.44, 0.33, "G47-F boundary: peak |β·S| ≥ ½ H2's peak —\n"
        "left: design-quotable · right: surface level only",
        color="#7a1f1f", fontsize=8.8, ha="right", va="top")
ax.plot(xs, ys, "-o", color="#1f4e79", lw=2.0, ms=7, zorder=3)
# The clamped level (-7.644644e-6) sits 2.13e-7 below the centre's
# level — indistinguishable at this scale, so it is drawn as a ring
# on the centre point and labelled; the exact value is in the label
# and in G47-C.
ax.plot([xs[-1]], [clamped_y], marker="o", mfc="none", mec="#b06000",
        mew=2.0, ms=15, zorder=4)
for x, (_, v), y in zip(xs, stages, ys):
    ax.annotate(f"{v:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
                xy=(x, y), xytext=(x, y + 0.15), fontsize=9.5,
                ha="center", color="#1f4e79", fontweight="bold")
ax.annotate(f"ring: same centre, end-clamped (G47-C):\n{clamped:.6e} (clamp cost 2.128×10⁻⁷)".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
            xy=(xs[-1], clamped_y), xytext=(4.28, -0.80),
            fontsize=9, ha="center", color="#7a4a00",
            arrowprops=dict(arrowstyle="->", color="#b06000", lw=0.9))
ax.set_xticks(xs)
ax.set_xticklabels([s for s, _ in stages], fontsize=8.5)
ax.set_ylabel("stationary joint level  [×10⁻⁴]\n(SET-244, SAMPLER-M, band [10, 20])",
              fontsize=10)
ax.set_xlim(-0.45, 5.45)
ax.set_ylim(-2.15, 0.42)
ax.grid(axis="y", color="#cccccc", lw=0.6, zorder=0)
ax.set_title("The stationary pressure level, A2 lineage — Gate-47 (v1.37.0)\n"
             "Phase 396's centre: −7.431892×10⁻⁶, gate-verified as a scaling-surface level\n"
             "(G47-F: not a design improvement — the standing design centre is Phase 395's, −2.980985×10⁻⁵)",
             fontsize=11, fontweight="bold")
attribution = ("ONE-FACTOR ATTRIBUTION of the Phase 395 → Phase 396 gain (+2.237796×10⁻⁵), gate-measured (G47-F):\n"
               "μ_S alone buys 77% (+1.726871×10⁻⁵) · μ_N alone 46% (+1.027234×10⁻⁵) · μ_M alone 5% (+1.034923×10⁻⁶);\n"
               "interaction ≈ −6.2×10⁻⁶ — shift removal is the dominant single purchaser of the gain.")
rider_e = ("RIDER G47-E (part of G47-A/B/C wherever their levels are quoted): the Phase 396 centre presses the\n"
           "registered box's μ_S lower edge (0.4003528067864536 vs 0.40) and nears its μ_N upper edge (vs 2.00) — the\n"
           "third widening in a row at the new μ_S edge; the centre is the optimum OF THE REGISTERED BOX.")
rider_f = ("RIDER G47-F (part of G47-A/B/C wherever their levels are quoted): the Phase 396 centre is quotable only as a\n"
           "scaling-surface level, NOT as a design improvement — peak |β·S| 0.35445175617988206 = 40.0% of H2's peak\n"
           "0.8853484980534808, below the pre-registered half-of-H2 bar; the last centre clearing the bar is Phase 395's.")
fence = ("FENCE: band pose [10, 20] only; Phase 356's full-extent caveats travel with every level; "
         "every level is negative —\nno EC pass, no member, no drive or transport implication.")
fig.text(0.065, 0.298, attribution, fontsize=8.6, color="#333333", va="top")
fig.text(0.065, 0.218, rider_e, fontsize=8.6, color="#7a1f1f", va="top")
fig.text(0.065, 0.140, rider_f, fontsize=8.6, color="#7a1f1f", va="top")
fig.text(0.065, 0.062, fence, fontsize=8.6, color="#333333", va="top")
fig.tight_layout(rect=(0, 0.315, 1, 1))
out = os.path.join(ROOT, "figures", "g47_level_progression.png")
fig.savefig(out)
print("wrote", out)
for s, v in stages:
    print(f"  {s.splitlines()[0]:24s} {v:.15e}")
print(f"  {'clamped centre':24s} {clamped:.15e}")
print(f"  peaks |beta*S|: H2 {peak['H2']:.15f}  C394 {peak['C394']:.15f}  "
      f"C395 {peak['ANCHOR']:.15f}  C396 {peak['BEST']:.15f}  half-H2 {half_h2:.15f}")
