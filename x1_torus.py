"""
x1_torus.py — X1: toroidal (donut) warp shell, Fuchs ingredients.

Construction (prescribed-profile / local-TOV): take the verified spherical
shell family's 1D profiles a(.), b(.) from shell.build_shell (edge-peaked
density, Gaussian smoothing, TOV pressure) and reinterpret the radial
argument as the TORUS DISTANCE s(x) = distance from x to the ring circle
of radius Rmaj in the z=0 plane:
    s = sqrt( (Rcyl - Rmaj)^2 + z^2 ),   Rcyl = sqrt(x^2+y^2).
Matter tube: s in [R1, R2] = [10, 20] (same cross-section as the spherical
finalists). Profiles are windowed to ZERO on s in [R2, R2+Delta] so the
metric is EXACTLY Minkowski for s > R2+Delta (incl. the whole axis when
Rmaj > R2+Delta) and flat (constant lapse, b=0) in the cavity s < R1.
Metric (ADM form, motion along the torus axis z):
    g_tt = -exp(2 a(s)),  g_tz = -S(s) * beta,
    gamma_ij = delta_ij + (exp(2 b(s)) - 1) shat_i shat_j,
    shat = grad s (unit vector away from the ring).
S = cosine window on [R1, R2] (the spherical winner). SSV escape (logged):
non-spherical topology + non-unit lapse + non-flat slices; topology is
posited as initial data (Geroch), never "formed".

M is the 1D profile mass parameter (compactness knob M/R1); the toroidal
ADM mass is not defined by these compactly-supported profiles, and the
measured volume integral of the Eulerian density is reported separately
for any candidate that passes. The judge is the pilot point auditor
(verify_metric.einstein_at_points) + Hawking-Ellis margins, unchanged.
float64 everywhere.
"""
import json
import numpy as np
from scipy.interpolate import CubicSpline

import shell as sh
import verify_metric as vm
from verify_finalist import audit_block, fib_dirs

DTYPE = np.float64
R1, R2 = 10.0, 20.0
DELTA = 5.0          # outer window width: profiles -> 0 on [R2, R2+DELTA]
KIND = 'edgepeaked'
PARAMS = {'wd': 3.0, 'floor': 0.2}
S_RHO, S_P = 2.0, 1.16   # Finalist A smoothing


def window_W(s, delta=DELTA):
    """1 for s <= R2, smootherstep down to 0 at s = R2 + delta."""
    return 1.0 - sh.smootherstep((np.asarray(s, dtype=DTYPE) - R2) / delta)


def torus_profiles(M, kind=KIND, params=None, s_rho=S_RHO, s_P=S_P,
                   delta=DELTA):
    """Windowed splines a_w(s), b_w(s) from the spherical 1D construction."""
    prof = sh.build_shell(R1, R2, M, kind=kind, params=params or PARAMS,
                          s_rho=s_rho, s_P=s_P, Nr=4001)
    W = window_W(prof['r'], delta)
    a_w = prof['a'] * W
    b_w = prof['b'] * W
    return {'a_s': CubicSpline(prof['r'], a_w),
            'b_s': CubicSpline(prof['r'], b_w),
            'smax': float(prof['r'][-1]), 'M': M, 'delta': delta,
            'a_in': float(a_w[0]), 'prof': prof}


def torus_gfunc(tp, Rmaj, beta):
    a_s, b_s, smax = tp['a_s'], tp['b_s'], tp['smax']

    def gfunc(pts):
        pts = np.asarray(pts, dtype=DTYPE)
        x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        Rcyl = np.sqrt(x ** 2 + y ** 2)
        s = np.sqrt((Rcyl - Rmaj) ** 2 + z ** 2)
        sc = np.clip(s, 0.0, smax)
        a = a_s(sc); b = b_s(sc)
        S = sh.shift_S(s, R1, R2, 'cos', 1.0, [R1, R2])
        # shat = grad s, guarded at s=0 (ring itself) and on the axis
        ssafe = np.where(s > 1e-9, s, 1.0)
        d = (Rcyl - Rmaj) / ssafe
        Rsafe = np.where(Rcyl > 1e-12, Rcyl, 1.0)
        ux = np.where(Rcyl > 1e-12, x / Rsafe, 0.0)
        uy = np.where(Rcyl > 1e-12, y / Rsafe, 0.0)
        shat = np.stack([d * ux, d * uy, z / ssafe], axis=1)
        P = pts.shape[0]
        g = np.zeros((P, 4, 4), dtype=DTYPE)
        g[:, 0, 0] = -np.exp(2 * a)
        g[:, 0, 3] = g[:, 3, 0] = -S * beta
        eb = np.exp(2 * b) - 1.0
        for i in range(3):
            for j in range(3):
                g[:, 1 + i, 1 + j] = eb * shat[:, i] * shat[:, j]
            g[:, 1 + i, 1 + i] += 1.0
        return g

    return gfunc


def torus_points(Rmaj, seed, n_tube=210, n_cav=30, n_ext=30, delta=DELTA):
    """Randomised audit points (seeded; the optimiser never sees finals).
    Tube points parametrised by (s, cross-section angle phi, azimuth th):
    P = ((Rmaj + s cos phi) cos th, (Rmaj + s cos phi) sin th, s sin phi),
    whose distance to the ring is exactly s."""
    rng = np.random.default_rng(seed)
    smax = R2 + delta
    # s: concentrated on the matter + window + margins, some deep cavity/exterior
    s_tube = np.concatenate([
        rng.uniform(R1 - 2.0, smax + 2.0, int(0.7 * n_tube)),
        rng.uniform(4.0, smax + 6.0, n_tube - int(0.7 * n_tube))])
    phi = rng.uniform(0, 2 * np.pi, len(s_tube))
    th = rng.uniform(0, 2 * np.pi, len(s_tube))
    Rc = Rmaj + s_tube * np.cos(phi)
    pts = np.stack([Rc * np.cos(th), Rc * np.sin(th),
                    s_tube * np.sin(phi)], axis=1)
    # cavity points: s in [2, R1-0.5]
    s_c = rng.uniform(2.0, R1 - 0.5, n_cav)
    phi = rng.uniform(0, 2 * np.pi, n_cav); th = rng.uniform(0, 2 * np.pi, n_cav)
    Rc = Rmaj + s_c * np.cos(phi)
    cav = np.stack([Rc * np.cos(th), Rc * np.sin(th), s_c * np.sin(phi)], axis=1)
    # exterior + axis points (must be exactly flat: s > smax)
    s_e = rng.uniform(smax + 1.0, smax + 10.0, n_ext - 7)
    phi = rng.uniform(0, 2 * np.pi, len(s_e)); th = rng.uniform(0, 2 * np.pi, len(s_e))
    Rc = Rmaj + s_e * np.cos(phi)
    ext = np.stack([Rc * np.cos(th), Rc * np.sin(th), s_e * np.sin(phi)], axis=1)
    axis = np.stack([np.zeros(7), np.zeros(7),
                     np.linspace(-35, 35, 7)], axis=1)
    return np.concatenate([pts, cav, ext, axis]).astype(DTYPE)


def audit_torus(M, Rmaj, beta, seed=424242, h=0.3, n_tube=210):
    tp = torus_profiles(M)
    gf = torus_gfunc(tp, Rmaj, beta)
    pts = torus_points(Rmaj, seed, n_tube=n_tube)
    out, m, That = audit_block(gf, pts, h, f'torus M={M} Rmaj={Rmaj} b={beta}')
    out.update({'M': M, 'Rmaj': Rmaj, 'aspect': Rmaj / 15.0, 'beta': beta,
                'seed': seed})
    return out


if __name__ == '__main__':
    # Validation 1: flat profiles + beta=1.5 shift -> T must be ~0
    _r = np.linspace(0.0, 60.0, 121)
    _z = np.zeros_like(_r)
    tp0 = {'a_s': CubicSpline(_r, _z), 'b_s': CubicSpline(_r, _z),
           'smax': 60.0, 'M': 0.0, 'delta': DELTA, 'a_in': 0.0, 'prof': None}
    gf0 = torus_gfunc(tp0, 30.0, 1.5)
    pts = torus_points(30.0, 123)
    G, That, m = vm.einstein_at_points(gf0, pts, h=0.3)
    print('X1 Minkowski+shift control: max|That| =',
          float(np.max(np.abs(That))), '(expect FD noise << 1e-6)')
    # Validation 2: spherical control reminder is Finalist A (already verified);
    # here: torus base at the spherical winner's mass, fat ring
    out = audit_torus(2.0, 45.0, 0.0)
    print(json.dumps(out, indent=1, default=float))
