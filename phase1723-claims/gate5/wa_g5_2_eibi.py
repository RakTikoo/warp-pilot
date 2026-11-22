#!/usr/bin/env python3
"""
Gate-5 WA — G5-2(a,b,c): EiBI wormhole obstructions, FRESH independent path.
Written from the CLAIM STATEMENT + my own transcription of Shaikh,
arXiv:1807.07941v2 (PRD 98 (2018)), fetched and read in this run.
The phase-20 script was NOT imported or re-run.

My transcription (verbatim from the fetched paper):
  Action (Sec.II): S_BI = c^4/(8 pi G kappa) int [ sqrt-|g+kappa R(Gamma)|
      - lambda sqrt-g ] + S_M.
  Field eq.(1): sqrt(-q) q^{mu nu} = lambda sqrt(-g) g^{mu nu}
      - kappabar sqrt(-g) T^{mu nu};  q_{mu nu} = g_{mu nu} + kappa R_{mu nu}.
  Eq.(2) => Gamma = Levi-Civita of q.
  Metrics (5),(6); auxiliary relations Eq.(7):
      e^alpha = e^nu sqrt(tau(1+kappa rho)),
      e^beta  = e^Psi sqrt(tau(1-kappa p_r)),
      r = H sqrt(tau(1-kappa p_theta)),
      tau = 1/sqrt((1+kappa rho)(1-kappa p_r)(1-kappa p_theta)^2).
  Ansatz p_r = -rho; conservation Eq.(21): rho' + (2/r)(rho+p_theta)=0.
  NCC Eq.(26): R_{mu nu} k^mu k^nu = (2 kappa/r^2)(rho+p_theta)
      [after using Eq.(25) e^{alpha+beta}=1/sqrt(1+kappa rho)].
  Throat definition (Sec.IV, below Eq.(28) and Eq.(29)):
      throat r0 solves (1+kappa rho)|_{r0} = 0  [expansion scalar vanishes];
      H(r) = r sqrt(1+kappa rho)  [Eq.(33)];  psi = 1/sqrt(1+kappa rho).
  Power-law NLED Eqs.(42),(43): p_theta = alpha_e rho,
      rho = C0 / r^{2(alpha_e+1)}.
  Fluid Sec.V.C: p_theta = rho(1+kappa rho),
      rho = (C0/r^4)/(1 - kappa C0/(2 r^4)),  r0 = (|kappa| C0/2)^{1/4}.
Units: 8pi=G=c=1, lambda=1, kappa=-1. float64.
"""
import json
import numpy as np
from scipy.optimize import brentq

kap = -1.0
out = {"claim": "G5-2(a,b,c) EiBI obstructions", "source": "arXiv:1807.07941v2, transcribed in-run",
       "kappa": kap}

# ---------------- families from the printed equations ----------------
def maxwell(ae, C0, r):
    rho = C0 / r**(2 * (ae + 1))
    return rho, -rho, ae * rho

def fluid(C0, r):
    rho = (C0 / r**4) / (1.0 - kap * C0 / (2.0 * r**4))
    return rho, -rho, rho * (1.0 + kap * rho)

# ---------------- (a) fluid sound speed, derived two ways ----------------
# Analytic: p_t(rho)=rho+kappa rho^2  =>  dp_t/drho = 1+2 kappa rho.
# Throat: 1+kappa rho(r0)=0 => rho(r0)=1/|kappa| => c_t^2 = 1-2 = -1.
# Numeric cross-check: finite-difference dp_t/drho along the family's rho(r).
res_a = {}
for C0 in (2.0, 0.5, 1.0, 5.0):
    r0 = (abs(kap) * C0 / 2.0) ** 0.25
    r = np.geomspace(r0, 1e3, 200001)
    rho, pr, pt = fluid(C0, r)
    ct2 = 1.0 + 2.0 * kap * rho
    # centred FD of p_t(rho(r)) w.r.t. rho(r), interior points
    fd = np.gradient(pt, rho)
    iz = int(np.argmin(np.abs(rho - 0.5 / abs(kap))))
    res_a[f"C0={C0}"] = {
        "r0": float(r0), "rho_throat": float(rho[0]),
        "one_plus_kappa_rho_throat": float(1 + kap * rho[0]),
        "ct2_throat_analytic": float(ct2[0]),
        "ct2_throat_FD_pt_vs_rho": float(fd[0]),
        "ct2_min": float(np.min(ct2)), "ct2_asymptote": float(ct2[-1]),
        "ct2_zero_r_numeric": float(r[iz]),
        "ct2_zero_r_analytic_(3C0/2)^(1/4)": float((1.5 * C0) ** 0.25),
        "neg_shell": [float(r0), float(r[iz])],
    }
out["a_fluid_ct2"] = res_a

# ---------------- (b) NLED branch: EoS derivative AND EM mode speed ----------------
# EoS derivative: dp_t/drho = alpha_e exactly (p_t = alpha_e rho).
# Independent physical check: for phi(F)=F^beta, alpha_e=1/(2 beta-1), the
# NLED photon effective-metric speed for one polarisation is
# c^2 = phi_F/(phi_F + 2F phi_FF) = 1/(2 beta - 1) = alpha_e  (the other
# polarisation is luminal). So the sign of alpha_e IS a propagation sign.
res_b = {}
for ae in (1.0, 0.5, 0.0, -0.5, -1.0):
    if ae == 0.0:
        beta = np.inf; em = 0.0
    else:
        beta = (1.0 + ae) / (2.0 * ae)
        em = 1.0 / (2.0 * beta - 1.0)
    res_b[f"alpha_e={ae}"] = {"dpt_drho": float(ae), "beta_from_alpha": float(beta),
                              "EM_mode_c2_phiF/(phiF+2FphiFF)": float(em),
                              "gradient_unhealthy": bool(ae < 0)}
out["b_NLED"] = res_b

# ---------------- (c) Omega block from Eq.(7), derived fresh ----------------
# q_{mu nu} = g_{mu sigma} Omega^sigma_nu (diagonal): from Eq.(7),
#   Omega^t_t = q_tt/g_tt = 1/[tau(1+kappa rho)],
#   Omega^r_r = 1/[tau(1-kappa p_r)],  Omega^th_th = 1/[tau(1-kappa p_theta)].
# With p_r=-rho: (1-kappa p_r)=(1+kappa rho), so on the r>r0 branch
# (all factors > 0) tau = 1/[(1+kappa rho)(1-kappa p_theta)], giving
#   w_t = w_r = 1-kappa p_theta,   w_theta = w_phi = 1+kappa rho,
#   det Omega = (1-kappa p_theta)^2 (1+kappa rho)^2.
def omega_eigs(rho, pt):
    wt = 1.0 - kap * pt
    wth = 1.0 + kap * rho
    return wt, wth, wt**2 * wth**2

res_c = {}
for name, fam, C0, r0 in (("maxwell_ae=1_C0=1", maxwell, 1.0, 1.0),
                          ("fluid_C0=2", fluid, 2.0, 1.0),
                          ("fluid_genuine_C0=0.5", fluid, 0.5, (0.5 / 2) ** 0.25),
                          ("maxwell_genuine_ae=1_C0=0.25", maxwell, 0.25, 0.25 ** 0.25)):
    r = np.geomspace(r0, 1e3, 200001)
    if name.startswith("maxwell"):
        rho, pr, pt = fam(1.0, C0, r)
    else:
        rho, pr, pt = fam(C0, r)
    wt, wth, det = omega_eigs(rho, pt)
    H = r * np.sqrt(np.maximum(1.0 + kap * rho, 0.0))
    res_c[name] = {
        "w_theta_throat": float(wth[0]), "w_t_throat": float(wt[0]),
        "det_Omega_throat": float(det[0]),
        "det_Omega_min_r>r0": float(np.min(det[1:])),
        "all_eigs_positive_r>r0": bool(np.all(wt[1:] > 0) and np.all(wth[1:] > 0)),
        "H_throat_aux_areal_radius": float(H[0]),
        "w_theta_range_r>r0": [float(np.min(wth[1:])), float(np.max(wth[1:]))],
        "w_t_range": [float(np.min(wt)), float(np.max(wt))],
    }
out["c_Omega"] = res_c
out["c_read"] = ("det Omega = (1-kappa p_t)^2 (1+kappa rho)^2 = 0 at r0 identically, "
                 "because the throat is DEFINED by 1+kappa rho=0; H(r0)=0 as well. "
                 "The g<->q perturbation map divides by these factors, so throat "
                 "boundary conditions for the coupled system cannot be fixed in "
                 "either frame by this map.")

# ---------------- gate echoes: conservation + NCC from printed eqs ----------------
rA = np.geomspace(1.0, 1e3, 200001)
rhoF, _, ptF = fluid(2.0, rA)
# analytic rho' for the fluid closed form
u = 2.0 / rA**4; d = 1.0 - kap * 2.0 / (2.0 * rA**4)
rp = (-4 * u / rA * d - u * (2.0 * kap * 2.0 / rA**5)) / d**2
out["gate"] = {
    "conservation_Eq21_fluid_max_abs": float(np.max(np.abs(rp + 2 * (rhoF + ptF) / rA))),
    "NCC_Eq26_throat_maxwell_ae1": float(2 * kap * (1.0 + 1.0)),
    "NCC_Eq26_throat_fluid": float(2 * kap * (rhoF[0] + ptF[0])),
    "fluid_pt_throat_is_zero": float(ptF[0]),
}
print(json.dumps(out, indent=2))
with open("results/wa_g5_2.json", "w") as fh:
    json.dump(out, fh, indent=2)
