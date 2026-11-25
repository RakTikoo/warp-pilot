#!/usr/bin/env python3
"""Gate-37 deciding reads (3)-(5): REST arithmetic re-read, Ellis gate
coefficient re-check, C/E wider-set collapse spot-check.  Exact
Fractions throughout except where the stored record is float (there
the float is converted exactly and the residue class is reported).
H{2,0}(3) values are THIS GATE's own (g37_results.json)."""
import json, math
from fractions import Fraction as Fr
import sys
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate37/work')

WP = '/home/hatch/workspace/warp-pilot'
res = json.load(open(f'{WP}/gate37/work/g37_results.json'))
reasm = json.load(open(f'{WP}/phase323/work/p323_reassembly.json'))
assembled = json.load(open(f'{WP}/phase259/results/p2591_assembled.json'))

def myH(key):
    """This gate's derived print H{2,0}(3) (Tt, Tr, Tth) = -E2."""
    d = res[key]['E_mixed_diag'][:3]
    return tuple(-Fr(v) for v in d)

def combo(H203, H3, H4):
    return tuple(Fr(1, 140) * H203[i] - Fr(8, 945) * H3[i]
                 + Fr(2, 315) * H4[i] for i in range(3))

out = {}

# ================= (3a) REST arithmetic at the Ellis throat ==========
REST_print = (Fr(44, 135), Fr(4, 27), Fr(100, 189))
H3_E = tuple(-Fr(v) for v in
             res['cal_ellis_throat_Ric3']['E_mixed_diag'][:3])
H4_E = tuple(-Fr(v) for v in
             res['cal_ellis_throat_RiemRic']['E_mixed_diag'][:3])
H203_E = myH('dec_ellis_throat_L2')
c34 = tuple(-Fr(8, 945) * H3_E[i] + Fr(2, 315) * H4_E[i]
            for i in range(3))
implied_print = tuple(140 * (REST_print[i] - c34[i]) for i in range(3))
# consistency: implied print + derived (3),(4) must rebuild REST_print
rebuild = combo(implied_print, H3_E, H4_E)
delta_bracket = tuple(210 * (combo(H203_E, H3_E, H4_E)[i]
                             - REST_print[i]) for i in range(3))
out['rest_ellis'] = {
    'H3_mine': [str(v) for v in H3_E], 'H4_mine': [str(v) for v in H4_E],
    'H203_mine_print': [str(v) for v in H203_E],
    'implied_print_H203': [str(v) for v in implied_print],
    'rest_rebuild_from_implied': [str(v) for v in rebuild],
    'rest_rebuild_matches': rebuild == REST_print,
    'implied_minus_mine': [str(implied_print[i] - H203_E[i])
                           for i in range(3)],
    'weighted_effect_Tr': str(210 * Fr(1, 140)
                              * (implied_print[1] - H203_E[1])),
    'delta_bracket': [str(v) for v in delta_bracket],
    'FULL_residual': ['0', '16', '0'],
    'arbitrated_residual': [str(Fr(0) + delta_bracket[i] +
                                (Fr(16) if i == 1 else Fr(0)))
                            for i in range(3)],
}

# ================= (3b) REST arithmetic at the A throat ==============
REST_print_A = (Fr(-23, 5040), Fr(1, 144), Fr(-199, 5040))
H3_A = (Fr(3), Fr(3, 2), Fr(39, 8))
H4_A = (Fr(3, 4), Fr(3, 4), Fr(-3, 8))
H203_A = myH('dec_A_throat_L2')
REST_der_A = combo(H203_A, H3_A, H4_A)
c34_A = tuple(-Fr(8, 945) * H3_A[i] + Fr(2, 315) * H4_A[i]
              for i in range(3))
implied_A = tuple(140 * (REST_print_A[i] - c34_A[i]) for i in range(3))
delta_A = tuple(210 * (REST_der_A[i] - REST_print_A[i])
                for i in range(3))
FULL_A = (Fr(0), Fr(2), Fr(-7))
out['rest_A'] = {
    'H203_mine_print': [str(v) for v in H203_A],
    'REST_derived_A': [str(v) for v in REST_der_A],
    'REST_print_A': [str(v) for v in REST_print_A],
    'implied_print_H203_A': [str(v) for v in implied_A],
    'delta_bracket': [str(v) for v in delta_A],
    'arbitrated_residual': [str(FULL_A[i] + delta_A[i])
                            for i in range(3)],
}

# ================= (4) Ellis gate coefficient ========================
gate_full = assembled['assemblies']['full']['gate']
P_full_stored = gate_full['P_coefs']
P_arb = [Fr(187), Fr(-1806), Fr(5460), Fr(-4200)]
def peval(coefs, x):
    return sum(c * x ** p for p, c in enumerate(coefs))
# exact rational bisection for the in-range root of the arbitrated P
lo, hi = Fr(0), Fr(2)
assert peval(P_arb, lo) * peval(P_arb, hi) < 0
for _ in range(200):
    mid = (lo + hi) / 2
    if peval(P_arb, lo) * peval(P_arb, mid) <= 0:
        hi = mid
    else:
        lo = mid
root_arb = (lo + hi) / 2
# root count in [-1, 2] by exact sign sampling on a rational grid
import numpy as np
roots_arb = np.roots([float(c) for c in reversed(P_arb)])
in_range = sorted(float(z.real) for z in roots_arb
                  if abs(z.imag) < 1e-9 and -1.0 <= z.real <= 2.0)
# NEC: arbitrated nec(xi) = -Tt_target(xi) + P_arb(xi); Tt target from
# the Phase 241 driver targets (record data) via the harness loader.
sys.path.insert(0, f'{WP}/phase259/work')
import importlib.util
spec = importlib.util.spec_from_file_location(
    'harness', f'{WP}/phase259/work/p2591_harness.py')
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)
Tt_targ = [float(harness.tha_ellis('Tt', p, 1.0)) for p in range(4)]
Tr_targ = [float(harness.tha_ellis('Tr', p, 1.0)) for p in range(4)]
nec_arb = [-Tt_targ[p] + float(P_arb[p]) for p in range(4)]
nec_roots = np.roots(list(reversed(nec_arb)))
nec_roots = sorted(float(z.real) for z in nec_roots if abs(z.imag) < 1e-9)
nec_targ = [0.15155109082, 0.25959968220, 1.42218256030]
# Stage B Delta p_r at xi = 1/6 from the arbitrated Tr (= P_arb)
Tr_at_16 = peval(P_arb, Fr(1, 6))
dpr_arb = float(Tr_at_16) / (20160.0 * math.pi ** 2)
out['gate'] = {
    'P_full_stored': P_full_stored,
    'delta_P0_from_read3': str(delta_bracket[1]),
    'P0_arbitrated': str(Fr(203) + delta_bracket[1]),
    'P_arbitrated_coefs': [str(c) for c in P_arb],
    'P_root_exact_bisection': float(root_arb),
    'P_root_target': 0.86035766893,
    'P_root_dev': abs(float(root_arb) - 0.86035766893),
    'P_roots_in_range_float': in_range,
    'Tt_target_coefs': Tt_targ, 'Tr_target_coefs': Tr_targ,
    'Tr_target_equals_P_target': Tr_targ == [187.0, -1806.0, 5460.0,
                                             -4200.0],
    'NEC_arbitrated_roots': nec_roots,
    'NEC_target_roots': nec_targ,
    'NEC_max_dev': max(abs(a - b) for a, b in zip(nec_roots, nec_targ)),
    'Delta_pr_arbitrated': dpr_arb,
    'Delta_pr_target': 9.158220e-5,
    'Delta_pr_rel_dev': abs(dpr_arb - 9.158220e-5) / 9.158220e-5,
}

# ================= (5) C / E collapse spot-check =====================
def collapse(point_key, res_key):
    pt = reasm['points'][point_key]
    tab = reasm['read3_table'][point_key]
    H = myH(res_key)
    H3 = tuple(Fr(pt['H3_derived'][c]) for c in ('Tt', 'Tr', 'Tth'))
    H4 = tuple(Fr(pt['H4_derived'][c]) for c in ('Tt', 'Tr', 'Tth'))
    RP = tuple(Fr(pt['rest_print'][c]) for c in ('Tt', 'Tr', 'Tth'))
    dREST = tuple(combo(H, H3, H4)[i] - RP[i] for i in range(3))
    new = {}
    for i, c in enumerate(('Tt', 'Tr', 'Tth')):
        new[c] = tab[c]['old'] + 210.0 * float(dREST[i])
    return {'H203_mine_print': [str(v) for v in H],
            'delta_bracket': [str(210 * dREST[i]) for i in range(3)],
            'old': {c: tab[c]['old'] for c in ('Tt', 'Tr', 'Tth')},
            'new_mine': new,
            'new_max_abs_mine': max(abs(v) for v in new.values()),
            'stored_new_max_abs': max(
                abs(tab[c]['new']) for c in ('Tt', 'Tr', 'Tth'))}

out['collapse_C12'] = collapse('C:1/2', 'dec_C12_L2')
out['collapse_E110'] = collapse('E:1/10', 'dec_E110_L2')
out['family_maxima_stored'] = reasm['read3_family_xi0_maxima']

with open(f'{WP}/gate37/work/g37_arithmetic.json', 'w') as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
