#!/usr/bin/env python3
"""
p182_basis.py -- coefficient-basis precomputation for P18-2.

For a fixed Bed (beta, profile, pi0, shape), every EOM quantity is
linear in the coefficient values at stencil points:
  scalar EOM(pi)(p) = sum_s [ W1(p,s,:) . c(q_s) + W2(p,s,:) . c(q_s) ]
      c(q) = (F_XL, A1, A2, A3, A4, A5) at q  (F_XL is x-independent)
  metric E(p) = E_R0(p) + f1 * E_R1(p)
      + sum_i [ A_i(p) * P0_i(p)
                - sum_a (A_i(q_a+) P1_i^a(q_a+)
                         - A_i(q_a-) P1_i^a(q_a-)) / (2h) ]
        * (2/sqrtg(p))     [P0/P1 stored as density derivatives]
All basis weights come from FD partials of the Lagrangian basis
(R, L1..L5) on field jets.  float64.
"""
import numpy as np

import p182_engine as E

DELTA = 2e-4     # jet-perturbation size for EL partials
HF = 0.3         # field stencil for divergences


def stencil(pts, h=HF):
    """(P,19,3): centre, 6 axial (+-e_i), 12 corners (+-e_i+-e_j)."""
    pts = np.asarray(pts, dtype=np.float64)
    P = len(pts)
    out = np.zeros((P, 19, 3))
    out[:, 0] = pts
    idx = 1
    for i in range(3):
        for s in (+1, -1):
            q = pts.copy(); q[:, i] += s * h
            out[:, idx] = q; idx += 1
    for i in range(3):
        for j in range(i + 1, 3):
            for si in (+1, -1):
                for sj in (+1, -1):
                    q = pts.copy()
                    q[:, i] += si * h; q[:, j] += sj * h
                    out[:, idx] = q; idx += 1
    return out


def jets_at(bed, pts, h=0.3):
    g, dg, ddg = E.metric_jets(bed.gf, pts, h)
    v, H = bed.pi_jets(pts)
    return g, dg, ddg, v, H


def _basis_at(bed, pts, h=0.3):
    g, dg, ddg, v, H = jets_at(bed, pts, h)
    sg, basis, aux = E.lag_basis(g, dg, ddg, v, H)
    return sg, basis, aux, (g, dg, ddg, v, H)


# ------------------------------------------------------------------
# scalar EOM basis
# ------------------------------------------------------------------
def scalar_eom_basis(bed, pts, h=HF, jet_h=0.3):
    """Returns dict: W1, W2 (P,19,6) [slots FXL,A1..A5], Xhat_s (P,19),
    XL_s (P,19), sqrtg (P,).  EOM = sum_s (W1+W2).c(q_s) / 1
    (weights already include 1/sqrtg(p))."""
    P = len(pts)
    st = stencil(pts, h)                       # (P,19,3)
    flat = st.reshape(P * 19, 3)
    sg, basis, aux, jets = _basis_at(bed, flat, jet_h)
    g, dg, ddg, v, H = jets
    sg = sg.reshape(P, 19)
    basis = basis.reshape(P, 19, 6)
    v = v.reshape(P, 19, 4)
    XLs = aux['XL'].reshape(P, 19)
    # --- P1 partials: d(sqrtg * basis_k)/d v_a  at every stencil pt
    # FD over v (4 vars), batched over all stencil points
    N = P * 19
    gf_, dg_, ddg_, v_, H_ = g, dg, ddg, v.reshape(N, 4), H.reshape(N, 4, 4)
    sgf = sg.reshape(N)
    P1 = np.zeros((N, 6, 4))                   # slots: R(FXL), L1..L5
    for a in range(4):
        for sgn in (+1, -1):
            vv = v_.copy(); vv[:, a] += sgn * DELTA
            s2, b2, _ = E.lag_basis(gf_, dg_, ddg_, vv, H_)
            val = s2[:, None] * b2             # (N,6)
            P1[:, :, a] += sgn * val
    P1 /= (2 * DELTA)
    # R-slot P1 is analytic instead: sqrtg * R * 2 v^a (replace FD,
    # which also sees it -- FD is fine and consistent; keep FD).
    P1 = P1.reshape(P, 19, 6, 4)
    # coefficient-derivative slots: d(A_i L_i)/d v_a via X_L:
    # A_iX * L_i * 2 v^a  (density).  Build (P,19,5,4).
    vup = np.einsum('psab,psb->psa',
                    aux['ginv'].reshape(P, 19, 4, 4),
                    v.reshape(P, 19, 4))
    P1X = sg.reshape(P, 19)[:, :, None, None] \
        * basis.reshape(P, 19, 6)[:, :, 1:, None] \
        * (2.0 * vup)[:, :, None, :]
    # R-sector X-slot: d(F R)/d v_a via X_L = F_XL * sqrtg * R * 2 v^a
    P1R = sg.reshape(P, 19)[:, :, None] \
        * basis.reshape(P, 19, 6)[:, :, 0][:, :, None] \
        * (2.0 * vup)
    # P1 slots are (R, L1..L5), aligned with c slots (FXL, A1..A5):
    # the R partials wrt (v, H) vanish identically (R is metric-only),
    # and the F-sector scalar term enters via W1R below.
    W1X = np.zeros((P, 19, 5))
    W1R = np.zeros((P, 19))
    # --- P2 partials: d(sqrtg * basis_k)/d H_ab at every stencil pt
    P2 = np.zeros((N, 6, 4, 4))
    for (a, b) in E.SYM:
        fac = 0.5 if a != b else 1.0   # pair FD = 2x component (a!=b)
        for sgn in (+1, -1):
            HH = H_.copy()
            HH[:, a, b] += sgn * DELTA
            if a != b:
                HH[:, b, a] += sgn * DELTA
            s2, b2, _ = E.lag_basis(gf_, dg_, ddg_, v_, HH)
            val = s2[:, None] * b2
            P2[:, :, a, b] += sgn * val * fac
            if a != b:
                P2[:, :, b, a] += sgn * val * fac
    P2 /= (2 * DELTA)
    P2 = P2.reshape(P, 19, 6, 4, 4)
    # --- assemble weights
    W1 = np.zeros((P, 19, 6))
    W2 = np.zeros((P, 19, 6))
    inv = 1.0 / sg[:, 0]
    # div P1: only spatial dirs a=1..3; axial stencil idx: dir i
    # (0-based spatial) -> slots 1+2i (+) and 2+2i (-)
    for i in range(3):
        ip, im = 1 + 2 * i, 2 + 2 * i
        W1[:, ip, :] += -P1[:, ip, :, i + 1] / (2 * h)
        W1[:, im, :] += +P1[:, im, :, i + 1] / (2 * h)
        W1X[:, ip, :] += -P1X[:, ip, :, i + 1] / (2 * h)
        W1X[:, im, :] += +P1X[:, im, :, i + 1] / (2 * h)
        W1R[:, ip] += -P1R[:, ip, i + 1] / (2 * h)
        W1R[:, im] += +P1R[:, im, i + 1] / (2 * h)
    W1X *= inv[:, None, None]
    W1R *= inv[:, None]
    # divdiv P2: diagonal second derivatives
    for i in range(3):
        ip, im = 1 + 2 * i, 2 + 2 * i
        a = i + 1
        W2[:, ip, :] += P2[:, ip, :, a, a] / h**2
        W2[:, 0, :] += -2.0 * P2[:, 0, :, a, a] / h**2
        W2[:, im, :] += P2[:, im, :, a, a] / h**2
    # cross derivatives: corners idx from 7: pairs (0,1),(0,2),(1,2),
    # signs (++),(+-),(-+),(--)
    cidx = 7
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        a, b = i + 1, j + 1
        for (si, sj, sgn) in ((1, 1, 1), (1, -1, -1),
                              (-1, 1, -1), (-1, -1, 1)):
            # P2^{ab} enters with factor 2 (a!=b, symmetric sum)
            W2[:, cidx, :] += sgn * 2.0 * P2[:, cidx, :, a, b] \
                / (4 * h**2)
            cidx += 1
    W1 *= inv[:, None, None]
    W2 *= inv[:, None, None]
    return dict(W1=W1, W2=W2, W1X=W1X, W1R=W1R, XL_s=XLs,
                sqrtg=sg[:, 0])


# ------------------------------------------------------------------
# metric E basis
# ------------------------------------------------------------------
def metric_E_basis(bed, pts, h=HF, jet_h=0.3):
    """Returns dict:
      ER0, ER1 (P,4,4) covariant F-sector basis (F=1/2 / F=Xhat),
      P0 (P,5,4,4) contravariant density partials per sector,
      P1n (P,6,3,5,4,4): [axial slot (dir,sign) flattened as
            2*i+{0:+,-}], dir a, sector, mu, nu] contravariant,
      g (P,4,4), sqrtg (P,), XL_p, XL axial neighbours (P,6),
      Xhat_p, G (P,4,4) from the jet Ricci."""
    P = len(pts)
    g, dg, ddg, v, H = jets_at(bed, pts, jet_h)
    sg, basis, aux = E.lag_basis(g, dg, ddg, v, H)
    ginv = aux['ginv']
    G = aux['Ric'] - 0.5 * basis[:, 0][:, None, None] * g
    # ---- F sector: Xhat field on stencil for nabla nabla F
    st = stencil(pts, h)
    flat = st.reshape(P * 19, 3)
    XLf, _, _, _, _ = bed.X_fields(flat)
    XLs = XLf.reshape(P, 19)
    Xref = None  # filled by caller via XLs median; Xhat = -XL/(2 Xref)
    # partial derivatives of a scalar field Fld (P,19) on stencil
    def fld_derivs(Fld):
        dF = np.zeros((P, 4))
        ddF = np.zeros((P, 4, 4))
        for i in range(3):
            ip, im = 1 + 2 * i, 2 + 2 * i
            dF[:, i + 1] = (Fld[:, ip] - Fld[:, im]) / (2 * h)
            ddF[:, i + 1, i + 1] = (Fld[:, ip] - 2 * Fld[:, 0]
                                    + Fld[:, im]) / h**2
        cidx = 7
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            vals = []
            for _ in range(4):
                vals.append(Fld[:, cidx]); cidx += 1
            ddF[:, i + 1, j + 1] = ddF[:, j + 1, i + 1] = \
                (vals[0] - vals[1] - vals[2] + vals[3]) / (4 * h**2)
        return dF, ddF
    Gam = aux['Gam']                            # (P,a,b,c) Gamma^c_ab

    def ER_of(Fld):
        dF, ddF = fld_derivs(Fld)
        Hess = ddF - np.einsum('pabc,pc->pab', Gam, dF)
        Box = np.einsum('pab,pab->p', ginv, Hess)
        return Hess - g * Box[:, None, None], dF
    # ER0: F = 1/2 const -> E = G.  ER1: coefficient of f1:
    # E_R = 2 F G + 2(HessF - g BoxF); F = 1/2 + f1 Xhat.
    HessX, _ = ER_of(XLs)                       # Hess of XL field
    # NOTE: ER1 uses Xhat = -XL/(2 Xref): caller scales by -1/(2Xref)
    ER1 = 2.0 * XLs[:, 0][:, None, None] * G + 2.0 * HessX
    ER0 = G.copy()
    # ---- A sectors: P0 at p (FD over ginv sym vars)
    ginv_j, dginv_j, ddginv_j = E.jets_to_ginv(g, dg, ddg)
    N = P
    P0 = np.zeros((P, 5, 4, 4))
    for (mu, nu) in E.SYM:
        fac = 0.5 if mu != nu else 1.0
        for sgn in (+1, -1):
            gi = ginv_j.copy()
            gi[:, mu, nu] += sgn * DELTA
            if mu != nu:
                gi[:, nu, mu] += sgn * DELTA
            gg, dd1, dd2 = E.jets_from_ginv(gi, dginv_j, ddginv_j)
            s2, b2, _ = E.lag_basis(gg, dd1, dd2, v, H)
            val = s2[:, None] * b2[:, 1:]       # sectors L1..L5
            P0[:, :, mu, nu] += sgn * val * fac
            if mu != nu:
                P0[:, :, nu, mu] += sgn * val * fac
    P0 /= (2 * DELTA)
    # coefficient-derivative slots for the metric EOM:
    # d(A_i L_i)/d ginv via X_L: A_iX * sqrtg * L_i * v^mu v^nu
    vup_p = np.einsum('pab,pb->pa', ginv, v)
    P0X = sg[:, None, None, None] * basis[:, 1:][:, :, None, None] \
        * np.einsum('pa,pb->pab', vup_p, vup_p)[:, None]
    # ---- P1 at axial neighbours: FD over dginv vars (a, mu, nu)
    ax = st[:, 1:7].reshape(P * 6, 3)
    ga, dga, ddga, va, Ha = jets_at(bed, ax, jet_h)
    gia, dgia, ddgia = E.jets_to_ginv(ga, dga, ddga)
    Na = P * 6
    P1n = np.zeros((Na, 3, 5, 4, 4))
    for a in range(4):
        for (mu, nu) in E.SYM:
            fac = 0.5 if mu != nu else 1.0
            for sgn in (+1, -1):
                dj = dgia.copy()
                dj[:, a, mu, nu] += sgn * DELTA
                if mu != nu:
                    dj[:, a, nu, mu] += sgn * DELTA
                gg, dd1, dd2 = E.jets_from_ginv(gia, dj, ddgia)
                s2, b2, _ = E.lag_basis(gg, dd1, dd2, va, Ha)
                val = s2[:, None] * b2[:, 1:]
                if a >= 1:
                    P1n[:, a - 1, :, mu, nu] += sgn * val * fac
                    if mu != nu:
                        P1n[:, a - 1, :, nu, mu] += sgn * val * fac
    P1n /= (2 * DELTA)
    P1n = P1n.reshape(P, 6, 3, 5, 4, 4)
    return dict(ER0=ER0, ER1=ER1, P0=P0, P0X=P0X, P1n=P1n, g=g,
                sqrtg=sg, XL_p=XLs[:, 0], XL_ax=XLs[:, 1:7], G=G)


# ------------------------------------------------------------------
# assembly
# ------------------------------------------------------------------
def assemble_E(mb, theta, X_ref, h=HF):
    """Full covariant E_ab at the basis points."""
    P = len(mb['g'])
    XLp = mb['XL_p']
    Xhatp = -XLp / (2 * X_ref)
    cv = E.coeff_values(theta, Xhatp, XLp, X_ref)
    A = np.stack([cv['A1'], cv['A2'], cv['A3'], cv['A4'], cv['A5']],
                 axis=1)                        # (P,5)
    XLax = mb['XL_ax']
    Xhatax = -XLax / (2 * X_ref)
    cvax = E.coeff_values(theta, Xhatax.reshape(-1),
                          XLax.reshape(-1), X_ref)
    Aax = np.stack([cvax['A1'], cvax['A2'], cvax['A3'], cvax['A4'],
                    cvax['A5']], axis=1).reshape(P, 6, 5)
    AX = np.stack([cv['A1XL'], -cv['A1XL'], cv['A3XL'],
                   cv['A4XL'], cv['A5XL']], axis=1)
    Eup = np.einsum('pi,pimn->pmn', A, mb['P0']) \
        + np.einsum('pi,pimn->pmn', AX, mb['P0X'])
    # divergence: axial slot s = 2*i (sign +) / 2*i+1 (sign -), dir i
    for i in range(3):
        sp, sm = 2 * i, 2 * i + 1
        Eup -= (np.einsum('pi,pimn->pmn', Aax[:, sp],
                          mb['P1n'][:, sp, i])
                - np.einsum('pi,pimn->pmn', Aax[:, sm],
                            mb['P1n'][:, sm, i])) / (2 * h)
    Eup *= (2.0 / mb['sqrtg'])[:, None, None]
    g = mb['g']
    Ecov_A = np.einsum('pac,pcd,pdb->pab', g, Eup, g)
    f1 = float(theta[0])
    Ecov = mb['ER0'] + f1 * (-1.0 / (2 * X_ref)) * mb['ER1'] \
        + Ecov_A
    return Ecov, cv


def assemble_scalar_eom(sb, theta, X_ref):
    """Scalar EOM (density-normalised) at collocation points +
    term scale.  sb from scalar_eom_basis."""
    XLs = sb['XL_s']
    P, S = XLs.shape
    Xhats = -XLs / (2 * X_ref)
    cv = E.coeff_values(theta, Xhats.reshape(-1), XLs.reshape(-1),
                        X_ref)
    A = np.stack([cv['A1'], cv['A2'], cv['A3'], cv['A4'], cv['A5']],
                 axis=1).reshape(P, S, 5)
    FXL = np.full((P, S, 1), -float(theta[0]) / (2.0 * X_ref))
    c = np.concatenate([FXL, A], axis=2)       # (P,19,6)
    eom1 = np.einsum('psk,psk->p', sb['W1'], c)
    eom2 = np.einsum('psk,psk->p', sb['W2'], c)
    AXs = np.stack([cv['A1XL'], -cv['A1XL'], cv['A3XL'],
                    cv['A4XL'], cv['A5XL']],
                   axis=1).reshape(P, S, 5)
    eom1x = np.einsum('psk,psk->p', sb['W1X'], AXs)
    fxl = -float(theta[0]) / (2.0 * X_ref)
    eomR = fxl * np.sum(sb['W1R'], axis=1)
    scale = np.abs(eom1) + np.abs(eom2) + np.abs(eom1x) \
        + np.abs(eomR)
    return eom1 + eom2 + eom1x + eomR, scale, eom1, eom2
