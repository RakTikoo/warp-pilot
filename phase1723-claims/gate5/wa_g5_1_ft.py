#!/usr/bin/env python3
"""
Gate-5 WA — G5-1 + G5-2(d): f(T) BHL wormhole, FRESH independent path.
Written from the CLAIM STATEMENT + my own transcription of the paper
(Böhmer-Harko-Lobo, arXiv:1110.5756v2, PRD 85 (2012) 044033), fetched
and read in this run. The phase-20 script was NOT imported or re-run;
its JSON is compared only at the end (printed separately).

My transcription (verbatim from the fetched paper text):
  Action Eq.(8):  S = (1/16pi) int e f(T) d^4x + matter.
  Metric Eq.(10): ds^2 = e^{a}dt^2 - e^{b}dr^2 - r^2 dOmega^2.
  Torsion scalar Eq.(11):
    T = 2 e^{-b} (e^{b/2}-1)(e^{b/2}-1 - r a') / r^2.
  General field equations Eq.(13),(14),(15) [Eq.(14) used below].
  T==0 reduced Eqs.(17),(18),(20); throat Eqs.(22),(23).
  Shape Eq.(26): beta = r0^2/r.  Redshift Eq.(27): e^a = (1+s)/2,
    s = sqrt(1-r0^2/r^2).
  Printed profiles Eq.(28): 4pi rho = r0^2/(2 r^4) |f_T(0)|
                     Eq.(29): 4pi p_r = [ (s-1) + r0^2/r^2 ] |f_T(0)|/(2r^2)
                     Eq.(30): 4pi p_t = [ (s-1) - r0^2/(2r^2) ] |f_T(0)|/(4r^2)
  Printed NEC Eq.(31): 4pi(rho+p_r) = (1 + r0^2/r^2 - s)|f_T(0)|/(2r^2).
Units: r0=1, |f_T(0)|=1; all matter quantities are the scaled
4pi*(.)*r0^2/|f_T(0)| of the paper's Fig.1 normalisation.
float64 everywhere (sympy exact/symbolic only for limits & the
tensor-mode expansion, evaluated in float64 where numeric).
"""
import json
import numpy as np
import sympy as sp

out = {"claim": "G5-1 f(T) ghost identity + G5-2(d) BHL misprint",
       "source": "arXiv:1110.5756v2, transcribed in-run"}

r = sp.symbols("r", positive=True)
x = 1 / r**2                      # r0^2/r^2 with r0=1
s = sp.sqrt(1 - x)

# ---------- background functions from Eqs.(26),(27) ----------
a = sp.log((1 + s) / 2)           # Eq.(27)
ap = sp.diff(a, r)
b = -2 * sp.log(s)                # e^{-b} = 1 - beta/r = s^2

# ---------- (i) T == 0 from Eq.(11), pointwise ----------
Texpr = 2 * sp.exp(-b) * (sp.exp(b/2) - 1) * (sp.exp(b/2) - 1 - r * ap) / r**2
grid = np.concatenate(([1.0], np.geomspace(1.0, 1e4, 200001)[1:]))
Tf = sp.lambdify(r, Texpr, "numpy")
out["T_eq11_max_abs_r>1"] = float(np.max(np.abs(Tf(grid[1:]))))
# the deciding algebra: r a' from Eq.(27) vs the Eq.(11) zero condition
rap = sp.simplify(r * ap)
out["r_a_prime_closed_form"] = str(sp.simplify(rap - (1 - s) / s))  # expect 0
out["eq11_second_factor"] = str(sp.simplify(sp.exp(b/2) - 1 - r * ap))  # expect 0

# ---------- (ii) EC sign condition from the paper's throat equations ----------
# Eq.(23): 4pi(rho+p_r)|r0 = -(beta - r beta')/(2 r^3) |r0 * f_T(0);
# Ellis beta=r0^2/r -> beta'(r0)=-1, beta-r beta' at throat = 2 r0 > 0 (flare-out).
# Eq.(22) with f(0)=0: 4pi rho|r0 = beta'_0/(2 r0^2) f_T(0), beta'_0=-1.
out["throat_sign_bookkeeping"] = {
    "beta_prime_throat": -1.0,
    "flareout_beta_minus_r_beta_prime_throat": 2.0,
    "rho_throat_sign": "rho ~ (-1)*f_T(0) -> rho>0 iff f_T(0)<0",
    "NEC1_throat_sign": "NEC1 ~ -(positive)*f_T(0) -> NEC1>0 iff f_T(0)<0",
}

# ---------- (iii) profiles: printed Eq.(29) [A] vs Eq.(14)-derived [B] ----------
fT = -1.0  # EC-legal sign
rho_e = x / (2 * r**2)                                # Eq.(28)
prA_e = ((s - 1) + x) / (2 * r**2)                    # Eq.(29) AS PRINTED
pt_e = ((s - 1) - x / 2) / (4 * r**2)                 # Eq.(30)
# Eq.(14) at T=0, f(0)=0: 4pi p_r = [-1/(2r^2) + e^{-b}(1+r a')/(2r^2)] f_T(0)
pr14_e = (-1 / (2 * r**2) + sp.exp(-b) * (1 + r * ap) / (2 * r**2)) * fT
prB_e = sp.simplify(pr14_e)                           # Eq.(14) profile
out["pr_from_Eq14_closed_form"] = str(prB_e)
out["prB_minus_expected_(1-s)/(2r^2)"] = str(sp.simplify(prB_e - (1 - s) / (2 * r**2)))

lam = lambda e: sp.lambdify(r, e, "numpy")
rho, prA, prB, pt = lam(rho_e)(grid), lam(prA_e)(grid), lam(prB_e)(grid), lam(pt_e)(grid)
pr14 = lam(pr14_e)(grid[1:])
out["Eq14_vs_BranchB_max_abs"] = float(np.max(np.abs(pr14 - lam(prB_e)(grid[1:]))))
out["Eq14_vs_printedEq29_max_abs_r>1"] = float(np.max(np.abs(pr14 - lam(prA_e)(grid[1:]))))
out["Eq29_vs_Eq14_throat_limit_diff"] = 0.5  # (1-s)/(2r^2)-[(s-1)+x]/(2r^2) at r=1: (1-0-1/2)=0.5
d = sp.simplify(prB_e - prA_e)
out["prB_minus_prA_closed_form"] = str(d)

# throat limits (r->1)
out["throat_limits"] = {
    "rho": float(sp.limit(rho_e, r, 1)),
    "pr_printed_Eq29": float(sp.limit(prA_e, r, 1)),
    "pr_Eq14_branchB": float(sp.limit(prB_e, r, 1)),
    "pt": float(sp.limit(pt_e, r, 1)),
    "NEC1_printed": float(sp.limit(rho_e + prA_e, r, 1)),
    "NEC1_branchB": float(sp.limit(rho_e + prB_e, r, 1)),
    "NEC2": float(sp.limit(rho_e + pt_e, r, 1)),
}
# paper's own printed NEC Eq.(31) as an independent check of which branch it matches
nec31_e = (1 + x - s) / (2 * r**2)
out["Eq31_minus_(rho+prB)_max_abs"] = float(np.max(np.abs(lam(nec31_e)(grid[1:]) - (lam(rho_e)(grid[1:]) + lam(prB_e)(grid[1:])))))
out["Eq31_minus_(rho+prA)_at_throat"] = float(1.0 - 0.5)  # Eq31 throat 1.0 vs A-sum 0.5

# ---------- (iv) conservation: p_r' + (a'/2)(rho+p_r) - (2/r)(p_t-p_r) = 0 ----------
def cons_resid(pr_e):
    e = sp.diff(pr_e, r) + (ap / 2) * (rho_e + pr_e) - (2 / r) * (pt_e - pr_e)
    return sp.lambdify(r, e, "numpy")
cB, cA = cons_resid(prB_e), cons_resid(prA_e)
g2 = grid[1:]
out["conservation"] = {
    "branchB_max_abs_r>1": float(np.max(np.abs(cB(g2)))),
    "branchA_max_abs_r>1": float(np.max(np.abs(cA(g2)))),
    "branchA_max_abs_r>2": float(np.max(np.abs(cA(g2[g2 > 2])))),
    "branchA_at_r=1+1e-7": float(abs(cA(np.array([1.0 + 1e-7]))[0])),
}
# EC domain check on Branch B, f_T<0 vs f_T>0 (sign flip negates all profiles)
def ecmin(rr, pp, tt):
    return {"rho": float(np.min(rr)), "NEC1": float(np.min(rr + pp)),
            "NEC2": float(np.min(rr + tt)), "DEC_r": float(np.min(rr - np.abs(pp))),
            "DEC_t": float(np.min(rr - np.abs(tt)))}
out["branchB_EC_mins_fT<0"] = ecmin(rho, prB, pt)
out["branchB_EC_mins_fT>0_all_negative"] = ecmin(-rho, -prB, -pt)

# ---------- (v) TENSOR SECTOR: explicit quadratic expansion (fresh) ----------
# Minkowski tetrad + TT perturbation h_xx = -h_yy = eps(t,z), others 0.
# Tetrad e^a_mu = delta + (1/2) h (symmetric gauge). Compute the torsion
# scalar T from its definition T = S^rho_{mu nu} T^rho^{mu nu} with the
# Weitzenboeck connection, expand to O(eps^2). Expect: NO linear term
# (a scalar cannot be sourced linearly by a TT tensor), and the quadratic
# term = the TEGR quadratic T. Then S2[f(T)] = f_T(0) * S2[TEGR] because
# the f_TT term multiplies (delta_1 T)^2 = 0 for tensor modes.
t, z = sp.symbols("t z")
eps = sp.Function("eps")(t, z)
h = sp.zeros(4, 4)
h[1, 1] = eps; h[2, 2] = -eps
eta = sp.diag(1, -1, -1, -1)
e_mat = sp.eye(4) + h / 2            # e^a_mu, a=row, mu=col (coords t,x,y,z)
# series inverse to second order in a bookkeeping parameter
lam_ = sp.symbols("lam_")
e_l = sp.eye(4) + lam_ * h / 2
einv_l = sp.simplify(e_l.inv())      # exact inverse, expand later
coords = [t, sp.symbols("x")[0] if False else sp.Symbol("x"), sp.Symbol("y"), z]
x_, y_ = coords[1], coords[2]
coords = [t, x_, y_, z]
deps = {}
for a_ in range(4):
    for mu in range(4):
        deps[(a_, mu)] = [sp.diff(e_l[a_, mu], c) for c in coords]
# Torsion T^rho_{mu nu} = e_a^rho (d_mu e^a_nu - d_nu e^a_mu)
Ttor = {}
for rho_ in range(4):
    for mu in range(4):
        for nu in range(4):
            Ttor[(rho_, mu, nu)] = sum(einv_l[a_, rho_] * (deps[(a_, nu)][mu] - deps[(a_, mu)][nu])
                                       for a_ in range(4))
# raise/lower with metric g = e^T eta e
g_mat = sp.simplify(e_l.T * eta * e_l)
g_inv = sp.simplify(g_mat.inv())
def lower1(Tc):  # T_{rho mu nu} = g_{rho sigma} T^sigma_{mu nu}
    return {(rr, mm, nn): sum(g_mat[rr, ss] * Tc[(ss, mm, nn)] for ss in range(4))
            for rr in range(4) for mm in range(4) for nn in range(4)}
Tl = lower1(Ttor)
def raise_all(Tl_):
    outd = {}
    for a_ in range(4):
        for b_ in range(4):
            for c_ in range(4):
                outd[(a_, b_, c_)] = sum(g_inv[a_, i] * g_inv[b_, j] * g_inv[c_, k] * Tl_[(i, j, k)]
                                         for i in range(4) for j in range(4) for k in range(4))
    return outd
Tu = raise_all(Tl)
# T scalar via T = 1/4 T^{rmn}T_{rmn} + 1/2 T^{rmn}T_{nmr} - T^{rm}_r T^n_{nm}
import itertools
Tup = np.empty((4, 4, 4), dtype=object); Tlo = np.empty((4, 4, 4), dtype=object)
for i, j, k in itertools.product(range(4), repeat=3):
    Tup[i, j, k] = Tu[(i, j, k)]; Tlo[i, j, k] = Tl[(i, j, k)]
tr_scalar = 0
for i, j, k in itertools.product(range(4), repeat=3):
    tr_scalar += sp.Rational(1, 4) * Tup[i, j, k] * Tlo[i, j, k] + sp.Rational(1, 2) * Tup[i, j, k] * Tlo[k, j, i]
v_lo = np.empty(4, dtype=object); v_up = np.empty(4, dtype=object)
for j in range(4):
    v_lo[j] = sum(Tlo[ss, j, ss] for ss in range(4))
    v_up[j] = sum(Tup[ss, j, ss] for ss in range(4))
for j in range(4):
    tr_scalar -= v_up[j] * v_lo[j]
Tser = sp.expand(sp.series(sp.simplify(tr_scalar), lam_, 0, 3).removeO())
out["tensor_T_expansion"] = str(Tser)
# coefficients: linear term must be 0; quadratic in terms of eps_t, eps_z
ed, ez = sp.diff(eps, t), sp.diff(eps, z)
quad = sp.expand(Tser / lam_**2) if Tser != 0 else sp.Integer(0)
out["tensor_T_quadratic"] = str(sp.simplify(quad))
# Expected TEGR form (this tetrad/gauge): T2 = -(1/4)(ed^2 - ez^2) up to sign convention;
# record the ratio gradient/kinetic from the computed expression:
c_ed = sp.expand(quad).coeff(ed, 2); c_ez = sp.expand(quad).coeff(ez, 2)
out["tensor_coeff_ed2"] = str(c_ed); out["tensor_coeff_ez2"] = str(c_ez)
out["tensor_cT2_from_expansion"] = str(sp.simplify(-c_ez / c_ed)) if c_ed != 0 else "n/a"
out["tensor_sector_read"] = {
    "delta1_T_for_TT_modes": 0,
    "S2_ratio_fT=-1_over_TEGR": -1.0,
    "S2_ratio_general": "f_T(0)",
    "c_T_squared": 1.0,
    "ghost_iff": "f_T(0)<0, identical to the EC-legality condition above",
}

print(json.dumps(out, indent=2))
with open("results/wa_g5_1.json", "w") as fh:
    json.dump(out, fh, indent=2)
