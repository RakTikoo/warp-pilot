"""P15 SA-2 environmental-coupling screening (Phase 15, Gate-4
claim G4-2, gate-restated form): the screen function S across the
wall at beta=1.1. S values are read at render time from
phase15/results/p152_bases_beta1.1.npz (stored Q/S fields on the
binding and volume point sets); radii come from the bed definition
in phase15/p152_lib.py (the same definitions the Gate-4 second
path imported). Exterior closure (S = 0.0 EXACTLY at all three
beta) and the 100%-open binding fraction are asserted against
phase15/results/p152_gate.json; the screened partial coverage is
asserted against phase15/results/p152_scan.json. The claim is the
construction + design laws ONLY: the screened-aether family is
CLOSED as a superluminal supply route (Gate-4 scope, stated on
the figure). All float64.
"""
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "screening.png")

sys.path.insert(0, os.path.join(WP, "phase15"))
import p152_lib as L  # bed definition (point sets + radii)

bed = L.bed(1.1)
r_b = np.asarray(bed["r_b"], dtype=np.float64)
r_v = np.asarray(bed["r_v"], dtype=np.float64)

z = np.load(os.path.join(WP, "phase15/results/p152_bases_beta1.1.npz"))
S_b = np.asarray(z["S_b"], dtype=np.float64)
S_v = np.asarray(z["S_v"], dtype=np.float64)
Q_b = np.asarray(z["Q_b"], dtype=np.float64)

g = json.load(open(os.path.join(WP, "phase15/results/p152_gate.json")))
sc = json.load(open(os.path.join(WP, "phase15/results/p152_scan.json")))
q_crit = float(sc["Q_crit"])
row11 = next(r for b in sc["betas"] if float(b["beta"]) == 1.1
             for r in b["rows"] if r["c0"] == [0.2, 1.0, 1.0])
partial11 = float(row11["bands"]["all"]["frac_partial"])
full11 = float(row11["bands"]["all"]["frac_full"])

print("points: binding", len(r_b), " volume", len(r_v))
print("S_b min:", S_b.min(), " S_v min:", S_v.min(),
      " Q_b min:", Q_b.min(), " Q_crit:", q_crit)
print("screened partial (beta=1.1):", partial11, " full:", full11)
assert len(r_b) == len(S_b) == 504 and len(r_v) == len(S_v) == 1270
assert S_b.min() > 0.9999 and np.mean(S_b >= 0.5) == 1.0
assert S_v.min() == 0.0
assert abs(Q_b.min() - 9.557658281956962e-05) < 1e-12
assert abs(q_crit - 2.3861204484797755e-08) < 1e-14
for bv in ("0.1", "1.1", "1.5"):
    assert float(g["exterior"][bv]["S_ext_max"]) == 0.0
    assert float(g["open_fraction"][bv]["binding_S_ge_0p5"]) == 1.0
assert abs(partial11 - 0.8988095238095238) < 1e-12
assert abs(full11 - 0.2916666666666667) < 1e-12

fig, ax = plt.subplots(figsize=(9.5, 5.6))

ax.axvspan(10.0, 20.0, color="#005f8f", alpha=0.05, zorder=0)
ax.text(15.0, 1.045, "wall band (R1 = 10, R2 = 20)", ha="center",
        fontsize=9.5, color="#00334d")

ax.scatter(r_v, S_v, s=7, color="#95a5a6", alpha=0.55, zorder=2,
           label="volume points (1270)")
ax.scatter(r_b, S_b, s=16, color="#005f8f", zorder=4,
           label="binding points (504) \u2014 all S $\\geq$ 0.99994")

ax.axhline(0.5, color="#1e8449", lw=1.4, ls="--", zorder=3)
ax.text(20.9, 0.53, "screen-open threshold S = 0.5", ha="right",
        fontsize=9, color="#145a32")

ax.annotate("EXTERIOR: S = 0.0 EXACTLY at $\\beta$ = 0.1, 1.1, 1.5\n"
            "(Q$_{ext,max}$ = Q$_{crit}$/30, so the couplings are off:\n"
            "$\\alpha_1^{eff}$ = $\\alpha_2^{eff}$ = 0, c$_T$ = 1 \u2014 "
            "the solar-system /\nGW exclusion is evaded by construction)",
            (9.05, 0.30), fontsize=9.5, color="#145a32",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#1e8449",
                      alpha=0.92))

ax.annotate("SCREENING COSTS ZERO COVERAGE: at $\\beta$ = 1.1 the "
            "screened\nassembly's partial coverage 0.899 reproduces the "
            "UNSCREENED\ntilted constant-coupling value (0.899) \u2014 "
            "identical to three\ndigits (bit-identical in the gate's "
            "independent second path)",
            (11.2, 0.60), fontsize=9.5, color="#00334d",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#005f8f",
                      alpha=0.92))

ax.annotate("CLOSURE (on the face of the claim): the screened aether is "
            "CLOSED as a\nsuperluminal supply route \u2014 this figure "
            "documents the construction, not a drive.\n(full coverage "
            f"{full11:.2f} at $\\beta$ = 1.1 vs the 0.90 bar \u2014 a "
            "property of the aether supply,\nscreening-independent.)",
            (0.985, 0.035), xycoords="axes fraction", ha="right",
            va="bottom", fontsize=9, color="#7b241c",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#c0392b",
                      alpha=0.92))

ax.set_xlim(8.8, 21.2); ax.set_ylim(-0.06, 1.10)
ax.set_xlabel("radius r across the wall")
ax.set_ylabel("screen function S($\\chi$) \u2014 couplings "
              "c$_i$ = c$_i^0$ \u00b7 S")
ax.set_title("P15 SA-2 \u2014 Environmental-coupling screening at "
             "$\\beta$ = 1.1: off exactly outside,\nopen at 100% of "
             "binding points inside")
ax.legend(loc="upper left", fontsize=9)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(OUT, dpi=200)
print("saved", OUT)
