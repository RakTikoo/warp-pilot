#!/usr/bin/env python3
"""Figure for the Gate-53 claims bundle (release v1.44.0).

Reads ONLY records bundled in this folder:
  sources/g53_audits_{y_his,E2-1,RW-5,B-2}.json  (registered-set audits)
  sources/g53_thin.json                          (A-6 registered ladder)
  sources/g53_dense.json                         (dense radial sampling +
                                                  corrected Richardson limits)
and the dose-response ceiling sequence as stated in GATE53.md SS5
(bundled verbatim in this folder): 0.1363 -> 0.18671875 ->
0.18984375 -> 0.191796875 -> 0.192578125 -> 0.193359375, with
deciding-margin floor multiples from GATE53.md SS2/SS6
(y_his 109.5x, E2-1 13.4x, RW-5 106.5x, A-6 6.82x at the
registered spacing). Writes figures/g53_ladder.png.
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.dirname(HERE)
SRC = os.path.join(BUNDLE, "sources")
OUT = os.path.join(BUNDLE, "figures", "g53_ladder.png")


def load(name):
    with open(os.path.join(SRC, name)) as f:
        return json.load(f)


def registered_sec(audit, beta_key):
    return audit["audits"][beta_key]["by_h"]["h0.0375"]["summary"]["all_sig"]["sec"]


# ---- registered-set deciding SEC margins (gate reads, h = 0.0375) ----
aud_yhis = load("g53_audits_y_his.json")
aud_e21 = load("g53_audits_E2-1.json")
aud_rw5 = load("g53_audits_RW-5.json")
thin = load("g53_thin.json")
dense = load("g53_dense.json")

subjects = ["y_his", "E2-1", "RW-5", "A-6"]
betas = [0.1363, 0.191796875, 0.192578125, 0.193359375]
reg_sec = [
    registered_sec(aud_yhis, "0.1363"),
    registered_sec(aud_e21, "0.191796875"),
    registered_sec(aud_rw5, "0.192578125"),
    thin["ladder"]["h0.0375"]["per_ec"]["sec"],
]
floor_mult = [109.5, 13.4, 106.5, 6.82]  # GATE53.md SS6 / SS2

# ---- dense radial sampling (step 0.05) SEC minima ----
a6_prof = dense["a6_radial_profile"]
a6_dense_min = min(p["sec_min"] for p in a6_prof)
a6_dense_r = min(a6_prof, key=lambda p: p["sec_min"])["r"]
dense_sec = [
    dense["dense_y_his"]["sec_min"],
    dense["dense_E2-1"]["sec_min"],
    dense["dense_RW-5"]["sec_min"],
    a6_dense_min,
]
dense_r = [
    dense["dense_y_his"]["sec_r"],
    dense["dense_E2-1"]["sec_r"],
    dense["dense_RW-5"]["sec_r"],
    a6_dense_r,
]
rich = dense["richardson_sec_limits_corrected"]
a6_converged = float(np.mean(rich["pairwise_limits"]))

# ---- dose-response (GATE53.md SS5 / G53-E) ----
stages = [
    "c = 0\n(Procaccia)",
    "386",
    "391\n(interm.)",
    "391\nE2-1",
    "392\nRW-5",
    "408\nA-6",
]
ceilings = [0.1363, 0.18671875, 0.18984375, 0.191796875, 0.192578125, 0.193359375]
increments = [None, 0.05041875, 0.003125, 0.001953125, 0.00078125, 0.00078125]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 6.6))

# Panel 1: dose-response
x = np.arange(len(ceilings))
ax1.plot(x, ceilings, "o-", color="#2456a6", lw=1.8, ms=6, zorder=3)
for i, (b, inc) in enumerate(zip(ceilings, increments)):
    ax1.annotate(f"{b:.9g}".rstrip("0").rstrip(".") if b != 0.1363 else "0.1363",
                 (x[i], b), textcoords="offset points", xytext=(0, 10),
                 ha="center", fontsize=8.5)
    if inc is not None:
        ax1.annotate(f"+{inc:.8g}", (x[i] - 0.5, (ceilings[i - 1] + b) / 2),
                     ha="center", fontsize=8, color="#666666")
ax1.set_xticks(x)
ax1.set_xticklabels(stages, fontsize=8)
ax1.set_ylabel(r"graded class best $\beta$ (registered set)")
ax1.set_title("Dose-response: the graded shell ladder (G53-E)", fontsize=11)
ax1.set_ylim(0.125, 0.205)
ax1.grid(True, alpha=0.3)

# Panel 2: registered margin vs dense-continuum minimum
xs = np.arange(len(subjects))
ax2.axhline(0.0, color="black", lw=1.0, zorder=2)
ax2.plot(xs, reg_sec, "o", color="#2456a6", ms=8, zorder=4,
         label="registered-set deciding SEC margin (gate read)")
ax2.plot(xs, dense_sec, "x", color="#c0392b", ms=10, mew=2.0, zorder=4,
         label="dense radial sampling (step 0.05) SEC minimum")
reg_offsets = [(14, 6), (0, 10), (-6, -26), (0, 10)]
for i, (v, fm) in enumerate(zip(reg_sec, floor_mult)):
    ax2.annotate(f"{v:+.3g}\n({fm:g}x FD floor)", (xs[i], v),
                 textcoords="offset points", xytext=reg_offsets[i],
                 ha="center", fontsize=8, color="#2456a6")
for i, (v, r) in enumerate(zip(dense_sec, dense_r)):
    off = (0, -16) if v > 0 else (0, 11)
    ax2.annotate(f"{v:+.3g} @ r={r:.2f}", (xs[i], v),
                 textcoords="offset points", xytext=off, ha="center",
                 fontsize=8, color="#c0392b")
ax2.annotate(f"A-6 converged margin (h->0): {a6_converged:+.3g}",
             (3, a6_converged), textcoords="offset points", xytext=(-52, -14),
             ha="center", fontsize=8, color="#2456a6",
             arrowprops=dict(arrowstyle="-", color="#2456a6", lw=0.7))
ax2.plot([3], [a6_converged], "o", color="#2456a6", ms=4, zorder=4)
ax2.set_ylim(-3.5e-6, 2.2e-6)
ax2.set_xticks(xs)
ax2.set_xticklabels([f"{s}\n$\\beta$ = {b:.9g}".rstrip("0").rstrip(".")
                     if b != 0.1363 else f"{s}\n$\\beta$ = 0.1363"
                     for s, b in zip(subjects, betas)], fontsize=8.5)
ax2.set_yscale("symlog", linthresh=1e-8)
ax2.set_ylabel("SEC margin / minimum")
ax2.set_title("Registered margin vs radial continuum (riders G53-R1/R2)",
              fontsize=11, pad=12)
ax2.grid(True, alpha=0.3)
handles, labels = ax2.get_legend_handles_labels()
fig.legend(handles, labels, fontsize=8.5, loc="lower center", ncol=2,
           bbox_to_anchor=(0.5, -0.015), frameon=False)

fig.suptitle(
    "Gate-53 — graded shell: A-6 legal at beta = 0.193359375 on the registered set\n"
    "GRADED CATEGORY ONLY (G53-B): this set never contests the step-profile category —\n"
    "Procaccia's beta = 0.1363 stands there; the programme's verified best there remains beta = 0.10.\n"
    "Rider G53-R2: on denser radial sampling A-6 and E2-1 dip below zero between the registered shells;\n"
    "every ceiling in this lineage is a registered-set statement. "
    "Arm B seed of record: 'RW-5 embedded, box-clipped at c13' (G53-R3).",
    fontsize=9.5, y=1.02)

fig.tight_layout()
fig.savefig(OUT, dpi=200, bbox_inches="tight")
print("wrote", OUT)
print("registered SEC:", reg_sec)
print("dense SEC:", dense_sec, "at r =", dense_r)
print("A-6 converged margin:", a6_converged)
