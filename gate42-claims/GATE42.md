# GATE-42 — INDEPENDENT RE-JUDGEMENT OF THE PHASE 386 CLAIM SET

**Charge:** ledger entry 988 (FU-P386-2). **Subject:** Phase 386 — the
graded shell for the subluminal record (wild-queue W5): the claim that a
continuously graded density, in Procaccia's (10,20) configuration class,
opens a new category with best β = 0.18671875.
**Gate machinery:** FRESH — the gate's own graded builder, summary,
legality, q-read and exact-min-null code (`gate42/work/g42_lib.py`),
written from the construction registered in CHECKPOINT386 §SS2 and the
shared class definitions; tensor instruments are the registered pair
(`gate6/wa_auditor.py`, 2nd-order FD; `phase50/p503_lib.audit4`,
4th-order second path). Nothing was imported from `phase386/work` or
from any Phase 386 driver. All gate reads on the VM frame of record
(Phase 166 pin: programme venv, numpy 2.5.5 / scipy 1.18.1); the laptop
is not a gate instrument (standing lineage pattern — no laptop read was
used for any deciding value). **Date:** 2026-11-26.

## Verdict summary

| Claim | Ruling |
|---|---|
| (a) Construction and step-profile limit (c = 0 is Procaccia's design; legal at 0.1363, ratio 1.000 to Gate-7; failing at 0.1364) | **SURVIVES** |
| (b) The category fence (graded class genuinely distinct from Gate-7's step-profile class; 386's wording never crosses) | **SURVIVES** — fence ruled sound, wording compliant |
| (c) Deciding reads (S1 and Rank-1 legal at β = 0.18671875 under the common bars; brackets 0.19171875 / 0.1875) | **SURVIVES** |
| (d) Artefact history (Stage-1 champion convicted and excluded; amended screening set + recalibration sound) | **SURVIVES** |
| (e) Dose–response ladder (0.1515625 → 0.16640625 → 0.18671875 vs step 0.1363) | **SURVIVES** |

The quotable set is §5 (G42-A…G42-E). Two diagnostic-convention notes
(sampled-NEC and q direction sets, §1 C-6) and the coarse-stencil
disclosure at the one marginal cross-check point (§1 C-5) are carried
on the record; neither touches a deciding value.

## §1 Machinery and calibrations

**C-1 · Stored bytes (hash gate).** All three stored copies of
Procaccia's design vector hash to the published figshare SHA-256
`a8814dfb…d74a` — PASS. The claim subjects' parameter vectors hash to
their recorded values: S1 `84c9043e…2068`, S2 `29af1376…27cf`,
S3 `87df3cfe…996`; Rank-1 `d1efd424…5418` (Rank-1's vector taken from
the harvest file's first candidate, provenance "stage2x GPU DE pop
member", and confirmed by its hash). The Stage-1 champion's hash
`2c14cbca…dbed` matches **none** of the claim subjects (§4).

**C-2 · The gate builder reproduces the construction.** The gate's
graded builder implements the registered construction (φ = exp(ΣcⱼBⱼ)
on the 8-spline grading basis over [R₁, R₂]; ρ = ρ₀·Box4_W[φ·1_[R₁,R₂]]
by four successive centred sliding box averages of width W on a
construction grid of 1,200,671 points — the gate's grid count matches
the phase's stored count exactly; stage 1 exact via the spline
antiderivative of φ, stages 2–4 via cumulative-trapezoid
antiderivatives with cubic Hermite evaluation at shifted points;
ρ₀ by the class mass convention on the builder grid; background and
source chain by the GenProcaccia conventions). At c = 0 its chain
reads reproduce the phase builder's stored graded reads at **float64
roundoff** (relative differences ≤ 1.4×10⁻¹⁵ on M, ρ_max, λ, k,
∫F/r², a(R_in), M_unscaled) and the step builder's stored reads at
ρ_max 3.99×10⁻¹², λ 2.07×10⁻¹¹, k 8.70×10⁻¹² — the phase's own C-G1
figures (3.99×10⁻¹² / 2.07×10⁻¹¹ / 8.70×10⁻¹²) reproduced. Against the
paper's §3 enclosures the gate reads sit ≤ 2.7×10⁻⁸ (print precision).
Profile agreement with the closed-form step density: max abs diff
5.41×10⁻¹² of ρ_max; max rel diff 6.33×10⁻¹⁰ where ρ ≥ 10⁻³ of peak.
A second, independent stage scheme (spline antiderivatives) lands
≤ 1.0×10⁻¹⁰ on the same reads — the construction is scheme-stable.
For the claim subjects the gate's chain reads reproduce the stored
ones (S1: ρ_max 3.161981×10⁻⁴, λ 0.653726, k 0.028582, a(R_in)
−0.677345, φ ∈ [0.1235, 4.4706]; S2, S3 likewise; Rank-1's chain,
unstored by the phase, reads ρ_max 3.174150×10⁻⁴, λ 0.643105 on gate
machinery). Every subject's chain mass is M_target exactly.

**C-3 · Minkowski anchor.** max |That| = 0.0 exactly.

**C-4 · β = 0 static anchor.** Auditor vs the exact spherical read
(ρ, 0, rρa′/2) of the gate builder's own profiles at eight radii:
ρ rel err ≤ 1.18×10⁻³, p abs err ≤ 3.8×10⁻⁹ at h = 0.0375, both
improving at h = 0.01875 — the Gate-6 anchor scale, matching the
phase's C-G4 rows.

**C-5 · The C-G3 cross-check point, with its disclosure.** At the
Gate-7 stored point (0, 16.635, 0) on the c = 0 member, gate exact
min-null (SLSQP and the Lagrange secular solve agree to ~10⁻¹⁵ on
every row):

| β | instrument | h = 0.0375 | h = 0.01875 | h = 0.009375 |
|---|---|---|---|---|
| 0.1364 | wa | **+7.4645×10⁻⁸, Type-I** | −8.1794×10⁻⁸ | −1.1821×10⁻⁷ |
| 0.1364 | audit4 | −2.0027×10⁻⁷ | −1.3394×10⁻⁷ | −1.3035×10⁻⁷ |
| 0.1363 | wa | +2.5651×10⁻⁷ | +1.0020×10⁻⁷ | +6.3809×10⁻⁸ |
| 0.1363 | audit4 | −1.8183×10⁻⁸ | +4.8094×10⁻⁸ | +5.1680×10⁻⁸ |

The phase's disclosed coarse-stencil flip reproduces **exactly**: at
β = 0.1364 the single coarsest 2nd-order read at this one marginal
point is Type-I with min-null +7.4645×10⁻⁸ (phase: +7.464453×10⁻⁸),
while every finer and every 4th-order read is negative, the finest
4th-order value −1.3035×10⁻⁷ sitting 0.17% from Procaccia's stored
−1.30135×10⁻⁷. The gate adds the symmetric observation: at
β = 0.1363 the coarsest 4th-order read at the same point is likewise
marginally negative (−1.82×10⁻⁸) while its finer reads are positive
(+4.81×10⁻⁸, +5.17×10⁻⁸ — the latter matching Gate-7's stored
+5.3×10⁻⁸). The point's tensor sits at the FD floor (~5×10⁻⁸) at
either β; coarse stencils of either instrument can flip it. The
verdict-set audits (§2, §3) decide, and they are unambiguous at both
registered spacings on both instruments. The flip is an FD-floor
artefact, disclosed here and carried in G42-A's fence.

**C-6 · Diagnostic conventions (disclosed, non-deciding).** Two
direction-sampled diagnostics differ from the phase's stored values
by sampling convention only: the shell sampled-NEC minima (gate:
S1 +1.784×10⁻⁷, Rank-1 +2.369×10⁻⁷; phase: +1.671×10⁻⁷, +2.790×10⁻⁷)
and S1's q_max (gate 0.9945, phase 0.9974; same site r = 16.4). At
the flat-valley fringe point that sets S1's sampled minimum
(r = 23.0), three different 162-direction samplings of the gate's
tensor give 1.72 / 1.78 / 2.16×10⁻⁷, a dense sampling 1.226×10⁻⁷,
and the exact min-null +1.218×10⁻⁷ — the phase's value sits inside
the sampling spread of the same tensor. Every eigenvalue margin —
the deciding quantities — agrees with the stored reads to ~10⁻¹³.
All bars that involve these diagnostics (sampled-NEC > 0, q_max < 1)
pass under every sampling.

## §2 Claim (a) — construction and step-profile limit: SURVIVES

The construction is the registered one (C-2: an independent
implementation lands on the phase builder's stored reads at roundoff
and on the step builder's at the phase's own C-G1 digits). The c = 0
member **is** Procaccia's design. Through the gate's graded factory
at β = 0.1363 it is **fully legal under the common bars**: worst
margin SEC **+3.404178×10⁻⁷ at r = 5.0** (h = 0.0375; phase stored
+3.404178×10⁻⁷), **109.5× the FD floor**, Type-I fraction 1.000 over
988 significant points, sampled-NEC min +8.585×10⁻⁸, second path
(audit4) worst +3.396×10⁻⁷ with sign agreement on every deciding
margin; h = 0.01875 concurs (+3.397875×10⁻⁷). The ratio to Gate-7's
stored read (+3.404×10⁻⁷, same site, same floor multiple) is
**1.000**. At β = 0.1364 the member fails on the fine and
second-path reads (C-5). Claim (a) survives as stated, with the
C-5 disclosure carried in the quotable fence.

## §3 Claim (c) — the deciding reads: SURVIVES

Gate audits on `pts_1020_control` (1,430 points), both spacings,
both instruments; legality = the registered common bars.

**S1** (GPU-DE best, hash `84c9043e…`) at **β = 0.18671875: FULLY
LEGAL.** h = 0.0375: worst SEC **+3.971325×10⁻⁷ at r = 3.75**,
**123.0× the FD floor**, Type-I 1.000 (1,066 significant), NEC/WEC/
DEC minima +4.724565×10⁻⁷, shell sampled-NEC min +1.784×10⁻⁷,
audit4 worst +3.967×10⁻⁷, q_max 0.9945 at r = 16.4 < 1.
h = 0.01875 concurs (+3.968024×10⁻⁷, 129.3× floor). Every value
reproduces the phase's stored audit (worst +3.971325×10⁻⁷, 123×
floor). At **β = 0.19171875 it fails**: SEC −2.673018×10⁻⁵ at
r = 9.75, Type-I 0.9559, both spacings, second path concurring —
the stored bracket reproduced.

**Rank-1** (DE population member, hash `d1efd424…` — a second,
distinct subject: max |Δy|∞ = 0.474 from S1) at **β = 0.18671875:
FULLY LEGAL.** h = 0.0375: worst SEC **+2.252869×10⁻⁷ at r = 7.0**,
**64.9× the FD floor**, Type-I 1.000, NEC/WEC/DEC +4.907537×10⁻⁷,
audit4 worst +2.037367×10⁻⁷, q_max 0.9956 at r = 21.0 < 1;
h = 0.01875 concurs (+2.091261×10⁻⁷). Stored values reproduced to
the digits shown. At **β = 0.1875 it fails**: SEC −3.630506×10⁻⁶ at
r = 9.75, Type-I 0.9981 — the tighter stored bracket reproduced.

The graded-class best β = 0.18671875 is therefore held by **two
distinct subjects**, each legal at the rung and failing at its
bracket, on fresh gate machinery.

## §4 Claims (d) and (e) — artefact history and the ladder

**(d) SURVIVES.** (i) *Conviction reproduced at verdict grade:* the
Stage-1 champion (y_stage1, hash `2c14cbca…`) is **illegal at
β = 0.1363** on gate machinery — worst SEC **−7.042941×10⁻⁶ at
r = 7.0**, Type-I fraction **0.9644**, both spacings, audit4
concurring (−7.097×10⁻⁶) — and illegal at the ladder's top rung
0.17422 (SEC −6.342114×10⁻⁵ at r = 9.0, Type-I 0.8912), matching
the phase's home re-judgement values. All binding sites sit at
r ≤ 9.0, below the old core mask's 9.25 floor: the mask blindness
is the artefact mechanism, confirmed geometrically. (ii)
*Exclusion verified:* the claim set's audited subjects are exactly
{S1, S2, S3} plus the separately filed Rank-1; the champion's hash
matches none of them (C-1). (iii) *Amendment and recalibration
sound:* on the gate's own FD screening instrument (the Phase-73
two-number score, wa_auditor at h = 0.0375, repaired radii × 26
directions — 98 radii, 2,470 points inside the extended mask,
matching the phase's stored set size exactly), β_crit(y_his) =
**0.136328125**, bracket [0.1359375, 0.13671875], under **both**
masks — the c = 0 read is mask-independent — while the champion
reads **0.174609375** under the old mask [9.25, 27.27] and
collapses to **0.120703125**, bracket [0.1203125, 0.12109375],
under the extended mask [R_in − 0.5, R_out] — every figure
identical to the phase's stored recalibration; at β = 0.1363 the
extended-set score is −7.043×10⁻⁶ with binding site SEC at
r = 7.0, inside the extended mask and outside the old one. A
denser gate radius variant (209 radii) returns the same four
β_crit values, so the soundness does not depend on set density.

**(e) SURVIVES.** Each ladder rung was re-audited at home grade on
gate machinery: grading alone (S3, extended set) **legal at
0.1515625** (worst DEC +4.649873×10⁻⁷, Type-I 1.000; fails at
0.1565625, SEC −1.337570×10⁻⁵); joint Powell (S2) **legal at
0.16640625** (worst SEC +1.650946×10⁻⁷; fails at 0.17140625,
−1.124156×10⁻⁵); joint DE (S1, Rank-1) **legal at 0.18671875**
(§3); against the step member's 0.1363 (§2). The dose–response
0.1363 → 0.1515625 → 0.16640625 → 0.18671875 is reproduced rung by
rung, with the binding clause changing along it (switch flux
overload at the step ceiling; inner-ramp SEC in the graded class —
q_max stays < 1 at every legal rung).

## §5 Quotable claim set

> **G42-A (construction and step limit).** The continuously graded
> family of Phase 386 is constructed as registered: ρ = ρ₀ ·
> Box4_W[exp(Σⱼ cⱼBⱼ) · 1_[R₁,R₂]] in Procaccia's (10,20)
> configuration class (R₁ = 10.0000162, R₂ = 19.9997787,
> W = 3.6328174, M = 6.11288573784887775, p_r ≡ 0 background rule,
> source-derived shift), ρ₀ fixed by the class mass convention.
> Its c = 0 member is Procaccia's step-profile design: an
> independent re-implementation reproduces the graded builder's
> stored chain reads at float64 roundoff and the step builder's at
> ρ_max 4.0×10⁻¹², λ 2.1×10⁻¹¹, k 8.7×10⁻¹² relative. The c = 0
> member is fully legal at β = 0.1363 under the common bars (worst
> margin SEC +3.404×10⁻⁷ at r = 5.0, 109.5× the FD floor, Type-I
> fraction 1.000, second path agreeing; ratio 1.000 to Gate-7's
> stored read) and fails at β = 0.1364 on the fine and second-path
> reads (exact min-null −1.30×10⁻⁷ at the (0, 16.635, 0)
> cross-check point on the finest 4th-order read; the single
> coarsest 2nd-order stencil at that one FD-floor point reads
> +7.46×10⁻⁸ and is disclosed as an artefact of the stencil, not
> of the design).
>
> **G42-B (graded-class best, with its fence).** In the
> continuously graded-density category of that configuration
> class, the best verified speed is β = 0.18671875, held by two
> distinct configurations (S1, vector hash 84c9043e…; Rank-1,
> vector hash d1efd424…), each fully legal at β = 0.18671875
> under the common bars on independent gate machinery (S1: worst
> SEC +3.971×10⁻⁷ at r = 3.75, 123× the FD floor; Rank-1: worst
> SEC +2.253×10⁻⁷ at r = 7.0, 65× the FD floor; Type-I fraction
> 1.000 and second-path sign agreement for both), with failure
> brackets β = 0.19171875 (S1) and β = 0.1875 (Rank-1). **FENCE:
> this is a new category. The graded-class best does NOT contest
> Procaccia's β = 0.1363 in the step-profile category; the
> programme's verified best in the step-profile category remains
> β = 0.10 (Gate-7); the β = 0.12 conversion in that category
> (Kaggle p1423, spec FINAL per Phase 251) remains owed.**
>
> **G42-C (dose–response).** Within the graded category the gain
> over the step member decomposes as: step member 0.1363 →
> grading alone 0.1515625 → joint Powell polish over
> (c, a, q, r_m) 0.16640625 → joint differential evolution
> 0.18671875, each rung verified legal at the stated β and
> failing at its stated bracket on gate machinery.
>
> **G42-D (artefact).** Phase 386's first Stage-1 screening
> champion (screening β_crit 0.17461 under the original core
> mask) is an artefact of mask blindness at the inner ramp:
> independently convicted as illegal at β = 0.1363 (worst SEC
> −7.043×10⁻⁶ at r = 7.0, Type-I fraction 0.964) and at every
> audited rung up to 0.17422, and excluded from the claim set.
> The amended screening set (repaired radii × 26 directions over
> [R_in − 0.5, R_out]) convicts it at β_crit = 0.120703125 while
> leaving the c = 0 member at β_crit = 0.136328125 under both
> masks, reproduced on the gate's own screening instrument with
> the stored brackets.
>
> **G42-E (the category fence, standing form).** The step-profile
> category (Gate-7) fixes the shell density to the flat step
> member; the graded category frees the plateau profile within
> the same geometry, mass, background rule and source chain, and
> contains the step member as its c = 0 point. Speeds are
> comparable only within a stated category: no wording may carry
> a graded-category speed into the step-profile category or vice
> versa. Scope (C12 accounting, as in the phase record):
> prescribed-geometry audits throughout; the required source is
> the Einstein tensor of the prescribed metric, conservation
> automatic; no matter model, formation route or stability is
> claimed for any row.

**Ruling on the fence (claim b), recorded:** the distinction is
definitional and real. Gate-7's category is fixed in its own claim
text by the step density ("step density, box-4 smoothed"); the
graded family relaxes exactly that one defining restriction while
holding every other element of the class fixed — verified
numerically, not just verbally (identical R₁, R₂, W, M and source
chain; the step design is the family's c = 0 member, §2). The
classes are nested design spaces, and the binding mechanism
changes between them (switch flux overload → inner-ramp SEC), so
the distinction is mechanical, not cosmetic. The phase's wording
was audited in full (CHECKPOINT386 verdict forms, the memo's
quotable wording and goal accounting, ledger entry 987): the fence
is carried on the verdict's face in every instance and **no
cross-category sentence was found**. The fence SURVIVES as drawn;
G42-E states it in standing form.

## §6 Provenance, goal accounting, artefacts

- **Frame:** VM frame of record only. The laptop was not used and
  is not admitted as a gate instrument (standing pattern of this
  lineage: laptop reads of these set statistics differ at ~10⁻⁷–
  10⁻⁶ and have never been admitted; no deciding value here rests
  on anything but the VM reads above).
- **Goal 1 (FTL drive):** no bearing — no drive read was charged
  or run; no joint pass exists anywhere; nothing in this set
  changes that. **Goal 2 (wormhole):** no bearing — the Gate-23 /
  G27-A set stands untouched. **Goal 3 (subluminal record):** this
  gate's subject — a new, separately fenced category is verified
  (G42-B); the step-profile standings are unchanged (Procaccia
  0.1363 standing; programme verified best 0.10; p1423 owed).
- **DESK: NO DATA CONTACT** — all objects are from the programme's
  own record; no real-world dataset was consulted.
- **Artefacts:** `gate42/work/g42_lib.py` (gate machinery),
  `g42_controls.py`, `g42_audits.py`, `g42_cg3.py`, `g42_screen.py`;
  `gate42/results/g42_controls.json` (hash gate, chain reads,
  anchors), `g42_audits.json` (full deciding audits, chain reads,
  vector hashes, exclusion and distinctness checks),
  `g42_cg3.json` (cross-check point ladder), `g42_screen.json`
  (registered-set screening), `g42_screen_dense_variant.json`
  (density cross-check). No ledger append, no publication, no
  successor launch — the parent publishes any surviving set.
