"""wb_symbolic.py — W-B Gate-7 G7-2: SYMBOLIC radial-reduction derivation.

Fresh derivation (W-B's own; NOT W-A's, NOT any phase/gate script) of the
Einstein tensor of the registered metric form, in coordinates (t, r, th, ph):

    g_tt = -exp(2 a(r))
    g_t. = -beta * S(r) dx        (shift along x, covector form)
         => g_tr = -beta S sin(th) cos(ph)
            g_tth = -beta S r cos(th) cos(ph)
            g_tph = +beta S r sin(th) sin(ph)
    gamma = diag(exp(2 b(r)), r^2, r^2 sin^2(th))
          (i.e. delta_ij + (exp(2b)-1) n_i n_j in Cartesian form)

a, b, S unspecified sympy Functions of r; beta a symbol. Inverse supplied
analytically via the ADM structure and verified (g*ginv = I numerically).
Einstein tensor by a generic index-loop routine written for this gate.
Expressions are xreplace-d onto 13 numeric variables
(r, th, ph, a, a1, a2, b, b1, b2, S, S1, S2, beta) and lambdified (CSE),
so the numeric auditor feeds ANALYTIC derivatives only — no FD stencil.

Anchor (i) is proven here symbolically: with a=b=S=0 (constants) every
entry of G simplifies to identically zero (run 2026-11-22, log line
"symbolic Minkowski nonzero entries: 0").

Python: system python3 (sympy 1.12 / numpy 2.2.6). float64 downstream.
"""
import os, pickle, time
import sympy as sp

t0 = time.time()
G7 = '/home/hatch/workspace/warp-pilot/gate7'
CACHE = G7 + '/wb_G_expr.pkl'
r, th, ph = sp.symbols('r th ph', positive=True)
t = sp.symbols('t')
beta = sp.symbols('beta')
A = sp.Function('A')(r); B = sp.Function('B')(r); Sf = sp.Function('S')(r)

def build_metric():
    g = sp.zeros(4, 4)
    g[0, 0] = -sp.exp(2 * A)
    g[0, 1] = g[1, 0] = -beta * Sf * sp.sin(th) * sp.cos(ph)
    g[0, 2] = g[2, 0] = -beta * Sf * r * sp.cos(th) * sp.cos(ph)
    g[0, 3] = g[3, 0] = beta * Sf * r * sp.sin(th) * sp.sin(ph)
    g[1, 1] = sp.exp(2 * B)
    g[2, 2] = r ** 2
    g[3, 3] = r ** 2 * sp.sin(th) ** 2
    return g

def derive():
    x = [t, r, th, ph]
    g = build_metric()
    ginv_sp = sp.diag(sp.exp(-2 * B), 1 / r ** 2, 1 / (r ** 2 * sp.sin(th) ** 2))
    w = sp.Matrix([g[0, 1], g[0, 2], g[0, 3]])
    W = ginv_sp * w
    alpha2 = sp.exp(2 * A) + (w.T * W)[0]
    ginv = sp.zeros(4, 4)
    ginv[0, 0] = -1 / alpha2
    for i in range(3):
        ginv[0, i + 1] = ginv[i + 1, 0] = W[i] / alpha2
        for j in range(3):
            ginv[i + 1, j + 1] = ginv_sp[i, j] - W[i] * W[j] / alpha2
    vals = {r: 17.3, th: 0.9, ph: 2.1, beta: 0.1, A: 0.05, B: 0.11, Sf: 0.4}
    prod = (g * ginv).subs(vals)
    err = max(abs(complex(prod[i, j] - (1 if i == j else 0))) for i in range(4) for j in range(4))
    assert err < 1e-12, err
    print('inverse supplied + verified (g*ginv=I, numeric, err<1e-12)', time.time() - t0, flush=True)
    n = 4
    dg = [[[sp.diff(g[i, j], x[k]) for k in range(n)] for j in range(n)] for i in range(n)]
    Gamma = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                Gamma[lam][mu][nu] = sum(
                    ginv[lam, s] * (dg[s][nu][mu] + dg[s][mu][nu] - dg[mu][nu][s])
                    for s in range(n)) / 2
    print('Gamma done', time.time() - t0, flush=True)
    Ric = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            e = 0
            for lam in range(n):
                e += sp.diff(Gamma[lam][nu][mu], x[lam]) - sp.diff(Gamma[lam][lam][mu], x[nu])
                for s in range(n):
                    e += Gamma[lam][lam][s] * Gamma[s][nu][mu] - Gamma[lam][nu][s] * Gamma[s][lam][mu]
            Ric[mu, nu] = e
    print('Ricci done', time.time() - t0, flush=True)
    Rsc = sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n))
    G = Ric - sp.Rational(1, 2) * Rsc * g
    print('G assembled', time.time() - t0, flush=True)
    return G, g

G, g = derive()

av, a1, a2, bv, b1, b2, sv, s1, s2 = sp.symbols('av a1 a2 bv b1 b2 sv s1 s2')
repl = {A: av, B: bv, Sf: sv,
        sp.diff(A, r): a1, sp.diff(A, r, 2): a2,
        sp.diff(B, r): b1, sp.diff(B, r, 2): b2,
        sp.diff(Sf, r): s1, sp.diff(Sf, r, 2): s2}
args = (r, th, ph, av, a1, a2, bv, b1, b2, sv, s1, s2, beta)
Gsub = G.xreplace(repl)
gsub = g.xreplace(repl)
print('xreplace done; G entry atom counts:', [len(Gsub[i, j].atoms()) for i in range(4) for j in range(4)], flush=True)
Gfun = sp.lambdify(args, Gsub, 'numpy', cse=True)
gfun = sp.lambdify(args, gsub, 'numpy', cse=True)
print('lambdified in', time.time() - t0, 's', flush=True)

if __name__ == '__main__':
    # Anchor (i), symbolic: Minkowski identically zero.
    subs_mink = {A: sp.Integer(0), B: sp.Integer(0), Sf: sp.Integer(0)}
    Gm = G.xreplace(subs_mink)
    nz = 0
    for i in range(4):
        for j in range(4):
            if sp.simplify(Gm[i, j]) != 0:
                nz += 1
                print('MINK NONZERO', i, j, flush=True)
    print('symbolic Minkowski nonzero entries:', nz, flush=True)
    print('ALL DONE', time.time() - t0, flush=True)
