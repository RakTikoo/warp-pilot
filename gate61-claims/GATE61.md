# GATE-61 REPORT — Phase 478's two shadow data (X(m) and
# H(0)) and the identity ruling's three legs

**Verdict: PASS WITH RIDER.** Phase 478's claim set
survives independent re-judgement in full: the identity
ruling **stands as a ruling** on all three legs (§3);
both shadows' full seven-clause vectors reproduce on
the gate's own machinery at diff **0.0** and are
strictly positive (§4); the D-identity re-derives
symbolically and by perturbation on both shadow paths
(§5); legality is scale-invariant as computed at the
rescue rung and at 2.5×10⁸ m (§6); and both rescue
radii and E_shell values confirm by 467's method,
with the closed forms recomputed at 50-digit mpmath
and the tides cross-checked on the gate's own
FD-Riemann second path (§7). The single rider
(G61-R1, §9) restates no figure of the claim set: it
corrects a fence sentence in the printed record of
Phases 467/477/478 (the combined march's status),
which the gate's G3 scan brought to light. Everything
verdict-carrying is intact.

Charge: ledger entry 1243. Claim under judgement:
ledger entry 1242 (Phase 478, CHECKPOINT478.md,
results/p478_memo.md). Ground records: entry 1238
(Phase 477 trace), entry 1236 (Phase 467 pricing).

**Wording discipline (in force on every number
below):** neither the P226-1 datum nor either shadow
is the Gate-27 certified pose and none carries a
certificate. Jet scope, t = 0, sector superposition,
exhibit ≠ construction, sustainment untouched. **No
traversability claim is made anywhere in this
report.**

**The three goals:** (1) FTL drive — no contact.
(2) Functional wormhole — this gate's home goal: the
wormhole line's two shadow data stand as verified
data of the P226-1 class, and the datum's identity
ruling stands. (3) Subluminal record — no contact.

**DESK: NO DATA CONTACT.**

## 1. Machinery (the gate's own)

Every deciding read was computed by the gate's driver
(`gate61/work/g61_run.py`), written from the stored
definitions (registration: `gate61/work/
g61_registration.md`, filed before computation). The
two builds under judgement are *defined* by stored
code, and those defining modules are imported as the
builds' definitions — the Phase 162 engine
(`instant_jets` / `channels`, the (A1) anchor ODE) for
the home build per P226-1 registration §2, the Phase
167 engine (`comp_jets` / `mtt_field`) for the
compensated build, and `lateral_tide` as the record's
tide sampler. Everything downstream of the channel
arrays is the gate's own: its own CH-COMB posing, its
own director addition (c₁ recomputed from the
registered formula), **its own clause arithmetic**
(the seven clauses implemented from their definitions
ρ + pᵢ, ρ, ρ − |pᵢ|; cross-checked pointwise against
the engine's `clauses_of` under CTL-CLAUSE at max abs
diff 0.0 — the checker's deciding path then used the
engine's clauses, so the two clause paths cross-check
each other), its own scale reads, its own
rescue/β-ceiling arithmetic with the closed forms
recomputed at **50-digit mpmath**, its own E_shell
quadrature (scipy Simpson base; gate fine Simpson for
the director term, cross-checked by 50-digit mpmath
quadrature at rel diff 1.5×10⁻¹⁵), and its own
**FD-Riemann second tide path** (P254-2 pattern,
gate implementation). The documentary legs were
judged on the stored texts read directly by the gate,
with the gate's own counts, text extractions and
absence scan (§3). 478's JSONs were read only as the
claim's printed values, after the gate's reads
existed. All deciding reads are VM reads (programme
venv, Phase-166 pin — frame of record), float64. The
pool was not used.

## 2. Controls (all before any deciding read)

- **CTL-H PASS (diff 0.0).** Base C-κ0 minima and the
  primary-point combined vector reproduce
  `p2261_results.json` on the gate's clause
  arithmetic at max abs diff 0.0; ũ_true(θ*) =
  1.1412482021558361.
- **CTL-CLAUSE PASS (diff 0.0).** Gate clause
  arithmetic vs engine `clauses_of`, pointwise on
  every channel set read.
- **CTL-X PASS (diff 0.0).** Phase 254's wound tide
  worsts reproduce `p2542_results.json` at abs diff
  0.0 on all three components; fallback anchors pass.
- **CTL-467 PASS.** 467's CTL-3 reproduced: Fuu diff
  0.9343747896249985, Mtt diff 2.569525345830215×10⁻⁷,
  R_tltl diff 0.765001585541698, R_tthtth / R_lthlth
  diffs 0.0; home radial worst 1.5202791951713714 at
  θ = π/2; X radial worst 0.9718746251967629.
- **CTL-477X PASS (diff 0.0).** All five 477 variant
  minima (35 clause minima) reproduced at max abs
  diff 0.0 on gate clauses.
- **Checker** (`work/g61_check.py`, separate
  process): **16/16 PASS** — CTL-H combined vector
  and both shadow vectors re-derived through the
  engine clause path at 0.0; rescue arithmetic
  recomputed from the stored worsts; E ∝ R ratios at
  ≤ 1.6×10⁻¹⁶; documentary counts re-verified;
  verdict consistency confirmed.

## 3. (a) The identity ruling — STANDS, on all three
## legs

**G1 (the build is fixed verbatim) — HOLDS.** The
gate quotes `phase226/work/p2261_registration.md` §2
from the file itself: "Datum build verbatim from
`phase224/work/p2242_run.py` (fine grid 2881, ũ_true
from the (A1) anchor ODE, `J0 = B.instant_jets(0,
0,0,0,0, ũ_a)`, `ch0 = B.channels(J0, AUDIT_TH)`,
clauses by `B.clauses_of`; engine
`phase162/work/p1621_engine.py`)". The gate's own
counts: `comp_jets` occurs **0 times** in both
`p2261_run.py` and `p2242_run.py` (`instant_jets`
once in each); `comp_jets` occurs 0 times in the
registration itself. The stored vector reproduces on
that build at diff 0.0 (CTL-H).

**G2 (the (A1) set is the datum's base set) —
HOLDS.** The gate extracted the (A1) set from
`phase169/results/p1691_run_record.md` (d)(A1)
itself — NEC_ρ = DEC_ρ = +0.43125000000000036,
NEC_θ = DEC_θ = +0.596875000000059, NEC_φ = DEC_φ =
−0.3406249999999409, WEC = +1.0624999999999998 — and
its own home-build base minima agree at max abs diff
**0.0**.

**G3 (the compensated pose is a different pose,
fenced off; no equal-standing registration poses the
combined datum in that family) — HOLDS, on a fuller
evidence base than 478 printed.** The (R1) text
stands verbatim in `phase167/CHECKPOINT167.md`
P167-1(c)(R1), read by the gate from the file: "The
compensated family is therefore NOT an extension of
the datum's Φ profile — it is a neighbouring pose
whose t = 0 CHANNEL VALUES coincide with the datum's
while its Φ_,ρρ jet differs by ΔJ... what is restored
is the audit's channel values, not the datum's jets."
For the absence, the gate scanned the record's
registrations / checkpoints / run records (scan set
**1380** files; **80** mention the compensated
machinery; **20** carry both compensated and
combined-datum markers) and classified every
both-marker file (full table in
`results/g61_results.json`): the director-alone line
(Phases 203, 221 — OTHER-DATUM); **the combined
march line (Phases 229, 233, 234 — OTHER-OBJECT)**;
the SOS and certified three-channel data (Phases
246, 249, 254, 260, 264 — OTHER-DATUM /
OTHER-OBJECT); 467 (COMPARISON); 477/478
(ARBITRATION); this gate (SELF). **No POSING-class
document exists.** Two classifications carry the
leg, and the gate states them plainly:

- *P229-1 (FU-P226-1, the combined march)* is the
  nearest document in the record: a sustainment
  registration that poses its marched jets on
  `comp_jets`. It does **not** pose the datum in
  that family — its own C0 control fixes the datum
  on the home build verbatim ("the combined primary
  point (CH-COMB, a = +0.10, κ₁ = 0.254873)
  reproduces Phase 226's seven minima with max abs
  diff ≤ 1e-9"), and its recorded t = 0 march-slice
  NEC_φ (+0.903081, CHECKPOINT229) is quoted there
  as a **march-slice** value — the X-configuration's
  value, on record before 477 traced it — never as
  the datum's vector. The march registration thus
  *distinguishes* the datum (home) from its own
  object (compensated march), exactly as the ruling
  holds.
- *P233-1 / P234-1* pose march-priced successors
  (κ moved off the premium point; the Gate-27 pose
  family adds CH-PHI-Auu at κ = 0.3) — different
  poses and march objects, not the P226-1 primary
  point.

**Ruling of the gate:** 478's identity ruling
**stands as a ruling**. The datum of record is the
home build's object; its Fuu is j_prof; **467's
rescue radius (133,522,009.61 m) stands UNQUALIFIED,
and entry 1236's build caveat is discharged** — now
gate-verified, not only phase-ruled.

## 4. (b) The shadow vectors — CONFIRMED at 0.0

On the gate's own assemblies and clause arithmetic
(checker: engine clause path, also 0.0):

**X(m)** — all seven strictly positive: NEC_ρ =
DEC_ρ = **+0.6781346234610093** (binding, at θ = π/2);
NEC_θ +1.4790316944454176; NEC_φ +0.9030810951057349;
WEC +1.3094045367416725; DEC_θ +1.1394910646834866;
DEC_φ +0.9030810951057349. Max abs diff vs the
charge: **0.0**.

**H(0)** — all seven strictly positive: NEC_ρ =
DEC_ρ = **+0.6781346234610093** (binding); NEC_θ
+1.479198706005177; NEC_φ +1.0541767526056953; WEC
+1.3094045367416725; DEC_θ +1.0279422865525754;
DEC_φ +1.0541767526056953. Max abs diff vs the
charge: **0.0**.

Both shadows are total-legal at jet scope on their
own terms, confirmed independently.

## 5. (c) The D-identity — RE-DERIVED on both paths

(i) *Expression level (the gate's own symbolic
differentiation of the stored expressions,*
`phase129/work/p1296_derive_raw.json` +
`phase254/work/p2542_riemann_jets.json`*):* the
carrying set is exactly {pth8, pph8, R_tltl} — every
other channel and tide component carries neither
Fuu nor Mtt (derivatives identically zero) — and for
each carrying read the gradient identity ∂g/∂Mtt +
e^{2(M−F)}·∂g/∂Fuu ≡ 0 holds at the five variants'
composed jets with worst relative residual
**2.21×10⁻¹⁶**. (ii) *Perturbation at each shadow's
composed jets:* D-preserving perturbations change
pth8/pph8/R_tltl by ≤ **2.22×10⁻¹⁶** at δ = −0.05
and +0.03; D-changing perturbations change them by
0.0409365377 / 0.0245619226 (O(δ)) — 478's values to
the digit. Every (Fuu, Mtt)-carrying read of both
shadows reads D := e^{−2M}·Fuu − e^{−2F}·Mtt alone,
gate-verified.

## 6. (d) Scale invariance — premise clean, computed
## invariance confirmed

Premise audit (the gate's own reading of the build
inputs, per shadow): march grids and steps, FD feed,
compensation replacement, CH-COMB amplitude,
director constants, engine constants — all
dimensionless; no physical length, mass or time
enters either construction; physicalisation only
through L = R/0.8; P226-2's semiclassical sector is
not a constituent of either shadow's total (the
boundary stands: a total carrying an intrinsic
length would not inherit the invariance). Computed
check, physical clause read from each shadow's
scaled channel arrays vs its own §4 vector,
normalised max rel diff: **X(m): 6.01×10⁻¹⁶ at its
rescue radius, 3.00×10⁻¹⁶ at 2.5×10⁸ m; H(0):
3.90×10⁻¹⁵ and 2.85×10⁻¹⁵** — 478's reads confirmed,
signs matching at both radii. Legality is
scale-invariant for both shadows as a computed fact.

## 7. (e) Rescue radii and E_shell — CONFIRMED by
## 467's method, with second paths

Tide worsts (gate sampler reads): both shadows'
radial worst sits at the pole — X(m)
|R_t̂l̂t̂l̂| = 0.9718746251967629 pose⁻² at θ = 0.02;
H(0) 0.9718745756442096 pose⁻² at θ = 0.02; lateral
combination worst at β = 0.1 = 0.9459504297033866
pose⁻² (both). The gate's **FD-Riemann second
path** agrees with the symbolic reads at θ ∈ {0.5,
1.0, π/2} on both shadows with worst rel diff
**7.51×10⁻⁵** (inside 467's checker class).

**Rescue radii (radial-bound, direct rungs):**
X(m) **106,756,986.38 m** (gate float64
106756986.37743658; 50-digit mpmath closed form
agrees at 0.0 m); H(0) **106,756,983.66 m** (gate
106756983.65585029; mpmath agrees at 1.5×10⁻⁸ m).
At each rescue radius the radial component is
1.0000× the SPEC-T1 bar, the lateral at β = 0.1 is
0.9733× bar, and the β ceiling is **0.194** (gate's
contiguous scan, both shadows).

**E_shell (467's method, A1 split quadrature, from
each shadow's own arrays):** X(m)
**1.6815079776×10⁵² J** at its rescue radius (gate
full value 1.6815079776212468×10⁵² J); H(0)
**1.6815079348×10⁵² J** (gate 1.6815079347540844×
10⁵² J). The director term's 50-digit mpmath
quadrature agrees with the gate's fine Simpson at
rel diff 1.5×10⁻¹⁵; E ∝ R verified per shadow (E/R
spread ≤ 2.5×10⁻¹⁶). **D-blindness cross-check:**
at R = 1.068×10⁸ m the datum H(ũ_true), X(m) and
H(0) shell energies coincide at
**1.6821854766022598×10⁵² J — pairwise diff 0.0**
(each from its own pre-director arrays; the charge's
printed 1.6821854766×10⁵² J confirmed). The toll is
priced by radius alone, gate-verified. E_shell
remains a posed-domain quantity (467 A1's
logarithmic-divergence fence).

## 8. Verdict application and the quotable claim set

Controls pass (§2); identity legs G1–G3 hold (§3);
vectors, D-identity, invariance and prices confirm
at their registered bars (§§4–7). The verdict is
**PASS WITH RIDER** — the rider (§9) restates no
figure or clause of the claim set; it corrects a
fence sentence in the phases' printed record, per
the Gate-59/Gate-60 practice for printed-record
corrections that touch no verdict. **Both shadows
stand as verified data of the P226-1 class**, quoted
only in this form:

> **G61-A (identity).** *The P226-1 combined datum
> of record is the home build's object
> (`instant_jets`, Fuu = j_prof, Mtt = the (A1)
> anchor ũ_true): P226-1's registration fixes that
> build verbatim, Phase 169's (A1) clause set is its
> base set, and Phase 167's compensated pose is a
> different posed Φ that no stored registration
> poses this datum in. Phase 467's tide verdict and
> rescue radius (133,522,009.61 m) stand
> unqualified; the build caveat of ledger entry
> 1236 is discharged.*
>
> **G61-B (shadow datum X(m)).** *The compensated
> transplant's third configuration (D = e^{−0.2}·j
> − (1 − e^{−0.2})·τ_m) is total-legal at jet scope
> on its own terms — all seven clauses strictly
> positive, binding NEC_ρ = DEC_ρ =
> +0.6781346234610093 — with rescue radius
> 106,756,986.38 m (radial-bound; lateral 0.9733×
> bar at β = 0.1; β ceiling 0.194) and E_shell =
> 1.6815079776×10⁵² J at that radius.*
>
> **G61-C (shadow datum H(0)).** *The tax-free pose
> (D = e^{−0.2}·j) is total-legal at jet scope on
> its own terms — all seven clauses strictly
> positive, binding NEC_ρ = DEC_ρ =
> +0.6781346234610093, NEC_φ = +1.0541767526056953
> the highest transverse margin of the three
> configurations — with rescue radius
> 106,756,983.66 m (radial-bound; same rung
> profile) and E_shell = 1.6815079348×10⁵² J at
> that radius.*
>
> **G61-D (structure).** *Every (Fuu, Mtt)-carrying
> read of these configurations reads the single
> combination D := e^{−2M}·Fuu − e^{−2F}·Mtt alone;
> E_shell is D-blind — datum and both shadows share
> 1.6821854766×10⁵² J at any common radius, so the
> toll is priced by radius alone; and each datum's
> legality is exactly scale-invariant, computed per
> rung.*

Riders G61-R1 (§9) binds every quotation of this
set. The wormhole line now holds **three verified
total-legal throat data at jet scope** (the P226-1
datum and the two shadows), each tide-priced; that
is the whole of the claim — construction (GAP-1 /
GAP-2 territory) and sustainment remain the line's
open problems, and **no traversability claim is
made**.

## 9. Rider and record disclosures

**G61-R1 (record correction; touches no verdict, no
figure of the claim set).** The fence sentence
carried in the Phase 467/477/478 memos and in
ledger entries 1236/1238 — that FU-P226-1 (the
combined march) is "unrun" / "still unrun" — is
**superseded**: the combined march ran as Phase 229
item P229-1 (2026-11-23) and failed at or before
Phase 214's t* (verdict form 2, FAILS AT OR BEFORE
t* ANYWAY; first NEC_φ crossing at refined
resolution in (0.48125, 0.4875]). The gate's G3
scan (§3) is what brought the march line's
registrations into this judgement. The correction
changes nothing in Gate-61's scope: the gate's
objects are t = 0 data, the march is a sustainment
read fenced off from every claim here, and P229-1's
C0 in fact reinforces legs G1/G3 (§3). Quotations
of the 467/477/478 memos' sustainment fences must
carry this correction.

**Incidents/amendments of this gate:** none. The
registration was executed as filed; the driver and
checker each ran once, clean. One methods note: the
gate's absence-scan set (1380 files, its own walk of
the phase*/gate* registration/checkpoint/run-record
population) is a superset of the shell enumeration
used in preparation (1372) — the both-marker
population is identical under both (20 files).

## 10. FENCES (on every number above)

Gate-27/28 wording discipline throughout: neither
the datum nor any shadow is the Gate-27 certified
pose; no certificate language. No traversability,
transit, gain or shortcut wording anywhere (C12).
The gate disturbed no stored read: every stored
vector was reproduced as a control, not re-judged;
Phase 254's own datum reads and Phase 229's march
reads stand as stored. Jet scope, t = 0, sector
superposition, exhibit ≠ construction — for the
shadows exactly as for the datum. Deciding values
at named points (θ named for every quoted
extremum), frame of record. Novelty NONE.

## Files

- `work/g61_registration.md` — registration
  (pre-run, unamended).
- `work/g61_run.py` — gate driver (controls gate
  the deciding reads; elapsed ≈ 69 s).
- `work/g61_check.py` — independent checker, 16/16.
- `results/g61_results.json`,
  `results/g61_verify.json`.
- `GATE61_REPORT.md` (this file),
  `CHECKPOINT61.md`.
- `bundle/gate61-claims/` — the publication bundle,
  assembled on this verdict and handed back; **the
  parent assigns the version at push time by
  landing order and pushes; the gate does not
  push.**
- No ledger append, no launch, nothing outside
  `gate61/` edited.
