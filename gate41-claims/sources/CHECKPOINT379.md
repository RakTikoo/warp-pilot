# PHASE 379 — THE HARVESTED CENTRE

**VERDICT: STATIONARY LEVEL IMPROVES AT THE HARVESTED
CENTRE — at both centres. The best stationary band
level on the A2 lineage is now −1.942246×10⁻⁴
(SET-244, band [10, 20]), at the μ = 1.15 harvested
centre (H2). The level remains NEGATIVE — no energy-
condition pass, no member, no gate referral (the
registered ≥ 0 flag does not fire).**

Charged at ledger entry 957. Registration filed
before any computation:
`phase379/work/p379_registration.md` (SS0–SS7).
Frame of record: the VM (laptop NOT admitted —
SS1 below).

## 1. The act

Phase 374's saturation anatomy proved the dwelling
pose's ceiling is the stationary profile of its own
centre: the champion's worst instant is a bottom-
dwell instant (μ = 1.1125, derivatives exactly zero)
whose read IS the stationary read L_stat(1.1125) =
−2.099385×10⁻⁴. This phase harvested the two bottom
configurations as new stationary centres — H1:
μ = 1.1125 (a = 0.15 line), H2: μ = 1.15 (a = 0.30
line), each = A2's total confirmed profiles scaled
exactly as 374's SNM modulation scales them (S→μS,
N→μN, M→1+μ(M−1)) — and re-ran the stationary joint
(S, N, M) search around each (344's machinery and
objective verbatim in form; band pose [10, 20];
K = 9/17 screen economy only).

## 2. Controls (all PASS on the VM, diff 0.0)

Record: `phase379/results/p379_controls.json`.

- CTL-379-V: A2's confirmed K = 33 vectors read
  back from the stored JSON at diff 0.0.
- CTL-379-A: the μ = 1 anchor through the 379 path
  reproduces 344's stored A2 confirmation exactly
  (NEC −2.319453132752996×10⁻⁴, DEC
  −2.2336932044559818×10⁻⁴, ρ 8.638078×10⁻⁵,
  polished depth −2.2644422911711972×10⁻⁴ — all
  diff 0.0).
- CTL-379-H1: centre H1's zero-displacement read =
  NEC −2.099385079591706×10⁻⁴, DEC
  −1.9410812223900952×10⁻⁴ — 374's bottom identity
  at diff 0.0.
- CTL-379-H2: centre H2's zero-displacement read =
  NEC −2.03181133812098×10⁻⁴, DEC
  −1.8546990569430298×10⁻⁴, ρ 8.801282×10⁻⁵ — the
  μ = 1.15 identity at diff 0.0 (two stored records
  agree digit-for-digit).
- CTL-379-F: positivity holds at zero displacement
  at both centres (centre floor minima on FINE_R:
  H1 N 1.112534, M 1.120691; H2 N 1.150035,
  M 1.124759).

**Frame admission: LAPTOP NOT ADMITTED.** The
laptop's control run (record copied back:
`p379_controls_laptop.json`) shows nonzero
SET-statistic diffs (CTL-379-A NEC 1.05×10⁻⁶, WEC
8.31×10⁻⁶; CTL-379-H2 NEC 6.07×10⁻⁸) while
pointwise and depth values agree to ~10⁻¹⁹ — the
same pattern as 344/364/372/374. All deciding reads
are VM reads.

**Machinery defect, disclosed:** the first VM
control run FAILED CTL-379-A on the polished depth
only (diff 9.94×10⁻⁶; every SET read diff 0.0).
Diagnosis isolated a transcription bug in the NEW
code (the polish objective in `adversary_polish379`
built the polish point with cos(φ) instead of
cos(θ) as the z-component); `set_read379` was
unaffected and both harvest-identity controls
passed throughout. Fixed; controls re-run; all
pass. No search step was taken before the fix.

## 3. The search and the confirmed incumbents

Per-centre cap 1100 screens; the caps did NOT bind
— both ladders completed at 481 counted evals
(K = 9: 246; K = 17: 235). Zero positivity
rejections at either centre. Confirmation
(`p379_confirmation.json`): each final incumbent's
full read reproduces its stored screen minima at
diff 0.0 (NEC, DEC, ρ).

| centre | confirmed joint level (SET-244) | NEC @ r | DEC @ r | ρ_min | margin over centre bar | margin over L_ceil |
|---|---|---|---|---|---|---|
| H1 (μ = 1.1125) | **−2.014605×10⁻⁴** | −2.014605×10⁻⁴ @ 17.683 | −1.964171×10⁻⁴ @ 19.634 | +8.750851×10⁻⁵ | +8.478×10⁻⁶ | +8.478×10⁻⁶ |
| H2 (μ = 1.15) | **−1.942246×10⁻⁴** | −1.942246×10⁻⁴ @ 16.220 | −1.898259×10⁻⁴ @ 19.634 | +8.789654×10⁻⁵ | +8.957×10⁻⁶ | **+1.571×10⁻⁵** |

Both incumbents are NEC-bound, C1-feasible, at
K = 17, and are simultaneously each centre's
best-NEC member. Polished depths (SAMPLER-M):
H1 −1.669779×10⁻⁴, H2 −1.440243×10⁻⁴ — both far
above the −0.0034 material bar (C2 not binding).
Exact pointwise worst-nulls at the SET NEC
argmins: H1 −2.023419×10⁻⁴, H2 −1.943288×10⁻⁴
(the Gate-39 sampled-bound effect, 8.8×10⁻⁷ /
1.0×10⁻⁷ below the SET figures); both remain
above their centre bars (H1 by +7.597×10⁻⁶, H2
over L_ceil by +1.561×10⁻⁵), so the verdict is
unchanged at pointwise grade.

## 4. Anatomy (SS6, at the global incumbent H2)

Boundary (end-knot) values of the correction
splines: S: −8.14×10⁻⁵ (r = 10), −7.927×10⁻³
(r = 20); N: −3.40×10⁻⁵, +7.02×10⁻⁶; M: +2.55×10⁻⁵,
+2.53×10⁻⁵. END-CLAMP re-read (all end knots
zeroed): joint −2.087299×10⁻⁴ (DEC-bound) — the
clamp COSTS 1.45×10⁻⁵: part of the gain uses the
correction's freedom at the band's outer edge
(chiefly the S correction's r = 20 value). This is
the same freedom 344's searches carried (A2's own
corrections were not end-clamped), so the
comparison is like-for-like; it is also exactly
where the band pose's caveat bites — see SS5.

Search-path anatomy: at K = 9 the NM stage did
most of the work at both centres; at K = 17 the
coordinate sweep found NO improving single-
coordinate step at either centre (objective
unchanged through the sweep) and NM added
+2.18×10⁻⁶ (H1) / +4.65×10⁻⁶ (H2) over the
resampled K = 9 incumbents.

## 5. Classification consequence

The dwelling ceiling was the A2 CENTRE's ceiling,
not the family's. Re-centring the stationary
search on the dwelling's bottom configurations
finds stationary configurations better than every
dwelling placement at A2 — the new stationary
best (H2, −1.942246×10⁻⁴) exceeds the best
dwelling worst-instant level (374's
−2.099385×10⁻⁴) by +1.571×10⁻⁵, like-for-like in
pose and instrument. The two levers compose: the
dwelling pose found the μ direction; the
stationary search converts it. The composition
suggests its own next iteration (a dwelling pose
around the NEW centres would have a new profile
to ride) — named here as the obvious follow-up
experiment; no successor is launched by this
phase.

**Fences.** Every level above is a BAND-POSED
[10, 20] SET-244 figure. Phase 356's full-extent
caveats travel with all of them: the A2 lineage's
stationary full-extent levels restate to
≈ −1.44×10⁻³ over [10, 60], and nothing in this
phase re-audits extent. No verdict name claims an
energy-condition pass; both levels are negative.
No sustainment, front, or transport content.

## 6. Incidents

One runtime restart killed both search workers
mid-K = 17; both resumed from their registered
per-rung checkpoints (n_evals 246) and reproduced
their warm-start reads identically. The killed
attempts' partial K = 17 screens remain in the
jsonl files (H1 521 lines vs 481 counted evals;
H2 517 vs 481) — the duplicates are the audit
trail of the interruption, disclosed here. One
first-launch shell redirect failure for H2 cost
no computation.

## 7. Three-goal accounting

Goal 1 (FTL drive): the extended-class stationary
pressure level improves again, to −1.942246×10⁻⁴
in the band — the wall moved, it did not break;
no EC pass, no member, no front or transport
content. Goal 2 (wormhole): untouched. Goal 3
(subluminal record): untouched.

DESK: NO DATA CONTACT.

Artefacts: `phase379/work/p379_registration.md`,
`p379_lib.py`, `p379_controls.py`, `p379_search.py`,
`p379_confirm.py`; `phase379/results/
p379_controls.json`, `p379_controls_laptop.json`,
`p379_screens_H1.jsonl`, `p379_screens_H2.jsonl`,
`p379_state_H1.json`, `p379_state_H2.json`,
`p379_confirmation.json`, search logs.
