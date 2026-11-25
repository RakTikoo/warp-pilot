#!/usr/bin/env python
"""P80-1 checker: recomputes the deciding numbers from the stored JSONs
(p801_audit.json, p801_solve.json, p801_recon.json if present) and
re-reads the stored per-theta stress arrays through the Eq.(35) margin
form (phi_HE, Phase-71 auditor). Verifies the registered bars per
audited pin and the L-refinement agreement at the deciding pins.
Run: ~/workspace/warp-pilot/venv/bin/python p801_check.py
Writes p801_check.json. Exit 0 iff all checks pass."""
import json, sys, os
import numpy as np

HERE = "/home/hatch/workspace/warp-pilot/phase80/results"
sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase71/work")
from p715_lib import phi_HE  # noqa: E402

checks = []


def chk(name, ok, detail=""):
    checks.append(dict(name=name, pass_=bool(ok), detail=str(detail)))


audit = json.load(open(f"{HERE}/p801_audit.json"))
solve = json.load(open(f"{HERE}/p801_solve.json"))
PAPER_MARGINS = {0.1: 1.8e-3, 0.3: 9.1e-3, 0.5: 18e-3, 0.7: 21e-3}

for key, A in sorted(audit.items()):
    x = A["x"]
    worst_re = np.inf; allI_re = True; pole_re = None; front_re = None
    bad_rows = 0
    for row in A["rows"]:
        m, t = phi_HE(*row["stress"])
        worst_re = min(worst_re, m)
        allI_re = allI_re and (t == 1)
        if abs(row["th"] - np.pi) < 1e-9:
            pole_re = m
        if abs(row["th"]) < 1e-9:
            front_re = m
        if abs(m - row["margin"]) > 1e-12 or t != row["type"]:
            bad_rows += 1
    chk(f"{key} stored rows recompute", bad_rows == 0, f"bad={bad_rows}")
    chk(f"{key} worst margin recompute", abs(worst_re - A["worst_margin"]) < 1e-12,
        f"{worst_re:+.6e} vs {A['worst_margin']:+.6e}")
    chk(f"{key} pole endpoint present+recompute",
        pole_re is not None and abs(pole_re - A["pole_margin"]) < 1e-12,
        f"pole={pole_re}")
    chk(f"{key} front pole endpoint present", front_re is not None,
        f"front={front_re}")
    chk(f"{key} Type-I recompute", allI_re == A["all_type_I"], f"{allI_re}")
    lad = A["ladder"]
    chk(f"{key} BAR worst>0", A["worst_margin"] > 0, A["worst_margin"])
    chk(f"{key} BAR pole>0", A["pole_margin"] > 0, A["pole_margin"])
    chk(f"{key} BAR Type-I everywhere", A["all_type_I"] is True)
    chk(f"{key} BAR eig margins>=0", A["min_eig_margin"] >= 0, A["min_eig_margin"])
    chk(f"{key} BAR sampled>=0", A["sampled_dec_at_bind"] >= -1e-9,
        A["sampled_dec_at_bind"])
    chk(f"{key} BAR ladder all>0", all(v["margin"] > 0 for v in lad.values()),
        {k: round(v["margin"], 8) for k, v in lad.items()})
    ladvals = [v["margin"] for v in lad.values()]
    chk(f"{key} ladder spread < 2e-5", max(ladvals) - min(ladvals) < 2e-5,
        f"spread {max(ladvals)-min(ladvals):.2e}")
    if x in PAPER_MARGINS:
        chk(f"{key} vs paper margin (factor 2)",
            0.5 < A["worst_margin"] / PAPER_MARGINS[x] < 2.0,
            f"audit {A['worst_margin']:+.4e} paper {PAPER_MARGINS[x]:.1e}")

# L-refinement agreement at the two Phase-71 deciding pins (adversarial:
# independent solves at L=4 and L=6 must give the same pole margin)
for xx in (0.1, 0.3):
    k4, k6 = f"x{xx}_L4", f"x{xx}_L6"
    if k4 in audit and k6 in audit:
        d = abs(audit[k4]["pole_margin"] - audit[k6]["pole_margin"])
        chk(f"x{xx} L4-vs-L6 pole margin agreement < 1e-4", d < 1e-4,
            f"L4 {audit[k4]['pole_margin']:+.4e} L6 {audit[k6]['pole_margin']:+.4e}")
        chk(f"x{xx} closure improves/stays small with L",
            audit[k6]["max_h"] < 1e-5, f"L6 max_h {audit[k6]['max_h']:.2e}")

# solve.json's own audit-grid reads agree with audit.json (two reads of
# the same coefficients by the same auditor on the same grid)
for skey, S in solve.items():
    if not S.get("done") or "worst_margin" not in S:
        continue
    akey = f"x{S['x']}_L{S['L']}"
    if akey in audit:
        chk(f"{skey} solve-read vs audit worst margin",
            abs(S["worst_margin"] - audit[akey]["worst_margin"]) < 1e-9,
            f"{S['worst_margin']:+.6e} vs {audit[akey]['worst_margin']:+.6e}")

# author-path corroboration, where landed
if os.path.exists(f"{HERE}/p801_recon.json"):
    recon = json.load(open(f"{HERE}/p801_recon.json"))
    for rkey, R in recon.items():
        chk(f"author {rkey} frame_ok", R["frame_ok"] is True)
        chk(f"author {rkey} residual below dipole (0.0139 at x=0.1 scale)",
            R["max_h"] < 0.014, f"max_h {R['max_h']:.2e}")

npass = sum(c["pass_"] for c in checks)
out = dict(n=npass, total=len(checks), checks=checks)
json.dump(out, open(f"{HERE}/p801_check.json", "w"), indent=1)
print(f"{npass}/{len(checks)} PASS")
for c in checks:
    if not c["pass_"]:
        print("FAIL:", c["name"], c["detail"])
sys.exit(0 if npass == len(checks) else 1)
