"""H6 wormhole exoticity floor identities (Phase 5, gate-verified).

For zero-tidal (Phi=0) Morris-Thorne wormholes the volume integral of
rho + p_r decomposes exactly:
  coordinate measure: I_V = -r0/2 - (1/2) int (b/r) dr   <=  -r0/2
  proper measure:     I_V = -r0   + int (sqrt(1-b/r)-1) dr <= -r0
so |I_V| can never fall below r0/2 (coordinate) or r0 (proper): the
exoticity can be concentrated but never reduced below the floor.
Values per audited profile are read from phase5/results/
h6_floor_identity.json (identity values = exact closed form; w1 values
= the Phase 2 volume integrator, an independent numerical path).
All arithmetic float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "h6_floor.png")

d = json.load(open(os.path.join(WP, "phase5/results/h6_floor_identity.json")))
r0 = float(d["r0"])
rows = d["rows"]
names = [row["profile"] for row in rows]
coord_id = np.array([abs(float(row["IV_coord_identity"])) for row in rows])
coord_w1 = np.array([abs(float(row["IV_coord_w1"])) for row in rows])
prop_id = np.array([abs(float(row["IV_proper_identity"])) for row in rows])
prop_w1 = np.array([abs(float(row["IV_proper_w1"])) for row in rows])
assert all(bool(row["coord_floor_ok"]) and bool(row["proper_floor_ok"]) for row in rows)

x = np.arange(len(rows))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), sharex=True)

for ax, ident, w1, floor, title in [
        (ax1, coord_id, coord_w1, r0 / 2.0,
         "coordinate measure: floor $|I_V| \\geq r_0/2$"),
        (ax2, prop_id, prop_w1, r0,
         "proper measure: floor $|I_V| \\geq r_0$")]:
    ax.axhline(floor, color="#c0392b", lw=1.6, ls="--",
               label=f"floor = {floor:.1f} ($r_0 = 1$)")
    ax.axhspan(0, floor, color="#c0392b", alpha=0.07)
    ax.plot(x, ident, "o", ms=8, color="#005f8f", mec="white", mew=1.2,
            label="$I_V$ from the exact identity", zorder=5)
    ax.plot(x, w1, "s", ms=6, mfc="none", color="#b34700", mew=1.4,
            label="$I_V$ from the Phase 2 integrator", zorder=5)
    ax.set_title(title)
    ax.set_ylabel("$|I_V|$ (geometric units)")
    ax.set_ylim(0, max(ident.max(), w1.max()) * 1.18)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", fontsize=8.5)
ax1.text(0.02, 0.06, "forbidden:\nbelow the floor", transform=ax1.transAxes,
         fontsize=8.5, color="#7b241c")

for ax in (ax1, ax2):
    ax.set_xticks(x)
    ax.set_xticklabels([n.replace("_", "\n") for n in names], fontsize=8.5)
ax1.set_xlabel("audited shape function $b(r)$ profile")
ax2.set_xlabel("audited shape function $b(r)$ profile")

fig.suptitle("H6 — wormhole exoticity floors: every audited profile sits at or above its floor\n"
             "(exoticity can be concentrated, never reduced below $r_0/2$ per side "
             "in coordinate measure, $r_0$ in proper measure)", fontsize=11)
fig.tight_layout(rect=[0, 0, 1, 0.90])
fig.savefig(OUT, dpi=200)
print("saved", OUT)
print("coord |I_V| identity:", coord_id, "floor", r0 / 2.0)
print("proper |I_V| identity:", prop_id, "floor", r0)
