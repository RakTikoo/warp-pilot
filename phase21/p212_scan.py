"""
P21-2 scan (float64): numerical audits behind the symbolic identities in
results/p212_identities.json (produced by p212_derive.py).

A. Prescribed-geometry required-T audit (4 registered (Phi, b) combos):
   ECs of the stress-energy GR would REQUIRE; throat DEC identity values;
   Kretschmann finiteness (numeric Riemann evaluator, Schwarzschild-checked).
B. L(F) families (F1, F2a, F2b, F4) on the magnetic trajectory
   F(r) = 2 q_m^2 / r^4, r in [r0, 1e3 r0], r0 = 1: EC margins, L_F range,
   F monotonicity, Bronnikov conditions R1/R3/R4.  Plus the F1 marginal-
   throat anatomy (b'(r0)=1 forward shape, proper-distance divergence).
C. F3 full BI dyonic: constitutive inversion (closed form), EC margins on
   the trajectory, constitutive-formula verification, and the prescribed-
   shape reconstruction residual (overdetermination measure).
"""
import json
import numpy as np
import sympy as sp
from scipy.optimize import brentq

PI = np.pi
ids = json.load(open('results/p212_identities.json'))
res = {'A_geometry': {}, 'B_LF_families': {}, 'C_F3_dyonic': {}}
rgrid = np.logspace(0, 3, 4000)          # r in [1, 1000], r0 = 1
rs, r0s = sp.symbols('r r0', positive=True)

def lam(expr_str):
    return sp.lambdify((rs, r0s), sp.sympify(expr_str), 'numpy')

# ---------------------------------------------------------------- A
def kretschmann(phi_f, b_f, rr, Mtest=False):
    """Numeric K = R_abcd R^abcd for ds2 = -e^{2Phi} dt2 + dr2/(1-b/r)
    + r2 dOmega2, via Christoffels with analytic r-derivatives supplied by
    phi_f, b_f: each returns (val, d1, d2) arrays.  theta fixed at pi/3
    (K is theta-independent by spherical symmetry)."""
    Phi, Pp, Ppp = phi_f(rr)
    b, bp, bpp = b_f(rr)
    th = np.pi/3.0
    g = np.zeros((4, 4, len(rr))); gi = np.zeros_like(g)
    g[0, 0] = -np.exp(2*Phi); g[1, 1] = 1.0/(1 - b/rr)
    g[2, 2] = rr**2; g[3, 3] = rr**2*np.sin(th)**2
    for i in range(4):
        gi[i, i] = 1.0/g[i, i]
    # Christoffels Gamma^l_{mn} (arrays); only r-derivatives of metric nonzero
    # plus d_theta Gamma^th_phph, Gamma^ph_thph handled analytically.
    N = len(rr)
    Gam = np.zeros((4, 4, 4, N))
    def gp(i):  # d_r g_ii
        return [ -2*np.exp(2*Phi)*Pp, (bp*rr - b)/rr**2/(1 - b/rr)**2,
                 2*rr, 2*rr*np.sin(th)**2 ][i]
    gpr = [gp(i) for i in range(4)]
    # standard diagonal-metric Christoffels:
    Gam[:] = 0.0
    for i in range(4):
        Gam[i, i, 1] = 0.5*gpr[i]/g[i, i]
        Gam[i, 1, i] = Gam[i, i, 1]
        if i != 1:
            Gam[1, i, i] = -0.5*gpr[i]/g[1, 1]
    Gam[2, 3, 3] = -np.sin(th)*np.cos(th)
    Gam[3, 2, 3] = 1.0/np.tan(th); Gam[3, 3, 2] = Gam[3, 2, 3]
    # derivatives: d_r Gamma (numeric, from analytic second derivatives)
    dGam = np.zeros_like(Gam)
    def gpp(i):
        return [ -2*np.exp(2*Phi)*(2*Pp**2 + Ppp),
                 None, 2.0*np.ones(N), 2.0*np.sin(th)**2*np.ones(N) ][i]
    # g_rr second derivative analytically:
    u = 1 - b/rr; up = -(bp*rr - b)/rr**2; upp = -bpp/rr \
        + 2*(bp*rr - b)/rr**3
    grr_pp = -upp/u**2 + 2*up**2/u**3
    gpp1 = grr_pp
    gpps = [gpp(0), gpp1, gpp(2), gpp(3)]
    for i in range(4):
        d = (gpps[i]*g[i, i] - gpr[i]**2)/g[i, i]**2   # d_r (g'_ii/g_ii)
        dGam[i, i, 1] = 0.5*d; dGam[i, 1, i] = 0.5*d
        if i != 1:
            dGam[1, i, i] = -0.5*(gpps[i]*g[1, 1] - gpr[i]*gpr[1])/g[1, 1]**2
    # d_theta derivatives (only two nonzero Gammas depend on theta):
    dGam_th = np.zeros_like(Gam)
    dGam_th[2, 3, 3] = -(np.cos(th)**2 - np.sin(th)**2)
    dGam_th[1, 3, 3] = -2*rr*np.sin(th)*np.cos(th)/g[1, 1]
    dGam_th[3, 2, 3] = -1.0/np.sin(th)**2; dGam_th[3, 3, 2] = dGam_th[3, 2, 3]
    dG = [np.zeros_like(Gam), dGam, dGam_th, np.zeros_like(Gam)]  # d_mu Gam
    # Riemann R^l_{m n p} = d_n Gam^l_{pm} - d_p Gam^l_{nm} + Gam Gam - Gam Gam
    R = np.zeros((4, 4, 4, 4, N))
    for l in range(4):
        for m in range(4):
            for n in range(4):
                for p in range(4):
                    R[l, m, n, p] = dG[n][l, p, m] - dG[p][l, n, m]
                    for k in range(4):
                        R[l, m, n, p] += (Gam[l, n, k]*Gam[k, p, m]
                                          - Gam[l, p, k]*Gam[k, n, m])
    # R_abcd = g_aa R^a_{bcd}; K = sum R_abcd R^abcd with gi raising
    Rabcd = np.zeros_like(R)
    for a in range(4):
        Rabcd[a] = g[a, a][None, None, None, :]*R[a]
    K = np.zeros(N)
    for a in range(4):
        for b_ in range(4):
            for c_ in range(4):
                for d_ in range(4):
                    K += Rabcd[a, b_, c_, d_]**2 * gi[a, a]*gi[b_, b_] \
                        * gi[c_, c_]*gi[d_, d_]
    return K

# Schwarzschild validation of the K evaluator (M = 0.7, b = 2M const)
M = 0.7
def phi_sch(rr):
    u = 1 - 2*M/rr
    return 0.5*np.log(u), M/(rr**2*u), -2*M/(rr**3*u) - 2*M**2/(rr**4*u**2)
def b_sch(rr):
    return np.full_like(rr, 2*M), np.zeros_like(rr), np.zeros_like(rr)
rrK = np.array([3.0, 5.0, 10.0])
Ksch = kretschmann(phi_sch, b_sch, rrK)
Kexact = 48*M**2/rrK**6
res['K_eval_schwarzschild_relerr'] = float(np.max(np.abs(Ksch/Kexact - 1)))

phi_funcs = {
    'phi0': lambda rr: (np.zeros_like(rr), np.zeros_like(rr), np.zeros_like(rr)),
    'phiMT': lambda rr: (-0.5/rr, 0.5/rr**2, -1.0/rr**3),
}
b_funcs = {
    'b1': lambda rr: (1.0/rr, -1.0/rr**2, 2.0/rr**3),
    'b2': lambda rr: (np.sqrt(rr), 0.5/np.sqrt(rr), -0.25*rr**-1.5),
}

for name, ci in ids['combos'].items():
    rho = lam(ci['rho_expr'])(rgrid, 1.0)
    pr = lam(ci['pr_expr'])(rgrid, 1.0)
    pt = lam(ci['pt_expr'])(rgrid, 1.0)
    # throat values (limits) replace r = r0 point
    rho[0] = float(sp.sympify(ci['rho_r0'], locals={'r0': r0s}).subs(r0s, 1.0))
    pr[0] = float(sp.sympify(ci['pr_r0'], locals={'r0': r0s}).subs(r0s, 1.0))
    pt[0] = float(sp.sympify(ci['pt_r0'], locals={'r0': r0s}).subs(r0s, 1.0))
    decr = rho - np.abs(pr); dect = rho - np.abs(pt)
    entry = {
        'bprime_r0': float(sp.sympify(ci['bprime_r0'], locals={'r0': r0s})),
        'rho_r0': rho[0], 'pr_r0': pr[0], 'pt_r0': pt[0],
        'min_NEC1': float(np.min(rho + pr)),
        'NEC1_r0': float(rho[0] + pr[0]),
        'min_NEC2': float(np.min(rho + pt)),
        'min_rho': float(np.min(rho)),
        'min_SEC': float(np.min(rho + pr + 2*pt)),
        'min_DEC_r': float(np.min(decr)), 'min_DEC_t': float(np.min(dect)),
        'DEC_r_margin_r0': float(decr[0]),
        'DEC_r_fail_out_to_r': float(rgrid[np.where(decr < 0)[0][-1]])
        if np.any(decr < 0) else None,
        'all_EC_legal': bool(np.min(rho + pr) >= 0 and np.min(rho + pt) >= 0
                             and np.min(rho) >= 0
                             and np.min(rho + pr + 2*pt) >= 0
                             and np.min(decr) >= 0 and np.min(dect) >= 0),
    }
    bk = 'b1' if name.startswith('b1') else 'b2'
    pk = 'phi0' if name.endswith('phi0') else 'phiMT'
    K = kretschmann(phi_funcs[pk], b_funcs[bk],
                    np.logspace(np.log10(1 + 1e-7), 3, 200))
    entry['K_max_on_domain'] = float(np.max(np.abs(K)))
    entry['K_finite'] = bool(np.all(np.isfinite(K)))
    res['A_geometry'][name] = entry

# ---------------------------------------------------------------- B
def audit_LF(L, LF, F):
    rho = L/(4*PI); pr = -rho; pt = (2*F*LF - L)/(4*PI)
    return {
        'min_rho': float(np.min(rho)), 'min_NEC1': 0.0,
        'min_NEC2': float(np.min(rho + pt)),
        'min_SEC': float(np.min(rho + pr + 2*pt)),
        'min_DEC_r': 0.0, 'min_DEC_t': float(np.min(rho - np.abs(pt))),
        'LF_min': float(np.min(LF)), 'LF_max': float(np.max(LF)),
        'rho_r0': float(rho[0]), 'pt_r0': float(pt[0]),
    }

FAMS = {}
for qm in (0.5, 1.0, 2.0):
    F = 2*qm**2/rgrid**4
    mono = bool(np.all(np.diff(F) < 0))
    for bb in (0.5, 1.0, 2.0, 5.0):
        L = 4*bb**2*(np.sqrt(1 + F/(2*bb**2)) - 1)
        LF = 1/np.sqrt(1 + F/(2*bb**2))
        e = audit_LF(L, LF, F); e['F_monotone_decreasing'] = mono
        e['note'] = 'R3 fails: L ~ sqrt(F) -> infinity as F -> inf'
        FAMS[f'F1_BI_b{bb}_qm{qm}'] = e
    for al in (0.05, 0.2, 1.0):
        L = F*np.exp(-al*F); LF = np.exp(-al*F)*(1 - al*F)
        e = audit_LF(L, LF, F); e['F_monotone_decreasing'] = mono
        e['alphaF_at_r0'] = float(al*F[0])
        e['R3_finite_limit'] = 0.0
        FAMS[f'F2a_exp_a{al}_qm{qm}'] = e
        L = F/(1 + al*F)**2; LF = (1 - al*F)/(1 + al*F)**3
        e = audit_LF(L, LF, F); e['F_monotone_decreasing'] = mono
        e['alphaF_at_r0'] = float(al*F[0])
        e['R3_finite_limit'] = 0.0
        FAMS[f'F2b_rat_a{al}_qm{qm}'] = e
    L = F**2; LF = 2*F
    e = audit_LF(L, LF, F); e['F_monotone_decreasing'] = mono
    e['LF_at_F0'] = 0.0
    FAMS[f'F4_pow2_qm{qm}'] = e
res['B_LF_families'] = FAMS

# F1 marginal-throat anatomy: choose q_m with b'(r0) = 2 r0^2 L(F(r0)) = 1
# exactly (the forward solution's forced throat slope), bb = 1.
bb = 1.0
qm_star = np.sqrt(17.0)/8.0*2  # L=4(sqrt(1+qm^2)-1)=1/2 -> qm^2 = 17/64
qm_star = np.sqrt(17.0/64.0)
F = 2*qm_star**2/rgrid**4
L = 4*(np.sqrt(1 + F/2) - 1)
bprime = 2*rgrid**2*L
bshape = 1.0 + np.concatenate(([0.0],
        np.cumsum(0.5*(bprime[1:] + bprime[:-1])*np.diff(rgrid))))
gap = rgrid - bshape                       # r - b(r); ~ C (r-r0)^2 near r0
near = (rgrid > 1.0) & (rgrid < 1.05)
Cfit = float(np.median(gap[near]/(rgrid[near] - 1.0)**2))
# proper distance from r0+eps to 2 r0 on a dedicated fine grid: if the gap
# is quadratic, ell(eps) grows by ln(10)/sqrt(C) per decade of eps.
rr2 = 1.0 + np.logspace(-7, np.log10(1.0), 40000)
F2_ = 2*qm_star**2/rr2**4
L2_ = 4*(np.sqrt(1 + F2_/2) - 1)
bp2 = 2*rr2**2*L2_
b2_ = 1.0 + np.concatenate(([0.0],
        np.cumsum(0.5*(bp2[1:] + bp2[:-1])*np.diff(rr2))))
integ = 1.0/np.sqrt((rr2 - b2_)/rr2)
ell_eps = {}
for eps in (1e-2, 1e-3, 1e-4, 1e-5):
    m = rr2 >= 1.0 + eps
    ell_eps[f'ell_from_r0+{eps:g}'] = float(np.trapezoid(integ[m], rr2[m]))
res['B_F1_marginal_throat'] = {
    'qm_for_bprime_r0_eq_1': float(qm_star),
    'bprime_r0': float(bprime[0]),
    'gap_quadratic_coeff_C': Cfit,
    'proper_distance_partials': ell_eps,
    'per_decade_growth_expected_ln10_over_sqrtC': float(np.log(10)/np.sqrt(Cfit)),
    'note': 'gap ~ C (r-r0)^2 with C>0 => proper distance to throat '
            'diverges logarithmically: extremal (null) throat, not a '
            'finite-distance traversable throat.',
}

# Marginal-throat redshift anatomy: Phi'(r) = N(r)/(2(r-b(r))) with
# N(r) = 8 pi r^2 p_r + b/r = -2 r^2 L + b/r (p_r = -rho).  N(r0) = 0
# (b'(r0)=1) but r-b(r) ~ C (r-r0)^2, so Phi' ~ N'(r0)/(2C (r-r0)):
# a log-divergent redshift at the throat unless N'(r0) = 0.
Nfun = -2*rr2**2*L2_ + b2_/rr2
h = rr2[1] - rr2[0]
Np0 = float((Nfun[1] - Nfun[0])/h)
res['B_F1_marginal_throat']['Nprime_r0'] = Np0
res['B_F1_marginal_throat']['Phi_prime_near_throat'] = {
    f'r-r0={d:g}': float(Nfun[np.argmin(np.abs(rr2 - (1 + d)))]
                         / (2*(rr2[np.argmin(np.abs(rr2 - (1 + d)))]
                               - b2_[np.argmin(np.abs(rr2 - (1 + d)))])))
    for d in (1e-2, 1e-3, 1e-4)}

# ---------------------------------------------------------------- C
def bi_T(E, B, bb):
    F = 2*(B**2 - E**2); G = 4*E*B
    Delta = 1 + F/(2*bb**2) - G**2/(16*bb**4)
    sq = np.sqrt(Delta)
    L = 4*bb**2*(sq - 1); LF = 1/sq; LG = -G/(4*bb**2*sq)
    rho = (-E*(B*LG - E*LF) + L/4)/PI
    pr = -rho
    pt = (B*(B*LF + E*LG) - L/4)/PI
    return rho, pr, pt, L, LF, LG, Delta

C = {}
for qm in (0.5, 1.0, 2.0):
    for qe in (0.5, 1.0):
        for bb in (1.0, 2.0):
            B = qm/rgrid**2; D = qe/rgrid**2
            E = np.sqrt(D**2/(1 + B**2/bb**2 + D**2/bb**2))
            rho, pr, pt, L, LF, LG, Delta = bi_T(E, B, bb)
            qe_check = rgrid**2*(LF*E - LG*B)
            e = {
                'min_rho': float(np.min(rho)), 'min_NEC1': 0.0,
                'min_NEC2': float(np.min(rho + pt)),
                'min_SEC': float(np.min(rho + pr + 2*pt)),
                'min_DEC_r': 0.0,
                'min_DEC_t': float(np.min(rho - np.abs(pt))),
                'LF_min': float(np.min(LF)), 'LF_max': float(np.max(LF)),
                'Delta_min': float(np.min(Delta)),
                'E_over_b_max': float(np.max(E/bb)),
                'constitutive_qe_relerr': float(
                    np.max(np.abs(qe_check/qe - 1))),
                'rho_r0': float(rho[0]), 'pt_r0': float(pt[0]),
            }
            C[f'F3_qm{qm}_qe{qe}_b{bb}'] = e
res['C_F3_dyonic'] = C

# Reconstruction residual on the best prescribed combo (b2_phiMT):
ci = ids['combos']['b2_phiMT']
rho_req = lam(ci['rho_expr'])(rgrid, 1.0)
pt_req = lam(ci['pt_expr'])(rgrid, 1.0)
pr_req = lam(ci['pr_expr'])(rgrid, 1.0)
rho_req[0] = float(sp.sympify(ci['rho_r0'], locals={'r0': r0s}).subs(r0s, 1.0))
pt_req[0] = float(sp.sympify(ci['pt_r0'], locals={'r0': r0s}).subs(r0s, 1.0))
pr_req[0] = float(sp.sympify(ci['pr_r0'], locals={'r0': r0s}).subs(r0s, 1.0))
for qm, bb in ((1.0, 2.0), (0.5, 1.0)):
    B = qm/rgrid**2
    Esol = np.full_like(rgrid, np.nan); ok = np.zeros(len(rgrid), bool)
    for i in range(len(rgrid)):
        f = lambda EE: bi_T(np.array([EE]), np.array([B[i]]), bb)[0][0] \
            - rho_req[i]
        lo, hi = f(0.0), f(0.999*bb)
        if lo*hi < 0:
            Esol[i] = brentq(f, 0.0, 0.999*bb, xtol=1e-14)
            ok[i] = True
    rho_b, pr_b, pt_b, L_b, LF_b, LG_b, D_b = bi_T(
        np.where(ok, Esol, 0.0), B, bb)
    qe_traj = rgrid**2*(LF_b*Esol - LG_b*B)
    rhoBI_at_r0_E0 = float(bi_T(np.array([0.0]), np.array([B[0]]), bb)[0][0])
    res['C_F3_dyonic'][f'recon_b2phiMT_qm{qm}_b{bb}'] = {
        'fraction_radii_with_E_solution': float(np.mean(ok)),
        'E_solution_at_r0': bool(ok[0]),
        'rho_req_r0': float(rho_req[0]),
        'rho_BI_min_at_r0_over_E': rhoBI_at_r0_E0,
        'NEC1_req_at_r0': float(rho_req[0] + pr_req[0]),
        'fraction_radii_with_E_solution': float(np.mean(ok)),
        'pr_residual_max': float(np.max(np.abs(
            (pr_b - pr_req)[ok]))) if ok.any() else None,
        'NEC1_req_max_abs': float(np.max(np.abs(rho_req + pr_req))),
        'pt_residual_max': float(np.max(np.abs((pt_b - pt_req)[ok])))
        if ok.any() else None,
        'qe_traj_rel_drift': float(
            np.max(np.abs(qe_traj[ok]/qe_traj[ok][0] - 1))) if ok.any()
        else None,
    }

with open('results/p212_results.json', 'w') as f:
    json.dump(res, f, indent=1)
print('K eval Schwarzschild relerr:', res['K_eval_schwarzschild_relerr'])
for n, e in res['A_geometry'].items():
    print(n, {k: e[k] for k in ('bprime_r0', 'rho_r0', 'min_NEC1', 'min_rho',
          'min_DEC_r', 'DEC_r_fail_out_to_r', 'all_EC_legal', 'K_finite')})
print('F1 marginal:', res['B_F1_marginal_throat'])
for n in ('F1_BI_b1.0_qm1.0', 'F2a_exp_a0.2_qm1.0', 'F2b_rat_a0.2_qm1.0',
          'F4_pow2_qm1.0'):
    print(n, FAMS[n])
for n in ('F3_qm1.0_qe1.0_b2.0', 'recon_b2phiMT_qm1.0_b2.0'):
    print(n, C[n])
