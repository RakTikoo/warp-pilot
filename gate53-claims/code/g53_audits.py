"""
g53_audits.py — Gate-53 full verdict audits on the gate's own
machinery (g53_lib.GradedBuilder + wa_auditor + audit4,
pts_1020_control, both registered spacings, the Gate-42 common
bars as registered, second path = sign agreement on the deciding
margins). Subjects and rungs (ledger entry 1086):
  y_his (c = 0 member) @ 0.1363, 0.1364   (controls; C-1 discipline)
  E2-1 @ 0.191796875                      (control)
  RW-5 @ 0.192578125, 0.195078125         (control / Arm B comparator)
  B-2 = clipped seed @ 0.192578125, 0.195078125   (claim b)
Stored bytes are hash-verified in g53_records.py before these
audits are read. Writes gate53/results/g53_audits_<subject>.json
incrementally. VM frame of record; float64 everywhere.
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate53/work")
from g53_lib import GradedBuilder, full_audit, DTYPE

WP = "/home/hatch/workspace/warp-pilot"

v408 = json.load(open(f"{WP}/phase408/results/p408_verdicts.json"))
v392 = json.load(open(f"{WP}/phase392/results/p392_verdicts.json"))
v391 = json.load(open(f"{WP}/phase391/results/p391_verdicts.json"))
rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))

y_his8 = np.asarray(rj["y_his"], dtype=DTYPE)
y_his12 = np.concatenate([np.zeros(12, dtype=DTYPE), y_his8[8:]])

PLAN = [
    ("y_his", y_his12, 12, [0.1363, 0.1364]),
    ("E2-1", np.array(v391["subjects"]["E2-1"]["y"], dtype=DTYPE), 12,
     [0.191796875]),
    ("RW-5", np.array(v392["subjects"]["RW-5"]["y"], dtype=DTYPE), 12,
     [0.192578125, 0.195078125]),
    ("B-2", np.array(v408["subjects"]["B-2"]["y"], dtype=DTYPE), 16,
     [0.192578125, 0.195078125]),
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
              "worst h0.0375:", a["legality"]["h0.0375"]["worst"],
              a["legality"]["h0.0375"]["worst_kind"],
              "sp_sign_agree:", a["second_path_sign_agreement"],
              flush=True)
    out["wall_s"] = time.time() - t0
    json.dump(out, open(f"{WP}/gate53/results/g53_audits_{name}.json", "w"),
              indent=1)
    print(name, "DONE", out["wall_s"], flush=True)
print("ALL DONE")
