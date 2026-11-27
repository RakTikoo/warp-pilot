"""Gate-54 laptop admission driver: re-runs the deciding reads of
claims (a) and (b) with the gate's own machinery (g54_lib) on the
laptop pool, from the same stored JSONs. Run from the staged dir."""
import json
import sys
import numpy as np

sys.path.insert(0, ".")
import g54_lib as G

OUT = {}


def load_primary(path):
    d = json.load(open(path))
    pvecs = np.array(d["pvecs"], dtype=float)
    avecs = np.array([[complex(*z) for z in row] for row in d["avecs"]])
    return pvecs, avecs, int(d["N"])


tg = json.load(open("p410_targets.json"))
sitesA, sitesB = tg["sitesA"], tg["sitesB"]
ptsA = [np.array(s["point"]) for s in sitesA]
thA = [np.array(s["That"]) for s in sitesA]
ptsB = [np.array(s["point"]) for s in sitesB]
thB = [np.array(s["That"]) for s in sitesB]

for lbl, prim_path, sites, pts, th in (
        ("fitA", "p410_fitA_primary.json", sitesA, ptsA, thA),
        ("fitB", "p410_fitB_primary.json", sitesB, ptsB, thB)):
    pv, av, N = load_primary(prim_path)
    f = G.Field(pv, av, 1.0)
    Rs, rhos, maxdiff = [], [], 0.0
    sec_diffs = {}
    for si, s in enumerate(sites):
        T, _, _ = f.stress(pts[si])
        Rs.append(float(np.linalg.norm(T - th[si])))
        rhos.append(float(T[0, 0]))
        nhat = pts[si] / s["r"]
        d_req = G.decompose(th[si], nhat)
        d_sup = G.decompose(T, nhat)
        if "channels" in d_req and "channels" in d_sup:
            for c in ("NEC_r", "WEC", "DEC_r", "DEC_flux", "SEC_trace", "SEC_r"):
                maxdiff = max(maxdiff, abs(d_sup["channels"][c] - d_req["channels"][c]))
            for c in ("NEC_t", "DEC_t", "SEC_t"):
                for u, v in zip(d_sup["channels"][c], d_req["channels"][c]):
                    maxdiff = max(maxdiff, abs(u - v))
            maxdiff = max(maxdiff, abs(d_sup["SEC_min_channel"] - d_req["SEC_min_channel"]))
            maxdiff = max(maxdiff, abs(d_sup["joint_min_channel"] - d_req["joint_min_channel"]))
            sec_diffs[s["key"]] = {
                "SEC_min_diff": d_sup["SEC_min_channel"] - d_req["SEC_min_channel"],
                "SEC_trace_diff": d_sup["channels"]["SEC_trace"] - d_req["channels"]["SEC_trace"]}
    rv = G.make_resid(pts, th)
    jac = G.jacobian_report(rv, G.pack(pv, av), N, 1.0, len(pts))
    OUT[lbl] = {"Rs": Rs, "maxR": max(Rs), "rhos": rhos,
                "sigma_min": jac["sigma_min"], "rank": jac["rank_tol_1e-10_rel"],
                "max_channel_diff": maxdiff, "sec_diffs": sec_diffs}
    print(lbl, "maxR", max(Rs), "sigma", jac["sigma_min"], "maxdiff", maxdiff, flush=True)

json.dump(OUT, open("g54_laptop_results.json", "w"), indent=1, default=str)
print("DONE")
