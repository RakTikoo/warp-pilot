"""Debug: exact (SymPy) Alcubierre That at sample points vs FD That,
and Hawking-Ellis type of the exact tensor."""
import sympy as sp
import numpy as np
import verify_metric as vm
import metrics as mx

t, X, y, z = sp.symbols('t X y z', real=True)
r = sp.symbols('r', positive=True)
v, R, sg = sp.symbols('v R sigma', positive=True)
coords = [t, X, y, z]; spatial = [X, y, z]
F = sp.Function('f'); f = F(r)

def D(expr, a):
    if a == 0: return sp.Integer(0)
    s = spatial[a - 1]
    return sp.diff(expr, s) + (s / r) * sp.diff(expr, r)

beta = v * (1 - f)
g = sp.Matrix([[-1 + beta**2, beta, 0, 0], [beta, 1, 0, 0],
               [0, 0, 1, 0], [0, 0, 0, 1]])
ginv = g.inv()
dg = [sp.Matrix(4, 4, lambda i, j, a=a: D(g[i, j], a)) for a in range(4)]
Gamma = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            Gamma[a][b][c] = sp.simplify(sum(
                ginv[a, d] * (dg[b][d, c] + dg[c][d, b] - dg[d][b, c]) for d in range(4)) / 2)
Ricci = sp.zeros(4, 4)
for b in range(4):
    for d in range(4):
        expr = 0
        for a in range(4):
            expr += D(Gamma[a][b][d], a) - D(Gamma[a][b][a], d)
            for e in range(4):
                expr += Gamma[a][a][e] * Gamma[e][b][d] - Gamma[a][d][e] * Gamma[e][b][a]
        Ricci[b, d] = expr
Rsc = sum(ginv[i, j] * Ricci[i, j] for i in range(4) for j in range(4))
G = Ricci - sp.Rational(1, 2) * Rsc * g
T = G / (8 * sp.pi)

fnum = (sp.tanh(sg * (r + R)) - sp.tanh(sg * (r - R))) / (2 * sp.tanh(sg * R))
subs_f = {F(r): fnum, sp.Derivative(F(r), r): sp.diff(fnum, r),
          sp.Derivative(F(r), r, r): sp.diff(fnum, r, 2)}
Tnum = T.subs(subs_f)

pts = [(0.0, 1.5, 0.0), (1.0, 1.0, 0.5), (-1.5, 0.3, 0.2), (0.0, 0.0, 1.5)]
for (px, py, pz) in pts:
    pt = {X: px, y: py, z: pz, r: (px**2 + py**2 + pz**2) ** 0.5, v: 0.7, R: 1.5, sg: 2.0}
    Tex = np.array(Tnum.subs(pt).evalf(), dtype=float)
    # Eulerian tetrad for Alcubierre comoving: alpha=1, gamma=delta -> That via vm
    fv = float(fnum.subs(pt).evalf())
    beta_v = 0.7 * (1 - fv)
    gmet = np.zeros((1, 4, 4)); gmet[0, 0, 0] = -1 + beta_v**2
    gmet[0, 0, 1] = gmet[0, 1, 0] = beta_v
    gmet[0, 1, 1] = gmet[0, 2, 2] = gmet[0, 3, 3] = 1.0
    That = vm.eulerian_that(gmet, Tex[None])
    m = vm.hawking_ellis_margins(That)
    Mx = That[0].copy(); Mx[0, :] *= -1
    ev = np.linalg.eigvals(Mx)
    print(f'pt {(px,py,pz)}: That00={That[0,0,0]:.5f} typeI={m["typeI"][0]} '
          f'rho_eig={m["rho_eig"][0]:.5f} p={np.round(m["p"][0],5)} NEC={m["nec"][0]:.5f}')
    print('   eigvals mixed:', np.round(ev, 5))
