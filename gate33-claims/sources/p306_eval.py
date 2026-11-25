#!/usr/bin/env python3
"""
Phase 306 — the Gupta cross-check.
Evaluate Gupta et al. (2021) [arXiv:2104.04596v2] Tolman VII
analytic sensitivity, their Eq. (tolman_sens_C) [= Eq. (80) of
the published PDF], at Phase 303's deciding points, and
compare against the rung-2 (YBBY Eq. 184 anchor) values of
G32-C inside f in [0.7, 1.3].

Transcription: from the arXiv LaTeX source (main.tex,
eq. label tolman_sens_C), cross-checked against the
Omega-form Eq. (tolman_sens_be) [= Eq. (82)] via their
Eq. (81) C(Omega) relation, evaluated independently below.

Arithmetic: mpmath at 60 digits; inputs as exact decimals.
"""
from mpmath import mp, mpf, nstr

mp.dps = 60

CSTAR = mpf("0.17")

# ------------------------------------------------------------------
# Deciding points (Phase 303 memo S3.2 table and S2.2), (c1, c2, c14)
POINTS = {
    "flat_max_cV2":  dict(c1=mpf("2.5443e-5"),  c2=mpf("6.3620e-6"),
                          c14=mpf("6.3608e-6"), rung2=mpf("2.5952e-6")),
    "flat_max_cV10": dict(c1=mpf("7.9511e-4"),  c2=mpf("7.9621e-6"),
                          c14=mpf("7.9511e-6"), rung2=mpf("3.2437e-6")),
    "corner_B":      dict(c1=mpf("0.08293104"), c2=mpf(2) / 21,
                          c14=mpf("7.9e-9"),    rung2=mpf("2.9546e-9")),
}


def alpha1(c14):
    return -4 * c14


def alpha2(c2, c14):
    """OMW Eq. (3.21) on the slice, as printed in Phase 298."""
    return c14 * (c14 + 2 * c2 * c14 - c2) / (c2 * (2 - c14))


def s_anchor(a1, a2, C=CSTAR):
    """YBBY Eq. (184) anchor in the programme's convention:
    s = -(a1 - (2/3) a2) * (3/5) C  [Omega/M* = -(3/5) C]."""
    return -(a1 - mpf(2) / 3 * a2) * mpf(3) / 5 * C


def sigma_of_s(s):
    return s / (1 - s)


def s_gupta_C(a1, a2, cw, C, variant="sum"):
    """Gupta et al. Eq. (tolman_sens_C): s(C) for Tolman VII,
    through O(C^3). `variant` selects the reading of the last
    c_omega-bracket term (16 a1^2 a2 (...)): 'sum' (summand,
    as in the parallel Omega-form) or 'drop' (omitted)."""
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
                          - 5974000 * a2**2))
    if variant == "sum":
        bracket += 16 * a1**2 * a2 * (1294533212 - 29152855 * a2
                                      + 212350 * a2**2)
    t3 = (first + cw * bracket) / (1801079280 * cw * a1**2) * C**3
    return t1 + t2 + t3, (t1, t2, t3)


def s_gupta_Om(a1, a2, cw, x):
    """Gupta et al. Eq. (tolman_sens_be): s as a function of
    x = Omega/M*, through O(x^3). Independent transcription."""
    t1 = (3 * a1 + 2 * a2) / 3 * x
    # NOTE: source prints (3a1 + 2a2)/3; the leading-order match
    # to Eq. (77) requires (a1 - (2/3)a2) = (3a1 - 2a2)/3.
    # Both readings are evaluated by the caller via t1_alt.
    num2 = (573 * a1**3 + a1**2 * (67669 - 764 * a2)
            + 96416 * a2**2 + 68 * a1 * a2 * (9 * a2 - 2632))
    t2 = num2 / (25740 * a1) * x**2
    first = -4 * a1**2 * (a1 + 8) * (36773030 * a1**2
            - 39543679 * a1 * a2 + 11403314 * a2**2)
    bracket = (1970100 * a1**5 - 13995878400 * a2**3
               - 640 * a1 * a2**2 * (-49528371 + 345040 * a2)
               - 5 * a1**4 * (19548109 + 788040 * a2)
               - 16 * a1**2 * a2 * (1294533212 - 29152855 * a2
                                    + 212350 * a2**2)
               + a1**3 * (2699192440 - 309701434 * a2
                          + 5974000 * a2**2))
    t3 = (first + cw * bracket) / (656370000 * cw * a1**2) * x**3
    return t1 + t2 + t3, (t1, t2, t3)


def omega_of_C(a1, C):
    """Invert Gupta Eq. (81): C = -(7/5) x + (35819 a1/85800) x^3
    for x = Omega/M*, by fixed-point iteration at 60 digits."""
    x = -mpf(5) / 7 * C
    for _ in range(200):
        x_new = (-C + (mpf(35819) * a1 / 85800) * x**3) * mpf(5) / 7
        if abs(x_new - x) < mpf(10) ** (-55):
            x = x_new
            break
        x = x_new
    return x


print("=" * 78)
print("CONTROLS")
print("=" * 78)
for name, P in POINTS.items():
    a1, a2 = alpha1(P["c14"]), alpha2(P["c2"], P["c14"])
    cw = 2 * P["c1"]  # c_- = 2 c1 on the slice
    s_a = s_anchor(a1, a2)
    sig_a = sigma_of_s(s_a)
    print(f"{name}: alpha1 = {nstr(a1, 8)}, alpha2 = {nstr(a2, 8)}, "
          f"c_omega = {nstr(cw, 8)}")
    print(f"   anchor sigma = {nstr(sig_a, 8)}   rung-2 (G32-C) = "
          f"{nstr(P['rung2'], 8)}   rel.diff = "
          f"{nstr(abs(sig_a - P['rung2']) / P['rung2'], 3)}")

# Overlap control at Corner B: Gupta Eq. (77) s_wf with the
# programme's Omega/M* convention must give the shared value.
P = POINTS["corner_B"]
a1, a2 = alpha1(P["c14"]), alpha2(P["c2"], P["c14"])
s_wf = (a1 - mpf(2) / 3 * a2) * (-(mpf(3) / 5) * CSTAR)
print(f"OVERLAP (Corner B, Gupta Eq. 77, programme Omega conv.): "
      f"sigma = {nstr(sigma_of_s(s_wf), 8)}  vs shared 2.9546e-9")

# Corner B alpha2 vs Phase 298's printed -3.95e-9
print(f"Corner B alpha2 = {nstr(a2, 6)}  (Phase 298 printed -3.95e-9)")

print()
print("=" * 78)
print("TRANSCRIPTION CROSS-CHECK: Eq. (tolman_sens_C) vs "
      "Eq. (tolman_sens_be) via Eq. (81)")
print("=" * 78)
for name, P in POINTS.items():
    a1, a2 = alpha1(P["c14"]), alpha2(P["c2"], P["c14"])
    cw = 2 * P["c1"]
    sC, _ = s_gupta_C(a1, a2, cw, CSTAR)
    x = omega_of_C(a1, CSTAR)
    # Omega-form with the (3a1 - 2a2)/3 leading reading:
    t1 = (3 * a1 - 2 * a2) / 3 * x
    sOm_raw, parts = s_gupta_Om(a1, a2, cw, x)
    sOm = sOm_raw - parts[0] + t1
    print(f"{name}: s_C-form = {nstr(sC, 10)}")
    print(f"          s_Om-form (lead (3a1-2a2)/3) = {nstr(sOm, 10)}"
          f"   rel.diff = {nstr(abs(sC - sOm) / abs(sC), 3)}")
    sOm_lit = sOm_raw  # literal (3a1 + 2a2)/3 reading
    print(f"          s_Om-form (literal (3a1+2a2)/3) = "
          f"{nstr(sOm_lit, 10)}   rel.diff = "
          f"{nstr(abs(sC - sOm_lit) / abs(sC), 3)}")

print()
print("=" * 78)
print("MAIN EVALUATION at C_* = 0.17")
print("=" * 78)
for name, P in POINTS.items():
    a1, a2 = alpha1(P["c14"]), alpha2(P["c2"], P["c14"])
    cw = 2 * P["c1"]
    sG, (t1, t2, t3) = s_gupta_C(a1, a2, cw, CSTAR)
    sG_drop, _ = s_gupta_C(a1, a2, cw, CSTAR, variant="drop")
    sigG = sigma_of_s(sG)
    ratio = sigG / P["rung2"]
    print(f"{name}:")
    print(f"   terms: C^1 = {nstr(t1, 8)}, C^2 = {nstr(t2, 8)}, "
          f"C^3 = {nstr(t3, 8)}")
    print(f"   s_Gupta = {nstr(sG, 10)}, sigma_Gupta = "
          f"{nstr(sigG, 10)}")
    print(f"   rung-2 = {nstr(P['rung2'], 8)},  ratio = "
          f"{nstr(ratio, 8)}  in [0.7,1.3]: "
          f"{mpf('0.7') <= ratio <= mpf('1.3')}")
    print(f"   variant 'drop last term': sigma = "
          f"{nstr(sigma_of_s(sG_drop), 10)} (rel. change "
          f"{nstr(abs(sG - sG_drop) / abs(sG), 3)})")

print()
print("=" * 78)
print("SUPPLEMENTARY (non-deciding): ratios at C_* = 0.11, 0.28")
print("=" * 78)
for name, P in POINTS.items():
    a1, a2 = alpha1(P["c14"]), alpha2(P["c2"], P["c14"])
    cw = 2 * P["c1"]
    for C in (mpf("0.11"), mpf("0.28")):
        sG, _ = s_gupta_C(a1, a2, cw, C)
        sA = s_anchor(a1, a2, C)
        print(f"{name} C={nstr(C, 3)}: sigma_Gupta = "
              f"{nstr(sigma_of_s(sG), 8)}, sigma_anchor = "
              f"{nstr(sigma_of_s(sA), 8)}, ratio = "
              f"{nstr(sigma_of_s(sG) / sigma_of_s(sA), 6)}")

print()
print("=" * 78)
print("GUPTA FIG. 3 TUPLE SANITY: (a1, a2, cw) = (-1e-4, -4e-7, 1e-3)")
print("=" * 78)
sG, (t1, t2, t3) = s_gupta_C(mpf("-1e-4"), mpf("-4e-7"),
                             mpf("1e-3"), CSTAR)
print(f"s(0.17) = {nstr(sG, 8)} (terms {nstr(t1, 5)}, "
      f"{nstr(t2, 5)}, {nstr(t3, 5)})")
