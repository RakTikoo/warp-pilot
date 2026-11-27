"""
g53_thin.py — Gate-53's thin-margin scrutiny of A-6 (claim a,
ledger entry 1086 FIRST QUESTION). On the gate's own machinery:
  1. the full registered audit of A-6 @ 0.193359375 (both
     registered spacings, wa + audit4) and @ 0.195859375 (the
     bracket's failing rung);
  2. a spacing ladder FINER than the registered pair —
     h in {0.0375, 0.01875, 0.009375, 0.0046875} — wa reads of
     A-6 @ 0.193359375 on the registered set, with the FD floor
     proxy measured at every rung, the deciding SEC margin's
     h-trajectory, and a Richardson h -> 0 extrapolation
     (2nd-order instrument: M(h) = M0 + C h^2);
  3. a dense inner-ramp minimum hunt: radii 2.6..10.6 step 0.05
     x DIRS26 at h = 0.009375, wa — does any point between the
     registered shells undercut the registered-set SEC minimum?
  4. an exact-min-style check at the deciding point: the
     sampled-null NEC minimum at the r = 5.0 registered point
     recomputed with 642 Fibonacci directions (vs the
     instrument's 162).
Writes gate53/results/g53_thin.json incrementally. VM frame of
record; float64 everywhere.
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate53/work")
import g53_lib as G
from g53_lib import GradedBuilder, full_audit, audit_chunked, \
    summarise, q_reads, pts_1020_control, DIRS26, DTYPE
import wa_auditor as wa

WP = "/home/hatch/workspace/warp-pilot"
OUT = {}
v408 = json.load(open(f"{WP}/phase408/results/p408_verdicts.json"))
A6 = np.array(v408["subjects"]["A-6"]["y"], dtype=DTYPE)

t0 = time.time()
b = GradedBuilder(A6, n_c=16)
OUT["chain_reads"] = b.chain_reads()
print("builder done", time.time() - t0, flush=True)

# ---- 1. registered audits ----
for beta in (0.193359375, 0.195859375):
    a = full_audit(b, beta)
    OUT[f"audit_{beta}"] = a
    print("A-6", beta, "legal:", a["legal_full_common_bars"],
          "worst h0.0375:", a["legality"]["h0.0375"]["worst"],
          a["legality"]["h0.0375"]["worst_kind"],
          "audit4 worst h0.0375:", a["by_h"]["h0.0375"]["second_path"]["worst"],
          flush=True)
    json.dump(OUT, open(f"{WP}/gate53/results/g53_thin.json", "w"), indent=1)

# ---- 2. the finer spacing ladder at the legal rung ----
pts, radp = pts_1020_control()
gf = b.metric_factory(0.193359375)
ladder = {}
for h in (0.0375, 0.01875, 0.009375, 0.0046875):
    m = audit_chunked(gf, pts, h, wa.audit)
    s = summarise(m, pts, radp)
    al = s["all_sig"]
    ladder[f"h{h}"] = {
        "worst": al["worst"], "worst_kind": al["worst_kind"],
        "worst_r": al[al["worst_kind"] + "_r"],
        "per_ec": {k: al[k] for k in ("nec", "wec", "sec", "dec")},
        "per_ec_r": {k: al[k + "_r"] for k in ("nec", "wec", "sec", "dec")},
        "typeI_frac": al["typeI_frac"],
        "sampled_nec_min": al["sampled_nec_min"],
        "floor_proxy": s["floor_proxy_nonsig_median_abs_nec"],
        "worst_over_floor": (al["worst"] / s["floor_proxy_nonsig_median_abs_nec"]
                             if s["floor_proxy_nonsig_median_abs_nec"] else None),
        "shell_sec": s["shell"]["sec"], "shell_sec_r": s["shell"]["sec_r"],
    }
    print("ladder h", h, "SEC", al["sec"], "@", al["sec_r"],
          "floor", s["floor_proxy_nonsig_median_abs_nec"],
          "ratio", ladder[f"h{h}"]["worst_over_floor"], flush=True)
    OUT["ladder"] = ladder
    json.dump(OUT, open(f"{WP}/gate53/results/g53_thin.json", "w"), indent=1)

# Richardson extrapolation of the SEC minimum (2nd-order in h):
hs = np.array([0.0375, 0.01875, 0.009375, 0.0046875])
secs = np.array([ladder[f"h{h}"]["per_ec"]["sec"] for h in hs])
# pairwise Richardson from successive pairs (error model M + C h^2)
rich = []
for i in range(len(hs) - 1):
    m0 = secs[i] + (secs[i] - secs[i + 1]) / 3.0
    rich.append(float(m0))
OUT["richardson_sec_limits"] = rich
print("Richardson SEC limits (successive pairs):", rich, flush=True)

# ---- 3. dense inner-ramp minimum hunt ----
radii = np.arange(2.6, 10.6001, 0.05)
dpts = np.concatenate([DIRS26 * r for r in radii]).astype(DTYPE)
drad = np.linalg.norm(dpts, axis=1)
m = audit_chunked(gf, dpts, 0.009375, wa.audit)
ds = summarise(m, dpts, drad)
OUT["dense_ramp"] = {
    "radii_range": [2.6, 10.6], "dr": 0.05, "h": 0.009375,
    "n_pts": int(len(dpts)),
    "all_sig": ds["all_sig"],
    "floor_proxy": ds["floor_proxy_nonsig_median_abs_nec"],
}
print("dense ramp: worst", ds["all_sig"]["worst"], ds["all_sig"]["worst_kind"],
      "@", ds["all_sig"][ds["all_sig"]["worst_kind"] + "_r"],
      "SEC", ds["all_sig"]["sec"], "@", ds["all_sig"]["sec_r"], flush=True)
json.dump(OUT, open(f"{WP}/gate53/results/g53_thin.json", "w"), indent=1)

# ---- 4. sampled-null NEC at the deciding point, 642 directions ----
dec_pt = np.array([[-0.20001482810949123, -4.325505065138212,
                    -2.500000000000001]], dtype=DTYPE)
m1 = wa.audit(gf, dec_pt, 0.009375)
That = m1["That"]
sn162 = float(m1["sampled_nec"][0])
sn642 = float(wa.sampled_nec_min(That, n_dir=642)[0])
OUT["deciding_point"] = {
    "pt": dec_pt[0].tolist(), "r": float(np.linalg.norm(dec_pt[0])),
    "h": 0.009375, "sampled_nec_162": sn162, "sampled_nec_642": sn642,
    "margins": {k: (float(m1[k][0]) if np.ndim(m1[k]) else None)
                for k in ("nec", "wec", "sec", "dec")},
    "typeI": bool(m1["typeI"][0]),
}
print("deciding point: NEC margins", OUT["deciding_point"]["margins"],
      "sampled NEC 162/642:", sn162, sn642, flush=True)
json.dump(OUT, open(f"{WP}/gate53/results/g53_thin.json", "w"), indent=1)
print("THIN DONE", time.time() - t0)
