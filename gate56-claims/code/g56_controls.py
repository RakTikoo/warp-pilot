#!/usr/bin/env python3
"""
g56_controls.py -- Gate-56 calibrations (CAL-1..5) and
controls (CTL-*) on gate machinery, run BEFORE the claim
reads (registration SS3). The lineage's machinery is
imported ONLY as calibration comparators, never in a
deciding path. Output: gate56/results/g56_controls.json.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate56/work')
import g56_lib as G  # noqa: E402
import g56_splines as GS  # noqa: E402

OUT = {'calibrations': {}, 'controls': {}}


def jdump(x):
    return json.loads(json.dumps(x, default=lambda o: (
        float(o) if isinstance(o, (np.floating, np.integer))
        else o.tolist() if isinstance(o, np.ndarray) else str(o))))


# ------------------------------------------------ configs
def cfg_of(d, KB=None, KS=None):
    return {'muN': float(d['muN']), 'muM': float(d['muM']),
            'K_B': int(KB if KB is not None else d.get('K_B', d.get('K', 17))),
            'vN': d.get('vN'), 'vM': d.get('vM'),
            'K_S': int(KS if KS is not None else d.get('K_S', 9)),
            'vS': d.get('vS_scaled', d.get('vS'))}


screens418 = [json.loads(ln) for ln in
              open(f'{WP}/phase418/results/p418_screens.jsonl')]
scr0 = screens418[0]
BASE400 = cfg_of(scr0)                       # 400 base, K_B 17
BASE400_STATIC = dict(BASE400, vS=None)
conf405 = json.load(open(f'{WP}/phase405/results/p405_confirmation.json'))
CFG405 = dict(BASE400,
              vS=conf405['shapeC_knots_at_criterion'], K_S=9)
base414 = json.load(open(f'{WP}/phase414/results/p414_base.json'))
B1 = cfg_of(base414, KB=9)
B1_STATIC = dict(B1, vS=None)
state414 = json.load(open(f'{WP}/phase414/results/p414_state2.json'))
t1 = state414['incumbents']['T1K17|K17|0.4426742490']
CFG_B1T1 = dict(B1, vS=t1['vS_scaled'], K_S=17)
CFGH2 = {'muN': 1.0, 'muM': 1.0, 'K_B': 17, 'vN': None,
         'vM': None, 'K_S': 9, 'vS': None}

# P* config: search 412's stored artefacts for the winner
# whose joint is J2_400.
J2 = 6.699288757141148e-07
CFGPSTAR = None
for path in (f'{WP}/phase412/results/p412_state.json',
             f'{WP}/phase412/results/p412_rungs.json'):
    try:
        doc = json.load(open(path))
    except Exception:
        continue
    stack = [doc]
    while stack and CFGPSTAR is None:
        cur = stack.pop()
        if isinstance(cur, dict):
            if abs(cur.get('joint', 1) - J2) < 1e-15 \
                    and cur.get('vS_scaled') is not None:
                merged = dict(BASE400)
                merged.update(cur)
                CFGPSTAR = cfg_of(merged)
                break
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
OUT['pstar_config_found'] = CFGPSTAR is not None

# ------------------------------------------------ CAL-1
from scipy.interpolate import CubicSpline  # noqa: E402
rr = np.linspace(10.0, 20.0, 2001)
cal1 = {}
for name, K, vec in (('A2_vN_K33', 33, G.A2_VN),
                     ('H2_vM_K17', 17, G.H2_VM),
                     ('G50_knots_K9', 9,
                      np.array([0.40243113547885484,
                                0.23237610808870765,
                                0.10110504581235646,
                                0.030274386301308052,
                                0.021559512630984955,
                                0.01297222477301449,
                                0.007865452045132022,
                                0.0035285750792539276,
                                -0.00043513901545560714]))):
    xk = np.linspace(10.0, 20.0, K)
    mine = GS.NotAKnotSpline(xk, vec)
    ref = CubicSpline(xk, vec, bc_type='not-a-knot')
    v0, v1, v2 = mine.eval_all(rr)
    cal1[name] = {
        'value': float(np.max(np.abs(v0 - ref(rr)))),
        'd1': float(np.max(np.abs(v1 - ref.derivative(1)(rr)))),
        'd2': float(np.max(np.abs(v2 - ref.derivative(2)(rr))))}
OUT['calibrations']['CAL-1_spline_vs_scipy'] = cal1

# ------------------------------------------------ lineage comparators
for p in (f'{WP}', f'{WP}/phase235/work', f'{WP}/phase258/work',
          f'{WP}/phase267/work', f'{WP}/phase274/work',
          f'{WP}/phase316/work', f'{WP}/phase317/work',
          f'{WP}/phase324/work', f'{WP}/phase338/work',
          f'{WP}/phase341/work', f'{WP}/phase344/work',
          f'{WP}/phase374/work', f'{WP}/phase379/work',
          f'{WP}/phase381/work', f'{WP}/phase398/work',
          f'{WP}/phase405/work', f'{WP}/phase414/work'):
    if p not in sys.path:
        sys.path.insert(0, p)
import verify_metric as vm  # noqa: E402
import p414_lib as L414  # noqa: E402
import p316_lib as L316  # noqa: E402
from p2352_run import margins_chunked  # noqa: E402

rng = np.random.default_rng(5601)
dirs = rng.normal(size=(23, 3))
dirs /= np.linalg.norm(dirs, axis=1)[:, None]
pts_rand = dirs * rng.uniform(10.3, 19.7, 23)[:, None]

# ------------------------------------------------ CAL-2
cal2 = {}
for name, cfg in (('CTL-405WIN', CFG405),):
    mine = G.profiles_g56(cfg, pts_rand)
    base = {'muN': cfg['muN'], 'muM': cfg['muM'],
            'vN': cfg['vN'], 'vM': cfg['vM'], 'K': cfg['K_B']}
    ref = L414.profiles_at414(base, cfg['vS'], cfg['K_S'],
                              pts_rand)
    cal2[name] = [float(np.max(np.abs(a - b)))
                  for a, b in zip(mine, ref)]
OUT['calibrations']['CAL-2_profiles_vs_lineage'] = cal2

# ------------------------------------------------ CAL-3
pr_mine = G.profiles_g56(CFG405, pts_rand)
T_mine, g_mine = G.T_at_g56(pts_rand, pr_mine)
pr_ref = L414.profiles_at414(
    {'muN': CFG405['muN'], 'muM': CFG405['muM'],
     'vN': CFG405['vN'], 'vM': CFG405['vM'], 'K': CFG405['K_B']},
    CFG405['vS'], CFG405['K_S'], pts_rand)
T_ref, g_ref = L316.T_from_SNM(pts_rand, 1.1, *pr_ref)
OUT['calibrations']['CAL-3a_T_vs_lineage'] = float(
    np.max(np.abs(T_mine - T_ref)))
OUT['calibrations']['CAL-3a_g_vs_lineage'] = float(
    np.max(np.abs(g_mine - g_ref)))


def gfunc(pts):
    pr = G.profiles_g56(CFG405, np.asarray(pts, dtype=float))
    return G.metric_g56(np.asarray(pts, dtype=float), pr)


fd = {}
for h in (0.2, 0.1):
    Gfd, _, _ = vm.einstein_at_points(gfunc, pts_rand, h=h,
                                      do_fallback=False)
    fd[f'h={h}'] = float(np.max(np.abs(Gfd / (8 * np.pi)
                                       - T_mine)))
OUT['calibrations']['CAL-3b_T_vs_FD_judge'] = fd

# ------------------------------------------------ CAL-4 / CAL-5
That_ref = vm.eulerian_that(g_ref, T_ref)
That_mine = G.eulerian_that_g56(g_ref, T_ref)
OUT['calibrations']['CAL-4_That_vs_lineage'] = float(
    np.max(np.abs(That_mine - That_ref)))
m_ref = margins_chunked(That_ref)
m_mine = G.margins_g56(That_ref)
cal5 = {}
for k in ('nec', 'wec', 'sec', 'dec'):
    cal5[k] = float(np.nanmax(np.abs(m_mine[k] - m_ref[k])))
cal5['typeI_agree'] = bool(np.all(m_mine['typeI']
                                  == m_ref['typeI']))
OUT['calibrations']['CAL-5_margins_vs_lineage'] = cal5

# B1T1 That has non-Type-I points: exercise the sampled
# fallback comparison there too.
pr_b = G.profiles_g56(CFG_B1T1, pts_rand)
T_b, g_b = G.T_at_g56(pts_rand, pr_b)
That_b = vm.eulerian_that(g_b, T_b)
mb_ref = margins_chunked(That_b)
mb_mine = G.margins_g56(That_b)
cal5b = {'n_nonI': int(np.sum(~mb_ref['typeI']))}
for k in ('nec', 'wec', 'sec', 'dec'):
    cal5b[k] = float(np.nanmax(np.abs(mb_mine[k] - mb_ref[k])))
OUT['calibrations']['CAL-5b_margins_nonTypeI'] = cal5b

# ------------------------------------------------ controls
TARGETS = {
    'CTL-405WIN': (CFG405, {
        'joint': 1.2273852081052888e-06,
        'sec_min': -0.0002213556504990559,
        'rho_min': 9.943368188592765e-05,
        'nec_argmin_r': 17.926829268292682,
        'worst_null': 7.282191364112375e-07,
        'typeI_fraction': 1.0}),
    'CTL-B1T1': (CFG_B1T1, {
        'joint': -4.60458433226168e-06,
        'sec_min': -0.000728237917620445,
        'nec_argmin_r': 16.21951219512195,
        'worst_null': -4.666009738694515e-06,
        'typeI_fraction': 0.8389039445950015}),
    'CTL-400STAT': (BASE400_STATIC, {
        'joint': 1.3977194851281464e-06}),
    'CTL-B1STAT': (B1_STATIC, {
        'joint': 6.257021665543401e-06,
        'sec_min': -0.0007149443971550401}),
}
if CFGPSTAR is not None:
    TARGETS['CTL-PSTAR'] = (CFGPSTAR, {
        'joint': J2, 'sec_min': -0.0002917201236465074,
        'nec_argmin_r': 18.170731707317074,
        'worst_null': 1.657750767723178e-07,
        'typeI_fraction': 1.0})

for name, (cfg, tgt) in TARGETS.items():
    rec = G.set_read_g56(cfg)
    pt = G.point_read_g56(cfg, rec['nec_argmin_pt'])
    got = {'joint': rec['joint'], 'nec_min': rec['nec_min'],
           'dec_min': rec['dec_min'], 'wec_min': rec['wec_min'],
           'sec_min': rec['sec_min'], 'rho_min': rec['rho_min'],
           'nec_argmin_r': rec['nec_argmin_r'],
           'typeI_fraction': rec['typeI_fraction'],
           'worst_null_exact': pt['worst_null']['value'],
           'worst_null_scan': pt['worst_null_scan_polish']['scan'],
           'worst_null_polish': pt['worst_null_scan_polish']['polish'],
           'wn_cert_resid': pt['worst_null']['cert_resid'],
           'wn_cert_norm': pt['worst_null']['cert_norm']}
    diffs = {}
    for k, v in tgt.items():
        gk = 'worst_null_exact' if k == 'worst_null' else k
        if gk in got:
            diffs[k] = got[gk] - v
    OUT['controls'][name] = {'got': got, 'targets': tgt,
                             'diffs': diffs}
    print(name, 'joint diff', diffs.get('joint'),
          'wn diff', diffs.get('worst_null'))

# CTL-B1T1 argmin-point reproduction: the phase's joint is
# the sampled NEC at its own (non-Type-I) argmin point
# (shell r = 16.21951219512195, dir 25); the frame-invariant
# anchor is the worst-null there. The gate's global sampled
# joint differs by -7.1e-8 (its argmin sits one shell up):
# the C-10 frame-convention band for sampled minima at
# non-Type-I points -- the two pipelines' Eulerian triads
# differ by a transverse rotation there (That diff 6.1e-6
# at T/g agreement 1e-15), while at the phase's argmin
# point both sampled and exact reads reproduce.
pt25 = (G.DIRS162 * 16.21951219512195)[25]
pr25 = G.point_read_g56(CFG_B1T1, pt25)
OUT['controls']['CTL-B1T1']['argmin_point_reproduction'] = {
    'sampled_nec': pr25['nec'],
    'sampled_nec_target': -4.60458433226168e-06,
    'sampled_nec_diff': pr25['nec'] + 4.60458433226168e-06,
    'worst_null_exact': pr25['worst_null']['value'],
    'worst_null_target': -4.666009738694515e-06,
    'worst_null_diff': pr25['worst_null']['value']
    + 4.666009738694515e-06,
    'typeI': pr25['typeI']}
print('CTL-B1T1 argmin point: sampled diff',
      pr25['nec'] + 4.60458433226168e-06,
      'wn diff', pr25['worst_null']['value']
      + 4.666009738694515e-06)

# CTL-H2CENTRE: the full H2 centre (incl. its own S
# sector) read directly from the gate's totals.
def set_read_profiles(pr_at_radii):
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec',
                           'sec', 'rho')}
    for i, rr in enumerate(G.R_NODES):
        pts = G.DIRS162 * rr
        pr = pr_at_radii(rr, pts)
        T, g = G.T_at_g56(pts, pr)
        That = G.eulerian_that_g56(g, T)
        m = G.margins_g56(That)
        for k in rec:
            rec[k].append(m[k] if k != 'rho'
                          else That[:, 0, 0])
    R = {k: np.concatenate(v) for k, v in rec.items()}
    return {'joint': float(min(R['nec'].min(),
                                R['dec'].min())),
            'nec_min': float(R['nec'].min()),
            'dec_min': float(R['dec'].min()),
            'sec_min': float(R['sec'].min()),
            'rho_min': float(R['rho'].min()),
            'typeI_fraction': float(np.mean(R['typeI']))}


def h2_centre_pr(rr, pts):
    r = np.linalg.norm(pts, axis=1)
    return G.h2_totals(r)


h2c = set_read_profiles(h2_centre_pr)
OUT['controls']['CTL-H2CENTRE'] = {
    'got': h2c,
    'targets': {'joint': -1.9422459891767227e-04,
                'sec_min': -2.0943799294291577e-03,
                'rho_min': 8.789653555683182e-05},
    'diffs': {k: h2c[k] - v for k, v in
              {'joint': -1.9422459891767227e-04,
               'sec_min': -2.0943799294291577e-03,
               'rho_min': 8.789653555683182e-05}.items()}}
print('CTL-H2CENTRE diffs',
      OUT['controls']['CTL-H2CENTRE']['diffs'])

# 405WIN adversary polish control (Gate-50 record value)
pol = G.adversary_polish_g56(CFG405, G.set_read_g56(CFG405))
OUT['controls']['CTL-405WIN']['polish'] = {
    'value': pol['value'], 'r': pol['r'],
    'target': 1.214723699102956e-06,
    'diff': pol['value'] - 1.214723699102956e-06}
print('CTL-405WIN polish', pol['value'],
      'diff', pol['value'] - 1.214723699102956e-06)

with open(f'{WP}/gate56/results/g56_controls.json', 'w') as fh:
    json.dump(jdump(OUT), fh, indent=1)
print('wrote gate56/results/g56_controls.json')
print(json.dumps(jdump(OUT['calibrations']), indent=1))
