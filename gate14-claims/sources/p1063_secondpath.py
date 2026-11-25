#!/usr/bin/env python
"""P106-3 second path: FROM-SCRATCH recomputation of the deciding lines.

Written independently of p1063_eval.py: no import of it, no shared
functions. Reads ONLY the raw point fields of
../../phase72/results/p722_results.json and applies the registered
definitions (p1063_run_record.md) with its own inline arithmetic.
Deciding lines recomputed here: per-sector E_net,B / net delivered /
R_net at each point; V1/V2 aggregate net at every M; V3 final-sector
net and all-in price per unit at every L; V4 crossing M at both
references and both granted reads. Writes p1063_secondpath.json.
float64 throughout.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve()
SRC = HERE.parents[2] / "phase72" / "results" / "p722_results.json"
OUT = HERE.parent / "p1063_secondpath.json"

raw = json.loads(SRC.read_text())
coef = raw["FR_coef_3_over_32pi2"]
by_r = {}
for p in raw["points"]:
    if p["h"] == 1.0:
        by_r[p["r"]] = p

deciding = []
worst_sector_net = None
worst_R = 0.0
v4 = []

for r in (0.5, 1.0, 2.0):
    p = by_r[r]
    eb = p["EB"]; ea = p["EA"]; ps = p["E_prep_sep"]; pm = p["E_prep_marg"]
    tau = p["tau_pulse"]
    # sector net, straight from the definition E_net,B = prep_marg - E_B
    enet = 0.0
    enet = pm - eb
    delivered = eb - pm
    if enet >= 0:
        rnet = 0.0
    else:
        rnet = (-enet) * tau / coef
    deciding.append({"kind": "per_sector", "r": r, "E_net_B": enet,
                     "net_delivered": delivered, "R_net": rnet})
    worst_sector_net = delivered if worst_sector_net is None else max(worst_sector_net, delivered)
    worst_R = max(worst_R, rnet)

    # V1/V2 aggregates: sum the per-sector net M times, term by term
    for M in (1, 2, 4, 8, 16, 64, 1024):
        total = 0.0
        for _ in range(min(M, 64)):  # exact for M<=64; for 1024 use block sum below
            total += delivered
        if M == 1024:
            total = delivered * 1024  # 16 blocks of the 64-sum would be identical; direct product stated
            total = 0.0
            block = 0.0
            for _ in range(64):
                block += delivered
            for _ in range(16):
                total += block
        deciding.append({"kind": "V1_V2_aggregate_net", "r": r, "M": M,
                         "aggregate_net_delivered": total,
                         "aggregate_R_net": rnet,
                         "price_per_unit_sep": (ps + ea) / eb,
                         "price_per_unit_marg": (pm + ea) / eb,
                         "alice_aggregate_injection_V2": M * ea})
        worst_R = max(worst_R, rnet)

    # V3: final sector is one copy; all L hops pay prep+injection
    for L in (2, 4, 8):
        deciding.append({"kind": "V3_final", "r": r, "L": L,
                         "final_E_net_B": enet, "final_R_net": rnet,
                         "price_per_unit_at_final_sep": L * (ps + ea) / eb,
                         "price_per_unit_at_final_marg": L * (pm + ea) / eb})

    # V4 crossings by direct search (no floor formula): first M with net > 0
    for ref, prep in (("sep", ps), ("marg", pm)):
        for read, cost in (("sector_prep_only", prep),
                           ("total_prep_plus_injection", prep + ea)):
            M = 1
            while M * eb - cost <= 0:
                M += 1
            v4.append({"r": r, "reference": ref, "read": read, "crossing_M": M,
                       "granted_net_at_crossing": M * eb - cost})

result = {
    "path": "independent second path (no eval-script functions used)",
    "source_phase72_json": str(SRC),
    "deciding_lines": deciding,
    "V4_crossings": v4,
    "worst_per_sector_net_delivered": worst_sector_net,
    "worst_R_net_V1_V3": worst_R,
    "reopening_bar_met": bool(worst_R > 1.0),
    "all_V1_V3_net_non_positive": bool(
        worst_sector_net <= 0.0 and worst_R == 0.0),
}
OUT.write_text(json.dumps(result, indent=2))
print(json.dumps({"worst_per_sector_net_delivered": worst_sector_net,
                  "worst_R_net_V1_V3": worst_R,
                  "reopening_bar_met": result["reopening_bar_met"],
                  "V4_crossings": v4}, indent=2))
