#!/usr/bin/env python3
"""
g46_run.py -- Gate-46 deciding reads (single process; the
sympy lambdify import is paid once).

Outputs:
  results/g46_numbers.json      -- claim (a)/(b): batch reads
                                   for centre + 4 controls with
                                   diffs vs stored; named-point
                                   frame-invariant reads and
                                   worst-nulls.
  results/g46_clamp_margins.json-- claim (c): clamp cross-
                                   checks (C-3) + clamped centre
                                   + margins.
  results/g46_ray_box.json      -- claim (d) re-reads: worst-
                                   DEC subject, DIAG trace,
                                   RAY2 trace; C-2 FD cross-path.
"""
import json
import os
import time

import numpy as np

import g46_lib as L
import g46_profiles as P

WP = '/home/hatch/workspace/warp-pilot'
RES = f'{WP}/gate46/results'
os.makedirs(RES, exist_ok=True)

CENTRE = (0.601180962300002, 1.5934531363763935, 4.887238651223381)
ANCHOR = (0.8015689430763502, 1.3179449338854314, 3.574968377899082)
MIX = (0.9323593026620368, 1.1444417317708335, 1.1445068359375)
SEED = (0.9323593026620368, 1.1444417317708335, 2.289013671875)
H2S = (1.0, 1.0, 1.0)

STORED = {
    'H2S': {'nec': -1.9422459891767227e-04, 'dec': -1.8982585080461558e-04,
            'wec': -1.7768467393179327e-03, 'sec': -2.0943799294291577e-03,
            'rho': 8.789653555683182e-05, 'typeI_count': 3262,
            'nec_argmin_r': 16.21951219512195, 'worst_null': None},
    'MIX': {'nec': -1.7570735537945242e-04, 'dec': -1.5670690855768682e-04,
            'wec': -1.176749370558998e-03, 'sec': -2.1496503801466693e-03,
            'rho': 8.936712674433238e-05, 'typeI_count': 3359,
            'nec_argmin_r': 12.560975609756097,
            'worst_null': -1.7703703917379307e-04},
    'SEED': {'nec': -1.2413718983790085e-04, 'dec': -3.4350860761739224e-05,
             'wec': -9.443823050476109e-04, 'sec': -1.5236814797256301e-03,
             'rho': 9.46961652955672e-05, 'typeI_count': 3148,
             'nec_argmin_r': 12.317073170731707,
             'worst_null': -1.2477276305772507e-04},
    'ANCHOR': {'nec': -6.812652656191736e-05, 'dec': -4.611098054060287e-06,
               'wec': -4.876872626344858e-04, 'sec': -8.24703941166269e-04,
               'rho': 9.678145350055573e-05, 'typeI_count': 3311,
               'nec_argmin_r': 15.487804878048781,
               'worst_null': -7.173153284502476e-05},
    'CENTRE': {'nec': -2.9809850277749006e-05, 'dec': -1.7766846142506707e-06,
               'wec': -1.2604578745184045e-04, 'sec': -4.6317591386364136e-04,
               'rho': 9.780857711542179e-05, 'typeI_count': 4067,
               'nec_argmin_r': 15.73170731707317,
               'worst_null': -3.0896210095678075e-05},
}
TRIPLES = {'H2S': H2S, 'MIX': MIX, 'SEED': SEED, 'ANCHOR': ANCHOR,
           'CENTRE': CENTRE}


def batch(name, triple, clamp=False):
    t0 = time.time()
    out, _ = L.set_read(*triple, clamp=clamp)
    print(f'batch {name} clamp={clamp}: {time.time() - t0:.0f} s',
          flush=True)
    return out


def diff_block(out, st):
    d = {}
    for k in ('nec', 'dec', 'wec', 'sec', 'rho'):
        d[k] = out[k]['min'] - st[k]
    d['typeI_count'] = out['typeI_count'] - st['typeI_count']
    d['nec_argmin_r'] = out['nec_argmin_r'] - st['nec_argmin_r']
    return d


numbers = {'configs': {}}
named = {}
for name in ('H2S', 'MIX', 'SEED', 'ANCHOR', 'CENTRE'):
    out = batch(name, TRIPLES[name])
    st = STORED[name]
    rec = {'triple': TRIPLES[name], 'gate': out,
           'stored': st, 'diffs': diff_block(out, st)}
    # named-point frame-invariant read at the gate's own
    # NEC argmin point
    pt = np.array(out['nec_argmin_point'])
    That = L.that_at(*TRIPLES[name], pt)
    m = L.margins(That[None, :, :])
    n_fin, wn, wn_fib = L.worst_null(That)
    rec['named_point'] = {
        'point': pt.tolist(),
        'typeI': bool(m['typeI'][0]),
        'nec_eig': float(m['nec'][0]),
        'rho': float(That[0, 0]),
        'worst_null': wn,
        'worst_null_fib': wn_fib,
        'worst_null_stored': st['worst_null'],
        'worst_null_diff': (None if st['worst_null'] is None
                            else wn - st['worst_null']),
    }
    numbers['configs'][name] = rec
    named[name] = rec['named_point']
    print(f'  {name}: joint {out["joint"]:.12e} '
          f'nec_diff {rec["diffs"]["nec"]:+.2e} '
          f'wn_diff {rec["named_point"]["worst_null_diff"]}',
          flush=True)

with open(f'{RES}/g46_numbers.json', 'w') as fh:
    json.dump(numbers, fh, indent=1)
print('g46_numbers.json written', flush=True)

# ---------------- clamp (claim (c)) with C-3 cross-checks
clamp = {}
# C-3 legs: clamped (1,1,1) vs Gate-41/43/45 -2.0872993097613136e-04;
# clamped MIX vs Gate-43 -1.7669632754376664e-04;
# clamped ANCHOR vs Phase 395 stored -6.968822658140883e-05.
for name, stored_clamped in (
        ('H2S', -2.0872993097613136e-04),
        ('MIX', -1.7669632754376664e-04),
        ('ANCHOR', -6.968822658140883e-05)):
    out = batch(f'{name}-clamped', TRIPLES[name], clamp=True)
    clamp[name] = {'gate_clamped_joint': out['joint'],
                   'stored_clamped_joint': stored_clamped,
                   'diff': out['joint'] - stored_clamped,
                   'gate': out}
    print(f'  clamp {name}: {out["joint"]:.12e} '
          f'diff {out["joint"] - stored_clamped:+.2e}', flush=True)

out_c = batch('CENTRE-clamped', CENTRE, clamp=True)
stored_cc = -3.0189206094012074e-05
gate_joint_c = numbers['configs']['CENTRE']['gate']['joint']
clamp['CENTRE'] = {
    'gate_clamped_joint': out_c['joint'],
    'stored_clamped_joint': stored_cc,
    'diff': out_c['joint'] - stored_cc,
    'gate': out_c,
    'clamp_cost_gate': out_c['joint'] - gate_joint_c,
    'clamp_cost_stored': 3.7935581626306804e-07,
    'margin_over_anchor_unclamped_gate':
        out_c['joint'] - STORED['ANCHOR']['nec'],
    'margin_over_anchor_unclamped_stored': 3.7937320467905286e-05,
    'margin_over_LstatH2_gate': out_c['joint'] - STORED['H2S']['nec'],
    'margin_over_LstatH2_stored': 1.640353928236602e-04,
}
print(f'  clamp CENTRE: {out_c["joint"]:.12e} '
      f'diff {out_c["joint"] - stored_cc:+.2e}', flush=True)
with open(f'{RES}/g46_clamp_margins.json', 'w') as fh:
    json.dump(clamp, fh, indent=1)
print('g46_clamp_margins.json written', flush=True)

# ---------------- claim (d) re-reads
raybox = {}
# worst-DEC subject from the recount
wd = (0.8015689430763502, 1.3179449338854314, 3.074968377899082)
out = batch('WORSTDEC', wd)
raybox['worst_dec_subject'] = {
    'triple': wd, 'gate_dec_min': out['dec']['min'],
    'stored_dec_min': -6.5529696405777245e-06,
    'diff': out['dec']['min'] - (-6.5529696405777245e-06),
    'gate_joint': out['joint'], 'stored_joint': -7.820673703308684e-05,
    'dec_argmin_r': out['dec_argmin_r'],
    'dec_argmin_typeI': out['dec_argmin_typeI'],
    'gate': out}
print(f'  worst-dec: gate {out["dec"]["min"]:.12e}', flush=True)

diag_stored = [
    (ANCHOR, -6.812652656191736e-05),
    ((0.7765689430763502, 1.3429449338854313, 3.824968377899082),
     -6.30499077553992e-05),
    ((0.7515689430763501, 1.3679449338854315, 4.074968377899082),
     -5.7546087526425514e-05),
    ((0.7265689430763502, 1.3929449338854314, 4.324968377899082),
     -5.289900410808198e-05),
    ((0.7015689430763502, 1.4179449338854315, 4.574968377899082),
     -4.8180178394382074e-05),
]
diag = []
prev_gate = None
prev_stored = None
for tr, sj in diag_stored:
    if tr == ANCHOR:
        gj = numbers['configs']['ANCHOR']['gate']['joint']
    else:
        gj = batch(f'DIAG{tr[0]:.3f}', tr)['joint']
    diag.append({'triple': list(tr), 'gate_joint': gj,
                 'stored_joint': sj, 'diff': gj - sj,
                 'gate_increment': (None if prev_gate is None
                                    else gj - prev_gate),
                 'stored_increment': (None if prev_stored is None
                                      else sj - prev_stored)})
    prev_gate, prev_stored = gj, sj
    print(f'  diag {tr}: gate {gj:.12e} diff {gj - sj:+.2e}', flush=True)
raybox['diag'] = diag

ray_stored = [
    (3.574968377899082, -6.812652656191736e-05),
    (3.75, -6.912170532920031e-05),
    (4.0, -6.730269399413535e-05),
    (4.25, -6.626715998014582e-05),
    (4.5, -6.572789116222605e-05),
    (4.75, -6.477082379332023e-05),
    (5.0, -6.33373546793503e-05),
]
ray = []
for muM, sj in ray_stored:
    tr = (ANCHOR[0], ANCHOR[1], muM)
    if muM == ANCHOR[2]:
        gj = numbers['configs']['ANCHOR']['gate']['joint']
    else:
        gj = batch(f'RAY{muM}', tr)['joint']
    ray.append({'mu_M': muM, 'gate_joint': gj, 'stored_joint': sj,
                'diff': gj - sj})
    print(f'  ray muM={muM}: gate {gj:.12e} diff {gj - sj:+.2e}',
          flush=True)
raybox['ray2'] = ray

# C-2 FD cross-path at the centre's NEC argmin point
pt = np.array(numbers['configs']['CENTRE']['gate']['nec_argmin_point'])
prof_fn = lambda P: P_.scaled_profiles(  # noqa: E731
    *CENTRE, np.linalg.norm(P, axis=1))
P_ = P
fd = {}
T_sym = L.T_at(*CENTRE, pt[None, :])[0][0]
for h in (0.1, 0.05, 0.025):
    T_fd = L.einstein_fd(pt[None, :], prof_fn, h=h)[0]
    fd[str(h)] = float(np.max(np.abs(T_fd - T_sym)))
    print(f'  FD h={h}: max|dT| {fd[str(h)]:.3e}', flush=True)
raybox['fd_crosspath'] = {'point': pt.tolist(), 'max_abs_dT': fd}

with open(f'{RES}/g46_ray_box.json', 'w') as fh:
    json.dump(raybox, fh, indent=1)
print('g46_ray_box.json written', flush=True)
print('ALL DONE', flush=True)
