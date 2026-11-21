"""
mg2_scan.py — MG-2 validation + scan.
Validations:
  V1 FLRW anchor: Q = +6H^2 (Mandal Eq. (8)) with the adopted pair.
  V2 beta=0 identity: Tm_zhao == G/(8 pi) at ansatz points (FD precision).
  V3 Zhao vs Mandal: Tm_zhao vs -Tm_mandal/(8 pi) at beta != 0 points
     (the two printed forms of arXiv:2208.13636 must agree).
  V4 shell known-yes: Finalist A metric through Tm_zhao at beta=0
     reproduces NEC +2.12140e-5.
Scan: generalised ADM ansatz (NumPy twin of mg1_fr.make_metric),
amps x v x beta-hat grid; audit T_m (Zhao) all-observer + T_eff margins.
Output: results/mg2_scan.json
"""
import json, time
import numpy as np
import verify_metric as vm
import mg2_fq as m2

EIGHT_PI = 8.0 * np.pi


def make_metric_np(v_s, R, Delta, aA, aC, eta):
    sigma = 1.0 / Delta

    def shape(r):
        return (np.tanh(sigma * (r + R)) - np.tanh(sigma * (r - R))) / \
               (2 * np.tanh(sigma * R))

    def gf(pts):
        pts = np.atleast_2d(np.asarray(pts, dtype=float))
        X, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        r = np.sqrt(X ** 2 + y ** 2 + z ** 2 + 1e-24)
        n = np.stack([X / r, y / r, z / r], axis=1)
        f = shape(r)
        bump = np.exp(-((r - R) / Delta) ** 2)
        lapse = np.exp(aA * bump)
        psi4 = np.exp(4 * aC * bump)
        # shape'(r) analytic
        fp = sigma * (1 / np.cosh(sigma * (r + R)) ** 2
                      - 1 / np.cosh(sigma * (r - R)) ** 2) / (2 * np.tanh(sigma * R))
        beta_irr = v_s * ((1 - f)[:, None] * np.array([1.0, 0.0, 0.0])
                          - (X * fp)[:, None] * n)
        beta_alc = np.stack([v_s * (1 - f), np.zeros_like(f),
                             np.zeros_like(f)], axis=1)
        beta = (1 - eta) * beta_irr + eta * beta_alc
        P = len(pts)
        g = np.zeros((P, 4, 4))
        g[:, 0, 0] = -lapse ** 2 + psi4 * np.sum(beta ** 2, axis=1)
        g[:, 0, 1:] = psi4[:, None] * beta
        g[:, 1:, 0] = psi4[:, None] * beta
        for i in range(3):
            g[:, 1 + i, 1 + i] = psi4
        return g
    return gf


def sample_points(R, Delta, ndir=10):
    i = np.arange(ndir)
    phi = np.arccos(1 - 2 * (i + 0.5) / ndir)
    th = np.pi * (1 + 5 ** 0.5) * i
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)
    rad = np.array([0.1 * R, 0.3 * R, 0.5 * R, R - 1.5 * Delta, R - 0.75 * Delta,
                    R - 0.25 * Delta, R, R + 0.25 * Delta, R + 0.75 * Delta,
                    R + 1.5 * Delta, 1.3 * R, 1.6 * R])
    rad = rad[rad > 0]
    return np.concatenate([dirs * r for r in rad])


def margins_of(gf, pt, Tm):
    That = vm.eulerian_that(gf(pt[None]), Tm[None])
    m = vm.hawking_ellis_margins(That, do_fallback=True)
    return {k: float(m[k][0]) for k in ('nec', 'wec', 'sec', 'dec')}, \
        bool(m['typeI'][0])


def audit_config(v_s, R, Delta, aA, aC, eta, beta, pts):
    gf = make_metric_np(v_s, R, Delta, aA, aC, eta)
    rows = []
    for pt in pts:
        Tm, Q0 = m2.Tm_zhao(gf, pt, beta)
        mm, tI = margins_of(gf, pt, Tm)
        G, That_eff, me = vm.einstein_at_points(gf, pt[None], h=0.15,
                                                do_fallback=False)
        rows.append((mm, tI, float(me['nec'][0]), abs(Q0)))
    worst = {k: min(r[0][k] for r in rows) for k in ('nec', 'wec', 'sec', 'dec')}
    return {'worst_m': min(worst.values()), **worst,
            'typeI_frac_m': float(np.mean([r[1] for r in rows])),
            'eff_nec_min': min(r[2] for r in rows),
            'Q_absmax': max(r[3] for r in rows)}


def main():
    out = {'validations': {}, 'scan': []}
    # V1
    def gf4(pts):
        pts = np.atleast_2d(pts)
        a2 = np.exp(2 * 0.7 * pts[:, 0])
        g = np.zeros((len(pts), 4, 4))
        g[:, 0, 0] = -1.0
        g[:, 1, 1] = a2; g[:, 2, 2] = a2; g[:, 3, 3] = a2
        return g
    q = m2.Qscalar(gf4, np.array([0.3, 0.1, -0.2, 0.05]), h=0.05)
    out['validations']['V1_FLRW_Q'] = {'Q': q, 'expect': 2.94}
    print('V1 Q =', q, '(expect +2.94)', flush=True)

    gf = make_metric_np(0.9, 1.0, 0.25, 0.3, -0.2, 0.1)
    pts = sample_points(1.0, 0.25)
    # V2 beta=0 identity (covariant Tm vs G/8pi — NOT the Eulerian That)
    diffs = []
    for pt in pts[::17]:
        Tm, _ = m2.Tm_zhao(gf, pt, 0.0)
        G, That, _ = vm.einstein_at_points(gf, pt[None], h=0.15, do_fallback=False)
        diffs.append(float(np.max(np.abs(Tm - G[0] / EIGHT_PI))))
    out['validations']['V2_beta0_maxdiff'] = max(diffs)
    print('V2 beta=0 max |Tm - G/8pi| =', max(diffs), flush=True)
    # V3 Zhao vs Mandal at beta != 0
    beta_t = 0.05
    zd, md = [], []
    for pt in pts[::23]:
        Tz, _ = m2.Tm_zhao(gf, pt, beta_t)
        Lm = m2.Tm_mandal(gf, pt, beta_t)
        Tm_from_mandal = -Lm / EIGHT_PI
        zd.append(float(np.max(np.abs(Tz - Tm_from_mandal))))
        md.append(float(np.max(np.abs(Tz))))
    out['validations']['V3_zhao_vs_mandal'] = {
        'beta': beta_t, 'maxdiff': max(zd), 'max_scale': max(md)}
    print('V3 Zhao-vs-Mandal maxdiff =', max(zd), 'scale', max(md), flush=True)
    # V4 shell known-yes
    import shell as sh
    prof = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2}, s_rho=2.0, s_P=1.16)
    gfs = sh.shell_point_factory(prof, 0.02, 'cos', 1.0, [10.0, 20.0])
    rad = (9.0, 10.5, 12.0, 15.0, 18.0, 19.5, 21.0)
    dirs = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1],
                     [0, 1, 1], [1, 1, 1], [-1, 1, 0], [1, -1, 1], [2, 1, -1]],
                    dtype=float)
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    necs = []
    for r in rad:
        for d in dirs:
            Tm, _ = m2.Tm_zhao(gfs, r * d, 0.0)
            mm, tI = margins_of(gfs, r * d, Tm)
            necs.append(mm['nec'])
    out['validations']['V4_shell_nec_min'] = min(necs)
    print('V4 shell NEC min =', min(necs), '(expect +2.12140e-5)', flush=True)

    # scan
    t0 = time.time()
    for amps in [(0.0, 0.0), (0.3, 0.0), (0.0, 0.3), (0.3, -0.3)]:
        for v in (0.9, 1.5, 2.0):
            base = audit_config(v, 1.0, 0.25, amps[0], amps[1], 0.0, 0.0, pts)
            Qs = base['Q_absmax']
            base.update(v_s=v, aA=amps[0], aC=amps[1], beta=0.0, betahat=0.0)
            out['scan'].append(base)
            for bh in (1e-2, 1e-1, 1.0, 10.0):
                beta = bh / Qs if Qs > 0 else 0.0
                r = audit_config(v, 1.0, 0.25, amps[0], amps[1], 0.0, beta, pts)
                r.update(v_s=v, aA=amps[0], aC=amps[1], beta=beta, betahat=bh,
                         Q_star=Qs)
                out['scan'].append(r)
            print(f"amps={amps} v={v} done ({time.time()-t0:.0f}s) "
                  f"GR worst={base['worst_m']:+.3e} Q*={Qs:.3e}", flush=True)
            json.dump(out, open('results/mg2_scan.json', 'w'), indent=1)
    print('MG2 DONE', flush=True)


if __name__ == '__main__':
    main()
