"""
redteam_sym.py — R2: symbolic third path for the frozen finalists.

Computes the Einstein tensor of the shell metric
  g_tt = -exp(2 a(r)),  g_tx = -beta S(r),
  g_ij = delta_ij + (exp(2 b(r)) - 1) x_i x_j / r^2,   r = sqrt(x^2+y^2+z^2)
SYMBOLICALLY in SymPy (a, b, S kept as functions of r; the tensor
algebra is exact). Margins at sample points are then evaluated by
substituting the profiles' spline values and derivatives — so the
derivation path shares no code with the FD auditor or the AD chain.
Compares NEC/WEC/SEC/DEC margins vs the FD point auditor at the same
points. Usage: ./venv/bin/python redteam_sym.py finalist_A
"""
import json, sys, time
import numpy as np
import sympy as sp
import shell as sh
import verify_metric as vm
import redteam as rt

t0 = time.time()
t, x, y, z = sp.symbols('t x y z')
r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
a = sp.Function('a')(r)
b = sp.Function('b')(r)
S = sp.Function('S')(r)
beta = sp.symbols('beta')

coords = [t, x, y, z]
g = sp.zeros(4, 4)
g[0, 0] = -sp.exp(2 * a)
g[0, 1] = g[1, 0] = -beta * S
eb = sp.exp(2 * b) - 1
xs = [x, y, z]
for i in range(3):
    for j in range(3):
        g[1 + i, 1 + j] = (1 if i == j else 0) + eb * xs[i] * xs[j] / r ** 2
gi = g.inv()
print(f'[{time.time()-t0:.0f}s] metric inverted', flush=True)

dg = [[g[mu, nu].diff(coords[s]) for nu in range(4)] for mu in range(4)
      for s in range(4)]
dg = np.array(dg, dtype=object).reshape(4, 4, 4)  # dg[s, mu, nu]
Gamma = np.zeros((4, 4, 4), dtype=object)
for lam in range(4):
    for mu in range(4):
        for nu in range(4):
            expr = 0
            for s in range(4):
                expr += gi[lam, s] * (dg[mu, s, nu] + dg[nu, s, mu]
                                      - dg[s, mu, nu])
            Gamma[lam, mu, nu] = sp.simplify(expr / 2)
print(f'[{time.time()-t0:.0f}s] Christoffel done', flush=True)

dG = np.zeros((4, 4, 4, 4), dtype=object)
for s in range(4):
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                dG[s, lam, mu, nu] = Gamma[lam, mu, nu].diff(coords[s])
print(f'[{time.time()-t0:.0f}s] dGamma done', flush=True)

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

# derivative placeholders for lambdify
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
        Gfuncs[(mu, nu)] = sp.lambdify((x, y, z, beta, av, a1, a2, bv, b1, b2,
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
    rng = np.random.default_rng(11)
    rad = np.array([R1 + f * (R2 - R1) for f in (0.05, 0.25, 0.5, 0.75, 0.95)]
                   + [0.6 * R1, 1.2 * R2])
    dirs = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [2, -1, 1]],
                    dtype=float)
    dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    pts = np.array([rr * d for rr in rad for d in dirs])
    Gfd, That_fd, m_fd = vm.einstein_at_points(gfunc, pts, h=0.03 * R1)
    rows = []
    for i, pt in enumerate(pts):
        rr = float(np.linalg.norm(pt))
        vals = (pt[0], pt[1], pt[2], cfg['beta'],
                float(a_s(rr)), float(a_s(rr, 1)), float(a_s(rr, 2)),
                float(b_s(rr)), float(b_s(rr, 1)), float(b_s(rr, 2)),
                float(S_of(rr)), float(Sp_of(rr)), float(Spp_of(rr)))
        Gsym = np.array([[Gfuncs[(mu, nu)](*vals) for nu in range(4)]
                         for mu in range(4)], dtype=float)
        That_sym = vm.eulerian_that(gfunc(pt[None]), (Gsym / (8 * np.pi))[None])[0]
        m_sym = vm.hawking_ellis_margins(That_sym[None])
        row = {'pt': pt.tolist(), 'r': rr,
               'maxdiff_T': float(np.max(np.abs(That_sym - That_fd[i]))),
               'nec_sym': float(m_sym['nec'][0]), 'nec_fd': float(m_fd['nec'][i]),
               'wec_sym': float(m_sym['wec'][0]), 'wec_fd': float(m_fd['wec'][i]),
               'sec_sym': float(m_sym['sec'][0]), 'sec_fd': float(m_fd['sec'][i]),
               'dec_sym': float(m_sym['dec'][0]), 'dec_fd': float(m_fd['dec'][i])}
        rows.append(row)
    md = max(r['maxdiff_T'] for r in rows)
    print(f"{name}: {len(rows)} pts, max |T_sym - T_fd| = {md:.3e}")
    for k in ('nec', 'wec', 'sec', 'dec'):
        print(f"  {k}: sym min {min(r[k+'_sym'] for r in rows):+.6e} | "
              f"fd min {min(r[k+'_fd'] for r in rows):+.6e}")
    json.dump({'config': name, 'rows': rows, 'maxdiff_T': md},
              open(f'results/redteam_R2_{name}.json', 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1])
