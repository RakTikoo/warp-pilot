# P270-1 — THE c_trim UNCERTAINTY ESTIMATE — memo

Phase 270, 2026-11-24. Registration (written BEFORE any
deciding computation of this phase):
`phase270/work/p270_registration.md`. Driver:
`phase270/work/p270_run.py`; numbers:
`phase270/results/p270_results.json`. Independent checker:
`phase270/work/p270_check.py` → `phase270/results/
p270_verify.json` — **PASS 39/39**, including a full
independent recomputation of all 60 refits (max abs diff
0.0 against the driver's table) and of every leg's headline
numbers; zero discrepancies. Frame of record: Phase 166
pin, Gate-19-corrected tensor, venv python, float64.
Stored-row arithmetic only — no march was re-run, no engine
imported; the four source files are md5-identical before
and after (checker-verified). INTERNAL only; no ledger
append, no launches, nobody contacted; nothing outside
`phase270/` edited.

## Verdict (registered form 2, verbatim in substance)

**THE GAP BITES** — the total defensible uncertainty on
c_trim = **+5.253378225339471** is

  **c_trim ∈ [4.094974, 5.693832],
  δc_trim ∈ [−1.158404, +0.440454]**

(cross-product of Leg 2's refit range with Leg 3 Tier 1's
divisor range; Leg 1 excluded under its registered rule,
§1), against Gate-27's stability band δc_trim ∈
[−0.11264, +0.10352]. The total exits the band on BOTH
sides — the lo side by 1.045764, the hi side by 0.336934.
Defensible refits of Phase 248 Part A's own procedure move
c_trim by up to −22% / +8.4%: **the fit's own parameter
uncertainty is an order of magnitude larger than the
±~2% band Gate-27 priced.** The exiting leg is Leg 2
(window/weighting variation of the fit); Leg 3's Tier-1
divisor summaries stay inside the band alone
(δ ∈ [−0.028056, +0.036207]). Only **5 of the 60**
defensible refits land inside the band at all, and all
five sit in the maximal-window corner (end 0.475, or end
0.45 with the start dropped): the stored coefficient is
the product of the single most aggressive window choice
in the defensible set — the full holding interval with
the posed t = 0 point included.

**What this does and does not touch.** Phase 266's
certificate certifies the pose AS POSED, with the stored
coefficient, fixed in advance of every march it governed
and never adjusted against any bracket (Gate-26 §4(3b),
Gate-27 §2) — that certificate is untouched, and nothing
here re-opens it, Phase 248's verdict, or any Gate-27
verdict. What changes is the status of G27-A's fence (i):
its open clause — "the fit's own parameter uncertainty
under window/weighting variation is not on record" — is
now answered, and the answer is that the uncertainty is
large. The fence therefore needs rewording by a successor
gate (§5): the fit uncertainty carried as a LIVE caveat
with the interval quoted, not as an unpriced gap.

**The bracket's robust interval under the uncertainty**
(Gate-27's linearised response, ≈ 0.0289 of t per unit
δc_trim about the linearised crossing
t* = 0.6782280511877113; locality caveat: the slope is a
read-grade local price at the certified point, and the
lo end of the δ range extrapolates it well past its
neighbourhood — the interval below is the record's own
pricing instrument applied to the measured uncertainty,
not a re-computed bracket): the crossing ranges over

  **t* ∈ [0.644750, 0.690957]**.

Orderings under the FULL defensible range:
- **Past the wound bracket (0.55625, 0.5625]: SURVIVES** —
  the lowest defensible crossing (0.644750) clears the
  wound hi end by 0.082250. The lead change over the
  wound pose is robust to any defensible refit.
- **Past the clamped bracket (0.65625, 0.6625]: DOES
  NOT SURVIVE as an ordering** — the crossing range
  straddles the clamped bracket (it begins 0.011500
  below its lo end and ends 0.028457 above its hi end).
  Under the shallowest defensible refits the unclamped
  pose's crossing falls INSIDE the clamped bracket;
  the statement "the stop-free bracket lies entirely
  past the clamped certificate" is a property of the
  stored coefficient, not of the fit.
- The certified bracket (0.675, 0.68125] as an interval
  is, as Gate-27 already priced, a statement about the
  stored coefficient: under the defensible range the
  crossing moves by up to −0.033478 / +0.012729 around
  t*, several bracket widths on the lo side.

## 1. Controls (all PASS, checker-verified)

- **CTRL-1** — OLS full quadratic on the 20 stored fit
  points (t = 0, 0.025, …, 0.475; composed NEC_φ,min from
  `p2481_results.json`) reproduces Phase 248's stored
  c₀ = 1.1919676197461249, c₁ = 0.6519585941496637,
  c₂ = −6.062834985645177, RMS 0.01717075411474814,
  max |resid| 0.04063136073121337 — diffs 0.0.
- **CTRL-2** — the same trajectory from
  `p2462_results.json` agrees at max abs diff 0.0 over
  [0, 0.5] (21 instants).
- **CTRL-3** — s̄ = 1.1540830919809508 and
  c_trim = 5.253378225339471 reproduced at ≤ 1×10⁻¹².

## 2. Leg 1 — the formal standard error, and what it means

Baseline fit (n = 20, k = 3): σ̂ = 0.01862429775601944;
**SE(q₂) = 0.22489878172866737** (3.71% of |q₂|);
SE(c_trim) = SE(q₂)/s̄ = **0.1948722611841016** (3.71% of
c_trim). (SE(c₀) = 0.011341, SE(c₁) = 0.110664.)

**Residual structure: SYSTEMATIC** — declared under the
registration's pre-fixed rule by both triggers: sign runs
= **4** (≤ n/3 = 6.67) and Durbin–Watson = **0.348108**
(< 1.0). The residual sign pattern is
`+++--------+++++++--` (10 positive / 10 negative), a
smooth arch: first-half mean −0.005456, second-half mean
+0.005456, max |resid| 0.040631 at the last point
(t = 0.475).

**The repricing, in words (as the registration required).**
These residuals are not measurement noise and were never
going to be: the fitted trajectory is a deterministic
march output — the same numbers reproduce bit-exactly
from two independently stored march records (CTRL-2) —
so there is no sampling distribution for the formal SE
to be the standard error OF. The residuals are the
quadratic model's deterministic misfit to a smooth curve
whose true shape carries higher-order content (the
composed curve is a forced t² drift plus a t²-eroding
lift, each only approximately quadratic — Phase 248 §§1–2).
The number 0.2249 therefore means exactly this: *the
scale at which this window's quadratic misfit projects
onto the c₂ axis* — a misfit-scale diagnostic for the
registered window, useful as a lower-scale reference for
how well ANY quadratic reads this curve, and nothing
more. Per the registered rule it does **not** enter the
total of §4; the movement a refit actually produces is
measured directly by Leg 2. For the record: the verdict
does not hinge on this exclusion — the ±1 SE band alone,
[5.058506, 5.448250] (δ ∈ [−0.194872, +0.194872]), already
exits Gate-27's band on both sides. Form 2 fires with or
without Leg 1 in the total.

## 3. Leg 2 — the variation spread (60 defensible refits)

Distribution of the implied c_trim (registered divisor)
over the 60 registered refits (15 lattice windows inside
the holding interval × full/half subsetting × OLS/Huber;
the registered baseline is one of them):

  min 4.116961 · q1 4.504021 · median 4.799039 ·
  q3 5.075319 · max 5.654858

(c₂: min −6.526176, median −5.538490, max −4.751316.)
Extremes: min at window [0, 0.375], half-lattice, OLS
(n = 8); max at window [0.05, 0.475], full lattice, OLS
(n = 18). Marginal anatomy (c_trim ranges):

- **Window END is the driver.** end 0.375 → [4.117,
  4.545]; 0.40 → [4.404, 4.799]; 0.425 → [4.504, 5.034];
  0.45 → [4.874, 5.361]; 0.475 → [5.000, 5.655]. The
  ranges by end barely overlap their neighbours': the
  composed curve steepens late (the drift accelerates
  into the crossing), so every instant of holding
  interval an analyst trims off the end shallows the
  fitted t² term materially. At the registered start/
  subsetting/weighting, the ends price as: 0.475 →
  5.253378 (baseline), 0.45 → 4.962715 (−5.53%),
  0.425 → 4.705721 (−10.42%), 0.40 → 4.478378 (−14.75%),
  0.375 → 4.277251 (−18.58%). Even the mildest end-trim
  (one instant, to 0.45) exits the band by ~3.5 points.
- **Window START is secondary and one-sided:** dropping
  the posed t = 0 point (and 0.025) removes the curve's
  high, flat early anchor and steepens the fit — at end
  0.475, start 0.025 → +3.65%, start 0.05 → +7.64%
  (OLS/full). This axis alone also exits the band, on
  the hi side.
- **Subsetting and weighting are minor:** half-lattice
  and Huber members sit inside the same ranges as their
  full/OLS counterparts (Huber max 5.558 vs OLS 5.655);
  neither axis rescues or drives the verdict.

Diagnostics (registered exclusions, priced, NOT in the
distribution): the cubic refit of the baseline window
gives c₂ = −0.922518 with c₃ = −7.214480 (implied c_trim
0.799351) — the quadratic coefficient is not order-stable
either, but cubic is outside Phase 248 A2's registered
fit class, so it is reported here as a diagnostic of the
model class, not a refit of the estimand. The forced-t²
form's c₂ = −4.783824837081042 (refit reproduces the
stored value exactly; implied c_trim 4.145130) is a
different parameter — the total t²-mode amplitude with
the linear part absorbed; Phase 248 B1 designated the
FULL form's c₂ as q₂. End 0.5 was not run: t = 0.5 is
the first FAILED instant, outside the holding interval
the registered procedure fits.

## 4. Leg 3 — the divisor's provenance

The three constituent sensitivities are numerically
exact for what they are: FD-step cross-check (δ = 3×10⁻⁶
vs stored δ = 1×10⁻⁶) agrees to ≤ 1.85×10⁻¹⁰, and the
finite-amplitude delivery at t = 0.475 (measured lift at
a = −0.5) agrees with the linear prediction a·s to
2.09×10⁻¹² absolute (3.78×10⁻¹² relative). No numerical
spread exists to price.

- **Tier 1 (defensible summaries; in the total):**
  (a) arithmetic mean (registered) 1.1540830919809508 →
  c_trim 5.253378; (b) median 1.1461834865666987 →
  5.289585; (c) trapezoidal time-average over
  [0.25, 0.475] 1.1602797411747192 → 5.225322.
  Tier-1 range [5.225322, 5.289585], δ ∈ [−0.028056,
  +0.036207] — inside Gate-27's band alone. The
  divisor's SUMMARY choice is not the problem.
- **Tier 2 (constituent range; descriptive, excluded
  from the total per the registration — a single-instant
  divisor is a different design, not a summary of the
  design-era slope):** t = 0.25 → 5.022802 (−4.39%);
  t = 0.4 → 5.289585; t = 0.475 → 5.466921 (+4.07%).
  Even the constituents individually straddle the band —
  priced here so the record shows it.
- **Tier 3 (provenance observations; priced, not in the
  total):** (i) the samples trend at −0.431536 per unit t
  (intercept 1.315909): s̄ is an average of a DRIFTING
  slope over the design era [0.25, 0.475], not a constant
  of the channel. (ii) Era edges: no sensitivity was
  ever measured below t = 0.25; the samples' linear
  extension averaged over [0, 0.475] gives 1.213419 →
  c_trim 4.996488 (−4.89%). (iii) The θ-profile-median
  alternative (per-instant medians 1.238515 / 1.221030 /
  1.209549, mean 1.223031 → c_trim 4.957220, −5.64%) is
  a different quantity — θ-averaged delivery, where the
  trim acts at the binding argmin — priced, not counted.
  (iv) The late-era reads (Phase 265, verified by the
  checker in Gate-27's own verify file:
  1.009839 / 1.006338 / 0.999345 at t = 0.65625 /
  0.6625 / 0.675) continue the same decline; a divisor
  designed at the bracket era would be ≈ 1.0 → c_trim
  ≈ 6.03 (+15%). Not available to Phase 248 and not the
  registered quantity — stated as the regime bound on
  what s̄ means: **s̄ is a design-era number, and the
  era choice is worth more than every summary choice
  inside it.**

## 5. Total, and the fence rewording form 2 requires

Total (registered combination rule; no quadrature — the
legs are not independent noise sources): cross-product
of Leg 2's range [4.116961, 5.654858] with Tier 1's
divisor range ⇒ **c_trim ∈ [4.094974, 5.693832]**,
δc_trim ∈ **[−1.158404, +0.440454]**. Leg 2 exits the
band on both sides by itself; the cross-product widens
the exits to 1.045764 (lo) and 0.336934 (hi).

**Rewording G27-A's fence (i) needs (for a successor
gate to issue):** the clause "the fit's own parameter
uncertainty under window/weighting variation is not on
record and no wording may imply the bracket is robust
to a refit beyond the priced band" is superseded by a
live caveat of the form: *the coefficient is a fitted
pose parameter (provenance as stated); its defensible-
refit uncertainty, measured in Phase 270 over the
registered variation set, is δc_trim ∈ [−1.158, +0.440]
(c_trim ∈ [4.095, 5.694]) — an order of magnitude wider
than the bracket's priced stability band
[−0.11264, +0.10352] — under which the crossing ranges
over [0.6448, 0.6910] (linearised price, locality
caveat); the lead change over the wound pose's
certified bracket survives the full range, and the
ordering past this pose's own clamped certificate does
not. The certified bracket (0.675, 0.68125] remains a
statement about the pose with the stored coefficient.*

## 6. Scope fences

Stored-row arithmetic only; no march re-run, no engine
imported, no bracket computed or certified here — the
robust interval of the verdict is Gate-27's linearised
response applied to the measured uncertainty, with its
locality caveat on the face. This phase prices the one
gap Gate-27 left in G27-A's fence (i); it does not
re-open Phase 248's verdict (the trim law and its
coefficient formula were fixed in advance there, and
the coefficient was never adjusted against any bracket
— the uncertainty priced here is the counterfactual
spread of that fixed procedure under its own defensible
variations, not evidence of tuning). The defensible set
is the registration's: variations a reasonable analyst
could have chosen in Phase 248's place, each with its
defence stated in advance; the cubic and forced-t²
numbers are diagnostics of the model class, excluded
from the total with their reasons on the face (§3).
Datum ≠ construction; jet scope; programme-level
sustainment wording remains gated by p1592 regardless.

## Files

- `phase270/work/p270_registration.md` — registration
  (controls, legs, registered grids, interpretation and
  combination rules, verdict forms), written before
  computation.
- `phase270/work/p270_run.py` — driver.
- `phase270/results/p270_results.json` — full record:
  md5s, controls, Leg 1 (full residual vector, SEs,
  diagnostics, declaration), Leg 2 (all 60 refits,
  distributions, labelled diagnostics), Leg 3 (all
  tiers), total, verdict.
- `phase270/work/p270_check.py` +
  `phase270/results/p270_verify.json` — independent
  checker, PASS 39/39.
- `phase270/results/p2701_memo.md` — this memo.
- `phase270/CHECKPOINT270.md` — checkpoint.
