"""
wb_regate.py — GATE-10 W-B machinery re-gate (BEFORE any multipole number).

Controls:
 (C1) static anchor: wb machinery at lam=0, zero coefficients reproduces the
      paper's Eqs.(22)-(23) sigma0, p0 (closed form) at x in {0.1, 0.3, 0.5}.
 (C2) DIPOLE re-gate (the registered Gate-10 anchor): the fresh auditor,
      applied to the paper's dipole construction (Phase 71's stored dipole
      dof, L=1 layout, Ai=wi=0), must reproduce Phase 71's dipole pole
      values at th=pi: -2.0096e-4 (x=0.1, lam=0.19) and -1.2263e-4
      (x=0.3, lam=0.19), within 5%.
 (C3) dipole [h] residual at (0.1, 0.19) is O(lam^2)-sized (paper: 1-10% of
      lam) — the mismatch the multipole solve exists to remove.
Output: results/wb_regate.json
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb_lib as W

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results", "wb_regate.json")
P715 = os.path.expanduser("~/workspace/warp-pilot/phase71/results/p715_results.json")

TARGETS = {0.1: -2.0096e-4, 0.3: -1.2263e-4}
PINS = {0.1: 0.19, 0.3: 0.19}


def dipole_p(dof):
    """L=1 parameter vector in the published layout [rho, At, w, wi, Ai]."""
    return np.array([dof["rho1"], dof["At1"], dof["w1"], 0.0, 0.0], dtype=W.DTYPE)


def pole_margin(x, lam, p, L, h=0.01, order=2):
    r = W.sample_shell(x, lam, p, L, [np.pi], h=h, order=order)
    s = W.lanczos(r["KP"][0], r["KM"][0])
    m, t = W.phi_HE(*s)
    return m, t, s


def main():
    t0 = time.time()
    res = {"interpreter": sys.executable, "controls": {}}

    # C1 static anchor
    c1 = {}
    for x in (0.1, 0.3, 0.5):
        r = W.sample_shell(x, 0.0, np.zeros(10), 2, [0.7, 1.4, 2.2])
        sigs, ps = [], []
        for i in range(3):
            s = W.lanczos(r["KP"][i], r["KM"][i])
            sigs.append(s[0]); ps.append(s[1])
        s0, p0 = W.anchor_closed(x)
        c1[str(x)] = dict(sigma=float(np.mean(sigs)), sigma_exact=s0,
                          sigma_err=float(abs(np.mean(sigs) - s0)),
                          p=float(np.mean(ps)), p_exact=p0,
                          p_err=float(abs(np.mean(ps) - p0)))
    res["controls"]["C1_static_anchor"] = c1

    # C2 dipole pole re-gate (stored Phase-71 dof = the dipole construction)
    stored = json.load(open(P715))
    c2 = {}
    for x, lam in PINS.items():
        dof = stored["frontier"][str(x)]["dof"]
        p = dipole_p(dof)
        m, t, s = pole_margin(x, lam, p, 1)
        # h-ladder + 4th order at the pole
        ladder = {}
        for hh, oo in ((0.02, 2), (0.01, 2), (0.005, 2), (0.01, 4)):
            mm, _, _ = pole_margin(x, lam, p, 1, h=hh, order=oo)
            ladder[f"h{hh}_o{oo}"] = mm
        tgt = TARGETS[x]
        c2[str(x)] = dict(lam=lam, dof={k: dof[k] for k in ("rho1", "At1", "w1")},
                          pole_margin=m, pole_type=t, stress=list(s),
                          ladder=ladder, target=tgt,
                          rel_agreement=float(abs(m - tgt) / abs(tgt)),
                          within_5pct=bool(abs(m - tgt) / abs(tgt) <= 0.05))
    res["controls"]["C2_dipole_pole_regate"] = c2

    # C3 dipole closure residual size at (0.1, 0.19)
    dof = stored["frontier"]["0.1"]["dof"]
    p = dipole_p(dof)
    ths = np.linspace(0.2, np.pi - 0.2, 21)
    r = W.sample_shell(0.1, 0.19, p, 1, ths)
    dh = r["hP"] - r["hM"]
    maxh = float(np.max(np.abs(dh)))
    res["controls"]["C3_dipole_residual"] = dict(max_h=maxh,
                                                 frac_of_lam=float(maxh / 0.19))
    res["seconds"] = time.time() - t0
    res["regate_pass"] = bool(all(v["within_5pct"] for v in c2.values()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(res, open(OUT, "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
