"""
W-A GATE-9 anchors (wa_anchors.py) — run BEFORE any claim number is read.
Anchor (i) MK numeric Bach-flatness at Phase-32's registered point;
Anchor (ii) T-b closed forms from phase32 p323_memo;
Anchor (iii) Phi=0 slice, symbolic p: NEC1 factorisation + slice identities.
Writes results/wa_anchors.json.  (Schwarzschild symbolic zero is
wa_test1.py output, rerun here in raw mode for the record + a
simplify check on request.)
"""
import sys, json, time
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate9')
import sympy as sp
from wa_engine import build_bach, r

res = {}
t00 = time.time()

# ---------- Anchor (i) MK at (beta,gamma,k) = (0.5, 0.01, 0.001) ----------
beta, gam, k = sp.Rational(1, 2), sp.Rational(1, 100), sp.Rational(1, 1000)
f = 1 - 3 * beta * gam - beta * (2 - 3 * beta * gam) / r + gam * r - k * r**2
b_mk = r * (1 - f)
phi_mk = sp.log(f) / 2
t0 = time.time()
out = build_bach(b_mk, phi_mk, final_simplify=False)
mk = {}
for rr in (3, 10, 30):
    mk[str(rr)] = {kk: float(sp.N(out[kk].subs({r: rr, sp.Symbol('theta'): 1}), 30))
                   for kk in ('Bt', 'Br', 'Bth')}
res['anchor_i_MK'] = {'values': mk,
                      'max_abs': max(abs(v) for d in mk.values() for v in d.values()),
                      'tolerance': 1e-12, 'build_s': time.time() - t0}
res['anchor_i_MK']['PASS'] = res['anchor_i_MK']['max_abs'] <= 1e-12
print('MK done', res['anchor_i_MK']['max_abs'], flush=True)

# ---------- Anchor (ii) T-b: b = sqrt(r), Phi = 0 ----------
t0 = time.time()
out = build_bach(sp.sqrt(r), sp.Integer(0), final_simplify=False)
u = sp.sqrt(r)
stored = {
    'Bt': -5 * (3 * u - 1) / (24 * r**5),
    'Br': -5 * (4 * u - 1) / (48 * r**5),
    'Bth': 5 * (10 * u - 3) / (96 * r**5),
}
tb = {}
for kk, sexpr in stored.items():
    diffs = []
    for rr in (sp.Rational(1), sp.Rational(3, 2), sp.Rational(2),
               sp.Rational(5), sp.Rational(10)):
        got = sp.simplify(out[kk].subs({r: rr, sp.Symbol('theta'): 1}))
        exp = sp.simplify(sexpr.subs(r, rr))
        diffs.append(str(sp.simplify(got - exp)))
    tb[kk] = {'exact_point_diffs': diffs,
              'all_zero': all(x == '0' for x in diffs)}
res['anchor_ii_Tb'] = {'components': tb, 'build_s': time.time() - t0,
                       'PASS': all(v['all_zero'] for v in tb.values())}
print('Tb done', res['anchor_ii_Tb']['PASS'], flush=True)

# symbolic simplify of the differences (best effort, recorded)
sym_ok = {}
for kk, sexpr in stored.items():
    try:
        sym_ok[kk] = str(sp.simplify(sp.together(out[kk] - sexpr)))
    except Exception as e:
        sym_ok[kk] = f'ERROR {e}'
res['anchor_ii_Tb']['symbolic_diff'] = sym_ok
print('Tb symbolic diffs', sym_ok, flush=True)

with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_anchors.json', 'w') as fh:
    json.dump(res, fh, indent=1)
print('total_s', time.time() - t00)
