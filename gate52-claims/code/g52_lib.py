#!/usr/bin/env python3
"""
g52_lib.py -- Gate-52 machinery, written for this gate.

ORGANISATION (used by no earlier read): CARTAN STRUCTURE
EQUATIONS IN AN ORTHONORMAL TETRAD. The Einstein tensor is
never formed in a coordinate basis and no Christoffel symbol
is ever computed. At each evaluation point:

  (1) the Eulerian-adapted orthonormal tetrad of the ansatz
      metric (g_tt = -N(r)^2, g_tx = -beta*S(r),
      gamma_ij = delta_ij + (M(r)-1) n_i n_j) is built
      algebraically from the profile values -- time axis =
      the Eulerian normal, spatial triad = the radial unit
      vector plus a tangential pair;
  (2) the tetrad field's first and second spatial
      derivatives are propagated by a forward-mode
      second-order Taylor-jet engine through the tetrad's
      defining formulas (the profiles enter as radial jets
      through their (f, f', f'') triplets);
  (3) the frame's commutation coefficients, the Ricci
      rotation coefficients and the Riemann tensor follow
      from Cartan's first and second structure equations in
      component form;
  (4) the Ricci contraction in the frame gives That
      directly (the tetrad's time axis IS the Eulerian
      normal);
  (5) That is rotated into the registered SAMPLER-M frame
      convention (spatial triad from the eigendecomposition
      of gamma, the programme's registered frame
      definition) and the Hawking-Ellis margins follow
      their registered definitions: eigenvalue margins at
      Type-I points; the registered sampled fallback (162
      Fibonacci directions, velocities linspace(0, 0.95, 6))
      at non-Type-I points.

Conventions: [e_b, e_c] = c^a_bc e_a;
Gamma^a_bc := omega^a_b(e_c) (so nabla_{e_c} e_b =
Gamma^a_bc e_a); Gamma_{abc} = eta_{ad} Gamma^d_bc =
(1/2)(c_{cab} - c_{abc} - c_{bca}) (Koszul; satisfies
Gamma_{abc} = -Gamma_{bac} and Gamma_{abc} - Gamma_{acb} =
-c_{abc} identically -- both are asserted in the
calibration). Riemann from the second structure equation:
R^a_bcd = e_c(Gamma^a_bd) - e_d(Gamma^a_bc)
        + Gamma^a_ec Gamma^e_bd - Gamma^a_ed Gamma^e_bc
        - c^e_cd Gamma^a_be;  Ricci R_bd = R^a_bad.

The pointwise worst null is a certified lattice
minimisation -- Fibonacci scan + pattern-search refinement
+ an a-posteriori KKT / positive-semidefinite certificate
of global optimality (the trust-region sufficiency
conditions) -- not the lineage's Nelder-Mead polish and
not Gate-50's secular-equation solve.

Profiles are assembled from the programme's registered
design definitions and the stored vectors extracted to
gate52/results/g52_stored_inputs.json (md5s recorded
there): closed-form base profiles (the incomplete-beta
plateau as the polynomial I_u(3,3); smootherstep plateau;
quintic ramps) and not-a-knot correction splines in moment
form, the moment systems solved by this file's own solver.
No phase or earlier-gate code is imported; scipy is never
imported on this path. VM is the frame of record.
"""
import json
import os

import numpy as np

DT = np.float64
BETA = 1.1
R_LO, R_HI = 10.0, 20.0
LAM_S = 0.70
WINNER_A = 0.07439108177516472
MU_H2 = 1.15
EIGHT_PI = 8.0 * np.pi
ETA = np.array([-1.0, 1.0, 1.0, 1.0], dtype=DT)   # eta_aa

WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
INP = json.load(open(f'{WP}/gate52/results/g52_stored_inputs.json'))

A2 = {k: np.array(INP['A2'][k], dtype=DT) for k in ('vS', 'vN', 'vM')}
H2V = {k: np.array(INP['H2'][k], dtype=DT) for k in ('vS', 'vN', 'vM')}
WIN = INP['winner400']
WIN_MUN = float(WIN['muN'])
WIN_MUM = float(WIN['muM'])
WIN_VN = np.array(WIN['vN'], dtype=DT)
WIN_VM = np.array(WIN['vM'], dtype=DT)
SHAPEC_CRIT = np.array(INP['conf405']['shapeC_knots_at_criterion'],
                       dtype=DT)
M2_VS = np.array(INP['rungs412']['m2']['winner']['vS_scaled'],
                 dtype=DT)
M5K17_VS = np.array(INP['rungs412']['m5']['winner']['vS_scaled'],
                    dtype=DT)
M5K9_VS = np.array(INP['screens412']['523']['vS_scaled'], dtype=DT)

H2_PEAK_STORED = 0.8853484980534808
SS7_BAR = 0.4426742490267404
FINE_R = np.linspace(R_LO, R_HI, 401)


def knots(K):
    return np.linspace(R_LO, R_HI, K)


# ============================================================ splines
# Not-a-knot cubic spline in moment form; the moment system
# (second derivatives at the knots) is assembled and solved
# here.
def nak_moments(xk, yk):
    xk = np.asarray(xk, dtype=DT)
    yk = np.asarray(yk, dtype=DT)
    n = len(xk)
    h = np.diff(xk)
    A = np.zeros((n, n), dtype=DT)
    b = np.zeros(n, dtype=DT)
    A[0, 0] = -h[1]
    A[0, 1] = h[0] + h[1]
    A[0, 2] = -h[0]
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2.0 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 6.0 * ((yk[i + 1] - yk[i]) / h[i]
                      - (yk[i] - yk[i - 1]) / h[i - 1])
    A[n - 1, n - 3] = -h[n - 2]
    A[n - 1, n - 2] = h[n - 3] + h[n - 2]
    A[n - 1, n - 1] = -h[n - 3]
    return np.linalg.solve(A, b)


def nak_eval(xk, yk, M, r):
    """(d, dp, dpp) at radii r; constant extension (end
    value, zero derivatives) outside [xk[0], xk[-1]] -- the
    lineage's registered correction-spline convention."""
    xk = np.asarray(xk, dtype=DT)
    yk = np.asarray(yk, dtype=DT)
    r = np.asarray(r, dtype=DT)
    rc = np.clip(r, xk[0], xk[-1])
    i = np.searchsorted(xk, rc, side='right') - 1
    i = np.clip(i, 0, len(xk) - 2)
    h = xk[i + 1] - xk[i]
    A_ = (xk[i + 1] - rc) / h
    B_ = (rc - xk[i]) / h
    d = (A_ * yk[i] + B_ * yk[i + 1]
         + ((A_ ** 3 - A_) * M[i] + (B_ ** 3 - B_) * M[i + 1])
         * h ** 2 / 6.0)
    dp = ((yk[i + 1] - yk[i]) / h
          + h / 6.0 * ((1.0 - 3.0 * A_ ** 2) * M[i]
                       + (3.0 * B_ ** 2 - 1.0) * M[i + 1]))
    dpp = A_ * M[i] + B_ * M[i + 1]
    out = (r < xk[0]) | (r > xk[-1])
    if np.any(out):
        dp = np.where(out, 0.0, dp)
        dpp = np.where(out, 0.0, dpp)
    return d, dp, dpp


class Corr:
    def __init__(self, vals, K):
        self.xk = knots(K)
        self.yk = np.asarray(vals, dtype=DT)
        self.M = nak_moments(self.xk, self.yk)

    def __call__(self, r):
        return nak_eval(self.xk, self.yk, self.M, r)


_CORR_CACHE = {}


def corr(vals, K):
    key = (K, tuple(np.asarray(vals, dtype=DT)))
    if key not in _CORR_CACHE:
        _CORR_CACHE[key] = Corr(vals, K)
    return _CORR_CACHE[key]


# ============================================================ base profiles
def s_ab(r):
    """1 below 10, 0 above 20, 1 - I_u(3,3) between,
    u = (r-10)/10 (polynomial form)."""
    r = np.asarray(r, dtype=DT)
    S = np.where(r >= R_HI, 0.0, 1.0)
    Sp = np.zeros_like(r)
    Spp = np.zeros_like(r)
    m = (r > R_LO) & (r < R_HI)
    if np.any(m):
        u = (r[m] - R_LO) / 10.0
        w = 1.0 - u
        S[m] = 1.0 - (10.0 * u ** 3 * w ** 2 + 5.0 * u ** 4 * w
                      + u ** 5)
        Sp[m] = -3.0 * u ** 2 * w ** 2
        Spp[m] = -0.6 * u * w * (1.0 - 2.0 * u)
    return S, Sp, Spp


def _H(t):
    """Smootherstep: 0 below 0, 1 above 1,
    10t^3 - 15t^4 + 6t^5 between."""
    t = np.asarray(t, dtype=DT)
    v = np.where(t >= 1.0, 1.0, 0.0)
    vp = np.zeros_like(t)
    vpp = np.zeros_like(t)
    m = (t > 0.0) & (t < 1.0)
    if np.any(m):
        tm = t[m]
        v[m] = 10.0 * tm ** 3 - 15.0 * tm ** 4 + 6.0 * tm ** 5
        vp[m] = 30.0 * tm ** 2 * (1.0 - tm) ** 2
        vpp[m] = 60.0 * tm * (1.0 - tm) * (1.0 - 2.0 * tm)
    return v, vp, vpp


def _plateau(r, c=15.0, W=5.0, e=3.0):
    Ha, Hpa, Hppa = _H((r - (c - W)) / e)
    Hb, Hpb, Hppb = _H(((c + W) - r) / e)
    B = Ha * Hb
    Bp = (Hpa * Hb - Ha * Hpb) / e
    Bpp = (Hppa * Hb - 2.0 * Hpa * Hpb + Ha * Hppb) / e ** 2
    return B, Bp, Bpp


def _ramp(r, a, b):
    """Quintic smoothstep ramp U(r; a, b)."""
    r = np.asarray(r, dtype=DT)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r)
    Upp = np.zeros_like(r)
    m = (r > a) & (r < b)
    if np.any(m):
        x = (r[m] - a) / (b - a)
        U[m] = 6.0 * x ** 5 - 15.0 * x ** 4 + 10.0 * x ** 3
        Up[m] = (30.0 * x ** 4 - 60.0 * x ** 3
                 + 30.0 * x ** 2) / (b - a)
        Upp[m] = (120.0 * x ** 3 - 180.0 * x ** 2
                  + 60.0 * x) / (b - a) ** 2
    return U, Up, Upp


def base_profiles(r):
    r = np.asarray(r, dtype=DT)
    S, Sp, Spp = s_ab(r)
    S, Sp, Spp = LAM_S * S, LAM_S * Sp, LAM_S * Spp
    B, Bp, Bpp = _plateau(r)
    N, Np, Npp = (1.0 + WINNER_A * B, WINNER_A * Bp,
                  WINNER_A * Bpp)
    U1, U1p, U1pp = _ramp(r, 8.5, 20.0)
    U2, U2p, U2pp = _ramp(r, 21.0, 24.0)
    M = 1.0 + 6.0 * (U1 - U2)
    Mp = 6.0 * (U1p - U2p)
    Mpp = 6.0 * (U1pp - U2pp)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


def _add_corr_arr(prof, vecs, K, r):
    out = []
    for i, key in enumerate(('vS', 'vN', 'vM')):
        d, dp, dpp = corr(vecs[key], K)(r)
        out += [prof[3 * i] + d, prof[3 * i + 1] + dp,
                prof[3 * i + 2] + dpp]
    return tuple(out)


def a2_totals(r):
    return _add_corr_arr(base_profiles(r), A2, 33, r)


def _centre(mu, prof):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof
    return (mu * S, mu * Sp, mu * Spp,
            mu * N, mu * Np, mu * Npp,
            1.0 + mu * (M - 1.0), mu * Mp, mu * Mpp)


def h2_totals(r):
    return _add_corr_arr(_centre(MU_H2, a2_totals(r)), H2V, 17, r)


def winner_base_profiles(r):
    """Phase 400's winner base: H2 totals' N/M rescaled by
    (WIN_MUN, WIN_MUM) + the winner's K=17 corrections;
    S identically zero."""
    _S, _Sp, _Spp, N, Np, Npp, M, Mp, Mpp = h2_totals(r)
    r = np.asarray(r, dtype=DT)
    z = np.zeros_like(r)
    N, Np, Npp = WIN_MUN * N, WIN_MUN * Np, WIN_MUN * Npp
    M, Mp, Mpp = (1.0 + WIN_MUM * (M - 1.0), WIN_MUM * Mp,
                  WIN_MUM * Mpp)
    d, dp, dpp = corr(WIN_VN, 17)(r)
    N, Np, Npp = N + d, Np + dp, Npp + dpp
    d, dp, dpp = corr(WIN_VM, 17)(r)
    M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    return z.copy(), z.copy(), z.copy(), N, Np, Npp, M, Mp, Mpp


def config_profiles(r, vS, K):
    """Winner base + the free S spline through vS (K knots);
    vS None gives the static base."""
    prof = winner_base_profiles(r)
    if vS is None:
        return prof
    d, dp, dpp = corr(np.asarray(vS, dtype=DT), K)(
        np.asarray(r, dtype=DT))
    return (d, dp, dpp) + prof[3:]


# ============================================================ jets
# A Jet carries (value, gradient, Hessian) of a scalar
# function of (x, y, z), vectorised over points:
#   v: (P,), g: (P, 3), H: (P, 3, 3).
class Jet:
    __slots__ = ('v', 'g', 'H')

    def __init__(self, v, g, H):
        self.v = v
        self.g = g
        self.H = H

    @staticmethod
    def const(c, P):
        return Jet(np.full(P, float(c), dtype=DT),
                   np.zeros((P, 3), dtype=DT),
                   np.zeros((P, 3, 3), dtype=DT))

    def __add__(self, o):
        return Jet(self.v + o.v, self.g + o.g, self.H + o.H)

    def __sub__(self, o):
        return Jet(self.v - o.v, self.g - o.g, self.H - o.H)

    def __neg__(self):
        return Jet(-self.v, -self.g, -self.H)

    def scale(self, c):
        return Jet(c * self.v, c * self.g, c * self.H)

    def __mul__(self, o):
        v = self.v * o.v
        g = self.g * o.v[:, None] + o.g * self.v[:, None]
        H = (self.H * o.v[:, None, None]
             + o.H * self.v[:, None, None]
             + self.g[:, :, None] * o.g[:, None, :]
             + self.g[:, None, :] * o.g[:, :, None])
        return Jet(v, g, H)

    def inv(self):
        v = 1.0 / self.v
        g = -self.g * (v ** 2)[:, None]
        H = (-self.H * (v ** 2)[:, None, None]
             + 2.0 * (self.g[:, :, None] * self.g[:, None, :])
             * (v ** 3)[:, None, None])
        return Jet(v, g, H)

    def __truediv__(self, o):
        return self * o.inv()

    def sqrt(self):
        v = np.sqrt(self.v)
        g = self.g / (2.0 * v)[:, None]
        H = (self.H / (2.0 * v)[:, None, None]
             - (self.g[:, :, None] * self.g[:, None, :])
             / (4.0 * v ** 3)[:, None, None])
        return Jet(v, g, H)


def _outer(a, b):
    return a[:, :, None] * b[:, None, :]


# ============================================================ Cartan core
def _tetrad_jets(pts, prof):
    """Tetrad and coframe component jets at pts, from the
    profile triplets prof at r = |pts|. E[a][mu], W[a][mu]
    are Jets over (x, y, z); mu = 0 is the time component
    (all fields are t-independent)."""
    pts = np.asarray(pts, dtype=DT)
    P = len(pts)
    r0 = np.linalg.norm(pts, axis=1)
    n = pts / r0[:, None]
    I3 = np.eye(3, dtype=DT)
    Hr = (I3[None] - _outer(n, n)) / r0[:, None, None]
    rj = Jet(r0, n.copy(), Hr)

    def prof_jet(f0, f1, f2):
        g = f1[:, None] * n
        H = (f2[:, None, None] * _outer(n, n)
             + (f1 / r0)[:, None, None]
             * (I3[None] - _outer(n, n)))
        return Jet(np.array(f0, dtype=DT), g, H)

    Sj = prof_jet(*prof[0:3])
    Nj = prof_jet(*prof[3:6])
    Mj = prof_jet(*prof[6:9])
    vj = Sj.scale(BETA)                       # beta * S
    xj = []
    for i in range(3):
        g = np.zeros((P, 3), dtype=DT)
        g[:, i] = 1.0
        xj.append(Jet(pts[:, i].copy(), g,
                      np.zeros((P, 3, 3), dtype=DT)))
    nj = [xj[i] / rj for i in range(3)]
    one = Jet.const(1.0, P)
    hj = Mj - one
    qj = one - one / Mj                       # (M-1)/M
    nnj = [[nj[i] * nj[j] for j in range(3)] for i in range(3)]
    gamj = [[(Jet.const(1.0 if i == j else 0.0, P)
              + hj * nnj[i][j]) for j in range(3)]
            for i in range(3)]
    gij = [[(Jet.const(1.0 if i == j else 0.0, P)
             - qj * nnj[i][j]) for j in range(3)]
           for i in range(3)]
    negv = -vj
    bup = [gij[i][0] * negv for i in range(3)]      # beta^i
    alpha2 = Nj * Nj + (vj * vj) * gij[0][0]
    alphaj = alpha2.sqrt()
    E = [[None] * 4 for _ in range(4)]
    inva = alphaj.inv()
    E[0][0] = inva
    for i in range(3):
        E[0][1 + i] = bup[i].scale(-1.0) * inva     # -beta^i/alpha
    sqM = Mj.sqrt()
    t1 = [nj[i] / sqM for i in range(3)]
    aref = np.zeros((P, 3), dtype=DT)
    use_z = np.abs(n[:, 2]) < 0.9
    aref[use_z, 2] = 1.0
    aref[~use_z, 0] = 1.0
    adotn = Jet.const(0.0, P)
    for k in range(3):
        coef = aref[:, k]
        adotn = adotn + Jet(nj[k].v * coef,
                            nj[k].g * coef[:, None],
                            nj[k].H * coef[:, None, None])
    wj = []
    for i in range(3):
        ai = Jet(np.array(aref[:, i], dtype=DT),
                 np.zeros((P, 3), dtype=DT),
                 np.zeros((P, 3, 3), dtype=DT))
        wj.append(ai - adotn * nj[i])
    wn = (wj[0] * wj[0] + wj[1] * wj[1] + wj[2] * wj[2]).sqrt()
    t2 = [wj[i] / wn for i in range(3)]
    t3 = [nj[1] * t2[2] - nj[2] * t2[1],
          nj[2] * t2[0] - nj[0] * t2[2],
          nj[0] * t2[1] - nj[1] * t2[0]]
    triads = [t1, t2, t3]
    zero = Jet.const(0.0, P)
    for a in range(3):
        E[1 + a][0] = zero
        for i in range(3):
            E[1 + a][1 + i] = triads[a][i]
    W = [[None] * 4 for _ in range(4)]
    W[0][0] = alphaj          # dual basis: theta^0 = alpha dt
    for i in range(3):
        W[0][1 + i] = zero
    for a in range(3):
        ecov = []
        for i in range(3):
            s = None
            for j in range(3):
                piece = gamj[i][j] * triads[a][j]
                s = piece if s is None else s + piece
            ecov.append(s)
        tcomp = None
        for i in range(3):
            piece = ecov[i] * bup[i]
            tcomp = piece if tcomp is None else tcomp + piece
        W[1 + a][0] = tcomp
        for i in range(3):
            W[1 + a][1 + i] = ecov[i]
    return E, W


def that_cartan(pts, prof):
    """Einstein/8pi in the Eulerian frame at pts.
    Returns (That_nat, That_reg): That in the gate's natural
    tetrad, and rotated into the registered SAMPLER-M frame
    convention (eigh triad of gamma)."""
    pts = np.asarray(pts, dtype=DT)
    P = len(pts)
    E, W = _tetrad_jets(pts, prof)
    Ev = [[E[a][mu].v for mu in range(4)] for a in range(4)]
    Eg = [[E[a][mu].g for mu in range(4)] for a in range(4)]
    Eh = [[E[a][mu].H for mu in range(4)] for a in range(4)]
    Wv = [[W[a][mu].v for mu in range(4)] for a in range(4)]
    Wg = [[W[a][mu].g for mu in range(4)] for a in range(4)]
    # commutation coefficients c^d_ab and their spatial
    # gradients cg[d][a][b] : (P, 3)
    C = np.zeros((P, 4, 4, 4), dtype=DT)
    CG = np.zeros((P, 4, 4, 4, 3), dtype=DT)
    for d in range(4):
        for a in range(4):
            for b in range(4):
                br = np.zeros(P, dtype=DT)
                brg = np.zeros((P, 3), dtype=DT)
                for mu in range(4):
                    t = np.zeros(P, dtype=DT)
                    dt = np.zeros((P, 3), dtype=DT)
                    for nu in range(3):
                        t += Ev[a][1 + nu] * Eg[b][mu][:, nu] \
                            - Ev[b][1 + nu] * Eg[a][mu][:, nu]
                        dt += Eg[a][1 + nu] * Eg[b][mu][:, nu][:, None] \
                            + Ev[a][1 + nu][:, None] \
                            * Eh[b][mu][:, :, nu] \
                            - Eg[b][1 + nu] * Eg[a][mu][:, nu][:, None] \
                            - Ev[b][1 + nu][:, None] \
                            * Eh[a][mu][:, :, nu]
                    br += Wv[d][mu] * t
                    brg += Wg[d][mu] * t[:, None] \
                        + Wv[d][mu][:, None] * dt
                C[:, d, a, b] = br
                CG[:, d, a, b] = brg
    # lowered c and Koszul Gamma (axes p, a, b, c[, lam])
    CL = C * ETA[None, :, None, None]
    CLg = CG * ETA[None, :, None, None, None]
    Gam = 0.5 * (CL.transpose(0, 2, 3, 1) - CL
                 - CL.transpose(0, 3, 1, 2))
    Gamg = 0.5 * (CLg.transpose(0, 2, 3, 1, 4) - CLg
                  - CLg.transpose(0, 3, 1, 2, 4))
    Gup = Gam * ETA[None, :, None, None]
    Gupg = Gamg * ETA[None, :, None, None, None]
    # DG[p, a, b, c, d] = e_d(Gamma^a_bc)
    Es = np.zeros((4, 3, P), dtype=DT)
    for d in range(4):
        for nu in range(3):
            Es[d, nu] = Ev[d][1 + nu]
    DG = np.einsum('dnp,pabcn->pabcd', Es, Gupg)
    # Riemann R^a_bcd
    R = DG.transpose(0, 1, 2, 4, 3) - DG
    R = R + np.einsum('paec,pebd->pabcd', Gup, Gup) \
        - np.einsum('paed,pebc->pabcd', Gup, Gup) \
        - np.einsum('pecd,pabe->pabcd', C, Gup)
    Ric = np.einsum('pabad->pbd', R)
    Rsc = np.sum(ETA[None, :] * np.diagonal(Ric, axis1=1,
                                            axis2=2), axis=1)
    Gfr = Ric - 0.5 * Rsc[:, None, None] \
        * (ETA[None, :, None] * np.eye(4)[None])
    That_nat = Gfr / EIGHT_PI
    # rotation into the registered (eigh-triad) frame
    r0 = np.linalg.norm(pts, axis=1)
    n = pts / r0[:, None]
    h = prof[6] - 1.0
    gam = np.eye(3)[None] + h[:, None, None] * _outer(n, n)
    lam, V = np.linalg.eigh(gam)
    # W3v[p, i, j] = component j of the i-th eigh frame
    # vector V[:, i] / sqrt(lam_i)
    W3v = np.transpose(V / np.sqrt(lam)[:, None, :], (0, 2, 1))
    T3 = np.zeros((P, 3, 3), dtype=DT)           # triad vectors
    for a in range(3):
        for i in range(3):
            T3[:, a, i] = Ev[1 + a][1 + i]
    A = np.einsum('pij,pjk,pak->pia', W3v, gam, T3)
    That_reg = np.zeros((P, 4, 4), dtype=DT)
    That_reg[:, 0, 0] = That_nat[:, 0, 0]
    cross = np.einsum('pia,pa->pi', A, That_nat[:, 0, 1:])
    That_reg[:, 0, 1:] = cross
    That_reg[:, 1:, 0] = cross
    That_reg[:, 1:, 1:] = np.einsum('pia,pjb,pab->pij',
                                    A, A, That_nat[:, 1:, 1:])
    return That_nat, That_reg


def that_at(vS, K, pts):
    """That_reg for the configuration (winner base + S
    spline vS/K; vS None = static base) at Cartesian pts."""
    pts = np.asarray(pts, dtype=DT)
    r = np.linalg.norm(pts, axis=1)
    prof = config_profiles(r, vS, K)
    return that_cartan(pts, prof)[1]


# ============================================================ margins
def fib_dirs(npts):
    i = np.arange(npts, dtype=DT)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


def sampled_margins(That, n_dir=162, n_vel=6):
    """The registered sampled fallback: min NEC/WEC/SEC
    contractions over Fibonacci observer directions and
    velocities linspace(0, 0.95, n_vel); DEC via the
    normalised future-causality margin of
    Upsilon^a = -T^a_b V^b."""
    dirs = fib_dirs(n_dir)
    That = np.asarray(That, dtype=DT)
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    nec_min = np.empty(Np)
    wec_min = np.empty(Np)
    sec_min = np.empty(Np)
    dec_min = np.empty(Np)
    vels = np.linspace(0.0, 0.95, n_vel)
    CH = 8192
    for s0 in range(0, Np, CH):
        F = flat[s0:s0 + CH]
        T00 = F[:, 0, 0]
        T0i = F[:, 0, 1:]
        Tij = F[:, 1:, 1:]
        tr = np.trace(Tij, axis1=1, axis2=2)
        quad = np.einsum('njk,ij,ik->ni', Tij, dirs, dirs)
        nec_min[s0:s0 + CH] = (T00[:, None]
                               + 2.0 * (T0i @ dirs.T)
                               + quad).min(axis=1)
        wm = np.full(F.shape[0], np.inf)
        sm = np.full(F.shape[0], np.inf)
        dm = np.full(F.shape[0], np.inf)
        Mm = F.copy()
        Mm[:, 0, :] *= -1.0
        for v in vels:
            gam = 1.0 / np.sqrt(1.0 - v * v)
            wec_vals = gam ** 2 * (T00[:, None]
                                   + 2.0 * v * (T0i @ dirs.T)
                                   + v * v * quad)
            wm = np.minimum(wm, wec_vals.min(axis=1))
            trT = -T00 + tr
            sec_vals = wec_vals - 0.5 * trT[:, None] \
                * gam ** 2 * (v * v - 1.0)
            sm = np.minimum(sm, sec_vals.min(axis=1))
            V = np.zeros((F.shape[0], n_dir, 4), dtype=DT)
            V[:, :, 0] = gam
            V[:, :, 1:] = gam * v * dirs[None, :, :]
            Ups = -np.einsum('nab,nib->nia', Mm, V)
            q = Ups[:, :, 0] ** 2 - np.sum(Ups[:, :, 1:] ** 2,
                                           axis=2)
            nrm = 1.0 + np.sum(Ups ** 2, axis=2)
            val = np.where(Ups[:, :, 0] > 0, q / nrm,
                           -np.abs(q) / nrm - 1.0)
            dm = np.minimum(dm, val.min(axis=1))
        wec_min[s0:s0 + CH] = wm
        sec_min[s0:s0 + CH] = sm
        dec_min[s0:s0 + CH] = dm
    return {'nec_s': nec_min, 'wec_s': wec_min,
            'sec_s': sec_min, 'dec_s': dec_min}


def hawking_ellis_margins(That):
    """Eigenvalue margins at Type-I points (registered
    definitions and tolerances); sampled fallback fills
    non-Type-I points. Returns flat (P,) arrays."""
    That = np.asarray(That, dtype=DT)
    flat = That.reshape(-1, 4, 4)
    Np = flat.shape[0]
    M = flat.copy()
    M[:, 0, :] *= -1.0                       # M^a_b
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1),
                       1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] \
        + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k_idx = np.argmax(cand, axis=1)
    ar = np.arange(Np)
    rho = np.where(typeI, -evals[ar, k_idx].real, np.nan)
    mask = np.ones((Np, 4), dtype=bool)
    mask[ar, k_idx] = False
    ps_all = evals.real[mask].reshape(Np, 3)
    ps = np.where(typeI[:, None], ps_all, np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1),
                       np.nan)
        wec = np.where(typeI, np.minimum(
            rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(
            np.min(rho[:, None] + ps, axis=1),
            rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(
            rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    filled = np.zeros(Np, dtype=bool)
    if np.any(~typeI):
        sub = sampled_margins(flat[~typeI])
        idx = np.where(~typeI)[0]
        nec[idx] = sub['nec_s']
        wec[idx] = sub['wec_s']
        sec[idx] = sub['sec_s']
        dec[idx] = sub['dec_s']
        filled[idx] = True
    return {'typeI': typeI, 'sampled_filled': filled,
            'nec': nec, 'wec': wec, 'sec': sec, 'dec': dec,
            'rho_eig': rho, 'p': ps,
            'rho_euler': flat[:, 0, 0]}


# ============================================================ worst null
def worst_null_certified(That, n_scan=20002):
    """Certified min over unit u of q(u) = T00 + 2 F.u +
    u^T P u (the Eulerian-frame worst null contraction at
    one point). Method: Fibonacci scan + pattern-search
    refinement on (theta, phi); certificate: at the
    refined u*, lambda* = -(u*^T P u* + F.u*) makes
    (P + lambda* I) u* = -F hold to a reported residual
    and P + lambda* I positive semidefinite to a reported
    margin -- the trust-region global-optimality
    conditions. Returns dict with the value, the scan
    value, and the certificate fields."""
    That = np.asarray(That, dtype=DT)
    T00 = float(That[0, 0])
    F = np.array(That[0, 1:], dtype=DT)
    Pm = np.array(That[1:, 1:], dtype=DT)
    Pm = 0.5 * (Pm + Pm.T)

    def q_of(u):
        return T00 + 2.0 * float(F @ u) + float(u @ Pm @ u)

    dirs = fib_dirs(n_scan)
    vals = T00 + 2.0 * (dirs @ F) \
        + np.einsum('ni,ij,nj->n', dirs, Pm, dirs)
    i0 = int(np.argmin(vals))
    scan_min = float(vals[i0])
    u0 = dirs[i0].copy()
    # work in a permuted spatial frame whose chart pole is
    # the axis least aligned with the scan minimiser (the
    # (theta, phi) chart is regular there)
    k = int(np.argmin(np.abs(u0)))
    perm = [k, (k + 1) % 3, (k + 2) % 3]
    Fp = F[perm]
    Pp = Pm[np.ix_(perm, perm)]
    u = u0[perm].copy()

    def q_of_p(uu):
        return T00 + 2.0 * float(Fp @ uu) + float(uu @ Pp @ uu)

    th = float(np.arccos(np.clip(u[2], -1.0, 1.0)))
    ph = float(np.arctan2(u[1], u[0]))
    best = q_of_p(u)

    def q_ang(th, ph):
        uu = np.array([np.sin(th) * np.cos(ph),
                       np.sin(th) * np.sin(ph), np.cos(th)])
        return q_of_p(uu), uu

    step = 0.05
    while step > 1e-7:
        improved = False
        for dth, dph in ((step, 0.0), (-step, 0.0),
                         (0.0, step), (0.0, -step),
                         (step, step), (step, -step),
                         (-step, step), (-step, -step)):
            v, uu = q_ang(th + dth, ph + dph)
            if v < best - 1e-15:
                best = v
                th, ph = th + dth, ph + dph
                u = uu
                improved = True
        if not improved:
            step *= 0.4
    # chart-Newton polish (analytic gradient/Hessian of q
    # on the (theta, phi) chart) to machine precision
    for _ in range(60):
        st_, ct_ = np.sin(th), np.cos(th)
        sp_, cp_ = np.sin(ph), np.cos(ph)
        uu = np.array([st_ * cp_, st_ * sp_, ct_])
        u_t = np.array([ct_ * cp_, ct_ * sp_, -st_])
        u_p = np.array([-st_ * sp_, st_ * cp_, 0.0])
        u_tt = -uu
        u_pp = np.array([-st_ * cp_, -st_ * sp_, 0.0])
        u_tp = np.array([-ct_ * sp_, ct_ * cp_, 0.0])
        gv = 2.0 * Fp + 2.0 * Pp @ uu
        grad = np.array([gv @ u_t, gv @ u_p])
        H = np.array([
            [2.0 * u_t @ Pp @ u_t + gv @ u_tt,
             2.0 * u_t @ Pp @ u_p + gv @ u_tp],
            [2.0 * u_p @ Pp @ u_t + gv @ u_tp,
             2.0 * u_p @ Pp @ u_p + gv @ u_pp]])
        try:
            delta = np.linalg.solve(H, -grad)
        except np.linalg.LinAlgError:
            break
        th += float(delta[0])
        ph += float(delta[1])
        if np.max(np.abs(delta)) < 1e-14:
            break
    u = np.array([np.sin(th) * np.cos(ph),
                  np.sin(th) * np.sin(ph), np.cos(th)])
    best = q_of_p(u)
    # certificate in the ORIGINAL frame
    u_orig = np.empty(3)
    u_orig[perm] = u
    lam = -(float(u_orig @ Pm @ u_orig) + float(F @ u_orig))
    A = Pm + lam * np.eye(3)
    res = A @ u_orig + F
    ev = np.linalg.eigvalsh(A)
    return {'worst_null': float(best), 'scan_min': scan_min,
            'u': u_orig.tolist(), 'lambda': float(lam),
            'kkt_residual': float(np.max(np.abs(res))),
            'psd_min_eig': float(ev[0]),
            'certified': bool(np.max(np.abs(res)) < 1e-9
                              and ev[0] > -1e-9)}


# ============================================================ SET read
R_NODES = 10.0 + (np.arange(41, dtype=DT) + 0.5) * (10.0 / 41.0)
DIRS162 = fib_dirs(162)


def set_read(vS, K, beta=BETA):
    """SET-244 read of the configuration (winner base + S
    spline vS/K) on gate machinery."""
    rec = {k: [] for k in ('typeI', 'nec', 'wec', 'dec', 'sec',
                           'rho')}
    typeI_nec = []
    for rr in R_NODES:
        pts = DIRS162 * rr
        That = that_at(vS, K, pts)
        m = hawking_ellis_margins(That)
        for k in rec:
            rec[k].append(m[k] if k != 'rho' else m['rho_euler'])
        if np.any(m['typeI']):
            typeI_nec.append(m['nec'][m['typeI']])
    R = {k: np.concatenate(v) for k, v in rec.items()}

    def st(arr):
        return {'min': float(np.min(arr)),
                'median': float(np.median(arr)),
                'max': float(np.max(arr))}
    i_nec = int(np.argmin(R['nec']))
    i_dec = int(np.argmin(R['dec']))
    i_r, i_d = divmod(i_nec, 162)
    j_r, j_d = divmod(i_dec, 162)
    out = {
        'set': 'SET-244 (41 radial midpoint nodes x 162 '
               'Fibonacci dirs)',
        'sampler': 'SAMPLER-M',
        'n_points': int(len(R['typeI'])),
        'typeI_fraction': float(np.mean(R['typeI'])),
        'typeI_count': int(np.sum(R['typeI'])),
        'nec': st(R['nec']), 'wec': st(R['wec']),
        'dec': st(R['dec']), 'sec': st(R['sec']),
        'rho': st(R['rho']),
        'nec_argmin_point': (DIRS162[i_d]
                             * R_NODES[i_r]).tolist(),
        'nec_argmin_r': float(R_NODES[i_r]),
        'nec_argmin_dir_index': int(i_d),
        'nec_argmin_typeI': bool(R['typeI'][i_nec]),
        'dec_argmin_point': (DIRS162[j_d]
                             * R_NODES[j_r]).tolist(),
        'dec_argmin_r': float(R_NODES[j_r]),
        'dec_argmin_dir_index': int(j_d),
        'dec_argmin_typeI': bool(R['typeI'][i_dec]),
        'typeI_nec_min': (float(np.min(np.concatenate(
            typeI_nec))) if typeI_nec else None),
        'joint': float(min(R['nec'].min(), R['dec'].min())),
    }
    return out, R


def nec_at_point(vS, K, pt):
    """(nec, typeI, That_reg) at one Cartesian point."""
    pt = np.asarray(pt, dtype=DT)
    That = that_at(vS, K, pt[None, :])
    m = hawking_ellis_margins(That)
    return float(m['nec'][0]), bool(m['typeI'][0]), That[0]


def phys_row(vS, K, argmin_r=None):
    """FINE_R x-axis peak read + profile locals at a
    radius (the registered phys-row form)."""
    pts = np.stack([FINE_R, np.zeros_like(FINE_R),
                    np.zeros_like(FINE_R)], axis=1)
    prof = config_profiles(FINE_R, vS, K)
    S = prof[0]
    peak = float(np.max(np.abs(BETA * S)))
    i_pk = int(np.argmax(np.abs(BETA * S)))
    # dense scan for the argmax location
    rd = np.linspace(R_LO, R_HI, 20001)
    Sd = config_profiles(rd, vS, K)[0]
    pkd = np.abs(BETA * Sd)
    i_d = int(np.argmax(pkd))
    out = {'peak_fine': peak, 'peak_radius_fine':
           float(FINE_R[i_pk]),
           'peak_dense': float(pkd[i_d]),
           'peak_radius_dense': float(rd[i_d]),
           'S_range': [float(np.min(S)), float(np.max(S))]}
    if argmin_r is not None:
        pr = config_profiles(np.array([float(argmin_r)]),
                             vS, K)
        names = ('S', 'Sp', 'Spp', 'N', 'Np', 'Npp',
                 'M', 'Mp', 'Mpp')
        out['local_at_argmin'] = {
            nm: float(pr[i][0]) for i, nm in enumerate(names)}
    return out
