#!/usr/bin/env python3
"""Gate-37 driver: backgrounds, background pass, dual extraction of
E[scalar] at a point, assembly of E_ab, its mixed components and its
exact divergence at the point.  Uses only g37_jets.py (this gate's own
machinery) plus stored record data as targets/background definitions.
"""
import sys
from fractions import Fraction as Fr
from math import factorial, sqrt

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate37/work')
from g37_jets import (DJ, dadd, dsub, dneg, dscale, dmul, geometry,
                      scalar_L, jadd, jsub, jneg, jscale, jmul, jdx, jdu,
                      jder, jshift, jinv1, jsqrt1, mmul, mscale, madd,
                      minv, mdet, ORD_G, ORD_L)

MONOS = sorted([(i, j) for i in range(4) for j in range(4) if i + j <= 3],
               key=lambda m: (m[0] + m[1], m[0], m[1]))
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]

def mfact(M):
    return factorial(M[0]) * factorial(M[1])

# ------------------------------------------------------------ 1d series
def smul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def sinv(a):
    """Series inverse, a[0] != 0."""
    n = len(a)
    out = [0] * n
    out[0] = 1 / a[0]
    for k in range(1, n):
        s = sum(a[i] * out[k - i] for i in range(1, k + 1))
        out[k] = -s / a[0]
    return out

def s2_from_rjet(rjet):
    return smul(rjet, rjet)

# ------------------------------------------------------------- metric
def build_metric(S2, gtt, exact=True):
    one = Fr(1) if exact else 1.0
    if exact:
        c2 = {0: Fr(1), 2: Fr(-1), 4: Fr(1, 3), 6: Fr(-2, 45)}
    else:
        c2 = {0: 1.0, 2: -1.0, 4: 1.0 / 3.0, 6: -2.0 / 45.0}
    g = [[{} for _ in range(4)] for _ in range(4)]
    for k, v in enumerate(gtt):
        if v != 0:
            g[0][0][(k, 0)] = v
    g[1][1] = {(0, 0): one}
    for k, v in enumerate(S2):
        if v != 0:
            g[2][2][(k, 0)] = v
    for k, v in enumerate(S2):
        if v == 0:
            continue
        for d, cv in c2.items():
            g[3][3][(k, d)] = v * cv
    return g

def dj_plain(M):
    return [[DJ(M[a][b]) for b in range(4)] for a in range(4)]

def background(S2, gtt, exact=True):
    """Returns dict with GG, HH (plain jets), and a function to run the
    geometry/scalar graph with DJ inputs."""
    GG = build_metric(S2, gtt, exact)
    HH = minv(GG, ORD_G)
    return GG, HH

def run_graph(GGd, HHd, kind):
    geo = geometry(HHd, GGd)
    geo['GG'] = GGd
    L = scalar_L(kind, HHd, geo)
    return geo, L

def background_pass(S2, gtt, kind, exact=True):
    GG, HH = background(S2, gtt, exact)
    geo, L = run_graph(dj_plain(GG), dj_plain(HH), kind)
    Ric = geo['Ric']
    HH0 = [[HH[a][b].get((0, 0), 0) for b in range(4)] for a in range(4)]
    Ric_mixed = [sum(HH0[a][c] * Ric[c][a].v.get((0, 0), 0)
                     for c in range(4)) for a in range(4)]
    D = jneg(mdet(GG, 4))          # -det g  (positive jet)
    D0 = D.get((0, 0), 0)
    sigma = jsqrt1(jscale(D, 1 / D0), 4)
    Gam0 = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam0[(a, b, c)] = geo['Gam'][a][b][c].v.get((0, 0), 0)
    return {'GG': GG, 'HH': HH, 'Ric_mixed': Ric_mixed,
            'L_jet': L.v, 'L0': L.v.get((0, 0), 0), 'sigma': sigma,
            'sigma_inv': jinv1(sigma, 4), 'Gam0': Gam0, 'geo': geo}

# ---------------------------------------------------------- extraction
def extract_E(S2, gtt, kind, exact=True, bg=None):
    """Full E[scalar] evaluation at the point.  Returns dict with
    E_cov (4x4 at 0), E_mixed diag, full E_mixed, trace, div, offdiag."""
    if bg is None:
        bg = background_pass(S2, gtt, kind, exact)
    GG, HH = bg['GG'], bg['HH']
    one = Fr(1) if exact else 1.0
    # --- dual runs: Btilde[(a,b,M)] = dL/dc_{ab,M} as a jet
    Btilde = {}
    for (a, b) in PAIRS:
        for M in MONOS:
            dH = [[{} for _ in range(4)] for _ in range(4)]
            dH[a][b] = {M: one}
            dH[b][a] = {M: one}
            dGG = mscale(mmul(GG, mmul(dH, GG, ORD_G), ORD_G), -1)
            HHd = [[DJ(HH[i][j], dH[i][j]) for j in range(4)]
                   for i in range(4)]
            GGd = [[DJ(GG[i][j], dGG[i][j]) for j in range(4)]
                   for i in range(4)]
            _, L = run_graph(GGd, HHd, kind)
            Btilde[(a, b, M)] = L.d
    # --- triangular solve for A_{ab,I} (jets, order |I|+1)
    A = {}
    for (a, b) in PAIRS:
        Aab = {}
        for M in MONOS:
            acc = dict(Btilde[(a, b, M)])
            for I in MONOS:
                if I == M:
                    continue
                if I[0] > M[0] or I[1] > M[1]:
                    continue
                dI = (M[0] - I[0], M[1] - I[1])
                coef = Fr(mfact(M), mfact(dI))
                acc = jsub(acc, jscale(jshift(Aab[I], dI[0], dI[1]),
                                       coef))
            Aab[M] = jscale(acc, Fr(1, mfact(M)))
            # truncate to order |M|+1
            Aab[M] = {k: v for k, v in Aab[M].items()
                      if k[0] + k[1] <= M[0] + M[1] + 1}
        A[(a, b)] = Aab
    # --- assemble E
    sigma, sigma_inv = bg['sigma'], bg['sigma_inv']
    Ljet, L0 = bg['L_jet'], bg['L0']
    GG0 = [[GG[a][b].get((0, 0), 0) for b in range(4)] for a in range(4)]
    HH0 = [[HH[a][b].get((0, 0), 0) for b in range(4)] for a in range(4)]
    E0 = [[0] * 4 for _ in range(4)]
    Ejet = [[{} for _ in range(4)] for _ in range(4)]
    for (a, b) in PAIRS:
        tot0 = 0
        totjet = {}
        for I in MONOS:
            sA = jmul(sigma, A[(a, b)][I], 4)
            sgn = -1 if ((I[0] + I[1]) % 2) else 1
            tot0 += sgn * mfact(I) * sA.get(I, 0)
            dI_jet = sA
            for _ in range(I[0]):
                dI_jet = jdx(dI_jet)
            for _ in range(I[1]):
                dI_jet = jdu(dI_jet)
            totjet = jadd(totjet, jscale(dI_jet, sgn))
        totjet = jmul(sigma_inv, totjet, 1)
        totjet = jadd(totjet, jscale(jmul(Ljet, GG[a][b], 1),
                                     Fr(-1, 2)))
        totjet = {k: v for k, v in totjet.items() if k[0] + k[1] <= 1}
        val0 = tot0 - Fr(1, 2) * L0 * GG0[a][b]
        E0[a][b] = E0[b][a] = val0
        Ejet[a][b] = Ejet[b][a] = totjet
    # consistency: Ejet constant term must equal E0
    for a in range(4):
        for b in range(4):
            assert Ejet[a][b].get((0, 0), 0) == E0[a][b], (a, b)
    # mixed components at 0
    Emixed = [[sum(HH0[a][c] * E0[c][b] for c in range(4))
               for b in range(4)] for a in range(4)]
    trace = sum(Emixed[a][a] for a in range(4))
    offdiag = max(abs(E0[a][b]) for a in range(4) for b in range(4)
                  if a != b)
    # divergence at 0 from the order-1 jets of E^{ab}
    Eup = [[{} for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            s = {}
            for c in range(4):
                for d in range(4):
                    s = jadd(s, jmul(jmul(HH[a][c], HH[b][d], 1),
                                     Ejet[c][d], 1))
            Eup[a][b] = {k: v for k, v in s.items() if k[0] + k[1] <= 1}
    Gam0 = bg['Gam0']
    div = []
    for b in range(4):
        val = 0
        for a in range(4):
            if a == 1:
                val += jdx(Eup[a][b]).get((0, 0), 0)
            elif a == 2:
                val += jdu(Eup[a][b]).get((0, 0), 0)
            for c in range(4):
                val += Gam0[(a, a, c)] * Eup[c][b].get((0, 0), 0)
                val += Gam0[(b, a, c)] * Eup[a][c].get((0, 0), 0)
        div.append(val)
    return {'E_cov': E0, 'E_mixed': Emixed,
            'E_mixed_diag': [Emixed[a][a] for a in range(4)],
            'trace': trace, 'div': div, 'offdiag_max': offdiag,
            'Ric_mixed': bg['Ric_mixed'], 'L0': L0}

# -------------------------------------------------------------- points
RJET_A = [Fr(1), Fr(0), Fr(1, 4), Fr(0), Fr(-1, 48), Fr(0), Fr(11, 2880),
          Fr(0), Fr(-73, 80640), Fr(0), Fr(887, 3628800)]
RJET_C12 = [Fr(1), Fr(0), Fr(5, 4), Fr(0), Fr(-15, 16), Fr(0), Fr(63, 64),
            Fr(0), Fr(-2421, 1792), Fr(0), Fr(19043, 8960)]

def point(name):
    """Returns (S2, gtt, exact)."""
    if name == 'ellis_throat':
        return [Fr(1), Fr(0), Fr(1)], [Fr(-1)], True
    if name == 'ellis_l1':
        return [Fr(2), Fr(2), Fr(1)], [Fr(-1)], True
    if name == 'ellis_R15_float':
        l0 = sqrt(1.25)
        return [2.25, 2.0 * l0, 1.0], [-1.0], False
    if name == 'A_throat':
        return s2_from_rjet(RJET_A), [Fr(-1)], True
    if name == 'C_1_2':
        return s2_from_rjet(RJET_C12), [Fr(-1)], True
    if name == 'E_1_10':
        S2 = s2_from_rjet(RJET_A)
        invR = sinv(RJET_A)
        invR2 = smul(invR, invR)
        eps = Fr(1, 10)
        arg = [(Fr(1) if k == 0 else Fr(0)) - invR[k] + eps * invR2[k]
               for k in range(len(RJET_A))]
        return S2, [-v for v in arg], True
    raise ValueError(name)
