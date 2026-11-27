#!/usr/bin/env python3
"""Figure generator for the Gate-50 claims bundle (release v1.42.0).

Reads ONLY the bundled records in ../sources/ (Gate-50's deciding
records and stored inputs, and Phase 405's confirmation record) and
writes ../figures/g50_shape_and_cost.png: (left) the winning free
shape's |beta*S| profile over the band [10, 20] at the SS7
criterion, with the fixed shape's stored local reads at the same
criterion marked for comparison; (right) the two shapes' joint vs
peak |beta*S| on Phase 400's static base (Gate-50 deciding reads),
with the winner's confirmations, the criterion spends, riders
G50-R2/G50-R5 and the SEC value on the figure's face.

The winner's profile is evaluated with scipy's not-a-knot
CubicSpline through its stored criterion knot vector -- the
registered p341 spline form (Gate-50 CAL-1 verified the gate's own
not-a-knot implementation against scipy CubicSpline at 2.1e-15).
The fixed shape's full profile is a base-plus-correction stack and
is not a bundled spline, so it is shown at its stored local reads
(Phase 404's ladder at mu_S = 0.5, bundled in
g50_stored_inputs.json) rather than as an invented curve.
"""
import json
import os

import numpy as np
from scipy.interpolate import CubicSpline

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources")
OUT = os.path.join(HERE, "..", "figures", "g50_shape_and_cost.png")

BETA = 1.1
FRAGILE_R = 17.926829268292682

# --- bundled records --------------------------------------------------
num = json.load(open(os.path.join(SRC, "g50_numbers.json")))
inp = json.load(open(os.path.join(SRC, "g50_stored_inputs.json")))
conf = json.load(open(os.path.join(SRC, "p405_confirmation.json")))

peaks = num["claim_b_peaks"]
costs = num["claim_c_costs"]
bar = peaks["SS7_bar_stored"]                    # 0.4426742490267404
h2_peak = peaks["H2_FINE_R"]["peak"]             # 0.8853484980534808

base_joint = costs["base_joint"]                 # gate CTL-A read
win_joint_crit = num["claim_a_winner"]["joint"]
win_worst_null = num["claim_a_winner"]["worst_null_at_nec_argmin"]
win_polish = json.load(open(os.path.join(SRC, "g50_polish.json")))[
    "winner405"]["polish"]["in_region_worst_nec_SAMPLER-M"]
sec_min = num["claim_a_winner"]["summary"]["sec"]["min"]

# --- profiles ---------------------------------------------------------
# The winner's S sector IS the free spline (the base has S = 0), so its
# stored criterion knot vector is the whole shape.
win_knots_r = np.array(conf["knot_radii_K9"], dtype=float)
win_knots_v = np.array(conf["shapeC_knots_at_criterion"], dtype=float)
win_spline = CubicSpline(win_knots_r, win_knots_v, bc_type="not-a-knot")

r = np.linspace(10.0, 20.0, 801)
win_prof = np.abs(BETA * win_spline(r))

# Fixed shape at the criterion (mu_S = 0.5): stored local reads from
# Phase 404's ladder, bundled in g50_stored_inputs.json -- the peak
# (S_range max, at r = 10) and S at its NEC / DEC argmin radii.
lad = inp["ladder404"]["0.5"]
fix_marks = [
    (10.0, BETA * lad["S_range"][1]),
    (lad["nec_argmin_r"], BETA * lad["local_at_nec_argmin"]["S"]),
    (lad["dec_argmin_r"], BETA * lad["local_at_dec_argmin"]["S"]),
]

# --- joint-vs-peak reads (Gate-50 deciding reads) ---------------------
win_pts = [
    (0.0, base_joint),
    (0.05, num["winner_p0.05"]["joint"]),
    (0.25, num["winner_p0.25"]["joint"]),
    (bar, win_joint_crit),
]
fix_pts = [
    (0.0, base_joint),
    (0.05 * h2_peak, num["fix_0.05"]["joint"]),
    (0.171875 * h2_peak, num["CTL-C_fix_0.171875"]["joint"]),
    (0.5 * h2_peak, num["CTL-C_fix_0.5"]["joint"]),
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 7.6), dpi=200)

# left panel: the shapes at the criterion
ax1.plot(r, win_prof, color="#1a5276", lw=2.0, zorder=3,
         label="winning free shape (K = 9 spline, Phase 405)")
fx_r, fx_v = zip(*fix_marks)
ax1.plot(fx_r, fx_v, "s", color="#b03a2e", ms=7, zorder=4,
         label="fixed shape at the criterion: stored local reads\n"
               "(Phase 404 ladder, mu_S = 0.5)")
ax1.axhline(bar, color="#616a6b", lw=1.1, ls=":", zorder=2)
ax1.annotate(f"SS7 criterion (bar) = {bar:.6f}\n"
             "both peaks AT the criterion, attained at r = 10",
             xy=(10.15, bar), xytext=(10.25, 0.352), fontsize=9.0,
             color="#333333")
ax1.plot([10.0], [bar], "o", color="#1a5276", ms=6, zorder=4)
ax1.axvline(FRAGILE_R, color="#7d6608", lw=1.1, ls=":", zorder=2)
win_at_fragile = float(win_spline(FRAGILE_R))
ax1.annotate(f"fragile site r = {FRAGILE_R:.3f}:\nwinner S = {win_at_fragile:.5f} "
             "(shift ~off);\nthe fixed shape still carries\n"
             f"S = {lad['local_at_nec_argmin']['S']:.4f} at its own NEC site "
             f"r = {lad['nec_argmin_r']:.2f}",
             xy=(FRAGILE_R, abs(BETA * win_at_fragile)),
             xytext=(12.4, 0.20), fontsize=9.0, color="#7d6608",
             arrowprops=dict(arrowstyle="->", color="#7d6608", lw=1.0))
ax1.set_xlim(10, 20)
ax1.set_ylim(-0.012, 0.53)
ax1.set_xlabel("r (band [10, 20], home pose)", fontsize=10.5)
ax1.set_ylabel(r"$|\beta \cdot S|$", fontsize=11)
ax1.set_title("The shapes at the criterion: front-loaded ramp vs fixed shape",
              fontsize=11.5, fontweight="bold")
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=8.6, loc="upper right")

# right panel: joint vs peak
wx, wy = zip(*win_pts)
fx, fy = zip(*fix_pts)
ax2.plot(wx, wy, "o-", color="#1a5276", lw=2.0, ms=6, zorder=3,
         label="free shape (winner), scaled")
ax2.plot(fx, fy, "s--", color="#b03a2e", lw=1.7, ms=6, zorder=3,
         label="fixed shape (H2's S scaled, Phase 404 ladder)")
ax2.axhline(0.0, color="#333333", lw=1.1, zorder=2)
ax2.axvline(bar, color="#616a6b", lw=1.1, ls=":", zorder=2)
ax2.annotate("joint = 0", xy=(0.36, 0.0), xytext=(0.355, 0.14e-6),
             fontsize=9.0, color="#333333")
ax2.annotate(f"at the criterion:\nfree shape joint {win_joint_crit:+.6e}\n"
             f"fixed shape joint {num['CTL-C_fix_0.5']['joint']:+.6e}",
             xy=(bar, win_joint_crit), xytext=(0.085, -7.6e-6), fontsize=9.2,
             color="#1a5276",
             arrowprops=dict(arrowstyle="->", color="#1a5276", lw=1.0))
ax2.set_xlim(-0.015, 0.475)
ax2.set_ylim(-10.6e-6, 2.1e-6)
ax2.set_xlabel(r"peak $|\beta \cdot S|$", fontsize=10.5)
ax2.set_ylabel("joint = min(NEC, DEC) minima (SET-244)", fontsize=10.5)
ax2.set_title("What the shapes cost on Phase 400's static base (Gate-50 reads)",
              fontsize=11.5, fontweight="bold")
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=8.8, loc="lower left")
ax2.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

fig.suptitle("Gate-50: Phase 405's re-introduced set \u2014 the free shape stands AT the SS7 criterion\n"
             "with the band joint positive on Phase 400's static base",
             fontsize=13, fontweight="bold")

confirm = (
    "Winner at the criterion (Gate-50 deciding reads):  "
    f"joint {win_joint_crit:+.6e} (diff \u22121.6e\u221218 vs stored);  exact worst-null "
    f"{win_worst_null:+.6e};  adversary polish {win_polish:+.6e} (SAMPLER-M);\n"
    "Type-I fraction 1.0; 50-digit mpmath confirms.   "
    f"Spends at the criterion: free shape {costs['winner_cost_at_criterion']:.4e} vs "
    f"fixed shape {costs['fixed_cost_at_criterion']:.4e} \u2014 ratio "
    f"{costs['ratio_fixed_over_winner']:.2f}.\n"
    "Both spends ~quadratic in peak on this base (coefficients 8.69e\u221207 vs 5.40e\u221205 "
    "per peak^2); what is nearly flat is the winner's JOINT, its spend staying far below the margin (G50-C)."
)
fig.text(0.5, 0.252, confirm, ha="center", va="top", fontsize=9.0,
         bbox=dict(boxstyle="round,pad=0.45", fc="#eaf2f8", ec="#1a5276", alpha=0.98))

fence = (
    f"SEC = {sec_min:.6e} at the winning point \u2014 FAILING, printed on the face (G50-E / rider G50-R2); SEC is outside the joint.\n"
    "Rider G50-R5: the peak is quoted AT THE CRITERION, never as exceeding it \u2014 attained at the band's inner edge r = 10 by a front-loaded ramp\n"
    "(H2's own reference peak is likewise attained at r = 10, like-for-like), the shape scaled to the criterion target (exact-arithmetic shortfall 6.58e\u221217).\n"
    "FENCE: band [10, 20] read at the home pose (Phase 356 full-extent caveat); no member claimed, no EC pass beyond the NEC/WEC/DEC joint, no drive implication."
)
fig.text(0.5, 0.012, fence, ha="center", va="bottom", fontsize=8.8,
         color="#78281f",
         bbox=dict(boxstyle="round,pad=0.4", fc="#fdedec", ec="#b03a2e"))

fig.tight_layout(rect=[0, 0.285, 1, 0.93])
fig.savefig(OUT)
print("wrote", OUT)
