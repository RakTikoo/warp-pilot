"""P72-1 shared machinery: Einstein tensor + Dirac T for the BSKR/KZ
singlet ansatz, derived with sympy from the published forms.
Conventions: EPJC 82,533 (2022) eqs (2.1)-(2.6), (3.1), (3.7);
gamma matrices per KZ arXiv:2106.05034 eq (26); bar per eq (29).
Metric: ds^2 = -F0(l)^2 dt^2 + F1(l)^2 dl^2 + F2(l)^2 dOmega^2,
F2 = sqrt(l^2+r0^2). Einstein eq: G_mn = 2 T_mn (paper norm).
"""
import sympy as sp

# ---------- gamma matrices (KZ eq 26) ----------
I2 = sp.eye(2); Z2 = sp.zeros(2)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d):
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))
g0h = sp.I * blk(Z2, I2, I2, Z2)
g1h = sp.I * blk(Z2, s3, -s3, Z2)
g2h = sp.I * blk(Z2, s1, -s1, Z2)
g3h = sp.I * blk(Z2, s2, -s2, Z2)
GH = [g0h, g1h, g2h, g3h]
ETA = sp.diag(-1, 1, 1, 1)

def check_gammas():
    out = {}
    for a in range(4):
        for b in range(4):
            lhs = GH[a] * GH[b] + GH[b] * GH[a]
            rhs = 2 * ETA[a, b] * sp.eye(4)
            out[(a, b)] = sp.simplify(lhs - rhs) == sp.zeros(4)
    return out

# ---------- symbols ----------
l, th, ph, t = sp.symbols('l theta phi t', real=True)
r0s = sp.symbols('r0', positive=True)
F0, F1, P, Q, Pd, Qd, F0d, F1d, F0dd = sp.symbols('F0 F1 P Q Pd Qd F0d F1d F0dd', real=True)
w, mu = sp.symbols('w mu', real=True)
kap = sp.symbols('kappa', real=True)

F2 = sp.sqrt(l**2 + r0s**2)
F2d = l / F2
F2dd = 1 / F2 - l**2 / F2**3

# ---------- Einstein tensor (orthonormal, diagonal metric) ----------
# ds^2 = -e^{2a} dt^2 + e^{2b} dl^2 + R^2 dOm^2, a=ln F0, b=ln F1, R=F2
# Standard formulas (e.g. Wald / MT): with ' = d/dl
# G^t_t = -[ 2 R''/(R e^{2b}) - 2 R' b'/(R e^{2b}) + (R'^2)/(R^2 e^{2b}) - 1/R^2 ] *? --
# derived here directly with sympy from the metric instead (see derive_G).
def derive_G():
    coords = [t, l, th, ph]
    F0f = sp.Function('F0f')(l); F1f = sp.Function('F1f')(l)
    R = sp.sqrt(l**2 + r0s**2)
    g = sp.diag(-F0f**2, F1f**2, R**2, R**2 * sp.sin(th)**2)
    gi = g.inv()
    n = 4
    Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    dg = [sp.diff(g, c) for c in coords]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                expr = sum(gi[a, d] * (dg[b][d, c] + dg[c][d, b] - dg[d][b, c]) for d in range(n)) / 2
                Gam[a][b][c] = sp.simplify(expr)
    Ric = [[sp.Integer(0)] * n for _ in range(n)]
    for b in range(n):
        for d in range(n):
            expr = 0
            for a in range(n):
                expr += sp.diff(Gam[a][b][d], coords[a]) - sp.diff(Gam[a][b][a], coords[d])
                for e in range(n):
                    expr += Gam[a][a][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][a]
            Ric[b][d] = expr
    Rs = sp.simplify(sum(gi[b, d] * Ric[b][d] for b in range(n) for d in range(n)))
    Gmix = {}
    for b in range(n):
        Gmix[b] = sp.simplify(sum(gi[b, d] * Ric[d][b] for d in range(n)) - Rs / 2)
    return Gmix  # G^t_t, G^l_l, G^th_th, G^ph_ph as exprs in F0f,F1f and derivs

if __name__ == '__main__':
    print('gamma check:', all(check_gammas().values()))
