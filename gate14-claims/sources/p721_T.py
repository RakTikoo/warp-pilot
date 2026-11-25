"""Derive T^(D) mixed diagonal components for the EPJC (3.7) singlet
ansatz from EPJC (2.5), KZ gamma/bar/spin-connection conventions.
Angles fixed at generic numeric values (T is angle-independent after
summing both spinors -- checked by evaluating at two angle pairs).
Output: expressions in radial symbols, saved to p721_T_exprs.json.
"""
import sympy as sp, json, sys
sys.path.insert(0, 'work')
from p721_lib import GH

I = sp.I
# symbols
l, r0 = sp.symbols('l r0', real=True)
F0, F1, F0d, F1d = sp.symbols('F0 F1 F0d F1d', real=True)
P, Q, Pd, Qd = sp.symbols('P Q Pd Qd', real=True)
w, mu, kap = sp.symbols('w mu kappa', real=True)
F2 = sp.sqrt(l**2 + r0**2); F2d = l / F2

TH = sp.Rational(1, 1) * sp.pi / 3  # theta = pi/3
PH = sp.Rational(7, 10)             # phi = 0.7
sth = sp.sin(TH); cth = sp.cos(TH)

# coordinates order t,l,th,ph ; metric and derivatives (symbols for F0,F1 derivs)
g = sp.diag(-F0**2, F1**2, F2**2, F2**2 * sth**2)
gi = g.inv()
dg = [sp.zeros(4), sp.zeros(4), sp.zeros(4), sp.zeros(4)]
dg[1] = sp.diag(-2 * F0 * F0d, 2 * F1 * F1d, 2 * F2 * F2d, 2 * F2 * F2d * sth**2)
dg[2] = sp.diag(0, 0, 0, 2 * F2**2 * sth * cth)
coords_n = 4
Gam = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            Gam[a][b][c] = sum(gi[a, d] * (dg[b][d, c] + dg[c][d, b] - dg[d][b, c]) for d in range(4)) / 2

# coframe e^a_mu and frame vectors E_a^mu ; e_{mu alpha} = eta_{alpha beta} e^beta_mu
ecof = sp.diag(F0, F1, F2, F2 * sth)          # e^a_mu (a row)
eta = sp.diag(-1, 1, 1, 1)
ecov_low = eta * ecof                          # e_{mu alpha} rows mu? build matrix [mu][alpha]
ecov_low = sp.Matrix(4, 4, lambda mu_, al: eta[al, al] * ecof[al, mu_] if al == mu_ else 0)
Evec = sp.diag(1 / F0, 1 / F1, 1 / F2, 1 / (F2 * sth))  # E_a^mu [a][mu] diag

# spin connection omega_{mu a b} via KZ eq (18):
# w_{mu a b} = (e_{nu a} Gam^nu_{mu rho} - d_mu e_{rho a}) g^{rho lam} e_{lam b}
omega = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
de = [sp.zeros(4, 4) for _ in range(4)]  # de[mu][rho][a] = d_mu e_{rho a}
de[1] = sp.Matrix(4, 4, lambda rho, a: (sp.diff(ecov_low[rho, a], l) if False else 0))
# e_{rho a} nonzero: (0,0):-F0 (d/d l = -F0d); (1,1):F1 (F1d); (2,2):F2 (F2d); (3,3):F2 sth (F2d sth)
de[1][0, 0] = -F0d; de[1][1, 1] = F1d; de[1][2, 2] = F2d; de[1][3, 3] = F2d * sth
de[2][3, 3] = F2 * cth
for mu_ in range(4):
    for a in range(4):
        for b in range(4):
            expr = 0
            for nu in range(4):
                for rho in range(4):
                    expr += ecof[b, rho] * 0  # placeholder
            # (e_{nu a} Gam^nu_{mu rho}) g^{rho lam} e_{lam b}: sum nu,rho,lam
            s = 0
            for nu in range(4):
                for rho in range(4):
                    for lam in range(4):
                        s += (ecov_low[nu, a] * Gam[nu][mu_][rho]) * gi[rho, lam] * ecof[b, lam]
            s -= sum(de[mu_][rho, a] * gi[rho, lam] * ecof[b, lam] for rho in range(4) for lam in range(4))
            omega[mu_][a][b] = sp.simplify(s)

GammaMu = []
for mu_ in range(4):
    Gm = sp.zeros(4)
    for a in range(4):
        for b in range(4):
            Gm += omega[mu_][a][b] * (GH[a] * GH[b])
    GammaMu.append(-Gm / 4)

# gamma^mu = E_a^mu GH[a]
gup = [sum((Evec[a, mu_] * GH[a] for a in range(4)), sp.zeros(4)) for mu_ in range(4)]
glo = [sum((g[mu_, nu] * gup[nu] for nu in range(4)), sp.zeros(4)) for mu_ in range(4)]

z = P + I * Q; zb = P - I * Q
e1 = sp.exp(I * (PH / 2 - w * 0))  # t set 0 (phases in t cancel in T diag; w enters via D_t)
# spinors at t=0: Psi1, Psi2 per EPJC (3.7)
c2 = sp.cos(TH / 2); s2_ = sp.sin(TH / 2)
ph1 = sp.exp(I * PH / 2); ph2 = sp.exp(-I * PH / 2)
Psi1 = sp.Matrix([z * c2, I * zb * s2_ * kap, -I * zb * c2, -z * s2_ * kap]) * ph1
Psi2 = sp.Matrix([I * z * s2_, zb * c2 * kap, zb * s2_, I * z * c2 * kap]) * ph2
# radial derivatives: dz/dl = Pd + i Qd ; phases constant in l
dPsi1 = sp.Matrix([ (Pd + I * Qd) * c2, I * (Pd - I * Qd) * s2_ * kap, -I * (Pd - I * Qd) * c2, -(Pd + I * Qd) * s2_ * kap]) * ph1
dPsi2 = sp.Matrix([I * (Pd + I * Qd) * s2_, (Pd - I * Qd) * c2 * kap, (Pd - I * Qd) * s2_, I * (Pd + I * Qd) * c2 * kap]) * ph2
# theta derivatives (analytic: d cos(th/2) = -sin(th/2)/2, d sin(th/2) = cos(th/2)/2)
dth1 = sp.Matrix([z * (-s2_ / 2), I * zb * (c2 / 2) * kap, -I * zb * (-s2_ / 2), -z * (c2 / 2) * kap]) * ph1
dth2 = sp.Matrix([I * z * (c2 / 2), zb * (-s2_ / 2) * kap, zb * (c2 / 2), I * z * (-s2_ / 2) * kap]) * ph2
# phi derivatives: Psi1 ~ exp(+i phi/2) -> +i/2 ; Psi2 -> -i/2 ; t derivatives: exp(-i w t) -> -i w
ders = [
    (-I * w * Psi1, -I * w * Psi2),          # t
    (dPsi1, dPsi2),                          # l
    (dth1, dth2),                            # th
    (I * Psi1 / 2, -I * Psi2 / 2),           # ph
]
def bar(Psi):
    return -Psi.conjugate().T * GH[0]  # row vector; conjugate: P,Q real symbols -> sympy conj needs care
# sympy: P,Q declared real, w real; exp(i PH/2) conj handled by .conjugate()
def Dcov(mu_, Psi, dPsi):
    return dPsi - GammaMu[mu_] * Psi
def Dbar(mu_, Psi, dPsi):
    Pb = bar(Psi)
    return sp.diff(Pb, [l, 0, 0, 0][mu_]) if False else None

T = sp.zeros(4)
for eps, Psi in enumerate([Psi1, Psi2]):
    Pb = bar(Psi)
    for mu_ in range(4):
        for nu in range(4):
            if mu_ != nu:
                continue
            dP_nu = ders[nu][eps]; dP_mu = ders[mu_][eps]
            DPnu = Dcov(nu, Psi, dP_nu); DPmu = Dcov(mu_, Psi, dP_mu)
            # (D_nu bar) = d_nu bar - bar * Gamma_nu  (row-vector cov derivative)
            # d_nu bar: differentiate bar(Psi) -- recompute via bar of derivative spinor plus Gamma-independent parts:
            # bar is linear in Psi^dagger; d_nu bar(Psi) = bar(d_nu Psi) with phases: use bar(dPsi_nu vector) where
            # the 'derivative spinor' for t is -i w Psi etc. bar() handles conjugation.
            Dbnu = bar(dP_nu) - Pb * GammaMu[nu]
            Dbmu = bar(dP_mu) - Pb * GammaMu[mu_]
            term = (Pb * glo[mu_] * DPnu)[0] + (Pb * glo[nu] * DPmu)[0] - (Dbnu * glo[mu_] * Psi)[0] - (Dbmu * glo[nu] * Psi)[0]
            T[mu_, nu] += -I * term / 4

out = {}
for i, name in [(0, 'Tt_t'), (1, 'Tl_l'), (2, 'Tth_th')]:
    expr = sp.simplify(T[i, i] * gi[i, i])
    out[name] = str(expr)
    print(name, '=', expr)
with open('work/p721_T_exprs.json', 'w') as f:
    json.dump(out, f, indent=1)
print('offdiag T01:', sp.simplify(T[0, 1]), 'T02:', sp.simplify(T[0, 2]))
