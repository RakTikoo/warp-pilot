# GATE-33 ITEM 3 — YBBY FIG. 7 BAND GEOMETRY, VECTOR/PIXEL-GRADE EXTRACTION

Worker deliverable: drawn band geometry and three point-membership reads only.
No physics verdicts beyond the membership reads.

## 0. Source note (a discrepancy in the tasking, resolved on disk)

`ybby_src/EA-constraints.pdf` is **not** the four-panel Fig. 7 itself: in
`paper.tex` it is the *combined summary* panel (Fig. 1, left) — one linear
(c₊, c₋) panel, c₊ ∈ [0,1], c₋ ∈ [0,1], with a **zoom inset**
(c₊ ∈ [0, ≈0.0365], c₋ ∈ [0, 0.004]) in which the combined binary-pulsar
region is drawn as a single filled purple polygon. The four individual
Fig. 7 panels (`fig:Pdot-EA`) are separate files in the same e-print source
and were extracted as well:

| panel | file | system |
|---|---|---|
| top-left | `Pdot-constraint-NSWD-Bhat.pdf` | Ṗ_b, J1141−6545 |
| top-right | `Pdot-constraint-NSWD-Antoniadis.pdf` | Ṗ_b, J0348+0432 |
| bottom-left | `Pdot-constraint-NSNS.pdf` | Ṗ_b, J0737−3039 |
| bottom-right | `alpha-constraint-NSWD.pdf` | α̂, J1738+0333 |

Combined reads rest on the EA purple polygon (the paper's own combined
region), cross-checked against the intersection of the four panel bands.

## 1. Method

- EA file: `pdftocairo -svg`; the purple region is exactly 3 paths of fill
  `rgb(50%, 0%, 50%)` (main-panel sliver, inset polygon of 26 vertices,
  legend swatch). Vertices taken verbatim from the vector data.
- Inset axes calibrated from the **drawn tick marks** (exact vector
  segments), not from label positions.
- Panels: log-log; rasterised at 600 dpi (`pdftocairo -png`), green hatch
  segmented by colour; axes calibrated from `pdftotext -bbox` tick-label
  centres (55.55 pt/decade in c₊, 53.90 pt/decade in c₋; label centres were
  verified against vector axis anchors in the EA file to ≤0.09 pt).
- Cross-checks: 600-dpi raster of the EA file (purple bbox in data coords
  agrees with the vector polygon to 1.3×10⁻⁵ in c₋); the main-panel purple
  sliver, independently calibrated, gives the same region
  (c₊ ≤ 0.03239, c₋ ≤ 3.167×10⁻³).
- Scripts + data: `g33_fig7_extract.py`, `g33_fig7_cherenkov.py`,
  `fig7_extract/g33_fig7_data.json`, SVGs/PNGs in `fig7_extract/`.

## 2. Calibration (EA inset) and extraction error

- c₊ = (x_svg − 172.155781) / 3004.45 — bottom ticks at c₊ = 0, 0.01, 0.03
  give 3004.4 and 3004.5 per unit (relative residual 3×10⁻⁵).
- c₋ = (138.235802 − y_svg) / 26290 — left ticks at c₋ = 0, 0.002, 0.004
  give exactly 52.58 pt per 0.002, twice.
- The polygon's own bottom-left vertex sits exactly on the calibrated
  origin (0, 0).
- **Residual error in c₋ at c₊ = 0: σ = ±2×10⁻⁵.** Tick/zero residuals
  contribute ≤4×10⁻⁷; the adopted σ is dominated by the 26-vertex polygon's
  chord-vs-smooth-curve sagitta and the drawn edge's stroke width, and is
  confirmed by the independent raster read (Δ = 1.3×10⁻⁵ on the region max).

## 3. The combined region as drawn (EA inset purple polygon, data coords)

Ordered vertices (c₊, c₋), abbreviated — full table in
`fig7_extract/g33_fig7_data.json`:

(0, 0) → (0.021486, 0) → (0.021851, 1.800×10⁻⁴) → (0.023312, 9.029×10⁻⁴) →
(0.024774, 1.3531×10⁻³) → (0.026235, 1.7464×10⁻³) → (0.027696, 2.1096×10⁻³) →
(0.029157, 2.4535×10⁻³) → (0.030618, 2.7831×10⁻³) → (0.032080, 3.1022×10⁻³) →
**(0.032394, 3.1704×10⁻³) [global max c₋]** → (0.031835, 3.1653×10⁻³) →
(0.028668, 3.1201×10⁻³) → (0.025500, 3.0636×10⁻³) → (0.022334, 2.9926×10⁻³) →
(0.019167, 2.9018×10⁻³) → (0.016667, 2.8173×10⁻³) → (0.013334, 2.6202×10⁻³) →
(0.009999, 2.3805×10⁻³) → (0.009700, 2.3565×10⁻³) → (0.007899, 2.2049×10⁻³) →
**(0.006100, 2.0416×10⁻³) [top of the left chain]** → (0.004467, 1.5254×10⁻³) →
(0.001678, 5.907×10⁻⁴) → (0.000630, 2.415×10⁻⁴) → (0, 0).

Top boundary T(c₊): T(0)=0; T(0.000630)=2.415×10⁻⁴; T(0.001678)=5.907×10⁻⁴;
T(0.004467)=1.5254×10⁻³; T(0.006100)=2.0416×10⁻³; T(0.01)=2.3805×10⁻³;
T(0.02)=2.9258×10⁻³; max 3.1704×10⁻³ at c₊=0.032394.

**Geometry that governs all reads:** the region is a wedge-blob containing
the origin. Its left boundary is the Cherenkov/stability edge rising from
the origin (drawn left edge at c₋=1.590×10⁻³ is c₊=0.004671; the drawn
Cherenkov line at that height, measured in the raster where purple does not
cover it and continued to the origin, is c₊≈0.004601 — coincident within
~1 line width, purple on the allowed side). A literal slice at exactly
c₊=0 therefore meets the region only at the single point (0,0): **the
literal c₊=0 extent is 0**. The reads below are the gate's registered
semantics (Arm 2's "almost-box containing the origin"): a point at c₊≈0 is
judged by its c₋ against the region's c₋ extent at its left edge, and by
the c₊-window the drawn region actually spans at that c₋. Both statements
are carried so the gate can see exactly what is and is not decided.

**Combined c₋ extent (as drawn):**
- at the region's left edge (top of left chain, c₊=0.006100): **2.0416×10⁻³**
- global maximum: **3.1704×10⁻³ ± 2×10⁻⁵** at c₊=0.032394
- literal slice at c₊=0: 0 (origin only)

## 4. The three reads

### (a) c₋ = 1.590×10⁻³ (c_V = 10 flat-row maximiser) — **INSIDE** (deciding grade)

- Combined: at c₋=1.590×10⁻³ the drawn purple region spans
  **c₊ ∈ [0.004671, 0.025653]**. Margin in c₋ against the region's
  left-edge extent (2.0416×10⁻³): **+4.52×10⁻⁴ = 23σ** (σ=2×10⁻⁵);
  against the global max: +1.580×10⁻³ = 79σ. Distance to nearest drawn
  boundary exceeds the extraction error by >20× — deciding grade met.
- Per panel (green band present at that row in every panel; raster c₊
  spans at c₋=1.590×10⁻³): J1141−6545 [0.0055, 0.112] **IN**;
  J0348+0432 [0.0055, 0.423] **IN**; J0737−3039 [0.0055, 0.0252] **IN**;
  J1738+0333 [0.0055, 0.499] **IN**. (Raster left edges sit on the first
  hatch stroke right of the shared stability line; the binding right edge
  is J0737's, 0.0252 raster vs 0.025653 vector — agreement ✓.)
- Caveat carried on the face: at exactly c₊=0 the point is outside the
  wedge (extent 0); it is inside for every c₊ in [0.004671, 0.025653].

### (b) c₋ = 0.16586208 (Corner B projection) — **OUTSIDE** (calibration cross-check PASS)

- Combined: exceeds the region's global maximum c₋ (3.1704×10⁻³) by
  **0.16269 = 8135σ**. This reproduces the registration's "outside by
  0.163" — the calibration is confirmed, not contradicted.
- Per panel: **OUTSIDE all four** — above every panel's plotted range
  (each frame ends at c₋=0.1).

### (c) c₋ = 5.089×10⁻⁵ (c_V = 2 maximiser) — **INSIDE** (combined)

- Combined: at c₋=5.089×10⁻⁵ the drawn purple region spans
  **c₊ ∈ [1.328×10⁻⁴, 0.021588]**. Margins: below the top boundary by
  ≥5.40×10⁻⁴ = 27σ (at c₊=0.001678, T=5.907×10⁻⁴); above the bottom edge
  (the c₋=0 axis, which the region includes) by 5.089×10⁻⁵ = 2.5σ.
- Per panel: **not decidable from the panels as drawn** — 5.089×10⁻⁵ lies
  below every panel's frame (frames end at c₋≈7.5×10⁻⁴, log axes). The
  panels neither contain nor exclude it; the combined EA inset (linear,
  drawn to c₋=0) is the deciding drawn source, and it contains it.
- Same c₊=0 caveat as (a): inside for c₊ ∈ [1.328×10⁻⁴, 0.021588], not at
  the single point c₊=0.

## 5. Failure modes / limits

- Tasking named EA-constraints.pdf as the multi-panel figure; it is the
  combined summary panel. Handled by extracting both it and the four real
  panel files (§0). No read depends on the misnomer: the combined polygon
  and the panel intersection agree on the binding edges at (a).
- The four panels are log-log and truncated (c₋ from ≈7.5×10⁻⁴ to 0.1):
  they cannot decide (c) (below frame) and decide (b) only as
  "above frame". The EA inset is the only drawn source covering (c).
- The combined polygon is a 26-vertex sampling of a smooth curve; σ=2×10⁻⁵
  in c₋ covers chord sagitta and stroke width. All deciding margins are
  ≥23σ except (c)'s distance to the c₋=0 axis itself (2.5σ), which is a
  boundary the region includes, not one it must clear.
- An SVG tile-union test for the Cherenkov region was discarded
  (main-panel light-blue tiles overlap the inset's SVG coordinate area);
  the Cherenkov-side check was done in the raster instead
  (`g33_fig7_cherenkov.py`).
