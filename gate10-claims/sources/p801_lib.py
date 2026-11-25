"""
p801_lib.py — P80-1 multipole gate auditor for Le arXiv:2606.22531.

Generalisation of the Phase 71 auditor (phase71/work/p715_lib.py, the
Phases 50/51/63 gate pattern): FD metric derivatives -> algebraic Gamma
-> FD normal gradient -> orthonormal-frame K -> Lanczos surface stress
-> Hawking-Ellis Type-I + Eq.(35) worst-observer DEC margin + sampled
cross-check + h-ladder. Pure numpy float64. NO author code, NO warpax/JAX.

Multipole generalisation (the paper's Supplement S / published-code
specification): shell areal shape R(th) = R0 + sum_{l=1..L} c_l P_l(mu),
c_l = lam * R0 * rho_l, mu = cos(th); frame seeds on both sides carry
Legendre / vector-harmonic modes:
  At_e = 1/sqrt(1-x) + lam * sum_l At_l P_l(mu),  w_e = lam * sum_l w_l S_l
  At_i = 1 + lam * sum_l Ai_l P_l(mu),            w_i = lam * sum_l wi_l S_l
with S_l(th) = sin(th) P_l'(cos th) (author convention, cf.
reproduce/multipole_frontier.py _Sl_np / induced_and_K_mp seed
seed_tau = At*dt + w*merid).

POLE TREATMENT (registered in p801_run_record.md BEFORE any number):
everything is evaluated from mu = cos(th); at the poles mu = +/-1
exactly, P_l(+/-1) = (+/-1)^l, S_l = 0 exactly (computed as
-P_l^1(mu) via the associated-Legendre recurrence, which vanishes at
mu = +/-1), and the Cartesian FD machinery is regular at the pole
point X = (0, -/+q, 0, 0). The pole margin is computed AT th = pi,
not extrapolated.
"""
import sys
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/warp-pilot/phase71/work")
from p715_lib import (metric_ext, metric_int, areal_ext, areal_int,  # noqa: E402
                      fd_jacobian, christoffel, lanczos, phi_HE,
                      sampled_dec_min, anchor_closed)

DTYPE = np.float64
R0 = 1.0


# ---------------------------------------------------------------- harmonics
def legendre_all(mu, L):
    """[P_0(mu), ..., P_L(mu)] by Bonnet recurrence (exact at mu=+/-1)."""
    P = [np.ones_like(np.asarray(mu, dtype=DTYPE)) if np.ndim(mu) else 1.0]
    mu = np.asarray(mu, dtype=DTYPE)
    P = [np.ones_like(mu)]
    if L >= 1:
        P.append(mu.copy())
    for l in range(2, L + 1):
        P.append(((2 * l - 1) * mu * P[-1] - (l - 1) * P[-2]) / l)
    return P[:L + 1]


def S_all(mu, L):
    """[S_1, ..., S_L], S_l = sin(th) P_l'(cos th) = -P_l^1(mu).
    Associated-Legendre recurrence in mu; exactly 0 at mu = +/-1."""
    mu = np.asarray(mu, dtype=DTYPE)
    somx2 = np.sqrt(np.maximum(0.0, 1.0 - mu * mu))
    Pm1 = np.zeros_like(mu)          # P_0^1 = 0
    if L == 0:
        return []
    Pc = -somx2                      # P_1^1 = -sqrt(1-mu^2)
    out = [-Pc]                      # S_1 = -P_1^1
    Pp, Pcur = Pm1, Pc
    for l in range(1, L):
        # (l-1+1)=l factor: l * P_{l+1}^1 = (2l+1) mu P_l^1 - (l+1) P_{l-1}^1
        Pn = ((2 * l + 1) * mu * Pcur - (l + 1) * Pp) / l if l >= 1 else -somx2
        out.append(-Pn)
        Pp, Pcur = Pcur, Pn
    return out[:L]


# ---------------------------------------------------------------- shell core
def _phi_factory(areal_fn, cvec):
    L = len(cvec)

    def Phi(Y):
        Y = np.asarray(Y, dtype=DTYPE)
        rho = np.sqrt(Y[1] ** 2 + Y[2] ** 2 + Y[3] ** 2)
        mu = Y[1] / rho if rho > 0 else 1.0
        Pl = legendre_all(mu, L)
        shape = R0 + float(sum(cvec[l - 1] * Pl[l] for l in range(1, L + 1)))
        return areal_fn(Y) - shape
    return Phi


def _normal_field(metric_fn, areal_fn, cvec):
    Phi = _phi_factory(areal_fn, cvec)

    def nfield(Y):
        Y = np.asarray(Y, dtype=DTYPE)
        dPhi = fd_jacobian(lambda Z: np.array([Phi(Z)]), Y, 1e-6)[0]
        g = metric_fn(Y)
        gi = np.linalg.inv(g)
        norm = np.sqrt(float(dPhi @ gi @ dPhi))
        return dPhi / norm
    return nfield


def induced_and_K_mp(metric_fn, areal_fn, cvec, X, th, At, w, h=0.01, order=2):
    """(h_ab, K^a_b) in the orthonormal geometric frame at shell point X.
    Identical construction to p715_lib.induced_and_K, multipole level set."""
    X = np.asarray(X, dtype=DTYPE)
    nfield = _normal_field(metric_fn, areal_fn, cvec)
    n_low = nfield(X)
    g = metric_fn(X)
    gi = np.linalg.inv(g)
    n_up = gi @ n_low
    dn = fd_jacobian(nfield, X, h, order)
    Gam = christoffel(metric_fn, X, h, order)
    gradn = dn.T - np.einsum("lmn,l->mn", Gam, n_low)
    gradn = 0.5 * (gradn + gradn.T)

    P = np.eye(4) - np.outer(n_up, n_low)
    sth, cth = np.sin(th), np.cos(th)
    merid = np.array([0.0, -sth, cth, 0.0], dtype=DTYPE)
    azim = np.array([0.0, 0.0, 0.0, 1.0], dtype=DTYPE)
    seed_tau = At * np.array([1.0, 0.0, 0.0, 0.0], dtype=DTYPE) + w * merid
    seeds = [seed_tau, merid, azim]
    E = [P @ s for s in seeds]
    hab = np.array([[float(E[i] @ g @ E[j]) for j in range(3)] for i in range(3)],
                   dtype=DTYPE)

    def dot(u, v):
        return float(u @ g @ v)

    e = []
    for v in E:
        vv = v.copy()
        for u_ in e:
            vv = vv - (dot(vv, u_) / dot(u_, u_)) * u_
        e.append(vv)
    fr = [e[0] / np.sqrt(-dot(e[0], e[0])),
          e[1] / np.sqrt(dot(e[1], e[1])),
          e[2] / np.sqrt(dot(e[2], e[2]))]
    Kab = np.array([[float(fr[i] @ gradn @ fr[j]) for j in range(3)] for i in range(3)],
                   dtype=DTYPE)
    eta3 = np.diag([-1.0, 1.0, 1.0])
    return hab, eta3 @ Kab


def exterior_point_mp(a, M, th, Rt):
    """t=0 point with exact exterior areal radius Rt (Newton on q)."""
    cth, sth = np.cos(th), np.sin(th)
    q = Rt
    for _ in range(60):
        X = np.array([0.0, q * cth, q * sth, 0.0], dtype=DTYPE)
        val = areal_ext(X, a)
        dq = 1e-7
        Xp = np.array([0.0, (q + dq) * cth, (q + dq) * sth, 0.0], dtype=DTYPE)
        der = (areal_ext(Xp, a) - val) / dq
        step = (val - Rt) / der
        q -= step
        if abs(step) < 1e-14:
            break
    return np.array([0.0, q * cth, q * sth, 0.0], dtype=DTYPE)


def unpack_params(p, L, interior_tilt=True, interior_lapse=True):
    """Author layout: [rho(1..L), At(1..L), w(1..L), (wi), (Ai)]."""
    p = np.asarray(p, dtype=DTYPE)
    rho = p[0:L]; At = p[L:2 * L]; w = p[2 * L:3 * L]
    i = 3 * L
    wi = np.zeros(L); Ai = np.zeros(L)
    if interior_tilt:
        wi = p[i:i + L]; i += L
    if interior_lapse:
        Ai = p[i:i + L]; i += L
    return rho, At, w, wi, Ai


def sample_mp(x, lam, p, L, thetas, interior_tilt=True, interior_lapse=True,
              h=0.01, order=2):
    """h and K on both sides over thetas (any grid, poles included)."""
    a = lam / R0
    M = x * R0 / 2.0
    At0_ext = 1.0 / np.sqrt(1.0 - x)
    rho, At, w, wi, Ai = unpack_params(p, L, interior_tilt, interior_lapse)
    cvec = lam * R0 * np.asarray(rho, dtype=DTYPE)
    out = {k: [] for k in ("th", "hP", "KP", "hM", "KM")}
    for th in thetas:
        mu = float(np.cos(th))
        Pl = legendre_all(mu, L)
        Sl = S_all(mu, L)
        Rt = R0 + float(sum(cvec[l - 1] * Pl[l] for l in range(1, L + 1)))
        Xp = exterior_point_mp(a, M, th, Rt)
        Xm = np.array([0.0, Rt * np.cos(th), Rt * np.sin(th), 0.0], dtype=DTYPE)
        At_e = At0_ext + lam * float(sum(At[l - 1] * Pl[l] for l in range(1, L + 1)))
        w_e = lam * float(sum(w[l - 1] * Sl[l - 1] for l in range(1, L + 1)))
        At_i = 1.0 + lam * float(sum(Ai[l - 1] * Pl[l] for l in range(1, L + 1)))
        w_i = lam * float(sum(wi[l - 1] * Sl[l - 1] for l in range(1, L + 1)))
        hP, KP = induced_and_K_mp(lambda Y: metric_ext(Y, a, M),
                                  lambda Y: areal_ext(Y, a), cvec, Xp, th,
                                  At_e, w_e, h=h, order=order)
        hM, KM = induced_and_K_mp(lambda Y: metric_int(Y, a), areal_int, cvec,
                                  Xm, th, At_i, w_i, h=h, order=order)
        out["th"].append(float(th)); out["hP"].append(hP); out["KP"].append(KP)
        out["hM"].append(hM); out["KM"].append(KM)
    for k in ("hP", "KP", "hM", "KM"):
        out[k] = np.array(out[k])
    out["th"] = np.array(out["th"])
    return out


def stress_rows(r):
    """[(sigma, p_th, p_ph, flux)] from a sample_mp result."""
    return [lanczos(r["KP"][i], r["KM"][i]) for i in range(len(r["th"]))]


def audit_grid():
    """Registered audit grid (run record S3): uniform in mu incl. BOTH pole
    endpoints exactly, plus refined near-pole bands."""
    mu = np.linspace(-1.0, 1.0, 161)
    th = np.arccos(np.clip(mu, -1.0, 1.0))
    rear = np.pi - np.linspace(0.0, 0.15, 41)      # theta in [pi-0.15, pi]
    front = np.linspace(0.0, 0.15, 21)             # theta in [0, 0.15]
    allth = np.unique(np.concatenate([th, rear, front]))
    return np.sort(allth)


def eig_margins(sig, pth, pph, f):
    """Boosted eigenvalue margins of the (tau,th) block + phi sector:
    returns (rho_eig, p_par_eig, margin_rho_minus_abs_ppar, margin_rho_minus_abs_pph,
             discriminant). disc < 0 -> Type IV (no real eigenvalues)."""
    disc = (sig + pth) ** 2 - 4.0 * f ** 2
    if disc < 0:
        return None, None, -np.sqrt(-disc), -np.sqrt(-disc), float(disc)
    root = np.sqrt(disc)
    rho = (sig - pth) / 2.0 + root / 2.0
    p_par = (pth - sig) / 2.0 + root / 2.0
    return float(rho), float(p_par), float(rho - abs(p_par)), \
        float(rho - abs(pph)), float(disc)
