#!/usr/bin/env python3
"""GATE-8 / W-B / G8-2 -- SPOT CHECK v2 (dense-grid deciding version).

v1 (wb_g82_spotcheck.py) read the Einstein tensor from spline jets
over the COARSE stored snap grid (dy=0.05): the ORIGINAL vacuum
fields read NEC_min = -1.40 there -- the discretisation floor of
that grid swamps everything (phase46's own r2r3 JSON flags the
stored grid's FD floor). v1 is therefore NOT deciding and is
superseded by this script.

v2: regenerate the P29-3 GN lift DENSELY (dy=0.0025, RK4, z-grid
N=161 sinh) using MY OWN sympy-derived Einstein jet functions
(wb_g82_spotcheck.py derivation, re-derived here) for the dk solve
-- the shared DEFINITION (the P29-3 lift) regenerated, as Gate-6
W-C was allowed to do; the deciding machinery (this evolution +
audit) is fresh. Then audit on the dense grid with np.gradient
jets:
  (a) original fields on the slab y in [0,0.30]  -> audit floor;
  (b) floored-D fields D' = sqrt(D^2+0.60^2) on the same slab
      (phase46's R3 ansatz) -> NEC_min.
Question: is (b)'s NEC violation ~1e6 x the floor, as phase46
found (-0.278 vs -1.5e-5), or was that phase-specific?
float64.
"""
import json
import numpy as np
import sympy as sp

OUT = "/home/hatch/workspace/warp-pilot/gate8/results/wb_g82_spotcheck2.json"
K5SQ = np.sqrt(48.0 * np.pi)
LAM5 = -K5SQ ** 2 / 6.0
K4 = 8.0 * np.pi

# ---------------- sympy derivation (fresh, as in v1) ----------------
z, y, th = sp.symbols('z y th')
A = sp.Function('A')(z, y); D = sp.Function('D')(z, y); C = sp.Function('C')(z, y)
coords = [sp.Symbol('t'), z, th, sp.Symbol('ph'), y]
g = sp.diag(-A**2, D**2, C**2, C**2 * sp.sin(th)**2, 1)
ginv = g.inv()
dg = [g.diff(c) for c in coords]
Gam = {}
for a in range(5):
    for b_ in range(5):
        for c_ in range(5):
            e = sum(ginv[a, dd] * (dg[b_][dd, c_] + dg[c_][dd, b_] - dg[dd][b_, c_])
                    for dd in range(5)) / 2
            e = sp.simplify(e)
            if e != 0:
                Gam[(a, b_, c_)] = e
Ric = {}
for b_ in range(5):
    for dd_ in range(5):
        e = 0
        for a in range(5):
            if (a, b_, dd_) in Gam:
                e += Gam[(a, b_, dd_)].diff(coords[a])
            if (a, dd_, a) in Gam:
                e -= Gam[(a, dd_, a)].diff(coords[dd_])
            for ee in range(5):
                if (a, a, ee) in Gam and (ee, b_, dd_) in Gam:
                    e += Gam[(a, a, ee)] * Gam[(ee, b_, dd_)]
                if (a, dd_, ee) in Gam and (ee, b_, a) in Gam:
                    e -= Gam[(a, dd_, ee)] * Gam[(ee, b_, a)]
        e = sp.simplify(e)
        if e != 0:
            Ric[(b_, dd_)] = e
Rsc = sp.simplify(sum(ginv[i, j] * Ric.get((i, j), 0) for i in range(5) for j in range(5)))
Gmix = [sp.simplify(sum(ginv[i, k] * Ric.get((k, i), 0) for k in range(5))
                    - sp.Rational(1, 2) * Rsc) for i in range(5)]
print("sympy G derived", flush=True)

jv = sp.symbols('jA jD jC jAz jDz jCz jAy jDy jCy '
                'jAzz jDzz jCzz jAyy jDyy jCyy jAzy jDzy jCzy')
(JA, JD, JC, JAz, JDz, JCz, JAy, JDy, JCy,
 JAzz, JDzz, JCzz, JAyy, JDyy, JCyy, JAzy, JDzy, JCzy) = jv


def jet_subs(expr):
    subs = {}
    for F, jF, jFz, jFy, jFzz, jFyy, jFzy in [
            (A, JA, JAz, JAy, JAzz, JAyy, JAzy),
            (D, JD, JDz, JDy, JDzz, JDyy, JDzy),
            (C, JC, JCz, JCy, JCzz, JCyy, JCzy)]:
        subs[F] = jF
        subs[sp.Derivative(F, z)] = jFz
        subs[sp.Derivative(F, y)] = jFy
        subs[sp.Derivative(F, (z, 2))] = jFzz
        subs[sp.Derivative(F, (y, 2))] = jFyy
        subs[sp.Derivative(F, z, y)] = jFzy
    return sp.simplify(expr.subs(subs).subs(th, sp.pi / 2))


Gf = [sp.lambdify(jv, jet_subs(Gmix[i]), 'numpy') for i in range(5)]
print("lambdified", flush=True)

# ---------------- dense evolution of the lift ----------------
N = 161
wmax = np.arcsinh(31.6 / 0.5)
w = np.linspace(-wmax, wmax, N)
zz = 0.5 * np.sinh(w)
dy = 0.0025
YC = 0.30


def grad(f):
    return np.gradient(f, zz, edge_order=2)


def jets_from_state(st, dk):
    """st: dict A,D,C,kt,kz,kth (arrays over z); dk: (3,N) trial."""
    argsF = {}
    for nm, knm in (('A', 'kt'), ('D', 'kz'), ('C', 'kth')):
        F = st[nm]; k = st[knm]
        Fy = F * k
        argsF[nm] = (F, grad(F), Fy, grad(grad(F)), None, grad(Fy))
    # Fyy needs dk per field
    dmap = {'A': dk[0], 'D': dk[1], 'C': dk[2]}
    out = []
    for nm in ('A', 'D', 'C'):
        F, Fz, Fy, Fzz, _, Fzy = argsF[nm]
        Fyy = F * (dmap[nm] + (st[{'A': 'kt', 'D': 'kz', 'C': 'kth'}[nm]]) ** 2)
        out.append((F, Fz, Fy, Fzz, Fyy, Fzy))
    (A_, D_, C_) = out
    return [A_[0], D_[0], C_[0], A_[1], D_[1], C_[1], A_[2], D_[2], C_[2],
            A_[3], D_[3], C_[3], A_[4], D_[4], C_[4], A_[5], D_[5], C_[5]]


def solve_dk(st):
    zero = np.zeros((3, N))
    args0 = jets_from_state(st, zero)
    F0 = [np.asarray(Gf[i](*args0), dtype=np.float64) for i in (0, 1, 2)]
    cols = []
    for which in range(3):
        dk = np.zeros((3, N)); dk[which] = 1.0
        argsw = jets_from_state(st, dk)
        Fw = [np.asarray(Gf[i](*argsw), dtype=np.float64) for i in (0, 1, 2)]
        cols.append([Fw[i] - F0[i] for i in range(3)])
    dk_out = np.zeros((3, N))
    rhs_ = np.array([-LAM5 - F0[i] for i in range(3)])
    for p in range(N):
        Mp = np.array([[cols[j][i][p] for j in range(3)] for i in range(3)])
        dk_out[:, p] = np.linalg.solve(Mp, rhs_[:, p])
    return dk_out


def rhs_state(st):
    dk = solve_dk(st)
    return {'A': st['A'] * st['kt'], 'D': st['D'] * st['kz'],
            'C': st['C'] * st['kth'],
            'kt': dk[0], 'kz': dk[1], 'kth': dk[2]}


def rk4_step(st, h):
    k1 = rhs_state(st)
    s2 = {k: st[k] + 0.5 * h * k1[k] for k in st}
    k2 = rhs_state(s2)
    s3 = {k: st[k] + 0.5 * h * k2[k] for k in st}
    k3 = rhs_state(s3)
    s4 = {k: st[k] + h * k3[k] for k in st}
    k4 = rhs_state(s4)
    return {k: st[k] + h * (k1[k] + 2 * k2[k] + 2 * k3[k] + k4[k]) / 6.0
            for k in st}


def initial_state():
    x = 1.0 + zz ** 2
    K5 = 6.0 * K4
    trG = -x ** -2.5
    aa, bb, cc = K5 / 6.0, -K4, -trG
    rho = (-bb - np.sqrt(bb * bb - 4 * aa * cc)) / (2 * aa)
    Br = 1.0 / np.sqrt(1.0 - x ** -0.5)
    D0 = np.where(np.abs(zz) > 1e-9, 2.0 * np.abs(zz) * Br, 2.0 * np.sqrt(2.0))
    return {'A': np.ones_like(zz), 'D': D0, 'C': x.copy(),
            'kt': -(K5SQ / 6.0) * (1.0 - 2.0 * rho),
            'kz': -(K5SQ / 6.0) * (rho + 1.0),
            'kth': -(K5SQ / 6.0) * (rho + 1.0)}


st = initial_state()
store = {k: [st[k].copy()] for k in ('A', 'D', 'C')}
nsteps = int(round(YC / dy))
for i in range(nsteps):
    st = rk4_step(st, dy)
    for k in store:
        store[k].append(st[k].copy())
    if (i + 1) % 40 == 0:
        print("evolved to y =", (i + 1) * dy, flush=True)
ys = np.linspace(0.0, YC, nsteps + 1)
F = {k: np.array(v) for k, v in store.items()}
i0 = int(np.argmin(np.abs(zz)))
gate = {"D_throat_y0": float(F['D'][0, i0]),
        "D_throat_at_yc_mine": float(F['D'][-1, i0]),
        "D_throat_at_yc_record": 1.1966801030556715,
        "A_throat_at_yc_mine": float(F['A'][-1, i0]),
        "A_throat_at_yc_record": 0.6593648485051706}
print("EVOLUTION GATE", gate, flush=True)

# ---------------- dense-grid audit ----------------
def audit(Ag, Dg, Cg, label):
    ny = len(ys)
    jets = {}
    for nm, arr in (('A', Ag), ('D', Dg), ('C', Cg)):
        Fz = np.gradient(arr, zz, axis=1, edge_order=2)
        Fy = np.gradient(arr, ys, axis=0, edge_order=2)
        jets[nm] = (arr, Fz, Fy,
                    np.gradient(Fz, zz, axis=1, edge_order=2),
                    np.gradient(Fy, ys, axis=0, edge_order=2),
                    np.gradient(Fy, zz, axis=1, edge_order=2))
    A_, D_, C_ = jets['A'], jets['D'], jets['C']
    args = [A_[0], D_[0], C_[0], A_[1], D_[1], C_[1], A_[2], D_[2], C_[2],
            A_[3], D_[3], C_[3], A_[4], D_[4], C_[4], A_[5], D_[5], C_[5]]
    G = [np.asarray(Gf[i](*args), dtype=np.float64) for i in range(5)]
    T = [(G[i] + LAM5) / K5SQ for i in range(5)]
    rho = -T[0]; pz = T[1]; pth = T[2]; py = T[4]
    mask = np.abs(zz) <= 3.0
    # exclude the outermost y row (one-sided gradient) for the floor read
    sl = (slice(0, ny - 1), mask)
    res = {"label": label,
           "rho_min": float(np.min(rho[sl])),
           "NEC_min": float(min(np.min((rho + pz)[sl]),
                                np.min((rho + pth)[sl]),
                                np.min((rho + py)[sl]))),
           "max_abs_T": float(max(np.max(np.abs(t[sl])) for t in T))}
    print(label, res, flush=True)
    return res


out = {"evolution_gate": gate}
out["original_fields_slab_dense"] = audit(F['A'], F['D'], F['C'], "original-dense")
Df = np.sqrt(F['D'] ** 2 + 0.60 ** 2)
out["floored_D_slab_dense"] = audit(F['A'], Df, F['C'], "floored-D-dense")
json.dump(out, open(OUT, "w"), indent=1)
print("DONE", flush=True)
