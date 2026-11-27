"""
p417_dense.py — Phase 417 THE DENSE READ (v2, significance-filtered
throughout; v1's classification took raw unfiltered minima and was
caught by its own cross-check against Gate-53 — the v1 record is
preserved as p417_dense_run1_unfiltered.json).

For each standing graded holder, at its standing ceiling beta:
  1. dense radial scan: radii 2.6..10.6 step 0.05 x DIRS26 (the
     registered 26 directions), wa at h = 0.009375 — the identical
     geometry to Gate-53's dense scan;
  2. significance filtering with the registered definition (a
     point is significant if max|That| > thr, thr = max(1e-9 *
     (10/R1)^2, 1e-3 * rho_peak), as in the lineage's summarise);
     all dense minima are over significant points — Gate-53's R2
     densification used the same filtered minima;
  3. radial refinement: step 0.01 over +-0.12 around the
     significant SEC argmin radius (same directions, same h, same
     thr);
  4. binding-shell ladder: at the refined worst point, wa at
     h in {0.0375, 0.01875, 0.009375, 0.0046875} and audit4 at the
     two registered spacings; Richardson pairs on SEC.
Classification: CONTINUUM-LEGAL (refined significant minima of
all four EC >= 0) or REGISTERED-SET (a dip between shells; depth
and site stated); FRAGILE if the dip depth exceeds 10x the
holder's registered margin (gate-stored, h = 0.0375), else
THIN-BUT-SCOPED. Raw unfiltered minima are recorded too (they
are ~1e-13 FD noise at the cavity fringe for the positive
holders, and are NOT the classification quantities).
Writes phase417/results/p417_dense.json incrementally.
VM frame of record.
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase417/work")
import p417_lib as P
from p417_lib import GradedBuilder, audit_chunked, summarise, DIRS26, \
    DTYPE, R1
import wa_auditor as wa
import p503_lib as p503

WP = "/home/hatch/workspace/warp-pilot"
OUT_PATH = f"{WP}/phase417/results/p417_dense.json"

v408 = json.load(open(f"{WP}/phase408/results/p408_verdicts.json"))
v392 = json.load(open(f"{WP}/phase392/results/p392_verdicts.json"))
v391 = json.load(open(f"{WP}/phase391/results/p391_verdicts.json"))
v386 = json.load(open(f"{WP}/phase386/results/p386_verdicts.json"))
rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))

HOLDERS = {
    "y_his": (np.array(rj["y_his"], dtype=DTYPE), 8, 0.1363),
    "S1": (np.array(v386["subjects"]["S1"]["y"], dtype=DTYPE), 8, 0.18671875),
    "E2-1": (np.array(v391["subjects"]["E2-1"]["y"], dtype=DTYPE), 12,
             0.191796875),
    "RW-5": (np.array(v392["subjects"]["RW-5"]["y"], dtype=DTYPE), 12,
             0.192578125),
    "B-2": (np.array(v408["subjects"]["B-2"]["y"], dtype=DTYPE), 16,
            0.192578125),
    "A-6": (np.array(v408["subjects"]["A-6"]["y"], dtype=DTYPE), 16,
            0.193359375),
}

# gate-stored registered margins (worst, h = 0.0375) — the record
# of record for the FRAGILE ratio
REG_MARGIN = {
    "y_his": 3.4041777787759174e-07,      # Gate-53 audit (SEC @ 5.0)
    "S1": 3.971324813154897e-07,          # Gate-42 / Phase 386 (SEC @ 3.75)
    "E2-1": 7.075488945987914e-08,        # Gate-53 audit (SEC @ 6.0)
    "RW-5": 6.055585116608624e-07,        # Gate-53 audit (SEC @ 3.75)
    "B-2": 6.042169269330512e-07,         # Gate-53 audit (SEC @ 3.75)
    "A-6": 3.6129700650270704e-08,        # Gate-53 ladder (SEC @ 5.0)
}

H_DENSE = 0.009375
EC = ("nec", "wec", "sec", "dec")


def scan(gf, radii, h=H_DENSE):
    """wa audit on radii x DIRS26. Returns per-point records:
    (pts, audit dict, scale per point)."""
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
    """Per-EC minima over significant points, with sites."""
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
    out = {}
    t0 = time.time()
    for name, (y, nc, beta) in HOLDERS.items():
        b = GradedBuilder(y, n_c=nc)
        gf = b.metric_factory(beta)
        # ---- 1+2. dense scan + significance threshold ----
        radii = np.round(np.arange(2.6, 10.6 + 1e-9, 0.05), 10)
        pts, mall, scale = scan(gf, radii)
        rho_peak = float(np.max(mall["That"][:, 0, 0]))
        thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
        sig = scale > thr
        radp = np.linalg.norm(pts, axis=1)
        summ = summarise(mall, pts, radp)
        dense_sig = sig_minima(pts, mall, scale, sig)
        # raw unfiltered minima (record only)
        raw = {}
        for k in EC:
            j = int(np.nanargmin(mall[k]))
            raw[k] = {"min": float(mall[k][j]),
                      "r": float(radp[j])}
        # per-radius significant SEC profile
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
        # ---- 3. refinement around the significant SEC argmin ----
        r_star = dense_sig["sec"]["r"]
        lo = max(2.6, r_star - 0.12)
        hi = min(10.6, r_star + 0.12)
        radii_f = np.round(np.arange(lo, hi + 1e-9, 0.01), 10)
        pts_f, mall_f, scale_f = scan(gf, radii_f)
        sig_f = scale_f > thr
        refined = sig_minima(pts_f, mall_f, scale_f, sig_f)
        worst_pt = np.array([refined["sec"]["pt"]], dtype=DTYPE)
        # ---- 4. binding-shell ladder at the refined worst point ----
        ladder = {}
        for h in (0.0375, 0.01875, 0.009375, 0.0046875):
            m = wa.audit(gf, worst_pt, h)
            ladder[f"wa_h{h}"] = {
                k: float(m[k][0]) for k in EC}
            ladder[f"wa_h{h}"]["typeI"] = bool(m["typeI"][0])
            ladder[f"wa_h{h}"]["sampled_nec"] = float(m["sampled_nec"][0])
        for h in (0.0375, 0.01875):
            m4 = p503.audit4(gf, worst_pt, h)
            ladder[f"audit4_h{h}"] = {
                k: float(m4[k][0]) for k in EC}
            ladder[f"audit4_h{h}"]["typeI"] = bool(m4["typeI"][0])
            ladder[f"audit4_h{h}"]["sampled_nec"] = float(
                m4["sampled_nec"][0])
        secs = [ladder[f"wa_h{h}"]["sec"]
                for h in (0.0375, 0.01875, 0.009375, 0.0046875)]
        rich = [float(secs[i + 1] + (secs[i + 1] - secs[i]) / 3.0)
                for i in range(3)]
        # ---- classification ----
        worst_ec = min(EC, key=lambda k: refined[k]["min"])
        dip = -refined[worst_ec]["min"] if refined[worst_ec]["min"] < 0 \
            else 0.0
        all_pos = all(refined[k]["min"] >= 0 for k in EC)
        cls = "CONTINUUM-LEGAL" if all_pos else "REGISTERED-SET"
        ratio = (dip / REG_MARGIN[name]) if dip > 0 else 0.0
        flag = None
        if not all_pos:
            flag = "FRAGILE" if ratio > 10.0 else "THIN-BUT-SCOPED"
        rec = {"beta": beta, "n_c": nc,
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
               "registered_margin_gate_stored": REG_MARGIN[name],
               "dip_depth": dip,
               "dip_over_registered_margin": ratio,
               "classification": cls, "flag": flag,
               "radial_profile_sec_sig": profile}
        out[name] = rec
        json.dump(out, open(OUT_PATH, "w"), indent=1)
        print(name, "dense_sig SEC", dense_sig["sec"]["min"], "@",
              dense_sig["sec"]["r"], "| refined SEC", refined["sec"]["min"],
              "@", refined["sec"]["r"], "| worst_ec", worst_ec,
              "| class", cls, flag, "| rich", rich,
              "| elapsed", time.time() - t0, flush=True)
    print("DENSE DONE", time.time() - t0)


if __name__ == "__main__":
    main()
