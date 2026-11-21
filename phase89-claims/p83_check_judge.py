#!/usr/bin/env python3
"""
p83_check_judge.py - P8-3 follow-ups for the solved config-A slice:
 (a) GRID-INDEPENDENCE CHECK: re-evaluate the config-A fields (from
     their basis coefficients, M=6 K=10) on a FINER grid (Ns=121,
     Np=48) with the gamma-system components and report the residual
     RMS on the same sample s in [1,14.5] - guards against the solve
     merely fitting its own FD grid.
 (b) JUDGE: corrected metric (alpha0+dalpha, beta, gamma) + axial
     shift g_tz = -S*0.02 (S = cos window on [10,15], p75 pattern),
     audited with the P6-4b sampling judge (verify_metric.
     einstein_at_points); inner-equator NEC at h in {0.3, 0.15}
     (0.075 added for convergence). Fields tapered to 0 on s in
     [15,18] outside the tube, as in p75.
float64. System python3: numpy 2.2.6 / scipy 1.14.1.
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
from numpy.polynomial import chebyshev as Cb
from scipy.interpolate import CubicSpline

HERE = Path(__file__).resolve().parent
P7 = HERE.parent / 'phase7'
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / 'phase6'))
sys.path.insert(0, str(P7))
import shell as sh              # noqa: E402
import verify_metric as vm      # noqa: E402
from p75_solve import build_prescription, derivs, R_MAJ, S_T, EIGHT_PI  # noqa: E402
import p75_Gg as Gg  # noqa: E402

DTYPE = np.float64
OUT = HERE / 'results'
COMPS = ['tt', 'ss', 'thth', 'psipsi', 'sth']

FZ = np.load(OUT / 'p83_fields_A.npz')
COEF = FZ['coef']; M = int(FZ['M']); K = int(FZ['K'])


def basis_field(field, sv, tv):
    """Evaluate one field (0=dalpha,1=beta,2=gamma) from coefficients
    at arbitrary (s,phi) arrays (basis as in p83_solve.py)."""
    u = np.clip(sv, 0, S_T) / S_T
    z = 2 * u ** 2 - 1.0
    out = np.zeros_like(np.asarray(sv, dtype=DTYPE))
    idx = field * M * K
    for m in range(M):
        for kk in range(K):
            F = Cb.chebval(z, [0] * kk + [1]) * np.cos(m * tv) * u ** m
            if field in (0, 1):
                F = F * (1.0 - u ** 2)
            out = out + COEF[idx] * F
            idx += 1
    return out


def main():
    t0 = time.time()
    pres = build_prescription()
    rho_s = CubicSpline(pres['r'], pres['rho']); ps_s = CubicSpline(pres['r'], pres['ps'])
    pz_s = CubicSpline(pres['r'], pres['pz']); a0_s = CubicSpline(pres['r'], pres['alpha0'])
    dps_s = CubicSpline(pres['r'], pres['dps']); ap_s = CubicSpline(pres['r'], pres['aprime'])

    # ---------- (a) finer-grid residual check ----------
    Ns, Np = 121, 48
    s1d = np.linspace(0.0, S_T, Ns)
    phi1d = np.linspace(0.0, 2 * np.pi, Np, endpoint=False)
    SS, TT = np.meshgrid(s1d, phi1d, indexing='ij')
    sc = np.clip(SS, 0, S_T)
    rho = rho_s(sc); ps = ps_s(sc); pz = pz_s(sc)
    Kk = np.cos(TT) / (R_MAJ + SS * np.cos(TT))
    pphi = ps + SS * (dps_s(sc) + (rho + ps) * ap_s(sc) + Kk * (ps - pz))
    pphi = np.where(SS > 0, pphi, ps)
    Tstar = {'tt': -rho, 'ss': ps, 'thth': pphi, 'psipsi': pz}
    A = a0_s(sc) + basis_field(0, SS, TT)
    B = basis_field(1, SS, TT)
    Gm = basis_field(2, SS, TT)
    ds = float(s1d[1] - s1d[0])
    As, Ass, At, Att, Ast = derivs(A, ds, Np)
    Bs, Bss, Bt, Btt, Bst = derivs(B, ds, Np)
    Gs, Gss, Gt, Gtt, Gst = derivs(Gm, ds, Np)
    args = (SS, TT, R_MAJ, A, B, Gm, As, At, Ass, Ast, Att,
            Bs, Bt, Bss, Bst, Btt, Gs, Gt, Gss, Gst, Gtt)
    E = {'tt': Gg.Gtt(*args), 'ss': Gg.Gss(*args), 'thth': Gg.Gthth(*args),
         'psipsi': Gg.Gpsipsi(*args)}
    sth_orth = Gg.Gsth(*args) / np.maximum(SS, 1e-9)
    R = {'tt': E['tt'] - EIGHT_PI * Tstar['tt'], 'ss': E['ss'] - EIGHT_PI * Tstar['ss'],
         'thth': E['thth'] - EIGHT_PI * Tstar['thth'],
         'psipsi': E['psipsi'] - EIGHT_PI * Tstar['psipsi'], 'sth': sth_orth}
    sample = (s1d >= 1.0 - 1e-9) & (s1d <= 14.5 + 1e-9)
    v = np.concatenate([R[c][sample].ravel() for c in COMPS])
    check = {'grid': [Ns, Np], 'rms': float(np.sqrt(np.mean(v ** 2))),
             'max': float(np.max(np.abs(v))),
             'per_comp': {c: float(np.sqrt(np.mean(R[c][sample] ** 2))) for c in COMPS}}
    print('finer-grid check:', check, flush=True)
    # base (uncorrected) on the same finer grid, for the ratio
    E0 = None
    A0g = a0_s(sc) * np.ones_like(SS); Zg = np.zeros_like(SS)
    As, Ass, At, Att, Ast = derivs(A0g, ds, Np)
    Bs, Bss, Bt, Btt, Bst = derivs(Zg, ds, Np)
    Gs, Gss, Gt, Gtt, Gst = derivs(Zg, ds, Np)
    args0 = (SS, TT, R_MAJ, A0g, Zg, Zg, As, At, Ass, Ast, Att,
             Bs, Bt, Bss, Bst, Btt, Gs, Gt, Gss, Gst, Gtt)
    E0 = {'tt': Gg.Gtt(*args0), 'ss': Gg.Gss(*args0), 'thth': Gg.Gthth(*args0),
          'psipsi': Gg.Gpsipsi(*args0)}
    sth0 = Gg.Gsth(*args0) / np.maximum(SS, 1e-9)
    R0 = {'tt': E0['tt'] - EIGHT_PI * Tstar['tt'], 'ss': E0['ss'] - EIGHT_PI * Tstar['ss'],
          'thth': E0['thth'] - EIGHT_PI * Tstar['thth'],
          'psipsi': E0['psipsi'] - EIGHT_PI * Tstar['psipsi'], 'sth': sth0}
    v0 = np.concatenate([R0[c][sample].ravel() for c in COMPS])
    check['base_rms_same_grid'] = float(np.sqrt(np.mean(v0 ** 2)))
    check['reduction_factor_same_grid'] = float(check['base_rms_same_grid'] / check['rms'])
    print('base on finer grid:', check['base_rms_same_grid'],
          'reduction:', check['reduction_factor_same_grid'], flush=True)

    # ---------- (b) judge ----------
    def taper(sv):
        uu = np.clip((np.asarray(sv, dtype=DTYPE) - S_T) / 3.0, 0.0, 1.0)
        return 1.0 - uu ** 2 * (3 - 2 * uu)

    def make_gfunc(beta_shift):
        def gfunc(pts):
            pts = np.asarray(pts, dtype=DTYPE)
            x_, y_, z_ = pts[:, 0], pts[:, 1], pts[:, 2]
            Rcyl = np.sqrt(x_ ** 2 + y_ ** 2)
            sv = np.sqrt((Rcyl - R_MAJ) ** 2 + z_ ** 2)
            tv = np.arctan2(z_, Rcyl - R_MAJ)
            scc = np.clip(sv, 0.0, S_T)
            tp = taper(sv)
            av = a0_s(scc) + tp * basis_field(0, sv, tv)
            bv = tp * basis_field(1, sv, tv)
            gv = tp * basis_field(2, sv, tv)
            Ssh = sh.shift_S(sv, 0.0, S_T, 'cos', 1.0, [10.0, 15.0])
            Rsafe = np.maximum(Rcyl, 1e-12)
            psihat = np.stack([np.where(Rcyl > 1e-12, -y_ / Rsafe, 0.0),
                               np.where(Rcyl > 1e-12, x_ / Rsafe, 0.0),
                               np.zeros_like(x_)], axis=1)
            P = pts.shape[0]
            g = np.zeros((P, 4, 4), dtype=DTYPE)
            eb = np.exp(2 * bv); eg = np.exp(2 * gv)
            for i in range(3):
                for j in range(3):
                    g[:, 1 + i, 1 + j] = eb * ((1.0 if i == j else 0.0)
                                               - psihat[:, i] * psihat[:, j]) \
                        + eg * psihat[:, i] * psihat[:, j]
            g[:, 0, 0] = -np.exp(2 * av)
            g[:, 0, 3] = g[:, 3, 0] = -Ssh * beta_shift
            return g
        return gfunc

    def judge(beta_shift, h):
        s_vals = np.concatenate([np.linspace(3.0, 9.0, 7), np.linspace(9.5, 14.5, 11)])
        phi_vals = np.concatenate([np.linspace(-0.2, 0.2, 9) + np.pi,
                                   np.linspace(-0.2, 0.2, 5),
                                   np.linspace(0.4, 2 * np.pi - 0.4, 13)])
        phi_vals = np.mod(phi_vals, 2 * np.pi)
        pts, tags = [], []
        for sv in s_vals:
            for pv in phi_vals:
                for t_ in (0.0, np.pi / 2):
                    Rc = R_MAJ + sv * np.cos(pv)
                    pts.append([Rc * np.cos(t_), Rc * np.sin(t_), sv * np.sin(pv)])
                    tags.append((sv, pv))
        pts = np.array(pts, dtype=DTYPE)
        _, _, m = vm.einstein_at_points(make_gfunc(beta_shift), pts, h=h)
        tags = np.array(tags)
        inner = np.abs(tags[:, 1] - np.pi) < 0.21
        return {'beta_shift': beta_shift, 'h': h, 'n_points': int(len(pts)),
                'inner_eq_nec_min': float(np.min(m['nec'][inner])),
                'inner_eq_typeI_frac': float(np.mean(m['typeI'][inner])),
                'all_nec_min': float(np.min(m['nec']))}

    judge_out = {}
    for bs in (0.0, 0.02):
        for h in (0.3, 0.15, 0.075):
            judge_out[f'b{bs}_h{h}'] = judge(bs, h)
            print('judge', bs, h, judge_out[f'b{bs}_h{h}'], flush=True)

    out = {'item': 'P8-3 solved-slice finer-grid check + sampling judge',
           'environment': 'system python3, numpy 2.2.6, scipy 1.14.1; float64',
           'finer_grid_check': check,
           'judge_solved_metric': judge_out,
           'note': ('judge metric: ds2 = -e^{2a}dt2 + e^{2b}(ds2+s2 dphi2) + '
                    'e^{2g}(R+s cosphi)2 dpsi2 with config-A fields, tapered '
                    'outside s=15; axial shift g_tz=-S*beta_shift, S cos window '
                    '[10,15] (p75 pattern)'),
           'runtime_s': time.time() - t0}
    (OUT / 'p83_check_judge.json').write_text(json.dumps(out, indent=1))
    print('wrote results/p83_check_judge.json')


if __name__ == '__main__':
    main()
