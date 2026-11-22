#!/usr/bin/env python3
"""GATE-6 / W-C / G6-3 — INDEPENDENT second path for the P43-1 bulk
shortcut measurement. float64 everywhere.

Method (structurally different from Phase 43's discrete variational
minimiser p431_geodesic.minimise_time, which is NOT used or re-run):
the optical functional T = int sqrt((D^2 dz^2 + dy^2)/A^2) is the
length functional of the 2D Riemannian metric diag(E,G),
E=(D/A)^2, G=(1/A)^2, in the (z,y) plane. Its stationary paths are
geodesics; we solve the Euler-Lagrange ODE for y(z),

  L = sqrt(E + G p^2),  p = dy/dz,
  d/dz (G p / L) = (E_y + G_y p^2) / (2 L),

expanded to p' = S/(G E) * [ (E_y+G_y p^2)/2 - (G_z+G_y p) p
                             + G p (E_z + E_y p + (G_z+G_y p) p^2)/(2S) ],
  S = E + G p^2,

with scipy solve_ivp (DOP853) shooting / root-finding:

 * cross-throat, depth cap c: the optimum is NOT a smooth symmetric
   crossing geodesic (shooting from the throat, (0,y0,p=0), returns
   to the brane within dz ~ 0.26 for every y0 — verified in-script);
   it is a cap-riding path: geodesic arc from (za,0) hitting y=c at
   z1 (corner admissible for the one-sided constraint y<=c), a
   boundary ride along y=c from z1 to -z1, and the mirrored arc.
   T(p0) is minimised over the arc's shooting slope p0 (1-D).
 * forced-depth rows: geodesic arc from (za,0) through the pinned
   throat point (0,Y): root-find p0 with y(0)=Y.
 * same-sheet control: symmetric shooting from the midpoint
   (1.5, y0, p=0), root-find the brane return at z=2.
 * flat gate: identical code path with A=D=1 fields.

Shared definition (allowed): the stored bulk fields
phase43/results/p431_bulk_fields.npz (A, D on (snap_y, zz)).
Field representation here: interpolating bicubic splines
(RectBivariateSpline, s=0) — different from Phase 43's linear
RegularGridInterpolator; the headline path is ALSO re-evaluated
under the linear representation as a sensitivity bound.
"""
import json
import numpy as np
from scipy.interpolate import RectBivariateSpline, RegularGridInterpolator
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq, minimize_scalar

NPZ = "/home/hatch/workspace/warp-pilot/phase43/results/p431_bulk_fields.npz"
OUT = "/home/hatch/workspace/warp-pilot/gate6/results/wc_g63_numbers.json"

d = np.load(NPZ)
ZZ, SY, AF, DF = d["zz"], d["snap_y"], d["A"], d["D"]


def make_fields(Aarr, Darr):
    return (RectBivariateSpline(SY, ZZ, Aarr, kx=3, ky=3, s=0),
            RectBivariateSpline(SY, ZZ, Darr, kx=3, ky=3, s=0))


SPL = make_fields(AF, DF)
FLAT = make_fields(np.ones_like(AF), np.ones_like(DF))
LIN_A = RegularGridInterpolator((SY, ZZ), AF)
LIN_D = RegularGridInterpolator((SY, ZZ), DF)


def rhs_factory(spl):
    sA, sD = spl

    def rhs(z, Y):
        y, p = float(Y[0]), float(Y[1])
        a = float(sA.ev(y, z)); dv = float(sD.ev(y, z))
        az = float(sA.ev(y, z, dx=0, dy=1)); ay = float(sA.ev(y, z, dx=1, dy=0))
        Dz = float(sD.ev(y, z, dx=0, dy=1)); Dy = float(sD.ev(y, z, dx=1, dy=0))
        q = dv / a
        qz = (Dz * a - dv * az) / a**2; qy = (Dy * a - dv * ay) / a**2
        E = q * q; Ez = 2 * q * qz; Ey = 2 * q * qy
        G = 1.0 / a**2; Gz = -2 * az / a**3; Gy = -2 * ay / a**3
        S = E + G * p * p
        R = (0.5 * (Ey + Gy * p * p) - (Gz + Gy * p) * p
             + G * p * (Ez + Ey * p + (Gz + Gy * p) * p * p) / (2 * S))
        return [p, S / (G * E) * R]

    return rhs


def q_of(spl, y, z):
    sA, sD = spl
    return float(sD.ev(y, z)) / float(sA.ev(y, z))


def arc_integral(spl, sol, z_from, z_to, n=2000):
    """Optical time along a dense-output solution between two z's."""
    zs = np.linspace(z_from, z_to, n)
    Ys = sol.sol(zs)
    sA, sD = spl
    Av = sA.ev(Ys[0], zs); Dv = sD.ev(Ys[0], zs)
    Tv = np.sqrt((Dv / Av) ** 2 + (1.0 / Av) ** 2 * Ys[1] ** 2)
    return float(np.trapezoid(Tv, zs)), zs, Ys


def ride_integral(spl, cap, z1, n=2000):
    zs = np.linspace(0.0, z1, n)
    sA, sD = spl
    qv = sD.ev(np.full_like(zs, cap), zs) / sA.ev(np.full_like(zs, cap), zs)
    return float(np.trapezoid(qv, zs))


# ---------------- brane times (shared definition: Phi=0 proper length)
def D0_of(z):
    x = 1.0 + z ** 2
    return 2.0 * np.sqrt(2.0) if abs(z) < 1e-12 else \
        2.0 * abs(z) / np.sqrt(1.0 - x ** -0.5)


def ell(za):
    v, _ = quad(D0_of, 0.0, za, epsabs=1e-13, epsrel=1e-13, limit=200)
    return float(v)


# ---------------- shooting primitives
def shoot_brane_to_throat(spl, za, p0, cap=None, rtol=1e-11, max_step=0.02):
    """Geodesic from (za, 0) with slope p0<0, integrated z: za -> 0.
    Returns dict with either cap-hit info or throat values."""
    rhs = rhs_factory(spl)

    def ev_turn(z, Y):
        return 60.0 - abs(Y[1])
    ev_turn.terminal = True; ev_turn.direction = -1
    events = [ev_turn]
    if cap is not None:
        def ev_cap(z, Y):
            return Y[0] - cap
        ev_cap.terminal = True; ev_cap.direction = 1
        events = [ev_cap, ev_turn]
    sol = solve_ivp(rhs, (za, 0.0), [0.0, p0], method="DOP853",
                    rtol=rtol, atol=1e-13, events=events,
                    max_step=max_step, dense_output=True)
    out = {"p0": p0}
    if sol.t_events[-1].size:
        # geodesic turned vertical in z-parametrisation: not a
        # candidate for any optimum here; assign infinite time.
        out.update({"hit_cap": False, "turned": True,
                    "y_at_0": -1.0, "p_at_0": float("nan"),
                    "ymax": float(np.max(sol.y[0])),
                    "T_total_smooth": float("inf")})
        return out
    out["turned"] = False
    if cap is not None and sol.t_events[0].size:
        z1 = float(sol.t_events[0][0])
        T_arc, _, _ = arc_integral(spl, sol, z1, za)
        out.update({"hit_cap": True, "z1": z1,
                    "p_at_cap": float(sol.y_events[0][0][1]),
                    "T_arc": T_arc,
                    "T_total": 2 * T_arc + 2 * ride_integral(spl, cap, z1)})
    else:
        out.update({"hit_cap": False, "y_at_0": float(sol.y[0, -1]),
                    "p_at_0": float(sol.y[1, -1]),
                    "ymax": float(np.max(sol.y[0]))})
        if not out["hit_cap"]:
            T_half, _, _ = arc_integral(spl, sol, 0.0, za)
            out["T_total_smooth"] = 2 * T_half
    return out


def cap_ride_optimum(spl, za, cap, rtol=1e-11, max_step=0.02):
    """Minimise T over shooting slope for the cap-riding family;
    also track the smooth (non-cap) candidate and the brane path."""
    scan = {}
    for p0 in [0.0, -0.02, -0.05, -0.1, -0.2, -0.3, -0.5, -0.8, -1.2,
               -1.8, -2.5, -3.5, -5.0, -7.0, -10.0, -12.0]:
        r = shoot_brane_to_throat(spl, za, p0, cap=cap, rtol=rtol,
                                  max_step=max_step)
        scan[p0] = r
    def value(r):
        return r["T_total"] if r["hit_cap"] else r["T_total_smooth"]

    def value_at(p):
        return value(shoot_brane_to_throat(spl, za, p, cap=cap, rtol=rtol,
                                           max_step=max_step))
    rides = {p0: value(r) for p0, r in scan.items()}
    best_p0 = min(rides, key=rides.get)
    # robust local refinement: two dense multiplicative zooms around
    # the scan optimum (Brent is unsafe here — turned slopes give
    # infinite values and poison its arithmetic).
    p_opt = float(best_p0)
    if best_p0 != 0.0:
        for facs in (np.linspace(0.6, 1.4, 17), np.linspace(0.92, 1.08, 17)):
            cand = [(p_opt * f, value_at(p_opt * f)) for f in facs]
            cand = [(p, v) for p, v in cand if np.isfinite(v)]
            if cand:
                p_opt = float(min(cand, key=lambda t: t[1])[0])
    r_opt = shoot_brane_to_throat(spl, za, p_opt, cap=cap, rtol=rtol,
                                  max_step=max_step)
    if not r_opt["hit_cap"]:
        # optimum is the mirrored-arc (smooth/corner-at-throat) path
        return {"za": za, "cap": cap, "p0_opt": p_opt,
                "T_bulk": float(r_opt["T_total_smooth"]), "z1": None,
                "p_at_cap": None, "optimum_type": "smooth_mirror",
                "scan_T": {str(k): v for k, v in rides.items()},
                "smooth_candidates": {}}
    r_opt = dict(r_opt); r_opt["optimum_type"] = "cap_ride"
    smooth = {p0: r for p0, r in scan.items() if not r["hit_cap"]}
    return {"za": za, "cap": cap, "p0_opt": p_opt,
            "optimum_type": "cap_ride",
            "T_bulk": float(r_opt["T_total"]), "z1": r_opt["z1"],
            "p_at_cap": r_opt["p_at_cap"],
            "scan_T": {str(k): (v["T_total"] if v["hit_cap"] else None)
                       for k, v in scan.items()},
            "smooth_candidates": {str(k): {"y_at_0": v["y_at_0"],
                                           "p_at_0": v["p_at_0"],
                                           "T": v.get("T_total_smooth")}
                                  for k, v in smooth.items()}}


def forced_depth(spl, za, Y):
    """Geodesic arc (za,0) -> (0,Y); root-find p0 on y(0)=Y."""
    def f(p0):
        r = shoot_brane_to_throat(spl, za, p0, cap=None)
        return r["y_at_0"] - Y
    grid = [-0.05, -0.15, -0.3, -0.5, -0.8, -1.2, -1.8, -2.6, -3.8]
    vals = [(p, f(p)) for p in grid]
    root = None
    for (p1, v1), (p2, v2) in zip(vals, vals[1:]):
        if v1 == 0.0:
            root = p1; break
        if v1 * v2 < 0:
            root = brentq(f, p2, p1, xtol=1e-10, rtol=1e-12); break
    if root is None:
        return {"Y": Y, "root_found": False,
                "scan": [[p, v + Y] for p, v in vals]}
    r = shoot_brane_to_throat(spl, za, root, cap=None)
    rhs = rhs_factory(spl)
    sol = solve_ivp(rhs, (za, 0.0), [0.0, root], method="DOP853",
                    rtol=1e-11, atol=1e-13, max_step=0.02, dense_output=True)
    T_arc, _, _ = arc_integral(spl, sol, 0.0, za)
    return {"Y": Y, "root_found": True, "p0": float(root),
            "T_bulk": 2 * T_arc, "arc_ymax": float(np.max(sol.y[0]))}


def same_sheet(spl, rtol=1e-11):
    """Symmetric shooting from midpoint z=1.5, y=y0, p=0 -> return z."""
    rhs = rhs_factory(spl)

    def shoot(y0):
        def ev(z, Y):
            return Y[0]
        ev.terminal = True; ev.direction = -1
        sol = solve_ivp(rhs, (1.5, 2.6), [y0, 0.0], method="DOP853",
                        rtol=rtol, atol=1e-13, events=[ev],
                        max_step=0.02, dense_output=True)
        if not sol.t_events[0].size:
            return None
        zh = float(sol.t_events[0][0])
        T_half, _, _ = arc_integral(spl, sol, 1.5, zh)
        return zh, 2 * T_half

    def g(y0):
        r = shoot(y0)
        return (r[0] - 2.0) if r else 1.0
    grid = [0.005, 0.01, 0.02, 0.04, 0.07, 0.1, 0.15, 0.22, 0.3]
    vals = [(y, g(y)) for y in grid]
    root = None
    for (a, va), (b, vb) in zip(vals, vals[1:]):
        if va * vb < 0:
            root = brentq(g, a, b, xtol=1e-12, rtol=1e-12); break
    tb = ell(2.0) - ell(1.0)
    if root is None:
        return {"t_brane": tb, "root_found": False,
                "scan": [[y, v + 2.0] for y, v in vals]}
    zh, T = shoot(root)
    return {"t_brane": tb, "root_found": True, "y0_mid": float(root),
            "T_bulk": T, "gain_frac": (tb - T) / tb}


def throat_return_scan(spl):
    """Smooth symmetric crossing geodesics: from (0,y0,p=0), where do
    they return to the brane? (Bounds the span of any smooth
    cross-throat geodesic.)"""
    rhs = rhs_factory(spl)
    rows = []
    for y0 in [0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.455]:
        def ev(z, Y):
            return Y[0]
        ev.terminal = True; ev.direction = -1
        sol = solve_ivp(rhs, (0.0, 6.0), [y0, 0.0], method="DOP853",
                        rtol=1e-11, atol=1e-13, events=[ev],
                        max_step=0.02)
        rows.append({"y0": y0,
                     "z_return": float(sol.t_events[0][0])
                     if sol.t_events[0].size else None})
    return rows


def headline_linear_eval(za, cap, p_opt):
    """Re-evaluate the ODE-optimal cap-riding path's time under
    Phase 43's LINEAR field representation (path not re-optimised:
    an upper-bound / sensitivity evaluation)."""
    r = shoot_brane_to_throat(SPL, za, p_opt, cap=cap)
    z1 = r["z1"]
    rhs = rhs_factory(SPL)

    def ev_cap(z, Y):
        return Y[0] - cap
    ev_cap.terminal = True; ev_cap.direction = 1
    # MUST stop at the cap: integrating past y=0.46 leaves the stored
    # grid and the spline extrapolation stalls the ODE (found the
    # hard way in the gate run).
    sol = solve_ivp(rhs, (za, 0.0), [0.0, p_opt], method="DOP853",
                    rtol=1e-11, atol=1e-13, max_step=0.02,
                    events=[ev_cap], dense_output=True)
    zs = np.linspace(z1, za, 4000)
    Ys = sol.sol(zs)
    pts = np.stack([Ys[0], zs], axis=1)
    Av = LIN_A(pts); Dv = LIN_D(pts)
    Tv = np.sqrt((Dv / Av) ** 2 + (1.0 / Av) ** 2 * Ys[1] ** 2)
    T_arc = float(np.trapezoid(Tv, zs))
    zr = np.linspace(0.0, z1, 4000)
    ptsr = np.stack([np.full_like(zr, cap), zr], axis=1)
    ride = float(np.trapezoid(LIN_D(ptsr) / LIN_A(ptsr), zr))
    return {"T_bulk_linear_fields": 2 * T_arc + 2 * ride, "z1": z1}


def main():
    out = {"method": "Euler-Lagrange geodesic ODE shooting (solve_ivp "
                     "DOP853) + cap-riding boundary arcs; bicubic-spline "
                     "field representation of the stored npz fields",
           "units": "r0=1, c=1"}
    # ---- flat gate on the identical code path
    gate = cap_ride_optimum(FLAT, 1.0, 0.455)
    tb_flat = 2.0 * 1.0
    out["flat_gate"] = {"T_bulk": gate["T_bulk"], "t_brane": tb_flat,
                        "gain_frac": (tb_flat - gate["T_bulk"]) / tb_flat,
                        "rel_err": abs(gate["T_bulk"] - tb_flat) / tb_flat,
                        "p0_opt": gate["p0_opt"]}
    print("FLAT GATE", out["flat_gate"], flush=True)
    out["throat_return_scan"] = throat_return_scan(SPL)
    print("THROAT RETURN", out["throat_return_scan"], flush=True)
    # ---- cross-throat rows, free depth = cap 0.455 (Phase bound),
    #      plus cap 0.46 (slab edge) sensitivity at za=1
    cross = []
    for za in (0.5, 1.0, 2.0):
        r = cap_ride_optimum(SPL, za, 0.455)
        tb = 2 * ell(za)
        r.update({"t_brane": tb, "gain_frac": (tb - r["T_bulk"]) / tb,
                  "u_eff": tb / r["T_bulk"]})
        cross.append(r)
        print("CROSS", za, r["T_bulk"], r["gain_frac"], "z1", r["z1"],
              flush=True)
    out["cross_throat_cap0455"] = cross
    r46 = cap_ride_optimum(SPL, 1.0, 0.46)
    tb1 = 2 * ell(1.0)
    r46.update({"t_brane": tb1, "gain_frac": (tb1 - r46["T_bulk"]) / tb1})
    out["za1_cap046"] = r46
    print("ZA1 CAP0.46", r46["T_bulk"], r46["gain_frac"], flush=True)
    # ---- convergence: headline row at looser tolerance / bigger step
    rc = cap_ride_optimum(SPL, 1.0, 0.455, rtol=1e-9, max_step=0.05)
    out["za1_convergence_loose"] = {"T_bulk": rc["T_bulk"],
                                    "p0_opt": rc["p0_opt"]}
    print("ZA1 LOOSE", rc["T_bulk"], flush=True)
    out["za1_linear_field_eval"] = headline_linear_eval(1.0, 0.455,
                                                        cross[1]["p0_opt"])
    print("ZA1 LINEAR EVAL", out["za1_linear_field_eval"], flush=True)
    # ---- cap scan at za=1
    caps = []
    for cap in (0.20, 0.30, 0.40):
        r = cap_ride_optimum(SPL, 1.0, cap)
        r.update({"t_brane": tb1, "gain_frac": (tb1 - r["T_bulk"]) / tb1})
        caps.append(r)
        print("CAP", cap, r["T_bulk"], r["gain_frac"], flush=True)
    out["cap_scan_za1"] = caps
    # ---- forced-depth rows at za=1
    fd = []
    for Y in (0.1, 0.2, 0.3, 0.4, 0.44, 0.45):
        r = forced_depth(SPL, 1.0, Y)
        if r.get("root_found"):
            r.update({"t_brane": tb1,
                      "gain_frac": (tb1 - r["T_bulk"]) / tb1})
        fd.append(r)
        print("FORCED", Y, r.get("T_bulk"), r.get("gain_frac"), flush=True)
    out["forced_depth_za1"] = fd
    # ---- same-sheet control
    out["same_sheet"] = same_sheet(SPL)
    print("SAME SHEET", out["same_sheet"], flush=True)
    json.dump(out, open(OUT, "w"), indent=1)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
