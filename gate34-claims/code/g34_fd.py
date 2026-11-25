#!/usr/bin/env python3
"""
g34_fd.py -- Gate-34's finite-difference assembly (GUARD ONLY).

Builds the Einstein tensor from metric VALUES alone
(g34_lib.metric_only), with 5-point central stencils for
first and second spatial derivatives at two step sizes and
Richardson extrapolation on the second derivative. Never
used as a deciding read; exists to catch a conceptual
error in the gate's analytic assembly.
"""
import numpy as np

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi


def _fd_T_at_point(pt, metric_fn, h):
    """T at one point by FD of the metric (stationary)."""
    pt = np.asarray(pt, dtype=DTYPE)
    # stencil points: centre + +-h, +-2h along each spatial axis
    offs = [np.zeros(3)]
    for k in range(3):
        for s in (1, -1, 2, -2):
            o = np.zeros(3); o[k] = s * h
            offs.append(o)
    pts = pt[None, :] + np.array(offs)
    gs = metric_fn(pts)                     # (13,4,4)
    g0 = gs[0]
    # index map: offs[1+4k + j], j=0:+h,1:-h,2:+2h,3:-2h for axis k
    dg = np.zeros((4, 4, 4))                # dg[d,a,b], time row 0
    ddg = np.zeros((4, 4, 4, 4))
    for k in range(3):
        gp1 = gs[1 + 4 * k + 0]; gm1 = gs[1 + 4 * k + 1]
        gp2 = gs[1 + 4 * k + 2]; gm2 = gs[1 + 4 * k + 3]
        dg[k + 1] = (gm2 - 8.0 * gm1 + 8.0 * gp1 - gp2) / (12.0 * h)
        ddg[k + 1, k + 1] = (-gp2 + 16.0 * gp1 - 30.0 * g0
                             + 16.0 * gm1 - gm2) / (12.0 * h ** 2)
    # mixed second derivatives: 2D 5-point via tensor product of
    # the 1D first-derivative stencil applied to dg slices is
    # O(h^4)-inconsistent; use the standard 4-point diagonal
    # stencil (O(h^2)) for the mixed partials only.
    for k in range(3):
        for l in range(k + 1, 3):
            def gp(sk, sl):
                o = np.zeros(3); o[k] = sk * h; o[l] = sl * h
                return metric_fn((pt + o)[None, :])[0]
            val = (gp(1, 1) - gp(1, -1) - gp(-1, 1) + gp(-1, -1)) \
                / (4.0 * h ** 2)
            ddg[k + 1, l + 1] = val
            ddg[l + 1, k + 1] = val
    ginv = np.linalg.inv(g0)
    Gam = 0.5 * (np.einsum('ad,bdc->abc', ginv, dg)
                 + np.einsum('ad,cdb->abc', ginv, dg)
                 - np.einsum('ad,dbc->abc', ginv, dg))
    dginv = -np.einsum('ad,edc,cb->eab', ginv, dg, ginv)
    dGam = (0.5 * (np.einsum('ead,bdc->eabc', dginv, dg)
                   + np.einsum('ead,cdb->eabc', dginv, dg)
                   - np.einsum('ead,dbc->eabc', dginv, dg))
            + 0.5 * (np.einsum('ad,ebdc->eabc', ginv, ddg)
                     + np.einsum('ad,ecdb->eabc', ginv, ddg)
                     - np.einsum('ad,edbc->eabc', ginv, ddg)))
    Ric = (np.einsum('aabd->bd', dGam)
           - np.einsum('daba->bd', dGam)
           + np.einsum('aae,ebd->bd', Gam, Gam)
           - np.einsum('ade,eba->bd', Gam, Gam))
    Rs = float(np.einsum('ab,ab->', ginv, Ric))
    G = Ric - 0.5 * Rs * g0
    return G / EIGHT_PI, g0


def fd_that(pts, metric_fn, eulerian_fn, hs=(0.02, 0.01)):
    """Richardson-extrapolated FD That at each point:
    That_R = (16*T(h/2) - T(h))/15 on the pure second-
    derivative part is not separable here, so instead the
    guard reports both step sizes' That and their spread;
    the caller compares the finer against the analytic."""
    out = {}
    for h in hs:
        Thats = []
        for pt in np.asarray(pts, dtype=DTYPE):
            T, g = _fd_T_at_point(pt, metric_fn, h)
            Thats.append(eulerian_fn(g[None], T[None])[0])
        out[h] = np.array(Thats)
    return out
