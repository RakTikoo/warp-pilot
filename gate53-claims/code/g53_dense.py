"""
g53_dense.py — Gate-53 follow-up on the dense-ramp finding of
g53_thin.py (A-6's SEC dips to -1.25e-6 at r = 5.4, between the
registered set's shells). Four parts:
  1. confirmation of the dip point: wa at four spacings and
     audit4 at both registered spacings, at the exact stored
     worst point of the dense scan;
  2. a fine radial map of the SEC minimum (DIRS26) over
     r in [4.8, 6.2] step 0.02 at h = 0.009375 for A-6;
  3. the identical dense scan (radii 2.6..10.6 step 0.05 x
     DIRS26, h = 0.009375, wa) for the lineage controls RW-5,
     E2-1, y_his and for B-2, each at its legal ceiling — is
     the between-shells dip specific to A-6 or a property of
     the registered set across the lineage?
  4. the corrected Richardson extrapolation of A-6's deciding
     SEC margin from the stored ladder of g53_thin.json
     (M(h) = M0 + C h^2: M0 = M(h/2) + (M(h/2) - M(h))/3).
Writes gate53/results/g53_dense.json. VM frame of record.
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate53/work")
import g53_lib as G
from g53_lib import GradedBuilder, audit_chunked, summarise, \
    DIRS26, DTYPE
import wa_auditor as wa
import p503_lib as p503

WP = "/home/hatch/workspace/warp-pilot"
OUT = {}
thin = json.load(open(f"{WP}/gate53/results/g53_thin.json"))
v408 = json.load(open(f"{WP}/phase408/results/p408_verdicts.json"))
v392 = json.load(open(f"{WP}/phase392/results/p392_verdicts.json"))
v391 = json.load(open(f"{WP}/phase391/results/p391_verdicts.json"))
rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))

A6 = np.array(v408["subjects"]["A-6"]["y"], dtype=DTYPE)
B2 = np.array(v408["subjects"]["B-2"]["y"], dtype=DTYPE)
RW5 = np.array(v392["subjects"]["RW-5"]["y"], dtype=DTYPE)
E21 = np.array(v391["subjects"]["E2-1"]["y"], dtype=DTYPE)
y_his8 = np.asarray(rj["y_his"], dtype=DTYPE)
y_his12 = np.concatenate([np.zeros(12, dtype=DTYPE), y_his8[8:]])

# ---- 4 (first, cheap): corrected Richardson from the stored ladder ----
lad = thin["ladder"]
hs = [0.0375, 0.01875, 0.009375, 0.0046875]
secs = [lad[f"h{h}"]["per_ec"]["sec"] for h in hs]
rich = [float(secs[i + 1] + (secs[i + 1] - secs[i]) / 3.0)
        for i in range(len(hs) - 1)]
OUT["richardson_sec_limits_corrected"] = {
    "hs": hs, "secs": secs, "pairwise_limits": rich}
print("corrected Richardson limits:", rich, flush=True)

# ---- 1. confirm the dip point ----
dip_pt = np.array([thin["dense_ramp"]["all_sig"]["sec_pt"]], dtype=DTYPE)
print("dip point:", dip_pt, "r =", float(np.linalg.norm(dip_pt[0])), flush=True)
bA = GradedBuilder(A6, n_c=16)
gfA = bA.metric_factory(0.193359375)
conf = {}
for h in (0.0375, 0.01875, 0.009375, 0.0046875):
    m = wa.audit(gfA, dip_pt, h)
    conf[f"wa_h{h}"] = {
        "sec": float(m["sec"][0]), "nec": float(m["nec"][0]),
        "wec": float(m["wec"][0]), "dec": float(m["dec"][0]),
        "typeI": bool(m["typeI"][0]),
        "sampled_nec": float(m["sampled_nec"][0])}
    print("dip wa h", h, conf[f"wa_h{h}"], flush=True)
for h in (0.0375, 0.01875):
    m4 = p503.audit4(gfA, dip_pt, h)
    conf[f"audit4_h{h}"] = {
        "sec": float(m4["sec"][0]), "nec": float(m4["nec"][0]),
        "wec": float(m4["wec"][0]), "dec": float(m4["dec"][0]),
        "typeI": bool(m4["typeI"][0]),
        "sampled_nec": float(m4["sampled_nec"][0])}
    print("dip audit4 h", h, conf[f"audit4_h{h}"], flush=True)
OUT["dip_point_confirmation"] = {
    "pt": dip_pt[0].tolist(), "r": float(np.linalg.norm(dip_pt[0])),
    "reads": conf}
json.dump(OUT, open(f"{WP}/gate53/results/g53_dense.json", "w"), indent=1)

# ---- 2. fine radial map for A-6 ----
radii = np.round(np.arange(4.8, 6.2001, 0.02), 10)
fpts = np.concatenate([DIRS26 * r for r in radii]).astype(DTYPE)
frad = np.linalg.norm(fpts, axis=1)
m = audit_chunked(gfA, fpts, 0.009375, wa.audit)
prof = []
for i, r in enumerate(radii):
    sel = np.abs(frad - r) < 1e-9
    prof.append({"r": float(r), "sec_min": float(np.nanmin(m["sec"][sel])),
                 "nec_min": float(np.nanmin(m["nec"][sel])),
                 "typeI_frac": float(np.mean(m["typeI"][sel]))})
OUT["a6_radial_profile"] = prof
neg = [p for p in prof if p["sec_min"] < 0]
print("A-6 radial profile: negative-SEC radii:",
      [(p["r"], p["sec_min"]) for p in neg], flush=True)
json.dump(OUT, open(f"{WP}/gate53/results/g53_dense.json", "w"), indent=1)

# ---- 3. identical dense scans for the controls and B-2 ----
radii_d = np.arange(2.6, 10.6001, 0.05)
dpts = np.concatenate([DIRS26 * r for r in radii_d]).astype(DTYPE)
drad = np.linalg.norm(dpts, axis=1)
for name, y, nc, beta in (("RW-5", RW5, 12, 0.192578125),
                          ("E2-1", E21, 12, 0.191796875),
                          ("y_his", y_his12, 12, 0.1363),
                          ("B-2", B2, 16, 0.192578125)):
    bb = GradedBuilder(y, n_c=nc)
    gf = bb.metric_factory(beta)
    mm = audit_chunked(gf, dpts, 0.009375, wa.audit)
    ss = summarise(mm, dpts, drad)
    al = ss["all_sig"]
    OUT[f"dense_{name}"] = {
        "beta": beta, "worst": al["worst"], "worst_kind": al["worst_kind"],
        "sec_min": al["sec"], "sec_r": al["sec_r"], "sec_pt": al["sec_pt"],
        "nec_min": al["nec"], "typeI_frac": al["typeI_frac"],
        "floor_proxy": ss["floor_proxy_nonsig_median_abs_nec"]}
    print("dense", name, "SEC min", al["sec"], "@", al["sec_r"],
          "typeI", al["typeI_frac"], flush=True)
    json.dump(OUT, open(f"{WP}/gate53/results/g53_dense.json", "w"), indent=1)
print("DENSE DONE")
