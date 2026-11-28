"""
g58_audit.py — Gate-58 (re-convened) independent re-derivation of
Phase 432's claim set, on Phase 417 machinery (p417_lib: the
panel-Lagrange organisation; imports nothing from phase432/work).
Instruments are the registered pair (gate6/wa_auditor,
phase50/p503_lib.audit4) — the shared instruments of every verdict
in the lineage; the GEOMETRY path (builder) is independent of the
phase's p432_lib16 evaluator, as the charge requires.

Reads:
  CONTROL  A-6 at 0.193359375 on this machinery vs Phase 417's
           stored controls record (machinery control, run first).
  C432-1   c=0 (y_his) at 0.1363 on gate machinery vs Gate-42's
           stored worst (+3.404178e-7 SEC @ r=5.0) and the phase's
           C-432-1 record.
  CHAIN    chain calibration for C-5 and B-4 (gate builder vs
           phase-stored chain reads).
  B-4      full registered audit at 0.194140625 (C-432-2 form:
           the standing best reproduces) + q reads.
  C-5/C-1/C-4  full registered audits at 0.194921875 + q reads.
  BRACKET  C-5 at 0.197421875 (the stored failing rung) and at
           the bracket interior 0.196171875 (gate's own addition).
Writes gate58/results/g58_audit.json incrementally.
VM frame of record (programme venv).
"""
import json, sys, time, hashlib
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase417/work")
import p417_lib as P
from p417_lib import GradedBuilder, full_audit, audit_chunked, \
    summarise, pts_1020_control, DIRS26, DIRS162, DTYPE, R1
import wa_auditor as wa

WP = "/home/hatch/workspace/warp-pilot"
OUT_PATH = f"{WP}/gate58/results/g58_audit.json"

v432 = json.load(open(f"{WP}/phase432/results/p432_verdicts.json"))
c432 = json.load(open(f"{WP}/phase432/results/p432_controls.json"))
v416 = json.load(open(f"{WP}/phase416/results/p416_verdicts.json"))
v408 = json.load(open(f"{WP}/phase408/results/p408_verdicts.json"))
c417 = json.load(open(f"{WP}/phase417/results/p417_controls.json"))
g57 = json.load(open(f"{WP}/gate57/results/g57_audit.json"))


def vhash(y):
    return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()


def q_reads(builder, beta, h=0.0375):
    """Flux-ratio reads from the gate's own wa audit tensor
    (Gate-57's g57_audit.q_reads form, verbatim logic)."""
    pts, radp = pts_1020_control()
    gf = builder.metric_factory(beta)
    m = audit_chunked(gf, pts, h, wa.audit)
    That = m["That"]
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
    sig = scale > thr
    T00 = That[:, 0, 0]; T0i = That[:, 0, 1:]; Tij = That[:, 1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij, DIRS162, DIRS162)
    vals = T00[:, None] + 2.0 * (T0i @ DIRS162.T) + quad
    jmin = np.argmin(vals, axis=1)
    nmin = DIRS162[jmin]
    T0n = np.einsum('ij,ij->i', T0i, nmin)
    Tnn = np.einsum('ij,ijk,ik->i', nmin, Tij, nmin)
    denom = T00 + Tnn
    q = np.where(denom > 0, 2.0 * np.abs(T0n) / np.maximum(denom, 1e-300),
                 np.inf)
    qs = q[sig]
    jq = int(np.argmax(qs))
    idxs = np.where(sig)[0]
    sn = m["sampled_nec"][sig]
    jw = int(np.argmin(sn))
    return {"h": h, "thr": float(thr), "n_sig": int(sig.sum()),
            "q_max": float(qs[jq]), "q_max_r": float(radp[idxs[jq]]),
            "q_max_typeI": bool(m["typeI"][idxs[jq]]),
            "n_q_gt_1_sig": int((qs > 1).sum()),
            "n_nonTypeI_sig": int((~m["typeI"][sig]).sum()),
            "q_at_worst_sampled_nec": float(qs[jw]),
            "q_at_worst_sampled_nec_r": float(radp[idxs[jw]])}


def slim(aud):
    out = {"beta": aud["beta"], "legal_full_common_bars":
           aud["legal_full_common_bars"],
           "second_path_sign_agreement": aud["second_path_sign_agreement"]}
    for hk in ("h0.0375", "h0.01875"):
        leg = aud["legality"][hk]
        sp = aud["by_h"][hk]["second_path"]
        out[hk] = {"worst": leg["worst"], "worst_kind": leg["worst_kind"],
                   "worst_r": leg["worst_r"], "per_ec": leg["per_ec"],
                   "per_ec_r": leg["per_ec_r"],
                   "typeI_frac": leg["typeI_frac"],
                   "floor": leg["floor"],
                   "worst_over_floor": leg["worst_over_floor"],
                   "shell_sampled_nec_min": leg["core_sampled_nec_min"],
                   "audit4_worst": sp["worst"],
                   "audit4_per_ec": {k: sp[k] for k in
                                     ("nec", "wec", "sec", "dec")},
                   "audit4_typeI_frac_sig": sp["typeI_frac_sig"]}
    return out


out = {}
t0 = time.time()

# ---------- CONTROL: A-6 on gate machinery vs Phase 417's record ----
y_a6 = np.array(v408["subjects"]["A-6"]["y"], dtype=DTYPE)
assert vhash(y_a6) == "6461827fac113c49f8f28aea04115df524446dbd44530b86f5e408e5d3c00039"
aud_a6 = full_audit(GradedBuilder(y_a6, n_c=16), 0.193359375)
ref = c417["A-6"]["audit"]["legality"]
ctl = {}
for hk in ("h0.0375", "h0.01875"):
    ctl[hk] = {"worst_mine": aud_a6["legality"][hk]["worst"],
               "worst_p417": ref[hk]["worst"],
               "absdiff": abs(aud_a6["legality"][hk]["worst"]
                              - ref[hk]["worst"])}
out["control_A6"] = {"audit": slim(aud_a6), "vs_p417_controls": ctl,
                     "legal_full": aud_a6["legal_full_common_bars"]}
json.dump(out, open(OUT_PATH, "w"), indent=1)
print("CONTROL A-6", ctl, "legal", aud_a6["legal_full_common_bars"],
      "elapsed", time.time() - t0, flush=True)

# ---------- C-432-1 form: c=0 at 0.1363 on gate machinery ----
y_c0 = np.array(c432["C-432-1"]["y"], dtype=DTYPE)
assert vhash(y_c0) == c432["C-432-1"]["vector_sha256_float64_tobytes"]
aud_c0 = full_audit(GradedBuilder(y_c0, n_c=16), 0.1363)
out["C432_1_c0"] = {
    "audit": slim(aud_c0),
    "gate42_worst_ref": 3.404178e-07,
    "phase_C432_1_worst": c432["C-432-1"]["deciding_h0.0375"]["worst_h0.0375"],
    "worst_ratio_to_gate42":
        aud_c0["legality"]["h0.0375"]["worst"] / 3.404178e-07,
    "chain_gate": GradedBuilder(y_c0, n_c=16).chain_reads(),
    "chain_phase": {k: c432["C-432-1"]["chain_reads"][k]
                    for k in ("M", "rho_max", "lambda", "k")}}
json.dump(out, open(OUT_PATH, "w"), indent=1)
print("C432-1 c=0 legal", aud_c0["legal_full_common_bars"],
      "worst", aud_c0["legality"]["h0.0375"]["worst"],
      "ratio to G42", out["C432_1_c0"]["worst_ratio_to_gate42"],
      "elapsed", time.time() - t0, flush=True)

# ---------- Chain calibration: C-5 and B-4 ----
chain = {}
for name, vdict in (("C-5", v432), ("B-4", v416)):
    y = np.array(vdict["subjects"][name]["y"], dtype=DTYPE)
    assert vhash(y) == vdict["subjects"][name][
        "vector_sha256_float64_tobytes"], name
    g = GradedBuilder(y, n_c=16).chain_reads()
    s = vdict["subjects"][name]["chain_reads"]
    chain[name] = {k: {"gate": g[k], "phase_stored": s[k],
                       "rel_diff": abs(g[k] - s[k]) / abs(s[k])}
                   for k in ("M", "rho_max", "lambda", "k")}
out["chain_calibration"] = chain
json.dump(out, open(OUT_PATH, "w"), indent=1)
print("CHAIN", {n: max(chain[n][k]["rel_diff"] for k in chain[n])
                for n in chain}, "elapsed", time.time() - t0, flush=True)

# ---------- B-4: C-432-2 reproduction on gate machinery ----
y_b4 = np.array(v416["subjects"]["B-4"]["y"], dtype=DTYPE)
assert vhash(y_b4) == "7a3fa7d58e8e526f5dbff8bac7c51a1a37a03b4cbd1a0ceecfc16a63793bcb42"
b_b4 = GradedBuilder(y_b4, n_c=16)
aud_b4 = full_audit(b_b4, 0.194140625)
out["B-4"] = {"sha256": vhash(y_b4), "audit": slim(aud_b4),
              "q_h0.0375": q_reads(b_b4, 0.194140625, 0.0375),
              "q_h0.01875": q_reads(b_b4, 0.194140625, 0.01875),
              "phase_C432_2": {
                  "worst": c432["C-432-2"]["legal_rung"]["audit"]
                  ["summaries"]["h0.0375"]["all_sig"]["worst"],
                  "measured_FD_floor_h0.0375":
                  c432["C-432-2"]["measured_FD_floor_h0.0375"],
                  "margin_multiple":
                  c432["C-432-2"]["B-4_margin_multiple_of_FD_floor_h0.0375"]},
              "gate57_gate_read_worst_h0.0375":
              g57["B-4"]["audit"]["h0.0375"]["worst"],
              "gate57_gate_read_floor_h0.0375":
              g57["B-4"]["audit"]["h0.0375"]["floor"]}
json.dump(out, open(OUT_PATH, "w"), indent=1)
print("B-4 legal", aud_b4["legal_full_common_bars"],
      "worst h.0375", aud_b4["legality"]["h0.0375"]["worst"],
      "floor", aud_b4["legality"]["h0.0375"]["floor"],
      "q_max", out["B-4"]["q_h0.0375"]["q_max"],
      "elapsed", time.time() - t0, flush=True)

# ---------- The rung subjects at 0.194921875 ----
for name in ("C-5", "C-1", "C-4"):
    y = np.array(v432["subjects"][name]["y"], dtype=DTYPE)
    sha = vhash(y)
    assert sha == v432["subjects"][name][
        "vector_sha256_float64_tobytes"], name
    b = GradedBuilder(y, n_c=16)
    aud = full_audit(b, 0.194921875)
    rec = {"sha256": sha, "audit": slim(aud),
           "q_h0.0375": q_reads(b, 0.194921875, 0.0375)}
    if name == "C-5":
        rec["q_h0.01875"] = q_reads(b, 0.194921875, 0.01875)
        rec["phase_stored"] = {
            "worst": v432["subjects"]["C-5"]["anatomy_at_ceiling"]
            ["binding"]["h0.0375"]["worst"],
            "floor_proxy": v432["subjects"]["C-5"]["anatomy_at_ceiling"]
            ["binding"]["h0.0375"]["floor_proxy"],
            "shell_sampled_nec_min": v432["subjects"]["C-5"]
            ["anatomy_at_ceiling"]["binding"]["h0.0375"]
            ["shell_sampled_nec_min"]}
    out[name] = rec
    json.dump(out, open(OUT_PATH, "w"), indent=1)
    print(name, sha[:8], "legal", aud["legal_full_common_bars"],
          "worst h.0375", aud["legality"]["h0.0375"]["worst"],
          "floor", aud["legality"]["h0.0375"]["floor"],
          "q_max", rec["q_h0.0375"]["q_max"],
          "elapsed", time.time() - t0, flush=True)

# ---------- Bracket: C-5 failing rung + interior ----
y_c5 = np.array(v432["subjects"]["C-5"]["y"], dtype=DTYPE)
b_c5 = GradedBuilder(y_c5, n_c=16)
for beta in (0.197421875, 0.196171875):
    aud = full_audit(b_c5, beta)
    out[f"bracket_{beta}"] = slim(aud)
    json.dump(out, open(OUT_PATH, "w"), indent=1)
    print("BRACKET", beta, "legal", aud["legal_full_common_bars"],
          "worst h.0375", aud["legality"]["h0.0375"]["worst"],
          aud["legality"]["h0.0375"]["worst_kind"],
          "@", aud["legality"]["h0.0375"]["worst_r"],
          "elapsed", time.time() - t0, flush=True)

print("AUDIT DONE", time.time() - t0)
