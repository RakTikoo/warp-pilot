"""
wb_lib.py — GATE-10 W-B fresh EC auditor + reconstruction machinery for
Le arXiv:2606.22531 (multipole Darmois shell).

Written fresh in gate10/ from the published definitions (paper text v3
Supplement S + the author's published code as the solution SPECIFICATION:
dof layout, box bounds, pins). No phase solver/auditor code is imported
or used as deciding machinery. float64 throughout.

Geometry (per-cut snapshot, t=0 slice, acceleration along +x, R0=1):
  Exterior: Kerr-Schild Kinnersley photon rocket,
    g = eta + (2M/r_a) l l,  l = retarded null covector of the hyperbolic
    worldline z(u) = (sinh(a u)/a, (cosh(a u)-1)/a, 0, 0),
    r_a = -eta(v(u), X - z(u)), v = dz/du (unit timelike, eta(v,v) = -1).
  Interior: flat Rindler cavity, g = diag(-(1 + a x)^2, 1, 1, 1).
  Shell: areal radius R(th) = R0 + sum_{l=1..L} c_l P_l(mu), mu = cos th,
    c_l = lam * R0 * rho_l, lam = a * R0.
  Frame seeds (shared both sides): seed_tau = At * d_t + w * meridian,
    seed_theta = meridian, seed_phi = azimuth; projected orthogonal to
    the unit normal n and Gram-Schmidt orthonormalised in g.
  At_e = 1/sqrt(1-x) + lam * sum_l At_l P_l(mu);  w_e = lam * sum_l w_l S_l
  At_i = 1 + lam * sum_l Ai_l P_l(mu);            w_i = lam * sum_l wi_l S_l
  with S_l(th) = sin(th) P_l'(cos th) = -P_l^1(mu) (exactly 0 at poles).

Method (my implementation): central FD (2nd order; 4th-order variant)
metric derivatives -> algebraic Christoffel -> FD gradient of the unit
normal field -> covariant gradient nabla n -> orthonormal-frame K ->
Lanczos S^a_b -> Hawking-Ellis classification of the (tau,th) block via
its discriminant, Eq.(35)-form worst-observer DEC margin, boosted
eigenvalue margins, sampled-observer DEC and sampled-null NEC checks.
"""
import numpy as np

DTYPE = np.float64
ETA = np.diag([-1.0, 1.0, 1.0, 1.0]).astype(DTYPE)
R0 = 1.0


# ------------------------------------------------------------ worldline
def _z(u, a):
    if abs(a) < 1e-14:
        return np.array([u, 0.0, 0.0, 0.0], dtype=DTYPE)
    return np.array([np.sinh(a * u) / a, (np.cosh(a * u) - 1.0) / a, 0.0, 0.0],
                    dtype=DTYPE)


def _v(u, a):
    if abs(a) < 1e-14:
        return np.array([1.0, 0.0, 0.0, 0.0], dtype=DTYPE)
    return np.array([np.cosh(a * u), np.sinh(a * u), 0.0, 0.0], dtype=DTYPE)


def retarded(X, a):
    """Newton solve of eta(X-z(u), X-z(u)) = 0 (past cone). Returns (u, r_a, D)."""
    X = np.asarray(X, dtype=DTYPE)
    u = X[0] - np.sqrt(X[1] ** 2 + X[2] ** 2 + X[3] ** 2)
    for _ in range(80):
        D = X - _z(u, a)
        F = float(D @ ETA @ D)
        ra = -float(_v(u, a) @ ETA @ D)
        if ra <= 0:
            ra = 1e-12
        step = -F / (2.0 * ra)
        u += step
        if abs(step) < 1e-15:
            break
    D = X - _z(u, a)
    ra = -float(_v(u, a) @ ETA @ D)
    return u, ra, D


def metric_ext(X, a, M):
    X = np.asarray(X, dtype=DTYPE)
    if M == 0.0:
        return ETA.copy()
    _, ra, D = retarded(X, a)
    lc = ETA @ (D / ra)
    return ETA + (2.0 * M / ra) * np.outer(lc, lc)


def metric_int(X, a):
    X = np.asarray(X, dtype=DTYPE)
    g = ETA.copy()
    N = 1.0 + a * X[1]
    g[0, 0] = -N * N
    return g


def areal_ext(X, a):
    return retarded(X, a)[1]


def areal_int(X):
    X = np.asarray(X, dtype=DTYPE)
    return float(np.sqrt(X[1] ** 2 + X[2] ** 2 + X[3] ** 2))


# ------------------------------------------------------------ harmonics
def legendre_P(mu, L):
    """[P_0(mu), ..., P_L(mu)] by Bonnet recurrence."""
    mu = float(mu)
    P = [1.0]
    if L >= 1:
        P.append(mu)
    for l in range(2, L + 1):
        P.append(((2 * l - 1) * mu * P[-1] - (l - 1) * P[-2]) / l)
    return P


def legendre_S(mu, L):
    """[S_1(mu), ..., S_L(mu)], S_l = -P_l^1(mu); P_l^1 by the m=1 recurrence.
    sqrt(1-mu^2) factor makes every S_l exactly 0 at mu = +/-1."""
    mu = float(mu)
    if L == 0:
        return []
    s = np.sqrt(max(0.0, 1.0 - mu * mu))
    Pm1 = [0.0] * (L + 1)          # P_l^1 table
    if L >= 1:
        Pm1[1] = -s
    for l in range(2, L + 1):
        Pm1[l] = ((2 * l - 1) * mu * Pm1[l - 1] - l * Pm1[l - 2]) / (l - 1)
    return [-Pm1[l] for l in range(1, L + 1)]


# ------------------------------------------------------------ FD tools
def fd_jac(field, X, h, order=2):
    """J[i, mu] = d_mu field_i (central differences)."""
    X = np.asarray(X, dtype=DTYPE)
    J = np.zeros((len(field(X)), 4), dtype=DTYPE)
    for mu in range(4):
        e = np.zeros(4, dtype=DTYPE); e[mu] = h
        if order == 2:
            J[:, mu] = (field(X + e) - field(X - e)) / (2.0 * h)
        else:
            J[:, mu] = (-field(X + 2 * e) + 8.0 * field(X + e)
                        - 8.0 * field(X - e) + field(X - 2 * e)) / (12.0 * h)
    return J


def christoffel(metric_fn, X, h, order=2):
    """Gamma^l_{mn} from FD metric derivatives (algebraic assembly)."""
    X = np.asarray(X, dtype=DTYPE)
    g = metric_fn(X)
    gi = np.linalg.inv(g)
    dg = np.zeros((4, 4, 4), dtype=DTYPE)          # dg[mu] = d_mu g_{nu s}
    for mu in range(4):
        e = np.zeros(4, dtype=DTYPE); e[mu] = h
        if order == 2:
            dg[mu] = (metric_fn(X + e) - metric_fn(X - e)) / (2.0 * h)
        else:
            dg[mu] = (-metric_fn(X + 2 * e) + 8.0 * metric_fn(X + e)
                      - 8.0 * metric_fn(X - e) + metric_fn(X - 2 * e)) / (12.0 * h)
    # A[m, n, s] = d_m g_{ns} + d_n g_{ms} - d_s g_{mn}
    A = dg + np.transpose(dg, (1, 0, 2)) - np.transpose(dg, (1, 2, 0))
    return 0.5 * np.einsum("ls,mns->lmn", gi, A)


# ------------------------------------------------- analytic-gradient path
def _dP_dmu(mu, L):
    """[P'_1(mu), ..., P'_L(mu)] via P'_l = l (mu P_l - P_{l-1}) / (mu^2 - 1),
    with the exact pole limits P'_l(+/-1) = (+/-1)^{l+1} l(l+1)/2."""
    P = legendre_P(mu, L)
    out = []
    for l in range(1, L + 1):
        if abs(1.0 - mu * mu) < 1e-12:
            sgn = 1.0 if mu > 0 else (-1.0) ** (l + 1)
            out.append(sgn * l * (l + 1) / 2.0)
        else:
            out.append(l * (mu * P[l] - P[l - 1]) / (mu * mu - 1.0))
    return out


def _dPhi_analytic(Y, areal_grad, cvec):
    """Gradient of Phi(Y) = areal(Y) - (R0 + sum_l c_l P_l(mu)), mu = Y1/|Y_sp|.
    areal_grad(Y) supplies the areal function's gradient covector:
    exterior = retarded null covector l (exact identity grad r_a = l);
    interior = (0, Y_sp/|Y_sp|)."""
    Y = np.asarray(Y, dtype=DTYPE)
    L = len(cvec)
    rho = np.sqrt(Y[1] ** 2 + Y[2] ** 2 + Y[3] ** 2)
    mu = Y[1] / rho if rho > 0 else 1.0
    dP = _dP_dmu(mu, L)
    dshape_dmu = float(sum(cvec[l - 1] * dP[l - 1] for l in range(1, L + 1)))
    # dmu/dY: time 0; spatial (delta_{1j} - mu * n_j) / rho, n = Y_sp/rho
    n = Y[1:] / rho
    dmu = np.zeros(4, dtype=DTYPE)
    dmu[1:] = (np.array([1.0, 0.0, 0.0]) - mu * n) / rho
    return areal_grad(Y) - dshape_dmu * dmu


def _areal_grad_ext(Y, a):
    """Exact gradient of the retarded areal radius r_a.
    With u the retarded time, D = Y - z(u), l_mu = D_mu / r_a (covariant),
    v the worldline 4-velocity and n(u) = (sinh(a u), cosh(a u), 0, 0) the
    unit spacelike normal to v in the t-x plane:
        d_mu r_a = -v_mu + l_mu * (1 + a * eta(n, D)).
    (Derived from eta(D, D) = 0 -> d_mu u = -l_mu; verified against FD in
    wb_validate_fast.py V1.)"""
    u, ra, D = retarded(Y, a)
    if abs(a) < 1e-14:
        return ETA @ (D / ra)
    v_cov = ETA @ _v(u, a)
    n_vec = np.array([np.sinh(a * u), np.cosh(a * u), 0.0, 0.0], dtype=DTYPE)
    l_cov = ETA @ (D / ra)
    return -v_cov + l_cov * (1.0 + a * float(n_vec @ ETA @ D))


def _areal_grad_int(Y):
    Y = np.asarray(Y, dtype=DTYPE)
    rho = np.sqrt(Y[1] ** 2 + Y[2] ** 2 + Y[3] ** 2)
    g = np.zeros(4, dtype=DTYPE)
    g[1:] = Y[1:] / rho
    return g


def _make_nfield_fast(metric_fn, areal_grad, cvec):
    def nfield(Y):
        Y = np.asarray(Y, dtype=DTYPE)
        dPhi = _dPhi_analytic(Y, areal_grad, cvec)
        gi = np.linalg.inv(metric_fn(Y))
        return dPhi / np.sqrt(float(dPhi @ gi @ dPhi))
    return nfield


def induced_and_K_fast(side, a, M, cvec, X, th, At, w, h=0.01, order=2):
    """Same construction as induced_and_K but the unit normal is built from
    the ANALYTIC Phi gradient (validated against the FD path in
    wb_validate_fast.py). side in {'ext', 'int'}."""
    if side == "ext":
        metric_fn = lambda Y: metric_ext(Y, a, M)
        areal_grad = lambda Y: _areal_grad_ext(Y, a)
    else:
        metric_fn = lambda Y: metric_int(Y, a)
        areal_grad = _areal_grad_int
    X = np.asarray(X, dtype=DTYPE)
    nfield = _make_nfield_fast(metric_fn, areal_grad, cvec)
    n_low = nfield(X)
    g = metric_fn(X)
    gi = np.linalg.inv(g)
    n_up = gi @ n_low
    dn = fd_jac(nfield, X, h, order)
    Gam = christoffel(metric_fn, X, h, order)
    gradn = dn.T - np.einsum("lmn,l->mn", Gam, n_low)
    gradn = 0.5 * (gradn + gradn.T)
    Proj = np.eye(4) - np.outer(n_up, n_low)
    sth, cth = np.sin(th), np.cos(th)
    merid = np.array([0.0, -sth, cth, 0.0], dtype=DTYPE)
    azim = np.array([0.0, 0.0, 0.0, 1.0], dtype=DTYPE)
    seed_tau = At * np.array([1.0, 0.0, 0.0, 0.0], dtype=DTYPE) + w * merid
    E = [Proj @ s for s in (seed_tau, merid, azim)]
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
    return hab, np.diag([-1.0, 1.0, 1.0]) @ Kab


def sample_shell_fast(x, lam, p, L, thetas, h=0.01, order=2):
    """sample_shell with the analytic-gradient normal (fast path)."""
    a = lam / R0
    M = x * R0 / 2.0
    At0 = 1.0 / np.sqrt(1.0 - x)
    rho, At, w, wi, Ai = unpack(p, L)
    cvec = lam * R0 * np.asarray(rho, dtype=DTYPE)
    out = {k: [] for k in ("th", "hP", "KP", "hM", "KM")}
    for th in thetas:
        mu = float(np.cos(th))
        P = legendre_P(mu, L)
        S = legendre_S(mu, L)
        Rt = R0 + float(sum(cvec[l - 1] * P[l] for l in range(1, L + 1)))
        Xp = exterior_point(a, th, Rt)
        Xm = np.array([0.0, Rt * np.cos(th), Rt * np.sin(th), 0.0], dtype=DTYPE)
        At_e = At0 + lam * float(sum(At[l - 1] * P[l] for l in range(1, L + 1)))
        w_e = lam * float(sum(w[l - 1] * S[l - 1] for l in range(1, L + 1)))
        At_i = 1.0 + lam * float(sum(Ai[l - 1] * P[l] for l in range(1, L + 1)))
        w_i = lam * float(sum(wi[l - 1] * S[l - 1] for l in range(1, L + 1)))
        hP, KP = induced_and_K_fast("ext", a, M, cvec, Xp, th, At_e, w_e,
                                    h=h, order=order)
        hM, KM = induced_and_K_fast("int", a, M, cvec, Xm, th, At_i, w_i,
                                    h=h, order=order)
        out["th"].append(float(th)); out["hP"].append(hP); out["KP"].append(KP)
        out["hM"].append(hM); out["KM"].append(KM)
    for k in ("hP", "KP", "hM", "KM"):
        out[k] = np.array(out[k])
    out["th"] = np.array(out["th"])
    return out


def sample_one_fast(args):
    x, lam, p, L, th, h, order = args
    r = sample_shell_fast(x, lam, np.asarray(p, dtype=DTYPE), L, [th],
                          h=h, order=order)
    return r["hP"][0], r["KP"][0], r["hM"][0], r["KM"][0]


# ------------------------------------------------------------ shell core
def _make_Phi(areal_fn, cvec):
    L = len(cvec)

    def Phi(Y):
        Y = np.asarray(Y, dtype=DTYPE)
        rho = np.sqrt(Y[1] ** 2 + Y[2] ** 2 + Y[3] ** 2)
        mu = Y[1] / rho if rho > 0 else 1.0
        P = legendre_P(mu, L)
        shape = R0 + sum(cvec[l - 1] * P[l] for l in range(1, L + 1))
        return areal_fn(Y) - shape
    return Phi


def _make_nfield(metric_fn, areal_fn, cvec):
    Phi = _make_Phi(areal_fn, cvec)

    def nfield(Y):
        Y = np.asarray(Y, dtype=DTYPE)
        dPhi = fd_jac(lambda Z: np.array([Phi(Z)]), Y, 1e-6)[0]
        gi = np.linalg.inv(metric_fn(Y))
        return dPhi / np.sqrt(float(dPhi @ gi @ dPhi))
    return nfield


def induced_and_K(metric_fn, areal_fn, cvec, X, th, At, w, h=0.01, order=2):
    """(h_ab in raw shared-seed basis, K^a_b in orthonormal frame) at X."""
    X = np.asarray(X, dtype=DTYPE)
    nfield = _make_nfield(metric_fn, areal_fn, cvec)
    n_low = nfield(X)
    g = metric_fn(X)
    gi = np.linalg.inv(g)
    n_up = gi @ n_low
    dn = fd_jac(nfield, X, h, order)                       # dn[nu, mu]
    Gam = christoffel(metric_fn, X, h, order)
    gradn = dn.T - np.einsum("lmn,l->mn", Gam, n_low)      # nabla_mu n_nu
    gradn = 0.5 * (gradn + gradn.T)

    Proj = np.eye(4) - np.outer(n_up, n_low)
    sth, cth = np.sin(th), np.cos(th)
    merid = np.array([0.0, -sth, cth, 0.0], dtype=DTYPE)
    azim = np.array([0.0, 0.0, 0.0, 1.0], dtype=DTYPE)
    seed_tau = At * np.array([1.0, 0.0, 0.0, 0.0], dtype=DTYPE) + w * merid
    E = [Proj @ s for s in (seed_tau, merid, azim)]
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
    return hab, np.diag([-1.0, 1.0, 1.0]) @ Kab


def exterior_point(a, th, Rt):
    """t=0 point with exact exterior areal radius Rt (Newton on spatial radius q)."""
    cth, sth = np.cos(th), np.sin(th)
    q = float(Rt)
    for _ in range(60):
        val = areal_ext(np.array([0.0, q * cth, q * sth, 0.0], dtype=DTYPE), a)
        dq = 1e-7
        der = (areal_ext(np.array([0.0, (q + dq) * cth, (q + dq) * sth, 0.0],
                                  dtype=DTYPE), a) - val) / dq
        step = (val - Rt) / der
        q -= step
        if abs(step) < 1e-14:
            break
    return np.array([0.0, q * cth, q * sth, 0.0], dtype=DTYPE)


def sample_one(args):
    """Top-level (picklable) single-theta sample: returns (hP, KP, hM, KM)."""
    x, lam, p, L, th, h, order = args
    r = sample_shell(x, lam, np.asarray(p, dtype=DTYPE), L, [th], h=h, order=order)
    return r["hP"][0], r["KP"][0], r["hM"][0], r["KM"][0]


def unpack(p, L):
    """Published layout: [rho, At, w, wi, Ai], each l = 1..L (interior tilt
    and interior lapse ON, per the published specification)."""
    p = np.asarray(p, dtype=DTYPE)
    return p[0:L], p[L:2 * L], p[2 * L:3 * L], p[3 * L:4 * L], p[4 * L:5 * L]


def sample_shell(x, lam, p, L, thetas, h=0.01, order=2):
    """h and K on both sides over thetas for parameter vector p."""
    a = lam / R0
    M = x * R0 / 2.0
    At0 = 1.0 / np.sqrt(1.0 - x)
    rho, At, w, wi, Ai = unpack(p, L)
    cvec = lam * R0 * np.asarray(rho, dtype=DTYPE)
    out = {k: [] for k in ("th", "hP", "KP", "hM", "KM")}
    for th in thetas:
        mu = float(np.cos(th))
        P = legendre_P(mu, L)
        S = legendre_S(mu, L)
        Rt = R0 + float(sum(cvec[l - 1] * P[l] for l in range(1, L + 1)))
        Xp = exterior_point(a, th, Rt)
        Xm = np.array([0.0, Rt * np.cos(th), Rt * np.sin(th), 0.0], dtype=DTYPE)
        At_e = At0 + lam * float(sum(At[l - 1] * P[l] for l in range(1, L + 1)))
        w_e = lam * float(sum(w[l - 1] * S[l - 1] for l in range(1, L + 1)))
        At_i = 1.0 + lam * float(sum(Ai[l - 1] * P[l] for l in range(1, L + 1)))
        w_i = lam * float(sum(wi[l - 1] * S[l - 1] for l in range(1, L + 1)))
        hP, KP = induced_and_K(lambda Y: metric_ext(Y, a, M),
                               lambda Y: areal_ext(Y, a), cvec, Xp, th,
                               At_e, w_e, h=h, order=order)
        hM, KM = induced_and_K(lambda Y: metric_int(Y, a), areal_int, cvec,
                               Xm, th, At_i, w_i, h=h, order=order)
        out["th"].append(float(th)); out["hP"].append(hP); out["KP"].append(KP)
        out["hM"].append(hM); out["KM"].append(KM)
    for k in ("hP", "KP", "hM", "KM"):
        out[k] = np.array(out[k])
    out["th"] = np.array(out["th"])
    return out


# ------------------------------------------------------------ EC auditor
def lanczos(KP, KM):
    """S^a_b = -(1/8pi)([K^a_b] - delta^a_b [K]); -> (sigma, p_th, p_ph, flux)."""
    dK = np.asarray(KP, dtype=DTYPE) - np.asarray(KM, dtype=DTYPE)
    S = -(1.0 / (8.0 * np.pi)) * (dK - np.eye(3) * np.trace(dK))
    return float(-S[0, 0]), float(S[1, 1]), float(S[2, 2]), float(S[0, 1])


def phi_HE(sig, pth, pph, f):
    """Eq.(35)-form worst-observer DEC margin + Hawking-Ellis type.
    disc < 0 -> Type IV (margin = -sqrt(-disc))."""
    disc = (sig + pth) ** 2 - 4.0 * f ** 2
    if disc < 0:
        return float(-np.sqrt(-disc)), 4
    root = np.sqrt(disc)
    rho = (sig - pth) / 2.0 + root / 2.0
    ppar = (pth - sig) / 2.0 + root / 2.0
    return float(min(rho - abs(ppar), rho - abs(pph))), 1


def eig_data(sig, pth, pph, f):
    """Boosted eigenvalues of the (tau,th) block + all DEC eigenvalue margins."""
    disc = (sig + pth) ** 2 - 4.0 * f ** 2
    if disc < 0:
        return dict(disc=float(disc), rho=None, ppar=None,
                    margins=[float(-np.sqrt(-disc))] * 2)
    root = np.sqrt(disc)
    rho = (sig - pth) / 2.0 + root / 2.0
    ppar = (pth - sig) / 2.0 + root / 2.0
    return dict(disc=float(disc), rho=float(rho), ppar=float(ppar),
                margins=[float(rho - abs(ppar)), float(rho - abs(pph))])


def sampled_null_min(sig, pth, pph, f, npsi=720):
    """Sampled-null NEC cross-check: min over null directions k=(1, cos psi,
    sin psi) in the orthonormal frame of T_ab k^a k^b (covariant T with flux
    in the tau-th plane). NEC holds at the point iff this min >= 0."""
    psi = np.linspace(0.0, 2.0 * np.pi, npsi, endpoint=False)
    c, s = np.cos(psi), np.sin(psi)
    vals = sig - 2.0 * f * c + pth * c ** 2 + pph * s ** 2
    return float(np.min(vals))


def sampled_dec_min(sig, pth, pph, f, n=600, seed=1102):
    """Sampled-observer DEC cross-check: min over sampled future-causal pairs
    (V, W) of T(V, W) / (V^0 W^0) in the orthonormal frame."""
    rng = np.random.default_rng(seed)
    T = np.array([[sig, -f, 0.0], [-f, pth, 0.0], [0.0, 0.0, pph]], dtype=DTYPE)
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


def anchor_closed(x):
    """Paper Eqs.(22)-(23) static shell values at R = 1."""
    s = np.sqrt(1.0 - x)
    return (float((1.0 - s) / (4.0 * np.pi * R0)),
            float(((1.0 - x / 2.0) / s - 1.0) / (8.0 * np.pi * R0)))


def audit_grid():
    """REGISTERED (Gate-10, before running): uniform in mu = cos th, 161 pts,
    BOTH pole endpoints included exactly (mu = +/-1), plus refined bands
    th in [pi-0.15, pi] (41 pts) and th in [0, 0.15] (21 pts)."""
    mu = np.linspace(-1.0, 1.0, 161)
    th = np.arccos(np.clip(mu, -1.0, 1.0))
    rear = np.pi - np.linspace(0.0, 0.15, 41)
    front = np.linspace(0.0, 0.15, 21)
    return np.sort(np.unique(np.concatenate([th, rear, front])))
