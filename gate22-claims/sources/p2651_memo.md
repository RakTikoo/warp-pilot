# P265-1 MEMO — THE B-SENSITIVITY READ: THE BRACKET'S
# DEPENDENCE ON THE OPERATIONAL STOP B, PRICED; THE
# STOP RETIRES AT READ GRADE

Phase 265 (single item), warp pilot. Registration
(pre-run): `phase265/work/p265_registration.md`. Driver:
`phase265/work/p2651_run.py`; results:
`phase265/results/p2651_results.json`. Checker:
`phase265/work/p2651_check.py` →
`phase265/results/p2651_verify.json` (8/8 PASS; §7).
Frame of record: Phase 166 pin, Gate-19-corrected
tensor, venv python, float64. INTERNAL only. No ledger
append, no launches, no external contact; protected
files byte-identical before/after (15 files; §7/C8).

## VERDICT

**FORM 1 — THE STOP RETIRES.** The §4 admissibility
gates pass at B = 3.0 and B = 3.5; their refined
first-crossing brackets coincide exactly at
**(0.675, 0.68125]**; the hi-end carriers at both arms
are exactly {NEC_φ, DEC_φ}; and t_clamp(3.0) =
0.6898436476740386 ≥ the coincident hi 0.68125, so at
B = 3.0 the clamp never binds at or before the
crossing — the coincident bracket is the **unclamped
law's own crossing**, the stop-free bracket at read
grade: **(0.675, 0.68125]**, carrier NEC_φ = DEC_φ.
Gate-26's priced gap (§1) closes at read grade; the
certified claim's fence rewording is the next gate's
act, not this phase's (§8 fences).

## 1. THE GAP PRICED (registration §0)

Gate-26 §4(3a) established that Phase 256's certified
object is the trim law a(t) = −0.5 − c_trim·t²
(c_trim = +5.253378225339471, fitted in Phase 248,
stored, not re-fit) **as clamped at the operational
stop B := 2.5** — the stop binds from t = 0.617015, so
the whole certified bracket (0.65625, 0.6625] is read
at a ≡ −2.5 — and that "no sensitivity of the bracket
to the stop's value is on record", while the record
itself proves the bracket clamp-sensitive as a class
(0.8-clamp → (0.525, 0.53125], Phase 248; 2.5-clamp →
(0.65625, 0.6625]). This phase marched the same datum
under the generalised clamp a_B(t) = max(−0.5 −
c_trim·t², −B) for B ∈ {1.5, 2.0, 2.5, 3.0, 3.5}, all
arms read off ONE pair of march states (main N_θ =
2881, h_t = 0.0025; aux h_t = 0.00125; both T_END =
1.0) — a pure clamp comparison with no march-to-march
variation. READ grade throughout: no Richardson
ladder, no certificate claimed or implied for any
bracket in this phase.

## 2. CONTROLS (registration §2 — all PASS)

- **CTRL-1 (inherited, verbatim):** CTRL-A untrimmed
  bracket (0.4875, 0.49375]; CTRL-B 0.8-clamped
  bracket (0.525, 0.53125], clamp instant 0.23896885;
  CTRL-C static pin S(θ*) = −4.0625 — all at Phase
  252's bars.
- **CTRL-2 (the B = 2.5 anchor):** the fresh B = 2.5
  arm reproduces Phase 252's stored re-posed record —
  sampled bracket (0.65, 0.675], first-fail carriers
  exactly {NEC_φ, DEC_φ}; refined bracket (0.65625,
  0.6625]; end NEC_φ margins +0.05279917238250764 /
  −0.07369468042669158 exactly; stop instant
  0.617014916018226 (diff 1.40×10⁻⁸ vs the recorded
  0.61701493, bar 1×10⁻⁶); the 41 sampled instants'
  per-clause minima at max abs diff **0.0** against
  Phase 252's stored rows. Checker C1 re-derived both
  bracket ends fresh at diff 0.0 against both records.

## 3. THE BRACKETS AS A FUNCTION OF B (§3b–c, f)

| B | t_clamp(B) | sampled | refined bracket | end NEC_φ margins (lo / hi) | hi carriers |
|---|---|---|---|---|---|
| 1.5 | 0.4362954312097357 | (0.575, 0.6] | (0.59375, 0.6] | +0.04444979106278524 / −0.039778537628649246 | {NEC_φ, DEC_φ} |
| 2.0 | 0.5343505917857057 | (0.625, 0.65] | (0.63125, 0.6375] | +0.0013636084937767023 / −0.10561892076459589 | {NEC_φ, DEC_φ} |
| 2.5 | 0.617014916018226 | (0.65, 0.675] | (0.65625, 0.6625] | +0.05279917238250764 / −0.07369468042669158 | {NEC_φ, DEC_φ} |
| 3.0 | 0.6898436476740386 | (0.675, 0.7] | (0.675, 0.68125] | +0.051321249458261775 / −0.04804452588981167 | {NEC_φ, DEC_φ} |
| 3.5 | 0.7556858539654343 | (0.675, 0.7] | (0.675, 0.68125] | +0.051321249458261775 / −0.04804452588981167 | {NEC_φ, DEC_φ} |

Lo-end carriers below zero: none at any arm (all seven
clauses hold at every lo end). Midpoints m(B):
0.596875, 0.634375, 0.659375, 0.678125, 0.678125 —
monotone nondecreasing over all five admissible arms;
interval rates per unit B: **0.075 (1.5→2.0), 0.050
(2.0→2.5), 0.0375 (2.5→3.0), 0.0 (3.0→3.5)** — the
bracket's sensitivity to the stop is real, decaying,
and saturated from B = 3.0. The full answer to the
brief's question (i): yes, monotone; the total
movement across the swept range is 0.08125 in the
midpoint, of which 0.01875 lies between the certified
B = 2.5 arm and the stop-free bracket.

**Why the 3.0/3.5 coincidence is the unclamped
crossing and not a shared clamped cell:** the
unclamped law reaches −3.0 only at t = 0.689844, past
the coincident hi 0.68125 — over the entire deciding
span [0, 0.68125] the B = 3.0 arm's applied amplitude
IS the unclamped law. The B = 3.5 arm agrees because
its clamp engages even later (0.755686). And the two
arms are not trivially the same arm: wherever the
clamps separate them they separate in the reads —
at t = 0.7 (past the crossing) the B = 3.0 and
B = 3.5 NEC_φ minima differ by 0.07307305580435397
(checker C5), while at every fixed t ≤ 0.675 they
agree at diff 0.0, exactly as the §3(g) structural
prediction requires.

## 4. MARGINS AT THE CERTIFIED INSTANTS (§3d)

NEC_φ = DEC_φ minima under each arm (full seven-clause
minima in the results JSON):

| t | B = 1.5 | B = 2.0 | B = 2.5 | B = 3.0 | B = 3.5 |
|---|---|---|---|---|---|
| 0.65625 | −0.957040 | −0.452120 | +0.052799 | +0.317823 | +0.317823 |
| 0.6625 | −1.080033 | −0.576864 | −0.073695 | +0.233984 | +0.233984 |

Read plainly: at the certified lo instant the margin
grows with B and is still growing between 2.5 and 3.0
(+0.0528 → +0.3178) — the certified bracket is a
B = 2.5 statement in exactly the way Gate-26 fenced —
and by B = 3.0 both certified instants sit *inside*
the living span (both margins positive), the crossing
having moved out to (0.675, 0.68125].

## 5. FIXED-t SENSITIVITY (§3e) — THE BANKED-LIFT
## SLOPE IN B

NEC_φ minima at fixed t, successive differences per
unit B (full precision in the results JSON; rates =
Δmargin/ΔB over each 0.5 step):

| t | B=1.5 | B=2.0 | B=2.5 | B=3.0 | B=3.5 | rates (per unit B) |
|---|---|---|---|---|---|---|
| 0.5625 | 0.423596 | 0.954650 | 1.126925 | 1.126925 | 1.126925 | 1.062107, 0.344551, 0, 0 |
| 0.6 | −0.039779 | 0.480881 | 0.888262 | 0.888262 | 0.888262 | 1.041319, 0.814761, 0, 0 |
| 0.65 | −0.838820 | −0.332150 | 0.174521 | 0.397002 | 0.397002 | 1.013341, 1.013341, 0.444963, 0 |
| 0.65625 | −0.957040 | −0.452120 | 0.052799 | 0.317823 | 0.317823 | 1.009839, 1.009839, 0.530047, 0 |
| 0.6625 | −1.080033 | −0.576864 | −0.073695 | 0.233984 | 0.233984 | 1.006338, 1.006338, 0.615357, 0 |
| 0.66875 | −1.208045 | −0.706625 | −0.205205 | 0.145238 | 0.145238 | 1.002840, 1.002840, 0.700886, 0 |
| 0.675 | −1.341336 | −0.841664 | −0.341991 | 0.051321 | 0.051321 | 0.999345, 0.999345, 0.786625, 0 |
| 0.7 | −1.933073 | −1.440371 | −0.947668 | −0.454965 | −0.381892 | 0.985405, 0.985405, 0.985405, 0.146146 |

Anatomy, as registered: at fixed t the margin's
B-slope is the channel's delivery sensitivity where
the clamp binds (≈ 1.0 per unit B at the late
instants, the s̄-class slope), exactly 0 wherever
neither arm is clamped at that t (the reads are then
the same read — §3(g)(i)), and partial in the
transition rows (0.5625 and 0.6 saturate early because
their unclamped amplitudes, −2.162202 and −2.391213,
are reached already at B = 2.5/2.0 respectively). The
t = 0.7 row is the one row where B = 3.0 and B = 3.5
still differ (rate 0.146146): past the crossing, the
3.5 arm is unclamped until 0.755686 while the 3.0 arm
clamps from 0.689844 — the separation the checker C5
verified fresh.

## 6. ADMISSIBILITY GATES (§4 — all PASS, no arm
## refused)

The B = 3.0/3.5 arms pose amplitudes beyond Phase
252's audited range [0, −2.5]; the gates were the
price of quoting them.

- **G-B1 (delivery exactness at peak amplitude, H1
  verbatim):** max |measured − linear| on NEC_φ,min
  over t ∈ {0, 0.25, 0.475}: B = 1.5 → 2.73×10⁻¹⁰;
  B = 2.0 → 3.64×10⁻¹⁰; B = 3.0 → 5.46×10⁻¹⁰;
  B = 3.5 → 6.37×10⁻¹⁰ — all ≥ 3 orders under the
  1×10⁻⁶ bar. The flat member's delivery stays
  affine-exact to a = −3.5. Checker C6 re-derived the
  B = 3.5, t = 0.475 point fresh: deviation
  1.4665602066088468×10⁻¹¹, matching the driver's
  stored value at diff 0.0. (This EXTENDS the
  affine-exactness observation to −3.5 as a measured
  property of this read; it does not amend Phase
  252's "no finite boundary in [0, −2.5]" statement,
  which stands in its range — §8.)
- **G-B2 (PR-φ at peak amplitude):** all arms pass,
  flat member at a = −B (t ∈ {0, 0.25, 0.475, 0.5625})
  and law-adapted at the arm's bracket ends: PR1
  offset extraction exact (diff 0.0); Wuu-solve
  residual ≤ 4.1×10⁻¹⁶; mom_ρ/mom_θ max ≤ 4.8×10⁻¹⁶;
  liveness ≥ 3.75 (bar 1×10⁻³); non-clause bars of
  record pass.

**Structural cross-check (§3g):** (i) equal-amplitude
arm pairs agree at max deviation **0.0** across all 41
sampled + 8 fixed instants; (ii) both-clamped affine
prediction: max deviation **5.30×10⁻¹⁰** over 23
pair/instant rows (bar 1×10⁻⁶). The read's
assumptions hold at every swept point.

## 7. CHECKER (independent; 8/8 PASS)

Fresh marches by the checker's own driver (main
15.8 s, aux 33.3 s; the Phase 265 driver not imported
or called as evidence): C1 CTRL-2 anchor at diff 0.0
against both the driver's and Phase 252's stored
margins; C2 the deciding coincidence re-derived fresh
(both arms, both ends, cross-arm diffs 0.0; fresh
41-instant scans: first fail t = 0.7, carriers exactly
{NEC_φ, DEC_φ}, no earlier crossing); C3 the B = 1.5 /
2.0 bracket ends at diff 0.0; C4 t_clamp arithmetic at
diff 0.0 and the form-1 condition t_clamp(3.0) ≥
0.68125 confirmed; C5 fixed-t spot rows at diff 0.0
including the t = 0.7 B = 3.0/3.5 separation; C6 the
G-B1 spot point (§6); C7 verdict-form consistency
re-applied mechanically from the stored results alone
(form 1 fires; forms 2 and 3 do not); C8 protected
md5 identity live (15 files, zero mismatches).
Driver wall 111.3 s total; checker 64.1 s; nothing
packaged (the §6 900 s trigger never approached).

## 8. FENCES AND WHAT THIS PHASE DOES NOT DO

READ grade only. The certified bracket remains
(0.65625, 0.6625] **as a statement about the pose
clamped at B := 2.5** — Phase 256's certificate and
Gate-26's restated G26-A stand untouched; this phase
adds the sensitivity record around them and the
stop-free read (0.675, 0.68125], which is a READ, not
a certificate: no Richardson ladder was run on it,
and any verdict-grade wording for the unclamped pose
is a future certification registration's and gate's
act (the natural successor: a Phase 243-pattern
certification of the unclamped-law bracket, whose
registration no longer needs a stop parameter at
all). The trim coefficient remains the Phase 248
fitted pose parameter with its Gate-26 §4(3b)
provenance; B remains an operational stop wherever
it binds — retiring it at read grade means the
bracket is demonstrably not an artefact of its
choice, not that any B was promoted to a physical
boundary. Phase 252's "no finite boundary in
[0, −2.5]" is neither extended as a claim nor
contradicted: §6's gates are this read's
admissibility evidence at the swept amplitudes.
Jet scope; sector superposition; datum ≠
construction; programme-level sustainment wording
remains gated by p1592 regardless.
