# CHECKPOINT 266 — P266-1: CERTIFICATION OF THE
# UNCLAMPED-LAW BRACKET (0.675, 0.68125] — THE
# STOP-FREE CERTIFICATE (PHASE 243 PATTERN, NO STOP
# PARAMETER)

Phase 266 (single item), warp pilot. Integrated
record: `phase266/results/p2661_memo.md`.
Registration (pre-run, FIXED):
`phase266/work/p2661_registration.md`. Driver:
`phase266/work/p2661_run.py`; results:
`phase266/results/p2661_results.json`; checker:
`phase266/work/p2661_check.py` →
`phase266/results/p2661_verify.json` (25/25 PASS).
Frame of record: Phase 166 pin, Gate-19-corrected
tensor, venv python, float64. INTERNAL only. No
ledger append, no launches, no external contact;
protected files byte-identical before/after
(29 files; memo §7).

## VERDICT

**FORM 1 — BRACKET CERTIFIED.** The combined-class
datum under the **unclamped** trim law
a(t) = −0.5 − c_trim·t² (c_trim =
+5.253378225339471, FITTED in Phase 248 Part A and
frozen since; the pose carries **no stop parameter
anywhere**) holds all seven throat clauses at all
28 sampled instants of [0, 0.675] on the standing
grid (Phase 265's rows, reproduced by CTRL-1 at
diff 0.0), and its first crossing is certified at
**(0.675, 0.68125]** on NEC_φ = DEC_φ: per-instant
Richardson limits on G3/G4/G5 over the window
[0.61875, 0.75] meet the unchanged 1×10⁻⁶ bar at
every window instant (CERT-1…4 all TRUE; limits
L(0.675) = +0.05132124946169617,
L(0.68125) = −0.048044525888048084). The bracket
lies entirely past the clamped pose's certified
(0.65625, 0.6625] (Phase 256 / Gate-26) and the
wound pose's certified (0.55625, 0.5625]
(Phase 243 / Gate-23) — certified-vs-certified in
each case. Gate-26's priced gap is now closed at
verdict grade as well as read grade: the certified
bracket is not an artefact of any stop, because
the certified pose has none.

## FTL VERDICT (leading): NO

No grouped joint pass anywhere; Frontier A
unchanged; drive step 1 remains unachieved. The
phase's yield is on the wormhole goal: the
programme's longest-lived throat datum now holds
its lead under a certificate whose pose is the
trim law itself — the operational stop B := 2.5,
which Gate-26 required to be named in every
quotation of the Phase 256 claim, is absent from
the certified object.

## WHAT RAN (decision order)

- **Registration first** (`phase266/work/
  p2661_registration.md`): Phase 243/256's
  certificate with six adaptations on the face —
  the stop removed (A1); grids unadapted (A2);
  window [0.61875, 0.75] with the top capped by
  Phase 265's audited-delivery coverage
  (a(0.76875) = −3.6046234051234713 lies outside
  the audited range [0, −3.5]; a(0.75) =
  −3.4550252517534528 inside it) (A3); no prior
  certificate re-opened (A4); CTRL-1's target =
  Phase 265's B = 3.5 (unclamped-equivalent) arm
  (A5); tail pricing from fresh rows with its
  amplitude caveat (A6). The fitted coefficient is
  named as fitted with provenance (§B); the
  evidence classes and the grid-stability character
  are fixed in advance (§C).
- **Controls first, all PASS** (memo §2): CTRL-2
  exact from Phase 265's stored rows (both arms'
  brackets coincide at (0.675, 0.68125];
  t_clamp(3.0) = 0.6898436476740386 ≥ 0.68125, so
  the bracket is arithmetically the unclamped
  law's own); CTRL-1 at diff **0.0** on every
  compared row (31 sampled instants t ≤ 0.75, both
  bracket ends, 8 fixed-t rows; matched T_END =
  1.0); CTRL-3 at 1.42×10⁻⁸ / 5.69×10⁻⁸ (identical
  to Phases 243/256, as required).
- **G5 probe** (§5(d)): 25.3 s → projected 505.7 s
  ≤ 900 s; the rule did not fire; G5 ran locally
  (636.0 s). No kernel spec owed.
- **Certificate** (memo §4): all nine window
  instants limit-certified (eight monotone,
  p ∈ [3.60, 4.38]; the bottom instant 0.61875
  degenerate at the rounding floor, r =
  1.403×10⁻¹³); worst |d34| = 3.322×10⁻¹³, worst
  |d45| = 2.309×10⁻¹⁴, worst residual
  2.109×10⁻¹⁵ — grid-stability character, recorded
  as such (the p values carry no convergence
  information; §C / Gate-26 §2 discipline).
  CERT-4's non-clause bars hold at both bracket
  instants (momentum ≤ 5.6×10⁻¹⁶, flare ≥ 0.1171,
  domain_R ≥ 0.5881).
- **Tail pricing on the face, fence (i) intact:**
  from this phase's fresh G3/G4 rows on (0.75, 1.0]
  — first exceedance of 1×10⁻⁶ at t = 0.775; stage
  max 1.6326921098652747×10⁻⁵ at t = 1.0, carrier
  WEC, relative 7.363195956559376×10⁻⁶. Amplitude
  caveat carried: past t = 0.7556858539654343 the
  tail reads pose amplitudes beyond Phase 265's
  audited delivery range, reaching −5.753378225339471
  at t = 1.0. Tail reads past the window are NOT
  certified.
- **Checker 25/25 PASS** (memo §8), including fresh
  G4/G5 spot recomputation of both bracket ends at
  diff 0.0, independent CTRL-2 recomputation,
  Richardson/CERT/tail recomputation, the
  NEC_φ ≡ DEC_φ identity on all grids (diff 0.0),
  and the no-stop-parameter record check. One
  execution disclosure (memo §8): the checker's
  first launch was killed by the runtime (SIGTERM,
  659 s) inside its G5 march after 16 checks had
  passed; the identical unmodified checker was
  re-run detached and completed 25/25.
  Driver wall 929.6 s; checker wall 671.8 s.

## NAMED SUCCESSOR

A Gate registration on the certified claim set —
re-examining Gate-26's G26-A fence ("the trim law
as clamped at B := 2.5") in light of this stop-free
certificate. This phase does not register it; the
parent's act.

## FENCES

Form 1's fences stand: (i) tail limitation — reads
past the window [0.61875, 0.75] are NOT certified,
and the tail pricing (with its amplitude caveat)
stands on the face as the tail reads' priced
uncertainty; (ii) pose scope (Phase 169 A-branch
datum, true lock; κ = 0.3 director + C2 rotating
headline + CH-PHI-Auu under P-PHI-TRIM-248 with
the unclamped law and its FITTED coefficient, as
posed — the certified bracket lies outside the
coefficient's fit window [0, 0.475], extrapolation
on the record); (iii) jet scope / sector
superposition (exhibit ≠ construction); (iv)
programme-level sustainment wording remains gated
by p1592 regardless. The evidence is the two
classes of registration §C — sampled standing-grid
span plus window limit-certification — and no
continuum claim between instants is made or
certified. Phase 243/256 verdicts and Gate-23/
Gate-26 claim sets stand untouched for their own
poses and scopes.
