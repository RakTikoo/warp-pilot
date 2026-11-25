# PHASE 307 — MEMO: BREAK THE CHANNEL (red team on the spin-1 result)

**Registration:** `phase307/work/p307_registration.md` (charge:
ledger 761; every arm's test, scope, and verdict forms fixed
before any arm ran). **Arm records:** `phase307/work/
p307_arm{1..7}_memo.md` (+ `p307_arm6_run.py`/`.out`).
**Controls (coordinator, before all arms):** Phase 303's
`p303_pricing.py` re-run reproduces Corner B HT 2.0607×10⁻¹⁸
and the flat rows HT 2.8044×10⁻⁵ / NS–BH 2.5394×10⁻² exactly;
`p303_audit.py` reproduces the stored fence tables including
Corner A's L9 reads 0.15411 / 0.31451 / 0.53153
(`p307_controls_pricing.out`, `p307_controls_audit.out`).

## OVERALL VERDICT: CHANNEL BROKEN

Two of seven arms break the Gate-32 claim set, at two
different scopes (registration: scopes are never merged):

- **ARM 1 BREAKS the flat value (G32-F's number).** At the
  confidence level L9's own tolerance implicitly uses, the
  J1738 timing data support a dipole cap of 0.067, not 0.1;
  the flat value falls to **HT 1.87×10⁻⁵** (NS–BH
  1.70×10⁻²), a factor 0.67 of 2.8044×10⁻⁵.
- **ARM 2 BREAKS Corner B (G32-E).** Corner B's (c₊, c₋)
  projection lies outside YBBY Fig. 7's combined drawn
  allowed region by 0.163 in c₋, ~55× the digitisation
  error.

The distance-0 statement (G32-G) is **not** broken: at the
data-grade flat value it still clears its bar by ×18.7
(§2). But G32-F and G32-E may not be quoted in their Gate-32
§5 forms; the affected claims return to a gate (the parent's
action, not this phase's). One arm FENCES the flat value's
pricing framework (Arm 4), three hold (Arms 5, 6 strong;
Arms 3, 7 weak, worded as such), and one point inside Arm 2
is UNRESOLVED (subsumed by the breaks; recorded in §3).

---

## 1. ARM 1 — THE TOLERANCE ITSELF: **BREAKS** (scope: the flat value)

**Retrieval (primary grade, full text).** Freire et al.
2012 (MNRAS 423, 3328), PSR J1738+0333: P_b =
0.3547907398724(13) d; Ṗ_b^obs = (−17.0 ± 3.1)×10⁻¹⁵;
Shklovskii +8.2 and Galactic +0.58 fs/s corrections give
Ṗ_b^Int = (−25.9 ± 3.2)×10⁻¹⁵ against Ṗ_b^GR =
−27.7⁺¹·⁵₋₁·₉×10⁻¹⁵ — an excess of +2.0⁺³·⁷₋₃·₆ fs/s.
Ratio R ≡ Ṗ_b^Int/Ṗ_b^GR = 0.9350, σ_rel = 0.132 (the
paper's published 0.94 ± 0.13 corroborates). The measured
decay is *slower* than GR's by 6.5% centrally.

**What Eq. (190) actually is.** YBBY Eq. (190) bounds the
TOTAL δṖ = ⟨𝒜⟩ − 1 (dipole + quadrupole pieces together),
as a linear sum of 1σ-class observational and inferred-
parameter errors, stated generically as O(10%). YBBY never
applied it to J1738's Ṗ_b — §VII C.1 sets J1738's Ṗ_b aside
as the weaker constraint (J1738 enters their bands via the
α̂ Eqs. 194–195) and Eq. (191) does the actual band work.
The programme's fence (Phases 294/303, registered) applies
0.1 to the dipole piece with the quadrupole deviation
bounded separately (≤ 2.62×10⁻⁵ at the deciding corner —
3–4 orders below every cap in play, so the decomposition
itself is not the issue).

**The data-grade cap.** In the fence's registered
decomposition, cap_dip = (R − 1) + n·σ_rel (the quadrupole
bound subtracted changes nothing at the quoted digits):
- **n = 1 — the tolerance's own implicit confidence**
  (Eq. 190 is a linear sum of 1σ errors): **cap = 0.067**
  (0.070 from the published ratio). The 0.1 figure silently
  spends the −6.5% central offset — the fact that the
  measured decay is slower than GR — as if it were headroom
  for a positive dipole excess.
- **n ≈ 2 (95% CL, the convention of legs L7/L8):**
  cap = 0.193. The flat value would then RISE to
  5.42×10⁻⁵ and the arm would hold.
- The adopted 0.1 sits at **1.25σ** — defensible at no
  single stated confidence level. This mismatch is the
  break's substance: not that 0.1 is unphysical, but that
  the fence's other legs are 95% statements while L9's
  number is a 1.25σ statement wearing an order-of-magnitude
  label.

**Re-pricing.** The maximised ratio is exactly linear in
the cap once L9 binds (Gate-32's skeleton; verified against
`p303_pricing.py`'s own formulas — the skeleton reproduces
2.80438×10⁻⁵ at cap 0.1 — and by an independent coarse
re-maximisation at cap 0.0668 reaching 1.83–1.86×10⁻⁵ from
below with L9 binding). At cap 0.067: **flat HT =
1.87×10⁻⁵, NS–BH = 1.70×10⁻²**. The 2026 timing update
(Vaglio et al., Ṗ_b = −1.82 ± 0.25×10⁻¹⁴) was used
indicatively only (its own Ṗ_b^GR not cleanly extractable
— gap named in the arm memo): its 1σ cap ≈ 0.095, still
below 0.1, so the break is not an artefact of the 2012
error budget.

**Scope discipline.** The break is to the flat VALUE.
Flatness itself (speed-independence) is untouched — the
value is linear in the cap at every speed alike. And the
distance-0 bar is not broken by this arm (§2).

## 2. What Arm 1 does to G32-G (distance-0)

The registered bar is HT ≥ 10⁻⁶ at c_V ≥ 2. At the
data-grade cap the flat rows stand at 1.87×10⁻⁵ — the bar
is still cleared, by **×18.7**, at c_V = 2 and c_V = 10
alike (far-zone pricing). G32-G therefore survives Arm 1
in substance, but its Gate-32 §5 wording quotes
2.8044×10⁻⁵ as the meeting ratio; that number is broken
and the claim returns to a gate for restatement at
1.87×10⁻⁵ (with Arm 4's fence also attached, §4).

## 3. ARM 2 — THE BANDS AS DRAWN: **BREAKS** (scope: Corner B)

**The figure, established first.** YBBY Fig. 7's panels are
all in the (c₊, c₋) plane — Ṗ_b bands for J1141/J0348/J0737
plus J1738 via α̂ (not via Ṗ_b). Crucially, α₁/α₂, masses,
P_b and EoS sensitivities are *varied*, not held fixed:
the bands are **existential projections**. Inside a band is
therefore only ever a weak hold (some varied parameter
choice puts the point there); outside is a clean exclusion
(no varied choice does). Retrieval limit, on the record:
the figure's raster/vector data were not extractable with
text-fetch tools, so the digitisation is **text-grade**,
built from YBBY's own §VII C.1 numbers — per-system band
width O(10⁻³) in c₋; the combined (Fig. 1) intersection an
almost-box of Δc₋ = O(10⁻³), Δc₊ = O(10⁻²) containing the
origin — with adopted read-off error **±3×10⁻³ in c₋**.
(The arm also corrects a Phase 303 aside: the bands are
not "computed inside the fits' region"; the Eq. (186)/
Appendix C fits are a separate object.)

**Per-point verdicts** (slice points project to (0, c₋)):
- c_V = 1 maximiser, c₋ = 5.314×10⁻⁶: **HOLDS (weak)** —
  inside the combined region.
- c_V = 2 maximiser, c₋ = 5.089×10⁻⁵: **HOLDS (weak)** —
  inside.
- c_V = 10 maximiser, c₋ = 1.590×10⁻³: **UNRESOLVED** —
  exceeds the nominal 10⁻³ box extent by 0.59×10⁻³, inside
  the ±3×10⁻³ text-grade error. Pixel-grade figure data is
  the exact gap. (Subsumed in the overall verdict by the
  breaks; it does not block anything because the overall
  form is already BROKEN.)
- **Corner B, c₋ = 0.16586208: BREAKS.** Outside the
  combined drawn allowed region by **0.163 in c₋ — ~55×
  the digitisation error, ~166× the nominal box width**.
  No varied parameter choice in YBBY's bands reaches
  c₋ = 0.166 on the c₊ = 0 line.

**Scope and the open discrepancy.** The break is at
projection scope, and it contradicts Phase 303 §4(ii)'s
recording that the bands' combined region "is consistent
with" this phase's fence. Both cannot stand as recorded:
the mechanism fence (L1–L9, rung-2 σ) passes Corner B,
while the drawn bands exclude its projection. Which leg's
rung-2 modelling (the anchor σ at c₋ = 0.166, deep in the
region Gate-32 §2 fenced as un-cross-checked; or the
bands' own varied-sensitivity construction) accounts for
the discrepancy is a **successor diagnosis**, named here
and not adjudicated by this phase. G32-E may not be quoted
until that diagnosis lands.

## 4. ARM 4 — THE DISPUTE: **FENCED** (scope: the flat value's pricing framework)

Taherasghari & Will (PRD 108, **124026** (2023) — Gate-32's
"102026" citation is corrected by this arm — and PRD 112,
024013 (2025)) derive the near-zone radiation-reaction
dE/dt; their dipole bracket depends on the vector speed
only (no scalar-speed term — their relaxed equations carry
no wave equation at v_L). TW do **not** claim the balance
law fails or the far-zone flux is wrong: the discrepancy
is left explicitly open in their text. Substituting their
coefficient as replacement pricing would exceed their
stated scope — hence FENCED, not BREAKS. Post-TW, Vaglio
et al. 2026 (PRD 114, 104021) engage TW explicitly and
deliberately adopt the balance-law expression with stated
reasons; Albertini–Vaglio–Barausse 2026 confirm the spin-0
mode is a dynamical energy-carrying wave nonlinearly,
while declining to decide the binary question.

Quantitatively (mapping cross-validated: the far-zone
bracket equals 3𝒞 exactly, ≤1.3×10⁻⁵, at all points;
sensitivities cancel to ≲10⁻⁵ at these σ): under TW's
coefficient, ⟨𝒜⟩_dip at the far-zone maximisers falls to
0.03001 (c_V = 2) and 3.00×10⁻⁴ (c_V = 10) — L9 stops
binding, flatness disappears (TW dipole ∝ c_V⁻³; the
maximisers' 𝒞 is 80% / 99.8% the disputed scalar piece),
and the rows re-price to **HT 8.415×10⁻⁶ at c_V = 2**
(still above the 10⁻⁶ bar) and **8.42×10⁻⁸ at c_V = 10**
(below it). **Fence wording handed to the claim set:
G32-F (and G32-G at c_V = 10) stand exactly and only where
energy-balance/far-zone pricing is the correct Ṗ_b
pricing.** Corner B and Corner A are not re-decided by
this arm (their TW dipole reads stay inert / out of
scope).

## 5. ARM 3 — FULL-THEORY COSMOLOGY: **HOLDS (weak)**

The full-EA dictionary was derived from EA sources and
sympy-verified (Jacobson arXiv:0711.3822 §3): G_cos/G_N =
(2−c₁₄)/(2+c₁₃+3c₂) — on the slice, G_cos/G_N − 1 =
−(c₁₄+3c₂)/(2+3c₂), a different combination from Phase
302's khronometric one, as registered. Point values are
tiny at the flat rows (−5.3×10⁻⁶ … −1.6×10⁻⁵) and
−0.125000 at Corner B (its BBN saturation). **No
retrievable primary full-EA cosmological constraint
excludes any tested point** — an absence statement, not a
pass: the only EA-native cosmology MCMC (Zuntz et al.
2008) scans classes the points are not in (class 𝒞 is
PPN-exact — on the slice it demands c₂ = c₁₄ = 0; class ℰ
demands c₁ = c₃ = 0); Audren et al. 2015's EA case imposes
α₁ = α₂ = 0 as exact priors (every point has α₁ = −4c₁₄
≠ 0); the generalised F(K) line has no projection onto the
linear c_i corner (confirmed, not inherited); no EA
fσ8/growth bound on the c_i was found.

Two conditional threats recorded in full, neither a break:
(i) FB2021's khronometric cap 1.9×10⁻³ would exclude
Corner B by ×65.8 **if transferred** — the transfer is not
licensed (Hořava ξ = 1 scope, no spin-1 sector), and the
flat rows pass that cap anyway by ×119–357; (ii) Audren's
EA-surface limit c_χ² < 427 (95% CL): the flat rows pass
by ~×425, but **Corner B (c_χ² = 1.055×10⁷) exceeds it by
×2.47×10⁴** — a surface-scoped limit the point is not on,
given the same disposition Phase 302 gave the identical
kh structure, and flagged by the arm itself as a *method*
protection, not a physical one. An off-surface EA MCMC is
the named instrument that could convert either record
into a verdict. Corner B thus accumulates, alongside
Arm 2's outright break, two recorded cosmological threats
whose only shield is scope.

## 6. ARM 5 — STABILITY AT THE POINTS: **HOLDS**

Published conditions taken from OMW PRD 97, 124023 §III/
App. A directly: ghost-freedom q_{S,V,T} > 0 (Eqs. 3.1–3.2;
A.10/A.13/A.16), gradient stability c²_{S,V,T} > 0
(Eqs. 3.3–3.4; A.11/A.14/A.17), plus Jacobson §4 energy
signs; slice forms verified against the source (scalar
speed = w₀², q_S = (2+3c₂)/c₂). Every condition passes at
all five points: q_S = 7.50×10⁵ / 3.14×10⁵ / 2.51×10⁵ at
the maximisers (c₂ tiny but strictly positive — the
condition is satisfied hugely, not marginally), 24.0 at
Corner B, 8.00×10⁴ at Corner A; q_V = c₁₄ > 0 everywhere
(7.9×10⁻⁹ at Corner B, strictly positive); speeds² —
c_T² = 1, c_V² = 1/4/100/1.050×10⁷/4000, c_S² =
1.00406/1.00018/1.00137/1.055×10⁷/1.00000 — all positive;
energy signs 2c₁ and c₁₄(2−c₁₄) positive throughout,
c₁₄ ∈ (0, 2) at all points. Corner B's scalar
superluminality was explicitly not scored as an
instability; the Čerenkov condition (OMW Eq. 3.5) was
reported but not scored (separate fence leg). No point is
killed by its own theory's consistency conditions —
including Corner A, whose death remains a fence death
(G32-D), not a stability death.

## 7. ARM 6 — THE EDGE: **HOLDS**

Identification confirmed with one correction of form:
w₀² is YBBY Eq. (108), the spin-0 companion's squared
speed; the w₀ > 1 side exists because a subluminal mode
would be vacuum-Čerenkov-radiated by UHECRs. The enforcing
leg L5 is coded in Phase 303 as a hard zero-tolerance
exclusion, whereas the physical bound (Moore & Nelson
2001; Elliott–Moore–Stoica 2005) is c² > 1 − ~10⁻¹⁵ —
immaterial at every δ tested. Nothing degenerates at
w₀ = 1 (the scalar energy sign is w₀-independent; 𝒞 and
the flux coefficients are finite and smooth there); it is
a regular point made an edge only by the Čerenkov leg.
Interior re-run (δ = 0 controls reproduced 2.804394×10⁻⁵ /
2.804397×10⁻⁵ first): at δ = 10⁻⁴ and at the registered
δ = 10⁻³, the flat value is reproduced **to all quoted
digits** at c_V = 2 and 10, L9 still binding at exactly
0.10000, maximisers moving ≤ 0.16% in c₁₄. At δ = 10⁻²
the regime changes (c₁₄ re-solves down ×5.8–7.3, binding
leg switches L9 → L8, HT falls to 4.76×10⁻⁶ / 3.78×10⁻⁶ —
below the envelope floor but still ×1.2×10³ / ×1.6×10⁵
above the spin-0 row at the same speeds). Verdict: the
flat value is edge-hugging but robust, not an edge
artefact. (Arm 6's values are at L9's registered cap 0.1;
Arm 1's data-grade cap rescales them linearly, per §1 —
at δ = 10⁻³ and cap 0.067 the interior value is 1.87×10⁻⁵
by the same linearity.)

## 8. ARM 7 — POLARISATION CONTENT: **NOT APPLICABLE** (weak HOLD)

What the tests bound: detected-signal content. GW170814
(Abbott et al., PRL 119, 141101) favours pure tensor over
pure vector (BF ≈ 200) and pure scalar (≈ 1000) for that
one BBH signal. GWTC-3 §VII (PRD 112, 084080, null-stream,
mixed hypotheses) gives combined log₁₀ B vs tensor of
−4.24 (pure S) and −1.70 (pure V), but +0.20 / +0.31 /
−0.08 for the mixed TS / TV / TVS hypotheses — mixed
content "cannot be ruled out conclusively" — and states
no amplitude limit and no coupling bound. The one
amplitude-style result in the class (Cheung et al. 2026)
gives 90% fractional-strain limits 0.28–11.30 (median
1.32) — signal content again. Four independent
applicability failures: (1) band — the fiducials' dipole
emission sits at f_orb = 3.58×10⁻⁵ Hz (HT) / 3.27×10⁻⁵ Hz
(J1738), 5.45 orders below the detector band's bottom;
(2) observable — signal content of detected events vs a
flux ratio for unobserved systems; (3) no retrieved source
states or translates to a bound on c₁, c₋, or any EA
coupling (no EA LIGO-band merger waveform map exists in
the retrieved literature; the tests also assume
co-propagating modes, while these points have c_V =
1–3240); (4) even the median fractional-strain limit sits
~5 orders above the channel's ratio, in the wrong band
for the wrong sources. NOT APPLICABLE with reasons =
weak HOLD, as registered.

## 9. State of the claim set after the red team

- **G32-A (structure):** untouched by every arm. Stands.
- **G32-B:** already FAILED at Gate-32. Unchanged.
- **G32-C (σ values, rung-2):** not directly attacked by
  any arm (Arm 4's mapping found σ cancelling in the
  TW/far ratio at these points). The Gupta cross-check
  (Phase 306) remains the outstanding second path.
- **G32-D (Corner A dead):** untouched; Arm 5 confirms
  the death is a fence death, not a stability death.
  Stands.
- **G32-E (Corner B):** **BROKEN at projection scope**
  (Arm 2), with two scope-shielded cosmological threats
  recorded against it (Arm 3). Not quotable until the
  bands-vs-mechanism-fence discrepancy is diagnosed.
- **G32-F (flat value):** **BROKEN as valued** (Arm 1):
  the data-grade value at L9's own implicit confidence is
  HT 1.87×10⁻⁵ / NS–BH 1.70×10⁻²; at the fence's 95%
  convention it would be 5.42×10⁻⁵. Flatness, the ridge,
  and the mechanism survive (Arms 5, 6); the pricing
  framework is **FENCED** to far-zone/balance-law pricing
  (Arm 4).
- **G32-G (distance-0):** not broken in substance — the
  bar is met at c_V = 2 under every pricing on record
  (1.87×10⁻⁵ far-zone data-grade; 8.415×10⁻⁶ under TW)
  and at c_V = 10 under far-zone pricing (1.87×10⁻⁵) but
  **not** under TW pricing (8.42×10⁻⁸). Its Gate-32 §5
  wording quotes the broken 2.8044×10⁻⁵ and is therefore
  not quotable as written; the claim returns to a gate
  for restatement carrying the data-grade value and
  Arm 4's fence.

**Successor diagnoses named by this phase (charges are
the parent's):** (i) the bands-vs-fence discrepancy at
Corner B — which rung-2 modelling choice drives it;
(ii) pixel-grade digitisation of YBBY Fig. 7 to resolve
the c_V = 10 maximiser's band status; (iii) an
off-surface EA cosmology MCMC, the only instrument that
can convert Arm 3's two conditional threats into
verdicts; (iv) the outstanding Gupta σ cross-check
(Phase 306, already charged elsewhere).

## 10. Reality Desk

`DESK: Phase 307 contacted data beyond the fences applied
in Phases 291–303 in one arm that changed a number — ARM 1
(PSR J1738+0333's measured orbital-period derivative at
published precision, Freire et al. 2012; the Vaglio et al.
2026 update used indicatively) — and evaluated published
data products for applicability in two more (ARM 3:
cosmological constraint sets, none applicable as a bound;
ARM 7: GW-catalog polarisation analyses, not applicable).
ARM 2 used the published Fig. 7's own stated geometry.
Net data contact: the J1738 timing precision caps the
dipole leg at 0.067 (1σ) where the fence had spent 0.1.`
