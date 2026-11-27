#!/usr/bin/env python
"""P420 driver — W26: COMPOSITE SUPPLY OF THE CORRECTED TARGET.
Registration: phase420/work/p420_registration.md (written before
this run). Machinery: phase420/work/p420_machinery.py (Phase 410's
verbatim block + the per-mode-mass generalisation, SS2). Targets:
Phase 410's stored records (p410_targets.json). Controls first
(SS3: the delta=0 reductions CTRL-420-A/B + the delta self-check
CTRL-420-delta), then the corrected target (SS1), the fits (SS4:
C-A primary, C-B tracking, C-S context, contingency), diagnostics
and the three reads (SS5), verdict (SS7). Per-start JSONL
persistence (Phase 410 recovery pattern). Run from
~/workspace/warp-pilot/ with the programme venv python.
"""
import json, os, sys, time
import numpy as np
from scipy.optimize import least_squares

t_start = time.time()
WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/phase420/work')
import p420_machinery as M  # noqa: E402

IU = M.IU
BAR = 1e-9
OUT = {"phase": 420}
RES = f'{WP}/phase420/results/p420_results.json'


def dump():
    json.dump(OUT, open(RES, "w"), indent=1, default=str)


def avecs_from_json(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


def avecs_to_json(av):
    return [[[float(z.real), float(z.imag)] for z in row] for row in av]


# =====================================================================
# Stored Phase 410 records: targets + primaries
# =====================================================================
tg410 = json.load(open(f'{WP}/phase410/work/p410_targets.json'))
sitesA410 = tg410["sitesA"]
sitesB410 = tg410["sitesB"]
primA410 = json.load(open(f'{WP}/phase410/work/p410_fitA_primary.json'))
primB410 = json.load(open(f'{WP}/phase410/work/p410_fitB_primary.json'))

XS_A = [np.array(s["point"]) for s in sitesA410]
TH_A = [np.array(s["That"]) for s in sitesA410]
XS_B = [np.array(s["point"]) for s in sitesB410]
TH_B = [np.array(s["That"]) for s in sitesB410]
KEYS_A = [s["key"] for s in sitesA410]
KEYS_B = [s["key"] for s in sitesB410]
FROB_A = np.array([float(np.linalg.norm(t)) for t in TH_A])
FROB_B = np.array([float(np.linalg.norm(t)) for t in TH_B])

pvA410 = np.array(primA410["pvecs"]); avA410 = avecs_from_json(primA410["avecs"])
pvB410 = np.array(primB410["pvecs"]); avB410 = avecs_from_json(primB410["avecs"])

# =====================================================================
# MACHINERY CHECKS (SS2: M1-M3)
# =====================================================================
mach = {}
S_v = M.S_of(pvA410, avA410, 1.0)
S_m = M.S_of_multi(pvA410, avA410, np.full(len(pvA410), 1.0))
mach["M1_S_multi_vs_S_of_maxdiff"] = float(np.max(np.abs(S_v - S_m)))
dmax = 0.0
for pv, av, XS in ((pvA410, avA410, XS_A), (pvB410, avB410, XS_B)):
    mm = np.full(len(pv), 1.0)
    for x in XS:
        dmax = max(dmax, float(np.max(np.abs(
            M.T_direct(pv, av, 1.0, x) - M.T_direct_multi(pv, av, mm, x)))))
mach["M2_direct_multi_vs_T_direct_maxdiff"] = dmax
rng_m = np.random.default_rng(4200)
pv_mix = rng_m.normal(size=(6, 3))
av_mix = (rng_m.normal(size=(6, 2)) + 1j * rng_m.normal(size=(6, 2))) * 0.03
mm_mix = np.array([1., 1., 1., 0., 0., 0.])
rel = 0.0
for _ in range(5):
    x = rng_m.normal(size=3) * 5.0
    Tp = M.T_pairwise(M.S_of_multi(pv_mix, av_mix, mm_mix), pv_mix, x)
    Td = M.T_direct_multi(pv_mix, av_mix, mm_mix, x)
    rel = max(rel, float(np.linalg.norm(Tp - Td) / np.linalg.norm(Td)))
mach["M3_mixed_mass_direct_vs_pairwise_rel"] = rel
mach["pass"] = bool(mach["M1_S_multi_vs_S_of_maxdiff"] <= 1e-13
                    and mach["M2_direct_multi_vs_T_direct_maxdiff"] <= 1e-13
                    and mach["M3_mixed_mass_direct_vs_pairwise_rel"] <= 1e-12)
OUT["machinery_checks"] = mach
print("MACHINERY:", json.dumps(mach), flush=True)
if not mach["pass"]:
    OUT["aborted"] = "MACHINERY CHECK BLOCKER"
    dump()
    raise SystemExit("MACHINERY BLOCKER — see results json")

# =====================================================================
# CONTROLS (SS3): CTRL-420-A / CTRL-420-B — the delta=0 reductions.
# The composite machinery with family 2 empty, at Phase 410's stored
# primaries, against the UNCORRECTED targets.
# =====================================================================
def control_primary(pv, av, XS, TH, stored_Rs, stored_sigma, label):
    mm = np.full(len(pv), 1.0)
    Rs, _ = M.site_residuals_multi(pv, av, mm, XS, TH, direct=True)
    theta = M.pack_block(pv, av)
    FROBS = np.array([float(np.linalg.norm(t)) for t in TH])
    resid = M.make_resid_multi(XS, TH, FROBS, len(pv), 0, 1.0, 0.0)
    jac = M.jacobian_report_g(resid, theta, len(XS))
    rep = {"Rs": Rs, "Rs_stored": stored_Rs,
           "maxR": max(Rs), "maxR_stored": max(stored_Rs),
           "sigma_min": jac["sigma_min"],
           "sigma_min_stored": stored_sigma,
           "sigma_rel_diff": abs(jac["sigma_min"] - stored_sigma)
           / stored_sigma,
           "rank": jac["rank_tol_1e-10_rel"], "jac_shape": jac["shape"]}
    rep["pass"] = bool(all(r <= 2 * s for r, s in zip(Rs, stored_Rs))
                       and rep["maxR"] <= 1e-11
                       and rep["sigma_rel_diff"] <= 0.01)
    print(f"{label}: maxR={rep['maxR']:.3e} sigma_min={rep['sigma_min']:.6e} "
          f"(stored {stored_sigma:.6e}, rel {rep['sigma_rel_diff']:.2e}) "
          f"pass={rep['pass']}", flush=True)
    return rep


cA = control_primary(pvA410, avA410, XS_A, TH_A,
                     [float(v) for v in primA410["Rs"]],
                     0.3857618146636974, "CTRL-420-A")
OUT["CTRL420A"] = cA
cB = control_primary(pvB410, avB410, XS_B, TH_B,
                     [float(v) for v in primB410["Rs"]],
                     0.015432479500623982, "CTRL-420-B")
OUT["CTRL420B"] = cB
dump()
if not (cA["pass"] and cB["pass"]):
    OUT["aborted"] = "CONTROL BLOCKER: delta=0 reduction not reproduced"
    dump()
    raise SystemExit("CONTROL BLOCKER — see results json")

# =====================================================================
# SS1 — THE CORRECTED TARGET. delta in the site eigenframe:
# eigenvalue shifts (+D/4 on rho, +D/4 on each principal pressure),
# D = -SEC_trace where SEC_trace < 0; delta = 0 at clean sites.
# =====================================================================
def build_delta(That, nhat):
    """Returns (deltaThat, info). delta = 0 exactly if SEC_trace >= 0
    and every channel >= 0. nhat is the site's radial direction
    (Phase 410's decomposition convention)."""
    dec = M.decompose(That, nhat)
    ch = dec["channels"]
    joint_vals = [ch["NEC_r"], min(ch["NEC_t"]), ch["WEC"], ch["DEC_r"],
                  min(ch["DEC_t"]), ch["DEC_flux"]]
    info = {"sec_trace_req": ch["SEC_trace"],
            "joint_min_req": float(min(joint_vals)),
            "channels_req": {k: ch[k] for k in
                             ("rho", "p_r", "p_t", "NEC_r", "NEC_t", "WEC",
                              "DEC_r", "DEC_t", "DEC_flux", "SEC_trace")}}
    if ch["SEC_trace"] >= 0 and min(joint_vals) >= 0:
        info["delta_applied"] = False
        info["Delta"] = 0.0
        return np.zeros((4, 4)), info
    Delta = -ch["SEC_trace"]
    Mx = M.ETA @ That
    ev, V = np.linalg.eig(Mx)
    ev = ev.real; V = V.real
    tl = None
    for idx in range(4):
        v = V[:, idx]
        if float(v @ M.ETA @ v) > 1e-9 * float(v @ v):
            tl = idx
    assert tl is not None, "no timelike eigenvector"
    W = np.full(4, -Delta / 4.0)
    W[tl] = Delta / 4.0
    deltaThat = M.ETA @ (V @ np.diag(W) @ np.linalg.inv(V))
    info["delta_applied"] = True
    info["Delta"] = float(Delta)
    info["delta_frob"] = float(np.linalg.norm(deltaThat))
    return deltaThat, info


def corrected_targets(XS, TH, KEYS):
    TC, infos = [], []
    for x, T, k in zip(XS, TH, KEYS):
        d, info = build_delta(T, x / np.linalg.norm(x))
        Tc = T + d
        dec_c = M.decompose(Tc, x / np.linalg.norm(x))
        chc = dec_c["channels"]
        joint_c = [chc["NEC_r"], min(chc["NEC_t"]), chc["WEC"],
                   chc["DEC_r"], min(chc["DEC_t"]), chc["DEC_flux"]]
        info["key"] = k
        info["sec_trace_corr"] = chc["SEC_trace"]
        info["joint_min_corr"] = float(min(joint_c))
        # joint channels non-decreasing, channel by channel
        chr_ = info["channels_req"]
        pairs = [("NEC_r", chc["NEC_r"] - chr_["NEC_r"]),
                 ("WEC", chc["WEC"] - chr_["WEC"]),
                 ("DEC_r", chc["DEC_r"] - chr_["DEC_r"]),
                 ("DEC_flux", chc["DEC_flux"] - chr_["DEC_flux"])]
        for i in range(2):
            pairs.append((f"NEC_t[{i}]", chc["NEC_t"][i] - chr_["NEC_t"][i]))
            pairs.append((f"DEC_t[{i}]", chc["DEC_t"][i] - chr_["DEC_t"][i]))
        info["joint_channel_diffs"] = {k2: float(v) for k2, v in pairs}
        info["joint_channels_nondecreasing"] = bool(
            all(v >= -1e-15 for _, v in pairs))
        info["channels_corr"] = {k2: chc[k2] for k2 in
                                 ("rho", "p_r", "p_t", "NEC_r", "NEC_t",
                                  "WEC", "DEC_r", "DEC_t", "DEC_flux",
                                  "SEC_trace")}
        TC.append(Tc)
        infos.append(info)
        print(f"  delta[{k}]: applied={info['delta_applied']} "
              f"Delta={info['Delta']:.6e} |delta|_F="
              f"{info.get('delta_frob', 0.0):.3e} SEC_corr="
              f"{info['sec_trace_corr']:.3e} joint {info['joint_min_req']:.3e}"
              f" -> {info['joint_min_corr']:.3e}", flush=True)
    return TC, infos


print("Building corrected targets (SS1)...", flush=True)
TC_A, delta_info_A = corrected_targets(XS_A, TH_A, KEYS_A)
TC_B, delta_info_B = corrected_targets(XS_B, TH_B, KEYS_B)
FROB_TC_A = np.array([float(np.linalg.norm(t)) for t in TC_A])
FROB_TC_B = np.array([float(np.linalg.norm(t)) for t in TC_B])
cdelta = {"sitesA": delta_info_A, "sitesB": delta_info_B}
cdelta["pass"] = bool(
    all((abs(i["sec_trace_corr"]) <= 1e-12 if i["delta_applied"]
         else i["Delta"] == 0.0) and i["joint_channels_nondecreasing"]
        for i in delta_info_A + delta_info_B))
OUT["CTRL420delta"] = cdelta
dump()
print("CTRL-420-delta pass:", cdelta["pass"], flush=True)
if not cdelta["pass"]:
    OUT["aborted"] = "CTRL-420-delta BLOCKER: corrected target failed its self-checks"
    dump()
    raise SystemExit("CTRL-420-delta BLOCKER — see results json")

json.dump({"sitesA": [{"key": k, "point": x.tolist(), "T_req": t.tolist(),
                       "T_corr": tc.tolist()}
                      for k, x, t, tc in zip(KEYS_A, XS_A, TH_A, TC_A)],
           "sitesB": [{"key": k, "point": x.tolist(), "T_req": t.tolist(),
                       "T_corr": tc.tolist()}
                      for k, x, t, tc in zip(KEYS_B, XS_B, TH_B, TC_B)]},
          open(f'{WP}/phase420/work/p420_targets.json', "w"), indent=1)

# =====================================================================
# FIT MACHINERY (SS4) — per-start JSONL persistence (410 pattern)
# =====================================================================
rng = np.random.default_rng(4201)


def rand_modes(N, rng_, a_scale=0.03):
    pvecs = []
    for _ in range(N):
        d = rng_.normal(size=3); d /= np.linalg.norm(d)
        pvecs.append(rng_.uniform(0.05, 6.0) * d)
    avecs = (rng_.normal(size=(N, 2)) + 1j * rng_.normal(size=(N, 2))) \
        * a_scale
    return np.array(pvecs), avecs


def run_fits_multi(N1, N2, m1, m2, XS, TARGETS, FROBS, starts, max_nfev,
                   label):
    tag = label.replace(" ", "_")
    cfile = f'{WP}/phase420/work/p420_cands_{tag}.jsonl'
    done = {}
    if os.path.exists(cfile):
        for line in open(cfile):
            rec = json.loads(line)
            pv1 = np.array(rec["pvecs1"]); av1 = avecs_from_json(rec["avecs1"])
            pv2 = np.array(rec["pvecs2"]); av2 = avecs_from_json(rec["avecs2"])
            pv, av, mm = M.join_modes(pv1, av1, m1, pv2, av2, m2)
            Rs, rhos = M.site_residuals_multi(pv, av, mm, XS, TARGETS)
            done[rec["start"]] = {"start": rec["start"],
                                  "theta": M.pack2(pv1, av1, pv2, av2),
                                  "pv1": pv1, "av1": av1, "pv2": pv2,
                                  "av2": av2, "Rs": Rs, "rhos": rhos,
                                  "maxR": max(Rs),
                                  "cost_time_s": rec["cost_time_s"],
                                  "nfev": rec["nfev"]}
    resid_vec = M.make_resid_multi(XS, TARGETS, FROBS, N1, N2, m1, m2)
    cands = []
    for name, th0 in starts:
        if name in done:
            cands.append(done[name])
            print(f"  [{label}] start={name} RESUMED "
                  f"maxR={done[name]['maxR']:.3e}", flush=True)
            continue
        t0 = time.time()
        sol = least_squares(resid_vec, th0, method="trf",
                            max_nfev=max_nfev)
        pv1, av1, pv2, av2 = M.unpack2(sol.x, N1, N2)
        pv, av, mm = M.join_modes(pv1, av1, m1, pv2, av2, m2)
        Rs, rhos = M.site_residuals_multi(pv, av, mm, XS, TARGETS)
        cand = {"start": name, "theta": sol.x, "pv1": pv1, "av1": av1,
                "pv2": pv2, "av2": av2, "Rs": Rs, "rhos": rhos,
                "maxR": max(Rs), "cost_time_s": time.time() - t0,
                "nfev": int(sol.nfev)}
        cands.append(cand)
        with open(cfile, "a") as fh:
            fh.write(json.dumps(
                {"start": name, "maxR": cand["maxR"], "Rs": Rs,
                 "rhos": rhos, "nfev": cand["nfev"],
                 "cost_time_s": cand["cost_time_s"],
                 "pvecs1": pv1.tolist(), "avecs1": avecs_to_json(av1),
                 "pvecs2": pv2.tolist(), "avecs2": avecs_to_json(av2)})
                + "\n")
        print(f"  [{label}] start={name} maxR={max(Rs):.3e} "
              f"Rs={['%.2e' % r for r in Rs]} nfev={sol.nfev} "
              f"({time.time() - t0:.1f}s)", flush=True)
    cands.sort(key=lambda c: c["maxR"])
    return cands


def starts_for(N1, N2, warm1_pv, warm1_av, n_rand, rng_):
    """warm-A: family 1 = warm modes (truncated/padded), family 2 = 0.
    warm-B: family 2 small random. Plus n_rand full-random starts."""
    pv1 = np.array(warm1_pv[:N1]); av1 = np.array(warm1_av[:N1])
    while len(pv1) < N1:
        p_, a_ = rand_modes(1, rng_)
        pv1 = np.concatenate([pv1, p_]); av1 = np.concatenate([av1, a_])
    starts = []
    if N2 > 0:
        # family 2 "empty": amplitudes exactly zero (its tensor
        # contribution vanishes identically), momenta at unit
        # random directions — an exactly-zero momentum is
        # singular for a massless mode (E + m = |p|).
        z2p, _ = rand_modes(N2, rng_, a_scale=0.0)
        z2p = np.array([p / np.linalg.norm(p) for p in z2p])
        z2a = np.zeros((N2, 2), dtype=complex)
        starts.append(("warmA", M.pack2(pv1, av1, z2p, z2a)))
        p2, a2 = rand_modes(N2, rng_, a_scale=0.01)
        starts.append(("warmB", M.pack2(pv1, av1, p2, a2)))
    else:
        starts.append(("warmA", M.pack_block(pv1, av1)))
    for i in range(n_rand):
        p1, a1 = rand_modes(N1, rng_)
        if N2 > 0:
            p2, a2 = rand_modes(N2, rng_)
            starts.append((f"rand{i}", M.pack2(p1, a1, p2, a2)))
        else:
            starts.append((f"rand{i}", M.pack_block(p1, a1)))
    return starts


def arm_report(cands):
    b = cands[0]
    return {"best_maxR": b["maxR"], "best_Rs": b["Rs"],
            "best_start": b["start"],
            "all_starts": [{"start": c["start"], "maxR": c["maxR"],
                            "Rs": c["Rs"], "nfev": c["nfev"]}
                           for c in cands]}


def save_primary(cand, N1, N2, m1, m2, label):
    json.dump({"N1": N1, "N2": N2, "m1": m1, "m2": m2,
               "maxR": cand["maxR"], "Rs": cand["Rs"],
               "rhos": cand["rhos"], "start": cand["start"],
               "pvecs1": cand["pv1"].tolist(),
               "avecs1": avecs_to_json(cand["av1"]),
               "pvecs2": cand["pv2"].tolist(),
               "avecs2": avecs_to_json(cand["av2"])},
              open(f'{WP}/phase420/work/p420_{label}_primary.json', "w"),
              indent=1)


# =====================================================================
# FIT C-A (primary): {A1, A2, A3} vs T_corr
# =====================================================================
print("FIT C-A: composite vs corrected target...", flush=True)
ca_arms = {}
ca_cands = {}
for (N1, N2, nfev) in ((3, 3, 900), (6, 6, 1500)):
    st = starts_for(N1, N2, pvA410, avA410, 6, rng)
    cands = run_fits_multi(N1, N2, 1.0, 0.0, XS_A, TC_A, FROB_TC_A,
                           st, nfev, f"fitCA N{N1}_{N2}")
    ca_cands[(N1, N2)] = cands
    ca_arms[f"{N1},{N2}"] = arm_report(cands)
OUT["fitCA_arms"] = ca_arms
dump()

# =====================================================================
# FIT C-S (context): family 1 alone vs T_corr
# =====================================================================
print("FIT C-S: single family vs corrected target (context)...",
      flush=True)
cs_arms = {}
cs_best = None
for (N1, nfev, nrand) in ((6, 900, 3), (12, 1500, 4)):
    st = starts_for(N1, 0, pvA410, avA410, nrand, rng)
    cands = run_fits_multi(N1, 0, 1.0, 0.0, XS_A, TC_A, FROB_TC_A,
                           st, nfev, f"fitCS N{N1}")
    cs_arms[str(N1)] = arm_report(cands)
    if cs_best is None or cands[0]["maxR"] < cs_best["maxR"]:
        cs_best = cands[0]
OUT["fitCS_arms"] = cs_arms
dump()

# Contingency (registered SS4): m2 = 2.0 arm if C-A (6,6) and C-S stall
ca66 = ca_cands[(6, 6)][0]
contingency = None
if ca66["maxR"] > BAR and cs_best["maxR"] > BAR:
    print("CONTINGENCY ARM: family 2 at m2 = 2.0...", flush=True)
    st = starts_for(6, 6, pvA410, avA410, 6, rng)
    cands = run_fits_multi(6, 6, 1.0, 2.0, XS_A, TC_A, FROB_TC_A,
                           st, 1500, "fitCAcont N6_6_m2")
    contingency = {"arm": "6,6 m2=2.0", "report": arm_report(cands),
                   "cands": cands}
    OUT["fitCA_contingency"] = contingency["report"]
    dump()

# C-A primary selection (registered SS4)
ca_pool = [("6,6 m2=0", ca_cands[(6, 6)][0], 6, 6, 0.0),
           ("3,3 m2=0", ca_cands[(3, 3)][0], 3, 3, 0.0)]
if contingency is not None:
    ca_pool.append(("6,6 m2=2", contingency["cands"][0], 6, 6, 2.0))
matching = [p for p in ca_pool if p[1]["maxR"] <= BAR]
if any(p[0] == "6,6 m2=0" for p in matching):
    primCA_arm, primCA, pN1, pN2, pm2 = [p for p in matching
                                         if p[0] == "6,6 m2=0"][0]
elif matching:
    primCA_arm, primCA, pN1, pN2, pm2 = min(matching,
                                            key=lambda p: p[1]["maxR"])
else:
    primCA_arm, primCA, pN1, pN2, pm2 = min(ca_pool,
                                            key=lambda p: p[1]["maxR"])
save_primary(primCA, pN1, pN2, 1.0, pm2, "fitCA")
OUT["primary_fitCA"] = {"arm": primCA_arm, "N1": pN1, "N2": pN2,
                        "m2": pm2, "maxR": primCA["maxR"],
                        "start": primCA["start"]}
print(f"PRIMARY C-A: arm={primCA_arm} maxR={primCA['maxR']:.3e}",
      flush=True)
dump()

# =====================================================================
# FIT C-B (tracking): stencil vs T_req (delta = 0)
# =====================================================================
print("FIT C-B: composite tracking on the stencil...", flush=True)
order = np.argsort(-np.sum(np.abs(avB410) ** 2, axis=1))
top6 = order[:6]
cb_arms = {}
st = starts_for(6, 6, pvB410[top6], avB410[top6], 4, rng)
cands_cb = run_fits_multi(6, 6, 1.0, 0.0, XS_B, TH_B, FROB_B,
                          st, 1500, "fitCB N6_6")
cb_arms["6,6"] = arm_report(cands_cb)
primCB, cN1, cN2 = cands_cb[0], 6, 6
if primCB["maxR"] > BAR:
    print("C-B contingency arm (12,6)...", flush=True)
    # family 1 = full Fit B primary (12 modes): build theta manually
    p2z, _ = rand_modes(6, rng, a_scale=0.0)
    p2z = np.array([p / np.linalg.norm(p) for p in p2z])
    a2z = np.zeros((6, 2), dtype=complex)
    th_warm = M.pack2(pvB410, avB410, p2z, a2z)
    p2s, a2s = rand_modes(6, rng, a_scale=0.01)
    th_warmB = M.pack2(pvB410, avB410, p2s, a2s)
    starts126 = [("warmA", th_warm), ("warmB", th_warmB)]
    for i in range(4):
        p1, a1 = rand_modes(12, rng); p2, a2 = rand_modes(6, rng)
        starts126.append((f"rand{i}", M.pack2(p1, a1, p2, a2)))
    cands_cb2 = run_fits_multi(12, 6, 1.0, 0.0, XS_B, TH_B, FROB_B,
                               starts126, 1500, "fitCB N12_6")
    cb_arms["12,6"] = arm_report(cands_cb2)
    if cands_cb2[0]["maxR"] < primCB["maxR"]:
        primCB, cN1, cN2 = cands_cb2[0], 12, 6
OUT["fitCB_arms"] = cb_arms
save_primary(primCB, cN1, cN2, 1.0, 0.0, "fitCB")
OUT["primary_fitCB"] = {"N1": cN1, "N2": cN2, "maxR": primCB["maxR"],
                        "start": primCB["start"]}
print(f"PRIMARY C-B: N=({cN1},{cN2}) maxR={primCB['maxR']:.3e}",
      flush=True)
dump()

# =====================================================================
# DIAGNOSTICS + READS (SS5) at the primaries
# =====================================================================
def diagnostics_and_reads(cand, N1, N2, m2, XS, TARGETS, KEYS, label,
                          ladder=False):
    pv1, av1, pv2, av2 = cand["pv1"], cand["av1"], cand["pv2"], cand["av2"]
    pv, av, mm = M.join_modes(pv1, av1, 1.0, pv2, av2, m2)
    ns = len(XS)
    FROBS = np.array([float(np.linalg.norm(t)) for t in TARGETS])
    out = {}
    Rs_d, _ = M.site_residuals_multi(pv, av, mm, XS, TARGETS, direct=True)
    out["direct"] = {"Rs": Rs_d, "maxR": max(Rs_d)}
    out["dirac_max_residual"] = M.dirac_max_residual_multi(pv, av, mm)
    resid = M.make_resid_multi(XS, TARGETS, FROBS, N1, N2, 1.0, m2)
    theta_d = M.pack2(pv1, av1, pv2, av2)
    out["jacobian"] = M.jacobian_report_g(resid, theta_d, ns)
    out["pricing"] = {"abs_a2_family1": float(np.sum(np.abs(av1) ** 2)),
                      "abs_a2_family2": float(np.sum(np.abs(av2) ** 2))}
    # read (ii): accounting + channel tables per site
    per = {}
    mm1 = np.full(len(pv1), 1.0)
    mm2 = np.full(len(pv2), float(m2)) if len(pv2) else np.zeros(0)
    for si in range(ns):
        x = XS[si]
        nhat = x / np.linalg.norm(x)
        Tsup = M.T_direct_multi(pv, av, mm, x)
        d_tgt = M.decompose(TARGETS[si], nhat)
        d_sup = M.decompose(Tsup, nhat)
        e = {"r": float(np.linalg.norm(x)),
             "rho_sup": float(Tsup[0, 0]),
             "rho_sup_sign": "positive" if Tsup[0, 0] > 0 else
                             ("negative" if Tsup[0, 0] < 0 else "zero"),
             "req": d_tgt, "sup": d_sup,
             "R": float(np.linalg.norm(Tsup - TARGETS[si]))}
        if len(pv1):
            e["rho_family1_alone"] = float(
                M.T_direct_multi(pv1, av1, mm1, x)[0, 0])
        if len(pv2):
            e["rho_family2_alone"] = float(
                M.T_direct_multi(pv2, av2, mm2, x)[0, 0])
            e["rho_interference"] = float(
                e["rho_sup"] - e["rho_family1_alone"]
                - e["rho_family2_alone"])
        if "channels" in d_tgt and "channels" in d_sup:
            e["channel_margin_diffs"] = {
                "NEC_r": d_sup["channels"]["NEC_r"]
                         - d_tgt["channels"]["NEC_r"],
                "WEC": d_sup["channels"]["WEC"] - d_tgt["channels"]["WEC"],
                "SEC_trace": d_sup["channels"]["SEC_trace"]
                             - d_tgt["channels"]["SEC_trace"],
                "SEC_min": d_sup["SEC_min_channel"]
                           - d_tgt["SEC_min_channel"],
                "joint_min": d_sup["joint_min_channel"]
                             - d_tgt["joint_min_channel"]}
        per[KEYS[si]] = e
    out["per_site"] = per
    print(f"[{label}] direct maxR={out['direct']['maxR']:.3e} "
          f"sigma_min={out['jacobian']['sigma_min']:.4e} "
          f"rank={out['jacobian']['rank_tol_1e-10_rel']}", flush=True)
    if ladder:
        rng_p = np.random.default_rng(4202)
        pert = {}
        for eps in (1e-9, 1e-6):
            rung = []
            for draw in range(2):
                thats_p, frobs_p = [], []
                for si in range(ns):
                    U = rng_p.uniform(-1.0, 1.0, (4, 4))
                    U = 0.5 * (U + U.T)
                    thats_p.append(TARGETS[si] + eps * FROBS[si] * U)
                    frobs_p.append(float(np.linalg.norm(thats_p[-1])))
                frobs_p = np.array(frobs_p)
                resid_p = M.make_resid_multi(XS, thats_p, frobs_p,
                                             N1, N2, 1.0, m2)
                bestp = None
                starts_p = [("warm", theta_d)]
                p1, a1 = rand_modes(N1, rng_p)
                if N2 > 0:
                    p2, a2 = rand_modes(N2, rng_p)
                    starts_p.append(("fresh", M.pack2(p1, a1, p2, a2)))
                else:
                    starts_p.append(("fresh", M.pack_block(p1, a1)))
                for nm, th0 in starts_p:
                    sol = least_squares(resid_p, th0, method="trf",
                                        max_nfev=900)
                    q1, b1, q2, b2 = M.unpack2(sol.x, N1, N2)
                    qq, bb, mmm = M.join_modes(q1, b1, 1.0, q2, b2, m2)
                    Rs_p, _ = M.site_residuals_multi(qq, bb, mmm, XS,
                                                     thats_p, direct=True)
                    candp = {"start": nm, "maxR_direct": max(Rs_p),
                             "Rs_direct": Rs_p, "nfev": int(sol.nfev)}
                    if bestp is None or candp["maxR_direct"] \
                            < bestp["maxR_direct"]:
                        bestp = candp
                rung.append(bestp)
                print(f"  [{label} pert eps={eps:.0e} draw={draw}] best "
                      f"maxR={bestp['maxR_direct']:.3e} ({bestp['start']})",
                      flush=True)
            pert[str(eps)] = rung
        out["perturbation_ladder"] = pert
    return out


diagCA = diagnostics_and_reads(primCA, pN1, pN2, pm2, XS_A, TC_A,
                               KEYS_A, "fitCA", ladder=True)
OUT["fitCA_diagnostics"] = diagCA
dump()
diagCB = diagnostics_and_reads(primCB, cN1, cN2, 0.0, XS_B, TH_B,
                               KEYS_B, "fitCB", ladder=False)
OUT["fitCB_diagnostics"] = diagCB
dump()

# =====================================================================
# READ (iii) — the unmated remainder (only if C-A fails the bar)
# =====================================================================
remainder = None
if diagCA["direct"]["maxR"] > BAR:
    pv, av, mm = M.join_modes(primCA["pv1"], primCA["av1"], 1.0,
                              primCA["pv2"], primCA["av2"], pm2)
    remainder = {}
    for si in range(len(XS_A)):
        x = XS_A[si]
        Tsup = M.T_direct_multi(pv, av, mm, x)
        R = TC_A[si] - Tsup
        dT = TC_A[si] - TH_A[si]
        # SEC content of R in T_corr's eigenframe (first-order
        # eigenvalue shifts of eta.R)
        Mx = M.ETA @ TC_A[si]
        ev, V = np.linalg.eig(Mx)
        V = V.real
        shifts = np.diag(np.linalg.inv(V) @ (M.ETA @ R) @ V).real
        tl = None
        for idx in range(4):
            v = V[:, idx]
            if float(v @ M.ETA @ v) > 1e-9 * float(v @ v):
                tl = idx
        # SEC_trace functional of R (first order, eta-eigenvalue
        # convention): d(rho) + sum_i d(p_i) = shifts[tl]
        # - sum_{i != tl} shifts[i].
        sec_content = None
        if tl is not None:
            sec_content = float(shifts[tl]
                                - sum(shifts[i] for i in range(4)
                                      if i != tl))
        frob_R = float(np.linalg.norm(R))
        frob_d = float(np.linalg.norm(dT))
        if frob_d > 0:
            inner = float(np.sum(R * dT))
            coef = inner / (frob_d ** 2)
            par = abs(coef) * frob_d
            orth = float(np.sqrt(max(frob_R ** 2 - par ** 2, 0.0)))
        else:
            coef, par, orth = 0.0, 0.0, frob_R
        remainder[KEYS_A[si]] = {
            "frobenius_R": frob_R, "sec_trace_content_of_R": sec_content,
            "delta_parallel_coef": coef, "delta_parallel_norm": par,
            "orthogonal_norm": orth,
            "delta_frobenius": frob_d,
            "sec_miss_exact": float(
                diagCA["per_site"][KEYS_A[si]]["sup"]["channels"]
                ["SEC_trace"] - diagCA["per_site"][KEYS_A[si]]["req"]
                ["channels"]["SEC_trace"]),
            "joint_miss_exact": float(
                diagCA["per_site"][KEYS_A[si]]["sup"]
                ["joint_min_channel"] - diagCA["per_site"][KEYS_A[si]]
                ["req"]["joint_min_channel"])}
        print(f"  remainder[{KEYS_A[si]}]: |R|={frob_R:.3e} "
              f"SEC content={sec_content:.3e} delta-parallel={par:.3e} "
              f"orth={orth:.3e}", flush=True)
    OUT["remainder_fitCA"] = remainder
    dump()

# =====================================================================
# VERDICT (SS7, registered forms)
# =====================================================================
jacCA = diagCA["jacobian"]
ladder_ok = True
if "perturbation_ladder" in diagCA:
    ladder_ok = all(r["maxR_direct"] <= BAR
                    for rung in diagCA["perturbation_ladder"].values()
                    for r in rung)
fitCA_ok = bool(diagCA["direct"]["maxR"] <= BAR
                and jacCA["rank_tol_1e-10_rel"] == 30 and ladder_ok)
if fitCA_ok:
    verdict = "COMPOSITE SUPPLIES THE CORRECTED TARGET"
else:
    v2_chan = True
    for k in KEYS_A:
        e = diagCA["per_site"][k]
        if "channel_margin_diffs" not in e:
            v2_chan = False
            break
        d = e["channel_margin_diffs"]
        if abs(d["joint_min"]) > 1e-6:
            v2_chan = False
    sec_miss = any(abs(diagCA["per_site"][k]["channel_margin_diffs"]
                       ["SEC_min"]) > 1e-6
                   for k in KEYS_A
                   if "channel_margin_diffs" in diagCA["per_site"][k])
    v2_par = False
    if remainder is not None:
        v2_par = all(
            remainder[k]["delta_parallel_norm"] >= 0.8
            * remainder[k]["frobenius_R"]
            for k in ("A2_sec_argmin", "A3_peak")
            if remainder[k]["frobenius_R"] > 0)
    verdict = ("SUPPLIES ONLY THE UNCORRECTED TARGET"
               if (cA["pass"] and cB["pass"]
                   and ((v2_chan and sec_miss) or v2_par))
               else "DOES NOT SUPPLY")
OUT["verdict"] = {
    "form": verdict,
    "fitCA_direct_maxR": diagCA["direct"]["maxR"],
    "fitCA_ok": fitCA_ok,
    "fitCA_arm": primCA_arm, "fitCA_N1": pN1, "fitCA_N2": pN2,
    "fitCA_m2": pm2,
    "fitCA_jacobian_sigma_min": jacCA["sigma_min"],
    "fitCA_per_site_sigma_min": {KEYS_A[int(k)]: v["sigma_min"]
                                 for k, v in
                                 jacCA["per_site_blocks"].items()},
    "fitCA_rank": jacCA["rank_tol_1e-10_rel"],
    "perturbation_ladder_fitCA_all_reclose": bool(ladder_ok),
    "fitCB_direct_maxR": diagCB["direct"]["maxR"],
    "fitCB_jacobian_sigma_min": diagCB["jacobian"]["sigma_min"],
    "fitCS_best_maxR": cs_best["maxR"],
    "pricing_fitCA": diagCA["pricing"],
    "rho_sup_fitCA": {k: diagCA["per_site"][k]["rho_sup"]
                      for k in KEYS_A},
    "gate_referral": bool(verdict
                          == "COMPOSITE SUPPLIES THE CORRECTED TARGET"),
}
OUT["wall_time_s"] = time.time() - t_start
dump()
print("VERDICT:", verdict, flush=True)
print(f"wall {OUT['wall_time_s']:.0f}s", flush=True)
