"""W-C fresh symbolic Bach tensor for the static spherical ansatz
ds^2 = -e^{2A(r)}dt^2 + e^{2B(r)}dr^2 + r^2 dOmega^2.
Bach (one common convention): B_ab = nabla^c nabla^d C_acbd
  + (1/2) R^{cd} C_acbd.
Derived from the metric with sympy; A, B are generic functions of r.
Derivative symbols: A0..A4, B0..B4 (value + 1st..4th r-derivatives).
Output: gate9/wc_bach_expr.json {Bt, Br, Bth} for the MIXED components
B^t_t, B^r_r, B^theta_theta as functions of (r, A0..A4, B0..B4),
plus the symbolic trace. Overall normalisation is fixed afterwards
against the T-b closed forms (documented in wc_static.py).
"""
import sympy as sp, json, os, time
t0 = time.time()
r, th = sp.symbols('r th', positive=True)
A = sp.Function('A')(r); Bf = sp.Function('B')(r)
coords = [sp.Symbol('t'), r, th, sp.Symbol('ph')]
g = sp.diag(-sp.exp(2*A), sp.exp(2*Bf), r**2, r**2*sp.sin(th)**2)
gi = g.inv()
n = 4
# Christoffel Gamma^a_bc
Gam = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
dg = [[[sp.diff(g[i, j], coords[k]) for j in range(n)] for i in range(n)] for k in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[a, s]*(dg[b][s][c] + dg[c][s][b] - dg[s][b][c]) for s in range(n)) / 2
            Gam[a][b][c] = v
print('Gamma', time.time()-t0, flush=True)
# Riemann R^a_bcd
Riem = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                v = sp.diff(Gam[a][b][d], coords[c]) - sp.diff(Gam[a][b][c], coords[d])
                for s in range(n):
                    v += Gam[a][c][s]*Gam[s][b][d] - Gam[a][d][s]*Gam[s][b][c]
                Riem[a][b][c][d] = v
print('Riem', time.time()-t0, flush=True)
Ric = [[sum(Riem[a][b][a][d] for a in range(n)) for d in range(n)] for b in range(n)]
Rsc = sum(gi[i, j]*Ric[i][j] for i in range(n) for j in range(n))
# Weyl C_abcd (all lower)
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
                C[a][b][c][d] = v
print('Weyl', time.time()-t0, flush=True)
# covariant derivative of Weyl: DC[e][a][b][c][d] = nabla_e C_abcd
def cov_deriv(T, rank):
    # T: nested lists, all-lower rank-`rank` tensor depending on coords
    DT = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    return DT
# Only need nabla^c nabla^d C_acbd for diagonal a=b in {t,r,th}: compute
# first derivative DC1[c][a][b][d] := nabla^c C_{a ? b d} with the middle
# index raised later; do it directly with all-lower C and raise after.
import itertools
def get(T, idx):
    for i in idx: T = T[i]
    return T
# DC[e][a][b][c][d]
DC = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if C[a][b][c][d] == 0: continue
                    v = sp.diff(C[a][b][c][d], coords[e])
                    for s in range(n):
                        v -= Gam[s][e][a]*C[s][b][c][d] + Gam[s][e][b]*C[a][s][c][d] \
                             + Gam[s][e][c]*C[a][b][s][d] + Gam[s][e][d]*C[a][b][c][s]
                    DC[e][a][b][c][d] = v
print('DC', time.time()-t0, flush=True)
# D2[a][b] = nabla^c nabla^d C_{a c b d}: first raise/contract step by step.
# E[c][a][b][d] = nabla^c C_{a c b d}  (c summed with gi)
E = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]  # E[a][b] after full contraction below
# Compute F[d][a][b][c] = nabla_d C_{a c b ? } -> instead compute
# G[a][b][c] = nabla^d C_{a c b d} summed over d: need nabla acting on C with
# last index free then contracted. Build DCd[d][a][c][b][e] = nabla_d C_{a c b e}
DCd = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for dd in range(n):
    for a in range(n):
        for c in range(n):
            for b in range(n):
                for e in range(n):
                    DCd[dd][a][c][b][e] = DC[dd][a][c][b][e]
# G[a][b] = sum_{c,d} gi[c,?] ... : nabla^c (nabla^d C_{a c b d})
# Step 1: H[a][b][c] = nabla^d C_{a c b d} = sum_d gi^{d d'} nabla_{d'} C_{a c b d}
H = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[d, dp]*DCd[dp][a][c][b][d] for d in range(n) for dp in range(n))
            H[a][b][c] = v
print('H', time.time()-t0, flush=True)
# Step 2: nabla_e H[a][b][c] (H is (2 lower, 1 upper) after raising c? No:
# H[a][b][c] has c as the contracted-partner index position of C's 2nd slot,
# already summed partner d raised; treat H as tensor with indices (a,b,c)
# where c is UPPER (it was raised by gi in step 1's contraction partner).
# Actually nabla^d C_{a c b d}: c remains lower. The outer nabla^c contracts c.
# Covariant derivative of the (0,3) tensor H_{a b c}:
DH = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]  # DH[e][a][b][c]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if H[a][b][c] == 0: continue
                v = sp.diff(H[a][b][c], coords[e])
                for s in range(n):
                    v -= Gam[s][e][a]*H[s][b][c] + Gam[s][e][b]*H[a][s][c] + Gam[s][e][c]*H[a][b][s]
                DH[e][a][b][c] = v
print('DH', time.time()-t0, flush=True)
# redo Ricci term properly (separate, clean):
Bach2 = [[sp.Integer(0)]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        v = sum(gi[c, e]*DH[e][a][b][c] for c in range(n) for e in range(n))
        rt = sp.Integer(0)
        for c in range(n):
            for d in range(n):
                if C[a][c][b][d] == 0: continue
                rt += sum(gi[c, cp]*gi[d, dp]*Ric[cp][dp] for cp in range(n) for dp in range(n))*C[a][c][b][d]
        Bach2[a][b] = sp.simplify(v + sp.Rational(1, 2)*rt)
print('Bach', time.time()-t0, flush=True)
# mixed components and trace
mixed = [sp.simplify(sum(gi[i, s]*Bach2[s][i] for s in range(n))) for i in range(n)]
trace = sp.simplify(sum(mixed))
# substitute derivative symbols
As = sp.symbols('A0:5'); Bs = sp.symbols('B0:5')
subs = {A: As[0], Bf: Bs[0]}
for k in range(1, 5):
    subs[sp.Derivative(A, (r, k))] = As[k]
    subs[sp.Derivative(Bf, (r, k))] = Bs[k]
def conv(e):
    e = e.subs(subs)
    e = sp.simplify(e.subs({sp.sin(th): 1, sp.cos(th): 0}))
    return e
out = {'trace': str(conv(trace)),
       'Bt': str(conv(mixed[0])), 'Br': str(conv(mixed[1])), 'Bth': str(conv(mixed[2]))}
json.dump(out, open(os.path.expanduser('~/workspace/warp-pilot/gate9/wc_bach_expr.json'), 'w'))
print('trace =', out['trace'], flush=True)
print('saved, time', time.time()-t0, flush=True)
