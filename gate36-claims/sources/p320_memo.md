# PHASE 320 MEMO — THE SPINOR MATING ON THE POINTWISE MEMBER

Registration: `work/p320_registration.md` (verdict forms
fixed before computation). Driver: `work/p320_run.py`;
recovery: `work/p320_recover.py` (see PROCESS NOTE);
results: `results/p320_results.json`; targets:
`work/p320_targets.json`; winning configuration:
`work/p320_joint_bestfit.json`; independent checker:
`work/p320_check.py` → `results/p320_check_results.json`
(all deciding numbers reproduced at diff 0.0; all four
targets re-derived from p312_lib at max diff 0.0;
verdict independently re-derived — all_pass).

## VERDICT: MATCH AT POSITIVE DENSITY

A single six-mode Dirac superposition (m = 1, on
shell) reproduces the pointwise member's required
stress tensor **in full, jointly at all four binding
sites**, at direct-path residuals ≤ 8.231×10⁻¹⁴ —
~12,000× inside the registered 1×10⁻⁹ bar. The
matched configuration's density is **positive at
every site** — it is the target's own density, to
per-site differences ≤ 3.7×10⁻¹⁵. The target is
Phase 314's headline member (ramp m₀ = +4.00), the
strongest member of the extended class: the one
whose required density Gate-35 certified positive
throughout the closed posed volume at adversary
grade (G35-B). Phase 313 mated the weaker Phase 312
winner at its binding sites; this phase mates the
pointwise member at its binding sites, by the same
protocol, with the counting-threshold ladder and
Gate-34's structural diagnostics added.

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
are ≤ 2.4×10⁻¹⁷.

**CTRL-293 — the protocol reproduces Phase 293's
stored match.** Phase 293's persisted winning
configuration, evaluated by the direct path against
Phase 293's persisted targets, reproduces the stored
per-site residuals, densities and k* contractions at
**diff 0.0 on every field** (max R = 2.876645×10⁻¹²,
the stored value).

**CTRL-313 — Phase 313's match reproduces under
this builder.** Phase 313's persisted winning
configuration against its persisted targets:
stored-U integrity 0.0; per-site residuals,
densities and k* contractions at **diff 0.0** (max
R = 3.253340×10⁻¹³, the stored value).

**CTRL-MEM — the pointwise member's stored reads
reproduce (the charge's control (i)).** At the four
stored site points, That via `p312_lib.T_at_ext` +
`verify_metric.eulerian_that` reproduces Phase 314's
stored per-site reads at **diff 0.0** (ρ_req,
SAMPLER-M NEC, exact pointwise NEC, Type-I flags
S1/S3 True, S2/S4 False) and Gate-35's independent
gate values to ≤ 9.8×10⁻¹⁹ (ρ), ≤ 1.7×10⁻¹⁸
(SAMPLER-M NEC), ≤ 4.6×10⁻¹⁸ (exact pointwise NEC).
S1's SAMPLER-M NEC equals the member's stored depth
−0.0005327658635240826. The SET-244 full read
reproduces Phase 314's stored set summary at **diff
0.0 on every statistic** (n = 6642, Type-I count
2615 exact; NEC min −1.1700067327832923×10⁻³, WEC
min −1.0440691445181194×10⁻², DEC min
−1.0000031873996493, ρ min +8.272455162810697×10⁻⁵).

## ITEM 1 — THE TARGET: T_req AT THE MEMBER'S
## BINDING SITES

Target member: Gate-30 winner's (S, N) verbatim in
the Phase 308 extended class (γ_ij = δ_ij +
(M−1) n_i n_j), profile = ramp, M = 1 +
4.00·[U(r;9,20.5) − U(r;21,24)] (m₀ = +4.00),
β = 1.1. Sites by Phase 293's rule as stored by
Phase 314 and re-derived identically by Gate-35
(S1 the adversary-polished worst site; S2 the
SET-244 SAMPLER-M NEC argmin; S3 the Type-I SET
argmin; S4 the SET argmin over r ≥ 15). Full tensors
persisted in `work/p320_targets.json`:

- **ρ_req is positive at all four sites:**
  +6.263182×10⁻⁴ (S1, r = 12.3134870420811),
  +6.818808×10⁻⁴ (S2, r = 11.829268292682926),
  +6.257630×10⁻⁴ (S3, r = 12.317073170731705),
  +1.172278×10⁻⁴ (S4, r = 17.68292682926829).
- **The target class is mixed, as in Phases
  293/313:** S1/S3 Type-I (Segre I), S2/S4 Type IV.
  At the Type-I sites SAMPLER-M NEC (−5.327659×10⁻⁴
  / −5.327425×10⁻⁴) and the exact pointwise NEC min
  (−1.267419×10⁻³ / −1.266247×10⁻³) differ by a
  factor ≈ 2.4 — both reported, named; at the
  Type-IV sites they agree to ≤ 1.2%.
- **Depth remains a negative NEC read:** the
  member's depth is −5.327659×10⁻⁴ (SAMPLER-M
  adversary-polished). Positivity of ρ_req is not
  an energy-condition pass (Item 3).

## ITEM 2 — THE MATCH

**The ladder (counting threshold 7N − 1 ≥ 40, first
met at N = 6):**

| N | eff. params | best max R (pairwise) | starts at bar |
|---|---|---|---|
| 4 | 27 | 7.317×10⁻⁴ | 0/6 |
| 5 | 34 | 6.215×10⁻⁵ | 0/6 |
| 6 | 41 | **8.231×10⁻¹⁴** | 4/9 |
| 8 | 55 | 8.878×10⁻¹² | 9/9 |
| 12 | 83 | 6.780×10⁻¹¹ | 6/9 |

The transition sits exactly at the counting
threshold, as in Gate-34's sweep on the Phase 312
winner: below it the best fits stall five-plus
orders above the bar; at and above it, fits land at
machine-precision residuals. (Start-success rates
are ensemble-dependent — 4/9 at N = 6 here against
Phase 313's 9/9 on the weaker target; the verdict
rests on the fits found, not on start rates, and all
rates are on this record.)

**The winning configuration** (N = 6, m = 1, warm
start; persisted in full in
`work/p320_joint_bestfit.json`): one six-mode Dirac
superposition, on shell (Dirac residuals
≤ 2.4×10⁻¹⁷), reproduces T_req in full at all four
sites jointly. Direct-path residuals:
7.012×10⁻¹⁵ (S1) / 7.802×10⁻¹⁴ (S2) /
8.231×10⁻¹⁴ (S3) / 1.296×10⁻¹⁵ (S4) — max
8.231×10⁻¹⁴ vs the 1×10⁻⁹ bar, ~12,000× inside it
(and ~4× tighter than Phase 313's match on the
weaker winner). The m = 0 secondary was not
triggered (best m = 1 maxR = 8.2×10⁻¹⁴ ≤ 1×10⁻⁶).

**Density at the match** (= the target's own, to
the reported differences): +6.263182×10⁻⁴ at S1
(diff 9.2×10⁻¹⁶); +6.818808×10⁻⁴ at S2
(3.6×10⁻¹⁵); +6.257630×10⁻⁴ at S3 (3.7×10⁻¹⁵);
+1.172278×10⁻⁴ at S4 (2.6×10⁻¹⁶) — **positive at
all four sites, verified from the direct path, not
assumed.** The matched configuration's fit Segre
types reproduce the targets' per site (I / IV / I /
IV). Per-component anatomy of the best fit: worst
single component 3.6×10⁻¹⁴ (T11 at S3); no component
class resists.

**Pricing:** one global scale |a|² =
0.010204382146024456; per-site implied s² =
0.010204382146057695 (S1) / 0.010204382146075329
(S2) / 0.010204382146005284 (S3) /
0.01020438214602024 (S4) — agreement with |a|² to
≤ 5.1×10⁻¹⁴ absolute at every site, the Phase 257
Leg-3 consistency signature of an exact joint
match. **QI price: NOT QUOTED** — no QI read for
any extended-class member exists in the record
(Phases 312/314 computed none; Gate-35 computed
none) and none is invented (registration, Item 2).

**Diagnostics:** D-a (per-site amplitude refits at
frozen momenta/spins) returns the joint solution at
every site — R = 7.018×10⁻¹⁵ / 7.802×10⁻¹⁴ /
8.231×10⁻¹⁴ / 1.300×10⁻¹⁵, the direct residuals
themselves: one field, one global scale, no
per-site rescaling. D-b was not run (registered:
only if the joint fit stalls above the bar).

**Structural diagnostics (Gate-34 Item 3
standard), at the N = 6 solution:** the 40 × 42
Jacobian of the |That|_F-normalised residual has
**full row rank 40**, singular values from
3.909×10³ down to σ_min = **3.994×10⁻⁴** — bounded
away from zero; the solution set is locally a smooth
2-parameter family and the target lies in the
interior of the superposition's reachable set, not
on its boundary. (σ_min is ~68× smaller than
Gate-34's 0.0272 for the Phase 312 winner — the
worst-direction margin is thinner on this target;
the operative robustness test is the perturbation
ladder, and it passes at every rung.) *Perturbation
ladder:* each target perturbed componentwise by
symmetric noise of relative size ε × |That_s|_F and
re-fit (warm + one fresh start, 2 draws per rung):
the bar is re-achieved at **every** rung —
ε = 1×10⁻¹² (stored-precision class): best max R
8.3×10⁻¹⁴; 1×10⁻⁹: 1.0×10⁻¹²; 1×10⁻⁶: 2.0×10⁻¹³;
1×10⁻⁴: 8.1×10⁻¹⁴ — with the matched densities
tracking the perturbed targets' densities (positive
throughout; minimum +1.172×10⁻⁴ at every rung).
**N = 6's success on this target is structural, not
a knife-edge fit.**

## PROCESS NOTE — DRIVER CRASH AND RECOVERY
## (disclosed on the record)

`work/p320_run.py` crashed in the perturbation
ladder — a TypeError (list/float) in `resid_vec_T`,
a helper added for this phase's structural block —
**after** all controls, all five fit arms, the
winner's direct-path verification, D-a, and the
Jacobian (rank 40, σ_min = 3.9943×10⁻⁴, printed to
the run log) had completed, and after the per-arm
bests and the results-through-best had persisted to
disk. No deciding computation was lost. The tail
(component anatomy, pricing, the perturbation
ladder, the verdict, the bestfit persist) was
completed by `work/p320_recover.py` — the driver's
own tail code verbatim except the one-line
`resid_vec_T` fix, reconstruction of the candidate
table from the persisted per-arm bests, and recovery
controls asserted before any recovered number was
written: the winner's direct residuals, densities
and k* contractions reproduce the executed run's
stored values at **diff 0.0**; the re-derived D-a
values and Jacobian σ_min reproduce the executed
run's logged values at log precision. No fit was
re-run. `p320_run.py` stands on disk exactly as
executed, bug included; the executed run's persisted
results are backed up at
`work/p320_results_executed_run_backup.json`. The
executed run's total wall time is not in the record
(its final dump was the crash's casualty; per-start
times are in `work/p320_run.log`); the recovery
segment's wall time is 593.6 s, recorded as such in
the results.

## ITEM 3 — FENCES

**DESK: NO DATA CONTACT** (a configuration, not a
datum; nothing manufactured).

- **Binding-site scope:** the match is a pointwise
  supply at the four binding sites under the site
  rule — not a configuration on the background, not
  sustainment, not transport. (The TARGET's
  positivity is independently a continuum statement
  at adversary grade (Gate-35 G35-B); that is the
  target's claim at Gate-35's scope. This match's
  scope is the four sites, identically to Phase
  313's.)
- **No energy-condition or front pass is implied:**
  the member's SET-244 EC reads remain violated
  (NEC min −1.170007×10⁻³, WEC min −1.044069×10⁻²,
  DEC min −1.000003, SAMPLER-M) and its depth is a
  negative NEC read (−5.327659×10⁻⁴ SAMPLER-M
  polished; exact pointwise reads at the sites are
  more negative and are quoted named). Those
  violations are Phase 317's question and are
  untouched by this verdict either way. Gate-30
  standings and the extended class's standings are
  untouched.
- What it retires: the **density leg + sourcing
  algebra at the binding sites for the pointwise
  member** — the strongest target in the extended
  class now has a supplier, as the weaker winner did
  (Phase 313). The drive line's sourcing statement
  sharpens to: *the required stress is suppliable in
  full by a healthy classical field at every
  deciding site of both extended-class targets mated
  so far — and for the pointwise member, the target
  itself is the one Gate-35 certified positive
  throughout its volume.*
- **Fence (b) stands open, now on the pointwise
  member**: one field on this background holding
  T_req over an extent — the Phase 315/319 band
  machinery re-based to this member (with its
  coherence scales measured first, Phase 261 Item 2
  pattern) is the named successor pattern. Not built
  here and not claimed.

## NAMED FOLLOW-UPS (none launched)

(i) The extent construction on the pointwise
member's background: band tracking of this member's
T_req by the Phase 315/319 machinery, with the
member's coherence scales measured first.
(ii) A QI read for the extended class (the
machinery extension to the M(r) class that any
pricing of this member or its match requires);
until it exists, no QI price attaches to either.
(iii) Gate-grade re-judgement of this joint match,
if the parent wants the binding-site density-leg
retirement for the pointwise member at gate scope.

## THREE-GOALS ACCOUNTING

(1) FTL drive/mechanism: NO — the spinor mating at
positive density closes the sourcing algebra +
density legs at the pointwise member's binding
sites; Frontier A unchanged; drive step 1
unachieved (the member still fails NEC/WEC/DEC
in-region; no front pass). (2) Wormhole: untouched
this phase. (3) Subluminal record: untouched this
phase (Procaccia β = 0.1363 stands; programme
gate-verified best 0.10).

## FILES

Registration `work/p320_registration.md`; driver
`work/p320_run.py` (+ log `work/p320_run.log`);
recovery `work/p320_recover.py` (+ log
`work/p320_recover.log`); executed-run results backup
`work/p320_results_executed_run_backup.json`;
targets `work/p320_targets.json`; winning
configuration `work/p320_joint_bestfit.json`;
per-arm bests `work/p320_best_N{4,5,6,8,12}.json`;
full record `results/p320_results.json`; checker
`work/p320_check.py` +
`results/p320_check_results.json`; memo
`results/p320_memo.md`. No ledger append, no launch,
no external contact was made by this phase.
