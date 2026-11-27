# PHASE 405 MEMO — W15: CHEAP-SHIFT SHAPES ON THE
STATIC WINNER'S BASE

VERDICT: SHAPE PAYS — GATE REFERRAL of the
re-introduced claim set.

Phase 404 priced the FIXED shape on Phase 400's
corrected static base: H2's S shape scaled breaks
even at μ_S* = 0.171875 (peak |β·S| = 0.1522) and
at the SS7 warp criterion (μ_S = 0.5, peak
0.4427) it stands at −9.186×10⁻⁶ — a measured
cost of 1.058×10⁻⁵ against the base's
+1.397719×10⁻⁶ margin. This phase freed the
shape: N/M held at 400's winner verbatim, S a
free spline (p341's family, K = 9) searched to
maximise the peak |β·S| subject to the joint
(SET-244, band [10, 20]) ≥ 0. THE SHAPE PAYS,
DECISIVELY: the best shape carries the FULL
criterion peak |β·S| = 0.4426742490267404 at a
confirmed joint of +1.227385×10⁻⁶ — it spends
1.703×10⁻⁷ of the base's margin where the fixed
shape spends 1.058×10⁻⁵, a factor of 62 cheaper
at the same amplitude on the same base. The
re-introduced configuration is a CANDIDATE: no
member is claimed (SS7 fences below); the claim
set is referred to a gate. Gate-48, pending at
charge time, has since ruled the BASE claim set
SURVIVES in full — the base fence is discharged;
what remains gated is this phase's re-introduced
set itself.

Charge: ledger entry 1043. Registration:
work/p405_registration.md (SS0–SS7), filed
before any computation. Frame: VM (laptop
admitted at roundoff; §Controls).

## The best shape and its cost curve

Best shape: the Stage C lineage (optimised at
peak 0.25), K = 9 knots at r = (10, 11.25, 12.5,
13.75, 15, 16.25, 17.5, 18.75, 20). At the
criterion amplitude its knot vector is
(0.402431, 0.232376, 0.101105, 0.030274,
0.021560, 0.012972, 0.007865, 0.003529,
−0.000435) — exact digits in
results/p405_confirmation.json. A monotone
front-loaded ramp: the shift lives at the INNER
edge of the band and has essentially vanished
by the fragile outer radii.

Cost curve (the shape scaled; Stage D reads,
confirmed at two amplitudes at diff 0.0):

| peak \|β·S\| | joint | binding | NEC site | SEC min |
|---|---|---|---|---|
| 0.0500 | +1.3960×10⁻⁶ | NEC | 17.68 | −2.052×10⁻⁴ |
| 0.1000 | +1.3902×10⁻⁶ | NEC | 17.93 | −2.057×10⁻⁴ |
| 0.1522 | +1.3793×10⁻⁶ | NEC | 17.93 | −2.067×10⁻⁴ |
| 0.2000 | +1.3653×10⁻⁶ | NEC | 17.93 | −2.079×10⁻⁴ |
| 0.2500 | +1.3463×10⁻⁶ | NEC | 17.93 | −2.095×10⁻⁴ |
| 0.3000 | +1.3226×10⁻⁶ | NEC | 17.93 | −2.119×10⁻⁴ |
| 0.3500 | +1.2942×10⁻⁶ | NEC | 17.93 | −2.147×10⁻⁴ |
| 0.4000 | +1.2605×10⁻⁶ | NEC | 17.93 | −2.181×10⁻⁴ |
| 0.4427 | +1.2274×10⁻⁶ | NEC | 17.93 | −2.214×10⁻⁴ |

The curve never turns down toward zero: at the
criterion the joint is still 88% of the static
margin. (The registered curve grid tops out at
the criterion; no amplitude beyond it was read.)

CONFIRMATION at the criterion amplitude (full
re-read, diff 0.0 vs the stored screen): joint
+1.2273852081052888×10⁻⁶; peak |β·S| =
0.44267424902674035; Type-I fraction 1.0000 and
the Type-I NEC min equals the joint; the exact
worst-null at the SET NEC argmin is
+7.282191×10⁻⁷ (positive pointwise); the
adversary polish's in-region worst NEC is
+1.214724×10⁻⁶ at r = 17.792 (positive — not a
grid artefact); SEC min −2.213557×10⁻⁴, ON THE
FACE (SEC is outside the lineage's joint at
every point of this line). At the stage
amplitude (peak 0.25): joint +1.346254×10⁻⁶
(diff 0.0), worst-null +1.019934×10⁻⁶, polish
+1.327027×10⁻⁶, SEC −2.095120×10⁻⁴.

THE SECOND SHAPE (Stage B lineage, optimised at
the criterion directly) also reaches the
criterion at joint ≥ 0 — but only just:
+9.733734×10⁻⁹ (screen 375). Its cost curve
sags onto the DEC plateau (DEC argmin migrating
to r = 19.88) and spends the whole margin by
peak 0.25 (+1.213×10⁻⁸). Stage D's P* is the
criterion for both shapes; the best shape is C
by the joint at the criterion (two orders of
magnitude). K = 17 (Stage E) was gated OFF by
the registration: the criterion was reached at
K = 9.

## Anatomy — why the shape is cheap

The NEC cost of a shift in this family is
carried by S′′ (Phase 316's anatomy, holding
throughout this line). At the criterion read's
binding site (r = 17.926829268292682, the base's
own fragile region) the winning shape has
S = 0.006480, S′ = −0.003428, S′′ = −0.000695 —
all nearly zero: the shape arrives at the
fragile radii already switched off. Its peak
|β·S| sits at r = 10.0, the inner band edge
(S = 0.402431), and its curvature budget is
spent at small radii, where the base's margins
are wide. The fixed shape does the opposite: it
peaks mid-band and carries substantial S′′
exactly where the base is fragile. In price
terms: the fixed shape's measured cost at the
criterion amplitude on this base is
1.058×10⁻⁵ (404; implied A_c ≈ 4.7×10⁻⁵ at
397's p — pricier even than 401's 3.66×10⁻⁵
prior on the neighbouring base); the free
shape's measured cost at the same amplitude is
1.703×10⁻⁷. Shape freedom is worth a factor of
~62 on this base, and the cost that remains is
nearly amplitude-flat (the curve above), not
the fixed shape's ~amplitude^2.16 law.

A SEARCH ANATOMY, ON THE RECORD: the shape
optimised AT the criterion (Stage B) landed on
the DEC plateau and nearly stalled; the shape
optimised at MID peak (Stage C), where a single
NEC site binds and the gradient is clean, found
the front-loaded direction, and scaling it up
stayed cheap. The amplitude at which you
optimise decides what you find.

## Controls

VM, all diff 0.0 (results/p405_controls.json):
CTL-405-WIN — the winner reproduced through
this phase's own assembly at vS = 0 (K = 9 and
K = 17): five minima, joint and worst-null at
diff 0.0; max |S|, |S′|, |S′′| over the SET
grid = 0.0 exactly; the frozen base's floors
hold. CTL-405-H2S — (1, 1, 1) → L_stat(H2).
CTL-405-C395 — the C395 triple → its stored TG
and worst-null. CTL-405-FIX — the fixed-shape
control on this base: 404's own assembly read
through this phase's session at μ_S = 0.171875
and μ_S = 0.5 reproduces p404_ladder.json's
stored rows (joint, five minima, peak) at diff
0.0; the fixed shape's achievable peak at joint
≥ 0 is P_fix = 0.152169273102942. Stage A's
reference curve (the H2 shape spline-embedded,
an interpolant, labelled as such) tracks 404's
ladder within 3.5×10⁻⁸ at the criterion.
CTL-405-ADM — laptop ADMITTED at roundoff
(diffs ≤ 5.5×10⁻¹⁹, argmin radii identical —
the 398/400/401 admission values exactly);
deciding reads are nevertheless all VM reads
per SS2.

SEARCH ACCOUNTING: 726 stored screens (A 8;
B 400, cap-bound; C 300, cap-bound; D 18;
E gated off), ZERO rejected — every screen
C1-feasible. PEN400 (LAM400 = 1.0×10⁻⁵, Phase
400's rescaled penalty) priced every walk.
ONE INCIDENT, DISCLOSED: a runtime restart
killed Stage B's first process at 308/400 stage
screens; the stage was resumed from the
state-file incumbent (screen 238) under the
stage count restored from the append-only
screens record (the Phase 398 precedent) and
completed the registered pattern at exactly
400. No screen was lost or duplicated.

## Fences

Band pose [10, 20] only, β = 1.1; 356's
full-extent caveats travel (no full-extent read
of the re-introduced configuration is claimed).
The level is the lineage's joint min(NEC, DEC);
SEC, outside that joint, is −2.213557×10⁻⁴ at
the best point and is reported on the face,
never hidden. No EC pass and no member by
verdict name: the configuration at the
criterion is a warp-grade CANDIDATE whose claim
set is referred to a gate — Gate-48 has
confirmed the BASE (the Phase 400 set SURVIVES
in full, (e) as rider G48-E); a gate of the
re-introduced set itself is still owed before
any member language. Sampled minima name their
frame convention (SAMPLER-M, Gate-43 C-10);
deciding values are diff-0.0 reproductions,
frame-invariant worst-nulls and the adversary
polish. No sustainment, front or transport
content. Three-goal accounting: Goal 1 — the
re-introduction question is answered on this
base: a free-shaped shift at the SS7 criterion
amplitude stands at a positive band joint; the
drive chain's next links (a gate of this set;
then sustainment) are named, not run. Goals 2
and 3 untouched.

DESK: NO DATA CONTACT — the programme's own
stored configurations, re-shaped and re-read on
its own instruments; no external data of any
kind.

Files: work/p405_registration.md, work/p405_lib.py,
work/p405_controls.py, work/p405_admission.py,
work/p405_search.py, work/p405_search_B_resume.py,
work/p405_confirm.py; results/p405_controls.json,
results/p405_controls_laptop.json,
results/p405_screens.jsonl, results/p405_state.json,
results/p405_search_B.log, results/p405_search_Bresume.log,
results/p405_search_C.log, results/p405_confirmation.json.
Spend: ≈ 90 min VM wall (controls ≈ 1 min,
search ≈ 85 min, confirmation ≈ 2 min); laptop:
the admission read only.
