# Gate-5 worker W-A: G5-1/G5-2(d) -- f(T) BHL independent verification.
# FRESH code. Inputs: ONLY the printed equations of Boehmer-Harko-Lobo,
# arXiv:1110.5756 (PRD 85, 044033), transcribed by hand from the paper:
#   action (8); tetrad below (10); T (11); field eqs (13)-(15);
#   T=0 family (17)-(19); NEC (20),(21); throat (22)-(24);
#   Ellis beta (26); redshift (27); profiles (28)-(30); NEC (31),(32);
#   TEGR (33)-(35).
# Phase-20 scripts are NOT used. Phase JSONs read only at the end (compare).
# Units: r0 = 1, |f_T(0)| = 1, profiles quoted as 4*pi*(.)*r0^2/|f_T(0)|.
import json
import numpy as np
import sympy as sp

r = sp.symbols('r', positive=True)
fT = sp.symbols('fT')          # f_T(0), sign kept symbolic where possible
s = sp.sqrt(1 - 1/r**2)        # s = sqrt(1 - beta/r), beta = 1/r (r0=1)

out = {}

# ----------------------------------------------------------------------------
# Background functions from printed (26),(27): beta = r0^2/r, e^a = (1+s)/2
# ----------------------------------------------------------------------------
a = sp.log((1 + s)/2)
ap = sp.diff(a, r)
app = sp.diff(ap, r)
# check r a' = (1-s)/s  (the T=0 condition from printed (11): e^{b/2}=1/s,
# second factor e^{b/2}-1-r a' must vanish)
out['ra_prime_check'] = sp.simplify(r*ap - (1-s)/s)   # expect 0

# Torsion scalar from printed (11): T = 2 e^{-b} (e^{b/2}-1)(e^{b/2}-1-r a')/r^2
eb = s**2                       # e^{-b} = 1 - beta/r
Texpr = 2*eb*(1/s - 1)*(1/s - 1 - r*ap)/r**2
out['T_symbolic'] = sp.simplify(Texpr)                # expect 0

# b(r) = -log(1-1/r^2); b' needed in printed (13)
b = -sp.log(1 - 1/r**2)
bp = sp.diff(b, r)

# ----------------------------------------------------------------------------
# Printed general field equations (13)-(15) at T=0, T'=0, f(0)=0.
# (13): 4 pi rho = e^{-b/2}/r (1-e^{-b/2}) T' f_TT - (T/4 - 1/(2r^2)) f_T
#                  + e^{-b}/(2 r^2) (r b' - 1) f_T - f/4
# (14): 4 pi p_r = [-1/(2r^2) + T/4 + e^{-b}(1 + r a')/(2 r^2)] f_T - f/4
# (15): 4 pi p_t = e^{-b}/2 (a'/2 + 1/r - e^{b/2}/r) T' f_TT
#                  + f_T { T/4 + e^{-b}/(2r) [ (1/2 + r a'/4)(a'-b')
#                                             + r a''/2 ] } - f/4
# ----------------------------------------------------------------------------
rho13 = fT*(1/(2*r**2) + eb*(r*bp - 1)/(2*r**2))
pr14 = fT*(-1/(2*r**2) + eb*(1 + r*ap)/(2*r**2))
pt15 = fT*(eb/(2*r)*( (sp.Rational(1, 2) + r*ap/4)*(ap - bp) + r*app/2 ))

rho13s = sp.simplify(rho13)
pr14s = sp.simplify(pr14)
pt15s = sp.simplify(pt15)
out['rho_from_Eq13'] = str(rho13s)     # expect -fT/(2 r^4)
out['pr_from_Eq14_branchB'] = str(pr14s)
out['pt_from_Eq15'] = str(pt15s)

# Printed T=0 family (17),(18) at f(0)=0:
# (17): 4 pi rho = beta'/(2 r^2) f_T ; beta' = -1/r^2
rho17 = fT*(-1/r**2)/(2*r**2)
out['Eq13_minus_Eq17'] = sp.simplify(rho13s - rho17)   # expect 0
# (18): 4 pi p_r = -1/(2 r^2) [1 - (1-beta/r)(1 + r a')] f_T
pr18 = -fT*(1 - eb*(1 + r*ap))/(2*r**2)
out['Eq14_minus_Eq18'] = sp.simplify(pr14s - pr18)     # expect 0

# Printed specific profiles (28),(29),(30) with f_T(0) = -|f_T| (EC window):
absfT = sp.symbols('absfT', positive=True)
rho28 = absfT/(2*r**4)
pr29 = absfT*((s - 1) + 1/r**2)/(2*r**2)
pt30 = absfT*((s - 1) - 1/(2*r**2))/(4*r**2)

# Branch B profiles: (13)/(14)/(15) with f_T -> -absfT
rhoB = sp.simplify(rho13s.subs(fT, -absfT))
prB = sp.simplify(pr14s.subs(fT, -absfT))
ptB = sp.simplify(pt15s.subs(fT, -absfT))
out['pr_branchB_closed_form'] = str(prB)               # expect absfT (1-s)/(2 r^2)
out['rho28_minus_rhoB'] = sp.simplify(rho28 - rhoB)    # expect 0
out['pt30_minus_ptB'] = sp.simplify(pt30 - ptB)        # expect 0
out['pr29_minus_prB'] = sp.simplify(pr29 - prB)        # the misprint difference

# Printed NEC combinations (31),(32) vs profile sums:
nec1_31 = absfT*(1 + 1/r**2 - s)/(2*r**2)
nec2_32 = absfT*(3/(2*r**2) - 1 + s)/(4*r**2)
out['Eq31_minus_branchB_sum'] = sp.simplify(nec1_31 - (rhoB + prB))  # expect 0
out['Eq32_minus_branchB_sum'] = sp.simplify(nec2_32 - (rhoB + ptB))  # expect 0
out['Eq31_minus_branchA_sum'] = sp.simplify(nec1_31 - (rho28 + pr29))  # expect nonzero

# Throat limits (r -> 1+):  s -> 0
def throat(expr):
    return float(sp.limit(expr/absfT, r, 1, dir='+'))
out['throat_branchB'] = {'rho': throat(rhoB), 'pr': throat(prB), 'pt': throat(ptB),
                         'NEC1': throat(rhoB + prB), 'NEC2': throat(rhoB + ptB)}
out['throat_branchA_printed'] = {'rho': throat(rho28), 'pr': throat(pr29),
                                 'pt': throat(pt30), 'NEC1': throat(rho28 + pr29),
                                 'NEC2': throat(rho28 + pt30)}

# ----------------------------------------------------------------------------
# EC scan on (1, 1e4], both branches, f_T(0) = -1 (legal) and +1 (control)
# ECs in phase convention: rho>=0, NEC1=rho+pr, NEC2=rho+pt,
# DEC_r = rho-|pr|, DEC_t = rho-|pt|  (all in units 4 pi (.) r0^2/|f_T|)
# ----------------------------------------------------------------------------
def lam(expr, fTval):
    return sp.lambdify(r, expr.subs({fT: fTval, absfT: abs(fTval)}), 'numpy')

grid = np.concatenate([1 + np.logspace(-9, -2, 400),
                       np.linspace(1.011, 2, 400),
                       np.logspace(np.log10(2), 4, 800)])
grid = np.unique(grid)

def ec_scan(rho_e, pr_e, pt_e, fTval):
    R, P, Tt = lam(rho_e, fTval)(grid), lam(pr_e, fTval)(grid), lam(pt_e, fTval)(grid)
    ecs = {'rho': R, 'NEC1': R + P, 'NEC2': R + Tt,
           'DEC_r': R - np.abs(P), 'DEC_t': R - np.abs(Tt)}
    return {k: {'min': float(np.min(v)), 'holds': bool(np.min(v) >= -1e-12)}
            for k, v in ecs.items()}

out['EC_branchB_fT=-1'] = ec_scan(rho13s, pr14s, pt15s, -1.0)
out['EC_branchB_fT=+1'] = ec_scan(rho13s, pr14s, pt15s, +1.0)
out['EC_branchA_fT=-1'] = ec_scan(rho28, pr29, pt30, -1.0)
out['EC_branchA_fT=+1'] = ec_scan(rho28, pr29, pt30, +1.0)

# ----------------------------------------------------------------------------
# Conservation: p_r' + (a'/2)(rho + p_r) + (2/r)(p_r - p_t) = 0 ?
# (nabla_mu T^mu_r = 0 for g_tt = e^{a}; paper states conservation is
#  ensured by the field equations, below printed (9).)
# ----------------------------------------------------------------------------
def cons_resid(rho_e, pr_e, pt_e):
    expr = sp.diff(pr_e, r) + (ap/2)*(rho_e + pr_e) + (2/r)*(pr_e - pt_e)
    return sp.simplify(expr)

consB = cons_resid(rhoB, prB, ptB)
consA = cons_resid(rho28, pr29, pt30)
out['cons_branchB_symbolic'] = str(consB)      # expect 0
out['cons_branchA_symbolic'] = str(consA)      # expect closed form != 0
fA = sp.lambdify(r, consA/absfT, 'numpy')
out['cons_branchA_maxabs_grid'] = float(np.max(np.abs(fA(grid))))
out['cons_branchA_maxabs_r>2'] = float(np.max(np.abs(fA(grid[grid > 2]))))
for rr in [1 + 1e-7, 1 + 1e-5, 1 + 1e-3, 1.01, 1.5, 2.0, 10.0]:
    out[f'cons_branchA_at_{rr}'] = float(fA(np.array([rr]))[0])

# ----------------------------------------------------------------------------
# TEGR control from printed (33),(34): f(T)=T, same beta and a(r):
# (33): 4 pi rho = beta'/(2 r^2) ; (34): 4 pi p_r = [-beta/r + (1-beta/r) r a']/(2 r^2)
# ----------------------------------------------------------------------------
rho33 = (-1/r**2)/(2*r**2)
pr34 = (-1/r + eb*r*ap)/(2*r**2)
out['TEGR_throat'] = {'rho': float(sp.limit(rho33, r, 1, dir='+')),
                      'pr': float(sp.limit(pr34, r, 1, dir='+')),
                      'NEC1': float(sp.limit(rho33 + pr34, r, 1, dir='+'))}

# ----------------------------------------------------------------------------
# G5-1 mechanism check: is delta_1 T = 0 for tensor (TT) perturbations of
# the BHL off-diagonal tetrad?  Perturb e^i_mu -> e^i_nu (delta + eps/2 H),
# H^theta_theta = -H^phi_phi = u(r), H^theta_phi = H^phi_theta (symmetrised
# mixed) = v(r): trace-free angular block. Compute T(eps) from the
# DEFINITIONS printed as (4)-(7) and extract the O(eps) coefficient
# numerically (central difference, eps=1e-3,1e-4) at sample radii.
# ----------------------------------------------------------------------------
import mpmath as mp
mp.mp.dps = 30

def tetrad(rv, th, ph, eps, u, v):
    # BHL off-diagonal tetrad (printed below eq. (10)), a,b for Ellis bg.
    sv = mp.sqrt(1 - 1/rv**2)
    ea = (1 + sv)/2            # e^{a/2} squared factor: e^a = (1+s)/2 -> e^{a/2}=sqrt
    Ea = mp.sqrt((1 + sv)/2)   # e^{a/2}
    Eb = 1/sv                  # e^{b/2}
    e = mp.matrix(4, 4)
    e[0, 0] = Ea
    e[1, 1] = Eb*mp.sin(th)*mp.cos(ph); e[1, 2] = rv*mp.cos(th)*mp.cos(ph); e[1, 3] = -rv*mp.sin(th)*mp.sin(ph)
    e[2, 1] = Eb*mp.sin(th)*mp.sin(ph); e[2, 2] = rv*mp.cos(th)*mp.sin(ph); e[2, 3] = rv*mp.sin(th)*mp.cos(ph)
    e[3, 1] = Eb*mp.cos(th);          e[3, 2] = -rv*mp.sin(th);           e[3, 3] = 0
    if eps != 0:
        # apply (delta + eps/2 H) on the coordinate index: angular block only
        H = {(2, 2): u, (3, 3): -u, (2, 3): v, (3, 2): v}
        en = mp.matrix(4, 4)
        for i in range(4):
            for mu in range(4):
                val = e[i, mu]
                for nu in range(4):
                    if (nu, mu) in H:
                        val += eps/2 * e[i, nu] * H[(nu, mu)]
                en[i, mu] = val
        e = en
    return e

def torsion_scalar(rv, th, ph, eps, u, v, h=mp.mpf('1e-4')):
    # T = S_sigma^{mu nu} T^sigma_{mu nu} from printed (4),(5),(6),(7),
    # all indices handled in coordinate basis with eta = diag(1,-1,-1,-1).
    coords = [mp.mpf(0), rv, th, ph]
    def E(x):
        return tetrad(x[1], x[2], x[3], eps, u, v)
    e0 = E(coords)
    ei = e0**-1                      # e_i^mu (rows: frame i? careful) -- e0[i,mu]; inverse gives e_i^mu as [mu,i] transposed below
    # derivatives d_mu e^i_nu by central differences
    de = {}
    for mu in range(4):
        xp = list(coords); xm = list(coords)
        hh = h if mu != 0 else h
        xp[mu] += hh; xm[mu] -= hh
        de[mu] = (E(xp) - E(xm))/(2*hh)
    eta = mp.diag([1, -1, -1, -1])
    # metric and inverse
    g = mp.matrix(4, 4)
    for mu in range(4):
        for nu in range(4):
            g[mu, nu] = sum(eta[i, i]*e0[i, mu]*e0[i, nu] for i in range(4))
    gi = g**-1
    # e_i^mu : inverse tetrad with frame index lowered: EInv[mu, i] = e_i^mu? 
    # e0[i,mu]; its matrix inverse Minv[mu,i] satisfies Minv[mu,i] e0[i,nu] = delta.
    # e_i^mu = Minv[mu, i'] eta_{i' i}... we need T^sigma_{mu nu} =
    # e_i^sigma (d_mu e^i_nu - d_nu e^i_mu) with e_i^sigma = sum_j eta_ij Minv[sigma, j]
    Minv = e0**-1
    def eup(sig, i):   # e_i^sigma
        return sum(eta[j, j]*Minv[sig, j] for j in range(4) if j == i) * 1 if False else Minv[sig, i]
    # NOTE: Minv[sigma, i] IS e_i^sigma when e0 rows are frame index with
    # eta already accounted? g = e^T eta e used Minv = e^{-1}: e_i^mu defined
    # by e_i^mu e^i_nu = delta^mu_nu -> e_i^mu = Minv[mu, i]. Use that.
    Ttor = {}
    for sig in range(4):
        for mu in range(4):
            for nu in range(4):
                Ttor[sig, mu, nu] = sum(Minv[sig, i]*(de[mu][i, nu] - de[nu][i, mu]) for i in range(4))
    # raise/lower: T^mu nu_sigma etc. Build fully covariant/contravariant as needed.
    # K^{mu nu}{}_sigma = -1/2 (T^{mu nu}{}_sigma - T^{nu mu}{}_sigma - T_sigma{}^{mu nu})
    def Tup(sig, mu, nu):   # T^sigma_{mu nu} already
        return Ttor[sig, mu, nu]
    def Tcov(sig, mu, nu):  # T_{sigma mu nu}
        return sum(g[sig, s2]*Ttor[s2, mu, nu] for s2 in range(4))
    def Tmix_up(sig_up, mu_lo, nu_up):  # T^{sigma mu}{}_nu ... build via components
        pass
    # S_sigma^{mu nu} = 1/2 (K^{mu nu}{}_sigma + delta^mu_sigma T^{rho nu}{}_rho
    #                        - delta^nu_sigma T^{rho mu}{}_rho)
    # K^{mu nu}{}_sigma: raise mu,nu of K_{..}: first build K^mu nu_sigma from T:
    # K^{mu}{}_{nu sigma} = -1/2( T^mu_{nu sigma} - T_{nu}{}^mu{}_sigma - T_{sigma}{}^mu{}_nu )
    # Work with components T[a][b][c] = T^a_{b c}; define helpers by index gymnastics.
    def T1(a, b, c):  # T^a_{bc}
        return Ttor[a, b, c]
    def T_down(a, b, c):  # T_{abc}
        return Tcov(a, b, c)
    def T_up3(a, b, c):  # T^{abc}
        return sum(gi[b, b2]*gi[c, c2]*Ttor[a, b2, c2] for b2 in range(4) for c2 in range(4))
    def K_up2(mu, nu, sig):  # K^{mu nu}{}_sigma
        # K^{mu nu}{}_sigma = -1/2 ( T^{mu nu}{}_sigma - T^{nu mu}{}_sigma - T_sigma{}^{mu nu} )
        t1 = sum(gi[nu, n2]*Ttor[mu, n2, sig] for n2 in range(4))          # T^{mu nu}{}_sigma (raise 2nd)
        t2 = sum(gi[mu, m2]*Ttor[nu, m2, sig] for m2 in range(4))          # T^{nu mu}{}_sigma
        t3 = sum(gi[mu, m2]*gi[nu, n2]*Tcov(sig, m2, n2) for m2 in range(4) for n2 in range(4))  # T_sigma{}^{mu nu}
        return -mp.mpf('0.5')*(t1 - t2 - t3)
    def Trho_nu(nu):  # T^{rho nu}{}_rho = sum_rho gi[nu, n2] T^rho_{n2 rho}
        return sum(gi[nu, n2]*Ttor[rho, n2, rho] for rho in range(4) for n2 in range(4))
    Tval = mp.mpf(0)
    for sig in range(4):
        for mu in range(4):
            for nu in range(4):
                S = mp.mpf('0.5')*(K_up2(mu, nu, sig)
                                   + (1 if mu == sig else 0)*Trho_nu(nu)
                                   - (1 if nu == sig else 0)*Trho_nu(mu))
                Tval += S*Ttor[sig, mu, nu]
    return Tval

mech = {}
for rv in [1.5, 2.0, 5.0]:
    for (u, v, tag) in [(mp.mpf('0.7'), mp.mpf(0), 'u-only'),
                        (mp.mpf(0), mp.mpf('0.7'), 'v-only')]:
        for eps in [mp.mpf('1e-3'), mp.mpf('1e-4')]:
            tp = torsion_scalar(rv, mp.pi/2, mp.mpf('0.3'), eps, u, v)
            tm = torsion_scalar(rv, mp.pi/2, mp.mpf('0.3'), -eps, u, v)
            t0 = torsion_scalar(rv, mp.pi/2, mp.mpf('0.3'), mp.mpf(0), u, v)
            lin = (tp - tm)/(2*eps)
            quad = (tp + tm - 2*t0)/eps**2
            mech[f'r={rv}_{tag}_eps={eps}'] = {'T0': float(t0), 'delta1T': float(lin),
                                               'delta2T_coeff': float(quad)}
out['tensor_mechanism_deltaT'] = mech

print(json.dumps({k: v for k, v in out.items() if k != 'tensor_mechanism_deltaT'},
                 indent=1, default=str))
print('MECH:', json.dumps(mech, indent=1))
with open('/home/hatch/workspace/warp-pilot/gate5/results/wa_ft_out.json', 'w') as fh:
    json.dump(out, fh, indent=1, default=str)
