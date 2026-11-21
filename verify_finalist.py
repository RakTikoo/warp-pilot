"""
verify_finalist.py — full verification protocol for one shell candidate.

1. Dense point audits (h=0.3 and h=0.15), radii 3..24 x 26 directions.
2. Pure-Schwarzschild control at the same points (auditor vacuum noise floor).
3. Grid audits N=81 / N=121 (independent discretisation).
4. Photon transit asymmetry along the axis (Fuchs S5.1-style nontriviality).
5. ADM mass from lapse asymptotics; peak density in SI.
6. QI accounting: grid-integrated negative Eulerian energy (expect ~0).
"""
import json, sys
import numpy as np
import verify_metric as vm
import shell as sh

C_SI = 2.99792458e8
G_SI = 6.674e-11
G_C2 = G_SI / C_SI ** 2


def fib_dirs(n):
    i = np.arange(n)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


def dense_points():
    dirs = fib_dirs(26)
    rad = np.linspace(3.0, 24.0, 85)
    return np.concatenate([dirs * r for r in rad])


def schwarzschild_point(M):
    def gf(pts):
        pts = np.atleast_2d(pts)
        P = len(pts)
        r = np.linalg.norm(pts, axis=1)
        rs = np.where(r > 0, r, 1.0)
        n = pts / rs[:, None]
        f = 1 - 2 * M / rs
        g = np.zeros((P, 4, 4))
        g[:, 0, 0] = -f
        gam = np.eye(3)[None] + ((2 * M / (rs - 2 * M))[:, None, None] * n[:, :, None] * n[:, None, :])
        g[:, 1:, 1:] = gam
        return g
    return gf


def audit_block(gfunc, pts, h, label):
    G, That, m = vm.einstein_at_points(gfunc, pts, h=h)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-7, 1e-3 * abs(rho_peak))
    sig = scale > thr
    core = scale > 1e-5
    out = {'label': label, 'h': h, 'rho_peak': rho_peak, 'thr': thr,
           'n_sig': int(sig.sum()), 'n_core': int(core.sum())}
    for name, mask in (('sig', sig), ('core', core)):
        if mask.sum() == 0:
            continue
        out[name] = {k: float(np.min(m[k][mask])) for k in ('nec', 'wec', 'sec', 'dec')}
        out[name]['worst'] = min(out[name].values())
        out[name]['typeI_frac'] = float(np.mean(m['typeI'][mask]))
    wi = int(np.where(sig)[0][np.argmin(m['dec'][sig])]) if sig.any() else -1
    out['worst_dec_radius'] = float(np.linalg.norm(pts[wi])) if wi >= 0 else None
    return out, m, That


def photon_asymmetry(prof, beta_w, shift_kind, Rb, ws, L=25.0):
    from scipy.interpolate import CubicSpline
    r = prof['r']
    ea = CubicSpline(r, np.exp(2 * prof['a']))
    eb = CubicSpline(r, np.exp(2 * prof['b']))
    xs = np.linspace(-L, L, 5001)
    rr = np.abs(xs)
    gtt = -ea(rr)
    gtx = -sh.shift_S(rr, prof['R1'], prof['R2'], shift_kind, Rb, ws) * beta_w
    gxx = eb(rr)
    disc = np.sqrt(gtx ** 2 - gtt * gxx)
    # future-directed roots for travel in +x and -x directions
    dt_plus = (-gtx + disc) / gtt    # dt/dx for +x-moving photon (choose dt>0 branch by test)
    dt_minus = (-gtx - disc) / gtt
    # integrate signed: time to go from -L to +L uses root with dt/dx>0
    r1 = np.where(dt_plus > 0, dt_plus, dt_minus)
    r2 = np.where(dt_plus > 0, dt_minus, dt_plus)  # the other branch: -x-moving
    t_fwd = np.trapz(r1, xs)                    # -L -> +L
    t_bwd = -np.trapz(r2, xs)                   # +L -> -L duration (positive)
    return {'t_forward_m': float(t_fwd), 't_backward_m': float(t_bwd),
            'delta_t_ns': float((t_bwd - t_fwd) * (1e9 / C_SI))}


def main(cfg, tag):
    prof = sh.build_shell(10.0, 20.0, cfg['M'], kind=cfg['kind'], params=cfg['params'],
                          s_rho=cfg['sr'], s_P=cfg['sp'], Nr=4001)
    gfunc = sh.shell_point_factory(prof, cfg['beta_w'], cfg['shift_kind'], cfg.get('Rb', 1.0), cfg.get('ws'))
    pts = dense_points()
    res = {'tag': tag, 'cfg': cfg}
    a1, m1, _ = audit_block(gfunc, pts, 0.3, 'points h=0.3')
    a2, m2, _ = audit_block(gfunc, pts, 0.15, 'points h=0.15')
    res['point_audits'] = [a1, a2]
    with open(f'results/finalist_{tag}.json', 'w') as fh:
        json.dump(res, fh, indent=1)
    # h-error at worst-dec points (h=0.3 ordering)
    scale1 = None
    # Schwarzschild control (vacuum noise floor) — exterior points only,
    # where the candidate's exterior IS Schwarzschild
    gfS = schwarzschild_point(cfg['M'])
    ext = np.linalg.norm(pts, axis=1) >= 21.0
    GS, TS, mS = vm.einstein_at_points(gfS, pts[ext], h=0.3)
    res['schwarzschild_control'] = {
        'max_abs_T': float(np.max(np.abs(TS))),
        'note': 'auditor noise floor on exact vacuum at same points/h'}
    # grid audits
    grids = []
    for N in (81, 121):
        g, h, _xyz = sh.shell_grid(prof, N, 30.0, cfg['beta_w'], cfg['shift_kind'],
                                    cfg.get('Rb', 1.0), cfg.get('ws'))
        s = vm.grid_margins_summary(g, h, mask=(slice(None),) * 0 or None) \
            if False else None
        # manual mask: r in [5,25]
        ax = (np.arange(N) - (N - 1) / 2) * h
        X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')
        R = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
        mask = (R >= 5) & (R <= 25)
        s = vm.grid_margins_summary(g, h, mask=mask)
        s = {k: float(v) for k, v in s.items() if np.isscalar(v)}
        s['N'] = N
        grids.append(s)
        print('grid', N, {k: (f"{v:.3e}" if isinstance(v, float) else v) for k, v in s.items() if np.isscalar(v)}, flush=True)
    res['grid_audits'] = grids
    # photon asymmetry
    res['photon'] = photon_asymmetry(prof, cfg['beta_w'], cfg['shift_kind'],
                                      cfg.get('Rb', 1.0), cfg.get('ws'))
    # ADM mass from lapse asymptotics: e^{2a} ~ 1 - 2 M_ADM / r
    r = prof['r']
    sel = (r >= 30) & (r <= 39.9)
    A = np.vstack([np.ones(sel.sum()), -2.0 / r[sel]]).T
    coef, *_ = np.linalg.lstsq(A, np.exp(2 * prof['a'][sel]), rcond=None)
    res['ADM_fit'] = {'intercept': float(coef[0]), 'M_ADM_geom': float(coef[1]),
                      'M_input_geom': cfg['M']}
    # QI: integrated negative Eulerian energy on the N=121 grid
    g, h, _xyz = sh.shell_grid(prof, 121, 30.0, cfg['beta_w'], cfg['shift_kind'],
                                cfg.get('Rb', 1.0), cfg.get('ws'))
    That = vm.eulerian_that(g, vm.einstein_from_grid(g, h) / vm.EIGHT_PI)
    gam = g[:, :, :, 1:, 1:]
    det = np.linalg.det(gam)
    vol = np.sqrt(np.maximum(det, 0)) * h ** 3
    neg = np.sum(np.minimum(That[:, :, :, 0, 0], 0.0) * vol)
    pos = np.sum(np.maximum(That[:, :, :, 0, 0], 0.0) * vol)
    res['QI'] = {'integrated_negative_rho_geom_m': float(neg),
                 'integrated_negative_mass_kg': float(neg / G_C2),
                 'integrated_positive_rho_geom_m': float(pos)}
    res['SI'] = {'M_kg': cfg['M'] / G_C2,
                 'M_jupiter': cfg['M'] / G_C2 / 1.898e27,
                 'rho_peak_J_m3': a1['rho_peak'] * C_SI ** 4 / G_SI,
                 'rho_peak_kg_m3': a1['rho_peak'] * C_SI ** 2 / G_SI}
    print(json.dumps(res, indent=1))
    with open(f'results/finalist_{tag}.json', 'w') as fh:
        json.dump(res, fh, indent=1)
    return res


if __name__ == '__main__':
    cfgA = {'M': 2.0, 'kind': 'edgepeaked', 'params': {'wd': 3.0, 'floor': 0.2},
            'sr': 2.0, 'sp': 1.16, 'beta_w': 0.02, 'shift_kind': 'cos', 'ws': [10.0, 20.0]}
    main(cfgA, 'A_M2.0_b0.02')
