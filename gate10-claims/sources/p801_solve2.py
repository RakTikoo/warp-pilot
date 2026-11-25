"""P80-1 R3b: high-compactness multipole solve — amplitude (lambda)
continuation + L continuation, scipy bounded least_squares on the FD
auditor residual (p801_lib), warm starts throughout. For pins where the
direct Gauss-Newton stalls (x=0.5, 0.7). Checkpoints per stage.
Usage: p801_solve2.py x lam L"""
import sys, json, time
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase80/work")
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase71/work")
from p801_lib import sample_mp, stress_rows, phi_HE, audit_grid
from p715_lib import darmois_solve

OUT = "/home/hatch/workspace/warp-pilot/phase80/results/p801_solve.json"
x = float(sys.argv[1]); lam_pin = float(sys.argv[2]); L = int(sys.argv[3])
key = f"x{x}_lam{lam_pin}_L{L}c"

thetas_solve = np.linspace(0.15, np.pi - 0.15, 13)


def make_resid(lam, Lc):
    def resid(pv):
        r = sample_mp(x, lam, pv, Lc, thetas_solve, h=0.01)
        dh = r["hP"] - r["hM"]
        v = np.concatenate([dh[:, 0, 0], dh[:, 0, 1], dh[:, 1, 1]]) / lam
        return np.where(np.isfinite(v), v, 5.0)
    return resid


def bounds(Lc):
    lo = np.concatenate([[-4.0] * Lc, [-8.0] * Lc, [-0.8] * Lc,
                         [-0.8] * Lc, [-8.0] * Lc])
    return lo, -lo


def pad(p_prev, L_prev, L_new):
    if p_prev is None:
        return None
    blocks = []
    for b in range(5):
        v = np.zeros(L_new)
        v[:L_prev] = p_prev[b * L_prev:(b + 1) * L_prev]
        blocks.append(v)
    return np.concatenate(blocks)


t0 = time.time()
dof = darmois_solve(x)
stages = []
p_cur, L_cur = None, None
for lam_stage in [0.25 * lam_pin, 0.5 * lam_pin, 0.75 * lam_pin, lam_pin]:
    for Lc in [l for l in (2, 4, 6) if l < L] + [L]:
        lo, hi = bounds(Lc)
        if p_cur is None:
            p0 = np.zeros(5 * Lc)
            p0[0] = dof["rho1"]; p0[Lc] = dof["At1"]; p0[2 * Lc] = dof["w1"]
        else:
            p0 = pad(p_cur, L_cur, Lc)
        sol = least_squares(make_resid(lam_stage, Lc), np.clip(p0, lo + 1e-9, hi - 1e-9),
                            method="trf", bounds=(lo, hi), x_scale="jac",
                            xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=150)
        rmax = float(np.max(np.abs(make_resid(lam_stage, Lc)(sol.x))))
        stages.append(dict(lam=lam_stage, L=Lc, rmax=rmax, nfev=int(sol.nfev)))
        print(f"stage lam={lam_stage:.4f} L={Lc}: |r|max={rmax:.3e} nfev={sol.nfev} "
              f"({time.time()-t0:.0f}s)", flush=True)
        p_cur, L_cur = sol.x, Lc

lam = lam_pin
grid = audit_grid()
r = sample_mp(x, lam, p_cur, L, grid, h=0.01)
S = stress_rows(r)
dh = r["hP"] - r["hM"]
margins = []; types = []
for s in S:
    m, t = phi_HE(*s); margins.append(m); types.append(t)
margins = np.array(margins)
finite = np.isfinite(margins)
i = int(np.argmin(np.where(finite, margins, np.inf)))
res = dict(x=x, lam=lam, L=L, p=[float(v) for v in p_cur], stages=stages,
           max_h_audit=float(np.nanmax(np.abs(dh))),
           worst_margin=float(margins[i]), theta_bind=float(grid[i]),
           pole_margin=float(margins[-1]),
           all_type_I=bool(all(t == 1 for t in types)),
           all_finite=bool(finite.all()), done=True, seconds=time.time() - t0)
try:
    out = json.load(open(OUT))
except Exception:
    out = {}
out[key] = res
json.dump(out, open(OUT, "w"), indent=1)
print("INDEP2", key, json.dumps({k: res[k] for k in
      ("max_h_audit", "worst_margin", "theta_bind", "pole_margin", "all_type_I",
       "all_finite")}), flush=True)
