"""W-C fresh Bach tensor, jet-space derivation (second, lean route after
the full-tensor route's final simplify proved intractable in-item;
that route is retained as wc_bach_derive.py, unfinished, no number
used from it).

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
# DC[e][a][b][c][d] = nabla_e C_abcd
DC = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if C[a][b][c][d] == 0: continue
                    v = dcoord(C[a][b][c][d], e)
                    for s in range(n):
                        v -= Gam[s][e][a]*C[s][b][c][d] + Gam[s][e][b]*C[a][s][c][d] \
                             + Gam[s][e][c]*C[a][b][s][d] + Gam[s][e][d]*C[a][b][c][s]
                    DC[e][a][b][c][d] = sp.simplify(v) if v != 0 else v
print('DC', time.time()-t0, flush=True)
# H[a][b][c] = nabla^d C_{a c b d}
H = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[d, dp]*DC[dp][a][c][b][d] for d in range(n) for dp in range(n))
            H[a][b][c] = sp.simplify(v) if v != 0 else v
print('H', time.time()-t0, flush=True)
DH = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]  # DH[e][a][b][c]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if H[a][b][c] == 0: continue
                v = dcoord(H[a][b][c], e)
                for s in range(n):
                    v -= Gam[s][e][a]*H[s][b][c] + Gam[s][e][b]*H[a][s][c] + Gam[s][e][c]*H[a][b][s]
                DH[e][a][b][c] = sp.simplify(v) if v != 0 else v
print('DH', time.time()-t0, flush=True)
Bach = [[sp.Integer(0)]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        v = sum(gi[c, e]*DH[e][a][b][c] for c in range(n) for e in range(n))
        rt = sp.Integer(0)
        for c in range(n):
            for d in range(n):
                if C[a][c][b][d] == 0: continue
                rt += sum(gi[c, cp]*gi[d, dp]*Ric[cp][dp] for cp in range(n) for dp in range(n))*C[a][c][b][d]
        Bach[a][b] = sp.simplify(v + sp.Rational(1, 2)*rt)
print('Bach', time.time()-t0, flush=True)
mixed = [sp.simplify(sum(gi[i, s]*Bach[s][i] for s in range(n))) for i in range(n)]
trace = sp.simplify(sum(mixed))
def fin(e):
    return str(sp.simplify(e.subs({sp.sin(th): 1, sp.cos(th): 0})))
out = {'trace': fin(trace), 'Bt': fin(mixed[0]), 'Br': fin(mixed[1]), 'Bth': fin(mixed[2]),
       'Bph_mixed': fin(mixed[3])}
json.dump(out, open(os.path.expanduser('~/workspace/warp-pilot/gate9/wc_bach_expr.json'), 'w'))
print('trace =', out['trace'], flush=True)
print('saved, time', time.time()-t0, flush=True)
