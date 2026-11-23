"""W-C static l=0 sector: fresh linearised-Bach traces on the member
background (and T-b control), from wc_bach5.py's fresh jet-space Bach
tensor in the RICCI FORM (arXiv:2505.17171 eq.6 — the shared
definition the phase record uses). Anchor validation (all passed
before any member trace was read): T-b closed forms (as recorded in
p711_static.py: Bt = -5(3 sqrt r - 1)/(24 r^5), etc.) reproduced with
ratio 1.0000000000000000 at every radius/component; member background
B reproduced against the stored values likewise; Schwarzschild
Bach-flat to ~1e-17. (An earlier Weyl-form assembly of mine,
wc_bach3/wc_bach4, failed the T-b anchor and was discarded — see the
W-C report's failure ledger.) Perturbation families (shared definitions):
delta_b: b_shape += eps (r-1)^2/r^2 ; delta_Phi: A += eps (r-1)^2/r^4,
with A = Phi, Blog = -0.5 ln(1 - b_shape/r).
Traces: float64 centred FD (eps 1e-4, halving check) and 40-digit
mpmath probes at 6 radii (eps 1e-6 centred FD on 40-digit values).
"""
import json, os
import numpy as np, sympy as sp
from mpmath import mp, mpf
mp.dps = 40
GATE = os.path.expanduser('~/workspace/warp-pilot/gate9')
E = json.load(open(os.path.join(GATE, 'wc_bach_expr.json')))
syms = sp.symbols('r A0:5 B0:5')
args = (syms[0],) + tuple(syms[1:6]) + tuple(syms[6:11])
BACH = {'t': sp.sympify(E['Bt']), 'r': sp.sympify(E['Br']), 'th': sp.sympify(E['Bth'])}
CF = {'ricci_form': {k: sp.lambdify(args, e, 'numpy') for k, e in BACH.items()}}
COMBOS = {'ricci_form': BACH}
Bfmp = {k: sp.lambdify(args, e, 'mpmath') for k, e in BACH.items()}
rs = sp.symbols('r', positive=True)
def deriv_exprs(p_rat, a_rat, which=None, eps_sym=0):
    b_shape = rs**p_rat
    if which == 'b': b_shape = b_shape + eps_sym*(rs-1)**2/rs**2
    Aex = a_rat*sp.log(rs)/(1+sp.log(rs)) if a_rat != 0 else sp.Integer(0)
    if which == 'P': Aex = Aex + eps_sym*(rs-1)**2/rs**4
    Blog = -sp.Rational(1, 2)*sp.log(1 - b_shape/rs)
    return ([sp.diff(Aex, rs, k) for k in range(5)],
            [sp.diff(Blog, rs, k) for k in range(5)])
def deriv_fns(p_rat, a_rat, which=None, module='numpy'):
    es = sp.symbols('eps')
    Ae, Be = deriv_exprs(p_rat, a_rat, which, es)
    return ([sp.lambdify((rs, es), e, module) for e in Ae],
            [sp.lambdify((rs, es), e, module) for e in Be])
def B_at(fa, fb, Bf, rv, eps=0.0):
    av = [f(rv, eps) for f in fa]; bv = [f(rv, eps) for f in fb]
    return np.array([Bf[k](rv, *av, *bv) for k in ('t', 'r', 'th')], dtype=float)
def closed_tb(rr):
    u = np.sqrt(rr)
    return np.array([-5*(3*u-1)/(24*rr**5), -5*(4*u-1)/(48*rr**5), 5*(10*u-3)/(96*rr**5)])

# ---- normalisation on T-b (Ricci form; expect factor exactly 1) ----
fa0, fb0 = deriv_fns(sp.Rational(1, 2), sp.Integer(0), None, 'numpy')
BEST = 'ricci_form'; Bf64 = CF[BEST]
_ratios = []
for rv in (1.05, 1.5, 2.0, 5.0, 10.0):
    _ratios.append(closed_tb(rv)/B_at(fa0, fb0, Bf64, rv))
_ratios = np.array(_ratios)
FACTOR = float(np.median(_ratios))
sel = {BEST: {'median_ratio': FACTOR, 'ratio_spread_rel': float(np.max(np.abs(_ratios/FACTOR - 1)))}}
print('T-b ratios median', FACTOR, 'spread', sel[BEST]['ratio_spread_rel'], flush=True)

# ---- Schwarzschild Bach-flatness of selected combo ----
A_s = sp.log(1-2/rs)/2
faS = [sp.lambdify(rs, sp.diff(A_s, rs, k), 'numpy') for k in range(5)]
fbS = [sp.lambdify(rs, sp.diff(-A_s, rs, k), 'numpy') for k in range(5)]
schw = []
for rv in (3.0, 5.0, 10.0):
    av = [f(rv) for f in faS]; bv = [f(rv) for f in fbS]
    schw.append([float(Bf64[k](rv, *av, *bv)) for k in ('t', 'r', 'th')])
schw_max = float(np.max(np.abs(schw)))
print('Schwarzschild max |B| (raw combo)', schw_max, flush=True)

# ---- trace numeric check on random jets (selected combo) ----
_trf = sp.lambdify(args, BACH['t'] + BACH['r'] + 2*BACH['th'], 'numpy')
_rng = np.random.default_rng(7); _tmax = 0.0
for _ in range(5):
    _jet = [2.0] + list(_rng.uniform(-0.5, 0.5, 10))
    _tmax = max(_tmax, abs(float(_trf(*_jet))))
print('trace numeric max on random jets', _tmax, flush=True)

RADII = [1.05, 1.5, 2.0, 5.0, 10.0, 100.0, 1000.0]
def run_member(p_rat, a_rat, label):
    out = {'background_B': {}}
    fa, fb = deriv_fns(p_rat, a_rat, None, 'numpy')
    for rv in RADII:
        out['background_B'][str(rv)] = [float(FACTOR*x) for x in B_at(fa, fb, Bf64, rv)]
    for which, key in (('b', 'delta_b'), ('P', 'delta_P')):
        fa, fb = deriv_fns(p_rat, a_rat, which, 'numpy')
        rows = {}; maxtr = 0.0; maxfd = 0.0
        for rv in RADII:
            d1 = FACTOR*(B_at(fa, fb, Bf64, rv, 1e-4) - B_at(fa, fb, Bf64, rv, -1e-4))/2e-4
            d2 = FACTOR*(B_at(fa, fb, Bf64, rv, 5e-5) - B_at(fa, fb, Bf64, rv, -5e-5))/1e-4
            rows[str(rv)] = [float(x) for x in d1]
            maxtr = max(maxtr, abs(float(d1[0] + d1[1] + 2*d1[2])))
            maxfd = max(maxfd, float(np.max(np.abs(d1-d2)/np.maximum(1.0, np.abs(d1)))))
        out[key] = {'deltaB_diag_t_r_th': rows, 'max_abs_trace_deltaB_float64': maxtr,
                    'max_eps_halving_rel_disagreement': maxfd}
        print(label, key, 'max|trace| float64', maxtr, flush=True)
    return out

res = {'combo_selection': sel, 'selected_combo': BEST,
       'normalisation_factor_closed_over_mine': FACTOR,
       'schwarzschild_max_abs_B_raw': schw_max,
       'trace_numeric_max_random_jets': _tmax}
res['TB'] = run_member(sp.Rational(1, 2), sp.Integer(0), 'TB')
mx = 0.0
for rv in RADII[:-1]:
    got = np.array(res['TB']['background_B'][str(rv)]); ex = closed_tb(rv)
    mx = max(mx, float(np.max(np.abs(got-ex)/np.abs(ex))))
res['TB_control_max_rel_err_vs_closed'] = mx
print('TB control max rel err', mx, flush=True)
res['JM'] = run_member(sp.Rational(1, 10), sp.Rational(277734, 10**6), 'JM')

# ---- 40-digit mpmath probes on the member ----
def derivs_mp(p_rat, a_rat, which, rv, eps):
    fa, fb = deriv_fns(p_rat, a_rat, which, 'mpmath')
    return [f(mpf(rv), mpf(eps)) for f in fa], [f(mpf(rv), mpf(eps)) for f in fb]
probes = {}
for rvs in ('1.05', '1.5', '2', '10', '100', '1000'):
    row = {}
    av, bv = derivs_mp(sp.Rational(1, 10), sp.Rational(277734, 10**6), None, rvs, 0)
    bg = {k: FACTOR*Bfmp[k](mpf(rvs), *av, *bv) for k in ('t', 'r', 'th')}
    row['background_B'] = {k: mp.nstr(v, 25) for k, v in bg.items()}
    for which, key in (('b', 'delta_b'), ('P', 'delta_P')):
        eps = mpf('1e-6')
        avp, bvp = derivs_mp(sp.Rational(1, 10), sp.Rational(277734, 10**6), which, rvs, eps)
        avm, bvm = derivs_mp(sp.Rational(1, 10), sp.Rational(277734, 10**6), which, rvs, -eps)
        d = {k: FACTOR*(Bfmp[k](mpf(rvs), *avp, *bvp) - Bfmp[k](mpf(rvs), *avm, *bvm))/(2*eps)
             for k in ('t', 'r', 'th')}
        row[key] = {k: mp.nstr(v, 25) for k, v in d.items()}
        row[key + '_trace'] = mp.nstr(d['t'] + d['r'] + 2*d['th'], 10)
    probes[rvs] = row
    print(rvs, 'tr_b', row['delta_b_trace'], 'tr_P', row['delta_P_trace'], flush=True)
res['mp40_probes'] = probes
json.dump(res, open(os.path.join(GATE, 'results', 'wc_static.json'), 'w'), indent=1)
print('WROTE wc_static.json', flush=True)
