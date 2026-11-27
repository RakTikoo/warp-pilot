"""
p416_check.py — Phase 416 coordinator checker. Recomputes the
phase verdict from the stored JSONs (controls, search, verdicts)
and the parent records (408 staged Arm B state, 408 verdicts,
392 verdicts, spec files). No audits are re-run; every check
is an identity/consistency recomputation over stored numbers.
Usage: ~/workspace/warp-pilot/venv/bin/python work/p416_check.py
"""
import json, hashlib
import numpy as np

P416 = '/home/hatch/workspace/warp-pilot/phase416'
P408 = '/home/hatch/workspace/warp-pilot/phase408'
P392 = '/home/hatch/workspace/warp-pilot/phase392'
DTYPE = np.float64
fails = []
npass = [0]

def chk(name, cond, detail=''):
    if cond:
        npass[0] += 1
        print(f'PASS  {name}  {detail}')
    else:
        fails.append(name)
        print(f'FAIL  {name}  {detail}')

def vhash(y):
    return hashlib.sha256(np.asarray(y, dtype=DTYPE).tobytes()).hexdigest()

def load(p):
    return json.load(open(p))

controls = load(f'{P416}/results/p416_controls.json')
search = load(f'{P416}/results/p416_search.json')
verdicts = load(f'{P416}/results/p416_verdicts.json')
staged = load(f'{P408}/results/p408_pool_b408_de_state.json')
v408 = load(f'{P408}/results/p408_verdicts.json')
v392 = load(f'{P392}/results/p392_verdicts.json')
spec_a = load(f'{P416}/work/p416_spec_a_de.json')
spec_b = load(f'{P416}/work/p416_spec_b_de.json')
spec_b408 = load(f'{P408}/work/p408_spec_b_de.json')
vectors = load(f'{P416}/work/p416_pool_vectors.json')
state_a = load(f'{P416}/results/p416_pool_a416_de_state.json')
state_b = load(f'{P416}/results/p416_pool_b416_de_state.json')

A6_SHA = '6461827fac113c49f8f28aea04115df524446dbd44530b86f5e408e5d3c00039'
RW5_SHA = '44719b508ba733bb257281f994f90340b1ac25b33684bbe8ac9c4da5f10535c2'
CLIP_SHA = 'd228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f'

# ---------- controls ----------
c1 = controls['C-416-1']
d1 = c1['deciding_h0.0375']
w1 = d1['worst_h0.0375']
chk('C-416-1 y_his legal, worst SEC within factor 3 of Gate-42',
    c1['audit']['legal_full_common_bars'] is True and w1 > 0
    and abs(w1 / 3.404178e-7 - 1) < 2.0 and d1['worst_kind_h0.0375'] == 'sec',
    f"worst={w1} ({d1['worst_kind_h0.0375']} @ {d1['worst_r_h0.0375']})")
c2 = controls['C-416-2']
chk('C-416-2 RW-5 pass + hash verified',
    c2['pass'] is True and c2['hash_verified_before_audit'] is True
    and c2['vector_sha256_float64_tobytes'] == RW5_SHA)
c3 = controls['C-416-3']
chk('C-416-3 A-6 pass + hash verified',
    c3['pass'] is True and c3['hash_verified_before_audit'] is True
    and c3['vector_sha256_float64_tobytes'] == A6_SHA)
floor3 = c3['measured_FD_floor_h0.0375']
mult3 = c3['A-6_margin_multiple_of_FD_floor_h0.0375']
chk('C-416-3 FD floor and A-6 margin multiple recompute',
    abs(floor3 / 5.295791e-9 - 1) < 0.01 and abs(mult3 - 6.8223) < 0.01
    and abs(c3['legal_rung']['deciding_h0.0375']['worst_h0.0375']
            / floor3 - mult3) < 0.01,
    f'floor={floor3}, multiple={mult3}')
chk('controls all_pass', controls['all_pass'] is True)

# ---------- specs ----------
lo_a = np.array(spec_a['lo'], dtype=DTYPE); hi_a = np.array(spec_a['hi'], dtype=DTYPE)
chk('spec A box: idx 0 widened to +-3.375, ALL other c at +-2.25 (D-416-1: idx 13 NOT widened)',
    lo_a[0] == -3.375 and hi_a[0] == 3.375
    and bool(np.all(lo_a[1:16] == -2.25)) and bool(np.all(hi_a[1:16] == 2.25))
    and lo_a[13] == -2.25 and hi_a[13] == 2.25,
    f'idx0=[{lo_a[0]},{hi_a[0]}], idx13=[{lo_a[13]},{hi_a[13]}]')
chk('spec A box: a/q/r_m bounds as registered',
    bool(np.all(lo_a[16:27] == -8)) and bool(np.all(hi_a[16:27] == 8))
    and lo_a[27] == -12 and hi_a[27] == 12
    and lo_a[28] == 0.25 and hi_a[28] == 3.0
    and lo_a[29] == 11 and hi_a[29] == 23)
a6_y = np.array(v408['subjects']['A-6']['y'], dtype=DTYPE)
chk('spec A y_ref is A-6 (hash + elementwise)',
    vhash(spec_a['y_ref']) == A6_SHA
    and bool(np.array_equal(np.array(spec_a['y_ref'], dtype=DTYPE), a6_y)))
chk('spec A seeds: [y_his-equivalent, A-6]',
    len(spec_a['seed_ys']) == 2 and vhash(spec_a['seed_ys'][1]) == A6_SHA
    and vhash(spec_a['seed_ys'][0]) == vectors['y_his_equivalent_armA_sha256'])
lo_b = np.array(spec_b['lo'], dtype=DTYPE); hi_b = np.array(spec_b['hi'], dtype=DTYPE)
chk('spec B box == staged state box elementwise',
    bool(np.array_equal(lo_b, np.array(staged['box_lo'], dtype=DTYPE)))
    and bool(np.array_equal(hi_b, np.array(staged['box_hi'], dtype=DTYPE))))
chk('spec B: 64 seeds == staged pop elementwise',
    len(spec_b['seed_ys']) == 64
    and bool(np.array_equal(np.array(spec_b['seed_ys'], dtype=DTYPE),
                            np.array(staged['pop'], dtype=DTYPE))))
chk('spec B y_ref is the box-clipped seed of record (== b408 spec y_ref)',
    vhash(spec_b['y_ref']) == CLIP_SHA
    and bool(np.array_equal(np.array(spec_b['y_ref'], dtype=DTYPE),
                            np.array(spec_b408['y_ref'], dtype=DTYPE))))

# ---------- pool gates ----------
val = search['validations_C-416-7']
chk('C-416-7 GPU validation both arms within 1e-7, no fallback',
    val['armA_full']['max_abs_diff_overall'] <= 1e-7
    and val['armB_spot']['max_abs_diff_overall'] <= 1e-7
    and val['armA_full']['pass'] is True and val['armB_spot']['pass'] is True
    and val['cpu_fallback_used'] is False,
    f"A={val['armA_full']['max_abs_diff_overall']}, B={val['armB_spot']['max_abs_diff_overall']}")
rec = search['recalibrations_C-416-4']
def rec_ok(r):
    return (r['pass'] is True
            and abs(r['step_design_read']['gpu_union_beta_crit'] - 0.136328125) < 1e-9
            and 0.115 <= r['artefact_read']['gpu_union_beta_crit'] <= 0.127)
chk('C-416-4 recalibration both arms (step design 0.136328125, artefact in range)',
    rec_ok(rec['armA']) and rec_ok(rec['armB']),
    f"A artefact={rec['armA']['artefact_read']['gpu_union_beta_crit']}, "
    f"B artefact={rec['armB']['artefact_read']['gpu_union_beta_crit']}")
g5 = search['gate_C-416-5_armA_continuity']['y_ref_read']
chk('C-416-5 Arm A continuity: A-6 reads exactly 0.193359375, bracket tops above 0.192578125',
    g5['y_ref_beta_crit_on_de_set'] == 0.193359375 and g5['bracket'][1] > 0.192578125
    and g5['n_pts'] == 3640)
g6 = search['gate_C-416-6_armB_resumption']
chk('C-416-6 resumption cross-check: 64/64 exact, best exact, n_pts 3640',
    g6['pass'] is True and g6['n_exact_64'] == 64 and g6['max_abs_dev'] == 0.0
    and g6['best_exact_match'] is True and g6['driver_n_pts'] == 3640)
da = search['armA']['de']; db = search['armB']['de']
chk('Arm A DE: full cap, best flat at seed (best_y IS A-6)',
    da['done'] is True and da['gens'] == 137 and da['best_beta_crit'] == 0.193359375
    and da['best_y_sha256'] == A6_SHA and state_a['done'] is True)
bh = db['best_hist']
g193 = [h['gen'] for h in bh if h['best'] >= 0.193359375]
g194 = [h['gen'] for h in bh if h['best'] >= 0.194140625]
chk('Arm B resumed trajectory: 0.193359375 first at resumed gen 32, 0.194140625 at gen 98',
    db['done'] is True and db['gens_resumed'] == 118
    and g193 and g193[0] == 32 and g194 and g194[0] == 98
    and abs(db['final_pop_mean'] - 0.1936767578125) < 1e-12,
    f'first193={g193[0] if g193 else None}, first194={g194[0] if g194 else None}')

# ---------- verdicts ----------
subs = verdicts['subjects']
chk('all 13 subjects hash-recompute from stored vectors',
    all(vhash(s['y']) == s['vector_sha256_float64_tobytes'] for s in subs.values()))
lc = verdicts['legal_ceilings']
chk('legal ceilings == per-subject records',
    all(lc[k] == s['legal_ceiling'] for k, s in subs.items()))
chk('phase best is the max ceiling and equals 0.194140625',
    verdicts['phase_graded_best_beta_star'] == max(lc.values()) == 0.194140625)
chk('named best B-4 with tied B-3/B-5',
    verdicts['phase_graded_best_subject'] == 'B-4'
    and set(verdicts['phase_graded_best_tied_subjects']) == {'B-3', 'B-4', 'B-5'})
b4 = verdicts['anatomy']['phase_best_subjects']['B-4']['best_legal_rung']
b4w = b4['h0.0375']['worst']; b4fl = b4['h0.0375']['floor_proxy']
chk('B-4 deciding margin + FD-floor multiple recompute (94.51x own floor; fatter than A-6 6.8223x)',
    abs(b4w - 5.803597e-7) / 5.803597e-7 < 1e-4 and b4['h0.0375']['worst_kind'] == 'sec'
    and abs(b4w / b4fl - 94.51) < 0.05 and b4w / b4fl > mult3
    and abs(b4w / floor3 - 109.59) < 0.05,
    f'worst={b4w}, own multiple={b4w / b4fl:.2f}, vs C-416-3 floor={b4w / floor3:.2f}')
chk('B-4 bracket [0.194140625, 0.196640625], Type-I 1.0, q_max < 1',
    subs['B-4']['home_bracket'] == [0.194140625, 0.196640625]
    and b4['h0.0375']['typeI_frac_all_sig'] == 1.0
    and b4['q_reads_h0.0375']['q_max'] < 1 and b4['q_reads_h0.0375']['n_q_gt_1_sig'] == 0)
chk('A-1 (A-6 dual role) ceiling reproduces C-416-3 digits',
    lc['A-1'] == 0.193359375
    and abs(subs['A-1']['anatomy_at_ceiling']['full']['h0.0375']['worst']
            - 3.612960e-8) / 3.612960e-8 < 1e-4)
chk('B-CONTROL ceiling exactly 0.192578125 (408 B-2 reproduced)',
    lc['B-CONTROL'] == 0.192578125
    and subs['B-CONTROL']['home_bracket'] == [0.192578125, 0.195078125])
chk('Arm A home yield over seed is zero (max Arm A ceiling == A-6 ceiling)',
    max(lc[k] for k in ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6']) == 0.193359375)
diag = verdicts['anatomy']['D-416-1_diagnostic_armA_c_idx13']
c13s = [abs(np.array(subs[k]['y'], dtype=DTYPE)[13]) for k in
        ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6']]
chk('D-416-1 diagnostic: every Arm A subject idx 13 interior (none within 0.05 of bound)',
    all(x < 2.20 for x in c13s)
    and all(diag[k]['on_bound_within_0.01'] is False and diag[k]['distance_to_bound'] > 0.05
            for k in ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6'])
    and 'NO idx-13 migration' in verdicts['anatomy']['D-416-1_verdict'],
    f'idx13 values={[round(float(np.array(subs[k]["y"], dtype=DTYPE)[13]), 6) for k in ["A-1","A-2","A-3","A-4","A-5","A-6"]]}')
chk('verdict form is the RAISES form at 0.194140625',
    verdicts['verdict_form'].startswith('GRADED CLASS BEST RAISES TO beta = 0.194140625'))
chk('budget overrun disclosed on the face of the search record',
    'OVER' in search['budget']['disclosure'] and '4.5 h' in search['budget']['disclosure'])
chk('pool priority: no yield events recorded',
    search['pool_priority']['yield_events'] == 0)

print(f"\n{npass[0]} PASS, {len(fails)} FAIL")
if fails:
    print('FAILS:', fails)
    raise SystemExit(1)
