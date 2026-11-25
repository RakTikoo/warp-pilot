"""W-B2 Gate-15: channel functionals LK, LR, LRn derived from scratch.

Derivation: conformal 2-metric gamma_tilde = diag(-P, Q), P = A/r^2, Q = Bm/r^2.
Ricci scalar of diag(-P,Q) from Christoffels (same route as W-A, re-derived
here symbolically):
  R = (-2 P Q P'' + P P' Q' + Q (P')^2) / (2 P^2 Q^2).
Rtilde_n = (r/sqrt(Bm)) d_r Rtilde ;  J_K = A'/(A sqrt(Bm)).
Linearise about the MK background at Sigma (r=1000) in the perturbation jets
(U,U',U'',U''' ; V,V',V'') with sympy, evaluated at 50 digits (mpmath).
Also: A1 member cross-check (direct nonlinear evaluation on member jets),
A2 truncation anchor, S-identity check.
"""
import json
import sympy as sp
from mpmath import mp, mpf

mp.dps = 50
OUT = "/home/hatch/workspace/warp-pilot/gate15/work_b2/wb2_functionals.json"

# ---------- background ----------
beta = mpf("2.142611"); gamma = mpf("1e-28"); kpar = mpf("-2.28996e-9")
Cpar = beta * (2 - 3 * beta * gamma)
rS = mpf(1000)

def f_bg(r):
    return 1 - 3 * beta * gamma - Cpar / r + gamma * r - kpar * r**2
def fp_bg(r):
    return Cpar / r**2 + gamma - 2 * kpar * r
def fpp_bg(r):
    return -2 * Cpar / r**3 - 2 * kpar
def fppp_bg(r):
    return 6 * Cpar / r**4

f0, f1, f2, f3 = f_bg(rS), fp_bg(rS), fpp_bg(rS), fppp_bg(rS)
# Bm background = 1/f and derivatives
g0 = 1 / f0
g1 = -f1 / f0**2
g2 = -f2 / f0**2 + 2 * f1**2 / f0**3
g3 = -f3 / f0**2 + 6 * f1 * f2 / f0**3 - 6 * f1**3 / f0**4

# ---------- symbolic Rtilde in terms of A,Bm jets ----------
A, A1, A2, A3, B, B1, B2, r, t = sp.symbols("A A1 A2 A3 B B1 B2 r t")
u, u1, u2, u3, v, v1, v2 = sp.symbols("u u1 u2 u3 v v1 v2")
P = A / r**2
P1 = A1 / r**2 - 2 * A / r**3
P2 = A2 / r**2 - 4 * A1 / r**3 + 6 * A / r**4
Q = B / r**2
Q1 = B1 / r**2 - 2 * B / r**3
Rexpr = (-2 * P * Q * P2 + P * P1 * Q1 + Q * P1**2) / (2 * P**2 * Q**2)
Rexpr = sp.simplify(Rexpr)
# dR/dr: R depends on (A,A1,A2,B,B1) and explicitly on r
dR = (sp.diff(Rexpr, A) * A1 + sp.diff(Rexpr, A1) * A2 + sp.diff(Rexpr, A2) * A3
      + sp.diff(Rexpr, B) * B1 + sp.diff(Rexpr, B1) * B2 + sp.diff(Rexpr, r))
Rn_expr = r / sp.sqrt(B) * dR
JK_expr = A1 / (A * sp.sqrt(B))

bg = {A: sp.Float(str(f0), 50), A1: sp.Float(str(f1), 50), A2: sp.Float(str(f2), 50),
      A3: sp.Float(str(f3), 50), B: sp.Float(str(g0), 50), B1: sp.Float(str(g1), 50),
      B2: sp.Float(str(g2), 50), r: sp.Float("1000", 50)}
pert = {A: A + t * u, A1: A1 + t * u1, A2: A2 + t * u2, A3: A3 + t * u3,
        B: B + t * v, B1: B1 + t * v1, B2: B2 + t * v2}

def lin_coeffs(expr, vars_):
    e = expr.subs(pert)
    lin = sp.expand(sp.diff(e, t).subs(t, 0))
    out = []
    for var in vars_:
        c = sp.expand(lin).coeff(var, 1)
        out.append(mpf(str(c.subs(bg).evalf(50))))
    const = mpf(str(sp.expand(lin).subs({x: 0 for x in vars_}).subs(bg).evalf(50)))
    return out, const

LK, LK0 = lin_coeffs(JK_expr, [u, u1, v])                    # (U, U', V)
LR, LR0 = lin_coeffs(Rexpr, [u, u1, u2, v, v1])              # (U,U',U'',V,V')
LRn, LRn0 = lin_coeffs(Rn_expr, [u, u1, u2, u3, v, v1, v2])  # (U..U''',V,V',V'')
print("LK ", [str(x) for x in LK], "const", LK0)
print("LR ", [str(x) for x in LR], "const", LR0)
print("LRn", [str(x) for x in LRn], "const", LRn0)

# numeric evaluators (nonlinear, for A1)
Rf = sp.lambdify((A, A1, A2, B, B1, r), Rexpr, "mpmath")
Rnf = sp.lambdify((A, A1, A2, A3, B, B1, B2, r), Rn_expr, "mpmath")
JKf = sp.lambdify((A, A1, B), JK_expr, "mpmath")

# ---------- A1: member jets ----------
# Exterior jets are (f, 1/f) above. Interior: A_int = exp(2 Phi2),
# Phi2 = a ln r/(1+ln r); Bm_int = 1/(1-b/r), b = r^p, p=0.1.
a_par = mpf("0.27773424114865775"); p_par = mpf("0.1")
rr = sp.symbols("rr", positive=True)
L = sp.log(rr)
Phi = sp.Float(str(a_par), 50) * L / (1 + L)
Aint = sp.exp(2 * Phi)
bfunc = rr**sp.Float("0.1", 50)
Bint = 1 / (1 - bfunc / rr)
int_jets = {}
for name, expr, orders in (("A", Aint, 3), ("B", Bint, 2)):
    for o in range(orders + 1):
        e = expr if o == 0 else sp.diff(expr, rr, o)
        int_jets[f"{name}{o}"] = mpf(str(e.subs(rr, 1000).evalf(50)))
ext_jets = {"A0": f0, "A1": f1, "A2": f2, "A3": f3, "B0": g0, "B1": g1, "B2": g2}
R_int = Rf(int_jets["A0"], int_jets["A1"], int_jets["A2"], int_jets["B0"], int_jets["B1"], rS)
R_ext = Rf(f0, f1, f2, g0, g1, rS)
Rn_int = Rnf(int_jets["A0"], int_jets["A1"], int_jets["A2"], int_jets["A3"],
             int_jets["B0"], int_jets["B1"], int_jets["B2"], rS)
Rn_ext = Rnf(f0, f1, f2, f3, g0, g1, g2, rS)
jump_R = R_ext - R_int
jump_Rn = Rn_ext - Rn_int
print("A1 jump_R  =", jump_R)
print("A1 jump_Rn =", jump_Rn, " (W-A: -0.01531714654192940335)")
print("A1 S00/a0  =", -mpf(4) / 3 * jump_Rn)

# ---------- A2: truncation ----------
# Truncation: U_l(r) = -C r^l / D^(l+1) (l>=1), U_0 = -C/D - 3 beta gamma (r-indep);
# V = -U/f^2 as a function of r; Theta = 0.
def trunc_jets(ell, D):
    if ell == 0:
        U = -Cpar / D - 3 * beta * gamma
        U1 = U2 = U3 = mpf(0)
    else:
        U = -Cpar * rS**ell / D**(ell + 1)
        U1 = ell * U / rS
        U2 = ell * (ell - 1) * U / rS**2
        U3 = ell * (ell - 1) * (ell - 2) * U / rS**3
    # V = -U(r) f(r)^-2 ; derivatives via product rule with h=1/f^2 jets
    h0 = 1 / f0**2
    h1 = -2 * f1 / f0**3
    h2 = -2 * f2 / f0**3 + 6 * f1**2 / f0**4
    V = -U * h0
    V1 = -(U1 * h0 + U * h1)
    V2 = -(U2 * h0 + 2 * U1 * h1 + U * h2)
    return dict(U=U, U1=U1, U2=U2, U3=U3, V=V, V1=V1, V2=V2)

def apply_LK(j): return LK[0] * j["U"] + LK[1] * j["U1"] + LK[2] * j["V"]
def apply_LR(j): return LR[0] * j["U"] + LR[1] * j["U1"] + LR[2] * j["U2"] + LR[3] * j["V"] + LR[4] * j["V1"]
def apply_LRn(j): return (LRn[0] * j["U"] + LRn[1] * j["U1"] + LRn[2] * j["U2"] + LRn[3] * j["U3"]
                          + LRn[4] * j["V"] + LRn[5] * j["V1"] + LRn[6] * j["V2"])

a2 = {}
for ell in range(4):
    row = {}
    for eps in [mpf("0.1"), mpf(1) / 30, mpf("0.01"), mpf("0.003"), mpf("0.001")]:
        D = rS / eps
        j = trunc_jets(ell, D)
        pw = eps**(ell + 1)
        row[str(eps)] = {"B_per": str(j["V"] / pw), "K_per": str(apply_LK(j) / pw),
                         "R_per": str(apply_LR(j) / pw), "Rn_per": str(apply_LRn(j) / pw)}
    a2[f"ell{ell}"] = row
    print("A2 ell", ell, " eps=0.1:", row["0.1"])

# S identity: profile U = delta r^l (delta=1), V=-U/f^2 jets as above with U=r^l
S_id = {}
for ell in range(4):
    U = rS**ell; U1 = ell * U / rS; U2 = ell * (ell - 1) * U / rS**2
    h0 = 1 / f0**2; h1 = -2 * f1 / f0**3
    j = dict(U=U, U1=U1, U2=U2, V=-U * h0, V1=-(U1 * h0 + U * h1))
    S_id[f"S{ell}"] = str(apply_LR(j) / U)
    print("S", ell, "=", S_id[f"S{ell}"], " expected", -(ell - 1) * (ell - 2))

res = {
    "background": {"f0": str(f0), "f1": str(f1), "f2": str(f2), "f3": str(f3),
                   "g0": str(g0), "g1": str(g1), "g2": str(g2), "C": str(Cpar), "Bm0": str(g0)},
    "LK_U_U1_V": [str(x) for x in LK],
    "LR_U_U1_U2_V_V1": [str(x) for x in LR],
    "LRn_U_U1_U2_U3_V_V1_V2": [str(x) for x in LRn],
    "lin_consts": {"LK": str(LK0), "LR": str(LR0), "LRn": str(LRn0)},
    "A1": {"jump_R": str(jump_R), "jump_Rn": str(jump_Rn), "S00_over_alpha0": str(-mpf(4) / 3 * jump_Rn),
           "int_jets": {kk: str(vv) for kk, vv in int_jets.items()},
           "R_int": str(R_int), "R_ext": str(R_ext), "Rn_int": str(Rn_int), "Rn_ext": str(Rn_ext)},
    "A2_truncation": a2,
    "S_identity": S_id,
}
json.dump(res, open(OUT, "w"), indent=1)
print("wrote", OUT)
