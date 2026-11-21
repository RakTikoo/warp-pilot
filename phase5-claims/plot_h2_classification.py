"""H2 decoupling criterion — classification of the seven audited cases.

Criterion (Phase 5 H2): a classical gravity-sector term can supply an
energy-condition violation while remaining healthy iff the combination
the geometry forces negative is NOT slaved to the perturbation-health
combinations — rank >= 2 of the map (theory free functions) ->
(crossing, health) at the crossing point. Rank 1 with health fixing
the sign = forbidden / anti-aligned.

Classification rows: CHECKPOINT5.md H2 record (classification table,
7/7 against the audited verdicts) in the gate-restated form
(gate/GATE.md): 5 strict instances of the rank predicate + 2
structural analogies (f(T), EiBI). Quantitative cells are read from
phase5/results/h2_criterion.json (scalar-tensor rank demonstration:
gamma invariant under the F4 rescaling while H sweeps sign; f(R)
affine slope). All arithmetic float64.
"""
import json
import os
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

WP = os.path.expanduser("~/workspace/warp-pilot")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "h2_classification.png")

d = json.load(open(os.path.join(WP, "phase5/results/h2_criterion.json")))
sr = d["scalar_tensor_rank"]
h_sweep = [float(sr[f"lam={lam}"]["H_throat"]) for lam in ("0.0", "0.5", "1.0", "2.0")]
gamma_dev = float(sr["lam=2.0"]["gamma_max_dev_vs_lam1"])
slope = float(d["fR_affine_slope"]["slope_M1_from_0_to_0.01"])
print("H sweep:", h_sweep, "| gamma dev:", gamma_dev, "| f(R) slope:", slope)

STRICT = "strict instance"
ANALOGY = "structural analogy"
rows = [
    ("Horndeski\n(scalar–tensor)", STRICT + "\nrank 1: $\\gamma \\equiv \\mathcal{H}$",
     "FORBIDDEN",
     "the throat crossing $\\gamma<0$ IS the odd-parity ghost "
     "$\\mathcal{H}<0$ — slaved, no decoupling"),
    ("Beyond-Horndeski\n(MRV class)", STRICT + "\nrank 2: $\\mathcal{H}-\\gamma = 2F_4\\pi'^4$",
     "ALLOWED",
     f"rescaling $F_4$ leaves $\\gamma$ invariant (dev {gamma_dev:.1e}) while "
     f"$\\mathcal{{H}}$ sweeps {h_sweep[0]:+.2f} $\\rightarrow$ {h_sweep[-1]:+.2f} "
     "— computed decoupling"),
    ("$f(R) = R + \\alpha R^2$\n(warp wall)", STRICT + "\nrank 1: affine in $\\alpha$",
     "ANTI-ALIGNED",
     f"health pins $\\alpha>0$; NEC margin slope {slope:.2e} per unit $\\alpha$ "
     "(negative throughout the healthy branch; 516-eval scan, zero passes)"),
    ("$f(Q) = Q + \\beta Q^2$\n(warp wall)", STRICT + "\nrank 1: affine in $\\beta$",
     "ANTI-ALIGNED",
     "same algebra as $f(R)$; 60-eval scan, zero passes, monotone worsening "
     "with $\\beta$"),
    ("X4 non-minimal\nscalar (warp wall)", STRICT + "\nrank 1, both frames",
     "ANTI-ALIGNED",
     "negative in BOTH frames; the supply's sign is fixed by kinetic health "
     "in either frame"),
    ("$f(T)$ wormhole\n(Böhmer–Harko–Lobo)", ANALOGY + "\nframe sign flip",
     "ALLOWED",
     "matter obeys all conditions iff $f_T(0)<0$ — the flip lives in the "
     "frame map. ⚠ health premise unexamined (flagged by the gate)"),
    ("EiBI wormhole\n(Shaikh et al.)", ANALOGY + "\nNCC $\\neq$ NEC",
     "ALLOWED",
     "geometric convergence condition and matter NEC are different "
     "functionals with numerically disjoint windows"),
]
OUTCOME_COLOR = {"ALLOWED": "#1e8449", "FORBIDDEN": "#c0392b",
                 "ANTI-ALIGNED": "#b9770e"}

W, H = 12.4, 7.2
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

col_x = [0.15, 2.80, 5.30, 7.25]
col_w = [2.50, 2.35, 1.80, 5.00]
headers = ["Case", "Status under the\nrank predicate", "Outcome", "Deciding fact"]
top = 5.95; rh = 0.70

ax.text(W / 2, 7.02,
        "H2 — the decoupling criterion: when can a gravity-sector term hold a throat open, healthily?",
        ha="center", va="center", fontsize=12.5, weight="bold")
ax.text(W / 2, 6.68,
        "Criterion: the NEC-supplying combination must not be slaved to the health combinations (rank $\\geq 2$).",
        ha="center", va="center", fontsize=9.5)
ax.text(W / 2, 6.42,
        "A throat binds one null contraction at one locus — rank 2 has room; a warp wall binds the full set everywhere — every wall case here is rank 1.",
        ha="center", va="center", fontsize=9.5)

for x0, w, htxt in zip(col_x, col_w, headers):
    ax.add_patch(FancyBboxPatch((x0, top), w, 0.40,
                                boxstyle="round,pad=0.02,rounding_size=0.04",
                                fc="#34495e", ec="none"))
    ax.text(x0 + w / 2, top + 0.20, htxt, ha="center", va="center",
            fontsize=9.5, color="white", weight="bold")

for i, (case, status, outcome, fact) in enumerate(rows):
    y = top - (i + 1) * rh
    band = "#f4f6f7" if i % 2 == 0 else "white"
    ax.add_patch(plt.Rectangle((0.1, y), 12.2, rh, fc=band, ec="none"))
    ymid = y + rh / 2
    ax.text(col_x[0] + 0.08, ymid, case, ha="left", va="center",
            fontsize=9.5, weight="bold")
    ax.text(col_x[1] + 0.08, ymid, status, ha="left", va="center",
            fontsize=8.8, style="italic",
            color="#7d6608" if status.startswith(ANALOGY) else "#1a5276")
    ax.add_patch(FancyBboxPatch((col_x[2] + 0.06, ymid - 0.16), col_w[2] - 0.12, 0.32,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                fc=OUTCOME_COLOR[outcome], ec="none", alpha=0.9))
    ax.text(col_x[2] + col_w[2] / 2, ymid, outcome, ha="center", va="center",
            fontsize=8.4, color="white", weight="bold")
    wrapped = "\n".join(textwrap.wrap(fact.replace("\n", " "), width=66))
    ax.text(col_x[3] + 0.08, ymid, wrapped, ha="left", va="center", fontsize=8.8)

ax.text(0.15, 0.62,
        "Gate-restated form: 5 strict instances + 2 structural analogies (the original 7/7-under-one-predicate\n"
        "framing overreached for $f(T)$ and EiBI).",
        fontsize=8.6, color="#555555", va="top")
ax.text(0.15, 0.20,
        "Sources: phase5/results/h2_criterion.json (rank demonstration, $f(R)$ slope); CHECKPOINT5.md H2 record (classification); gate/GATE.md (restatement).",
        fontsize=8.6, color="#555555", va="top")

fig.savefig(OUT, dpi=200)
print("saved", OUT)
