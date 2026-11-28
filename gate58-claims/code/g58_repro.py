"""
g58_repro.py — Gate-58 (re-convened) independent recomputation of
Phase 432's stored-record claims, with the gate's own code (does
not import the phase's checker):
  (a) controls C-432-3..6 from the stored pool/staging records:
      gen0check gate of record (n_pts 3,640; 64/64 exact, max dev
      0.0) recomputed row by row; the VM staging cross-check the
      same; C-432-4 recalibration brackets; C-432-5 (B-4 = staged
      member idx 10, its row reads exactly 0.194140625);
      C-432-6 max |Delta|.
  (b) the search record: DE trajectory facts from
      b432_de_state.json (best step at resumed gen 58; final
      population 43/64 at the new best, all 64 >= the old best,
      mean) and the saturation-bar (i) consequence.
  (c) the margin multiples, from the GATE's own audit record
      (g58_audit.json): C-5's worst SEC over (i) the gate's own
      re-measured FD floor at the B-4 rung (the C-432-2-form
      floor), (ii) the phase's C-432-2 floor as stored,
      (iii) C-5's own gate floor proxy; B-4's multiple
      recomputed on gate reads; the tied subjects' stored vs
      gate margins.
Writes gate58/results/g58_repro.json.
"""
import json, hashlib
import numpy as np

WP = "/home/hatch/workspace/warp-pilot"
DTYPE = np.float64

v432 = json.load(open(f"{WP}/phase432/results/p432_verdicts.json"))
c432 = json.load(open(f"{WP}/phase432/results/p432_controls.json"))
gen0 = json.load(open(f"{WP}/phase432/results/p432_gen0check.json"))
xchk = json.load(open(f"{WP}/phase432/results/p432_crosscheck_cpu.json"))
recal = json.load(open(f"{WP}/phase432/results/p432_recalib_b.json"))
val = json.load(open(f"{WP}/phase432/results/p432_validate_b.json"))
search = json.load(open(f"{WP}/phase432/results/p432_search.json"))
state = json.load(open(f"{WP}/phase432/results/b432_de_state.json"))
ga = json.load(open(f"{WP}/gate58/results/g58_audit.json"))


def vhash(y):
    return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()


out = {}

# ---- (a) C-432-3 both forms, recomputed row by row ----
def crosscheck_recompute(rec, label):
    rows = rec["rows"]
    devs = [abs(r["reread_bc"] - r["stored_bc"]) for r in rows]
    return {"label": label, "n_pts": rec["n_pts"],
            "n_members": len(rows),
            "n_exact_recomputed": int(sum(1 for d in devs if d == 0.0)),
            "max_abs_dev_recomputed": float(max(devs)),
            "best_reread": rec["best_reread"],
            "stored_fields": {k: rec[k] for k in
                              ("n_exact", "n_brackets_equal",
                               "max_abs_dev") if k in rec}}
out["C-432-3_gate_of_record_pool"] = crosscheck_recompute(gen0, "pool gen0check")
out["C-432-3_staging_form_vm"] = crosscheck_recompute(xchk, "VM CPU staging")
out["C-432-5"] = {
    "b4_idx_in_crosscheck": xchk["b4_idx"],
    "b4_row_reread_bc": xchk["rows"][xchk["b4_idx"]]["reread_bc"],
    "b4_row_stored_bc": xchk["rows"][xchk["b4_idx"]]["stored_bc"],
    "expected": 0.194140625}

# ---- (a) C-432-4 / C-432-6 from stored records ----
out["C-432-4"] = {"stored_pass": recal["pass"],
                  "y_his_class_pass": recal["y_his_class_pass"],
                  "artefact_class_pass": recal["artefact_class_pass"],
                  "reads": recal["reads"]}
out["C-432-6"] = {"stored_pass": val["pass"],
                  "max_abs_diff_overall": val["max_abs_diff_overall"],
                  "bar": val["bar"]}

# ---- (b) search trajectory facts ----
bc = np.array(state["beta_crit"], dtype=DTYPE)
bh = [row["best"] for row in state["best_hist"]]
step_gens = [i for i in range(1, len(bh)) if bh[i] > bh[i - 1]]
out["search"] = {
    "gen_final": state["gen"], "n_evals": state["n_evals"],
    "elapsed_s": state["elapsed_s"], "n_pts": state["n_pts"],
    "best_beta_crit": state["best_beta_crit"],
    "best_hist_steps_at_resumed_gens": step_gens,
    "best_hist_final": bh[-1],
    "final_pop_n_at_new_best": int((bc == 0.194921875).sum()),
    "final_pop_n_at_or_above_old_best": int((bc >= 0.194140625).sum()),
    "final_pop_mean": float(bc.mean()),
    "final_pop_min": float(bc.min()),
    "saturation_bar_i_best_never_exceeds_old": bool(
        state["best_beta_crit"] <= 0.194140625),
    "best_y_hash": vhash(state["best_y"]),
    "harvest_record": search["arm"]["harvest"] if "harvest" in
    search.get("arm", {}) else None}

# ---- (c) margin multiples on the gate's own reads ----
c5w = ga["C-5"]["audit"]["h0.0375"]["worst"]
c5_floor_own = ga["C-5"]["audit"]["h0.0375"]["floor"]
b4_floor_gate = ga["B-4"]["audit"]["h0.0375"]["floor"]
b4w_gate = ga["B-4"]["audit"]["h0.0375"]["worst"]
floor_phase_c4322 = c432["C-432-2"]["measured_FD_floor_h0.0375"]
out["margins"] = {
    "C-5_worst_SEC_gate": c5w,
    "C-5_worst_SEC_phase": v432["subjects"]["C-5"]["anatomy_at_ceiling"]
    ["binding"]["h0.0375"]["worst"],
    "gate_FD_floor_at_B4_rung_C432_2_form": b4_floor_gate,
    "phase_FD_floor_C-432-2": floor_phase_c4322,
    "C-5_multiple_over_gate_floor": c5w / b4_floor_gate,
    "C-5_multiple_over_phase_floor": c5w / floor_phase_c4322,
    "C-5_own_gate_floor": c5_floor_own,
    "C-5_multiple_over_own_gate_floor": c5w / c5_floor_own,
    "phase_claimed_multiple": v432["raise_margin"]
    ["multiple_of_C-432-2_floor"],
    "B-4_worst_SEC_gate": b4w_gate,
    "B-4_multiple_over_gate_floor": b4w_gate / b4_floor_gate,
    "B-4_multiple_phase_record": c432["C-432-2"]
    ["B-4_margin_multiple_of_FD_floor_h0.0375"]}
tied = {}
for name in ("C-1", "C-4"):
    tied[name] = {
        "phase_worst": v432["subjects"][name]["anatomy_at_ceiling"]
        ["binding"]["h0.0375"]["worst"],
        "gate_worst": ga[name]["audit"]["h0.0375"]["worst"],
        "gate_legal": ga[name]["audit"]["legal_full_common_bars"]}
out["tied_subjects"] = tied

json.dump(out, open(f"{WP}/gate58/results/g58_repro.json", "w"), indent=1)
print(json.dumps({k: out[k] for k in ("C-432-5", "margins")}, indent=1))
print("search:", json.dumps(out["search"])[:600])
print("REPRO DONE")
