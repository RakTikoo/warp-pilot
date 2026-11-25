"""P80-1 R2 (full): gate audit of a solved multipole coefficient set from
p801_solve.json (or p801_recon.json with --author) on the registered
pole-inclusive audit grid, with h-ladder + 4th-order FD + sampled-observer
cross-check at the deciding angle. Stores into p801_audit.json.
Usage: p801_audit2.py <solve_key> [--author]"""
import sys, json, time
import numpy as np
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase80/work")
from p801_lib import (sample_mp, stress_rows, phi_HE, eig_margins,
                      sampled_dec_min, audit_grid)

RES = "/home/hatch/workspace/warp-pilot/phase80/results"
skey = sys.argv[1]
author = "--author" in sys.argv
src = json.load(open(f"{RES}/p801_recon.json" if author else f"{RES}/p801_solve.json"))
rec = src[skey]
x, lam, L = rec["x"], rec["lam"], rec["L"]
p = np.array(rec["p"])
key = f"x{x}_L{L}" + ("_author" if author else "")

try:
    out = json.load(open(f"{RES}/p801_audit.json"))
except Exception:
    out = {}
if key in out:
    print("already audited", key); sys.exit(0)

t0 = time.time()
grid = audit_grid()
r = sample_mp(x, lam, p, L, grid, h=0.01)
S = stress_rows(r)
dh = r["hP"] - r["hM"]
rows = []
worst = np.inf; ibind = None
allI = True; min_disc = np.inf; min_eig = np.inf
for i, (th, s) in enumerate(zip(grid, S)):
    m, t = phi_HE(*s)
    rho_e, ppar, em1, em2, disc = eig_margins(*s)
    allI = allI and (t == 1)
    min_disc = min(min_disc, disc)
    min_eig = min(min_eig, em1, em2)
    if m < worst:
        worst, ibind = m, i
    rows.append(dict(th=float(th), stress=[float(v) for v in s],
                     margin=float(m), type=int(t),
                     eig_rho=None if rho_e is None else float(rho_e),
                     eig_ppar=None if ppar is None else float(ppar),
                     eig_margin=float(min(em1, em2)), disc=float(disc)))
th_bind = float(grid[ibind]); s_bind = S[ibind]
samp = sampled_dec_min(*s_bind, n=2000, seed=801)
ladder = {}
for h, order in [(0.02, 2), (0.01, 2), (0.005, 2), (0.01, 4)]:
    rr = sample_mp(x, lam, p, L, np.array([th_bind]), h=h, order=order)
    ss = stress_rows(rr)[0]
    mm, tt = phi_HE(*ss)
    ladder[f"h{h}_o{order}"] = dict(margin=float(mm), type=int(tt),
                                   stress=[float(v) for v in ss])
out[key] = dict(
    x=x, lam=lam, L=L, source=("author_code" if author else "fd_solve"),
    n_grid=len(grid),
    max_h=float(np.max(np.abs(dh))), max_h_per_lam=float(np.max(np.abs(dh))) / lam,
    worst_margin=float(worst), theta_bind=th_bind,
    pole_margin=float(rows[-1]["margin"]), pole_type=int(rows[-1]["type"]),
    front_pole_margin=float(rows[0]["margin"]),
    all_type_I=bool(allI), min_disc=float(min_disc), min_eig_margin=float(min_eig),
    sampled_dec_at_bind=float(samp), ladder=ladder, rows=rows,
    seconds=time.time() - t0)
json.dump(out, open(f"{RES}/p801_audit.json", "w"), indent=1)
print(f"AUDIT {key}: worst={worst:+.6e} at pi-th={np.pi-th_bind:.4f} "
      f"pole={rows[-1]['margin']:+.6e} max_h={out[key]['max_h']:.3e} allI={allI} "
      f"min_eig={min_eig:+.3e} samp={samp:+.3e} ladder=" +
      {k: round(v['margin'], 8) for k, v in ladder.items()}.__repr__(), flush=True)
