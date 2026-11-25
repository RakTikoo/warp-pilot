# PHASE 313 MEMO — THE SPINOR MATING AT POSITIVE DENSITY

Registration: `work/p313_registration.md` (verdict forms
fixed before computation). Driver: `work/p313_run.py`;
results: `results/p313_results.json`; targets:
`work/p313_targets.json`; winning configuration:
`work/p313_joint_bestfit.json`; independent checker:
`work/p313_check.py` → `results/p313_check_results.json`
(all deciding numbers reproduced at diff 0.0; all four
targets re-derived from p312_lib at max diff 0.0).

## VERDICT: MATCH AT POSITIVE DENSITY

A single six-mode Dirac superposition (m = 1, positive
frequency, on shell) reproduces the Phase 312
extended-class winner's required stress tensor **in
full, jointly at all four binding sites**, at
direct-path residuals ≤ 3.253×10⁻¹³ — ~3000× inside
the registered 1×10⁻⁹ bar. And the matched
configuration's density is **positive at every one of
the four sites**, because this target's own T_req has
positive Eulerian density at every binding site
(Item 1). This is the first mating in the drive line
where the density leg is decided in the supplier's
favour: Phases 293/295 showed the two-function class's
targets demand negative density at their binding
sites by an algebraic identity; Phase 308 broke the
identity in the extended class; Phase 312 found
members whose binding sites demand only positive
density; this phase supplies the strongest such
member's full tensor there.

## CONTROLS (all PASS before any fit was read)

**K1–K4 — the spinor machinery on the stored D1
record** (Phase 261's controls, verbatim): K1 Phase
257's stored match reproduced (R = 1.7677×10⁻¹⁶);
K2 per-site s² table to rel. ≤ 4.5×10⁻¹⁶; K3 phase
machinery vs the direct builder ≤ 9.9×10⁻¹⁴
displaced, 5.3×10⁻¹⁵ at x = 0; K4 stored
contractions ≤ 8.7×10⁻¹⁹. The vectorised S builder
agrees with the verbatim builder to 3.5×10⁻¹⁸. The
Pauli guard held; the winning modes' Dirac residuals
are ≤ 1.45×10⁻¹⁶.

**CTRL-293 — the protocol reproduces Phase 293's
stored match.** Phase 293's persisted winning
configuration (N = 6, m = 1, from
`phase293/work/p293_joint_bestfit.json`), evaluated
by the direct path in this phase's fresh process
against Phase 293's persisted targets, reproduces
the stored per-site residuals (4.535729×10⁻¹³ /
2.206452×10⁻¹² / 2.876645×10⁻¹² / 2.644017×10⁻¹³),
densities and k* contractions at **diff 0.0 on every
field** — the stored match at stored precision,
exactly as registered.

**CTRL-TGT — the extended-class interface.** At the
winner's four stored site points, That via
`p312_lib.T_at_ext` + `verify_metric.eulerian_that`
reproduces Phase 312's stored per-site reads at
**diff 0.0**: ρ_req (all four), SAMPLER-M NEC (all
four), exact pointwise NEC minima (all four), and
the Hawking–Ellis Type-I flags (S1/S3 True, S2/S4
False); S1's SAMPLER-M NEC equals the member's
stored polished depth −1.1802747430460956×10⁻³. The
target assembled here is the extended class's own
tensor in its own Eulerian frame — the same objects
Phase 312 read — not the two-function tensor with a
new density pasted in.

## ITEM 1 — THE TARGET: T_req AT THE WINNER'S
## BINDING SITES

Target member: Gate-30 winner's (S, N) verbatim in
the Phase 308 extended class (γ_ij = δ_ij +
(M−1) n_i n_j), profile = broad ramp, M = 1 +
[U(r;10.5,19.5) − U(r;21,24)] (m₀ = +1.0), β = 1.1.
Sites by Phase 293's rule as stored by Phase 312
(S1 the adversary-polished worst site; S2 the SET-244
SAMPLER-M NEC argmin; S3 the Type-I-restricted SET
argmin; S4 the SET argmin over r ≥ 15):

| site | r | ρ_req = That[0,0] | NEC (SAMPLER-M) | NEC min (exact, k*) | HE type | Segre |
|---|---|---|---|---|---|---|
| S1 polished worst | 12.323867740249835 | **+2.168496×10⁻⁴** | −0.0011802747430460956 | −0.0035163382702022706 | I | I |
| S2 SET argmin | 11.829268292682926 | **+1.521832×10⁻⁴** | −0.003126869593306922 | −0.003150423790303257 | — | IV |
| S3 SET argmin, Type-I | 12.317073170731705 | **+2.161432×10⁻⁴** | −0.0011801454543835454 | −0.0035170200901904285 | I | I |
| S4 SET argmin, r ≥ 15 | 17.68292682926829 | **+6.498030×10⁻⁵** | −0.0018276014032702216 | −0.0018309985991530307 | — | IV |

(Full tensors, points, k* directions and both
samplers' margin sets persisted in
`work/p313_targets.json`.)

Three facts of the target:

1. **The density is positive at every binding
   site.** ρ_req ∈ [+6.50×10⁻⁵, +2.17×10⁻⁴] across
   the four sites — the mirror image of Phase 293's
   target (there ρ_req ∈ [−9.34×10⁻⁵, −5.05×10⁻⁵]).
   Per Phase 312's anatomy the density is R-carried
   at every site: the spatial-curvature piece
   R/(16π) is positive and larger than |Q_K/(16π)|,
   the negated-square remnant. The density leg of
   Item 2 was therefore decided by the target again
   — this time in the supplier's favour.
2. **The target class is mixed, as in Phase 293.**
   S1 and S3 are Type-I tensors (Segre I); S2 and
   S4 are Type IV. At the Type-I sites the two NEC
   reads differ materially and are both reported,
   named: SAMPLER-M reads −0.001180 / −0.001180
   where the exact pointwise worst null direction
   reads −0.003516 / −0.003517 (factor ≈ 3.0); at
   the Type-IV sites the two reads agree to ≈ 0.8%
   / 0.2%. The fit targets the full tensor, so both
   reads are reproduced by it (contractions below).
3. **Depth is still a negative NEC read.** The
   member's depth is −1.180275×10⁻³ (SAMPLER-M
   adversary-polished; Phase 312's record). Positive
   ρ_req at the binding sites coexists with a
   failing NEC — the density is not the binding
   failure of this member; the NEC failure is
   pressure/direction-carried, as it was (inverted)
   for the lapse winner. Nothing in this phase is
   an energy-condition pass.

## ITEM 2 — THE MATCH

Phase 293 protocol verbatim in structure (m = 1;
N ∈ {6, 8, 12}; 1 warm + 8 random starts per arm;
40 targets). Every arm closes:

| N | best max R (pairwise) | starts ≤ 1×10⁻⁹ |
|---|---|---|
| 6 | 3.253×10⁻¹³ (rand1) | 9 / 9 |
| 8 | 2.574×10⁻¹¹ (rand5) | 8 / 9 (rand4 stalled at 3.01×10⁻³) |
| 12 | 2.049×10⁻¹⁰ (rand6) | 5 / 9 |

The mode-count threshold is N = 6 again — the count
that sufficed for the lapse winner suffices for the
extended winner, and it is again the best arm. The
winning configuration (N = 6, m = 1, persisted in
full at `work/p313_joint_bestfit.json`), definitional
direct-path reads:

| site | R_s (direct) | T_fit(k*,k*) | ρ_fit |
|---|---|---|---|
| S1 | 9.817×10⁻¹⁴ | −0.003516338270 | **+2.168496×10⁻⁴** |
| S2 | 2.847×10⁻¹³ | −0.003150423790 | **+1.521832×10⁻⁴** |
| S3 | 3.253×10⁻¹³ | −0.003517020090 | **+2.161432×10⁻⁴** |
| S4 | 7.547×10⁻¹⁴ | −0.001830998599 | **+6.498030×10⁻⁵** |

Max R = 3.253339860306391×10⁻¹³ against the 1×10⁻⁹
bar — ~3000× inside it, ~9× tighter than Phase 293's
match (2.877×10⁻¹²). ρ_fit agrees with ρ_req to
≤ 1.4×10⁻¹³ absolute at every site — the density at
the match IS the target's positive density, as it
must be for a full-tensor match. The fit's per-site
Segre types reproduce the targets' (I / IV / I /
IV). The independent checker recomputes every
residual, density and contraction from the persisted
modes via the direct path only: **diff 0.0
throughout**, and re-derives all four target tensors
from p312_lib at max diff 0.0.

**Diagnostic D-a** (per-site amplitude refits at
frozen momenta/spins): returns the joint solution at
every site (R = 9.8×10⁻¹⁴ / 2.8×10⁻¹³ / 3.3×10⁻¹³ /
7.5×10⁻¹⁴, the joint values) — no amplitude-sharing
failure; one field carries all four sites at one
global scale.

**Pricing.** The winning configuration's global
amplitude scale is |a|² = 0.05698446045985037
(folded normalisation). The per-site implied s²
(Phase 257 Leg-3 form) is 0.05698446046… at **all
four sites**, agreeing with |a|² to ≤ 1.3×10⁻¹⁰
relative — the exact-match consistency identity
holds, as registered. **QI price: NOT QUOTED.** No
QI read for any extended-class member exists in the
record — Phase 312 computed none, the QI machinery
of this line has never been run on the M(r) class —
and none is invented. (Phase 293 could quote its
target's own on-record SAMPLER-A price; no such read
exists here, and the absence is stated rather than
papered over. Named follow-up (iii) in the
checkpoint.)

## ITEM 3 — WHAT THIS DOES AND DOES NOT ESTABLISH

**DESK: NO DATA CONTACT** (the winner is a
configuration, not a datum; no measured data set is
compared anywhere in this phase, and none is
manufactured).

On the drive chain (front pass → full configuration
→ sustainment → transport accounting):

- This phase is a **pointwise supply result at four
  sites** of one extended-class member. It is not a
  front pass (the member's NEC still fails
  in-region — Phase 312's standing, untouched), not
  a configuration (no field on the winner's
  background is constructed), not sustainment, not
  transport. Frontier A is unchanged; drive step 1
  of the main line remains unachieved.
- What it retires: the **density leg at the binding
  sites for this target**, and with it the last
  leg of the mating protocol for the extended-class
  winner. The drive line's sourcing record now
  reads: the spinor sector matches the full
  required stress of **all three** fronts at their
  deciding sites (D1, Phase 257/261; the lapse
  winner, Phase 293; the extended winner, here).
  For the first two, the matched density is
  negative because the targets demand it — Phase
  295's identity makes that a theorem of their
  class. For the third, the target demands positive
  density at its binding sites and the match
  carries exactly that. *The required stress is
  suppliable in full by a healthy classical field
  at every deciding site of every front the drive
  line has posed; where a front's sourcing fails on
  density, the failure is the target's, and the
  extended class contains targets for which it does
  not fail at the binding sites.*
- **Scope fence, stated plainly (Phase 312 fence
  (i), carried identically):** the positivity is a
  binding-site statement under the site rule. This
  member's SET-244 ρ minimum over the shell is
  −7.561×10⁻⁸ — still negative, at the 10⁻⁷ level.
  No pointwise-over-the-shell positivity is claimed
  for the target, and none for the match.
- Phase 253's sign-leg result stands untouched, as
  before: a weaker target (one contraction), not
  promoted or demoted by a tensor match.
- **Fence (b) stands open, now at positive
  density**: a single Dirac field, on the winner's
  background (spin connection, mode mixing), whose
  stress tracks T_req over the whole failing
  region — the Phase 272/275/277 extent machinery
  (segment tracking, patch fits, joining, width) is
  the named successor pattern, now with a
  positive-density target as its object, and the
  winner's coherence scales (Phase 261 Item 2
  pattern) are this line's to measure first. It is
  not built here and not claimed. Its fence is
  unchanged in kind: the extent question decides
  whether one field HOLDS the tensor over the
  region; the density classification at each point
  remains a property of T_req there — and over the
  failing region, unlike at the four binding sites,
  that classification is not yet positive
  everywhere (the SET ρ minimum above).

## NAMED FOLLOW-UPS (none launched)

(i) The extent construction on the extended
winner's background (fence (b) with this phase's
target): coherence-scale measurement first (Phase
261 Item 2 pattern), then segment/patch tracking of
the winner's T_req by the Phase 272/275/277
machinery — decides the tracking leg for the
extended line.
(ii) Gate-grade re-judgement of this joint match,
if the parent wants the binding-site density-leg
retirement at gate scope (extends the Gate-25 /
Phase 293 follow-up pattern to the third front).
(iii) A QI read for the extended class: the
machinery extension to the M(r) class that any
pricing of this member — and hence any QI statement
about the matched configuration — requires. Until
it exists, no QI price attaches to either.

## FILES

- `work/p313_registration.md` — registration +
  verdict forms, written before computation.
- `work/p313_run.py` + `work/p313_run.log` — driver
  (controls K1–K4 / CTRL-293 / CTRL-TGT, Item 1
  extraction, Item 2 campaign, D-a, pricing,
  verdict). Wall 1298.2 s.
- `work/p313_targets.json` — the four sites' full
  tensors, k* directions, both samplers' reads.
- `work/p313_joint_bestfit.json` — the winning
  six-mode configuration in full (momenta, folded
  amplitudes, spinors, Dirac residuals).
- `work/p313_best_N{6,8,12}.json` — per-arm best
  configurations (incremental persistence).
- `results/p313_results.json` — full numeric record.
- `work/p313_check.py` +
  `results/p313_check_results.json` — independent
  checker; all deciding numbers at diff 0.0.

No ledger append, no launch, no external contact was
made by this phase.
