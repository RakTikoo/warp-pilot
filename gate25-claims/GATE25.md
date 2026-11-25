# GATE-25 — ADJUDICATION OF THE SPINOR CLAIM SET
# (Phase 253 P253-1 + Phase 257 Legs 1–3)

Date: 2026-11-24. Adversarial re-judgement, not a phase. Frame
of record: Phase 166 pin, Gate-19-corrected tensor, venv python.
Method: Gate-25 re-derived every deciding number by a code path
written from scratch for this gate (`gate25/work/g25_verify.py`
→ `gate25/work/g25_verify_results.json`): ψ(x) and ψ̄(x) built
as explicit field functions from the stored mode lists, derivatives
taken analytically mode-by-mode inside the field function, T_ab
assembled directly from the symmetrised formula with the −g_ab·L
term computed honestly (not assumed zero). No driver from
phase253/work/, phase257/work/, phase250/work/ or phase235/ was
imported, copied, or executed; only stored data JSONs were read.
The gate also attacked the registrations (integrity, scope,
DOF pricing), the classical/quantum reading, the Phase 72
comparison, and graded novelty against the literature
(`gate25/work/g25_literature.md`). Independence limits, on the
face: T_req itself is the stored Phase 250 site row (control-exact
against Phase 235 under earlier gates) and was not re-derived
from the Alcubierre metric; R_diff was not recomputed by the
phase or by this gate (§4); Phase 72's p721 memo was read via
Phase 253's registration account and CHECKPOINT72.md, not
re-derived (it carries no deciding number in this claim set).

## VERDICTS

- **G25-A: SURVIVES IN RESTATED WORDING** (restated wording in
  §2). Every deciding number reproduces to machine precision
  through the gate's independent path, single-mode positivity
  and the interference origin included. The restatement adds
  the fences the claim always carried but its compressed form
  drops: pointwise/tangent-frame, the c-number pose (equivalently
  the one-particle expectation), and the literature position —
  classical Dirac NEC violation in *other* settings is
  published, and the claim's mechanism/setting distinction
  must travel with it.
- **G25-B: SURVIVES IN RESTATED WORDING** (restated wording in
  §3). The six-mode match reproduces independently at
  R = 1.767×10⁻¹⁶, complex eigenvalue pair included. The
  restatement moves the claim's weight off the residual's
  smallness — with 41 effective real parameters against 10
  tensor components the exact fit is a parametrisation fact —
  and onto the content that survives pricing: the family's
  reachable set contains Type-IV tensors at all, inside the
  on-shell positive-frequency family. No novelty is granted
  (§5), though the literature affirmatively states the
  opposite state of knowledge.
- **G25-C: SURVIVES IN RESTATED WORDING** (restated wording in
  §4). The negative companion is accurate in all three parts.
  The restatement marks the QI line as a definitional identity
  (R_diff prices the target tensor, not its supplier), not a
  computed invariance, and records a disclosed procedural
  deviation: Leg 3 ran on Leg 2's remainder read although the
  registration gated it on the registered sum improving. The
  deviation does not touch this claim's content.
- **Novelty: NONE granted** (§5). For G25-A the bare phenomenon
  is published prior art by other mechanisms; the specific
  mechanism/setting was not found. For G25-B nothing was
  found, and the closest literature states no classical
  Type-IV field is known — graded "not found in our search",
  with the search's limits stated, per the claim gate.

---

## §1. Independent re-derivation — what reproduces

**Convention, resolved first.** Both registrations write
T_ab = (i/4)[ψ̄γ_(a D_b)ψ − (D_(aψ̄)γ_b)ψ] − g_ab·L. Read with
the averaged symmetrisation γ_(a D_b) = (γ_aD_b + γ_bD_a)/2,
that formula yields exactly **half** the tensor the phases
report (gate's first pass: T(k*,k*) = −5.439245950801301,
ρ = 1.1201760181156213 — the claimed values ÷ 2, exactly).
Read with the unnormalised sum under the (i/4) — equivalently
(i/2) with averaged symmetrisation, which is the standard
canonical Dirac stress-energy tensor — every number below
matches to machine precision. The tensor that matches T_req
is therefore the textbook tensor, and the phases' numbers are
in the standard convention; only the registrations' notation
is ambiguous. One clarifying line is owed in any future
registration quoting the formula. No number in either phase
changes.

**Phase 253 deciding configuration** (m = 1, three modes, from
p2531_results.json tierB_best): all modes on shell (stored E
matches √(|p|²+1) to all digits); Dirac residuals
[9.8×10⁻¹⁶, 4.3×10⁻¹⁵, 3.7×10⁻¹⁶]; u†u − 2E ≤ 1.8×10⁻¹⁵;
all p⁰ > 0; Σ|c|² = 1.0000000000000002. The gate's field-
function tensor gives:

| quantity | gate | claimed |
|---|---|---|
| T(k*,k*) | −10.878491901602603 | −10.878491901602604 |
| ρ = T₀₀ | +2.2403520362312404 | +2.2403520362312377 |
| ψ†ψ(0) | 2.1935720040297464 | 2.1935720040297464 (stored) |
| L at the point | ~10⁻¹⁵–10⁻¹⁹ (computed, not assumed) | 0 on shell |

k*'s spatial direction in the stored p2502 site row is
identical to the registration's n̂ (max diff 0.0). Single
modes alone (renormalised): T(k*,k*) = **+1.3279, +259.9833,
+26.6018 — all ≥ 0**. The negative value is purely the cross
terms, as claimed.

**Phase 257 N = 6 best fit** (p257_bestfit.json): all six
modes on shell, residuals 1.7×10⁻¹⁶ … 2.8×10⁻¹⁵,
Σ|c|² = 0.007884090763433323 (the leg-2 exact value, identical).
The gate's tensor against the stored T_req (p2502 site
worst_r12.84_b1.1; gate's |T_req|_F = 2.3978336134611576×10⁻³,
as registered):

| quantity | gate | claimed |
|---|---|---|
| R = \|T − T_req\|_F | 1.767×10⁻¹⁶ | 1.7674932537562168×10⁻¹⁶ |
| mixed eigenvalues | 0.000675506126 ± 0.000820127813 i, 0.000113043770, 0.001041942748 | 0.000676 ± 0.000820 i, 0.000113, 0.001042 |
| ρ | −9.800905387229392×10⁻⁵ | ρ_req = −9.800905387216327×10⁻⁵ |
| ρ_unit = ρ/Σ\|c\|² | −0.012431243730331365 | −0.012431243730330888 (leg-2 exact) |
| T(k*,k*) | −0.003801760529158496 | −0.0038017605291582623 |

**Type-scan spot check.** The gate's own spinor construction
(u from √(E+m)χ and (σ·p)χ/√(E+m), χ uniform on the ℂ²
sphere), 60 random superpositions N ∈ {2..5}: **13/60 (21.7%)
have a complex mixed-eigenvalue pair**, vs the phase's 40/300
(13.3%). Same order; the excess is ~1.9σ at n = 60 and the
phase's draw distribution is not stored, so this is a
consistency spot check, not an exact replication. It confirms
the qualitative content: Type-IV members are a generic,
non-negligible fraction of the family, not a fitted rarity.

**Patch spot check (Leg 2).** At the stored fitted scale, the
gate's field function over x ∈ [−π,π]³: NEC min −0.01523
(coarse grid) → −0.02021 (denser random sampling), converging
toward the phase's dense-read −0.02231455; max Frobenius
departure from T_req on the coarse grid 0.1128 (≈50× |T_req|_F);
ρ range [−9.80×10⁻⁵, +0.09841] vs the phase's +0.09209 upper
end (grid-dependent, same order). The point-match character
is confirmed independently.

**DOF count (attack line 4, arithmetic).** Registered family,
per mode: momentum (3) + spin χ on the unit ℂ² sphere modulo
phase (2) + coefficient c ∈ ℂ (2) = 7; at N = 6: 42, minus the
overall phase = **41 effective real parameters** (the overall
real scale counts; the target's norm fixes it). Target: 10
independent components, +1 contraction condition in the
constrained fit = 11 conditions. The fit is over-parametrised
≈4×. Priced in §3.

---

## §2. G25-A — the sign break: SURVIVES IN RESTATED WORDING

### The attacks, and what they found

**(a) Health / on-shell audit (attack line 2).** The modes are
genuinely on shell, positive-frequency, u†u = 2E, m = 1 ≥ 0,
correct-sign kinetic term — the registered health conditions
H1–H3 of p2531_registration.md, all verified from the stored
artefacts (§1). "Healthy" is earned **under the record's own
registered usage**: it names the field's action-level health
(sign of kinetic term, m² ≥ 0, on shell), not satisfaction of
the energy conditions — which is precisely what is under test —
and not global normalisability on the background, which both
phases fence as untested. Against Phase 72: its spinor closure
rested on (i) the published Einstein–Dirac *solutions* failing
the full EC set / normalisability bars and (ii) a domain
obstruction of the programme's frozen-shape throat system;
its own audit exhibits on-shell Dirac NEC violation (BSKR
S-A). Neither ground is a sign identity, so Phase 253's scope
correction — Phase 72 closes spinor-supported *throats* at its
bars, not spinor sourcing generally — is accurate and stands.

**(b) The classical/quantum confinement (attack line 3).**
Phase 253 §3 claims the classical/quantum dependence is
confined to two steps the verdict does not take: negative-
frequency modes (excluded by registration) and Grassmann
point-values (no sign until a state is chosen). The gate
tested this. It holds, with one sharpening. The c-number
configuration with Σ|c|² = 1 is, in the quantised theory,
exactly a **one-particle superposition state**, and the
normal-ordered stress tensor's one-particle expectation
⟨:T_ab(x):⟩ contains the same cross terms c_i*c_j ū_iΓu_j
e^{i(p_i−p_j)·x} — normal ordering removes the vacuum
contribution, not one-particle interference — so at x = 0 the
quantum expectation equals the classical bilinear the phases
computed, sign included. The interference therefore survives
quantisation *in the one-particle sector*, which is also
exactly the sector where "positive-frequency only" is
automatic. What does not follow, and what neither phase
claims: that this expectation may be used as a classical
source in Einstein's equations (a semiclassical sourcing
assumption, separate from the tensor's algebra), and any
"classical field configuration" phrasing — a Grassmann-valued
classical field has no c-number point values, so the honest
label is the one Phase 253 used (c-number pose, equivalently
one-particle expectation). Phase 257's checkpoint language
("a healthy classical field sector", "a concrete classical
field configuration") outruns that label; the restatement
corrects it. Pointwise negativity conflicts with no quantum
inequality (QEIs bound smeared averages), as Phase 253 fenced.

**(c) Pointwise scope.** The claim is a statement at the site
point (x = 0 of the superposition, where the phases align).
ρ > 0 is likewise pointwise. The claim as put to this gate
says nothing stronger, and the restatement keeps it so.

### Restated G25-A (the quotable form)

*In the classical c-number Dirac pose — equivalently, as the
one-particle expectation of the normal-ordered stress tensor —
a superposition of three on-shell, positive-frequency,
flat-space plane waves (m = 1, Σ|c|² = 1, health conditions
H1–H3) has T(k*,k*) = −10.8785 along the Phase 235 drive's
deciding null direction at its β = 1.1 worst site, with local
density ρ = +2.2404 at the same point. Each constituent mode
separately has T(k*,k*) ≥ 0 (gate: +1.33, +259.98, +26.60);
the negativity is a multi-mode interference effect of the
on-shell Hermitian form N = A∘C, C_ij = ½(f_i + f_j)
indefinite. Phase 31's sign identity therefore does not
extend to spinor superpositions in this pose. The statement
is pointwise and tangent-frame: no global on-background
existence, normalisability, or sourcing is claimed. Classical
Dirac NEC violation in other settings is published prior art
(§5); the mechanism and setting here — flat on-shell plane
waves, single-mode positivity, ρ > 0 retained — were not
found in the literature searched, and any quotation must
carry that distinction.*

---

## §3. G25-B — the full tensor match: SURVIVES IN RESTATED WORDING

### The attacks, and what they found

**(a) Registration integrity (attack line 4).** Both
registrations were written before any deciding computation,
with verdict forms and bars fixed verbatim (Phase 253:
IDENTITY EXTENDS / SPINORS BREAK / CANNOT BE POSED; Phase
257: R_constr ≤ 1e-9 for FULL MATCH). The N-dial
N ∈ {3, 4, 6, 8, 12} with ≥ 8 restarts per N was registered
in advance — N = 6 was not invented after the fact, and
"best of 8 restarts" is selection inside the registered
protocol against a target (T_req) stored before the phase
ran. No goalpost moved. Two procedural notes, neither moving
a number: the symmetrisation-notation ambiguity (§1), and
the Leg-3 gating deviation (§4).

**(b) Fitting-to-the-target, priced.** With 41 effective real
parameters against 10 components + 1 constraint (§1), a
smooth family's image generically covers a neighbourhood of
any reachable target; the exact residual 1.77×10⁻¹⁶ is what
float64 least squares delivers once the target is in the
image, and **carries no evidential weight by itself**. What
carries the weight, and survives pricing: (i) the target is
*not* in the image of any real-spectrum family (the C3 floor,
8.201×10⁻⁴, bounds all of those), so reachability turns
entirely on the family escaping Type-I confinement; (ii) the
escape is structural, not fitted — cross terms carry
transition currents ū_iγu_j (i ≠ j), which are complex and
subject to no Fierz causality constraint, so the single-mode
argument (T_ab = p_(a j_b), both factors future causal) has
no superposition analogue; (iii) the scan shows Type-IV
members are generic in the family (40/300; gate 13/60), not a
measure-zero corner the fit hunted down; (iv) the stall
pattern is informative in the other direction — N = 3 and
N = 4 stall at 3.13× / 1.84× the floor, so the reachable set
genuinely grows with mode count and the N = 6 closure is not
a triviality of the parametrisation at every N. The claim's
discovery-grade content is the type-confinement failure;
the match is its corollary at the drive's site.

**(c) The "one spinor" reframe.** ψ = Σψ_i is formally a
single spinor field, so a referee may reframe (ii) as "the
general classical Dirac field was never classified" rather
than "superpositions break a theorem". No theorem confining
the classical Dirac tensor to Type I was found in the
literature (§5) — the Type-I impression rests on
symmetry-reduced Einstein–Dirac ansätze (diagonal T_ab by
symmetry) and single-mode Fierz intuition — so the reframe
costs the claim nothing: under either framing, an on-shell
classical Dirac field whose stress tensor is Type IV is
exhibited, against a literature that states none is known.
The on-shell condition is load-bearing here and is verified
(§1): with freely prescribed ψ, ∂ψ point data (the curved-
background mechanism of §5's Weinbaum result) Type IV would
be near-trivial; this configuration's data all come from
on-shell modes.

### Restated G25-B (the quotable form)

*Dirac superpositions in the c-number / one-particle pose are
not confined to real-spectrum stress tensors: their cross
terms carry complex transition currents ū_iγu_j that no
causality constraint binds, and Type-IV members are generic
in the registered family (40/300 draws; gate spot check
13/60). Consequently a six-mode on-shell positive-frequency
superposition reproduces T_req at the drive's β = 1.1 worst
site to Frobenius residual 1.77×10⁻¹⁶, mixed eigenvalues
(0.000676 ± 0.000820 i, 0.000113, 0.001042) included —
independently re-derived by this gate. The residual's
smallness is a parametrisation fact (41 effective real
parameters vs 10 components + 1 constraint) and carries no
weight; the content is that the family's reachable set
includes the Type-IV target at all. Phase 244's named exit —
a healthy sector producing non-Type-I stress — is met at
pointwise tangent-frame scope, by the sector that was in the
library all along. No global field, normalisability, or
backreaction is claimed. No classical Type-IV matter field
was found in the literature searched (§5, limits stated); no
first/record claim is granted.*

---

## §4. G25-C — the negative companion: SURVIVES IN RESTATED WORDING

### The attacks, and what they found

**(a) Negative density of the matching configuration.**
Gate-reproduced exactly: ρ_unit = −0.012431243730331365
(phase's leg-2 exact −0.012431243730330888). The two spinor
properties — Phase 253's positive-density sign configuration
and Phase 257's tensor-matching configuration — are carried
by different configurations; no configuration in either phase
carries both. Confirmed, and it is the honest centre of this
claim: the interference that buys the tensor spends the
density.

**(b) Point match.** Gate-confirmed at order (§1): the
field's stress departs from T_req by up to ~50× |T_req|_F
over the patch and the patch NEC minimum (≈ −0.0223, phase's
dense read; gate −0.0202 at lower sampling density,
converging) is 5.9× deeper than the site deficit it covers.
The global-existence cost is not retired; both phases said
so, and the gate's numbers agree.

**(c) The QI line.** R_diff = 2852.41 appears identically in
the stored leg-3 JSON before and after sourcing, with the
reason stated there: the Phase 66 difference-QEI prices the
total stress T_req sampled along the worldline, and sourcing
changes who supplies T_req, not T_req. The gate verifies
this is an **identity by construction**, not a computed
invariance — neither the phase (sketch grade, as registered)
nor this gate recomputed R_diff from the QEI form. Quoted as
"unchanged identically" it is correct; quoted as a measured
robustness it would overstate. The restatement fixes the
label. The companion budget statement is the same kind: a
shell-wide realisation would carry exactly the drive's
−2.5903 by definition, and no shell-wide field was
constructed.

**(d) The Leg-3 gating deviation (procedural, on the face).**
The registration gates Leg 3 on "Leg 2 improves the net
position". Leg 2's registered verdict on the registered sum
(T_req + s²T_Dirac) was NET POSITION WORSE OR EQUAL — with
the presupposition failure disclosed on its face (under a
full match the sum is 2·T_req by construction). Leg 3
nevertheless ran, gated on the sourcing-semantics remainder
read (T_req − s²T_Dirac = 0 at float64 class), with the
choice disclosed on both memos' faces. This is a deviation
from the registration's letter, made openly in-phase. It
does not affect G25-C: the QI/budget content prices T_req
under either framing, as Leg 2's memo itself notes. The gate
records the deviation because the registration's gate
condition was reinterpreted mid-phase; future registrations
should write the remainder-read branch into the gate
condition in advance when a full match is a registered
possibility.

**(e) Sampler note (record hygiene, no restatement).** Leg 2's
all-boost WEC read of T_req (−0.188) differs from the record's
restricted-observer margins read (−0.0362103); the phase
disclosed this and kept within-phase comparisons on one
sampler. G25-C quotes no WEC number, so nothing here
restates — but the record now carries two sampler-dependent
WEC values for the same tensor, and any future quotation of
T_req's WEC margin must name its sampler.

### Restated G25-C (the quotable form)

*The tensor-matching configuration does not inherit the sign
configuration's positive density (ρ_unit = −0.012431,
gate-reproduced); no configuration in Phases 253/257 carries
both properties. The match is a point match: over any
neighbourhood the field's stress departs from T_req (patch
NEC minimum ≈ −0.0223 at the fitted scale), so the global
on-background existence question remains the open cost. The
QI price is unchanged — R_diff 2852.41 → 2852.41 — by
construction: R_diff prices the target tensor, not its
supplier, so this is a definitional identity, not a computed
invariance. The two algebraic legs of the drive's sourcing
obstruction (sign, G25-A; type, G25-B) are retired at
pointwise scope; the two size legs (budget ≈ −2.5903, QI
≈ 2852×) stand exactly as Phase 235/244 left them.*

---

## §5. Novelty position

**None granted for either claim.** Full search record:
`gate25/work/g25_literature.md` (12 query families; full text
read for the four deciding sources).

**G25-A.** The bare phenomenon — a classical Dirac field
violating pointwise energy conditions — is published prior
art: Kontou & Sanders, CQG 37 (2020) 193001 (arXiv:2003.01815)
record the classical Dirac T_00 as unbounded below and the
WEC violation as "often stated"; Tóth (arXiv:1509.02878,
2015) treats classical-Dirac NEC failure as well known; and
Weinbaum, "Obstructions to traversable wormholes in
Einstein-Dirac theory," Phys. Rev. D (DOI 10.1103/g89c-gqyf),
§III C is titled "Dirac Fields Can Violate the Pointwise and
Averaged Null Energy Conditions" for classical
positive-frequency fields. But the mechanisms are different,
in one case opposite: Weinbaum's violators live on a curved
wormhole background where a *single* stationary mode already
violates (spinor and derivative data at a point are freely
specifiable there) and no ρ > 0 statement is made; the
textbook unboundedness runs through the unrestricted field
and delivers ρ < 0; the flat-space superposition results
(Vollick, arXiv:gr-qc/9806064; Yu & Shu, Phys. Lett. B 570
(2003) 123) are quantum expectations about ρ < 0. The
programme's configuration — flat tangent space, on-shell
plane waves only, every single mode T(k,k) ≥ 0, ρ > 0
retained, negativity purely from the interference form
A∘C — was **not found** and does not follow trivially from
the textbook argument. Not granted: any novelty for
"spinors violate NEC". Carried with the claim, per §2: the
mode/setting distinction (his "single modes violate" vs this
record's "single modes ≥ 0" differ because "mode" means a
curved stationary spinor with free derivative data there, a
flat on-shell plane wave here).

**G25-B.** Nothing found, and the closest literature
affirmatively asserts the opposite state of knowledge:
Martín-Moruno & Visser (arXiv:2102.13551, 2021), §2.2.4 —
"There are no known classical matter fields that lead to a
type IV stress-energy tensor"; Maeda et al.
(arXiv:2001.11335) repeat that no classical Type-IV field is
known; Type IV was previously assigned to renormalised
quantum expectation values only (Unruh state: Roman 1986;
Abdolrahimi–Page–Tzounis). No theorem confining the classical
Dirac tensor to Type I was found either — the gap is a
literature gap, not a contradicted theorem (§3(c)). Graded,
per the claim gate: **not found in our search**, with these
limits — 12 query families over web search; Hawking & Ellis
(1973) and Wald monograph treatments were not opened, so a
textbook assertion in a monograph cannot be fully excluded;
no systematic INSPIRE-HEP subject search was possible with
these tools, and a post-2021 classical Type-IV example
cannot be excluded; Weinbaum was read via an arXiv mirror
whose displayed metadata looked corrupted — cite the PRD DOI
(10.1103/g89c-gqyf) and verify before any external use. An
INSPIRE recheck is owed before any external wording stronger
than "not found in our search". No "first", "unique", or
"record" wording is granted or implied for any claim in this
set.

## §6. What this gate leaves standing

The drive's sourcing obstruction, as Phase 235/244 left it,
had four legs. After this gate: the **sign** leg and the
**type** leg are retired at pointwise tangent-frame scope, in
restated wording, on independently re-derived numbers. The
**health/global-existence** leg stands open and priced (point
match; patch NEC −0.0223; no on-background field). The
**budget/QI** legs stand untouched and were always the larger
numbers (budget ≈ 2.21–2.59; R_diff ≈ 2852). Nothing in this
claim set is a front pass, a drive, or new physics claimed
beyond the tensor algebra stated; the FTL verdict of both
phases — NO — is unaffected.

## Files

- `gate25/work/g25_verify.py` + `g25_verify_results.json` —
  the gate's independent re-derivation (field-function path;
  both symmetrisation conventions recorded).
- `gate25/work/g25_literature.md` — the novelty search record.
- No ledger append, no launches, no external contact.
  Nothing outside `gate25/` was edited.
