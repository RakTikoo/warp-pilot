"""
W-B GATE-9 G9-2 fresh verifier. Definitions from BDE arXiv:1710.10438 Sec III.B
as transcribed in phase61 run record (shared definitions only; code fresh):
  gamma_tilde = diag(-A/r^2, B/r^2); Rtilde = 2D Ricci scalar of gamma_tilde
  Rtilde_,n = (r/sqrt(B)) dRtilde/dr ; S0^0 = -(4 alpha0/3)[Rtilde_,n], alpha0=alpha_g/2
  Darmois pair: B and K = A'/(A sqrt(B)) continuous.
Rtilde formula derived fresh in this file via sympy from the 2-metric:
  R = (-2 P Q P'' + P P' Q' + Q P'^2)/(2 P^2 Q^2), P=A/r^2, Q=B/r^2.
All deciding evaluations at 40-digit mpmath using ANALYTIC A,B derivatives
(no finite differences, no phase junction code).
"""
import json, sympy as sp
from mpmath import mp, mpf, sqrt as msqrt, log as mlog, exp as mexp, findroot

mp.dps = 40
OUT = {}

# ---------- symbolic derivation of Rtilde formula (fresh) ----------
r_s, t_s = sp.symbols('r t', positive=True)
P_f = sp.Function('P')(r_s); Q_f = sp.Function('Q')(r_s)
g = sp.diag(-P_f, Q_f); ginv = g.inv(); coords = [t_s, r_s]
def d(e, k): return sp.diff(e, coords[k])
Gamma = [[[sum(ginv[k, l]*(d(g[l, j], i)+d(g[l, i], j)-d(g[i, j], l))/2
                for l in range(2)) for j in range(2)] for i in range(2)] for k in range(2)]
Riem = {}
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                e = d(Gamma[i][j][l], k) - d(Gamma[i][j][k], l)
                for m in range(2):
                    e += Gamma[i][k][m]*Gamma[m][j][l] - Gamma[i][l][m]*Gamma[m][j][k]
                Riem[(i, j, k, l)] = sp.simplify(e)
Ric = [[sum(Riem[(i, j, i, l)] for i in range(2)) for l in range(2)] for j in range(2)]
Rsc = sp.simplify(sum(ginv[j, l]*Ric[j][l] for j in range(2) for l in range(2)))
# Expected closed form:
Pp, Qp, Ppp = sp.diff(P_f, r_s), sp.diff(Q_f, r_s), sp.diff(P_f, r_s, 2)
closed = (-2*P_f*Q_f*Ppp + P_f*Pp*Qp + Q_f*Pp**2) / (2*P_f**2*Q_f**2)
assert sp.simplify(Rsc - closed) == 0, "formula mismatch"
OUT['symbolic_Rtilde_formula'] = str(closed)

def Rtilde_from_PQ(P, Pp, Ppp, Q, Qp):
    """mpmath evaluation of the derived formula."""
    return (-2*P*Q*Ppp + P*Pp*Qp + Q*Pp**2) / (2*P**2*Q**2)

def PQ_from_AB(r, A, Ap, App, B, Bp):
    """P=A/r^2, Q=B/r^2 and derivatives."""
    P = A/r**2; Pp = Ap/r**2 - 2*A/r**3; Ppp = App/r**2 - 4*Ap/r**3 + 6*A/r**4
    Q = B/r**2; Qp = Bp/r**2 - 2*B/r**3
    return P, Pp, Ppp, Q, Qp

# ---------- interior family (r0=1): b=r^p, Phi2 ----------
def interior_AB(r, p, a):
    """Returns A,Ap,App,B,Bp analytically (mpmath). Phi=a*L/(1+L), L=ln r."""
    p = mpf(p); a = mpf(a); r = mpf(r)
    L = mlog(r)
    Phi = a*L/(1+L)
    Phip = a/(r*(1+L)**2)
    Phipp = -a*(1+L+2)/(r**2*(1+L)**3)  # d/dr [a/(r(1+L)^2)]
    A = mexp(2*Phi); Ap = 2*Phip*A; App = (2*Phipp + 4*Phip**2)*A
    b = r**p; bp = p*r**(p-1)
    u = 1 - b/r
    B = 1/u; Bp = (bp/r - b/r**2)/u**2
    return A, Ap, App, B, Bp

def interior_Rtilde(r, p, a):
    A, Ap, App, B, Bp = interior_AB(r, p, a)
    return Rtilde_from_PQ(*PQ_from_AB(mpf(r), A, Ap, App, B, Bp))

def interior_Rtilde_n(r, p, a):
    """(r/sqrt(B)) * dRtilde/dr, derivative by analytic sympy-free route:
    differentiate Rtilde formula w.r.t. r using derivative values of P,Q
    obtained from A,B and their 1st-3rd derivatives (all analytic)."""
    p_ = mpf(p); a_ = mpf(a); r = mpf(r)
    L = mlog(r)
    Phi = a_*L/(1+L); Phip = a_/(r*(1+L)**2)
    Phipp = -a_*(1+L+2)/(r**2*(1+L)**3)
    # Phi''' : differentiate Phipp = -a (L+3)/(r^2 (1+L)^3)  [since 1+L+2 = L+3]
    # let h=(L+3)*(1+L)^-3 ; h'=(1/r)[(1+L)^-3 -3(L+3)(1+L)^-4]=(1/r)(1+L)^-4[(1+L)-3(L+3)]=(1/r)(1+L)^-4(-2L-8)
    hp = (1/r)*(1+L)**-4*(-2*L-8)
    Phippp = -a_*(hp/r**2 - 2*(L+3)/(r**3*(1+L)**3))
    A = mexp(2*Phi); Ap = 2*Phip*A; App = (2*Phipp+4*Phip**2)*A
    Appp = (2*Phippp + 12*Phip*Phipp)*A + 2*Phip*App
    b = r**p_; bp = p_*r**(p_-1); bpp = p_*(p_-1)*r**(p_-2); bppp = p_*(p_-1)*(p_-2)*r**(p_-3)
    u = 1-b/r; up = -(bp/r - b/r**2); upp = -(bpp/r - 2*bp/r**2 + 2*b/r**3)
    B = 1/u; Bp = -up/u**2; Bpp = -upp/u**2 + 2*up**2/u**3
    P, Pp, Ppp, Q, Qp = PQ_from_AB(r, A, Ap, App, B, Bp)
    Pppp = Appp/r**2 - 6*App/r**3 + 18*Ap/r**4 - 24*A/r**5
    Qpp = Bpp/r**2 - 4*Bp/r**3 + 6*B/r**4
    # differentiate closed form F(P,Pp,Ppp,Q,Qp)
    # F = N/D, N=-2 P Q Ppp + P Pp Qp + Q Pp^2, D=2 P^2 Q^2
    N = -2*P*Q*Ppp + P*Pp*Qp + Q*Pp**2
    Np = (-2*(Pp*Q*Ppp + P*Qp*Ppp + P*Q*Pppp)
          + (Pp*Pp*Qp + P*Ppp*Qp + P*Pp*Qpp)
          + (Qp*Pp**2 + 2*Q*Pp*Ppp))
    D = 2*P**2*Q**2; Dp = 4*P*Pp*Q**2 + 4*P**2*Q*Qp
    dR = (Np*D - N*Dp)/D**2
    return (r/msqrt(B))*dR

def interior_K(r, p, a):
    A, Ap, App, B, Bp = interior_AB(r, p, a)
    return Ap/(A*msqrt(B)), B

# ---------- MK exterior ----------
GAMMA = mpf('1e-28')  # registered gamma * r0, r0=1 units (gamma=1e-28 m^-1, r0=1 m scale)

def exterior_AB(r, beta, k, gamma=GAMMA):
    r = mpf(r); beta = mpf(beta); k = mpf(k); gamma = mpf(gamma)
    f = 1 - 3*beta*gamma - beta*(2-3*beta*gamma)/r + gamma*r - k*r**2
    fp = beta*(2-3*beta*gamma)/r**2 + gamma - 2*k*r
    fpp = -2*beta*(2-3*beta*gamma)/r**3 - 2*k
    A = f; Ap = fp; App = fpp; B = 1/f; Bp = -fp/f**2
    return A, Ap, App, B, Bp

def exterior_Rtilde(r, beta, k, gamma=GAMMA):
    A, Ap, App, B, Bp = exterior_AB(r, beta, k, gamma)
    return Rtilde_from_PQ(*PQ_from_AB(mpf(r), A, Ap, App, B, Bp))

def exterior_Rtilde_n(r, beta, k, gamma=GAMMA):
    r = mpf(r); beta = mpf(beta); k = mpf(k); gamma = mpf(gamma)
    f = 1 - 3*beta*gamma - beta*(2-3*beta*gamma)/r + gamma*r - k*r**2
    fp = beta*(2-3*beta*gamma)/r**2 + gamma - 2*k*r
    fpp = -2*beta*(2-3*beta*gamma)/r**3 - 2*k
    fppp = 6*beta*(2-3*beta*gamma)/r**4
    A, Ap, App, Appp = f, fp, fpp, fppp
    B = 1/f; Bp = -fp/f**2; Bpp = -fpp/f**2 + 2*fp**2/f**3
    P, Pp, Ppp, Q, Qp = PQ_from_AB(r, A, Ap, App, B, Bp)
    Pppp = Appp/r**2 - 6*App/r**3 + 18*Ap/r**4 - 24*A/r**5
    Qpp = Bpp/r**2 - 4*Bp/r**3 + 6*B/r**4
    N = -2*P*Q*Ppp + P*Pp*Qp + Q*Pp**2
    Np = (-2*(Pp*Q*Ppp + P*Qp*Ppp + P*Q*Pppp)
          + (Pp*Pp*Qp + P*Ppp*Qp + P*Pp*Qpp)
          + (Qp*Pp**2 + 2*Q*Pp*Ppp))
    D = 2*P**2*Q**2; Dp = 4*P*Pp*Q**2 + 4*P**2*Q*Qp
    dR = (Np*D - N*Dp)/D**2
    return (r/msqrt(B))*dR

def darmois_solve(Sigma, p, a, gamma=GAMMA):
    """Solve B_ext=B_int and K_ext=K_int for (beta,k). gamma enters f and f'
    as printed: constant term -3 beta gamma, linear term +gamma r, and the
    3 beta^2 gamma / r piece inside -beta(2-3 beta gamma)/r (quadratic in beta)."""
    Kint, Bint = interior_K(Sigma, p, a)
    ftarget = 1/Bint
    def eqs(beta, k):
        A, Ap, App, B, Bp = exterior_AB(Sigma, beta, k, gamma)
        Kext = Ap/(A*msqrt(B))
        return (B - Bint, Kext - Kint)
    # gamma=0 linear guess: f = 1 - 2 beta/r - k r^2 ; f' = 2 beta/r^2 - 2 k r
    S = mpf(Sigma)
    # solve linear system for guess
    import sympy as _sp
    bb, kk = _sp.symbols('bb kk')
    sol = _sp.solve([1-2*bb/S-kk*S**2-ftarget, 2*bb/S**2-2*kk*S-Kint*msqrt(ftarget)], [bb, kk])
    guess = (mpf(str(sol[bb])), mpf(str(sol[kk])))
    beta, k = findroot(lambda B_, K_: (eqs(B_, K_)[0], eqs(B_, K_)[1]),
                       guess, tol=mpf('1e-35'), maxsteps=100)
    return beta, k

# ---------- ANCHOR (i): flat ----------
# A=B=1: P=Q=1/r^2 at r=7.3 (any r)
rr = mpf('7.3')
P = 1/rr**2; Pp = -2/rr**3; Ppp = 6/rr**4; Q = 1/rr**2; Qp = -2/rr**3
OUT['anchor_flat_Rtilde'] = str(Rtilde_from_PQ(P, Pp, Ppp, Q, Qp))

# ---------- ANCHOR (iii): Phi=0 slice symbolic ----------
p_s = sp.symbols('p', positive=True)
# Phi=0: A=1, B=1/(1-r^(p-1)); P=r^-2, Q=B r^-2. Compute Rtilde symbolically.
B_s = 1/(1-r_s**(p_s-1))
P_s = r_s**-2; Q_s = B_s*r_s**-2
Rt_s = (-2*P_s*Q_s*sp.diff(P_s, r_s, 2) + P_s*sp.diff(P_s, r_s)*sp.diff(Q_s, r_s)
        + Q_s*sp.diff(P_s, r_s)**2) / (2*P_s**2*Q_s**2)
Rt_s = sp.simplify(sp.powsimp(Rt_s, force=True))
target_int = (3-p_s)*r_s**(p_s-1) - 2
OUT['anchor_phi0_Rt_int_simplified'] = str(Rt_s)
OUT['anchor_phi0_identity_residual'] = str(sp.simplify(Rt_s - target_int))
# Exterior on the slice at Darmois match beta=Sigma^p/3, k=Sigma^(p-2)/3, gamma=0:
# f = 1 - 2 beta/r - k r^2 ; evaluate Rtilde_ext(Sigma) symbolically in Sigma,p
S_s = sp.symbols('Sigma', positive=True)
beta_s = S_s**p_s/3; k_s = S_s**(p_s-2)/3
f_s = 1 - 2*beta_s/r_s - k_s*r_s**2
Pe = f_s*r_s**-2; Qe = r_s**-2/f_s
Rt_e = (-2*Pe*Qe*sp.diff(Pe, r_s, 2) + Pe*sp.diff(Pe, r_s)*sp.diff(Qe, r_s)
        + Qe*sp.diff(Pe, r_s)**2) / (2*Pe**2*Qe**2)
Rt_e_at = sp.simplify(sp.powsimp(Rt_e.subs(r_s, S_s), force=True))
OUT['anchor_phi0_Rt_ext_at_Sigma'] = str(Rt_e_at)
OUT['anchor_phi0_jump'] = str(sp.simplify(Rt_e_at - target_int.subs(r_s, S_s)))
# numeric spot-check of the identity at several p,Sigma
checks = {}
for pv in ['0.1', '0.3', '0.5', '0.9']:
    for Sv in ['10', '100', '1000']:
        num = float((1+mpf(pv))*(mpf(Sv))**(mpf(pv)-1))
        checks[f'p={pv},Sig={Sv}'] = num
OUT['anchor_phi0_jump_numeric_examples'] = checks

# ---------- ANCHOR (ii): T-b (p=1/2, Phi=0) with STORED Darmois pair ----------
tb = {}
for Sv, stored in [('10', '0.474342'), ('100', '0.150000')]:
    S = mpf(Sv)
    beta = (mpf(1)/3)*msqrt(S)          # (1/3) sqrt(Sigma r0), r0=1
    k = beta/S**3
    # interior Phi=0 is a=0 in Phi2 family (Phi identically 0)
    Rt_int = interior_Rtilde(S, mpf('0.5'), mpf(0))
    Rt_ext = exterior_Rtilde(S, beta, k, gamma=mpf(0))
    jump = Rt_ext - Rt_int
    tb[Sv] = {'beta': str(beta), 'k': str(k), 'Rt_int': str(Rt_int),
              'Rt_ext': str(Rt_ext), 'jump': str(jump), 'stored': stored,
              'rel_err': str(abs(jump-mpf(stored))/mpf(stored))}
OUT['anchor_Tb'] = tb

# ---------- DECIDING READ: audited point p=0.1, Phi2, Sigma=1000 ----------
S = mpf(1000); p_ = mpf('0.1')
a_stored = mpf('0.27773424114865775')
# my own bisection for a_zero on [0.27, 0.29] using my [Rtilde](a)
def jump_of_a(a):
    beta, k = darmois_solve(S, p_, a)
    return exterior_Rtilde(S, beta, k) - interior_Rtilde(S, p_, a), beta, k
lo, hi = mpf('0.27'), mpf('0.29')
flo, _, _ = jump_of_a(lo); fhi, _, _ = jump_of_a(hi)
assert flo*fhi < 0, (flo, fhi)
for _ in range(200):
    mid = (lo+hi)/2; fm, _, _ = jump_of_a(mid)
    if flo*fm <= 0: hi = mid; fhi = fm
    else: lo = mid; flo = fm
    if hi-lo < mpf('1e-35'): break
a_zero_mine = (lo+hi)/2
jump_mine, beta_mine, k_mine = jump_of_a(a_zero_mine)
Rn_mine = exterior_Rtilde_n(S, beta_mine, k_mine) - interior_Rtilde_n(S, p_, a_zero_mine)
S00_mine = -(mpf(4)/3)*Rn_mine   # in units of alpha0
# also evaluate at stored a_zero and at rounded a=0.277734
jump_stored_a, beta_s, k_s = jump_of_a(a_stored)
Rn_s = exterior_Rtilde_n(S, beta_s, k_s) - interior_Rtilde_n(S, p_, a_stored)
jump_round_a, beta_r, k_r = jump_of_a(mpf('0.277734'))
# gamma-entry check: recompute with gamma=0
beta_g0, k_g0 = darmois_solve(S, p_, a_zero_mine, gamma=mpf(0))
OUT['deciding'] = {
    'Sigma': '1000', 'p': '0.1', 'gamma_per_r0': str(GAMMA),
    'a_zero_mine': str(a_zero_mine), 'a_zero_stored': str(a_stored),
    'a_zero_abs_diff': str(abs(a_zero_mine-a_stored)),
    'beta_MK_r0': str(beta_mine), 'beta_stored': '2.142611',
    'beta_rel_err_vs_stored': str(abs(beta_mine-mpf('2.142611'))/mpf('2.142611')),
    'k_r0^-2': str(k_mine), 'k_stored': '-2.28996e-9',
    'k_rel_err_vs_stored': str(abs(k_mine-mpf('-2.28996e-9'))/mpf('2.28996e-9')),
    'jump_Rtilde_at_my_a_zero': str(jump_mine),
    'jump_Rtilde_at_stored_a_zero': str(jump_stored_a),
    'jump_Rtilde_at_rounded_a_0.277734': str(jump_round_a),
    'beta_at_stored_a': str(beta_s), 'k_at_stored_a': str(k_s),
    'jump_Rtilde_n': str(Rn_mine), 'Rn_stored': '-0.0152186',
    'Rn_rel_err': str(abs(Rn_mine-mpf('-0.0152186'))/mpf('0.0152186')),
    'Rn_at_stored_a': str(Rn_s),
    'S00_over_alpha0': str(S00_mine), 'S00_stored': '0.020291',
    'S00_rel_err': str(abs(S00_mine-mpf('0.020291'))/mpf('0.020291')),
    'S00_sign_positive': bool(S00_mine > 0),
    'gamma_zero_beta': str(beta_g0), 'gamma_zero_k': str(k_g0),
    'gamma_effect_on_beta_rel': str(abs(beta_mine-beta_g0)/abs(beta_mine)),
    'gamma_effect_on_k_rel': str(abs(k_mine-k_g0)/abs(k_mine)) if k_mine != 0 else 'n/a',
}
# primary radii non-join spot check for the audited interior (a=a_zero_mine):
prim = {}
for Sv in ['10', '100']:
    beta, k = darmois_solve(mpf(Sv), p_, a_zero_mine)
    prim[Sv] = {'beta': str(beta), 'k': str(k),
                'jump': str(exterior_Rtilde(mpf(Sv), beta, k) - interior_Rtilde(mpf(Sv), p_, a_zero_mine))}
OUT['primary_radii_audited_interior'] = prim

with open('/home/hatch/workspace/warp-pilot/gate9/results/wb_g92_numbers.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print(json.dumps({k: OUT[k] for k in ['anchor_flat_Rtilde', 'anchor_Tb',
      'anchor_phi0_identity_residual', 'anchor_phi0_Rt_ext_at_Sigma', 'anchor_phi0_jump']}, indent=1))
print(json.dumps(OUT['deciding'], indent=1))
print(json.dumps(OUT['primary_radii_audited_interior'], indent=1))
