# P88-2 — THE FRINGE-NARROWED SPAN (FU-P803-1)

## VERDICT: ABOVE 0.08745 AT FULL LEGALITY

**MILESTONE (payload transport category only).** Narrowing the
outer shell's source span from the Phase-80 extension ±0.30W to
**±0.10W** raises the outer shell's alone ceiling from β = 0.06
to β = 0.07, and the composed row built from it — outer shell
alone at β = 0.07 (span [4.5, 10.5]), inner shell alone at
β = 0.06 (Phase-80 span, unchanged), both orthonormal shifts
held under Phase 46's lapse re-equilibration — carries a held
payload of **0.09556c** and passes the full gate-standard
legality audit (Type-I + sampled-null + margins, full volume
over both shells AND the cavity, the one cavity site decided by
the Gate-8 settlement ladder re-derived in this item; §2). That
is above the Phase-80 phase-verified row in this category
(0.08745c, NOT gated — Gate-10 is re-checking it in parallel and
was not awaited) and above this category's standing verified
mark, 0.0799c (Phase 46, Gate-8 restated scope). A second row
at **0.08915c** (inner β = 0.05) beats 0.08745 under the same
audit pattern and corroborates the first. Locked language: this
is a payload-transport result, phase-verified in this item; it
has NOT been through a Gate. No bare-shell comparison is made
or implied anywhere in this memo.

## Plain language

Phase 80 found that its stronger shells could each legally run
at speed 0.06 alone, but at 0.07 the outer shell broke — not in
its wall, which stayed perfectly healthy, but in the faint
"fringe" where its drive profile fades in and out beyond the
shell's edges. The fade region was much wider than the shell
itself (the transition spanned radii 3.5 to 11.5 around a shell
that lives between 5 and 10), and the thin density out there
could not support the drive gradient crossing it. This item
tested the obvious fix: squeeze the fade region inward. At the
widest tested narrowing short of the tightest (±0.20W, ±0.15W)
the break shrank steadily but did not close; at the tightest
registered span, ±0.10W (transition 4.5 to 10.5), it closed
completely — the outer shell alone is legal at 0.07, with its
fringe margins actually stronger than the old shell's wall
margins at 0.06. Composing that shell with the inner shell at
its proven setting then carries a payload at 0.0956c, about 9%
above Phase 80's row and 20% above the verified 0.0799c mark,
with every energy condition satisfied everywhere the audit can
resolve. The next step up (either shell alone at 0.08) still
breaks, in the same fringe family of places, so 0.0956c is
where this design space now stops — and the stop has moved
again: it is no longer the fringe width, it is the fringe at
the next speed.

## 1. Control re-derivation (before any narrowed number)

Per the registration, both control patterns were re-derived on
this item's machinery first (full numbers in the run record):

- **(a) The 0.0799 cosine row's cavity site, Gate-8 standard:**
  stencil-clear cavity reads on the Gate-8 (4th-order) path
  +1.62×10⁻⁴ / +2.01×10⁻⁴ / +1.98×10⁻⁴ (h = 0.15 / 0.075 /
  0.0375), Type-I 1.000 — the Gate-8 settlement pattern
  (their reads +9.98×10⁻⁵ class) reproduced; raw near-edge
  shell reads (4.6 < r < 5) non-monotone across h in both
  discretisations, i.e. sign/magnitude-unstable with no
  convergent negative value.
- **(b) The Phase-80 0.08745 row's cavity ladder:** focused
  +5.04×10⁻⁷ / +1.21×10⁻⁵ and stencil-clear +9.33×10⁻⁵ /
  +1.61×10⁻⁴ at the fine rungs — digit-for-digit Phase 80's
  stored values, Type-I 1.000 throughout.

## 2. The deciding row

Row `e0.10_o0.07_i0.06` (outer span ±0.10W, β_o^alone = 0.07;
inner β_i^alone = 0.06 at ±0.30W). Economics first: held-W sum
0.17259, recorded in `p882_economics.json` before any composed
legality read (24 rows frozen; the audit order in the composed
file is descending held payload). Held shifts verified:
β_o^comp = 0.057064, β_i^comp = 0.038704, W relative errors
1.5×10⁻¹⁶ / 1.7×10⁻¹⁶ (checker-recomputed).

Gate-standard audit, h = 0.15, worst margin by region:
payload **+3.84×10⁻⁶**, inner wall **+1.190×10⁻³**, cavity
−1.121×10⁻⁴ †, outer wall **+3.35×10⁻⁵**, exterior
**+1.11×10⁻⁶**; Type-I fraction **1.000**; min sampled NEC
+1.13×10⁻⁶ overall (+1.13×10⁻⁴ in the cavity); conservation
relative median 0.0117.

† The cavity site is the composition line's settled stencil
artefact, at the same radius (r ≈ 4.53) and magnitude as on
Phase 80's rows and on this item's cosine control of the
0.0799 row itself. The re-derived settlement ladder on this
row: focused DEC −1.84×10⁻⁴ → **+1.45×10⁻⁶** (h = 0.075) →
**+1.38×10⁻⁵** (0.0375); stencil-clear −1.53×10⁻⁴ →
**+9.50×10⁻⁵** → **+1.63×10⁻⁴**; Type-I 1.000 at every rung.

**Independent second path (required for this verdict form):**
two discretisations different in kind (wa_diag 4th-order;
Phase-1 judge), same point set, h = 0.15 — both Type-I 1.000,
every region positive except the same cavity floor site at
−2.20×10⁻⁶ / −2.84×10⁻⁶ (r = 4.87), inside the Gate-8 settled
floor class (the standing mark's own carried touch was
−3.7×10⁻⁶ at this site). The corroborating row (0.08915c)
verifies identically. Checker: `p882_check.py`, 19/19 PASS.

## 3. Anatomy — how the binding moved, with numbers

**Alone ladder, outer shell, β = 0.07** (h = 0.15; Type-I
fraction / min sampled NEC; fringe split in the run record):

| span | Type-I | sampled NEC | fringe_lo worst | wall worst |
|---|---|---|---|---|
| ±0.30W [3.5, 11.5] | 0.646 | −5.04×10⁻⁴ | +3.5×10⁻⁶ (TI 0.93) | +1.49×10⁻⁴ |
| ±0.20W [4.0, 11.0] | 0.699 | −5.38×10⁻⁵ | +8.2×10⁻⁵ (TI 1.00) | +1.48×10⁻⁴ |
| ±0.15W [4.25, 10.75] | 0.869 | −2.93×10⁻⁵ | +1.57×10⁻⁴ (TI 1.00) | +1.53×10⁻⁴ |
| ±0.10W [4.5, 10.5] | **1.000** | −2.17×10⁻⁷ ‡ | +1.56×10⁻⁴ (TI 1.00) | +1.43×10⁻⁴ |

‡ the fixed exterior floor read (−5.01×10⁻⁷ worst, identical
across spans and β — a design-independent background tail
point), which flips to +6.38×10⁻⁷ at h = 0.075: the Phase-80
artefact signature, under the standing criterion.

Reading: narrowing does exactly what the mechanism predicted
to the low fringe — fringe_lo goes from marginal (+3.5×10⁻⁶,
Type-I 0.93) to the strongest region in the shell — and the
failure retreats monotonically (Type-I 0.646 → 1.000, sampled
NEC improving by ~3 orders) through the interior-classified
and high-fringe points whose stencils sample the transition,
until at ±0.10W nothing is left but the floor artefact. The
wall never binds at any span (always ≈ +1.5×10⁻⁴).

**The new cap: β = 0.08 alone, at every span.** At ±0.10W,
β = 0.08 reads Type-I 0.705, sampled NEC −1.28×10⁻⁴
(h-converged: −1.26 / −1.28 / −1.29×10⁻⁴), with the failure
in interior-classified points (Type-I 0.18) and fringe_hi /
exterior (0.65 / 0.40) while fringe_lo (+1.55×10⁻⁴, Type-I
1.000) and the wall (+1.44×10⁻⁴) stay clean — the same fringe
family, one speed higher. The (0.08, ·) economics rows
(0.09727 / 0.10366) are therefore unassemblable in this item.

**Composed anatomy:** none of the composition's historical
bindings appears. Inner wall +1.19×10⁻³ (strongest region;
no composed row named the inner fringe, so the inner shell
kept its 0.30W span per the registration's conditional);
outer wall +3.35×10⁻⁵ — the closest real composed margin,
slightly WIDER than Phase 80's deciding row (+3.20×10⁻⁵ at a
lower payload); cavity clean under the settlement ladder.

**Net:** Phase 80 moved the binding from the composition to
the outer shell's alone fringe; this item shows the fringe
binding was a span-width effect, removes it at ±0.10W, and
the payload rises by the full held-W value of the unlocked
β step (0.08745 → 0.09556). The binding now sits at β = 0.08
alone in the same fringe family — a speed wall, not a span
wall, at the narrowest registered span.

## 4. C12 accounting

All speeds subluminal; both shells are pre-existing
configurations (pre-arrangement by ≤ c signals);
construction-inclusive arrival ≥ D/c. No formation claim.
The result is a prescribed-geometry audit under the
programme's shell standard: the required source satisfies
the energy conditions; no matter model, stability, or
formation route is claimed. Category: payload transport
only. This row is phase-verified, NOT gated; the standing
verified mark in the category remains 0.0799c until a Gate
rules on the Phase-80 and Phase-88 rows.

## 5. Follow-ups (Failure Protocol — ≥1, mechanism-suggested)

1. **FU-P882-1 — Bisect the new speed wall (β = 0.075 alone,
   ±0.10W and ±0.075W).** The ceiling moved from span-bound
   (0.07 at ±0.30W) to somewhere in (0.07, 0.08) at ±0.10W,
   and the registered span set bottomed out at 0.10W while
   the trend was still improving. One β = 0.075 rung at
   ±0.10W, plus a ±0.075W span at β = 0.07/0.08, decides
   whether the wall is span or speed at the next digit —
   the composed prize is the (0.075, 0.06) economics class
   (≈ 0.100c) if 0.075 assembles.
2. **FU-P882-2 — Composed-space polish at 0.09556**
   (FU-P803-2, now with a deciding row worth hardening):
   bounded polish of both design vectors against the
   composed core score under the held-W constraint, aimed
   at the outer wall's +3.35×10⁻⁵, before any Gate referral.
3. **FU-P882-3 — Endpoint-residual watch.** The narrowed
   chain's endpoint residuals grew (S_lo−1 = −3.9×10⁻³ at
   ±0.10W vs −1.0×10⁻⁴ at ±0.30W) while balance and
   monotonicity stayed exact. If spans narrow further
   (FU-P882-1), track whether the endpoint residual starts
   to reach the audit — a ρ̂-floor weighting in the source
   (Phase 80's FU-P803-1 alternative form) is the registered
   counter-move if it does.

## Files

Scripts (`phase88/work/`): `p882_lib.py`, `p882_control.py`,
`p882_control_a2.py`, `p882_alone.py`, `p882_compose.py`,
`p882_verify.py`, `p882_check.py`. Results
(`phase88/results/`): `p882_control.json`, `p882_alone.json` +
`p882_alone_state.json`, `p882_economics.json`,
`p882_composed.json`, `p882_verify_e0.10_o0.07_i0.06.json`,
`p882_verify_e0.10_o0.07_i0.05.json`, `p882_check.json`,
`p882_run_record.md`, logs (`p882_control.log`,
`p882_alone.log`, `p882_compose.log`). INTERNAL only.
