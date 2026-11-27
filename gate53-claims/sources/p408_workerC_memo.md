# Phase 408 — Worker C memo (HOME RE-JUDGEMENT, Arms A + B)

Scope executed on the VM (frame of record), per CHECKPOINT408.md
**including Amendment A-408-1 (binding)** and the Worker C brief.
Code: `work/p408_verdicts.py` (adapted from
`phase392/work/p392_verdicts.py`); record:
`results/p408_verdicts.json`; log: `results/p408_workerC.log`.
CHECKPOINT408.md and p408_controls.json not edited; no pool work,
no ledger append, no external contact.

**Machinery.** Programme venv, float64 everywhere. Every subject
audited with Gate-6 `wa_auditor` via `p2513_lib.audit_chunked` +
`phase50` `audit4` second path, on `p2513_lib.pts_1020_control`
(1,430 pts), at BOTH h = 0.0375 and h = 0.01875; legality via
`p2513_lib.legality_1020` under the Gate-42 common bars; the
EXACT-MIN RULE was applied inside `audit_beta` wherever a read
turned on a sampled min-null (triggers disclosed below). Builders:
`phase408/work/p408_lib16.py` `GradedProcaccia16` for all subjects
(both arms are 16-mode); the lib was re-verified on the VM against
C-408-1's chain reads before any audit (rel diffs 0.0 on M,
rho_max, λ, k). Every subject's sha256 was verified from its stored
float64 vector against both `p408_search.json` and its harvest file
before auditing — all 13 verified.

**Subjects (13 distinct vectors).** A-1…A-6: Arm A harvest by
screening rank (all screening 0.193359375). A-CONTROL: Arm A's
staged `best_y` (sha `e28f083f…`, screening 0.191015625).
B-1…B-6: Arm B harvest by screening rank — B-1 the Powell subject
`b2527d10…` (screening 0.193359375); B-2 the control "RW-5
embedded, box-clipped at c13" (sha `d228c82e…`, screening
0.192578125, naturally in the top-6); B-3/B-4 screening
0.192578125; B-5/B-6 screening 0.191796875. All screening numbers
in this memo are labelled screening; all other numbers are home
verdict numbers.

## VERDICT FORM SUPPORTED

**GRADED CLASS BEST RAISES TO β = 0.193359375** — produced by
**Arm A (RESUME)**, subject **A-6** (sha256
`6461827fac113c49f8f28aea04115df524446dbd44530b86f5e408e5d3c00039`),
home-verified fully legal at β = 0.193359375, above RW-5's
standing 0.192578125 (C-408-3) by one screening rung
(+0.00078125). Deciding margins and failure bracket below.
Gate referral; graded-category wording only.

## Home ladders — every subject

Ladder rule (392 pattern): screening bracket top first; if legal,
climb +0.005 rungs, then the +0.0025 midpoint refine; if illegal,
descend 0.005 steps, then the same refine.

| Subject | Screening | Home ceiling | First failing rung |
|---|---|---|---|
| A-1 (`59abd692…`) | 0.193359375 | **0.190859375** | 0.193359375 (Type-I only) |
| A-2 (`244992ca…`) | 0.193359375 | **0.190859375** | 0.193359375 (SEC −7.78×10⁻⁷ @ 9.75 + Type-I) |
| A-3 (`c598034e…`) | 0.193359375 | **0.190859375** | 0.193359375 (SEC −1.54×10⁻⁷ @ 7.0 + Type-I) |
| A-4 (`8d92bee8…`) | 0.193359375 | **0.190859375** | 0.193359375 (SEC −2.60×10⁻⁷ @ 9.75 + Type-I) |
| A-5 (`d7ec16e8…`) | 0.193359375 | **0.190859375** | 0.193359375 (Type-I only) |
| A-6 (`6461827f…`) | 0.193359375 | **0.193359375** | 0.195859375 (SEC −1.257×10⁻⁵ @ 9.75) |
| A-CONTROL (`e28f083f…`, staged best_y) | 0.191015625 | **0.191015625** | 0.193515625 (SEC −9.37×10⁻⁶ @ 9.75) |
| B-1 (`b2527d10…`, Powell winner) | 0.193359375 | **0.190859375** | 0.193359375 (SEC −4.56×10⁻⁷ @ 9.75 + Type-I) |
| B-2 (`d228c82e…`, clipped-seed control) | 0.192578125 | **0.192578125** | 0.195078125 (SEC −1.275×10⁻⁵ @ 9.75) |
| B-3 (`fd5ca3c9…`) | 0.192578125 | **0.190078125** | 0.192578125 (SEC −4.37×10⁻⁷ @ 9.75 + Type-I) |
| B-4 (`174f7775…`) | 0.192578125 | **0.190078125** | 0.192578125 (SEC −1.56×10⁻⁶ @ 10.25 + Type-I) |
| B-5 (`dbc7214f…`) | 0.191796875 | **0.191796875** | 0.194296875 (SEC −1.327×10⁻⁵ @ 9.75) |
| B-6 (`a86767e8…`) | 0.191796875 | **0.189296875** | 0.191796875 (Type-I only) |

Every ladder completed; no COST-BOUNDED element.

## The phase best: A-6 at β = 0.193359375

- **Legal rung (home):** Type-I fraction 1.000 at both spacings.
  Worst margin h = 0.0375: **SEC +3.613×10⁻⁸ @ r = 5.0** (inner
  ramp, Rin..R1), 6.8× the measured FD floor (bar ≥ 3×); h =
  0.01875 worst SEC +2.910×10⁻⁸ @ 5.0, same sign. audit4 agrees:
  +2.675×10⁻⁸ at both spacings. Shell sampled-NEC min
  +1.334×10⁻⁷ > 0. q at the worst sampled-NEC point 0.9938;
  q_max 0.9938 @ r = 23.0. Per-region worst (h = 0.0375): shell
  SEC +3.61×10⁻⁸ (the binder); nominal core DEC +5.42×10⁻⁶.
  **Inner-ramp SEC remains the ceiling-setter** — but note the
  margin is thin (6.8× floor, vs RW-5's 106.5×): A-6 buys its
  extra rung by spending almost all of RW-5's SEC slack.
- **Failure bracket (home):** [0.193359375, 0.195859375]. The
  +0.005 climb rung 0.198359375 fails hard (SEC −2.847×10⁻⁵ @
  9.75); the +0.0025 refine 0.195859375 also fails (SEC
  −1.257×10⁻⁵ @ 9.75, Type-I 0.98499, shell sampled-NEC min
  −2.29×10⁻⁷, audit4 −1.258×10⁻⁵) — a plain SEC wall, not a
  Type-I-only wall.
- **Box record (Arm A box, the R-16 box):** exactly one
  bound-sitter — **c idx 0 = +2.25 on its hi edge**. That is the
  next widening's price list for A-6: a single coordinate.
  (Full 30-coordinate records for every subject are in
  `p408_verdicts.json` `box_record_all`.)
- **Anatomy vs RW-5** (RW-5 home record from C-408-3: legal at
  0.192578125, worst SEC +6.056×10⁻⁷ @ 3.75, q_max 0.9934 @
  19.75): A-6's binder sits at r = 5.0 (vs RW-5's 3.75), its
  q_max is essentially unmoved (0.9938 vs 0.9934 — the flux wall
  did not move), and its ceiling margin is ~17× thinner.
- **Mass redistribution (1-m bins vs the c = 0 step, fractions of
  M_target; full table in the JSON):** mass is pulled inward —
  the largest gains are r ∈ [10,11) (+0.0464 of M_target), [11,12)
  (+0.0431), [9,10) (+0.0384); the largest losses are [17,18)
  (−0.0405) and [18,19) (−0.0384). Fine-grid totals reproduce
  M_target for both profiles.
- **φ profile:** φ_max 9.4877 @ r = R₁ = 10.0000162 (= φ(R₁));
  φ_min 0.11776 @ r = 18.5428; **φ(R₂) = 2.0739**. Chain reads:
  q = 1.75324, r_m = 16.23846, rho_max 3.287×10⁻⁴.

## Home story per arm

**Arm A (RESUME — the finished 16-mode DE at the original box).**
Screening said the finished DE reached 0.193359375 with six
distinct members tied there. At home the tie breaks: five of the
six land at ceiling **0.190859375** — *below* RW-5's standing
0.192578125 — and only **A-6 holds its screening rung**,
0.193359375, becoming the phase best. The arm's honest home yield
over its own seed is real but carried by one member: the staged
control A-CONTROL home-verifies exactly at its screening level
(ceiling 0.191015625, bracket [0.191015625, 0.193515625]), so
Arm A's home yield over the truncation point is +0.00234375
(A-6); the other five members' ceilings (0.190859375) sit one
refine step below the control's home level. Screening
overstated five of six members by one rung (0.0025); A-6 it
stated exactly.

**Arm B (COMBINED — 16-mode × widened box).** No Arm B subject
home-verifies above RW-5. The Powell winner **B-1** falls two
rungs at home: ceiling **0.190859375**, failing at its screening
rung 0.193359375 (SEC −4.56×10⁻⁷ @ 9.75 + Type-I 0.99906). Its
widened-coordinate use: **c idx 0 = +2.5477** (inside the widened
±3.375, beyond the old ±2.25 — the one genuinely widened
coordinate it uses; the seed had +2.4882), **c idx 11 =
−2.1134, unchanged from the seed** (the widened switch-region
coordinate was not used further), and **c idx 13 = −2.25,
exactly on its clip bound** — B-1's only bound-sitter. The
combination's screening yield (+0.00078125 over RW-5, via Powell
on the seed) does **not** survive home re-judgement. B-3/B-4 land
at 0.190078125, B-5 holds its screening rung at 0.191796875,
B-6 lands at 0.189296875.

**Arm B seed anatomy (the clipped-seed control, B-2).** "RW-5
embedded, box-clipped at c13" home-verifies at ceiling
**0.192578125 — exactly RW-5's standing β**, with the identical
failure bracket [0.192578125, 0.195078125] and near-identical
deciding margins (worst SEC +6.042×10⁻⁷ @ 3.75 vs RW-5's
+6.056×10⁻⁷; audit4 +6.037×10⁻⁷; q_max 0.9920 @ 16.3 vs 0.9934
@ 19.75). **The LS embedding plus the c13 clip costs RW-5
nothing at home in the 16-mode basis** — no refine step is lost
(contrast 392's R16-2 read, where the E2-1 embedding cost a
refine step). Screening's losslessness read is confirmed at
home. B-2's only bound-sitter is c idx 13 = −2.25 (the clip
bound itself).

## The Type-I-only walls — judgement

Three failing rungs immediately above a ceiling have all EC
margins positive with Type-I alone failing: **A-1** and **A-5**
at 0.193359375, **B-6** at 0.191796875. Judgement, on the
numbers, the same for all three: **DISTINCT DIRECTIONAL
STRUCTURE — the flux clause has NOT arrived.**

- A-1 @ 0.193359375: 1 non-Type-I significant point, at r =
  15.25; q there 0.9865; q_max 0.9932 @ 23.0 < 1; n(q>1) = 0.
- A-5 @ 0.193359375: 2 non-Type-I points, both at r = 23.0;
  q at those points = q_max = 0.9979 < 1.
- B-6 @ 0.191796875: 1 non-Type-I point at r = 19.75; q there =
  q_max = 0.9980 < 1.

In each case Type-I fails while q stays strictly below 1
everywhere, including at the failing points themselves — the
392 pattern: a directional (sampled-null / eigenvalue-ordering)
structure distinct from the flux clause, which would require
q ≥ 1 at or near the failing points. The margins are close
(A-5 and B-6 sit within 0.002 of q = 1), so the flux clause is
near, but on the deciding reads it has not arrived at any of
these rungs. All other failing rungs in the phase fail on SEC
(usually with Type-I also failing) and are not Type-I-only
walls; their per-rung bars are in the JSON.

## Ceiling-setter, per subject

Every subject's binding EC at its legal ceiling is **SEC in the
inner ramp (Rin..R1)** — at r = 3.75 for all except A-6 (r =
5.0) and A-CONTROL (r = 6.0). Inner-ramp SEC remains the
ceiling-setter for the whole phase. Ceiling q_max values run
0.978–0.997; the flux wall did not move for any subject.

## Box records (bound-sitters, per subject — next widening's price list)

- Arm A box (all c ∈ ±2.25): A-1: c0 +2.25, c10 −2.25. A-2: c0
  +2.25. A-3: c0 +2.25, c10 −2.25. A-4: c0 +2.25. A-5: c0
  +2.25, c10 −2.25. **A-6: c0 +2.25 only.** A-CONTROL: c0 +2.25.
  (Every Arm A subject sits on c idx 0 — the innermost mode is
  saturated across the arm.)
- Arm B box (c idx 0/11 ∈ ±3.375, rest ±2.25): B-1: c13 −2.25
  only (idx 0 at +2.5477 is interior to the widened box). B-2:
  c13 −2.25. B-3: c13 −2.25. B-4: c13 −2.2428 (within 0.01 of
  the lo edge). B-5: c13 −2.25. B-6: c13 −2.25. (Every Arm B
  subject sits on/near the c13 clip bound — inherited from the
  seed lineage; no Arm B subject sits on either widened edge.)

## Incidents (all disclosed)

1. **Exact-min triggers (6 rungs):** the EXACT-MIN RULE fired
   inside `audit_beta` at A-2, A-3, A-4 @ 0.193359375 and B-1 @
   0.193359375, B-3/B-4 @ 0.192578125. Exact min-null values:
   A-2 +1.874×10⁻⁷ (positive; its failure is SEC/Type-I, not the
   null read), A-3 −2.351×10⁻⁸ and A-4 −2.543×10⁻⁸ (negative —
   the exact read confirms those rungs' failure independently),
   B-1 +1.924×10⁻⁷, B-3 +3.077×10⁻⁷, B-4 +3.230×10⁻⁷ (all
   positive; failures rest on SEC/Type-I). No legality call
   turned on a sampled min-null without the exact read. Full
   records in the JSON (`exact_min` per rung).
2. **A-6's ceiling margin is thin but clears every bar:**
   worst/floor = 6.8× (bar 3×), sign-stable across both
   spacings, audit4 positive at both spacings (+2.675×10⁻⁸).
   It is a legal rung under the registered bars, stated with
   its thinness on the face.
3. The harmless `RuntimeWarning: invalid value encountered in
   log` from the lib16 builder (r → 0 guard) appears in the
   home log, exactly as in 392's runs; it affects no read.
4. No other incidents: all 13 hash verifications passed, all 13
   ladders completed, total home wall 512 s.

## Bottom line (HOME numbers)

- **β\* = 0.193359375, subject A-6, Arm A** — GRADED CLASS BEST
  RAISES TO β = 0.193359375 (deciding margins and failure
  bracket above).
- Arm A home yield: one member (A-6) above the standing best;
  five members at 0.190859375; the staged control exactly at
  its screening level 0.191015625.
- Arm B home yield: nothing above RW-5; its best member is the
  clipped-seed control itself at exactly 0.192578125 — the
  embedding+clip is home-lossless, and the combination bought
  nothing at home beyond its seed.
- Type-I-only walls (A-1, A-5, B-6): distinct directional
  structure, flux clause not arrived, on the numbers above.

DESK: NO DATA CONTACT (this phase's objects are prescribed
configurations from the programme's own record).
