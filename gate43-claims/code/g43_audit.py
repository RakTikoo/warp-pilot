#!/usr/bin/env python3
"""Gate-43 deciding audits (part 1): full SET-244 reads
+ adversary polish + exact worst-null for the control
triples, the mixed centre, and the clamped mixed
centre. Output: gate43/results/g43_numbers.json."""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate43/work')
import g43_lib as G  # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/gate43/results'
MIX = (0.9323593026620368, 1.1444417317708335, 1.1445068359375)
L_H2 = -1.9422459891767227e-4
L_CEIL = -2.099385079591706e-4

STORED = {
    'centre_111': {
        'nec_min': -1.9422459891767227e-4,
        'dec_min': -1.8982585080461558e-4,
        'wec_min': -1.7768467393179327e-3,
        'sec_min': -2.0943799294291577e-3,
        'rho_min': 8.789653555683182e-5,
        'typeI_count': 3262,
        'depth': -1.4402430840320638e-4,
        'worst_null': -1.9432881962794707e-4},
    'mix_383pt': {
        'nec_min': -1.9954038171026746e-4,
        'dec_min': -1.287489042939161e-4},
    'mixed': {
        'nec_min': -0.00017570735537945242,
        'dec_min': -0.00015670690855768682,
        'wec_min': -0.001176749370558998,
        'sec_min': -0.0021496503801466693,
        'rho_min': 8.936712674433238e-05,
        'typeI_count': 3359,
        'depth': -9.660225437141954e-05,
        'worst_null': -0.00017703703917379307},
}


def full_audit(name, triple, clamp=False):
    s, aux = G.set_read(*triple, clamp=clamp)
    pol = G.adversary_polish(*triple, aux, clamp=clamp)
    argpt = np.array(s['nec_argmin_point'], dtype=float)
    _, _, That = G.nec_at(*triple, argpt, clamp=clamp)
    n_fin, q_full, q_fib = G.worst_null(That)
    # multistart confirmation of the worst-null minimum
    def q_of(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)
    vals = np.array([q_of(d) for d in G.DIRS642])
    starts = np.argsort(vals)[:8]
    best = q_full
    from scipy.optimize import minimize
    for si in starts:
        nb = G.DIRS642[si]
        x0 = np.array([np.arccos(np.clip(nb[2], -1, 1)),
                       np.arctan2(nb[1], nb[0])])

        def obj(x):
            th, ph = x
            return q_of(np.array([np.sin(th) * np.cos(ph),
                                  np.sin(th) * np.sin(ph),
                                  np.cos(th)]))
        r_ = minimize(obj, x0, method='Nelder-Mead',
                      options={'maxiter': 400, 'xatol': 1e-10,
                               'fatol': 1e-14})
        best = min(best, float(r_.fun))
    rec = {
        'triple': list(triple), 'clamp': clamp,
        'set': s,
        'joint': float(min(s['nec']['min'], s['dec']['min'])),
        'depth': float(pol['in_region_worst_nec_SAMPLER-M']),
        'depth_point': pol['point'], 'depth_r': pol['r'],
        'depth_source': pol['source'],
        'worst_null': float(q_full),
        'worst_null_fib': float(q_fib),
        'worst_null_multistart_best': float(best),
        'worst_null_dir': n_fin.tolist(),
    }
    st = STORED.get(name)
    if st:
        diffs = {}
        for k, v in st.items():
            got = {'nec_min': s['nec']['min'],
                   'dec_min': s['dec']['min'],
                   'wec_min': s['wec']['min'],
                   'sec_min': s['sec']['min'],
                   'rho_min': s['rho']['min'],
                   'typeI_count': s['typeI_count'],
                   'depth': rec['depth'],
                   'worst_null': rec['worst_null']}[k]
            diffs[k] = (got - v) if k != 'typeI_count' else (
                int(got) - int(v))
        rec['diffs_vs_stored'] = diffs
    print('AUDIT', name, 'joint', rec['joint'], 'depth',
          rec['depth'], 'wn', rec['worst_null'],
          'diffs', rec.get('diffs_vs_stored'), flush=True)
    return rec


def main():
    out = {}
    out['centre_111'] = full_audit('centre_111', (1.0, 1.0, 1.0))
    out['mix_383pt'] = full_audit('mix_383pt', (1.225, 1.30, 1.30))
    out['mixed'] = full_audit('mixed', MIX)
    out['mixed_clamped'] = full_audit('mixed_clamped', MIX,
                                      clamp=True)
    mc = out['mixed_clamped']
    mc['margins'] = {
        'clamped_joint': mc['joint'],
        'clamp_cost_vs_unclamped': float(
            out['mixed']['joint'] - mc['joint']),
        'vs_L_H2': float(mc['joint'] - L_H2),
        'vs_dweller_ceiling': float(mc['joint'] - L_CEIL),
        'unclamped_vs_L_H2': float(out['mixed']['joint'] - L_H2),
        'unclamped_vs_dweller_ceiling': float(
            out['mixed']['joint'] - L_CEIL),
        'worst_null_vs_L_H2': float(
            out['mixed']['worst_null'] - L_H2),
    }
    with open(f'{RES}/g43_numbers.json', 'w') as f:
        json.dump(out, f, indent=1)
    print('AUDITS DONE', flush=True)


if __name__ == '__main__':
    main()
