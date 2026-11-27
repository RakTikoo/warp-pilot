#!/usr/bin/env python
"""g59_crossing.py -- Gate-59 precision cross-check of the
A_t2_6_6 verbatim representation crossing.

Three evaluations of R_F(t) for the stored A_t2 mating:
  (a) Acoef pair form (phases exp(-i dE t), dE exact float
      differences) -- the form of the phase's own grid read;
  (b) per-mode pair form in float64 (coefficients
      exp(i p.x - i E t)) -- the form the phase's driver used
      for its spots and first_crossing (B2.RF_t);
  (c) per-mode pair form with the phase argument computed
      and reduced mod 2pi in longdouble before casting --
      the faithful version of (b).
If (a) == (c) and (b) departs, the faithful crossing is
(a)'s. Writes gate59/results/g59_crossing.json.
"""
import json
import sys

import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate59/work')
import g59_lib as G  # noqa: E402

RES = f'{WP}/gate59/results'
BAR = 1e-9


def avecs(rows):
    return np.array([[complex(*z) for z in row] for row in rows])


tg = json.load(open(f'{WP}/phase420/work/p420_targets.json'))
XS = [np.array(s['point']) for s in tg['sitesA']]
TG = [np.array(s['T_corr']) for s in tg['sitesA']]
bj = json.load(open(f'{WP}/phase431/work/p431_best_A_t2_6_6.json'))
pv = np.array(bj['pvecs']); av = avecs(bj['avecs'])
mm = np.array(bj['masses'])
S = G.pair_kernel(pv, av, mm)
Ek = G.energies(pv, mm)
TWO_PI_LD = np.longdouble('6.283185307179586476925286766559')


def RF_acoef(t):
    return float(G.RF_grid_pair(S, pv, XS, TG, np.array([t]),
                                mm=mm)[0])


def coeffs(t, longdouble=False):
    cs = []
    for si, x in enumerate(XS):
        row = []
        for k in range(len(pv)):
            if longdouble:
                ph = (np.longdouble(float(pv[k] @ x))
                      - np.longdouble(float(Ek[k]))
                      * np.longdouble(t))
                ph = ph % TWO_PI_LD
                row.append(np.exp(1j * float(ph)))
            else:
                row.append(np.exp(1j * float(pv[k] @ x)
                                  - 1j * float(Ek[k]) * t))
        cs.append(np.array(row))
    return cs


def RF_permode(t, longdouble=False):
    cs = coeffs(t, longdouble)
    return max(float(np.linalg.norm(
        np.einsum('i,ijab,j->ab', cs[si].conj(), S,
                  cs[si]).real - TG[si]))
        for si in range(len(XS)))


out = {'gate': 59}
probe_t = [2e5, 2e6, 2e7, 35727055.84393014, 67210312.02652377,
           2e8]
rows = {}
for t in probe_t:
    rows[f'{t:.6g}'] = {
        'acoef': RF_acoef(t),
        'permode_float64': RF_permode(t, False),
        'permode_longdouble_phase': RF_permode(t, True)}
    print(t, rows[f'{t:.6g}'], flush=True)
out['R_F_probes'] = rows


def bisect(form, lo, hi):
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if form(mid) > BAR:
            hi = mid
        else:
            lo = mid
        if hi - lo < 1e-2:
            break
    return 0.5 * (lo + hi)


# bracket from the probes: acoef crosses between 3.57e7 and 2e8
out['crossing_acoef'] = bisect(RF_acoef, 3.0e7, 2.0e8)
out['crossing_permode_longdouble'] = bisect(
    lambda t: RF_permode(t, True), 3.0e7, 2.0e8)
out['stored_driver_crossing'] = 35727055.84393014
out['sec_per_unit'] = 1.218123e8 / 3.6518e16
out['crossing_acoef_s'] = out['crossing_acoef'] * out['sec_per_unit']
out['crossing_ld_s'] = (out['crossing_permode_longdouble']
                        * out['sec_per_unit'])
print('crossing acoef:', out['crossing_acoef'],
      '=', out['crossing_acoef_s'], 's')
print('crossing per-mode LD:', out['crossing_permode_longdouble'],
      '=', out['crossing_ld_s'], 's')
json.dump(out, open(f'{RES}/g59_crossing.json', 'w'), indent=1,
          default=str)
print('written g59_crossing.json')
