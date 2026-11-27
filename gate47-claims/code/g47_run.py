#!/usr/bin/env python3
"""g47_run.py -- Gate-47 deciding reads driver (fresh machinery only)."""
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

def diffs(got, tgt):
    return {k: float(got[k] - tgt[k]) for k in tgt}

def read_entry(name, triple, targets, clamp=False):
    out, R = G.set_read(*triple, clamp=clamp)
    got = {'nec': out['nec']['min'], 'dec': out['dec']['min'],
           'wec': out['wec']['min'], 'sec': out['sec']['min'],
           'rho': out['rho']['min']}
    e = {'name': name, 'triple': list(triple), 'clamp': clamp,
         'nec': out['nec'], 'wec': out['wec'], 'dec': out['dec'],
         'sec': out['sec'], 'rho': out['rho'], 'joint': out['joint'],
         'typeI_count': out['typeI_count'],
         'typeI_fraction': out['typeI_fraction'],
         'nec_argmin_r': out['nec_argmin_r'],
         'nec_argmin_point': out['nec_argmin_point'],
         'nec_argmin_typeI': out['nec_argmin_typeI'],
         'dec_argmin_r': out['dec_argmin_r'],
         'dec_argmin_point': out['dec_argmin_point'],
         'dec_argmin_typeI': out['dec_argmin_typeI'],
         'stored_targets': targets,
         'diffs_vs_stored': diffs(got, targets) if targets else None}
    log(name, 'joint', out['joint'], 'nec', got['nec'], 'dec', got['dec'])
    return e, out, R

H2 = (1.0, 1.0, 1.0)
MIX = (0.9323593026620368, 1.1444417317708335, 1.1445068359375)
SEED = (0.9323593026620368, 1.1444417317708335, 2.289013671875)
C394 = (0.8015689430763502, 1.3179449338854314, 3.574968377899082)
ANCHOR = (0.601180962300002, 1.5934531363763935, 4.887238651223381)
CENTRE = (0.4003528067864536, 1.9863455070489624, 6.715383396291902)

TG = {
 'H2': {'nec': -1.9422459891767227e-04, 'dec': -1.8982585080461558e-04,
        'wec': -1.7768467393179327e-03, 'sec': -2.0943799294291577e-03,
        'rho': 8.789653555683182e-05},
 'MIX': {'nec': -1.7570735537945242e-04, 'dec': -1.5670690855768682e-04,
         'wec': -1.176749370558998e-03, 'sec': -2.1496503801466693e-03,
         'rho': 8.936712674433238e-05},
 'SEED': {'nec': -1.2413718983790085e-04, 'dec': -3.4350860761739224e-05,
          'wec': -9.443823050476109e-04, 'sec': -1.5236814797256301e-03,
          'rho': 9.46961652955672e-05},
 'C394': {'nec': -6.812652656191736e-05, 'dec': -4.611098054060287e-06,
          'wec': -0.0004876872626344858, 'sec': -0.000824703941166269,
          'rho': 9.678145350055573e-05},
 'ANCHOR': {'nec': -2.9809850277749006e-05, 'dec': -1.7766846142506707e-06,
            'wec': -1.2604578745184045e-04, 'sec': -4.6317591386364136e-04,
            'rho': 9.780857711542179e-05},
 'CENTRE': {'nec': -7.4318921690925e-06, 'dec': -1.0979323923912478e-06,
            'sec': -3.391058851844148e-04, 'rho': 9.858014400881535e-05},
}

numbers = {'reads': {}, 'worst_nulls': {}, 'clamps': {}}
outs = {}
for name, tr in (('H2', H2), ('MIX', MIX), ('SEED', SEED), ('C394', C394),
                 ('ANCHOR', ANCHOR), ('CENTRE', CENTRE)):
    e, out, R = read_entry(name, tr, TG[name])
    numbers['reads'][name] = e
    outs[name] = out
numbers['reads']['CENTRE']['stored_typeI_fraction'] = 0.7160493827160493
numbers['reads']['CENTRE']['typeI_fraction_diff'] = (
    outs['CENTRE']['typeI_fraction'] - 0.7160493827160493)

# ---- worst-nulls at own NEC argmin points
WN_TG = {'CENTRE': -8.706718841221561e-06, 'ANCHOR': -3.0896210095678075e-05,
         'SEED': -1.2477276305772507e-04}
for name in ('CENTRE', 'ANCHOR', 'SEED'):
    pt = np.array(outs[name]['nec_argmin_point'])
    q, qfib = G.worst_null_at(*{'CENTRE': CENTRE, 'ANCHOR': ANCHOR,
                                'SEED': SEED}[name], pt)
    numbers['worst_nulls'][name] = {
        'point': pt.tolist(), 'r': float(np.linalg.norm(pt)),
        'worst_null': q, 'worst_null_fib642': qfib,
        'stored_target': WN_TG[name], 'diff': float(q - WN_TG[name])}
    log('worst-null', name, q, 'diff', q - WN_TG[name])

# ---- clamps
clamp_reads = {}
for name, tr in (('CENTRE', CENTRE), ('ANCHOR', ANCHOR), ('H2', H2), ('MIX', MIX)):
    e, out, R = read_entry(f'{name}_CLAMPED', tr, None, clamp=True)
    clamp_reads[name] = (e, out)
numbers['clamps']['CENTRE'] = {
    **clamp_reads['CENTRE'][0],
    'stored_targets': {'joint': -7.644643599300465e-06,
                       'nec': -7.644643599300465e-06,
                       'dec': -1.0999871338545134e-06,
                       'rho': 9.858005002779685e-05},
    'diffs_vs_stored': {
        'joint': clamp_reads['CENTRE'][1]['joint'] - (-7.644643599300465e-06),
        'nec': clamp_reads['CENTRE'][1]['nec']['min'] - (-7.644643599300465e-06),
        'dec': clamp_reads['CENTRE'][1]['dec']['min'] - (-1.0999871338545134e-06),
        'rho': clamp_reads['CENTRE'][1]['rho']['min'] - 9.858005002779685e-05}}
numbers['clamps']['ANCHOR'] = {
    **clamp_reads['ANCHOR'][0],
    'stored_joint': -3.0189206094012074e-05,
    'joint_diff': clamp_reads['ANCHOR'][1]['joint'] - (-3.0189206094012074e-05)}
numbers['clamps']['H2'] = {
    **clamp_reads['H2'][0],
    'stored_targets_p379_anatomy_end_clamp_set': {
        'nec': -0.00019562414497796698, 'dec': -0.0002087299309761311,
        'rho': 8.793529206482093e-05},
    'diffs_vs_stored': {
        'nec': clamp_reads['H2'][1]['nec']['min'] - (-0.00019562414497796698),
        'dec': clamp_reads['H2'][1]['dec']['min'] - (-0.0002087299309761311),
        'rho': clamp_reads['H2'][1]['rho']['min'] - 8.793529206482093e-05}}
G43 = -1.7669632754376664e-04
numbers['clamps']['MIX'] = {
    **clamp_reads['MIX'][0],
    'stored_gate43_clamped_joint': G43,
    'joint_diff_vs_gate43': clamp_reads['MIX'][1]['joint'] - G43,
    'abs_diff_vs_gate43': abs(clamp_reads['MIX'][1]['joint'] - G43),
    'c10_band': 3e-06,
    'inside_c10_band': bool(abs(clamp_reads['MIX'][1]['joint'] - G43) <= 3e-06)}
clamp_cost = outs['CENTRE']['joint'] - clamp_reads['CENTRE'][1]['joint']
# note: cost defined stored as unclamped - clamped with sign: stored
# clamp_cost = clamped_joint - unclamped_joint? p396_clamp: unclamped
# -7.4318921690925e-06, clamped -7.644643599300465e-06, cost +2.1275e-07
# => cost = unclamped - clamped.
numbers['clamps']['centre_clamp_cost'] = {
    'value': float(clamp_cost), 'stored_target': 2.1275143020796448e-07,
    'diff': float(clamp_cost - 2.1275143020796448e-07)}
clamp_margins = {
    'clamped_centre_joint': clamp_reads['CENTRE'][1]['joint'],
    'anchor_unclamped_joint_mine': outs['ANCHOR']['joint'],
    'clamped_centre_minus_anchor_unclamped': float(
        clamp_reads['CENTRE'][1]['joint'] - outs['ANCHOR']['joint']),
    'L_stat_H2_stored_nec': TG['H2']['nec'],
    'H2_joint_mine': outs['H2']['joint'],
    'clamped_centre_minus_LstatH2_stored': float(
        clamp_reads['CENTRE'][1]['joint'] - TG['H2']['nec']),
    'clamped_centre_minus_H2_joint_mine': float(
        clamp_reads['CENTRE'][1]['joint'] - outs['H2']['joint'])}
with open(f'{RES}/g47_numbers.json', 'w') as f:
    json.dump(numbers, f, indent=1)
with open(f'{RES}/g47_clamp_margins.json', 'w') as f:
    json.dump(clamp_margins, f, indent=1)
log('numbers + clamp margins written')

# ================= box recount (pure recount) + worst-DEC re-read
recs = [json.loads(l) for l in open(f'{WP}/phase396/results/p396_screens.jsonl')
        if l.strip()]
anchor_joint = -2.9809850277749006e-05
box = {'total_reads': len(recs),
       'feasible_count': int(sum(1 for r in recs if r.get('feasible'))),
       'count_joint_gt_anchor_joint': int(sum(
           1 for r in recs if r['joint'] > anchor_joint)),
       'worst_dec_min': float(min(r['dec_min'] for r in recs)),
       'count_dec_le_-0.5': int(sum(1 for r in recs if r['dec_min'] <= -0.5)),
       'count_dec_le_-0.9999': int(sum(1 for r in recs if r['dec_min'] <= -0.9999)),
       'stored_anatomy': {'n_reads': 336, 'n_feasible': 336,
                          'n_beat_anchor': 326,
                          'min_dec_over_reads': -2.0253148251802704e-06,
                          'n_dec_saturated': 0}}
worst_dec_rec = min(recs, key=lambda r: r['dec_min'])
box['worst_dec_record'] = worst_dec_rec
e, out, R = read_entry('BOX_WORST_DEC', tuple(worst_dec_rec['triple']), None)
box['worst_dec_reread'] = {
    'triple': worst_dec_rec['triple'], 'stored_dec_min': worst_dec_rec['dec_min'],
    'mine_dec_min': out['dec']['min'],
    'diff': float(out['dec']['min'] - worst_dec_rec['dec_min']),
    'dec_argmin_r': out['dec_argmin_r'], 'dec_argmin_typeI': out['dec_argmin_typeI'],
    'nec_min': out['nec']['min'], 'joint': out['joint']}
log('box recount done; worst-DEC reread dec', out['dec']['min'])

# ================= diagonal re-reads + RAY3
anat = json.load(open(f'{WP}/phase396/results/p396_anatomy.json'))
diag_entries = []
seq = [{'triple': ANCHOR, 'stored_joint': anchor_joint, 'label': 'anchor'}]
for d in anat['diag']:
    seq.append({'triple': tuple(d['triple']), 'stored_joint': d['joint'],
                'label': 'diag'})
mine_joints = []
for s in seq:
    o, _ = G.set_read(*s['triple'])
    s['mine_joint'] = o['joint']
    s['diff'] = float(o['joint'] - s['stored_joint'])
    mine_joints.append(o['joint'])
    log('diag', s['label'], s['triple'], o['joint'], 'diff', s['diff'])
incs_mine = [float(mine_joints[i + 1] - mine_joints[i]) for i in range(8)]
incs_stored = [float(seq[i + 1]['stored_joint'] - seq[i]['stored_joint'])
               for i in range(8)]
diag_out = {
    'entries': [{**{k: s[k] for k in ('label', 'stored_joint', 'mine_joint', 'diff')},
                 'triple': list(s['triple'])} for s in seq],
    'monotone_mine': bool(all(b > a for a, b in zip(mine_joints, mine_joints[1:]))),
    'monotone_stored': bool(all(incs_stored[i] > 0 for i in range(8))),
    'increments_mine_from_anchor': incs_mine,
    'increments_stored_from_anchor_file': incs_stored,
    'stored_diag_increments_field': anat['diag_increments'],
    'stored_diag_increments_from_anchor_field': anat['diag_increments_from_anchor'],
    'first_increment_mine': incs_mine[0], 'first_increment_stored_exact': incs_stored[0],
    'last_increment_mine': incs_mine[-1],
    'last_increment_stored': 1.7767731003360187e-06,
    'ratio_last_over_first_mine': float(incs_mine[-1] / incs_mine[0]),
    'ratio_last_over_first_stored_exact': float(incs_stored[-1] / incs_stored[0])}
o, _ = G.set_read(0.601180962300002, 1.5934531363763935, 7.0)
diag_out['ray3_endpoint'] = {
    'triple': [0.601180962300002, 1.5934531363763935, 7.0],
    'mine_joint': o['joint'], 'stored_joint': -2.8521103406138924e-05,
    'diff': float(o['joint'] - (-2.8521103406138924e-05)),
    'nec_min': o['nec']['min'], 'dec_min': o['dec']['min']}
box['diagonal'] = diag_out
with open(f'{RES}/g47_box_diag.json', 'w') as f:
    json.dump(box, f, indent=1)
log('box/diag written')

# ================= calibrations
cal = {}
pts_t = np.array([[12.0, 3.0, 4.0], [0.0, 15.0, 5.0], [11.0, -6.0, 8.0],
                  [16.0, 1.0, 2.0]])
z3 = np.zeros(3); o3 = np.ones(3)
Tt, _ = G.T_from_profiles(pts_t, (z3, z3, z3, o3, z3, z3, o3, z3, z3))
cal['trivial_limit_max_abs_T'] = float(np.max(np.abs(Tt)))
cal['vector_agreement'] = G.vector_agreement()
# FD cross-path at centre NEC argmin + H2 NEC argmin (control point)
fd = {}
for label, tr, pt in (('centre_nec_argmin', CENTRE,
                       np.array(outs['CENTRE']['nec_argmin_point'])),
                      ('H2_nec_argmin_control', H2,
                       np.array(outs['H2']['nec_argmin_point']))):
    Tmine, _ = G.T_at(*tr, pt[None, :])
    That_mine = G.eulerian_that(G.metric_only(pt[None, :], *tr), Tmine)
    rows = []
    for h in (0.1, 0.05, 0.025, 0.0125):
        Tfd, gfd = G.einstein_fd(pt[None, :], *tr, h)
        dT = float(np.max(np.abs(Tfd - Tmine)))
        That_fd = G.eulerian_that(gfd, Tfd)
        dThat = float(np.max(np.abs(That_fd - That_mine)))
        rows.append({'h': h, 'max_abs_diff_T': dT, 'max_abs_diff_That': dThat,
                     'scale_T': float(np.max(np.abs(Tmine)))})
        log('FD', label, 'h', h, 'dT', dT, 'dThat', dThat)
    fd[label] = {'point': pt.tolist(), 'rows': rows,
                 'T_mine': Tmine[0].tolist()}
cal['fd_cross_path'] = fd

# ================= degeneracy (claim f)
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
             'peak_ratio_to_H2_mine': None,
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
    log('phys', key, 'peak', peak, 'maxdiff', max(abs(v) for v in
        [md['S_range'], md['N_range'], md['M_range'], md['peak_abs_beta_S'],
         md['local_at_nec_argmin'], md['H2_totals_at_same_r']]))
h2peak = phys['H2']['peak_abs_beta_S']
for key in phys:
    phys[key]['peak_ratio_to_H2_mine'] = float(phys[key]['peak_abs_beta_S'] / h2peak)
    phys[key]['stored_peak_ratio'] = phys_stored['rows'][key]['peak_shift_ratio_to_H2']
deg['physicality'] = phys

# (ii) binding-site mu_S scan at MY centre NEC argmin point
pt_site = np.array(outs['CENTRE']['nec_argmin_point'])
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

# (iii) shift-free SET reads
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

# (iv) gain attribution
attr = {}
for label, tr in (('muS_only', (CENTRE[0], ANCHOR[1], ANCHOR[2])),
                  ('muN_only', (ANCHOR[0], CENTRE[1], ANCHOR[2])),
                  ('muM_only', (ANCHOR[0], ANCHOR[1], CENTRE[2]))):
    o, _ = G.set_read(*tr)
    attr[label] = {'triple': list(tr), 'joint': o['joint'],
                   'nec_min': o['nec']['min'], 'dec_min': o['dec']['min'],
                   'gain_over_anchor_mine': float(o['joint'] - outs['ANCHOR']['joint'])}
    log('attr', label, o['joint'])
deg['gain_attribution'] = {
    'singles': attr, 'anchor_joint_mine': outs['ANCHOR']['joint'],
    'centre_joint_mine': outs['CENTRE']['joint'],
    'full_centre_gain_mine': float(outs['CENTRE']['joint'] - outs['ANCHOR']['joint']),
    'full_centre_gain_stored': 2.2377958108656506e-05}

# (v) ridge table
ridge = []
jH2s = TG['H2']['nec']
for name, tr in (('H2', H2), ('C394', C394), ('ANCHOR', ANCHOR), ('CENTRE', CENTRE)):
    j = outs[name]['joint']; muS = tr[0]
    ridge.append({'name': name, 'muS': muS, 'joint_mine': j,
                  'joint_over_muS2': float(j / muS ** 2),
                  'pure_shift_scaling_prediction': float(jH2s * muS ** 2),
                  'actual_minus_prediction': float(j - jH2s * muS ** 2)})
deg['ridge'] = ridge
with open(f'{RES}/g47_degeneracy.json', 'w') as f:
    json.dump(deg, f, indent=1)
log('degeneracy written')

# ================= summary: calibrations + md5 registry
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
md5s = {}
for rel in artefacts:
    md5s[rel] = hashlib.md5(open(f'{WP}/{rel}', 'rb').read()).hexdigest()
summary = {'calibrations': cal, 'md5_registry': md5s,
           'vector_agreement': G.vector_agreement(),
           'tensor_path': 'sympy Cartesian symbolic first/second spatial '
                          'derivatives of the registered metric, radial '
                          'symbols substituted, numpy lambdify (cse=True); '
                          'own vectorised Christoffel/Ricci/Einstein assembly',
           'scoping_note': 'adversary-polish depth not run (per tasking); '
                           'controls judged on five minima + worst-nulls',
           'wall_time_s': time.time() - t_start}
with open(f'{RES}/g47_summary.json', 'w') as f:
    json.dump(summary, f, indent=1)
log('summary written; total wall', time.time() - t_start)
