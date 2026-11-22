#!/usr/bin/env python3
"""
P33-3 -- EiBI TWO-FLUID augmentation of the Shaikh anisotropic-fluid throat.

Baseline failure (P20-2, structural): single-fluid EiBI throat has
c_t^2 = dp_t/drho = 1 + 2 kappa rho = -1 FORCED at the throat, because the
throat condition itself is kappa rho(r0) = -1 (Gate-5 G5-2).

Addition: a SECOND ordinary fluid, isotropic, p2 = w rho2, w in [0,1],
itself EC-legal everywhere, comoving with fluid 1 (Shaikh-type anisotropic:
p_r1 = -rho1, p_t1 = rho1 (1 + kappa rho1) -- EoS in fluid 1's OWN density,
the autonomous/microphysical reading). EiBI couples to the TOTAL T only.

Units: 8 pi = G = c = 1 (Shaikh), kappa = -1 (|kappa| = 1), genuine-wormhole
regime x = r0^2/|kappa| = 0.5 < 1  =>  r0 = sqrt(0.5). Conditional
observational caveat |kappa| <~ 1e8 m^2 carried in all statements (memo).

CONSTRUCTION (profile level -- the P20-2 closure standard: ECs +
conservation + throat algebra + Omega read; the q-Einstein metric
reconstruction b(r), Phi(r) is NOT performed, exactly as P20-2 did not
reconstruct Shaikh's f(r); named as the follow-up experiment):
  * Fluid 1 separately conserved. With p_r1 = -rho1 its conservation is
    Phi-free (Shaikh Eq.21 applied to fluid 1):
        rho1' + (2/r)(rho1 + p_t1) = 0,  p_t1 = rho1(1 + kappa rho1)
    whose integral is Shaikh's own family with its own constant C1:
        rho1 = (C1/r^4) / (1 - kappa C1/(2 r^4)).
  * Fluid 2 separately conserved (isotropic):
        w rho2' + (1+w) Phi' rho2 = 0.
    Its profile is taken in the same rational family (own constant C2);
    Phi'(r) is then SOLVED from fluid-2 conservation,
        Phi' = - w rho2' / ((1+w) rho2),
    and total conservation is verified as an identity (it is equivalent
    to fluid-1 + fluid-2 conservation; the numerator of the total
    conservation equation reduces analytically to w rho2').
  * Throat condition imposed on TOTALS (registered gate):
        kappa rho_tot(r0) = -1,  rho_tot = rho1 + rho2,
    with throat mixture fraction f := rho2(r0)/rho_tot(r0) in [0,1],
    i.e. rho1(r0) = (1-f)/|kappa|, rho2(r0) = f/|kappa|.

PERTURBATION FRAMEWORK (explicit): comoving two-fluid, adiabatic
perturbations (each fluid perturbed along its own barotropic EoS),
MATTER SECTOR on the closed background. The EiBI gravitational coupling
through the auxiliary metric q is NOT included -- and cannot be posed at
the throat: det Omega = 0 there for ANY mixture (omega_theta =
sqrt((1+kappa rho_tot)(1-kappa p_r,tot)) vanishes because 1+kappa
rho_tot(r0) = 0 by the throat condition on totals; P20-2 obstruction,
unchanged). Two velocity readings are computed:
  (i) LOCKED velocities (single common delta-u, strict comoving):
      one acoustic mode per direction, enthalpy-weighted:
          c_mix,n^2 = sum_i c_{i,n}^2 (rho_i + p_{i,n})
                      / sum_i (rho_i + p_{i,n}),
      plus a non-propagating composition (entropy) mode, omega = 0.
  (ii) INDEPENDENT velocities (gravity-only coupling, standard
      multi-fluid): one acoustic mode per fluid per direction with the
      per-fluid adiabatic speed c_{i,n}^2 = dp_{i,n}/d rho_i.
      Fluid 1's RADIAL mode is degenerate: rho1 + p_r1 = 0 identically,
      so it carries no radial inertia and no radial acoustic mode exists
      for it (its dp_r1/drho1 = -1 multiplies a vanishing enthalpy and
      is NOT a propagating speed -- same reason P20-2's single-fluid
      radial sector had no acoustic read).
The bar is applied across BOTH readings: every computed physical sound
speed must lie in [0,1].

float64. Writes results/p333_results.json.
"""
import json
import numpy as np

KAP = -1.0                      # kappa < 0 required
AKAP = abs(KAP)
R0 = np.sqrt(0.5)               # x = r0^2/|kappa| = 0.5 (genuine, off criticality)
X_GATE = R0**2 / AKAP
TOL = 1e-12
OUT = "results/p333_results.json"

r = np.geomspace(R0, 1e3 * R0, 200001)      # task domain [r0, 1e3 r0]
r_in = r[1:]                                 # r > r0 subgrid (Omega reads)

def profile(C, rr):
    """Shaikh-family profile and analytic derivative.
    rho = (C/r^4)/(1 - kappa C/(2 r^4));  rho' = -4u/(r d^2),
    u = C/r^4, d = 1 - kappa u/2 (kappa=-1: d = 1 + u/2)."""
    u = C / rr**4
    d = 1.0 - KAP * u / 2.0
    rho = u / d
    rhop = -4.0 * u / (rr * d**2)
    return rho, rhop

def C_for_rho_at_r0(rho_target):
    """Invert rho(r0) = u/(1+u/2), u = C/r0^4  ->  u = 2 rho/(2-rho)
    (in |kappa|=1 units, rho_target = |kappa| rho_target <= 2)."""
    if rho_target <= 0.0:
        return 0.0
    u = 2.0 * rho_target / (2.0 - rho_target)
    return u * R0**4

def ec_block(rho, pr, pt):
    combos = {
        "rho": rho, "NEC_r_rho+pr": rho + pr, "NEC_t_rho+pt": rho + pt,
        "SEC_rho+pr+2pt": rho + pr + 2 * pt,
        "DEC_r_rho-|pr|": rho - np.abs(pr), "DEC_t_rho-|pt|": rho - np.abs(pt),
    }
    out = {}
    allpass = True
    for k, v in combos.items():
        out[k + "_min"] = float(np.min(v))
        if np.min(v) < -TOL:
            allpass = False
    out["all_ECs_pass"] = bool(allpass)
    return out

res = {"item": "P33-3 EiBI two-fluid", "kappa": KAP, "r0": float(R0),
       "x_r0sq_over_abs_kappa": float(X_GATE),
       "units": "8pi=G=c=1 (Shaikh), |kappa|=1",
       "caveat": "conditional observational caveat |kappa| <~ 1e8 m^2 "
                 "carried in all statements (Phases 3/20/23)",
       "domain": [float(R0), float(1e3 * R0)]}

# =====================================================================
# GATE 1: single-fluid limit reproduces P20-2 / Phase-3 background
# =====================================================================
gate = {}
# (a) Phase-3 normalisation row: C0 = 2, r0 = 1, x = 1 (critical)
rA = np.geomspace(1.0, 1e3, 200001)
rhoA, _ = profile(2.0, rA)
ptA = rhoA * (1.0 + KAP * rhoA)
gate["phase3_C0=2_r0=1"] = {
    "rho_throat": float(rhoA[0]), "pt_throat": float(ptA[0]),
    "one_plus_kappa_rho_throat": float(1.0 + KAP * rhoA[0]),
    "NCC_throat_Eq26": float(2 * KAP / 1.0**2 * (rhoA[0] + ptA[0])),
    "c_t2_throat_1+2kap_rho": float(1.0 + 2 * KAP * rhoA[0]),
}
# stored Phase-3 targets
with open("../phase3/results/p32_modgrav.json") as fh:
    p32 = json.load(fh)
tgt = p32["EiBI"]["anisotropic_fluid_SecVC"]["at_throat"]
gate["phase3_stored_targets"] = {"rho": tgt["rho"], "pt": tgt["pt"],
                                 "NCC_Rkk": tgt["NCC_Rkk_Eq26"]}
gate["phase3_match"] = bool(
    abs(gate["phase3_C0=2_r0=1"]["rho_throat"] - tgt["rho"]) < 1e-12 and
    abs(gate["phase3_C0=2_r0=1"]["pt_throat"] - tgt["pt"]) < 1e-12 and
    abs(gate["phase3_C0=2_r0=1"]["NCC_throat_Eq26"] - tgt["NCC_Rkk_Eq26"]) < 1e-12)

# (b) P20-2 genuine fluid member: C0 = 1/2, r0 = (1/4)^{1/4} = sqrt(0.5), x=0.5
rhoG, rhoGp = profile(0.5, r)
ptG = rhoG * (1.0 + KAP * rhoG)
ct2G = 1.0 + 2 * KAP * rhoG
i_star = int(np.argmin(np.abs(rhoG - 0.5)))
consG = float(np.max(np.abs(rhoGp + 2.0 * (rhoG + ptG) / r)))
gate["p20_genuine_C0=0.5"] = {
    "rho_throat": float(rhoG[0]),
    "kappa_rho_throat": float(KAP * rhoG[0]),
    "c_t2_throat": float(ct2G[0]),
    "c_t2_zero_r_numeric": float(r[i_star]),
    "c_t2_zero_r_analytic_(0.75)^(1/4)": float(0.75 ** 0.25),
    "conservation_Eq21_maxabs_resid": consG,
    "ECs": ec_block(rhoG, -rhoG, ptG),
}
with open("../phase20/results/p202a_eibi.json") as fh:
    p202 = json.load(fh)
p202_ct2 = p202["sector_Eb_EoS_sound_speeds"]["fluid_genuine_C0=0.5"]["c_t2_throat"]
gate["p20_stored_c_t2_throat_genuine"] = float(p202_ct2)
gate["p20_match"] = bool(abs(gate["p20_genuine_C0=0.5"]["c_t2_throat"] - p202_ct2) < 1e-12
                         and abs(gate["p20_genuine_C0=0.5"]["kappa_rho_throat"] + 1.0) < 1e-12)
gate["GATE_PASSED"] = bool(gate["phase3_match"] and gate["p20_match"])
res["gate_single_fluid_limit"] = gate

# =====================================================================
# TWO-FLUID GRID over throat mixture fraction f and w
# =====================================================================
FS = [0.0, 0.25, 0.4, 0.5, 0.6, 0.75, 0.9, 1.0]
WS = [0.0, 1.0 / 3.0, 0.5, 1.0]
rows = {}
for f in FS:
    C1 = C_for_rho_at_r0((1.0 - f) / AKAP)
    C2 = C_for_rho_at_r0(f / AKAP)
    rho1, rho1p = profile(C1, r)
    rho2, rho2p = profile(C2, r)
    pr1, pt1 = -rho1, rho1 * (1.0 + KAP * rho1)
    # fluid-1 conservation residual (analytic, Phi-free)
    cons1 = float(np.max(np.abs(rho1p + 2.0 * (rho1 + pt1) / r))) if C1 > 0 else 0.0
    for w in WS:
        p2 = w * rho2
        rhoT, prT, ptT = rho1 + rho2, pr1 + p2, pt1 + p2
        # Phi' solved from fluid-2 separate conservation (f>0); w=0 -> Phi'=0
        if f > 0.0:
            with np.errstate(divide="ignore", invalid="ignore"):
                Phi_p = np.where(rho2 > 0, -w * rho2p / ((1.0 + w) * rho2), 0.0)
            # total conservation residual with this Phi' (must vanish identically)
            prTp = -rho1p + w * rho2p
            consT = float(np.max(np.abs(
                prTp + Phi_p * (rhoT + prT) + 2.0 * (prT - ptT) / r)))
            cons2 = float(np.max(np.abs(w * rho2p + (1.0 + w) * Phi_p * rho2)))
            Phi_throat = float(Phi_p[0])
            Phi_max = float(np.max(np.abs(Phi_p)))
            Phi_tail_coeff = float(Phi_p[-1] * r[-1])   # -> 4w/(1+w) for 1/r^4 tail
        else:
            consT, cons2, Phi_throat, Phi_max, Phi_tail_coeff = None, None, None, None, None
        # ---- Omega (general totals): a=1+kap rho, b=1-kap pr, c=1-kap pt
        a_om = 1.0 + KAP * rhoT
        b_om = 1.0 - KAP * prT
        c_om = 1.0 - KAP * ptT
        wth = np.sqrt(a_om[1:] * b_om[1:])
        det = c_om[1:]**2 * a_om[1:] * b_om[1:]
        wt_first = float(c_om[1] * np.sqrt(b_om[1] / a_om[1]))  # pole as r->r0+
        # ---- sound speeds
        c1t2 = 1.0 + 2 * KAP * rho1            # per-fluid tangential, fluid 1
        c1r2 = -1.0                            # formal derivative; zero enthalpy (see header)
        h1t = rho1 + pt1                       # tangential enthalpy fluid 1 = rho1(2+kap rho1)
        h2t = (1.0 + w) * rho2
        with np.errstate(divide="ignore", invalid="ignore"):
            cmix_t2 = np.where(h1t + h2t > 0,
                               (c1t2 * h1t + w * h2t) / (h1t + h2t), np.nan)
        # radial locked mode: fluid-1 radial enthalpy = 0 identically -> = w
        cmix_r2 = float(w)
        # background derivative dp_t,tot/d rho_tot along the profile (NOT a mode)
        ptTp = rho1p * (1.0 + 2 * KAP * rho1) + w * rho2p
        rhoTp = rho1p + rho2p
        bg_deriv_throat = float(ptTp[0] / rhoTp[0]) if f < 1.0 else float(w)
        # radius where c1t2 crosses 0 (rho1 = 1/(2|kap|)): u=2/3 -> r=(1.5 C1)^{1/4}
        r_star = float((1.5 * C1) ** 0.25) if (C1 > 0 and (1.0 - f) > 0.5) else None
        speeds_ok = bool(np.nanmin(c1t2) >= -TOL and np.nanmax(c1t2) <= 1.0 + TOL
                         and np.nanmin(cmix_t2) >= -TOL and np.nanmax(cmix_t2) <= 1.0 + TOL
                         and 0.0 <= w <= 1.0)
        ecT = ec_block(rhoT, prT, ptT)
        ec1 = ec_block(rho1, pr1, pt1)
        ec2 = ec_block(rho2, p2, p2)
        row_pass = bool(ecT["all_ECs_pass"] and ec1["all_ECs_pass"]
                        and ec2["all_ECs_pass"] and speeds_ok and f < 1.0)
        rows[f"f={f}_w={w:.4g}"] = {
            "f_throat": f, "w": w, "C1": float(C1), "C2": float(C2),
            "rho1_throat": float(rho1[0]), "rho2_throat": float(rho2[0]),
            "kappa_rhoTOT_throat": float(KAP * rhoT[0]),
            "cons_fluid1_maxabs": cons1, "cons_fluid2_maxabs": cons2,
            "cons_total_maxabs_with_solved_Phi": consT,
            "Phi_prime_throat": Phi_throat, "Phi_prime_maxabs": Phi_max,
            "Phi_prime_tail_r_times_Phi_at_rmax": Phi_tail_coeff,
            "EC_total": ecT, "EC_fluid1_alone": ec1, "EC_fluid2_alone": ec2,
            "Omega": {"a_throat_1+kap_rhoTOT": float(a_om[0]),
                      "det_throat": float(c_om[0]**2 * a_om[0] * b_om[0]),
                      "omega_theta_min_r>r0": float(np.min(wth)),
                      "det_min_r>r0": float(np.min(det)),
                      "omega_t_first_gridpoint_r>r0": wt_first,
                      "all_eigs_positive_r>r0": bool(np.all(a_om[1:] > 0)
                                                     and np.all(b_om[1:] > 0)
                                                     and np.all(c_om[1:] > 0))},
            "speeds": {
                "c1t2_throat_formula_2f-1": float(2 * f - 1) if f < 1.0 else None,
                "c1t2_throat": float(c1t2[0]) if f < 1.0 else None,
                "c1t2_min_domain": float(np.min(c1t2)) if f < 1.0 else None,
                "c1t2_zero_radius": r_star,
                "c2_speed2_equals_w": float(w),
                "coupled_tangential_cmix2_throat": float(cmix_t2[0]),
                "coupled_tangential_cmix2_min_domain": float(np.nanmin(cmix_t2)),
                "coupled_tangential_cmix2_max_domain": float(np.nanmax(cmix_t2)),
                "coupled_radial_cmix2": cmix_r2,
                "entropy_composition_mode_speed2": 0.0,
                "background_derivative_dpt_drho_at_throat_NOT_A_MODE": bg_deriv_throat,
            },
            "row_verdict": ("BOUNDARY (f=1: fluid 1 absent, not an augmentation row)"
                            if f == 1.0 else
                            ("PASS" if row_pass else "FAIL")),
            "deciding_mode_if_fail": (
                None if row_pass or f == 1.0 else
                "fluid-1 tangential acoustic mode (independent-velocity reading): "
                f"c1t2(r0) = 1 + 2 kappa rho1(r0) = {float(c1t2[0]):.4f} < 0"),
        }
res["two_fluid_grid"] = rows

# =====================================================================
# Summary
# =====================================================================
pass_rows = [k for k, v in rows.items() if v["row_verdict"] == "PASS"]
fail_rows = [k for k, v in rows.items() if v["row_verdict"] == "FAIL"]
res["summary"] = {
    "n_rows": len(rows), "n_pass": len(pass_rows), "n_fail": len(fail_rows),
    "pass_rows": pass_rows, "fail_rows": fail_rows,
    "pass_condition_found": "throat mixture fraction f >= 1/2, i.e. "
        "rho1(r0) <= 1/(2|kappa|): fluid 2 carries at least half the throat "
        "density. Then c1t2 = 1 + 2 kappa rho1 in [0,1] on the whole domain "
        "(rho1 maximal at the throat, decreasing outward), and the locked "
        "coupled tangential speed, an enthalpy-weighted average of c1t2 and "
        "w, is in [0,1] automatically.",
    "core_answer": "The forced -1 is a property of the ONE-FLUID ANSATZ, not "
        "of the mixture: the throat condition fixes only the TOTAL density "
        "(kappa rho_tot(r0) = -1); fluid 1's tangential speed at the throat "
        "is 1 + 2 kappa rho1(r0) = 2f - 1, which equals -1 only when f = 0.",
    "persistent_obstruction": "det Omega(r0) = 0 for EVERY mixture (depends "
        "only on total rho through 1 + kappa rho_tot(r0) = 0); off-ansatz "
        "omega_t additionally has a pole at the throat. The full EiBI "
        "gravitational perturbation system through q remains NOT COMPUTABLE "
        "at the throat (P20-2 obstruction, unchanged). Verdict scope: "
        "matter-sector modes, both velocity readings.",
}
res["verdict"] = ("AUGMENTED-PASS" if pass_rows else "AUGMENTED-FAIL")

with open(OUT, "w") as fh:
    json.dump(res, fh, indent=2)
print("GATE phase3 match:", gate["phase3_match"], "| p20 match:", gate["p20_match"],
      "| GATE_PASSED:", gate["GATE_PASSED"])
print("gate genuine: kappa*rho(r0) =", gate["p20_genuine_C0=0.5"]["kappa_rho_throat"],
      "c_t2(r0) =", gate["p20_genuine_C0=0.5"]["c_t2_throat"],
      "cons resid =", consG)
for k, v in rows.items():
    s = v["speeds"]
    print(k, "| ECtot", v["EC_total"]["all_ECs_pass"],
          "| c1t2(r0)", s["c1t2_throat"], "| cmix_t2(r0)", round(s["coupled_tangential_cmix2_throat"], 4),
          "| cmix range", (round(s["coupled_tangential_cmix2_min_domain"], 4),
                           round(s["coupled_tangential_cmix2_max_domain"], 4)),
          "| bg deriv", round(s["background_derivative_dpt_drho_at_throat_NOT_A_MODE"], 4),
          "|", v["row_verdict"])
print("VERDICT:", res["verdict"], "| pass", len(pass_rows), "fail", len(fail_rows))
print("WROTE", OUT)
