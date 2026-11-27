#!/usr/bin/env python3
"""
g52_extract.py -- Gate-52 stored-input extraction.

Extracts, ONCE, the stored numerical inputs the gate's deciding
reads need, from the primary phase artefacts (never from phase or
earlier-gate evaluation code), recording the md5 of every source
file. Output: gate52/results/g52_stored_inputs.json.

Sources:
  phase344/results/p344_confirmation.json  -> A2 K=33 vectors
  phase379/results/p379_confirmation.json  -> H2 K=17 vectors
  phase400/results/p400_confirmation.json  -> the 400 winner base
  phase405/results/p405_confirmation.json  -> the Gate-50 winner
                                              (criterion control)
  phase412/results/p412_rungs.json         -> the ladder winners
  phase412/results/p412_screens.jsonl      -> per-screen records
  phase412/results/p412_fit.json           -> the ladder fit record
  phase412/results/p412_controls.json      -> the phase's controls
"""
import hashlib
import json
import os

WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
OUT = f'{WP}/gate52/results/g52_stored_inputs.json'


def md5(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def load(rel):
    p = f'{WP}/{rel}'
    return json.load(open(p)), md5(p)


def main():
    inp = {'md5': {}}

    d344, m = load('phase344/results/p344_confirmation.json')
    inp['md5']['p344_confirmation'] = m
    a2 = [c for c in d344['confirmations'] if c['point'] == 'A2'][0]
    inp['A2'] = {'vS': a2['vS'], 'vN': a2['vN'], 'vM': a2['vM'],
                 'K': a2['K']}

    d379, m = load('phase379/results/p379_confirmation.json')
    inp['md5']['p379_confirmation'] = m
    h2 = [e for e in d379['confirmations'] if e['centre'] == 'H2'][0]
    inp['H2'] = {'vS': h2['vS'], 'vN': h2['vN'], 'vM': h2['vM']}

    d400, m = load('phase400/results/p400_confirmation.json')
    inp['md5']['p400_confirmation'] = m
    cand = d400['candidate']
    inp['winner400'] = {
        'muN': cand['muN'], 'muM': cand['muM'], 'K': cand['K'],
        'vN': cand['vN'], 'vM': cand['vM'],
        'joint': d400['joint'], 'nec_min': d400['nec_min'],
        'dec_min': d400['dec_min'], 'wec_min': d400['wec_min'],
        'sec_min': d400['sec_min'], 'rho_min': d400['rho_min'],
        'nec_argmin_r': d400['nec_argmin_r'],
        'typeI_fraction': d400['typeI_fraction'],
        'polished_depth_SAMPLER-M': d400['polished_depth_SAMPLER-M'],
    }

    d405, m = load('phase405/results/p405_confirmation.json')
    inp['md5']['p405_confirmation'] = m
    inp['conf405'] = d405

    dr, m = load('phase412/results/p412_rungs.json')
    inp['md5']['p412_rungs'] = m
    inp['rungs412'] = dr

    df, m = load('phase412/results/p412_fit.json')
    inp['md5']['p412_fit'] = m
    inp['fit412'] = df

    dc, m = load('phase412/results/p412_controls.json')
    inp['md5']['p412_controls'] = m
    inp['controls412'] = dc

    # screens: keep only the fields the gate re-judges
    sp = f'{WP}/phase412/results/p412_screens.jsonl'
    inp['md5']['p412_screens'] = md5(sp)
    screens = {}
    with open(sp) as f:
        for line in f:
            d = json.loads(line)
            screens[d['id']] = {
                k: d[k] for k in ('id', 'stage', 'K', 'tag',
                                  'target_peak', 'peak', 'vS_scaled',
                                  'joint', 'score', 'pen400',
                                  'nec_min', 'dec_min', 'wec_min',
                                  'sec_min', 'rho_min',
                                  'nec_argmin_r', 'dec_argmin_r',
                                  'typeI_fraction', 'feasible',
                                  'binding', 'local_at_nec_argmin')}
    inp['screens412'] = screens
    inp['n_screens412'] = len(screens)

    with open(OUT, 'w') as f:
        json.dump(inp, f, indent=1)
    print('wrote', OUT)
    print('screens:', len(screens))
    for k, v in inp['md5'].items():
        print(' md5', k, v)


if __name__ == '__main__':
    main()
