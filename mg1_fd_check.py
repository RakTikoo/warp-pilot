"""
mg1_fd_check.py — G1 second engine for MG-1: T_m by nested finite
differences (no autodiff), with Richardson error estimate.

At each target point:
  * G_mn and Gamma from the validated FD machinery (vm.einstein_at_points,
    vm._gamma_at) with step h1; R = -tr(G).
  * F = 1 + 2 alpha R evaluated on a 4th-order FD stencil of radius h2
    (each F value needs its own Einstein evaluation -> nested stencils).
  * nabla nabla F = ddF - Gamma.dF ; Box F = g^mn nabla_m nabla_n F.
  * R_mn = G_mn + (1/2) R g_mn ;
    8 pi T_m = F R_mn - (1/2)(R + alpha R^2) g_mn - nabla nabla F + g_mn Box F.
Richardson: two (h1, h2) pairs; error ~ |T(h) - T(h/2)| / (2^2 - 1)
(conservative order p=2 for the nested scheme).
"""
import numpy as np
import verify_metric as vm

EIGHT_PI = 8.0 * np.pi
C4 = np.array([1.0, -8.0, 0.0, 8.0, -1.0]) / 12.0     # 4th-order 1st deriv
C4D2 = np.array([-1.0, 16.0, -30.0, 16.0, -1.0]) / 12.0  # 4th-order 2nd deriv


def _R_at(gfunc, pts, h1):
    G, That, m = vm.einstein_at_points(gfunc, np.atleast_2d(pts), h=h1,
                                       do_fallback=False)
    g = gfunc(np.atleast_2d(pts))
    gi = np.linalg.inv(g)
    R = -np.einsum('pab,pba->p', gi, G)
    return R, G, g, gi


def Tm_FD(gfunc, pt, alpha, h1, h2):
    pt = np.asarray(pt, dtype=float)
    # centre quantities
    Gamma, g, gi = vm._gamma_at(gfunc, pt[None], h1)
    Gamma = Gamma[0]; g = g[0]; gi = gi[0]
    R0, G0, _, _ = _R_at(gfunc, pt[None], h1)
    R0 = R0[0]; G0 = G0[0]
    Ric = G0 + 0.5 * R0 * g
    # F on stencil: offsets k*h2, k in -2..2 per spatial axis
    offs = np.arange(-2, 3)
    Fvals = {}
    allpts = []
    keys = []
    for a in range(3):
        for k in offs:
            if k == 0:
                continue
            p = pt.copy(); p[a] += k * h2
            allpts.append(p); keys.append(('ax', a, k))
    for a in range(3):
        for b in range(a + 1, 3):
            for ka in (-1, 1):
                for kb in (-1, 1):
                    p = pt.copy(); p[a] += ka * h2; p[b] += kb * h2
                    allpts.append(p); keys.append(('mix', a, b, ka, kb))
    Rall, _, _, _ = _R_at(gfunc, np.array(allpts), h1)
    Fall = 1.0 + 2.0 * alpha * Rall
    Fmap = {key: Fall[i] for i, key in enumerate(keys)}
    F0 = 1.0 + 2.0 * alpha * R0
    dF = np.zeros(4)
    ddF = np.zeros((4, 4))
    for a in range(3):
        vals = np.array([Fmap[('ax', a, k)] if k != 0 else F0 for k in offs])
        dF[a + 1] = np.sum(C4 * vals) / h2
        ddF[a + 1, a + 1] = np.sum(C4D2 * vals) / h2 ** 2
    for a in range(3):
        for b in range(a + 1, 3):
            fpp = Fmap[('mix', a, b, 1, 1)]; fpm = Fmap[('mix', a, b, 1, -1)]
            fmp = Fmap[('mix', a, b, -1, 1)]; fmm = Fmap[('mix', a, b, -1, -1)]
            ddF[a + 1, b + 1] = ddF[b + 1, a + 1] = (fpp - fpm - fmp + fmm) / (4 * h2 ** 2)
    nabnabF = ddF - np.einsum('lmn,l->mn', Gamma, dF)
    boxF = np.einsum('mn,mn->', gi, nabnabF)
    f = R0 + alpha * R0 ** 2
    Tm = (F0 * Ric - 0.5 * f * g - nabnabF + g * boxF) / EIGHT_PI
    return Tm


def Tm_FD_richardson(gfunc, pt, alpha, h1=0.1, h2=0.2):
    T1 = Tm_FD(gfunc, pt, alpha, h1, h2)
    T2 = Tm_FD(gfunc, pt, alpha, h1 / 2, h2 / 2)
    err = np.max(np.abs(T1 - T2)) / 3.0
    return T2, err
