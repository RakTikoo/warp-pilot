# GATE-31 — REGISTRATION: CERTIFICATION OF THE AXIS A
# MEMBER'S BRACKET (0.575, 0.58125] AT VERDICT GRADE

Gate registration, written BEFORE any Gate-31 computation.
Gate-31 is an adversarial re-judgement in the Gate-23/26/27
pattern: it certifies or refuses the claim below, re-deriving
every deciding number from stored artefacts and from the
certification reads this registration fixes. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python
(`~/workspace/warp-pilot/venv/bin/python`; numpy 2.5.5 /
scipy 1.18.1), float64. Writes ONLY under `gate31/`. No
ledger append, no launches, no external contact. Protected
files md5-asserted before and after:
`phase169/work/p1692_engine.py`,
`phase167/work/p167_engine.py`,
`phase162/work/p1621_engine.py`.

## 0. THE CLAIM UNDER JUDGEMENT (verbatim, drafted from
## Phase 288's record)

"The Axis A member (θ-dependent deformation 𝒜(θ) = 0.2 +
(−0.5 + 0.15·cos 2θ) on the Phase 264 joint pose's
background class, with the centring term J derived through
the TOV identity — background audit-clean at max|δP₂| =
1.047×10⁻⁶, zero of 181 angles above the floor) sustains
all seven throat clauses on the sampled march to a first
crossing in (0.575, 0.58125] on NEC_φ = DEC_φ."

Fixed context, not in dispute and not re-opened by this
gate: the member's pose test (Phase 287: POSE HOLDS AT
t = 0, binding NEC_φ +1.015422 datum slice); the read-grade
bracket (Phase 288: (0.575, 0.58125], carriers NEC_φ =
DEC_φ, full state at `phase288/work/p288_member_state.npz`);
the §4b standing (Phase 289: §4b FAILS UNMOVED on this
member, median 0.169177 — Stage D form 2 stands for the
class; this gate does NOT touch it); the lead claim
(G27-A as reworded by Gate-28: combined-class certified
bracket (0.675, 0.68125] — this gate's claim does NOT
replace it).

## 1. THE CERTIFICATE (the Phase 243 §3 instrument,
## transported to this pose and read layer)

Grids (Phase 210 discipline, doubling): G3 (N_θ = 5761,
h_t = 0.00125), G4 (N_θ = 11521, h_t = 0.000625),
G5 (N_θ = 23041, h_t = 0.0003125). **Every grid's march
runs to T_END = 1.0** (the Phase 240 repair discipline:
every window instant is an interior, centred-stencil read
in every grid). The march is pose-independent
(`phase288/work/p288_lib.py`: `march_incumbent(n_th, h_t,
1.0, 0.25)` — the J1 construction, RK4 through the true
lock, seed μ ≡ +0.25 flat, incumbent att); the member
lives entirely in the read layer (`read_arm_A` with the
member profiles `Auu_new` and `J_derived` loaded once from
`phase287/work/p287_built_profiles_amended.npz`, md5
39cc4c573a610908b056045bb82d8758, and frozen). Reads are
indexed by march index m = round(t / h_t), never by
float-t search. Binding clauses: **NEC_φ and DEC_φ**
(both carried through the whole treatment, as in the
record).

**Window (fixed here, not trimmable):**
W = sampled {0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65}
∪ refined {0.56875, 0.58125, 0.5875};
bracket (t_lo, t_hi] = (0.575, 0.58125].

**Per-instant Richardson (per binding clause)** — verbatim
Phase 243 §3: with clause-minimum values v3, v4, v5 on
G3, G4, G5 at one instant: d34 = v3 − v4, d45 = v4 − v5.
- *Monotone case* (d34·d45 > 0): p = log2(d34/d45);
  admissible iff 0.5 ≤ p ≤ 6; L = v5 − d45/(2^p − 1);
  residual r = |L − v5| = |d45|/(2^p − 1).
- *Degenerate case* (otherwise, incl. any zero difference,
  and the monotone formula at inadmissible p): L := v5;
  r := max(|d34|, |d45|).
The instant is **limit-certified for that clause** iff
r ≤ 1×10⁻⁶ AND |d34| ≤ 1×10⁻⁶ AND |d45| ≤ 1×10⁻⁶.
The 1×10⁻⁶ bar is nowhere changed.

**Certificate conditions for the bracket** (all four, for
BOTH binding clauses unless stated):
- **CERT-1 (neighbourhood limit agreement):** every
  instant of W is limit-certified.
- **CERT-2 (bracket at the limit and at the finest
  grid):** L(t_lo) ≥ 0 and L(t_hi) < 0; v5(t_lo) ≥ 0 and
  v5(t_hi) < 0.
- **CERT-3 (no earlier crossing in the window):** for
  every window instant t ≤ t_lo: L(t) ≥ 0 and v5(t) ≥ 0.
- **CERT-4 (first-crossing uniqueness at the finest
  grid):** at every window instant t ≤ t_hi, every
  NON-binding clause's G5 minimum is > 0. Non-clause bars
  are read at G5 at the bracket instants (t_lo, t_hi) and
  reported; a non-clause bar failure at a bracket instant
  voids CERT-4. The bars, in this read layer (transported
  from `phase243/work/p2431_run.py`'s read, with the one
  registered substitution in the last item):
  momentum worst = max over (mom_rho, mom_th, mom_ph) of
  `mom_resid_max` ≤ 1×10⁻¹⁰; flare_min =
  min_θ(exp(−2μ_a)·B.AUU) > 0 (μ_a = the G5 state's μ row
  interpolated to AUDIT_TH at that instant);
  domain_R_min = min over θ, ρ_g ∈ linspace(0, 2, 41) of
  (R00 + 0.1·ρ_g² + 0.5·t²·B.att(θ)) > 0;
  domain_exp2Phi_min = min over θ, ρ_g of exp(2·Phidom),
  Phidom = Φ₀(θ) + ρ_g²·phi2_a, phi2_a =
  0.5·exp(2μ_a)·jpose_a, with the member's jpose
  **jpose_a := J_derived(θ) + exp(−2Φ₀(θ))·mtt_a**
  (the registered substitution: Phase 243's read used
  B.j_prof; the member's read layer replaces it with
  J_derived, exactly as `comp_jets_A` does).

**Character, fixed in advance (Gate-26 §2 discipline):**
whatever the outcome, the certificate is a
**grid-stability** certificate: the per-instant grid
disagreements and residuals are quoted against the
1×10⁻⁶ bar, the worst |d34| / |d45| / r over the window
are stated on the face of the verdict, and no p value or
margin may be worded as a measured convergence rate or
convergence assurance.

## 2. CONTROLS (run first; all must pass before any
## certificate is evaluated)

- **CTRL-1 (stored-read reproduction, diff 0.0
  standard):** fresh reads from the STORED member state
  (`phase288/work/p288_member_state.npz`) via
  `read_arm_A` at the stored rows' march indices
  reproduce `phase288/results/p288_results.json`'s
  `member_instants` (41 sampled) and
  `member_refinement_instants` (3) clause minima at max
  abs diff 0.0 (mom_resid_max compared likewise). If
  CTRL-1 fails, STOP: the machinery discrepancy is the
  result.
- **CTRL-2 (fresh-march reproduction):** a fresh G4
  march's MU/U/MTT at [::40] equal the stored member
  state's [::40] at max abs diff 0.0. (This is the
  control that admits the fresh G3/G5 marches: same code
  path, different (N_θ, h_t).) If CTRL-2 fails, STOP.
- **CTRL-3 (G5 admission):** at t = 0.5, the member's
  NEC_φ and DEC_φ minima on G3/G4/G5 satisfy |d34| ≤
  1×10⁻⁶ and |d45| ≤ 1×10⁻⁶. If CTRL-3 fails, STOP: G5
  is not admitted as a grid and no certificate is
  evaluated.
- **CTRL-4 (protected files):** the three protected
  engines md5-identical before and after.

## 3. DECIDING READS (definitions, fixed)

- **(a) Window reads.** For each grid G3/G4/G5: clause
  minima (all seven) and mom_resid_max at every window
  instant, computed fresh from that grid's marched state
  via the member read layer. (The fresh G4 rows double as
  CTRL-2's read side; the stored-state rows of CTRL-1 are
  a separate comparison, not the certificate's G4 rows.)
- **(b) Non-clause bars** at G5 at the bracket instants,
  per §1 CERT-4.
- **(c) Certificate evaluation.** Per §1: per-instant
  per-binding-clause (v3, v4, v5, d34, d45, case, p, L, r,
  limit-certified); CERT-1…4 booleans with the failing
  instant/clause named for any failure.
- **(d) Span record (for the claim's evidence split;
  record only, no new march):** per-clause minima over
  Phase 288's stored sampled instants t ∈ [0, 0.575]
  (24 instants), computed from the stored
  `member_instants` rows and cross-checked against
  CTRL-1's recomputation at those instants.
- **(e) G5 cost probe (registered decision rule, Phase
  243 §5(e) pattern, threshold unchanged):** before the
  G5 march: march G5 over [0, 0.05] (160 steps), time it,
  project the [0, 1.0] march (3200 steps) as 20 × probe
  wall. State-array size at G5/[0, 1.0]: (3201 × 23041)
  float64 ≈ 5.9×10⁸ B per field; MU + U + MTT ≈ 1.77 GB;
  G3/G4 states are freed before the G5 march, and each
  grid's march+reads run in its own process. **If the
  projected G5 march wall exceeds 900 s, G5 is NOT run:**
  verdict form FAILS-(c) fires, and the G5 route is
  packaged as a kernel spec at
  `gate31/work/g31_g5_kernel_spec.md` with the probe
  numbers on its face.

## 4. DECISION ORDER (fixed)

(i) Any control (§2) fails → no certificate is evaluated;
the control/machinery result is reported (one honest
attempt only) and the verdict is FAILS-(b) for CTRL-1,
FAILS-(a) for CTRL-2/CTRL-3 (machinery cannot support the
certificate), with the failing control named. (ii) The
probe rule (§3(e)) fires → FAILS-(c). (iii) Evaluate
CERT-1…4: any condition fails → FAILS-(a) (the failing
condition, instant, and clause named; the crossing
restated to whatever the certified reads support, priced
in the memo). (iv) CERT-1…4 all hold → the claim SURVIVES:
INTACT if its wording needs no correction, IN RESTATED
WORDING if the gate's wording rulings (§5) require any —
the restated wording is issued by the gate in GATE31.md.

## 5. WORDING RULINGS RESERVED TO THE GATE (decided in
## GATE31.md, on the verified numbers)

(a) Whether "background consistent by construction" is
quotable as stated, or only with the audit's scope
carried (Phase 287's own fence: the verdict is about the
background's O(ρ¹) TOV-consistency at throat scope —
the Phase 285 δP₂ audit, its per-θ ladder-error floor,
the A1.2 smoothness guard). (b) Whether the
sampled-instants fence of Gate-23 (G23-A: the interval is
[0, t) at the sampled and window instants named; no
continuum claim between instants is made or certified)
applies verbatim, and the evidence-class split (span =
sampled standing-grid read; window = limit-certified)
the restated wording must carry. (c) The fences the
claim must carry on its face: §4b / Stage D form 2
standing for this pose (Phase 289) — certification does
not touch it; pose scope and jet scope (jet-scope sector
superposition, exhibit ≠ construction); the director's
south-pole defect domain fence; programme-level
sustainment wording gated by p1592 regardless.
(d) Novelty: NONE (Gate-22 §6 position carried; no
"first", "unique" or "record" wording granted — any
distinction of this bracket is stated programme-internally
only). (e) Publication consequence: decided by the
pattern of Gates 23/26/27/28 and stated with reasons.

## 6. EXECUTION DISCIPLINE

Staged processes (controls+probe / G3 / G4 / G5 /
evaluation), states freed between grids; peak memory at
G5 ≈ 1.77 GB of state plus read temporaries — if a stage
is OOM-killed, that is reported as the stage's result,
not retried with altered settings. The worker's driver
(`gate31/work/g31_run.py`) writes
`gate31/work/g31_results.json` (controls, probe, per-grid
window rows, span record, Richardson table, CERT
booleans); an independent checker
(`gate31/work/g31_check.py`) recomputes the Richardson
arithmetic and CERT booleans from the stored per-grid
rows, spot-recomputes the bracket instants' G4 reads from
the stored member npz at diff 0.0, checks verdict-form
consistency under §4, and writes
`gate31/results/g31_verify.json`. A run memo
(`gate31/results/g31_memo.md`) records walls, the
decision order as executed, and any incident on its face.
