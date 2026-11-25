# CHECKPOINT 259 — FU-P228-2c: direct derivation of the semiclassical source (Décanini–Folacci arbitration)

**VERDICT: K3.** Arbitration succeeded; the assembled T_S fails the core and the
Ellis gate in the ξ⁰ sector only. Per the registration, the published-data route
closes entirely and **FU-P237-1a (augmented-basis re-solve) inherits**, carrying
the priced ξ⁰ anatomy below. No identification is claimed. Iteration 2 was NOT
run and is NOT registrable on this outcome.

Registration: `phase259/work/p2591_registration.md` (Phase 255 draft adopted
verbatim in scope, filled in as Phase 259, filed before any computation).
Frame: venv sympy 1.14.0, exact-rational arithmetic throughout; Part A/B engines
unmodified after calibration (one global machinery fix in Stage 1, recorded in
the Stage 1a memo: P is the gradient w.r.t. lower R_{abcd}).

## What was derived (all exact-rational, DF print units: print H = −E[invariant])

- H(6,3)(1) = −E[R³] — control C1, exact (Stage 1a).
- H{2,0}(1) = variation of R□R (density −(∇R)²) — control, contents exact (Stage 1b calibrator i).
- H(6,3)(2) = −E[R·Ric²], 22 patterns — Stage 1c identification CONFIRMED
  (R□R_ab coefficient +1 programme / −1 print, exactly as recorded).
- H(6,3)(5) = −E[R·Riem²], 63 patterns (Stage 2a).
- H(6,3)(6) = −E[Ric·Riem²], 75 patterns — the UNIQUE genuine Ric·Riem² scalar
  (840-matching enumeration: placements A/B/C identical by Riemann symmetries;
  Stage 2b/2b′).
- H(6,3)(8) = −E[Riem³ cross], 122 patterns; its sibling (chain, 122 patterns)
  is print H(6,3)(7) — Stage 3 calibration, exact (max diff 1.1×10⁻¹² over
  26 points × 3 components). K1 does not fire for any indicted tensor.

Every derived tensor: two-route agreement diff 0 (engine dual-probing +
analytic P), conservation exactly 0 on generic rational jets and |S| ≤ 2.5×10⁻¹⁴
(harness jet route, 26 background points, two paths; FD route Richardson-verified
as pure O(h²) truncation), tr E_alg = L at D=4. Certificates:
`results/p2591_conservation_certificates.json`.

## Arbitration (Stage 3, `results/p2591_arbitration.md/.json`)

- H(6,3)(5): print − derived is EXACTLY PURE-TRACE at every point (at Ellis ℓ=1
  exactly −1·g_ab; deviation ≤3.4×10⁻¹²). The direct sector agrees; the print's
  error is confined to a trace-sector scalar×g_ab term. Not a coefficient or
  sign error.
- H(6,3)(6): differs (max 170.5); verdict secured by conservation (recorded
  print S = +0.4375 at Ellis ℓ=1 vs derived S = 0). Value table qualified by a
  §2-transcription residue in the Stage 3 worker's own (2.29) transcription
  (its S reads +0.234 vs recorded +0.4375); the S-anchored verdict is unaffected.
- H(6,3)(8): differs (max 94.5 vs derived B); print non-conserved (recorded
  S = +0.84375 at ℓ=1), derived certified S = 0. Same transcription-residue
  qualification on values (0.773 vs 0.84375); verdict S-anchored.
- The assembled print−derived difference is ~95% but NOT exactly spanned by the
  exclusive monomial set {m11, m15, m27, m33, m34, m35, m37, m39, m41, t9, t14,
  t15, t17}; the ξ¹ shortfall is real and involves only H(5).

## Assembly (Stage 4, `results/p2591_assembled.json`, `p2591_gate_readout.md`)

Derived (5), (6), (8-B) substituted; seven print tensors kept; Eq. (3.14)
weights print-exact; modes 1/2 cross-checked (max dev 2.91×10⁻¹¹, on the largest
C-family totals only — driver float accumulation; ≤4.6×10⁻¹⁴ on all core points;
no verdict within 3 orders of this noise).

PASSES: core ξ¹ 3.4×10⁻¹³, ξ² 6.8×10⁻¹³, ξ³ 2.8×10⁻¹³ (ξ²/ξ³ bit-identical to
print — no degradation); per-power S_T all ≤ 2.0×10⁻¹⁵ (print: S(ξ⁰) = +0.030556,
S(ξ¹) = −0.200000); forced deficit; Δρ (rel 2.5×10⁻⁸); Δp_t (rel 1.2×10⁻⁸);
ξ¹ fixed on the whole wider set.

FAILS — all ξ⁰, all one number: core ξ⁰ residual at the Ellis throat is exactly
T^r_r = +16.0 (T^t_t = T^θ_θ = 0.0; print was −72.889/−67.556/−72.889), decaying
over Ellis R = 1/1.5/2/3 as 16 / 0.291 / 0.053 / 0.0029; A-family throat 7.0;
wider-set ξ⁰ maxima C 250, E 108, D 7.997. P(ξ) = [203, −1806, 5460, −4200] vs
target [187, …] — only ξ⁰ off, by the same +16 (root 0.869316 vs 0.860358).
NEC roots 0.144365/0.267503/1.421465 vs targets, max dev 0.007904. Δp_r =
1.71996×10⁻⁴ vs 9.158220×10⁻⁵ — the excess is exactly the +16 read at ξ = 1/6
(16/(20160π²) = 8.04×10⁻⁵), at both m·r₀ = 1 and 2. Attribution: the three
substitutions' throat T^r_r moves (+74.667, +2.667, +6.222) sum past the print
residual (−67.556), leaving +16.0 — so the residual also implicates the KEPT
print tensors' ξ⁰ values or the ξ⁰ assembly, not the indicted three alone.

## Discriminators (Stage 5, `results/p2591_discriminators.json`, `p2591_stage5_memo.md`)

- D1 CONCLUSIVE: the ξ⁰ residual is NOT spanned by the exclusive monomial set
  under ANY of seven candidate index readings (R0–R6). Exact-rational rank test
  fails for every reading; LS shortfall after projection 4.53 (R0–R4, identical
  because those readings act on backgrounds through Riemann symmetries / column
  sign flips), 5.54 (R5 cyclic), 3.76 (R6 midswap); fixed-print-coefficient check
  fails by 1147.78–2563.56. No index-reading artefact of the exclusive set
  produces the residual. K4 does not fire.
- D2 PASS on completed configs: exact quadrupolar Ellis deformation
  A(ℓ,θ) = (ℓ²+1) + ε₂P₂(cosθ), ε₂ ∈ {1/10, 1/5}; at ℓ=0 equator (genuinely
  non-SSS) derived H(5), H(6), H(8-B) and control H(7)-A are conserved with
  S = 0 EXACTLY on all components; localisation confirmed off SSS (A = print
  H(7) exactly; H(5) difference still exactly pure-trace; (6)/(8) differences
  persist in character). COMPLETION GAP (flagged, not a verdict input):
  generic-θ configs were still running at phase close — `results/d2_parts/`
  holds config_0/config_5 only; ℓ=1 configs were triage-stopped by the worker.

## Inheritance for FU-P237-1a (the named successor)

1. The failure is compressed from Phase 237's four-power blowup
   (26.94 / 719.37 / 3955.13 / 7658.62) to a single-power (ξ⁰), single-component
   (+16.0 in T^r_r at the throat) residual with an exact R-decay profile.
2. Unarbitrated sectors that could carry it: H{2,0}(3) (Ric□Ric — its variation
   E2 exists as a Stage 1b byproduct, conserved, never arbitrated against
   print), H(6,3)(3) and H(6,3)(4) (kept as print, never derived), and the
   ξ⁰ assembly weights themselves.
3. Flagged untested: the 263-group trace-reduced scalar (Ric × (2,4)-traced
   Riem × Riem) found in the Stage 2b enumeration, outside the span of
   {tr Ric³, R·Ric²}.
4. Fences unchanged: massive-scalar DS stand-in at order 1/m² only; the THA
   Eq. (26) ξ³ defect stands as Phase 241 recorded it; no T_S is identified;
   the deficit sequence (forced −0.0795775 → iterate 1) is unchanged.

## Artefacts

Registration `work/p2591_registration.md`; harness `work/p2591_harness.py` +
`results/p2591_harness_selftest.json` (ALL_OK); engines `work/p2591_engine.py`,
`work/p2591_engine_d.py`; controls `results/p2591_controls.json` (parts A/B/C,
all_pass under the documented readings); derived tensors
`results/p2591_derived_H632.json`, `p2591_derived_H635.json`,
`p2591_derived_H636_candidates.json`, `p2591_derived_H638_candidates.json`;
arbitration + certificates (above); assembly + gate readout (above);
discriminators (above); stage memos `results/p2591_stage{1a,1b,1c,2a,2b,3*,4*,5}_*.md`
(gate readout = Stage 4 memo). Two worker deaths (Stage 2b, Stage 5) were
infrastructure restarts, recovered from disk state with re-verification; no
computation was lost silently. No ledger append, no launches, no iteration 2 —
per the tasking.
