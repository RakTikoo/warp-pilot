# P80-3 — SOURCE-MODULATED COMPOSITION

## VERDICT: BEATS 0.0799 AT FULL LEGALITY

**MILESTONE (payload transport category only).** A composed
(nested-shell) configuration built in the source-modulated design
space — each shell's shift derived by integration from an optimised
Procaccia-form source, both shells' orthonormal shifts held at their
alone values under lapse re-equilibration — carries a payload at
**0.08745c** and passes the full gate-standard legality audit
(Type-I + sampled-null + margins, full volume over both shells AND
the cavity, with the one cavity site resolved by the registered
ladder pattern; see §3). The standing verified mark in this exact
category is 0.0799c (Phase 46, Gate-8 restated scope); this row beats
it. Locked language: this is a payload-transport result. The
bare-shell mark is a different category and is not claimed, not
compared against, and not approached in any wording here.

A second row in the same space, at **0.08104c**, also beats the mark
under the same audit pattern and corroborates the first (§2).

## Plain language

Phase 46's nested shells carried a payload at 0.0799c using ordinary
cosine-shaped shift profiles. The question here was whether building
the same nested object in Procaccia's design space — where the shift
is not drawn directly but grown by integration from an optimised
"source" function — would carry a payload faster. It does, by about
9%: 0.0875c against 0.0799c, with every energy condition satisfied
everywhere the audit can resolve. The gain did NOT come from either
shell's wall getting stronger in composition (the walls read almost
exactly what they read in Phase 46). It came one level earlier: in
this design space each shell ALONE stays legal up to a higher
operating speed (0.06 instead of the cosine shells' 0.05), so when
both shells' speeds are held honestly through the composition's
gravity (the lapse tax), the discounted sum lands higher. The wall
that stopped Phase 52/57 — the cavity between the shells — does not
bind here at all: this is the narrow frontier cavity, and its only
negative read is the numerical stencil artefact the programme has
already met and settled three times on this exact background. What
actually caps this design space is new: at the next speed step
(0.07 alone) the outer shell's shift transition — which spills
wider than the shell itself — breaks in its own fringe, even though
the shell wall stays perfectly legal. The binding moved from the
composition to the single shell's fringe.

## 1. Construction (as registered)

- **Machinery route: REUSE.** The source→flux→shift chain is Phase
  73's P73-1 build (`phase73/p731_lib.py`, itself the registered
  adaptation of `phase50/p501_recon.py`), generalised from its
  single (10,30) shell to an arbitrary shell profile in
  `phase80/p803_lib.py`: per shell, chain grid dr = 2.5e-4, 12 cubic
  B-splines on the extended span [R1−0.3W, R2+0.3W] (P73-1's
  extended-domain rule), g₀ = ρ̂^q · tanh((r_m−r)/0.05) ·
  exp(ΣaᵢBᵢ), λ-balanced, F reset past r_m, S = 1 − k∫(F/r²)dr.
  Design vector per shell: 14 numbers (12 aᵢ, q, r_m) — the anatomy
  memo's pattern. Optimisation: L-BFGS-B polish (explicit
  forward-difference Jacobian, step 2e-3) maximising the
  clone-algebra core screening score (P73-1 pattern; screening
  only, never a verdict), continuation in β_alone.
- **Composition: Phase 46/52, unchanged.** Frontier class — outer
  (5,10) M = 1.9125, inner (2,4) M = 0.765 ×0.4 copy, TOV profiles;
  composed background by the p413 pattern (m_comp = m_i + m_o,
  outer TOV re-integrated against m_comp, a_comp integrated
  inward) — i.e. TOV backgrounds of the composed geometry.
  Staircase shift V(r) = β_o·S_o(r) + β_i·S_i(r) with each cosine
  window replaced by that shell's source-modulated S.
- **Held shifts (both shells, CHECKPOINT80 §P80-3):**
  β_s^comp = β_s^alone · exp(a_comp(r_mid,s) − a_alone,s(r_mid,s)),
  so each characteristic orthonormal shift W_s equals its alone
  value. Checker-verified: W relative error 1.7×10⁻¹⁶ on the
  deciding row. Lapse factors: inner 0.6451, outer 0.8152 (the
  Phase 46/52 numbers, reproduced).
- **Calibration:** the (0.05, 0.05) dual-held row's payload comes
  out 0.07292 — P52-3's F-dual row exactly — before any new number
  was trusted. The cosine P46-2 0.0799 row, read with the
  gate-standard auditor as a control, reproduces its regional
  pattern (inner +1.18e-3, outer +1.9e-5, cavity −1.109e-4 — the
  known artefact read, §3).

## 2. Economics BEFORE legality (standing discipline)

Held-W payload sums for every candidate row, computed and frozen
to `p803_economics.json` before any composed legality read:

| row (β_o, β_i alone) | W sum | payload (relat.) | alone-legal pair? |
|---|---|---|---|
| (0.05, 0.05) | 0.13276 | 0.07292 | yes |
| (0.05, 0.06) | 0.14604 | 0.07934 | yes |
| (0.06, 0.05) | 0.14604 | 0.08104 | yes |
| **(0.06, 0.06)** | **0.15931** | **0.08745** | yes |
| (0.07, 0.05) | 0.16503 | 0.08915 | no — outer not alone-legal at 0.07 (§4) |
| (0.07, 0.06) | 0.17834 | 0.09556 | no — same |

Composed audits (gate-standard, h = 0.15, worst margin by region;
full h = 0.3/0.15 tables in `p803_results.json`):

| row | payload region | inner wall | cavity | outer wall | exterior | Type-I | conservation (rel. med.) |
|---|---|---|---|---|---|---|---|
| (0.06, 0.06) **0.08745** | +3.85e-06 | +1.188e-03 | −1.107e-04 † | +3.20e-05 | +1.04e-06 | 1.000 | 0.0115 |
| (0.06, 0.05) 0.08104 | +3.86e-06 | +1.079e-03 | −1.104e-04 † | +3.20e-05 | +1.04e-06 | 1.000 | 0.0133 |
| (0.05, 0.06) 0.07934 | +3.86e-06 | +1.186e-03 | −1.072e-04 † | +2.71e-05 | +1.11e-06 | 1.000 | 0.0112 |
| (0.05, 0.05) 0.07292 | +3.87e-06 | +1.111e-03 | −1.070e-04 † | +2.71e-05 | +1.11e-06 | 1.000 | 0.0120 |

† the cavity site of §3 — a demonstrated stencil artefact, not a
margin failure; with it resolved by the ladder, every region of
the two beating rows is positive at h = 0.15, Type-I 1.000, and
the sampled-null cross-check is positive at every significant
point (deciding row min +8.5e-07 overall, +1.34e-04 in the cavity).

## 3. The cavity site (the deciding read, stated in full)

The only negative margin in any composed row sits in the cavity at
r ≈ 4.53, DEC, on the main grids (−1.11e-04 at h = 0.15,
−6.13e-04 at h = 0.3). It is the same read, at the same radius, at
the same magnitude, as (a) this item's cosine control of the
P46-2 0.0799 row on the identical background (−1.109e-04 — the
artefact belongs to the composed background's representation, not
to the source-modulated shift), (b) P52-3's F-dual row
(−1.09e-04), which its ladder showed to be a stencil artefact,
and (c) the read Gate-8 settled as a representation artefact in
the cavity shell 4.6 < r < 5 for the standing mark itself. The
registered ladder pattern, run here on the deciding row
(gate-standard auditor):

- focused set DEC: −1.81e-04 (h=0.15) → **+5.04e-07** (0.075) →
  **+1.21e-05** (0.0375), Type-I 1.000 at every rung;
- stencil-clear set DEC: −1.50e-04 → **+9.33e-05** → **+1.61e-04**
  (P52-3's F-dual stencil-clear numbers were +9.28e-05 / +1.60e-04
  — the same artefact, on the same background, to two digits);
- sampled-null NEC positive on both sets at every rung.

The deciding row therefore stands at exactly the standard the
standing 0.0799 mark stands at — no stronger, and the caveat is
carried identically.

## 4. Anatomy on the three registered axes

- **Inner wall — does not bind.** +1.19e-03 at h = 0.15 on the
  deciding row (Phase 46's row: +9.79e-04). The re-equilibration
  holds exactly as in Phase 46; the source-modulated inner shell
  is, if anything, slightly stronger in composition.
- **Outer wall — does not bind, but is the closest real margin.**
  +3.20e-05 at h = 0.15 (Phase 46's 0.0799 row: +4.05e-05, at a
  lower payload). Phase 46's binding (the outer shell's own
  overdrive at 0.0998) is absent here by construction: the outer
  shift is held, not overdriven.
- **Cavity — does not bind.** Phase 52's wide-cavity flux-vs-density
  constraint and Phase 57's element economics do not appear: this
  is the narrow frontier cavity, its sampled-null read is
  +1.34e-04, its stencil-clear DEC is +9.3e-05/+1.6e-04 at the
  fine ladder rungs, and its only negative is the §3 artefact.
- **What binds instead (the binding moved): the outer shell's
  ALONE fringe.** In this design space the outer shell alone is
  legal at β_alone = 0.06 (core polish score −9.8e-05 → +1.58e-04;
  wall +1.5e-04 at all audit spacings) but at β_alone = 0.07 its
  full-volume audit collapses — Type-I 0.646, sampled NEC
  −5.04e-04, h-converged at h = 0.075 — while its wall stays
  +1.49e-04, Type-I 1.000. The failure lives in the radii the
  audit classifies as payload/exterior but which are inside the
  source-modulated transition's span [3.5, 11.5] (the shell's
  nominal support is [5, 10]): the shift's fringe, where the
  density is only the smoothed tail, carries shift gradient the
  tail cannot support — the cavity-flux mechanism, relocated
  into the single shell's own fringe. The inner shell shows the
  same fringe signature in miniature at its transition edge
  (r ≈ 4.6: −9.2e-04 → −2.0e-04 → −1.4e-05 across the ladder,
  Richardson limit ≈ +4e-05 — an artefact-class read there, but
  the same address). **Net: relative to Phase 46/52/57's reads in
  our design space, the source-modulated design moved the binding
  off the composition entirely (walls held, cavity clean) and
  onto the alone shells' operating ceilings — and raised those
  ceilings enough (0.05 → 0.06 on the outer shell) that the
  held-W sum beats the mark before the new binding is reached.**

## 5. Independent second path (required for this verdict form)

On the deciding row (0.06, 0.06), two discretisations different in
kind from the primary gate-standard auditor, same point set,
h = 0.15 (`p803_verify_o0.06_i0.06.json`):

- **4th-order direct-∂² auditor (wa_diag):** Type-I 1.000,
  sampled-null +2.85e-06, every region positive except the §3
  cavity site at −5.93e-07 (floor level);
- **Phase-1 judge (nested-Γ, cross-check):** Type-I 1.000, every
  region positive except the same site at −1.18e-06 (r = 4.87);
- the §3 ladder (focused + stencil-clear, three rungs) concurs.
The second beating row (0.06, 0.05) was verified identically
(`p803_verify_o0.06_i0.05.json`: 4th-order worst −5.94e-07,
Phase-1 −1.18e-06, ladder stencil-clear +9.34e-05/+1.61e-04).
Checker: `p803_check.py` — 17/17 clauses PASS, including an
independent recompute of the held-W anatomy and both chains'
balance (λ = 1.0352 / 0.7356; balance_rel ≤ 2.5e-16; monotone;
endpoint reads S_lo−1 = −1.0e-04 / −2.2e-06, S_hi = +8.9e-05 /
+2.1e-06 — the chain's own endpoint residuals, reported as in
P73-1, not clipped).

## 6. Alone-shell record (the space the rows are built from)

Outer shell alone (gate-standard full audits; wall region worst):
β=0.05 legal (wall +1.57e-04); β=0.06 legal (wall +1.52e-04;
exterior tail artefact-pattern only, ladder-clean at h=0.075);
β=0.07 NOT legal (§4 fringe collapse; wall itself +1.49e-04).
β=0.08 not run — abandoned after the 0.07 anatomy showed the
ceiling (recorded in the run record). Inner shell alone: β=0.05
and β=0.06 legal under the same criterion (wall +6.3e-05…
+4.8e-04 across spacings; the r≈4.6 fringe site artefact-class,
§4); β=0.07/0.08 not run (the scan stopped once the deciding
pairs were in hand — the (0.06,0.06) pair does not need them;
recorded in the run record). The alone legality criterion —
payload+wall regions clean at h=0.3/0.15, exterior clean at
h=0.15 or the demonstrated artefact signature with a clean
h=0.075 rung — is stated in full in the run record; it is the
programme's P46-2/P52-3 artefact pattern made explicit, and no
row's status changes under the stricter reading except by the
named artefact sites.

## 7. C12 accounting

All speeds subluminal; both shells are pre-existing configurations
(pre-arrangement by ≤ c signals); construction-inclusive arrival
≥ D/c. No formation claim. The result is a prescribed-geometry
audit under the programme's shell standard: the required source
satisfies the energy conditions; no matter model, stability, or
formation route is claimed. Category: payload transport only.

## 8. Follow-ups (Failure Protocol — ≥1, mechanism-suggested)

1. **FU-P803-1 — Fringe-narrowed source span.** The new binding is
   the transition span [R1−0.3W, R2+0.3W] outrunning the density
   support. Re-run the alone optimisation with the span narrowed
   (e.g. ±0.15W) or with ρ̂-support weighting that forces S′ → 0
   where ρ̂ falls below a floor: does the outer shell's alone
   ceiling rise past 0.07, and does the composed held-W sum then
   reach the (0.07, ·) economics rows (0.08915 / 0.09556) that
   this item computed but could not legally assemble?
2. **FU-P803-2 — Composed-space polish.** This item optimised each
   shell alone and composed; the composed rows were never
   themselves polished. A bounded polish of both design vectors
   against the composed core score (held-W constraint imposed)
   tests whether the outer wall's +3.2e-05 — the closest real
   composed margin — can be widened at 0.08745, hardening the row
   before any Gate referral.
3. **FU-P803-3 — Analytic-tensor read of the §3 site.** The
   cavity artefact has now been ladder-settled on three
   backgrounds; an analytic/symbolic tensor evaluation at
   r ≈ 4.53–4.87 on the composed background would close the
   site class outright instead of by pattern.

## Files

`p803_lib.py`, `p803_alone.py`, `p803_inner.py`, `p803_compose.py`,
`p803_verify.py`, `p803_check.py`; results: `p803_results.json`
(frozen), `p803_economics.json`, `p803_alone.json` +
`p803_alone_state.json`, `p803_composed.json`,
`p803_verify_o0.06_i0.06.json`, `p803_verify_o0.06_i0.05.json`,
`p803_check.json`, `p803_run_record.md`, logs. INTERNAL only.
