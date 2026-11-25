"""
wa_symbolic.py — Gate-10 W-A SYMBOLIC RADIAL-REDUCTION derivation.

Fresh derivation (Gate-7 pattern, written for Gate-10) of the Einstein
tensor of the registered composed metric form
    g_tt = -exp(2a(r)),  g_tx = -V(r),
    g_ij = delta_ij + (exp(2b(r))-1) n_i n_j ,  n_i = x_i/r,
where V(r) is the TOTAL composed shift profile (the Phase-46 staircase
V = beta_o S_o + beta_i S_i enters only at evaluation time, through the
analytic derivatives of V). Atoms:
    (r, n_x, n_y, n_z, a, a', a'', b, b', b'', V, V', V'').

Radial reduction: spatial derivatives act through the exact chain-rule
identities
    d_k r   = n_k
    d_k n_i = (delta_ki - n_k n_i)/r
    d_k f(r) = f'(r) n_k      for f in {a, b, V}
    d_k f'(r) = f''(r) n_k
No Cartesian finite-difference stencil appears anywhere: first and
second spatial derivatives of every metric component are produced by
the symbolic operator D below; the inverse metric is the closed-form
block (Schur) inverse; d(ginv) is the exact algebra -ginv dg ginv;
Gamma, dGamma, Ricci and G are assembled as SymPy expression trees
from those symbolic objects.

This script only DERIVES and caches the expressions (wa_g_expr.pkl)
plus a derivation log (wa_derivation.json). The Minkowski anchor (i)
is executed on the lambdified expressions in wa_run.py.
Run: ~/workspace/warp-pilot/venv/bin/python wa_symbolic.py. float64
at evaluation time.
"""
import json, pickle, sys, time
import numpy as np
import sympy as sp

t0 = time.time()
LOG = {'python': sys.version, 'sympy': sp.__version__,
       'run_with': '~/workspace/warp-pilot/venv/bin/python'}

r = sp.symbols('r')
nx, ny, nz = sp.symbols('nx ny nz')
n = [nx, ny, nz]
a, b, V = sp.symbols('a b V')
ap, bp, Vp = sp.symbols('ap bp Vp')
app, bpp, Vpp = sp.symbols('app bpp Vpp')
ATOMS = [r, nx, ny, nz, a, b, V, ap, bp, Vp]  # app/bpp/Vpp enter only via D(ap) etc.


def atom_deriv(atom, k):
    if atom == r:
        return n[k]
    if atom in (nx, ny, nz):
        i = [nx, ny, nz].index(atom)
        return ((1 if i == k else 0) - n[k] * n[i]) / r
    if atom == a:
        return ap * n[k]
    if atom == b:
        return bp * n[k]
    if atom == V:
        return Vp * n[k]
    if atom == ap:
        return app * n[k]
    if atom == bp:
        return bpp * n[k]
    if atom == Vp:
        return Vpp * n[k]
    raise ValueError(str(atom))


def D(expr, k):
    """Symbolic spatial derivative d/dx_k via the radial chain rule."""
    expr = sp.expand(expr)
    tot = sp.Integer(0)
    for at in ATOMS:
        d = sp.diff(expr, at)
        if d != 0:
            tot += d * atom_deriv(at, k)
    return sp.expand(tot)


# ---------------- metric and closed-form inverse ----------------
E = sp.exp(2 * a)
F = sp.exp(2 * b)
g = sp.zeros(4, 4)
g[0, 0] = -E
g[0, 1] = g[1, 0] = -V
for i in range(3):
    for j in range(3):
        g[1 + i, 1 + j] = (1 if i == j else 0) + (F - 1) * n[i] * n[j]

gi_sp = sp.zeros(3, 3)  # inverse of spatial gamma
for i in range(3):
    for j in range(3):
        gi_sp[i, j] = (1 if i == j else 0) + (sp.exp(-2 * b) - 1) * n[i] * n[j]
cvec = sp.Matrix([-V, 0, 0])                 # beta_cov (only x component)
w = gi_sp * cvec                             # gamma^{-1} . beta_cov
alpha2 = E + (cvec.T * w)[0]                 # lapse^2 = e^{2a} + c^T gamma^{-1} c
ginv = sp.zeros(4, 4)
ginv[0, 0] = -1 / alpha2
for i in range(3):
    ginv[0, 1 + i] = ginv[1 + i, 0] = w[i] / alpha2
    for j in range(3):
        ginv[1 + i, 1 + j] = gi_sp[i, j] - w[i] * w[j] / alpha2

# numeric spot-check of the inverse at random atoms (n a unit vector)
rng = np.random.default_rng(11)
max_inv_err = 0.0
for _ in range(5):
    th = rng.uniform(0, 2 * np.pi); ph = np.arccos(rng.uniform(-1, 1))
    vals = {r: 13.7, nx: float(np.sin(ph) * np.cos(th)), ny: float(np.sin(ph) * np.sin(th)),
            nz: float(np.cos(ph)), a: -0.31, b: 0.11, V: 0.037, ap: 0.02, bp: -0.01, Vp: -0.04,
            app: 0.002, bpp: 0.001, Vpp: 0.003}
    prod = np.array((g * ginv).subs(vals), dtype=float)
    max_inv_err = max(max_inv_err, float(np.max(np.abs(prod - np.eye(4)))))
LOG['ginv_numeric_check_max_err'] = max_inv_err
print(f'[sym] ginv check max err {max_inv_err:.3e}  ({time.time()-t0:.0f}s)', flush=True)
assert max_inv_err < 1e-12

# ---------------- symbolic first/second spatial derivatives ----------------
dg = [[[None] * 4 for _ in range(4)] for _ in range(4)]
for mu in range(4):
    for nu in range(4):
        for rho_ in range(4):
            dg[mu][nu][rho_] = sp.Integer(0) if mu == 0 else D(g[nu, rho_], mu - 1)
print(f'[sym] dg done ({time.time()-t0:.0f}s)', flush=True)
d2 = [[[[None] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for e in range(4):
    for mu in range(4):
        for nu in range(4):
            for rho_ in range(4):
                if e == 0 or mu == 0:
                    d2[e][mu][nu][rho_] = sp.Integer(0)
                else:
                    d2[e][mu][nu][rho_] = D(dg[mu][nu][rho_], e - 1)
print(f'[sym] d2g done ({time.time()-t0:.0f}s)', flush=True)

dginv = [None] * 4
for e in range(4):
    if e == 0:
        dginv[e] = sp.zeros(4, 4)
    else:
        dge = sp.Matrix(4, 4, lambda i, j: dg[e][i][j])
        dginv[e] = -ginv * dge * ginv
print(f'[sym] dginv done ({time.time()-t0:.0f}s)', flush=True)

# ---------------- Gamma, dGamma, Ricci, Einstein (expression trees) ----------------
Gamma = [[[None] * 4 for _ in range(4)] for _ in range(4)]
for aa in range(4):
    for bb in range(4):
        for cc in range(4):
            tot = sp.Integer(0)
            for d in range(4):
                if ginv[aa, d] == 0:
                    continue
                tot += ginv[aa, d] * (dg[bb][d][cc] + dg[cc][d][bb] - dg[d][bb][cc])
            Gamma[aa][bb][cc] = sp.Rational(1, 2) * tot if tot != 0 else sp.Integer(0)
print(f'[sym] Gamma done ({time.time()-t0:.0f}s)', flush=True)

dGamma = [[[[None] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
for e in range(4):
    for aa in range(4):
        for bb in range(4):
            for cc in range(4):
                if e == 0:
                    dGamma[e][aa][bb][cc] = sp.Integer(0)
                    continue
                tot = sp.Integer(0)
                for d in range(4):
                    combo = dg[bb][d][cc] + dg[cc][d][bb] - dg[d][bb][cc]
                    if dginv[e][aa, d] != 0:
                        tot += dginv[e][aa, d] * combo
                    if ginv[aa, d] != 0:
                        tot += ginv[aa, d] * (d2[e][bb][d][cc] + d2[e][cc][d][bb] - d2[e][d][bb][cc])
                dGamma[e][aa][bb][cc] = sp.Rational(1, 2) * tot if tot != 0 else sp.Integer(0)
print(f'[sym] dGamma done ({time.time()-t0:.0f}s)', flush=True)

Ricci = [[None] * 4 for _ in range(4)]
for bb in range(4):
    for dd in range(4):
        tot = sp.Integer(0)
        for aa in range(4):
            tot += dGamma[aa][aa][bb][dd] - dGamma[dd][aa][bb][aa]
            for e in range(4):
                tot += Gamma[aa][aa][e] * Gamma[e][bb][dd] - Gamma[aa][dd][e] * Gamma[e][bb][aa]
        Ricci[bb][dd] = tot
Rsc = sp.Integer(0)
for i in range(4):
    for j in range(4):
        if ginv[i, j] != 0:
            Rsc += ginv[i, j] * Ricci[i][j]
Gcomp = {}
for i in range(4):
    for j in range(i, 4):
        Gcomp[(i, j)] = Ricci[i][j] - sp.Rational(1, 2) * Rsc * g[i, j]
print(f'[sym] G trees done ({time.time()-t0:.0f}s)', flush=True)

LOG['minkowski_check'] = ('deferred to wa_run.py lambdified evaluation '
                          '(a=b=V=0, all radial derivatives 0, generic (r,n) points)')
LOG['elapsed_s'] = time.time() - t0
ATOM_LIST = [r, nx, ny, nz, a, ap, app, b, bp, bpp, V, Vp, Vpp]
with open('/home/hatch/workspace/warp-pilot/gate10/wa_g_expr.pkl', 'wb') as fh:
    pickle.dump({'Gcomp': Gcomp, 'atoms': ATOM_LIST, 'g': g, 'ginv': ginv}, fh)
json.dump(LOG, open('/home/hatch/workspace/warp-pilot/gate10/wa_derivation.json', 'w'), indent=1)
print(f'[sym] SAVED wa_g_expr.pkl; TOTAL {time.time()-t0:.0f}s', flush=True)
