# GATE-35 REGISTRATION — ADVERSARIAL RE-JUDGEMENT OF PHASE 314'S POINTWISE MEMBER

Written before any gate computation. The gate writes its own
machinery and does not repair what it breaks.

## The claim under attack (Phase 314, stored record)

Headline member: ramp profile M(r) = 1 + 4.00·[U(r; 9, 20.5)
− U(r; 21, 24)] (U = quintic smoothstep), on the Gate-30
winner's (S, N) verbatim (WINNER_SPEC: plat, a=2, b=2,
A = 0.07439108177516472, c=15, W=5, e=3.0), β = 1.1, posed
shell r ∈ [10, 20]. Stored reads (phase314/results/
p314_results.json):

- SET-244 (41 radial midpoint nodes × 162 Fibonacci dirs,
  SAMPLER-M): ρ min **+8.272455×10⁻⁵**, 0/6642 negative,
  argmin r = 19.878 transverse; ρ median +2.722×10⁻⁴,
  max +8.831×10⁻⁴.
- Depth (SAMPLER-M, adversary-polished): **−5.327659×10⁻⁴**
  (bar −0.0034), polish site r = 12.3135, Type-I,
  ρ_t = +6.263×10⁻⁴.
- Binding sites (Phase 293 rule): S1 r=12.313 ρ +6.263182×10⁻⁴;
  S2 r=11.829 ρ +6.818808×10⁻⁴; S3 r=12.317 ρ +6.257630×10⁻⁴;
  S4 r=17.683 ρ +1.172278×10⁻⁴ (min site ρ). All ≥ 0.
- SET EC reads (SAMPLER-M): NEC min −1.170007×10⁻³,
  WEC min −1.044069×10⁻², DEC min −1.000003,
  SEC min −1.200683×10⁻². Type-I count 2615/6642.

Phase 314's own fence (§6 of its memo): "everywhere" is a
SET READ, quoted as a set read; no continuum claim was made.
This gate exists to decide whether the continuum upgrade is
earned, and to re-read the member independently.

## Standing quoting rules applied

- SET-READ QUOTING (Phase 204 X5): stored finite-set maxima/
  minima are set reads; continuum statements require a
  legality-restricted adversary read or a Gate.
- MARGIN-FLOOR QUOTING (Phases 216/219): adversary numbers
  quote their margin floor.

## ITEM 1 — SET READ → CONTINUUM (deciding item)

Legality-restricted adversary search over the headline
member's posed volume (closed shell r ∈ [10, 20], all
directions) for any locus with ρ_req < 0 OFF the SET-244
grid. Registered protocol elements:

(a) The gate's own ρ evaluator, implemented fresh from the
    Phase 308 split (16πρ_req = R(γ) + Q_K; R = R1 + R2
    direction-free; Q_K as printed in CHECKPOINT308),
    validated by controls (below) BEFORE any search read
    is quoted.
(b) Structural reduction, to be verified numerically by
    the worker before use: ρ depends on the direction
    only through u = n_x̂² ∈ [0, 1] (axisymmetry about the
    shift axis; R direction-free; Q_K affine in u in its
    numerator pieces; α² affine in u). If verified, the
    angular minimum at fixed r is computed EXACTLY
    (1-D minimisation over u of the closed form), and the
    continuum problem reduces to the 1-D radial function
    ρ*(r) = min_u ρ(r, u). If the reduction fails
    verification, the worker falls back to dense
    (r × direction) sampling at ≥ 4× SET-244 density in
    the near-zero regions plus a full-volume coarse pass,
    and says so.
(c) Radial adversary: fine mesh over [10, 20] (target
    Δr ≤ 0.01, i.e. ≥ 25× the SET radial spacing in node
    count) + local optimisation of ρ*(r) seeded from
    every mesh local minimum and from the analytic seed
    loci: the grid argmin region (rim, r ≈ 19.878,
    transverse), the radii where S′ peaks with u = 0
    (Q_K term-1 bite), the profile transition zones
    (rise top r → 20.5 approached from inside the volume;
    M′′ sign change mid-rise), both closed boundaries
    r = 10 and r = 20 exactly.
(d) MARGIN FLOOR, quoted per region (inner [10, 12.5],
    mid [12.5, 17.5], rim [17.5, 20]): the certified
    continuum lower bound per region = (found regional
    minimum of ρ*) − (regional floor), with the floor
    derived from a stated bound on |dρ*/dr| over the
    region (analytic derivative of the closed form, or
    FD-verified envelope) times the regional mesh
    half-spacing, tightened wherever the optimiser has
    polished the regional minimum to a stationary point.
    The floor is the smallest |ρ| dip the search could
    have missed at its resolution, per region.

VERDICTS (registered):
- CONTINUUM-CLEAN AT ADVERSARY GRADE — no negative locus;
  certified lower bound > 0 in every region. The
  positivity becomes quotable as a continuum statement AT
  THAT GRADE, with grade + floors carried in the claim.
- POCKET FOUND — locus + depth reported; the claim falls
  back to the set read, restated by the gate (Item 3).
- SEARCH-GRADE INSUFFICIENT — the certified bound does
  not decide some region; the deciding refinement is
  named exactly.

## ITEM 2 — INDEPENDENT RE-READ

The member re-read with the gate's OWN assembly — no
import of p312_lib / p314_lib / p308_lib for the tensor
or ρ computation. (Programme base layer is permitted:
numpy/scipy; p258_lib shape/grid primitives S_ab,
R_NODES, DIRS162; verify_metric frame utilities;
p2352_run SAMPLER-M margins — these define the pose and
the sampler, not the extended-class assembly.) The
assembly path must differ in kind from p312_lib's: e.g.
a symbolic (sympy) Einstein-tensor computation from the
spherical line element with radial shift, lambdified, with
the Eulerian frame transform applied — or an equivalent
independent derivation. Reads: depth (gate's own
adversary polish of SAMPLER-M NEC, protocol form as
registered in p314_common.pick_sites), the four binding
sites under Phase 293's rule, per-site ρ_req (tensor and
split cross-check), EC reads over SET-244 (SAMPLER-M;
exact pointwise NEC minimum at the Type-I sites named).
Differences from the stored record reported at BOTH
values wherever they differ.

## CONTROLS (before any re-judgement read is quoted)

- C-G1 (evaluator vs stored splits): the gate's ρ
  evaluator reproduces the stored per-site split values
  (R1, R2, Q_K, ρ_req at S1–S4, from p314_results.json)
  to ≤ 1×10⁻⁹ relative (or the discrepancy is reported
  and resolved before proceeding).
- C-G2 (M ≡ 1 reduction): the gate's assembly at M ≡ 1
  reproduces the stored two-function control values
  (Phase 312 C1: depth −0.001386956608122417, SET NEC min
  −0.004079744835667814, Type-I count 1245 exact, polish
  r 12.369476376022238, four site ρ_req vs p312 stored)
  at the tolerances those records carry.
- C-G3 (headline set reproduction): the gate's assembly
  reproduces the stored headline SET reads (ρ min
  +8.272455×10⁻⁵ with argmin locus, NEC/WEC/DEC minima,
  Type-I count 2615) before its own reads are quoted;
  differences reported at both values.

## ITEM 3 — THE CLAIM SET (coordinator, after Items 1–2)

Per-claim verdicts SURVIVES / SURVIVES RESTATED / FAILS
for: (i) the member's existence and stored values;
(ii) its positivity — at Item 1's certified scope only;
(iii) its depth. The quotable set carries the EC fence
VERBATIM in substance: the member's NEC/WEC/DEC reads
remain violated at the stated values — the claim is a
density statement about a target, never a legality or
front statement.

## Scope fences

Verdicts bind the headline member only, on the posed
shell [10, 20], β = 1.1, (S, N) verbatim. The other four
confirmed pointwise members are NOT under attack in this
gate (their set reads stand as Phase 314 recorded them,
unquoted by this gate either way). No spinor match is
run or judged. DESK: one-line summary in the deliverable.

No ledger append, no launches, no publication, no user
contact.
