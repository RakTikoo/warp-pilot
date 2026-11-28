"""
p432_check.py — Phase 432 coordinator checker. Recomputes the phase
verdict from the stored JSONs (controls, cross-checks, search, verdicts,
dense) and the parent records (416 staged DE state, 416 verdicts, specs).
No audits are re-run; every check is an identity/consistency
recomputation over stored numbers.
Usage: ~/workspace/warp-pilot/venv/bin/python work/p432_check.py
"""
import json, hashlib
import numpy as np

P432 = '/home/hatch/workspace/warp-pilot/phase432'
P416 = '/home/hatch/workspace/warp-pilot/phase416'
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

controls = load(f'{P432}/results/p432_controls.json')
search = load(f'{P432}/results/p432_search.json')
verdicts = load(f'{P432}/results/p432_verdicts.json')
dense = load(f'{P432}/results/p432_dense.json')
staged = load(f'{P416}/results/p416_pool_b416_de_state.json')
v416 = load(f'{P416}/results/p416_verdicts.json')
spec = load(f'{P432}/work/p432_spec_b_de.json')
state = load(f'{P432}/results/b432_de_state.json')
harvest = load(f'{P432}/results/p432_pool_b432_harvest.json')
xc = load(f'{P432}/results/p432_crosscheck_cpu.json')
g0 = load(f'{P432}/results/p432_gen0check.json')
rec = load(f'{P432}/results/p432_recalib_b.json')
val = load(f'{P432}/results/p432_validate_b.json')

B4_SHA = '7a3fa7d58e8e526f5dbff8bac7c51a1a37a03b4cbd1a0ceecfc16a63793bcb42'
CLIP_SHA = 'd228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f'
C5_SHA = verdicts['subjects']['C-5']['vector_sha256_float64_tobytes']

# ---------- controls ----------
c1 = controls['C-432-1']
chk('C-432-1 y_his legal at 0.1363 in the 16-mode basis',
    c1['audit']['legal_full_common_bars'] is True and c1['pass'] is True)
c2 = controls['C-432-2']
floor2 = c2['measured_FD_floor_h0.0375']
mult2 = c2['B-4_margin_multiple_of_FD_floor_h0.0375']
chk('C-432-2 B-4 pass + hash verified before audit',
    c2['pass'] is True and c2['hash_verified_before_audit'] is True
    and c2['vector_sha256_float64_tobytes'] == B4_SHA)
chk('C-432-2 FD floor and B-4 margin multiple recompute',
    abs(c2['legal_rung']['deciding_h0.0375']['worst_h0.0375'] / floor2 - mult2) < 0.01
    and abs(mult2 - 94.5133) < 0.01, f'floor={floor2}, multiple={mult2}')
chk('C-432-2 B-4 worst SEC reproduces 416 at rel diff 0.0',
    c2['legal_rung']['deciding_h0.0375']['worst_h0.0375']
    == v416['subjects']['B-4']['rung_summaries']['0.194140625']['h0.0375']['worst'])
chk('controls all_pass', controls['all_pass'] is True)

# ---------- staging ----------
chk('staged state is 416 gen 118 (best/mean/pop shape)',
    staged['gen'] == 118 and max(staged['beta_crit']) == 0.194140625
    and abs(float(np.mean(staged['beta_crit'])) - 0.1936767578125) < 1e-15
    and len(staged['pop']) == 64)
chk('spec box == staged box; y_ref is the original clipped embedding',
    spec['lo'] == staged['box_lo'] and spec['hi'] == staged['box_hi']
    and vhash(spec['y_ref']) == CLIP_SHA and len(spec['seed_ys']) == 64)
chk('spec seeds == staged population exactly',
    all(vhash(a) == vhash(b) for a, b in zip(spec['seed_ys'], staged['pop'])))
chk('C-432-5: B-4 is staged member idx 10',
    vhash(staged['pop'][10]) == B4_SHA and xc['b4_idx'] == 10)

# ---------- cross-checks / gates ----------
chk('C-432-3 CPU staging cross-check 64/64 exact',
    xc['n_exact'] == 64 and xc['n_done'] == 64 and xc['max_abs_dev'] == 0.0
    and xc['n_brackets_equal'] == 64 and xc['n_pts'] == 3640)
chk('C-432-3 pool gen0check (gate of record) 64/64 exact, best exact',
    g0['n_exact'] == 64 and g0['max_abs_dev'] == 0.0 and g0['best_exact_match'] is True
    and g0['n_pts'] == 3640)
chk('C-432-4 recalibration pass (step class + artefact class)',
    rec['pass'] is True and rec['y_his_class_pass'] is True
    and rec['artefact_class_pass'] is True
    and rec['reads']['y_his30_step_design']['gpu_bracket'][0] <= 0.1363
    <= rec['reads']['y_his30_step_design']['gpu_bracket'][1])
chk('C-432-6 GPU-vs-CPU validation pass at the 1e-7 bar',
    val['pass'] is True and val['max_abs_diff_overall'] <= 1e-7
    and val['margins_pass'] is True and val['brackets_pass'] is True
    and all(abs(r['gpu_bc'] - r['cpu_bc']) <= 0.001
            for r in val['beta_crit_agreement']),
    f"max dev={val['max_abs_diff_overall']}")

# ---------- DE / search record ----------
de = search['arm']['de']
bc = np.array(state['beta_crit'])
chk('DE done, 134 gens, best 0.194921875',
    state['done'] is True and state['gen'] == 134
    and float(bc.max()) == 0.194921875 and de['gens_this_run'] == 134)
chk('DE first step above the staged best at gen 58 (best_hist)',
    de['first_gen_above_staged_best'] == 58
    and next(h['best'] for h in state['best_hist'] if h['gen'] == 58) == 0.194921875
    and all(h['best'] <= 0.194140625 for h in state['best_hist'] if h['gen'] < 58))
chk('DE final population anatomy recompute (mean, 43 at best, all >= B-4)',
    abs(float(bc.mean()) - de['final_pop_mean']) < 1e-15
    and int((bc >= 0.194921875 - 1e-12).sum()) == 43 == de['n_at_best']
    and int((bc >= 0.194140625 - 1e-12).sum()) == 64)
chk('DE best_y hash in search == argmax member of the copied-back state',
    de['best_y_sha256'] == vhash(state['pop'][int(np.argmax(bc))]))
chk('saturation bar (i) recorded FAILED (SATURATES excluded on its face)',
    search['saturation_bars_registered']['bar_i_screening_best_never_exceeds_0.194140625'] is False)
chk('Powell: three runs done, none improved on 0.194921875',
    all(search['arm']['powell'][f'de{k}']['done'] is True
        and search['arm']['powell'][f'de{k}']['best_beta_crit_screening'] == 0.194921875
        for k in range(3)))
chk('harvest: 68 candidates, top 6 all at 0.194921875, y_ref control = RW-5 level',
    len(harvest['all_candidates']) == 68
    and all(t['cpu_beta_crit_screening'] == 0.194921875 for t in harvest['harvest_top'])
    and harvest['y_ref_control']['cpu_beta_crit_screening'] == 0.19257812500000002
    and harvest['y_ref_control']['sha256'] == CLIP_SHA)

# ---------- verdicts ----------
ceil = verdicts['legal_ceilings']
chk('home ceilings: C-1/C-4/C-5 at the new rung; B-4 control reproduces',
    ceil['C-1'] == 0.194921875 and ceil['C-4'] == 0.194921875
    and ceil['C-5'] == 0.194921875 and ceil['B-4'] == 0.194140625
    and verdicts['anatomy']['B-4_control']['reproduces_C-432-2_and_416'] is True)
tied = verdicts['phase_graded_best_tied_subjects']
margins = {k: verdicts['subjects'][k]['rung_summaries']['0.194921875']['h0.0375']['worst']
           for k in tied}
chk('C-5 named: largest deciding margin among the tied subjects',
    verdicts['phase_graded_best_subject'] == 'C-5'
    and margins['C-5'] == max(margins.values())
    and abs(margins['C-5'] - 3.740426000178131e-07) < 1e-15,
    f'margins={margins}')
chk('C-5 home bracket [0.194921875, 0.197421875], plain wall at the failing rung',
    verdicts['subjects']['C-5']['home_bracket'] == [0.194921875, 0.197421875]
    and verdicts['subjects']['C-5']['typeI_wall_at_first_failing_rung']['typeI_only_failure'] is False)
rm = verdicts['raise_margin']
chk('raise_margin corrected to the named subject and recomputes (60.9x)',
    rm['named_subject'] == 'C-5' and 'correction_note' in rm
    and abs(rm['h0.0375_worst_margin'] / rm['fd_floor_C-432-2_at_B-4_rung']
            - rm['multiple_of_C-432-2_floor']) < 0.01
    and abs(rm['multiple_of_C-432-2_floor'] - 60.9139) < 0.01,
    f"multiple={rm['multiple_of_C-432-2_floor']}")
chk('C-2/C-6 Type-I-only walls recorded (distinct directional structure)',
    sorted(w['subject'] for w in verdicts['anatomy']['typeI_only_walls']) == ['C-2', 'C-6']
    and all('DISTINCT DIRECTIONAL STRUCTURE' in w['wall']['judgement']
            for w in verdicts['anatomy']['typeI_only_walls']))
chk('verdict form states the raise to 0.194921875',
    verdicts['phase_graded_best_beta_star'] == 0.194921875
    and 'RAISES TO beta = 0.194921875' in verdicts['verdict_form'])

# ---------- dense read ----------
d5 = dense['C-5']
chk('dense read: C-5 CONTINUUM-LEGAL, refined SEC positive, Richardson agrees',
    d5['classification'] == 'CONTINUUM-LEGAL' and d5['flag'] is None
    and d5['refined_sig']['sec']['min'] > 0
    and all(x > 0 for x in d5['richardson_sec_limits'])
    and d5['vector_sha256_float64_tobytes'] == C5_SHA
    and verdicts['dense_read_C-5']['classification'] == 'CONTINUUM-LEGAL',
    f"refined SEC={d5['refined_sig']['sec']['min']} @ {d5['refined_sig']['sec']['r']}")

print(f"\n{npass[0]} PASS, {len(fails)} FAIL")
if fails:
    print('FAILS:', fails)
