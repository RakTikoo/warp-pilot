"""
symbolic_alcubierre.py — Independent SYMBOLIC path (SymPy, exact arithmetic).

Alcubierre metric in comoving coordinates (stationary):
    ds^2 = -dt^2 + (dX + v (1 - f(r)) dt)^2 + dy^2 + dz^2,
    r = sqrt(X^2 + y^2 + z^2)
(ADM: alpha=1, gamma=delta, shift beta^X = v (1-f).)

Checks the Eulerian energy density against Alcubierre 1994 /
Pfenning & Ford Eq. (8):
    rho_E = -(v^2 / (32 pi)) * ((y^2 + z^2) / r^2) * (f'(r))^2    [G = c = 1]

r is carried as an independent symbol; spatial derivatives use the total
derivative operator  D_i = d/ds_i|_r + (s_i/r) d/dr  (chain rule).
"""
import sympy as sp

t, X, y, z = sp.symbols('t X y z', real=True)
r = sp.symbols('r', positive=True)
v, R, sg = sp.symbols('v R sigma', positive=True)
coords = [t, X, y, z]
spatial = [X, y, z]
F = sp.Function('f')
f = F(r)


def D(expr, a):
    """Total derivative wrt coords[a]."""
    if a == 0:
        return sp.Integer(0)
    s = spatial[a - 1]
    return sp.diff(expr, s) + (s / r) * sp.diff(expr, r)


beta = v * (1 - f)                      # shift beta^X
g = sp.Matrix([
    [-1 + beta**2, beta, 0, 0],
    [beta,         1,    0, 0],
    [0,            0,    1, 0],
    [0,            0,    0, 1],
])
ginv = g.inv()

dg = []
for a in range(4):
    dg.append(sp.Matrix(4, 4, lambda i, j, a=a: D(g[i, j], a)))

Gamma = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            expr = sum(ginv[a, d] * (dg[b][d, c] + dg[c][d, b] - dg[d][b, c])
                       for d in range(4)) / 2
            Gamma[a][b][c] = sp.simplify(expr)

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

n = sp.Matrix([1, -beta, 0, 0])         # Eulerian observer, alpha = 1
rho_E = sp.simplify(sum(T[i, j] * n[i] * n[j] for i in range(4) for j in range(4)))

fp = sp.diff(f, r)
target = -(v**2 / (32 * sp.pi)) * ((y**2 + z**2) / r**2) * fp**2
diff = sp.simplify(rho_E - target)
print('SYMBOLIC rho_E =', rho_E)
print('SYMBOLIC diff (rho_E - analytic target) simplified =', diff)

# ---- Check B: numeric shape function at random points ----------------------
import random
random.seed(20261120)
fnum = (sp.tanh(sg * (r + R)) - sp.tanh(sg * (r - R))) / (2 * sp.tanh(sg * R))
rho_num_expr = rho_E.subs({sp.Derivative(F(r), r): sp.diff(fnum, r), F(r): fnum})
target_num = -(v**2 / (32 * sp.pi)) * ((y**2 + z**2) / r**2) * sp.diff(fnum, r)**2
max_err = 0.0
for _ in range(12):
    px, py, pz = (random.uniform(-3, 3) for _ in range(3))
    if abs(px) + abs(py) + abs(pz) < 0.3:
        continue
    pt = {X: px, y: py, z: pz, r: (px**2 + py**2 + pz**2) ** 0.5,
          v: 0.7, R: 1.5, sg: 2.0}
    a_ = float(rho_num_expr.subs(pt).evalf())
    b_ = float(target_num.subs(pt).evalf())
    max_err = max(max_err, abs(a_ - b_))
print('NUMERIC max |rho_E - target| over random points =', max_err)
