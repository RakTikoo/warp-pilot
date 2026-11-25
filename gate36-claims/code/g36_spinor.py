"""Gate-36 Worker B: independent Dirac spinor builder (from the field definition).

Implements, from scratch (no imports of phase320/gate34 spinor code):
- Dirac-representation gamma matrices, mass m = 1.
- Mode spinors U(p, a) with folded 2-spinor amplitude a in C^2.
- Field psi(t=0, x) = sum_j exp(i p_j.x) U_j.
- Symmetrised Dirac stress tensor via two paths:
    (1) DIRECT: build psi and d_a psi at the point, contract.
    (2) PAIRWISE: T(x) = sum_ij conj(c_i) S_ij c_j.
- Packing theta = [p (3N), Re a (2N), Im a (2N)] (7N reals).
- Optimiser residual: per site, 10 upper-triangular components of
  (T_fit - That) / |That|_F, stacked (40 for 4 sites).
- Definitional residual per site: R = |T_fit - That|_F (direct path).
- Segre classifier from eigenvalues of eta.T.
- Central-FD Jacobian of the optimiser residual.
"""
import numpy as np

M_MASS = 1.0

# Pauli matrices
_S1 = np.array([[0, 1], [1, 0]], dtype=complex)
_S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
_S3 = np.array([[1, 0], [0, -1]], dtype=complex)
_SIGMA = [_S1, _S2, _S3]
_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)

# Dirac representation gamma^mu
GAMMA_UP = [
    np.block([[_I2, _Z2], [_Z2, -_I2]]),
    np.block([[_Z2, _S1], [-_S1, _Z2]]),
    np.block([[_Z2, _S2], [-_S2, _Z2]]),
    np.block([[_Z2, _S3], [-_S3, _Z2]]),
]
# Covariant gamma_a = (gamma^0, -gamma^i)
GAMMA_LO = [GAMMA_UP[0], -GAMMA_UP[1], -GAMMA_UP[2], -GAMMA_UP[3]]
ETA = np.diag([1.0, -1.0, -1.0, -1.0])

UPPER_IDX = [(a, b) for a in range(4) for b in range(a, 4)]  # 10 components


def spinor_U(p, a):
    """Positive-frequency spinor U(p, a); a in C^2 (amplitude folded in)."""
    p = np.asarray(p, dtype=float)
    a = np.asarray(a, dtype=complex)
    E = np.sqrt(np.dot(p, p) + M_MASS**2)
    s = np.sqrt(E + M_MASS)
    sp = sum(p[i] * _SIGMA[i] for i in range(3))
    U = np.empty(4, dtype=complex)
    U[:2] = s * a
    U[2:] = (sp @ a) / s
    return U, E


def modes_from_theta(theta, N):
    theta = np.asarray(theta, dtype=float)
    p = theta[:3 * N].reshape(N, 3)
    a = (theta[3 * N:5 * N] + 1j * theta[5 * N:7 * N]).reshape(N, 2)
    return p, a


def theta_from_modes(p, a):
    p = np.asarray(p, dtype=float)
    a = np.asarray(a, dtype=complex)
    return np.concatenate([p.ravel(), a.real.ravel(), a.imag.ravel()])


def build_modes(p, a):
    """Return lists: U_j (4,), E_j, p4cov_j = (E, -p)."""
    Us, Es, p4s = [], [], []
    for j in range(len(p)):
        U, E = spinor_U(p[j], a[j])
        Us.append(U)
        Es.append(E)
        p4s.append(np.array([E, -p[j][0], -p[j][1], -p[j][2]]))
    return Us, Es, p4s


# ---------------------------------------------------------------- DIRECT path
def T_direct(p, a, x):
    """Stress tensor at point x (t=0) by building psi and d_a psi."""
    x = np.asarray(x, dtype=float)
    Us, Es, p4s = build_modes(p, a)
    psi = np.zeros(4, dtype=complex)
    dpsi = np.zeros((4, 4), dtype=complex)  # dpsi[a] = d_a psi
    for j in range(len(p)):
        c = np.exp(1j * np.dot(p[j], x))
        psi += c * Us[j]
        for aa in range(4):
            dpsi[aa] += (-1j * p4s[j][aa]) * c * Us[j]
    psibar = psi.conj() @ GAMMA_UP[0]
    dbar = np.zeros((4, 4), dtype=complex)  # dbar[a] = d_a psibar (row)
    for aa in range(4):
        dbar[aa] = dpsi[aa].conj() @ GAMMA_UP[0]
    T = np.zeros((4, 4), dtype=complex)
    for aa in range(4):
        for bb in range(4):
            T[aa, bb] = (1j / 4.0) * (
                psibar @ GAMMA_LO[aa] @ dpsi[bb]
                + psibar @ GAMMA_LO[bb] @ dpsi[aa]
                - dbar[aa] @ GAMMA_LO[bb] @ psi
                - dbar[bb] @ GAMMA_LO[aa] @ psi
            )
    return T.real  # T is real for this construction (imag at round-off)


def T_direct_complex(p, a, x):
    """Same as T_direct but returns the raw complex tensor (for checks)."""
    x = np.asarray(x, dtype=float)
    Us, Es, p4s = build_modes(p, a)
    psi = np.zeros(4, dtype=complex)
    dpsi = np.zeros((4, 4), dtype=complex)
    for j in range(len(p)):
        c = np.exp(1j * np.dot(p[j], x))
        psi += c * Us[j]
        for aa in range(4):
            dpsi[aa] += (-1j * p4s[j][aa]) * c * Us[j]
    psibar = psi.conj() @ GAMMA_UP[0]
    dbar = np.zeros((4, 4), dtype=complex)
    for aa in range(4):
        dbar[aa] = dpsi[aa].conj() @ GAMMA_UP[0]
    T = np.zeros((4, 4), dtype=complex)
    for aa in range(4):
        for bb in range(4):
            T[aa, bb] = (1j / 4.0) * (
                psibar @ GAMMA_LO[aa] @ dpsi[bb]
                + psibar @ GAMMA_LO[bb] @ dpsi[aa]
                - dbar[aa] @ GAMMA_LO[bb] @ psi
                - dbar[bb] @ GAMMA_LO[aa] @ psi
            )
    return T


# -------------------------------------------------------------- PAIRWISE path
def pairwise_S(p, a):
    """S_ij[a,b] tensors: S_ij = 1/4[(p_i+p_j) x J_ij + J_ij x (p_i+p_j)],
    J_ij,b = Ubar_i gamma_b U_j, p covariant."""
    N = len(p)
    Us, Es, p4s = build_modes(p, a)
    Ubars = [U.conj() @ GAMMA_UP[0] for U in Us]
    S = np.zeros((N, N, 4, 4), dtype=complex)
    for i in range(N):
        for j in range(N):
            J = np.array([Ubars[i] @ GAMMA_LO[b] @ Us[j] for b in range(4)])
            psum = p4s[i] + p4s[j]
            S[i, j] = 0.25 * (np.outer(psum, J) + np.outer(J, psum))
    return S


def T_pairwise(p, a, x, S=None):
    x = np.asarray(x, dtype=float)
    if S is None:
        S = pairwise_S(p, a)
    c = np.exp(1j * (np.asarray(p, dtype=float) @ x))
    T = np.einsum('i,ijab,j->ab', c.conj(), S, c)
    return T.real


def T_pairwise_complex(p, a, x, S=None):
    x = np.asarray(x, dtype=float)
    if S is None:
        S = pairwise_S(p, a)
    c = np.exp(1j * (np.asarray(p, dtype=float) @ x))
    return np.einsum('i,ijab,j->ab', c.conj(), S, c)


# ------------------------------------------------------------------ residuals
def resid_vec(theta, N, sites, thats, frobs):
    """Optimiser residual: 10 upper-tri components per site / |That|_F."""
    p, a = modes_from_theta(theta, N)
    S = pairwise_S(p, a)
    out = np.empty(10 * len(sites))
    for s, (x, That) in enumerate(zip(sites, thats)):
        Tf = T_pairwise(p, a, x, S=S)
        d = (Tf - That) / frobs[s]
        out[10 * s:10 * s + 10] = [d[i, j] for (i, j) in UPPER_IDX]
    return out


def resid_vec_targets(theta, N, sites, thats, frobs):
    """Same residual but against arbitrary (e.g. perturbed) target tensors."""
    return resid_vec(theta, N, sites, thats, frobs)


def direct_residuals(p, a, sites, thats):
    Rs, rhos_fit, Ts_fit = [], [], []
    for x, That in zip(sites, thats):
        Tf = T_direct(p, a, x)
        Ts_fit.append(Tf)
        Rs.append(float(np.linalg.norm(Tf - That)))
        rhos_fit.append(float(Tf[0, 0]))
    return Rs, rhos_fit, Ts_fit


def pairwise_residuals(p, a, sites, thats):
    S = pairwise_S(p, a)
    Rs = []
    for x, That in zip(sites, thats):
        Tf = T_pairwise(p, a, x, S=S)
        Rs.append(float(np.linalg.norm(Tf - That)))
    return Rs


# --------------------------------------------------------------------- Segre
def segre_type(T):
    """Classify T (4x4 symmetric, covariant components as stored).

    Eigenvalues of eta.T: Type IV iff a complex pair (max|Im| above
    1e-9*scale and 1e-12); else Type I iff a timelike eigenvector exists
    and the eigenvector matrix is well-conditioned (cond < 1e8).
    Returns (label, info dict)."""
    T = np.asarray(T, dtype=float)
    M = ETA @ T
    w, V = np.linalg.eig(M)
    scale = max(float(np.max(np.abs(w))) if len(w) else 0.0, 1e-300)
    maxim = float(np.max(np.abs(w.imag)))
    info = {'eigvals': w, 'max_imag': maxim, 'scale': scale,
            'cond_V': None, 'has_timelike_eigvec': False}
    if maxim > 1e-9 * scale and maxim > 1e-12:
        return 'IV', info
    # all eigenvalues effectively real
    condV = float(np.linalg.cond(V))
    info['cond_V'] = condV
    has_tl = False
    for k in range(4):
        v = V[:, k]
        # eta-norm using Hermitian form (v real up to phase in type I)
        nrm = np.vdot(v, ETA @ v).real
        denom = np.vdot(v, v).real
        if denom > 0 and nrm / denom > 1e-9:
            has_tl = True
    info['has_timelike_eigvec'] = bool(has_tl)
    if has_tl and condV < 1e8:
        return 'I', info
    return 'other', info


# ------------------------------------------------------------------ Jacobian
def fd_jacobian(theta, N, sites, thats, frobs, h_rel=1e-6):
    """Central FD Jacobian of the optimiser residual.
    h_j = h_rel * max(1, |theta_j|). Returns (J, singular values)."""
    theta = np.asarray(theta, dtype=float)
    n = len(theta)
    J = np.empty((10 * len(sites), n))
    for j in range(n):
        h = h_rel * max(1.0, abs(theta[j]))
        tp = theta.copy(); tp[j] += h
        tm = theta.copy(); tm[j] -= h
        J[:, j] = (resid_vec(tp, N, sites, thats, frobs)
                   - resid_vec(tm, N, sites, thats, frobs)) / (2.0 * h)
    sv = np.linalg.svd(J, compute_uv=False)
    return J, sv


def dirac_residual(pj, U):
    """|slash(p) U - m U| with slash(p) = gamma^a p_a (covariant p)."""
    E = np.sqrt(np.dot(pj, pj) + M_MASS**2)
    p4 = np.array([E, -pj[0], -pj[1], -pj[2]])  # covariant p_a
    slash = sum(p4[a] * GAMMA_UP[a] for a in range(4))  # gamma^a p_a
    return float(np.linalg.norm(slash @ U - M_MASS * U))
