# Phase 323 memo — THE A-THROAT EVALUATION

**VERDICT: IDENTIFICATION.** The last named datum of the semiclassical
identification is produced. The derived H{2,0}(3) at the A-family
throat is exactly the registered prediction, and the A-throat core
re-read with the fully arbitrated assembly passes at ξ⁰ exactly,
(0, 0, 0). T_S is identified in the registered form: the Ellis core
and the Ellis gate pass at all powers (Phase 318), and the A core now
passes at all powers — ξ⁰ exactly, ξ¹/ξ²/ξ³ at the residue class of
Phase 259's FULL record, unchanged by this substitution.

DESK: NO DATA CONTACT.

## Read (1) — the deciding datum: PREDICTION CONFIRMED EXACTLY

Derived H{2,0}(3) at the A throat, DF print units (Tt, Tr, Tθ):

    route (a), exact rational:  (9/4, 3/4, 21/4)
    registered prediction:      (9/4, 3/4, 21/4)
    route (b), float:           (2.25, 0.7499999999999964, 5.250000000000003)

Route (a) is the ∇-sector engine extended to consume the A family's
Riemann-jet solve: the A metric jet is built in local coordinates
(t, x = l − l₀, u = θ − π/2, φ) from the exact-rational R-jet, and
the E2 programme (Phase 259 `p2591_engine_d.py`, unpatched at the A
throat where g(0) = η) is evaluated in exact Fractions. The derived
tensor there is divergence-free exactly, ∇_a H^a_b = (0, 0, 0, 0),
and its Ricci cross-check against the harness's independent driver
geometry deviates by 0.0.

Route (b) is the independent second path: a Phase 323 copy of
Phase 318 Task D's full transcription of DF Eq. (2.23), evaluated on
the A background through the Phase 241 driver machinery. It agrees
with route (a) at the deciding datum to ≤ 3.6×10⁻¹⁵ (float residue),
reproduces Phase 318's stored `check_h4_out.json` bit-for-bit on
every shared point and tensor (max deviation 0.0), and returns the
derived H(6,3)(3) / H(6,3)(4) values at A exactly, (3, 3/2, 39/8)
and (3/4, 3/4, −3/8). Phase 318's stored file was not overwritten
(md5 verified before and after).

Caveat carried from Phase 318, unchanged: route (b)'s REST
cross-check at A shows diffs (Tr −1/105, Tθ +1/30 in DF-sum units)
attributable to the arbitration-side print H(6)/H(8) §2-transcription
values — the known residue family of that transcription. Read (2)
below is algebraically immune: P6/P8 enter the Phase 259 FULL
residual and the REST back-out with opposite signs and cancel, which
is verified in the working. Route (b)'s evidentiary role is the
H{2,0}(3) value itself, where it is clean.

## Read (2) — the A-throat core at ξ⁰, exact

With Phase 318's derived H(6,3)(3) = (3, 3/2, 39/8) and
H(6,3)(4) = (3/4, 3/4, −3/8) at A (joint-consistent set; print (3),(4)
at A were never separately isolated — REST is one back-out equation
in three tensors, as Phase 318 recorded):

    REST_derived(A) = (1/140)(9/4, 3/4, 21/4)
                      − (8/945)(3, 3/2, 39/8)
                      + (2/315)(3/4, 3/4, −3/8)
                    = (−23/5040, −13/5040, −31/5040)
    REST_print(A)   = (−23/5040, 1/144, −199/5040)     [Phase 318 record]
    delta bracket   = 210·(REST_derived − REST_print) = (0, −2, +7)

    Phase 259 FULL A-throat ξ⁰ residual:   (0, +2, −7)
    arbitrated ξ⁰ residual:                (0, 0, 0)   EXACT

H{2,0}(3) enters the assembly only through REST at the ξ⁰ power, so
the A core's other powers are exactly Phase 259's FULL record:
ξ¹ max residual 2.27×10⁻¹³, ξ² 5.60×10⁻¹³, ξ³ 0.0 — the record's
residue class. The A core passes at all powers.

## Read (3) — the wider set, reported at its own weight

The route-(a) evaluation covers every non-Ellis harness point. The
ξ⁰ re-read below is a float re-read (stored FULL ξ⁰ cell +
210·ΔREST(point), with ΔREST from the exact route-(a) H{2,0}(3) and
the replicated per-point H(3)/H(4) and REST values). It decides
nothing — the deciding reads are the two exact cores — and is
reported as corroboration: the H{2,0}(3) substitution accounts for
the ξ⁰ failure at every evaluated point of the harness, not only at
the cores.

Per-family ξ⁰ maxima, Phase 259 FULL → arbitrated:

    A_throat   7.000      →  2.1×10⁻¹⁴
    A_fullr    4.116      →  7.1×10⁻¹⁴
    C          250.000    →  5.1×10⁻¹³
    D          7.997      →  4.3×10⁻¹⁴
    E          108.044    →  2.8×10⁻¹²

Every individual ξ⁰ cell of the 20 evaluated points lands at
≤ 2.8×10⁻¹² (full per-point table in `p323_reassembly.json`).

## Controls

- **C(i) PASS, exact.** Phase 318's final read reproduced from the
  stored artefacts in exact Fractions (`p323_control_i.json`):
  REST_print(throat) = (44/135, 4/27, 100/189); substitution delta
  (0, −16, 0); substituted throat ξ⁰ residual (0, 0, 0); gate P(ξ)
  ξ⁰ coefficient 203 → 187.
- **Exact R-jets validated.** `solve_Rjet_throat` re-implemented in
  exact Fractions for families A, C, D; max deviation vs the driver
  float solves 5.6×10⁻¹⁷ (bar 1×10⁻¹³). The A jet is
  [1, 0, 1/4, 0, −1/48, 0, 11/2880, 0, −73/80640, 0, 887/3628800].
- **C(ii) PASS.** Route (a) validated on Ellis backgrounds
  (`p323_validate.json`): Ellis throat exact — E2 programme mixed
  (−80, −16, −112), divergence exactly (0,0,0,0); Ellis ℓ=1 exact
  via the g0-patched engine — (47/8, 1/8, 55/8), divergence exactly
  0; float off-throat Ellis R = 1.5/2/3 bit-identical (dev 0.0) to
  Phase 318's stored `p318_ellis_e2_offthroat.json`.
- **Reassembly validations PASS** (`p323_reassembly.json`): the
  replicated Phase 259 mode-2 FULL totals match the stored
  `p2591_assembled.json` cells at every power on all 24 harness
  backgrounds, max deviation 1.53×10⁻¹² (0.0 on 22 backgrounds);
  stored-value checks — Ellis rest (44/135, 4/27, 100/189) dev
  1.2×10⁻¹⁵, Ellis H(3)/H(4) dev 0.0, A rest (−23/5040, 1/144,
  −199/5040) dev 3.5×10⁻¹⁷, A H(3)/H(4) dev 0.0.

## The full route-(a) evaluation (DF print units, exact unless noted)

    A throat   (9/4, 3/4, 21/4)
    C:1/2      (5645/4, 1375/4, 7705/4)
    C:1        (741/4, 207/4, 1011/4)
    C:2        (301/8, 23/2, 859/16)
    C:3        (17795/972, 625/108, 8935/324)
    C:5        (113953/12500, 7399/2500, 187607/12500)
    C:8        (94205/16384, 3875/2048, 338015/32768)
    D:3/20     (−49923/800000, −11997/640000, 2324709/6400000)
    D:3/10     (−42849/200000, −2277/40000, 117369/200000)
    D:9/20     (−583443/1600000, −51597/640000, 4959927/6400000)
    D:3/5      (−4563/12500, −117/2500, 13923/12500)
    D:3/4      (0, 99/1024, 3861/2048)
    D:9/10     (204363/200000, 16443/40000, 696087/200000)
    E:1/10     (1591, 110, 3005/4)
    E:1/5      (459/4, 45/4, 945/16)
    E:7/20     (−8049/686, 405/343, −540/343)
    E:1/2      (−21, 0, −27/4)
    A_fullr l=0.5 (float)  (0.1069762442, 1.0042155983, 1.3795942284)
    A_fullr l=1.0 (float)  (−0.8530798148, 0.6728413636, −0.8737847158)
    A_fullr l=2.0 (float)  (−0.1262089606, 0.0681158732, −0.1659377936)

Every exact point: divergence exactly (0,0,0,0), Ricci cross-check
deviation ≤ 2.2×10⁻¹⁶. Float points: divergence ≤ 2×10⁻¹⁵, Ricci
deviation 0.0. (Full values in `p323_eval_points.json`.)

## Fences

- The identification is in the registered form only: T_S of the
  DF/THA semiclassical record, identified against THA's targets on
  the harness cores (Ellis + A) and the Ellis gate, at all powers,
  under the fully arbitrated assembly of Phases 259/318/323.
- Phase 259's D1 stands: the ξ⁰ residual was not spanned by the
  exclusive monomial set under any candidate index reading — it was
  not a reading artefact; it was one print number, H{2,0}(3)'s
  throat T^r_r sector, now evaluated on both cores.
- The D2 generic-θ gap remains a gap. Nothing in this phase touches
  it.
- The THA Eq. (26) ξ³ bracket defect (Phase 241, confirmed by
  independent second path) stands; it is a separate sector and is
  not repaired by this identification.
- No wormhole construction, no traversability claim, and no FTL
  claim follows from this verdict. What closes here is the
  semiclassical identification datum — the W-ii (GJW mouth-coupling)
  port's blocker is removed; the port itself is a separate,
  uncharged piece of work.

## Incidents on the record

1. The first reassembly run was killed by a service restart during
   the E-family points. The script was made resumable with per-point
   checkpointing and rerun; every point was recomputed in the rerun
   and no unverified value was carried over.
2. The first reassembly compared replicated totals against stored
   *residuals*, producing spurious mode-2 deviations (~3.3×10⁴ at
   the Ellis throat). Found by direct comparison against the
   arbitration record (all per-tensor values dev 0.0); the corrected
   comparison gives max deviation 1.53×10⁻¹² over all 24
   backgrounds.
3. The route-(b) script's output path was mis-built (a nested path
   under `phase318/work/`), so its output file was absent on disk
   when the deliverables were assembled. The path was fixed and
   route (b) re-run; the re-run reproduces Phase 318's stored values
   bit-for-bit and Phase 318's file was never overwritten.
4. One bug in the exact-jet work was found and fixed on the record
   during the build (the C-branch jet subtraction); the validated
   jets above are post-fix.

## Artefacts

- `phase323/work/p323_registration.md` — registration, filed before
  computation.
- `phase323/work/p323_control_i.json` — Control C(i).
- `phase323/work/p323_exact_jets.json` — exact R-jets, families
  A/C/D, vs driver floats.
- `phase323/work/p323_validate.json` — Control C(ii), V1/V2/V3.
- `phase323/work/p323_e2_lib.py` — the route-(a) metric-jet builder.
- `phase323/work/p323_eval_points.json` — Read (1) + the full
  20-point evaluation.
- `phase323/work/p323_route_b.py`, `p323_route_b_out.json` —
  route (b), the independent second path.
- `phase323/work/p323_reassembly.json` — reassembly validations,
  Read (2) exact, Read (3) per-point table.
