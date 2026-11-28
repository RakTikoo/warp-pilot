"""
g58_dense.py — Gate-58 (re-convened) THE DENSE READ on C-5, in
Phase 417's form (CHECKPOINT417 SS4, identical geometry to
Gate-53's and Gate-57's densifications):
  1. dense radial scan: radii 2.6..10.6 step 0.05 x DIRS26,
     wa at h = 0.009375, on Phase 417 machinery (p417_lib);
  2. significance filtering with the registered definition
     (max|That| > thr, thr = max(1e-9*(10/R1)^2, 1e-3*rho_peak));
     all dense minima over significant points;
  3. radial refinement step 0.01 over +-0.12 around the
     significant SEC argmin radius;
  4. binding-shell ladder at the refined worst point: wa at
     h in {0.0375, 0.01875, 0.009375, 0.0046875}, audit4 at both
     registered spacings, Richardson pairs on SEC.
Classification (417's form): CONTINUUM-LEGAL (refined
significant minima of all four EC >= 0) or REGISTERED-SET
(a dip between shells; depth and site stated); FRAGILE if the
dip depth exceeds 10x the holder's registered margin
(C-5: +3.740426000178131e-07, Phase 432's home record),
else THIN-BUT-SCOPED.
C-5 at its Phase-432 ceiling beta = 0.194921875, vector
hash-verified against the phase record before any read.
Writes gate58/results/g58_dense.json. VM frame of record.
"""
import json, sys, time, hashlib
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase417/work")
import p417_lib as P
from p417_lib import GradedBuilder, audit_chunked, summarise, DIRS26, \
    DTYPE, R1
import wa_auditor as wa
import p503_lib as p503

WP = "/home/hatch/workspace/warp-pilot"
OUT_PATH = f"{WP}/gate58/results/g58_dense.json"

v432 = json.load(open(f"{WP}/phase432/results/p432_verdicts.json"))
y = np.array(v432["subjects"]["C-5"]["y"], dtype=DTYPE)
sha = hashlib.sha256(y.tobytes()).hexdigest()
assert sha == "cb56c30165ccb7b5dd651f24fdcfa55add2a860016c051336fe83bd9faa86930", sha
BETA = 0.194921875
REG_MARGIN = 3.740426000178131e-07   # C-5 registered worst, h=0.0375

H_DENSE = 0.009375
EC = ("nec", "wec", "sec", "dec")


def scan(gf, radii, h=H_DENSE):
    allpts = []
    parts = []
    for r in radii:
        pts = (DIRS26 * r).astype(DTYPE)
        allpts.append(pts)
        parts.append(audit_chunked(gf, pts, h, wa.audit))
    mall = {k: np.concatenate([m[k] for m in parts], axis=0)
            for k in parts[0]}
    pts = np.concatenate(allpts)
    scale = np.max(np.abs(mall["That"]), axis=(1, 2))
    return pts, mall, scale


def sig_minima(pts, mall, scale, sig):
    out = {}
    for k in EC:
        v = np.where(sig, mall[k], np.inf)
        j = int(np.argmin(v))
        out[k] = {"min": float(v[j]), "r": float(np.linalg.norm(pts[j])),
                  "pt": [float(x) for x in pts[j]]}
    out["typeI_frac_sig"] = float(np.mean(mall["typeI"][sig])) \
        if sig.sum() else None
    out["n_sig"] = int(sig.sum())
    return out


def main():
    t0 = time.time()
    b = GradedBuilder(y, n_c=16)
    gf = b.metric_factory(BETA)
    radii = np.round(np.arange(2.6, 10.6 + 1e-9, 0.05), 10)
    pts, mall, scale = scan(gf, radii)
    rho_peak = float(np.max(mall["That"][:, 0, 0]))
    thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
    sig = scale > thr
    radp = np.linalg.norm(pts, axis=1)
    summ = summarise(mall, pts, radp)
    dense_sig = sig_minima(pts, mall, scale, sig)
    raw = {}
    for k in EC:
        j = int(np.nanargmin(mall[k]))
        raw[k] = {"min": float(mall[k][j]), "r": float(radp[j])}
    profile = []
    for i, r in enumerate(radii):
        sl = slice(i * 26, (i + 1) * 26)
        s = sig[sl]
        if s.sum():
            profile.append({
                "r": float(r),
                "sec_min_sig": float(np.min(mall["sec"][sl][s])),
                "nec_min_sig": float(np.min(mall["nec"][sl][s])),
                "n_sig": int(s.sum())})
        else:
            profile.append({"r": float(r), "sec_min_sig": None,
                            "nec_min_sig": None, "n_sig": 0})
    print("dense scan done", time.time() - t0, flush=True)
    r_star = dense_sig["sec"]["r"]
    lo = max(2.6, r_star - 0.12)
    hi = min(10.6, r_star + 0.12)
    radii_f = np.round(np.arange(lo, hi + 1e-9, 0.01), 10)
    pts_f, mall_f, scale_f = scan(gf, radii_f)
    sig_f = scale_f > thr
    refined = sig_minima(pts_f, mall_f, scale_f, sig_f)
    worst_pt = np.array([refined["sec"]["pt"]], dtype=DTYPE)
    ladder = {}
    for h in (0.0375, 0.01875, 0.009375, 0.0046875):
        m = wa.audit(gf, worst_pt, h)
        ladder[f"wa_h{h}"] = {k: float(m[k][0]) for k in EC}
        ladder[f"wa_h{h}"]["typeI"] = bool(m["typeI"][0])
        ladder[f"wa_h{h}"]["sampled_nec"] = float(m["sampled_nec"][0])
    for h in (0.0375, 0.01875):
        m4 = p503.audit4(gf, worst_pt, h)
        ladder[f"audit4_h{h}"] = {k: float(m4[k][0]) for k in EC}
        ladder[f"audit4_h{h}"]["typeI"] = bool(m4["typeI"][0])
        ladder[f"audit4_h{h}"]["sampled_nec"] = float(m4["sampled_nec"][0])
    secs = [ladder[f"wa_h{h}"]["sec"]
            for h in (0.0375, 0.01875, 0.009375, 0.0046875)]
    rich = [float(secs[i + 1] + (secs[i + 1] - secs[i]) / 3.0)
            for i in range(3)]
    worst_ec = min(EC, key=lambda k: refined[k]["min"])
    dip = -refined[worst_ec]["min"] if refined[worst_ec]["min"] < 0 else 0.0
    all_pos = all(refined[k]["min"] >= 0 for k in EC)
    cls = "CONTINUUM-LEGAL" if all_pos else "REGISTERED-SET"
    ratio = (dip / REG_MARGIN) if dip > 0 else 0.0
    flag = None
    if not all_pos:
        flag = "FRAGILE" if ratio > 10.0 else "THIN-BUT-SCOPED"
    rec = {"subject": "C-5", "sha256": sha, "beta": BETA, "n_c": 16,
           "thr": float(thr), "rho_peak_dense": rho_peak,
           "dense_step0.05_sig": dense_sig,
           "dense_step0.05_raw_unfiltered": raw,
           "dense_all_sig": summ["all_sig"],
           "dense_floor_proxy": summ["floor_proxy_nonsig_median_abs_nec"],
           "refined_window": {"lo": float(lo), "hi": float(hi),
                              "step": 0.01},
           "refined_sig": refined,
           "worst_point": refined["sec"]["pt"],
           "worst_r": refined["sec"]["r"],
           "worst_ec": worst_ec,
           "ladder": ladder,
           "richardson_sec_limits": rich,
           "registered_margin_phase432": REG_MARGIN,
           "dip_depth": dip,
           "dip_over_registered_margin": ratio,
           "classification": cls, "flag": flag,
           "radial_profile_sec_sig": profile,
           "elapsed_s": time.time() - t0}
    json.dump(rec, open(OUT_PATH, "w"), indent=1)
    print("C-5 dense_sig SEC", dense_sig["sec"]["min"], "@",
          dense_sig["sec"]["r"], "| refined SEC", refined["sec"]["min"],
          "@", refined["sec"]["r"], "| worst_ec", worst_ec,
          "| class", cls, flag, "| rich", rich,
          "| elapsed", time.time() - t0, flush=True)
    print("DENSE DONE", time.time() - t0)


if __name__ == "__main__":
    main()
