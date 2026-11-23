#!/usr/bin/env python3
"""Gate-8 bundle figures - generated only from the gate's own result
files in ../results/ (wa_g8_1_numbers.json, wb_g82_numbers.json,
wb_g82_israel.json). Plain-text labels (no mathtext) for portability.
Run with the programme venv python:
  ~/workspace/warp-pilot/venv/bin/python make_figures.py
NOTE (G8-1): the claim is HELD in this bundle (see ../RESULTS.md);
its figure is generated for the evidence record, not for upload.
"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")

# ---- G8-1: region margins + cavity floor ladder ----
wa = json.load(open(os.path.join(RES, "wa_g8_1_numbers.json")))
v = wa["wa_run1"]["verdict_h0.15_o4"]["regions"]
regs = ["payload", "inner_wall", "cavity", "outer_wall", "exterior"]
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.6))
vals = [v[r]["worst"] for r in regs]
cols = ["#4070a0", "#4070a0", "#b03030", "#4070a0", "#4070a0"]
ax[0].bar([r.replace("_", " ") for r in regs], vals, color=cols)
ax[0].axhline(0, color="black", lw=0.8)
ax[0].set_ylabel("worst margin, h = 0.15, 4th-order path")
ax[0].set_title("G8-1 verdict row (payload 0.0799c)\ncavity (red) at the representation floor", fontsize=10)
lad = wa["wa_run2"]["richardson_o4"]["dec_series"]
ax[1].plot([0.15, 0.075, 0.0375, 0.01875], lad, "o-")
ax[1].axhline(0, color="black", lw=0.8)
ax[1].set_xlabel("grid spacing h at the cavity site (r = 4.8)")
ax[1].set_ylabel("DEC read, 4th-order path")
ax[1].set_title("Cavity DEC ladder is non-monotone:\nno convergent negative continuum value", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g81_composed_payload.png"), dpi=200)
plt.close(fig)

# ---- G8-2: attained gain ladder + Kretschmann bounds ----
wb = json.load(open(os.path.join(RES, "wb_g82_numbers.json")))
iso = json.load(open(os.path.join(RES, "wb_g82_israel.json")))
caps = [float(k) for k in wb["mirror_rows"].keys()]
gains = [wb["mirror_rows"][k]["gain"] for k in wb["mirror_rows"].keys()]
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.6))
ax[0].plot(caps, gains, "o-", label="attained (mirror completion)")
for c, g in zip(caps, gains):
    ax[0].annotate(f"{g:.3f}", (c, g), textcoords="offset points", xytext=(0, 7), ha="center")
u = wb["uncompleted_cap0455_za1"]
ax[0].plot([u["cap"]], [u["gain"]], "x", ms=10, color="#b03030",
           label="uncompleted, cap 0.455 (not attained)")
ax[0].set_xlabel("mirror depth y_c (r0 units), z_a = 1")
ax[0].set_ylabel("fractional gain")
ax[0].set_title("G8-2 attained gain vs mirror depth\ny_c = 0.30: 0.167, u_eff = 1.200c (geometry)", fontsize=10)
ax[0].legend(fontsize=8)
kb = iso["kretschmann"]["bounds"]
ax[1].bar([str(k) for k in kb.keys()], [kb[k] for k in kb.keys()])
ax[1].set_yscale("log")
ax[1].set_xlabel("mirror depth y_c (r0 units)")
ax[1].set_ylabel("max Kretschmann along path (log scale)")
ax[1].set_title("Regularity: finite on every attained path\n(uncompleted lift diverges near y* = 0.4675)", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig_g82_attained_completion.png"), dpi=200)
plt.close(fig)

print("figures written:", sorted(f for f in os.listdir(HERE) if f.endswith(".png")))
