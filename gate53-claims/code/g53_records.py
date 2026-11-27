"""
g53_records.py — Gate-53 stored-bytes verification and builder
calibration. Hash-verifies every audited vector against its stored
record BEFORE any audit; independently recomputes the C-408-5 LS
embedding of RW-5 onto the 16-mode basis (the registered method:
log phi on linspace(R1,R2,20001), np.linalg.lstsq of the target
basis, a/q/r_m carried unchanged) and compares hashes; verifies the
Amendment A-408-1 clip coordinate-by-coordinate; calibrates the
gate builder's chain reads against the stored records and the
c = 0 member against the closed-form step density.
Writes gate53/results/g53_records.json. VM frame of record.
"""
import hashlib, json, sys
import numpy as np
from scipy.interpolate import BSpline

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate53/work")
from g53_lib import GradedBuilder, grading_knots, analytic_step_rho, \
    R1, R2, DTYPE

WP = "/home/hatch/workspace/warp-pilot"
OUT = {"hashes": {}, "embedding": {}, "chain_calibration": {}}


def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()


v408 = json.load(open(f"{WP}/phase408/results/p408_verdicts.json"))
amd = json.load(open(f"{WP}/phase408/results/p408_amendment_A408_1.json"))
v392 = json.load(open(f"{WP}/phase392/results/p392_verdicts.json"))
v391 = json.load(open(f"{WP}/phase391/results/p391_verdicts.json"))
rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))

A6 = np.array(v408["subjects"]["A-6"]["y"], dtype=DTYPE)
B2 = np.array(v408["subjects"]["B-2"]["y"], dtype=DTYPE)
UNC = np.array(amd["unclipped_vector"], dtype=DTYPE)
CLI = np.array(amd["clipped_vector"], dtype=DTYPE)
RW5 = np.array(v392["subjects"]["RW-5"]["y"], dtype=DTYPE)
E21 = np.array(v391["subjects"]["E2-1"]["y"], dtype=DTYPE)
y_his8 = np.array(rj["y_his"], dtype=DTYPE)          # (0_8, a12, q, r_m)
y_his12 = np.concatenate([np.zeros(12, dtype=DTYPE), y_his8[8:]])
y_his16 = np.concatenate([np.zeros(16, dtype=DTYPE), y_his8[8:]])

exp = {
    "A-6": (A6, "6461827fac113c49f8f28aea04115df524446dbd44530b86f5e408e5d3c00039"),
    "B-2_clipped_seed": (B2, "d228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f"),
    "unclipped_embedding": (UNC, "a0201be16477e244d82b14e421f8de5d6fff1a2917b6cfe40441a4a03dd2d374"),
    "clipped_amendment_record": (CLI, "d228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f"),
    "RW-5": (RW5, "44719b508ba733bb257281f994f90340b1ac25b33684bbe8ac9c4da5f10535c2"),
    "E2-1": (E21, v391["subjects"]["E2-1"]["vector_sha256_float64_tobytes"]),
}
for name, (y, e) in exp.items():
    h = sha(y)
    OUT["hashes"][name] = {"sha256": h, "expected": e, "match": bool(h == e)}
    print(name, h[:12], "match:", h == e, flush=True)

# B-2's stored subject vector IS the amendment's clipped vector?
OUT["hashes"]["B-2_equals_clipped_amendment_vector"] = bool(
    np.array_equal(B2, CLI))
print("B-2 == clipped amendment vector:", np.array_equal(B2, CLI))

# ---- the clip, coordinate by coordinate ----
diff = np.where(UNC != CLI)[0]
OUT["embedding"]["clip_differing_indices"] = [int(i) for i in diff]
OUT["embedding"]["clip_unclipped_value_idx13"] = float(UNC[13])
OUT["embedding"]["clip_clipped_value_idx13"] = float(CLI[13])
OUT["embedding"]["excess_outside_box"] = float(-2.25 - UNC[13])
print("clip differing indices:", diff, "unclipped c13:", UNC[13])

# ---- independent recomputation of the LS embedding ----
xg = np.linspace(float(R1), float(R2), 20001, dtype=DTYPE)
k12, k16 = grading_knots(12), grading_knots(16)
B12 = np.array([BSpline(k12, np.eye(12)[j], 3, extrapolate=False)(xg)
                for j in range(12)])
B12 = np.nan_to_num(B12)
logphi = RW5[:12] @ B12
B16 = np.array([BSpline(k16, np.eye(16)[j], 3, extrapolate=False)(xg)
                for j in range(16)])
B16 = np.nan_to_num(B16)
c16, *_ = np.linalg.lstsq(B16.T, logphi, rcond=None)
resid = B16.T @ c16 - logphi
emb = np.concatenate([c16, RW5[12:]])
OUT["embedding"]["recomputed"] = {
    "residual_rms": float(np.sqrt(np.mean(resid ** 2))),
    "residual_max_abs": float(np.max(np.abs(resid))),
    "sha256": sha(emb),
    "matches_stored_unclipped": bool(sha(emb) == exp["unclipped_embedding"][1]),
    "max_abs_diff_vs_stored_unclipped": float(np.max(np.abs(emb - UNC))),
    "c13_recomputed": float(c16[13]),
}
print("embedding recomputed: rms", OUT["embedding"]["recomputed"]["residual_rms"],
      "max", OUT["embedding"]["recomputed"]["residual_max_abs"],
      "hash match:", OUT["embedding"]["recomputed"]["matches_stored_unclipped"],
      "maxdiff", OUT["embedding"]["recomputed"]["max_abs_diff_vs_stored_unclipped"],
      flush=True)

# ---- builder calibration: chain reads vs stored records ----
stored_chain = {
    "RW-5": (RW5, 12, {"M": 6.112885737848849, "rho_max": 3.240335264325754e-04,
                       "lambda": 0.8999655940391417, "k": 0.02367465973823105}),
    "E2-1": (E21, 12, {"rho_max": 3.2585104937459165e-04,
                       "lambda": 0.8931410086746383, "k": 0.024530591100784323}),
    "A-6": (A6, 16, v408["subjects"]["A-6"]["chain_reads"]),
    "B-2": (B2, 16, v408["subjects"]["B-2"]["chain_reads"]),
}
for name, (y, nc, stored) in stored_chain.items():
    b = GradedBuilder(y, n_c=nc)
    cr = b.chain_reads()
    row = {}
    for k in ("M", "rho_max", "lambda", "k"):
        if k in stored:
            row[k] = {"gate": cr[k], "stored": stored[k],
                      "abs_diff": abs(cr[k] - stored[k]),
                      "rel_diff": abs(cr[k] - stored[k]) / abs(stored[k])}
    OUT["chain_calibration"][name] = row
    print(name, {k: f"{row[k]['rel_diff']:.2e}" for k in row}, flush=True)

# scheme cross-check on A-6 and RW-5 (spline vs trapH chain reads)
for name, (y, nc, _) in (("A-6", stored_chain["A-6"]),
                         ("RW-5", stored_chain["RW-5"])):
    b1 = GradedBuilder(y, n_c=nc, stage_scheme="spline")
    b2 = GradedBuilder(y, n_c=nc, stage_scheme="trapH")
    d = {k: abs(b1.chain_reads()[k] - b2.chain_reads()[k])
         for k in ("rho_max", "lambda", "k")}
    OUT["chain_calibration"][name + "_scheme_xcheck_absdiff"] = d
    print(name, "scheme xcheck:", d, flush=True)

# c = 0 member vs the closed-form step density
b0 = GradedBuilder(y_his16, n_c=16)
rr = np.linspace(0.5, 29.5, 2901)
# both profiles are Box4[1_[R1,R2]] with plateau value 1 at unit
# rho0, so the max-normalised shapes are directly comparable:
sh_b = b0.rho(rr) / b0.rho(rr).max()
sh_a = analytic_step_rho(rr) / analytic_step_rho(rr).max()
OUT["chain_calibration"]["c0_step_shape_max_norm_diff"] = float(
    np.max(np.abs(sh_b - sh_a)))
OUT["chain_calibration"]["y_his16_chain"] = b0.chain_reads()
print("c0 step shape max normalised diff:",
      OUT["chain_calibration"]["c0_step_shape_max_norm_diff"], flush=True)

json.dump(OUT, open(f"{WP}/gate53/results/g53_records.json", "w"), indent=1)
print("RECORDS DONE")
