#!/usr/bin/env python3
"""Gate-16/19 figure: what the fluid_T adjudication changed.

All values read from gate16-claims/results/g19_g16_results.json (the
Gate-19 re-judgement of the Gate-16 set): the corrected legality, the
machinery rows' grouped EoM scores, and the full EC minima. The script
locates the corrected legality 0.8928571428571429 in the stored record by
search rather than by a typed key path.
"""
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = "/home/hatch/workspace/warp-pilot"
FIG = f"{ROOT}/publication/figures"
d = json.load(open(f"{ROOT}/gate16-claims/results/g19_g16_results.json"))

def find(x, target, path=""):
    if isinstance(x, float) and abs(x - target) < 1e-12:
        return path
    if isinstance(x, dict):
        for k, v in x.items():
            r = find(v, target, f"{path}/{k}")
            if r:
                return r
    if isinstance(x, list):
        for i, v in enumerate(x):
            r = find(v, target, f"{path}[{i}]")
            if r:
                return r
    return None

corr_path = find(d, 0.8928571428571429)
print("corrected legality found at:", corr_path)
_node = d
for _seg in corr_path.strip("/").split("/"):
    _node = _node[int(_seg[1:-1])] if _seg.startswith("[") else _node[_seg]
corr_legal = _node
hinge = d["hinge"]
rows = d["machinery_gate"]["rows"]

fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.4))
fig.patch.set_facecolor("white")

ax = axes[0]
ax.bar(["hinge candidate,\ncorrected tensor",
        "best candidate (p1281),\ncorrected tensor"],
       [hinge["subset_legal"], corr_legal],
       color=["0.55", "tab:green"])
ax.set_ylim(0, 1)
ax.set_ylabel("legality (subset frame)")
ax.set_title("A. G16-1 restated under Gate-19's\nfluid_T fix: legality 0.75 -> 0.8929",
             fontsize=10)

ax = axes[1]
ax.bar([r["name"].replace("direct/", "") for r in rows],
       [r["emax"] for r in rows], color="tab:red", alpha=0.7)
ax.axhline(1.0, color="k", lw=1)
ax.set_ylabel("grouped EoM score, max")
ax.set_title("B. But the joint pass still fails:\nevery machinery row's grouped score ~ 1",
             fontsize=10)
ax.tick_params(axis="x", labelrotation=30, labelsize=7.5)

ax = axes[2]
ec = hinge["ec_min_full"]
ax.bar(list(ec.keys()), [ec[k] for k in ec], color="tab:purple", alpha=0.75)
ax.axhline(0, color="k", lw=1)
ax.set_ylabel("EC minimum (full read)")
ax.set_title("C. Full energy-condition minima\nof the hinge candidate", fontsize=10)
fig.tight_layout()
out = f"{FIG}/fig_gate16_legality.png"
fig.savefig(out, dpi=200, facecolor="white")
print("wrote", out)
