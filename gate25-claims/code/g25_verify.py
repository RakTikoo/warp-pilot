#!/usr/bin/env python
"""
GATE-25 independent verification of Phase 253 / 257 spinor claims.

METHOD (deliberately different code path from the phases' builders):
  psi(x) and psibar(x) are built as EXPLICIT functions of x (complex arrays),
  derivatives are computed ANALYTICALLY mode-by-mode inside the field function
  (d_b psi = sum_j -i p_{j,b} c_j u_j exp(-i p_j.x)),
  and T_ab(x) is assembled directly from the symmetrised formula
    T_ab = (i/4)[ psibar gamma_(a D_b) psi - (D_(a psibar) gamma_b) psi ]
           - eta_ab * L ,   L = psibar (i gamma.D - m) psi
  with L evaluated honestly (not assumed zero).
Conventions: eta = diag(+1,-1,-1,-1), Dirac representation,
  p.x = E t - pvec . xvec,  p_b (covariant) = (E, -pvec).
No file from phase253/work, phase257/work, phase250/work or phase235 is
imported, copied or executed. Only stored data JSONs are read.
"""
import json, math
import numpy as np

BASE = "/home/hatch/workspace/warp-pilot/"
rng_global = np.random.default_rng(20261124)

# ---------------- gamma matrices, Dirac representation ----------------
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex); I2 = np.eye(2, dtype=complex)
gamma_up = [None] * 4   # gamma^mu
gamma_up[0] = np.block([[I2, Z2], [Z2, -I2]])
for i, s in enumerate([s1, s2, s3], start=1):
    gamma_up[i] = np.block([[Z2, s], [-s, Z2]])
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
gamma_lo = [ETA[a, a] * gamma_up[a] for a in range(4)]  # gamma_a = eta_aa gamma^a (no sum)

def cplx(pair):
    return complex(pair[0], pair[1])

def load_modes(mode_list):
    modes = []
    for md in mode_list:
        pvec = np.array(md["pvec"], dtype=float)
        u = np.array([cplx(z) for z in md["u"]], dtype=complex)
        c = cplx(md["c"])
        modes.append({"pvec": pvec, "u": u, "c": c})
    return modes

# ---------------- field function ----------------
def field(modes, m, x4):
    """Return psi, psibar, dpsi[b], dpsibar[a], L at spacetime point x4=(t,x,y,z).
    Derivatives analytic, mode by mode."""
    psi = np.zeros(4, dtype=complex)
    dpsi = np.zeros((4, 4), dtype=complex)      # dpsi[b, spinor]
    dpsibar = np.zeros((4, 4), dtype=complex)   # dpsibar[a, spinor] (row components)
    for md in modes:
        pvec = md["pvec"]; u = md["u"]; c = md["c"]
        E = math.sqrt(float(pvec @ pvec) + m * m)
        phase = E * x4[0] - float(pvec @ np.asarray(x4[1:], dtype=float))
        e_minus = np.exp(-1j * phase); e_plus = np.exp(+1j * phase)
        p_lo = np.array([E, -pvec[0], -pvec[1], -pvec[2]])  # covariant p_b
        psi += c * u * e_minus
        ubar = u.conj() @ gamma_up[0]   # ubar components (row)
        for b in range(4):
            dpsi[b] += (-1j * p_lo[b]) * c * u * e_minus
            dpsibar[b] += (+1j * p_lo[b]) * np.conj(c) * ubar * e_plus
    psibar = psi.conj() @ gamma_up[0]
    # L = psibar ( i gamma^mu d_mu psi - m psi )
    slash = np.zeros(4, dtype=complex)
    for mu in range(4):
        slash += gamma_up[mu] @ dpsi[mu]
    L = psibar @ (1j * slash - m * psi)
    return psi, psibar, dpsi, dpsibar, L

def T_of_x(modes, m, x4):
    psi, psibar, dpsi, dpsibar, L = field(modes, m, x4)
    T = np.zeros((4, 4), dtype=complex)
    for a in range(4):
        for b in range(4):
            # Symmetrisation as SUM (gamma_a D_b + gamma_b D_a), prefactor i/4.
            # This is the standard canonical-SET convention, equivalent to
            # (i/2) x averaged symmetrisation. NOTE: with AVERAGED symmetrisation
            # and prefactor i/4 every T value below is exactly HALF; that factor-2
            # convention split was found and is recorded in the results.
            term1 = (psibar @ gamma_lo[a] @ dpsi[b] + psibar @ gamma_lo[b] @ dpsi[a])
            term2 = (dpsibar[a] @ gamma_lo[b] @ psi + dpsibar[b] @ gamma_lo[a] @ psi)
            T[a, b] = 0.25j * (term1 - term2) - ETA[a, b] * L
    return T, L, psi

def mode_checks(modes, m):
    out = []
    for md in modes:
        pvec = md["pvec"]; u = md["u"]
        E_stored = math.sqrt(float(pvec @ pvec) + m * m)
        E = E_stored
        p_lo = np.array([E, -pvec[0], -pvec[1], -pvec[2]])
        # (pslash - m) u,  pslash = gamma^mu p_mu
        pslash = sum(gamma_up[mu] * p_lo[mu] for mu in range(4))
        resid = np.linalg.norm((pslash - m * np.eye(4)) @ u)
        out.append({
            "pvec": pvec.tolist(),
            "E_from_pvec": E,
            "onshell_resid_E2_minus_p2_minus_m2": E * E - float(pvec @ pvec) - m * m,
            "dirac_resid_norm": float(resid),
            "u_dag_u": float(np.real(u.conj() @ u)),
            "two_E": 2 * E,
            "u_dag_u_minus_2E": float(np.real(u.conj() @ u) - 2 * E),
            "p0_positive": bool(E > 0),
        })
    return out

def mixed_eigs(T):
    M = ETA @ T
    ev = np.linalg.eigvals(M)
    return ev

def sort_eigs(ev):
    # sort by (real, imag) descending real for reporting stability
    return sorted([complex(z) for z in ev], key=lambda z: (-z.real, -z.imag))

def Tkk(T, nhat):
    k = np.array([1.0, nhat[0], nhat[1], nhat[2]])
    return float(k @ T @ k)

RESULTS = {}

# ================= TASK 1: Phase 253 deciding config =================
p253 = json.load(open(BASE + "phase253/results/p2531_results.json"))
ver = p253["tierB_best"]["1.0"]["verification"]
modes253 = load_modes(ver["modes"])
m = 1.0
nhat = np.array([0.9999920898272356, 0.003925947046906336, 0.0006381400653280247])
# cross-check k* against p2502 site row
p2502 = json.load(open(BASE + "phase250/results/p2502_results.json"))
site = p2502["sites"]["worst_r12.84_b1.1"]
nhat2502 = np.array(site["nec_worst_spatial_dir"])
T_req = np.array(site["That"], dtype=float)

T253, L253, psi253 = T_of_x(modes253, m, np.zeros(4))
T253r = np.real(T253)
single = []
for j, md in enumerate(modes253):
    sc = sum(abs(x["c"]) ** 2 for x in modes253)
    one = [{"pvec": md["pvec"], "u": md["u"], "c": md["c"] / math.sqrt(abs(md["c"]) ** 2) * 1.0}]
    # renormalised single mode: |c|=1
    one[0]["c"] = complex(1.0, 0.0)
    Tj, _, _ = T_of_x(one, m, np.zeros(4))
    single.append({"mode": j, "Tkk_single_renorm_c1": Tkk(np.real(Tj), nhat),
                   "T_single": np.real(Tj).tolist()})
RESULTS["task1_phase253"] = {
    "mode_checks": mode_checks(modes253, m),
    "E_stored_in_json": [md.get("E") for md in ver["modes"]],
    "sum_c_sq_mine": float(sum(abs(x["c"]) ** 2 for x in modes253)),
    "sum_c_sq_claimed": ver["sum_c_sq"],
    "convention_note": "T assembled with (i/4) x UNNORMALISED symmetrisation (= standard canonical SET, (i/2) x averaged). With (i/4) x AVERAGED symmetrisation all T values are exactly half (Tkk=-5.439245950801301, rho=1.1201760181156213 for task 1).",
    "T_ab_mine": T253r.tolist(),
    "T_imag_maxabs": float(np.max(np.abs(np.imag(T253)))),
    "L_at_0": [float(np.real(L253)), float(np.imag(L253))],
    "Tkk_mine": Tkk(T253r, nhat),
    "Tkk_claimed": -10.878491901602604,
    "nhat_crosscheck_p2502_site": nhat2502.tolist(),
    "nhat_max_abs_diff_vs_registration": float(np.max(np.abs(nhat - nhat2502))),
    "rho_mine_T00": float(T253r[0, 0]),
    "rho_claimed": 2.2403520362312377,
    "psi_dag_psi_mine": float(np.real(psi253.conj() @ psi253)),
    "psi_dag_psi_claimed": ver["psi_dagger_psi"],
    "single_modes": single,
}

# ================= TASK 2: Phase 257 N=6 best fit =================
bf = json.load(open(BASE + "phase257/work/p257_bestfit.json"))
modes257 = load_modes(bf["modes"])
T257, L257, psi257 = T_of_x(modes257, m, np.zeros(4))
T257r = np.real(T257)
sumc2_257 = float(sum(abs(x["c"]) ** 2 for x in modes257))
ev257 = mixed_eigs(T257r)
R_p2502 = float(np.linalg.norm(T257r - T_req))
# leg1 json stores no fitted tensor (only R / eigs / tkk); record that fact
leg1 = json.load(open(BASE + "phase257/results/p257_leg1_results.json"))
leg1_has_tensor = any(isinstance(v, list) and len(v) == 4 and isinstance(v[0], list)
                      for v in leg1.get("leg1_fits", {}).get("N6_constr", {}).values())
RESULTS["task2_phase257"] = {
    "mode_checks": mode_checks(modes257, m),
    "sum_c_sq_mine": sumc2_257,
    "sum_c_sq_claimed": 0.007884,
    "bestfit_R_claimed": bf["R"],
    "T_ab_mine": T257r.tolist(),
    "T_imag_maxabs": float(np.max(np.abs(np.imag(T257)))),
    "L_at_0": [float(np.real(L257)), float(np.imag(L257))],
    "T_req_from_p2502": T_req.tolist(),
    "T_req_frobenius_mine": float(np.linalg.norm(T_req)),
    "T_req_frobenius_claimed": 2.3978336134611576e-3,
    "R_vs_Treq_p2502": R_p2502,
    "leg1_json_stores_fitted_tensor": bool(leg1_has_tensor),
    "leg1_N6_constr_R_claimed": leg1["leg1_fits"]["N6_constr"]["R"],
    "mixed_eigs_mine": [[z.real, z.imag] for z in sort_eigs(ev257)],
    "mixed_eigs_claimed": [[0.000676, 0.000820], [0.000676, -0.000820],
                            [0.000113, 0.0], [0.001042, 0.0]],
    "mixed_eigs_leg1_N6_constr_exact": leg1["leg1_fits"]["N6_constr"]["segre"]["eigs"],
    "rho_mine": float(T257r[0, 0]),
    "rho_req": -9.800905387216327e-05,
    "rho_unit_mine_div_sumc2": float(T257r[0, 0] / sumc2_257),
    "rho_unit_claimed": -0.0124,
    "rho_unit_leg2_exact": -0.012431243730330888,
    "Tkk_mine": Tkk(T257r, nhat),
    "Tkk_req_claimed": -0.0038017605291582623,
    "Tkk_Treq_mine": Tkk(T_req, nhat),
}

# ================= TASK 3: type scan spot check =================
def build_u(pvec, m, chi):
    """Standard Dirac u: u = ( sqrt(E+m) chi ; (sigma.p)/sqrt(E+m) chi ), |chi|=1
    => u+u = 2E, (pslash-m)u = 0."""
    E = math.sqrt(float(pvec @ pvec) + m * m)
    sp = s1 * pvec[0] + s2 * pvec[1] + s3 * pvec[2]
    top = math.sqrt(E + m) * chi
    bot = (sp @ chi) / math.sqrt(E + m)
    return np.concatenate([top, bot]), E

rng = np.random.default_rng(777)
n_complex = 0; n_tot = 60; details = []
for trial in range(n_tot):
    N = int(rng.integers(2, 6))
    modes = []
    for _ in range(N):
        pmag = rng.uniform(0.05, 6.0)
        d = rng.normal(size=3); d /= np.linalg.norm(d)
        pvec = pmag * d
        z = rng.normal(size=2) + 1j * rng.normal(size=2); z /= np.linalg.norm(z)
        u, E = build_u(pvec, 1.0, z)
        c = rng.normal() + 1j * rng.normal()
        modes.append({"pvec": pvec, "u": u, "c": c})
    T, _, _ = T_of_x(modes, 1.0, np.zeros(4))
    Tr = np.real(T)
    ev = mixed_eigs(Tr)
    scale = max(1e-30, float(np.max(np.abs(ev))))
    has_pair = bool(np.max(np.abs(np.imag(ev))) > 1e-6 * scale)
    n_complex += int(has_pair)
    details.append({"N": N, "has_complex_pair": has_pair,
                    "max_imag_over_scale": float(np.max(np.abs(np.imag(ev))) / scale)})
RESULTS["task3_type_scan"] = {
    "n_draws": n_tot, "complex_pair_count": n_complex,
    "fraction": n_complex / n_tot,
    "claimed_phase": "40/300 = 0.1333",
    "tolerance_rule": "max|Im eig| > 1e-6 * max|eig|",
    "spinor_construction": "u=(sqrt(E+m) chi, (sigma.p)chi/sqrt(E+m)), chi uniform on C^2 sphere",
    "details": details,
}

# ================= TASK 5: patch spot check =================
# N=6 config as stored (already at fitted scale, sum|c|^2 = 0.007884...)
dirs = []
for ax in range(3):
    for sgn in (+1, -1):
        v = np.zeros(3); v[ax] = sgn; dirs.append(v)
for i in range(3):
    for j in range(i + 1, 3):
        for s1_ in (+1, -1):
            for s2_ in (+1, -1):
                v = np.zeros(3); v[i] = s1_; v[j] = s2_; dirs.append(v / np.linalg.norm(v))
v = np.ones(3) / math.sqrt(3)
for s in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]:
    dirs.append(np.array(s, dtype=float) / math.sqrt(3))
dirs.append(nhat.copy())
rngp = np.random.default_rng(42)
for _ in range(24):
    d = rngp.normal(size=3); dirs.append(d / np.linalg.norm(d))
grid = np.linspace(-math.pi, math.pi, 7)
nec_min = 1e300; nec_arg = None; frob_max = 0.0; frob_at = None; rho_min = 1e300; rho_max = -1e300
for gx in grid:
    for gy in grid:
        for gz in grid:
            x4 = np.array([0.0, gx, gy, gz])
            Tx, _, _ = T_of_x(modes257, 1.0, x4)
            Txr = np.real(Tx)
            rho_min = min(rho_min, float(Txr[0, 0])); rho_max = max(rho_max, float(Txr[0, 0]))
            fd = float(np.linalg.norm(Txr - T_req))
            if fd > frob_max: frob_max, frob_at = fd, x4.tolist()
            for d in dirs:
                val = Tkk(Txr, d)
                if val < nec_min: nec_min, nec_arg = val, (x4.tolist(), d.tolist())
# denser random refinement (same field function, same fitted scale)
rngr = np.random.default_rng(1234)
rdirs = [nhat.copy()]
for _ in range(79):
    d = rngr.normal(size=3); rdirs.append(d / np.linalg.norm(d))
nec_min_r = 1e300; nec_arg_r = None
for _ in range(1500):
    x4 = np.array([0.0] + list(rngr.uniform(-math.pi, math.pi, size=3)))
    Tx, _, _ = T_of_x(modes257, 1.0, x4)
    Txr = np.real(Tx)
    for d in rdirs:
        val = Tkk(Txr, d)
        if val < nec_min_r: nec_min_r, nec_arg_r = val, (x4.tolist(), d.tolist())
RESULTS["task5_patch"] = {
    "nec_min_random_refinement": float(nec_min_r),
    "nec_arg_random_refinement": nec_arg_r,
    "random_refinement_note": "1500 uniform random points in [-pi,pi]^3 at t=0, 80 null directions (k* + 79 random)",
    "scale_note": "stored bestfit used as-is: sum|c|^2 = %.15g (fitted scale, = s2)" % sumc2_257,
    "grid": "7x7x7 over [-pi,pi]^3 at t=0, 51 null directions (axes/diagonals/corners/k*/24 random)",
    "nec_min_mine": float(nec_min),
    "nec_min_claimed_leg2_patch_s2": -0.022314545788106002,
    "nec_arg": nec_arg,
    "max_frobenius_departure_from_Treq_on_grid": float(frob_max),
    "max_departure_at": frob_at,
    "rho_min_on_grid": float(rho_min), "rho_max_on_grid": float(rho_max),
    "leg2_rho_range_claimed": [-9.800905387228425e-05, 0.09208694440704122],
}

with open(BASE + "gate25/work/g25_verify_results.json", "w") as f:
    json.dump(RESULTS, f, indent=1)

# ---- console summary ----
t1 = RESULTS["task1_phase253"]
print("TASK1 sumc2", t1["sum_c_sq_mine"], "Tkk", t1["Tkk_mine"], "vs -10.878491901602604",
      "rho", t1["rho_mine_T00"], "psidagpsi", t1["psi_dag_psi_mine"], "L", t1["L_at_0"],
      "imagmax", t1["T_imag_maxabs"])
for mc in t1["mode_checks"]:
    print("  mode resid %.3e normdiff %.3e" % (mc["dirac_resid_norm"], mc["u_dag_u_minus_2E"]))
for s in t1["single_modes"]:
    print("  single mode", s["mode"], "Tkk", s["Tkk_single_renorm_c1"])
t2 = RESULTS["task2_phase257"]
print("TASK2 sumc2", t2["sum_c_sq_mine"], "R", t2["R_vs_Treq_p2502"], "Tkk", t2["Tkk_mine"],
      "rho", t2["rho_mine"], "rho_unit", t2["rho_unit_mine_div_sumc2"], "L", t2["L_at_0"])
print("  eigs mine", t2["mixed_eigs_mine"])
for mc in t2["mode_checks"]:
    print("  mode resid %.3e normdiff %.3e" % (mc["dirac_resid_norm"], mc["u_dag_u_minus_2E"]))
print("TASK3", RESULTS["task3_type_scan"]["complex_pair_count"], "/", n_tot)
print("TASK5 nec_min", RESULTS["task5_patch"]["nec_min_mine"], "frob_max", RESULTS["task5_patch"]["max_frobenius_departure_from_Treq_on_grid"],
      "rho range", RESULTS["task5_patch"]["rho_min_on_grid"], RESULTS["task5_patch"]["rho_max_on_grid"])
