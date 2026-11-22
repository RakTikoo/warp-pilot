#!/usr/bin/env python3
"""G6-3 W-C: classification scans settling (a) whether any geodesic
arc from (1,0) reaches the throat plane z=0 aloft within the slab
(the forced-depth construction's geodesic form), and (b) the
same-sheet control: whether any geodesic dive arc from (1,0)
returning to the brane at z_r beats the brane time over [1, z_r].
Same ODE code path as wc_g63_solver.py."""
import json
import numpy as np
from scipy.integrate import solve_ivp
import wc_g63_solver as W

OUT = "/home/hatch/workspace/warp-pilot/gate6/results/wc_g63_numbers_scans.json"
rhs = W.rhs_factory(W.SPL)
out = {}

# (a) arcs from (1,0), z decreasing to 0, slope p0<0
rows = []
for p0 in [-0.1, -0.2, -0.35, -0.5, -0.7, -1.0, -1.5, -2.0, -3.0,
           -4.5, -6.0, -9.0]:
    def ev_ret(z, Y):
        return Y[0]
    ev_ret.terminal = True; ev_ret.direction = -1

    def ev_slab(z, Y):
        return Y[0] - 0.46
    ev_slab.terminal = True; ev_slab.direction = 1

    def ev_turn(z, Y):
        return 60.0 - abs(Y[1])
    ev_turn.terminal = True; ev_turn.direction = -1
    sol = solve_ivp(rhs, (1.0, 0.0), [0.0, p0], method="DOP853",
                    rtol=1e-11, atol=1e-13, max_step=0.02,
                    events=[ev_ret, ev_slab, ev_turn], dense_output=True)
    row = {"p0": p0, "ymax": float(np.max(sol.y[0]))}
    if sol.t_events[0].size:
        row.update({"class": "returned_to_brane",
                    "z_return": float(sol.t_events[0][0])})
    elif sol.t_events[1].size:
        row.update({"class": "exited_slab_top",
                    "z_exit": float(sol.t_events[1][0])})
    elif sol.t_events[2].size:
        row.update({"class": "turned_vertical",
                    "z_turn": float(sol.t[-1])})
    else:
        row.update({"class": "reached_z0_aloft",
                    "y_at_0": float(sol.y[0, -1])})
    rows.append(row)
    print("ARC", row, flush=True)
out["arcs_from_za1_to_throat_plane"] = rows

# (b) same-sheet dive arcs from (1,0), z increasing, slope p0>0
rows = []
for p0 in [0.05, 0.1, 0.2, 0.35, 0.5, 0.8, 1.2, 2.0, 3.5]:
    def ev_ret(z, Y):
        return Y[0]
    ev_ret.terminal = True; ev_ret.direction = -1

    def ev_turn(z, Y):
        return 60.0 - abs(Y[1])
    ev_turn.terminal = True; ev_turn.direction = -1
    sol = solve_ivp(rhs, (1.0, 3.2), [0.0, p0], method="DOP853",
                    rtol=1e-11, atol=1e-13, max_step=0.02,
                    events=[ev_ret, ev_turn], dense_output=True)
    row = {"p0": p0, "ymax": float(np.max(sol.y[0]))}
    if sol.t_events[0].size:
        zr = float(sol.t_events[0][0])
        T_arc, _, _ = W.arc_integral(W.SPL, sol, 1.0, zr)
        tb = W.ell(zr) - W.ell(1.0)
        row.update({"class": "returned", "z_return": zr,
                    "T_arc": T_arc, "t_brane_span": tb,
                    "arc_minus_brane": T_arc - tb})
    elif sol.t_events[1].size:
        row.update({"class": "turned_vertical"})
    else:
        row.update({"class": "no_return_by_z3.2"})
    rows.append(row)
    print("DIVE", row, flush=True)
out["same_sheet_dive_arcs"] = rows
json.dump(out, open(OUT, "w"), indent=1)
print("DONE", flush=True)
