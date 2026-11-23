# Gate 8 — Worker W-A: G8-1 (lapse-re-equilibrated nested shells)

**Claim source:** Phase 46 P46-2 (`phase46/CHECKPOINT46.md` §P46-2,
`phase46/results/p462_memo.md`, `p462_results.json`, `p462_follow.json`);
baseline Phase 41 P41-3. **Gate protocol:** `gate8/GATE8.md`.
**My machinery:** `gate8/wa_lib.py` — fresh code, different in kind from
the Phase-1 judge. The judge differentiates Γ numerically (nested
FD4-of-FD4). Mine takes **direct finite differences of the metric's
first and second derivatives** (2nd-order and 4th-order flavours) and
forms ∂Γ **algebraically** from ∂g, ∂²g and ∂g⁻¹ = −g⁻¹∂g g⁻¹. Only
the stored composed-metric *definition* (shell profiles,
`build_composed`, `composed_gfunc`) and the audit point sets are
shared — that definition is the object under audit. float64
everywhere. Numbers: `results/wa_g8_1_numbers.json`
(runs `wa_run1…wa_run6`); search log: `results/wa_search_log.md`.

---

## 1. Correctness verdict: **REPRODUCED WITH RESTATEMENT**

The verdict row, the anatomy, the calibration gate, both instrument
claims and the follow-up row all reproduce on the independent path.
Two restatements are required: the carried DEC caveat (§3) and the
quantification of the 0.0998 boundary failure (§4). Neither touches
the headline: **payload 0.0799c passes full bars; the 0.05c
single-shell frontier is beaten by composition.**

### Anchors (before any claim number)

- **Minkowski:** max|T| = **0.0 exactly** on my path, both
  discretisation orders, h = 0.3 and 0.15.
- **Finalist-A calibration (payload 0.04, P41-3 control):** anatomy
  reproduced exactly (composed lapse at inner mid-wall −0.29750 vs
  −0.13197 alone, e^a ratio 0.84745, W held at 0.022822). My worst
  margin **+5.30×10⁻⁷ at h = 0.15** (phase record +5.50×10⁻⁷;
  h = 0.3: mine +2.34×10⁻⁷ vs +5.48×10⁻⁷ — the exterior-tail margin
  is the most FD-sensitive number in the row; sign, kind (SEC) and
  Type-I fraction 1.000 all match). Gate passes on my path.

### Verdict row — frontier payload 0.0799 (β_o = 0.04775, β_i = 0.03225)

Anatomy, verified on my path to all printed digits: composed lapse
at inner mid-wall **−0.72178** vs **−0.28339** alone; e^a ratio
**0.64507**; coordinate β_i turned down 0.05 → 0.032254 (×0.6451);
characteristic orthonormal shift **W = 0.066381**, equal to the
verified alone value — held, not relabelled.

Full-volume worst margins by region, my 4th-order direct-∂² path,
h = 0.15 (phase record in brackets):

| region | mine | phase |
|---|---|---|
| payload | **+1.14×10⁻⁴** | +1.09×10⁻⁴ |
| inner wall | **+9.74×10⁻⁴** | +9.79×10⁻⁴ |
| outer wall | **+2.86×10⁻⁵** | +4.05×10⁻⁵ |
| cavity | −1.49×10⁻⁶ (see §3) | −1.49×10⁻⁶ |
| exterior | +2.11×10⁻⁶ | +2.09×10⁻⁶ |

Type-I fraction **1.000** (mine and phase). My 2nd-order flavour at
h = 0.15 agrees in sign on every deciding region (inner +1.18×10⁻³,
outer +1.91×10⁻⁵, payload +3.9×10⁻⁶). Conservation, my own
divergence read on 28 wall points: relative median **7.8×10⁻³**
(phase 4.6×10⁻³) — clean by the programme's pattern.

## 2. The other two instrument claims — both confirmed

- **h = 0.3 payload-region negatives are under-resolution:** my
  payload worst runs **−4.43×10⁻⁵ (h = 0.3) → +1.14×10⁻⁴ (0.15) →
  +1.16×10⁻⁴ (0.075)** — flips positive and stays, as claimed.
- **Cavity stencil-clear reads:** cavity points with 4.0 < r ≤ 4.6
  (stencil clear of the outer wall's inner edge at r = 5) read DEC
  min **+9.98×10⁻⁵ (h = 0.15), +1.18×10⁻⁴ (0.075), +1.27×10⁻⁴
  (0.0375)** on my path — confirming the phase's +1.13×10⁻⁴ /
  +1.15×10⁻⁴.

## 3. THE CAVEAT — settlement: **ARTEFACT** (representation floor),
## with the floor stated exactly in the claim wording

Record location, stated precisely: the −3.7×10⁻⁶ touch is the
**cavity** region's worst DEC on the focused point set at
**r = 4.8, h = 0.075** (`p462_follow.json`,
`F_payload0.08_focused_pc`; the claim text's "payload-region" label
is the phase memo's loose wording — the payload region itself reads
+1.21×10⁻⁵ there). r = 4.8 sits 0.2 inside the outer wall's inner
edge (R1o = 5).

What my settlement runs show (fixed worst site
(−2.245, −2.387, −3.508), r = 4.8; full tables in the numbers JSON):

- **At the registered spacings the value is sign-unstable.** Focused
  cavity DEC min: mine **+2.06×10⁻⁶ at h = 0.15** (phase +2.39×10⁻⁶);
  at h = 0.075 the phase judge reads −3.73×10⁻⁶ at its worst
  direction, **+1.08×10⁻⁶ at my site point**, while my direct-∂²
  path reads −1.21×10⁻⁵ at that point. Same shell, same h, two
  discretisations and two directions span both signs at
  |DEC| ≲ 1.2×10⁻⁵.
- **Refinement does not converge to a negative continuum value.**
  The h-ladder at the fixed site is non-monotone in *both*
  machineries (judge: +5.80×10⁻⁶, +1.08×10⁻⁶, −3.25×10⁻⁵,
  −1.90×10⁻⁵ for h = 0.15 → 0.01875; mine, 4th-order: +6.87×10⁻⁶,
  −1.21×10⁻⁵, −3.95×10⁻⁵, −2.06×10⁻⁴), and the fine-h radial
  profile oscillates in sign on a ~0.1 radial wavelength
  (r = 4.8: −2.06×10⁻⁴; 4.9: +9.9×10⁻⁵; 4.95: −2.27×10⁻⁴, mine at
  h = 0.01875). No Richardson extrapolation is supported — the
  sequence has no continuum limit to extrapolate. The cause is in
  the stored object itself: the metric is a cubic spline over a
  dr = 0.005 tabulation of functions built from *linearly
  interpolated* mass profiles, so below h ≈ 0.0375 both evaluators
  resolve representation structure near the wall edge, not a smooth
  field. This is the Gate-6 G6-1 pattern: a machinery/representation
  artefact point, settled by ladder + second discretisation.
- **The cavity interior is not marginal.** Stencil-clear cavity
  (§2) is +1.0–1.3×10⁻⁴, stable under refinement in both
  machineries — two orders above the dip. Type I is 1.000 at the
  site at every h in both machineries.

**Settlement:** the −3.7×10⁻⁶ touch is an **artefact of the
discretisation/representation floor in the near-edge cavity shell
(4.6 < r < 5)**, not a genuine marginal DEC failure of the composed
configuration: it has no convergent negative continuum value in
either discretisation, while every stencil-clear cavity read is
≥ +9.98×10⁻⁵. Honesty rider, carried into the wording below:
refinement does not make the near-edge shell read clean either —
at h ≤ 0.0375 it reads down to −3.9×10⁻⁵ (both machineries agree at
h = 0.0375) — so the claim may not assert a clean continuum DEC
pass in that shell; it asserts the pass at the registered audit
pattern with the floor named.

## 4. Boundaries

- **Payload 0.0998 — failure CONFIRMED on my path, quantification
  restated.** The judge's worst point (7.038, 1.834, −0.280),
  r = 7.278, is **non-Type-I in my machinery too, at every h and
  both orders** — and a non-Type-I point fails the ECs by
  Hawking–Ellis classification. My independent sampled NEC at that
  point: **−3.3×10⁻⁵ … −3.7×10⁻⁵**, matching the judge's NEC
  −3.35×10⁻⁵. My outer-wall Type-I fraction 0.983 (judge 0.985);
  inner wall passes on my path at **+9.81×10⁻⁴** — the P41-3 inner
  kill is gone, as claimed. The phase's "SEC −2.73×10⁻⁴" is the
  judge's sampled-fallback quantification at that non-Type-I point;
  the failure itself (outer wall, classification-level, h-stable)
  is real and machinery-independent, but the −2.73×10⁻⁴ figure is
  judge-specific and the wording below says so.
- **Follow-up row, β_o capped at 0.05 → payload 0.0821 — PASS
  confirmed** on my path (h = 0.15, 4th-order): payload
  +1.14×10⁻⁴, inner wall +9.75×10⁻⁴, outer wall +2.62×10⁻⁵,
  Type-I 1.000, cavity −1.83×10⁻⁶ (the same §3 floor shell).
  (Phase: +1.09×10⁻⁴ / +9.79×10⁻⁴ / +3.96×10⁻⁵.) The dual
  re-equilibration row (0.0729) was not re-run; the capped row was
  the spot-check.

## 5. Novelty verdict: **NOVEL**

Systematic search logged verbatim in `results/wa_search_log.md`
(11 queries; arXiv + web native; INSPIRE / Semantic Scholar reached
only via arXiv-linked indexes — gap stated in the log, Gate-6
precedent). Near neighbours, all single-shell: Bobrick–Martire
(arXiv:2102.06824 — one shell moving inertially; framework, no
composition); Fuchs et al. (arXiv:2405.02709 — one stable shell +
shift, ~0.04c class); Warp Factory (arXiv:2404.03095 — toolkit,
single metrics); Lentz (arXiv:2006.07125) and Fell–Heisenberg
(arXiv:2104.06488) — single solitons, Eulerian-frame claims;
Procaccia (academia.edu, Oct 2026, unrefereed — continuum EC
certificate for ONE optimized Fuchs-form shell to β = 0.1363);
Le (arXiv:2605.25417, 2602.18023, 2606.22531 — single shells).
Concentric-shell GR exists as collapse/dynamics theory (two dust
shells, AdS interacting shells, null-shell pairs) — none of it is a
transport configuration, none composes EC-legal shells, and no
source found holds an inner shell's orthonormal shift fixed against
an outer shell's deepened lapse. The ingredients (Fuchs-form legal
shell, Bobrick–Martire shell picture) are known; the composition
result is not.

**Novel part, one quotable sentence:** "Nesting two individually
energy-condition-legal warp shells defeats legality only through
lapse-deepening amplification of the inner shell's orthonormal
shift, and re-solving the inner shell in the composed lapse —
coordinate β_i reduced by exactly the lapse factor (×0.6451) so the
orthonormal shift stays at its verified alone value (0.06638) —
restores full legality at a composed payload of 0.0799c, above the
0.05c single-shell frontier."

## 6. EXACT restated wording for the claim (the only form it may
## be uploaded with)

> Nested GR shells with the inner shell solved in the composed
> lapse (coordinate β_i turned down by exactly the lapse factor
> ×0.6451; orthonormal shift W held at the verified alone value
> 0.06638) carry a payload at 0.0799c at full bars on the
> registered audit pattern (full-volume all-directions
> NEC/WEC/SEC/DEC at h = 0.3/0.15, Hawking–Ellis Type-I fraction
> 1.000, conservation clean; h = 0.15 worst margins by region:
> inner wall +9.79×10⁻⁴, outer wall +4.05×10⁻⁵, payload region
> +1.09×10⁻⁴; independently reproduced by a direct-∂² evaluator:
> +9.74×10⁻⁴ / +2.86×10⁻⁵ / +1.14×10⁻⁴). One floor caveat is part
> of the claim: in the near-edge cavity shell 4.6 < r < 5 the DEC
> read is at the discretisation/representation floor — it touches
> −3.7×10⁻⁶ at h = 0.075 on the focused set, is sign-unstable
> across spacings, directions and discretisations at
> |DEC| ≲ 4×10⁻⁵ under refinement, and has no convergent negative
> continuum value in either of two discretisations different in
> kind; every stencil-clear cavity read is ≥ +9.98×10⁻⁵ and
> Type I remains 1.000 — the touch is a floor artefact, and no
> clean continuum DEC value is asserted for that shell. Follow-up
> rows (not verdict rows): dual re-equilibration passes at 0.0729;
> β_o capped at its verified 0.05 gives a passing 0.0821
> (independently confirmed). At 0.0998 the inner wall passes
> (+9.86×10⁻⁴; the P41-3 inner kill is gone) but the outer wall
> fails: its worst point is Hawking–Ellis non-Type-I in two
> independent discretisations (sampled NEC ≈ −3.4×10⁻⁵; the
> Phase-1 judge's sampled SEC quantification is −2.73×10⁻⁴), so
> the P22-3 trigger does not fire. C12: subluminal pre-arranged
> configuration; construction-inclusive arrival ≥ D/c; no
> transport claim beyond the payload's own speed.

**Gate verdict (W-A recommendation): UPLOAD-READY AFTER
RESTATEMENT** — correctness REPRODUCED WITH RESTATEMENT, novelty
NOVEL, hedges intact, nothing uploaded.
