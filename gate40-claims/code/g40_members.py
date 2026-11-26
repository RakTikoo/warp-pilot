#!/usr/bin/env python3
"""Gate-40 member table: Phase 374's registered family (entry 943 /
p374_registration SS2), the anchor, and Phase 364's Gate-39-verified
champions (calibration targets)."""
import numpy as np

SUBSETS = {'M': {'M'}, 'SNM': {'S', 'N', 'M'}}


def mk(subset, a, T, D=0.75, m=0.75):
    mname = '0.75' if m == 0.75 else '0.88'
    name = f"{subset}_a{a:.2f}_T{T}_D{D:.3f}_m{mname}"
    return {'name': name, 'subset': SUBSETS[subset], 'subset_name': subset,
            'a': a, 'T': T, 'Om': 2.0 * np.pi / T, 'D': D, 'm': m}


def bottom_mu(mem):
    return 1.0 + mem['a'] * (2.0 * mem['m'] - 1.0)


def top_mu(mem):
    return 1.0 + mem['a']


ANCHOR = {'name': 'ANCHOR', 'subset': set(), 'subset_name': 'NONE',
          'a': 0.0, 'T': None, 'Om': 1.0, 'D': 0.75, 'm': 0.75}

# Phase 374 family: order subset (M, SNM), a (0.15, 0.30), T (320, 640),
# m (0.75, 0.875) -- registration SS2 order.
FAMILY374 = [mk(s, a, T, 0.75, m)
             for s in ('M', 'SNM') for a in (0.15, 0.30)
             for T in (320, 640) for m in (0.75, 0.875)]

# Phase 364 champions (Gate-39 quotable set, J = 128):
# name -> (NEC_worst, phi_nec, DEC_worst, phi_dec)
CHAMPS364 = {
    'SNM_a0.30_T160_D0.750_m0.75': (-2.169047936502377e-4, 2.9943304979527716,
                                   -1.8546990569430298e-4, np.pi),
    'M_a0.30_T160_D0.750_m0.75': (-2.224589e-4, 3.2889,
                                 -1.8546990569430298e-4, np.pi),
    'SNM_a0.15_T160_D0.750_m0.75': (-2.256428e-4, 2.9943,
                                   -2.032703e-4, np.pi),
    'M_a0.15_T160_D0.750_m0.75': (-2.272118e-4, 2.9943,
                                 -2.032703e-4, np.pi),
}
FAMILY364 = [mk(s, a, 160, 0.75, 0.75)
             for s in ('SNM', 'M') for a in (0.30, 0.15)]
