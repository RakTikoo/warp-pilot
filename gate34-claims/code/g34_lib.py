#!/usr/bin/env python3
"""
g34_lib.py -- Gate-34's OWN machinery for the extended class.

Written fresh for this gate; imports NOTHING from p312_lib /
p308_lib. Organisation: the metric is differentiated by
chain-rule derivative operators (d_k r = n_k,
d_k n_i = P_ki / r, d_k F(r) = F' n_k for each profile F),
and the Einstein tensor is assembled by einsum tensor
calculus. Profiles are re-implemented from their
registered definitions:

  S(r): S_{2,2} = 1 - I_u(3,3), u = (r-10)/10 on (10,20)
        (incomplete-beta form, p258_lib's registered form);
  N(r): 1 + A * B_plat(c=15, W=5, e=3), B = H(x) H(y) with
        H the quintic smoothstep (p274_lib's registered form);
  M(r): broad ramp, M = 1 + m0 [U(r;10.5,19.5) - U(r;21,24)],
        U = SS((r-a)/(b-a)), SS the quintic smoothstep
        (Phase 312's registered profile), m0 = +1.0.

Metric (stationary, Cartesian):
  g_tt = -N^2,  g_ti = -beta * S * delta_i1,
  gamma_ij = delta_ij + (M-1) n_i n_j.
float64. Programme venv.
"""
import numpy as np
from scipy.special import betainc, beta as beta_fn
from scipy.optimize import minimize

DTYPE = np.float64
BETA = 1.1
A_LAPSE = 0.07439108177516472
M0 = 1.0
R1_RAMP, R2_RAMP = 10.5, 19.5
EIGHT_PI = 8.0 * np.pi


# ------------------------------------------------------------- profiles
def _ss(x):
    """Quintic smoothstep SS and derivatives (value, 1st, 2nd)."""
    x = np.asarray(x, dtype=DTYPE)
    v = 6.0 * x**5 - 15.0 * x**4 + 10.0 * x**3
    d1 = 30.0 * x**4 - 60.0 * x**3 + 30.0 * x**2
    d2 = 120.0 * x**3 - 180.0 * x**2 + 60.0 * x
    return v, d1, d2


def _U(r, a, b):
    """(U, U', U'') for U(r;a,b) = SS((r-a)/(b-a)) on [a,b]."""
    r = np.asarray(r, dtype=DTYPE)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r); Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, d1, d2 = _ss(x)
        U[mid] = v; Up[mid] = d1 / (b - a); Upp[mid] = d2 / (b - a) ** 2
    return U, Up, Upp


def M_jet(r, m0=M0):
    """(M, M', M'') for the broad-ramp profile."""
    U1, U1p, U1pp = _U(r, R1_RAMP, R2_RAMP)
    U2, U2p, U2pp = _U(r, 21.0, 24.0)
    return (1.0 + m0 * (U1 - U2), m0 * (U1p - U2p),
            m0 * (U1pp - U2pp))


def S_jet(r, a=2.0, b=2.0):
    """(S, S', S'') for S_{a,b} = 1 - I_u(a+1, b+1), u=(r-10)/10."""
    r = np.asarray(r, dtype=DTYPE)
    S = np.ones_like(r); Sp = np.zeros_like(r); Spp = np.zeros_like(r)
    S = np.where(r >= 20.0, 0.0, S)
    m = (r > 10.0) & (r < 20.0)
    if np.any(m):
        u = (r[m] - 10.0) / 10.0
        B = beta_fn(a + 1.0, b + 1.0)
        S[m] = 1.0 - betainc(a + 1.0, b + 1.0, u)
        f = u ** a * (1.0 - u) ** b
        Sp[m] = -f / (10.0 * B)
        with np.errstate(divide='ignore', invalid='ignore'):
            fp = (u ** (a - 1.0) * (1.0 - u) ** (b - 1.0)
                  * (a * (1.0 - u) - b * u))
        fp = np.where(np.isfinite(fp), fp, 0.0)
        Spp[m] = -fp / (100.0 * B)
    return S, Sp, Spp


def _H(t):
    """Quintic step H and derivatives: 10t^3-15t^4+6t^5 on (0,1)."""
    t = np.asarray(t, dtype=DTYPE)
    v = np.where(t >= 1.0, 1.0, 0.0)
    d1 = np.zeros_like(t); d2 = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    if np.any(m):
        tm = t[m]
        v[m] = 10.0 * tm**3 - 15.0 * tm**4 + 6.0 * tm**5
        d1[m] = 30.0 * tm**2 * (1.0 - tm) ** 2
        d2[m] = 60.0 * tm * (1.0 - tm) * (1.0 - 2.0 * tm)
    return v, d1, d2


def N_jet(r, A=A_LAPSE, c=15.0, W=5.0, e=3.0):
    """(N, N', N'') for N = 1 + A * B_plat(c, W, e)."""
    r = np.asarray(r, dtype=DTYPE)
    r1 = c - W; r2 = c + W
    x = (r - r1) / e; y = (r2 - r) / e
    Hx, Hpx, Hppx = _H(x)
    Hy, Hpy, Hppy = _H(y)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / e
    Bpp = (Hppx * Hy - 2.0 * Hpx * Hpy + Hx * Hppy) / e ** 2
    return 1.0 + A * B, A * Bp, A * Bpp


def profiles_at(pts, m0=M0):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    S, Sp, Spp = S_jet(r)
    N, Np, Npp = N_jet(r)
    M, Mp, Mpp = M_jet(r, m0)
    return r, S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


# ------------------------------------------------- metric + derivatives
def metric_only(pts, m0=M0):
    """g_ab at pts (values only; for the FD guard)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rsafe[:, None], 0.0)
    S, _, _ = S_jet(r)
    N, _, _ = N_jet(r)
    M, _, _ = M_jet(r, m0)
    P = len(pts)
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -N ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + (M - 1.0) * n[:, i] * n[:, j])
    return g


def metric_jets(pts, m0=M0):
    """(g, dg, ddg): dg[:,k,a,b] = d_k g_ab (k spatial 0..2,
    time derivatives zero), ddg[:,l,k,a,b] = d_l d_k g_ab.
    Built by the derivative-operator rules stated in the
    module docstring."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    r, S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = profiles_at(pts, m0)
    rsafe = np.where(r > 0, r, 1.0)
    n = np.where(r[:, None] > 0, pts / rsafe[:, None], 0.0)
    h = M - 1.0
    # P_ki = delta_ki - n_k n_i  -> Pm[:,k,i]
    Pm = np.zeros((P, 3, 3), dtype=DTYPE)
    for k in range(3):
        for i in range(3):
            Pm[:, k, i] = (1.0 if k == i else 0.0) - n[:, k] * n[:, i]
    # dn[:,k,i] = d_k n_i = Pm[:,k,i] / r
    # ddn[:,l,k,i] = d_l d_k n_i
    #   = -(P_lk n_i + n_k P_li + n_l P_ki) / r^2
    dn = Pm / rsafe[:, None, None]
    ddn = np.zeros((P, 3, 3, 3), dtype=DTYPE)
    for l in range(3):
        for k in range(3):
            for i in range(3):
                ddn[:, l, k, i] = -(Pm[:, l, k] * n[:, i]
                                    + n[:, k] * Pm[:, l, i]
                                    + n[:, l] * Pm[:, k, i]) / rsafe ** 2
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    dg = np.zeros((P, 3, 4, 4), dtype=DTYPE)
    ddg = np.zeros((P, 3, 3, 4, 4), dtype=DTYPE)
    v = BETA * S
    # --- g_00 = -N^2
    g[:, 0, 0] = -N ** 2
    for k in range(3):
        dg[:, k, 0, 0] = -2.0 * N * Np * n[:, k]
        for l in range(3):
            ddg[:, l, k, 0, 0] = (
                -2.0 * (Np ** 2 + N * Npp) * n[:, l] * n[:, k]
                - 2.0 * N * Np * Pm[:, l, k] / rsafe)
    # --- g_0i = -v delta_i1 (only i=0 spatial, i.e. coord 1)
    g[:, 0, 1] = g[:, 1, 0] = -v
    for k in range(3):
        dg[:, k, 0, 1] = dg[:, k, 1, 0] = -BETA * Sp * n[:, k]
        for l in range(3):
            val = -BETA * (Spp * n[:, l] * n[:, k]
                           + Sp * Pm[:, l, k] / rsafe)
            ddg[:, l, k, 0, 1] = ddg[:, l, k, 1, 0] = val
    # --- gamma_ij = delta_ij + h n_i n_j
    # d_k gamma_ij = Mp n_k n_i n_j + h (dn_ki n_j + n_i dn_kj)
    # (dn already carries the 1/r)
    dgam = (Mp[:, None, None, None] * n[:, :, None, None]
            * n[:, None, :, None] * n[:, None, None, :])
    for k in range(3):
        for i in range(3):
            for j in range(3):
                dgam[:, k, i, j] += h * (dn[:, k, i] * n[:, j]
                                         + n[:, i] * dn[:, k, j])
    # d_l d_k gamma_ij =
    #   Mpp n_l n_k n_i n_j
    #   + Mp [ ddn_lk,i n_j + dn_ki dn_lj + dn_li dn_kj ... ]
    # expanded term by term below from differentiating dgam:
    #   d_l (Mp n_k n_i n_j) = Mpp n_l n_k n_i n_j
    #       + Mp (dn_lk n_i n_j + n_k dn_li n_j + n_k n_i dn_lj)
    #   d_l (h dn_ki n_j) = Mp n_l dn_ki n_j + h (ddn_l,ki n_j
    #       + dn_ki dn_lj)
    #   d_l (h n_i dn_kj) = Mp n_l n_i dn_kj + h (dn_li dn_kj
    #       + n_i ddn_l,kj)
    ddgam = np.zeros((P, 3, 3, 3, 3), dtype=DTYPE)
    for l in range(3):
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    ddgam[:, l, k, i, j] = (
                        Mpp * n[:, l] * n[:, k] * n[:, i] * n[:, j]
                        + Mp * (dn[:, l, k] * n[:, i] * n[:, j]
                                + n[:, k] * dn[:, l, i] * n[:, j]
                                + n[:, k] * n[:, i] * dn[:, l, j])
                        + Mp * n[:, l] * dn[:, k, i] * n[:, j]
                        + h * (ddn[:, l, k, i] * n[:, j]
                               + dn[:, k, i] * dn[:, l, j])
                        + Mp * n[:, l] * n[:, i] * dn[:, k, j]
                        + h * (dn[:, l, i] * dn[:, k, j]
                               + n[:, i] * ddn[:, l, k, j]))
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = ((1.0 if i == j else 0.0)
                                  + h * n[:, i] * n[:, j])
            dg[:, :, 1 + i, 1 + j] = dgam[:, :, i, j]
            ddg[:, :, :, 1 + i, 1 + j] = ddgam[:, :, :, i, j]
    return g, dg, ddg


def einstein(pts, m0=M0):
    """(T, g): T = G_ab / (8 pi) from metric_jets by einsum
    tensor calculus. dg4[:,d,a,b] with d=0 (time) zero."""
    g, dg3, ddg3 = metric_jets(pts, m0)
    P = len(g)
    dg = np.zeros((P, 4, 4, 4), dtype=DTYPE)       # dg[:,d,a,b]
    ddg = np.zeros((P, 4, 4, 4, 4), dtype=DTYPE)    # ddg[:,e,d,a,b]
    dg[:, 1:, :, :] = dg3
    ddg[:, 1:, 1:, :, :] = ddg3
    ginv = np.linalg.inv(g)
    # Gamma^a_bc = 1/2 g^ad (d_b g_dc + d_c g_db - d_d g_bc)
    Gam = 0.5 * (np.einsum('pad,pbdc->pabc', ginv, dg)
                 + np.einsum('pad,pcdb->pabc', ginv, dg)
                 - np.einsum('pad,pdbc->pabc', ginv, dg))
    # d_e ginv^ab = -ginv^ad (d_e g_dc) ginv^cb
    dginv = -np.einsum('pad,pedc,pcb->peab', ginv, dg, ginv)
    # d_e Gamma^a_bc
    dGam = (0.5 * (np.einsum('pead,pbdc->peabc', dginv, dg)
                   + np.einsum('pead,pcdb->peabc', dginv, dg)
                   - np.einsum('pead,pdbc->peabc', dginv, dg))
            + 0.5 * (np.einsum('pad,pebdc->peabc', ginv, ddg)
                     + np.einsum('pad,pecdb->peabc', ginv, ddg)
                     - np.einsum('pad,pedbc->peabc', ginv, ddg)))
    # R_bd = d_a Gam^a_bd - d_d Gam^a_ba + Gam^a_ae Gam^e_bd
    #        - Gam^a_de Gam^e_ba
    Ric = (np.einsum('paabd->pbd', dGam)
           - np.einsum('pdaba->pbd', dGam)
           + np.einsum('paae,pebd->pbd', Gam, Gam)
           - np.einsum('pade,peba->pbd', Gam, Gam))
    Rs = np.einsum('pab,pab->p', ginv, Ric)
    G = Ric - 0.5 * Rs[:, None, None] * g
    return G / EIGHT_PI, g


# ------------------------------------------------------- Eulerian frame
def eulerian_that(g, T):
    """ADM Eulerian orthonormal frame (definition as in
    verify_metric): e_0 = unit normal; spatial triad from
    the eigendecomposition of gamma. Gate's own code."""
    g = np.asarray(g, dtype=DTYPE)
    T = np.asarray(T, dtype=DTYPE)
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...',
                                       beta_cov, beta_up)
    alpha = np.sqrt(np.maximum(alpha2, 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros(g.shape[:-2] + (4, 4), dtype=DTYPE)
    E[..., 0, 0] = 1.0 / alpha
    E[..., 1:, 0] = -beta_up / alpha[..., None]
    for i in range(3):
        E[..., 1:, i + 1] = (V[..., :, i]
                             / np.sqrt(lam[..., i])[..., None])
    That = np.einsum('...ma,...nb,...mn->...ab', E, E, T)
    return 0.5 * (That + np.swapaxes(That, -1, -2))


def rho_normal(T, g):
    """rho = T_ab n^a n^b with n the ADM unit normal
    (frame-free cross-check of That[0,0])."""
    gamma = g[..., 1:, 1:]
    beta_cov = g[..., 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('...ij,...j->...i', gamma_inv, beta_cov)
    alpha2 = -g[..., 0, 0] + np.einsum('...i,...i->...',
                                       beta_cov, beta_up)
    alpha = np.sqrt(alpha2)
    nvec = np.zeros(g.shape[:-2] + (4,), dtype=DTYPE)
    nvec[..., 0] = 1.0 / alpha
    nvec[..., 1:] = -beta_up / alpha[..., None]
    return np.einsum('...a,...b,...ab->...', nvec, nvec, T)


# ------------------------------------------------------------ reads
def fib_dirs(npts):
    """The protocol's Fibonacci sphere (p2352_run form)."""
    i = np.arange(npts, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi), np.cos(phi)],
                    axis=1)


R_NODES = 10.0 + (np.arange(41, dtype=DTYPE) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)
DIRS642 = fib_dirs(642)

ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def typeI_flag(That):
    """Hawking-Ellis Type-I test (eigenvalue form): real
    spectrum of eta*T with exactly one timelike
    eigenvector. Gate's own implementation."""
    That = np.asarray(That, dtype=DTYPE)
    flat = That.reshape(-1, 4, 4)
    M = flat.copy()
    M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    return (real_ok & (cand.sum(axis=1) == 1)).reshape(
        That.shape[:-2])


def worst_null(That, polish=True):
    """Exact pointwise NEC minimum: min over unit spatial
    n of That(k,k), k = (1, n). fib(642) scan + NM polish.
    Returns (n_best, value)."""
    That = np.asarray(That, dtype=DTYPE)

    def q_of(n):
        k = np.concatenate([[1.0], n])
        return float(k @ That @ k)

    K = np.concatenate([np.ones((len(DIRS642), 1)), DIRS642], axis=1)
    vals = np.einsum('ni,ij,nj->n', K, That, K)
    n_best = DIRS642[int(np.argmin(vals))]
    val_best = float(np.min(vals))
    if not polish:
        return n_best, val_best
    th0 = np.arccos(np.clip(n_best[2], -1, 1))
    ph0 = np.arctan2(n_best[1], n_best[0])

    def obj(x):
        th, ph = x
        n = np.array([np.sin(th) * np.cos(ph),
                      np.sin(th) * np.sin(ph), np.cos(th)])
        return q_of(n)
    res = minimize(obj, np.array([th0, ph0]), method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10,
                            'fatol': 1e-14})
    th, ph = res.x
    n_fin = np.array([np.sin(th) * np.cos(ph),
                      np.sin(th) * np.sin(ph), np.cos(th)])
    v_fin = float(obj(res.x))
    if v_fin < val_best:
        return n_fin, v_fin
    return n_best, val_best


def nec_exact_eig(That):
    """Exact pointwise NEC min for Type-I points from the
    eigen-decomposition in the tensor's own frame is NOT
    That(k,k) in the Eulerian frame; this helper instead
    returns the fib(642) contraction min (unpolished) --
    used only as the dense-scan general read."""
    K = np.concatenate([np.ones((len(DIRS642), 1)), DIRS642], axis=1)
    vals = np.einsum('ni,ij,nj->n', K, np.asarray(That), K)
    return float(np.min(vals))


# ------------------------------------------------------------ R/QK split
def rho_split(pts, m0=M0):
    """Phase 308 Item-1 split, re-implemented from the
    registered formula:
      16 pi rho = R + Q_K,
      R  = (2/r^2)(1 - 1/M) + 2 M'/(r M^2)   [= R1 + R2],
      Q_K = (beta^2/alpha^2)[ -S'^2 (1-C^2)/(2M)
            - 4(M-1) S S' C^2/(r M^2)
            + 2(M-1)^2 S^2 C^2/(r^2 M^2)
            + 2(M-1) M' S^2 C^2/(r M^3) ],
      alpha^2 = N^2 + beta^2 S^2 (1 - ((M-1)/M) C^2),
      C = n_xhat.  Returns *_over_16pi arrays."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    C = pts[:, 0] / r
    _, S, Sp, _, N, _, _, M, Mp, _ = profiles_at(pts, m0)
    R1 = (2.0 / r ** 2) * (1.0 - 1.0 / M)
    R2 = 2.0 * Mp / (r * M ** 2)
    R = R1 + R2
    alpha2 = N ** 2 + BETA ** 2 * S ** 2 * (1.0 - ((M - 1.0) / M)
                                            * C ** 2)
    bracket = (-Sp ** 2 * (1.0 - C ** 2) / (2.0 * M)
               - 4.0 * (M - 1.0) * S * Sp * C ** 2 / (r * M ** 2)
               + 2.0 * (M - 1.0) ** 2 * S ** 2 * C ** 2
               / (r ** 2 * M ** 2)
               + 2.0 * (M - 1.0) * Mp * S ** 2 * C ** 2
               / (r * M ** 3))
    QK = BETA ** 2 / alpha2 * bracket
    d = 16.0 * np.pi
    return {'R_over_16pi': R / d, 'R1_over_16pi': R1 / d,
            'R2_over_16pi': R2 / d, 'QK_over_16pi': QK / d,
            'rho_split': (R + QK) / d, 'M': M, 'Mp': Mp}
