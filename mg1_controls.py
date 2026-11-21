"""
mg1_controls.py — MG-1 mandatory controls:
 (1) alpha = 0 identity: fast-path T_m must equal the FD point auditor's
     G/8pi on a general ansatz config (cross-engine, GR limit).
 (2) Known-yes control: Finalist A's shell metric (spline profiles + cos
     shift) through the f(R) AD chain at alpha = 0 must reproduce A's
     verified margins (NEC +2.1214e-5 at the cross-check points).
"""
import numpy as np
import jax.numpy as jnp
import mg1_fr as mg
import verify_metric as vm
import metrics as mt
import shell as sh
from warpax_candidate import _spline_eval


def control_alpha0_identity():
    # general config: v=0.9, R=1, Delta=0.25, aA=0.3, aC=-0.2, eta=0.1
    v, R, D, aA, aC, eta = 0.9, 1.0, 0.25, 0.3, -0.2, 0.1
    pts = mg.sample_points(R, D)[:40]
    out = mg.audit_config_fast(v, R, D, aA, aC, eta, 0.0, pts)
    # FD auditor on the same metric: rebuild via make_metric -> numpy
    gf_jax = mg.make_metric(v, R, D, aA, aC, eta)
    gf_np = lambda P: np.stack([np.asarray(gf_jax(p)) for p in np.atleast_2d(P)])
    G, That, m = vm.einstein_at_points(gf_np, pts, h=0.05)
    print('alpha=0 identity: AD worst_m =', f"{out['worst_m']:+.6e}",
          ' FD nec min =', f"{float(np.min(m['nec'])):+.6e}",
          ' AD nec =', f"{out['m_nec']:+.6e}",
          ' typeI AD/FD =', out['typeI_frac_m'], float(np.mean(m['typeI'])))
    return out, m


def control_shell_known_yes():
    from scipy.interpolate import CubicSpline
    prof = sh.build_shell(10.0, 20.0, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2}, s_rho=2.0, s_P=1.16,
                          Nr=4001)
    sa = CubicSpline(prof['r'], prof['a'])
    sb = CubicSpline(prof['r'], prof['b'])
    r_grid = jnp.asarray(prof['r'])
    a_c = jnp.asarray(sa.c); b_c = jnp.asarray(sb.c)
    beta_w = 0.02

    def gf(xyz):
        X, y, z = xyz
        r = jnp.sqrt(X ** 2 + y ** 2 + z ** 2 + 1e-24)
        n = jnp.stack([X, y, z]) / r
        a = _spline_eval(r, r_grid, a_c)
        b = _spline_eval(r, r_grid, b_c)
        u = jnp.clip((r - 10.0) / 10.0, 0.0, 1.0)
        S = 0.5 * (1.0 + jnp.cos(jnp.pi * u))
        eb = jnp.exp(2 * b)
        gam = jnp.eye(3) + (eb - 1.0) * jnp.outer(n, n)
        g = jnp.zeros((4, 4))
        g = g.at[0, 0].set(-jnp.exp(2 * a))
        g = g.at[0, 1].set(-S * beta_w)
        g = g.at[1, 0].set(-S * beta_w)
        g = g.at[1:, 1:].set(gam)
        return g

    from verify_finalist import fib_dirs
    dirs = fib_dirs(10)
    pts = np.concatenate([dirs * r for r in (9.0, 10.5, 12.0, 15.0, 18.0, 19.5, 21.0)])
    Tm, Te, Rsc, F = mg.tensors_at_points(gf, pts, 0.0)
    mm = vm.hawking_ellis_margins(np.stack(
        [vm.eulerian_that(np.asarray(gf(p)), np.asarray(Tm[i])) for i, p in enumerate(pts)]))
    print('shell known-yes (alpha=0, AD chain): NEC min =', f"{float(np.min(mm['nec'])):+.6e}",
          ' (verified FD value +2.12140e-05)  typeI =', float(np.mean(mm['typeI'])))


if __name__ == '__main__':
    control_alpha0_identity()
    control_shell_known_yes()
