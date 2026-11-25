"""
wb_check.py — GATE-10 W-B checker: recomputes every deciding bar from the
stored wb_*.json result files (no re-solve). Bars per GATE10.md (G10-2):
 (regate) dipole pole values within 5% of -2.0096e-4 / -1.2263e-4;
 (a) Type-I at every grid point at each pin (L=4 and L=6);
 (b) worst DEC > 0 and within max(15% rel, 3e-4 abs) of the phase values
     +1.728e-3 (x=0.1), +5.143e-3 (x=0.2), +9.102e-3 (x=0.3);
 (c) binding sites: rear pole th=pi at x=0.1; front pole th=0 at x=0.3;
     front pole th=0 at x=0.2 (as recorded in phase80 p801_audit.json);
 (d) closure max|[h]| at x=0.1 within a factor 2 of 1.5e-7;
 (e) L=4 and L=6 agree on the sign of every deciding margin.
Output: results/wb_check.json + printed summary.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
PHASE = {0.1: 1.728e-3, 0.2: 5.143e-3, 0.3: 9.102e-3}
BIND = {0.1: np.pi, 0.2: 0.0, 0.3: 0.0}


def load(name):
    return json.load(open(os.path.join(RESULTS, name)))


def main():
    checks = []

    def chk(name, ok, detail):
        checks.append(dict(name=name, pass_=bool(ok), detail=detail))

    rg = load("wb_regate.json")
    for x in ("0.1", "0.3"):
        c = rg["controls"]["C2_dipole_pole_regate"][x]
        chk(f"regate dipole pole x={x} within 5%", c["within_5pct"],
            f"got {c['pole_margin']:+.6e} vs target {c['target']:+.6e} "
            f"(rel {c['rel_agreement']:.2e})")
    vf = load("wb_validate_fast.json")
    chk("fast path V1 grad identity < 1e-8", vf["V1_grad_ra_max_err"] < 1e-8,
        f"{vf['V1_grad_ra_max_err']:.2e}")
    chk("fast path V3 grid margins < 1e-7", vf["V3_grid_margin_agreement"]["max_abs_margin_diff"] < 1e-7,
        f"{vf['V3_grid_margin_agreement']['max_abs_margin_diff']:.2e}")

    audits = {}
    for x in (0.1, 0.2, 0.3):
        for L in (4, 6):
            try:
                audits[(x, L)] = load(f"wb_audit_x{x}_L{L}.json")
            except FileNotFoundError:
                chk(f"audit exists x={x} L={L}", False, "missing")
    for (x, L), a in sorted(audits.items()):
        chk(f"(a) Type-I everywhere x={x} L={L}", a["all_type_I"],
            f"min_disc {a['min_disc']:.3e}, n_grid {a['n_grid']}")
        tol = max(0.15 * PHASE[x], 3e-4)
        chk(f"(b) worst DEC x={x} L={L}", a["worst_margin"] > 0
            and abs(a["worst_margin"] - PHASE[x]) <= tol,
            f"got {a['worst_margin']:+.6e}, phase {PHASE[x]:+.6e}, tol {tol:.1e}")
        chk(f"(b-FD) FD binding read x={x} L={L}", a["fd_poles"]["bind"]["margin"] > 0
            and abs(a["fd_poles"]["bind"]["margin"] - PHASE[x]) <= tol,
            f"FD bind margin {a['fd_poles']['bind']['margin']:+.6e}")
        bind_ok = abs(a["theta_bind"] - BIND[x]) < 1e-9
        chk(f"(c) binding site x={x} L={L}", bind_ok,
            f"theta_bind {a['theta_bind']:.6f}, expected {BIND[x]:.6f}")
        chk(f"sampled-null > 0 x={x} L={L}", a["min_null"] > 0,
            f"min_null {a['min_null']:+.6e}")
        lad = [v["margin"] for v in a["ladder"].values()]
        chk(f"ladder all > 0 x={x} L={L}", all(v > 0 for v in lad),
            f"ladder margins {[f'{v:+.3e}' for v in lad]}")
    for x in (0.1, 0.2, 0.3):
        if (x, 4) in audits and (x, 6) in audits:
            s4 = np.sign(audits[(x, 4)]["worst_margin"])
            s6 = np.sign(audits[(x, 6)]["worst_margin"])
            chk(f"(e) L4/L6 sign agreement x={x}", s4 == s6 and s4 > 0,
                f"L4 {audits[(x, 4)]['worst_margin']:+.6e} vs "
                f"L6 {audits[(x, 6)]['worst_margin']:+.6e}")
    if (0.1, 6) in audits:
        a = audits[(0.1, 6)]
        for key in ("fd_closure_61", "max_h_audit_grid"):
            v = a[key]
            chk(f"(d) closure x=0.1 L=6 [{key}] within factor 2 of 1.5e-7",
                0.75e-7 <= v <= 3.0e-7, f"{v:.3e}")
    npass = sum(c["pass_"] for c in checks)
    out = dict(n=len(checks), n_pass=npass, all_pass=npass == len(checks),
               checks=checks)
    json.dump(out, open(os.path.join(RESULTS, "wb_check.json"), "w"), indent=1)
    for c in checks:
        print(f"{'PASS' if c['pass_'] else 'FAIL'}  {c['name']}  [{c['detail']}]")
    print(f"{npass}/{len(checks)} PASS")
    return 0 if out["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
