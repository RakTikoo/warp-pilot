# GATE-54 REGISTRATION — INDEPENDENT RE-JUDGEMENT OF PHASE 410
# (SOURCE THE CANDIDATE: THE SPINOR SUPPLIER AT THE PHASE 405
# WINNER'S SITES)

Charged at ledger entry 1095 (2026-11-27). Written before any
Gate-54 computation. Frame of record: the VM
(`~/workspace/warp-pilot/venv`, numpy 2.5.5 / scipy 1.18.1) +
Phase 166 pin, float64. The gate does not repair what it
breaks; failures are recorded with their diagnosis.

## The claims under test (Phase 410, ledger 1094)

(a) REPRODUCTION. At the Phase 405 winner's binding sites —
A1 joint argmin r = 17.926829268292682, A2 SEC argmin
r = 12.073170731707318, A3 peak (10, 0, 0), and the B stencil
(r = A1_r + {−1.0, −0.5, 0, +0.5, +1.0} along A1's direction) —
one m = 1 six-mode Dirac superposition (Fit A primary, N = 6)
reproduces T_req in full at the three A sites: direct
residuals R = ||T_sup − T_req||_F of 8.15×10⁻¹⁵ /
2.76×10⁻¹³ / 2.97×10⁻¹² against the 1×10⁻⁹ bar; joint
Jacobian σ_min = 0.3857618146636974 (rank 30/30); and one
12-mode superposition (Fit B primary, N = 12) tracks the
five-site stencil: 9/9 matched, max direct residual
2.31×10⁻¹⁴, joint σ_min = 0.015432479500623982 (rank 50/50).
σ_min is quoted PER-SOLUTION (G36-C), never as a property
of the target or the mating.

(b) DECOMPOSITION. The supplier's NEC/WEC/DEC and SEC
eigen-channel margins agree with T_req's to ≤ 1.3×10⁻¹² at
all eight site reads (3 Fit A sites + 5 stencil sites); at
A2 the SEC value −2.213557×10⁻⁴ is reproduced at diff
3.9×10⁻¹³; at A3 the SEC trace combination −3.388413×10⁻⁴
at diff 9.0×10⁻¹³. The supplier misses no channel; it
sources T_req as it stands, SEC violation included.

(c) SUPPLIER ACCOUNTING. The supplier's density
T_sup[0,0] is POSITIVE at every site read (Fit A:
+1.239×10⁻⁴ / +3.957×10⁻⁴ / +1.860×10⁻³; stencil:
+1.406×10⁻⁴ … +1.102×10⁻⁴); prices |a|² = Σ|avecs|² =
0.02927 (Fit A) / 0.02123 (Fit B).

(d) THE CTRL-313 CLARIFICATION. The record's σ_min 0.0272
for the Phase 313 mating is Gate-34's value at Gate-34's
OWN refit solution (stored full precision
0.027165249637030254, gate34/results/g34_item3c.json),
reproduced by Phase 410 at rel. ~1.1×10⁻⁹; at Phase 313's
stored solution σ_min = 0.0347527502565207. The gate rules
the quotable form for 313's number going forward.

## Gate machinery (fresh organisation; nothing imported
## from phase410/work, phase320/work, phase313/work,
## gate34/work or gate36/work for any deciding computation)

- `g54_lib.py`, written for this gate alone:
  - γ matrices in the Dirac representation assembled by
    Kronecker products (γ⁰ = σ₃⊗I₂, γⁱ = iσ₂⊗σᵢ) — a
    different construction from the phases' np.block
    assembly; the representation itself is the convention
    the stored χ spinors are written in.
  - The superposition as an explicit FIELD FUNCTION
    ψ(X), X = (t, x⃗): modes summed directly with
    analytic mode-by-mode derivatives. NO pairwise
    S-matrix, NO T_from_S einsum, NO folded-amplitude
    shortcut anywhere in a deciding path (Phase 410's
    fits and Jacobians ran on the pairwise path).
  - T_ab from the canonical symmetrised formula
    (i/2)[ψ̄γ_(a∂_b)ψ − (∂_(aψ̄)γ_b)ψ] − η_ab·L with the
    Lagrangian density L computed honestly, not assumed
    zero (Gate-25's convention resolution applies:
    (i/2) with averaged symmetrisation is the textbook
    tensor).
  - A separately written pairwise assembly exists in the
    lib ONLY as the builder self-consistency control
    path (C1); it feeds no deciding read.
  - Own Hawking–Ellis type classifier and own
    eigen-channel decomposition, written from the
    definitions. Channel definitions are Phase 410
    SS4(ii)'s (the definitions are the claim's content;
    the code is the gate's): NEC_r = ρ + p_r, NEC_t =
    ρ + p_t (each tangential), WEC = ρ, DEC_i = ρ − |p_i|,
    DEC_flux = ρ − ||T_0i||₂, SEC_trace = ρ + p_r +
    p_t1 + p_t2, SEC_i = ρ + p_i; SEC_min = min(SEC_trace,
    SEC_r, SEC_t); joint_min = min(NEC_r, NEC_t, WEC,
    DEC_r, DEC_t, DEC_flux). p_r is the principal
    pressure whose eigenvector's spatial part has the
    largest |component along n̂|, n̂ = point/r.
  - Own FD Jacobians of the gate's own residual map
    (upper-triangular components of (T − T_req) /
    ||T_req||_F per site, θ = [pvecs; Re avecs;
    Im avecs]): central differences h_j =
    1×10⁻⁶·max(1, |θ_j|) (the 313/320 recipe), plus a
    forward-difference variant for the Gate-34-theta leg
    (mirroring Phase 410's amended CTRL-313 leg) and an
    h-stability spot check (h×10, h÷10) at the Fit A
    primary.
- Targets are the STORED tensors (phase410/work/
  p410_targets.json That per site), taken as data —
  Gate-36's precedent (fits against stored targets;
  the winner's geometry itself is Gate-50's verified
  record, not re-judged here). Stored solutions are
  phase410/work/p410_fitA_primary.json and
  p410_fitB_primary.json.

## Controls (all run before any claim read is believed)

- C1 BUILDER SELF-CONSISTENCY: field-function path vs
  the lib's pairwise cross-check path on 20 random mode
  sets and on both stored primaries: max relative T
  component diff ≤ 1×10⁻¹². Per-mode health: u†u = 2E
  and (p̸ − m)u = 0 at ≤ 1×10⁻¹³ for every stored mode.
- C2 STORED 320 WINNER: gate direct residuals at
  phase320/work/p320_joint_bestfit.json's solution vs
  its stored Rs_direct: max abs diff ≤ 1×10⁻¹³ and gate
  maxR ≤ 1×10⁻¹²; gate σ_min at that θ vs stored
  3.994300907411277×10⁻⁴: rel diff ≤ 1×10⁻².
- C3 STORED 313 WINNER: gate maxR at
  phase313/work/p313_joint_bestfit.json's solution vs
  stored max R_direct 3.253339860306391×10⁻¹³: abs diff
  ≤ 1×10⁻¹³ and gate maxR ≤ 1×10⁻¹².
- If any control fails, the gate stops, records the
  failure with its diagnosis, and rules on what survives
  without the failed leg.

## Ruling bars (fixed in advance)

(a) SURVIVES if gate per-site direct residuals for both
    primaries are ≤ 1×10⁻⁹ (the registered match bar)
    and gate σ_min agrees with the phase's at rel diff
    ≤ 1×10⁻² for each fit; RESTATED with the gate's
    numbers if the residuals pass but a σ_min rel diff
    exceeds 1×10⁻²; FAILS if any primary residual
    exceeds 1×10⁻⁹.
(b) SURVIVES as stated if the gate's max |channel diff|
    over all channels and all eight site reads is
    ≤ 2×10⁻¹² (the claim's ≤ 1.3×10⁻¹² class), with the
    A2 SEC_min diff and A3 SEC_trace diff individually
    ≤ 1×10⁻¹²; RESTATED with the gate's max diff if it
    lands in (2×10⁻¹², 1×10⁻⁹]; FAILS above 1×10⁻⁹.
(c) SURVIVES if every site density sign is positive on
    the gate's reads and both |a|² prices reproduce at
    rel diff ≤ 1×10⁻⁹ (pure arithmetic on stored
    avecs); the per-site implied s² consistency is
    recomputed as supporting evidence.
(d) The reproduction stands if the gate's σ_min at
    Gate-34's stored θ (g34_item3a.json N6_winner) agrees
    with the stored 0.027165249637030254 at rel diff
    ≤ 2×10⁻² (Phase 410's amended bar) under at least
    one of the gate's FD variants, and the gate's σ_min
    at Phase 313's stored θ agrees with
    0.0347527502565207 at rel diff ≤ 1×10⁻². The ruling
    on quotable form follows G36-C regardless of the
    numbers: a σ_min is quotable only with its solution
    named on the face.

## Laptop admission control

The gate lib + a driver + the stored JSONs it needs are
staged to the laptop pool (spark@100.71.86.14); the
deciding reads of (a) and (b) are re-run there and
compared read-by-read. Admission is reported per read
class; deciding reads are the VM's regardless.

## Standing fences (carried onto any surviving set)

Site mating ≠ extent coverage (no coverage claim; the
candidate's extent audit is Phase 409's, the coverage
line is 346/357/368/362). Sourcing ≠ curing: the mating
sources the winner's tensor AS IT STANDS, SEC violation
included — NO no-exotic-matter claim attaches to any
sourced design. Novelty NONE for the method
(Martín-Moruno & Visser 2021, Gate-25). σ_min per-solution
only (G36-C).

DESK: NO DATA CONTACT (anticipated — a
configuration-space re-judgement against stored records;
no measured dataset bears on it).
