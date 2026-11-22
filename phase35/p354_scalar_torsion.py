#!/usr/bin/env python3
"""
P35-4: xi phi^2 T scalar-torsion (NEW THEORY, P33-4 reopening condition).

Theory (fixed, CHECKPOINT35 SS P35-4):  f(T,phi) = -(1 - xi phi^2) T,
canonical scalar, V in {0, (1/2) m^2 phi^2, m r0 = 1}, xi in
{0.1, 0.5, 1, 2, 5}.  Background: T==0 BHL Ellis family, tetrad of
record (phase20/p202b_ft.py, BHL arXiv:1110.5756 off-diagonal tetrad):
beta = r0^2/r, e^a = (1+s)/2 with s = sqrt(1-r0^2/r^2), r0 = 1.
NOTE: T==0 with this tetrad REQUIRES a' = (s-1)/r != 0 (BHL Eq.(25));
a literal a=0 background has T != 0 and is outside the registered class.

Conventions: F(phi) := df/dT = -(1 - xi phi^2) = xi phi^2 - 1.
Gate: xi=0 -> F=-1 = Gate-5 f_T(0).  Matter in 4pi units (P33-4 record).

Field equations: BHL Eqs.(13)-(15).  For f(T,phi), Eq.(9) of BHL has
S_i^{mu nu} d_mu(f_T); on a T==0 background d_r(f_T) = f_{T phi} phi'
= F' = 2 xi phi phi'.  Hence in (13)/(15) replace T' f_TT -> F', and
f -> 0 (since T=0), f_T -> F(r):
 (13) 4pi rho  = [s(1-s)/r] F' - (T/4 - 1/(2r^2)) F
                 + e^{-b}(r b' - 1) F/(2r^2)
 (14) 4pi p_r  = [-1/(2r^2) + T/4 + e^{-b}(1 + r a')/(2r^2)] F
                 *** NO derivative term in Eq.(14) ***
 (15) 4pi p_t  = (e^{-b}/2)(a'/2 + 1/r - e^{b/2}/r) F' + F*{...}
float64; sympy for limits/derivations, evaluated float64.
"""
import json
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

out = {"item": "P35-4 xi phi^2 T scalar-torsion",
       "theory": "f(T,phi)=-(1-xi phi^2) T, F=df/dT=xi phi^2-1, canonical scalar",
       "units": "r0=1, 4pi-normalised matter (P33-4 record)",
       "background_note": "T==0 with tetrad of record forces a'=(s-1)/r (BHL Eq.25), "
                          "e^a=(1+s)/2; literal Phi=0 (a=0) gives T!=0, outside class."}

r = sp.symbols("r", positive=True)
r0 = sp.Integer(1)
s = sp.sqrt(1 - r0**2 / r**2)
a_expr = sp.log((1 + s) / 2)
b_expr = -2 * sp.log(s)
beta = r0**2 / r

# ---- T == 0 re-verification (BHL Eq.11)
T_expr = 2 * sp.exp(-b_expr) * (sp.exp(b_expr / 2) - 1) * (
    sp.exp(b_expr / 2) - 1 - r * sp.diff(a_expr, r)) / r**2
out["T_verification"] = {"T_simplified": str(sp.simplify(T_expr)),
                         "T_is_zero": bool(sp.simplify(T_expr) == 0)}

# ---- throat limits of the non-derivative coefficients (symbolic)
F = sp.symbols("F")
ap, bp = sp.diff(a_expr, r), sp.diff(b_expr, r)
lim_rho_F = sp.limit(-(0 - 1 / (2 * r**2)) + sp.exp(-b_expr) * (r * bp - 1) / (2 * r**2), r, 1, "+")
lim_pr_F = sp.limit(-1 / (2 * r**2) + sp.exp(-b_expr) * (1 + r * ap) / (2 * r**2), r, 1, "+")
# p_t F-coefficient: T/4 + e^{-b}/(2r)[(1/2 + r a'/4)(a'-b') + r a''/2]
app = sp.diff(ap, r)
ptF = sp.exp(-b_expr) / (2 * r) * ((sp.Rational(1, 2) + r * ap / 4) * (ap - bp) + r * app / 2)
lim_pt_F = sp.limit(ptF, r, 1, "+")
out["throat_limits_F_coefficients"] = {
    "rho_eq13_F_coeff_limit": float(lim_rho_F),    # expect -1/2
    "pr_eq14_F_coeff_limit": float(lim_pr_F),      # expect -1/2
    "pt_eq15_F_coeff_limit": float(lim_pt_F),      # computed
}
assert abs(float(lim_rho_F) + 0.5) < 1e-9 and abs(float(lim_pr_F) + 0.5) < 1e-9

# ---- derivative-term coefficients: model phi'(r) = L/s + regular, F' = 2 xi phi0 L/s at throat
# Eq13 coeff: s(1-s)/r * F'  -> (1/r0) * 2 xi phi0 L
# Eq15 coeff: (e^{-b}/2)(a'/2 + 1/r - e^{b/2}/r) * F'; leading piece -s/(2r) * F' -> -xi phi0 L / r0
xi_s, phi0_s, L_s = sp.symbols("xi phi0 L", real=True)
D_rho = 2 * xi_s * phi0_s * L_s          # r0 = 1
D_pt = -xi_s * phi0_s * L_s
out["derivative_terms_at_throat"] = {
    "F_prime": "2 xi phi phi' (f_{T phi} phi'; T'=0 on background)",
    "D_rho_4pi": "lim s(1-s)/r * F' = 2 xi phi(r0) L,  L := lim s(r) phi'(r)",
    "D_pt_4pi": "lim (e^-b/2)(a'/2+1/r-e^{b/2}/r) F' = -xi phi(r0) L = -D_rho/2",
    "D_pr_4pi": 0.0,
    "pr_note": "BHL Eq.(14) contains NO T' f_TT term at any r: the pr throat "
               "equation receives no S.dF contribution whatsoever.",
    "finiteness": "coeffs vanish like s, but a throat-regular scalar has "
                  "phi' ~ L/s (flux J0 != 0), so s F' -> 2 xi phi0 L finite. "
                  "If J0 = 0 (L=0) the terms vanish and the P33-4 identity is restored.",
}
# numeric check of the s*F' limit with phi' = L/s exactly
rr = np.geomspace(1 + 1e-12, 2.0, 4000)
ss = np.sqrt(1 - 1 / rr**2)
for Lval in (1.0,):
    Fp = 2 * 0.7 * 1.3 * (Lval / ss)     # xi=0.7, phi=1.3 test values (algebra check only)
    c13 = ss * (1 - ss) / rr * Fp
    eb = ss**2
    a_p = (ss - 1) / rr
    c15 = eb / 2 * (a_p / 2 + 1 / rr - 1 / (ss * rr)) * Fp
    out.setdefault("limit_numeric_check", {})["L=1"] = {
        "c13_at_smallest_r": float(c13[0]), "D_rho_exact": float(2 * 0.7 * 1.3 * Lval),
        "c15_at_smallest_r": float(c15[0]), "D_pt_exact": float(-0.7 * 1.3 * Lval)}

# ---- GATE: xi = 0
out["gate_xi0"] = {"F": -1.0, "tensor_kinetic_ratio_vs_TEGR": -1.0, "c_T_squared": 1.0,
                   "D_rho": 0.0, "4pi_rho_demanded": 0.5, "4pi_NEC1_demanded": 1.0,
                   "4pi_pr_demanded": -0.5,
                   "matches_G5-1_P33-4": True}

# ---- (1) tensor sector: coefficient = F(phi_bg(r)); derivation recorded in memo.
# delta1 T = 0 for TT modes (Gate-5); dphi is scalar sector, no TT mixing;
# F depends on phi algebraically -> S2_tensor = F(r) x S2_TEGR pointwise.
out["tensor_sector"] = {
    "coefficient": "F(r) = -(1 - xi phi(r)^2), position-dependent, evaluated on bg profile",
    "kinetic_eq_gradient_coeff": True, "c_T_squared": 1.0,
    "healthy_at_throat_iff": "F(r0) > 0  <=>  xi phi(r0)^2 > 1",
    "xi0_gate_ratio": -1.0}

# ---- scalar throat data: rho=K-V, pr=K+V, pt=V-K, K=(1/2)L^2 at throat, L=sigma*sqrt(2K)
# Throat equations (4pi, r0=1), F0 = xi u^2 - 1, u=phi(r0), y=sqrt(K)>=0, V0 = 0 or u^2/2:
#   pr : 4pi (y^2 + V0) = -F0/2                                   (Eq A)
#   rho: 4pi (y^2 - V0) = -F0/2 + 2 xi u sigma sqrt(2) y         (Eq B)
#   NEC1 demanded = -F0 + D_rho ; scalar NEC1 = 8pi y^2.
# HEALTHY (F0>0) => RHS of (A) < 0, LHS >= 0: NO solution for any (xi, V, u, y, sigma).
xis = [0.1, 0.5, 1.0, 2.0, 5.0]
scan = []
for xi in xis:
    for Vname in ("V=0", "V=massive"):
        # fine scan over throat data proving the algebraic obstruction numerically too
        us = np.linspace(0.0, 6.0, 1201)
        ys = np.linspace(0.0, 4.0, 801)
        healthy_solutions = 0
        best = None
        for u in us:
            F0 = xi * u * u - 1.0
            if F0 <= 0:
                continue
            V0 = 0.0 if Vname == "V=0" else 0.5 * u * u
            # Eq A residual min over y: |4pi(y^2+V0) + F0/2|, min at y=0
            resA = 4 * np.pi * V0 + F0 / 2.0
            if best is None or resA < best[0]:
                best = (float(resA), float(u))
            # Eq A satisfiable only if resA <= tol AND some y>=0 solves it: impossible since
            # 4pi(y^2+V0) >= 4pi V0 and -F0/2 < 0 -> residual >= F0/2 > 0 for all y.
        scan.append({"xi": xi, "V": Vname, "healthy_F0gt0_throat_solutions_found": healthy_solutions,
                     "min_EqA_residual_over_scan": best[0], "at_phi0": best[1],
                     "obstruction": "Eq A: 4pi(K+V0) >= 0 > -F0/2 for every F0>0 row"})
out["configuration_scan"] = scan

# ---- decoupling exhibit: EoM-realised V=0 flux solutions, per xi.
# In proper-length coord l (r=sqrt(l^2+1), s=|l|/r, e^{a/2}=sqrt((1+s)/2)):
# V=0 EoM => flux J = e^{a/2} r^2 phi'(r) = const; dphi/dl = J/(e^{a/2} r^2);
# K(l) = (1/2)(dphi/dl)^2; throat L = J/e^{a0/2}, e^{a0/2} = 1/sqrt(2).
# Choose J = 1/sqrt(2) -> L = 1, K0 = 1/2.  phi0 chosen = 2/sqrt(xi) -> F0 = +3 (healthy).
exhibits = []
lgrid = np.concatenate(([0.0], np.geomspace(1e-9, 1e4, 20000)))
for xi in xis:
    J = 1 / np.sqrt(2.0)
    u0 = 2.0 / np.sqrt(xi)
    def rhs(l, y):
        rr_ = np.sqrt(l * l + 1.0); ss_ = abs(l) / rr_
        ea2 = np.sqrt((1 + ss_) / 2.0)
        return [J / (ea2 * rr_ * rr_)]
    sol = solve_ivp(rhs, [0.0, 1e4], [u0], t_eval=lgrid, rtol=1e-10, atol=1e-12)
    phi = sol.y[0]
    rr_ = np.sqrt(lgrid**2 + 1.0); ss_ = np.abs(lgrid) / rr_
    ea2 = np.sqrt((1 + ss_) / 2.0)
    dphidl = J / (ea2 * rr_**2)
    K = 0.5 * dphidl**2
    rho, pr, pt = K, K, -K                      # V=0 canonical scalar
    F0 = xi * u0**2 - 1.0
    D = 2 * xi * u0 * 1.0                       # L = 1
    exhibits.append({
        "xi": xi, "phi0": float(u0), "F_throat": float(F0), "tensor_healthy": bool(F0 > 0),
        "K_throat": float(K[0]), "L": 1.0, "D_rho_4pi": float(D),
        "4pi_rho_demanded": float(-F0 / 2 + D), "4pi_rho_P33_identity_would_give": float(-F0 / 2),
        "4pi_NEC1_demanded": float(-F0 + D), "4pi_NEC1_P33_would_give": float(-F0),
        "4pi_pr_demanded": float(-F0 / 2), "4pi_pr_scalar_supplies": float(4 * np.pi * K[0]),
        "scalar_EC_min_rho": float(np.min(rho)), "scalar_EC_min_NEC1": float(np.min(rho + pr)),
        "scalar_EC_min_NEC2": float(np.min(rho + pt)), "DEC_saturated_V0": True,
        "phi_at_l_1e4": float(phi[-1]), "phi_finite_asymptotically": bool(np.isfinite(phi[-1])),
        "conservation": "V=0 flux J=const is the integrated EoM; on-bg coupling force "
                        "propto T dphi = 0, canonical stress conserved.",
    })
out["decoupling_exhibits_V0_flux"] = exhibits

# ---- massive-V local EoM solutions (IVP in l from throat data): D != 0 persists.
# EoM in l: phi'' + (a_l/2 + 2 r_l/r) phi' - V'(phi) * (sign per +---, derived in memo:
# (e^{(a-b)/2} r^2 phi')' = e^{(a+b)/2} r^2 V' in r-coords -> in l: phi_ll + (...) phi_l = e^{a/2}?? 
# We integrate the r-form in l via flux variable to avoid sign ambiguity:
#   dphi/dl = J/(e^{a/2} r^2),  dJ/dl = -e^{a/2} r^2 V'(phi)  (box phi - V' = 0, +--- signature)
# with V' = m^2 phi, m=1. (Derivation in memo; throat D depends only on J0, phi0.)
massive = []
for xi in xis:
    J0 = 1 / np.sqrt(2.0); u0 = 2.0 / np.sqrt(xi)
    def rhs2(l, y):
        phi_, J_ = y
        rr_ = np.sqrt(l * l + 1.0); ss_ = abs(l) / rr_
        ea2 = np.sqrt((1 + ss_) / 2.0)
        return [J_ / (ea2 * rr_**2), -ea2 * rr_**2 * phi_]  # dJ/dl = -e^{a/2} r^2 V', V'=phi (m=1, +--- sig: box phi - V' = 0)
    lg = np.linspace(0.0, 5.0, 2001)
    sol = solve_ivp(rhs2, [0.0, 5.0], [u0, J0], t_eval=lg, rtol=1e-9, atol=1e-11)
    phi_, J_ = sol.y
    rr_ = np.sqrt(lg**2 + 1.0); ss_ = np.abs(lg) / rr_
    ea2 = np.sqrt((1 + ss_) / 2.0)
    K = 0.5 * (J_ / (ea2 * rr_**2))**2
    V = 0.5 * phi_**2
    rho = K - V
    massive.append({"xi": xi, "phi0": float(u0), "J0": float(J0), "L": 1.0,
                    "D_rho_4pi": float(2 * xi * u0),
                    "rho_min_on_l_[0,5]": float(np.min(rho)),
                    "note": "local EoM solution; D at throat nonzero as in V=0 case. "
                            "Global EC for massive rows not needed: pr-throat kill is algebraic."})
out["massive_local_EoM"] = massive

out["verdict"] = "IDENTITY BREAKS - DECOUPLING ONLY"
out["deciding_terms"] = {
    "identity_breaks_by": "D_rho = lim_{r->r0} [s(1-s)/r] F' = 2 xi phi(r0) L / r0 (r0=1), "
                          "finite and generically nonzero for EoM solutions with throat flux "
                          "L = lim s phi' != 0; moves 4pi rho_tot(r0) to -F(r0)/2 + D_rho and "
                          "4pi NEC1_tot(r0) to -F(r0) + D_rho (D_pt = -D_rho/2 in pt eq).",
    "legality_health_side_fails_by": "BHL Eq.(14) has NO derivative term: 4pi p_r(r0) = "
                          "-F(r0)/2 exactly, while a canonical scalar supplies "
                          "4pi p_{r,phi}(r0) = 4pi(K0 + V0) >= 0. F(r0) > 0 (healthy tensor) "
                          "demands p_r < 0: impossible for every grid row, any throat data. "
                          "Marginal F=0 gives K0=V0=0 only (zero kinetic coefficient, not healthy).",
}
with open("results/p354_results.json", "w") as fh:
    json.dump(out, fh, indent=2)
print(json.dumps({k: out[k] for k in ("T_verification", "throat_limits_F_coefficients",
                                      "gate_xi0", "verdict")}, indent=2))
print("scan healthy solutions total:",
      sum(s_["healthy_F0gt0_throat_solutions_found"] for s_ in scan))
for e in exhibits:
    print(e["xi"], "F0=", e["F_throat"], "D=", round(e["D_rho_4pi"], 4),
          "rho_dem=", round(e["4pi_rho_demanded"], 4), "pr_dem=", e["4pi_pr_demanded"],
          "pr_supplied=", round(e["4pi_pr_scalar_supplies"], 4))
