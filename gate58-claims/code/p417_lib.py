"""
p417_lib.py — Phase 417 (THE DENSE READ) machinery. Written for this
phase; imports NOTHING from phase386/391/392/408/work or gate53/work.
Instruments: gate6/wa_auditor.py and phase50/p503_lib.audit4, the
registered pair (shared instruments of every verdict in the lineage).

Construction (shared class definition, unchanged since CHECKPOINT386
SS2): rho = rho0 * Box4_W[phi * 1_[R1,R2]], phi = exp(sum_j c_j B_j)
on an n_c-mode grading basis, Box4_W = four successive centred
sliding box averages of width W; background (m, a) and source chain
(g, lambda, F, k, S) by the GenProcaccia conventions of the (10,20)
shell class (phase50/p501_recon.py parameters); y = (c[n_c], a[12],
q, r_m).

Phase 417's numerical organisation — the "panel-Lagrange" scheme,
distinct from both predecessors:
  * Gate-53: box-4 stages 2-4 by the antiderivative of a global
    cubic spline of the stage values; stage 1 likewise.
  * The phases: cumulative-trapezoid antiderivative + cubic
    Hermite evaluation at shifted points.
  * Here: stages 2-4 on a UNIFORM construction grid (dr = 2.5e-5,
    no knot insertions). Each stage's antiderivative on the grid
    is the cumulative sum of PANEL-EXACT integrals: on each panel
    the integrand is the cubic Lagrange interpolant through the
    four nearest grid values (stencil i-1..i+2 interior; i..i+3 /
    i-3..i at the edges) and the panel integral is that cubic's
    exact integral (weights computed once per stencil geometry by
    exact polynomial integration). Shifted-point evaluation of an
    antiderivative is by 6-point Lagrange interpolation of its
    grid values. Stage 1 is treated separately (see the builder):
    phi * 1_[R1,R2] is discontinuous at R1/R2, and no stencil
    scheme may straddle the jumps — its antiderivative is built
    on the inside grid [R1, R2] alone by per-panel Gauss-Legendre
    quadrature of the exact phi (the B-spline representation
    evaluated at the GL nodes), and F1 clips its argument to
    [R1, R2]. (An earlier draft of this module applied the panel
    scheme to phi * 1_ on the uniform grid; the calibration caught
    the resulting O(h) jump-panel error — chain reads off by up
    to 7.4e-6 relative in lambda — and stage 1 was rebuilt as
    described. The calibration record is p417_calibration.json
    (superseded draft) vs the rerun.)
Downstream of the box-4 profile (builder grid, m, a, the source
chain, the metric factory) the GenProcaccia conventions are
followed as the shared class definition. float64 everywhere.
VM frame of record.
"""
import sys
import numpy as np
from scipy.interpolate import BSpline, CubicSpline
from scipy.integrate import cumulative_trapezoid

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/gate6")
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase50")
import wa_auditor as wa          # noqa: E402  (instrument, allowed)
import p503_lib as p503          # noqa: E402  (audit4 instrument, allowed)

DTYPE = np.float64

# ---- S2/S3 exact parameters (binary64, taken as exact; p501_recon) ----
DR = DTYPE("5.07447603241606e-4")
R1 = DTYPE(19706.5) * DR            # 10.0000162
R2 = DTYPE(39412.5) * DR            # 19.9997787
W = DTYPE(7159.0) * DR              # 3.6328174
RHO0_NOMINAL = DTYPE(9.0) / (DTYPE(14000.0) * np.pi)
R_IN = R1 - 2.0 * W                 # 2.734381
R_OUT = R2 + 2.0 * W                # 27.265413
W_SWITCH = DTYPE(0.05)
M_TARGET = DTYPE("6.11288573784887775")
INSET_LO = DTYPE(3.0) - R_IN        # 0.265619
INSET_HI = R_OUT - DTYPE(27.0)      # 0.265413


def grading_knots(n_c):
    return np.r_[[R1] * 3, np.linspace(R1, R2, n_c - 2), [R2] * 3].astype(DTYPE)


# =====================================================================
# Panel-Lagrange antiderivative on a uniform grid.
# For a stencil of 4 nodes at positions u[0..3] (uniform spacing h),
# the exact integral over one panel [xa, xb] (a sub-interval spanned
# by two adjacent nodes) of the cubic Lagrange interpolant through
# the stencil values:  integral = sum_j w_j * v_j.  The weights are
# computed once per geometry by exact polynomial integration.
# =====================================================================
def _lagrange_panel_weights(nodes, xa, xb):
    """Exact integral over [xa, xb] of each Lagrange basis polynomial
    for the given 4 nodes (float64, via exact polynomial algebra)."""
    nodes = np.asarray(nodes, dtype=DTYPE)
    w = np.zeros(4, dtype=DTYPE)
    for j in range(4):
        others = np.delete(nodes, j)
        # basis poly coefficients (highest degree first)
        coef = np.poly(others) / np.prod(nodes[j] - others)
        integ = np.polyint(coef)
        w[j] = np.polyval(integ, xb) - np.polyval(integ, xa)
    return w


class PanelAntiderivative:
    """Antiderivative of grid values v on a uniform grid (x0, h),
    by panel-exact cubic-Lagrange panel integrals. A(x) at arbitrary
    x by 6-point Lagrange interpolation of the grid antiderivative."""

    def __init__(self, v, x0, h):
        v = np.asarray(v, dtype=DTYPE)
        n = v.size
        self.x0 = float(x0)
        self.h = float(h)
        self.n = n
        # stencil geometries: interior panel i (between nodes i, i+1)
        # uses nodes i-1..i+2; first panel nodes 0..3; last panel
        # nodes n-4..n-1. Weights relative to panel start.
        h_ = self.h
        w_int = _lagrange_panel_weights([-h_, 0.0, h_, 2 * h_], 0.0, h_)
        w_first = _lagrange_panel_weights([0.0, h_, 2 * h_, 3 * h_], 0.0, h_)
        w_last = _lagrange_panel_weights([-3 * h_, -2 * h_, -h_, 0.0],
                                         -h_, 0.0)
        panel = np.empty(n - 1, dtype=DTYPE)
        # interior panels 1..n-3 (panel i uses stencil i-1..i+2)
        if n > 4:
            idx = np.arange(1, n - 2)
            panel[idx] = (w_int[0] * v[idx - 1] + w_int[1] * v[idx]
                          + w_int[2] * v[idx + 1] + w_int[3] * v[idx + 2])
            panel[0] = (w_first[0] * v[0] + w_first[1] * v[1]
                        + w_first[2] * v[2] + w_first[3] * v[3])
            panel[n - 2] = (w_last[0] * v[n - 4] + w_last[1] * v[n - 3]
                            + w_last[2] * v[n - 2] + w_last[3] * v[n - 1])
        A = np.empty(n, dtype=DTYPE)
        A[0] = 0.0
        A[1:] = np.cumsum(panel)
        self.A = A

    def __call__(self, x):
        x = np.asarray(x, dtype=DTYPE)
        shape = x.shape
        # clip to the grid range (the shared construction clips the
        # shifted arguments at the grid ends)
        xf = np.clip(x.ravel(), self.x0, self.x0 + (self.n - 1) * self.h)
        # 6-point Lagrange interpolation of A on the uniform grid
        t = (xf - self.x0) / self.h
        i0 = np.floor(t).astype(np.int64) - 2
        i0 = np.clip(i0, 0, self.n - 6)
        frac = t - i0  # in [2, 3) for interior stencils
        ii = i0[:, None] + np.arange(6)[None, :]      # (N, 6)
        Aval = self.A[ii]                             # (N, 6)
        num = np.ones((xf.size, 6), dtype=DTYPE)
        for j in range(6):
            for k in range(6):
                if k != j:
                    num[:, j] = num[:, j] * (frac - k) / (j - k)
        return np.sum(Aval * num, axis=1).reshape(shape)


def lagrange_eval(xgrid, values, x, nst=6):
    """Vectorised nst-point Lagrange interpolation of `values` on a
    (possibly non-uniform) grid `xgrid`, evaluated at points `x`
    (clipped to the grid range)."""
    xgrid = np.asarray(xgrid, dtype=DTYPE)
    values = np.asarray(values, dtype=DTYPE)
    x = np.clip(np.asarray(x, dtype=DTYPE), xgrid[0], xgrid[-1])
    shape = x.shape
    xf = x.ravel()
    n = xgrid.size
    i0 = np.searchsorted(xgrid, xf) - nst // 2
    i0 = np.clip(i0, 0, n - nst)
    ii = i0[:, None] + np.arange(nst)[None, :]          # (N, nst)
    nodes = xgrid[ii]                                   # (N, nst)
    vals = values[ii]                                   # (N, nst)
    num = np.ones((xf.size, nst), dtype=DTYPE)
    for j in range(nst):
        for k in range(nst):
            if k != j:
                num[:, j] = num[:, j] * (xf - nodes[:, k]) \
                    / (nodes[:, j] - nodes[:, k])
    return np.sum(vals * num, axis=1).reshape(shape)


_GL8_X, _GL8_W = np.polynomial.legendre.leggauss(8)


def _stage1_antiderivative(builder_c, knots_c, n_c, gx):
    """A1 on the inside grid gx (gx[0] = R1, gx[-1] = R2):
    A1[i] = int_{R1}^{gx[i]} phi(t) dt, by per-panel 8-point
    Gauss-Legendre quadrature of phi = exp(c . B(t)) with B the
    grading B-spline basis evaluated exactly at the GL nodes.
    A1[0] = 0. phi is C^2 on [R1, R2] (kinks at the grading knots
    only); GL-8 on panels of width <= 2.5e-5 is exact far below
    float64 relevance for this integrand."""
    lo = gx[:-1]
    hi = gx[1:]
    mid = 0.5 * (lo + hi)
    half = 0.5 * (hi - lo)
    # GL nodes for all panels at once: (P, 8)
    nodes = mid[:, None] + half[:, None] * _GL8_X[None, :]
    nf = nodes.ravel()
    Bm = np.array([BSpline(knots_c, np.eye(n_c)[j], 3,
                           extrapolate=False)(nf) for j in range(n_c)])
    Bm = np.nan_to_num(Bm)
    phi_nodes = np.exp(builder_c @ Bm).reshape(nodes.shape)
    panel = half * (phi_nodes @ _GL8_W)
    A1 = np.empty(gx.size, dtype=DTYPE)
    A1[0] = 0.0
    A1[1:] = np.cumsum(panel)
    return A1


def _box_average(pa, grid, w):
    """Centred sliding box average of width w of the profile whose
    PanelAntiderivative is pa, evaluated on grid (clipped at the
    grid ends, as in the shared construction)."""
    g0, gN = float(grid[0]), float(grid[-1])
    return (pa(np.clip(grid + w / 2, g0, gN))
            - pa(np.clip(grid - w / 2, g0, gN))) / w


class GradedBuilder:
    """rho = rho0 * Box4_W[phi * 1_[R1,R2]], phi = exp(sum_j c_j B_j)
    on an n_c-mode grading basis; background (m, a) and source chain
    (g, lambda, F, k, S) by the GenProcaccia conventions; metric
    factory of the class. y = (c[n_c], a[12], q, r_m). Box-4 stages
    by the panel-Lagrange scheme (see module docstring)."""

    def __init__(self, y, n_c=16, dr_con=DTYPE(2.5e-5),
                 dr_bld=DTYPE(2.5e-4)):
        y = np.asarray(y, dtype=DTYPE)
        assert y.shape == (n_c + 14,), y.shape
        self.n_c = n_c
        self.knots_c = grading_knots(n_c)
        self.y = y
        self.c = y[:n_c]
        self.a_i = y[n_c:n_c + 12]
        self.q = DTYPE(y[n_c + 12])
        self.r_m = DTYPE(y[n_c + 13])
        rmax = float(R_OUT) + 2.75
        # ---- construction grid: UNIFORM, dr_con (no insertions) ----
        npts = int(np.floor(rmax / float(dr_con))) + 1
        grid = (np.arange(npts, dtype=DTYPE) * dr_con)
        self.construction_grid_n = int(grid.size)
        self._cgrid = grid
        h = float(dr_con)
        # ---- phi on [R1, R2]; stage 1 by the GL-quadrature
        #      antiderivative on the inside grid alone (no stencil
        #      straddles the R1/R2 jumps of phi * 1_[R1,R2]); the
        #      edge jumps are carried by the clip in F1 ----
        inside = (grid >= R1) & (grid <= R2)
        gx_in = grid[inside]
        gx = np.unique(np.r_[float(R1), gx_in, float(R2)]).astype(DTYPE)
        Bm = np.array([BSpline(self.knots_c, np.eye(n_c)[j], 3,
                               extrapolate=False)(gx) for j in range(n_c)])
        Bm = np.nan_to_num(Bm)
        phi_vals = np.exp(self.c @ Bm)
        self.phi_min = float(phi_vals.min())
        self.phi_max = float(phi_vals.max())
        A1 = _stage1_antiderivative(self.c, self.knots_c, n_c, gx)
        self._A1_grid = gx
        self._A1 = A1

        def F1(x):
            return lagrange_eval(gx, A1,
                                 np.clip(x, float(R1), float(R2)))

        vals = (F1(grid + W / 2) - F1(grid - W / 2)) / W
        # ---- stages 2-4: panel-Lagrange antiderivatives ----
        for _ in range(3):
            pa = PanelAntiderivative(vals, 0.0, h)
            vals = _box_average(pa, grid, W)
        self._rho_shape = CubicSpline(grid, vals)
        # ---- builder grid (GenProcaccia convention) ----
        r = np.arange(0.0, rmax + 1e-12, float(dr_bld), dtype=DTYPE)
        r = np.unique(np.sort(np.r_[r, self.r_m, R_IN, R_OUT]))
        self.rg = r
        shape = np.maximum(self._rho_shape(r), 0.0)
        M_un = float(cumulative_trapezoid(4.0 * np.pi * r ** 2 * shape,
                                          r, initial=0.0)[-1])
        self.M_unscaled_unit_rho0 = M_un
        self.rho0 = M_TARGET / M_un
        rho = self.rho0 * shape
        self.rho_max = float(rho.max())
        self._rho_arr = rho
        m = cumulative_trapezoid(4.0 * np.pi * r ** 2 * rho, r, initial=0.0)
        self.M = float(m[-1])
        self._m = CubicSpline(r, m)
        with np.errstate(divide="ignore", invalid="ignore"):
            ap = np.where(r > 0, m / (r * (r - 2.0 * m)), 0.0)
        ap = np.where(np.isfinite(ap), ap, 0.0)
        a_out = np.where(r > 2.0 * self.M,
                         0.5 * np.log(1.0 - 2.0 * self.M
                                      / np.maximum(r, 1e-300)), 0.0)
        i_out = int(np.searchsorted(r, R_OUT))
        seg = cumulative_trapezoid(ap[:i_out + 1][::-1], r[:i_out + 1][::-1],
                                   initial=0.0)[::-1]
        a = np.empty_like(r)
        a[:i_out + 1] = a_out[i_out] + seg
        a[i_out + 1:] = a_out[i_out + 1:]
        self.a_Rin = float(a[0])
        self._a = CubicSpline(r, a)
        self._ap = CubicSpline(r, ap)
        # ---- source chain (GenProcaccia conventions) ----
        klo = R_IN + INSET_LO
        khi = R_OUT - INSET_HI
        self.knot_lo, self.knot_hi = float(klo), float(khi)
        knots = np.r_[[klo] * 3, np.linspace(klo, khi, 10), [khi] * 3]
        Bv = np.array([BSpline(knots, np.eye(12)[i], 3, extrapolate=False)(
            np.clip(r, klo, khi)) for i in range(12)])
        Bv = np.nan_to_num(Bv)
        mod = np.exp(self.a_i @ Bv)
        rhohat = rho / self.rho_max
        g0v = (rhohat ** self.q) * np.tanh((self.r_m - r) / W_SWITCH) * mod
        u = g0v * r ** 2
        i_m = int(np.searchsorted(r, self.r_m))
        I_in = float(np.trapezoid(u[:i_m + 1], r[:i_m + 1]))
        I_out = float(np.trapezoid(u[i_m:], r[i_m:]))
        self.lam = -I_in / I_out
        g = np.where(r < self.r_m, g0v, self.lam * g0v)
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

    # ---- profile accessors ----
    def rho(self, r):
        return np.maximum(
            self.rho0 * self._rho_shape(np.asarray(r, dtype=DTYPE)), 0.0)

    def m_of(self, r):
        r = np.asarray(r, dtype=DTYPE)
        return np.where(r <= 0, 0.0, self._m(np.clip(r, 0, None)))

    def a_of(self, r):
        return self._a(np.asarray(r, dtype=DTYPE))

    def ap_of(self, r):
        return self._ap(np.asarray(r, dtype=DTYPE))

    def B_of(self, r):
        r = np.asarray(r, dtype=DTYPE)
        m = self.m_of(r)
        with np.errstate(divide="ignore", invalid="ignore"):
            B = np.where(r > 0, 1.0 / (1.0 - 2.0 * m
                                       / np.maximum(r, 1e-300)), 1.0)
        return B

    def S_of(self, r):
        return self._S(np.asarray(r, dtype=DTYPE))

    def metric_factory(self, beta):
        beta = DTYPE(beta)
        rmax = float(self.rg[-1])

        def gfunc(pts):
            pts = np.asarray(pts, dtype=DTYPE)
            P = pts.shape[0]
            r = np.linalg.norm(pts, axis=1)
            rc = np.clip(r, 0.0, rmax)
            E = np.exp(2.0 * self.a_of(rc))
            B = self.B_of(rc)
            S = self.S_of(rc)
            g = np.zeros((P, 4, 4), dtype=DTYPE)
            g[:, 0, 0] = -E
            g[:, 0, 1] = g[:, 1, 0] = -beta * S
            gam = np.tile(np.eye(3, dtype=DTYPE), (P, 1, 1))
            safe = r > 1e-12
            if np.any(safe):
                x = pts[safe]
                rr = r[safe]
                n = x / rr[:, None]
                gam[safe] += (B[safe] - 1.0)[:, None, None] \
                    * n[:, :, None] * n[:, None, :]
            g[:, 1:, 1:] = gam
            return g

        return gfunc

    def chain_reads(self):
        return {
            "M": self.M,
            "rho0": float(self.rho0),
            "rho0_rescale_vs_nominal": float(self.rho0 / RHO0_NOMINAL),
            "rho_max": self.rho_max,
            "lambda": float(self.lam),
            "k": float(self.k),
            "int_F_over_r2": self.int_Fr2,
            "a_Rin": self.a_Rin,
            "q": float(self.q),
            "r_m": float(self.r_m),
            "R_in": float(R_IN),
            "R_out": float(R_OUT),
            "knot_lo": self.knot_lo,
            "knot_hi": self.knot_hi,
            "M_unscaled_unit_rho0": self.M_unscaled_unit_rho0,
            "construction_grid_n": self.construction_grid_n,
            "phi_min": self.phi_min,
            "phi_max": self.phi_max,
            "c": [float(v) for v in self.c],
            "stage_scheme": "panel-Lagrange stages 2-4 + GL stage 1 (Phase 417)",
        }


# =====================================================================
# The (10,20)-class verdict point set (shared definition; Gate-7 form)
# =====================================================================
def fib_dirs(n):
    i = np.arange(n, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


DIRS26 = fib_dirs(26)
DIRS162 = fib_dirs(162)


def pts_1020_control():
    rad = np.concatenate([np.arange(0.3 * 10.0, 10.0 - 0.74, 1.0),
                          np.arange(10.0 - 0.75, 20.0 + 0.01, 0.5),
                          np.arange(20.0 + 1.0, 1.35 * 20.0 + 0.01, 2.0)])
    pts = np.concatenate([DIRS26 * r for r in rad]).astype(DTYPE)
    extra_rad = np.concatenate([np.arange(2.5, 4.01, 0.25),
                                np.arange(16.3, 17.01, 0.1),
                                np.arange(26.0, 27.51, 0.25)])
    epts = np.concatenate([DIRS26 * r for r in extra_rad]).astype(DTYPE)
    allpts = np.concatenate([pts, epts])
    return allpts, np.linalg.norm(allpts, axis=1)


# =====================================================================
# Phase 417's own summary / legality code (registered definitions of
# CHECKPOINT386 SS2, as applied by Gates 42/44/51/53)
# =====================================================================
_MKEYS = ("rho", "p", "typeI", "nec", "wec", "sec", "dec", "rho_euler",
          "That", "sampled_nec")


def audit_chunked(gfunc, pts, h, fn, chunk=200):
    parts = []
    for i in range(0, len(pts), chunk):
        parts.append(fn(gfunc, pts[i:i + chunk], h))
    out = {}
    for k in _MKEYS:
        out[k] = np.concatenate([m[k] for m in parts], axis=0)
    return out


def _region_block(m, mask, radp, pts):
    out = {"n": int(mask.sum())}
    if mask.sum() == 0:
        return out
    for key in ("nec", "wec", "sec", "dec"):
        v = m[key][mask]
        if np.all(np.isnan(v)):
            out[key] = None
            out[key + "_r"] = None
            continue
        j = int(np.nanargmin(v))
        idx = np.where(mask)[0][j]
        out[key] = float(v[j])
        out[key + "_r"] = float(radp[idx])
        out[key + "_pt"] = [float(x) for x in pts[idx]]
    finite = [out[k] for k in ("nec", "wec", "sec", "dec")
              if out.get(k) is not None]
    if finite:
        wk = ("nec", "wec", "sec", "dec")[
            int(np.argmin([out.get(k, np.inf)
                           for k in ("nec", "wec", "sec", "dec")]))]
        out["worst"] = out[wk]
        out["worst_kind"] = wk
    ti = m["typeI"][mask]
    out["typeI_frac"] = float(ti.mean()) if ti.size else None
    sn = m["sampled_nec"][mask]
    out["sampled_nec_min"] = float(np.nanmin(sn)) if sn.size else None
    return out


def summarise(m, pts, radp):
    That = m["That"]
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
    out = {"rho_peak": rho_peak, "n_pts": int(len(pts)), "thr": float(thr)}
    regions = (("all_sig", np.ones(len(pts), bool)),
               ("shell", (radp >= R_IN) & (radp <= R_OUT)),
               ("nominal_core", (radp >= R1) & (radp <= R2)),
               ("cavity", radp < R_IN),
               ("exterior", radp > R_OUT))
    for name, mask0 in regions:
        out[name] = _region_block(m, mask0 & (scale > thr), radp, pts)
    ns = scale <= thr
    out["floor_proxy_nonsig_median_abs_nec"] = (
        float(np.nanmedian(np.abs(m["nec"][ns]))) if ns.sum() > 10 else None)
    out["n_nonsig"] = int(ns.sum())
    return out


def legality(summ_by_h, core_key="shell"):
    """Common bars for a (10,20)-class row from {hkey: summary}."""
    out = {}
    ok = True
    for hkey, s in summ_by_h.items():
        a = s["all_sig"]
        floor = s.get("floor_proxy_nonsig_median_abs_nec") or 0.0
        ratio = (a["worst"] / floor) if floor and floor > 0 else None
        c = {"typeI_frac": a["typeI_frac"], "worst": a["worst"],
             "worst_kind": a["worst_kind"],
             "worst_r": a[a["worst_kind"] + "_r"],
             "floor": floor, "worst_over_floor": ratio,
             "core_sampled_nec_min": s[core_key]["sampled_nec_min"],
             "per_ec": {k: a[k] for k in ("nec", "wec", "sec", "dec")},
             "per_ec_r": {k: a[k + "_r"] for k in ("nec", "wec", "sec", "dec")}}
        c["pass"] = bool(a["typeI_frac"] == 1.0
                         and all(a[k] > 0 for k in ("nec", "wec", "sec", "dec"))
                         and (ratio is None or ratio >= 3.0)
                         and s[core_key]["sampled_nec_min"] > 0)
        ok = ok and c["pass"]
        out[hkey] = c
    out["legal"] = bool(ok)
    return out


def second_path_signs(m4, radp):
    """Per-EC all-significant minima from the 4th-order path."""
    That = m4["That"]
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
    sig = scale > thr
    out = {"n_sig": int(sig.sum()),
           "typeI_frac_sig": float(np.mean(m4["typeI"][sig]))
           if sig.sum() else None,
           "sampled_nec_min_sig": float(np.min(m4["sampled_nec"][sig]))
           if sig.sum() else None}
    for k in ("nec", "wec", "sec", "dec"):
        v = m4[k][sig]
        out[k] = float(np.nanmin(v)) if np.isfinite(v).any() else None
    vals = [out[k] for k in ("nec", "wec", "sec", "dec")
            if out[k] is not None]
    out["worst"] = min(vals) if vals else None
    return out


def full_audit(builder, beta, hs=(0.0375, 0.01875), with_audit4=True):
    """wa_auditor (+ audit4) at the given spacings on pts_1020_control,
    with the summary, legality and second-path signs."""
    pts, radp = pts_1020_control()
    gf = builder.metric_factory(beta)
    by_h, sp = {}, {}
    legal_input = {}
    for h in hs:
        hk = f"h{h}"
        m = audit_chunked(gf, pts, h, wa.audit)
        s = summarise(m, pts, radp)
        entry = {"summary": s}
        if with_audit4:
            m4 = audit_chunked(gf, pts, h, p503.audit4)
            sp[hk] = second_path_signs(m4, radp)
            entry["second_path"] = sp[hk]
        by_h[hk] = entry
        legal_input[hk] = s
    leg = legality(legal_input)
    out = {"beta": float(beta), "by_h": by_h, "legality": leg}
    if with_audit4:
        sp_ok = all(v[k] is not None and v[k] > 0
                    for v in sp.values() for k in ("nec", "wec", "sec", "dec"))
        out["second_path_sign_agreement"] = bool(sp_ok)
        out["legal_full_common_bars"] = bool(leg["legal"] and sp_ok)
    return out
