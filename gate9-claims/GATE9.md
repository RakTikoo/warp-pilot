# Novelty & Verification Gate 9 — GATE9.md (ground record)

**Status:** COMPLETE (pre-registered 2026-11-22 before any
Gate-9 run; all four workers returned; all four claims
verdicted — verdicts and closing synthesis at the end of
this file). All four claims REPRODUCED on independent
second paths; novelty PARTIALLY KNOWN ×4; gate verdict
UPLOAD-READY AFTER RESTATEMENT ×4. Nothing uploaded.
**Work dir:** `~/workspace/warp-pilot/gate9/` — verifier code,
search logs and memos in this dir and `results/`.
**Parent records:** `../gate7/GATE7.md`, `../gate8/GATE8.md`
(method — this gate follows Gates 5–8 exactly),
`../phase38/CHECKPOINT38.md` (P38-1/P38-2/P38-3),
`../phase61/CHECKPOINT61.md` (P61-1/P61-4),
`../phase71/CHECKPOINT71.md` (P71-1/P71-2),
`../NEW_PHYSICS_LEDGER.md` (the conformal row's current
UNDER ATTACK wording, ledger line 110 — read before any
claim language below).
**This gate prepares verdicts only. It uploads NOTHING,
contacts no one, and edits no phase record and no ledger.**
The ledger edit is PROPOSED at the end of this file, not
applied.

## The ruling this gate implements

Rakshit (2026-11-22): "Verify everything and tell honestly
what you found" + the Uniqueness Protocol (2026-11-22
~05:13 PT). Scope: the four claims below — the conformal
(Weyl) gravity joining member's legality, join, stability
and formation (Phases 38/61/71). Until this gate closes, the
member remains **"scan signal under attack"** in the
programme's locked language, and the conformal row remains
UNDER ATTACK in the ledger.

## Standards (identical to Gates 5–8)

float64 everywhere (40-digit mpmath where the phases used
it). Hedges intact. A NOVEL verdict requires the search to
be DOCUMENTED (queries verbatim + sources checked), never
asserted. Verdict categories per axis:
- Novelty: **NOVEL** / **PARTIALLY KNOWN** (exact known part
  cited) / **KNOWN** (cited — claim dies as "ours").
- Correctness: **REPRODUCED** (independent second path,
  within the margins/tolerances registered below) /
  **REPRODUCED WITH RESTATEMENT** (survives only weakened —
  exact restated wording supplied) / **NOT REPRODUCED**
  (second path disagrees — full anatomy required).
GATE VERDICT per claim: **UPLOAD-READY** /
**UPLOAD-READY AFTER RESTATEMENT** (restated form supplied)
/ **NOT YET** / **DEAD AS OURS** (KNOWN or NOT REPRODUCED).

**Uniqueness Protocol (binding, as amended into Gate-7):**
no claim may be worded "unique", "first", "record" or
"novel" outright unless (a) it beats the best verified mark
in its EXACT category (not applicable here — no speed claim
is in this set), (b) independent second-path reproduction
inside this gate, (c) the novelty search log is complete
with queries verbatim AND coverage gaps stated, (d) the
claim's category and scope are stated in the wording
itself. Otherwise the wording is "not found in our search
(limits: …)" or "scan signal under attack". These claims
are NOT expected to meet the outright bar; PARTIALLY KNOWN
/ not-found-in-our-search strength is the expected landing.

## The (V-b) clause (binding verbatim rider)

The following sentence, verbatim as carried in the phase
record (Phase 38 checkpoint; Phase 71 results/p711_memo.md),
must appear **verbatim** in every restated wording this
gate produces, and no gate language may soften it:

**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## Carried facts (never separated from the claims)

- The joining member's **tidal-bar radius r₀\* = 4.785×10⁷ m**
  (Phase 61 P61-1; static-radial-decided; worse than T-b's
  6.802×10⁶ m) rides with G9-1/G9-2/G9-3 in every wording.
- The member's **formation standing is PRE-EXISTING ONLY**
  (G9-4) and rides with the claim set as a whole.
- **C12 accounting:** this is a throat OBJECT claim set. No
  transport is claimed; no traversability is claimed; the
  word "traversable" may appear only in negations. The
  scored gauge is Ω = 1 (minimal-coupling metric), the
  Bach normalisation is 4α_g·B_μν = T_μν, conventions −+++,
  α_g > 0 (Phase 32 registrations, unchanged).

## Protocol (pre-registered, per claim, BEFORE any gate run)

NOVELTY: systematic arXiv + INSPIRE-HEP + Semantic Scholar
+ general web search for the claim's exact statement and
near neighbours; every query logged verbatim with the
sources actually checked and the date; near neighbours
cited by arXiv ID / DOI / stable URL; the novel part (if
any) delimited in one quotable sentence. **Coverage gaps
stated plainly** (e.g. if INSPIRE or Semantic Scholar is
reachable only via indexes, the report says so in those
words). A search that could not be run is a gap, not a
negative result.

CORRECTNESS: independent second path — reimplement the
deciding computation FROM THE CLAIM STATEMENT (fresh code
in `gate9/`, not a re-run of a phase script; shared
*definitions* — the profile forms, the BDE junction
formalism, the Galerkin method description, the Class-B
read-off definition — may be imported as text, the deciding
machinery may not). Reproduction = same signs and values
within the tolerances registered per claim below. Anchors
must pass BEFORE any claim number is read; a failed anchor
stops the item as a machinery failure, not a claim failure.

OPTIMISATION DIRECTIVE + RIDER (standing): verification
runs as unattended scripts; pass/fail computed by checker
scripts over result files; offloading never trades quality,
speed or breadth.

## The four claims (exact statements as tasked)

The member: static spherical throat in conformal (Weyl)
gravity, Ω = 1, b(r) = r₀(r/r₀)^p with **p = 0.1**, redshift
profile **Φ₂ = a·ln(r/r₀)/(1 + ln(r/r₀))** with
**a = 0.277734**, scored on [r₀, 10³ r₀], r₀ = 1 units
unless stated. (The legal locus segment is p ∈ [0.1,
0.10120) at a = a_zero(p); the audited point is its
registered representative.)

- **G9-1 LEGALITY (P38-1 region + P61-1 audited point).**
  The member is EC-legal on its whole interior domain: with
  T = 4α_g·B, α_g > 0, all four ECs hold strictly on
  [r₀, 10³ r₀], all directions. Stored deciding values
  (B-combinations, per P61-1's convention; P71-2's G1 gate
  re-read them): throat **NEC1 = +0.00364119103852**,
  **DEC_t = +0.00182059551926**; tail minima > 0 at 40
  digits on the whole domain (P61-1 adversarial protocol).
  Records: `../phase61/results/p611_memo.md`,
  `p611_ecaudit.json`, `../phase71/results/p712_memo.md` §G1.
- **G9-2 THE JOIN (P61-1).** At r_Σ = 10³ r₀ the member
  joins the Mannheim–Kazanas exterior at the registered
  galactic γ = 10⁻²⁸ m⁻¹ under the published
  Berezin–Dokuchaev–Eroshenko conditions
  (arXiv:1710.10438 §III.B): **[R̃] = 0** (40-digit mpmath
  second path 0.0; symbolic path agrees < 10⁻⁹),
  [R̃_,n] = **−0.0152186**, and the shell the formalism
  fixes, Ŝ₀⁰ = −(4α₀/3)[R̃_,n] = **+0.020291 α₀ ≥ 0**, is
  LEGAL. Darmois-matched exterior: **β_MK = 2.142611 r₀**,
  **k = −2.28996×10⁻⁹ r₀⁻²**. (α₀ = α_g/2, BDE eq. (57)
  mapping.) At both primary radii (10, 10² r₀) NO member of
  the region joins; on the Φ = 0 slice
  [R̃] = (1 + p)(r₀/r_Σ)^{1−p} > 0 exactly. Records:
  `../phase61/results/p611_memo.md`, `p611_junction_raw.json`,
  `p611_locus_ledger.json`.
- **G9-3 STABILITY (P71-1).** The member's interior
  background is CLASSICALLY STABLE in the computable
  sectors: exact static ℓ=0 clean (linearised-Bach traces
  ≤ 2.9×10⁻¹² float64; ≤ 5.7×10⁻³¹ at 40-digit probes at 6
  radii); dynamic ℓ=0 Galerkin quotient spectrum — no zero
  crossing anywhere in ω² ∈ [−5, 0) (2001 points × profiles
  P1/P2 × R ∈ {10, 20, 30} × both extractions), smallest
  physical eigenvalue **≥ 0.00121741** (P2 averaged;
  P1 ≥ 0.00424541), R-independent in the P38-2 sense;
  principal symbol in all ℓ = double light cone, no
  tachyon/gradient branch. REGISTERED SCOPE: interior
  sectors only — the shell/exterior perturbation problem is
  OPEN (not computed); ℓ ≥ 1 long-wavelength and nonlinear
  stability not computable (P38-2 obstructions); the
  dynamic read is Galerkin/variational, NOT an exact
  spectrum; the packet numeric sign check remains OPEN
  (P38-2's named follow-up). Records:
  `../phase71/results/p711_memo.md`, `p711_results.json`,
  `p711_dyn_raw.json`, `p711_static.json`, `p711_mp40.json`;
  method parent `../phase38/results/p382_memo.md`.
- **G9-4 FORMATION (P61-4 + P71-2).** The member's
  formation standing is PRE-EXISTING ONLY: (i) growth is
  GROWABLE-ONLY-EXOTICALLY — the frozen family is EC-legal
  at all 8 ladder radii (1 m → 4.785×10⁷ m, scale
  covariance T = r₀⁻⁴F(r/r₀)); the common-domain increment
  fails NEC1/DEC_r/DEC_t only in a thin inner layer
  x_b ∈ [1, 1.00348] (ΔNEC1 = **−0.016680 r₀_{j+1}⁻⁴**,
  scale-free), priced at **5.83×10⁶⁸ × E_legal per decade
  step**; and the grown shell (Phase-30 Class-B read-off)
  is SINGULAR — Φ₂ has a pole at x_b = e⁻¹ where all ECs
  diverge (40-digit probes NEC1 = **−6.58×10²¹** at
  e⁻¹(1−10⁻³), **−6.65×10⁴²** at e⁻¹(1−10⁻⁶); pole order
  ≈ 7, non-integrable; NEC1 < 0 already at x_b = 0.99) —
  so the shell price per decade step is UNBOUNDED (lower
  bounds ≥ **6.925×10⁸⁴** × E_legal at pole-exclusion
  ε = 10⁻², ≥ **7.327×10⁹⁰** at 10⁻³, ≥ **1.711×10⁹⁶** at
  10⁻⁴), against T-b's finite 2.216×10⁷³ (P61-4); (ii)
  nucleation is CLOSED as a property of the theory's home:
  P61-4's conformally-flat fork (the only Euclidean
  wormholes on record are conformally flat shapes on which
  this theory's action is exactly zero; the conformal
  instantons that exist are vacuum-tunnelling saddles with
  no throat), inherited by the Φ₂ member by argued
  inheritance (P71-2: every fork premise quantifies over
  the home, none mentions T-b's (b, Φ)). Dynamic growth
  read: UNCOMPUTED for this member (P71-2, FU-P712-1) —
  carried, not hidden. Records:
  `../phase71/results/p712_memo.md`, `p712_results.json`;
  `../phase61/results/p614_memo.md`, `p614_results.json`.

## Registered correctness paths and bars

### Shared fresh engine (G9-1; used by G9-4 under Gate-7 precedent)

A fresh symbolic derivation of the Bach tensor for the
static spherical ansatz ds² = −e^{2Φ(r)}dt² +
(1 − b(r)/r)⁻¹dr² + r²dΩ², from the metric, in `gate9/`
(SymPy), giving B^t_t, B^r_r, B^θ_θ as exact functions of
(b, Φ) and derivatives; EC combinations formed from
T = 4α_g·B with α_g = 1 (signs are α_g-scale-free for
α_g > 0). The stored deciding values are B-combinations
(P61-1 convention): the worker evaluates BOTH the
B-combinations and the T-combinations and compares the
B-combinations to the stored numbers.
ANCHORS (before any claim number): (i) Schwarzschild and
MK-ansatz Bach-flatness: B ≡ 0 symbolically; (ii) T-b
(p = 1/2, Φ = 0) reproduces Phase 32's closed-form EC
combinations (signs and stored throat values, from
`../phase32/results/p323_memo.md`); (iii) the Φ = 0 slice
identities DEC_r = NEC1, DEC_t = NEC2, SEC = 2ρ hold
symbolically, and NEC1 ∝ (1 − 3p + 2pq), q = r^{1−p}
(P38-1's factorisation) is reproduced.

### G9-1 bars

Deciding set: [r₀, 10³ r₀], float64 grid ≥ 2000 log-spaced
points PLUS 40-digit mpmath probes at the throat and at
the stored tail-minimum radii (`p611_ecaudit.json`).
REPRODUCED iff: (a) all six combinations (ρ, NEC1 = ρ+p_r,
NEC2 = ρ+p_t, DEC_r = ρ−p_r, DEC_t = ρ−p_t,
SEC = ρ+p_r+2p_t, in B-combination form) are > 0 at every
grid point and probe; (b) throat NEC1 and DEC_t agree with
the stored values within 2%. Sign agreement with a miss on
(b) = REPRODUCED WITH RESTATEMENT (gate numbers replace
the phase's). Any (a) failure = NOT REPRODUCED, with full
anatomy (site, deciding combination, 40-digit tie-break at
the site run before the verdict is final).

### G9-2 bars

Fresh computation of the conformal 2-scalar R̃ from the
BDE printed definitions (arXiv:1710.10438 §III.B), for the
interior (b, Φ) family and the MK exterior; Darmois
matching at r_Σ; shell datum Ŝ₀⁰ = −(4α₀/3)[R̃_,n].
ANCHORS (before the member's number): (i) R̃(flat) = −2;
(ii) T-b reproduces P38-3's stored [R̃] = +0.474342
(r_Σ = 10 r₀) and +0.150000 (10² r₀) within 0.1%, with the
Darmois pair (β_MK, k) = ((1/3)√(r_Σ r₀), β_MK/r_Σ³);
(iii) the Φ = 0 slice identity [R̃] = (1 + p)(r₀/r_Σ)^{1−p}
reproduced symbolically.
REPRODUCED iff at r_Σ = 10³ r₀ for the audited point:
(a) β_MK = 2.142611 r₀ within 1% and k = −2.28996×10⁻⁹ r₀⁻²
within 2% (γ = 10⁻²⁸ m⁻¹ carried as registered; the worker
states how γ enters the matching algebra); (b) [R̃] = 0 at
40 digits (|R̃| < 10⁻²⁰) or by exact symbolic cancellation
(< 10⁻⁹ float64); (c) [R̃_,n] = −0.0152186 within 2%;
(d) Ŝ₀⁰ = +0.020291 α₀ within 2% with sign exactly
positive. Misses on magnitudes with signs and the zero
intact = REPRODUCED WITH RESTATEMENT; [R̃] ≠ 0 beyond the
registered precision, or Ŝ₀⁰ < 0 = NOT REPRODUCED (anatomy
required).

### G9-3 bars

Fresh implementation of the P38-2/P71-1 method (the method
description in `p382_memo.md`/`p711_memo.md` is a shared
definition; all code fresh in `gate9/`).
MACHINERY RE-GATE on T-b (before any member number): the
fresh quotient implementation reproduces T-b's smallest
physical eigenvalues P1 = 0.00265284 / P2 = 0.00087671
(R = 10; P71-1's re-run values, consistent with P38-2's
stored 0.00265 / 0.000877) within 5%, and finds no zero
crossing on T-b; the gauge anatomy (det M ≡ 0, null vector
(1,1,1)) is verified structurally on T-b. A failed re-gate
stops the item as a machinery failure.
REPRODUCED iff on the member: (a) static sector —
linearised-Bach traces at 40-digit probes at ≥ 6 radii are
consistent with zero (|trace| < 10⁻²⁵ at 40 digits; the
stored read is ≤ 5.7×10⁻³¹), via a fresh static derivation
(may share the G9-1 symbolic pattern only if independently
anchor-validated per Gate-7 precedent); (b) dynamic sector
— no zero crossing in ω² ∈ [−5, 0) on the registered grid
(2001 points × P1/P2 × R ∈ {10, 20, 30} × both extraction
conventions, or a stated equivalent registered before
running), smallest physical eigenvalue > 0 with the
P2-averaged value within a factor 2 of 0.00121741 and the
P1 value within a factor 2 of 0.00424541; (c) symbol — the
double-light-cone principal symbol verified by exact
algebra on a generic background point, or the P71-1
transfer argument's premises each checked on the member
with the controlling computation (P61-3's flat quotient
spectrum) re-derived independently. Any zero crossing or
negative physical eigenvalue on the fresh path = NOT
REPRODUCED (anatomy: profile, R, extraction, eigenvalue).

### G9-4 bars

(a) FROZEN + COVARIANCE: the member's EC set at r₀ = 1 is
G9-1's deciding read (shared, anchor-validated); scale
covariance verified independently by direct evaluation at
r₀ = 10 and r₀ = 10³ (matched x = r/r₀; relative deviation
of the EC combinations < 10⁻⁹), from which legality at all
8 ladder radii follows in the phase's stated form.
(b) INCREMENT: fresh Class-B read-off implementation (the
read-off definition from `p712_memo.md`/`p614_memo.md` is
shared text; code fresh): the common-domain increment's
failures confined to x_b ∈ [1, 1.00348] (endpoints within
5%) with ΔNEC1 min = −0.016680 r₀_{j+1}⁻⁴ within 5%; the
per-decade price 5.83×10⁶⁸ × E_legal reproduced within a
factor 2, with E_legal re-derived from the P61-4 record.
(c) POLE: Φ₂'s pole at exactly x_b = e⁻¹ shown
analytically (1 + ln x_b = 0); 40-digit NEC1 probes at
e⁻¹(1−10⁻³) and e⁻¹(1−10⁻⁶) negative and within a factor 3
of −6.58×10²¹ / −6.65×10⁴²; pole order 7 ± 1 by log-log
fit; price lower bounds at ε = 10⁻²/10⁻³/10⁻⁴ each within
a factor 10 of 6.925×10⁸⁴ / 7.327×10⁹⁰ / 1.711×10⁹⁶
× E_legal and strictly increasing as ε → 0 (the deciding
content is UNBOUNDED, not the digits).
(d) NUCLEATION INHERITANCE (document audit): every premise
of P61-4's fork (from `p614_memo.md`) listed verbatim in
substance and checked to quantify over the theory's home
(action/Euclidean sector/RW geometry/Bach equation), none
mentioning T-b's (b, Φ); PLUS a fresh symbolic check that
B ≡ 0 on a general Robertson–Walker metric (the
conformally-flat clause). Inheritance fails if any premise
is member- or T-b-specific (named).
REPRODUCED iff (a)–(d) all hold; partial failures are
restated clause-by-clause (the formation claim is a
conjunction of separately-scored clauses).

## Worker assignments

- W-A: G9-1 (legality; the shared fresh engine) →
  `results/wA_g9_1.md`; fresh code `gate9/wa_*.py`;
  numbers `results/wa_g91_numbers.json`; search log
  `results/wa_search_log.md`.
- W-B: G9-2 (the join) → `results/wB_g9_2.md`; fresh code
  `gate9/wb_*.py`; numbers `results/wb_g92_numbers.json`;
  search log `results/wb_search_log.md`.
- W-C: G9-3 (stability) → `results/wC_g9_3.md`; fresh code
  `gate9/wc_*.py`; numbers `results/wc_g93_numbers.json`;
  search log `results/wc_search_log.md`.
- W-D: G9-4 (formation) → `results/wD_g9_4.md`; fresh code
  `gate9/wd_*.py`; numbers `results/wd_g94_numbers.json`;
  search log `results/wd_search_log.md`.

Each worker: correctness FIRST (fresh code in `gate9/`,
run with the programme venv `~/workspace/warp-pilot/venv/bin/python`
— state it), then novelty with logged queries. Each
returns per claim: correctness verdict + deciding numbers
from THEIR run; novelty verdict + citations + coverage
gaps; and, wherever the claim survives only weakened, the
EXACT restated wording — which must carry the (V-b)
sentence verbatim (above), the tidal bar and
pre-existing-only standing where they belong, and the C12
accounting. Workers do not edit this file; the coordinator
integrates verdicts from the worker reports +
checker-verified result JSONs.

## Status log

- 2026-11-22: gate opened by coordinator; ground records
  read (GATE7.md + GATE8.md in full; CHECKPOINT38 P38-1/2/3;
  CHECKPOINT61 closure summary P61-1/P61-4; CHECKPOINT71
  closure summary P71-1/P71-2; ledger conformal row, line
  110). Protocol pre-registered above BEFORE any Gate-9
  number was computed. Workers dispatched in parallel:
  W-A = G9-1, W-B = G9-2, W-C = G9-3, W-D = G9-4.

## Verdicts

### G9-1 — Legality of the joining member (W-A, 2026-11-22)

Full report: `results/wA_g9_1.md`; fresh code `wa_engine.py`
(full Christoffel→Riemann→Ricci→Weyl→double-covariant-
divergence SymPy derivation; no phase script imported),
`wa_anchors.py`, `wa_phi0.py`, `wa_member.py`,
`wa_probes.py`, `wa_checker.py`; numbers
`results/wa_g91_numbers.json`; search log
`results/wa_search_log.md`. Programme venv, float64 +
50-digit probes. All three anchors passed before any claim
number (Schwarzschild B ≡ 0 symbolically; MK max |B| =
1.3×10⁻¹⁶⁹; T-b closed forms reproduced with 50-digit
diffs exactly 0.0; Φ = 0 factorisation reproduced, max rel
err 1.8×10⁻¹³). Two machinery findings on the way, both
caught by the anchors: ∇C must be formed for all index
patterns (the sparse version failed Schwarzschild), and the
registered Bach convention is B = 2∇∇C + R·C (the naive
∇∇C + ½R·C bracket is exactly half of it, ratio 0.500 at
every T-b point/component — erratum 3 below).

- **Correctness: REPRODUCED.** On the deciding set (2,500-
  point float64 grid on [1, 1000] + high-digit probes) all
  six B-combinations are > 0 everywhere (bar (a) PASS,
  checker-recomputed): grid minima all at the tail r = 1000
  and matching the stored tail minima to ~9 digits
  (ρ 6.275140592×10⁻¹⁵, NEC1 1.229852039×10⁻¹⁵,
  NEC2 1.193535517×10⁻¹⁴, DEC_r = NEC1,
  DEC_t 6.149260195×10⁻¹⁶, SEC 1.255028118×10⁻¹⁴).
  Throat (bar (b)): NEC1 = 0.00364086750048,
  DEC_t = 0.00182043375024 — within 8.9×10⁻⁵ relative of
  the stored +0.00364119103852 / +0.00182059551926 (bar
  2%). The residual is an a-rounding sensitivity inside
  the phase record: the stored digits correspond to
  a = 0.27773424114865775 (W-B's bisection value), and at
  that a the gate path's limit matches the Phase-38 throat
  formula digit-for-digit (erratum 2 below). No
  restatement of the claim's numbers is needed.
- **Novelty: PARTIALLY KNOWN.** Known part: EC
  satisfaction near a conformal-gravity wormhole throat is
  published — Lobo, arXiv:0801.4401 (CQG 25 175006, DOI
  10.1088/0264-9381/25/17/175006; "in the vicinity of the
  throat") and Varieschi & Ault, arXiv:1510.05054 (legal
  only for r ≲ 1.03–1.10 r₀, junction exotic matter
  beyond). Not found in the search: whole-domain legality
  to 10³ r₀ for T = 4α_g·B (α_g > 0); the Φ = 0 power-law
  family or its NEC1 ∝ (1 − 3p + 2pq) factorisation; the
  Φ₂ profile used for any conformal-gravity wormhole; any
  40-digit Bach throat-legality audit. Coverage gaps
  (stated plainly by the worker): arXiv checked natively;
  INSPIRE-HEP and Semantic Scholar checked only via the
  general web index, not their native interfaces.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** — the
  restatement is on the novelty axis only; the claim's
  numbers stand as claimed. Exact restated wording in
  `results/wA_g9_1.md` ("Exact restated wording"), carrying
  the (V-b) sentence verbatim, r₀* = 4.785×10⁷ m,
  PRE-EXISTING ONLY, C12 object accounting, and the
  limits-named not-found strength.

### G9-2 — The join (W-B, 2026-11-22)

Full report: `results/wB_g9_2.md`; fresh code `wb_g92.py`
(fresh SymPy derivation of R̃ from the BDE
arXiv:1710.10438 §III.B printed definitions; 40-digit
mpmath, analytic derivatives only), `wb_checker.py`
(12/12 PASS); numbers `results/wb_g92_numbers.json`;
search log `results/wb_search_log.md`. All three anchors
passed before the member's number: R̃(flat) = −2.0
exactly; T-b [R̃] = +0.474341649 at 10 r₀ (rel err
7.4×10⁻⁷ vs stored +0.474342) and +0.150000000 at 10² r₀
with the stored Darmois pair; the Φ = 0 slice identity
reproduced symbolically exactly (R̃_int = (3−p)r^{p−1} − 2,
[R̃] = (1 + p)(r₀/r_Σ)^{1−p}).

- **Correctness: REPRODUCED.** At r_Σ = 10³ r₀, audited
  point (worker's own bisection a_zero =
  0.27773424114866288, 5.1×10⁻¹⁵ from the stored a):
  β_MK = 2.142610720 r₀ (stored 2.142611; rel err
  1.3×10⁻⁷, bar 1%); k = −2.28995912×10⁻⁹ r₀⁻² (stored
  −2.28996×10⁻⁹; rel err 3.8×10⁻⁷, bar 2%);
  **[R̃] = −2.4×10⁻³⁹** (bar |R̃| < 10⁻²⁰);
  [R̃_,n] = −0.0153171 (stored −0.0152186; 0.65%, bar 2%);
  **Ŝ₀⁰ = +0.0204229 α₀** (stored +0.020291 α₀; 0.65%,
  sign exactly positive) — LEGAL shell. The registered γ
  is carried as registered and is numerically inert at
  this radius (γ = 0 changes β_MK by 7.7×10⁻²⁴ relative).
  Scope confirmed on the gate path: the same interior at
  10 / 10² r₀ gives [R̃] = +0.115542 / +0.011505 — no join
  at the primary radii, as claimed.
- **Novelty: PARTIALLY KNOWN.** Known: the BDE formalism
  itself (arXiv:1710.10438); conformal wormhole interiors
  with MK matching mentioned but without BDE conditions
  (Lobo arXiv:0801.4401); fourth-order conformal wormholes
  with the junction left possibly exotic (Varieschi
  arXiv:1510.05054); two-MKdS thin-shell wormholes
  (arXiv:1301.1532); vacuum conformal wormholes
  (arXiv:1802.02184). Not found: the specific BDE
  [R̃] = 0 join of this EC-legal interior to registered-γ
  MK at 10³ r₀ with Ŝ₀⁰ ≥ 0. Coverage gaps (stated
  plainly): INSPIRE-HEP and Semantic Scholar reached only
  via indexes/mirrors — no direct database/API query;
  paywalled/non-English literature not exhaustive.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** —
  exact restated wording in `results/wB_g9_2.md` ("Exact
  restated wording (G9-2)"), carrying the (V-b) sentence
  verbatim, the extension-radius-only scope, the
  registered γ, r₀* = 4.785×10⁷ m, PRE-EXISTING ONLY, C12
  object accounting, the no-ADM-mass read, and the
  limits-named not-found strength. (The wording quotes
  the claim's stored [R̃_,n]/Ŝ₀⁰ values, reproduced by the
  gate path within the registered 2% bar, per Gate-8
  precedent.)

### G9-3 — Stability (W-C, 2026-11-22)

Full report: `results/wC_g9_3.md`; fresh code `wc_symq.py`,
`wc_dyn.py`, `wc_bach5.py`, `wc_static.py`, `wc_symbol.py`,
`wc_checker.py` (20/20 PASS over the worker's numbers);
numbers `results/wc_g93_numbers.json`; search log
`results/wc_search_log.md`. MACHINERY RE-GATE on T-b
passed before any member number (fresh symbolic Weyl²
density + fresh Galerkin code): P1 R = 10 averaged =
0.0026528417913793652 (stored 0.00265284), P2 R = 10 =
0.000876709357515032 (stored 0.00087671) — agreement to
every printed digit (~10⁻⁷ relative vs the 5% bar); no
T-b crossing; gauge anatomy structural (max |det M|
3.1×10⁻⁹, row-sum residuals ≤ 1.0×10⁻⁸, alignment
≥ 0.99999999999993; no bare determinant read).

- **Correctness: REPRODUCED.** (a) Static sector: fresh
  jet-space Bach implementation in the Ricci form
  (arXiv:2505.17171 eq. 6), anchor-validated (T-b
  closed-form ratio 1.0000000000000000, control err
  9.9×10⁻¹⁵; member background B to 2.7×10⁻¹⁴ vs stored);
  40-digit traces at 6 radii: **max |trace| = 3.13×10⁻³⁴**
  (bar < 10⁻²⁵; stored ≤ 5.7×10⁻³¹). (b) Dynamic sector:
  no zero crossing and zero negative points in all 12
  blocks (2001 points × P1/P2 × R ∈ {10, 20, 30} × both
  extractions); smallest physical eigenvalue P2 averaged
  R = 10 = **0.0012174053847267233** (stored 0.00121741 —
  ratio 1.0000, bar factor 2), P1 = **0.004245411313722145**
  (stored 0.00424541). (c) Symbol: P61-3's flat quotient
  spectrum independently re-derived exactly (5 gauge
  directions symbolically null; rank 5 off-cone; physical
  eigenvalues ∝ (ω² − k²)² with the same Q¹⁰
  quotient-determinant factorisation and sign as P61-3's
  −Q¹⁰/24 in the worker's normalisation); double light
  cone, no tachyon or c² ≠ 1 branch; the transfer
  argument's non-degeneracy premises checked on the
  member. Failure ledger (recorded, Gate-7/8 style): the
  worker's first Weyl-form Bach assemblies failed the T-b
  anchor twice (a skipped-component bug, anatomised and
  fixed; then a ∇∇C assembly error no sign/placement
  combination cured, spread 2.28) — that instrument was
  DISCARDED and no number from it is used; the deciding
  static read is the Ricci-form implementation, which
  passes every anchor exactly. One concrete-function
  variant test was lost to CPU contention with no number
  used.
- **Novelty: PARTIALLY KNOWN.** Known: linear-perturbation
  stability of conformal-gravity wormholes of a DIFFERENT
  class is published — Cadoni, Modesto, Pitzalis & Sanna,
  arXiv:2503.14214, JCAP 06 (2025) 016 (Weyl-rescaled-
  Minkowski / conformal scalar–tensor; different background
  and method). Not found: this member's linearised-Bach
  stability computation (quotient spectrum on a
  Morris–Thorne background in pure Weyl gravity).
  Coverage gaps (stated plainly): INSPIRE-HEP / Semantic
  Scholar via web indexes only; no exhaustive arXiv
  listing-API sweep.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** —
  exact restated wording in `results/wC_g9_3.md` §8,
  carrying the (V-b) sentence verbatim, the FULL
  registered scope (interior sectors only; shell/exterior
  perturbations OPEN; Galerkin ≠ exact spectrum; packet
  check OPEN; no positive conserved energy + IVP
  unproven as recorded facts), r₀* = 4.785×10⁷ m,
  PRE-EXISTING ONLY, C12 object accounting. Note: the
  worker's wording retains the sentence "The member
  remains a scan signal under attack — nothing stronger"
  (erratum 4 below).

### G9-4 — Formation (W-D, 2026-11-22)

Full report: `results/wD_g9_4.md`; fresh code
`wd_derive.py` (own Ricci-form Bach derivation; W-A's
engine was not used), `wd_audit.py`, `wd_rw.py`,
`wd_rw_trig.py`, `wd_assemble.py`, `wd_checker.py`
(16/16 PASS); numbers `results/wd_g94_numbers.json`;
search log `results/wd_search_log.md`. The worker's own
engine was anchor-validated before any claim number
(trace ≡ 0 symbolically; Schwarzschild B = 0.0 exactly;
MK max |B| = 8.91×10⁻¹⁷; T-b vs closed forms max rel dev
2.05×10⁻¹⁶). One anchor initially "failed" because
Schwarzschild was posed with Φ = 0 in Morris–Thorne
coordinates — the engine was fine; the corrected anchor
passes exactly (anatomy in the memo).

- **Correctness: REPRODUCED (all four clauses).**
  (a) Covariance: direct physical-jet evaluation at
  r₀ = 10 / 10³ gives max EC-combination relative
  deviation 5.18×10⁻¹³ / 1.31×10⁻¹² (bar < 10⁻⁹); the
  ladder consequence to 4.785×10⁷ m follows in the
  phase's stated form; the worker's supporting r₀ = 1
  grid minima match P61-1's stored tail minima.
  (b) Increment: ΔNEC1 min = −0.016679355263679
  r₀_{j+1}⁻⁴ (stored −0.016680); failures confined to
  exactly {NEC1, DEC_r, DEC_t} in the layer x_b ∈
  [1, 1.0034815202679233] (crossing digit-identical to
  the stored endpoint); layer price
  5.828036304258646×10⁶⁸ × E_legal, with E_legal
  re-derived from the P61-4 record (matches its stored
  3.00309032448144×10⁻²⁹ J at 10 m).
  (c) Pole: analytic at x_b = e⁻¹ (1 + ln x_b = 0);
  40-digit NEC1 = −6.58154461639×10²¹ at e⁻¹(1−10⁻³) and
  −6.64506547545×10⁴² at e⁻¹(1−10⁻⁶) — digit-for-digit
  the stored probes; pole order 7.009 by log-log fit;
  shell price lower bounds 6.925055976328622×10⁸⁴ /
  7.32659837454598×10⁹⁰ / 1.7106788738441663×10⁹⁶
  × E_legal at ε = 10⁻²/10⁻³/10⁻⁴, strictly increasing
  as ε → 0 — the deciding content UNBOUNDED holds.
  (d) Inheritance: all 8 fork premises extracted from
  `p614_memo.md` in substance; each quantifies over the
  home (the conformal action's Euclidean sector,
  Robertson–Walker geometry as such, the Bach equation);
  none mentions T-b's (b, Φ) or the member; fresh SymPy
  check: Bach ≡ 0 identically on a general RW metric
  (a(t) arbitrary, k free).
- **Novelty: PARTIALLY KNOWN.** Ingredients known (Lobo
  arXiv:0801.4401; Varieschi & Ault arXiv:1510.05054;
  Strominger–Horowitz–Perry, Nucl. Phys. B238 (1984) 653;
  Corral–Giribet–Olea arXiv:2105.10574). Not found: the
  growth-increment audit, the singular-shell unbounded
  price, or the fork-closure-with-inheritance as applied
  to a member. Coverage gap (stated plainly): INSPIRE-HEP
  and Semantic Scholar reached only via indexed records,
  not their own search interfaces.
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** —
  exact restated wording in `results/wD_g9_4.md` ("Exact
  restated wording"), carrying PRE-EXISTING ONLY as its
  head, the (V-b) sentence verbatim, the dynamic-read
  UNCOMPUTED status, the Class-B read-off scope, C12
  object accounting, and r₀* = 4.785×10⁷ m.

## Closing synthesis (coordinator, 2026-11-22)

**The honest headline: the conformal joining member is
real in every column the programme knows how to audit —
legality, join, stability, formation — and it is still
not a wormhole anyone can use, and the theory it lives in
still carries an undecided quantum-ghost clause.** All
four claims survived genuinely independent second paths:
two fresh Bach derivations built from the metric (W-A's
Weyl-divergence form, W-D's Ricci form — different
constructions, agreeing where they overlap), a junction
computation rebuilt from BDE's printed definitions, and a
stability implementation rebuilt from the method
description that reproduced T-b's stored eigenvalues to
every printed digit before it was allowed to read the
member. The gate's catches are precision- and prose-level,
not verdict-level: the stored throat digits carry a
~9×10⁻⁵ a-rounding sensitivity (inside every bar), one
Φ = 0 identity in the Phase-38 prose is false as stated
(no number depends on it), and every claim's novelty lands
at PARTIALLY KNOWN — conformal-gravity wormholes with
legal matter near the throat, and stable conformal
wormholes of another class, are already in print. What was
not found in the searches is the specific package: a
whole-domain-legal member of this family that joins at
10³ r₀ with a legal shell, is classically stable in the
computable interior sectors, and whose formation is
pre-existing only with an unbounded exotic growth price.
The member's limits ride with it, inseparably: joined
only at the extension radius; tidal bar 4.785×10⁷ m;
shell/exterior perturbations OPEN; formation PRE-EXISTING
ONLY; and (V-b) UNDECIDED — Pais–Uhlenbeck spin-2 ghost vs
Mannheim PT-symmetric quantisation — attached to every
statement. C12 throughout: a throat OBJECT; no transport
and no traversability is claimed anywhere in this gate.

**Count (claim level, 4 claims):**
- **Survived intact (UPLOAD-READY as stated): 0** — each
  claim's upload form is its restated wording (novelty
  and/or scope restatement in every case).
- **Survived weakened (UPLOAD-READY AFTER RESTATEMENT):
  4** — G9-1 (correctness as stated; restatement on the
  novelty axis), G9-2 (correctness as stated; restatement
  fixes the extension-radius scope + novelty form), G9-3
  (correctness as stated in its registered scope;
  restatement carries the full scope + the Cadoni et al.
  prior), G9-4 (all four clauses as stated; restatement
  carries the standing, the read-off scope and the
  novelty form).
- **Fell (DEAD AS OURS): 0.** **NOT YET: 0.**
- **NOT REPRODUCED: 0** — no deciding number failed on any
  fresh path.

**Correctness sub-count:** REPRODUCED ×4 (G9-1: all
combinations > 0 on the deciding set, throat values
within 8.9×10⁻⁵ relative; G9-2: [R̃] = −2.4×10⁻³⁹,
Ŝ₀⁰ > 0 at 0.65% of stored; G9-3: re-gate to all printed
digits, member smallest eigenvalue at ratio 1.0000 of
stored, static traces ≤ 3.13×10⁻³⁴; G9-4: all four
clauses, pole probes digit-for-digit).

**Novelty sub-count:** PARTIALLY KNOWN ×4 (G9-1: Lobo
2008 + Varieschi–Ault 2015, throat vicinity only; G9-2:
the BDE formalism and conformal/MK matching known, the
specific join not found; G9-3: Cadoni et al. 2025, a
different class; G9-4: all ingredients published, the
audit package not found). Outright "novel" ×0 — the
Uniqueness Protocol's bar is not met by any claim in this
set, as expected at registration. KNOWN ×0.

**Rung verdicts:** FTL (2a): NO — nothing in this set is a
transport or speed claim. Traversable wormhole: NO — the
set is a throat OBJECT claim set; traversability is
nowhere claimed (the member's tidal bar, pre-existing-only
formation and open shell/exterior stability are part of
why). Rung 2b: nothing. Technical results: the gated
four-claim package itself, plus the gate's instrument
record (two independent fresh Bach derivations; the
registered-convention identification, erratum 3).

## Errata / follow-ups owed (recorded, not executed by this gate)

1. **"DEC_t = NEC2" is false as stated** (this gate's own
   pre-registration anchor text above, inherited from
   `../phase38/results/p381_memo.md`): on the Φ = 0 slice,
   DEC_t − NEC2 = −2p_t ≠ 0 at all probed points, and the
   identity contradicts Phase 32's own T-b closed forms.
   The correct identity is DEC_t = ρ − |p_t| (DEC_r = NEC1
   and SEC = 2ρ are correct as stated). No claim number in
   Phase 38, 61, 71 or this gate depends on it — every
   audit scores the six EC combinations directly. A
   correction is owed to the p381_memo prose (and this
   erratum line is the correction of record for GATE9.md's
   anchor text).
2. **a-rounding sensitivity of the stored throat digits:**
   P61-1/P71-2's stored NEC1 = +0.00364119103852 /
   DEC_t = +0.00182059551926 correspond to a at fuller
   precision (0.27773424114865775, W-B's bisection
   a_zero); at exactly a = 0.277734 the values shift by
   ~9×10⁻⁵ relative (W-A). Inside every registered bar;
   future quotations of the throat digits should carry
   a's precision with them.
3. **Bach-convention identification:** the programme's
   registered Bach tensor is B = 2∇∇C + R·C (the
   Mannheim/Varieschi W), exactly twice the
   ∇∇C + ½R·C bracket (W-A's anchor, ratio 0.500 at every
   T-b point/component). Recorded so future fresh
   derivations start from the registered convention.
4. **G9-3 wording note:** W-C's restated wording retains
   "The member remains a scan signal under attack —
   nothing stronger." If the claim set is uploaded, the
   write-up decides whether the gated wording replaces
   that sentence (this gate does not edit worker
   wordings); the other three wordings carry no such
   sentence.
5. **Coverage gap (all four novelty searches):** no worker
   queried the INSPIRE-HEP or Semantic Scholar search
   interfaces natively (indexes/mirrors/general-web index
   only) — the same bounded gap as Gates 5–8, to be
   closed at write-up time if any claim is uploaded.
6. **Open scope carried, not closed by this gate:** the
   shell/exterior perturbation problem (G9-3's named
   scope limit); the packet numeric sign check (P38-2's
   named follow-up); the member's dynamic growth read
   (FU-P712-1); (V-b) UNDECIDED — untouched by every read
   in this gate, attached verbatim to every wording.
7. **Ledger:** the conformal row (NEW_PHYSICS_LEDGER.md
   line 110) can be updated per the PROPOSED edit below —
   proposed by this gate, NOT applied (see next section).

## Proposed ledger edit (PROPOSED by this gate — NOT applied)

The ledger's current conformal bullet (line 110) is stale
in two places: it states the √-shape throat "DOES NOT JOIN
to the MK exterior" as the row's standing (true of T-b,
superseded for the family by P61-1's joining member) and
says "Phase 61 is running the coefficient-4 join sweep"
(Phase 61 is complete; Phases 71 and Gate-9 have since
run). Proposed replacement text for that bullet, in the
ledger's style, if the ledger editor adopts it:

> - **Conformal (Weyl) gravity throats** (Phase 32 signal;
> red team = Phase 38, COMPLETE; join sweep = Phase 61;
> member columns = Phase 71; **Gate-9 PASSED 2026-11-22 —
> all four claims REPRODUCED on independent second paths,
> novelty PARTIALLY KNOWN ×4, upload-ready only in the
> Gate-9 restated wordings; publication pending Rakshit's
> decision**): T-b (b = r₀√(r/r₀), Φ = 0) is EC-legal in
> exact closed form on its whole domain and classically
> stable in the computable sectors, but joins at NO radius
> ([R̃] = (1 + p)(r₀/r_Σ)^{1−p} > 0 on the Φ = 0 slice,
> exact). One member of the Phase-38 legality region —
> Φ₂ profile, p = 0.1, a = 0.277734 — is EC-legal on
> [r₀, 10³ r₀] (throat NEC1 +0.003641, DEC_t +0.001821,
> 40-digit audit) AND joins the registered-γ (10⁻²⁸ m⁻¹)
> Mannheim–Kazanas exterior at r_Σ = 10³ r₀ with a legal
> shell ([R̃] = 0 at 40 digits, Ŝ₀⁰ = +0.020291 α₀ ≥ 0;
> joined β_MK = 2.142611 r₀, k = −2.28996×10⁻⁹ r₀⁻²; no
> ADM mass in MK asymptotics). It is classically stable
> in the computable interior sectors (dynamic quotient
> spectrum: no zero crossing, smallest physical
> eigenvalue 0.00121741; shell/exterior perturbations
> OPEN; Galerkin read, not an exact spectrum). Its tidal
> bar is r₀* = 4.785×10⁷ m. Its formation is
> PRE-EXISTING ONLY: growth is growable-only-exotically
> (common-domain increment fails in a thin inner layer
> priced 5.83×10⁶⁸ × E_legal per decade; the grown shell
> is SINGULAR at Φ₂'s pole x = 1/e, price UNBOUNDED) and
> nucleation is CLOSED as a property of the theory's home
> (P61-4's conformally-flat fork, inherited). This is a
> throat OBJECT result: no transport, no traversability.
> (V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).

Placement note: the ledger's PUBLISHED tier is defined as
"passed a Gate AND in a public release" — these claims
have passed the Gate but are NOT published, so the gate
proposes the row stay under the UNDER ATTACK heading with
the wording above (including its Gate-9 marker) until a
publication decision moves it; alternatively the ledger
editor may add a gated-unpublished marker. The gate takes
no position beyond recording that the current bullet's two
stale statements should not survive another ledger sync.

**Upload-ready list (standing two-part rule):** G9-1,
G9-2, G9-3, G9-4 — each ONLY in its restated wording as
recorded verbatim in its worker report (W-A: "Exact
restated wording"; W-B: "Exact restated wording (G9-2)";
W-C: §8; W-D: "Exact restated wording"). Nothing was
uploaded by this gate; publication remains Rakshit's
separate decision.

**Status: COMPLETE** (all four workers returned; all four
claims verdicted; record closed 2026-11-22).

## Status log (continued)

- 2026-11-22: W-B returned (G9-2 REPRODUCED / PARTIALLY
  KNOWN); W-D returned (G9-4 REPRODUCED, all four clauses /
  PARTIALLY KNOWN); W-A returned (G9-1 REPRODUCED /
  PARTIALLY KNOWN; the DEC_t = NEC2 prose error caught —
  erratum 1); W-C returned (G9-3 REPRODUCED / PARTIALLY
  KNOWN; machinery re-gate passed to all printed digits).
  Coordinator integrated verdicts, closing synthesis,
  errata and the proposed ledger edit above. Gate CLOSED.
  Nothing uploaded; the ledger was NOT edited.
