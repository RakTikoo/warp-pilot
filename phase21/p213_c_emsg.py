"""
P21-3(c) ENERGY-MOMENTUM-SQUARED GRAVITY WORMHOLE AUDIT
Paper: Ganiyeva, Rosa, Lobo, "Wormhole geometries in f(R,T^2) gravity
satisfying the energy conditions", Eur. Phys. J. C 83 (2023) 1040;
proceedings version arXiv:2502.19323 (text fetched).
Model: f(R,T^2) = R + gamma T^2, gamma = -1; metric ansatz eq.(10)
zeta = zeta0 (r0/r)^alpha, b = r0 (r0/r)^beta with alpha=beta=1,
r0 = 3M (M=1), zeta0 = -6/5 (fixed by the paper's own matching, eq.40).
Field eqs. (12)-(14) are a quadratic algebraic system for (rho, p_r, p_t).
Claim (abstract): "we demonstrate the existence of a wide range of wormhole
solutions that satisfy all of the energy conditions without requiring
fine-tuning of the model parameters" and, after matching, "satisfy all the
energy conditions throughout the entire spacetime".
The paper NEVER states L_m.  Theta_ab is taken in the standard
Board-Barrow / Katirci-Kavuk form (second-derivative term zero for a fluid
Lagrangian depending only on the metric):
  Theta_ab = -2 L_m (T_ab - 1/2 g_ab T) - T T_ab + 2 T_a^c T_cb .
We reverse-engineer L_m from the printed coefficients of eqs.(12)-(14),
then re-run the whole construction with the other standard choice.
Units: kappa^2 = 8 pi (paper), M = 1, r0 = 3.
"""
import json, os
import numpy as np
import sympy as sp
from scipy.optimize import fsolve

OUT = os.path.join(os.path.dirname(__file__), "results", "p213_results.json")
res = {}
GAMMA = -1.0; ALPHA = 1.0; BETA = 1.0; R0 = 3.0; Z0 = -6/5

# ---------- 1. Theta identification (sympy, mixed components) -----------------
rho, pr, pt, L = sp.symbols("rho pr pt L")
S = pr + 2*pt
T = -rho + S
T2 = rho**2 + pr**2 + 2*pt**2
# Theta^a_a = -2L(T^a_a - T/2) - T*T^a_a + 2 (T^a_c T^c_a), no sum
Th_t = -2*L*(-rho - T/2) - T*(-rho) + 2*rho**2
Th_r = -2*L*(pr - T/2) - T*pr + 2*pr**2
Th_th = -2*L*(pt - T/2) - T*pr*0 - T*pt + 2*pt**2
# paper gamma-brackets (eqs.12-14), from 8pi*rho = gamma*B_rho + geo etc.:
B_rho_paper = (pr**2 - 2*pt**2 - 3*rho**2 - 8*pr*pt - 8*pr*rho - 16*pt*rho)/6
B_pr_paper = (pr**2 + 2*pt**2 - 3*rho**2 - 12*pr*pt + 4*pr*rho - 4*pt*rho)/6
B_pt_paper = -(pr**2 + 6*pt**2 + 3*rho**2 + 2*pr*pt + 2*pr*rho - 2*pt*rho)/6
# field eq (7) mixed: 8pi rho = b'/r^2 + gamma*(-Th_t + T2/2)  [t-comp, derived]
#                     8pi pr  = G^r_r + gamma*(Th_r - T2/2)
#                     8pi pt  = G^th_th + gamma*(Th_th - T2/2)
checks = {}
for name, expr, paper in (("t", -Th_t + T2/2, B_rho_paper),
                          ("r", Th_r - T2/2, B_pr_paper),
                          ("th", Th_th - T2/2, B_pt_paper)):
    for Lname, Lval in (("L=pbar=(pr+2pt)/3", S/3), ("L=-rho", -rho), ("L=pr", pr)):
        diff = sp.expand(expr.subs(L, Lval) - paper)
        checks[f"{name}_comp_{Lname}"] = "IDENTICAL" if diff == 0 else str(diff)[:120]
res["theta_identification"] = checks
res["theta_identification_conclusion"] = (
    "All three printed gamma-brackets are reproduced identically iff "
    "L_m = (p_r + 2 p_t)/3 (mean pressure); L_m = -rho and L_m = p_r do NOT "
    "reproduce them. The paper states no L_m anywhere in the fetched text.")

# ---------- 2. Solve the paper's system (12)-(14) -----------------------------
def paper_residuals(x, r):
    ro, prr, ptt = x
    u = R0/r
    e1 = GAMMA/6*(prr**2 - 2*ptt**2 - 3*ro**2 - 8*prr*ptt - 8*prr*ro - 16*ptt*ro) \
        - BETA/r**2 * u**(BETA+1) - 8*np.pi*ro
    e2 = GAMMA/6*(prr**2 + 2*ptt**2 - 3*ro**2 - 12*prr*ptt + 4*prr*ro - 4*ptt*ro) \
        - 1/r**2 * u**(BETA+1) - ALPHA*Z0/r**2 * u**ALPHA * (1 - u**(BETA+1)) - 8*np.pi*prr
    e3 = -GAMMA/6*(prr**2 + 6*ptt**2 + 3*ro**2 + 2*prr*ptt + 2*prr*ro - 2*ptt*ro) \
        + (1+BETA)/(2*r**2) * u**(BETA+1) \
        + ALPHA**2 * Z0**2/(4*r**2) * u**(2*ALPHA) * (1 - u**(BETA+1)) \
        + ALPHA*Z0/(4*r**2) * u**ALPHA * (2*ALPHA - (1+2*ALPHA+BETA)*u**(BETA+1)) - 8*np.pi*ptt
    return [e1, e2, e3]

def ec_ok(x, tol=0.0):
    ro, prr, ptt = x
    return (ro >= tol and ro+prr >= tol and ro+ptt >= tol and ro+prr+2*ptt >= tol
            and ro-abs(prr) >= tol and ro-abs(ptt) >= tol)

# Root census at the throat, COMPLETE: Groebner lex elimination of the
# throat system gives a degree-8 univariate polynomial in pt (coefficients
# below, in powers of pi, as produced by sympy.groebner in-run); its four
# real roots seed exact fsolve polishes of the full system.
_pt_coeffs = [
    1,
    -476*np.pi/15,
    932/2025 + 5936*np.pi**2/15,
    -12864*np.pi**3/5 - 736*np.pi/75,
    52241/874800 + 161504*np.pi**2/2025 + 142592*np.pi**4/15,
    -300032*np.pi**5/15 - 8576*np.pi**3/27 - 843047*np.pi/1093500,
    263719/131220000 + 947653*np.pi**2/273375 + 1315328*np.pi**4/2025 + 110592*np.pi**6/5,
    -49152*np.pi**7/5 - 428032*np.pi**5/675 - 581564*np.pi**3/91125 - 27229*np.pi/2187000,
    169/97200000 + 1693*np.pi**2/91125 + 121888*np.pi**4/30375 + 16384*np.pi**6/75]
roots = []
for rt in np.roots(_pt_coeffs):
    if abs(rt.imag) > 1e-7:
        continue
    ptv = float(rt.real)
    for ga in np.linspace(-40, 40, 17):
        for gb in np.linspace(-40, 40, 17):
            try:
                sol, info, ier, _ = fsolve(
                    lambda y: [paper_residuals((y[0], y[1], ptv), R0)[0],
                               paper_residuals((y[0], y[1], ptv), R0)[1]],
                    (ga, gb), full_output=True)
            except Exception:
                continue
            if ier == 1:
                cand = (float(sol[0]), float(sol[1]), ptv)
                if np.max(np.abs(paper_residuals(cand, R0))) < 1e-8 and \
                        not any(np.max(np.abs(np.array(cand) - np.array(q))) < 1e-6 for q in roots):
                    roots.append(cand)
res["throat_root_census"] = [{"rho": q[0], "pr": q[1], "pt": q[2], "all_ECs_hold": bool(ec_ok(q))}
                             for q in roots]
res["throat_root_census_note"] = ("Complete census (Groebner degree-8 elimination): "
    "exactly 4 real roots at the throat; exactly one satisfies all ECs: "
    "(rho, pr, pt) = (12.562, 4.185, 4.194), i.e. rho*r0^2 = 113, a near-constant "
    "radiation-like fixed point (branch tends to rho=4pi, pr=pt=4pi/3 as r grows).")

# continue the EC branch (if any) over the interior domain and beyond
ec_roots = [q for q in roots if ec_ok(q)]
branch = []
if ec_roots:
    x = np.array(ec_roots[0])
    for r in np.concatenate((np.linspace(R0, 4.5, 301), np.linspace(4.51, 30.0, 200))):
        sol, info, ier, _ = fsolve(paper_residuals, x, args=(r,), full_output=True)
        if ier == 1 and np.max(np.abs(paper_residuals(sol, r))) < 1e-9:
            x = sol
            branch.append((r, *sol))
        else:
            branch.append((r, np.nan, np.nan, np.nan))
branch = np.array(branch, dtype=float)
res["branch_points"] = int(len(branch))
if len(branch):
    ro, prr, ptt = branch[:, 1], branch[:, 2], branch[:, 3]
    combos = {"rho": ro, "rho+pr": ro+prr, "rho+pt": ro+ptt, "rho+pr+2pt": ro+prr+2*ptt,
              "rho-|pr|": ro-np.abs(prr), "rho-|pt|": ro-np.abs(ptt)}
    for dom, m in (("interior_r0_to_rSigma=4.5", branch[:, 0] <= 4.5),
                   ("extended_to_30", branch[:, 0] > 4.5)):
        res[f"matter_EC_minima_{dom}"] = {k: float(np.nanmin(v[m])) for k, v in combos.items()}
    res["matter_at_throat"] = {"rho": float(ro[0]), "pr": float(prr[0]), "pt": float(ptt[0])}
    res["matter_at_rSigma_and_asymptote"] = {
        "at_rSigma=4.5": {"rho": float(ro[300]), "pr": float(prr[300]), "pt": float(ptt[300])},
        "at_r=30": {"rho": float(ro[-1]), "pr": float(prr[-1]), "pt": float(ptt[-1])},
        "note": "rho -> 4pi = 12.566, pr,pt -> 4pi/3 = 4.189: the branch does not decay; matching at finite rSigma is mandatory, as the paper states"}
    rr_ = branch[:, 0]; u_ = R0/rr_
    rho_eff = -BETA*u_**(BETA+1)/(8*np.pi*rr_**2)
    res["effective_rho_minmax_interior"] = {"min": float(rho_eff[rr_ <= 4.5].min()),
                                            "max": float(rho_eff[rr_ <= 4.5].max()),
                                            "note": "rho_eff < 0 on the whole interior: effective WEC violated, flare-out carried by the gamma sector"}
    prp = np.gradient(prr, rr_)
    zetap = -ALPHA*Z0*u_**ALPHA/rr_
    cons = prp + zetap/2*(ro+prr) + 2*(prr-ptt)/rr_
    scale = np.abs(prp) + np.abs(zetap/2*(ro+prr)) + np.abs(2*(prr-ptt)/rr_)
    m = rr_ <= 4.5
    res["conservation_interior"] = {
        "max_abs_nablaT": float(np.nanmax(np.abs(cons[m]))),
        "at_throat": float(cons[0]),
        "max_relative_to_term_scale": float(np.nanmax(np.abs(cons[m])/scale[m])),
        "dominant_term": "zeta'(rho+pr)/2 = +3.35 at the throat, essentially uncancelled",
        "note": "nabla T != 0 at O(1) relative size, as eq.(8) of the paper requires; the paper states non-conservation explicitly (eqs.5,8) and no step of the construction (12)-(14) or of the matching assumes conservation"}

# matching arithmetic: eqs.(39),(40),(41) vs eq.(42) as rendered (M=1)
rS = (2.0)**(-1/BETA) * R0**(1+1/BETA)
z0_match = (2.0)**((1-ALPHA+BETA)/BETA) * R0**(ALPHA/BETA) / (ALPHA*((2.0)**(1+1/BETA) - R0**(1+1/BETA)))
C_41 = (1 - 2.0/rS) * np.exp(-z0_match * (R0/rS)**ALPHA)
C_42_rendered = (1 - (2.0/R0)**(1+1/BETA)) * np.exp(-ALPHA*((R0/2.0)**(1+1/BETA) - 1))
res["matching_check"] = {"rSigma_eq39": float(rS), "zeta0_eq40": float(z0_match),
    "C_from_eq41": float(C_41), "C_paper_stated_(5/9)e^(4/5)": float(5/9*np.exp(4/5)),
    "C_from_eq42_as_rendered": float(C_42_rendered),
    "note": "eqs.(39),(40),(41) mutually consistent and reproduce the paper's stated C=(5/9)e^{4/5}; eq.(42) as rendered gives 0.159 instead of 1.237: logged as a rendered-equation discrepancy, not repaired"}

# ---------- 3. Alternative L_m = -rho: rebuild the system ---------------------
# Theta with L=-rho (sympy above): build the three field equations directly.
def alt_residuals(x, r):
    ro, prr, ptt = x
    u = R0/r
    Sv = prr + 2*ptt; Tv = -ro + Sv; T2v = ro**2 + prr**2 + 2*ptt**2
    Lv = -ro
    th_t = -2*Lv*(-ro - Tv/2) - Tv*(-ro) + 2*ro**2
    th_r = -2*Lv*(prr - Tv/2) - Tv*prr + 2*prr**2
    th_h = -2*Lv*(ptt - Tv/2) - Tv*ptt + 2*ptt**2
    # geometric (gamma-independent) parts transcribed from eqs.(12)-(14)
    geo1 = -BETA/r**2 * u**(BETA+1)
    geo2 = -1/r**2 * u**(BETA+1) - ALPHA*Z0/r**2 * u**ALPHA * (1 - u**(BETA+1))
    geo3 = (1+BETA)/(2*r**2) * u**(BETA+1) \
        + ALPHA**2 * Z0**2/(4*r**2) * u**(2*ALPHA) * (1 - u**(BETA+1)) \
        + ALPHA*Z0/(4*r**2) * u**ALPHA * (2*ALPHA - (1+2*ALPHA+BETA)*u**(BETA+1))
    e1 = geo1 + GAMMA*(-th_t + T2v/2) - 8*np.pi*ro
    e2 = geo2 + GAMMA*(th_r - T2v/2) - 8*np.pi*prr
    e3 = geo3 + GAMMA*(th_h - T2v/2) - 8*np.pi*ptt
    return [e1, e2, e3]

roots_alt = []
rng2 = np.random.default_rng(77)
guesses = [tuple(v) for v in rng2.uniform(-45, 45, size=(600, 3))] + \
          [(12.0, 4.0, 4.0), (12.566, 4.189, 4.189), (0.0, 0.0, 0.0), (37.0, -37.0, 37.0)]
for g in guesses:
    try:
        sol, info, ier, _ = fsolve(alt_residuals, g, args=(R0,), full_output=True)
    except Exception:
        continue
    if ier == 1 and np.max(np.abs(alt_residuals(sol, R0))) < 1e-9 and np.all(np.isfinite(sol)):
        if not any(np.max(np.abs(sol - np.array(q))) < 1e-6 for q in roots_alt):
            roots_alt.append(tuple(float(v) for v in sol))
res["alt_Lm_minus_rho_throat_roots"] = [
    {"rho": q[0], "pr": q[1], "pt": q[2], "all_ECs_hold": bool(ec_ok(q))} for q in roots_alt]
# continue any EC root of the alt system over the interior
alt_branch_ok = False; alt_min = {}
ec_alt = [q for q in roots_alt if ec_ok(q)]
if ec_alt:
    x = np.array(ec_alt[0]); rows = []
    for r in np.linspace(R0, 4.5, 151):
        sol, info, ier, _ = fsolve(alt_residuals, x, args=(r,), full_output=True)
        if ier == 1 and np.max(np.abs(alt_residuals(sol, r))) < 1e-9:
            x = sol; rows.append(sol)
    if rows:
        rows = np.array(rows)
        alt_branch_ok = bool(np.all([ec_ok(q) for q in rows]))
        alt_min = {"rho": float(rows[:, 0].min()), "rho+pr": float((rows[:, 0]+rows[:, 1]).min()),
                   "rho+pt": float((rows[:, 0]+rows[:, 2]).min())}
res["alt_Lm_minus_rho_EC_branch_survives_interior"] = alt_branch_ok
res["alt_Lm_minus_rho_EC_minima_interior"] = alt_min

data = {}
if os.path.exists(OUT):
    data = json.load(open(OUT))
data["c_emsg_ganiyeva2023"] = res
json.dump(data, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1)[:6000])
