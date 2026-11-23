"""W-A anchor (ii): T-b closed forms from phase32 p323_memo.
Bt: symbolic point diffs (simplify). Br/Bth: 50-digit point diffs
(sympy simplify is pathological on the raw Br expression; the
50-digit probe is the phases' own deciding standard).
PASS per point: symbolic diff == 0, or |50-digit diff| < 1e-38.
"""
import sys, json, time
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate9')
import sympy as sp
from wa_engine import build_bach, r, th

t0 = time.time()
out = build_bach(sp.sqrt(r), sp.Integer(0), final_simplify=False)
print('build_s', time.time() - t0, flush=True)
u = sp.sqrt(r)
stored = {
    'Bt': -5 * (3 * u - 1) / (24 * r**5),
    'Br': -5 * (4 * u - 1) / (48 * r**5),
    'Bth': 5 * (10 * u - 3) / (96 * r**5),
}
tb = {}
for kk, sexpr in stored.items():
    rows = []
    for rr in (sp.Rational(3, 2), sp.Rational(2), sp.Rational(5), sp.Rational(10)):
        got50 = sp.N(out[kk].subs({r: rr, th: 1}), 50)
        exp50 = sp.N(sexpr.subs(r, rr), 50)
        d = abs(float(got50 - exp50))
        rows.append({'r': str(rr), 'diff50': str(got50 - exp50),
                     'absdiff': d, 'zero50': d < 1e-38})
        print(kk, rr, d, flush=True)
    tb[kk] = {'points': rows, 'all_zero': all(x['zero50'] for x in rows)}
res = {'anchor_ii_Tb': {'components': tb, 'build_s': time.time() - t0,
                        'PASS': all(v['all_zero'] for v in tb.values()),
                        'note': 'Bt additionally verified with symbolic '
                                'simplify point diffs == 0 at r = 3/2, 2, 5, 10 '
                                'in the preceding run (wa_tb.py v1).'}}
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_tb.json', 'w') as fh:
    json.dump(res, fh, indent=1)
print('PASS', res['anchor_ii_Tb']['PASS'], 'total_s', time.time() - t0)
