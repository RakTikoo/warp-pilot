#!/usr/bin/env python
"""P106-3 evaluation: multi-party QET net reads.

Accounting item only. Definitions fixed in
results/p1063_run_record.md (registered in CHECKPOINT106.md
section P106-3, inherited verbatim from P72-2). Every number is
recomputed from ../../phase72/results/p722_results.json's stored
point fields, never quoted from prose. float64 throughout.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve()
P72_JSON = HERE.parents[2] / "phase72" / "results" / "p722_results.json"
OUT_JSON = HERE.parents[1] / "results" / "p1063_results.json"

M_SET = [1, 2, 4, 8, 16, 64, 1024]
L_SET = [2, 4, 8]
R_SET = [0.5, 1.0, 2.0]


def r_net(E_net_B, tau_pulse, fr_coef):
    """P72-2 section 4 FR-net: 0 iff E_net,B >= 0, else |E_net,B|*tau/coef."""
    if E_net_B >= 0.0:
        return 0.0
    return abs(E_net_B) * tau_pulse / fr_coef


def main():
    p72 = json.loads(P72_JSON.read_text())
    fr_coef = float(p72["FR_coef_3_over_32pi2"])
    pts = []
    for r in R_SET:
        pt = next(p for p in p72["points"] if p["h"] == 1.0 and p["r"] == r)
        pts.append(pt)

    points_out = []
    v1_rows, v2_rows, v3_rows, v4_rows = [], [], [], []

    for pt in pts:
        EB = float(pt["EB"]); EA = float(pt["EA"])
        prep_sep = float(pt["E_prep_sep"]); prep_marg = float(pt["E_prep_marg"])
        tau = float(pt["tau_pulse"])
        E_net_B = prep_marg - EB
        base = {
            "h": float(pt["h"]), "k": float(pt["k"]), "r": float(pt["r"]),
            "EA": EA, "EB": EB,
            "E_prep_sep": prep_sep, "E_prep_marg": prep_marg,
            "tau_pulse": tau,
            "E_net_B_recomputed": E_net_B,
            "E_net_B_stored": float(pt["E_net_B_sector"]),
            "E_net_B_matches_stored": abs(E_net_B - float(pt["E_net_B_sector"])) < 1e-12,
            "net_delivered_per_sector": EB - prep_marg,
            "R_net_per_sector": r_net(E_net_B, tau, fr_coef),
            "R_net_stored_single_copy": float(pt["R_net"]),
            "price_sep_per_copy": prep_sep + EA,
            "price_marg_per_copy": prep_marg + EA,
            "price_per_unit_sep": (prep_sep + EA) / EB,
            "price_per_unit_marg": (prep_marg + EA) / EB,
            "price_per_unit_sep_stored": float(pt["total_per_EB"]),
            "price_per_unit_marg_stored": float(pt["total_per_EB_marg"]),
        }
        points_out.append(base)

        # ---- V1 parallel / V2 star (identical resource accounting) ----
        for M in M_SET:
            common = {
                "r": base["r"], "M": M,
                "per_sector_E_net_B": E_net_B,
                "per_sector_net_delivered": EB - prep_marg,
                "per_sector_R_net": base["R_net_per_sector"],
                "aggregate_R_net": base["R_net_per_sector"],
                "aggregate_raw_delivered": M * EB,
                "aggregate_net_delivered": M * (EB - prep_marg),
                "aggregate_price_sep": M * (prep_sep + EA),
                "aggregate_price_marg": M * (prep_marg + EA),
                "total_price_per_unit_delivered_sep": (M * (prep_sep + EA)) / (M * EB),
                "total_price_per_unit_delivered_marg": (M * (prep_marg + EA)) / (M * EB),
                "aggregate_net_le_zero": bool(M * (EB - prep_marg) <= 0.0),
            }
            v1_rows.append(dict(common, variant="V1_parallel"))
            v2_rows.append(dict(common, variant="V2_star",
                                alice_aggregate_injection=M * EA,
                                shared_single_measurement_granted=False,
                                each_pair_separately_prepared_and_measured=True))

        # ---- V3 relay chain ----
        for L in L_SET:
            v3_rows.append({
                "variant": "V3_relay", "r": base["r"], "L": L,
                "final_sector_E_net_B": E_net_B,
                "final_sector_net_delivered": EB - prep_marg,
                "final_sector_R_net": base["R_net_per_sector"],
                "delivered_at_final_sector": EB,
                "total_price_all_hops_sep": L * (prep_sep + EA),
                "total_price_all_hops_marg": L * (prep_marg + EA),
                "total_price_per_unit_delivered_at_final_sep": L * (prep_sep + EA) / EB,
                "total_price_per_unit_delivered_at_final_marg": L * (prep_marg + EA) / EB,
                "upstream_hops_counted": L - 1,
                "upstream_cost_sep": (L - 1) * (prep_sep + EA),
                "upstream_cost_marg": (L - 1) * (prep_marg + EA),
                "final_net_le_zero": bool(EB - prep_marg <= 0.0),
            })

        # ---- V4 adversarial bound (artefact; NOT an R_net read) ----
        for ref_name, prep in (("sep", prep_sep), ("marg", prep_marg)):
            for read_name, cost in (("sector_prep_only", prep),
                                    ("total_prep_plus_injection", prep + EA)):
                cross = math.floor(cost / EB) + 1
                # verify crossing property directly
                assert cross * EB - cost > 0.0
                assert (cross - 1) * EB - cost <= 0.0
                v4_rows.append({
                    "variant": "V4_adversarial_bound", "r": base["r"],
                    "reference": ref_name, "read": read_name,
                    "cost_paid_once": cost, "E_prep_ref": prep, "EA": EA, "EB": EB,
                    "crossing_M": cross,
                    "granted_net_at_crossing_M": cross * EB - cost,
                    "granted_net_at_crossing_M_minus_1": (cross - 1) * EB - cost,
                    "granted_net_at_registered_M": {str(M): M * EB - cost for M in M_SET},
                    "R_net_assigned": None,
                    "can_fire_reopening_bar": False,
                    "caveat": ("the uncorrelated reference against which R_net is "
                               "defined is PER RECEIVING SECTOR (each sector's "
                               "marginal-product correlation energy is its own), so "
                               "this crossing is an artefact of deleting per-sector "
                               "resources from the books, not an R_net read; V4 "
                               "cannot fire the reopening bar"),
                })

    all_protocol_rows = v1_rows + v2_rows + v3_rows
    max_per_sector_net = max(
        [row["per_sector_net_delivered"] for row in v1_rows]
        + [row["final_sector_net_delivered"] for row in v3_rows])
    max_aggregate_net = max(row["aggregate_net_delivered"] for row in v1_rows + v2_rows)
    max_R = max([row["per_sector_R_net"] for row in v1_rows + v2_rows]
                + [row["final_sector_R_net"] for row in v3_rows])
    any_positive = any(
        [row["aggregate_net_delivered"] > 0.0 for row in v1_rows + v2_rows]
        + [row["final_sector_net_delivered"] > 0.0 for row in v3_rows])
    bar_met = bool(max_R > 1.0)

    verdict = ("MULTI-PARTY NET POSITIVE \u2014 REOPENING BAR MET" if bar_met
               else "NET NON-POSITIVE IN ALL REGISTERED MULTI-PARTY FORMS")

    out = {
        "item": "P106-3 MULTI-PARTY QET NET READS (FU-P833-2)",
        "source_phase72_json": str(P72_JSON),
        "FR_coef_3_over_32pi2": fr_coef,
        "evaluated_points_r": R_SET,
        "M_set": M_SET, "L_set": L_SET,
        "points": points_out,
        "V1_parallel": v1_rows,
        "V2_star": v2_rows,
        "V3_relay": v3_rows,
        "V4_adversarial_bound": v4_rows,
        "summary": {
            "max_per_sector_net_delivered_V1_V3": max_per_sector_net,
            "max_aggregate_net_delivered_V1_V2": max_aggregate_net,
            "max_R_net_V1_V3": max_R,
            "any_V1_V3_net_positive": bool(any_positive),
            "reopening_bar_met": bar_met,
            "reopening_bar": "any variant (V1-V3) with R_net > 1 resource-counted",
            "closure_count": {
                "protocol_forms": 3,
                "V1_reads": len(v1_rows), "V2_reads": len(v2_rows),
                "V3_reads": len(v3_rows),
                "total_protocol_net_reads": len(all_protocol_rows),
                "statement": ("3 protocol forms (V1, V2, V3) x scales "
                              "(V1: 7 M values, V2: 7 M values, V3: 3 L values "
                              "= 17 form-scale combinations) x 3 evaluated points "
                              "= 51 net reads"),
            },
        },
        "verdict": verdict,
        "C12": ("an accounting verdict on a sourcing scheme; no throat, no "
                "transport, nothing FTL is claimed by any outcome of this item"),
    }
    OUT_JSON.write_text(json.dumps(out, indent=2))
    print(json.dumps({"verdict": verdict,
                      "max_per_sector_net_delivered": max_per_sector_net,
                      "max_aggregate_net_delivered": max_aggregate_net,
                      "max_R_net": max_R,
                      "V4_crossings": [
                          {"r": row["r"], "ref": row["reference"],
                           "read": row["read"], "crossing_M": row["crossing_M"]}
                          for row in v4_rows]}, indent=2))


if __name__ == "__main__":
    main()
