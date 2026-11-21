"""
mg1_symbolic_check.py — G1 symbolic slice check for the f(R) module.

Static spherical subcase of the MG-1 ansatz (v_s = 0):
    ds^2 = -exp(2A(r)) dt^2 + exp(4C(r)) (dr^2 + r^2 dOmega^2),
    A = aA exp(-((r-R)/Delta)^2),  C = aC exp(-((r-R)/Delta)^2).
SymPy computes R, F = 1 + 2 alpha R, nabla nabla F, Box F and
    8 pi T_m = F R_mn - (1/2) f g_mn - nabla_m nabla_n F + g_mn Box F
exactly (rational arithmetic on explicit expressions), giving
rho_m = -T^t_t, p_r = T^r_r, p_t = T^th_th at sample radii.
The JAX engine must reproduce these numbers at (r, 0, 0).
"""
import numpy as np
import sympy as sp


def symbolic_Tm_eigs(rvals, aA, aC, R, Delta, alpha):
    r, th = sp.symbols('r th', positive=True)
    A = aA * sp.exp(-(((r - R) / Delta) ** 2))
    C = aC * sp.exp(-(((r - R) / Delta) ** 2))
    coords = sp.symbols('t r th ph')
    t, rr, th_, ph = coords
    g = sp.diag(-sp.exp(2 * A), sp.exp(4 * C), sp.exp(4 * C) * r ** 2,
                sp.exp(4 * C) * r ** 2 * sp.sin(th) ** 2)
    gi = g.inv()
    xs = [t, r, th, ph]
    # Christoffel
    Gam = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                expr = 0
                for s in range(4):
                    expr += gi[lam, s] * (sp.diff(g[nu, s], xs[mu])
                                          + sp.diff(g[mu, s], xs[nu])
                                          - sp.diff(g[mu, nu], xs[s])) / 2
                Gam[lam][mu][nu] = sp.simplify(expr)
    # Ricci: R_{sm} = d_r Gam^r_{ms} - d_m Gam^r_{rs} + Gam Gam - Gam Gam
    Ric = sp.zeros(4, 4)
    for s in range(4):
        for m in range(4):
            expr = 0
            for rho in range(4):
                expr += sp.diff(Gam[rho][m][s], xs[rho]) - sp.diff(Gam[rho][rho][s], xs[m])
                for lam in range(4):
                    expr += Gam[rho][rho][lam] * Gam[lam][m][s] - Gam[rho][m][lam] * Gam[lam][rho][s]
            Ric[s, m] = sp.simplify(expr)
    Rsc = sp.simplify(sum(gi[s, m] * Ric[s, m] for s in range(4) for m in range(4)))
    F = 1 + 2 * alpha * Rsc
    f = Rsc + alpha * Rsc ** 2
    dF = [sp.diff(F, xs[k]) for k in range(4)]
    nabnabF = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            expr = sp.diff(dF[nu], xs[mu])
            for lam in range(4):
                expr -= Gam[lam][mu][nu] * dF[lam]
            nabnabF[mu, nu] = expr
    boxF = sp.simplify(sum(gi[mu, nu] * nabnabF[mu, nu] for mu in range(4) for nu in range(4)))
    Tm = (F * Ric - sp.Rational(1, 2) * f * g - nabnabF + g * boxF) / (8 * sp.pi)
    Tmix = gi * Tm   # mixed tensor T^mu_nu (diagonal metric: componentwise)
    out = []
    for rv in rvals:
        sub = {r: rv, th: sp.pi / 2}
        rho_m = float(-Tmix[0, 0].subs(sub))
        p_r = float(Tmix[1, 1].subs(sub))
        p_t = float(Tmix[2, 2].subs(sub))
        out.append((rv, rho_m, p_r, p_t))
    return out


if __name__ == '__main__':
    import mg1_fr as mg
    import verify_metric as vm
    aA, aC, R, Delta, alpha = 0.3, -0.2, 1.0, 0.25, 0.7
    rvals = [0.6, 0.85, 1.0, 1.15, 1.4]
    sym = symbolic_Tm_eigs(rvals, aA, aC, R, Delta, alpha)
    gf = mg.make_metric(0.0, R, Delta, aA, aC, 0.0)
    pts = np.array([[rv, 0.0, 0.0] for rv in rvals])
    Tm, Te, Rsc, F = mg.tensors_at_points(gf, pts, alpha)
    print(f"{'r':>5} {'rho_m sym':>12} {'rho_m jax':>12} {'p_r sym':>12} {'p_r jax':>12} {'p_t sym':>12} {'p_t jax':>12}")
    for i, (rv, rho_s, pr_s, pt_s) in enumerate(sym):
        g = np.asarray(gf(pts[i]))
        That = vm.eulerian_that(g, np.asarray(Tm[i]))
        print(f"{rv:5.2f} {rho_s:12.6f} {That[0,0]:12.6f} {pr_s:12.6f} {That[1,1]:12.6f} {pt_s:12.6f} {That[2,2]:12.6f}")
