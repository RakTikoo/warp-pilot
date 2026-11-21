"""P9-3 Einstein-aether on warp walls (Phase 9, Gate-2 claim G2-2):
the speed asymmetry plus the data exclusion.

Per beta, the plotted pair is (frac_partial, frac_full) of the best
health-passing row by partial coverage, read at render time from
phase9/results/p93_scan.json (109 rows per beta, 327 total; ratio-free
cross-checks asserted in the scan). Subluminally the supply is starved
(best partial exactly 0.000); superluminally it is fed (partial 0.813 /
0.791) but full coverage (0.218 / 0.449) never reaches the 0.90
alignment bar -- no alignment, no candidate. And 0 of 327 rows pass
the solar-system PPN data gates (alpha1/alpha2): the claim is the
asymmetry AND the exclusion together, not a drive. All float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "aether_asymmetry.png")

s = json.load(open(os.path.join(WP, "phase9/results/p93_scan.json")))
betas, partial, full = [], [], []
n_rows = 0
n_data_pass = 0
for b in s["betas"]:
    hp = [r for r in b["rows"] if r["health"]["health_pass"]]
    best = max(hp, key=lambda r: r["frac_partial"])
    betas.append(float(b["beta"]))
    partial.append(float(best["frac_partial"]))
    full.append(float(best["frac_full"]))
    n_rows += len(b["rows"])
    n_data_pass += sum(1 for r in b["rows"] if r["health"]["data_pass"])
print("betas:", betas, "partial:", partial, "full:", full)
print("rows:", n_rows, "data_pass:", n_data_pass)
assert betas == [0.1, 1.1, 1.5]
assert abs(partial[0]) == 0.0 and abs(partial[1] - 0.813) < 0.001
assert abs(partial[2] - 0.791) < 0.001
assert abs(full[1] - 0.218) < 0.001 and abs(full[2] - 0.449) < 0.001
assert n_rows == 327 and n_data_pass == 0

x = np.arange(len(betas), dtype=np.float64)
w = 0.36
fig, ax = plt.subplots(figsize=(9.5, 5.6))

ax.axvspan(0.5, 2.5, color="#7d3c98", alpha=0.05)
ax.text(1.5, 0.965, "superluminal ($\\beta > 1$): supply fed", ha="center",
        fontsize=9.5, color="#4a235a")
ax.text(0.0, 0.965, "subluminal: supply starved", ha="center",
        fontsize=9.5, color="#00334d")

bp = ax.bar(x - w / 2, partial, w, color="#005f8f", zorder=3,
            label="partial coverage (best health-passing row)")
bf = ax.bar(x + w / 2, full, w, color="#e67e22", zorder=3,
            label="full coverage (same row)")
for xi, v in zip(x - w / 2, partial):
    ax.annotate(f"{v:.3f}", (xi, v), textcoords="offset points",
                xytext=(0, 5), ha="center", fontsize=10.5, color="#00334d")
for xi, v in zip(x + w / 2, full):
    ax.annotate(f"{v:.3f}", (xi, v), textcoords="offset points",
                xytext=(0, 5), ha="center", fontsize=10.5, color="#7e5109")

ax.axhline(0.50, color="#1e8449", lw=1.4, ls="--", zorder=4)
ax.text(2.48, 0.515, "0.50 partial bar", ha="right", fontsize=9,
        color="#145a32")
ax.axhline(0.90, color="#c0392b", lw=1.4, ls="--", zorder=4)
ax.text(2.48, 0.915, "0.90 alignment bar (full) \u2014 never reached",
        ha="right", fontsize=9, color="#7b241c")

ax.annotate("DATA EXCLUSION: 0 of 327 scanned rows pass the solar-system\n"
            "PPN gates ($\\alpha_1$/$\\alpha_2$) \u2014 the claim is the asymmetry "
            "+ the exclusion\ntogether, not a drive",
            (0.02, 0.62), fontsize=9.5, color="#4a235a",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#7d3c98",
                      alpha=0.9))

ax.set_xlim(-0.55, 2.55); ax.set_ylim(0, 1.02)
ax.set_xticks(x)
ax.set_xticklabels([f"$\\beta = {b}$" for b in betas], fontsize=10.5)
ax.set_ylabel("coverage of the wall's binding points")
ax.set_title("P9-3 \u2014 Einstein-aether on a warp wall: starved below light speed,\n"
             "fed above it, excluded by solar-system data at every speed")
ax.legend(loc="upper left", bbox_to_anchor=(0.005, 0.86), fontsize=9)
ax.grid(alpha=0.25, axis="y")
fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("saved", OUT)
