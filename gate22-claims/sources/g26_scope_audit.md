# GATE-26 — REGISTRATION-INTEGRITY AND SCOPE AUDIT
# Phase 256's certification registration vs Phase 243's;
# the B := 2.5 stop; the fitted trim coefficient; the A2
# grid anatomy; the G26-A wording

Audit worker, Gate-26, 2026-11-24. Read-only outside
`gate26/`. Method: full text diff of the two registrations
(`diff -u phase243/work/p2431_registration.md
phase256/work/p2561_registration.md`, 839 diff lines over
458 → 420 registration lines), plus the registrations,
memos and stored results named in the tasking. No march
was run; arithmetic below is selection/arithmetic on
stored floats and small hand arithmetic only.

Sources cited by short name: **R256** =
`phase256/work/p2561_registration.md`; **R243** =
`phase243/work/p2431_registration.md`; **R252** =
`phase252/work/p252_registration.md`; **M252-1 / M252-2** =
`phase252/results/p2521_memo.md` / `p2522_memo.md`;
**CK252** = `phase252/CHECKPOINT252.md`; **R248** =
`phase248/work/p2482_registration.md` (incl. Amendment
A-1); **M248-2** = `phase248/results/p2482_memo.md`;
**M256** = `phase256/results/p2561_memo.md`; **GATE23** =
`gate23/GATE23.md`.

---

## 1. FULL DIFF — EVERY SUBSTANTIVE DIFFERENCE, CLASSIFIED

R256's claim (R256 header and §A): it "carries the Phase
243 certificate … with the adaptations stated in §A on
the face — and no others", and §A: "The adaptations are
exactly these four" — A1 pose, A2 grids NOT adapted, A3
window, A4 no t* disposition.

### 1.1 Classification counts (grouped by locus)

| class | count of grouped loci | verdict |
|---|---|---|
| (a) inside A1–A4 as stated | 14 grouped loci (§1.2) | as claimed |
| (b) §5(c) tail-pricing source adaptation | **1** | a **fifth** adaptation in counting terms — disclosed on the face of §5(c) itself, not counted in §A (§1.3) |
| (c) cosmetic (title / phase numbers / paths / renumbering / restated constants) | pervasive, no locus affects a bar, window, clause or deciding number | as expected |
| (d) UNLISTED SUBSTANTIVE | **0 hidden**; 3 minor disclosed-but-unlisted elaborations (§1.4), none touching a bar, window, clause or deciding number — the Gate-23 analogue class | §A's "exactly four" is a counting defect, not a concealment |

### 1.2 The (a) loci — traceable to A1–A4

1. **Header / protected-file list.** The six Phase 243
   protected files are retained; fifteen are added
   (Phase 210/214 results, `phase243/work/p2431_run.py` +
   its results, Phase 246/248 drivers and results, R252,
   Phase 252 drivers and results, and R256 itself).
   Classified (a)-adjacent / protective: the additions are
   exactly the source files of the A1 pose, its controls
   and the A4 grid-admission machinery. They widen only
   the md5 fence; they change no read. (Also listed in
   §1.4 as not itself enumerated in §A.)
2. **§0 question** — entirely new: Phase 252's bracket,
   margins +0.052799 / −0.073695, the successor quotation
   from CK252. Consequence of A1 + A3.
3. **§1 scope** — carried in substance, compressed:
   R243 §1.1–§1.5's five-part argument is replaced by a
   summary citing "Phase 243 §1.1–1.3 (Phase 210 /
   Gate-22…)" and restating the bar, the per-instant
   application, CERT-2/3's limit-sign requirement and the
   cherry-picking guard in prose. No scope widening: the
   1×10⁻⁶ threshold, per-carrying-read aggregation and
   tail exclusion are identical. Abridgement, not
   adaptation — but note the citation covers §1.1–1.3
   only; §1.4 (bar-not-moved) and §1.5 (cherry-picking
   guard) are restated in R256 §1's own words rather than
   carried, with the same content.
4. **§2** — R243's whole t* disposition (T-A/T-B/T-C,
   re-reading Phase 214's t* under the same certificate)
   is replaced by a no-re-open disposition. **A4, verbatim
   as registered.**
5. **§3 windows** — R243's two windows (new bracket +
   t*) become one window; the window itself is **A3**
   (see §5 of this memo for the margin arithmetic).
6. **§3 pose line** — wound three-channel pose (flat
   a = −0.5) → the re-posed combined-class arm (trim law,
   B := 2.5, stored c_trim). **A1.**
7. **§3 CERT-4 parenthetical** — R243's non-clause bars
   "(momentum ≤ 1×10⁻¹⁰, flare > 0, domain regular)"
   become "(momentum ≤ 1×10⁻¹⁰, flare > 0, domain regular
   — the base-pose bars of record, as Phase 252 read
   them)". Bars unchanged; source attribution added.
   A1-derived elaboration (also §1.4).
8. **§4 CTRL-1** — target rows change completely: R243's
   Phase 234 three-channel + Phase 214 director stored
   rows at G3/G4 → R256's Phase 252 stored `reposed_sampled`
   (41 sampled instants) and `reposed_bracket` end margins,
   reproduced by fresh marches at the *standing*
   discretisation (N_θ = 2881; main h_t = 0.0025, aux
   h_t = 0.00125, T_END = 1.0), with the bracket ends read
   exactly as `p2522_run.py`'s `read_at` (lo from aux index
   525, hi from main index 265), plus an ulp-class
   profile-entry reporting footnote (≤ ~5×10⁻¹⁶, Phase 248
   CTRL-2 class — reported, not a failure). Diff-0.0
   standard and STOP consequence unchanged. **A1** (the
   control must pin the new pose's claim rows).
9. **§4 CTRL-2** — R243's Phase 234 stage-gate values
   (Stage A/B maxima) → R256's replay of Phase 252's
   bracket from its stored rows: sampled bracket
   (0.65, 0.675], carriers exactly {NEC_φ, DEC_φ}, refined
   bracket and end margins, the bracket decomposition
   identity, and the stop instant √(2/5.253378) = 0.617015
   to 1×10⁻⁶. **A1.**
10. **§5(a)/(b)** — window reads and certificate
    evaluation for one pose instead of two (three-channel
    primary + director-only). **A1 + A4.**
11. **§5 t* search deleted** — R243 §5(c) (the
    restated-bracket ladder search, only if T-A failed)
    has no counterpart. **A4.**
12. **§6 decision order** — steps (i)–(iii) identical in
    substance; step (iv) loses R243's entire t*
    evaluation / T-B common-frame refutation branch and
    states the comparison "per §2
    (certified-vs-certified)". **A4.**
13. **§7 verdict forms** — form 1: new bracket, new pose
    fence (ii) ("…CH-PHI-Auu under P-PHI-TRIM-248 at the
    B := 2.5 operational stop, as posed"), comparison
    stated certified-vs-certified; form 2: restatement
    language changes from "the crossing remains a G4
    read" / "Phase 234's GATE-BLOCKED disposition stands"
    to "the crossing remains a standing-grid read" /
    "Phase 252's disposition stands unamended: the
    combined-class bracket remains a read and the wound
    pose keeps the certified lead"; form 3: kernel-spec
    path only (cosmetic). All **A1/A3/A4** consequences;
    no form's firing condition changes.
14. **§8 fences** — R243's Phase 234/240 successor
    sentences are replaced by: the trim-law open-loop
    fence ("≠ the closed-loop stabilisability proof
    (Phase 208) and ≠ Phase 217 V2"), the B := 2.5 fence
    ("an operational limit of the pose as certified, not
    a priced boundary (Phase 252 Item 1: no finite
    boundary in [0, −2.5]; the audited range's end is not
    a boundary)"), and the sentence that Phase 252's
    bracket stands as a read unless form 1 fires. These
    are the A1 pose's own fences, stated on the face;
    they narrow, they do not widen.

**A2 verified as a true non-adaptation.** The ladder is
numerically identical in R243 §3/§R(b) and R256 §A2/§3:
G3 (N_θ = 5761, h_t = 0.00125), G4 (11521, 0.000625),
G5 (23041, 0.0003125), every march T_END = 1.0; the
Richardson formulae, the admissible-p range 0.5 ≤ p ≤ 6,
the limit-certified test (r, |d34|, |d45| all
≤ 1×10⁻⁶) and CERT-1…4 are textually the same in
substance. R256 §A2 additionally *argues* the ladder's
applicability (pose-independent march state; read-level
sector) and registers the counterpoint (the ladder never
uses the 2881 standing grid) — an argument added on the
face, not a change to the instrument. What that argument
does and does not buy is priced in §4 of this memo.

**Checker (§9).** R256 §9's recomputation targets change
with the pose (spot recomputation for one pose, not both;
stored-row controls vs Phases 210/252, not 210/214/234;
no stage gates; tail pricing "recomputed from the stored
G3/G4 rows in the results file" — the §5(c) source change
of §1.3, downstream). One citation slip, cosmetic:
R256 §9 calls the decision-order-consistent assertion
form "the Phase 243 §8 lesson" — in R243 that text is in
§9 (Checker); §8 is Fences. No effect on any assertion.

### 1.3 The (b) locus — §5(c) is a fifth adaptation

R243 §5(d): tail pricing "(record only, **from Phase
234's stored rows; no new march**)". R256 §5(c), headed
on its own face "**Tail pricing (record only; ADAPTED as
stated)**": "Phase 243 priced the tail from the
predecessor's stored multi-grid rows; no stored
multi-grid rows exist for this pose, so the tail is
priced from THIS phase's fresh G3 and G4 rows… (Same
aggregation, same bar — only the rows' source differs,
as stated.)"

Judgement:

- **It is not inside A1–A4 as §A words them.** A1's
  stated content is the pose, its read machinery and the
  binding clauses; A2 expressly claims the grids are
  *not* adapted; A3 is the window; A4 is the t*
  disposition. None of the four mentions the tail-pricing
  source. The only textual hook is A1's section range
  "(§§3–5, 7)", which sweeps §5 in by reference — but §A
  then enumerates what A1 *is*, and tail pricing is not
  in the enumeration, while §5(c) flags itself with the
  same word §A uses for its own list: "ADAPTED".
- **Therefore §A's "exactly these four … and no others"
  does not survive §5(c) as a literal count.** The true
  count is five adaptations, the fifth being §5(c).
- **Price: counting defect, not a certificate defect,
  and not a concealment.** §5(c) is disclosed on the face
  of the very section it changes, with its reason (no
  stored multi-grid rows exist for this pose — true:
  Phase 252 ran only the standing grid, R252 §3 /
  M252-2). Tail pricing is record-only under both
  registrations: it fires no verdict form, enters no
  CERT condition, and is reported on the face of either
  verdict as a limitation (R256 §1, §7 form 1 fence (i)).
  The aggregation (per-instant max G3–G4 disagreement
  over all seven clauses on the post-window stage), the
  reported quantities and the 1×10⁻⁶ bar are unchanged.
  What changes is provenance of the priced numbers:
  Phase 243's tail price was an *independent stored
  artefact's* disagreement; Phase 256's is the certifying
  run's *own* G3/G4 rows — one independence notch lower,
  mitigated on the record by the checker recomputing the
  tail pricing from the stored G3/G4 rows in the results
  file (R256 §9; M256 §8). The tail numbers themselves
  (M256 §5: first exceedance t = 0.775, stage max
  1.6326915963205124×10⁻⁵ at t = 1.0, carrier DEC_θ) are
  therefore priced from fresh rows, and any quotable
  tail statement must say so.

### 1.4 The Gate-23 §3 analogue — unlisted-but-disclosed additions

Gate-23 §3 diffed Phase 240 vs 243 the same way and found
the scope argument character-identical, all differences
traced to §R's three declared repairs, plus **two
additions not listed in §R, both disclosed in Phase 243's
own memo/checkpoint, neither touching a bar, a window or
a deciding number** (the §8 successor-disclaimer sentences
and the §9 checker-assertion sentences). Priced there as
survivable; the gate's verdicts rested on its own
recomputation.

The analogues here, same class and same price:

1. The §5(c) adaptation (§1.3) — disclosed on the face of
   §5(c), stronger than Gate-23's pair in one respect (it
   *is* labelled "ADAPTED" where it sits) and weaker in
   another (Gate-23's additions changed no registered
   *method*; §5(c) changes a registered method's data
   source, albeit a record-only one).
2. The expanded protected-file list (§1.2 item 1) — on
   the face of the header, protective only.
3. The CTRL-3 execution sentence (R256 §4: "Executed
   with the wound-pose read machinery copied from
   `phase243/work/p2431_run.py`, unmodified") — R243 §4's
   CTRL-3 does not state its machinery source; R256 adds
   the provenance. Tightening, not widening (see §5.2).
4. The CERT-4 parenthetical (§1.2 item 7) — attribution,
   bars unchanged.

**No (d) hidden substantive difference was found.** Every
remaining diff line is title/phase-number/path cosmetics,
the §5(d)/(e) → §5(c)/(d) renumbering forced by A4's
deletion, or restatements of constants at higher
precision (e.g. the G5 state size "≈ 5.9×10⁸ B" in
R243 §R(b) vs the exact 590,033,928 B in R256 §5(d) —
the same number). The 1×10⁻⁶ threshold is, as both
registrations claim, nowhere changed; the Richardson
construction and CERT-1…4 are unchanged in substance.

**Bottom line, §1:** R256's registration integrity is
Gate-23-class, not perfect-count class. "Exactly four
adaptations and no others" is false as a count (five,
with §5(c)) and imprecise as a census (three further
disclosed elaborations), but every deviation is disclosed
on the face of the registration itself, none moves a bar,
a window, a clause set or a CERT condition, and the one
method change (§5(c)) is record-only. The quotable
registration-integrity sentence is: *Phase 243's
certificate carried with four registered adaptations
(A1–A4) plus one face-disclosed record-only adaptation
(§5(c), tail-pricing source: fresh G3/G4 rows, no stored
multi-grid rows existing for this pose).*

---

## 2. B := 2.5 AUDIT

The pose (R256 §A1): a(t) = −0.5 − c_trim·t², c_trim =
+5.253378 stored, "clamped at the operational stop
**B := 2.5** (the stop binds from t_stop = √(2/c_trim)
= 0.617015)".

### 2.1 (i) Is 2.5 derived from anything?

**No. 2.5 is the sweep's endpoint, adopted as a round
number at the edge of the audited range.** Chain:

- R252 §2.2 registers the boundary sweep "over
  a ∈ [0, −2.5]" — the range is fixed in the registration
  before the sweep; no locus in R252, M252-1 or CK252
  derives 2.5 from a condition, a scale or a datum
  property. M252-1 §4 prices the datum's own scales
  (base J[Auu] scale 0.2; CH-COMB offset class 0.10) and
  2.5 appears there only as a sweep row (ratios 12.5 /
  25.0 — themselves round multiples of those scales,
  with no event at 2.5 either).
- M252-1 §3/§5: no H-condition fails anywhere in the
  range; "the sweep end |a| = 2.5 is the audit's limit,
  not a boundary"; verdict form 3, "NO FINITE BOUNDARY
  IN THE AUDITED RANGE".
- R252 §3 then fixes the consequence in advance: form 3
  (or form 1 with no finite boundary) → "**B := 2.5
  operational stop** (the law runs unclamped through the
  deciding window; the march halts and reports if |a|
  would exceed 2.5…)". The parenthetical's justification
  is about the *comparison* window ("at the wound
  bracket's far end the unclamped law reads −2.162, so
  the stop does not bind the comparison") — a reason the
  stop does not corrupt the wound comparison, not a
  derivation of the level 2.5.

So 2.5's entire warrant is: *the largest amplitude the
audit swept*. It is an audited-range endpoint chosen as a
round number, exactly as the tasking hypothesised. Both
records say this on their faces (M252-1 §5; R256 §8:
"the audited range's end is not a boundary") — there is
no derivation claim to impeach.

### 2.2 (ii) The stop binds INSIDE the certified window, BEFORE the bracket — is it disclosed?

Arithmetic: t_stop = √(2/5.253378) = 0.617015 (R256 §A1;
CTRL-2(d) re-derives it, M256 §2: 0.61701493). The
certified window is [0.6, 0.75] (R256 §A3/§3) and the
bracket is (0.65625, 0.6625]. Hence:

- the stop binds at the window's *second* sampled
  instant's neighbourhood: at t = 0.6 the law is still
  unclamped (a = −0.5 − 5.253378×0.36 = −2.391216); from
  t = 0.625 onward every window read is at a ≡ −2.5;
- **the entire bracket, and 6 of the 7 sampled window
  instants (0.625…0.75), are read on the clamped pose** —
  a flat a = −2.5 channel, not on the t² law.

Disclosure loci, quoted:

- CK252: "the 2.5 stop binds only at t = 0.617015, **past
  the comparison point but before the crossing**" — the
  checkpoint states the ordering against the *comparison*
  (0.5625) and the *crossing* (the bracket), which is
  exactly the locus that matters for Phase 256.
- M252-2 §3: "At both ends the law is already at the stop
  (a = −2.5; the stop binds from t = 0.617015, *after*
  the wound comparison point 0.5625, where a =
  −2.162202)"; §3 decomposition: "the crossing is
  carried by the headline μ-drift against a **saturated
  lift**".
- M252-2 header: "the stop binds at t_stop =
  √(2/c_trim) = 0.617015", with the registration's
  "does not bind the comparison" priced immediately
  beside it.
- R256 §A1 states t_stop = 0.617015 in the same sentence
  as the window-defining A3 bracket (0.65625, 0.6625] in
  §0/§A3 — the ordering 0.617015 < 0.65625 is on the face
  of the registration for any reader who compares the
  two numbers, and M256 §§1, 9(ii) repeat both numbers.

**Verdict on disclosure: disclosed, completely, at every
level of the record** — registration, both Phase 252
memos, the Phase 252 checkpoint and the Phase 256 memo
all carry t_stop and the bracket side by side, and
M252-2 §3 names the bracket's anatomy ("saturated
lift") in words. What no locus does is draw the
*sentence* "therefore the certified bracket is a bracket
of the clamped pose, not of the unclamped law" — that
sentence is owed in the claim wording (§2.4), not missing
from the evidence.

One registration sentence does **not** survive into
Phase 256's scope and must not be quoted there: R252
§3's "the law runs unclamped through the deciding
window" was true of *Phase 252's* deciding window (the
wound comparison, ending 0.5625 < 0.617015). For Phase
256's window the law runs unclamped through exactly one
sampled instant (0.6). R256 does not repeat the sentence
— correctly.

### 2.3 (iii) The a_equiv = −2.743808 point, and B-sensitivity

M252-2 §3 (descriptive, Phase 248 B5 method): the flat
amplitude whose constant lift would repay the headline
deficit at the bracket's hi end (D = 2.589541 over
s̄ = 1.154083) is a_equiv = −2.743808 — "beyond even the
2.5 stop. The law nevertheless crosses at 0.6625 because
its lift was banked earlier along the trajectory."

Implication, priced: at the bracket the pose is *not*
self-supporting at its own terminal amplitude. A flat
channel at the stop value −2.5, run from t = 0, is a
different (weaker-at-the-hi-end, in this descriptive
pricing) pose than the law-that-arrived-at−2.5; the
bracket depends on the whole clamped trajectory —
the t² growth phase (0 → 0.617015) banking lift, then
the flat phase eroding slowly (lift +2.524597 →
+2.515846 across the bracket, M252-2 §3) while the
headline drift falls (−2.471798 → −2.589541). The
certificate therefore certifies a *trajectory*, and the
stop's value is one of the trajectory's defining
parameters — on the same footing as c_trim, not a
detail downstream of the result.

**Would the bracket move if B were 2.0 or 3.0? No
sensitivity of the bracket to B is on record anywhere.**
Phase 252 ran exactly one B (2.5); Phase 256 certifies
exactly that pose; no B ∈ {2.0, 3.0} march, spot read or
pricing exists in either phase's results. What the
record does establish about clamp-sensitivity in
general is strong: the *same law* clamped at 0.8
brackets at (0.525, 0.53125] (Phase 248 / CTRL-B) and
clamped at 2.5 at (0.65625, 0.6625] — a 0.13125 shift in
the bracket for a change of clamp, i.e. this pose's
bracket is clamp-sensitive as a class. Direction for the
unrun cases (reasoning from the stored decomposition,
**not a read, magnitude unpriced**): B = 3.0 binds at
√(2.5/5.253378) = 0.6899 — *after* the bracket — so the
bracket instants would be read on the unclamped law
(a(0.65625) ≈ −2.762, a(0.6625) ≈ −2.806), a strictly
larger-lift pose at both ends, and the crossing would
move later or vanish from the bracket; B = 2.0 binds at
√(1.5/5.253378) = 0.5344, the lift saturates lower and
earlier, and the crossing would move earlier. Neither
direction is a number; any claim of B-robustness would
need a run that does not exist.

### 2.4 (iv) Verdict — operational stop or smuggled assumption?

**Operational stop — a pose parameter — with one wording
debt. Not a smuggled assumption.** Reasoning:

- A smuggled assumption is a value the claim *needs* that
  nothing prices and the record presents as derived or
  natural. B fails every element of that test: it is
  named "operational stop" in R252 §3, R256 §A1, §7 form
  1 fence (ii) and §8; §8 states outright it is "not a
  priced boundary"; M252-1 §5 states the audited range's
  end "is the audit's limit, not a boundary"; and §2.1
  above confirms no derivation is anywhere claimed.
- The distinction from the wound pose's flat a = −0.5 is
  real and must be priced, as the tasking directs. The
  wound pose's −0.5 is a *posed constant*: the channel is
  that constant at every instant, so the certified object
  is exhausted by naming the constant. Here the certified
  object is a *law plus a clamp*: a(t) = −0.5 −
  5.253378·t² for t < 0.617015 and a(t) ≡ −2.5 thereafter,
  and — decisively — **the bracket itself, both window
  margins and the CERT-2/CERT-3 reads at every instant
  ≥ 0.625 are reads of the flat segment**. The honest
  name of the certified object is therefore **"the trim
  law as clamped at B := 2.5"**, never "the trim law"
  simpliciter, and never "the trim law at the audited
  amplitude" without the stop's binding instant beside
  it. R256 §7 form 1 fence (ii) in fact names it
  correctly ("under P-PHI-TRIM-248 at the B := 2.5
  operational stop, as posed"); the debt is only that
  any shorter quotable form (a claim line, a ledger line)
  tends to drop the clamp, and with it the fact that the
  bracket is a flat-channel bracket.
- **What was and was not audited at the stop value —
  stated exactly.**
  *Audited at a = −2.5:* (1) Phase 252 Item 1's boundary
  sweep of the **flat member** at the single amplitude
  a = −2.5 (one point of the 51-point grid over
  [0, −2.5]) under H1 (delivery exactness vs the linear
  prediction), H2 (PR-φ liveness and Wuu-solve), H3
  (non-clause bars), H4 (t = 0 seven-clause legality) —
  at **t ∈ {0, 0.25, 0.475} only** (R252 §2.2; M252-1
  §3: all pass, e.g. worst t = 0 clause minimum
  +3.718750 at −2.5). (2) Phase 252 Item 2's pose-refusal
  for the **flat member at a = −2.5** at
  t ∈ {0, 0.25, 0.475, 0.5625} (M252-2 §2: PR-φ offset /
  momentum / liveness and non-clause bars pass; liveness
  6.25) — pose-level checks, not seven-clause minima.
  (3) The law-adapted pose-refusal at all 41 sampled
  instants of the actual clamped trajectory (M252-2 §2),
  and the march's own seven-clause sampled reads along
  that trajectory to t = 1.0 — the claim's reads
  themselves.
  *Not audited at the stop value:* H1–H4 for the flat
  member at any t > 0.475 (Item 1's sweep stops at
  0.475); seven-clause legality of the flat −2.5 member
  at the bracket instants as an independent audit (the
  bracket reads are the clamped *law's* reads, in which
  the headline/lift history differs from a flat-from-0
  member — cf. a_equiv, §2.3); any amplitude beyond
  2.5 (M252-1 §6: "amplitudes beyond |a| = 2.5 are
  unaudited"); and any B ≠ 2.5 sensitivity (§2.3).
  The gap is narrow but real: the conditions that
  *license posing* a = −2.5 were verified on the flat
  member only up to t = 0.475 (H-conditions) and
  t = 0.5625 (pose-refusal), while the certified bracket
  sits at 0.65625–0.6625. What covers the bracket
  instants is not the Item 1 audit but Phase 256's own
  window reads (all seven clauses at G3/G4/G5, CERT-4's
  non-binding positivity and non-clause bars at G5) —
  i.e. the certificate itself, which is the correct
  instrument, provided the claim does not cite Item 1's
  sweep as covering ground it did not sweep.

---

## 3. TRIM-LAW FITTED-COUNTER-TERM AUDIT

The law (R256 §A1): a(t) = −0.5 − c_trim·t², **c_trim =
−q₂/s̄ = +5.253378**, where q₂ = −6.062835 is the c₂
coefficient of the FULL quadratic least-squares fit to
the composed arm's NEC_φ,min(t) over [0, 0.475] and
s̄ = 1.154083 is the mean of Phase 246's three stored
Auu sensitivities at the NEC_φ argmin (1.2070621979720642,
1.1461834865666987, 1.1090035914040897; mean
1.1540830919812842) (R248 B1; M248-2 §§2, 4).

### 3.1 (i) Chain of custody — where the coefficient was last exposed to the data it counters

- **Phase 248, formula before data.** R248 is "Written
  BEFORE any deciding computation (no fit, no march of
  this item has been run at registration time)"; B0/B1
  fix the prescription and the formula c_trim = −q₂/s̄,
  the fit form (FULL), the window ([0, 0.475]) and the
  sensitivity source in advance, and B1 bars substitution
  ("If q₂ ≥ 0 … NO other law is chosen"). The *formula*
  is a priori; the *value* is computed from Part A's fits
  on stored Phase 248 Item 1 rows, in the registered
  decision order ("Part A fits → … → coefficient computed
  from the FIXED formula → trimmed march"), **before
  Phase 248's own Part B march ran**. Verified from
  R248's header, B1 and Decision order, and M248-2 §2/§4.
- **Phase 252, stored, not re-fit.** R252 §3: "trim law
  P-PHI-TRIM-248 with the **STORED c_trim = +5.253378
  (q₂ = −6.062835, s̄ = 1.154083 — not re-fit; CTRL-B
  pins them)**". M252-2 header repeats "STORED c_trim …
  — not re-fit", and CTRL-B re-derives the constant from
  the stored q₂/s̄ as a control (M252-1 §1, M252-2 §1).
- **Phase 256, copied.** R256 §A1: "the STORED c_trim =
  +5.253378" (M256 §1 gives the full stored float
  5.253378225339471 from `phase248/results/p2482_results.json`);
  CTRL-2(d) pins the derived stop instant. No fit of any
  kind occurs in Phase 256.

**Answer: the coefficient was last exposed to the data
it counters in Phase 248 Part A** — fitted to the
composed arm's own NEC_φ,min trajectory over its holding
interval [0, 0.475]. Phases 252 and 256 expose it to no
new data; they inherit a frozen constant. Note the exact
shape of the exposure: the fit window ends at 0.475, the
Phase 248 trimmed bracket it produced sat at
(0.525, 0.53125], and the Phase 252/256 bracket sits at
(0.65625, 0.6625] — the certified crossing is an
*extrapolation* of the fitted counter-term well past its
fit window, not an interpolation within it. That is on
the record (the windows are stated in R248 A2 and
M248-2 §2) and is priced in §3.3.

### 3.2 (ii) Amendment A-1 — does it touch c_trim's derivation?

**No.** Verified from R248's Amendment A-1 text and
M248-2 §2:

- A-1 replaces exactly one thing: the A2 forced-form
  classification rule's second sub-criterion
  (|c₁|·t_max ≤ 3 × RMS(FULL) → |c₁|·t_max ≤ 0.25 ×
  |c₂|·t_max²), the test of whether the *headline* fit
  "supports the FORCED-t² form". It is recorded "after
  the Part A fits were printed but BEFORE any Part B
  deciding computation", and closes: "No other
  registered form, window, formula, cap, control, or
  verdict form changes."
- q₂ is the **FULL** fit's c₂ (R248 B1: "q₂ is the
  COMPOSED arm's fitted t² coefficient (FULL form,
  window [0, 0.475], Part A2)"). The FULL fit's
  coefficients do not depend on the forced-form
  classification rule at all — the rule consumes the
  fits; it does not produce them. M248-2 §2 prints the
  full fit (c₂ = q₂ = −6.062835) independently of the
  A-1 discussion, and §4 computes c_trim from it.
- What A-1 *does* touch is the verdict narrative: under
  the original sub-criterion the headline forced form
  fails on the c₁ clause alone (0.1052 vs bound 0.0171,
  M248-2 §2), so the "SAME FORCED MODE" identification
  rests partly on the amended rule — a fact M248-2 §2
  states on its face, together with the grounds that do
  not rest on it (exact decomposition §1, bit-identity
  to P169-1 §3, forced root 0.391898 ∈ (0.375, 0.400]).
  **c_trim's value would be bit-identical had A-1 never
  been written.** The trim *coefficient* is A-1-clean;
  the trim's *mode story* carries the A-1 disclosure,
  which is already on the face of M248-2.

### 3.3 (iii) Fitted pose — legitimate pose or curve-fitting? Bottom-line judgement

**Legitimate pose; the certificate is unaffected; one
wording fence is owed.** The price, itemised:

*For legitimacy.* (1) The certificate certifies the
bracket **of the pose as posed**. A pose parameter does
not become suspect because it was chosen with knowledge
of the system: it must be fixed in advance of the
certified march and not adjusted against it. c_trim
satisfies the strongest form of that test available in
this record — its *formula* was registered before any
fit existed (R248 header/B1), its value was frozen
before Phase 248's own first trimmed march, and the two
later phases that used it were barred from re-fitting
and pinned it by control (R252 §3 CTRL-B; R256 CTRL-2).
No feedback from any bracket read — Phase 248's, 252's
or 256's — ever touched the coefficient. (2) The fitted
form is not an arbitrary basis chosen to flatter the
data: the t² shape is the drift mode's own shape. The
decomposition composed = headline + lift is **exact**
(max deviation 0.0 over all 41 instants, M248-2 §1);
the headline arm is bit-identical to the P169-1 datum
(M248-2 §3); and the wound line's characterisation
(Phase 208, cited in R248 §0 inputs) is that the failure
is a *forced* mode, μ(·,t) ≈ (t²/2)·ũ(θ), spectrally
neutral — the counter-term cancels the fitted t²
coefficient of a drift whose t² character was
established independently of the fit. (3) Fitted /
feedback control poses are standard in this record and
were never barred as a class: Phase 208's κ-trimming
loop was "stabilisable on paper", Phase 217's V2
closed-loop law was run and failed on its merits; what
Phase 217 barred (R248 B0) is closed-loop laws and
hand-tuning *for this prescription* — and P-PHI-TRIM-248
is open-loop and registered, the exact compliant class.
Phase 243's wound pose, by contrast, used flat
a = −0.5, unfitted — a difference of pose style, not of
evidentiary standard: Gate-23 imposed no
"coefficients must be unfitted" condition on it, because
none exists in the certificate.

*The price that remains.* (1) **Extrapolation:** the
coefficient is fitted on [0, 0.475] and the certificate
is issued at 0.65625–0.6625, where moreover the law has
saturated (§2.2) — so at the bracket the "counter-term"
is no longer countering anything t²-shaped; it is a flat
channel whose level was set by a t² law whose level was
set by a fit on an earlier window. Each step is
registered and disclosed; the chain is three steps long
and the claim must not shorten it. (2) **Fit slack:**
the FULL fit's RMS on [0, 0.475] is 0.017171 with
c₁ = +0.651959 unmodelled by the law (M248-2 §2) — the
law cancels the fitted t² coefficient only, not the
trajectory; the residual drift is precisely what carries
the eventual crossing (M252-2 §3). Nothing here is
hidden; it is why the bracket is finite. (3) **No
generality:** c_trim is a property of *this* datum's
measured drift and *these* stored sensitivities. It
transfers to no other datum, and a claim that read it as
a channel constant would be false.

**Wording fence owed (the judgement's operative part):**
any quotable form of the claim must describe the law as
**fitted**, in words on the face — e.g. "CH-PHI-Auu under
P-PHI-TRIM-248, a(t) = −0.5 − c_trim·t² with c_trim =
+5.253378 **fitted in Phase 248 (registered formula
c_trim = −q₂/s̄) to the composed arm's measured
NEC_φ t² drift coefficient over [0, 0.475] and Phase
246's stored mean Auu sensitivity, frozen thereafter and
not re-fit**". The bare label "CH-PHI-Auu trim" — and
a fortiori any phrasing suggesting the law was derived
from the Auu channel's physics, from the forced-mode
theory, or from first principles — overstates the
provenance: the *form* (t²) is the mode's; the
*coefficient* is a least-squares fit to the drift it
counters. With that fence, the fitted coefficient is a
pose parameter like any other, and the certificate
stands at full weight. Without it, the claim borrows
authority the record does not contain.

---

## 4. A2 GRID ANATOMY — WHAT THE RICHARDSON CERTIFICATE ACTUALLY TESTS HERE

M256 §4, on its own face: the combined-class binding
minima are grid-stable to ~10⁻¹³ (worst in-window
|d34| = 1.750×10⁻¹³ at t = 0.725; worst |d45| =
1.865×10⁻¹⁴; worst residual r = 2.220×10⁻¹⁵), against
Phase 243's wound-pose table at p ≈ 2.0000 with
disagreements ~10⁻⁷ — "the combined-class clause minima
are a read-level sector off the marched state,
interpolated onto the fixed audit grid, and at these
instants they are grid-stable to ~10⁻¹³, so the
Richardson limit sits on top of the finest-grid value."
This gate prices that anatomy; it does not discover it.

**What the three rungs vary, and what they cannot vary.**
Per R256 §A2/§3, the ladder varies N_θ (5761 / 11521 /
23041) and h_t (0.00125 / 0.000625 / 0.0003125) of the
*march* (MU, U, MTT — pose-independent). The combined-class
clause minima are then computed from jets interpolated
onto the **fixed audit grid TH** — the same audit grid at
every rung. The binding minimum sits at the fixed locus
θ* (index 90; M252-2 §3: no argmin migration at any
sampled instant). The three reads therefore differ only
through the marched state's own grid dependence, filtered
through an interpolation onto a common grid and a minimum
at a common locus. Their agreement at 10⁻¹³ — i.e. at
~10⁻¹³ *relative* to minima of magnitude 0.05…2.5, a few
hundred float64 ulps of the profile arithmetic — is the
signature of a read whose discretisation error is already
below the arithmetic noise floor at the *coarsest* rung,
not of an error being driven down rung by rung.

**Consequences for what CERT-1…3 certify here.**

1. **The Richardson extrapolation is inert.** With
   |d45| ≤ 1.865×10⁻¹⁴, L differs from v5 by
   r ≤ 2.220×10⁻¹⁵ at every window instant (M256 §4
   table). CERT-2's "bracket at the limit" and "bracket
   at the finest grid" are, for this pose, the same
   statement to fifteen digits; the limit adds no
   independent evidence beyond v5. In Phase 243 the
   limit was a genuinely different number from v5
   (L(0.55625) = +0.004468 vs the standing margins) and
   CERT-2's double requirement did real work.
2. **The order reads p ∈ [3.23, 4.61] carry no
   convergence information.** p = log2(d34/d45) is a
   ratio of two noise-floor differences; its landing in
   the admissible band [0.5, 6] is a property of how the
   rounding-level differences happen to scale, not a
   measured convergence order. Gate-23 §1 could quote
   Phase 243's "p ≈ 2.0000" as an exact, meaningful
   property of that window (p ∈ [1.99999, 2.00003] —
   genuine second-order discretisation error shrinking
   4× per rung). No analogous sentence is available
   here, and none must be written: a quotable "p ∈
   [3.23, 4.61]" without the noise-floor context would
   claim a *faster-converging* read, which is precisely
   backwards — there is no visible convergence because
   there is no visible error.
3. **What the certificate does test, at full weight:**
   (a) **the bracket is not an artefact of the claim's
   standing grid.** The ladder never uses N_θ = 2881
   (R256 §A2's counterpoint); three independent
   (N_θ, h_t) marches reproduce the bracket-end signs
   and, to 10⁻¹³, the margins (+0.052799 / −0.073695) —
   this kills the specific artefact class a certification
   registration exists to kill, and CTRL-1 (diff 0.0
   against Phase 252's stored rows) ties the ladder's
   answer to the claim's rows. (b) **CERT-3/CERT-4 at
   G5**: no earlier in-window crossing at v5, and
   non-binding clauses positive at G5 at every window
   instant ≤ t_hi — real, rung-dependent checks that do
   not reduce to the noise floor. (c) The **tail
   contrast** (M256 §5): the same machinery's G3–G4
   disagreement on DEC_θ past the window is 10⁻⁵-class,
   so the ladder *can* see grid disagreement where the
   read has any — the in-window 10⁻¹³ is a property of
   the binding read, not a blind instrument.
4. **What it does not test:** a truncation-error bound.
   In Phase 243, CERT-1's three quantities (|d34|,
   |d45|, r) at 10⁻⁷-class priced the distance from the
   finite-grid reads to the continuum limit — Gate-23
   §1's margin table (worst |d34| 2.87× under the bar,
   |d45| 11.49×, r 34.47×) is a table of *real margins
   against real error*. Here the same table reads:
   |d34| 5.7×10⁶× under the bar, |d45| 5.4×10⁷×, r
   4.5×10⁸× — margins against *rounding noise*. Quoting
   M256's "clears the bar by nine orders of magnitude"
   as if it were nine orders of convergence assurance
   would repeat, inverted, the defect Gate-23 corrected
   in Phase 243's ">10×" phrase.

**Priced verdict:** for this pose the Phase 243
certificate functions as a **grid-stability and
cross-grid-reproduction certificate at the 1×10⁻⁶ bar**,
not as a convergence certificate in Phase 243's sense.
That is a weaker statement than Phase 243's certificate
— weaker in exactly one dimension (no measured approach
to a limit; the limit is the finest read restated) and
equal in the others (independent grids, one frame,
registered window, unchanged bar, CERT-3/4 content).
It is not a failed or relaxed certificate: the bar is
met as registered, and the reason it is met so far
beyond the bar is disclosed on M256 §4's face.

**Wording the claim needs:** the certificate sentence
must carry the anatomy — e.g. "…limit-certified under
per-instant Richardson on G3/G4/G5, **the three grids'
binding-clause reads agreeing to ≤ 1.750×10⁻¹³ (worst
|d34|) with Richardson residuals ≤ 2.220×10⁻¹⁵, the
limit coinciding with the finest-grid read at that
precision — a grid-stability certificate for a
read-level sector, not a measured convergence rate**".
The phrases "Richardson limits" alone, or any p-value
quotation, do not carry it.

---

## 5. A3 / A4 CHECKS

### 5.1 A3 — window arithmetic: the margin pattern carries exactly

Phase 243 (R243 §3): bracket (0.55625, 0.5625], window
(0.5, 0.65]. Margins: 0.55625 − 0.05625 = 0.5 ✓;
0.5625 + 0.0875 = 0.65 ✓.

Phase 256 (R256 §A3/§3): bracket (0.65625, 0.6625],
window sampled {0.6, …, 0.75} ∪ refined {0.65625,
0.6625, 0.66875}. Margins: **0.65625 − 0.05625 = 0.6 ✓;
0.6625 + 0.0875 = 0.75 ✓** — the identical pattern
(0.05625 below t_lo, 0.0875 above t_hi), as §A3 claims.
Further checks: every window instant is a multiple of
0.00625 and hence an index read on all three rungs
(h_t divides 0.00625 in 5 / 10 / 20 steps — R256 §A3,
arithmetic verified); the window contains the bracket
plus three sampled instants below t_lo (0.6, 0.625,
0.65) at which CERT-3 has content, and the refined
0.66875 above t_hi. The window is claim-fixed plus the
registered pattern and "NOT trimmable" in both
registrations. **A3 verified without remainder.**

### 5.2 A4 — no t* disposition; no wound re-read beyond CTRL-3

- R256 contains no T-A/T-B/T-C machinery, no wound-pose
  window, and no t* search (§1.2 items 4, 11, 12). §2
  fixes the comparison as certified-vs-certified only
  under form 1, and under forms 2–3 "no lead change is
  stated at any grade".
- The only wound-machinery use in R256 is **CTRL-3**:
  fresh G5 director-only reads at t ∈ {0.25, 0.5} against
  Phase 210's *stored* G4 director rows, bar 1×10⁻⁶,
  "solely to admit the G5 grid; it re-opens nothing"
  (R256 §2, §4). It reads no wound bracket instant,
  derives no wound bracket number, and its comparison
  values are Phase 210's stored rows, not Phase 243's
  certified bracket. M256 §2 records the outcome
  (1.4235054024425153×10⁻⁸ / 5.694021876223587×10⁻⁸ —
  numerically identical to Phase 243's CTRL-3, as M256
  notes they must be). CTRL-2 touches only Phase 252
  stored rows. **No wound number is re-read, re-derived
  or re-priced anywhere in R256 beyond CTRL-3's
  grid-admission use, exactly as A4 states.** The one
  wound *fact* the phase consumes — the bracket
  (0.55625, 0.5625] and disposition T-A — is consumed as
  a Gate-23 verdict by citation (R256 §2), which is the
  use A4 registers.
- **A4 verified without remainder.**

---

## 6. G26-A WORDING AUDIT

The claim as put to this gate: the datum "**holds all
seven throat clauses on [0, 0.65625] at the sampled
instants … CERTIFIED at the Phase 243 standard
(Richardson limits …)**".

### 6.1 What evidence supports which part

**Part 1 — "all seven clauses on [0, 0.65625] at the
sampled instants."** Evidence class: **standing-grid
reads, not Richardson limits.** Phase 252's re-posed
march on the standing discretisation (N_θ = 2881, main
h_t = 0.0025) read all seven clauses at 41 sampled
instants over [0, 1.0] (M252-2 §2/§3; `reposed_sampled`
in `phase252/results/p2522_results.json`), with the
refined bracket lo end t = 0.65625 read from the aux
march. Phase 256's CTRL-1 reproduced those rows at
**max abs diff 0.0** — all 41 sampled clause minima and
both bracket ends, profiles also 0.0 (R256 §4; M256 §2).
Worst per-clause minima over the sampled instants
t ≤ 0.65 plus the refined lo instant t = 0.65625,
computed by this gate from the stored `reposed_sampled`
rows and `reposed_bracket` lo margins (selection /
minimum on stored floats only):

| clause | worst minimum on [0, 0.65625] sampled + lo | at t |
|---|---|---|
| NEC_φ | **+0.05279917238250764** | 0.65625 |
| DEC_φ | **+0.05279917238250764** | 0.65625 |
| NEC_ρ | +1.6812500000000001 | 0 |
| DEC_ρ | +1.6812500000000001 | 0 |
| NEC_θ | +1.6875750349885346 | 0 |
| DEC_θ | +1.6875750349885346 | 0 |
| WEC | +2.306493031032269 | 0 |

(The binding pair decreases monotonically toward the
bracket — +1.126925 at t = 0.5625, +0.888262 at 0.6,
+0.618093 at 0.625, +0.174521 at 0.65, +0.052799 at
0.65625, per M252-2 §3's carrier trajectory — while
every non-binding clause's interval minimum sits at
t = 0 and only grows.) So Part 1 is *true at the sampled
instants*, on one grid, reproduced bit-exactly by the
certifying phase's control. It is a sampled-instant
read statement — the Gate-22/Gate-23 "[0, 0.5] at the 21
sampled instants" evidence class.

**Part 2 — "CERTIFIED at the Phase 243 standard
(Richardson limits…)".** Evidence class: **the window
certificate, binding clauses only.** CERT-1…3 concern
NEC_φ/DEC_φ alone, at the 10 window instants of
[0.6, 0.75] only (R256 §3). The non-binding clauses
enter the certificate only through CERT-4: positivity
**at G5** (a finest-grid condition, not a limit
condition — Gate-23 §2 made exactly this distinction
for Phase 243) at window instants ≤ t_hi, plus the
non-clause bars at the bracket instants (M256 §4:
next clause at the hi end ≥ +4.188 at G5; momentum
≤ 6.106×10⁻¹⁶, flare ≥ 0.12069, domain R ≥ 0.59964).
Nothing in Phase 256 limit-certifies any clause on
[0, 0.6), and nothing limit-certifies the five
non-binding clauses anywhere.

### 6.2 Does G26-A as worded conflate the two classes?

**Yes — in the same way, and for the same reason, as
the wording Gate-23 §2 restated.** Gate-23's G23-A
restatement split the claim precisely because
"satisfies every throat clause on [0, t)" fused a
sampled-instant part ([0, 0.5], G4 reads) with a
window limit-certified part ((0.5, 0.65], binding
clauses at the limit, non-binding at G5). G26-A's
sentence attaches "CERTIFIED at the Phase 243 standard
(Richardson limits…)" to a subject whose span
([0, 0.65625], all seven clauses) is mostly *outside*
the Richardson evidence (which covers [0.6, 0.75],
two clauses, plus G5-positivity for the rest inside
the window). A reader taking the sentence at face
value would believe all seven clauses hold *at
Richardson limits* on [0, 0.65625]. The record supports
no such statement. The defect is wording scope, not
evidence: every component claim is on the record at
its own class, and both classes are strong of their
kind (diff-0.0 reproduction; §4's grid-stability
certificate). **G26-A survives only in split,
restated wording**, following Gate-23 §2's model.

### 6.3 Draft restated G26-A (Gate-23 style, quotable form)

> *On the Phase 169 A-branch throat datum with the true
> lock, the composed combined-class pose (κ = 0.3
> director + C2 rotating headline construction,
> W = 0.2 sin²θ profile family + CH-PHI-Auu under
> P-PHI-TRIM-248: a(t) = −0.5 − c_trim·t² with the
> stored fitted c_trim = +5.253378 — fitted in Phase
> 248 under the registered formula c_trim = −q₂/s̄ to
> the composed arm's measured NEC_φ t² drift
> coefficient over [0, 0.475] and Phase 246's stored
> mean Auu sensitivity, frozen thereafter — clamped at
> the operational stop B := 2.5, which binds from
> t_stop = 0.617015, so the pose reads a ≡ −2.5 at and
> after that instant) meets every registered throat
> clause bar at all 27 sampled instants of [0, 0.65]
> and at the refined instant t = 0.65625 on the
> standing grid (N_θ = 2881; worst per-clause minima
> over those instants: NEC_φ = DEC_φ
> +0.05279917238250764 at t = 0.65625, NEC_ρ = DEC_ρ
> +1.6812500000000001, NEC_θ = DEC_θ
> +1.6875750349885346, WEC +2.306493031032269, the
> non-binding minima at t = 0; the standing-grid rows
> reproduced by Phase 256's CTRL-1 at max abs diff
> 0.0), and on the registered window [0.6, 0.75] its
> binding clauses NEC_φ = DEC_φ are limit-certified at
> every window instant under per-instant Richardson
> limits on G3/G4/G5 at the unchanged 1×10⁻⁶ bar — the
> three grids' binding reads agreeing to worst
> |d34| = 1.750×10⁻¹³, worst |d45| = 1.865×10⁻¹⁴,
> worst residual 2.220×10⁻¹⁵, the limit coinciding
> with the finest-grid read at that precision (a
> grid-stability certificate for a read-level sector,
> not a measured convergence rate) — the limits and
> the G5 reads straddling zero at the bracket
> (L(0.65625) = +0.05279917238387332, L(0.6625) =
> −0.073694680424036624) with no earlier in-window
> crossing and every non-binding clause positive at
> G5 at every window instant ≤ 0.6625 (next clause at
> the hi end ≥ +4.188) — so the pose's first crossing
> sits at t ∈ (0.65625, 0.6625] on NEC_φ = DEC_φ, in
> the certified scope of the fences: tail reads past
> [0.6, 0.75] are not certified (tail priced from
> Phase 256's fresh G3/G4 rows: first 1×10⁻⁶
> exceedance at t = 0.775, stage max
> 1.6326915963205124×10⁻⁵ at t = 1.0 on DEC_θ); the
> certified object is the trim law as clamped at
> B := 2.5, an operational stop at the end of Phase
> 252's audited amplitude range [0, −2.5], not a
> priced boundary, with no B-sensitivity on record;
> jet scope / sector superposition (exhibit ≠
> construction); programme-level sustainment wording
> remains gated by p1592 regardless. The interval is
> [0, 0.65625] at the sampled and refined instants
> named, and the window statement is [0.6, 0.75] at
> the window instants named; no continuum claim
> between instants is made or certified.*

Differences from the G26-A wording as put to the gate,
each forced by a section of this memo: the sampled part
and the window part are stated separately with their
grids and evidence classes (§6.1); "all seven clauses …
CERTIFIED (Richardson)" is replaced by seven-clause
sampled reads + two-clause limits + G5 positivity
(§6.2); the trim coefficient is named *fitted* with its
provenance (§3.3); the certified object is named as the
law *as clamped*, with t_stop on the face (§2.4); the
Richardson sentence carries the grid-stability anatomy
and no convergence-rate implication (§4); the tail
price carries its fresh-rows provenance (§1.3).

---

## 7. HEADLINES FOR THE GATE

1. **Diff:** A1–A4 verified as stated (A2 a true
   non-adaptation; A3/A4 exact, §5). One further
   adaptation exists — §5(c)'s tail-pricing source
   (fresh G3/G4 rows for stored rows), face-disclosed
   but uncounted: "exactly four" fails as a count,
   survives as substance. Three further Gate-23-class
   disclosed elaborations; **zero hidden substantive
   differences**; no bar, window, clause or CERT
   condition moved anywhere.
2. **B := 2.5:** underived — the audited sweep's round
   endpoint, adopted as an operational stop, and
   disclosed as such everywhere. It binds at 0.617015,
   inside the window and before the bracket, so the
   certified bracket is a bracket of the clamped pose;
   no B-sensitivity is on record and the record's own
   0.8-vs-2.5 comparison proves the bracket
   clamp-sensitive as a class. Verdict: **operational
   stop (pose parameter), not a smuggled assumption** —
   with the standing wording debt that the certified
   object must always be named "the trim law as clamped
   at B := 2.5".
3. **Trim law:** c_trim is a fitted counter-term whose
   formula was registered before the fit (Phase 248),
   frozen before its first march, never re-fit (Phases
   252/256 pin it by control); Amendment A-1 does not
   touch its derivation (it amended the forced-form
   classification sub-criterion only, and states so).
   Verdict: **legitimate pose parameter; certificate at
   full weight — provided the claim names the
   coefficient as fitted, with provenance, and never
   lets "CH-PHI-Auu trim" imply a physics derivation.**
4. **A2:** the Richardson certificate here certifies
   **grid-stability / cross-grid reproduction** of a
   read-level sector (agreements ≤ 1.750×10⁻¹³,
   residuals ≤ 2.220×10⁻¹⁵, limit ≡ finest read), not
   a measured convergence to a limit as in Phase 243
   (p ≈ 2.0000, 10⁻⁷-class real error). Weaker in that
   one dimension, equal in the others; the anatomy is
   on M256 §4's own face. Claim wording must carry it
   (§4's draft sentence).
5. **G26-A:** as worded, it conflates the sampled
   seven-clause evidence ([0, 0.65625], standing grid,
   CTRL-1 diff 0.0) with the window Richardson evidence
   ([0.6, 0.75], binding clauses only). **Survives
   only in the split restated wording of §6.3.**

*No computation beyond text diffs, stored-row selection
and small arithmetic was performed; no march was run;
nothing outside `gate26/` was written.*
