"""GATE-12 brute-force check of the xi-double-dot coefficient C.

Fully independent construction: moving spherical shell R(t) = R0 +
(1/2) alpha_t t^2 in BULK COORDINATE time t, surface field
Phi(Y) = |Y| - R(t) in Cartesian coordinates; unit normal field from
grad Phi; Christoffels from FD metric derivatives (gate12 g12_le
tools); K(u,u) = u^mu u^nu nabla_mu n_nu at the shell point
(0, R0, 0, 0) at t = 0, where u = (1/sqrt(A), 0,0,0).
Predictions (interior, A = 1.6246..., sqrt(B) = 1.00099913...):
  slope wrt alpha_t = sqrt(B)/A = 0.616174  <=>  C_proper = sqrt(B)
  slope wrt alpha_t = sqrt(B)/A^2 = 0.379   <=>  C_proper = sqrt(B)/A (phase)
Also prints the static K(u,u) (should be -A'/(2A sqrt(B))).
"""
import numpy as np
import g12_le as G

A_STORED = 0.27773424114865775
P_EXP = 0.1
BETA_MK = None
import json
bg = json.load(open("/home/hatch/workspace/warp-pilot/phase80/results/p802_shell.json"))["background_shell_datum_from_P61_1"]
BETA_MK = float(bg["beta_MK"]); K_MK = float(bg["k"]); GAM = 1e-28
R0 = 1000.0

def Afun_in(x):
    return float(np.exp(2 * A_STORED * np.log(x) / (1 + np.log(x))))
def Bfun_in(x):
    return 1.0 / (1.0 - x ** (P_EXP - 1.0))
def Afun_ex(x):
    return 1 - 3 * BETA_MK * GAM - BETA_MK * (2 - 3 * BETA_MK * GAM) / x + GAM * x - K_MK * x ** 2
def Bfun_ex(x):
    return 1.0 / Afun_ex(x)

def metric4(Af, Bf):
    def mf(Y):
        Y = np.asarray(Y, float)
        rr = np.sqrt(Y[1] ** 2 + Y[2] ** 2 + Y[3] ** 2)
        A = Af(rr); B = Bf(rr)
        # ds2 = -A dt2 + dr2-ish: g = diag(-A, B xhat xhat + (delta - xhat xhat))
        xh = Y[1:] / rr
        g = np.zeros((4, 4))
        g[0, 0] = -A
        g[1:, 1:] = np.eye(3) + (B - 1.0) * np.outer(xh, xh)
        return g
    return mf

def Kuu(Af, Bf, alpha_t, h=0.05):
    mf = metric4(Af, Bf)
    def Rof(t):
        return R0 + 0.5 * alpha_t * t * t
    def nfield(Y):
        Y = np.asarray(Y, float)
        def Phi(Z):
            return np.sqrt(Z[1] ** 2 + Z[2] ** 2 + Z[3] ** 2) - Rof(Z[0])
        dPhi = G.fd_jac(lambda Z: np.array([Phi(Z)]), Y, 1e-6)[0]
        gi = np.linalg.inv(mf(Y))
        return dPhi / np.sqrt(float(dPhi @ gi @ dPhi))
    X = np.array([0.0, R0, 0.0, 0.0])
    n_low = nfield(X)
    g = mf(X)
    dn = G.fd_jac(nfield, X, h, 2)
    Gam = G.christoffel(mf, X, h, 2)
    gradn = dn.T - np.einsum("lmn,l->mn", Gam, n_low)
    A0 = Af(R0)
    u = np.array([1.0 / np.sqrt(A0), 0.0, 0.0, 0.0])
    return float(u @ gradn @ u), float(n_low @ np.array([0.0, 1.0, 0.0, 0.0]))

for name, Af, Bf in [("in", Afun_in, Bfun_in), ("ex", Afun_ex, Bfun_ex)]:
    k0, _ = Kuu(Af, Bf, 0.0)
    ka, _ = Kuu(Af, Bf, 1e-3)
    kb, _ = Kuu(Af, Bf, 2e-3)
    slope = (ka - k0) / 1e-3
    slope2 = (kb - k0) / 2e-3
    print(f"   linearity: slope(1e-3)={slope:+.6f} slope(2e-3)={slope2:+.6f}")
    A0 = Af(R0); sB = np.sqrt(Bf(R0))
    print(f"{name}: Kuu(0)={k0:+.6e}  slope wrt alpha_t = {slope:+.6f}")
    print(f"   predictions: sqrt(B)/A = {sB/A0:.6f} (C_proper = sqrt(B)); "
          f"sqrt(B)/A^2 = {sB/A0**2:.6f} (C_proper = sqrt(B)/A, phase); "
          f"Ktt static formula A'/(2A sqrtB) sign check: -Kuu(0) should be +")
    hh = 1.0
    Apr = (Af(R0 + hh) - Af(R0 - hh)) / (2 * hh)
    print(f"   -Kuu(0) = {-k0:+.6e} vs A'/(2A sqrt(B)) = {Apr/(2*A0*sB):+.6e}")
