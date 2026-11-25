"""Gate-14 checker: re-derives every deciding number from the gate's OWN
results file (results/g14_numbers.json) and compares against the stored
phase anchors (Phase 72 pair-form reads; Phase 108 deciding reads;
Phase 119 completed price values). The gate passes on no phase checker."""
import json, math, sys

G = json.load(open("results/g14_numbers.json"))
P108 = json.load(open("../phase108/results/p1085_results.json"))
P72 = json.load(open("../phase72/results/p722_results.json"))
P1193 = json.load(open("../phase119/results/p1193_results.json"))
FR = 3.0 / (32.0 * math.pi ** 2)
fails = []
n = 0

def chk(cond, label, detail=""):
    global n
    n += 1
    if not cond:
        fails.append(f"{label} {detail}")
    return cond

def rel(a, b):
    return abs(a - b) / max(abs(b), 1e-300)

rows = {(r["N"], r["m"], r["r"]): r for r in G["rows"]}
s108 = {(r["N"], r["m"], r["r"]): r for r in P108["rows"]}

# --- internal consistency of the gate's own machinery (every row) ---
for key, r in rows.items():
    chk(abs(r["E_ground_eig"]) <= 1e-10, f"{key} ground energy ~0", r["E_ground_eig"])
    chk(r["ground_overlap_eq3"] >= 1 - 1e-10, f"{key} Eq.(3) overlap", r["ground_overlap_eq3"])
    chk(rel(r["E_out_sim"], r["E_out"]) <= 1e-9, f"{key} E_out sim vs Eq.(11)", (r["E_out_sim"], r["E_out"]))
    chk(rel(r["E_in_sim"], r["E_in"]) <= 1e-9, f"{key} E_in sim vs Eq.(6)", (r["E_in_sim"], r["E_in"]))
    chk(rel(r["E_prep_marg_matrix"], r["E_prep_marg"]) <= 1e-9, f"{key} E_prep_marg matrix vs 4k^2/D",
        (r["E_prep_marg_matrix"], r["E_prep_marg"]))
    chk(abs(r["S0_plus_E_out_sim"]) <= 1e-9, f"{key} S(0) = -E_out", r["S0_plus_E_out_sim"])
    chk(rel(r["E_net_B"], r["E_prep_marg"] - r["E_out"]) <= 1e-12, f"{key} E_net identity")
    # R re-derived from the gate's own E_net and tau
    for tkey, rkey in (("tau0", "R_tau0"), ("tau_marg", "R_tau_marg")):
        tau = r[tkey]
        expect = abs(r["E_net_B"]) * tau / FR if (r["E_net_B"] < 0 and tau is not None) else 0.0
        chk(rel(r[rkey], expect) <= 1e-12 if expect else r[rkey] == 0.0,
            f"{key} {rkey} re-derived", (r[rkey], expect))

# --- N=2 control vs Phase 72 stored pair-form anchor (exact) ---
# RECOVERY REPAIR (disclosed in GATE14.md): the stored p722_results.json
# schema is "points" with the net read under "E_net_B_sector"; the
# original checker assumed "rows"/"E_net_B" and would have crashed.
# Schema adaptation only — the anchor values are Phase 72's stored
# reads, identical to the C1 values printed in CHECKPOINT119 S P119-1.
p72 = {(row["r"]): row for row in P72["points"]}
for r_ in (0.5, 1.0, 2.0):
    g = rows[(2, 1, r_)]; a = p72[r_]
    chk(rel(g["E_out"], a["EB"]) <= 1e-9, f"N=2 r={r_} E_out vs P72 EB", (g["E_out"], a["EB"]))
    chk(rel(g["E_prep_marg"], a["E_prep_marg"]) <= 1e-9, f"N=2 r={r_} E_prep_marg vs P72",
        (g["E_prep_marg"], a["E_prep_marg"]))
    chk(rel(g["E_net_B"], a["E_net_B_sector"]) <= 1e-9, f"N=2 r={r_} E_net vs P72",
        (g["E_net_B"], a["E_net_B_sector"]))
    chk(abs(g["tau0"] - a["tau_pulse"]) <= 1e-6, f"N=2 r={r_} tau0 vs P72 tau_pulse",
        (g["tau0"], a["tau_pulse"]))
    chk(g["E_net_B"] > 0, f"N=2 r={r_} pair form stays closed (E_net>0)")

# C3: tau_marg(2,0.5) registered value
chk(abs(rows[(2, 1, 0.5)]["tau_marg"] - 0.838533050344258) <= 1e-6,
    "C3 tau_marg(2,0.5)", rows[(2, 1, 0.5)]["tau_marg"])

# --- full-table replication vs Phase 108 stored reads ---
for key, a in s108.items():
    g = rows[key]
    chk(rel(g["E_out"], a["E_out"]) <= 1e-6, f"{key} E_out vs P108", (g["E_out"], a["E_out"]))
    chk(rel(g["E_net_B"], a["E_net_B"]) <= 1e-6, f"{key} E_net vs P108", (g["E_net_B"], a["E_net_B"]))
    chk(abs(g["tau0"] - a["tau0"]) <= 1e-4 * max(1.0, abs(a["tau0"])), f"{key} tau0 vs P108",
        (g["tau0"], a["tau0"]))
    if a["tau_marg"] is None:
        chk(g["tau_marg"] is None, f"{key} tau_marg null vs P108", g["tau_marg"])
    else:
        chk(g["tau_marg"] is not None and abs(g["tau_marg"] - a["tau_marg"]) <= 1e-4 * a["tau_marg"],
            f"{key} tau_marg vs P108", (g["tau_marg"], a["tau_marg"]))
    chk(rel(g["R_tau0"], a["R_tau0"]) <= 1e-4, f"{key} R_tau0 vs P108", (g["R_tau0"], a["R_tau0"]))
    if a["R_tau_marg"] is None:
        chk(g["R_tau_marg"] == 0.0, f"{key} R_tau_marg null-side vs P108", g["R_tau_marg"])
    else:
        chk(rel(g["R_tau_marg"], a["R_tau_marg"]) <= 1e-4, f"{key} R_tau_marg vs P108",
            (g["R_tau_marg"], a["R_tau_marg"]))

# --- the claim's deciding content, from the gate's own numbers ---
neg = sorted(k for k, r in rows.items() if r["E_net_B"] < 0)
chk(neg == sorted(s108[k] and k for k in s108 if s108[k]["E_net_B"] < 0),
    "negative-row set matches P108", neg)
chk(neg[0] == (5, 1, 0.5), "first negative row is (5,1,0.5)", neg[:1])
for key in [(6, 1, 0.5), (8, 1, 0.5), (8, 1, 1.0), (10, 1, 0.5), (10, 1, 1.0)]:
    chk(rows[key]["R_tau_marg"] > 1, f"DECIDING {key} R(tau_marg) > 1", rows[key]["R_tau_marg"])
chk(rows[(10, 1, 2.0)]["R_tau0"] > 1 and rows[(10, 1, 2.0)]["tau_marg"] is None,
    "DECIDING (10,1,2) R(tau0) > 1 with tau_marg null",
    (rows[(10, 1, 2.0)]["R_tau0"], rows[(10, 1, 2.0)]["tau_marg"]))
chk(rows[(5, 1, 0.5)]["R_tau_marg"] > 1 and rows[(5, 1, 0.5)]["R_tau0"] < 1,
    "split row (5,1,0.5) as registered", (rows[(5, 1, 0.5)]["R_tau0"], rows[(5, 1, 0.5)]["R_tau_marg"]))
chk(rows[(6, 1, 1.0)]["R_tau_marg"] > 1 and rows[(6, 1, 1.0)]["R_tau0"] < 1,
    "split row (6,1,1) as registered", (rows[(6, 1, 1.0)]["R_tau0"], rows[(6, 1, 1.0)]["R_tau_marg"]))

# --- completed price caveat, gate's own sep certificates ---
sep = {(tuple(s["row"])): s for s in G["sep_certificate"]}
p1193rows = {(r["N"], r["m"], r["r"]): r for r in P1193["rows"]}
for key, s in sep.items():
    chk(s["E_sep_multistart"] >= s["E_sep_corner_D_minus_N"] - 1e-9,
        f"SEP {key} no product state below corner", (s["E_sep_multistart"], s["E_sep_corner_D_minus_N"]))
    chk(abs(s["E_sep_multistart"] - s["E_sep_corner_D_minus_N"]) <= 1e-6,
        f"SEP {key} corner attains the minimum", (s["E_sep_multistart"], s["E_sep_corner_D_minus_N"]))
    chk(rel(s["Pi_sep"], p1193rows[key]["Pi_sep"]) <= 1e-6,
        f"SEP {key} Pi_sep vs P119-3", (s["Pi_sep"], p1193rows[key]["Pi_sep"]))
lo, hi = G["price_deciding_range_sep"]
chk(abs(lo - 5.3401206317727405) <= 1e-4 and abs(hi - 28.170099145164052) <= 1e-4,
    "completed price range 5.34-28.17 reproduced", (lo, hi))

print(f"GATE-14 CHECKER: {n - len(fails)}/{n} PASS")
for f in fails:
    print("FAIL:", f)
sys.exit(1 if fails else 0)
