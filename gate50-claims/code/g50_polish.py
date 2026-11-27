#!/usr/bin/env python3
"""
g50_polish.py -- Gate-50 adversary polishes (the
frame-invariant deciding statistic for claims (a)
and the base control), plus the C395 diagnostic read
(an independent stored configuration whose TG tests
this gate's margin machinery, sampled fallback
included, on a configuration outside the claim set).
Writes gate50/results/g50_polish.json.
"""
import json
import os
import sys

import numpy as np

WP = os.environ.get('G50_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/gate50/work')
import g50_lib as G  # noqa: E402

out = {}


def polish_block(name, prof_fn, stored_polish):
    s, aux = G.set_read(prof_fn)
    pol = G.adversary_polish(prof_fn, aux)
    out[name] = {'polish': pol,
                 'stored_polish': stored_polish,
                 'diff': (pol['in_region_worst_nec_SAMPLER-M']
                          - stored_polish)}
    print(name, pol['in_region_worst_nec_SAMPLER-M'],
          'stored', stored_polish, 'diff', out[name]['diff'],
          flush=True)


# base winner polish (stored: p400 confirmation's
# polished depth)
polish_block('base_winner', G.prof_winner_base,
             float(G.INP['winner400']['polished_depth_SAMPLER-M']))
# claim (a): the 405 winner (stored polish
# +1.214723699102956e-06)
polish_block('winner405', G.prof_winner405,
             float(G.INP['conf405']['at_criterion_polish']))
# winner at stage peak 0.25 (stored polish
# +1.327026604141981e-06)
polish_block('winner405_p0.25', G.prof_winner_at_peak(0.25),
             float(G.INP['conf405']['at_stage_peak_0.25_polish']))

# ---------------- C395 diagnostic
C395 = (0.601180962300002, 1.5934531363763935, 4.887238651223381)
C395_TG = {'nec': -2.9809850277749006e-05,
           'dec': -1.7766846142506707e-06,
           'wec': -1.2604578745184045e-04,
           'sec': -4.6317591386364136e-04,
           'rho': 9.780857711542179e-05}
C395_WN = -3.0896210095678075e-05


def prof_c395(r):
    r = np.asarray(r, dtype=G.DT)
    h2 = G.h2_totals(r)
    muS, muN, muM = C395
    return (muS * h2[0], muS * h2[1], muS * h2[2],
            muN * h2[3], muN * h2[4], muN * h2[5],
            1.0 + muM * (h2[6] - 1.0), muM * h2[7],
            muM * h2[8])


s, aux = G.set_read(prof_c395)
pt = np.array(s['nec_argmin_point'])
nec, ti, That = G.nec_at(prof_c395, pt)
q, _m, _l = G.worst_null_exact(That)
out['C395_diagnostic'] = {
    'joint': G.joint_of(s),
    'cmp': {k: {'gate': s[k]['min'], 'stored': C395_TG[k],
                'diff': s[k]['min'] - C395_TG[k]}
            for k in ('nec', 'dec', 'wec', 'sec', 'rho')},
    'typeI_fraction': s['typeI_fraction'],
    'nec_argmin_r': s['nec_argmin_r'],
    'worst_null_at_nec_argmin': q,
    'worst_null_stored': C395_WN,
    'worst_null_diff': q - C395_WN}
print('C395 diagnostic done', flush=True)

json.dump(out, open(f'{WP}/gate50/results/g50_polish.json', 'w'),
          indent=1)
print('g50_polish complete')
