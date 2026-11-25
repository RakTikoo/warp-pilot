"""P72-1 independent second path:
- throat system solved by fsolve directly on G-2T residuals (no analytic solve);
- mu=0 floor by direct parametrised scan;
- extension by fixed-step RK4 (different method/step from DOP853 main path);
- part (i) analytic cross-checks (NEC1 throat, spinor at infinity).
Writes results/p721_second_path.json."""
import numpy as np, json
from scipy.optimize import fsolve
import sys
sys.path.insert(0, 'work')
from p721_main import Gcomps, Tdirac, dirac_rhs, F1_shape_scalar

out = {'throat_fsolve': {}, 'mu0_floor': {}, 'extension_rk4': {}, 'part_i_cross': {}}

def throat_res(x, beta, mu, F10):
    P0, Q0, w = x
    Pd0, Qd0 = dirac_rhs(0.0, [P0, Q0], 'ellis' if F10 == 1.0 else 'sqrt', w, mu)
    Gtt, Gll, Gth = Gcomps(0.0, 1.0, F10, 0.0, 0.0, 0.0)
    Tt, Tl, Tth = Tdirac(P0, Q0, Pd0, Qd0, 1.0, F10, 1.0, w)
    return [Gtt - 2 * Tt, Gll - 2 * Tl, Gth - 2 * Tth]

main = json.load(open('results/p721_results.json'))
for shape, beta, F10 in [('ellis', -1.0, 1.0), ('sqrt', 0.5, 2.0)]:
    for mu in [0.2, 1.0]:
        e = main['part_ii'][f'{shape}_mu{mu}']
        x0 = [e['P0'], e['Q0'], e['w']]
        # start fsolve from a perturbed point to be a genuine second solve
        xs, info, ier, msg = fsolve(throat_res, [x0[0] * 1.3 + 0.05, x0[1] * 0.7 - 0.04, x0[2] * 1.5 + 0.02],
                                    args=(beta, mu, F10), full_output=True)
        res = throat_res(xs, beta, mu, F10)
        out['throat_fsolve'][f'{shape}_mu{mu}'] = dict(
            datum=[float(v) for v in xs], max_resid=float(np.max(np.abs(res))),
            diff_vs_main=float(np.max(np.abs(np.array(xs) - np.array(x0)))), ier=int(ier))
    # mu = 0 floor: parametrise by S>=|D|, sign of PQ; A and C hold exactly, read EqB residual (Gll-2Tl)
    D = (beta - 1) / 8.0
    best = 1e9
    for S in np.linspace(abs(D) + 1e-6, 5.0, 400):
        for sgn in [1, -1]:
            P0sq = (S + D) / 2; Q0sq = (S - D) / 2
            if P0sq < 0 or Q0sq < 0: continue
            P0 = np.sqrt(P0sq); Q0 = sgn * np.sqrt(Q0sq)
            w = beta / (8 * S) if S > 0 else 0.0
            r = throat_res([P0, Q0, w], beta, 0.0, F10)
            best = min(best, np.max(np.abs(r)))
    out['mu0_floor'][shape] = dict(min_max_resid_over_A_C_family=float(best), beta=beta)

# RK4 extension second path
def rk4_ext(shape, w, mu, P0, Q0, h=2e-4, lmax=3.0):
    n = int(lmax / h); lv = 0.0; y = np.array([P0, Q0])
    breach = None; blow = None; S0 = P0**2 + Q0**2
    prof = []
    for i in range(n + 1):
        R = np.sqrt(lv**2 + 1)
        Pd, Qd = dirac_rhs(lv, y, shape, w, mu)
        F1 = F1_shape_scalar(lv, shape)
        hh = 1e-6 * max(1.0, lv)
        F1d = (F1_shape_scalar(lv + hh, shape) - F1_shape_scalar(lv - hh, shape)) / (2 * hh) if lv > 0 else 0.0
        Gtt, Gll, Gth = Gcomps(lv, 1.0, F1, 0.0, F1d, 0.0)
        Tt, Tl, Tth = Tdirac(y[0], y[1], Pd, Qd, 1.0, F1, R, w)
        scale = max(abs(Gtt), abs(Gll), abs(Gth), abs(2 * Tt), abs(2 * Tl), abs(2 * Tth), 1e-12)
        rel = max(abs(Gtt - 2 * Tt), abs(Gll - 2 * Tl), abs(Gth - 2 * Tth)) / scale
        if breach is None and rel > 0.02: breach = float(R)
        if blow is None and (y[0]**2 + y[1]**2) > 1e6 * S0: blow = float(R)
        if i == n: break
        k1 = np.array(dirac_rhs(lv, y, shape, w, mu))
        k2 = np.array(dirac_rhs(lv + h / 2, y + h * k1 / 2, shape, w, mu))
        k3 = np.array(dirac_rhs(lv + h / 2, y + h * k2 / 2, shape, w, mu))
        k4 = np.array(dirac_rhs(lv + h, y + h * k3, shape, w, mu))
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; lv += h
        if not np.all(np.isfinite(y)): 
            if blow is None: blow = float(np.sqrt(lv**2 + 1))
            break
    return breach, blow

for shape in ['ellis', 'sqrt']:
    for mu in [0.2, 1.0]:
        e = main['part_ii'][f'{shape}_mu{mu}']
        b, bl = rk4_ext(shape, e['w'], mu, e['P0'], e['Q0'])
        out['extension_rk4'][f'{shape}_mu{mu}'] = dict(breach_R=b, blowup_R=bl,
            main_breach_R=e['domain_breach_R_over_r0'], main_blowup_R=e['spinor_blowup_R_over_r0'])

for Qe in [0.25, 0.5, 0.75, 0.9]:
    e = main['part_i'][f'Qe_{Qe}']
    out['part_i_cross'][f'Qe_{Qe}'] = dict(
        NEC1_throat_analytic=float((Qe**2 - 1) / (8 * np.pi)),
        NEC1_min_numeric=float(e['NEC1_min_fine']),
        spinor_inf_analytic=float(1 / (8 * (Qe**2 + 1))),
        spinor_inf_numeric_Q=float(e['spinor_at_infinity_Q']))

json.dump(out, open('results/p721_second_path.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
