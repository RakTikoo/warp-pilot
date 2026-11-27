# GATE-51 — INDEPENDENT RE-JUDGEMENT OF THE PHASE 392 CLAIM SET

**Charge:** ledger entry 1061 (FU-P392-1). **Frame:** VM frame of
record only; the laptop was not used and is not admitted as a gate
instrument (standing pattern of this lineage). **Machinery:** fresh
gate machinery only — `gate51/work/g51_lib.py`, written for this gate
in the gate-lineage builder pattern of Gates 42/44 (the graded-family
builder at grading bases of n_c ∈ {8, 12}); tensor instruments
gate6/wa_auditor.py and phase50/p503_lib.audit4, the registered pair.
Nothing was imported from phase392/work, phase391/work or
phase386/work. Stored bytes verified by hash before any audit.
float64 everywhere.

**The registered bars, applied as written** (CHECKPOINT386 §2,
inherited verbatim by CHECKPOINT391/392): on the primary wa audit at
BOTH spacings (h = 0.0375, 0.01875), registered set
pts_1020_control (1,430 rows) — Type-I fraction = 1.000 over
significant points; worst NEC/WEC/SEC/DEC margins > 0, sign-stable,
worst ≥ 3× the measured FD floor; shell sampled-null NEC min > 0 —
**and audit4 agreement on the sign of every deciding margin** (the
four eigenvalue EC minima). Per Gate-44 §1 C-1, audit4's own Type-I
fraction and direction-sampled diagnostics are recorded as
diagnostics, not bars.

## Verdict summary

| Claim | Ruling |
|---|---|
| (a) RW-5 legal at β = 0.192578125; failure bracket 0.195078125 | **SURVIVES** |
| (b) RW-5 interiority: no coordinate on a box edge; hash identity | **SURVIVES** |
| (c) Arm T flatness: the resumed DE's best is E2-1's level, flat from gen 0; the cap was not binding | **SURVIVES RESTATED** (the identity wording only — see §4; the level, the flatness and the conclusion stand as charged) |
| (d) Arm R-16's no-yield is a truncated-run statement, never a basis verdict | **SURVIVES** (the wording rule is confirmed on the stored records, §5) |
| Controls: y_his at 0.1363 (legal) and 0.1364 (fails); E2-1 legal at 0.191796875 | **SURVIVE with calibration note C-1** (the 0.1364 half is a screening-rating statement, not a pointwise failure on either instrument — §1, §6) |

The quotable set is §7 (G51-A…G51-E). The fence is carried verbatim
in G51-B and G51-E: **graded-category wording only — this set never
contests the step-profile category (Procaccia's 0.1363 stands
there; the programme's verified best there remains 0.10).**

## §1 Machinery and calibrations

**C-0 · Stored bytes (hash gate).** Every audited vector was
re-hashed (sha256 of the float64 tobytes) against its stored record
before auditing: RW-5 `44719b50…35c2` ✓, RW-1 `afcde914…8bc` ✓,
E2-1 `61679383…3066` ✓ (and T-4, Arm T's harvest member, hashes to
E2-1's value exactly — §4). Full hashes in
`gate51/results/g51_records.json`.

**C-0b · The gate builder reproduces the constructions.** RW-5's
chain reads on gate machinery vs the phase's stored record: ρ_max
3.240335264325754×10⁻⁴ (stored identical), λ 0.8999655940391417
(identical), k 0.02367465973823105 (identical), M
6.112885737848847 vs stored 6.112885737848849 (3×10⁻¹⁵ relative —
the class convention fixes M to the target). Construction grid
1,200,707 points. E2-1's chain reads reproduce Gate-44's gate reads
(ρ_max 3.2585104937459165×10⁻⁴, λ 0.8931410086746383,
k 0.024530591100784323). RW-5's grading range on the gate builder:
φ ∈ [0.11231, 11.900] (phase anatomy: min 0.1123 @ 18.55, max 11.900
@ R₁ ✓).

**C-1 · Calibration note — the y_his 0.1364 control (read before
§6).** The charged control pair "(0.1363 legal, 0.1364 fails)" is,
in the Gate-42 record this gate calibrates against, a statement of
two different instruments: the verdict audit at 0.1363 (the
calibration digit) and the FD screen's β_crit rating. On this
gate's machinery: the verdict audit finds y_his **still legal at
0.1364** (worst SEC +3.386648×10⁻⁷ @ r = 5.0, 109.0× floor, Type-I
1.000 at both spacings, second path agreeing — the margin moves
0.5% from its 0.1363 value), and the screen's pointwise score at
exactly 0.1364 is still marginally positive (+6.80×10⁻⁸, NEC at the
exterior tail r = 25.77). What the screen does reproduce, exactly,
is Gate-42's rating: β_crit(y_his) = **0.136328125**, bracket
[0.1359375, 0.13671875], under BOTH masks — so 0.1364 lies above
the design's screen-rated speed, inside the bracket's failing
side, and "fails at 0.1364" survives **only** in that rating sense.
No claim (a)–(d) turns on 0.1364; the calibration digit at 0.1363
is reproduced at ratio 1.000000 (§6). The gate records the wording
correction here rather than repeating the shorthand.

**C-2 · Direction-sampled diagnostics are subordinate.** RW-5's
shell sampled-NEC at its legal rung reads +2.065×10⁻⁷ on gate
machinery vs the phase's stored +2.007×10⁻⁷, and q_max 0.9921 vs
stored 0.9934 — both positive / both < 1, sign and magnitude class
agreeing, while every deciding (eigenvalue) margin agrees to
≤ 3×10⁻¹³ (§2). This is the Gate-44 §1 pattern (there: a
sampled-NEC diagnostic differing in sign at 5×10⁻⁸ between
samplings at non-Type-I points; here all points are Type-I and
only the third digit moves). Direction-sampled quantities are
C-10 (Gate-43) sampling-convention territory; no ruling in this
gate turns on one.

**Machinery note (disclosed).** The builder's exterior-branch line
emits a benign RuntimeWarning (log of a negative argument inside a
`np.where` branch whose values are discarded by that same where) —
inherited verbatim from the gate-lineage pattern; all chain reads
reproduce stored digits (C-0b), so it touches no read.

## §2 Claim (a) — RW-5's legality and its bracket: SURVIVES

RW-5 (12-mode lineage, R-W widened box, sha256 `44719b50…`), full
registered bars on gate machinery, registered set, both spacings:

- **β = 0.192578125: LEGAL.** wa worst margin SEC
  **+6.055586×10⁻⁷ @ r = 3.75**, **106.5× FD floor**, Type-I 1.000
  at both spacings (fine spacing worst +6.051406×10⁻⁷); per-EC
  minima NEC/WEC/DEC +6.973×10⁻⁷, SEC +6.056×10⁻⁷; shell
  sampled-NEC +2.065×10⁻⁷ > 0; audit4 worst **+6.050012×10⁻⁷**,
  all four deciding margins positive at both spacings — sign
  agreement met. Stored digits reproduced: phase worst SEC
  +6.055585×10⁻⁷ (agreement 3×10⁻¹³), audit4 +6.050012×10⁻⁷.
  q_max 0.9921 @ r = 19.75 (< 1; diagnostic, C-2).
- **β = 0.195078125: FAILS — compound, as charged.** wa worst SEC
  **−1.031586×10⁻⁵ @ r = 9.75** (stored −1.031586×10⁻⁵), Type-I
  fraction 0.98499 (the stored figure exactly), shell sampled-NEC
  −4.54×10⁻⁷, audit4 SEC −1.032461×10⁻⁵ (stored identical) — SEC,
  Type-I and sampled-NEC bars fail together at both spacings; not
  a Type-I-only wall.
- **The tie.** RW-1 (`afcde914…`) is also LEGAL at
  β = 0.192578125 on gate machinery (worst SEC **+5.792298×10⁻⁷
  @ r = 3.75**, 104.3× floor, Type-I 1.000, audit4 +5.786895×10⁻⁷
  agreeing; stored +5.792×10⁻⁷). Two subjects hold the ceiling;
  RW-5 leads on margin, the 391 tie-break pattern, as charged.

## §3 Claim (b) — RW-5's interiority: SURVIVES

Pure arithmetic on the hash-verified stored vector against the
registered R-W box (CHECKPOINT392 Arm R-W: c₁, c₉ ∈ [−3.375,
3.375]; other c ∈ [−2.25, 2.25]; a ∈ [−8, 8], a₁₂ ∈ [−12, 12];
q ∈ [0.25, 3.0]; r_m ∈ [11, 23]) — `gate51/results/g51_records.json`:

- **All 26 coordinates lie strictly inside the box; none sits on
  any edge.** The nearest approach to any edge is c₁₀ = −2.2073,
  0.0427 from its −2.25 bound. The phase's own stored
  `box_edges` field for RW-5 is the empty list — consistent.
- The two widened coordinates: **c₁ = +2.476579** — beyond the old
  E2 edge (+2.25), so the widened room is genuinely used, but
  0.898 short of the widened edge (+3.375); **c₉ = −2.192138** —
  does not reach even the old edge (−2.25), 1.183 short of the
  widened edge.
- The charged conclusion stands: RW-5's optimum is an interior
  optimum of the widened box, and **the next widening's price
  list is empty** for this lineage.

## §4 Claim (c) — Arm T's flatness: SURVIVES RESTATED

Re-judged from the stored population records
(`p392_pool_t_de_state.json`, `p392_search.json` t_lineage,
`p392_verdicts.json`), no re-run:

- The resumed DE ran to its registered 120-min cap: **118
  generations, 7,616 β_crit evaluations, 7,229.6 s wall,
  done = True** (the resumption cross-check — the driver's startup
  read of the stored best = 0.191796875 — is in the phase record).
- **The best-history is flat at exactly 0.191796875 at every one
  of the 119 recorded generations (gen 0 through gen 118)** —
  min = max = 0.191796875. More time bought nothing; 391's
  late-generation slope does not continue; **the cap was not the
  binding constraint**, as charged.
- One wording precision, restated for exactness (the Gate-44
  claim-(b) pattern):

> **Restated identity (replaces "the resumed DE's best is E2-1
> itself" in the charge's shorthand):** the resumed DE's best
> *level* never moved from E2-1's 0.191796875; the DE's own final
> best vector is a distinct vector (sha256 `e2d02cd9…`) sitting at
> that same screening level, while the arm's home-verdict ceiling
> at 0.191796875 is held by **E2-1 itself** — harvested as T-4,
> hash-identical to E2-1 (`61679383…`, verified in §1 C-0) — and
> by T-2. The negative claim (no subject of Arm T exceeds
  E2-1's level, at screening or at home) stands exactly as
  charged.

## §5 Claim (d) — Arm R-16's status: SURVIVES (wording rule confirmed)

The truncation facts, verified from the stored records
(`p392_pool_r16_de_state.json` — the staged state itself —
`p392_search.json` r16_lineage, Worker B's memo):

- The R-16 DE stopped at **generation 106** after **6,848 β_crit
  evaluations / 5,113.7 s**, with **done = False** in its own
  staged state file. Its registered arm cap was 120 min
  (7,200 s): it stopped **before its own cap**, and the stored
  stop string names the binding constraint — the phase's
  registered **6 h total pool budget** across all arms, not the
  arm cap and not convergence.
- The run was not converged: the population mean β_crit was
  **still rising** — 0.10242 (gen 39) → 0.12791 (gen 71) →
  0.15165 (gen 85) → **0.17787 (gen 106)**; the final figure is
  independently recomputed by this gate from the staged
  population's stored β_crit array (64 members): **0.177869** —
  the recorded value. The DE best stayed static at its gen-0
  level 0.191015625 at every recorded generation (the E2-style
  late lift had not arrived when the budget bound).
- **Ruling (the claim as charged):** Arm R-16's no-yield may be
  quoted **only** as a truncated-run statement — a statement
  about a budget-stopped, still-rising run — and **never** as a
  verdict on the 16-mode basis. Its population stands staged for
  resumption (FU-P392-2), and any future quotation of the arm
  carries this rider.

## §6 Controls: SURVIVE with calibration note C-1

- **y_his (c = 0 member) @ β = 0.1363: LEGAL** on gate machinery
  under the full registered bars — worst SEC
  **+3.4041776408044866×10⁻⁷ @ r = 5.0**, **109.5× FD floor**,
  Type-I 1.000 at both spacings, audit4 +3.395770×10⁻⁷ agreeing.
  This is digit-identical to Gate-42's stored read and to the
  phase's C-392-1 control (both +3.4041776408044866×10⁻⁷):
  **ratio 1.000000**. The gate builder carries Procaccia's
  a-block, q, r_m onto the 12-mode basis with c = 0; the member
  is basis-independent (φ = exp(0) = 1), and the digit identity
  confirms it.
- **y_his @ β = 0.1364:** see C-1 (§1). The verdict audit remains
  legal there; the screen rates the design at β_crit =
  0.136328125 (bracket [0.1359375, 0.13671875], both masks —
  Gate-42's exact read), so 0.1364 is above the rated speed.
  The control survives as a calibration of the gate machinery;
  its second half survives only in the rating sense recorded in
  C-1.
- **The convicted Phase-386 Stage-1 artefact** on the gate's
  screen: **0.174609375** under the old core mask,
  **0.120703125** under the extended mask — Gate-42's conviction
  values exactly. The extended mask was in force from the start
  of 392; no artefact occurred in the phase, and none is needed
  for its claims.
- **E2-1 @ β = 0.191796875: LEGAL** — worst SEC
  **+7.075488×10⁻⁸ @ r = 6.0**, 13.4× floor, Type-I 1.000 both
  spacings, audit4 +5.407155×10⁻⁸ agreeing: Gate-44's gate digits
  reproduced exactly (its §2: +7.075488×10⁻⁸, +5.407155×10⁻⁸).

## §7 Quotable claim set

> **G51-A (construction and controls).** The graded family of
> Gate-42, at the 12-spline grading basis of Phase 391 (knots
> [R₁,R₁,R₁, linspace(R₁,R₂,10), R₂,R₂,R₂]; φ = exp(Σⱼ cⱼBⱼ),
> j = 1..12) inside the same (10,20) configuration class
> (R₁ = 10.0000162, R₂ = 19.9997787, W = 3.6328174,
> M = 6.11288573784887775, p_r ≡ 0 rule, source-derived shift),
> with Phase 392's R-W coefficient box (c₁, c₉ widened to
> ±3.375), is reproduced by an independent gate builder
> (RW-5 chain reads ρ_max, λ, k identical to the phase's stored
> reads; M to 3×10⁻¹⁵ relative). Its c = 0 member remains
> Procaccia's step design, fully legal at β = 0.1363 under the
> common bars (worst SEC +3.404178×10⁻⁷ at r = 5.0, 109.5× the
> FD floor, Type-I 1.000, second path agreeing; ratio 1.000 to
> Gate-42's stored read), the gate's screen rates that member
> at β_crit = 0.136328125 under both masks, and the extended-
> mask discipline convicts the Phase-386 artefact at
> β_crit = 0.120703125 (0.174609375 under the old mask), on the
> gate's own instruments. The Phase-391 best E2-1 (hash
> 61679383…) remains legal at β = 0.191796875 (worst SEC
> +7.075×10⁻⁸ at r = 6.0, 13.4× the FD floor, second path
> agreeing).
>
> **G51-B (graded-class best, raised, with its fence).** In the
> continuously graded-density category of that configuration
> class, the best verified speed is now **β = 0.192578125**,
> held by two configurations of the 12-spline exponential
> family — RW-5 (vector hash 44719b50…) and RW-1 (vector hash
> afcde914…) — RW-5 fully legal at β = 0.192578125 under the
> common bars on independent gate machinery (worst SEC
> +6.056×10⁻⁷ at r = 3.75, 106.5× the FD floor, Type-I
> fraction 1.000 at both spacings, audit4 second path
> +6.050×10⁻⁷ agreeing), with failure bracket
> β = 0.195078125 (inner-ramp SEC −1.032×10⁻⁵ at r = 9.75,
> compound failure). The Gate-44 best β = 0.191796875 is
> superseded **within the graded category only**. **FENCE:
> this is the graded category. The graded-class best does NOT
> contest Procaccia's β = 0.1363 in the step-profile category;
> the programme's verified best in the step-profile category
> remains β = 0.10 (Gate-7); the β = 0.12 conversion in that
> category (Kaggle p1423, spec FINAL per Phase 251) remains
> owed.**
>
> **G51-C (the raise is an interior optimum).** RW-5 lies
> strictly inside the widened R-W box on all 26 coordinates
> (nearest edge: c₁₀, 0.0427 away). Its widened coordinates use
> the room without sitting on it: c₁ = +2.4766 (past the old
> E2 edge +2.25, 0.898 short of the widened edge +3.375) and
> c₉ = −2.1921 (inside even the old box). No further widening
> of this lineage has a price list: the widening lever is
> exhausted at this optimum.
>
> **G51-D (time vs room, priced; the R-16 rider).** Within the
> graded category, Phase 392's two candidate explanations for
> further gains are priced separately on the stored records,
> re-judged: **more time bought nothing** — E2's differential
> evolution, resumed from its stored final population at the
> original 12-mode basis and box, ran 118 further generations
> (7,616 evaluations) to its cap with its best level at exactly
> 0.191796875 at every recorded generation from gen 0, and the
> arm's home ceiling is held by E2-1 itself (hash-identical,
> harvested as T-4); **more room bought the raise** — widening
> exactly c₁/c₉ to ±3.375 bought +0.00078125 (0.191796875 →
> 0.192578125, G51-B). **Rider (binding on any quotation of
> the 16-mode arm):** Arm R-16's no-yield is a truncated-run
> statement only — its DE was stopped at generation 106
> (5,114 s, done = False in its staged state) by the phase's
> registered 6 h total pool budget, before its 120-min arm
> cap, with its population mean still rising (0.10242 at
> gen 39 → 0.17787 at gen 106, recomputed from the staged
> population) and its best static at its gen-0 level; it is
> not a verdict on the 16-mode basis, whose population stands
> staged for resumption (FU-P392-2).
>
> **G51-E (the category fence, standing form — G42-E restated
> for the raised set).** The step-profile category (Gate-7)
> fixes the shell density to the flat step member; the graded
> category frees the plateau profile within the same geometry,
> mass, background rule and source chain, and contains the step
> member as its c = 0 point. Speeds are comparable only within
> a stated category: no wording may carry a graded-category
> speed into the step-profile category or vice versa. Scope
> (C12 accounting, as in the phase record): prescribed-geometry
> audits throughout; the required source is the Einstein tensor
> of the prescribed metric, conservation automatic; no matter
> model, formation route or stability is claimed for any row.

**Ruling on the fence (standing), recorded:** Gate-42's ruling,
inherited by Gate-44, stands unchanged: the distinction is
definitional and mechanical (nested design spaces; the binding
mechanism differs), and the raised set changes nothing about it.
The gate audited Phase 392's wording in full (CHECKPOINT392
registration, closure and final synthesis; the memo's quotable
wording and goal accounting; ledger entries 1060–1061 as charged
to this gate): the fence is carried on the face of the verdict
and of the quotable wording, the step-profile standings
(0.1363 / 0.10 / p1423 owed) are restated wherever the raised
number appears, and **no cross-category sentence was found**.
The fence SURVIVES as drawn; G51-E states it in standing form
for the raised set.

## §8 Provenance, goal accounting, artefacts

- **Frame:** VM frame of record only. Laptop not used.
- **Goal accounting (three-goal rule):** Goal 3 (subluminal
  record) — this gate's subject: the graded-category best is
  raised to β = 0.192578125, gate-verified, within its category
  only. Goal 1 (FTL drive/mechanism) — untouched by this claim
  set; no joint pass anywhere in the programme. Goal 2
  (functional wormhole) — untouched; Gate-23 / G27-A stands; no
  traversability claimed.
- **DESK: NO DATA CONTACT** (inherited from the phase record; no
  real-world dataset was consulted by this gate either).
- **Artefacts:** `gate51/work/g51_lib.py` (gate machinery),
  `gate51/work/g51_audits.py`, `gate51/work/g51_screen.py`,
  `gate51/work/g51_records.py`, `gate51/work/g51_summary.py`;
  `gate51/results/g51_records.json` (hash gate, interiority,
  Arm T / Arm R-16 record re-judgements),
  `g51_audits_<subject>.json` (4 subjects), `g51_screen.json`,
  `g51_summary.json` (registered-bar verdict table),
  `g51_audits.log`.
- **Incidents disclosed:** (i) calibration note C-1 — the
  charged control shorthand "0.1364 fails" does not survive as a
  pointwise statement on either instrument; it survives as the
  screen's rating statement, recorded in §1/§6 (a charge-wording
  correction, not a machinery failure; no claim turns on it).
  (ii) The benign builder RuntimeWarning recorded in §1. (iii)
  Direction-sampled diagnostics (shell sampled-NEC, q_max)
  differ from the phase's stored values in the third digit while
  every deciding margin agrees to ≤ 3×10⁻¹³ — C-2, §1. No other
  incidents; all audits completed on first run.
- **No ledger append, no publication, no successor launch** —
  those remain the parent's. Publication of this set, if the
  parent charges it, follows the standing route (bundle → GitHub
  release + Zenodo DOI) and must carry the §7 fence, the G51-D
  R-16 rider, and calibration note C-1's correction of the
  0.1364 shorthand verbatim.
