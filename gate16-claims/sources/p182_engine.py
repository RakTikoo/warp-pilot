#!/usr/bin/env python3
"""
p182_engine.py -- P18-2 DHOST class-Ia engine (built by P18-2 worker;
no P18-1 engine existed in phase18/ at start -- recorded in run record).

Action (registered, CHECKPOINT18.md):  L = F R + sum_i A_i L_i,
  L1 = phi_mn phi^mn,  L2 = (Box phi)^2,
  L3 = Box phi * phi^m phi_mn phi^n,
  L4 = phi^m phi_mr phi^rn phi_n,  L5 = (phi^m phi_mn phi^n)^2,
  X_L := phi_m phi^m  (Langlois convention),
  X_p := -X_L/2       (programme convention, p61 Sector.X),
  Xhat := X_p / X_ref.
  F  = 1/2 + f1 * Xhat
  A1 = a10 + a11 * Xhat,  A3 = a30 + a31 * Xhat,  A2 = -A1,
  A4, A5 from the published class-Ia degeneracy formulas
  (Boumaza & Langlois, arXiv:2207.13624, eq. above (2.2);
   Langlois review 1811.06271):
    A4 = [ A1 A3 (12 X F - 16 X^2 F_X) + 4 A1^2 (16 X F_X + 3 F)
           - 16 A1 (4 X F_X + 3 F) F_X - 16 X A1^3
           + 8 A3 F (X F_X - F) - X^2 A3^2 F + 48 F F_X^2 ]
         / (8 (F - X A1)^2)
    A5 = (4 F_X - 2 A1 + X A3)(4 A1 F_X - 3 X A1 A3 - 2 A1^2
           + 4 F A3) / (8 (F - X A1)^2)
  with X = X_L and F_X = dF/dX_L there.
  Algebraic checks (run in p182_run.py): A1=0 limit reproduces
  Langlois review (1711.07403) eq. (7); the beyond-Horndeski slice
  A3 = -4 F_X / X_L gives A4 = +4 F_X / X_L, A5 = 0 (Boumaza eq. (3)).

Method: EOM tensors by Euler-Lagrange finite differences on the
field jets (g, dg, ddg, dphi, ddphi):
  - F*R sector: analytic programme form (p61 convention)
    E_R,ab = 2 F G_ab + 2 (nabla_a nabla_b - g_ab Box) F.
  - A_i sectors: E_i via EL in (g^mn, d g^mn) jet variables
    (P0 - div P1), scalar EOM via EL in (dphi, ddphi) jet
    variables (-div P1 + divdiv P2).  All FD partials are taken
    on the LAGRANGIAN BASIS (R, L1..L5), so every EOM quantity
    is a linear functional of the coefficient values
    (F, A_i) at stencil points -- the optimiser assembles
    residuals by dot products against precomputed basis weights.
float64.  System python3.
"""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase6')
import shell as sh            # noqa: E402
import verify_metric as vm    # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402

EIGHT_PI = 8.0 * np.pi
R1, R2 = 10.0, 20.0
PROFILES = {'wallarch': (8.0, 12.0, 12.0, 16.0),
            'wallwide': (8.0, 12.0, 16.0, 22.0)}
CENTRE = {'wallarch': 12.0, 'wallwide': 15.0}

SYM = [(a, b) for a in range(4) for b in range(a, 4)]  # 10 pairs


# ------------------------------------------------------------------
# coefficients
# ------------------------------------------------------------------
def coeff_values(theta, Xhat, X_L, X_ref):
    """All coefficient values + X_L-derivatives at points.
    theta = (f1, a10, a11, a30, a31).  Returns dict of arrays."""
    f1, a10, a11, a30, a31 = [float(t) for t in theta]
    F = 0.5 + f1 * Xhat
    FXL = np.full_like(Xhat, -f1 / (2.0 * X_ref))       # dF/dX_L
    A1 = a10 + a11 * Xhat
    A1XL = np.full_like(Xhat, -a11 / (2.0 * X_ref))
    A3 = a30 + a31 * Xhat
    A3XL = np.full_like(Xhat, -a31 / (2.0 * X_ref))
    X = X_L
    A4, A5 = _A45(F, FXL, A1, A3, X)
    # total X_L-derivatives of A4/A5 along the theory functions
    # (central FD in X_L; F, A1, A3 follow their Xhat dependence)
    dX = 1e-6 * np.maximum(1.0, np.abs(X))
    Fp = 0.5 + f1 * (-(X + dX) / (2.0 * X_ref))
    Fm = 0.5 + f1 * (-(X - dX) / (2.0 * X_ref))
    A1p = a10 + a11 * (-(X + dX) / (2.0 * X_ref))
    A1m = a10 + a11 * (-(X - dX) / (2.0 * X_ref))
    A3p = a30 + a31 * (-(X + dX) / (2.0 * X_ref))
    A3m = a30 + a31 * (-(X - dX) / (2.0 * X_ref))
    A4p, A5p = _A45(Fp, FXL, A1p, A3p, X + dX)
    A4m, A5m = _A45(Fm, FXL, A1m, A3m, X - dX)
    return dict(F=F, FXL=FXL, A1=A1, A2=-A1, A3=A3, A4=A4, A5=A5,
                A1XL=A1XL, A3XL=A3XL,
                A4XL=(A4p - A4m) / (2 * dX),
                A5XL=(A5p - A5m) / (2 * dX))


def _A45(F, FXL, A1, A3, X):
    den = 8.0 * (F - X * A1) ** 2
    A4 = (A1 * A3 * (12.0 * X * F - 16.0 * X**2 * FXL)
          + 4.0 * A1**2 * (16.0 * X * FXL + 3.0 * F)
          - 16.0 * A1 * (4.0 * X * FXL + 3.0 * F) * FXL
          - 16.0 * X * A1**3
          + 8.0 * A3 * F * (X * FXL - F)
          - X**2 * A3**2 * F + 48.0 * F * FXL**2) / den
    A5 = ((4.0 * FXL - 2.0 * A1 + X * A3)
          * (4.0 * A1 * FXL - 3.0 * X * A1 * A3 - 2.0 * A1**2
             + 4.0 * F * A3)) / den
    return A4, A5


def cT2_of(theta, Xhat, X_L, X_ref):
    """Tensor speed^2: ADM L = (F - X_L A1) K^2 + F R3 (Langlois
    review eq. (5)) -> c_T^2 = F / (F - X_L A1)."""
    cv = coeff_values(theta, Xhat, X_L, X_ref)
    FT = cv['F'] - X_L * cv['A1']
    return cv['F'] / FT, FT


# ------------------------------------------------------------------
# profile
# ------------------------------------------------------------------
def pi_splines(profile, pi0, shape):
    a, b, c, d = PROFILES[profile]
    cen = CENTRE[profile]
    r = np.linspace(0.0, 60.0, 4001)
    rr = cen + (r - cen) * shape
    prof = sh.smootherstep((rr - a) / (b - a)) \
        * (1.0 - sh.smootherstep((rr - c) / (d - c)))
    cs = CubicSpline(r, pi0 * prof)
    return cs, cs.derivative(), cs.derivative(2)


class Bed:
    """Metric factory + pi jets for one (beta, profile, pi0, shape)."""

    def __init__(self, beta, profile, pi0, shape):
        self.beta, self.profile = beta, profile
        self.pi0, self.shape = pi0, shape
        prof = sh.build_shell(R1, R2, 2.0, kind='edgepeaked',
                              params={'wd': 3.0, 'floor': 0.2},
                              s_rho=2.0, s_P=1.16, Nr=4001)
        self.gf = sh.shell_point_factory(prof, beta, 'cos', 1.0,
                                         [R1, R2])
        self.cs, self.d1, self.d2 = pi_splines(profile, pi0, shape)

    def pi_jets(self, pts):
        """(v_a = d_a pi, H_ab = d_a d_b pi) partial derivatives."""
        pts = np.asarray(pts, dtype=np.float64)
        r = np.linalg.norm(pts, axis=1)
        rs = np.where(r > 0, r, 1.0)
        n = pts / rs[:, None]
        rc = np.clip(r, 0.0, 60.0)
        pip, pipp = self.d1(rc), self.d2(rc)
        P = len(pts)
        v = np.zeros((P, 4))
        v[:, 1:] = pip[:, None] * n
        H = np.zeros((P, 4, 4))
        coef = np.where(r > 0, pip / rs, 0.0)
        for i in range(3):
            for j in range(3):
                H[:, 1 + i, 1 + j] = pipp * n[:, i] * n[:, j] \
                    + coef * ((1.0 if i == j else 0.0)
                              - n[:, i] * n[:, j])
        return v, H

    def X_fields(self, pts):
        """X_L, X_p at points (from gf + spline)."""
        g = self.gf(pts)
        ginv = np.linalg.inv(g)
        v, _ = self.pi_jets(pts)
        XL = np.einsum('pab,pa,pb->p', ginv, v, v)
        return XL, -0.5 * XL, g, ginv, v


def metric_jets(gf, pts, h=0.3):
    """(g, dg[e], ddg[e,f]) by central FD of the metric factory."""
    pts = np.asarray(pts, dtype=np.float64)
    P = len(pts)
    g0 = gf(pts)
    dg = np.zeros((P, 4, 4, 4))
    ddg = np.zeros((P, 4, 4, 4, 4))
    gp, gm = {}, {}
    for e in range(4):
        off = np.zeros(3); 
        if e > 0:
            off[e - 1] = h
        pp = pts + off if e > 0 else pts.copy()
        pm = pts - off if e > 0 else pts.copy()
        if e == 0:
            gp[e] = gm[e] = g0
        else:
            gp[e] = gf(pp); gm[e] = gf(pm)
        dg[:, e] = (gp[e] - gm[e]) / (2 * h) if e > 0 else 0.0
        ddg[:, e, e] = (gp[e] - 2 * g0 + gm[e]) / h**2 if e > 0 else 0.0
    for e in range(1, 4):
        for f in range(e + 1, 4):
            oe = np.zeros(3); oe[e - 1] = h
            of = np.zeros(3); of[f - 1] = h
            gpp = gf(pts + oe + of); gpm = gf(pts + oe - of)
            gmp = gf(pts - oe + of); gmm = gf(pts - oe - of)
            ddg[:, e, f] = ddg[:, f, e] = \
                (gpp - gpm - gmp + gmm) / (4 * h**2)
    return g0, dg, ddg


# ------------------------------------------------------------------
# Lagrangian basis from jets
# ------------------------------------------------------------------
def lag_basis(g, dg, ddg, v, H):
    """Returns (sqrtg, basis) with basis (...,6) = (R, L1..L5).
    Jets: g (...,4,4); dg (...,e,4,4) = d_e g; ddg (...,e,f,4,4);
    v (...,4); H (...,4,4) partial second derivatives of phi."""
    ginv = np.linalg.inv(g)
    sqrtg = np.sqrt(np.abs(np.linalg.det(g)))
    # d_e ginv
    dginv = -np.einsum('...ac,...ecd,...db->...eab', ginv, dg, ginv)
    # Gamma^c_ab ; term_{ab d} = d_a g_{db} + d_b g_{da} - d_d g_{ab}
    term = (np.einsum('...adb->...abd', dg)
            + np.einsum('...bda->...abd', dg)
            - np.einsum('...dab->...abd', dg))
    Gam = 0.5 * np.einsum('...cd,...abd->...abc', ginv, term)
    # d_e Gamma^c_ab
    dterm = (np.einsum('...eadb->...eabd', ddg)
             + np.einsum('...ebda->...eabd', ddg)
             - np.einsum('...edab->...eabd', ddg))
    dGam = 0.5 * (np.einsum('...ecd,...abd->...eabc', dginv, term)
                  + np.einsum('...cd,...eabd->...eabc', ginv, dterm))
    # R^r_{s m n} = d_m Gam^r_{ns} - d_n Gam^r_{ms} + Gam Gam - Gam Gam
    Riem = (np.einsum('...mnsr->...rsmn', dGam)
            - np.einsum('...nmsr->...rsmn', dGam)
            + np.einsum('...mlr,...nsl->...rsmn', Gam, Gam)
            - np.einsum('...nlr,...msl->...rsmn', Gam, Gam))
    Ric = np.einsum('...rsrn->...sn', Riem)
    R = np.einsum('...sn,...sn->...', ginv, Ric)
    # phi_mn covariant
    ph = H - np.einsum('...abc,...c->...ab', Gam, v)
    vup = np.einsum('...ab,...b->...a', ginv, v)
    XL = np.einsum('...a,...a->...', v, vup)
    phup = np.einsum('...ac,...bd,...cd->...ab', ginv, ginv, ph)
    L1 = np.einsum('...ab,...ab->...', ph, phup)
    box = np.einsum('...ab,...ab->...', ginv, ph)
    L2 = box**2
    hv = np.einsum('...ab,...b->...a', ph, vup)          # phi_m^n v_n cov
    vhv = np.einsum('...a,...a->...', vup, hv)
    L3 = box * vhv
    # L4 = v^m ph_mr ph^rn v_n (ph^rn = contravariant phup)
    L4 = np.einsum('...m,...mr,...rn,...n->...', vup, ph, phup, v)
    L5 = vhv**2
    basis = np.stack([R, L1, L2, L3, L4, L5], axis=-1)
    return sqrtg, basis, dict(ginv=ginv, Gam=Gam, ph=ph, XL=XL,
                              Ric=Ric)


def lag_density(g, dg, ddg, v, H, coeffs6):
    """sqrt(-g) * sum_k coeffs6_k * basis_k ; coeffs6 (...,6)."""
    sqrtg, basis, _ = lag_basis(g, dg, ddg, v, H)
    return sqrtg * np.einsum('...k,...k->...', basis, coeffs6)


# ------------------------------------------------------------------
# jet conversion: (ginv, dginv, ddginv) -> (g, dg, ddg)
# ------------------------------------------------------------------
def jets_from_ginv(ginv, dginv, ddginv):
    g = np.linalg.inv(ginv)
    dg = -np.einsum('...ac,...ecd,...db->...eab', g, dginv, g)
    # ddg_{ef} = g G_e g G_f g - g G_{ef} g + g G_f g G_e g
    # (staged contractions: the flat 5-operand einsum has a
    # pathological contraction path in numpy)
    M = np.einsum('...ac,...ecd,...db->...eab', g, dginv, g)
    t1 = np.einsum('...eac,...fcd,...db->...efab', M, dginv, g)
    t2 = -np.einsum('...ac,...efcd,...db->...efab', g, ddginv, g)
    t3 = np.einsum('...fac,...ecd,...db->...efab', M, dginv, g)
    ddg = t1 + t2 + t3
    return g, dg, ddg


def jets_to_ginv(g, dg, ddg):
    ginv = np.linalg.inv(g)
    dginv = -np.einsum('...ac,...ecd,...db->...eab', ginv, dg, ginv)
    # invert ddg relation: ddginv from ddg via same formula applied
    # with (g<->ginv) roles: ddg formula is symmetric under exchange
    ddginv = np.zeros_like(ddg)
    # Use: g_{ef} pieces: solve by applying jets_from_ginv formula to
    # (ginv, dginv, X) and matching ddg -> X = ddginv satisfies
    # ddg = A(X) + quad(dginv); A linear: X -> -g X g pairs.
    # Compute quad part with ddginv=0, then invert the linear map.
    _, _, ddg_quad = jets_from_ginv(ginv, dginv,
                                    np.zeros_like(ddg))
    resid = ddg - ddg_quad          # = -g * ddginv * g (per e,f)
    ddginv = -np.einsum('...ac,...efcd,...db->...efab',
                        ginv, resid, ginv)
    return ginv, dginv, ddginv
