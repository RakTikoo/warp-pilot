#!/usr/bin/env python3
"""g47_run2.py -- Gate-47 part 2: FD calibration, degeneracy (claim f),
summary. (Part 1, g47_run.py, wrote g47_numbers / clamp margins /
box_diag; its calibration block failed on a driver-side array-size
bug in the trivial-limit call, fixed here.)"""
import hashlib
import json
import time

import numpy as np

import g47_lib as G

WP = G.WP
RES = f'{WP}/gate47/results'
t_start = time.time()

def log(*a):
    print(f'[{time.time()-t_start:7.1f}s]', *a, flush=True)

H2 = (1.0, 1.0, 1.0)
C394 = (0.8015689430763502, 1.3179449338854314, 3.574968377899082)
ANCHOR = (0.601180962300002, 1.5934531363763935, 4.887238651223381)
CENTRE = (0.4003528067864536, 1.9863455070489624, 6.715383396291902)
TG_H2_NEC = -1.9422459891767227e-04

outC, _ = G.set_read(*CENTRE)
outH, _ = G.set_read(*H2)
outA, _ = G.set_read(*ANCHOR)
out4, _ = G.set_read(*C394)
outs = {'H2': outH, 'C394': out4, 'ANCHOR': outA, 'CENTRE': outC}
log('re-reads for site points done')

cal = {}
pts_t = np.array([[12.0, 3.0, 4.0], [0.0, 15.0, 5.0], [11.0, -6.0, 8.0],
                  [16.0, 1.0, 2.0]])
P4 = len(pts_t)
z4 = np.zeros(P4); o4 = np.ones(P4)
Tt, _ = G.T_from_profiles(pts_t, (z4, z4, z4, o4, z4, z4, o4, z4, z4))
cal['trivial_limit_max_abs_T'] = float(np.max(np.abs(Tt)))
cal['vector_agreement'] = G.vector_agreement()
log('trivial max|T|', cal['trivial_limit_max_abs_T'])

fd = {}
for label, tr, pt in (('centre_nec_argmin', CENTRE,
                       np.array(outC['nec_argmin_point'])),
                      ('H2_nec_argmin_control', H2,
                       np.array(outH['nec_argmin_point']))):
    Tmine, gmine = G.T_at(*tr, pt[None, :])
    That_mine = G.eulerian_that(gmine, Tmine)
    rows = []
    for h in (0.1, 0.05, 0.025, 0.0125):
        Tfd, gfd = G.einstein_fd(pt[None, :], *tr, h)
        dT = float(np.max(np.abs(Tfd - Tmine)))
        That_fd = G.eulerian_that(gfd, Tfd)
        dThat = float(np.max(np.abs(That_fd - That_mine)))
        rows.append({'h': h, 'max_abs_diff_T': dT,
                     'max_abs_diff_That': dThat,
                     'scale_T': float(np.max(np.abs(Tmine)))})
        log('FD', label, 'h', h, 'dT', dT, 'dThat', dThat)
    fd[label] = {'point': pt.tolist(), 'rows': rows}
cal['fd_cross_path'] = fd

deg = {}
phys_stored = json.load(open(f'{WP}/phase396/results/p396_physicality.json'))
rows_spec = {'H2': (H2, 16.21951219512195), 'C394': (C394, 15.487804878048781),
             'ANCHOR': (ANCHOR, 15.73170731707317), 'BEST': (CENTRE, 16.46341463414634)}
phys = {}
for key, (tr, r_arg) in rows_spec.items():
    pr = G.profiles_at_radius(*tr, G.FINE_R)
    S, N, M = pr[0], pr[3], pr[6]
    peak = float(np.max(np.abs(G.BETA * S)))
    loc = G.profiles_at_radius(*tr, np.array([r_arg]))
    h2loc = G.profiles_at_radius(1.0, 1.0, 1.0, np.array([r_arg]))
    names = ('S', 'Sp', 'Spp', 'N', 'Np', 'Npp', 'M', 'Mp', 'Mpp')
    entry = {'triple': list(tr),
             'S_range': [float(S.min()), float(S.max())],
             'N_range': [float(N.min()), float(N.max())],
             'M_range': [float(M.min()), float(M.max())],
             'peak_abs_beta_S': peak,
             'peak_abs_S': float(np.max(np.abs(S))),
             'local_at_nec_argmin': {n: float(loc[i][0]) for i, n in enumerate(names)},
             'H2_totals_at_same_r': {n: float(h2loc[i][0]) for i, n in enumerate(names)}}
    st = phys_stored['rows'][key]
    md = {}
    for kk in ('S_range', 'N_range', 'M_range'):
        md[kk] = float(max(abs(entry[kk][0] - st[kk][0]), abs(entry[kk][1] - st[kk][1])))
    md['peak_abs_beta_S'] = float(entry['peak_abs_beta_S'] - st['peak_abs_beta_S'])
    for sec in ('local_at_nec_argmin', 'H2_totals_at_same_r'):
        md[sec] = float(max(abs(entry[sec][n] - st[sec][n]) for n in names))
    entry['max_diffs_vs_stored'] = md
    entry['stored_peak_abs_beta_S'] = st['peak_abs_beta_S']
    phys[key] = entry
    log('phys', key, 'peak', peak)
h2peak = phys['H2']['peak_abs_beta_S']
for key in phys:
    phys[key]['peak_ratio_to_H2_mine'] = float(phys[key]['peak_abs_beta_S'] / h2peak)
    phys[key]['stored_peak_ratio'] = phys_stored['rows'][key]['peak_shift_ratio_to_H2']
deg['physicality'] = phys

pt_site = np.array(outC['nec_argmin_point'])
mu_list = [0.0, 0.05, 0.1, 0.2, 0.3, 0.4003528067864536, 0.5,
           0.601180962300002, 0.8, 1.0]
scan = []
for muS in mu_list:
    pm = G.point_margins(muS, CENTRE[1], CENTRE[2], pt_site)
    q, qfib = G.worst_null_at(muS, CENTRE[1], CENTRE[2], pt_site)
    scan.append({'muS': muS, 'nec_margin': pm['nec'], 'typeI': pm['typeI'],
                 'worst_null': q, 'worst_null_fib642': qfib})
    log('muS scan', muS, pm['nec'], q, 'typeI', pm['typeI'])
wn0 = scan[0]['worst_null']; nec0 = scan[0]['nec_margin']
xs = np.array([s['muS'] ** 2 for s in scan[1:]])
yw = np.array([s['worst_null'] - wn0 for s in scan[1:]])
yn = np.array([s['nec_margin'] - nec0 for s in scan[1:]])
fitw = np.polyfit(xs, yw, 1); fitn = np.polyfit(xs, yn, 1)
ll_mu = np.array([0.1, 0.2, 0.3, 0.4003528067864536, 0.5, 0.601180962300002, 0.8, 1.0])
ll_y = np.array([abs(s['worst_null'] - wn0) for s in scan if s['muS'] in ll_mu])
ll_slope = float(np.polyfit(np.log(ll_mu), np.log(ll_y), 1)[0])
deg['binding_site_scan'] = {
    'point': pt_site.tolist(), 'r': float(np.linalg.norm(pt_site)),
    'muN': CENTRE[1], 'muM': CENTRE[2], 'table': scan,
    'nec_at_muS0': nec0, 'worst_null_at_muS0': wn0,
    'fit_worst_null_vs_muS2': {'slope': float(fitw[0]), 'intercept': float(fitw[1]),
        'max_abs_residual': float(np.max(np.abs(yw - np.polyval(fitw, xs))))},
    'fit_nec_margin_vs_muS2': {'slope': float(fitn[0]), 'intercept': float(fitn[1]),
        'max_abs_residual': float(np.max(np.abs(yn - np.polyval(fitn, xs))))},
    'loglog_slope_worst_null': ll_slope}

sf = {}
for label, tr in (('shiftfree_centre_NM', (0.0, CENTRE[1], CENTRE[2])),
                  ('shiftfree_H2_NM', (0.0, 1.0, 1.0))):
    o, _ = G.set_read(*tr)
    sf[label] = {'triple': list(tr), 'nec': o['nec'], 'wec': o['wec'],
                 'dec': o['dec'], 'sec': o['sec'], 'rho': o['rho'],
                 'joint': o['joint'], 'typeI_fraction': o['typeI_fraction'],
                 'nec_argmin_r': o['nec_argmin_r'], 'dec_argmin_r': o['dec_argmin_r']}
    log('shift-free', label, o['joint'])
deg['shift_free'] = sf

attr = {}
for label, tr in (('muS_only', (CENTRE[0], ANCHOR[1], ANCHOR[2])),
                  ('muN_only', (ANCHOR[0], CENTRE[1], ANCHOR[2])),
                  ('muM_only', (ANCHOR[0], ANCHOR[1], CENTRE[2]))):
    o, _ = G.set_read(*tr)
    attr[label] = {'triple': list(tr), 'joint': o['joint'],
                   'nec_min': o['nec']['min'], 'dec_min': o['dec']['min'],
                   'gain_over_anchor_mine': float(o['joint'] - outA['joint'])}
    log('attr', label, o['joint'])
deg['gain_attribution'] = {
    'singles': attr, 'anchor_joint_mine': outA['joint'],
    'centre_joint_mine': outC['joint'],
    'full_centre_gain_mine': float(outC['joint'] - outA['joint']),
    'full_centre_gain_stored': 2.2377958108656506e-05}

ridge = []
for name, tr in (('H2', H2), ('C394', C394), ('ANCHOR', ANCHOR), ('CENTRE', CENTRE)):
    j = outs[name]['joint']; muS = tr[0]
    ridge.append({'name': name, 'muS': muS, 'joint_mine': j,
                  'joint_over_muS2': float(j / muS ** 2),
                  'pure_shift_scaling_prediction': float(TG_H2_NEC * muS ** 2),
                  'actual_minus_prediction': float(j - TG_H2_NEC * muS ** 2)})
deg['ridge'] = ridge
with open(f'{RES}/g47_degeneracy.json', 'w') as f:
    json.dump(deg, f, indent=1)
log('degeneracy written')

artefacts = [
 'phase396/CHECKPOINT396.md', 'phase396/results/p396_memo.md',
 'phase396/results/p396_confirmation.json', 'phase396/results/p396_clamp.json',
 'phase396/results/p396_controls.json', 'phase396/results/p396_anatomy.json',
 'phase396/results/p396_physicality.json',
 'phase396/results/p396_search_summary.json',
 'phase396/results/p396_screens.jsonl',
 'phase395/results/p395_confirmation.json', 'phase395/results/p395_clamp.json',
 'phase395/results/p395_search_summary.json',
 'phase394/results/p394_confirmation.json',
 'phase379/results/p379_confirmation.json', 'phase379/results/p379_state_H2.json',
 'phase344/results/p344_confirmation.json',
 'phase344/results/p344_state_A2.json']
md5s = {rel: hashlib.md5(open(f'{WP}/{rel}', 'rb').read()).hexdigest()
        for rel in artefacts}
summary = {'calibrations': cal, 'md5_registry': md5s,
           'vector_agreement': G.vector_agreement(),
           'tensor_path': 'sympy Cartesian symbolic first/second spatial '
                          'derivatives of the registered metric, radial '
                          'symbols substituted, numpy lambdify (cse=True); '
                          'own vectorised Christoffel/Ricci/Einstein assembly',
           'scoping_note': 'adversary-polish depth not run (per tasking); '
                           'controls judged on five minima + worst-nulls',
           'wall_time_s_part2': time.time() - t_start}
with open(f'{RES}/g47_summary.json', 'w') as f:
    json.dump(summary, f, indent=1)
log('summary written; total wall', time.time() - t_start)
