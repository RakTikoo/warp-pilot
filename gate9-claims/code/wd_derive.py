#!/usr/bin/env python3
"""W-D fresh derivation: Bach tensor jet formulas for the static spherical
ansatz ds^2 = -e^{2P(r)} dt^2 + dr^2/(1-b(r)/r) + r^2 dOmega^2, from the
metric, using the Ricci form of the Bach tensor (the shared definition,
arXiv:2505.17171 eq.6 form):
  B_mn = Box R_mn - (1/3) nabla_m nabla_n R - (1/6) g_mn Box R
         + 2 R^{ab} R_{m a n b} - (1/2) g_mn R^{ab}R_ab
         - (2/3) R R_mn + (1/6) g_mn R^2
Written fresh for Gate 9 (W-D); no phase script is imported.
Output: gate9/wd_generic_bach.json with B^t_t, B^r_r, B^th_th as functions
of (r, b0..b4, P1..P4), plus the symbolic trace."""
import sympy as sp, json, time
t0 = time.time()
r, th = sp.symbols('r th', positive=True)
b = sp.Function('b')(r); P = sp.Function('P')(r)
coords = [sp.Symbol('t'), r, th, sp.Symbol('ph')]
n = 4
E = sp.exp(2*P); G = 1/(1 - b/r)
g = sp.diag(-E, G, r**2, r**2*sp.sin(th)**2)
ginv = g.inv()

def dg(i, j, k):
    return sp.diff(g[i, j], coords[k]) if g[i, j] != 0 else sp.Integer(0)

Gam = {}
for a in range(n):
    for bb in range(n):
        for c in range(n):
            e = sum(ginv[a, d]*(dg(d, bb, c) + dg(d, c, bb) - dg(bb, c, d))
                    for d in range(n) if ginv[a, d] != 0)/2
            e = sp.simplify(e)
            if e != 0: Gam[(a, bb, c)] = e
def gam(a, bb, c): return Gam.get((a, bb, c), sp.Integer(0))
print('Gamma', time.time()-t0, len(Gam), flush=True)

Riem = {}
for a in range(n):
    for bb in range(n):
        for c in range(n):
            for d in range(n):
                if c >= d: continue
                e = sp.diff(gam(a, bb, d), coords[c]) - sp.diff(gam(a, bb, c), coords[d])
                for s in range(n):
                    e += gam(a, c, s)*gam(s, bb, d) - gam(a, d, s)*gam(s, bb, c)
                e = sp.simplify(e)
                if e != 0: Riem[(a, bb, c, d)] = e; Riem[(a, bb, d, c)] = -e
def riem(a, bb, c, d): return Riem.get((a, bb, c, d), sp.Integer(0))
print('Riemann', time.time()-t0, len(Riem), flush=True)

Ric = {}
for bb in range(n):
    for d in range(n):
        e = sp.simplify(sum(riem(a, bb, a, d) for a in range(n)))
        if e != 0: Ric[(bb, d)] = e
def ric(i, j): return Ric.get((i, j), sp.Integer(0))
Rsc = sp.simplify(sum(ginv[i, j]*ric(i, j) for i in range(n) for j in range(n) if ginv[i, j] != 0))
print('Ricci', time.time()-t0, flush=True)

D1 = {}
for a in range(n):
    for m in range(n):
        for nn in range(n):
            e = sp.diff(ric(m, nn), coords[a])
            for s in range(n):
                e -= gam(s, a, m)*ric(s, nn) + gam(s, a, nn)*ric(m, s)
            e = sp.simplify(e)
            if e != 0: D1[(a, m, nn)] = e
def d1(a, m, nn): return D1.get((a, m, nn), sp.Integer(0))
print('D1', time.time()-t0, len(D1), flush=True)

D2 = {}
for a in range(n):
    for bb in range(n):
        for m in range(n):
            for nn in range(n):
                e = sp.diff(d1(bb, m, nn), coords[a])
                for s in range(n):
                    e -= gam(s, a, bb)*d1(s, m, nn) + gam(s, a, m)*d1(bb, s, nn) + gam(s, a, nn)*d1(bb, m, s)
                e = sp.simplify(e)
                if e != 0: D2[(a, bb, m, nn)] = e
def d2(a, bb, m, nn): return D2.get((a, bb, m, nn), sp.Integer(0))
print('D2', time.time()-t0, len(D2), flush=True)

BoxRic = {}
for m in range(n):
    for nn in range(n):
        e = sp.simplify(sum(ginv[a, bb]*d2(a, bb, m, nn) for a in range(n) for bb in range(n) if ginv[a, bb] != 0))
        if e != 0: BoxRic[(m, nn)] = e
def boxric(m, nn): return BoxRic.get((m, nn), sp.Integer(0))

dR = [sp.diff(Rsc, coords[i]) for i in range(n)]
Hess = {}
for m in range(n):
    for nn in range(n):
        e = sp.diff(dR[nn], coords[m]) - sum(gam(s, m, nn)*dR[s] for s in range(n))
        e = sp.simplify(e)
        if e != 0: Hess[(m, nn)] = e
def hess(m, nn): return Hess.get((m, nn), sp.Integer(0))
BoxR = sp.simplify(sum(ginv[a, bb]*hess(a, bb) for a in range(n) for bb in range(n) if ginv[a, bb] != 0))

RicUp = {}
for i in range(n):
    for j in range(n):
        e = sp.simplify(sum(ginv[i, a]*ginv[j, bb]*ric(a, bb) for a in range(n) for bb in range(n)))
        if e != 0: RicUp[(i, j)] = e
def ricup(i, j): return RicUp.get((i, j), sp.Integer(0))
RicSq = sp.simplify(sum(ricup(i, j)*ric(i, j) for i in range(n) for j in range(n)))

def rlow(m, rr, nn, s):
    return sum(g[m, e]*riem(e, rr, nn, s) for e in range(n) if g[m, e] != 0)

Bmix = {}
for m in range(n):
    nn = m
    quad = sum(ricup(rr, s)*rlow(m, rr, nn, s) for rr in range(n) for s in range(n))
    Bcov = (boxric(m, nn) - sp.Rational(1, 3)*hess(m, nn) - sp.Rational(1, 6)*g[m, nn]*BoxR
            + 2*quad - sp.Rational(1, 2)*g[m, nn]*RicSq - sp.Rational(2, 3)*Rsc*ric(m, nn)
            + sp.Rational(1, 6)*g[m, nn]*Rsc**2)
    Bmix[m] = sp.simplify(sum(ginv[m, a]*(Bcov if a == nn else 0) for a in range(n)))
    print(f'Bmix[{m}]', time.time()-t0, 'len', len(str(Bmix[m])), flush=True)

trace = sp.simplify(sum(Bmix[i] for i in range(n)))
print('trace:', trace, flush=True)

db = [b] + [sp.diff(b, r, k) for k in range(1, 5)]
dP = [sp.diff(P, r, k) for k in range(1, 5)]
Bsym = sp.symbols('b0 b1 b2 b3 b4'); Psym = sp.symbols('P1 P2 P3 P4')
repl = {db[i]: Bsym[i] for i in range(5)}
repl.update({dP[i]: Psym[i] for i in range(4)})
repl[P] = sp.Integer(0)
out = {}
for i, nm in [(0, 'Bt'), (1, 'Br'), (2, 'Bth')]:
    e = Bmix[i].subs(repl)
    out[nm] = str(sp.factor(e))
    print(nm, 'len', len(out[nm]), 'bare P:', 'P(r)' in out[nm], 'exp:', 'exp' in out[nm], flush=True)
out['trace'] = str(trace.subs(repl))
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate9/wd_generic_bach.json', 'w'), indent=1)
print('TOTAL', time.time()-t0, flush=True)
