#!/usr/bin/env python3
"""
Phase 303 -- THE SPIN-1 FULL AUDIT (Einstein-aether vector mode).
Registration: phase303/work/p303_registration.md (binding).

Part A (this script): symbolic identities (control C-B) and the
completed-fence evaluation at Phase 298's Corners A and B.
Part B (p303_pricing.py): pricing + spot-row maximisation.

Published forms only, primary-source grade:
  YBBY (Yagi, Blas, Barausse & Yunes, PRD 89, 084067 (2014),
  arXiv:1311.7144v4, retrieved in full 2026-11-24):
    Eq. (95)   w2^2 = 1/(1-c+)
    Eq. (100)  w1^2 = (2c1 - c+ c-)/[2(1-c+) c14]
    Eq. (107)  Z = (alpha1 - 2 alpha2)(1-c+)/[3(2c+ - c14)]
    Eq. (108)  w0^2 = (2-c14) c123/[(2+3c2+c+)(1-c+) c14]
    Eqs. (110)-(114) flux coefficients A1,A2,A3,B1,B2,B3,C,D
    Eqs. (192)-(193) circular-orbit <A>: dipole term
      (5(1-c14/2)/32) (s1-s2)^2 (Pb/(2 pi G m))^(2/3) C
    Eq. (173)  sigma_AE = 2 c1 (2A - 4 - alpha1)/[c- (8+alpha1)]
    Eq. (183)  sigma_kh = (2A - 4 - alpha1)/(8+alpha1)
    Eq. (184)  s^wf = (alpha1 - (2/3) alpha2) Omega/M_obs,
               Omega/M = -(3/5) C_* (uniform density, as Phase 292)
    Eqs. (194)-(195) strong-field PPN:
      ahat1 = alpha1 + c- (8+alpha1) sigma/(2 c1)
      ahat2 = alpha2 + c- (8+alpha1) sigma/(4 c1)
              - (c14-2)(alpha1-2 alpha2) sigma/[2(c14-2c+)]
    Sec. VI A: O(v^0) solutions depend only on c14; numerical s
      deviates from Eq. (184) by 15-30% at realistic compactness
      (Fig. 3, at c+ = c- = 1e-4) -> EA bracket f in [0.7, 1.3];
      s increases monotonically with c- (Fig. 4, c+ = 0.1, 1);
      fit Eq. (186) region: c+ in 3x(1e-4,1e-1),
      c- in 3x(1e-5,1e-3), C_* in (0.11, 0.28), at fixed
      alpha1 = 1e-4, alpha2 = 4e-7 (saturating solar).
  OMW (Oost, Mukohyama & Wang, PRD 97, 124023 (2018)):
    Eq. (1.1) PPN alpha1, alpha2; Eq. (3.8) Shao-Wex bounds
      |ahat1| <= 1e-5, |ahat2| <= 1e-9 (95%);
    Eq. (3.9) general ahat forms; Eq. (3.24) c13=0 reductions.
  Phase 298 (inputs): on the GW slice c13 = 0 (c+ = 0, c3 = -c1,
  c- = 2 c1): cV^2 = c1/c14, alpha1 = -4 c14,
  alpha2 = c14(c14 + 2 c2 c14 - c2)/[c2 (2 - c14)] (c1-free).

Sigma model (Item 1, rung 2 structural read):
  sigma(C_*) = s/(1-s),  s = f * (-(alpha1 - (2/3) alpha2))
             * (3/5) C_* ,
  f = 1 central; EA published-deviation bracket f in [0.7, 1.3].
  The weak-field anchor is exact leading behaviour and depends
  on the couplings only through (alpha1, alpha2), i.e. only
  through (c14, c2) on the slice; the strong-field c-dependence
  enters through the integration constant A of Eq. (173) and is
  NOT published at c+ ~ 0, c- > 3e-3 (see memo).
"""
import numpy as np
import sympy as sp

print("=" * 72)
print("PART A1 -- SYMBOLIC IDENTITIES (control C-B)")
print("=" * 72)
c1, c2, c14s, sg = sp.symbols("c1 c2 c14 sigma")
c3 = -c1                      # slice c13 = 0
c4 = c14s - c1
cp = c1 + c3                  # c+ = 0 on slice
cm = c1 - c3                  # c- = 2 c1 on slice
c123 = c1 + c2 + c3

# OMW Eq. (1.1) PPN parameters (as in p298_row2.py)
alpha1 = -8 * (c3**2 + c1 * c4) / (2 * c1 - c1**2 + c3**2)
alpha2 = alpha1 / 2 - (c1 + 2 * c3 - c4) * (2 * c1 + 3 * c2 + c3 + c4) / (
    c123 * (2 - c14s))
a1s = sp.simplify(alpha1)
a2s = sp.simplify(alpha2)
print("alpha1 on slice:", a1s, " (expect -4*c14)")
print("alpha2 on slice:", a2s)

# YBBY Eqs. (194)-(195) on the slice
ah1 = a1s + cm * (8 + a1s) * sg / (2 * c1)
ah2 = a2s + cm * (8 + a1s) * sg / (4 * c1) - (c14s - 2) * (a1s - 2 * a2s) * sg / (
    2 * (c14s - 2 * cp))
print("ahat1 (YBBY 194) - [alpha1 + (8+alpha1) sigma] =",
      sp.simplify(ah1 - (a1s + (8 + a1s) * sg)), " (expect 0)")
print("ahat2 (YBBY 195) - (alpha2/alpha1)(alpha1 + (8+alpha1) sigma) =",
      sp.simplify(ah2 - (a2s / a1s) * (a1s + (8 + a1s) * sg)), " (expect 0)")

# YBBY Eq. (108) w0^2 and Eq. (100) w1^2 on the slice
w02 = (2 - c14s) * c123 / ((2 + 3 * c2 + cp) * (1 - cp) * c14s)
w12 = (2 * c1 - cp * cm) / (2 * (1 - cp) * c14s)
print("w0^2 on slice:", sp.simplify(w02),
      " (expect c2*(2-c14)/(c14*(2+3*c2)) = khronometric c_S^2)")
print("w1^2 on slice:", sp.simplify(w12), " (expect c1/c14)")

# YBBY Eq. (173) extraction on the slice vs Eq. (183)
A = sp.symbols("A")
sig173 = 2 * c1 * (2 * A - 4 - a1s) / (cm * (8 + a1s))
print("sigma_AE (173) / sigma_kh form (183) on slice:",
      sp.simplify(sig173 / ((2 * A - 4 - a1s) / (8 + a1s))),
      " (expect 1: same form in A; A itself differs)")

print()
print("=" * 72)
print("PART A2 -- NUMERIC FENCE MACHINERY (slice functions)")
print("=" * 72)
G = 6.67430e-11
clight = 299792458.0
Msun = 1.98847e30


def alpha2f(c2v, c14v):
    return c14v * (c14v + 2 * c2v * c14v - c2v) / (c2v * (2 - c14v))


def modes(c1v, c2v, c14v):
    a1 = -4 * c14v
    a2 = alpha2f(c2v, c14v)
    w02v = (2 - c14v) * c2v / ((2 + 3 * c2v) * c14v)
    w12v = c1v / c14v
    Z = -(a1 - 2 * a2) / (3 * c14v)
    return a1, a2, np.sqrt(w02v), np.sqrt(w12v), Z


def flux_coeffs(c1v, c2v, c14v):
    a1, a2, w0, w1, Z = modes(c1v, c2v, c14v)
    A1 = 1.0 + 3 * c14v * (Z - 1) ** 2 / (2 * w0 * (2 - c14v))   # c+ = 0 kills term 2
    A2 = 2 * (Z - 1) / ((c14v - 2) * w0**3)                      # + c+ term = 0
    A3 = 1 / (2 * w1**5 * c14v) + 2 / (3 * c14v * (2 - c14v) * w0**5)
    Ccoef = 4 / (3 * w0**3 * c14v * (2 - c14v)) + 4 / (3 * c14v * w1**3)
    D = 1 / (6 * w1**5 * c14v)
    return dict(A1=A1, A2=A2, A3=A3, C=Ccoef, D=D, Z=Z, w0=w0, w1=w1,
                alpha1=a1, alpha2=a2)


def sigma(c2v, c14v, Cstar, f=1.0):
    a1 = -4 * c14v
    a2 = alpha2f(c2v, c14v)
    s = f * (-(a1 - (2.0 / 3.0) * a2)) * (3.0 / 5.0) * Cstar
    return s / (1 - s)


def ahats(c2v, c14v, Cstar, f=1.0):
    a1 = -4 * c14v
    a2 = alpha2f(c2v, c14v)
    sg = sigma(c2v, c14v, Cstar, f)
    ah1 = a1 + (8 + a1) * sg
    # unsimplified YBBY (195) on the slice (no division by alpha1):
    ah2 = a2 + (8 + a1) * sg / 2 - (c14v - 2) * (a1 - 2 * a2) * sg / (2 * c14v)
    return ah1, ah2


def Xfac(Pb_h, m_msun):
    """(Pb/(2 pi G m))^(2/3) in c=1 units = (Pb c^3/(2 pi G m))^(2/3)."""
    return (Pb_h * 3600.0 * clight**3 / (2 * np.pi * G * m_msun * Msun)) ** (2 / 3)


X_J1738 = Xfac(8.5, 1.6)     # YBBY/Phase 292 J1738 class: Pb=8.5h, m=1.6
X_HT = Xfac(7.75, 2.83)      # Hulse-Taylor class
print(f"X_J1738 (Pb=8.5h, m=1.6 Msun)  = {X_J1738:.6e}")
print(f"X_HT    (Pb=7.75h, m=2.83 Msun) = {X_HT:.6e}  (Phase 292: 1/v^2, v/c=1.464e-3"
      f" -> {1/1.464e-3**2:.4e} at their rounding)")

print()
print("--- Machinery controls vs the khronometric record (KH C only) ---")
# Phase 294 C3: J1738 dipole at the old kh corner (a=2e-7, l=2/21),
# kappa=0.374, KH C = 4/[3 cs^3 a (2-a)], cs=645.5: expect 7.8608e-12.
a_old, l_old = 2.0e-7, 2 / 21
cs_old = np.sqrt(l_old * (2 - a_old) / (a_old * (2 + 3 * l_old)))
C_kh_old = 4 / (3 * cs_old**3 * a_old * (2 - a_old))
Ad = (5 * (1 - a_old / 2) / 32) * (0.374 * a_old) ** 2 * X_J1738 * C_kh_old
print(f"KH old corner: cs={cs_old:.1f} C={C_kh_old:.4e} <A>dip(J1738)={Ad:.4e}"
      f"  (Phase 294 C3: 7.8608e-12, C=1.2394e-02)")
# Phase 294 leg 9 at the KH loudest corner: expect 9.99953e-02.
a_l, l_l = 9.459326e-6, 9.459505e-6
cs_l = np.sqrt(l_l * (2 - a_l) / (a_l * (2 + 3 * l_l)))
C_kh_l = 4 / (3 * cs_l**3 * a_l * (2 - a_l))
Ad = (5 * (1 - a_l / 2) / 32) * (0.374 * a_l) ** 2 * X_J1738 * C_kh_l
print(f"KH loudest corner: cs={cs_l:.4f} C={C_kh_l:.4e} <A>dip(J1738)={Ad:.5e}"
      f"  (Phase 294 leg 9: 9.99953e-02)")

print()
print("=" * 72)
print("PART A3 -- COMPLETED FENCE AT CORNERS A AND B")
print("=" * 72)
CSTAR_C = 0.17


def fence_table(c1v, c2v, c14v, label):
    fc = flux_coeffs(c1v, c2v, c14v)
    a1, a2, w0, w1 = fc["alpha1"], fc["alpha2"], fc["w0"], fc["w1"]
    bbn = abs((1 - c14v / 2) / (1 + 3 * c2v / 2) - 1)
    qS = (2 + 3 * c2v) / c2v
    print(f"--- {label}: (c1,c2,c14) = ({c1v:.8g}, {c2v:.8g}, {c14v:.8g});"
          f" c- = {2*c1v:.8g}")
    print(f"    w0 (spin-0) = {w0:.6f}   w1 = c_V = {w1:.4f}   Z = {fc['Z']:.6f}")
    print(f"    C (EA dipole coeff) = {fc['C']:.6e}   [scalar piece "
          f"{4/(3*w0**3*c14v*(2-c14v)):.6e} + vector piece "
          f"{4/(3*c14v*w1**3):.6e}]")
    print(f"    A1 = {fc['A1']:.6e}  A2 = {fc['A2']:.6e}  A3 = {fc['A3']:.6e}"
          f"  D = {fc['D']:.3e}")
    print(f"    L2 solar |alpha1| = {abs(a1):.4e} <= 1e-4 : "
          f"{'SATURATES' if abs(abs(a1)-1e-4) < 1e-10 else 'pass'}")
    print(f"    L3 solar |alpha2| = {abs(a2):.4e} <= 1e-7 : "
          f"{'pass' if abs(a2) <= 1e-7 else 'FAIL'}")
    print(f"    L4 BBN = {bbn:.4e} <= 0.125 : {'pass' if bbn <= 0.125 else 'FAIL'}")
    print(f"    L5 Cerenkov w0^2 = {w0**2:.6f} >= 1, w1^2 = {w1**2:.4f} >= 1 : "
          f"{'pass' if w0 >= 1 and w1 >= 1 else 'FAIL'}")
    print(f"    L6 stability qS = {qS:.4g} > 0, qV = c14 > 0, signs 2c1, "
          f"c14(2-c14) > 0 : pass")
    for f in (0.7, 1.0, 1.3):
        sg = sigma(c2v, c14v, CSTAR_C, f)
        ah1, ah2 = ahats(c2v, c14v, CSTAR_C, f)
        Adip = (5 * (1 - c14v / 2) / 32) * sg**2 * X_J1738 * fc["C"]
        # quadrupole-deviation bound for the J1738 NS-WD system:
        # |<A>quad - 1| <= |A1-1| + S|A2| + S^2|A3| + c14/2 + (2/3)(s1+s2),
        # S <= sigma (mass-weighted mean sensitivity), s2 = 0.
        qdev = (abs(fc["A1"] - 1) + sg * abs(fc["A2"]) + sg**2 * abs(fc["A3"])
                + c14v / 2 + (2.0 / 3.0) * sg)
        print(f"    [f={f}] sigma(C*=0.17) = {sg:.4e}")
        print(f"        L7 |ahat1| = {abs(ah1):.4e} <= 1e-5 : "
              f"{'pass' if abs(ah1) <= 1e-5 else 'FAIL (x%.2f over)' % (abs(ah1)/1e-5)}")
        print(f"        L8 |ahat2| = {abs(ah2):.4e} <= 1e-9 : "
              f"{'pass' if abs(ah2) <= 1e-9 else 'FAIL (x%.2f over)' % (abs(ah2)/1e-9)}"
              f"   [ahat2 = {ah2:.4e}]")
        print(f"        L9 dipole <A>dip(J1738) = {Adip:.4e} <= 0.1 : "
              f"{'pass' if Adip <= 0.1 else 'FAIL (x%.2f over)' % (Adip/0.1)}"
              f"   |<A>quad-1| <= {qdev:.2e} (bound)")
    # compactness sweep at f = 1 for the deciding legs
    print("    C_* sweep at f=1: ", end="")
    for Cs in (0.11, 0.28):
        ah1, ah2 = ahats(c2v, c14v, Cs, 1.0)
        print(f"[C*={Cs}: ahat1={ah1:.3e}, ahat2={ah2:.3e}] ", end="")
    print()
    return fc


# Corner A: c14 saturates solar alpha1; c2 on the alpha2=0 line.
c14A = 2.5e-5
c2A = c14A / (1 - 2 * c14A)
fcA = fence_table(0.1, c2A, c14A, "Corner A (Phase 298 strong-coupling witness)")
print()
# Corner B: c14 = 7.9e-9, c2 = 2/21, c1 for c_V = 3240.
fcB = fence_table(3240.0**2 * 7.9e-9, 2 / 21, 7.9e-9,
                  "Corner B (Phase 298 c_V = 3240 parity point)")
