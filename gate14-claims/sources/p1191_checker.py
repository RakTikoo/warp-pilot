#!/usr/bin/env python
"""P119-1 independent checker. Recomputes every verdict-carrying number
from results/p1191_results.json and the stored targets
(phase108 p1085_results.json, phase72 p722_results.json) only.
Does NOT import p1191_eval / p1191_lean10 / p1191_asymptotics.
Checks: controls C1-C3 from the results file's fresh rows; closed-form
E_out/E_in/E_prep per row; E_net and R and price arithmetic per row;
replication tolerances vs the target; deciding/split/non-return
conditions; asymptotics rows' closed-form and R arithmetic.
"""
import json, math, sys

RES = "/home/hatch/workspace/warp-pilot/phase119/results/p1191_results.json"
TGT = "/home/hatch/workspace/warp-pilot/phase108/results/p1085_results.json"
P72 = "/home/hatch/workspace/warp-pilot/phase72/results/p722_results.json"
FR = 3.0/(32.0*math.pi**2)

R = json.load(open(RES))
T = {(r["N"], r["m"], r["r"]): r for r in json.load(open(TGT))["rows"]}
P = {p["r"]: p for p in json.load(open(P72))["points"]}
F = {(r["N"], r["m"], r["r"]): r for r in R["rows_fresh"]}
fails = []
def chk(cond, msg):
    if not cond:
        fails.append(msg)
def rel(a, b):
    if a is None and b is None: return 0.0
    if a is None or b is None: return None
    return abs(a-b)/max(abs(b), 1e-300)

chk(len(F) == 30 and set(F) == set(T), "row set != 30 target rows")
for k, f in F.items():
    N, m, r = k; h = 1.0; kpar = r
    D = math.sqrt(N**2 + 4*kpar**2)
    A = N*m + 4*kpar**2
    E_out_cf = A/D*(math.sqrt(1 + (2*(N-m)*kpar)**2/A**2) - 1)
    E_in_cf = (N-m)*N/D
    E_prep_cf = 4*kpar**2/D
    chk(rel(f["E_out"], E_out_cf) <= 1e-12, f"{k} E_out != Eq.(11)")
    chk(rel(f["E_in"], E_in_cf) <= 1e-12, f"{k} E_in != Eq.(6)")
    chk(rel(f["E_prep_marg"], E_prep_cf) <= 1e-12, f"{k} E_prep != 4k^2/D")
    chk(abs(f["E_net_B"] - (f["E_prep_marg"] - f["E_out"])) <= 1e-12, f"{k} E_net arithmetic")
    chk(abs(f["E_out"] - f["E_out_sim"]) <= 1e-9, f"{k} E_out sim cross-check")
    chk(abs(f["E_in"] - f["E_in_sim"]) <= 1e-9, f"{k} E_in sim cross-check")
    chk(abs(f["E_prep_marg"] - f["E_prep_marg_matrix"]) <= 1e-9, f"{k} E_prep matrix cross-check")
    for tau_q, R_q in (("tau0", "R_tau0"), ("tau_marg", "R_tau_marg")):
        tau, Rv = f[tau_q], f[R_q]
        expect = abs(f["E_net_B"])*tau/FR if (f["E_net_B"] < 0 and tau) else 0.0
        chk(abs(Rv - expect) <= 1e-9*max(1, abs(expect)), f"{k} {R_q} arithmetic")
    chk(rel(f["price_per_unit"], (f["E_prep_marg"] + f["E_in"])/f["E_out"]) <= 1e-12, f"{k} price arithmetic")
    # replication standard vs target
    t = T[k]
    for q in ("E_out", "E_prep_marg", "E_net_B"):
        chk(rel(f[q], t[q]) <= 1e-6, f"{k} {q} fails replication tol")
    for q in ("tau0", "tau_marg", "R_tau0", "R_tau_marg"):
        fv, tv = f[q], t[q]
        if q.startswith("R") and fv in (0.0, None) and tv in (0.0, None):
            continue
        d = rel(fv, tv)
        chk(d is not None and d <= 1e-4, f"{k} {q} fails replication tol (d={d})")
# controls
for r_ in (0.5, 1.0, 2.0):
    f, p = F[(2, 1, r_)], P[r_]
    chk(rel(f["E_out"], p["EB"]) <= 1e-9, f"C1 r={r_} E_out")
    chk(rel(f["E_prep_marg"], p["E_prep_marg"]) <= 1e-9, f"C1 r={r_} E_prep")
    chk(rel(f["E_net_B"], p["E_net_B_sector"]) <= 1e-9, f"C1 r={r_} E_net")
    chk(abs(f["tau0"] - p["tau_pulse"]) <= 1e-6, f"C1 r={r_} tau0")
chk(max(abs(f["E_ground_eig"]) for f in F.values()) <= 1e-12, "C2 ground energy")
chk(min(f["ground_overlap_eq3"] for f in F.values()) >= 1 - 1e-10, "C2 overlap")
chk(abs(F[(2, 1, 0.5)]["tau_marg"] - 0.838533050344258) <= 1e-6, "C3 tau_marg")
# deciding / split / non-return / first negative
for k in [(6, 1, 0.5), (8, 1, 0.5), (8, 1, 1.0), (10, 1, 0.5), (10, 1, 1.0)]:
    chk(F[k]["R_tau0"] > 1 and F[k]["R_tau_marg"] > 1, f"deciding {k} not both-clear")
for k in [(5, 1, 0.5), (6, 1, 1.0)]:
    chk(F[k]["R_tau0"] < 1 < F[k]["R_tau_marg"], f"split {k} not split")
chk(F[(10, 1, 2.0)]["tau_marg"] is None and T[(10, 1, 2.0)]["tau_marg"] is None, "(10,1,2) non-return mismatch")
chk(F[(10, 1, 2.0)]["R_tau0"] > 1, "(10,1,2) R_tau0 <= 1")
neg = sorted(k for k, f in F.items() if f["E_net_B"] < 0)
chk(neg == [(5, 1, 0.5), (6, 1, 0.5), (6, 1, 1.0), (8, 1, 0.5), (8, 1, 1.0),
            (10, 1, 0.5), (10, 1, 1.0), (10, 1, 2.0)], f"negative row set differs: {neg}")
chk(abs(F[(5, 1, 0.5)]["E_net_B"] - (-0.04140061640580686)) <= 1e-9, "first negative row value")
# asymptotics arithmetic
for row in R["tau_asymptotics_m1"]["rows"]:
    N, r = row["N"], row["r"]
    D = math.sqrt(N**2 + 4*r**2); A = N + 4*r**2
    Eo = A/D*(math.sqrt(1 + (2*(N-1)*r)**2/A**2) - 1); Ep = 4*r**2/D
    chk(rel(row["E_out"], Eo) <= 1e-12 and rel(row["E_prep"], Ep) <= 1e-12, f"asym N={N} r={r} closed forms")
    chk(abs(row["E_net_B"] - (Ep - Eo)) <= 1e-9, f"asym N={N} r={r} E_net")
    for tau_q, R_q in (("tau0", "R_tau0"), ("tau_marg", "R_tau_marg")):
        expect = abs(row["E_net_B"])*row[tau_q]/FR if (row["E_net_B"] < 0 and row[tau_q]) else 0.0
        chk(abs(row[R_q] - expect) <= 1e-9*max(1, abs(expect)), f"asym N={N} r={r} {R_q}")
chk(R["verdict"] == "REPLICATED", "verdict field != REPLICATED")
chk(R["tau_convention_ruling"]["ruling"] == "tau_marg", "ruling field != tau_marg")

n_checks_note = "all checks"
if fails:
    print(f"P119-1 CHECKER: FAIL ({len(fails)})")
    for x in fails:
        print(" -", x)
    sys.exit(1)
print("P119-1 CHECKER: ALL PASS (controls C1-C3, 30-row replication tolerances, "
      "closed-form + arithmetic recomputation, deciding/split/non-return conditions, asymptotics arithmetic)")
