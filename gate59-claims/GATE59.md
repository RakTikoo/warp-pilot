# GATE-59 REPORT — Phase 431's persistent-mating claim set, re-judged

**Gate:** Gate-59 (ledger entry 1151).
**Subject:** Phase 431, THE DEGENERATE MATING (ledger entry
1150) — persistent matings for the two standing supply
targets.
**Verdict of the gate: PASS — the claim set SURVIVES as
fenced, with three corrections to the phase's printed
record (§6) that touch no verdict.** All four arm/target
verdicts are confirmed on the gate's own machinery; the
Arm A / T_req negative is ruled **STRUCTURAL AT THE
REGISTERED SCOPE, carried by the anatomy** (§5, rider
G59-R3).

## Three goals (on the face)

- **(1) FTL drive/mechanism:** the formation complex's
  supply leg is confirmed answerable in principle —
  persistent matings exist for both standing targets at
  prices below the drifting fits. No sustainment is
  claimed: 428's geometry leg (GAP-3, a four-condition
  geometry) still gates every sustainment claim, and
  nothing in this gate touches it.
- **(2) Functional wormhole:** untouched — no throat read
  in this gate.
- **(3) Subluminal record:** untouched — the graded best
  stands at 0.194140625 (Gate-57); the step-profile
  category stands (Procaccia 0.1363; programme best 0.10).

**DESK: NO DATA CONTACT.**

## §1 Machinery and admission

The gate does not reuse the phase's evaluator for any
deciding read. Every deciding read was taken with the
gate's own implementation (`gate59/work/g59_lib.py`),
written from the definition: Dirac-representation gamma
matrices built in the file, positive-energy spinors in
the record's form, the field assembled mode by mode, and
the stress tensor evaluated from the field bilinear
T_ab = (i/4)[ψ̄γ_a∂_bψ + ψ̄γ_b∂_aψ − (∂_aψ̄)γ_bψ −
(∂_bψ̄)γ_aψ] directly — a different organisation from the
phase's pairwise-S machinery. The gate's pair kernel
(derived in the file from the same bilinear) was
validated against the gate's field path on random
superpositions (agreement 3.2×10⁻¹⁶ relative) and is used
only where the field path is not evaluable (long grids,
window spots) — the same division of labour the record
itself uses, with both paths the gate's own. Self-tests
in the file: Clifford algebra exact; Dirac residuals
~10⁻¹⁵; single-mode stationarity at roundoff. All
deciding reads on the VM (programme venv, numpy 2.5.5 /
scipy 1.18.1 — the Phase-166 pin, frame of record),
float64. Every audited object was sha256-recorded before
any read (`results/g59_audit.json`).

**Laptop admission (corroboration only):** the admission
object (Phase 410 Fit A's t = 0 read) was re-run on the
pool with the gate's own lib (staged files md5-verified
against the VM): laptop maxR (pair) 2.9659850903775113×
10⁻¹² vs the VM gate read 2.965984413711632×10⁻¹² — diff
6.8×10⁻¹⁹, far inside the 1×10⁻¹³ admission bar; the
pool's priority run (Phase 368 step 2) was live and
undisturbed. ADMITTED as corroboration.

**Checker:** the phase's coordinator checker
(`phase431/work/p431_check.py`) re-run at the gate:
**ALL PASS**, and its output file is identical to the
stored record.

## §2 Controls (re-derived before any mating was believed)

- **CTL-431-0 (Fit A reproduction):** gate field maxR
  2.9659839407219894×10⁻¹² — the stored direct value
  digit-for-digit; gate pair maxR 2.965984413711632×10⁻¹²
  — the phase's own reproduction digit-for-digit (the
  stored pairwise figure, 2.9659878908312287×10⁻¹², sits
  3.5×10⁻¹⁸ away, the record's known two-path spread).
  Price |a|² = 0.029266406597128584, exact.
- **CTL-431-1 (C-A reproduction):** gate pair maxR
  3.49600985773513×10⁻¹⁰ — the stored value digit-for-
  digit; gate field 3.496009861987862×10⁻¹⁰ — 420's
  stored direct value digit-for-digit. Prices exact:
  fam1 0.029172052178672605, fam2
  2.0362442383995038×10⁻⁶, total 0.02917408842291128.
- **CTL-431-3 (B-2 self-checks, gate's lib):** single
  mode (Fit A mode 6 at A1): max normalised T difference
  over 17 instants 3.7373020080051595×10⁻¹⁶ — the stored
  value (3.73730200800516×10⁻¹⁶) to all printed digits.
  Two-mode beat (modes 6 & 2, ΔE = 0.2536221530926388,
  exact): the gate's return and anti-phase errors are
  2.04×10⁻¹⁶ and 4.07×10⁻¹⁶ normalised — roundoff class,
  consistent with the stored 1.22×10⁻¹⁵ / 2.04×10⁻¹⁶ at
  the precision the definitions support (the gate's
  return error equals the stored anti-phase figure
  digit-for-digit; no claim turns on the assignment).
- **Targets integrity:** the two target files' site sets
  are identical; the inter-target distance recomputes to
  1.6945974153888293×10⁻⁴ (the stored sweep minima,
  1.6945974196533054×10⁻⁴ / 1.6945985678760018×10⁻⁴,
  differ at 4×10⁻¹³ — the unconstrained fits' own
  residuals, as expected).

## §3 The three ADMITS — confirmed

Gate reads (field path / pair path) vs the phase's stored
driver (pairwise) and checker (direct) values:

| mating | gate field | gate pair | stored |
|---|---|---|---|
| B / T_req (N = 6, L3) | 1.3398×10⁻¹⁶ | 1.3730105602628296×10⁻¹⁶ | 1.3730105602628296×10⁻¹⁶ |
| A / T_corr ((6,6)) | 9.9274×10⁻¹⁵ | 9.969570519623321×10⁻¹⁵ | 9.969570519623321×10⁻¹⁵ |
| B / T_corr ((6,6) L3) | 1.2118×10⁻¹⁵ | 1.2310921712911173×10⁻¹⁵ | 1.2310921712911173×10⁻¹⁵ |

Spectra recomputed from the stored vectors: B/T_req rung
ratios exact (max dev 0.0; rungs (1,1,2,2,3,3),
E₀ = 1.0191336197578293); B/T_corr max ratio dev
4.440892098500626×10⁻¹⁶ (representation level); A/T_corr
scatter 4.440892098500626×10⁻¹⁶. Prices recomputed
exactly: B/T_req |a|² = 0.013963391555057172 = **0.4771×
Fit A**; A/T_corr 0.02407134655563152 (fam1
0.010002960189597976 + fam2 0.014068386366033546) =
**0.8251× C-A**; B/T_corr 0.017173314465132507 =
**0.5887× C-A**. Supplier densities (the gate's T₀₀ per
site) reproduce the stored ρ_sup; Dirac residuals
reproduce the stored values digit-for-digit; the
supplied tensors are symmetric to ≤1.4×10⁻²⁰.

**Persistence (the gate's B-2 reads, `results/
g59_b2.json`):**
- **A / T_corr — stationary by construction.** With the
  registered energy, R_F(t) is constant: the gate's grid
  read over [0, 2×10⁵] deviates from R_F(0) by 0.0
  (bit-identical contraction), and the window spots
  {W/4, W/2, W} read 9.953822294003724×10⁻¹⁵ (pair form —
  the phase supplement's own Acoef value, digit-for-
  digit) and ≤9.927×10⁻¹⁵ (the gate's factored direct
  form). The mating's stationarity across the full
  3.860 yr window is confirmed in both evaluable forms.
- **B / T_req — periodic by construction.** T_c =
  6.165222288194773 units (2.06×10⁻⁸ s);
  5.923×10¹⁵ cycles in the window. Worst instant over
  the period: **0.20790521338785312** (gate pair grid,
  digit-for-digit the stored value; the gate's direct
  field grid concurs, 0.20789 on a coarse grid).
  Ladder returns n = 1…1024: ≤1.155×10⁻¹³ (gate pair
  form), ≤1.399×10⁻¹⁴ (gate direct form) — against the
  Form P per-cycle bar 1×10⁻⁶, seven orders inside.
- **B / T_corr — periodic by construction.** T_c =
  5.330800806832096 units (1.78×10⁻⁸ s);
  6.850×10¹⁵ cycles. Worst instant **0.656877388021271**
  (digit-for-digit). Ladder returns ≤1.005×10⁻¹³ (pair)
  / ≤7.850×10⁻¹⁴ (direct) vs the same bar.

The stored ladder tables' individual entries (e.g.
4.706×10⁻¹⁴ at 2¹⁰ for B/T_req) are evaluation-form
values at the 10⁻¹³–10⁻¹⁴ argument-reduction floor and
differ between forms at that level; the certificate
content — every return ≤ ~10⁻¹³, seven orders inside
the 1×10⁻⁶ bar — is form-independent and is what the
gate confirms (rider G59-R2).

## §4 The Arm A / T_req mating itself (the negative's subject)

The confirmed mating (N = 12) reproduces exactly: gate
field maxR 1.2754152716575767×10⁻³ (the checker's stored
direct value digit-for-digit), gate pair
1.275415271657572×10⁻³. Price |a|² = 5.998223488760628
= **204.9× Fit A**. Its spectrum scatter is exactly 0.0
— the stored momenta sit on one shell to the last bit —
so its stationarity is exact in every form: the gate's
registered grid deviates 0.0, and the window spots read
R_F(0) in both evaluable forms (pair
1.2754152716575808×10⁻³; factored direct
1.2754152716575767×10⁻³), confirming the phase's
supplement. **The found mating persists; what fails is
expressibility** — the phase's central anatomical claim
about this arm is confirmed before the negative itself
is re-examined.

## §5 The negative re-examined — anatomy, rigidity, search, relaxation

**Anatomy (gate-recomputed; identical to the stored
anatomy at every component).** At the confirmed mating
the residual is carried by the spatial diagonals,
nearly isotropically, at all three sites: A3_peak
T11/T33/T22 = 7.3962/7.3551/7.3393×10⁻⁴; A2_sec_argmin
≈ 2.00–2.03×10⁻⁴ each; A1_joint_argmin ≈ 3.13–3.29×
10⁻⁵ each. The density is matched (T00 ≤ 4.1134×10⁻⁶,
at A3) and every off-diagonal is ≤ 1.1108×10⁻⁶ (T23 at
A3) — three orders below the diagonal shortfall. (The
phase memo's blanket "off-diagonals ≤ 3.1×10⁻⁷" is
A1's figure, not the maximum; correction §6(c).)

**Local rigidity (gate-recomputed).** The constrained
Jacobian at the reconstructed registered θ (the gate's
own parameterisation build and residual; central FD at
the phase's recipe h = 1×10⁻⁶·max(1,|θ_j|), and at
h = 3×10⁻⁷): **rank 30/30** at 1×10⁻¹⁰ relative
tolerance at both step sizes; σ_min =
5.408346221368049×10⁻⁴ (h = 1×10⁻⁶) /
5.408339163078754×10⁻⁴ (h = 3×10⁻⁷) — the phase's
5.408373155676678×10⁻⁴ reproduced to 7×10⁻⁹ relative;
σ_max 2851.686640572 (stored 2851.686640830). The
found point is a genuine, shallow, strict local
minimum of the constrained problem — not a singular
artefact, not an optimiser stall.

**Independent search (gate's implementation, the
A1/A2 protocol).** Warm-started from the stored
mating, the gate's search re-converges to the same
basin and its polish lands at **1.271574327515576×
10⁻³** — 0.13% *below* the phase's best
(1.27316549597957×10⁻³, N = 8). Nineteen fresh random
starts of the gate's (N = 6: six, 1.662–1.932×10⁻³;
N = 8: six, 1.669–1.886×10⁻³; N = 12: four,
1.685–1.868×10⁻³; N = 16, beyond the registered
scope: three, 1.652–1.879×10⁻³) find nothing lower,
mirroring the phase's own start pattern (its random
starts: 1.47–2.03×10⁻³; its best from warm starts).
Two independent implementations, 50 starts between
them (the phase's 30, the gate's 20), one floor:
≈ 1.27×10⁻³, six orders above the bar, flat in N.

**Per-site relaxation (the decisive read).** The
joint problem couples the sites through shared
amplitudes and directions; the gate decoupled it. At
each site separately, a dense fixed dictionary (96
Fibonacci directions × 2 spin basis = 192 modes, all
on one shell) with **free per-site amplitudes** was
fitted by Adam + Gauss–Newton polish (analytic
Jacobian) — a feasible set strictly containing the
joint problem's per-site behaviour. The converged
floors equal the joint fit's per-site residuals at
every site:

| site | relaxation floor (E = 1.005853) | joint fit residual |
|---|---|---|
| A1_joint_argmin | 6.4090×10⁻⁵ | 5.6074×10⁻⁵ |
| A2_sec_argmin | 3.5095×10⁻⁴ | 3.4859×10⁻⁴ |
| A3_peak | **1.2852×10⁻³** | **1.2754×10⁻³** |

At A3 the floor was scanned over E ∈ {1.005853, 1.2,
1.5, 2.0, 3.0, 4.3}: minimised at the mating's own
energy and rising monotonically (1.2852 → 1.4414 →
1.5977 → 1.7351 → 1.8659 → 1.9139, ×10⁻³) — no shell
energy escapes it. The relaxation's best A3 fit
carries the **same anatomy** (diagonals
7.72/7.65/6.84×10⁻⁴; next component 3.5×10⁻⁵) at a
price of only |c|² ≈ 0.178 (vs the joint mating's
5.998): the obstruction is not amplitude budget,
not mode count, not site coupling, and not search.
It is what a single shell can express at one site.

**Ruling (G59-R3): STRUCTURAL at the registered
scope, carried by the anatomy.** The Jacobian-rank
anatomy does not stand alone — a full-rank Jacobian
proves local rigidity, not global impossibility —
but it does not have to: the per-site relaxation
moves the obstruction out of the search entirely
and into the single-shell family's expressiveness
at a site, with the joint floor, the relaxation
floor, and the residual anatomy coinciding. The
negative is therefore quotable as a structural
property of the single-shell family at these sites,
in the fenced form of rider G59-R3 — with its scope
attached and its one stated limit: the relaxation's
dictionary is finite (96 directions; pair kernels
vary smoothly with direction, so a span defect at
the 10⁻³ scale is implausible but not excluded), and
no analytic impossibility proof exists or is
claimed. An exhibited single-energy mating at the
bar reopens the arm at once.

## §6 Three corrections to the printed record (no verdict touched)

**(a) The representation bound t\* for Arm A / T_corr.**
The phase prints t\* = 3.573×10⁷ units = 0.119 s (the
verbatim stored-pvec crossing of the 1×10⁻⁹ bar). The
gate finds that value is an artefact of its evaluation
form. The driver's spots and crossing were computed in
the per-mode-phase form (B2.RF_t — the same form the
registration itself superseded for the window spots):
at E·t ≳ 10⁷ its float64 argument rounding injects
phase noise of order the effect being measured. The
gate reproduces the phase's stored spots digit-for-
digit in that form (5.5258556341232435×10⁻¹² at 2×10⁵ …
4.6802065711613605×10⁻⁹ at 2×10⁸) — and then evaluates
the same stored floats faithfully, two ways: the ΔE
(Acoef) pair form (the form of the phase's own grid
read, whose [0, 2×10⁵] maximum the gate reproduces
exactly, 2.9755557716447667×10⁻¹²) and a per-mode form
with the phase argument reduced mod 2π in longdouble.
The two faithful forms agree to 0.03% on the crossing:
**t\* = 6.72×10⁷ units = 0.224 s** (Acoef 67210312.02;
longdouble per-mode 67187297.34). At the printed
3.573×10⁷ the faithful R_F is 5.32×10⁻¹⁰ — still below
the bar. The correction makes the bound *stronger*;
t\* is a representation bound on the stored floats,
not a certificate term — the Arm A / T_corr
certificate rests on the construction and the
registered-E reads of §3, which are exact.

**(b) The "24 orders of magnitude" gloss.** The memo,
checkpoint and ledger entry 1150 describe t\* as "24
orders of magnitude beyond the unconstrained fits'
2.42×10⁻¹⁷ s". That is an arithmetic error: 0.119 s /
2.422×10⁻¹⁷ s = 4.9×10¹⁵ ≈ 15.7 orders; with the
faithful t\* (0.224 s) the ratio is 9.3×10¹⁵ ≈ **16.0
orders**. The quotable comparison is ~16 orders
(rider G59-R4).

**(c) The off-diagonal bound in the anatomy.** The
memo, checkpoint and ledger entry 1150 state the
Arm A / T_req residual's off-diagonals as
≤ 3.1×10⁻⁷. That is the maximum at A1; the largest
off-diagonal residual overall is 1.1108×10⁻⁶ (T23 at
A3), with A2's at 9.118×10⁻⁷. The gate's recomputed
anatomy agrees with the phase's stored per-component
table digit-for-digit — only the summary figure in
the prose is wrong. Immaterial to the anatomy claim
(the off-diagonals remain three orders below the
diagonal shortfall); the quotable bound is
≤ 1.11×10⁻⁶ (rider G59-R3).

## §7 Riders decided by the gate

- **G59-R1 (the quotable form of "persistent", per
  mating).** *Arm A / T_corr is persistent in the
  STATIONARY form: one registered energy
  (E = 2.189896), the supplied tensor constant by
  construction, B-2-confirmed at the registered energy
  over the full window in both evaluable forms.
  Arm B / T_req and Arm B / T_corr are persistent in
  the PERIODIC (Form P) form: exact integer ladders
  (rungs (1,1,2,2,3,3) of E₀ = 1.019134 / 1.178657),
  common periods 6.165222 / 5.330801 units, ladder
  returns ≤ ~10⁻¹³ at 2¹⁰ cycles against the 1×10⁻⁶
  per-cycle bar. "Persistent" is never quoted without
  its form (stationary / periodic) attached.*
- **G59-R2 (worst instants are geometry-side inputs).**
  *Every quotation of a ladder mating carries its
  worst instant over the period — R_F = 0.20791
  (T_req, at t = 2.1565) and 0.65688 (T_corr, at
  t = 2.9974) — labelled as the input a geometry-side
  worst-instant legality read would consume, never as
  a supply-certificate term: within a period the
  supplied tensor departs from the fixed target by
  that much, and a geometry mated to it must be legal
  at every instant of the period, which no standing
  geometry is (§8 fence). Ladder-return entries are
  quoted at their form-independent content (≤ ~10⁻¹³
  at 2¹⁰ cycles), not as single-form table values.*
- **G59-R3 (the negative's quotable form).** *Arm A /
  T_req DOES NOT ADMIT — structural at the registered
  scope: in the record's mating machinery at Phase
  410's sites, no single-energy (single-shell,
  m = 1) supply mates T_req at the 1×10⁻⁹ bar. The
  best fits stall at maxR ≈ 1.27×10⁻³ with the
  residual carried almost isotropically by the
  spatial diagonals (peak site 7.40/7.36/7.34×10⁻⁴;
  T00 ≤ 4.12×10⁻⁶; off-diagonals ≤ 1.11×10⁻⁶); the
  constrained Jacobian at the optimum is full-rank
  (σ_min 5.41×10⁻⁴); and a per-site relaxation with
  free amplitudes over a dense direction dictionary
  floors at the same per-site residuals (peak site
  1.285×10⁻³) — a single-energy supply cannot
  express T_req's principal pressures. Scope: joint
  searches to N = 12 (16 probed) by two independent
  implementations; relaxation dictionary 96
  directions per site; no analytic impossibility
  proof is claimed, and an exhibited single-energy
  mating at the bar reopens the arm.*
- **G59-R4 (the representation bound).** *Arm A /
  T_corr's verbatim representation bound is quoted as
  t\* = 6.72×10⁷ units = 0.224 s (faithful forms; the
  phase's printed 0.119 s is the per-mode-form value,
  superseded), and the comparison to the unconstrained
  fits is ~16 orders of magnitude, never 24.*
- **G59-R5 (prices).** *Prices are quoted as the
  gate-recomputed ratios: B/T_req 0.4771× Fit A;
  A/T_corr 0.8251× C-A; B/T_corr 0.5887× C-A;
  A/T_req's found mating 204.9× Fit A. (The phase's
  rounded 0.48× / 0.82× / 0.59× / 205× are consistent
  with these.)*

## §8 The fence (on every quotation of this set)

428's functional has two legs. This set satisfies its
**supply leg in principle** for both standing targets
(Route A stationary for T_corr; Form P periodic for
T_req and T_corr). Its **geometry leg — GAP-3, a
four-condition geometry with J ≥ 0 and SEC_min ≥ 0 at
gate scope — is untouched and still gates every
sustainment claim.** The targets' own status stands:
the 405 winner's geometry fails SEC (stored SEC_min
−2.213557×10⁻⁴, Gate-50 record), and **T_corr is a
construction of Phase 420 — a corrected target tensor,
not a geometry**. Test-field scope throughout: a
persistent supply is not a sustained geometry.

## §9 The ACTIVE SUPPLY disposition

Entry 1136's wild attack 1 (THE ACTIVE SUPPLY —
continuously re-phasing the modes) was premised on no
persistent mating existing. With persistent matings
confirmed for both standing targets (§3), **the gate
rules the premise FALSIFIED for both targets: the
ACTIVE SUPPLY is never quotable as a live route for
these targets.** It remains the named road only for a
future target that defeats both arms — the disposition
the phase itself registered.

## §10 Process record (disclosed on the face)

- The phase's Amendments A1 (search at the record's
  default-tolerance precedent with a tight polish; the
  polished point is the candidate of record) and A2
  (search cap 4000 → 1200 on the record's convergence
  evidence) were reviewed against the banked JSONL
  record and stand as disclosed; no bar, size list,
  start list or verdict form changed under either.
  The gate's own search (§5) followed the same A1/A2
  protocol.
- The phase's two incidents (a warm-start padding
  crash, fixed with 410's pattern; a silent mid-run
  death under shared-VM memory pressure, resumed from
  banked JSONL state) are on the phase's face; the
  gate's re-derivation is independent of the affected
  runs' bookkeeping — the matings of record were
  re-read from their persisted vectors.
- The phase's window-spot supersession (supplement):
  the gate confirms it — the supplement's Acoef spots
  for A/T_corr reproduce digit-for-digit in the gate's
  pair form, and its factored-direct spots in the
  gate's factored form. The same form limitation is
  what §6(a) corrects in the verbatim spots, which the
  supplement did not cover.
- The driver's stored `first_crossing` for the
  A/T_req mating (3.111507638930571×10⁻⁷³) is a
  numerical artefact of running a crossing-finder on a
  constant above-bar function; it appears in no claim
  and the gate notes it only for the record.
- Gate-side incidents, all disclosed, none affecting
  any deciding read:
  (i) The gate's first grid script called its grid
  routine without the mass array and produced NaNs;
  caught before any number was used, fixed, re-run —
  the affected run's outputs were discarded entire.
  (ii) The gate's Arm A script (search + first-pass
  relaxation) died in a service restart after its
  search completed and before it wrote its JSON —
  the same failure mode as the phase's own Incident
  2. Its per-start search values survive in its log
  (`work/g59_armA.log`) and are transcribed in
  `results/g59_armA.json` marked as transcribed; the
  anatomy, both Jacobians and the decisive N = 12
  warm re-convergence were recomputed in a recovery
  run (`work/g59_armA_recovery.py`) and reproduce
  the logged values (σ_min bit-for-bit at both step
  sizes; warm search 1.2734805813737378×10⁻³ vs the
  logged 1.273481×10⁻³). The random-start sizes'
  polish outcomes were in memory at the restart and
  were not re-run; their search-pass values stand
  (all ≥ 1.65×10⁻³, far from the floor basin, and
  the phase's polishes of like starts stayed
  ≥ 1.47×10⁻³).
  (iii) The relaxation's first pass (1500-step Adam)
  did not converge and is superseded entire by the
  converged relaxation of §5 (Adam + analytic-
  Jacobian Gauss–Newton polish); the first-pass
  numbers are kept in the record marked
  undertrained. In the converged run's other-sites
  loop, each site was run twice at the same energy
  with the same seed (the scan's best energy equals
  the stored energy) — a redundancy in the gate's
  script, producing identical values; no
  independent-seed claim is made from them.
  (iv) A gate `pkill` matched the gate's own shell
  once (the failure mode the phase's checkpoint
  itself warns of); the only casualty was the
  already-superseded first relaxation process.
