# GATE-34 — ADVERSARIAL RE-JUDGEMENT OF THE POSITIVE-DENSITY
# PAIR (PHASE 312 + PHASE 313)

Date: 2026-11-24. Adversarial re-judgement, not a phase.
Scope, fixed in advance (`gate34/work/g34_registration.md`):
whether Phase 312's positive-density member (broad ramp
m₀ = +1.0 in the Phase 308 extended class) and Phase 313's
six-mode spinor match at positive density survive
independent attack, and in what wording they may be
quoted. Frame of record: Phase 166 pin, venv python
(numpy 2.5.5 / scipy 1.18.1), float64.
Method: the gate wrote its own machinery throughout —
`g34_lib.py` (profiles from their definitions; Einstein
assembly by chain-rule derivative operators + einsum
tensor calculus; ADM Eulerian frame from its definition;
own worst-null), `g34_fd.py` (finite-difference guard
assembly), `g34_spinor.py` (Dirac stress builder from the
field definitions; pairwise fast path validated against
the direct builder; own optimiser, own starts). The
SAMPLER-M margin functional is the protocol's definition
(programme machinery predating both phases), applied to
the gate's own tensors. The gate does not repair what it
breaks; nothing here broke.

## VERDICT

- **All four claims SURVIVE** (claim set in §5). Every
  deciding number of both phases was reproduced by the
  gate's independent machinery at ≤ 1×10⁻¹⁷, and the two
  attacks that could have shrunk the claims — the site
  rule's coverage on the new background (Item 2) and the
  match's structural robustness (Item 3) — both closed
  in the claims' favour, at the scopes stated.
- **Item 2 certifies one notch beyond the phases'
  literal wording.** Phase 312/313 claimed positivity
  only "at the four binding sites." The gate's volume
  adversary (129,042-point scan + continuum polishes,
  SAMPLER-M evaluated on every negative-density locus)
  finds NO binding-grade locus with ρ_req < 0 anywhere
  in the shell, at any of the three registered binding
  grades. All negative-ρ loci are confined to the strip
  r ∈ [10, 10.5] where M ≡ 1 (the ramp has not risen;
  Phase 295's two-function identity still governs
  there), with |ρ| ≤ 2.6×10⁻⁷ and NEC no more binding
  than −4.9×10⁻⁴. The binding-site claim may therefore
  be quoted with the certification sentence of §5 —
  and still NOT as pointwise positivity (§5, fence 1).

## §1. Controls (all PASS, run before any re-judgement read)

- **G34-C1 (two-function limit):** the gate assembly at
  M ≡ 1 reproduces Phase 295's factorisation
  −β²S′²(1−n_x̂²)/(32πα²) at the Gate-30 winner's four
  Phase 293 sites to max diff **3.2×10⁻¹⁹** (bar 1e-12).
- **G34-C2 (FD guard):** the gate's analytic That agrees
  with a finite-difference assembly (metric values only)
  at the four sites + 12 off-site points to 7.4×10⁻⁷ at
  h = 0.01 (2.2×10⁻⁶ at h = 0.02), and to **2.7×10⁻⁷**
  after Richardson extrapolation of the O(h²)
  mixed-partial stencil — the FD truncation class, two
  orders below the smallest deciding density
  (6.5×10⁻⁵). No conceptual error in the assembly.
- **G34-C3 (split audit):** the gate's R/Q_K split
  reproduces Phase 312's stored per-site R/(16π), R1,
  R2, Q_K at **diff 0.0**; the split total reproduces
  16π × (gate ρ) to 3.0×10⁻¹⁹.
- **G34-C4 (spinor builder):** on Phase 313's stored
  winning modes, the gate builder reproduces the stored
  spinors from the stored χ at diff 0.0, the stored
  per-site direct residuals to ≤ **9.2×10⁻¹⁷**, the
  stored densities to ≤ 2.1×10⁻¹⁶, Dirac residuals
  ≤ 8.5×10⁻¹⁷; the pairwise fast path agrees with the
  direct builder to 1.1×10⁻¹⁶.
- **Record reproduction:** the gate's That at the four
  site points reproduces `p313_targets.json`'s stored
  tensors to max component diff **8.7×10⁻¹⁹**; the
  frame-free normal contraction T(n,n) agrees with
  That[0,0] at diff 0.0.

## §2. Item 1 — the member, independently re-read

The gate's SET-244 read of the broad-ramp m₀ = +1.0
member reproduces Phase 312's stored set read on every
statistic: Type-I count **1336** (exact), SAMPLER-M NEC
min **−0.0031268695933069223** (stored
−0.003126869593306922), ρ min **−7.561242105046518×10⁻⁸**
(identical), medians identical. The gate's own adversary
polish lands on the identical S1 point
(3.5270717698283187×10⁻⁶, 10.50456804584383,
6.444514430846971), r = 12.323867740249835, and the
gate-derived S2/S3/S4 (SET argmin / Type-I argmin /
r ≥ 15 argmin under Phase 293's rule) are the stored
sites point-for-point. Depth: gate
**−0.0011802747430460965** vs stored
−0.0011802747430460956 (diff 9×10⁻¹⁹). Per-site reads
(gate; stored values identical at ≤ 1×10⁻¹⁷):

| site | r | ρ_req | NEC (SAMPLER-M) | NEC (exact pointwise) | Type-I | R/(16π) | Q_K/(16π) |
|---|---|---|---|---|---|---|---|
| S1 | 12.323868 | +2.168496×10⁻⁴ | −1.180275×10⁻³ | −3.516338×10⁻³ | yes | +2.649137×10⁻⁴ | −4.806409×10⁻⁵ |
| S2 | 11.829268 | +1.521832×10⁻⁴ | −3.126870×10⁻³ | −3.150424×10⁻³ | no | +1.760127×10⁻⁴ | −2.382942×10⁻⁵ |
| S3 | 12.317073 | +2.161432×10⁻⁴ | −1.180145×10⁻³ | −3.517020×10⁻³ | yes | +2.638171×10⁻⁴ | −4.767383×10⁻⁵ |
| S4 | 17.682927 | +6.498030×10⁻⁵ | −1.827601×10⁻³ | −1.830999×10⁻³ | no | +1.133883×10⁻⁴ | −4.840799×10⁻⁵ |

At every site R/(16π) > 0 and exceeds |Q_K/(16π)|: the
density is R-carried, as Phase 312 recorded. **No
deciding number moves.**

## §3. Item 2 — the site rule on the new background

Attack: does the volume hide a locus where ρ_req < 0
that binds as hard as the selected sites — a site the
rule should have picked? Registered binding grades:
(a) SAMPLER-M NEC ≤ −3.126870×10⁻³ (S2's, the rule's
global argmin); (b) exact pointwise NEC ≤
−3.517021×10⁻³ (the sites' most binding exact read);
(c) SAMPLER-M NEC ≤ −1.180275×10⁻³ (the depth) at a
Type-I locus (an S1-class site).

Dense scan (201 radial nodes × 642 dirs = 129,042
points, gate assembly): ρ_req < 0 at **6,431 points,
all with r ∈ [10.0, 10.5]** — exactly the strip where
the broad ramp has not yet risen (M ≡ 1 for r ≤ 10.5),
i.e. where Phase 295's negated-square identity still
holds; the density there is correspondingly tiny
(scan min −2.492×10⁻⁷). SAMPLER-M NEC was evaluated on
**every** ρ < 0 scan point (not a pre-filtered subset):

- most binding SAMPLER-M NEC among ρ < 0 loci:
  **−4.876×10⁻⁴** → grade (a): **0 hits**;
- most binding fib-642 exact NEC among ρ < 0 loci:
  **−4.885×10⁻⁴** → grade (b): **0 hits** (the
  scan-vs-polish gap at the sites is ~7×10⁻⁶, three
  orders below the margin to the threshold);
- most binding SAMPLER-M NEC among Type-I ρ < 0 loci:
  **−1.616×10⁻⁴** → grade (c): **0 hits**.

Continuum polishes confirm the scan: minimising ρ over
the volume gives **−2.552×10⁻⁷** at r = 10.506 (exact
NEC −4.99×10⁻⁴, SAMPLER-M −4.98×10⁻⁴ — weakly binding
by any grade); minimising SAMPLER-M NEC over the volume
reaches only −3.071×10⁻³ (at ρ = +2.475×10⁻⁴), i.e.
does not beat S2's −3.126870×10⁻³; minimising the exact
pointwise NEC reaches −3.5181×10⁻³ in the S1/S3 cluster
(1×10⁻⁶ deeper than S3's stored read, polish class) at
ρ = **+2.138×10⁻⁴ > 0**.

**Certified scope.** On this background, at the
registered thresholds and the gate's scan+polish
resolution: every locus binding at grade (a), (b), or
(c) carries ρ_req ≥ 0, and every ρ_req < 0 locus is
non-binding by a factor ≥ 2.4 in NEC terms against the
weakest binding grade. The binding-site verdict
certifies exactly this. It does not certify pointwise
positivity: the volume minimum of ρ_req is negative
(fence 1, §5).

## §4. Item 3 — the match, independently

**Reproduction.** The gate's optimiser (own builder,
own starts) finds joint four-site fits at the bar from
random starts: stage A (tight tolerances, seed 3401)
best max R = **3.0×10⁻¹⁶** (1/6 starts at the bar);
stage B (protocol-class tolerances, seed 3402) best
max R = **7.1×10⁻¹⁶**, **7/8 starts at the bar**
(residuals 7×10⁻¹⁶ … 1.8×10⁻¹⁴). Phase 313's stored
best is 3.253×10⁻¹³; the gate's fits are at or below
it. Densities at the gate's match:
+2.168496×10⁻⁴ / +1.521832×10⁻⁴ / +2.161432×10⁻⁴ /
+6.498030×10⁻⁵ — the targets' own values. (Start
success is ensemble- and tolerance-dependent — 1/6 vs
7/8 across the gate's own two ensembles, against
Phase 313's 9/9; the existence verdict rests on the
fits found, not on start rates, and both rates are on
this record.)

**Mode-count sweep (gate's own).** 7N real parameters
against 40 residual components (10 per site × 4),
minus one overall-phase gauge:

| N | effective params | best max R | starts at bar |
|---|---|---|---|
| 4 | 27 | 1.537×10⁻³ | 0/6 |
| 5 | 34 | 2.470×10⁻⁴ | 0/6 |
| 6 | 41 | 7.1×10⁻¹⁶ | 7/8 |
| 7 | 48 | 4.578×10⁻¹⁴ | 7/7 |
| 8 | 55 | 1.119×10⁻¹³ | 7/7 |

The transition sits exactly at the counting threshold:
below it the best fits stall five-plus orders above
the bar; at and above it, fits land at
machine-precision residuals from most starts.

**Structural read.** The 40 × 42 Jacobian at the
gate's N = 6 solution has full row rank 40, with
singular values from 3966 down to σ₄₀ = **0.0272**
(σ₃₉ = 0.0370, σ₃₈ = 0.0820) — bounded away from zero.
The solution set is locally a smooth 2-parameter
family and the target lies in the interior of the
superposition's reachable set, not on its boundary.

**Perturbation read.** Each target perturbed
componentwise by symmetric noise of relative size
ε × |That_s|_F and re-fit (warm from the gate winner
+ one fresh start, 2 draws per rung): the bar is
re-achieved at **every** rung — ε = 1×10⁻¹²
(stored-precision class): best max R 3.1×10⁻¹⁵;
1×10⁻⁹: 2.0×10⁻¹⁴; 1×10⁻⁶: 1.4×10⁻¹⁵; 1×10⁻⁴:
9.1×10⁻¹⁵ — with the matched densities tracking the
perturbed targets' densities (positive throughout).
The match survives target noise four orders of
magnitude above the record's own precision class.
**N = 6's success is structural, not a knife-edge
fit.**

## §5. The claim set — the only quotable form

Pointwise supply at four sites of one extended-class
member, in every claim: not a front pass, not a
configuration on the background, not sustainment, not
transport.

- **G34-A — SURVIVES.** *The member.* "In the Phase 308
  extended class (γ_ij = δ_ij + (M−1) n_i n_j) at the
  Gate-30 winner's base pose (β = 1.1), the broad-ramp
  member M = 1 + [U(r;10.5,19.5) − U(r;21,24)]
  (m₀ = +1.0) has depth −1.180275×10⁻³ (SAMPLER-M,
  adversary-polished) and four binding sites under
  Phase 293's rule with ρ_req = +2.168496×10⁻⁴ (S1,
  r = 12.323868), +1.521832×10⁻⁴ (S2, r = 11.829268),
  +2.161432×10⁻⁴ (S3, r = 12.317073), +6.498030×10⁻⁵
  (S4, r = 17.682927), R-carried at every site
  (R/(16π) > |Q_K/(16π)|). Gate-34 reproduced every
  value independently (assembly, frame, polish and
  site derivation all the gate's own; max deviation
  1×10⁻¹⁷)."
- **G34-B — SURVIVES.** *Binding-site positivity,
  certified scope.* "ρ_req ≥ 0 at all four binding
  sites of the G34-A member; and (Gate-34, Item 2) no
  locus in the member's volume that binds at any
  registered grade — SAMPLER-M NEC at S2's
  −3.126870×10⁻³, exact pointwise NEC at
  −3.517021×10⁻³, or SAMPLER-M NEC at the depth
  −1.180275×10⁻³ with Type-I type — has ρ_req < 0.
  All negative-ρ loci lie at r ≤ 10.5, where M ≡ 1,
  with |ρ_req| ≤ 2.6×10⁻⁷ and NEC ≥ −4.9×10⁻⁴."
- **G34-C — SURVIVES.** *The match.* "One six-mode
  Dirac superposition (m = 1, on shell) reproduces the
  G34-A member's full T_req jointly at its four
  binding sites at direct-path residuals
  ≤ 3.253×10⁻¹³ against the 1×10⁻⁹ bar (Phase 313;
  Gate-34's independent optimiser and builder find
  fits at ≤ 7.1×10⁻¹⁶). The threshold is structural:
  N ≤ 5 stalls ≥ 5 orders above the bar, N ≥ 6 closes
  from most starts; the solution Jacobian has full
  row rank (σ_min = 0.0272), and the match re-closes
  under target perturbations up to 1×10⁻⁴ relative —
  four orders above the targets' stored-precision
  class (Gate-34, Item 3)."
- **G34-D — SURVIVES.** *Density at the match.* "The
  matched configuration's density is the target's own
  (full-tensor match): +2.168496×10⁻⁴ / +1.521832×10⁻⁴
  / +2.161432×10⁻⁴ / +6.498030×10⁻⁵ at S1/S2/S3/S4 —
  positive at all four sites, the first mating in the
  drive line whose density leg is decided in the
  supplier's favour. Scope: G34-B's, identically."

**Fences carried verbatim with the set:**
1. *Full-volume fence:* this member's SET-244 ρ
   minimum is −7.561×10⁻⁸ — still negative, at the
   10⁻⁷ level. Positivity is NOT pointwise over the
   shell, for the target or for the match. (Gate-34's
   denser adversary read, reported beside the fence
   per the gate's both-values rule: volume minimum
   −2.55×10⁻⁷, polished, at r = 10.506 — same 10⁻⁷
   class, same conclusion.)
2. *NEC fence:* the member's depth is a negative NEC
   read (−1.180275×10⁻³ SAMPLER-M adversary-polished;
   exact pointwise reads at the sites are more
   negative: −3.516×10⁻³ / −3.150×10⁻³ / −3.517×10⁻³ /
   −1.831×10⁻³ at S1/S2/S3/S4). No energy-condition
   pass, front pass, or drive is implied by any claim
   in this set.
3. *QI fence:* no QI read for any extended-class
   member exists in the record (Phase 312 computed
   none) and none is quoted; no QI price attaches to
   this member or to its match.

## §6. What this gate did not do

No extent construction (fence (b) of Phases 293/313 —
one field holding T_req over the failing region)
was attempted or re-judged; it stands open, now at
positive density, exactly as Phase 313 left it. No
QI machinery was extended to the M(r) class. No other
Phase 312 member was re-judged (the gate's charge
covered the broad-ramp m₀ = +1.0 winner; the other
positive-density members stand at Phase 312's grade).
Nothing was published, forwarded, or appended to the
ledger.

## §7. Reality Desk

`DESK: NO DATA CONTACT — Gate-34 re-judged two
configuration-space results against their own stored
records with independent machinery; no measured
dataset bears on either, and none was manufactured.`
