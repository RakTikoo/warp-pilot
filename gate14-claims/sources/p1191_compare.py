#!/usr/bin/env python
"""P119-1 comparison + results assembly. Run AFTER the fresh rows existed
(/tmp/p1191_part_*.json, merged to /tmp/p1191_fresh_merged.json) and after
results/p1191_run_record.md was drafted. Opens the Phase 108 target
(p1085_results.json) and P72-2 stored reads, applies the registered
replication standard, and writes results/p1191_results.json.
"""
import json

FRESH = "/tmp/p1191_fresh_merged.json"
TARGET = "/home/hatch/workspace/warp-pilot/phase108/results/p1085_results.json"
P72 = "/home/hatch/workspace/warp-pilot/phase72/results/p722_results.json"
ASYM = "/tmp/p1191_asym.json"
OUT = "/home/hatch/workspace/warp-pilot/phase119/results/p1191_results.json"

fresh = {(r["N"], r["m"], r["r"]): r for r in json.load(open(FRESH))["rows"]}
target = {(r["N"], r["m"], r["r"]): r for r in json.load(open(TARGET))["rows"]}
p72 = {(p["r"],): p for p in json.load(open(P72))["points"]}
asym = json.load(open(ASYM))

def rel(a, b):
    if a is None and b is None:
        return 0.0
    if a is None or b is None:
        return None
    return abs(a - b) / max(abs(b), 1e-300)

comp_rows = []
all_pass = True
for k in sorted(target):
    f, t = fresh[k], target[k]
    d = {}
    ok = True
    for q in ("E_out", "E_prep_marg", "E_net_B"):
        d[q] = rel(f[q], t[q]); ok &= d[q] <= 1e-6
    for q in ("tau0", "tau_marg", "R_tau0", "R_tau_marg"):
        fv, tv = f[q], t[q]
        if q.startswith("R") and fv in (0.0, None) and tv in (0.0, None):
            d[q] = 0.0; continue
        dd = rel(fv, tv)
        if dd is None:
            d[q] = None; ok &= (fv is None and tv is None); continue
        d[q] = dd; ok &= dd <= 1e-4
    all_pass &= ok
    comp_rows.append({"N": k[0], "m": k[1], "r": k[2], "replicates": bool(ok),
                      "rel_diffs": d})

# controls from the fresh rows
c1 = []
for r_ in (0.5, 1.0, 2.0):
    f = fresh[(2, 1, r_)]; p = p72[(r_,)]
    c1.append({"r": r_,
               "dE_out_rel": rel(f["E_out"], p["EB"]),
               "dE_prep_rel": rel(f["E_prep_marg"], p["E_prep_marg"]),
               "dE_net_rel": rel(f["E_net_B"], p["E_net_B_sector"]),
               "dtau0_abs": abs(f["tau0"] - p["tau_pulse"])})
controls = {
    "C1": {"rows": c1,
           "pass": all(x["dE_out_rel"] <= 1e-9 and x["dE_prep_rel"] <= 1e-9
                       and x["dE_net_rel"] <= 1e-9 and x["dtau0_abs"] <= 1e-6 for x in c1)},
    "C2": {"max_abs_E_ground": max(abs(r["E_ground_eig"]) for r in fresh.values()),
           "min_ground_overlap_eq3": min(r["ground_overlap_eq3"] for r in fresh.values()),
           "pass": max(abs(r["E_ground_eig"]) for r in fresh.values()) <= 1e-12
                   and min(r["ground_overlap_eq3"] for r in fresh.values()) >= 1 - 1e-10},
    "C3": {"tau_marg_2_05_fresh": fresh[(2, 1, 0.5)]["tau_marg"],
           "tau_marg_2_05_target": target[(2, 1, 0.5)]["tau_marg"],
           "diff_abs": abs(fresh[(2, 1, 0.5)]["tau_marg"] - target[(2, 1, 0.5)]["tau_marg"]),
           "pass": abs(fresh[(2, 1, 0.5)]["tau_marg"] - target[(2, 1, 0.5)]["tau_marg"]) <= 1e-6},
    "internal_cross_checks": {
        "max_abs_E_out_minus_sim": max(abs(r["E_out"] - r["E_out_sim"]) for r in fresh.values()),
        "max_abs_E_in_minus_sim": max(abs(r["E_in"] - r["E_in_sim"]) for r in fresh.values()),
        "max_abs_E_prep_minus_matrix": max(abs(r["E_prep_marg"] - r["E_prep_marg_matrix"]) for r in fresh.values())},
}
controls_pass = controls["C1"]["pass"] and controls["C2"]["pass"] and controls["C3"]["pass"]

deciding = [(6, 1, 0.5), (8, 1, 0.5), (8, 1, 1.0), (10, 1, 0.5), (10, 1, 1.0)]
split = [(5, 1, 0.5), (6, 1, 1.0)]
deciding_ok = all(fresh[k]["R_tau0"] > 1 and fresh[k]["R_tau_marg"] > 1 for k in deciding)
split_ok = all(fresh[k]["R_tau0"] < 1 < fresh[k]["R_tau_marg"] for k in split)
nonreturn_ok = fresh[(10, 1, 2.0)]["tau_marg"] is None and target[(10, 1, 2.0)]["tau_marg"] is None
verdict = "REPLICATED" if (controls_pass and all_pass and deciding_ok and split_ok and nonreturn_ok) \
    else "REPLICATION FAILURE"

results = {
    "item": "P119-1 (FU-P1085-1) Gate-style replication of P108-5 (Xun & Ren arXiv:2410.04919)",
    "verdict": verdict,
    "fresh_machinery": "work/p1191_eval.py (dense Kronecker, full eigh); work/p1191_lean10.py (N=10 lean route, validated vs dense); work/p1191_asymptotics.py (derived pair-block evolution). Phase 108 code not read/imported/adapted.",
    "controls": controls,
    "rows_fresh": [fresh[k] for k in sorted(fresh)],
    "comparison_vs_p1085": comp_rows,
    "comparison_summary": {
        "n_rows": len(comp_rows), "all_rows_replicate": bool(all_pass),
        "worst_rel_diffs": {
            q: max((c["rel_diffs"][q] for c in comp_rows if c["rel_diffs"][q] is not None), default=0.0)
            for q in ("E_out", "E_prep_marg", "E_net_B", "tau0", "tau_marg", "R_tau0", "R_tau_marg")},
        "deciding_rows_both_conventions_clear_fresh": {str(k): [fresh[k]["R_tau0"], fresh[k]["R_tau_marg"]] for k in deciding},
        "split_rows_fresh_R_tau0_R_taumarg": {str(k): [fresh[k]["R_tau0"], fresh[k]["R_tau_marg"]] for k in split},
        "tau_marg_nonreturn_10_1_2": {"fresh": fresh[(10, 1, 2.0)]["tau_marg"], "target": target[(10, 1, 2.0)]["tau_marg"],
                                      "note": "both no return for t <= 30; fresh R_tau_marg stored 0.0 (no-return encoding), target stores null"},
        "first_negative_row": {"key": [5, 1, 0.5], "E_net_B_fresh": fresh[(5, 1, 0.5)]["E_net_B"],
                               "E_net_B_target": target[(5, 1, 0.5)]["E_net_B"]},
        "negative_rows_fresh": [list(k) for k in sorted(fresh) if fresh[k]["E_net_B"] < 0],
    },
    "tau_convention_ruling": {
        "ruling": "tau_marg",
        "argument": "P72-2 S4: the FR-net read is referenced to the uncorrelated vacuum (R-marg), not the entangled ground; the priced pulse is the excursion below the uncorrelated-reference level, ending when S(t) returns to +E_prep^(marg). tau0 is S4's tau_pulse of the FR-raw read (entangled-ground reference) - a different read's duration.",
        "status_under_other_convention_tau0": "Claim stands at the deciding rows: all five both-convention rows keep R(tau0) > 1 and (10,1,2) keeps R(tau0)=5.134; only the split rows (5,1,0.5) and (6,1,1) fall below 1 under tau0. Under tau_marg the bar is met at seven rows; under tau0 at six (five both-convention + (10,1,2)).",
    },
    "tau_asymptotics_m1": {
        "route": "derived pair-block exact exponentiation (work/p1191_asymptotics.py), validated vs dense at N in {3,5,8,10} (tau agreement <= 1.2e-10) and at N=2 vs P72-2 (tau0 to 5e-17); energies from the printed closed forms. Largest N read: 200.",
        "validation": asym["validation"],
        "rows": asym["asymptotics"],
        "read": "tau0(N) and tau_marg(N) FALL with N for both r (after the small-N plateau ~0.23): at r=0.5, tau0 goes 0.2265 (N=5) -> 0.1831 (N=10) -> 0.0466 (N=200); tau_marg tracks it closely and the two converge at large N. |E_net,B| grows and saturates (r=0.5: 0.0414 -> 0.2202 -> 0.4042, asymptote ~0.41; r=1: -> ~1.20). R therefore does NOT grow carried by |E_net,B| alone: R rises while |E_net,B| growth outruns the falling tau (peak R_tau0 ~4.67 at N=16 for r=0.5; ~13.76 at N=20 for r=1), then FALLS at larger N as tau's decline dominates (r=0.5: R_tau0 = 1.98 at N=200; r=1: 6.76 at N=200, still > 1).",
    },
    "c12": "Sourcing-accounting result in a finite spin model; preparation and injection on the books; no energy source, no field claim, no FTL wording. INTERNAL only.",
}
with open(OUT, "w") as f:
    json.dump(results, f, indent=1, default=float)
print("verdict:", verdict, "| controls pass:", controls_pass, "| all rows replicate:", all_pass,
      "| deciding ok:", deciding_ok, "| split ok:", split_ok, "| nonreturn ok:", nonreturn_ok)
print("WROTE", OUT)
