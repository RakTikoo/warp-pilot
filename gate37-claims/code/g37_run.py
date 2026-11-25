#!/usr/bin/env python3
"""Gate-37 deciding evaluations with the gate's own engine.
Writes g37_results.json.  Targets are the stored record values
(Phase 318/323); this script computes everything itself."""
import json, time
from fractions import Fraction as Fr
import sys
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate37/work')
from g37_engine import point, extract_E

def s(x):
    if isinstance(x, Fr):
        return str(x.numerator) if x.denominator == 1 else \
            f"{x.numerator}/{x.denominator}"
    return x

def run(name, kind, target_diag=None, target_ric=None, exact=True):
    t0 = time.time()
    S2, gtt, ex = point(name)
    r = extract_E(S2, gtt, kind, ex)
    out = {
        'point': name, 'scalar': kind,
        'E_mixed_diag': [s(v) for v in r['E_mixed_diag']],
        'Ric_mixed': [s(v) for v in r['Ric_mixed']],
        'div': [s(v) for v in r['div']],
        'offdiag_max': s(r['offdiag_max']),
        'trace': s(r['trace']),
        'L0': s(r['L0']),
        'wall_s': round(time.time() - t0, 1),
    }
    if target_diag is not None:
        out['target_diag'] = [s(v) for v in target_diag]
        out['diag_match'] = ([Fr(v) if not isinstance(v, float) else v
                              for v in r['E_mixed_diag']] ==
                             [Fr(v) if not isinstance(v, float) else v
                              for v in target_diag])
    if target_ric is not None:
        out['target_Ric'] = [s(v) for v in target_ric]
        out['ric_match'] = (r['Ric_mixed'] == target_ric)
    out['div_zero'] = all(v == 0 for v in r['div'])
    out['offdiag_zero'] = (r['offdiag_max'] == 0)
    print(name, kind, out['E_mixed_diag'], 'div0:', out['div_zero'],
          'offdiag0:', out['offdiag_zero'], 'wall', out['wall_s'],
          flush=True)
    return out

res = {}
# ---- calibrations
res['cal_ellis_l1_L2'] = run(
    'ellis_l1', 'L2',
    target_diag=[Fr(47, 8), Fr(1, 8), Fr(55, 8), Fr(55, 8)],
    target_ric=[Fr(0), Fr(-1, 2), Fr(0), Fr(0)])
res['cal_ellis_throat_Ric3'] = run(
    'ellis_throat', 'Ric3',
    target_diag=[Fr(-32), Fr(-8), Fr(-44), Fr(-44)],
    target_ric=[Fr(0), Fr(-2), Fr(0), Fr(0)])
res['cal_ellis_throat_RiemRic'] = run(
    'ellis_throat', 'RiemRic',
    target_diag=[Fr(-4), Fr(-4), Fr(-16), Fr(-16)],
    target_ric=[Fr(0), Fr(-2), Fr(0), Fr(0)])
S2, gtt, ex = point('ellis_R15_float')
t0 = time.time()
r = extract_E(S2, gtt, 'L2', ex)
res['cal_ellis_R15_float_L2'] = {
    'point': 'ellis_R15_float', 'scalar': 'L2',
    'E_mixed_diag': r['E_mixed_diag'],
    'target_diag': [2.9095233525452513, 0.6281487502846053,
                    2.8941086592867307, 2.8941086592867307],
    'max_dev': max(abs(a - b) for a, b in
                   zip(r['E_mixed_diag'],
                       [2.9095233525452513, 0.6281487502846053,
                        2.8941086592867307, 2.8941086592867307])),
    'div_max': max(abs(v) for v in r['div']),
    'wall_s': round(time.time() - t0, 1)}
print('ellis_R15_float L2', res['cal_ellis_R15_float_L2']['E_mixed_diag'],
      'max_dev', res['cal_ellis_R15_float_L2']['max_dev'], flush=True)
# ---- deciding reads
res['dec_ellis_throat_L2'] = run(
    'ellis_throat', 'L2',
    target_diag=[Fr(-80), Fr(-16), Fr(-112), Fr(-112)],
    target_ric=[Fr(0), Fr(-2), Fr(0), Fr(0)])
res['dec_A_throat_L2'] = run(
    'A_throat', 'L2',
    target_diag=[Fr(-9, 4), Fr(-3, 4), Fr(-21, 4), Fr(-21, 4)],
    target_ric=[Fr(0), Fr(-1), Fr(1, 2), Fr(1, 2)])
res['dec_C12_L2'] = run(
    'C_1_2', 'L2',
    target_diag=[Fr(-5645, 4), Fr(-1375, 4), Fr(-7705, 4), Fr(-7705, 4)],
    target_ric=[Fr(0), Fr(-5), Fr(-3, 2), Fr(-3, 2)])
res['dec_E110_L2'] = run(
    'E_1_10', 'L2',
    target_diag=[Fr(-1591), Fr(-110), Fr(-3005, 4), Fr(-3005, 4)],
    target_ric=[Fr(-2), Fr(-3), Fr(1, 2), Fr(1, 2)])

with open('/home/hatch/workspace/warp-pilot/gate37/work/'
          'g37_results.json', 'w') as f:
    json.dump(res, f, indent=1, default=str)
print('WROTE g37_results.json')
