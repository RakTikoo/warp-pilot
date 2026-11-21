"""
redteam.py — Red-team verification package (work order 2026-11-21 01:23).

R1: adversarial point-hunt — JAX autodiff through the frozen shell
    metric; Adam restarts minimising the NEC (and WEC) contraction over
    (position, observer direction/boost). The finalist stands only if
    the hunt cannot push the margin below zero.
R3: observer-completeness cross-check — FD auditor tensors at random
    points; eigenvalue margins vs brute random-observer contractions
    (sign + ordering agreement at scale).

Metric/JAX conventions mirror shell.shell_point_factory exactly
(cos shift on [R1, R2]); profiles via the same C2 spline warpax used.
"""
import json
import numpy as np
import jax
import jax.numpy as jnp
from scipy.interpolate import CubicSpline
import shell as sh
import verify_metric as vm
import mg1_fr as mg

jax.config.update('jax_enable_x64', True)
EIGHT_PI = 8.0 * np.pi


def load_cfg(name):
    return json.load(open(f'results/frozen/{name}.json'))


def build_profiles(cfg):
    prof = sh.build_shell(cfg['R1'], cfg['R2'], cfg['M_geom'], kind=cfg['kind'],
                          params=cfg['params'], s_rho=cfg['s_rho'],
                          s_P=cfg['s_P'], Nr=3001)
    return prof


def _spline_eval(x, xs, coeffs):
    idx = jnp.clip(jnp.searchsorted(xs, x) - 1, 0, coeffs.shape[1] - 1)
    dx = x - xs[idx]
    c = coeffs[:, idx]
    return ((c[0] * dx + c[1]) * dx + c[2]) * dx + c[3]


def make_jax_gf(cfg):
    prof = build_profiles(cfg)
    xs = jnp.asarray(prof['r'])
    ac = jnp.asarray(CubicSpline(prof['r'], prof['a']).c)
    bc = jnp.asarray(CubicSpline(prof['r'], prof['b']).c)
    R1, R2, bw = cfg['R1'], cfg['R2'], cfg['beta']
    lo, hi = cfg['ws']

    def gf(xyz):
        r = jnp.sqrt(jnp.sum(xyz ** 2) + 1e-18)
        rc = jnp.clip(r, xs[0], xs[-1])
        a = _spline_eval(rc, xs, ac)
        b = _spline_eval(rc, xs, bc)
        u = jnp.clip((r - lo) / (hi - lo), 0.0, 1.0)
        S = 0.5 * (1.0 + jnp.cos(jnp.pi * u))
        n = xyz / jnp.where(r > 0, r, 1.0)
        g = jnp.zeros((4, 4))
        g = g.at[0, 0].set(-jnp.exp(2 * a))
        g = g.at[0, 1].set(-S * bw).at[1, 0].set(-S * bw)
        eb = jnp.exp(2 * b) - 1.0
        gam = jnp.eye(3) + eb * jnp.outer(n, n)
        g = g.at[1:, 1:].set(gam)
        return g
    return gf


def that_jax(gf, xyz):
    """Eulerian-frame T_ab at xyz via the AD chain + analytic ADM tetrad."""
    Ric, Rsc, G, Gamma, g, gi = mg._ricci_scalar_and_tensor(gf, xyz)
    T = G / EIGHT_PI
    r = jnp.sqrt(jnp.sum(xyz ** 2) + 1e-18)
    n = xyz / jnp.where(r > 0, r, 1.0)
    # gamma and its inverse from g's spatial block
    gam = g[1:, 1:]
    gami = gi[1:, 1:] - jnp.outer(gi[1:, 0], gi[0, 1:]) / gi[0, 0] \
        if False else jnp.linalg.inv(gam)
    beta_cov = g[0, 1:]
    beta_up = gami @ beta_cov
    N = jnp.sqrt(jnp.exp(0.0) * (-g[0, 0]) + beta_cov @ beta_up)
    e0 = jnp.concatenate([jnp.array([1.0 / N]), -beta_up / N])
    # spatial triad: radial e^{-b} n ; tangential from cross products
    bprof = jnp.log(jnp.sqrt(gam[0, 0] * 0 + jnp.einsum('i,ij,j', n, gam, n)))
    erad = n / jnp.sqrt(jnp.einsum('i,ij,j', n, gam, n))
    ref = jnp.where(jnp.abs(n[2]) < 0.9, jnp.array([0.0, 0.0, 1.0]),
                    jnp.array([0.0, 1.0, 0.0]))
    t1 = ref - (ref @ erad) * erad
    t1 = t1 / jnp.sqrt(jnp.einsum('i,ij,j', t1, gam, t1))
    t2v = jnp.cross(erad, t1)
    t2 = t2v / jnp.sqrt(jnp.einsum('i,ij,j', t2v, gam, t2v))
    E = jnp.stack([e0,
                   jnp.concatenate([jnp.zeros(1), erad]),
                   jnp.concatenate([jnp.zeros(1), t1]),
                   jnp.concatenate([jnp.zeros(1), t2])])
    That = E @ T @ E.T
    return That


def nec_contraction(gf, xyz, th, ph):
    That = that_jax(gf, xyz)
    nvec = jnp.array([jnp.sin(th) * jnp.cos(ph), jnp.sin(th) * jnp.sin(ph),
                      jnp.cos(th)])
    k = jnp.concatenate([jnp.ones(1), nvec])
    return k @ That @ k, That


def wec_contraction(gf, xyz, th, ph, chi):
    That = that_jax(gf, xyz)
    nvec = jnp.array([jnp.sin(th) * jnp.cos(ph), jnp.sin(th) * jnp.sin(ph),
                      jnp.cos(th)])
    u = jnp.concatenate([jnp.array([jnp.cosh(chi)]), jnp.sinh(chi) * nvec])
    return u @ That @ u, That


def hunt(cfg, kind='nec', n_restarts=192, steps=500, seed=0, lr=0.06,
         seed_xyz=None):
    """Adam restarts minimising the contraction over (position, angles)."""
    gf = make_jax_gf(cfg)
    R1, R2 = cfg['R1'], cfg['R2']
    L = 1.6 * R2
    rng = np.random.default_rng(seed)

    def unpack(p):
        xyz = L * jnp.tanh(p[:3])
        th = p[3]; ph = p[4]
        return xyz, th, ph

    if kind == 'nec':
        def obj(p):
            xyz, th, ph = unpack(p)
            v, _ = nec_contraction(gf, xyz, th, ph)
            r = jnp.sqrt(jnp.sum(xyz ** 2))
            pen = 1e2 * jax.nn.softplus(r - 1.55 * R2) ** 2 \
                + 1e2 * jax.nn.softplus(0.3 - r) ** 2
            return v + pen
        npar = 5
    else:
        def obj(p):
            xyz, th, ph = unpack(p)
            v, _ = wec_contraction(gf, xyz, th, ph, p[5])
            r = jnp.sqrt(jnp.sum(xyz ** 2))
            pen = 1e2 * jax.nn.softplus(r - 1.55 * R2) ** 2 \
                + 1e2 * jax.nn.softplus(0.3 - r) ** 2
            return v + pen
        npar = 6

    grad_fn = jax.value_and_grad(obj)

    @jax.jit
    def run_batch(p0):
        def step(carry, _):
            p, m, v, t = carry
            val, gr = jax.vmap(grad_fn)(p)
            t = t + 1
            m = 0.9 * m + 0.1 * gr
            v = 0.999 * v + 0.001 * gr ** 2
            mh = m / (1 - 0.9 ** t)
            vh = v / (1 - 0.999 ** t)
            p = p - lr * mh / (jnp.sqrt(vh) + 1e-12)
            return (p, m, v, t), val
        p = p0
        m = jnp.zeros_like(p); v = jnp.zeros_like(p); t = 0
        (p, m, v, t), vals = jax.lax.scan(step, (p, m, v, t), None, length=steps)
        final = jax.vmap(obj)(p)
        return p, final

    # initial points: random in shell band + seeded worst locations
    inits = []
    for i in range(n_restarts):
        if seed_xyz is not None and i < len(seed_xyz):
            xyz = np.array(seed_xyz[i], dtype=float) \
                + rng.normal(0, 0.3, 3)
        else:
            rr = rng.uniform(0.35 * R1, 1.5 * R2)
            d = rng.normal(size=3); d /= np.linalg.norm(d)
            xyz = rr * d
        raw = np.arctanh(np.clip(xyz / L, -0.98, 0.98))
        base = [raw[0], raw[1], raw[2], rng.uniform(0, np.pi),
                rng.uniform(0, 2 * np.pi)]
        if kind == 'wec':
            base.append(rng.uniform(0, 2.0))
        inits.append(base)
    p0 = jnp.array(np.array(inits))
    p, final = run_batch(p0)
    p = np.array(p); final = np.array(final)
    i = int(np.argmin(final))
    xyz, th, ph = np.array(L * np.tanh(p[i][:3])), p[i][3], p[i][4]
    out = {'kind': kind, 'worst_value': float(final[i]), 'xyz': xyz.tolist(),
           'r': float(np.linalg.norm(xyz)), 'theta': float(th), 'phi': float(ph),
           'n_restarts': n_restarts, 'steps': steps,
           'frac_negative': float(np.mean(final < 0))}
    if kind == 'wec':
        out['chi'] = float(p[i][5])
    return out


# ---------------------------------------------------------------- R3
def observer_crosscheck(cfg, n_points=150, n_obs=300, seed=5):
    """FD tensors at random points; eigenvalue NEC vs random-observer
    contraction signs (null directions + boosted timelike)."""
    prof = build_profiles(cfg)
    gfunc = sh.shell_point_factory(prof, cfg['beta'], cfg['shift_kind'], 1.0,
                                   cfg['ws'])
    rng = np.random.default_rng(seed)
    R1, R2 = cfg['R1'], cfg['R2']
    rad = np.concatenate([rng.uniform(R1 - 0.15 * (R2 - R1), R2 + 0.3 * (R2 - R1),
                                      n_points - 20),
                          rng.uniform(0.4 * R1, R1, 20)])
    dirs = rng.normal(size=(n_points, 3))
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    pts = dirs * rad[:, None]
    G, That, m = vm.einstein_at_points(gfunc, pts, h=0.03 * R1)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    sig = scale > max(1e-9 * (10.0 / R1) ** 2, 1e-3 * abs(rho_peak))
    agree_nec = 0; agree_wec = 0; n_sig = 0
    ratios = []
    for i in np.where(sig)[0]:
        n_sig += 1
        # null contractions: k = e0 + n (Eulerian frame components)
        nd = rng.normal(size=(n_obs, 3))
        nd /= np.linalg.norm(nd, axis=1, keepdims=True)
        k = np.concatenate([np.ones((n_obs, 1)), nd], axis=1)
        c = np.einsum('pa,ab,pb->p', k, That[i], k)
        if np.sign(np.min(c)) == np.sign(m['nec'][i]) or m['nec'][i] > 0 and np.min(c) > 0:
            agree_nec += 1
        ratios.append(np.min(c) / m['nec'][i] if m['nec'][i] != 0 else np.nan)
        chi = rng.uniform(0, 2.0, n_obs)
        u = np.concatenate([np.cosh(chi)[:, None], np.sinh(chi)[:, None] * nd],
                           axis=1)
        cw = np.einsum('pa,ab,pb->p', u, That[i], u)
        if (np.min(cw) > 0) == (m['wec'][i] > 0):
            agree_wec += 1
    return {'n_points': int(n_points), 'n_sig': int(n_sig),
            'nec_sign_agree_frac': agree_nec / max(n_sig, 1),
            'wec_sign_agree_frac': agree_wec / max(n_sig, 1),
            'sampled_over_eigen_nec_ratio_median': float(np.nanmedian(ratios))}
