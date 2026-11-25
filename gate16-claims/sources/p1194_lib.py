#!/usr/bin/env python3
"""
p1194_lib.py -- P119-4 shared machinery.

- Gate/alignment helpers on p1015_lib.canonical_terms.
- WallNF: Wall with the non-flat blend profile of the run
  record S2 (closed-form blend, PhiProfile-pattern jets).
- Residuals in the p1015_partB pattern (p791_main form).
float64.
"""
import json
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, os.path.join(W, 'phase101/work'))
sys.path.insert(0, os.path.join(W, 'phase79'))
sys.path.insert(0, os.path.join(W, 'phase76'))
sys.path.insert(0, os.path.join(W, 'phase18'))
import p761_lib as L      # noqa: E402
import p1015_lib as H     # noqa: E402
import p182_engine as E   # noqa: E402
import shell as sh        # noqa: E402

BETA = 1.1
HINGE_Z = np.array([2.756667559450937, -1.498683175695639,
                    0.7811507949670238, 0.3385988091052908,
                    0.870145941019083, 1.222294121969537,
                    0.0639057960421364, -0.15512773896022752])
HINGE_RHO = 0.046611949162594764
HINGE_LEGAL = 0.5892857142857143
HINGE_EMAX = 0.9999999999784565

B76 = json.load(open(os.path.join(W, 'phase76/results/p761_B_1.1.json')))
W_B = float(B76['joint_best']['w'])

LO8 = np.array([0.0, -2.0, -2.0, 0.0, 0.85, -3.0, -3.0, -3.0])
HI8 = np.array([5.0, 4.0, 2.0, 3.0, 1.15, 3.0, 3.0, 3.0])


def alignment_set(ct):
    """Registered definition (CHECKPOINT119 S P119-4):
    nondeg point; both force terms live >= 1e-6 * max|term|
    at the point; same strict sign; S_F >= 0.90;
    |t_kin|/D_can <= 1e-6. Returns (indices, per-point detail,
    residual array, D array)."""
    tk, tp, tA, tB = ct['t_kin'], ct['t_pxx'], ct['t_FA'], ct['t_FB']
    terms = np.stack([tk, tp, tA, tB])
    D = np.sum(np.abs(terms), axis=0)
    tot = np.sum(terms, axis=0)
    rel = np.abs(tot) / (D + 1e-12)
    maxterm = np.max(np.abs(terms), axis=0)
    idx, detail = [], {}
    for i in range(len(D)):
        if D[i] < H.FLOOR:
            continue
        live = (abs(tA[i]) >= 1e-6 * maxterm[i]
                and abs(tB[i]) >= 1e-6 * maxterm[i])
        samesign = (tA[i] * tB[i] > 0)
        SF = (abs(tA[i]) + abs(tB[i])) / D[i]
        kin = abs(tk[i]) / D[i]
        if live and samesign and SF >= 0.90 and kin <= 1e-6:
            idx.append(int(i))
            detail[int(i)] = dict(
                t_kin=float(tk[i]), t_pxx=float(tp[i]),
                t_FA=float(tA[i]), t_FB=float(tB[i]),
                D_can=float(D[i]), S_F=float(SF),
                kin_share=float(kin), rel_resid=float(rel[i]))
    return idx, detail, rel, D


def full_read(wall, pts, z, fluid=None):
    """p1015_lib.read + alignment anatomy at one candidate."""
    r = H.read(wall, pts, z, fluid)
    ct = H.canonical_terms(wall, pts, z)
    idx, detail, rel, D = alignment_set(ct)
    nd = D >= H.FLOOR
    rel_nd = np.where(nd, rel, -1.0)
    imax = int(np.argmax(rel_nd)) if nd.any() else None
    dec = None
    if imax is not None:
        dec = dict(point=imax,
                   t_kin=float(ct['t_kin'][imax]),
                   t_pxx=float(ct['t_pxx'][imax]),
                   t_FA=float(ct['t_FA'][imax]),
                   t_FB=float(ct['t_FB'][imax]),
                   D_can=float(D[imax]), rel_resid=float(rel[imax]),
                   phi=float(ct['phi'][imax]),
                   PX=float(ct['PX'][imax]),
                   shares=dict(
                       kin=float(abs(ct['t_kin'][imax]) / D[imax]),
                       pxx=float(abs(ct['t_pxx'][imax]) / D[imax]),
                       FA=float(abs(ct['t_FA'][imax]) / D[imax]),
                       FB=float(abs(ct['t_FB'][imax]) / D[imax])))
    r['alignment_set'] = idx
    r['alignment_detail'] = detail
    r['max_resid_point'] = imax
    r['max_resid_in_alignment'] = bool(imax in idx) if imax is not None else None
    r['max_resid_decomp'] = dec
    r['kin_share_former_plateau'] = [
        float(abs(ct['t_kin'][i]) / D[i]) if D[i] > 0 else 0.0
        for i in range(44)]
    r['n_plateau_kin_live'] = int(sum(
        1 for i in range(44)
        if D[i] >= H.FLOOR and abs(ct['t_kin'][i]) / D[i] > 1e-6))
    return r


# ==================================================================
# Non-flat profile (run record S2)
# ==================================================================

def _window(r):
    up = sh.smootherstep((r - 10.0) / 1.25)
    dn = 1.0 - sh.smootherstep((r - 18.75) / 1.25)
    return up * dn


class NFProfile:
    """phi(r) = wallwide(pi0, shape) + A * W(r) * sin(2 pi (r-10)/lam).
    CubicSpline on the pi_splines 4001-pt grid; d1/d2 spline
    derivatives; pi_jets verbatim from PhiProfile."""

    def __init__(self, pi0, shape, A, lam):
        base_cs, _, _ = E.pi_splines('wallwide', pi0, shape)
        r = np.linspace(0.0, 60.0, 4001)
        vals = base_cs(r) + A * _window(r) * np.sin(
            2.0 * np.pi * (r - 10.0) / lam)
        self.cs = CubicSpline(r, vals)
        self.d1 = self.cs.derivative()
        self.d2 = self.cs.derivative(2)
        self.A, self.lam = float(A), float(lam)

    def pi_jets(self, pts):
        pts = np.asarray(pts, dtype=np.float64)
        r = np.linalg.norm(pts, axis=1)
        rs = np.where(r > 0, r, 1.0)
        n = pts / rs[:, None]
        rc = np.clip(r, 0.0, 60.0)
        pip, pipp = self.d1(rc), self.d2(rc)
        P = len(pts)
        v = np.zeros((P, 4))
        v[:, 1:] = pip[:, None] * n
        Hh = np.zeros((P, 4, 4))
        coef = np.where(r > 0, pip / rs, 0.0)
        for i in range(3):
            for j in range(3):
                Hh[:, 1 + i, 1 + j] = pipp * n[:, i] * n[:, j] \
                    + coef * ((1.0 if i == j else 0.0)
                              - n[:, i] * n[:, j])
        return v, Hh


class WallNF(L.Wall):
    """Wall whose phi_jets returns the NF blend profile.
    Profile parameters held in wall.prof_A / wall.prof_lam."""

    prof_A = 0.15
    prof_lam = 3.0

    def phi_jets(self, pts, pi0, shape):
        if not hasattr(self, '_nf'):
            self._nf = {}
        key = (round(float(pi0), 10), round(float(shape), 10),
               round(float(self.prof_A), 10),
               round(float(self.prof_lam), 10))
        if key not in self._nf:
            self._nf[key] = NFProfile(float(pi0), float(shape),
                                      float(self.prof_A),
                                      float(self.prof_lam))
        bed = self._nf[key]
        v, Hh = bed.pi_jets(pts)
        return bed, v, Hh


# ==================================================================
# Residuals (p1015_partB pattern)
# ==================================================================

def ec_scale(wall, pts):
    Egr, _ = wall.E_total(pts, (0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0))
    mgr = L.margins(Egr, wall.kern(pts)['g'], fast=True)
    return {k: max(abs(float(mgr[k].min())), 1e-12)
            for k in ('nec', 'wec', 'sec', 'dec')}


def residuals_gen(wall, pts, g_sub, scale, z8, fluid):
    E, auxE = H.hinge_E_total(wall, pts, z8, fluid)
    m = L.margins(E, g_sub, fast=True)
    hinge = lambda mm, s: np.minimum(mm, 0.0) / s  # noqa: E731
    ec = np.concatenate([hinge(m[k], scale[k])
                         for k in ('nec', 'wec', 'sec', 'dec')])
    ct = H.canonical_terms(wall, pts, z8)
    tot = ct['t_kin'] + ct['t_pxx'] + ct['t_FA'] + ct['t_FB']
    D = (np.abs(ct['t_kin']) + np.abs(ct['t_pxx'])
         + np.abs(ct['t_FA']) + np.abs(ct['t_FB']))
    rel = np.abs(tot) / (D + 1e-12)
    eom = np.where(D >= H.FLOOR, rel, 0.0)
    PX, X = ct['PX'], ct['X']
    PXX = 2.0 * float(z8[6])
    with np.errstate(divide='ignore', invalid='ignore'):
        cr2 = PX / (PX + 2 * X * PXX)
    cr2f = cr2[np.isfinite(cr2)]
    hv = np.array([min(float(np.min(auxE['H'])), 0.0),
                   min(float(np.min(PX)), 0.0),
                   min(float(cr2f.min()) if len(cr2f) else -1.0, 0.0),
                   min(1.0 - (float(cr2f.max()) if len(cr2f) else 2.0), 0.0)])
    return np.concatenate([eom, 50.0 * ec, 50.0 * hv])
