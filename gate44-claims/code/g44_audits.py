"""
g44_audits.py — Gate-44 full verdict audits on the gate's own machinery
(g44_lib.GradedBuilder + wa_auditor + audit4, pts_1020_control, both
spacings, the Gate-42 common bars). Subjects and rungs:
  y_his @ 0.1363 (claim d control)
  H3 @ 0.1859375, 0.18671875; H4/H5/H6 @ 0.18671875 (claim b)
  E1-4 @ 0.18984375, 0.19046875 (claim c ladder top + bracket)
  E2-1 @ 0.191796875, 0.1921875 (claim a)
Writes gate44/results/g44_audits_<subject>.json incrementally.
VM frame of record; float64 everywhere.
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate44/work")
from g44_lib import GradedBuilder, full_audit, DTYPE

WP = "/home/hatch/workspace/warp-pilot"

v = json.load(open(f"{WP}/phase391/results/p391_verdicts.json"))
st = json.load(open(f"{WP}/phase391/results/p391_step0.json"))
rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))

PLAN = [
    ("y_his", np.array(rj["y_his"], dtype=DTYPE), 8, [0.1363]),
    ("H3", np.array(st["subjects"]["H3"]["y"], dtype=DTYPE), 8,
     [0.1859375, 0.18671875]),
    ("H4", np.array(st["subjects"]["H4"]["y"], dtype=DTYPE), 8, [0.18671875]),
    ("H5", np.array(st["subjects"]["H5"]["y"], dtype=DTYPE), 8, [0.18671875]),
    ("H6", np.array(st["subjects"]["H6"]["y"], dtype=DTYPE), 8, [0.18671875]),
    ("E1-4", np.array(v["subjects"]["E1-4"]["y"], dtype=DTYPE), 8,
     [0.18984375, 0.19046875]),
    ("E2-1", np.array(v["subjects"]["E2-1"]["y"], dtype=DTYPE), 12,
     [0.191796875, 0.1921875]),
]

only = sys.argv[1:] or None
for name, y, nc, betas in PLAN:
    if only and name not in only:
        continue
    t0 = time.time()
    b = GradedBuilder(y, n_c=nc)
    out = {"subject": name, "n_c": nc, "chain_reads": b.chain_reads(),
           "audits": {}}
    for beta in betas:
        out["audits"][str(beta)] = full_audit(b, beta)
        a = out["audits"][str(beta)]
        print(name, beta, "legal:", a["legal_full_common_bars"],
              "worst h0.0375:", a["by_h"]["h0.0375"]["legality"]["worst"]
              if "legality" in a["by_h"]["h0.0375"] else
              a["legality"]["h0.0375"]["worst"],
              flush=True)
    out["wall_s"] = time.time() - t0
    json.dump(out, open(f"{WP}/gate44/results/g44_audits_{name}.json", "w"),
              indent=1)
    print(name, "DONE", out["wall_s"], flush=True)
print("ALL DONE")
