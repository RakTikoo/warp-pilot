"""
stageC_opt.py — Stage C: precise point-auditor optimisation of shell configs.

Fixed sample set (radii 8.5..21.5 x 14 Fibonacci directions = 378 points)
so configs are compared on identical points. Objective: worst all-observer
margin (eigenvalue margins; any non-Type-I point with significant |T|
counts as a failure with its sampled NEC).
"""
import json, time
import numpy as np
import verify_metric as vm
import shell as sh

G_C2 = 7.426e-28
FUCHS_M = G_C2 * 4.49e27


def sample_points():
    rng = np.random.default_rng(42)
    i = np.arange(14)
    phi = np.arccos(1 - 2 * (i + 0.5) / 14)
    th = np.pi * (1 + 5 ** 0.5) * i
    dirs = np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)
    rad = np.linspace(8.5, 21.5, 27)
    pts = np.concatenate([dirs * r for r in rad])
    return pts


PTS = sample_points()


def eval_config(M, kind, params, sr, sp, beta_w=0.02, shift_kind='fuchs',
                Rb=1.0, ws=None, h=0.3, pts=None):
    if pts is None:
        pts = PTS
    prof = sh.build_shell(10.0, 20.0, M, kind=kind, params=params,
                          s_rho=sr, s_P=sp, Nr=3001)
    gfunc = sh.shell_point_factory(prof, beta_w, shift_kind, Rb, ws)
    G, That, m = vm.einstein_at_points(gfunc, pts, h=h)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-7, 1e-3 * abs(rho_peak))
    sig = scale > thr
    worst = {}
    for k in ('nec', 'wec', 'sec', 'dec'):
        worst[k] = float(np.min(m[k][sig]))
    w = min(worst.values())
    wk = min(worst, key=worst.get)
    wi = int(np.where(sig)[0][int(np.argmin(m[wk][sig]))])
    return {'M_geom': M, 'kind': kind, 'params': params, 's_rho': sr, 's_P': sp,
            'beta_w': beta_w, 'shift_kind': shift_kind, 'Rb': Rb, 'ws': ws,
            'worst': w, 'worst_kind': wk, 'worst_radius': float(np.linalg.norm(pts[wi])),
            **worst, 'typeI_frac_sig': float(np.mean(m['typeI'][sig])),
            'n_sig': int(np.sum(sig)),
            'rho_peak': rho_peak}


if __name__ == '__main__':
    import sys
    # (i) Stage B winner, precise audit
    t0 = time.time()
    base = eval_config(FUCHS_M, 'smoothbox', {'edge': 3.0}, 2.0, 1.16)
    print('BEST-BASE', {k: (round(v, 9) if isinstance(v, float) else v) for k, v in base.items()}, flush=True)
    # (ii) shift variants on the winner
    variants = [
        ('fuchs Rb=0.5', dict(shift_kind='fuchs', Rb=0.5)),
        ('fuchs Rb=2.0', dict(shift_kind='fuchs', Rb=2.0)),
        ('smoothstep Rb=0.5', dict(shift_kind='smoothstep', Rb=0.5)),
        ('smoothstep Rb=2.0', dict(shift_kind='smoothstep', Rb=2.0)),
        ('tanh w=3', dict(shift_kind='tanh', ws=[15.0, 3.0])),
        ('tanh w=4', dict(shift_kind='tanh', ws=[15.0, 4.0])),
        ('tanh w=5', dict(shift_kind='tanh', ws=[15.0, 5.0])),
    ]
    rows = [base]
    for name, kw in variants:
        r = eval_config(FUCHS_M, 'smoothbox', {'edge': 3.0}, 2.0, 1.16, **kw)
        r['variant'] = name
        rows.append(r)
        print('VAR', name, 'worst=', f"{r['worst']:.3e}", 'nec=', f"{r['nec']:.2e}",
              f"({time.time()-t0:.0f}s)", flush=True)
    with open('results/stageC1.json', 'w') as fh:
        json.dump(rows, fh, indent=1)
    print('STAGE C1 DONE')
