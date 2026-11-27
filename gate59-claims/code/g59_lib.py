"""g59_lib.py -- Gate-59's INDEPENDENT spinor-stress implementation.

Written from the definition, for the gate. No code from
p420_machinery.py / p430_* / p431_* is imported or reused; the
only shared objects are the stored records (matings, targets,
primaries), which are data.

Definition (the record's mating tensor, Gates 34/54/55 form):
  gamma matrices in the Dirac representation,
    gamma^0 = diag(I, -I),  gamma^i = [[0, sigma^i], [-sigma^i, 0]],
    gamma_a = eta_aa gamma^a (no sum),  eta = diag(1, -1, -1, -1).
  Positive-energy spinor for momentum p, mass m, 2-spinor chi:
    E = sqrt(|p|^2 + m^2),
    u = ( sqrt(E+m) chi ; (sigma.p) chi / sqrt(E+m) )   (m > 0)
    u = ( sqrt(E)   chi ; (sigma.p) chi / sqrt(E)   )   (m = 0)
  Field of a superposition at (x, t):
    psi = sum_k c_k u_k,   c_k = exp(i p_k . x - i E_k t),
    d_a psi = sum_k c_k (-i p^cov_a) u_k,
      p^cov = (E, -p)  (so d_0 -> -iE, d_i -> +i p_i).
  Stress (covariant components):
    T_ab = (i/4) [ psibar gamma_a d_b psi + psibar gamma_b d_a psi
                   - (d_a psibar) gamma_b psi
                   - (d_b psibar) gamma_a psi ],   psibar = psi^+ gamma^0,
  real by construction (the .real projection is applied as in
  the record; the imaginary residue is also returned by the
  raw routine for inspection).

Pair kernel (derived here from the bilinear, and validated
against the direct field path inside this module's self-test
and in g59_audit.py): with J_b^ij = ubar_i gamma_b u_j and
p^cov the covariant momenta,
  S_ij,ab = (1/4) [ (p_i + p_j)_a J_b^ij + (p_i + p_j)_b J_a^ij ],
  T_ab(x, t) = Re sum_ij conj(c_i) S_ij,ab c_j.
"""
import numpy as np

# ---- gamma matrices, Dirac representation (built here) ----
_s1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
_s2 = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
_s3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)
SIGMA = (_s1, _s2, _s3)
G_UP = [np.block([[_I2, _Z2], [_Z2, -_I2]])] + [
    np.block([[_Z2, s], [-s, _Z2]]) for s in SIGMA]
G_LO = [G_UP[0], -G_UP[1], -G_UP[2], -G_UP[3]]
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
IU = [(a, b) for a in range(4) for b in range(a, 4)]


def energies(pv, mm):
    pv = np.asarray(pv, dtype=float)
    mm = np.asarray(mm, dtype=float)
    return np.sqrt(np.sum(pv ** 2, axis=1) + mm ** 2)


def spinor(p, m, chi):
    """Positive-energy Dirac spinor; returns (u, E)."""
    p = np.asarray(p, dtype=float)
    chi = np.asarray(chi, dtype=complex)
    E = float(np.sqrt(p @ p + m * m))
    sp = SIGMA[0] * p[0] + SIGMA[1] * p[1] + SIGMA[2] * p[2]
    if m == 0.0:
        d = np.sqrt(E)
        u = np.concatenate([d * chi, (sp @ chi) / d])
    else:
        d = np.sqrt(E + m)
        u = np.concatenate([d * chi, (sp @ chi) / d])
    return u, E


def dirac_residual(p, m, chi):
    """|(gamma^a p_a - m) u|_inf with p_a = (E, -p)."""
    u, E = spinor(p, m, chi)
    pcov = np.concatenate([[E], -np.asarray(p, dtype=float)])
    slash = sum(G_UP[a] * pcov[a] for a in range(4))
    return float(np.max(np.abs(slash @ u - m * u)))


def _fields(pv, av, mm, x, t=0.0, E=None, factored_E=None):
    """psi and its four covariant derivatives at (x, t).

    factored_E: if given (a single float), every mode's time
    phase is the SAME float z = exp(-i E t) multiplied onto the
    spatial coefficient (the factored form; |z|^2 cancels in
    the bilinear). E: per-mode energy override array.
    """
    pv = np.asarray(pv, dtype=float)
    av = np.asarray(av, dtype=complex)
    mm = np.asarray(mm, dtype=float)
    x = np.asarray(x, dtype=float)
    Ek = energies(pv, mm) if E is None else np.asarray(E, dtype=float)
    psi = np.zeros(4, dtype=complex)
    dpsi = [np.zeros(4, dtype=complex) for _ in range(4)]
    z = None if factored_E is None else np.exp(-1j * factored_E * t)
    for k in range(len(pv)):
        u, _ = spinor(pv[k], float(mm[k]), av[k])
        c = np.exp(1j * float(pv[k] @ x))
        if factored_E is not None:
            c = c * z
        elif t != 0.0:
            c = c * np.exp(-1j * float(Ek[k]) * t)
        pcov = np.concatenate([[Ek[k]], -pv[k]])
        psi += c * u
        for a in range(4):
            dpsi[a] += c * (-1j * pcov[a]) * u
    return psi, dpsi


def T_field_raw(pv, av, mm, x, t=0.0, E=None, factored_E=None):
    """Complex T_ab from the field bilinear (imag part ~ 0)."""
    psi, dpsi = _fields(pv, av, mm, x, t=t, E=E,
                        factored_E=factored_E)
    psibar = psi.conj() @ G_UP[0]
    dpsibar = [d.conj() @ G_UP[0] for d in dpsi]
    T = np.zeros((4, 4), dtype=complex)
    for a in range(4):
        for b in range(4):
            T[a, b] = (1j / 4.0) * (
                psibar @ G_LO[a] @ dpsi[b]
                + psibar @ G_LO[b] @ dpsi[a]
                - dpsibar[a] @ G_LO[b] @ psi
                - dpsibar[b] @ G_LO[a] @ psi)
    return T


def T_field(pv, av, mm, x, t=0.0, E=None, factored_E=None):
    return T_field_raw(pv, av, mm, x, t=t, E=E,
                       factored_E=factored_E).real


def pair_kernel(pv, av, mm):
    """S[i, j, a, b] as derived in the module docstring."""
    pv = np.asarray(pv, dtype=float)
    av = np.asarray(av, dtype=complex)
    mm = np.asarray(mm, dtype=float)
    n = len(pv)
    Ek = energies(pv, mm)
    U = np.array([spinor(pv[k], float(mm[k]), av[k])[0]
                  for k in range(n)])                    # (n, 4)
    Ubar = U.conj() @ G_UP[0]                            # (n, 4)
    GU = np.einsum('bac,jc->bja', np.array(G_LO), U)     # gamma_b u_j
    J = np.einsum('ic,bjc->bij', Ubar, GU)               # J[b, i, j]
    pcov = np.concatenate([Ek[:, None], -pv], axis=1)   # (n, 4)
    psum = pcov[:, None, :] + pcov[None, :, :]           # (i, j, a)
    S = 0.25 * (psum[:, :, :, None] * J.transpose(1, 2, 0)[:, :, None, :]
                + J.transpose(1, 2, 0)[:, :, :, None]
                * psum[:, :, None, :])
    return S


def T_pair(S, pv, x, t=0.0, E=None, mm=None):
    pv = np.asarray(pv, dtype=float)
    x = np.asarray(x, dtype=float)
    Ek = (energies(pv, mm) if E is None
          else np.asarray(E, dtype=float))
    c = np.exp(1j * (pv @ x) - 1j * Ek * t)
    return np.einsum('i,ijab,j->ab', c.conj(), S, c).real


def site_residuals(pv, av, mm, XS, TG, path='field', t=0.0, E=None):
    """Per-site Frobenius residuals; returns (Rs, Ts)."""
    Rs, Ts = [], []
    S = pair_kernel(pv, av, mm) if path == 'pair' else None
    for si, x in enumerate(XS):
        if path == 'pair':
            T = T_pair(S, pv, x, t=t, E=E, mm=mm)
        else:
            T = T_field(pv, av, mm, x, t=t, E=E)
        Ts.append(T)
        Rs.append(float(np.linalg.norm(T - TG[si])))
    return Rs, Ts


def RF_grid_pair(S, pv, XS, TG, ts, E=None, mm=None):
    """R_F(t) = max_site ||T(t) - TG||_F on a time grid,
    pairwise form (vectorised over t)."""
    pv = np.asarray(pv, dtype=float)
    Ek = (energies(pv, mm) if E is None
          else np.asarray(E, dtype=float))
    ts = np.asarray(ts, dtype=float)
    dE = Ek[None, :] - Ek[:, None]                       # E_j - E_i
    RF = np.zeros(len(ts))
    for si, x in enumerate(XS):
        c0 = np.exp(1j * (pv @ np.asarray(x, dtype=float)))
        A = c0.conj()[:, None, None, None] * S * c0[None, :, None, None]
        ph = np.exp(-1j * ts[:, None, None] * dE[None, :, :])
        Tt = np.einsum('tij,ijab->tab', ph, A)
        res = np.linalg.norm(Tt - TG[si][None, :, :], axis=(1, 2))
        RF = np.maximum(RF, res)
    return RF


def price(av):
    av = np.asarray(av, dtype=complex)
    return float(np.sum(np.abs(av) ** 2))


def self_test():
    out = {}
    # Clifford algebra {gamma^a, gamma^b} = 2 eta^ab
    err = 0.0
    for a in range(4):
        for b in range(4):
            ac = G_UP[a] @ G_UP[b] + G_UP[b] @ G_UP[a]
            err = max(err, float(np.max(np.abs(
                ac - 2.0 * ETA[a, b] * np.eye(4)))))
    out['clifford_max_err'] = err
    # random superposition: field vs pair kernel, t = 0 and t != 0
    rng = np.random.default_rng(590431)
    n = 5
    pv = rng.normal(size=(n, 3))
    av = rng.normal(size=(n, 2)) + 1j * rng.normal(size=(n, 2))
    mm = np.array([1.0, 1.0, 0.0, 1.0, 0.0])
    x = rng.normal(size=3)
    S = pair_kernel(pv, av, mm)
    d0 = np.max(np.abs(T_field(pv, av, mm, x)
                       - T_pair(S, pv, x, mm=mm)))
    d1 = np.max(np.abs(T_field(pv, av, mm, x, t=0.731)
                       - T_pair(S, pv, x, t=0.731, mm=mm)))
    out['field_vs_pair_t0'] = float(d0)
    out['field_vs_pair_t'] = float(d1)
    out['dirac_resid_rand'] = max(
        dirac_residual(pv[k], float(mm[k]), av[k]) for k in range(n))
    # single mode: T stationary in t (closed form)
    T0 = T_field(pv[:1], av[:1], mm[:1], x)
    Tt = T_field(pv[:1], av[:1], mm[:1], x, t=3.7)
    out['single_mode_stationarity'] = float(np.max(np.abs(Tt - T0)))
    return out


if __name__ == '__main__':
    import json
    print(json.dumps(self_test(), indent=1))
