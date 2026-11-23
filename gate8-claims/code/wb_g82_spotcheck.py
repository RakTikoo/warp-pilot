#!/usr/bin/env python3
"""GATE-8 / W-B / G8-2 -- SPOT CHECK (deciding, qualitative) of the
alternative completions' price: does a floored-D bulk also demand
NEC-violating bulk matter on THIS path, or was phase46's read
(-0.278 on the slab; -17.6 in its transition) phase-specific?

Method (fresh): derive the 5D Einstein tensor of
  ds^2 = -A(z,y)^2 dt^2 + D(z,y)^2 dz^2 + C(z,y)^2 (dth^2+sin^2 th dph^2)
         + dy^2
with sympy (my own derivation), substitute first/second jets, lambdify.
kappa5^2 T^a_b = G^a_b + LAM5, LAM5 = -(sqrt(48 pi))^2/6 = -8 pi
(P29-3 convention, lambda_b=1). Jets of A, D, C and all needed
derivatives come from bicubic splines over the stored fields
(shared definition) -- for the ORIGINAL fields and for the
FLOORED field D' = sqrt(D^2 + 0.60^2) (phase46's R3 ansatz),
A, C unchanged. NEC read in the bulk orthonormal frame:
rho = -T^t_t, p_i = T^i_i; NEC_min = min(rho+p_z, rho+p_th, rho+p_y)
over the slab y in [0, 0.30], |z| <= 3.
The original-fields read on the same machinery is the audit floor
for this discretisation. float64.
"""
import json
import numpy as np
import sympy as sp
from scipy.interpolate import RectBivariateSpline

NPZ = "/home/hatch/workspace/warp-pilot/phase43/results/p431_bulk_fields.npz"
OUT = "/home/hatch/workspace/warp-pilot/gate8/results/wb_g82_spotcheck.json"
K5SQ = np.sqrt(48.0 * np.pi)
LAM5 = -K5SQ ** 2 / 6.0

# ---------------- sympy derivation (fresh) ----------------
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

# ---------------- fields and jets from splines ----------------
d = np.load(NPZ)
ZZ, SY = d["zz"], d["snap_y"]


def jets_for(Aarr, Darr, Carr, ys, zs):
    spls = [RectBivariateSpline(SY, ZZ, arr, kx=3, ky=3, s=0)
            for arr in (Aarr, Darr, Carr)]
    out = []
    for s in spls:
        F = s.ev(ys, zs)
        Fz = s.ev(ys, zs, dx=0, dy=1); Fy = s.ev(ys, zs, dx=1, dy=0)
        Fzz = s.ev(ys, zs, dx=0, dy=2); Fyy = s.ev(ys, zs, dx=2, dy=0)
        Fzy = s.ev(ys, zs, dx=1, dy=1)
        out += [F, Fz, Fy, Fzz, Fyy, Fzy]
    # reorder to jv order: per field (F, Fz, Fy) then seconds grouped
    A_, D_, C_ = out[0:6], out[6:12], out[12:18]
    args = [A_[0], D_[0], C_[0], A_[1], D_[1], C_[1], A_[2], D_[2], C_[2],
            A_[3], D_[3], C_[3], A_[4], D_[4], C_[4], A_[5], D_[5], C_[5]]
    return args


def nec_read(Aarr, Darr, Carr, label):
    ys = np.linspace(0.0, 0.30, 13)
    zs = ZZ[np.abs(ZZ) <= 3.0]
    YY, ZZg = np.meshgrid(ys, zs, indexing="ij")
    args = jets_for(Aarr, Darr, Carr, YY.ravel(), ZZg.ravel())
    G = [np.asarray(Gf[i](*args), dtype=np.float64) for i in range(5)]
    T = [(G[i] + (LAM5 if i == 0 else 0.0)) / K5SQ for i in range(5)]
    # mixed Einstein eq: kappa5^2 T^a_b = G^a_b + LAM5 delta^a_b
    T = [(G[i] + LAM5) / K5SQ for i in range(5)]
    rho = -T[0]; pz = T[1]; pth = T[2]; py = T[4]
    res = {"label": label,
           "rho_min": float(np.min(rho)), "rho_max": float(np.max(rho)),
           "NEC_min": float(min(np.min(rho + pz), np.min(rho + pth),
                                np.min(rho + py))),
           "max_abs_T": float(max(np.max(np.abs(t)) for t in T))}
    print(label, res, flush=True)
    return res


out = {}
out["original_fields_slab"] = nec_read(d["A"], d["D"], d["C"], "original")
Df = np.sqrt(d["D"] ** 2 + 0.60 ** 2)
out["floored_D_slab"] = nec_read(d["A"], Df, d["C"], "floored-D f=0.60")
json.dump(out, open(OUT, "w"), indent=1)
print("DONE", flush=True)
