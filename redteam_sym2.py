"""redteam_sym2.py — R2 fallback: symbolic third path in SPHERICAL
coordinates (independent derivation from both the Cartesian FD auditor
and the JAX AD chain).

Shell metric in (t, r, th, ph): lapse exp(a(r)), spatial metric
diag(exp(2b(r)), r^2, r^2 sin^2 th), shift along +x with magnitude
beta*S(r). Shift covector components:
  beta_r  = -beta S sin(th) cos(ph)
  beta_th = -beta S r cos(th) cos(ph)
  beta_ph = +beta S r sin(th) sin(ph)
We work in the ph=0 plane (cos=1, sin=0): beta_ph = 0,
beta_r = -beta S sin(th), beta_th = -beta S r cos(th).
a, b, S stay symbolic functions of r; th stays symbolic through the
tensor algebra and is substituted (pi/2 = +x axis point, 0 = +z axis
point) only at evaluation. Derivative placeholders are substituted
before lambdify, exactly as in redteam_sym.py.
Usage: ./venv/bin/python redteam_sym2.py finalist_A
"""
import json, sys, time
import numpy as np
import sympy as sp
import shell as sh
import verify_metric as vm
import redteam as rt

t0 = time.time()
t, r, th, ph = sp.symbols('t r th ph', positive=True)
a = sp.Function('a')(r)
b = sp.Function('b')(r)
S = sp.Function('S')(r)
beta = sp.symbols('beta')

coords = [t, r, th, ph]
g = sp.zeros(4, 4)
g[0, 0] = -sp.exp(2 * a)
g[0, 1] = g[1, 0] = -beta * S * sp.sin(th)
g[0, 2] = g[2, 0] = -beta * S * r * sp.cos(th)
g[1, 1] = sp.exp(2 * b)
g[2, 2] = r ** 2
g[3, 3] = r ** 2 * sp.sin(th) ** 2
gi = g.inv()
print(f'[{time.time()-t0:.0f}s] metric inverted', flush=True)

dg = np.zeros((4, 4, 4), dtype=object)  # dg[s, mu, nu]
for s in range(4):
    for mu in range(4):
        for nu in range(4):
            dg[s, mu, nu] = g[mu, nu].diff(coords[s])

Gamma = np.zeros((4, 4, 4), dtype=object)
for lam in range(4):
    for mu in range(4):
        for nu in range(4):
            expr = sum(gi[lam, s] * (dg[mu, s, nu] + dg[nu, s, mu]
                                     - dg[s, mu, nu]) for s in range(4))
            Gamma[lam, mu, nu] = sp.simplify(expr / 2)
print(f'[{time.time()-t0:.0f}s] Christoffel done', flush=True)

dG = np.zeros((4, 4, 4, 4), dtype=object)
for s in range(4):
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                dG[s, lam, mu, nu] = Gamma[lam, mu, nu].diff(coords[s])

Ric = np.zeros((4, 4), dtype=object)
for mu in range(4):
    for nu in range(4):
        expr = 0
        for lam in range(4):
            expr += dG[lam, lam, mu, nu] - dG[nu, lam, mu, lam] \
                + sum(Gamma[lam, lam, s] * Gamma[s, mu, nu]
                      - Gamma[lam, nu, s] * Gamma[s, mu, lam]
                      for s in range(4))
        Ric[mu, nu] = sp.simplify(expr)
print(f'[{time.time()-t0:.0f}s] Ricci done', flush=True)

Rsc = sum(gi[mu, nu] * Ric[mu, nu] for mu in range(4) for nu in range(4))
G = np.zeros((4, 4), dtype=object)
for mu in range(4):
    for nu in range(4):
        G[mu, nu] = sp.simplify(Ric[mu, nu] - Rsc * g[mu, nu] / 2)
print(f'[{time.time()-t0:.0f}s] Einstein done', flush=True)

av, bv, Sv = sp.symbols('av bv Sv')
a1, a2 = sp.symbols('a1 a2')
b1, b2 = sp.symbols('b1 b2')
S1, S2 = sp.symbols('S1 S2')
subs_map = {}
for f, v, d1, d2 in ((sp.Function('a')(r), av, a1, a2),
                     (sp.Function('b')(r), bv, b1, b2),
                     (sp.Function('S')(r), Sv, S1, S2)):
    subs_map[f] = v
    subs_map[f.diff(r)] = d1
    subs_map[f.diff(r, 2)] = d2

Gfuncs = {}
for mu in range(4):
    for nu in range(4):
        e = G[mu, nu].subs(subs_map)
        Gfuncs[(mu, nu)] = sp.lambdify((r, th, beta, av, a1, a2, bv, b1, b2,
                                        Sv, S1, S2), e, 'numpy')
print(f'[{time.time()-t0:.0f}s] lambdified', flush=True)


def main(name):
    cfg = rt.load_cfg(name)
    prof = rt.build_profiles(cfg)
    from scipy.interpolate import CubicSpline
    a_s = CubicSpline(prof['r'], prof['a'])
    b_s = CubicSpline(prof['r'], prof['b'])
    R1, R2 = cfg['R1'], cfg['R2']
    lo, hi = cfg['ws']

    def S_of(rr):
        u = np.clip((rr - lo) / (hi - lo), 0, 1)
        return 0.5 * (1 + np.cos(np.pi * u))

    def Sp_of(rr):
        u = np.clip((rr - lo) / (hi - lo), 0, 1)
        return -0.5 * np.pi / (hi - lo) * np.sin(np.pi * u)

    def Spp_of(rr):
        u = np.clip((rr - lo) / (hi - lo), 0, 1)
        return -0.5 * (np.pi / (hi - lo)) ** 2 * np.cos(np.pi * u)

    gfunc = sh.shell_point_factory(prof, cfg['beta'], cfg['shift_kind'], 1.0,
                                   cfg['ws'])
    rad = [0.6 * R1] + [R1 + f * (R2 - R1)
                        for f in (0.05, 0.25, 0.5, 0.75, 0.95)] + [1.2 * R2]
    # sample points in the ph=0 plane at three orientations:
    # th=pi/2 (+x axis, n parallel to shift), pi/4, and 0.3 rad
    # (near-pole but regular; the exact pole is a coordinate artefact
    # of the check, not of the geometry)
    pts, ths = [], []
    for rr in rad:
        for thv in (np.pi / 2, np.pi / 4, 0.3):
            pts.append([rr * np.sin(thv), 0.0, rr * np.cos(thv)])
            ths.append(thv)
    pts = np.array(pts, dtype=float)
    Gfd, That_fd, m_fd = vm.einstein_at_points(gfunc, pts, h=0.03 * R1)
    rows = []
    for i, pt in enumerate(pts):
        rr = float(np.linalg.norm(pt))
        vals = (rr, ths[i], cfg['beta'],
                float(a_s(rr)), float(a_s(rr, 1)), float(a_s(rr, 2)),
                float(b_s(rr)), float(b_s(rr, 1)), float(b_s(rr, 2)),
                float(S_of(rr)), float(Sp_of(rr)), float(Spp_of(rr)))
        Gsph = np.array([[Gfuncs[(mu, nu)](*vals) for nu in range(4)]
                         for mu in range(4)], dtype=float)
        # spherical-basis Einstein tensor -> Cartesian at the point:
        # build the rotation from spherical orthonormal frame to Cartesian
        # via the Jacobian of (t,r,th,ph) wrt (t,x,y,z) is singular on the
        # z axis; instead transform with the orthonormal frames:
        # e_r, e_th, e_ph (Cartesian unit vectors) at (th, ph=0):
        thv = ths[i]
        er = np.array([np.sin(thv), 0.0, np.cos(thv)])
        eth = np.array([np.cos(thv), 0.0, -np.sin(thv)])
        eph = np.array([0.0, 1.0, 0.0])
        # covariant G in spherical COORDINATE basis -> orthonormal frame:
        # G_orthonormal(i,j) = G_coord(mn) * (d coord^m / d xhat^i)(...)
        # scale factors: h_r=1 (but g_rr includes exp(2b): coordinate-basis
        # tensor components transform with the Jacobian of the coordinate
        # change; use full Jacobian J = d(t,r,th,ph)/d(t,x,y,z) evaluated
        # numerically by finite differences of the coordinate map.
        def sph_coords(p):
            xx, yy, zz = p
            rrv = np.sqrt(xx**2 + yy**2 + zz**2)
            thh = np.arccos(np.clip(zz / max(rrv, 1e-12), -1, 1))
            phh = np.arctan2(yy, xx)
            return np.array([0.0, rrv, thh, phh])
        J = np.zeros((4, 4)); J[0, 0] = 1.0
        eps = 1e-6
        for cc in range(3):
            dp = np.zeros(3); dp[cc] = eps
            J[1:, 1 + cc] = (sph_coords(pt + dp)[1:]
                             - sph_coords(pt - dp)[1:]) / (2 * eps)
        Gcart = J.T @ Gsph @ J
        That_sym = vm.eulerian_that(gfunc(pt[None]),
                                    (Gcart / (8 * np.pi))[None])[0]
        m_sym = vm.hawking_ellis_margins(That_sym[None])
        rows.append({'pt': pt.tolist(), 'r': rr, 'theta': ths[i],
                     'maxdiff_T': float(np.max(np.abs(That_sym - That_fd[i]))),
                     'nec_sym': float(m_sym['nec'][0]),
                     'nec_fd': float(m_fd['nec'][i]),
                     'wec_sym': float(m_sym['wec'][0]),
                     'wec_fd': float(m_fd['wec'][i]),
                     'sec_sym': float(m_sym['sec'][0]),
                     'sec_fd': float(m_fd['sec'][i]),
                     'dec_sym': float(m_sym['dec'][0]),
                     'dec_fd': float(m_fd['dec'][i])})
    md = max(r['maxdiff_T'] for r in rows)
    print(f"{name}: {len(rows)} pts, max |T_sym - T_fd| = {md:.3e}")
    for k in ('nec', 'wec', 'sec', 'dec'):
        print(f"  {k}: sym min {min(r[k+'_sym'] for r in rows):+.6e} | "
              f"fd min {min(r[k+'_fd'] for r in rows):+.6e}")
    json.dump({'config': name, 'rows': rows, 'maxdiff_T': md},
              open(f'results/redteam_R2_{name}.json', 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1])
