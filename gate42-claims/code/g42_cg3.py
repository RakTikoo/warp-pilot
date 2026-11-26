"""
g42_cg3.py — Gate-42 re-run of the C-G3 cross-check: the point
(0, 16.635, 0) on the c = 0 member at beta = 0.1364 (and 0.1363),
wa_auditor at h = 0.0375 / 0.01875 / 0.009375 and audit4 at the same
spacings, each with the gate's exact min-null minimisation.
Writes gate42/results/g42_cg3.json.
"""
import json, sys
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate42/work")
from g42_lib import GradedBuilder, wa, p503, min_null_exact, DTYPE

WP = "/home/hatch/workspace/warp-pilot"
rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))
y_his = np.array(rj["y_his"], dtype=DTYPE)
b = GradedBuilder(y_his)
pt = np.array([[0.0, 16.635, 0.0]])
out = {"point": [0.0, 16.635, 0.0], "rows": []}
for beta in (0.1363, 0.1364):
    gf = b.metric_factory(beta)
    for name, fn in (("wa", wa.audit), ("audit4", p503.audit4)):
        for h in (0.0375, 0.01875, 0.009375):
            m = fn(gf, pt, h)
            That = m["That"][0]
            sl, sec = min_null_exact(That)
            row = {"beta": beta, "instrument": name, "h": h,
                   "typeI": bool(m["typeI"][0]),
                   "min_null_slsqp": sl, "min_null_secular": sec,
                   "sampled_nec_162": float(m["sampled_nec"][0])}
            if m["typeI"][0]:
                row["margins"] = {k: float(m[k][0])
                                  for k in ("nec", "wec", "sec", "dec")}
            out["rows"].append(row)
            print(row, flush=True)
json.dump(out, open(f"{WP}/gate42/results/g42_cg3.json", "w"), indent=1)
print("DONE")
