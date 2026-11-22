"""P16-2 transient quantum-inequality law (Phase 16, Gate-4 claim
G4-1(b), UPLOAD-READY as gated): the exact legal pulse duration
tau* relative to the wall-thickness crossing time Delta/c, for all
27 sweep configurations, read at render time from
phase16/results/p162_ledger.json (162 ratio rows confirmed against
the closed form to 2.9e-16 in log10). The law's scaling and the
tau* functional form are Pfenning & Ford 1997, eq. (17); the
closed-form ratio in the free variable (ctau/Delta)^4 and the
tanh-profile prefactor k = f'_max * Delta_eff ~ 1.50-1.61 are this
work (Gate-4 delimitation). tau here is a wall LIFETIME, not
Pfenning & Ford's observer-crossing sampling time. All float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "qi_pulse_law.png")

L = json.load(open(os.path.join(WP, "phase16/results/p162_ledger.json")))
cfgs = L["configs"]
assert len(cfgs) == 27 and len(L["table_ratio_required_over_legal"]) == 162

delta = np.array([float(c["Delta_eff_m"]) for c in cfgs], dtype=np.float64)
beta = np.array([float(c["beta_v_over_c"]) for c in cfgs], dtype=np.float64)
k = np.array([float(c["k_fpmax_times_Delta"]) for c in cfgs],
             dtype=np.float64)
ustar = np.array([float(c["u_star_c_tau_star_over_Delta"]) for c in cfgs],
                 dtype=np.float64)
ratio_cross = np.array(
    [float(c["ratio_at_crossing_tau_eq_Delta_over_c"]) for c in cfgs],
    dtype=np.float64)

proper = k > 1.0  # 24 proper-wall rows; the diffuse profile (k=0.069) x 3 beta
print("k (proper):", k[proper].min(), "...", k[proper].max(),
      " outlier k:", k[~proper])
print("u* range:", ustar.min(), "...", ustar.max())
print("min ratio at crossing:", ratio_cross.min())
assert abs(ratio_cross.min() - 3.939904393564e+64) / 3.939904393564e+64 < 1e-9
imin = int(np.argmin(ratio_cross))
assert abs(delta[imin] - 0.454219498569822) < 1e-9
assert abs(beta[imin] - 0.1) < 1e-12
assert k[proper].min() > 1.4999 and k[proper].max() < 1.6117
assert (~proper).sum() == 3 and np.all(np.abs(k[~proper] - 0.0690196) < 1e-6)
assert 7.9e-19 < ustar.min() < 8.0e-19
assert 7.0e-17 < ustar.max() < 7.2e-17
orders = -np.log10(ustar)
assert orders.min() > 16.0 and orders.max() < 18.2
assert float(L["scaling_fit"]
             ["max_log10_deviation_from_closed_form_with_k"]) < 1e-12

fig, ax = plt.subplots(figsize=(9.5, 5.6))

ax.axhspan(-18.3, -16.0, color="#7d3c98", alpha=0.06, zorder=0)
ax.axhline(0.0, color="#c0392b", lw=1.5, zorder=2,
           label="crossing duration: $\\tau$ = $\\Delta$/c "
                 "($\\tau^*$/(\\Delta/c) = 1)")

colors = {0.1: "#005f8f", 0.5: "#e67e22", 1.0: "#1e8449"}
for bv in (0.1, 0.5, 1.0):
    m = beta == bv
    ax.scatter(delta[m], np.log10(ustar[m]), s=64, color=colors[bv],
               zorder=4, label=f"$\\beta$ = {bv}")
ax.scatter(delta[~proper], np.log10(ustar[~proper]), s=110,
           facecolors="none", edgecolors="#7d3c98", lw=1.4, zorder=5,
           label="diffuse outlier (k = 0.069)")

ax.annotate("", xy=(0.30, -16.15), xytext=(0.30, -0.6),
            arrowprops=dict(arrowstyle="->", color="#4a235a", lw=1.3))
ax.text(18.5, -17.05, "the gap: $\\tau^*$ sits 16\u201318 orders of "
        "magnitude below $\\Delta$/c \u2014 for every configuration",
        fontsize=9.5, color="#4a235a", ha="right")

ax.annotate("THE LAW (closed form, this work):\n"
            "ratio = ($\\pi$k$^2$/3)\u00b7$\\beta^2$\u00b7"
            "($\\Delta$/$\\ell_P$)$^2$\u00b7(c$\\tau$/$\\Delta$)$^4$,"
            "   k = f$'_{max}$\u00b7$\\Delta_{eff}$ $\\approx$ "
            "1.50\u20131.61\n"
            "$\\tau^*$ = [3/($\\pi$k$^2$$\\beta^2$)]$^{1/4}$"
            "\u00b7$\\sqrt{\\ell_P \\Delta}$/c  \u2014 the geometric-mean "
            "time\n"
            "confirmed with prefactor across 162 rows (matches to "
            "2.9$\\times$10$^{-16}$ in log$_{10}$)\n"
            f"at $\\tau$ = $\\Delta$/c: required/legal ratio "
            f"$\\geq$ {ratio_cross.min():.6e} (sweep minimum:\n"
            "R = 1 m, $\\Delta_{eff}$ = 0.454 m, $\\beta$ = 0.1); "
            "pulse trains do not evade the sustained\n"
            "law (legal duty cycle $\\leq$ ~10$^{-65}$, quantum "
            "interest)",
            (0.985, 0.50), xycoords="axes fraction", ha="right",
            va="top", fontsize=9, color="#00334d",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#005f8f",
                      alpha=0.92))

ax.set_xscale("log")
ax.set_xlim(0.12, 20.0); ax.set_ylim(-19.2, 1.6)
ax.set_xlabel("effective wall thickness $\\Delta_{eff}$ (m)")
ax.set_ylabel("log$_{10}$[ $\\tau^*$ / ($\\Delta$/c) ]")
ax.set_title("P16-2 \u2014 The transient QI window: a warp wall's exact "
             "legal lifetime $\\tau^*$\nvs the time light needs to cross "
             "its own wall")
ax.legend(loc="upper left", fontsize=9)
ax.grid(alpha=0.25, which="both")

fig.text(0.5, 0.012,
         "Scaling and $\\tau^*$ form: Pfenning & Ford 1997, eq. (17); "
         "closed-form ratio and prefactor k $\\approx$ 1.50\u20131.61: "
         "this work.\n"
         "A QI-legal pulse is a statement about quantum bounds, NOT a "
         "drive. Registered reading: OPEN-but-incoherent;\n"
         "CLOSED at every $\\tau$ $\\geq$ $\\Delta$/c.",
         ha="center", fontsize=9, color="#555555")
fig.tight_layout(rect=(0, 0.075, 1, 1))
fig.savefig(OUT, dpi=200)
print("saved", OUT)
