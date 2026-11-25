# P243-1 — MEMO: CERTIFY OR REFUTE THE (0.55625, 0.5625]
# BRACKET (FU-P234-1, SECOND REGISTRATION) — INTEGRATED RECORD

Worker of Phase 243 (single item P243-1), warp pilot.
Registration (pre-run): `phase243/work/p2431_registration.md`.
Driver: `phase243/work/p2431_run.py`; results:
`phase243/results/p2431_results.json`; checker:
`phase243/work/p2431_check.py` →
`phase243/results/p2431_verify.json`. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python
(numpy 2.5.5 / scipy 1.18.1), float64. INTERNAL only. No
ledger append, no launch, no external contact; nothing
outside `phase243/` edited. Protected files byte-identical
before/after (§7).

## VERDICT — FORM 1 FIRES

**BRACKET CERTIFIED** (disposition **T-A**). The run's
recorded verdict note, verbatim from `p2431_results.json`:

> The three-channel first crossing (0.55625, 0.5625] on
> NEC_ph = DEC_ph is CERTIFIED under the p2401 registration:
> CERT-1..4 hold (per-instant Richardson limits on NEC_ph/DEC_ph
> over (0.5, 0.65] meet the 1e-6 bar; the limit straddles zero
> at the bracket with no earlier in-window crossing). Phase
> 214's t* bracket, re-read under the SAME certificate,
> certifies as posed (0.5, 0.50625] (disposition T-A) — the
> comparison is in one frame and the sustainment interval's
> extension is a finding in the certified scope, fenced by
> the tail limitation (tail_pricing_stored: Stage B reads
> past the window are NOT certified), pose scope, jet scope,
> and the p1592 gate on programme-level wording. Named
> successor: a Gate registration on the certified claim set.

One wording note, stated plainly: the note's phrase "under
the p2401 registration" is driver prose carried verbatim
from Phase 240's driver (the phrase spans a string
concatenation in the source and was not rewritten by the
adaptation). The registration of record for this run is
`phase243/work/p2431_registration.md`, as recorded in the
results file's `registration` field; the certificate
applied is that registration's (Phase 240's design,
unchanged in substance, plus the §R repair). No number is
affected.

Named successor (registration §7, form 1): **a Gate
registration on the certified claim set.** (Amending
Gate-22's claim set is the parent's act, not this phase's.)

## 1. REGISTRATION SUMMARY, WITH THE REPAIR

The registration carries Phase 240's registration unchanged
in substance: §0 the question; §1 the scope argument (a
refinement gate certifies the reads that carry a claim; the
1×10⁻⁶ threshold nowhere changed; the tail's Stage B
failure recorded on the face of the verdict as the tail
reads' priced limitation, NOT silently dropped); §2 the t*
disposition (Phase 214's bracket (0.5, 0.50625] re-read
under the SAME certificate on the director-only pose;
dispositions T-A / T-B / T-C fixed in advance, with the
§5(c) restated-bracket search on the ladder {0.50625,
0.5125, 0.51875, 0.525}); §3 the certificate (grids G3
N_θ=5761 h_t=0.00125, G4 11521/0.000625, G5 23041/0.0003125;
binding clauses NEC_φ and DEC_φ; windows W_new = sampled
{0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65} ∪ refined
{0.55625, 0.5625, 0.56875} with bracket (0.55625, 0.5625],
W_* = sampled {0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6} ∪
refined {0.50625, 0.5125, 0.51875} with bracket
(0.5, 0.50625]; per-instant Richardson exactly as Phase 240
§3 — monotone case p = log2(d34/d45), admissible
0.5 ≤ p ≤ 6, L = v5 − d45/(2^p − 1), r = |d45|/(2^p − 1);
degenerate case L := v5, r := max(|d34|, |d45|);
limit-certified iff r ≤ 1×10⁻⁶ AND |d34| ≤ 1×10⁻⁶ AND
|d45| ≤ 1×10⁻⁶; CERT-1 every window instant
limit-certified both binding clauses; CERT-2 L(t_lo) ≥ 0,
L(t_hi) < 0, v5(t_lo) ≥ 0, v5(t_hi) < 0; CERT-3 no earlier
in-window crossing at L or v5; CERT-4 no non-binding clause
crosses first at G5 in the window, non-clause bars —
momentum ≤ 1×10⁻¹⁰, flare > 0, domain regular — read at G5
at the bracket instants, a failure voids CERT-4); §4
controls CTRL-2/CTRL-3 as in Phase 240; §5 deciding reads
including §5(d) tail pricing from Phase 234's stored rows
(record only, reported on the face under either verdict
form); §6 decision order (controls → probe rule →
new-bracket certificate → t* dispositions; under T-B form 1
requires the new bracket entirely past the restated
certified t* bracket, else form 2; under T-C form 1 is
stated against the Stage-A-certified interval end 0.5
only); §7 the three verdict forms verbatim in substance;
§8 fences; §9 checker.

**THE ONE REPAIR** (registration §R; the only deviations,
each stated on the registration's face with Phase 240's
anatomy — memo §8 of Phase 240 — cited):
(a) CTRL-1 restated at MATCHED MARCH LENGTH: fresh G3/G4
marches run to T_END = 1.0, the stored rows' length.
(b) ALL window-read marches fixed at T_END = 1.0 for every
grid (G3, G4, G5), so every window instant (max 0.65) is an
interior (centred-stencil) read in every grid and the
cross-grid Richardson treatment compares one read class
throughout. Per-grid state-array size stated on the face:
(3201 × 23041) float64 = 590,033,928 B per field at G5
(MU + U + MTT ≈ 1.770 GB); G3/G4 states freed before the G5
march.
(c) The §5(e) G5 cost probe, arithmetic only: probe [0, 0.05]
(160 steps), project the registered [0, 1.0] march (3200
steps) as 20 × probe wall; the 900 s threshold UNCHANGED.

Run wall: 772.5 s total (G5 march alone 466.7 s).

## 2. CONTROLS

**CTRL-2 — PASS, bit-exact** (evaluated first in the
driver's stored-row block, per Phase 240's machinery):
stage gates recomputed from Phase 234's stored rows —
Stage A 3.4339573895536546×10⁻⁷ = stored, Stage B
3.4498744435396134×10⁻⁵ = stored.

**CTRL-1 — PASS, all diffs 0.0** (restated, matched length
T_END = 1.0):

| comparison | max abs diff |
|---|---|
| three-channel G4 sampled (≤ 0.65) vs Phase 234 stored | 0.0 |
| three-channel G3 sampled (≤ 0.65) vs Phase 234 stored | 0.0 |
| three-channel G4 refined {0.55625, 0.5625, 0.56875} vs stored | 0.0 |
| director-only G4 sampled vs Phase 214 stored | 0.0 |
| director-only G4 refined t = 0.50625 vs Phase 214 stored | 0.0 |

The Phase 240 failure is closed exactly where the anatomy
said it would be: at matched march length every stored row
reproduces at 0.0, including t = 0.65.

**CTRL-3 — PASS** (G5 admitted): fresh G5 director-only
reads vs Phase 210's stored G4 director rows — t = 0.25:
1.4235054024425153×10⁻⁸; t = 0.5: 5.694021876223587×10⁻⁸,
both ≤ 1×10⁻⁶.

## 3. G5 COST PROBE (§5(e), repaired arithmetic)

Probe march G5 over [0, 0.05] (160 steps): **21.2278 s**.
Projection for the registered [0, 1.0] march (3200 steps):
20 × probe = **424.556 s ≤ 900 s** — the rule does NOT
fire; G5 was run. (Actual G5 march wall: 466.65 s.)
State-array size on the face: 590,033,928 B per field;
MU + U + MTT = 1.770 GB. The §5(e) kernel-spec packaging
obligation attaches only to form 3, which did not fire; no
spec was written.

## 4. THE CERTIFICATE — NEW BRACKET (three-channel pose)

Per-instant Richardson on NEC_φ = DEC_φ (the two clauses
are pointwise identical in this machinery; one row serves
both — the results file carries both, identical). v3/v4/v5
are the G3/G4/G5 clause minima; L the Richardson limit;
r = |L − v5| the residual. Bar 1×10⁻⁶ throughout.

| t | case | p | v3 | v4 | v5 | d34 | d45 | L | r | cert |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.5 | degenerate | — | 0.44451093947009213 | 0.4445109446003479 | 0.44451096479147711 | −5.130×10⁻⁹ | −2.019×10⁻⁸ | 0.44451096479147711 | 2.019×10⁻⁸ | ✓ |
| 0.525 | degenerate | — | 0.26725749481104621 | 0.26725750785058899 | 0.26725753200888125 | −1.304×10⁻⁸ | −2.416×10⁻⁸ | 0.26725753200888125 | 2.416×10⁻⁸ | ✓ |
| 0.55 | monotone | 2.00001 | 0.061139890494202653 | 0.06114008302117302 | 0.061140131152431998 | −1.925×10⁻⁷ | −4.813×10⁻⁸ | 0.061140147195970052 | 1.604×10⁻⁸ | ✓ |
| **0.55625** (t_lo) | monotone | 2.00001 | 0.0044678765360699479 | 0.0044680761717996731 | 0.0044681260804186884 | −1.996×10⁻⁷ | −4.991×10⁻⁸ | **0.0044681427164857323** | 1.664×10⁻⁸ | ✓ |
| **0.5625** (t_hi) | monotone | 2.00000 | −0.054340077032336787 | −0.054339870018019099 | −0.054339818264502959 | −2.070×10⁻⁷ | −5.175×10⁻⁸ | **−0.054339801013359036** | 1.725×10⁻⁸ | ✓ |
| 0.56875 | monotone | 2.00001 | −0.1153811303795238 | −0.11538091570173625 | −0.11538086203257558 | −2.147×10⁻⁷ | −5.367×10⁻⁸ | −0.11538084414298257 | 1.789×10⁻⁸ | ✓ |
| 0.575 | monotone | 2.00003 | −0.17875773255873195 | −0.17875750991796302 | −0.17875745425910416 | −2.226×10⁻⁷ | −5.566×10⁻⁸ | −0.17875743570674379 | 1.855×10⁻⁸ | ✓ |
| 0.6 | monotone | 2.00000 | −0.45787269289916921 | −0.45787243509889386 | −0.45787237064864694 | −2.578×10⁻⁷ | −6.445×10⁻⁸ | −0.45787234916515218 | 2.148×10⁻⁸ | ✓ |
| 0.625 | monotone | 1.99999 | −0.78417133094263747 | −0.78417103178834813 | −0.78417095699928785 | −2.992×10⁻⁷ | −7.479×10⁻⁸ | −0.78417093206938426 | 2.493×10⁻⁸ | ✓ |
| 0.65 | monotone | 2.00001 | −1.1675966481588502 | −1.1675962999904201 | −1.1675962129489537 | −3.482×10⁻⁷ | −8.704×10⁻⁸ | −1.1675961839354163 | 2.901×10⁻⁸ | ✓ |

The monotone instants sit at p ≈ 2.0000 across the whole
window — clean second-order Richardson behaviour; the two
early instants are degenerate by the registered rule
(d34·d45 ≤ 0 at the 10⁻⁸ scale) with residuals ≤ 2.5×10⁻⁸.
Worst in-window |d34| = 3.482×10⁻⁷ (t = 0.65); worst
residual r = 2.901×10⁻⁸ — every instant clears the bar by
more than an order of magnitude.

**CERT booleans (new bracket): CERT-1 TRUE** (no failures),
**CERT-2 TRUE** (L(0.55625) = +0.0044681427 ≥ 0,
L(0.5625) = −0.0543398010 < 0; v5 likewise +0.0044681261 /
−0.0543398183), **CERT-3 TRUE** (no earlier in-window
crossing at L or v5), **CERT-4 TRUE** (no non-binding clause
crosses first at G5; non-clause bars at the bracket
instants: momentum worst 3.886×10⁻¹⁶ (0.55625) /
4.441×10⁻¹⁶ (0.5625), flare_min 0.14039 / 0.13926 > 0,
domain_R_min 0.65875 / 0.65556 > 0, domain_exp2Phi_min > 0 —
all ok).

## 5. THE CERTIFICATE — t* (director-only pose) AND THE
## DISPOSITION

Per-instant Richardson on NEC_φ = DEC_φ (identical, one row
serves both):

| t | case | p | v3 | v4 | v5 | d34 | d45 | L | r | cert |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.45 | monotone | 0.99992 | 0.2768780033991507 | 0.27687796880462923 | 0.27687795150644856 | 3.459×10⁻⁸ | 1.730×10⁻⁸ | 0.27687793420642781 | 1.730×10⁻⁸ | ✓ |
| 0.475 | monotone | 3.13810 | 0.15080250221139302 | 0.15080241563149732 | 0.15080240579695237 | 8.658×10⁻⁸ | 9.835×10⁻⁹ | 0.15080240453670307 | 1.260×10⁻⁹ | ✓ |
| **0.5** (t_lo) | monotone | 3.13810 | 0.0045419745541246392 | 0.0045418770853060675 | 0.004541866013908713 | 9.747×10⁻⁸ | 1.107×10⁻⁸ | **0.0045418645951645232** | 1.419×10⁻⁹ | ✓ |
| **0.50625** (t_hi) | monotone | 3.13810 | −0.035378515461850668 | −0.035378615815707448 | −0.03537862721480467 | 1.004×10⁻⁷ | 1.140×10⁻⁸ | **−0.035378628675540646** | 1.461×10⁻⁹ | ✓ |
| 0.5125 | monotone | 3.13810 | −0.076755854478407048 | −0.076755957786697637 | −0.076755969521384859 | 1.033×10⁻⁷ | 1.173×10⁻⁸ | −0.076755971025124797 | 1.504×10⁻⁹ | ✓ |
| 0.51875 | monotone | 3.13811 | −0.11965257083847369 | −0.11965267717293537 | −0.11965268925135719 | 1.063×10⁻⁷ | 1.208×10⁻⁸ | −0.1196526907991442 | 1.548×10⁻⁹ | ✓ |
| 0.525 | monotone | 3.13811 | −0.16413442380543986 | −0.16413453324026417 | −0.16413454567084074 | 1.094×10⁻⁷ | 1.243×10⁻⁸ | −0.16413454726375276 | 1.593×10⁻⁹ | ✓ |
| 0.55 | monotone | 2.93074 | −0.36088489979876659 | −0.36088489979879368 | −0.36088489979879723 | 2.709×10⁻¹⁴ | 3.553×10⁻¹⁵ | −0.36088489979879779 | 5.551×10⁻¹⁶ | ✓ |
| 0.575 | degenerate | — | −0.59086934726693618 | −0.59086934726696771 | −0.59086934726696727 | 3.153×10⁻¹⁴ | −4.441×10⁻¹⁶ | −0.59086934726696727 | 3.153×10⁻¹⁴ | ✓ |
| 0.6 | degenerate | — | −0.85929987890753523 | −0.85929987890757697 | −0.85929987890757697 | 4.174×10⁻¹⁴ | 0.0 | −0.85929987890757697 | 4.174×10⁻¹⁴ | ✓ |

**CERT booleans (t*): CERT-1 TRUE, CERT-2 TRUE**
(L(0.5) = +0.0045418646 ≥ 0, L(0.50625) = −0.0353786287 < 0;
v5 likewise), **CERT-3 TRUE, CERT-4 TRUE** (non-clause bars
at bracket instants ok: momentum worst ≤ 3.886×10⁻¹⁶,
flare_min 0.15033 / 0.14925, domain_R_min 0.68588 / 0.68300).

**Disposition: T-A — t* certifies as posed.** The
certificate supports (0.5, 0.50625] for the director-only
pose; the §5(c) restated-bracket search was not needed.
The comparison between the new crossing and t* is now in
one frame: both brackets are certified under the same
certificate, same clauses, same bars.

## 6. TAIL PRICING (§5(d) — ON THE FACE, AS REGISTERED)

From Phase 234's stored rows (record only; no new march):
per-instant G3–G4 max disagreement on (0.5, 0.65] —
2.38697642096497×10⁻⁷ (0.525), 2.61972015191958×10⁻⁷
(0.55), 2.863289170207395×10⁻⁷ (0.575),
3.1176834758284144×10⁻⁷ (0.6), 3.382903068782639×10⁻⁷
(0.625), 6.25625901307103×10⁻⁷ (0.65). First exceedance of
the 1×10⁻⁶ bar in Stage B at **t = 0.775**; max on
(0.65, 1.0] = **3.4498744435396134×10⁻⁵ at t = 1.0**, carrier
**DEC_θ**, relative disagreement 3.3942464143610627×10⁻⁶.
This stands on the face of the form-1 verdict as fence (i):
Stage B reads past the window are NOT certified; the
stage-max gate still fails on the tail and that failure
stands as the tail reads' priced uncertainty.

## 7. PROTECTED FILES — BYTE IDENTITY HOLDS

md5-identical before and after the run (driver-recorded;
checker re-verified live):

| file | md5 |
|---|---|
| phase129/work/p1296_derive_raw.json | d89f6a8646e4a96d7733c0b1827b5fcd |
| phase150/work/p1501_families.py | 9738b6267ec51a10f62db9f495b06b40 |
| phase162/work/p1621_engine.py | 1f12ec29c2693ca00a19da365abeccf4 |
| phase167/work/p167_engine.py | 9db35c0b82635409e0bddf17251ba53f |
| phase169/work/p1692_engine.py | 1781b544920052bcc9b919574561acb2 |
| phase202/work/p2022_wound.py | 24f0d69cd099b89cd42abef59d378b3d |

## 8. CHECKER — 17/17 PASS

`phase243/work/p2431_check.py` →
`phase243/results/p2431_verify.json`: **17 passed, 0
failed.** The checks: protected byte identity (live vs
results before/after); CTRL-2 stage gates recomputed ==
stored; tail first exceedance == 0.775; tail max past 0.65
== stored pricing; stored G3–G4 disagreement on (0.5, 0.65]
≤ 6.26×10⁻⁷ (max 6.25625901307103×10⁻⁷); CTRL-1 recorded
outcome consistent with recorded diffs; fresh G4 spot
recomputation (three-channel and director, T_END = 1.0) at
diff 0.0; fresh G5 spot recomputation (both poses) at diff
0.0; CTRL-3 recorded values ≤ bar and pass; Phase 210
stored director t = 0.5 NEC_φ anchor; Richardson arithmetic
reproduced for both brackets; CERT booleans reproduced for
both brackets; verdict form consistent with §6's decision
order (form 1, disposition T-A).

**What was done differently from Phase 240's checker, as
tasked:** Phase 240's checker asserted "CTRL-1 recorded
diffs all 0.0" as a standalone pass/fail — on a
CTRL-1-failed results file that assertion restates the
discrepancy itself and produced that phase's single
structural FAIL (6/7). The Phase 243 checker's
corresponding assertion is written to match the registered
decision order: it checks that the recorded CTRL-1 pass
flag is *consistent* with the recorded diffs (pass ⟺ all
diffs vanish), so a legitimate control-failure file is
checked consistently rather than failed by construction.
On this phase's file the recorded outcome is a pass with
all diffs 0.0, and the assertion passes. The checker's spot
marches were also moved to T_END = 1.0 to match the
repaired march length.

## 9. FENCES (unchanged from the registration)

(i) Tail limitation (§6 above): Stage B reads past the
window are NOT certified; the stage-max gate still fails
on the tail. (ii) Pose scope: Phase 169 A-branch datum,
true lock; κ = 0.3 director P-DIR-T2 + CH-COMB flat +0.10
P-PROF-FROZEN + CH-PHI-Auu flat −0.5 P-PHI-FROZEN.
(iii) Jet scope / sector superposition: exhibit ≠
construction; no claim a physical sector realises the
three channels jointly. (iv) Programme-level sustainment
wording remains gated by p1592 regardless — untouched by
this verdict. Phase 210/214/226/229/233 verdicts stand for
their own poses and scopes. Phase 234's GATE-BLOCKED
disposition is superseded only in the manner form 1
provides: the bracket it priced is now certified under
this registration's certificate; its stage-gate failure on
the tail stands as priced. Phase 240's control-stopped
record stands as written.
