#!/usr/bin/env python3
"""Figure generator for the Gate-52 claims bundle (release v1.43.0).

Reads ONLY the bundled records in ../sources/ (Phase 412's fit record
and Gate-52's arithmetic record) and writes ../figures/g52_ladder.png.
No data is invented: every plotted point, the fit line, the local
exponents and the million-c gap figures are read from those records.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources")
OUT = os.path.join(HERE, "..", "figures", "g52_ladder.png")

fit = json.load(open(os.path.join(SRC, "p412_fit.json")))
arith = json.load(open(os.path.join(SRC, "g52_arith.json")))

rows = fit["rows"]  # criterion, m=2 (K9), m=5 (K17)
peaks = np.array([r["peak"] for r in rows])
joints = np.array([r["joint"] for r in rows])
spends = np.array([r["spend"] for r in rows])
legal = [r["legal"] for r in rows]
M0 = fit["M0"]
A = arith["refit"]["A"]
p = arith["refit"]["p"]
crossing = arith["refit"]["implied_zero_crossing_peak"]
exp_lo = arith["local_exponents"]["crit_to_2x"]
exp_hi = arith["local_exponents"]["2x_to_5x"]
gap_fit = arith["million_c_gap"]["fit_law"]["orders_short"]
gap_loc = arith["million_c_gap"]["local_exponent_law"]["orders_short"]
gap_naive = arith["million_c_gap"]["gate50_naive_law"]["orders_short"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.5, 6.4))

# ---- Panel 1: the ladder — joint vs peak -------------------------------
ax1.set_yscale("symlog", linthresh=1e-7)
ax1.axhline(0.0, color="black", lw=1.0)
ax1.plot(peaks[:2], joints[:2], color="#1a7f37", lw=1.2, ls="--", zorder=3)
ax1.annotate("", xy=(peaks[2], joints[2]), xytext=(peaks[1], joints[1]),
             arrowprops=dict(arrowstyle="->", color="#b62324", lw=1.2, ls="--"))
for x, y, ok in zip(peaks, joints, legal):
    ax1.plot([x], [y], marker="o", ms=10,
             color="#1a7f37" if ok else "#b62324",
             markerfacecolor="#1a7f37" if ok else "#b62324", zorder=5)
ax1.annotate(f"criterion (1x, control)\njoint {joints[0]:+.4e}",
             (peaks[0], joints[0]), textcoords="offset points",
             xytext=(10, -6), fontsize=9)
ax1.annotate(f"2x  (P*)\njoint {joints[1]:+.4e}",
             (peaks[1], joints[1]), textcoords="offset points",
             xytext=(10, 2), fontsize=9)
ax1.annotate(f"5x\njoint {joints[2]:+.4e}",
             (peaks[2], joints[2]), textcoords="offset points",
             xytext=(-118, 14), fontsize=9)
ax1.set_xscale("log")
ax1.set_xlim(peaks[0] * 0.75, peaks[2] * 1.35)
ax1.set_xlabel("peak |beta*S|  (band [10, 20], SET-244, Phase 400's base)")
ax1.set_ylabel("joint = min(NEC, WEC, DEC) margin")
ax1.set_title("The speed ladder: legal at the criterion and at 2x,\n"
              "best-found illegal at 5x — the ceiling is bracketed\n(G52-A / G52-B)",
              pad=10)
ax1.grid(True, which="both", alpha=0.25)
ax1.text(0.03, 0.05,
         "5x point: best-found within the registered boxes only\n"
         "(search-scoped, rider G52-R2) — not a non-existence proof.",
         transform=ax1.transAxes, fontsize=8.5,
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.6", alpha=0.9))

# ---- Panel 2: the spend curve ------------------------------------------
xs = np.logspace(np.log10(peaks[0] * 0.8), np.log10(peaks[2] * 1.6), 200)
ax2.loglog(xs, A * xs**p, color="0.35", lw=1.4,
           label=f"3-point fit: spend = {A:.3e} * peak^{p:.3f}")
ax2.loglog(peaks, spends, marker="o", ms=10, color="#1f6feb",
           markerfacecolor="#1f6feb", ls="none", zorder=5,
           label="measured spends (recomputed at diff 0.0, G52-C)")
for x, y in zip(peaks, spends):
    ax2.annotate(f"{y:.3e}", (x, y), textcoords="offset points",
                 xytext=(8, 6), fontsize=9)
ax2.axhline(M0, color="#b62324", lw=1.2, ls=":")
ax2.annotate(f"static margin M0 = {M0:.3e}", (peaks[2] * 0.62, M0 * 1.6),
             fontsize=9, color="#b62324")
ax2.axvline(crossing, color="0.35", lw=1.0, ls="--")
ax2.annotate(f"fit-implied crossing {crossing:.3f} — below the\n"
             f"measured-legal 2x rung {peaks[1]:.3f}:\nthe fit fails on its face (G52-C)",
             (crossing, spends[2] * 0.9), fontsize=8.5,
             xytext=(10, 0), textcoords="offset points")
ax2.annotate(f"local exponent {exp_lo:.3f}\n(quadratic law holds)",
             (peaks[0] * 0.86, spends[0] * 2.6), fontsize=9)
ax2.annotate(f"local exponent {exp_hi:.3f}\n(law fails beyond 2x)",
             (peaks[1] * 1.25, spends[1] * 5.0), fontsize=9)
ax2.set_xlabel("peak |beta*S|")
ax2.set_ylabel("margin spend (M0 - joint)")
ax2.set_title("The cost law: quadratic to 2x, steepening beyond;\n"
              "no single power law describes the ladder (G52-C)", pad=10)
ax2.grid(True, which="both", alpha=0.25)
ax2.legend(fontsize=8.5, loc="lower right")

fig.suptitle("Phase 412's speed ladder as re-judged by Gate-52 — band [10, 20] only;\n"
             "SEC at the P* candidate = -2.917201e-04 (fails, outside the joint): no member, no EC pass.\n"
             "P* peak per rider G52-R1: \"at 2x the criterion — H2's own peak, by the SS7 definition —\n"
             "the shape scaled to the rung target.\" Million-c gap is fit-based only (G52-D / G52-R3):\n"
             f"{gap_fit:.2f} orders short under the fit, {gap_loc:.2f} under the steeper local exponent\n"
             f"(naive quadratic {gap_naive:.2f}, understates). In the A2 scaling lineage of this programme (G52-R4).",
             fontsize=10.5)
fig.tight_layout(rect=(0, 0, 1, 0.86))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, dpi=200)
print("wrote", OUT)
