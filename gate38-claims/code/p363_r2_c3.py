#!/usr/bin/env python3
"""Phase 363 R2 localisation inside the driver's c3 group: per-monomial
raw mixed values, driver (float) vs exact library (Fractions), aligned
in the programme order Phase 361 Arm B established."""
import sys, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase361/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase355/work/step3')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase259/work')
import p2591_engine_d as ed
ed.DTYPE = object
import p355_print_eval as p355
import p361_eval as ev
from p355_print_eval import E0

RES = json.load(open('/home/hatch/workspace/warp-pilot/phase361/work/'
                     'df_resolved_transcription.json'))['equations']
terms = RES['3.15']

# exact side
g_s = p355.sss_jet([Fr(1), Fr(0), Fr(1)], [Fr(-1)])
S = ed.build_series_general(g_s, 7)
F = ed.fields(S)
f = ev.fields_from_355(S, F)
_dR = ed.assemble_first(ed.covd_any(S['Riem'], S['Gam'], 4, [-1, -1, -1, -1]),
                        (4, 4, 4, 4))
_ddR = ed.assemble_first(ed.covd_any(_dR, S['Gam'], 4, [-1, -1, -1, -1, -1]),
                         (4, 4, 4, 4, 4))
_v = _ddR.get(E0)
f['ddRiem'] = np.zeros((4, 4, 4, 4, 4, 4), dtype=object) if _v is None else _v
M, Sc = ev.monomials(f)
exact_raw = {}
for t in terms:
    mid = t['monomial']
    if mid.startswith('N'):
        exact_raw[mid] = ev.mixed_diag(f, M[mid])
    else:
        exact_raw[mid] = ev.mixed_diag(f, f['g'] * Sc[mid])

# driver side
import importlib.util
spec = importlib.util.spec_from_file_location(
    'harness', '/home/hatch/workspace/warp-pilot/phase259/work/p2591_harness.py')
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)
NS = harness.NS
bg = [b for b in harness.build_backgrounds() if b['name'] == 'Ellis R=1.0'][0]
G = harness.build_geometry(bg['Phi1'], bg['R1'])
P = harness.deriv_pack(G)

entries = list(NS['MONO']) + list(NS['TMONO'])
assert len(entries) == len(terms), (len(entries), len(terms))
rows = []
for i, ((group, spec_, fn), t) in enumerate(zip(entries, terms)):
    mid = t['monomial']
    coef = NS['expand_coef'](spec_)
    c0 = Fr(coef[0]) if len(coef) > 0 else Fr(0)
    T = fn(G, P)
    if T is None:
        continue
    if i < len(NS['MONO']):
        raw = [NS['mixed_val'](G, T, a) for a in range(3)]
    else:
        raw = [float(T[0, 0])] * 3
    er = exact_raw[mid]
    rows.append({'i': i, 'group': group, 'monomial': mid,
                 'xi0_coef': str(c0), 'driver_raw': raw,
                 'exact_raw': [str(x) for x in er[:3]],
                 'diff_Tr_bracket': str(210 * c0 * (Fr(raw[1]).limit_denominator(10**9) - er[1]))})
for r in rows:
    flag = '  <<<' if r['group'] == 'c3' and abs(float(r['diff_Tr_bracket'])) > 1e-6 else ''
    print(r['i'], r['group'], r['monomial'], 'coef', r['xi0_coef'],
          'driver', ['%.6g' % x for x in r['driver_raw']],
          'exact', r['exact_raw'], 'dTr', r['diff_Tr_bracket'], flag)
json.dump(rows, open('/home/hatch/workspace/warp-pilot/phase363/work/'
                     'p363_r2_c3_out.json', 'w'), indent=1, default=str)
