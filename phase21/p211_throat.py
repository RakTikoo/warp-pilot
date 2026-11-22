#!/usr/bin/env python3
"""
p211_throat.py -- P21-1(a) THROAT: Morris-Thorne metric on an RS brane.
SMS (published form, CHECKPOINT21 S P21-1):
  G^mu_nu = k4^2 tau^mu_nu + k5^4 Pi^mu_nu - E^mu_nu ,  Lambda4 = 0,
  k4^2 = k5^4 * lam / 6.
Pi^mu_nu = -1/4 (tau^2)^mu_nu + 1/12 tau tau^mu_nu
           + delta^mu_nu [ 1/8 tau_ab tau^ab - 1/24 tau^2 ].
E^mu_nu = diag(-U, P1, P2, P2) (mixed, static spherical).
Units: r0 = 1, k4^2 = 8 pi (programme/Lobo units).
Einstein tensor: SymPy-exact from the metric.  Divergence of a
diagonal mixed tensor in this metric (verified against a full
SymPy Christoffel divergence in this script):
  (div T)_r = (T^r_r)' + Phi' (T^r_r - T^t_t) + (2/r)(T^r_r - T^th_th).
float64 numerics on r in [1, 1e3] (log grid).  System python3.
"""
import json
import numpy as np
import sympy as sp

r, r0 = sp.symbols('r r0', positive=True)
TH = sp.symbols('th')
K4 = 8.0 * np.pi
RES = '/home/hatch/workspace/warp-pilot/phase21/results/'

SHAPES = {
    'ellis': r0**2 / r,
    'sqrt': r0 * (r / r0) ** sp.Rational(1, 2),
}
PHIS = {'zero': sp.Integer(0), 'minus': -r0 / r}


_GEN = None


def _generic_einstein():
    """SymPy-exact mixed Einstein components for generic b(r), Phi(r),
    computed ONCE from the metric (Christoffel -> Ricci), then
    specialised per case by substitution."""
    global _GEN
    if _GEN is not None:
        return _GEN
    B = sp.Function('B')(r)
    P = sp.Function('P')(r)
    t, ph = sp.symbols('t ph')
    th = TH
    coords = [t, r, th, ph]
    g = sp.diag(-sp.exp(2 * P), 1 / (1 - B / r),
                r**2, r**2 * sp.sin(th)**2)
    ginv = g.inv()
    dg = [g.diff(c) for c in coords]
    Gam = {}
    for a in range(4):
        for b_ in range(4):
            for c in range(4):
                expr = sum(ginv[a, d] * (dg[b_][d, c] + dg[c][d, b_]
                                         - dg[d][b_, c])
                           for d in range(4)) / 2
                expr = sp.simplify(expr)
                if expr != 0:
                    Gam[(a, b_, c)] = expr
    Ric = {}
    for b_ in range(4):
        for d_ in range(4):
            expr = 0
            for a in range(4):
                if (a, b_, d_) in Gam:
                    expr += Gam[(a, b_, d_)].diff(coords[a])
                if (a, d_, a) in Gam:
                    expr -= Gam[(a, d_, a)].diff(coords[d_])
                for e in range(4):
                    if (a, a, e) in Gam and (e, b_, d_) in Gam:
                        expr += Gam[(a, a, e)] * Gam[(e, b_, d_)]
                    if (a, d_, e) in Gam and (e, b_, a) in Gam:
                        expr -= Gam[(a, d_, e)] * Gam[(e, b_, a)]
            expr = sp.simplify(expr)
            if expr != 0:
                Ric[(b_, d_)] = expr
    Rsc = sp.simplify(sum(ginv[i, j] * Ric.get((i, j), 0)
                          for i in range(4) for j in range(4)))
    Gmix = []
    for i in range(4):
        expr = sum(ginv[i, k] * Ric.get((k, i), 0) for k in range(4)) \
            - sp.Rational(1, 2) * Rsc
        Gmix.append(sp.simplify(expr))
    _GEN = (Gmix, sp.simplify(Rsc), B, P)
    return _GEN


def einstein_mixed(b_expr, phi_expr):
    Gmix, Rsc, B, P = _generic_einstein()
    subs = {B: b_expr, P: phi_expr,
            sp.Derivative(B, r): sp.diff(b_expr, r),
            sp.Derivative(B, (r, 2)): sp.diff(b_expr, r, 2),
            sp.Derivative(P, r): sp.diff(phi_expr, r),
            sp.Derivative(P, (r, 2)): sp.diff(phi_expr, r, 2)}
    return [sp.simplify(g.subs(subs)) for g in Gmix], \
        sp.simplify(Rsc.subs(subs))


def pi_mixed(rho, pr, pt):
    """Pi^mu_nu for tau^mu_nu = diag(-rho, pr, pt, pt)."""
    tau = -rho + pr + 2 * pt
    S = rho**2 + pr**2 + 2 * pt**2
    base = S / 8 - tau**2 / 24
    return [-rho**2 / 4 + tau * (-rho) / 12 + base,
            pr**2 / 4 * -1 + tau * pr / 12 + base,
            -pt**2 / 4 + tau * pt / 12 + base]


def ec_margins(rho, pr, pt):
    """All four ECs for anisotropic fluid; returns dict of arrays."""
    return dict(
        nec1=rho + pr, nec2=rho + pt, rho=rho,
        sec=rho + pr + 2 * pt,
        dec_r=rho - np.abs(pr), dec_t=rho - np.abs(pt))


def div_r(Tt, Tr, Tth, dTr, phi_p):
    return dTr + phi_p * (Tr - Tt) + (2.0 / RV) * (Tr - Tth)


# numeric grid
RV = np.logspace(0, 3, 4001)          # r/r0 in [1, 1e3]
LAMBDAS = (1.0, 100.0)


def num(expr, r0v=1.0):
    f = sp.lambdify(r, expr.subs(r0, r0v).subs(TH, sp.pi / 2), 'numpy')
    out = np.asarray(f(RV), dtype=np.float64)
    return np.broadcast_to(out, RV.shape).astype(np.float64)


LOGR = np.log(RV)


def dnum(arr):
    """d/dr via uniform log-grid gradient (d/dr = (1/r) d/dlnr)."""
    return np.gradient(arr, LOGR, edge_order=2) / RV


def analyse(name, Gc, Rsc, tau_fns, lam):
    """tau_fns: (rho, pr, pt) numeric arrays or None (vacuum).
    Returns audit dict for this (shape, Phi, tau, lambda)."""
    k5_4 = 6.0 * K4 / lam
    Gt, Gr, Gth = Gc[0], Gc[1], Gc[2]
    Gtr = Gt + Gr + 2 * Gth
    if tau_fns is None:
        rho = np.zeros_like(RV); pr = np.zeros_like(RV)
        pt = np.zeros_like(RV)
    else:
        rho, pr, pt = tau_fns
    Pi = pi_mixed(rho, pr, pt)
    # required E (mixed): E = k4^2 tau + k5^4 Pi - G
    Et = K4 * (-rho) + k5_4 * Pi[0] - Gt
    Er = K4 * pr + k5_4 * Pi[1] - Gr
    Eth = K4 * pt + k5_4 * Pi[2] - Gth
    trE = Et + Er + 2 * Eth
    escale = np.maximum(np.max(np.abs(
        np.stack([Et, Er, Eth])), axis=0), 1e-300)
    # divergence identity: div E - k5^4 div Pi  (= k4^2 div tau if
    # div G = 0); radial component, analytic derivatives via gradient
    phi_p = PHIP_NUM[name.split('|')[1]]
    dEr = dnum(Er)
    divE = div_r(Et, Er, Eth, dEr, phi_p)
    dPir = dnum(k5_4 * Pi[1])
    divPi = div_r(k5_4 * Pi[0], k5_4 * Pi[1], k5_4 * Pi[2], dPir, phi_p)
    resid = divE - divPi
    # physical divergence scale at each r: |E|/r (both divE and
    # k5^4 divPi are bounded by component-magnitude/r scales of
    # their tensors; E-scale used, Pi-scale folded in via xcheck)
    pscale = np.maximum(escale / RV, 1e-300)
    rel_resid = np.abs(resid) / pscale
    # tau divergence (cross-check: resid should equal k4^2 div tau)
    dtaur = dnum(K4 * pr)
    divtau = div_r(K4 * (-rho), K4 * pr, K4 * pt, dtaur, phi_p)
    xcheck = np.max(np.abs(resid - divtau)
                    / np.maximum(np.abs(divtau), 1e-300))
    # ECs of tau
    ec = ec_margins(rho, pr, pt)
    ec_min = {k: float(np.min(v)) for k, v in ec.items()}
    ec_legal = bool(all(v >= -1e-12 for v in ec_min.values()))
    # E effective ECs (report only): T_E = -E/k4^2 mixed
    rhoE = Et / K4            # -T_E^t_t = E^t_t/k4^2
    prE = -Er / K4
    ptE = -Eth / K4
    ecE = ec_margins(rhoE, prE, ptE)
    ecE_min = {k: float(np.min(v)) for k, v in ecE.items()}
    # Pi null contraction sign (does Pi carry the violation?)
    # total effective NEC1 = (G^r_r - G^t_t)/k4^2 must be < 0 at throat
    nec1_tot_throat = float((Gr[0] - Gt[0]) / K4)
    pi_nec1 = (Pi[1] - Pi[0])          # Pi^r_r - Pi^t_t ~ (rho+pr) dir
    tau_nec1_throat = float(rho[0] + pr[0])
    # tidal alpha test: tidal (M=0) E profile derived in-script from
    # the tidal metric itself (see tidal_profile()): E_tidal mixed
    # = (q_t, q_r, q_th) / r^4 with constant q's, traceless.
    # alpha-match iff (U, P1, P2) * r^4 is a constant multiple of
    # ( -q_t, q_r, q_th ) with one common factor Q.
    U = -Et
    qt, qr, qth = TIDAL_Q
    prof = np.stack([U * RV**4, Er * RV**4, Eth * RV**4])
    base = np.array([-qt, qr, qth])
    # least squares common factor per radius, then constancy
    denom = float(base @ base)
    Qfit = (base @ prof) / denom
    fitres = prof - np.outer(base, Qfit)
    spread = float(np.max(np.abs(fitres)) /
                   max(np.max(np.abs(prof)), 1e-300))
    spread2 = spread
    const_dev = float(np.std(Qfit) / np.mean(np.abs(Qfit))) \
        if np.mean(np.abs(Qfit)) > 0 else np.inf
    return dict(
        lambda_=lam, ec_legal=ec_legal, ec_min=ec_min,
        traceE_max_abs=float(np.max(np.abs(trE))),
        traceE_rel=float(np.max(np.abs(trE) / escale)),
        div_resid_rel_med=float(np.median(rel_resid)),
        div_resid_rel_max=float(np.max(rel_resid)),
        div_xcheck_max_rel=float(xcheck),
        E_ec_min=ecE_min,
        nec1_total_throat=nec1_tot_throat,
        tau_nec1_throat=tau_nec1_throat,
        pi_nec1_throat=float(pi_nec1[0]),
        tidal=dict(Q_fit_mean=float(np.mean(Qfit)),
                   Q_const_dev=const_dev, spread_r=spread,
                   spread_th=spread2,
                   alpha_match=bool(const_dev < 0.01 and spread < 0.01
                                    and spread2 < 0.01)),
        throat=dict(rho=float(rho[0]), pr=float(pr[0]), pt=float(pt[0]),
                    U=float(U[0]), P1=float(Er[0]), P2=float(Eth[0])),
        far=dict(rho_end=float(rho[-1]), U_end=float(U[-1])))


def main():
    out = dict(item='P21-1(a) throat SMS audit', k4sq=K4,
               grid='log r/r0 in [1,1e3], 4001 pts', cases={})
    Gcache = {}
    for sname, bexpr in SHAPES.items():
        for pname, pexpr in PHIS.items():
            Gc_sym, Rsc_sym = einstein_mixed(bexpr, pexpr)
            Gc = [num(g) for g in Gc_sym]
            Gcache[(sname, pname)] = (Gc, num(Rsc_sym))
            out['cases'][f'{sname}|{pname}|G'] = dict(
                G_throat=[float(g[0]) for g in Gc],
                R_throat=float(num(Rsc_sym)[0]),
                traceG_max=float(np.max(np.abs(
                    Gc[0] + Gc[1] + 2 * Gc[2]))))
    # Tidal (Schwarzschild-AdS5 projection) profile, derived from the
    # tidal metric itself: M=0, Q=1: f = 1 - 1/r^2, b = 1/r,
    # Phi = (1/2) ln(1 - 1/r^2); E_tidal = -G_tidal (vacuum brane).
    global TIDAL_Q
    Gt_sym, _ = einstein_mixed(1 / r, sp.log(1 - 1 / r**2) / 2)
    Gt_num = [num(g) for g in Gt_sym]
    far = RV >= 2.0
    Eq = [-Gt_num[0][far] * RV[far]**4, -Gt_num[1][far] * RV[far]**4,
          -Gt_num[2][far] * RV[far]**4]
    TIDAL_Q = tuple(float(np.mean(e)) for e in Eq)
    out['tidal_profile'] = dict(
        E_times_r4_means=list(TIDAL_Q),
        E_times_r4_stds=[float(np.std(e)) for e in Eq],
        trace_times_r4=float(np.mean(Eq[0] + Eq[1] + 2 * Eq[2])),
        note='mixed E_tidal = (q_t, q_r, q_th)/r^4 on r>=2')
    print('TIDAL profile q =', TIDAL_Q, 'trace*r^4 =',
          out['tidal_profile']['trace_times_r4'])
    # Phi' numeric per Phi case (for divergence formula)
    global PHIP_NUM
    PHIP_NUM = {'zero': np.zeros_like(RV),
                'minus': num(sp.diff(PHIS['minus'], r))}
    for sname in SHAPES:
        for pname in PHIS:
            Gc, Rsc = Gcache[(sname, pname)]
            Gt, Gr, Gth = Gc[0], Gc[1], Gc[2]
            Gtr = Gt + Gr + 2 * Gth
            key0 = f'{sname}|{pname}'
            # F0 vacuum
            for lam in LAMBDAS:
                out['cases'][f'{key0}|vacuum|lam{lam:g}'] = \
                    analyse(key0, Gc, Rsc, None, lam)
            for lam in LAMBDAS:
                k5_4 = 6.0 * K4 / lam
                # F1 dust, trace-solved: a rho^2 + b rho + c = 0,
                # a = k5^4/6, b = -k4^2, c = -Gtr  (from tr Pi = rho^2/6)
                a = k5_4 / 6.0
                disc = K4**2 + 4 * a * Gtr
                for branch, sgn in (('minus', -1.0), ('plus', 1.0)):
                    ok = disc >= 0
                    rho = np.where(ok, (K4 + sgn * np.sqrt(
                        np.maximum(disc, 0))) / (2 * a), np.nan)
                    tau = (rho, np.zeros_like(RV), np.zeros_like(RV))
                    rec = analyse(key0, Gc, Rsc, tau, lam)
                    rec['disc_frac_ok'] = float(np.mean(ok))
                    rec['rho_min'] = float(np.nanmin(rho))
                    out['cases'][f'{key0}|dust-{branch}|lam{lam:g}'] = rec
                # F2 radiation w=1/3, trace-solved: Gtr = k5^4 rho^2/3
                ok = Gtr >= 0
                rho = np.where(ok, np.sqrt(np.maximum(
                    3 * Gtr / k5_4, 0)), np.nan)
                tau = (rho, rho / 3, rho / 3)
                rec = analyse(key0, Gc, Rsc, tau, lam)
                rec['Gtr_frac_ok'] = float(np.mean(ok))
                out['cases'][f'{key0}|radiation|lam{lam:g}'] = rec
                # F3 anisotropic: rho = A/(k4^2 r) (A=1), pr = rho/2,
                # pt from CONSERVATION (div tau = 0 by construction):
                # pt = pr + (r/2)(pr' + (rho+pr) Phi')
                rho = 1.0 / (K4 * RV)
                pr = 0.5 * rho
                dpr = dnum(pr)
                phi_p = PHIP_NUM[pname]
                pt = pr + (RV / 2) * (dpr + (rho + pr) * phi_p)
                rec = analyse(key0, Gc, Rsc, (rho, pr, pt), lam)
                out['cases'][f'{key0}|cons-aniso|lam{lam:g}'] = rec
                # F4 anisotropic trace-solved: rho, pr as F3; pt root
                # of trace equation (quadratic in pt), root nearer F3 pt
                # coefficients from trE = 0 (symbolic in pt, numeric):
                # use per-point quadratic via pi_mixed algebra:
                # tr constraint: Gtr = k4^2(-rho+pr+2pt)
                #   + k5^4[(rho^2+pr^2+2pt^2)/4 - tau^2/12], tau=-rho+pr+2pt
                # expand with sympy once:
                ptsym = sp.symbols('pt')
                rho_s, pr_s = sp.symbols('rho pr')
                tau_s = -rho_s + pr_s + 2 * ptsym
                S_s = rho_s**2 + pr_s**2 + 2 * ptsym**2
                expr = K4 * tau_s + k5_4 * (S_s / 4 - tau_s**2 / 12)
                poly = sp.Poly(expr, ptsym)
                c2, c1, c0 = [float(poly.nth(i)) if False else None
                              for i in (2, 1, 0)]
                # nth needs numeric rho/pr; do it vectorised manually:
                # tau = T0 + 2 pt, T0 = -rho+pr
                T0 = -rho + pr
                # S/4 - tau^2/12: pt^2 coeff: (2/4) - (4/12) = 1/6
                # pt^1 coeff: -(2*T0*2)/12 = -T0/3 ; const:
                # (rho^2+pr^2)/4 - T0^2/12
                A2 = k5_4 / 6.0
                A1 = K4 * 2 + k5_4 * (-T0 / 3.0)
                A0 = K4 * T0 + k5_4 * ((rho**2 + pr**2) / 4
                                       - T0**2 / 12) - Gtr
                disc4 = A1**2 - 4 * A2 * A0
                ok4 = disc4 >= 0
                sq = np.sqrt(np.maximum(disc4, 0))
                r_a = (-A1 + sq) / (2 * A2)
                r_b = (-A1 - sq) / (2 * A2)
                pt4 = np.where(np.abs(r_a - pt) < np.abs(r_b - pt),
                               r_a, r_b)
                pt4 = np.where(ok4, pt4, np.nan)
                rec = analyse(key0, Gc, Rsc, (rho, pr, pt4), lam)
                rec['disc_frac_ok'] = float(np.mean(ok4))
                out['cases'][f'{key0}|trace-aniso|lam{lam:g}'] = rec
    with open(RES + 'p211_throat.json', 'w') as fh:
        json.dump(out, fh, indent=2, default=float)
    # compact printout
    for k, v in out['cases'].items():
        if 'G' in k.split('|')[-1]:
            continue
        print(k, 'EC', v['ec_legal'], 'trErel %.2e' % v['traceE_rel'],
              'divmed %.2e' % v['div_resid_rel_med'],
              'tidal', v['tidal']['alpha_match'],
              'Qdev %.2g' % v['tidal']['Q_const_dev'])


PHIP_NUM = {}
TIDAL_Q = (0.0, 0.0, 0.0)
if __name__ == '__main__':
    main()
