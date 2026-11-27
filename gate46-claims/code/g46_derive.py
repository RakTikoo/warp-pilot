#!/usr/bin/env python3
"""
g46_derive.py -- Gate-46 symbolic derivation (run once).

Derives the Einstein tensor of the registered metric ansatz
with sympy, in SPHERICAL coordinates (t, r, th, ph) -- an
organisation used by no earlier read in this lineage (the
lineage used hand-derived radial formulas; Gate-43 loop
contractions in Cartesian; Gate-45 forward-mode AD jets with
whole-array einsum in Cartesian).

The metric is prescribed componentwise (the registered
ansatz): in Cartesian form g_tt = -N(r)^2, g_tx = -BETA*S(r)
(shift along x only), g_ty = g_tz = 0, and the spatial metric
gamma = delta + (M(r)-1) n n. Transformed to spherical
coordinates:

  g_tt  = -N^2
  g_tr  = -BETA*S*sin(th)*cos(ph)
  g_tth = -BETA*S*r*cos(th)*cos(ph)
  g_tph = +BETA*S*r*sin(th)*sin(ph)
  g_rr  = M,  g_thth = r^2,  g_phph = r^2 sin^2(th)

with S, N, M functions of r alone; the spacetime is
stationary. T = G / (8 pi). The derived components are
stored as srepr strings in g46_exprs.py with the radial
derivatives replaced by symbols (S, Sp, Spp, ...), ready for
lambdify in g46_lib.py.

Robustness (this derivation's first two attempts died in
unbounded simplify calls, whose cost varies run to run):
the inverse metric is built analytically by the block
Schur complement (the spatial block is diagonal in these
coordinates) and verified numerically in the gate's
calibrations; every simplify/factor call is time-boxed by
SIGALRM with a cancel/raw fallback; the Ricci and Einstein
stages are accumulated raw.
"""
import signal

import sympy as sp

BETA = sp.Rational(11, 10)


class _Timeout(Exception):
    pass


def _alarm(sig, frame):
    raise _Timeout()


signal.signal(signal.SIGALRM, _alarm)


def timeboxed(fn, expr, seconds):
    signal.alarm(seconds)
    try:
        return fn(expr), True
    except _Timeout:
        return expr, False
    finally:
        signal.alarm(0)


t, r, th, ph = sp.symbols('t r th ph')
coords = [t, r, th, ph]
S = sp.Function('S')(r)
N = sp.Function('N')(r)
M = sp.Function('M')(r)

g = sp.zeros(4, 4)
g[0, 0] = -N ** 2
g[0, 1] = g[1, 0] = -BETA * S * sp.sin(th) * sp.cos(ph)
g[0, 2] = g[2, 0] = -BETA * S * r * sp.cos(th) * sp.cos(ph)
g[0, 3] = g[3, 0] = BETA * S * r * sp.sin(th) * sp.sin(ph)
g[1, 1] = M
g[2, 2] = r ** 2
g[3, 3] = r ** 2 * sp.sin(th) ** 2

# Inverse by the block Schur complement: g = [[A, b^T], [b, D]]
# with D = diag(M, r^2, r^2 sin^2 th). sch = A - b^T D^-1 b;
# g^tt = 1/sch, g^ti = -(D^-1 b)^i / sch,
# g^ij = D^-1_ij + (D^-1 b)^i (D^-1 b)^j / sch.
A = g[0, 0]
bvec = [g[i, 0] for i in range(1, 4)]
Dinv = [1 / M, 1 / r ** 2, 1 / (r ** 2 * sp.sin(th) ** 2)]
Db = [Dinv[i] * bvec[i] for i in range(3)]
sch = A - sum(bvec[i] * Db[i] for i in range(3))
ginv = sp.zeros(4, 4)
ginv[0, 0] = 1 / sch
for i in range(3):
    ginv[0, i + 1] = ginv[i + 1, 0] = -Db[i] / sch
    for j in range(3):
        ginv[i + 1, j + 1] = (Dinv[i] if i == j else 0) \
            + Db[i] * Db[j] / sch
print('inverse (Schur) done', flush=True)

# Christoffel Gamma^a_bc; simplify time-boxed per component.
Gam = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
for a in range(4):
    for b in range(4):
        for c in range(b, 4):
            expr = 0
            for d in range(4):
                if ginv[a, d] == 0:
                    continue
                expr += ginv[a, d] * (
                    sp.diff(g[d, c], coords[b])
                    + sp.diff(g[d, b], coords[c])
                    - sp.diff(g[b, c], coords[d]))
            expr, ok = timeboxed(sp.simplify, expr / 2, 20)
            if not ok:
                expr, _ = timeboxed(sp.cancel, expr, 10)
            Gam[a][b][c] = expr
            Gam[a][c][b] = expr
print('christoffel done', flush=True)

# Ricci R_bd = d_a Gam^a_bd - d_d Gam^a_ba
#            + Gam^a_ae Gam^e_bd - Gam^a_de Gam^e_ba (raw).
Ric = sp.zeros(4, 4)
for b in range(4):
    for d in range(b, 4):
        expr = 0
        for a in range(4):
            if Gam[a][b][d] != 0:
                expr += sp.diff(Gam[a][b][d], coords[a])
            if Gam[a][b][a] != 0:
                expr -= sp.diff(Gam[a][b][a], coords[d])
            for e in range(4):
                if Gam[a][a][e] != 0 and Gam[e][b][d] != 0:
                    expr += Gam[a][a][e] * Gam[e][b][d]
                if Gam[a][d][e] != 0 and Gam[e][b][a] != 0:
                    expr -= Gam[a][d][e] * Gam[e][b][a]
        Ric[b, d] = expr
        Ric[d, b] = expr
        print('ricci component', b, d, 'done', flush=True)
print('ricci done', flush=True)

Rs = sum(ginv[a, b] * Ric[a, b] for a in range(4) for b in range(4))
G = Ric - sp.Rational(1, 2) * Rs * g
T = G / (8 * sp.pi)

# replace functions and their derivatives by symbols
Ss, Sps, Spps = sp.symbols('Sv Spv Sppv')
Ns, Nps, Npps = sp.symbols('Nv Npv Nppv')
Ms, Mps, Mpps = sp.symbols('Mv Mpv Mppv')
subs = {
    sp.Derivative(sp.Function('S')(r), (r, 2)): Spps,
    sp.Derivative(sp.Function('N')(r), (r, 2)): Npps,
    sp.Derivative(sp.Function('M')(r), (r, 2)): Mpps,
    sp.Derivative(sp.Function('S')(r), r): Sps,
    sp.Derivative(sp.Function('N')(r), r): Nps,
    sp.Derivative(sp.Function('M')(r), r): Mps,
    sp.Function('S')(r): Ss,
    sp.Function('N')(r): Ns,
    sp.Function('M')(r): Ms,
}

out = {}
for a in range(4):
    for b in range(a, 4):
        expr = T[a, b].subs(subs)
        leftover = {x for x in expr.atoms(sp.Function)
                    if getattr(x.func, '__name__', '') in ('S', 'N', 'M')}
        leftover |= expr.atoms(sp.Derivative)
        assert not leftover, (a, b, leftover)
        expr, ok = timeboxed(sp.factor, expr, 30)
        out[(a, b)] = sp.srepr(expr)
        print('component', a, b, 'factored' if ok else 'raw',
              'len', len(out[(a, b)]), flush=True)

with open('g46_exprs.py', 'w') as fh:
    fh.write('# Generated by g46_derive.py (sympy, spherical\n')
    fh.write('# coordinates). T_ab srepr strings, args order:\n')
    fh.write('# (r, th, ph, Sv, Spv, Sppv, Nv, Npv, Nppv,\n')
    fh.write('#  Mv, Mpv, Mppv). T = G / (8 pi), stationary.\n')
    fh.write('EXPRS = {\n')
    for k in sorted(out):
        fh.write(f'    {k}: {out[k]!r},\n')
    fh.write('}\n')
print('written g46_exprs.py', flush=True)
