"""Home-side helper (Worker B): from a pool DE state JSON, write the
Powell-start specs (top 3 distinct pop members) and, after Powell, the
harvest spec. Usage:
  p392_make_followups.py powell <state.json> <de_spec.json> <out_prefix>
  p392_make_followups.py harvest <state.json> <de_spec.json> <powell_json...> <out.json>
Distinctness: pairwise ||dy||_inf >= 0.05 over the (c,a) block (all but
last two coords), 391 pattern."""
import sys, json, hashlib
import numpy as np

def sha(y): return hashlib.sha256(np.asarray(y, dtype=np.float64).tobytes()).hexdigest()

def top_distinct(state, k, dmin=0.05):
    pop = np.array(state['pop'], dtype=np.float64)
    fit = np.array(state['beta_crit'], dtype=np.float64)
    order = np.argsort(-fit)
    picked = []
    for i in order:
        if all(np.max(np.abs(pop[i][:-2] - pop[j][:-2])) >= dmin for j in picked):
            picked.append(int(i))
        if len(picked) >= k:
            break
    return picked, [float(fit[i]) for i in picked], [state['brackets'][i] for i in picked]

if sys.argv[1] == 'powell':
    state = json.load(open(sys.argv[2])); spec = json.load(open(sys.argv[3]))
    prefix = sys.argv[4]
    picked, fits, brs = top_distinct(state, 3)
    out = {'picked_idx': picked, 'picked_fit': fits, 'picked_brackets': brs,
           'picked_hashes': [sha(state['pop'][i]) for i in picked]}
    for n, i in enumerate(picked):
        ps = {'tag': spec['tag'], 'name': f'de{n}', 'lib': spec['lib'],
              'start_y': state['pop'][i], 'lo': spec['lo'], 'hi': spec['hi'],
              'maxfev': 1500}
        json.dump(ps, open(f'{prefix}_powell_de{n}.json', 'w'), indent=1)
    json.dump(out, open(f'{prefix}_powell_starts.json', 'w'), indent=1)
    print(json.dumps(out))
elif sys.argv[1] == 'harvest':
    state = json.load(open(sys.argv[2])); spec = json.load(open(sys.argv[3]))
    powell_files = sys.argv[4:-1]; out_path = sys.argv[-1]
    pop = state['pop']; fit = state['beta_crit']
    order = np.argsort(-np.array(fit))
    cands = []
    for rank, i in enumerate(order[:12]):
        cands.append({'provenance': f"{spec['tag']} GPU DE pop member rank{rank} (union-set bc {fit[i]})",
                      'y': pop[i], 'source_beta_crit_screening': float(fit[i])})
    best_i = int(order[0])
    cands[0]['provenance'] = f"{spec['tag']} GPU DE best (union set)"
    for pf in powell_files:
        pj = json.load(open(pf))
        cands.append({'provenance': f"{spec['tag']} Powell polish of DE top member {pj['start']}",
                      'y': pj['y_opt'], 'source_beta_crit_screening': pj['beta_crit_screening']})
    hs = {'tag': spec['tag'], 'lib': spec['lib'], 'candidates': cands,
          'y_ref': spec['y_ref'], 'top_k': 6, 'distinct_min': 0.05}
    json.dump(hs, open(out_path, 'w'), indent=1)
    print(f'harvest spec: {len(cands)} candidates -> {out_path}')
