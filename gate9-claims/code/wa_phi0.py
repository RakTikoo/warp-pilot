"""
W-A anchor (iii): Phi=0 slice, power shapes b = r^p at exact rational p.
Float64 CSE-lambdified evaluation (the engine's exactness is already
established by anchors (i)/(ii); this anchor checks the slice
IDENTITIES and the NEC1 factorisation formula):
  NEC1 = (p-3)(p-1)(1-3p+2p q)/(6 r^{6-2p}), q = r^{1-p}
  DEC_r = rho - |p_r| vs NEC1 ; SEC vs 2 rho ; DEC_t vs NEC2 (measured).
B-combinations: rho=-Bt, pr=Br, pt=Bth.
"""
import sys, json, time
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate9')
import sympy as sp
import numpy as np
from wa_engine import build_bach, r, th

res = {'ps': {}, 'max_nec1_formula_relerr': 0.0}
for p in (sp.Rational(1, 10), sp.Rational(3, 10), sp.Rational(1, 2),
          sp.Rational(7, 10), sp.Rational(9, 10)):
    t0 = time.time()
    out = build_bach(r**p, sp.Integer(0), final_simplify=False)
    fns = [sp.lambdify(r, out[k].subs(th, 1), modules='numpy', cse=True)
           for k in ('Bt', 'Br', 'Bth')]
    pf = float(p)
    rows = []
    for rr in (1.5, 2.0, 5.0, 10.0, 100.0):
        bt, br, bth = (float(f(rr)) for f in fns)
        rho, pr, pt = -bt, br, bth
        nec1 = rho + pr
        q = rr ** (1 - pf)
        f = (pf - 3) * (pf - 1) * (1 - 3 * pf + 2 * pf * q) / (6 * rr ** (6 - 2 * pf))
        rel = abs(nec1 - f) / abs(f)
        res['max_nec1_formula_relerr'] = max(res['max_nec1_formula_relerr'], rel)
        rows.append({
            'r': rr, 'nec1': nec1, 'nec1_formula': f, 'nec1_relerr': rel,
            'pr': pr, 'pt': pt,
            'dec_r_minus_nec1': (rho - abs(pr)) - nec1,
            'sec_minus_2rho': (rho + pr + 2 * pt) - 2 * rho,
            'dec_t': rho - abs(pt), 'nec2': rho + pt,
            'dec_t_minus_nec2': (rho - abs(pt)) - (rho + pt),
            'trace': -rho + pr + 2 * pt,
        })
    res['ps'][str(p)] = {'rows': rows, 'build_s': time.time() - t0}
    print('p', p, 'done, max relerr so far', res['max_nec1_formula_relerr'], flush=True)
res['PASS_factorisation'] = res['max_nec1_formula_relerr'] < 1e-8
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_phi0.json', 'w') as fh:
    json.dump(res, fh, indent=1)
print('factorisation PASS', res['PASS_factorisation'])
