#!/usr/bin/env python3
"""
P35-1 -- EiBI MIXTURE gravitational sector. See results/p351_run_record.md
(system, prescriptions, ladder stated BEFORE solving). float64.
Gate -> Omega eigen-structure -> Step B series balance -> Step C ladder.
Writes results/p351_results.json.
"""
import json
import numpy as np
from scipy.integrate import solve_ivp

KAP = -1.0
R0 = np.sqrt(0.5)
OUT = "results/p351_results.json"
res = {"item": "P35-1 EiBI mixture gravitational sector", "kappa": KAP,
       "r0": float(R0), "x": 0.5}

# ---------------- P33-3 construction (verbatim formulas) ----------------
def C_for(rho_target):
    if rho_target <= 0: return 0.0
    u = 2.0*rho_target/(2.0-rho_target)
    return u*R0**4

def prof(C, rr):
    """rho = C/(r^4 + C/2) [kappa=-1 form of P33 profile]; returns rho, rho', rho''."""
    D = rr**4 + C/2.0
    rho = C/D
    rp = -4.0*C*rr**3/D**2
    rpp = -12.0*C*rr**2/D**2 + 32.0*C*rr**6/D**3
    return rho, rp, rpp

def totals(f, w, rr):
    C1, C2 = C_for(1.0-f), C_for(f)
    r1, r1p, r1pp = prof(C1, rr); r2, r2p, r2pp = prof(C2, rr)
    rho = r1+r2
    pr = -r1 + w*r2
    pt = r1*(1.0+KAP*r1) + w*r2
    # derivatives
    prp = -r1p + w*r2p
    ptp = r1p*(1.0+2*KAP*r1) + w*r2p
    rhop = r1p+r2p
    return dict(C1=C1, C2=C2, rho=rho, pr=pr, pt=pt, rhop=rhop, prp=prp, ptp=ptp,
                r1=r1, r2=r2, r1p=r1p, r2p=r2p, r1pp=r1pp, r2pp=r2pp)

def omegas(f, w, rr):
    T = totals(f, w, rr)
    a = 1.0+KAP*T["rho"]; b = 1.0-KAP*T["pr"]; c = 1.0-KAP*T["pt"]
    wt = c*np.sqrt(b/a); wr = c*np.sqrt(a/b); wth = np.sqrt(a*b)
    return T, a, b, c, wt, wr, wth

def ec_min(rho, pr, pt):
    combos = [rho, rho+pr, rho+pt, rho+pr+2*pt, rho-np.abs(pr), rho-np.abs(pt)]
    return float(min(np.min(x) for x in combos))

ROWS = [(0.75, 1/3), (0.5, 1/3), (0.6, 0.0)]
KEYS = ["f=0.75_w=0.3333", "f=0.5_w=0.3333", "f=0.6_w=0"]

# ---------------- GATE ----------------
stored = json.load(open("../phase33/results/p333_results.json"))["two_fluid_grid"]
gate = {}
rgrid = np.geomspace(R0, 1e3*R0, 200001)
for (f, w), key in zip(ROWS, KEYS):
    T, a, b, c, wt, wr, wth = omegas(f, w, rgrid)
    st = stored[key]
    # Phi' from fluid-2 conservation; total conservation residual (P33 form)
    with np.errstate(divide="ignore", invalid="ignore"):
        Phip = np.where(T["r2"] > 0, -w*T["r2p"]/((1+w)*T["r2"]), 0.0)
    consT = float(np.max(np.abs(T["prp"] + Phip*(T["rho"]+T["pr"]) + 2*(T["pr"]-T["pt"])/rgrid))) if f > 0 else 0.0
    c1t2 = 1.0+2*KAP*T["r1"][0]
    det0 = float(c[0]**2*a[0]*b[0])
    gate[key] = {
        "kappa_rhoTOT_throat": float(KAP*T["rho"][0]),
        "stored": st["kappa_rhoTOT_throat"],
        "c1t2_throat": float(c1t2), "formula_2f-1": 2*f-1,
        "c1t2_err_vs_formula": float(abs(c1t2-(2*f-1))),
        "stored_c1t2": st["speeds"]["c1t2_throat"],
        "cons_total_maxabs": consT, "stored_cons": st["cons_total_maxabs_with_solved_Phi"],
        "EC_total_min": ec_min(T["rho"], T["pr"], T["pt"]),
        "EC_total_pass": bool(ec_min(T["rho"], T["pr"], T["pt"]) >= -1e-12),
        "stored_EC_pass": st["EC_total"]["all_ECs_pass"],
        "det_Omega_throat": det0, "stored_det": st["Omega"]["det_throat"],
        "a_throat": float(a[0]), "b_throat": float(b[0]), "c_throat": float(c[0]),
    }
    g = gate[key]
    g["GATE_ROW_PASS"] = bool(abs(g["kappa_rhoTOT_throat"]+1) < 1e-12
        and g["c1t2_err_vs_formula"] <= 1e-9 and consT <= 1e-12
        and g["EC_total_pass"] and abs(det0) < 1e-12)
res["gate"] = gate
res["GATE_PASSED"] = bool(all(v["GATE_ROW_PASS"] for v in gate.values()))

# ---------------- Omega eigen-structure in epsilon ----------------
eps_arr = np.logspace(-8, -3, 41)
eig = {}
for (f, w), key in zip(ROWS, KEYS):
    rr = R0 + eps_arr
    T, a, b, c, wt, wr, wth = omegas(f, w, rr)
    det = c**2*a*b
    S = rr*(a*b)**0.25
    def slope(y):  # log-log fit slope of |y| vs eps
        return float(np.polyfit(np.log(eps_arr), np.log(np.abs(y)), 1)[0])
    eig[key] = {
        "a_slope": slope(a), "b_at_throat_limit": float(b[0]),
        "b_slope_of_b_minus_b0": slope(b-b[0]) if abs(b[0]) > 0 else None,
        "c_at_throat_limit": float(c[0]),
        "omega_t_slope": slope(wt), "omega_r_slope": slope(wr),
        "omega_theta_slope": slope(wth), "det_slope": slope(det),
        "S_slope": slope(S),
        "a1_a_prime_throat_numeric": float((a[1]-a[0])/(eps_arr[1]-eps_arr[0])),
        "omega_t_at_eps1e-6": float(wt[np.argmin(np.abs(eps_arr-1e-6))]),
        "b0_formula_f(1+w)": f*(1+w), "c0_formula": None,
    }
    # c0: 1 - kappa*pt_tot(r0); pt_tot(r0) = (1-f)(1-(1-f)) + w f = f(1-f)+wf
    eig[key]["c0_formula"] = 1.0 + (f*(1-f) + w*f)
    eig[key]["c_at_throat_formula_check"] = float(c[0])
res["omega_eigenstructure_eps"] = eig
# one-fluid comparison (f=0, w=1/3): b=a, wt finite
T0, a0_, b0_, c0_, wt0, wr0, wth0 = omegas(0.0, 1/3, R0+eps_arr)
res["omega_onefluid_comparison"] = {
    "b_equals_a": bool(np.allclose(b0_, a0_)),
    "omega_t_slope": float(np.polyfit(np.log(eps_arr), np.log(np.abs(wt0)), 1)[0]),
    "omega_t_throat_limit": float(wt0[0]),
    "det_slope": float(np.polyfit(np.log(eps_arr), np.log(np.abs(c0_**2*a0_*b0_)), 1)[0]),
    "S_slope": float(np.polyfit(np.log(eps_arr), np.log(np.abs((R0+eps_arr)*(a0_*b0_)**0.25)), 1)[0]),
    "omega_theta_slope": float(np.polyfit(np.log(eps_arr), np.log(np.abs(wth0)), 1)[0]),
}

# ---------------- STEP B: epsilon-series balance of q = g + kappa R(q) ----
def derivs_at(f, w, rr):
    """a,b,c and first/second log derivatives; Phi', Phi'' at points rr (array)."""
    T = totals(f, w, rr)
    a = 1.0+KAP*T["rho"]; b = 1.0-KAP*T["pr"]; c = 1.0-KAP*T["pt"]
    # second derivatives of totals
    r1pp, r2pp = T["r1pp"], T["r2pp"]
    rhopp = r1pp+r2pp; prpp = -r1pp + w*r2pp
    ptpp = r1pp*(1.0+2*KAP*T["r1"]) + 2*KAP*T["r1p"]**2 + w*r2pp
    ap, bp, cp = KAP*T["rhop"], -KAP*T["prp"], -KAP*T["ptp"]
    app, bpp, cpp = KAP*rhopp, -KAP*prpp, -KAP*ptpp
    def ld(x, xp, xpp):  # (ln x)', (ln x)''
        return xp/x, xpp/x - (xp/x)**2
    la, laa = ld(a, ap, app); lb, lbb = ld(b, bp, bpp); lc, lcc = ld(c, cp, cpp)
    # Phi = -(w/(1+w)) ln(rho2/rho2(r0)); Phi' = -(w/(1+w)) rho2'/rho2
    if w > 0:
        l2, l22 = ld(T["r2"], T["r2p"], r2pp)
        Phip = -(w/(1+w))*l2; Phipp = -(w/(1+w))*l22
    else:
        Phip = np.zeros_like(rr); Phipp = np.zeros_like(rr)
    return dict(a=a, b=b, c=c, la=la, laa=laa, lb=lb, lbb=lbb, lc=lc, lcc=lcc,
                Phip=Phip, Phipp=Phipp, T=T)

def ricci_q(f, w, rr, q_exp, U=1.0):
    """R_rr(q), R_tt(q), R_thth(q) with u = U*eps^q_exp; returns dict of arrays."""
    d = derivs_at(f, w, rr)
    eps = rr-R0
    # A = ln Q_t = ln wt + 2Phi ; B = ln Q_r = ln wr - ln u ; lnS
    Ap = d["lc"] + 0.5*(d["lb"]-d["la"]) + 2*d["Phip"]
    App = d["lcc"] + 0.5*(d["lbb"]-d["laa"]) + 2*d["Phipp"]
    Bp = d["lc"] + 0.5*(d["la"]-d["lb"]) - q_exp/eps
    lSp = 1.0/rr + 0.25*(d["la"]+d["lb"])
    lSpp = -1.0/rr**2 + 0.25*(d["laa"]+d["lbb"])
    Sp2 = lSpp + lSp**2  # S''/S
    Kt = App/2 + Ap**2/4 - Ap*Bp/4 + Ap*lSp
    Rrr = -App/2 - Ap**2/4 + Ap*Bp/4 + Bp*lSp - 2*Sp2
    # R_tt = exp(A-B) Kt ; exp(A-B) = (wt/wr)*exp(2Phi)*u ; wt/wr = b/a
    # Phi itself: -(w/(1+w)) ln(rho2/rho2(r0))
    T = d["T"]
    if w > 0:
        _, _, _ = None, None, None
        rho2_0 = totals(f, w, np.array([R0]))["r2"][0]
        Phi = -(w/(1+w))*np.log(T["r2"]/rho2_0)
    else:
        Phi = np.zeros_like(rr)
    u = U*eps**q_exp
    expAB = (d["b"]/d["a"])*np.exp(2*Phi)*u
    Rtt = expAB*Kt
    # R_thth = exp(-B)[ -S A' S'/2 + S B' S'/2 - S S'' + exp(B) - S'^2 ]
    #        = exp(-B) * S^2 * [ -(A' lSp)/2 + (B' lSp)/2 - Sp2 + exp(B)/S^2 - lSp^2 ]
    S = rr*(d["a"]*d["b"])**0.25
    expB = (d["c"]*np.sqrt(d["a"]/d["b"]))/u  # Q_r = wr/u
    expmB = 1.0/expB
    Rth = expmB*S**2*(-(Ap*lSp)/2 + (Bp*lSp)/2 - Sp2 + expB/S**2 - lSp**2)
    return dict(Rrr=Rrr, Rtt=Rtt, Rth=Rth, Kt=Kt, u=u, Phi=Phi, d=d)

stepB = {}
eps_small = np.array([1e-4, 3e-5, 1e-5, 3e-6, 1e-6])
for (f, w), key in zip(ROWS, KEYS):
    rr = R0 + eps_small
    out = {}
    for q in (1.0, 1.5, 2.0, 2.5):
        R = ricci_q(f, w, rr, q)
        out[f"q={q}"] = {
            "eps2_Kt_at_1e-6": float(eps_small[-1]**2 * R["Kt"][-1]),
            "eps_Kt_at_1e-6": float(eps_small[-1] * R["Kt"][-1]),
        }
    R2 = ricci_q(f, w, rr, 2.0, U=1.0)
    d = R2["d"]
    wt = d["c"]*np.sqrt(d["b"]/d["a"]); wr = d["c"]*np.sqrt(d["a"]/d["b"]); wth = np.sqrt(d["a"]*d["b"])
    Rrr_req = (1.0-wr)/R2["u"]            # (G_r - Q_r), kappa=-1
    Rtt_req = np.exp(2*R2["Phi"])*(wt-1.0)
    Rth_req = rr**2*(1.0-wth)
    out["q=2_limits"] = {
        "eps2_Rrr_computed": [float(e**2*x) for e, x in zip(eps_small, R2["Rrr"])],
        "eps2_Rrr_required_U1": [float(e**2*x) for e, x in zip(eps_small, Rrr_req)],
        "eps_Rtt_computed": [float(e*x) for e, x in zip(eps_small, R2["Rtt"])],
        "epshalf_Rtt_required": [float(np.sqrt(e)*x) for e, x in zip(eps_small, Rtt_req)],
        "Rth_computed_at_eps": [float(x) for x in R2["Rth"]],
        "Rth_required_at_eps": [float(x) for x in Rth_req],
        "c_Phi_profile_tail": 4*w/(1+w),
        "Phi_prime_throat": float(d["Phip"][0]),
    }
    stepB[key] = out
res["stepB_series_balance"] = stepB

# ---------------- STEP C: regularised-layer matching ----------------
def layer_S(f, w, delta, eta, prescription, rr):
    """S_reg and (ln S_reg)' on rr in [r0, r0+delta]; also a_reg,b_reg."""
    T = totals(f, w, rr)
    a = 1.0+KAP*T["rho"]; b = 1.0-KAP*T["pr"]; c = 1.0-KAP*T["pt"]
    t = (rr-R0)/delta
    if prescription == "hard_floor":
        a_reg = eta + (a-eta)*t**2
        # derivative via analytic a' : a' = kappa*rhop
        ap = KAP*T["rhop"]
        a_reg_p = ap*t**2 + (a-eta)*2*t/delta
        b_reg, b_reg_p = b, -KAP*T["prp"]
        la = a_reg_p/a_reg; lb = b_reg_p/b_reg
        rho_reg = (a_reg-1.0)/KAP
        ec_layer_min = ec_min(rho_reg, T["pr"], T["pt"])
    else:  # smooth interpolation of totals
        s = 3*t**2-2*t**3; sp = (6*t-6*t**2)/delta
        Ttop = totals(f, w, np.array([R0+delta]))
        rho_in, pr_in, pt_in = 1.0-eta, float(T["pr"][0]*0 + totals(f, w, np.array([R0]))["pr"][0]), float(totals(f, w, np.array([R0]))["pt"][0])
        rho_reg = rho_in + (float(Ttop["rho"][0])-rho_in)*s
        pr_reg = pr_in + (float(Ttop["pr"][0])-pr_in)*s
        pt_reg = pt_in + (float(Ttop["pt"][0])-pt_in)*s
        rho_reg_p = (float(Ttop["rho"][0])-rho_in)*sp
        pr_reg_p = (float(Ttop["pr"][0])-pr_in)*sp
        a_reg = 1.0+KAP*rho_reg; b_reg = 1.0-KAP*pr_reg
        la = KAP*rho_reg_p/a_reg; lb = -KAP*pr_reg_p/b_reg
        ec_layer_min = ec_min(rho_reg, pr_reg, pt_reg)
    S = rr*(a_reg*b_reg)**0.25
    lSp = 1.0/rr + 0.25*(la+lb)
    return S, lSp, ec_layer_min

def sector_L(f, w, delta, eta, prescription, sector):
    S0, _, _ = layer_S(f, w, delta, eta, prescription, np.array([R0]))
    def rhs(rr, y):
        S, lSp, _ = layer_S(f, w, delta, eta, prescription, np.array([rr]))
        return [y[1], -2*lSp[0]*y[1] + 6.0/S[0]**2*y[0]]
    y0 = [1.0, 0.0] if sector == "even" else [0.0, 1.0]
    sol = solve_ivp(rhs, [R0, R0+delta], y0, method="LSODA",
                    rtol=1e-9, atol=1e-12, dense_output=False)
    psi, psip = sol.y[0, -1], sol.y[1, -1]
    _, _, ecmin = layer_S(f, w, delta, eta, prescription, np.array([R0+delta/2]))
    return {"Psi_top": float(psi), "Psip_top": float(psip),
            "L_top": float(psip/psi) if psi != 0 else None,
            "layer_EC_min_mid": float(ecmin), "success": bool(sol.success)}

ladder = {}
DELTAS = [1e-1, 1e-2, 1e-3]; ETAS = [1e-2, 1e-4, 1e-6]
for presc in ("hard_floor", "smooth_interp"):
    ladder[presc] = {}
    for dr in DELTAS:
        for eta in ETAS:
            entry = {}
            for sector in ("even", "odd"):
                entry[sector] = sector_L(0.75, 1/3, dr*R0, eta, presc, sector)
            ladder[presc][f"delta_r0={dr}_eta={eta}"] = entry
res["stepC_ladder_primary_f0.75_w13"] = ladder
# cross rows: diagonal only, both prescriptions
cross = {}
for (f, w), key in zip(ROWS[1:], KEYS[1:]):
    cross[key] = {}
    for presc in ("hard_floor", "smooth_interp"):
        cross[key][presc] = {}
        for dr, eta in zip(DELTAS, ETAS):
            cross[key][presc][f"delta_r0={dr}_eta={eta}"] = {
                s: sector_L(f, w, dr*R0, eta, presc, s) for s in ("even", "odd")}
res["stepC_cross_rows_diagonal"] = cross

# health signs on [r0+delta, 10 r0], original background, primary row
health = {}
for dr in DELTAS:
    rr = np.geomspace(R0+dr*R0, 10*R0, 20001)
    T, a, b, c, wt, wr, wth = omegas(0.75, 1/3, rr)
    health[f"delta_r0={dr}"] = {
        "sqrt_detOmega_min": float(np.min(c*np.sqrt(a*b))),
        "kinetic_sign_positive": bool(np.all(c*np.sqrt(a*b) > 0)),
        "radial_cone_ratio2_b_over_a_min": float(np.min(b/a)),
        "angular_cone_ratio2_wt_over_wth_min": float(np.min(wt/wth)),
        "gradient_signs_positive": bool(np.all(b/a > 0) and np.all(wt/wth > 0)),
    }
res["stepC_health_signs_primary"] = health

# convergence reads: diagonal sequence, last-step relative change; cross-prescription
def diagL(presc, sector):
    return [ladder[presc][f"delta_r0={d}_eta={e}"][sector]["L_top"]
            for d, e in zip(DELTAS, ETAS)]
conv = {}
for sector in ("even", "odd"):
    conv[sector] = {}
    for presc in ("hard_floor", "smooth_interp"):
        L = diagL(presc, sector)
        conv[sector][presc] = {"L_diagonal": L,
            "last_step_rel_change": float(abs(L[-1]-L[-2])/abs(L[-2])) if L[-2] else None}
    Lh, Ls = diagL("hard_floor", sector), diagL("smooth_interp", sector)
    conv[sector]["cross_prescription_rel_diff_finest"] = float(abs(Lh[-1]-Ls[-1])/abs(Lh[-1])) if Lh[-1] else None
res["stepC_convergence"] = conv

with open(OUT, "w") as fh:
    json.dump(res, fh, indent=2)
print("GATE:", res["GATE_PASSED"], {k: v["GATE_ROW_PASS"] for k, v in gate.items()})
print("eig primary:", eig[KEYS[0]])
print("one-fluid cmp:", res["omega_onefluid_comparison"])
print("stepB primary q=2:", stepB[KEYS[0]]["q=2_limits"])
print("conv:", json.dumps(conv, indent=1))
print("WROTE", OUT)
