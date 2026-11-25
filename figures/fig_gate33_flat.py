#!/usr/bin/env python3
"""Figure: Gate-33 spin-1 (Einstein-aether vector) flat curve + Corner B.

Gate-33 stored no results JSON for these values: the quotable claim set is
the prose of GATE33.md section 5 (G33-E/F/G). This script therefore EXTRACTS
the numbers from that stored document by pattern (mantissa x 10^superscript)
-- nothing is typed in by hand; if a pattern is absent the script fails.

Source: gate33-claims/GATE33.md (section 5, G33-E and G33-F)
Output: fig_gate33_flat.png
"""
import re

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
text = open(f"{ROOT}/gate33-claims/GATE33.md", encoding="utf-8").read()

SUP = str.maketrans("⁻⁰¹²³⁴⁵⁶⁷⁸⁹", "-0123456789")

def sci(mantissa):
    """Find 'mantissa x 10^exp' (unicode superscript) in the stored text."""
    pat = re.escape(mantissa) + r"×10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)"
    m = re.search(pat, text)
    assert m, f"pattern for mantissa {mantissa} not found in GATE33.md"
    return float(mantissa) * 10 ** int(m.group(1).translate(SUP))

ht_flat = sci("1.87")        # G33-F headline, data-grade cap 0.067
ns_flat = sci("1.70")        # G33-F NS-BH bound-class
ht_95 = sci("5.42")          # G33-F stated alternative (95% face)
ns_95 = sci("4.91")
ht_corner = sci("2.0607")    # G33-E Corner B HT ratio at its coordinate
ns_corner = sci("1.8660")    # G33-E Corner B NS-BH bound-class
m = re.search(r"c₁₄\* = ([\d.]+)×10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+) \(c_V = ([\d.]+)", text)
assert m, "Corner B coordinate pattern not found"
c14_star = float(m.group(1)) * 10 ** int(m.group(2).translate(SUP))
cv_corner = float(m.group(3))
print(f"extracted from GATE33.md: HT flat {ht_flat:.3e}, NS-BH flat {ns_flat:.3e}, "
      f"95% face {ht_95:.3e}/{ns_95:.3e}, Corner B c14* {c14_star:.4e} at "
      f"c_V {cv_corner}, HT {ht_corner:.4e}, NS-BH {ns_corner:.4e}")

cv_flat = np.array([1.0, 2.0, 10.0])   # "at c_V = 1, 2 and 10 alike" (G33-F)

fig, ax = plt.subplots(figsize=(9.4, 5.8))
fig.patch.set_facecolor("white")
ax.plot(cv_flat, [ht_flat] * 3, "o-", color="#1a5276", lw=2, ms=8,
        label=f"flat curve (G33-F, data-grade cap): HT = {ht_flat:.2e}")
ax.plot(cv_flat, [ht_95] * 3, "o--", color="#1a5276", alpha=0.45, lw=1.2, ms=6,
        label=f"stated alternative, 95% face: HT = {ht_95:.2e} (not the headline)")
ax.axhline(1e-6, color="#c0392b", ls=":", lw=1.3,
           label="G33-G distance-0 bar: HT ≥ 10⁻⁶ (met at c_V = 2 under every pricing)")
ax.plot([cv_corner], [ht_corner], "*", ms=20, color="#b8860b",
        label=f"Corner B (G33-E): HT ratio {ht_corner:.3e} at c_V = {cv_corner:.0f}")
ax.annotate(f"Corner B survives at c₁₄* = {c14_star:.3e},\nc_V = {cv_corner:.0f} "
            f"(second-pathed coordinate)", xy=(cv_corner, ht_corner),
            xytext=(60, 3.2e-13), fontsize=9.5, color="#8a6414",
            arrowprops=dict(arrowstyle="->", color="#8a6414"))
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.8, 9000)
ax.set_xlabel("vector-mode speed  $c_V$  (log scale)")
ax.set_ylabel("HT dipole-ratio strain measure (log scale)")
ax.set_title("Gate-33: the spin-1 channel's flat curve and Corner B\n"
             "flat = speed-independent at c_V = 1, 2, 10 (NS–BH bound-class "
             f"{ns_flat:.2e} flat; 95% face {ns_95:.2e};\nCorner B NS–BH {ns_corner:.3e})",
             fontsize=10.5)
ax.legend(fontsize=8.8, loc="lower left")
ax.grid(alpha=0.25, which="both")
fig.tight_layout()
out = f"{ROOT}/publication/figures/fig_gate33_flat.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
