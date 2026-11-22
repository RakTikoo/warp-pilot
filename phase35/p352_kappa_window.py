#!/usr/bin/env python3
"""
P35-2 -- The |kappa| window for the EiBI MIXTURE row.
float64. Level: q-curvature / PROFILE level (P35-1 Step B output not
landed at run time -- phase35/results/ empty of P35-1 files -- so no
reconstructed metric is used; stated in the memo).

GATE (Phase 23 fluid row): tidal bar = traveller-frame gradient
<= 4.905 s^-2 (= 1 g across a 2 m traveller; GBAR of p233_ledger.py)
at v = 0.1 c, evaluated as gradient = c^2 * Cmax / |kappa|, where
Cmax = max(|radial|, |boosted transverse|) dimensionless tidal
coefficient per |kappa| at the throat, x = r0^2/|kappa| = 0.5 kept
along the scaling family (r0 = sqrt(x |kappa|)). Phase 23 fluid:
Cmax = 1 (radial R_tltl = +1 per |kappa|, Phi_ll = -1, f'(r0)=
2(1-x)/r0, Phi_r(r0) = -sqrt(2) in |kappa|=1 units).
Then |kappa|* = c^2 Cmax / GBAR, r0* = sqrt(0.5 |kappa|*).

MIXTURE COEFFICIENT (profile level): for a Morris-Thorne metric
ds^2 = -e^{2Phi} dt^2 + dr^2/F + r^2 dOmega^2, F = 1 - b/r,
at the throat (F=0, Phi_l = 0):
  radial R_tltl = -(F'(r0)/2) * Phi'(r0)      [Phi_ll = F'/2 Phi']
  transverse (boosted, v=0.1c) = gamma^2 v^2 * (-(F'(r0)/(2 r0)))
                                [R_lthlth = -F'/(2 r0)]
with F'(r0) = 2(1-x)/r0 (Shaikh Eq.41 flare value, throat-algebra
in x only) and Phi'(r0) for the mixture taken from the P33-3
construction: Phi' solved from fluid-2 conservation,
  Phi'(r0) = [w/(1+w)] * 2 (2-f) / r0   (analytic, |kappa|=1 units;
  verified in-run against phase33/results/p333_results.json).
Gate column f=0 uses Phase 23's own Phi_r = -sqrt(2) (the P33
Phi is undefined at f=0 -- fluid 2 absent; the mixture branch is
discontinuous there, stated in the memo).
Sign check (P13-3): f=0 -> C_rad = -(1.41421/2)*(-1.41421) = +1
exactly the Phase-23 fluid value; w=0 -> Phi'=0 -> C_rad = 0.
"""
import json
import numpy as np

C_LIGHT = 299792458.0
GBAR = 4.905
V = 0.1
GAMMA2 = 1.0 / (1.0 - V**2)
X = 0.5
R0D = float(np.sqrt(X))          # r0 in |kappa|=1 units
FPRIME = 2.0 * (1.0 - X) / R0D   # 1.41421 (1/length, dimless units)
BOUND_CARRIED = 1e8              # Feng et al. Buchdahl, kappa>0 only

out = {"item": "P35-2 mixture |kappa| window", "float": "float64",
       "level": "q-curvature/profile level (no P35-1 Step B output "
                "landed at run time)",
       "tidal_bar": {"definition": "traveller-frame tidal gradient "
                     "<= 4.905 s^-2 (1 g across 2 m) at v=0.1c; "
                     "gradient = c^2*Cmax/|kappa|; Cmax = max(|radial|, "
                     "|gamma^2 v^2 R_lthlth|) at throat; scaling family "
                     "x = r0^2/|kappa| = 0.5",
                     "GBAR_s-2": GBAR, "v_over_c": V}}

# ---------------- GATE: Phase 23 fluid row ----------------
phi_r_gate = -np.sqrt(2.0)
C_gate = -(FPRIME / 2.0) * phi_r_gate
kap_gate = C_LIGHT**2 * C_gate / GBAR
r0_gate = np.sqrt(X * kap_gate)
stored = {"r0star_m": 95716358.48670936, "kapstar_m2": 1.832324256391251e16,
          "Cmax": 0.999999854268535}
out["gate_phase23_fluid"] = {
    "Cmax_recomputed": float(C_gate), "Cmax_stored": stored["Cmax"],
    "kapstar_recomputed_m2": float(kap_gate),
    "kapstar_stored_m2": stored["kapstar_m2"],
    "kapstar_rel_err": float(abs(kap_gate - stored["kapstar_m2"]) / stored["kapstar_m2"]),
    "r0star_recomputed_m": float(r0_gate), "r0star_stored_m": stored["r0star_m"],
    "r0star_rel_err": float(abs(r0_gate - stored["r0star_m"]) / stored["r0star_m"]),
    "gradient_at_1m_recomputed_s-2": float(C_LIGHT**2 * C_gate / (1.0 / R0D)**2),
    "gradient_at_1m_stored_s-2": 4.493775238799545e16,
    "PASS_le_1pct": bool(abs(kap_gate - stored["kapstar_m2"]) / stored["kapstar_m2"] <= 0.01
                         and abs(r0_gate - stored["r0star_m"]) / stored["r0star_m"] <= 0.01)}
print("GATE:", out["gate_phase23_fluid"])

# ---------------- verify P33 Phi'(r0) formula ----------------
with open("../phase33/results/p333_results.json") as fh:
    p333 = json.load(fh)
ver = {}
for key, row in p333["two_fluid_grid"].items():
    if row.get("Phi_prime_throat") is None:
        continue
    f, w = row["f_throat"], row["w"]
    pred = (w / (1.0 + w)) * 2.0 * (2.0 - f) / R0D if w > 0 else 0.0
    ver[key] = {"stored": row["Phi_prime_throat"], "formula": float(pred),
                "abs_err": float(abs(pred - row["Phi_prime_throat"]))}
maxerr = max(v["abs_err"] for v in ver.values())
out["phiprime_formula_vs_p333_json"] = {"max_abs_err": float(maxerr), "n_rows": len(ver)}
print("Phi' formula max err vs P333 JSON:", maxerr, "rows:", len(ver))
assert maxerr < 1e-12

# ---------------- COMPUTATION 1: mixture grid ----------------
Ctrans = GAMMA2 * V**2 * (FPRIME / (2.0 * R0D))   # = 0.010101..., per |kappa|
grid = {}
for f in (0.0, 0.5, 0.6, 0.75, 0.9):
    for w in (0.0, 1.0 / 3.0, 0.5, 1.0):
        if f == 0.0:
            phi_p, Crad = phi_r_gate, C_gate   # Phase-23 gate column
        else:
            phi_p = (w / (1.0 + w)) * 2.0 * (2.0 - f) / R0D
            Crad = -(FPRIME / 2.0) * phi_p
        Cmax = max(abs(Crad), Ctrans)
        kap_star = C_LIGHT**2 * Cmax / GBAR
        r0_star = np.sqrt(X * kap_star)
        # |kappa| p_t,tot(r0) signed (kappa=-1): -f(1-f+w); |kappa| p_t = +f(1-f+w)
        grid[f"f={f}_w={w:.4f}"] = {
            "f": f, "w": w, "Phi_prime_r0_dimless": float(phi_p),
            "abs_kappa_pt_tot_r0": float(f * (1.0 - f + w)),
            "kappa_pt_tot_r0_signed": float(-f * (1.0 - f + w)),
            "C_radial_per_abs_kappa": float(Crad),
            "C_transverse_boosted_per_abs_kappa": float(-Ctrans),
            "Cmax": float(Cmax),
            "deciding_component": "radial" if abs(Crad) >= Ctrans else "transverse",
            "kapstar_m2": float(kap_star), "r0star_m": float(r0_star),
            "x_at_r0star": float(r0_star**2 / kap_star),
            "ratio_kapstar_over_1e8": float(kap_star / BOUND_CARRIED),
            "gap_orders_vs_1e8": float(np.log10(kap_star / BOUND_CARRIED))}
out["mixture_grid"] = grid
for k, v in grid.items():
    print(k, "Crad=%+.4f Cmax=%.4f kap*=%.3e r0*=%.3e ratio=%.3e (%.2f orders)"
          % (v["C_radial_per_abs_kappa"], v["Cmax"], v["kapstar_m2"],
             v["r0star_m"], v["ratio_kapstar_over_1e8"], v["gap_orders_vs_1e8"]))

pass_rows = {k: v for k, v in grid.items() if v["f"] >= 0.5}
out["verdict_tests"] = {
    "min_ratio_pass_rows": float(min(v["ratio_kapstar_over_1e8"] for v in pass_rows.values())),
    "max_ratio_pass_rows": float(max(v["ratio_kapstar_over_1e8"] for v in pass_rows.values())),
    "all_pass_rows_ratio_ge_1e6": bool(all(v["ratio_kapstar_over_1e8"] >= 1e6
                                          for v in pass_rows.values())),
    "x_lt_1_all_rows": bool(all(v["x_at_r0star"] < 1 for v in grid.values()))}

# ---------------- COMPUTATION 2 (numeric part): decomposition ----
# fluid gap: log10(1.8323e8) = 8.263 orders.
fluid_gap_orders = float(np.log10(stored["kapstar_m2"] / BOUND_CARRIED))
out["gap_decomposition_fluid_baseline"] = {
    "total_orders": fluid_gap_orders,
    "(a)_row_coefficient": "C enters kappa* linearly: changing C from 1 to "
        "Cmax(f,w) moves the gap by log10(Cmax) orders: mixture range "
        "log10(Cmax) in [-1.996, +0.176]; coefficient can remove at most "
        "~2.0 orders (w=0 rows, transverse floor) and can add 0.18.",
    "(b)_bound_branch": "Feng-Geng-Luo 1810.06753 (Phase 3's Buchdahl "
        "source): text restricts to kappa>0 ('we will only focus on the "
        "case of kappa>0', Sec.IIA) and the 1e8 figure requires a FUTURE "
        "~3 Msun NS (abstract/conclusions: typical NS gives 1e9; 1e8 only "
        "if a 3 Msun NS 'is observed in the future'). As published it "
        "constrains kappa<0 NOT AT ALL. Sign-blind alternative in the "
        "literature: Avelino 2012 existence-of-NS / fundamental-length "
        "l_f = sqrt(|kappa|) argument, quoted by Sham et al. as "
        "|8 pi kappa rho0| <~ 0.1 -- an |kappa| bound of the same 1e8 "
        "order. So factor (b) moves APPLICABILITY, not the order of "
        "magnitude: 0 orders of the numeric gap, all of its branch status.",
    "(c)_scaling": "kappa* = c^2 Cmax / GBAR is forced by dimensions: "
        "tidal gradient ~ c^2/|kappa| at fixed x, so r0* = sqrt(x kappa*) "
        "~ sqrt(|kappa|). The remaining ~8.3 orders (fluid) / ~6.3-8.4 "
        "orders (mixture) are (c): no coefficient or branch factor in "
        "the audit touches the sqrt scaling."}
print("fluid gap orders:", fluid_gap_orders)

with open("results/p352_results.json", "w") as fh:
    json.dump(out, fh, indent=2)
print("WROTE results/p352_results.json")
