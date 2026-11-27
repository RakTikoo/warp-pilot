#!/usr/bin/env python3
"""Gate-49 bundle figure: the Phase 403 width curve — C395 carried by
Phase 402's registered transport from W10 (pose [10, 20]) to the
registered cap W28 (pose [1, 29]) — with the re-optimised centre at
[1, 29] marked, the gain decomposition stated, and riders G49-E and
G49-F on the figure's face.

Reads ONLY the bundle's own stored records (sources/):
  - sources/g49_numbers.json   Gate-49's deciding reads (the width
                               curve's stored joints — W10/W12/W14
                               filed under controls, W16..W28 under
                               width_curve; the winner's stored joint).
  - sources/g49_recount.json   the gate's decomposition of the gain
                               (transport / re-optimisation / total).
Writes figures/g49_width_curve.png next to this script's bundle root.

The values drawn are the claim's stored values as quoted in
GATE49.md section 8; they are asserted before drawing. Wording
discipline (G49-F): the W28 centre is AT the SS7 criterion with the
construction disclosed — it is never described on this figure as
clearing the bar; C395 is named as the last centre clearing the bar
with a genuine margin.
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


g49 = load("g49_numbers.json")
recount = load("g49_recount.json")

widths = [10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0]
poses = ["[10, 20]", "[9, 21]", "[8, 22]", "[7, 23]",
         "[6, 24]", "[5, 25]", "[3, 27]", "[1, 29]"]
# The gate's record files the W10/W12/W14 reads under controls and
# W16..W28 under width_curve; the stored joints are the claim's values.
joints = [g49["controls"]["C395_home"]["stored"]["joint"],
          g49["controls"]["W12"]["stored"]["joint"],
          g49["controls"]["W14"]["stored"]["joint"]] + \
         [g49["width_curve"][str(w)]["stored"]["joint"] for w in widths[3:]]
expected = [-2.980985e-05, -2.472805e-05, -2.050977e-05, -1.792647e-05,
            -1.571427e-05, -1.393772e-05, -1.128452e-05, -9.384899e-06]
for v, e in zip(joints, expected):
    assert abs(v - e) < 5e-12, (v, e)

centre = g49["winner"]["stored"]["joint"]
assert abs(centre - (-3.676112e-06)) < 5e-12, centre
decomp = recount["decomposition"]
transport = decomp["transport_gain"]
reopt = decomp["reoptimisation_increment"]
total = decomp["total_gain"]
assert abs(transport - 2.0424951526593445e-05) < 1e-18, transport
assert abs(reopt - 5.708787224231813e-06) < 1e-18, reopt
assert abs(total - 2.613373875082526e-05) < 1e-18, total

xs = widths
ys = [v * 1e6 for v in joints]  # plot in units of 1e-6

fig, ax = plt.subplots(figsize=(10.6, 7.4), dpi=200)
ax.plot(xs, ys, "-o", color="#1f4e79", lw=2.2, ms=7, zorder=3,
        label="C395 transported (Phase 402's transport, Phase 403 Step 1)")
ax.plot([28.0], [centre * 1e6], marker="*", color="crimson", ms=22,
        zorder=5, label="Re-optimised centre at W28, pose [1, 29] (Phase 403 Step 2)")
ax.annotate(f"W10, {poses[0]}: {joints[0]:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
            xy=(10.0, ys[0]), xytext=(10.1, ys[0] - 2.6),
            fontsize=9.5, color="#1f4e79", fontweight="bold")
ax.annotate(f"W28 transported: {joints[-1]:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
            xy=(28.0, ys[-1]), xytext=(20.9, ys[-1] - 4.9),
            fontsize=9.5, color="#1f4e79", fontweight="bold")
ax.annotate(f"centre: {centre:.6e}".replace("e-0", "×10⁻").replace("e-", "×10⁻"),
            xy=(28.0, centre * 1e6), xytext=(20.6, centre * 1e6 + 1.15),
            fontsize=10, color="crimson", fontweight="bold")
ax.annotate("gain over C395's home level: transport +2.042495×10⁻⁵,\n"
            "re-optimisation +5.708787×10⁻⁶, total +2.613374×10⁻⁵\n"
            "(G49-D; ρ_min falls +9.780858×10⁻⁵ → +4.705368×10⁻⁵ along the curve:\n"
            "widening spends density margin to buy pressure level)",
            xy=(10.3, -11.6), fontsize=9.2, color="#333333", va="top")
ax.set_xticks(xs)
ax.set_xticklabels([f"W{int(w)}\n{p}" for w, p in zip(widths, poses)], fontsize=8.6)
ax.set_ylabel("joint level  [×10⁻⁶]\n(SET-244, SAMPLER-M, band at each pose)", fontsize=10)
ax.set_xlabel("band width under transport (pose)", fontsize=10)
ax.set_xlim(9.2, 28.8)
ax.set_ylim(-32.5, 1.5)
ax.grid(axis="y", color="#cccccc", lw=0.6, zorder=0)
ax.legend(loc="lower right", fontsize=8.8, framealpha=0.95)
ax.set_title("The width curve and the W28 centre — Gate-49 (v1.40.0)\n"
             "monotone, unturned at the registered cap W28; every level negative",
             fontsize=11, fontweight="bold")

rider_e = ("RIDER G49-E (part of G49-A, G49-B and G49-C wherever their levels are quoted): the centre presses the registered box's\n"
           "μ_S lower edge (0.5000090643041506 against 0.50) and its μ_N upper edge (1.8999807308424006 against 1.90) — the optimum\n"
           "OF THE REGISTERED BOX at pose [1, 29]; behaviour outside the box is unmeasured in this claim set.")
rider_f = ("RIDER G49-F (the SS7 ruling): the centre is quotable as AT the SS7 physicality criterion, not as clearing it with margin,\n"
           "and not as an artefact candidate — its band peak |β·S| is 0.44268227409480604, the half-of-H2 bar (0.4426742490267404)\n"
           "plus 8.025×10⁻⁶, a clearance identically equal to the centre's distance above a box edge the search's own registration\n"
           "placed at the criterion's boundary; the pass certifies the fence, not a margin. The last centre on this line clearing\n"
           "the bar with a genuine margin is Phase 395's (peak ratio 0.6012, clearance 8.958×10⁻²).")
fence = ("FENCE: every level in this set is a band read at its stated pose under transport (the centre's pose is [1, 29]); Phase 356's\n"
         "full-extent caveats travel with every level; every level is negative; no EC pass, no member, no drive implication.")
fig.text(0.055, 0.278, rider_e, fontsize=8.2, color="#7a1f1f", va="top")
fig.text(0.055, 0.190, rider_f, fontsize=8.2, color="#7a1f1f", va="top")
fig.text(0.055, 0.078, fence, fontsize=8.2, color="#333333", va="top")
fig.tight_layout(rect=(0, 0.30, 1, 1))
out = os.path.join(ROOT, "figures", "g49_width_curve.png")
fig.savefig(out)
print("wrote", out)
for w, p, v in zip(widths, poses, joints):
    print(f"  W{int(w):<3d} {p:9s} {v:.15e}")
print(f"  {'centre':13s} {'[1, 29]':9s} {centre:.15e}")
print(f"  transport {transport:.15e}  re-opt {reopt:.15e}  total {total:.15e}")
