"""X3 diagnostics: volume-integral I_V^- and SNEC functional for the
frozen finalists, as post-processing on the established judge.

I_V^- (all-observer version, Visser-Kar-Dadhich style): integral over
the spatial volume of min(rho + p_min, 0), where rho + p_min is the
NEC margin at Type-I points (Hawking-Ellis eigenvalues). Computed on
an N=81 grid audit.

SNEC functional (Freivogel-Krommydas, conjectured): along the axis
null geodesic through the shell centre,
  S(tau) = int g^2(lam) T_kk dlam + (4B/G_N) int (g')^2 dlam >= 0 ?
with Gaussian smearing g of width tau centred on the wall crossing.
We report I(tau) = int g^2 T_kk dlam and the implied B_min (the B at
which S = 0); pointwise NEC >= 0 everywhere implies I(tau) >= 0 and
B_min <= 0, i.e. SNEC is satisfied for any B >= 0 — the numbers are
the diagnostic. Null tangent: axis ray, k^t = 1 normalisation,
k^x from the null condition of the shell metric at y=z=0 (diagnostic
normalisation, stated as such). Geometric units (G_N = 1 in the
functional's second term as reported via B_min).
"""
import json
import numpy as np

import verify_metric as vm
import shell as sh


class rt:  # minimal stand-ins (redteam.py pulls in jax; not needed here)
    @staticmethod
    def load_cfg(name):
        return json.load(open(f'results/frozen/{name}.json'))

    @staticmethod
    def build_profiles(cfg):
        return sh.build_shell(cfg['R1'], cfg['R2'], cfg['M_geom'],
                              kind=cfg['kind'], params=cfg['params'],
                              s_rho=cfg['s_rho'], s_P=cfg['s_P'], Nr=3001)


def iv_minus(cfg, N=81):
    prof = rt.build_profiles(cfg)
    g, h, _xyz = sh.shell_grid(prof, N, 30.0, cfg['beta'], cfg['shift_kind'],
                               1.0, cfg['ws'])
    out = vm.audit_metric(g, h)
    nec = out['nec']  # grid array of NEC margins (eigenvalue; sampled fallback)
    neg = np.minimum(nec, 0.0)
    return float(np.sum(neg) * h**3), out


def snec_axis(cfg, taus=(0.5, 1.0, 2.0, 5.0), xs_half=30.0, n=241):
    prof = rt.build_profiles(cfg)
    gfunc = sh.shell_point_factory(prof, cfg['beta'], cfg['shift_kind'],
                                   1.0, cfg['ws'])
    xs = np.linspace(-xs_half, xs_half, n)
    pts = np.stack([xs, np.zeros(n), np.zeros(n)], axis=1)
    G, That, _ = vm.einstein_at_points(gfunc, pts, h=0.15,
                                       do_fallback=False)
    T = G / (8 * np.pi)
    # Eulerian-frame T_ab -> covariant in coordinate basis along axis:
    # at y=z=0 the Eulerian tetrad of the shell metric: use T_ab k^a k^b
    # with k from the metric null condition, k^t = 1.
    g = gfunc(pts)
    gtt, gtx, gxx = g[:, 0, 0], g[:, 0, 1], g[:, 1, 1]
    # null: gtt + 2 gtx kx + gxx kx^2 = 0, forward root
    disc = np.maximum(gtx**2 - gtt * gxx, 0.0)
    kx = (-gtx + np.sqrt(disc)) / gxx
    k = np.zeros((n, 4)); k[:, 0] = 1.0; k[:, 1] = kx
    Tkk = np.einsum('ni,nij,nj->n', k, T, k)
    res = {}
    for tau in taus:
        for centre, cname in ((cfg['R1'] + 0.5 * (cfg['R2'] - cfg['R1']), 'wall'),
                              (0.0, 'centre')):
            gsm = np.exp(-0.5 * ((xs - centre) / tau) ** 2)
            gp = np.gradient(gsm, xs)
            I = float(np.trapz(gsm**2 * Tkk, xs))
            J = float(np.trapz(gp**2, xs))
            Bmin = -I / (4 * J) if J > 0 else float('nan')
            res[f'tau={tau}_{cname}'] = {'I_smeared_Tkk': I,
                                         'int_gp2': J, 'B_min': Bmin}
    return res, float(np.min(Tkk))


def main():
    out = {}
    for name in ('finalist_A', 'finalist_B2', 'frontier_b005'):
        cfg = rt.load_cfg(name)
        iv, _ = iv_minus(cfg)
        snec, tkk_min = snec_axis(cfg)
        out[name] = {'I_V_minus_geom': iv, 'axis_Tkk_min': tkk_min,
                     'snec': snec}
        print(name, 'I_V^- =', iv, ' axis Tkk min =', tkk_min)
        for kk, vv in snec.items():
            print('   ', kk, {a: round(b, 6) for a, b in vv.items()})
    json.dump(out, open('results/x3_diag.json', 'w'), indent=1)
    print('X3 DONE')


if __name__ == '__main__':
    main()
