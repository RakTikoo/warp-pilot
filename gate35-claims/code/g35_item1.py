#!/usr/bin/env python3
"""
g35_item1.py -- Gate-35 ITEM 1 driver: SET READ -> CONTINUUM adversary
search on the Phase 314 headline member, per g35_registration.md (b)-(d).

Sequence: C-G1 control FIRST (evaluator vs stored S1-S4 splits and the
stored SET-244 rho minimum); structural-reduction verification (b); radial
adversary (c); margin floors (d). Writes g35_item1_results.json.
float64. No p312/p314/p308 lib imports.
"""
import json
import sys

import numpy as np
from scipy.optimize import minimize_scalar

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate35/work')
from g35_rho import (M_funcs, profiles_SN, rho_ru, rho_split, rho_star)  # noqa: E402

WP = '/home/hatch/workspace/warp-pilot'
OUT = {}
rng = np.random.default_rng(20261124)

# ============================================================ C-G1 control
stored = json.load(open(f'{WP}/phase314/results/p314_results.json'))
hm = stored['headline_member']
cg1 = {'sites': []}
for site in hm['sites']:
    r = site['r']
    u = site['n_xhat'] ** 2
    sp = rho_split(r, u)
    row = {'key': site['key'], 'r': r, 'n_xhat': site['n_xhat']}
    for mine, theirs in (('R1', 'R1_over_16pi'), ('R2', 'R2_over_16pi'),
                         ('QK', 'QK_over_16pi'), ('rho', 'rho_req')):
        got = float(sp[mine])
        want = float(site[theirs])
        rel = abs(got - want) / abs(want) if want != 0 else abs(got - want)
        row[mine] = {'got': got, 'stored': want, 'rel_diff': rel}
    row['M_got'] = float(sp['M'])
    row['Mp_got'] = float(sp['Mp'])
    row['M_stored'] = site['M']
    row['Mp_stored'] = site['Mp']
    cg1['sites'].append(row)
cg1['max_rel_diff'] = max(row[k]['rel_diff'] for row in cg1['sites']
                          for k in ('R1', 'R2', 'QK', 'rho'))
# stored SET-244 rho minimum at its stored argmin locus (memo S3:
# r = 19.878049 = outermost midpoint node 10 + 40.5*10/41, n_xhat = +0.0041)
r_node = 10.0 + 40.5 * (10.0 / 41.0)
set_min_stored = hm['set']['rho']['min']
ev = rho_split(r_node, 0.0041 ** 2)
rs_node, u_node = rho_star(r_node)
cg1['set_min'] = {
    'r_node': r_node, 'n_xhat_memo': 0.0041,
    'rho_at_memo_locus': float(ev['rho']),
    'split_at_memo_locus': {k: float(ev[k]) for k in ('R1', 'R2', 'QK')},
    'rho_star_at_node': rs_node, 'u_star_at_node': u_node,
    'stored_set_min': set_min_stored,
    'rel_diff_at_memo_locus': abs(float(ev['rho']) - set_min_stored)
    / set_min_stored,
    'rel_diff_rho_star': abs(rs_node - set_min_stored) / set_min_stored}
cg1['pass_1e-9_sites'] = bool(cg1['max_rel_diff'] <= 1e-9)
OUT['control_CG1'] = cg1
print(f"C-G1 sites max rel diff: {cg1['max_rel_diff']:.3e}")
print(f"C-G1 set-min: at memo locus {cg1['set_min']['rho_at_memo_locus']:.9e} "
      f"(rel {cg1['set_min']['rel_diff_at_memo_locus']:.2e}); "
      f"rho* at node {rs_node:.9e} (rel {cg1['set_min']['rel_diff_rho_star']:.2e}) "
      f"vs stored {set_min_stored:.9e}")

# ============================================ (b) structural verification
# (i) evaluator sees only (r, u): rotating a direction about the x-axis at
# fixed n_x leaves u (hence rho) identical -- verified by construction of
# rotated samples; (ii) the substantive check: (16pi*rho - R) * alpha^2 /
# beta^2 (the Q_K numerator) is affine in u, and alpha^2 is affine in u,
# at ~50 random (r, direction) samples; (iii) rho(u) monotonicity spot
# check (ratio of affine functions) on the same samples.
samples = []
max_affine_dev = 0.0
max_mono_viol = 0.0
for _ in range(50):
    r = float(rng.uniform(10.0, 20.0))
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    theta = float(rng.uniform(0.0, 2.0 * np.pi))
    nrot = np.array([n[0],
                     n[1] * np.cos(theta) - n[2] * np.sin(theta),
                     n[1] * np.sin(theta) + n[2] * np.cos(theta)])
    u0, u1 = float(n[0] ** 2), float(nrot[0] ** 2)
    assert abs(u0 - u1) < 1e-15
    # Q_K numerator at u = 0, 1/2, 1 from the evaluator's pieces:
    def qk_num(uu):
        sp = rho_split(r, uu)
        return (float(sp['QK']) * 16.0 * np.pi
                * float(sp['alpha2']) / 1.1 ** 2)
    dev = abs(qk_num(0.5) - 0.5 * (qk_num(0.0) + qk_num(1.0)))
    scale = max(abs(qk_num(0.0)), abs(qk_num(1.0)), 1e-30)
    max_affine_dev = max(max_affine_dev, dev / scale)
    a0 = float(rho_split(r, 0.0)['alpha2'])
    a5 = float(rho_split(r, 0.5)['alpha2'])
    a1 = float(rho_split(r, 1.0)['alpha2'])
    max_affine_dev = max(max_affine_dev,
                         abs(a5 - 0.5 * (a0 + a1)) / max(abs(a0), 1e-30))
    us = np.linspace(0.0, 1.0, 401)
    vals = rho_ru(r, us)
    d = np.diff(vals)
    if np.any(d > 0) and np.any(d < 0):
        max_mono_viol = max(max_mono_viol,
                            float(min(np.max(np.abs(d)), 1.0)))
        samples.append({'r': r, 'nonmonotone': True})
OUT['structural_b'] = {
    'n_samples': 50,
    'max_affine_dev_rel (QK numerator & alpha2 in u)': max_affine_dev,
    'nonmonotone_samples': len(samples),
    'statement': ('rho depends on the direction only through u = n_xhat^2: '
                  'R1, R2 are functions of (r, M, M\') only; the Q_K '
                  'numerator pieces carry (1-u) in term 1 and u in terms '
                  '2-4 and nothing else directional; alpha^2 carries u '
                  'linearly and nothing else directional. Hence rho(u) at '
                  'fixed r is a ratio of affine functions of u (monotonic), '
                  'and rho*(r) = min over u in [0,1] is the exact angular '
                  'minimum; rotation about the x-axis at fixed n_xhat '
                  'leaves the evaluator input (r, u) unchanged.')}
print(f"(b) affine dev {max_affine_dev:.3e}; nonmonotone samples "
      f"{len(samples)}/50")

# ============================================================ (c) adversary
DR = 0.01
U_SCAN = np.linspace(0.0, 1.0, 2001)

def mesh_rho_star(r_arr):
    """rho* on an array of radii via ONE broadcast (r x u) evaluation of the
    gate evaluator on the registered 2001-point u-scan; u* = scan argmin
    (golden polish of rho* in r below refines the radial locus; the angular
    minimum is at a u endpoint by the verified monotonicity, and the scan
    argmin confirms it per radius)."""
    vals = rho_ru(np.asarray(r_arr)[:, None], U_SCAN[None, :])
    i = np.argmin(vals, axis=1)
    return vals[np.arange(len(r_arr)), i], U_SCAN[i]

def fast_rho_star(r):
    """rho*(r) for the radial polisher: by the (b)-verified structure
    (Q_K numerator and alpha^2 affine in u => rho monotonic in u), the
    angular minimum is min(rho(r,0), rho(r,1)). Every polished result is
    cross-checked against the full scan-based rho_star before recording."""
    v0 = float(rho_ru(r, 0.0))
    v1 = float(rho_ru(r, 1.0))
    return (v0, 0.0) if v0 <= v1 else (v1, 1.0)

r_mesh = np.linspace(10.0, 20.0, 1001)
rs_mesh, us_mesh = mesh_rho_star(r_mesh)
# rim extra density
r_rim = np.linspace(19.5, 20.0, 501)
rs_rim, us_rim = mesh_rho_star(r_rim)

polished = []

def polish(lo, hi, seed_desc):
    res = minimize_scalar(lambda rr: fast_rho_star(rr)[0], bounds=(lo, hi),
                          method='bounded',
                          options={'xatol': 1e-12})
    v_fast, u_fast = fast_rho_star(float(res.x))
    v_scan, u_scan = rho_star(float(res.x))  # full-scan cross-check
    assert abs(v_fast - v_scan) <= 1e-9 * max(1.0, abs(v_scan)), \
        (seed_desc, v_fast, v_scan)
    polished.append({'r': float(res.x), 'rho_star': v_scan, 'u_star': u_scan,
                     'seed': seed_desc})
    return v_scan

# every mesh local minimum (base mesh + rim mesh), polished in its cell
for arr_r, arr_v, dr, tag in ((r_mesh, rs_mesh, DR, 'mesh'),
                              (r_rim, rs_rim, 0.001, 'rim-mesh')):
    for i in range(1, len(arr_r) - 1):
        if arr_v[i] <= arr_v[i - 1] and arr_v[i] <= arr_v[i + 1]:
            polish(float(arr_r[i] - dr), float(arr_r[i] + dr),
                   f'{tag} local min at r={arr_r[i]:.4f}')
# registered analytic seeds
seed_points = {}
seed_points['r=10 boundary'] = rho_star(10.0)
seed_points['r=20 boundary'] = rho_star(20.0)
# S' extremum: S_ab with a=b=2 -> |S'| max at u=(r-10)/10=1/2 -> r=15; verify
rr = np.linspace(10.0, 20.0, 20001)
_Sv, Spv, _Nv = profiles_SN(rr)
r_sp_extremum = float(rr[int(np.argmin(Spv))])
seed_points['Sprime extremum r (numeric)'] = r_sp_extremum
seed_points['rho at Sprime extremum, u=0'] = float(rho_ru(r_sp_extremum, 0.0))
seed_points['rho* at Sprime extremum'] = rho_star(r_sp_extremum)
polish(r_sp_extremum - 0.05, r_sp_extremum + 0.05, 'Sprime extremum window')
# M'' sign change mid-rise: SS'' zero at x=1/2 of rise [9, 20.5] -> r=14.75
r_mpp = 9.0 + 0.5 * 11.5
seed_points['Mpp sign-change r'] = r_mpp
seed_points['rho* at Mpp sign-change'] = rho_star(r_mpp)
polish(r_mpp - 0.05, r_mpp + 0.05, 'Mpp sign-change window')
# rim approach / rise-top approach from inside the volume: boundary r=20
# (polished on the rim cell) and a window polish ending at 20
polish(19.99, 20.0, 'rim approach window [19.99, 20]')
polish(10.0, 10.01, 'inner boundary window [10, 10.01]')

all_candidates = [(float(v), float(r), float(u), 'mesh')
                  for r, v, u in zip(r_mesh, rs_mesh, us_mesh)]
all_candidates += [(float(v), float(r), float(u), 'rim-mesh')
                   for r, v, u in zip(r_rim, rs_rim, us_rim)]
all_candidates += [(p['rho_star'], p['r'], p['u_star'], 'polished')
                   for p in polished]
all_candidates += [(seed_points['r=10 boundary'][0], 10.0,
                    seed_points['r=10 boundary'][1], 'seed-boundary'),
                   (seed_points['r=20 boundary'][0], 20.0,
                    seed_points['r=20 boundary'][1], 'seed-boundary')]
gmin = min(all_candidates)
gsp = rho_split(gmin[1], gmin[2])
global_min = {'rho': gmin[0], 'r': gmin[1], 'u': gmin[2],
              'n_xhat_abs': float(np.sqrt(gmin[2])), 'source': gmin[3],
              'split': {k: float(gsp[k]) for k in ('R1', 'R2', 'QK')},
              'M': float(gsp['M']), 'Mp': float(gsp['Mp'])}
OUT['search_c'] = {
    'mesh': {'n': 1001, 'dr': DR, 'min_rho_star': float(rs_mesh.min()),
             'argmin_r': float(r_mesh[int(np.argmin(rs_mesh))])},
    'rim_mesh': {'n': 501, 'dr': 0.001,
                 'min_rho_star': float(rs_rim.min()),
                 'argmin_r': float(r_rim[int(np.argmin(rs_rim))])},
    'polished': polished,
    'seeds': {k: (list(v) if isinstance(v, tuple) else v)
              for k, v in seed_points.items()},
    'global_min': global_min,
    'any_negative': bool(gmin[0] < 0)}
print(f"(c) global min rho* = {gmin[0]:.9e} at r={gmin[1]:.6f}, "
      f"u={gmin[2]:.4f} ({gmin[3]}); split "
      f"R1={global_min['split']['R1']:.4e} R2={global_min['split']['R2']:.4e} "
      f"QK={global_min['split']['QK']:.4e}")

# ============================================================ (d) floors
SAFETY = 2.0
HALF = DR / 2.0
# d rho/dr at the minimising u (FD, h=1e-5, central; one-sided at edges)
h = 1e-5
drho = np.empty(1001)
for i, r in enumerate(r_mesh):
    u = us_mesh[i]
    if i == 0:
        drho[i] = (float(rho_ru(r + h, u)) - float(rho_ru(r, u))) / h
    elif i == 1000:
        drho[i] = (float(rho_ru(r, u)) - float(rho_ru(r - h, u))) / h
    else:
        drho[i] = (float(rho_ru(r + h, u)) - float(rho_ru(r - h, u))) / (2 * h)
# second derivative of rho* on the mesh (second differences)
d2 = np.abs(np.diff(rs_mesh, n=2)) / DR ** 2

REGIONS = {'inner': (10.0, 12.5), 'mid': (12.5, 17.5), 'rim': (17.5, 20.0)}
regions_out = {}
for name, (lo, hi) in REGIONS.items():
    m = (r_mesh >= lo) & (r_mesh <= hi)
    cand = [c for c in all_candidates if lo <= c[1] <= hi]
    found = min(cand)
    maxd1 = float(np.max(np.abs(drho[m])))
    floor1 = SAFETY * maxd1 * HALF
    idx = np.where(m)[0]
    d2_reg = d2[max(idx[0] - 1, 0):idx[-1]] if len(idx) > 2 else d2
    maxd2 = float(np.max(d2_reg)) if len(d2_reg) else 0.0
    floor2 = SAFETY * maxd2 * HALF ** 2 / 2.0
    # is the regional found min a polished stationary point?
    stat = any(abs(p['r'] - found[1]) < 1e-6 and p['rho_star'] == found[0]
               for p in polished)
    regions_out[name] = {
        'range': [lo, hi],
        'found_min': found[0], 'found_r': found[1], 'found_u': found[2],
        'found_source': found[3],
        'max_abs_drho_dr_at_ustar': maxd1,
        'floor_first_order': floor1,
        'certified_bound_first_order': found[0] - floor1,
        'max_abs_d2rho_dr2_mesh': maxd2,
        'floor_second_order': floor2,
        'certified_bound_second_order': found[0] - floor2,
        'regional_min_is_polished_stationary': bool(stat),
        'any_negative_in_region': bool(found[0] < 0)}
    print(f"(d) {name}: found {found[0]:.6e} @ r={found[1]:.4f}; "
          f"floor1 {floor1:.3e} -> bound {found[0]-floor1:.6e}; "
          f"floor2 {floor2:.3e} -> bound {found[0]-floor2:.6e}; "
          f"stationary={stat}")
OUT['floors_d'] = {'safety_factor': SAFETY, 'mesh_half_spacing': HALF,
                   'fd_h': h, 'regions': regions_out}
OUT['verdict_input'] = {
    'global_min': global_min,
    'any_negative_anywhere': bool(gmin[0] < 0),
    'per_region': {k: {'found_min': v['found_min'],
                       'floor_first_order': v['floor_first_order'],
                       'certified_bound_first_order':
                           v['certified_bound_first_order'],
                       'floor_second_order': v['floor_second_order'],
                       'certified_bound_second_order':
                           v['certified_bound_second_order']}
                   for k, v in regions_out.items()}}

with open(f'{WP}/gate35/work/g35_item1_results.json', 'w') as f:
    json.dump(OUT, f, indent=1)
print('wrote g35_item1_results.json')
