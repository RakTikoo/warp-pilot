#!/usr/bin/env python3
"""
Phase 303 Part B -- pricing the spin-1 channel at the completed
corner(s) and the spot rows c_V in {1, 2, 10}.
Registration: phase303/work/p303_registration.md (binding).
Forms/machinery: p303_audit.py (YBBY Eqs. 110-114, 192-193;
sigma = weak-field anchor Eq. (184), f bracket [0.7, 1.3] from
YBBY Sec. VI A Fig. 3's stated 15-30% deviation).

Fiducials (Phase 294 verbatim):
  HT: m1=1.44, m2=1.39 Msun, Pb=7.75h, e_orb=0.617, R=12 km both
      stars (C1, C2 from fixed radius); Peters eccentric quad.
  NS-BH bound class: 1.4+10 Msun, Pb=7.75h, e_orb=0, ds = sigma
      at C_*=0.17 (s2 = 0 bound class); Peters circular quad.
Completed fence (central model C_*=0.17, f=1), legs L1-L9 as in
p303_audit.py Part A3; L4 carries the programme's 1e-9-relative
saturation tolerance (Phase 294 memo note (i)).
"""
import numpy as np
from scipy.optimize import minimize

G = 6.67430e-11
clight = 299792458.0
Msun = 1.98847e30

# ---------------- slice machinery (from p303_audit.py) ----------------
def alpha2f(c2v, c14v):
    return c14v * (c14v + 2 * c2v * c14v - c2v) / (c2v * (2 - c14v))

def Ccoef(c1v, c2v, c14v):
    w02 = (2 - c14v) * c2v / ((2 + 3 * c2v) * c14v)
    w12 = c1v / c14v
    return 4 / (3 * w02**1.5 * c14v * (2 - c14v)) + 4 / (3 * c14v * w12**1.5)

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
    ah2 = a2 + (8 + a1) * sg / 2 - (c14v - 2) * (a1 - 2 * a2) * sg / (2 * c14v)
    return ah1, ah2

def Xfac(Pb_h, m_msun):
    return (Pb_h * 3600.0 * clight**3 / (2 * np.pi * G * m_msun * Msun)) ** (2 / 3)

X_J1738 = Xfac(8.5, 1.6)
X_HT = Xfac(7.75, 2.83)
X_NSBH = Xfac(7.75, 11.4)

# ---------------- Peters controls ----------------
def peters(m1m, m2m, Pb_h, e):
    m1, m2 = m1m * Msun, m2m * Msun
    m = m1 + m2
    mu = m1 * m2 / m
    Pb = Pb_h * 3600.0
    a_orb = (G * m * Pb**2 / (4 * np.pi**2)) ** (1 / 3)
    F = (1 + 73 / 24 * e**2 + 37 / 96 * e**4) / (1 - e**2) ** 3.5
    Pcirc = (32 / 5) * G**4 * mu**2 * m**3 / (clight**5 * a_orb**5)
    return Pcirc * F, Pcirc, a_orb, mu

Pquad_HT, _, _, _ = peters(1.44, 1.39, 7.75, 0.617)
Pquad_NSBH, _, aorb_N, mu_N = peters(1.4, 10.0, 7.75, 0.0)
print(f"Peters HT quad   = {Pquad_HT:.4e} W  (Phase 294 control: 7.7808e24)")
print(f"Peters NSBH quad = {Pquad_NSBH:.4e} W  (Phase 294 control: 1.2696e25;"
      f" mu={mu_N/Msun:.4f} Msun, a_orb={aorb_N:.4e} m)")
e_orb = 0.617
g_e = (1 + e_orb**2 / 2) / (1 - e_orb**2) ** 2.5
F_e = (1 + 73 / 24 * e_orb**2 + 37 / 96 * e_orb**4) / (1 - e_orb**2) ** 3.5
print(f"g(e)={g_e:.4f}  F(e)={F_e:.4f}  g/F={g_e/F_e:.4f}")

R_ns = 12e3
C1_HT = G * 1.44 * Msun / (R_ns * clight**2)
C2_HT = G * 1.39 * Msun / (R_ns * clight**2)
print(f"HT compactnesses at R=12 km: C1={C1_HT:.4f} C2={C2_HT:.4f} dC={C1_HT-C2_HT:.5f}"
      f"  (Phase 292: 0.1772 / 0.1710 / 0.00615)")

# ---------------- ratios at a point ----------------
def ratios(c1v, c2v, c14v, f=1.0):
    Cc = Ccoef(c1v, c2v, c14v)
    ds_HT = sigma(c2v, c14v, C1_HT, f) - sigma(c2v, c14v, C2_HT, f)
    Ad_HT = (5 * (1 - c14v / 2) / 32) * ds_HT**2 * X_HT * Cc
    r_HT = Ad_HT * g_e / F_e
    ds_N = sigma(c2v, c14v, 0.17, f)
    r_N = (5 * (1 - c14v / 2) / 32) * ds_N**2 * X_NSBH * Cc
    return r_HT, r_N, r_HT * Pquad_HT, r_N * Pquad_NSBH, Cc

print()
print("=== Corner B priced (completed corner, c_V = 3240) ===")
c1B, c2B, c14B = 3240.0**2 * 7.9e-9, 2 / 21, 7.9e-9
for f in (0.7, 1.0, 1.3):
    r_HT, r_N, P_HT, P_N, Cc = ratios(c1B, c2B, c14B, f)
    print(f"[f={f}] C={Cc:.4e}  HT ratio={r_HT:.4e} (P_dip={P_HT:.4e} W)   "
          f"NS-BH ratio={r_N:.4e} (P_dip={P_N:.4e} W)")
print("  (spin-0 row at the same (c14,c2), Phase 292/294: HT 6.8296e-19,"
      " NS-BH 6.1899e-16, P_dip 5.3140e6 W)")

# ---------------- completed fence (central model) ----------------
def feasible(c2v, c14v, cstar_v, f=1.0):
    """c1 = cstar_v^2 * c14 (speed floor). Returns (ok, binding dict)."""
    c1v = cstar_v**2 * c14v
    if not (0 < c14v <= 2.5e-5) or c2v <= 0:
        return False, {}
    a2 = alpha2f(c2v, c14v)
    if abs(a2) > 1e-7:
        return False, {}
    bbn = abs((1 - c14v / 2) / (1 + 3 * c2v / 2) - 1)
    if bbn > 0.125 * (1 + 1e-9):
        return False, {}
    w02 = (2 - c14v) * c2v / ((2 + 3 * c2v) * c14v)
    if w02 < 1.0:
        return False, {}
    ah1, ah2 = ahats(c2v, c14v, 0.17, f)
    if abs(ah1) > 1e-5 or abs(ah2) > 1e-9:
        return False, {}
    sg = sigma(c2v, c14v, 0.17, f)
    Cc = Ccoef(c1v, c2v, c14v)
    Adip = (5 * (1 - c14v / 2) / 32) * sg**2 * X_J1738 * Cc
    if Adip > 0.1:
        return False, {}
    return True, dict(Adip=Adip, ah1=ah1, ah2=ah2, a2=a2, bbn=bbn)

def maximise(cstar_v, f=1.0):
    best = (-np.inf, None)
    for c14v in np.logspace(-9, np.log10(2.5e-5), 400):
        edge = c14v / (1 - 2 * c14v)
        c2grid = np.concatenate(([edge * (1 + 1e-12)],
                                 np.logspace(np.log10(edge * 1.000001),
                                             np.log10(0.35), 260)))
        for c2v in c2grid:
            ok, _ = feasible(c2v, c14v, cstar_v, f)
            if ok:
                r = ratios(cstar_v**2 * c14v, c2v, c14v, f)[0]
                if r > best[0]:
                    best = (r, (c2v, c14v))
    # polish (Nelder-Mead on log variables, feasibility as barrier)
    def neg(x):
        c2v, c14v = np.exp(x[0]), np.exp(x[1])
        ok, _ = feasible(c2v, c14v, cstar_v, f)
        if not ok:
            return 1e6
        return -np.log10(ratios(cstar_v**2 * c14v, c2v, c14v, f)[0])
    x0 = np.log(best[1])
    res = minimize(neg, x0, method="Nelder-Mead",
                   options=dict(xatol=1e-10, fatol=1e-12, maxiter=4000))
    c2p, c14p = np.exp(res.x)
    okp, info = feasible(c2p, c14p, cstar_v, f)
    rp = ratios(cstar_v**2 * c14p, c2p, c14p, f) if okp else (np.nan,) * 5
    if okp and rp[0] > best[0]:
        best = (rp[0], (c2p, c14p))
        return best, info, True
    ok0, info0 = feasible(best[1][0], best[1][1], cstar_v, f)
    return best, info0, False

print()
print("=== Spot rows: maximise HT ratio s.t. c_V >= c* (completed fence) ===")
for f in (1.0, 0.7, 1.3):
    for cstar_v in (1.0, 2.0, 10.0):
        (rbest, (c2m, c14m)), info, polished = maximise(cstar_v, f)
        c1m = cstar_v**2 * c14m
        r_HT, r_N, P_HT, P_N, Cc = ratios(c1m, c2m, c14m, f)
        w0m = np.sqrt((2 - c14m) * c2m / ((2 + 3 * c2m) * c14m))
        print(f"[f={f}] c*={cstar_v:>4}: (c1,c2,c14)=({c1m:.4e},{c2m:.4e},{c14m:.4e})"
              f" c-={2*c1m:.3e} w0={w0m:.4f} C={Cc:.4e}")
        print(f"        HT ratio={r_HT:.4e} (P_dip={P_HT:.4e} W)  NS-BH ratio={r_N:.4e}"
              f" (P_dip={P_N:.4e} W)  [grid+{'polish' if polished else 'grid'}]")
        print(f"        legs at maximiser: L9 dipole={info.get('Adip', float('nan')):.4e}"
              f"  L7 ahat1={info.get('ah1', float('nan')):.4e}"
              f"  L8 ahat2={info.get('ah2', float('nan')):.4e}"
              f"  L3 alpha2={info.get('a2', float('nan')):.4e}"
              f"  L4 BBN={info.get('bbn', float('nan')):.4e}")

print()
print("=== c1-monotonicity check at the c*=1 maximiser (central) ===")
(rbest, (c2m, c14m)), info, _ = maximise(1.0, 1.0)
for mult in (1.0, 4.0, 100.0, 1e4):
    c1v = mult * c14m
    r = ratios(c1v, c2m, c14m, 1.0)
    print(f"  c1 x{mult:>6}: c_V={np.sqrt(c1v/c14m):8.1f}  C={r[4]:.4e}  HT ratio={r[0]:.4e}")
