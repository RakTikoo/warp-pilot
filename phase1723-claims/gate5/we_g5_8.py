"""
we_g5_8.py — Gate-5 worker W-E: INDEPENDENT verification of claim G5-8
(Phase 17 formation paths: morphs M1/M3, ramps, destination ceiling).

Fresh deciding machinery, written from the CLAIM STATEMENT only.
Deliberate differences from the Phase 7/16/17 deciding machinery
(neither p74_auditor.py, p161_dynamic.py, p172_morph.py nor
p173_ramp.py is imported or re-run; stored JSONs are read only in the
final comparison step, never by the audit code):

  * Finite differences: SECOND-order central stencils (offsets +-1)
    for dg and dGamma, in time and space. (Phase 7 used 4th-order.)
    Accuracy established by an explicit h-scan on the stationary
    control (h = 0.30, 0.15, 0.075).
  * Morph lambda-interpolation: LOCAL 4-point Lagrange interpolation
    in lambda over the slice nodes. (Phase 17 used a global cubic
    spline in lambda.)
  * Einstein tensor / Eulerian tetrad / Hawking-Ellis margins: own
    vectorised implementation (same pattern as Gate-4 worker V1,
    re-derived here; no phase code imported).

Imported (authorised shared DEFINITIONS only, per Gate-4 precedent):
  shell.py — the frozen Finalist-A prescription (build_shell profiles,
  cos shift window S(r)). The non-stationary audit machinery is mine.

Frozen family (from the claim statement / CHECKPOINT17 §P17-2):
  R1=10, R2=20, M_geom=2.0, edgepeaked wd=3.0/floor=0.2, s_rho=2.0,
  s_P=1.16, cos shift on [10,20]; endpoint beta=0.02.
  Audit points: 26 Fibonacci directions x radii 8..22 step 0.5 plus
  cavity radii 2,4,6 (832 points); core = max|That| > 1e-5.

float64 everywhere. Pieces by argv:
  control | m1slow | m1fast | shiftonly | ramps | ceiling
"""
import json
import os
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import shell as sh  # definition only: build_shell + shift_S

DTYPE = np.float64
EIGHT_PI = 8.0 * np.pi
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, 'results')
os.makedirs(RES, exist_ok=True)

BASE = dict(kind='edgepeaked', params={'wd': 3.0, 'floor': 0.2},
            s_rho=2.0, s_P=1.16)
NR = 4001
NLAM = 17
LAM_NODES = np.linspace(0.0, 1.0, NLAM)


# ---------------------------------------------------------------------------
# audit points (claim's sampling definition)
# ---------------------------------------------------------------------------
def fib_dirs(n):
    i = np.arange(n, dtype=DTYPE)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi),
                     np.cos(phi)], axis=1)


DIRS = fib_dirs(26)
RAD_SHELL = np.linspace(8.0, 22.0, 29)
RAD_CAV = np.array([2.0, 4.0, 6.0])
PTS = np.concatenate(
    [np.concatenate([DIRS * r for r in RAD_SHELL]),
     np.concatenate([DIRS * r for r in RAD_CAV])]).astype(DTYPE)
N_SHELL = 26 * len(RAD_SHELL)
RAD_PTS = np.linalg.norm(PTS, axis=1)


# ---------------------------------------------------------------------------
# fresh Einstein tensor: 2nd-order central differences throughout
# ---------------------------------------------------------------------------
def gamma_at(gtfunc, t, pts, h):
    pts = np.asarray(pts, dtype=DTYPE)
    g = np.asarray(gtfunc(t, pts), dtype=DTYPE)
    ginv = np.linalg.inv(g)
    dg = np.zeros((4,) + g.shape, dtype=DTYPE)
    dg[0] = (gtfunc(t + h, pts) - gtfunc(t - h, pts)) / (2 * h)
    for a in range(3):
        pp = pts.copy(); pp[:, a] += h
        pm = pts.copy(); pm[:, a] -= h
        dg[a + 1] = (gtfunc(t, pp) - gtfunc(t, pm)) / (2 * h)
    P = pts.shape[0]
    Gamma = np.zeros((P, 4, 4, 4), dtype=DTYPE)
    for b in range(4):
        for c in range(4):
            vec = (dg[b][:, :, c] + dg[c][:, :, b]
                   - np.stack([dg[d][:, b, c] for d in range(4)], axis=1))
            Gamma[:, :, b, c] = 0.5 * np.einsum('pad,pd->pa', ginv, vec)
    return Gamma, g, ginv


def einstein_td(gtfunc, t, pts, h):
    pts = np.asarray(pts, dtype=DTYPE)
    Gamma, g, ginv = gamma_at(gtfunc, t, pts, h)
    Ricci = np.zeros((pts.shape[0], 4, 4), dtype=DTYPE)
    for e in range(4):
        if e == 0:
            Gp = gamma_at(gtfunc, t + h, pts, h)[0]
            Gm = gamma_at(gtfunc, t - h, pts, h)[0]
        else:
            pp = pts.copy(); pp[:, e - 1] += h
            pm = pts.copy(); pm[:, e - 1] -= h
            Gp = gamma_at(gtfunc, t, pp, h)[0]
            Gm = gamma_at(gtfunc, t, pm, h)[0]
        dG = (Gp - Gm) / (2 * h)
        Ricci += dG[:, e, :, :]
        Ricci[:, :, e] -= np.einsum('paba->pb', dG)
    Ricci += (np.einsum('paae,pebd->pbd', Gamma, Gamma)
              - np.einsum('pade,peba->pbd', Gamma, Gamma))
    Rsc = np.einsum('pab,pab->p', ginv, Ricci)
    G = Ricci - 0.5 * Rsc[:, None, None] * g
    return G, G / EIGHT_PI, g


# ---------------------------------------------------------------------------
# own Eulerian tetrad + Hawking-Ellis margins
# ---------------------------------------------------------------------------
def eulerian_that(g, Tcov):
    gamma = g[:, 1:, 1:]
    beta_cov = g[:, 0, 1:]
    gamma_inv = np.linalg.inv(gamma)
    beta_up = np.einsum('pij,pj->pi', gamma_inv, beta_cov)
    alpha = np.sqrt(np.maximum(
        -g[:, 0, 0] + np.einsum('pi,pi->p', beta_cov, beta_up), 1e-300))
    lam, V = np.linalg.eigh(gamma)
    P = g.shape[0]
    E = np.zeros((P, 4, 4), dtype=DTYPE)
    E[:, 0, 0] = 1.0 / alpha
    E[:, 1:, 0] = -beta_up / alpha[:, None]
    for i in range(3):
        E[:, 1:, i + 1] = V[:, :, i] / np.sqrt(lam[:, i])[:, None]
    That = np.einsum('pma,pnb,pmn->pab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, 1, 2))


def sampled_margins(That):
    dirs = fib_dirs(162)
    P = That.shape[0]
    T00 = That[:, 0, 0]; T0i = That[:, 0, 1:]; Tij = That[:, 1:, 1:]
    quad = np.einsum('pjk,ij,ik->pi', Tij, dirs, dirs)
    lin = T0i @ dirs.T
    nec = (T00[:, None] + 2 * lin + quad).min(axis=1)
    tr = np.trace(Tij, axis1=1, axis2=2)
    trT = -T00 + tr
    wec = np.full(P, np.inf); sec = np.full(P, np.inf); dec = np.full(P, np.inf)
    Mm = That.copy(); Mm[:, 0, :] *= -1.0
    for v in np.linspace(0.0, 0.95, 6):
        gam = 1.0 / np.sqrt(1 - v * v)
        wv = gam ** 2 * (T00[:, None] + 2 * v * lin + v * v * quad)
        wec = np.minimum(wec, wv.min(axis=1))
        sv = wv - 0.5 * trT[:, None] * gam ** 2 * (v * v - 1.0)
        sec = np.minimum(sec, sv.min(axis=1))
        Vv = np.zeros((P, len(dirs), 4), dtype=DTYPE)
        Vv[:, :, 0] = gam
        Vv[:, :, 1:] = gam * v * dirs[None, :, :]
        Ups = -np.einsum('pab,pib->pia', Mm, Vv)
        q = Ups[:, :, 0] ** 2 - np.sum(Ups[:, :, 1:] ** 2, axis=2)
        nrm = 1.0 + np.sum(Ups ** 2, axis=2)
        val = np.where(Ups[:, :, 0] > 0, q / nrm, -np.abs(q) / nrm - 1.0)
        dec = np.minimum(dec, val.min(axis=1))
    return nec, wec, sec, dec


def margins(That):
    P = That.shape[0]
    M = That.copy(); M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k = np.argmax(cand, axis=1)
    ar = np.arange(P)
    rho = np.where(typeI, -evals[ar, k].real, np.nan)
    mask = np.ones((P, 4), dtype=bool); mask[ar, k] = False
    ps = np.where(typeI[:, None], evals.real[mask].reshape(P, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.min(rho[:, None] + ps, axis=1)
        wec = np.minimum(rho, nec)
        sec = np.minimum(nec, rho + np.sum(ps, axis=1))
        dec = np.minimum(rho, rho - np.max(np.abs(ps), axis=1))
    if np.any(~typeI):
        idx = np.where(~typeI)[0]
        sn, sw, ss, sd = sampled_margins(That[idx])
        nec[idx], wec[idx], sec[idx], dec[idx] = sn, sw, ss, sd
    return {'nec': nec, 'wec': wec, 'sec': sec, 'dec': dec,
            'typeI': typeI, 'rho_euler': That[:, 0, 0]}


def audit(gtfunc, t, h, label):
    t0 = time.time()
    _, T, g = einstein_td(gtfunc, t, PTS, h)
    That = eulerian_that(g, T)
    m = margins(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    out = {'label': label, 't': float(t), 'h': float(h),
           'max_abs_That': float(np.max(np.abs(That)))}
    for name, mk in (('core', scale > 1e-5), ('all', np.ones(len(PTS), bool))):
        if mk.sum() == 0:
            out[name] = None
            continue
        d = {kk: float(np.min(m[kk][mk])) for kk in ('nec', 'wec', 'sec', 'dec')}
        d['worst'] = min(d.values())
        d['typeI_frac'] = float(np.mean(m['typeI'][mk]))
        d['n'] = int(mk.sum())
        # worst site (radius of point attaining the worst EC minimum)
        wec_name = min(('nec', 'wec', 'sec', 'dec'), key=lambda kk: d[kk])
        idxs = np.where(mk)[0]
        i = idxs[int(np.argmin(m[wec_name][mk]))]
        d['worst_ec'] = wec_name
        d['worst_radius'] = float(RAD_PTS[i])
        out[name] = d
    out['wall_s'] = time.time() - t0
    cw = out['core']['worst'] if out['core'] else None
    print(f"  {label} t={t:.3f} h={h}: core worst={cw} "
          f"typeI={out['core']['typeI_frac'] if out['core'] else None} "
          f"({out['wall_s']:.0f}s)", flush=True)
    return out


def dump(obj, fname):
    with open(os.path.join(RES, fname), 'w') as f:
        json.dump(obj, f, indent=1, default=float)
    print('wrote', fname, flush=True)


# ---------------------------------------------------------------------------
# metric factories
# ---------------------------------------------------------------------------
def smoothstep(s):
    s = float(np.clip(s, 0.0, 1.0))
    return 3.0 * s * s - 2.0 * s * s * s


def metric_from_ab(a, b, beta, pts):
    pts = np.asarray(pts, dtype=DTYPE)
    r = np.sqrt(np.sum(pts ** 2, axis=1))
    S = sh.shift_S(r, 10.0, 20.0, 'cos', 1.0, [10.0, 20.0])
    P = pts.shape[0]
    g = np.zeros((P, 4, 4), dtype=DTYPE)
    g[:, 0, 0] = -np.exp(2 * a)
    g[:, 0, 1] = g[:, 1, 0] = -S * beta
    eb = np.exp(2 * b) - 1.0
    rsafe = np.where(r > 0, r, 1.0)
    n = pts / rsafe[:, None]
    for i in range(3):
        for j in range(3):
            g[:, 1 + i, 1 + j] = eb * n[:, i] * n[:, j]
        g[:, 1 + i, 1 + i] += 1.0
    return g


# --- morph slices: build once, cache splines in r -------------------------
_SLICES = None


def get_slices():
    global _SLICES
    if _SLICES is not None:
        return _SLICES
    prof1 = sh.build_shell(10.0, 20.0, 2.0, kind=BASE['kind'],
                           params=dict(BASE['params']), s_rho=BASE['s_rho'],
                           s_P=BASE['s_P'], Nr=NR)
    r = prof1['r']
    a_sp, b_sp = [], []
    for j in range(NLAM):
        lam = j / 16.0
        if j == 0:
            a = np.zeros_like(r); b = np.zeros_like(r)
        elif j == 16:
            a, b = prof1['a'], prof1['b']
        else:
            p = sh.build_shell(10.0, 20.0, 2.0 * lam, kind=BASE['kind'],
                               params=dict(BASE['params']),
                               s_rho=BASE['s_rho'], s_P=BASE['s_P'], Nr=NR)
            a, b = p['a'], p['b']
        a_sp.append(CubicSpline(r, a))
        b_sp.append(CubicSpline(r, b))
    _SLICES = (r, a_sp, b_sp)
    return _SLICES


def lagrange_w(nodes, x):
    n = len(nodes)
    w = np.ones(n, dtype=DTYPE)
    for j in range(n):
        for k in range(n):
            if k != j:
                w[j] *= (x - nodes[k]) / (nodes[j] - nodes[k])
    return w


def ab_at_lam(lam, rc):
    """Local 4-point Lagrange interpolation in lambda (fresh method)."""
    r, a_sp, b_sp = get_slices()
    lam = float(np.clip(lam, 0.0, 1.0))
    j0 = int(np.floor(lam * 16)) - 1
    j0 = max(0, min(NLAM - 4, j0))
    idx = [j0 + j for j in range(4)]
    nodes = LAM_NODES[idx]
    w = lagrange_w(nodes, lam)
    a = np.zeros(len(rc), dtype=DTYPE); b = np.zeros(len(rc), dtype=DTYPE)
    for wj, ij in zip(w, idx):
        a += wj * a_sp[ij](rc)
        b += wj * b_sp[ij](rc)
    return a, b


class MorphM1:
    """M1 amplitude morph: lam(t)=smoothstep(t/T) clipped, beta=0.02*lam.
    frozen_at pins (lam, beta) -> t-independent gtfunc (frozen audit)."""

    def __init__(self, T, frozen_at=None):
        self.T = float(T)
        self.frozen_at = frozen_at
        r, _, _ = get_slices()
        self.rmax = float(r[-1])

    def lam_beta(self, t):
        if self.frozen_at is not None:
            lam = smoothstep(self.frozen_at / self.T)
        else:
            lam = smoothstep(float(t) / self.T)
        return lam, 0.02 * lam

    def gtfunc(self, t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, self.rmax)
        lam, beta = self.lam_beta(t)
        a, b = ab_at_lam(lam, rc)
        return metric_from_ab(a, b, beta, pts)


class RampMetric:
    """P17-3 ramps: Finalist-A profile fixed, beta(t) piecewise smoothstep.
    frozen_beta pins beta (frozen audit through same code path)."""

    def __init__(self, T, frozen_beta=None):
        self.T = float(T)
        self.frozen_beta = frozen_beta
        prof = sh.build_shell(10.0, 20.0, 2.0, kind=BASE['kind'],
                              params=dict(BASE['params']),
                              s_rho=BASE['s_rho'], s_P=BASE['s_P'], Nr=NR)
        self.a_sp = CubicSpline(prof['r'], prof['a'])
        self.b_sp = CubicSpline(prof['r'], prof['b'])
        self.rmax = float(prof['r'][-1])

    def beta_of(self, t):
        if self.frozen_beta is not None:
            return float(self.frozen_beta)
        t = float(t); T = self.T
        if t <= 0.0:
            return 0.0
        if t <= T:
            return 0.02 * smoothstep(t / T)
        if t <= 1.25 * T:
            return 0.02
        if t <= 2.25 * T:
            return 0.02 + 0.03 * smoothstep((t - 1.25 * T) / T)
        return 0.05

    def gtfunc(self, t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, self.rmax)
        a = self.a_sp(rc); b = self.b_sp(rc)
        return metric_from_ab(a, b, self.beta_of(t), pts)


class StaticBeta:
    """Stationary Finalist-A at fixed beta (ceiling scan / controls)."""

    def __init__(self, beta):
        self.beta = float(beta)
        prof = sh.build_shell(10.0, 20.0, 2.0, kind=BASE['kind'],
                              params=dict(BASE['params']),
                              s_rho=BASE['s_rho'], s_P=BASE['s_P'], Nr=NR)
        self.a_sp = CubicSpline(prof['r'], prof['a'])
        self.b_sp = CubicSpline(prof['r'], prof['b'])
        self.rmax = float(prof['r'][-1])

    def gtfunc(self, t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        r = np.sqrt(np.sum(pts ** 2, axis=1))
        rc = np.clip(r, 0.0, self.rmax)
        return metric_from_ab(self.a_sp(rc), self.b_sp(rc), self.beta, pts)


class ShiftOnly:
    """Pure varying shift on flat space: a=b=0, beta fixed (frozen) —
    the M3 stage-1 slices. beta may also follow a ramp in t if T given."""

    def __init__(self, beta=None, T=None):
        self.beta = beta
        self.T = T

    def beta_of(self, t):
        if self.T is None:
            return float(self.beta)
        # M3 stage 1: beta = 0.02*smoothstep(2t/T) on [0, T/2], then 0.02
        s = 2.0 * float(t) / self.T
        return 0.02 * smoothstep(s)

    def gtfunc(self, t, pts):
        pts = np.asarray(pts, dtype=DTYPE)
        P = pts.shape[0]
        a = np.zeros(P, dtype=DTYPE); b = np.zeros(P, dtype=DTYPE)
        return metric_from_ab(a, b, self.beta_of(t), pts)


# ---------------------------------------------------------------------------
# pieces
# ---------------------------------------------------------------------------
def piece_control():
    out = {}
    print('== stationary Finalist-A control, beta=0.02, h-scan ==', flush=True)
    sm = StaticBeta(0.02)
    for h in (0.30, 0.15, 0.075):
        out[f'h{h}'] = audit(sm.gtfunc, 0.0, h, 'static beta=0.02')
    print('== beta=0 static wall control ==', flush=True)
    s0 = StaticBeta(0.0)
    out['beta0_h0.3'] = audit(s0.gtfunc, 0.0, 0.3, 'static beta=0')
    out['beta0_h0.15'] = audit(s0.gtfunc, 0.0, 0.15, 'static beta=0')
    print('== Minkowski smoke (shift-only beta=0) ==', flush=True)
    mk = ShiftOnly(beta=0.0)
    out['minkowski'] = audit(mk.gtfunc, 0.0, 0.3, 'flat beta=0')
    dump(out, 'we_control.json')


def piece_m1slow():
    T = 200.0
    print('== M1 T=200: 13 dynamic instants, h=0.3 ==', flush=True)
    mm = MorphM1(T)
    rows = []
    for k in range(13):
        t = k * T / 12.0
        rows.append(audit(mm.gtfunc, t, 0.3, f'M1 T200 dyn k={k}'))
        rows[-1]['lam'] = smoothstep(k / 12.0)
    # frozen at worst instant + endpoint
    cored = [r for r in rows if r['core']]
    w = min(cored, key=lambda r: r['core']['worst'])
    print(f"worst instant t={w['t']} lam={w['lam']}", flush=True)
    fm = MorphM1(T, frozen_at=w['t'])
    conf = {'t_worst': w['t'], 'lam_worst': w['lam'],
            'dyn_h015': audit(mm.gtfunc, w['t'], 0.15, 'M1 T200 worst dyn h015'),
            'frozen_h03': audit(fm.gtfunc, w['t'], 0.3, 'M1 T200 worst frozen'),
            'frozen_h015': audit(fm.gtfunc, w['t'], 0.15, 'M1 T200 worst frozen h015')}
    # frozen minimum over path (spot: k=2,3,4,6,12)
    frz_spot = {}
    for k in (2, 3, 4, 6, 12):
        t = k * T / 12.0
        fk = MorphM1(T, frozen_at=t)
        frz_spot[f'k{k}'] = audit(fk.gtfunc, t, 0.3, f'M1 T200 frozen k={k}')
        frz_spot[f'k{k}']['lam'] = smoothstep(k / 12.0)
    dump({'T': T, 'instants': rows, 'confirm': conf, 'frozen_spot': frz_spot},
         'we_m1_T200.json')


def piece_m1fast():
    T = 40.0
    print('== M1 T=40: dynamic instants (subset incl. first-fail + worst) ==',
          flush=True)
    mm = MorphM1(T)
    rows = []
    for k in (0, 1, 2, 3, 4, 6, 8, 12):
        t = k * T / 12.0
        rows.append(audit(mm.gtfunc, t, 0.3, f'M1 T40 dyn k={k}'))
        rows[-1]['lam'] = smoothstep(k / 12.0)
    # frozen at first failing instant k=1 and at k=6
    out = {'T': T, 'instants': rows}
    for k in (1, 6):
        t = k * T / 12.0
        fk = MorphM1(T, frozen_at=t)
        out[f'frozen_k{k}'] = audit(fk.gtfunc, t, 0.3, f'M1 T40 frozen k={k}')
        out[f'frozen_k{k}']['lam'] = smoothstep(k / 12.0)
    # h=0.15 confirmation at first failing instant k=1 (dyn + frozen)
    t1 = T / 12.0
    out['firstfail_dyn_h015'] = audit(mm.gtfunc, t1, 0.15, 'M1 T40 k1 dyn h015')
    f1 = MorphM1(T, frozen_at=t1)
    out['firstfail_frozen_h015'] = audit(f1.gtfunc, t1, 0.15, 'M1 T40 k1 frz h015')
    dump(out, 'we_m1_T40.json')


def piece_shiftonly():
    print('== shift-only on flat space: frozen beta scan ==', flush=True)
    out = {}
    for beta in (0.005, 0.0074, 0.01, 0.015, 0.02):
        so = ShiftOnly(beta=beta)
        out[f'beta{beta}'] = audit(so.gtfunc, 0.0, 0.3, f'shift-only beta={beta}')
    so = ShiftOnly(beta=0.01)
    out['beta0.01_h015'] = audit(so.gtfunc, 0.0, 0.15, 'shift-only beta=0.01 h015')
    # dynamic M3 stage-1 at its beta=0.01 instant (T=200: t=50; T=40: t=10)
    for T in (200.0, 40.0):
        dyn = ShiftOnly(T=T)
        tstar = T / 4.0  # smoothstep(2t/T)=0.5 -> beta=0.01
        out[f'dyn_T{int(T)}_beta0.01'] = audit(dyn.gtfunc, tstar, 0.3,
                                               f'M3 stage1 dyn T={int(T)}')
    dump(out, 'we_shiftonly.json')


def piece_ramps():
    out = {}
    # segment-1 midpoints (max |beta_dot|) at all three rates: dyn + frozen
    for T in (400.0, 200.0, 40.0):
        rm = RampMetric(T)
        tmid = 0.5 * T
        dyn = audit(rm.gtfunc, tmid, 0.3, f'ramp seg1 mid T={int(T)} dyn')
        frz = RampMetric(T, frozen_beta=0.01)
        fr = audit(frz.gtfunc, tmid, 0.3, f'ramp seg1 mid T={int(T)} frozen')
        tax = {k: (fr['core'][k] - dyn['core'][k]) for k in ('nec', 'wec', 'sec', 'dec')}
        out[f'T{int(T)}_seg1mid'] = {'dyn': dyn, 'frozen': fr, 'tax': tax,
                                     'beta_dot_max': 1.5 * 0.02 / T}
        # segment-2 midpoint beta=0.035 (frozen-illegal zone): dyn + frozen
        tmid2 = 1.75 * T
        dyn2 = audit(rm.gtfunc, tmid2, 0.3, f'ramp seg2 mid T={int(T)} dyn')
        frz2 = RampMetric(T, frozen_beta=0.035)
        fr2 = audit(frz2.gtfunc, tmid2, 0.3, f'ramp seg2 mid T={int(T)} frozen')
        tax2 = {k: (fr2['core'][k] - dyn2['core'][k]) for k in ('nec', 'wec', 'sec', 'dec')}
        out[f'T{int(T)}_seg2mid'] = {'dyn': dyn2, 'frozen': fr2, 'tax': tax2,
                                     'beta_dot_max': 1.5 * 0.03 / T}
    # segment-1 worst-instant spot check at T=40 (t=20 is the midpoint, done);
    # extra instants T=40 seg1: t=10 (beta=0.0069), t=30 (beta=0.0137)
    rm40 = RampMetric(40.0)
    for t, b in ((10.0, 0.02 * smoothstep(0.25)), (30.0, 0.02 * smoothstep(0.75))):
        out[f'T40_seg1_t{int(t)}'] = audit(rm40.gtfunc, t, 0.3,
                                           f'ramp seg1 T40 t={int(t)} dyn')
    # hold instant identity check T=40: t=45 (beta=0.02, beta_dot=0)
    out['T40_hold'] = audit(rm40.gtfunc, 45.0, 0.3, 'ramp hold T40 dyn')
    # linearity regression on seg1 DEC tax and seg2 NEC tax
    import numpy as _np
    for seg, ec in (('seg1mid', 'dec'), ('seg2mid', 'nec'), ('seg2mid', 'sec')):
        x = _np.array([out[f'T{int(T)}_{seg}']['beta_dot_max'] for T in (400.0, 200.0, 40.0)])
        y = _np.array([out[f'T{int(T)}_{seg}']['tax'][ec] for T in (400.0, 200.0, 40.0)])
        A = _np.vstack([x, _np.ones_like(x)]).T
        slope, intercept = _np.linalg.lstsq(A, y, rcond=None)[0]
        pred = slope * x + intercept
        ss_res = float(_np.sum((y - pred) ** 2)); ss_tot = float(_np.sum((y - y.mean()) ** 2))
        out[f'reg_{seg}_{ec}'] = {'slope': float(slope), 'intercept': float(intercept),
                                  'R2': (1.0 - ss_res / ss_tot) if ss_tot > 0 else None,
                                  'x': list(x), 'y': list(y)}
    dump(out, 'we_ramps.json')


def piece_ceiling():
    print('== static ceiling scan ==', flush=True)
    out = {}
    for beta in (0.02, 0.0225, 0.025, 0.0275, 0.03, 0.05):
        sb = StaticBeta(beta)
        out[f'beta{beta}_h03'] = audit(sb.gtfunc, 0.0, 0.3, f'ceiling beta={beta}')
    for beta in (0.025, 0.0275):
        sb = StaticBeta(beta)
        out[f'beta{beta}_h015'] = audit(sb.gtfunc, 0.0, 0.15, f'ceiling beta={beta} h015')
    sb = StaticBeta(0.025)
    out['beta0.025_h0075'] = audit(sb.gtfunc, 0.0, 0.075, 'ceiling beta=0.025 h0075')
    dump(out, 'we_ceiling.json')


if __name__ == '__main__':
    which = sys.argv[1]
    t00 = time.time()
    {'control': piece_control, 'm1slow': piece_m1slow, 'm1fast': piece_m1fast,
     'shiftonly': piece_shiftonly, 'ramps': piece_ramps,
     'ceiling': piece_ceiling}[which]()
    print(f'TOTAL {time.time() - t00:.0f}s', flush=True)
