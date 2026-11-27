# GATE-48 — Independent re-judgement of the Phase 400 claim set

Charged at ledger entry 1041 (2026-11-26). Phase 400 claimed
that the incumbent-centred static search at S ≡ 0 — Phase
398's incumbent re-searched with 341's roughness penalty
rescaled to the level's own scale (PEN400, LAM400 =
LAM_REG × 10⁻³) and the dip family widened — raised the
scaling ridge's static floor through zero to a confirmed
joint level of **+1.3977194851281464×10⁻⁶** (SET-244, band
[10, 20]), with S identically zero, Type-I fraction 1.0000,
the exact worst-null at the argmin identical to the joint,
an adversary-polished in-region depth of +1.376183×10⁻⁶,
and stakes, under Phase 397's fitted carried law, of a
break-even shift μ_S* = 0.271/0.282 — below the SS7 warp
criterion of 0.5. This gate re-judges that claim set with
fresh machinery only, every deciding value reproduced
independently on the VM frame of record.

## Verdict

- **(a) The winner's configuration and its joint level
  +1.397719×10⁻⁶: SURVIVES.** The gate's SET-244 read of
  the stored configuration (base (μ_N, μ_M) =
  (2.330448313835416, 11.343911464156438); K = 17 vN with
  knots 11–13 at (−0.04167124952425175,
  −0.07069986031752953, −0.058496328373661255); vM as
  stored) reproduces the joint at
  +1.3977194851287427×10⁻⁶ (diff +6.0×10⁻¹⁹), the NEC,
  DEC and WEC minima identical to the joint, the argmin
  on the stored shell r = 17.682926829268293. All five
  lineage controls reproduce at roundoff (§2).
- **(b) The static character and the polished depth:
  SURVIVES.** S ≡ 0 exactly on the gate's own assembly
  (max |S|, |S′|, |S′′| over the SET radii = 0.0 exactly;
  max |g_ti| over a full SET shell = 0.0 exactly);
  Type-I fraction 1.0000 (6642 of 6642); the exact
  worst-null at the argmin is identical to the gate's
  joint; ρ_min +9.943381×10⁻⁵ (diff +5.4×10⁻¹⁷). The
  gate's independent adversary polish re-derives the
  in-region depth at +1.3761826609×10⁻⁶ (diff
  +1.8×10⁻¹⁵ vs stored) — positive, not a grid artefact
  (§2).
- **(c) The search accounting: SURVIVES.** 981 stored
  screens (stages A 328, B 22, C 432, D 182, E 17 — the
  registered counts), zero rejected (a rejection would
  be stored with a `rejected` key; none of the 981
  carries one; the state file's n_evals = 981 with the
  cap unreached), the five stage bests as stored, the
  zero crossing inside Stage A, and the phase's quoted
  running incumbent at A-screen 200 reproduced to the
  quoted digits. The gate independently re-read the
  Stage A–D best configurations: all four joints
  reproduce at ≤ +6.5×10⁻¹⁹ (§3).
- **(d) The penalty arithmetic: SURVIVES.** LAM400 =
  LAM_REG × 10⁻³ holds exactly in float64
  (1.0×10⁻⁵ = 0.01 × 10⁻³, ratio 0.001); the incumbent
  dip's roughness is 0.0024, priced
  2.4000000000000004×10⁻⁵ under 341's penalty and
  2.4000000000000003×10⁻⁸ under PEN400 — the stored
  CTL-400-PEN values at diff 0.0. Stronger: every one of
  the 981 stored screens' `penalty` and `pen341` fields
  recomputes from that screen's own stored vectors at
  max diff 0.0 (§4).
- **(e) The fences and stakes: SURVIVE AS RIDERS**
  (issued as G48-E, attached on the face of G48-A and
  G48-B wherever their levels are quoted). The gate
  re-measures SEC at the winner at **−2.050292×10⁻⁴**
  (diff +1.8×10⁻¹⁸ vs stored; Type-I, frame-invariant):
  SEC remains violated at the winner, outside the
  lineage's NEC/DEC joint, and **no member and no EC
  pass is quotable** — the object is static. The stakes
  recompute on the gate's own confirmed margin:
  μ_S* = 0.271335 (Trace-A law) / 0.282108 (Trace-B),
  m_req = 5.219677×10⁻⁶ / 4.803209×10⁻⁶, shortfall
  3.821957×10⁻⁶ / 3.405489×10⁻⁶ — below the 0.5
  criterion under either law, with the
  fitted-on-uncorrected-bases caveat on the face (§5).

## §1 Machinery and calibrations

Fresh gate machinery (`gate48/work/g48_lib.py`), written
for this gate: **forward-mode second-order Taylor jets
of the metric in spherical coordinates (t, r, θ, φ)**,
with explicit index-loop Christoffel and Ricci
contractions in the spherical basis and the Eulerian
frame taken as the spherical orthonormal frame
(n, r̂, θ̂, φ̂) of the same metric. The organisation is
used by no earlier read: the lineage assembles
hand-derived radial formulas in Cartesian coordinates;
Gate-43 ran Cartesian analytic loops; Gate-45 ran AD
jets of the metric in **Cartesian** coordinates with
einsum contractions; Gate-46 formed **symbolic** sympy
expressions in spherical coordinates and lambdified
them; Gate-47 formed symbolic expressions in Cartesian
coordinates with cse. Here no symbolic expression is
ever formed — derivatives are numbers carried through
jet arithmetic — and the jets live in spherical
coordinates. Own profile assembly from the programme's
registered design definitions (base shapes, A2 totals
from Phase 344's stored K = 33 vectors, H2 totals =
centre(1.15) + Phase 379's stored K = 17 vectors,
per-profile scaling, not-a-knot correction splines with
constant extension); own Hawking–Ellis eigenvalue
margins; own worst-null (fib-642 scan + Nelder–Mead
polish); own adversary polish. No phase or earlier-gate
code is imported or reused for any deciding read. All
deciding reads ran on the VM; the laptop is not a gate
instrument. Stored bytes were md5-verified before use
(§7).

Calibrations (`gate48/results/g48_numbers.json`):

- **C-0** Stored vectors: the gate's A2 and H2
  correction vectors agree between the two stored
  artefacts each (confirmation JSON and state file) at
  max diff 0.0.
- **C-1** Trivial limit (S = 0, N = 1, M = 1):
  max |T| = 2.53×10⁻¹⁷ — the roundoff residue of the
  raw spherical assembly (coordinate Christoffels are
  nonzero in spherical coordinates and cancel in the
  Ricci contraction), disclosed as Gate-46 disclosed
  its 2.5×10⁻¹⁸.
- **C-2** Profile assembly: the gate's locals at the
  winner's binding site reproduce Phase 400's stored
  anatomy locals at diff 0.0 on all nine fields
  (S, S′, S′′, N, N′, N′′, M, M′, M′′).
- **C-3** A stored control reproduced through the full
  tensor machinery: the Trace-A endpoint SET read
  (§2) reproduces Phase 397's stored level at diff
  +3.7×10⁻¹⁹, with its worst-null at the same diff.
- **C-4** Pointwise tensor check: the gate's That
  eigenvalues at the winner's stored site point
  reproduce Phase 400's stored eigenvalues at max diff
  6.6×10⁻¹⁷, and the gate's point NEC and worst-null
  there are both +1.397719485128797×10⁻⁶.
- **C-10 (frame-convention discipline, applied as in
  Gates 43–47).** Deciding values are taken at named
  points or from frame-invariant statistics
  (eigenvalue margins at Type-I points, Eulerian ρ,
  Type-I counts, exact worst-nulls). At the winner,
  the endpoints and the anchor every SET point is
  Type-I, so their full-set minima are frame-invariant
  and are compared directly. For the shift-carrying
  controls (H2, C395), whose stored batch NEC minima
  sit at non-Type-I points, the gate compares only
  frame-invariant fields (ρ_min, Type-I count, the
  DEC minimum whose argmin is Type-I, and exact
  worst-nulls at the stored named argmin points); the
  raw sampled batch minima are not deciding values
  and are not re-issued.

## §2 Claims (a) and (b) — the winner, its controls, its pointwise grade, its polish

**The winner.** Gate SET-244 read of the stored
configuration: joint (min of the NEC and DEC eigenvalue
margins) **+1.3977194851287427×10⁻⁶**, diff +6.0×10⁻¹⁹
vs stored; NEC min = DEC min = WEC min = the joint;
argmin shell r = 17.682926829268293 (the stored radius;
at S ≡ 0 the object is spherically symmetric, so the
argmin direction is the whole shell — the gate's
argmin direction differs from the phase's, the shell
and the value are the claim); Type-I count 6642 of
6642; ρ_min +9.943380734115006×10⁻⁵ (diff +5.4×10⁻¹⁷).
The exact worst-null at the gate's argmin point is
+1.3977194851287427×10⁻⁶ — identical to the gate's
joint, as stored. **Ruling (a): SURVIVES**, with
rider G48-E.

**Controls (all through the gate's machinery):**

| control | stored joint | gate joint | diff | worst-null diff |
|---|---|---|---|
| Trace-A endpoint (397) | −6.587071568730905×10⁻⁷ | −6.587071568727246×10⁻⁷ | +3.7×10⁻¹⁹ | +3.7×10⁻¹⁹ |
| Trace-B endpoint (397) | −7.229718758606569×10⁻⁷ | −7.229718758603858×10⁻⁷ | +2.7×10⁻¹⁹ | +2.7×10⁻¹⁹ |
| 398 anchor | −2.5991706000781927×10⁻⁷ | −2.5991706000760243×10⁻⁷ | +2.2×10⁻¹⁹ | +2.2×10⁻¹⁹ |
| L_stat(H2), (1,1,1) | ρ_min 8.789653555683182×10⁻⁵ | ρ_min diff +9.5×10⁻²⁰ | — | at the stored argmin point: −1.9432881962794750×10⁻⁴ vs Gate-46's independent −1.9432881962794723×10⁻⁴, diff −2.7×10⁻¹⁹ |
| C395 | ρ_min 9.780857711542179×10⁻⁵; DEC −1.7766846142506707×10⁻⁶; Type-I 4067 | ρ diff −6.9×10⁻¹⁸; DEC diff −1.1×10⁻¹⁹ (argmin Type-I, r = 18.65853658536585); Type-I count 4067 exact | — | at the stored argmin point (−15.383488301698574, 2.2228398846289754, −2.4277326106594397): −3.089621009567839×10⁻⁵ vs stored −3.0896210095678075×10⁻⁵, diff −3.1×10⁻¹⁹ |

(The H2 and C395 batch NEC minima sit at non-Type-I
points and are C-10-band quantities; per §1 they are
not deciding values and the gate does not re-issue
them. Every frame-invariant field of both controls
reproduces at roundoff.)

**Static character.** On the gate's own assembly of
the winner: max |S|, |S′|, |S′′| over the SET radii =
0.0 exactly, and max |g_ti| over a full SET shell =
0.0 exactly — the shift is absent, not cancelled.
Type-I fraction 1.0000. **Ruling (b), static leg:
SURVIVES.**

**Adversary polish (the not-a-grid-artefact leg).**
The gate re-ran the polish protocol on its own SET
read (starts = the five lowest Type-I SET points —
all on the argmin shell, by symmetry; Nelder–Mead over
(r, θ, φ) at the stored tolerances): polished depth
**+1.3761826609474655×10⁻⁶** at r = 17.774281481893205,
diff +1.8×10⁻¹⁵ vs stored +1.3761826591108812×10⁻⁶.
A tighter second polish (xatol 1e-9, fatol 1e-13)
finds +1.3761826576426817×10⁻⁶ at
r = 17.774246447910805 — the stored protocol depth is
the converged value at its tolerances, and the true
in-region floor is the same number to 3×10⁻¹⁵. A fine
radial bracket (r = 17.30…18.10 by 0.025, two
directions) bottoms at +1.376184184408673×10⁻⁶ at
r = 17.775 with a direction difference of 5.4×10⁻²⁰ —
the margin is a function of r alone, as a static
object requires. The depth is positive by every path:
**the level is not a grid artefact. Ruling (b):
SURVIVES.**

## §3 Claim (c) — the search accounting

Recount of the stored record
(`gate48/results/g48_recount.json`): **981 screens**,
stage counts A 328, B 22, C 432, D 182, E 17 — the
registered counts exactly; the state file records
n_evals = 981, cap_reached = false, incumbent =
the E-stage winner at +1.3977194851281464×10⁻⁶.
**Zero rejected**: in the search's own record format
a floor-rejected screen is stored with a `rejected`
key and no read fields; none of the 981 records
carries the key, and every record carries a full
feasible read (vectors, margins, both penalty
fields). Stage bests as stored: A
+1.2307650495664633×10⁻⁶ (A_K9_nm), B
+1.1236913755491599×10⁻⁷ (B_dip6_-0.05), C
+1.3086792649733925×10⁻⁶ (C_K17_nm), D
+1.3115398051287528×10⁻⁶ (D_cd_cd), E the winner.
The gate re-read the Stage A–D best configurations
through its own machinery: joints reproduce at diffs
+5.1×10⁻¹⁹ (A), +1.1×10⁻¹⁹ (B), +6.0×10⁻¹⁹ (C),
+6.5×10⁻¹⁹ (D). **The zero crossing is inside Stage
A**: the first positive pure-joint screen of the
record is A-index 15 (tag A_K9_s0.02_cd,
+1.5792476403001996×10⁻⁷, a trial of the first
coordinate-descent sweep), and the running pure-joint
incumbent at A-screen 200 is +9.219392729314463×10⁻⁷
— the phase's quoted +9.219393×10⁻⁷ to its quoted
digits. **Ruling (c): SURVIVES.**

## §4 Claim (d) — the penalty arithmetic

The gate recomputed the roughness (sum of squared
second differences) and both pricings from the
vectors themselves. LAM_REG = 0.01 (Phase 338's
registered coefficient); LAM400 = 1.0×10⁻⁵;
**LAM400 = LAM_REG × 10⁻³ holds exactly** (the
float64 equality 1.0×10⁻⁵ == 0.01 × 10⁻³ is true;
the ratio is 0.001). The incumbent dip (K = 9,
knot 6 at −0.02, all else zero) has roughness
0.0024000000000000002; priced under 341's penalty at
2.4000000000000004×10⁻⁵ and under PEN400 at
2.4000000000000003×10⁻⁸ — both identical to the
stored CTL-400-PEN values at diff 0.0. The audit
extends to the whole record: for **all 981 stored
screens**, the stored `penalty` field equals
LAM400 × (rough(vN) + rough(vM)) recomputed from
that screen's own vectors at max diff **0.0**, and
the stored `pen341` field equals LAM_REG × the same
roughness at max diff **0.0**. The mechanism of the
crossing — the dip priced at 0.092 × |L_anchor|
under PEN400 against 92 × |L_anchor| under 341's
pricing — is arithmetically exact. **Ruling (d):
SURVIVES.**

## §5 Claim (e) — the fences and the stakes, as riders

**SEC at the winner, re-measured by the gate:**
−2.050291598674923×10⁻⁴ (stored
−2.0502915986749415×10⁻⁴; diff +1.8×10⁻¹⁸), a
Type-I eigenvalue margin, frame-invariant. SEC is
not part of the lineage's joint min(NEC, DEC) at any
point of this line, and it remains violated at the
winner by ~2.05×10⁻⁴. The winner's positive joint is
therefore a statement about NEC and DEC (with WEC)
at a static configuration — **no EC pass and no
member is quotable**, and the object, being static
(S ≡ 0, warpless), carries no drive content whatever
its level.

**Stakes, recomputed on the gate's margin.** With
m = the gate's confirmed joint
+1.3977194851287427×10⁻⁶ in Phase 397's carried law
|L(μ_S) − L_static| = A_c·μ_S^p (Trace-A:
A_c = 2.3255901039892218×10⁻⁵, p = 2.15556441798475;
Trace-B: A_c = 2.1420515201850943×10⁻⁵,
p = 2.1569227773790267): μ_S* = (m/A_c)^(1/p) =
**0.271335** (A) / **0.282108** (B) — the stored
0.27133544952741057 / 0.28210849536188903 reproduced
to 5×10⁻¹⁴ (the residue is the gate margin's own
6×10⁻¹⁹ diff, amplified by the 1/p power). The
margin a warp-grade re-introduction would require,
m_req = A_c·0.5^p, is 5.219676929899912×10⁻⁶ (A) /
4.803208707352303×10⁻⁶ (B); the shortfall is
3.821957×10⁻⁶ (A) / 3.405489×10⁻⁶ (B). Both
break-evens are **below the SS7 criterion
μ_S* ≥ 0.5**. The caveat stands on the face: the
carried law was fitted along the ridge on the
endpoints' **uncorrected** bases; on this corrected
base the coefficient may differ, so these
break-evens are the law's estimates, not
measurements — the direct measurement is Phase
404's re-introduction read, charged separately.
**Ruling (e): SURVIVES as rider G48-E.**

## §6 The quotable set (G48-*), with the fence

**FENCE (verbatim, travels with every quotation):**
band pose [10, 20] only; Phase 356's full-extent
caveats travel with every level in this set; the
object is static (S ≡ 0); SEC's measured status is
on the face of the set (G48-E); no EC pass, no
member, no drive implication.

- **G48-A (the confirmed static level).** The static
  configuration on H2's total profiles with base
  scalings (μ_N, μ_M) = (2.330448313835416,
  11.343911464156438), a K = 17 N-correction spline
  whose dip sits at knots 11–13
  (−0.04167124952425175, −0.07069986031752953,
  −0.058496328373661255; full vectors in Phase 400's
  confirmation record) and the stored near-zero
  K = 17 M-correction, S identically zero, has
  stationary joint level (SET-244, SAMPLER-M, band
  [10, 20]) **+1.397719×10⁻⁶** (NEC = DEC = WEC =
  +1.3977194851281464×10⁻⁶ at r = 17.682926829268293;
  ρ min +9.943381×10⁻⁵; Type-I fraction 1.0000) —
  above Phase 398's static floor
  (−2.599171×10⁻⁷) by +1.657637×10⁻⁶ and above
  Phase 397's Trace-A endpoint (−6.587072×10⁻⁷) by
  +2.056427×10⁻⁶. **G48-E is part of this claim
  wherever its level is quoted.**
- **G48-B (pointwise grade and static character).**
  The exact worst-null at G48-A's argmin is
  +1.397719×10⁻⁶, identical to the joint; S, S′ and
  S′′ are identically zero on the configuration's
  own assembly; and the adversary-polished
  in-region depth is +1.376183×10⁻⁶ — the level is
  not a grid artefact. **G48-E is part of this
  claim wherever its level is quoted.**
- **G48-C (the search accounting).** The level was
  reached by 981 stored screens in five stages
  (A 328, B 22, C 432, D 182, E 17), zero rejected,
  with stage bests −2.599171×10⁻⁷ (anchor) →
  +1.230765×10⁻⁶ (A) → +1.123691×10⁻⁷ (B, the
  single-dip family alone) → +1.308679×10⁻⁶ (C) →
  +1.311540×10⁻⁶ (D) → +1.397719×10⁻⁶ (E); the
  zero crossing lies inside Stage A's walks.
- **G48-D (the penalty mechanism).** The rescaled
  penalty PEN400 has LAM400 = LAM_REG × 10⁻³
  exactly (LAM400 = 1.0×10⁻⁵, LAM_REG = 0.01); the
  incumbent's one-knot dip that Phase 398's
  penalised walks could not accept is priced
  2.4×10⁻⁸ under PEN400 against 2.400000×10⁻⁵
  under 341's penalty — the crossing was inside
  the earlier search's reach, priced out by the
  penalty's scale.
- **G48-E (the fence rider — part of G48-A and
  G48-B wherever their levels are quoted).** No
  member and no EC pass is claimed or implied:
  the configuration is static (S ≡ 0, warpless)
  and has no drive content; the quoted level is
  the lineage's joint min(NEC, DEC), and **SEC,
  outside that joint, is measured at the winner
  at −2.050292×10⁻⁴** (Gate-48's re-measurement),
  so the full set of energy conditions does not
  hold at this configuration. Under Phase 397's
  carried law — fitted on the endpoints'
  uncorrected bases, an estimate and not a
  measurement — the static margin
  +1.397719×10⁻⁶ would buy back the shift only
  to a break-even μ_S* = 0.271 (Trace-A law) /
  0.282 (Trace-B), below the SS7 warp criterion
  of 0.5, with a shortfall to the required margin
  of 3.822×10⁻⁶ / 3.405×10⁻⁶; the direct
  measurement of the break-even on this corrected
  base is Phase 404's charged read, whose result
  supersedes these fitted figures when it lands.

## §7 Provenance and artefacts

Machinery: `gate48/work/g48_lib.py` (jets, profile
assembly, tensor, frame, margins, worst-null, reads),
`gate48/work/g48_run.py` (calibrations and deciding
reads), `gate48/work/g48_polish.py` (adversary polish
re-derivation), `gate48/work/g48_recount.py` (search
recount, stage-best re-reads, penalty audit, stakes).
Records: `gate48/results/g48_numbers.json`,
`gate48/results/g48_polish.json`,
`gate48/results/g48_recount.json`.

Stored bytes consumed, md5-verified before use:
phase400/results/p400_confirmation.json
7a7792e3941380d23d38e959f0cd0b6f; p400_anatomy.json
b1b87b4d3513d30df87735f40caaf060; p400_stakes.json
f9fc9ebec2d8e687f6d1b39515d78cd4; p400_controls.json
02fb49deecfe9e76173493df2f066e20; p400_screens.jsonl
dd5234f0cc34d1cc01faf7bf55bfb363; p400_state.json
5a3ff364051faf91742972c534efc663;
phase398/results/p398_confirmation.json
b08efbc6c8ced50f2a1705870be799c2;
phase344/results/p344_confirmation.json
bca93c039daf9c8baf68f4e567abe873;
phase379/results/p379_confirmation.json
1bcb8b3900026cc78e6aacb33654ad72;
phase395/results/p395_confirmation.json
6d3e2c209ffbcd36ff2f59bdee09a0bb. (The named
control points for H2 and C395 were taken from
gate46/results/g46_shellpoints.json — stored
artefact data, not machinery.)

Process incidents, disclosed: (i) the gate's first
polish run terminated on a singular spherical
metric when a Nelder–Mead step reached a coordinate
pole (θ → 0, a chart singularity, not a property of
the configuration); a pole guard (θ kept within
[0.05, π − 0.05], returning the protocol's
out-of-region value) was added and the polish
re-run in full — no read was lost or reused from
the failed run. (ii) The first full run of
g48_run.py completed all reads but failed at the
final JSON serialisation (raw That arrays in the
record); the arrays were converted to eigenvalue
lists and the run repeated in full — all deciding
values in this record are from the completed run.
No other incident; no read depends on the laptop.

DESK: NO DATA CONTACT.
