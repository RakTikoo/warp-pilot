#!/usr/bin/env python3
"""
p93_tensor.py -- P9-3: Einstein-aether correction tensor, FD form.

Theory (survey in CHECKPOINT9.md, recorded before building):
  S = (1/16pi) int sqrt(-g) [ R + L_ae ] + S_m,  signature (-,+,+,+),
  L_ae = -(c1 A1 + c2 A2 + c3 A3 - c4 A4),
  A1 = D_a^c D^a_c, A2 = (D_a^a)^2, A3 = D_a^c D_c^a,
  A4 = a^c a_c,  D_a^c = nabla_a u^c, a^c = u^a D_a^c,
  u^a unit timelike (u^a u_a = -1), designer choice on the bed:
  u = Eulerian normal of the metric.

Correction tensor (E_ab = G_ab + C_ab = 8pi T_matter_ab):
  C_ab = K_ab := -1/2 g_ab L + E_expl,ab - Mdiv_ab
                 + lam_sign * lam * u_a u_b,
where, with Q^a_c = dL/dD_a^c
     = -2 [ c1 D^a_c + c2 theta delta^a_c + c3 D_c^a
            - c4 u^a a_c ],   J^a_c = Q^a_c / 2,
  E_expl,ab = (dL/dg^{ab}) at fixed D_a^c and fixed u^c
     (computed by pointwise central FD in g^{ab}; L is a
     polynomial in the metric, so this is accurate),
  R^{dae} = Q^a_c g^{cd} u^e,
  Mdiv^{mn} = sym[ -1/2 nabla_a R^{man} - 1/2 nabla_a R^{mna}
                   + 1/2 nabla_a R^{amn} ]   (from the dGamma
     part of delta D, integrated by parts),
  lam = 1/2 u^c ( nabla_b J^b_c - Y_c ),  Y_c = 2 c4 a^d D_cd
     (aether EOM u-projection; lam_sign = -1 by the derivation
     -- C contains -lam u_a u_b for the multiplier term
     lam(u^c u_c + 1) in L -- and is FIT in gate A2).
Derivation pattern: the M_alg + M_div variation of p71/p84,
generalised from a scalar Hessian to a vector first derivative.
The -1/2 overall scale vs the naive stress
Ttilde = -(2/sqrt-g) d(sqrt-g L)/dg^{ab} is the Lambda-anchor:
C = -1/2 Ttilde when L sits inside (1/16pi) int (R + L)
(checked: L = -2 Lambda gives C = +Lambda g_ab, as required).
Gates A1 (random-field action FD) and A2 (spherical reduced
action) in p93_gate.py verify all of this BEFORE any wall
number is read.

float64.  System python3 (numpy 2.2.6).
"""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import verify_metric as vm   # noqa: E402

FD_STENCIL = ((-2, 1.0), (-1, -8.0), (1, 8.0), (2, -1.0))


def eulerian_u(pts, g):
    """u^a = Eulerian normal from the ADM split of g."""
    gam = g[:, 1:, 1:]
    gam_inv = np.linalg.inv(gam)
    beta_cov = g[:, 0, 1:]
    beta_up = np.einsum('pij,pj->pi', gam_inv, beta_cov)
    alpha = np.sqrt(np.maximum(
        -g[:, 0, 0] + np.einsum('pi,pi->p', beta_cov, beta_up),
        1e-300))
    u = np.zeros((len(pts), 4))
    u[:, 0] = 1.0 / alpha
    u[:, 1:] = -beta_up / alpha[:, None]
    return u


def L_of(ginv, Dm, u_up, cs):
    """L_ae from (ginv, D_a^c mixed, u^c); also returns parts."""
    c1, c2, c3, c4 = cs
    g = np.linalg.inv(ginv)
    Dup = np.einsum('pab,pbd,pdc->pac', ginv, Dm, g)
    theta = np.einsum('paa->p', Dm)
    a_up = np.einsum('pa,pac->pc', u_up, Dm)
    a_cov = np.einsum('pab,pb->pa', g, a_up)
    A1 = np.einsum('pac,pac->p', Dm, Dup)
    A2 = theta**2
    A3 = np.einsum('pac,pca->p', Dm, Dm)
    A4 = np.einsum('pa,pa->p', a_up, a_cov)
    L = -(c1 * A1 + c2 * A2 + c3 * A3 - c4 * A4)
    return L, dict(Dup=Dup, theta=theta, a_up=a_up,
                   a_cov=a_cov, A=(A1, A2, A3, A4))


def field(gf, pts, h_gamma, u_of, cs, h_fd=0.15):
    """All aether fields at pts.  u_of(pts, g) -> u^a (P,4)."""
    Gamma, g, ginv = vm._gamma_at(gf, pts, h_gamma)
    u_up = u_of(pts, g)
    u_cov = np.einsum('pab,pb->pa', g, u_up)
    P = len(pts)
    du = np.zeros((P, 4, 4))          # du[:, a, c] = d_a u^c
    for e in range(1, 4):
        acc = np.zeros((P, 4))
        for k, wk in FD_STENCIL:
            off = np.zeros(3)
            off[e - 1] = k * h_fd
            po = pts + off
            acc += wk * u_of(po, gf(po))
        du[:, e] = acc / (12.0 * h_fd)
    Dm = du + np.einsum('pcad,pd->pac', Gamma, u_up)
    L, parts = L_of(ginv, Dm, u_up, cs)
    Dcov = np.einsum('pbc,pac->pab', g, Dm)   # nabla_a u_b
    c1, c2, c3, c4 = cs
    Q = -2.0 * (c1 * parts['Dup']
                + c2 * parts['theta'][:, None, None] * np.eye(4)[None]
                + c3 * np.swapaxes(Dm, -1, -2)
                - c4 * np.einsum('pa,pc->pac', u_up, parts['a_cov']))
    R = np.einsum('pac,pcd,pe->pdae', Q, ginv, u_up)
    Y = 2.0 * c4 * np.einsum('pd,pad->pa', parts['a_up'], Dcov)
    return dict(g=g, ginv=ginv, Gamma=Gamma, u_up=u_up,
                u_cov=u_cov, Dm=Dm, Dcov=Dcov, L=L, Q=Q, R=R,
                Y=Y, **parts)


def _expl_fd(fc, cs, eps=1e-5):
    """E_expl,ab = dL/dg^{ab} at fixed D_a^c, u^c (pointwise FD)."""
    ginv, Dm, u_up = fc['ginv'], fc['Dm'], fc['u_up']
    P = len(Dm)
    E = np.zeros((P, 4, 4))
    for m in range(4):
        for n in range(m, 4):
            gp = ginv.copy()
            gm = ginv.copy()
            gp[:, m, n] += eps
            gm[:, m, n] -= eps
            if n != m:
                gp[:, n, m] += eps
                gm[:, n, m] -= eps
            Lp, _ = L_of(gp, Dm, u_up, cs)
            Lm, _ = L_of(gm, Dm, u_up, cs)
            fac = 2.0 * eps if m == n else 4.0 * eps
            E[:, m, n] = (Lp - Lm) / fac
            E[:, n, m] = E[:, m, n]
    return E


def _divergences(gf, centers, h_gamma, u_of, cs, fc, h_fd=0.15):
    """Div1/Div2/Div3 (contravariant) and divJ (covariant)."""
    P = len(centers)
    dR = np.zeros((P, 4, 4, 4, 4))    # [e, d, a, e2]
    dJ = np.zeros((P, 4, 4, 4))       # [e, b, c]
    for e in range(1, 4):
        accR = np.zeros((P, 4, 4, 4))
        accJ = np.zeros((P, 4, 4))
        for k, wk in FD_STENCIL:
            off = np.zeros(3)
            off[e - 1] = k * h_fd
            fo = field(gf, centers + off, h_gamma, u_of, cs, h_fd)
            accR += wk * fo['R']
            accJ += wk * (0.5 * fo['Q'])
        dR[:, e] = accR / (12.0 * h_fd)
        dJ[:, e] = accJ / (12.0 * h_fd)
    Gam = fc['Gamma']
    R = fc['R']
    trG = np.einsum('paas->ps', Gam)
    Div1 = np.einsum('paman->pmn', dR) \
        + np.einsum('pmas,psan->pmn', Gam, R) \
        + np.einsum('ps,pmsn->pmn', trG, R) \
        + np.einsum('pnas,pmas->pmn', Gam, R)
    Div2 = np.einsum('pamna->pmn', dR) \
        + np.einsum('pmas,psna->pmn', Gam, R) \
        + np.einsum('pnas,pmsa->pmn', Gam, R) \
        + np.einsum('ps,pmns->pmn', trG, R)
    Div3 = np.einsum('paamn->pmn', dR) \
        + np.einsum('ps,psmn->pmn', trG, R) \
        + np.einsum('pmas,pasn->pmn', Gam, R) \
        + np.einsum('pnas,pams->pmn', Gam, R)
    J = 0.5 * fc['Q']
    divJ = np.einsum('pbbc->pc', dJ) \
        + np.einsum('ps,psc->pc', trG, J) \
        - np.einsum('psbc,pbs->pc', Gam, J)
    return Div1, Div2, Div3, divJ


def C_aether(gf, centers, h_gamma, u_of, cs, lam_sign=-1.0,
             h_fd=0.15, want_parts=False, lam_override=None):
    """Correction tensor C_ab (covariant) at centers.
    lam_override: prescribed multiplier field values at centers
    (gate A1 mode; replaces the EOM-projection lambda)."""
    fc = field(gf, centers, h_gamma, u_of, cs, h_fd)
    E_expl = _expl_fd(fc, cs)
    Div1, Div2, Div3, divJ = _divergences(
        gf, centers, h_gamma, u_of, cs, fc, h_fd)
    Mdiv_up = -0.5 * Div1 - 0.5 * Div2 + 0.5 * Div3
    Mdiv_up = 0.5 * (Mdiv_up + np.swapaxes(Mdiv_up, -1, -2))
    g = fc['g']
    Mdiv = np.einsum('pac,pcd,pdb->pab', g, Mdiv_up, g)
    # aether EOM: A_c = -nabla_a Q^a_c + Y_c + 2 lam u_c = 0;
    # u-projection (u.u = -1): lam = -u.(nabla J) + (1/2) u.Y
    # with J = Q/2.  (Fitted/confirmed in gate A2.)
    lam = -np.einsum('pa,pa->p', fc['u_up'], divJ) \
        + 0.5 * np.einsum('pa,pa->p', fc['u_up'], fc['Y'])
    if lam_override is not None:
        lam = np.asarray(lam_override, dtype=np.float64)
    C = -0.5 * g * fc['L'][:, None, None] + E_expl - Mdiv \
        + lam_sign * lam[:, None, None] \
        * np.einsum('pa,pb->pab', fc['u_cov'], fc['u_cov'])
    if want_parts:
        return C, dict(fc=fc, E_expl=E_expl, Mdiv=Mdiv, lam=lam,
                       Div=(Div1, Div2, Div3))
    return C
