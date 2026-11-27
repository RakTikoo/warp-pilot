"""
p408_pool_p408_lib16.py — POOL COPY of phase408/work/p392_lib16.py (VM sys.path entries replaced by dual home/pool paths, exactly as p391_pool_p391_lib12.py relates to p391_lib12.py; numerics unchanged).
Original header: p392_lib16.py — Phase 392: 16-mode generalisation of phase391/work/p391_lib12.py.
Only the grading basis changes (N_GRADING=16, knots [R1,R1,R1, linspace(R1,R2,14), R2,R2,R2],
y in R^30: c in R^16, a in R^12, q, r_m); every other numerical path is identical to p391_lib12.py.
Python: programme venv ~/workspace/warp-pilot/venv/bin/python
(numpy 2.5.5 / scipy 1.18.1), float64 everywhere.

Implements the registered graded family of CHECKPOINT386.md
§"THE GRADED FAMILY" exactly:

  * fixed (R1, R2, W, M_target) from phase50/p501_recon.py;
  * plateau phi(r) = exp(sum_j c_j B_j(r)), 8 cubic B-splines on knots
    [R1,R1,R1, linspace(R1,R2,6), R2,R2,R2];
  * rho = rho0 * Box4_W[phi * 1_{[R1,R2]}], Box4_W = four successive
    sliding box averages of width W (centred windows), built on the
    registered construction grid (dr = 2.5e-5 on [0, R_out + 2.75],
    with R1, R2, the grading knots and their +- {W/2, W, 3W/2, 2W}
    shifts inserted); rho carried as a CubicSpline on that grid;
  * rho0 set so the grid-integrated mass equals M_target, by the
    GenProcaccia convention (cumulative-trapezoid mass of the
    unscaled shape on the builder grid, rho0 = M_target / that);
  * background (m, a) and source chain (g, lambda, F, k, S) and
    metric_factory(beta) EXACTLY as p2513_lib.GenProcaccia does them
    (code paths copied, only the density construction substituted).

Construction of the box averages (numerical scheme):
  stage 1 acts on the discontinuous phi*1_{[R1,R2]}: phi is carried
  as a CubicSpline on the construction-grid points inside [R1, R2]
  and its spline antiderivative is used, so the jump at R1/R2 is
  represented exactly (no smearing across the edge);
  stages 2-4 act on continuous profiles: the antiderivative is the
  cumulative-trapezoid integral on the construction grid, evaluated
  at shifted points by cubic Hermite interpolation (values + the
  profile itself as derivative).  At c = 0 this reproduces the
  analytic Pfun step response to ~5e-12 absolute (prototype check,
  phase386 worker A) — far inside the C-G1 bar of 1e-5 relative.
"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline, BSpline
from scipy.integrate import cumulative_trapezoid

for _p in ('/home/hatch/workspace/warp-pilot', '/home/spark/work/p386/warp-pilot'):
    sys.path.insert(0, _p)
for _p in ('/home/hatch/workspace/warp-pilot/phase50', '/home/spark/work/p386/warp-pilot/phase50'):
    sys.path.insert(0, _p)
for _p in ('/home/hatch/workspace/warp-pilot/phase251/work', '/home/spark/work/p386/warp-pilot/phase251/work'):
    sys.path.insert(0, _p)
import p501_recon as REC
import p2513_lib as H

DTYPE = np.float64
M_TARGET = float(H.M_TARGET)          # 6.11288573784887775
R1 = float(REC.R1)                    # 10.0000162
R2 = float(REC.R2)                    # 19.9997787
W = float(REC.W)                      # 3.6328174
R_IN = float(REC.R_IN)                # 2.734381
R_OUT = float(REC.R_OUT)              # 27.265413
W_SWITCH = float(REC.W_SWITCH)        # 0.05
INSET_LO = float(H.INSET_LO)
INSET_HI = float(H.INSET_HI)
DR_CONSTR = DTYPE(2.5e-5)

N_GRADING = 16
GRADING_KNOTS_INNER = np.linspace(R1, R2, 14, dtype=DTYPE)
GRADING_KNOTS = np.r_[[R1] * 3, GRADING_KNOTS_INNER, [R2] * 3].astype(DTYPE)


def construction_grid():
    """Registered construction grid: dr = 2.5e-5 on [0, R_out + 2.75]
    with R1, R2, the grading knots and their +- {W/2, W, 3W/2, 2W}
    shifts inserted."""
    rmax = R_OUT + 2.75
    r = np.arange(0.0, rmax + 1e-12, float(DR_CONSTR), dtype=DTYPE)
    ins = [R1, R2]
    for k in GRADING_KNOTS_INNER:
        ins.append(float(k))
        for s in (0.5 * W, W, 1.5 * W, 2.0 * W):
            ins.append(float(k) - s)
            ins.append(float(k) + s)
    r = np.unique(np.sort(np.r_[r, np.asarray(ins, dtype=DTYPE)]))
    return r[(r >= 0.0) & (r <= rmax)]


def _eval_integral(g, I, v, x):
    """Evaluate the antiderivative (node values I, derivative v) at x
    by cubic Hermite interpolation on each grid interval."""
    xc = np.clip(x, g[0], g[-1])
    idx = np.searchsorted(g, xc) - 1
    idx = np.clip(idx, 0, len(g) - 2)
    h = g[idx + 1] - g[idx]
    t = (xc - g[idx]) / h
    t2 = t * t
    t3 = t2 * t
    return ((2.0 * t3 - 3.0 * t2 + 1.0) * I[idx]
            + (t3 - 2.0 * t2 + t) * (v[idx] * h)
            + (-2.0 * t3 + 3.0 * t2) * I[idx + 1]
            + (t3 - t2) * (v[idx + 1] * h))


def _box_avg(g, v):
    """One centred sliding box average of width W on grid g."""
    I = np.zeros_like(g)
    I[1:] = np.cumsum(0.5 * (v[1:] + v[:-1]) * np.diff(g))
    return (_eval_integral(g, I, v, g + 0.5 * W)
            - _eval_integral(g, I, v, g - 0.5 * W)) / W


def box4_shape(cvec):
    """Unscaled Box4_W[phi * 1_{[R1,R2]}] on the construction grid.
    Returns (grid, shape_values, phi_on_plateau_grid)."""
    cvec = np.asarray(cvec, dtype=DTYPE)
    g = construction_grid()
    inside = (g >= R1) & (g <= R2)
    gs = g[inside]
    nb = len(cvec)
    Bv = np.array([BSpline(GRADING_KNOTS, np.eye(nb)[i], 3,
                           extrapolate=False)(np.clip(gs, R1, R2))
                   for i in range(nb)])
    Bv = np.nan_to_num(Bv)
    phi = np.exp(cvec @ Bv)
    # stage 1: exact antiderivative of the spline-carried plateau
    spl = CubicSpline(gs, phi)
    A = spl.antiderivative()
    A_R1 = float(A(R1))
    tot = float(A(R2)) - A_R1

    def Iphi(x):
        xc = np.clip(x, R1, R2)
        return np.where(x <= R1, 0.0,
                        np.where(x >= R2, tot, A(xc) - A_R1))

    v = (Iphi(g + 0.5 * W) - Iphi(g - 0.5 * W)) / W
    # stages 2-4: successive sliding box averages
    for _ in range(3):
        v = _box_avg(g, v)
    v = np.maximum(v, 0.0)
    v = np.where((g >= R_IN) & (g <= R_OUT), v, 0.0)
    return g, v, phi


class GradedProcaccia16:
    """Graded-density Procaccia shell, 16-mode grading. Parameter vector
    y = (c[16], a[12], q, r_m) in R^30. Background and source chain
    copied from p2513_lib.GenProcaccia with only the density
    construction substituted."""

    def __init__(self, yvec, dr=DTYPE(2.5e-4), M_target=M_TARGET):
        y = np.asarray(yvec, dtype=DTYPE)
        assert y.shape == (30,), y.shape
        self.y = y
        self.c_j = y[:16]
        self.a_i = y[16:28]
        self.q = DTYPE(y[28])
        self.r_m = DTYPE(y[29])
        self.W = DTYPE(W); self.R1 = DTYPE(R1); self.R2 = DTYPE(R2)
        self.R_in = DTYPE(R_IN); self.R_out = DTYPE(R_OUT)
        # ---- graded density on the construction grid ----
        gc, shape_c, phi = box4_shape(self.c_j)
        self.constr_grid = gc
        self.phi_plateau = phi
        self._rho_constr = CubicSpline(gc, shape_c)
        # ---- builder grid (GenProcaccia's) ----
        rmax = float(self.R_out) + 2.75
        r = np.arange(0.0, rmax + 1e-12, float(dr), dtype=DTYPE)
        r = np.unique(np.sort(np.r_[r, self.r_m, self.R_in, self.R_out]))
        self.rg = r
        shape = np.maximum(self._rho_constr(r), 0.0)
        shape = np.where((r >= self.R_in) & (r <= self.R_out), shape, 0.0)
        m_shape = cumulative_trapezoid(4.0 * np.pi * r ** 2 * shape, r,
                                       initial=0.0)
        self.M_unscaled_unit_rho0 = float(m_shape[-1])
        self.rho0 = DTYPE(M_target) / DTYPE(self.M_unscaled_unit_rho0)
        self.rescale_factor = float(self.rho0 / float(REC.RHO0))
        rho = self.rho0 * shape
        self.rho_max = float(rho.max())
        m = cumulative_trapezoid(4.0 * np.pi * r ** 2 * rho, r, initial=0.0)
        self.M = float(m[-1])
        self._m = CubicSpline(r, m)
        with np.errstate(divide='ignore', invalid='ignore'):
            ap = np.where(r > 0, m / (r * (r - 2.0 * m)), 0.0)
        ap = np.where(np.isfinite(ap), ap, 0.0)
        self._ap = CubicSpline(r, ap)
        a_out = np.where(r > 2.0 * self.M,
                         0.5 * np.log(1.0 - 2.0 * self.M / np.maximum(r, 1e-300)), 0.0)
        i_out = int(np.searchsorted(r, self.R_out))
        a = np.empty_like(r)
        seg = cumulative_trapezoid(ap[:i_out + 1][::-1], r[:i_out + 1][::-1],
                                   initial=0.0)[::-1]
        a[:i_out + 1] = a_out[i_out] + seg
        a[i_out + 1:] = a_out[i_out + 1:]
        self.a_Rin = float(a[0])
        self._a = CubicSpline(r, a)
        klo = float(self.R_in) + INSET_LO
        khi = float(self.R_out) - INSET_HI
        self.knot_lo, self.knot_hi = klo, khi
        nb = 12
        knots = np.r_[[klo] * 3, np.linspace(klo, khi, nb - 2), [khi] * 3]
        self.knots = knots
        Bv = np.array([BSpline(knots, np.eye(nb)[i], 3, extrapolate=False)(
            np.clip(r, klo, khi)) for i in range(nb)])
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
        with np.errstate(divide='ignore', invalid='ignore'):
            Fr2 = np.where(r > 0, F / r ** 2, 0.0)
        I = cumulative_trapezoid(Fr2, r, initial=0.0)
        self.int_Fr2 = float(I[-1])
        self.k = 1.0 / self.int_Fr2
        S = 1.0 - self.k * I
        S = np.where(r >= self.R_out, 0.0, S)
        S = np.where(r <= self.R_in, 1.0, S)
        self._S = CubicSpline(r, S)
        self._rho_arr = rho
        self._rho = CubicSpline(r, rho)

    # ---- profile accessors (C-G4 exact spherical read) ----
    def rho_of(self, r):
        r = np.asarray(r, dtype=DTYPE)
        return np.where((r >= self.R_in) & (r <= self.R_out),
                        np.maximum(self._rho(np.clip(r, 0.0, None)), 0.0), 0.0)

    def ap_of(self, r):
        return self._ap(np.asarray(r, dtype=DTYPE))

    def exact_static_T(self, r):
        """beta=0 exact spherical read: (rho, 0, r*rho*a'/2)."""
        r = np.asarray(r, dtype=DTYPE)
        rho = self.rho_of(r)
        pt = r * rho * self.ap_of(r) / 2.0
        return rho, np.zeros_like(rho), pt

    def chain_reads(self):
        return {'M': self.M, 'rho0': float(self.rho0),
                'rescale_factor_vs_his_rho0': self.rescale_factor,
                'rho_max': self.rho_max, 'lambda': float(self.lam),
                'k': float(self.k), 'int_F_over_r2': self.int_Fr2,
                'a_Rin': self.a_Rin, 'q': float(self.q), 'r_m': float(self.r_m),
                'R_in': float(self.R_in), 'R_out': float(self.R_out),
                'knot_lo': self.knot_lo, 'knot_hi': self.knot_hi,
                'grading': {
                    'c': [float(v) for v in self.c_j],
                    'grading_knots': [float(v) for v in GRADING_KNOTS],
                    'grading_knots_inner': [float(v) for v in GRADING_KNOTS_INNER],
                    'phi_min_plateau': float(np.min(self.phi_plateau)),
                    'phi_max_plateau': float(np.max(self.phi_plateau)),
                    'M_unscaled_unit_rho0': self.M_unscaled_unit_rho0,
                    'construction_grid_n': int(len(self.constr_grid)),
                    'construction_grid_dr': float(DR_CONSTR)}}

    def metric_factory(self, beta):
        beta = DTYPE(beta)
        a_s, m_s, S_s = self._a, self._m, self._S
        rmax = float(self.rg[-1])

        def gfunc(pts):
            pts = np.asarray(pts, dtype=DTYPE)
            P = pts.shape[0]
            r = np.linalg.norm(pts, axis=1)
            rc = np.clip(r, 0.0, rmax)
            E = np.exp(2.0 * a_s(rc))
            mm = m_s(rc)
            with np.errstate(divide='ignore', invalid='ignore'):
                B = np.where(r > 0, 1.0 / (1.0 - 2.0 * mm / np.maximum(r, 1e-300)), 1.0)
            S = S_s(rc)
            g = np.zeros((P, 4, 4), dtype=DTYPE)
            g[:, 0, 0] = -E
            g[:, 0, 1] = g[:, 1, 0] = -beta * S
            gam = np.tile(np.eye(3, dtype=DTYPE), (P, 1, 1))
            safe = r > 1e-12
            if np.any(safe):
                xx = pts[safe]; rr = r[safe]; n = xx / rr[:, None]
                gam[safe] += (B[safe] - 1.0)[:, None, None] * n[:, :, None] * n[:, None, :]
            g[:, 1:, 1:] = gam
            return g
        return gfunc


def y_his_vector16(x_slp2):
    """His design in the 16-mode graded parametrisation: y = (0_16, x_slp2)."""
    x = np.asarray(x_slp2, dtype=DTYPE)
    assert x.shape == (14,), x.shape
    return np.r_[np.zeros(16, dtype=DTYPE), x]
