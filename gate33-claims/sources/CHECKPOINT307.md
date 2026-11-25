# PHASE 307 — CHECKPOINT: BREAK THE CHANNEL (red team on the spin-1 result)

**Registration:** `phase307/work/p307_registration.md`
(ledger 761's charge; all seven arms' tests, scopes, and
verdict forms fixed before any arm ran). **Arm records:**
`phase307/work/p307_arm{1..7}_memo.md` (+ Arm 6 script/
output). **Synthesis:** `phase307/results/p307_memo.md`.
**Controls (before all arms, all PASS):** Phase 303's
pricing re-run reproduces Corner B HT 2.0607×10⁻¹⁸ and the
flat rows 2.8044×10⁻⁵ exactly; the audit re-run reproduces
the stored fence tables incl. Corner A's L9 reads
0.15411/0.31451/0.53153 (`work/p307_controls_*.out`).

## OVERALL VERDICT: CHANNEL BROKEN

Two arms break, at two different scopes; one arm fences;
four hold (two weak, worded as such); one sub-point is
unresolved (subsumed). Per the registration, the affected
claims (G32-E, G32-F, and G32-G's wording) return to a
gate — the parent's action, not this phase's.

| Arm | Test | Verdict | Scope |
|---|---|---|---|
| 1 | L9's O(10%) tolerance vs J1738's measured Ṗ_b | **BREAKS** | the flat value |
| 2 | YBBY Fig. 7 bands as drawn | **BREAKS** | Corner B (projection scope) |
| 3 | Full-EA cosmology | HOLDS (weak) | all points — absence, not a pass |
| 4 | Taherasghari–Will dispute | **FENCED** | flat value's pricing framework |
| 5 | Three-sector stability at the points | HOLDS | all five points |
| 6 | The w₀ ≈ 1 edge, interior δ = 10⁻³ | HOLDS | the flat value |
| 7 | GW polarisation content | NOT APPLICABLE (weak HOLD) | fence completeness |

## The breaks, in numbers

**Arm 1.** Freire et al. 2012: Ṗ_b^Int/Ṗ_b^GR = 0.9350 ±
0.132 for J1738+0333 (the measured decay is 6.5% SLOWER
than GR centrally). YBBY Eq. (190)'s tolerance is a linear
sum of 1σ-class errors bounding the TOTAL ⟨𝒜⟩ − 1, and
YBBY never applied it to J1738's Ṗ_b. At that implicit
confidence the data-grade dipole cap is **0.067**, not 0.1
(the 0.1 spends the negative central offset as headroom;
it sits at 1.25σ — defensible at no single stated
confidence; at the fence's own 95% convention the cap
would be 0.193 and the value would rise to 5.42×10⁻⁵).
The maximised ratio is exactly linear in the cap (verified
two ways), so the flat value falls to **HT 1.87×10⁻⁵ /
NS–BH 1.70×10⁻²** (factor 0.67). Flatness itself is not
touched. The 2026 timing update's indicative 1σ cap
(≈ 0.095) is also below 0.1.

**Arm 2.** Fig. 7's bands are existential projections in
the (c₊, c₋) plane (α₁/α₂, masses, P_b, sensitivities
varied): inside = weak hold, outside = clean exclusion.
Text-grade digitisation from §VII C.1's own numbers
(combined region an almost-box, Δc₋ = O(10⁻³), containing
the origin; read-off error ±3×10⁻³ in c₋ — the figure's
raster/vector data were not extractable, gap on record).
The c_V = 1 and c_V = 2 maximisers (c₋ = 5.3×10⁻⁶,
5.1×10⁻⁵) hold weakly; the c_V = 10 maximiser
(c₋ = 1.590×10⁻³) is UNRESOLVED (0.59×10⁻³ past the
nominal box edge, inside the digitisation error);
**Corner B (c₋ = 0.16586208) is outside by 0.163 in c₋,
~55× the error** — BREAKS at projection scope. This
contradicts Phase 303 §4(ii)'s "consistent with"
recording; which rung-2 modelling choice drives the
bands-vs-mechanism-fence discrepancy is a named successor
diagnosis, not adjudicated here.

**Arm 4 (fence, not break).** TW (PRD 108, **124026**
(2023) — Gate-32's citation corrected — and PRD 112,
024013 (2025)) do not claim the far-zone pricing is wrong;
their near-zone dipole (vector-speed only) would stop L9
binding at the c_V = 2/10 maximisers, kill flatness, and
re-price the rows to HT 8.415×10⁻⁶ (c_V = 2, still above
the bar) and 8.42×10⁻⁸ (c_V = 10, below it). Vaglio et al.
2026 engage TW and deliberately adopt the far-zone
expression. **Fence wording: G32-F stands exactly and
only where energy-balance/far-zone pricing is the
correct Ṗ_b pricing.**

## What survives

- **Distance-0 (G32-G) in substance:** the bar (HT ≥ 10⁻⁶
  at c_V ≥ 2) is met at c_V = 2 under every pricing on
  record (1.87×10⁻⁵ far-zone data-grade; 8.415×10⁻⁶ TW)
  and at c_V = 10 under far-zone pricing only. Its
  Gate-32 §5 wording quotes the broken 2.8044×10⁻⁵ and
  returns to a gate for restatement.
- **Flatness, the ridge, the mechanism** (Arms 5, 6):
  stability-clean at every point (q_S up to 7.5×10⁵,
  q_V = c₁₄ > 0, all speeds² > 0); the w₀ ≈ 1 edge is the
  scalar Čerenkov surface and the value reproduces to all
  quoted digits with the edge held interior at δ = 10⁻³.
- **G32-A (structure) and G32-D (Corner A's death):**
  untouched by every arm.
- **G32-C (σ values):** not directly attacked; the Gupta
  cross-check (Phase 306) remains outstanding.
- **Arms 3/7 weak holds** are absences, recorded as such;
  Arm 3 additionally records two scope-shielded threats
  against Corner B (unlicensed khronometric transfer
  would exclude it ×65.8; Audren's EA-surface c_χ² < 427
  limit, which Corner B exceeds ×2.47×10⁴ off-surface) —
  an off-surface EA MCMC is the named instrument that
  could activate either.

## DESK

`DESK: one arm contacted data beyond the applied fences
and changed a number — ARM 1 (PSR J1738+0333's measured
Ṗ_b at published precision, Freire et al. 2012; Vaglio et
al. 2026 update indicative): the dipole leg's data-grade
cap is 0.067 at its own implicit confidence, not 0.1.
Arms 3 and 7 evaluated published data products
(cosmological constraint sets; GW-catalog polarisation
analyses) and applied no new bound; Arm 2 used the
published Fig. 7's stated geometry.`

## Successor diagnoses named (charges are the parent's)

(i) The bands-vs-mechanism-fence discrepancy at Corner B;
(ii) pixel-grade digitisation of YBBY Fig. 7 (resolves the
c_V = 10 maximiser's band status); (iii) an off-surface EA
cosmology MCMC (converts Arm 3's conditional threats);
(iv) the Gupta σ cross-check (Phase 306, charged
elsewhere). No ledger append, no launches, no user
contact, no publication action — this phase's output is
the internal record above.
