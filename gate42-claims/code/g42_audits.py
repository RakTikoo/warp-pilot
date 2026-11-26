"""
g42_audits.py — Gate-42 deciding audits on fresh machinery:
  y_his @ 0.1363 (claim a/e base); S1, Rank-1, S2, S3 at their legal
  rungs and failure brackets (claims c, e); the Stage-1 artefact
  champion @ 0.1363 and @ 0.17422 (claim d conviction). Also verifies
  the stored vectors' hashes and the claim-set exclusion of the
  champion. Writes gate42/results/g42_audits.json incrementally.
"""
import hashlib, json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate42/work")
from g42_lib import GradedBuilder, full_audit, DTYPE

WP = "/home/hatch/workspace/warp-pilot"
OUT = f"{WP}/gate42/results/g42_audits.json"

res = {"subjects": {}}
try:
    res = json.load(open(OUT))
except Exception:
    pass


def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()


def save():
    json.dump(res, open(OUT, "w"), indent=1)


verdicts = json.load(open(f"{WP}/phase386/results/p386_verdicts.json"))
harvest = json.load(open(f"{WP}/phase386/results/p386_pool_stage2x_harvest.json"))
rejudge = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))

y_his = np.array(rejudge["y_his"], dtype=DTYPE)
y_champ = np.array(rejudge["y_stage1"], dtype=DTYPE)
y_S1 = np.array(verdicts["subjects"]["S1"]["y"], dtype=DTYPE)
y_S2 = np.array(verdicts["subjects"]["S2"]["y"], dtype=DTYPE)
y_S3 = np.array(verdicts["subjects"]["S3"]["y"], dtype=DTYPE)
y_R1 = np.array(harvest["all_candidates"][0]["y"], dtype=DTYPE)

res["vector_hashes"] = {
    "y_his": sha(y_his), "champion_stage1": sha(y_champ),
    "S1": sha(y_S1), "S2": sha(y_S2), "S3": sha(y_S3), "rank1": sha(y_R1),
    "stored": {"S1": "84c9043eec5c6e087074394050b40d863acc1d81bd1643aa87c29fb447242068",
               "S2": "29af13762dfd4a1b0326e7b04ba4cfb2264b1ba6eee4a9461f55af6b0f8427cf",
               "S3": "87df3cfeb9199eef59dcfdb84a322a1e09482060eccfac79975b7dbbdb9b3996",
               "rank1": "d1efd42486a1e350e6aefe9a92e8b8a83a1638d48983b416721c03655d035418"},
}
res["vector_hashes"]["all_stored_match"] = all(
    res["vector_hashes"][k] == v for k, v in res["vector_hashes"]["stored"].items())
res["claim_set_subjects"] = sorted(verdicts["subjects"].keys())
res["champion_in_claim_set"] = sha(y_champ) in (
    sha(y_S1), sha(y_S2), sha(y_S3), sha(y_R1))
res["S1_rank1_max_abs_dy"] = float(np.max(np.abs(y_S1 - y_R1)))
res["S1_rank1_distinct"] = bool(np.max(np.abs(y_S1 - y_R1)) >= 0.05)
save()
print("hashes ok:", res["vector_hashes"]["all_stored_match"],
      "| champion in claim set:", res["champion_in_claim_set"],
      "| S1-R1 max|dy|:", res["S1_rank1_max_abs_dy"], flush=True)

JOBS = [
    ("y_his", y_his, [0.1363]),
    ("S1", y_S1, [0.18671875, 0.19171875]),
    ("rank1", y_R1, [0.18671875, 0.1875]),
    ("S2", y_S2, [0.16640625, 0.17140625]),
    ("S3", y_S3, [0.1515625, 0.1565625]),
    ("champion", y_champ, [0.1363, 0.17422]),
]
for name, y, betas in JOBS:
    if name in res["subjects"] and all(
            str(b) in res["subjects"][name].get("audits", {}) for b in betas):
        print("skip", name, flush=True)
        continue
    t0 = time.time()
    b = GradedBuilder(y)
    entry = res["subjects"].setdefault(name, {})
    entry["chain_reads"] = b.chain_reads()
    entry.setdefault("audits", {})
    for beta in betas:
        if str(beta) in entry["audits"]:
            continue
        ta = time.time()
        entry["audits"][str(beta)] = full_audit(b, beta)
        print(f"{name} @ {beta}: legal_full = "
              f"{entry['audits'][str(beta)]['legal_full_common_bars']} "
              f"({time.time()-ta:.0f}s)", flush=True)
        save()
    entry["build_plus_audits_s"] = time.time() - t0
    save()
print("DONE")
