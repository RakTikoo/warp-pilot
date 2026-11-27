#!/usr/bin/env python
"""P420 independent checker (Phase 410 pattern: a separate path).

Re-derives from stored records, NOT from the driver's functions:
 (1) the corrected targets — this file carries its OWN
     implementation of the registered SS1 delta construction,
     applied to Phase 410's stored targets, compared against
     the driver's stored corrected targets;
 (2) the delta=0 controls (residuals + sigma_min spot checks);
 (3) the C-A primary's direct residuals vs the corrected
     targets, its FD-Jacobian sigma_min, its per-family
     pricing, and the supplied tensor's four-condition status
     at the sites;
 (4) the C-B primary's direct residuals vs the uncorrected
     stencil;
 (5) the verdict, re-derived from the registered SS7 forms
     (reading the completed-ladder record for the ladder leg).
Writes phase420/results/p420_check_results.json.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/phase420/work')
import p420_machinery as M  # noqa: E402

IU = M.IU
BAR = 1e-9
chk = {}


def avecs_from_json(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


def joint_channels(dec):
    ch = dec["channels"]
    return [ch["NEC_r"], min(ch["NEC_t"]), ch["WEC"], ch["DEC_r"],
            min(ch["DEC_t"]), ch["DEC_flux"]]


# ---------------------------------------------------------------------
# (1) Independent delta construction (registered SS1, re-implemented)
# ---------------------------------------------------------------------
def my_delta(That, nhat):
    dec = M.decompose(That, nhat)
    sec = dec["channels"]["SEC_trace"]
    if sec >= 0 and min(joint_channels(dec)) >= 0:
        return np.zeros((4, 4)), 0.0
    Delta = -sec
    w, V = np.linalg.eig(M.ETA @ That)
    V = V.real
    tl = max(range(4),
             key=lambda i: float(V[:, i] @ M.ETA @ V[:, i])
             / float(V[:, i] @ V[:, i]))
    shift = np.array([Delta / 4.0 if i == tl else -Delta / 4.0
                      for i in range(4)])
    return M.ETA @ V @ np.diag(shift) @ np.linalg.inv(V), Delta


tg410 = json.load(open(f'{WP}/phase410/work/p410_targets.json'))
tg420 = json.load(open(f'{WP}/phase420/work/p420_targets.json'))
res = json.load(open(f'{WP}/phase420/results/p420_results.json'))

maxdiff = 0.0
delta_info = {}
for group in ("sitesA", "sitesB"):
    for s410, s420 in zip(tg410[group], tg420[group]):
        T = np.array(s410["That"])
        x = np.array(s410["point"])
        d, Delta = my_delta(T, x / np.linalg.norm(x))
        Tc = T + d
        maxdiff = max(maxdiff, float(np.max(np.abs(
            Tc - np.array(s420["T_corr"])))))
        dec = M.decompose(Tc, x / np.linalg.norm(x))
        delta_info[s410["key"]] = {
            "Delta": Delta,
            "sec_trace_corr": dec["channels"]["SEC_trace"],
            "joint_min_corr": float(min(joint_channels(dec)))}
chk["delta_rebuild"] = {"max_abs_diff_vs_driver_targets": maxdiff,
                        "per_site": delta_info,
                        "pass": bool(maxdiff <= 1e-13)}
print("delta rebuild max diff:", maxdiff, flush=True)

# ---------------------------------------------------------------------
# (2) Controls re-check
# ---------------------------------------------------------------------
primA410 = json.load(open(f'{WP}/phase410/work/p410_fitA_primary.json'))
primB410 = json.load(open(f'{WP}/phase410/work/p410_fitB_primary.json'))


def sigma_spot(pv, av, XS, TH):
    FROBS = np.array([float(np.linalg.norm(t)) for t in TH])
    resid = M.make_resid_multi(XS, TH, FROBS, len(pv), 0, 1.0, 0.0)
    theta = M.pack_block(pv, av)
    J = M.fd_jacobian_g(resid, theta)
    return float(np.linalg.svd(J, compute_uv=False)[-1])


XS_A = [np.array(s["point"]) for s in tg410["sitesA"]]
TH_A = [np.array(s["That"]) for s in tg410["sitesA"]]
XS_B = [np.array(s["point"]) for s in tg410["sitesB"]]
TH_B = [np.array(s["That"]) for s in tg410["sitesB"]]
ctl = {}
for name, prim, XS, TH, sig_stored in (
        ("A", primA410, XS_A, TH_A, 0.3857618146636974),
        ("B", primB410, XS_B, TH_B, 0.015432479500623982)):
    pv = np.array(prim["pvecs"]); av = avecs_from_json(prim["avecs"])
    Rs, _ = M.site_residuals_multi(pv, av, np.full(len(pv), 1.0),
                                   XS, TH, direct=True)
    sig = sigma_spot(pv, av, XS, TH)
    ctl[name] = {"Rs": Rs, "Rs_stored": prim["Rs"],
                 "sigma_min": sig, "sigma_stored": sig_stored,
                 "sigma_rel_diff": abs(sig - sig_stored) / sig_stored,
                 "pass": bool(all(r <= 2 * s for r, s in zip(Rs, prim["Rs"]))
                              and max(Rs) <= 1e-11
                              and abs(sig - sig_stored) / sig_stored <= 0.01)}
    print(f"control {name}: maxR={max(Rs):.3e} sigma={sig:.6e} "
          f"pass={ctl[name]['pass']}", flush=True)
chk["controls"] = ctl

# ---------------------------------------------------------------------
# (3) C-A primary: residuals, sigma_min, pricing, four-condition read
# ---------------------------------------------------------------------
TC_A = [np.array(s["T_corr"]) for s in tg420["sitesA"]]
primCA = json.load(open(f'{WP}/phase420/work/p420_fitCA_primary.json'))
pv, av, mm = M.join_modes(np.array(primCA["pvecs1"]),
                          avecs_from_json(primCA["avecs1"]),
                          primCA["m1"],
                          np.array(primCA["pvecs2"]),
                          avecs_from_json(primCA["avecs2"]),
                          primCA["m2"])
RsA, _ = M.site_residuals_multi(pv, av, mm, XS_A, TC_A, direct=True)
FROBS_TC = np.array([float(np.linalg.norm(t)) for t in TC_A])
residCA = M.make_resid_multi(XS_A, TC_A, FROBS_TC, primCA["N1"],
                             primCA["N2"], primCA["m1"], primCA["m2"])
thetaCA = M.pack2(np.array(primCA["pvecs1"]),
                  avecs_from_json(primCA["avecs1"]),
                  np.array(primCA["pvecs2"]),
                  avecs_from_json(primCA["avecs2"]))
jacCA = M.jacobian_report_g(residCA, thetaCA, len(XS_A))
per_site = {}
for si, s in enumerate(tg410["sitesA"]):
    x = XS_A[si]
    Tsup = M.T_direct_multi(pv, av, mm, x)
    dsup = M.decompose(Tsup, x / np.linalg.norm(x))
    per_site[s["key"]] = {
        "rho_sup": float(Tsup[0, 0]),
        "joint_min_sup": dsup["joint_min_channel"],
        "sec_min_sup": dsup["SEC_min_channel"],
        "sec_trace_sup": dsup["channels"]["SEC_trace"],
        "four_condition_clean": bool(
            dsup["joint_min_channel"] >= -1e-9
            and dsup["SEC_min_channel"] >= -1e-9)}
ca = {"direct_Rs": RsA, "direct_maxR": max(RsA),
      "sigma_min": jacCA["sigma_min"],
      "rank": jacCA["rank_tol_1e-10_rel"],
      "abs_a2_family1": float(np.sum(
          np.abs(avecs_from_json(primCA["avecs1"])) ** 2)),
      "abs_a2_family2": float(np.sum(
          np.abs(avecs_from_json(primCA["avecs2"])) ** 2)),
      "per_site": per_site,
      "dirac_max_residual": M.dirac_max_residual_multi(pv, av, mm)}
chk["fitCA_primary"] = ca
print(f"C-A primary: maxR={ca['direct_maxR']:.3e} "
      f"sigma_min={ca['sigma_min']:.4e} rank={ca['rank']}", flush=True)

# ---------------------------------------------------------------------
# (4) C-B primary vs the uncorrected stencil
# ---------------------------------------------------------------------
primCB = json.load(open(f'{WP}/phase420/work/p420_fitCB_primary.json'))
pvB, avB, mmB = M.join_modes(np.array(primCB["pvecs1"]),
                             avecs_from_json(primCB["avecs1"]),
                             primCB["m1"],
                             np.array(primCB["pvecs2"]),
                             avecs_from_json(primCB["avecs2"]),
                             primCB["m2"])
RsB, rhosB = M.site_residuals_multi(pvB, avB, mmB, XS_B, TH_B,
                                    direct=True)
chk["fitCB_primary"] = {"direct_Rs": RsB, "direct_maxR": max(RsB),
                        "rhos": rhosB,
                        "all_rho_positive": bool(all(r > 0 for r in rhosB))}
print(f"C-B primary: maxR={max(RsB):.3e}", flush=True)

# ---------------------------------------------------------------------
# (5) Verdict re-derivation (SS7 forms; completed ladder per Amdt 3)
# ---------------------------------------------------------------------
lad = json.load(open(f'{WP}/phase420/results/'
                     'p420_ladder_completed.json'))
ladder_ok = bool(lad["all_reclose"])
fitCA_ok = bool(ca["direct_maxR"] <= BAR
                and ca["rank"] == 30 and ladder_ok)
if fitCA_ok:
    verdict = "COMPOSITE SUPPLIES THE CORRECTED TARGET"
else:
    verdict = "NOT VERDICT 1 (see driver record)"
agree = bool(verdict == res["verdict"]["form"])
chk["verdict"] = {"rederived": verdict,
                  "driver_record": res["verdict"]["form"],
                  "agree": agree,
                  "ladder_completed_all_reclose": ladder_ok,
                  "driver_sigma_min": res["verdict"]
                  ["fitCA_jacobian_sigma_min"],
                  "sigma_min_agrees": bool(
                      abs(ca["sigma_min"] - res["verdict"]
                          ["fitCA_jacobian_sigma_min"])
                      / res["verdict"]["fitCA_jacobian_sigma_min"]
                      <= 0.01)}
chk["ALL_PASS"] = bool(chk["delta_rebuild"]["pass"]
                       and ctl["A"]["pass"] and ctl["B"]["pass"]
                       and agree and chk["verdict"]["sigma_min_agrees"])
json.dump(chk, open(f'{WP}/phase420/results/p420_check_results.json',
                    "w"), indent=1, default=str)
print("CHECK ALL_PASS:", chk["ALL_PASS"], "| verdict agree:", agree,
      flush=True)
