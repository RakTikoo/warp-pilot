"""GATE-12 fresh auditor for Le's multipole accelerating shell.

Written from scratch for Gate-12. NO phase code imported: no p715_lib,
no p801_lib, no p881_jax, no worldtube/warpax. The geometry is rebuilt
here from the paper's own published forms (arXiv:2606.22531):

  exterior: exact Kerr-Schild Kinnersley photon rocket,
    g = eta + (2M/ra) l l,  l = retarded null covector,
    worldline z(u) = (sinh(a u)/a, (cosh(a u)-1)/a, 0, 0),
    ra = -eta(v, X - z(u)), v = dz/du, u = retarded time (null-cone root);
  interior: flat Rindler cavity g = diag(-(1 + a x)^2, 1, 1, 1),
    areal radius = Euclidean radius;
  shell: areal radius R(th) = R0 + sum_l c_l P_l(cos th), c_l = lam R0 rho_l;
  frame seeds per side: At_e = 1/sqrt(1-x) + lam sum At_l P_l,
    w_e = lam sum w_l S_l,  At_i = 1 + lam sum Ai_l P_l,
    w_i = lam sum wi_l S_l,  S_l = sin(th) P_l'(cos th) = -P_l^1(cos th);
  seeds projected orthogonal to the unit normal, Gram-Schmidt in g;
  K from the FD gradient of the unit-normal field with Christoffels
  built algebraically from FD metric derivatives (this gate's own
  implementation); Lanczos stress; Hawking-Ellis type of the
  (tau,theta) block via its discriminant; worst-observer DEC margin
  in the paper's Eq.(35) boosted-eigenvalue form; sampled-observer
  DEC cross-check (Fibonacci/random causal pairs, this gate's code).

float64 throughout. R0 = 1, lam = a R0, M = x R0 / 2.
"""
import numpy as np

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
R0 = 1.0


# ------------------------------------------------------------------ harmonics
def legendre(mu, L):
    """[P_0..P_L] at mu (Bonnet recurrence; exact at mu = +/-1)."""
    mu = float(mu)
    P = [1.0]
    if L >= 1:
        P.append(mu)
    for l in range(2, L + 1):
        P.append(((2 * l - 1) * mu * P[-1] - (l - 1) * P[-2]) / l)
    return P


def s_harm(mu, L):
    """[S_1..S_L], S_l = -P_l^1(mu) (associated-Legendre recurrence)."""
    mu = float(mu)
    s = np.sqrt(max(0.0, 1.0 - mu * mu))
    if L == 0:
        return []
    Pm1 = 0.0            # P_0^1
    Pc = -s              # P_1^1
    out = [-Pc]
    Pp, Pcur = Pm1, Pc
    for l in range(1, L):
        Pn = ((2 * l + 1) * mu * Pcur - (l + 1) * Pp) / l
        out.append(-Pn)
        Pp, Pcur = Pcur, Pn
    return out[:L]


# ------------------------------------------------------------------ exterior
def _retarded(X, a):
    """Newton root of eta(X-z(u), X-z(u)) = 0 (past cone); returns (u, ra, D)."""
    X = np.asarray(X, float)
    if abs(a) < 1e-14:
        D = X.copy()
        return X[0] - np.sqrt(X[1] ** 2 + X[2] ** 2 + X[3] ** 2), \
            np.sqrt(X[1] ** 2 + X[2] ** 2 + X[3] ** 2), D
    u = X[0] - np.sqrt(X[1] ** 2 + X[2] ** 2 + X[3] ** 2)
    for _ in range(80):
        z = np.array([np.sinh(a * u) / a, (np.cosh(a * u) - 1.0) / a, 0.0, 0.0])
        v = np.array([np.cosh(a * u), np.sinh(a * u), 0.0, 0.0])
        D = X - z
        F = float(D @ ETA @ D)
        ra = -float(v @ ETA @ D)
        if ra <= 0:
            ra = 1e-13
        du = -F / (2.0 * ra)
        u += du
        if abs(du) < 1e-15:
            break
    z = np.array([np.sinh(a * u) / a, (np.cosh(a * u) - 1.0) / a, 0.0, 0.0])
    v = np.array([np.cosh(a * u), np.sinh(a * u), 0.0, 0.0])
    D = X - z
    return u, -float(v @ ETA @ D), D


def metric_ext(X, a, M):
    if M == 0.0:
        return ETA.copy()
    _, ra, D = _retarded(X, a)
    lc = ETA @ (D / ra)
    return ETA + (2.0 * M / ra) * np.outer(lc, lc)


def metric_int(X, a):
    g = ETA.copy()
    N = 1.0 + a * float(np.asarray(X, float)[1])
    g[0, 0] = -N * N
    return g


def areal_ext(X, a):
    return _retarded(X, a)[1]


def areal_int(X):
    X = np.asarray(X, float)
    return float(np.sqrt(X[1] ** 2 + X[2] ** 2 + X[3] ** 2))


# ------------------------------------------------------------------ FD tools
def fd_jac(field, X, h, order=2):
    X = np.asarray(X, float)
    n = len(field(X))
    J = np.zeros((n, 4))
    for mu in range(4):
        e = np.zeros(4); e[mu] = 1.0
        if order == 2:
            J[:, mu] = (field(X + h * e) - field(X - h * e)) / (2 * h)
        else:
            J[:, mu] = (-field(X + 2 * h * e) + 8 * field(X + h * e)
                        - 8 * field(X - h * e) + field(X - 2 * h * e)) / (12 * h)
    return J


def christoffel(metric_fn, X, h, order=2):
    g = metric_fn(X)
    gi = np.linalg.inv(g)
    dg = np.zeros((4, 4, 4))          # dg[mu] = d_mu g
    for mu in range(4):
        e = np.zeros(4); e[mu] = 1.0
        if order == 2:
            dg[mu] = (metric_fn(X + h * e) - metric_fn(X - h * e)) / (2 * h)
        else:
            dg[mu] = (-metric_fn(X + 2 * h * e) + 8 * metric_fn(X + h * e)
                      - 8 * metric_fn(X - h * e) + metric_fn(X - 2 * h * e)) / (12 * h)
    A = dg + np.transpose(dg, (1, 0, 2)) - np.transpose(dg, (1, 2, 0))
    # A[mu,nu,s] = d_mu g_{nu s} + d_nu g_{mu s} - d_s g_{mu nu}:
    # transpose(dg,(1,2,0))[mu,nu,s] = dg[s,mu,nu]  ✓
    return 0.5 * np.einsum("ls,mns->lmn", gi, A)


# ------------------------------------------------------------------ shell core
def _phi_fn(areal_fn, cvec):
    L = len(cvec)

    def Phi(Y):
        Y = np.asarray(Y, float)
        rho = np.sqrt(Y[1] ** 2 + Y[2] ** 2 + Y[3] ** 2)
        mu = Y[1] / rho if rho > 0 else 1.0
        Pl = legendre(mu, L)
        shape = R0 + sum(cvec[l - 1] * Pl[l] for l in range(1, L + 1))
        return areal_fn(Y) - shape
    return Phi


def _nfield(metric_fn, areal_fn, cvec):
    Phi = _phi_fn(areal_fn, cvec)

    def nfield(Y):
        Y = np.asarray(Y, float)
        dPhi = fd_jac(lambda Z: np.array([Phi(Z)]), Y, 1e-6)[0]
        gi = np.linalg.inv(metric_fn(Y))
        return dPhi / np.sqrt(float(dPhi @ gi @ dPhi))
    return nfield


def induced_and_K(metric_fn, areal_fn, cvec, X, th, At, w, h=0.01, order=2,
                  need_K=True):
    X = np.asarray(X, float)
    nfield = _nfield(metric_fn, areal_fn, cvec)
    n_low = nfield(X)
    g = metric_fn(X)
    gi = np.linalg.inv(g)
    n_up = gi @ n_low
    P = np.eye(4) - np.outer(n_up, n_low)
    sth, cth = np.sin(th), np.cos(th)
    merid = np.array([0.0, -sth, cth, 0.0])
    azim = np.array([0.0, 0.0, 0.0, 1.0])
    seed_tau = At * np.array([1.0, 0.0, 0.0, 0.0]) + w * merid
    E = [P @ s for s in (seed_tau, merid, azim)]
    hab = np.array([[float(E[i] @ g @ E[j]) for j in range(3)] for i in range(3)])
    if not need_K:
        return hab, None

    def dot(u, v):
        return float(u @ g @ v)

    dn = fd_jac(nfield, X, h, order)
    Gam = christoffel(metric_fn, X, h, order)
    gradn = dn.T - np.einsum("lmn,l->mn", Gam, n_low)
    gradn = 0.5 * (gradn + gradn.T)
    e = []
    for v in E:
        vv = v.copy()
        for u_ in e:
            vv = vv - (dot(vv, u_) / dot(u_, u_)) * u_
        e.append(vv)
    fr = [e[0] / np.sqrt(-dot(e[0], e[0])),
          e[1] / np.sqrt(dot(e[1], e[1])),
          e[2] / np.sqrt(dot(e[2], e[2]))]
    Kab = np.array([[float(fr[i] @ gradn @ fr[j]) for j in range(3)] for i in range(3)])
    return hab, np.diag([-1.0, 1.0, 1.0]) @ Kab


def exterior_point(a, M, th, Rt):
    cth, sth = np.cos(th), np.sin(th)
    q = float(Rt)
    for _ in range(60):
        X = np.array([0.0, q * cth, q * sth, 0.0])
        val = areal_ext(X, a)
        dq = 1e-7
        Xp = np.array([0.0, (q + dq) * cth, (q + dq) * sth, 0.0])
        der = (areal_ext(Xp, a) - val) / dq
        step = (val - Rt) / der
        q -= step
        if abs(step) < 1e-14:
            break
    return np.array([0.0, q * cth, q * sth, 0.0])


def unpack(p, L):
    p = np.asarray(p, float)
    return p[0:L], p[L:2 * L], p[2 * L:3 * L], p[3 * L:4 * L], p[4 * L:5 * L]


def frame_values(x, lam, p, L, th):
    """Per-side (At, w) and Rt at angle th from the coefficient layout."""
    a = lam / R0
    rho, At, w, wi, Ai = unpack(p, L)
    cvec = lam * R0 * rho
    mu = float(np.cos(th))
    Pl = legendre(mu, L)
    Sl = s_harm(mu, L)
    Rt = R0 + sum(cvec[l - 1] * Pl[l] for l in range(1, L + 1))
    At_e = 1.0 / np.sqrt(1.0 - x) + lam * sum(At[l - 1] * Pl[l] for l in range(1, L + 1))
    w_e = lam * sum(w[l - 1] * Sl[l - 1] for l in range(1, L + 1))
    At_i = 1.0 + lam * sum(Ai[l - 1] * Pl[l] for l in range(1, L + 1))
    w_i = lam * sum(wi[l - 1] * Sl[l - 1] for l in range(1, L + 1))
    return cvec, float(Rt), (At_e, w_e), (At_i, w_i)


def sample(x, lam, p, L, thetas, h=0.01, order=2):
    a = lam / R0
    M = x * R0 / 2.0
    out = {k: [] for k in ("th", "hP", "KP", "hM", "KM")}
    for th in thetas:
        cvec, Rt, (At_e, w_e), (At_i, w_i) = frame_values(x, lam, p, L, th)
        Xp = exterior_point(a, M, th, Rt)
        Xm = np.array([0.0, Rt * np.cos(th), Rt * np.sin(th), 0.0])
        hP, KP = induced_and_K(lambda Y: metric_ext(Y, a, M),
                               lambda Y: areal_ext(Y, a), cvec, Xp, th, At_e, w_e, h, order)
        hM, KM = induced_and_K(lambda Y: metric_int(Y, a), areal_int, cvec,
                               Xm, th, At_i, w_i, h, order)
        out["th"].append(float(th)); out["hP"].append(hP); out["KP"].append(KP)
        out["hM"].append(hM); out["KM"].append(KM)
    for k in ("hP", "KP", "hM", "KM"):
        out[k] = np.array(out[k])
    out["th"] = np.array(out["th"])
    return out


def frame_margins(x, lam, p, L, thetas, frames=("F0", "F1", "F2", "F3", "F4")):
    """min over grid of -h00 for alternative seed frames (h only, no K).
    F0 shared (At,w); F1 pure-time (At,0); F2 flipped (At,-w);
    F3 swapped sides; F4 unit-time (1,w). Margin = min over both sides."""
    a = lam / R0
    M = x * R0 / 2.0
    mins = {f: np.inf for f in frames}
    argmin = {f: None for f in frames}
    for th in thetas:
        cvec, Rt, (At_e, w_e), (At_i, w_i) = frame_values(x, lam, p, L, th)
        Xp = exterior_point(a, M, th, Rt)
        Xm = np.array([0.0, Rt * np.cos(th), Rt * np.sin(th), 0.0])
        seedmap = {
            "F0": ((At_e, w_e), (At_i, w_i)),
            "F1": ((At_e, 0.0), (At_i, 0.0)),
            "F2": ((At_e, -w_e), (At_i, -w_i)),
            "F3": ((At_i, w_i), (At_e, w_e)),
            "F4": ((1.0, w_e), (1.0, w_i)),
        }
        for f in frames:
            (se, si) = seedmap[f]
            hP, _ = induced_and_K(lambda Y: metric_ext(Y, a, M),
                                  lambda Y: areal_ext(Y, a), cvec, Xp, th,
                                  se[0], se[1], need_K=False)
            hM, _ = induced_and_K(lambda Y: metric_int(Y, a), areal_int, cvec,
                                  Xm, th, si[0], si[1], need_K=False)
            v = min(-hP[0, 0], -hM[0, 0])
            if v < mins[f]:
                mins[f] = float(v); argmin[f] = float(th)
    return {f: dict(margin=mins[f], theta=argmin[f]) for f in frames}


# ------------------------------------------------------------------ stress / EC
def lanczos(KP, KM):
    dK = KP - KM
    tr = np.trace(dK)
    S = -(1.0 / (8.0 * np.pi)) * (dK - np.eye(3) * tr)
    return float(-S[0, 0]), float(S[1, 1]), float(S[2, 2]), float(S[0, 1])


def phi_HE(sig, pth, pph, f):
    disc = (sig + pth) ** 2 - 4.0 * f ** 2
    if disc < 0:
        return -float(np.sqrt(-disc)), 4
    root = np.sqrt(disc)
    rho = (sig - pth) / 2.0 + root / 2.0
    p_par = (pth - sig) / 2.0 + root / 2.0
    return float(min(rho - abs(p_par), rho - abs(pph))), 1


def eig_margins(sig, pth, pph, f):
    disc = (sig + pth) ** 2 - 4.0 * f ** 2
    if disc < 0:
        return -float(np.sqrt(-disc)), float(disc)
    root = np.sqrt(disc)
    rho = (sig - pth) / 2.0 + root / 2.0
    p_par = (pth - sig) / 2.0 + root / 2.0
    return float(min(rho - abs(p_par), rho - abs(pph))), float(disc)


def sampled_dec_min(sig, pth, pph, f, n=2000, seed=12):
    rng = np.random.default_rng(seed)
    T = np.array([[sig, -f, 0.0], [-f, pth, 0.0], [0.0, 0.0, pph]])
    best = np.inf
    for _ in range(n):
        vs = []
        for _k in range(2):
            beta = rng.uniform(0.0, 0.999)
            ang = rng.uniform(0.0, 2.0 * np.pi)
            gam = 1.0 / np.sqrt(1.0 - beta ** 2)
            vs.append(gam * np.array([1.0, beta * np.cos(ang), beta * np.sin(ang)]))
        V, W = vs
        best = min(best, float(V @ T @ W) / (V[0] * W[0]))
    return float(best)


def audit_grid():
    """Phase-80-pattern pole-inclusive grid: uniform in mu (161, both pole
    endpoints exact) + rear band [pi-0.15, pi] (41) + front band [0, 0.15] (21)."""
    mu = np.linspace(-1.0, 1.0, 161)
    th = np.arccos(np.clip(mu, -1.0, 1.0))
    rear = np.pi - np.linspace(0.0, 0.15, 41)
    front = np.linspace(0.0, 0.15, 21)
    return np.sort(np.unique(np.concatenate([th, rear, front])))
