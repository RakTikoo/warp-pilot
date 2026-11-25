# PHASE 307 — ARM 2 MEMO: THE BANDS AS DRAWN (red team)

Scope (registered): each tested point — the three
floor-binding flat maximisers and Corner B — against
YBBY Fig. 7 (PRD 89, 084067 (2014), arXiv:1311.7144v4).
Sources retrieved 2026-11-24: YBBY full text (ar5iv HTML
and arXiv PDF), §VII C.1 and the Fig. 7 caption in full;
Fig. 1's combined-region discussion (§VII C.1 and the
Executive Summary). **Retrieval limit, on the face of
this memo:** the Fig. 7 raster/vector itself could not be
extracted through this arm's text-fetch tools (the PDF
and HTML text layers carry the caption and discussion
but no axis tick data or band coordinates, and no image
file was obtainable). The digitisation below is
therefore **text-grade**: it uses YBBY's own published
quantitative characterisation of the drawn bands — their
widths and the combined region's shape and extents,
stated in §VII C.1 — as the digitised boundary data.
The read-off error this induces is stated in §3 and
carried through every per-point verdict; points whose
test falls inside that error are scored UNRESOLVED, not
forced.

## 1. What Fig. 7 actually shows (established first)

From the caption and §VII C.1, verbatim in substance:

- **Axes / plane:** every panel is the Einstein-aether
  **(c₊, c₋) plane**. There is no third axis and no
  per-panel slice in (c₁, c₂, c₁₄): after Solar-System
  constraints the theory is presented as depending on
  (c₊, c₋) up to O(10⁻⁴) corrections, and the remaining
  freedom is **varied, not held fixed** — Eq. (191) and
  Eqs. (194)–(195) are evaluated "allowing for the
  inferred error in the masses, the observational error
  in the orbital decay rate, the allowed range on
  (α₁^Æ, α₂^Æ) given Solar System constraints, and
  various NS sensitivities associated with different
  EoSs." The drawn band at a given (c₊, c₋) is therefore
  an **existential projection**: the point is shaded if
  *some* allowed choice of (α₁, α₂, masses, P_b, EoS)
  makes the constraint pass. It is not a statement that
  every theory point projecting to (c₊, c₋) passes.
- **Panels:** top-left J1141−6545, top-right
  J0348+0432, bottom-left J0737−3039 — all three are
  **orbital-decay (Ṗ_b, Eq. 191) constraints from other
  systems**; bottom-right is J1738+0333, but through the
  **conservative α̂₁/α̂₂ mapping (Eqs. 194–195), not
  through J1738's Ṗ_b**, which YBBY explicitly do not
  use ("weaker"). No panel of Fig. 7 is a J1738 Ṗ_b band.
  Also drawn in each panel: the Cherenkov/stability
  allowed side of the solid black line, and the dashed
  zero-sensitivity ("weak-field") GR-agreement curve.
- **Logical consequence for testing fence points.** A
  fence point (c₁, c₂, c₁₄) on the c₁₃ = 0 slice
  projects to exactly one plane point, (c₊, c₋) =
  (0, 2c₁). Two cases:
  (a) the projection lies **outside** a drawn band ⇒ the
  fence point is excluded by that system's constraint
  for *every* choice of the varied parameters — a clean
  break at projection scope;
  (b) the projection lies **inside** a band ⇒ only that
  *some* (α₁, α₂, EoS, …) choice passes there. The fence
  point's own (α₁, α₂) are fixed by its (c₂, c₁₄)
  (α₁ = −4c₁₄; α₂(c₂, c₁₄)) and its σ is the fence's
  rung-2 anchor value, not YBBY's numerically varied
  sensitivities — so inside-the-band can never be more
  than the registered **weak-form HOLD**.

## 2. The points in the plane

| Point | (c₁, c₂, c₁₄) | (c₊, c₋) in Fig. 7 |
|---|---|---|
| Maximiser c_V = 1 | (2.6568×10⁻⁶, 2.6676×10⁻⁶, 2.6568×10⁻⁶) | (0, 5.314×10⁻⁶) |
| Maximiser c_V = 2 | (2.5443×10⁻⁵, 6.3620×10⁻⁶, 6.3608×10⁻⁶) | (0, 5.089×10⁻⁵) |
| Maximiser c_V = 10 | (7.9511×10⁻⁴, 7.9621×10⁻⁶, 7.9511×10⁻⁶) | (0, 1.590×10⁻³) |
| Corner B | (0.08293104, 2/21, 7.9×10⁻⁹) | (0, 0.16586208) |

All four sit on the plane's left edge, c₊ = 0 — inside
the figure's plotted domain (the bands and the combined
region are drawn across the (c₊, c₋) plane from the
origin outward; the GR point (0,0) is in every band, as
it must be, since c_i → 0 is GR and passes every Ṗ_b and
α̂ constraint exactly). No point is outside the bands'
*coverage*; the test is band membership at c₊ = 0. (The
fits' region, c₋ ∈ 3×(10⁻⁵, 10⁻³), c₊ ∈ 3×(10⁻⁴, 10⁻¹)
at fixed α₁^Æ = 10⁻⁴, α₂^Æ = 4×10⁻⁷, is the region of
the Eq. (186)/App. C sensitivity *fits* — a different
object from the Fig. 7 bands, whose sensitivities were
computed numerically point-by-point. Phase 303 §4(ii)'s
statement that the bands "were computed inside the fits'
region" is, on the retrieved text, not what YBBY say
about Fig. 7; the bands are drawn across the full plane.
This memo tests the bands as drawn, per the charge, and
flags the Phase 303 framing as inaccurate in passing.)

## 3. Text-grade digitisation of the drawn boundaries

YBBY's own numbers for the bands as drawn (§VII C.1):

- "For any given system, we find that the allowed region
  is not a box with sides of O(10⁻²) but rather **a band
  with width O(10⁻³)**."
- "When we combine all of these allowed regions in the
  left panel of Fig. 1, **their intersection is indeed
  almost a box with width of O(10⁻³) in the c₋ direction
  and O(10⁻²) in the c₊ direction**. The width of the box
  is determined by the smallest width of the bands,
  which is of O(10⁻³)."
- The allowed-region width per system is "between
  O(0.1%) and O(1%)" (relative width of the band region,
  same passage).

Digitised boundary statement used for the tests: the
**combined** drawn allowed region (intersection of the
Fig. 7 bands with each other and with the
Cherenkov/stability/BBN regions, Fig. 1 left) is a
single almost-box containing the origin, of total
extent Δc₋ = O(10⁻³) and Δc₊ = O(10⁻²). Since the box
contains (0,0) and its total c₋ extent is O(10⁻³), its
c₋ interval at c₊ = 0 is contained in [0, few×10⁻³].
**Read-off error:** the O(·) characterisation carries a
factor of a few; this arm adopts ±3×10⁻³ in c₋ (i.e.
treats the box's c₋ edge as lying anywhere in
[10⁻³, 3×10⁻³] with the nominal value 10⁻³) and
±10⁻² in c₊ (immaterial here — all points are at
c₊ = 0, the box's own edge). Any point with
c₋ > 3×10⁻³ is outside the combined drawn region by
more than this error; any point with c₋ ≪ 10⁻³ is
inside it; a point with c₋ within [10⁻³, 3×10⁻³] is
inside the error bar and cannot be decided text-grade.

Caveat recorded, not hidden: this tests the **combined**
region. A point outside the combined region is outside
at least one individual drawn band (that is what
intersection means), which is sufficient for a break at
that point's scope under §1(a). The text does not state
which single panel excludes it, and this arm does not
invent one.

## 4. Per-point tests

- **Maximiser c_V = 1 — (0, 5.314×10⁻⁶): INSIDE.**
  c₋ = 5.3×10⁻⁶ is ~200× below the combined box's
  nominal c₋ extent (10⁻³) and ~600× below the adopted
  error ceiling (3×10⁻³). Inside every band that
  contains the origin with O(10⁻³) width.
  **HOLDS (weak form)** — per §1(b), inside-the-band is
  an existential projection over (α₁, α₂, EoS, masses)
  that YBBY varied; it does not certify this point's own
  fixed (α₁, α₂, σ). Wording: the bands as drawn do not
  exclude this point.
- **Maximiser c_V = 2 — (0, 5.089×10⁻⁵): INSIDE.**
  c₋ = 5.1×10⁻⁵, ~20× below nominal extent, ~60× below
  the error ceiling. **HOLDS (weak form)**, same wording.
- **Maximiser c_V = 10 — (0, 1.590×10⁻³):
  UNRESOLVED.** c₋ = 1.59×10⁻³ exceeds the nominal
  combined-box c₋ extent (O(10⁻³)) by 0.59×10⁻³, but
  lies inside the adopted text-grade read-off error
  (edge anywhere in [10⁻³, 3×10⁻³]). The bands as drawn
  may or may not contain this point; deciding it needs
  the figure raster/vector at pixel grade, which this
  arm could not obtain (§0 retrieval limit). Not forced
  in either direction.
- **Corner B — (0, 0.16586208): OUTSIDE, by ≫ error.**
  c₋ = 0.1659 exceeds the nominal combined c₋ extent by
  a factor of ~166, and the adopted error ceiling
  (3×10⁻³) by a factor of ~55; the margin in plane
  coordinates is 0.163 in c₋, against a digitisation
  error of ±0.003. No reading of "width O(10⁻³)" —
  YBBY's own characterisation of their own figure —
  reaches 0.166. Corner B's projection lies outside the
  combined drawn allowed region, hence outside at
  least one Fig. 7 band, hence (§1(a)) excluded by that
  system's YBBY constraint for every value of the
  parameters YBBY varied. **BREAKS at Corner B's
  scope.**

## 5. What this does and does not touch

Corner B's fence survival (G32-E) rests on the
programme's own legs — BBN saturation and the
isolated-pulsar α̂₂ leg L8 at the fence's rung-2 σ —
applied through the fence's Eqs. (194)–(195) mechanism.
YBBY's drawn bands are an *independent, published*
evaluation of overlapping constraints (three other
systems' Ṗ_b plus J1738's α̂ via Eqs. 194–195 with
numerically computed sensitivities, varied α's and
EoSs), and at (c₊, c₋) = (0, 0.166) they allow nothing.
The break is at projection scope: it shows Corner B is
not merely un-cross-checked against the literature's
bands (Phase 303 §4(ii) recorded them as
"recorded-not-applied… consistent with, but not, this
phase's fence" — that consistency claim does not
survive for Corner B), it is *contradicted* by them.
It does not by itself identify which fence leg's
rung-2 modelling (σ anchor at c₋ = 0.166, the α̂₂
mapping, or the BBN saturation reading) is responsible
for the discrepancy; that diagnosis is the parent's
successor work, not this arm's. The flat maximisers at
c_V = 1, 2 are untouched by this arm (weak hold), the
c_V = 10 maximiser is unresolved at text grade, and
the flat *value* (G32-F) is not decided by this arm —
its deciding leg is Arm 1's.

## 6. Verdict — ARM 2: BREAKS (scope: Corner B)

Per point: c_V = 1 maximiser **HOLDS (weak form — bands
computed as an existential projection over varied
(α₁, α₂, EoS, masses); the point's projection lies
inside the combined drawn region)**; c_V = 2 maximiser
**HOLDS (weak form, same wording)**; c_V = 10 maximiser
**UNRESOLVED** (c₋ = 1.590×10⁻³ vs the combined box's
nominal O(10⁻³) c₋ extent — inside the ±3×10⁻³
text-grade digitisation error; pixel-grade figure data
is the exact gap); Corner B **BREAKS** (projection
(0, 0.16586208) outside YBBY's combined drawn allowed
region by 0.163 in c₋, ~55× the digitisation error).
Overall arm verdict per the registration (any point
BREAKS ⇒ arm BREAKS, scope named): **BREAKS at Corner
B's scope (G32-E)**.

Retrieval limits: YBBY full text, caption and §VII C.1
retrieved at primary grade; the Fig. 7 image itself
(raster or vector) was not extractable through this
arm's tools, so band boundaries are digitised from
YBBY's published width/extent statements with the
error stated in §3 — sufficient to decide three of
four points, insufficient for the c_V = 10 maximiser,
which is scored UNRESOLVED rather than forced.
