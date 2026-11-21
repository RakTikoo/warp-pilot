"""
warpax_candidate.py — Our shell candidate as a warpax ADMMetric, so warpax's
JAX-autodiff curvature chain can audit the SAME metric independently of our
finite-difference paths.

ADM data for the shell + shift metric (see shell.py):
  gamma_ij = delta_ij + (exp(2b)-1) n_i n_j          (profiles via interp)
  beta_i   = (-S(r) beta_w, 0, 0)                    (covariant shift)
  beta^i   = gamma^{ij} beta_j,  gamma^{-1} = I + (exp(-2b)-1) n n^T
  alpha    = sqrt(exp(2a) + beta_i beta^i)           (since g_tt = -exp(2a))
"""
import numpy as np
import jax.numpy as jnp
import equinox as eqx
from jaxtyping import Array, Float
from warpax.geometry import ADMMetric


def _spline_eval(x, xs, coeffs):
    """Cubic-spline evaluation in JAX. coeffs: (4, N-1) PPoly coefficients
    (highest power first), identical to scipy's CubicSpline representation,
    so warpax differentiates exactly the C2 function our FD path samples."""
    idx = jnp.clip(jnp.searchsorted(xs, x) - 1, 0, coeffs.shape[1] - 1)
    dx = x - xs[idx]
    c = coeffs[:, idx]
    return ((c[0] * dx + c[1]) * dx + c[2]) * dx + c[3]


class ShellCandidateMetric(ADMMetric):
    r_grid: Float[Array, "Nr"]
    a_coeffs: Float[Array, "4 Nm1"]
    b_coeffs: Float[Array, "4 Nm1"]
    R1: Float[Array, ""] = eqx.field(converter=jnp.asarray, default=10.0)
    R2: Float[Array, ""] = eqx.field(converter=jnp.asarray, default=20.0)
    Rb: Float[Array, ""] = eqx.field(converter=jnp.asarray, default=1.0)
    beta_w: Float[Array, ""] = eqx.field(converter=jnp.asarray, default=0.02)

    def _ab(self, r):
        rc = jnp.clip(r, self.r_grid[0], self.r_grid[-1])
        a = _spline_eval(rc, self.r_grid, self.a_coeffs)
        b = _spline_eval(rc, self.r_grid, self.b_coeffs)
        return a, b

    shift_kind: str = eqx.field(static=True, default='cos')

    def _S(self, r):
        R1, R2, Rb = self.R1, self.R2, self.Rb
        if self.shift_kind == 'cos':
            u = jnp.clip((r - R1) / (R2 - R1), 0.0, 1.0)
            return 0.5 * (1.0 + jnp.cos(jnp.pi * u))
        ex = (R2 - R1) * (1.0 / (r - R2) + 1.0 / (r - R1))
        f = 1.0 / (jnp.exp(jnp.clip(ex, -60.0, 60.0)) + 1.0)
        return jnp.where(r < R1 + Rb, 1.0, jnp.where(r > R2 - Rb, 0.0, 1.0 - f))

    def _adm(self, coords):
        t, x, y, z = coords
        r = jnp.sqrt(x ** 2 + y ** 2 + z ** 2)
        a, b = self._ab(r)
        rsafe = jnp.where(r > 0, r, 1.0)
        n = jnp.array([x / rsafe, y / rsafe, z / rsafe])
        eb = jnp.exp(2 * b)
        gamma = jnp.eye(3) + (eb - 1.0) * jnp.outer(n, n)
        gamma_inv = jnp.eye(3) + (jnp.exp(-2 * b) - 1.0) * jnp.outer(n, n)
        w = -self._S(r) * self.beta_w
        beta_cov = jnp.array([w, 0.0, 0.0])
        beta_vec = gamma_inv @ beta_cov
        alpha = jnp.sqrt(jnp.exp(2 * a) + beta_cov @ beta_vec)
        return alpha, beta_vec, gamma

    def name(self) -> str:
        return "ShellCandidate (warp-pilot finalist)"

    def shape_function_value(self, coords):
        t, x, y, z = coords
        r = jnp.sqrt(x ** 2 + y ** 2 + z ** 2)
        return self._S(r)

    def symbolic(self):
        raise NotImplementedError("numeric-only candidate metric")

    def lapse(self, coords):
        return self._adm(coords)[0]

    def shift(self, coords):
        return self._adm(coords)[1]

    def spatial_metric(self, coords):
        return self._adm(coords)[2]


def make_metric(prof, beta_w, Rb=1.0, shift_kind='cos'):
    from scipy.interpolate import CubicSpline
    sa = CubicSpline(prof['r'], prof['a'])
    sb = CubicSpline(prof['r'], prof['b'])
    return ShellCandidateMetric(
        r_grid=jnp.asarray(prof['r']), a_coeffs=jnp.asarray(sa.c),
        b_coeffs=jnp.asarray(sb.c), R1=float(prof['R1']), R2=float(prof['R2']),
        Rb=float(Rb), beta_w=float(beta_w), shift_kind=shift_kind)
