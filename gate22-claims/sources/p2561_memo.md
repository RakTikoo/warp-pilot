# P256-1 — MEMO: CERTIFY OR REFUTE THE COMBINED-CLASS
# BRACKET (0.65625, 0.6625] (Phase 243-pattern certificate)
# — INTEGRATED RECORD

Worker of Phase 256 (single item P256-1), warp pilot.
Registration (pre-run, FIXED, not edited):
`phase256/work/p2561_registration.md`. Driver:
`phase256/work/p2561_run.py`; results:
`phase256/results/p2561_results.json`; checker:
`phase256/work/p2561_check.py` →
`phase256/results/p2561_verify.json`. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python
(numpy 2.5.5 / scipy 1.18.1), float64. INTERNAL only. No
ledger append, no launch, no external contact; nothing
outside `phase256/` edited. Protected files
byte-identical before/after (§7).

## VERDICT — FORM 1 FIRES

**BRACKET CERTIFIED.** The run's recorded verdict note,
verbatim from `p2561_results.json`:

> The combined-class first crossing (0.65625, 0.6625] on
> NEC_ph = DEC_ph stands as a verdict in the certified
> scope: per-instant Richardson limits on the binding
> clauses over the window [0.6, 0.75] meet the 1e-6 bar
> (CERT-1..4 hold). The sustainment lead changes hands AT
> VERDICT GRADE: this bracket, certified here, lies
> entirely past the wound pose's (0.55625, 0.5625],
> certified at Phase 243 and upheld at Gate-23 — the
> comparison is certified-vs-certified. Fenced by: (i)
> the tail limitation of sec.5(c) (reads past the window
> are NOT certified; tail pricing stands on the face);
> (ii) pose scope (Phase 169 A-branch datum, true lock;
> kappa = 0.3 director + C2 rotating headline +
> CH-PHI-Auu under P-PHI-TRIM-248 at the B := 2.5
> operational stop, as posed); (iii) jet scope / sector
> superposition (exhibit != construction); (iv)
> programme-level sustainment wording remains gated by
> p1592 regardless. Named successor: a Gate registration
> on the certified claim set.

Named successor (registration §7, form 1): **a Gate
registration on the certified claim set.** (Amending the
gate's claim set is the parent's act, not this phase's.)

## 1. REGISTRATION SUMMARY, WITH THE ADAPTATIONS

The registration carries Phase 243's certificate with
exactly the four adaptations stated on its face (§A):
(A1) the pose is Phase 252's re-posed combined-class arm
— Phase 169 A-branch datum (true lock) + κ = 0.3 director
+ the C2 rotating headline construction (W = 0.2 sin²θ)
+ CH-PHI-Auu under P-PHI-TRIM-248, a(t) = −0.5 −
c_trim·t² with the STORED c_trim = +5.253378 (full stored
float 5.253378225339471, from
`phase248/results/p2482_results.json`), clamped at the
operational stop B := 2.5 (stop binds from t_stop =
√(2/c_trim) = 0.617015) — read with Phase 252's machinery
(`base_jets` → `posed_jets` → `solve_wuu_generic` →
`clauses_of` on the fixed audit grid TH), copied into
`phase256/` and unmodified in substance; binding clauses
NEC_φ and DEC_φ. (A2) grids NOT adapted: the Phase 243
ladder verbatim — G3 (N_θ = 5761, h_t = 0.00125), G4
(11521, 0.000625), G5 (23041, 0.0003125), every march to
T_END = 1.0. (A3) window fixed by the claim plus Phase
243's margin pattern: W = sampled {0.6, 0.625, 0.65,
0.675, 0.7, 0.725, 0.75} ∪ refined {0.65625, 0.6625,
0.66875}; bracket (0.65625, 0.6625]. (A4) no t*
disposition: the wound pose's bracket is NOT re-opened,
re-read, or re-priced; the comparison is
certified-vs-certified only because form 1 fired.
Everything else — per-instant Richardson (monotone case
p = log2(d34/d45), admissible 0.5 ≤ p ≤ 6, L = v5 −
d45/(2^p − 1), r = |d45|/(2^p − 1); degenerate case
L := v5, r := max(|d34|, |d45|); limit-certified iff
r ≤ 1×10⁻⁶ AND |d34| ≤ 1×10⁻⁶ AND |d45| ≤ 1×10⁻⁶),
CERT-1…4, CTRL-1/2/3, the §5(d) probe rule (900 s
threshold), the §6 decision order, the three verdict
forms, the fences — is Phase 243's, unchanged in
substance. **The 1×10⁻⁶ threshold is nowhere changed.**

One execution-order note, stated plainly (Phase 243's
own driver order, followed here): CTRL-2 and CTRL-1 ran
first; the §5(d) probe ran before the G5 march because
the probe gates that march; CTRL-3 — which by
construction reads off the G5 state — was evaluated
immediately after the G5 march and BEFORE any
certificate evaluation. No certificate quantity was
computed before all three controls had passed, so the
§6 decision order is preserved in substance. No driver
bug was found or fixed during the run; the driver
completed in one honest attempt (wall 662.1 s total).

## 2. CONTROLS

**CTRL-2 — PASS, exact** (stored rows of
`phase252/results/p2522_results.json` only): (a) the
re-posed arm's sampled first-crossing bracket recomputes
to (0.65, 0.675] with first-fail carriers exactly
{NEC_φ, DEC_φ}; (b) the stored halving ladder replays to
the refined bracket (0.65625, 0.6625] with end margins
NEC_φ = +0.05279917238250764 / −0.07369468042669158 (the
stored full-precision floats, ladder entries identical
to the bracket-end margins); (c) the bracket
decomposition identity headline + lift = composed holds
at both ends at exactly 0.0 difference; (d) the stop
instant √(2/5.253378) = 0.61701493, within 8.4×10⁻⁸ of
0.617015 (bar 1×10⁻⁶).

**CTRL-1 — PASS, all diffs 0.0** (matched march length
T_END = 1.0; standing discretisation N_θ = 2881, main
h_t = 0.0025 / aux h_t = 0.00125):

| comparison | max abs diff |
|---|---|
| fresh re-posed rows, 41 sampled instants (main lattice), clause minima vs Phase 252 stored `reposed_sampled` | 0.0 |
| same instants, full clause profiles (report-only, ulp class) | 0.0 |
| bracket lo end t = 0.65625 (aux march, index 525), clause minima vs stored `reposed_bracket` lo margins | 0.0 |
| bracket hi end t = 0.6625 (main march, index 265), clause minima vs stored hi margins | 0.0 |

No ulp-class profile entries were seen at all — every
profile entry also reproduces at 0.0.

**CTRL-3 — PASS** (G5 admitted): fresh G5 director-only
reads (wound machinery copied from `p2431_run.py`,
unmodified in substance) vs Phase 210's stored G4
director rows — t = 0.25: 1.4235054024425153×10⁻⁸;
t = 0.5: 5.694021876223587×10⁻⁸, both ≤ 1×10⁻⁶. (These
are numerically identical to Phase 243's CTRL-3 values,
as they must be: same grid, same machinery, same stored
rows.)

## 3. G5 COST PROBE (§5(d))

Probe march G5 over [0, 0.05] (160 steps): **21.0 s**.
Projection for the registered [0, 1.0] march (3200
steps): 20 × probe = **419.9 s ≤ 900 s** — the rule does
NOT fire; G5 was run. (Actual G5 march wall: 497.4 s.)
State-array size on the face: 590,033,928 B per field;
MU + U + MTT = 1.770 GB; G3/G4 states were freed before
the G5 march. The §5(d) kernel-spec packaging obligation
attaches only to form 3, which did not fire; no spec was
written. March walls: standing main 7.0 s / aux 12.3 s;
G3 29.8 s; G4 80.2 s; G5 497.4 s.

## 4. THE CERTIFICATE — COMBINED-CLASS BRACKET

Per-instant Richardson on NEC_φ = DEC_φ (the two clauses
are pointwise identical in this machinery — the checker
verified the two rows equal at every instant; one row
serves both — the results file carries both, identical).
v3/v4/v5 are the G3/G4/G5 clause minima; L the
Richardson limit; r = |L − v5| the residual. Bar
1×10⁻⁶ throughout.

| t | case | p | v3 | v4 | v5 | d34 | d45 | L | r | cert |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.6 | monotone | 3.70044 | 0.88826151468098580 | 0.88826151468110126 | 0.88826151468111014 | −1.155×10⁻¹³ | −8.882×10⁻¹⁵ | 0.88826151468111092 | 7.772×10⁻¹⁶ | ✓ |
| 0.625 | monotone | 4.24793 | 0.61809315086183148 | 0.61809315086196648 | 0.61809315086197358 | −1.350×10⁻¹³ | −7.105×10⁻¹⁵ | 0.61809315086197403 | 4.441×10⁻¹⁶ | ✓ |
| 0.65 | monotone | 4.04439 | 0.17452067033937713 | 0.17452067033952368 | 0.17452067033953256 | −1.465×10⁻¹³ | −8.882×10⁻¹⁵ | 0.17452067033953314 | 5.829×10⁻¹⁶ | ✓ |
| **0.65625** (t_lo) | monotone | 4.11270 | 0.052799172383710236 | 0.05279917238386389 | 0.052799172383872772 | −1.537×10⁻¹³ | −8.882×10⁻¹⁵ | **0.05279917238387332** | 5.482×10⁻¹⁶ | ✓ |
| **0.6625** (t_hi) | monotone | 3.63559 | −0.073694680424204684 | −0.073694680424050141 | −0.073694680424037706 | −1.545×10⁻¹³ | −1.243×10⁻¹⁴ | **−0.073694680424036624** | 1.082×10⁻¹⁵ | ✓ |
| 0.66875 | monotone | 4.30581 | −0.20520507819118183 | −0.20520507819102374 | −0.20520507819101574 | −1.581×10⁻¹³ | −7.994×10⁻¹⁵ | −0.20520507819101533 | 4.163×10⁻¹⁶ | ✓ |
| 0.675 | monotone | 4.20163 | −0.34199126810277569 | −0.34199126810261227 | −0.34199126810260339 | −1.634×10⁻¹³ | −8.882×10⁻¹⁵ | −0.34199126810260289 | 4.996×10⁻¹⁶ | ✓ |
| 0.7 | monotone | 3.53916 | −0.94766802431313835 | −0.94766802431297315 | −0.94766802431295893 | −1.652×10⁻¹³ | −1.421×10⁻¹⁴ | −0.94766802431295760 | 1.332×10⁻¹⁵ | ✓ |
| 0.725 | monotone | 3.22973 | −1.66321792064178100 | −1.66321792064160600 | −1.66321792064158740 | −1.750×10⁻¹³ | −1.865×10⁻¹⁴ | −1.66321792064158510 | 2.220×10⁻¹⁵ | ✓ |
| 0.75 | monotone | 4.61471 | −2.51530261051342840 | −2.51530261051325430 | −2.51530261051324720 | −1.741×10⁻¹³ | −7.105×10⁻¹⁵ | −2.51530261051324680 | 4.441×10⁻¹⁶ | ✓ |

Every window instant is monotone with p in [3.23, 4.61]
— admissible Richardson behaviour at the float64 noise
floor of this read: the pairwise grid disagreements are
at the 10⁻¹³ level (worst in-window |d34| = 1.750×10⁻¹³
at t = 0.725; worst |d45| = 1.865×10⁻¹⁴) and the worst
residual is r = 2.220×10⁻¹⁵ — every instant clears the
1×10⁻⁶ bar by nine orders of magnitude. Stated plainly,
the anatomy differs from Phase 243's wound-pose table
(there p ≈ 2.0000 with disagreements at 10⁻⁷): the
combined-class clause minima are a read-level sector off
the marched state, interpolated onto the fixed audit
grid, and at these instants they are grid-stable to
~10⁻¹³, so the Richardson limit sits on top of the
finest-grid value. The certificate's bar is met as
registered; the smallness of the disagreements is a
property of the read, recorded here, not a relaxation —
CERT-2/CERT-3 still required the LIMIT to straddle zero
at the bracket with no earlier in-window crossing, and
it does, with the bracket-end limits carrying
essentially the standing-grid margins (+0.052799 /
−0.073695).

**CERT booleans: CERT-1 TRUE** (no failures), **CERT-2
TRUE** (L(0.65625) = +0.0527991724 ≥ 0, L(0.6625) =
−0.0736946804 < 0; v5 likewise +0.0527991724 /
−0.0736946804), **CERT-3 TRUE** (no earlier in-window
crossing at L or v5 — all window instants ≤ t_lo are
positive at both), **CERT-4 TRUE** (no non-binding
clause crosses first at G5 anywhere in the window up to
t_hi — the next clause at the hi end is ≥ +4.188 at the
standing read and remains > 0 at G5; non-clause bars at
the bracket instants: momentum worst 6.106×10⁻¹⁶
(0.65625) / 4.996×10⁻¹⁶ (0.6625), flare_min 0.12187 /
0.12069 > 0, domain_R_min 0.60340 / 0.59964 > 0,
domain_exp2Phi_min 0.0058112 > 0 — all ok).

## 5. TAIL PRICING (§5(c) — ON THE FACE, AS REGISTERED)

From THIS phase's fresh G3 and G4 rows (the §5(c)
adaptation: no stored multi-grid rows exist for this
pose): per-instant max G3–G4 disagreement over all
seven clauses at the sampled instants on (0.75, 1.0] —
1.674898×10⁻⁶ (0.775), 2.080761×10⁻⁶ (0.8),
2.547346×10⁻⁶ (0.825), 3.207685×10⁻⁶ (0.85),
4.038274×10⁻⁶ (0.875), 5.230806×10⁻⁶ (0.9),
6.832710×10⁻⁶ (0.925), 8.975727×10⁻⁶ (0.95),
1.201324×10⁻⁵ (0.975), 1.632692×10⁻⁵ (1.0). First
exceedance of the 1×10⁻⁶ bar on (0.75, 1.0] at the
first tail instant, **t = 0.775**; stage max =
**1.6326915963205124×10⁻⁵ at t = 1.0**, carrier
**DEC_θ**, relative disagreement |d|/|v4| =
1.8932984155740035×10⁻⁶. This stands on the face of the
form-1 verdict as fence (i): reads past the window are
NOT certified; the tail disagreement stands as the tail
reads' priced uncertainty. (Note the contrast, recorded
without interpretation beyond the numbers: the tail
disagreement is carried by DEC_θ at the 10⁻⁵ level
while the binding clauses' in-window disagreements sit
at 10⁻¹³ — the tail price attaches to the tail reads,
exactly as the scope argument of §1 provides.)

## 6. FILES

- `phase256/work/p2561_run.py` — driver (controls,
  probe, ladder marches, window reads, Richardson +
  CERT-1..4, tail pricing, verdict; 662.1 s).
- `phase256/results/p2561_results.json` — full record
  (controls, probe, window rows G3/G4/G5, tail rows,
  per-instant Richardson table, CERT booleans, tail
  pricing, verdict).
- `phase256/work/p2561_check.py` — independent checker
  (§8 below).
- `phase256/results/p2561_verify.json` — checker record.
- `phase256/results/p2561_memo.md` — this memo.
- No G5 kernel spec: the §5(d) obligation attaches only
  to form 3, which did not fire.

## 7. PROTECTED FILES — BYTE IDENTITY HOLDS

md5-identical before and after the run (driver-recorded;
checker re-verified live). Full table in
`p2561_results.json` (`md5_protected_before/after`); the
load-bearing entries:

| file | md5 |
|---|---|
| phase129/work/p1296_derive_raw.json | d89f6a8646e4a96d7733c0b1827b5fcd |
| phase150/work/p1501_families.py | 9738b6267ec51a10f62db9f495b06b40 |
| phase162/work/p1621_engine.py | 1f12ec29c2693ca00a19da365abeccf4 |
| phase167/work/p167_engine.py | 9db35c0b82635409e0bddf17251ba53f |
| phase169/work/p1692_engine.py | 1781b544920052bcc9b919574561acb2 |
| phase202/work/p2022_wound.py | 24f0d69cd099b89cd42abef59d378b3d |
| phase210/results/p2101_results.json | cd6ecb6c23c26b58642749f6b0e7d33c |
| phase214/results/p2141_results.json | 394717c0825306f779fb8321cefa166c |
| phase243/work/p2431_run.py | 67da28856ee73c15ae1fde2128289708 |
| phase243/results/p2431_results.json | 0a66e60ff23cadaf8d967795d12dbe82 |
| phase252/work/p252_registration.md | d4aa00fa7620708c4596aa3359d86d3a |
| phase252/work/p2521_run.py | 02e6e3bf6e74f74a9fbce3d01d34ef5a |
| phase252/work/p2522_run.py | 316bc6d77f9f5d0e0c2e8964d770affb |
| phase252/results/p2522_results.json | e8fc99bfc5b971394519d75ed05b18b1 |
| phase256/work/p2561_registration.md | a5bb1778016ac2c4bc86d27df09d7c36 |

(21 protected files in total, including the Phase
246/248 files and `phase252/results/p2521_results.json`;
all identical before/after.)

## 8. CHECKER — 20/20 PASS

`phase256/work/p2561_check.py` →
`phase256/results/p2561_verify.json`: **20 passed, 0
failed** (checker wall 708.7 s, including its own fresh
G4 and G5 marches). The checks: protected byte identity
(live vs results before/after, two checks); CTRL-2
recomputed from Phase 252's stored rows (sampled
bracket + carriers, refined bracket + margins,
decomposition identity, stop instant, recorded-pass
consistency); CTRL-1 recorded outcome consistent with
its recorded diffs (pass ⟺ all verdict-carrying diffs
0.0 — the decision-order-consistent assertion form of
registration §9, not an assertion of pass) and the
report-only profile diff present (0.0); Phase 210 stored
director t = 0.5 NEC_φ anchor; CTRL-3 recorded outcome
consistent with its recorded diffs; probe projection
arithmetic (20 × probe wall, 900 s rule, state size);
**fresh G4 spot recomputation of both bracket-end
instants at diff 0.0**; **fresh G5 spot recomputation of
both bracket-end instants at diff 0.0**; fresh G5
director read at t = 0.5 reproducing the recorded
CTRL-3 diff exactly (5.694021876223587×10⁻⁸); Richardson
arithmetic reproduced from the stored per-instant
values; per-instant v3/v4/v5 equal to the stored window
rows; CERT booleans reproduced; tail pricing recomputed
from the stored G3/G4 tail rows (first exceedance
0.775, stage max 1.6326915963205124×10⁻⁵); verdict form
consistent with §6's decision order (form 1).

## 9. FENCES (unchanged from the registration)

(i) Tail limitation (§5 above): reads past the window
[0.6, 0.75] are NOT certified; the tail pricing stands
on the face as the tail reads' priced uncertainty.
(ii) Pose scope: Phase 169 A-branch datum, true lock;
κ = 0.3 director + C2 rotating headline construction +
CH-PHI-Auu under P-PHI-TRIM-248 at the B := 2.5
operational stop, as posed. The stop is an operational
limit of the pose as certified, not a priced boundary.
(iii) Jet scope / sector superposition: posed jet
entries, no coupled solve — no claim a physical sector
realises the channels jointly; exhibit ≠ construction.
(iv) Programme-level sustainment wording remains gated
by p1592 regardless — untouched by this verdict. The
trim law is open-loop and fixed in advance — ≠ the
closed-loop stabilisability proof (Phase 208) and ≠
Phase 217 V2. Phase 210/214/226/229/233/243 verdicts
stand for their own poses and scopes; Gate-23's claim
set stands untouched. This certificate is this phase's
registered instrument, adopted in advance — not a
retroactive amendment of Phase 252's registration,
whose checkpoint named exactly this successor.
