# GATE-6 — Worker W-D report: G6-4 (P43-3c) COMPONENT-BLINDNESS

Worker W-D, Gate 6, 2026-11-22. Sources audited: `gate6/GATE6.md`
(standards), `phase43/results/p433_memo.md` §(c),
`phase43/CHECKPOINT43.md` §P43-3(c) verdicts, `phase27/CHECKPOINT27.md`
+ `phase27/results/p273_audit.md` (A1/A3/A4). Check code:
`gate6/wd_arith.py` (run with system python3 + mpmath, 30-digit).

## Verdicts (summary)

- **Correctness: REPRODUCED WITH RESTATEMENT.** The proof's logic is
  sound and its three counterexample routes are genuinely closed, but
  (i) the factored form B_tot = (Σᵢcᵢ)·Φ[f] with a *single common* Φ
  holds only where the per-field bounds really do share one Φ up to a
  constant; the theorem-grade general form is B_tot = Σᵢ Φᵢ[f];
  (ii) the scope needs three explicit clauses the memo leaves implicit
  (all components quantum free fields admitting *state-independent*
  QEIs, on a common background/worldline/sampler, in Hadamard states;
  classical components and non-minimally coupled scalars are outside);
  (iii) **one arithmetic claim is wrong**: the Dvali species scale at
  N = 10⁷² is Λ ≈ 1.2×10⁻⁸ eV, **not** ~10⁻¹⁷ eV (a GeV↔eV slip —
  10⁻¹⁷ is the value in GeV). The qualitative conclusion survives the
  correction (see §2).
- **Novelty: PARTIALLY KNOWN.** The summed bound is an immediate
  corollary of the published per-field QEIs, and in one literature
  corner (2D CFT) the summed form is effectively printed, via the
  central charge. The explicit anti-loophole corollary for
  exotic-matter engineering — "re-attributing a fixed total among
  components cannot inflate its QEI bound", applied to the Krasnikov
  tube with the species escape priced at N ≥ 1.06×10⁷² — was not found
  stated anywhere searched.
- **Gate verdict: UPLOAD-READY AFTER RESTATEMENT** (exact restated
  wording in §4).

---

## 1. Correctness — proof audit (done first)

### 1.1 The argument, re-derived

The memo's proof, stripped to its skeleton:

1. Per free field i, Hadamard state, worldline with sampler f = g²:
   ∫⟨Tᵢ(u,u)⟩ f dt ≥ −cᵢ·Φ[f], with the RHS state-independent
   (Fewster–Eveson, arXiv:gr-qc/9805024; Fewster–Teo,
   PRD 59, 104007 (1999); Fewster's general worldline QEI,
   arXiv:gr-qc/9910060; review arXiv:math-ph/0501073).
2. T_tot = Σᵢ Tᵢ as operators/expectations, so the smeared total is
   the sum of the smeared components (linearity of the integral and
   of expectation values — no assumption needed).
3. Summing N valid inequalities gives a valid inequality:
   ∫⟨T_tot(u,u)⟩ f dt ≥ −(Σᵢcᵢ)·Φ[f].
4. The RHS mentions only (field content, sampler, background). The
   required total is pinned separately, by G/8π of the fixed metric;
   it enters the *demand* side, never the bound. Hence no
   re-attribution of the demand among components can move the bound.

Steps 2–4 are elementary and correct. All the content — and all the
risk — is in step 1 and in what "decomposition" is allowed to mean.
Findings, in the order the task posed them:

### 1.2 (Task Q1) Is the per-field QEI state-independent and additive as needed?

**Mostly yes, with two qualifications.**

- *State-independence:* For free scalar (any mass), Dirac, Maxwell,
  Proca and Rarita–Schwinger fields, state-independent worldline
  QEIs over all Hadamard states are theorems (programme record A4,
  verified at P27-3; literature as cited above). Additivity needs
  nothing more: each inequality holds for *every* Hadamard state of
  field i, in particular for the marginal (reduced) state of field i
  in any joint state of the multi-field system — entanglement or
  classical correlation *between* components cannot break a bound
  that already quantifies over all states of each component. This
  closes a route the memo does not even list: cross-component
  entanglement buys nothing. Good.
- *Qualification A — non-minimal coupling:* the non-minimally
  coupled scalar (ξ ≠ 0) in curved spacetime admits only a
  *state-dependent* QEI (Fewster's review, arXiv:math-ph/0501073,
  notes exactly this exception). For such a component the memo's
  step 1 fails as stated. This is a genuine scope hole, not a
  counterexample to the tube conclusion (nobody's tube proposal
  rests on a non-minimal scalar), but the proof's quantifier "for
  one free field" is too broad and must be narrowed (§4).
- *Qualification B — absolute vs difference QEI:* in a general
  curved background the theorem-grade statement is a *difference*
  QEI: the bound controls ⟨T⟩_ω − ⟨T⟩_{ω₀} relative to a reference
  Hadamard state ω₀ (Fewster–Teo 1999; Fewster gr-qc/9910060 normal
  orders w.r.t. a reference state; the review's §3 makes the same
  point: in curved/compact spacetimes a constant negative density
  exists, so the bound is on the difference). Summing difference
  QEIs is still fine — the reference contributions sum too — but the
  honest statement is: B_tot bounds the total's excursion *below the
  summed reference (vacuum) value*, not the absolute total. For the
  tube application this is precisely the programme's own A5 /
  difference-QI caveat (P43-3a): the proof prices the pulse/absolute
  form as the programme's ledger does, and under Branch 2 the
  comparator changes in kind for reasons *outside* this proof. The
  proof itself is not damaged, but its statement must carry the
  "absolute form where an absolute QEI exists (flat space / short
  sampling); difference form otherwise" clause.

### 1.3 (Task Q2) Does summing preserve the SAME Φ[f] across fields?

**Not in general — this is the audit's main technical finding.**
In the Fewster–Eveson/Fewster–Teo form, the bound functional is
built from the field's own two-point/Hadamard structure: it depends
on the field's mass and spin, not only on (sampler, background).
E.g. the Fewster–Eveson scalar bound carries the mass-dependent
factor Q₃(u/m) (0 ≤ Q₃ ≤ 1, mass only tightens); the Maxwell bound
is 2× the scalar bound *for the same sampler in flat space*; a
massive field's functional is a different functional of g, not a
constant multiple of the massless one. So the literal factorisation
B_tot = (Σᵢcᵢ)·Φ[f] with one common Φ is exact only where it is
actually used in the programme's pricing:

- N *identical* fields (the species case): exact, Φ common, Σcᵢ = Nc.
- Flat-space massless species with the Ford–Roman/Fewster–Eveson
  sampler (scalar c = 1, Maxwell c = 2 in units of the scalar
  constant): exact up to the recorded constants (A4).

The *decomposition-independence conclusion* does not need the
factorisation: with per-field functionals Φᵢ[f] (each a function of
field i's identity, the common sampler, worldline and background
only), summing gives **B_tot = Σᵢ Φᵢ[f]**, still a function of
(field content, sampler, background) only, still with no reference
to attribution. The proof stands; its headline formula must be
restated in the summed-functional form, with the factored form
demoted to the identical-fields / flat-massless special case that
the tube pricing actually uses. Legitimacy of the *common*
sampler/worldline/background across components: yes — the
components coexist in one spacetime, are sampled by one observer
along one worldline with one f; nothing in the per-field theorems
forbids applying them simultaneously on a shared background. The
one thing the shared-background step silently assumes is that the
background is *given* (the fixed tube metric), i.e. semiclassical
self-consistency/backreaction is outside the statement — the
programme's A7, already on record; the bound is a necessary
condition on any semiclassical realisation, which is all the
ledger needs.

### 1.4 (Task Q3) The three counterexample routes, attacked independently

- **(a) A component below its own QEI floor.** Excluded by theorem,
  not by hypothesis-stacking: for an actual free quantum field in a
  Hadamard state the floor *cannot* be crossed — that is what the
  QEI says. A "component" that sits below the floor is by
  construction not the expectation value of such a field. The memo
  is right that this route is closed, and the correct way to say it
  is: the proof constrains *realisations by the stated field
  content*, and route (a) is a change of subject, not a
  counterexample. ✔ closed.
- **(b) A decomposition that changes Φ[f].** Φ (resp. each Φᵢ) is
  fixed by sampler, worldline and background geometry. The total is
  fixed ⇒ (semiclassical) geometry fixed ⇒ background fixed. A
  decomposition is a bookkeeping split of one fixed total on one
  fixed background; it has no lever on f, the worldline, or the
  metric. One attempted lever deserves naming: could a component's
  *own* contribution to curvature make "its" background different
  from the total's? No — there is one spacetime; each field's QEI
  is evaluated on the total geometry, which the fixed total pins.
  ✔ closed.
- **(c) Adding fields.** Exactly the species case, and the pricing
  is §2. Adding a field changes the field content, i.e. changes the
  claim's fixed quantity, and the gain is exactly additive (≤ N·max
  cᵢ; exactly N× for identical fields — A4's theorem-grade
  linearity). ✔ closed, priced.

### 1.5 Hidden assumptions found (the task's specific probes)

1. **Uncoupled free fields in a shared Hadamard framework — YES,
   silently required, and it matters for wording, not for the
   verdict.** If components are coupled to each other, "the QEI of
   component i" is not in general a theorem about Tᵢ separately
   (the interacting theory's total T still may obey a QEI where
   proven, but the *decomposition* statement is then about the
   total of an interacting theory, which is the memo's named
   reopening, correctly flagged). Within the free scope, mutual
   coupling = interaction = outside. The restated claim must say
   "mutually non-interacting (free) fields" explicitly.
2. **Classical required total vs quantum components — sound, with
   the direction of logic stated.** The tube's total is a classical
   G/8π profile (a *demand*). The proof does not apply QEIs to the
   classical profile directly; it proves a necessary condition:
   *if* that total is realised as ⟨T_tot⟩ of the stated field
   content in Hadamard states on that background, *then* its
   smeared value respects B_tot. A demand violating B_tot is
   therefore unrealisable by that content. That inference is valid.
   What it does **not** cover: a decomposition with a *classical*
   component (e.g. a classical field or phenomenological fluid
   carrying part of the total) — classical components obey no QEI,
   and the proof says nothing about them. But that is no loophole
   for the tube: a classical component carrying sustained negative
   ⟨T(u,u)⟩ is itself the exotic matter whose existence is in
   question, and the programme prices classical totals by the
   classical EC ledgers (N4/NEC lines), not by this bound. Scope
   clause required: *every* component is a free quantum field.
3. **State-independent-QEI fields only** (non-minimal scalar
   exception, §1.2A).
4. **Absolute vs difference form** (§1.2B).

None of these narrows the *tube* application: the ledger's use is
N identical free fields / standard species on the tube background
in the programme's pulse-bound pricing, where the factored form
and the state-independent QEIs are exactly the theorem-grade ones.

**Correctness verdict: the proof STANDS WITH SCOPE RESTATEMENT**
(gate language: REPRODUCED WITH RESTATEMENT). No step fails; the
generality of the headline formula and three implicit scope clauses
must be made explicit, and one number (§2) corrected.

---

## 2. Arithmetic — independently verified (`gate6/wd_arith.py`)

| Claim | My computation | Verdict |
|---|---|---|
| N ≥ 1.06×10⁷² (D = 1 m, L = ε) | required/legal = 1.06×10⁷² (P22-2 ledger, taken as given per claim statement); bound scales exactly ∝ N (A4), so N_min = ratio = 1.06×10⁷² | ✔ |
| N ≥ 1.06×10⁷³ at L = a | ratio ×10 (E_legal ∝ 1/L, ε→a is ×10 at a = 1 m, ε = 0.1 m) ⇒ 1.06×10⁷³ | ✔ |
| Cap ℓ²/l_P² ≈ 3.8×10⁶⁹ at ℓ = 1 m | 1/(1.616×10⁻³⁵)² = **3.83×10⁶⁹** (CODATA l_P = 1.616255×10⁻³⁵ m: 3.828×10⁶⁹) | ✔ |
| Cap ≈ 3.8×10⁶⁷ at ℓ = ε = 0.1 m | 0.01/(1.616×10⁻³⁵)² = **3.83×10⁶⁷** | ✔ |
| Shortfall ≈ 2.4 orders (ℓ = 1 m) | log₁₀(1.06×10⁷² / 3.8×10⁶⁹) = **2.45** | ✔ |
| Shortfall ≈ 4.4 orders (ℓ = 0.1 m) | log₁₀(1.06×10⁷² / 3.8×10⁶⁷) = **4.45** | ✔ |
| Species scale Λ ~ M_P/√N ~ 10⁻¹⁷ eV at N = 10⁷² | M_P = 1.22×10²⁸ eV; √N = 10³⁶; Λ = **1.22×10⁻⁸ eV** (at N = 1.06×10⁷²: 1.19×10⁻⁸ eV) | ✘ **WRONG by 9 orders** |

The Λ error is a units slip: M_P/√N = 1.22×10⁻¹⁷ **GeV**, transcribed
as eV. **Downstream effect — the qualitative claim survives, and in
length terms is essentially unchanged in kind:** Λ ≈ 1.2×10⁻⁸ eV
corresponds to a cutoff length ħc/Λ ≈ 197 eV·nm / 1.2×10⁻⁸ eV ≈
**16 m** — i.e. at the required species count the semiclassical
frame (A7) would break down at a scale *larger than the 1 m tube
itself*. The memo's phrasing "a gravitational cutoff below every
measured scale" should be restated (§4): the corrected Λ is an
energy ~10⁻⁸ eV, equivalently a breakdown length ~10 m — still a
dissolution of the frame the bound lives in, for a metre-scale
construction. The caps remain labelled heuristic, not theorem —
the memo and checkpoint label them so, correctly (A4).

---

## 3. Novelty

### 3.1 Search log (queries verbatim; sources: arXiv, INSPIRE-HEP,
Semantic Scholar, general web)

1. `quantum energy inequality multiple fields sum of fields bound species number of fields`
2. `Fewster quantum energy inequalities review multiple fields total stress energy tensor bound`
3. `"quantum energy inequality" "number of fields" OR "species" negative energy bound scaling`
4. `Ford Roman quantum inequalities many fields negative energy density bound proportional number species`
5. `"quantum inequality" bound "sum" fields stress-energy tensor total Fewster Eveson Teo`
6. `Krasnikov tube quantum inequality many fields species negative energy Everett Roman`
7. `splitting negative energy multiple fields loophole quantum inequalities wormhole exotic matter`
8. `Kontou Olum quantum energy conditions review number of fields bound negative energy`
9. `site:inspirehep.net quantum energy inequality fields bound`
10. `site:semanticscholar.org quantum energy inequality multiple fields stress energy`
11. `two dimensional quantum energy inequality bound central charge Flanagan proportional c fields`

Plus full-text reading of Fewster's review (arXiv:math-ph/0501073)
§3, and the Fewster–Eveson abstract/text (arXiv:gr-qc/9805024).

### 3.2 What the literature actually states

- **QEIs are standardly stated per theory/per field.** Ford–Roman
  (arXiv:gr-qc/9607003): bounds derived field by field (scalar,
  then electromagnetic at its own constant, massive scalar). Fewster–
  Eveson (gr-qc/9805024): "for the free real scalar field". Fewster–
  Teo (PRD 59, 104007): scalar in static spacetimes. Fewster–Roman
  (arXiv:gr-qc/0209036): scalar. Fewster's review
  (math-ph/0501073): the general argument is run for *a* theory's
  stress tensor T_ab satisfying a classical sum-of-squares form —
  i.e. within one theory, T is already whatever total that theory
  has; no statement about re-splitting a fixed total across fields
  or about attribution.
- **The summed form IS effectively printed in one corner:** for
  2D conformal field theory, Fewster's QEI bound depends on the
  theory's **central charge(s)** (Fewster, "Quantum energy
  inequalities in two-dimensional conformal field theory", Rev.
  Math. Phys. 17 (2005) 577; cf. Flanagan's optimal 2D bound,
  whose constant is ∝ c). For a multi-field CFT, c = Σᵢ cᵢ — the
  bound on the *total* stress tensor is literally the sum over
  components. So "bound of a sum = sum of bounds, via an additive
  field-content charge" is in print in 2D CFT language.
- **Species/N-scaling** of negative-energy bounds is folklore in
  the exotic-spacetime literature in the weak sense that everyone
  prices one field (or the SM content) and notes more fields help
  linearly; the Dvali species scale Λ ~ M_P/√N is standard
  (Dvali, arXiv:0706.2050 [hep-th]). No source found states a
  *required* N for a Krasnikov tube, nor compares it to ℓ²/l_P²
  caps. Everett–Roman (arXiv:gr-qc/9702049) price the tube with
  the single-field QI and do not discuss decomposition/species
  escapes. Fewster–Roman (arXiv:gr-qc/0510079) close the
  "arbitrarily small exotic matter" wormhole route with a QI on
  the total — the closest anti-loophole *style* of result — but
  the loophole there is geometric (small total amount), not
  decompositional, and no component-blindness statement is made.
- **No source found** — in arXiv full texts/reviews, INSPIRE,
  Semantic Scholar, or web — states the anti-loophole corollary:
  that for a *fixed* total ⟨T_μνu^μu^ν⟩ the applicable QEI bound
  is invariant under re-attribution of the total among components,
  with adding fields (species) as the only escape. The step is a
  one-line summation of published inequalities; the literature
  treats it as too immediate to state, and the exotic-matter
  literature never needed it stated because mixture attempts were
  aimed at classical constraints (the programme's Phase-33
  context), not at the sampling bound.

### 3.3 Novelty verdict

**PARTIALLY KNOWN.** Known part, cited: the per-field QEIs and
their trivial summability (Ford–Roman gr-qc/9607003; Fewster–
Eveson gr-qc/9805024; Fewster–Teo PRD 59, 104007 (1999)), and the
additive field-content dependence of the total bound in print in
2D CFT via the central charge (Fewster, Rev. Math. Phys. 17
(2005) 577). Not found in print: the decomposition-independence
corollary stated as an anti-loophole result for a fixed,
metric-pinned total, and its Krasnikov-tube species pricing.

**The novel part, in one quotable sentence:** "Stated as an
anti-loophole corollary for exotic-matter engineering — for a
fixed total stress-energy pinned by the metric, the QEI bound
cannot be inflated by re-attributing the total among free-field
components, so a mixture buys only the species factor, which for
the 1 m Krasnikov tube costs N ≥ 1.06×10⁷² fields — the
component-blindness statement and its tube pricing do not appear
in the QEI literature, where the summed bound is used (and, in 2D
CFT, printed via the central charge) but never isolated as the
closure of the splitting loophole."

---

## 4. EXACT restated wording (the form in which the claim survives)

> **G6-4 (restated).** Let the total stress-energy be realised on a
> fixed background, along a fixed worldline with a fixed sampler
> f = g², by a fixed content of mutually non-interacting (free)
> quantum fields, each admitting a state-independent worldline QEI
> over Hadamard states (scalar, Dirac, Maxwell, Proca class;
> non-minimally coupled scalars, classical components and
> interacting components are outside this statement). Then the
> smeared total obeys ∫⟨T_tot(u,u)⟩ f dt ≥ −B_tot with
> **B_tot = Σᵢ Φᵢ[f]**, where each Φᵢ depends only on field i's
> identity, the sampler, the worldline and the background — never
> on how the fixed total is attributed among the components. Where
> the per-field bounds share a common functional up to constants
> (identical fields; flat-space massless species), B_tot factors
> as (Σᵢcᵢ)·Φ[f]. Hence a decomposition of a fixed total cannot
> inflate its applicable bound; the only enlargement is adding
> fields, worth exactly N× for N identical fields. For the 1 m
> Krasnikov tube that escape needs **N ≥ 1.06×10⁷²** (L = ε;
> 1.06×10⁷³ at L = a), which is **2.4 orders** beyond the heuristic
> cap ℓ²/l_P² = 3.8×10⁶⁹ at ℓ = 1 m and **4.4 orders** beyond
> 3.8×10⁶⁷ at ℓ = ε = 0.1 m (caps heuristic, not theorem), and at
> N = 10⁷² the Dvali species scale is **Λ ~ M_P/√N ≈ 1.2×10⁻⁸ eV**
> (cutoff length ħc/Λ ≈ 16 m), so the escape dissolves the
> semiclassical frame the bound lives in. In curved backgrounds
> the statement holds in difference-QEI form (excursion below the
> summed reference-state value). Reopening condition (unchanged):
> a theorem-grade interacting-field QEI in 4D whose total bound
> is decomposition-dependent.

## 5. Gate verdict

**UPLOAD-READY AFTER RESTATEMENT** — correctness REPRODUCED WITH
RESTATEMENT (proof sound; factored formula demoted to its valid
special case; three scope clauses made explicit; species-scale
number corrected from 10⁻¹⁷ eV to ≈1.2×10⁻⁸ eV, qualitative
conclusion intact), novelty PARTIALLY KNOWN (summed bound an
explicit corollary of published per-field QEIs and printed in 2D
CFT via c = Σcᵢ; the anti-loophole corollary + tube species
pricing not found in print).

### Key citations
- Ford & Roman, arXiv:gr-qc/9607003 (per-field QIs, scalar/EM/massive).
- Fewster & Eveson, arXiv:gr-qc/9805024 (arbitrary-sampler QEI, scalar).
- Fewster & Teo, Phys. Rev. D 59, 104007 (1999) (static spacetimes; difference form).
- Fewster, arXiv:gr-qc/9910060 (general worldline QEI, reference-state form).
- Fewster, arXiv:math-ph/0501073 (review; non-minimal-coupling state-dependent exception).
- Fewster, Rev. Math. Phys. 17 (2005) 577 (2D CFT QEI ∝ central charge — summed form in print).
- Fewster & Roman, arXiv:gr-qc/0209036; arXiv:gr-qc/0510079 (QI constraints on totals for wormholes).
- Everett & Roman, arXiv:gr-qc/9702049 (Krasnikov tube QI pricing, single-field; no decomposition discussion).
- Dvali, arXiv:0706.2050 [hep-th] (species scale Λ ~ M_P/√N).
