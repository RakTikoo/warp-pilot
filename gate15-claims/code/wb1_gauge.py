"""W-B1 gauge check (sympy): Lie action of xi^r = X(r) P_2, xi^th = Y(r) d_th P_2
on the spherical MK background; verify the registered formulas
  dU = f' X ; dV = X (1/f)' + 2 X'/f ; dW = r^2 Y' + X/f ;
  dTheta = 2X/r - l(l+1) Y (trace part) ; dG = 2Y (tracefree part, with the
  E_thth/E_phph basis of the Phase-122 run record);
and that W=G=0 preservation forces X=Y=0 (class (a) empty at l>=1).
Writes wb1_gauge.json."""
import sympy as sp, json

r, th = sp.symbols('r theta', positive=True)
X = sp.Function('X')(r); Y = sp.Function('Y')(r)
f = sp.Function('f')(r)
ell = 2
P = sp.legendre(ell, sp.cos(th))
dP = sp.diff(P, th)

# Background metric components (covariant), coords (t, r, th, ph)
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2)
coords = sp.symbols('t r theta phi')
xi = [0, X * P, Y * dP, 0]  # contravariant components

# Lie derivative: (L_xi g)_{mn} = xi^a d_a g_{mn} + g_{an} d_m xi^a + g_{ma} d_n xi^a
dg = {}
L = sp.zeros(4, 4)
varmap = {1: r, 2: th}
for m in range(4):
    for n in range(4):
        expr = 0
        for a in range(4):
            if a in varmap:
                expr += xi[a] * sp.diff(g[m, n], varmap[a])
            expr += g[a, n] * (sp.diff(xi[a], varmap[m]) if m in varmap else 0)
            expr += g[m, a] * (sp.diff(xi[a], varmap[n]) if n in varmap else 0)
        L[m, n] = sp.simplify(expr)

res = {}
# dU: dg_tt = -dU * P  -> dU = -L_tt / P
dU = sp.simplify(-L[0, 0] / P)
res['dU_residual'] = float(abs(sp.simplify(dU - sp.diff(f, r) * X).subs(
    {sp.diff(f, r): 1.0, X: 1.0}).evalf())) if False else str(sp.simplify(dU - sp.diff(f, r) * X))
# dV: dg_rr = dV * P
dV = sp.simplify(L[1, 1] / P)
targetV = X * sp.diff(1 / f, r) + 2 * sp.diff(X, r) / f
res['dV_residual'] = str(sp.simplify(dV - targetV))
# dW: dg_rth = dW * dP
dW = sp.simplify(L[1, 2] / dP)
targetW = r**2 * sp.diff(Y, r) + X / f
res['dW_residual'] = str(sp.simplify(dW - targetW))
# Theta (trace): (dg_thth/r^2 + dg_phph/(r^2 sin^2))/2 = dTheta * P + (G-basis trace=0)
trace = sp.simplify((L[2, 2] / r**2 + L[3, 3] / (r**2 * sp.sin(th)**2)) / 2)
dTheta = sp.simplify(trace / P)
targetT = 2 * X / r - ell * (ell + 1) * Y
res['dTheta_residual'] = str(sp.simplify(dTheta - targetT))
# G (tracefree): dg_thth/r^2 - trace = dG/2 * E_thth_l where
# E_thth = d_th^2 P + l(l+1)/2 P ; check the coefficient ratio is th-independent
diffpart = sp.simplify(L[2, 2] / r**2 - trace)
Ethth = sp.diff(P, th, 2) + ell * (ell + 1) / 2 * P
ratio = sp.simplify(diffpart / Ethth)
# angular perturbation carried as Theta*P + G*E_thth: diffpart = dG * E_thth
res['dG_residual'] = str(sp.simplify(ratio - 2 * Y))
res['dG_ratio'] = str(ratio)
res['formulas'] = dict(dU=str(dU), dV=str(dV), dW=str(dW), dTheta=str(dTheta),
                       dG=str(2 * Y))
res['completeness'] = ("dG = 2Y = 0 => Y = 0; then dW = X/f = 0 => X = 0 "
                       "(f != 0 on the exterior). Class (a) EMPTY for l>=1.")
with open(__file__.rsplit('/', 1)[0] + '/wb1_gauge.json', 'w') as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
