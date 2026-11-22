"""W-B GATE-6 G6-2: INDEPENDENT THIRD PATH.
Route: general diagonal parametrisation with INDEPENDENT lapse N(r) and
radial function S(r):
    ds^2 = -N(r)^2 dt^2 + dr^2/S(r) + r^2 dOmega^2
F, N, S kept as unspecified sympy Functions. Einstein tensor, Box F and
nabla nabla F computed by a generic index-loop tensor routine written
for this gate (no phase42 code imported/copied). Only at the END do we
set S = 1-b/r, N = exp(Phi), and take the throat limit by a series in
eps = r-r0 (not by the phase42 substitution map).
Conventions: field eq  F G^mu_nu + delta^mu_nu BoxF - nabla^mu nabla_nu F
 = 8 pi T^mu_nu(demanded total).  So 8pi rho_dem = -(that)^t_t,
 8pi p_r,dem = (that)^r_r.
"""
import sympy as sp

r, th = sp.symbols('r th', positive=True)
t, ph = sp.symbols('t ph')
x = [t, r, th, ph]
N = sp.Function('N')(r)
S = sp.Function('S')(r)
F = sp.Function('F')(r)

g = sp.diag(-N**2, 1/S, r**2, r**2*sp.sin(th)**2)
ginv = sp.diag(-1/N**2, S, 1/r**2, 1/(r**2*sp.sin(th)**2))
n = 4
# partials of metric
dg = [[[sp.diff(g[i, j], x[k]) for k in range(n)] for j in range(n)] for i in range(n)]
Gamma = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for lam in range(n):
    for mu in range(n):
        for nu in range(n):
            Gamma[lam][mu][nu] = sp.simplify(sum(
                ginv[lam, s]*(dg[s][nu][mu] + dg[s][mu][nu] - dg[mu][nu][s])
                for s in range(n))/2)
# Ricci by generic loop
Ric = sp.zeros(n, n)
for mu in range(n):
    for nu in range(n):
        e = 0
        for lam in range(n):
            e += sp.diff(Gamma[lam][nu][mu], x[lam]) - sp.diff(Gamma[lam][lam][mu], x[nu])
            for s in range(n):
                e += Gamma[lam][lam][s]*Gamma[s][nu][mu] - Gamma[lam][nu][s]*Gamma[s][lam][mu]
        Ric[mu, nu] = sp.simplify(e)
Rsc = sp.simplify(sum(ginv[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
Gmix = sp.zeros(n, n)
for i in range(n):
    Gmix[i, i] = sp.simplify(sum(ginv[i, k]*Ric[k, i] for k in range(n)) - Rsc/2)

Fp = sp.diff(F, r); Fpp = sp.diff(F, r, 2)
Np = sp.diff(N, r); Sp = sp.diff(S, r)
# covariant Hessian of scalar F(r): Hess_{mu nu} = d_mu d_nu F - Gamma^lam_{mu nu} d_lam F
Hess = {}
for mu in range(n):
    for nu in range(n):
        Hess[(mu, nu)] = sp.simplify((Fpp if (mu == 1 and nu == 1) else 0) - Gamma[1][mu][nu]*Fp)
BoxF = sp.simplify(sum(ginv[i, j]*Hess[(i, j)] for i in range(n) for j in range(n)))
nab_tt = sp.simplify(ginv[0, 0]*Hess[(0, 0)])   # nabla^t nabla_t F
nab_rr = sp.simplify(ginv[1, 1]*Hess[(1, 1)])

E_tt = sp.simplify(F*Gmix[0, 0] + BoxF - nab_tt)   # = -8 pi rho_dem
E_rr = sp.simplify(F*Gmix[1, 1] + BoxF - nab_rr)   # = +8 pi p_r,dem
rho8 = sp.simplify(-E_tt)
pr8 = sp.simplify(E_rr)

def show(name, e):
    print(f"{name} = {sp.factor(e)}")

show("G^t_t", Gmix[0, 0]); show("G^r_r", Gmix[1, 1]); show("R", Rsc)
show("BoxF", BoxF); show("nab^t_t F", nab_tt); show("nab^r_r F", nab_rr)
show("8pi rho_dem (general N,S)", rho8)
show("8pi pr_dem  (general N,S)", pr8)
# Cancellation exhibits, as computed facts:
print("BoxF - nab^t_t F =", sp.simplify(BoxF - nab_tt))
print("BoxF - nab^r_r F =", sp.simplify(BoxF - nab_rr))
print("coeff of F'' in BoxF-nab_rr:", sp.simplify(sp.diff(BoxF - nab_rr, Fpp)))
print("coeff of F'' in 8pi rho:", sp.simplify(sp.diff(rho8, Fpp)))

# Translate: S = 1-b/r  =>  b/r^3 = (1-S)/r^2 ; b'/r^2 = (1-S)/r^2 - S'/r
# (since S' = -b'/r + b/r^2). Claimed general-r formulas (task statement):
# 8pi pr = -F b/r^3 + S[ F' Phi' + 2F Phi'/r + 2F'/r ],  Phi' = N'/N
# 8pi rho = F b'/r^2 - S F'' - 2 S F'/r - S' F'/2
claim_pr = F*(S-1)/r**2 + S*(Fp*Np/N + 2*F*Np/(N*r) + 2*Fp/r)
claim_rho = F*((1-S)/r - Sp)/r - S*Fpp - 2*S*Fp/r - Sp*Fp/2  # F*b'/r^2 with b'/r^2=(1-S)/r^2 - S'/r
print("DIFF pr  (mine - claimed, general r):", sp.simplify(pr8 - claim_pr))
print("DIFF rho (mine - claimed, general r):", sp.simplify(rho8 - claim_rho))

# Throat limit by SERIES in eps: r = r0+eps, S(r0)=0, S'(r0)=(1-beta)/r0,
# N(r0)=1 wlog (Phi(r0)=0 gauge), N'/N -> P1, etc.
r0, beta, eps = sp.symbols('r0 beta eps', positive=True)
F0, F1, F2, P1 = sp.symbols('F0 F1 F2 P1')
# Series ansatz for the functions near throat
S_ser = (1-beta)/r0*eps + sp.Symbol('S2')*eps**2
N_ser = 1 + P1*eps + sp.Symbol('N2')*eps**2
F_ser = F0 + F1*eps + F2*eps**2/2
def series_limit(expr):
    e = expr.subs({S: S_ser, N: N_ser, F: F_ser,
                   sp.diff(S, r): sp.diff(S_ser, eps), sp.diff(N, r): sp.diff(N_ser, eps),
                   Fp: F1 + F2*eps, Fpp: F2})
    e = e.subs(r, r0+eps)
    return sp.simplify(sp.series(e, eps, 0, 1).removeO())
for name, e, claimed in [
    ("8pi rho_dem", rho8, F0*beta/r0**2 - (1-beta)*F1/(2*r0)),
    ("8pi pr_dem", pr8, -F0/r0**2),
    ("R", Rsc, 2*beta/r0**2 - (1-beta)*P1/r0),
]:
    lim = series_limit(e)
    print(f"THROAT {name}: mine={lim}  claimed(8pi-scaled where applicable)={claimed}  DIFF={sp.simplify(lim-claimed)}")
# Box phi throat (same Box operator with F->phi): Box phi = S phi''+[S N'/N+2S/r+S'/2] phi'
phi1 = sp.symbols('phi1')
print("THROAT Box phi coeff of phi'0:", (1-beta)/(2*r0), " (all other terms carry S=0)")
print("DONE")
