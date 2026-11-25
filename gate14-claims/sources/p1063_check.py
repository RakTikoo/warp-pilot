#!/usr/bin/env python
"""P106-3 checker: recomputes EVERY verdict-carrying number in
results/p1063_results.json from ../../phase72/results/
p722_results.json + the registered definitions
(results/p1063_run_record.md), and cross-checks the deciding lines
against the independent second path's output
(work/p1063_secondpath.json). Prints PASS/FAIL counts.
float64 throughout.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve()
P72_JSON = HERE.parents[2] / "phase72" / "results" / "p722_results.json"
RES_JSON = HERE.parents[1] / "results" / "p1063_results.json"
SP_JSON = HERE.parent / "p1063_secondpath.json"

npass = nfail = 0
fails = []


def chk(name, cond):
    global npass, nfail
    if cond:
        npass += 1
    else:
        nfail += 1
        fails.append(name)


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main():
    p72 = json.loads(P72_JSON.read_text())
    res = json.loads(RES_JSON.read_text())
    sp = json.loads(SP_JSON.read_text())
    coef = float(p72["FR_coef_3_over_32pi2"])
    chk("FR coef matches 3/(32 pi^2)", close(coef, 3.0 / (32 * math.pi ** 2), 1e-15))
    src = {p["r"]: p for p in p72["points"] if p["h"] == 1.0}

    def rnet(enet, tau):
        return 0.0 if enet >= 0.0 else abs(enet) * tau / coef

    # ---- points block ----
    chk("3 points", len(res["points"]) == 3)
    for base in res["points"]:
        p = src[base["r"]]
        EB, EA = float(p["EB"]), float(p["EA"])
        ps, pm = float(p["E_prep_sep"]), float(p["E_prep_marg"])
        tau = float(p["tau_pulse"])
        enet = pm - EB
        chk(f"r={base['r']} EB", close(base["EB"], EB, 1e-15))
        chk(f"r={base['r']} EA", close(base["EA"], EA, 1e-15))
        chk(f"r={base['r']} E_net_B recomputed", close(base["E_net_B_recomputed"], enet, 1e-12))
        chk(f"r={base['r']} E_net_B vs stored field", close(enet, float(p["E_net_B_sector"]), 1e-12))
        chk(f"r={base['r']} E_prep_marg formula 2k^2/sqrt(h^2+k^2)",
            close(pm, 2 * p["k"] ** 2 / math.sqrt(p["h"] ** 2 + p["k"] ** 2), 1e-12))
        chk(f"r={base['r']} EA formula h^2/sqrt(h^2+k^2)",
            close(EA, p["h"] ** 2 / math.sqrt(p["h"] ** 2 + p["k"] ** 2), 1e-12))
        chk(f"r={base['r']} net delivered", close(base["net_delivered_per_sector"], EB - pm, 1e-12))
        chk(f"r={base['r']} R_net", close(base["R_net_per_sector"], rnet(enet, tau), 1e-12))
        chk(f"r={base['r']} R_net vs stored", close(base["R_net_per_sector"], float(p["R_net"]), 1e-12))
        chk(f"r={base['r']} price/unit sep", close(base["price_per_unit_sep"], (ps + EA) / EB, 1e-12))
        chk(f"r={base['r']} price/unit marg", close(base["price_per_unit_marg"], (pm + EA) / EB, 1e-12))
        chk(f"r={base['r']} price/unit sep vs stored total_per_EB",
            close(base["price_per_unit_sep"], float(p["total_per_EB"]), 1e-12))
        chk(f"r={base['r']} price/unit marg vs stored total_per_EB_marg",
            close(base["price_per_unit_marg"], float(p["total_per_EB_marg"]), 1e-12))
        chk(f"r={base['r']} EB <= EA (source bound)", EB <= EA)

    # ---- V1 / V2 ----
    for tag, rows in (("V1", res["V1_parallel"]), ("V2", res["V2_star"])):
        chk(f"{tag} row count 21", len(rows) == 21)
        for row in rows:
            p = src[row["r"]]
            EB, EA = float(p["EB"]), float(p["EA"])
            ps, pm = float(p["E_prep_sep"]), float(p["E_prep_marg"])
            M = row["M"]; enet = pm - EB
            chk(f"{tag} r={row['r']} M={M} per-sector E_net_B", close(row["per_sector_E_net_B"], enet))
            chk(f"{tag} r={row['r']} M={M} per-sector R_net", close(row["per_sector_R_net"], rnet(enet, float(p["tau_pulse"]))))
            chk(f"{tag} r={row['r']} M={M} aggregate net", close(row["aggregate_net_delivered"], M * (EB - pm)))
            chk(f"{tag} r={row['r']} M={M} aggregate net <= 0", row["aggregate_net_delivered"] <= 0.0)
            chk(f"{tag} r={row['r']} M={M} aggregate raw", close(row["aggregate_raw_delivered"], M * EB))
            chk(f"{tag} r={row['r']} M={M} price/unit sep", close(row["total_price_per_unit_delivered_sep"], (ps + EA) / EB))
            chk(f"{tag} r={row['r']} M={M} price/unit marg", close(row["total_price_per_unit_delivered_marg"], (pm + EA) / EB))
            chk(f"{tag} r={row['r']} M={M} aggregate price sep", close(row["aggregate_price_sep"], M * (ps + EA)))
            chk(f"{tag} r={row['r']} M={M} aggregate price marg", close(row["aggregate_price_marg"], M * (pm + EA)))
            if tag == "V2":
                chk(f"V2 r={row['r']} M={M} Alice aggregate injection", close(row["alice_aggregate_injection"], M * EA))
                chk(f"V2 r={row['r']} M={M} no shared measurement granted",
                    row["shared_single_measurement_granted"] is False)

    # ---- V3 ----
    chk("V3 row count 9", len(res["V3_relay"]) == 9)
    for row in res["V3_relay"]:
        p = src[row["r"]]
        EB, EA = float(p["EB"]), float(p["EA"])
        ps, pm = float(p["E_prep_sep"]), float(p["E_prep_marg"])
        L = row["L"]; enet = pm - EB
        chk(f"V3 r={row['r']} L={L} final E_net_B", close(row["final_sector_E_net_B"], enet))
        chk(f"V3 r={row['r']} L={L} final R_net", close(row["final_sector_R_net"], rnet(enet, float(p["tau_pulse"]))))
        chk(f"V3 r={row['r']} L={L} final net <= 0", row["final_sector_net_delivered"] <= 0.0)
        chk(f"V3 r={row['r']} L={L} price/unit final sep", close(row["total_price_per_unit_delivered_at_final_sep"], L * (ps + EA) / EB))
        chk(f"V3 r={row['r']} L={L} price/unit final marg", close(row["total_price_per_unit_delivered_at_final_marg"], L * (pm + EA) / EB))
        chk(f"V3 r={row['r']} L={L} upstream counted", close(row["upstream_cost_sep"], (L - 1) * (ps + EA))
            and close(row["upstream_cost_marg"], (L - 1) * (pm + EA)))

    # ---- V4 ----
    chk("V4 row count 12", len(res["V4_adversarial_bound"]) == 12)
    for row in res["V4_adversarial_bound"]:
        p = src[row["r"]]
        EB, EA = float(p["EB"]), float(p["EA"])
        prep = float(p["E_prep_sep"]) if row["reference"] == "sep" else float(p["E_prep_marg"])
        cost = prep if row["read"] == "sector_prep_only" else prep + EA
        chk(f"V4 r={row['r']} {row['reference']} {row['read']} cost", close(row["cost_paid_once"], cost))
        chk(f"V4 r={row['r']} {row['reference']} {row['read']} crossing is floor+1",
            row["crossing_M"] == math.floor(cost / EB) + 1)
        chk(f"V4 r={row['r']} {row['reference']} {row['read']} net>0 at crossing",
            row["crossing_M"] * EB - cost > 0.0 and close(row["granted_net_at_crossing_M"], row["crossing_M"] * EB - cost))
        chk(f"V4 r={row['r']} {row['reference']} {row['read']} net<=0 at crossing-1",
            (row["crossing_M"] - 1) * EB - cost <= 0.0)
        chk(f"V4 r={row['r']} {row['reference']} {row['read']} cannot fire bar",
            row["can_fire_reopening_bar"] is False and row["R_net_assigned"] is None)
        for M_str, val in row["granted_net_at_registered_M"].items():
            chk(f"V4 r={row['r']} {row['reference']} {row['read']} granted net M={M_str}",
                close(val, int(M_str) * EB - cost))

    # ---- summary + verdict ----
    s = res["summary"]
    all_enet = [float(p["E_prep_marg"]) - float(p["EB"]) for p in src.values()]
    chk("summary max per-sector net", close(s["max_per_sector_net_delivered_V1_V3"], max(-e for e in all_enet)))
    chk("summary max R_net = 0", s["max_R_net_V1_V3"] == 0.0)
    chk("summary no positive", s["any_V1_V3_net_positive"] is False)
    chk("summary bar not met", s["reopening_bar_met"] is False)
    chk("closure count 51", s["closure_count"]["total_protocol_net_reads"] == 51)
    chk("verdict form", res["verdict"] == "NET NON-POSITIVE IN ALL REGISTERED MULTI-PARTY FORMS")

    # ---- second-path cross-check ----
    chk("second path worst sector net", close(sp["worst_per_sector_net_delivered"],
                                              s["max_per_sector_net_delivered_V1_V3"]))
    chk("second path worst R", close(sp["worst_R_net_V1_V3"], s["max_R_net_V1_V3"]))
    chk("second path bar not met", sp["reopening_bar_met"] is False)
    sp_v4 = {(d["r"], d["reference"], d["read"]): d["crossing_M"] for d in sp["V4_crossings"]}
    for row in res["V4_adversarial_bound"]:
        chk(f"second path V4 crossing r={row['r']} {row['reference']} {row['read']}",
            sp_v4[(row["r"], row["reference"], row["read"])] == row["crossing_M"])
    sp_agg = {(d["r"], d["M"]): d for d in sp["deciding_lines"] if d["kind"] == "V1_V2_aggregate_net"}
    for row in res["V1_parallel"]:
        d = sp_agg[(row["r"], row["M"])]
        chk(f"second path V1 aggregate r={row['r']} M={row['M']}",
            close(d["aggregate_net_delivered"], row["aggregate_net_delivered"]))
    sp_v3 = {(d["r"], d["L"]): d for d in sp["deciding_lines"] if d["kind"] == "V3_final"}
    for row in res["V3_relay"]:
        d = sp_v3[(row["r"], row["L"])]
        chk(f"second path V3 price sep r={row['r']} L={row['L']}",
            close(d["price_per_unit_at_final_sep"], row["total_price_per_unit_delivered_at_final_sep"]))
        chk(f"second path V3 price marg r={row['r']} L={row['L']}",
            close(d["price_per_unit_at_final_marg"], row["total_price_per_unit_delivered_at_final_marg"]))

    print(f"P106-3 CHECKER: {npass} PASS, {nfail} FAIL")
    for f in fails:
        print("FAIL:", f)
    raise SystemExit(1 if nfail else 0)


if __name__ == "__main__":
    main()
