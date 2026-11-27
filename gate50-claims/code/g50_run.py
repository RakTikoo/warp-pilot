#!/usr/bin/env python3
"""
g50_run.py -- Gate-50 controls and claim reads
(float64 path; the mpmath named-point verification is
g50_mp.py; the adversary polish is g50_polish.py).

Controls (must pass before claim reads are believed):
  CTL-A  Phase 400 base winner at vS = 0 (stored joint
         +1.3977194851281464e-06, five minima, worst-null
         identical to the joint);
  CTL-B  the (1,1,1) -> L_stat(H2) anchor
         -1.9423115870905664e-04 (both S readings of the
         H2 totals computed; the matching one identified);
  CTL-C  Phase 404 ladder points muS = 0.171875 and
         muS = 0.5 through this gate's assembly.
Claims:
  (a) the 405 winner's joint / worst-null at the
      criterion amplitude;
  (b) peak reads (winner and H2), dense monotonicity
      scan of the winning shape;
  (c) cost curves: winner at peaks 0.05 / 0.25 /
      criterion (from (a)); fixed shape at muS = 0.05 /
      0.171875 / 0.5 (CTL-C + one extra read);
  (d) the shape's locals (in the calibration record)
      and Stage B's criterion read vs screen 375;
  (e) SEC minima on the face of every read.
Writes gate50/results/g50_numbers.json incrementally.
"""
import json
import os
import sys
import time

import numpy as np

WP = os.environ.get('G50_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/gate50/work')
import g50_lib as G  # noqa: E402

OUT_PATH = f'{WP}/gate50/results/g50_numbers.json'
out = {}
if os.path.exists(OUT_PATH):
    out = json.load(open(OUT_PATH))


def save():
    json.dump(out, open(OUT_PATH, 'w'), indent=1)


def cmp_block(gate, stored):
    return {'gate': gate, 'stored': stored,
            'diff': (gate - stored) if gate is not None
            and stored is not None else None}


def read_block(name, prof_fn, stored=None, do_wn=False):
    t0 = time.time()
    s, aux = G.set_read(prof_fn)
    blk = {'summary': s, 'joint': G.joint_of(s),
           'wall_s': time.time() - t0}
    if do_wn:
        pt = np.array(s['nec_argmin_point'])
        nec, ti, That = G.nec_at(prof_fn, pt)
        q, _m, _l = G.worst_null_exact(That)
        blk['worst_null_at_nec_argmin'] = q
        blk['worst_null_fib_at_nec_argmin'] = G.worst_null_scan(That)
        blk['nec_at_argmin_recheck'] = nec
    if stored:
        blk['cmp'] = {}
        pairs = [('joint', blk['joint'], stored.get('joint')),
                 ('nec_min', s['nec']['min'], stored.get('nec_min')),
                 ('dec_min', s['dec']['min'], stored.get('dec_min')),
                 ('wec_min', s['wec']['min'], stored.get('wec_min')),
                 ('sec_min', s['sec']['min'], stored.get('sec_min')),
                 ('rho_min', s['rho']['min'], stored.get('rho_min')),
                 ('typeI_fraction', s['typeI_fraction'],
                  stored.get('typeI_fraction')),
                 ('nec_argmin_r', s['nec_argmin_r'],
                  stored.get('nec_argmin_r'))]
        for nm, gv, sv in pairs:
            if sv is not None:
                blk['cmp'][nm] = cmp_block(gv, sv)
        if do_wn and stored.get('worst_null_at_nec_argmin') is not None:
            blk['cmp']['worst_null'] = cmp_block(
                blk['worst_null_at_nec_argmin'],
                stored['worst_null_at_nec_argmin'])
    out[name] = blk
    save()
    print(f'{name}: joint={blk["joint"]:.12e} '
          f'({blk["wall_s"]:.0f}s)', flush=True)
    return blk


WIN = G.INP['winner400']
WIN_STORED = {'joint': WIN['joint'], 'nec_min': WIN['nec_min'],
              'dec_min': WIN['dec_min'], 'wec_min': WIN['wec_min'],
              'sec_min': WIN['sec_min'], 'rho_min': WIN['rho_min'],
              'typeI_fraction': WIN['typeI_fraction'],
              'nec_argmin_r': WIN['nec_argmin_r'],
              'worst_null_at_nec_argmin':
              WIN['worst_null_at_set_nec_argmin']}

# ---------------- controls
if 'CTL-A_base_winner' not in out:
    read_block('CTL-A_base_winner', G.prof_winner_base,
               stored=WIN_STORED, do_wn=True)
if 'CTL-B_h2_static' not in out:
    read_block('CTL-B_h2_static', G.prof_h2_scaled(0.0))
if 'CTL-B_h2_full' not in out:
    read_block('CTL-B_h2_full', G.prof_h2_scaled(1.0))
out['CTL-B_anchor'] = {
    'anchor_value': -1.9423115870905664e-04,
    'diff_static': out['CTL-B_h2_static']['joint']
    - (-1.9423115870905664e-04),
    'diff_full': out['CTL-B_h2_full']['joint']
    - (-1.9423115870905664e-04)}
save()

LAD = G.INP['ladder404']
if 'CTL-C_fix_0.171875' not in out:
    read_block('CTL-C_fix_0.171875', G.prof_fixed(0.171875),
               stored=LAD['0.171875'])
if 'CTL-C_fix_0.5' not in out:
    read_block('CTL-C_fix_0.5', G.prof_fixed(0.5),
               stored=LAD['0.5'])
if 'fix_0.05' not in out:
    lad_full = json.load(open(f'{WP}/phase404/results/'
                              'p404_ladder.json'))
    row05 = [r for r in lad_full['table'] if r['muS'] == 0.05][0]
    read_block('fix_0.05', G.prof_fixed(0.05), stored=row05)

# ---------------- claim (a): the winner
C405 = G.INP['conf405']['at_criterion']
WIN405_STORED = {'joint': C405['joint'], 'nec_min': C405['nec_min'],
                 'dec_min': C405['dec_min'],
                 'wec_min': C405['wec_min'],
                 'sec_min': C405['sec_min'],
                 'rho_min': C405['rho_min'],
                 'typeI_fraction': C405['typeI_fraction'],
                 'nec_argmin_r': C405['nec_argmin_r'],
                 'worst_null_at_nec_argmin':
                 C405['worst_null_at_nec_argmin']}
if 'claim_a_winner' not in out:
    read_block('claim_a_winner', G.prof_winner405,
               stored=WIN405_STORED, do_wn=True)

# ---------------- claim (c): winner cost-curve points
if 'winner_p0.05' not in out:
    read_block('winner_p0.05', G.prof_winner_at_peak(0.05))
if 'winner_p0.25' not in out:
    read_block('winner_p0.25', G.prof_winner_at_peak(0.25),
               do_wn=True)

# ---------------- claim (d): Stage B's shape
B375 = G.INP['screen_B375']
if 'claim_d_shapeB' not in out:
    read_block('claim_d_shapeB', G.prof_shapeB,
               stored={'joint': B375['joint'],
                       'nec_min': B375['nec_min'],
                       'dec_min': B375['dec_min'],
                       'sec_min': B375['sec_min'],
                       'typeI_fraction': B375['typeI_fraction'],
                       'nec_argmin_r': B375['nec_argmin_r']})

# ---------------- claim (b): peaks and shape anatomy
if 'claim_b_peaks' not in out:
    pk_w = G.peak_read(G.prof_winner405)
    pk_h2 = G.peak_read(lambda r: G.h2_totals(r))
    dense_r = np.linspace(10.0, 20.0, 20001)
    Sw = G.prof_winner405(dense_r)[0]
    Sh2 = G.h2_totals(dense_r)[0]
    dS, dSp, _dSpp = G.corr(G.SHAPEC_CRIT, 9)(dense_r)
    i_w = int(np.argmax(np.abs(Sw)))
    i_h = int(np.argmax(np.abs(Sh2)))
    out['claim_b_peaks'] = {
        'winner_FINE_R': {'peak': pk_w['peak_abs_beta_S'],
                          'peak_radius': pk_w['peak_radius'],
                          'stored_peak': 0.44267424902674035},
        'H2_FINE_R': {'peak': pk_h2['peak_abs_beta_S'],
                      'peak_radius': pk_h2['peak_radius'],
                      'stored_peak': 0.8853484980534808},
        'half_H2_peak_gate': 0.5 * pk_h2['peak_abs_beta_S'],
        'SS7_bar_stored': G.SS7_BAR,
        'winner_peak_minus_bar': pk_w['peak_abs_beta_S']
        - G.SS7_BAR,
        'dense_winner': {'argmax_r': float(dense_r[i_w]),
                         'max_abs_S': float(np.abs(Sw[i_w])),
                         'S_at_10': float(Sw[0]),
                         'S_at_20': float(Sw[-1]),
                         'monotone_decreasing':
                         bool(np.all(np.diff(Sw) <= 0.0)),
                         'max_Sp_on_dense': float(np.max(dSp)),
                         'min_Sp_on_dense': float(np.min(dSp))},
        'dense_H2': {'argmax_r': float(dense_r[i_h]),
                     'max_abs_S': float(np.abs(Sh2[i_h])),
                     'S_at_10': float(Sh2[0])},
        'winner_S_at_fragile': float(
            G.prof_winner405(np.array([17.926829268292682]))[0][0]),
        'peak_over_H2peak': pk_w['peak_abs_beta_S']
        / pk_h2['peak_abs_beta_S']}
    save()
    print('claim_b_peaks done', flush=True)

# ---------------- claim (c): assembled comparison
if 'claim_c_costs' not in out:
    base_joint = out['CTL-A_base_winner']['joint']
    w_joint = out['claim_a_winner']['joint']
    f_joint = out['CTL-C_fix_0.5']['joint']
    f_017 = out['CTL-C_fix_0.171875']['joint']
    f_005 = out['fix_0.05']['joint']
    w_005 = out['winner_p0.05']['joint']
    w_025 = out['winner_p0.25']['joint']
    cost = lambda j: base_joint - j  # noqa: E731
    cw_crit, cf_crit = cost(w_joint), cost(f_joint)
    out['claim_c_costs'] = {
        'base_joint': base_joint,
        'winner_cost_at_criterion': cw_crit,
        'fixed_cost_at_criterion': cf_crit,
        'ratio_fixed_over_winner': cf_crit / cw_crit,
        'winner_cost_at_0.05': cost(w_005),
        'winner_cost_at_0.25': cost(w_025),
        'fixed_cost_at_0.171875': cost(f_017),
        'fixed_cost_at_0.05': cost(f_005),
        'winner_eff_coef_crit': cw_crit / 0.44267424902674035 ** 2,
        'fixed_eff_coef_crit': cf_crit / 0.44267424902674035 ** 2,
        'winner_two_point_exponent_0.05_to_crit':
        float(np.log(cw_crit / cost(w_005))
              / np.log(0.44267424902674035 / 0.05)),
        'winner_two_point_exponent_0.25_to_crit':
        float(np.log(cw_crit / cost(w_025))
              / np.log(0.44267424902674035 / 0.25)),
        'fixed_two_point_exponent_0.171875_to_0.5':
        float(np.log(cf_crit / cost(f_017))
              / np.log(0.44267424902674035 / 0.152169273102942)),
        'stored_fixed_cost_at_criterion': 1.0583817900205046e-05,
        'stored_winner_cost_at_criterion': 1.703342300228576e-07}
    save()
    print('claim_c_costs done', flush=True)
print('g50_run complete')
