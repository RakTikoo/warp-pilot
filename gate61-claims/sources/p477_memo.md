# P477 — MEMO: THE FUU ARBITRATION (FU-P467-1)
## (ledger entry 1237)

Phase 477 coordinator, warp pilot. Registration:
`phase477/work/p477_registration.md` (written BEFORE
any deciding computation; one amendment, A1,
evaluation-only, §7). Frame of record: Phase 166 pin,
Gate-19-corrected tensor, venv python (numpy 2.5.5 /
scipy 1.18.1), float64. Deciding reads on the VM
only. INTERNAL only. No ledger append, no launches,
no external contact; nothing outside `phase477/`
written.

**The three goals:** (1) FTL drive — no contact: the
object is a throat datum's jet pair, not a drive
configuration. (2) Functional wormhole — this phase's
home goal: the build ambiguity on the scaled datum's
tide read (Phase 467) is traced to its source and its
scope is settled exactly; the arbitration itself
stops at the charge's registered stop rule (§0).
(3) Subluminal record — no contact.

**DESK: NO DATA CONTACT.**

## 0. FIRST RESULT — THE DIVERGENCE REACHES THE
## LEGALITY CLAUSES; THE ARBITRATION STOPS HERE

The charge (entry 1237) premises that the legality
vector agrees between the record's two jet builds,
confines the arbitration to Fuu/Mtt on that premise,
and registers the stop rule: if the trace shows the
divergence reaches the legality clauses, that is the
first result and the arbitration stops for the
parent's re-registration. **The premise fails, by
measurement (T3, §4).** Composing the P226-1 primary
composition on the compensated build (Phase 254's
path) does NOT reproduce the datum's stored clause
vector. Per-clause minima deltas of the compensated
build's read (X, mtt_field feed — 467's CTL-3 build)
against the stored vector:

| clause | stored (home) | X read | delta |
|---|---|---|---|
| NEC_ρ | +0.6781346234610093 | +0.6781346234610093 | 0.0 |
| NEC_θ | +0.9281631165591328 | +1.4790316944454176 | +0.5508685778862848 |
| NEC_φ | +0.1764749454550547 | +0.9030810951057349 | +0.7266061496506802 |
| WEC | +1.3094045367416725 | +1.3094045367416725 | 0.0 |
| DEC_ρ | +0.6781346234610093 | +0.6781346234610093 | 0.0 |
| DEC_θ | +0.9281631165591328 | +1.1394910646834866 | +0.2113279481243538 |
| DEC_φ | +0.1764749454550547 | +0.9030810951057349 | +0.7266061496506802 |

The full clause ARRAYS differ by up to
0.765001585541698 (transverse clauses; §4). **No
verdict form of registration §4 fires.** What
follows is the complete trace the re-registration
needs: the divergence is a single, exactly
characterised quantity (§2–§4), both builds compute
their stored definitions exactly (§1), and the
trace's conclusions about which Fuu is the datum's
are stated as derivations in §6 — for the parent to
record under a re-registered charge, not as a
verdict of this one.

**Wording discipline (registration §0, in force):**
this datum is not the Gate-27 certified pose and
carries no certificate; jet scope, t = 0, sector
superposition, exhibit ≠ construction. **No
traversability claim is made anywhere in this
memo.**

## 1. CONTROLS — both builds compute their stored
## definitions exactly

- **CTL-H PASS (diff 0.0).** The P226-1 build
  verbatim (fine grid 2881, (A1) anchor ũ_true,
  `J0 = instant_jets(0, 0,0,0,0, ũ_a)`, CH-COMB
  a = +0.10, director κ = 0.254873): base C-κ0
  minima and the primary-point combined vector
  reproduce `p2261_results.json` at max abs diff
  0.0; ũ_true(θ*) = 1.1412482021558361.
- **CTL-X PASS (diff 0.0).** Phase 254's assembly
  verbatim (march(2881, 0.0025), `mtt_field`,
  `comp_jets` t = 0 slice, wound posing): the wound
  datum's tide worsts reproduce
  `p2542_results.json` at abs diff 0.0 on all three
  components (stored 0.46327403240424314 /
  0.9369752522890477 / 0.9718746251967629 pose⁻²);
  the fallback anchors pass at P254-2's registered
  tolerances.
- **CTL-467 PASS.** 467's CTL-3 comparison
  reproduced exactly: jet diffs Fuu
  0.9343747896249985, Mtt 2.569525345830215×10⁻⁷,
  every other JET_ORDER field 0.0; tide diffs
  R_tltl 0.765001585541698, R_tthtth and R_lthlth
  0.0; home radial worst 1.5202791951713714 at
  θ = π/2; X radial worst 0.9718746251967629.
- **Checker** (`work/p477_check.py`): overall PASS
  — CTL-H combined vector and CTL-X wound worsts
  re-derived in a fresh process at 0.0; the T3
  H(0) and X(ũ_true) rows recomputed by an
  independently ordered assembly (own clause
  arithmetic) at 0.0; rescue arithmetic recomputed
  at 0.0; decision consistency verified (§7 for
  the checker's one corrected pairing).

Neither build is arithmetically defective. The
divergence is definitional, and it is traced next.

## 2. T1 — EVERY (Fuu, Mtt)-CARRYING READ READS ONE
## COMBINATION: D := e^{−2M}·Fuu − e^{−2F}·Mtt

Symbolic differentiation of the stored expressions
themselves (`phase129/work/p1296_derive_raw.json`;
`phase254/work/p2542_riemann_jets.json`), tested by
the gradient identity ∂g/∂Mtt + e^{2(M−F)}·∂g/∂Fuu
≡ 0 (evaluated at the datum jets and at five
perturbed jet points; relative residual
4.0×10⁻¹⁶) and by direct perturbation of the
lambdified reads along D-preserving vs D-changing
directions at the posed jets (T1b; D-preserving
changes ≤ 4.4×10⁻¹⁶ on every read, D-changing
changes O(δ)):

- **Channels:** rho8, prho8, mom_rho, mom_th,
  mom_ph, S carry neither Fuu nor Mtt. **pth8 and
  pph8 carry (Fuu, Mtt) only through D**, with
  ∂/∂Fuu = e^{−2M} (= 0.8187307530779818 on the
  composed jets, M = 0.1) and ∂/∂Mtt = −e^{−2F}
  (= −1.4914667503993406 at θ = 0.02,
  −0.8187307530779819 at θ*) — i.e. unit
  coefficient on D itself.
- **Tides:** R_tthtth and R_lthlth carry neither
  Fuu nor Mtt (hence their exact agreement between
  the builds, and the variant-independent lateral
  rescue in §5). **R_tltl carries (Fuu, Mtt) only
  through D**, with the same evaluated derivatives
  as the transverse channels; its response to the
  H → X step is exactly affine (linearisation
  residual 3.3×10⁻¹⁶, §5).

**Consequence, stated once and used throughout:**
there is no separate "tide ambiguity" and "clause
ambiguity". Every read that differs between the
builds reads the single quantity D of the composed
jets; the builds differ exactly where their D
differs. The clause spread and the tide spread of
467's CTL-3 are the same ΔD through two reads —
numerically the same number at the maximum
(§4/§5: 0.765001585541698).

## 3. T2 — THE PARTING STEP

The two builds part at exactly one line each:

- **Home:** `instant_jets` poses **`'Fuu':
  j_prof(θ)`** — the P159-3b audit closed form,
  the exact ∂²Φ/∂u² of the recorded pose
  Φ(u,θ,t) = Φ₀(θ) + (u²/2)·J(θ). It is posed
  data: no march, no Mtt, enters it.
- **Compensated:** `comp_jets` calls
  `instant_jets` and then **replaces Fuu**:
  `J['Fuu'] = e^{2μ}·(j_prof + e^{−2Φ₀}·mtt_a)` —
  the exact ∂²Φ/∂u² of Phase 167's own posed Φ
  (Φ₂ = ½·e^{2μ₀}·J_pose, J_pose = J_c +
  e^{−2Φ₀}·μ_,tt; CHECKPOINT167 P167-1(a)), a
  μ_,tt-loaded, time-dependent dial, by that
  phase's registered design: a compensating
  degree of freedom that cancels the forced
  μ_,tt **in the channels**.

Measured identity at t = 0 (μ₀ ≡ 0):
**Fuu_X − Fuu_H = e^{−2Φ₀(θ)}·Mtt(θ) pointwise**
(max deviation of the identity 1.1×10⁻¹⁶), max
0.9343747896249985 at θ* — 467's CTL-3 Fuu spread.

**The Mtt feeds agree; they are not the
divergence.** Home feeds the (A1) analytic anchor
ũ_true (Phase 169 P169-1(d)(A1), the true-lock
anchor); X feeds `mtt_field`, the march FD on the
Phase-169-fixed engine. Max |difference| on the
audit grid = 2.569525345830215×10⁻⁷ — exactly the
FD-vs-anchor class Phase 169 itself stored
(FD θ* 1.1412479452033015 vs analytic
1.1412482021558361). The record's OTHER anchor —
the defective-lock ũ (θ* = 0.8883536487880518),
surviving in `p167_engine.utilde_analytic` and
Phase 167's own t = 0 posed reads — is used by
**neither** build as composed by Phases 254/467;
it is recorded here so the Mtt provenance is
whole, and it plays no role in the divergence.

Define the tax profile τ(θ) := e^{−2Φ₀(θ)}·ũ(θ):
τ(θ*) = 0.9343749999999407 (anchor feed;
0.9343747896249985 with the FD feed — the
2.1×10⁻⁷ feed difference). On the home build the
transverse channels carry the tax in full: the
H(0) − H(ũ_true) clause-array difference is
τ(θ) pointwise (response ratio 1.0000000000000002
at θ*; array max 0.9343749999999406).

## 4. T3 — LEGALITY REACH: THE FIVE VARIANTS, AND
## WHY THE COMPENSATION LANDS BETWEEN TWO POSES

The primary composition (CH-COMB + director
applied identically) on five jet variants —
H(m) := `instant_jets` fed Mtt = m; X(m) :=
`comp_jets` fed Mtt = m:

| variant | NEC_θ min | NEC_φ min | DEC_θ min | DEC_φ min |
|---|---|---|---|---|
| **H(ũ_true) — the datum as recorded** | +0.9281631165591328 | +0.1764749454550547 | +0.9281631165591328 | +0.1764749454550547 |
| H(0) | +1.479198706005177 | +1.0541767526056953 | +1.0279422865525754 | +1.0541767526056953 |
| X(mtt_field) — 467's X | +1.4790316944454176 | +0.9030810951057349 | +1.1394910646834866 | +0.9030810951057349 |
| X(ũ_true) | +1.479031694445414 | +0.9030810669112042 | +1.1394910646834866 | +0.9030810669112042 |
| X(0) | = H(0), jet-identical (all 40 fields, diff 0.0) | | | |

(NEC_ρ, DEC_ρ, WEC minima are the stored values on
every variant — rho8/prho8 carry no (Fuu, Mtt).)

**The D each variant poses** (composed jets,
M = 0.1 after CH-COMB; j := j_prof):

- D_H(ũ) = e^{−0.2}·j − τ(θ) — the tax in full.
- D_H(0) = e^{−0.2}·j — tax-free.
- D_X(m) = e^{−0.2}·j − (1 − e^{−0.2})·τ_m(θ) —
  the tax reduced to the fraction (1 − e^{−0.2})
  ≈ 0.18127 of itself, **not removed**.

**The mechanism of the residue is exact, and it
localises the divergence to the composition step,
not to either engine.** Phase 167's cancellation
is exact in the compensated pose's own frame: the
pose's M profile IS μ₀, and e^{−2μ₀}·(e^{2μ₀}·
J_pose) = J_pose identically, so D = J_c there.
But in the assembly Phases 254/467 use, `comp_jets`
is applied at the t = 0 slice (μ₀ = 0) and CH-COMB
then poses **M += 0.1 on top** — the composed jets'
M (= 0.1) is no longer the μ₀ (= 0) the Fuu
replacement was keyed to, so e^{−2M}·Fuu picks up
the factor e^{−0.2} and the cancellation leaves
exactly the (1 − e^{−2a}) residue at CH-COMB's
amplitude a = 0.1. Clause-array spreads against
the stored composition, transverse clauses:
H(0): 0.9343749999999406 (= τ_anchor max);
X(anchor feed): 0.7650015474071905
(= e^{−0.2}·τ_anchor max, identity verified by the
checker at 2.2×10⁻¹⁶); X(FD feed):
0.765001585541698 (the same identity on τ_FD;
feeds differ by (1 − e^{−0.2})·(τ_anchor − τ_FD)
= 3.8×10⁻⁸ at the spread).

So the compensated build's read of this
composition is the clause vector of a **third
configuration** — neither the datum as recorded
(tax in full) nor the tax-free pose (H(0)); it
sits strictly between them, at a D determined by
the CH-COMB amplitude. The charge's premise —
one legality vector shared by the builds, tides
alone in dispute — does not hold for this
composition. (It would hold, exactly, for a
composition with no post-compensation M-posing:
at a = 0 the residue vanishes and X(m) ≡ H(0) at
the channel level for every m — Phase 167's
registered property, recovered here as the
a → 0 limit of the measured residue law.)

## 5. T4 — TIDE REACH, PRICED PER VARIANT

Radial component R_tltl (pose⁻²; signed at named
points) and the β = 0.1 rescue radii by 467's R⁻²
law (bar 4.905 s⁻², A = 0.8). The lateral
combination is variant-independent (worst
0.9459504297033866 pose⁻²; lateral rescue
105,323,522.02 m on every variant) — it carries
no (Fuu, Mtt).

| variant | R_tltl worst | at θ | R_tltl(π/2) signed | rescue (radial) | radial ratio at 1.068×10⁸ m |
|---|---|---|---|---|---|
| **H(ũ_true) — datum as recorded** | 1.5202791951713714 | π/2 | −1.5202791951713714 | **133,522,009.61 m** | 1.563015 (fail) |
| H(0) | 0.9718745756442096 | 0.02 | −0.5859041951714309 | 106,756,983.66 m | 0.999195 |
| X(mtt_field) | 0.9718746251967629 | 0.02 | −0.7552776096296735 | 106,756,986.38 m | 0.999195 |
| X(ũ_true) | 0.9718746251967629 | 0.02 | −0.7552776477641808 | 106,756,986.38 m | 0.999195 |
| X(0) | = H(0) | | | 106,756,983.66 m | 0.999195 |

The H → X radial step decomposes exactly:
ΔR_tltl = (∂R_tltl/∂D)·ΔD with the linearisation
residual 3.3×10⁻¹⁶ — the 0.765001585541698 tide
spread is the §4 clause spread, the same ΔD.
Note the pole values: at θ = 0.02 the variants
agree to ~5×10⁻⁷ (τ(0.02) ≈ 2.7×10⁻⁷), which is
why X's *worst* (pole-bound) nearly equals H(0)'s
while the builds' tides differ by 0.765 at the
equator — the worst-point summary hides the
divergence that the arrays carry in full.

## 6. WHAT THE TRACE ESTABLISHES (derivations, for
## the re-registration — not a verdict form)

1. **The datum as recorded is the home build's
   object, and its Fuu is j_prof.** P226-1's
   registration fixes the build verbatim
   (`instant_jets`, (A1) anchor); its stored
   clause vector exists only in that build and
   is reproduced there at diff 0.0 (CTL-H). Its
   Fuu is the posed profile J(θ) of the recorded
   pose Φ = Φ₀ + (u²/2)·J — posed data of the
   datum's definition, continuous with the
   P159-3b audit form and Phase 169's true-lock
   re-record (whose (A1) clause set IS this
   datum's base set, at the same values).
2. **The compensated build's Fuu is the Fuu of a
   different posed Φ** — Phase 167's compensated
   pose, whose u² coefficient is
   e^{2μ₀}·J_pose(θ,t) by that phase's registered
   design. It is computed exactly (CTL-X), and
   for Phase 167's own sustained-family purpose
   its channel property is exact in its own
   frame. It is not the Fuu of the P226-1 datum's
   Φ, and no stored definition poses the P226-1
   datum in the compensated family.
3. **Transplanted under the P226-1 composition,
   the compensated path poses a third D** (§4):
   its clause vector and its tide read
   (106,756,986.38 m) are reads of that
   configuration — not second readings of the
   datum, and not readings of the tax-free pose
   either. Phase 467's tide verdict stands on
   the home build not merely by its CTL-3 rule
   but by the derivation: 133,522,009.61 m is
   the rescue radius of the datum as recorded;
   the compensated number prices a configuration
   whose legality vector (+0.9030810951057349
   NEC_φ etc.) is not the datum's and was never
   recorded as one.
4. **The fork a re-registration would have to
   decide, named and not run here:** a
   compensated-build read OF a CH-COMB composition
   whose channels are the tax-free ones requires
   the Fuu replacement keyed to the COMPOSED
   pose's M (μ₀ := M_composed in `comp_jets`),
   i.e. a third assembly that is neither stored
   build. Whether that assembly is a legitimate
   posing of anything in the record is a
   registration question, not an arithmetic one.

## 7. AMENDMENTS AND INCIDENTS (disclosed)

- **Amendment A1 (evaluation only, run):** T1b's
  D-preserving perturbation direction was first
  implemented with the base-pose (M = 0) factor
  e^{−2Φ₀}; on the composed jets (M = 0.1) that
  direction is not D-preserving, and its first-
  launch readings (channels/R_tltl change
  0.02973927601195303 at δ = 0.11) are exactly the
  (1 − e^{−0.2}) residue of §4 seen from the
  other side. Corrected to the registered
  direction (factor e^{2(M−F)} on the jets' own
  M, F); corrected readings: invariance at
  ≤ 4.4×10⁻¹⁶. No registered definition, control,
  or decision rule changed; all other first-launch
  numbers are identical (deterministic rebuild).
- **Checker pairing (harness only):** the
  checker's first launch asserted the spread
  identity τ_max·e^{−0.2} against the FD-feed
  variant's spread and failed by 3.8×10⁻⁸ — the
  identity pairs with the matched (anchor) feed,
  against which it holds at 2.2×10⁻¹⁶; the FD
  offset is the feed propagation, now recorded
  separately in `p477_verify.json`. The run's
  results were untouched.

## 8. FENCES (on every number above)

Fuu/Mtt only — no other read of either build was
re-opened; Phase 254's own datum reads stand as
stored (reproduced as controls, not re-judged —
the residue law of §4 describes the assembly
pattern they share with 467's CTL-3, and any
consequence for them is the parent's to register,
not this phase's to draw). Jet scope, t = 0, one
datum, sector superposition, exhibit ≠
construction. This datum is not the Gate-27
certified pose and carries no certificate. No
traversability, transit, gain or shortcut wording
anywhere. GAP-1/GAP-2 untouched; FU-P226-1 (the
march) still unrun.

## Files

- `work/p477_registration.md` — registration
  (pre-run; Amendment A1 recorded in results +
  this memo §7).
- `work/p477_run.py` — driver (controls gate the
  trace; elapsed ≈ 35 s).
- `work/p477_check.py` — independent checker,
  overall PASS.
- `results/p477_results.json`,
  `results/p477_verify.json`,
  `results/p477_memo.md` (this file).
- No ledger append, no launch, nothing outside
  `phase477/` edited.
