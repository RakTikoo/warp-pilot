#!/usr/bin/env python
"""P420 laptop admission + primary cross-check (registration SS6).

Run on the VM and on the laptop (inside the minimal mirror) and
compare the printed values. Two parts:
 (a) admission: Phase 405's set_read405 at the 405 winner's
     stored knots (Phase 410's admission pattern, its exact
     call form) — joint, sec_min, rho_min and the argmin radii;
 (b) primary cross-check: the C-A primary's DIRECT residuals
     against the corrected targets, recomputed from the stored
     primary + stored corrected targets on the executing
     machine.
WP root from env P420_WP (the mirror root on the laptop; the
real tree on the VM); P405_WP follows it.
"""
import json
import os
import sys

WP = os.environ.get('P420_WP', '/home/hatch/workspace/warp-pilot')
os.environ.setdefault('P405_WP', WP)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{WP}/phase420/work')
sys.path.insert(0, f'{WP}/phase405/work')

import numpy as np  # noqa: E402
import p405_lib as L405  # noqa: E402
import p420_machinery as M  # noqa: E402


def avecs_from_json(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


out = {}
vS = np.array(json.load(open(f'{WP}/phase410/work/'
                             'p410_winner_knots.json')),
              dtype=L405.DTYPE)
s, _aux = L405.set_read405(vS, 9)
out["set_read405"] = {
    'joint': float(L405.joint_of_read(s)),
    'nec_min': float(s['nec']['min']), 'dec_min': float(s['dec']['min']),
    'wec_min': float(s['wec']['min']), 'sec_min': float(s['sec']['min']),
    'rho_min': float(s['rho']['min']),
    'nec_argmin_r': float(s['nec_argmin_r']),
    'dec_argmin_r': float(s['dec_argmin_r']),
    'typeI_fraction': float(s['typeI_fraction'])}
print("SET_READ405:", json.dumps(out["set_read405"]), flush=True)

tg = json.load(open(f'{WP}/phase420/work/p420_targets.json'))
prim = json.load(open(f'{WP}/phase420/work/p420_fitCA_primary.json'))
XS = [np.array(s2["point"]) for s2 in tg["sitesA"]]
TC = [np.array(s2["T_corr"]) for s2 in tg["sitesA"]]
pv, av, mm = M.join_modes(np.array(prim["pvecs1"]),
                          avecs_from_json(prim["avecs1"]), prim["m1"],
                          np.array(prim["pvecs2"]),
                          avecs_from_json(prim["avecs2"]), prim["m2"])
Rs, rhos = M.site_residuals_multi(pv, av, mm, XS, TC, direct=True)
out["primary_direct"] = {"Rs": Rs, "maxR": max(Rs), "rhos": rhos,
                         "abs_a2_family1": float(np.sum(
                             np.abs(avecs_from_json(prim["avecs1"])) ** 2)),
                         "abs_a2_family2": float(np.sum(
                             np.abs(avecs_from_json(prim["avecs2"])) ** 2))}
print("PRIMARY_DIRECT:", json.dumps(out["primary_direct"]), flush=True)
json.dump(out, open(os.path.join(HERE, 'p420_admission_local.json'), "w"),
          indent=1)
