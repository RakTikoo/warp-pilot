#!/usr/bin/env python3
"""Gate-39 member enumeration (Phase 364 registration SS2) + instant audit."""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate39/work')
import g39_lib as G  # noqa: E402


def member_id(subset, a, T, D, m):
    return f"{subset}_a{a:.2f}_T{T}_D{D:.3f}_m{m:.2f}"


def enumerate_members():
    mems = [{'subset': 'ANCHOR', 'a': 0.0, 'Om': 2 * np.pi / 40.0,
             'D': 0.75, 'm': 0.0, 'id': 'ANCHOR'}]
    for subset in ('M', 'SNM'):
        for a in (0.15, 0.30):
            for D in (0.50, 0.75, 0.875):
                for T in (160, 40):
                    mems.append({'subset': subset, 'a': a,
                                 'Om': 2 * np.pi / T, 'D': D, 'm': 0.0,
                                 'id': member_id(subset, a, T, D, 0.0)})
    for subset in ('M', 'SNM'):
        for T in (160, 40):
            for a, m in ((0.30, 0.50), (0.30, 0.75), (0.15, 0.75)):
                mems.append({'subset': subset, 'a': a,
                             'Om': 2 * np.pi / T, 'D': 0.75, 'm': m,
                             'id': member_id(subset, a, T, 0.75, m)})
    return mems


def audit_member(centre, member, J, want_aux_at=None):
    """Full instant audit at J phases. want_aux_at: optional set of j
    indices for which the SET aux (Type-I points, That) is retained."""
    instants = []
    aux_keep = {}
    for j in range(J):
        phi = 2 * np.pi * j / J
        want = want_aux_at is not None and j in want_aux_at
        out, aux = G.set_read(centre, member, phi, want_aux=want)
        if want:
            aux_keep[j] = (out, aux)
        fok = G.floors_ok(centre, member, phi)
        instants.append({
            'j': j, 'phi': phi,
            'nec_min': out['nec']['min'], 'dec_min': out['dec']['min'],
            'wec_min': out['wec']['min'], 'sec_min': out['sec']['min'],
            'rho_min': out['rho']['min'],
            'nec_argmin_r': out['nec_argmin_r'],
            'dec_argmin_r': out['dec_argmin_r'],
            'dec_argmin_point': out['dec_argmin_point'],
            'dec_argmin_typeI': out['dec_argmin_typeI'],
            'typeI_nec_min': out['typeI_nec_min'],
            'floors_ok': bool(fok),
            'L': min(out['nec']['min'], out['dec']['min'])})
    feas = [it for it in instants if it['floors_ok']]

    def worst(key):
        it = min(feas, key=lambda z: z[key])
        return it
    lw = min(feas, key=lambda z: z['L'])
    lb = max(feas, key=lambda z: z['L'])
    nw = worst('nec_min'); dw = worst('dec_min')
    summ = {
        'member': {k: member[k] for k in ('subset', 'a', 'Om', 'D', 'm', 'id')},
        'J': J,
        'instants': instants,
        'L_worst': lw['L'], 'worst_phi': lw['phi'], 'worst_j': lw['j'],
        'NEC_worst': nw['nec_min'], 'nec_worst_phi': nw['phi'],
        'nec_worst_j': nw['j'],
        'DEC_worst': dw['dec_min'], 'dec_worst_phi': dw['phi'],
        'dec_worst_j': dw['j'],
        'L_best': lb['L'], 'best_phi': lb['phi'], 'best_j': lb['j'],
        'min_rho': min(it['rho_min'] for it in instants),
        'n_floor_infeasible': int(sum(1 for it in instants
                                      if not it['floors_ok'])),
    }
    return summ, aux_keep
