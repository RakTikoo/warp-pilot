#!/usr/bin/env python3
"""
g34_item2.py -- Gate-34 Item 2: adversary read over the
winner's volume, hunting rho_req < 0 loci that are
binding-grade candidates the site rule never selects.

Dense scan: 201 radial nodes x 642 Fibonacci dirs on
[10,20]; per point rho, Type-I flag, fib-642 exact NEC
min (unpolished). Then continuum polishes and the
threshold audit fixed in the registration:
  (a) SAMPLER-M NEC <= -3.126870e-3 (S2's stored value)
  (b) exact pointwise NEC <= -3.517021e-3 (S3's stored)
  (c) SAMPLER-M NEC <= depth -1.180275e-3 AND Type-I
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

K642 = np.concatenate([np.ones((642, 1)), G.DIRS642], axis=1)
RAD = np.linspace(10.0, 20.0, 201)

rho_l, nec_l, ti_l, pts_l = [], [], [], []
for rr in RAD:
    pts = G.DIRS642 * rr
    T, g = G.einstein(pts)
    That = G.eulerian_that(g, T)
    TK = np.einsum('pab,kb->pka', That, K642)
    vals = np.einsum('pka,ka->pk', TK, K642)
    rho_l.append(That[:, 0, 0])
    nec_l.append(np.min(vals, axis=1))
    ti_l.append(G.typeI_flag(That))
    pts_l.append(pts)
rho = np.concatenate(rho_l); nec = np.concatenate(nec_l)
ti = np.concatenate(ti_l); P = np.vstack(pts_l)
radii = np.linalg.norm(P, axis=1)
np.savez('/home/hatch/workspace/warp-pilot/gate34/results/'
         'g34_item2_scan.npz', rho=rho, nec_fib=nec, typeI=ti,
         pts=P)

OUT = {'scan': {'n_points': int(len(P)),
                'rho_min': float(np.min(rho)),
                'rho_min_point': P[int(np.argmin(rho))].tolist(),
                'rho_min_r': float(radii[int(np.argmin(rho))]),
                'n_rho_neg': int(np.sum(rho < 0)),
                'nec_fib_min': float(np.min(nec)),
                'nec_fib_min_point': P[int(np.argmin(nec))].tolist(),
                'nec_fib_min_rho': float(rho[int(np.argmin(nec))])}}

neg = rho < 0
OUT['neg_rho_loci'] = {
    'count': int(np.sum(neg)),
    'r_range': [float(np.min(radii[neg])), float(np.max(radii[neg]))]
    if np.any(neg) else None,
    'most_binding_fib_nec': float(np.min(nec[neg]))
    if np.any(neg) else None,
    'most_binding_point': P[neg][int(np.argmin(nec[neg]))].tolist()
    if np.any(neg) else None,
    'most_binding_rho': float(rho[neg][int(np.argmin(nec[neg]))])
    if np.any(neg) else None,
    'min_rho': float(np.min(rho[neg])) if np.any(neg) else None}


def nec_at(pt):
    T, g = G.einstein(np.asarray(pt)[None, :])
    That = G.eulerian_that(g, T)
    m = margins_chunked(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def sph(pt):
    r = float(np.linalg.norm(pt))
    return np.array([r, np.arccos(np.clip(pt[2] / r, -1, 1)),
                     np.arctan2(pt[1], pt[0])])


def unsph(x):
    rr, th, ph = x
    return rr * np.array([np.sin(th) * np.cos(ph),
                          np.sin(th) * np.sin(ph), np.cos(th)])


def polish_min(func, starts, maxiter=400):
    best = None
    for x0 in starts:
        res = minimize(func, x0, method='Nelder-Mead',
                       options={'maxiter': maxiter, 'xatol': 1e-5,
                                'fatol': 1e-9})
        if best is None or res.fun < best.fun:
            best = res
    return best


# ---- polish 1: minimise exact NEC among rho<0 region starts
def obj_nec_exact(x):
    if x[0] < 10.0 or x[0] > 20.0:
        return 1.0
    pt = unsph(x)
    T, g = G.einstein(pt[None, :])
    That = G.eulerian_that(g, T)[0]
    _, v = G.worst_null(That)
    return v

idx_neg_sorted = np.where(neg)[0][np.argsort(nec[neg])[:5]] \
    if np.any(neg) else []
starts = [sph(P[i]) for i in idx_neg_sorted]
res_nec = polish_min(obj_nec_exact, starts) if starts else None
if res_nec is not None:
    pt = unsph(res_nec.x)
    T, g = G.einstein(pt[None, :])
    That = G.eulerian_that(g, T)[0]
    nm, is_ti, _ = nec_at(pt)
    OUT['polish_exact_nec_from_neg'] = {
        'point': pt.tolist(), 'r': float(np.linalg.norm(pt)),
        'exact_nec': float(res_nec.fun), 'rho': float(That[0, 0]),
        'nec_SAMPLER-M': nm, 'typeI': is_ti}

# ---- polish 2: minimise rho over the volume
def obj_rho(x):
    if x[0] < 10.0 or x[0] > 20.0:
        return 1.0
    pt = unsph(x)
    T, g = G.einstein(pt[None, :])
    That = G.eulerian_that(g, T)[0]
    return float(That[0, 0])

imin = int(np.argmin(rho))
res_rho = polish_min(obj_rho, [sph(P[imin])])
pt = unsph(res_rho.x)
T, g = G.einstein(pt[None, :])
That = G.eulerian_that(g, T)[0]
_, v_exact = G.worst_null(That)
nm, is_ti, _ = nec_at(pt)
OUT['polish_rho_min'] = {'point': pt.tolist(),
                         'r': float(np.linalg.norm(pt)),
                         'rho': float(res_rho.fun),
                         'exact_nec': float(v_exact),
                         'nec_SAMPLER-M': nm, 'typeI': is_ti}

# ---- polish 3: minimise SAMPLER-M NEC over the volume
def obj_nec_m(x):
    if x[0] < 10.0 or x[0] > 20.0:
        return 1.0
    nm, _, _ = nec_at(unsph(x))
    return nm

order = np.argsort(nec)[:5]
res_m = polish_min(obj_nec_m, [sph(P[i]) for i in order])
pt = unsph(res_m.x)
T, g = G.einstein(pt[None, :])
That = G.eulerian_that(g, T)[0]
_, v_exact = G.worst_null(That)
OUT['polish_samplerM_nec_min'] = {
    'point': pt.tolist(), 'r': float(np.linalg.norm(pt)),
    'nec_SAMPLER-M': float(res_m.fun), 'rho': float(That[0, 0]),
    'exact_nec': float(v_exact)}

# ---- threshold audit on the dense scan
# SAMPLER-M NEC for scan points in the near-binding classes:
cand = np.where(neg & (nec <= -1.0e-3))[0]
OUT['threshold_audit'] = {'n_neg_and_fibnec_le_-1e-3': int(len(cand))}
if len(cand):
    Thats = []
    for s in range(0, len(cand), 1024):
        idx = cand[s:s + 1024]
        T, g = G.einstein(P[idx])
        Thats.append(G.eulerian_that(g, T))
    That_c = np.vstack(Thats)
    m = margins_chunked(That_c)
    necM_c = m['nec']; ti_c = m['typeI']
    a = necM_c <= -3.126870e-3
    b = nec[cand] <= -3.517021e-3
    c = (necM_c <= -1.180275e-3) & ti_c
    OUT['threshold_audit'].update({
        'cand_rho_range': [float(np.min(rho[cand])),
                           float(np.max(rho[cand]))],
        'a_hits': int(np.sum(a)), 'b_hits': int(np.sum(b)),
        'c_hits': int(np.sum(c)),
        'cand_min_necM': float(np.min(necM_c)),
        'cand_min_necM_rho': float(rho[cand][int(np.argmin(necM_c))]),
        'cand_min_fibnec': float(np.min(nec[cand]))})
    for name, hits in (('a', a), ('b', b), ('c', c)):
        if np.any(hits):
            j = np.where(hits)[0]
            OUT['threshold_audit'][f'{name}_loci'] = [
                {'point': P[cand[t]].tolist(),
                 'rho': float(rho[cand[t]]),
                 'nec_SAMPLER-M': float(necM_c[t]),
                 'nec_fib': float(nec[cand[t]]),
                 'typeI': bool(ti_c[t])} for t in j[:10]]

print(json.dumps(OUT, indent=1))
json.dump(OUT, open('/home/hatch/workspace/warp-pilot/gate34/'
                    'results/g34_item2.json', 'w'), indent=1)
