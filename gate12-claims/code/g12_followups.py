"""GATE-12 follow-ups:
(1) Alternative-frame probe on Phase 88's degenerate strategy-A sets
    (phase88/results/p881_solve.json, data only) with gate12 machinery.
(2) Brute-force C check with alpha_t large enough for FD signal and a
    linearity read at two alphas.
"""
import json
import numpy as np
import g12_le as G

W = "/home/hatch/workspace/warp-pilot/"
out = {}
s88 = json.load(open(W + "phase88/results/p881_solve.json"))
GRID57 = np.linspace(0.05, np.pi - 0.05, 57)
for key, x, lam in [("x0.5_lam0.14_L6", 0.5, 0.14), ("x0.7_lam0.09_L6", 0.7, 0.09)]:
    rec = s88[key]
    fr = G.frame_margins(x, lam, np.array(rec["p"]), rec["L"], GRID57)
    out[f"frames_phase88_A_{key}"] = fr
    print(key, {k: round(v["margin"], 6) for k, v in fr.items()}, flush=True)
json.dump(out, open(W + "gate12/results/g12_followups.json", "w"), indent=1)
print("WROTE g12_followups.json")
