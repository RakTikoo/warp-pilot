"""Phase 408 Worker A2: Amendment A-408-1 clipped seed + arm specs.
Reads only programme records; writes amendment record, DE specs for
Arms A/B, and Powell/harvest spec templates (DE-state fields as
placeholders for Worker B). float64 everywhere."""
import json, hashlib, os
import numpy as np

BASE = os.path.expanduser('~/workspace/warp-pilot')
P408 = os.path.join(BASE, 'phase408')
P392 = os.path.join(BASE, 'phase392')
WORK = os.path.join(P408, 'work')
RES = os.path.join(P408, 'results')

def sha(y):
    return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()

def dump(obj, path):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=1)
    print('wrote', path)

controls = json.load(open(os.path.join(RES, 'p408_controls.json')))
c5 = controls['C-408-5']['RW-5_to_16mode']
unclipped = [float(v) for v in c5['embedded_y30']]
EXPECTED_UNCLIPPED_SHA = 'a0201be16477e244d82b14e421f8de5d6fff1a2917b6cfe40441a4a03dd2d374'

# ---------- Task 1: clipped seed ----------
unclipped_sha = sha(unclipped)
assert unclipped_sha == EXPECTED_UNCLIPPED_SHA, unclipped_sha
assert unclipped[13] == -2.3199648239179234

clipped = list(unclipped)
clipped[13] = -2.25
clipped_sha = sha(clipped)
diff_idx = [i for i in range(30) if clipped[i] != unclipped[i]]
assert diff_idx == [13], diff_idx
excess = abs(unclipped[13]) - 2.25
assert excess == 0.06996482391792336, excess

# Arm B box (CHECKPOINT408 as amended / controls armB_box_lo/hi)
LO_B = [float(v) for v in c5['armB_box_lo']] if 'armB_box_lo' in c5 else None
# controls stores box under C-408-5.RW-5_to_16mode? it is there per Worker A record
if LO_B is None:
    LO_B = [float(v) for v in controls['C-408-5']['RW-5_to_16mode']['armB_box_lo']]
HI_B = [float(v) for v in controls['C-408-5']['RW-5_to_16mode']['armB_box_hi']]
# independent reconstruction per task text, cross-checked against stored box
LO_B_check = ([-3.375] + [-2.25]*10 + [-3.375] + [-2.25]*4 +
              [-8.0]*11 + [-12.0] + [0.25] + [11.0])
HI_B_check = ([3.375] + [2.25]*10 + [3.375] + [2.25]*4 +
              [8.0]*11 + [12.0] + [3.0] + [23.0])
assert LO_B == LO_B_check and HI_B == HI_B_check, (LO_B, HI_B)

names = [f'c{i}' for i in range(16)] + [f'a{i}' for i in range(1, 13)] + ['q', 'r_m']
table = []
for i in range(30):
    inside = LO_B[i] <= clipped[i] <= HI_B[i]
    outside_by = 0.0 if inside else max(LO_B[i] - clipped[i], clipped[i] - HI_B[i])
    table.append({'index': i, 'name': names[i], 'value': clipped[i],
                  'lo': LO_B[i], 'hi': HI_B[i], 'inside': bool(inside),
                  'outside_by': float(outside_by)})
all_inside = all(r['inside'] for r in table)
assert all_inside

amendment = {
    'item': 'Phase 408 Amendment A-408-1: clipped Arm B seed of record (Worker A2)',
    'amendment': 'A-408-1 (2026-11-26, coordinator ruling on the C-408-5 containment failure)',
    'seed_name': 'RW-5_embedded_ls_16mode_boxclipped_c13',
    'seed_wording_required_downstream': 'RW-5 embedded, box-clipped at c13',
    'unclipped_vector': unclipped,
    'unclipped_vector_sha256_float64_tobytes': unclipped_sha,
    'unclipped_sha256_expected': EXPECTED_UNCLIPPED_SHA,
    'unclipped_sha256_verified': bool(unclipped_sha == EXPECTED_UNCLIPPED_SHA),
    'clipped_vector': clipped,
    'clipped_vector_sha256_float64_tobytes': clipped_sha,
    'clip_record': {
        'index': 13,
        'name': 'c13',
        'coordinate_block': 'c (16-mode grading coefficients, indices 0..15)',
        'unclipped_value': unclipped[13],
        'clipped_value': clipped[13],
        'bound_lo': -2.25,
        'bound_hi': 2.25,
        'excess_outside_box_unclipped': excess,
        'n_coordinates_differing_from_unclipped': len(diff_idx),
        'differing_indices': diff_idx,
    },
    'armB_box_lo': LO_B,
    'armB_box_hi': HI_B,
    'containment_table_clipped_vector': table,
    'all_30_coordinates_inside_armB_box': bool(all_inside),
    'containment_verdict': 'PASS — clipped vector inside the Arm B box at all 30 coordinates',
}
dump(amendment, os.path.join(RES, 'p408_amendment_A408_1.json'))

# ---------- Shared spec inputs ----------
spec_r16 = json.load(open(os.path.join(P392, 'work', 'p392_spec_r16_de.json')))
state_r16 = json.load(open(os.path.join(P392, 'results', 'p392_pool_r16_de_state.json')))
LO_A = [float(v) for v in spec_r16['lo']]
HI_A = [float(v) for v in spec_r16['hi']]
assert LO_A == [float(v) for v in state_r16['box_lo']]
assert HI_A == [float(v) for v in state_r16['box_hi']]
y_ref_a = [float(v) for v in spec_r16['y_ref']]
assert y_ref_a[29] == 16.187589217631558

# ---------- Task 2: Arm A spec ----------
pop64 = [[float(v) for v in row] for row in state_r16['pop']]
assert len(pop64) == 64 and all(len(r) == 30 for r in pop64)
for row in pop64:
    assert all(LO_A[i] <= row[i] <= HI_A[i] for i in range(30))
spec_a = {'tag': 'a408', 'lib': 'p392_16', 'lo': LO_A, 'hi': HI_A,
          'cap_min': 120, 'pop': 64, 'y_ref': y_ref_a,
          'seed_ys': pop64,
          'seed_names': ['staged_population_64_in_stored_order']}
dump(spec_a, os.path.join(WORK, 'p408_spec_a_de.json'))

# ---------- Task 3: Arm B spec ----------
verdicts = json.load(open(os.path.join(P392, 'results', 'p392_verdicts.json')))
rw5 = [float(v) for v in verdicts['subjects']['RW-5']['y']]
assert len(rw5) == 26
assert sha(rw5) == '44719b508ba733bb257281f994f90340b1ac25b33684bbe8ac9c4da5f10535c2'
# RW-5 26-vector layout: c 0..11, a 12..23, q 24, r_m 25
y_his_equiv = [0.0]*16 + rw5[12:24] + [rw5[24], rw5[25]]
assert y_his_equiv[28] == 1.6681638067393412 and y_his_equiv[29] == 16.17148847124908
# cross-check against Worker A's stored y_his_equivalent in controls
stored_yhe = controls['C-408-5']['y_his_equivalent_armB']['y']
assert y_his_equiv == [float(v) for v in stored_yhe]
assert sha(y_his_equiv) == controls['C-408-5']['y_his_equivalent_armB']['vector_sha256_float64_tobytes']
for vec in (y_his_equiv, clipped):
    assert all(LO_B[i] <= vec[i] <= HI_B[i] for i in range(30))
assert clipped[29] == 16.17148847124908
spec_b = {'tag': 'b408', 'lib': 'p392_16', 'lo': LO_B, 'hi': HI_B,
          'cap_min': 120, 'pop': 64, 'y_ref': clipped,
          'seed_ys': [y_his_equiv, clipped],
          'seed_names': ['y_his_equivalent', 'RW-5_embedded_ls_16mode_boxclipped_c13']}
dump(spec_b, os.path.join(WORK, 'p408_spec_b_de.json'))

# ---------- Task 4: Powell-starts + harvest templates ----------
for tag, lo, hi, yref, state_path in (
        ('a408', LO_A, HI_A, y_ref_a, '~/work/p408/state/a408_de_state.json'),
        ('b408', LO_B, HI_B, clipped, '~/work/p408/state/b408_de_state.json')):
    arm = tag[0]
    starts = {
        'tag': tag, 'lib': 'p392_16', 'lo': lo, 'hi': hi, 'maxfev': 1500,
        'de_state_path': state_path,
        'picked_idx': 'PLACEHOLDER — Worker B fills at runtime from the DE state at de_state_path (top 3 distinct pop members, 392 p392_make_followups pattern)',
        'picked_fit': 'PLACEHOLDER — Worker B fills at runtime (screening beta_crit of the picked members)',
        'picked_brackets': 'PLACEHOLDER — Worker B fills at runtime (screening brackets of the picked members)',
        'picked_hashes': 'PLACEHOLDER — Worker B fills at runtime (sha256 float64 tobytes of each picked member)',
        '_template_note': ('TEMPLATE (Worker A2, pre-search): mirrors p392_spec_r16_powell_starts.json '
                           '(picked_idx/picked_fit/picked_brackets/picked_hashes). DEVIATION from the 392 pattern, '
                           'by tasking: the 392 powell_starts file was written AFTER its DE finished and embeds the '
                           'actual picked members\' indices/fits/brackets/hashes, and the individual '
                           'p392_spec_*_powell_de{n}.json files embed the actual start_y vectors; here the DE has not '
                           'run, so those fields are clearly-marked placeholders referencing the DE state file path '
                           'instead of embedded member vectors. Worker B completes this file at runtime and writes the '
                           'per-start powell specs (keys tag/name/lib/start_y/lo/hi/maxfev, maxfev=1500) from the picked '
                           'members, exactly as p392_make_followups.py does. tag/lib/lo/hi/maxfev/de_state_path are final.'),
    }
    dump(starts, os.path.join(WORK, f'p408_spec_{arm}_powell_starts.json'))
    harvest = {
        'tag': tag, 'lib': 'p392_16', 'candidates': [],
        'y_ref': yref, 'top_k': 6, 'distinct_min': 0.05,
        'de_state_path': state_path,
        '_template_note': ('TEMPLATE (Worker A2, pre-search): mirrors p392_spec_r16_harvest.json '
                           '(keys tag/lib/candidates/y_ref/top_k/distinct_min). candidates is EMPTY by design. '
                           'Worker B fills candidates at runtime from the DE state at de_state_path plus the Powell '
                           'results, following the 392 pattern (each {provenance, y, source_beta_crit_screening}: '
                           'DE pop members by screening beta_crit, then the Powell polishes; the harvest then takes '
                           'top <=6 distinct, pairwise ||dy||_inf >= 0.05 over the (c,a) block, plus the registered '
                           'control member for this arm). y_ref/top_k/distinct_min are final.'),
    }
    dump(harvest, os.path.join(WORK, f'p408_spec_{arm}_harvest.json'))

print(json.dumps({
    'unclipped_sha256': unclipped_sha,
    'clipped_sha256': clipped_sha,
    'y_his_equivalent_sha256': sha(y_his_equiv),
    'all_clipped_inside': all_inside,
    'armA_seeds': len(pop64),
    'armB_y_ref_r_m': clipped[29],
}, indent=1))
