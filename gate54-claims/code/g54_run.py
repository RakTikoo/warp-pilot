"""Gate-54 driver: controls C1-C3, then claim reads (a)-(d).
All deciding reads use g54_lib's field-function path on the VM.
Writes gate54/results/g54_results.json incrementally."""
import json
import sys
import numpy as np

sys.path.insert(0, "gate54/work")
import g54_lib as G

WP = "."
OUT = {}
OUTP = "gate54/results/g54_results.json"


def dump():
    json.dump(OUT, open(OUTP, "w"), indent=1, default=str)


def load_modes(path):
    bf = json.load(open(path))
    pvecs = np.array([md["pvec"] for md in bf["modes"]], dtype=float)
    avecs = np.array([[complex(*z) for z in md["a"]] for md in bf["modes"]])
    return pvecs, avecs, float(bf["m"]), int(bf["N"]), bf


def load_primary(path):
    d = json.load(open(path))
    pvecs = np.array(d["pvecs"], dtype=float)
    avecs = np.array([[complex(*z) for z in row] for row in d["avecs"]])
    return pvecs, avecs, float(d["m"]), int(d["N"]), d


def direct_residuals(pvecs, avecs, m, points, thats):
    f = G.Field(pvecs, avecs, m)
    Rs, rhos, Ls = [], [], []
    for x, th in zip(points, thats):
        T, L, _ = f.stress(x)
        Rs.append(float(np.linalg.norm(T - th)))
        rhos.append(float(T[0, 0]))
        Ls.append(L)
    return Rs, rhos, Ls


# =====================================================================
# CONTROLS
# =====================================================================
rng = np.random.default_rng(5401)
c1_max = 0.0
for trial in range(20):
    N = int(rng.integers(2, 9))
    pv = rng.normal(size=(N, 3))
    av = (rng.normal(size=(N, 2)) + 1j * rng.normal(size=(N, 2))) * 0.05
    x = rng.normal(size=3) * 5.0
    T1, _ = G.stress_field(pv, av, 1.0, x)
    T2 = G.stress_pairwise_check(pv, av, 1.0, x)
    scale = max(1e-30, float(np.max(np.abs(T1))))
    c1_max = max(c1_max, float(np.max(np.abs(T1 - T2))) / scale)

tg410 = json.load(open("phase410/work/p410_targets.json"))
sitesA = tg410["sitesA"]
sitesB = tg410["sitesB"]
ptsA = [np.array(s["point"]) for s in sitesA]
thA = [np.array(s["That"]) for s in sitesA]
ptsB = [np.array(s["point"]) for s in sitesB]
thB = [np.array(s["That"]) for s in sitesB]

pvA, avA, mA, NA, primA_file = load_primary("phase410/work/p410_fitA_primary.json")
pvB, avB, mB, NB, primB_file = load_primary("phase410/work/p410_fitB_primary.json")
for lbl, pv, av in (("fitA_primary", pvA, avA), ("fitB_primary", pvB, avB)):
    x = ptsA[0] if lbl.startswith("fitA") else ptsB[0]
    T1, _ = G.stress_field(pv, av, 1.0, x)
    T2 = G.stress_pairwise_check(pv, av, 1.0, x)
    scale = max(1e-30, float(np.max(np.abs(T1))))
    c1_max = max(c1_max, float(np.max(np.abs(T1 - T2))) / scale)

health = {}
for lbl, pv, av in (("fitA", pvA, avA), ("fitB", pvB, avB)):
    nd = max(G.mode_health(p, 1.0, a)[2] for p, a in zip(pv, av))
    dr = max(G.mode_health(p, 1.0, a)[3] for p, a in zip(pv, av))
    health[lbl] = {"max_norm_dev": nd, "max_dirac_resid": dr}
OUT["C1"] = {"max_rel_diff_field_vs_pairwise": c1_max,
             "bar": 1e-12, "pass": bool(c1_max <= 1e-12),
             "mode_health": health}
print("C1:", OUT["C1"]["max_rel_diff_field_vs_pairwise"], "pass", OUT["C1"]["pass"], flush=True)

# C2 — stored 320 winner
pv320, av320, m320, N320, bf320 = load_modes("phase320/work/p320_joint_bestfit.json")
tg320 = json.load(open("phase320/work/p320_targets.json"))
pts320 = [np.array(s["point"]) for s in tg320["sites"]]
th320 = [np.array(s["That"]) for s in tg320["sites"]]
Rs320, _, _ = direct_residuals(pv320, av320, m320, pts320, th320)
stored_Rs320 = [float(v) for v in bf320["Rs_direct"]]
rv320 = G.make_resid(pts320, th320)
jac320 = G.jacobian_report(rv320, G.pack(pv320, av320), N320, m320, len(pts320))
OUT["C2"] = {"Rs_gate": Rs320, "Rs_stored": stored_Rs320,
             "max_abs_diff": max(abs(a - b) for a, b in zip(Rs320, stored_Rs320)),
             "maxR_gate": max(Rs320),
             "sigma_min_gate": jac320["sigma_min"],
             "sigma_min_stored": 3.994300907411277e-04,
             "sigma_rel_diff": abs(jac320["sigma_min"] - 3.994300907411277e-04) / 3.994300907411277e-04,
             "rank_gate": jac320["rank_tol_1e-10_rel"]}
OUT["C2"]["pass"] = bool(OUT["C2"]["max_abs_diff"] <= 1e-13
                         and OUT["C2"]["maxR_gate"] <= 1e-12
                         and OUT["C2"]["sigma_rel_diff"] <= 1e-2)
print("C2: maxR", OUT["C2"]["maxR_gate"], "sigma", OUT["C2"]["sigma_min_gate"],
      "rel", OUT["C2"]["sigma_rel_diff"], "pass", OUT["C2"]["pass"], flush=True)

# C3 — stored 313 winner
pv313, av313, m313, N313, bf313 = load_modes("phase313/work/p313_joint_bestfit.json")
tg313 = json.load(open("phase313/work/p313_targets.json"))
pts313 = [np.array(s["point"]) for s in tg313["sites"]]
th313 = [np.array(s["That"]) for s in tg313["sites"]]
Rs313, _, _ = direct_residuals(pv313, av313, m313, pts313, th313)
OUT["C3"] = {"Rs_gate": Rs313, "maxR_gate": max(Rs313),
             "maxR_stored": 3.253339860306391e-13,
             "abs_diff": abs(max(Rs313) - 3.253339860306391e-13)}
OUT["C3"]["pass"] = bool(OUT["C3"]["abs_diff"] <= 1e-13 and OUT["C3"]["maxR_gate"] <= 1e-12)
print("C3: maxR", OUT["C3"]["maxR_gate"], "pass", OUT["C3"]["pass"], flush=True)
dump()

if not (OUT["C1"]["pass"] and OUT["C2"]["pass"] and OUT["C3"]["pass"]):
    OUT["aborted"] = "CONTROL BLOCKER — see C1/C2/C3"
    dump()
    raise SystemExit("CONTROL BLOCKER")

# =====================================================================
# (a) REPRODUCTION — primaries under the gate's machinery
# =====================================================================
res410 = json.load(open("phase410/results/p410_results.json"))
a_out = {}
for lbl, pv, av, pts, th, diagkey in (
        ("fitA", pvA, avA, ptsA, thA, "fitA_diagnostics"),
        ("fitB", pvB, avB, ptsB, thB, "fitB_diagnostics")):
    N = len(pv)
    Rs, rhos, Ls = direct_residuals(pv, av, 1.0, pts, th)
    rv = G.make_resid(pts, th)
    theta = G.pack(pv, av)
    jac = G.jacobian_report(rv, theta, N, 1.0, len(pts))
    stored_jac = res410[diagkey]["jacobian"]
    blocks_gate = {sitesA[int(i)]["key"] if lbl == "fitA" else sitesB[int(i)]["key"]: v
                   for i, v in jac["per_site_blocks"].items()}
    blocks_stored = {sitesA[int(k)]["key"] if lbl == "fitA" else sitesB[int(k)]["key"]: v
                     for k, v in stored_jac["per_site_blocks"].items()}
    entry = {"N": N,
             "Rs_gate": Rs, "Rs_stored": res410[diagkey]["direct"]["Rs"],
             "maxR_gate": max(Rs), "maxR_stored": res410[diagkey]["direct"]["maxR"],
             "L_at_sites": Ls,
             "dirac_max_residual": max(G.mode_health(p, 1.0, a)[3] for p, a in zip(pv, av)),
             "sigma_min_gate": jac["sigma_min"],
             "sigma_min_stored": stored_jac["sigma_min"],
             "sigma_rel_diff": abs(jac["sigma_min"] - stored_jac["sigma_min"]) / stored_jac["sigma_min"],
             "sigma_max_gate": jac["sigma_max"],
             "rank_gate": jac["rank_tol_1e-10_rel"],
             "rank_stored": stored_jac["rank_tol_1e-10_rel"],
             "blocks_gate": blocks_gate, "blocks_stored": blocks_stored}
    if lbl == "fitA":
        for hs in (10.0, 0.1):
            jh = G.jacobian_report(rv, theta, N, 1.0, len(pts), hscale=hs)
            entry[f"sigma_min_hscale_{hs}"] = jh["sigma_min"]
    a_out[lbl] = entry
    print(f"(a) {lbl}: maxR {max(Rs):.3e} sigma {jac['sigma_min']:.6e} "
          f"rel {entry['sigma_rel_diff']:.2e} rank {jac['rank_tol_1e-10_rel']}", flush=True)
OUT["claim_a"] = a_out
dump()

# =====================================================================
# (b) DECOMPOSITION — all eight site reads
# =====================================================================
CHAN_SCALARS = ["NEC_r", "WEC", "DEC_r", "DEC_flux", "SEC_trace", "SEC_r"]
b_out = {}
max_chan_diff = 0.0
for lbl, pv, av, sites, pts, th in (
        ("fitA", pvA, avA, sitesA, ptsA, thA),
        ("fitB", pvB, avB, sitesB, ptsB, thB)):
    f = G.Field(pv, av, 1.0)
    for si, s in enumerate(sites):
        nhat = pts[si] / s["r"]
        Tsup, _, _ = f.stress(pts[si])
        d_req = G.decompose(th[si], nhat)
        d_sup = G.decompose(Tsup, nhat)
        entry = {"r": s["r"], "segre_req": d_req["segre_type"],
                 "segre_sup": d_sup["segre_type"],
                 "R": float(np.linalg.norm(Tsup - th[si])),
                 "component_max_diff": float(np.max(np.abs(Tsup - th[si])))}
        if "channels" in d_req and "channels" in d_sup:
            diffs = {}
            for c in CHAN_SCALARS:
                diffs[c] = d_sup["channels"][c] - d_req["channels"][c]
            for c in ("NEC_t", "DEC_t", "SEC_t"):
                diffs[c] = [u - v for u, v in zip(d_sup["channels"][c], d_req["channels"][c])]
            diffs["SEC_min"] = d_sup["SEC_min_channel"] - d_req["SEC_min_channel"]
            diffs["joint_min"] = d_sup["joint_min_channel"] - d_req["joint_min_channel"]
            flat = [abs(diffs[c]) for c in CHAN_SCALARS] \
                + [abs(v) for c in ("NEC_t", "DEC_t", "SEC_t") for v in diffs[c]] \
                + [abs(diffs["SEC_min"]), abs(diffs["joint_min"])]
            entry["channel_diffs"] = diffs
            entry["max_channel_diff"] = max(flat)
            entry["req_SEC_min"] = d_req["SEC_min_channel"]
            entry["sup_SEC_min"] = d_sup["SEC_min_channel"]
            entry["req_SEC_trace"] = d_req["channels"]["SEC_trace"]
            entry["sup_SEC_trace"] = d_sup["channels"]["SEC_trace"]
            entry["req_joint_min"] = d_req["joint_min_channel"]
            entry["sup_joint_min"] = d_sup["joint_min_channel"]
            max_chan_diff = max(max_chan_diff, entry["max_channel_diff"])
        b_out[s["key"]] = entry
        print(f"(b) {s['key']}: max channel diff {entry.get('max_channel_diff')}", flush=True)
OUT["claim_b"] = {"per_site": b_out, "max_channel_diff_all": max_chan_diff}
dump()

# =====================================================================
# (c) SUPPLIER ACCOUNTING
# =====================================================================
c_out = {}
for lbl, pv, av, sites, pts, th, diagkey in (
        ("fitA", pvA, avA, sitesA, ptsA, thA, "fitA_diagnostics"),
        ("fitB", pvB, avB, sitesB, ptsB, thB, "fitB_diagnostics")):
    f = G.Field(pv, av, 1.0)
    a2 = float(np.sum(np.abs(av) ** 2))
    stored_a2 = res410[diagkey]["pricing"]["global_amplitude_scale_abs_a2"]
    av_unit = av / np.sqrt(a2)
    fu = G.Field(pv, av_unit, 1.0)
    s2 = {}
    for si, s in enumerate(sites):
        Tu, _, _ = fu.stress(pts[si])
        ks = np.array(s["kstar"])
        tkk_u = float(ks @ Tu @ ks)
        tkk_t = float(ks @ th[si] @ ks)
        s2[s["key"]] = abs(tkk_t) / abs(tkk_u) if tkk_u != 0 else None
    rhos = []
    for si in range(len(sites)):
        T, _, _ = f.stress(pts[si])
        rhos.append(float(T[0, 0]))
    c_out[lbl] = {"abs_a2_gate": a2, "abs_a2_stored": stored_a2,
                  "abs_a2_rel_diff": abs(a2 - stored_a2) / stored_a2,
                  "rhos_sup": rhos,
                  "all_positive": bool(all(r > 0 for r in rhos)),
                  "s2_implied_gate": s2,
                  "s2_implied_stored": {k: v["s2_implied"] for k, v in
                                        res410[diagkey]["pricing"]["per_site_s2_implied"].items()}}
    print(f"(c) {lbl}: |a|^2 {a2:.8f} rhos {rhos}", flush=True)
OUT["claim_c"] = c_out
dump()

# =====================================================================
# (d) CTRL-313 CLARIFICATION — sigma_min at the two solutions
# =====================================================================
g34 = json.load(open("gate34/results/g34_item3a.json"))
theta_g34 = np.array(g34["N6_winner"]["theta"])
item3c = json.load(open("gate34/results/g34_item3c.json"))
sv_stored_g34 = item3c["jacobian"]["singular_values"]
rv313 = G.make_resid(pts313, th313)
jac_g34_fwd = G.jacobian_report(rv313, theta_g34, 6, 1.0, 4, mode="forward")
jac_g34_ctr = G.jacobian_report(rv313, theta_g34, 6, 1.0, 4, mode="central")
theta_313 = G.pack(pv313, av313)
jac_313_ctr = G.jacobian_report(rv313, theta_313, 6, 1.0, 4, mode="central")
OUT["claim_d"] = {
    "gate34_theta": {
        "sigma_min_forward_gate": jac_g34_fwd["sigma_min"],
        "sigma_min_central_gate": jac_g34_ctr["sigma_min"],
        "sigma_max_forward_gate": jac_g34_fwd["sigma_max"],
        "sigma_min_stored": 0.027165249637030254,
        "sigma_max_stored": float(sv_stored_g34[0]),
        "stored_smallest_two": item3c["jacobian"]["smallest_two"],
        "rel_diff_forward": abs(jac_g34_fwd["sigma_min"] - 0.027165249637030254) / 0.027165249637030254,
        "rel_diff_central": abs(jac_g34_ctr["sigma_min"] - 0.027165249637030254) / 0.027165249637030254},
    "phase313_theta": {
        "sigma_min_central_gate": jac_313_ctr["sigma_min"],
        "sigma_min_phase410": 0.0347527502565207,
        "rel_diff_vs_410": abs(jac_313_ctr["sigma_min"] - 0.0347527502565207) / 0.0347527502565207,
        "sigma_max_central_gate": jac_313_ctr["sigma_max"],
        "rank_gate": jac_313_ctr["rank_tol_1e-10_rel"]}}
print("(d) g34 fwd", jac_g34_fwd["sigma_min"], "ctr", jac_g34_ctr["sigma_min"],
      "| 313 ctr", jac_313_ctr["sigma_min"], flush=True)
dump()
print("DONE")
