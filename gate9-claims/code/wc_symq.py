"""W-C fresh symbolic derivation of the Weyl^2 density for the diagonal
log-metric ds^2 = -e^{2a}dt^2 + e^{2b}dr^2 + e^{2c} r^2 dOmega^2,
evaluated at theta=pi/2 (with d_th^2(2 ln sin th) = -2 included for the
phi-phi component, as spherical symmetry requires).
Variables: r and, for x in {a,b,c}: x, x_t, x_r, x_tt, x_tr, x_rr.
Output: gate9/wc_symq_expr.json with Q = sqrt(-g) C^2 (sin-stripped)
and C2 as sympy strings. Written from the tensor definitions only.
"""
import sympy as sp, json, time, os
t0 = time.time()
names = ['r']
S = {'r': sp.Symbol('r')}
for x in 'abc':
    for suf in ['', '_t', '_r', '_tt', '_tr', '_rr']:
        S[x + suf] = sp.Symbol(x + suf); names.append(x + suf)
r = S['r']
def comp(x):
    return dict(v=S[x], t=S[x+'_t'], rr_=S[x+'_r'], tt=S[x+'_tt'], tr=S[x+'_tr'], rr=S[x+'_rr'])
B = {x: comp(x) for x in 'abc'}
comps = [B['a'], B['b'], B['c'], B['c']]
g = [-sp.exp(2*B['a']['v']), sp.exp(2*B['b']['v']),
     sp.exp(2*B['c']['v'])*r**2, sp.exp(2*B['c']['v'])*r**2]
gi = [1/v for v in g]
# lg[i][k] = d_k log|g_i| ; dlg[i][k][l] = d_l lg[i][k]; coords (t,r,th,ph)
lg = [[sp.Integer(0)]*4 for _ in range(4)]
dlg = [[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)]
for i in range(4):
    bs = comps[i]
    lg[i][0] = 2*bs['t']; lg[i][1] = 2*bs['rr_']
    if i >= 2: lg[i][1] += 2/r
    m = [[sp.Integer(0)]*4 for _ in range(4)]
    m[0][0] = 2*bs['tt']; m[0][1] = 2*bs['tr']; m[1][0] = 2*bs['tr']; m[1][1] = 2*bs['rr']
    if i >= 2: m[1][1] += -2/r**2
    if i == 3: m[2][2] += -2
    dlg[i] = m
dg = [[g[i]*lg[i][k] for i in range(4)] for k in range(4)]            # dg[k][i]
d2g = [[[g[i]*(dlg[i][k][l] + lg[i][k]*lg[i][l]) for i in range(4)]
        for k in range(4)] for l in range(4)]                          # d2g[l][k][i]
Gam = [[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)]       # Gam[a][b][c]
dGam = [[[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for a_ in range(4):
    for b_ in range(4):
        for c_ in range(4):
            val = sp.Integer(0); dval = [sp.Integer(0)]*4
            if a_ == c_:
                val += dg[b_][a_]
                for l in range(4): dval[l] += d2g[l][b_][a_]
            if a_ == b_:
                val += dg[c_][a_]
                for l in range(4): dval[l] += d2g[l][c_][a_]
            if b_ == c_:
                val -= dg[a_][b_]
                for l in range(4): dval[l] -= d2g[l][a_][b_]
            Gam[a_][b_][c_] = sp.Rational(1, 2)*gi[a_]*val
            for l in range(4):
                dGam[l][a_][b_][c_] = sp.Rational(1, 2)*gi[a_]*(dval[l] - lg[a_][l]*val)
print('Gamma done', time.time()-t0, flush=True)
Riem = [[[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for a_ in range(4):
    for b_ in range(4):
        for c_ in range(4):
            for d_ in range(4):
                v = dGam[c_][a_][b_][d_] - dGam[d_][a_][b_][c_]
                for s in range(4):
                    v += Gam[a_][c_][s]*Gam[s][b_][d_] - Gam[a_][d_][s]*Gam[s][b_][c_]
                Riem[a_][b_][c_][d_] = v
print('Riem done', time.time()-t0, flush=True)
Ric = [[sum(Riem[a_][b_][a_][d_] for a_ in range(4)) for d_ in range(4)] for b_ in range(4)]
Rsc = sum(gi[i]*Ric[i][i] for i in range(4))
K = sp.Integer(0)
for a_ in range(4):
    for b_ in range(4):
        for c_ in range(4):
            for d_ in range(4):
                if Riem[a_][b_][c_][d_] != 0:
                    K += g[a_]*gi[b_]*gi[c_]*gi[d_]*Riem[a_][b_][c_][d_]**2
Ric2 = sp.Integer(0)
for i in range(4):
    for j in range(4):
        Ric2 += gi[i]*gi[j]*Ric[i][j]*Ric[j][i]
C2 = sp.simplify(K - 2*Ric2 + Rsc**2/3)
Q = sp.simplify(sp.exp(B['a']['v'] + B['b']['v'] + 2*B['c']['v'])*r**2 * C2)
print('C2 terms:', len(sp.Add.make_args(sp.expand(C2))), 'time', time.time()-t0, flush=True)
out = os.path.expanduser('~/workspace/warp-pilot/gate9/wc_symq_expr.json')
json.dump({'names': names, 'Q': str(Q), 'C2': str(C2)}, open(out, 'w'))
print('saved', out, flush=True)
