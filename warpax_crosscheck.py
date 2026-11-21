"""
warpax_crosscheck.py — independent-path audit of a finalist: warpax's JAX
autodiff curvature chain vs our finite-difference point auditor, at the
same spacetime points. Compares the Eulerian-frame stress-energy tensor
component by component and the Hawking-Ellis margins.
"""
import json, sys
import numpy as np
import jax.numpy as jnp
from warpax.geometry import evaluate_curvature_points
import verify_metric as vm
import shell as sh
from warpax_candidate import make_metric
from verify_finalist import fib_dirs


def warpax_that(metric, pts):
    coords = jnp.asarray(np.concatenate([np.zeros((len(pts), 1)), pts], axis=1))
    chain = evaluate_curvature_points(metric, coords)
    g = np.asarray(chain.metric)
    T = np.asarray(chain.stress_energy)
    That = np.empty_like(T)
    for i in range(len(pts)):
        That[i] = vm.eulerian_that(g[i], T[i])
    return g, T, That


def run(cfg, tag, npts_radii=(9.0, 10.5, 12.0, 15.0, 18.0, 19.5, 21.0)):
    prof = sh.build_shell(10.0, 20.0, cfg['M'], kind=cfg['kind'], params=cfg['params'],
                          s_rho=cfg['sr'], s_P=cfg['sp'], Nr=4001)
    gfunc = sh.shell_point_factory(prof, cfg['beta_w'], cfg['shift_kind'],
                                   cfg.get('Rb', 1.0), cfg.get('ws'))
    dirs = fib_dirs(10)
    pts = np.concatenate([dirs * r for r in npts_radii])
    metric = make_metric(prof, cfg['beta_w'], cfg.get('Rb', 1.0), cfg['shift_kind'])
    g_w, T_w, That_w = warpax_that(metric, pts)
    G_f, That_f, m_f = vm.einstein_at_points(gfunc, pts, h=0.15)
    # metric agreement first (same geometry?)
    g_f = gfunc(pts)
    dg = np.max(np.abs(g_w - g_f))
    scale = np.maximum(np.max(np.abs(That_f), axis=(1, 2)), 1e-12)
    rel = np.max(np.abs(That_w - That_f), axis=(1, 2)) / scale
    m_w = vm.hawking_ellis_margins(That_w)
    out = {'tag': tag, 'max_metric_diff': float(dg),
           'max_rel_That_diff': float(np.max(rel)),
           'median_rel_That_diff': float(np.median(rel)),
           'warpax_margins_min': {k: float(np.min(m_w[k])) for k in ('nec', 'wec', 'sec', 'dec')},
           'fd_margins_min': {k: float(np.min(m_f[k])) for k in ('nec', 'wec', 'sec', 'dec')},
           'warpax_typeI_frac': float(np.mean(m_w['typeI'])),
           'fd_typeI_frac': float(np.mean(m_f['typeI']))}
    print(json.dumps(out, indent=1))
    with open(f'results/warpax_{tag}.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    return out


if __name__ == '__main__':
    cfgA = {'M': 2.0, 'kind': 'edgepeaked', 'params': {'wd': 3.0, 'floor': 0.2},
            'sr': 2.0, 'sp': 1.16, 'beta_w': 0.02, 'shift_kind': 'cos', 'ws': [10.0, 20.0]}
    run(cfgA, 'A_M2.0_b0.02')
