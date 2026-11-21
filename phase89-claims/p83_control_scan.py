#!/usr/bin/env python3
"""
p83_control_scan.py - P8-3 parts (1) CONTROL and (3) GELFAND BRANCH SCAN.

(1) CONTROL: rebuild the P6-4a filled slice prescription exactly as
    Phase 7 did (p75_solve.build_prescription) and recompute the base
    realisation residual (alpha=alpha0(s), beta=0, gamma=0) on the
    Phase-7 grid/sample: Ns=61, Np=32, sample s in [1, 14.5], 5
    components (tt, ss, thth, psipsi, sth_orth). Stored Phase-7
    control: RMS 2.9880108962577947e-3, max 6.807017349082338e-3.

(3) BRANCH SCAN: fixed-psi radial shooting test of P7-5. The (t,t)
    equation for phi-independent beta(s) is
        beta'' + beta'/s = -8 pi rho*(s) e^{2 beta},
        beta'(0) = 0, beta(0) = b0 in [0,1];
    record beta(15); obstruction iff max over b0 of beta(15) < 0.
    Primary path: rho_c scaled by lam in {1, 1/2, 1/4, 1/10} at
    s_t = 15 (Gelfand parameter lam * rho_c * s_t^2).
    Secondary path (optional, also run): s_t in {10, 7.5} at fixed
    rho_c, with the density shape rescaled to the smaller tube
    (plateau on [0, 0.6 s_t], Cinf taper to 0 at s_t, same rho_c);
    record max beta(s_t). Labelled as a rescaled-prescription path.

float64. System python3: numpy 2.2.6 / scipy 1.14.1.
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
P7 = HERE.parent / 'phase7'
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / 'phase6'))
sys.path.insert(0, str(P7))
from p75_solve import build_prescription, einstein_grid, R_MAJ, S_T, EIGHT_PI  # noqa: E402
import p64_torus as p64  # noqa: E402

DTYPE = np.float64
OUT = HERE / 'results'
OUT.mkdir(exist_ok=True)


def control():
    pres = build_prescription()
    rho_s = CubicSpline(pres['r'], pres['rho']); ps_s = CubicSpline(pres['r'], pres['ps'])
    pz_s = CubicSpline(pres['r'], pres['pz']); a0_s = CubicSpline(pres['r'], pres['alpha0'])
    dps_s = CubicSpline(pres['r'], pres['dps']); ap_s = CubicSpline(pres['r'], pres['aprime'])
    Ns, Np = 61, 32
    s1d = np.linspace(0.0, S_T, Ns)
    phi1d = np.linspace(0.0, 2 * np.pi, Np, endpoint=False)
    SS, TT = np.meshgrid(s1d, phi1d, indexing='ij')
    sc = np.clip(SS, 0, S_T)
    rho = rho_s(sc); ps = ps_s(sc); pz = pz_s(sc)
    K = np.cos(TT) / (R_MAJ + SS * np.cos(TT))
    pphi = ps + SS * (dps_s(sc) + (rho + ps) * ap_s(sc) + K * (ps - pz))
    pphi = np.where(SS > 0, pphi, ps)
    Tstar = {'tt': -rho, 'ss': ps, 'thth': pphi, 'psipsi': pz}
    A0 = a0_s(sc) * np.ones_like(SS)
    B0 = np.zeros_like(SS)
    E = einstein_grid(A0, B0, s1d, phi1d)
    R = {'tt': E['tt'] - EIGHT_PI * Tstar['tt'], 'ss': E['ss'] - EIGHT_PI * Tstar['ss'],
         'thth': E['thth'] - EIGHT_PI * Tstar['thth'],
         'psipsi': E['psipsi'] - EIGHT_PI * Tstar['psipsi'], 'sth': E['sth_orth']}
    sample = (s1d >= 1.0 - 1e-9) & (s1d <= 14.5 + 1e-9)
    comps = ['tt', 'ss', 'thth', 'psipsi', 'sth']
    v = np.concatenate([R[c][sample].ravel() for c in comps])
    per = {c: {'rms': float(np.sqrt(np.mean(R[c][sample] ** 2))),
               'max': float(np.max(np.abs(R[c][sample])))} for c in comps}
    return {'sigma': pres['sigma'], 'rho_c': pres['rho_c'], 'shoot_F': pres['shoot_F'],
            'rms': float(np.sqrt(np.mean(v ** 2))), 'max': float(np.max(np.abs(v))),
            'per_comp': per,
            'stored_phase7': {'rms': 0.0029880108962577947, 'max': 0.006807017349082338}}


def shoot_beta15(rho_fun, s_end, b0_grid):
    """Integrate beta'' + beta'/s = -8 pi rho(s) e^{2 beta}, beta'(0)=0."""
    out = []
    for b0 in b0_grid:
        def rhs(s, y):
            b, bp = y
            src = -EIGHT_PI * float(rho_fun(np.clip(s, 0, None))) * np.exp(2 * b)
            if s < 1e-8:
                bpp = 0.5 * src
            else:
                bpp = src - bp / s
            return [bp, bpp]
        sol = solve_ivp(rhs, (1e-9, s_end), [b0, 0.0], method='DOP853',
                        rtol=1e-11, atol=1e-13, dense_output=False)
        out.append(float(sol.y[0, -1]) if sol.success else np.nan)
    return np.array(out)


def main():
    t0 = time.time()
    ctl = control()
    print('CONTROL rms %.6e max %.6e (stored %.6e / %.6e) sigma %.4f rho_c %.4e'
          % (ctl['rms'], ctl['max'], ctl['stored_phase7']['rms'],
             ctl['stored_phase7']['max'], ctl['sigma'], ctl['rho_c']), flush=True)

    pres = build_prescription()
    rho_s = CubicSpline(pres['r'], pres['rho'])
    rho_c = pres['rho_c']
    b0_grid = np.linspace(0.0, 1.0, 101)

    # ---- primary path: reduce rho_c at s_t = 15 ----
    primary = []
    for lam in (1.0, 0.5, 0.25, 0.1):
        rf = lambda s, lam=lam: lam * float(rho_s(np.clip(s, 0, S_T)))
        b15 = shoot_beta15(rf, S_T, b0_grid)
        i = int(np.nanargmax(b15))
        # refine b0 near the max
        lo = b0_grid[max(i - 1, 0)]; hi = b0_grid[min(i + 1, len(b0_grid) - 1)]
        fine = np.linspace(lo, hi, 41)
        b15f = shoot_beta15(rf, S_T, fine)
        j = int(np.nanargmax(b15f))
        primary.append({'lam_rho_c_s_t2': lam,
                        'gelfand_param_rho_c_times_st2': lam * rho_c * S_T ** 2,
                        'max_beta15': float(b15f[j]), 'b0_at_max': float(fine[j]),
                        'beta15_at_b0_0': float(b15[0]), 'beta15_at_b0_1': float(b15[-1]),
                        'curve_b0': b0_grid.tolist(), 'curve_beta15': b15.tolist()})
        print('primary lam=%.3g max beta(15)=%.5f at b0=%.3f' % (lam, b15f[j], fine[j]),
              flush=True)

    # ---- secondary path: smaller tube at fixed rho_c, rescaled shape ----
    _cinf = p64._cinf
    secondary = []
    for st in (10.0, 7.5):
        def wfun(s, st=st):
            return 1.0 - _cinf((np.asarray(s, dtype=DTYPE) - 0.6 * st) / (0.4 * st))
        sg = np.linspace(0.0, st, 2001)
        rf_s = CubicSpline(sg, rho_c * wfun(sg))
        rf = lambda s: float(rf_s(np.clip(s, 0, st)))
        b15 = shoot_beta15(rf, st, b0_grid)
        i = int(np.nanargmax(b15))
        lo = b0_grid[max(i - 1, 0)]; hi = b0_grid[min(i + 1, len(b0_grid) - 1)]
        fine = np.linspace(lo, hi, 41)
        b15f = shoot_beta15(rf, st, fine)
        j = int(np.nanargmax(b15f))
        secondary.append({'s_t': st, 'lam_equiv_rho_c_s_t2': (st / S_T) ** 2,
                          'gelfand_param_rho_c_times_st2': rho_c * st ** 2,
                          'max_beta_at_st': float(b15f[j]), 'b0_at_max': float(fine[j]),
                          'beta_at_b0_0': float(b15[0]), 'beta_at_b0_1': float(b15[-1]),
                          'curve_b0': b0_grid.tolist(), 'curve_beta': b15.tolist()})
        print('secondary s_t=%.1f max beta(s_t)=%.5f at b0=%.3f'
              % (st, b15f[j], fine[j]), flush=True)

    out = {'item': 'P8-3 control + Gelfand branch scan',
           'environment': 'system python3, numpy 2.2.6, scipy 1.14.1; float64',
           'control': ctl,
           'branch_scan_primary_rho_c_path': primary,
           'branch_scan_secondary_s_t_path': secondary,
           'runtime_s': time.time() - t0}
    (OUT / 'p83_control_scan.json').write_text(json.dumps(out, indent=1))
    print('wrote results/p83_control_scan.json')


if __name__ == '__main__':
    main()
