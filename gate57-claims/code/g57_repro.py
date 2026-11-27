"""
g57_repro.py — Gate-57 independent recomputation of Phase 416's
claims (ii), (iii), (iv) from the stored JSON records, with the
gate's own code (does not import the phase's checker):
  (ii)  fatness multiples: B-4's deciding margin over its own
        measured FD floor and over the C-416-3 floor
        (5.295791e-9, from p416_controls.json); A-6's multiple
        of the same floor recomputed.
  (iii) Arm A zero yield: A-6's hash == subject A-1's hash;
        every Arm A subject's stored legal ceiling; the arm's
        other subjects' ceiling range.
  (iv)  D-416-1 diagnostic: every Arm A subject's c idx 13
        coordinate and distance to the -2.25 bound, recomputed
        from the stored vectors.
Writes gate57/results/g57_repro.json.
"""
import json, hashlib
import numpy as np

WP = "/home/hatch/workspace/warp-pilot"
DTYPE = np.float64

v = json.load(open(f"{WP}/phase416/results/p416_verdicts.json"))
ctl = json.load(open(f"{WP}/phase416/results/p416_controls.json"))
subs = v["subjects"]
lc = v["legal_ceilings"]


def vhash(y):
    return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()


out = {}

# (ii) fatness
floor_c3 = ctl["C-416-3"]["measured_FD_floor_h0.0375"]
b4 = subs["B-4"]["anatomy_at_ceiling"]["binding"]["h0.0375"]
b4_worst = b4["worst"]; b4_floor = b4["floor_proxy"]
a6_worst = ctl["C-416-3"]["legal_rung"]["deciding_h0.0375"]["worst_h0.0375"]
out["fatness"] = {
    "C-416-3_floor": floor_c3,
    "B-4_worst_SEC": b4_worst, "B-4_own_FD_floor": b4_floor,
    "B-4_multiple_own_floor": b4_worst / b4_floor,
    "B-4_multiple_C-416-3_floor": b4_worst / floor_c3,
    "A-6_worst_SEC_C-416-3": a6_worst,
    "A-6_multiple_C-416-3_floor": a6_worst / floor_c3,
    "B-3_multiple_own_floor":
        subs["B-3"]["anatomy_at_ceiling"]["binding"]["h0.0375"]["worst"]
        / subs["B-3"]["anatomy_at_ceiling"]["binding"]["h0.0375"]["floor_proxy"],
    "B-5_multiple_own_floor":
        subs["B-5"]["anatomy_at_ceiling"]["binding"]["h0.0375"]["worst"]
        / subs["B-5"]["anatomy_at_ceiling"]["binding"]["h0.0375"]["floor_proxy"]}

# (iii) Arm A zero yield
armA = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6"]
out["armA"] = {
    "A-1_hash": vhash(subs["A-1"]["y"]),
    "A-1_hash_is_standing_A-6":
        vhash(subs["A-1"]["y"])
        == "6461827fac113c49f8f28aea04115df524446dbd44530b86f5e408e5d3c00039",
    "ceilings": {k: lc[k] for k in armA},
    "arm_max_ceiling": max(lc[k] for k in armA),
    "others_range": [min(lc[k] for k in armA[1:]),
                     max(lc[k] for k in armA[1:])]}

# (iv) D-416-1 diagnostic from stored vectors
diag = {}
for k in armA:
    c13 = float(np.asarray(subs[k]["y"], dtype=DTYPE)[13])
    diag[k] = {"c_idx13": c13, "distance_to_-2.25_bound": abs(c13 + 2.25)}
out["D-416-1"] = {"per_subject": diag,
                  "any_at_bound_within_0.01":
                      any(d["distance_to_-2.25_bound"] <= 0.01
                          for d in diag.values()),
                  "distance_range": [min(d["distance_to_-2.25_bound"]
                                         for d in diag.values()),
                                     max(d["distance_to_-2.25_bound"]
                                         for d in diag.values())]}

json.dump(out, open(f"{WP}/gate57/results/g57_repro.json", "w"), indent=1)
print(json.dumps(out, indent=1))
