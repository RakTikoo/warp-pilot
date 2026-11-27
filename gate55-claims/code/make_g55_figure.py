#!/usr/bin/env python3
"""Figure generator for the Gate-55 claims bundle (release v1.46.0).

Reads ONLY the bundled records in ../sources/ (g55_results.json:
Gate-55's own deciding reads) and writes ../figures/g55_correction.png.

Left panel: the corrected target's margins at the three A sites
(Gate-55 claim_a) -- SEC_trace of T_req vs T_corr (the correction
delta zeroes the SEC deficit at A2/A3 and spends no joint surplus:
joint_min rises at both corrected sites; at A1 delta = 0).
Right panel: the supplied composite total's densities at A1/A2/A3
under BOTH definitions in the record (Gate-55 claim_c, rider
G55-R2): the Eulerian T[0,0] and the eigenvalue rho -- both
positive at every site; every quotation names which density it
quotes.
"""
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources", "g55_results.json")
OUT = os.path.join(HERE, "..", "figures", "g55_correction.png")

SITES = ["A1_joint_argmin", "A2_sec_argmin", "A3_peak"]
LABELS = ["A1", "A2", "A3"]

with open(SRC) as f:
    g = json.load(f)

ca = g["claim_a"]
sec_req = [ca[s]["sec_trace_req"] for s in SITES]
sec_corr = [ca[s]["sec_trace_corr_gate"] for s in SITES]
jm_req = [ca[s]["joint_min_req"] for s in SITES]
jm_corr = [ca[s]["joint_min_corr"] for s in SITES]

cc = g["claim_c"]
t00 = [cc[s]["T00"] for s in SITES]
rho_eig = [cc[s]["rho_eigen"] for s in SITES]
assert all(v > 0 for v in t00) and all(v > 0 for v in rho_eig)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))

ax = axes[0]
x = range(3)
w = 0.38
ax.bar([i - w / 2 for i in x], sec_req, width=w, color="#C00000",
       label="SEC_trace of T_req")
ax.bar([i + w / 2 for i in x], sec_corr, width=w, color="#305496",
       label="SEC_trace of T_corr")
ax.bar([i - w / 2 for i in x], jm_req, width=w, color="#A6A6A6",
       label="joint_min of T_req")
ax.bar([i + w / 2 for i in x], jm_corr, width=w, color="#548235",
       label="joint_min of T_corr")
ax.axhline(0.0, color="black", linewidth=0.8)
ax.set_xticks(list(x))
ax.set_xticklabels(LABELS)
ax.set_ylabel("margin (target tensor channels)")
ax.legend(fontsize=7.5, loc="lower right")
ax.set_title(
    "Gate-55 claim (a): the correction delta zeroes SEC_trace\n"
    "at A2/A3 and spends no joint surplus (joint_min rises)",
    fontsize=10,
)

ax = axes[1]
ax.bar([i - w / 2 for i in x], t00, width=w, color="#305496",
       label="Eulerian T[0,0]")
ax.bar([i + w / 2 for i in x], rho_eig, width=w, color="#548235",
       label="eigenvalue rho")
ax.set_xticks(list(x))
ax.set_xticklabels(LABELS)
ax.set_ylabel("supplier density of the supplied total tensor")
ax.legend(fontsize=8)
ax.set_title(
    "Gate-55 claim (c): the supplied total's density is positive\n"
    "at every site under BOTH definitions (rider G55-R2)",
    fontsize=10,
)

fig.suptitle(
    "Phase 420 corrected-target supply, as re-judged by Gate-55",
    fontsize=12,
)
fig.text(
    0.5,
    0.005,
    "Fences: T_corr is a construction of Phase 420 corresponding to NO existing geometry -- no corrected object\n"
    "exists or is claimed. Site mating is not extent coverage. Sourcing a corrected target is not producing a legal\n"
    "design. \"Composite\" is not necessary at site scope (rider G55-R1): the single m = 1 family reaches T_corr alone\n"
    "(max residual 1.468e-11, G55-D); the quotable claim is that the SEC correction is expressible at essentially zero\n"
    "extra price. Densities named per G55-R2. Data: bundled sources/g55_results.json only.",
    ha="center",
    fontsize=8,
)
fig.tight_layout(rect=(0, 0.10, 1, 0.94))
fig.savefig(OUT, dpi=200)
print("wrote", OUT)
print("SEC_trace req:", sec_req)
print("SEC_trace corr:", sec_corr)
print("joint_min req:", jm_req)
print("joint_min corr:", jm_corr)
print("T[0,0]:", t00)
print("eigenvalue rho:", rho_eig)
