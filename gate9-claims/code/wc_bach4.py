"""W-C fresh Bach tensor, jet-space derivation (third route: front
tensor stage validated on Schwarzschild Ricci/Weyl; Bach contraction
in the standard slot placement, see below).

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
# ---- Bach parts, BOTH divergence placements ----
# Placement 1: DD1_mn = nabla^a nabla^b C_{a m b n}, RC1_mn = R^{ab} C_{a m b n}
# Placement 2: DD2_mn = nabla^c nabla^d C_{m c n d}, RC2_mn = R^{cd} C_{m c n d}
Cmix = [[[[sum(gi[a, ap]*C[ap][m][b][nn] for ap in range(n)) for nn in range(n)] for b in range(n)] for m in range(n)] for a in range(n)]
DCmix = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for m in range(n):
            for b in range(n):
                for nn in range(n):
                    v = dcoord(Cmix[a][m][b][nn], e)
                    for s in range(n):
                        v += Gam[a][e][s]*Cmix[s][m][b][nn]
                        v -= Gam[s][e][m]*Cmix[a][s][b][nn] + Gam[s][e][b]*Cmix[a][m][s][nn] \
                             + Gam[s][e][nn]*Cmix[a][m][b][s]
                    DCmix[e][a][m][b][nn] = sp.simplify(v) if v != 0 else v
print('DCmix', time.time()-t0, flush=True)
K = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for m in range(n):
        for nn in range(n):
            v = sum(gi[b, bp]*DCmix[bp][a][m][b][nn] for b in range(n) for bp in range(n))
            K[a][m][nn] = sp.simplify(v) if v != 0 else v
DK = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for m in range(n):
            for nn in range(n):
                v = dcoord(K[a][m][nn], e)
                for s in range(n):
                    v += Gam[a][e][s]*K[s][m][nn]
                    v -= Gam[s][e][m]*K[a][s][nn] + Gam[s][e][nn]*K[a][m][s]
                DK[e][a][m][nn] = sp.simplify(v) if v != 0 else v
print('DK', time.time()-t0, flush=True)
DD1 = [[sp.Integer(0)]*n for _ in range(n)]; RC1 = [[sp.Integer(0)]*n for _ in range(n)]
for m in range(n):
    for nn in range(n):
        DD1[m][nn] = sum(gi[a, ap]*DK[ap][a][m][nn] for a in range(n) for ap in range(n))
        RC1[m][nn] = sum(gi[a, ap]*gi[b, bp]*Ric[ap][bp]*C[a][m][b][nn]
                         for a in range(n) for b in range(n) for ap in range(n) for bp in range(n))
print('DD1/RC1 assembled', time.time()-t0, flush=True)
# Placement 2 via all-lower DC derived from DCmix:
# nabla_e C_{a b c d} = (d_e g_{a al}) C^al_{b c d} + g_{a al} nabla_e C^al_{b c d}
DClow = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    v = dg[e][a][a]*Cmix[a][b][c][d] + g[a, a]*DCmix[e][a][b][c][d]
                    DClow[e][a][b][c][d] = sp.simplify(v) if v != 0 else v
print('DClow', time.time()-t0, flush=True)
H2 = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[d, dp]*DClow[dp][a][c][b][d] for d in range(n) for dp in range(n))
            H2[a][b][c] = sp.simplify(v) if v != 0 else v
DH2 = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                v = dcoord(H2[a][b][c], e)
                for s in range(n):
                    v -= Gam[s][e][a]*H2[s][b][c] + Gam[s][e][b]*H2[a][s][c] + Gam[s][e][c]*H2[a][b][s]
                DH2[e][a][b][c] = sp.simplify(v) if v != 0 else v
print('DH2', time.time()-t0, flush=True)
DD2 = [[sp.Integer(0)]*n for _ in range(n)]; RC2 = [[sp.Integer(0)]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        DD2[a][b] = sum(gi[c, e]*DH2[e][a][b][c] for c in range(n) for e in range(n))
        RC2[a][b] = sum(gi[c, cp]*gi[d, dp]*Ric[cp][dp]*C[a][c][b][d]
                        for c in range(n) for d in range(n) for cp in range(n) for dp in range(n))
print('DD2/RC2 assembled', time.time()-t0, flush=True)
def mixfin(T, i):
    return str(sum(gi[i, s]*T[s][i] for s in range(n)).subs(th, sp.pi/2))
out = {}
for nm, T in (('DD1', DD1), ('RC1', RC1), ('DD2', DD2), ('RC2', RC2)):
    out[nm] = {'t': mixfin(T, 0), 'r': mixfin(T, 1), 'th': mixfin(T, 2), 'ph': mixfin(T, 3)}
json.dump(out, open(os.path.expanduser('~/workspace/warp-pilot/gate9/wc_bach_parts.json'), 'w'))
print('saved parts, time', time.time()-t0, flush=True)
