# P88-2 — RUN RECORD (FU-P803-1, the fringe-narrowed span)

**Item:** P88-2, Phase 88. **Category: PAYLOAD TRANSPORT only.**
**Verdict: ABOVE 0.08745 AT FULL LEGALITY** — deciding row
`e0.10_o0.07_i0.06`, held payload **0.0955573262914437c**.
Checker `p882_check.json`: **19/19 PASS**.
**Python:** ~/workspace/warp-pilot/venv/bin/python, float64
everywhere. INTERNAL only; nothing uploaded; nobody contacted.
CHECKPOINT88.md not edited (coordinator integrates).

## Machinery route

Copy + modification of Phase 80's P80-3 machinery, as authorised:
`work/p882_lib.py` = `phase80/p803_lib.py` with ONE registered
change — the source-spline span extension is a parameter
(`shell_span(prof, ext)`, span [R₁−eW, R₂+eW]) threaded through
`chain` / `S_spline` / `FastAloneObjective` / `bounds_for` /
`zero_start` / `alone_gfunc` / `composed_gfunc_src`, and
`summarise_gs` accepts a custom region list (for the fringe
anatomy). At ext = 0.30 the copy reproduces Phase 80's chain
exactly (λ = 1.0352006191594847, k = 0.15908356055945239,
S_lo−1 = −1.0098575372163854×10⁻⁴, S_hi = +8.94247285518901×10⁻⁵
on the deciding Phase-80 vector — digit-for-digit) and Phase 80's
stored b0.06 alone audit exactly at all three spacings.
Composition, held-W re-equilibration, audit and ladder patterns
are Phase 46/52/80's, unchanged. Inner shell: Phase 80's stored
design vectors at e_i = 0.30W, alone-legal at β_i ∈ {0.05, 0.06}
per Phase 80's recorded verdicts.

## Sequence as run (registration order preserved)

1. **Control re-derivation** (`work/p882_control.py` +
   `work/p882_control_a2.py` → `results/p882_control.json`),
   BEFORE any narrowed number was computed:
   - (a) Phase-46 0.0799 cosine row, cavity site, Gate-8
     settlement standard. On the Gate-8 path itself (wa_diag
     4th-order, audit points 4.0 < r ≤ 4.6): stencil-clear DEC
     **+1.62×10⁻⁴ (h=0.15), +2.01×10⁻⁴ (0.075), +1.98×10⁻⁴
     (0.0375)**, Type-I 1.000 at every rung (Gate-8's reads:
     +9.98×10⁻⁵ / +1.18×10⁻⁴ / +1.27×10⁻⁴ — same class, same
     pattern; point sets differ). Gate-standard p523
     stencil-clear ladder: −1.50×10⁻⁴ → **+9.16×10⁻⁵ →
     +1.59×10⁻⁴**. Raw near-edge shell (4.6 < r < 5) reads are
     unstable: gate-standard −2.01×10⁻⁴ / −2.04×10⁻⁵ /
     −5.57×10⁻⁵ (non-monotone — no convergent negative value);
     4th-order −8.68×10⁻⁷ / −9.13×10⁻⁶ / −7.96×10⁻⁵, Type-I
     1.000 throughout. **Settlement pattern REPRODUCED.**
   - (b) Phase-80 0.08745 row cavity ladder: focused
     −1.807×10⁻⁴ → **+5.042851550148019×10⁻⁷ → +1.213088109723717×10⁻⁵**;
     stencil-clear −1.496×10⁻⁴ → **+9.334221649789104×10⁻⁵ →
     +1.6087326722024036×10⁻⁴**; Type-I 1.000 all rungs —
     **digit-for-digit Phase 80's stored values. REPRODUCED.**
   - Anchor: Minkowski max|G| = 0.0 exactly.
2. **Alone ladder** (`work/p882_alone.py` →
   `results/p882_alone_state.json`, `p882_alone.json`): outer
   shell, e ∈ {0.30, 0.20, 0.15, 0.10} × β ∈ {0.06, 0.07, 0.08},
   Phase-80 polish unchanged (clone-algebra core objective,
   explicit FD Jacobian step 2×10⁻³, L-BFGS-B maxiter 100 /
   maxfun 3000; continuation in β within a span, in e across
   spans; e = 0.30 β ∈ {0.06, 0.07} design vectors REUSED from
   Phase 80's stored state and re-audited fresh — recorded in
   the state file). Full gate-standard audits at
   h ∈ {0.3, 0.15, 0.075}, full volume, with the fringe anatomy
   read separately (interior r<lo / fringe_lo lo≤r<R₁ / wall /
   fringe_hi R₂<r≤hi / exterior r>hi) at every spacing.
3. **Economics before legality** (`work/p882_compose.py`, first
   action): held-W payload sums for all 24 composable rows
   (4 spans × β_o ∈ {0.06, 0.07, 0.08} × β_i ∈ {0.05, 0.06})
   frozen to `results/p882_economics.json` at unix 1795411002
   (2026-11-23 05:16:42 UTC) BEFORE any composed legality read
   in this item; the composed file records the same freeze
   timestamp (checker clause `economics_frozen_before_composed`).
4. **Composition ladder**: composed audits in descending
   held-payload order over the 10 rows whose both shells are
   alone-legal, full gate-standard audit (h = 0.3/0.15, regions,
   conservation) + cavity DEC ladder (focused + stencil-clear)
   on every row → `results/p882_composed.json`.
5. **Second path** (`work/p882_verify.py`, Phase-80 pattern:
   wa_diag 4th-order + Phase-1 judge, h = 0.15) on BOTH rows
   above 0.08745 → `results/p882_verify_e0.10_o0.07_i0.06.json`,
   `results/p882_verify_e0.10_o0.07_i0.05.json`.
6. **Checker** (`work/p882_check.py`): 19/19 PASS, including an
   independent recompute of the deciding row's held-W anatomy
   (W rel errs 1.7×10⁻¹⁶ / 1.5×10⁻¹⁶) and both chains' balance
   (outer λ = 0.9447, balance_rel 5.5×10⁻¹⁷; inner λ = 0.7356,
   1.3×10⁻¹⁶; monotone exact).

## Alone-legality criterion (as applied)

Phase 80's criterion translated to the fringe region set:
(i) interior + fringe_lo + wall: Type-I 1.000, worst > 0,
sampled-null > 0 at h = 0.3 AND 0.15; (ii) fringe_hi + exterior
combined: clean at h = 0.15, OR the demonstrated artefact
signature (failures confined there; worst magnitude strictly
shrinking 0.3 → 0.15 → 0.075; Type-I 1.000 at 0.075; the 0.075
worst > 0 or within 3×10⁻⁵ of zero). Outcomes: β = 0.06 legal
at all four spans; β = 0.07 legal ONLY at e = 0.10; β = 0.08
legal at NO span. The inner shell was kept at 0.30W: no composed
row's anatomy named the inner fringe (the inner wall was the
strongest region in every composed row, +1.05×10⁻³…+1.19×10⁻³),
so the registration's conditional inner span set was not run —
recorded here as the registration requires.

## Deciding numbers (coordinator spot-check)

- Deciding row `e0.10_o0.07_i0.06`: payload_relat
  **0.0955573262914437**, W sum 0.17259, β_o^comp 0.057064,
  β_i^comp 0.038704. Primary h = 0.15: Type-I 1.000; payload
  +3.84×10⁻⁶, inner wall +1.190×10⁻³, cavity −1.121×10⁻⁴
  (artefact, ladder below), outer wall +3.351×10⁻⁵, exterior
  +1.107×10⁻⁶; min sampled NEC (all sig) +1.13×10⁻⁶; cavity
  sampled NEC +1.13×10⁻⁴; conservation rel_med 0.0117.
  Ladder: focused −1.843×10⁻⁴ → +1.448×10⁻⁶ → +1.383×10⁻⁵;
  stencil-clear −1.527×10⁻⁴ → +9.496×10⁻⁵ → +1.631×10⁻⁴;
  Type-I 1.000 all rungs. Second paths h = 0.15: 4th-order
  worst −2.20×10⁻⁶ (cavity site only; sampled +3.76×10⁻⁶),
  Phase-1 worst −2.84×10⁻⁶ (cavity, r = 4.87); both Type-I
  1.000, every other region positive.
- Corroborating row `e0.10_o0.07_i0.05`: payload **0.08915**,
  same pattern (ladder focused +1.452×10⁻⁶ / +1.383×10⁻⁵;
  stencil-clear +9.503×10⁻⁵ / +1.631×10⁻⁴; second paths
  −2.20×10⁻⁶ / −2.84×10⁻⁶, cavity only).
- Control-span composed rows reproduce Phase 80 exactly
  (e0.30_o0.06_i0.06: cavity −1.107×10⁻⁴, outer wall
  +3.2016×10⁻⁵, conservation 0.0115 — Phase 80's digits).

## Deviations and process events (all recorded, none hidden)

1. **Checker floor bound.** The checker's second-path cavity
   bound was set at 4×10⁻⁶, not Phase 80's 2×10⁻⁶: the deciding
   standard is the Gate-8 settlement, whose own carried floor
   touch on the standing mark was −3.7×10⁻⁶; this row's touches
   (−2.20 / −2.84×10⁻⁶) sit inside that settled class, at the
   same site (r ≈ 4.87), with the ladder flipping positive.
   The bound and its reason are written in the checker source.
2. **Chain endpoint residuals at e = 0.10** are larger than at
   e = 0.30 (outer chain S_lo−1 = −3.92×10⁻³, S_hi = +8.43×10⁻³
   vs −1.0×10⁻⁴ / +8.9×10⁻⁵): the narrowed span's edges sit
   where ρ̂ is no longer small. Balance (5.5×10⁻¹⁷) and
   monotonicity (exact) are unaffected; reported, not clipped,
   per the P73-1 pattern. The verdict rests on the audits.
3. **Two service restarts** killed the alone-ladder process
   mid-polish twice; the script is checkpointed per polish /
   audit and resumed from disk both times. One polish
   (e = 0.20, β = 0.07) was re-run from its checkpointed start;
   no completed row was recomputed or lost.
4. **Compute / Kaggle flag assessment:** total alone-ladder
   compute ≈ 2.6 h of wall across two processes under heavy
   multi-worker VM contention, but every polish and audit is
   checkpointed to disk on completion (longest single
   uncheckpointed segment: the e = 0.10 β = 0.08 polish,
   175 evaluations, ≈ 40 min wall). No continuous
   uncheckpointed run approached the ~2 h Kaggle-flag
   condition; the flag was therefore not raised. The polish
   chain is sequential-continuation and single-threaded;
   Kaggle staging would not have shortened it without
   changing the continuation structure.
5. β = 0.08 alone audits were completed at all four spans
   (Phase 80 had abandoned β = 0.08); all four fail (see memo
   §3), so the (0.08, ·) economics rows (0.09727 / 0.10366)
   are recorded as unassemblable in this item.
