"""P9-1 moving re-solved shell at beta=0.02 in a Schwarzschild background
(Phase 9, Gate-2 claim G2-1).

Cavity and core NEC margins at h=0.1 read from
phase9/results/p91_chain.json ("moving" section): the AREAL embedding
passes every bar at both offsets d=50 and d=100 (cavity at the FD floor,
core +3.2e-5, Type-I fraction 1.000); the PAINLEVIE-GULLSTRAND (PG)
embedding fails at d=50 (cavity -1.25e-4, core NEC -3.4e-6). The claim
is embedding-dependent and both embeddings are named -- the pass is a
property of the areal spacetime construction, not of the PG one.
Reference line: the Phase 5 H4 cavity failure class, -1.95e-4
(concentric moving cavity at M_bg=1, CHECKPOINT5 H4 record).
All arithmetic float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "moving_shell.png")

d = json.load(open(os.path.join(WP, "phase9/results/p91_chain.json")))
mv = d["moving"]

def nec(emb, dist, region):
    return float(mv[f"d={dist}"][emb]["h=0.1"][region]["nec"])

areal = {("cavity", 50): nec("areal", 50, "cavity"),
         ("cavity", 100): nec("areal", 100, "cavity"),
         ("core", 50): nec("areal", 50, "core"),
         ("core", 100): nec("areal", 100, "core")}
pg50 = {("cavity", 50): nec("pg_consistent", 50, "cavity"),
        ("core", 50): nec("pg_consistent", 50, "core")}
print("areal:", areal)
print("PG d=50:", pg50)
# gate-verified values (CHECKPOINT9 P9-1)
assert abs(areal[("core", 50)] - 3.162e-5) < 1e-7
assert abs(areal[("core", 100)] - 3.271e-5) < 1e-7
assert abs(areal[("cavity", 50)] - (-2.745e-8)) < 1e-9
assert abs(pg50[("core", 50)] - (-3.36e-6)) < 1e-7
assert abs(pg50[("cavity", 50)] - (-1.250e-4)) < 1e-6

H4_CAVITY_CLASS = -19.5  # x1e-5, Phase 5 H4 concentric moving cavity NEC

groups = [("cavity", 50), ("cavity", 100), ("core", 50), ("core", 100)]
labels = ["cavity\nd = 50", "cavity\nd = 100", "core (wall)\nd = 50", "core (wall)\nd = 100"]
x = np.arange(len(groups), dtype=np.float64)
w = 0.38

fig, ax = plt.subplots(figsize=(9.5, 5.6))
ax.axhspan(0, 6.5, color="#1e8449", alpha=0.07)
ax.axhspan(-22, 0, color="#c0392b", alpha=0.07)
ax.axhline(0, color="black", lw=1.2)
ax.text(3.55, 5.9, "PASS", ha="right", fontsize=9.5, color="#145a32")
ax.text(3.55, -21.4, "FAIL", ha="right", fontsize=9.5, color="#7b241c")

av = np.array([areal[g] for g in groups]) * 1e5
ax.bar(x - w / 2, av, w, color="#005f8f", zorder=3,
       label="areal embedding (re-solved shell, $\\beta=0.02$)")
for xi, v, g in zip(x - w / 2, av, groups):
    lab = f"{areal[g]:+.2e}" if g[0] == "cavity" else f"{v:+.2f}"
    ax.annotate(lab, (xi, v), textcoords="offset points",
                xytext=(0, 6 if v >= 0 else -14), ha="center",
                fontsize=9, color="#00334d")

pv = [pg50.get(g) for g in groups]
px = [xi + w / 2 for xi, g in zip(x, groups) if g in pg50]
pvv = np.array([pg50[g] for g in groups if g in pg50]) * 1e5
ax.bar(px, pvv, w, color="#c0392b", zorder=3,
       label="Painlev\u00e9\u2013Gullstrand embedding, d = 50 only (fails)")
for xi, v, g in zip(px, pvv, [g for g in groups if g in pg50]):
    ax.annotate(f"{pg50[g]:+.2e}", (xi, v), textcoords="offset points",
                xytext=(0, -14), ha="center", fontsize=9, color="#7b241c")

ax.axhline(H4_CAVITY_CLASS, color="#7d3c98", lw=1.4, ls="--", zorder=4,
           label="Phase 5 H4 cavity failure class: $-1.95\\times10^{-4}$")
ax.annotate("the failure this result had to beat", (0.02, H4_CAVITY_CLASS),
            textcoords="offset points", xytext=(2, 5), fontsize=9,
            color="#4a235a")

ax.set_xlim(-0.6, 3.6); ax.set_ylim(-22, 6.5)
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.5)
ax.set_ylabel("worst NEC margin ($\\times 10^{-5}$, geometric units)")
ax.set_title("P9-1 \u2014 a warp shell MOVING at $\\beta=0.02$ past a black hole\n"
             "areal embedding: passes at both offsets (cavity at the numerical floor, "
             "core $+3.2\\times10^{-5}$);\nPainlev\u00e9\u2013Gullstrand embedding: fails at "
             "d = 50 \u2014 the verdict is embedding-dependent")
ax.legend(loc="upper left", bbox_to_anchor=(0.015, 0.99), fontsize=9)
ax.grid(alpha=0.25, axis="y")
fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("saved", OUT)
