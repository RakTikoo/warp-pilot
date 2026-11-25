"""P80-1 R3/R1b: multipole Darmois solve in the programme FD auditor
(p801_lib; numpy float64, no JAX/warpax/author code), from the published
specification (Supplement S + published code's dof layout/bounds):
unknowns [rho, At, w, wi, Ai] l=1..L multiplying lam; residual
([h_tautau],[h_tautheta],[h_thetatheta])/lam on a solve grid; damped
Gauss-Newton with FD-in-coefficient-space Jacobian; start = padded
Phase-71 dipole solution. Checkpoints after every iteration.
Usage: p801_solve.py x lam L [ntheta] [maxiter]"""
import sys, json, time
import numpy as np
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase80/work")
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase71/work")
from p801_lib import sample_mp, stress_rows, phi_HE, audit_grid
from p715_lib import darmois_solve

OUT = "/home/hatch/workspace/warp-pilot/phase80/results/p801_solve.json"
x = float(sys.argv[1]); lam = float(sys.argv[2]); L = int(sys.argv[3])
ntheta = int(sys.argv[4]) if len(sys.argv) > 4 else 13
maxiter = int(sys.argv[5]) if len(sys.argv) > 5 else 6
key = f"x{x}_lam{lam}_L{L}"

try:
    out = json.load(open(OUT))
except Exception:
    out = {}
if key in out and out[key].get("done"):
    print("already done", key); sys.exit(0)

dof = darmois_solve(x)
p = np.zeros(5 * L)
p[0] = dof["rho1"]; p[L] = dof["At1"]; p[2 * L] = dof["w1"]
print("dipole start:", {k: dof[k] for k in ("rho1", "At1", "w1")}, flush=True)

thetas_solve = np.linspace(0.15, np.pi - 0.15, ntheta)
lo = np.concatenate([[-4.0] * L, [-8.0] * L, [-0.8] * L, [-0.8] * L, [-8.0] * L])
hi = -lo


def resid(pv):
    r = sample_mp(x, lam, pv, L, thetas_solve, h=0.01)
    dh = r["hP"] - r["hM"]
    return np.concatenate([dh[:, 0, 0], dh[:, 0, 1], dh[:, 1, 1]]) / lam


hist = []
t0 = time.time()
r0 = resid(p)
print(f"iter0 |r|max={np.max(np.abs(r0)):.4e} ({time.time()-t0:.0f}s)", flush=True)
hist.append(dict(it=0, rmax=float(np.max(np.abs(r0))), p=[float(v) for v in p]))
out[key] = dict(x=x, lam=lam, L=L, hist=hist, done=False)
json.dump(out, open(OUT, "w"), indent=1)

for it in range(1, maxiter + 1):
    npar = len(p)
    J = np.zeros((len(r0), npar))
    for k in range(npar):
        step = 1e-3 * max(1.0, abs(p[k]))
        pk = p.copy(); pk[k] += step
        J[:, k] = (resid(pk) - r0) / step
    # damped Gauss-Newton step
    A = J.T @ J + 1e-8 * np.eye(npar)
    dp = np.linalg.solve(A, -J.T @ r0)
    # backtracking on the true residual
    alpha = 1.0
    improved = False
    for _ in range(4):
        pn = np.clip(p + alpha * dp, lo, hi)
        rn = resid(pn)
        if np.max(np.abs(rn)) < np.max(np.abs(r0)):
            improved = True
            break
        alpha *= 0.5
    print(f"iter{it} alpha={alpha} |r|max {np.max(np.abs(r0)):.4e} -> "
          f"{np.max(np.abs(rn)):.4e} ({time.time()-t0:.0f}s)", flush=True)
    p, r0 = pn, rn
    hist.append(dict(it=it, rmax=float(np.max(np.abs(r0))),
                     p=[float(v) for v in p], alpha=alpha))
    out[key] = dict(x=x, lam=lam, L=L, hist=hist, done=False)
    json.dump(out, open(OUT, "w"), indent=1)
    if not improved or np.max(np.abs(r0)) < 2e-5:
        break

# audit read of the independently solved coefficients
grid = audit_grid()
r = sample_mp(x, lam, p, L, grid, h=0.01)
S = stress_rows(r)
dh = r["hP"] - r["hM"]
margins = []; types = []
for s in S:
    m, t = phi_HE(*s); margins.append(m); types.append(t)
margins = np.array(margins); i = int(np.argmin(margins))
out[key].update(dict(done=True, p=[float(v) for v in p],
                     max_h_audit=float(np.max(np.abs(dh))),
                     worst_margin=float(margins[i]), theta_bind=float(grid[i]),
                     pole_margin=float(margins[-1]),
                     all_type_I=bool(all(t == 1 for t in types)),
                     seconds=time.time() - t0))
json.dump(out, open(OUT, "w"), indent=1)
print("INDEP", key, json.dumps({k: out[key][k] for k in
      ("max_h_audit", "worst_margin", "theta_bind", "pole_margin", "all_type_I")}),
      flush=True)
