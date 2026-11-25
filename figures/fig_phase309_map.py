#!/usr/bin/env python3
"""Figure: Phase 309 design-space map -- the 84-cell evasion table as a grid.

The grid is PARSED from the stored map document itself
(phase309/results/DESIGN_SPACE_MAP.md, section (i), rows 1-12 x walls
K-A..K-G, cell entries of the form '**K-X -- STATE'). No cell state is
typed into this script; the parser asserts 84 cells.

Source: phase309/results/DESIGN_SPACE_MAP.md
Output: fig_phase309_map.png
"""
import re
from collections import Counter

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = "/home/hatch/workspace/warp-pilot"
doc = open(f"{ROOT}/phase309/results/DESIGN_SPACE_MAP.md", encoding="utf-8").read()
sec = doc.split("## 1. The 84 cells, row by row")[1].split("## 2. Rows considered")[0]

STATES = ["DECIDED", "PRICED", "CLOSED", "OPEN", "UNREACHED"]
COLORS = {"DECIDED": "#2e7d4f", "PRICED": "#2b6cb0", "CLOSED": "#6b6b6b",
          "OPEN": "#d9a404", "UNREACHED": "#d7d7d7"}
LETTER = {"DECIDED": "D", "PRICED": "P", "CLOSED": "C", "OPEN": "O",
          "UNREACHED": "·"}

rows = {}
cur = None
for line in sec.splitlines():
    mh = re.match(r"### Row (\d+) — (.+)", line)
    if mh:
        cur = int(mh.group(1))
        name = re.split(r"[;(]", mh.group(2))[0].strip()
        rows[cur] = {"name": name, "cells": {}}
        continue
    mc = re.search(r"\*\*K-([A-G]) — (DECIDED|PRICED|CLOSED|OPEN|UNREACHED)", line)
    if mc and cur is not None and mc.group(1) not in rows[cur]["cells"]:
        rows[cur]["cells"][mc.group(1)] = mc.group(2)

grid = []
counts = Counter()
for r in range(1, 13):
    assert r in rows, f"row {r} missing"
    row = []
    for k in "ABCDEFG":
        st = rows[r]["cells"].get(k)
        assert st, f"cell R{r} K-{k} not parsed"
        row.append(st)
        counts[st] += 1
    grid.append(row)
total = sum(counts.values())
print(f"parsed {total} cells:", dict(counts))
assert total == 84

fig, ax = plt.subplots(figsize=(10.5, 7.6))
fig.patch.set_facecolor("white")
for i, row in enumerate(grid):
    for j, st in enumerate(row):
        ax.add_patch(plt.Rectangle((j, 11 - i), 1, 1, facecolor=COLORS[st],
                                   edgecolor="white", lw=1.5))
        ax.text(j + 0.5, 11 - i + 0.5, LETTER[st], ha="center", va="center",
                fontsize=11, fontweight="bold",
                color="white" if st in ("DECIDED", "PRICED", "CLOSED") else "#333333")
ax.set_xlim(0, 7)
ax.set_ylim(0, 12)
ax.set_xticks(np.arange(7) + 0.5)
ax.set_xticklabels([f"K-{c}" for c in "ABCDEFG"], fontsize=11)
ax.xaxis.set_ticks_position("top")
ax.set_yticks(np.arange(12) + 0.5)
ax.set_yticklabels([f"R{r}: {rows[r]['name']}" for r in range(12, 0, -1)],
                   fontsize=8.6)
ax.tick_params(length=0)
for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_title("Phase 309 — THE MAP: evasion table, 84 cells (12 route classes × 7 walls)\n"
             + " · ".join(f"{s} {counts[s]}" for s in STATES)
             + "  (states as compiled by Phase 309)", fontsize=11, pad=28)
ax.legend(handles=[Patch(facecolor=COLORS[s], label=f"{s} ({counts[s]})")
                   for s in STATES],
          loc="upper center", bbox_to_anchor=(0.5, -0.045), ncol=5, fontsize=9.5,
          frameon=False)
fig.tight_layout()
out = f"{ROOT}/publication/figures/fig_phase309_map.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
