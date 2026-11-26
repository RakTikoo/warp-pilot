#!/usr/bin/env python3
"""Gate-40 audit programme (resumable, per-audit checkpoint files):
- J=32 scan: anchor + all 16 Phase 374 members
- J=128 audit: anchor + all 16 members (the registered consequence, in
  substance, re-executed on gate machinery)
- J=64 audit: refinement members (i) and (ii) only (acceptance statistics)
- stationary scaled reads at constant mu for the bottom identity
Each audit: per-instant SET-244 read + floor check; summaries per SS3."""
import json
import os
import sys
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, '.')
import g40_lib as G
from g40_members import ANCHOR, FAMILY374, bottom_mu

PARTS = '../results/parts'
os.makedirs(PARTS, exist_ok=True)

_CEN = None


def _init():
    global _CEN
    conf = json.load(open('../../phase344/results/p344_confirmation.json'))
    a2 = [c for c in conf['confirmations'] if c['point'] == 'A2'][0]
    _CEN = G.Centre(a2['vS'], a2['vN'], a2['vM'])


def _read(task):
    mem, phi = task
    out = G.set_read(_CEN, mem, phi)
    fl = G.floors_ok(_CEN, mem, phi)
    return {'phi': phi, 'nec': out['nec']['min'], 'wec': out['wec']['min'],
            'dec': out['dec']['min'], 'sec': out['sec']['min'],
            'rho_min': out['rho']['min'], 'floors_ok': fl,
            'nec_argmin_r': out['nec_argmin_r'],
            'nec_argmin_typeI': out['nec_argmin_typeI'],
            'dec_argmin_r': out['dec_argmin_r'],
            'dec_argmin_typeI': out['dec_argmin_typeI']}


def audit(mem, J, pool):
    key = f"{mem['name']}@J{J}"
    path = os.path.join(PARTS, key + '.json')
    if os.path.exists(path):
        return json.load(open(path))
    phis = [2 * np.pi * j / J for j in range(J)]
    rows = pool.map(_read, [(mem, p) for p in phis])
    feas = [r for r in rows if r['floors_ok']]
    src = feas if feas else rows
    Lw = min(src, key=lambda r: min(r['nec'], r['dec']))
    Nw = min(src, key=lambda r: r['nec'])
    Dw = min(src, key=lambda r: r['dec'])
    Lb = max(src, key=lambda r: min(r['nec'], r['dec']))
    out = {'member': mem['name'], 'J': J,
           'L_worst': min(Nw['nec'], Dw['dec']) if False else min(Lw['nec'], Lw['dec']),
           'L_worst_phi': Lw['phi'],
           'NEC_worst': Nw['nec'], 'nec_worst_phi': Nw['phi'],
           'DEC_worst': Dw['dec'], 'dec_worst_phi': Dw['phi'],
           'L_best': min(Lb['nec'], Lb['dec']), 'best_phi': Lb['phi'],
           'min_rho': min(r['rho_min'] for r in rows),
           'n_floor_infeasible': sum(1 for r in rows if not r['floors_ok']),
           'instants': rows}
    # L_worst must be min over instants of L(phi): recompute exactly
    out['L_worst'] = min(min(r['nec'], r['dec']) for r in src)
    out['L_worst_phi'] = min(src, key=lambda r: min(r['nec'], r['dec']))['phi']
    json.dump(out, open(path, 'w'))
    return out


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    pool = Pool(2, initializer=_init)
    summary = {}
    if which in ('all', 'scan32'):
        for mem in [ANCHOR] + FAMILY374:
            a = audit(mem, 32, pool)
            summary[f"{mem['name']}@J32"] = {k: a[k] for k in
                ('L_worst', 'NEC_worst', 'DEC_worst', 'L_best', 'min_rho',
                 'n_floor_infeasible')}
            print('J32', mem['name'], a['L_worst'], a['min_rho'], flush=True)
    if which in ('all', 'audit128'):
        for mem in [ANCHOR] + FAMILY374:
            a = audit(mem, 128, pool)
            summary[f"{mem['name']}@J128"] = {k: a[k] for k in
                ('L_worst', 'NEC_worst', 'DEC_worst', 'L_best', 'min_rho',
                 'n_floor_infeasible')}
            print('J128', mem['name'], a['L_worst'], a['NEC_worst'],
                  a['DEC_worst'], a['min_rho'], flush=True)
    if which in ('all', 'audit64'):
        for nm in ('SNM_a0.15_T640_D0.750_m0.88', 'SNM_a0.30_T640_D0.750_m0.75'):
            mem = [m for m in FAMILY374 if m['name'] == nm][0]
            a = audit(mem, 64, pool)
            summary[f"{nm}@J64"] = {k: a[k] for k in
                ('L_worst', 'NEC_worst', 'DEC_worst', 'L_best', 'min_rho',
                 'n_floor_infeasible')}
            print('J64', nm, a['L_worst'], a['L_best'], flush=True)
    pool.close(); pool.join()
    out_path = f'../results/g40_audit_summary_{which}.json'
    prev = {}
    if os.path.exists(out_path):
        prev = json.load(open(out_path))
    prev.update(summary)
    json.dump(prev, open(out_path, 'w'), indent=1)


if __name__ == '__main__':
    main()
