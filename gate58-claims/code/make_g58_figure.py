"""
make_g58_figure.py — the Gate-58 bundle figure. Reads only
the bundled records in ../sources/ (p417_dense.json,
g57_dense.json, g58_dense.json, p432_verdicts.json) plus the
ladder's dose-response sequence as stated in GATE58_REPORT
G58-R4, and writes ../figures/g58_ladder.png.

Panel A: the graded ladder — best beta per push, C-5 last.
Panel B: registered vs dense (refined) SEC margins for the
scope-table holders, C-5 last: the two registered-set-only
holders (E2-1, A-6) dip below zero on densification;
RW-5, B-4 and C-5 do not — and the dense margin thins
along the last three continuum-legal holders.
"""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources")
FIG = os.path.join(HERE, "..", "figures", "g58_ladder.png")

d417 = json.load(open(os.path.join(SRC, "p417_dense.json")))
d57 = json.load(open(os.path.join(SRC, "g57_dense.json")))
d58 = json.load(open(os.path.join(SRC, "g58_dense.json")))
v432 = json.load(open(os.path.join(SRC, "p432_verdicts.json")))

ladder = [("step\n(y_his)", 0.1363), ("386\n(S1)", 0.18671875),
          ("391 E1", 0.18984375), ("391 E2\n(E2-1)", 0.191796875),
          ("392\n(RW-5)", 0.192578125), ("408\n(A-6)", 0.193359375),
          ("416\n(B-4)", 0.194140625), ("432\n(C-5)", 0.194921875)]

holders = ["y_his", "S1", "E2-1", "RW-5", "A-6"]
reg = [d417[h]["registered_margin_gate_stored"] for h in holders]
dense = [d417[h]["refined_sig"]["sec"]["min"] for h in holders]
labels = ["y_his\n0.1363", "S1\n0.18671875", "E2-1\n0.191796875",
          "RW-5\n0.192578125", "A-6\n0.193359375"]
reg.append(5.803597080787196e-07)          # B-4 registered (416 home)
dense.append(d57["refined_sig"]["sec"]["min"])
labels.append("B-4\n0.194140625")
reg.append(v432["subjects"]["C-5"]["anatomy_at_ceiling"]["binding"]
           ["h0.0375"]["worst"])           # C-5 registered (432 home)
dense.append(d58["refined_sig"]["sec"]["min"])
labels.append("C-5\n0.194921875")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 4.4))
xs = np.arange(len(ladder))
ax1.step(xs, [b for _, b in ladder], where="mid", color="#2456a6",
         lw=2)
ax1.plot(xs, [b for _, b in ladder], "o", color="#2456a6", ms=5)
for i in range(1, len(ladder)):
    d = ladder[i][1] - ladder[i - 1][1]
    ax1.annotate(f"+{d:.5f}" if d < 0.01 else f"+{d:.4f}",
                 (xs[i], ladder[i][1]), textcoords="offset points",
                 xytext=(0, 8), ha="center", fontsize=7.5)
ax1.set_xticks(xs, [n for n, _ in ladder], fontsize=8)
ax1.set_ylabel(r"graded category best $\beta$")
ax1.set_title("The graded ladder — dose–response (Gate-58)", fontsize=10)
ax1.grid(alpha=0.3)
ax1.annotate("last four increments each exactly\n+0.00078125, one rung per finished push",
             (0.98, 0.06), xycoords="axes fraction", ha="right",
             fontsize=8, style="italic")

x = np.arange(len(labels))
w = 0.38
ax2.bar(x - w / 2, np.array(reg) * 1e6, w, label="registered margin",
        color="#2456a6")
ax2.bar(x + w / 2, np.array(dense) * 1e6, w, label="dense SEC (refined)",
        color="#c05621")
ax2.axhline(0, color="black", lw=0.8)
ax2.set_xticks(x, labels, fontsize=7.5)
ax2.set_ylabel(r"SEC margin ($\times 10^{-6}$)")
ax2.set_title("Registered vs dense margins — C-5 stays legal, thinner",
              fontsize=10)
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3, axis="y")
ax2.annotate("E2-1 and A-6 dip on densification (REGISTERED-SET);\n"
             "dense margins of the continuum-legal holders thin:\n"
             "RW-5 +2.86, B-4 +2.450, C-5 +1.432 (×10⁻⁷)",
             (0.02, 0.94), xycoords="axes fraction", va="top",
             fontsize=8, style="italic")
fig.tight_layout()
fig.savefig(FIG, dpi=200)
print("wrote", FIG)
