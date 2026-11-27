#!/usr/bin/env python3
"""
g48_run.py -- Gate-48 calibrations and deciding reads.
All values from g48_lib (spherical Taylor jets) only.
Writes gate48/results/g48_numbers.json.
"""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate48/work')
import g48_lib as L  # noqa: E402

OUT = '/home/hatch/workspace/warp-pilot/gate48/results/g48_numbers.json'
res = {'organisation': 'forward-mode second-order Taylor jets '
         'of the metric in spherical coordinates (t, r, theta, '
         'phi); loop Christoffel/Ricci contractions in the '
         'spherical basis; spherical orthonormal Eulerian '
         'frame; Hawking-Ellis eigenvalue margins; exact '
         'worst-nulls at named points'}

# ------------------------------------------------ stored data
conf400 = json.load(open(f'{L.WP}/phase400/results/'
                         'p400_confirmation.json'))
cand = conf400['candidate']
WIN = {'muS': 0.0, 'muN': cand['muN'], 'muM': cand['muM'],
       'vN': np.array(cand['vN']), 'vM': np.array(cand['vM']),
       'K': 17}
STORED_WIN = {'nec': 1.3977194851281464e-06,
              'dec': 1.3977194851281464e-06,
              'wec': 1.3977194851281464e-06,
              'sec': -0.00020502915986749415,
              'rho': 9.943380734109653e-05,
              'worst_null': 1.3977194851281464e-06,
              'polished_depth': 1.3761826591108812e-06}
ANCH = {'muS': 0.0, 'muN': 2.386698313835416,
        'muM': 11.968911464156438,
        'vN': np.array([0., 0., 0., 0., 0., 0., -0.02, 0., 0.]),
        'vM': np.zeros(9), 'K': 9}
STORED_ANCH = {'nec': -2.5991706000781927e-07,
               'dec': -2.5991706000781927e-07,
               'wec': -2.5991706000781927e-07,
               'sec': -2.0014278082959033e-04,
               'rho': 9.949830702927364e-05,
               'worst_null': -2.5991706000781927e-07}
EP = {'A': {'mu': (2.386698313835416, 10.718911464156438),
            'stored': {'nec': -6.587071568730905e-07,
                       'dec': -6.587071568730905e-07,
                       'wec': -6.587071568730905e-07,
                       'sec': -2.2216793442105583e-04,
                       'rho': 9.936047786433927e-05,
                       'worst_null': -6.587071568730905e-07}},
      'B': {'mu': (2.633929922196695, 9.76391679857471),
            'stored': {'nec': -7.229718758606569e-07,
                       'dec': -7.229718758606569e-07,
                       'wec': -7.229718758606569e-07,
                       'sec': -2.4179720889569109e-04,
                       'rho': 9.92317425767731e-05,
                       'worst_null': -7.229718758606569e-07}}}
C395_PT = [-15.383488301698574, 2.2228398846289754,
           -2.4277326106594397]
C395_WN_STORED = -3.0896210095678075e-05
H2_PT = [12.330081871976182, -2.9640809161871493,
         -10.112165010538996]
H2_WN_GATE46 = -0.00019432881962794723


def diffs(gate, stored, keys):
    return {k: float(gate[k] - stored[k]) for k in keys}


def full_read(cfg, stored, label):
    out, aux = L.set_read(cfg['muS'], cfg['muN'], cfg['muM'],
                          cfg['vN'], cfg['vM'], cfg['K'])
    pr = L.point_read(cfg['muS'], cfg['muN'], cfg['muM'],
                      cfg['vN'], cfg['vM'], cfg['K'],
                      out['nec_argmin_point'])
    pr['That_eigenvalues'] = np.sort(
        np.linalg.eigvalsh(pr.pop('That'))).tolist()
    gate = {'nec': out['nec_min'], 'dec': out['dec_min'],
            'wec': out['wec_min'], 'sec': out['sec_min'],
            'rho': out['rho_min']}
    d = {'label': label, 'set': out, 'point_at_argmin': pr,
         'gate': gate,
         'worst_null_at_argmin': pr['worst_null']}
    if stored is not None:
        d['stored'] = stored
        d['diffs'] = diffs(gate, stored,
                           ('nec', 'dec', 'wec', 'sec', 'rho'))
        d['worst_null_diff'] = float(pr['worst_null']
                                     - stored['worst_null'])
    print(label, 'joint', out['joint_min_nec_dec'],
          'typeI', out['typeI_count'], flush=True)
    return d


# ------------------------------------------------ C-0 vectors
c0 = {}
for name, a, b in (('A2', L.load_a2(), L.load_a2_state()),
                   ('H2', L.load_h2(), L.load_h2_state())):
    c0[name] = [float(np.max(np.abs(x - y))) for x, y in zip(a, b)]
res['C0_vector_agreement'] = c0

# ------------------------------------------------ C-1 trivial
P = 5
r = np.array([11.0, 13.5, 15.0, 17.68, 19.5])
th = np.array([0.7, 1.1, 1.9, 2.6, 0.3])
ph = np.array([0.2, 2.0, -1.0, 0.9, 2.8])
orig = L.object_profiles
L.object_profiles = lambda *a, **k: (  # noqa: E731
    (np.zeros(P),) * 3
    + (np.ones(P), np.zeros(P), np.zeros(P))
    + (np.ones(P), np.zeros(P), np.zeros(P)))
Gv, Gd, Gdd = L.metric_jets(0.0, 1.0, 1.0, None, None, 9,
                            r, th, ph)
T, _ = L.einstein_from_jets(Gv, Gd, Gdd)
res['C1_trivial_max_abs_T'] = float(np.max(np.abs(T)))
L.object_profiles = orig

# --------------------------------------- C-2 assembly locals
ana = json.load(open(f'{L.WP}/phase400/results/p400_anatomy.json'))
prof = L.object_profiles(0.0, WIN['muN'], WIN['muM'], WIN['vN'],
                         WIN['vM'], 17, np.array([ana['site_r']]))
names = ['S', 'Sp', 'Spp', 'N', 'Np', 'Npp', 'M', 'Mp', 'Mpp']
res['C2_locals_at_winner_site'] = {
    nm: {'gate': float(prof[i][0]), 'stored': ana['locals_at_site'][nm],
         'diff': float(prof[i][0]) - ana['locals_at_site'][nm]}
    for i, nm in enumerate(names)}

# ------------------------------ C-4 That eigenvalues at site
pr_site = L.point_read(0.0, WIN['muN'], WIN['muM'], WIN['vN'],
                       WIN['vM'], 17, ana['site_point'])
ev_gate = np.sort(np.linalg.eigvalsh(pr_site['That']))
ev_st = np.sort(np.array(ana['That_eigenvalues_at_site']))
pr_site.pop('That')
res['C4_site_That_eigenvalues'] = {
    'gate': ev_gate.tolist(), 'stored': ev_st.tolist(),
    'max_abs_diff': float(np.max(np.abs(ev_gate - ev_st))),
    'gate_nec': pr_site['nec'],
    'gate_worst_null': pr_site['worst_null']}

# --------------------------------------- S identically zero
prof_grid = L.object_profiles(0.0, WIN['muN'], WIN['muM'],
                              WIN['vN'], WIN['vM'], 17, L.R_NODES)
res['winner_S_on_grid'] = {
    'max_abs_S': float(np.max(np.abs(prof_grid[0]))),
    'max_abs_Sp': float(np.max(np.abs(prof_grid[1]))),
    'max_abs_Spp': float(np.max(np.abs(prof_grid[2])))}
pts1 = L.DIRS162 * L.R_NODES[20]
rr, tt, pp = L._sph_of_cart(pts1)
Gv1, _, _ = L.metric_jets(0.0, WIN['muN'], WIN['muM'], WIN['vN'],
                          WIN['vM'], 17, rr, tt, pp)
res['winner_S_on_grid']['max_abs_g_ti_shell20'] = float(
    np.max(np.abs(Gv1[:, 0, 1:])))

# ------------------------------------------------ main reads
res['winner'] = full_read(WIN, STORED_WIN, 'winner')
res['anchor'] = full_read(ANCH, STORED_ANCH, 'anchor')
for k in ('A', 'B'):
    muN, muM = EP[k]['mu']
    cfg = {'muS': 0.0, 'muN': muN, 'muM': muM, 'vN': None,
           'vM': None, 'K': 9}
    res[f'endpoint_{k}'] = full_read(cfg, EP[k]['stored'],
                                     f'endpoint_{k}')

# ------------------------------------------------ H2 control
h2, _ = L.set_read(1.0, 1.0, 1.0, None, None, 9)
pr_h2 = L.point_read(1.0, 1.0, 1.0, None, None, 9, H2_PT)
pr_h2['That_eigenvalues'] = np.sort(
    np.linalg.eigvalsh(pr_h2.pop('That'))).tolist()
res['H2_control'] = {
    'set': h2, 'rho_min_stored': 8.789653555683182e-05,
    'rho_min_diff': float(h2['rho_min'] - 8.789653555683182e-05),
    'typeI_count_gate47_C396_context': None,
    'named_point': pr_h2,
    'worst_null_gate46_at_point': H2_WN_GATE46,
    'worst_null_diff_vs_gate46': float(pr_h2['worst_null']
                                       - H2_WN_GATE46)}
print('H2 rho', h2['rho_min'], 'typeI', h2['typeI_count'],
      flush=True)

# ------------------------------------------------ C395 control
c395, _ = L.set_read(0.601180962300002, 1.5934531363763935,
                     4.887238651223381, None, None, 9)
pr_c = L.point_read(0.601180962300002, 1.5934531363763935,
                    4.887238651223381, None, None, 9, C395_PT)
pr_c['That_eigenvalues'] = np.sort(
    np.linalg.eigvalsh(pr_c.pop('That'))).tolist()
res['C395_control'] = {
    'set': c395,
    'stored': {'nec': -2.9809850277749006e-05,
               'dec': -1.7766846142506707e-06,
               'rho': 9.780857711542179e-05,
               'typeI_count': 4067,
               'worst_null_at_argmin': C395_WN_STORED},
    'named_point': pr_c,
    'worst_null_diff': float(pr_c['worst_null'] - C395_WN_STORED),
    'rho_diff': float(c395['rho_min'] - 9.780857711542179e-05),
    'dec_diff': float(c395['dec_min'] - (-1.7766846142506707e-06))}
print('C395 rho', c395['rho_min'], 'typeI', c395['typeI_count'],
      'dec', c395['dec_min'], c395['dec_argmin_typeI'], flush=True)

with open(OUT, 'w') as f:
    json.dump(res, f, indent=1)
print('WROTE', OUT)
