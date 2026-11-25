"""
wb_validate_fast.py — validate the analytic-gradient (fast) path against
the FD path (which passed the registered re-gate) BEFORE the fast path is
trusted anywhere:
 (V1) grad r_a = l identity vs FD gradient of areal_ext at sample points;
 (V2) dipole pole margins (x=0.1 / 0.3) fast vs FD vs the Phase-71 targets;
 (V3) full-grid margin agreement fast vs FD for the dipole at (0.1, 0.19)
      on a coarse theta grid;
 (V4) closure read: fast vs FD max|[h]| at Phase 80's stored L=4
      coefficient vector for x=0.1 (a test POINT only — not our solution).
Output: results/wb_validate_fast.json
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb_lib as W

HERE = os.path.dirname(os.path.abspath(__file__))
P715 = os.path.expanduser("~/workspace/warp-pilot/phase71/results/p715_results.json")
S80 = os.path.expanduser("~/workspace/warp-pilot/phase80/results/p801_solve.json")


def margins(r):
    out = []
    for i in range(len(r["th"])):
        s = W.lanczos(r["KP"][i], r["KM"][i])
        out.append(W.phi_HE(*s)[0])
    return np.array(out)


def main():
    t0 = time.time()
    res = {}
    # V1
    errs = []
    for X in ([0.0, 0.8, 0.3, 0.1], [0.0, -0.9, 0.2, 0.0], [0.0, 0.1, -1.0, 0.2]):
        X = np.array(X, dtype=W.DTYPE)
        fd = W.fd_jac(lambda Z: np.array([W.areal_ext(Z, 0.19)]), X, 1e-6)[0]
        an = W._areal_grad_ext(X, 0.19)
        errs.append(float(np.max(np.abs(fd - an))))
    res["V1_grad_ra_max_err"] = max(errs)

    stored = json.load(open(P715))
    # V2 + V3
    v2, v3 = {}, {}
    for x, lam in ((0.1, 0.19), (0.3, 0.19)):
        dof = stored["frontier"][str(x)]["dof"]
        p = np.array([dof["rho1"], dof["At1"], dof["w1"], 0.0, 0.0])
        rf = W.sample_shell_fast(x, lam, p, 1, [np.pi])
        sf = W.lanczos(rf["KP"][0], rf["KM"][0])
        v2[str(x)] = dict(fast_pole_margin=W.phi_HE(*sf)[0])
        if x == 0.1:
            ths = np.linspace(0.05, np.pi - 0.05, 25)
            m_fd = margins(W.sample_shell(x, lam, p, 1, ths))
            m_fast = margins(W.sample_shell_fast(x, lam, p, 1, ths))
            v3 = dict(max_abs_margin_diff=float(np.max(np.abs(m_fd - m_fast))),
                      grid_n=len(ths))
    res["V2_dipole_pole_fast"] = v2
    res["V3_grid_margin_agreement"] = v3

    # V4
    s80 = json.load(open(S80))["x0.1_lam0.19_L4"]
    p80 = np.array(s80["p"], dtype=W.DTYPE)
    ths = np.linspace(0.2, np.pi - 0.2, 21)
    r_fd = W.sample_shell(0.1, 0.19, p80, 4, ths)
    r_fast = W.sample_shell_fast(0.1, 0.19, p80, 4, ths)
    res["V4_closure_test_point"] = dict(
        max_h_FD=float(np.max(np.abs(r_fd["hP"] - r_fd["hM"]))),
        max_h_fast=float(np.max(np.abs(r_fast["hP"] - r_fast["hM"]))),
        phase80_stored_max_h=float(s80["max_h_audit"]))
    res["seconds"] = time.time() - t0
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    json.dump(res, open(os.path.join(HERE, "results", "wb_validate_fast.json"), "w"),
              indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
