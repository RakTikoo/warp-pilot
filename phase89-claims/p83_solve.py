#!/usr/bin/env python3
"""
p83_solve.py - P8-3 part (2): gamma-extended Gauss-Newton solve of the
toroidal realisation system, pushing past Phase 7's 8.4x (RMS 3.54e-4,
45 dof / 14 iterations, no surface BC on beta) to the Phase-8 bar
RMS <= 2.99e-4 (>=10x vs base 2.99e-3) WITH the gamma-system BCs
enforced by basis construction:

BC SET (stated explicitly; matches P7-5's gamma-system):
 - centre s=0: alpha, beta, gamma phi-independent at s=0 and mode-m
   Fourier amplitude O(s^m) (basis factor u^m, u=s/15); d_s = 0 at
   s=0 for the m=0 (phi-independent) part (radial basis even in s:
   polynomials in u^2 times u^m).
 - surface s=15: beta(15,phi) = 0 exactly (basis factor (1-u^2));
   alpha continuous in the flat-exterior gauge, i.e. the correction
   dalpha(15,phi) = 0 (same factor; alpha0(15)=0 already);
   p_s(15,phi) = 0 is prescription-side (P6-4a slice: p_s(15)=0 by
   the sigma-shooting construction); gamma finite on the domain
   (no surface constraint on gamma - exterior matching stated, not
   solved, as in P7-5).
Unknowns: dalpha, beta, gamma in basis cos(m phi), m=0..M-1, times
radial T_k(2u^2-1), k=0..K-1, times u^m. Equations: the 5 gamma-system
components (p75_Gg.py) minus 8 pi T* on the Phase-7 sample
(s in [1,14.5], Ns x Np grid), RMS over all 5 components - the same
residual measure as the control / Phase 7.

Solver: damped Gauss-Newton (Levenberg), forward-FD Jacobian
(eps=1e-3), adaptive damping (lam x//= on success/failure), step cap
on max field change, backtracking scales. Config via argv:
  python3 p83_solve.py TAG M K NS NP MAXITER [WARMSTART_NPZ]
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
from p75_solve import build_prescription, derivs, R_MAJ, S_T, EIGHT_PI  # noqa: E402
import p75_Gg as Gg  # noqa: E402

DTYPE = np.float64
OUT = HERE / 'results'
OUT.mkdir(exist_ok=True)
COMPS = ['tt', 'ss', 'thth', 'psipsi', 'sth']


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else 'A'
    M = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    Ns = int(sys.argv[4]) if len(sys.argv) > 4 else 81
    Np = int(sys.argv[5]) if len(sys.argv) > 5 else 32
    MAXIT = int(sys.argv[6]) if len(sys.argv) > 6 else 50
    warm = sys.argv[7] if len(sys.argv) > 7 else None
    t0 = time.time()

    pres = build_prescription()
    rho_s = CubicSpline(pres['r'], pres['rho']); ps_s = CubicSpline(pres['r'], pres['ps'])
    pz_s = CubicSpline(pres['r'], pres['pz']); a0_s = CubicSpline(pres['r'], pres['alpha0'])
    dps_s = CubicSpline(pres['r'], pres['dps']); ap_s = CubicSpline(pres['r'], pres['aprime'])

    s1d = np.linspace(0.0, S_T, Ns)
    phi1d = np.linspace(0.0, 2 * np.pi, Np, endpoint=False)
    SS, TT = np.meshgrid(s1d, phi1d, indexing='ij')
    sc = np.clip(SS, 0, S_T)
    rho = rho_s(sc); ps = ps_s(sc); pz = pz_s(sc)
    Kk = np.cos(TT) / (R_MAJ + SS * np.cos(TT))
    pphi = ps + SS * (dps_s(sc) + (rho + ps) * ap_s(sc) + Kk * (ps - pz))
    pphi = np.where(SS > 0, pphi, ps)
    Tstar = {'tt': -rho, 'ss': ps, 'thth': pphi, 'psipsi': pz}
    sample = (s1d >= 1.0 - 1e-9) & (s1d <= 14.5 + 1e-9)

    def einstein_g(A, B, Gm):
        ds = float(s1d[1] - s1d[0])
        As, Ass, At, Att, Ast = derivs(A, ds, Np)
        Bs, Bss, Bt, Btt, Bst = derivs(B, ds, Np)
        Gs, Gss, Gt, Gtt, Gst = derivs(Gm, ds, Np)
        args = (SS, TT, R_MAJ, A, B, Gm, As, At, Ass, Ast, Att,
                Bs, Bt, Bss, Bst, Btt, Gs, Gt, Gss, Gst, Gtt)
        E = {'tt': Gg.Gtt(*args), 'ss': Gg.Gss(*args), 'thth': Gg.Gthth(*args),
             'psipsi': Gg.Gpsipsi(*args), 'sth_mixed': Gg.Gsth(*args)}
        E['sth_orth'] = E['sth_mixed'] / np.maximum(SS, 1e-9)
        return E

    def residual(A, B, Gm):
        E = einstein_g(A, B, Gm)
        return {'tt': E['tt'] - EIGHT_PI * Tstar['tt'],
                'ss': E['ss'] - EIGHT_PI * Tstar['ss'],
                'thth': E['thth'] - EIGHT_PI * Tstar['thth'],
                'psipsi': E['psipsi'] - EIGHT_PI * Tstar['psipsi'],
                'sth': E['sth_orth']}

    def vec(R):
        return np.concatenate([R[c][sample].ravel() for c in COMPS])

    def rms(v):
        return float(np.sqrt(np.mean(v ** 2)))

    # ---------- BC-enforcing basis ----------
    u = SS / S_T
    z = 2 * u ** 2 - 1.0
    cheb = [Cb.chebval(z, [0] * kk + [1]) for kk in range(K)]
    basis = []  # (field, array); field 0=dalpha, 1=beta, 2=gamma
    for field in range(3):
        for m in range(M):
            for kk in range(K):
                F = cheb[kk] * np.cos(m * TT) * u ** m
                if field in (0, 1):
                    F = F * (1.0 - u ** 2)
                basis.append((field, F))
    nb = len(basis)
    Bmat = np.array([F.ravel() for _, F in basis])  # nb x (Ns*Np)

    A0 = a0_s(sc) * np.ones_like(SS)
    Z = np.zeros_like(SS)

    def fields_from_coef(coef):
        d = (coef @ Bmat).reshape(3, Ns, Np) if False else None
        F = np.zeros((3, Ns, Np))
        idx = 0
        for field in range(3):
            acc = np.zeros_like(SS)
            for _ in range(M * K):
                acc = acc + coef[idx] * basis[idx][1]; idx += 1
            F[field] = acc
        return F[0], F[1], F[2]

    coef = np.zeros(nb)
    if warm:
        wz = np.load(warm)
        # project stored fields onto this basis by least squares on grid
        tgt = [wz['dalpha'].ravel(), wz['beta'].ravel(), wz['gamma'].ravel()]
        # NOTE: warm fields were on their own grid; require same grid
        for field in range(3):
            cols = [j for j, (f, _) in enumerate(basis) if f == field]
            sol, *_ = np.linalg.lstsq(Bmat[cols].T, tgt[field], rcond=None)
            coef[cols] = sol
        print('warm start projected from', warm, flush=True)

    dA, Bf, Gm = fields_from_coef(coef)
    A = A0 + dA
    v = vec(residual(A, Bf, Gm))
    cur = rms(v)
    traj = [{'iter': 0, 'rms': cur, 'max': float(np.max(np.abs(v)))}]
    print('config %s: M=%d K=%d dof=%d grid %dx%d start rms %.6e'
          % (tag, M, K, nb, Ns, Np, cur), flush=True)

    eps = 1e-3
    lam_rel = 1e-8
    stall = 0
    for it in range(MAXIT):
        J = np.empty((len(v), nb))
        for j in range(nb):
            cp = coef.copy(); cp[j] += eps
            dAj, Bj, Gj = fields_from_coef(cp)
            J[:, j] = (vec(residual(A0 + dAj, Bj, Gj)) - v) / eps
        base_lam = lam_rel * float(np.mean(np.sum(J ** 2, axis=0)))
        accepted = False
        for lam_mult in (1.0, 10.0, 100.0, 1000.0):
            lam = base_lam * lam_mult
            step, *_ = np.linalg.lstsq(
                np.vstack([J, np.sqrt(lam) * np.eye(nb)]),
                np.concatenate([-v, np.zeros(nb)]), rcond=None)
            for scale in (1.0, 0.5, 0.25):
                cn = coef + scale * step
                dAn, Bn, Gn = fields_from_coef(cn)
                mx = max(float(np.max(np.abs(dAn - dA))), float(np.max(np.abs(Bn - Bf))),
                         float(np.max(np.abs(Gn - Gm))))
                if mx > 0.8:
                    continue
                vn = vec(residual(A0 + dAn, Bn, Gn))
                if rms(vn) < cur:
                    rel_improve = (cur - rms(vn)) / cur
                    coef, dA, Bf, Gm = cn, dAn, Bn, Gn
                    v, cur = vn, rms(vn)
                    accepted = True
                    traj.append({'iter': it + 1, 'rms': cur,
                                 'max': float(np.max(np.abs(v))),
                                 'lam_mult': lam_mult, 'scale': scale})
                    print('iter %d rms %.6e lam_mult %g scale %g (%.0fs)'
                          % (it + 1, cur, lam_mult, scale, time.time() - t0), flush=True)
                    break
            if accepted:
                break
        if not accepted:
            traj.append({'iter': it + 1, 'rms': cur, 'note': 'no decreasing step'})
            print('stalled at iter', it + 1, 'rms', cur, flush=True)
            stall += 1
            if stall >= 2:
                break
        else:
            stall = 0
        if cur <= 2.5e-4:
            print('below 2.5e-4 with margin; stopping', flush=True)
            break

    Rfin = residual(A0 + dA, Bf, Gm)
    per = {c: {'rms': rms(Rfin[c][sample].ravel()),
               'max': float(np.max(np.abs(Rfin[c][sample])))} for c in COMPS}
    # BC verification numbers
    bc = {'beta_at_surface_maxabs': float(np.max(np.abs(Bf[-1, :]))),
          'dalpha_at_surface_maxabs': float(np.max(np.abs(dA[-1, :]))),
          'centre_phi_spread_max': float(max(np.ptp((A0 + dA)[0, :]), np.ptp(Bf[0, :]),
                                             np.ptp(Gm[0, :]))),
          'gamma_minmax': [float(np.min(Gm)), float(np.max(Gm))],
          'beta_minmax': [float(np.min(Bf)), float(np.max(Bf))],
          'dalpha_minmax': [float(np.min(dA)), float(np.max(dA))],
          'alpha_total_minmax': [float(np.min(A0 + dA)), float(np.max(A0 + dA))],
          'gamma_finite': bool(np.all(np.isfinite(Gm)))}
    base = traj[0]['rms']
    out = {'item': 'P8-3 gamma-extended GN solve, config ' + tag,
           'environment': 'system python3, numpy 2.2.6, scipy 1.14.1; float64',
           'config': {'M_modes': M, 'K_radial': K, 'dof': nb, 'Ns': Ns, 'Np': Np,
                      'maxiter': MAXIT, 'jacobian': 'forward FD eps=1e-3',
                      'damping': 'Levenberg lam_rel=1e-8 x mean col norm^2, adaptive x10 retries, step cap 0.8, backtracking 1/0.5/0.25'},
           'bc_set': ('centre: alpha,beta,gamma phi-independent at s=0, mode-m amplitude '
                      'O(s^m) via u^m factor, m=0 part even in s (d_s=0 at s=0); '
                      'surface: beta(15,phi)=0 and dalpha(15,phi)=0 via (1-u^2) factor '
                      '(alpha continuous, flat-exterior gauge alpha0(15)=0); '
                      'p_s(15,phi)=0 prescription-side (P6-4a sigma-shoot); '
                      'gamma finite, unconstrained at surface (matching stated, not solved)'),
           'bc_verification': bc,
           'trajectory': traj,
           'residual_before_rms': base,
           'residual_after_rms': cur,
           'rms_reduction_factor': float(base / cur),
           'residual_after_per_comp': per,
           'bar_rms': 2.99e-4, 'solved': bool(cur <= 2.99e-4),
           'runtime_s': time.time() - t0}
    (OUT / ('p83_solve_%s.json' % tag)).write_text(json.dumps(out, indent=1))
    np.savez(OUT / ('p83_fields_%s.npz' % tag), coef=coef, dalpha=dA, beta=Bf, gamma=Gm,
             alpha0=A0, s1d=s1d, phi1d=phi1d, M=M, K=K)
    print(json.dumps({k: out[k] for k in ('residual_after_rms', 'rms_reduction_factor',
                                          'solved', 'residual_after_per_comp',
                                          'bc_verification')}, indent=1))
    print('wrote results/p83_solve_%s.json + p83_fields_%s.npz' % (tag, tag))


if __name__ == '__main__':
    main()
