# P207-4 — Memo: phase167 defective-helper erratum (worker, 2026-11-23)

**Verdict (registered form): ERRATUM WRITTEN, NO DECIDING READ AFFECTED**

## What was verified

- **Helper.** `utilde_analytic` in `phase167/work/p167_engine.py`,
  line 32, solves ũ′ − Φ₀′ũ = Att·Φ₀′/0.8 − Att′ by the integrating
  factor — the deciding line is
  `rhs = B.att(th_f) * B.phi0_h(th_f) / R00 - B.att_h(th_f)`:
  the `−Att′` term carries no `/R00` (= 0.8), which is exactly the
  defective lock's bracket. The true-lock ODE (Phase 169 (A1)) has
  `−Att′/0.8`.
- **Verified value.** Running the helper in the project venv
  (bounded, local) gives ũ(θ*) = **0.8883536487880518** exactly
  (interpolated at π/2 on the 2881 grid; also the profile's
  max|ũ|). True-lock anchor (Phase 169): ũ_true(θ*) =
  **1.1412482021558361**.

## Consumer audit (independent, phases 167–174)

Grep for `utilde_analytic`, for `0.8883536487880518`, and for
variables assigned from the helper found exactly **three** call
sites; none in phase168, 170, 171, 173 or 174. Phase 204's
"none did" claim was not copied — each consumer was traced in its
code and phase record:

1. **`phase167/work/p1671_verify.py:99` — non-deciding.**
   Verification (2) puts the same profile both as the Mtt jet and
   inside J_pose, so the compensated t=0 clause minima are
   cancellation-invariant to its value (Phase 169 RC1(iii)
   reproduced the datum to 1.33×10⁻¹⁵ with ũ_true). Verification
   (3) reads channel coefficients, independent of ũ's magnitude.
   The stored ΔJ(θ*) price is defective-based but is not a bar;
   P167-1's verdict rests on the symbolic identity.
2. **`phase167/work/p1672_run.py:77` — non-deciding (control C2
   only).** Same compensated-audit construction; Phase 169 states
   on the record that C2 is lock-form-invariant and does not move.
   The run's deciding march reads use `mtt_field` on the marched
   field, never the helper.
3. **`phase169/work/p1692_pricing.py:41` — non-deciding
   (pricing-auxiliary).** Channel evaluations at posed jets only,
   no march, no lock solve (script's own header). P169-2's verdict
   rests on `p1692_run.py`, which solves ũ_true directly. The one
   pricing output that fed a design choice (Muu sensitivity
   exactly 0.0 → M₂₂ = 0) is base-independent.

Related non-helper finds, documented in the erratum:
`phase167/work/p1673_engine.py` re-implements the same defective
bracket itself (never calls the helper) — its s / t_mu / race
numbers were already corrected by Phase 172's append-only
correction in CHECKPOINT167, with P167-3's verdict standing;
defective-value occurrences in phase169 are comparators /
correction targets, not consumptions; Phase 204 X3 solved
ũ_true directly and only flagged the helper.

## Phase 167 deciding reads — re-based vs still on the helper

Already re-based by Phase 169's record (none of it via the
helper): the ũ anchor (→ 1.1412482021558361), the uncompensated
t=0 clause set (NEC_φ −0.13357121333787725 → −0.3406249999999409;
NEC_θ +0.8039287866621226 → +0.596875000000059), and the
compensated march's deciding reads by true-lock re-run (momentum
discharged, worst mom_θ 3.61×10⁻¹⁶; NEC_φ first failure
t = 0.425 → 0.400, worst −0.43254399924557174 →
−0.6297872673028908). Still resting on the helper: **no deciding
read** — only the descriptive ΔJ(θ*) price in P167-1/P167-2 and
the P1 pricing listing in `p1692_pricing.json`.

## Deliverables

- `phase167/ERRATUM_UTILDE.md` — the erratum of record: helper
  identity (file/function/line), wrong and right values, the
  consumer audit table with per-consumer disposition and
  evidence, and the standing warning (helper must not be used
  for any deciding read; ũ_true is the only anchor; engine file
  deliberately left unedited so stored records remain
  reproducible).
- `phase207/results/p2074_results.json` — the audit table in
  machine-readable form.
- This memo. No pre-existing file was edited; the engine file
  `phase167/work/p167_engine.py` is untouched. No ledger append,
  nothing launched, nobody contacted. INTERNAL only.
