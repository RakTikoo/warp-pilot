"""W-B2 Gate-15: SECOND PATH for the source.
Independent implementation: float64, 200-point Gauss-Legendre quadrature in mu
(numpy), kernels written directly from the definitions (no monomial algebra,
no mpmath), radial derivatives by 9-point finite differences of the raw
coefficient functions in r (step h=2), gauge transform re-implemented
directly from the Lie formulas with FD derivatives of X, Y in r.
Channels from the same LK/LR/LRn numbers (read as data from
wb2_functionals.json, converted to float).
Output: per (l, eps) channel values -> wb2_second.json (fits done in solve).
"""
import json
import numpy as np
from math import comb, factorial

WB = "/home/hatch/workspace/warp-pilot/gate15/work_b2/"
func = json.load(open(WB + "wb2_functionals.json"))
LK = [float(x) for x in func["LK_U_U1_V"]]
LR = [float(x) for x in func["LR_U_U1_U2_V_V1"]]
LRn = [float(x) for x in func["LRn_U_U1_U2_U3_V_V1_V2"]]
Bm0 = float(func["background"]["Bm0"])
beta, gamma, kpar = 2.142611, 1e-28, -2.28996e-9
Cpar = beta * (2 - 3 * beta * gamma)
rS = 1000.0

xg, wg = np.polynomial.legendre.leggauss(200)
mu = xg

def Ple(l):
    if l == 0: return np.ones_like(mu)
    if l == 1: return mu
    if l == 2: return (3 * mu**2 - 1) / 2
    if l == 3: return (5 * mu**3 - 3 * mu) / 2
    if l == 4: return (35 * mu**4 - 30 * mu**2 + 3) / 8
def dPle(l):
    if l == 0: return np.zeros_like(mu)
    if l == 1: return np.ones_like(mu)
    if l == 2: return 3 * mu
    if l == 3: return (15 * mu**2 - 3) / 2
    if l == 4: return (140 * mu**3 - 60 * mu) / 8
def Dl(l):
    if l < 2: return np.zeros_like(mu)
    dd = {2: 3.0, 3: 15 * mu, 4: (420 * mu**2 - 60) / 8}[l]
    return (1 - mu**2) * dd

def f_bg(r): return 1 - 3 * beta * gamma - Cpar / r + gamma * r - kpar * r**2

def raw_funcs(l, r, D):
    """(Uraw, Vraw, Wraw, Kraw, Graw) at radius r (float)."""
    s = np.sqrt(r**2 - 2 * r * D * mu + D**2)
    Uraw = -Cpar * r**l / D**(l + 1) if l >= 1 else -Cpar / D - 3 * beta * gamma
    nr2 = ((r - D * mu) / s)**2
    Vraw = Cpar * (2 * l + 1) / 2 * np.sum(wg * (1 / s) * nr2 * Ple(l))
    H = Cpar * r * D * (r - D * mu) / s**3
    denW = 2 * l * (l + 1) / (2 * l + 1)
    Wraw = -np.sum(wg * H * (1 - mu**2) * dPle(l)) / denW if l >= 1 else 0.0
    alpha = Cpar * D**2 * (1 - mu**2) / s**3
    Kraw = (2 * l + 1) / 4 * np.sum(wg * alpha * Ple(l))
    if l >= 2:
        Graw = np.sum(wg * alpha * Dl(l)) / np.sum(wg * Dl(l)**2)
    else:
        Graw = 0.0
    return Uraw, Vraw, Wraw, Kraw, Graw

# 9-point FD derivative weights (uniform step), orders 1..4, from numpy Vandermonde solve
def fd_weights(order, h):
    n = 9
    offs = np.arange(-4, 5, dtype=float)
    A = np.vander(offs, n, increasing=True).T  # A[j,k] = offs^k
    b = np.zeros(n); b[order] = factorial(order)
    wts = np.linalg.solve(A, b)
    return wts / h**order

def derivs_at(func_of_r, r0, maxorder, h=2.0):
    offs = np.arange(-4, 5, dtype=float)
    vals = np.array([func_of_r(r0 + o * h) for o in offs])
    out = [vals[4]]
    for o in range(1, maxorder + 1):
        out.append(float(np.sum(fd_weights(o, h) * vals)))
    return out  # [f, f', ..., f^(maxorder)]

def jets_at(l, D):
    comp = [lambda r, i=i: raw_funcs(l, r, D)[i] for i in range(5)]
    Uraw_d = derivs_at(comp[0], rS, 3)
    Vraw_d = derivs_at(comp[1], rS, 2)
    Wraw_d = derivs_at(comp[2], rS, 3)
    Kraw_d = derivs_at(comp[3], rS, 1)
    Graw_d = derivs_at(comp[4], rS, 4)
    Y_d = [-g / 2 for g in Graw_d]                     # Y, Y', ..., Y''''
    # S(r) = Wraw + r^2 Y' ; build S values on the FD stencil from Wraw/Y' functions
    def S_of_r(r):
        _, _, w_, _, g_ = raw_funcs(l, r, D)
        # Y'(r) by FD of Graw function at r (nested, small stencil 5pt)
        hh = 1.0
        gp = (-raw_funcs(l, r + 2 * hh, D)[4] + 8 * raw_funcs(l, r + hh, D)[4]
              - 8 * raw_funcs(l, r - hh, D)[4] + raw_funcs(l, r - 2 * hh, D)[4]) / (12 * hh)
        return w_ + r**2 * (-gp / 2)
    S_d = derivs_at(S_of_r, rS, 3)
    f_d = derivs_at(f_bg, rS, 4)
    g_d = derivs_at(lambda r: 1 / f_bg(r), rS, 4)      # (1/f)^{(k)}
    X_d = []
    for kk in range(4):
        X_d.append(-sum(comb(kk, j) * f_d[j] * S_d[kk - j] for j in range(kk + 1)))
    def X_of(k): return X_d[k]
    U = [Uraw_d[kk] + sum(comb(kk, j) * f_d[j + 1] * X_d[kk - j] for j in range(kk + 1)) for kk in range(4)]
    V = []
    for kk in range(3):
        t1 = sum(comb(kk, j) * X_d[j] * g_d[kk - j + 1] for j in range(kk + 1))
        t2 = sum(comb(kk, j) * X_d[j + 1] * g_d[kk - j] for j in range(kk + 1))
        V.append(Vraw_d[kk] + t1 + 2 * t2)
    Th = []
    for kk in range(2):
        tx = 2 * X_d[kk] / rS - (2 * kk * X_d[kk - 1] / rS**2 if kk >= 1 else 0.0)
        Th.append(Kraw_d[kk] + tx - l * (l + 1) * Y_d[kk])
    return U, V, Th

def channels(U, V, Th):
    B = V[0]
    K = LK[0] * U[0] + LK[1] * U[1] + LK[2] * V[0]
    R = LR[0] * U[0] + LR[1] * U[1] + LR[2] * U[2] + LR[3] * V[0] + LR[4] * V[1]
    Rn = (LRn[0] * U[0] + LRn[1] * U[1] + LRn[2] * U[2] + LRn[3] * U[3]
          + LRn[4] * V[0] + LRn[5] * V[1] + LRn[6] * V[2])
    kth = Th[1] / (2 * np.sqrt(Bm0)) - V[0] / (2 * rS * Bm0**1.5)
    return {"B": B, "K": K, "Rt": R, "Rtn": Rn, "hth": Th[0], "kth": kth}

out = {"modes": {}}
for l in [1, 2, 3, 4]:
    out["modes"][str(l)] = {}
    for eps in [0.1, 1 / 30, 0.01, 0.003, 0.001]:
        D = rS / eps
        U, V, Th = jets_at(l, D)
        ch = channels(U, V, Th)
        out["modes"][str(l)][str(eps)] = {kk: float(vv) for kk, vv in ch.items()}
        print("SP l", l, "eps", eps, {kk: f"{vv:.6e}" for kk, vv in ch.items()}, flush=True)
json.dump(out, open(WB + "wb2_second.json", "w"), indent=1)
print("wrote wb2_second.json")
