# CHECKPOINT 248 — SUSTAINMENT OF THE COMPOSED COMBINED-CLASS
# DATUM: OUTLIVED BY THE WOUND POSE; THE DRIFT IS THE SAME
# FORCED MODE, AND THE κ-TRIM TRANSFERS BUT IS CAP-LIMITED

Phase 248, 2026-11-24. Named successor of Phase 246 §5(i):
how long can the rotating, time-varying throat (Phase 245's
combined-class pin-break + Phase 246's CH-PHI-Auu φ-channel)
actually live? Frame of record: Phase 166 pin,
Gate-19-corrected tensor, venv python. Both items ran
registrations + verdict forms BEFORE computation, controls
first; worst-instant discipline; per-slice channel posed
under the frozen P-PHI-FROZEN-246 (Item 1) and under the
pre-registered open-loop law P-PHI-TRIM-248 (Item 2, Part B);
total-stress accounting throughout (total stress = G/8π is
the read itself). Item memos: results/p2481_memo.md,
results/p2482_memo.md; registrations, drivers, checkers,
results JSONs under work/ and results/.

## FTL VERDICT (leading): NO

No grouped joint pass anywhere; Frontier A unchanged; drive
step 1 remains unachieved. The phase's yield: the composed
combined-class datum's sustainment is now bracketed —
**(0.4875, 0.49375]** as posed, **(0.525, 0.53125]** under
the priced κ-analogue trim — both short of the wound pose's
Gate-23-certified **(0.55625, 0.5625]**, which stands as the
line's best throat; and the failure is identified, exactly,
as the same forced μ-drift t² mode that governs the whole
A branch.

## ITEM 1 — THE MARCH (composed datum as posed)

**VERDICT: OUTLIVED BY THE WOUND POSE** (form 2) — checker
37/37, including fresh spot recomputation of both bracket
instants at diff 0.0 and live protected-file md5 identity
(nothing outside phase248/ edited).

Controls: CTRL-1 PASS at diff 0.0 (Phase 246 composed reads
reproduced in full — anchors NEC_φ = +0.093089 @ 0.475,
NEC_ρ +1.295071 @ 0.475, first fail t = 0.5 at −0.081831;
headline NEC_φ first fail 0.400, worst
−0.6297872673028908). CTRL-3 PASS (static pin −4.0625, both
arms). CTRL-2 (march-length invariance, T_END = 1.0 vs 0.5)
PASS on every verdict-carrying read — all clause statistics,
S(θ*), identity decompositions, momentum maxima at exactly
0.0 at all 21 instants — with a disclosed footnote: 54
individual profile entries at t = 0.5 differ by ±1–2 ulp
(max 4.44×10⁻¹⁶, moving no statistic); anatomy priced (MU/U
rows 0–200 and MTT rows 0–199 bit-identical; MTT row 200
differs ≤ 1.54×10⁻⁵ by the final-index stencil — the Phase
240 class — but MTT feeds only Fuu and reaches the clause
pipeline at roundoff; bracket instants are interior /
aux-priced ≤ 6.1×10⁻¹¹). A profile-bitwise reading of
CTRL-2 would fail on those ulps; no bracket number is
within 10¹³ of that scale. PR-φ PASS 41/41 (mom_φ residual
≤ 1.3×10⁻¹⁵). Cost rule did not fire (projection 38.9 s
≤ 900 s; no kernel spec owed).

**The march (T_END = 1.0, frozen a = −0.5):** refined
first-crossing bracket **(0.4875, 0.49375]**, width 0.00625,
carrier **NEC_φ = DEC_φ** at both ends (margins +0.008513 →
−0.035909) — the ladder refines Phase 246's sampled picture
(holds at 0.475, fails at 0.5) to inside (0.475, 0.5). No
overlap with the wound bracket. The channel did buy life
against the no-channel headline datum (sampled bracket
(0.375, 0.400]): ≈ +0.09 — but the flat Auu lift is outrun
by the μ-drift before t = 0.5 (NEC_φ lift at t = 0.5 is
+0.547957, priced). On the record past the crossing:
composed NEC_ρ survives sampled instants to 0.725, fails at
0.75; S(θ*) peaks +2.1540 at t = 0.5 — the pin break itself
is not what dies; the φ drift is.

One-table comparison (per form 2):

| datum | worst NEC_φ at t = 0 | first-crossing bracket | carrier |
|---|---|---|---|
| headline (no channel) | +0.585 (fit c₀) | (0.375, 0.400] sampled | NEC_φ = DEC_φ (μ-drift) |
| composed (Auu a = −0.5) | +0.626 (lift incl.) | **(0.4875, 0.49375]** refined | NEC_φ = DEC_φ (μ-drift) |
| wound pose (κ = 0.3 + CH-COMB + CH-PHI-Auu) | — | **(0.55625, 0.5625]** Gate-23 CERTIFIED | NEC_φ = DEC_φ |

Per the form, the combined-class line's value restates as
the NEC_ρ pin break (Phase 245), not sustainment.

## ITEM 2 — THE DRIFT ANATOMY + κ-TRIM TRANSFER

**VERDICT: SAME FORCED MODE — TRIM TRANSFERS AT A PRICE**
(form 1) — checker 23/23, including fresh recomputation of
both trimmed bracket instants at diff 0.0.

**Part A (stored rows only).** The decomposition is EXACT:
composed NEC_φ,min(t) = headline NEC_φ,min(t) + lift(t) at
all 41 instants, max deviation 0.0. At the bracket the
headline drift term drops 0.042781 between 0.4875 and
0.49375 while the lift erodes only 0.001641 — the drift
itself carries NEC_φ through zero (96% of the drop); the
argmin sits at θ* throughout, no migration. Fits: headline
[0, 0.375] — full (c₀ +0.585128, c₁ +0.280588, c₂
−4.629047, RMS 0.005709); forced-t² (c₀ +0.604014, c₂
−3.932798, RMS 0.010259, 1.80× the full fit); linear
rejected (RMS 0.054962); forced-fit root 0.391898 ∈
(0.375, 0.400], matching the headline bracket. Composed
[0, 0.475]: q₂ = −6.062835 (full fit). The lift is
t²-eroding but weakly (c₂ −0.280631; ≈ 0.072 total erosion
against its 0.625 level; fit RMS 0.000404). Same-mode
identification: Item 1's headline NEC_φ trajectory is
BIT-IDENTICAL to Phase 245's stored ω_a = 0 baseline (max
diff 0.0) — rotation's effect on the drift coefficients is
exactly 0.0, and the carrier is the P169-1 μ-drift (first
fail 0.400, worst −0.6297872673028908), matching the
forced-mode characterisation in phase208/results/
p2085_memo.md §§2–4 (μ ≈ (t²/2)ũ, spectrally neutral; the
on-paper κ-trim stabilisability and the Phase 217 V2
closed-loop contrast also live there — the wound record's
home, corrected on this phase's face). Disclosure —
Amendment A-1: the registration's original c₁ sub-criterion
failed the headline form on a fit-noise scale comparison
alone (0.1052 vs 0.0171) while the RMS and root criteria
passed; A-1 was recorded in the registration AFTER the fits
printed but BEFORE any Part B computation, replacing it
with the scale-correct |c₁|·t ≤ 0.25|c₂|·t² (0.105 ≤ 0.163
✓). Both outcomes are on the memo's face; the verdict also
rests on the exact decomposition and the bit-identity, not
on the fit form alone.

**Part B (the trim, priced).** Law P-PHI-TRIM-248
(open-loop, fixed in advance): a(t) = −0.5 − c_trim·t²,
c_trim = −q₂/s̄ = **+5.253378** (s̄ = 1.154083, Phase 246
stored sensitivities), cap |a| ≤ 0.8 clamped. Controls all
PASS (c_trim = 0 arm reproduces Item 1's composed reads at
diff 0.0; static pin; CTRL-2 class covered). The cap
CLAMPS at **t = 0.238969** — the arm runs at a = −0.8 for
most of its life (peak |a| = 0.8, headroom 0.0). PR-φ
adapted PASS 41/41. **Trimmed refined bracket:
(0.525, 0.53125]**, carrier NEC_φ = DEC_φ — an extension
of **+0.0375** past the untrimmed bracket, still short of
the wound (0.55625, 0.5625]. Descriptive flat price (stored
sensitivities only): carrying the untrimmed datum's
crossing to 0.5625 would need a flat a* = **−1.517513** —
outside the 0.8 cap. **The transfer is cap-limited, not
law-limited:** the κ-trim mechanism works at this datum
(same mode, priced extension) but the registered amplitude
cap, not the trim law, is what keeps the composed datum
behind the wound pose.

## PHASE SYNTHESIS

The A branch's two surviving throat lines are now compared
in one frame on sustainment, and the wound pose keeps the
lead — certified (0.55625, 0.5625] against the composed
datum's (0.4875, 0.49375] as posed and (0.525, 0.53125]
trimmed. The deeper result is the unification of the
failure: every A-branch datum in the record dies of the
same forced μ-drift t² mode, rotation contributes exactly
nothing to it, and each line's lifetime is set by how much
priced lift its channels hold against that one drift. The
combined-class datum's deficit is no longer mysterious and
no longer structural in the law — it is an amplitude-cap
deficit: the trim law that would carry it past the wound
pose exists and is priced (flat-equivalent |a*| ≈ 1.52),
and the |a| ≤ 0.8 cap is the standing obstruction.

Named successors: (i) **the amplitude-cap provenance
audit** — the C1-style question for CH-PHI-Auu's |a| ≤ 0.8
cap (Phase 246 §5): what does the cap protect (liveness?
posed-jet sanity?), is its level that condition's true
boundary or a convention, and what is the re-priced
crossing if the datum is re-posed at the cap's true level
— the cheapest registered route past the wound bracket if
the cap proves conventional; (ii) a certification
registration for the trimmed bracket (Phase 243 pattern)
only if the line wants it as a verdict — it does not lead,
so this is subordinate to (i); (iii) the structural route
remains Phase 245 §5's: a datum whose lock drift is
smaller at the source (P169-2-class t-controlled
spatial-jet pose), now sharpened — any such datum inherits
this phase's exact test (decomposition + forced-mode fit +
bracket vs (0.55625, 0.5625]).

Fences: jet scope; per-instant diagonal ZAMO reads at
sampled/refined instants; datum ≠ construction; the
trimmed arm is a NEW posed datum under a law fixed in
advance (Item 1's datum and verdict untouched); open-loop
trim ≠ the closed-loop stabilisability proof — the priced
effect is what transferred; no certificate is claimed for
any bracket in this phase (Phase 243/Gate-23 cover the
wound pose only); the CTRL-2 ulp footnote and Amendment
A-1 stand on the face of the item memos.

No ledger append (parent's step); no launches; no external
contact.
