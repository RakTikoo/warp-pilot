#!/usr/bin/env python3
"""
Gate-33 controls — the gate's own re-implementation of the fence
forms (YBBY Eq. (184) anchor sigma; OMW (3.24) slice ahat forms;
YBBY Eq. (114) C; Eq. (192)-(193) dipole read), written from the
forms as recorded in the Phase 303/306/307 memos. Reproduces the
stored deciding numbers BEFORE any Gate-33 re-judgement read.
"""
import numpy as np

G = 6.67430e-11; c_light = 299792458.0; Msun = 1.98847e30

def alpha2(c2, c14):
    return c14 * (c14 + 2 * c2 * c14 - c2) / (c2 * (2 - c14))

def Ccoef(c1, c2, c14):
    w02 = (2 - c14) * c2 / ((2 + 3 * c2) * c14)
    w12 = c1 / c14
    scal = 4 / (3 * w02**1.5 * c14 * (2 - c14))
    vec = 4 / (3 * c14 * w12**1.5)
    return scal + vec, scal, vec, np.sqrt(w02), np.sqrt(w12)

def sigma(c2, c14, Cstar, f=1.0):
    a1 = -4 * c14; a2 = alpha2(c2, c14)
    s = f * (-(a1 - (2.0 / 3.0) * a2)) * (3.0 / 5.0) * Cstar
    return s / (1 - s)

def ahats(c2, c14, Cstar, f=1.0, sg=None):
    a1 = -4 * c14; a2 = alpha2(c2, c14)
    if sg is None: sg = sigma(c2, c14, Cstar, f)
    ah1 = a1 + (8 + a1) * sg
    ah2 = a2 + (8 + a1) * sg / 2 - (c14 - 2) * (a1 - 2 * a2) * sg / (2 * c14)
    return ah1, ah2

def Xfac(Pb_h, m_msun):
    return (Pb_h * 3600.0 * c_light**3 / (2 * np.pi * G * m_msun * Msun)) ** (2 / 3)

X_J1738 = Xfac(8.5, 1.6)

def L9(c1, c2, c14, Cstar=0.17, f=1.0, cap=0.1):
    sg = sigma(c2, c14, Cstar, f)
    Cc, *_ = Ccoef(c1, c2, c14)
    return (5 * (1 - c14 / 2) / 32) * sg**2 * X_J1738 * Cc

print("=== C1: Corner B stored reads (Phase 303) ===")
c14B, c2B = 7.9e-9, 2 / 21
c1B = 3240.0**2 * c14B
sgB = sigma(c2B, c14B, 0.17)
ah1B, ah2B = ahats(c2B, c14B, 0.17)
CcB, scalB, vecB, w0B, w1B = Ccoef(c1B, c2B, c14B)
l9B = L9(c1B, c2B, c14B)
print(f"c1 = {c1B:.8f} (stored 0.08293104); c- = {2*c1B:.8f} (stored 0.16586208)")
print(f"sigma(0.17) = {sgB:.4e}   (stored 2.9546e-9)")
print(f"L7 ahat1    = {ah1B:.4e}  (stored 7.9632e-9, inert)")
print(f"L8 ahat2    = {ah2B:.4e}  (stored -9.9540e-10, saturating)")
print(f"L9 dipole   = {l9B:.4e}  (stored 7.3481e-15, inert)")
print(f"C pieces    = scalar {scalB:.4e} + vector {vecB:.4e} = {CcB:.4e}"
      f"  (stored 2.4632e-3 + 4.9622e-3 = 7.4254e-3)")
print(f"w0 = {w0B:.2f} (c_S^2 = {w0B**2:.4e}); w1 = c_V = {w1B:.1f}")
bbnB = abs((1 - c14B / 2) / (1 + 3 * c2B / 2) - 1)
print(f"BBN read    = {bbnB:.6f} (bound 0.125, saturating at margin 0: "
      f"(1)/(1+3c2/2) = {1/(1+3*c2B/2):.6f} vs 0.875)")

print()
print("=== C1b: flat rows at cap 0.1 (stored maximisers, Arm 2 memo) ===")
for name, (c1, c2, c14) in {
    "c_V=1": (2.6568e-6, 2.6676e-6, 2.6568e-6),
    "c_V=2": (2.5443e-5, 6.3620e-6, 6.3608e-6),
    "c_V=10": (7.9511e-4, 7.9621e-6, 7.9511e-6)}.items():
    print(f"{name}: c- = {2*c1:.4e}  L9 = {L9(c1, c2, c14):.5f} (binding at 0.1)")

print()
print("=== C2: Phase 306 stored reads ===")
for pt, sg_r2, sg_g in [("c_V=2 max", 2.5952e-6, 2.4539e-6),
                        ("c_V=10 max", 3.2437e-6, 2.8713e-6),
                        ("Corner B", 2.9546e-9, 2.7200e-9)]:
    print(f"{pt}: ratio sigma_Gupta/sigma_rung2 = {sg_g/sg_r2:.4f}")
_, ah2B_g = ahats(c2B, c14B, 0.17, sg=2.7199855e-9)
print(f"ahat2 at Corner B with sigma_Gupta=2.7199855e-9: {ah2B_g:.4e}"
      f"  (stored -1.2300144e-9)")
c14s = 6.4226891e-9
print(f"c_V at c14* (c1 fixed) = {np.sqrt(c1B/c14s):.4f} (stored 3593.3549);"
      f" c- unchanged = {2*c1B:.8f}")

print()
print("=== C3: Arm 1 cap arithmetic ===")
R, srel = 0.9350, 0.132
for n, lab in [(1.0, "implicit (n=1)"), (1.96, "95% two-sided")]:
    cap = (R - 1) + n * srel
    print(f"{lab}: cap = {cap:.4f}; flat HT = {2.8044e-5 * cap / 0.1:.3e};"
          f" NS-BH = {2.5394e-2 * cap / 0.1:.3e}")
print(f"0.1 sits at n = {(0.1 + 0.065) / srel:.2f} sigma (Arm 1: 1.25)")
