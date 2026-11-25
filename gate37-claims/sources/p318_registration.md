# P318 — REGISTRATION (FU-P237-1a, the augmented-basis re-solve)

Status: filed by the Phase 318 coordinator at phase start, BEFORE any
Phase 318 computation. Executing phase: Phase 318. Driver names:
`p318_*`; worker outputs under `phase318/work/{control,h203,h34,weights263}/`.
Frame of record: venv python (numpy/scipy/sympy; exact-rational
arithmetic where Phase 259 used it), Phase 166 pin.

## The question

> Phase 259 (K3) compressed the semiclassical identification failure
> to a single residual: at ξ⁰, throat core T^r_r = +16.0 exactly
> (T^t_t = T^θ_θ = 0), decaying 16 / 0.291 / 0.053 / 0.0029 over
> Ellis R = 1/1.5/2/3, with P(ξ) ξ⁰ coefficient 203 vs target 187.
> Which of the named unarbitrated sectors carries it — H{2,0}(3),
> H(6,3)(3), H(6,3)(4), the ξ⁰ assembly weights, or the 263-group
> trace-reduced scalar — and does the fully arbitrated assembly
> pass the core and the Ellis gate at all powers?

## Fixed inheritance (not re-litigated)

- Phase 259's D1 result stands: the residual is NOT a reading
  artefact of the exclusive monomial set under any of seven index
  readings (R0–R6). A NEW reading question, if one arises, is
  stated as new.
- The D2 generic-θ completion gap flagged by Phase 259
  (`results/d2_parts/` holds config_0/config_5 only) is inherited
  AS A GAP, not silently closed.
- Fences: massive-scalar DS stand-in at order 1/m² only; the THA
  Eq. (26) ξ³ defect stands as Phase 241 recorded it; no T_S is
  identified unless the IDENTIFICATION verdict below fires in full.

## Control (must precede any quoted arbitration)

Reproduce Phase 259's assembled record from the stored artefacts:
throat ξ⁰ T^r_r = +16.0 with T^t_t = T^θ_θ = 0; R-decay
16 / 0.291 / 0.053 / 0.0029; core ξ¹/ξ²/ξ³ maxima
3.4×10⁻¹³ / 6.8×10⁻¹³ / 2.8×10⁻¹³; per-power S_T ≤ 2×10⁻¹⁵;
P(ξ) = [203, −1806, 5460, −4200].

## Arbitration (registered order)

(i) H{2,0}(3) — its Stage 1b variation (E2, the Ric□Ric byproduct)
    arbitrated against its print form by Phase 259's standards
    (two-route agreement; conservation on generic jets; the Ellis
    calibration).
(ii) H(6,3)(3) and H(6,3)(4) — derived by the same machinery and
    arbitrated likewise.
(iii) The ξ⁰ assembly weights — re-derived from the source's
    stated assembly rule (Eq. (3.14) as preserved in Phase 259's
    record) and the ξ⁰ bookkeeping checked independently.
(iv) The 263-group trace-reduced scalar — evaluated whether it
    enters the ξ⁰ assembly at all, and at what coefficient.

After EACH sector's arbitration: re-assemble T_S with the
arbitrated substitutions so far and re-read the ξ⁰ core residual.
The record must show which substitution moves the +16, and by how
much.

## Final read

The fully arbitrated assembly against the core and the Ellis gate
at all powers (ξ⁰–ξ³), with conservation per power, at Phase 259's
bars (core ≤ 2.2×10⁻⁸ all powers, ξ²/ξ³ ≤ 1×10⁻¹⁰; gate bars
≤ 1×10⁻⁸; per-power S_T ≤ 1×10⁻¹² assembled / certificate standard
as in Phase 259).

## Verdict forms (exactly one fires; ledger 790)

- **IDENTIFICATION** — core + Ellis gate pass at all powers at the
  record's tolerance class; T_S is identified; the assembled
  tensor's full record is reported.
- **RESIDUAL PERSISTS** — the residual reported in the same
  compressed form (power, component, value, decay profile), the
  suspect list narrowed by the per-sector reads, or the route's
  closure argued from them.
- **SECTOR-BY-SECTOR** — the arbitration completes for some
  sectors and is blocked for others; each sector's verdict and
  its effect on the residual stated; what blocks the remainder
  named exactly.

## Artefacts

This registration; worker memos + JSONs under `work/`; the
stepwise re-assembly record; `CHECKPOINT318.md`;
`results/p318_memo.md`. No ledger append, no launches, no user
contact.
