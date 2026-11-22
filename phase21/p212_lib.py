"""
P21-2 lib: Einstein + NLED, S = int sqrt(-g) [ R/16pi - L(F,G)/4pi ],
F = F_mn F^mn, G = F_mn *F^mn.  Signature (-,+,+,+), float64 numerics.

RUN RECORD -- exact family forms + citations, recorded BEFORE any scan number
(registration requirement, CHECKPOINT21.md P21-2):

Action/conventions: as registered in CHECKPOINT21.md S P21-2.
  Matter density Lm = -L(F,G)/(4pi).  Maxwell limit in this normalisation:
  L -> F with L_F(0)=1 (energy densities are 4x the textbook Heaviside-Lorentz
  values at equal charge, i.e. q_textbook = 2 q_here; every EC sign, identity
  and verdict below is independent of this overall factor).

(F1) Born-Infeld, F-only (truncated BI):
  L_BI1(F) = 4 b^2 ( sqrt(1 + F/(2 b^2)) - 1 ),  b = BI parameter (>0).
  Source form: Born & Infeld, Proc. Roy. Soc. A 144 (1934) 425; determinant
  form L_density = (b^2/4pi)( sqrt(-g) - sqrt|det(g_mn + F_mn/b)| ), whose
  expansion det(g+F/b) = -g (1 + F/(2b^2) - G^2/(16 b^4)) gives the F,G form
  below in the present action normalisation (Maxwell limit L -> F checked
  symbolically in p212_derive.py).

(F3) Full Born-Infeld, both invariants:
  L_BI(F,G) = 4 b^2 ( sqrt(Delta) - 1 ),
  Delta = 1 + F/(2 b^2) - G^2/(16 b^4).
  L_F = 1/sqrt(Delta),  L_G = -G/(4 b^2 sqrt(Delta))  (verified symbolically).

(F2) Bronnikov-class L(F) regular-magnetic families:
  (F2a) L = F exp(-alpha F)
  (F2b) L = F / (1 + alpha F)^2
  Bronnikov's regularity conditions (recorded from K.A. Bronnikov,
  gr-qc/0006014, PRD 63 (2001) 044005; review arXiv:2211.00743):
    (R1) Maxwell weak-field limit: L ~ F, L_F -> 1 as F -> 0;
    (R2) regular centre with Maxwell limit possible ONLY for magnetic
         charge (electric regular centre excluded -- Bronnikov's theorem);
    (R3) for a globally regular magnetic configuration L(F) must tend to a
         FINITE limit as F -> infinity;
    (R4) L > 0 and L_F > 0 for F > 0 (positive energy density rho = L/4pi
         and rho + p_t = F L_F/(2pi) >= 0; L_F < 0 is the ghost /
         NEC2-violating corner).
  Both F2 forms satisfy R1 and R3 (L -> 0 as F -> inf); R4 is tested on the
  trajectory in the scan (L_F changes sign at alpha F = 1 for both forms).

(F4) CONTROL: L = F^2 (power law n=2).  No Maxwell limit (L_F(0)=0);
  expected to fail DEC -- validates the audit.

Phase-3 precedent (CHECKPOINT3.md S P3-2(2), EiBI/Shaikh): ansatz p_r = -rho
makes NEC1 identically 0 (saturated) -- the same degeneracy audited here in
pure GR, where there is no gravity-sector term to relocate it into.
"""
import sympy as sp

# --------------------------------------------------------------------------
# Symbolic stress-energy from the action, by direct variation.
# Diagonal metric via POSITIVE symbols (a,bd,c,d):
#   g^tt = -a, g^rr = bd, g^thth = c, g^phph = d ; sqrt(-g) = 1/sqrt(a bd c d)
# Covariant field components fixed: F_tr = A, F_thph = Q sin(th) (s = sin th).
#   F = 2(-a bd A^2 + c d Q^2 s^2)
#   G = 4 A Q s sqrt(a bd c d)     [eps^{tr th ph} = +1 convention]
# T^mu_mu (no sum) = -2 x_mu d(sqrt(-g) Lm)/dx_mu / sqrt(-g), x = (a,bd,c,d).
# --------------------------------------------------------------------------

def derive_T():
    a, bd, c, d, A, Q, s = sp.symbols('a bd c d A Q s', positive=True)
    F = 2*(-a*bd*A**2 + c*d*Q**2*s**2)
    G = 4*A*Q*s*sp.sqrt(a*bd*c*d)
    LF, LG, L0 = sp.symbols('L_F L_G L')
    # T^mu_mu (no sum) = Lm - 2 x_mu dLm/dx_mu, Lm = -L(F,G)/(4pi),
    # by direct variation (see lib header algebra).
    Lm = -L0/(4*sp.pi)
    T = {}
    for name, x in (('t', a), ('r', bd), ('th', c), ('ph', d)):
        dLm = -(LF*sp.diff(F, x) + LG*sp.diff(G, x))/(4*sp.pi)
        T[name] = sp.simplify(Lm - 2*x*dLm)
    # Physical parametrisation: orthonormal electric field E and magnetic B.
    #   a = exp(-2 Phi), bd = (1 - b(r)/r) =: beta, c = 1/r^2, d = 1/(r^2 s^2),
    #   A = E exp(Phi)/sqrt(beta), Q = B r^2  =>  F = 2(B^2 - E^2), G = 4 E B.
    E, B, r = sp.symbols('E B r', positive=True)
    Phi, beta = sp.symbols('Phi beta', positive=True)
    phys = {a: sp.exp(-2*Phi), bd: beta, c: 1/r**2, d: 1/(r**2*s**2),
            A: E*sp.exp(Phi)/sp.sqrt(beta), Q: B*r**2}
    Tp = {k: sp.simplify(v.subs(phys)) for k, v in T.items()}
    Fphys = sp.simplify(F.subs(phys))
    Gphys = sp.simplify(G.subs(phys))
    return Tp, Fphys, Gphys, (LF, LG, L0), (E, B)

def bi_partials():
    """L_F, L_G of full BI from differentiating the explicit L(F,G)."""
    F, G, b = sp.symbols('F G b', positive=True)
    Delta = 1 + F/(2*b**2) - G**2/(16*b**4)
    L = 4*b**2*(sp.sqrt(Delta) - 1)
    LF = sp.simplify(sp.diff(L, F))
    LG = sp.simplify(sp.diff(L, G))
    # Maxwell limit: series in F,G at fixed b -> L = F + O(F^2,G^2)
    return L, LF, LG, Delta

# --------------------------------------------------------------------------
# Einstein tensor for the 4 registered prescribed (Phi, b) combos, r0 = 1
# units in the scan (expressions kept in r, r0 here).
# --------------------------------------------------------------------------

def einstein_combo(phi_expr, b_expr):
    """Return (rho, pr, pt) = G^mu_nu/(8pi) for MT metric with given Phi(r),
    b(r) (sympy expressions in r, r0)."""
    r, th, r0 = sp.symbols('r theta r0', positive=True)
    t, ph = sp.symbols('t phi')
    coords = [t, r, th, ph]
    g = sp.diag(-sp.exp(2*phi_expr), 1/(1 - b_expr/r), r**2,
                r**2*sp.sin(th)**2)
    gi = g.inv()
    dg = [sp.diff(g, x) for x in coords]          # dg[mu] = d_mu g
    # Christoffel Gamma^l_{mn}
    Gam = [[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)]
    for l in range(4):
        for m in range(4):
            for n in range(4):
                expr = sum(gi[l, k]*(dg[n][k, m] + dg[m][k, n] - dg[k][m, n])
                           for k in range(4))/2
                Gam[l][m][n] = sp.simplify(expr)
    dGam = [[[ [sp.diff(Gam[l][m][n], x) for x in coords]
               for n in range(4)] for m in range(4)] for l in range(4)]
    Ric = [[sp.Integer(0)]*4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            expr = 0
            for l in range(4):
                expr += dGam[l][m][n][l] - dGam[l][m][l][n]
                for k in range(4):
                    expr += Gam[l][l][k]*Gam[k][m][n] - Gam[l][n][k]*Gam[k][m][l]
            Ric[m][n] = sp.simplify(expr)
    R = sp.simplify(sum(gi[m, n]*Ric[m][n] for m in range(4) for n in range(4)))
    Gmix = {}
    for mu in range(4):
        Gmix[mu] = sp.simplify(sum(gi[mu, k]*Ric[k][mu] for k in range(4))
                               - R/2)
    rho = sp.simplify(-Gmix[0]/(8*sp.pi))
    pr = sp.simplify(Gmix[1]/(8*sp.pi))
    pt = sp.simplify(Gmix[2]/(8*sp.pi))
    return rho, pr, pt

COMBOS = {
    # name: (Phi(r), b(r)) with symbols r, r0
    'b1_phi0':   ('0', 'r0**2/r'),
    'b1_phiMT':  ('-r0/(2*r)', 'r0**2/r'),
    'b2_phi0':   ('0', 'r0*(r/r0)**Rational(1,2)'),
    'b2_phiMT':  ('-r0/(2*r)', 'r0*(r/r0)**Rational(1,2)'),
}
