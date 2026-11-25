# Warp Pilot — an open, verified search for positive-energy warp metrics

An independent computational search for warp-drive spacetimes whose matter
satisfies the classical energy conditions (NEC, WEC, SEC, DEC) for **all
observers**, audited with a purpose-built verifier, adversarial red-teaming,
and three independent computation paths. Everything here is reproducible
from the code and frozen configurations in this repository.

**We are publishing this to ask for independent verification.** If you can
re-run an audit, break a result, or extend a search, please see the
[help-wanted issues](../../issues) — several are scoped as good first
issues (run a script, compare numbers, report).

## What's new here

Everything below passed this project's verification gate — an independent recomputation on a second code path plus a literature novelty check — before it was published. Archived releases are on Zenodo (all versions: https://doi.org/10.5281/zenodo.24425078).

- **v1.21.0 — Gate-21 claims.** Two gated results from Phase 186 (`gate21-claims/`): **(G21-1, survived in restated wording)** the flipped pose's enriched-instrument gate read HOLDS at finite λ = 0.10 — closure 0.6233418793559693 ≤ the 0.63 cap, Type-I [False, False], count 52 — with the fence as part of the claim: the witness is coefficient-large and near-null-carried (‖d‖₂ = 4.407427, 99.976% of ‖d‖² below σ_cut) and the pass is an exact-reads pass via the registered fallback route. **(G21-2, survived intact)** at λ = 0.1452 the read FAILS under the registered count-preserving discipline; onset bracket (0.10, 0.12], tightened by the gate's probes to (0.10, 0.11]. Both SPECULATIVE and instrument-scoped. DOI: 10.5281/zenodo.24525077.
- **v1.20.0 — Gate-20 claim.** One gated result from Phase 178 (`gate20-claims/`): **(G20-1, survived intact)** P178-1 (SPECULATIVE): the flipped pose's recovery gate PASSES in the enriched diagonal instrument (E-a: {1, P₂, P₄} × 8 knots) — a single exhibited field reads coupled closure 0.6232117059867903 ≤ the registered 0.63 cap, Δq inside the 5×10⁻⁴ tolerance, Type-I [False, False], subset count 52. Instrument scope only — not an untruncated-pose verdict; the finite-λ question is NOT decided by this claim. DOI: 10.5281/zenodo.24524702.
- **v1.19.0 — Gate-15 claim.** One gated result from Phase 122 (`gate15-claims/`): **(G15-1, survived in restated wording)** the two-mouth RE-MATCH CLOSES in the full linearised Bach system — a posed two-mouth configuration exists: the complete condition set ([B], [K], [R̃], [R̃_,n] + the angular Darmois pair per mode, round Σ, modes ℓ ≤ 3, ε ∈ {0.1, 1/30, 0.01, 0.003, 0.001}) is satisfied in the full homogeneous solution space — settled dimensions ℓ=0: 7, ℓ=1: 10 (four of them a verified pure-gauge family; (e) quotient 6), ℓ=2: 8, ℓ=3: 8 (response rank 6, full, at every mode) — with residuals ≤ 1.2×10⁻¹⁷ per unit ε^entering (bar 10⁻⁵) and amplitudes ≤ 2.2×10⁻² (bar 10²); the joining shells are legal at BOTH mouths (shell sign minimum Ŝ⁰⁰/α₀ = +0.0202914453 at both; +0.0202882 after the corrected ℓ≥4 tail bound 2.459×10⁻⁶, ε = 0.1 row). **Qualifications, inseparable:** restricted to the (e)-quotient representatives alone, the residuals still close (≤ 5.7×10⁻¹³) but at ℓ=1 the representative amplitudes reach 6.949×10³, above the 10² bar — the small-amplitude closing representative uses the full space, gauge directions included (physically inert). The gate corrected the claim's dimension clause, its [R̃]₂ coefficient (−1.213920×10⁻⁴ → −2.260117×10⁻⁴) and its uniform amplitude bound. **Scope fences, inseparable:** linearised pose (channels above ε⁴ and O(ε²) nonlinear terms unposed); formation PRE-EXISTING ONLY; (V-b) UNDECIDED (Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE); chronology protection POSTURE ONLY; the second-order standing beyond ℓ=0 is not gate-judged. **Novelty: PARTIALLY KNOWN** — the exact pose was not found in the gate's search (limits: web-index only, INSPIRE-HEP/Semantic Scholar via web indexes not direct sessions, no exhaustive arXiv sweep, English only) and every ingredient is published; no unique/first wording. Phase 122's second claim (G15-2, the measured shortcut) is not part of this release; it received its verdict at the completed gate (survived in restated wording, with the corrected boosted tide at β = 0.9 of 1.65–1.75×10⁻⁶ s⁻²) and is recorded in the public ledger. The claim is stated only in Gate-15's restated wording. DOI: 10.5281/zenodo.24523644.
- **v1.17.0 — Gate-10 claims. Two gated results from Phase 80 (`gate10-claims/`), both upload-ready after restatement in Gate-10’s wordings only: **(G10-1, correctness reproduced)** payload transport — a nested (composed) warp configuration, an inner shell and an outer shell, each shell’s shift derived by integration from an optimised Procaccia-form source, composed under the Phase-46 protocol with both shells’ orthonormal shifts held at their alone values by lapse re-equilibration, carries a held payload of **0.08745c** at full legality (Hawking–Ellis Type-I at every significant point of the full-volume audit over both shells, the cavity, the payload region and the exterior; worst margins: payload +3.85×10⁻⁶, inner wall +1.188×10⁻³, outer wall +3.20×10⁻⁵, exterior +1.04×10⁻⁶; sampled-null NEC positive everywhere; a second composed row at 0.08104c corroborates). This row **supersedes the Gate-8-verified 0.0799c as the payload transport category’s gate-verified best**; no comparison with any bare-shell result is made or implied. **Cavity caveat, in its settled form:** the primary finite-difference auditor’s raw cavity DEC read on this row is −1.107×10⁻⁴ at r ≈ 4.53; an independent symbolic radial-reduction audit with analytic derivatives (Gate-10) reads that site cleanly positive (DEC +2.02×10⁻⁴ at r = 4.53), reads the control row’s cavity site at floor level with no convergent negative continuum value, and finds the only residual negative reads on either row at floor level (|DEC| ≲ 5×10⁻⁷ near r ≈ 4.87), sign-unstable under refinement — the flagged read is a finite-difference representation artefact, settled on three different-in-kind machineries. Accounting (C12): a prescribed-geometry audit of a subluminal, pre-arranged configuration; construction-inclusive arrival is ≥ D/c; no transport claim beyond the payload’s own speed; no matter model, formation route or stability claimed; Le’s source-consistency standard (arXiv:2605.25417) stands as a caveat. **(G10-2, confirmed at our bars)** an independent confirmation of Le’s multipole (Darmois) shell, arXiv:2606.22531 v3 — a subluminal accelerating shell of Bobrick–Martire class; no superluminal claim is made or implied: on a fresh reconstruction from the published record, audited on a pole-inclusive grid with both poles evaluated exactly (θ = 0 and θ = π as computed points, the π−0.15…π band covered), the shell is Type-I at every grid point at (x, λ) = (0.1, 0.19), (0.2, 0.20) and (0.3, 0.19), with worst-observer DEC margins +1.728×10⁻³ (binding at the rear pole θ = π), +5.139×10⁻³ and +9.102×10⁻³ (both binding at the front pole θ = 0) at L = 6, L = 4 agreeing in sign and value at every pin, and closure max|[h]| = 1.40×10⁻⁷ at x = 0.1 (the paper prints 1.4×10⁻⁷; the paper prints margins 1.8×10⁻³ at x = 0.1 and 9.1×10⁻³ at x = 0.3 and no margin at x = 0.2, where our value confirms Phase 80’s audit). As recorded by Phase 80 from the published code, the author’s own multipole stress grid stops at π−0.12, so the author’s binding-at-the-pole statement was not pole-evaluated by the author; this confirmation’s pole reads are pole-exact. **Open clause: the x ∈ {0.5, 0.7} pins are untested (our solvers’ gap), not impeached; the paper’s margins there (18, 21×10⁻³) stand untested.** Succession note: the payload chain’s current gate-verified best is 0.09758c (Gate-13, v1.14.0), via 0.09556c (Gate-11); the 0.08745c row above is stated at its place in that chain, in Gate-10’s wording. The claims are stated only in Gate-10’s restated wordings. DOI: 10.5281/zenodo.24522763
- **v1.16.0 — Gate-16 claim, as corrected by Gate-19.** One gated result from Phase 128 (`gate16-claims/`), on the registered superluminal front (Phase 48 bed at β = 1.1, 56-point subset, hinge theory): **(G16-1, survives in restated wording)** the first joint legality + solution-grade improvement on the front, by composing Phase 119’s two escapes — a non-flat profile blend AND the exact constraint H,_φ(π₀) = 0 — Pareto-dominating the hinge best: subset legality 0.75 → 0.8928571428571429 (both margin forms; the hinge’s 0.75 and the candidate’s 0.8928571428571429 are Gate-19’s corrected re-reads — the legality figures in Gate-16’s original record were computed with a fluid stress-energy function later proved to transpose its tensor, and are superseded), worst-point relative EoM residual 0.9999999999784565 → 0.999981215379503 (a 1.9×10⁻⁵ move); the median EoM residual WORSENED (0.22437629566157347 → 0.47963896879690177) and health fails (on the cr2 clause); the alignment set is empty and the pin re-forms one point out, at point 44, carried by t_FB (share 0.882). **Fence, inseparable:** Frontier A = 0 — an improvement, not a pass; no legal superluminal configuration is claimed. Accounting (C12): a pre-existing wall at β = 1.1 inside one designer scalar+fluid theory; a moved front is not a legal wall, and nothing here implies transport or anything faster than light in the world. The claim is stated only in its Gate-19-restated wording (in `gate16-claims/RESULTS.md`). (A second Gate-16 claim, G16-2, was withdrawn before publication: under Gate-19’s corrected re-reads its legality coordinate reversed against the corrected hinge, 0.6071428571428571 < 0.75, so it fails as a joint improvement; its surviving anatomy is in the phase record, not in this release.) DOI: 10.5281/zenodo.24522116.
- **v1.15.0 — Gate-14 claim.** One gated result from Phases 108/119 (`gate14-claims/`): **(G14-1, survived intact)** multipartite QET delivers net negative energy against its uncorrelated reference, with the entanglement resource fully counted — in the N-qubit quantum-energy-teleportation model of Xun & Ren (arXiv:2410.04919; the model is theirs, the accounting result is ours), the receiving sector’s net delivered energy E_net,B = E_prep^(marg) − E_out is negative at eight (N, m, k/h) rows, first at (5,1,0.5), and the Ford–Roman ratio R exceeds 1 at the five deciding rows under the τ_marg convention (3.196, 4.681, 11.054, 5.195, 14.337) and under τ₀ as well, with (10,1,2) standing under τ₀ alone at 5.134 and no τ_marg return for t ≤ 30 — the claim is not convention-dependent at the deciding rows. **Price caveat, inseparable:** against the cheapest uncorrelated preparation (the separable minimum E_prep^(sep) = 4k²/(D + N)) the total price is 5.34–28.17 per unit delivered at the deciding rows, classical leg omitted, so the figure is a lower bound — this is NOT an energy source: every unit delivered costs between 5.34 and 28.17 units of preparation and injection. **Scope:** a finite spin model under a pulse construction; not a field-theory claim — no multipartite field/oscillator QET exists in published form (Phase 119-2), and the 1/N dilution behind the effect is a property of this model’s single shared interaction. Accounting (C12): a sourcing-accounting result in a finite model; it implies no device, no transport, and nothing faster than light. The claim is stated only in Gate-14’s upload wording. DOI: 10.5281/zenodo.24521594.
- **v1.14.0 — Gate-13 claim.** One gated result from Phase 116 (`gate13-claims/`): **(G13-1, survived intact)** the payload transport category’s new gate-verified best — a nested (composed) warp configuration carrying a held payload of 0.09758c at full legality, **superseding Gate-11’s 0.09556c as the payload transport category’s gate-verified best** (Phase 80’s 0.08745c row remains phase-verified under Gate-10; its outcome is not cited); no comparison with any bare-shell result is made or implied. The mechanism: raising the outer shell’s alone β from 0.07 to 0.0725 inside its span-narrowed legal window (alone ceiling bracketed to (0.0725, 0.075) at span ±0.10W) raises the composition’s held payload from 0.09556c to 0.09758c. Cavity, in its settled form: the flagged finite-difference read is a representation artefact, settled on different-in-kind machineries — the Gate-13 analytic path reads the flagged site cleanly positive, and the only residual negative reads are at floor level (|DEC| ≲ 3.0×10⁻⁶ near r ≈ 4.87), sign-unstable under refinement, with the row’s legality resting on the re-derived settlement, not on any floor-class bound. Accounting (C12): this is a prescribed-geometry audit of a subluminal, pre-arranged configuration; construction-inclusive arrival is ≥ D/c; no transport claim beyond the payload’s own speed is made; no matter model, formation route or stability is claimed. The source-consistency standard of Le (arXiv:2605.25417) stands as a caveat on this result: the audit certifies the geometry’s required source against the classical energy conditions and does not supply a source-first matter model. The claim is stated only in Gate-13’s upload wording. DOI: 10.5281/zenodo.24521116.
- **v1.13.0 — Gate-12 claims.** Two gated results from Phase 96 (`gate12-claims/`): **(G12-1, survived intact)** Le's multipole accelerating shell (arXiv:2606.22531) confirmed at this programme's bars at the (0.7, 0.09) pin — closure 1.989087×10⁻³ against the 2.0×10⁻³ bar, Type-I everywhere, worst DEC margin +1.345981×10⁻² — our independent confirmation at our bars, not a priority claim over the author; the (0.5, 0.14) pin remains STILL UNCLOSEABLE, its obstruction named in the claim. **(G12-2, restated)** the P61-1 shell endowed with the Brown–Gladush surface perfect-fluid action — a NEW labelled object, NOT the conformal member — has an ℓ = 0 fixed-bulk spectrum: stable at the action's linear EoS (ω² = +6.384×10⁻¹⁰ r₀⁻² in shell proper time; Gate-12 restated Phase 96's values, which were squared coordinate-time frequencies) and unstable if pressureless, threshold β² = 0.0020611430310; the member's own shell sector remains UNPOSABLE in pure Weyl gravity, and (V-b) UNDECIDED rides with any mention of the member. Both claims stated only in their gate wordings. DOI: 10.5281/zenodo.24520713.
- - **v1.12.0 - Gate-11 claim.** One gated result (`gate11-claims/`), stated only in its gate wording: the nested (composed) payload configuration of Phase 88 — inner and outer shells, each shell’s shift derived by integration from an optimised Procaccia-form source, the outer shell’s source-spline span narrowed to ±0.10W — carries a held payload at 0.09556c at full legality (Hawking–Ellis Type-I at every significant point of the full-volume audit; the cavity caveat settled in its stronger form on an independent symbolic path; both of the phase’s open disclosures closed on their merits). Gate-11’s verdict: SURVIVED INTACT; novelty graded NOVEL in the documented search (limits stated in the bundle). This row supersedes G8-1’s 0.0799c (v1.10.0) as the payload transport category’s gate-verified best; no comparison with any bare-shell result is made or implied. DOI: 10.5281/zenodo.24457976.
- **v1.11.0 - Gate-9 claims.** Four gated results (`gate9-claims/`), each stated only in its gate-restated wording, all concerning ONE throat object in conformal (Weyl) gravity — the joining member (b = r0(r/r0)^0.1, Phi2 profile, a = 0.277734): whole-domain energy-condition legality to 10^3 r0 on an independent symbolic path; the exact join to a Mannheim–Kazanas exterior at 10^3 r0 with a legal shell (the same interior joins at no smaller radius); classical stability in the computable interior sectors; and formation PRE-EXISTING ONLY (grown-shell price unbounded, nucleation closed). No transport and no traversability is claimed; the theory's ghost question rides as (V-b) UNDECIDED in every claim. DOI: 10.5281/zenodo.24453655
- **v1.10.0 - Gate-7 and Gate-8 claims.** Five gated results (`gate7-claims/`, `gate8-claims/`), each stated only in its gate-restated wording: the (10,30) thick shell verified at beta = 0.10 in two configurations (halved smoothing - with a thin DEC-negative layer just inside its inner edge named in the claim’s scope - and a spline shift profile at full smoothing); an independent confirmation, at this programme’s bars, of Procaccia’s beta = 0.1363 shell design (his design, our audit; the standing verified mark in the single-shell category remains his 0.1363); the Gate-8 composed payload - nested shells carrying a payload at 0.0799c (payload transport category; the claim’s one caveat is a discretisation-floor DEC read in the cavity near-edge shell 4.6 < r < 5, sign-unstable at |DEC| ≲ 2.3×10⁻⁴ under refinement in the amended wording, with no convergent negative continuum value); and the attained form of the exhibited throat’s bulk shortcut - a Z2 mirror completion at y_c = 0.30 r0 makes the gain 0.167 an attained, everywhere-regular geodesic (the v1.9.0 figure 0.480 remains an unattained infimum; EFFECTIVE ONLY, pre-existing structure, no formation route). DOI: 10.5281/zenodo.24452706
- **v1.9.0 — Gate-6 claims.** Four gated results (`gate6-claims/`): the (10,30) thick shell verified at β = 0.07 **and β = 0.08** (Gate-6 found the 0.07 "ceiling" was a single-point instrument artefact; β = 0.09 unsettled); the Φ ≠ 0 inertness theorem for scalar-tensor throats; a measured bulk-shortcut gain (0.480) inside an exhibited wormhole-throat bulk lift — effective only, setup leg unavailable; and the component-blindness of the quantum-inequality sampling bound, with the species escape priced at N ≥ 1.06×10⁷². All four stated only in their gate-restated wordings. DOI: 10.5281/zenodo.24439601
- **A warp shell that beats the published benchmark, with the maths checked twice** — verified subluminal shells 40% lighter (Finalist A, β = 0.02) and 50% faster (Finalist B2) than the Fuchs et al. baseline, passing all energy conditions. [Release v1.0.0](https://doi.org/10.5281/zenodo.24425079)
- **A hard floor under every wormhole** — exact formulas for the minimum amount of "exoticity" any throat of a given size must have, whatever it is made of (the H6 floor identities). [Release v1.1.0](https://doi.org/10.5281/zenodo.24425833)
- **Warp shells inside curved spacetime, not just empty space** — shells re-solved in Schwarzschild and anti-de Sitter backgrounds; they work until a named pressure-amplification mechanism kills them at high background mass (H4). [Release v1.1.0](https://doi.org/10.5281/zenodo.24425833)
- **A published "stable wormhole" that isn't** — the Mironov–Rubakov–Volkova beyond-Horndeski wormhole of arXiv:1811.05832 carries a hidden instability (an even-parity ghost), certified directly from its action; two misprints in the paper, repeated in its sequel, documented along the way. [Release v1.7.0](https://doi.org/10.5281/zenodo.24434411) (audit trail: [v1.6.0](https://doi.org/10.5281/zenodo.24433260))
- **How to build a warp shell without breaking the rules on the way** — formation paths that stay legal at every instant exist (grow the wall and the shift together); the obvious "shift first" route is impossible already at β = 0.01. [Release v1.8.0](https://doi.org/10.5281/zenodo.24435291)
- **In one torsion-based gravity, a legal wormhole *is* an unstable one** — on the f(T) T ≡ 0 background, matter legality and a tensor ghost are the same sign choice (the ghost identity, restated scope). [Release v1.8.0](https://doi.org/10.5281/zenodo.24435291)
- **Why a leading alternative-gravity wormhole can't be certified, plus an unflagged misprint** — the EiBI throat obstructions (a forced sound speed of −1, a degenerating auxiliary metric), and the Böhmer–Harko–Lobo Eq. (29) misprint, no published erratum found on arXiv, the publisher's page, or INSPIRE (re-checked Nov 2026). [Release v1.8.0](https://doi.org/10.5281/zenodo.24435291)
- **The traversable-wormhole loophole, priced in plain numbers** — the Gao–Jafferis–Wall bounds evaluated at human scales: the open-time window falls 73.8 orders of magnitude short, the mass capacity 45.3 orders short. [Release v1.8.0](https://doi.org/10.5281/zenodo.24435291)
- **Quantum corrections that cancel exactly** — in asymptotic-safety gravity, the running-coupling corrections at a wormhole throat cancel identically (an analytic identity, not a numerical coincidence); three errors in the source paper documented. [Release v1.8.0](https://doi.org/10.5281/zenodo.24435291)
- **Hiding the exoticity in a second metric doesn't work — measured** — in bimetric gravity the violation relocates into the second sector, which then breaks the null energy condition on 70–100% of the volume in every configuration tried. [Release v1.8.0](https://doi.org/10.5281/zenodo.24435291)
- **A screen that hides a warp drive from gravity tests — and what it costs** — an environment-dependent coupling construction that switches off outside the shell, with its energy-budget laws; plus a "breathing" shell that stays legal while it pulses, and the exact law for how long a negative-energy pulse may last. [Release v1.5.0](https://doi.org/10.5281/zenodo.24432779)

## Headline results (all numbers in `REPORT.md` and `CHECKPOINT.md`)

- **Two novel subluminal warp shells, verified.** Shell geometries outside
  the Natário class (non-unit lapse, non-flat spatial slices) that pass all
  energy conditions for all observers, confirmed by a finite-difference
  auditor, an independent autodiff code (warpax), and a symbolic SymPy
  derivation, plus an adversarial optimiser that tried and failed to find
  a violating point:
  - *Finalist A* — β = 0.02c, ADM mass 2.69×10²⁷ kg, **40% below** the
    Fuchs et al. (2024) baseline mass at the same radius and velocity.
  - *Finalist B2* — β = 0.03c, 3.64×10²⁷ kg, **19% below** that baseline
    at 50% higher velocity.
  - A β = 0.05c frontier design of the Phase-1 family at compactness
    M/R₁ = 0.383 (lightest: 2.58×10²⁷ kg), with a fitted scale-covariance
    law for the frontier.
- EC-legal subluminal shells are known (Fuchs et al. 2024); this programme's
  verified rows include Finalist A (β = 0.02) and the Phase-26 (10,30)
  configuration at β = 0.07–0.08 (Gate-6). In the Phase-1 family, the
  positive-energy frontier terminates between β = 0.05 and β = 0.1: at
  β = 0.1, three independent constructions (named families, free-form machine
  search, and a conditions-first reverse construction) all land within ~10⁻⁸
  of zero worst-margin and none certifies a pass. The boundary is a wall:
  different energy conditions bind on its two sides.
- **No superluminal candidate anywhere.** A per-geometry exclusion map
  (16 rows in `REPORT.md`) covers spherical shells, toroidal shells
  (symmetric and asymmetric), free-form and fully-3D shapes, shells on
  Schwarzschild/(A)dS backgrounds, shells in expanding (FLRW/de Sitter)
  backgrounds, and modified-gravity / exotic-source lenses — f(R), f(Q),
  Kaluza–Klein lifts, Einstein–Cartan torsion, non-minimal scalars,
  Casimir threading, and multi-component sources (the last closed by a
  linearity proof, not by search).

## The shape of Finalist A

![Finalist A cross-section and profiles](finalist_A_shape.png)

*Finalist A, computed from the frozen configuration in `results/frozen/finalist_A.json` with the repository's own `shell.py` (plot script: `plot_finalist_A.py`). Left: matter density in a cross-section through the centre — an empty cavity (r < 10) inside a spherical wall (10–20) whose density peaks at its two edges; the whole configuration moves at β = 0.02. Right: the density profile and the shift (velocity) profile — the interior rides at the full β and the shift falls to zero across the wall, so the transition lives entirely inside the matter. This is a constant-velocity configuration; formation and stability are not claimed (see Limits).*

### Finalist B2, and the frontier

![Finalist B2 cross-section and profiles](finalist_B2_shape.png)

*Finalist B2 (β = 0.03, 3.64×10²⁷ kg), computed from `results/frozen/finalist_B2.json` with `shell.py` (plot script: `plot_finalist_B2_shape.py`). Same edge-peaked wall design as Finalist A, at 50% higher velocity.*

![The positive-energy frontier](frontier.png)

*The mass–velocity frontier (plot script: `plot_frontier.py`). In the Phase-1 family, verified positive-energy designs exist at β = 0.02, 0.03 and 0.05 along a compactness curve; at β = 0.1 three independent constructions land within ~10⁻⁸ of zero worst-margin and none certifies a pass — the Phase-1 family's frontier terminates between β = 0.05 and β = 0.1.*

## Limits — read these before citing anything

- The verified shells are **constant-velocity** configurations. Formation,
  acceleration, and stability are **not** solved; a quasi-static snapshot
  sequence is included and labelled necessary-not-sufficient.
- Margins are numerical (~10⁻⁵–10⁻⁷), established by finite sampling of
  points and observers — strong evidence, **not a proof**.
- Matter is characterised only through the energy conditions; no specific
  physical matter model is proposed.
- No outside expert has re-run these results yet. That is the point of
  this repository.

## Phase 5 claims (gate-verified)

Three results from the later, origination phase of the programme, published after passing a novelty-and-verification gate (documented literature search for prior art + independent reimplementation of the deciding computations). Full write-ups, wording conditions and limits: [`phase5-claims/CLAIMS.md`](phase5-claims/CLAIMS.md); how each was gated: [`phase5-claims/GATE_SUMMARY.md`](phase5-claims/GATE_SUMMARY.md).

- **Wormhole exoticity floor identities** — the volume integral of ρ + p_r for zero-tidal wormholes decomposes exactly, and the proper-volume floor (−r₀) is twice the coordinate floor. Stated with a tightened hypothesis set; zero-tidal (Φ = 0) scope only.
- **Warp shells re-solved inside curved backgrounds** — a positive-energy shell re-equilibrated in Schwarzschild gravity passes the full audit at background masses 1 and 2 (an earlier superposition-based failure was an artefact of the method), fails at mass 4 by a named mechanism, and passes in AdS. Static configurations; the moving case fails in the cavity, by a named mechanism.
- **A decoupling criterion for gravity-sector exoticity (restated)** — when a modified-gravity term can supply an energy-condition violation while remaining healthy: strict for five audited theory cases, by structural analogy for two more, with the underlying mechanism credited to Mironov–Rubakov–Volkova. It also explains why throats admit this decoupling and warp walls resist it, and predicts that only a rank-≥2 correction could align on a wall — a prediction since tested in Phase 6, where it was refined (necessary, not sufficient).

## Learnings

[LEARNINGS.md](LEARNINGS.md) is the programme’s living methods record: the artefacts we now catalogue, the self-corrections (including an internal result retracted over a units error, and a scan signal killed by our own red team before it was ever published), and the standing rules each episode produced. It contains no discovery claims — it exists so others running searches like this can avoid our mistakes.

## Phase 8–9 claims (gate-verified)

Three further results have passed the same novelty + verification gate (independent literature search and independent re-computation), in the folder [`phase89-claims/`](phase89-claims/CLAIMS2.md):

- **A warp shell that moves legally through a curved background.** Re-solved in the total geometry around a Schwarzschild mass and set moving at β = 0.02, it passes the full energy-condition audit in the areal embedding at both distances tested (the result is embedding-dependent: in the total-lapse-consistent PG embedding it passes at the larger distance and fails at the closer one — both outcomes are part of the claim).
- **A speed-asymmetric wall supply in Einstein-aether theory.** The first non-scalar-tensor correction tested on a warp wall supplies nothing at β = 0.1 (best partial coverage 0.000) but reaches health-passing partial coverage 0.813 at β = 1.1 — starved subluminally, fed superluminally. Full coverage never reaches alignment, and every scanned row is excluded by solar-system PPN data (0 of 327 pass). The claim is the asymmetry and the exclusion together, not a drive.
- **The first realised toroidal shell of the conditions-first programme** (in the delimited sense stated in the claims file): the γ-extended meridional system solves to residual RMS 1.89×10⁻⁴, with the obstruction's branch boundary bracketed at (0.6–0.7)× the original density×size². Its motion audit at β = 0.02 is negative (converged −1.51×10⁻⁴) and is reported as part of the claim.

Two of the three are published in gate-restated form: the gate's second path disproved the original explanation of the aether exclusion mechanism (the exclusion itself reproduced exactly), and the torus motion headline was replaced by its converged value. The corrections and the errata appended to the internal records are documented in `phase89-claims/GATE2_SUMMARY.md`. No superluminal result is claimed anywhere in this release series.

## Phase 15–16 claims (gate-verified)

A third claims pack, in `phase1516-claims/`: a breathing warp shell audited legal at every instant of its cycle (with the motion tax measured), an exact transient quantum-inequality pulse law (scaling credited to Pfenning & Ford 1997), and a verified screening construction for Einstein-aether — published with its family closure on its face: screened aether is closed as a superluminal supply route. Each claim passed the programme's novelty + verification gate (Gate-4), two of them in gate-restated form. No superluminal result is claimed anywhere in this pack.

Archived release: https://doi.org/10.5281/zenodo.24432779

## Audit note (gate-verified)

An independent audit of a published beyond-Horndeski wormhole (Mironov–Rubakov–Volkova 2019), in `mrv-audit/`: what the audit verified (the background is a genuine solution; the radial and odd sectors are healthy), two certified defects in the paper’s printed stability formulas, and the construction's trajectory incompleteness — with the audit's own transcription error disclosed in the same place. The even-sector ghost question is under certification and is not claimed here.

Archived release: https://doi.org/10.5281/zenodo.24433260
Update (v1.7.0): the even-sector ghost claim is certified branch-independently at the action level and stated in full in mrv-audit/AUDIT.md §6; the l=0 soft-mode value reported in v1.6.x is retracted as a discretisation artefact (§2).
Archived release: https://doi.org/10.5281/zenodo.24434411

## Phase 17–23 results (gate-verified)

Gate-5 re-verified the programme's nine ungated results from Phases 17–23 by independent recomputation and literature novelty check: six stand in restated form (an f(T) ghost identity, EiBI throat obstructions and a literature misprint, the evaluated GJW ledger, an asymptotic-safety cancellation identity, legal formation paths, and a bimetric relocation anatomy), and three are labelled independent confirmations of published results. See phase1723-claims/RESULTS.md.

Archived release: https://doi.org/10.5281/zenodo.24435291

## Repository layout

- `REPORT.md` — the final internal report: plain-language summary,
  technical record, verification appendix, superluminal exclusion map.
- `CHECKPOINT.md` — the full ground record: every run, failure anatomy,
  fitted pattern, data binding (Planck, GW170817, Eöt-Wash, ATLAS values
  used as gates), and the exhaustion ledger.
- `verify_metric.py`, `metrics.py`, `shell.py` — the auditor (Einstein
  tensor by finite differences, Hawking–Ellis classification, all-observer
  margins).
- `results/frozen/` — the three verified configurations (A, B2, β=0.05
  frontier winner) exactly as audited.
- `results/` — JSON/log output of every run cited in the report.
- Track scripts: `trackL.py` (frontier), `trackP*.py` (free-form search),
  `mg1_*.py` / `mg2_*.py` (modified gravity), `x1_*.py`–`x5_*.py`
  (geometry/source lenses), `n1_*.py`–`n4_*.py` (new-physics tracks),
  `redteam*.py` (adversarial verification), `qi_ledger.py` (quantum
  inequality ledger).

## Re-running the headline check

Python 3.12, NumPy/SciPy/SymPy (float64 throughout). The finalist audits
are driven by `verify_finalist.py` / `run_finalistB2.py` against the
frozen configurations in `results/frozen/`; the cross-check path uses
`warpax_check.py` / `warpax_crosscheck.py` (optional, requires warpax).
Expected agreement: NEC minima +2.121×10⁻⁵ (A) and +2.864×10⁻⁵ (B2) on
both paths, Hawking–Ellis Type I everywhere.

## Licence

MIT. The physics, favourable or not, belongs to whoever checks it.
