"""
g42_controls.py — Gate-42 controls: stored-bytes hash gate, the gate
builder's c = 0 reproduction (C-G1 equivalent), Minkowski anchor and the
beta = 0 static anchor (C-G4 equivalent). Writes
gate42/results/g42_controls.json.
"""
import hashlib, json, sys, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate42/work")
from g42_lib import (GradedBuilder, analytic_step_rho, wa, R1, R2, R_IN,
                     R_OUT, RHO0_NOMINAL, M_TARGET, DTYPE)

WP = "/home/hatch/workspace/warp-pilot"
PUBLISHED_SHA = "a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a"

out = {}
t0 = time.time()

# ---- stored bytes: the design vector, three copies ----
copies = [
    f"{WP}/phase50/procaccia/opt/optimal_shift_code/results/x_slp2.npy",
    f"{WP}/phase50/procaccia/cont/continuum_cert_code/x_slp2.npy",
    f"{WP}/phase50/procaccia/opt/optimal_shift_code/results/slp2.npy",
]
hashes = {}
for p in copies:
    hashes[p] = hashlib.sha256(open(p, "rb").read()).hexdigest()
out["hash_gate"] = {"copies": hashes,
                    "published_sha256": PUBLISHED_SHA,
                    "all_match": all(v == PUBLISHED_SHA for v in hashes.values())}

x = np.load(copies[0]).astype(DTYPE)
y_his = np.r_[np.zeros(8), x].astype(DTYPE)
out["y_his_sha256_float64"] = hashlib.sha256(y_his.tobytes()).hexdigest()

# ---- gate builder at c = 0 ----
b = GradedBuilder(y_his)
cr = b.chain_reads()
out["gate_chain_reads_c0"] = cr
out["graded_build_s"] = time.time() - t0

stored_graded = {"M": 6.112885737848813, "rho_max": 2.0204754599440912e-04,
                 "lambda": 0.2783957468415073, "k": 0.030277497148614742,
                 "int_F_over_r2": 33.02782905375493,
                 "a_Rin": -0.5847109564381374,
                 "M_unscaled_unit_rho0": 29873.19521865146,
                 "rho0": 0.00020462778397529235}
stored_gen = {"M": 6.112885737848849, "rho_max": 2.0204754599521463e-04,
              "lambda": 0.27839574684728247, "k": 0.030277497148878153,
              "int_F_over_r2": 33.02782905346759,
              "a_Rin": -0.5847109564395452}
paper = {"rho_max": 2.0204755e-4, "lambda": 0.27839575423,
         "k": 0.0302774968097, "int_F_over_r2": 33.0278294235,
         "a_Rin": -0.58471095644715723624}


def rel(a, ref):
    return abs(a - ref) / abs(ref)


out["vs_stored_graded_rel"] = {k: rel(cr[k], v) for k, v in stored_graded.items()
                               if k in cr}
out["vs_stored_genprocaccia_rel"] = {k: rel(cr[k], v) for k, v in stored_gen.items()}
out["vs_paper_rel"] = {k: rel(cr[k], v) for k, v in paper.items()}
out["stored_phase_CG1_rel"] = {"rho_max": 3.98672500613882e-12,
                               "lambda": 2.074441939180621e-11,
                               "k": 8.69988756461444e-12}

# ---- profile agreement vs the closed-form step density ----
r = b.rg
prof_gate = b.rho(r)
prof_exact = analytic_step_rho(r) * (cr["rho0"] / float(RHO0_NOMINAL))
# analytic_step_rho carries the nominal rho0; the builder's rho0 differs
# from nominal by the rescale ~1 + 1e-13, applied above for shape compare.
d = np.abs(prof_gate - prof_exact)
out["profile"] = {
    "max_abs_diff_over_rho_max": float(d.max() / cr["rho_max"]),
    "max_rel_diff_where_rho_ge_1e-3_peak": float(
        np.max(d[prof_exact >= 1e-3 * cr["rho_max"]]
               / prof_exact[prof_exact >= 1e-3 * cr["rho_max"]])),
}

# ---- Minkowski anchor ----
def mink(pts):
    P = len(pts)
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -1.0
    g[:, 1, 1] = g[:, 2, 2] = g[:, 3, 3] = 1.0
    return g

rng = np.random.default_rng(42)
pts_m = rng.normal(size=(50, 3)) * 5.0
mm = wa.audit(mink, pts_m, 0.0375)
out["minkowski_max_abs_That"] = float(np.max(np.abs(mm["That"])))

# ---- beta = 0 static anchor: auditor vs exact (rho, 0, r rho a'/2) ----
radii = [5.0, 8.0, 12.0, 15.0, 17.5, 20.0, 22.5, 25.0]
rows = []
gf0 = b.metric_factory(0.0)
for h in (0.0375, 0.01875):
    for rr in radii:
        pt = np.array([[0.0, rr, 0.0]])
        m1 = wa.audit(gf0, pt, h)
        That = m1["That"][0]
        rho_ex = float(b.rho(np.array([rr]))[0])
        pt_ex = float(rr * rho_ex * float(b.ap_of(np.array([rr]))[0]) / 2.0)
        ev = np.linalg.eigvalsh(That[1:, 1:])
        rows.append({"h": h, "r": rr, "rho_auditor": float(That[0, 0]),
                     "rho_exact": rho_ex,
                     "rho_rel_err": abs(float(That[0, 0]) - rho_ex) / rho_ex,
                     "pt_exact": pt_ex,
                     "p_abs_err": float(np.max(np.abs(ev - np.array([0.0, pt_ex, pt_ex]))))})
out["static_anchor_rows"] = rows
out["static_anchor_max"] = {
    "rho_rel_err_h0.0375": max(rw["rho_rel_err"] for rw in rows if rw["h"] == 0.0375),
    "p_abs_err_h0.0375": max(rw["p_abs_err"] for rw in rows if rw["h"] == 0.0375),
    "rho_rel_err_h0.01875": max(rw["rho_rel_err"] for rw in rows if rw["h"] == 0.01875),
    "p_abs_err_h0.01875": max(rw["p_abs_err"] for rw in rows if rw["h"] == 0.01875),
}
out["wall_s"] = time.time() - t0
json.dump(out, open(f"{WP}/gate42/results/g42_controls.json", "w"), indent=1)
print(json.dumps({k: out[k] for k in
                  ("hash_gate", "vs_stored_graded_rel", "vs_stored_genprocaccia_rel",
                   "vs_paper_rel", "profile", "minkowski_max_abs_That",
                   "static_anchor_max", "wall_s")}, indent=1))
print("construction_grid_n:", cr["construction_grid_n"])
