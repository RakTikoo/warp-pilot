# GATE-26 — ADJUDICATION OF THE PHASE 256 CERTIFIED CLAIM SET
# (the combined-class bracket; amending the Gate-22/Gate-23
# sustainment set)

Date: 2026-11-24. Adversarial re-judgement, not a phase. Frame
of record: Phase 166 pin, Gate-19-corrected tensor, venv python
(numpy 2.5.5 / scipy 1.18.1). Method: Gate-26 re-derived every
deciding number from the stored artefacts of Phases 243/252/256
with its own arithmetic (`gate26/work/g26_verify.py` →
`gate26/work/g26_verify_results.json`) — pure JSON arithmetic
on the stored per-grid rows; no programme engine was imported,
no Phase 256 driver or checker was used as evidence, and no
march was re-run (spot recomputation only, per the Gate-23
pattern). In parallel, the registration was audited by full
text diff against Phase 243's and the two priced scope
questions (the B := 2.5 stop; the fitted trim coefficient)
were adjudicated from the Phase 246/248/252 record
(`gate26/work/g26_scope_audit.md`). Independence, priced on
the face: the gate's arithmetic path is independent of Phase
256's driver and checker at the arithmetic level (it
re-derives from the same stored rows — the same independence
class as Gates 15/19/22/23).

## VERDICTS

- **G26-A: SURVIVES IN RESTATED WORDING** (restated wording in
  §3). The certificate's arithmetic is fully verified — the
  bracket limits reproduce at 0.0 deviation. The corrections
  are the Gate-23 class: the claim's wording attaches the
  certificate to a seven-clause interval span whose evidence
  is mostly standing-grid sampled reads (§3), and it does not
  price what this certificate actually measures — for this
  pose the Richardson ladder is a **grid-stability**
  certificate, not a convergence certificate (§2) — nor name
  the certified object exactly (the trim law **as clamped at
  B := 2.5**, with a **fitted** coefficient; §4).
- **G26-B: SURVIVES INTACT.** Both brackets certified under
  the same instrument at the same bar on the same binding
  clauses; the brackets are disjoint and ordered
  (0.5625 < 0.65625), recomputed at 0.0 deviation (§1). The
  evidential asymmetry priced in §2 attaches to G26-A's
  restated wording and is carried there; it does not move
  any number in the comparison.
- **G26-C: SURVIVES INTACT.** All four fences verified —
  window/sampled scope, tail reads not certified (tail
  pricing recomputed exactly, §1), jet scope / sector
  superposition, the p1592 gate untouched. Two record notes
  are priced in §5 (a fifth registration adaptation,
  face-disclosed; the unpriced sensitivity of the bracket
  to the stop's value) — neither touches a fence as stated.
- **Novelty: NONE granted** — Gate-22 §6's position carries
  over unchanged (§6).

No claim FAILS. No deciding number in Phase 256's record
failed to reproduce: the gate's recomputation of the
certificate table matches at 0.0 deviation in every
verdict-carrying field (v3/v4/v5, d34, d45, p, L), the
bracket-end limits are exact, CTRL-2 replays exactly from
Phase 252's stored rows, and the tail pricing is exact
against Phase 256's stored G3/G4 rows. Two sub-10⁻¹⁵
evaluation notes and one Phase 252 record gap are priced in
§1 — none touches a verdict.

---

## §1. Attack line (1) — the Richardson straddle,
## independently verified; the small print priced

Gate-26 recomputed the per-instant Richardson treatment from
the stored G3/G4/G5 window rows in `p2561_results.json`
(NEC_φ and DEC_φ — verified pointwise identical in every
stored window and tail row, max abs diff 0.0, so one row
serves both, as the record states), under the registration's
§3 definitions verbatim:

**The certificate reproduces.** All 10 window instants ×
both clauses: case = monotone, p ∈ [3.22973, 4.61471], every
instant limit-certified; CERT-1, CERT-2, CERT-3, CERT-4 all
TRUE under the gate's own evaluation. The straddle is real:
**L(0.65625) = +0.05279917238387332 ≥ 0,
L(0.6625) = −0.073694680424036624 < 0** — deviation **0.0**
from the claim at float64 precision — with v5 agreeing in
sign at both instants; CERT-3 holds (no earlier in-window
crossing at L or v5); CERT-4 holds (non-binding G5 minimum
over window instants ≤ t_hi = **+4.05210858855158 > 0**; the
non-clause bars at the bracket instants re-read from the
stored G5 rows: t = 0.65625 — momentum worst
6.106226635438361×10⁻¹⁶ ≤ 1×10⁻¹⁰, flare min
0.1218677961567533 > 0, domain R min 0.6034021651754861 > 0,
exp(2Φ) min 0.005811244884212129 > 0; t = 0.6625 — momentum
4.996003610813204×10⁻¹⁶, flare 0.12068808091222741, domain R
0.5996396125090033, exp(2Φ) 0.005811244842692699 — all pass,
matching the recorded CERT-4 bars).

**CTRL-2 replays exactly.** From `p2522_results.json`'s
stored rows alone: sampled bracket (0.65, 0.675], first-fail
carriers exactly {NEC_φ, DEC_φ}; the halving ladder replays
to (0.65625, 0.6625] with end margins
+0.05279917238250764 / −0.07369468042669158; the bracket
decomposition identity (headline + lift = composed) holds at
exactly 0.0 at both ends; the stop instant
√(2/5.253378) = 0.6170149292514079, within 7.1×10⁻⁸ of the
recorded 0.617015 (bar 1×10⁻⁶).

**Tail pricing (for §5).** Recomputed from Phase 256's
stored fresh G3/G4 rows on (0.75, 1.0]: per-instant maxima
reproduce the recorded table exactly (1.674898×10⁻⁶ at
0.775 rising to 1.201324×10⁻⁵ at 0.975); first exceedance
of the 1×10⁻⁶ bar at **t = 0.775** (the first tail
instant); stage max **1.6326915963205124×10⁻⁵ at t = 1.0,
carrier DEC_θ**, relative disagreement
1.8932984155740035×10⁻⁶ — bit-for-bit the recorded pricing.

**The comparison numbers (for §5/G26-B).** Recomputed from
Phase 243's stored three-channel window rows:
L(0.55625) = +0.004468142716485732,
L(0.5625) = −0.054339801013359036 — deviation 0.0 from both
the claim and Gate-23's recorded values. Same 1×10⁻⁶ bar,
same binding clauses {NEC_φ, DEC_φ}, same window discipline
(§4). The brackets are disjoint and ordered:
0.5625 < 0.65625.

**Three small notes, priced.**

(i) *Residual evaluation order (nil).* The recorded
`resid` field is |L − v5| evaluated as a float64
subtraction, not the algebraically identical
|d45|/(2^p − 1). Under the float-subtraction evaluation
the gate's r matches the record at 0.0 deviation at every
instant; under the formula evaluation it differs by up to
1.417×10⁻¹⁶ (worst r 2.225492517544063×10⁻¹⁵ vs recorded
2.220446049250313×10⁻¹⁵). L, p, the case classifications
and every certification are unaffected under either
evaluation.

(ii) *Case-classification split (inert here).* Gate-23 §1
noted that Phase 243's driver implements the monotone case
with admissibility (0.5 ≤ p ≤ 6) folded into the case
definition. Gate-26 evaluated the literal alternative
(monotone by sign of d34·d45 alone, admissibility checked
separately): every window instant's p is admissible under
either reading, so **no instant's case or certification
changes** — the ambiguity that was live (though priced
nil) at two Phase 243 instants does not arise here.

(iii) *One Phase 252 number the stored record does not
fully underwrite.* The re-posed datum's NEC_φ margin at
t = 0.5625 (+1.126925, quoted in Phase 252's checkpoint and
in the restated G26-A's trajectory note) is not a
full-precision stored row: t = 0.5625 is not on Phase
252's 0.025-spaced sampled lattice, and the value survives
only as the rounded detail string of `p2522_verify.json`'s
spot check `holds_at_wound_far_end` (pass = true) — a fresh
read by Phase 252's own checker, consistent at the six
decimals recorded, not independently recomputable from
stored rows. It carries no part of the certificate (the
bracket ends and window rows are all stored at full
precision); it is priced here so the record carries the
distinction, and the restated wording in §3 marks it as a
checker-read value.

## §2. Attack line (2) — what this certificate measures:
## grid stability, not convergence (the A2 pricing)

Phase 256's memo §4 records the anatomy on its own face,
and the gate's recomputation confirms it: the
combined-class binding minima are a read-level sector off
the marched state, interpolated onto the fixed audit grid,
and the three ladder grids agree on them to the float64
rounding floor — worst |d34| = 1.7497114868092467×10⁻¹³
(t = 0.725), worst |d45| = 1.865174681370263×10⁻¹⁴, worst
residual r = 2.220446049250313×10⁻¹⁵ (recorded evaluation).
Priced per component against the 1×10⁻⁶ bar, in Gate-23
§1's format:

| component | worst | factor under the 1×10⁻⁶ bar |
|---|---|---|
| \|d34\| | 1.7497114868092467×10⁻¹³ (t = 0.725) | **5.72×10⁶×** |
| \|d45\| | 1.865174681370263×10⁻¹⁴ (t = 0.725) | **5.36×10⁷×** |
| residual r | 2.220446049250313×10⁻¹⁵ (t = 0.725) | **4.49×10⁸×** |

Contrast Gate-23 §1's table for the wound pose
(2.87× / 11.49× / 34.47× — a genuine discretisation error
shrinking at a measured order p ∈ [1.99999, 2.00003]).
Here the margins are six to eight orders of magnitude
under the bar because the disagreements are **rounding
noise, not truncation error**: the Richardson limit
coincides with the finest-grid read to 15 digits
(L − v5 ≤ 2.3×10⁻¹⁵ at every instant), so CERT-2's
"at the limit AND at the finest grid" double test
collapses to a single statement, and the order reads
p ∈ [3.23, 4.61] are ratios of noise-floor differences
carrying **no convergence information**.

**What the certificate therefore does and does not
establish.** It establishes, at full weight: the bracket
is **not an artefact of the claim's standing grid**
(N_θ = 2881) — the ladder never uses that grid, and three
independent marches (G3/G4/G5) reproduce the bracket's
sign pattern and margins to ~10⁻¹³; CERT-3 (no earlier
in-window crossing) and CERT-4 (first-crossing uniqueness
at G5, non-clause bars) hold as registered; and the
instrument demonstrably *can* register disagreement where
disagreement exists — the same rows carry the tail's
DEC_θ disagreement at the 10⁻⁵ level (§1), so the
in-window agreement is a property of this read, not a
blind instrument. It does **not** establish a measured
convergence rate for the combined-class read, and no
wording may quote the p values, or the "nine orders of
magnitude" clearance, as convergence assurance. This is a
weaker certificate than Phase 243's in exactly that one
dimension and equal in all others; the restated G26-A
(§3) carries the distinction in its text, as Phase 256's
own memo (§4) already does in substance. The bar was not
relaxed and no CERT condition was waived — the conditions
are met as registered; what is priced is the evidential
character of their meeting.

## §3. G26-A — the bracket: SURVIVES IN RESTATED WORDING

The deciding numbers are verified (§1). What the original
wording outruns is its evidence structure, in the same way
Gate-23 §2 found for G23-A: "holds all seven throat
clauses on [0, 0.65625] at the sampled instants …
CERTIFIED at the Phase 243 standard (Richardson limits
…)" attaches the certificate to the whole span, but the
evidence is two distinct classes —

- on [0, 0.65625] at sampled instants: Phase 252's
  standing-grid march (N_θ = 2881; 27 sampled instants of
  [0, 0.65] plus the refined instant t = 0.65625), whose
  rows Phase 256's CTRL-1 reproduced at max abs diff 0.0
  (gate-verified via CTRL-2's replay and the stored rows:
  worst per-clause minima over the span — NEC_φ = DEC_φ
  **+0.05279917238250764** at t = 0.65625, the span's
  binding minimum; NEC_ρ = DEC_ρ +1.68125; NEC_θ = DEC_θ
  +1.6875750349885346; WEC +2.306493031032269; the
  non-binding minima sit at t = 0). This is a sampled
  standing-grid read, reproduced exactly — not a
  limit-certified one;
- on the window [0.6, 0.75]: the binding clauses
  NEC_φ = DEC_φ limit-certified at every window instant
  (CERT-1), the bracket straddled at the limit and at G5
  (CERT-2), no earlier in-window crossing (CERT-3), and
  the non-binding clauses positive at G5 at every window
  instant ≤ t_hi (CERT-4; next clause ≥ +4.188 at the hi
  end) — a G5-instant condition on the non-binding
  clauses, exactly as the certificate was registered, and
  a grid-stability certificate in the sense of §2.

Two further wording debts, both priced in §4: the
certified object is the trim law **as clamped at the
operational stop B := 2.5** (the stop binds from
t = 0.617015 — inside the window, before the bracket —
so every bracket instant is read at the clamped value
a ≡ −2.5), and the law's coefficient c_trim is a
**fitted** pose parameter (provenance §4), which the
claim's bare phrase "CH-PHI-Auu trim" does not state.

**Restated G26-A (the quotable form):** *On the Phase 169
A-branch throat datum with the true lock, the combined-class
pose (κ = 0.3 wound director + the Phase 245 C2 rotating
headline construction, W = 0.2 sin²θ + CH-PHI-Auu under
P-PHI-TRIM-248 — the open-loop trim law
a(t) = −0.5 − c_trim·t² with c_trim = +5.253378225339471
fitted in Phase 248 to the composed datum's measured drift
and frozen before every subsequent march — **as clamped at
the operational stop B := 2.5**, the stop binding from
t = 0.617015) meets every registered throat clause bar at
all 27 sampled instants of [0, 0.65] and at the refined
instant t = 0.65625 on the standing grid (N_θ = 2881;
worst clause minima over the span: NEC_φ = DEC_φ
+0.05279917238250764 at t = 0.65625; NEC_ρ = DEC_ρ
+1.68125; NEC_θ = DEC_θ +1.6875750349885346; WEC
+2.306493031032269 — the binding trajectory passing
NEC_φ = +1.126925 at t = 0.5625 by Phase 252's checker
read, §1 note (iii); rows reproduced by Phase 256 CTRL-1
at max abs diff 0.0), and on the registered window
[0.6, 0.75] its binding clauses NEC_φ = DEC_φ are
limit-certified at every window instant under per-instant
Richardson limits on G3/G4/G5 at the unchanged 1×10⁻⁶ bar
— the three grids agreeing to worst |d34| =
1.7497114868092467×10⁻¹³, worst |d45| =
1.865174681370263×10⁻¹⁴, worst residual
2.220446049250313×10⁻¹⁵, the limit coinciding with the
finest-grid read (a grid-stability certificate for a
read-level sector, not a measured convergence rate) — the
limits and the G5 reads straddling zero at the bracket
(L(0.65625) = +0.05279917238387332, L(0.6625) =
−0.073694680424036624) with no earlier in-window crossing
and every non-binding clause positive at G5 at every
window instant ≤ 0.6625 — so the pose's first crossing
sits at t ∈ (0.65625, 0.6625] on NEC_φ = DEC_φ, in the
certified scope of G26-C's fences. The interval is
[0, 0.65625] at the sampled, refined and window instants
named; no continuum claim between instants is made or
certified.*

## §4. Attack lines (3) and (4) — the stop, the fitted
## coefficient, and the registration's adaptations

**(3a) B := 2.5 — an operational stop, not a smuggled
assumption; one sensitivity unpriced.** The audit
(`g26_scope_audit.md` §2) establishes: 2.5 is derived
from nothing — it is the round endpoint of the amplitude
range Phase 252's registration fixed in advance for its
boundary sweep ([0, −2.5]), and Phase 252's record says
so outright ("the sweep end is the audit's limit, not a
boundary"; the sweep found **no finite boundary** in the
range — delivery affine-exact, all health conditions
passing, the t = 0 clauses *growing* with |a|). Nothing
in the claim needs 2.5 to be a boundary, and no wording
may call it one: Phase 256's fence (ii) already states
"an operational limit, not a priced boundary", and the
restated G26-A names the certified object as the law
*as clamped at* the stop. The stop's placement is fully
disclosed on the face of the record (Phase 252: "past
the comparison point but before the crossing"; Phase
256 §A1/§A3 carry the stop instant and the window side
by side): it binds from t_stop = √(2/c_trim) =
0.6170149292514079 (gate-recomputed), inside the window
[0.6, 0.75] and before the bracket, so only the window
instant t = 0.6 is read unclamped and **the entire
bracket is read at the clamped flat value a ≡ −2.5** —
the certificate certifies that pose, and the restated
wording says so. (One quotation fence: Phase 252 §3's
"runs unclamped through the deciding window" was true
only of Phase 252's comparison window and must not be
quoted for Phase 256's.) What was audited *at* the stop
value, exactly: the flat member's health conditions
H1–H4 at t ∈ {0, 0.25, 0.475} (Phase 252 Item 1) and a
flat pose-refusal read at t ∈ {0, 0.25, 0.475, 0.5625}
(Item 2, PR-φ/non-clause scope only). Not audited: the
flat member's health or clause legality at the bracket
instants (those instants are covered instead by Phase
256's own window reads of the clamped pose), anything
beyond 2.5, and **any B ≠ 2.5 — no sensitivity of the
bracket to the stop's value is on record.** That the
bracket is clamp-sensitive *as a class* is proven by the
record itself (the 0.8-clamped trim brackets at
(0.525, 0.53125], Phase 248; the 2.5-clamped at
(0.65625, 0.6625]) — unsurprising, since the bracket is
a property of the whole clamped trajectory (Phase 252's
descriptive flat equivalent at the hi end,
a_equiv = −2.743808, lies beyond even the stop: the
crossing is where it is because lift was banked along
the trajectory, not because the terminal amplitude alone
repays the drift). The absence of a B-sensitivity is a
priced gap in the record, carried here; it does not
impeach the certificate, which certifies the pose as
posed, but no wording may imply the bracket is robust
to the stop's choice.

**(3b) The trim coefficient — a legitimate fitted pose
parameter; a wording fence owed and now carried.** Chain
of custody (audit §3): the formula c_trim = −q₂/s̄ was
registered in Phase 248's registration (B1) *before* any
fit or march; the value was fitted in Phase 248 Part A —
q₂ = −6.062835, the c₂ coefficient of the full quadratic
least-squares fit to the composed arm's NEC_φ,min(t) over
[0, 0.475], divided by s̄ = 1.154083, the mean of Phase
246's stored Auu sensitivities — and frozen before Phase
248's own Part B march; Phase 252 used the **stored**
coefficient, explicitly not re-fit (its CTRL-B pins it);
Phase 256 copied it (CTRL-2(d), gate-verified). So the
coefficient's last exposure to the data it counters was
Phase 248 Part A, and the certified bracket
(0.65625–0.6625) lies **outside the fit window**
[0, 0.475] — the law is extrapolated there, on the
record. Amendment A-1 (Phase 248, recorded after the
fits were printed, before any Part B computation) does
**not** touch c_trim: it replaced only the forced-t²
*classification* sub-criterion and states that no other
registered form, window or formula changes; q₂ comes
from the full fit, which the classification rule
consumes but does not produce — the coefficient is
bit-identical with or without A-1. (A-1's disclosure
rides on the SAME-FORCED-MODE narrative of Phase 248 §2,
where it already stands on the face.) Legitimacy: the
certificate certifies the bracket **of the pose as
posed**; the coefficient was fixed in advance of every
march it governed and was never adjusted against any
bracket — the defining property of a pose parameter, not
of curve-fitting to the certified quantity. The law's
t² *form* is not an arbitrary basis either: the drift it
counters is the P169-1 forced mode, whose decomposition
is exact (Phase 248 §1: composed = headline + lift at
deviation 0.0 at all 41 instants), whose trajectory is
bit-identical to the untrimmed datum's, and whose
t² shape is the mode's own characterisation
(Phase 208: μ ≈ (t²/2)·ũ(θ), a forced particular
solution, not an instability). Open-loop fitted control
laws are a standard pose class in this record (Phase
208's κ-trimming analysis). The price, carried in the
restated wording: the coefficient must be named as
**fitted**, with its provenance — bare "CH-PHI-Auu
trim" must not be quoted in a way that implies the law
was derived from the channel's physics.

**(4) Registration integrity — "exactly four
adaptations" fails as a literal count, survives as
substance; nothing hidden.** Gate-26 diffed
`p2561_registration.md` against `p2431_registration.md`
in full (839 diff lines; audit §1). Findings: (a) the
four stated adaptations cover the substantive changes —
A2 verified a true non-adaptation (the ladder, the
Richardson formulae, CERT-1…4 and the 1×10⁻⁶ bar are
numerically and textually identical); A3's window
carries Phase 243's margin pattern exactly
(0.65625 − 0.05625 = 0.6, 0.6625 + 0.0875 = 0.75, as
0.55625 − 0.05625 = 0.5, 0.5625 + 0.0875 = 0.65); A4 is
clean (no t* disposition machinery anywhere; the only
wound-machinery use is CTRL-3's G5 grid admission,
director-only reads at t ∈ {0.25, 0.5} against Phase
210's stored rows — no wound bracket number re-read,
re-derived or re-priced). (b) **§5(c) is a fifth
adaptation**: Phase 243 priced the tail from the
predecessor's stored multi-grid rows ("no new march");
no such rows exist for this pose, so Phase 256 prices
it from its own fresh G3/G4 rows. §A as worded does not
list it (its only hook is A1's "(§§3–5, 7)" range),
while §5(c) itself flags the change "ADAPTED as
stated" — so the registration's "exactly these four …
and no others" is false as a literal count and true in
substance: the change is face-disclosed in the very
section that makes it, it is record-only (it fires no
verdict form and enters no CERT condition), the
aggregation and the bar are unchanged, and its only
cost is one notch of independence (the tail rows are
the phase's own, mitigated by the phase's checker and
by this gate's exact recomputation from the stored
rows, §1). (c) Three further disclosed-but-unlisted
elaborations of the Gate-23 §3 class (the expanded
21-file protected list; CTRL-3's wound-machinery
provenance sentence; CERT-4's "as Phase 252 read them"
parenthetical) — Gate-23 priced two such additions in
the 240→243 diff as nil, and the same price applies
here. (d) Cosmetics are pervasive and priced nil (one
citation slip: §9's "Phase 243 §8 lesson" should read
§9). **No hidden substantive difference exists.**

## §5. G26-B and G26-C; the amended claim set

**G26-B: SURVIVES INTACT.** Phase 243's wound bracket
certifies at Gate-23 (disposition T-A); Phase 256's
combined-class bracket certifies here (restated G26-A);
both were decided by the same registered certificate —
same 1×10⁻⁶ bar, same binding clauses NEC_φ = DEC_φ,
same window discipline, same CERT-1…4 conditions — and
the brackets are disjoint and ordered
(0.5625 < 0.65625; gate-recomputed limits at both, §1).
The comparison is certified-vs-certified in one frame,
not a cross-instrument one. The §2 asymmetry (the wound
certificate is a convergence certificate; this one is a
grid-stability certificate) is a difference in the
evidential character of the two certificates, priced on
G26-A's restated wording; the comparison claim itself —
which bracket lies later, and that both are verdicts
under the one instrument — is exact as stated, so no
restatement of G26-B is owed. Phase 243's and Gate-23's
verdicts stand for their own pose and scope exactly as
recorded; G26-B adds the lead change, it does not
rewrite them. The programme's longest-lived throat datum
at verdict grade is the combined-class datum.

**G26-C: SURVIVES INTACT** — the fences are claims about
scope, and each is verified: (i) the certificate covers
the window [0.6, 0.75] at the sampled and refined
instants named, under the stated pose — the tail reads
past the window are **not** certified, and the tail
pricing stands on the face recomputed exactly by this
gate (first exceedance at t = 0.775, stage max
1.6326915963205124×10⁻⁵ at t = 1.0 on DEC_θ, §1);
(ii) the pose is a jet-scope sector superposition
(posed jet entries, no coupled solve — exhibit ≠
construction), as registered; (iii) programme-level
sustainment wording remains gated by the p1592 deciding
scan regardless of this gate's outcome — the
certificate's design leaves that gate untouched, and
this gate grants no programme-level wording either.
The two record notes of §4 (the fifth adaptation; the
unpriced B-sensitivity) qualify the record around the
fences; neither falsifies a fence as stated, so no
restatement of G26-C is owed — both notes are carried
into the quotable set below so that no quotation of
G26-A can shed them.

**The amended sustainment claim set (the quotable
whole).** Gate-22's restated G22-1/G22-2/G22-3 and
Gate-23's appended G23-A (restated)/G23-B/G23-C stand as
recorded there. Gate-26 appends:

- **G26-A (restated, §3):** the combined-class pose
  (κ = 0.3 director + C2 rotating headline + CH-PHI-Auu
  trim law with fitted c_trim, as clamped at
  B := 2.5) meets every registered throat clause bar at
  the sampled instants of [0, 0.65625] on the standing
  grid and is limit-certified (grid-stability sense,
  §2) on the window [0.6, 0.75] in the terms stated,
  with first crossing at t ∈ (0.65625, 0.6625] on
  NEC_φ = DEC_φ.
- **G26-B:** the certified bracket lies entirely past
  the wound pose's Gate-23-certified (0.55625, 0.5625];
  the sustainment lead changes hands at verdict grade.
- **G26-C:** the fences — tail reads past the window
  not certified (exceedance from t = 0.775, priced from
  Phase 256's fresh G3/G4 rows); pose scope and jet
  scope as registered, the certified object being the
  trim law as clamped at B := 2.5 with its fitted
  coefficient, the bracket's sensitivity to the stop's
  value unpriced on the record; programme-level
  sustainment wording remains gated by p1592
  regardless.

**Publication consequence:** the Gate-26 claim set
(G26-A restated, G26-B, G26-C) **joins the v1.22.0
bundle's claim list** — it does not open a v1.24.0 set.
Reasons: (1) it is the same claim line v1.22.0 exists
to publish — the wound-throat sustainment line of
Gate-22/Gate-23 — and Gate-23 set the operative
precedent by appending its claim set to v1.22.0 rather
than opening a new version for a successor certificate
in the same line; (2) the v1.22.0 bundle is not yet
packaged (packaging is owed, not done), so appending
costs nothing and keeps a single coherent sustainment
release whose internal story — director bracket,
three-channel extension, combined-class lead change —
is exactly the sequence a reader needs; (3) v1.23.0 is
already spoken for by Gate-25's spinor-sourcing set, a
different line, and a v1.24.0 for Gate-26 alone would
fragment the sustainment record across two releases
for no gate-level reason. (Packaging is the parent's
act, not this gate's.)

## §6. Novelty position

Unchanged from Gate-22 §6, and it extends to the new
claims without re-search: every ingredient remains
published; the combined-class datum is the same pose
class and jet/channel scope as the Gate-22/23 set, with
a fitted open-loop trim law and a rotating headline
added — it inherits both Gate-22's "not found in our
search (limits: …)" position and its stated headwind
(Hochberg & Visser: NEC violation is generic for dynamic
throats in full spacetimes; these claims are not a
full-spacetime solution, and the scope fence is what
keeps the two from colliding). **No "first", "unique"
or "record" wording is granted or implied for
G26-A/G26-B/G26-C.**

## Files

- `gate26/work/g26_verify.py` + `g26_verify_results.json`
  — Gate-26's independent re-derivation: Richardson
  limits and CERT booleans for the combined-class
  bracket from the stored per-grid rows (both
  case-classification readings); CERT-4 non-clause bars
  at the bracket instants; CTRL-2 replay and tail
  pricing from the stored rows of Phases 252/256; the
  wound bracket's limits recomputed from Phase 243's
  stored rows; NEC_φ/DEC_φ pointwise identity; the
  trim-law and stop arithmetic of §4.
- `gate26/work/g26_scope_audit.md` — the full
  registration diff (Phase 256 vs Phase 243) with every
  difference classified; the B := 2.5 audit; the
  fitted-coefficient chain of custody; the A2 pricing;
  the A3/A4 checks; the G26-A wording audit with the
  per-clause span minima.
- No ledger append, no launches, no external contact.
  Nothing outside `gate26/` was edited.
