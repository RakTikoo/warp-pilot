"""redteam_sym3.py — R2, restructured: SymPy derives the Christoffel
symbols AND their derivatives symbolically in spherical coordinates
(ph=0 plane) from the shell metric (a, b, S symbolic functions of r,
th symbolic). The expressions are lambdified with derivative
placeholders; the Ricci/Einstein contractions (finite sums) are then
evaluated numerically per sample point. The derivation path (metric
-> Gamma -> dGamma) is exact symbolic algebra in an independent
coordinate system; no FD or AD of the metric is used anywhere.
Usage: ./venv/bin/python redteam_sym3.py finalist_A
"""
import json, sys, time
import numpy as np
import sympy as sp
import shell as sh
import verify_metric as vm
import redteam as rt

t0 = time.time()
# Spherical coordinates with polar axis = +x (the shift axis), so the
# configuration is genuinely axisymmetric: NO ph dependence anywhere.
# x = r cos(th), y = r sin(th) sin(ph), z = r sin(th) cos(ph).
# Shift along +x: beta_r = -beta S cos(th), beta_th = +beta S r sin(th),
# beta_ph = 0.
t, r, th = sp.symbols('t r th', positive=True)
a = sp.Function('a')(r)
b = sp.Function('b')(r)
S = sp.Function('S')(r)
beta = sp.symbols('beta')
coords = [t, r, th, sp.symbols('ph')]

g = sp.zeros(4, 4)
g[0, 0] = -sp.exp(2 * a)
g[0, 1] = g[1, 0] = -beta * S * sp.cos(th)
g[0, 2] = g[2, 0] = beta * S * r * sp.sin(th)
g[1, 1] = sp.exp(2 * b)
g[2, 2] = r ** 2
g[3, 3] = r ** 2 * sp.sin(th) ** 2
gi = np.array(g.inv(), dtype=object)
print(f'[{time.time()-t0:.0f}s] metric inverted', flush=True)

dg = np.zeros((4, 4, 4), dtype=object)
for s in range(3):  # t-derivatives vanish (stationary); ph: axisymmetry
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

dG = np.zeros((4, 4, 4, 4), dtype=object)  # dG[s, lam, mu, nu], s in r,th
for s, coord in ((1, r), (2, th)):
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                dG[s, lam, mu, nu] = Gamma[lam, mu, nu].diff(coord)
print(f'[{time.time()-t0:.0f}s] dGamma done', flush=True)

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

ARGS = (r, th, beta, av, a1, a2, bv, b1, b2, Sv, S1, S2)
Gam_f = {}
for lam in range(4):
    for mu in range(4):
        for nu in range(4):
            e = Gamma[lam, mu, nu].subs(subs_map)
            Gam_f[(lam, mu, nu)] = sp.lambdify(ARGS, e, 'numpy')
dG_f = {}
for s in (1, 2):
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                e = dG[s, lam, mu, nu].subs(subs_map)
                dG_f[(s, lam, mu, nu)] = sp.lambdify(ARGS, e, 'numpy')
gi_f = {}
for mu in range(4):
    for nu in range(4):
        gi_f[(mu, nu)] = sp.lambdify(ARGS, gi[mu, nu].subs(subs_map),
                                     'numpy')
g_f = {}
for mu in range(4):
    for nu in range(4):
        g_f[(mu, nu)] = sp.lambdify(ARGS, g[mu, nu].subs(subs_map),
                                    'numpy')
print(f'[{time.time()-t0:.0f}s] lambdified', flush=True)


def einstein_sph(vals):
    Gam = np.array([[[float(Gam_f[(l, m, n)](*vals))
                      for n in range(4)] for m in range(4)]
                    for l in range(4)])
    dGam = np.zeros((4, 4, 4, 4))
    for s in (1, 2):
        for l in range(4):
            for m in range(4):
                for n in range(4):
                    dGam[s, l, m, n] = float(dG_f[(s, l, m, n)](*vals))
    # Ricci: R_mn = d_l Gam^l_mn - d_n Gam^l_ml + Gam^l_ls Gam^s_mn
    #                - Gam^l_ns Gam^s_ml   (sum over l, s)
    Ric = (np.einsum('llmn->mn', dGam)
           - np.einsum('nlml->mn', dGam)
           + np.einsum('lls,smn->mn', Gam, Gam)
           - np.einsum('lns,sml->mn', Gam, Gam))
    gim = np.array([[float(gi_f[(m, n)](*vals)) for n in range(4)]
                    for m in range(4)])
    gm = np.array([[float(g_f[(m, n)](*vals)) for n in range(4)]
                   for m in range(4)])
    Rsc = float(np.sum(gim * Ric))
    return Ric - 0.5 * Rsc * gm


def main(name):
    cfg = rt.load_cfg(name)
    prof = rt.build_profiles(cfg)
    from scipy.interpolate import CubicSpline
    a_s = CubicSpline(prof['r'], prof['a'])
    b_s = CubicSpline(prof['r'], prof['b'])
    R1, R2 = cfg['R1'], cfg['R2']
    lo, hi = cfg['ws']

    def S_of(rr):
        if rr <= lo:
            return 1.0
        if rr >= hi:
            return 0.0
        u = (rr - lo) / (hi - lo)
        return 0.5 * (1 + np.cos(np.pi * u))

    def Sp_of(rr):
        if rr <= lo or rr >= hi:
            return 0.0
        u = (rr - lo) / (hi - lo)
        return -0.5 * np.pi / (hi - lo) * np.sin(np.pi * u)

    def Spp_of(rr):
        if rr <= lo or rr >= hi:
            return 0.0
        u = (rr - lo) / (hi - lo)
        return -0.5 * (np.pi / (hi - lo)) ** 2 * np.cos(np.pi * u)

    gfunc = sh.shell_point_factory(prof, cfg['beta'], cfg['shift_kind'], 1.0,
                                   cfg['ws'])
    rad = [0.6 * R1] + [R1 + f * (R2 - R1)
                        for f in (0.05, 0.25, 0.5, 0.75, 0.95)] + [1.2 * R2]
    pts, ths = [], []
    for rr in rad:
        for thv in (np.pi / 2, np.pi / 4, 0.3):
            # ph=0 plane: x = r cos(th), z = r sin(th), y = 0
            pts.append([rr * np.cos(thv), 0.0, rr * np.sin(thv)])
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
        Gsph = einstein_sph(vals)

        def sph_coords(p):
            xx, yy, zz = p
            rrv = np.sqrt(xx**2 + yy**2 + zz**2)
            thh = np.arccos(np.clip(xx / max(rrv, 1e-12), -1, 1))
            phh = np.arctan2(yy, zz)
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
