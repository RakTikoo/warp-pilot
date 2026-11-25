# P141-1 — THE p2-FIELD ANATOMY

**Worker:** W-1. Implementation fixed in `work/p1411_runrecord.md`
before any deciding number was computed (one dated machinery
amendment appended in-item: the first S2 script's removal order
carried a code-side singular-value filter that excluded the
load-carrying component; the corrected order, over all components
as the record fixed, was run from the item's own stored assemblies
and is what is reported below). Checker: 25/25 PASS
(`results/p1411_checker.json`, script `work/p1411_checker.py`).

## VERDICT: LOAD IRREDUCIBLE IN THE REGISTERED BASIS

In plain language: Phase 133's second-order price is carried by
ONE piece of the particular field p2 — a single singular component
of the prolonged system, the one the system itself can barely see
(singular value 1.5×10⁻²¹, against the system's largest of
1.0×10⁻⁷). That one component is, to every measurable precision,
the whole of p2: deleting it would erase the entire price (the
shell datum Ŝ⁰⁰⁽²⁾ would go from −162.648 to −0.00000006 per unit
ε²). But deleting it is not allowed by the registered standard:
the prolonged equations would then be solved only to 1.0×10⁻¹⁹,
ten times worse than the 10⁻²⁰ residual bar this sweep was
registered under. Every other way of cutting the load by more
than the noise floor — removing any other component or set,
truncating the singular-value solve at any registered threshold,
or rebuilding the system one order higher at P = 4 — either
changes nothing or breaks the same residual bar. So the price
Phase 133 computed stands, and it is now known to be irreducible
in this basis at this residual standard: it is the cost of
answering one specific, tiny piece of the right-hand side
(1.23×10⁻¹⁹ of it) that only this barely-visible direction can
answer, at an amplification of 82.81 in the field and ~94 in the
join functionals.

One honest caveat, reported as a machinery discrepancy and not
averaged away: that barely-visible direction sits BELOW the level
at which the two programme engines agree on the assembled system
(their matrices differ by 2.4×10⁻²⁰ in norm, against the
direction's singular value of 1.5×10⁻²¹). The second engine's
assembly puts the same structural feature in a somewhat different
place (singular value 7.8×10⁻²¹, a smaller load share). What both
engines agree on is the deciding structure: exactly one such
direction carries essentially all of the load in each assembly,
and removing it breaks the residual bar in each assembly. Whether
the direction is a genuine feature of the exact prolonged system
or an artefact of float64 assembly is the first follow-up below;
it does not change this item's verdict, which is a statement
about the registered basis and its registered residual bar.

Phase 122's milestones are cited here only as scan signals under
attack (Gate-15 pending), at their registered scope (perturbative
through the entering orders of modes ℓ ≤ 3; D/r_Σ ∈ {10, 30, 100};
pre-existing configuration). Nothing here is a transport or FTL
claim; every transit read in the parent programme is EFFECTIVE
transit accounting (C12) — local light speed is never beaten
anywhere. **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## Anchors (both PASS, before any deciding read)

- **A1** — the in-item rebuild (bachgen assembly, Phase 133's
  stage-3 route, stencils recomputed in-item; no stored `.npy`
  loaded) reproduces the stored p2 chat vector and
  L_J[p2] = (−43.135816, +0.0190721, −33.237455, +77.109537) per
  unit ε² EXACTLY (difference 0.0), row residual max 6.44×10⁻²¹
  ≤ 10⁻²⁰, equal to the stored value. The recomputed B2 stencil
  matches Phase 133's stored stencil at all 7 radii.
- **A2** — the deciding chain from the stored components
  reproduces κ⁽²⁾ = 0.0, Ŝ⁰⁰⁽²⁾ = −162.64802149771168 per unit
  ε², amplitudes (−2714.4828262295855, +2.6094584913725335×10⁻⁵,
  −274.0041153566436), and the shell rows (−1.60619, −0.16043,
  +0.00402) — all exact, well inside the 5% bar.

## S1 — the spectrum and where the load sits

Full spectrum of the prolonged matrix M at P = 3 (12 singular
values, per unit ε² machinery throughout):

    1.040×10⁻⁷, 2.076×10⁻⁸, 5.182×10⁻⁹, 1.726×10⁻⁹, 4.366×10⁻¹⁰,
    3.109×10⁻¹¹, 3.235×10⁻¹², 8.068×10⁻¹³, 1.481×10⁻²¹,
    2.209×10⁻²², 4.319×10⁻²⁵, 5.390×10⁻²⁶

Eight values form the working ladder (down to 8.1×10⁻¹³); then a
gap of ~5×10⁸; then the tail. Decomposing p2 in the
right-singular basis, the L_J shares are:

| component | s_i | amplitude a_i | L_J share (norm) | L_J share vector |
|---|---|---|---|---|
| 0–7 (each) | 1.0×10⁻⁷ … 8.1×10⁻¹³ | ≤ 7.4×10⁻⁸ | ≤ 1.08×10⁻⁷ | — |
| **8** | **1.481×10⁻²¹** | **+82.806** | **94.400** | **(−43.135816, +0.0190721, −33.237455, +77.109537)** |
| 9–11, null (each) | ≤ 2.2×10⁻²² | ≤ 5.0×10⁻¹⁴ | ≤ 9.5×10⁻¹⁴ | — |

Component 8's share vector IS L_J[p2] (the shares sum to L_J[p2]
to ≤ 2.1×10⁻¹⁴). In chat/Taylor terms, v₈ is dominated by the
Bm Taylor coefficients at Σ — B₂ (−0.562), B₀ (−0.521), B₁
(−0.392) — and the A coefficients A₀ (−0.449), A₁ (+0.224); and
a₈v₈'s jet equals the stored p2 jet to ~10⁻⁹ relative. p2 is
this component.

Left-null content of the RHS: the part no p2 can answer is the
content along the left-singular directions i ≥ 9, norm
7.84×10⁻²¹ — exactly the row residual (norm 7.92×10⁻²¹, max
6.44×10⁻²¹). The i = 8 content, u₈·rhs = +1.2265×10⁻¹⁹, IS
answered by p2 — at amplitude a₈ = (u₈·rhs)/s₈ = +82.81. That
1.2265×10⁻¹⁹ is the exact residual cost of removing the
component.

## S2 — removal tests: the breaking point

Components removed in descending |L_J share| order (component 8
first), one at a time and as joint prefixes, the remaining
freedom re-solved by the same min-norm rule:

- Removing component 8 alone: |L_J| falls by 94.40 (≫ floor_J2 =
  3.241), Ŝ⁰⁰⁽²⁾ goes −162.648 → −6.3×10⁻⁸ — but the row
  residual rises 6.44×10⁻²¹ → **1.001×10⁻¹⁹ > 10⁻²⁰ bar**.
  NOT removable.
- Every other single removal changes |L_J| by ≤ 1.1×10⁻⁷ (below
  floor) — nothing to gain.
- No joint prefix meets the bar (the first prefix already breaks
  the residual bar; later prefixes only worsen it).

## S3 — regularisation sweep: the re-read trigger is not met

- P = 3, SVD truncation at relative thresholds {10⁻⁶, 10⁻⁸,
  10⁻¹⁰, 10⁻¹²} (all four give the same kept set — the spectrum's
  gap): L_J[p2] → ~10⁻⁷ (load gone), Ŝ⁰⁰⁽²⁾ → −6.3×10⁻⁸, but
  row residual 1.00×10⁻¹⁹ > 10⁻²⁰.
- P = 4 untruncated: L_J[p2] = (−4.068, +0.00160, −7.355,
  +7.104), Ŝ⁰⁰⁽²⁾ = −5.553, amplitudes (+304.80, +2.19×10⁻⁶,
  −15.39), shell rows (−0.03524, +0.01412, +0.01973) — a
  completely different price, and its load again sits in one
  near-null tail component (i = 10, s = 1.916×10⁻¹⁹, share 11.01
  of |L_J| = 11.01). But its row residual is 9.56×10⁻²⁰ >
  10⁻²⁰.
- P = 4 truncations (all thresholds): L_J → ~10⁻⁷, residual
  8.61×10⁻¹⁹ > 10⁻²⁰.

The registered PRICE RE-READ trigger requires the load to move
by more than floor_J2 WHILE the row residuals stay ≤ 10⁻²⁰. At
every swept setting that moves the load, the residual breaks
the bar. The trigger is met nowhere; no price is re-read, and
the swept values above are recorded, not adopted.

κ⁽²⁾ under every arm: audited over all settings (removals,
prefixes, truncations, P = 4, second path) — max |κ⁽²⁾| =
4.4×10⁻¹⁶, i.e. κ⁽²⁾ = 0 everywhere, as registered (invariance
under p2 shifts). No machinery alarm on κ⁽²⁾.

## Second path (bachfloat assembly; engines' roles exchanged)

- Agreement: the working spectrum s₀…s₇ agrees with the primary
  to ≤ 1.6×10⁻¹¹ relative; the B2 stencil agrees at all 7 radii;
  the bachfloat solve also satisfies its system (residual
  1.26×10⁻²¹) with κ⁽²⁾ = 0; in the bachfloat assembly, too,
  exactly one near-null component (its i = 8) carries ~100% of
  its load (share 4.521 of |L_J| = 4.521; all others ≤ 1.1×10⁻⁷),
  and removing it breaks the residual bar (1.32×10⁻²⁰ > 10⁻²⁰).
  The removal DECISION — the registered deciding feature —
  agrees on both paths.
- Discrepancy (reported, not averaged): s₈ = 7.80×10⁻²¹
  (bachfloat) vs 1.48×10⁻²¹ (bachgen), a factor 5.3; the
  component's L_J share 4.52 vs 94.40; total L_J[p2] =
  (−1.577, +0.00049, −3.286, +2.674) and Ŝ⁰⁰⁽²⁾ = −1.275 on the
  bachfloat assembly; |v₈(primary) · v₈(second)| = 0.553. The
  two assemblies' matrices differ by ||ΔM||_F = 2.40×10⁻²⁰ —
  larger than s₈ itself — so at float64 finite-difference
  precision the deciding direction's exact content is
  assembly-dependent. The irreducibility verdict above is a
  statement about the registered (bachgen) basis at its
  registered bar; the discrepancy is the anatomy of why the
  direction is delicate, and it is exactly what follow-up F1
  is aimed at.

## Follow-up experiments (failure protocol; aimed at the mechanism)

1. **F1** — assemble M at 40-digit mpmath precision and recompute
   s₈ and v₈: decides whether the load-carrying direction at
   s ~ 1.5×10⁻²¹ is a genuine feature of the exact prolonged
   system or a float64 assembly artefact (the two float engines
   already disagree on it by a factor 5.3, and it lies below
   their mutual difference).
2. **F2** — P141-2 (already registered): the radial-ODE
   construction of h₂ reads the join load from a profile with no
   jet algebra — the basis-independent counterpart of this
   item's question.
3. **F3** (for the coordinator) — any future removal sweep on
   this system needs its residual bar set against the assembly's
   own reproducibility scale (here the inter-engine ||ΔM||),
   since the registered 10⁻²⁰ bar sits below that scale for the
   deciding direction. This item applied the bar as registered
   and does not re-set it.

## Scope

The registered basis only: chat coordinates, P = 3 primary with
P = 4 as the swept extension, min-norm rule, bachgen assembly as
primary. A removal verdict is a statement about p2's
representation of the second-order field IN THIS BASIS;
whether the field itself (basis-independently) carries the load
is P141-2's question, not this item's. ℓ = 0 only; second order
in amplitude only. Formation standing: PRE-EXISTING ONLY.
INTERNAL only; nothing uploaded; nobody contacted.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
