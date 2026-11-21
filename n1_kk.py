"""
n1_kk.py — N1: Kaluza-Klein lift of the shell.

Ansatz: ds5^2 = g4(shell) + exp(2 sigma(r)) dy^2, y on S^1 of
radius L_y (a free parameter of the construction — the D3
fifth-force gate L_y < 30 um is satisfiable by choice and does
not bind the geometry audit; the ATLAS 2.3 TeV floor binds the
RS-warped variant, not this flat S^1; both stated, neither
hidden). sigma stabilised by an unspecified potential (named
assumption, not derived).

Exact warped-product reduction (no 5D FD needed):
  R5_ab = R4_ab - Hess(sigma)_ab - d sigma_a d sigma_b   (4D block)
  R5^w_w = -(Box sigma + (d sigma)^2)
  R5 = R4 - 2 Box sigma - 2 (d sigma)^2
  G5 = R5 - 1/2 R5 g5 ;  T5 = G5 / 8 pi  = the 5D source required.
Audits:
  (i) 5D SOURCE: Hawking-Ellis margins of T5 in the 5D Eulerian
      frame (block tetrad + e_w) — eigenvalue form + sampled
      5D-null cross-check. If T5 violates its own ECs, any 4D
      relief is disguised exotic matter = FAIL (proposal rule).
  (ii) 4D EINSTEIN FRAME: g_tilde = exp(sigma) g4 (the frame in
      which the reduced action is canonical); standard judge.
  (iii) 4D Jordan/brane frame = the shell itself (known verdicts).
Configs: (M=2, beta=0.02) Finalist-A geometry (verified control)
and (M=2, beta=1.5) S7 superluminal point; sigma0 in {0.1, 0.3}.
float64 everywhere.
"""
import json, time
import numpy as np
from scipy.interpolate import CubicSpline

import shell as sh
import verify_metric as vm
from verify_finalist import dense_points

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi


def sigma_profile(sig0, Nr=4001, rmax=60.0):
    r = np.linspace(0.0, rmax, Nr)
    bump = sh.smootherstep((r - 6.0) / 4.0) \
        * (1.0 - sh.smootherstep((r - 20.0) / 4.0))
    cs = CubicSpline(r, sig0 * bump)
    return cs, cs.derivative(), cs.derivative(2)


def margins5(That5, rng):
    """5D margins: eigenvalue form (Type I) + sampled null check."""
    Tm = np.diag([-1.0, 1, 1, 1, 1]) @ That5
    ev = np.linalg.eigvals(Tm)
    out = {}
    if np.max(np.abs(ev.imag)) < 1e-9:
        ev = np.sort(ev.real)
        rho = -ev[0]; p = ev[1:]
        out = {'rho': float(rho), 'nec': float(rho + np.min(p)),
               'wec': float(rho), 'sec': float(rho + np.sum(p)),
               'dec': float(rho - np.max(np.abs(p))),
               'typeI': True}
    # sampled NEC over S^4 null directions
    n = rng.normal(size=(600, 4))
    n /= np.linalg.norm(n, axis=1)[:, None]
    k = np.zeros((600, 5)); k[:, 0] = 1.0; k[:, 1:] = n
    Tkk = np.einsum('ki,ij,kj->k', k, That5, k)
    out['nec_sampled'] = float(np.min(Tkk))
    return out


def run_config(M, beta, sig0, pts, rng):
    prof = sh.build_shell(10.0, 20.0, M, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 20.0])
    h = 0.3
    G4, That4, m4 = vm.einstein_at_points(gf, pts, h=h)
    Gamma, g4, ginv4 = vm._gamma_at(gf, pts, h)
    cs, d1, d2 = sigma_profile(sig0)
    r = np.linalg.norm(pts, axis=1)
    rs = np.where(r > 0, r, 1.0)
    n = pts / rs[:, None]
    rc = np.clip(r, 0.0, 60.0)
    s1 = d1(rc); s2 = d2(rc)
    P = len(pts)
    dsig = np.zeros((P, 4)); dsig[:, 1:] = s1[:, None] * n
    dd = np.zeros((P, 4, 4))
    coef = np.where(r > 0, s1 / rs, 0.0)
    for i in range(3):
        for j in range(3):
            dd[:, 1 + i, 1 + j] = s2 * n[:, i] * n[:, j] \
                + coef * ((1.0 if i == j else 0.0) - n[:, i] * n[:, j])
    Hess = dd - np.einsum('pabc,pc->pab', Gamma, dsig)
    BoxS = np.einsum('pab,pab->p', ginv4, Hess)
    grad2 = np.einsum('pab,pa,pb->p', ginv4, dsig, dsig)
    R4sc = -np.einsum('pab,pab->p', ginv4, G4)
    R4 = G4 + 0.5 * R4sc[:, None, None] * g4
    R5sc = R4sc - 2.0 * BoxS - 2.0 * grad2
    G5_4 = (R4 - Hess - dsig[:, :, None] * dsig[:, None, :]) \
        - 0.5 * R5sc[:, None, None] * g4
    sig = cs(rc)
    Rww_mixed = -(BoxS + grad2)
    G5_ww = np.exp(2 * sig) * (Rww_mixed - 0.5 * R5sc)
    T5_4 = G5_4 / EIGHT_PI
    That5_4 = vm.eulerian_that(g4, T5_4)
    That5 = np.zeros((P, 5, 5))
    That5[:, :4, :4] = That5_4
    That5[:, 4, 4] = np.exp(-2 * sig) * G5_ww / EIGHT_PI
    scale = np.max(np.abs(That5), axis=(1, 2))
    sigmask = scale > 1e-6
    m5 = [margins5(That5[i], rng) for i in np.where(sigmask)[0]]
    nec5 = min(x['nec'] for x in m5 if 'nec' in x) if m5 else None
    nec5s = min(x['nec_sampled'] for x in m5) if m5 else None
    wec5 = min(x['wec'] for x in m5 if 'wec' in x) if m5 else None
    dec5 = min(x['dec'] for x in m5 if 'dec' in x) if m5 else None
    # Einstein frame
    def gf_tilde(p):
        gg = gf(p)
        rr = np.linalg.norm(p, axis=1)
        return np.exp(cs(np.clip(rr, 0, 60.0)))[:, None, None] * gg
    _, _, me = vm.einstein_at_points(gf_tilde, pts, h=h)
    worst_e = float(np.min(np.minimum(
        np.minimum(me['nec'], me['wec']),
        np.minimum(me['sec'], me['dec']))))
    worst_j = float(np.min(np.minimum(
        np.minimum(m4['nec'], m4['wec']),
        np.minimum(m4['sec'], m4['dec']))))
    return {'M': M, 'beta': beta, 'sigma0': sig0,
            'jordan_worst': worst_j,
            'source5_nec': nec5, 'source5_nec_sampled': nec5s,
            'source5_wec': wec5, 'source5_dec': dec5,
            'einstein_worst': worst_e,
            'einstein_nec': float(np.min(me['nec']))}


def main():
    t0 = time.time()
    pts = dense_points()[::2]
    rng = np.random.default_rng(99)
    out = {'configs': []}
    for (M, beta) in ((2.0, 0.02), (2.0, 1.5)):
        for sig0 in (0.1, 0.3):
            row = run_config(M, beta, sig0, pts, rng)
            out['configs'].append(row)
            print(f"M={M:g} beta={beta} sig0={sig0}: jordan "
                  f"{row['jordan_worst']:+.3e} | 5D source NEC "
                  f"{row['source5_nec']:+.3e} (sampled "
                  f"{row['source5_nec_sampled']:+.3e}) WEC "
                  f"{row['source5_wec']:+.3e} DEC "
                  f"{row['source5_dec']:+.3e} | einstein worst "
                  f"{row['einstein_worst']:+.3e}", flush=True)
    out['elapsed_s'] = time.time() - t0
    out['gates'] = ('L_y free: D3 fifth-force gate L_y < 30 um '
                    'satisfiable by choice; ATLAS RS floor binds '
                    'the warped variant only (this is flat S1). '
                    'Assumption: sigma stabilised by an '
                    'unspecified potential (stated, not derived); '
                    'an unstabilised modulus would be case (1) '
                    'under D3/MICROSCOPE.')
    json.dump(out, open('results/n1_kk.json', 'w'), indent=1, default=float)
    print('N1 DONE', flush=True)


if __name__ == '__main__':
    main()
