"""
mg2_fq.py — MG-2: f(Q) symmetric teleparallel gravity, coincident gauge.

Field equations (primary sources, verified from arXiv:2208.13636 full
text — Mandal, Sahoo & Santos reply):
  Mandal et al. Eq. (1) [their PRD 102, 024057 form]:
    (2/sqrt(-g)) d_gamma( sqrt(-g) f_Q P^gamma_{mu nu} ) + (1/2) g_mn f
    + f_Q ( P_{mu gamma i} Q_nu^{gamma i} - 2 Q_{gamma i mu} P^{gamma i}_nu )
    = -T_mn        (their conventions, kappa=1)
  Zhao covariant form, their Eq. (2):
    f_Q Ghat_mn + (1/2) g_mn (f_Q Q - f) + 2 f_QQ P^lambda_{mn} d_lambda Q
    = T_mn         (kappa=1; d = Levi-Civita derivative)
Definitions (Jimenez-Heisenberg-Koivisto): Q_lmn = d_l g_mn (coincident
gauge), traces Q_l = Q_l mu^mu, Qt_l = Q^mu_{l mu}, superpotential
  P^l_mn = -1/4 Q^l_mn + 1/2 Q_(m^l_n) + 1/4 (Q^l - Qt^l) g_mn
           - 1/4 delta^l_(m Q_n) ,
Q = Q_lmn P^lmn (sign fixed by the FLRW anchor Q = +6H^2, Mandal Eq. (8)).

Convention resolution strategy (documented in CHECKPOINT): the overall
sign/scale is fixed by demanding beta=0 reproduce Ghat/(8 pi) exactly;
the two printed forms must then agree numerically on test metrics.
We audit T_m obtained by solving Zhao's form for the matter tensor —
the rho/p both camps' Friedmann equations agree on (reply Eqs. (14)-(15)
= Mandal's original Eqs. (13)-(14)); the De & How vs Mandal dispute
concerns only the bookkeeping of "effective" density/pressure.
"""
import numpy as np
import verify_metric as vm

EIGHT_PI = 8.0 * np.pi


def _dg_at(gfunc, pt, h):
    """First partials of g at one point: dg[l] = d_l g (4th-order FD)."""
    pt = np.asarray(pt, dtype=float)
    g0 = gfunc(pt[None])[0]
    dg = np.zeros((4, 4, 4))
    for a in range(4):
        vals = []
        for k in (-2, -1, 0, 1, 2):
            p = pt.copy(); p[a] += k * h
            vals.append(gfunc(p[None])[0])
        vals = np.array(vals)
        dg[a] = (vals[0] - 8 * vals[1] + 8 * vals[3] - vals[4]) / (12 * h)
    return g0, dg


def _QP_at(gfunc, pt, h):
    """Q scalar, superpotential P^l_mn, and Q_lmn at one point."""
    g, dg = _dg_at(gfunc, pt, h)
    gi = np.linalg.inv(g)
    Qlmn = dg.copy()                       # Q_lmn = d_l g_mn
    # traces
    Qtr = np.einsum('mn,lmn->l', gi, Qlmn)             # Q_l = Q_l mu^mu
    Qt = np.einsum('mn,mln->l', gi, Qlmn)              # Qt_l = g^mn Q_m l n
    # P^l_mn:
    # term1: -1/4 Q^l_mn  (raise first index only)
    Q1 = np.einsum('la,amn->lmn', gi, Qlmn)
    # term2: +1/2 Q_(m^l_n) : Q_m^l_n = g^{ls} Q_m s n ; symmetrise m<->n
    Qm = np.einsum('ls,msn->mln', gi, Qlmn)
    term2 = 0.5 * (Qm + np.einsum('mln->nlm', Qm))  # symmetrise (m,n) around l
    # term2 enters as (1/2) * [that symmetrised object with indices (l,m,n)]
    term2 = np.einsum('mln->lmn', term2)
    # term3: +1/4 (Q^l - Qt^l) g_mn
    Qup_tr = np.einsum('la,a->l', gi, Qtr)
    Qtup = np.einsum('la,a->l', gi, Qt)
    term3 = 0.25 * (Qup_tr - Qtup)[:, None, None] * g[None]
    # term4: -1/4 delta^l_(m Q_n)
    d = np.eye(4)
    term4 = -0.25 * 0.5 * (d[:, :, None] * Qtr[None, None, :]
                           + d[:, None, :] * Qtr[None, :, None])
    P = -0.25 * Q1 + 0.5 * term2 + term3 + term4
    # P^{l mn} = g^{ma} g^{nb} P^l_{ab} (first index of P is already upper)
    Qs = float(np.einsum('lmn,lmn->', Qlmn, np.einsum('ma,nb,lab->lmn', gi, gi, P)))
    # Convention: the (Q, P) pair above is the Jimenez-Heisenberg-Koivisto
    # convention, giving Q_FLRW = -6H^2. Mandal et al.'s Eq. (8) uses
    # Q = +6H^2, i.e. the flipped pair (Q_M, P_M) = (-Q, -P). We adopt
    # the Mandal/Zhao pair throughout so the printed Eqs. (1)-(2) of
    # arXiv:2208.13636 hold as written.
    return -Qs, -P, Qlmn, g, gi


def Qscalar(gfunc4, pt4, h=0.1):
    return _QP_at(gfunc4, pt4, h)[0]


def _wrap4(gfunc3):
    def gf4(pts4):
        pts4 = np.atleast_2d(pts4)
        return gfunc3(pts4[:, 1:])
    return gf4


def Tm_zhao(gfunc3, pt3, beta, hG=0.15, hQ=0.2):
    """T_m from Zhao's covariant equation with f(Q) = Q + beta Q^2.
    gfunc3: spatial-point metric (N,3)->(N,4,4), stationary."""
    pt3 = np.asarray(pt3, dtype=float)
    pt4 = np.concatenate([[0.0], pt3])
    gfunc4 = _wrap4(gfunc3)
    G, That, m = vm.einstein_at_points(gfunc3, pt3[None], h=hG, do_fallback=False)
    G = G[0]
    Q0, P, Qlmn, g, gi = _QP_at(gfunc4, pt4, hQ)
    # d_l Q on a stencil (each Q eval is itself an FD evaluation);
    # stationary: d_0 Q = 0, spatial components only
    dQ = np.zeros(4)
    for a in range(3):
        vals = []
        for k in (-2, -1, 1, 2):
            p = pt4.copy(); p[a + 1] += k * hQ
            vals.append(Qscalar(gfunc4, p, hQ))
        dQ[a + 1] = (vals[0] - 8 * vals[1] + 8 * vals[2] - vals[3]) / (12 * hQ)
    f = Q0 + beta * Q0 ** 2
    fQ = 1.0 + 2.0 * beta * Q0
    fQQ = 2.0 * beta
    Tm = (fQ * G + 0.5 * g * (fQ * Q0 - f)
          + 2.0 * fQQ * np.einsum('l,lmn->mn', dQ, P)) / EIGHT_PI
    return Tm, Q0


def Tm_mandal(gfunc3, pt3, beta, hQ=0.2, hdiv=0.2):
    """Mandal et al. Eq. (1) LHS (divergence form), 4-coord wrapper.
    Overall sign/scale fixed by the beta=0 anchor (must return -8 pi T_m
    with T_m = G/(8 pi) at beta=0, per their printed '= -T_mn')."""
    pt4 = np.concatenate([[0.0], np.asarray(pt3, dtype=float)])
    gfunc4 = _wrap4(gfunc3)

    def sqrtg_fQ_P(p4):
        Qs, P, Qlmn, g, gi = _QP_at(gfunc4, p4, hQ)
        fQ = 1.0 + 2.0 * beta * Qs
        return np.sqrt(-np.linalg.det(g)) * fQ * P, Qs, P, Qlmn, g, gi

    dens0, Q0, P0, Qlmn0, g, gi = sqrtg_fQ_P(pt4)
    sqrtg = np.sqrt(-np.linalg.det(g))
    # divergence d_gamma ( sqrt(-g) fQ P^gamma_mn ), gamma spatial (stationary)
    div = np.zeros((4, 4))
    for a in range(3):
        vals = []
        for k in (-2, -1, 0, 1, 2):
            p = pt4.copy(); p[a + 1] += k * hdiv
            vals.append(sqrtg_fQ_P(p)[0][a + 1])
        vals = np.array(vals)
        div += (vals[0] - 8 * vals[1] + 8 * vals[3] - vals[4]) / (12 * hdiv)
    f = Q0 + beta * Q0 ** 2
    fQ = 1.0 + 2.0 * beta * Q0
    # algebraic terms: f_Q ( P_{m g i} Q_n^{g i} - 2 Q_{g i m} P^{g i}_n )
    # P_abc all-lower (P0 is P^l_mn):
    Pall = np.einsum('al,bm,cn,lmn->abc', g, g, g, P0)
    # Q_n^{g i} = g^{ga} g^{ib} Q_{n a b}  (Q_lmn = d_l g_mn is (0,3))
    Qn_gi = np.einsum('ga,ib,nab->ngi', gi, gi, Qlmn0)
    # formula needs P_{m g i}: superpotential slots (mu, gamma, i) =
    # (slot2, slot1, slot3) of the all-lower P_{l m n}
    term_a = np.einsum('mgi,ngi->mn', np.transpose(Pall, (1, 0, 2)), Qn_gi)
    # P^{g i}_n = g^{ga} g^{ib} P_{ab n}, P_{abn} = g_{a l} P^l_{b n}
    Pabn = np.einsum('al,lbn->abn', g, P0)
    P_gi_n = np.einsum('ga,ib,abn->gin', gi, gi, Pabn)
    term_b = np.einsum('gim,gin->mn', Qlmn0, P_gi_n)
    LHS = (2.0 / sqrtg) * div + 0.5 * g * f + fQ * (term_a - 2.0 * term_b)
    return LHS  # = -8 pi T_m in Mandal's printed conventions (kappa=1 -> 8pi)
