#!/usr/bin/env python3
"""Gate-37 independent engine (written from scratch for this gate; no
Phase 259/318/323 code is imported or reused).

Formalism: local coordinates (t, x, u, ph) = (0, 1, 2, 3) about a
point of a static spherical background
    ds^2 = -e^{2Phi(l)} dt^2 + dl^2 + R(l)^2 dOmega^2,
x = l - l0, u = theta - pi/2.  Every background quantity is independent
of t and ph, so jets are power series in (x, u) only:
    jet = dict {(i, j): coeff}  meaning  sum coeff * x^i u^j,
coefficients exact Fractions (or floats for the float calibration).

The variation E[scalar] is the programme-convention Euler-Lagrange
derivative:  delta S = int sqrt(-g) E_ab delta g^{ab},  S = int
sqrt(-g) L.  It is extracted by exact dual-jet linearisation:
perturb one Taylor coefficient c_{ab,M} of the inverse metric jet,
read delta L(x) as a jet, solve the triangular system
    dL/dc_{ab,M} = sum_{I<=M} (M!/(M-I)!) x^{M-I} A_{ab,I},
    A_{ab,I} := dL/d(d_I g^{ab}),
and assemble
    E_ab = sum_I (-1)^|I| d_I( sigma A_{ab,I} ) / 1  - (1/2) L g_ab
at the point (sigma = sqrt(-det g / -det g(0)), the rho-ratio jet;
the -1/2 L g_ab term is (1/rho) L drho/dg^{ab}, rho = sqrt(-det g)).
E_ab(x) to first order is also produced (sigma^{-1} form) so the
conservation read nabla^a E_ab at the point is exact.

Conventions (locked against the stored Ricci reads):
    Gamma^a_bc = (1/2) g^{ad} (d_b g_dc + d_c g_db - d_d g_bc)
    R^a_{bcd}   = d_c Gamma^a_{bd} - d_d Gamma^a_{bc}
                  + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc}
    R_{ab}      = R^c_{a c b}
    nabla_e R_{ab} = d_e R_{ab} - Gamma^f_{ea} R_{fb} - Gamma^f_{eb} R_{af}
Derivatives d_t and d_ph of any jet vanish identically in this frame.
"""
from fractions import Fraction as Fr
from math import factorial

# ---------------------------------------------------------------- jets
def jadd(a, b):
    if not a: return dict(b)
    if not b: return dict(a)
    out = dict(a)
    for k, v in b.items():
        nv = out.get(k, 0) + v
        if nv == 0: out.pop(k, None)
        else: out[k] = nv
    return out

def jneg(a): return {k: -v for k, v in a.items()}
def jsub(a, b): return jadd(a, jneg(b))
def jscale(a, s):
    if s == 0: return {}
    return {k: v * s for k, v in a.items()}

def jmul(a, b, ord_):
    if not a or not b: return {}
    out = {}
    for (i1, j1), v1 in a.items():
        for (i2, j2), v2 in b.items():
            i, j = i1 + i2, j1 + j2
            if i + j > ord_: continue
            k = (i, j)
            nv = out.get(k, 0) + v1 * v2
            if nv == 0: out.pop(k, None)
            else: out[k] = nv
    return out

def jdx(a):
    out = {}
    for (i, j), v in a.items():
        if i: out[(i - 1, j)] = v * i
    return out

def jdu(a):
    out = {}
    for (i, j), v in a.items():
        if j: out[(i, j - 1)] = v * j
    return out

def jder(a, d):
    if d == 1: return jdx(a)
    if d == 2: return jdu(a)
    return {}

def jshift(a, di, dj):
    """Multiply by the monomial x^di u^dj."""
    return {(i + di, j + dj): v for (i, j), v in a.items()}

def _one_like(c):
    """The multiplicative unit in the coefficient type of c."""
    return c / c

def jinv1(w, ord_):
    """Inverse of a jet with constant term 1: 1/(1+z) = sum (-z)^n."""
    one = _one_like(w[(0, 0)])
    z = {k: v for k, v in w.items() if k != (0, 0)}
    out = {(0, 0): one}
    term = {(0, 0): one}
    sign = -1
    for _ in range(ord_ + 1):
        term = jmul(term, z, ord_)
        if not term: break
        out = jadd(out, jscale(term, sign))
        sign = -sign
    return out

def jinv_general(w, ord_):
    """Inverse of a jet with nonzero constant term c: (1/c) * 1/(1+z)."""
    c = w[(0, 0)]
    inv_c = _one_like(c) / c
    z = jscale({k: v for k, v in w.items() if k != (0, 0)}, inv_c)
    unit = jadd({(0, 0): _one_like(c)}, z)
    return jscale(jinv1(unit, ord_), inv_c)

def jsqrt1(w, ord_):
    """sqrt of a jet with constant term 1, via Newton with jinv_general."""
    y = {(0, 0): _one_like(w[(0, 0)])}
    for _ in range(6):
        yinv = jinv_general(y, ord_)
        y = jscale(jadd(y, jmul(w, yinv, ord_)), Fr(1, 2))
    return y

# ------------------------------------------------------- jet matrices
def mzero():
    return [[{} for _ in range(4)] for _ in range(4)]

def mmul(A, B, ord_):
    C = mzero()
    for a in range(4):
        for b in range(4):
            s = {}
            for c in range(4):
                if A[a][c] and B[c][b]:
                    s = jadd(s, jmul(A[a][c], B[c][b], ord_))
            C[a][b] = s
    return C

def mscale(A, s):
    return [[jscale(A[a][b], s) for b in range(4)] for a in range(4)]

def madd(A, B):
    return [[jadd(A[a][b], B[a][b]) for b in range(4)] for a in range(4)]

def mconst_inv(M0):
    """Exact inverse of a constant 4x4 matrix (list of lists of numbers)."""
    n = 4
    A = [[Fr(M0[a][b]) for b in range(n)] + [Fr(1) if a == b else Fr(0)
         for b in range(n)] for a in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [v / pv for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [v - f * w for v, w in zip(A[r], A[col])]
    return [[A[a][n + b] for b in range(n)] for a in range(n)]

def minv(M, ord_):
    """Inverse of a jet matrix via Newton, exact."""
    M0 = [[M[a][b].get((0, 0), 0) for b in range(4)] for a in range(4)]
    H0 = mconst_inv(M0)
    H = [[{(0, 0): H0[a][b]} if H0[a][b] != 0 else {}
          for b in range(4)] for a in range(4)]
    I4 = [[{(0, 0): 1} if a == b else {} for b in range(4)] for a in range(4)]
    for _ in range(4):
        MH = mmul(M, H, ord_)
        H = mmul(H, madd(mscale(I4, 2), mscale(MH, -1)), ord_)
    return H

def mdet(M, ord_):
    import itertools
    out = {}
    for perm in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4)
                  if perm[i] > perm[j])
        term = {(0, 0): 1}
        for a in range(4):
            term = jmul(term, M[a][perm[a]], ord_)
            if not term: break
        if term:
            out = jadd(out, jscale(term, -1 if inv % 2 else 1))
    return out

# ------------------------------------------------------------ dual jets
class DJ:
    __slots__ = ('v', 'd')
    def __init__(self, v, d=None):
        self.v = v
        self.d = d if d is not None else {}

def dadd(a, b): return DJ(jadd(a.v, b.v), jadd(a.d, b.d))
def dneg(a): return DJ(jneg(a.v), jneg(a.d))
def dsub(a, b): return DJ(jsub(a.v, b.v), jsub(a.d, b.d))
def dscale(a, s): return DJ(jscale(a.v, s), jscale(a.d, s))

def dmul(a, b, ord_):
    return DJ(jmul(a.v, b.v, ord_),
              jadd(jmul(a.v, b.d, ord_), jmul(a.d, b.v, ord_)))

def dder(a, dirn):
    return DJ(jder(a.v, dirn), jder(a.d, dirn))

def dmul_mat(A, B, ord_):
    C = [[None] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            s = DJ({})
            for c in range(4):
                if (A[a][c].v or A[a][c].d) and (B[c][b].v or B[c][b].d):
                    s = dadd(s, dmul(A[a][c], B[c][b], ord_))
            C[a][b] = s
    return C

# ------------------------------------------------------------- geometry
ORD_G, ORD_GAM, ORD_R, ORD_NR, ORD_L = 7, 6, 5, 4, 4

def geometry(HH, GG):
    """HH, GG: 4x4 DJ matrices (inverse metric, metric).  Returns dict
    with DJ entries: Gam[a][b][c], Ric[a][b], dRic[e][a][b]."""
    Gam = [[[None] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                s = DJ({})
                for d in range(4):
                    if not (HH[a][d].v or HH[a][d].d):
                        continue
                    t = dadd(dadd(dder(GG[d][c], b), dder(GG[d][b], c)),
                             dneg(dder(GG[b][c], d)))
                    s = dadd(s, dmul(HH[a][d], t, ORD_GAM))
                Gam[a][b][c] = dscale(s, Fr(1, 2))
    Rup = [[[[None] * 4 for _ in range(4)] for _ in range(4)]
           for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    s = dsub(dder(Gam[a][b][d], c), dder(Gam[a][b][c], d))
                    for e in range(4):
                        g1, g2 = Gam[a][c][e], Gam[e][b][d]
                        if (g1.v or g1.d) and (g2.v or g2.d):
                            s = dadd(s, dmul(g1, g2, ORD_R))
                        g1, g2 = Gam[a][d][e], Gam[e][b][c]
                        if (g1.v or g1.d) and (g2.v or g2.d):
                            s = dsub(s, dmul(g1, g2, ORD_R))
                    Rup[a][b][c][d] = s
    Ric = [[None] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            s = DJ({})
            for c in range(4):
                s = dadd(s, Rup[c][a][c][b])
            Ric[a][b] = s
    dRic = [[[None] * 4 for _ in range(4)] for _ in range(4)]
    for e in range(4):
        for a in range(4):
            for b in range(4):
                s = dder(Ric[a][b], e)
                for f in range(4):
                    g1 = Gam[f][e][a]
                    if (g1.v or g1.d) and (Ric[f][b].v or Ric[f][b].d):
                        s = dsub(s, dmul(g1, Ric[f][b], ORD_NR))
                    g1 = Gam[f][e][b]
                    if (g1.v or g1.d) and (Ric[a][f].v or Ric[a][f].d):
                        s = dsub(s, dmul(g1, Ric[a][f], ORD_NR))
                dRic[e][a][b] = s
    return {'Gam': Gam, 'Rup': Rup, 'Ric': Ric, 'dRic': dRic, 'GG': GG}

def scalar_L(kind, HH, geo):
    """The three scalars, as DJ jets (order ORD_L)."""
    if kind == 'L2':
        dRic = geo['dRic']
        # raise the three indices of dRic one at a time -> W[e][a][b]
        X = [[[None] * 4 for _ in range(4)] for _ in range(4)]
        for e in range(4):
            for a in range(4):
                for b in range(4):
                    s = DJ({})
                    for e2 in range(4):
                        if (HH[e][e2].v or HH[e][e2].d) and \
                           (dRic[e2][a][b].v or dRic[e2][a][b].d):
                            s = dadd(s, dmul(HH[e][e2], dRic[e2][a][b],
                                             ORD_L))
                    X[e][a][b] = s
        Y = [[[None] * 4 for _ in range(4)] for _ in range(4)]
        for e in range(4):
            for a in range(4):
                for b in range(4):
                    s = DJ({})
                    for a2 in range(4):
                        if (HH[a][a2].v or HH[a][a2].d) and \
                           (X[e][a2][b].v or X[e][a2][b].d):
                            s = dadd(s, dmul(HH[a][a2], X[e][a2][b],
                                             ORD_L))
                    Y[e][a][b] = s
        W = [[[None] * 4 for _ in range(4)] for _ in range(4)]
        for e in range(4):
            for a in range(4):
                for b in range(4):
                    s = DJ({})
                    for b2 in range(4):
                        if (HH[b][b2].v or HH[b][b2].d) and \
                           (Y[e][a][b2].v or Y[e][a][b2].d):
                            s = dadd(s, dmul(HH[b][b2], Y[e][a][b2],
                                             ORD_L))
                    W[e][a][b] = s
        L = DJ({})
        for e in range(4):
            for a in range(4):
                for b in range(4):
                    if (dRic[e][a][b].v or dRic[e][a][b].d) and \
                       (W[e][a][b].v or W[e][a][b].d):
                        L = dadd(L, dmul(dRic[e][a][b], W[e][a][b],
                                         ORD_L))
        return dneg(L)
    if kind == 'Ric3':
        Ric = geo['Ric']
        RicM = [[None] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(4):
                s = DJ({})
                for c in range(4):
                    s = dadd(s, dmul(HH[a][c], Ric[c][b], ORD_L))
                RicM[a][b] = s
        L = DJ({})
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    L = dadd(L, dmul(RicM[a][b],
                                     dmul(RicM[b][c], RicM[c][a], ORD_L),
                                     ORD_L))
        return L
    if kind == 'RiemRic':
        Ric, Rup, GG = geo['Ric'], geo['Rup'], geo['GG']
        Rcov = [[[[None] * 4 for _ in range(4)] for _ in range(4)]
                for _ in range(4)]
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        s = DJ({})
                        for e in range(4):
                            s = dadd(s, dmul(GG[a][e], Rup[e][b][c][d],
                                             ORD_L))
                        Rcov[a][b][c][d] = s
        # raise Rcov[p][r][q][s] index by index -> RU
        def raise_idx(T, slot):
            out = [[[[None] * 4 for _ in range(4)] for _ in range(4)]
                   for _ in range(4)]
            for i0 in range(4):
                for i1 in range(4):
                    for i2 in range(4):
                        for i3 in range(4):
                            idx = [i0, i1, i2, i3]
                            s = DJ({})
                            for m in range(4):
                                h = HH[idx[slot]][m]
                                if not (h.v or h.d):
                                    continue
                                src = list(idx); src[slot] = m
                                t = T[src[0]][src[1]][src[2]][src[3]]
                                if t.v or t.d:
                                    s = dadd(s, dmul(h, t, ORD_L))
                            out[i0][i1][i2][i3] = s
            return out
        RU = raise_idx(raise_idx(raise_idx(raise_idx(
            Rcov, 3), 2), 1), 0)
        L = DJ({})
        for p in range(4):
            for q in range(4):
                if not (Ric[p][q].v or Ric[p][q].d):
                    continue
                for r in range(4):
                    for s_ in range(4):
                        if (Ric[r][s_].v or Ric[r][s_].d) and \
                           (RU[p][r][q][s_].v or RU[p][r][q][s_].d):
                            L = dadd(L, dmul(Ric[p][q],
                                             dmul(Ric[r][s_],
                                                  RU[p][r][q][s_], ORD_L),
                                             ORD_L))
        return L
    raise ValueError(kind)
