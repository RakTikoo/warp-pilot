# Warp Pilot v1.47.0 — Gate-56: Phase 418's carried-point claim set survives independent re-judgement as fenced — a carrying-aware hunt finds base B418, an interior base in the A2 scaling lineage, whose criterion spend is 1.254×10⁻⁹ (≈136× below Phase 400's base, ≈8,660× below B1) and which carries the SS7 criterion at joint +3.652621×10⁻⁶ in the band [10, 20] — at the criterion — H2's own peak halved, by the SS7 definition — the shape scaled to the criterion target (rider G56-R1); B418 is a CRITERION SPECIALIST — it carries nothing at 2× the criterion in the registered search (search-scoped, rider G56-R2) and Phase 412's P* remains the 2× carrier of record (rider G56-R5); SEC −5.294469×10⁻⁴ at the carried point — NO member, NO EC pass

This release publishes Phase 418's claim set as
re-judged by Gate-56 (ledger entry 1118). Phase
418 (THE CARRYING-AWARE HUNT) took up the
question Phase 414's verdict left open: Phase
414 had completed the static margin hunt on a
new base B1, (μ_N, μ_M) = (2.161842, 3.034791),
raising the confirmed static level to
+6.257022×10⁻⁶ — yet when Phase 405's winning
shift shape was carried on B1, the criterion
joint read −4.604584×10⁻⁶, illegal: the deeper
static base trades worse, because the criterion
spend on B1 (1.086161×10⁻⁵) is 63.8× the spend
on Phase 400's base (1.703343×10⁻⁷) at the same
peak. Phase 418 therefore optimised the CARRIED
joint itself: joint optimisation over base
scalings, base corrections and shift shape,
maximising the band joint (NEC/WEC/DEC,
SET-244, band [10, 20]) at the SS7 criterion
peak 0.4426742490267404 directly, under
PEN400, seeded from both ends — Phase 400's
base with Phase 405's proven carrier, and B1
with its Part-2 shapes. Its verdict: A BETTER
CARRYING BASE EXISTS. The winner, base B418,
(μ_N, μ_M) = (2.0473858121439443,
5.606036969201072), K_B = 17, is an interior
base between the two seeds, and at the
criterion its shift is free to within ~10⁻⁹:
its static joint is +3.653875×10⁻⁶ and its
carried joint +3.652621×10⁻⁶, a criterion
spend of 1.254002×10⁻⁹ — the floor of the
three-base comparison. At 2× the criterion
B418 carries nothing (joint −3.055685×10⁻⁵ in
the registered search): it is a criterion
specialist, and Phase 412's P* on Phase 400's
base remains the 2× carrier of record. GATE
REFERRAL.

Gate-56 re-judged the set with fresh machinery
built for the gate alone: its own not-a-knot
cubic spline solver at every spline layer of
the stored assembly (A2 K = 33, H2 K = 17,
base K_B, shape K_S); ALL first/second metric
derivatives derived symbolically with sympy
from the metric (g_tt = −N², g_tx = −βS,
γ_ij = δ_ij + (M−1)n_i n_j) and contracted by
the gate's own einsum assembly — replacing
exactly the layer where the lineage carries
hand-derived formulas; its own ADM Eulerian
tetrad; its own Hawking–Ellis eigenvalue
margins; its own exact secular-equation
worst-null (Newton-refined, KKT certificate),
corroborated by a re-implemented fib(642) scan
plus Nelder–Mead polish; the registered
adversary polish protocol on gate machinery;
and a 50-digit mpmath spot check of the full
chain at the carried point's binding site.
Nothing was imported from phase418/work or the
lineage libraries in any deciding path (they
appear only as calibration comparators).
Calibrations CAL-1…CAL-5 pass (spline vs scipy
≤4.8×10⁻¹⁶; profiles vs the lineage assembly
≤8.9×10⁻¹⁶; gate tensor vs the lineage's hand
algebra ≤2.7×10⁻¹⁵; tetrad and margins exact);
controls (the Phase 405 winner, Phase 412's
P*, the Phase 400 and B1 statics) reproduce at
roundoff before any claim read. The laptop was
run as an admission control and is ADMITTED
(endpoint joint diff −2.7×10⁻²⁰, SEC
+1.7×10⁻¹⁸, ρ 0.0, worst-null +1.4×10⁻²⁰,
argmin radius and peak identical); deciding
reads remain the VM's. The 50-digit spot check
reads NEC 3.6526207343841666×10⁻⁶ and
worst-null 3.5127967556115107×10⁻⁶ at the
binding point, with all four mixed-tensor
eigenvalues exactly real — the float64
deciding values are confirmed independent of
the float64 frame entirely. Both of Phase
418's disclosures were audited and are
CONFIRMED from the stored records: the Phase
414 seed-attribution correction (in
p414_screens2.jsonl, id 0's shape vector is
bit-identical to the Gate-50 shape scaled to
the criterion and id 1 is the H2-shape seed —
the pairing Phase 418 asserts; both seeds are
deep B1-carried failures under either label,
so the correction changes no verdict) and the
pattern-execution disclosure (stage counts
recounted from the screen record equal the
state's exactly — S 6, T 228, A 800, B 350,
R 300, R17 200; total 1,884 ≤ the registered
2,200 cap; Stage G not triggered; rejects and
penalised evaluations 0; the referred points
are coordinate-descent screens found by the
base search, so the verdict rests on none of
the squeezed blocks; one cosmetic record note:
p418_state.json's total_screens field reads
1,684 — the main driver only — while the
screen record, stage counts, memo and
checkpoint all carry the correct 1,884).
Verdicts: (a) SURVIVES; (b) SURVIVES; (c)
SURVIVES AS FENCED (search-scoped, rider
G56-R2); (d) SURVIVES — with riders G56-R1
(the peak is construction, quoted in the
rider's form), G56-R3 (the C-10 frame
convention for sampled joints at non-Type-I
argmins) and G56-R5 (the specialist fence).
The quotable set (GATE56.md §1: G56-A…G56-D,
riders G56-R1…R5) is embedded verbatim as a
blockquote at the end of these notes.

## The claims in brief

(a) G56-A — THE CARRIED POINT SURVIVES. On
base B418 the stored criterion configuration
(Phase 418 screen 1347) carries a positive
joint at the SS7 criterion: joint (NEC = DEC
= WEC minimum) +3.6526207343841256×10⁻⁶ (gate
diff +1.2×10⁻¹⁹), binding at
r = 18.170731707317074, Type-I at every SET-244
point; worst-null +3.5127967556114907×10⁻⁶
(diff −8.5×10⁻²¹); adversary polish
+3.616014548066894×10⁻⁶ (diff +1.4×10⁻²⁰). The
score-incumbent (screen 1320) reads the same
way: joint +3.6518621144739354×10⁻⁶, worst-null
+3.512020893143546×10⁻⁶, polish
+3.626875336510207×10⁻⁶. SEC minimum
−5.294468643886768×10⁻⁴, confirmed on the face
— not an EC pass, not a member. The peak is
at the criterion under rider G56-R1: the
stored vector's achieved peak reads exactly
the float 0.4426742490267404 at r = 10 on the
FINE_R grid and on 20,001-point and
200,001-point dense scans; quote it only as
"at the criterion — H2's own peak halved, by
the SS7 definition — the shape scaled to the
criterion target."

(b) G56-B — THE SPEND FLOOR SURVIVES. B418's
static joint is +3.653874736289154×10⁻⁶ (gate
diff 0.0), so its criterion spend — static
minus carried at the matched peak — is
1.2540019050282306×10⁻⁹, the floor of the
three-base comparison at matched peaks,
gate-recomputed: B418 1.254×10⁻⁹ < Phase 400's
base 1.703342770228576×10⁻⁷ < B1
1.0861605997805081×10⁻⁵ (≈136× and ≈8,660×
above B418 respectively). The B1 leg carries
rider G56-R3 (its stored-joint form is the
quotable one; the gate-frame global form is
1.0932787907783542×10⁻⁵, +0.65%); the ordering
is untouched under it.

(c) G56-C — THE 2× NEGATIVE SURVIVES AS
FENCED (rider G56-R2, search-scoped). On B418
at 2× the criterion, the stored winners of
both registered resolutions (K_S = 9, screen
1648; K_S = 17, screen 1788) read joint
−3.05568504581619×10⁻⁵ / −3.055685517891921×10⁻⁵
— the rungs agree — NEC-bound at
r = 12.073170731707318, with the exact
worst-null at the binding point
−3.206208318096399×10⁻⁵ (gate diff +1.2×10⁻¹⁹
at the identified point) and SEC
−5.578679240331959×10⁻⁴. B418 carries nothing
at 2× in the registered search; Phase 412's
P* on Phase 400's base remains the 2× carrier
of record. This is a statement about a search,
never a non-existence proof.

(d) G56-D — THE LANDSCAPE SURVIVES. Along the
400-base→B1 transect (K_B = 9 representation)
the static joint rises monotonically
+1.182534×10⁻⁶ → +6.257022×10⁻⁶ while the
carried joint peaks in the interior
(+2.583524×10⁻⁶ at μ_M ≈ 6.36) and collapses
at the B1 end; the gate re-derived all twelve
stored transect configurations (statics at
≤2.7×10⁻¹⁹; interior carried reads at
≤5.4×10⁻²⁰; the B1-end carried reads inside
the G56-R3 band). The screen-cloud recount is
exact: 1,378 feasible criterion screens, 859
with joint > 0, 760 above the old bar
+1.227385×10⁻⁶, with per-μ_M-bin maxima
matching the phase's table at every bin.

## Fences (GATE56.md §0 — bind every quotation)

- **Band [10, 20]** on every figure in this
  set.
- **No member, no EC pass:** SEC fails at the
  carried point (−5.294469×10⁻⁴) and is
  printed on its face in G56-A. Nothing here
  is a drive: the candidate remains
  band-scoped, like its lineage.
- **The peak is construction (rider G56-R1):**
  quote it only as "at the criterion — H2's
  own peak halved, by the SS7 definition — the
  shape scaled to the criterion target," never
  as a measured coincidence and never as
  exceeding the criterion.
- **Criterion specialist (rider G56-R5):**
  whenever the criterion ladder or the spend
  comparison is quoted, G56-C rides alongside:
  B418 holds the criterion point and the spend
  floor, and carries nothing at 2×; the 2×
  rung of the ladder remains Phase 412's P*
  on Phase 400's base. G56-C itself is
  search-scoped (rider G56-R2), not an
  impossibility result.
- **C-10 frame convention (rider G56-R3):** a
  SET joint whose argmin is a non-Type-I point
  is a sampled statistic carrying the Gate-43
  C-10 band (±~3×10⁻⁶); its deciding anchor is
  the exact worst-null at a named point. The
  gate's global sampled joints differ from the
  lineage's by ≤7.2×10⁻⁷ at B1T1, the 2×
  winners, the H2 centre and the Phase 414
  seeds — in every case the stored read
  reproduces at roundoff at the phase's own
  argmin point and the exact worst-null
  anchors agree at ≤1.5×10⁻¹⁸. No deciding
  figure of G56-A or of the B418/400 legs of
  G56-B is exposed: their argmins are Type-I.
- **Lineage wording (rider G56-R4):** every
  quotation retains "in the A2 scaling lineage
  of this programme" together with these
  fences.
- **The spend floor is a property of the three
  named bases at the criterion peak**, not a
  bound on the family.

## The quotable set (GATE56.md §1, verbatim)

> **G56-A (the carried point).** On base B418, (μ_N, μ_M) =
> (2.0473858121439443, 5.606036969201072), K_B = 17, the stored
> criterion configuration (Phase 418 screen 1347) carries a positive
> joint at the SS7 criterion: **joint (NEC = DEC = WEC minimum)
> +3.6526207343841256×10⁻⁶**, binding at r = 18.170731707317074,
> Type-I at every SET-244 point; worst-null at the binding point
> **+3.5127967556114907×10⁻⁶**; adversary polish
> **+3.616014548066894×10⁻⁶** at r = 18.8126818196957 (Type-I,
> SAMPLER-M). **SEC minimum −5.294468643886768×10⁻⁴ — on the face:
> not an EC pass, not a member.** The peak is at the criterion under
> rider G56-R1. The score-incumbent (screen 1320) reads the same
> way: joint +3.6518621144739354×10⁻⁶, worst-null
> +3.512020893143546×10⁻⁶, polish +3.626875336510207×10⁻⁶, SEC
> −5.489496097910961×10⁻⁴. Both configurations are re-derived from
> the stored vectors; every deciding figure reproduces at ≤1.4×10⁻¹⁹
> (worst-null at ≤8.5×10⁻²¹), and the binding point is confirmed in
> 50-digit arithmetic (NEC 3.6526207343841666×10⁻⁶; worst-null
> 3.5127967556115107×10⁻⁶).
>
> **G56-B (the spend floor).** B418's static joint is
> **+3.653874736289154×10⁻⁶** (gate diff 0.0), so its criterion
> spend — static minus carried at the matched peak — is
> **1.2540019050282306×10⁻⁹**, the floor of the three-base
> comparison at matched peaks, gate-recomputed: **B418 1.254×10⁻⁹ <
> 400's base 1.703342770228576×10⁻⁷ < B1 1.0861605997805081×10⁻⁵**
> (≈136× and ≈8,660× above B418 respectively). The B1 leg carries
> rider G56-R3; the ordering is untouched under it.
>
> **G56-C (the 2× negative, search-scoped — G56-R2).** On B418 at 2×
> the criterion, the stored winners of both registered resolutions
> (K_S = 9, screen 1648; K_S = 17, screen 1788) read joint
> **−3.05568504581619×10⁻⁵ / −3.055685517891921×10⁻⁵** — the rungs
> agree — NEC-bound at r = 12.073170731707318, with the exact
> worst-null at the binding point **−3.206208318096399×10⁻⁵** (gate
> diff +1.2×10⁻¹⁹ at the identified point) and SEC
> −5.578679240331959×10⁻⁴. B418 carries nothing at 2× in the
> registered search; **412's P\* on 400's base remains the 2×
> carrier of record.**
>
> **G56-D (the landscape).** Along the 400-base→B1 transect (K_B = 9
> representation), the static joint rises monotonically
> **+1.182534×10⁻⁶ → +6.257022×10⁻⁶** while the carried joint peaks
> in the interior (+2.583524×10⁻⁶ at μ_M ≈ 6.36) and collapses at
> the B1 end; the gate re-derived all twelve stored transect
> configurations (statics at ≤2.7×10⁻¹⁹; the interior carried reads
> at ≤5.4×10⁻²⁰; the B1-end carried reads inside the G56-R3 band).
> The screen cloud recount is exact: **1,378 feasible criterion
> screens, 859 with joint > 0, 760 above the old bar
> +1.227385×10⁻⁶**, with per-μ_M-bin maxima matching the phase's
> table at every bin (the [5,6) bin holds the G56-A winner; [7,8)
> and [10,11) are unsampled).
>
> **G56-R1 (peak quotation form; the G49-F / G50-R5 / G52-R1
> discipline).** The equality of the carried point's peak with the
> SS7 criterion is **construction, not an independent measurement**:
> the criterion is defined as one half of H2's peak, and the
> winner's shape was scaled to that target. The gate's independent
> content is: the stored vector's achieved peak reads **exactly the
> float 0.4426742490267404** on the FINE_R grid and on 20,001-point
> and 200,001-point dense scans, attained at the band's inner edge r
> = 10 (the shape spline's first knot, β × 0.4024311354788549); the
> shift at the binding site is S = 0.004528237519742856 — the
> front-loaded ramp is nearly off where the joint binds; and the
> joint at that peak is positive (G56-A). Quote the peak as "**at
> the criterion — H2's own peak halved, by the SS7 definition — the
> shape scaled to the criterion target**," never as a measured
> coincidence and never as exceeding the criterion.
>
> **G56-R2 (search scope of the 2× negative).** G56-C is a statement
> about a *search*: the registered pattern on base B418 (K_S = 9
> family and its gated K_S = 17 arm), the band [10, 20], SET-244.
> Outside that scope it says nothing; it is not, and may never be
> quoted as, a non-existence proof at 2× on this base.
>
> **G56-R3 (C-10 frame convention).** A SET joint whose argmin is a
> non-Type-I point is a sampled statistic and carries the Gate-43
> C-10 frame-convention band (±~3×10⁻⁶); its deciding anchor is the
> exact worst-null at a named point. This rider touches: the G56-C
> sampled joints (gate's own global reads −3.1105×10⁻⁵ in its frame;
> both stored winners reproduce at the phase's own argmin point at
> +5.4×10⁻²⁰, worst-null at +1.2×10⁻¹⁹); the B1 leg of G56-B
> (gate-frame global form of the spend 1.0932787907783542×10⁻⁵,
> +0.65% — the stored-joint form in G56-B is the quotable one); and
> the transect's two B1-end carried reads in G56-D. **No deciding
> figure of G56-A or of the B418/400 legs of G56-B is exposed**:
> their argmins are Type-I and reproduce at roundoff.
>
> **G56-R4 (lineage wording, carried from G50-R6 / G52-R4).** Any
> quotation of this set retains "in the A2 scaling lineage of this
> programme" together with the §0 fences.
>
> **G56-R5 (the specialist fence).** Whenever the criterion ladder
> or the spend comparison is quoted, G56-C rides alongside: B418
> holds the criterion point and the spend floor, and carries nothing
> at 2×; the 2× rung of the ladder remains 412's P\* on 400's base.

> *Gate-56 records: `gate56/results/` (g56_controls.json,
> g56_reads.json, g56_spot.json, g56_admission_vm.json,
> g56_admission_laptop.json); machinery `gate56/work/`
> (g56_registration.md, g56_splines.py, g56_lib.py,
> g56_build_tensor.py, g56_tensor.py, g56_controls.py,
> g56_reads.py, g56_reads2.py, g56_spot.py,
> g56_admission.py). Working record:
> `gate56/GATE56_CHECKPOINT.md`.*
>
> DESK: NO DATA CONTACT.

**Links.** Concept DOI: 10.5281/zenodo.24425078.
Version DOI: TBD — Zenodo mints it at release.

Disclosure: this is AI-driven analysis — the
computation was produced by an AI research system
working under my direction, and I am posting it
precisely to have its legitimacy checked by humans:
is the argument sound, and is it already known?
Corrections and references are exactly what I am
asking for.
