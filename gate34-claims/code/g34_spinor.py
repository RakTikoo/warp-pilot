#!/usr/bin/env python3
"""
g34_spinor.py -- Gate-34's own Dirac stress machinery,
written from the field definitions.

Field: psi(x) = sum_j U(p_j, chi_j) exp(i p_j . x) at
t = 0, with U the positive-frequency Dirac spinor for
momentum p_j, mass m, 2-spinor chi_j (amplitude folded
into chi), Dirac representation gamma matrices.
On shell: E_j = sqrt(|p_j|^2 + m^2); the full phase is
exp(i(p.x - E t)), so d_0 psi = -i E psi-contributions
and d_i psi = +i p_i psi-contributions, i.e.
d_a psi = sum_j (-i p_a) c_j U_j with p_a = (E, -p_vec)
covariant and c_j = exp(i p_j . x).

Stress (symmetrised Dirac form, Phases 253/257 form):
  T_ab = (i/4) [ psibar gamma_a D_b psi
               + psibar gamma_b D_a psi
               - (D_a psibar) gamma_b psi
               - (D_b psibar) gamma_a psi ],
gamma_a covariant, psibar = psi^dagger gamma^0.
Residual per site (definitional): R_s = ||T_fit - That||_F
(full 4x4 Frobenius, direct path).
"""
import numpy as np

DTYPE = np.float64
_s1 = np.array([[0, 1], [1, 0]], dtype=complex)
_s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
_s3 = np.array([[1, 0], [0, -1]], dtype=complex)
_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)
GAMMA = [np.block([[_I2, _Z2], [_Z2, -_I2]])] + [
    np.block([[_Z2, s], [-s, _Z2]]) for s in (_s1, _s2, _s3)]
GAMMA_COV = [GAMMA[0], -GAMMA[1], -GAMMA[2], -GAMMA[3]]
ETA = np.diag([1.0, -1.0, -1.0, -1.0])


def u_spinor(pvec, m, chi):
    pvec = np.asarray(pvec, dtype=DTYPE)
    E = np.sqrt(pvec @ pvec + m * m)
    denom = np.sqrt(E + m) if m != 0.0 else np.sqrt(E)
    top = denom * chi
    bot = ((_s1 * pvec[0] + _s2 * pvec[1] + _s3 * pvec[2])
           @ chi) / denom
    return np.concatenate([top, bot]), E


def dirac_residual(u, pvec, m):
    E = np.sqrt(pvec @ pvec + m * m)
    p = np.concatenate([[E], pvec])
    pcov = ETA @ p
    slash = sum(GAMMA[a] * pcov[a] for a in range(4))
    return slash @ u - m * u


def stress_at(pvecs, chis, m, x):
    """Direct-path T_ab of the superposition at point x
    (t = 0). pvecs (N,3), chis (N,2) complex."""
    pvecs = np.asarray(pvecs, dtype=DTYPE)
    N = len(pvecs)
    Us = []
    Es = []
    for j in range(N):
        U, E = u_spinor(pvecs[j], m, chis[j])
        Us.append(U); Es.append(E)
    Us = np.array(Us)                                   # (N,4)
    phase = np.exp(1j * (pvecs @ np.asarray(x, dtype=DTYPE)))
    psi = phase @ Us                                    # (4,)
    # d_a psi: coefficients (-i p_a) with p_a = (E, -p)
    pcov = np.concatenate([np.array(Es)[:, None], -pvecs],
                            axis=1)                     # (N,4)
    dpsi = np.zeros((4, 4), dtype=complex)              # [a, comp]
    for a in range(4):
        dpsi[a] = ((-1j * pcov[:, a]) * phase) @ Us
    psibar = psi.conj() @ GAMMA[0]
    dpsibar = np.array([d.conj() @ GAMMA[0] for d in dpsi])
    T = np.zeros((4, 4), dtype=DTYPE)
    for a in range(4):
        for b in range(4):
            val = (1j / 4.0) * (
                psibar @ GAMMA_COV[a] @ dpsi[b]
                + psibar @ GAMMA_COV[b] @ dpsi[a]
                - dpsibar[a] @ GAMMA_COV[b] @ psi
                - dpsibar[b] @ GAMMA_COV[a] @ psi)
            T[a, b] = float(val.real)
    return T


def pairwise_S(pvecs, chis, m):
    """Polarised bilinear S_ij for mode pairs (gate's own
    implementation of the plane-wave polarisation algebra):
    for psi = sum_j c_j U_j e^{i p_j x}, the symmetrised
    stress is sesquilinear, T = sum_ij c_i* S_ij c_j with
      S_ij = (1/4) [ (p_i + p_j) x J_ij + J_ij x (p_i + p_j) ]
    (outer products over the 4-vector index), where
    J_ij,b = ubar_i gamma_b U_j and p are covariant
    4-momenta (E, -p_vec). Validated against the direct
    builder in g34_item3.py before any fit uses it."""
    pvecs = np.asarray(pvecs, dtype=DTYPE)
    N = len(pvecs)
    Us = np.array([u_spinor(pvecs[j], m, chis[j])[0]
                   for j in range(N)])                  # (N,4)
    Es = np.sqrt(np.sum(pvecs ** 2, axis=1) + m * m)
    pcov = np.concatenate([Es[:, None], -pvecs], axis=1)  # (N,4)
    ubar = Us.conj() @ GAMMA[0]                           # (N,4)
    GC = np.array(GAMMA_COV)                              # (b,4,4)
    GU = np.einsum('bac,jc->bja', GC, Us)                 # gamma_b U_j
    J = np.einsum('ic,bjc->ijb', ubar, GU)                # (i,j,b)
    psum = pcov[:, None, :] + pcov[None, :, :]            # (i,j,a)
    S = 0.25 * (psum[:, :, :, None] * J[:, :, None, :]
                + J[:, :, :, None] * psum[:, :, None, :])
    return S                                              # (i,j,a,b)


def T_pairwise(S, pvecs, x):
    ph = np.exp(1j * (np.asarray(pvecs, dtype=DTYPE)
                      @ np.asarray(x, dtype=DTYPE)))
    return np.einsum('i,ijab,j->ab', ph.conj(), S, ph).real


IU = [(a, b) for a in range(4) for b in range(a, 4)]


def pack(pvecs, chis):
    parts = [np.asarray(pvecs, dtype=DTYPE).ravel()]
    chis = np.asarray(chis, dtype=complex)
    parts.append(chis.real.ravel())
    parts.append(chis.imag.ravel())
    return np.concatenate(parts)


def unpack(theta, N):
    theta = np.asarray(theta, dtype=DTYPE)
    pvecs = theta[:3 * N].reshape(N, 3)
    re = theta[3 * N:5 * N].reshape(N, 2)
    im = theta[5 * N:7 * N].reshape(N, 2)
    return pvecs, re + 1j * im


def resid_vec(theta, N, m, targets):
    """targets: list of (point, That, frob). Residual =
    10 upper-triangular components per site, normalised
    by the site's |That|_F (the protocol's optimiser
    residual; definitional reads are direct Frobenius).
    Uses the pairwise fast path (validated against the
    direct builder by the gate's C4 control)."""
    pvecs, chis = unpack(theta, N)
    S = pairwise_S(pvecs, chis, m)
    out = []
    for pt, That, frob in targets:
        T = T_pairwise(S, pvecs, pt)
        D = (T - That) / frob
        out.append(np.array([D[a, b] for a, b in IU]))
    return np.concatenate(out)


def direct_residuals(pvecs, chis, m, targets):
    Rs, rhos = [], []
    for pt, That, frob in targets:
        T = stress_at(pvecs, chis, m, pt)
        Rs.append(float(np.linalg.norm(T - That)))
        rhos.append(float(T[0, 0]))
    return Rs, rhos
