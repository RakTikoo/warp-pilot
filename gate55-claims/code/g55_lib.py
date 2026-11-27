"""Gate-55 machinery — written for this gate alone.

Organisation (deliberately NOT Phase 420's): the composite Dirac
superposition is evaluated as an explicit field function psi(X),
each mode carrying its own mass, with analytic mode-by-mode
derivatives. T_ab is the canonical symmetrised bilinear on the
total field — the object Phase 420's registration SS2 defines —
assembled directly from psi and dpsi. NO pairwise S-matrix feeds
any deciding read; a separately written pairwise assembly is
present ONLY as the C1 self-consistency cross-check.

Conventions: eta = diag(+,-,-,-); Dirac representation
gamma^0 = s3 (x) I2, gamma^i = i s2 (x) s_i (Kronecker products);
gamma_a = eta_aa gamma^a (no sum). Mode spinor
u(p, chi, m) = ( sqrt(E+m) chi ; (sigma.p) chi / sqrt(E+m) ),
E = sqrt(|p|^2 + m^2). Field at X = (t, x):
psi(X) = sum_j exp(-i E_j t + i p_j . x) u_j.
"""
import numpy as np

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
    """Plane-wave spinor for momentum pvec, mass m, two-spinor chi."""
    pvec = np.asarray(pvec, dtype=float)
    chi = np.asarray(chi, dtype=complex)
    E = float(np.sqrt(pvec @ pvec + m * m))
    sq = np.sqrt(E + m)
    sig_p = PAULI[0] * pvec[0] + PAULI[1] * pvec[1] + PAULI[2] * pvec[2]
    u = np.concatenate([sq * chi, (sig_p @ chi) / sq])
    return u, E


def mode_health(pvec, m, chi):
    """(u, E, |u^dag u - 2E|chi|^2|, max |(pslash - m) u|)."""
    u, E = u_spinor(pvec, m, chi)
    chi2 = float(np.vdot(np.asarray(chi, dtype=complex),
                         np.asarray(chi, dtype=complex)).real)
    norm_dev = abs(float(np.vdot(u, u).real) - 2.0 * E * chi2)
    p_lo = ETA @ np.concatenate([[E], np.asarray(pvec, dtype=float)])
    pslash = sum(p_lo[a] * GAMMA_UP[a] for a in range(4))
    dirac = float(np.max(np.abs(pslash @ u - m * u)))
    return u, E, norm_dev, dirac


class CompositeField:
    """Sum of Dirac plane-wave modes with per-mode masses."""

    def __init__(self, modes):
        """modes: list of (pvec(3,), chi(2,) complex, mass float)."""
        self.modes = []
        for pv, chi, m in modes:
            u, E = u_spinor(pv, float(m), chi)
            self.modes.append((np.asarray(pv, dtype=float), u, E))

    def psi(self, X):
        out = np.zeros(4, dtype=complex)
        for pv, u, E in self.modes:
            out += np.exp(-1.0j * E * X[0] + 1.0j * float(pv @ X[1:4])) * u
        return out

    def dpsi(self, X):
        """dpsi[a] = d/dX^a psi(X), a = 0..3."""
        out = []
        for a in range(4):
            acc = np.zeros(4, dtype=complex)
            for pv, u, E in self.modes:
                pa = E if a == 0 else -pv[a - 1]
                acc += (-1.0j * pa) * np.exp(
                    -1.0j * E * X[0] + 1.0j * float(pv @ X[1:4])) * u
            out.append(acc)
        return out

    def stress(self, x_spatial):
        """Symmetrised canonical bilinear at (t = 0, x_spatial):
        T_ab = (i/4)[ psibar gamma_a d_b psi + psibar gamma_b d_a psi
                      - (d_a psibar) gamma_b psi
                      - (d_b psibar) gamma_a psi ],  real part."""
        X = np.concatenate([[0.0], np.asarray(x_spatial, dtype=float)])
        psi = self.psi(X)
        dpsi = self.dpsi(X)
        psibar = psi.conj() @ GAMMA_UP[0]
        dpsibar = [d.conj() @ GAMMA_UP[0] for d in dpsi]
        T = np.zeros((4, 4))
        for a in range(4):
            for b in range(4):
                val = (psibar @ GAMMA_LO[a] @ dpsi[b]
                       + psibar @ GAMMA_LO[b] @ dpsi[a]
                       - dpsibar[a] @ GAMMA_LO[b] @ psi
                       - dpsibar[b] @ GAMMA_LO[a] @ psi)
                T[a, b] = float((0.25j * val).real)
        return T


def field_from_blocks(blocks):
    """blocks: list of (pvecs (N,3), avecs (N,2) complex, mass)."""
    modes = []
    for pvecs, avecs, m in blocks:
        for pv, av in zip(pvecs, avecs):
            modes.append((pv, av, float(m)))
    return CompositeField(modes)


# ------------------------------------------------------------------
# C1 cross-check ONLY: an independently written pairwise assembly
# with per-mode masses. Never feeds a deciding read.
# ------------------------------------------------------------------
def stress_pairwise_check(modes, x_spatial):
    us, Es, pcovs = [], [], []
    for pv, chi, m in modes:
        u, E = u_spinor(pv, float(m), chi)
        us.append(u)
        Es.append(E)
        pcovs.append(np.concatenate([[E], -np.asarray(pv, dtype=float)]))
    x = np.asarray(x_spatial, dtype=float)
    ph = [np.exp(1.0j * float(np.asarray(pv, dtype=float) @ x))
          for pv, chi, m in modes]
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
# Hawking-Ellis type and eigen-channel decomposition (gate's own
# code; channel definitions per Phase 410 SS4(ii)).
# ------------------------------------------------------------------
def segre_type(T):
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
    """Eigen-channel decomposition (definitions per Phase 410
    SS4(ii)): rho, p_r (nhat-aligned), p_t; NEC/WEC/DEC/SEC
    channels; SEC_min and joint_min over channels."""
    T = np.asarray(T, dtype=float)
    nhat = np.asarray(nhat, dtype=float)
    out = {"segre_type": segre_type(T)["type"],
           "rho_eulerian_T00": float(T[0, 0]),
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


JOINT_CHANNELS = ("NEC_r", "NEC_t", "WEC", "DEC_r", "DEC_t", "DEC_flux")


def joint_channel_values(chans):
    """Flat list of the joint (NEC/WEC/DEC) channel values."""
    vals = [chans["NEC_r"], chans["WEC"], chans["DEC_r"], chans["DEC_flux"]]
    vals += list(chans["NEC_t"]) + list(chans["DEC_t"])
    return vals


# ------------------------------------------------------------------
# The delta construction (gate's own implementation of the
# registered construction): eigenframe of eta*T; Delta =
# -SEC_trace split equally over the four eigenvalues entering
# SEC_trace (+Delta/4 on rho's eigenvalue, -Delta/4 on each
# spacelike eigenvalue of eta*T, i.e. +Delta/4 on each pressure);
# deltaThat = eta . V W V^-1; delta = 0 where SEC_trace >= 0.
# ------------------------------------------------------------------
def build_delta(T):
    T = np.asarray(T, dtype=float)
    M = ETA @ T
    ev, V = np.linalg.eig(M)
    ev = ev.real
    V = V.real
    tl = None
    for idx in range(4):
        v = V[:, idx]
        if float(v @ ETA @ v) > 1e-9 * float(v @ v):
            tl = idx
    if tl is None:
        raise ValueError("no timelike eigenvector — not Type-I")
    rho = float(ev[tl])
    pressures = [float(-ev[idx]) for idx in range(4) if idx != tl]
    sec_trace = rho + sum(pressures)
    if sec_trace >= 0.0:
        return np.zeros((4, 4)), {"Delta": 0.0, "sec_trace_req": sec_trace,
                                  "rho": rho, "pressures": pressures,
                                  "applied": False}
    Delta = -sec_trace
    w = np.full(4, -Delta / 4.0)
    w[tl] = +Delta / 4.0
    delta = ETA @ V @ np.diag(w) @ np.linalg.inv(V)
    return delta, {"Delta": float(Delta), "sec_trace_req": sec_trace,
                   "rho": rho, "pressures": pressures, "applied": True}


# ------------------------------------------------------------------
# Residual map and FD Jacobians (gate's own, on the field path).
# Theta layout: concatenated family blocks, each in the folded
# form [pvecs (3N), Re avecs (2N), Im avecs (2N)].
# ------------------------------------------------------------------
def unpack_block(theta, N):
    pvecs = theta[:3 * N].reshape(N, 3)
    avecs = (theta[3 * N:5 * N] + 1.0j * theta[5 * N:7 * N]).reshape(N, 2)
    return pvecs, avecs


def pack_block(pvecs, avecs):
    return np.concatenate([np.asarray(pvecs, dtype=float).ravel(),
                           np.asarray(avecs).real.ravel(),
                           np.asarray(avecs).imag.ravel()])


def make_resid(blockspec, points, targets):
    """blockspec: list of (N, mass). Residual: per site the 10
    upper-triangular components of (T_sup - T_target)/||T_target||_F
    via the field path."""
    frobs = [float(np.linalg.norm(t)) for t in targets]
    ns = len(points)

    def resid_vec(theta):
        blocks = []
        off = 0
        for (N, m) in blockspec:
            pv, av = unpack_block(theta[off:off + 7 * N], N)
            blocks.append((pv, av, m))
            off += 7 * N
        f = field_from_blocks(blocks)
        r = np.empty(10 * ns)
        for si in range(ns):
            T = f.stress(points[si])
            d = (T - targets[si]) / frobs[si]
            r[si * 10:(si + 1) * 10] = np.array([d[a, b] for a, b in IU])
        return r
    return resid_vec


def fd_jacobian(resid_vec, theta):
    theta = np.asarray(theta, dtype=float)
    npar = len(theta)
    J = np.empty((len(resid_vec(theta)), npar))
    for j in range(npar):
        h = 1e-6 * max(1.0, abs(theta[j]))
        tp = theta.copy(); tp[j] += h
        tm = theta.copy(); tm[j] -= h
        J[:, j] = (resid_vec(tp) - resid_vec(tm)) / (2.0 * h)
    return J


def jacobian_report(resid_vec, theta, ns):
    J = fd_jacobian(resid_vec, theta)
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


def avecs_from_json(raw):
    """Stored avecs: per mode [[re, im], [re, im]]."""
    return np.array([[complex(c[0], c[1]) for c in mode] for mode in raw])
