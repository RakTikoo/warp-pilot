"""Gate-54 machinery — written for this gate alone.

Organisation (deliberately NOT Phase 410's): the Dirac superposition
is evaluated as an explicit field function psi(X) with analytic
mode-by-mode derivatives; T_ab is assembled from the canonical
symmetrised formula with the Lagrangian density computed honestly.
No pairwise S-matrix / T_from_S path feeds any deciding read; a
separately written pairwise assembly is present ONLY as the C1
self-consistency cross-check.

Conventions: metric eta = diag(+,-,-,-); Dirac representation
gamma^0 = s3 (x) I2, gamma^i = i s2 (x) s_i (Kronecker products);
gamma_a = eta_aa gamma^a (no sum). Stored mode format: momentum
pvec (3,), two-spinor chi (2,) complex; mode spinor
u(p, chi) = ( sqrt(E+m) chi ; (sigma.p) chi / sqrt(E+m) ),
E = sqrt(|p|^2 + m^2), m = 1. Field at X = (t, x):
psi(X) = sum_j exp(-i E_j t + i p_j . x) u_j.
"""
import numpy as np

# ------------------------------------------------------------------
# Pauli matrices and gamma matrices via Kronecker products
# ------------------------------------------------------------------
_s1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
_s2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
_s3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
_I2 = np.eye(2, dtype=complex)
PAULI = (_s1, _s2, _s3)

GAMMA_UP = [np.kron(_s3, _I2)] + [np.kron(1.0j * _s2, s) for s in PAULI]
GAMMA_LO = [GAMMA_UP[0], -GAMMA_UP[1], -GAMMA_UP[2], -GAMMA_UP[3]]
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
IU = [(a, b) for a in range(4) for b in range(a, 4)]


def u_spinor(pvec, m, chi):
    """Plane-wave spinor for momentum pvec and two-spinor chi."""
    pvec = np.asarray(pvec, dtype=float)
    chi = np.asarray(chi, dtype=complex)
    E = float(np.sqrt(pvec @ pvec + m * m))
    sq = np.sqrt(E + m)
    sig_p = PAULI[0] * pvec[0] + PAULI[1] * pvec[1] + PAULI[2] * pvec[2]
    u = np.concatenate([sq * chi, (sig_p @ chi) / sq])
    return u, E


def mode_health(pvec, m, chi):
    """Return (u, E, |u^dag u - 2E|, max |(pslash - m) u|)."""
    u, E = u_spinor(pvec, m, chi)
    chi2 = float(np.vdot(np.asarray(chi, dtype=complex),
                         np.asarray(chi, dtype=complex)).real)
    norm_dev = abs(float(np.vdot(u, u).real) - 2.0 * E * chi2)
    p_up = np.concatenate([[E], np.asarray(pvec, dtype=float)])
    p_lo = ETA @ p_up
    # pslash = gamma^a p_a (contravariant gamma, covariant momentum)
    pslash = sum(p_lo[a] * GAMMA_UP[a] for a in range(4))
    dirac = float(np.max(np.abs(pslash @ u - m * u)))
    return u, E, norm_dev, dirac


class Field:
    """The superposition as an explicit field function of X = (t, x)."""

    def __init__(self, pvecs, avecs, m):
        self.pvecs = [np.asarray(p, dtype=float) for p in pvecs]
        self.m = float(m)
        self.us = []
        self.Es = []
        for pv, av in zip(self.pvecs, avecs):
            u, E = u_spinor(pv, self.m, av)
            self.us.append(u)
            self.Es.append(E)
        self.N = len(self.us)

    def _phase(self, j, X):
        return np.exp(-1.0j * self.Es[j] * X[0]
                      + 1.0j * float(self.pvecs[j] @ X[1:4]))

    def psi(self, X):
        out = np.zeros(4, dtype=complex)
        for j in range(self.N):
            out += self._phase(j, X) * self.us[j]
        return out

    def dpsi(self, X):
        """dpsi[a] = d_a psi(X), a = 0..3 (covariant derivative index)."""
        out = []
        for a in range(4):
            acc = np.zeros(4, dtype=complex)
            for j in range(self.N):
                pa = self.Es[j] if a == 0 else -self.pvecs[j][a - 1]
                acc += (-1.0j * pa) * self._phase(j, X) * self.us[j]
            out.append(acc)
        return out

    def stress(self, x_spatial):
        """Canonical T_ab at (t=0, x_spatial), with L computed honestly.

        T_ab = (i/2)[ psibar gamma_(a d_b) psi - (d_(a psibar) gamma_b) psi ]
               - eta_ab * L,   L = psibar (i gamma^c d_c - m) psi.
        """
        X = np.concatenate([[0.0], np.asarray(x_spatial, dtype=float)])
        psi = self.psi(X)
        dpsi = self.dpsi(X)
        psibar = psi.conj() @ GAMMA_UP[0]
        dpsibar = [d.conj() @ GAMMA_UP[0] for d in dpsi]
        # Lagrangian density (on shell it must come out ~0; computed, not assumed)
        slash_d = sum(GAMMA_UP[c] @ dpsi[c] for c in range(4))
        L = float((psibar @ (1.0j * slash_d - self.m * psi)).real)
        T = np.zeros((4, 4))
        for a in range(4):
            for b in range(4):
                t1 = psibar @ GAMMA_LO[a] @ dpsi[b] \
                    + psibar @ GAMMA_LO[b] @ dpsi[a]
                t2 = dpsibar[a] @ GAMMA_LO[b] @ psi \
                    + dpsibar[b] @ GAMMA_LO[a] @ psi
                T[a, b] = float((0.25j * (t1 - t2)).real)
        T = T - ETA * L
        return T, L, psi


def stress_field(pvecs, avecs, m, x_spatial):
    f = Field(pvecs, avecs, m)
    T, L, _ = f.stress(x_spatial)
    return T, L


# ------------------------------------------------------------------
# C1 cross-check ONLY: an independently written pairwise assembly.
# (Never feeds a deciding read.)
# ------------------------------------------------------------------
def stress_pairwise_check(pvecs, avecs, m, x_spatial):
    us, Es, pcovs = [], [], []
    for pv, av in zip(pvecs, avecs):
        u, E = u_spinor(pv, m, av)
        us.append(u)
        Es.append(E)
        pcovs.append(np.concatenate([[E], -np.asarray(pv, dtype=float)]))
    x = np.asarray(x_spatial, dtype=float)
    ph = [np.exp(1.0j * float(np.asarray(pv, dtype=float) @ x))
          for pv in pvecs]
    T = np.zeros((4, 4), dtype=complex)
    n = len(us)
    for i in range(n):
        ubar_i = us[i].conj() @ GAMMA_UP[0]
        for j in range(n):
            J = np.array([ubar_i @ GAMMA_LO[b] @ us[j] for b in range(4)])
            psum = pcovs[i] + pcovs[j]
            Sij = 0.25 * (np.outer(psum, J) + np.outer(J, psum))
            T += (ph[i].conjugate() * ph[j]) * Sij
    return T.real


# ------------------------------------------------------------------
# Hawking-Ellis type and eigen-channel decomposition (gate's own)
# ------------------------------------------------------------------
def segre_type(T):
    """Type from the mixed tensor M = eta T: real spectrum plus a
    timelike eigenvector with a well-conditioned eigenbasis -> I."""
    M = ETA @ np.asarray(T, dtype=float)
    ev, evec = np.linalg.eig(M)
    scale = max(1e-30, float(np.max(np.abs(ev))))
    max_im = float(np.max(np.abs(ev.imag))) if ev.size else 0.0
    out = {"eigs": ev, "max_abs_imag": max_im}
    if max_im > 1e-9 * scale and max_im > 1e-12:
        out["type"] = "IV"
        return out
    timelike = False
    for idx in range(4):
        v = evec[:, idx].real
        if float(v @ ETA @ v) > 1e-9 * float(v @ v):
            timelike = True
    out["timelike_eigenvector"] = timelike
    out["evec_cond"] = float(np.linalg.cond(evec))
    out["type"] = "I" if (timelike and out["evec_cond"] < 1e8) \
        else "II/III-degenerate"
    return out


def decompose(T, nhat):
    """Eigen-channel decomposition per Phase 410 SS4(ii) definitions,
    gate's own code. Returns dict with segre type, rho, pressures,
    channels, SEC_min, joint_min (channels only when Type-I)."""
    T = np.asarray(T, dtype=float)
    nhat = np.asarray(nhat, dtype=float)
    out = {"segre_type": segre_type(T)["type"],
           "rho": float(T[0, 0]),
           "flux_norm": float(np.linalg.norm(T[0, 1:4])),
           "components": {f"T{a}{b}": float(T[a, b]) for a, b in IU}}
    if out["segre_type"] != "I":
        return out
    ev, evec = np.linalg.eig(ETA @ T)
    ev = ev.real
    evec = evec.real
    tl = None
    for idx in range(4):
        v = evec[:, idx]
        if float(v @ ETA @ v) > 1e-9 * float(v @ v):
            tl = idx
    if tl is None:
        out["segre_type"] = "II/III-degenerate"
        return out
    rho = float(ev[tl])
    ps = []
    for idx in range(4):
        if idx == tl:
            continue
        v = evec[:, idx]
        sp = v[1:4]
        nrm = float(np.linalg.norm(sp))
        align = abs(float(sp @ nhat)) / nrm if nrm > 0 else 0.0
        ps.append({"p": float(-ev[idx]), "nhat_align": align})
    ir = int(np.argmax([p["nhat_align"] for p in ps]))
    p_r = ps[ir]["p"]
    p_ts = [ps[i]["p"] for i in range(3) if i != ir]
    chans = {"rho": rho, "p_r": p_r, "p_t": p_ts,
             "NEC_r": rho + p_r,
             "NEC_t": [rho + p for p in p_ts],
             "WEC": rho,
             "DEC_r": rho - abs(p_r),
             "DEC_t": [rho - abs(p) for p in p_ts],
             "DEC_flux": rho - out["flux_norm"],
             "SEC_trace": rho + p_r + sum(p_ts),
             "SEC_r": rho + p_r,
             "SEC_t": [rho + p for p in p_ts]}
    out["channels"] = chans
    out["SEC_min_channel"] = float(min(chans["SEC_trace"], chans["SEC_r"],
                                       min(chans["SEC_t"])))
    out["joint_min_channel"] = float(min(
        chans["NEC_r"], min(chans["NEC_t"]), chans["WEC"],
        chans["DEC_r"], min(chans["DEC_t"]), chans["DEC_flux"]))
    return out


# ------------------------------------------------------------------
# Residual map and FD Jacobians (gate's own, on the field-function path)
# ------------------------------------------------------------------
def unpack(theta, N):
    theta = np.asarray(theta, dtype=float)
    pvecs = theta[:3 * N].reshape(N, 3)
    avecs = (theta[3 * N:5 * N] + 1.0j * theta[5 * N:7 * N]).reshape(N, 2)
    return pvecs, avecs


def pack(pvecs, avecs):
    pvecs = np.asarray(pvecs, dtype=float)
    avecs = np.asarray(avecs, dtype=complex)
    return np.concatenate([pvecs.ravel(), avecs.real.ravel(),
                           avecs.imag.ravel()])


def make_resid(points, thats):
    """Normalised residual vector: per site, the 10 upper-triangular
    components of (T_sup - T_req)/||T_req||_F via the field path."""
    frobs = [float(np.linalg.norm(t)) for t in thats]
    ns = len(points)

    def resid_vec(theta, N, m):
        pvecs, avecs = unpack(theta, N)
        f = Field(pvecs, avecs, m)
        r = np.empty(10 * ns)
        for si in range(ns):
            T, _, _ = f.stress(points[si])
            d = (T - thats[si]) / frobs[si]
            r[si * 10:(si + 1) * 10] = np.array([d[a, b] for a, b in IU])
        return r
    return resid_vec


def fd_jacobian(resid_vec, theta, N, m, mode="central", hscale=1.0):
    theta = np.asarray(theta, dtype=float)
    npar = len(theta)
    f0 = resid_vec(theta, N, m) if mode == "forward" else None
    J = np.empty((len(resid_vec(theta, N, m)), npar))
    for j in range(npar):
        h = hscale * 1e-6 * max(1.0, abs(theta[j]))
        tp = theta.copy(); tp[j] += h
        if mode == "central":
            tm = theta.copy(); tm[j] -= h
            J[:, j] = (resid_vec(tp, N, m) - resid_vec(tm, N, m)) / (2.0 * h)
        else:
            J[:, j] = (resid_vec(tp, N, m) - f0) / h
    return J


def jacobian_report(resid_vec, theta, N, m, ns, mode="central", hscale=1.0):
    J = fd_jacobian(resid_vec, theta, N, m, mode=mode, hscale=hscale)
    sv = np.linalg.svd(J, compute_uv=False)
    blocks = {}
    for si in range(ns):
        svb = np.linalg.svd(J[si * 10:(si + 1) * 10, :], compute_uv=False)
        blocks[str(si)] = {
            "sigma_min": float(svb[-1]), "sigma_max": float(svb[0]),
            "rank_tol_1e-10_rel": int(np.sum(svb > 1e-10 * svb[0]))}
    return {"shape": [int(J.shape[0]), int(J.shape[1])],
            "singular_values": [float(v) for v in sv],
            "rank_tol_1e-10_rel": int(np.sum(sv > 1e-10 * sv[0])),
            "sigma_min": float(sv[-1]), "sigma_max": float(sv[0]),
            "per_site_blocks": blocks}
