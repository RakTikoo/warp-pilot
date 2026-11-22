#!/usr/bin/env python3
"""
p214_lib.py -- P21-4 shared machinery: f(T,B) under BBW Eq. (42).

Transcription (run record, stated before any scan number):
  BBW = Bahamonde-Bohmer-Wright, PRD 92 (2015) 104042, Eq. (42):
    H = -f_T G + g Box f_B - nabla nabla f_B
        + 1/2 (B f_B + T f_T - f) g
        + 2[(f_BB+f_BT) nabla B + (f_TT+f_BT) nabla T] S
  Programme variables: t = T_prog (p111_d, f=t is TEGR),
  b = R + t (so R = -t + b); BBW variables u = -t, v = R - t.
  Families phi(t,b); BBW function F(u,v) = phi(-u, v-2u).
  All partials to third order carried through the linear map
  (dt,db)_u = (-1,-2), (dt,db)_v = (0,1).
  B_b is computed from the torsion vector (B = 2 nabla.T^mu),
  cross-checked against R - t in the gate.
  Torsion / superpotential from the p111_d path (good areal
  BHL tetrad, direct Cartesian FD). float64, system python3.
"""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase10')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase11')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase12')
import shell as sh            # noqa: E402
import verify_metric as vm    # noqa: E402
import p103_lib as lib        # noqa: E402
import p111_d as D            # noqa: E402
import p121_lib as L121       # noqa: E402
from verify_finalist import dense_points  # noqa: E402

EIGHT_PI = 8.0 * np.pi
LW = 10.0
BETAS = (0.1, 1.1, 1.5)
TOL = 1.430e-4


# ---------------------------------------------------------------- torsion
def coframe(g, pts):
    return D.coframe(g, pts)


def fields_at(gf, pts, h=0.1):
    """One fields_at pass (p111_d pattern): returns g, ginv, S
    (p111_d's flipped S), T_prog, torsion vector V^mu (raw, from
    Tc before the S/T flip), sqrt(-det g)."""
    def fa(pp):
        g = gf(pp)
        e, e_up = coframe(g, pp)
        de = np.zeros((len(pp), 4, 4, 4))
        for k in range(1, 4):
            off = np.zeros(3)
            off[k - 1] = h
            ep, _ = coframe(gf(pp + off), pp + off)
            em, _ = coframe(gf(pp - off), pp - off)
            de[:, k] = (ep - em) / (2.0 * h)
        Ta = de.transpose(0, 2, 1, 3) - de.transpose(0, 2, 3, 1)
        Tc = np.einsum('par,pamn->prmn', e_up, Ta)
        ginv = np.linalg.inv(g)
        Tlow = np.einsum('prs,psmn->prmn', g, Tc)
        Trmn = np.einsum('pma,pnb,prab->prmn', ginv, ginv, Tlow)
        Tup = np.einsum('pma,pnb,prab->prmn', ginv, ginv, Tc)
        coeff2 = np.einsum('prs,pnms->prmn', g, Tup)
        Vcov = np.einsum('pssm->pm', Tc)
        V = np.einsum('pmn,pn->pm', ginv, Vcov)
        eye = np.eye(4)
        S = 0.25 * Trmn + 0.5 * coeff2 \
            - 0.5 * (np.einsum('rm,pn->prmn', eye, V)
                     - np.einsum('rn,pm->prmn', eye, V))
        T_raw = np.einsum('prmn,prmn->p', S, Tc)
        return g, ginv, S, T_raw, V

    g, ginv, S_raw, T_raw, V = fa(pts)
    S = -S_raw
    T = -T_raw
    sdet = np.sqrt(np.maximum(-np.linalg.det(g), 1e-300))
    return dict(g=g, ginv=ginv, S=S, T=T, V=V, sdet=sdet)


def _z_of(F, grad):
    """Superpotential contraction, p111_d pattern:
    Z_ab = S_b^c_a grad_c (S_low from F['S'])."""
    S_low = np.einsum('pdm,prmn->prdn', F['g'], F['S'])
    return np.einsum('pcd,pbda,pc->pab', F['ginv'], S_low, grad)


def scalar_fields(gf, pts, h, B_sign=+1.0):
    """(T_prog, B_b, R) at pts. B_b = 2 nabla_mu T^mu via FD of
    the torsion vector (B_sign +1 per BBW Eq. 17; the gate
    fixes the sign against R - t). R = -t + B_b."""
    Fc = fields_at(gf, pts, h)
    T = Fc['T']
    div = np.zeros(len(pts))
    for k in range(1, 4):
        off = np.zeros(3)
        off[k - 1] = h
        Fp = fields_at(gf, pts + off, h)
        Fm = fields_at(gf, pts - off, h)
        flux_p = Fp['sdet'] * Fp['V'][:, k]
        flux_m = Fm['sdet'] * Fm['V'][:, k]
        div += (flux_p - flux_m) / (2.0 * h)
    div = div / Fc['sdet']
    Bb = B_sign * 2.0 * div
    R = -T + Bb
    return T, Bb, R


def gf_of(beta):
    return L121.gf_of(beta)


def fields_for_set(gf, pts, h, B_sign=+1.0):
    """All family-independent fields at pts with FD step h:
    g, G_cov, T, B_b, R, grads, Hessians (covariant, with
    Christoffel term), Z_t, Z_R (superpotential contractions
    with grad T and grad R). Time derivatives are zero on
    the t=0 slice (programme convention, as P12-1)."""
    P = len(pts)
    # scalar values on the stencil: centre, +-e_i, +-e_i+-e_j
    offs = [(0, 0, 0)]
    for i in range(3):
        for s in (1, -1):
            v = [0, 0, 0]; v[i] = s; offs.append(tuple(v))
    for i in range(3):
        for j in range(i + 1, 3):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0, 0, 0]; v[i] = si; v[j] = sj
                    offs.append(tuple(v))
    vals = {}
    for o in offs:
        pp = pts + h * np.array(o, dtype=np.float64)
        T, Bb, R = scalar_fields(gf, pp, h, B_sign=B_sign)
        vals[o] = (T, Bb, R)
    T0, Bb0, R0 = vals[(0, 0, 0)]
    gradT = np.zeros((P, 4))
    gradR = np.zeros((P, 4))
    HessT = np.zeros((P, 4, 4))
    HessR = np.zeros((P, 4, 4))
    for i in range(3):
        ep = [0, 0, 0]; ep[i] = 1
        em = [0, 0, 0]; em[i] = -1
        ep, em = tuple(ep), tuple(em)
        gradT[:, i + 1] = (vals[ep][0] - vals[em][0]) / (2 * h)
        gradR[:, i + 1] = (vals[ep][2] - vals[em][2]) / (2 * h)
        HessT[:, i + 1, i + 1] = (vals[ep][0] - 2 * T0
                                  + vals[em][0]) / h ** 2
        HessR[:, i + 1, i + 1] = (vals[ep][2] - 2 * R0
                                  + vals[em][2]) / h ** 2
    for i in range(3):
        for j in range(i + 1, 3):
            def tup(a, b):
                v = [0, 0, 0]; v[i] = a; v[j] = b
                return tuple(v)
            HessT[:, i + 1, j + 1] = HessT[:, j + 1, i + 1] = (
                vals[tup(1, 1)][0] - vals[tup(1, -1)][0]
                - vals[tup(-1, 1)][0] + vals[tup(-1, -1)][0]) / (4 * h ** 2)
            HessR[:, i + 1, j + 1] = HessR[:, j + 1, i + 1] = (
                vals[tup(1, 1)][2] - vals[tup(1, -1)][2]
                - vals[tup(-1, 1)][2] + vals[tup(-1, -1)][2]) / (4 * h ** 2)
    Gamma, g, ginv = vm._gamma_at(gf, pts, h)
    # covariant Hessians: d_a d_b f - Gamma^u_{ab} d_u f
    # (Gamma[p,u,a,b] = Gamma^u_{ab})
    HessT = HessT - np.einsum('puab,pu->pab', Gamma, gradT)
    HessR = HessR - np.einsum('puab,pu->pab', Gamma, gradR)
    G, That_GR, _ = vm.einstein_at_points(gf, pts, h=h)
    Fc = fields_at(gf, pts, h)
    Zt = _z_of(Fc, gradT)
    Zr = _z_of(Fc, gradR)
    return dict(g=g, ginv=ginv, G=G, That_GR=That_GR, T=T0, Bb=Bb0,
                R=R0, gradT=gradT, gradR=gradR, HessT=HessT,
                HessR=HessR, Zt=Zt, Zr=Zr, Gamma=Gamma)


# ---------------------------------------------------------------- families
# partials in (t, b) up to third order; keys are index tuples
# (0 = t, 1 = b).  Every family: value + all partials.
def fam_partials(fam, par, t, b):
    t = np.asarray(t, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    z = np.zeros_like(t)
    o = np.ones_like(t)
    if fam == 'B1a':
        g = par
        return {( ): t + g * LW**2 * b**2,
                (0,): o, (1,): 2 * g * LW**2 * b,
                (0, 0): z, (0, 1): z, (1, 1): np.full_like(t, 2 * g * LW**2),
                (0, 0, 0): z, (0, 0, 1): z, (0, 1, 1): z,
                (1, 1, 1): z}
    if fam == 'B1b':
        g = par
        ab = np.abs(b)
        s = np.sign(b)
        with np.errstate(all='ignore'):
            val = t + g * np.sqrt(ab) / LW
            pb = g * s / (2 * LW * np.sqrt(ab))
            pbb = -g / (4 * LW * ab ** 1.5)
            pbbb = 3 * g * s / (8 * LW * ab ** 2.5)
        return {( ): val, (0,): o, (1,): pb,
                (0, 0): z, (0, 1): z, (1, 1): pbb,
                (0, 0, 0): z, (0, 0, 1): z, (0, 1, 1): z,
                (1, 1, 1): pbbb}
    if fam == 'B2':
        a, g = par
        return {( ): t + a * LW**2 * t**2 + g * LW**2 * b**2,
                (0,): 1 + 2 * a * LW**2 * t, (1,): 2 * g * LW**2 * b,
                (0, 0): np.full_like(t, 2 * a * LW**2), (0, 1): z,
                (1, 1): np.full_like(t, 2 * g * LW**2),
                (0, 0, 0): z, (0, 0, 1): z, (0, 1, 1): z,
                (1, 1, 1): z}
    if fam == 'B3':
        k = par
        R = -t + b
        u = k * LW**2 * R
        E = np.exp(u)
        F1 = E * (1 + u)                    # dF/dR
        F2 = k * LW**2 * E * (2 + u)        # d2F/dR2
        F3 = (k * LW**2) ** 2 * E * (3 + u)  # d3F/dR3
        # partials w.r.t. (t,b): dR/dt=-1, dR/db=+1
        return {( ): R * E, (0,): -F1, (1,): F1,
                (0, 0): F2, (0, 1): -F2, (1, 1): F2,
                (0, 0, 0): -F3, (0, 0, 1): F3,
                (0, 1, 1): -F3, (1, 1, 1): F3}
    if fam == 'GR':
        return {( ): t, (0,): o, (1,): z,
                (0, 0): z, (0, 1): z, (1, 1): z,
                (0, 0, 0): z, (0, 0, 1): z, (0, 1, 1): z,
                (1, 1, 1): z}
    raise ValueError(fam)


_COEF = {0: (-1.0, -2.0), 1: (0.0, 1.0)}  # BBW var -> (dt, db)


def _transform(partials, order_idx):
    """BBW partial for index tuple order_idx (0=u, 1=v)."""
    n = len(order_idx)
    out = np.zeros_like(partials[(0,) * n]) if n > 0 else partials[()]
    if n == 0:
        return partials[()]
    import itertools
    for a in itertools.product((0, 1), repeat=n):
        c = 1.0
        for k, idx in enumerate(order_idx):
            c *= _COEF[idx][a[k]]
        out = out + c * partials[tuple(sorted(a))]
    return out


def bbw_partials(fam, par, t, b):
    """All BBW (u,v) partials needed: F, Fu, Fv, Fuu, Fuv, Fvv,
    Fvuu, Fvuv, Fvvv (thirds enter Hess f_B)."""
    p = fam_partials(fam, par, t, b)
    d = dict(F=p[()], Fu=_transform(p, (0,)), Fv=_transform(p, (1,)),
             Fuu=_transform(p, (0, 0)), Fuv=_transform(p, (0, 1)),
             Fvv=_transform(p, (1, 1)),
             Fvuu=_transform(p, (1, 0, 0)),
             Fvuv=_transform(p, (1, 0, 1)),
             Fvvv=_transform(p, (1, 1, 1)))
    # raw (t,b) partials for health reads
    d['phi_t'] = p[(0,)]
    d['phi_b'] = p[(1,)]
    d['phi_bb'] = p[(1, 1)]
    d['all_finite'] = np.isfinite(p[()]) & np.isfinite(p[(0,)]) \
        & np.isfinite(p[(1,)]) & np.isfinite(p[(0, 0)]) \
        & np.isfinite(p[(0, 1)]) & np.isfinite(p[(1, 1)]) \
        & np.isfinite(p[(0, 0, 0)]) & np.isfinite(p[(0, 0, 1)]) \
        & np.isfinite(p[(0, 1, 1)]) & np.isfinite(p[(1, 1, 1)])
    return d


def H_cov(F, fam, par):
    """BBW Eq. (42) covariant LHS at points of field dict F."""
    t, b = F['T'], F['R'] + F['T']       # b = R + t
    u, v = -t, F['R'] - t
    d = bbw_partials(fam, par, t, b)
    g, ginv, G = F['g'], F['ginv'], F['G']
    grad_u = -F['gradT']
    grad_v = F['gradR'] - F['gradT']
    Hess_u = -F['HessT']
    Hess_v = F['HessR'] - F['HessT']
    # Hessian of f_B = F_v
    HessFv = (d['Fvv'][:, None, None] * Hess_v
              + d['Fuv'][:, None, None] * Hess_u
              + d['Fvuu'][:, None, None]
              * np.einsum('pa,pb->pab', grad_u, grad_u)
              + d['Fvuv'][:, None, None]
              * (np.einsum('pa,pb->pab', grad_u, grad_v)
                 + np.einsum('pa,pb->pab', grad_v, grad_u))
              + d['Fvvv'][:, None, None]
              * np.einsum('pa,pb->pab', grad_v, grad_v))
    BoxFv = np.einsum('pab,pab->p', ginv, HessFv)
    # Superpotential term sign: fixed AGAINST the programme's
    # published-W tensor (p111_d) by the PL2 regression gate --
    # with the sign as first transcribed from BBW Eq. (42), the
    # B2 gamma=0 rows reproduced P12-1's PL2 partial/full/sign
    # exactly but ratio_med was off by a systematic ~4.8-5.0x;
    # BBW's S (their Eq. 14) carries the opposite sign to
    # p111_d's flipped S in the programme variables.  The B3
    # gate cannot see this sign (Z == 0 there); the regression
    # can, and it is the arbiter (run record, post-hoc note 3).
    Zx = -((d['Fvv'] + d['Fuv'])[:, None, None] * (F['Zr'] - F['Zt'])
           + (d['Fuu'] + d['Fuv'])[:, None, None] * (-F['Zt']))
    H = (-d['Fu'][:, None, None] * G
         + (g * BoxFv[:, None, None] - HessFv)
         + 0.5 * (v * d['Fv'] + u * d['Fu'] - d['F'])[:, None, None] * g
         + Zx)
    return H, d


def H_orth(F, fam, par):
    H, d = H_cov(F, fam, par)
    return vm.eulerian_that(F['g'], H), d


# ---------------------------------------------------------------- rows
def null_contract(That, n):
    return (That[:, 0, 0]
            + 2.0 * np.einsum('pi,pi->p', That[:, 0, 1:], n)
            + np.einsum('pij,pi,pj->p', That[:, 1:, 1:], n, n))


def binding_fields(beta, B_sign=+1.0):
    bd = lib.bed(beta)
    gf = gf_of(beta)
    pts = bd['pts_b']
    F = fields_for_set(gf, pts, 0.1, B_sign=B_sign)
    F['bd'] = bd
    F['gf'] = gf
    F['pts'] = pts
    return F


def volume_points():
    pts = dense_points()
    r = np.linalg.norm(pts, axis=1)
    m = (r >= 9.0) & (r <= 21.0)
    return pts[m], r[m]


def volume_fields(beta, h, B_sign=+1.0):
    gf = gf_of(beta)
    pts, r = volume_points()
    F = fields_for_set(gf, pts, h, B_sign=B_sign)
    F['gf'] = gf
    F['pts'] = pts
    F['r'] = r
    return F


def _health(F, fam, par):
    t, b = F['T'], F['R'] + F['T']
    d = bbw_partials(fam, par, t, b)
    Geff = -d['Fu']
    fin = d['all_finite']
    b_active = bool(np.any(np.abs(d['phi_b'][fin]) > 0)
                    or np.any(np.abs(d['phi_bb'][fin]) > 0))
    scalar_pass = bool(np.all(d['phi_bb'][fin] > 0)) if b_active else True
    health = bool(np.all(fin) and np.min(Geff[fin]) > 0.0
                  and scalar_pass) if np.any(fin) else False
    return dict(health_pass=health, Geff_min=float(np.min(Geff[fin]))
                if np.any(fin) else None,
                phi_t_min=float(np.min(d['phi_t'][fin]))
                if np.any(fin) else None,
                phi_bb_min=float(np.min(d['phi_bb'][fin]))
                if np.any(fin) else None,
                phi_bb_frac_pos=float(np.mean(d['phi_bb'][fin] > 0))
                if np.any(fin) else None,
                scalar_pass=scalar_pass,
                n_nonfinite=int((~fin).sum()))


def binding_row(F, fam, par):
    bd = F['bd']
    Horth, d = H_orth(F, fam, par)
    # correction against the BED baseline (stored That_GR_b, the
    # same baseline D_that / Gkk_raw / n_b derive from -- P12-1
    # pattern; mixing baselines breaks the cross-check)
    That_GR_bed = bd['That_GR_b']
    Gorth = That_GR_bed * EIGHT_PI
    Corth = Horth - Gorth
    Ckk = null_contract(Corth, bd['n_b'])
    ratio = (Ckk / EIGHT_PI) / bd['D_that']
    fin = d['all_finite']
    ratio = np.where(fin, ratio, -np.inf)
    That_req = That_GR_bed + Corth / EIGHT_PI
    Tkk_req = null_contract(That_req, bd['n_b'])
    c_xf_full = int(np.sum(fin & (Tkk_req >= 0)))
    c_xf_part = int(np.sum(fin & (Ckk >= 0.5 * (-bd['Gkk_raw']))))
    c_f_full = int(np.sum(ratio >= 1.0))
    c_f_part = int(np.sum(ratio >= 0.5))
    npts = len(ratio)
    # Ratio-free cross-check (P12-1 convention, generalised in the
    # dated post-hoc note in the run record): the two evaluations
    # of each inequality may disagree ONLY on points within
    # rounding of the boundary.  B3 kappa=-20 has >100 binding
    # points with H(k*,k*) ~= 0, which sit at ratio = 1 +- 1e-16
    # automatically; a count-only tolerance cannot express that.
    dis_f = np.where(fin & ((ratio >= 1.0) != (Tkk_req >= 0)))[0]
    dis_p = np.where(fin & ((ratio >= 0.5)
                            != (Ckk >= 0.5 * (-bd['Gkk_raw']))))[0]
    assert np.all(np.abs(ratio[dis_f] - 1.0) <= 1e-9), \
        'full cross-check mismatch beyond rounding boundary'
    assert np.all(np.abs(ratio[dis_p] - 0.5) <= 1e-9), \
        'partial cross-check mismatch beyond rounding boundary'
    rfin = ratio[np.isfinite(ratio)]
    hl = _health(F, fam, par)
    row = dict(family=fam, par=par,
               partial=float(c_f_part / npts), full=float(c_f_full / npts),
               partial_crosscheck=float(c_xf_part / npts),
               full_crosscheck=float(c_xf_full / npts),
               n_crosscheck_disagree_full=int(len(dis_f)),
               n_crosscheck_disagree_part=int(len(dis_p)),
               sign=float(np.mean(ratio > 0)),
               ratio_med=float(np.median(rfin)) if rfin.size else None,
               ratio_min=float(np.min(rfin)) if rfin.size else None,
               ratio_max=float(np.max(rfin)) if rfin.size else None,
               T_min=float(np.min(F['T'])), T_max=float(np.max(F['T'])),
               R_min=float(np.min(F['R'])), R_max=float(np.max(F['R'])),
               B_min=float(np.min(F['R'] + F['T'])),
               B_max=float(np.max(F['R'] + F['T'])))
    row.update(hl)
    return row


def fib_dirs(n):
    i = np.arange(n, dtype=np.float64)
    phi = np.arccos(1.0 - 2.0 * (i + 0.5) / n)
    th = np.pi * (1.0 + 5.0 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi),
                     np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)


def worst_nec(That, ndir=4096):
    m = vm.hawking_ellis_margins(That, do_fallback=False)
    dirs = fib_dirs(ndir)
    lin = 2.0 * np.einsum('pi,di->pd', That[:, 0, 1:], dirs)
    quad = np.einsum('pij,di,dj->pd', That[:, 1:, 1:], dirs, dirs)
    vals = That[:, 0, 0][:, None] + lin + quad
    samp = np.min(vals, axis=1)
    worst = np.where(m['typeI'], m['nec'], samp)
    return worst, m['typeI']


def volume_row(F, fam, par, tol=TOL):
    Horth, d = H_orth(F, fam, par)
    Gorth = F['That_GR'] * EIGHT_PI
    That_req = F['That_GR'] + (Horth - Gorth) / EIGHT_PI
    fin = d['all_finite']
    That_req = np.where(fin[:, None, None], That_req, np.nan)
    with np.errstate(all='ignore'):
        worst, typeI = worst_nec(np.nan_to_num(That_req))
    viol = (~fin) | (worst < -tol)
    wgt = F['r'] ** 2
    return dict(nec_viol_frac_vol=float(np.sum(wgt[viol]) / np.sum(wgt)),
                nec_viol_frac_pts=float(np.mean(viol)),
                worst_vol_nec=float(np.min(worst[fin]))
                if np.any(fin) else None,
                n_nonfinite_vol=int((~fin).sum()),
                typeI_frac=float(np.mean(typeI & fin)),
                typeI_frac_vol=float(np.sum(wgt[typeI & fin])
                                     / np.sum(wgt)),
                n_viol=int(viol.sum()))


def volume_ec_row(F, fam, par, tol=TOL):
    """All-four-EC volume read (Hawking-Ellis margins)."""
    Horth, d = H_orth(F, fam, par)
    Gorth = F['That_GR'] * EIGHT_PI
    That_req = F['That_GR'] + (Horth - Gorth) / EIGHT_PI
    fin = d['all_finite']
    m = vm.hawking_ellis_margins(np.nan_to_num(That_req),
                                 do_fallback=True)
    wgt = F['r'] ** 2
    out = dict(typeI_frac=float(np.mean(m['typeI'] & fin)))
    for key in ('nec', 'wec', 'sec', 'dec'):
        viol = (~fin) | (m[key] < -tol)
        out[key + '_viol_frac_vol'] = float(np.sum(wgt[viol])
                                           / np.sum(wgt))
        out[key + '_viol_frac_pts'] = float(np.mean(viol))
        out[key + '_worst'] = float(np.min(m[key][fin])) \
            if np.any(fin) else None
    return out
