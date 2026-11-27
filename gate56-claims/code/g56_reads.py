#!/usr/bin/env python3
"""
g56_reads.py -- Gate-56 claim reads (a)-(d) and the two
disclosure audits, all on gate machinery (VM, float64).
Output: gate56/results/g56_reads.json.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate56/work')
import g56_lib as G  # noqa: E402

OUT = {}


def jd(x):
    return json.loads(json.dumps(x, default=lambda o: (
        float(o) if isinstance(o, (np.floating, np.integer))
        else o.tolist() if isinstance(o, np.ndarray)
        else str(o))))


def cfg_of(d):
    return {'muN': float(d['muN']), 'muM': float(d['muM']),
            'K_B': int(d.get('K_B', d.get('K', 17))),
            'vN': d.get('vN'), 'vM': d.get('vM'),
            'K_S': int(d.get('K_S', 9)),
            'vS': d.get('vS_scaled', d.get('vS'))}


conf418 = json.load(open(f'{WP}/phase418/results/p418_confirmation.json'))
state418 = json.load(open(f'{WP}/phase418/results/p418_state.json'))
screens = [json.loads(ln) for ln in
           open(f'{WP}/phase418/results/p418_screens.jsonl')]
J1 = 1.2273852081052888e-06
CRIT = 0.4426742490267404


def full_read(cfg, stored, with_polish=True):
    rec = G.set_read_g56(cfg)
    pt = G.point_read_g56(cfg, rec['nec_argmin_pt'])
    out = {
        'joint': rec['joint'], 'nec_min': rec['nec_min'],
        'dec_min': rec['dec_min'], 'wec_min': rec['wec_min'],
        'sec_min': rec['sec_min'], 'rho_min': rec['rho_min'],
        'nec_argmin_r': rec['nec_argmin_r'],
        'dec_argmin_r': rec['dec_argmin_r'],
        'typeI_fraction': rec['typeI_fraction'],
        'typeI_nec_min': rec['typeI_nec_min'],
        'worst_null_exact': pt['worst_null']['value'],
        'wn_cert_resid': pt['worst_null']['cert_resid'],
        'wn_cert_norm': pt['worst_null']['cert_norm'],
        'wn_hard_case': pt['worst_null']['hard_case'],
        'worst_null_scan': pt['worst_null_scan_polish']['scan'],
        'worst_null_polish': pt['worst_null_scan_polish']['polish'],
        'argmin_typeI': pt['typeI'],
        'local_at_nec_argmin': pt['local'],
        'diffs_vs_stored': {}}
    for k in ('joint', 'nec_min', 'dec_min', 'wec_min',
              'sec_min', 'rho_min', 'nec_argmin_r',
              'typeI_fraction'):
        if k in stored:
            out['diffs_vs_stored'][k] = out[k] - stored[k]
    if 'worst_null_at_nec_argmin' in stored:
        out['diffs_vs_stored']['worst_null'] = \
            out['worst_null_exact'] \
            - stored['worst_null_at_nec_argmin']
    if 'local_at_nec_argmin' in stored:
        out['local_diffs'] = {
            k: pt['local'][k] - stored['local_at_nec_argmin'][k]
            for k in stored['local_at_nec_argmin']}
    if with_polish:
        pol = G.adversary_polish_g56(cfg, rec)
        out['polish'] = {'value': pol['value'], 'r': pol['r']}
        if 'adversary_polish' in stored:
            out['polish']['diff'] = pol['value'] \
                - stored['adversary_polish'][
                    'in_region_worst_nec_SAMPLER-M']
            out['polish']['r_diff'] = pol['r'] \
                - stored['adversary_polish']['r']
    pk = G.peak_g56(cfg['vS'], cfg['K_S'])
    out['peak'] = pk
    return out, rec


# ------------------------------------------------ (a) + (b)
cbj_cfg = cfg_of(conf418['criterion_best_joint']['config'])
cb_cfg = cfg_of(conf418['criterion_best']['config'])
cbj_read, _ = full_read(
    cbj_cfg, conf418['criterion_best_joint'])
cb_read, _ = full_read(cb_cfg, conf418['criterion_best'])
OUT['a_cbj_screen1347'] = cbj_read
OUT['a_cb_screen1320'] = cb_read

for name, cfg, stored in (
        ('cbj', cbj_cfg, conf418['criterion_best_joint']),
        ('cb', cb_cfg, conf418['criterion_best'])):
    st = G.set_read_g56(dict(cfg, vS=None))
    OUT[f'b_static_{name}'] = {
        'joint': st['joint'], 'sec_min': st['sec_min'],
        'stored_base_static_joint': stored['base_static_joint'],
        'diff': st['joint'] - stored['base_static_joint'],
        'spend_gate': st['joint'] - OUT[
            'a_cbj_screen1347' if name == 'cbj'
            else 'a_cb_screen1320']['joint'],
        'spend_stored': stored['spend_vs_own_base']}

# three-base spend comparison (gate reads; 400/B1 legs
# recomputed here for a single record)
base400 = cfg_of(screens[0])
st400 = G.set_read_g56(dict(base400, vS=None))
win400 = G.set_read_g56(dict(
    base400, vS=json.load(open(
        f'{WP}/phase405/results/p405_confirmation.json'))[
        'shapeC_knots_at_criterion'], K_S=9))
base414 = json.load(open(f'{WP}/phase414/results/p414_base.json'))
state414 = json.load(open(f'{WP}/phase414/results/p414_state2.json'))
b1 = {'muN': base414['muN'], 'muM': base414['muM'], 'K_B': 9,
      'vN': base414['vN'], 'vM': base414['vM'], 'K_S': 9,
      'vS': None}
stb1 = G.set_read_g56(b1)
t1 = state414['incumbents']['T1K17|K17|0.4426742490']
b1t1 = G.set_read_g56(dict(b1, vS=t1['vS_scaled'], K_S=17))
OUT['b_spend_comparison'] = {
    'SPEND_400_gate': st400['joint'] - win400['joint'],
    'SPEND_400_stored': 1.703342770228576e-07,
    'SPEND_B1_gate_storedjoint': stb1['joint']
    - (-4.60458433226168e-06),
    'SPEND_B1_gate_ownglobal': stb1['joint'] - b1t1['joint'],
    'SPEND_B1_stored': 1.0861605997805081e-05,
    'SPEND_B418_gate': OUT['b_static_cbj']['spend_gate'],
    'SPEND_B418_stored': 1.2540019050282306e-09,
    'statics': {'400': st400['joint'], 'B1': stb1['joint'],
                'B418_cbj_base': OUT['b_static_cbj']['joint']}}

# ------------------------------------------------ (c)
tw_cfg = cfg_of(conf418['twice_best']['config'])
tw_read, tw_rec = full_read(tw_cfg, conf418['twice_best'],
                            with_polish=False)
OUT['c_twice_screen1648'] = tw_read
# frame-invariant anchor at the stored argmin shell: the
# stored worst-null is at the phase's own argmin point;
# find the gate's sampled argmin on that shell and read
# the exact worst-null there and at the shell's exact
# worst-null minimum.
shell_r = conf418['twice_best']['nec_argmin_r']
shell = G.DIRS162 * shell_r
pr = G.profiles_g56(tw_cfg, shell)
T, g = G.T_at_g56(shell, pr)
That = G.eulerian_that_g56(g, T)
m = G.margins_g56(That)
i_s = int(np.argmin(m['nec']))
wns = [G.worst_null_exact(That[j])['value'] for j in range(162)]
OUT['c_twice_anchor'] = {
    'shell_r': shell_r,
    'gate_sampled_nec_at_own_argmin': float(m['nec'][i_s]),
    'stored_joint': conf418['twice_best']['joint'],
    'worst_null_at_gate_argmin': wns[i_s],
    'worst_null_shell_min': float(min(wns)),
    'stored_worst_null': conf418['twice_best'][
        'worst_null_at_nec_argmin'],
    'argmin_typeI': bool(m['typeI'][i_s])}
# R17 arm winner
r17 = [s for s in screens if s['stage'] == 'R17']
r17_best = max(r17, key=lambda s: s['joint'])
r17_read, _ = full_read(cfg_of(r17_best), r17_best,
                        with_polish=False)
OUT['c_r17_winner'] = {'screen_id': r17_best['id'],
                       'stored_joint': r17_best['joint'],
                       'read': r17_read}

with open(f'{WP}/gate56/results/g56_reads.json', 'w') as fh:
    json.dump(jd(OUT), fh, indent=1)
print('part 1 written')
for k in ('a_cbj_screen1347', 'a_cb_screen1320'):
    r = OUT[k]
    print(k, 'joint diff', r['diffs_vs_stored'].get('joint'),
          'sec diff', r['diffs_vs_stored'].get('sec_min'),
          'wn diff', r['diffs_vs_stored'].get('worst_null'),
          'polish diff', r.get('polish', {}).get('diff'),
          'peak dense', r['peak']['dense20001'])
print('b statics diffs:', OUT['b_static_cbj']['diff'],
      OUT['b_static_cb']['diff'])
print('b spends:', jd(OUT['b_spend_comparison']))
print('c twice joint diff',
      OUT['c_twice_screen1648']['diffs_vs_stored'].get('joint'))
print('c anchor:', jd(OUT['c_twice_anchor']))
print('c r17 stored', OUT['c_r17_winner']['stored_joint'],
      'gate', OUT['c_r17_winner']['read']['joint'])
