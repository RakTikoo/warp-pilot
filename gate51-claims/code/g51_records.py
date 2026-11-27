"""
g51_records.py — Gate-51 record checks (no tensor machinery):
  * hash gate: RW-5, RW-1 (phase392 verdicts) and E2-1 (phase391
    verdicts) re-hashed as sha256 of the float64 tobytes against
    their stored records;
  * claim (b): RW-5 interiority — every coordinate of the stored
    vector against the registered R-W box (CHECKPOINT392 Arm R-W:
    c1, c9 in [-3.375, 3.375]; other c in [-2.25, 2.25];
    a in [-8, 8] (a12 in [-12, 12]); q in [0.25, 3.0];
    r_m in [11, 23]), distances to the nearest edge, and the
    phase's own stored box_edges field cross-checked;
  * claim (c): Arm T flatness from the stored DE state
    (best_hist over gens 0..118, n_evals, done flag) and the
    identity of the arm's home-ceiling holder T-4 with E2-1
    (hash equality);
  * claim (d): Arm R-16 truncation facts from the stored DE
    state and lineage records (gen, done=False, n_evals, wall,
    stop string, best static at the gen-0 level, final-population
    beta_crit mean recomputed from the stored population).
Writes gate51/results/g51_records.json. VM frame of record.
"""
import hashlib, json
import numpy as np

WP = "/home/hatch/workspace/warp-pilot"
out = {}

def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()

v392 = json.load(open(f"{WP}/phase392/results/p392_verdicts.json"))
v391 = json.load(open(f"{WP}/phase391/results/p391_verdicts.json"))
search = json.load(open(f"{WP}/phase392/results/p392_search.json"))

# ---- hash gate ----
hashes = {}
for name, rec in [("RW-5", v392["subjects"]["RW-5"]),
                  ("RW-1", v392["subjects"]["RW-1"]),
                  ("T-4", v392["subjects"]["T-4"]),
                  ("E2-1", v391["subjects"]["E2-1"])]:
    h = sha(rec["y"])
    hashes[name] = {"computed": h,
                    "stored": rec["vector_sha256_float64_tobytes"],
                    "match": h == rec["vector_sha256_float64_tobytes"]}
out["hashes"] = hashes

# ---- claim (b): RW-5 interiority ----
rw5 = v392["subjects"]["RW-5"]
y = np.asarray(rw5["y"], dtype=np.float64)
bd = rw5["box_definition"]
bounds = ([tuple(b) for b in bd["c_bounds"]]
          + [tuple(b) for b in bd["a_bounds"]]
          + [tuple(bd["q"]), tuple(bd["r_m"])])
labels = ([f"c{j+1}" for j in range(12)] + [f"a{j+1}" for j in range(12)]
          + ["q", "r_m"])
rows = []
for lab, val, (lo, hi) in zip(labels, y, bounds):
    rows.append({"coord": lab, "value": float(val), "lo": float(lo),
                 "hi": float(hi), "dist_lo": float(val - lo),
                 "dist_hi": float(hi - val),
                 "min_dist": float(min(val - lo, hi - val)),
                 "on_edge": bool(val == lo or val == hi),
                 "inside": bool(lo < val < hi)})
out["rw5_interiority"] = {
    "all_strictly_inside": all(r["inside"] for r in rows),
    "any_on_edge": any(r["on_edge"] for r in rows),
    "min_edge_distance": min(r["min_dist"] for r in rows),
    "min_edge_coord": min(rows, key=lambda r: r["min_dist"])["coord"],
    "c1": rows[0], "c9": rows[8],
    "c1_beyond_old_box": bool(y[0] > 2.25),
    "phase_stored_box_edges": rw5["box_edges"],
    "rows": rows,
}

# ---- claim (c): Arm T flatness ----
tst = json.load(open(f"{WP}/phase392/results/p392_pool_t_de_state.json"))
bh = tst["best_hist"]
vals = [e["best"] for e in bh]
out["arm_t"] = {
    "gen_final": tst["gen"], "done": tst["done"],
    "n_evals": tst["n_evals"], "elapsed_s": tst["elapsed_s"],
    "best_hist_n": len(bh),
    "best_hist_gens": [bh[0]["gen"], bh[-1]["gen"]],
    "best_hist_all_equal": all(v == 0.191796875 for v in vals),
    "best_hist_max": max(vals), "best_hist_min": min(vals),
    "best_beta_crit": tst["best_beta_crit"],
    "lineage_de": {k: search["t_lineage"]["de"][k]
                   for k in ("generations_completed", "beta_crit_evals",
                             "done_flag", "stop",
                             "best_beta_crit_screening_union_set")},
    "t4_is_e2_1_by_hash": hashes["T-4"]["computed"] == hashes["E2-1"]["computed"],
    "t4_ceiling": v392["subjects"]["T-4"]["legal_ceiling"],
    "t2_ceiling": v392["subjects"]["T-2"]["legal_ceiling"],
}

# ---- claim (d): Arm R-16 truncation ----
rst = json.load(open(f"{WP}/phase392/results/p392_pool_r16_de_state.json"))
rbh = rst["best_hist"]
rvals = [e["best"] for e in rbh]
pop_bc = np.asarray(rst["beta_crit"], dtype=np.float64)
out["arm_r16"] = {
    "gen_final": rst["gen"], "done": rst["done"],
    "n_evals": rst["n_evals"], "elapsed_s": rst["elapsed_s"],
    "best_beta_crit": rst["best_beta_crit"],
    "best_hist_all_equal_gen0_level": all(v == rvals[0] for v in rvals),
    "best_hist_gen0": rvals[0],
    "final_population_n": int(pop_bc.size),
    "final_population_beta_crit_mean_recomputed": float(pop_bc.mean()),
    "lineage_de": {k: search["r16_lineage"]["de"][k]
                   for k in ("generations_completed", "beta_crit_evals",
                             "cap_min", "done_flag", "stop",
                             "best_beta_crit_screening_union_set")},
    "registered_cap_min": 120,
    "stopped_before_cap": bool(rst["elapsed_s"] < 120 * 60),
}

json.dump(out, open(f"{WP}/gate51/results/g51_records.json", "w"), indent=1)
print(json.dumps({k: (v if not isinstance(v, dict) else
                      {kk: vv for kk, vv in v.items() if kk != "rows"})
                  for k, v in out.items()}, indent=1)[:3000])
print("RECORDS DONE")
