# CHECKPOINT 214 — integration

Date: 2026-11-23. Registration: `phase214/REGISTRATION214.md`
(written before any Phase 214 computation; item-level
registration for Item 2 in `phase214/work/p2142_registration.md`,
likewise pre-run). Frame of record: Phase 166 pin,
Gate-19-corrected tensor, venv python (numpy 2.5.5 /
scipy 1.18.1). Both items executed with controls first; every
verdict-carrying number recomputed by an item checker from
the results files (29/29, 13/13). No ledger append, no
launches, no contact. Nothing outside `phase214/` was edited
by any item.

## VERDICTS FIRST

1. **P214-1 (FU-P210-1, interval extension): FAILS AT
   t* ∈ (0.5, 1.0] — bracketed to (0.5, 0.50625], mechanism
   MARGIN EXHAUSTION.** The director pose does not double its
   interval: it holds barely 1/200 of a time unit past 0.5.
   The sustainment interval at this pose's scope is
   [0, t*), t* ∈ (0.5, 0.50625]. The failing clause is
   NEC_φ = DEC_φ — the same clause Phase 210 left declining
   at +0.0045418770853060675 at t = 0.5 — reaching zero on its
   established trend, not a new clause. Past t* the collapse
   is deep and monotone with no recovery (director NEC_φ
   −37.400387861728845 at t = 1.0; worst clause DEC_ρ
   −39.455894142388544; all seven clauses negative by
   t = 1.0), while the non-clause bars never fail (momentum
   worst 1.7763568394002505×10⁻¹⁵; flare min
   0.05774016940840757 > 0; domain regular at every instant).
   The κ = 0 arm tracks the same collapse (worst
   −41.94885152609051 at t = 1.0): the director's shift buys
   [0, 0.5] and nothing beyond.
2. **P214-2 (FU-P210-2, two-sided true modes):
   TWO-SIDED CONSTRUCTION FAILS ITS OWN CONTROL.** The
   parity construction is integrator-sound (K-3a max L2 rel
   2.06×10⁻¹⁰; K-1/K-2 exact), but the K-3 successor —
   unrescaled tunnelling throat amplitudes vs the discrete
   eigenvectors under the same normalisation — misses the
   pre-registered ≤ 0.10 bar at ℓ = 16 (rel 0.312–0.318),
   ℓ = 24 (0.704–0.710), ℓ = 32 (0.934–0.936), passing only
   at ℓ = 8 (0.045–0.047). Per the registration the
   construction was not adjusted and the E-A diagnostic did
   not run: no increment table, no cumulative THA read, no
   repair package. The obstruction is priced, and it sits in
   the CONTROL REFERENCE, not the construction: the h = 0.05
   tridiagonal eigenvectors decay through the barrier at
   κ_d < κ (cosh(κ_d h) = 1 + (κh)²/2), inflating their own
   throat values by e^{+Δ}; integrating κ − κ_d over the
   barrier predicts the observed deficit (pred/obs =
   1.27 / 1.13 / 1.09 / 1.07 at ℓ = 8/16/24/32). Production
   reads remain VOID.

## ITEM 1 — INTERVAL EXTENSION (FU-P210-1)

Controls, asserted before the extension march, all exact:
(C-a) both arms' 21 G4 instants on [0, 0.5] reproduce
`phase210/results/p2101_results.json` stored G4 minima with
max abs diff 0.0 each arm; (C-b) κ = 0 anchors on the G2
anchor grid (first NEC_φ failure t = 0.400; worst
−0.6297872673028908; diff 0.0), G4 cross-value
−0.6297872673031459 (diff 2.55×10⁻¹³, the documented grid
agreement); (C-c) director t = 0 audit vs Phase 202 stored
minima diff 0.0 at both κ; ũ_true(θ*) = 1.1412482021558361
diff 0.0. Bonus diagnostic: the extension march's own
t = 0.5 read joins the stored G4 record with diff 0.0 on both
arms. Six protected files md5-identical before/after (the
extension used an in-memory T_END setting only).

Deciding reads (G4, sampled instants every 0.025 on [0, 1.0],
41 instants per arm): within the sampled bracket (0.5, 0.525]
four clauses cross zero (NEC_ρ, NEC_φ, DEC_ρ, DEC_φ); the
pre-registered refinement (intermediate instants at 0.00625
spacing) orders them — NEC_φ = DEC_φ crosses first, already
−0.03537861581570745 at t = 0.50625, while NEC_ρ = DEC_ρ is
still +0.004707212097541547 there and crosses one refinement
step later, in (0.50625, 0.5125]. Hence t* ∈ (0.5, 0.50625]
and the mechanism is margin exhaustion: the clause Phase 210
flagged as still declining at the interval end is the clause
that fails, on trend. Execution home-short, 89.7 s total —
verdict form 3 (budget) not owed. Process note on the memo's
face: the driver's first run classified the mechanism off the
sampled-instant crossing set and mislabelled it "new clause";
the driver was fixed to price the mechanism on the
refinement-ordered first crossing (the refinement's
registered purpose), re-run, and the checker independently
recomputes it the same way (29/29).

Fences: pose scope (m = 1, κ = 0.3, P-DIR-T2); jet/
channel-read scope; P129-6 combined-class scope; p1592 still
gates programme-level milestone wording; extension reads are
G4 single-grid reads under the exact [0, 0.5] reproduction
control — no (G3, G4) gate is claimed on the extension
interval. What this decides and what it does not: Phase 210's
pose-scope SUSTAINED bar set on [0, 0.5] stands untouched
(the bar set was met there); this item prices the pose's
actual holding interval as [0, t*) with t* barely past 0.5,
and the deep post-t* collapse (−37…−39 by t = 1.0, both arms)
closes the "the margin decline is a boundary effect that
recovers" reading at this pose. Record:
`phase214/results/p2141_memo.md`, `p2141_results.json`;
`phase214/work/p2141_run.py`, `p2141_check.py`.

## ITEM 2 — TWO-SIDED TRUE MODES (FU-P210-2)

Construction as registered in
`phase214/work/p2142_registration.md` (pre-run): parity
sectors — even u(0) = 1, u′(0) = 0 / odd u(0) = 0, u′(0) = 1 —
integrated outward from the throat by Numerov (S = 8,
h_f = 0.00625) and mirrored to the full box, so in each
barrier crossing the physical branch grows in the direction
of integration and admixture decays relatively (the exact
opposite of Phase 210's one-sided disease). Normalisation:
box norm rescaled to the C_n phase-averaged target norm
(evanescent points zero, Phase 209 convention).

Controls: K-1 PASS (counts exactly 258 at ℓ = 0, 251 at
ℓ = 16, headroom every ℓ). K-2 PASS (V0 D increments
reproduce the full-precision stored values at ℓ = 8/16/24/32
with relative error 0.0 at all four). K-3a PASS (parity
integrator vs exact sinusoids, max L2 rel 2.06×10⁻¹⁰).
K-3 SUCCESSOR FAIL, decisive: even doublet members' relative
throat-amplitude error 0.045–0.047 at ℓ = 8 (pass), 0.312–0.318
at ℓ = 16, 0.704–0.710 at ℓ = 24, 0.934–0.936 at ℓ = 32 vs the
≤ 0.10 bar; odd members are 0 on both sides and pass
trivially. Stop rule applied as registered: no adjustment,
no E-A run, no repair package.

Obstruction pricing (the form-3 requirement): the deficit is
one-sided and exponential — ln(u_disc/u_two) = 0.048 / 0.383 /
1.236 / 2.756 at ℓ = 8/16/24/32, against S/2 = 21.06 / 43.21 /
65.65 / 88.24. It is quantitatively explained by the discrete
reference's own barrier dispersion: the h = 0.05 tridiagonal
eigenproblem's evanescent decay rate satisfies
cosh(κ_d h) = 1 + (κh)²/2 < κh cosh-form, i.e. κ_d < κ, so the
DISCRETE eigenvectors under-decay through the barrier and
their throat values are inflated by e^{+Δ} with
Δ = ∫(κ − κ_d) predicted 0.061 / 0.432 / 1.347 / 2.951 —
pred/obs 1.27 / 1.13 / 1.09 / 1.07, converging to 1 as ℓ
grows. Integrator conditioning (Phase 210's disease) is
absent; the normalisation transfer cancels in the ratio and
is exonerated. Restated obstruction: at ℓ ≥ 16 the
unrescaled-amplitude control compares continuum modes against
a reference whose own throat amplitudes carry an
e^{+∫(κ−κ_d)} error growing ~quadratically in ℓ — the control
as registered cannot distinguish "construction wrong" from
"reference wrong", and on the priced numbers it is the
reference that is wrong by the named factor. Whether the
two-sided basis passes the E-A decay gate remains UNDECIDED
by anything run here. Subtraction B's residual (Phase 209
B_new plateau, cumulative +2.95×10⁵ × THA) is untouched and
remains a separate open term. Production reads remain VOID.
Checker 13/13 (it verifies the failure, the stop rule, and
the pricing). Record: `phase214/results/p2142_memo.md`,
`p2142_results.json`, `p2142_verify.json`;
`phase214/work/p2142_registration.md`, `p2142_run.py`,
`p2142_check.py`.

## FOLLOW-UP QUEUE (named by this phase)

- FU-P214-1 (from Item 1): the pose's holding interval is
  [0, t*), t* ∈ (0.5, 0.50625], and the binder is the
  NEC_φ/DEC_φ margin's decline rate, not a new clause. The
  named successor question for a future registration: a
  time-dependent director (κ(t) schedule, or a second
  compensator channel) priced against that decline rate —
  Phase 208 P208-5's trimming-loop gain window around this
  same pose (Kp ∈ (0, 0.0415] at one-sample delay) is the
  registered starting point. Any such item is a new pose and
  a new registration; the [0, 0.5] bar-set verdict of
  Phase 210 is neither extended nor reopened by it.
- FU-P214-2 (from Item 2): the unrescaled-amplitude control
  needs a reference with PRICED barrier dispersion — e.g.
  discrete eigenvectors on refined spatial grids (h, h/2,
  h/4) with Richardson-extrapolated throat amplitudes and
  the extrapolation's own error carried, or a two-grid
  self-convergence control on the parity construction with
  the discrete comparison demoted to ℓ ≤ 8 where its
  dispersion error is ≤ the bar. Only with such a reference
  can the K-3 successor be passed or failed cleanly at
  ℓ ≥ 16 and the E-A gate run on the two-sided basis. No
  production C1b rerun before that diagnostic passes.
