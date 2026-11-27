"""g51_summary.py — collect the Gate-51 deciding reads into
gate51/results/g51_summary.json (registered-bar verdict table)."""
import json

WP = "/home/hatch/workspace/warp-pilot"
rec = json.load(open(f"{WP}/gate51/results/g51_records.json"))
scr = json.load(open(f"{WP}/gate51/results/g51_screen.json"))
out = {"records": {"hashes": rec["hashes"],
                   "rw5_interiority_min": {
                       "all_strictly_inside": rec["rw5_interiority"]["all_strictly_inside"],
                       "min_edge_distance": rec["rw5_interiority"]["min_edge_distance"],
                       "min_edge_coord": rec["rw5_interiority"]["min_edge_coord"],
                       "c1": rec["rw5_interiority"]["c1"],
                       "c9": rec["rw5_interiority"]["c9"]},
                   "arm_t": rec["arm_t"], "arm_r16": rec["arm_r16"]},
       "screen": scr, "audits": {}}
for name in ("y_his", "E2-1", "RW-5", "RW-1"):
    a = json.load(open(f"{WP}/gate51/results/g51_audits_{name}.json"))
    out["audits"][name] = {"chain_reads": a["chain_reads"], "rungs": {}}
    for beta, au in a["audits"].items():
        rung = {"legal_full_common_bars": au["legal_full_common_bars"],
                "second_path_sign_agreement": au["second_path_sign_agreement"],
                "per_h": {}}
        for hk in ("h0.0375", "h0.01875"):
            L = au["legality"][hk]
            sp = au["by_h"][hk]["second_path"]
            q = au["by_h"][hk]["q"]
            rung["per_h"][hk] = {
                "worst": L["worst"], "worst_kind": L["worst_kind"],
                "worst_r": L["worst_r"], "floor": L["floor"],
                "worst_over_floor": L["worst_over_floor"],
                "typeI_frac": L["typeI_frac"],
                "shell_sampled_nec_min": L["shell_sampled_nec_min"],
                "per_ec": L["per_ec"],
                "audit4_worst": sp["worst"],
                "audit4_per_ec": {k: sp[k] for k in ("nec", "wec", "sec", "dec")},
                "audit4_typeI_frac_diag": sp["typeI_frac"],
                "q_max": q["q_max"], "q_max_r": q["q_max_r"]}
        out["audits"][name]["rungs"][beta] = rung
json.dump(out, open(f"{WP}/gate51/results/g51_summary.json", "w"), indent=1)
print("SUMMARY DONE")
