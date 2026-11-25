#!/usr/bin/env python3
"""
Phase 306 addendum — Corner B's alpha-hat-2 read under
Gupta's sigma, and the shrunk corner along c2 = 2/21 at
fixed c1 = 0.08293104 (Corner B's construction), solving
alpha-hat-2(c14) = -1e-9 exactly with sigma from Gupta
Eq. (tolman_sens_C) at each c14.
alpha-hat forms: OMW Eq. (3.24) slice forms (Phase 303 S1.2):
  ah1 = a1 + (8 + a1) sigma
  ah2 = (a2/a1) (a1 + (8 + a1) sigma)
"""
from mpmath import mp, mpf, nstr, findroot

mp.dps = 60
CSTAR = mpf("0.17")
C1_B = mpf("0.08293104")
C2_B = mpf(2) / 21


def alpha2(c2, c14):
    return c14 * (c14 + 2 * c2 * c14 - c2) / (c2 * (2 - c14))


def s_gupta_C(a1, a2, cw, C):
    t1 = mpf(5) / 21 * C * (-3 * a1 + 2 * a2)
    num2 = (573 * a1**3 + a1**2 * (67669 - 764 * a2)
            + 96416 * a2**2 + 68 * a1 * a2 * (-2632 + 9 * a2))
    t2 = 5 * num2 / (252252 * a1) * C**2
    first = (4 * a1)**2 * (8 + a1) * (36773030 * a1**2
            - 39543679 * a1 * a2 + 11403314 * a2**2)
    bracket = (-1970100 * a1**5 + 13995878400 * a2**3
               + 640 * a1 * a2**2 * (-49528371 + 345040 * a2)
               + 5 * a1**4 * (-19596941 + 788040 * a2)
               + a1**3 * (-2699192440 + 440184934 * a2
                          - 5974000 * a2**2)
               + 16 * a1**2 * a2 * (1294533212 - 29152855 * a2
                                    + 212350 * a2**2))
    t3 = (first + cw * bracket) / (1801079280 * cw * a1**2) * C**3
    return t1 + t2 + t3


def sigma_gupta_at(c14, c2=C2_B, c1=C1_B):
    a1 = -4 * c14
    a2 = alpha2(c2, c14)
    s = s_gupta_C(a1, a2, 2 * c1, CSTAR)
    return s / (1 - s)


def ah2(c14, sigma):
    a1 = -4 * c14
    a2 = alpha2(C2_B, c14)
    return (a2 / a1) * (a1 + (8 + a1) * sigma)


c14_lit = mpf("7.9e-9")
sig_lit = sigma_gupta_at(c14_lit)
print(f"Literal Corner B (c14 = 7.9e-9): sigma_Gupta = "
      f"{nstr(sig_lit, 8)}")
print(f"  alpha-hat-2(sigma_Gupta) = {nstr(ah2(c14_lit, sig_lit), 8)}"
      f"   (bound 1e-9; rung-2 central read -9.9540e-10)")

f = lambda c14: ah2(c14, sigma_gupta_at(c14)) + mpf("1e-9")
root = findroot(f, mpf("6.4e-9"))
print(f"Shrunk corner: c14* = {nstr(root, 8)} "
      f"(vs literal 7.9e-9; factor {nstr(root / c14_lit, 6)})")
print(f"  check alpha-hat-2(c14*) = "
      f"{nstr(ah2(root, sigma_gupta_at(root)), 8)}")
print(f"  c_V at c14* (c1 fixed) = sqrt(c1/c14*) = "
      f"{nstr(mp.sqrt(C1_B / root), 8)}  (literal corner: 3240)")
print(f"  sigma_Gupta(c14*) = {nstr(sigma_gupta_at(root), 8)}")
# BBN leg at the shrunk corner: G_cos/G_N - 1 ~ (a+e+3l)/(2-a)
# with a=c14, e=0, l=c2=2/21 is c14-independent to first order;
# the corner's BBN saturation is a (c14, c2)-plane statement
# inherited from Phase 292/303 and is not re-decided here.
