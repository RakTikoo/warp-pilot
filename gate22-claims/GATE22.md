# GATE-22 — ADJUDICATION OF THE WOUND-DIRECTOR SUSTAINMENT CLAIM SET (Phases 207/209/210)

Date: 2026-11-23. Adversarial re-judgement, not a phase. Frame of
record: Phase 166 pin, Gate-19-corrected tensor, venv python
(numpy 2.5.5 / scipy 1.18.1). Method: the claim set was re-derived
and re-run from the stored artifacts with Gate-22's own drivers
(`gate22/work/g22_sym.py`, `gate22/work/g22_march.py`); nothing
quoted from Phases 207/209/210 was trusted. Independence, priced
on the face: the SymPy derivation of attack line (a) is
from-scratch (no Phase 202/205 driver code used); the march
re-runs of attack lines (b)/(e) use the programme's own engines
(phase162 march, phase167 reads, phase207 T2 read-level engine)
driven by Gate-22's own driver and gate construction — the same
independence class as Gates 15/19. All deciding numbers below
reproduced at abs diff **0.0** against the stored records, which
on the frame of record is the signature of a correct re-run in
the same frame, not an independent-frame confirmation.

## VERDICTS

- **G22-1: SURVIVES IN RESTATED WORDING** (restated wording in §1).
- **G22-2: SURVIVES IN RESTATED WORDING** (restated wording in §2).
- **G22-3: SURVIVES IN RESTATED WORDING** (the conjunction of the
  restated G22-1 and G22-2, with the bar-set audit of §4 and the
  scope fences of the original claim; §5).
- **Novelty: NONE granted** — "not found in our search (limits:
  §6)". No "first/unique" wording is available to this claim set.

No claim FAILS. The two restatements are precision corrections,
not softening: every deciding number in the original set
reproduces exactly under independent re-run; what the
restatements fix is (i) two scope qualifiers the original wording
left implicit (sampled instants; the grid at which the FD
second-path bar was discharged) and (ii) one mechanism clause
that is pointwise false for DEC_ρ as stated, though true at
every point that carries a minimum or a gate read.

---

## §1. G22-1 — the director arm's clause set on [0, 0.5]

**Attack lines (b), (e).** Gate-22 re-ran the director march
(m = 1, κ = 0.3, P-DIR-T2) on G3 (5761, 0.00125) and G4 (11521,
0.000625), 21 sampled instants, fresh process. Reproduced
exactly (abs diff 0.0 vs `phase210/results/p2101_results.json`):

- worst clause minimum at G4 = **+0.0045418770853060675**
  (NEC_φ = DEC_φ, tied, at t = 0.5) — the claim's quoted value;
- per-clause worst minima at G4: NEC_ρ = DEC_ρ
  +0.024846605153054924; NEC_θ +1.0625750349885348; DEC_θ
  +0.9053748593945452; WEC +1.0625234390625884 — all ≥ the
  registered −10⁻⁹ bar at every sampled instant;
- momentum worst 3.3306690738754696×10⁻¹⁶ ≤ 10⁻¹⁰;
- flare min 0.15033189900880217 > 0; domain R min
  0.6858751797844092 > 0, exp(2Φ) min 0.0058112457952559345 > 0
  at every sampled instant.

The one bar the original wording asserts but Phase 210 did not
re-read is the **FD second path**: `p2101_results.json` contains
no FD second-path block (Gate-22 verified by key inspection —
the conditional's read list was the gate + clause set + momentum
+ flare/domain). The FD sign-agreement bar (≥ 5 instants) was
discharged in Phase 207 at the 5 registered instants on the G2
march (`p2071_memo.md` §2), and Phase 210's director G2
cross-check against Phase 207's stored director-fine minima is
0.0 — so the G2 march to which those FD reads attach is
bit-identical to the one re-run here. The bar is met, but at G2,
not G4. Additionally, "the whole march interval" in the
registered bar set means the 21 sampled instants (Phase 203
registration: "pointwise at every sampled instant"; worst-instant
standard) — the claim inherits that meaning and the restatement
makes it explicit.

**Restated G22-1 (the quotable form):** *Under the corrected
prescription P-DIR-T2, the director arm (m = 1, κ = 0.3) at the
Phase 169 A-branch throat datum meets every registered throat
clause bar at all 21 sampled instants of [0, 0.5] on grid G4
(worst clause minimum +0.0045418770853060675, NEC_φ = DEC_φ at
t = 0.5), with momentum (worst 3.3306690738754696×10⁻¹⁶), flare
(min 0.15033189900880217 > 0) and domain regularity passing at
G4, and FD second-path sign agreement as read in Phase 207 at
the 5 registered instants on the G2 march (not re-read at G4;
the G2 director march is bit-identical in both records,
cross-check diff 0.0).*

## §2. G22-2 — the refinement gate is a grid artefact

**Attack lines (b), (d).** Gate-22 re-ran the κ = 0 march on all
four grids and rebuilt the gates with its own construction.
Reproduced at abs diff **0.0** against the stored sequence:

D12 = 5.82636026180694×10⁻⁶ (t = 0.5); D23 =
1.359258471111957×10⁻⁶ (t = 0.5); D34 =
2.5300142314499396×10⁻⁷ (worst instant t = 0.425, moved off the
interval end); p34 = 2.42560241398276; Richardson limit L34 =
3.108629483945071×10⁻⁷ ≤ 1×10⁻⁶ bar. Every clause's (G3, G4)
pair maximum is below the bar (Gate-22's recomputation:
NEC_ρ/DEC_ρ 2.5300142314499396×10⁻⁷; WEC 2.1650333681400014×10⁻⁷;
DEC_θ 2.2174152913834178×10⁻⁷; NEC_θ 8.570956278042274×10⁻⁸;
NEC_φ/DEC_φ 1.554312234475219×10⁻¹⁴). The director arm's own
gate gate_dir(G3, G4) = 2.5300142314499396×10⁻⁷ — **bit-exactly
equal** to the κ = 0 D34 in Gate-22's re-run (abs diff 0.0).

**The mechanism clause needs one correction.** The claim states
the equality holds "because the director shifts the carrier
clauses by identically zero". Gate-22's pointwise check (G2,
t = 0.5, director vs control clause arrays): NEC_ρ max pointwise
diff 1.05×10⁻¹³, NEC_θ 5.48×10⁻¹⁴ (float residue at the
defect-core magnitudes; the underlying shifts are the exact
trace cancellation +(κ/2)c_m − (κ/2)c_m), and ΔNEC_φ = κ·c_m,
ΔWEC = (κ/2)·c_m pointwise to 3.6×10⁻¹⁵ — all as claimed. But
**DEC_ρ is NOT pointwise shift-invariant**: DEC_ρ = ρ − |p_ρ|,
and where the shift s = (κ/2)c_m moves p_ρ across zero, DEC_ρ
changes by 2p_ρ ≠ 0; Gate-22 measures pointwise DEC_ρ
differences up to **0.6203498633618989** at t = 0.5. This is the
DEC-saturation algebra the record already knows (Phase 202 §4,
for DEC_φ/DEC_θ). It touches nothing deciding: the saturation
points are non-carrying (DEC_ρ's minimum sits at the θ* region,
where p_ρ does not cross zero), DEC_ρ's minima reproduce the
κ = 0 arm's exactly (+0.024846605153054924 at G4, both arms),
and its gate contribution is bit-identical. The claim's
conclusion is exactly right; its stated reason is exactly right
for NEC_ρ and right at every carrying point for DEC_ρ.

**Restated G22-2 (the quotable form):** *The refinement gate
that blocked the SUSTAINED form in Phase 207 is a grid artefact
under the decision rules registered before each study (Phases
209/210): the κ = 0 four-grid gate sequence falls monotonically
(5.82636026180694×10⁻⁶ → 1.359258471111957×10⁻⁶ →
2.5300142314499396×10⁻⁷) with Richardson limit
3.108629483945071×10⁻⁷ ≤ the 1×10⁻⁶ bar, and every clause's
(G3, G4) pair maximum is below the bar. The director arm's own
(G3, G4) gate equals the κ = 0 value bit-exactly: the gate's
maximum is carried by NEC_ρ/DEC_ρ; the director shifts NEC_ρ by
identically zero pointwise (exact trace cancellation), and
DEC_ρ's minima and pair disagreements reproduce the κ = 0 arm's
exactly — DEC_ρ's pointwise shift vanishes wherever p_ρ does not
change sign under the shift, while pointwise DEC_ρ differences
up to 0.620 (t = 0.5) occur at non-carrying grid points where
p_ρ crosses zero (DEC saturation) and touch no minimum and no
gate read.*

## §3. Attack line (a) — the T2 derivation, independently re-derived

Gate-22 re-derived (∇n)² from scratch (`g22_sym.py`): throat
geometry dl² = dρ² + R(ρ,θ)²(dθ² + sin²θ dφ²) with
R(ρ,θ) = A(θ) + ρ²B(θ) (so R_,ρ(0,θ) = 0 identically, A generic),
n = cos(mφ)φ̂ + sin(mφ)θ̂, full symbolic Christoffel/covariant
derivative computation, m = 1 and m = 2. Results, both m:

- (∇n)² − c_m^(T2) simplifies to **0 exactly** — the corrected
  profile [(m − cosθ) − (A_,θ/A)sinθ]²/(sin²θ·A²) is the posed
  director's actual (∇n)², with the A_,θ term's coefficient and
  sign exactly as P-DIR-T2 states (−(A_,θ/A)·sinθ inside the
  bracket, entering through Γ^θ_{φφ}/Γ^φ_{φθ}'s ∂_θ ln(A sinθ));
- (∇n)² ≠ the refused P-DIR-T1 form (difference nonzero) — the
  Phase 205 refusal and the correction were both necessary;
- ∇_ρ̂n = 0 and ∇_θ̂n = 0 at the throat, identically (the A_,θ
  terms in ∇_θ̂n cancel exactly, as Phase 205 found);
- (∇n)² is exactly φ-independent (∂_φ = 0 symbolically);
- the φ-averaged Ericksen tensor is diagonal with
  ⟨G_ρρ⟩ = ⟨G_θθ⟩ = 0 and ⟨G_φφ⟩ = (∇n)², all averaged
  off-diagonals zero — so C-SYM's clauses pass under Gate-22's
  own derivation, and the channel-entry form (only the four
  diagonal channels shift; no momentum content) is correct.
  The engine's J['Ah'] is the analytic A_,θ = (t²/2)·Att′(θ)
  (verified in `p1621_engine.instant_jets`).

## §4. Attack line (d) — the bar set was not moved

Phase 203's registration (`p2034_registration.md`, Bars) fixes:
full throat EC set ≥ −10⁻⁹ pointwise at every sampled instant;
momentum ≤ 10⁻¹⁰; flare > 0; domain regularity; refinement gate
≤ 10⁻⁶; FD second-path sign agreement at ≥ 5 instants;
worst-instant standard. Phase 207's registration carries the
identical list in substance and applies it (its sole failure:
the gate, at the (G1, G2) pair). Phases 209/210 changed **no
threshold and no gate construction** (max abs disagreement of
per-instant clause minima between a grid pair, over instants and
clauses); what they changed is the grid pair at which the
disagreement is evaluated, under decision rules registered
before each run (Phase 209's three forms; Phase 210's ARTEFACT
iff D34 < D23 AND L34 ≤ 10⁻⁶). That is not a moved bar: the
artefact question — is the 5.826×10⁻⁶ value a property of the
pose or of the G1/G2 resolution — is the follow-up Phase 207's
own record named (FU-P207-1) before any finer grid existed, and
a refinement gate whose verdict could never be revisited at
finer resolution would be a bar on the grid, not on the physics.
The (G1, G2) pair still reads 5.82636026180694×10⁻⁶ (Gate-22
reproduced it); the artefact verdict is the statement, now
decided under the pre-registered rule, that this disagreement
vanishes under refinement (sequence → Richardson limit
3.11×10⁻⁷, every clause individually below the bar on the
finest pair, WEC's non-monotone three-pair history — 5.9×10⁻⁸ →
1.36×10⁻⁶ → 2.17×10⁻⁷ — resolved as a transient on the finest
pair). **No bar moved between Phase 203's registration and
Phase 210's read.**

## §5. Attack lines (c), (e), and the conjunction G22-3

**(e) Control identity — reproduced exactly.** Gate-22's own
κ = 0 G2 run: first NEC_φ failure at **t = 0.400**, worst
NEC_φ = **−0.6297872673028908**, abs diff 0.0 against
P169-1(f). The baseline against which every director movement
is priced is intact, and the baseline's failure value is itself
grid-converged (G3/G4 agree to ~10⁻¹²) — the artefact verdict
concerns the gate value only, not the baseline's failure.

**(c) The interval edge — priced from the record, march not
extended.** The director's NEC_φ/DEC_φ minimum (G4, Gate-22's
re-run; G3 agrees to ≤ 10⁻⁶ throughout) declines monotonically
from t ≈ 0.075 to **+0.0045418770853060675 at t = 0.5**, and the
decline is *steepening* at the edge: secant slope over the last
0.2 of the interval −3.68 per unit t; over the last 0.1, −4.75;
last step (0.475 → 0.5), −5.85; least-squares over the last five
instants −4.74. Linear extrapolation at the terminal rates
exhausts the remaining margin at **t ≈ 0.5008–0.5010** — i.e.
within ~10⁻³ of additional time (≈ 0.2% of the interval) — and
because the slope is steepening, that is an optimistic bound,
not a conservative one. **The honest coverage of the pose-scope
claim is exactly [0, 0.5] and nothing past it**: the interval
extension question (Phase 210's FU-P210-1) is not a formality —
at the terminal decline rate the pose's margin is spent
essentially immediately beyond the registered interval. No
wording in the claim set reads past t = 0.5, and none may.

**G22-3: SURVIVES IN RESTATED WORDING** — the conjunction of
restated G22-1 and restated G22-2: *therefore the Phase 207
SUSTAINED form's bar set is met at this pose's scope, in the
restated G22-1/G22-2 forms above* — jet/channel-read scope
(sector superposition at the channel-read level; per-instant
ZAMO re-pose; no ṅ terms, no director dynamics, no back-reaction
on the geometry — the (a.3)/(a.4) fences of the Phase 203
registration), P129-6 combined-class fences, interval exactly
[0, 0.5] per §5(c), and the p1592 deciding scan still gates
programme-level milestone wording. No programme-level claim is
in this set, and this gate grants none.

## §6. Novelty position (claim-gate terms)

Searches run for this gate (web index, English only, abstracts
and partial full texts): dynamic/evolving traversable wormholes
and NEC theorems; sustained time-dependent throat audits;
director/Ericksen/nematic matter at wormhole throats; Teo-class
constructions; all-energy-conditions-satisfied throat matter.
Nearest neighbours in primary sources:

- **Hochberg & Visser, gr-qc/9802048; gr-qc/9901020** — NEC
  violation is *generic* for dynamic wormhole throats in full
  spacetimes. This does not contradict the claim set: the claims
  are jet/channel-read scope (posed jets, sector superposition,
  exhibit ≠ construction), not a full spacetime solution, and
  the scope fence is precisely what keeps the two from
  colliding. It does mean any future full-solution promotion of
  this pose faces a theorem-grade headwind, stated here so the
  fence is not mistaken for a loophole.
- **Teo, gr-qc/9803098** — the rotating class itself (published);
  its throats generically violate NEC.
- **Dynamic-wormhole constructions** (Kim-line cosmological
  wormholes; Kuhfittig's time-dependent-EoS solutions;
  Ditta & Channuie, arXiv:2607.04041, transient dynamical
  wormholes) — time-dependent throats whose NEC is *violated*
  at/near the throat, in several cases with the violation
  decaying in time. None audits a full clause set held ≥ 0 over
  a marched window.
- **Harko, Lobo, Mak & Sushkov (arXiv:1301.6878)** and the
  modified-gravity line — throat *matter* satisfying all energy
  conditions while curvature terms carry the flare-out
  violation: a different mechanism (modified gravity, static),
  not this claim's category (GR, director sector, time-marched
  jet scope).
- **Director/Ericksen matter**: no hit couples a nematic
  director sector to a wormhole throat; the Ericksen/Frank
  stress itself is textbook-published (de Gennes & Prost line).

Position: every ingredient is published; the specific
conjunction — a φ-wound director closing the φ clause at a
Teo-class throat datum and holding the full registered clause
set over a lock-marched time window at jet scope, with the
refinement gate adjudicated — was **not found in our search
(limits: web-index only, English only, four query families,
abstracts/partial texts; no systematic INSPIRE/ADS full-text
sweep)**. The claim gate's full protocol (exact-category
best-mark comparison + independent second path + complete
literature search with gaps stated) **cannot be met from a
web-index search alone, and this gate does not pretend
otherwise**: no "first", "unique" or "record" wording is
granted or implied. Novelty classification, in the gate's
terms: **PARTIALLY KNOWN at ingredient level; the conjunction
ungraded — "not found in our search", nothing stronger.**

## Files

- `gate22/work/g22_sym.py` + `g22_sym_results.json` — the
  from-scratch SymPy re-derivation (§3).
- `gate22/work/g22_march.py` + `g22_march_results.json` —
  Gate-22's fresh-process march re-runs (κ = 0 on G1–G4;
  director on G3/G4; pointwise shift-identity check; edge
  pricing) (§§1, 2, 5).
- No ledger append, no launches, no external contact beyond the
  novelty searches above. Nothing outside `gate22/` was edited.
