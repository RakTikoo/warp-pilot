"""
p408_verdicts.py — Worker C, Phase 408: HOME RE-JUDGEMENT of the harvested
candidates (Arms A + B) + registered anatomy. Adapted from
phase392/work/p392_verdicts.py (same machinery, output structure).
Verdict machinery ONLY: p386_rejudge_stage1.audit_beta (wa_auditor via
audit_chunked + audit4 second path, p2513_lib.pts_1020_control 1,430 pts,
h=0.0375/0.01875, legality_1020 under Gate-42 common bars, exact-min rule
inside audit_beta). Programme venv, float64 everywhere.
ALL subjects are 16-mode via phase408/work/p408_lib16.py
GradedProcaccia16 (CHECKPOINT408 + Amendment A-408-1 binding).
Vectors taken from results/p408_pool_{a408,b408}_harvest.json, hashes
verified against results/p408_search.json before auditing.
Partial-writes results/p408_verdicts.json after each subject.
LADDER (392 pattern): start at the candidate's screening beta_crit; if
LEGAL climb in +0.005 rungs until the first failing rung, then the
+0.0025 refine (midpoint of the last legal / first failing pair); if
ILLEGAL descend in 0.005 steps until a legal rung is found, then the same
midpoint refine against the failing rung above it.
Subjects: A-1..A-6 (Arm A harvest, screening rank), A-CONTROL (staged
best_y, screening 0.191015625), B-1..B-6 (Arm B harvest, screening rank;
B-2 is the clipped-seed control "RW-5 embedded, box-clipped at c13",
sha d228c82e..., naturally in the top-6).
"""
import json, os, sys, time, hashlib
import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase408/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase386/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase251/work')
import p386_lib as G
import p408_lib16 as L16
import p2513_lib as H
import p386_rejudge_stage1 as C

DTYPE = np.float64
BASE = '/home/hatch/workspace/warp-pilot/phase408'
RES = os.path.join(BASE, 'results')
OUT = os.path.join(RES, 'p408_verdicts.json')
SEARCH = json.load(open(os.path.join(RES, 'p408_search.json')))
CONTROLS = json.load(open(os.path.join(RES, 'p408_controls.json')))
RW5_BETA = 0.192578125  # standing best, C-408-3 (Worker A home reproduction)

def log(m): print(f'{time.strftime("%H:%M:%S")} {m}', flush=True)
def vhash(y): return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()

# ---------------- lib16 verification (VM, before any audit) ----------------
def verify_lib16():
    y30 = np.array(CONTROLS['C-408-1']['y'], dtype=DTYPE)
    b = L16.GradedProcaccia16(y30)
    cr = b.chain_reads()
    got = {'M': cr['M'], 'rho_max': cr['rho_max'], 'lambda': cr['lambda'], 'k': cr['k']}
    ref = {k: CONTROLS['C-408-1']['chain_reads'][k] for k in got}
    out = {'builder': 'phase408/work/p408_lib16.py GradedProcaccia16',
           'subject': 'c=0 member: y=(0_16, y_his a/q/r_m), vector from p408_controls.json C-408-1',
           'chain_reads_c0': got,
           'rel_diff_vs_C-408-1': {k: abs(got[k]-ref[k])/abs(ref[k]) for k in got}}
    out['pass_C408_1_scale_1e-10'] = all(v <= 1e-10 for v in out['rel_diff_vs_C-408-1'].values())
    out['verified'] = bool(out['pass_C408_1_scale_1e-10'])
    log(f"lib16 verify: {out['rel_diff_vs_C-408-1']} verified={out['verified']}")
    return out

# ---------------- subjects ----------------
def load_subjects():
    subs = []
    hvA = json.load(open(os.path.join(RES, 'p408_pool_a408_harvest.json')))
    hvB = json.load(open(os.path.join(RES, 'p408_pool_b408_harvest.json')))
    sA = SEARCH['armA']['harvest']['top']; sB = SEARCH['armB']['harvest']['top']
    assert len(hvA['harvest_top']) == 6 and len(sA) == 6
    assert len(hvB['harvest_top']) == 6 and len(sB) == 6
    for i, (e, se) in enumerate(zip(hvA['harvest_top'], sA)):
        y = np.array(e['y'], dtype=DTYPE); h = vhash(y)
        assert h == e['sha256'] == se['sha256'], f'hash mismatch A-{i+1}'
        subs.append(dict(id=f'A-{i+1}', arm='A', entry=e, is_control=bool(se.get('is_control'))))
    # Arm A control: staged best_y from all_candidates
    ctrl = [e for e in hvA['all_candidates'] if e['sha256'] == SEARCH['armA']['harvest']['control_member']['sha256']]
    assert len(ctrl) == 1
    e = ctrl[0]; y = np.array(e['y'], dtype=DTYPE)
    assert vhash(y) == e['sha256'] == 'e28f083f7e63f5317495021bcdee797a61ba83f66f455aae9d143208634f985f'
    subs.append(dict(id='A-CONTROL', arm='A', entry=e, is_control=True,
                     control_name='staged best_y (392 R-16 staged population argmax)'))
    for i, (e, se) in enumerate(zip(hvB['harvest_top'], sB)):
        y = np.array(e['y'], dtype=DTYPE); h = vhash(y)
        assert h == e['sha256'] == se['sha256'], f'hash mismatch B-{i+1}'
        subs.append(dict(id=f'B-{i+1}', arm='B', entry=e, is_control=bool(se.get('is_control')),
                         control_name=('RW-5 embedded, box-clipped at c13' if se.get('is_control') else None)))
    return subs

def box_for(arm):
    if arm == 'B':
        c = [(-2.25, 2.25)]*16; c[0] = (-3.375, 3.375); c[11] = (-3.375, 3.375)
    else:
        c = [(-2.25, 2.25)]*16
    return {'c': c, 'a': [(-8.0, 8.0)]*11 + [(-12.0, 12.0)],
            'q': (0.25, 3.0), 'r_m': (11.0, 23.0), 'nc': 16}

def box_edges(y, arm):
    """392-style near-edge hits (within 0.01) — the bound-sitter list."""
    y = np.asarray(y, dtype=DTYPE); box = box_for(arm); nc = box['nc']; hits = []
    def chk(name, idx, lo, hi):
        v = float(y[idx])
        if abs(v-lo) < 0.01 or abs(v-hi) < 0.01:
            hits.append({'coord': name, 'y_index': int(idx), 'value': v,
                         'edge': ('lo' if abs(v-lo) <= abs(v-hi) else 'hi'),
                         'edge_value': (lo if abs(v-lo) <= abs(v-hi) else hi),
                         'distance_to_edge': min(abs(v-lo), abs(v-hi))})
    for j, (lo, hi) in enumerate(box['c']): chk(f'c{j}', j, lo, hi)
    for j, (lo, hi) in enumerate(box['a']): chk(f'a{j+1}', nc+j, lo, hi)
    chk('q', nc+12, *box['q']); chk('r_m', nc+13, *box['r_m'])
    return hits

def box_record_all(y, arm):
    """Full per-coordinate record against the arm's box."""
    y = np.asarray(y, dtype=DTYPE); box = box_for(arm); nc = box['nc']; recs = []
    names = [f'c{j}' for j in range(16)] + [f'a{j+1}' for j in range(12)] + ['q', 'r_m']
    bounds = box['c'] + box['a'] + [box['q'], box['r_m']]
    for idx, (nm, (lo, hi)) in enumerate(zip(names, bounds)):
        v = float(y[idx])
        recs.append({'coord': nm, 'y_index': int(idx), 'value': v, 'lo': lo, 'hi': hi,
                     'inside': bool(lo - 1e-12 <= v <= hi + 1e-12),
                     'distance_to_nearest_edge': min(abs(v-lo), abs(v-hi)),
                     'at_edge_within_0.01': bool(min(abs(v-lo), abs(v-hi)) < 0.01)})
    return recs

def failing_bars(rec):
    bars = []
    for hk in ('h0.0375', 'h0.01875'):
        a = rec['summaries'][hk]['all_sig']; leg = rec['legality_1020'][hk]
        if a['typeI_frac'] != 1.0: bars.append(f'{hk}:TypeI_frac={a["typeI_frac"]}')
        for k in ('nec', 'wec', 'sec', 'dec'):
            if a[k] <= 0: bars.append(f'{hk}:{k}={a[k]:+.6e}@{a[k+"_r"]}')
        if leg['worst_over_floor'] is not None and leg['worst_over_floor'] < 3.0:
            bars.append(f'{hk}:worst_over_floor={leg["worst_over_floor"]:.3f}<3')
        sn = rec['summaries'][hk]['shell'].get('sampled_nec_min')
        if sn is not None and sn <= 0: bars.append(f'{hk}:shell_sampled_nec_min={sn:+.6e}')
        sp = rec['second_path_signs'][hk]
        for k in ('nec', 'wec', 'sec', 'dec'):
            if sp[k] is not None and sp[k] <= 0: bars.append(f'{hk}:audit4_{k}={sp[k]:+.6e}')
    return bars

def is_typeI_only(rec):
    if rec['legal_full_common_bars']: return False
    bars = failing_bars(rec)
    return len(bars) > 0 and all('TypeI_frac' in b for b in bars)

def rung_summary(rec):
    a = rec['summaries']['h0.0375']['all_sig']; a2 = rec['summaries']['h0.01875']['all_sig']
    leg = rec['legality_1020']['h0.0375']
    wk = a['worst_kind']
    return {'beta': rec['beta'], 'legal_full_common_bars': rec['legal_full_common_bars'],
            'failing_bars': failing_bars(rec), 'typeI_only_failure': is_typeI_only(rec),
            'h0.0375': {'worst': a['worst'], 'worst_kind': wk, 'worst_r': a[wk+'_r'], 'worst_pt': a[wk+'_pt'],
                        'per_ec': {k: a[k] for k in ('nec', 'wec', 'sec', 'dec')},
                        'per_ec_r': {k: a[k+'_r'] for k in ('nec', 'wec', 'sec', 'dec')},
                        'typeI_frac': a['typeI_frac'], 'floor_multiple_worst_over_floor': leg['worst_over_floor'],
                        'floor': leg['floor'], 'shell_sampled_nec_min': rec['summaries']['h0.0375']['shell'].get('sampled_nec_min'),
                        'audit4_worst': rec['second_path_signs']['h0.0375']['worst'],
                        'q_max': rec['q_reads']['h0.0375']['q_max'], 'q_max_r': rec['q_reads']['h0.0375']['q_max_r'],
                        'q_max_typeI': rec['q_reads']['h0.0375']['q_max_typeI'],
                        'n_q_gt_1_sig': rec['q_reads']['h0.0375']['n_q_gt_1_sig'],
                        'n_nonTypeI_sig': rec['q_reads']['h0.0375']['n_nonTypeI_sig'],
                        'q_at_worst_sampled_nec': rec['q_reads']['h0.0375']['q_worst'],
                        'q_at_worst_sampled_nec_r': rec['q_reads']['h0.0375']['q_worst_r']},
            'h0.01875': {'worst': a2['worst'], 'worst_kind': a2['worst_kind'],
                         'worst_r': a2[a2['worst_kind']+'_r'], 'typeI_frac': a2['typeI_frac'],
                         'per_ec': {k: a2[k] for k in ('nec', 'wec', 'sec', 'dec')},
                         'floor_multiple_worst_over_floor': rec['legality_1020']['h0.01875']['worst_over_floor'],
                         'shell_sampled_nec_min': rec['summaries']['h0.01875']['shell'].get('sampled_nec_min'),
                         'audit4_worst': rec['second_path_signs']['h0.01875']['worst'],
                         'q_max': rec['q_reads']['h0.01875']['q_max'],
                         'n_q_gt_1_sig': rec['q_reads']['h0.01875']['n_q_gt_1_sig'],
                         'n_nonTypeI_sig': rec['q_reads']['h0.01875']['n_nonTypeI_sig']},
            'exact_min_triggered': bool(rec.get('exact_min')),
            'exact_min': rec.get('exact_min')}

def q_array(m):
    That = m['That']
    T00 = That[:, 0, 0]; T0i = That[:, 0, 1:]; Tij = That[:, 1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij, H.DIRS162, H.DIRS162)
    vals = T00[:, None] + 2.0 * (T0i @ H.DIRS162.T) + quad
    jmin = np.argmin(vals, axis=1)
    nmin = H.DIRS162[jmin]
    T0n = np.einsum('ij,ij->i', T0i, nmin)
    Tnn = np.einsum('ij,ijk,ik->i', nmin, Tij, nmin)
    denom = T00 + Tnn
    return np.where(denom > 0, 2.0 * np.abs(T0n) / np.maximum(denom, 1e-300), np.inf)

def typeI_wall_analysis(rec, raw, builder, pts, radp):
    out = {'beta': rec['beta'], 'typeI_only_failure': is_typeI_only(rec),
           'failing_bars': failing_bars(rec), 'per_spacing': {}}
    for hk in ('h0.0375', 'h0.01875'):
        m = raw[hk]
        summ = rec['summaries'][hk]
        sig, thr, _ = H.P633.sig_mask(m, float(builder.R1))
        q = q_array(m)
        idxs = np.where(sig)[0]
        non = [i for i in idxs if not m['typeI'][i]]
        jq = idxs[int(np.argmax(q[sig]))]
        entry = {'n_sig': int(sig.sum()), 'n_nonTypeI_sig': int(len(non)),
                 'typeI_frac': summ['all_sig']['typeI_frac'],
                 'q_max': float(q[jq]), 'q_max_r': float(radp[jq]),
                 'q_max_typeI': bool(m['typeI'][jq]),
                 'q_max_region': C.region_of(float(radp[jq]), builder),
                 'n_q_gt_1_sig': int(np.sum(q[sig] > 1.0)),
                 'all_ec_positive': bool(all(summ['all_sig'][k] > 0 for k in ('nec', 'wec', 'sec', 'dec'))),
                 'worst_margin': summ['all_sig']['worst'], 'worst_kind': summ['all_sig']['worst_kind'],
                 'nonTypeI_points': []}
        for i in non:
            entry['nonTypeI_points'].append({
                'pt': [float(x) for x in pts[i]], 'r': float(radp[i]),
                'region': C.region_of(float(radp[i]), builder),
                'q_at_point': float(q[i]), 'sampled_nec_at_point': float(m['sampled_nec'][i])})
        if non:
            qs = [float(q[i]) for i in non]
            entry['q_at_nonTypeI_points_max'] = max(qs)
            entry['q_at_nonTypeI_points_min'] = min(qs)
            entry['nonTypeI_radii'] = sorted(set(float(radp[i]) for i in non))
        out['per_spacing'][hk] = entry
    e = out['per_spacing']['h0.0375']
    if not out['typeI_only_failure']:
        out['judgement'] = 'NOT a Type-I-only wall: other bars fail at this rung (see failing_bars).'
    elif e['n_nonTypeI_sig'] > 0 and e.get('q_at_nonTypeI_points_max', 0) >= 1.0:
        out['judgement'] = ('FLUX CLAUSE ARRIVING: q >= 1 at the Type-I-failing points themselves '
                            f"(max q at a non-Type-I point = {e['q_at_nonTypeI_points_max']:.4f}).")
    elif e['q_max'] >= 1.0:
        out['judgement'] = ('FLUX CLAUSE ARRIVING (near): q_max >= 1 among significant points '
                            f"(q_max = {e['q_max']:.4f} @ r = {e['q_max_r']}), though the non-Type-I "
                            f"points themselves carry q up to {e.get('q_at_nonTypeI_points_max')}.")
    else:
        out['judgement'] = ('DISTINCT DIRECTIONAL STRUCTURE: Type-I fails while q_max < 1 everywhere '
                            f"(q_max = {e['q_max']:.4f} @ r = {e['q_max_r']}; max q at the non-Type-I "
                            f"points = {e.get('q_at_nonTypeI_points_max')}) — the flux clause has NOT arrived.")
    return out

def bind_block(a_):
    o = {}
    for hk in ('h0.0375', 'h0.01875'):
        o[hk] = {'binding_ec': a_[hk]['binding_ec'], 'binding_value': a_[hk]['binding_value'],
                 'binding_r': a_[hk]['binding_r'], 'binding_region': a_[hk]['binding_region'],
                 'per_ec': a_[hk]['per_ec'],
                 'typeI_frac': a_[hk]['typeI_frac_all_sig'], 'worst': a_[hk]['worst'],
                 'floor_proxy': a_[hk]['floor_proxy'], 'shell_sampled_nec_min': a_[hk]['shell_sampled_nec_min'],
                 'regions_worst': {reg: {'worst': a_[hk]['regions'][reg].get('worst'),
                                         'worst_kind': a_[hk]['regions'][reg].get('worst_kind'),
                                         'typeI_frac': a_[hk]['regions'][reg].get('typeI_frac'),
                                         'sampled_nec_min': a_[hk]['regions'][reg].get('sampled_nec_min')}
                                   for reg in ('shell', 'nominal_core')}}
    o['q_reads_h0.0375'] = a_['q_reads_h0.0375']
    return o

def run_subject(subj, pts, radp, state, keep_raws):
    e = subj['entry']; y = np.array(e['y'], dtype=DTYPE)
    h = vhash(y)
    crit = round(float(e['cpu_beta_crit_screening']), 10)
    log(f"=== {subj['id']} hash={h} screening={crit} bracket={e['cpu_record']['bracket']} control={subj['is_control']} ===")
    builder = L16.GradedProcaccia16(y)
    log(f"{subj['id']} chain: M={builder.M} rho_max={builder.rho_max} lam={float(builder.lam)} k={float(builder.k)} q={float(builder.q)} r_m={float(builder.r_m)}")
    audits = {}; raw_by_beta = {}; order = []
    def do(beta):
        beta = round(float(beta), 10)
        if beta in raw_by_beta: return audits[str(beta)]['legal_full_common_bars']
        log(f"{subj['id']} AUDIT beta={beta}")
        t0 = time.time()
        rec, raw = C.audit_beta(builder, beta, pts, radp)
        audits[str(beta)] = rec; raw_by_beta[beta] = raw; order.append(beta)
        log(f" -> {subj['id']} beta={beta} legal_full={rec['legal_full_common_bars']} bars={failing_bars(rec)} ({time.time()-t0:.0f}s)")
        return rec['legal_full_common_bars']
    if do(crit):
        ceiling = crit; failing = None; b = round(crit + 0.005, 10)
        while b <= 0.26:
            if do(b): ceiling = b; b = round(b + 0.005, 10)
            else: failing = b; break
        if failing is not None:
            mid = round((ceiling + failing) / 2.0, 10)
            if mid not in raw_by_beta:
                if do(mid): ceiling = mid
                else: failing = mid
    else:
        failing = crit; ceiling = None; b = round(crit - 0.005, 10)
        while b >= 0.10:
            if do(b): ceiling = b; break
            failing = b; b = round(b - 0.005, 10)
        if ceiling is not None:
            above = sorted(x for x in raw_by_beta if x > ceiling and not audits[str(x)]['legal_full_common_bars'])
            failing = min(above) if above else None
            if failing is not None:
                mid = round((ceiling + failing) / 2.0, 10)
                if mid not in raw_by_beta:
                    if do(mid): ceiling = mid
                    else: failing = mid
    out = dict(id=subj['id'], arm=subj['arm'], n_modes=16,
               provenance=e['provenance'], y=[float(v) for v in y],
               vector_sha256_float64_tobytes=h,
               hash_verified_against_search_record=True,
               hash_verified_against_pool_harvest_file=True,
               is_control=subj['is_control'], control_name=subj.get('control_name'),
               screening_beta_crit=crit, screening_bracket=[float(v) for v in e['cpu_record']['bracket']],
               source_beta_crit_screening=e.get('source_beta_crit_screening'),
               chain_reads=builder.chain_reads(),
               box_edges=box_edges(y, subj['arm']),
               box_record_all=box_record_all(y, subj['arm']),
               box_definition={'c_bounds': box_for(subj['arm'])['c'],
                               'a_bounds': box_for(subj['arm'])['a'],
                               'q': box_for(subj['arm'])['q'],
                               'r_m': box_for(subj['arm'])['r_m']},
               ladder_audited=order, audits=audits,
               rung_summaries={str(b): rung_summary(audits[str(b)]) for b in order},
               legal_ceiling=ceiling, first_failing_rung=failing,
               home_bracket=([ceiling, failing] if (ceiling is not None and failing is not None) else None))
    if failing is not None:
        out['typeI_wall_at_first_failing_rung'] = typeI_wall_analysis(
            audits[str(failing)], raw_by_beta[failing], builder, pts, radp)
    # per-subject anatomy at its legal ceiling (registered reads)
    if ceiling is not None:
        an = C.anatomy_for(ceiling, audits, raw_by_beta, builder)
        out['anatomy_at_ceiling'] = {'beta': ceiling, 'binding': bind_block(an), 'full': an}
        ceil_rec = audits[str(ceiling)]
        out['anatomy_at_ceiling']['flux_reads'] = {
            'q_at_worst_sampled_nec_point_h0.0375': ceil_rec['q_reads']['h0.0375']['q_worst'],
            'q_at_worst_sampled_nec_r': ceil_rec['q_reads']['h0.0375']['q_worst_r'],
            'q_max_h0.0375': ceil_rec['q_reads']['h0.0375']['q_max'],
            'q_max_r_h0.0375': ceil_rec['q_reads']['h0.0375']['q_max_r'],
            'typeI_frac_h0.0375': ceil_rec['summaries']['h0.0375']['all_sig']['typeI_frac']}
    state['subjects'][subj['id']] = out
    state['legal_ceilings'] = {k: v['legal_ceiling'] for k, v in state['subjects'].items()}
    json.dump(state, open(OUT, 'w'), indent=1, default=float)
    keep_raws[subj['id']] = (builder, raw_by_beta, audits)
    log(f"{subj['id']} DONE ceiling={ceiling} first_failing={failing}")
    return out, builder

def main():
    t00 = time.time()
    lib16_ver = verify_lib16()
    if not lib16_ver['verified']:
        raise SystemExit('lib16 NOT verified on VM')
    pts, radp = H.pts_1020_control()
    C.PTS, C.RADP = pts, radp
    log(f'pts {len(pts)}')
    subjects = load_subjects()
    log(f'subjects: {[s["id"] for s in subjects]} (all hashes verified vs p408_search.json + harvest files)')
    state = {'item': 'Phase 408 Worker C: HOME RE-JUDGEMENT of all harvested candidates (Arms A + B + controls) + registered anatomy (verdict audits; screening numbers provisional only)',
             'frame': 'programme venv float64; wa_auditor (audit_chunked) + audit4 second path; pts_1020_control 1430 pts; h=0.0375/0.01875; legality_1020 Gate-42 common bars + audit4 sign agreement; exact-min rule applied by audit_beta triggers',
             'ladder_rule': 'start at screening beta_crit; if legal climb +0.005 rungs then +0.0025 midpoint refine; if illegal descend 0.005 steps then midpoint refine',
             'lib16_verification': lib16_ver, 'subjects': {}, 'legal_ceilings': {}}
    json.dump(state, open(OUT, 'w'), indent=1, default=float)
    results = {}; builders = {}; keep_raws = {}
    for subj in subjects:
        res, builder = run_subject(subj, pts, radp, state, keep_raws)
        results[subj['id']] = res; builders[subj['id']] = builder
    # ---- phase graded best (incl. RW-5 standing floor) ----
    best_id = None; best_beta = None; best_margin = None
    for k, v in results.items():
        c = v['legal_ceiling']
        if c is None: continue
        m = v['rung_summaries'][str(c)]['h0.0375']['worst']
        if best_beta is None or c > best_beta or (c == best_beta and m > best_margin):
            best_beta, best_id, best_margin = c, k, m
    log(f'phase best among subjects: {best_id} {best_beta}')
    tied = [k for k, v in results.items() if v['legal_ceiling'] == best_beta]
    # ---- anatomy ----
    anatomy = {'per_arm_yield': {}, 'typeI_only_walls': []}
    for arm in ('A', 'B'):
        arm_subs = {k: v for k, v in results.items() if v['arm'] == arm}
        anatomy['per_arm_yield'][arm] = {
            'screening_levels': {k: v['screening_beta_crit'] for k, v in arm_subs.items()},
            'home_ceilings': {k: v['legal_ceiling'] for k, v in arm_subs.items()},
            'home_brackets': {k: v['home_bracket'] for k, v in arm_subs.items()},
            'arm_home_best': max((v['legal_ceiling'] for v in arm_subs.values() if v['legal_ceiling'] is not None), default=None),
            'arm_home_best_subjects': [k for k, v in arm_subs.items() if v['legal_ceiling'] == max((x['legal_ceiling'] for x in arm_subs.values() if x['legal_ceiling'] is not None), default=None)]}
    for k, v in results.items():
        w = v.get('typeI_wall_at_first_failing_rung')
        if w and w['typeI_only_failure']:
            anatomy['typeI_only_walls'].append({'subject': k, 'arm': v['arm'], 'ceiling': v['legal_ceiling'],
                                                'failing_rung': v['first_failing_rung'], 'wall': w})
    # step builder for mass redistribution: c=0 16-mode member (C-408-1 vector)
    y_his16 = np.array(CONTROLS['C-408-1']['y'], dtype=DTYPE)
    assert vhash(y_his16) == CONTROLS['C-408-1']['vector_sha256_float64_tobytes']
    b_step = L16.GradedProcaccia16(y_his16)
    def mass_phi(builder):
        rf = np.arange(0.0, 30.0001, 0.001, dtype=DTYPE)
        rho_g = builder.rho_of(rf); rho_s = b_step.rho_of(rf)
        bins = []
        for lo in range(0, 30):
            hi = lo + 1
            seg = (rf >= lo) & (rf <= hi)
            mg = float(np.trapezoid(4*np.pi*rf[seg]**2*rho_g[seg], rf[seg]))
            ms = float(np.trapezoid(4*np.pi*rf[seg]**2*rho_s[seg], rf[seg]))
            bins.append({'bin_r_lo': lo, 'bin_r_hi': hi, 'mass_graded': mg, 'mass_step': ms,
                         'delta_mass': mg-ms, 'delta_frac_of_Mtarget': (mg-ms)/G.M_TARGET,
                         'mass_graded_frac': mg/G.M_TARGET, 'mass_step_frac': ms/G.M_TARGET})
        from scipy.interpolate import BSpline
        cr = builder.chain_reads()
        knots = np.array(cr['grading']['grading_knots'], dtype=DTYPE)
        cvec = np.array(cr['grading']['c'], dtype=DTYPE); nb = len(cvec)
        rr = np.linspace(float(G.R1), float(G.R2), 20001, dtype=DTYPE)
        Bv = np.array([BSpline(knots, np.eye(nb)[i], 3, extrapolate=False)(rr) for i in range(nb)])
        phi = np.exp(cvec @ np.nan_to_num(Bv))
        imin, imax = int(np.argmin(phi)), int(np.argmax(phi))
        mass = {'method': 'rho_of on fine grid dr=0.001, 4pi r^2 rho trapezoid per 1-m bin; fractions of M_target=6.11288573784887775; step = c=0 member in the 16-mode basis (C-408-1 vector, phi==1)',
                'total_mass_graded_finegrid': float(sum(x['mass_graded'] for x in bins)),
                'total_mass_step_finegrid': float(sum(x['mass_step'] for x in bins)),
                'M_target': G.M_TARGET, 'bins': bins}
        phip = {'c': [float(v) for v in cvec], 'n_modes': nb,
                'phi_min_plateau': float(phi[imin]), 'phi_min_r': float(rr[imin]),
                'phi_max_plateau': float(phi[imax]), 'phi_max_r': float(rr[imax]),
                'phi_at_R1': float(phi[0]), 'phi_at_R2': float(phi[-1]),
                'chain_reads_phi_min': cr['grading']['phi_min_plateau'],
                'chain_reads_phi_max': cr['grading']['phi_max_plateau'],
                'rho0_graded': float(builder.rho0), 'rho_max_graded': float(builder.rho_max),
                'rho0_step': float(b_step.rho0), 'rho_max_step': float(b_step.rho_max)}
        return mass, phip
    # phase-best anatomy for every subject tied at the top ceiling
    anatomy['phase_best_subjects'] = {}
    for bid in tied:
        b_anat = builders[bid]; res_anat = results[bid]
        builder_b, raw_b, audits_b = keep_raws[bid]
        an = {'subject': bid, 'arm': res_anat['arm'], 'n_modes': 16,
              'provenance': res_anat['provenance'],
              'subject_vector_sha256_float64_tobytes': res_anat['vector_sha256_float64_tobytes'],
              'legal_ceiling': res_anat['legal_ceiling'], 'first_failing_rung': res_anat['first_failing_rung'],
              'home_bracket': res_anat['home_bracket']}
        an['best_legal_rung'] = C.anatomy_for(res_anat['legal_ceiling'], audits_b, raw_b, b_anat)
        if res_anat['first_failing_rung'] is not None:
            an['first_failing_rung_anatomy'] = C.anatomy_for(res_anat['first_failing_rung'], audits_b, raw_b, b_anat)
        an['binding_ceiling'] = bind_block(an['best_legal_rung'])
        if 'first_failing_rung_anatomy' in an:
            an['binding_first_failing'] = bind_block(an['first_failing_rung_anatomy'])
        an['ceiling_setter_is_inner_ramp_SEC'] = bool(
            an['binding_ceiling']['h0.0375']['binding_ec'] == 'sec'
            and 'inner_ramp' in str(an['binding_ceiling']['h0.0375']['binding_region']))
        ceil_rec = audits_b[str(res_anat['legal_ceiling'])]
        an['flux_wall_at_ceiling'] = {
            'q_at_worst_sampled_nec_point_h0.0375': ceil_rec['q_reads']['h0.0375']['q_worst'],
            'q_at_worst_sampled_nec_r': ceil_rec['q_reads']['h0.0375']['q_worst_r'],
            'q_max_h0.0375': ceil_rec['q_reads']['h0.0375']['q_max'],
            'q_max_r_h0.0375': ceil_rec['q_reads']['h0.0375']['q_max_r'],
            'RW-5_reference_from_C-408-3': {'beta': RW5_BETA, 'worst_SEC': 6.055585252705956e-07,
                                            'worst_SEC_r': 3.7499999999999996,
                                            'audit4_worst': 6.050011956571471e-07,
                                            'q_max': 0.9933621063959674, 'q_max_r': 19.749999999999996,
                                            'q_at_worst_sampled_nec': 0.9213977022140747}}
        mass, phip = mass_phi(b_anat)
        an['mass_redistribution_vs_step'] = mass
        an['phi_grading'] = phip
        an['box_edges_on_arm_box'] = res_anat['box_edges']
        an['box_record_all'] = res_anat['box_record_all']
        an['box_definition'] = res_anat['box_definition']
        anatomy['phase_best_subjects'][bid] = an
    # Arm B winner widened-coordinate use (registered read)
    b_best_ids = anatomy['per_arm_yield']['B']['arm_home_best_subjects']
    anatomy['B_winner_widened_coords'] = {}
    for bid in b_best_ids:
        v = results[bid]
        anatomy['B_winner_widened_coords'][bid] = {
            'subject': bid, 'home_ceiling': v['legal_ceiling'],
            'c_idx0': float(v['y'][0]), 'c_idx11': float(v['y'][11]),
            'c_idx13': float(v['y'][13]), 'c13_clip_bound': -2.25,
            'widened_box_idx0_idx11': [-3.375, 3.375], 'old_box': [-2.25, 2.25],
            'box_edges': v['box_edges']}
    # Powell winner B-1 widened use regardless of home rank
    v = results['B-1']
    anatomy['B-1_Powell_winner_widened_coords'] = {
        'subject': 'B-1', 'home_ceiling': v['legal_ceiling'],
        'c_idx0': float(v['y'][0]), 'c_idx11': float(v['y'][11]),
        'c_idx13': float(v['y'][13]), 'c13_clip_bound': -2.25,
        'widened_box_idx0_idx11': [-3.375, 3.375], 'old_box': [-2.25, 2.25],
        'seed_values_for_comparison': {'c_idx0_seed': 2.4881984560738917,
                                       'c_idx11_seed': -2.1134365124109813,
                                       'c_idx13_seed_clipped': -2.25},
        'box_edges': v['box_edges']}
    # clipped-seed control anatomy note
    anatomy['clipped_seed_control'] = {
        'subject': 'B-2', 'name': 'RW-5 embedded, box-clipped at c13',
        'sha256': results['B-2']['vector_sha256_float64_tobytes'],
        'screening_beta_crit': results['B-2']['screening_beta_crit'],
        'home_ceiling': results['B-2']['legal_ceiling'],
        'home_bracket': results['B-2']['home_bracket'],
        'RW-5_standing_beta_for_comparison': RW5_BETA}
    anatomy['A_staged_control'] = {
        'subject': 'A-CONTROL', 'name': 'staged best_y (392 R-16 staged population argmax)',
        'sha256': results['A-CONTROL']['vector_sha256_float64_tobytes'],
        'screening_beta_crit': results['A-CONTROL']['screening_beta_crit'],
        'home_ceiling': results['A-CONTROL']['legal_ceiling'],
        'home_bracket': results['A-CONTROL']['home_bracket']}
    state['anatomy'] = anatomy
    # phase best including the standing RW-5 floor
    phase_beta = best_beta; phase_subject = best_id
    if phase_beta is None or phase_beta < RW5_BETA:
        phase_beta, phase_subject = RW5_BETA, 'RW-5 (standing, control C-408-3)'
    elif phase_beta == RW5_BETA:
        phase_subject = f'{", ".join(tied)} (tie standing RW-5 at the same beta)'
    state['phase_graded_best_beta_star'] = phase_beta
    state['phase_graded_best_subject'] = phase_subject
    state['phase_graded_best_tied_subjects'] = tied
    state['best_among_subjects'] = {'subjects': tied, 'beta': best_beta,
                                    'worst_margin_h0.0375_at_ceiling': best_margin}
    state['RW-5_standing_reference'] = {'beta': RW5_BETA, 'worst_SEC': 6.055585252705956e-07,
                                        'worst_SEC_r': 3.7499999999999996,
                                        'audit4_worst': 6.050011956571471e-07,
                                        'q_max': 0.9933621063959674, 'q_max_r': 19.749999999999996,
                                        'source': 'p408_controls.json C-408-3 (home reproduction, rel diff 0.0 vs 392)'}
    if phase_beta is not None and phase_beta > RW5_BETA:
        state['verdict_form'] = (f'GRADED CLASS BEST RAISES TO beta = {phase_beta} '
                                 f'(subjects {", ".join(tied)}; see anatomy.phase_best_subjects for deciding margins and failure brackets)')
    else:
        state['verdict_form'] = '0.192578125 STANDS'
    state['elapsed_s'] = time.time() - t00
    json.dump(state, open(OUT, 'w'), indent=1, default=float)
    log(f'DONE elapsed={time.time()-t00:.1f}s ceilings={state["legal_ceilings"]} phase_best={phase_beta} {phase_subject}')

if __name__ == '__main__':
    main()
