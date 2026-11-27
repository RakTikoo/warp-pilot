#!/usr/bin/env python
"""g59_audit.py -- Gate-59 main audit of Phase 431's claim set.

All deciding reads use g59_lib (the gate's own implementation).
Objects audited (sha256 recorded before any read):
  - the two target files (410 T_req / 420 T_corr, stored records);
  - the unconstrained primaries (410 Fit A / 420 C-A) -- controls;
  - Phase 431's four matings of record.
Reads: controls CTL-431-0/1/3 re-derived; per mating: t = 0
residuals (field path AND pair path), spectrum, prices,
supplier densities, Dirac residuals, tensor symmetry.
Writes gate59/results/g59_audit.json.
"""
import hashlib
import json
import os
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate59/work')
import g59_lib as G  # noqa: E402

RES = f'{WP}/gate59/results'
BAR = 1e-9

FILES = {
    'targets_t1': f'{WP}/phase410/work/p410_targets.json',
    'targets_t2': f'{WP}/phase420/work/p420_targets.json',
    'fitA_primary': f'{WP}/phase410/work/p410_fitA_primary.json',
    'fitCA_primary': f'{WP}/phase420/work/p420_fitCA_primary.json',
    'p431_results': f'{WP}/phase431/results/p431_results.json',
    'p431_check_results': f'{WP}/phase431/results/p431_check_results.json',
    'p431_admission': f'{WP}/phase431/results/p431_admission.json',
    'p431_supplement': f'{WP}/phase431/results/p431_supplement.json',
    'best_A_t1_N12': f'{WP}/phase431/work/p431_best_A_t1_N12.json',
    'best_B_t1_N6_L3': f'{WP}/phase431/work/p431_best_B_t1_N6_L3.json',
    'best_A_t2_6_6': f'{WP}/phase431/work/p431_best_A_t2_6_6.json',
    'best_B_t2_6_6_L3': f'{WP}/phase431/work/p431_best_B_t2_6_6_L3.json',
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def avecs(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


def load_targets(which):
    tg = json.load(open(FILES[f'targets_{which}']))
    key = 'That' if which == 't1' else 'T_corr'
    XS = [np.array(s['point']) for s in tg['sitesA']]
    TG = [np.array(s[key]) for s in tg['sitesA']]
    keys = [s['key'] for s in tg['sitesA']]
    return XS, TG, keys


out = {'gate': 59, 'phase_audited': 431,
       'hashes_sha256': {k: sha256(v) for k, v in FILES.items()},
       'lib_self_test': G.self_test()}

# ---------------- targets integrity ----------------
XS1, TG1, KEYS = load_targets('t1')
XS2, TG2, _ = load_targets('t2')
out['targets'] = {
    'site_keys': KEYS,
    'sites_match_between_files': bool(
        all(np.array_equal(a, b) for a, b in zip(XS1, XS2))),
    'frobs_t1': [float(np.linalg.norm(t)) for t in TG1],
    'frobs_t2': [float(np.linalg.norm(t)) for t in TG2],
    'inter_target_distance': float(max(
        np.linalg.norm(a - b) for a, b in zip(TG1, TG2))),
    't1_T00': [float(t[0, 0]) for t in TG1],
    't2_T00': [float(t[0, 0]) for t in TG2],
}

# ---------------- controls: primaries ----------------
fa = json.load(open(FILES['fitA_primary']))
pv = np.array(fa['pvecs']); av = avecs(fa['avecs'])
mm = np.full(len(pv), float(fa['m']))
Rs_f, _ = G.site_residuals(pv, av, mm, XS1, TG1, path='field')
Rs_p, _ = G.site_residuals(pv, av, mm, XS1, TG1, path='pair')
out['CTL431_0_fitA'] = {
    'gate_maxR_field': max(Rs_f), 'gate_maxR_pair': max(Rs_p),
    'gate_Rs_field': Rs_f,
    'stored_maxR_pairwise': 2.9659878908312287e-12,
    'stored_maxR_direct': 2.9659839407219894e-12,
    'p431_repro_pairwise': 2.965984413711632e-12,
    'gate_price': G.price(av), 'stored_price': 0.029266406597128584,
}

ca = json.load(open(FILES['fitCA_primary']))
pv1 = np.array(ca['pvecs1']); av1 = avecs(ca['avecs1'])
pv2 = np.array(ca['pvecs2']); av2 = avecs(ca['avecs2'])
pvc = np.vstack([pv1, pv2]); avc = np.vstack([av1, av2])
mmc = np.concatenate([np.full(len(pv1), float(ca['m1'])),
                      np.full(len(pv2), float(ca['m2']))])
Rs_f, _ = G.site_residuals(pvc, avc, mmc, XS2, TG2, path='field')
Rs_p, _ = G.site_residuals(pvc, avc, mmc, XS2, TG2, path='pair')
out['CTL431_1_fitCA'] = {
    'gate_maxR_field': max(Rs_f), 'gate_maxR_pair': max(Rs_p),
    'gate_Rs_field': Rs_f,
    'stored_maxR': 3.49600985773513e-10,
    'gate_price_fam1': G.price(av1), 'stored_fam1': 0.029172052178672605,
    'gate_price_fam2': G.price(av2), 'stored_fam2': 2.0362442383995038e-06,
    'gate_price_total': G.price(avc), 'stored_total': 0.02917408842291128,
}

# CTL-431-3: B-2 self-check objects with the gate's lib:
# Fit A mode 6 (1-based) alone at A1; modes 6 & 2 beat at A1.
xA1 = XS1[0]
pvA = np.array(fa['pvecs']); avA = avecs(fa['avecs'])
mmA = np.full(len(pvA), 1.0)
EA = G.energies(pvA, mmA)
one = (pvA[5:6], avA[5:6], mmA[5:6])
T0 = G.T_field(*one, xA1)
scale1 = np.linalg.norm(T0)
dmax = 0.0
for t in np.linspace(0.0, 50.0, 17):
    dmax = max(dmax, float(np.max(np.abs(
        G.T_field(*one, xA1, t=float(t)) - T0))))
two = (pvA[[5, 1]], avA[[5, 1]], mmA[[5, 1]])
Tb0 = G.T_field(*two, xA1)
scale2 = np.linalg.norm(Tb0)
dE = abs(EA[5] - EA[1])
Tper = 2 * np.pi / dE
err_ret = float(np.max(np.abs(G.T_field(*two, xA1, t=Tper) - Tb0)))
err_anti = float(np.max(np.abs(G.T_field(*two, xA1, t=Tper / 2)
                               - (2 * (Tb0 - 0) - Tb0))))  # placeholder
# anti-phase closed form: T(T/2) = T_ii + T_jj - (cross terms);
# compute directly: single-mode tensors sum minus cross at t=0
Ti = G.T_field(pvA[5:6], avA[5:6], mmA[5:6], xA1)
Tj = G.T_field(pvA[1:2], avA[1:2], mmA[1:2], xA1)
cross0 = Tb0 - Ti - Tj
Tanti_exact = Ti + Tj - cross0
err_anti = float(np.max(np.abs(
    G.T_field(*two, xA1, t=Tper / 2) - Tanti_exact)))
out['CTL431_3_B2_selfcheck_gate'] = {
    'single_mode': {
        'max_abs_T_diff_17_instants': dmax,
        'normalised_by_frob_T0': dmax / scale1,
        'stored_p431': 3.73730200800516e-16,
        'stored_p430': 3.74e-16},
    'two_mode_beat': {
        'DeltaE': float(dE), 'stored_DeltaE': 0.2536221530926388,
        'err_return_normalised': err_ret / scale2,
        'stored_p431_return': 1.2214209375487422e-15,
        'err_antiphase_normalised': err_anti / scale2,
        'stored_p431_antiphase': 2.0357015625812368e-16},
}

# ---------------- the four matings ----------------
MATINGS = {
    'A_t1_N12': ('t1', 'A', [(1.0, 12)], None),
    'B_t1_N6_L3': ('t1', 'B', [(1.0, 6)], [(2, 2, 2)]),
    'A_t2_6_6': ('t2', 'A', [(1.0, 6), (0.0, 6)], None),
    'B_t2_6_6_L3': ('t2', 'B', [(1.0, 6), (0.0, 6)],
                    [(2, 2, 2), (2, 2, 2)]),
}
RES431 = json.load(open(FILES['p431_results']))
CHK431 = json.load(open(FILES['p431_check_results']))
ARMKEY = {'A_t1_N12': 'armA_target1_Treq',
          'B_t1_N6_L3': 'armB_target1_Treq',
          'A_t2_6_6': 'armA_target2_Tcorr',
          'B_t2_6_6_L3': 'armB_target2_Tcorr'}

out['matings'] = {}
for tag, (tgt, kind, fams, counts_list) in MATINGS.items():
    bj = json.load(open(FILES[f'best_{tag}']))
    pv = np.array(bj['pvecs']); av = avecs(bj['avecs'])
    mm = np.array(bj['masses'])
    XS, TG, _ = load_targets(tgt)
    Rs_f, Ts = G.site_residuals(pv, av, mm, XS, TG, path='field')
    Rs_p, _ = G.site_residuals(pv, av, mm, XS, TG, path='pair')
    Ek = G.energies(pv, mm)
    Ebase = float(bj['info_Ebase'])
    rec = {'tag': tag, 'target': tgt, 'kind': kind,
           'gate_maxR_field': max(Rs_f), 'gate_Rs_field': Rs_f,
           'gate_maxR_pair': max(Rs_p),
           'stored_driver_maxR_pairwise': float(bj['maxR']),
           'stored_checker_maxR_direct':
               CHK431['items'][tag]['maxR_direct'],
           'at_bar_gate': bool(max(Rs_f) <= BAR),
           'rhos_sup_gate_T00': [float(T[0, 0]) for T in Ts],
           'stored_rhos_sup':
               RES431['arms'][ARMKEY[tag]]['confirmation']['rhos_sup'],
           'tensor_symmetry_max': float(max(
               np.max(np.abs(T - T.T)) for T in Ts)),
           'dirac_max_residual_gate': max(
               G.dirac_residual(pv[k], float(mm[k]), av[k])
               for k in range(len(pv))),
           'stored_dirac_max_residual':
               RES431['arms'][ARMKEY[tag]]['confirmation']
               ['dirac_max_residual'],
           'Ebase_stored': Ebase,
           'E_recomputed_gate': Ek.tolist()}
    # prices per family
    prices = {}
    pos = 0
    for fi, (m, N) in enumerate(fams):
        prices[f'family{fi + 1}_m{m}'] = G.price(av[pos:pos + N])
        pos += N
    rec['prices_gate'] = prices
    rec['price_total_gate'] = G.price(av)
    rec['stored_prices'] = RES431['arms'][ARMKEY[tag]]['confirmation'][
        'abs_a2_per_family']
    # spectrum
    if kind == 'A':
        rec['spectrum_scatter_gate'] = float(Ek.max() - Ek.min())
        rec['spectrum_max_dev_from_Ebase_gate'] = float(
            np.max(np.abs(Ek - Ebase)))
    else:
        rungs = []
        for counts in counts_list:
            rungs += [n + 1 for n, c in enumerate(counts)
                      for _ in range(c)]
        rungs = np.array(rungs, dtype=float)
        rec['rungs_in_stored_order'] = rungs.tolist()
        rec['spectrum_max_ratio_dev_gate'] = float(
            np.max(np.abs(Ek / Ebase - rungs)))
        rec['spectrum_sorted_ratio_dev_gate'] = float(
            np.max(np.abs(np.sort(Ek / Ebase) - np.sort(rungs))))
    out['matings'][tag] = rec
    print(tag, 'gate field maxR =', max(Rs_f), ' pair maxR =',
          max(Rs_p), ' stored =', bj['maxR'], flush=True)

json.dump(out, open(f'{RES}/g59_audit.json', 'w'), indent=1,
          default=str)
print('written g59_audit.json')
