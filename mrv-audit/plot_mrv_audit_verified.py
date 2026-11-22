"""MRV wormhole audit -- what the independent audit VERIFIED (Gate-3).

Two panels, both on the healthy side of the audit of
Mironov-Rubakov-Volkova, arXiv:1811.05832 (JHEP/CQG 2019), whose
wormhole has J = sqrt(r^2 + tau^2), tau = 10, A = B = 1:

(a) Radial (l=0) sector: the kinetic coefficient K0, divided by J^2
    (covariant normalisation), from two independent from-the-action
    derivations (Gate-3 worker V2; Phase 4 worker F4-2b).  On the
    corrected coefficients K0 > 0 at every sampled radius and
    K0/J^2 -> +1/tau^2 = +0.01 at BOTH infinities.  The printed
    Appendix-B formula (V2's printed route, converted from the
    Appendix-B normalisation by /2) instead goes negative on the
    r < 0 side (K0 = -34.91 at r = -40) and tends to -1/tau^2 as
    r -> -infinity: the printed l=0 "ghost" is an artefact of two
    spurious printed terms, not of the theory.

(b) Odd sector, l=2: the effective potential
    V_eff = l(l+1)/J^2 + V,  V = 2 J'^2/J^2 - 2 J''/J - 2/J^2
    (closed form -4 tau^2 / J^4, checked not assumed), evaluated on
    Gate-3 V3's own box grid.  V_eff > 0 everywhere; its minimum is
    0.0015924 at the box edge r = -60, and the lowest mode is
    om^2 = +0.008254 on two grids: no odd-sector tachyon.

All plotted values are read from the result files at render time
(gate3/results/v_g3_2.json, gate3/results/v_g3_3.json,
phase4/results/p42b_ell0_indep.json) and asserted against the
stored verdict numbers.  All arithmetic float64.
"""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "mrv_audit_verified.png")
TAU = 10.0

# ----------------------------------------------------------------------
# (a) radial sector: K0 / J^2
# ----------------------------------------------------------------------
v2 = json.load(open(os.path.join(WP, "gate3/results/v_g3_2.json")))
s1 = v2["subtask1_K0_from_action"]
assert s1["all_spot_K0_positive"] is True
assert abs(s1["min_spot_K0"] - 0.004515900049353649) < 1e-15

r_v2 = np.array(sorted(float(k) for k in s1["profile"]), dtype=np.float64)
k_v2 = np.array([s1["profile"][f"{r:.1f}"]["K0_over_J2"] for r in r_v2],
                dtype=np.float64)
assert np.all(k_v2 > 0)

# far-field spots (same V2 route): K0/J^2 -> +1/tau^2 at both infinities
asym = s1["asymptotics"]
for rr in ("100.0", "200.0", "400.0", "-100.0", "-200.0", "-400.0"):
    assert abs(asym[rr]["K0_over_J2"] - 1.0 / TAU**2) < 3e-4
asym_txt = ", ".join(f"{asym[s]['K0_over_J2']:.5f}"
                     for s in ("100.0", "200.0", "400.0"))

# F4-2b independent route (Phase 4): 31 radii, covariant normalisation
f42b = json.load(open(os.path.join(
    WP, "phase4/results/p42b_ell0_indep.json")))["profile"]
r_f = np.array(sorted(float(k) for k in f42b), dtype=np.float64)
k_f = np.array([f42b[f"{r:.1f}"]["K0"] / f42b[f"{r:.1f}"]["J"]**2
                for r in r_f], dtype=np.float64)
assert np.all(np.array([f42b[f"{r:.1f}"]["K0"] for r in r_f]) > 0)
# the two independent routes agree at common radii: <= 0.5% at every
# common radius except r = -0.1 (1.94%), where K0 ~ 0.0045 is at its
# smallest (K0 vanishes quadratically at the throat, so the relative
# difference inflates while the absolute difference is 8.6e-5)
common = [r for r in r_v2 if f"{r:.1f}" in f42b]
devs = {r: abs(s1["profile"][f"{r:.1f}"]["K0"] - f42b[f"{r:.1f}"]["K0"])
        / f42b[f"{r:.1f}"]["K0"] for r in common}
max_dev = max(v for r, v in devs.items() if abs(r) >= 0.5)
assert max_dev < 0.005, max_dev
assert abs(devs[-0.1] - 0.01941) < 1e-4

# printed Appendix-B route (V2 subtask 2): K0 in App-B normalisation,
# converted here to the covariant K0/J^2 by /2/J^2
s2 = v2["subtask2_printed_route"]
assert abs(s2["K0_printed_samples"]["r=-40"] - (-34.913390930889065)) < 1e-9
assert s2["K0_corr_all_positive_on_grid"] is True
assert s2["K0_corr_min_on_grid"] > 0
r_p = np.array([float(k.split("=")[1]) for k in s2["K0_printed_samples"]],
               dtype=np.float64)
k_p = np.array([s2["K0_printed_samples"][f"r={int(r)}"] / 2.0
                / (r**2 + TAU**2) for r in r_p], dtype=np.float64)
assert k_p[r_p == -40.0][0] < 0 and k_p[r_p == -20.0][0] < 0
p_asym = s2["asymptotics"]
for rr in ("-100.0", "-200.0", "-400.0"):
    conv = p_asym[rr]["K0_printed"] / 2.0 / (float(rr)**2 + TAU**2)
    assert abs(conv - (-1.0 / TAU**2)) < 3e-4  # printed -> -1/tau^2, r -> -inf

# ----------------------------------------------------------------------
# (b) odd sector: V_eff for l = 2 (Gate-3 V3's formula and box grid)
# ----------------------------------------------------------------------
v3 = json.load(open(os.path.join(WP, "gate3/results/v_g3_3.json")))
stored = v3["task1a_odd_sector"]["per_ell"]["ell2"]
assert abs(stored["Veff_min"] - 0.0015924032140248357) < 1e-15
assert stored["Veff_min_r"] == -60.0
assert stored["Veff_positive_everywhere"] is True


def odd_V(r):
    J = np.sqrt(r**2 + TAU**2)
    Jp = r / J
    Jpp = TAU**2 / J**3
    return 2.0 * Jp**2 / J**2 - 2.0 * Jpp / J - 2.0 / J**2


r_box = np.linspace(-60.0, 60.0, 12001)
J_box = np.sqrt(r_box**2 + TAU**2)
V_box = odd_V(r_box)
cf_dev = float(np.max(np.abs(V_box + 4.0 * TAU**2 / J_box**4)))
assert cf_dev < 2e-17, cf_dev  # closed form -4 tau^2/J^4, as V3 stored
veff2 = 2 * 3 / J_box**2 + V_box
i_min = int(np.argmin(veff2))
assert abs(veff2[i_min] - stored["Veff_min"]) < 1e-12
assert r_box[i_min] == stored["Veff_min_r"]
assert np.all(veff2 > 0)
om2_low = v3["task1a_odd_sector"]["ell2_lowest_eigs_two_grids"]["N4801"][0]
assert abs(om2_low - 0.008254432498221389) < 1e-12

# ----------------------------------------------------------------------
# figure
# ----------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

ax1.axhline(0.0, color="black", lw=0.9)
ax1.axhline(1.0 / TAU**2, color="#c0392b", lw=1.4, ls="--",
            label="asymptote $+1/\\tau^2 = +0.01$ (both infinities)")
ax1.plot(r_v2, k_v2, "o-", ms=6, lw=1.2, color="#005f8f", mec="white",
         mew=1.0, zorder=5,
         label="corrected, from the action — Gate-3 V2")
ax1.plot(r_f, k_f, "s", ms=5, mfc="none", color="#b34700", mew=1.3,
         zorder=5, label="corrected, from the action — Phase 4 F4-2b")
ax1.plot(r_p, k_p, "x", ms=9, color="#c0392b", mew=2.0, zorder=6,
         label="printed Appendix-B formula (V2 printed route, $\\div 2$)")
ax1.text(0.99, 0.02,
         "printed route: $\\mathcal{K}_0/J^2 = -0.0103$ at $r = -40$ "
         "($\\mathcal{K}_0 = -34.91$, App-B),\n"
         "and $\\rightarrow -1/\\tau^2$ as $r \\rightarrow -\\infty$\n"
         f"corrected $\\mathcal{{K}}_0/J^2$ at $|r| = 100/200/400$: "
         f"{asym_txt} $\\rightarrow +1/\\tau^2$;\n"
         "corrected $\\mathcal{K}_0 > 0$ on the whole grid "
         f"(two routes agree to $\\leq$0.5% off-throat)",
         transform=ax1.transAxes, fontsize=8.5, ha="right", va="bottom",
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.7", alpha=0.95))
ax1.set_xlim(-62, 62)
ax1.set_ylim(-0.0175, 0.034)
ax1.set_xlabel("wormhole coordinate $r$  ($J = \\sqrt{r^2 + \\tau^2}$, $\\tau = 10$)")
ax1.set_ylabel("$\\mathcal{K}_0 / J^2$ (covariant normalisation)")
ax1.set_title("(a) radial sector ($\\ell = 0$): corrected "
              "$\\mathcal{K}_0/J^2 > 0$ everywhere")
ax1.grid(alpha=0.25)
ax1.legend(loc="upper left", fontsize=8.5)

ax2.axhline(0.0, color="black", lw=0.9)
ax2.plot(r_box, veff2, lw=1.5, color="#005f8f",
         label="$V_{\\mathrm{eff}} = \\ell(\\ell+1)/J^2 + V$, $\\ell = 2$")
ax2.plot([-60.0], [veff2[i_min]], "o", ms=8, color="#c0392b", mec="white",
         mew=1.2, zorder=5, label="minimum (box edge)")
ax2.annotate(f"min $V_{{\\mathrm{{eff}}}} = {veff2[i_min]:.7f}$ at $r = -60$\n"
             f"lowest $\\omega^2 = +0.008254$ (two grids) — no tachyon",
             xy=(-60.0, veff2[i_min]), xytext=(-38, 0.0125),
             fontsize=8.5, color="#7b241c",
             arrowprops=dict(arrowstyle="->", color="#7b241c", lw=1.0))
ax2.set_xlim(-62, 62)
ax2.set_ylim(-0.001, 0.0215)
ax2.set_xlabel("wormhole coordinate $r$ (tortoise coordinate, $A = B = 1$)")
ax2.set_ylabel("$V_{\\mathrm{eff}}(r)$")
ax2.set_title("(b) odd sector ($\\ell = 2$): tachyon pass")
ax2.grid(alpha=0.25)
ax2.legend(loc="upper right", fontsize=8.5)

fig.suptitle("MRV wormhole (arXiv:1811.05832) — what the independent "
             "audit verified", fontsize=11.5)
fig.text(0.5, 0.012,
         "Independent audit of Mironov–Rubakov–Volkova (2019): the radial "
         "sector is healthy on the corrected coefficients and the odd "
         "sector has no tachyon.\nThe even-sector $\\ell\\geq2$ question "
         "is under certification and is not shown.",
         ha="center", fontsize=9.5)
fig.tight_layout(rect=[0, 0.055, 1, 0.93])
fig.savefig(OUT, dpi=200)
print("saved", OUT)
print("panel (a): V2 spots", len(r_v2), " F4-2b spots", len(r_f),
      " max route dev", max_dev)
print("panel (a): printed K0/J^2 at r=-40:", k_p[r_p == -40.0][0],
      " (K0 = -34.913390930889065 App-B)")
print("panel (b): Veff_min =", veff2[i_min], "at r =", r_box[i_min],
      " closed-form dev =", cf_dev)
