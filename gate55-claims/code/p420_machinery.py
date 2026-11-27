"""p420_machinery.py -- Phase 420 spinor machinery.

The block between the MACHINERY markers is Phase 410's machinery
block extracted verbatim (itself Phase 320/313 verbatim in
content). `decompose` is Phase 410's, verbatim. Everything after
the END OF VERBATIM marker is Phase 420's per-mode-mass
generalisation (registration SS2).
"""
import os
import sys
import numpy as np

WP = os.environ.get('P420_WP', '/home/hatch/workspace/warp-pilot')
for _p in (WP, f'{WP}/phase235/work', f'{WP}/phase258/work',
           f'{WP}/phase267/work', f'{WP}/phase274/work',
           f'{WP}/phase312/work', f'{WP}/phase405/work'):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from p2352_run import margins_chunked, fib_dirs  # noqa: E402,F401
from p258_lib import R_NODES, DIRS162  # noqa: E402,F401

# ============ MACHINERY (Phase 320 verbatim in content) ============
# =====================================================================
# Spinor machinery (Phase 253/257/261/293, verbatim in content)
# =====================================================================
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), dtype=complex)
gamma = [np.block([[I2, Z2], [Z2, -I2]])] + [
    np.block([[Z2, s], [-s, Z2]]) for s in (s1, s2, s3)]
gamma_cov = [gamma[0], -gamma[1], -gamma[2], -gamma[3]]  # gamma_a
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
def slash_cov(kcov):
    return sum(gamma[a] * kcov[a] for a in range(4))
def lower(v): return ETA @ v

def u_spinor(pvec, m, chi):
    E = np.sqrt(pvec @ pvec + m * m)
    if m == 0.0:
        denom = np.sqrt(E)
        top = denom * chi
        bot = (s1 * pvec[0] + s2 * pvec[1] + s3 * pvec[2]) @ chi / denom
    else:
        denom = np.sqrt(E + m)
        top = denom * chi
        bot = (s1 * pvec[0] + s2 * pvec[1] + s3 * pvec[2]) @ chi / denom
    return np.concatenate([top, bot]), E

def dirac_residual(u, pvec, m):
    E = np.sqrt(pvec @ pvec + m * m)
    p = np.concatenate([[E], pvec])
    return slash_cov(lower(p)) @ u - m * u

def fields_at_point(modes):
    m = modes[0][3]
    psi = sum(c * u for c, u, pv, _ in modes)
    dpsi = []
    for a in range(4):
        acc = np.zeros(4, dtype=complex)
        for c, u, pv, _ in modes:
            E = np.sqrt(pv @ pv + m * m)
            pa = E if a == 0 else -pv[a - 1]
            acc += c * (-1j * pa) * u
        dpsi.append(acc)
    return psi, dpsi

def T_bilinear(modes, uvec, vvec):
    psi, dpsi = fields_at_point(modes)
    psibar = psi.conj() @ gamma[0]
    dpsibar = [d.conj() @ gamma[0] for d in dpsi]
    def gam(vec): return slash_cov(lower(vec))
    def D(vec): return sum(vec[a] * dpsi[a] for a in range(4))
    def Db(vec): return sum(vec[a] * dpsibar[a] for a in range(4))
    val = (1j / 4) * (psibar @ gam(uvec) @ D(vvec)
                      + psibar @ gam(vvec) @ D(uvec)
                      - Db(uvec) @ gam(vvec) @ psi
                      - Db(vvec) @ gam(uvec) @ psi)
    return float(val.real), psi

def stress_at_point(modes):
    T = np.zeros((4, 4)); psi = None
    for a in range(4):
        for b in range(4):
            va = np.zeros(4); va[a] = 1.0
            vb = np.zeros(4); vb[b] = 1.0
            T[a, b], psi = T_bilinear(modes, va, vb)
    return T, psi

def pairwise_S(modes_pm):
    n = len(modes_pm); S = np.zeros((n, n, 4, 4), dtype=complex)
    pcov = []
    for u, pv, m in modes_pm:
        E = np.sqrt(pv @ pv + m * m)
        pcov.append(np.concatenate([[E], -pv]))
    for i in range(n):
        ui = modes_pm[i][0]; ubar_i = ui.conj() @ gamma[0]
        for j in range(n):
            uj = modes_pm[j][0]
            J = np.array([ubar_i @ gamma_cov[b] @ uj for b in range(4)])
            psum = pcov[i] + pcov[j]
            S[i, j] = 0.25 * (np.outer(psum, J) + np.outer(J, psum))
    return S

def T_from_S(S, c):
    return np.einsum('i,ijab,j->ab', c.conj(), S, c).real

def modes_at_point(pvecs, avecs, m, x):
    modes = []
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        modes.append((np.exp(1j * float(pv @ x)), U, pv, m))
    return modes

def T_direct(pvecs, avecs, m, x):
    T, _ = stress_at_point(modes_at_point(pvecs, avecs, m, x))
    return T

def S_of(pvecs, avecs, m):
    modes_pm = []
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        modes_pm.append((U, pv, m))
    return pairwise_S(modes_pm)

GAMMA_COV_ARR = np.array(gamma_cov)  # (4,4,4)

def S_of_vec(pvecs, avecs, m):
    pvecs = np.asarray(pvecs, dtype=float)
    Us = []
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        Us.append(U)
    U = np.array(Us)                                   # (N,4)
    E = np.sqrt(np.sum(pvecs ** 2, axis=1) + m * m)
    pcov = np.concatenate([E[:, None], -pvecs], axis=1)  # (N,4)
    ubar = U.conj() @ gamma[0]                         # (N,4)
    GU = np.einsum('bac,jc->bja', GAMMA_COV_ARR, U)    # gamma_cov[b] @ U_j
    J = np.einsum('ic,bjc->bij', ubar, GU)             # J[b,i,j]
    psum = pcov[:, None, :] + pcov[None, :, :]         # (i,j,a)
    S = 0.25 * (psum[:, :, :, None] * J.transpose(1, 2, 0)[:, :, None, :]
                + J.transpose(1, 2, 0)[:, :, :, None] * psum[:, :, None, :])
    return S

def T_pairwise(S, pvecs, x):
    ph = np.exp(1j * (pvecs @ x))
    return T_from_S(S, ph)

def segre(T):
    """Phase 257's classifier, verbatim."""
    M = ETA @ T
    ev, evec = np.linalg.eig(M)
    max_im = float(np.max(np.abs(ev.imag))) if np.any(np.abs(ev.imag) > 0) else 0.0
    out = {"eigs": [[float(z.real), float(z.imag)] for z in ev],
           "max_abs_imag": max_im}
    scale = max(1e-30, float(np.max(np.abs(ev.real))))
    if max_im > 1e-9 * scale and max_im > 1e-12:
        out["type"] = "IV (complex pair)"
        return out
    timelike = False
    for idx in range(4):
        v = evec[:, idx].real
        n2 = float(v @ ETA @ v)
        if n2 > 1e-9 * float(v @ v):
            timelike = True
    cond = float(np.linalg.cond(evec))
    out["timelike_eigenvector"] = timelike
    out["evec_cond"] = cond
    if timelike and cond < 1e8:
        out["type"] = "I"
    else:
        out["type"] = "II/III-degenerate (real spectrum, no timelike eigenvector or defective)"
    return out

IU = [(a, b) for a in range(4) for b in range(a, 4)]

# ============ end MACHINERY ============

# =====================================================================
# Phase 410's decompose(), verbatim
# =====================================================================
def decompose(T, nhat):
    out = {}
    sg = segre(T)
    out["segre_type"] = sg["type"]
    mm = margins_chunked(T[None, :, :])
    out["samplerM"] = {k: float(mm[k][0]) for k in ("nec", "wec", "dec", "sec")}
    out["flux_norm"] = float(np.linalg.norm(T[0, 1:4]))
    out["rho"] = float(T[0, 0])
    out["components"] = {f"T{a}{b}": float(T[a, b]) for a, b in IU}
    if sg["type"] == "I":
        ev, evec = np.linalg.eig(ETA @ T)
        ev = ev.real; evec = evec.real
        # timelike eigenvector -> rho; others -> -p_i
        tl = None
        for idx in range(4):
            v = evec[:, idx]
            if float(v @ ETA @ v) > 1e-9 * float(v @ v):
                tl = idx
        if tl is not None:
            rho = float(ev[tl])
            ps = []
            for idx in range(4):
                if idx == tl:
                    continue
                v = evec[:, idx]
                align = abs(float(v[1:4] @ nhat)) / max(
                    float(np.linalg.norm(v[1:4])), 1e-300)
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
            out["SEC_min_channel"] = float(min(
                chans["SEC_trace"], chans["SEC_r"], min(chans["SEC_t"])))
            out["joint_min_channel"] = float(min(
                chans["NEC_r"], min(chans["NEC_t"]), chans["WEC"],
                chans["DEC_r"], min(chans["DEC_t"]), chans["DEC_flux"]))
    return out



# =====================================================================
# END OF VERBATIM BLOCK. Phase 420 additions: per-mode-mass
# generalisations (registration SS2). Family 1: m = 1 (Phase 410's
# family). Family 2: m = 0. The total field is the sum of both
# families' fields; the composite tensor is the total field's
# stress tensor, cross terms included.
# =====================================================================

def S_of_multi(pvecs, avecs, masses):
    """S_of_vec generalised to per-mode masses."""
    pvecs = np.asarray(pvecs, dtype=float)
    masses = np.asarray(masses, dtype=float)
    Us = []
    for pv, av, m in zip(pvecs, avecs, masses):
        U, _ = u_spinor(pv, float(m), av)
        Us.append(U)
    U = np.array(Us)                                   # (N,4)
    E = np.sqrt(np.sum(pvecs ** 2, axis=1) + masses ** 2)
    pcov = np.concatenate([E[:, None], -pvecs], axis=1)  # (N,4)
    ubar = U.conj() @ gamma[0]                         # (N,4)
    GU = np.einsum('bac,jc->bja', GAMMA_COV_ARR, U)    # gamma_cov[b] @ U_j
    J = np.einsum('ic,bjc->bij', ubar, GU)             # J[b,i,j]
    psum = pcov[:, None, :] + pcov[None, :, :]         # (i,j,a)
    S = 0.25 * (psum[:, :, :, None] * J.transpose(1, 2, 0)[:, :, None, :]
                + J.transpose(1, 2, 0)[:, :, :, None] * psum[:, :, None, :])
    return S


def fields_at_point_multi(modes):
    """fields_at_point with per-mode masses: modes are
    (c, u, pvec, m); the derivative phase of each mode uses its
    own E_i = sqrt(|p_i|^2 + m_i^2)."""
    psi = sum(c * u for c, u, pv, m in modes)
    dpsi = []
    for a in range(4):
        acc = np.zeros(4, dtype=complex)
        for c, u, pv, m in modes:
            E = np.sqrt(pv @ pv + m * m)
            pa = E if a == 0 else -pv[a - 1]
            acc += c * (-1j * pa) * u
        dpsi.append(acc)
    return psi, dpsi


def T_bilinear_multi(modes, uvec, vvec):
    psi, dpsi = fields_at_point_multi(modes)
    psibar = psi.conj() @ gamma[0]
    dpsibar = [d.conj() @ gamma[0] for d in dpsi]
    def gam(vec): return slash_cov(lower(vec))
    def D(vec): return sum(vec[a] * dpsi[a] for a in range(4))
    def Db(vec): return sum(vec[a] * dpsibar[a] for a in range(4))
    val = (1j / 4) * (psibar @ gam(uvec) @ D(vvec)
                      + psibar @ gam(vvec) @ D(uvec)
                      - Db(uvec) @ gam(vvec) @ psi
                      - Db(vvec) @ gam(uvec) @ psi)
    return float(val.real), psi


def stress_at_point_multi(modes):
    T = np.zeros((4, 4)); psi = None
    for a in range(4):
        for b in range(4):
            va = np.zeros(4); va[a] = 1.0
            vb = np.zeros(4); vb[b] = 1.0
            T[a, b], psi = T_bilinear_multi(modes, va, vb)
    return T, psi


def modes_at_point_multi(pvecs, avecs, masses, x):
    modes = []
    for pv, av, m in zip(pvecs, avecs, masses):
        U, _ = u_spinor(pv, float(m), av)
        modes.append((np.exp(1j * float(pv @ x)), U, pv, float(m)))
    return modes


def T_direct_multi(pvecs, avecs, masses, x):
    T, _ = stress_at_point_multi(modes_at_point_multi(pvecs, avecs,
                                                      masses, x))
    return T


# ---- composite parametrisation: theta = [fam1 block, fam2 block],
# each block in Phase 410's folded form [pvecs 3N, Re a 2N, Im a 2N].

def pack_block(pvecs, avecs):
    return np.concatenate([np.asarray(pvecs, dtype=float).ravel(),
                           np.asarray(avecs).real.ravel(),
                           np.asarray(avecs).imag.ravel()])


def unpack_block(block, N):
    pvecs = block[:3 * N].reshape(N, 3)
    avecs = (block[3 * N:5 * N] + 1j * block[5 * N:7 * N]).reshape(N, 2)
    return pvecs, avecs


def pack2(pv1, av1, pv2, av2):
    return np.concatenate([pack_block(pv1, av1), pack_block(pv2, av2)])


def unpack2(theta, N1, N2):
    pv1, av1 = unpack_block(theta[:7 * N1], N1)
    if N2 > 0:
        pv2, av2 = unpack_block(theta[7 * N1:7 * N1 + 7 * N2], N2)
    else:
        pv2 = np.zeros((0, 3)); av2 = np.zeros((0, 2), dtype=complex)
    return pv1, av1, pv2, av2


def guard_zero_momenta(pv, mm):
    """Numerical guard (Phase 420 addition, disclosed): the
    massless spinor u_spinor divides by E + m = |p|, so an
    EXACTLY zero momentum in a massless mode is singular
    (0/0). Any nonzero |p|, however small, is finite (the
    lower component is O(1) in the direction). Replace an
    exactly-zero massless momentum by (1, 0, 0); this
    touches only the measure-zero singular set. Returns a
    copy; the input is not mutated."""
    pv = np.array(pv, dtype=float)
    for i in range(len(pv)):
        if mm[i] == 0.0 and pv[i, 0] == 0.0 and pv[i, 1] == 0.0 \
                and pv[i, 2] == 0.0:
            pv[i] = (1.0, 0.0, 0.0)
    return pv


def join_modes(pv1, av1, m1, pv2, av2, m2):
    """Concatenated (pvecs, avecs, masses) for a two-family theta."""
    pv = np.concatenate([pv1, pv2]) if len(pv2) else np.array(pv1)
    av = np.concatenate([av1, av2]) if len(av2) else np.array(av1)
    mm = np.concatenate([np.full(len(pv1), float(m1)),
                         np.full(len(pv2), float(m2))]) if len(pv2) \
        else np.full(len(pv1), float(m1))
    return pv, av, mm


def make_resid_multi(XS, TARGETS, FROBS, N1, N2, m1, m2):
    ns = len(XS)

    def resid_vec(theta):
        pv1, av1, pv2, av2 = unpack2(theta, N1, N2)
        pv1 = guard_zero_momenta(pv1, np.full(len(pv1), m1))
        pv2 = guard_zero_momenta(pv2, np.full(len(pv2), m2))
        pv, av, mm = join_modes(pv1, av1, m1, pv2, av2, m2)
        S = S_of_multi(pv, av, mm)
        r = np.empty(10 * ns)
        for si in range(ns):
            T = T_pairwise(S, pv, XS[si])
            d = T - TARGETS[si]
            r[si * 10:(si + 1) * 10] = np.array([d[a, b] for a, b in IU]) \
                / FROBS[si]
        return r
    return resid_vec


def site_residuals_multi(pv, av, mm, XS, TARGETS, direct=False):
    pv = guard_zero_momenta(pv, mm)
    Rs, rhos = [], []
    if direct:
        for si in range(len(XS)):
            T = T_direct_multi(pv, av, mm, XS[si])
            Rs.append(float(np.linalg.norm(T - TARGETS[si])))
            rhos.append(float(T[0, 0]))
    else:
        S = S_of_multi(pv, av, mm)
        for si in range(len(XS)):
            T = T_pairwise(S, pv, XS[si])
            Rs.append(float(np.linalg.norm(T - TARGETS[si])))
            rhos.append(float(T[0, 0]))
    return Rs, rhos


def fd_jacobian_g(resid_vec, theta_d):
    """410's fd_jacobian, generic in the parameter count; the
    residual callable takes theta alone."""
    npar = len(theta_d)
    J = np.empty((len(resid_vec(theta_d)), npar))
    for j in range(npar):
        h = 1e-6 * max(1.0, abs(theta_d[j]))
        tp = theta_d.copy(); tp[j] += h
        tm = theta_d.copy(); tm[j] -= h
        J[:, j] = (resid_vec(tp) - resid_vec(tm)) / (2.0 * h)
    return J


def jacobian_report_g(resid_vec, theta_d, ns):
    J = fd_jacobian_g(resid_vec, theta_d)
    sv = np.linalg.svd(J, compute_uv=False)
    blocks = {}
    for si in range(ns):
        svb = np.linalg.svd(J[si * 10:(si + 1) * 10, :], compute_uv=False)
        blocks[str(si)] = {"sigma_min": float(svb[-1]),
                           "sigma_max": float(svb[0]),
                           "rank_tol_1e-10_rel":
                               int(np.sum(svb > 1e-10 * svb[0]))}
    return {"shape": [10 * ns, int(len(theta_d))],
            "singular_values": [float(v) for v in sv],
            "rank_tol_1e-10_rel": int(np.sum(sv > 1e-10 * sv[0])),
            "sigma_min": float(sv[-1]), "sigma_max": float(sv[0]),
            "per_site_blocks": blocks}


def dirac_max_residual_multi(pv, av, mm):
    pv = guard_zero_momenta(pv, mm)
    mx = 0.0
    for p_, a_, m_ in zip(pv, av, mm):
        U, _ = u_spinor(p_, float(m_), a_)
        r = dirac_residual(U, p_, float(m_))
        mx = max(mx, float(np.max(np.abs(r))))
    return mx
