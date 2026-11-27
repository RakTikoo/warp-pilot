"""
p408_check.py — Phase 408 coordinator checker. Recomputes the
phase verdict from the stored JSONs (controls, amendment,
search, verdicts) and the parent records (392 staged state,
392 verdicts, spec files). No audits are re-run; every check
is an identity/consistency recomputation over stored numbers.
Usage: ~/workspace/warp-pilot/venv/bin/python work/p408_check.py
"""
import json, hashlib, sys
import numpy as np

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

controls = load(f'{P408}/results/p408_controls.json')
amend = load(f'{P408}/results/p408_amendment_A408_1.json')
search = load(f'{P408}/results/p408_search.json')
verdicts = load(f'{P408}/results/p408_verdicts.json')
staged = load(f'{P392}/results/p392_pool_r16_de_state.json')
v392 = load(f'{P392}/results/p392_verdicts.json')
spec_a = load(f'{P408}/work/p408_spec_a_de.json')
spec_b = load(f'{P408}/work/p408_spec_b_de.json')

# ---------- controls ----------
c1 = controls['C-408-1']
d1 = c1['deciding_h0.0375']
w1 = d1['worst_h0.0375']
chk('C-408-1 y_his legal, worst SEC within factor 3 of Gate-42',
    c1['audit']['legal_full_common_bars'] is True and w1 > 0
    and abs(w1 / 3.404178e-7 - 1) < 2.0 and d1['worst_kind_h0.0375'] == 'sec',
    f"worst={w1} ({d1['worst_kind_h0.0375']} @ {d1['worst_r_h0.0375']})")
c2 = controls['C-408-2']
chk('C-408-2 E2-1 pass + hash verified',
    c2['pass'] is True and c2['hash_verified_before_audit'] is True)
c3 = controls['C-408-3']
chk('C-408-3 RW-5 pass + hash verified',
    c3['pass'] is True and c3['hash_verified_before_audit'] is True
    and c3['vector_sha256_float64_tobytes'] ==
    '44719b508ba733bb257281f994f90340b1ac25b33684bbe8ac9c4da5f10535c2')
chk('controls record the C-408-5 failure as registered (amended later)',
    controls['all_pass'] is False and 'C-408-5' in controls['machinery_failure'])

# ---------- amendment A-408-1 ----------
unc = np.array(amend['unclipped_vector'], dtype=DTYPE)
clp = np.array(amend['clipped_vector'], dtype=DTYPE)
chk('amendment: unclipped hash recomputes',
    vhash(unc) == 'a0201be16477e244d82b14e421f8de5d6fff1a2917b6cfe40441a4a03dd2d374')
chk('amendment: clipped hash recomputes',
    vhash(clp) == 'd228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f')
diff = np.nonzero(unc != clp)[0]
chk('amendment: clip touches exactly c idx 13 -> -2.25',
    list(diff) == [13] and clp[13] == -2.25
    and abs(unc[13] - (-2.3199648239179234)) < 1e-15,
    f'diff idx={list(diff)}, unclipped c13={unc[13]}')
lo_b = np.array(spec_b['lo'], dtype=DTYPE); hi_b = np.array(spec_b['hi'], dtype=DTYPE)
chk('amendment: clipped vector inside Arm B box (all 30)',
    bool(np.all(clp >= lo_b) and np.all(clp <= hi_b)))
chk('amendment: unclipped vector outside Arm B box at exactly idx 13',
    list(np.nonzero((unc < lo_b) | (unc > hi_b))[0]) == [13])

# ---------- specs ----------
chk('spec A: 64 seeds == staged pop elementwise',
    len(spec_a['seed_ys']) == 64 and
    all(np.array_equal(np.array(s, dtype=DTYPE), np.array(p, dtype=DTYPE))
        for s, p in zip(spec_a['seed_ys'], staged['pop'])))
chk('spec A: box == staged state box',
    spec_a['lo'] == staged['box_lo'] and spec_a['hi'] == staged['box_hi'])
chk('spec B: y_ref == clipped vector',
    np.array_equal(np.array(spec_b['y_ref'], dtype=DTYPE), clp))
chk('spec B: widened coords are idx 0 and idx 11 only',
    [i for i in range(16) if spec_b['hi'][i] > 2.25] == [0, 11]
    and all(spec_b['hi'][i] == 3.375 for i in (0, 11)))

# ---------- search (screening record) ----------
val = search['validations_C-408-6']
chk('C-408-6: Arm A spot validation pass, diff <= 1e-7',
    val['armA_spot']['pass'] is True
    and val['armA_spot']['max_abs_diff_overall'] <= 1e-7,
    f"{val['armA_spot']['max_abs_diff_overall']:.2e}")
chk('C-408-6: Arm B full validation pass, diff <= 1e-7',
    val['armB_full']['pass'] is True
    and val['armB_full']['max_abs_diff_overall'] <= 1e-7,
    f"{val['armB_full']['max_abs_diff_overall']:.2e}")
rec = search['recalibrations_C-408-4']
chk('C-408-4: recalibration pass both arms',
    rec['armA']['pass'] is True and rec['armB']['pass'] is True)
gate = search['gate_C-408-5_pool']
chk('C-408-5 pool gate: clipped seed screens exactly 0.192578125 (<=1 ulp)',
    abs(gate['clipped_gpu_union_beta_crit'] - 0.192578125) <= 1e-16
    and abs(gate['clipped_cpu_extended_beta_crit'] - 0.192578125) <= 1e-16,
    f"gpu={gate['clipped_gpu_union_beta_crit']}")
cc = search['armA']['resumption_cross_check']
chk('Arm A resumption cross-check: n_pts 3640, 64/64 exact, best 0.191015625',
    cc['pass'] is True and cc['n_pts_printed'] == 3640
    and cc['n_exact_64'] == 64 and cc['max_abs_dev_vs_staged'] == 0.0
    and cc['best_reread'] == 0.191015625)
chk('Arm A DE: done, best screening 0.193359375',
    search['armA']['de']['done'] is True
    and search['armA']['de']['best_beta_crit'] == 0.193359375)
chk('Arm B DE: done within cap',
    search['armB']['de']['done'] is True)

# ---------- verdicts (home) ----------
subs = verdicts['subjects']
ok_hash = all(vhash(s['y']) == s['vector_sha256_float64_tobytes'] for s in subs.values())
chk('verdicts: all 13 subject hashes recompute from stored vectors', ok_hash)
ok_ceil = True
for s in subs.values():
    rs = s['rung_summaries']
    legal = [float(b) for b, r in rs.items() if r['legal_full_common_bars']]
    illegal_above = [float(b) for b, r in rs.items()
                     if not r['legal_full_common_bars'] and float(b) > s['legal_ceiling']]
    if not legal or max(legal) != s['legal_ceiling'] or not illegal_above \
            or min(illegal_above) != s['first_failing_rung']:
        ok_ceil = False
chk('verdicts: every legal_ceiling is the max legal audited rung and '
    'first_failing_rung the min illegal rung above it', ok_ceil)
ceil = {k: s['legal_ceiling'] for k, s in subs.items()}
chk('phase best == max ceiling == 0.193359375 (A-6)',
    max(ceil.values()) == 0.193359375 and ceil['A-6'] == 0.193359375
    and verdicts['phase_graded_best_beta_star'] == 0.193359375
    and verdicts['phase_graded_best_subject'] == 'A-6')
a6 = subs['A-6']
rung = a6['rung_summaries']['0.193359375']
chk('A-6 ceiling rung legal at both spacings, worst SEC > 0',
    rung['legal_full_common_bars'] is True
    and rung['h0.0375']['worst'] > 0 and rung['h0.01875']['worst'] > 0,
    f"h.0375 worst={rung['h0.0375']['worst']:.3e} ({rung['h0.0375']['worst_kind']})")
chk('A-6 failing rung 0.195859375 illegal with SEC < 0',
    a6['rung_summaries']['0.195859375']['legal_full_common_bars'] is False
    and a6['rung_summaries']['0.195859375']['h0.0375']['worst'] < 0)
chk('A-6 sole bound-sitter is c idx 0 at +2.25 (Arm A box)',
    len(a6['box_edges']) == 1 and a6['box_edges'][0]['coord'] == 'c0',
    f"{a6['box_edges']}")
b2 = subs['B-2']
chk('B-2 clipped-seed control: ceiling == RW-5 standing 0.192578125',
    b2['legal_ceiling'] == 0.192578125 and b2['first_failing_rung'] == 0.195078125
    and vhash(b2['y']) == 'd228c82e18396fe5d6a7ccc85881c558355d8d096bc8923e856ea7fc3615d69f')
chk('B-1 Powell winner: home ceiling 0.190859375 (screening raise does not survive)',
    subs['B-1']['legal_ceiling'] == 0.190859375)
chk('A-CONTROL: ceiling exactly its screening 0.191015625',
    subs['A-CONTROL']['legal_ceiling'] == 0.191015625)
rw5_392 = v392['subjects']['RW-5']
chk('RW-5 reference: 392 verdicts ceiling 0.192578125 matches C-408-3 floor',
    rw5_392['legal_ceiling'] == 0.192578125)
walls = verdicts['anatomy']['typeI_only_walls']
chk('Type-I-only walls: 3 recorded, all judged distinct from flux clause',
    len(walls) == 3 and all('NOT arrived' in w['wall']['judgement'] for w in walls)
    and all(w['wall']['per_spacing']['h0.0375']['q_max'] < 1.0 for w in walls))

print(f'\n{npass[0]} PASS, {len(fails)} FAIL')
if fails:
    print('FAILURES:', fails)
    sys.exit(1)
print('CHECKER: ALL PASS')
