# GATE-44 — INDEPENDENT RE-JUDGEMENT OF THE PHASE 391 CLAIM SET

**Charge:** ledger entry 1001 (FU-P391-1). **Frame:** VM frame of
record only; the laptop was not used and is not admitted as a gate
instrument (standing pattern of this lineage). **Machinery:** fresh
gate machinery only — `gate44/work/g44_lib.py`, written for this gate
by generalising the gate-lineage builder pattern of Gate-42 to
grading bases of n_c ∈ {8, 12} modes (Phase 391's E2 enrichment
requires the 12-mode basis); tensor instruments gate6/wa_auditor.py
and phase50/p503_lib.audit4, the registered pair. Nothing was
imported from phase391/work or phase386/work. Stored bytes verified
by hash before any audit. float64 everywhere.

## Verdict summary

| Claim | Ruling |
|---|---|
| (a) Raised class best: E2-1 legal at β = 0.191796875, failing at 0.1921875 | **SURVIVES** |
| (b) Step-0 tie: H4, H5, H6 legal at 0.18671875 (five holders); H3 ceiling 0.1859375, Type-I-only failure above | **SURVIVES RESTATED** (the H3 failure-mode wording only; the ceilings and the tie stand as charged) |
| (c) Enrichment yield ladder: E1 +0.003125 → 0.18984375; E2 +0.001953125 → 0.191796875 | **SURVIVES** |
| (d) Controls and no-artefact recalibration | **SURVIVES** |
| (e) The category fence for the raised set (G42-E form) | **SURVIVES** |

The quotable set is §5 (G44-A…G44-E). One calibration note (C-1,
§1) is carried on the face of claim (b): the second path's Type-I
classification at a handful of non-Type-I points in H4/H5 is a
diagnostic, not one of the registered bars — see §1 and §3.

## §1 Machinery and calibrations

**C-0 · Stored bytes (hash gate).** Every audited vector was
re-hashed (sha256 of the float64 tobytes) against its stored record
before auditing: E2-1 `61679383…` ✓, E1-4 `2732e3be…` ✓, H3
`29aa162b…` ✓, H4 `08773ac6…` ✓, H5 `2c64fb21…` ✓, H6 `0d965624…` ✓
(`gate44/results/g44_hashes.json`). The five holders of the Gate-42
best are five distinct vectors (S1 `84c9043e…`, Rank-1 `d1efd424…`,
H4, H5, H6 — all hashes distinct).

**C-0b · The gate builder reproduces both constructions.** At
n_c = 8 the gate builder's construction grid count is 1,200,671 —
Gate-42's count exactly — and its c = 0 chain reads reproduce the
stored reads (M = 6.11288573784887775 by the class convention;
§4). At n_c = 12 the gate builder reproduces Phase 391's stored
E2-1 chain reads at near-roundoff: ρ_max 3.2585104937459165×10⁻⁴
(gate) vs 3.2585104937459127×10⁻⁴ (stored), λ 0.8931410086746383 vs
0.8931410086746355, k 0.024530591100784323 vs 0.024530591100784312,
M equal to the target at 1.5×10⁻¹⁵ relative. E2-1's grading vector
sits on the registered E2 box at exactly the two stored
bound-sitters (c₁ = +2.25, c₉ = −2.25) and nowhere else.

**C-1 · Calibration note — what the second-path bar is (read
before §3).** The registered common bars (CHECKPOINT391, standing
rules, inherited from 386/Gate-42) are: on the primary wa audit at
BOTH spacings — Type-I fraction = 1.000 over significant points,
all four EC margins > 0 and sign-stable, worst ≥ 3× the FD floor,
shell sampled-null NEC min > 0 — **and audit4 agreement on the sign
of every deciding margin**. The deciding margins are the four
eigenvalue EC minima. Gate-42's subjects happened to also show
audit4 Type-I fraction exactly 1.000, so a stricter second-path
condition sat latent in the gate-lineage legality code without
ever deciding a read. It decides nothing here either, once the
registered bar is applied as written — but the gate records the
diagnostics in full (§3): for H4 and H5, audit4 classifies 4 and
2–1 of 1066 significant points respectively as non-Type-I while
every audit4 EC margin and its sampled-NEC minimum over the
significant set stay positive, and the phase's own stored record
shows the identical audit4 Type-I fractions (0.99625 / 0.99812 /
0.99906) with a marginally negative audit4 sampled-NEC diagnostic
(−5.2×10⁻⁸, H4) at those same non-Type-I points where the gate's
sampling reads +2.70×10⁻⁷. Direction-sampled diagnostics at
non-Type-I points disagreeing in sign at the 5×10⁻⁸ scale between
samplings is the C-10 (Gate-43) frame/sampling-convention
territory; every deciding (eigenvalue) margin agrees between the
phase's record, Gate-42's machinery pattern, and this gate's reads
to ~10⁻¹³ or better. No ruling in this gate turns on a sampled
diagnostic at a non-Type-I point.

## §2 Claim (a) — the raised class best: SURVIVES

E2-1 (12-mode lineage, sha256 `61679383…`), full Gate-42 bars on
gate machinery, registered set, both spacings:

- **β = 0.191796875: LEGAL.** wa worst margin SEC **+7.075488×10⁻⁸
  @ r = 6.0**, **13.4× FD floor**, Type-I 1.000 at both spacings
  (fine-spacing worst +5.825×10⁻⁸); audit4 worst **+5.407155×10⁻⁸**,
  Type-I 1.000; q_max 0.9947 @ r = 19.75 (< 1; a direction-sampled
  diagnostic — the phase's stored read is 0.9933 at the same site;
  both subordinate, cf. Gate-42 §1 C-6). Stored digits reproduced:
  phase worst SEC +7.075485×10⁻⁸, audit4 +5.407152×10⁻⁸.
- **β = 0.1921875: FAILS.** wa worst SEC **−7.281066×10⁻⁷ @
  r = 9.75** (stored −7.281067×10⁻⁷), audit4 −7.372241×10⁻⁷,
  Type-I 1.000 — the failure is the inner-ramp SEC margin, as
  charged.

## §3 Claim (b) — the Step-0 tie and H3: SURVIVES RESTATED

**The tie.** H4, H5, H6 each LEGAL at β = 0.18671875 under the
registered bars on gate machinery (wa Type-I 1.000 at both
spacings for all three; worst SEC: H4 **+4.335646×10⁻⁷ @ r = 3.75**
(stored +4.336×10⁻⁷), H5 **+4.495082×10⁻⁷ @ r = 5.0** (stored
+4.495×10⁻⁷), H6 **+2.782551×10⁻⁷ @ r = 3.75** (stored
+2.783×10⁻⁷); audit4 deciding margins positive for all three —
H4 +4.331310×10⁻⁷, H5 +4.419619×10⁻⁷, H6 +2.776850×10⁻⁷ — sign
agreement met). With S1 and Rank-1 (Gate-42), **five distinct
subjects hold β = 0.18671875**. The C-1 diagnostics for H4/H5
(audit4 Type-I 0.99625 / 0.99812–0.99906) are recorded in §1 and
do not touch any registered bar.

**H3.** LEGAL at its ceiling **β = 0.1859375** (worst SEC
+4.700812×10⁻⁷ @ r = 3.75, stored +4.701×10⁻⁷; Type-I 1.000 both
spacings; audit4 +4.696669×10⁻⁷). At 0.18671875 it fails, and the
failure-mode wording is restated for exactness:

> **Restated failure mode (replaces "Type-I-only" in the phase's
> wording):** H3 fails at β = 0.18671875 on the Type-I clause of
> the primary audit at the fine spacing alone (fraction
> **0.99719**, the stored figure exactly; coarse spacing 1.000),
> with **every EC margin positive at both spacings** (worst
> +4.690×10⁻⁷). The three non-Type-I points sit at the r = 16.3
> flux site (q_max 1.00025 > 1 there) and carry a marginally
> negative fine-spacing shell sampled-NEC (−3.6×10⁻⁸) — the same
> flux-clause event seen from the sampled side, not an EC-margin
> failure.

The ceiling, the tie, and H3's exclusion from the holders stand
exactly as charged.

## §4 Claims (c) and (d) — the ladder, the controls, the recalibration: SURVIVE

**(c) Enrichment yield ladder.** The enrichments are as registered
in CHECKPOINT391 §Step 1 *before* the search ran (E1: coefficient
box widened ×1.5 at the bound-sitters; E2: the 12-mode basis on
knots [R₁³, linspace(R₁,R₂,10), R₂³]) — verified against the
registration text and against the audited vectors (E2-1's
bound-sitters are exactly the E2 box's, §1 C-0b). Rungs re-audited
on gate machinery: Gate-42 best 0.18671875 (§3) → **E1-4 LEGAL at
0.18984375** (worst DEC +1.150958×10⁻⁷ @ r = 16.6, stored
+1.150958×10⁻⁷; audit4 +1.174142×10⁻⁷; Type-I 1.000), failing at
0.19046875 (DEC −9.320041×10⁻⁷ @ r = 16.6, stored −9.320040×10⁻⁷)
— **E1 bought +0.003125** → **E2-1 LEGAL at 0.191796875** (§2) —
**E2 bought a further +0.001953125**. Ladder total +0.005078125
over the Gate-42 best, every rung a home-grade audit, no screening
number anywhere in the chain.

**(d) Controls and recalibration.** y_his (c = 0) LEGAL at
β = 0.1363 on gate machinery: worst SEC **+3.404178×10⁻⁷ @
r = 5.0**, **109.5× FD floor**, Type-I 1.000 both spacings,
audit4 +3.395770×10⁻⁷ — **ratio 1.000** to Gate-42's / Gate-7's
stored read. On the gate's own FD screening instrument
(repaired-radii × 26 directions, Phase-73 two-number score,
bisection to ≤ 0.0008): β_crit(y_his) = **0.136328125** (bracket
[0.1359375, 0.13671875]) under BOTH masks; the convicted Phase-386
Stage-1 artefact reads **0.174609375** under the old core mask and
**0.120703125** under the extended mask (brackets identical to
Gate-42's and to 391's stored recalibration), and on the extended
set its score at 0.1363 is −7.042831×10⁻⁶ (SEC @ r = 7.0) — the
Gate-42 conviction value. The extended mask was in force from the
start of 391; no artefact occurred in the phase, and none is
needed for its claims.

## §5 Quotable claim set

> **G44-A (construction and controls).** The graded family of
> Gate-42, generalised as registered in Phase 391 to a 12-spline
> grading basis (knots [R₁,R₁,R₁, linspace(R₁,R₂,10), R₂,R₂,R₂];
> φ = exp(Σⱼ cⱼBⱼ), j = 1..12) inside the same (10,20)
> configuration class (R₁ = 10.0000162, R₂ = 19.9997787,
> W = 3.6328174, M = 6.11288573784887775, p_r ≡ 0 rule,
> source-derived shift), is reproduced by an independent gate
> builder at near-roundoff (E2-1 chain reads: ρ_max, λ, k agree
> with the phase's stored reads to ≤ 3×10⁻¹⁵ relative). Its
> c = 0 member remains Procaccia's step design, fully legal at
> β = 0.1363 under the common bars (worst SEC +3.404×10⁻⁷ at
> r = 5.0, 109.5× the FD floor, Type-I 1.000, second path
> agreeing; ratio 1.000 to Gate-7's stored read), and the
> extended-mask screening discipline convicts the Phase-386
> artefact at β_crit = 0.120703125 while leaving the c = 0 member
> at 0.136328125 under both masks, on the gate's own screen.
>
> **G44-B (graded-class best, raised, with its fence).** In the
> continuously graded-density category of that configuration
> class, the best verified speed is now **β = 0.191796875**,
> held by E2-1 (12-spline lineage, vector hash 61679383…), fully
> legal at β = 0.191796875 under the common bars on independent
> gate machinery (worst SEC +7.075×10⁻⁸ at r = 6.0, 13.4× the FD
> floor, Type-I fraction 1.000 at both spacings, audit4 second
> path +5.407×10⁻⁸ agreeing), with failure bracket
> β = 0.1921875 (inner-ramp SEC −7.281×10⁻⁷ at r = 9.75). The
> Gate-42 best β = 0.18671875 is superseded **within the graded
> category only**, and is now held by five distinct
> configurations (S1, Rank-1, H4, H5, H6). **FENCE: this is the
> graded category. The graded-class best does NOT contest
> Procaccia's β = 0.1363 in the step-profile category; the
> programme's verified best in the step-profile category remains
> β = 0.10 (Gate-7); the β = 0.12 conversion in that category
> (Kaggle p1423, spec FINAL per Phase 251) remains owed.**
>
> **G44-C (H3's ceiling, restated failure mode).** Harvest member
> H3 (hash 29aa162b…) is fully legal at β = 0.1859375 and fails
> at β = 0.18671875 on the Type-I clause of the primary audit at
> the fine spacing alone (fraction 0.99719), with every EC
> margin positive at both spacings; its three non-Type-I points
> sit at the r = 16.3 flux site (q_max 1.00025) and carry a
> marginally negative fine-spacing sampled-NEC (−3.6×10⁻⁸) — the
> same flux-clause event, not an EC-margin failure.
>
> **G44-D (enrichment yield).** Within the graded category the
> gain over the Gate-42 best decomposes by enrichment, each rung
> verified legal at the stated β and failing at its stated
> bracket on gate machinery: widened coefficient box (E1)
> 0.18671875 → 0.18984375 (E1-4, hash 2732e3be…; bracket
> 0.19046875), a further +0.003125; 12-spline basis (E2)
> 0.18984375 → 0.191796875 (E2-1; bracket 0.1921875), a further
> +0.001953125. Both enrichments were registered before the
> search that ran them.
>
> **G44-E (the category fence, standing form — G42-E restated
> for the raised set).** The step-profile category (Gate-7)
> fixes the shell density to the flat step member; the graded
> category frees the plateau profile within the same geometry,
> mass, background rule and source chain, and contains the step
> member as its c = 0 point. Speeds are comparable only within a
> stated category: no wording may carry a graded-category speed
> into the step-profile category or vice versa. Scope (C12
> accounting, as in the phase record): prescribed-geometry
> audits throughout; the required source is the Einstein tensor
> of the prescribed metric, conservation automatic; no matter
> model, formation route or stability is claimed for any row.

**Ruling on the fence (claim e), recorded:** Gate-42's ruling
stands and is inherited: the distinction is definitional and
mechanical (nested design spaces; the binding mechanism differs),
and the raised set changes nothing about it. The gate audited
Phase 391's wording in full (CHECKPOINT391 registration, closure
and final synthesis; the memo's quotable wording and goal
accounting; ledger entries 999–1000 as charged to this gate):
the fence is carried on the face of the verdict and of the
quotable wording, the step-profile standings (0.1363 / 0.10 /
p1423 owed) are restated wherever the raised number appears, and
**no cross-category sentence was found**. The fence SURVIVES as
drawn; G44-E states it in standing form for the raised set.

## §6 Provenance, goal accounting, artefacts

- **Frame:** VM frame of record only. Laptop not used.
- **Goal accounting (three-goal rule):** Goal 3 (subluminal
  record) — this gate's subject: the graded-category best is
  raised to β = 0.191796875, gate-verified, within its category
  only. Goal 1 (FTL drive/mechanism) — untouched by this claim
  set; no joint pass anywhere in the programme. Goal 2
  (functional wormhole) — untouched; Gate-23 / G27-A stands; no
  traversability claimed.
- **DESK: NO DATA CONTACT** (inherited from the phase record; no
  real-world dataset was consulted by this gate either).
- **Artefacts:** `gate44/work/g44_lib.py` (gate machinery),
  `gate44/work/g44_audits.py`, `gate44/work/g44_screen.py`;
  `gate44/results/g44_hashes.json`, `g44_audits_<subject>.json`
  (7 subjects), `g44_summary.json` (registered-bar verdict table),
  `g44_screen.json`.
- **No ledger append, no publication, no successor launch** —
  those remain the parent's. Publication of this set, if the
  parent charges it, follows the standing route (bundle → GitHub
  release + Zenodo DOI) and must carry the §5 fence and the
  G44-C restated failure mode verbatim.
