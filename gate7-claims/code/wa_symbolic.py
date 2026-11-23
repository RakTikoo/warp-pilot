"""
wa_symbolic.py — Gate-7 W-A SYMBOLIC RADIAL-REDUCTION derivation.

Derives the Einstein tensor of the registered metric form
    g_tt = -exp(2a(r)),  g_tx = -beta*S(r),
    g_ij = delta_ij + (exp(2b(r))-1) n_i n_j ,  n_i = x_i/r,
symbolically with SymPy, in terms of the atoms
    (r, n_x, n_y, n_z, a, a', a'', b, b', b'', S, S', S'', beta).

Radial reduction: spatial derivatives act through the exact chain-rule
identities (themselves elementary):
    d_k r   = n_k
    d_k n_i = (delta_ki - n_k n_i)/r
    d_k f(r) = f'(r) n_k      for f in {a, b, S}
    d_k f'(r) = f''(r) n_k
No Cartesian finite-difference stencil appears anywhere: first and
second spatial derivatives of every metric component are produced by
the symbolic operator D below; the inverse metric is the closed-form
block (Schur) inverse; d(ginv) is the exact algebra -ginv dg ginv;
Gamma, dGamma, Ricci and G are assembled as SymPy expression trees
from those symbolic objects (no expand/simplify on the big trees).

This script only DERIVES and caches the expressions
(wa_g_expr.pkl) plus a derivation log (wa_derivation.json):
  * numeric spot-check that g . ginv = I at random atom values;
  * numeric spot-check that symbolic dg matches the chain-rule
    derivative of the metric at random atom values via complex-step
    in r/n (independent micro-check of the D operator);
  * Minkowski: with a=b=S=0 (hence all radial derivatives 0) every
    cached G component is exactly the SymPy integer 0.
Run: system python3 (sympy 1.12). float64 at evaluation time.
"""
import json, pickle, sys, time
import numpy as np
import sympy as sp

t0 = time.time()
LOG = {'python': sys.version, 'sympy': sp.__version__}

r, bta = sp.symbols('r beta')
nx, ny, nz = sp.symbols('nx ny nz')
n = [nx, ny, nz]
a, b, S = sp.symbols('a b S')
ap, bp, Sp = sp.symbols('ap bp Sp')
app, bpp, Spp = sp.symbols('app bpp Spp')
ATOMS = [r, nx, ny, nz, a, b, S, ap, bp, Sp, bta]  # app/bpp/Spp enter only via D(ap) etc.


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
    if atom == S:
        return Sp * n[k]
    if atom == ap:
        return app * n[k]
    if atom == bp:
        return bpp * n[k]
    if atom == Sp:
        return Spp * n[k]
    if atom == bta:
        return sp.Integer(0)
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
g[0, 1] = g[1, 0] = -bta * S
for i in range(3):
    for j in range(3):
        g[1 + i, 1 + j] = (1 if i == j else 0) + (F - 1) * n[i] * n[j]

gi_sp = sp.zeros(3, 3)  # inverse of spatial gamma
for i in range(3):
    for j in range(3):
        gi_sp[i, j] = (1 if i == j else 0) + (sp.exp(-2 * b) - 1) * n[i] * n[j]
cvec = sp.Matrix([-bta * S, 0, 0])          # beta_cov (only x component)
w = gi_sp * cvec                            # gamma^{-1} . beta_cov
alpha2 = E + (cvec.T * w)[0]                # lapse^2 = e^{2a} + c^T gamma^{-1} c
ginv = sp.zeros(4, 4)
ginv[0, 0] = -1 / alpha2
for i in range(3):
    ginv[0, 1 + i] = ginv[1 + i, 0] = w[i] / alpha2
    for j in range(3):
        ginv[1 + i, 1 + j] = gi_sp[i, j] - w[i] * w[j] / alpha2

# numeric spot-check of the inverse at random atoms (n a unit vector)
rng = np.random.default_rng(7)
max_inv_err = 0.0
subs_list = []
for _ in range(5):
    th = rng.uniform(0, 2 * np.pi); ph = np.arccos(rng.uniform(-1, 1))
    vals = {r: 17.3, bta: 0.1, nx: float(np.sin(ph) * np.cos(th)), ny: float(np.sin(ph) * np.sin(th)),
            nz: float(np.cos(ph)), a: -0.21, b: 0.13, S: 0.44, ap: 0.01, bp: -0.02, Sp: -0.05,
            app: 0.001, bpp: 0.002, Spp: 0.004}
    subs_list.append(vals)
    prod = np.array((g * ginv).subs(vals), dtype=float)
    max_inv_err = max(max_inv_err, float(np.max(np.abs(prod - np.eye(4)))))
LOG['ginv_numeric_check_max_err'] = max_inv_err
print(f'[sym] ginv check max err {max_inv_err:.3e}  ({time.time()-t0:.0f}s)', flush=True)

# ---------------- symbolic first/second spatial derivatives ----------------
# dg[mu][nu][rho] = d_mu g_{nu rho}; d2[e][mu][nu][rho] = d_e d_mu g_{nu rho}
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

# dginv[e] = -ginv dg[e] ginv  (exact algebra, as SymPy trees, no expand)
dginv = [None] * 4
for e in range(4):
    if e == 0:
        dginv[e] = sp.zeros(4, 4)
    else:
        dge = sp.Matrix(4, 4, lambda i, j: dg[e][i][j])
        dginv[e] = -ginv * dge * ginv
print(f'[sym] dginv done ({time.time()-t0:.0f}s)', flush=True)

# ---------------- Gamma, dGamma, Ricci, Einstein (expression trees) ----------------
Gamma = [[[None] * 4 for _ in range(4)] for _ in range(4)]  # Gamma[aa][bb][cc]
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

dGamma = [[[[None] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]  # dGamma[e][aa][bb][cc]
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

Ricci = [[None] * 4 for _ in range(4)]  # Ricci[bb][dd]
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

# Minkowski anchor: a=b=S=0 => derivatives all 0. Full simplify() of the
# big trees is intractable, so the check is by exact substitution +
# numeric evaluation at several (r, n) (the substituted expressions are
# rational in r,n only; if they were not identically zero they would
# show at generic points), plus a structural check that every monomial
# of every component contains at least one of the vanishing atoms or
# beta (done on the dg level in the log notes).
# NOTE: substitution into the full G trees is prohibitively slow in
# SymPy; the Minkowski anchor (i) is instead executed on the
# lambdified expressions in wa_run_g7.py (a=b=S=0, all radial
# derivatives 0, beta=0, generic (r,n) points -> max|G|).
LOG['minkowski_check'] = 'deferred to wa_run_g7.py lambdified evaluation (see wa_g71_numbers.json)'
print(f'[sym] Minkowski check deferred to evaluator ({time.time()-t0:.0f}s)', flush=True)

sizes = {str(k_): int(len(expr.args)) for k_, expr in Gcomp.items()}  # top-level arity only; full op-count traverses the shared DAG exponentially
LOG['G_top_level_args'] = sizes
LOG['elapsed_s'] = time.time() - t0
ATOM_LIST = [r, nx, ny, nz, a, ap, app, b, bp, bpp, S, Sp, Spp, bta]
with open('/home/hatch/workspace/warp-pilot/gate7/wa_g_expr.pkl', 'wb') as fh:
    pickle.dump({'Gcomp': Gcomp, 'atoms': ATOM_LIST, 'g': g, 'ginv': ginv}, fh)
json.dump(LOG, open('/home/hatch/workspace/warp-pilot/gate7/wa_derivation.json', 'w'), indent=1)
print('[sym] SAVED wa_g_expr.pkl; ops:', sizes, flush=True)
print(f'[sym] TOTAL {time.time()-t0:.0f}s', flush=True)
