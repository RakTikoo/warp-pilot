# P252-1 (Item 1) — THE PROVENANCE AUDIT OF CH-PHI-Auu's
# AMPLITUDE CAP |a| ≤ 0.8 — memo

Worker W252-1, 2026-11-24. Registration (fixed, NOT edited):
`phase252/work/p252_registration.md`. Driver:
`phase252/work/p2521_run.py` (machinery copied from
`phase248/work/p2481_run.py` / `p2482_run.py`, generalised in
the Auu amplitude; `phase248/` not edited); checker:
`phase252/work/p2521_check.py` (**ALL PASS, 65/65**, including
fresh spot recomputation of every deciding read at diff 0.0
and live protected-file md5 identity); numbers:
`phase252/results/p2521_results.json`,
`phase252/results/p2521_verify.json`. Frame of record: Phase
166 pin, Gate-19-corrected tensor, venv python, float64.
Total stress = G/8π is the read itself. Datum ≠ construction;
jet scope. INTERNAL only; no ledger append, no launches, no
user contact; nothing outside `phase252/` edited
(protected-file md5s identical before/after, checker-verified
live). Driver wall 24.8 s, checker 19.6 s — no run approached
the 900 s rule; no kernel spec owed.

## Verdict (registration §2.3 form 3, verbatim in substance)

**CAP PROTECTS NOTHING CURRENT** — no H-condition fails
anywhere in the swept range [0, −2.5] at any registered
instant, AND no soft scale plausibly reconstructs the cap's
intent (S1, §4: 0.8 is 4.0× the base J[Auu] profile scale and
8.0× the CH-COMB-class offset — plain round multiples, with
no condition, sign change, or scale event at 0.8 itself; the
posed Auu entry crosses zero at |a| = 0.2, not 0.8). **The
cap's true boundary is NO FINITE BOUNDARY IN THE AUDITED
RANGE** — the sweep end |a| = 2.5 is the audit's limit, not a
boundary. Provenance (§2): **nothing in the record ever
derived 0.8** — it enters in Phase 234 §3 as an assertion
("the registered cap (NC-a's basis)"), and NC-a's floor was
itself priced *against* it, circularly. Per registration §3,
Item 2 therefore runs with B := 2.5 operational stop (form 3
branch).

Interpretation notes, recorded in the driver header BEFORE
the sweep ran (no registration amendment was forced):
(i) H2 liveness is the PR-φ-3 read of record (max clause diff
vs the a = 0 headline read > 1e-3); at exactly a = 0 the
channel is absent and liveness is 0 by construction — that
degenerate point is on the stored grid (flagged there) and is
not counted as an amplitude-failure onset; the onset scan
runs over |a| ∈ [0.05, 2.5]. (ii) H3's flare/domain bars are
the base-pose bars of record (Phase 246 memo §4 fence: the
flare bar is a property of the base pose and is not re-read
on the posed jet — re-reading it on the posed Auu would
"fail" already at the standing primary a = −0.5, contradicting
the record's own non-clause bars); the posed Auu value
0.2 + a is recorded at every grid point. (iii) H1's linear
prediction is base NEC_φ grid min + a·s(argmin_base) with s
the stored Phase 246 profile at t = 0.25 / 0.475; at t = 0
(no stored profile) s was computed by the identical per-index
FD machinery — which reproduces the stored profiles at the
other two instants at **diff 0.0** (checker-verified), so the
t = 0 profile stands on validated machinery. Pointwise
exactness (max over θ of |profile − (base + a·s)|) was also
recorded at every grid point, so the H1 read is not an
argmin-migration artefact either way.

## 1. Controls (run first; all PASS)

- **CTRL-A (untrimmed bracket) PASS.** Composed sampled reads
  vs Phase 246 stored, first 21 instants: max abs clause-stat
  diff **0.0**. Anchors: NEC_φ worst over [0, 0.475]
  +0.093089 @ 0.475; NEC_ρ +1.295071 @ 0.475; first sampled
  fail t = 0.5 at NEC_φ −0.081831. Refined first-crossing
  bracket **(0.4875, 0.49375]**, carrier NEC_φ = DEC_φ,
  bracket-end margins **+0.008513 / −0.035909** — the
  registration's values, at diff 0.0 on the margins
  (checker fresh-recomputed both ends).
- **CTRL-B (trimmed bracket) PASS.** Stored constants
  re-derived: q₂ = −6.062835, s̄ = 1.154083, c_trim =
  −q₂/s̄ = **+5.253378**; clamp instant
  √(0.3/c_trim) = **0.238969**. Refined bracket
  **(0.525, 0.53125]**, carrier NEC_φ = DEC_φ, margins
  **+0.042998 / −0.012405**.
- **CTRL-C (static pin) PASS.** S(θ*) = −4.0625, NEC_ρ min
  = −4.0625, identity deviation ≤ 8.9×10⁻¹⁶ class, Wuu-solve
  residual ≤ 1e-9 — both arms.

## 2. Provenance — the table

Exhaustive search: every registration and memo in phases
221–248 was grepped for the cap and for amplitude bounds on
this channel (`|a|`, "amplitude cap", "0.8" in cap context).
The complete locus set is:

| # | locus | verbatim substance | what it derives 0.8 from |
|---|---|---|---|
| P1 | Phase 234 registration §2 (NC-a) | the authority floor \|med\| ≥ 0.5 is justified as what a receiver needs to price the deficit of record (−0.884152 at t = 0.6, ρ-only arm) "inside the registered amplitude cap \|a\| ≤ 0.8 of §3, even at perfect delivery" | nothing — it *uses* 0.8 as a given to size the 0.5 floor (0.5 × 0.8 = 0.4 of guaranteed-floor lift is the scale of the argument); the direction of derivation runs cap → floor, not condition → cap |
| P2 | Phase 234 registration §3 | "\|a\| ≤ 0.8 is the registered cap (NC-a's basis). No other amplitudes are marched…" Amplitude plan PRIMARY 0.5 / DESCRIPTIVE 0.25 priced beneath it, on the deficit record | **nothing. This is the cap's point of entry into the record, and it is an assertion**: no health, regularity, linearisation, liveness, or delivery condition is stated in §3 (or anywhere in the registration) from which 0.8 follows |
| P3 | Phase 246 registration §3 | "cap \|a\| ≤ 0.8 as in Phase 234" — inherited verbatim; amplitudes 0.5 / 0.25 re-priced against this datum's 0.6298 deficit | nothing — inheritance |
| P4 | Phase 246 memo §5 | the named successor prices "a larger registered amplitude inside the \|a\| ≤ 0.8 cap" | nothing — inheritance (and the successor question this phase answers) |
| P5 | Phase 248 registration §B2 | "\|a(t)\| ≤ 0.8 at every instant (Phase 246 §5's registered cap)"; the trim law runs clamped | nothing — inheritance; this is where the cap first *binds* a result (clamp at t = 0.238969) |
| P6 | Phase 248 memo §4 / CHECKPOINT248 | "outside the \|a\| ≤ 0.8 cap by 0.72" (of a* = −1.517513); "the transfer is cap-limited, not law-limited" | nothing — inheritance, with the cap's price first measured |

Negative space, confirmed by the same search: Phase 224's
channel family (the machinery the cap governs) registers
amplitudes **a ∈ ℝ unbounded** ("reads are per-unit-amplitude";
finite-amplitude spot checks only); Phase 224's |a| ≈ 0.1
bump saturation is a *measured* saturation of localised
members, expressly not applied to the flat member; Phases
229/233 pose CH-COMB flat at a = +0.10 (a posed value, not a
cap); Phase 243's certification registration contains no
statement of the cap at all. **No locus in phases 221–248
derives 0.8 from any condition. The cap is a bare registered
assertion of Phase 234 §3, inherited verbatim ever since,
whose only "basis" (NC-a) was priced against the cap itself.**

Sibling bounds on this channel (inventory, classified):

| bound | level | class |
|---|---|---|
| PRIMARY / DESCRIPTIVE plan amplitudes | 0.5 / 0.25 | **plan** — amplitudes chosen for the marches, priced against the deficits of record; not bounds on posing |
| NC-a authority floor \|med\| ≥ 0.5 | 0.5 | **criterion** — a qualification bar on receivers, priced AGAINST the cap; not a bound on posing |
| PR-φ bars: liveness > 1e-3; Wuu-solve residual ≤ 1e-9 | — | **checks** — pose-refusal conditions; their amplitude-failure points are candidate boundaries, tested as H2 in §3 |
| CH-COMB flat fence \|a\| ≤ 0.10 (Phase 226/229, ρ channel) | 0.10 | **cap (other channel)** — a scope fence on the ρ profile channel's own registrations; does not govern CH-PHI-Auu |
| \|a\| ≤ 0.8 (CH-PHI-Auu) | 0.8 | **cap** — the audited bound; provenance P1–P6 above |

## 3. Boundary sweep (§2.2) — no H-condition fails anywhere

Composed combined-class datum, flat Auu member under
P-PHI-FROZEN-246; a over [0, −2.5] at resolution 0.05 (51
points) at t ∈ {0, 0.25, 0.475} (march indices 0, 100, 190).
Base NEC_φ minima / argmins: t = 0: +0.593750 @ idx 90 (θ*);
t = 0.25: +0.371598 @ θ*; t = 0.475: −0.461412 @ θ*.
Sensitivity s(argmin): −1.250000 (t = 0, FD; the t = 0 profile
is exactly constant: median = min = max = −1.250000),
−1.207062 (0.25), −1.109004 (0.475); gain-signed floors
1.250 / 1.207 / 1.109.

**H1 — delivery exactness: PASS everywhere.** Max
|measured − linear| on NEC_φ,min over the whole grid:
1.6×10⁻¹⁰ (t = 0), 4.5×10⁻¹⁰ (0.25), 1.0×10⁻¹¹ (0.475) —
against the 1e-6 bar. Pointwise: max over θ and the whole
grid ≤ **7.8×10⁻¹⁰**. The flat Auu response is affine-exact
at every amplitude to 5× the standing primary — the Phase
234 prior (exact to 1.4×10⁻¹¹ at |a| = 0.5) extends over the
entire audited range with no onset.

**H2 — PR-φ liveness and solve: PASS everywhere.** Wuu-solve
residual max over the whole grid **3.9×10⁻¹⁶** (bar 1e-9).
Liveness (global max clause diff) grows linearly in |a|:
0.1875 at a = −0.05, 2.0000 at −0.8, 6.2500 at −2.5 (bar
1e-3); pointwise-min liveness at a = −2.5 is 6.25 / 6.04 /
5.55 at the three instants — live at every grid point, not
just in the max.

**H3 — non-clause bars: PASS everywhere.** Momentum max over
the whole grid **3.9×10⁻¹⁶** (bar 1e-10 — Auu is
momentum-free in this machinery at every amplitude). Base-
pose bars (a-independent, of record): flare_min 0.2000 /
0.1862 / 0.1546 > 0; domain R_min 0.8000 / 0.7715 / 0.6970
> 0; domain exp(2Φ)_min ≈ 0.005811 > 0 at the three
instants.

**H4 — t = 0 clause legality: PASS everywhere.** All seven
clauses ≥ 0 at t = 0 at every swept amplitude, and every
clause's minimum *grows* with |a| (the interference prior
survives and strengthens): worst-clause minimum at t = 0 is
+1.593750 (a = −0.8), +2.468750 (−1.5), **+3.718750**
(−2.5). No clause crosses; there is no first clause to name.

Sweep table (NEC_φ grid min / median / max; worst clause min):

| t | a = −0.8 | a = −1.5 | a = −2.5 |
|---|---|---|---|
| 0 | 1.593750 / 1.871321 / 2.062425; worst 1.593750 | 2.468750 / 2.746321 / 2.937425; worst 2.468750 | 3.718750 / 3.996321 / 4.187425; worst 3.718750 |
| 0.25 | 1.337248 / 2.045116 / 2.121776; worst 1.337248 | 2.182192 / 2.912077 / 2.994918; worst 2.182192 | 3.389254 / 4.150592 / 4.242524; worst 3.389254 |
| 0.475 | 0.425791 / 2.185030 / 2.609273; worst 0.425791 | 1.202093 / 3.047978 / 3.462896; worst 1.202093 | 2.311097 / 4.279227 / 4.684260; worst 2.311097 |

(Full 51-point × 3-instant grid, per-clause min/median/max,
in `p2521_results.json: sweep`. At a* = −1.517513 the NEC_φ
minima read by the exact affine response: +2.490641 at
t = 0 — between the −1.5 and −1.55 grid rows at the other
instants likewise; nothing stirs there either.)

Since no grid point failed, no bisection was owed; the
onset machinery ran and returned "no failure on
|a| ∈ [0.05, 2.5]" for every condition × instant pair
(13/13, stored in `failure_onsets`).

## 4. S1 — soft scales (reported; no stir at 0.8)

Base J[Auu] profile on the audit grid: constant +0.2 at all
three instants (max |J[Auu]| = 0.2, median 0.2, range 0.0 —
ratios to the range are undefined and are not used). Ratios
of |a| to the base profile scale (0.2) and to the datum's
other posed-offset class (CH-COMB +0.10):

| a | \|a\| / 0.2 | \|a\| / 0.10 | posed Auu (0.2 + a) |
|---|---|---|---|
| −0.8 | 4.0 | 8.0 | −0.6 |
| −1.517513 (a*) | 7.588 | 15.175 | −1.317513 |
| −2.5 | 12.5 | 25.0 | −2.3 |

0.8 sits at no event of the datum's own scales: the posed
Auu entry's zero-crossing is at |a| = 0.2; the sensitivity
profile, the delivery response, and every clause minimum
vary smoothly and monotonically straight through 0.8 (the
a = −0.8 sweep rows are unremarkable neighbours of −0.75 and
−0.85 in every stored column). 4.0× and 8.0× are round
multiples of scales the record never connects to the cap.
No soft scale plausibly reconstructs the cap's intent —
consistent with §2: the record states no intent beyond the
circular NC-a pricing.

## 5. The boundary, stated per §2.3

**NO FINITE BOUNDARY IN THE AUDITED RANGE [0, −2.5].** No
H-condition (delivery exactness, PR-φ liveness/solve,
non-clause bars, t = 0 clause legality) fails at any swept
amplitude or instant; the failing condition and failure
price required by the finite-boundary branch do not exist
to state. The sweep's end, |a| = 2.5, is the audit's limit,
not a boundary. Verdict form 3 fires (form 1's soft-scale
branch fails on §4; form 2 requires a boundary within
tolerance of 0.8 and there is none). Consequence per
registration §3: Item 2 runs at B := 2.5 operational stop —
at the wound bracket's far end the unclamped trim law reads
−2.162, so the stop does not bind that comparison.

## 6. Scope fences

Jet scope; sampled/spot instant reads; datum ≠ construction;
sector superposition (a posed Auu profile is posed jet data,
not a derived second derivative of a posed A field — Phase
234 §6). No certificate is claimed for any bracket here
(Phase 243/Gate-23 cover the wound pose only). Retiring the
cap in this phase is a finding about THIS datum's lifetime
question: the cap's standing in the wound line's
registrations (Phases 234/243) is untouched, and any
programme-wide discipline change is a framing decision above
this phase (Phase 245 §5 pattern). The audit range is
[0, −2.5]: amplitudes beyond |a| = 2.5 are unaudited, and
"protects nothing current" is stated for the conditions and
range registered, no further.

## Files

- `phase252/work/p2521_run.py` — driver (controls, provenance
  constants, sweep, onsets, S1, verdict; 24.8 s).
- `phase252/work/p2521_check.py` — independent checker,
  ALL PASS (65/65): fresh marches, bracket-end and sweep spot
  recomputation at diff 0.0, full-grid no-failure consistency,
  S1 arithmetic, verdict consistency, protected md5 live.
- `phase252/results/p2521_results.json` — full reads
  (controls, 51×3 sweep grid with per-clause min/median/max,
  sensitivity profiles, base-pose bars, onsets, S1).
- `phase252/results/p2521_verify.json` — checker record.
- `phase252/results/p2521_memo.md` — this memo.
