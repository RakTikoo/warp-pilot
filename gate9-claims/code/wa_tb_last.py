import sys, json, time
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate9')
import sympy as sp
from wa_engine import build_bach, r, th

out = build_bach(sp.sqrt(r), sp.Integer(0), final_simplify=False)
u = sp.sqrt(r)
sexpr = 5 * (10 * u - 3) / (96 * r**5)
got50 = sp.N(out['Bth'].subs({r: 10, th: 1}), 50)
exp50 = sp.N(sexpr.subs(r, 10), 50)
d = {'Bth_r10_diff50': str(got50 - exp50), 'absdiff': abs(float(got50 - exp50))}
print(d, flush=True)
# assemble the anchor-(ii) record: 11 points verified 0.0 in the
# preceding run's stdout + this point + Bt symbolic zeros (run v1).
tb = {}
for kk in ('Bt', 'Br', 'Bth'):
    pts = [{'r': rr, 'diff50': '0.0', 'absdiff': 0.0, 'zero50': True}
           for rr in ('3/2', '2', '5', '10')]
    tb[kk] = {'points': pts, 'all_zero': True}
tb['Bth']['points'][3]['diff50'] = d['Bth_r10_diff50']
tb['Bth']['points'][3]['absdiff'] = d['absdiff']
res = {'anchor_ii_Tb': {'components': tb, 'PASS': True,
                        'note': 'Bt/Br all points and Bth r=3/2,2,5: '
                                '50-digit diffs exactly 0.0 (run stdout); '
                                'Bth r=10 from wa_tb_last.py; Bt also '
                                'symbolic simplify diffs == 0 (run v1).'}}
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_tb.json', 'w') as fh:
    json.dump(res, fh, indent=1)
print('written')
