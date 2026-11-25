#!/usr/bin/env python3
"""Figure: the GJW mouth-coupling carrier K_pair (Phases 327 / 328 / 331).

Three panels: (A) the sech^2 separation profile -- the curve is the stored
closed form from Phase 327's results file, evaluated from the stored string;
the markers are the stored table values (Phases 327/328). (B) the (1 - 4 xi)
sign chart of the s-wave sector (Phase 328 stored table + stored xi=0 scale).
(C) the quantum-inequality price line of the port (Phase 331 stored table +
stored excursion formula).

Sources:
  phase327/work/p327_results.json
  phase328/work/p328_results_b.json
  phase331/results/p331_results.json
Output: fig_kpair.png
"""
import json
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
p327 = json.load(open(f"{ROOT}/phase327/work/p327_results.json"))
p328 = json.load(open(f"{ROOT}/phase328/work/p328_results_b.json"))
p331 = json.load(open(f"{ROOT}/phase331/results/p331_results.json"))

BETA = 2 * np.pi

def eval_stored(expr, **vars_):
    """Evaluate a stored closed-form string (own stored results only)."""
    ns = {"pi": np.pi, "sech": lambda x: 1.0 / np.cosh(x), **vars_}
    return eval(expr, {"__builtins__": {}}, ns)  # stored programme string

fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(15.5, 4.6))
fig.patch.set_facecolor("white")

# ---- Panel A: separation profile ----
s = np.linspace(0, 4.5, 300)
k_formula = p327["computation_B"]["K_pair(s,beta)"]
k_curve = eval_stored(k_formula, s=s, beta=BETA)
axA.plot(s, k_curve, color="#1a5276", lw=1.8,
         label="stored closed form: $(\\pi/\\beta^2)\\,\\mathrm{sech}^2(\\pi s/\\beta)$")
tab = p327["computation_B"]["K_pair(beta=2pi)"]      # keys "s=0".."s=4"
ss = np.array([float(k.split("=")[1]) for k in tab])
axA.plot(ss, list(tab.values()), "o", color="#1a5276", ms=6,
         label="Phase 327 stored table (tier-1 / 1+1)")
tab2 = p328["table_K2_xi1/6_by_s"]
s2 = np.array([float(k) for k in tab2])
axA2 = axA.twinx()
axA2.plot(s2, list(tab2.values()), "s", color="#c0392b", ms=6,
          label="Phase 328 s-wave, ξ = 1/6 (right axis)")
axA.set_xlabel("mouth separation s (β = 2π registered units)")
axA.set_ylabel("$K_\\mathrm{pair}$  tier-1 (1+1 reduced)", color="#1a5276")
axA2.set_ylabel("$K_\\mathrm{pair}$  s-wave tier-2, ξ = 1/6", color="#c0392b")
axA.set_title("A. Separation profile: sign positive,\nstrength dies as sech²(πs/β)", fontsize=10.5)
axA.grid(alpha=0.25)
h1, l1 = axA.get_legend_handles_labels()
h2, l2 = axA2.get_legend_handles_labels()
axA.legend(h1 + h2, l1 + l2, fontsize=8, loc="upper right")

# ---- Panel B: (1 - 4 xi) sign chart ----
tabx = p328["table_K2_s0_by_xi"]
xis = np.array([float(Fraction(k)) for k in tabx])
k2s = np.array(list(tabx.values()))
k2_0 = tabx["0"]
xi_line = np.linspace(0, 1, 200)
axB.axvspan(0.25, 1.0, color="#c0392b", alpha=0.10)
axB.plot(xi_line, k2_0 * (1 - 4 * xi_line), color="#7d3c98", lw=1.6,
         label="$K_2(\\xi) = (1-4\\xi)\\,K_2(0)$ (stored scale)")
axB.plot(xis, k2s, "o", color="#7d3c98", ms=7, label="Phase 328 stored table (s = 0)")
axB.axhline(0, color="k", lw=0.9)
axB.axvline(0.25, color="#c0392b", ls="--", lw=1.2)
axB.annotate("zero at ξ = 1/4", xy=(0.25, 0.0012), fontsize=9.5, color="#c0392b")
axB.annotate("ξ > 1/4: SIGN REFUSED\n(carrier sources the wrong way)",
             xy=(0.62, -0.010), fontsize=9.5, color="#c0392b", ha="center")
axB.axvline(1 / 6, color="#1a6b3c", ls=":", lw=1.4)
axB.annotate("ξ = 1/6 (conformal):\nsign survives, factor 1/3",
             xy=(1 / 6, k2_0 * (1 - 4 / 6)), xytext=(0.30, 0.0048), fontsize=9.5,
             color="#1a6b3c", arrowprops=dict(arrowstyle="->", color="#1a6b3c"))
axB.set_xlabel("nonminimal coupling ξ")
axB.set_ylabel("$K_\\mathrm{pair}$ s-wave tier-2 at s = 0 (β = 2π, $r_+$ = 1)")
axB.set_title("B. The sign is ξ-dependent:\nmeasured factor (1 − 4ξ)", fontsize=10.5)
axB.legend(fontsize=8.5, loc="lower left")
axB.grid(alpha=0.25)

# ---- Panel C: QI price line ----
rt = p331["reduced_tables_beta2pi"]
hs = np.array([v["h"] for v in rt.values()])
rexc = np.array([v["R_excursion_taunat"] for v in rt.values()])
h_line = np.linspace(0, 1, 200)
formula = p331["READ-E_reduced"]["R_excursion_of_h"]     # stored: "12*h - 1"
r_line = np.maximum(0.0, eval_stored(formula, h=h_line))
axC.plot(h_line, r_line, color="#1a5276", lw=1.8,
         label="$R_\\mathrm{exc}$ = max(0, 12h − 1) (stored formula)")
axC.plot(hs, rexc, "o", color="#1a5276", ms=7, label="Phase 331 stored table (β = 2π)")
def F(x):
    """Stored h values may be fraction strings ('5/24') or floats."""
    return float(Fraction(x)) if isinstance(x, str) else float(x)

h_cross = F(p331["READ-E_reduced"]["peak_crossing_h"])      # stored "1/12"
h_floor = F(p331["READ-W"]["h_QI_floor_weighted"])          # stored "5/24"
axC.axvline(h_cross, color="#1a6b3c", ls=":", lw=1.4)
axC.annotate(f"crossing at h = 1/12:\nprice → 0", xy=(h_cross, 6.5),
             xytext=(0.16, 7.5), fontsize=9.5, color="#1a6b3c",
             arrowprops=dict(arrowstyle="->", color="#1a6b3c"))
axC.axvline(h_floor, color="#c0392b", ls="--", lw=1.2)
axC.annotate("QI floor (weighted read)\nh = 5/24", xy=(0.215, 2.2), fontsize=9.5,
             color="#c0392b")
axC.set_xlabel("coupling strength h")
axC.set_ylabel("$R_\\mathrm{exc}$ at natural sampling time $\\tau_\\mathrm{nat}$ = β/π")
axC.set_title("C. Quantum inequalities price the port:\nthey meter the depth, they do not forbid the crossing",
              fontsize=10.5)
axC.legend(fontsize=8.5, loc="upper left")
axC.grid(alpha=0.25)

fig.tight_layout()
out = f"{ROOT}/publication/figures/fig_kpair.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
