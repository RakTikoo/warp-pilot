#!/usr/bin/env python3
"""
g34_item1.py -- Gate-34 Item 1: independent re-read of the
broad-ramp m0 = +1.0 member with the gate assembly.

SET-244 read (gate tensors + protocol SAMPLER-M margins),
gate adversary polish, site re-derivation under Phase
293's rule, per-site reads at BOTH the gate-derived sites
and Phase 312's stored sites.
"""
import json
import numpy as np
import sys
from scipy.optimize import minimize

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase235/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate34/work')
import g34_lib as G
from p2352_run import margins_chunked

OUT = {}

# ------------------------------------------------ SET-244 read
rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec', 'rho')}
all_pts = []
for rr in G.R_NODES:
    pts = G.DIRS162 * rr
    T, g = G.einstein(pts)
    That = G.eulerian_that(g, T)
    m = margins_chunked(That)
    rec['typeI'].append(m['typeI']); rec['nec'].append(m['nec'])
    rec['wec'].append(m['wec']); rec['dec'].append(m['dec'])
    rec['sec'].append(m['sec']); rec['rho'].append(That[:, 0, 0])
    all_pts.append(pts)
P = np.vstack(all_pts)
R = {k: np.concatenate(v) for k, v in rec.items()}
radii = np.linalg.norm(P, axis=1)


def st(a):
    return {'min': float(np.min(a)), 'median': float(np.median(a)),
            'max': float(np.max(a))}
OUT['set'] = {'n_points': int(len(P)),
              'typeI_count': int(np.sum(R['typeI'])),
              'typeI_fraction': float(np.mean(R['typeI'])),
              'nec': st(R['nec']), 'wec': st(R['wec']),
              'dec': st(R['dec']), 'sec': st(R['sec']),
              'rho': st(R['rho'])}

# ------------------------------------------------ site derivation
iS2 = int(np.argmin(R['nec']))
ti = np.where(R['typeI'])[0]
iS3 = int(ti[np.argmin(R['nec'][ti])])
outer = np.where(radii >= 15.0)[0]
iS4 = int(outer[np.argmin(R['nec'][outer])])


def nec_at(pt):
    T, g = G.einstein(np.asarray(pt)[None, :])
    That = G.eulerian_that(g, T)
    m = margins_chunked(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def polish():
    order = ti[np.argsort(R['nec'][ti])[:5]]
    best = None
    starts = []
    for i in order:
        p0 = P[i]
        r0 = float(np.linalg.norm(p0))
        x0 = np.array([r0, np.arccos(np.clip(p0[2] / r0, -1, 1)),
                       np.arctan2(p0[1], p0[0])])

        def objective(x):
            rr, th, ph = x
            if rr < 10.0 or rr > 20.0:
                return 1.0
            pt = rr * np.array([np.sin(th) * np.cos(ph),
                                np.sin(th) * np.sin(ph), np.cos(th)])
            nec, is_ti, _ = nec_at(pt)
            return nec if is_ti else nec + 1.0
        res = minimize(objective, x0, method='Nelder-Mead',
                       options={'maxiter': 300, 'xatol': 1e-4,
                                'fatol': 1e-7})
        rr, th, ph = res.x
        pt = rr * np.array([np.sin(th) * np.cos(ph),
                            np.sin(th) * np.sin(ph), np.cos(th)])
        nec, is_ti, _ = nec_at(pt)
        starts.append({'start_r': r0, 'polished_point': pt.tolist(),
                       'polished_r': float(rr),
                       'polished_nec': nec, 'polished_typeI': is_ti})
        if is_ti and (best is None or nec < best['nec']):
            best = {'point': pt, 'nec': nec}
    return best, starts


best_pol, pol_starts = polish()
OUT['polish'] = {'starts': pol_starts,
                 'best_nec': None if best_pol is None
                 else best_pol['nec'],
                 'best_point': None if best_pol is None
                 else best_pol['point'].tolist(),
                 'best_r': None if best_pol is None
                 else float(np.linalg.norm(best_pol['point']))}
depth = best_pol['nec']

# ------------------------------------------------ per-site reads
def site_read(pt):
    pt = np.asarray(pt, dtype=float)
    T, g = G.einstein(pt[None, :])
    That = G.eulerian_that(g, T)[0]
    m = margins_chunked(That[None])
    n_fin, nec_exact = G.worst_null(That)
    sp = G.rho_split(pt[None, :])
    return {'point': pt.tolist(),
            'r': float(np.linalg.norm(pt)),
            'rho_req': float(That[0, 0]),
            'nec_SAMPLER-M': float(m['nec'][0]),
            'nec_exact_pointwise': float(nec_exact),
            'typeI': bool(m['typeI'][0]),
            'split': {k: float(sp[k][0]) for k in
                      ('R_over_16pi', 'R1_over_16pi', 'R2_over_16pi',
                       'QK_over_16pi')}}

gate_sites = {'S1': best_pol['point'], 'S2': P[iS2], 'S3': P[iS3],
              'S4': P[iS4]}
OUT['gate_sites'] = {k: site_read(v) for k, v in gate_sites.items()}
OUT['depth_gate'] = float(depth)

p312 = json.load(open('/home/hatch/workspace/warp-pilot/'
                      'phase312/results/p312_results.json'))
member = [m for m in p312['members']
          if m['label'] == 'ramp_broad_m+1.00'][0]
OUT['stored_sites_reread'] = {
    s['key']: site_read(np.array(s['point']))
    for s in member['sites']}
OUT['stored'] = {
    'depth': member['depth_SAMPLER-M_polished'],
    'set_rho_min': member['set']['rho']['min'],
    'set_nec_min': member['set']['nec']['min'],
    'typeI_count': member['set']['typeI_count']}

print(json.dumps(OUT, indent=1))
json.dump(OUT, open('/home/hatch/workspace/warp-pilot/gate34/'
                    'results/g34_item1.json', 'w'), indent=1)
