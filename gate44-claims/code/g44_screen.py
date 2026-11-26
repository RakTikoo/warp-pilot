"""
g44_screen.py — Gate-44 recalibration check (claim d, second half) on
the gate's own FD screening instrument: the Phase-73 two-number score
(worst EC margin over significant Type-I points; sampled-NEC min over
significant non-Type-I points; score = min) with wa_auditor at
h = 0.0375 on the repaired-radii x 26-direction set, under the OLD core
mask [9.25, 27.27] and the EXTENDED mask [2.234381, 27.265413].
beta_crit by bisection on [0.10, 0.20] to bracket width <= 0.0008.
Subjects: y_his (c = 0) and the convicted Phase-386 Stage-1 artefact.
Registered expectations (391 C-391-3 / Gate-42 §4): extended mask —
y_his 0.136328125-class, artefact 0.120703125-class; old mask —
y_his 0.136328125-class, artefact 0.174609375-class.
Screening is a search instrument, never a verdict.
Writes gate44/results/g44_screen.json.
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate44/work")
from g44_lib import (GradedBuilder, wa, DIRS26, R1, R2, R_IN, R_OUT, DTYPE)

WP = "/home/hatch/workspace/warp-pilot"


def repaired_radii(rm):
    mid = 0.5 * (R1 + R2)
    a = np.arange(0.3 * R1, 1.35 * R2 + 0.01, 1.0)
    b = np.arange(R1 - 0.75, R1 + 1.51, 0.25)
    c = np.concatenate([np.arange(R1 - 0.25, R1 + 1.51, 0.125),
                        [R1 + 0.0625, R1 + 0.1875]])
    d = np.arange(mid - 1.5, mid + 1.51, 0.25)
    e = np.arange(R2 - 1.5, R2 + 0.76, 0.25)
    f = np.arange(R_IN - 0.5, R_IN + 2.01, 0.25)
    g = np.arange(R_OUT - 2.0, R_OUT + 0.51, 0.25)
    s = np.arange(rm - 0.5, rm + 0.51, 0.125)
    rad = np.unique(np.round(np.concatenate([a, b, c, d, e, f, g, s]), 10))
    return rad.astype(DTYPE)


def screen_score(builder, beta, pts, radp, mask):
    gf = builder.metric_factory(beta)
    m = wa.audit(gf, pts, 0.0375)
    That = m["That"]
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
    sig = mask & (scale > thr)
    ti = sig & m["typeI"]
    nt = sig & ~m["typeI"]
    parts = []
    site = {}
    if ti.any():
        w = np.inf
        for k in ("nec", "wec", "sec", "dec"):
            v = m[k][ti]
            j = int(np.nanargmin(v))
            if v[j] < w:
                w = float(v[j])
                site = {"kind": k, "r": float(radp[ti][j])}
        parts.append(w)
    if nt.any():
        j = int(np.argmin(m["sampled_nec"][nt]))
        parts.append(float(m["sampled_nec"][nt][j]))
        if parts[-1] <= min(parts[:-1] or [np.inf]):
            site = {"kind": "sampled_nec_nontypeI", "r": float(radp[nt][j])}
    return (min(parts) if parts else None), site


def beta_crit(builder, pts, radp, mask, lo=0.10, hi=0.20):
    slo, _ = screen_score(builder, lo, pts, radp, mask)
    shi, _ = screen_score(builder, hi, pts, radp, mask)
    assert slo is not None and slo > 0, slo
    assert shi is not None and shi < 0, shi
    while hi - lo > 0.0008:
        mid = 0.5 * (lo + hi)
        sm, _ = screen_score(builder, mid, pts, radp, mask)
        if sm is not None and sm > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), [lo, hi]


rj = json.load(open(f"{WP}/phase386/results/p386_rejudge_stage1.json"))
subjects = {"y_his": np.array(rj["y_his"], dtype=DTYPE),
            "artefact": np.array(rj["y_stage1"], dtype=DTYPE)}
MASKS = {"old_[9.25,27.27]": (9.25, 27.27),
         "extended_[2.234381,27.265413]": (2.234381410067394, 27.265413445973113)}
out = {}
for name, y in subjects.items():
    b = GradedBuilder(y)
    rad = repaired_radii(float(b.r_m))
    pts = np.concatenate([DIRS26 * r for r in rad]).astype(DTYPE)
    radp = np.linalg.norm(pts, axis=1)
    out[name] = {"n_radii": int(rad.size), "r_m": float(b.r_m)}
    for mname, (mlo, mhi) in MASKS.items():
        mask = (radp >= mlo) & (radp <= mhi)
        t0 = time.time()
        bc, bracket = beta_crit(b, pts, radp, mask)
        s1363, site1363 = screen_score(b, 0.1363, pts, radp, mask)
        out[name][mname] = {"n_pts_mask": int(mask.sum()),
                            "beta_crit": bc, "bracket": bracket,
                            "score_at_0.1363": s1363,
                            "binding_site_at_0.1363": site1363,
                            "wall_s": time.time() - t0}
        print(name, mname, out[name][mname], flush=True)
    json.dump(out, open(f"{WP}/gate44/results/g44_screen.json", "w"), indent=1)
print("DONE")
