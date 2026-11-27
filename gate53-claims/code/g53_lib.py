"""
PROVENANCE (Gate-53): this module is the gate's own machinery, written
for Gate-53 in the gate-lineage builder pattern of Gates 42/44/51 (the
graded-family builder generalised here to grading bases of
n_c in {8, 12, 16} modes). It imports NOTHING from phase408/work,
phase392/work, phase391/work or phase386/work. Instruments:
gate6/wa_auditor.py and phase50/p503_lib.audit4, the registered pair.

g53_lib.py — Gate-53 FRESH machinery for the independent re-judgement
of the Phase 408 claim set (ledger entry 1086, FU-P408-1). Written
for this gate from:
  * the construction registered in phase386/CHECKPOINT386.md SS2
    (graded family: phi = exp(sum_j c_j B_j) on [R1, R2],
    rho = rho0 * Box4_W[phi*1_[R1,R2]], Box4_W = four successive
    sliding box averages of width W, centred), carried unchanged
    through CHECKPOINT391/392/408 (the arena is unchanged; the
    phases' box widenings are search-space facts, not construction
    changes);
  * the shared class definitions of the (10,20) shell class
    (Procaccia background chain and metric factory as fixed by the
    paper's S2/S3 parameters and the programme's reconstruction,
    phase50/p501_recon.py);
  * the common verdict bars registered in CHECKPOINT386 SS2 and
    inherited verbatim by CHECKPOINT391/392/408: on the primary wa
    audit at BOTH spacings (h = 0.0375, 0.01875), registered set
    pts_1020_control — Type-I fraction = 1.000 over significant
    points; worst NEC/WEC/SEC/DEC margins > 0, sign-stable, worst
    >= 3x the measured FD floor; shell sampled-null NEC min > 0 —
    AND audit4 agreement on the sign of every deciding margin (the
    four eigenvalue EC minima). Per Gate-44 SS1 C-1, audit4's own
    Type-I fraction and direction-sampled diagnostics are recorded
    as diagnostics, NOT bars.

Gate-53's own additions (the thin-margin scrutiny charged at entry
1086): the box-4 stages 2-4 are evaluated by the SPLINE-
ANTIDERIVATIVE scheme (each stage's profile carried as a cubic
spline on the construction grid, the box average taken from the
spline's exact antiderivative) — a different numerical organisation
from the phase's cumulative-trapezoid + Hermite scheme; a
trapezoid+Hermite scheme is carried alongside as an internal
cross-check. The deciding reads are additionally taken on a spacing
ladder FINER than the registered pair (h = 0.009375, 0.0046875)
with the FD floor proxy measured at every rung and a Richardson
h -> 0 extrapolation of the deciding margin.
Tensor instruments: gate6/wa_auditor.py (2nd-order FD, the Gate-6
standard auditor) and phase50/p503_lib.audit4 (4th-order second
path) — the registered instrument pair, as in Gates 42/44/51. The
summary, legality, q-read and point-set code below is the gate's
own. float64 everywhere. VM frame of record.
"""
import sys
import numpy as np
from scipy.interpolate import BSpline, CubicSpline, CubicHermiteSpline
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


def Pfun_gen(x):
    """Closed-form box-4 step response (shared definition)."""
    from math import comb
    u = np.asarray(x, dtype=DTYPE) / W
    out = np.zeros_like(u)
    for j in range(5):
        t = u + 2.0 - j
        out = out + ((-1.0) ** j) * comb(4, j) * np.where(
            t > 0, t ** 4, 0.0)
    return out / 24.0


def analytic_step_rho(r):
    """The step member's density in closed form (shared definition)."""
    r = np.asarray(r, dtype=DTYPE)
    return np.maximum(RHO0_NOMINAL * (Pfun_gen(r - R1) - Pfun_gen(r - R2)), 0.0)


class GradedBuilder:
    """rho = rho0 * Box4_W[phi * 1_[R1,R2]], phi = exp(sum_j c_j B_j)
    on an n_c-mode grading basis; background (m, a) and source chain
    (g, lambda, F, k, S) by the GenProcaccia conventions; metric
    factory of the class. y = (c[n_c], a[12], q, r_m)."""

    def __init__(self, y, n_c=16, dr_con=DTYPE(2.5e-5),
                 dr_bld=DTYPE(2.5e-4), stage_scheme="spline"):
        y = np.asarray(y, dtype=DTYPE)
        assert y.shape == (n_c + 14,), y.shape
        self.n_c = n_c
        self.stage_scheme = stage_scheme
        self.knots_c = grading_knots(n_c)
        self.y = y
        self.c = y[:n_c]
        self.a_i = y[n_c:n_c + 12]
        self.q = DTYPE(y[n_c + 12])
        self.r_m = DTYPE(y[n_c + 13])
        rmax = float(R_OUT) + 2.75
        # ---- construction grid: base + R1, R2, grading knots and
        #      their +- {W/2, W, 3W/2, 2W} shifts inserted ----
        base = np.arange(0.0, rmax + 1e-12, float(dr_con), dtype=DTYPE)
        knots_u = np.unique(self.knots_c)
        ins = list(knots_u)
        for k in knots_u:
            for s in (W / 2, W, 3 * W / 2, 2 * W):
                ins += [k - s, k + s]
        ins = [v for v in ins if 0.0 <= float(v) <= rmax]
        grid = np.unique(np.sort(np.r_[base, np.array(ins, dtype=DTYPE)]))
        self.construction_grid_n = int(grid.size)
        self._cgrid = grid
        # ---- phi on [R1, R2]; stage 1 exact via the plateau spline's
        #      antiderivative (the edge jump is carried exactly) ----
        inside = (grid >= R1) & (grid <= R2)
        gx = grid[inside]
        Bm = np.array([BSpline(self.knots_c, np.eye(n_c)[j], 3,
                               extrapolate=False)(gx) for j in range(n_c)])
        Bm = np.nan_to_num(Bm)
        phi_vals = np.exp(self.c @ Bm)
        self.phi_min = float(phi_vals.min())
        self.phi_max = float(phi_vals.max())
        phi_sp = CubicSpline(gx, phi_vals)
        Aphi = phi_sp.antiderivative()
        Aphi_R1 = float(Aphi(R1))

        def F1(x):
            return Aphi(np.clip(x, float(R1), float(R2))) - Aphi_R1

        vals = (F1(grid + W / 2) - F1(grid - W / 2)) / W
        # ---- stages 2-4: centred sliding box average of the current
        #      stage profile. Gate-53 primary scheme "spline": the
        #      average is taken from the antiderivative of the stage's
        #      cubic spline. Cross-check scheme "trapH": cumulative-
        #      trapezoid antiderivative evaluated at shifted points by
        #      cubic Hermite interpolation (the phase's scheme). ----
        g0, gN = float(grid[0]), float(grid[-1])
        for _ in range(3):
            if stage_scheme == "spline":
                A = CubicSpline(grid, vals).antiderivative()
                vals = (A(np.clip(grid + W / 2, g0, gN))
                        - A(np.clip(grid - W / 2, g0, gN))) / W
            elif stage_scheme == "trapH":
                Avals = cumulative_trapezoid(vals, grid, initial=0.0)
                H = CubicHermiteSpline(grid, Avals, vals)
                vals = (H(np.clip(grid + W / 2, g0, gN))
                        - H(np.clip(grid - W / 2, g0, gN))) / W
            else:
                raise ValueError(stage_scheme)
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
            "stage_scheme": self.stage_scheme,
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
# The gate's own summary / legality / q-read code
# (registered bars of CHECKPOINT386 SS2; definitions as in Gate-7)
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


def q_reads(m, radp):
    """q = 2|T_0n| / (T_00 + T_nn) at the sampled-NEC-minimising
    direction per point (162 Fibonacci directions); q_worst at the
    worst sampled-NEC significant point; q_max over significant
    points."""
    That = m["That"]
    T00 = That[:, 0, 0]
    T0i = That[:, 0, 1:]
    Tij = That[:, 1:, 1:]
    quad = np.einsum("njk,ij,ik->ni", Tij, DIRS162, DIRS162)
    vals = T00[:, None] + 2.0 * (T0i @ DIRS162.T) + quad
    jmin = np.argmin(vals, axis=1)
    n_at = DIRS162[jmin]
    T0n = np.einsum("ij,ij->i", T0i, n_at)
    Tnn = np.einsum("ij,ijk,ik->i", n_at, Tij, n_at)
    denom = T00 + Tnn
    with np.errstate(divide="ignore", invalid="ignore"):
        q = np.where(denom > 0,
                     2.0 * np.abs(T0n) / np.maximum(denom, 1e-300), np.inf)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(T00))
    thr = max(1e-9 * (10.0 / float(R1)) ** 2, 1e-3 * abs(rho_peak))
    sig = scale > thr
    sn = m["sampled_nec"]
    iw = int(np.where(sig)[0][np.argmin(sn[sig])])
    qs = q[sig]
    rs = radp[sig]
    imax = int(np.argmax(qs))
    return {
        "thr": float(thr), "n_sig": int(sig.sum()),
        "typeI_frac_sig": float(np.mean(m["typeI"][sig])),
        "q_worst": float(q[iw]), "q_worst_r": float(radp[iw]),
        "min_sampled_nec_sig": float(sn[iw]),
        "q_max": float(qs[imax]), "q_max_r": float(rs[imax]),
        "q_max_typeI": bool(m["typeI"][sig][imax]),
        "n_q_gt_1_sig": int(np.sum(qs > 1.0)),
        "n_nonTypeI_sig": int(np.sum(~m["typeI"][sig])),
    }


def full_audit(builder, beta, hs=(0.0375, 0.01875), with_audit4=True):
    """wa_auditor (+ audit4) at the given spacings on pts_1020_control,
    with the gate's summary, legality, second-path signs and q reads."""
    pts, radp = pts_1020_control()
    gf = builder.metric_factory(beta)
    by_h, sp = {}, {}
    legal_input = {}
    for h in hs:
        hk = f"h{h}"
        m = audit_chunked(gf, pts, h, wa.audit)
        s = summarise(m, pts, radp)
        entry = {"summary": s, "q": q_reads(m, radp)}
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
