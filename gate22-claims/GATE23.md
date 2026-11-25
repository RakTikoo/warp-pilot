# GATE-23 — ADJUDICATION OF THE PHASE 243 CERTIFIED CLAIM SET
# (amending Gate-22)

Date: 2026-11-24. Adversarial re-judgement, not a phase. Frame
of record: Phase 166 pin, Gate-19-corrected tensor, venv python
(numpy 2.5.5 / scipy 1.18.1). Method: Gate-23 re-derived every
deciding number from the stored artefacts of Phases 214/234/243
with its own arithmetic (`gate23/work/g23_verify.py` →
`gate23/work/g23_verify_results.json`) — pure JSON arithmetic
on the stored per-grid rows; no programme engine was imported
and no march was re-run. The Richardson limits, the CERT
booleans, the CERT-4 non-clause bars, the CTRL-1 artefact
agreement, and the CTRL-2 / tail-pricing numbers were all
recomputed by that separate path. Independence, priced on the
face: the gate's path is independent of Phase 243's driver and
checker at the arithmetic level (it re-derives from the same
stored rows — the same independence class as Gates 15/19/22,
whose re-runs shared the frame of record).

## VERDICTS

- **G23-A: SURVIVES IN RESTATED WORDING** (restated wording in
  §2). The certificate's arithmetic is fully verified; the two
  corrections are scope/margin precision: the claim's interval
  wording is continuum where its evidence is sampled/window
  instants (the Gate-22 defect, §5), and its ">10×" margin
  phrase is false for one of the three certified components
  (§1).
- **G23-B: SURVIVES INTACT.** Phase 214's t* bracket certifies
  under the same certificate (disposition T-A), independently
  recomputed; the comparison is in one frame.
- **G23-C: SURVIVES INTACT.** All three fences verified — the
  tail numbers recomputed exactly from Phase 234's stored
  rows (§1), the pose/jet scope as registered, the p1592 gate
  untouched by the certificate's design.
- **Novelty: NONE granted** — Gate-22 §6's position carries
  over unchanged (§6).

No claim FAILS. No deciding number in Phase 243's record
failed to reproduce: the gate's recomputation of the recorded
certificate agrees to ≤ 9.6×10⁻¹⁷ (float round-off in
re-derivation), CTRL-1's artefact agreement is 0.0, and the
tail pricing is bit-exact against Phase 234's stored rows.

---

## §1. Attack line (1) — the Richardson straddle, independently
## verified; the margin phrase priced

Gate-23 recomputed the per-instant Richardson treatment from
the stored G3/G4/G5 window rows in `p2431_results.json`
(NEC_φ and DEC_φ — pointwise identical in this machinery, so
one row serves both, as the record states):

**New bracket.** Every window instant's (d34, d45, p, L, r,
certified) reproduces the recorded certificate (max deviation
9.6×10⁻¹⁷). The monotone instants sit at p ∈ [1.99999,
2.00003] — the claim's "p ≈ 2.0000" is exact for this window.
The straddle is real: **L(0.55625) = +0.004468142716485732 ≥ 0,
L(0.5625) = −0.054339801013359036 < 0**, with v5 agreeing in
sign at both instants; CERT-3 holds (no earlier in-window
crossing at L or v5); CERT-1/2/4 all TRUE under the gate's own
evaluation.

**The margin phrase does not survive as stated.** The claim
(and Phase 243's memo §4) says every window instant clears
the 1×10⁻⁶ bar "by more than an order of magnitude". Priced
per component over the new window (binding clauses):

| component | worst | factor under the 1×10⁻⁶ bar |
|---|---|---|
| \|d34\| | 3.481684300865595×10⁻⁷ (t = 0.65) | **2.87×** |
| \|d45\| | 8.704146647886546×10⁻⁸ (t = 0.65) | 11.49× |
| residual r | 2.901353725451977×10⁻⁸ (t = 0.65) | 34.47× |

The blanket ">10×" holds for |d45| and r but **fails for
|d34|** (2.87×). The certificate is unaffected — every
component is under the bar at every instant, which is what
CERT-1 requires — but the quotable wording must price the
margins exactly (§2). (Phase 243's recorded worst |d34|,
3.482×10⁻⁷, and the gate's 3.481684300865595×10⁻⁷ are the
same number at the memo's printed precision.)

**One case-classification note, priced nil.** At the
three-channel window instants t = 0.5 and t = 0.525 the
differences share a sign but imply p = −1.977 / −0.890
(inadmissible), and Phase 243's driver files them under the
degenerate case (L := v5, r := max(|d34|, |d45|)). The
registration's §3 text defines the monotone case by
d34·d45 > 0 with admissibility 0.5 ≤ p ≤ 6 stated inside it;
the driver's split implements "admissible" as part of the
case definition. Gate-23 cross-checked the literal
alternative — the monotone formula applied at the
inadmissible p — and both instants still certify
(L_literal = +0.4445109377225491 / +0.267257479518888 ≥ 0;
|r_literal| = 2.71×10⁻⁸ / 5.25×10⁻⁸ ≤ bar). The two readings
disagree on a label at two non-bracket instants and on no
deciding number; the classification is noted here so the
record carries it, and it changes no verdict.

**t* window (for §3).** The same recomputation reproduces
Phase 243's t* certificate (max deviation 2.6×10⁻¹⁷):
L(0.5) = +0.004541864595164523 ≥ 0, L(0.50625) =
−0.035378628675540646 < 0; CERT-1…4 all TRUE. The t* window's
order reads are NOT ≈ 2.0000 (p ∈ [0.99992, 3.13811]; the
bracket instants sit at p = 3.13810) — no claim says they
are; the p ≈ 2.0000 phrase belongs to the new bracket only,
and the restated G23-A keeps it there.

**Tail pricing (for §4).** Recomputed from Phase 234's stored
G3/G4 rows (`threech_G3/G4_instants_primary`), Gate-23 gets,
bit-exact against the recorded pricing: Stage A max
3.4339573895536546×10⁻⁷; Stage B max
3.4498744435396134×10⁻⁵; first Stage B exceedance of the
1×10⁻⁶ bar at t = 0.775; worst instant t = 1.0, carrier
DEC_θ, relative disagreement 3.3942464143610627×10⁻⁶;
per-instant disagreements on (0.5, 0.65] of 2.38697642096497×
10⁻⁷ … 6.25625901307103×10⁻⁷, all under the bar.

## §2. G23-A — the extension: SURVIVES IN RESTATED WORDING

The deciding numbers are verified (§1, §3). What the
original wording outruns is its scope, in the same way
Gate-22 §1 found for the [0, 0.5] claim: "satisfies every
throat clause on [0, t)" is a continuum sentence, and the
evidence is instants —

- on [0, 0.5]: Phase 234's G4 march at 21 sampled instants
  (Gate-23 verified from the stored rows: worst per-clause
  minima over those instants — NEC_φ = DEC_φ
  +0.4445109446003479, NEC_ρ = DEC_ρ +1.2658166235665387,
  NEC_θ = DEC_θ +1.9907384300755062, WEC +2.3328215038710747,
  all at t = 0.5), Stage A gate 3.4339573895536546×10⁻⁷, and
  Phase 243's CTRL-1 reproduction (§3 of this gate);
- on the window (0.5, 0.65]: the binding clauses
  limit-certified at every window instant (CERT-1), the
  bracket straddled at the limit and at G5 (CERT-2), no
  earlier in-window crossing (CERT-3), and the non-binding
  clauses positive at G5 at every window instant ≤ t_hi
  (CERT-4; the window's non-binding G5 minimum there is
  +1.0390366790303922) — a G5-instant condition, not a
  limit condition on the non-binding clauses, exactly as
  the certificate was registered.

**Restated G23-A (the quotable form):** *On the Phase 169
A-branch throat datum with the true lock, the three-channel
pose (κ = 0.3 wound director under P-DIR-T2 + CH-COMB
profile channel under P-PROF-FROZEN + CH-PHI-Auu φ channel,
flat a = −0.5, under P-PHI-FROZEN) meets every registered
throat clause bar at all sampled instants of [0, 0.5] on
grid G4 (worst clause minimum +0.4445109446003479, NEC_φ =
DEC_φ at t = 0.5; Stage A refinement gate
3.4339573895536546×10⁻⁷), and on the registered window
(0.5, 0.65] its binding clauses NEC_φ = DEC_φ are
limit-certified at every window instant under per-instant
Richardson limits on G3/G4/G5 (monotone order reads p ∈
[1.99999, 2.00003]; worst |d34| = 3.481684300865595×10⁻⁷,
worst |d45| = 8.704146647886546×10⁻⁸, worst residual
2.901353725451977×10⁻⁸, against the unchanged 1×10⁻⁶ bar),
the limits and the G5 reads straddling zero at the bracket
(L(0.55625) = +0.004468142716485732, L(0.5625) =
−0.054339801013359036) with no earlier in-window crossing
and every non-binding clause positive at G5 at every window
instant ≤ 0.5625 — so the pose's first crossing sits at
t ∈ (0.55625, 0.5625] on NEC_φ = DEC_φ, in the certified
scope of G23-C's fences. The interval is [0, t) at the
sampled and window instants named; no continuum claim
between instants is made or certified.*

## §3. Attack lines (2) and (3) — the CTRL-1 repair, and
## CERT-4's non-clause bars

**(2) The repair was the only substantive change; the scope
argument is verbatim.** Gate-23 diffed
`phase240/work/p2401_registration.md` against
`phase243/work/p2431_registration.md` in full. §§0, 1 (the
scope argument), 2 (the t* disposition) and 6 (the decision
order) are **character-identical** — the scope argument was
carried verbatim, not "in substance", and not widened: the
1×10⁻⁶ threshold, the window (0.5, 0.65], the CERT-1…4
conditions, and the verdict forms are unchanged. Every
difference in the file is one of:

- §R itself (the repair, stated on the face with Phase
  240's anatomy cited) and its three declared consequences:
  §3's march-length sentence and §5(a)'s T_END sentence
  (repair (b)); §4's CTRL-1 restated at matched march
  length, T_END = 1.0 (repair (a)); §5(e)'s probe arithmetic
  adapted to the [0, 1.0] march (20 × probe; state sizes
  restated; the 900 s threshold unchanged) (repair (c));
- cosmetics: title/phase numbers, the kernel-spec path in
  form 3, §7's header "verbatim" → "verbatim in substance"
  (the forms' text is in fact identical);
- two additions **not** listed in §R, both disclosed in
  Phase 243's own memo (§8) and checkpoint, neither touching
  a bar, a window, or a deciding number: §8's sentences
  recording that Phase 240's control-stopped record stands
  and that this registration is its named successor, not an
  amendment (a narrowing disclaimer); and §9's sentences
  writing the checker's assertions to match the registered
  decision order (a recorded control outcome is checked for
  internal consistency with its recorded numbers rather
  than asserted to be a pass). On this run the stricter
  assert-pass form would also have passed — CTRL-1 recorded
  a pass with all diffs 0.0 — and Gate-23's verdicts rest on
  its own recomputation, not on Phase 243's checker (17/17,
  as recorded) in either form.

Gate-23 also re-derived CTRL-1's agreement from the stored
artefacts alone (no fresh march): Phase 243's stored G3/G4
window rows vs Phase 234's stored three-channel rows and
Phase 214's stored director rows agree at max abs diff
**0.0** on all four comparisons (G4 sampled, G3 sampled, G4
refined, director G4 sampled). The stored record the
certificate rests on is internally bit-consistent across
three phases.

**(3) CERT-4's non-clause bars re-read at the bracket
instants** (from the stored G5 rows, Gate-23's own reads):

New bracket — t = 0.55625: momentum worst
3.885780586188048×10⁻¹⁶ ≤ 1×10⁻¹⁰; flare min
0.14038579426044095 > 0; domain R min 0.6587527029800476 > 0;
exp(2Φ) min 0.005811245495000393 > 0. t = 0.5625: momentum
worst 4.440892098500626×10⁻¹⁶; flare min
0.1392551145979583; domain R min 0.6555607744146429;
exp(2Φ) min 0.005811245459629085. All pass, matching the
recorded CERT-4 bars to the last digit.

t* bracket — t = 0.5: momentum worst
3.885780586188048×10⁻¹⁶; flare min 0.15033189900880242;
domain R min 0.6858751797844092. t = 0.50625: momentum worst
2.636779683484747×10⁻¹⁶; flare min 0.14924956565808287;
domain R min 0.6830042272758607. All pass. One margin priced
on the face: at t*'s t_hi the nearest non-binding clause at
G5 is NEC_ρ at **+0.004707162309991464** — CERT-4 holds, and
consistently with Phase 214's own ordering (NEC_ρ crosses
one refinement step later, in (0.50625, 0.5125]); the margin
is real but not large, and the restated set carries it here
rather than in the claim.

## §4. G23-B and G23-C

**G23-B: SURVIVES INTACT.** Phase 214's director-only
t* ∈ (0.5, 0.50625] certifies under the same certificate
(disposition T-A): Gate-23's independent evaluation gives
CERT-1…4 all TRUE on the t* window, the limit straddle
L(0.5) = +0.004541864595164523 / L(0.50625) =
−0.035378628675540646, and CTRL-3's G5 sanity reads
(1.4235054024425153×10⁻⁸ at t = 0.25, 5.694021876223587×10⁻⁸
at t = 0.5 vs Phase 210's stored G4) as recorded. The
extension of G23-A is therefore a one-frame comparison —
both brackets certified by one instrument, at one bar — not
a cross-instrument one. Phase 214's verdict stands for its
own pose and scope (a G4 read) exactly as its checkpoint
states; G23-B adds the certificate, it does not rewrite
Phase 214.

**G23-C: SURVIVES INTACT** — the fences are claims about
scope, and each is verified: (i) tail reads past the window
are not certified — the Stage B stage-max gate still fails,
first exceedance at t = 0.775, max 3.4498744435396134×10⁻⁵
at t = 1.0 on DEC_θ, recomputed bit-exact by this gate
(§1); (ii) the result is pose-scoped (the named datum, lock,
and three channels with their frozen prescriptions) and
jet-scoped (sector superposition exhibit ≠ construction —
no claim a physical sector realises the three channels
jointly); (iii) programme-level "sustained wormhole"
wording remains gated by the p1592 deciding scan regardless
of this gate's outcome — the certificate's design (§8 of
both registrations) leaves that gate untouched, and this
gate grants no programme-level wording either.

## §5. The amended Gate-22 claim set (the quotable whole)

Gate-22's surviving claims stand as restated there (G22-1:
the director arm's clause set on [0, 0.5] at the 21 sampled
instants; G22-2: the refinement gate is a grid artefact;
G22-3: their conjunction at pose scope, interval exactly
[0, 0.5]). Gate-23 appends, for the three-channel pose:

- **G23-A (restated, §2):** the three-channel pose meets
  every registered throat clause bar at all sampled instants
  of [0, 0.5] on G4 and is limit-certified on the window
  (0.5, 0.65] in the terms stated, with first crossing at
  t ∈ (0.55625, 0.5625] on NEC_φ = DEC_φ.
- **G23-B:** Phase 214's t* ∈ (0.5, 0.50625] certifies under
  the same certificate (T-A); the extension is a one-frame
  comparison.
- **G23-C:** the fences — tail reads past the window not
  certified (Stage B exceedance from t = 0.775); pose scope
  and jet scope as registered; programme-level sustainment
  wording remains gated by p1592 regardless.

**Publication consequence:** the amended set — Gate-22's
restated G22-1/G22-2/G22-3 plus G23-A (restated), G23-B and
G23-C above — joins the v1.22.0 bundle's claim list in this
wording. (Packaging is the parent's act, not this gate's.)

## §6. Novelty position

Unchanged from Gate-22 §6, and it extends to the new claims
without re-search: every ingredient remains published; the
extension is the same pose class, at the same jet/channel
scope, marched further under a stricter certificate — it
inherits both Gate-22's "not found in our search (limits:
…)" position and its stated headwind (Hochberg & Visser:
NEC violation is generic for dynamic throats in full
spacetimes; these claims are not a full-spacetime solution,
and the scope fence is what keeps the two from colliding).
**No "first", "unique" or "record" wording is granted or
implied for G23-A/G23-B/G23-C.**

## Files

- `gate23/work/g23_verify.py` + `g23_verify_results.json` —
  Gate-23's independent re-derivation: Richardson limits and
  CERT booleans for both brackets from the stored per-grid
  rows; CERT-4 non-clause bars at the bracket instants;
  CTRL-1 artefact agreement (0.0) across Phases 214/234/243;
  CTRL-2 stage gates and tail pricing from Phase 234's
  stored rows; the [0, 0.5] three-channel clause record; the
  literal-reading cross-check of §1.
- No ledger append, no launches, no external contact.
  Nothing outside `gate23/` was edited.
