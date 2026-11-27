#!/usr/bin/env python3
"""
g52_polish.py -- Gate-52 adversary polishes (the registered
SAMPLER-M polish protocol, re-run on gate machinery) plus
the claim-(b) supplementary frame-robustness reads.
Protocol (the lineage's registered form): Nelder-Mead on
(r, theta, phi) from the five lowest Type-I SET points,
objective = NEC margin, +1 penalty at non-Type-I points,
maxiter 300, xatol 1e-4, fatol 1e-7; the reported value is
the best polished Type-I NEC (SAMPLER-M).
Output: gate52/results/g52_polish.json.
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g52_lib as G   # noqa: E402

WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
OUT = f'{WP}/gate52/results/g52_polish.json'
out = {}


def typeI_points(vS, K):
    """My SET read's Type-I points with their NEC values."""
    pts_all, nec_all, ti_all = [], [], []
    for rr in G.R_NODES:
        pts = G.DIRS162 * rr
        That = G.that_at(vS, K, pts)
        m = G.hawking_ellis_margins(That)
        pts_all.append(pts)
        nec_all.append(m['nec'])
        ti_all.append(m['typeI'])
    pts = np.vstack(pts_all)
    nec = np.concatenate(nec_all)
    ti = np.concatenate(ti_all)
    return pts[ti], nec[ti]


def adversary_polish(vS, K):
    pts_ti, nec_ti = typeI_points(vS, K)
    if len(pts_ti) == 0:
        return None
    rr_ti = np.linalg.norm(pts_ti, axis=1)

    def objective(x):
        rr, th, ph = x
        if rr < 10.0 or rr > 20.0:
            return 1.0
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = G.nec_at_point(vS, K, pt)
        return nec if is_ti else nec + 1.0

    order = np.argsort(nec_ti)[:5]
    polished = []
    for i in order:
        p0 = pts_ti[i]
        r0 = float(np.linalg.norm(p0))
        x0 = np.array([r0, np.arccos(np.clip(p0[2] / r0, -1, 1)),
                       np.arctan2(p0[1], p0[0])])
        res = minimize(objective, x0, method='Nelder-Mead',
                       options={'maxiter': 300, 'xatol': 1e-4,
                                'fatol': 1e-7})
        rr, th, ph = res.x
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = G.nec_at_point(vS, K, pt)
        polished.append({'start_set_nec': float(nec_ti[i]),
                         'polished_point': pt.tolist(),
                         'polished_r': float(rr),
                         'polished_nec_SAMPLER-M': nec,
                         'polished_typeI': bool(is_ti)})
    cand = [p for p in polished if p['polished_typeI']]
    if cand:
        best_p = min(cand, key=lambda p: p['polished_nec_SAMPLER-M'])
        site_pt = np.array(best_p['polished_point'], dtype=G.DT)
        source = 'polished'
    else:
        i0 = int(order[0])
        site_pt = pts_ti[i0]
        best_p = None
        source = 'set_argmin_fallback'
    nec_site, is_ti_site, _ = G.nec_at_point(vS, K, site_pt)
    return {'source': source, 'point': site_pt.tolist(),
            'r': float(np.linalg.norm(site_pt)),
            'typeI': bool(is_ti_site),
            'in_region_worst_nec_SAMPLER-M': nec_site,
            'polished': polished, 'best_polished': best_p}


out['crit_polish'] = adversary_polish(G.SHAPEC_CRIT, 9)
out['crit_polish_stored'] = 1.214723699102956e-06
print('crit polish:', out['crit_polish']
      ['in_region_worst_nec_SAMPLER-M'], flush=True)

out['m2_polish'] = adversary_polish(G.M2_VS, 9)
out['m2_polish_stored'] = 6.489725143840711e-07
out['m2_polish_stored_r'] = 18.09150031104932
print('m2 polish:', out['m2_polish']
      ['in_region_worst_nec_SAMPLER-M'], 'at r',
      out['m2_polish']['r'], flush=True)

out['m5k17_polish'] = adversary_polish(G.M5K17_VS, 17)
out['m5k17_polish_stored'] = -1.775824194571974e-05
out['m5k17_polish_stored_r'] = 19.999998212961863
print('m5 polish:', out['m5k17_polish']
      ['in_region_worst_nec_SAMPLER-M'], 'at r',
      out['m5k17_polish']['r'], flush=True)

# ---- claim (b) supplements: pin the sampled argmin's
# location story and the Type-I companions on gate reads.
supp = {}
for tag, vs, K in (('K17', G.M5K17_VS, 17), ('K9', G.M5K9_VS, 9)):
    s, R = G.set_read(vs, K)
    i_dir = s['nec_argmin_dir_index']
    rows = {}
    for rr in (15.0, 15.24390243902439):
        pt = G.DIRS162[i_dir] * rr
        nec, is_ti, That = G.nec_at_point(vs, K, pt)
        wn = G.worst_null_certified(That)
        rows[f'r={rr}'] = {
            'point': pt.tolist(), 'nec_SAMPLER-M': nec,
            'typeI': bool(is_ti),
            'worst_null': wn['worst_null'],
            'worst_null_certified': wn['certified']}
    # Type-I NEC argmin point of the gate read
    ti_idx = np.where(R['typeI'])[0]
    j = ti_idx[int(np.argmin(R['nec'][ti_idx]))]
    jr, jd = divmod(int(j), 162)
    pt_ti = G.DIRS162[jd] * G.R_NODES[jr]
    nec_ti, _, That_ti = G.nec_at_point(vs, K, pt_ti)
    wn_ti = G.worst_null_certified(That_ti)
    rows['typeI_nec_argmin'] = {
        'point': pt_ti.tolist(), 'r': float(G.R_NODES[jr]),
        'dir_index': int(jd), 'nec': nec_ti,
        'worst_null': wn_ti['worst_null'],
        'worst_null_certified': wn_ti['certified']}
    supp[tag] = rows
out['claim_b_supplements'] = supp

with open(OUT, 'w') as f:
    json.dump(out, f, indent=1)
print('wrote', OUT)
