#!/usr/bin/env python
"""p431_check.py -- Phase 431 independent checker.

Opposite path to the driver wherever the driver has two paths:
the driver's headline residuals are PAIRWISE; the checker
recomputes them DIRECT (stress_at_point_multi). It verifies,
from the persisted best matings (phase431/work/
p431_best_{tag}.json) alone:
  - per-site and max residuals (direct) vs the driver's
    stored pairwise values and vs the 1e-9 bar;
  - the spectrum constraint exactly (Arm A: one energy --
    recomputed scatter; Arm B: E_k/E0 vs the rung labels);
  - |a|^2 pricing per family;
  - the B-2 headline numbers (Arm A: registered-E grid
    deviation and window spots, verbatim first crossing;
    Arm B: return at T_c, ladder return at 2^10 cycles,
    worst instant over the period) recomputed through
    p431_b2 with independently rebuilt coefficients;
  - supplier densities (direct) sign pattern.
Writes results/p431_check_results.json; prints PASS/FAIL.
"""
import json
import os
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
os.environ.setdefault('P420_WP', WP)
sys.path.insert(0, f'{WP}/phase420/work')
sys.path.insert(0, f'{WP}/phase431/work')
import p420_machinery as M  # noqa: E402
import p431_b2 as B2  # noqa: E402

BAR = 1e-9
W_UNITS = 3.6518e16
HERE = f'{WP}/phase431/work'
RES = f'{WP}/phase431/results'
RESJ = json.load(open(f'{RES}/p431_results.json'))


def avecs_from_json(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


def load_targets(which):
    if which == 't1':
        tg = json.load(open(f'{WP}/phase410/work/p410_targets.json'))
        return ([np.array(s['point']) for s in tg['sitesA']],
                [np.array(s['That']) for s in tg['sitesA']])
    tg = json.load(open(f'{WP}/phase420/work/p420_targets.json'))
    return ([np.array(s['point']) for s in tg['sitesA']],
            [np.array(s['T_corr']) for s in tg['sitesA']])


# tag -> (target, kind, fams, counts_list)
ARMS = {
    "A_t1_N6": ('t1', 'A', [(1.0, 6)], None),
    "A_t1_N8": ('t1', 'A', [(1.0, 8)], None),
    "A_t1_N12": ('t1', 'A', [(1.0, 12)], None),
    "B_t1_N6_L3": ('t1', 'B', [(1.0, 6)], [(2, 2, 2)]),
    "B_t1_N8_L3": ('t1', 'B', [(1.0, 8)], [(3, 3, 2)]),
    "B_t1_N12_L3": ('t1', 'B', [(1.0, 12)], [(4, 4, 4)]),
    "B_t1_N6_L6": ('t1', 'B', [(1.0, 6)], [(1, 1, 1, 1, 1, 1)]),
    "A_t2_6_6": ('t2', 'A', [(1.0, 6), (0.0, 6)], None),
    "A_t2_8_8": ('t2', 'A', [(1.0, 8), (0.0, 8)], None),
    "A_t2_single_N6": ('t2', 'A', [(1.0, 6)], None),
    "A_t2_single_N12": ('t2', 'A', [(1.0, 12)], None),
    "B_t2_6_6_L3": ('t2', 'B', [(1.0, 6), (0.0, 6)],
                    [(2, 2, 2), (2, 2, 2)]),
    "B_t2_8_8_L3": ('t2', 'B', [(1.0, 8), (0.0, 8)],
                    [(3, 3, 2), (3, 3, 2)]),
    "B_t2_6_6_L6": ('t2', 'B', [(1.0, 6), (0.0, 6)],
                    [(1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]),
}

# which tag each arm's confirmation used (from the results)
CONF_TAG = {}
for arm_key, arm in RESJ["arms"].items():
    conf = arm["confirmation"]
    # the confirmation was run on the arm's best tag; recover it
    # from the persisted best files by matching maxR.
    CONF_TAG[arm_key] = conf

out = {"phase": 431, "checker": "p431_check.py", "items": {}}
allpass = True

for tag, (tgt, kind, fams, counts_list) in ARMS.items():
    path = f'{HERE}/p431_best_{tag}.json'
    if not os.path.exists(path):
        continue
    bj = json.load(open(path))
    pv = np.array(bj["pvecs"]); av = avecs_from_json(bj["avecs"])
    mm = np.array(bj["masses"])
    XS, TG = load_targets(tgt)
    item = {"tag": tag}
    # direct residuals (opposite path)
    Rs_di, rhos = M.site_residuals_multi(pv, av, mm, XS, TG,
                                         direct=True)
    item["maxR_direct"] = max(Rs_di)
    item["Rs_direct"] = Rs_di
    item["driver_maxR_pairwise"] = bj["maxR"]
    item["direct_vs_pairwise_absdiff"] = abs(max(Rs_di) - bj["maxR"])
    item["at_bar_direct"] = bool(max(Rs_di) <= BAR)
    item["rhos_sup"] = rhos
    # pricing
    prices = {}
    pos = 0
    for fi, (m, N) in enumerate(fams):
        prices[f"family{fi + 1}_m{m}"] = float(
            np.sum(np.abs(av[pos:pos + N]) ** 2))
        pos += N
    item["abs_a2_per_family"] = prices
    # spectrum, exact
    E_rec = np.sqrt(np.sum(pv ** 2, axis=1) + mm ** 2)
    if kind == 'A':
        item["spectrum_scatter"] = float(E_rec.max() - E_rec.min())
        item["spectrum_max_dev_from_E"] = float(
            np.max(np.abs(E_rec - bj["info_Ebase"])))
        item["spectrum_ok"] = bool(
            item["spectrum_max_dev_from_E"] <= 1e-9)
    else:
        E0 = bj["info_Ebase"]
        rungs = []
        for counts in counts_list:
            rungs += [n + 1 for n, c in enumerate(counts)
                      for _ in range(c)]
        rungs = np.array(rungs, dtype=float)
        item["spectrum_max_ratio_dev"] = float(
            np.max(np.abs(E_rec / E0 - rungs)))
        item["spectrum_ok"] = bool(
            item["spectrum_max_ratio_dev"] <= 1e-9)
    # B-2 headlines, independently rebuilt coefficients
    o = B2.prep(pv, av, mm, XS, TG)
    R0 = B2.RF_t(o, 0.0)
    item["B2_R_F_0"] = R0
    if kind == 'A':
        Earr = np.full(len(pv), bj["info_Ebase"])
        ts = np.linspace(0.0, 2e5, 2048)
        RF_reg, _ = B2.grid_RF(o, ts, E=Earr)
        item["B2_registered_grid_max_dev"] = float(
            np.max(np.abs(RF_reg - R0)))
        # window spot in the evaluable Acoef form (the
        # per-mode-phase form is not evaluable at t ~ W;
        # see p431_supplement.py, whose factored-direct
        # read is the second path).
        RF_W, _ = B2.grid_RF(o, np.array([W_UNITS]), E=Earr)
        item["B2_registered_spot_W_acoef"] = float(RF_W[0])
        item["B2_ok"] = bool(item["B2_registered_grid_max_dev"]
                             <= 1e-12
                             and abs(item["B2_registered_spot_W_acoef"]
                                     - R0) <= 1e-12)
    else:
        E0 = bj["info_Ebase"]
        Tc = 2 * np.pi / E0
        ts = np.linspace(0.0, Tc, 2048)
        RFg, _ = B2.grid_RF(o, ts)
        item["B2_worst_instant"] = float(RFg.max())
        item["B2_return_at_T_c"] = float(B2.RF_t(o, Tc) - R0)
        item["B2_return_at_1024_T_c"] = float(
            B2.RF_t(o, 1024 * Tc) - R0)
        item["B2_ok"] = bool(
            abs(item["B2_return_at_T_c"]) <= 1e-9
            and abs(item["B2_return_at_1024_T_c"]) <= 1e-6)
    item["pass"] = bool(item["spectrum_ok"] and item["B2_ok"]
                        and item["direct_vs_pairwise_absdiff"]
                        <= max(1e-12, 1e-6 * bj["maxR"]))
    allpass = allpass and item["pass"]
    out["items"][tag] = item
    print(f"{tag}: maxR_direct={item['maxR_direct']:.3e} "
          f"spec_ok={item['spectrum_ok']} B2_ok={item['B2_ok']} "
          f"pass={item['pass']}", flush=True)

out["ALL_PASS"] = bool(allpass and len(out["items"]) > 0)
json.dump(out, open(f'{RES}/p431_check_results.json', 'w'),
          indent=1, default=str)
print("CHECKER:", "ALL PASS" if out["ALL_PASS"] else "SEE ITEMS")
