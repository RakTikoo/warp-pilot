#!/usr/bin/env python3
"""Figure generator for the Gate-51 claims bundle (release v1.41.0).

Reads ONLY the bundled records in ../sources/ (Gate-51's deciding
records and Phase 392's memo values, as bundled) and writes
../figures/g51_dose_response.png: the graded-category dose-response
0.1363 -> 0.18671875 -> 0.18984375 -> 0.191796875 -> 0.192578125,
RW-5's margin anatomy at the new best, the failure bracket above it,
and the category fence plus the G51-D rider on the figure's face.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources")
OUT = os.path.join(HERE, "..", "figures", "g51_dose_response.png")

# --- deciding values from the bundled gate records -------------------
aud = json.load(open(os.path.join(SRC, "g51_audits_RW-5.json")))
rec = json.load(open(os.path.join(SRC, "g51_records.json")))

beta_best = 0.192578125
beta_fail = 0.195078125
sec_best = aud["audits"][str(beta_best)]["by_h"]["h0.0375"]["summary"]["all_sig"]["sec"]
sec_best_r = aud["audits"][str(beta_best)]["by_h"]["h0.0375"]["summary"]["all_sig"]["sec_r"]
sec_fail = aud["audits"][str(beta_fail)]["by_h"]["h0.0375"]["summary"]["all_sig"]["sec"]
sec_fail_r = aud["audits"][str(beta_fail)]["by_h"]["h0.0375"]["summary"]["all_sig"]["sec_r"]
typeI_fail = aud["audits"][str(beta_fail)]["by_h"]["h0.0375"]["summary"]["all_sig"]["typeI_frac"]
min_edge = rec["rw5_interiority"]["min_edge_distance"]
min_edge_coord = rec["rw5_interiority"]["min_edge_coord"]

# --- dose-response stages (sources/p392_memo.md, "Dose-response in
# the graded category"; gate-verified endpoints per GATE51.md SS7) ---
stages = [
    (0.1363, "step member\nc = 0 (Procaccia)"),
    (0.18671875, "8-mode grading\nPhase 386 - Gate-42"),
    (0.18984375, "E1 widened box\nPhase 391"),
    (0.191796875, "E2 12-mode basis\nPhase 391 - Gate-44"),
    (0.192578125, "E3 / R-W widened box\nPhase 392 - Gate-51"),
]
xs = list(range(len(stages)))
ys = [s[0] for s in stages]
incs = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]

fig, ax = plt.subplots(figsize=(11.5, 6.8), dpi=200)
ax.plot(xs, ys, "o-", color="#1a5276", lw=2.0, ms=7, zorder=3)
ax.axhline(beta_fail, color="#b03a2e", ls="--", lw=1.4, zorder=2)
ax.annotate(
    f"failure bracket beta = {beta_fail}: SEC {sec_fail:+.3e} @ r = {sec_fail_r:g}, "
    f"Type-I {typeI_fail:.5f} (compound failure)",
    xy=(0.02, beta_fail), xytext=(0.05, beta_fail + 0.0016),
    color="#b03a2e", fontsize=9.5)

for i, (y, lab) in enumerate(stages):
    ax.annotate(f"{y:.9g}", (xs[i], y), textcoords="offset points",
                xytext=(0, 10), ha="center", fontsize=10.5,
                fontweight="bold", color="#1a5276")
    ax.annotate(lab, (xs[i], y), textcoords="offset points",
                xytext=(0, -34), ha="center", fontsize=8.6, color="#333333")
for i, d in enumerate(incs):
    ax.annotate(f"+{d:.4f}", ((xs[i] + xs[i + 1]) / 2, (ys[i] + ys[i + 1]) / 2),
                textcoords="offset points", xytext=(0, 7), ha="center",
                fontsize=8.6, color="#616a6b")

ax.set_xlim(-0.35, 4.35)
ax.set_ylim(0.128, 0.1995)
ax.set_xticks([])
ax.set_ylabel(r"best verified speed $\beta$ (graded category)", fontsize=11)
ax.set_title("Graded-category dose-response - Gate-51: Phase 392's raised set\n"
             r"graded-class best now $\beta$ = 0.192578125 (RW-5, gate-verified)",
             fontsize=12.5, fontweight="bold")
ax.grid(True, axis="y", alpha=0.3)

anatomy = (
    "RW-5 margin anatomy at beta = 0.192578125 (Gate-51 deciding reads):\n"
    f"worst SEC {sec_best:+.3e} @ r = {sec_best_r:g} - 106.5x the FD floor; Type-I 1.000 at both spacings;\n"
    "audit4 second path +6.050012e-07 agreeing; shell sampled-NEC positive (diagnostic).\n"
    f"Interior optimum: all 26 coordinates strictly inside the widened R-W box "
    f"(nearest edge {min_edge_coord}, {min_edge:.4f} away) -\n"
    "the widening lever is exhausted at this optimum (G51-C)."
)
ax.text(0.335, 0.30, anatomy, transform=ax.transAxes, fontsize=9.2,
        va="top", ha="left",
        bbox=dict(boxstyle="round,pad=0.45", fc="#eaf2f8", ec="#1a5276", alpha=0.95))

fence = (
    "FENCE: graded category only - this best does NOT contest Procaccia's beta = 0.1363 in the step-profile category;\n"
    "the programme's verified best there remains beta = 0.10 (Gate-7); the beta = 0.12 conversion there (Kaggle p1423) remains owed.\n"
    "Rider G51-D: Arm R-16's no-yield is a truncated-run statement only (budget-stopped at gen 106, population mean still rising) - never a basis verdict."
)
fig.text(0.5, 0.012, fence, ha="center", va="bottom", fontsize=8.8,
         color="#78281f",
         bbox=dict(boxstyle="round,pad=0.4", fc="#fdedec", ec="#b03a2e"))

fig.tight_layout(rect=[0, 0.075, 1, 1])
fig.savefig(OUT)
print("wrote", OUT)
