"""
wb_solve.py — GATE-10 W-B fresh reconstruction of Le's multipole solution.

Solves the published specification (paper Supplement S method + published
code's dof layout / box bounds / pins) with fresh code in gate10/:
scipy bounded least-squares (trf) on the Darmois residual
([h_tautau], [h_tautheta], [h_thetatheta]) / lam over the author's solve
grid th in [0.2, pi-0.2] (21 pts), interior tilt + interior lapse ON,
starting from the padded Phase-71 dipole dof (L=4) or the padded own
L=4 solution (L=6). Phase 80's solver/auditor code is NOT used.

Usage: wb_solve.py x lam L [startfile]
Writes results/wb_solve_x{x}_L{L}.json (checkpointed per pin).
"""
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb_lib as W

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
P715 = os.path.expanduser("~/workspace/warp-pilot/phase71/results/p715_results.json")
SOLVE_TH = np.linspace(0.2, np.pi - 0.2, 21)
POOL = None


def residual(p, x, lam, L):
    args = [(x, lam, list(map(float, p)), L, float(th), 0.01, 2) for th in SOLVE_TH]
    if POOL is not None:
        rows = POOL.map(W.sample_one_fast, args)
    else:
        rows = [W.sample_one_fast(a) for a in args]
    dh = np.array([r[0] - r[2] for r in rows])       # hP - hM
    return np.concatenate([dh[:, 0, 0], dh[:, 0, 1], dh[:, 1, 1]]) / lam


def bounds(L):
    lo, hi = [], []
    for cap in (4.0, 8.0, 0.8, 0.8, 8.0):            # rho, At, w, wi, Ai
        lo += [-cap] * L; hi += [cap] * L
    return np.array(lo), np.array(hi)


def dipole_start(x, L):
    dof = json.load(open(P715))["frontier"][str(x)]["dof"]
    p = np.zeros(5 * L)
    p[0] = dof["rho1"]; p[L] = dof["At1"]; p[2 * L] = dof["w1"]
    return p


def pad_start(p_prev, L_prev, L):
    p = np.zeros(5 * L)
    for b in range(5):
        p[b * L:b * L + L_prev] = p_prev[b * L_prev:(b + 1) * L_prev]
    return p


def max_h_on(p, x, lam, L, thetas):
    r = W.sample_shell(x, lam, p, L, thetas)
    dh = r["hP"] - r["hM"]
    return float(np.max(np.abs(dh)))


def main():
    global POOL
    x, lam, L = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
    startfile = sys.argv[4] if len(sys.argv) > 4 else None
    if startfile:
        prev = json.load(open(startfile))
        p0 = pad_start(np.array(prev["p"]), int(prev["L"]), L)
        start_desc = f"padded own L={prev['L']} solution from {startfile}"
    else:
        p0 = dipole_start(x, L)
        start_desc = "padded Phase-71 dipole dof"
    lo, hi = bounds(L)
    p0 = np.clip(p0, lo + 1e-9, hi - 1e-9)
    POOL = Pool(2)
    t0 = time.time()
    hist = []

    def fun(p):
        r = residual(p, x, lam, L)
        hist.append(float(np.max(np.abs(r))))
        return r

    max_nfev = int(os.environ.get("WB_MAX_NFEV", "300"))
    sol = least_squares(fun, p0, method="trf", bounds=(lo, hi),
                        diff_step=1e-5, xtol=1e-12, ftol=1e-12, gtol=1e-12,
                        max_nfev=max_nfev, verbose=0)
    POOL.close(); POOL.join()
    p = sol.x
    dense = np.linspace(0.12, np.pi - 0.12, 61)
    out = dict(x=x, lam=lam, L=L, start=start_desc, p=[float(v) for v in p],
               hist=hist, nfev=int(sol.nfev), cost=float(sol.cost),
               max_h_solvegrid=float(lam * hist[-1]),
               max_h_dense=float(max_h_on(p, x, lam, L, dense)),
               seconds=time.time() - t0)
    os.makedirs(RESULTS, exist_ok=True)
    fn = os.path.join(RESULTS, f"wb_solve_x{x}_L{L}.json")
    json.dump(out, open(fn, "w"), indent=1)
    print(f"x={x} L={L}: max_h_solve={out['max_h_solvegrid']:.3e} "
          f"max_h_dense={out['max_h_dense']:.3e} nfev={sol.nfev} "
          f"({out['seconds']:.0f}s) -> {fn}", flush=True)


if __name__ == "__main__":
    main()
