# GATE-6 — Worker W-C Report — Claim G6-3 (P43-1): Bulk-shortcut measurement in the √-shape braneworld throat bulk

**Worker:** W-C · **Claim:** G6-3 only · **float64 everywhere** · Nothing uploaded, no external contact.
**Code:** `gate6/wc_g63_solver.py` (ODE solver), `gate6/wc_g63_rest.py` (remaining rows, lean rerun), `gate6/wc_g63_scans.py` (classification scans).
**Numbers:** `gate6/results/wc_g63_numbers_main.json`, `wc_g63_numbers_rest.json`, `wc_g63_numbers_scans.json`.

---

## Verdict summary

- **Correctness: REPRODUCED WITH RESTATEMENT.** The headline measurement reproduces essentially exactly (my converged gain at z_a = 1, cap y ≤ 0.455: **0.4800**, vs the claim's subdivided 0.480; the stored nseg-24 value 0.5065 is confirmed to be the coarse-midpoint artefact, not the continuum value). The z_a = 0.5 row, the cap sequence, and the same-sheet control all reproduce. **One row does not survive as quoted: z_a = 2.** The converged gain there is **≈ 0.289**, not 0.177 (anatomy in §3.3). The claim survives with that row's number restated (§6).
- **Novelty: PARTIALLY KNOWN.** The bulk-shortcut concept and quantitative shortcut measurements in other bulks are published (Chung–Freese; Caldwell–Langlois; Abdalla et al.; Leach–Lesame; Dai–Stojkovic). What was not found in the literature is the measurement inside an exhibited wormhole-throat bulk lift, with its throat-specificity control and unattained-infimum-at-the-singularity structure (§5).
- **GATE VERDICT: UPLOAD-READY AFTER RESTATEMENT** (exact restated wording in §6; all hedges — cap-labelled, infimum not attained, EFFECTIVE ONLY under C12, graviton-only carrier — intact and independently supported).

---

## 1. Method — the independent second path

Phase 43's deciding machinery was a **discrete variational path minimiser** (`p431_geodesic.py minimise_time` over path nodes, midpoint-rule segment times, linear `RegularGridInterpolator` fields). It was **not** re-run or reused.

My path is structurally different: the optical functional
T = ∫ √((D² dz² + dy²)/A²)
is the length functional of the 2D Riemannian metric diag(E, G), E = (D/A)², G = (1/A)², in the (z, y) plane. I derived the Euler–Lagrange equation for y(z) from L = √(E + G p²), p = dy/dz,

  p′ = S/(G·E) · [ (E_y + G_y p²)/2 − (G_z + G_y p)·p + G·p·(E_z + E_y p + (G_z + G_y p)·p²)/(2S) ],  S = E + G p²,

and integrated it with `scipy solve_ivp` (DOP853, rtol 1e-11, atol 1e-13) in shooting/root-finding form:

- **Cross-throat rows.** A key structural finding first: shooting from the throat (0, y₀, p=0) shows every smooth symmetric crossing geodesic returns to the brane within Δz ≤ 0.260 (scan: y₀ = 0.05…0.455 → z_return = 0.193…0.260…0.169). **No smooth symmetric geodesic connects z = ∓z_a for any z_a ∈ {0.5, 1, 2}.** The optimum is therefore a **cap-riding path**: a geodesic arc from (z_a, 0) that hits the depth cap y = c at z₁, a boundary ride along y = c from z₁ to −z₁, and the mirrored arc. I minimised T over the arc's shooting slope p₀ (scan + two multiplicative zooms). At the z_a = 1 optimum the entry slope at the cap is small (near-tangential), as in Phase 43's stored path (their path reaches the cap at |z| ≈ 0.73; mine at z₁ = 0.697).
- **Field representation.** The stored fields (the shared definition, loaded from `phase43/results/p431_bulk_fields.npz`: A, D on snap_y × zz grids) were represented by **interpolating bicubic splines** (`RectBivariateSpline`, s = 0) — not Phase 43's linear interpolant. As a representation-sensitivity check, each headline path was also re-evaluated under Phase 43's **linear** representation (§3.4).
- **Brane times** are the shared definition (Φ = 0 proper length, D₀(z) = 2|z|/√(1−(1+z²)^(−1/2))), evaluated by quadrature at 1e-13 tolerance; they reproduce Phase 43's t_brane values exactly (2.9135262490, 6.2784217903, 15.2972393741, same-sheet 4.5094087919).

**Flat-bulk gate (same code path, A = D = 1): PASSED EXACTLY.** The full cap-ride minimisation on a flat bulk returns T_bulk = 2.0 for z_a = 1, t_brane = 2.0, **gain = 0.0, relative error 0.0** (bar ≤ 1e-10). (First attempt returned 2.0082 because the slope scan did not include p₀ = 0; the grid was fixed and the gate re-run clean — anatomy recorded in §7.)

---

## 2. Deciding numbers (mine)

Units r₀ = 1, c = 1. Gain = (t_brane − T_bulk)/t_brane. "Free depth" = cap y ≤ 0.455 (Phase 43's minimiser bound; slab edge row also given).

| pair | t_brane | T_bulk (mine) | **gain (mine)** | u_eff | Phase 43 checked read | Phase 43 nseg-24 stored |
|---|---|---|---|---|---|---|
| cross z_a = 0.5 | 2.913526 | 1.642818 | **0.4361** | 1.774 c | 0.422 (T 1.6841) | 0.4841 (T 1.5032) |
| cross z_a = 1.0 | 6.278422 | 3.264644 | **0.4800** | 1.923 c | 0.480 (T 3.2618) | 0.5065 (T 3.0986) |
| cross z_a = 2.0 | 15.297239 | 10.883336 | **0.2885** | 1.405 c | 0.177 (T 12.5837) | 0.3583 (T 9.8160) |
| cross z_a = 1.0, cap 0.46 (slab edge) | 6.278422 | 3.189436 | **0.4920** | 1.969 c | — | — |
| same-sheet z = 1 → 2 | 4.509409 | ≈ 4.50856 (composite, §4) | **≈ 0.00019** | — | 0.00025 | 0.00025 |

**Cap scan at z_a = 1 (mine vs Phase 43's coarse cap reads in p431_check.json):**

| cap y ≤ | gain (mine) | gain (Phase coarse) |
|---|---|---|
| 0.20 | **0.0665** | 0.068 |
| 0.30 | **0.1664** | 0.171 |
| 0.40 | **0.3481** | 0.371 |
| 0.455 | **0.4800** | 0.509 |

Monotone growth with cap confirmed; every optimum sits **at** its cap (z₁ and p_at_cap recorded in the JSONs), and the cap-0.46 row exceeds the cap-0.455 row — the infimum over the open slab is **not attained inside the existing bulk**; it lives at the singular boundary y* ≈ 0.4675, exactly as the claim states. All quoted gains are cap-labelled.

**Internal convergence (my own path, two resolutions):** the headline row at production tolerance (DOP853, rtol 1e-11, max_step 0.02) gives T = 3.26464392199692; at loose tolerance (rtol 1e-9, max_step 0.05) T = 3.26464392198313 — agreement to **4 × 10⁻¹² relative**. The z_a = 2 row computed under both field representations agrees to 0.03% in T (§3.4).

---

## 3. Reconciliation of the stored numbers

### 3.1 Headline: 0.480 vs 0.506 — the continuum gain is ≈ 0.480
My converged z_a = 1 value is **gain 0.4800 (T = 3.2646)**, agreeing with Phase 43's nseg-48 refinement (0.48047, T = 3.2618) to 0.09% and with its ×10-subdivision read (0.47976) to 0.05%. The stored nseg-24 row (0.5065, T = 3.0986) is the coarse midpoint-rule artefact Phase 43's own checker diagnosed (midpoint quadrature on segments spanning the throat's rapid scale variation understates T). **Deciding number: gain(z_a = 1, cap 0.455) = 0.480 ± 0.002** (error budget: integrator 4e-12; field-representation ±0.001 in gain, §3.4; slope-refinement ≲ 0.1% in T). u_eff = **1.923 c** (the claim's 1.92 c ✓).

### 3.2 z_a = 0.5: mine 0.4361 vs Phase subdivided 0.4219
Phase's "checked" 0.422 was the ×10-subdivision **re-evaluation of the coarse path**, not a re-minimisation — an upper bound on T, hence a lower bound on gain. My geodesic arc + ride path is genuinely better (T = 1.6428 < 1.6841), so the converged gain is slightly **larger**: **0.436 ± 0.004**. Sign, size, and ordering all agree; the row survives with the number updated.

### 3.3 z_a = 2: the quoted 0.177 does NOT survive — converged ≈ 0.289
Phase's stored z_a = 2 path is visibly tangled (its stored node sequence jumps non-monotonically in z along the cap segment), and its subdivided time T = 12.5837 is merely that path's true time — again an upper bound, here a loose one. The nseg-24 number (T = 9.8160, gain 0.3583) errs the other way (midpoint understatement, the largest of the three rows at 28%). My clean symmetric arc + ride optimum gives **T = 10.8833 (spline) / 10.8797 (linear fields), gain 0.2885 / 0.2888** — between the two Phase numbers and consistent under both field representations. **Deciding number: gain(z_a = 2, cap 0.455) = 0.289 ± 0.003.** The claim's z_a = 2 row must be restated with this value (§6). This does not weaken the claim's substance — the true gain is larger than quoted — but the quoted figure is wrong as a converged value and cannot be uploaded as-is.

### 3.4 Field-representation sensitivity
Re-evaluating my optimal paths under Phase 43's linear interpolant (paths not re-optimised there, so these are upper-bound-style evaluations; the rest-run also re-scanned the slope under the spline and evaluated at the scan optimum): z_a = 1: T_linear = 3.2624, gain **0.4804** (vs spline 0.4800). z_a = 2: T_linear = 10.8797, gain **0.2888** (vs spline 0.2885). The gain is representation-insensitive at the ±0.001 level; the z_a = 2 correction in §3.3 is **not** a representation artefact.

---

## 4. Controls

**Same-sheet control (z = 1 → 2, stored gain 0.00025491501821169304): REPRODUCED at ≈ 0.0002.**
Anatomy, from my scans (`wc_g63_scans.py`): the single smooth geodesic between the endpoints (midpoint shooting, y₀ = 0.0332) has T = 4.9326 — *worse* than the brane path; it is a non-minimal stationary path and is not the control's minimiser. The minimiser is a composite: a shallow geodesic dive arc from (1, 0) that returns to the brane at z_r, plus the brane segment z_r → 2. Dive arcs beat the brane over their own span by only ~10⁻⁴ relative (arc − brane = −1.8e-5 … −3.7e-3 over spans 0.19…1.74, changing sign for steep arcs). Best composite found (slope 0.2 arc returning at z_r = 1.9119, T_arc = 4.041714, plus brane remainder 0.466846): **T = 4.508560, gain = 1.9 × 10⁻⁴**, vs stored 2.55 × 10⁻⁴ — agreement in size, both ≈ 0. The gain is a throat phenomenon, not a generic bulk effect: **throat-specificity confirmed.**

**Forced-depth table (stored forced_depth_za1: gains 0.296 @ Y=0 … 0.501 @ Y=0.4): NOT a geodesic object — comparison superseded by the cap scan.** My classification scan of every geodesic arc launched from (1, 0) toward the throat plane shows **no arc reaches z = 0 aloft inside the slab**: slopes |p₀| ≤ 3 return to the brane at z_return ∈ [0.298, 0.731] (peak heights ≤ 0.39); slopes |p₀| ≥ 4.5 exit the slab top (y = 0.46) at z ∈ [0.70, 0.89] first. So a path pinned through (0, Y) has no geodesic-arc representative at any Y > 0; Phase 43's forced-depth rows are cornered discrete paths (valid variational upper bounds under a pinning constraint, not geodesic times). The claim's depth hedge does not rest on that table — it rests on the cap sequence, which I reproduce (§2). No restatement needed on this account, but the forced-depth table should not be quoted as geodesic data.

**Flat gate:** exact zero (§1). **Mechanism check (raw fields):** D/A at the throat falls 2.828 → 0.231 between y = 0 and y = 0.45 while at z = 1 it falls only 3.71 → 2.80 — the pinch is at the throat, matching the claim's mechanism and the control.

---

## 5. Novelty

**Verdict: PARTIALLY KNOWN.** The shortcut concept, its graviton-only carrier, and quantitative shortcut measurements in other bulks are all published. The specific measurement claimed here was not found.

### 5.1 Search log (queries verbatim; sources checked: arXiv, INSPIRE-HEP, Semantic Scholar, general web)

1. `Chung Freese bulk shortcut graviton propagation brane world faster than brane light`
2. `bulk geodesic shortcut braneworld wormhole throat null geodesic gain`
3. `"shortcut" bulk geodesic wormhole brane world traversable throat graviton faster brane`
4. `Caldwell Langlois "Shortcuts in the Fifth Dimension" arXiv hep-ph`
5. `Chung Freese "Can geodesics in extra dimensions solve" arXiv 9912346 OR 9910235`
6. `null geodesics bulk shortcut Morris-Thorne wormhole embedded brane world 5D lift travel time`
7. `INSPIRE-HEP shortcuts fifth dimension graviton bulk geodesic Ishihara null geodesics anti-de Sitter brane`
8. `Semantic Scholar "shortcut" graviton bulk brane wormhole throat signal arrival time comparison`
9. `"bulk singularity" wormhole brane world Gaussian normal coordinates geodesic shortcut signal`
10. `Ishihara "gravitational signals" null geodesics five-dimensional anti-de Sitter shortcut horizon radius`
11. `"wormhole" brane world "shortcut" graviton arrival time earlier photon quantitative gain fraction`

Queries 2, 3, 6, 9, 11 were aimed directly at the wormhole-throat version of the question; they returned the cosmological/domain-wall/AdS-black-hole shortcut literature and braneworld-wormhole *solution* literature (e.g. Bronnikov–Kim, arXiv:gr-qc/0212112), but **no measured cross-throat shortcut gain in a wormhole bulk, no same-sheet throat-specificity control, and no unattained-infimum-at-a-bulk-singularity structure**.

### 5.2 Near neighbours (the known part, cited)

- **Chung & Freese**, "Can geodesics in extra dimensions solve the cosmological horizon problem?", Phys. Rev. D 62 (2000) 063513, **arXiv:hep-ph/9910235** — the shortcut concept: extra-dimensional null geodesics connecting brane points faster than brane-confined signals. *(Citation correction for the gate record: the brief and GATE6.md's parent record cite hep-ph/9912346; every citing source I found — the paper's own arXiv listing, Chung's CV, and multiple citing papers — gives hep-ph/9910235 for this paper. I could not verify 9912346 as this paper's ID.)*
- **Caldwell & Langlois**, "Shortcuts in the Fifth Dimension", Phys. Lett. B 511 (2001) 129, **arXiv:gr-qc/0103070** — quantified graviton shortcuts vs brane photons in AdS₅ cosmology.
- **Abdalla, Casali & Cuadros-Melgar et al.**, "The shortest cut in brane cosmology", Phys. Rev. D 65 (2002) 083512, **arXiv:hep-th/0109024** — derives the shortest-bulk-path ODE and compares photon vs graviton arrival times/redshifts numerically in cosmological branes (and finds *no* shortcut for the RS vacuum brane — the flat-brane zero, consistent with Phase 2 W3).
- **Abdalla et al.**, "Shortcuts for Graviton Propagation in a Six Dimensional Brane World Model", **arXiv:hep-th/0205203** — numerically solves the shortest-graviton-path equations in AdS-Schwarzschild / AdS-Reissner–Nordström bulks, with shortcut examples.
- **Abdalla & Cuadros-Melgar**, "Shortcuts in domain walls and the horizon problem", Phys. Rev. D 67 (2003) 084012, **arXiv:hep-th/0209101**; and "Shortcuts in Cosmological Branes", **arXiv:hep-th/0501076** — shortcuts "usually appear under mild conditions"; some primordial cases "quite effective" (cosmological, horizon-problem framing).
- **Leach & Lesame**, "Conditional escape of gravitons from the brane", **arXiv:gr-qc/0502109** — conditions for bulk null geodesics to return to an FRW brane and for shortcuts (ρ_b + p_b > 0 bending condition).
- **Dai & Stojkovic**, "Superluminal propagation along the brane in space with extra dimensions", Eur. Phys. J. C 84 (2024) 175, **arXiv:2306.04069** — bulk signal beating brane light via differential Shapiro delay near a massive brane; constrained with GW170104. (A delay-difference mechanism, not a throat pinch.)
- Also noted: Greene, Kabat, Levin & Menon, "Superluminal propagation on a moving braneworld", Phys. Rev. D 106 (2022) 085001 (bulk shortcuts from brane motion); Päs, Pakvasa & Weiler, arXiv:hep-ph/0504096 (sterile-neutrino shortcuts — a non-graviton carrier proposal in asymmetrically warped models, different construction).

In all of these the bulk is a cosmological brane, a domain wall, or an AdS black-hole bulk — **none is a Morris–Thorne-type throat on the brane with its own constructed Gaussian-normal bulk lift**, none poses the two-point problem *across a throat between its two sheets*, and none reports the gain's infimum sitting at a bulk curvature singularity that terminates the slab.

### 5.3 The novel part, delimited in one quotable sentence

> "What is new here is not the bulk shortcut — it is the first measured shortcut gain inside an exhibited wormhole-throat bulk lift: a cross-throat gain of 0.480 (cap y ≤ 0.455 r₀) between the throat's two sheets, shown to be throat-specific by a same-sheet control of ≈ 0.0002, with the gain's infimum provably unattained inside the bulk because it lives at the bulk curvature singularity that ends the slab."

(The claim's novelty, if any, is the measurement in this constructed bulk — not the shortcut concept, which is Chung–Freese's.)

---

## 6. Exact restated wording (the form in which the claim survives)

> **G6-3 (P43-1), restated:** In the P29-3 constructed Gaussian-normal bulk lift of the exhibited √-shape braneworld throat (brane metric Φ = 0, b(r) = r₀√(r/r₀); slab y ∈ [0, 0.46] r₀, bulk curvature singularity at the throat at y* ≈ 0.4675 r₀), a cross-throat bulk null geodesic between brane points z = ∓z_a beats brane-confined light by a fractional gain of **0.480 at z_a = 1** (brane time 6.2784 r₀/c → bulk 3.2646 r₀/c, u_eff = 1.92 c, depth cap y ≤ 0.455 r₀), **0.436 at z_a = 0.5**, and **0.289 at z_a = 2** (all cap-labelled at y ≤ 0.455 r₀; independently reproduced by geodesic-ODE shooting, flat-bulk gate exact). The gain is throat-specific (same-sheet control gain ≈ 0.0002), grows monotonically with the depth cap (0.067 at y ≤ 0.20, 0.166 at y ≤ 0.30, 0.348 at y ≤ 0.40, 0.480 at y ≤ 0.455, 0.492 at the slab edge y ≤ 0.46), and its infimum is **not attained** inside the existing bulk — it lives at the singular boundary. **EFFECTIVE ONLY** under C12: formation of throat+bulk has no classical route (Phase 28), so the setup leg is unavailable, not merely losing; the carrier is graviton-only.

Changes from the claim as tasked: (i) z_a = 2 gain 0.177 → **0.289** and z_a = 0.5 gain 0.422 → **0.436** (converged values; §3.2–3.3); (ii) cap sequence extended with the 0.40 row (0.348) and the slab-edge row (0.492); (iii) bulk time at z_a = 1 stated as 3.2646 (my converged value; Phase's 3.2618 is within 0.09%). Headline 0.480, u_eff 1.92 c, control ≈ 0.00025 → ≈ 0.0002, and every hedge are unchanged in substance.

---

## 7. Instrument-failure anatomies (gate-run honesty)

1. **Flat-gate scan gap (caught by the gate itself):** first flat run returned gain −0.0041 because the slope scan omitted p₀ = 0. Grid fixed; gate re-run exact (0.0). The gate did its job.
2. **Steep-slope crawl:** geodesics that turn vertical in the z-parametrisation (p → ∞) stall DOP853. Fixed with a |p| = 60 turn-guard event (turned slopes are assigned infinite time; they are never optima here).
3. **Linear-eval stall:** re-integrating an arc without the cap event lets the trajectory exit the stored grid (y > 0.46), where spline extrapolation stalls the ODE. Fixed by stopping at the cap event; the evaluation then completes in ~3 s.
4. **A superseded prototype read:** an early killed prototype run reported smooth-crossing values (y_at_0 = +0.247 at slope −0.5) that three later independent executions (direct IVP, solver shooting, prototype-function rerun — rhs implementations verified pointwise identical) all contradict (y_at_0 = −0.5477, i.e. the geodesic returns to the brane at z = 0.357 and crosses into the mirror). The deciding cap-ride results are unaffected: they agree with Phase 43's independent minimiser at every comparable point (headline T within 0.09%, cap entries z₁ ≈ 0.70 vs 0.73, cap gains 0.067/0.166 vs coarse 0.068/0.171).
5. The main solver was stopped twice under severe VM CPU contention (other agents' work; ~4–10% CPU share) and its remaining rows finished by the lean rerun and scans scripts; the main run's completed numbers were transcribed from its log into `wc_g63_numbers_main.json` with the transcription cross-checked (gain = 1 − T/t_brane reproduces every logged gain).

---

## 8. Bottom line for the coordinator

- Correctness: **REPRODUCED WITH RESTATEMENT** — deciding numbers: gain(z_a = 1, cap 0.455) = **0.480 ± 0.002** (T = 3.2646, u_eff = 1.923 c); gain(z_a = 0.5) = **0.436**; gain(z_a = 2) = **0.289** (not 0.177); caps 0.067 / 0.166 / 0.348 / 0.480 / 0.492 (caps 0.20 / 0.30 / 0.40 / 0.455 / 0.46); same-sheet control **≈ 0.0002**; flat gate **exact 0.0**.
- Novelty: **PARTIALLY KNOWN** — concept and other-bulk measurements published (hep-ph/9910235; gr-qc/0103070; hep-th/0109024; hep-th/0205203; hep-th/0209101; hep-th/0501076; gr-qc/0502109; arXiv:2306.04069); the throat-lift measurement + control + unattained-infimum structure not found. One citation correction flagged: Chung–Freese is hep-ph/**9910235**, not 9912346.
- Gate verdict: **UPLOAD-READY AFTER RESTATEMENT** (restated wording in §6, hedges intact: cap-labelled, infimum not attained, EFFECTIVE ONLY, graviton-only).
