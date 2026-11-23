#!/usr/bin/env python3
"""W-D fresh symbolic check: Bach tensor on a GENERAL Robertson-Walker metric
ds^2 = -dt^2 + a(t)^2 [ dr^2/(1-k r^2) + r^2 dOmega^2 ], a(t) an arbitrary
function, k a free constant. Computes (1) the independent Weyl components,
(2) the Bach tensor via the Ricci form (shared definition). Both must vanish
identically. Written fresh for Gate 9 (W-D)."""
import sympy as sp, json, time
t0 = time.time()
t, r, th = sp.symbols('t r th', positive=True)
k = sp.symbols('k')
a = sp.Function('a')(t)
coords = [t, r, th, sp.Symbol('ph')]
n = 4
A2 = a**2
g = sp.diag(-1, A2/(1-k*r**2), A2*r**2, A2*r**2*sp.sin(th)**2)
ginv = g.inv()

def dg(i, j, kk):
    return sp.diff(g[i, j], coords[kk]) if g[i, j] != 0 else sp.Integer(0)

Gam = {}
for aa in range(n):
    for bb in range(n):
        for c in range(n):
            e = sum(ginv[aa, d]*(dg(d, bb, c) + dg(d, c, bb) - dg(bb, c, d))
                    for d in range(n) if ginv[aa, d] != 0)/2
            e = sp.simplify(e)
            if e != 0: Gam[(aa, bb, c)] = e
def gam(aa, bb, c): return Gam.get((aa, bb, c), sp.Integer(0))
print('Gamma', time.time()-t0, len(Gam), flush=True)

Riem = {}
for aa in range(n):
    for bb in range(n):
        for c in range(n):
            for d in range(n):
                if c >= d: continue
                e = sp.diff(gam(aa, bb, d), coords[c]) - sp.diff(gam(aa, bb, c), coords[d])
                for s in range(n):
                    e += gam(aa, c, s)*gam(s, bb, d) - gam(aa, d, s)*gam(s, bb, c)
                e = sp.simplify(e)
                if e != 0: Riem[(aa, bb, c, d)] = e; Riem[(aa, bb, d, c)] = -e
def riem(aa, bb, c, d): return Riem.get((aa, bb, c, d), sp.Integer(0))
print('Riemann', time.time()-t0, len(Riem), flush=True)

Ric = {}
for bb in range(n):
    for d in range(n):
        e = sp.simplify(sum(riem(aa, bb, aa, d) for aa in range(n)))
        if e != 0: Ric[(bb, d)] = e
def ric(i, j): return Ric.get((i, j), sp.Integer(0))
Rsc = sp.simplify(sum(ginv[i, j]*ric(i, j) for i in range(n) for j in range(n) if ginv[i, j] != 0))
print('Ricci', time.time()-t0, 'R =', Rsc, flush=True)

# Weyl tensor C_{abcd} (fully covariant)
def rlow(aa, bb, c, d):
    return sum(g[aa, e]*riem(e, bb, c, d) for e in range(n) if g[aa, e] != 0)
weyl = {}
for aa in range(n):
    for bb in range(n):
        for c in range(n):
            for d in range(n):
                e = (rlow(aa, bb, c, d)
                     - sp.Rational(1, 2)*(g[aa, c]*ric(bb, d) - g[aa, d]*ric(bb, c)
                                          - g[bb, c]*ric(aa, d) + g[bb, d]*ric(aa, c))
                     + Rsc/6*(g[aa, c]*g[bb, d] - g[aa, d]*g[bb, c]))
                e = sp.simplify(e)
                if e != 0: weyl[(aa, bb, c, d)] = e
print('Weyl nonzero components:', len(weyl), {kk: str(vv)[:80] for kk, vv in list(weyl.items())[:5]}, flush=True)

# Bach via Ricci form
D1 = {}
for aa in range(n):
    for m in range(n):
        for nn in range(n):
            e = sp.diff(ric(m, nn), coords[aa])
            for s in range(n):
                e -= gam(s, aa, m)*ric(s, nn) + gam(s, aa, nn)*ric(m, s)
            e = sp.simplify(e)
            if e != 0: D1[(aa, m, nn)] = e
def d1(aa, m, nn): return D1.get((aa, m, nn), sp.Integer(0))
D2 = {}
for aa in range(n):
    for bb in range(n):
        for m in range(n):
            for nn in range(n):
                e = sp.diff(d1(bb, m, nn), coords[aa])
                for s in range(n):
                    e -= gam(s, aa, bb)*d1(s, m, nn) + gam(s, aa, m)*d1(bb, s, nn) + gam(s, aa, nn)*d1(bb, m, s)
                e = sp.simplify(e)
                if e != 0: D2[(aa, bb, m, nn)] = e
def d2(aa, bb, m, nn): return D2.get((aa, bb, m, nn), sp.Integer(0))
print('D2', time.time()-t0, len(D2), flush=True)
BoxRic = {}
for m in range(n):
    for nn in range(n):
        e = sp.simplify(sum(ginv[aa, bb]*d2(aa, bb, m, nn) for aa in range(n) for bb in range(n) if ginv[aa, bb] != 0))
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
BoxR = sp.simplify(sum(ginv[aa, bb]*hess(aa, bb) for aa in range(n) for bb in range(n) if ginv[aa, bb] != 0))
RicUp = {}
for i in range(n):
    for j in range(n):
        e = sp.simplify(sum(ginv[i, aa]*ginv[j, bb]*ric(aa, bb) for aa in range(n) for bb in range(n)))
        if e != 0: RicUp[(i, j)] = e
def ricup(i, j): return RicUp.get((i, j), sp.Integer(0))
RicSq = sp.simplify(sum(ricup(i, j)*ric(i, j) for i in range(n) for j in range(n)))
Bmix = {}
for m in range(n):
    nn = m
    quad = sum(ricup(rr, s)*rlow(m, rr, nn, s) for rr in range(n) for s in range(n))
    Bcov = (boxric(m, nn) - sp.Rational(1, 3)*hess(m, nn) - sp.Rational(1, 6)*g[m, nn]*BoxR
            + 2*quad - sp.Rational(1, 2)*g[m, nn]*RicSq - sp.Rational(2, 3)*Rsc*ric(m, nn)
            + sp.Rational(1, 6)*g[m, nn]*Rsc**2)
    Bmix[m] = sp.simplify(sum(ginv[m, aa]*(Bcov if aa == nn else 0) for aa in range(n)))
    print(f'Bmix[{m}] =', Bmix[m], flush=True)
out = {"metric": "general RW: -dt^2 + a(t)^2[dr^2/(1-k r^2)+r^2 dOmega^2], a(t) arbitrary, k free",
       "weyl_nonzero_components": len(weyl),
       "bach_mixed_diagonal": {str(i): str(Bmix[i]) for i in range(n)},
       "bach_all_zero": bool(all(Bmix[i] == 0 for i in range(n))),
       "weyl_all_zero": len(weyl) == 0,
       "elapsed_s": time.time()-t0}
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate9/wd_rw_result.json', 'w'), indent=1)
print('RW DONE', out['bach_all_zero'], out['weyl_all_zero'], flush=True)
