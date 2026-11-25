# GATE-35 — ADVERSARIAL RE-JUDGEMENT OF PHASE 314'S POINTWISE MEMBER

Date: 2026-11-24. Adversarial re-judgement, not a phase.
Scope, fixed in advance (`gate35/work/g35_registration.md`):
whether Phase 314's headline member — ramp M(r) = 1 + 4.00·
[U(r; 9, 20.5) − U(r; 21, 24)] on the Gate-30 winner's
(S, N) verbatim, β = 1.1, posed shell r ∈ [10, 20] — earns
the continuum upgrade of its SET-244 density-positivity
read, and whether its stored values survive an independent
re-read. Frame of record: Phase 166 pin, venv python
(numpy/scipy/sympy), float64. Method: the gate wrote its
own machinery throughout — a fresh split-formula ρ
evaluator (`g35_rho.py`) and a symbolic-Einstein assembly
(`g35_lib.py`: spherical line element with radial shift,
sympy Einstein tensor, Eulerian frame transform) sharing
no tensor machinery with p312_lib/p314_lib/p308_lib,
none of which was imported for any tensor or ρ
computation. The gate does not repair what it breaks.

## VERDICT

- **ITEM 1 — CONTINUUM-CLEAN AT ADVERSARY GRADE.** The
  legality-restricted adversary search found NO locus with
  ρ_req < 0 anywhere in the closed posed volume. The
  continuum minimum of ρ_req is **+8.100317×10⁻⁵ at
  r = 20.000000 (the closed outer boundary), u = 0** —
  slightly below the SET-244 minimum, R1-carried against
  Q_K = 0 exactly. Certified continuum lower bounds
  (found minimum − margin floor) are positive in all
  three registered regions: inner **+2.547705×10⁻⁴**,
  mid **+1.167761×10⁻⁴**, rim **+8.081922×10⁻⁵**. The
  positivity is therefore quotable as a continuum
  statement AT THE GRADE STATED IN §3 — an adversary-grade
  numerical certificate (exact angular reduction + radial
  mesh + derivative floors), not an analytic proof.
- **ITEM 2 — THE STORED RECORD IS CONFIRMED.** The gate's
  independent assembly reproduces every stored headline
  value at float64 round-off level (≤ ~2×10⁻¹⁵ relative,
  several exactly): depth, all four binding sites (point,
  ρ_req, both NEC reads, Type-I status), and the full
  SET-244 EC summary. No discrepancies.
- **ITEM 3 — CLAIM SET (§5):** the member's existence and
  values **SURVIVE**; its positivity **SURVIVES RESTATED**
  (continuum form at adversary grade, §5 G35-B); its depth
  **SURVIVES**. The EC fence is carried verbatim in
  substance in every claim: the member's NEC/WEC/DEC reads
  remain violated at the stated values — this is a density
  statement about a target, never a legality or front
  statement.

## §1. Controls — all PASS, run before any attack read

- **C-G1 (Item 1 evaluator vs stored splits):** the gate's
  fresh split evaluator reproduces the stored per-site
  (R1, R2, Q_K, ρ_req) at S1–S4 with max relative diff
  **1.79×10⁻¹⁵** (bar 1×10⁻⁹), and the stored SET-244 ρ
  minimum at its stored locus (r = 19.878049, transverse)
  at rel diff 1.1×10⁻¹².
- **C-G2 (Item 2 assembly, M ≡ 1 reduction):** depth rel
  diff 2.50×10⁻¹⁵ vs −0.001386956608122417; SET NEC min
  rel diff 4.25×10⁻¹⁶; Type-I count **1245 exact**; polish
  radius exact; four site ρ_req rel diffs 1.7–8.6×10⁻¹⁵.
- **C-G3 (Item 2 assembly, headline SET reproduction):**
  ρ min rel diff 1.80×10⁻¹⁵ (same SET point, index 6516,
  r = 19.87804878, n_x̂ = +0.0040761); NEC/WEC/DEC minima
  rel diffs ≤ 1.7×10⁻¹⁵ (DEC 0.0); Type-I count **2615
  exact**.
- **Internal certificate (Item 2):** the assembly's tensor
  ρ vs its own fresh split implementation — binding sites
  max rel diff 1.56×10⁻¹⁵; 20 random volume points max rel
  diff 7.62×10⁻¹⁶; vs Item 1's independent evaluator at the
  sites, max rel diff 1.73×10⁻¹⁵. Three implementations of
  ρ (Phase 314's assembly, the gate's evaluator, the
  gate's symbolic tensor) agree at round-off level.

## §2. Item 2 — independent re-read (detail)

Assembly path: metric in spherical coordinates (t, r, θ, φ)
with the polar axis along the shift direction (γ = M dr² +
r²dΩ²; g_tr = −βS cosθ, g_tθ = +rβS sinθ as the pullback of
the shift covector); sympy Einstein tensor with (S, N, M)
as undefined functions of r and an analytic ADM inverse
asserted symbolically; T_req = G/(8π) lambdified;
Cartesian transform T_cart = J^(−T) T_sph J^(−1); Eulerian
frame via verify_metric. Depth by the gate's own adversary
polish (Nelder–Mead of SAMPLER-M NEC, Type-I-gated, seeded
from the worst Type-I SET points); sites by Phase 293's
rule in the registered form; exact pointwise NEC by the
gate's own 642-fibre scan + polish.

| read | gate | stored | diff |
|---|---|---|---|
| depth (SAMPLER-M polished) | −5.327658635240827×10⁻⁴ | −5.327659×10⁻⁴ (full prec. −0.0005327658635240826) | −1.08×10⁻¹⁹ |
| polish point | r = 12.3134870420811, Type-I | identical | 0.0 |
| ρ_t at polish point | +6.263182190001702×10⁻⁴ | +6.263182×10⁻⁴ | round-off |
| S1 ρ_req (r = 12.313487, Type-I) | +6.263182190001702×10⁻⁴ | +6.263182×10⁻⁴ | 0.0 |
| S2 ρ_req (r = 11.829268) | +6.818808066077541×10⁻⁴ | +6.818808×10⁻⁴ | +8.7×10⁻¹⁹ |
| S3 ρ_req (r = 12.317073, Type-I) | +6.257630013907989×10⁻⁴ | +6.257630×10⁻⁴ | +9.8×10⁻¹⁹ |
| S4 ρ_req (r = 17.682927) | +1.172278×10⁻⁴ | +1.172278×10⁻⁴ | 0.0 |
| site NEC (SAMPLER-M and exact pointwise) | — | — | ≤ 4.6×10⁻¹⁸ abs, all sites |
| SET NEC min / median / max | −1.1700067327832906×10⁻³ / −1.6869212992366483×10⁻⁴ / +6.541263184102982×10⁻⁴ | −1.1700067327832923×10⁻³ / −1.6869212992366763×10⁻⁴ / +6.541263184103002×10⁻⁴ | ≤ ~2×10⁻¹⁵ rel |
| SET WEC min | −1.0440691445181177×10⁻² | −1.0440691445181194×10⁻² | round-off |
| SET DEC min | −1.0000031873996493 | identical | 0.0 |
| SET SEC min | −1.2006829673724798×10⁻² | −1.2006829673724816×10⁻² | round-off |
| SET ρ min / median / max | +8.272455162810711×10⁻⁵ / +2.722318715886096×10⁻⁴ / +8.830803571811661×10⁻⁴ | +8.272455162810697×10⁻⁵ / +2.722318715886096×10⁻⁴ / +8.830803571811661×10⁻⁴ | ≤ ~2×10⁻¹⁵ rel |
| Type-I count | 2615 | 2615 | exact |

**Discrepancies: none.** (One process note: the first
Item 2 worker was killed mid-run by an infrastructure
restart; its code was recovered, audited in full by the
replacement worker, required no changes, and every number
above comes from the replacement's own executed run.)

## §3. Item 1 — the adversary search and its grade

**Structural reduction (verified, then used):** ρ_req
depends on the direction only through u = n_x̂² ∈ [0, 1] —
R(γ) is direction-free; the Q_K numerator and α² are
affine in u (max affine deviation 2.5×10⁻¹⁶ over 50 random
samples; ρ(u) at fixed r is a ratio of affine functions,
monotonic in 50/50 samples). The angular minimum
ρ*(r) = min_u ρ(r, u) is therefore EXACT, attained at a u
endpoint. The registered 2001-point u-scan + golden polish
was nevertheless run at every radius.

**Radial adversary:** mesh Δr = 0.01 over [10, 20] (1001
radii) plus a rim mesh Δr = 0.001 on [19.5, 20] (501
radii). ρ* decreases monotonically over the volume — there
were NO interior mesh local minima to polish. Registered
analytic seeds evaluated directly: r = 10 and r = 20
exactly (closed boundaries); the S′ extremum r = 15.0 at
u = 0 (ρ = +2.013728×10⁻⁴); the M′′ sign-change radius
r = 14.75 (ρ* = +2.252896×10⁻⁴); the rim window
[19.99, 20]. No mesh, seed, or polished point has ρ < 0.

**Global continuum minimum:** ρ* = **+8.100317×10⁻⁵ at
r = 20.000000, u = 0** — split R1/(16π) = +7.9565×10⁻⁵,
R2/(16π) = +1.4379×10⁻⁶, Q_K/(16π) = 0 (S = S′ = 0 at
r = 20, so ρ is direction-independent there). The
continuum minimum sits BELOW the SET-244 minimum
(+8.272455×10⁻⁵ at r = 19.878) and is Phase 314's rim
mechanism pushed to the boundary itself: the floor is
R1's (1 − 1/M)/r² term at its weakest radius, against a
vanished negated-square remnant.

**Margin floors** (Phases 216/219 quoting; floor₁ =
2·max|dρ*/dr|_FD(h=1e-5) × mesh half-spacing 0.005 —
the safety factor 2 and the COARSE half-spacing are used
throughout, so the rim floor is conservative against the
finer rim mesh that actually ran; floor₂, the
second-order form, is recorded in the results file and
is smaller in every region; no regional minimum is an
interior stationary point, so floor₁ certifies):

| region | found min | at r | floor₁ | certified bound |
|---|---|---|---|---|
| inner [10, 12.5] | +2.590271×10⁻⁴ | 10.000 | 4.257×10⁻⁶ | **+2.547705×10⁻⁴** |
| mid [12.5, 17.5] | +1.187206×10⁻⁴ | 17.500 | 1.944×10⁻⁶ | **+1.167761×10⁻⁴** |
| rim [17.5, 20] | +8.100317×10⁻⁵ | 20.000 | 1.839×10⁻⁷ | **+8.081922×10⁻⁵** |

The floors (≤ 4.3×10⁻⁶) sit at or below the depth class
of the Phase 312 sibling pockets (10⁻⁷–10⁻⁵): a dip of
that class deeper than its regional floor could not have
hidden between mesh nodes, and every regional found
minimum exceeds its floor by ×60 (inner), ×61 (mid),
×440 (rim).

**Grade statement.** The certificate is: exact angular
reduction (a property of the split formula's structure,
verified numerically) × radial mesh Δr ≤ 0.01 (Δr = 0.001
on the rim window) with derivative-bounded floors. It is
an adversary-grade numerical certificate at that
resolution. It is NOT an analytic proof over the radial
continuum, and the claim set (§5) quotes it at exactly
this grade.

## §4. What this gate did not do

The other four confirmed pointwise members of Phase 314
were not under attack; their set reads stand as recorded,
neither quoted nor endorsed here. No spinor match was run
or judged — the supplier question for this target is the
parent's charge, untouched by this gate. The search
covers the posed shell [10, 20] only, at β = 1.1 with
(S, N) verbatim; nothing is said about any other member,
pose, or radius range. The gate repaired nothing.

## §5. The claim set — the only quotable form

Fence, carried in every claim: this member's SET EC reads
(SAMPLER-M) remain violated — NEC min −1.170007×10⁻³,
WEC min −1.044069×10⁻², DEC min −1.000003 — and its depth
is a negative NEC read. Every claim below is a DENSITY
statement about a target. None is a legality, energy-
condition, front, joint-pass, or drive statement.

- **G35-A — SURVIVES.** *Existence and stored values.*
  "The extended (three-function) class member with ramp
  M(r) = 1 + 4.00·[U(r; 9, 20.5) − U(r; 21, 24)] on the
  Gate-30 winner's (S, N) verbatim at β = 1.1 exists as
  posed, and its Phase 314 stored reads are confirmed by
  an independent symbolic-Einstein re-read (Gate-35 §2)
  at float64 round-off level: SET-244 ρ min
  +8.272455×10⁻⁵ (0/6642 negative), binding-site ρ_req
  ≥ +1.172278×10⁻⁴ at all four Phase 293-rule sites,
  SET EC reads as fenced above, Type-I count 2615/6642."
- **G35-B — SURVIVES RESTATED.** *Positivity, continuum
  form at adversary grade.* "For this member, ρ_req > 0
  throughout the closed posed volume r ∈ [10, 20], all
  directions — certified at adversary grade by Gate-35:
  exact angular reduction (ρ depends on direction only
  through n_x̂²) × radial mesh Δr ≤ 0.01 (Δr = 0.001 on
  [19.5, 20]) with derivative-bounded margin floors.
  Continuum minimum +8.100317×10⁻⁵ at r = 20 (the closed
  outer boundary; R1-carried, Q_K = 0 there); certified
  regional lower bounds: inner [10, 12.5] +2.547705×10⁻⁴
  (floor 4.257×10⁻⁶), mid [12.5, 17.5] +1.167761×10⁻⁴
  (floor 1.944×10⁻⁶), rim [17.5, 20] +8.081922×10⁻⁵
  (floor 1.839×10⁻⁷). This is an adversary-grade
  numerical certificate at the stated resolution, not an
  analytic proof. Phase 314's set-read form (SET-244 ρ
  min +8.272455×10⁻⁵) remains quotable as a set read;
  this restated form is the only continuum form."
- **G35-C — SURVIVES.** *Depth.* "The member's depth
  (SAMPLER-M, adversary-polished) is −5.327659×10⁻⁴,
  past the −0.0034 material bar by ×6.4 (gate re-read:
  −5.327658635240827×10⁻⁴, polish point r = 12.313487,
  Type-I, identical to stored). Depth is a negative NEC
  read: it is quoted as the target's depth, not as any
  legality property."

## §6. Reality Desk

`DESK: NO DATA CONTACT — Gate-35 re-judged Phase 314's
record against its own stored numbers and an independent
symbolic computation; no real-world dataset bears on a
density statement about a posed target, and none was
contacted.`

## §7. Artefacts

- Registration: `gate35/work/g35_registration.md`
- Item 1: `gate35/work/g35_rho.py`, `g35_item1.py`,
  `g35_item1_results.json`, `g35_item1_memo.md`
- Item 2: `gate35/work/g35_lib.py`, `g35_item2.py`,
  `g35_item2_results.json`, `g35_item2_memo.md`
- This record: `gate35/GATE35.md`; checkpoint:
  `gate35/CHECKPOINT_GATE35.md`

No ledger append, no launches, no publication, no
external contact was made by this gate.
