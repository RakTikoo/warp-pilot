"""
wc_recon.py — W-C (Gate-7, G7-3) reconstruction of Procaccia's continuum
warp shell. This is the SHARED DEFINITION permitted by GATE7.md: the
closed-form geometry of the certificates paper §2/§3 as transcribed by
Phase-50's p501_recon.py (read as text and re-implemented here in fresh
Gate-7 code; no Phase-50 or archive code is executed or imported).
  * step density, 4x box convolution W = 3.6328174 m (Pfun below),
    R1 = 10.0000162, R2 = 19.9997787, rho0 = 9/(14000 pi), zero radial
    pressure (a' = m/(r(r-2m)), B = (1-2m/r)^-1);
  * spline-modulated shift source: 12 cubic B-spline coefficients
    (knots [3,3,3, linspace(3,27,10), 27,27,27], constant extension),
    g0 = rhohat^q tanh((r_m-r)/w) exp(sum a_i B_i), w = 0.05,
    balance lambda from the r_m split, flux F, shift S = 1 - k * int F/r^2.
Design vector: the hashed .npy DATA file only (np.load of data, no code).
float64 everywhere. Python: programme venv (numpy 2.5.5 / scipy 1.18.1).
"""
import hashlib
from math import comb
import numpy as np
from scipy.interpolate import BSpline, CubicSpline
from scipy.integrate import cumulative_trapezoid

DTYPE = np.float64
PUBLISHED_SHA256 = "a8814dfb6273956da9656379a8dd887218ecc28cbafb03fc87f980c07510d74a"
DESIGN_PATHS = [
    "/home/hatch/workspace/warp-pilot/phase50/procaccia/cont/continuum_cert_code/x_slp2.npy",
    "/home/hatch/workspace/warp-pilot/phase50/procaccia/opt/optimal_shift_code/results/x_slp2.npy",
    "/home/hatch/workspace/warp-pilot/phase50/procaccia/opt/optimal_shift_code/results/slp2.npy",
]

DR = DTYPE("5.07447603241606e-4")
R1 = DTYPE(19706.5) * DR
R2 = DTYPE(39412.5) * DR
W = DTYPE(7159.0) * DR
RHO0 = DTYPE(9.0) / (DTYPE(14000.0) * np.pi)
R_IN = R1 - 2.0 * W
R_OUT = R2 + 2.0 * W
W_SWITCH = DTYPE(0.05)

# Paper §3 printed targets (fidelity spot check)
PAPER = {
    "M": 6.11288573784887775,
    "a_Rin": -0.58471095644715724,
    "lambda": 0.27839575423,
    "k": 0.0302774968097,
    "int_F_over_r2": 33.0278294235,
    "rho_max": 2.0204755e-4,
}


def hash_gate():
    out = {}
    for p in DESIGN_PATHS:
        raw = open(p, "rb").read()
        out[p] = hashlib.sha256(raw).hexdigest()
    return out


def load_design_vector(path):
    x = np.load(path).astype(DTYPE)
    assert x.shape == (14,), x.shape
    return x


def Pfun(x):
    u = np.asarray(x, dtype=DTYPE) / W
    out = np.zeros_like(u)
    for j in range(5):
        t = u + 2.0 - j
        out += ((-1.0) ** j) * comb(4, j) * np.where(t > 0, t, 0.0) ** 4
    return out / 24.0


def rho_of_r(r):
    r = np.asarray(r, dtype=DTYPE)
    return RHO0 * (Pfun(r - R1) - Pfun(r - R2))


class ProcacciaShellWC:
    def __init__(self, xvec, dr=DTYPE(2.5e-4), rmax=DTYPE(30.0)):
        self.x = xvec
        self.a_i = xvec[:12]
        self.q = DTYPE(xvec[12])
        self.r_m = DTYPE(xvec[13])
        r = np.arange(0.0, float(rmax) + 1e-12, float(dr), dtype=DTYPE)
        r = np.unique(np.sort(np.r_[r, self.r_m, R_IN, R_OUT]))
        self.rg = r
        rho = np.maximum(rho_of_r(r), 0.0)
        self.rho_max = float(rho.max())
        m = cumulative_trapezoid(4.0 * np.pi * r ** 2 * rho, r, initial=0.0)
        self.M = float(m[-1])
        self._m = CubicSpline(r, m)
        with np.errstate(divide="ignore", invalid="ignore"):
            ap = np.where(r > 0, m / (r * (r - 2.0 * m)), 0.0)
        ap = np.where(np.isfinite(ap), ap, 0.0)
        a_out = np.where(r > 2.0 * self.M,
                         0.5 * np.log(1.0 - 2.0 * self.M / np.maximum(r, 1e-300)), 0.0)
        i_out = int(np.searchsorted(r, R_OUT))
        a = np.empty_like(r)
        seg = cumulative_trapezoid(ap[:i_out + 1][::-1], r[:i_out + 1][::-1],
                                   initial=0.0)[::-1]
        a[:i_out + 1] = a_out[i_out] + seg
        a[i_out + 1:] = a_out[i_out + 1:]
        self.a_Rin = float(a[0])
        self._a = CubicSpline(r, a)
        nb = 12
        knots = np.r_[[3.0] * 3, np.linspace(3.0, 27.0, nb - 2), [27.0] * 3]
        self.knots = knots
        Bv = np.array([BSpline(knots, np.eye(nb)[i], 3, extrapolate=False)(
            np.clip(r, 3.0, 27.0)) for i in range(nb)])
        Bv = np.nan_to_num(Bv)
        mod = np.exp(self.a_i @ Bv)
        rhohat = rho / self.rho_max
        g0 = (rhohat ** self.q) * np.tanh((self.r_m - r) / W_SWITCH) * mod
        u = g0 * r ** 2
        i_m = int(np.searchsorted(r, self.r_m))
        I_in = float(np.trapezoid(u[:i_m + 1], r[:i_m + 1]))
        I_out = float(np.trapezoid(u[i_m:], r[i_m:]))
        self.lam = -I_in / I_out
        g = np.where(r < self.r_m, g0, self.lam * g0)
        Fcum = cumulative_trapezoid(g * r ** 2, r, initial=0.0)
        F = np.where(r <= self.r_m, Fcum, Fcum - Fcum[-1])
        with np.errstate(divide="ignore", invalid="ignore"):
            Fr2 = np.where(r > 0, F / r ** 2, 0.0)
        I = cumulative_trapezoid(Fr2, r, initial=0.0)
        self.int_Fr2 = float(I[-1])
        self.k = 1.0 / self.int_Fr2
        S = 1.0 - self.k * I
        S = np.where(r >= R_OUT, 0.0, S)
        S = np.where(r <= R_IN, 1.0, S)
        self._S = CubicSpline(r, S)

    def m_of(self, r):
        r = np.asarray(r, dtype=DTYPE)
        return np.where(r <= 0, 0.0, self._m(np.clip(r, 0, None)))

    def a_of(self, r):
        return self._a(np.asarray(r, dtype=DTYPE))

    def B_of(self, r):
        r = np.asarray(r, dtype=DTYPE)
        m = self.m_of(r)
        with np.errstate(divide="ignore", invalid="ignore"):
            B = np.where(r > 0, 1.0 / (1.0 - 2.0 * m / np.maximum(r, 1e-300)), 1.0)
        return B

    def S_of(self, r):
        return self._S(np.asarray(r, dtype=DTYPE))

    def metric_factory(self, beta):
        beta = DTYPE(beta)

        def gfunc(pts):
            pts = np.asarray(pts, dtype=DTYPE)
            P = pts.shape[0]
            r = np.linalg.norm(pts, axis=1)
            E = np.exp(2.0 * self.a_of(r))
            B = self.B_of(r)
            S = self.S_of(r)
            g = np.zeros((P, 4, 4), dtype=DTYPE)
            g[:, 0, 0] = -E
            g[:, 0, 1] = g[:, 1, 0] = -beta * S
            gam = np.tile(np.eye(3, dtype=DTYPE), (P, 1, 1))
            safe = r > 1e-12
            if np.any(safe):
                x = pts[safe]
                rr = r[safe]
                n = x / rr[:, None]
                gam[safe] += (B[safe] - 1.0)[:, None, None] * n[:, :, None] * n[:, None, :]
            g[:, 1:, 1:] = gam
            return g

        return gfunc

    def fidelity(self):
        mine = {"M": self.M, "a_Rin": self.a_Rin, "lambda": float(self.lam),
                "k": float(self.k), "int_F_over_r2": self.int_Fr2,
                "rho_max": self.rho_max}
        out = {}
        for key, target in PAPER.items():
            v = mine[key]
            out[key] = {"mine": float(v), "paper": float(target),
                        "rel_err": float(abs(v - target) / abs(target))}
        out["q"] = {"mine": float(self.q), "paper": 1.47838}
        out["r_m"] = {"mine": float(self.r_m), "paper": 16.79963}
        out["R_in"] = float(R_IN)
        out["R_out"] = float(R_OUT)
        return out
