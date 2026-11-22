# P21-4 — f(T,B): the boundary-term sector — MEMO

**VERDICT: KILL — TELEPARALLEL CLOSES** (KILL clause 1 met;
clause 2 not met — the B sector *does* move the Lorentz
floor, on a row that supplies nothing; see below).
Run 2026-11-21: `p214_lib.py`, `p214_gate.py`,
`p214_scan.py`, `p214_audit.py`, `p214_check.py`; survey
addendum + gates + post-hoc notes in
`results/p214_run_record.md`; results
`results/p214_results.json` (checker), `p214_scan.json`,
`p214_audit.json`, `p214_gate.json`. System python3,
float64; published tensor only (BBW Eq. (42)); internal
only, nothing uploaded.

## PLAIN LANGUAGE

Adding the boundary term B to teleparallel gravity does
two real things and neither saves it. First, it can
genuinely supply the wall's energy bill at the binding
points — several rows cover 75–89% of the binding set at
superluminal speed. But every one of those rows is
unhealthy (the effective gravitational coupling flips
sign somewhere on the wall, by the same dial as in pure
f(T)), and not one row in all 108 — at any speed, healthy
or not — is clean across the wall's full volume: the
required matter violates the null energy condition on
55–99% of the volume in every strong row. Second, the B
sector *can* move the Lorentz floor — the best healthy
row's antisymmetric residual falls to 0.052 / 0.072 at
β = 1.1 / 1.5, against the six-function floor of
0.298 / 0.330 — but that row's supply points the wrong
way (it covers 3–4% of the binding set), and 0.052 is
still 2.6× above the 0.02 solution-grade bar. The two
things B fixes never occur in the same row. With pure
f(T) already dead (P12-1) and the floor a continuum
property (P19-3), the teleparallel programme closes:
no f(T,B) row on this bed is simultaneously healthy,
volume-clean, and supplying.

## CONTROL GATE (passed BEFORE any scan number)

B3 control, Bahamonde–Böhmer–Wright Eq. (42) vs the
textbook f(R) equations (their Eq. (40)) computed
independently from (G, R, ∇R, ∇∇R): rel_med
1.2e-16 – 2.1e-16 at β ∈ {1.1, 1.5}, κ ∈ {−5, 1, 20}
— the transcription is *exact* for the f(R) sub-class.
GR control: H ≡ G exactly (max|H−G| = 0.0). B from the
torsion vector (B = 2∇·T^μ) vs R − t: median rel. error
0.0017 (sign fixed by this check). Superpotential
contraction Z_t vs p111_d's published W: identical
(rel_med 0.0). PL2 regression (in-run, B2 γ=0 vs P12-1's
stored PL2): PASSED on the corrected machinery —
partial/full 0.000/0.000 at α ∈ {5, 20}, β ∈ {1.1, 1.5},
ratio_med −3.61/−14.44 (β=1.1) and −5.82/−23.30
(β=1.5) matching P12-1 within Δlog10 ≤ 0.001. (The
regression first caught a superpotential-term sign
against the programme's published-W tensor — systematic
4.79×/5.04× in ratio_med with partial/full/sign exact;
fixed, re-gated, re-run in full; run record post-hoc
note 3. The B3 gate is blind to that sign, the
regression is not — both gates were necessary.)

## RUNG-2a (FTL) — the superluminal numbers on their own

β = 1.1 (504 binding points, max deficit 2.825e-3):
strongest rows — B2 (α=−5, γ=0) [the PL2 member itself]
partial 0.837 / full 0.756, health FAIL (G_eff,min < 0),
volume NEC violation 0.820, Type-I 0.154; B1b γ=−5
partial 0.794 / full 0.790, health FAIL (G_eff,min
−112.4), volume violation 0.883; B3 κ=−20 partial
0.734 / full 0.583, health FAIL, volume violation
0.745. Best HEALTH-passing row at β=1.1: B2 (20, 1),
partial 0.038 — and it is the floor row below.
β = 1.5 (594 points, max deficit 3.387e-3): B2 (−5, 0)
partial 0.891 / full 0.828, health FAIL, volume
violation 0.816; B1b γ=−5 partial 0.754 / full 0.751,
health FAIL (G_eff,min −53.3), volume violation 0.885;
B3 κ=−20 partial 0.662 / full 0.522, health FAIL,
volume violation 0.735. Best health-passing row: B2
(20, 1), partial 0.032. No superluminal row is
health-passing with partial ≥ 0.50 — the conservation
audit's selection (health-passing, partial ≥ 0.50) is
therefore *empty* at both superluminal β, itself a
registered-read finding. No ALIGNMENT: the shared bars
(full ≥ 0.90 + health + volume-clean + antisym ≤ 0.02)
are failed on every clause by every superluminal row.

## LORENTZ-FLOOR READ (the item's second question)

Best health-passing row per β, antisymmetric residual
of the full Eq. (42) on independent Sobol points
(96 pts, h ∈ {0.3, 0.15}): B2 (α=20, γ=1) — rel_med
0.0523 / 0.0522 at β=1.1 (P19-3 floor 0.298: **82%
improvement**) and 0.0723 / 0.0718 at β=1.5 (floor
0.330: **78% improvement**). The registered floor-move
test (≥25% at either superluminal β at solution-grade
health) is therefore MET at both β — KILL clause 2
does not fire. But: (i) 0.052 / 0.072 remains
2.6× / 3.6× above the 0.02 good-tetrad bar, so the row
is not solution-grade and ALIGNMENT's antisym clause
fails; (ii) the row is supply-dead (partial
0.038 / 0.032, ratio_med −18.4 / −26.3 — its supply is
sign-reversed like every strong-T row). Mechanism:
the antisymmetric part of Eq. (42) is carried entirely
by the superpotential term, whose (∇T, ∇B) coefficients
are (f_TT+f_BT) and (f_BB+f_BT); at (α, γ) = (20, 1)
these partially cancel on the bed while the symmetric
denominator grows — B *can* tune the antisym
coefficient combination in a way pure f(T) (one
coefficient, f_TT) cannot. The B3 control's antisym
residual is 0.0000 at both h and both β, exactly as
BBW's Eq. (43) requires (only the f(R) sub-class is
Lorentz invariant) — the floor is a property of the
non-f(R) sector, and the machinery sees it correctly.

## PER-FAMILY ANATOMY — what B can and cannot change

(B1a) f = t + γ L_w² B². β=0.1: γ>0 rows healthy,
best partial 0.586 (γ=20) — but volume NEC violation
0.71, SEC violation 1.000. Superluminal: **zero**
health-passing rows at either β. γ>0 rows pass the
scalar proxy (φ_bb = 2γL_w² > 0) but fail G_eff:
G_eff = 1 + 4γL_w²·b, and b ranges over both signs on
the superluminal bed (b ∈ [−0.028, 0.079] at β=1.5),
so G_eff,min is negative for every γ ≠ 0 scanned
(−0.57 at γ=0.2 to −357 at γ=20, β=1.5); γ<0 rows
fail the scalar proxy and G_eff together. Best
superluminal partial 0.569 / 0.594 (γ=20), volume
violation 0.947.
(B1b) f = t + γ|B|^{1/2}/L_w. The strongest raw supply
of any B-family at β=0.1 (γ=−5: partial 0.825) — bought
entirely with a singular derivative: f_b ∝
γ|b|^{−1/2} diverges where b → 0 and G_eff,min reaches
−112 (β=1.1, γ=−5). γ>0 rows fail the scalar proxy
(φ_bb = −γ/(4L_w|b|^{3/2}) < 0 identically). One
health-passing row in the whole family (β=0.1,
γ=−0.2, partial 0.637, volume NEC violation 0.285,
SEC 0.987 — still volume-dirty, and its conservation
rel_med 0.0246 is the audit's only median failure).
(B2) f = t + αL_w²T² + γL_w²B² — what B adds to PL2,
isolated: at α=−5, turning γ on from 0 *lowers*
partial (0.837 → 0.603 at γ=1, β=1.1; 0.891 → 0.643 at
β=1.5) and raises volume violation (0.820 → 0.940).
At α=+20, γ=1 is what creates the floor row above —
the B term's one constructive act in the scan is
antisym cancellation, not supply. The γ=0 spine
reproduces P12-1's PL2 exactly (regression above):
the T-sector's κ<0-aligns-but-unhealthy /
κ>0-healthy-but-reversed trap is untouched by B.
(B3) CONTROL f = F(R), F = R·exp(κL_w²R): behaves
exactly as the f(R) class must (gate at 1e-16;
antisym identically 0). As a supply it is the
programme's known f(R) story retold: partial up to
0.734 / 0.662 superluminal at κ=−20, but F1(R) crosses
zero on the bed's R-range so every superluminal B3
row fails G_eff health, and volume NEC violation is
0.73–0.77 on its best rows. Health-passing B3 rows
exist only at β=0.1 (best partial 0.657, volume
violation 0.784). The control validates the machinery
and closes nothing new — f(R) was already subsumed
(P9-3: scalar-tensor in disguise, closed P8-4).

Cross-cutting: **zero of 108 rows is volume-clean**
(NEC violation fraction 0 at both h AND Type-I
fraction 1) — the volume, not the binding set, is
where every f(T,B) row dies, as it was for P12-3's
Proca rows and P12-1's f(T) rows. All-four-EC volume
reads on partial ≥ 0.50 rows: SEC violation fraction
0.73–1.000, DEC 0.45–0.87, WEC 0.46–0.84 — no row is
close on any condition. Conservation (health-passing
partial ≥ 0.50 rows, all at β=0.1): rel_med ≤ 0.02
for 10 of 11 rows (0.0039–0.0109; B1b γ=−0.2 fails at
0.0246), but rel_p90 is 0.25–0.48 and rel_max ≈ 1.0
on every row — median-level conservation with O(1)
tails, the designer-sustained pattern, not
solution-grade.

## VERDICT vs the fixed bars

ALIGNMENT: met by no row (no superluminal row has
full ≥ 0.90 with health; none is volume-clean; the
only antisym ≤ 0.02 rows are the B3 control's, whose
antisym vanishes by construction and which fail
health and volume). KILL clause 1 MET (no row at any
β is simultaneously health-passing, volume-clean and
partial ≥ 0.50 — indeed no row at any β is
volume-clean at all). KILL clause 2 NOT met (the
floor-move test passes at both superluminal β, on
B2 (20, 1)) — recorded plainly: the closure rests on
clause 1, and the floor improvement is a real,
registered-test-passing result that changes no
verdict because the improving row supplies nothing
and remains 2.6–3.6× above the solution-grade bar.
**KILL — TELEPARALLEL CLOSES.**

What B can change (from the runs): the antisymmetric
coefficient combination (a second dial pure f(T)
lacks — 78–82% floor reduction at tuned (α, γ)); the
binding-set supply at fixed health at β=0.1 (B1b's
0.825, B3's f(R)-class supply). What B cannot change:
the G_eff sign trap (B enters G_eff through
2φ_b, and b takes both signs on the moving bed, so
any B coupling strong enough to supply flips G_eff
somewhere — the P12-1 dial with a second handle on
the same trap); the volume (B's supply is as
volume-dirty as T's — worst at the same mid-wall
band); solution-grade status (antisym floor 0.052
at best, conservation tails O(1)).

REOPENING CONDITIONS (stated): (i) a pre-registered
row family built *on* the antisym-cancellation locus
{(f_TT+f_BT), (f_BB+f_BT) ≈ 0 on the bed} with the
supply sign audited independently — the one place
this scan found constructive B behaviour; (ii) the
P19-3 reopening (full 3-D / adaptive-basis / PDE
good-tetrad search), which now also bounds f(T,B):
its floor read here used the tetrad of record, and a
genuinely good moving tetrad would reopen both
P12-1 and this item; (iii) an F(R) member with
F1 > 0 and F′ > 0 on the whole bed R-range as a B3
row — that is the f(R)/scalar-tensor programme's
question (closed P8-4), not teleparallel's.

## FOLLOW-UPS (named, for future pre-registration)

(F1) **Antisym-cancellation locus map** (the item's
one constructive find): solve for the (α, γ) curve
along which B2's antisym rel_med minimises at
β = 1.1 / 1.5, and read supply sign + G_eff along it.
Question: does the locus pass through any
supply-positive, G_eff-positive point? If the locus
and the supply-positive region are disjoint on the
bed, the floor/supply decoupling is structural and
the closure hardens; if they meet, that point is a
new pre-registration.
(F2) **B1b singularity audit**: the |B|^{1/2} family's
supply is carried by points near b = 0 where f_b
diverges — a per-point anatomy of whether *any*
non-singular B-power (e.g. B²/(|B|+B₀) regularised
at a stated B₀) keeps the β=0.1 supply without the
G_eff blow-up. Expected negative; cheap and decisive
for the B-power family as a whole.

## DISCLOSURES

Three dated post-hoc notes in the run record
(numerical conventions and one tensor sign; no bar,
grid or tolerance changed): the cross-check boundary
convention (B3 κ=−20 has 112 binding points at
ratio = 1 ± 1e-16 automatically), the B-active health
definition, and the superpotential sign found by the
PL2 regression (first scan superseded in full, no
number from it used). The ∝g_μν scalar term uses
BBW Eq. (42)'s sign, which differs from P12-1's —
immaterial to every P12-1 verdict (all null
contractions / antisym parts) and validated here by
the B3 gate at 1e-16. All numbers are tetrad-relative
(tetrad of record, Phase-3 frame caveat). The
optimisation directive was applied to execution only
(unattended chain + mechanical checker); grid, bars
and audits are exactly as pre-registered — no
conflict with the rider arose.
