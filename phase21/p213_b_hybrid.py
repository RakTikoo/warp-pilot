"""
P21-3(b) HYBRID METRIC-PALATINI f(R,Rcal) WORMHOLE AUDIT
Paper: Capozziello, Harko, Koivisto, Lobo, Olmo,
"Wormholes supported by hybrid metric-Palatini gravity",
PRD 86, 127504 (2012), arXiv:1209.5862.
Action (1): S = (1/2k^2) int sqrt-g [R + f(Rcal)] + S_m.
Scalar-tensor form (paper): S = (1/2k^2) int sqrt-g
  [(1+phi)R + (3/2phi)(dphi)^2 - V(phi)] + S_m.
Solution II (paper Sec.IV.B, eqs.29-33): Phi=Phi0 (alpha=0, const),
b(r)=r0 (beta=0), phi=phi0 (r0/r)^3 (gamma=3),
V(r) eq.(31), V(phi) eq.(32), printed rho/p_r/p_t after eq.(32).
Claim audited: throat NEC for matter, rho(r0)+p_r(r0) = (phi0-2)/(2 k^2 r0^2) > 0
for phi0 > 2, with rho(r0)=3 phi0/(5 k^2 r0^2) > 0.
Units: kappa^2 = r0 = 1.  u = r0/r in (0,1].
"""
import json, os
import numpy as np
import sympy as sp

OUT = os.path.join(os.path.dirname(__file__), "results", "p213_results.json")
res = {}
phi0 = 3.0   # > 2, the paper's NEC branch; results for phi0=5 also recorded

def profiles(r, ph0):
    u = 1.0/r
    rho = 21*ph0/10 * u**5 * (1 - (5/7)*u)
    pr = -u**3 * (1 + (3*ph0/5)*u**2*(1 - (5/6)*u))
    pt = 0.5*u**3 * (1 + (9*ph0/5)*u**2*(1 - (10/9)*u))
    return rho, pr, pt

r = np.geomspace(1.0, 1e4, 4000)
for ph0 in (3.0, 5.0):
    rho, pr, pt = profiles(r, ph0)
    combos = {"rho": rho, "rho+pr": rho+pr, "rho+pt": rho+pt,
              "rho+pr+2pt": rho+pr+2*pt, "rho-|pr|": rho-np.abs(pr), "rho-|pt|": rho-np.abs(pt)}
    entry = {"throat_values": {k: float(v[0]) for k, v in combos.items()},
             "minima_full_domain": {k: float(v.min()) for k, v in combos.items()}}
    # first NEC1 sign crossing
    nec1 = rho + pr
    ix = np.where(np.diff(np.sign(nec1)))[0]
    entry["rho+pr_first_crossing_r_over_r0"] = float(r[ix[0]]) if len(ix) else None
    dec_t = rho - np.abs(pt)
    ix2 = np.where(np.diff(np.sign(dec_t)))[0]
    entry["rho-|pt|_first_crossing_r_over_r0"] = float(r[ix2[0]]) if len(ix2) else None
    res[f"matter_EC_phi0={ph0}"] = entry
res["throat_NEC1_formula_check_phi0=3"] = {
    "printed_formula_(phi0-2)/2": (3.0-2)/2,
    "computed_rho+pr_at_throat": float((profiles(np.array([1.0]), 3.0)[0] + profiles(np.array([1.0]), 3.0)[1])[0])}

# ---- effective sector: T_eff = G/(kappa^2) for b=r0, Phi=const ---------------
rho_e = np.zeros_like(r)                       # b'=0
pr_e = -1.0/r**3                                # -b/r^3
pt_e = 0.5/r**3                                 # (b-b'r)/(2 r^3)
res["effective_EC"] = {
    "rho_eff": 0.0, "rho_eff+pr_eff_at_throat": float((rho_e + pr_e)[0]),
    "rho_eff+pr_eff_min": float((rho_e + pr_e).min()),
    "note": "effective NEC violated everywhere (rho_eff+p_r,eff = -u^3 < 0): the flare-out is carried by the effective sector, as the paper intends"}

# ---- closure: field equations (15)-(17) with Phi'=0, b=r0, b'=0 --------------
# phi = phi0 u^3 ; V from eq.(31); derivatives analytic.
def field_eq_residuals(rr, ph0):
    u = 1.0/rr
    phi = ph0*u**3
    phip = -3*ph0*u**3/rr            # dphi/dr = phi0 * (-3) u^3 / r ... (u=r0/r, r0=1)
    phipp = 12*ph0*u**3/rr**2
    V = (9*ph0/10)*u**5*(5*u - 3)    # eq.(31) with r0=1
    rho_p, pr_p, pt_p = profiles(np.array([rr]), ph0)
    rho_p, pr_p, pt_p = float(rho_p[0]), float(pr_p[0]), float(pt_p[0])
    b, bp = 1.0, 0.0
    # eq.(15): k^2 rho = b'/r^2 (1+phi) - (1-b/r)[phi'' - 3 phi'^2/(4 phi)]
    #                    + phi'/(2r)(b' + 3b/r - 4) - V/2
    rhs15 = bp/rr**2*(1+phi) - (1-b/rr)*(phipp - 3*phip**2/(4*phi)) \
        + phip/(2*rr)*(bp + 3*b/rr - 4) - V/2
    # eq.(16): k^2 p_r = [-b/r^3 + 2 Phi'/r (1-b/r)](1+phi)
    #                    + phi'(Phi' + 2/r + 3 phi'/(4 phi))(1-b/r) + V/2 , Phi'=0
    rhs16 = (-b/rr**3)*(1+phi) + phip*(2/rr + 3*phip/(4*phi))*(1-b/rr) + V/2
    # eq.(17): k^2 p_t = [(Phi''+Phi'^2+Phi'/r)(1-b/r) + (b-b'r)/(2r^3)(1+r Phi')](1+phi)
    #                    + [phi''+phi' Phi' + 3phi'^2/(4phi)](1-b/r)
    #                    + phi'/r (1 - (b+r b')/(2r)) + V/2
    rhs17 = ((b-bp*rr)/(2*rr**3))*(1+phi) + (phipp + 3*phip**2/(4*phi))*(1-b/rr) \
        + phip/rr*(1 - (b+rr*bp)/(2*rr)) + V/2
    return {"eq15_rho": rhs15 - rho_p, "eq16_pr": rhs16 - pr_p, "eq17_pt": rhs17 - pt_p,
            "rhs15": rhs15, "rho_printed": rho_p, "rhs16": rhs16, "pr_printed": pr_p,
            "rhs17": rhs17, "pt_printed": pt_p}

for rr in (1.0, 1.5, 2.0, 5.0):
    res[f"closure_eqs15-17_r={rr}"] = {k: float(v) for k, v in field_eq_residuals(rr, phi0).items()}
# anatomy of the eq.(17) residual: it equals 2(1-b/r)*3phi'^2/(4phi) at every r,
# i.e. eq.(17) as printed under-weights the 3phi'^2/(4phi) sub-term by a factor 3
for rr in (1.5, 2.0, 5.0):
    u = 1.0/rr; phi = phi0*u**3; phip = -3*phi/rr
    pred = 2*(1-u)*3*phip**2/(4*phi)
    res[f"eq17_residual_anatomy_r={rr}"] = {
        "residual": float(field_eq_residuals(rr, phi0)["eq17_pt"]),
        "predicted_2(1-b/r)*3phip2/(4phi)": float(pred)}

# ---- closure: Klein-Gordon eq.(11) -------------------------------------------
# -Box phi + (dphi)^2/(2phi) + phi[2V-(1+phi)V_phi]/3 = phi k^2 T/3
# metric: ds^2=-dt^2+dr^2/(1-1/r)+r^2 dOm^2 (Phi=const absorbed)
# Box phi = (1-b/r)[phi'' + phi'(2/r + (b-b'r)/(2r(r-b)))]  (Phi'=0)
# V(phi) eq.(32): V = (9 phi0/2)(phi/phi0)^{5/3}[(phi/phi0)^{1/3}-3/5]  (r0=1)
def kg_residual(rr, ph0):
    u = 1.0/rr
    phi = ph0*u**3
    phip = -3*phi/rr; phipp = 12*phi/rr**2
    b, bp = 1.0, 0.0
    box = (1-b/rr)*(phipp + phip*(2/rr + (b-bp*rr)/(2*rr*(rr-b))))
    dphi2 = (1-b/rr)*phip**2
    y = phi/ph0
    V = (9*ph0/2)*y**(5/3)*(y**(1/3) - 3/5)
    Vphi = (15/2)*y**(2/3)*(y**(1/3) - 3/5) + (3/2)*y   # dV/dphi of eq.(32), y=phi/phi0
    rho_p, pr_p, pt_p = profiles(np.array([rr]), ph0)
    T = float(-rho_p[0] + pr_p[0] + 2*pt_p[0])
    lhs = -box + dphi2/(2*phi) + phi*(2*V - (1+phi)*Vphi)/3
    rhs = phi*T/3
    Tst = float((4*V + 9*ph0*u**3*(1-2*u))/(2*rr**2))
    return {"KG_lhs": float(lhs), "KG_rhs_phi_k2T_over3": float(rhs),
            "KG_residual": float(lhs-rhs),
            "KG_residual_using_paper_stated_T": float(lhs - phi*Tst/3),
            "T_from_printed_profiles": T,
            "T_paper_stated_formula": float((4*V + 9*ph0*u**3*(1-2*u))/(2*rr**2))}
for rr in (1.5, 2.0, 5.0):
    res[f"closure_KG_eq11_r={rr}"] = kg_residual(rr, phi0)

# V(r) eq.(31) vs V(phi(r)) eq.(32): identity check
rr = 2.0; u = 1/rr; y = u**3
res["V31_vs_V32_at_r=2"] = {"V31": float((9*phi0/10)*u**5*(5*u-3)),
                            "V32": float((9*phi0/2)*y**(5/3)*(y**(1/3)-3/5))}
# eq.(30) as printed vs derivative of eq.(31)
rr3 = 3.0; u3 = 1/rr3
Vp31 = float((9*phi0/10) * (30*u3**5 - 15*u3**4) * (-u3/rr3))   # d/dr [u^5(5u-3)] chain
res["eq30_check_at_r=3"] = {
    "dV31_dr": Vp31,
    "eq30_printed_lhs_2r0^3_Vprime_plus_27phi0_(r/r0)^6(1-2u)":
        float(2*Vp31 + 27*phi0*(rr3**6)*(1-2*u3)),
    "eq30_with_(r0/r)^6_and_sign_flip": float(2*Vp31 - 27*phi0*(u3**6)*(1-2*u3)),
    "note": "eq.(30) as printed does not integrate to eq.(31): sign and (r/r0)^6 vs (r0/r)^6 both differ; logged, not repaired"}

# ---- conservation of matter: nabla T (must vanish; matter minimally coupled) -
def conservation(rr, ph0):
    h = 1e-5*rr
    rp_, prp_, ptp_ = profiles(np.array([rr]), ph0)
    rp2, prp2, ptp2 = profiles(np.array([rr+h]), ph0)
    rp1, prp1, ptp1 = profiles(np.array([rr-h]), ph0)
    prprime = float((prp2[0]-prp1[0])/(2*h))
    # Phi'=0: nabla_mu T^mu_r = p_r' + 2(p_r-p_t)/r
    return {"pr_prime": prprime, "cons_residual": float(prprime + 2*(float(prp_[0])-float(ptp_[0]))/rr)}
for rr in (1.5, 2.0, 5.0, 20.0):
    res[f"conservation_r={rr}"] = conservation(rr, phi0)

# ---- scalar ghost health (enter at the ACTION) --------------------------------
# Jordan action: (1+phi)R + (3/2phi)(dphi)^2 - V.  Set Phi=1+phi (nonminimal
# coupling field). Kinetic term = -Z(Phi)(dPhi)^2 with Z = -3/(2(Phi-1)).
# Einstein-frame (dPhi)^2 coefficient = -Z/Phi - 3/(2 Phi^2)
#   = 3/(2 Phi^2 (Phi-1)) = 3/(2 phi (1+phi)^2).
# With -+++ signature a POSITIVE (dPhi)^2 coefficient = negative time-kinetic
# energy = ghost. Healthy iff coefficient < 0 iff phi in (-1,0).
phi_s = sp.symbols("phi", real=True)
KEF = 3/(2*phi_s*(1+phi_s)**2)
res["ghost_EF_kinetic_coeff"] = {
    "formula": "K_EF(phi) = 3/(2 phi (1+phi)^2), coefficient of (dPhi)^2 in Einstein-frame Lagrangian",
    "at_phi_throat_phi0=3": float(KEF.subs(phi_s, 3.0)),
    "at_phi_r=2_phi0=3": float(KEF.subs(phi_s, 3.0/8)),
    "sign_for_phi>0": "positive => GHOST (negative time-kinetic term)",
    "healthy_window": "-1 < phi < 0 (with 1+phi > 0), disjoint from the phi0 > 2 throat-NEC branch",
    "two_omega_plus_3_equivalent": "-3/phi (pointwise, from omega_eff = -3(1+phi)/(2phi))"}
# scalar's own stress-energy share at throat: T_eff - T/(1+phi) decomposition
# rho_scalar-part via eq.(10): the bracket terms; report rho_eff-rho relation
res["scalar_sector_at_throat"] = {
    "rho_matter": float(profiles(np.array([1.0]), phi0)[0][0]),
    "rho_eff": 0.0,
    "note": "rho_eff=0 at throat while rho_matter=3phi0/5>0: the scalar/curvature sector supplies -rho_matter/(1+phi) net in the tt equation; its NEC share is what carries the flare-out"}

data = {}
if os.path.exists(OUT):
    data = json.load(open(OUT))
data["b_hybrid_capozziello2012"] = res
json.dump(data, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1))
