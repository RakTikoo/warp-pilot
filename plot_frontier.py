"""The mass-velocity frontier of verified positive-energy warp shells.

Points are read from the frozen configurations (compactness = M_geom / R1).
The beta >= 0.1 region is empty: three independent constructions (named
families, free-form machine search, conditions-first inversion) all land
within ~1e-8 of zero worst-margin and none certifies a pass (Phase 1
REPORT.md sec. 1.2). Closest named-family attempt at beta=0.1: worst
margin -2.06e-7. All arithmetic float64.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontier.png")

pts = []
for name, label in [("finalist_A", "Finalist A"),
                    ("finalist_B2", "Finalist B2"),
                    ("frontier_b005", "frontier winner")]:
    cfg = json.load(open(os.path.join(WP, "results/frozen", name + ".json")))
    pts.append((float(cfg["beta"]), float(cfg["M_geom"]) / float(cfg["R1"]), label))
pts.sort()
betas = [p[0] for p in pts]; comps = [p[1] for p in pts]

fig, ax = plt.subplots(figsize=(9.5, 5.6))

# empty region
ax.axvspan(0.1, 0.15, color="#c0392b", alpha=0.08)
ax.axvline(0.1, color="#c0392b", lw=1.0, ls=":")
ax.text(0.125, 0.415,
        "no verified design at $\\beta \\geq 0.1$\n"
        "three independent constructions land within\n"
        "$\\sim 10^{-8}$ of zero worst-margin; none certifies\n"
        "closest named-family attempt ($\\beta=0.1$):\n"
        "worst margin $-2.06\\times10^{-7}$ (fails)",
        ha="center", va="top", fontsize=9, color="#7b241c")

# frontier line through the verified minima + verified points
ax.plot(betas, comps, "--", color="#005f8f", lw=1.4,
        label="minimum verified compactness at each $\\beta$")
ax.plot(betas, comps, "o", ms=8, color="#005f8f", mec="white", mew=1.2, zorder=5)
for b, c, lab in pts:
    ax.annotate(f"{lab}\n$\\beta={b:.2f}$, $M/R_1={c:.3f}$",
                (b, c), textcoords="offset points", xytext=(-6, 12),
                fontsize=9.5, color="#00334d")

ax.set_xlim(0, 0.15); ax.set_ylim(0, 0.5)
ax.set_xlabel("velocity $\\beta = v/c$")
ax.set_ylabel("compactness $M/R_1$ (geometric units)")
ax.set_title("Positive-energy warp shells: the verified frontier\n"
             "(each point passes NEC/WEC/SEC/DEC for all observers, "
             "confirmed by three computation paths)")
ax.legend(loc="upper left", fontsize=9)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("saved", OUT, "; points:", pts)
