"""P16-1 breathing warp shell (Phase 16, Gate-4 claim G4-1(a),
gate-restated form): per-instant core margins over one full period
for the breathing Finalist-A shell (delta=0.5, T=40, beta=0.02),
read at render time from phase16/results/p161_breathing_d0.5_T40.json
(12 audited instants, h=0.3; worst instant re-audited at h=0.15),
with the static twin's core worst margin from
phase16/results/p161_static.json as reference. The delta=1.0
annotation follows GATE4.md's restatement: the dynamic audit fails
at every grid spacing in two independent auditors, and the frozen
slice's sampled margin +1.53e-05 (from
phase16/results/p161_controls.json) is quoted as an h=0.3 value.
All float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "breathing_shell.png")

b = json.load(open(os.path.join(
    WP, "phase16/results/p161_breathing_d0.5_T40.json")))
inst = b["instants"]
t = np.array([float(i["t"]) for i in inst], dtype=np.float64)
sec = np.array([float(i["core"]["sec"]) for i in inst], dtype=np.float64)
worst = np.array([float(i["core"]["worst"]) for i in inst], dtype=np.float64)
typeI = np.array([float(i["core"]["typeI_frac"]) for i in inst],
                 dtype=np.float64)

st = json.load(open(os.path.join(WP, "phase16/results/p161_static.json")))
static_worst = float(st["static_h03"]["core"]["worst"])

ct = json.load(open(os.path.join(
    WP, "phase16/results/p161_controls.json")))
frozen_d1 = float(ct["frozen_breathing_d1_t26.67_R110.87_R219.13"]
                  ["core"]["worst"])
d1 = json.load(open(os.path.join(
    WP, "phase16/results/p161_breathing_d1.0_T40.json")))
dyn_d1 = min((float(i["core"]["worst"]) for i in d1["instants"]
              if abs(float(i["t"]) - 26.6667) < 0.01))

agg_sec = float(b["aggregate"]["worst_instant_core"]["sec"])
print("instants:", len(inst), "min core SEC:", sec.min(),
      "at t =", t[np.argmin(sec)])
print("static twin core worst:", static_worst)
print("frozen d=1.0 (h=0.3):", frozen_d1, " dynamic d=1.0 t=26.67:", dyn_d1)
assert len(inst) == 12
assert abs(sec.min() - 7.203001107399105e-06) < 1e-12
assert abs(agg_sec - sec.min()) < 1e-15
assert abs(t[np.argmin(sec)] - 10.0) < 1e-9
assert float(b["confirm_h015"]["t_worst"]) == 10.0
assert np.all(worst > 0) and np.all(typeI == 1.0)
assert abs(static_worst - 1.1949248907449214e-05) < 1e-12
assert abs(frozen_d1 - 1.5305074520586465e-05) < 1e-12
assert abs(dyn_d1 - (-5.460822506161556e-05)) < 1e-12

U = 1e-5  # plot margins in units of 1e-5
fig, ax = plt.subplots(figsize=(9.5, 5.6))

ax.axhline(0.0, color="#c0392b", lw=1.3, zorder=2)
ax.text(39.6, 0.04, "zero margin (illegal below)", ha="right",
        fontsize=9, color="#7b241c")

ax.plot(t, sec / U, "o-", color="#005f8f", lw=1.8, ms=5.5, zorder=4,
        label="core SEC margin at each audited instant ($\\delta$=0.5)")
ax.plot(t, worst / U, "s--", color="#e67e22", lw=1.4, ms=4.5, zorder=3,
        label="core worst-overall margin (min over NEC/WEC/SEC/DEC)")

ax.axhline(static_worst / U, color="#1e8449", lw=1.4, ls=":", zorder=3)
ax.text(40.6, static_worst / U - 0.13,
        f"static twin core worst margin: +{static_worst:.3e}",
        ha="right", fontsize=9.5, color="#145a32")

iw = int(np.argmin(sec))
ax.annotate(f"worst instant (t = 10): SEC +{sec[iw]:.3e}\n"
            "Type I everywhere; re-audited at h = 0.15",
            (t[iw], sec[iw] / U), textcoords="offset points",
            xytext=(0, -52), ha="center", fontsize=9.5, color="#00334d",
            arrowprops=dict(arrowstyle="->", color="#00334d", lw=1.0))

ax.annotate("THE $\\delta$=1.0 LESSON (gate-restated): at t = 26.67 the "
            "DYNAMIC audit\nfails at EVERY grid spacing in two independent "
            "auditors\n($-5.46\\times10^{-5}$ at h = 0.3) \u2014 a pure "
            "$\\partial_t$ failure. The frozen slice's\nType-I margins stay "
            "positive at every h, but its sampled margin\n"
            f"$+1.53\\times10^{{-5}}$ is an h = 0.3 value (marginal at "
            "r $\\approx$ 11 on finer grids).\nRobust content: the "
            "Type-I-margin split + the all-h dynamic failure \u2014\n"
            "RATE, not amplitude, kills (the T = 200 control passes).",
            (0.99, 0.615), xycoords="axes fraction", va="top", ha="right",
            fontsize=9, color="#4a235a",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#7d3c98",
                      alpha=0.92))

ax.set_xlim(-1.0, 41.0); ax.set_ylim(0.0, 1.5)
ax.set_xlabel("time within one breathing period (T = 40; 12 audited "
              "instants, h = 0.3)")
ax.set_ylabel("core margin ($\\times 10^{-5}$)")
ax.set_title("P16-1 \u2014 A breathing warp shell ($\\delta$=0.5, T=40, "
             "$\\beta$=0.02): legal at every\naudited instant, with a "
             "thinner margin than its static twin")
ax.legend(loc="lower left", fontsize=9)
ax.grid(alpha=0.25)

fig.text(0.5, 0.012,
         "Legal at every audited instant \u2014 robust-within-audit; "
         "evolution-sense stability not established\n"
         "(kinematic auditor, prescribed metric, no Einstein evolution). "
         "GR only, one shell family, $\\beta$ = 0.02.",
         ha="center", fontsize=9, color="#555555")
fig.tight_layout(rect=(0, 0.055, 1, 1))
fig.savefig(OUT, dpi=200)
print("saved", OUT)
