# PHASE 379 MEMO — THE HARVESTED CENTRE

**FTL verdict: STATIONARY LEVEL IMPROVES AT THE
HARVESTED CENTRE — at both harvested centres. New
best stationary level on the A2 lineage:
−1.942246×10⁻⁴ (SET-244, band pose [10, 20]), at
the μ = 1.15 centre. Still negative — the pressure
wall moved again; it did not break. No energy-
condition pass, no member, no gate referral.**

## What was done

Phase 374 proved the dwelling pose's ceiling is
its centre's stationary profile: the champion's
worst instant is a momentarily stationary bottom
configuration, L_worst = L_stat(1.1125) =
−2.099385×10⁻⁴. This phase harvested the two
bottom configurations (μ = 1.1125 and μ = 1.15 on
the A2 lineage, built by scaling A2's confirmed
total profiles exactly as 374's modulation scales
them) as new stationary centres and re-ran the
stationary joint (S, N, M) search around each —
344's machinery and objective, band [10, 20],
K = 9/17 economy. Registration filed before
computation (`work/p379_registration.md`).

## Controls

All pass on the VM at diff 0.0 (`results/
p379_controls.json`): the A2 anchor reproduces
344's stored confirmation exactly; centre H1's
zero-displacement read reproduces 374's bottom
identity (NEC −2.099385079591706×10⁻⁴, DEC
−1.9410812223900952×10⁻⁴); centre H2's reproduces
the μ = 1.15 identity (NEC
−2.03181133812098×10⁻⁴, DEC
−1.8546990569430298×10⁻⁴). Frame admission: the
laptop is NOT admitted (SET statistics differ at
10⁻⁶–10⁻⁸; pointwise values agree to ~10⁻¹⁹ — the
lineage pattern); all deciding reads are VM reads.

Disclosed machinery defect: the first control run
failed the A2 anchor's polished depth only
(9.94×10⁻⁶) — a transcription bug in the new
polish code (cos(φ) for cos(θ)); the SET path was
unaffected, both identity controls passed
throughout, the fix preceded any search step, and
the re-run passes at diff 0.0.

## Result (confirmation grade, diff 0.0)

Both ladders completed (481 counted evals per
centre; caps did not bind; zero floor rejections).

- **H1 (μ = 1.1125):** joint level
  −2.0146052429091614×10⁻⁴ (NEC-bound, NEC at
  r = 17.683; DEC −1.964171×10⁻⁴; ρ_min
  +8.750851×10⁻⁵). Margin over its centre bar:
  +8.478×10⁻⁶. Polished depth −1.669779×10⁻⁴;
  exact worst-null at the NEC argmin
  −2.023419×10⁻⁴ (still above the bar).
- **H2 (μ = 1.15):** joint level
  **−1.9422459891767227×10⁻⁴** (NEC-bound, NEC at
  r = 16.220; DEC −1.898259×10⁻⁴; ρ_min
  +8.789654×10⁻⁵). Margins: +8.957×10⁻⁶ over its
  centre bar, **+1.571×10⁻⁵ over the dwelling
  ceiling L_ceil**. Polished depth
  −1.440243×10⁻⁴; exact worst-null
  −1.943288×10⁻⁴ (still above L_ceil by
  +1.561×10⁻⁵).

Anatomy at H2: clamping the correction splines'
end knots to zero costs 1.45×10⁻⁵ (clamped level
−2.087299×10⁻⁴) — part of the gain uses the S
correction's freedom at the band's outer edge
(end value −7.927×10⁻³), the same freedom 344's
searches carried, and exactly where the band
pose's caveat applies.

## Reading

The dwelling ceiling was the A2 centre's ceiling,
not the family's. The dwelling pose found the μ
direction; harvesting its bottom points and
searching stationarily around them converts the
gain into a stationary level that beats the best
dwelling worst instant by +1.571×10⁻⁵,
like-for-like. The obvious next iteration — a
dwelling pose around the new centres, riding the
new profile — is named as a follow-up; this phase
launches no successor.

**Fences:** all levels are band-posed [10, 20]
SET-244 figures; Phase 356's full-extent caveats
travel (the lineage's full-extent levels restate
to ≈ −1.44×10⁻³ over [10, 60]; no extent audit
was run here). No EC pass is claimed by any
verdict name; no sustainment or transport
wording.

**Incidents:** one runtime restart killed both
workers mid-K = 17; both resumed from per-rung
checkpoints and reproduced their warm-start reads
identically (the killed partials remain in the
screen logs: 521/517 lines vs 481 counted evals).

**Three goals:** Goal 1 — pressure level improved
in the band, wall unbroken. Goal 2 (wormhole) —
untouched. Goal 3 (subluminal) — untouched.

DESK: NO DATA CONTACT.
