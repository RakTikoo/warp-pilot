# W-D — G9-4 FORMATION of the conformal joining member

Worker W-D, Gate 9. Claim G9-4 (P61-4 + P71-2): the frozen
Φ₂ family (p = 0.1, a = 0.277734), formation standing
**PRE-EXISTING ONLY**. All runs with the programme venv
`~/workspace/warp-pilot/venv/bin/python`. Fresh code in
`gate9/wd_*.py`; numbers in `results/wd_g94_numbers.json`;
checker `gate9/wd_checker.py` over that JSON; search log
`results/wd_search_log.md`.

## Machinery (fresh, anchor-validated before any claim number)

W-D did **not** use W-A's engine and did not import any
phase script. `wd_derive.py` derives the Bach tensor for
the static spherical ansatz from the metric (Christoffel →
Riemann → Ricci → Ricci-form Bach, the shared definition),
giving jet formulas B^t_t, B^r_r, B^θ_θ in
(r, b₀…b₄, P₁…P₄); symbolic trace ≡ 0. Anchors, all run
before any claim number was read:

- Schwarzschild (MT coordinates, b = r_s,
  Φ = ½ ln(1 − r_s/r)): B = 0.0 exactly at the test points.
  (An initial anchor attempt with Φ = 0 failed at
  6.6×10⁻² — that metric is not Schwarzschild; the error
  was in the anchor's jets, not the engine, as the two
  anchors below already passed. Corrected and re-run.)
- Mannheim–Kazanas ansatz (generic β = 2, γ = 0.01,
  k = 0.001): max |B| = 8.91×10⁻¹⁷ (scale r⁻⁴ = 1.6×10⁻³).
- T-b (p = ½, Φ = 0) vs Phase-32/P61-4 closed forms
  (T-convention): max relative deviation 2.05×10⁻¹⁶;
  throat NEC1 (B-convention) = 0.10416666… = (5/12)/4. ✓

## Clause-by-clause verdicts

### (a) Frozen family + scale covariance — REPRODUCED

Direct (unscaled) evaluation with physical jets of
b(r; r₀) = r₀(r/r₀)^0.1 and Φ₂(r; r₀) at r₀ = 10 and
r₀ = 10³, matched x = r/r₀ ∈ {1, 1.3, 3, 7, 30, 100, 1000},
all six EC combinations: max relative deviation vs the
scaled read F(x)/r₀⁴ is **5.18×10⁻¹³** (r₀ = 10) and
**1.31×10⁻¹²** (r₀ = 10³) — inside the registered bar
< 10⁻⁹ (the phase record's "0.0" was its own evaluation
route; the deciding content, covariance at bar precision,
holds). From covariance, legality at all 8 ladder radii
1 m → 4.785×10⁷ m follows in the phase's stated form.
The r₀ = 1 legality read itself is W-A's (G9-1); as a
supporting cross-check only, W-D's own grid at r₀ = 1 has
all six combinations > 0 on [1, 10³] (minima at the tail:
NEC1 1.230×10⁻¹⁵, DEC_t 6.149×10⁻¹⁶, matching the stored
P61-1 minima).

### (b) Common-domain increment (fresh Class-B read-off) — REPRODUCED

Fresh implementation of the read-off from its shared
definition (new slice minus old slice on the common
domain; grown shell = new slice's closed form on
[r₀_j, r₀_{j+1}]). Decade step, scaled units r₀_{j+1}⁻⁴:

- Δ minima: ΔNEC1 = ΔDEC_r = **−0.016679355263679**
  (stored −0.016680; within 0.004%), ΔDEC_t =
  −0.008339677631838; Δρ, ΔNEC2, ΔSEC positive everywhere.
  Failures confined to exactly {NEC1, DEC_r, DEC_t}. ✓
- Failure layer: ΔNEC1 < 0 exactly on x_b ∈ [1, **1.0034815202679233**]
  (bisected crossing; stored 1.00348 — same digits). ✓
- Layer price: E_legal re-derived from the P61-4 record,
  E_legal(L) = (3/(32π²))ħc/L (at L = 10 m:
  3.00309032448144×10⁻²⁹ J, matching p614_results.json);
  integrated negative ΔNEC1 (T = 4α_g·B) over the layer
  gives **5.828036304258646×10⁶⁸ × E_legal** per decade
  step (stored 5.83×10⁶⁸; factor 0.9997, bar factor 2). ✓

### (c) Pole anatomy / singular shell — REPRODUCED

- Analytic: Φ₂ = a·L/(1 + L), L = ln x_b; the denominator
  1 + ln x_b = 0 at L = −1, i.e. **x_b = e⁻¹ exactly**,
  inside every Class-B shell interval. ✓
- 40-digit mpmath probes (W-D's engine): NEC1 =
  **−6.58154461639×10²¹** at e⁻¹(1−10⁻³) and
  **−6.64506547545×10⁴²** at e⁻¹(1−10⁻⁶) — negative, and
  digit-for-digit the stored values (bar: factor 3).
  Supporting probe at x_b = 0.99: NEC1 =
  −0.0500024683181, also digit-for-digit. ✓
- Pole order by log–log fit of |NEC1| vs |1 + ln x_b|,
  δ = 10⁻²…10⁻⁵: **7.009** (stored ≈ 7; bar 7 ± 1);
  order ≥ 2 in the integration variable makes the shell
  integral non-integrable. ✓
- Shell price lower bounds per decade step (fresh
  integration, pole-exclusion ε in |1 + ln x_b|):
  **6.925055976328622×10⁸⁴** (ε = 10⁻²),
  **7.32659837454598×10⁹⁰** (ε = 10⁻³),
  **1.7106788738441663×10⁹⁶** (ε = 10⁻⁴) × E_legal —
  factors 1.000 / 1.000 / 0.9998 of the stored bounds
  (bar: factor 10), **strictly increasing as ε → 0**. ✓
  The deciding content — the shell price per decade step
  is **UNBOUNDED**, against T-b's finite 2.216×10⁷³ ×
  E_legal (P61-4 record) — holds on the fresh path.

### (d) Nucleation inheritance (document audit + fresh symbolic check) — REPRODUCED

Every premise of P61-4's fork, extracted from
`p614_memo.md` §(b) in substance:

1. Conformal-gravity instantons exist
   (Strominger–Horowitz–Perry, Nucl. Phys. B238 (1984)
   653): asymptotically Euclidean extrema of the
   conformally invariant action, arbitrary Euler number /
   signature, tunnelling between zero-curvature vacua and
   between flat space and topologically non-trivial
   zero-energy initial data. They are not throat-creating
   bounces: no Morris–Thorne handle, action fixed by
   topological invariants, no S_E(r₀). — Quantifies over
   **the conformal action's Euclidean sector (the home)**.
2. The Giddings–Strominger Euclidean wormhole is
   O(4)-symmetric of Robertson–Walker form
   dτ² + a(τ)²dΩ₃². — **RW geometry as such**.
3. All RW metrics have C_μνρσ = 0 (sourced in P61-4:
   J. Math. Phys. 48 (2007) 122501). — **RW geometry as
   such**.
4. Hence the Weyl action of the candidate bounce vanishes
   identically on that class. — **The home's action**.
5. The geometry is not a solution of the home's equations
   with its axion matter: B = 0 forces T = 0 under
   T = 4α_g·B, and the axion's T ≠ 0. — **The home's Bach
   equation**.
6. What prices the GS bounce in the literature is the
   Einstein–Hilbert + axion action — a different theory's
   action; no source prices a throat bounce inside
   conformal gravity (named absence). — **Home-level
   literature statement**.
7. The (H-GR) area-law analogue (derivation class (B))
   is rejected because it prices an Einstein–Hilbert
   bounce on that conformally-flat class. — **The home's
   action + the geometry class**.
8. Lorentzian wormholes in Weyl gravity
   (Varieschi–Ault; Heydari-Fard et al.) are classical
   solutions, not nucleation bounces. — **Home-level**.

No premise mentions T-b's b = √(r r₀), its Φ = 0, or any
(p, Φ, a) value, and none mentions the Φ₂ member.
Inheritance therefore holds as argued in P71-2.

Fresh symbolic check (W-D's own `wd_rw.py`, general RW
metric −dt² + a(t)²[dr²/(1 − kr²) + r²dΩ²], a(t)
arbitrary, k free): all four mixed Bach diagonal
components simplify to **exactly 0**; the Weyl tensor's
only components left unreduced by plain simplify share
the trig factor −sin(2θ)tanθ − cos(2θ) + 1, which
`wd_rw_trig.py` reduces to exactly 0 (fu), so C ≡ 0
identically as well. The conformally-flat clause is
verified on the fresh path.

## Overall correctness verdict: REPRODUCED

All four clauses (a)–(d) hold on W-D's independent second
path, inside every registered bar — most deciding numbers
agree with the stored records to all printed digits.
Checker: `wd_checker.py` over `wd_g94_numbers.json`
(anchors, bars (a)–(d)) — **16/16 PASS**.

Carried, not hidden: the **dynamic growth read remains
UNCOMPUTED for this member** (P71-2, FU-P712-1: the
time-extended Bach derivation for Φ₂(r,t) did not close;
expression swell in the Φ_t-bearing terms). The shell
verdict is scored under the **Phase-30 Class-B read-off**
(the new slice's closed form extended inside its own
throat, x < 1), exactly as P30-1/P61-4 scored their rows
and as recorded in P61-4/P71-2; an intermediate-slice
shell fill would be a different registered read. The
formation standing is **PRE-EXISTING ONLY**. C12: this is
a throat OBJECT claim — no transport is claimed, no
traversability is claimed. The member's tidal-bar radius
r₀* = 4.785×10⁷ m (P61-1) rides with the claim set.

## Novelty verdict: PARTIALLY KNOWN (per clause)

Search log: `results/wd_search_log.md` (11 queries
verbatim, sources checked, 2026-11-22).

- Clauses (i)/(a) and the premises of (iv)/(d): **KNOWN
  ingredients**. EC-legal static wormholes in conformal
  Weyl gravity are published (Lobo, arXiv:0801.4401;
  Varieschi–Ault, arXiv:1510.05054); conformal-gravity
  instantons exist as vacuum-tunnelling saddles with
  topological action and no throat (Strominger–Horowitz–
  Perry, Nucl. Phys. B238 (1984) 653; self-dual instantons
  without throats, Corral–Giribet–Olea,
  arXiv:2105.10574); the Giddings–Strominger class is
  RW/O(4) and RW ⇒ C = 0 is textbook. Scale covariance
  T = r₀⁻⁴F(r/r₀) is a structural property of the ansatz.
- Clauses (ii)/(b), (iii)/(c), and the fork-as-closure
  with its inheritance audit in (iv)/(d): **not found in
  our search** — no growth/increment audit, no Class-B
  grown-shell read-off, no exotic-price-vs-E_legal table
  (finite or unbounded), no Φ₂-type pole inside a shell
  extension scored as a formation obstruction, and no
  conformally-flat fork closing nucleation for the Weyl
  home was found for any conformal-gravity wormhole.
  Near neighbours are Lorentzian classical solutions
  only (Hohmann et al., arXiv:1802.02184; Oliva–Tempo–
  Troncoso, arXiv:0907.1128; Cadoni et al.,
  arXiv:2503.14214; Heydari-Fard et al.,
  arXiv:2312.07588), a conformally non-invariant model
  (Darabi, arXiv:1012.1012), or other theories (GR
  nucleation, Horowitz et al., arXiv:1904.02187; EiBI
  instantons, arXiv:1809.06579).

**Coverage gaps (plainly):** INSPIRE-HEP and Semantic
Scholar were reached only via their indexed records in
the general search index (site:-restricted queries);
neither database's own search interface was queried
directly, so a record visible only inside those
interfaces could have been missed. arXiv and the general
web were searched directly. A search that could not be
run is a gap, not a negative result; the "not found"
statements above are bounded by this coverage.

## Exact restated wording

> **PRE-EXISTING ONLY** (standing, never separated). The
> conformal joining member (frozen Φ₂ family, p = 0.1,
> a = 0.277734, scored gauge Ω = 1, T = 4α_g·B, α_g > 0)
> is a throat OBJECT (C12: no transport claimed, no
> traversability claimed); its tidal-bar radius is
> r₀* = 4.785×10⁷ m. Formation (Gate 9, G9-4, reproduced
> on an independent second path): (i) the frozen family
> is EC-legal at all 8 ladder radii 1 m → 4.785×10⁷ m by
> scale covariance T = r₀⁻⁴F(r/r₀), verified by direct
> evaluation at r₀ = 10 and r₀ = 10³ (max relative
> deviation ≤ 1.31×10⁻¹²); (ii) the common-domain growth
> increment fails NEC1/DEC_r/DEC_t only in a thin inner
> layer x_b ∈ [1, 1.00348], ΔNEC1 = −0.016680
> r₀_{j+1}⁻⁴ scale-free, priced 5.83×10⁶⁸ × E_legal per
> decade step; (iii) the grown shell under the Phase-30
> Class-B read-off (the new slice's closed form extended
> inside its own throat, x < 1 — the shell failure is a
> property of this registered read-off, scored as P30-1
> scored its rows, as recorded in P61-4/P71-2) is
> SINGULAR: Φ₂ = a·ln(x)/(1 + ln x) has a pole at
> x_b = e⁻¹ where all ECs diverge (40-digit NEC1 =
> −6.58×10²¹ at e⁻¹(1−10⁻³), −6.65×10⁴² at e⁻¹(1−10⁻⁶);
> pole order ≈ 7, non-integrable), so the shell price
> per decade step is UNBOUNDED (lower bounds ≥
> 6.925×10⁸⁴ / 7.327×10⁹⁰ / 1.711×10⁹⁶ × E_legal at
> pole-exclusion ε = 10⁻²/10⁻³/10⁻⁴, strictly increasing
> as ε → 0), against T-b's finite 2.216×10⁷³ × E_legal;
> growth is therefore GROWABLE-ONLY-EXOTICALLY, and the
> dynamic growth read is UNCOMPUTED for this member
> (carried, not hidden); (iv) nucleation is CLOSED as a
> property of the theory's home by P61-4's
> conformally-flat fork, inherited by this member:
> every fork premise quantifies over the conformal
> action's Euclidean sector, Robertson–Walker geometry
> as such, or the Bach equation, and none over any
> throat family's (b, Φ). Novelty: PARTIALLY KNOWN —
> the ingredients (EC-legal Weyl-gravity wormholes;
> throat-less conformal instantons; the conformally
> flat Giddings–Strominger class) are published; the
> growth-increment audit, the singular-shell unbounded
> price, and the fork closure with its inheritance
> audit were not found in our search (limits:
> INSPIRE-HEP and Semantic Scholar reached only via
> indexed records, not their own search interfaces;
> arXiv and the general web searched directly,
> 2026-11-22). (V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).

## Files

- Code: `gate9/wd_derive.py`, `gate9/wd_audit.py`,
  `gate9/wd_rw.py`, `gate9/wd_rw_trig.py`,
  `gate9/wd_assemble.py`, `gate9/wd_checker.py`;
  derived data `gate9/wd_generic_bach.json`,
  `gate9/wd_audit_raw.json`, `gate9/wd_rw_result.json`,
  `gate9/wd_rw_trig.json`.
- Numbers: `results/wd_g94_numbers.json`.
- Search log: `results/wd_search_log.md`.
- Nothing edited outside `gate9/`; nothing uploaded.
