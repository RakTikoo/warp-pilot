"""
wa_symbolic.py -- Gate-11 W-A: symbolic radial reduction, derived fresh
for this gate in this file.

Metric form under audit (the registered composed form):
    ds^2 = -e^{2a(r)} dt^2 - 2 V(r) dt dx
           + [ delta_ij + (e^{2b(r)} - 1) n_i n_j ] dx^i dx^j ,
    n_i = x_i / r,  V(r) = total composed shift profile.
Only the combination (a, b, V) and their first two radial derivatives
enter the Einstein tensor.  We therefore derive G_mn symbolically with
SymPy treating
    A = (r, nx, ny, nz, a, a1, a2, b, b1, b2, V, V1, V2)
as atoms (a1 = a'(r) etc.), using the exact radial chain rules
    d_k r = n_k,   d_k n_i = (delta_ki - n_k n_i)/r,
    d_k f = f1 n_k,  d_k f1 = f2 n_k     (f in {a, b, V}),
to build every first and second spatial derivative of the metric
symbolically.  Time derivatives vanish (stationary ansatz).  The
inverse metric is written in closed block form and checked numerically
against g * ginv = I at random atom values; d(ginv) follows from the
exact identity d(ginv) = -ginv (dg) ginv.  Christoffel symbols, their
derivatives, Ricci, the scalar and G are then assembled as expression
trees and cached to wa_g11_expr.pkl for wa_eval.py.

No finite-difference stencil of any kind appears here or downstream:
derivatives of the actual profiles are supplied analytically by the
profile representations in wa_profiles.py.

Run with ~/workspace/warp-pilot/venv/bin/python.  float64 at evaluation.
"""
import json
import pickle
import sys
import time

import numpy as np
import sympy as sp

HERE = '/home/hatch/workspace/warp-pilot/gate11'
t_start = time.time()
meta = {'run_with': '~/workspace/warp-pilot/venv/bin/python',
        'sympy_version': sp.__version__, 'python': sys.version}

# ------------------------------------------------------------------ atoms
r = sp.symbols('r')
nx, ny, nz = sp.symbols('nx ny nz')
nvec = [nx, ny, nz]
a, a1, a2 = sp.symbols('a a1 a2')
b, b1, b2 = sp.symbols('b b1 b2')
V, V1, V2 = sp.symbols('V V1 V2')
BASE_ATOMS = [r, nx, ny, nz, a, b, V, a1, b1, V1]  # a2/b2/V2 reached via d(f1)


def d_atom(atom, k):
    """d(atom)/dx_k under the radial chain rule."""
    if atom is r:
        return nvec[k]
    if atom in nvec:
        i = nvec.index(atom)
        return ((1 if i == k else 0) - nvec[k] * nvec[i]) / r
    table = {a: a1, b: b1, V: V1, a1: a2, b1: b2, V1: V2}
    if atom in table:
        return table[atom] * nvec[k]
    raise KeyError(atom)


def Dop(expr, k):
    """Symbolic partial derivative wrt x_k of an atom polynomial."""
    expr = sp.expand(expr)
    out = sp.Integer(0)
    for at in BASE_ATOMS:
        part = sp.diff(expr, at)
        if part != 0:
            out += part * d_atom(at, k)
    return sp.expand(out)


# ------------------------------------------------------------------ metric
ea = sp.exp(2 * a)
eb = sp.exp(2 * b)
g = sp.zeros(4, 4)
g[0, 0] = -ea
g[1, 0] = g[0, 1] = -V
for i in range(3):
    for j in range(3):
        g[1 + i, 1 + j] = (1 if i == j else 0) + (eb - 1) * nvec[i] * nvec[j]

# closed-form inverse: gamma^{-1} for the spatial block, Schur complement
# for the (t, x) block (shift covector is (-V, 0, 0)).
gam_inv = sp.zeros(3, 3)
for i in range(3):
    for j in range(3):
        gam_inv[i, j] = (1 if i == j else 0) + (sp.exp(-2 * b) - 1) * nvec[i] * nvec[j]
beta_cov = sp.Matrix([-V, 0, 0])
wvec = gam_inv * beta_cov                       # gamma^{-1} beta_cov
lap2 = ea + (beta_cov.T * wvec)[0]              # alpha^2
ginv = sp.zeros(4, 4)
ginv[0, 0] = -1 / lap2
for i in range(3):
    ginv[0, 1 + i] = ginv[1 + i, 0] = wvec[i] / lap2
    for j in range(3):
        ginv[1 + i, 1 + j] = gam_inv[i, j] - wvec[i] * wvec[j] / lap2

rng = np.random.default_rng(23)
worst_inv = 0.0
for _ in range(6):
    th = float(rng.uniform(0, 2 * np.pi)); ph = float(np.arccos(rng.uniform(-1, 1)))
    subs = {r: 11.3, nx: float(np.sin(ph) * np.cos(th)),
            ny: float(np.sin(ph) * np.sin(th)), nz: float(np.cos(ph)),
            a: -0.27, b: 0.09, V: 0.041, a1: 0.017, b1: -0.008, V1: -0.03,
            a2: 0.0015, b2: 0.0007, V2: 0.0025}
    prod = np.array((g * ginv).subs(subs), dtype=float)
    worst_inv = max(worst_inv, float(np.max(np.abs(prod - np.eye(4)))))
meta['inverse_check_max_err'] = worst_inv
print(f'[wa_symbolic] inverse check max err {worst_inv:.3e}', flush=True)
assert worst_inv < 1e-12

# ------------------------------------------------- metric derivatives (exact)
# dg[e][mu][nu] = d_e g_{mu nu}; index 0 (time) is identically zero.
dg = [[[(sp.Integer(0) if e == 0 else None) for _ in range(4)]
       for _ in range(4)] for e in range(4)]
for e in range(1, 4):
    for mu in range(4):
        for nu in range(4):
            dg[e][mu][nu] = Dop(g[mu, nu], e - 1)
print(f'[wa_symbolic] dg built ({time.time()-t_start:.0f}s)', flush=True)

d2g = [[[[sp.Integer(0) for _ in range(4)] for _ in range(4)]
        for _ in range(4)] for _ in range(4)]
for e in range(1, 4):
    for mu in range(1, 4):
        for nu in range(4):
            for rho_ in range(4):
                d2g[e][mu][nu][rho_] = Dop(dg[mu][nu][rho_], e - 1)
print(f'[wa_symbolic] d2g built ({time.time()-t_start:.0f}s)', flush=True)

dginv = [sp.zeros(4, 4) for _ in range(4)]
for e in range(1, 4):
    dge = sp.Matrix(4, 4, lambda i, j: dg[e][i][j])
    dginv[e] = -ginv * dge * ginv
print(f'[wa_symbolic] dginv built ({time.time()-t_start:.0f}s)', flush=True)

# ------------------------------------------------------------- connections
Gamma = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
for up in range(4):
    for lo1 in range(4):
        for lo2 in range(4):
            acc = sp.Integer(0)
            for d in range(4):
                if ginv[up, d] == 0:
                    continue
                acc += ginv[up, d] * (dg[lo1][d][lo2] + dg[lo2][d][lo1]
                                      - dg[d][lo1][lo2])
            Gamma[up][lo1][lo2] = sp.Rational(1, 2) * acc if acc != 0 else sp.Integer(0)
print(f'[wa_symbolic] Gamma built ({time.time()-t_start:.0f}s)', flush=True)

dGamma = [[[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for e in range(1, 4):
    for up in range(4):
        for lo1 in range(4):
            for lo2 in range(4):
                acc = sp.Integer(0)
                for d in range(4):
                    combo = (dg[lo1][d][lo2] + dg[lo2][d][lo1] - dg[d][lo1][lo2])
                    if dginv[e][up, d] != 0:
                        acc += dginv[e][up, d] * combo
                    if ginv[up, d] != 0:
                        acc += ginv[up, d] * (d2g[e][lo1][d][lo2]
                                              + d2g[e][lo2][d][lo1]
                                              - d2g[e][d][lo1][lo2])
                dGamma[e][up][lo1][lo2] = (sp.Rational(1, 2) * acc
                                           if acc != 0 else sp.Integer(0))
print(f'[wa_symbolic] dGamma built ({time.time()-t_start:.0f}s)', flush=True)

Ric = [[sp.Integer(0)] * 4 for _ in range(4)]
for lo1 in range(4):
    for lo2 in range(4):
        acc = sp.Integer(0)
        for up in range(4):
            acc += dGamma[up][up][lo1][lo2] - dGamma[lo2][up][lo1][up]
            for e in range(4):
                acc += (Gamma[up][up][e] * Gamma[e][lo1][lo2]
                        - Gamma[up][lo2][e] * Gamma[e][lo1][up])
        Ric[lo1][lo2] = acc
Rscalar = sp.Integer(0)
for i in range(4):
    for j in range(4):
        if ginv[i, j] != 0:
            Rscalar += ginv[i, j] * Ric[i][j]
Gexpr = {}
for i in range(4):
    for j in range(i, 4):
        Gexpr[(i, j)] = Ric[i][j] - sp.Rational(1, 2) * Rscalar * g[i, j]
print(f'[wa_symbolic] Einstein trees built ({time.time()-t_start:.0f}s)', flush=True)

ATOM_ORDER = [r, nx, ny, nz, a, a1, a2, b, b1, b2, V, V1, V2]
with open(f'{HERE}/wa_g11_expr.pkl', 'wb') as fh:
    pickle.dump({'Gcomp': Gexpr, 'atoms': ATOM_ORDER}, fh)
meta['elapsed_s'] = time.time() - t_start
meta['minkowski'] = ('checked numerically on the lambdified expressions '
                     'in wa_run.py (all atoms except r, n set to zero)')
json.dump(meta, open(f'{HERE}/wa_derivation.json', 'w'), indent=1)
print(f'[wa_symbolic] saved wa_g11_expr.pkl in {meta["elapsed_s"]:.0f}s', flush=True)
