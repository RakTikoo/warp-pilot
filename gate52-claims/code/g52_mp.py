#!/usr/bin/env python3
"""
g52_mp.py -- Gate-52 named-point verification in 50-digit
mpmath. An independent arbitrary-precision path: profiles
rebuilt in mpmath (own moment solver), the metric's first
and second Cartesian derivatives by the analytic radial
(r, n) algebra, Gamma/Ricci by textbook loops, the
Eulerian frame by mpmath symmetric eigendecomposition,
margins from mpmath eigenvalues of the mixed tensor.
Points: the m2 winner's NEC argmin point; the m5 (K17)
winner's sampled-NEC argmin point (gate read's); the m5
(K17) Type-I NEC argmin point (gate read's).
Output: gate52/results/g52_mp.json.
"""
import json
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g52_lib as G   # noqa: E402

mp.mp.dps = 50
WP = os.environ.get('G52_WP', '/home/hatch/workspace/warp-pilot')
OUT = f'{WP}/gate52/results/g52_mp.json'
BETA = mp.mpf('1.1')


# ---------------- mpmath profile layer ----------------
def nak_moments_mp(xk, yk):
    n = len(xk)
    h = [xk[i + 1] - xk[i] for i in range(n - 1)]
    A = mp.zeros(n, n)
    b = mp.zeros(n, 1)
    A[0, 0] = -h[1]
    A[0, 1] = h[0] + h[1]
    A[0, 2] = -h[0]
    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        b[i] = 6 * ((yk[i + 1] - yk[i]) / h[i]
                    - (yk[i] - yk[i - 1]) / h[i - 1])
    A[n - 1, n - 3] = -h[n - 2]
    A[n - 1, n - 2] = h[n - 3] + h[n - 2]
    A[n - 1, n - 1] = -h[n - 3]
    sol = mp.lu_solve(A, b)
    return [sol[i] for i in range(n)]


def nak_eval_mp(xk, yk, M, r):
    rc = min(max(r, xk[0]), xk[-1])
    i = 0
    while i < len(xk) - 2 and rc >= xk[i + 1]:
        i += 1
    h = xk[i + 1] - xk[i]
    A_ = (xk[i + 1] - rc) / h
    B_ = (rc - xk[i]) / h
    d = (A_ * yk[i] + B_ * yk[i + 1]
         + ((A_ ** 3 - A_) * M[i] + (B_ ** 3 - B_) * M[i + 1])
         * h ** 2 / 6)
    dp = ((yk[i + 1] - yk[i]) / h
          + h / 6 * ((1 - 3 * A_ ** 2) * M[i]
                     + (3 * B_ ** 2 - 1) * M[i + 1]))
    dpp = A_ * M[i] + B_ * M[i + 1]
    if r < xk[0] or r > xk[-1]:
        dp = mp.mpf(0)
        dpp = mp.mpf(0)
    return d, dp, dpp


_SPL = {}


def corr_mp(vals, K):
    key = (K, tuple(float(v) for v in vals))
    if key not in _SPL:
        xk = [mp.mpf(10) + mp.mpf(10) * i / (K - 1)
              for i in range(K)]
        yk = [mp.mpf(float(v)) for v in vals]
        _SPL[key] = (xk, yk, nak_moments_mp(xk, yk))
    xk, yk, M = _SPL[key]
    return lambda r: nak_eval_mp(xk, yk, M, r)


def H_mp(t):
    if t <= 0:
        return mp.mpf(0), mp.mpf(0), mp.mpf(0)
    if t >= 1:
        return mp.mpf(1), mp.mpf(0), mp.mpf(0)
    return (10 * t ** 3 - 15 * t ** 4 + 6 * t ** 5,
            30 * t ** 2 * (1 - t) ** 2,
            60 * t * (1 - t) * (1 - 2 * t))


def plateau_mp(r, c=15.0, W=5.0, e=3.0):
    Ha, Hpa, Hppa = H_mp((r - (c - W)) / e)
    Hb, Hpb, Hppb = H_mp(((c + W) - r) / e)
    return (Ha * Hb, (Hpa * Hb - Ha * Hpb) / e,
            (Hppa * Hb - 2 * Hpa * Hpb + Ha * Hppb) / e ** 2)


def ramp_mp(r, a, b):
    if r >= b:
        return mp.mpf(1), mp.mpf(0), mp.mpf(0)
    if r <= a:
        return mp.mpf(0), mp.mpf(0), mp.mpf(0)
    x = (r - a) / (b - a)
    return (6 * x ** 5 - 15 * x ** 4 + 10 * x ** 3,
            (30 * x ** 4 - 60 * x ** 3 + 30 * x ** 2) / (b - a),
            (120 * x ** 3 - 180 * x ** 2 + 60 * x) / (b - a) ** 2)


def s_ab_mp(r):
    if r >= 20:
        return mp.mpf(0), mp.mpf(0), mp.mpf(0)
    if r <= 10:
        return mp.mpf(1), mp.mpf(0), mp.mpf(0)
    u = (r - 10) / 10
    w = 1 - u
    return (1 - (10 * u ** 3 * w ** 2 + 5 * u ** 4 * w + u ** 5),
            -3 * u ** 2 * w ** 2,
            -mp.mpf('0.6') * u * w * (1 - 2 * u))


def base_mp(r):
    S, Sp, Spp = s_ab_mp(r)
    S, Sp, Spp = (mp.mpf('0.7') * S, mp.mpf('0.7') * Sp,
                  mp.mpf('0.7') * Spp)
    B, Bp, Bpp = plateau_mp(r)
    A = mp.mpf('0.07439108177516472')
    N, Np, Npp = 1 + A * B, A * Bp, A * Bpp
    U1, U1p, U1pp = ramp_mp(r, mp.mpf('8.5'), mp.mpf(20))
    U2, U2p, U2pp = ramp_mp(r, mp.mpf(21), mp.mpf(24))
    M = 1 + 6 * (U1 - U2)
    Mp = 6 * (U1p - U2p)
    Mpp = 6 * (U1pp - U2pp)
    return [S, Sp, Spp, N, Np, Npp, M, Mp, Mpp]


def add_corr_mp(prof, vecs, K, r):
    out = []
    for i, key in enumerate(('vS', 'vN', 'vM')):
        d, dp, dpp = corr_mp(vecs[key], K)(r)
        out += [prof[3 * i] + d, prof[3 * i + 1] + dp,
                prof[3 * i + 2] + dpp]
    return out


def centre_mp(mu, prof):
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = prof
    return [mu * S, mu * Sp, mu * Spp, mu * N, mu * Np,
            mu * Npp, 1 + mu * (M - 1), mu * Mp, mu * Mpp]


def h2_mp(r):
    return add_corr_mp(
        centre_mp(mp.mpf('1.15'),
                  add_corr_mp(base_mp(r), G.A2, 33, r)),
        G.H2V, 17, r)


def config_mp(r, vS, K):
    h2 = h2_mp(r)
    muN = mp.mpf(float(G.WIN_MUN))
    muM = mp.mpf(float(G.WIN_MUM))
    N = muN * h2[3]
    Np = muN * h2[4]
    Npp = muN * h2[5]
    M = 1 + muM * (h2[6] - 1)
    Mp = muM * h2[7]
    Mpp = muM * h2[8]
    d, dp, dpp = corr_mp(G.WIN_VN, 17)(r)
    N, Np, Npp = N + d, Np + dp, Npp + dpp
    d, dp, dpp = corr_mp(G.WIN_VM, 17)(r)
    M, Mp, Mpp = M + d, Mp + dp, Mpp + dpp
    if vS is None:
        S = Sp = Spp = mp.mpf(0)
    else:
        S, Sp, Spp = corr_mp(vS, K)(r)
    return [S, Sp, Spp, N, Np, Npp, M, Mp, Mpp]


# ---------------- tensor at a point (analytic (r, n) algebra)
def that_mp(pt, vS, K):
    x = [mp.mpf(float(c)) for c in pt]
    r = mp.sqrt(sum(c * c for c in x))
    n = [c / r for c in x]
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = config_mp(r, vS, K)
    h = M - 1
    hp, hpp = Mp, Mpp
    v = BETA * S
    # metric and derivatives; indices: 0 = t, 1..3 = x, y, z
    g = mp.zeros(4, 4)
    g[0, 0] = -N * N
    g[0, 1] = g[1, 0] = -v
    for i in range(3):
        for j in range(3):
            g[1 + i, 1 + j] = (1 if i == j else 0) \
                + h * n[i] * n[j]
    Z = mp.mpf(0)
    dg = [[[Z] * 4 for _ in range(4)] for _ in range(4)]
    ddg = [[[[Z] * 4 for _ in range(4)] for _ in range(4)]
           for _ in range(4)]
    Pm = [[(1 if a == b else 0) - n[a] * n[b]
           for b in range(3)] for a in range(3)]
    for k in range(3):
        dg[k][0][0] = -2 * N * Np * n[k]
        dg[k][0][1] = dg[k][1][0] = -BETA * Sp * n[k]
        for i in range(3):
            for j in range(3):
                A = ((1 if k == i else 0) * n[j]
                     + (1 if k == j else 0) * n[i]
                     - 2 * n[k] * n[i] * n[j])
                dg[k][1 + i][1 + j] = hp * n[k] * n[i] * n[j] \
                    + (h / r) * A
                for l in range(3):
                    dA = (Pm[l][j] * (1 if k == i else 0)
                          + Pm[l][i] * (1 if k == j else 0)
                          - 2 * (Pm[l][k] * n[i] * n[j]
                                 + n[k] * Pm[l][i] * n[j]
                                 + n[k] * n[i] * Pm[l][j])) / r
                    ddg[l][k][1 + i][1 + j] = (
                        hpp * n[l] * n[k] * n[i] * n[j]
                        + (hp / r) * (Pm[l][k] * n[i] * n[j]
                                      + n[k] * Pm[l][i] * n[j]
                                      + n[k] * n[i] * Pm[l][j])
                        + (n[l] * (hp / r - h / r ** 2)) * A
                        + (h / r) * dA)
        for l in range(3):
            ddg[l][k][0][0] = (
                -2 * (Np ** 2 + N * Npp) * n[l] * n[k]
                - 2 * N * (Np / r) * ((1 if l == k else 0)
                                      - n[l] * n[k]))
            ddg[l][k][0][1] = ddg[l][k][1][0] = -BETA * (
                Spp * n[l] * n[k]
                + (Sp / r) * ((1 if l == k else 0)
                              - n[l] * n[k]))
    # full dg4[mu, a, b] with time derivatives zero
    dg4 = [[[Z] * 4 for _ in range(4)] for _ in range(4)]
    ddg4 = [[[[Z] * 4 for _ in range(4)] for _ in range(4)]
            for _ in range(4)]
    for k in range(3):
        for a in range(4):
            for b in range(4):
                dg4[k + 1][a][b] = dg[k][a][b]
                for l in range(3):
                    ddg4[l + 1][k + 1][a][b] = ddg[l][k][a][b]
    ginv = mp.inverse(g)
    Gam = [[[Z] * 4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam[a][b][c] = mp.mpf('0.5') * sum(
                    ginv[a, d] * (dg4[b][d][c] + dg4[c][d][b]
                                  - dg4[d][b][c])
                    for d in range(4))
    dginv = [[[Z] * 4 for _ in range(4)] for _ in range(4)]
    for e in range(4):
        for a in range(4):
            for b in range(4):
                dginv[e][a][b] = -sum(
                    ginv[a, m] * dg4[e][m][nn] * ginv[nn, b]
                    for m in range(4) for nn in range(4))
    dGam = [[[[Z] * 4 for _ in range(4)] for _ in range(4)]
            for _ in range(4)]
    for e in range(4):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = sum(ginv[a, d] * (
                        ddg4[e][b][d][c] + ddg4[e][c][d][b]
                        - ddg4[e][d][b][c]) for d in range(4))
                    t2 = sum(dginv[e][a][d] * (
                        dg4[b][d][c] + dg4[c][d][b]
                        - dg4[d][b][c]) for d in range(4))
                    dGam[e][a][b][c] = mp.mpf('0.5') * (t1 + t2)
    Ric = mp.zeros(4, 4)
    for b in range(4):
        for d in range(4):
            val = mp.mpf(0)
            for a in range(4):
                val += dGam[a][a][b][d] - dGam[d][a][b][a]
                for e in range(4):
                    val += Gam[a][a][e] * Gam[e][b][d] \
                        - Gam[a][d][e] * Gam[e][b][a]
            Ric[b, d] = val
    Rs = sum(ginv[a, b] * Ric[a, b]
             for a in range(4) for b in range(4))
    T = mp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            T[a, b] = (Ric[a, b] - mp.mpf('0.5') * Rs * g[a, b]) \
                / (8 * mp.pi)
    # Eulerian frame
    gam = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            gam[i, j] = (1 if i == j else 0) + h * n[i] * n[j]
    gam_inv = mp.inverse(gam)
    bcov = [g[0, 1 + i] for i in range(3)]
    bup = [sum(gam_inv[i, j] * bcov[j] for j in range(3))
           for i in range(3)]
    alpha2 = -g[0, 0] + sum(bcov[i] * bup[i] for i in range(3))
    alpha = mp.sqrt(alpha2)
    evals, V = mp.eigsy(gam)
    E = mp.zeros(4, 4)
    E[0, 0] = 1 / alpha
    for i in range(3):
        E[1 + i, 0] = -bup[i] / alpha
        for j in range(3):
            E[1 + j, 1 + i] = V[j, i] / mp.sqrt(evals[i])
    That = mp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            That[a, b] = sum(E[m, a] * E[nn, b] * T[m, nn]
                             for m in range(4) for nn in range(4))
    That = (That + That.T) / 2
    return That


def margins_mp(That):
    """Eigenvalue margins (Type-I test as registered)."""
    Mx = mp.matrix(4, 4)
    for a in range(4):
        for b in range(4):
            Mx[a, b] = -That[a, b] if a == 0 else That[a, b]
    ev, ER = mp.eig(Mx)
    scale = max(abs(mp.re(e)) for e in ev)
    real_ok = all(abs(mp.im(e)) < mp.mpf('1e-8') * scale
                  for e in ev)
    cand = []
    for k in range(4):
        vec = [ER[i, k] for i in range(4)]
        nrm = -abs(vec[0]) ** 2 + sum(abs(vec[i]) ** 2
                                      for i in range(1, 4))
        if nrm < mp.mpf('-1e-6'):
            cand.append(k)
    typeI = bool(real_ok and len(cand) == 1)
    if not typeI:
        return {'typeI': False}
    k = cand[0]
    rho = -mp.re(ev[k])
    ps = [mp.re(ev[j]) for j in range(4) if j != k]
    nec = min(rho + p for p in ps)
    return {'typeI': True, 'rho': rho, 'nec': nec,
            'wec': min(rho, nec),
            'sec': min(nec, rho + sum(ps)),
            'dec': min(rho, rho - max(abs(p) for p in ps))}


def transfer_u(pt, vS, K, u_gate):
    """The gate's certified minimiser direction, re-expressed
    in this path's own eigh basis. u_gate holds components in
    the gate's gamma-eigh frame; the physical direction is
    d = sum_i u_i w_i (Cartesian). Its components in the
    mpmath eigh basis follow from gamma-inner products.
    (The tangential eigh basis is arbitrary within the
    exactly degenerate eigenvalue-1 plane, so raw components
    are NOT comparable across paths; the direction is.)"""
    pt = np.asarray(pt, dtype=G.DT)
    r = float(np.linalg.norm(pt))
    prof = G.config_profiles(np.array([r]), vS, K)
    gam64 = np.eye(3) + (prof[6][0] - 1.0) * np.outer(
        pt / r, pt / r)
    lam, V = np.linalg.eigh(gam64)
    w = V / np.sqrt(lam)[None, :]
    d = w @ np.asarray(u_gate, dtype=G.DT)
    pm = config_mp(mp.mpf(r), vS, K)
    n_mp = [mp.mpf(float(c)) for c in (pt / r)]
    gam = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            gam[i, j] = (1 if i == j else 0) \
                + (pm[6] - 1) * n_mp[i] * n_mp[j]
    ev, Vmp = mp.eigsy(gam)
    up = []
    for i in range(3):
        wi = [Vmp[j, i] / mp.sqrt(ev[i]) for j in range(3)]
        up.append(sum(wi[a] * gam[a, b] * mp.mpf(float(d[b]))
                      for a in range(3) for b in range(3)))
    nrm = mp.sqrt(sum(c * c for c in up))
    return [c / nrm for c in up]


def worst_null_mp(That, pt, vS, K, u_gate):
    """The worst-null of the mpmath tensor: q at the
    transferred gate direction, a fib(642) scan, and a
    pattern-search polish of the minimum in mpmath."""
    def q(u):
        k = [mp.mpf(1)] + [
            c if isinstance(c, mp.mpf) else mp.mpf(float(c))
            for c in u]
        return sum(k[a] * k[b] * That[a, b]
                   for a in range(4) for b in range(4))

    up = transfer_u(pt, vS, K, u_gate)
    q_at_gate_u = q(up)
    scan = min(q(dvec) for dvec in G.fib_dirs(642))
    # pattern search on the sphere from the transferred u
    u = list(up)
    best = q_at_gate_u
    step = mp.mpf('0.05')
    while step > mp.mpf('1e-9'):
        improved = False
        for i in range(3):
            for s in (1, -1):
                v = list(u)
                v[i] += s * step
                nrm = mp.sqrt(sum(c * c for c in v))
                v = [c / nrm for c in v]
                val = q(v)
                if val < best:
                    best, u, improved = val, v, True
        if not improved:
            step /= 5
    return {'mp_polished_min': best, 'q_at_gate_u': q_at_gate_u,
            'scan642_min': scan}


def main():
    nums = json.load(open(f'{WP}/gate52/results/g52_numbers.json'))
    pol = json.load(open(f'{WP}/gate52/results/g52_polish.json'))
    out = {}
    jobs = [
        ('m2_argmin', G.M2_VS, 9,
         nums['claim_a_m2']['set']['nec_argmin_point'],
         nums['claim_a_m2']['set'],
         nums['claim_a_m2']['worst_null_at_argmin']),
        ('m5k17_sampled_argmin', G.M5K17_VS, 17,
         nums['claim_b_m5']['K17']['set']['nec_argmin_point'],
         nums['claim_b_m5']['K17']['set'],
         nums['claim_b_m5']['K17']['worst_null_at_nec_argmin']),
        ('m5k17_typeI_argmin', G.M5K17_VS, 17,
         pol['claim_b_supplements']['K17']['typeI_nec_argmin']
         ['point'],
         None,
         None),
    ]
    for tag, vs, K, pt, setrec, wnrec in jobs:
        That = that_mp(pt, vs, K)
        mm = margins_mp(That)
        # float64 gate reads at the same point: pointwise
        # margins and the spatial block's eigenvalues (the
        # basis-invariant content; raw That components are
        # NOT comparable across eigh bases -- the tangential
        # eigenspace of gamma is exactly degenerate)
        pta = np.array(pt, dtype=G.DT)
        _, _, Tg = G.nec_at_point(vs, K, pta)
        mg = G.hawking_ellis_margins(Tg)
        eig_g = np.sort(np.linalg.eigvalsh(Tg[1:, 1:]))
        eig_m = sorted(float(x) for x in
                       mp.eigsy(mp.matrix(That[1:, 1:]))[0])
        rec = {'point': pt,
               'margins_mp': {
                   k: (float(v) if not isinstance(v, bool)
                       else v) for k, v in mm.items()},
               'margins_gate_pointwise': {
                   'nec': float(mg['nec'][0]),
                   'wec': float(mg['wec'][0]),
                   'sec': float(mg['sec'][0]),
                   'dec': float(mg['dec'][0]),
                   'typeI': bool(mg['typeI'][0])},
               'spatial_block_eig_max_diff': float(np.max(
                   np.abs(eig_g - np.array(eig_m))))}
        if mm.get('typeI'):
            rec['margin_diffs_mp_minus_gate'] = {
                k: float(mm[k]) - float(mg[k][0])
                for k in ('nec', 'wec', 'sec', 'dec')}
        if wnrec is not None:
            wn = worst_null_mp(That, pt, vs, K, wnrec['u'])
            rec['worst_null'] = {
                'gate_certified': wnrec['worst_null'],
                'mp_polished_min': float(wn['mp_polished_min']),
                'mp_q_at_transferred_gate_u':
                float(wn['q_at_gate_u']),
                'mp_scan642_min': float(wn['scan642_min']),
                'mp_polished_minus_gate': float(
                    wn['mp_polished_min'] - wnrec['worst_null'])}
        if setrec is not None:
            rec['nec_gate_set_value'] = setrec['nec']['min']
        out[tag] = rec
        print(tag, 'done', flush=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=1)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
