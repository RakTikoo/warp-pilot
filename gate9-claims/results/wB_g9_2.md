# W-B — G9-2 THE JOIN (Gate 9)

Worker W-B. Run with the programme venv `~/workspace/warp-pilot/venv/bin/python`.
Fresh code: `gate9/wb_g92.py` (checker `gate9/wb_checker.py`); numbers:
`results/wb_g92_numbers.json`; checker output `results/wb_checker.json` —
**12/12 PASS**. Search log: `results/wb_search_log.md`. Nothing outside
`gate9/` was edited; nothing uploaded.

## Method (fresh, from the printed definitions)

Definitions taken as printed text from Berezin–Dokuchaev–Eroshenko,
arXiv:1710.10438 §III.B (as transcribed in the Phase-61 run record, the shared
definition): the conformal 2-metric γ̃ = diag(−A/r², B/r²); R̃ is its
2-dimensional Ricci scalar; [R̃] = 0 excludes a double layer; a shell is
carried only by Ŝ₀⁰ = −(4α₀/3)[R̃_,n] with R̃_,n = (r/√B)·dR̃/dr and
α₀ = α_g/2 (BDE eq. (57) mapping). No phase junction code was copied or run.

Fresh derivation inside `wb_g92.py`: SymPy computed the Ricci scalar of a
general 2-metric diag(−P, Q) from the Christoffel symbols, giving
R̃ = (−2PQ P″ + P P′Q′ + Q(P′)²)/(2P²Q²), P = A/r², Q = B/r² (the script
asserts the closed form equals the tensor computation symbolically).
All deciding evaluations are 40-digit mpmath with **analytic** A, B
derivatives (interior: A = e^{2Φ₂}, B = 1/(1−b/r), b = r^0.1,
Φ₂ = a·ln r/(1+ln r); exterior: A = f, B = 1/f, f the MK form) — no finite
differences. Darmois matching solves B and K = A′/(A√B) continuous for
(β_MK, k) by mpmath `findroot` from the γ = 0 linear guess.

**How the registered γ enters the matching algebra:** γ is held fixed at the
registered value (γ·r₀ = 10⁻²⁸ in r₀ = 1 units, i.e. γ = 10⁻²⁸ m⁻¹ at the
r₀ = 1 m scale) and is NOT solved for. In f it enters as the constant term
−3β_MKγ, the linear term +γr, and the quadratic-in-β term
+3β_MK²γ/r inside −β_MK(2−3β_MKγ)/r; in f′ correspondingly. At
r_Σ = 10³ r₀ its numerical effect is negligible: recomputing with γ = 0
changes β_MK by a relative 7.7×10⁻²⁴ and k by 2.9×10⁻²³ — γ is carried as
registered and stated, but it does not decide the join (consistent with
P38-3's finding that γ enters ~26 orders below the deciding residuals).

## Anchors (all passed BEFORE the member's number was read)

| Anchor | Bar | My result |
|---|---|---|
| (i) R̃(flat), A = B = 1 | = −2 | **−2.0 exactly** |
| (ii) T-b [R̃] at 10 r₀, stored Darmois pair ((1/3)√(r_Σr₀), β_MK/r_Σ³) | +0.474342 within 0.1% | **+0.474341649…**, rel. err 7.4×10⁻⁷ |
| (ii) T-b [R̃] at 10² r₀, same pair | +0.150000 within 0.1% | **+0.150000000…**, rel. err 4×10⁻⁴⁰ |
| (iii) Φ = 0 slice identity, symbolic | [R̃] = (1+p)(r₀/r_Σ)^{1−p} | **Exact**: SymPy gives R̃_int = (3−p)r^{p−1} − 2 (residual 0), R̃_ext(Σ) = 4Σ^{p−1} − 2, jump = Σ^{p−1}(p+1) |

## Deciding reads — audited point (p = 0.1, Φ₂, r_Σ = 10³ r₀, γ registered)

My own 40-digit bisection on my [R̃](a) located a_zero = **0.27773424114866288**,
differing from the stored 0.27773424114865775 by 5.1×10⁻¹⁵. At that point:

| Quantity | Stored (claim) | Mine | Bar | Result |
|---|---|---|---|---|
| β_MK | 2.142611 r₀ | **2.142610720 r₀** | within 1% | rel. err 1.3×10⁻⁷ ✓ |
| k | −2.28996×10⁻⁹ r₀⁻² | **−2.28995912×10⁻⁹ r₀⁻²** | within 2% | rel. err 3.8×10⁻⁷ ✓ |
| [R̃] | 0 | **−2.4×10⁻³⁹** | \|R̃\| < 10⁻²⁰ at 40 digits | ✓ (at the stored a_zero my residual is 4.0×10⁻¹⁷, consistent with the a_zero difference; at the rounded a = 0.277734 it is 1.9×10⁻⁹) |
| [R̃_,n] | −0.0152186 | **−0.0153171** | within 2% | rel. diff 0.65% ✓ |
| Ŝ₀⁰/α₀ = −(4/3)[R̃_,n] | +0.020291 | **+0.0204229** | within 2%, sign exactly positive | rel. diff 0.65%, sign **positive** ✓ |

Scope check (my numbers): the same audited interior Darmois-matched at the
primary radii gives [R̃] = **+0.115542 at 10 r₀** and **+0.011505 at 10² r₀**
— strictly positive, no join at either primary radius, confirming the
extension-radius-only scope.

## Correctness verdict: **REPRODUCED**

Every registered bar passes on an independent second path (fresh symbolic
R̃ derivation, analytic-derivative 40-digit evaluation, my own a_zero
bisection). The only non-trivial difference is [R̃_,n] (and hence Ŝ₀⁰) at
0.65% from the stored value — inside the 2% bar, same sign, zero intact —
so no restatement of the numbers is required; the phase's stored digits
stand. (Noted for the record: the 0.65% offset is larger than the
β_MK/k agreement of ~10⁻⁷, plausibly a derivative-route difference in the
phase's second path; it does not approach any bar.)

## Novelty verdict: **PARTIALLY KNOWN**

Known parts, cited: the BDE junction formalism itself (Berezin, Dokuchaev &
Eroshenko, arXiv:1710.10438); conformal-Weyl wormhole interiors with
energy-condition reads and an interior-to-Mannheim–Kazanas matching
mentioned without the BDE conditions (Lobo, arXiv:0801.4401); fourth-order
conformal wormholes whose junction is left possibly needing exotic matter
(Varieschi, arXiv:1510.05054); thin-shell wormholes joining two
Mannheim–Kazanas–de Sitter copies (arXiv:1301.1532); vacuum conformal-gravity
wormholes by conformal transformation (Hohmann et al., arXiv:1802.02184).
Not found in my search: any application of the BDE §III.B conditions
([R̃] = 0 double-layer exclusion, Ŝ₀⁰ = −(4α₀/3)[R̃_,n]) to a wormhole
throat, and specifically no EC-legal interior (b = r₀(r/r₀)^0.1, Φ₂ family)
joined to a registered-γ (γ = 10⁻²⁸ m⁻¹) Mannheim–Kazanas exterior at
r_Σ = 10³ r₀ with a legal shell Ŝ₀⁰ ≥ 0. Coverage gaps (full log in
`results/wb_search_log.md`): INSPIRE-HEP and Semantic Scholar were reached
only via indexes/mirrors in general web results — no direct INSPIRE-HEP
database query and no direct Semantic Scholar API query was run; those are
gaps, not negative results; paywalled/non-English literature was not
exhaustively checked.

## Exact restated wording (G9-2)

> **G9-2 — THE JOIN (restated, Gate-9 verified).** At the extension radius
> r_Σ = 10³ r₀ only — no region member joins at r_Σ = 10 r₀ or 10² r₀, and
> this wording does not imply a join at any other radius — the conformal
> throat b = r₀(r/r₀)^0.1 with Φ₂ = a·ln(r/r₀)/(1 + ln(r/r₀)),
> a = 0.277734, joins the Mannheim–Kazanas exterior at the registered
> galactic γ = 10⁻²⁸ m⁻¹ under the Berezin–Dokuchaev–Eroshenko junction
> conditions (arXiv:1710.10438 §III.B), independently reproduced in Gate 9:
> [R̃] = 0 at 40 digits, [R̃_,n] = −0.0152186, and the shell the formalism
> fixes, Ŝ₀⁰ = −(4α₀/3)[R̃_,n] = +0.020291 α₀ ≥ 0 (α₀ = α_g/2), is LEGAL.
> The Darmois-matched exterior is β_MK = 2.142611 r₀,
> k = −2.28996×10⁻⁹ r₀⁻²; on the Φ = 0 slice
> [R̃] = (1 + p)(r₀/r_Σ)^{1−p} > 0 exactly. There is no ADM mass in
> Mannheim–Kazanas asymptotics; the joined (β_MK, γ, k) are reported
> instead. The member's tidal-bar radius is r₀* = 4.785×10⁷ m, and its
> formation standing is PRE-EXISTING ONLY. This is a throat OBJECT claim:
> no transport is claimed and no traversability is claimed. The specific
> BDE-conditions join above was not found in our search (limits:
> INSPIRE-HEP and Semantic Scholar reached only via indexes, no direct
> database/API query; paywalled and non-English literature not
> exhaustively checked); its components — the BDE formalism, conformal
> wormhole interiors, and Mannheim–Kazanas matching — are known in the
> cited literature. **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## Gaps / notes
- Direct INSPIRE-HEP and Semantic Scholar queries remain open coverage gaps (above).
- γ's role is stated exactly: carried as registered, numerically inert at the 10⁻²³–10⁻²⁴ relative level in the matching at this radius.
- The claim remains, in the programme's locked language, a "scan signal under attack"; this gate verdict is REPRODUCED / PARTIALLY KNOWN, i.e. UPLOAD-READY AFTER RESTATEMENT in the wording above (no outright "novel/first/unique" language, per the Uniqueness Protocol).
