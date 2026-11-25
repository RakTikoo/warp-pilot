#!/usr/bin/env python3
"""
g16_audit.py -- GATE-16 fresh auditor (coordinator-written, 2026-11-23).

INDEPENDENCE: this file implements the hinge E_total assembly, the
canonical EoM terms, the relative-residual statistics, the alignment
set, the targeting read, health / Frontier A / trap, and the profile
blends FROM THE REGISTERED FORMULAS (phase128/CHECKPOINT128.md's
registered front; p1015_lib's published docstring). It imports NO
Phase 101/119/128 work code. Datum machinery imported (predates the
claims; defines the bed and base profile): phase76/p761_lib (Wall,
H_of, dH_of, fld_derivs, fluid_T, margins, legal_frac) and
phase18/p182_engine + p182_basis (lag_basis, pi_splines, stencil).
float64.
"""
import json
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

W = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, os.path.join(W, 'phase76'))
sys.path.insert(0, os.path.join(W, 'phase18'))
import p761_lib as L    # noqa: E402
import p182_engine as E  # noqa: E402
import p182_basis as B   # noqa: E402

FLOOR = 1e-9
B76 = json.load(open(os.path.join(W, 'phase76/results/p761_B_1.1.json')))
W_B = float(B76['joint_best']['w'])


# ------------------------------------------------------------------
# Gate-16's own hinge E_total (P value carries (mu/2) phi^2; P_X form
# unchanged) -- assembled here from the registered formula.
# ------------------------------------------------------------------
def hinge_E_total(wall, pts, z, fluid=None):
    xi, bc, b2, pi0, shape, p1, p2, mu = [float(q) for q in z]
    K = wall.kern(pts)
    g, ginv, Gam = K['g'], K['ginv'], K['Gam']
    bed, v, H = wall.phi_jets(pts, pi0, shape)
    sg, basis, aux = E.lag_basis(g, K['dg'], K['ddg'], v, H)
    XL = aux['XL']
    X = -0.5 * XL
    phi = bed.cs(np.clip(np.linalg.norm(pts, axis=1), 0, 60))
    Hf = L.H_of(phi, xi, bc, b2)
    st = B.stencil(pts, 0.3).reshape(-1, 3)
    phis = bed.cs(np.clip(np.linalg.norm(st, axis=1), 0, 60))
    Hs = L.H_of(phis, xi, bc, b2).reshape(len(pts), 19)
    _, HessH = L.fld_derivs(Hs, Gam)
    BoxH = np.einsum('pab,pab->p', ginv, HessH)
    ER = Hf[:, None, None] * K['G'] + HessH - g * BoxH[:, None, None]
    Pval = p1 * X + p2 * X**2 + 0.5 * mu * phi**2
    PX = p1 + 2.0 * p2 * X
    TP = PX[:, None, None] * np.einsum('pa,pb->pab', v, v) \
        + Pval[:, None, None] * g
    Ecov = ER + TP
    if fluid is not None:
        w, rho0 = fluid
        Ecov = Ecov + L.fluid_T(pts, g, w, rho0)
    return Ecov, dict(phi=phi, X=X, PX=PX, H=Hf)


def canonical_terms(wall, pts, z):
    xi, bc, b2, pi0, shape, p1, p2, mu = [float(q) for q in z]
    K = wall.kern(pts)
    ginv = K['ginv']
    bed, v, H = wall.phi_jets(pts, pi0, shape)
    sg, basis, aux = E.lag_basis(K['g'], K['dg'], K['ddg'], v, H)
    X = -0.5 * aux['XL']
    PX = p1 + 2.0 * p2 * X
    PXX = 2.0 * p2
    box = np.einsum('pab,pab->p', ginv, aux['ph'])
    vup = np.einsum('pab,pb->pa', ginv, v)
    hv = np.einsum('pab,pb->pa', aux['ph'], vup)
    vhv = np.einsum('pa,pa->p', vup, hv)
    phi = bed.cs(np.clip(np.linalg.norm(pts, axis=1), 0, 60))
    FA = 0.5 * L.dH_of(phi, xi, bc, b2) * K['Rsc']
    FB = -mu * phi
    with np.errstate(divide='ignore', invalid='ignore'):
        t_kin = box
        t_pxx = np.where(np.abs(PX) > 0, -(PXX / PX) * vhv, 0.0)
        t_FA = np.where(np.abs(PX) > 0, FA / PX, 0.0)
        t_FB = np.where(np.abs(PX) > 0, FB / PX, 0.0)
    return dict(t_kin=t_kin, t_pxx=t_pxx, t_FA=t_FA, t_FB=t_FB,
                FA=FA, FB=FB, phi=phi, PX=PX, X=X, Rsc=K['Rsc'])


def rel_stats(ct):
    tot = ct['t_kin'] + ct['t_pxx'] + ct['t_FA'] + ct['t_FB']
    D = (np.abs(ct['t_kin']) + np.abs(ct['t_pxx'])
         + np.abs(ct['t_FA']) + np.abs(ct['t_FB']))
    rel = np.abs(tot) / (D + 1e-12)
    return rel, D


def alignment_set(ct):
    rel, D = rel_stats(ct)
    tk, tp, tA, tB = ct['t_kin'], ct['t_pxx'], ct['t_FA'], ct['t_FB']
    terms = np.stack([tk, tp, tA, tB])
    maxterm = np.max(np.abs(terms), axis=0)
    idx, detail = [], {}
    for i in range(len(tk)):
        live = (abs(tA[i]) >= 1e-6 * maxterm[i]
                and abs(tB[i]) >= 1e-6 * maxterm[i])
        samesign = (tA[i] * tB[i] > 0)
        SF = (abs(tA[i]) + abs(tB[i])) / D[i] if D[i] > 0 else 0.0
        kin = abs(tk[i]) / D[i] if D[i] > 0 else 0.0
        if live and samesign and SF >= 0.90 and kin <= 1e-6:
            idx.append(int(i))
            detail[int(i)] = dict(
                t_kin=float(tk[i]), t_pxx=float(tp[i]),
                t_FA=float(tA[i]), t_FB=float(tB[i]),
                D_can=float(D[i]), S_F=float(SF),
                kin_share=float(kin), rel_resid=float(rel[i]))
    return idx, detail, rel, D


def targeting_read(ct, points):
    tk, tB = ct['t_kin'], ct['t_FB']
    terms = np.stack([ct['t_kin'], ct['t_pxx'], ct['t_FA'], ct['t_FB']])
    maxterm = np.max(np.abs(terms), axis=0)
    det, n_live, n_opp = {}, 0, 0
    for i in points:
        live = (abs(tk[i]) >= 1e-6 * maxterm[i]
                and abs(tB[i]) >= 1e-6 * maxterm[i])
        opp = bool(live and tk[i] * tB[i] < 0)
        if live:
            n_live += 1
            n_opp += int(opp)
        det[int(i)] = dict(t_kin=float(tk[i]), t_FB=float(tB[i]),
                           live=bool(live), opposed=opp)
    return dict(points=[int(i) for i in points], n_live=n_live,
                n_opposed=n_opp, detail=det)


def full_read(wall, pts, z, fluid=None):
    z = np.asarray(z, dtype=np.float64)
    E, auxE = hinge_E_total(wall, pts, z, fluid)
    K = wall.kern(pts)
    m_fast = L.margins(E, K['g'], fast=True)
    lf_fast, ok_fast = L.legal_frac(m_fast)
    m_full = L.margins(E, K['g'], fast=False)
    lf_full, ok_full = L.legal_frac(m_full)
    ct = canonical_terms(wall, pts, z)
    rel, D = rel_stats(ct)
    nd = D >= FLOOR
    PX, X = ct['PX'], ct['X']
    PXX = 2.0 * float(z[6])
    with np.errstate(divide='ignore', invalid='ignore'):
        cr2 = PX / (PX + 2 * X * PXX)
    cr2f = cr2[np.isfinite(cr2)]
    health = bool(np.min(auxE['H']) > 0 and np.min(PX) > 0
                  and len(cr2f) and cr2f.min() >= 0 and cr2f.max() <= 1)
    xi, bc, b2, mu = float(z[0]), float(z[1]), float(z[2]), float(z[7])
    trap_sub = (abs(bc) < 1e-12 and abs(2 * xi + b2) < 1e-12
                and abs(mu) < 1e-12)
    fsum_max = float(np.max(np.abs(ct['FA'] + ct['FB'])))
    trap = bool(fsum_max < FLOOR or trap_sub)
    frontier = float(lf_fast) if (nd.any()
                                  and float(rel[nd].max()) <= 0.02
                                  and health) else 0.0
    idx, detail, _, _ = alignment_set(ct)
    rel_nd = np.where(nd, rel, -1.0)
    imax = int(np.argmax(rel_nd)) if nd.any() else None
    dec = None
    if imax is not None:
        dec = dict(
            point=imax,
            t_kin=float(ct['t_kin'][imax]), t_pxx=float(ct['t_pxx'][imax]),
            t_FA=float(ct['t_FA'][imax]), t_FB=float(ct['t_FB'][imax]),
            D_can=float(D[imax]), rel_resid=float(rel[imax]),
            phi=float(ct['phi'][imax]), PX=float(ct['PX'][imax]),
            shares=dict(
                kin=float(abs(ct['t_kin'][imax]) / D[imax]),
                pxx=float(abs(ct['t_pxx'][imax]) / D[imax]),
                FA=float(abs(ct['t_FA'][imax]) / D[imax]),
                FB=float(abs(ct['t_FB'][imax]) / D[imax])))
    # near-zero margin points (legality noise audit), fast form
    mall = np.minimum(np.minimum(m_fast['nec'], m_fast['wec']),
                      np.minimum(m_fast['sec'], m_fast['dec']))
    near = [dict(point=int(i), min_margin=float(mall[i]))
            for i in range(len(mall)) if abs(float(mall[i])) < 1e-6]
    return dict(
        z=[float(x) for x in z],
        subset_legal=float(lf_fast), subset_legal_full=float(lf_full),
        n_legal_fast=int(np.sum(ok_fast)), n_legal_full=int(np.sum(ok_full)),
        ec_min_fast={k: float(m_fast[k].min())
                     for k in ('nec', 'wec', 'sec', 'dec')},
        ec_min_full={k: float(m_full[k].min())
                     for k in ('nec', 'wec', 'sec', 'dec')},
        eom_rel_max_nondeg=float(rel[nd].max()) if nd.any() else None,
        eom_rel_med_nondeg=float(np.median(rel[nd])) if nd.any() else None,
        n_nondeg=int(np.sum(nd)), n_deg=int(np.sum(~nd)),
        H_min=float(np.min(auxE['H'])), PX_min=float(np.min(PX)),
        cr2_min=float(cr2f.min()) if len(cr2f) else None,
        cr2_max=float(cr2f.max()) if len(cr2f) else None,
        health_ok=health, Fsum_maxabs=fsum_max, trap_fires=trap,
        frontier_A=frontier, alignment_set=idx,
        alignment_detail=detail, max_resid_point=imax,
        max_resid_in_alignment=bool(imax in idx) if imax is not None else None,
        max_resid_decomp=dec, near_zero_margin_points=near,
        kin_share_former_plateau=[
            float(abs(ct['t_kin'][i]) / D[i]) if D[i] > 0 else 0.0
            for i in range(44)],
        n_plateau_kin_live=int(sum(
            1 for i in range(44)
            if D[i] >= FLOOR and abs(ct['t_kin'][i]) / D[i] > 1e-6)))


# ------------------------------------------------------------------
# Profile blends (gate's own PhiProfile-pattern implementation).
# ------------------------------------------------------------------
def smootherstep(t):
    t = np.clip(np.asarray(t, dtype=np.float64), 0.0, 1.0)
    return t**3 * (10.0 + t * (-15.0 + 6.0 * t))


def window_W(r):
    r = np.asarray(r, dtype=np.float64)
    up = smootherstep((r - 10.0) / 1.25)
    dn = 1.0 - smootherstep((r - 18.75) / 1.25)
    return up * dn


class BlendProfile:
    """phi(r) = wallwide(pi0, shape) + W(r) * blend(r); blend given by
    a callable. Jets by the PhiProfile pattern (CubicSpline, 4001-pt
    grid on [0, 60])."""

    def __init__(self, pi0, shape, blend_fn):
        base_cs, _, _ = E.pi_splines('wallwide', pi0, shape)
        r = np.linspace(0.0, 60.0, 4001)
        vals = base_cs(r) + window_W(r) * blend_fn(r)
        self.cs = CubicSpline(r, vals)
        self.d1 = self.cs.derivative()
        self.d2 = self.cs.derivative(2)

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


class WallBlend(L.Wall):
    """Wall whose phi_jets returns the gate's blend profile.
    blend_fn held in wall.blend_fn."""

    blend_fn = staticmethod(lambda r: np.zeros_like(np.asarray(r, float)))

    def phi_jets(self, pts, pi0, shape):
        if not hasattr(self, '_bl'):
            self._bl = {}
        key = (round(float(pi0), 10), round(float(shape), 10),
               id(self.blend_fn))
        if key not in self._bl:
            if len(self._bl) >= 8:
                self._bl.clear()
            self._bl[key] = BlendProfile(float(pi0), float(shape),
                                         self.blend_fn)
        bed = self._bl[key]
        v, Hh = bed.pi_jets(pts)
        return bed, v, Hh


def sine1(A, lam):
    return lambda r: A * np.sin(2.0 * np.pi * (np.asarray(r, float) - 10.0) / lam)


def sineK(bp):
    def f(r):
        r = np.asarray(r, dtype=np.float64)
        out = np.zeros_like(r)
        for k in range(3):
            A, lam, ph = bp[3 * k], bp[3 * k + 1], bp[3 * k + 2]
            out = out + A * np.sin(2.0 * np.pi * (r - 10.0) / lam + ph)
        return out
    return f
