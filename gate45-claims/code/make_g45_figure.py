#!/usr/bin/env python3
"""Gate-45 bundle figure: the stationary-level lineage progression.

Reads ONLY the bundle's own stored records (sources/):
  - sources/p394_controls.json   Phase 394's controls — the stored joints
                                 for (1,1,1) = L_stat(H2), the Phase 389
                                 mixed centre, and the Phase 393 seed
                                 (joint = min(NEC min, DEC min) per read).
  - sources/g45_numbers.json     Gate-45's deciding reads — the Phase 394
                                 centre (CENTRE) and its end-clamped read
                                 (CENTRE_CLAMP), joints likewise.
  - sources/g45_clamp_margins.json  the gate's clamped-centre value.
Writes figures/g45_level_progression.png next to this script's bundle root.

The G45-E box-edge rider and the section-5 fence are printed on the
figure's face, as charged.
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


ctl = load("p394_controls.json")["controls"]
g45 = load("g45_numbers.json")
margins = load("g45_clamp_margins.json")


def joint_ctl(key):
    r = ctl[key]
    return min(r["nec_min"], r["dec_min"])


def joint_gate(key):
    r = g45[key]["read"]
    return min(r["nec"]["min"], r["dec"]["min"])


stages = [
    ("H2 centre\nPhase 379 · Gate-41\n$L_{stat}$(H2)", joint_ctl("CTL-394-H2S")),
    ("Mixed centre\nPhase 389 · Gate-43", joint_ctl("CTL-394-MIX")),
    ("Ray point (seed)\nPhase 393", joint_ctl("CTL-394-SEED")),
    ("Ray-seeded centre\nPhase 394 · Gate-45", joint_gate("CENTRE")),
]
clamped = margins["clamped_centre_gate"]
assert abs(clamped - joint_gate("CENTRE_CLAMP")) < 1e-18

xs = list(range(len(stages)))
ys = [v * 1e4 for _, v in stages]  # plot in units of 1e-4
clamped_y = clamped * 1e4

fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
ax.axhline(0.0, color="crimson", lw=1.4)
ax.text(-0.42, 0.055, "0 — an energy-condition pass (not reached)",
        color="crimson", fontsize=9, ha="left", va="bottom")
ax.plot(xs, ys, "-o", color="#1f4e79", lw=2.0, ms=7, zorder=3)
# The clamped level (-6.968823e-5) sits 1.56e-6 below the centre's level --
# indistinguishable at this scale, so it is drawn as a ring on the centre
# point and labelled; the exact value is in the label and in G45-C.
ax.plot([xs[-1]], [clamped_y], marker="o", mfc="none", mec="#b06000",
        mew=2.0, ms=15, zorder=4)
for x, (_, v), y in zip(xs, stages, ys):
    ax.annotate(f"{v:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
                xy=(x, y), xytext=(x, y + 0.15), fontsize=9.5,
                ha="center", color="#1f4e79", fontweight="bold")
ax.annotate(f"ring: same centre, end-clamped (G45-C):\n{clamped:.6e} (clamp cost 1.562×10⁻⁶)".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
            xy=(xs[-1], clamped_y), xytext=(1.95, -0.52),
            fontsize=9, ha="center", color="#7a4a00",
            arrowprops=dict(arrowstyle="->", color="#b06000", lw=0.9))
ax.set_xticks(xs)
ax.set_xticklabels([s for s, _ in stages], fontsize=9.5)
ax.set_ylabel("stationary joint level  [×10⁻⁴]\n(SET-244, SAMPLER-M, band [10, 20])",
              fontsize=10)
ax.set_xlim(-0.45, 3.45)
ax.set_ylim(-2.15, 0.30)
ax.grid(axis="y", color="#cccccc", lw=0.6, zorder=0)
ax.set_title("The stationary pressure level, A2 lineage — Gate-45 (v1.36.0)\n"
             "Phase 394's ray-seeded centre: −6.812653×10⁻⁵, gate-verified",
             fontsize=11.5, fontweight="bold")
rider = ("RIDER G45-E (part of G45-A/B/C wherever their levels are quoted): the Phase 394 centre\n"
         "presses the registered box's μ_S lower edge (0.8015689430763502 vs 0.80) and the pure μ_M ray\n"
         "was still rising at the box's μ_M edge (3.60) — the centre is the optimum OF THE REGISTERED BOX;\n"
         "whether the level keeps rising outside the box is unmeasured in this claim set.")
fence = ("FENCE: band pose [10, 20] only; Phase 356's full-extent caveats travel with every level; "
         "every level is negative —\nno EC pass, no member, no drive or transport implication.")
fig.text(0.07, 0.145, rider, fontsize=8.6, color="#7a1f1f", va="top")
fig.text(0.07, 0.045, fence, fontsize=8.6, color="#333333", va="top")
fig.tight_layout(rect=(0, 0.20, 1, 1))
out = os.path.join(ROOT, "figures", "g45_level_progression.png")
fig.savefig(out)
print("wrote", out)
for s, v in stages:
    print(f"  {s.splitlines()[0]:24s} {v:.15e}")
print(f"  {'clamped centre':24s} {clamped:.15e}")
