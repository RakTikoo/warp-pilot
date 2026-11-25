#!/usr/bin/env python3
"""
g35_item2.py -- Gate-35 Item 2 driver: controls C-G2 / C-G3
first, then the independent re-read of the Phase 314 headline
member, all with g35_lib's own symbolic assembly.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate35/work')
import g35_lib as G  # noqa: E402

WP = '/home/hatch/workspace/warp-pilot'
TOL = 1e-9


def rel(a, b):
    return abs(a - b) / max(abs(b), 1e-300)


def cmpv(name, got, stored, out):
    d = got - stored
    out[name] = {'gate': got, 'stored': stored, 'diff': d,
                 'rel_diff': rel(got, stored),
                 'within_1e-9_rel': bool(rel(got, stored) <= TOL)}
    return out[name]


def main():
    t0 = time.time()
    res = {'assembly': 'sympy spherical Einstein tensor, lambdified; '
                       'Cartesian Jacobian transform; Eulerian frame '
                       'via verify_metric.eulerian_that'}
    p312 = json.load(open(f'{WP}/phase312/results/p312_results.json'))
    c1 = json.load(open(f'{WP}/phase312/results/p312_controls.json'))
    c1m = c1['C1_member']
    p314 = json.load(open(f'{WP}/phase314/results/p314_results.json'))
    head = p314['headline_member']

    # ---------------- assembly internal certificate: split vs tensor
    rng = np.random.default_rng(35)
    dirs = rng.normal(size=(20, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    rpts = dirs * rng.uniform(10.0, 20.0, size=(20, 1))
    cert = {}
    for mode in ('one', 'headline'):
        That = G.That_at(rpts, mode)
        sp_ = G.rho_split(rpts, mode)
        rd = np.abs(sp_['rho_split'] - That[:, 0, 0]) / np.maximum(
            np.abs(That[:, 0, 0]), 1e-300)
        cert[mode] = {'max_rel_diff_20_random_pts': float(np.max(rd)),
                      'max_abs_diff': float(np.max(np.abs(
                          sp_['rho_split'] - That[:, 0, 0])))}
    res['split_crosscheck_random20'] = cert

    # ---------------- C-G2: M == 1
    out1, aux1 = G.set_read('one')
    pol1 = G.adversary_polish('one', aux1)
    sites1, depth1 = G.pick_sites(aux1, pol1)
    recs1 = {k: G.site_record('one', k, sites1[k])
             for k in ('S1', 'S2', 'S3', 'S4')}
    cg2 = {}
    cmpv('depth', depth1, -0.001386956608122417, cg2)
    cmpv('set_nec_min', out1['nec']['min'], -0.004079744835667814, cg2)
    cg2['typeI_count'] = {'gate': out1['typeI_count'], 'stored': 1245,
                          'exact': bool(out1['typeI_count'] == 1245)}
    cmpv('polish_r', pol1['r'], 12.369476376022238, cg2)
    stored_sites1 = {s['key']: s for s in c1m['sites']}
    cg2['site_rho'] = {}
    for k in ('S1', 'S2', 'S3', 'S4'):
        cmpv(k, recs1[k]['rho_req_tensor'], stored_sites1[k]['rho_req'],
             cg2['site_rho'])
        cg2['site_rho'][k]['gate_r'] = recs1[k]['r']
        cg2['site_rho'][k]['stored_r'] = stored_sites1[k]['r']
        cg2['site_rho'][k]['split_rel_diff'] = recs1[k]['split_rel_diff']
    cg2['pass'] = bool(cg2['depth']['within_1e-9_rel']
                       and cg2['set_nec_min']['within_1e-9_rel']
                       and cg2['typeI_count']['exact']
                       and cg2['polish_r']['within_1e-9_rel']
                       and all(v['within_1e-9_rel']
                               for v in cg2['site_rho'].values()))
    cg2['set'] = out1
    cg2['polish'] = pol1
    res['C-G2'] = cg2
    print('C-G2 pass:', cg2['pass'], flush=True)
    for k, v in cg2.items():
        if isinstance(v, dict) and 'rel_diff' in v:
            print(' ', k, v['gate'], 'vs', v['stored'], 'rel', v['rel_diff'])
    print('  typeI', cg2['typeI_count'], flush=True)
    for k, v in cg2['site_rho'].items():
        print('  site', k, v['gate'], 'vs', v['stored'], 'rel',
              v['rel_diff'], 'r', v['gate_r'], 'vs', v['stored_r'],
              flush=True)

    # ---------------- C-G3 + headline re-read
    outh, auxh = G.set_read('headline')
    cg3 = {}
    cmpv('rho_min', outh['rho']['min'], 8.272455e-05, cg3)
    cmpv('rho_min_full_precision', outh['rho']['min'],
         head['set']['rho']['min'], cg3)
    cmpv('nec_min', outh['nec']['min'], -1.170007e-03, cg3)
    cmpv('nec_min_full_precision', outh['nec']['min'],
         head['set']['nec']['min'], cg3)
    cmpv('wec_min', outh['wec']['min'], -1.044069e-02, cg3)
    cmpv('wec_min_full_precision', outh['wec']['min'],
         head['set']['wec']['min'], cg3)
    cmpv('dec_min', outh['dec']['min'], -1.000003, cg3)
    cmpv('dec_min_full_precision', outh['dec']['min'],
         head['set']['dec']['min'], cg3)
    cg3['typeI_count'] = {'gate': outh['typeI_count'], 'stored': 2615,
                          'exact': bool(outh['typeI_count'] == 2615)}
    cg3['rho_argmin'] = outh['rho_argmin']
    cg3['rho_argmin_stored_r'] = 19.878049
    # full-precision values are the binding comparison; the rounded
    # registration values are reported alongside.
    cg3['pass'] = bool(cg3['rho_min_full_precision']['within_1e-9_rel']
                       and cg3['nec_min_full_precision']['within_1e-9_rel']
                       and cg3['wec_min_full_precision']['within_1e-9_rel']
                       and cg3['dec_min_full_precision']['within_1e-9_rel']
                       and cg3['typeI_count']['exact'])
    res['C-G3'] = cg3
    print('C-G3 pass:', cg3['pass'], flush=True)
    for k, v in cg3.items():
        if isinstance(v, dict) and 'rel_diff' in v:
            print(' ', k, v['gate'], 'vs', v['stored'], 'rel', v['rel_diff'])
    print('  typeI', cg3['typeI_count'], 'argmin', outh['rho_argmin'],
          flush=True)

    # headline polish + binding sites
    polh = G.adversary_polish('headline', auxh)
    sitesh, depthh = G.pick_sites(auxh, polh)
    recsh = {k: G.site_record('headline', k, sitesh[k])
             for k in ('S1', 'S2', 'S3', 'S4')}
    stored_sitesh = {s['key']: s for s in head['sites']}
    rr = {'depth': {'gate': depthh,
                    'stored': head['depth_SAMPLER-M_polished'],
                    'diff': depthh - head['depth_SAMPLER-M_polished']},
          'polish': polh,
          'polish_stored': head['polish'],
          'set': outh, 'set_stored': head['set'], 'sites': {}}
    for k in ('S1', 'S2', 'S3', 'S4'):
        g_, s_ = recsh[k], stored_sitesh[k]
        rr['sites'][k] = {
            **g_,
            'stored': {'r': s_['r'], 'typeI': s_['typeI'],
                       'rho_req': s_['rho_req'],
                       'nec_SAMPLER-M': s_['nec_SAMPLER-M'],
                       'nec_exact_pointwise': s_['nec_exact_pointwise']},
            'diffs': {'rho_req': g_['rho_req_tensor'] - s_['rho_req'],
                      'nec_SAMPLER-M': (g_['nec_SAMPLER-M']
                                        - s_['nec_SAMPLER-M']),
                      'nec_exact_pointwise': (g_['nec_exact_pointwise']
                                              - s_['nec_exact_pointwise']),
                      'r': g_['r'] - s_['r']}}
    # binding-site split certificate (tensor vs split at the 4 sites)
    rr['binding_site_split_max_rel_diff'] = float(max(
        recsh[k]['split_rel_diff'] for k in recsh))
    res['headline_reread'] = rr
    print('headline depth gate', depthh, 'stored',
          head['depth_SAMPLER-M_polished'], flush=True)
    for k in ('S1', 'S2', 'S3', 'S4'):
        print(' ', k, 'rho gate', recsh[k]['rho_req_tensor'], 'stored',
              stored_sitesh[k]['rho_req'], 'splitrel',
              recsh[k]['split_rel_diff'], flush=True)
    res['wall_s'] = time.time() - t0
    with open(f'{WP}/gate35/work/g35_item2_results.json', 'w') as f:
        json.dump(res, f, indent=1)
    print('DONE wall', res['wall_s'], flush=True)


if __name__ == '__main__':
    main()
