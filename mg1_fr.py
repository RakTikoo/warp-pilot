"""
mg1_fr.py — MG-1 lens: metric f(R) = R + alpha R^2 gravity on a generalised
warp ansatz, audited for the MATTER stress-energy tensor.

Field equation (Lobo, arXiv:1112.6333, Eqs. 2-5; standard form, kappa^2=8pi):
    8 pi T_m = F R_mn - (1/2) f g_mn - nabla_m nabla_n F + g_mn Box F,
    f = R + alpha R^2,  F = df/dR = 1 + 2 alpha R.
T_eff = G_mn / (8 pi) is the geometric tensor (must violate NEC somewhere
for the geometry to do warp work). alpha -> 0 recovers GR exactly.

Numerics: JAX autodiff (x64). R(x) is built from nested jacfwd of the
metric, so dR and d2R (hence nabla nabla F, containing 4th metric
derivatives) are exact AD quantities, not finite differences.
The metric is stationary: all t-derivatives vanish; spatial AD only,
embedded into 4x4 arrays.

Ansatz (COMOVING frame: coordinates (T, X, y, z), bubble centre at origin,
metric stationary in T — the standard warp-bubble presentation):
    ds^2 = -lapse^2 dT^2 + psi^4 delta_ij (dX^i + beta^i dT)(dX^j + beta^j dT)
    lapse = exp(A(r)), A = aA * exp(-((r-R)/Delta)^2)         (wall bump)
    psi   = exp(C(r)), C = aC * exp(-((r-R)/Delta)^2)
    beta  = (1-eta) * grad(Phi) + eta * beta_Alcubierre,
    Phi   = +v_s * X * (1 - f(r))  (irrotational / Rodal-type seed:
            grad Phi = v_s ((1-f) e_X - X f'(r) n) -> 0 inside (passengers
            at rest in the comoving frame), +v_s e_X outside)
    beta_Alcubierre = (+v_s (1 - f(r)), 0, 0)  (comoving ADM shift, the
            Phase-0 convention: g_TT = -1 + v_s^2 (1-f)^2 etc.)
    f     = Alcubierre tanh shape with wall thickness Delta.
"""
import numpy as np
import jax
import jax.numpy as jnp

jax.config.update('jax_enable_x64', True)
EIGHT_PI = 8.0 * np.pi


# ---------------------------------------------------------------- ansatz
def make_metric(v_s, R, Delta, aA, aC, eta):
    sig = 1.0 / Delta
    den = 2.0 * jnp.tanh(sig * R)

    def shape(r):
        return (jnp.tanh(sig * (r + R)) - jnp.tanh(sig * (r - R))) / den

    def shape_p(r):
        return sig * (1.0 / jnp.cosh(sig * (r + R)) ** 2
                      - 1.0 / jnp.cosh(sig * (r - R)) ** 2) / den

    def g_of_xyz(xyz):
        X, y, z = xyz
        r = jnp.sqrt(X ** 2 + y ** 2 + z ** 2 + 1e-24)
        n = xyz / r
        f = shape(r)
        fp = shape_p(r)
        bump = jnp.exp(-(((r - R) / Delta) ** 2))
        lapse = jnp.exp(aA * bump)
        psi4 = jnp.exp(4.0 * aC * bump)
        # irrotational shift: grad Phi, Phi = +v X (1-f(r)) (comoving frame)
        beta_irr = v_s * ((1.0 - f) * jnp.array([1.0, 0.0, 0.0]) - X * fp * n)
        beta_alc = jnp.array([v_s * (1.0 - f), 0.0, 0.0])
        beta = (1.0 - eta) * beta_irr + eta * beta_alc
        g = jnp.zeros((4, 4))
        g = g.at[0, 0].set(-lapse ** 2 + psi4 * (beta @ beta))
        g = g.at[0, 1:].set(psi4 * beta)
        g = g.at[1:, 0].set(psi4 * beta)
        g = g.at[1:, 1:].set(psi4 * jnp.eye(3))
        return g
    return g_of_xyz


# ---------------------------------------------------------------- AD chain
def _christoffel(gf, xyz):
    """Gamma^lam_{mu nu} (4,4,4) at xyz; t-derivatives are zero."""
    g = gf(xyz)
    dg3 = jax.jacfwd(gf)(xyz).transpose(2, 0, 1)   # (3,4,4): d_a g_mn
    dg = jnp.zeros((4, 4, 4)).at[1:].set(dg3)   # d_mu g_mn
    gi = jnp.linalg.inv(g)
    # Gamma^lam_{mu nu} = 1/2 g^{lam s} (d_mu g_{nu s} + d_nu g_{mu s} - d_s g_{mu nu})
    d = dg  # d[mu][a][b]
    Slist = []
    for mu in range(4):
        row = []
        for nu in range(4):
            row.append(d[mu, nu, :] + d[nu, mu, :] - d[:, mu, nu])
        Slist.append(jnp.stack(row))
    S = jnp.stack(Slist)                   # (mu, nu, s)
    Gamma = 0.5 * jnp.einsum('ls,mns->lmn', gi, S)
    return Gamma, g, gi


def _ricci_scalar_and_tensor(gf, xyz):
    """Returns (R_mn (4,4), R scalar, G_mn (4,4)) via AD."""
    def Gamma_of(x):
        return _christoffel(gf, x)[0]
    Gamma, g, gi = _christoffel(gf, xyz)
    dG3 = jax.jacfwd(Gamma_of)(xyz).transpose(3, 0, 1, 2)   # (3,4,4,4)
    dGamma = jnp.zeros((4, 4, 4, 4)).at[1:].set(dG3)
    # R^rho_{s mu nu} = d_mu Gamma^rho_{nu s} - d_nu Gamma^rho_{mu s}
    #                   + Gamma^rho_{mu l} Gamma^l_{nu s} - Gamma^rho_{nu l} Gamma^l_{mu s}
    # dGamma layout: [d_a][lam][mu][nu]; T1[rho][s][mu][nu] = d_mu Gamma^rho_{nu s}
    T1 = jnp.einsum('dlms->lsdm', dGamma)
    GG = jnp.einsum('rml,lns->rsmn', Gamma, Gamma)
    Riem = (T1 - T1.transpose(0, 1, 3, 2)
            + GG - GG.transpose(0, 1, 3, 2))
    Ric = jnp.einsum('rsrn->sn', Riem)     # R_{s n} = R^r_{s r n}
    Rsc = jnp.einsum('sm,sm->', gi, Ric)
    G = Ric - 0.5 * Rsc * g
    return Ric, Rsc, G, Gamma, g, gi


def _scalar_R(gf, xyz):
    return _ricci_scalar_and_tensor(gf, xyz)[1]


def tensors_at_point(gf, xyz, alpha):
    """T_m and T_eff (covariant, coordinate frame) at one point, plus
    diagnostics (R, F). alpha is the f(R) coupling (geometric units)."""
    Ric, Rsc, G, Gamma, g, gi = _ricci_scalar_and_tensor(gf, xyz)
    F = 1.0 + 2.0 * alpha * Rsc
    f = Rsc + alpha * Rsc ** 2
    # derivatives of F: dF = 2 alpha dR ; d2F = 2 alpha d2R (spatial blocks)
    dR = jax.jacfwd(lambda x: _scalar_R(gf, x))(xyz)          # (3,)
    d2R = jax.jacfwd(jax.jacfwd(lambda x: _scalar_R(gf, x)))(xyz)  # (3,3)
    dF = jnp.zeros(4).at[1:].set(2.0 * alpha * dR)
    ddF = jnp.zeros((4, 4)).at[1:, 1:].set(2.0 * alpha * d2R)
    nabnabF = ddF - jnp.einsum('lmn,l->mn', Gamma, dF)
    boxF = jnp.einsum('mn,mn->', gi, nabnabF)
    Tm = (F * Ric - 0.5 * f * g - nabnabF + g * boxF) / EIGHT_PI
    Teff = G / EIGHT_PI
    return Tm, Teff, Rsc, F


def tensors_at_points(gf, pts, alpha):
    """vmap over points (P,3) -> (Tm, Teff, R, F) arrays."""
    fn = jax.vmap(lambda x: tensors_at_point(gf, x, alpha))
    return fn(jnp.asarray(pts))


# ---------------------------------------------------------------- audit
import verify_metric as vm


def audit_config(v_s, R, Delta, aA, aC, eta, alpha, pts):
    gf = make_metric(v_s, R, Delta, aA, aC, eta)
    Tm, Teff, Rsc, F = tensors_at_points(gf, pts, alpha)
    Tm = np.asarray(Tm); Teff = np.asarray(Teff)
    Rsc = np.asarray(Rsc); F = np.asarray(F)
    g = np.stack([np.asarray(gf(p)) for p in pts])
    That_m = np.stack([vm.eulerian_that(g[i], Tm[i]) for i in range(len(pts))])
    That_e = np.stack([vm.eulerian_that(g[i], Teff[i]) for i in range(len(pts))])
    mm = vm.hawking_ellis_margins(That_m)
    me = vm.hawking_ellis_margins(That_e)
    scale_e = float(np.max(np.abs(That_e)))
    out = {'v_s': v_s, 'R': R, 'Delta': Delta, 'aA': aA, 'aC': aC, 'eta': eta,
           'alpha': alpha,
           'm_nec': float(np.min(mm['nec'])), 'm_wec': float(np.min(mm['wec'])),
           'm_sec': float(np.min(mm['sec'])), 'm_dec': float(np.min(mm['dec'])),
           'typeI_frac_m': float(np.mean(mm['typeI'])),
           'eff_nec_min': float(np.min(me['nec'])),
           'eff_scale': scale_e,
           'F_min': float(np.min(F)), 'F_max': float(np.max(F)),
           'R_absmax': float(np.max(np.abs(Rsc)))}
    out['worst_m'] = min(out['m_nec'], out['m_wec'], out['m_sec'], out['m_dec'])
    out['J'] = out['worst_m'] / scale_e if scale_e > 0 else 0.0
    return out


# ---------------------------------------------------------------- fast path
def g_of_p(p, xyz):
    """Metric with parameters as a traced vector p=(v_s,R,Delta,aA,aC,eta)."""
    v_s, R, Delta, aA, aC, eta = p[0], p[1], p[2], p[3], p[4], p[5]
    sig = 1.0 / Delta
    den = 2.0 * jnp.tanh(sig * R)
    X, y, z = xyz
    r = jnp.sqrt(X ** 2 + y ** 2 + z ** 2 + 1e-24)
    n = xyz / r
    f = (jnp.tanh(sig * (r + R)) - jnp.tanh(sig * (r - R))) / den
    fp = sig * (1.0 / jnp.cosh(sig * (r + R)) ** 2
                - 1.0 / jnp.cosh(sig * (r - R)) ** 2) / den
    bump = jnp.exp(-(((r - R) / Delta) ** 2))
    lapse = jnp.exp(aA * bump)
    psi4 = jnp.exp(4.0 * aC * bump)
    beta_irr = v_s * ((1.0 - f) * jnp.array([1.0, 0.0, 0.0]) - X * fp * n)
    beta_alc = jnp.array([v_s * (1.0 - f), 0.0, 0.0])
    beta = (1.0 - eta) * beta_irr + eta * beta_alc
    g = jnp.zeros((4, 4))
    g = g.at[0, 0].set(-lapse ** 2 + psi4 * (beta @ beta))
    g = g.at[0, 1:].set(psi4 * beta)
    g = g.at[1:, 0].set(psi4 * beta)
    g = g.at[1:, 1:].set(psi4 * jnp.eye(3))
    return g


def _tensors_p(p, xyz, alpha):
    gf = lambda q: g_of_p(p, q)
    return tensors_at_point(gf, xyz, alpha)


_batch = jax.jit(lambda p, alpha, pts: jax.vmap(lambda x: _tensors_p(p, x, alpha))(pts))
_gbatch = jax.jit(lambda p, pts: jax.vmap(lambda x: g_of_p(p, x))(pts))


def audit_config_fast(v_s, R, Delta, aA, aC, eta, alpha, pts):
    p = jnp.array([v_s, R, Delta, aA, aC, eta])
    Tm, Teff, Rsc, F = _batch(p, float(alpha), jnp.asarray(pts))
    Tm = np.asarray(Tm); Teff = np.asarray(Teff)
    Rsc = np.asarray(Rsc); F = np.asarray(F)
    g = np.asarray(_gbatch(p, jnp.asarray(pts)))
    That_m = np.stack([vm.eulerian_that(g[i], Tm[i]) for i in range(len(pts))])
    That_e = np.stack([vm.eulerian_that(g[i], Teff[i]) for i in range(len(pts))])
    mm = vm.hawking_ellis_margins(That_m)
    me = vm.hawking_ellis_margins(That_e)
    scale_e = float(np.max(np.abs(That_e)))
    out = {'v_s': v_s, 'R': R, 'Delta': Delta, 'aA': aA, 'aC': aC, 'eta': eta,
           'alpha': alpha,
           'm_nec': float(np.min(mm['nec'])), 'm_wec': float(np.min(mm['wec'])),
           'm_sec': float(np.min(mm['sec'])), 'm_dec': float(np.min(mm['dec'])),
           'typeI_frac_m': float(np.mean(mm['typeI'])),
           'eff_nec_min': float(np.min(me['nec'])),
           'eff_scale': scale_e,
           'F_min': float(np.min(F)), 'F_max': float(np.max(F)),
           'R_absmax': float(np.max(np.abs(Rsc)))}
    out['worst_m'] = min(out['m_nec'], out['m_wec'], out['m_sec'], out['m_dec'])
    out['J'] = out['worst_m'] / scale_e if scale_e > 0 else 0.0
    return out


def sample_points(R, Delta):
    dirs = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1],
                     [0, 0, -1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]],
                    dtype=float)
    dirs = dirs / np.linalg.norm(dirs, axis=1)[:, None]
    # NOTE: innermost radius 0.1R, never the exact origin: radial profiles
    # with exponentially small nonzero slope at r=0 (Gaussian bumps) make
    # bump(|x|) only C0 at the centre, and 4th-order AD amplifies that
    # microscopic cusp into a fake curvature spike (observed R ~ 1e7).
    # At r >= 0.1R the cusp contribution is < 1e-3 of wall scales.
    rad = np.array([0.1 * R, 0.3 * R, 0.5 * R, R - 1.5 * Delta, R - 0.75 * Delta,
                    R - 0.25 * Delta, R, R + 0.25 * Delta, R + 0.75 * Delta,
                    R + 1.5 * Delta, 1.3 * R, 1.6 * R])
    rad = rad[rad > 0]
    pts = []
    for r in rad:
        pts.extend(dirs * r)
    return np.array(pts)
