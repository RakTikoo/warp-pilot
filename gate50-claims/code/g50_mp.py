#!/usr/bin/env python3
"""
g50_mp.py -- Gate-50 named-point verification in
50-digit mpmath: the profile stack, the tensor, the
Eulerian frame, the Hawking-Ellis margins and the
exact worst-null are all recomputed in arbitrary
precision at the two deciding points (the Phase 400
base winner's SET argmin; the Phase 405 winner's SET
argmin), and the SS7 peak arithmetic is done exactly
(the winner's peak vs the registered bar, from the
stored float64 inputs). Also pins the winning
shape's derivative sign scan (the monotonicity
question of claim (b)).
Writes gate50/results/g50_mp.json.
"""
import json
import os
import sys

import numpy as np
from mpmath import mp, mpf

mp.dps = 50

WP = os.environ.get('G50_WP', '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, f'{WP}/gate50/work')
import g50_lib as G  # noqa: E402

out = {}

# ================================================= mp profiles
def nak_moments_mp(xk, yk):
    n = len(xk)
    h = [mpf(xk[i + 1]) - mpf(xk[i]) for i in range(n - 1)]
    A = mp.matrix(n, n)
    b = mp.matrix(n, 1)
    A[0, 0] = -h[1]
    A[0, 1] = h[0] + h[1]
    A[0, 2] = -h[0]
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 6 * ((mpf(yk[i + 1]) - mpf(yk[i])) / h[i]
                    - (mpf(yk[i]) - mpf(yk[i - 1])) / h[i - 1])
    A[n - 1, n - 3] = -h[n - 2]
    A[n - 1, n - 2] = h[n - 3] + h[n - 2]
    A[n - 1, n - 1] = -h[n - 3]
    return mp.lu_solve(A, b)


_SPL_MP = {}


def corr_mp(vals, K, r):
    key = (K, tuple(float(v) for v in vals))
    if key not in _SPL_MP:
        xk = [mpf(v) for v in G.knots(K)]
        yk = [mpf(v) for v in vals]
        _SPL_MP[key] = (xk, yk, nak_moments_mp(
            [float(v) for v in G.knots(K)], vals))
    xk, yk, M = _SPL_MP[key]
    n = len(xk)
    if r <= xk[0]:
        return yk[0], mpf(0), mpf(0)
    if r >= xk[-1]:
        return yk[-1], mpf(0), mpf(0)
    i = 0
    while not (xk[i] <= r <= xk[i + 1]):
        i += 1
    h = xk[i + 1] - xk[i]
    A_ = (xk[i + 1] - r) / h
    B_ = (r - xk[i]) / h
    d = (A_ * yk[i] + B_ * yk[i + 1]
         + ((A_ ** 3 - A_) * M[i] + (B_ ** 3 - B_) * M[i + 1])
         * h ** 2 / 6)
    dp = ((yk[i + 1] - yk[i]) / h
          + h / 6 * ((1 - 3 * A_ ** 2) * M[i]
                     + (3 * B_ ** 2 - 1) * M[i + 1]))
    dpp = A_ * M[i] + B_ * M[i + 1]
    return d, dp, dpp


def s_ab_mp(r):
    if r <= 10:
        return mpf(1), mpf(0), mpf(0)
    if r >= 20:
        return mpf(0), mpf(0), mpf(0)
    u = (r - 10) / 10
    w = 1 - u
    S = 1 - (10 * u ** 3 * w ** 2 + 5 * u ** 4 * w + u ** 5)
    Sp = -3 * u ** 2 * w ** 2
    Spp = -mpf('0.6') * u * w * (1 - 2 * u)
    return S, Sp, Spp


def H_mp(t):
    if t <= 0:
        return mpf(0), mpf(0), mpf(0)
    if t >= 1:
        return mpf(1), mpf(0), mpf(0)
    v = 10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5
    vp = 30 * t ** 2 * (1 - t) ** 2
    vpp = 60 * t * (1 - t) * (1 - 2 * t)
    return v, vp, vpp


def plateau_mp(r):
    Ha, Hpa, Hppa = H_mp((r - 10) / 3)
    Hb, Hpb, Hppb = H_mp((20 - r) / 3)
    B = Ha * Hb
    Bp = (Hpa * Hb - Ha * Hpb) / 3
    Bpp = (Hppa * Hb - 2 * Hpa * Hpb + Ha * Hppb) / 9
    return B, Bp, Bpp


def ramp_mp(r, a, b):
    a = mpf(a)
    b = mpf(b)
    if r <= a:
        return mpf(0), mpf(0), mpf(0)
    if r >= b:
        return mpf(1), mpf(0), mpf(0)
    x = (r - a) / (b - a)
    U = 6 * x ** 5 - 15 * x ** 4 + 10 * x ** 3
    Up = (30 * x ** 4 - 60 * x ** 3 + 30 * x ** 2) / (b - a)
    Upp = (120 * x ** 3 - 180 * x ** 2 + 60 * x) / (b - a) ** 2
    return U, Up, Upp


def base_mp(r):
    S, Sp, Spp = s_ab_mp(r)
    lam = mpf(G.LAM_S)
    S, Sp, Spp = lam * S, lam * Sp, lam * Spp
    B, Bp, Bpp = plateau_mp(r)
    A = mpf(G.WINNER_A)
    N, Np, Npp = 1 + A * B, A * Bp, A * Bpp
    U1, U1p, U1pp = ramp_mp(r, '8.5', '20')
    U2, U2p, U2pp = ramp_mp(r, '21', '24')
    M = 1 + 6 * (U1 - U2)
    Mp = 6 * (U1p - U2p)
    Mpp = 6 * (U1pp - U2pp)
    return [S, Sp, Spp, N, Np, Npp, M, Mp, Mpp]


def add_corr_mp(prof, vecs, K, r):
    out = list(prof)
    for i, key in enumerate(('vS', 'vN', 'vM')):
        d, dp, dpp = corr_mp(vecs[key], K, r)
        out[3 * i] += d
        out[3 * i + 1] += dp
        out[3 * i + 2] += dpp
    return out


def h2_mp(r):
    prof = add_corr_mp(base_mp(r),
                       {k: [float(v) for v in G.A2[k]]
                        for k in ('vS', 'vN', 'vM')}, 33, r)
    mu = mpf(G.MU_H2)
    prof = [mu * prof[0], mu * prof[1], mu * prof[2],
            mu * prof[3], mu * prof[4], mu * prof[5],
            1 + mu * (prof[6] - 1), mu * prof[7], mu * prof[8]]
    prof = add_corr_mp(prof,
                       {k: [float(v) for v in G.H2V[k]]
                        for k in ('vS', 'vN', 'vM')}, 17, r)
    return prof


def winner_base_mp(r):
    prof = h2_mp(r)
    muN, muM = mpf(G.WIN_MUN), mpf(G.WIN_MUM)
    N = muN * prof[3]
    Np = muN * prof[4]
    Npp = muN * prof[5]
    M = 1 + muM * (prof[6] - 1)
    Mp = muM * prof[7]
    Mpp = muM * prof[8]
    d, dp, dpp = corr_mp([float(v) for v in G.WIN_VN], 17, r)
    N, Np, Npp = N + d, Np + dp, Npp + dpp
    d, dp, dpp = corr_mp([float(v) for v in G.WIN_VM], 17, r)
    M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    return [mpf(0), mpf(0), mpf(0), N, Np, Npp, M, Mp, Mpp]


def winner405_mp(r):
    prof = winner_base_mp(r)
    d, dp, dpp = corr_mp([float(v) for v in G.SHAPEC_CRIT], 9, r)
    prof[0], prof[1], prof[2] = d, dp, dpp
    return prof


# ================================================= mp tensor
def T_mp(pt, prof):
    """(T, g, That) at a Cartesian point (mpf triple)
    with profile 9-tuple of mpf, all in mpmath."""
    F = G.tensor_funcs_mp()
    x, y, z = pt
    r = mp.sqrt(x * x + y * y + z * z)
    args = [x, y, z, r] + list(prof)
    g = mp.matrix(4, 4)
    DG = {}
    DDG = {}
    for (mu, nu), f in F['g'].items():
        v = f(*args)
        g[mu, nu] = v
        g[nu, mu] = v
    for (k, mu, nu), f in F['dg'].items():
        v = f(*args)
        DG[(k + 1, mu, nu)] = v
        DG[(k + 1, nu, mu)] = v
    for (k, l, mu, nu), f in F['ddg'].items():
        v = f(*args)
        DDG[(k + 1, l + 1, mu, nu)] = v
        DDG[(k + 1, l + 1, nu, mu)] = v

    def dg(e, mu, nu):
        return DG.get((e, mu, nu), mpf(0))

    def ddg(e1, e2, mu, nu):
        return DDG.get((e1, e2, mu, nu), mpf(0))

    ginv = mp.inverse(g)
    Gam = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam[a, b, c] = mpf(1) / 2 * sum(
                    ginv[a, d] * (dg(b, d, c) + dg(c, d, b)
                                  - dg(d, b, c))
                    for d in range(4))
    dGinv = {}
    for e in range(4):
        for a in range(4):
            for b in range(4):
                dGinv[e, a, b] = -sum(
                    ginv[a, m] * dg(e, m, n) * ginv[n, b]
                    for m in range(4) for n in range(4))
    dGam = {}
    for e in range(4):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = [dg(b, d, c) + dg(c, d, b) - dg(d, b, c)
                          for d in range(4)]
                    dt = [ddg(e, b, d, c) + ddg(e, c, d, b)
                          - ddg(e, d, b, c) for d in range(4)]
                    dGam[e, a, b, c] = mpf(1) / 2 * (
                        sum(dGinv[e, a, d] * t1[d] for d in range(4))
                        + sum(ginv[a, d] * dt[d] for d in range(4)))
    Ric = mp.matrix(4, 4)
    for b in range(4):
        for d in range(4):
            val = mpf(0)
            for a in range(4):
                val += dGam[a, a, b, d] - dGam[d, a, b, a]
            for a in range(4):
                for e in range(4):
                    val += (Gam[a, a, e] * Gam[e, b, d]
                            - Gam[a, d, e] * Gam[e, b, a])
            Ric[b, d] = val
    Rs = sum(ginv[a, b] * Ric[a, b]
             for a in range(4) for b in range(4))
    T = mp.matrix(4, 4)
    for a in range(4):
        for b in range(4):
            T[a, b] = (Ric[a, b] - mpf(1) / 2 * Rs * g[a, b]) \
                / (8 * mp.pi)
    # Eulerian frame
    gamma = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            gamma[i, j] = g[i + 1, j + 1]
    beta_cov = mp.matrix([g[0, 1], g[0, 2], g[0, 3]])
    gamma_inv = mp.inverse(gamma)
    beta_up = gamma_inv * beta_cov
    alpha2 = -g[0, 0] + sum(beta_cov[i] * beta_up[i]
                             for i in range(3))
    alpha = mp.sqrt(alpha2)
    evals, V = mp.eigsy(gamma)
    E = mp.matrix(4, 4)
    E[0, 0] = 1 / alpha
    for i in range(3):
        E[i + 1, 0] = -beta_up[i] / alpha
        for j in range(3):
            E[j + 1, i + 1] = V[j, i] / mp.sqrt(evals[i])
    That = E.T * T * E
    That = (That + That.T) / 2
    return T, g, That


def margins_mp(That):
    """Hawking-Ellis margins at one point in mpmath
    (eigenvalues of the mixed tensor by mp.eig;
    Type-I test per the registered definitions with
    the thresholds scaled to the working precision),
    plus the exact worst null by the secular equation
    (spatial block by mp.eigsy)."""
    Mm = mp.matrix(4, 4)
    for a in range(4):
        for b in range(4):
            Mm[a, b] = (-That[a, b] if a == 0 else That[a, b])
    E, ER = mp.eig(Mm)
    ev = [E[i] for i in range(4)]
    scale = max(abs(mp.re(v)) for v in ev)
    real_ok = all(abs(mp.im(v)) < mpf('1e-30') * scale for v in ev)
    timelike = []
    for i in range(4):
        vec = [ER[j, i] for j in range(4)]
        nrm = (-abs(vec[0]) ** 2 + abs(vec[1]) ** 2
               + abs(vec[2]) ** 2 + abs(vec[3]) ** 2)
        timelike.append(nrm < mpf('-1e-6'))
    typeI = bool(real_ok and sum(timelike) == 1)
    res = {'typeI': typeI, 'evals': [mp.nstr(v, 25) for v in ev]}
    if typeI:
        k = timelike.index(True)
        rho = -mp.re(ev[k])
        ps = [mp.re(ev[i]) for i in range(4) if i != k]
        res['rho'] = mp.nstr(rho, 25)
        res['nec'] = mp.nstr(min(rho + p for p in ps), 25)
        res['wec'] = mp.nstr(min(rho, min(rho + p for p in ps)), 25)
        res['sec'] = mp.nstr(min(min(rho + p for p in ps),
                                 rho + sum(ps)), 25)
        res['dec'] = mp.nstr(min(rho, rho - max(abs(p) for p in ps)),
                             25)
    # exact worst null (secular; P symmetric -> eigsy)
    rho = That[0, 0]
    F = mp.matrix([That[0, 1], That[0, 2], That[0, 3]])
    P = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            P[i, j] = That[i + 1, j + 1]
    lam, Q = mp.eigsy(P)
    Fh = Q.T * F
    lam_min = lam[0]

    def gsec(l):
        return sum((Fh[i] / (lam[i] + l)) ** 2 for i in range(3))

    # the same branch structure as the gate's float64
    # secular solver, including the trust-region hard
    # case (F without a usable component in the
    # lam_min eigenspace: lambda* = -lam_min and the
    # minimiser fills that eigenspace to unit norm)
    scale = max(mpf(1), abs(lam_min))
    d0 = mpf('1e-9') * scale
    if gsec(-lam_min + d0) <= 1:
        lstar = -lam_min
        mh = mp.matrix(3, 1)
        for i in range(3):
            if lam[i] + lstar > mpf('1e-12') * scale:
                mh[i] = -Fh[i] / (lam[i] + lstar)
        m = Q * mh
        rem = 1 - sum(m[i] ** 2 for i in range(3))
        if rem > 0:
            m = m + mp.sqrt(rem) * mp.matrix(
                [Q[0, 0], Q[1, 0], Q[2, 0]])
    else:
        lo = -lam_min + d0
        hi = lo + 1
        while gsec(hi) > 1:
            hi = lo + 2 * (hi - lo)
        for _ in range(300):
            mid = (lo + hi) / 2
            if gsec(mid) > 1:
                lo = mid
            else:
                hi = mid
        lstar = (lo + hi) / 2
        mh = mp.matrix([-Fh[i] / (lam[i] + lstar)
                        for i in range(3)])
        m = Q * mh
    q = rho + 2 * sum(F[i] * m[i] for i in range(3)) \
        + sum(m[i] * P[i, j] * m[j]
              for i in range(3) for j in range(3))
    res['worst_null'] = mp.nstr(q, 25)
    res['worst_null_lambda'] = mp.nstr(lstar, 25)
    return res


def point_block(name, pt_list, prof_fn_mp, prof_fn_np):
    pt = [mpf(v) for v in pt_list]
    r = mp.sqrt(sum(v * v for v in pt))
    prof = prof_fn_mp(r)
    T, g, That = T_mp(pt, prof)
    mg = margins_mp(That)
    # float64 comparison at the same point
    T64, g64 = G.T_at(np.array([pt_list], dtype=G.DT), prof_fn_np)
    That64 = G.eulerian_that(g64, T64)
    m64 = G.margins(That64)
    q64, _m, _l = G.worst_null_exact(That64[0])
    blk = {'point': pt_list, 'r': mp.nstr(r, 25),
           'mp_margins': mg,
           'float64_margins': {
               'nec': float(m64['nec'][0]),
               'dec': float(m64['dec'][0]),
               'wec': float(m64['wec'][0]),
               'sec': float(m64['sec'][0]),
               'typeI': bool(m64['typeI'][0]),
               'worst_null': q64},
           'max_abs_T_diff_mp_vs_float64': float(max(
               abs(T[i, j] - mpf(float(T64[0][i, j])))
               for i in range(4) for j in range(4)))}
    out[name] = blk
    print(name, 'done', flush=True)


NUM = json.load(open(f'{WP}/gate50/results/g50_numbers.json'))
pt_win = NUM['claim_a_winner']['summary']['nec_argmin_point']
pt_base = NUM['CTL-A_base_winner']['summary']['nec_argmin_point']
point_block('winner405_argmin', pt_win, winner405_mp,
            G.prof_winner405)
point_block('base_winner_argmin', pt_base, winner_base_mp,
            G.prof_winner_base)

# ---------------- exact SS7 peak arithmetic
knot0 = mpf(float(G.SHAPEC_CRIT[0]))
beta_mp = mpf(G.BETA)
peak_exact = beta_mp * knot0
prof10 = h2_mp(mpf(10))
S_H2_10 = prof10[0]
bar_exact = beta_mp * S_H2_10 / 2
out['peak_arithmetic'] = {
    'winner_peak_exact': mp.nstr(peak_exact, 30),
    'S_H2_at_10_exact': mp.nstr(S_H2_10, 30),
    'bar_exact': mp.nstr(bar_exact, 30),
    'peak_minus_bar_exact': mp.nstr(peak_exact - bar_exact, 10),
    'bar_registered_float': G.SS7_BAR,
    'winner_peak_float': 0.44267424902674035}
print('peak arithmetic done', flush=True)

# ---------------- shape derivative scan (float64)
dense_r = np.linspace(10.0, 20.0, 200001)
_d, dSp, _dpp = G.corr(G.SHAPEC_CRIT, 9)(dense_r)
pos = dSp > 0.0
out['shape_derivative_scan'] = {
    'max_Sp': float(np.max(dSp)),
    'min_Sp': float(np.min(dSp)),
    'Sp_positive_intervals': [
        [float(dense_r[i]), float(dense_r[i + 1])]
        for i in np.where(np.diff(pos.astype(int)) != 0)[0][:8]],
    'Sp_at_10': float(dSp[0]),
    'Sp_at_20': float(dSp[-1]),
    'argmax_Sp_r': float(dense_r[int(np.argmax(dSp))])}
print('derivative scan done', flush=True)

json.dump(out, open(f'{WP}/gate50/results/g50_mp.json', 'w'),
          indent=1)
print('g50_mp complete')
