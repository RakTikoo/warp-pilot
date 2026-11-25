# T9 memo — THE COUNTER-ROTATING PAIR — **SPECULATIVE**

Plain language first. Details and hedges after.

## The bottom line

**SPECULATIVE** — Phase 79 found that rotation's push on the
radial flux mostly cancels itself: the frame-dragging term and
the diagonal metric correction the spin forces are nearly equal
and opposite, leaving ≤2% alive. This item asked whether that
cancellation belongs to the shell's NET rotation. We built the
wall from two counter-rotating layers (spins +λ and −λ, zero net
angular momentum) and computed the second-order radial-flux
response directly, through the original machinery, at the two
binding sites.

**The theory's mechanism is confirmed at the deciding site.**
In the counter-rotating pose the two geometry channels do not
cancel the matter term — they are simply absent (both are
quadratic in the NET spin, which is zero), and the local matter
coupling survives whole: the two-layer coefficient at site 44
equals the single-layer matter coefficient to twelve digits.
Measured against the naive uncancelled single-layer coefficient,
the survival fraction at site 44 is **0.1406** (rigid profile;
0.3606 for the differential profile) — above the registered
0.10 success factor, and seventy times Phase 79's ≤2% survival
of the geometry pair. At validity-legal layer spins the site's
Type-I read is not worsened (subset count 52, unchanged).

**Site 41 lands the other way.** Its naive coefficient is
dominated by the frame-dragging channel (0.0617 of 0.0661), so
the surviving matter share there is only **0.0137** (rigid;
0.0379 differential) — inside the registered kill class
(≤ 0.04). The survival fraction is a site-local share, not a
property of the mechanism alone.

**And the relief is still priced out — by less.** Survival is
not relief: the spin at which the surviving matter term would
actually relieve site 44 is λ_needed = 0.145, against per-layer
validity bounds λ_metric = 0.0200 / λ_Kepler = 0.0281 — a
7.3× / 5.2× breach, improved from the single layer's 26× / 18×
but still outside the expansion. At the legal spin the relief
delivered is 1.9% of what site 44 needs. No site is relieved
inside validity, no configuration is exhibited, and nothing
here is a candidate.

## Verdict (registered language, CHECKPOINT97 §T9)

**SPECULATIVE — REGISTERED SUCCESS at site 44**: survival
0.1406 ≥ 0.10 at validity-legal layer spins (rigid pose; the
fraction is a coefficient ratio, read at the extraction spins
h = 0.02/0.01 at the validity edge), with the site's Type-I
read not worsened (direct finite-λ read at λ = 0.01999:
Type-I status unchanged at both binding sites, subset count
52 = base). **Site 41 is recorded on the face in the
registered KILL class**: survival 0.0137 ≤ 0.04 — at that site
the cancellation's removal buys almost nothing, because the
uncancelled coefficient there was never matter-carried. The
registered KILL for the item (survival stays ≤ 0.04) does not
fire, because it does not stay there: site 44 breaks it by
3.5×. The intermediate band (0.04–0.10) is landed in by
neither site in the rigid pose.

## 1. Grounding (named, measured)

Phase 79 P79-3 (memo + CHECKPOINT79 §P79-3, read in full):
rotation couples to radial flux at Ω²; decomposition at the
binding sites — ϖ² term +6.170×10⁻² / −8.120×10⁻³ (sites
41/44), ADM diagonal −6.170×10⁻² / +8.121×10⁻³, cancelling to
≤2%; totals −9.03×10⁻⁵ (site 44) / +4.43×10⁻³ (site 41);
λ_needed = 0.519 vs λ_metric = 0.0200 / λ_Kepler = 0.0281
(26×/18× breach); Type-I subset count falls 52 → 35 at that
spin. T9's theory: the canceller ran through the shell's net
frame-dragging field; counter-rotation removes the net field
while each layer keeps its local Ω² coupling.

## 2. Recovery — passed, before any two-layer number

With the original machinery (t9_solver.py, run of record;
results in t9_results.json):

- (R0) Phase-64 joint-best point: cost **129.25855456223337**,
  every stored read reproduced at absdiff **0.0** (as in
  P79-3's own gate).
- (R2) Single-layer Ω² reads: matter / ϖ² / both-linear
  coefficients at sites 41/44 reproduced **bit-exactly**
  (reldiff 0.0); the total (ADM + Ia) agreed with the stored
  −9.03×10⁻⁵ / +4.43×10⁻³ to ≤ 2.1×10⁻¹¹ relative. The stored
  ≤2% cancellation survival recomputed as 3.2×10⁻⁶ (site 41)
  and 1.9×10⁻⁴ (site 44) for the (ϖ² + diagonal) pair.
- Checker clauses C1–C2 verify all of the above from the
  stored files.

## 3. Two-layer construction

Stationary Hartle-order pose on the (10,30)-family bed of
P79-3 (Phase-64 joint-best point, β = 1.1 TEST / β = 0.1
CONTROL, 56 binding-subset points, sites 44 and 41 deciding).
Nothing in the construction is time-dependent, so
worst-instant auditing does not arise.

- **Two independent Proca species**, each carrying the base
  field A/√2 (coeff/√2), with m₂ and ξ unchanged and the
  quartic coupling doubled per species (λ_a = 2λ_). The sum
  of the two species' base stress tensors then equals the
  single-field base stress **exactly** — quadratic terms
  2·(1/2) = 1, quartic 2·(2λ_)·(1/4) = λ_, ξ terms (linear
  in A²) 2·(1/2) = 1. Construction gate, computed: relative
  max difference **8.45×10⁻¹⁶** (β = 1.1) and 2.43×10⁻¹⁵
  (β = 0.1). Total matter content is preserved; no factor of
  two is available to game the survival ratio.
- **Layer spins** λ₁ = +t, λ₂ = −t. Each species' azimuthal
  datum is its own profile-following δA (P76-2's datum,
  scaled by its 1/√2 share), rigid profile primary,
  differential profile as variant.
- **The metric responds only to the net spin** s = λ₁ + λ₂
  (one metric, one shift): ADM-complete pose at s, exactly as
  P79-3's completion. In the counter pose s = 0, so the
  metric is the base metric identically, and the Ia sector —
  evaluated on that metric — contributes zero intrinsic
  response.
- **Validity pricing (per layer, neither waived):** each
  layer's own spin is priced by P79-3's pattern on the
  two-layer bed — λ_metric from that layer's own diagonal
  correction reaching 10% (λ²ϖ²s²/|g_tt| = 0.10) and
  λ_Kepler from that layer's own surface speed against the
  bed mass M = 2.0. The net-based metric bound is vacuous in
  this pose (the net correction is identically zero) and is
  recorded as such; the deciding price is the per-layer one.

## 4. Decomposition anatomy (β = 1.1, ∂²T_0r̂/∂λ²)

| channel | site 41 | site 44 |
|---|---|---|
| (i) matter self-coupling, single layer (rigid) | +9.0286×10⁻⁴ | −1.1544×10⁻³ |
| (iii) ϖ² (net-spin²) | +6.1700×10⁻² | −8.1195×10⁻³ |
| (ii) ADM diagonal (net-spin²) | −6.1700×10⁻² | +8.1211×10⁻³ |
| cross (ϖ × δA) | +3.5268×10⁻³ | +1.0625×10⁻³ |
| (iv) Ia intrinsic | +4.7×10⁻⁹ | −3.1×10⁻⁸ |
| **single-layer total** | **+4.4299×10⁻³** | **−9.0343×10⁻⁵** |
| **two-layer counter-rotating total** | **+9.0286×10⁻⁴** | **−1.1544×10⁻³** |
| — of which species 1 only | +4.5143×10⁻⁴ | −5.7721×10⁻⁴ |
| — of which species 2 only | +4.5143×10⁻⁴ | −5.7721×10⁻⁴ |
| naive uncancelled (both-linear) | +6.6130×10⁻² | −8.2114×10⁻³ |
| **survival fraction (rigid)** | **0.013653** | **0.140589** |
| survival fraction (differential) | 0.037909 | 0.360558 |

The anatomy, stated plainly:

- In the counter pose the response is **exactly the matter
  channel**: the computed two-layer coefficient equals the
  single-layer matter coefficient to ~5×10⁻¹² relative at
  both sites (checker C4). Channels (ii), (iii) and the cross
  term are each proportional to powers of the net spin
  (s², s², s·λ_layer summed over layers) and vanish at s = 0
  — not by cancelling each other, but by having no net field
  to be built from. The cancellation of P79-3 is therefore,
  in this pose, a **net-rotation property**: the registered
  theory's mechanism is what the numbers do.
- Each species contributes exactly half the matter channel
  (checker C5): the stresses of independent layers add, and
  no inter-layer matter coupling appears at this order.
- **Bilinear path consistency (second path):** writing the
  response along a path (λ₁, λ₂) as M·(λ₁²+λ₂²)/2 +
  G·(λ₁+λ₂)² + X·(λ₁+λ₂)²/2 with M, G, X the single-layer
  matter / net-geometry / cross coefficients, the directly
  computed co-rotating path (t, t) and single-rotating-
  species path (t, 0) match the prediction at both sites
  (checker C6; worst deviation 1.8% on the smallest
  coefficient, site 44 single-rotating). The decomposition
  is a measured bilinear form, not a bookkeeping choice.
- **Why the sites split:** survival is the matter share of
  the naive coefficient. At site 44 the ϖ² channel is only
  ~7× the matter channel, so removing the net field leaves
  14%. At site 41 the ϖ² channel is ~68× the matter channel;
  removing it leaves 1.4%. Same mechanism, different local
  shares — the fraction is site-local, exactly as P79-3's
  β = 0.1 control already hinted for the single layer.

## 5. Validity reads and finite-λ Type-I

Per-layer bounds (two-layer bed): site 44 λ_metric =
**0.0200**, λ_Kepler = **0.0281**; site 41 λ_metric =
**0.0293**, λ_Kepler = **0.0436** — numerically P79-3's
bounds, now charged per layer.

Needed spins in the counter pose (from the surviving matter
coefficient and P79-3's R1 needed sizes):

| site | profile | λ_needed | vs λ_metric | vs λ_Kepler |
|---|---|---|---|---|
| 44 | rigid | 0.1452 | 7.26× breach | 5.17× breach |
| 44 | diff | 0.0830 | 4.15× breach | 2.96× breach |
| 41 | rigid | 0.0876 | 2.99× breach | 2.01× breach |
| 41 | diff | 0.0509 | 1.74× breach | 1.17× breach |

Direct finite-λ reads in the counter pose (ADM-net = base
metric; Ia on base metric):

- At **λ = 0.01999** (site 44's metric bound, legal at both
  sites): q_r = 1.1030 (site 44, from 1.1116) and 1.0033
  (site 41); **Type-I improves at neither site and worsens
  at neither** — both remain non-Type-I exactly as at base,
  subset count **52 = base** (checker C9). The registered
  success clause "Type-I not worsened" is met by direct
  read, and the relief actually delivered at the legal spin
  is Δ|T_0r̂| ≈ 2.3×10⁻⁷ at site 44 — **1.9% of the needed
  1.218×10⁻⁵**.
- At **λ = 0.1452** (the rigid λ_needed, 7.3× outside
  validity — an extrapolated read, reported as P79-3
  reported its own): q_r(44) = 0.762 and site 44's Type-I
  read **does** flip to Type-I, subset count 53; site 41
  reaches q_r = 0.980 but stays non-Type-I (its failure is
  not carried by the radial component alone — P79-3's R1
  caveat, again). Unlike the single layer at its needed
  spin (count fell 52 → 35), the counter pose at its needed
  spin does not degrade the subset. This read is outside
  the expansion that defines it and decides nothing; it is
  the shape the follow-up below must test honestly.

## 6. β = 0.1 CONTROL

In P79-3's control convention (same point on the β = 0.1
bed): the counter-rotating coefficient at sites 41/44 is
−2.35×10⁻⁵ / +2.68×10⁻⁵ — **signs opposite to β = 1.1 at
both sites** — against naive coefficients −0.258 / −0.348,
giving survival fractions **+9.1×10⁻⁵ / −7.7×10⁻⁵**,
i.e. zero. The β = 1.1 survival is a property of the
β = 1.1 pose, not a β-stable scaling law — the same
conclusion P79-3's own control reached for the single-layer
coefficient (sign agreement 25/56). The deciding TEST cell
(β = 1.1) is unaffected; the control is recorded as a
scope limit on any generalisation.

## 7. Failure protocol — anatomy and follow-ups

Anatomy. (a) The item's registered success and its
practical limit are both real, and they are different
statements: counter-rotation provably removes the geometry
cancellation (the canceller is net-spin-built in this pose),
but what survives is the matter channel, whose own size —
not the cancellation — is now the binding constraint
(λ_needed still 7.3× outside validity at site 44, rigid).
(b) The survival fraction is a share, and shares are
site-local: site 41's naive coefficient was geometry-
carried, so the same mechanism scores 0.0137 there. Any
future use of "survival" must name its site and its naive
denominator. (c) The β = 0.1 control shows the matter
channel itself flips sign between poses; nothing here is a
scaling law.

Follow-ups (mechanism-suggested):
1. **FU-T9-1 (the other counter-rotating pose — radially
   separated layers):** layers in disjoint radial bands,
   zero *integrated* angular momentum but nonzero local
   dragging in each band. This decides whether "net" in
   the confirmed mechanism means pointwise-net (this
   item's pose) or only globally net. Prediction on this
   item's anatomy: in a band, the local δβ is nonzero, its
   ADM diagonal returns, and survival falls back to the
   ≤2% class — if so, the mechanism is pointwise and the
   co-located two-stream pose is the only form that
   survives. Not run.
2. **FU-T9-2 (finite-rotation two-layer pose):** the
   extrapolated read at λ = 0.145 flipped site 44's
   Type-I without degrading the subset — the opposite of
   the single layer's behaviour at its needed spin. A
   non-Hartle, self-consistent two-stream construction at
   that spin (the FU-P793-1 rapid-rotation form, now with
   a specific target spin 3.6× lower than the single
   layer's) is the mechanism-matched test of whether that
   flip is real. Not run; registered here as the
   reopening for the relief question, which this item
   leaves priced out at Hartle order.
3. **FU-T9-3 (β-stability of the matter channel):** the
   control's sign flip bounds every claim above to the
   β = 1.1 pose. A β-scan of the counter-rotating
   coefficient's sign/magnitude between 0.1 and 1.1 would
   locate where the channel stabilises and whether the
   site-44 share survives the scan. Not run.

## 8. Run record / deviations

- Scripts: `phase97/work/t9_solver.py` (recovery + first
  full run), `phase97/work/t9_rebuild.py` (rebuild, below),
  checker `phase97/results/t9_checker.py` (**30/30 PASS**,
  output in `t9_check.json`). float64 throughout; venv
  python.
- Deviation, on the record: t9_solver.py completed every
  β = 1.1 read, then crashed at its final save (a per-point
  error array in the β = 0.1 block was not JSON-serialisable)
  and truncated t9_results.json mid-write. t9_rebuild.py
  re-ran all two-layer paths and the β = 0.1 control with
  atomic saves; every re-run site value agrees with the
  first run's logged values (checker C10, ≤1e-7 relative —
  in fact identical to all printed digits). No number in
  this memo comes from the truncated file.
- One bookkeeping note: the solver's single-layer "total"
  field double-added the Ia channel (≤3.1×10⁻⁸, immaterial);
  the results file's decomposition uses the corrected
  total (ADM + Ia once), which is what checker C2 verifies
  against the stored Phase-79 total.

## 9. C12 accounting

All configurations here are pre-existing walls — no
formation mechanism is computed and **no transport claim
is made or implied** by any verdict in this item. β is a
velocity tested directly at β ∈ {0.1, 1.1}; crossing is
never modelled.

## Files

- `results/t9_memo.md` — this memo (**SPECULATIVE**)
- `results/t9_results.json` — base, recovery, single-layer
  decomposition, two-layer paths (full 56-point arrays),
  survival, validity, finite-λ reads, β = 0.1 control
- `results/t9_checker.py` + `results/t9_check.json` —
  independent checker, 30/30 PASS
- `work/t9_solver.py`, `work/t9_rebuild.py`,
  `work/t9_solver.log`, `work/t9_rebuild.log`

Internal only. Nothing here is a candidate; the signal bar
is not met; language stays at the registered forms.
**SPECULATIVE** label carried in every verdict line, as
registered.
