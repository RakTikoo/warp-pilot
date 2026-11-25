"""W-B2 Gate-15: full-system source extraction (primary path, mpmath 40-digit).

Sign derivation for W_l (stated): dg_rth = (C/s) n_rhat * (r n_thhat)
  = (C/s)*((r-Dmu)/s)*(D sin th/s)*r = sin(th) * H(mu),
  H(mu) := C r D (r-Dmu)/s^3.
Ansatz g_rth = sum_l W_l d_th P_l = sum_l W_l (-sin th) P_l'(mu), so
  H = -sum_l W_l P_l'  =>  W_l = -<H,(1-mu^2)P_l'>/<(1-mu^2)(P_l')^2>.
The minus sign is therefore forced by d_th P_l = -sin(th) P_l'(mu).

Raw kernels (r-derivatives by sympy differentiation of the kernel, then
mpmath quadrature of the differentiated kernel = differentiation under
the integral):
  Vraw_l^(k) = C(2l+1)/2 int d_r^k[(r-Dmu)^2/s^3] P_l dmu
  Wraw_l^(k) = -int d_r^k[H] (1-mu^2) P_l' dmu / (2l(l+1)/(2l+1))
  Kraw_l^(k) = (2l+1)/4 int d_r^k[alpha] P_l dmu,  alpha = C D^2 (1-mu^2)/s^3
  Graw_l^(k) = int d_r^k[alpha] D_l dmu / int D_l^2 dmu, D_l=(1-mu^2)P_l''
Gauge transform to RW gauge at jet level (Leibniz rules, background jets
of f and 1/f). Channels via wb2_functionals.json LK/LR/LRn + angular pair.
"""
import json
import sympy as sp
from mpmath import mp, mpf, quad

mp.dps = 40
WB = "/home/hatch/workspace/warp-pilot/gate15/work_b2/"
OUT = WB + "wb2_source.json"
func = json.load(open(WB + "wb2_functionals.json"))
LK = [mpf(x) for x in func["LK_U_U1_V"]]
LR = [mpf(x) for x in func["LR_U_U1_U2_V_V1"]]
LRn = [mpf(x) for x in func["LRn_U_U1_U2_U3_V_V1_V2"]]
Bm0 = mpf(func["background"]["Bm0"])
f0 = mpf(func["background"]["f0"]); f1 = mpf(func["background"]["f1"])
f2 = mpf(func["background"]["f2"]); f3 = mpf(func["background"]["f3"])
g0 = mpf(func["background"]["g0"]); g1 = mpf(func["background"]["g1"]); g2 = mpf(func["background"]["g2"])
beta = mpf("2.142611"); gamma = mpf("1e-28"); kpar = mpf("-2.28996e-9")
Cpar = beta * (2 - 3 * beta * gamma)
rS = mpf(1000)
f4 = -24 * Cpar / rS**5  # d^4/dr^4 of -C/r at rS (other terms vanish)
FJ = [f0, f1, f2, f3, f4]
# 1/f jets to order 4 from f jets (Leibniz on f*g=1)
GJ = [g0, g1, g2, mpf(func["background"].get("g3", "0"))]
# recompute g3, g4 directly:
GJ = [1 / f0]
for n in range(1, 5):
    # (f*g)^(n) = 0 for n>=1: sum_j binom(n,j) f^(j) g^(n-j) = 0 (f^(0)=f0 term separate)
    from math import comb
    s = sum(comb(n, j) * FJ[j] * GJ[n - j] for j in range(1, n + 1))
    GJ.append(-s / f0)
GJ = GJ[:5]

# ---------- kernels and their r-derivatives (exact monomial algebra) ----------
import sys
sys.path.insert(0, WB)
from wb2_kernels import KV, KW, KA, eval_terms
dV = [lambda rr, mu, DD, _t=t: eval_terms(_t, rr, mu, DD) for t in KV]
dW = [lambda rr, mu, DD, _t=t: eval_terms(_t, rr, mu, DD) for t in KW]
dA = [lambda rr, mu, DD, _t=t: eval_terms(_t, rr, mu, DD) for t in KA]

# ---------- Legendre polynomials (explicit, mu) ----------
def Ple(l, mu):
    if l == 0: return mpf(1)
    if l == 1: return mu
    if l == 2: return (3 * mu**2 - 1) / 2
    if l == 3: return (5 * mu**3 - 3 * mu) / 2
    if l == 4: return (35 * mu**4 - 30 * mu**2 + 3) / 8
def dPle(l, mu):
    if l == 0: return mpf(0)
    if l == 1: return mpf(1)
    if l == 2: return 3 * mu
    if l == 3: return (15 * mu**2 - 3) / 2
    if l == 4: return (140 * mu**3 - 60 * mu) / 8
def ddPle(l, mu):
    if l == 0: return mpf(0)
    if l == 1: return mpf(0)
    if l == 2: return mpf(3)
    if l == 3: return 15 * mu
    if l == 4: return (420 * mu**2 - 60) / 8
def Dl(l, mu):
    return (1 - mu**2) * ddPle(l, mu)

denG = {}
for l in range(1, 5):
    denG[l] = quad(lambda mu: Dl(l, mu)**2, [-1, 1]) if l >= 2 else mpf(0)

from math import comb, factorial

def source_jets(l, D):
    # raw derivative arrays
    Vraw = [Cpar * (2 * l + 1) / 2 * quad(lambda mu: dV[k](rS, mu, D) * Ple(l, mu), [-1, 1]) for k in range(3)]
    denW = 2 * l * (l + 1) / (2 * l + 1)
    Wraw = [-quad(lambda mu: Cpar * dW[k](rS, mu, D) * (1 - mu**2) * dPle(l, mu), [-1, 1]) / denW for k in range(4)]
    Kraw = [Cpar * (2 * l + 1) / 4 * quad(lambda mu: dA[k](rS, mu, D) * Ple(l, mu), [-1, 1]) for k in range(2)]
    if l == 1:
        Graw = [mpf(0)] * 5
    else:
        Graw = [quad(lambda mu: Cpar * dA[k](rS, mu, D) * Dl(l, mu), [-1, 1]) / denG[l] for k in range(5)]
    Uraw = []
    for kk in range(4):
        if kk <= l:
            Uraw.append(-Cpar / D**(l + 1) * (factorial(l) / factorial(l - kk)) * rS**(l - kk))
        else:
            Uraw.append(mpf(0))
    # gauge transform
    Y = [-Graw[k] / 2 for k in range(5)]              # Y^(k), k=0..4
    # S^(k) = Wraw^(k) + (r^2 Y')^(k) ; (r^2)^(0..2) = r^2, 2r, 2
    r2j = [rS**2, 2 * rS, mpf(2), mpf(0), mpf(0)]
    S = []
    for kk in range(4):
        ssum = Wraw[kk]
        for j in range(min(kk, 2) + 1):
            ssum += comb(kk, j) * r2j[j] * Y[kk - j + 1]
        S.append(ssum)
    X = []
    for kk in range(4):
        X.append(-sum(comb(kk, j) * FJ[j] * S[kk - j] for j in range(kk + 1)))
    U = [Uraw[kk] + sum(comb(kk, j) * FJ[j + 1] * X[kk - j] for j in range(kk + 1)) for kk in range(4)]
    # V^(k) = Vraw^(k) + (X*g')^(k) + 2*(X'/f)^(k), g=1/f, g'^(m)=GJ[m+1]
    V = []
    for kk in range(3):
        t1 = sum(comb(kk, j) * X[j] * GJ[kk - j + 1] for j in range(kk + 1))
        t2 = sum(comb(kk, j) * X[j + 1] * GJ[kk - j] for j in range(kk + 1))
        V.append(Vraw[kk] + t1 + 2 * t2)
    Th = []
    for kk in range(2):
        tx = 2 * X[kk] / rS
        if kk >= 1: tx -= 2 * kk * X[kk - 1] / rS**2
        if kk >= 2: tx += 2 * kk * (kk - 1) * X[kk - 2] / rS**3
        Th.append(Kraw[kk] + tx - l * (l + 1) * Y[kk])
    return dict(U=U, V=V, Th=Th, X=X, Y=Y, Vraw=Vraw, Wraw=Wraw, Kraw=Kraw, Graw=Graw, Uraw=Uraw)

def channels(j):
    U, V, Th = j["U"], j["V"], j["Th"]
    B = V[0]
    K = LK[0] * U[0] + LK[1] * U[1] + LK[2] * V[0]
    R = LR[0] * U[0] + LR[1] * U[1] + LR[2] * U[2] + LR[3] * V[0] + LR[4] * V[1]
    Rn = (LRn[0] * U[0] + LRn[1] * U[1] + LRn[2] * U[2] + LRn[3] * U[3]
          + LRn[4] * V[0] + LRn[5] * V[1] + LRn[6] * V[2])
    hth = Th[0]
    kth = Th[1] / (2 * mp.sqrt(Bm0)) - V[0] / (2 * rS * Bm0**mpf("1.5"))
    return {"B": B, "K": K, "Rt": R, "Rtn": Rn, "hth": hth, "kth": kth}

eps_list = [mpf("0.1"), mpf(1) / 30, mpf("0.01"), mpf("0.003"), mpf("0.001")]
result = {"denG": {str(k): str(v) for k, v in denG.items()}, "modes": {}}
for l in [1, 2, 3, 4]:
    result["modes"][str(l)] = {}
    for eps in eps_list:
        D = rS / eps
        j = source_jets(l, D)
        ch = channels(j)
        result["modes"][str(l)][str(eps)] = {
            "jets": {"U": [str(x) for x in j["U"]], "V": [str(x) for x in j["V"]],
                     "Th": [str(x) for x in j["Th"]]},
            "channels": {kk: str(vv) for kk, vv in ch.items()},
        }
        print("l", l, "eps", eps, {kk: mp.nstr(vv, 6) for kk, vv in ch.items()}, flush=True)
json.dump(result, open(OUT, "w"), indent=1)
print("wrote", OUT)
