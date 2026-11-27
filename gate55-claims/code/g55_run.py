"""Gate-55 driver — independent re-judgement of the Phase 420 set.

All deciding reads on gate55/work/g55_lib.py (explicit field
function, per-mode masses). Stored solutions/targets are data.
Writes gate55/results/g55_results.json.
"""
import json
import sys
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate55/work')
import g55_lib as G

WP = '/home/hatch/workspace/warp-pilot'
rng = np.random.default_rng(55)
OUT = {}


def load(p):
    with open(p) as f:
        return json.load(f)


def rel(a, b):
    return abs(a - b) / abs(b) if b != 0 else abs(a - b)


# ------------------------------------------------------------------
# Data
# ------------------------------------------------------------------
t410 = load(f'{WP}/phase410/work/p410_targets.json')
t420 = load(f'{WP}/phase420/work/p420_targets.json')
res420 = load(f'{WP}/phase420/results/p420_results.json')
lad420 = load(f'{WP}/phase420/results/p420_ladder_completed.json')
chk420 = load(f'{WP}/phase420/results/p420_check_results.json')
fitA410 = load(f'{WP}/phase410/work/p410_fitA_primary.json')
fitB410 = load(f'{WP}/phase410/work/p410_fitB_primary.json')
fitCA = load(f'{WP}/phase420/work/p420_fitCA_primary.json')
fitCB = load(f'{WP}/phase420/work/p420_fitCB_primary.json')
cs_cands = [json.loads(ln) for ln in
            open(f'{WP}/phase420/work/p420_cands_fitCS_N6.jsonl')
            if ln.strip()]
cs_warmA = next(c for c in cs_cands if c['start'] == 'warmA')

sitesA420 = t420['sitesA']
sitesB420 = t420['sitesB']
ptsA = [np.array(s['point']) for s in sitesA420]
ptsB = [np.array(s['point']) for s in sitesB420]
nhA = [p / np.linalg.norm(p) for p in ptsA]
nhB = [p / np.linalg.norm(p) for p in ptsB]
TreqA = [np.array(s['T_req']) for s in sitesA420]
TreqB = [np.array(s['T_req']) for s in sitesB420]
TcorrA_stored = [np.array(s['T_corr']) for s in sitesA420]
TcorrB_stored = [np.array(s['T_corr']) for s in sitesB420]
keysA = [s['key'] for s in sitesA420]
keysB = [s['key'] for s in sitesB420]

# identity of the two stored T_req records (gate re-check)
idmax = 0.0
for i, s in enumerate(t410['sitesA']):
    idmax = max(idmax, float(np.max(np.abs(np.array(s['That']) - TreqA[i]))))
OUT['treq_record_identity_maxdiff'] = idmax

# ------------------------------------------------------------------
# C1 — builder self-consistency + mode health
# ------------------------------------------------------------------
modes_rand = []
for k in range(6):
    pv = rng.normal(size=3)
    chi = rng.normal(size=2) + 1j * rng.normal(size=2)
    modes_rand.append((pv, chi, 1.0 if k < 3 else 0.0))
f_rand = G.CompositeField(modes_rand)
c1_max = 0.0
for _ in range(5):
    x = rng.normal(size=3)
    T1 = f_rand.stress(x)
    T2 = G.stress_pairwise_check(modes_rand, x)
    c1_max = max(c1_max, float(np.max(np.abs(T1 - T2)))
                 / float(np.linalg.norm(T1)))
OUT['C1_pairwise_rel_maxdiff'] = c1_max
OUT['C1_pass'] = bool(c1_max <= 1e-12)

health = {}
for name, pv_raw, av_raw, m in (
        ('fitA410', fitA410['pvecs'], fitA410['avecs'], 1.0),
        ('fitB410', fitB410['pvecs'], fitB410['avecs'], 1.0)):
    mx_d = mx_n = 0.0
    for pv, av in zip(np.array(pv_raw), G.avecs_from_json(av_raw)):
        _, _, nd, dr = G.mode_health(pv, m, av)
        mx_d = max(mx_d, dr); mx_n = max(mx_n, nd)
    health[name] = {'dirac_max': mx_d, 'norm_dev_max': mx_n}
for name, sol in (('fitCA', fitCA), ('fitCB', fitCB)):
    mx_d = mx_n = 0.0
    for blk, m in (('1', sol['m1']), ('2', sol['m2'])):
        for pv, av in zip(np.array(sol[f'pvecs{blk}']),
                          G.avecs_from_json(sol[f'avecs{blk}'])):
            _, _, nd, dr = G.mode_health(pv, float(m), av)
            mx_d = max(mx_d, dr); mx_n = max(mx_n, nd)
    health[name] = {'dirac_max': mx_d, 'norm_dev_max': mx_n}
OUT['mode_health'] = health
OUT['C1_health_pass'] = bool(all(
    v['dirac_max'] <= 1e-12 and v['norm_dev_max'] <= 1e-12
    for v in health.values()))


def direct_residuals(blocks, points, targets):
    f = G.field_from_blocks(blocks)
    return [float(np.linalg.norm(f.stress(p) - t))
            for p, t in zip(points, targets)]


def theta_of(sol):
    th1 = G.pack_block(np.array(sol['pvecs1']),
                       G.avecs_from_json(sol['avecs1']))
    if sol['N2'] > 0:
        th2 = G.pack_block(np.array(sol['pvecs2']),
                           G.avecs_from_json(sol['avecs2']))
        return np.concatenate([th1, th2])
    return th1


def blocks_of(sol):
    bl = [(np.array(sol['pvecs1']), G.avecs_from_json(sol['avecs1']),
           float(sol['m1']))]
    if sol['N2'] > 0:
        bl.append((np.array(sol['pvecs2']),
                   G.avecs_from_json(sol['avecs2']), float(sol['m2'])))
    return bl


# ------------------------------------------------------------------
# C2 / C3 — Phase 420's delta=0 controls on gate machinery
# ------------------------------------------------------------------
ThatA410 = [np.array(s['That']) for s in t410['sitesA']]
ThatB410 = [np.array(s['That']) for s in t410['sitesB']]
ptsB410 = [np.array(s['point']) for s in t410['sitesB']]

thA410 = G.pack_block(np.array(fitA410['pvecs']),
                      G.avecs_from_json(fitA410['avecs']))
blkA410 = [(np.array(fitA410['pvecs']),
            G.avecs_from_json(fitA410['avecs']), 1.0)]
Rs_C2 = direct_residuals(blkA410, ptsA, ThatA410)
resid_C2 = G.make_resid([(6, 1.0)], ptsA, ThatA410)
jac_C2 = G.jacobian_report(resid_C2, thA410, 3)
stored_C2 = [8.157213446731793e-15, 2.7633923118189793e-13,
             2.9659878908312287e-12]
OUT['C2'] = {'Rs': Rs_C2, 'Rs_stored': stored_C2,
             'ratios': [r / s for r, s in zip(Rs_C2, stored_C2)],
             'sigma_min': jac_C2['sigma_min'],
             'sigma_min_stored': 0.3857618146636974,
             'sigma_rel_diff': rel(jac_C2['sigma_min'],
                                   0.3857618146636974),
             'rank': jac_C2['rank_tol_1e-10_rel']}
OUT['C2_pass'] = bool(all(r <= 2 * s for r, s in zip(Rs_C2, stored_C2))
                      and max(Rs_C2) <= 1e-11
                      and OUT['C2']['sigma_rel_diff'] <= 1e-2)

thB410 = G.pack_block(np.array(fitB410['pvecs']),
                      G.avecs_from_json(fitB410['avecs']))
blkB410 = [(np.array(fitB410['pvecs']),
            G.avecs_from_json(fitB410['avecs']), 1.0)]
Rs_C3 = direct_residuals(blkB410, ptsB410, ThatB410)
resid_C3 = G.make_resid([(12, 1.0)], ptsB410, ThatB410)
jac_C3 = G.jacobian_report(resid_C3, thB410, 5)
stored_C3 = [9.110193089121277e-15, 1.6913168093005374e-14,
             2.3051650590783883e-14, 2.0952740079404155e-14,
             7.928455600124212e-15]
OUT['C3'] = {'Rs': Rs_C3, 'Rs_stored': stored_C3,
             'ratios': [r / s for r, s in zip(Rs_C3, stored_C3)],
             'sigma_min': jac_C3['sigma_min'],
             'sigma_min_stored': 0.015432479500623982,
             'sigma_rel_diff': rel(jac_C3['sigma_min'],
                                   0.015432479500623982),
             'rank': jac_C3['rank_tol_1e-10_rel']}
OUT['C3_pass'] = bool(all(r <= 2 * s for r, s in zip(Rs_C3, stored_C3))
                      and max(Rs_C3) <= 1e-11
                      and OUT['C3']['sigma_rel_diff'] <= 1e-2)

# ------------------------------------------------------------------
# Claim (a) — delta construction re-derived from stored T_req
# ------------------------------------------------------------------
claim_a = {}
TcorrA_gate = []
for i, s in enumerate(sitesA420):
    delta, info = G.build_delta(TreqA[i])
    Tc = TreqA[i] + delta
    TcorrA_gate.append(Tc)
    d_req = G.decompose(TreqA[i], nhA[i])
    d_cor = G.decompose(Tc, nhA[i])
    entry = {'key': keysA[i], **info,
             'delta_frob': float(np.linalg.norm(delta)),
             'gate_vs_stored_Tcorr_maxdiff':
                 float(np.max(np.abs(Tc - TcorrA_stored[i]))),
             'sec_trace_corr_gate':
                 d_cor['channels']['SEC_trace'] if 'channels' in d_cor
                 else None,
             'joint_min_req': d_req['joint_min_channel'],
             'joint_min_corr': d_cor['joint_min_channel']}
    if 'channels' in d_req and 'channels' in d_cor:
        diffs = [c - r for c, r in zip(
            G.joint_channel_values(d_cor['channels']),
            G.joint_channel_values(d_req['channels']))]
        entry['joint_channel_diffs_corr_minus_req'] = diffs
        entry['joint_channel_min_diff'] = float(min(diffs))
    claim_a[keysA[i]] = entry
for i, s in enumerate(sitesB420):
    delta, info = G.build_delta(TreqB[i])
    claim_a[keysB[i]] = {
        'key': keysB[i], **info,
        'delta_frob': float(np.linalg.norm(delta)),
        'gate_vs_stored_Tcorr_maxdiff':
            float(np.max(np.abs(TreqB[i] + delta - TcorrB_stored[i])))}
OUT['claim_a'] = claim_a

# ------------------------------------------------------------------
# Claim (b) — reproduction of the corrected target
# ------------------------------------------------------------------
blkCA = blocks_of(fitCA)
Rs_CA = direct_residuals(blkCA, ptsA, TcorrA_gate)
thCA = theta_of(fitCA)
resid_CA = G.make_resid([(6, 1.0), (6, 0.0)], ptsA, TcorrA_gate)
jac_CA = G.jacobian_report(resid_CA, thCA, 3)
OUT['claim_b_fitCA'] = {
    'Rs': Rs_CA, 'maxR': max(Rs_CA),
    'maxR_stored': 3.496009861987862e-10,
    'sigma_min': jac_CA['sigma_min'],
    'sigma_min_stored': 30.12132520557749,
    'sigma_rel_diff': rel(jac_CA['sigma_min'], 30.12132520557749),
    'rank': jac_CA['rank_tol_1e-10_rel'],
    'per_site_blocks': jac_CA['per_site_blocks'],
    'per_site_stored': {'0': 309.2806006954244, '1': 118.50418718151461,
                        '2': 50.93919217155723}}

blkCB = blocks_of(fitCB)
Rs_CB = direct_residuals(blkCB, ptsB, TreqB)
thCB = theta_of(fitCB)
resid_CB = G.make_resid([(6, 1.0), (6, 0.0)], ptsB, TreqB)
jac_CB = G.jacobian_report(resid_CB, thCB, 5)
OUT['claim_b_fitCB'] = {
    'Rs': Rs_CB, 'maxR': max(Rs_CB),
    'maxR_stored': 3.564601757239122e-15,
    'sigma_min': jac_CB['sigma_min'],
    'sigma_min_stored': 0.011390408308609587,
    'sigma_rel_diff': rel(jac_CB['sigma_min'], 0.011390408308609587),
    'rank': jac_CB['rank_tol_1e-10_rel']}

# ------------------------------------------------------------------
# Claim (c) — the composite total's status at the sites
# ------------------------------------------------------------------
fCA = G.field_from_blocks(blkCA)
claim_c = {}
for i, key in enumerate(keysA):
    Tsup = fCA.stress(ptsA[i])
    d = G.decompose(Tsup, nhA[i])
    chans = d['channels']
    all_ch = G.joint_channel_values(chans) + [
        chans['SEC_trace'], chans['SEC_r']] + list(chans['SEC_t'])
    claim_c[key] = {
        'T00': float(Tsup[0, 0]), 'rho_eigen': chans['rho'],
        'channels': {k: chans[k] for k in
                     ('rho', 'p_r', 'NEC_r', 'WEC', 'DEC_r', 'DEC_flux',
                      'SEC_trace', 'SEC_r')},
        'NEC_t': chans['NEC_t'], 'DEC_t': chans['DEC_t'],
        'SEC_t': chans['SEC_t'], 'p_t': chans['p_t'],
        'min_joint_channel': float(min(G.joint_channel_values(chans))),
        'min_all_channels': float(min(all_ch)),
        'SEC_trace': chans['SEC_trace'],
        'SEC_min': d['SEC_min_channel'],
        'joint_min': d['joint_min_channel'],
        'segre_type': d['segre_type']}
OUT['claim_c'] = claim_c
a2_1 = float(np.sum(np.abs(G.avecs_from_json(fitCA['avecs1'])) ** 2))
a2_2 = float(np.sum(np.abs(G.avecs_from_json(fitCA['avecs2'])) ** 2))
a2_410 = float(np.sum(np.abs(G.avecs_from_json(fitA410['avecs'])) ** 2))
OUT['claim_c_prices'] = {
    'family1': a2_1, 'family1_stored': 0.029172052178672605,
    'family2': a2_2, 'family2_stored': 2.0362442383995038e-06,
    'fitA410_uncorrected': a2_410,
    'fitA410_stored': 0.029266406597128584}
# family decomposition of the supplied density at the A sites
fam_split = {}
for i, key in enumerate(keysA):
    T1 = G.field_from_blocks([blkCA[0]]).stress(ptsA[i])
    T2 = G.field_from_blocks([blkCA[1]]).stress(ptsA[i])
    Tt = fCA.stress(ptsA[i])
    fam_split[key] = {'rho11_T00': float(T1[0, 0]),
                      'rho22_T00': float(T2[0, 0]),
                      'rho_total_T00': float(Tt[0, 0]),
                      'rho_interference_T00':
                          float(Tt[0, 0] - T1[0, 0] - T2[0, 0])}
OUT['claim_c_family_split_T00'] = fam_split

# ------------------------------------------------------------------
# Claim (d) — C-S context arm: single m=1 family vs T_corr
# ------------------------------------------------------------------
blkCS = [(np.array(cs_warmA['pvecs1']),
          G.avecs_from_json(cs_warmA['avecs1']), 1.0)]
Rs_CS = direct_residuals(blkCS, ptsA, TcorrA_gate)
thCS = G.pack_block(np.array(cs_warmA['pvecs1']),
                    G.avecs_from_json(cs_warmA['avecs1']))
resid_CS = G.make_resid([(6, 1.0)], ptsA, TcorrA_gate)
jac_CS = G.jacobian_report(resid_CS, thCS, 3)
OUT['claim_d_CS'] = {
    'Rs': Rs_CS, 'maxR': max(Rs_CS),
    'maxR_stored': 1.468495745267423e-11,
    'sigma_min_context_only': jac_CS['sigma_min'],
    'rank': jac_CS['rank_tol_1e-10_rel'],
    'stands_at_bar_1e-9': bool(max(Rs_CS) <= 1e-9)}

# ------------------------------------------------------------------
# Amendment audits
# ------------------------------------------------------------------
# A1: the ill-posed cap
stored_fitA_max = max(res420['CTRL420A']['Rs_stored'])
OUT['amendment_1'] = {
    'stored_410_fitA_max_residual': stored_fitA_max,
    'exceeds_registered_1e-12_cap': bool(stored_fitA_max > 1e-12),
    'ctrl420A_ratios': [r / s for r, s in zip(
        res420['CTRL420A']['Rs'], res420['CTRL420A']['Rs_stored'])],
    'corrected_bar_met': bool(max(res420['CTRL420A']['Rs']) <= 1e-11)}
# A2: the 0/0 singularity and the guard's footprint on stored reads
with np.errstate(all='ignore'):
    u0, E0 = G.u_spinor(np.zeros(3), 0.0, np.array([1.0, 0.0]))
zero_modes = {}
for name, sol in (('fitCA', fitCA), ('fitCB', fitCB)):
    zm = 0
    for blk in ('1', '2'):
        for pv in np.array(sol[f'pvecs{blk}']):
            if np.all(pv == 0.0):
                zm += 1
    zero_modes[name] = zm
for c in cs_cands:
    for pv in np.array(c['pvecs1']):
        if np.all(pv == 0.0):
            zero_modes['fitCS_N6'] = zero_modes.get('fitCS_N6', 0) + 1
OUT['amendment_2'] = {
    'u_spinor_zero_massless_finite': bool(np.all(np.isfinite(u0))),
    'E_at_zero': float(E0),
    'exactly_zero_momenta_in_stored_primaries': zero_modes}
# A3: the ladder records
orig = res420['fitCA_diagnostics']['perturbation_ladder']
comp = lad420['ladder']
OUT['amendment_3'] = {
    'original_eps1e-6_draw0_maxR': orig['1e-06'][0]['maxR_direct'],
    'original_eps1e-6_draw1_maxR': orig['1e-06'][1]['maxR_direct'],
    'original_all_reclose': res420['verdict']
        ['perturbation_ladder_fitCA_all_reclose'],
    'completed_rungs_maxR': {
        k: [r['maxR_direct'] for r in v] for k, v in comp.items()},
    'completed_max': max(r['maxR_direct'] for v in comp.values()
                         for r in v),
    'completed_all_reclose': lad420['all_reclose'],
    'checker_agrees_completed': chk420['verdict']
        ['ladder_completed_all_reclose']}

with open(f'{WP}/gate55/results/g55_results.json', 'w') as f:
    json.dump(OUT, f, indent=1)
print(json.dumps({k: OUT[k] for k in
                  ('C1_pairwise_rel_maxdiff', 'C1_pass', 'C1_health_pass',
                   'treq_record_identity_maxdiff')}, indent=1))
print('C2', OUT['C2'], OUT['C2_pass'])
print('C3', OUT['C3'], OUT['C3_pass'])
