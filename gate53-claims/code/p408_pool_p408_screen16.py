"""
p408_pool_p408_screen16.py - Phase 391 E2 screening machinery (SCREENING ONLY, never
a verdict): 16-mode grading basis variant of p386_screen.GradedScreen +
p386_stage2x_common.JointScreenX (EXTENDED mask [R_in-0.5, R_out] =
[2.234381, 27.265413], point set follows candidate r_m = y[25]).
Construction grid coarsened inside this driver only via P408_CONSTR_DR
(default 2.5e-4), mirroring p386_screen's P386_CONSTR_DR discipline;
calibration on the y_his-equivalent is the guard.
"""
import os, sys
import numpy as np

POOL = '/home/spark/work/p386/warp-pilot'
P408 = POOL + '/phase408/work'
for p in [P408, POOL, POOL + '/phase386/work', POOL + '/phase251/work',
          POOL + '/phase50', POOL + '/gate6', POOL + '/phase63']:
    sys.path.insert(0, p)

import p408_pool_p408_lib16 as L12
import p2513_lib as H
import p503_lib as L

DTYPE = np.float64
SCREEN_H = 0.0375
DR_SCREEN = 0.002
CONSTR_DR = float(os.environ.get('P408_CONSTR_DR', '2.5e-4'))

_orig_cg = L12.construction_grid


def _coarse_cg():
    rmax = L12.R_OUT + 2.75
    r = np.arange(0.0, rmax + 1e-12, CONSTR_DR, dtype=DTYPE)
    ins = [L12.R1, L12.R2]
    for k in L12.GRADING_KNOTS_INNER:
        ins.append(float(k))
        for s in (0.5 * L12.W, L12.W, 1.5 * L12.W, 2.0 * L12.W):
            ins.append(float(k) - s)
            ins.append(float(k) + s)
    r = np.unique(np.sort(np.r_[r, np.asarray(ins, dtype=DTYPE)]))
    return r[(r >= 0.0) & (r <= rmax)]


if CONSTR_DR != float(L12.DR_CONSTR):
    L12.construction_grid = _coarse_cg

R1, R2, W = float(L12.R1), float(L12.R2), float(L12.W)
R_IN = float(L12.R_IN)
MASK_LO = R_IN - 0.5
MASK_HI = float(L12.R_OUT)


def load_y_his30():
    x = np.load(POOL + '/phase50/procaccia/opt/optimal_shift_code/results/x_slp2.npy')
    return L12.y_his_vector16(x)


Y_HIS30 = load_y_his30()


class Screen16:
    """beta_crit screening for the 16-mode graded family on the EXTENDED
    mask, point set rebuilt per candidate r_m. Screening only."""

    def __init__(self, r_m_ref):
        self._set_pts(r_m_ref)
        self._builders = {}
        self.cache = {}
        self.n_builds = 0
        self.n_reads = 0

    def _set_pts(self, r_m):
        rad = H.repaired_radii_cell(R1, R2, W, float(r_m))
        pts = np.concatenate([H.DIRS26 * r for r in rad]).astype(DTYPE)
        radp = np.linalg.norm(pts, axis=1)
        core = (radp >= MASK_LO) & (radp <= MASK_HI)
        self.pts = pts[core]
        self.radp = radp[core]
        self.n_radii = len(rad)
        self.n_radii_kept = int(np.sum((rad >= MASK_LO) & (rad <= MASK_HI)))

    def builder(self, y):
        key = tuple(np.round(np.asarray(y, dtype=DTYPE), 10))
        if key not in self._builders:
            self._builders[key] = L12.GradedProcaccia16(
                np.asarray(y, dtype=DTYPE), dr=DTYPE(DR_SCREEN))
            self.n_builds += 1
        return self._builders[key]

    def score(self, y, beta):
        y = np.asarray(y, dtype=DTYPE)
        self._set_pts(y[29])
        g = self.builder(y)
        m = L.fast_audit(g.metric_factory(beta), self.pts, SCREEN_H)
        self.n_reads += 1
        That = m['That']
        scale = np.max(np.abs(That), axis=(1, 2))
        rho_peak = float(np.max(That[:, 0, 0]))
        thr = max(1e-9 * (10.0 / R1) ** 2, 1e-3 * abs(rho_peak))
        sig = scale > thr
        if sig.sum() == 0:
            return False, None
        w = np.where(m['typeI'], m['nec'], m['sampled_nec'])
        for k in ('wec', 'sec', 'dec'):
            w = np.minimum(w, np.where(m['typeI'], m[k], m['sampled_nec']))
        tI = float(np.mean(m['typeI'][sig]))
        worst = float(np.min(w[sig]))
        return bool(tI == 1.0 and worst > 0.0), worst

    def legal(self, y, beta):
        return self.score(y, beta)[0]

    def beta_crit(self, y):
        y = np.asarray(y, dtype=DTYPE)
        key = tuple(np.round(y, 10))
        if key in self.cache:
            return self.cache[key]['beta_crit']
        if not self.legal(y, 0.10):
            rec = {'beta_crit': 0.10, 'bracket': [None, 0.10], 'flag': 'at_or_below_lo'}
            self.cache[key] = rec
            return 0.10
        if self.legal(y, 0.20):
            rec = {'beta_crit': 0.20, 'bracket': [0.20, None], 'flag': 'at_or_above_hi'}
            self.cache[key] = rec
            return 0.20
        lo, hi = 0.10, 0.20
        while hi - lo > 0.001:
            mid = 0.5 * (lo + hi)
            if self.legal(y, mid):
                lo = mid
            else:
                hi = mid
        rec = {'beta_crit': 0.5 * (lo + hi), 'bracket': [lo, hi], 'flag': 'bisected'}
        self.cache[key] = rec
        return rec['beta_crit']

    def record(self, y):
        return self.cache.get(tuple(np.round(np.asarray(y, dtype=DTYPE), 10)))


def make_screen16():
    return Screen16(float(Y_HIS30[29]))
