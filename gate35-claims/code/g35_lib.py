#!/usr/bin/env python3
"""
g35_lib.py -- Gate-35 Item 2 INDEPENDENT assembly for the
three-function class. Deliberately different in kind from
p312_lib/p314_lib (which are NOT imported here):

  * The metric is built in spherical coordinates
    (t, r, theta, phi) with the polar axis along the shift
    direction x-hat. The pose defines the shift COVECTOR
    (Cartesian beta_i = (-beta*S, 0, 0), g_tt = -N^2);
    pulling -beta*S dx back with x = r cos th gives
        gamma = M dr^2 + r^2 dOmega^2,
        g_tt = -N^2, g_tr = -beta*S*cos th,
        g_tth = +r beta*S*sin th.
    (First version of this file wrongly used the
    contravariant shift in g_ti and an ADM g_tt; C-G2 caught
    it and it was corrected. A second defect -- the spherical
    -> Cartesian transform applied as J T J^T instead of
    J^{-T} T J^{-1} -- was caught by the split cross-check
    failing at the binding sites while the split itself
    matched the stored record; also corrected. See memo.)
  * The Einstein tensor is computed SYMBOLICALLY with sympy
    from that line element (S, N, M left as undefined
    functions of r; the inverse metric is supplied in its
    analytic ADM form and verified against g symbolically),
    T_req = G/(8 pi), then lambdified.
  * T_req is transformed spherical -> Cartesian with the
    pointwise Jacobian, and the Eulerian orthonormal frame
    is applied via verify_metric.eulerian_that (permitted
    frame utility) on the Cartesian metric built directly
    from its definition (g_tt=-N^2, g_tX=-beta*S,
    gamma_ij = delta_ij + (M-1) n_i n_j).

Permitted programme imports ONLY: p258_lib (S_ab shape,
R_NODES, DIRS162 grid), p274_lib (winner lapse shape),
verify_metric (frame), p2352_run (SAMPLER-M margins).
The M(r) profiles and the Phase-308 split cross-check are
implemented here from the printed definitions.
float64 throughout.
"""
import sys

import numpy as np
import sympy as sp
from scipy.optimize import minimize

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase235/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase258/work')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase274/work')
import verify_metric as vm  # noqa: E402
from p2352_run import margins_chunked  # noqa: E402
from p258_lib import S_ab, R_NODES, DIRS162  # noqa: E402
import p274_lib as L274  # noqa: E402

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi
BETA = 1.1
WINNER_SPEC = {'shape': 'plat', 'a': 2, 'b': 2,
               'A': 0.07439108177516472, 'c': 15, 'W': 5, 'e': 3.0}
SET_PTS = np.vstack([DIRS162 * rr for rr in R_NODES])
SET_R = np.linalg.norm(SET_PTS, axis=1)


# ------------------------------------------------------------ M(r)
def _ss(x):
    """Quintic smoothstep SS and first two derivatives."""
    return (6.0 * x**5 - 15.0 * x**4 + 10.0 * x**3,
            30.0 * x**4 - 60.0 * x**3 + 30.0 * x**2,
            120.0 * x**3 - 180.0 * x**2 + 60.0 * x)


def _U(r, a, b):
    """U(r;a,b) = SS((r-a)/(b-a)) on [a,b], 0 below, 1 above.
    Returns (U, U', U'')."""
    r = np.asarray(r, dtype=DTYPE)
    U = np.where(r >= b, 1.0, 0.0)
    Up = np.zeros_like(r); Upp = np.zeros_like(r)
    mid = (r > a) & (r < b)
    if np.any(mid):
        x = (r[mid] - a) / (b - a)
        v, vp, vpp = _ss(x)
        U = np.where(mid, v, U)
        Up[mid] = vp / (b - a); Upp[mid] = vpp / (b - a) ** 2
    return U, Up, Upp


def M_funcs(r, mode):
    """(M, M', M'') for mode 'one' (M == 1) or 'headline'
    (ramp: 1 + 4.00*[U(r;9,20.5) - U(r;21,24)])."""
    r = np.asarray(r, dtype=DTYPE)
    if mode == 'one':
        return np.ones_like(r), np.zeros_like(r), np.zeros_like(r)
    if mode == 'headline':
        U1, U1p, U1pp = _U(r, 9.0, 20.5)
        U2, U2p, U2pp = _U(r, 21.0, 24.0)
        return (1.0 + 4.0 * (U1 - U2), 4.0 * (U1p - U2p),
                4.0 * (U1pp - U2pp))
    raise ValueError(mode)


def profiles(r, mode):
    """(S,Sp,Spp,N,Np,Npp,M,Mp,Mpp) at radii r (winner (S,N))."""
    r = np.asarray(r, dtype=DTYPE)
    S, Sp, Spp = S_ab(r, WINNER_SPEC['a'], WINNER_SPEC['b'])
    N, Np, Npp = L274.lapse_funcs_p(WINNER_SPEC, r)
    M, Mp, Mpp = M_funcs(r, mode)
    return S, Sp, Spp, N, Np, Npp, M, Mp, Mpp


# --------------------------------------- symbolic Einstein tensor
def _build_G_funcs():
    """Sympy Einstein tensor of the spherical line element,
    lambdified. Returns dict {(a,b): f(r, th, beta, S,Sp,Spp,
    N,Np,Npp, M,Mp,Mpp)} for the 7 nonzero components."""
    r, th = sp.symbols('r theta')
    beta = sp.symbols('beta')
    Sf = sp.Function('S')(r); Nf = sp.Function('N')(r)
    Mf = sp.Function('M')(r)
    c, s = sp.cos(th), sp.sin(th)
    g = sp.zeros(4, 4)
    g[0, 0] = -Nf**2
    g[0, 1] = g[1, 0] = -beta * Sf * c
    g[0, 2] = g[2, 0] = r * beta * Sf * s
    g[1, 1] = Mf; g[2, 2] = r**2; g[3, 3] = r**2 * s**2
    # analytic inverse: alpha^2 = N^2 + gamma^{ij} beta_i beta_j
    # = N^2 + beta^2 S^2 (cos^2/M + sin^2); shift vector
    # beta^r = -beta*S*cos/M, beta^th = +beta*S*sin/r.
    al2 = Nf**2 + beta**2 * Sf**2 * (c**2 / Mf + s**2)
    gi = sp.zeros(4, 4)
    br, bt = -beta * Sf * c / Mf, beta * Sf * s / r
    gi[0, 0] = -1 / al2
    gi[0, 1] = gi[1, 0] = br / al2
    gi[0, 2] = gi[2, 0] = bt / al2
    gi[1, 1] = 1 / Mf - br**2 / al2
    gi[2, 2] = 1 / r**2 - bt**2 / al2
    gi[1, 2] = gi[2, 1] = -br * bt / al2
    gi[3, 3] = 1 / (r**2 * s**2)
    assert sp.simplify(g * gi - sp.eye(4)) == sp.zeros(4, 4)
    coords = [None, r, th, None]
    dg = {}
    for mu in (1, 2):
        for a in range(4):
            for b in range(4):
                dg[(mu, a, b)] = sp.diff(g[a, b], coords[mu])

    def DG(mu, a, b):
        return dg.get((mu, a, b), sp.Integer(0))

    Gam = {}
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                e = 0
                for q in range(4):
                    e += gi[mu, q] * (DG(a, q, b) + DG(b, q, a)
                                      - DG(q, a, b))
                Gam[(mu, a, b)] = e / 2
    dG = {}
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                for cc in (1, 2):
                    dG[(cc, mu, a, b)] = sp.diff(Gam[(mu, a, b)],
                                                 coords[cc])
    Ric = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            e = 0
            for mu in range(4):
                e += dG.get((mu, mu, b, a), 0)
                if b in (1, 2):
                    e -= dG[(b, mu, mu, a)]
                for q in range(4):
                    e += (Gam[(mu, mu, q)] * Gam[(q, b, a)]
                          - Gam[(mu, b, q)] * Gam[(q, mu, a)])
            Ric[a, b] = e
    Rs = sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4))
    G = Ric - Rs * g / 2
    subs = {}
    for nm, f in (('S', Sf), ('N', Nf), ('M', Mf)):
        subs[sp.Derivative(f, (r, 2))] = sp.Symbol(nm + 'pp')
        subs[sp.Derivative(f, r)] = sp.Symbol(nm + 'p')
        subs[f] = sp.Symbol(nm)
    arglist = [r, th, beta] + [subs[k] for k in (
        Sf, sp.Derivative(Sf, r), sp.Derivative(Sf, (r, 2)),
        Nf, sp.Derivative(Nf, r), sp.Derivative(Nf, (r, 2)),
        Mf, sp.Derivative(Mf, r), sp.Derivative(Mf, (r, 2)))]
    out = {}
    for (a, b) in [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2),
                   (2, 2), (3, 3)]:
        out[(a, b)] = sp.lambdify(arglist, G[a, b].subs(subs),
                                  modules='numpy', cse=True)
    return out


_GF = None


def _G_funcs():
    global _GF
    if _GF is None:
        _GF = _build_G_funcs()
    return _GF


# ------------------------------------------------------- assembly
def T_and_g_cart(pts, mode):
    """(T_cov, g) Cartesian at pts from the symbolic spherical
    Einstein tensor. T_req = G/(8 pi)."""
    pts = np.asarray(pts, dtype=DTYPE)
    P = len(pts)
    r = np.linalg.norm(pts, axis=1)
    n = pts / r[:, None]
    th = np.arccos(np.clip(n[:, 0], -1.0, 1.0))
    ph = np.arctan2(n[:, 2], n[:, 1])
    prof = profiles(r, mode)
    gf = _G_funcs()
    args = [r, th, np.full(P, BETA)] + [np.full(P, v) if np.ndim(v) == 0
                                        else v for v in prof]
    Ts = np.zeros((P, 4, 4), dtype=DTYPE)
    for (a, b), f in gf.items():
        val = np.broadcast_to(np.asarray(f(*args), dtype=DTYPE),
                              (P,)) / EIGHT_PI
        Ts[:, a, b] = val
        Ts[:, b, a] = val
    # Jacobian J^a_mu = dx^a/dy^mu, y=(t,r,th,ph), x=(t,x,y,z),
    # x = r cos th, y = r sin th cos ph, z = r sin th sin ph
    st, ct = np.sin(th), np.cos(th)
    sph_, cph = np.sin(ph), np.cos(ph)
    eth = np.stack([-st, ct * cph, ct * sph_], axis=1)
    eph = np.stack([np.zeros(P), -sph_, cph], axis=1)
    J = np.zeros((P, 4, 4), dtype=DTYPE)
    J[:, 0, 0] = 1.0
    J[:, 1:, 1] = n
    J[:, 1:, 2] = r[:, None] * eth
    J[:, 1:, 3] = (r * st)[:, None] * eph
    # T_cart = J^{-T} T_sph J^{-1}  (T_sph = J^T T_cart J)
    Ji = np.linalg.inv(J)
    T = np.einsum('pia,pij,pjb->pab', Ji, Ts, Ji)
    T = 0.5 * (T + np.swapaxes(T, -1, -2))
    # Cartesian metric from its definition
    S = prof[0]; M = prof[6]
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -prof[3] ** 2
    g[:, 0, 1] = g[:, 1, 0] = -BETA * S
    h = M - 1.0
    g[:, 1:, 1:] = (np.eye(3)[None, :, :]
                    + h[:, None, None] * n[:, :, None] * n[:, None, :])
    return T, g


def That_at(pts, mode):
    T, g = T_and_g_cart(pts, mode)
    return vm.eulerian_that(g, T)


def set_read(mode):
    """SET-244 read: SAMPLER-M margins + Hawking-Ellis Type-I."""
    That = That_at(SET_PTS, mode)
    m = margins_chunked(That)
    mh = vm.hawking_ellis_margins(That, do_fallback=False)

    def st(a):
        return {'min': float(np.min(a)), 'median': float(np.median(a)),
                'max': float(np.max(a))}
    rho = That[:, 0, 0]
    ia = int(np.argmin(rho))
    return {
        'n_points': int(len(rho)), 'typeI_count': int(np.sum(mh['typeI'])),
        'nec': st(m['nec']), 'wec': st(m['wec']), 'dec': st(m['dec']),
        'sec': st(m['sec']), 'rho': st(rho),
        'rho_argmin': {'index': ia, 'point': SET_PTS[ia].tolist(),
                       'r': float(SET_R[ia]),
                       'direction': (SET_PTS[ia] / SET_R[ia]).tolist(),
                       'n_xhat': float(SET_PTS[ia][0] / SET_R[ia])},
    }, {'That': That, 'margins': m, 'typeI': mh['typeI'],
        'nec': m['nec'], 'rho': rho}


# ------------------------------------------- split cross-check
def rho_split(pts, mode):
    """Phase 308 split implemented fresh from CHECKPOINT308's
    printed formula: 16 pi rho = R + Q_K. Returns dict of
    rho_split and pieces (all divided by 16 pi where named)."""
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.linalg.norm(pts, axis=1)
    u = (pts[:, 0] / r) ** 2
    S, Sp, Spp, N, Np, Npp, M, Mp, Mpp = profiles(r, mode)
    R1 = (2.0 / r**2) * (1.0 - 1.0 / M)
    R2 = 2.0 * Mp / (r * M**2)
    alpha2 = N**2 + BETA**2 * S**2 * (1.0 - ((M - 1.0) / M) * u)
    QK = (BETA**2 / alpha2) * (
        -Sp**2 * (1.0 - u) / (2.0 * M)
        - 4.0 * (M - 1.0) * S * Sp * u / (r * M**2)
        + 2.0 * (M - 1.0)**2 * S**2 * u / (r**2 * M**2)
        + 2.0 * (M - 1.0) * Mp * S**2 * u / (r * M**3))
    d = 16.0 * np.pi
    return {'rho_split': (R1 + R2 + QK) / d, 'R1_over_16pi': R1 / d,
            'R2_over_16pi': R2 / d, 'R_over_16pi': (R1 + R2) / d,
            'QK_over_16pi': QK / d, 'M': M, 'Mp': Mp}


# ------------------------------------------------------- protocol
def _fib_dirs(npts):
    i = np.arange(npts, dtype=DTYPE)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / npts)
    theta = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(phi)], axis=1)


DIRS642 = _fib_dirs(642)


def worst_null(That, fib=642):
    """My own exact pointwise NEC minimum: Fibonacci-sphere
    null-direction scan of That(k,k), k=(1,n), + Nelder-Mead
    polish. Returns (n_best, nec_exact, nec_fib_scan)."""
    dirs = DIRS642 if fib == 642 else _fib_dirs(fib)
    K = np.concatenate([np.ones((len(dirs), 1)), dirs], axis=1)
    vals = np.einsum('ni,ij,nj->n', K, That, K)
    n0 = dirs[int(np.argmin(vals))]

    def obj(x):
        t_, p_ = x
        nn = np.array([np.sin(t_) * np.cos(p_), np.sin(t_) * np.sin(p_),
                       np.cos(t_)])
        k = np.concatenate([[1.0], nn])
        return float(k @ That @ k)

    x0 = np.array([np.arccos(np.clip(n0[2], -1, 1)),
                   np.arctan2(n0[1], n0[0])])
    res = minimize(obj, x0, method='Nelder-Mead',
                   options={'maxiter': 400, 'xatol': 1e-10,
                            'fatol': 1e-14})
    return float(res.fun), float(np.min(vals)), fib


def nec_at_point(pt, mode):
    """(SAMPLER-M NEC, Type-I, That) at one Cartesian point."""
    That = That_at(np.asarray(pt, dtype=DTYPE)[None, :], mode)
    m = margins_chunked(That)
    mh = vm.hawking_ellis_margins(That, do_fallback=False)
    return float(m['nec'][0]), bool(mh['typeI'][0]), That[0]


def adversary_polish(mode, aux):
    """My own adversary polish in the registered protocol form:
    Nelder-Mead minimisation of SAMPLER-M NEC over (r, th, ph),
    seeded from the 5 worst Type-I SET points; objective = NEC
    at Type-I points, NEC + 1 otherwise, 1.0 outside [10, 20]."""
    ti = aux['typeI']; nec = aux['nec']
    ti_idx = np.where(ti)[0]
    if len(ti_idx) == 0:
        return None
    pts_ti = SET_PTS[ti_idx]; nec_ti = nec[ti_idx]

    def objective(x):
        rr, t_, p_ = x
        if rr < 10.0 or rr > 20.0:
            return 1.0
        pt = rr * np.array([np.sin(t_) * np.cos(p_),
                            np.sin(t_) * np.sin(p_), np.cos(t_)])
        v, is_ti, _ = nec_at_point(pt, mode)
        return v if is_ti else v + 1.0

    order = np.argsort(nec_ti)[:5]
    polished = []
    for i in order:
        p0 = pts_ti[i]; r0 = float(np.linalg.norm(p0))
        x0 = np.array([r0, np.arccos(np.clip(p0[2] / r0, -1, 1)),
                       np.arctan2(p0[1], p0[0])])
        res = minimize(objective, x0, method='Nelder-Mead',
                       options={'maxiter': 300, 'xatol': 1e-4,
                                'fatol': 1e-7})
        rr, t_, p_ = res.x
        pt = rr * np.array([np.sin(t_) * np.cos(p_),
                            np.sin(t_) * np.sin(p_), np.cos(t_)])
        v, is_ti, _ = nec_at_point(pt, mode)
        polished.append({'point': pt, 'nec': v, 'typeI': is_ti})
    cand = [p for p in polished if p['typeI']]
    if cand:
        best = min(cand, key=lambda p: p['nec'])
        site_pt, source = best['point'], 'polished'
    else:
        site_pt = pts_ti[order[0]]; source = 'set_argmin_fallback'
    v, is_ti, That = nec_at_point(site_pt, mode)
    return {'source': source, 'point': site_pt.tolist(),
            'r': float(np.linalg.norm(site_pt)), 'typeI': is_ti,
            'in_region_worst_nec_SAMPLER-M': v,
            'rho_t': float(That[0, 0])}


def pick_sites(aux, polish):
    """Phase 293 site rule, my implementation (form as in
    p314_common.pick_sites, which I read)."""
    nec = aux['nec']; ti = aux['typeI']
    sites = {}
    if polish is not None:
        sites['S1'] = np.array(polish['point'], dtype=DTYPE)
        depth = polish['in_region_worst_nec_SAMPLER-M']
    else:
        i0 = int(np.argmin(nec)); sites['S1'] = SET_PTS[i0]
        depth = float(nec[i0])
    order_all = np.argsort(nec)
    sites['S2'] = SET_PTS[order_all[0]]
    used = [sites['S1'], sites['S2']]
    ti_idx = np.where(ti)[0]
    s3 = None
    if len(ti_idx):
        for i in ti_idx[np.argsort(nec[ti_idx])]:
            if not any(np.array_equal(SET_PTS[i], u) for u in used):
                s3 = SET_PTS[i]; break
        if s3 is None:
            s3 = SET_PTS[ti_idx[np.argsort(nec[ti_idx])][0]]
    if s3 is not None:
        sites['S3'] = s3; used.append(s3)
    far_idx = np.where(SET_R >= 15.0)[0]
    s4 = None
    for i in far_idx[np.argsort(nec[far_idx])]:
        if not any(np.array_equal(SET_PTS[i], u) for u in used):
            s4 = SET_PTS[i]; break
    if s4 is None:
        s4 = SET_PTS[far_idx[np.argsort(nec[far_idx])][0]]
    sites['S4'] = s4
    return sites, float(depth)


def site_record(mode, key, pt):
    pt = np.asarray(pt, dtype=DTYPE)
    That = That_at(pt[None, :], mode)[0]
    m = margins_chunked(That[None, :, :])
    mh = vm.hawking_ellis_margins(That[None, :, :], do_fallback=False)
    nec_exact, nec_fib, fib = worst_null(That)
    sp_ = rho_split(pt[None, :], mode)
    r = float(np.linalg.norm(pt))
    return {'key': key, 'point': pt.tolist(), 'r': r,
            'direction': (pt / r).tolist(), 'n_xhat': float(pt[0] / r),
            'typeI': bool(mh['typeI'][0]),
            'rho_req_tensor': float(That[0, 0]),
            'rho_req_split': float(sp_['rho_split'][0]),
            'split_rel_diff': float(abs(sp_['rho_split'][0] - That[0, 0])
                                    / max(abs(That[0, 0]), 1e-300)),
            'R1_over_16pi': float(sp_['R1_over_16pi'][0]),
            'R2_over_16pi': float(sp_['R2_over_16pi'][0]),
            'QK_over_16pi': float(sp_['QK_over_16pi'][0]),
            'nec_SAMPLER-M': float(m['nec'][0]),
            'nec_exact_pointwise': nec_exact,
            'nec_fib_scan': nec_fib, 'fib_count': fib}
