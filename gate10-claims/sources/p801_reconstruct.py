"""P80-1 R1: reconstruction of Le's multipole solution by running the
PUBLISHED code (github.com/anindex/world_tube @ 1e9e3db,
reproduce/multipole_frontier.py machinery) at the five frontier pins,
full dof set (interior tilt + interior lapse ON, bounded), L=6, and
L=8 at x=0.5,0.7. Stores converged coefficient vectors (the reconstructed
solution) + author's own-grid diagnostics. Checkpoints per pin."""
import sys, json, time
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase80/work/world_tube_repo")
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase80/work/world_tube_repo/reproduce")

from multipole_frontier import solve_multipole, surface_stress_over_theta, _unpack  # noqa: E402
from worldtube.energy import FRONTIER_G, phi_HE  # noqa: E402
from worldtube.geometry import lanczos  # noqa: E402

OUT = "/home/hatch/workspace/warp-pilot/phase80/results/p801_recon.json"
res = {}
if len(sys.argv) > 1 and sys.argv[1] == "resume":
    try:
        res = json.load(open(OUT))
    except Exception:
        res = {}

def pad5(p_prev, L_prev, L_new):
    """Warm-start pad for the 5-block layout [rho, At, w, wi, Ai]."""
    if p_prev is None:
        return None
    blocks = []
    for b in range(5):
        v = np.zeros(L_new)
        v[:L_prev] = p_prev[b * L_prev:(b + 1) * L_prev]
        blocks.append(v)
    return np.concatenate(blocks)


jobs = [(0.1, 6), (0.2, 6), (0.3, 6), (0.5, 6), (0.7, 6), (0.5, 8), (0.7, 8)]
for x, L in jobs:
    key = f"x{x}_L{L}"
    if key in res:
        print("skip", key, flush=True)
        continue
    lam = FRONTIER_G[x]
    t0 = time.time()
    # warm-start continuation in L (same published solve, staged):
    # L=2 -> L=4 -> target L, each bounded, full dof.
    p_warm, L_warm = None, None
    for L_stage in [l for l in (2, 4, 6, 8) if l < L] + [L]:
        p_warm, info_s = solve_multipole(
            x, lam, L_stage, interior_tilt=True, interior_lapse=True,
            ntheta=23, bounded=True,
            p0=pad5(p_warm, L_warm, L_stage) if p_warm is not None else None)
        print(f"  stage {key} L={L_stage} max_h={info_s['max_h']:.3e}", flush=True)
        L_warm = L_stage
    p, info = p_warm, info_s
    # author's own stress read (their grid [0.12, pi-0.12], 29 pts)
    ths, S = surface_stress_over_theta(x, lam, p, L, info["ext"], info["gI"],
                                       interior_tilt=True, interior_lapse=True,
                                       ntheta=29)
    margins = []
    types = []
    for s in S:
        m, t = phi_HE(*s)
        margins.append(float(m)); types.append(int(t))
    margins = np.array(margins)
    i = int(np.argmin(margins))
    rho, At, w, wi, Ai = _unpack(p, L, True, True)
    res[key] = dict(
        x=x, lam=lam, L=L,
        coeff=dict(rho=[float(v) for v in rho], At=[float(v) for v in At],
                   w=[float(v) for v in w], wi=[float(v) for v in wi],
                   Ai=[float(v) for v in Ai]),
        p=[float(v) for v in p],
        max_h=float(info["max_h"]), max_h_per_lam=float(info["max_h_per_lam"]),
        coeff_norm=float(info["coeff_norm"]), frame_ok=bool(info["frame_ok"]),
        author_grid=dict(thetas=[float(v) for v in ths],
                         margins=[float(v) for v in margins],
                         types=types,
                         worst=float(margins[i]), theta_bind=float(ths[i]),
                         stress=[[float(v) for v in s] for s in S]),
        seconds=time.time() - t0)
    json.dump(res, open(OUT, "w"), indent=1)
    print(f"DONE {key} max_h={info['max_h']:.3e} worst_author={margins[i]:+.5f} "
          f"at th={ths[i]:.3f} types={sorted(set(types))} ({time.time()-t0:.0f}s)",
          flush=True)
print("ALL DONE")
