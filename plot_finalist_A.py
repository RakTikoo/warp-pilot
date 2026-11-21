"""Plot Finalist A (the verified warp shell) from its frozen configuration.

Uses the pilot's own shell.py so the figure shows the exact audited object:
edge-peaked density, cosine shift, R1=10, R2=20, M=2.0 geom, beta=0.02.
All arithmetic float64 (shell.py DTYPE).
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

import shell

CFG = json.load(open("results/frozen/finalist_A.json"))
prof = shell.build_shell(CFG["R1"], CFG["R2"], CFG["M_geom"], kind=CFG["kind"],
                         params=CFG["params"], s_rho=CFG["s_rho"], s_P=CFG["s_P"])
r = prof["r"]; rho = prof["rho_ex"]
S = shell.shift_S(r, CFG["R1"], CFG["R2"], kind=CFG["shift_kind"], ws=CFG["ws"])
beta = CFG["beta"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))

# --- left: cross-section through the centre, coloured by density ------------
N = 600
xs = np.linspace(-24, 24, N)
X, Y = np.meshgrid(xs, xs)
R = np.sqrt(X**2 + Y**2)
RHO2 = np.interp(R, r, rho, left=0.0, right=0.0)
cmap = plt.get_cmap("inferno").copy()
cmap.set_under("white")
ax1.set_facecolor("white")
ax1.pcolormesh(X, Y, RHO2, cmap=cmap, shading="auto",
               vmin=0.03 * float(rho.max()), vmax=float(rho.max()))
ax1.add_patch(Circle((0, 0), CFG["R1"], fill=False, ls="--", lw=1.0, color="0.35"))
ax1.add_patch(Circle((0, 0), CFG["R2"], fill=False, ls="--", lw=1.0, color="0.35"))
ax1.annotate("", xy=(17, -16.5), xytext=(7, -16.5),
             arrowprops=dict(arrowstyle="->", color="black", lw=1.6))
ax1.text(12, -13.6, "motion\n$\\beta = 0.02$", ha="center", fontsize=9)
ax1.text(0, 0, "empty\ncavity", ha="center", va="center", fontsize=9, color="black")
ax1.set_xlim(-24, 24); ax1.set_ylim(-24, 24); ax1.set_aspect("equal")
ax1.set_xlabel("x (geometric units)"); ax1.set_ylabel("y")
ax1.set_title("Cross-section: matter density $\\rho(r)$")

# --- right: radial profiles ---------------------------------------------------
ax2.plot(r, rho, color="#b34700", lw=1.8, label="density $\\rho(r)$ (exact)")
ax2.axvspan(CFG["R1"], CFG["R2"], color="grey", alpha=0.12)
ax2.set_xlim(0, 30); ax2.set_xlabel("r (geometric units)")
ax2.set_ylabel("density $\\rho$ (geometric units)", color="#b34700")
ax2.tick_params(axis="y", labelcolor="#b34700")
ax2b = ax2.twinx()
ax2b.plot(r, beta * S, color="#005f8f", lw=1.8, label="shift $\\beta\\,S(r)$")
ax2b.set_ylabel("shift (velocity) profile", color="#005f8f")
ax2b.tick_params(axis="y", labelcolor="#005f8f")
ax2b.set_ylim(0, 0.03)
ax2.set_title("Profiles: density peaks at the wall edges;\nshift lives inside the wall")
h1, l1 = ax2.get_legend_handles_labels(); h2, l2 = ax2b.get_legend_handles_labels()
ax2.legend(h1 + h2, l1 + l2, loc="upper right", fontsize=8.5)

fig.suptitle("Finalist A — verified positive-energy warp shell "
             "($M = 2.69\\times10^{27}$ kg, $\\beta = 0.02$)", fontsize=12)
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig("finalist_A_shape.png", dpi=200)
print("saved finalist_A_shape.png; rho max", float(rho.max()), "at r =", float(r[int(np.argmax(rho))]))
