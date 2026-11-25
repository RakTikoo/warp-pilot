# P214-1 — MEMO: INTERVAL EXTENSION OF THE SUSTAINED POSE (FU-P210-1) (Phase 214 ITEM 1)

Worker 1 of Phase 214, warp pilot. Execution of
`phase214/REGISTRATION214.md` ITEM 1 — the follow-up Phase 210's
own memo named: the director arm (m = 1, κ = 0.3, P-DIR-T2) met
every Phase 207 throat bar on [0, 0.5] at G4 with its worst
clause minimum +0.0045418770853060675 (NEC_φ = DEC_φ at t = 0.5)
still declining at the interval end; this item extended the
SAME march (`B.march` phase162 + `E.mtt_field` /
`E.instant_read_comp` phase167, director reads via phase207
`instant_read_dir_T2`, imported, never edited) to T = 1.0 at
G4-class resolution (N_θ = 11521, h_t = 0.000625, RK4), both
arms read off the same marched state at 41 sampled instants
(every 0.025 on [0, 1.0]), per-instant minima for all seven
clauses + momentum worst + flare min + domain regularity at
every instant. Frame of record: Phase 166 pin,
Gate-19-corrected tensor. Execution form: HOME-SHORT — all
marches ran locally in 89.7 s total (extension march+reads
56.8 s), far inside the 1800 s wall budget; verdict form 3 is
not owed and no laptop package was needed. INTERNAL only. No
ledger append, no launch, no external contact.

## VERDICT (registered Phase 214 ITEM 1 form 2): FAILS AT t* ∈ (0.5, 1.0]

**t* ∈ (0.5, 0.50625]** — the pose holds for barely one
two-hundredth of a time unit past the Phase 210 interval. The
first failing sampled instant is t = 0.525; within that sampled
bracket (0.5, 0.525] four clauses cross zero (NEC_ρ, NEC_φ,
DEC_ρ, DEC_φ), and the pre-registered refinement (intermediate
instants at 0.00625 spacing inside the bracket) orders the
crossings: **NEC_φ = DEC_φ crosses first, in (0.5, 0.50625]**
(already −0.03537861581570745 at t = 0.50625), while NEC_ρ =
DEC_ρ is still positive at t = 0.50625 (+0.004707212097541547)
and crosses one refinement step later, in (0.50625, 0.5125].

**Mechanism: MARGIN EXHAUSTION.** The failing clause is the
very clause whose margin Phase 210 left declining at the
interval end — NEC_φ = DEC_φ, +0.0045418770853060675 at
t = 0.5 — reaching zero on its established trend, ahead of
every other clause. It is not a new clause failing first:
NEC_ρ/DEC_ρ, the only other clauses to cross inside the
sampled bracket, cross strictly later at refined resolution.
**The sustainment interval is [0, t*), t* ∈ (0.5, 0.50625].**
The Phase 210 result stands exactly as stated — the pose is
sustained on [0, 0.5] at this pose's scope — and it does not
extend materially past 0.5: the interval does not double.

## 1. RUN RECORD — controls first, asserted before any extension read

**Byte identity (asserted before and after, md5):** the six
protected files — `phase129/work/p1296_derive_raw.json`,
`phase150/work/p1501_families.py`,
`phase162/work/p1621_engine.py`, `phase167/work/p167_engine.py`,
`phase169/work/p1692_engine.py`, `phase202/work/p2022_wound.py`
— byte-identical before/after (md5 table in
`results/p2141_results.json`; independently re-verified live
by the checker against the Phase 210 stored list). Nothing
outside `phase214/` was edited. The T = 1.0 extension sets the
march module's `T_END` global in memory only (the phase162
file is untouched, as the md5 table proves); the control
marches ran first at the file's own T_END = 0.5.

- **(C-a) G4 reproduction on [0, 0.5] — PASS, exact.** Both
  arms' 21 sampled instants at G4 (T = 0.5 march) reproduce
  `phase210/results/p2101_results.json` stored G4 per-instant
  clause minima with max abs diff **0.0** (κ = 0 arm 0.0;
  director arm 0.0).
- **(C-b) κ = 0 anchors — PASS, exact.** On the G2 arm (the
  P169-1(f) anchor grid, as in Phases 209/210): first NEC_φ
  failure **t = 0.400**; worst NEC_φ
  **−0.6297872673028908**, abs diff **0.0**. Cross-value: the
  G4 arm's own worst NEC_φ on [0, 0.5] is −0.6297872673031459,
  abs diff vs the anchor 2.5512925105886097×10⁻¹³ — the
  ~10⁻¹² grid agreement Phase 210 documented.
- **(C-c) Director t = 0 audit — PASS, exact.** κ = 0.3 and
  κ = 0 clause minima vs Phase 202 stored minima, max abs
  diff **0.0** each; ũ_true(θ*) = **1.1412482021558361**
  (abs diff 0.0); A_,θ at t = 0 max abs 0.0.

Only after all three controls passed was the T = 1.0 march
run. One diagnostic, not a control: the extension march's own
t = 0.5 read vs the stored T = 0.5-march G4 read differs by
max abs **0.0** on both arms (the `E.mtt_field` stencil
boundary at t = 0.5 — centred in the long march, one-sided as
the short march's final instant — moves no clause minimum at
the stored precision), so the extension's anatomy joins the
Phase 210 record seamlessly at t = 0.5.

## 2. The failure anatomy (director arm, extension)

**Refinement inside the sampled bracket (0.5, 0.525]**
(director clause minima; the registered 0.00625-spaced
intermediate instants):

| t | NEC_ρ = DEC_ρ | NEC_φ = DEC_φ |
|---|---|---|
| 0.5 | +0.024846605153054924 | **+0.0045418770853060675** |
| 0.50625 | +0.004707212097541547 | **−0.03537861581570745** |
| 0.5125 | −0.015826151504813257 | −0.07675595778669764 |
| 0.51875 | −0.036759947686793915 | −0.11965267717293537 |
| 0.525 | −0.05810079544054636 | −0.16413453324026417 |

NEC_φ = DEC_φ falls ≈ 0.040 in the first 0.00625 past t = 0.5
— roughly nine times its remaining margin per refinement
step; the margin was not eroding slowly toward a distant
zero, it was the last step of a steepening decline (Phase 210's
[0, 0.5] anatomy: +0.15080241563149732 at t = 0.475 →
+0.0045418770853060675 at t = 0.5). The NEC_ρ = DEC_ρ companion
pair follows the same shape one step behind: its margin
(+0.024846605153054924 at t = 0.5) is consumed by t = 0.5125.

**Full per-instant decline of the failing clause on the
extension** (director NEC_φ = DEC_φ; NEC_ρ alongside; all 21
instants from t = 0.5 are in the JSON anatomy block):

| t | NEC_φ = DEC_φ | NEC_ρ |
|---|---|---|
| 0.5 | +0.0045418770853060675 | +0.024846605153054924 |
| 0.525 | −0.16413453324026417 | −0.05810079544054636 |
| 0.55 | −0.3608848997987937 | −0.14767288278057844 |
| 0.575 | −0.5908693472669677 | −0.24433140266869335 |
| 0.6 | −0.859299878907577 | −0.34858521933568154 |
| 0.625 | −1.1740508689279014 | −0.46099525904146543 |
| 0.65 | −1.5449533316732673 | −0.5821800686321568 |
| 0.675 | −1.9843665275917959 | −0.7128221039517264 |
| 0.7 | −2.509404698923423 | −0.8542101175030536 |
| 0.725 | −3.1400832964817393 | −1.0082399845405323 |
| 0.75 | −3.9011634441195406 | −1.1753344044467995 |
| 0.8 | −5.959544588364516 | −1.5617715195206014 |
| 0.85 | −9.106376812202676 | −2.039194648130465 |
| 0.9 | −14.113740157567136 | −2.657692446863458 |
| 0.95 | −22.48662033783558 | −3.511080237112041 |
| 1.0 | −37.400387861728845 | −4.790398897925462 |

There is no plateau or recovery: past t* the failure deepens
superlinearly for the rest of the interval. By t = 1.0 every
one of the seven clauses is negative on the director arm
(worst DEC_ρ −39.455894142388544; WEC −10.70440185951847;
NEC_θ −8.849795370523418; DEC_θ −12.613394323223764). The
non-clause bars, by contrast, never fail on the extension:
momentum worst 1.7763568394002505×10⁻¹⁵ ≤ 10⁻¹⁰, flare min
0.05774016940840757 > 0, domain regular at every instant
(R min 0.3435007191376366, exp(2Φ) min 0.005811242014959039,
both > 0). The pose dies by clause-margin exhaustion alone.

**Registered step blocks — worst clause minimum per block**
(director / κ = 0):

| block | director worst | κ = 0 worst |
|---|---|---|
| (0.5, 0.625] | −1.1740508689279014 (DEC_φ) | −1.9502756561074923 (DEC_φ) |
| (0.625, 0.75] | −3.9011634441195406 (DEC_φ) | −4.910006173807935 (DEC_φ) |
| (0.75, 0.875] | −11.307512517369268 (DEC_φ) | −12.75118595237414 (DEC_φ) |
| (0.875, 1.0] | −39.455894142388544 (DEC_ρ) | −41.94885152609051 (DEC_ρ) |

**κ = 0 comparison arm:** its failure anatomy is the same
collapse without the director's [0, 0.5] rescue — already
failing from t = 0.400 (worst −0.6297872673028908 on
[0, 0.5]) and deepening monotonically to −41.94885152609051
(DEC_ρ at t = 1.0). On the extension the two arms track each
other closely (director NEC_φ −37.400387861728845 vs κ = 0
−39.87206455287926 at t = 1.0): the director's +(κ/2)c_m shift
buys the [0, 0.5] interval and nothing beyond it — once the
underlying march's NEC_φ decline outruns the shift, both arms
fall together.

## 3. What stands, and the fences

Standing: all three controls reproduce their stored values
**exactly** (diff 0.0), so the extension is priced against a
verified baseline, and the extension's t = 0.5 read joins the
Phase 210 record with diff 0.0. The answer to FU-P210-1 is
sharp: the sustained pose's interval is [0, t*) with
t* ∈ (0.5, 0.50625] — the Phase 210 sustainment on [0, 0.5]
is real but terminal; the margin Phase 210 flagged as "thin
and still declining at the interval end" exhausts almost
immediately past the end, by the registered mechanism (margin
exhaustion of NEC_φ = DEC_φ), and the subsequent collapse is
deep and monotone, not a marginal re-crossing. Any future
extension of the pose's life is a construction question (a
director whose shift grows, or a different pose), not an
interval question — that is a future registration's business,
not run here.

**Fences on this verdict's face (carried from Phase 210):**
pose scope (m = 1, κ = 0.3, P-DIR-T2); jet/channel-read scope;
P129-6 combined-class scope; the p1592 deciding scan still
gates programme-level milestone wording — no verdict here is
a programme-level milestone claim. Extension reads are G4
single-grid reads whose frame control is the exact [0, 0.5]
reproduction (C-a); no (G3, G4) gate on the extension interval
is claimed, and no G3 extension companion was run.

**Failure Protocol note:** the failure is fully anatomised
above (per-instant decline, refinement-ordered crossings,
mechanism named); the follow-up it defines — a construction
that keeps the NEC_φ/DEC_φ margin from exhausting, e.g. a
time-growing director shift — is a new registration's
question, not attempted here.

## Files

- `work/p2141_run.py` — driver (item-level work record with
  the controls, the in-memory T_END extension mechanism and
  the t = 0.5 stencil note stated in advance; md5 asserted
  before/after; controls C-a/C-b/C-c asserted before the
  extension march; registered step blocks; failure scan with
  the pre-registered 0.00625 refinement; mechanism priced on
  the refined first-crossing clause set).
- `work/p2141_check.py` — checker: recomputes every
  verdict-carrying number from the results file (protected
  md5 live re-hash vs the Phase 210 stored list, C-a/C-b/C-c,
  both arms' 41-instant sets, per-block worst values for both
  arms, extension worst + bar set, failure scan, refinement
  brackets, refined first-crossing clauses/bracket, mechanism
  classification, the decline anatomy, verdict-form
  consistency). **ALL PASS, 29/29, TOTAL FAILURES 0** (run at
  delivery).
- `results/p2141_results.json` — controls with measured
  diffs, control-march G4 instants for both arms, per-instant
  minima for both arms on [0, 1.0] (41 instants each, all
  seven clauses + momentum + flare + domain), registered
  step-block worst values, the t = 0.5 stencil diagnostic,
  the failure block with sampled and refined brackets, the
  refinement instants, the full NEC_φ/DEC_φ decline anatomy,
  verdict and note, md5 before/after table.
- Full study executed home-short (89.7 s); no Kaggle/laptop
  package was required. No ledger append, no launch, no other
  file edited.
