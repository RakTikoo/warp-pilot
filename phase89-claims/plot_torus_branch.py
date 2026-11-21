"""P8-3 toroidal realisation (Phase 8, Gate-2 claim G2-3): the Gelfand
branch scan and the realised solve.

The fixed-psi-form ansatz can satisfy its surface condition only if
max over centre-shots of beta(15) reaches 0; that maximum is plotted
vs the normalised Gelfand parameter lambda = rho_c * s_t^2 (primary
rho_c path: phase8/results/p83_control_scan.json; refinement rows:
phase8/results/p83_branch_refine.json). The obstruction is real for
lambda >~ 0.65 and is a branch boundary, bracketed to (0.6, 0.7).
At lambda = 1 itself -- the obstructed prescription -- the
gamma-extended system nevertheless REALISES the torus: residual RMS
2.99e-3 -> 1.89e-4 (15.8x, phase8/results/p83_solve_A.json, control
RMS from p83_control_scan.json), grid-independent. All float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "torus_branch.png")

cs = json.load(open(os.path.join(WP, "phase8/results/p83_control_scan.json")))
prim = [(float(r["lam_rho_c_s_t2"]), float(r["max_beta15"]))
        for r in cs["branch_scan_primary_rho_c_path"]]
ref = json.load(open(os.path.join(WP, "phase8/results/p83_branch_refine.json")))
refp = [(float(r["lam_rho_c_s_t2"]), float(r["max_beta15"])) for r in ref["rows"]]
sol = json.load(open(os.path.join(WP, "phase8/results/p83_solve_A.json")))
rms0 = float(cs["control"]["rms"])
rms1 = float(sol["residual_after_rms"])
factor = float(sol["rms_reduction_factor"])
print("primary:", prim)
print("refine:", refp)
print(f"solve: RMS {rms0:.3e} -> {rms1:.3e} ({factor:.1f}x)")
assert abs(dict(prim)[1.0] - (-0.1853)) < 1e-3
assert abs(rms1 - 1.894e-4) < 1e-6 and abs(factor - 15.8) < 0.05

fig, ax = plt.subplots(figsize=(9.5, 5.6))
# obstruction region (max beta15 < 0 side of the bracket) and the bracket band
ax.axvspan(0.70, 1.03, color="#c0392b", alpha=0.07)
ax.axvspan(0.60, 0.70, color="#e67e22", alpha=0.13)
ax.text(0.865, 0.62, "OBSTRUCTED\n(fixed-$\\psi$ ansatz:\nmax $\\beta(15) < 0$)",
        ha="center", fontsize=9, color="#7b241c")
ax.text(0.65, -0.24, "boundary\nbracket\n(0.6, 0.7)", ha="center",
        fontsize=8.5, color="#7e5109")
ax.axhline(0, color="black", lw=1.2)
ax.text(0.115, 0.03, "surface condition reachable", fontsize=9,
        color="#145a32")

allp = sorted(prim + refp)
ax.plot([p[0] for p in allp], [p[1] for p in allp], "-", color="#005f8f",
        lw=1.4, zorder=3)
ax.plot([p[0] for p in prim], [p[1] for p in prim], "o", ms=9,
        color="#005f8f", mec="white", mew=1.2, zorder=4,
        label="primary scan ($\\lambda$ = 1, 1/2, 1/4, 1/10)")
ax.plot([p[0] for p in refp], [p[1] for p in refp], "s", ms=7,
        color="#005f8f", mec="white", mew=1.0, zorder=4,
        label="boundary refinement rows")
for lam, v in prim:
    off = (16, -5) if lam == 0.1 else (0, 10 if v >= 0 else -16)
    ax.annotate(f"{v:+.3f}", (lam, v), textcoords="offset points",
                xytext=off, ha="left" if lam == 0.1 else "center",
                fontsize=10, color="#00334d")

ax.annotate(f"at $\\lambda = 1$ (obstructed for the fixed-$\\psi$ ansatz) the\n"
            f"$\\gamma$-extended system REALISES the torus anyway:\n"
            f"residual RMS {rms0:.2e} $\\rightarrow$ {rms1:.2e} "
            f"({factor:.1f}$\\times$), grid-independent",
            (1.0, dict(prim)[1.0]), textcoords="axes fraction",
            xytext=(0.30, 0.70), fontsize=9.5, color="#00334d",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#005f8f",
                      alpha=0.95),
            arrowprops=dict(arrowstyle="->", color="#005f8f"))

ax.set_xlim(0.03, 1.03); ax.set_ylim(-0.30, 0.85)
ax.set_xlabel("normalised Gelfand parameter $\\lambda = \\rho_c s_t^2$ "
              "(1 = the original prescription)")
ax.set_ylabel("max over centre-shots of $\\beta(15)$")
ax.set_title("P8-3 \u2014 the donut's obstruction is a branch boundary, not a wall\n"
             "and the $\\gamma$-extended solve realises the torus on the "
             "obstructed side of it")
ax.legend(loc="lower left", fontsize=9)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("saved", OUT)
