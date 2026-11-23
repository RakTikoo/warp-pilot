"""W-C fresh Bach tensor, jet-space, RICCI FORM (the shared definition:
arXiv:2505.17171 eq.6, the form the phase record uses):
B_mn = Box R_mn - (1/3) Hess_mn R - (1/6) g_mn Box R
     + 2 R^{rs} R_{m r n s} - (1/2) g_mn R^{rs}R_rs
     - (2/3) R R_mn + (1/6) g_mn R^2.
Front stage (Gamma/Riem/Ric) is wc_bach4's, validated on Schwarzschild
(Ric=0, Weyl values) and on T-b (Ric via Bianchi). No computation is
skipped: every covariant derivative is formed in full; simplify is
applied only to a fully-formed expression.

Metric: ds^2 = -e^{2A}dt^2 + e^{2B}dr^2 + r^2 dOmega^2, A,B functions
of r only. All tensor quantities are built as expressions in the jet
symbols (r, th, A0..A4, B0..B4); the radial derivative is the jet
operator D = d/dr + sum_i (d/dA_i)(.) A_{i+1} + (d/dB_i)(.) B_{i+1};
theta derivatives are ordinary sympy derivatives (only the
phi-phi metric sector depends on th). Bach convention:
B_ab = nabla^c nabla^d C_acbd + (1/2) R^{cd} C_acbd, same index
conventions as wc_bach_derive.py. Output wc_bach_expr.json with the
mixed components B^t_t, B^r_r, B^th_th in jet symbols and the trace.
Anchors (checked in wc_static.py): Schwarzschild/MK Bach-flatness is
implied by the T-b closed-form match + member stored values; the
trace must come out identically zero.
"""
import sympy as sp, json, os, time
t0 = time.time()
r, th = sp.symbols('r th')
A = sp.symbols('A0:5'); B = sp.symbols('B0:5')
n = 4
def Djet(e):
    if e == 0: return sp.Integer(0)
    v = sp.diff(e, r)
    for i in range(4):
        v += sp.diff(e, A[i])*A[i+1] + sp.diff(e, B[i])*B[i+1]
    return v
def dcoord(e, k):
    if k == 1: return Djet(e)
    if k == 2: return sp.diff(e, th)
    return sp.Integer(0)
g = sp.diag(-sp.exp(2*A[0]), sp.exp(2*B[0]), r**2, r**2*sp.sin(th)**2)
gi = sp.diag(-sp.exp(-2*A[0]), sp.exp(-2*B[0]), 1/r**2, 1/(r**2*sp.sin(th)**2))
dg = [[[dcoord(g[i, j], k) for j in range(n)] for i in range(n)] for k in range(n)]
Gam = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[a, s]*(dg[b][s][c] + dg[c][s][b] - dg[s][b][c]) for s in range(n))/2
            Gam[a][b][c] = sp.simplify(v) if v != 0 else v
print('Gamma', time.time()-t0, flush=True)
dGam = [[[[dcoord(Gam[a][b][c], l) for c in range(n)] for b in range(n)] for a in range(n)] for l in range(n)]
Riem = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                v = dGam[c][a][b][d] - dGam[d][a][b][c]
                for s in range(n):
                    v += Gam[a][c][s]*Gam[s][b][d] - Gam[a][d][s]*Gam[s][b][c]
                Riem[a][b][c][d] = sp.simplify(v) if v != 0 else v
print('Riem', time.time()-t0, flush=True)
Ric = [[sum(Riem[a][b][a][d] for a in range(n)) for d in range(n)] for b in range(n)]
Rsc = sp.simplify(sum(gi[i, j]*Ric[i][j] for i in range(n) for j in range(n)))
Rl = [[[[sum(g[a, s]*Riem[s][b][c][d] for s in range(n)) for d in range(n)]
        for c in range(n)] for b in range(n)] for a in range(n)]
C = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                v = Rl[a][b][c][d]
                v -= sp.Rational(1, 2)*(g[a, c]*Ric[b][d] - g[a, d]*Ric[b][c]
                                        - g[b, c]*Ric[a][d] + g[b, d]*Ric[a][c])
                v += Rsc/6*(g[a, c]*g[b, d] - g[a, d]*g[b, c])
                C[a][b][c][d] = sp.simplify(v) if v != 0 else v
print('Weyl', time.time()-t0, flush=True)
# ---- Ricci-form Bach (arXiv:2505.17171 eq.6) ----
# D1[a][m][n] = nabla_a Ric_mn
D1 = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for m in range(n):
        for nn in range(n):
            v = dcoord(Ric[m][nn], a)
            for s in range(n):
                v -= Gam[s][a][m]*Ric[s][nn] + Gam[s][a][nn]*Ric[m][s]
            D1[a][m][nn] = sp.simplify(v) if v != 0 else v
print('D1', time.time()-t0, flush=True)
# D2[a][b][m][n] = nabla_a nabla_b Ric_mn
D2 = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for m in range(n):
            for nn in range(n):
                v = dcoord(D1[b][m][nn], a)
                for s in range(n):
                    v -= Gam[s][a][b]*D1[s][m][nn] + Gam[s][a][m]*D1[b][s][nn] + Gam[s][a][nn]*D1[b][m][s]
                D2[a][b][m][nn] = sp.simplify(v) if v != 0 else v
print('D2', time.time()-t0, flush=True)
BoxRic = [[sp.Integer(0)]*n for _ in range(n)]
for m in range(n):
    for nn in range(n):
        v = sum(gi[a, b]*D2[a][b][m][nn] for a in range(n) for b in range(n))
        BoxRic[m][nn] = sp.simplify(v) if v != 0 else v
dR = [dcoord(Rsc, i) for i in range(n)]
Hess = [[sp.Integer(0)]*n for _ in range(n)]
for m in range(n):
    for nn in range(n):
        v = dcoord(dR[nn], m) - sum(Gam[s][m][nn]*dR[s] for s in range(n))
        Hess[m][nn] = sp.simplify(v) if v != 0 else v
BoxR = sp.simplify(sum(gi[a, b]*Hess[a][b] for a in range(n) for b in range(n)))
RicUp = [[sum(gi[i, a]*gi[j, b]*Ric[a][b] for a in range(n) for b in range(n)) for j in range(n)] for i in range(n)]
RicSq = sp.simplify(sum(RicUp[i][j]*Ric[i][j] for i in range(n) for j in range(n)))
print('Box/Hess', time.time()-t0, flush=True)
Bach = [[sp.Integer(0)]*n for _ in range(n)]
for m in range(n):
    nn = m
    quad = sum(RicUp[rr][s]*sum(g[m, e]*Riem[e][rr][nn][s] for e in range(n))
               for rr in range(n) for s in range(n))
    v = (BoxRic[m][nn] - sp.Rational(1, 3)*Hess[m][nn] - sp.Rational(1, 6)*g[m, nn]*BoxR
         + 2*quad - sp.Rational(1, 2)*g[m, nn]*RicSq - sp.Rational(2, 3)*Rsc*Ric[m][nn]
         + sp.Rational(1, 6)*g[m, nn]*Rsc**2)
    Bach[m][nn] = v
print('Bach', time.time()-t0, flush=True)
def fin(e):
    return str(e.subs(th, sp.pi/2))
mixed = [sum(gi[i, s]*Bach[s][i] for s in range(n)) for i in range(n)]
out = {'trace': fin(sum(mixed)), 'Bt': fin(mixed[0]), 'Br': fin(mixed[1]), 'Bth': fin(mixed[2]),
       'Bph_mixed': fin(mixed[3])}
json.dump(out, open(os.path.expanduser('~/workspace/warp-pilot/gate9/wc_bach_expr.json'), 'w'))
print('saved, time', time.time()-t0, flush=True)
