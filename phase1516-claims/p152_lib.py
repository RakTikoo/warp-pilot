#!/usr/bin/env python3
"""
p152_lib.py -- Phase 15 SA-2 (symmetron-screened Einstein-aether)
shared machinery.  Registration: CHECKPOINT15.md (SA-2 block +
continuation clarifications C1-C7).

Screening sector (operative symmetron formulas, clarification C1):
  Q = Q1 + Q2 >= 0 built from nabla u (tilted u, wwall):
    Q2 = A4 = a^c a_c,
    Q1 = || P . (nabla u) . P ||^2,  P^a_b = delta^a_b + u^a u_b
         on both indices of nabla_a u_b, contracted with ginv.
  U_eff = 1/2 (m^2 - lam Q) chi^2 + (mu/4) chi^4,
  chi(x) = 0 for Q <= Q_crit, sqrt((lam Q - m^2)/mu) above.
  lam = 1, m^2 = Q_crit, mu = 2 Q_crit / chi_v^2, chi_v = 3,
  Q_crit = 30 x max Q on the bed exterior (C3 sampling).
  S(chi) = chi^2/(chi^2+1);  c_i(x) = S(x) * c0_i.
Q carries no c0 dependence: one (chi, S) field per beta.

float64.  System python3.
"""
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase6')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase9')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase10')
import shell as sh            # noqa: E402
import verify_metric as vm    # noqa: E402
from verify_finalist import dense_points  # noqa: E402
import p61_scan as p61        # noqa: E402
import p93_tensor as tn       # noqa: E402
import p102_lib as lib102     # noqa: E402

EIGHT_PI = 8.0 * np.pi
R1, R2 = 10.0, 20.0
U_TILT = lib102.TILTS['wwall']
LAM = 1.0
CHI_V = 3.0
ROWS = [(0.2, 1.0, 1.0), (0.2, 0.3, 1.0), (0.5, 1.0, 1.0),
        (0.2, 1.0, 0.5), (0.5, 0.3, 0.5), (0.8, 1.0, 1.0),
        (0.2, 0.0, 0.2), (0.0, 1.0, 0.2)]


def cs_of(c1, c2, c14):
    return (c1, c2, -c1, c14 - c1)


def bed_gf(beta):
    prof = sh.build_shell(R1, R2, 2.0, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    return sh.shell_point_factory(prof, beta, 'cos', 1.0, [R1, R2])


def bed(beta):
    """Binding set + volume set + GR fields for one beta."""
    gf = bed_gf(beta)
    pts = dense_points()
    sec = p61.Sector(gf, pts, 0.3, 1.0)
    nec_s, n_hat = p61.binding_directions(sec.That_GR)
    r_pts = np.linalg.norm(pts, axis=1)
    deficit = -nec_s
    band = (r_pts >= 9.0) & (r_pts <= 21.0) & (deficit > 0)
    maxdef = float(np.max(deficit[band]))
    bind = band & (deficit >= 0.5 * maxdef)
    vol = (r_pts >= 9.0) & (r_pts <= 21.0)
    return dict(
        gf=gf, sec=sec,
        pts_b=pts[bind], n_b=n_hat[bind], r_b=r_pts[bind],
        D_that=deficit[bind],
        Gkk_raw=p61.null_contract(sec.That_GR, n_hat)[bind]
        * EIGHT_PI,
        That_GR_b=sec.That_GR[bind], g_b=sec.g[bind],
        maxdef=maxdef, n_bind=int(bind.sum()),
        pts_v=pts[vol], r_v=r_pts[vol],
        That_GR_v=sec.That_GR[vol], g_v=sec.g[vol],
        n_vol=int(vol.sum()))


def Q_of_field(fc):
    """Q = Q1 + Q2 from a tn.field dict (any u factory)."""
    g, ginv = fc['g'], fc['ginv']
    u_up, u_cov = fc['u_up'], fc['u_cov']
    Dcov = fc['Dcov']                       # nabla_a u_b
    Pmix = np.eye(4)[None] + np.einsum('pa,pb->pab', u_up, u_cov)
    # M_ab = P^c_a D_cd P^d_b  (projector on both indices)
    M = np.einsum('pca,pcd,pdb->pab', Pmix, Dcov, Pmix)
    Q1 = np.einsum('pab,pcd,pac,pbd->p', M, M, ginv, ginv)
    Q2 = fc['A'][3]                          # a^c a_c
    return Q1 + Q2, Q1, Q2


def Q_at(gf, pts, u_of=U_TILT, h_fd=0.15):
    fc = tn.field(gf, pts, 0.3, u_of, (0.0, 0.0, 0.0, 0.0),
                  h_fd=h_fd)
    return Q_of_field(fc)


def exterior_points():
    """C3: p151-style 60-pt set (seed 15) + denser fib set."""
    rng = np.random.default_rng(15)
    dirs = rng.normal(size=(60, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    rad = rng.uniform(60.0, 90.0, 60)
    pts_a = dirs * rad[:, None]
    fd = p61.fib_dirs(26)
    pts_b = np.concatenate([fd * r for r in (62.0, 70.0, 80.0, 90.0)])
    return pts_a, pts_b


def q_crit(gf11=None):
    """Q_crit from the beta=1.1 bed exterior (C3 union rule)."""
    if gf11 is None:
        gf11 = bed_gf(1.1)
    pa, pb = exterior_points()
    Qa, _, _ = Q_at(gf11, pa)
    Qb, _, _ = Q_at(gf11, pb)
    mx_a, mx_b = float(np.max(Qa)), float(np.max(Qb))
    qc = 30.0 * max(mx_a, mx_b)
    return qc, dict(max_Q_p151_set=mx_a, max_Q_fib_set=mx_b,
                    Q_crit=qc)


def chi_S(Q, qc):
    """Adiabatic symmetron solve: returns (chi, S)."""
    Q = np.asarray(Q, dtype=np.float64)
    mu = 2.0 * qc / CHI_V**2
    chi = np.where(Q > qc,
                   np.sqrt(np.maximum(LAM * Q - qc, 0.0) / mu), 0.0)
    S = chi**2 / (chi**2 + 1.0)
    return chi, S


def mink_gf(pts):
    P = len(pts)
    g = np.zeros((P, 4, 4))
    g[:, 0, 0] = -1.0
    g[:, 1, 1] = g[:, 2, 2] = g[:, 3, 3] = 1.0
    return g
