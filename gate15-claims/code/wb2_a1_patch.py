"""W-B2: A1 diagnosis patch. Recomputes interior Rn with W-A's printed A3
expression vs the true d^3/dr^3 of exp(2 Phi2), and records both in
wb2_functionals.json. Jets via mpmath.diff (independent of sympy route)."""
import json
from mpmath import mp, mpf, log, exp, sqrt, diff

mp.dps = 50
FN = "/home/hatch/workspace/warp-pilot/gate15/work_b2/wb2_functionals.json"
d = json.load(open(FN))
a = mpf("0.27773424114865775"); p = mpf("0.1"); rS = mpf(1000)
L = log(rS)
Phi = a * L / (1 + L)
Phi1 = a / (rS * (1 + L)**2)
Phi2 = -a * rS**-2 * (1 + L)**-3 * (3 + L)
Phi3 = -a * rS**-3 * (-2 * (1 + L)**-3 * (3 + L) - 3 * (1 + L)**-4 * (3 + L) + (1 + L)**-3)
A0 = exp(2 * Phi); A1 = 2 * Phi1 * A0; A2 = (2 * Phi2 + 4 * Phi1**2) * A0
A3_true = (2 * Phi3 + 12 * Phi1 * Phi2 + 8 * Phi1**3) * A0
A3_WA = (2 * Phi3 + 12 * Phi1 * Phi2) * A0 + (2 * Phi2 + 4 * Phi1**2) * A1
u = rS**(p - 1); u1 = (p - 1) * u / rS; u2 = (p - 1) * (p - 2) * u / rS**2
B0 = 1 / (1 - u); B1 = B0**2 * u1; B2 = 2 * B0**3 * u1**2 + B0**2 * u2

def Rtilde(A, A1, A2, B, B1, r):
    P = A / r**2; P1 = A1 / r**2 - 2 * A / r**3; P2 = A2 / r**2 - 4 * A1 / r**3 + 6 * A / r**4
    Q = B / r**2; Q1 = B1 / r**2 - 2 * B / r**3
    return (-2 * P * Q * P2 + P * P1 * Q1 + Q * P1**2) / (2 * P**2 * Q**2)

def Rn_int(A3v):
    dR = (diff(lambda x: Rtilde(x, A1, A2, B0, B1, rS), A0) * A1
          + diff(lambda x: Rtilde(A0, x, A2, B0, B1, rS), A1) * A2
          + diff(lambda x: Rtilde(A0, A1, x, B0, B1, rS), A2) * A3v
          + diff(lambda x: Rtilde(A0, A1, A2, x, B1, rS), B0) * B1
          + diff(lambda x: Rtilde(A0, A1, A2, B0, x, rS), B1) * B2
          + diff(lambda rr: Rtilde(A0, A1, A2, B0, B1, rr), rS))
    return rS / sqrt(B0) * dR

Rn_true = Rn_int(A3_true)
Rn_WA = Rn_int(A3_WA)
Rn_ext = mpf(d["A1"]["Rn_ext"])
d["A1_diagnosis"] = {
    "A3_true_d3_exp2Phi": str(A3_true),
    "A3_WA_printed_expression": str(A3_WA),
    "A3_difference_WA_minus_true": str(A3_WA - A3_true),
    "note": "W-A's printed A3 = (2Phi3+12Phi1Phi2)A0 + (2Phi2+4Phi1^2)A1 expands to "
            "(2Phi3+16Phi1Phi2+8Phi1^3)A0; the true third derivative of exp(2Phi) is "
            "(2Phi3+12Phi1Phi2+8Phi1^3)A0. Difference = 4*Phi1*Phi2*A0.",
    "Rn_int_with_true_A3": str(Rn_true),
    "Rn_int_with_WA_A3": str(Rn_WA),
    "WA_Rn_int_stated": "-0.010368518866140533073221935931268206421770277911899",
    "jump_Rn_with_true_A3": str(Rn_ext - Rn_true),
    "jump_Rn_with_WA_A3": str(Rn_ext - Rn_WA),
    "WA_jump_Rn_stated": "-0.015317146541929403352171237579044122743192801994298",
    "stored_control_Rn": "-0.0152185840",
}
json.dump(d, open(FN, "w"), indent=1)
print("Rn_int true A3:", Rn_true)
print("Rn_int WA A3:  ", Rn_WA)
print("jump true:", Rn_ext - Rn_true, " jump WA-A3:", Rn_ext - Rn_WA)
