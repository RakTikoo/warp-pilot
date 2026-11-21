"""H4 re-solved shells in a Schwarzschild background (Phase 5, gate-verified).

Core DEC margins are the exact 1D spherical margins (beta = 0) read from
phase5/results/h4_resolved_shell.json: the flat control and the
Schwarzschild configs M_bg = 1, 2, 4, where the shell's pressure is
re-solved from conservation in the TOTAL geometry. The contrasting
marker is the Phase 1 X2 superposition method's static-shell worst
margin at M_bg = 1 (-9.9e-5, Phase 1 REPORT.md): superposition fails
where re-solving passes. At M_bg = 4 the re-solved shell fails DEC
only (NEC/WEC/SEC still pass) via tangential-pressure amplification.
All arithmetic float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "h4_margins.png")

d = json.load(open(os.path.join(WP, "phase5/results/h4_resolved_shell.json")))
flat_dec = float(d["controls"]["flat_solve"]["static1d_core"]["dec"])
rows = [(0.0, flat_dec)]
for key in ["schw M=1 beta=0.0", "schw M=2 beta=0.0", "schw M=4 beta=0.0"]:
    cfg = d["configs"][key]
    rows.append((float(key.split()[1].split("=")[1]),
                 float(cfg["solve"]["static1d_core"]["dec"])))
mbg = np.array([r_[0] for r_ in rows])
dec = np.array([r_[1] for r_ in rows]) * 1e5  # plot in units of 1e-5
print("M_bg:", mbg, " core DEC x1e5:", dec)
assert np.allclose(dec, [3.76, 2.77, 1.31, -5.71], atol=0.01)

SUPERPOSITION_M1 = -9.9  # x1e-5, Phase 1 X2 static superposition at M_bg=1

fig, ax = plt.subplots(figsize=(9.5, 5.6))
ax.axhspan(0, 5.2, color="#1e8449", alpha=0.07)
ax.axhspan(-11.5, 0, color="#c0392b", alpha=0.07)
ax.axhline(0, color="black", lw=1.2)
ax.text(3.98, 4.6, "PASS (all energy conditions)", ha="right",
        fontsize=9.5, color="#145a32")
ax.text(3.98, -10.9, "FAIL", ha="right", fontsize=9.5, color="#7b241c")

ax.plot(mbg, dec, "-", color="#005f8f", lw=1.6, zorder=3)
ax.plot(mbg, dec, "o", ms=9, color="#005f8f", mec="white", mew=1.2, zorder=4,
        label="re-solved shell (Phase 5 H4), exact 1D core DEC margin")
for x_, y_ in zip(mbg, dec):
    ax.annotate(f"{y_:+.2f}", (x_, y_), textcoords="offset points",
                xytext=(0, 11), ha="center", fontsize=10.5, color="#00334d")
ax.plot([1.0], [SUPERPOSITION_M1], "X", ms=13, color="#c0392b", mec="white",
        mew=1.0, zorder=4,
        label="superposition (Phase 1 method), static worst margin at $M_{bg}=1$")
ax.annotate("$-9.9$", (1.0, SUPERPOSITION_M1), textcoords="offset points",
            xytext=(14, -4), fontsize=10.5, color="#7b241c")
ax.annotate("at $M_{bg}=4$ only DEC fails\n(NEC/WEC/SEC still pass):\n"
            "tangential-pressure amplification",
            (4.0, dec[-1]), textcoords="offset points", xytext=(-128, 26),
            fontsize=9, color="#00334d")

ax.set_xlim(-0.25, 4.25); ax.set_ylim(-11.5, 5.2)
ax.set_xticks([0, 1, 2, 4])
ax.set_xticklabels(["0\n(flat)", "1", "2", "4"])
ax.set_xlabel("Schwarzschild background mass $M_{bg}$ (geometric units)")
ax.set_ylabel("core DEC margin ($\\times 10^{-5}$, geometric units)")
ax.set_title("H4 — a warp shell re-solved inside a black hole's gravity\n"
             "re-solving reverses the superposition failure at $M_{bg}=1$–2; "
             "the window closes by $M_{bg}=4$")
ax.legend(loc="center left", bbox_to_anchor=(0.015, 0.40), fontsize=9)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("saved", OUT)
