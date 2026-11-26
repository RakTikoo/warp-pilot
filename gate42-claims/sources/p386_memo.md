# Phase 386 — THE GRADED SHELL (W5): memo

**Charge:** ledger entry 977. Goal-3 line (best subluminal
record). **Verdict: GRADED CLASS BEST β = 0.18671875**
(gate referral; new-category wording only — see the fence).
Checker: `work/p386_check.py`, coordinator-run, 20/20 PASS.

## Claim-gate fence (carried verbatim in substance)

A graded-class optimum opens a **NEW CATEGORY**
(continuously graded density, Procaccia (10,20)
configuration class). It does **NOT** contest Procaccia's
β = 0.1363 in the step-profile shell category, and no
wording may cross categories. The β = 0.12 conversion in
the original category (Kaggle p1423, spec FINAL per
P251-2) remains owed and is **NOT** discharged by this
phase. No FTL wording: this is the subluminal line.

**Quotable wording (pending its gate):** *In the
continuously graded density category of Procaccia's
(10,20) configuration class — same geometry
(R₁, R₂) = (10,20), same continuum mass
M = 6.11288573784887775, same zero-radial-pressure
background rule and source-derived shift machinery,
with the density's radial profile a free continuously
graded function (8-spline exponential grading of the
plateau, box-4 smoothed) rather than a flat step — the
best home-verified fully legal speed is
β = 0.18671875, held by two distinct configurations
(worst margins +3.97×10⁻⁷ / +2.25×10⁻⁷, both SEC,
Type-I 1.000 at both registered spacings, audit4
second path agreeing on every deciding sign), with
failure brackets at β = 0.1875 and 0.19171875 set by
inner-ramp SEC. Procaccia's β = 0.1363 remains the
standing verified mark of the step-profile category,
uncontested. Prescribed-geometry audit; no matter
model, formation route, or stability is claimed.*

## Controls — the family is his design at c = 0 (all PASS)

- C-G0: `x_slp2.npy` SHA-256 exact.
- C-G1: graded builder at y_his vs `GenProcaccia`:
  ρ_max / λ / k relative diffs 4.0×10⁻¹² / 2.1×10⁻¹¹ /
  8.7×10⁻¹² (bar 1×10⁻⁵). The step limit is the step
  design, to construction precision.
- C-G2: y_his through the graded factory at β = 0.1363
  LEGAL at both spacings; worst +3.40418×10⁻⁷ (SEC,
  r = 5.0), ratio 1.000 to the stored Gate-7 read,
  109.5× the FD floor; audit4 agrees (+3.3958×10⁻⁷).
- C-G3: at β = 0.1364, (0, 16.635, 0): non-Type-I with
  exact min-null → his −1.30135×10⁻⁷ on the fine and
  4th-order reads (audit4 h = 0.009375: −1.30351×10⁻⁷,
  0.17%). Disclosed exception: the 2nd-order auditor at
  the coarsest h = 0.0375 alone flips Type-I there
  (+7.46×10⁻⁸, at its FD floor) — contradicted by every
  finer and every 4th-order read; recorded in full in
  `p386_controls.json`. The bar was judged on the
  fine/second-path reads, as registered.
- C-G4: Minkowski max|G| = 0 exactly; β = 0 static read
  within the Gate-6 anchor scale.

## The search — one artefact, caught and priced

**Stage 1 (old screening mask) — artefact.** B1's
screening (clone algebra, repaired radii × 26 dirs,
core mask [R₁−0.75, R_out], h = 0.0375; calibration
β_crit(y_his) = 0.13633, bracket [0.13594, 0.13672])
ran a GPU DE over the grading c alone: screening
β_crit **0.17461**. Worker C's interim home
re-judgement (`p386_rejudge_stage1.json`) convicted it:
illegal at **every** audited rung down to and including
β = 0.1363 (at 0.1363: SEC −7.04×10⁻⁶ at r = 7.0,
Type-I 0.964). The grading had stripped mass from the
inner ramp (r = 3.75–9.0) — below the mask's lower
edge, hence invisible to the screen — breaking the
very clause (inner-ramp SEC/flux) that is the step
member's own tightest at home (SEC +3.404×10⁻⁷ at
r = 5.0). A screening-mask artefact, not a machinery
disagreement (wa and audit4 agreed throughout).

**Amendment (screening machinery only; bars
untouched).** The screening set was extended to the
full verdict-relevant radii — mask [R_in−0.5, R_out] =
[2.234381, 27.265413], 2,470 pts at his r_m.
Recalibration: β_crit(y_his) = 0.136328125, identical
to the old mask; the old champion collapses to
0.120703125 — the extended set convicts it, consistent
with the home read. GPU evaluator: B1's pure-torch
port failed its ≤ 10⁻⁷ validation gate on
`eulerian_that`'s frame convention in γ's degenerate
tangential eigenspace (GPU Einstein tensor itself
agreed to 1.4×10⁻¹²); the shipped hybrid (GPU Einstein
→ CPU wa frame machinery verbatim) validates at
6.9×10⁻¹³ / 4.3×10⁻¹³ max score difference with
identical brackets.

**Extended-set search (all screening).** Grading-only
DE re-run: **0.15195** [0.15156, 0.15234]. Joint Powell
restarts: from y_his **0.16680** [0.16641, 0.16719]
(1,486 evals); from the Stage-1x best 0.15586; five
seeded random restarts terminated at the 0.10 floor.
Box-widening (≤ 2 per lineage): stage1x lineage
(c idx 1–6 → ±2.25) 0.15195 → 0.15820; powellbest
lineage (a idx 8, 19 → ±12) no improvement. GPU DE
(22 params, pop 64, 190 gens, 12,224 evals; box =
registered except c idx 1–6 at ±2.25): best
**0.18711** [0.18672, 0.18750]. Harvest: top 6 distinct
(DE population members, 0.18711 + 5 × 0.18633).

## Home re-judgement — the verdict reads

Full verdict audits (wa_auditor + audit4, 1,430-pt
registered set, h = 0.0375 / 0.01875, common bars;
`p386_verdicts.json`, `p386_verdicts_rank1.json`):

| Subject | Screening | Home ceiling | Failure bracket | Legal-rung worst |
|---|---|---|---|---|
| S1 GPU-DE best (`84c9043e…`) | 0.18711 | **0.18671875** | 0.19171875 | SEC +3.971×10⁻⁷ @ r = 3.75 |
| Rank-1 DE member (`d1efd424…`) | 0.18711 | **0.18671875** | 0.1875 | SEC +2.253×10⁻⁷ @ r = 7.0 |
| S2 Powell-from-his (`29af1376…`) | 0.16680 | 0.16640625 | 0.17140625 | SEC +1.651×10⁻⁷ @ r = 8.0 |
| S3 grading-only (`87df3cfe…`) | 0.15195 | 0.1515625 | 0.1565625 | DEC +4.650×10⁻⁷ @ r = 25.0 |

At S1's legal rung: Type-I 1.000 (1,066 significant
points), shell sampled-NEC +1.671×10⁻⁷, worst = 123×
the FD floor, audit4 worst +3.967×10⁻⁷ (sign agreement
on every deciding margin), q_max 0.9974 at r = 16.4.
The coordinator independently re-audited S1's legal
rung (worst +3.971325×10⁻⁷, identical) and ran
rank-1's ladder. Dose–response at home, same
configuration class: step member 0.1363 → grading
alone 0.1515625 (+0.0153) → joint Powell 0.16640625
(+0.0301) → joint DE 0.18671875 (+0.0504).

## Anatomy — what the grading buys, and what it costs

S1's grading: φ = 4.47 at R₁ falling to φ_min = 0.123
at r ≈ 13.2, recovering to 0.657 at R₂
(c = [1.4975, 0.1956, −2.25, −2.1104, −1.0328, −1.7237,
−2.25, −0.4193]; ρ₀ × 3.29 vs the step member;
ρ_max 3.162×10⁻⁴; λ 0.6537; k 0.028582; q = 1.5539,
r_m = 16.234). Mass moves **inward and onto the inner
ramp**: 1-m bins r = 7–13 gain up to +0.0432 of
M_target (bin [10, 11)); bins r = 14–22 lose up to
−0.0326 (bin [17, 18)); total mass conserved by
construction. Mechanistically: the added inner mass
**relaxes the flux-overload wall in the nominal core**
— q_max stays at 0.997 < 1 at β = 0.18671875, at the
same site as the step member's (r = 16.4, the switch),
where y_his is already at its ceiling at 0.1363 — and
**tightens inner-ramp SEC**, which becomes the
ceiling-setter: at the legal rung SEC binds at
+3.971×10⁻⁷ (r = 3.75); at the first failing rung
(β = 0.19171875) SEC collapses to −2.673×10⁻⁵ at
r = 9.75 (DEC also −7.01×10⁻⁶; Type-I 0.9559 with the
non-Type-I patch now mid-shell at r = 14.75–23.0;
q_max 1.0243). The flux-overload onset neither moved
site nor was replaced as the *screening* mechanism —
but at verdict grade the graded class's ceiling is set
by SEC in the inner ramp, not by q crossing 1.
Contrast the old-mask champion: it moved mass inward
*off* the ramp's support structure (its φ peaked the
plateau while the smoothed fringe starved), and the
same clause convicted it at 0.1363. The difference
between the artefact and the result is *where* the
inward mass lands — on the ramp (S1) vs past it
(Stage-1 champion).

## Goal accounting

- **Goal 3 (subluminal record):** this phase's
  headline. A new category is opened: continuously
  graded density in Procaccia's configuration class,
  best home-verified β = 0.18671875. In the original
  step-profile category nothing changes: Procaccia's
  0.1363 stands as the verified mark, the programme's
  verified best there remains β = 0.10 (Gate-7) with
  the 0.105 row G29-A-restated and the 0.12 conversion
  (p1423) still owed.
- **Goal 1 (FTL drive):** unchanged — no joint pass
  anywhere; this phase ran no drive read.
- **Goal 2 (wormhole):** unchanged — the Gate-23 /
  G27-A claim set stands; no traversability claimed.

## Follow-ups (logged, not run)

- **FU-P386-1:** second box-widening lineage from the
  DE best — S1 sits on the widened c edges (c3, c7 at
  −2.25) and a₁₂ at the +8.0 box edge; one more
  widening round (c idx 1–6 → ±3.375, a₁₂ → ±12) +
  DE/Powell, then home re-judgement. Screening headroom
  is suggested, not established.
- **FU-P386-2:** a Gate for the graded-class claim set
  (β\* = 0.18671875, two subjects, this memo's quotable
  wording) before any publication — the phase verdict
  is a gate referral, per the charge.
- **FU-P386-3:** harvest ranks 3–6 (screening 0.18633)
  were not home-audited; audit only if a future claim
  needs them.
- **Standing lesson (priced twice now — P251-3 and
  here):** record-line searches must screen on the
  full verdict-relevant radii, inner ramp included.
  The extended set of this phase is the pattern.

## C12 accounting / DESK

Prescribed-geometry audits throughout; the required
source is the Einstein tensor, conservation automatic
(Bianchi). No matter model, formation route, or
stability is claimed for any row. Le
(arXiv:2605.25417)'s stricter source-consistency
standard is a standing caveat, not a bar.
**DESK: NO DATA CONTACT** — no real-world dataset was
consulted; all objects are from the programme's own
record.

## Files

`results/p386_controls.json` (C-G0..C-G4),
`results/p386_stage1.json` + `p386_pool_stage1_state.json`
+ `p386_pool_gpu_validate.json` (B1),
`results/p386_rejudge_stage1.json` (Worker C),
`results/p386_search.json` + `p386_pool_stage2x_*.json`
(B2, as amended), `results/p386_verdicts.json` (C2),
`results/p386_verdicts_rank1.json` (coordinator),
`work/p386_check.py` (checker, 20/20), all code in
`work/` (pool code with the `p386_pool_` prefix).
No ledger append (parent owns it); no launches beyond
the registered pool search; no external contact.
