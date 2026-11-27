"""
p408_workerA.py — Phase 408 Worker A: home/VM controls C-408-1, C-408-2,
C-408-3, C-408-5 (home part: RW-5 LS embedding onto the 16-mode basis +
artefact embedding for Worker B's C-408-4), and the arm spec files
(Arm A resume DE, Arm B combined DE, Powell/harvest templates for both).
Adapted from phase392/work/p392_workerA.py (same patterns).
Verdict machinery: p386_rejudge_stage1.audit_beta (wa_auditor via
p2513_lib.audit_chunked + gate6 wa_auditor, phase50 p503_lib audit4 second
path, p2513_lib.pts_1020_control, h=0.0375/0.01875, legality via
p2513_lib.legality_1020). Programme venv, float64 everywhere.
Writes results/p408_controls.json (partial after each control).
"""
import json, os, sys, time, hashlib
import numpy as np
from scipy.interpolate import BSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase408/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase391/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase386/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase251/work')
import p386_lib as G
import p391_lib12 as L12
import p408_lib16 as L16
import p2513_lib as H
import p386_rejudge_stage1 as C

DTYPE = np.float64
WP = '/home/hatch/workspace/warp-pilot'
RES391 = f'{WP}/phase391/results'
RES386 = f'{WP}/phase386/results'
RES392 = f'{WP}/phase392/results'
WORK392 = f'{WP}/phase392/work'
RES = f'{WP}/phase408/results'
WORK = f'{WP}/phase408/work'
OUT = os.path.join(RES, 'p408_controls.json')

VERDICTS391 = json.load(open(os.path.join(RES391, 'p391_verdicts.json')))
VERDICTS392 = json.load(open(os.path.join(RES392, 'p392_verdicts.json')))
CONTROLS392 = json.load(open(os.path.join(RES392, 'p392_controls.json')))
HARV386 = json.load(open(os.path.join(RES386, 'p386_pool_stage2x_harvest.json')))
REJ386 = json.load(open(os.path.join(RES386, 'p386_rejudge_stage1.json')))
SPEC_R16_392 = json.load(open(os.path.join(WORK392, 'p392_spec_r16_de.json')))
DE_STATE_R16 = json.load(open(os.path.join(RES392, 'p392_pool_r16_de_state.json')))
POOL_VECTORS392 = json.load(open(os.path.join(WORK392, 'p392_pool_vectors.json')))

def log(m): print(f'{time.strftime("%H:%M:%S")} {m}', flush=True)
def vhash(y): return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()
def rel(a, b): return abs(float(a) - float(b)) / abs(float(b)) if float(b) != 0 else abs(float(a) - float(b))

def deciding(rec):
    a = rec['summaries']['h0.0375']['all_sig']
    wk = a['worst_kind']
    leg = rec['legality_1020']['h0.0375']
    a2 = rec['summaries']['h0.01875']['all_sig']
    return {'worst_h0.0375': a['worst'], 'worst_kind_h0.0375': wk,
            'worst_r_h0.0375': a[wk + '_r'], 'worst_pt_h0.0375': a[wk + '_pt'],
            'typeI_frac_h0.0375': a['typeI_frac'],
            'floor_multiple_worst_over_floor_h0.0375': leg.get('worst_over_floor'),
            'floor_h0.0375': leg.get('floor'),
            'shell_sampled_nec_min_h0.0375': rec['summaries']['h0.0375']['shell'].get('sampled_nec_min'),
            'audit4_worst_h0.0375': rec['second_path_signs']['h0.0375']['worst'],
            'audit4_worst_h0.01875': rec['second_path_signs']['h0.01875']['worst'],
            'q_max_h0.0375': rec['q_reads']['h0.0375']['q_max'],
            'q_max_r_h0.0375': rec['q_reads']['h0.0375']['q_max_r'],
            'q_at_worst_sampled_nec_h0.0375': rec['q_reads']['h0.0375']['q_worst'],
            'worst_h0.01875': a2['worst'], 'worst_kind_h0.01875': a2['worst_kind'],
            'worst_r_h0.01875': a2[a2['worst_kind'] + '_r'],
            'typeI_frac_h0.01875': a2['typeI_frac'],
            'legal_full_common_bars': rec['legal_full_common_bars']}

# ---------------- vectors ----------------
y_his22 = np.array(HARV386['y_his_control']['y'], dtype=DTYPE)          # 22-dim, c=0 (8-mode)
E2_1 = np.array(VERDICTS391['subjects']['E2-1']['y'], dtype=DTYPE)      # 26-dim
E2_1_HASH_STORED = VERDICTS391['subjects']['E2-1']['vector_sha256_float64_tobytes']
RW5 = np.array(VERDICTS392['subjects']['RW-5']['y'], dtype=DTYPE)       # 26-dim
RW5_HASH_STORED = VERDICTS392['subjects']['RW-5']['vector_sha256_float64_tobytes']
RW5_HASH_EXPECTED = '44719b508ba733bb257281f994f90340b1ac25b33684bbe8ac9c4da5f10535c2'
ARTEFACT22 = np.array(REJ386['y_stage1'], dtype=DTYPE)                  # 22-dim convicted Stage-1 artefact

# Arm B box (CHECKPOINT408): c idx0 +-3.375, c idx11 +-3.375, other c +-2.25;
# a in [-8,8]^11, a12 in [-12,12]; q in [0.25,3.0]; r_m in [11,23]
LO_B = [-3.375] + [-2.25] * 10 + [-3.375] + [-2.25] * 4 + [-8.0] * 11 + [-12.0] + [0.25, 11.0]
HI_B = [3.375] + [2.25] * 10 + [3.375] + [2.25] * 4 + [8.0] * 11 + [12.0] + [3.0, 23.0]
assert len(LO_B) == 30 and len(HI_B) == 30

state = {'item': 'Phase 408 Worker A: controls C-408-1, C-408-2, C-408-3, C-408-5 (home part) + arm spec JSONs',
         'frame': 'programme venv float64; wa_auditor (audit_chunked) + audit4 (audit4_chunked); pts_1020_control 1430 pts; h=0.0375/0.01875; legality_1020 + audit4 sign agreement (p386_rejudge_stage1.audit_beta)',
         'lib16_copy': 'phase408/work/p408_lib16.py is the Phase 408 copy of phase392/work/p392_lib16.py (verbatim except header note; numerics identical)'}

def save():
    json.dump(state, open(OUT, 'w'), indent=1, default=float)

def main():
    t00 = time.time()
    pts, radp = H.pts_1020_control()
    C.PTS, C.RADP = pts, radp
    log(f'pts {len(pts)}')

    # ============ C-408-1: y_his (c=0 through p408_lib16 GradedProcaccia16) at beta=0.1363 ============
    hh22 = vhash(y_his22)
    log(f'y_his22 hash {hh22}')
    assert hh22 == 'd4eb224779778f58308abbb28c4832562dcad02d40e90b2b8055ce29990eddd7', 'y_his HASH MISMATCH'
    y16_his = np.r_[np.zeros(16, dtype=DTYPE), y_his22[8:]]   # (0_16, y_his a/q/r_m), 30-dim — 392 C-392-4a pattern
    b_his16 = L16.GradedProcaccia16(y16_his)
    cr1 = b_his16.chain_reads()
    ref392 = CONTROLS392['C-392-1']['chain_reads']   # Gate-42 digits as carried by 392's C-392-1 record
    chain_cmp = {k: {'value': float(cr1[k]), 'gate42_ref_via_p392_controls_C-392-1': float(ref392[k]),
                     'rel_diff': rel(cr1[k], ref392[k])} for k in ('M', 'rho_max', 'lambda', 'k')}
    ref4a = CONTROLS392['C-392-4a']['chain_reads_c0']
    chain_cmp_4a = {k: {'value': float(cr1[k]), 'p392_controls_C-392-4a_16mode_value': float(ref4a[k]),
                        'rel_diff': rel(cr1[k], ref4a[k])} for k in ('M', 'rho_max', 'lambda', 'k')}
    log('C-408-1 AUDIT beta=0.1363 (16-mode builder, c=0)')
    rec1, _ = C.audit_beta(b_his16, 0.1363, pts, radp)
    a1 = rec1['summaries']['h0.0375']['all_sig']
    gate_worst = 3.404178e-7
    ratio = a1['worst'] / gate_worst
    chain_ok = all(v['rel_diff'] <= 1e-10 for v in chain_cmp.values())
    c1_pass = bool(rec1['legal_full_common_bars'] and (1.0 / 3.0) <= ratio <= 3.0 and chain_ok)
    state['C-408-1'] = {'control': 'C-408-1 (c=0 reproduces Gate-42)',
                        'subject': 'y_his (c=0 through p408_lib16 GradedProcaccia16: y=(0_16, y_his a/q/r_m), 30-dim)',
                        'y': [float(v) for v in y16_his],
                        'vector_sha256_float64_tobytes': vhash(y16_his),
                        'source_y_his22_sha256_float64_tobytes': hh22,
                        'source_y_his22_expected_sha256': 'd4eb224779778f58308abbb28c4832562dcad02d40e90b2b8055ce29990eddd7',
                        'hash_verified': True,
                        'factory': 'phase408/work/p408_lib16.py GradedProcaccia16 (Phase 408 copy of p392_lib16)',
                        'beta': 0.1363, 'audit': rec1, 'deciding_h0.0375': deciding(rec1),
                        'chain_reads': cr1, 'chain_reads_vs_gate42': chain_cmp,
                        'chain_reads_vs_p392_C-392-4a_16mode': chain_cmp_4a,
                        'gate42_worst_ref': gate_worst, 'worst_ratio_to_gate42': ratio,
                        'bar': 'LEGAL; h=0.0375 worst within factor 3 of +3.404178e-7 (SEC @ r=5.0); chain (M, rho_max, lambda, k) rel diffs <= 1e-10 vs Gate-42 digits (392 C-392-1 record)',
                        'pass': c1_pass}
    save()
    log(f'C-408-1 pass={c1_pass} worst={a1["worst"]:+.12e} kind={a1["worst_kind"]} r={a1[a1["worst_kind"]+"_r"]} ratio={ratio:.6f} chain_ok={chain_ok}')
    if not c1_pass:
        state['all_pass'] = False; state['machinery_failure'] = 'C-408-1'; state['elapsed_s'] = time.time() - t00; save()
        log('C-408-1 FAILED — stopping as MACHINERY FAILURE'); return

    # ============ C-408-2: E2-1 at beta=0.191796875, 12-mode machinery ============
    he = vhash(E2_1)
    log(f'E2-1 hash {he} stored {E2_1_HASH_STORED}')
    hash_ok = (he == E2_1_HASH_STORED)
    assert hash_ok, 'E2-1 HASH MISMATCH — refusing to audit'
    b_e2 = L12.GradedProcaccia12(E2_1)
    log('C-408-2 AUDIT beta=0.191796875')
    rec2, _ = C.audit_beta(b_e2, 0.191796875, pts, radp)
    stored = VERDICTS391['subjects']['E2-1']['rung_summaries']['0.191796875']['h0.0375']
    cmp2 = {'worst_SEC': {'value': rec2['summaries']['h0.0375']['all_sig']['worst'],
                          'stored_391': stored['worst'], 'rel_diff': rel(rec2['summaries']['h0.0375']['all_sig']['worst'], stored['worst'])},
            'worst_r': {'value': rec2['summaries']['h0.0375']['all_sig']['sec_r'], 'stored_391': stored['worst_r']},
            'audit4_worst': {'value': rec2['second_path_signs']['h0.0375']['worst'],
                             'stored_391': stored['audit4_worst'], 'rel_diff': rel(rec2['second_path_signs']['h0.0375']['worst'], stored['audit4_worst'])},
            'q_max': {'value': rec2['q_reads']['h0.0375']['q_max'],
                      'stored_391': stored['q_max'], 'rel_diff': rel(rec2['q_reads']['h0.0375']['q_max'], stored['q_max'])},
            'q_max_r': {'value': rec2['q_reads']['h0.0375']['q_max_r'], 'stored_391': stored['q_max_r']}}
    digits_ok = (cmp2['worst_SEC']['rel_diff'] <= 1e-9 and cmp2['worst_r']['value'] == cmp2['worst_r']['stored_391']
                 and cmp2['audit4_worst']['rel_diff'] <= 1e-9 and cmp2['q_max']['rel_diff'] <= 1e-9
                 and cmp2['q_max_r']['value'] == cmp2['q_max_r']['stored_391'])
    c2_pass = bool(hash_ok and rec2['legal_full_common_bars'] and digits_ok)
    state['C-408-2'] = {'control': 'C-408-2 (the 391 best reproduces)',
                        'subject': 'E2-1 (phase391/results/p391_verdicts.json subjects/E2-1)',
                        'vector_sha256_float64_tobytes': he,
                        'stored_full_hash': E2_1_HASH_STORED, 'hash_verified_before_audit': hash_ok,
                        'machinery': 'phase391/work/p391_lib12.py GradedProcaccia12',
                        'beta': 0.191796875, 'audit': rec2, 'deciding_h0.0375': deciding(rec2),
                        'chain_reads': b_e2.chain_reads(),
                        'reproduction_vs_391_home_record': cmp2,
                        'bar': 'LEGAL; worst SEC +7.075e-8 @ r=6.0, audit4 +5.407e-8, q_max 0.9933 @ 19.75 reproduced to stored digits',
                        'pass': c2_pass}
    save()
    log(f'C-408-2 pass={c2_pass} worst={cmp2["worst_SEC"]["value"]:+.12e} rel={cmp2["worst_SEC"]["rel_diff"]:.3e} audit4 rel={cmp2["audit4_worst"]["rel_diff"]:.3e} qmax rel={cmp2["q_max"]["rel_diff"]:.3e}')
    if not c2_pass:
        state['all_pass'] = False; state['machinery_failure'] = 'C-408-2'; state['elapsed_s'] = time.time() - t00; save()
        log('C-408-2 FAILED — stopping as MACHINERY FAILURE'); return

    # ============ C-408-3: RW-5 at beta=0.192578125 (LEGAL) and 0.195078125 (FAIL), 12-mode ============
    hrw = vhash(RW5)
    log(f'RW-5 hash {hrw} stored {RW5_HASH_STORED} expected {RW5_HASH_EXPECTED}')
    hash_rw_ok = (hrw == RW5_HASH_STORED == RW5_HASH_EXPECTED)
    assert hash_rw_ok, 'RW-5 HASH MISMATCH — refusing to audit'
    b_rw = L12.GradedProcaccia12(RW5)
    log('C-408-3 AUDIT beta=0.192578125')
    rec3a, _ = C.audit_beta(b_rw, 0.192578125, pts, radp)
    st3 = VERDICTS392['subjects']['RW-5']['rung_summaries']['0.192578125']['h0.0375']
    cmp3a = {'worst_SEC': {'value': rec3a['summaries']['h0.0375']['all_sig']['worst'],
                           'stored_392': st3['worst'], 'rel_diff': rel(rec3a['summaries']['h0.0375']['all_sig']['worst'], st3['worst'])},
             'worst_r': {'value': rec3a['summaries']['h0.0375']['all_sig']['sec_r'], 'stored_392': st3['worst_r']},
             'audit4_worst': {'value': rec3a['second_path_signs']['h0.0375']['worst'],
                              'stored_392': st3['audit4_worst'], 'rel_diff': rel(rec3a['second_path_signs']['h0.0375']['worst'], st3['audit4_worst'])},
             'q_max': {'value': rec3a['q_reads']['h0.0375']['q_max'],
                       'stored_392': st3['q_max'], 'rel_diff': rel(rec3a['q_reads']['h0.0375']['q_max'], st3['q_max'])},
             'q_max_r': {'value': rec3a['q_reads']['h0.0375']['q_max_r'], 'stored_392': st3['q_max_r']}}
    digits3a_ok = (cmp3a['worst_SEC']['rel_diff'] <= 1e-9 and cmp3a['worst_r']['value'] == cmp3a['worst_r']['stored_392']
                   and cmp3a['audit4_worst']['rel_diff'] <= 1e-9 and cmp3a['q_max']['rel_diff'] <= 1e-9
                   and cmp3a['q_max_r']['value'] == cmp3a['q_max_r']['stored_392'])
    log('C-408-3 AUDIT beta=0.195078125 (must FAIL)')
    rec3b, _ = C.audit_beta(b_rw, 0.195078125, pts, radp)
    st3b = VERDICTS392['subjects']['RW-5']['rung_summaries']['0.195078125']['h0.0375']
    a3b = rec3b['summaries']['h0.0375']['all_sig']
    cmp3b = {'worst': {'value': a3b['worst'], 'stored_392': st3b['worst'], 'rel_diff': rel(a3b['worst'], st3b['worst'])},
             'worst_kind': {'value': a3b['worst_kind'], 'stored_392': st3b['worst_kind']},
             'worst_r': {'value': a3b[a3b['worst_kind'] + '_r'], 'stored_392': st3b['worst_r']},
             'sec': {'value': a3b['sec'], 'stored_392': st3b['per_ec']['sec'], 'rel_diff': rel(a3b['sec'], st3b['per_ec']['sec'])},
             'audit4_worst': {'value': rec3b['second_path_signs']['h0.0375']['worst'],
                              'stored_392': st3b['audit4_worst'], 'rel_diff': rel(rec3b['second_path_signs']['h0.0375']['worst'], st3b['audit4_worst'])},
             'legal_full_common_bars': rec3b['legal_full_common_bars']}
    fail_repro_ok = bool((not rec3b['legal_full_common_bars']) and a3b['worst_kind'] == 'sec'
                         and a3b['sec_r'] == st3b['worst_r'] and cmp3b['sec']['rel_diff'] <= 1e-6)
    c3_pass = bool(hash_rw_ok and rec3a['legal_full_common_bars'] and digits3a_ok and fail_repro_ok)
    state['C-408-3'] = {'control': 'C-408-3 (the standing best reproduces)',
                        'subject': 'RW-5 (phase392/results/p392_verdicts.json subjects/RW-5)',
                        'vector_sha256_float64_tobytes': hrw,
                        'stored_full_hash': RW5_HASH_STORED, 'expected_full_hash': RW5_HASH_EXPECTED,
                        'hash_verified_before_audit': hash_rw_ok,
                        'machinery': 'phase391/work/p391_lib12.py GradedProcaccia12',
                        'chain_reads': b_rw.chain_reads(),
                        'legal_rung': {'beta': 0.192578125, 'audit': rec3a, 'deciding_h0.0375': deciding(rec3a),
                                       'reproduction_vs_392_home_record': cmp3a},
                        'failing_rung': {'beta': 0.195078125, 'audit': rec3b, 'deciding_h0.0375': deciding(rec3b),
                                         'reproduction_vs_392_home_record': cmp3b,
                                         'must_fail': True, 'failed_as_required': bool(not rec3b['legal_full_common_bars'])},
                        'bar': 'LEGAL at 0.192578125 (worst SEC +6.056e-7 @ 3.75; audit4 +6.050e-7; q_max 0.9934 @ 19.75) AND FAIL at 0.195078125 (SEC ~ -1.032e-5 @ 9.75)',
                        'pass': c3_pass}
    save()
    log(f'C-408-3 pass={c3_pass} legal_worst={cmp3a["worst_SEC"]["value"]:+.12e} rel={cmp3a["worst_SEC"]["rel_diff"]:.3e} fail_sec={a3b["sec"]:+.12e} @ {a3b["sec_r"]} legal_b={rec3b["legal_full_common_bars"]}')
    if not c3_pass:
        state['all_pass'] = False; state['machinery_failure'] = 'C-408-3'; state['elapsed_s'] = time.time() - t00; save()
        log('C-408-3 FAILED — stopping as MACHINERY FAILURE'); return

    # ============ C-408-5 (home part): LS embeddings onto 16-mode basis (391 e2gate pattern) ============
    R1, R2 = float(L12.R1), float(L12.R2)
    grid = np.linspace(R1, R2, 20001, dtype=DTYPE)
    def basis(knots, nb):
        B = np.array([BSpline(knots, np.eye(nb)[i], 3, extrapolate=False)(np.clip(grid, R1, R2)) for i in range(nb)])
        return np.nan_to_num(B)
    B8 = basis(G.GRADING_KNOTS, 8)
    B12 = basis(L12.GRADING_KNOTS, 12)
    B16 = basis(L16.GRADING_KNOTS, 16)
    def embed(logphi, B):
        c, *_ = np.linalg.lstsq(B.T, logphi, rcond=None)
        resid = B.T @ c - logphi
        return c, float(np.sqrt(np.mean(resid ** 2))), float(np.max(np.abs(resid)))
    # RW-5 (12-mode) -> 16-mode; a/q/r_m carried unchanged
    logphi_rw = RW5[:12] @ B12
    c16_rw, rms_rw, mx_rw = embed(logphi_rw, B16)
    emb_rw_30 = np.r_[c16_rw, RW5[12:]]
    emb_rw_hash = vhash(emb_rw_30)
    # Arm B box containment, every coordinate
    names = [f'c{j}' for j in range(16)] + [f'a{j+1}' for j in range(12)] + ['q', 'r_m']
    box_check = []
    all_inside = True
    for i in range(30):
        v = float(emb_rw_30[i]); lo = float(LO_B[i]); hi = float(HI_B[i])
        inside = bool(lo <= v <= hi)
        all_inside = all_inside and inside
        box_check.append({'index': i, 'name': names[i], 'value': v, 'lo': lo, 'hi': hi,
                          'inside': inside, 'outside_by': (0.0 if inside else (lo - v if v < lo else v - hi))})
    outside = [e for e in box_check if not e['inside']]
    # artefact (8-mode) -> 16-mode, recomputed fresh here; cross-checked vs 392 stored
    logphi_art = ARTEFACT22[:8] @ B8
    c16_art, rms_a16, mx_a16 = embed(logphi_art, B16)
    emb_art_30 = np.r_[c16_art, ARTEFACT22[8:]]
    emb_art_hash = vhash(emb_art_30)
    stored_art_emb = np.array(POOL_VECTORS392['artefact_emb16'], dtype=DTYPE)
    art_stored_hash = POOL_VECTORS392['artefact_emb16_sha256']
    art_match_stored = bool(np.array_equal(emb_art_30, stored_art_emb) and emb_art_hash == art_stored_hash
                            and art_stored_hash == CONTROLS392['C-392-4b']['artefact_to_16mode']['embedded_vector_sha256_float64_tobytes'])
    art_maxdiff = float(np.max(np.abs(emb_art_30 - stored_art_emb)))
    # y_his-equivalent for Arm B seeds (c=0 with RW-5's a/q/r_m)
    y_his_equiv_b = np.r_[np.zeros(16, dtype=DTYPE), RW5[12:]]
    state['C-408-5'] = {
        'control': 'C-408-5 (home part: RW-5 embedding control; the screening-losslessness gate on the pool instrument is Worker B scope, not run here)',
        'method': '391 e2gate LS pattern: log phi on linspace(R1,R2,20001), np.linalg.lstsq of the 16-mode BSpline basis, residual = B^T c - logphi on the same grid; a/q/r_m carried unchanged from RW-5',
        'RW-5_to_16mode': {'source': 'RW-5 log phi (12-mode c)',
                           'source_vector_sha256_float64_tobytes': hrw,
                           'q_carried': float(RW5[24]), 'r_m_carried': float(RW5[25]),
                           'c16': [float(v) for v in c16_rw],
                           'residual_rms': rms_rw, 'residual_max_abs': mx_rw,
                           'embedded_y30': [float(v) for v in emb_rw_30],
                           'embedded_vector_sha256_float64_tobytes': emb_rw_hash,
                           'armB_box_lo': LO_B, 'armB_box_hi': HI_B,
                           'armB_box_check_every_coordinate': box_check,
                           'all_coordinates_inside_armB_box': all_inside,
                           'coordinates_outside_armB_box': outside},
        'artefact_to_16mode_for_C-408-4': {
            'note': 'Recomputed fresh in this run by the same LS pattern (NOT merely copied); cross-checked against the stored 392 embedded vector.',
            'source': 'convicted Stage-1 artefact log phi (8-mode c; phase386/results/p386_rejudge_stage1.json y_stage1)',
            'source_vector_sha256_float64_tobytes': vhash(ARTEFACT22),
            'c16': [float(v) for v in c16_art],
            'residual_rms': rms_a16, 'residual_max_abs': mx_a16,
            'embedded_y30': [float(v) for v in emb_art_30],
            'embedded_vector_sha256_float64_tobytes': emb_art_hash,
            'stored_392_artefact_emb16_sha256': art_stored_hash,
            'matches_stored_p392_pool_vectors_artefact_emb16': art_match_stored,
            'max_abs_diff_vs_stored': art_maxdiff,
            'also_matches_p392_controls_C-392-4b_record': bool(emb_art_hash == CONTROLS392['C-392-4b']['artefact_to_16mode']['embedded_vector_sha256_float64_tobytes'])},
        'y_his_equivalent_armB': {'definition': 'c=0 (16 zeros) with RW-5 a/q/r_m carried',
                                  'y': [float(v) for v in y_his_equiv_b],
                                  'vector_sha256_float64_tobytes': vhash(y_his_equiv_b)},
        'pass': bool(all_inside),
        'pass_note': 'home part bar: residual (RMS, max) reported; embedded vector sha256 recorded; embedded vector must lie inside the Arm B box (every coordinate reported). Screening-losslessness (embedded seed screening beta_crit exactly 0.192578125 on the pool instrument) is Worker B / C-408-5 pool part.'}
    save()
    log(f'C-408-5 RW5->16 rms={rms_rw:.6e} max={mx_rw:.6e} hash={emb_rw_hash} all_inside={all_inside} outside={outside}')
    log(f'C-408-5 artefact->16 rms={rms_a16:.6e} max={mx_a16:.6e} hash={emb_art_hash} matches_stored={art_match_stored} maxdiff={art_maxdiff:.3e}')
    if not all_inside:
        state['all_pass'] = False; state['machinery_failure'] = 'C-408-5 (embedded RW-5 outside Arm B box)'; state['elapsed_s'] = time.time() - t00; save()
        log('C-408-5 FAILED (box containment) — stopping as MACHINERY FAILURE'); return

    # ============ ARM SPECS ============
    lo30_r16 = [float(v) for v in SPEC_R16_392['lo']]; hi30_r16 = [float(v) for v in SPEC_R16_392['hi']]
    y_ref_a = [float(v) for v in SPEC_R16_392['y_ref']]   # ORIGINAL R-16 spec's y_ref (E2-1 embedding)
    # --- Arm A (RESUME) ---
    pop64 = [[float(v) for v in row] for row in DE_STATE_R16['pop']]
    assert len(pop64) == 64 and all(len(r) == 30 for r in pop64)
    assert [float(v) for v in DE_STATE_R16['box_lo']] == lo30_r16 and [float(v) for v in DE_STATE_R16['box_hi']] == hi30_r16
    spec_a = {'tag': 'a408', 'lib': 'p392_16', 'lo': lo30_r16, 'hi': hi30_r16, 'cap_min': 120, 'pop': 64,
              'y_ref': y_ref_a,
              'seed_ys': pop64,
              'seed_names': ['staged_population_64']}
    json.dump(spec_a, open(os.path.join(WORK, 'p408_spec_a_de.json'), 'w'), indent=1)
    # --- Arm B (COMBINED) ---
    spec_b = {'tag': 'b408', 'lib': 'p392_16', 'lo': LO_B, 'hi': HI_B, 'cap_min': 120, 'pop': 64,
              'y_ref': [float(v) for v in emb_rw_30],
              'seed_ys': [[float(v) for v in y_his_equiv_b], [float(v) for v in emb_rw_30]],
              'seed_names': ['y_his_equivalent', 'RW-5_embedded_ls_16mode']}
    json.dump(spec_b, open(os.path.join(WORK, 'p408_spec_b_de.json'), 'w'), indent=1)
    # --- Powell / harvest templates (392 pattern; DE-state-dependent fields for Worker B) ---
    for tag, lo, hi, yref in (('a408', lo30_r16, hi30_r16, y_ref_a), ('b408', LO_B, HI_B, [float(v) for v in emb_rw_30])):
        for i in range(3):
            tmpl = {'tag': tag, 'name': f'de{i}', 'lib': 'p392_16',
                    'start_y': list(yref),
                    'lo': list(lo), 'hi': list(hi), 'maxfev': 1500,
                    '_template_note': 'TEMPLATE (Worker A, pre-search): start_y is a PLACEHOLDER set to this arm\'s y_ref. Worker B must replace start_y with the arm\'s DE top member de%d (distinct, in DE rank order) at runtime before running Powell; lo/hi/tag/lib/maxfev are final.' % i}
            json.dump(tmpl, open(os.path.join(WORK, f'p408_spec_{tag[0]}_powell_de{i}.json'), 'w'), indent=1)
        htmpl = {'tag': tag, 'lib': 'p392_16', 'candidates': [],
                 'y_ref': list(yref), 'top_k': 6, 'distinct_min': 0.05,
                 '_template_note': 'TEMPLATE (Worker A, pre-search): candidates is EMPTY by design. Worker B fills candidates at runtime with the harvest members (each {provenance, y, source_beta_crit_screening}: top <=6 distinct by screening beta_crit, pairwise ||dy||_inf >= 0.05 over the (c,a) block, plus the registered control member for this arm) following the p392_spec_r16_harvest.json pattern; y_ref/top_k/distinct_min are final.'}
        json.dump(htmpl, open(os.path.join(WORK, f'p408_spec_{tag[0]}_harvest.json'), 'w'), indent=1)
    state['arm_specs'] = {
        'p408_spec_a_de.json': {'tag': 'a408', 'lib': 'p392_16', 'pop': 64, 'cap_min': 120, 'dim': 30,
                                'box': 'exactly the ORIGINAL R-16 box (from p392_spec_r16_de.json lo/hi; verified identical to the staged state box_lo/box_hi)',
                                'y_ref': 'the ORIGINAL R-16 spec y_ref (E2-1 embedding, r_m=16.187589217631558) from p392_spec_r16_de.json',
                                'n_seed_ys': 64,
                                'seed_note': 'seed_ys = ALL 64 members of phase392/results/p392_pool_r16_de_state.json pop, in stored order; seed_names=["staged_population_64"] and seeds 0..63 are the staged members in order',
                                'staged_state': {'gen': DE_STATE_R16['gen'], 'best_beta_crit': DE_STATE_R16['best_beta_crit'],
                                                 'n_pts_stored': DE_STATE_R16['n_pts'], 'n_evals': DE_STATE_R16['n_evals']}},
        'p408_spec_b_de.json': {'tag': 'b408', 'lib': 'p392_16', 'pop': 64, 'cap_min': 120, 'dim': 30,
                                'box': 'Arm B box per CHECKPOINT408: c idx 0 and c idx 11 in [-3.375, 3.375]; other c in [-2.25, 2.25]; a in [-8,8]^11, a12 in [-12,12]; q in [0.25,3.0]; r_m in [11,23]',
                                'y_ref': 'RW-5 embedding (C-408-5 30-vector)',
                                'y_ref_sha256_float64_tobytes': emb_rw_hash,
                                'n_seed_ys': 2,
                                'seed_names': ['y_his_equivalent', 'RW-5_embedded_ls_16mode']},
        'powell_templates': 'p408_spec_a_powell_de0/1/2.json and p408_spec_b_powell_de0/1/2.json written following p392_spec_r16_powell_de*.json (keys tag/name/lib/start_y/lo/hi/maxfev); start_y is a y_ref PLACEHOLDER — Worker B replaces it with each arm\'s DE top member at runtime (marked in each file\'s _template_note).',
        'harvest_templates': 'p408_spec_a_harvest.json and p408_spec_b_harvest.json written following p392_spec_r16_harvest.json (keys tag/lib/candidates/y_ref/top_k/distinct_min); candidates EMPTY — Worker B fills at runtime (marked in each file\'s _template_note).'}
    state['all_pass'] = bool(c1_pass and c2_pass and c3_pass and all_inside)
    state['elapsed_s'] = time.time() - t00
    save()
    log(f'ALL DONE pass C1={c1_pass} C2={c2_pass} C3={c3_pass} C5_home={all_inside} elapsed={time.time()-t00:.1f}s')

if __name__ == '__main__':
    main()
