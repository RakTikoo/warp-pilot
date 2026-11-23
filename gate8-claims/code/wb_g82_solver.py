#!/usr/bin/env python3
"""GATE-8 / W-B / G8-2 -- INDEPENDENT second path for the P46-3 attained
mirror completion. float64 everywhere.

Deciding machinery (fresh, Gate-6 W-C pattern): the optical functional
T = int sqrt((D^2 dz^2 + dy^2)/A^2) is the length functional of the 2D
Riemannian metric diag(E,G), E=(D/A)^2, G=(1/A)^2 in the (z,y) plane.
Stationary paths obey the Euler-Lagrange ODE for y(z) (L=sqrt(E+G p^2)):

  p' = S/(G E) * [ (E_y+G_y p^2)/2 - (G_z+G_y p) p
                   + G p (E_z + E_y p + (G_z+G_y p) p^2)/(2S) ],
  S = E + G p^2,

integrated with scipy solve_ivp DOP853 in shooting form. Phase 46's
discrete variational minimiser (p431_geodesic.minimise_time) is NOT
used anywhere. Shared definition (allowed, as in Gate-6): the stored
P29-3 bulk fields phase43/results/p431_bulk_fields.npz (A, D, C on
snap_y x zz), represented here by interpolating bicubic splines.

Rows:
 * flat-RS2 gate on the identical code path (A=D=1): zero EXACT bar.
 * uncompleted record: cap y<=0.455 at z_a=1 (claim 0.480).
 * completed bulk (Z2 mirror at y_c): cap-ride optimum at cap=y_c is
   the attained minimiser of the completed space; rows y_c in
   {0.20,0.25,0.30,0.35,0.40}.
 * Z2 double-space check at y_c=0.30,0.40: mirrored spline fields on
   u in [0, 2 y_c]; crossing-class shooting from (-1,0) to (1,2 y_c).
 * valley evidence: q(u)=D/A profile across the interface in the
   double at several z; one-sided slopes at the cap.
"""
import json
import numpy as np
from scipy.interpolate import RectBivariateSpline
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

NPZ = "/home/hatch/workspace/warp-pilot/phase43/results/p431_bulk_fields.npz"
OUT = "/home/hatch/workspace/warp-pilot/gate8/results/wb_g82_numbers.json"
TB_RECORD = 6.278421790292845

d = np.load(NPZ)
ZZ, SY, AF, DF, CF = d["zz"], d["snap_y"], d["A"], d["D"], d["C"]
print("snap_y:", SY, "zz range:", ZZ[0], ZZ[-1], "nz:", len(ZZ), flush=True)


def make_splines(Aarr, Darr, ygrid=SY, zgrid=ZZ):
    return (RectBivariateSpline(ygrid, zgrid, Aarr, kx=3, ky=3, s=0),
            RectBivariateSpline(ygrid, zgrid, Darr, kx=3, ky=3, s=0))


SPL = make_splines(AF, DF)
FLAT = make_splines(np.ones_like(AF), np.ones_like(DF))


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


def arc_time(spl, sol, z_from, z_to, n=900):
    zs = np.linspace(z_from, z_to, n)
    Ys = sol.sol(zs)
    sA, sD = spl
    Av = sA.ev(Ys[0], zs); Dv = sD.ev(Ys[0], zs)
    Tv = np.sqrt((Dv / Av) ** 2 + (1.0 / Av) ** 2 * Ys[1] ** 2)
    return float(np.trapezoid(Tv, zs))


def ride_time(spl, cap, z1, n=900):
    zs = np.linspace(0.0, z1, n)
    sA, sD = spl
    qv = sD.ev(np.full_like(zs, cap), zs) / sA.ev(np.full_like(zs, cap), zs)
    return float(np.trapezoid(qv, zs))


def shoot_to_cap(spl, za, p0, cap, rtol=1e-10, max_step=0.04):
    """Geodesic from (za,0) slope p0<0 integrated z: za->0, stop at cap."""
    rhs = rhs_factory(spl)

    def ev_turn(z, Y):
        return 60.0 - abs(Y[1])
    ev_turn.terminal = True; ev_turn.direction = -1

    def ev_cap(z, Y):
        return Y[0] - cap
    ev_cap.terminal = True; ev_cap.direction = 1
    sol = solve_ivp(rhs, (za, 0.0), [0.0, p0], method="DOP853",
                    rtol=rtol, atol=1e-13, events=[ev_cap, ev_turn],
                    max_step=max_step, dense_output=True)
    if sol.t_events[1].size:
        return {"hit_cap": False, "turned": True, "T_total": float("inf")}
    if sol.t_events[0].size:
        z1 = float(sol.t_events[0][0])
        T_arc = arc_time(spl, sol, z1, za)
        return {"hit_cap": True, "turned": False, "z1": z1,
                "p_at_cap": float(sol.y_events[0][0][1]),
                "T_arc": T_arc,
                "T_total": 2 * T_arc + 2 * ride_time(spl, cap, z1)}
    T_half = arc_time(spl, sol, 0.0, za)
    return {"hit_cap": False, "turned": False,
            "y_at_0": float(sol.y[0, -1]), "p_at_0": float(sol.y[1, -1]),
            "T_total": 2 * T_half}


def cap_optimum(spl, za, cap, rtol=1e-10, max_step=0.04):
    scan_p = [0.0, -0.02, -0.05, -0.1, -0.2, -0.3, -0.5, -0.8, -1.2,
              -1.8, -2.5, -3.5, -5.0, -7.0, -10.0, -12.0]
    vals = {}
    for p0 in scan_p:
        r = shoot_to_cap(spl, za, p0, cap, rtol, max_step)
        vals[p0] = r["T_total"]
    p_opt = float(min(vals, key=vals.get))
    if p_opt != 0.0:
        for facs in (np.linspace(0.7, 1.3, 9), np.linspace(0.94, 1.06, 9)):
            cand = []
            for f in facs:
                p = p_opt * f
                v = shoot_to_cap(spl, za, p, cap, rtol, max_step)["T_total"]
                if np.isfinite(v):
                    cand.append((p, v))
            if cand:
                p_opt = float(min(cand, key=lambda t: t[1])[0])
    r = shoot_to_cap(spl, za, p_opt, cap, rtol, max_step)
    return {"za": za, "cap": cap, "p0_opt": p_opt, "T_bulk": r["T_total"],
            "hit_cap": r.get("hit_cap"), "z1": r.get("z1"),
            "p_at_cap": r.get("p_at_cap"),
            "scan_T": {str(k): v for k, v in vals.items()}}


# ---------------- brane time (shared definition: Phi=0 proper length)
def D0_of(z):
    x = 1.0 + z ** 2
    return 2.0 * np.sqrt(2.0) if abs(z) < 1e-12 else \
        2.0 * abs(z) / np.sqrt(1.0 - x ** -0.5)


def ell(za):
    v, _ = quad(D0_of, 0.0, za, epsabs=1e-13, epsrel=1e-13, limit=200)
    return float(v)


def main():
    out = {"method": "Gate-8 W-B fresh Euler-Lagrange geodesic-ODE "
                     "shooting (DOP853), bicubic-spline fields from the "
                     "stored P29-3 npz (shared definition)",
           "units": "r0=1, c=1"}
    tb = 2 * ell(1.0)
    out["t_brane_za1_mine"] = tb
    out["t_brane_za1_record"] = TB_RECORD
    print("t_brane mine", tb, "record", TB_RECORD, flush=True)

    # ---- flat gate, identical code path
    g = cap_optimum(FLAT, 1.0, 0.455)
    out["flat_gate"] = {"T_bulk": g["T_bulk"], "t_brane": 2.0,
                        "gain": (2.0 - g["T_bulk"]) / 2.0,
                        "rel_err": abs(g["T_bulk"] - 2.0) / 2.0,
                        "p0_opt": g["p0_opt"]}
    print("FLAT GATE", out["flat_gate"], flush=True)

    # ---- uncompleted record: cap 0.455, za=1
    r = cap_optimum(SPL, 1.0, 0.455)
    r["gain"] = (tb - r["T_bulk"]) / tb
    out["uncompleted_cap0455_za1"] = r
    print("UNCOMPLETED cap0.455", r["T_bulk"], r["gain"], "z1", r["z1"],
          "p_at_cap", r["p_at_cap"], flush=True)

    # ---- completed bulk: mirror rows
    rows = {}
    for yc in (0.20, 0.25, 0.30, 0.35, 0.40):
        r = cap_optimum(SPL, 1.0, yc)
        r["gain"] = (tb - r["T_bulk"]) / tb
        r["u_eff"] = tb / r["T_bulk"]
        rows[str(yc)] = r
        print("MIRROR yc", yc, "T", r["T_bulk"], "gain", r["gain"],
              "z1", r["z1"], "p_at_cap", r["p_at_cap"], flush=True)
    out["mirror_rows"] = rows

    # convergence of headline row at loose tolerance
    rc = cap_optimum(SPL, 1.0, 0.30, rtol=1e-9, max_step=0.05)
    out["headline_loose_tol"] = {"T_bulk": rc["T_bulk"], "p0_opt": rc["p0_opt"]}
    print("HEADLINE LOOSE", rc["T_bulk"], flush=True)

    # ---- Z2 double-space construction at yc = 0.30, 0.40
    dbl = {}
    for yc in (0.30, 0.40):
        iy = int(np.argmin(np.abs(SY - yc)))
        assert abs(SY[iy] - yc) < 1e-9
        # mirrored grids: u in [0, 2yc]; rows 0..iy then iy-1..0
        A_d = np.vstack([AF[:iy + 1], AF[iy - 1::-1]])
        D_d = np.vstack([DF[:iy + 1], DF[iy - 1::-1]])
        u_grid = np.concatenate([SY[:iy + 1], 2 * yc - SY[iy - 1::-1]])
        spl_d = make_splines(A_d, D_d, ygrid=u_grid)
        # valley evidence: q(u) = D/A across the interface
        valley = {}
        for zq in (0.0, 0.3, 0.6):
            us = np.linspace(yc - 0.1, yc + 0.1, 21)
            qv = [float(spl_d[1].ev(u, zq)) / float(spl_d[0].ev(u, zq))
                  for u in us]
            valley[str(zq)] = {"u": [float(u) for u in us],
                               "q": qv,
                               "q_min_u": float(us[int(np.argmin(qv))]),
                               "dq_left": float(qv[10] - qv[0]),
                               "dq_right": float(qv[-1] - qv[10])}
        # crossing-class shooting: from (-1, 0) in the double, slope p0,
        # integrate z: -1 -> 1, record u(1); want u(1) = 2 yc.
        rhs_d = rhs_factory(spl_d)

        def cross_shoot(p0):
            def ev_top(z, Y):
                return Y[0] - 2 * yc
            ev_top.terminal = True; ev_top.direction = 1

            def ev_bot(z, Y):
                return Y[0]
            ev_bot.terminal = True; ev_bot.direction = -1

            def ev_turn(z, Y):
                return 60.0 - abs(Y[1])
            ev_turn.terminal = True; ev_turn.direction = -1
            sol = solve_ivp(rhs_d, (-1.0, 1.0), [0.0, p0], method="DOP853",
                            rtol=1e-10, atol=1e-12,
                            events=[ev_top, ev_bot, ev_turn],
                            max_step=0.04, dense_output=True)
            if sol.t_events[2].size:
                return {"status": "turned"}
            if sol.t_events[0].size:
                return {"status": "exited_top", "z": float(sol.t_events[0][0])}
            if sol.t_events[1].size and sol.t[-1] < 1.0 - 1e-9:
                return {"status": "returned_bottom",
                        "z": float(sol.t_events[1][0])}
            T = arc_time(spl_d, sol, -1.0, 1.0)
            return {"status": "reached", "u_at_1": float(sol.y[0, -1]),
                    "T": T}
        scan = {}
        for p0 in np.concatenate([[0.0], np.linspace(0.05, 3.0, 30)]):
            scan[float(p0)] = cross_shoot(float(p0))
        dbl[str(yc)] = {"valley": valley,
                        "crossing_scan": {str(k): v for k, v in scan.items()}}
        reached = {k: v for k, v in scan.items() if v["status"] == "reached"}
        print("DOUBLE yc", yc, "statuses:",
              {s: sum(1 for v in scan.values() if v["status"] == s)
               for s in ("reached", "turned", "exited_top", "returned_bottom")},
              flush=True)
        if reached:
            for k, v in reached.items():
                print("  reached p0", k, "u(1)", v["u_at_1"], "T", v["T"],
                      flush=True)
    json.dump(out, open(OUT, "w"), indent=1)
    out["double_space"] = dbl
    json.dump(out, open(OUT, "w"), indent=1)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
