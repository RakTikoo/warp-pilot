# Novelty & Verification Gate 12 — GATE12.md (ground record)

**Status:** COMPLETE (2026-11-23) — **G12-1 SURVIVED
INTACT** (correctness REPRODUCED, confirmation-form
novelty as delimited below); **G12-2 UPLOAD-READY AFTER
RESTATEMENT** (correctness REPRODUCED WITH
RESTATEMENT — one catch on the ξ̈ coefficient's time
variable, anatomised in full below; novelty NOVEL in
the delimited form). Checker **35/35 PASS**
(`results/g12_check.json`). Nothing was uploaded; the
ledger was NOT edited; no phase record was edited.
**Work dir:** `~/workspace/warp-pilot/gate12/` — fresh
verifier code (`g12_le.py`, `g12_le_run.py`,
`g12_endowed.py`, `g12_c_bruteforce.py`,
`g12_followups.py`, `g12_check.py`), numbers and the
search log in `results/`.
**Parent records:** `../gate11/GATE11.md` (form and
method), `../phase96/CHECKPOINT96.md` §P96-1(b)+(c)
and §P96-3(a) integrated verdicts (the claims as
made), `../phase96/results/p961_memo.md`,
`../phase96/results/p963_memo.md`.
**This gate prepares verdicts only. It uploads
NOTHING, contacts no one, and edits no phase record
and no ledger.** Ledger edits are PROPOSED at the end
of this file, not applied.

## Standards (identical to Gates 5–11)

float64 everywhere; 40-digit mpmath on deciding reads.
The gate's bars are the programme's: full-volume
all-directions NEC + full EC set; Type-I +
sampled-null + margins. Fresh machinery written for
this gate — no phase code imported as deciding
machinery (coefficient sets, anchor targets and
shared definitions imported as data/text only).
Verdict categories per axis and gate verdicts as in
Gate-11. Uniqueness Protocol binding: nothing is
called first/record/novel beyond what the documented
search supports; coverage gaps stated.

## The claims (exact statements as tasked)

- **G12-1 (confirmation form):** Phase 96's
  confirmation, at this programme's bars, of Le's
  (0.7, 0.09) pin for the multipole accelerating shell
  (arXiv:2606.22531) — the hard frame-constrained
  solve read closure 1.989×10⁻³ against the 2.0×10⁻³
  bar, Type-I everywhere, worst DEC margin
  +1.346×10⁻², zero non-finite rows of 221. The
  claim's open clause rides verbatim in any wording
  (see the upload wording below).
- **G12-2 (new-object form):** Phase 96's
  endowed-shell spectrum — the P61-1 shell endowed
  with the Brown–Gladush surface perfect-fluid action
  (a NEW labelled object, NOT the conformal member)
  has an ℓ=0 fixed-bulk spectrum, stable at the
  action's linear EoS (ω² = +7.894×10⁻¹⁰ r₀⁻², sign
  claimed at 40 digits), unstable if pressureless.
  Scope discipline is the claim: the endowed object
  and the conformal member stay strictly separate;
  the member's own shell sector remains UNPOSABLE in
  pure Weyl gravity, and (V-b) UNDECIDED rides
  verbatim wherever the member is mentioned.

---

## G12-1 — correctness (fresh path)

**Machinery:** `gate12/g12_le.py` — a from-scratch
pure-numpy FD auditor: the Kinnersley photon-rocket
exterior (Kerr–Schild form, retarded time by Newton
root-finding) and the flat Rindler interior rebuilt
from the paper's own published forms; multipole shell
shape and per-side frame seeds from the paper's
Supplement/code specification; Christoffels built
algebraically from FD metric derivatives (this gate's
own implementation — its first draft carried a
transpose error in the Christoffel contraction,
caught and fixed against the analytic interior
Christoffels BEFORE any anchor was run; no number
was read from the broken draft); Lanczos stress;
Hawking–Ellis type via the (τ,θ)-block discriminant;
Eq.-(35) worst-observer DEC margins; sampled-observer
DEC cross-check. No `p715_lib`, `p801_lib`,
`p881_jax`, `worldtube` or `warpax` import anywhere.

**Anchors (all passed BEFORE any deciding number;
bar |diff| < 5×10⁻⁷, the Phase-96 re-gate bar):**
dipole pole x = 0.1: −2.009572×10⁻⁴ (target
−2.0096×10⁻⁴, diff +2.8×10⁻⁹); dipole pole x = 0.3:
−1.226338×10⁻⁴ (target −1.2263×10⁻⁴, diff
−3.8×10⁻⁹); Phase-80 confirmed-pin poles: x = 0.1
rear +1.728328×10⁻³ (diff +2.8×10⁻⁸), x = 0.3 front
+9.102104×10⁻³ (diff +4.3×10⁻⁹).

**Deciding audit of the stored confirming set**
(`x0.7_L6_fromZeros`, Phase-80-pattern pole-inclusive
grid, 221 points, h = 0.01 order 2):
- closure (residual of record, [h] components
  ττ/τθ/θθ): **1.989087×10⁻³ ≤ 2.0×10⁻³ bar** —
  agrees with Phase 96's FD audit evaluation
  (1.9891×10⁻³) to all printed digits and with its
  JAX own-evaluation (1.9893×10⁻³) within 2×10⁻⁷;
- **0 non-finite rows of 221**; **Type-I at every
  grid point** (min discriminant +1.307×10⁻³ class);
- worst DEC margin **+1.345981×10⁻² at θ = 2.4775**
  (phase: +1.3460×10⁻² at the same angle; agreement
  within FD truncation, 1.7×10⁻⁷ absolute);
- frame margin fm_min **+4.2877×10⁻³** (phase
  +4.288×10⁻³) — the shared frame is timelike at
  every audit angle, above the constraint δ = 10⁻³;
- sampled-observer DEC at the binding angle
  **+1.204×10⁻²** (phase +1.087×10⁻²; different
  sampler seed — sign and magnitude class agree);
- h-ladder at the binding angle converged, spread
  **2.95×10⁻⁴** (phase 2.9×10⁻⁴);
- poles: rear +3.788×10⁻², front +2.975×10⁻², both
  Type-I (phase values, reproduced).

**Corroborating anatomy (the from-A set, same pin):**
this gate's audit reproduces Phase 96's named
distinction exactly — closure 7.826×10⁻⁴ (deeper),
worst margin +1.730942×10⁻² at θ = 2.5868, but
**exactly 1 non-finite row** and fm_fd_min
**−5.6908×10⁻⁵** (phase −5.690805×10⁻⁵): the
inter-node dip at θ ≈ 2.7202 is real on this path
too, and the from-zeros set remains the confirming
set. The distinction between the constraint grid and
the audit grid is where that dip lives, as Phase 96
recorded.

**The open clause, re-derived on this path:**
- the (0.5, 0.14) constrained-floor sets, read with
  h-only evaluations on the dense61 grid: L = 8 best
  strictly-feasible set closes at **1.606143×10⁻²**
  (phase 1.606×10⁻², agreement to 7 digits), L = 6 at
  **1.757490×10⁻²** (phase 1.757×10⁻²) — both ~8× the
  closure bar, both constraint-active (fm_min on
  dense61 +1.20×10⁻³ / +1.04×10⁻³ ≈ δ);
- alternative frames on Phase 88's degenerate
  strategy-A set at x = 0.5 (constructible class
  {shared, pure-time, flipped, swapped, unit-time} ×
  both sides, this gate's machinery): F0 **−0.548303**,
  F2 −0.547499, F3 −0.555639, F4 −0.242071 — every
  tilt-carrying seed spacelike in the rear band,
  matching Phase 96's FD probe to all printed digits;
  the pure-time seed F1 reads **+2.52×10⁻⁵** on this
  FD path, i.e. at FD truncation scale, consistent
  with Phase 96's exact JAX read of **+6.6×10⁻⁷**
  (null within ~10⁻⁶) and not contradicting it — this
  gate's FD floor at that site is ~10⁻⁵, recorded as
  such; the near-nullity clause therefore stands on
  the phase's exact read, corroborated in kind here;
- control: on the (0.7, 0.09) confirming set all five
  frames are comfortably timelike on this path
  (F0 +4.433×10⁻³, F1 +4.535×10⁻³, F2 +4.416×10⁻³,
  F3 +4.15×10⁻⁴, F4 +0.120470 — phase FD values,
  reproduced).

**Correctness: REPRODUCED.**

## G12-1 — novelty (confirmation form)

Search log: `results/g12_search_log.md` (queries
Q1–Q2 verbatim; sources: arXiv listing/PDF of the
paper, general web). No independent confirmation or
refutation of any of Le's multipole pins, and no
discussion of the (0.7, 0.09) or (0.5, 0.14) pins at
any residual level, was found outside this programme.
Coverage gaps: INSPIRE-HEP and Semantic Scholar not
reached in native sessions (indexed content only);
non-English literature not searched. The claim is
worded as OUR independent confirmation at OUR bars —
never priority over the author, whose published
x = 0.7 margin (21×10⁻³) belongs to the paper's own
unpublished coefficient set.

**G12-1 GATE VERDICT: SURVIVED INTACT.**

## G12-1 upload wording (verbatim, the only form in
which this claim may be carried)

> **Accelerating shell (subluminal, Bobrick–Martire
> class — never FTL).** Le's multipole accelerating
> shell (arXiv:2606.22531) is confirmed at this
> programme's bars at the (x, λ) = (0.7, 0.09) pin:
> a hard frame-constrained solve (timelikeness
> −h_ττ ≥ δ = 1×10⁻³ imposed as a constraint of the
> solve, with exact autodiff Jacobians of the
> residual and the constraints) produced an
> independently stored L = 6 coefficient set that
> closes at max|[h]| = 1.989×10⁻³ against the
> 2.0×10⁻³ bar under two evaluations, and passes the
> full pole-inclusive audit — zero non-finite rows
> of 221, Hawking–Ellis Type-I at every grid point,
> worst DEC margin +1.346×10⁻², frame margin
> +4.288×10⁻³. Gate-12 independently reproduced the
> confirmation on a fresh from-scratch auditor
> (anchors ≤ 2.8×10⁻⁸; closure 1.989087×10⁻³; worst
> margin +1.345981×10⁻² at the same binding angle;
> the companion from-A set's single non-finite row
> and its −5.69×10⁻⁵ inter-node frame dip reproduced
> exactly). This is our independent confirmation at
> our bars (including the pole-exact read), not a
> priority claim over the author: the paper's own
> published margin at this pin (21×10⁻³) belongs to
> the paper's unpublished set. The claim's open
> clause rides verbatim: the (0.5, 0.14) pin remains
> STILL UNCLOSEABLE at one level deeper (best
> constrained fit 1.606×10⁻²; obstruction = the
> shell's rear hemisphere within ~10⁻⁶ of
> frame-nullity under every constructible frame — a
> shell property, class-scoped) — untested is not
> impeached, in either direction.

---

## G12-2 — correctness (fresh paths)

**Machinery:** `gate12/g12_endowed.py` — the two bulk
metrics rebuilt from their registered definitions;
K̄ geometry derived from the covariant definition;
three paths: (1) sympy analytic float64; (2) mpmath
40-digit full recomputation of every deciding value;
(3) finite-difference path for every K quantity and
its radial derivative (relative errors ≤ 1.3×10⁻⁵),
plus two independent constructions of the ξ̈
coefficient C (below). Shared data only: a =
0.27773424114865775, p = 0.1, r_Σ = 1,000 r₀, the
registered-γ MK exterior parameters and σ₀ from the
stored P61-1 shell datum.

**Reproduced exactly (all at the phase's values):**
K̄^t_t(0) = +4.4369985428×10⁻⁶ r₀⁻¹ and
K̄^θ_θ(0) = +9.9900187071×10⁻⁴ r₀⁻¹ (identical on
both sides); admissibility w₀ = p₀/σ₀ =
+0.0022207158329 (p₀ = +4.5061523831×10⁻⁵ α₀); the
literal dust sub-case inadmissible (residual
−4.4369985428×10⁻⁶ per unit σ₀); D_R =
−1.5233785879×10⁻⁵, D_Rn = +1.8844230756×10⁻⁵
(recomputed from the R̃ defining formula with fresh
sympy code; [R̃_,n] at Σ = −0.01521858059121 vs
stored −0.01521858059122); the fixed-bulk J3 strain
vs conservation strain ratio **0.6177473545**; the
spectrum law's threshold β² = **0.0020611430310**
(40-digit: 0.00206114303102618371…); and, *with the
phase's C*, ω²(w₀) = +7.8937794457691367370…×10⁻¹⁰
and ω²(0) = −1.0196103785374905956…×10⁻⁸ at 40
digits — the phase's arithmetic is exact given its C.

### THE CATCH — the ξ̈ coefficient's time variable

The phase's C_avg = +0.8095870468 is
√B/A per side (interior 0.6161737182, exterior
1.0030003754). Its checker entry for C is circular:
labelled a trajectory extraction, it re-evaluates
the same √B/A formula (p963_check.py, read in this
gate). This gate extracted C two genuinely
independent ways:

1. **Proper-time trajectory path**
   (`g12_endowed.py`): trial worldlines
   R(τ) = R₀ + ½ατ² (τ = shell proper time, t(τ)
   integrated from the proper-time condition),
   K^t_t = −K(u,u) evaluated from the worldline
   construction; the α-slope is **√B per side**
   (1.0009991265 both sides — B is continuous at
   this Σ), NOT √B/A: interior slope 1.0009991265
   vs the phase formula's 0.6161737182 (62% off);
   exterior slope 1.0009991265 vs 1.0030003754
   (0.2% off — the exterior's A ≈ 0.998 masks the
   distinction there, which is how the error
   survived the phase's spot checks).
2. **Brute-force Φ-field FD path**
   (`g12_c_bruteforce.py`): moving shell
   R(t) = R₀ + ½α_t t² in bulk coordinate time,
   normal field from grad Φ in Cartesian
   coordinates, full FD ∇n: static −K(u,u) =
   +4.436999×10⁻⁶ matches the analytic static value;
   the α_t-slope of K^t_t is **+0.6164 (interior) /
   +1.0034 (exterior)** = √B/A per side, linear in
   α_t (slope stable to 6×10⁻⁴ between α_t = 10⁻³
   and 2×10⁻³). Since R̈_τ = R̈_t/A at the static
   point, this is the same statement as path 1:
   **K^t_t ⊃ √B · R̈_τ = (√B/A) · R̈_t.**

Anatomy: the phase's derivation (its compute code's
comment) writes "C = √B · u_t² with u_t = 1/√A" —
1/√A is u^t, not u_t; the correct proper-time
coefficient from K^t_t = −n·a is √B. The phase's C
is exactly the coefficient of the **bulk
coordinate-time** second derivative. Its spectrum
values are therefore squared **coordinate-time**
frequencies, while its memo and results law state
"τ = shell proper time". Rescaling to proper time
(ω² ∝ 1/C, factor C_phase/C_true =
0.8087789742548870931… at 40 digits; the threshold
is C-independent and unchanged):

- ω² at the linear EoS, proper time:
  **+6.3843228431434735479…×10⁻¹⁰ r₀⁻²** (ω =
  2.5267217581568955864…×10⁻⁵ r₀⁻¹) — **sign
  positive at 40 digits, as claimed**;
- ω² at β² = 0, proper time:
  **−8.2463943609318879003…×10⁻⁹ r₀⁻²** — unstable,
  as claimed;
- β² threshold **0.0020611430310** — unchanged.

Nothing else in the claim moves: the spectrum
exists, the linear-EoS mode is stable, the
pressureless branch is unstable, the dust sub-case
is inadmissible, ℓ ≥ 1 is not closed by this
action, and the fixed-bulk scope (strain ratio
0.6177473545 carried) is untouched. The catch is a
mislabelled time variable / wrong coefficient —
a value correction of 24% in ω², not a sign or
existence failure.

**Correctness: REPRODUCED WITH RESTATEMENT** (the
restated wording below carries the proper-time
values and names the phase's values as the
coordinate-time reading).

## G12-2 — novelty (new-object form)

Search log: `results/g12_search_log.md` (queries
Q3–Q7 verbatim). Near neighbours, all different
objects: Bochicchio–Laserra (arXiv:1301.1532) — two
identical MKdS copies, imposed Chaplygin-gas EoS,
Eiroa/Weierstrass stability, no matter action, no
fixed-bulk spectrum; "Stability of generic thin
shells in conformally flat spacetimes" — imposed
linear EoS, not an action endowment, not this join;
Kijowski–Magli–Malafarina (PRD 74 (2006) 084017) and
Gladush (arXiv:gr-qc/0312067) — the GR action
literature the endowment draws on, no conformal
join and no such spectrum; Grumiller et al.
(arXiv:1310.0819) — conditions at infinity, no
shell. Delimitation: not found in our search
(limits: INSPIRE-HEP and Semantic Scholar reached
only via indexes, no native sessions; non-English
literature not searched; one query failed once on a
tool timeout and was re-run in altered form) — any
published ℓ = 0 fixed-bulk spectrum of a shell
obtained by endowing a conformal-gravity joined
shell with a surface perfect-fluid matter action,
in particular of the P61-1 shell under the
Brown–Gladush action.

**Novelty: NOVEL** (in the delimited form above).

**G12-2 GATE VERDICT: UPLOAD-READY AFTER
RESTATEMENT.**

## G12-2 upload wording (verbatim, the only form in
which this claim may be carried)

> **A new labelled object — not the conformal
> member.** The P61-1 shell endowed with the
> Brown–Gladush surface perfect-fluid action (Brown,
> Class. Quantum Grav. 10 (1993) 1579; Gladush,
> arXiv:gr-qc/0312067 eq. (2.23)) — the P61-1
> background (Φ2 interior, joined at r_Σ = 1,000 r₀
> to the registered-γ MK exterior, σ₀ =
> +0.02029144078829105 α₀) with its shell matter
> given that action — possesses the ξ̈ equation the
> member lacks: its normal equation
> S^{ab}K̄_{ab} = 0 carries d²R/dτ² (τ = shell
> proper time) with averaged coefficient √B =
> +1.0009991265 (Gate-12 correction: Phase 96's
> coefficient √B/A is the coefficient of the bulk
> coordinate-time second derivative; its published
> ω² values are squared coordinate-time frequencies
> and are restated here in proper time). Background
> admissibility fixes the endowed fluid's own
> p₀ = +0.0022207158329 σ₀; the literal dust
> sub-case does not admit this background (residual
> −4.4369985428×10⁻⁶ per unit σ₀). The ℓ = 0
> fixed-bulk spectrum of the P61-1 shell endowed
> with the Brown–Gladush surface perfect-fluid
> action is ω²(β²) linear in β² with stability
> threshold β² = 0.0020611430310: at the action's
> linear EoS (β² = w₀), **ω² =
> +6.384×10⁻¹⁰ r₀⁻² (proper time; sign confirmed at
> 40 digits: +6.3843228431434735479…×10⁻¹⁰) —
> stable** (the coordinate-time reading of the same
> mode is +7.894×10⁻¹⁰ r₀⁻²); at β² = 0, ω² =
> −8.246×10⁻⁹ r₀⁻² (proper time) — unstable. This
> is the endowed shell's own fixed-bulk dynamics
> (the fixed-bulk junction strain and the action's
> conservation strain differ by the ratio
> 0.6177473545, carried, not hidden); ℓ ≥ 1 is not
> closed by this action (no tangential displacement
> or shear response). No sentence here is about the
> conformal member: the member's own shell sector
> remains **UNPOSABLE in pure Weyl gravity**, and
> this spectrum does not revise that standing.
> **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs
> Mannheim PT-symmetric quantisation — opposed
> literature positions, B3 NOT COMPUTABLE
> (Phase 32).** Not found in our search (limits:
> INSPIRE-HEP and Semantic Scholar reached only via
> indexes; non-English literature not searched):
> any published ℓ = 0 fixed-bulk spectrum of a
> conformal-gravity joined shell endowed with a
> surface perfect-fluid matter action. No
> traversability claim is made.

---

## Proposed ledger edits (PROPOSED, not applied)

**For G12-1** (new GATE-VERIFIED entry, accelerating-
shell category):

> **Le (0.7, 0.09) pin, GATE-VERIFIED confirmation**
> (Phase 96, Gate-12 — SURVIVED INTACT: correctness
> REPRODUCED on a fresh from-scratch FD auditor,
> anchors ≤ 2.8×10⁻⁸, closure 1.989087×10⁻³ vs the
> 2.0×10⁻³ bar, Type-I everywhere, 0 non-finite rows
> of 221, worst DEC +1.345981×10⁻², fm
> +4.2877×10⁻³): the hard frame-constrained solve's
> L = 6 set confirms Le's x = 0.7 multipole pin at
> our bars — our independent confirmation, not
> priority over the author. The (0.5, 0.14) pin
> remains STILL UNCLOSEABLE (Gate-12 re-read the
> constrained floors: 1.606×10⁻² at L = 8,
> 1.757×10⁻² at L = 6; the degenerate set's rear
> band is spacelike under every tilt-carrying
> constructible frame and within ~10⁻⁶ of nullity
> under the pure-time frame, per the phase's exact
> read, corroborated in kind) — untested is not
> impeached, in either direction. The claim may be
> carried only in Gate-12's upload wording
> (gate12/GATE12.md). Basis: P96-1(b)+(c) (checker
> 23/23); Gate-12 (checker 35/35).

**For G12-2** (new GATE-VERIFIED entry, new-object
category):

> **Endowed-shell spectrum, GATE-VERIFIED WITH
> CORRECTION** (Phase 96, Gate-12 — UPLOAD-READY
> AFTER RESTATEMENT: correctness REPRODUCED WITH
> RESTATEMENT, novelty NOVEL delimited): the P61-1
> shell endowed with the Brown–Gladush surface
> perfect-fluid action — a new labelled object, NOT
> the conformal member — has an ℓ = 0 fixed-bulk
> spectrum, stable at the action's linear EoS and
> unstable if pressureless, threshold β² =
> 0.0020611430310. Gate-12 catch: the phase's ξ̈
> coefficient √B/A is the bulk coordinate-time
> coefficient; the proper-time coefficient is √B,
> so the proper-time values are ω² =
> +6.384×10⁻¹⁰ r₀⁻² at the linear EoS (sign + at 40
> digits) and −8.246×10⁻⁹ r₀⁻² at β² = 0; the
> phase's +7.894×10⁻¹⁰ / −1.020×10⁻⁸ are the
> coordinate-time readings of the same modes. The
> member's shell sector remains UNPOSABLE in pure
> Weyl gravity, unrevised. **(V-b) UNDECIDED:
> Pais–Uhlenbeck spin-2 ghost vs Mannheim
> PT-symmetric quantisation — opposed literature
> positions, B3 NOT COMPUTABLE (Phase 32).** The
> claim may be carried only in Gate-12's upload
> wording (gate12/GATE12.md). Basis: P96-3(a)
> (checker 17/17); Gate-12 (checker 35/35).

**Upload-ready list:** G12-1 (SURVIVED INTACT) and
G12-2 (restated form only) — ONLY in the upload
wordings recorded verbatim above. Nothing was
uploaded by this gate; publication follows the
parent's standing rule.

**Status: COMPLETE** (both items run on fresh
machinery; verdicts integrated; record closed
2026-11-23).
