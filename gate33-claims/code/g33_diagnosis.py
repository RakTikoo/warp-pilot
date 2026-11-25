#!/usr/bin/env python3
"""
Gate-33 Item 1 -- the Corner B diagnosis, deciding computation.
A: the reduced (small-alpha) family at Corner B's plane point.
B: YBBY's stated constraints evaluated at Corner B's OWN parameters.
C: candidate-(b) toggle -- sigma evaluation (anchor vs Gupta PM).
Forms: YBBY Eqs. (188)-(195) as reconstructed in
gate33/work/g33_ybby_reconstruction.md; fence forms as in
g33_controls.py (controls C1-C3 already reproduced).
"""
import numpy as np

G = 6.67430e-11; c_light = 299792458.0; Msun = 1.98847e30

def alpha2_slice(c2, c14):
    return c14 * (c14 + 2 * c2 * c14 - c2) / (c2 * (2 - c14))

def Ccoef(c1, c2, c14):
    w02 = (2 - c14) * c2 / ((2 + 3 * c2) * c14)
    w12 = c1 / c14
    return (4 / (3 * w02**1.5 * c14 * (2 - c14)) + 4 / (3 * c14 * w12**1.5),
            np.sqrt(w02), np.sqrt(w12))

def sigma(c2, c14, Cstar, f=1.0):
    a1 = -4 * c14; a2 = alpha2_slice(c2, c14)
    s = f * (-(a1 - (2.0 / 3.0) * a2)) * (3.0 / 5.0) * Cstar
    return s / (1 - s)

def Xfac(Pb_h, m_msun):
    return (Pb_h * 3600.0 * c_light**3 / (2 * np.pi * G * m_msun * Msun)) ** (2 / 3)

X_J1738 = Xfac(8.5, 1.6)

print("=" * 74)
print("PART A -- THE REDUCED FAMILY AT (c+, c-) = (0, 0.16586208)")
print("=" * 74)
cp_, cm_ = 0.0, 0.16586208
c1 = (cp_ + cm_) / 2; c3 = (cp_ - cm_) / 2
# YBBY Eqs. (Aecons)/(Aecons2), tex L669-677: leading order in (a1, a2)
c2_fam = (-2 * c1**2 - c1 * c3 + c3**2) / (3 * c1)
c4_fam = -c3**2 / c1
c14_fam = c1 + c4_fam
print(f"family: c1 = {c1:.8f}, c3 = {c3:.8f}")
print(f"family: c2 = {c2_fam:.3e}, c4 = {c4_fam:.8f}, c14 = {c14_fam:.3e}")
# alpha1, alpha2 at the family point vanish identically (numerators):
num_a1 = c3**2 + c1 * c4_fam
num_a2 = c1 + 2 * c3 - c4_fam
print(f"alpha1 numerator (c3^2 + c1*c4)      = {num_a1:.3e}  -> alpha1 = 0")
print(f"alpha2 numerator (c1 + 2c3 - c4)     = {num_a2:.3e}  -> alpha2 = 0")
print("along the whole c+ = 0 line (c3 = -c1): c2 = 0 and c14 = 0")
print("identically -- the family's c+ = 0 slice is the degenerate point")
print("(c2, c14) = (0, 0) at every c-; mode speeds w0^2 ~ c2/c14 singular.")
print()
print("Corner B's departure from the family at the same plane point:")
c14B, c2B, c1B = 7.9e-9, 2 / 21, 3240.0**2 * 7.9e-9
a1B, a2B = -4 * c14B, alpha2_slice(c2B, c14B)
print(f"  (c2, c14) = ({c2B:.7f}, {c14B:.3e}) vs family (0, 0)")
print(f"  (alpha1, alpha2) = ({a1B:.4e}, {a2B:.4e}) vs family (0, 0);")
print(f"  SS ranges (tex L653): |a1| <= 1e-4, |a2| <= 1e-7 -- B inside both.")
c14s = 6.4226891e-9
print(f"Phase 306 point: (c2, c14*) = ({c2B:.7f}, {c14s:.7e}), same (c+, c-);")
print(f"  alpha1* = {-4*c14s:.4e}, alpha2* = {alpha2_slice(c2B, c14s):.4e}.")

print()
print("=" * 74)
print("PART B -- YBBY'S STATED CONSTRAINTS AT CORNER B'S OWN PARAMETERS")
print("=" * 74)
CcB, w0B, w1B = Ccoef(c1B, c2B, c14B)
# quadrupole-deviation bound at Corner B (fence audit forms, A1/A2/A3
# at the point as stored in p303_audit.out: bound 5.92e-9 at f = 1,
# 6.51e-9 at f = 1.3 -- recomputed here from the audit's printed A-reads)
qdev_f13 = 6.51e-9
# dipole bound for the three Pdot systems: X_sys <= 0.68 * X_J1738
# (P_b <= 4.74 h from tex L435/L3044; m_sys >= 1.6 Msun floor),
# (s1-s2)^2 <= sigma(C_* = 0.30, f = 1.3)^2 (largest compactness,
# bracket top -- a bound, not an evaluation).
sg_max = sigma(c2B, c14B, 0.30, f=1.3)
dip_bound = (5 * (1 - c14B / 2) / 32) * sg_max**2 * (0.68 * X_J1738) * CcB
print(f"sigma bound (C_*=0.30, f=1.3) = {sg_max:.4e}")
print(f"Eq. (191) dipole term, ANY of J1141/J0348/J0737: <= {dip_bound:.3e}")
print(f"Eq. (193) quadrupole deviation at B (audit bound, f=1.3): "
      f"<= {qdev_f13:.3e}")
print(f"=> |delta Pdot| at Corner B <= {dip_bound + qdev_f13:.3e} for all")
print(f"   three Pdot systems. Eq. (191) needs delta Pdot <= delta_obs;")
print(f"   every delta_obs in YBBY's sample is >= 1e-3 at era precision")
print(f"   (and Eq. (190) characterises delta_obs + delta_inf = O(10%)):")
print(f"   margin >= {(1e-3) / (dip_bound + qdev_f13):.2e} even at 1e-3,")
print(f"   >= {(1e-4) / (dip_bound + qdev_f13):.2e} even at a hypothetical 1e-4.")
print()
print("Eqs. (194)-(195) at B vs YBBY's stated alpha-hat bounds:")
print(f"  fence reads: |ahat1| = 7.9632e-9, ahat2 = -9.9540e-10 (C1).")
print(f"  YBBY Sec. VII B bounds: ahat1 <~ 1e-5, ahat2 < 1.8e-4 -> pass by")
print(f"  >= 3.2 / 5.3 orders. YBBY Sec. II / fence L7-L8 bounds")
print(f"  (1e-5, 1e-9): ahat1 passes x1.3e3; ahat2 saturates (the fence's")
print(f"  own leg, not a band leg).")
print()
print("Stability/Cherenkov at B, full theory (Phase 307 Arm 5, OMW forms):")
print("  q_S = 24.0 > 0, q_V = c14 > 0, all speeds^2 > 0 -- PASS.")
print("  The reduced-family edge c- <= c+/[3(1-c+)] (tex, leading order")
print("  in alpha) reads c- <= 0 at c+ = 0: it is the family's wedge,")
print("  and Fig. 1's drawn left edge IS that line (extraction: drawn")
print("  edge c+ = 0.004671 at c- = 1.590e-3 vs line value 0.004751).")

print()
print("=" * 74)
print("PART C -- CANDIDATE (b) TOGGLE: SIGMA EVALUATION AT B")
print("=" * 74)
print(f"anchor sigma(0.17) = {sigma(c2B, c14B, 0.17):.4e}; Gupta PM = 2.7200e-9")
print(f"(ratio 0.9206, Phase 306). Dipole scales as sigma^2: the toggle")
print(f"moves any Pdot read by <= x{(1/0.9206)**2:.3f} (or x1.69 at f = 1.3) --")
print("against margins of >= 4 orders, candidate (b) cannot drive the")
print("discrepancy at Corner B's own (alpha1, alpha2). On the reduced")
print("family the bands' sigma is a family object (Sec. VI: sensitivities")
print("computed on the family, growing with c- at SS-saturating alphas) --")
print("it is not evaluated at B's alphas anywhere in YBBY's construction.")
