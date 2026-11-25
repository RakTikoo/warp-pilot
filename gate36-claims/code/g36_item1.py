#!/usr/bin/env python3
"""
g36_item1.py -- Gate-36 Worker A driver: CTRL-T1, CTRL-T2, Item 1.
Re-derives the pointwise member's That at the four stored
binding sites with g36_lib (own assembly), compares against
phase320/work/p320_targets.json component-wise, computes own
exact pointwise NEC minima and Type-I flags, and cross-checks
the analytic assembly against an own FD Einstein computation.
Writes g36_item1_results.json.  No stored tensor machinery is
imported; the targets file is read as data only.
"""
import json
import time

import numpy as np

import g36_lib as L

WD = '/home/hatch/workspace/warp-pilot/gate36/work'
TGT_PATH = '/home/hatch/workspace/warp-pilot/phase320/work/p320_targets.json'

with open(TGT_PATH) as f:
    TGT = json.load(f)

t0 = time.time()
pts = np.array([s['point'] for s in TGT['sites']], dtype=np.float64)
That = L.That_at(pts)
build_s = time.time() - t0

out_sites = []
max_abs_all = 0.0
ctrlT1_rho_pass = True
ctrlT1_comp_pass = True
ctrlT2_pass = True
for i, s in enumerate(TGT['sites']):
    stored = np.array(s['That'], dtype=np.float64)
    mine = That[i]
    diff = np.abs(mine - stored)
    max_abs = float(np.max(diff))
    denom = np.maximum(np.abs(stored), 1e-300)
    max_rel = float(np.max(diff / denom))
    rho_mine = float(mine[0, 0]); rho_st = float(s['rho'])
    rho_absdiff = abs(rho_mine - rho_st)
    rho_reldiff = rho_absdiff / abs(rho_st)
    max_abs_all = max(max_abs_all, max_abs)
    if rho_reldiff > 1e-15:
        ctrlT1_rho_pass = False
    if max_abs > 1e-16:
        ctrlT1_comp_pass = False
    # invariants (rotation diagnosis)
    eta = np.diag([-1.0, 1.0, 1.0, 1.0])
    ev_mine = np.linalg.eigvals(eta @ mine)
    ev_st = np.linalg.eigvals(eta @ stored)
    sortk = lambda z: sorted(z, key=lambda w: (round(w.real, 12), w.imag))
    ev_diff = float(np.max(np.abs(np.array(sortk(ev_mine))
                                  - np.array(sortk(ev_st)))))
    inv = {
        'eig_etaThat_max_abs_diff_sorted': ev_diff,
        'abs_T0i_mine': float(np.linalg.norm(mine[0, 1:])),
        'abs_T0i_stored': float(np.linalg.norm(stored[0, 1:])),
        'transverse_block_eigs_mine':
            [float(v) for v in np.linalg.eigvalsh(mine[1:, 1:])],
        'transverse_block_eigs_stored':
            [float(v) for v in np.linalg.eigvalsh(stored[1:, 1:])],
        'frob_mine': float(np.linalg.norm(mine)),
        'frob_stored': float(s['frob']),
    }
    # own derived reads
    nec_min, kstar, fib_min = L.worst_null(mine)
    nec_st = float(s['nec_min_exact'])
    nec_absdiff = abs(nec_min - nec_st)
    nec_reldiff = nec_absdiff / abs(nec_st)
    isI, seg = L.segre_typeI(mine)
    typeI_st = bool(s['hawking_ellis_typeI'])
    if isI != typeI_st or nec_reldiff > 1e-9:
        ctrlT2_pass = False
    # FD cross-check at this site (on T_req, then tetrad of FD tensor
    # with the analytic metric's tetrad for comparability of rho/nec)
    Tfd, Tfd1, Tfd2 = L.fd_T_req(pts[i])
    g_an = L.metric_cart(pts[i])
    That_fd = L.eulerian_that(g_an, Tfd)
    fd_max_abs_that = float(np.max(np.abs(That_fd - mine)))
    fd_rho = float(That_fd[0, 0])
    out_sites.append({
        'key': s['key'],
        'point': s['point'],
        'r_stored': float(s['r']),
        'r_mine': float(np.linalg.norm(pts[i])),
        'That_mine': mine.tolist(),
        'That_stored': stored.tolist(),
        'That_diff': (mine - stored).tolist(),
        'max_abs_component_diff': max_abs,
        'max_rel_component_diff': max_rel,
        'rho_mine': rho_mine,
        'rho_stored': rho_st,
        'rho_abs_diff': rho_absdiff,
        'rho_rel_diff': rho_reldiff,
        'invariants': inv,
        'nec_min_exact_mine': float(nec_min),
        'nec_min_exact_stored': nec_st,
        'nec_abs_diff': nec_absdiff,
        'nec_rel_diff': nec_reldiff,
        'nec_fib642_mine': float(fib_min),
        'nec_fib642_stored': float(s['nec_fib642']),
        'kstar_mine': kstar.tolist(),
        'kstar_stored': s['kstar'],
        'typeI_mine': bool(isI),
        'typeI_stored': typeI_st,
        'segre_mine': seg,
        'segre_stored_type': s['segre']['type'],
        'fd_crosscheck': {
            'That_fd_richardson': That_fd.tolist(),
            'fd_vs_analytic_max_abs_That_diff': fd_max_abs_that,
            'fd_rho': fd_rho,
            'fd_rho_rel_diff_vs_mine': abs(fd_rho - rho_mine) / abs(rho_mine),
        },
    })
    print(f"{s['key']}: max_abs_diff={max_abs:.3e} rho_rel={rho_reldiff:.3e} "
          f"nec_mine={nec_min:.12e} nec_st={nec_st:.12e} "
          f"typeI {isI} vs {typeI_st} fd_max={fd_max_abs_that:.3e}",
          flush=True)

ctrlT1 = bool(ctrlT1_rho_pass and ctrlT1_comp_pass)
results = {
    'worker': 'Gate-36 Worker A (controls target side + Item 1)',
    'assembly_build_and_eval_s': build_s,
    'CTRL-T1': {
        'pass': ctrlT1,
        'rho_bar_rel_1e-15_pass': bool(ctrlT1_rho_pass),
        'components_bar_abs_1e-16_pass': bool(ctrlT1_comp_pass),
        'max_abs_component_diff_overall': max_abs_all,
        'per_site_max_abs': [o['max_abs_component_diff'] for o in out_sites],
        'per_site_rho_rel_diff': [o['rho_rel_diff'] for o in out_sites],
    },
    'CTRL-T2': {
        'pass': bool(ctrlT2_pass),
        'per_site_nec_rel_diff': [o['nec_rel_diff'] for o in out_sites],
        'per_site_typeI_match': [o['typeI_mine'] == o['typeI_stored']
                                  for o in out_sites],
    },
    'sites': out_sites,
    'wall_time_s': time.time() - t0,
}
with open(f'{WD}/g36_item1_results.json', 'w') as f:
    json.dump(results, f, indent=1)
print('CTRL-T1', 'PASS' if ctrlT1 else 'FAIL',
      '(rho sub-bar', ctrlT1_rho_pass, ', comp sub-bar', ctrlT1_comp_pass, ')')
print('CTRL-T2', 'PASS' if ctrlT2_pass else 'FAIL')
print('max abs component diff overall', max_abs_all)
