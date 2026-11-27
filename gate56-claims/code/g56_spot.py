#!/usr/bin/env python3
"""
g56_spot.py -- Gate-56 spot check: the screen-1347
configuration's NEC argmin point re-evaluated END TO END
in 50-digit mpmath (profiles via the gate's mpmath
spline solver and mpmath analytic profiles; metric
derivatives via the sympy-derived mpmath evaluators;
contraction, tetrad, eigenvalue margins and the secular
worst-null all in mpmath). Output:
gate56/results/g56_spot.json.
"""
import json
import sys

import numpy as np
from mpmath import mp, mpf, sqrt as msqrt

mp.dps = 50
WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, f'{WP}/gate56/work')
import g56_lib as G  # noqa: E402
import g56_splines as GS  # noqa: E402
import g56_tensor as GT  # noqa: E402

conf418 = json.load(open(f'{WP}/phase418/results/p418_confirmation.json'))
cbj = conf418['criterion_best_joint']
cfg = {'muN': cbj['config']['muN'], 'muM': cbj['config']['muM'],
       'K_B': 17, 'vN': cbj['config']['vN'],
       'vM': cbj['config']['vM'], 'K_S': 9,
       'vS': cbj['config']['vS_scaled']}

# the float64 gate read identifies the point
rec = G.set_read_g56(cfg)
pt_f = rec['nec_argmin_pt']
ptf = G.point_read_g56(cfg, pt_f)
print('float point: r', rec['nec_argmin_r'], 'nec',
      ptf['nec'], 'wn', ptf['worst_null']['value'])

# ------------------------------------------------ mpmath profiles
def ss_mp(u):
    uc = min(max(u, mpf(0)), mpf(1))
    s = 6 * uc ** 5 - 15 * uc ** 4 + 10 * uc ** 3
    sp = 30 * uc ** 4 - 60 * uc ** 3 + 30 * uc ** 2
    spp = 120 * uc ** 3 - 180 * uc ** 2 + 60 * uc
    if not (u > 0 and u < 1):
        sp, spp = mpf(0), mpf(0)
    return s, sp, spp


def U_mp(r, a, b):
    s, sp, spp = ss_mp((r - a) / (b - a))
    return s, sp / (b - a), spp / (b - a) ** 2


def S_ab22_mp(r):
    if r <= 10:
        return mpf(1), mpf(0), mpf(0)
    if r >= 20:
        return mpf(0), mpf(0), mpf(0)
    u = (r - 10) / 10
    B = mp.beta(3, 3)
    S = 1 - mp.betainc(3, 3, 0, u, regularized=True)
    Sp = -(u ** 2 * (1 - u) ** 2) / (10 * B)
    Spp = -(2 * u * (1 - u) * (1 - 2 * u)) / (100 * B)
    return S, Sp, Spp


def shape_B_mp(r):
    Hx, Hpx, Hppx = ss_mp((r - 10) / 3)
    Hy, Hpy, Hppy = ss_mp((20 - r) / 3)
    B = Hx * Hy
    Bp = (Hpx * Hy - Hx * Hpy) / 3
    Bpp = (Hppx * Hy - 2 * Hpx * Hpy + Hx * Hppy) / 9
    return B, Bp, Bpp


def spline_mp(K, vec):
    xk = [mpf(float(v)) for v in np.linspace(10.0, 20.0, K)]
    return GS.NotAKnotSplineMP(mp, xk, [mpf(float(v))
                                        for v in vec])


SPL = {}


def corr_mp(K, vec, r):
    key = (K, tuple(vec))
    if key not in SPL:
        SPL[key] = spline_mp(K, vec)
    return SPL[key].eval_all(r)


def profiles_mp(cfg, r):
    S, Sp, Spp = S_ab22_mp(r)
    S, Sp, Spp = mpf('0.7') * S, mpf('0.7') * Sp, mpf('0.7') * Spp
    B, Bp, Bpp = shape_B_mp(r)
    A = mpf(float(G.LAPSE_A))
    N, Np, Npp = 1 + A * B, A * Bp, A * Bpp
    U1, U1p, U1pp = U_mp(r, mpf('8.5'), mpf(20))
    U2, U2p, U2pp = U_mp(r, mpf(21), mpf(24))
    M = 1 + 6 * (U1 - U2); Mp = 6 * (U1p - U2p)
    Mpp = 6 * (U1pp - U2pp)
    for K, vec, tgt in ((33, G.A2_VS, 'S'), (33, G.A2_VN, 'N'),
                        (33, G.A2_VM, 'M')):
        d, dp, dpp = corr_mp(K, [float(v) for v in vec], r)
        if tgt == 'S':
            S, Sp, Spp = S + d, Sp + dp, Spp + dpp
        elif tgt == 'N':
            N, Np, Npp = N + d, Np + dp, Npp + dpp
        else:
            M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    mu = mpf('1.15')
    S, Sp, Spp = mu * S, mu * Sp, mu * Spp
    N, Np, Npp = mu * N, mu * Np, mu * Npp
    M, Mp, Mpp = 1 + mu * (M - 1), mu * Mp, mu * Mpp
    for K, vec, tgt in ((17, G.H2_VS, 'S'), (17, G.H2_VN, 'N'),
                        (17, G.H2_VM, 'M')):
        d, dp, dpp = corr_mp(K, [float(v) for v in vec], r)
        if tgt == 'S':
            S, Sp, Spp = S + d, Sp + dp, Spp + dpp
        elif tgt == 'N':
            N, Np, Npp = N + d, Np + dp, Npp + dpp
        else:
            M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    dN, dNp, dNpp = corr_mp(17, cfg['vN'], r)
    dM, dMp, dMpp = corr_mp(17, cfg['vM'], r)
    muN, muM = mpf(float(cfg['muN'])), mpf(float(cfg['muM']))
    N = muN * N + dN; Np = muN * Np + dNp; Npp = muN * Npp + dNpp
    M = 1 + muM * (M - 1) + dM; Mp = muM * Mp + dMp
    Mpp = muM * Mpp + dMpp
    S, Sp, Spp = corr_mp(9, cfg['vS'], r)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


# ------------------------------------------------ mpmath tensor
def inv_mp(A):
    n = A.rows
    cols = []
    for j in range(n):
        e = mp.matrix(n, 1)
        e[j] = 1
        cols.append(mp.lu_solve(A, e))
    out = mp.matrix(n, n)
    for j in range(n):
        for i in range(n):
            out[i, j] = cols[j][i]
    return out


def T_mp(pt, pr):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = pr
    x, y, z = pt
    r = msqrt(x * x + y * y + z * z)
    beta = mpf(1.1)
    g = mp.matrix(4, 4)
    g[0, 0] = -N * N
    g[0, 1] = g[1, 0] = -beta * S
    nn = [x / r, y / r, z / r]
    for i in range(3):
        for j in range(3):
            g[i + 1, j + 1] = (1 if i == j else 0) \
                + (M - 1) * nn[i] * nn[j]
    dg_s = GT.dg_mp(x, y, z, N, Np, Npp, M, Mp, Mpp,
                    S, Sp, Spp, beta)
    ddg_s = GT.ddg_mp(x, y, z, N, Np, Npp, M, Mp, Mpp,
                      S, Sp, Spp, beta)
    DG = [[[mpf(0)] * 4 for _ in range(4)] for _ in range(4)]
    DDG = [[[[mpf(0)] * 4 for _ in range(4)] for _ in range(4)]
           for _ in range(4)]
    for a in range(3):
        for mu in range(4):
            for nu in range(4):
                DG[a + 1][mu][nu] = mpf(dg_s[a][mu][nu])
                for b in range(3):
                    DDG[a + 1][b + 1][mu][nu] = mpf(
                        ddg_s[a][b][mu][nu])
    ginv = inv_mp(g)
    Gam = [[[mpf(0)] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                s = mpf(0)
                for d in range(4):
                    s += ginv[a, d] * (
                        DG[b][d][c] + DG[c][d][b] - DG[d][b][c])
                Gam[a][b][c] = s / 2
    dGam = [[[[mpf(0)] * 4 for _ in range(4)] for _ in range(4)]
            for _ in range(4)]
    for e in range(4):
        dginv = [[mpf(0)] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(4):
                s = mpf(0)
                for mm in range(4):
                    for n_ in range(4):
                        s += ginv[a, mm] * DG[e][mm][n_] \
                            * ginv[n_, b]
                dginv[a][b] = -s
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    s = mpf(0)
                    for d in range(4):
                        s += dginv[a][d] * (
                            DG[b][d][c] + DG[c][d][b]
                            - DG[d][b][c]) \
                            + ginv[a, d] * (
                                DDG[e][b][d][c]
                                + DDG[e][c][d][b]
                                - DDG[e][d][b][c])
                    dGam[e][a][b][c] = s / 2
    Ric = [[mpf(0)] * 4 for _ in range(4)]
    for b in range(4):
        for d in range(4):
            s = mpf(0)
            for a in range(4):
                s += dGam[a][a][b][d] - dGam[d][a][b][a]
                for e in range(4):
                    s += Gam[a][a][e] * Gam[e][b][d] \
                        - Gam[a][d][e] * Gam[e][b][a]
            Ric[b][d] = s
    Rs = mpf(0)
    for a in range(4):
        for b in range(4):
            Rs += ginv[a, b] * Ric[a][b]
    T = [[(Ric[a][b] - Rs * g[a, b] / 2) / (8 * mp.pi)
          for b in range(4)] for a in range(4)]
    return T, g


def that_mp(T, g):
    gamma = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            gamma[i, j] = g[i + 1, j + 1]
    beta_cov = [g[0, i + 1] for i in range(3)]
    ginv3 = inv_mp(gamma)
    beta_up = [sum(ginv3[i, j] * beta_cov[j] for j in range(3))
               for i in range(3)]
    alpha2 = -g[0, 0] + sum(beta_cov[i] * beta_up[i]
                            for i in range(3))
    alpha = msqrt(alpha2)
    E_val, E_vec = mp.eigsy(gamma)
    E = mp.matrix(4, 4)
    E[0, 0] = 1 / alpha
    for i in range(3):
        E[i + 1, 0] = -beta_up[i] / alpha
        lam = E_val[i]
        for j in range(3):
            E[j + 1, i + 1] = E_vec[j, i] / msqrt(lam)
    That = [[mpf(0)] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            s = mpf(0)
            for mu in range(4):
                for nu in range(4):
                    s += E[mu, a] * E[nu, b] * T[mu][nu]
            That[a][b] = s
    for a in range(4):
        for b in range(a + 1, 4):
            v = (That[a][b] + That[b][a]) / 2
            That[a][b] = That[b][a] = v
    return That


def charpoly_roots_mp(Mm):
    """Eigenvalues of a 4x4 mpmath matrix via the
    Faddeev-LeVerrier characteristic polynomial +
    polyroots."""
    n = 4
    A = Mm
    Mk = mp.eye(n)
    coeffs = [mpf(1)]
    for k in range(1, n + 1):
        AM = A * Mk
        ck = -sum(AM[i, i] for i in range(n)) / k
        coeffs.append(ck)
        Mk = AM + ck * mp.eye(n)
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=20)
    return roots


pt = [mpf(float(v)) for v in pt_f]
r_mp = msqrt(sum(v * v for v in pt))
pr = profiles_mp(cfg, r_mp)
T, g = T_mp(pt, pr)
That = that_mp(T, g)
Mm = mp.matrix(4, 4)
for a in range(4):
    for b in range(4):
        Mm[a, b] = -That[a][b] if a == 0 else That[a][b]
roots = charpoly_roots_mp(Mm)
roots = sorted(roots, key=lambda v: mp.re(v))
lam = [mp.re(v) for v in roots]
max_imag = max(abs(mp.im(v)) for v in roots)
rho = -lam[0]
ps = lam[1:]
nec = min(rho + p for p in ps)
wec = min(rho, nec)
sec = min(nec, rho + sum(ps))
dec = min(rho, rho - max(abs(p) for p in ps))

# secular worst-null in mpmath
A3 = [[That[i + 1][j + 1] for j in range(3)] for i in range(3)]
f3 = [That[0][i + 1] for i in range(3)]
Am = mp.matrix(3, 3)
for i in range(3):
    for j in range(3):
        Am[i, j] = (A3[i][j] + A3[j][i]) / 2
Ev, Vec = mp.eigsy(Am)
lamA = [Ev[i] for i in range(3)]
fh = [sum(Vec[j, i] * f3[j] for j in range(3)) for i in range(3)]


def phi_mp(mu):
    return sum((fh[i] / (lamA[i] - mu)) ** 2 for i in range(3)) - 1


lo = lamA[0] - (msqrt(sum(v * v for v in f3)) + 1)
hi = lamA[0] - mpf('1e-30')
for _ in range(400):
    mid = (lo + hi) / 2
    if phi_mp(mid) > 0:
        hi = mid
    else:
        lo = mid
mu = (lo + hi) / 2
nvec = [-sum(Vec[j, i] * fh[i] / (lamA[i] - mu)
             for i in range(3)) for j in range(3)]
nn = msqrt(sum(v * v for v in nvec))
nvec = [v / nn for v in nvec]
q = That[0][0] + 2 * sum(f3[i] * nvec[i] for i in range(3)) \
    + sum(nvec[i] * A3[i][j] * nvec[j]
          for i in range(3) for j in range(3))

out = {
    'point_float': [float(v) for v in pt_f],
    'r_mp': mp.nstr(r_mp, 30),
    'nec_mp': mp.nstr(nec, 30), 'wec_mp': mp.nstr(wec, 30),
    'sec_mp': mp.nstr(sec, 30), 'dec_mp': mp.nstr(dec, 30),
    'rho_mp': mp.nstr(rho, 30),
    'worst_null_mp': mp.nstr(q, 30),
    'max_imag_eig': mp.nstr(max_imag, 5),
    'float_nec': ptf['nec'], 'float_rho_eig': ptf['rho_eig'],
    'float_worst_null': ptf['worst_null']['value'],
    'stored_nec': cbj['joint'],
    'stored_worst_null': cbj['worst_null_at_nec_argmin'],
    'nec_mp_minus_float': mp.nstr(nec - mpf(ptf['nec']), 5),
    'wn_mp_minus_float': mp.nstr(q - mpf(
        ptf['worst_null']['value']), 5),
    'profiles_mp_vs_float': {
        k: mp.nstr(a - mpf(float(np.asarray(b).ravel()[0])), 5)
        for k, a, b in zip(
            ('S', 'Sp', 'Spp', 'N', 'Np', 'Npp', 'M', 'Mp',
             'Mpp'), pr, G.profiles_g56(cfg, pt_f.reshape(1, 3)))}}
with open(f'{WP}/gate56/results/g56_spot.json', 'w') as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
