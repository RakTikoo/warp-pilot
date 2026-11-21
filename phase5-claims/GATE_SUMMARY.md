# How these claims were gated

Before any Phase 5 result from this programme may be uploaded
for outside verification, it must pass an internal Novelty &
Verification Gate implementing a standing rule: publish only
what we are sure is (a) **new** — not already in the literature —
and (b) **right** — verified to the programme's full standard.
The gate itself uploads nothing and contacts no one; it prepares
verdicts only. This page summarises, for each of the three claims
in `CLAIMS.md`, how it was gated and what the gate decided.
(Adapted from the gate's internal record, GATE.md, 2026-11-21.)

## The gate's method (same for every claim)

**Novelty axis.** A systematic arXiv + web search for the claim's
exact statement and its near neighbours. Every query is logged
verbatim, sources are graded, near neighbours are cited by arXiv
ID/DOI, and the key neighbouring papers are read in full text.
Verdicts: **NOVEL** / **PARTIALLY KNOWN** (with the known part
cited exactly) / **KNOWN** (the claim dies as "ours"). A NOVEL
verdict is always backed by a one-sentence delimitation of
exactly what is new, quotable in an upload.

**Correctness axis.** An independent second path: the deciding
computation is reimplemented *from the claim statement*, as
fresh code that does not import the original machinery (shared
*definitions* — e.g. a published metric prescription — may be
imported; the deciding machinery may not), or derived
analytically where feasible. Verdicts: **REPRODUCED** (same signs
and values within the claim's stated margins) / **NOT YET** (the
specific missing piece named) / **FAILS** (anatomy required).

**Gate verdict per claim.** **UPLOAD-READY** requires novelty at
least PARTIALLY KNOWN with the novel part exactly delimited, AND
correctness REPRODUCED. Anything less is NOT YET (missing piece
named) or DEAD AS OURS.

All arithmetic float64, throughout.

## Claim 1 — H6, the wormhole exoticity floor identities

- **Novelty: NOVEL as a stated result.** 19 logged queries;
  full-text reads of the landmarks (Visser–Kar–Dadhich 2003,
  Nandi–Zhang–Kumar 2004, Lobo, Kar–Dadhich–Visser, Kuhfittig,
  Nandi–Zhang–Migranov, Zaslavskii, Marquet). Per component:
  the coordinate identity for general zero-tidal b — not found
  (the published general formula is a log-form, never reduced
  to the b/r form at Φ = 0); the proper identity — not found
  (the proper measure is published but evaluated only on
  specific solutions); both floors — not found (the
  literature's "arbitrarily small" results live only outside
  the claim's hypotheses: Φ ≠ 0 and/or finite cut-off); the
  factor-of-2 comparison and the −πr₀/2 spot value — not found.
  All *ingredients* are previously published; the
  identities/floors/factor-2 as stated results are not. (Under
  a stricter gate convention the verdict would read PARTIALLY
  KNOWN with the same delimitation; the scientific content is
  identical.) Caveat recorded: Visser's 1995 book could not be
  page-inspected from open sources; the quantifier postdates it
  (2003) per all citing papers.
- **Correctness: REPRODUCED.** Independent second path: a fresh
  symbolic derivation (both integrands reduce to total
  derivatives with residual exactly 0) plus fresh
  Gauss–Legendre quadrature — no original code — on 4 *new*
  shape profiles: left- and right-hand sides agree to
  ≤ 1.6×10⁻¹¹ on every profile, both floors hold on all
  profiles, the b = r₀²/r spot check returns −π/2 exactly, and
  both floors scale linearly in r₀. The second path also
  produced precision fixes, adopted in the claim's wording:
  the hypothesis set must include b C¹ and ∫(b/r) dr < ∞ (the
  looser original phrasing does not imply integrability —
  counterexample recorded), and no monotonicity condition on
  b′ is needed.
- **Gate verdict: UPLOAD-READY** — with the corrected hypothesis
  set and the Φ = 0-only scope carried in the wording (both are,
  in `CLAIMS.md`).

## Claim 2 — H4, warp shells re-solved in curved backgrounds

- **Novelty: NOVEL (delimited).** 21 logged queries, 25 sources
  graded, including full-text reads of Garattini–Zatrimaylov's
  Schwarzschild warp papers and Schuster–Santiago–Visser's
  ADM-mass paper, and citation follow-ups on Fuchs et al.
  (arXiv:2405.02709) searched specifically for curved-background
  extensions — none found. Per component: the re-solved
  Schwarzschild shell — not found (nearest neighbours are
  different objects: embedded Alcubierre bubbles with
  alleviated-but-persisting violations, no material shell, no
  conservation re-solve; Natário-class bubbles on Schwarzschild
  violating all conditions; thin Israel shells studied for
  stability, not thick re-equilibrated shells audited for
  energy conditions); the M_bg = 4 DEC mechanism — not found
  (only the published theme "DEC bounds compactness"); the AdS
  rows — not found as a shell result, and the weakest component
  (confirmatory); the superposition-artefact interpretation in
  demonstrated form (a re-solve that flips the verdict) — not
  found (the generic nonlinearity point is textbook). Caveat
  recorded: static all-conditions hollow shells with
  Schwarzschild exteriors exist as a class (gravastars) — the
  ingredients are not new, and the claim's wording carries that
  caveat.
- **Correctness: REPRODUCED.** Independent reimplementation from
  the claim statement (fresh code importing only the shell
  prescription definition; conservation solved with solve_ivp
  DOP853 at rtol 10⁻¹¹ where the original used a hand-rolled
  integrator; the Einstein tensor derived in-code with SymPy
  from the ansatz; margins from re-derived Type-I formulas).
  Shooting scales match to < 0.1% in all five configurations;
  exact core DEC margins match to 3 significant figures,
  including the M_bg = 4 DEC-only failure and the monotone
  margin sequence; the realised tangential pressure matches the
  prescription to ≤ 7.7×10⁻¹¹, so the built metric really
  carries the prescribed matter. Explicitly **not checked** by
  the second path (not failed — not attempted): the AdS β = 0.02
  row and all moving cases, which need the full 3-D judge.
- **Gate verdict: UPLOAD-READY** — with the delimitation
  sentence, the gravastar-class caveat, the AdS rows labelled
  confirmatory, and the AdS β = 0.02 row labelled as not
  independently re-checked (all carried in `CLAIMS.md`).

## Claim 3 — H2, the decoupling criterion

- **Novelty: PARTIALLY KNOWN, novel part delimited.** 23 logged
  queries plus full-text reads of Mironov–Rubakov–Volkova
  (arXiv:1812.07022, arXiv:1807.08361) and Franciolini et al.
  (arXiv:1811.05481), and checks across the Horndeski-wormhole,
  f(T), EiBI, f(R)/f(Q)-warp and non-minimal-scalar literatures.
  Per component: the γ identity — partially published (pieces
  sit inside MRV's published equations; the closed identity
  γ = 2(G₄ − 2XG₄X), "F₄'s only role is keeping ℋ > 0", and "in
  Horndeski γ ≡ ℋ" are nowhere stated — an unpublished
  consequence, low novelty weight); the rank / "not slaved"
  formulation — not found; the 7-case classification *as a
  classification* — not found (the individual wormhole verdicts
  are each published separately; the warp anti-aligned rows have
  no published counterpart); the throat-vs-wall asymmetry — not
  found; the rank-≥2 warp prediction — not found. Delimited
  novel part: "the general rank≥2 iff criterion together with
  its 7-case throat+wall classification, the asymmetry
  explanation, and the warp prediction is novel; the
  scalar-tensor mechanism is MRV's." Hazard flagged: the
  published cosmological term "γ-crossing" is a *different*
  functional, and MRV's Γ is a different object — any upload
  must disambiguate (ours does).
- **Correctness: computations REPRODUCED; framing qualified.**
  Independent second path implemented fresh from MRV's LaTeX
  source, no original engine imports. The γ identity and the
  ℋ − γ identity hold exactly (symbolic). The rank
  demonstration reproduces to the digit: γ(0) =
  −0.9900414979064531 invariant under F₄ rescaling (deviations
  ≤ 4.4×10⁻¹⁶), ℋ(0) sweeping −0.990 → +0.005 → +1.000 →
  +2.990. The f(R) required-matter tensor is exactly affine in
  α (symbolic), and a fresh finite-difference spot-check of the
  NEC-margin slope gives −1052.19 per unit α vs the claimed
  −1053.96 (0.17%, converging), sign negative. The
  qualification: a conceptual audit found the rank predicate is
  *not* one uniform mathematical statement across all 7 cases —
  it is literal for 5 (scalar-tensor pair, f(R), f(Q), X4) and
  a structural analogy for 2 (f(T): a single-number sign
  condition, no rank computed, and its perturbation-health
  premise unexamined; EiBI: two distinct functionals with
  disjoint windows, no rank computed). Strict score: 5/7 strict
  + 2/7 by analogy.
- **Gate verdict: NOT YET as originally stated** — the statement,
  not just its presentation, had to be fixed: (1) restate the
  classification as 5/7 strict + 2/7 structural analogies, with
  the f(T) row's unexamined-health-premise flag; (2)
  disambiguate the γ terminology. The gate ruled that once (1)
  and (2) are applied to the claim text, the verdict converts
  to UPLOAD-READY on the existing evidence, no new computation
  required — and `CLAIMS.md` publishes the claim in exactly
  that restated form. A recommended strengthening (a DHOST/EFT
  kinetic-matrix specialist sweep of the novelty search) is
  recorded as outstanding; the strong form (literal rank
  computations for f(T)/EiBI) remains an open strengthening,
  not part of the claim.

## Summary

| Claim | Novelty | Correctness | Gate verdict |
|---|---|---|---|
| H6 floor identities | NOVEL as a stated result | REPRODUCED | UPLOAD-READY (corrected hypotheses, Φ = 0 scope) |
| H4 re-solved shells | NOVEL (delimited) | REPRODUCED (AdS β = 0.02 row not re-checked) | UPLOAD-READY (delimitation, gravastar caveat, AdS labels) |
| H2 decoupling criterion | PARTIALLY KNOWN (novel part delimited; mechanism credited to Mironov–Rubakov–Volkova) | Computations REPRODUCED; framing qualified | UPLOAD-READY in the restated form published in `CLAIMS.md` (5/7 strict + 2/7 analogy; γ disambiguated) |

Nothing in this bundle was uploaded by the gate. The gate
prepared verdicts only.
