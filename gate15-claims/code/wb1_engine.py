"""
W-B1 (Gate-15) independent Bach engine. Written from scratch for Gate-15.

Derivation summary
------------------
Metric (static, axisymmetric, diagonal, coordinates t,r,theta,phi):
    g = diag(-A(r,th), Bm(r,th), r^2 E(r,th), r^2 sin^2(th) E(r,th))
All tensor fields are represented as multivariate Taylor jets in (r,theta)
at the evaluation point.  A jet field carries, for every Taylor coefficient,
a value channel (channel 0) plus one linearisation channel per perturbation
unknown (channels 1..N): channel j is d(field)/d(unknown_j) evaluated on the
background.  This is exact linearisation (dual-number jet algebra written
here), not finite differencing in the perturbation amplitude.

Tensor chain (standard definitions, Riemann sign
R^k_{lmn} = d_m G^k_{ln} - d_n G^k_{lm} + G G - G G, Ricci R_{ln}=R^k_{lkn}):
    metric jet (order 4) -> Christoffel (order 3) -> Riemann (order 2)
    -> Ricci / Schouten / Weyl (order 2)
    -> first covariant derivative of Weyl, contracted on the derivative
       index with Weyl's second index:  S_{mn s} = nabla^rho C_{m rho n s}
       (kept to jet order 1)
    -> covariant derivative of S (jet order 0), contracted:
       (nabla^rho nabla^sigma C_{m rho n sigma}) = nabla^sigma S_{m n sigma}
    -> registered Bach (Gate-9 erratum 3 convention):
       B_{mn} = 2 * nabla^rho nabla^sigma C_{m rho n sigma}
                + R^{rho sigma} C_{m rho n sigma}
Staged truncation: a field kept to jet order q has exact Taylor coefficients
to order q whenever its definition involves metric derivatives to order
q + (its differential order); the stages above respect that, so the final
order-0 Bach value and its linearisation channels are exact functions of the
metric 4-jet.
"""
import numpy as np
from math import comb, factorial

BETA = 2.142611
GAMMA = 1e-28
KPAR = -2.28996e-9
RSIG = 1000.0

# ---------------- jet monomial bookkeeping ----------------
_MON = {}
def mons(order):
    if order not in _MON:
        lst = [(i, j) for d in range(order + 1) for i in range(d + 1)
               for j in (d - i,)]
        # the comprehension above yields (i, d-i); rebuild cleanly:
        lst = []
        for d in range(order + 1):
            for i in range(d + 1):
                lst.append((i, d - i))
        _MON[order] = lst
    return _MON[order]

def mon_idx(order):
    return {m: n for n, m in enumerate(mons(order))}

def new_jet(shape, order, W):
    return np.zeros(tuple(shape) + (len(mons(order)), W))

def jet_slice(A, oa, oo):
    if oa == oo:
        return A
    ia = mon_idx(oa); io = mon_idx(oo)
    out = np.zeros(A.shape[:-2] + (len(mons(oo)), A.shape[-1]))
    for m, n in io.items():
        out[..., n, :] = A[..., ia[m], :]
    return out

def jet_deriv(A, oa, var):
    """Derivative wrt coordinate var (0=r,1=theta); output order oa-1."""
    oo = oa - 1
    ia = mon_idx(oa); io = mon_idx(oo)
    out = np.zeros(A.shape[:-2] + (len(mons(oo)), A.shape[-1]))
    for (i, j), n in io.items():
        if var == 0:
            out[..., n, :] = (i + 1) * A[..., ia[(i + 1, j)], :]
        else:
            out[..., n, :] = (j + 1) * A[..., ia[(i, j + 1)], :]
    return out

def _vec_mul(a, b):
    """Product of (value + linear channels) vectors along last axis."""
    out = np.empty(np.broadcast_shapes(a.shape, b.shape))
    av = a[..., 0:1]; bv = b[..., 0:1]
    out[..., 0:1] = av * bv
    if a.shape[-1] > 1:
        out[..., 1:] = av * b[..., 1:] + a[..., 1:] * bv
    return out

def jet_mul(A, B, oa, ob, oo):
    """Truncated jet product; leading axes broadcast."""
    ma = mons(oa); mb = mons(ob); mo = mon_idx(oo)
    lead = np.broadcast_shapes(A.shape[:-2], B.shape[:-2])
    W = A.shape[-1]
    out = np.zeros(lead + (len(mo), W))
    for na, (ia_, ja_) in enumerate(ma):
        for nb, (ib_, jb_) in enumerate(mb):
            s = (ia_ + ib_, ja_ + jb_)
            if s not in mo:
                continue
            out[..., mo[s], :] += _vec_mul(A[..., na, :], B[..., nb, :])
    return out

def jet_mm(A, B, oa, ob, oo):
    """Contract last axis of A (I,K) with first axis of B (K,J), jet product."""
    I, K = A.shape[0], A.shape[1]
    J = B.shape[1]
    W = A.shape[-1]
    out = np.zeros((I, J, len(mons(oo)), W))
    for k in range(K):
        out += jet_mul(A[:, k][:, None, :, :], B[k, :][None, :, :, :],
                       oa, ob, oo)
    return out

def jet_inv(A, order):
    """Inverse of a jet field with nonzero value at the point."""
    mo = mons(order); idx = mon_idx(order)
    out = np.zeros_like(A)
    # monomials are ordered by total degree, so lower degrees come first
    for n, (i, j) in enumerate(mo):
        acc = np.zeros(A.shape[:-2] + (A.shape[-1],))
        for na, (ia_, ja_) in enumerate(mo):
            for nb, (ib_, jb_) in enumerate(mo):
                if na == 0 or nb >= n:
                    continue
                if (ia_ + ib_, ja_ + jb_) == (i, j):
                    acc += _vec_mul(A[..., na, :], out[..., nb, :])
        if n == 0:
            rhs = np.zeros(A.shape[:-2] + (A.shape[-1],))
            rhs[..., 0] = 1.0
        else:
            rhs = -acc
        a0 = A[..., 0, 0]
        out[..., n, 0] = rhs[..., 0] / a0
        if A.shape[-1] > 1:
            out[..., n, 1:] = (rhs[..., 1:] - out[..., n, 0] * A[..., 0, 1:]) / a0
    return out

# ---------------- Legendre angular jets ----------------
_PDERIV = {}
def legendre_theta_derivs(ell, th):
    """[P, dP/dth, d2P/dth2, d3P/dth3, d4P/dth4] at theta=th."""
    if ell not in _PDERIV:
        import sympy as sp
        t = sp.symbols('t')
        expr = sp.legendre(ell, sp.cos(t))
        fs = []
        e = expr
        for _ in range(5):
            fs.append(sp.lambdify(t, e, 'numpy'))
            e = sp.diff(e, t)
        _PDERIV[ell] = fs
    return [float(f(th)) for f in _PDERIV[ell]]

def legendre_P(ell, mu):
    from numpy.polynomial.legendre import legval
    c = np.zeros(ell + 1); c[ell] = 1.0
    return float(legval(mu, c))

# ---------------- background f(r) ----------------
def f_and_derivs(r, beta=BETA, gamma=GAMMA, k=KPAR):
    C = beta * (2 - 3 * beta * gamma)
    f = 1 - 3 * beta * gamma - C / r + gamma * r - k * r**2
    d = [f]
    # d^i/dr^i of -C/r is -C * (-1)^i i! r^{-1-i}; gamma r only i=1; -k r^2 i=1,2
    for i in range(1, 5):
        v = -C * ((-1) ** i) * factorial(i) * r ** (-1 - i)
        if i == 1:
            v += gamma - 2 * k * r
        if i == 2:
            v += -2 * k
        d.append(v)
    return d

# ---------------- metric jet builder ----------------
def build_metric(r, th, ell=None, center=None, K=8, nunk=0,
                 value_coeffs=None, params=(BETA, GAMMA, KPAR)):
    """
    Returns g, ginv as arrays (4,4,15,W) of order-4 jets at (r,th).
    If nunk>0: perturbation unknowns are the Taylor coefficients
      U(r) = sum_k u_k ((r-center)/center)^k   (channels 1..K+1)
      V(r) = sum_k v_k ...                    (next K+1 channels)
      Wfun(r) = sum_k w_k ...                 (next K+1 channels, ell>=1)
    If value_coeffs is given (dict with arrays 'U','V','W'), the perturbation
    is instead carried in the value channel with those numeric coefficients
    (for finite-amplitude checks).
    """
    W = 1 + nunk
    idx4 = mon_idx(4)
    beta, gamma, kpar = params
    fd = f_and_derivs(r, beta, gamma, kpar)
    fjet = new_jet((), 4, W)
    for i in range(5):
        fjet[idx4[(i, 0)], 0] = fd[i] / factorial(i)
    bmjet = jet_inv(fjet, 4)
    Ajet = fjet.copy()
    Ejet = new_jet((), 4, W); Ejet[idx4[(0, 0)], 0] = 1.0
    if ell is not None:
        pd = legendre_theta_derivs(ell, th)
        Pjet = new_jet((), 4, W)
        for j in range(5):
            Pjet[idx4[(0, j)], 0] = pd[j] / factorial(j)
        X = (r - center) / center
        def radial_jet(chan0):
            rj = new_jet((), 4, W)
            for kk in range(K + 1):
                for i in range(min(kk, 4) + 1):
                    c = comb(kk, i) * X ** (kk - i) / center ** i
                    if value_coeffs is not None:
                        rj[idx4[(i, 0)], 0] += value_coeffs['UVW'[chan0]][kk] * c
                    else:
                        ch = 1 + chan0 * (K + 1) + kk
                        rj[idx4[(i, 0)], ch] += c
            return rj
        Ajet = Ajet + jet_mul(radial_jet(0), Pjet, 4, 4, 4)
        bmjet = bmjet + jet_mul(radial_jet(1), Pjet, 4, 4, 4)
        if ell >= 1:
            Ejet = Ejet + jet_mul(radial_jet(2), Pjet, 4, 4, 4)
    r2jet = new_jet((), 4, W)
    r2jet[idx4[(0, 0)], 0] = r**2
    r2jet[idx4[(1, 0)], 0] = 2 * r
    r2jet[idx4[(2, 0)], 0] = 1.0
    s2jet = new_jet((), 4, W)
    s2 = np.sin(th) ** 2
    ders = [s2, np.sin(2 * th), 2 * np.cos(2 * th), -4 * np.sin(2 * th),
            -8 * np.cos(2 * th)]
    for j in range(5):
        s2jet[idx4[(0, j)], 0] = ders[j] / factorial(j)
    g = np.zeros((4, 4, len(mons(4)), W))
    g[0, 0] = -Ajet
    g[1, 1] = bmjet
    g[2, 2] = jet_mul(r2jet, Ejet, 4, 4, 4)
    g[3, 3] = jet_mul(jet_mul(r2jet, s2jet, 4, 4, 4), Ejet, 4, 4, 4)
    ginv = np.zeros_like(g)
    for a in range(4):
        ginv[a, a] = jet_inv(g[a, a], 4)
    return g, ginv

# ---------------- Bach tensor ----------------
DEBUG = {}
def bach_mixed(g, ginv, debug=False):
    """Returns B^mu_nu as array (4,4,W): order-0 jet of the mixed Bach tensor
    in the registered convention B = 2 divdiv C + R.C."""
    W = g.shape[-1]
    # Christoffel, order 3
    D = np.stack([jet_deriv(g, 4, 0), jet_deriv(g, 4, 1)], axis=0)
    # D[var,a,b]; pad theta-derivative var index: coordinates are (t,r,th,phi)
    # but metric depends only on (r,th) = vars (1,2). Build full Dfull[4,4,4].
    Dfull = np.zeros((4, 4, 4, len(mons(3)), W))
    Dfull[1] = D[0]
    Dfull[2] = D[1]
    T = (Dfull + np.transpose(Dfull, (1, 0, 2, 3, 4))
         - np.transpose(Dfull, (2, 1, 0, 3, 4)))  # T[i,j,l] = d_i g_jl + d_j g_il - d_l g_ij
    Gam = 0.5 * jet_mm(ginv.reshape(4, 4, len(mons(4)), W),
                       np.transpose(T, (2, 0, 1, 3, 4)).reshape(4, 16, len(mons(3)), W), 4, 3, 3)
    Gam = Gam.reshape(4, 4, 4, len(mons(3)), W)  # Gam[k,i,j]
    # Riemann, order 2
    DG = np.zeros((4, 4, 4, 4, len(mons(2)), W))
    DG[1] = jet_deriv(Gam, 3, 0)
    DG[2] = jet_deriv(Gam, 3, 1)
    Gam2 = jet_slice(Gam, 3, 2)
    p1 = jet_mm(np.transpose(Gam2, (0, 1, 2, 3, 4)).reshape(16, 4, len(mons(2)), W),
                Gam2.reshape(4, 16, len(mons(2)), W), 2, 2, 2)  # (k,m),(l,n)
    p1 = np.transpose(p1.reshape(4, 4, 4, 4, len(mons(2)), W), (0, 2, 1, 3, 4, 5))
    p2 = jet_mm(np.transpose(Gam2, (0, 2, 1, 3, 4)).reshape(16, 4, len(mons(2)), W),
                Gam2.reshape(4, 16, len(mons(2)), W), 2, 2, 2)  # (k,n),(l,m)
    p2 = np.transpose(p2.reshape(4, 4, 4, 4, len(mons(2)), W), (0, 2, 3, 1, 4, 5))
    Riem = DG[:, :, :, :, :, :]  # placeholder shape fix below
    Riem = np.zeros((4, 4, 4, 4, len(mons(2)), W))
    # R^k_{lmn} = d_m Gam^k_{ln} - d_n Gam^k_{lm} + ...
    Riem = (np.transpose(DG, (1, 2, 0, 3, 4, 5)) - np.transpose(DG, (1, 2, 3, 0, 4, 5))
            + p1 - p2)
    Ric = np.trace(Riem, axis1=0, axis2=2)  # Ric[l,n], shape (4,4,n2,W)
    g2 = jet_slice(g, 4, 2); gi2 = jet_slice(ginv, 4, 2)
    Rs = np.zeros((len(mons(2)), W))
    tmp = jet_mul(gi2, Ric, 2, 2, 2)
    Rs = tmp.sum(axis=(0, 1))
    P = 0.5 * (Ric - (1.0 / 6.0) * jet_mul(Rs[None, None], g2, 2, 2, 2))
    Rcov = jet_mm(g2.reshape(4, 4, len(mons(2)), W),
                  Riem.reshape(4, 64, len(mons(2)), W), 2, 2, 2)
    Rcov = Rcov.reshape(4, 4, 4, 4, len(mons(2)), W)
    # Kulkarni-Nomizu (g (x) P)_{abcd} = g_ac P_bd + g_bd P_ac - g_ad P_bc - g_bc P_ad
    # Build each term with explicit axis placement:
    def place(M, ax_out):
        # M is (4,4,n,W) with axes (x,y); place into (4,4,4,4) at positions ax_out
        shp = [1, 1, 1, 1]
        shp[ax_out[0]] = 4; shp[ax_out[1]] = 4
        return M.reshape(shp[0], shp[1], shp[2], shp[3], M.shape[2], M.shape[3])
    KN = (jet_mul(place(g2, (0, 2)), place(P, (1, 3)), 2, 2, 2)
          + jet_mul(place(g2, (1, 3)), place(P, (0, 2)), 2, 2, 2)
          - jet_mul(place(g2, (0, 3)), place(P, (1, 2)), 2, 2, 2)
          - jet_mul(place(g2, (1, 2)), place(P, (0, 3)), 2, 2, 2))
    Weyl = Rcov - KN
    # First covariant derivative of Weyl, order 1
    C1 = jet_slice(Weyl, 2, 1)
    dC = np.zeros((4, 4, 4, 4, 4, len(mons(1)), W))
    dC[1] = jet_deriv(Weyl, 2, 0)
    dC[2] = jet_deriv(Weyl, 2, 1)
    Gam1 = jet_slice(Gam, 3, 1)
    A2 = np.transpose(Gam1, (1, 2, 0, 3, 4)).reshape(16, 4, len(mons(1)), W)
    DC = dC.copy()
    # slot 0 (index a): C[t,b,c,d]
    t1 = jet_mm(A2, C1.reshape(4, 64, len(mons(1)), W), 1, 1, 1)
    DC -= t1.reshape(4, 4, 4, 4, 4, len(mons(1)), W)
    # slot 1 (index b): C[a,t,c,d]
    t2 = jet_mm(A2, np.transpose(C1, (1, 0, 2, 3, 4, 5)).reshape(4, 64, len(mons(1)), W), 1, 1, 1)
    DC -= np.transpose(t2.reshape(4, 4, 4, 4, 4, len(mons(1)), W), (0, 2, 1, 3, 4, 5, 6))
    # slot 2 (index c): C[a,b,t,d]
    t3 = jet_mm(A2, np.transpose(C1, (2, 0, 1, 3, 4, 5)).reshape(4, 64, len(mons(1)), W), 1, 1, 1)
    DC -= np.transpose(t3.reshape(4, 4, 4, 4, 4, len(mons(1)), W), (0, 2, 3, 1, 4, 5, 6))
    # slot 3 (index d): C[a,b,c,t]
    t4 = jet_mm(A2, np.transpose(C1, (3, 0, 1, 2, 4, 5)).reshape(4, 64, len(mons(1)), W), 1, 1, 1)
    DC -= np.transpose(t4.reshape(4, 4, 4, 4, 4, len(mons(1)), W), (0, 2, 3, 4, 1, 5, 6))
    # S_{m n s} = g^{rho a} DC[a, m, rho, n, s] traced: first raise a
    gi1 = jet_slice(ginv, 4, 1)
    E = jet_mm(gi1.reshape(4, 4, len(mons(1)), W),
               DC.reshape(4, 256, len(mons(1)), W), 1, 1, 1)
    E = E.reshape(4, 4, 4, 4, 4, len(mons(1)), W)  # E[b,m,rho,n,s]
    S = np.trace(E, axis1=0, axis2=2)  # S[m,n,s] shape (4,4,4,n1,W)
    # Covariant derivative of S, order 0
    S0 = jet_slice(S, 1, 0)
    dS = np.zeros((4, 4, 4, 4, len(mons(0)), W))
    dS[1] = jet_deriv(S, 1, 0)
    dS[2] = jet_deriv(S, 1, 1)
    Gam0 = jet_slice(Gam, 3, 0)
    B2m = np.transpose(Gam0, (1, 2, 0, 3, 4)).reshape(16, 4, len(mons(0)), W)
    DS = dS.copy()
    u1 = jet_mm(B2m, S0.reshape(4, 16, len(mons(0)), W), 0, 0, 0)
    DS -= u1.reshape(4, 4, 4, 4, len(mons(0)), W)  # slot m: (b,m),(n,s)
    u2 = jet_mm(B2m, np.transpose(S0, (1, 0, 2, 3, 4)).reshape(4, 16, len(mons(0)), W), 0, 0, 0)
    DS -= np.transpose(u2.reshape(4, 4, 4, 4, len(mons(0)), W), (0, 2, 1, 3, 4, 5))
    u3 = jet_mm(B2m, np.transpose(S0, (2, 0, 1, 3, 4)).reshape(4, 16, len(mons(0)), W), 0, 0, 0)
    DS -= np.transpose(u3.reshape(4, 4, 4, 4, len(mons(0)), W), (0, 2, 3, 1, 4, 5))
    # Bach1[m,n] = g^{s b} DS[b,m,n,s] traced over s
    gi0 = jet_slice(ginv, 4, 0)
    F = jet_mm(gi0.reshape(4, 4, len(mons(0)), W),
               DS.reshape(4, 64, len(mons(0)), W), 0, 0, 0)
    F = F.reshape(4, 4, 4, 4, len(mons(0)), W)  # F[s,m,n,s2]
    Bach1 = np.trace(F, axis1=0, axis2=3)  # (m,n,1,W)
    # R^{rho sigma} C_{m rho n sigma}, order 0
    Ric0 = jet_slice(Ric, 2, 0); C0 = jet_slice(Weyl, 2, 0)
    M1 = jet_mm(gi0.reshape(4, 4, 1, W), Ric0.reshape(4, 4, 1, W), 0, 0, 0)
    Rup = jet_mm(M1.reshape(4, 4, 1, W), gi0.reshape(4, 4, 1, W), 0, 0, 0)
    T1 = jet_mm(np.transpose(Rup, (1, 0, 2, 3)).reshape(4, 4, 1, W),
                np.transpose(C0, (1, 0, 2, 3, 4, 5)).reshape(4, 64, 1, W), 0, 0, 0)
    T1 = T1.reshape(4, 4, 4, 4, 1, W)  # T1[s,m,n,s2]
    Rterm = np.trace(T1, axis1=0, axis2=3)
    Bach_cov = 2.0 * Bach1 + Rterm  # (m,n,1,W)
    Bmix = jet_mm(gi0.reshape(4, 4, 1, W), Bach_cov.reshape(4, 4, 1, W), 0, 0, 0)
    if debug:
        DEBUG.update(Gam=Gam, Riem=Riem, Ric=Ric, Weyl=Weyl, DC=DC, S=S,
                     DS=DS, Bach1=Bach1, Rterm=Rterm, Rs=Rs)
    return Bmix[:, :, 0, :]  # (4,4,W)

def bach_at(r, th, **kw):
    g, ginv = build_metric(r, th, **kw)
    return bach_mixed(g, ginv)
