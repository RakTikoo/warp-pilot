# CHECKPOINT 207 — integration

Date: 2026-11-23. Registration: `phase207/REGISTRATION207.md` (written
before any Phase 207 computation). Frame of record: Phase 166 pin,
Gate-19-corrected tensor, venv python. All four items executed with
controls first; every verdict-carrying number recomputed by an item
checker from the results files (45/45, 72/72, 19/19, and the item-4
audit table respectively). No ledger append, no launches, no contact.

## VERDICTS FIRST

1. **P207-1 (P-DIR-T2 march): DIRECTOR IS A t = 0 PATCH — PATCH WITH
   EXTENSION.** The form-vs-substance anatomy is the item's headline
   and is stated without softening: under the corrected prescription
   the director arm meets EVERY throat clause bar on the whole
   [0, 0.5] — NEC_φ/DEC_φ never fail (worst +0.004542169502404825 at
   t = 0.5, vs the baseline's first failure at t = 0.400 and worst
   −0.6297872673028908). The registered SUSTAINED form is nevertheless
   not available, because one registered bar fails: the refinement
   gate reads 5.8263602620289845×10⁻⁶ against the 1×10⁻⁶ bar — and
   that value is the BASELINE march's own gate value, reproduced by
   the κ = 0 control arm to 2.2×10⁻¹⁶ and carried per-clause by
   NEC_ρ/DEC_ρ, the clause the director shifts by identically zero.
   The director is therefore not the failing bar's carrier; the gate
   failure is inherited from the P169-1(f) march's discretisation.
   Deciding follow-up named: a third-grid study of the base march
   (κ = 0) to decide whether the gate value is a grid artefact of the
   baseline or a property of the pose.
2. **P207-2 (p2052 re-judgement): RE-JUDGEMENT CONFIRMS.** Full-scan
   floors as home set reads: direction (a) grouped max
   0.33359735790526734; direction (b) grouped max
   0.30988004951050263. Full depth bought 4.53×10⁻⁶ on (a)
   (effectively nothing) and 0.0013872152028245877 on (b) (real but
   small). No headline point: B2 is closest, short of grouped max
   < 0.30 by 0.00988004951050263, passing legality, discipline and
   densified survival.
3. **P207-3 (mode-sum C1b): ANATOMY NAMED, NO REPAIR YET.** The
   failure is kernel defects in BOTH subtractions as coded — not
   tail-fit non-convergence and not h-resolution. The scheme as coded
   cannot reproduce THA at any cutoff. Production reads remain void.
4. **P207-4 (phase167 erratum): ERRATUM WRITTEN, NO DECIDING READ
   AFFECTED.** `phase167/ERRATUM_UTILDE.md` is on disk; the engine
   file is deliberately unedited.

## ITEM 1 — P-DIR-T2 AND THE MARCH, RE-DECIDED

Controls, in registered order, all PASS. C-SYM under T2: the symbolic
identity (∇n)² = c_m^(T2) holds for m = 1 and m = 2, numeric grid
identity ≤ 1.5×10⁻¹¹ over t ∈ {0, 0.125, 0.25, 0.375, 0.5};
∇_ρ̂n = ∇_θ̂n = 0; averaged stress diagonal; no momentum content; T2
reduces to Phase 202's c_m at t = 0 with max diff 0.0 (the P205-1
refusal is discharged — the corrected profile is the posed director's
actual stress). C0: Phase 202's seven minima at κ = 0.3 and the κ = 0
datum set reproduced with max abs diff 0.0; ũ_true(θ*) exact;
J['Ah'] ≡ 0 at t = 0. C1: the κ = 0 arm reproduces P169-1(f) exactly
(per-instant clause minima max diff 0.0 over 21 instants; first
NEC_φ failure t = 0.400; worst −0.6297872673028908; worst mom
3.608224830031759e-16; S(θ*) 0.431250 → 1.058131). C2: one march
state consumed by both arms; θ*(t) and momentum channels identical,
max diff 0.0.

March (FULL, home-short, 49.2 s; no package needed): director arm
(m = 1, κ = 0.3) — no NEC_φ/DEC_φ failure on [0, 0.5]; worst
NEC_φ = DEC_φ = +0.004542169502404825 at t = 0.5 (same-instant shift
vs control +0.6343294368052956); worst clause overall +0.004542;
worst NEC_ρ/DEC_ρ +0.024846 at t = 0.5 (a Δ ≡ 0 clause holding on
the uncontrolled S trajectory, as the registration anticipated);
momentum worst 3.61×10⁻¹⁶; flare and domain regularity pass at every
instant; FD second-path sign agreement at all 5 registered instants.
The one failing bar is the refinement gate (above). Checker 45/45.
Record: `phase207/results/p2071_memo.md`, `p2071_results.json`;
`phase207/work/p2071_engine.py` (new module; protected files
byte-identical before/after, md5-verified), `p2071_run.py`,
`p2071_check.py`.

Fences carried from the registration: sector superposition at the
channel-read level; per-instant ZAMO re-pose (no ṅ terms, no director
dynamics); the p1592 gating clause would have applied to any
sustained-form claim and is not triggered.

## ITEM 2 — p2052 HOME RE-JUDGEMENT

Controls in a fresh home process: ALL PASS, every diff 0.0 (c188
ξ′≡0; Phase 200 quadratic; s1881; R-DISC; both local floors
(a) 0.33360189190103595 and (b) 0.3112672647133272 re-read at home).

Deciding rows, re-read at home from stored parameters only (set
reads): A2 best feasible (fixed c188; a = 209.77147156834883,
b = −402.337211727546): grouped max 0.33359735790526734, median
0.13420781142863725, legality 0.5357142857142857 /
0.5218253968253969, all discipline clauses pass, densified
0.5660981137016052 (kernel diff 2.7×10⁻¹⁵; the worst-idx flip
53 → 47 is a near-tie, rel₅₃ within 1.05×10⁻¹³ of the max). A1
cross-check: 0.33360189190103595 — exactly the local (a) floor.
B2 best disciplined-legal (stored c; a = 264.76201780516345,
b = −448.01250001545833): grouped max 0.30988004951050263, median
0.143465342493379, worst idx 53, legality 0.5535714285714286 /
0.5317460317460317, all discipline clauses pass (C* 0.04652,
shadow 0.04696, coverage 8/8, λmin +0.6483, budgets ≤ 1e-9),
densified home re-read 0.5686747891261495 (kernel diff 1.11×10⁻¹³,
the kernel's own control-noise class).

Densified base: home recomputation from c188 = 0.5823609867395406
(diff 0.0 vs registered). The laptop B2 block's quoted base
0.8873403305593545 was computed on the candidate's own braiding
profile at ξ′ = 0, not on c188 — flagged here so the kernel number
is never quoted as the base; the home base governs, and B2 survives
against it regardless. Headline test: not met by any point — A2, A1
and B2 each pass legality, discipline and densified survival and
fail only grouped max < 0.30. Checker 72/72. Record:
`phase207/results/p2072_memo.md`, `p2072_results.json`,
`p2072_check.json`; `phase207/work/p2072_driver.py`,
`p2072_checker.py`.

## ITEM 3 — THE MODE-SUM'S C1b FAILURE ANATOMY

Verdict: ANATOMY NAMED, NO REPAIR YET. The deciding defects are in
`phase200/kaggle/p2003_modesum_kernel.py` as coded:

- **D-A (deciding, subtraction A; lines 300–309).** The counterterm
  subtracts a box-averaged spectral mean, amp = w/(2L r₀²) with
  corr = 1 − V_t/(2ω²) + 3V_t²/(8ω⁴), from POINTWISE throat values:
  alternate modes have an exact node at the throat (pointwise
  factors ~1e-26 against a mean subtracted from every mode), and the
  1/ω² expansion is applied in its forbidden region (fraction of
  modes with ω² < V_t: 0.26 at ℓ = 8 → 1.00 at ℓ ≥ 32; corr_max
  grows to 4.0×10³ at ℓ = 64) while bare throat contributions
  collapse by tunnelling (B-channel bare 1.6×10⁻⁵⁰ at ℓ = 64 vs
  counterterm 1.04×10⁵). Renormalised per-ℓ increments therefore
  GROW (D-channel 467 → 5.44×10⁶, ℓ = 8 → 64), reproducing the
  harvested −10⁷…−10⁸ scale and sign.
- **D-App (subtraction A, separable; lines 306–311).** The
  counterterm is subtracted only at j₀ and A″(0) is then
  differenced: measured spike exactly 2·CT_A/h² (at ℓ_max = 4:
  coded App 1242.68 vs bare −0.340; ratio 1.0000000000000002). This
  explains NEC_ρ's ×3.079 worsening under h-halving — and
  contributes nothing to NEC_φ (App cancels identically in the
  channel algebra), proving a D-App-only repair cannot pass C1b.
- **D-B (deciding, subtraction B; lines 202–205, 227–232,
  250–260).** The reference problem is not locally matched (line 205
  omits the (1−2ξ) term; R_ref = +2/r₀² vs the background's
  −2/r₀²) and the mutual spectrum truncation silently discards the
  bare spectrum (reference counts fall 230 → 133 by ℓ = 24 and to 0
  at ℓ ≥ 32), leaving per-ℓ residuals growing to −40.14 by ℓ = 24
  and a cumulative ~−1.7×10³. Separately, the finite local
  counterterm difference promised in the kernel's own comments is
  never added anywhere in the code (real, but not size-deciding:
  no ~10⁻⁴-scale term explains −1.7×10³).
- **D-kmax (both, non-deciding; lines 211–215).** The
  continuum-dispersion kmax estimate silently truncates at
  ω ≈ 27.42 (ℓ = 0) / 28.03 (ℓ = 16) instead of the registered 30
  (230 modes kept with headroom 0; a direct eigensolve finds 258 /
  251 eigenvalues ≤ ω_max²).

Excluded on numbers: (b) h-resolution — B moves only 4.2% / 12.6%
and A NEC_φ only 0.54% under h-halving while sitting 9.5×10⁶×–
9.3×10¹¹× off target; (a) tail-fit — the per-ℓ sequences are
divergent or mis-set by construction before any fit is applied.
No repair is packaged: the deciding defects require replacing the
coded counterterms with objects the source does not contain (true
WKB mode functions for A; a locally matched reference plus an
explicit finite local term for B), and the two mechanically fixable
defects provably cannot pass C1b alone. The deciding experiment is
specified exactly in `phase207/results/p2073_memo.md`
(eigenvalue-by-value selection + per-ℓ bare/counterterm/renormalised
increment logging as precondition; E-A three counterterm variants at
ℓ_max ∈ {8, 16, 24, 32}; E-B locally matched reference without
min-length truncation plus the explicit local term; gate: decaying
per-ℓ increments in both subtractions before any production C1b
rerun is proposed). Checker 19/19. Record:
`phase207/results/p2073_memo.md`, `p2073_results.json`,
`p2073_verify.json`; `phase207/work/p2073_diag.py`,
`p2073_check.py`. No repaired kernel exists; production NOT rerun;
the harvested production reads remain void under the registered
fence.

## ITEM 4 — THE phase167 DEFECTIVE-HELPER ERRATUM

Verdict: ERRATUM WRITTEN, NO DECIDING READ AFFECTED. The helper is
`utilde_analytic`, `phase167/work/p167_engine.py` line 32: it solves
ũ′ − Φ₀′ũ = Att·Φ₀′/0.8 − Att′, where the −Att′ term lacks the /R00
(= 0.8) of the true-lock ODE. Run in the venv it returns
ũ(θ*) = 0.8883536487880518 exactly; the true-lock anchor (Phase 169)
is ũ_true(θ*) = 1.1412482021558361.

Independent consumer audit (grep of phases 167–174 for the helper,
the defective value, and assigned variables): exactly three call
sites, none in phases 168/170/171/173/174, all non-deciding —
`phase167/work/p1671_verify.py:99` (verification whose clause minima
are cancellation-invariant; Phase 169 RC1(iii) reproduced the datum
to 1.33×10⁻¹⁵ with ũ_true; its other outputs are a channel-coefficient
read and a descriptive ΔJ price, not bars);
`phase167/work/p1672_run.py:77` (control C2 only, lock-form-invariant
per Phase 169; the run's deciding march reads use the marched field,
never the helper); `phase169/work/p1692_pricing.py:41`
(pricing-auxiliary posed-jet evaluations; P169-2's verdict rests on
`p1692_run.py`, which solves ũ_true directly; the one design-feeding
output is base-independent). Phase 167's own deciding reads that had
rested on the defective ũ were already re-based by Phase 169's
record (the anchor itself; the uncompensated t = 0 clause set,
NEC_φ −0.13357121333787725 → −0.3406249999999409; the march re-run,
first failure t = 0.425 → 0.400, worst −0.43254399924557174 →
−0.6297872673028908). The parallel re-implementation in
`p1673_engine.py` is not a helper call and was already corrected by
Phase 172's append-only note. Record: `phase167/ERRATUM_UTILDE.md`
(dated; standing warning included), `phase207/results/p2074_memo.md`,
`p2074_results.json`. The engine file was NOT edited.

## FOLLOW-UP QUEUE (priced/named by this phase)

- FU-P207-1: third-grid study of the BASE march (κ = 0) — decides
  whether the inherited refinement-gate value 5.826×10⁻⁶ is a grid
  artefact of the baseline march or a property of the pose; this is
  now the only bar between the T2 director arm and the registered
  SUSTAINED form at this pose's scope (p1592 gating would still
  apply to any programme-level milestone wording).
- FU-P207-3: the mode-sum deciding experiment exactly as specified
  in p2073_memo.md (E-A / E-B with per-ℓ increment logging); no
  production C1b rerun before its gate passes.
- Item 2 leaves no follow-up of its own: the joint direction's floor
  stands at 0.30988004951050263 (set read), 0.00988 above the
  headline test's grouped-max conjunct.
- Item 4 is closed by the erratum; the standing warning in
  `phase167/ERRATUM_UTILDE.md` is the durable record.
