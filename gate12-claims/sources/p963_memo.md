# P96-3 MEMO — Phase 88's shell follow-ups (FU-P883-1/2/3)

**HEADLINE (a): SPECTRUM EXISTS (NEW OBJECT)** — the P61-1 shell
endowed with the Brown–Gladush surface perfect-fluid action has a
computed ℓ = 0 spectrum in the fixed-bulk sector (details §2, every
sentence labelled). **(b): COUPLED SPECTRUM UNPOSABLE** under the
traceless datum and under the barotropic datum family (§3).
**(c): CONDITION NOT FOUND** — "not found in our search
(limits: §4)" (§4); the upgraded unposability of the conformal
member stands unchanged.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

Plain language first: the joined object is a throat OBJECT — an
interior, a thin shell at r_Σ = 1,000 r₀, and an outside — and this
is not a traversability claim; nothing here makes the object
traversable. Phase 88 showed the member's shell has no equation of
motion at all in pure Weyl gravity. This item did the three
registered follow-ups. First, we gave the shell a real matter
action — a published surface-fluid action, which is a NEW object,
not the member — and that endowed shell does move by an equation:
its slowest wobble is computed below, and at the action's own
linear equation of state it is (barely) stable. Second, we tried
to pose the bulk modes of the joined object with the shell's
strain law as their boundary condition, under a named datum: the
boundary condition turns out to spend itself entirely on fixing
the shell's displacement and never touches the frequency, so no
coupled spectrum is selected. Third, we searched beyond Phase
88's six candidates for a pure-Weyl regularity condition that
would fix the shell's sideways stress from the bulk: none found
in the searched literature. Throughout:
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

Checker: `p963_check.json` — **17/17 PASS** (independent
finite-difference path for every K quantity, the ξ̈ coefficient,
and D_Rn; full 40-digit recomputation of the deciding ω² values).
float64; 40-digit mpmath probes at every deciding point.
Re-gates: [R̃](1000) and [R̃_,n](1000) reproduce the stored
P61-1/P80-2 values with gate differences exactly 0.0, using the
stored full-precision a = 0.27773424114865775; D_R =
−1.5233785879×10⁻⁵, D_Rn = +1.8844230756×10⁻⁵ (P88-3 values).

---

## 1. Sources, searches, poses

All searches were logged verbatim and all poses written BEFORE
any eigenvalue was read: `p963_run_record.md` §§2–5. (a)'s search
(A1–A6) covered the surface perfect-fluid / elastic-shell action
literature; the chosen action is in §2. (c)'s search (C1–C6) is
in §4. (b)'s pose and count are in §3.

## 2. (a) FU-P883-1 — SPECTRUM EXISTS (NEW OBJECT)

**Chosen action (logged before computing; run record §3):** the
P61-1 shell endowed with the Brown–Gladush surface perfect-fluid
action, S_shell = −∫_Σ ε(n_s)√−γ d³y (Brown, Class. Quantum
Grav. 10 (1993) 1579, fluid action with Lagrangian density
−ε(n); Gladush, arXiv:gr-qc/0312067, eq. (2.23), quoted verbatim
in the run record, is its dust case: "The dust on the singular
shell Σ is described by the action I_m = c∫_Σ σ√−g dΣ_n∧dθ∧dα",
inside the total action of his eq. (2.21)). The P61-1 shell
endowed with the Brown–Gladush surface perfect-fluid action has
σ = ε(n_s), p = n_sε′(n_s) − ε(n_s), δp = β²δσ with β² the
action's own response parameter. The P61-1 shell endowed with
the Brown–Gladush surface perfect-fluid action is NOT the
conformal member, and no sentence in this section revises the
member's standing.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

**The equation the action supplies.** Normal variation of the
action of the P61-1 shell endowed with the Brown–Gladush surface
perfect-fluid action in vacuum gives S^{ab}K̄_{ab} = 0, i.e.
−σK̄^t_t + 2p_tK̄^θ_θ = 0, with K̄ the extrinsic curvature of Σ
averaged over the two P61-1 bulk sides. For the P61-1 shell
endowed with the Brown–Gladush surface perfect-fluid action,
K̄^t_t contains d²R/dτ² linearly (τ = shell proper time) with
averaged coefficient C_avg = +0.8095870468 (per side: interior
0.6161737182, exterior 1.0030003754; 40-digit C_avg =
0.80958704679790470388…) — so the P61-1 shell endowed with the
Brown–Gladush surface perfect-fluid action possesses a genuine
ξ̈ equation, the object Phase 88 showed the member lacks.

**Background admissibility (deciding, computed first).** The
background geometry of the P61-1 shell endowed with the
Brown–Gladush surface perfect-fluid action gives K̄^t_t(0) =
+4.4369985428×10⁻⁶ r₀⁻¹ and K̄^θ_θ(0) = +9.9900187071×10⁻⁴ r₀⁻¹
(identical on both sides, as the Darmois match requires; 40-digit
values in `p963_results.json`). The static equation of the
P61-1 shell endowed with the Brown–Gladush surface perfect-fluid
action therefore holds only if its fluid has background pressure
p₀ = +0.0022207158329 σ₀ (40-digit w₀ =
0.00222071583290804039…), i.e. p₀ = +4.5061523831×10⁻⁵ α₀ at
σ₀ = +0.02029144078829105 α₀: the endowed object's own background
equation of state, fixed by its action plus the P61-1 geometry.
Sub-anatomy: the literal dust sub-case of the P61-1 shell
endowed with the Brown–Gladush surface perfect-fluid action
(Gladush's p = 0 action) does NOT admit the P61-1 background —
its static equation residual is −K̄^t_t(0) = −4.4369985428×10⁻⁶
per unit σ₀ ≠ 0 — so no dust spectrum around this background
exists for the P61-1 shell endowed with the Brown–Gladush
surface perfect-fluid action; the perfect-fluid form is required.

**Spectrum (ℓ = 0, fixed-bulk sector — the sector posed in the
run record).** Linearising the equation of motion of the P61-1
shell endowed with the Brown–Gladush surface perfect-fluid
action, with its conservation strain law δσ =
−2(σ₀+p₀)ξ/r_Σ = −4.0673004624×10⁻⁵ α₀·(ξ/r₀), gives
ξ̈ = −ω²ξ with
  ω²(β²) = −1.0196103785×10⁻⁸ + 4.946…×10⁻⁶·β²  (r₀⁻², exact
  linear law; coefficients in `p963_results.json` / checker),
for the P61-1 shell endowed with the Brown–Gladush surface
perfect-fluid action. The stability threshold for the P61-1
shell endowed with the Brown–Gladush surface perfect-fluid
action is β² = 0.0020611430310 (40-digit:
0.00206114303102618371…). At the named linear equation of state
of the P61-1 shell endowed with the Brown–Gladush surface
perfect-fluid action, p = w₀σ with β² = w₀ = 0.0022207158329,
the lowest ℓ = 0 mode of the P61-1 shell endowed with the
Brown–Gladush surface perfect-fluid action has **ω² =
+7.8937794458×10⁻¹⁰ r₀⁻² (ω = 2.8095870597×10⁻⁵ r₀⁻¹) — stable,
by a 7.7% margin in β² over the threshold**, with the sign
confirmed at 40 digits (ω²_mp40 =
+7.8937794457691367370…×10⁻¹⁰) because the value is a near
cancellation of two ~10⁻⁸ terms. At β² = 0 the P61-1 shell
endowed with the Brown–Gladush surface perfect-fluid action is
unstable at ℓ = 0 (ω² = −1.0196103785×10⁻⁸ r₀⁻²). Consistency
number, stated plainly: in the fixed-bulk sector the junction
read-off (J3) strain, −(4/3)D_Rn = −2.5125641008×10⁻⁵ α₀ per
unit ξ, differs from the endowed action's conservation strain
above by the ratio 0.6177473545 — the remaining fraction is
precisely what bulk perturbations must supply in the coupled
problem of §3, so the spectrum in this section is a statement
about the endowed shell's own dynamics at fixed bulks, not about
coupled modes. Sectors: ℓ = 0 of the P61-1 shell endowed with
the Brown–Gladush surface perfect-fluid action is posed in full
in the fixed-bulk sector; ℓ ≥ 1 of the P61-1 shell endowed with
the Brown–Gladush surface perfect-fluid action is NOT closed by
this action (it supplies no tangential displacement variable and
no surface shear modulus), stated in the pose before computing.

**Verdict (a): SPECTRUM EXISTS (NEW OBJECT)** — the spectrum
above belongs in every sentence to the P61-1 shell endowed with
the Brown–Gladush surface perfect-fluid action; it is not a
spectrum of the conformal member, whose shell sector remains
UNPOSABLE UPGRADED.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## 3. (b) FU-P883-2 — COUPLED SPECTRUM UNPOSABLE

Pose (run record §4, written before any eigenvalue): interior
P71-1 and exterior P80-2 quotient systems; boundary condition at
r_Σ = the strain law under a NAMED datum, imposed as the single
scalar condition −(4α₀/3)[δR̃_,n]_Σ = (strain coefficient)·ξ,
with ξ the boundary value the bulk system supplies. Both
registered datums were posed: the traceless datum first, then
the barotropic datum family. Every sentence in this section is a
statement about the joined object's BULK modes under the named
datum — never a shell-own-mode claim, never a traversability
statement.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

**Obstruction (exact, datum-independent in form).** Under the
traceless datum, the strain coefficient is −σ₀/r_Σ =
−2.0291440788×10⁻⁵ α₀/r₀ ≠ 0; under the barotropic datum family
it is −2(σ₀+p₀)/r_Σ, nonzero for every (p₀, β₀²) except the
single slice p₀ = −σ₀. The coupled system's unknowns are
{δg⁻, δg⁺, ξ, ω²}; its Σ conditions are perturbed Darmois (2),
[δR̃] = 0 (1), and, under the traceless datum resp. the
barotropic datum family, the strain-law condition (1). But the
strain-law condition under the traceless datum, and equally
under the barotropic datum family, is one scalar equation whose
only new unknown is ξ itself: for ANY ω² and ANY bulk quotient
amplitudes on either side, it is satisfied exactly by choosing
ξ = −(4α₀/3)[δR̃_,n]_Σ/(strain coefficient). Net constraint on
ω² imposed by the coupling under the traceless datum: **zero**;
net constraint on ω² imposed by the coupling under the
barotropic datum family: **zero**. The coupling therefore
selects ξ, never ω²: the joined object's bulk modes under the
traceless datum form no discrete coupled spectrum (the P71-1 /
P80-2 quotient reads stand, uncoupled, exactly as computed
there: interior smallest physical eigenvalue ≥ 0.00121741,
exterior ≥ 8.3166×10⁻⁵, no crossings), and the joined object's
bulk modes under the barotropic datum family likewise form no
discrete coupled spectrum. This is the P88-3 anatomy one level
up: an algebraic strain law spends itself on the boundary value
it introduces, in the coupled system just as in the shell-only
system. The exceptional barotropic slice p₀ = −σ₀ is worse, not
better, under the barotropic datum family: there the strain
coefficient vanishes, the condition collapses to
[δR̃_,n]_Σ = 0 as a pure bulk constraint, and ξ drops out of the
coupled system entirely (a PARTIAL-style degeneracy, named here;
it does not rescue a spectrum under the barotropic datum
family, since ξ then has no equation at all).

**Verdict (b): COUPLED SPECTRUM UNPOSABLE** — obstruction: the
boundary condition under the traceless datum, and under the
barotropic datum family, introduces exactly as many unknowns
(ξ) as equations (1), so no coupled eigenvalue is ever selected;
this is a statement about the joined object's bulk modes under
the traceless datum and under the barotropic datum family, not
a shell-own-mode statement and not a traversability statement.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## 4. (c) FU-P883-3 — CONDITION NOT FOUND

Condition (verbatim-in-substance, run record §5): a sourced
model keeping the PURE Weyl action, adding only a regularity
condition at Σ on a bulk scalar/invariant not already continuous
here, yielding a determining equation for Ŝ₂² whose premises ALL
hold for the P61-1 shell. Search C1–C6 (run record §2) beyond
Phase 88's six premise-checked candidates (those six were NOT
re-run). New candidates, premise-checked one by one:

| Candidate | Pure Weyl kept | No double layer | No EH term | Regularity quantity not already continuous here | Premises true on BOTH sides | Determining eq. for Ŝ₂² |
|---|---|---|---|---|---|---|
| Rosa, f(X₁,…,Xₙ) junction method (arXiv:2311.11752, PRD 109 (2024) 064018) | FAIL — theory class is f of scalar invariants (worked cases f(R), f(T), f(𝒢)); pure Weyl C² is not posed in it and no C² case is derived | double-layer branch present in its own classification | FAIL in its standard framing (EH-based f(R) class) | its conditions are continuity of the Xᵢ and their derivatives — for this shell the candidate quantities are either R̃-class (already continuous, [R̃] = 0) or underived for C² | not reached | NONE stated for pure Weyl |
| Rosa, f(R,T) thin shells (arXiv:2103.11698) | FAIL — action is f(R,T) | — | FAIL — Einstein–Hilbert-based | — | — | its junction-forced EoS σ = 2p_t belongs to f(R,T), a different theory; quoting it here would be a statement about an f(R,T) object |
| Generalised Darmois–Israel for higher-derivative gravity (Deruelle–Germani–Kaneda line, Universe 8 (2022) 250) | FAIL as a pure-Weyl model — action treated is EH + quadratic terms | regularisation excludes the δ′ sector only by added extrinsic-curvature constraints | FAIL — Einstein–Hilbert term present | its quadratic-gravity conditions reduce, at the conformal exceptional point, to the BDE system (64)–(67), which contains Ŝ₂² nowhere | — | NONE for this shell |
| Grumiller–Irakleidou–Lovrekovic–McNees, conformal gravity holography (arXiv:1310.0819) | PASS — pure conformal gravity | PASS | PASS | FAIL of locus — its conditions are asymptotic (A)dS boundary conditions at infinity (weaker than Starobinsky; admitting the MK–Riegert term), not a regularity condition at Σ on a bulk scalar | not applicable at Σ | NONE — it yields holographic response functions at infinity, no shell equation |
| Kiefer–Nikolic, conformal / Weyl–Einstein canonical gravity (arXiv:1702.04973) | FAIL — the formulation is Weyl² EXTENDED by the Einstein–Hilbert term and a nonminimally coupled scalar | — | FAIL — EH term + scalar added explicitly | — | — | NONE for this shell |

No candidate passes every premise, so no Ŝ₂² value is computed
under (c) (computing one under a failed-premise candidate would
repeat Phase 88's Route-2 error).

**Verdict (c): CONDITION NOT FOUND** — "not found in our search
(limits: web/arXiv search queries C1–C6 as logged verbatim in
the run record §2, covering the pure-Weyl/conformal junction and
regularity literature returned by those queries beyond Phase
88's six candidates; five new candidates premise-checked in
full above)". The upgraded unposability of the conformal
member's shell sector stands unchanged.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## 5. Failure-Protocol ledger

| Item | Anatomy | Follow-up |
|---|---|---|
| (a) dust sub-case inadmissible | The literal Gladush dust action's static equation fails on the P61-1 background by −4.437×10⁻⁶ per unit σ₀ (K̄^t_t(0) ≠ 0): a dust shell cannot sit statically on this join; the perfect-fluid form with p₀ = +0.0022207 σ₀ is the minimal admissible endowment. | Any future endowed-action read must re-check background admissibility first; other actions (elastic, with shear) remain unposed for ℓ ≥ 1 — a sourced surface-elastic action supplying tangential displacement is the named reopening for the ℓ ≥ 1 sectors of an endowed object. |
| (a) fixed-bulk J3 strain mismatch (ratio 0.6177) | At fixed bulks the junction read-off strain and the action's conservation strain differ; bulk perturbations must supply the difference — which is the coupled problem. | Feeds (b): the mismatch is absorbed by ξ-choice there, which is exactly why (b) selects no eigenvalue. |
| (b) coupled spectrum unposable (both datums) | Structural: one algebraic boundary condition, one new boundary unknown (ξ); net constraint on ω² is zero under the traceless datum and under the barotropic datum family. | Reopening condition: a boundary condition containing a TIME DERIVATIVE of ξ or of a bulk field at Σ (e.g. from an endowed action's EOM imposed at Σ, joining (a)'s ξ̈ equation to the bulk systems) would change the count; that is a new registration, not this item. |
| (c) no reopening condition found | Every new candidate either changes the theory (f(R), f(R,T), EH+quadratic, Weyl–Einstein), lives at infinity rather than Σ (holographic BCs), or reduces at the conformal point to BDE, which contains Ŝ₂² nowhere. | FU-P883-3's own condition, carried verbatim: a future sourced model keeping the PURE Weyl action + only a regularity condition at Σ on a bulk scalar/invariant not already continuous here, with all premises holding for this shell, reopens the premise table. |

## 6. C12 accounting

Computed: the [R̃]/[R̃_,n] re-gates (exact, 0.0) and slopes
D_R, D_Rn with the stored full-precision a; for the P61-1 shell
endowed with the Brown–Gladush surface perfect-fluid action, the
averaged extrinsic-curvature data at Σ from both bulk sides
(float64, FD, and 40-digit paths), the ξ̈ coefficient, the
admissibility pressure p₀ and the dust residual, its
conservation vs read-off strain consistency ratio, and its
ℓ = 0 fixed-bulk spectrum law ω²(β²) with named evaluations and
threshold; the (b) count and the exact ξ-absorption argument
under the traceless datum and under the barotropic datum
family; the (c) premise table for five new candidates.
Claimed: exactly the three verdicts above, each in its
registered form and scope. NOT computed and not claimed: any
spectrum of the conformal member (its shell sector remains
UNPOSABLE UPGRADED); ℓ ≥ 1 modes of the endowed object; coupled
bulk modes beyond the count obstruction; any Ŝ₂² value under
(c); nonlinear stability; (V-b) — not computed by anything here
and attached unchanged:
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
Derivation classes: (a) direct computation on stored P61-1 data
with the named action (Class A pattern), second path FD + 40-digit;
(b) exact counting/linear-algebra over the posed system as
registered (Class A pattern); (c) sourced literature audit with
premises checked against stored shell data. No computation
approached ~2 h (main run ~1 min; checker ~7 s). INTERNAL only;
nothing uploaded; nobody contacted.

Files: `results/p963_memo.md`, `results/p963_run_record.md`,
`results/p963_results.json`, `results/p963_check.py`,
`results/p963_check.json`; script `work/p963_compute.py`.
CHECKPOINT96.md not edited; phase88/, phase80/, phase61/ untouched.
