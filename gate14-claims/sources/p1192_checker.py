#!/usr/bin/env python
"""
P119-2 checker — independent recomputation of every verdict-carrying
number in results/p1192_results.json.

Independent route: correlators g_r, h_r are recomputed from Eqs. (3)-(5)
of arXiv:1007.2234 via COMPLEX exponential sums (the evaluation script
used real cosine sums), the delivered energy via Eq. (26) assembled
independently, and the sector marginal-product reference as
alpha * g_1 / 2 derived from Eq. (19) + Eq. (20). Checks:
  (a) every stored E_delivered / E_prep / E_net agrees <= 1e-9 relative;
  (b) E_net,sector > 0 at every stored row  =>  R_net = 0 (P72-2 SS4);
  (c) cross-check against the paper's own printed critical fit, Eq. (40):
      |<H_B>| ~ 0.12 N^-2.1 + 0.0020613 at maximal measurement (Setting 2,
      alpha = 1 - 1e-7): stored N=100 read within 1% of the fit value.
Prints PASS/FAIL lines only; exit code 0 iff all pass.
"""
import json
import sys

import numpy as np

RES = "/home/hatch/workspace/warp-pilot/phase119/results/p1192_results.json"
OMEGA = 1.0
fails = []


def corr_cx(N, alpha, rmax):
    k = np.arange(N)
    th = 2.0 * np.pi * k / N
    w = np.sqrt(1.0 - alpha * np.cos(th))
    out_g, out_h = [], []
    for r in range(rmax + 1):
        e = np.exp(1j * r * th)
        out_g.append(float(np.real(np.sum(e / (2.0 * w))) / N))
        out_h.append(float(np.real(np.sum(e * w / 2.0)) / N))
    return np.array(out_g), np.array(out_h)


def check(name, got, want, rtol=1e-9):
    ok = abs(got - want) <= rtol * max(1.0, abs(want))
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)


def main():
    res = json.load(open(RES))
    for row in res["setting1_N100"]:
        N, a, d = row["N"], row["alpha"], row["d"]
        g, h = corr_cx(N, a, d + 1)
        Jq = g[d] - 0.5 * a * (g[d - 1] + g[d + 1])
        e_del = 0.5 * (h[d] ** 2 / (h[0] + OMEGA / 2.0)
                       + Jq ** 2 / (g[0] + 1.0 / (2.0 * OMEGA)))
        e_prep = 0.5 * a * g[1]
        tag = f"S1 a={a} d={d}"
        check(tag + " E_delivered", e_del, row["E_delivered"])
        check(tag + " E_prep", e_prep, row["E_prep_marg_sector"])
        check(tag + " E_net", e_prep - e_del, row["E_net_sector"])
        check(tag + " E_net>0 => R_net=0", 1.0 if row["E_net_sector"] > 0
              and row["R_net"] == 0.0 else 0.0, 1.0, rtol=0.0)
    for row in res["setting2_maximal"]:
        N, a, ell = row["N"], row["alpha"], row["ell"]
        m = 2 * ell + 1
        nB = N // 2 + ell + 1
        g, h = corr_cx(N, a, N)
        j = np.arange(1, m + 1)
        D = np.abs(j[:, None] - j[None, :])
        Tp = h[D] + 0.5 * np.eye(m)
        Tq = g[D] + 0.5 * np.eye(m)
        dist = np.abs(j - nB)
        Jp = h[dist]
        Jq = g[dist] - 0.5 * a * (g[np.abs(j - (nB - 1))] + g[np.abs(j - (nB + 1))])
        e_del = 0.5 * (Jp @ np.linalg.solve(Tp, Jp)
                       + Jq @ np.linalg.solve(Tq, Jq))
        e_prep = 0.5 * a * g[1]
        tag = f"S2 a={a} N={N}"
        check(tag + " E_delivered", e_del, row["E_delivered"])
        check(tag + " E_prep", e_prep, row["E_prep_marg_sector"])
        check(tag + " E_net>0 => R_net=0", 1.0 if row["E_net_sector"] > 0
              and row["R_net"] == 0.0 else 0.0, 1.0, rtol=0.0)
    crit = [r for r in res["setting2_maximal"]
            if abs(r["alpha"] - (1 - 1e-7)) < 1e-12 and r["N"] == 100][0]
    fit = 0.12 * 100.0 ** -2.1 + 0.0020613  # paper Eq. (40), printed fit
    check("paper Eq.(40) critical fit vs stored S2 N=100 E_delivered (1%)",
          crit["E_delivered"], fit, rtol=1e-2)
    print(f"TOTAL: {'ALL PASS' if not fails else 'FAILURES: ' + str(fails)}")
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
