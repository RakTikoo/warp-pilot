#!/usr/bin/env python3
"""Figure: Gate-13 / Phase 116 composed payload configuration -- shell layout.

Geometry is read from stored files only: the shell supports and region cuts
are regex-extracted from the stored bundle code (gate13-claims/code/
wa_profiles.py: build_shell calls and region_name), the outer span from the
stored alone-ladder file, and the row anatomy (held payload, shell betas)
from the stored composed-results file.

Sources:
  gate13-claims/code/wa_profiles.py                  (shell supports, regions)
  gate13-claims/sources/p1161_alone.json             (outer span lo/hi)
  gate13-claims/sources/p1161_composed.json          (row anatomy)
Output: fig_gate13_schematic.png
"""
import json
import re

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

ROOT = "/home/hatch/workspace/warp-pilot"

code = open(f"{ROOT}/gate13-claims/code/wa_profiles.py").read()
shells = [(float(a), float(b)) for a, b in
          re.findall(r"build_shell\((\d+\.\d+),\s*(\d+\.\d+)", code)]
shells.sort()
inner, outer = shells[0], shells[1]          # (2, 4) inner, (5, 10) outer
reg = open(f"{ROOT}/gate13-claims/code/wa_profiles.py").read()
m = re.search(r"def region_name\(rr\):(.+?)\n\n", reg, re.S)
cuts = [float(x) for x in re.findall(r"(\d+\.\d+)", m.group(1))]
r_payload, r_cavity, r_outer_end = cuts[0], cuts[2], cuts[3]

alone = json.load(open(f"{ROOT}/gate13-claims/sources/p1161_alone.json"))
span = alone["spans"]["e0.10"]
span_lo, span_hi = span["lo"], span["hi"]

comp = json.load(open(f"{ROOT}/gate13-claims/sources/p1161_composed.json"))
best_key, best = max(comp["rows"].items(),
                     key=lambda kv: kv[1]["anatomy"]["payload_relat"])
anat = best["anatomy"]
payload_c = anat["payload_relat"]
print(f"shells from stored code: inner {inner}, outer {outer}; "
      f"region cuts {cuts}; span [{span_lo}, {span_hi}]; row {best_key}: "
      f"payload {payload_c}, beta_i {anat['beta_i_alone']}, beta_o {anat['beta_o_alone']}")

fig, ax = plt.subplots(figsize=(8.6, 8.2))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

def ring(r_in, r_out, color, label, alpha=0.75, hatch=None):
    ax.add_patch(Wedge((0, 0), r_out, 0, 360, width=r_out - r_in,
                       facecolor=color, alpha=alpha, edgecolor="k",
                       lw=0.7, hatch=hatch))
    return label

# span (source-spline support): dashed outline circles only, so the ring
# reads as a support interval and does not tint the cavity it overlaps
for rr in (span_lo, span_hi):
    ax.add_patch(Circle((0, 0), rr, fill=False, edgecolor="#b8860b",
                        lw=1.4, ls="--"))
ring(outer[0], outer[1], "#e07a5f", "outer shell")
ring(inner[0], inner[1], "#3d7ea6", "inner shell")
ring(inner[1], outer[0], "#dddddd", "cavity", alpha=0.55, hatch="//")
ax.add_patch(Circle((0, 0), r_payload, facecolor="#f2d16b", edgecolor="k", lw=0.9))

ax.annotate(f"payload region  r < {r_payload:.0f}\nheld payload = {payload_c:.5f}c",
            xy=(0.7, 0.7), xytext=(-9.6, 8.6), fontsize=10, fontweight="bold",
            arrowprops=dict(arrowstyle="->"))
ax.annotate(f"inner shell  [{inner[0]:.0f}, {inner[1]:.0f}]\n"
            f"$\\beta_i$ = {anat['beta_i_alone']} (alone)",
            xy=(-2.9, 1.9), xytext=(-10.4, 3.4), fontsize=10,
            arrowprops=dict(arrowstyle="->"))
ax.annotate(f"cavity  ({inner[1]:.0f}, {outer[0]:.0f})", xy=(3.4, -3.1),
            xytext=(5.4, -8.8), fontsize=10, arrowprops=dict(arrowstyle="->"))
ax.annotate(f"outer shell  [{outer[0]:.0f}, {outer[1]:.0f}]\n"
            f"$\\beta_o$ = {anat['beta_o_alone']} (alone)",
            xy=(6.4, 6.4), xytext=(3.2, 11.6), fontsize=10,
            arrowprops=dict(arrowstyle="->"))
ax.annotate(f"outer source span (ext 0.10): [{span_lo}, {span_hi}]",
            xy=(-7.8, -7.8), xytext=(-11.8, -12.6), fontsize=10,
            color="#8a6414", arrowprops=dict(arrowstyle="->", color="#8a6414"))

ax.set_xlim(-13.2, 13.2)
ax.set_ylim(-13.6, 13.6)
ax.set_aspect("equal")
ax.set_xlabel("x (geometric units)")
ax.set_ylabel("y (geometric units)")
ax.set_title("Gate-13 composed payload configuration (cross-section)\n"
             "nested shells under the Phase-46 composition protocol; "
             f"row {best_key}", fontsize=11)
ax.grid(alpha=0.2)
fig.tight_layout()
out = f"{ROOT}/publication/figures/fig_gate13_schematic.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
