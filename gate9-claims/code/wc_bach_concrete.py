"""W-C concrete-function Bach variant test on T-b (Phi=0, b=sqrt(r)).
Computes, with A(r)=0, Blog(r)=-0.5 ln(1-r^{-1/2}) as CONCRETE sympy
functions, the two divergence placements and both Ricci-term signs:
  DD1 = nabla^a nabla^b C_{a m b n}   (slots 1,4 contracted)
  RC1 = R^{ab} C_{a m b n}
  DD2 = nabla^c nabla^d C_{m c n d}   (slots 2,4 contracted)
  RC2 = R^{cd} C_{m c n d}
and compares DD +/- (1/2) RC to the Phase-32 T-b closed forms.
No component is skipped anywhere (the v2/v3 lesson)."""
import sympy as sp, json, time
t0 = time.time()
r, th = sp.symbols('r th', positive=True)
n = 4
A = sp.Integer(0)
B = -sp.log(1 - r**sp.Rational(-1, 2))/2
g = sp.diag(-sp.exp(2*A), sp.exp(2*B), r**2, r**2*sp.sin(th)**2)
gi = g.inv()
coords = [sp.Symbol('t'), r, th, sp.Symbol('ph')]
dg = [[[sp.diff(g[i, j], coords[k]) for j in range(n)] for i in range(n)] for k in range(n)]
Gam = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[a, s]*(dg[b][s][c] + dg[c][s][b] - dg[s][b][c]) for s in range(n))/2
            Gam[a][b][c] = sp.simplify(v) if v != 0 else v
dGam = [[[[sp.diff(Gam[a][b][c], coords[l]) for c in range(n)] for b in range(n)] for a in range(n)] for l in range(n)]
Riem = [[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                v = dGam[c][a][b][d] - dGam[d][a][b][c]
                for s in range(n):
                    v += Gam[a][c][s]*Gam[s][b][d] - Gam[a][d][s]*Gam[s][b][c]
                Riem[a][b][c][d] = sp.simplify(v) if v != 0 else v
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
# all-lower covariant derivative DC[e][a][b][c][d], NO skips
DC = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    v = sp.diff(C[a][b][c][d], coords[e])
                    for s in range(n):
                        v -= Gam[s][e][a]*C[s][b][c][d] + Gam[s][e][b]*C[a][s][c][d] \
                             + Gam[s][e][c]*C[a][b][s][d] + Gam[s][e][d]*C[a][b][c][s]
                    DC[e][a][b][c][d] = sp.simplify(v) if v != 0 else v
print('DC', time.time()-t0, flush=True)
def cov3(H, e, a, b, c):
    v = sp.diff(H[a][b][c], coords[e])
    for s in range(n):
        v -= Gam[s][e][a]*H[s][b][c] + Gam[s][e][b]*H[a][s][c] + Gam[s][e][c]*H[a][b][s]
    return sp.simplify(v) if v != 0 else v
def cov3mix(K, e, a, m, nn):
    # K[a][m][n] is (1,2): slot a upper
    v = sp.diff(K[a][m][nn], coords[e])
    for s in range(n):
        v += Gam[a][e][s]*K[s][m][nn] - Gam[s][e][m]*K[a][s][nn] - Gam[s][e][nn]*K[a][m][s]
    return sp.simplify(v) if v != 0 else v
# Placement 2: H2[a][b][c] = nabla^d C_{a c b d} (as (0,3) in (a,b,c))
H2 = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            v = sum(gi[d, dp]*DC[dp][a][c][b][d] for d in range(n) for dp in range(n))
            H2[a][b][c] = sp.simplify(v) if v != 0 else v
DD2 = [[sp.Integer(0)]*n for _ in range(n)]; RC2 = [[sp.Integer(0)]*n for _ in range(n)]
for a in range(n):
    for b in range(n):
        DD2[a][b] = sp.simplify(sum(gi[c, e]*cov3(H2, e, a, b, c) for c in range(n) for e in range(n)))
        RC2[a][b] = sp.simplify(sum(gi[c, cp]*gi[d, dp]*Ric[cp][dp]*C[a][c][b][d]
                                    for c in range(n) for d in range(n) for cp in range(n) for dp in range(n)))
print('DD2/RC2', time.time()-t0, flush=True)
# Placement 1: Cmix[a][m][b][n] = C^a_{m b n}; DCmix; K1[a][m][n] = nabla^b C^a_{m b n}
Cmix = [[[[sum(gi[a, ap]*C[ap][m][b][nn] for ap in range(n)) for nn in range(n)] for b in range(n)] for m in range(n)] for a in range(n)]
DCmix = [[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
for e in range(n):
    for a in range(n):
        for m in range(n):
            for b in range(n):
                for nn in range(n):
                    v = sp.diff(Cmix[a][m][b][nn], coords[e])
                    for s in range(n):
                        v += Gam[a][e][s]*Cmix[s][m][b][nn]
                        v -= Gam[s][e][m]*Cmix[a][s][b][nn] + Gam[s][e][b]*Cmix[a][m][s][nn] \
                             + Gam[s][e][nn]*Cmix[a][m][b][s]
                    DCmix[e][a][m][b][nn] = sp.simplify(v) if v != 0 else v
K1 = [[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for m in range(n):
        for nn in range(n):
            v = sum(gi[b, bp]*DCmix[bp][a][m][b][nn] for b in range(n) for bp in range(n))
            K1[a][m][nn] = sp.simplify(v) if v != 0 else v
DD1 = [[sp.Integer(0)]*n for _ in range(n)]; RC1 = [[sp.Integer(0)]*n for _ in range(n)]
for m in range(n):
    for nn in range(n):
        DD1[m][nn] = sp.simplify(sum(gi[a, ap]*cov3mix(K1, ap, a, m, nn) for a in range(n) for ap in range(n)))
        RC1[m][nn] = sp.simplify(sum(gi[a, ap]*gi[b, bp]*Ric[ap][bp]*C[a][m][b][nn]
                                     for a in range(n) for b in range(n) for ap in range(n) for bp in range(n)))
print('DD1/RC1', time.time()-t0, flush=True)
def mixed(T, i):
    return sp.simplify(sum(gi[i, s]*T[s][i] for s in range(n))).subs(th, sp.pi/2)
import numpy as np
def closed(rr):
    u = np.sqrt(rr)
    return np.array([-5*(3*u-1)/(24*rr**5), -5*(4*u-1)/(48*rr**5), 5*(10*u-3)/(96*rr**5)])
out = {}
for name, DD, RC in (('P1', DD1, RC1), ('P2', DD2, RC2)):
    for sgn in ('+', '-'):
        vals = {}
        for rv in (1.5, 2.0, 5.0):
            got = []
            for i in range(3):
                e = mixed(DD, i) + (1 if sgn == '+' else -1)*sp.Rational(1, 2)*mixed(RC, i)
                got.append(float(e.subs(r, rv)))
            vals[str(rv)] = {'got': got, 'closed': list(closed(rv)),
                             'ratio': [float(c/g) if g != 0 else None for c, g in zip(closed(rv), got)]}
        out[name+sgn] = vals
        print(name+sgn, json.dumps(vals), flush=True)
json.dump(out, open(os.path.expanduser('~/workspace/warp-pilot/gate9/results/wc_bach_concrete.json'), 'w'), indent=1)
print('DONE', time.time()-t0, flush=True)
