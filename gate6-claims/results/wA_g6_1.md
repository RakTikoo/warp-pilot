# GATE-6 — Worker W-A report: Claim G6-1 (P26-1, the β = 0.07 shell + β = 0.08 boundary)

**Worker:** W-A · **Date:** 2026-11-22 · **float64 everywhere** · nothing uploaded, no external contact.
**Code (fresh, in `gate6/`):** `wa_auditor.py` (auditor), `wa_run.py` (anchors / main audits / ladder), `wa_diag.py` (point-level confrontation), data `wa_results.json`, logs `wa_main.log`, `wa_ladder.log`.
**Metric definition:** imported from `shell.py` (`build_shell` + `shell_point_factory`) only — the Gate-5 shared-definition precedent. **`verify_metric.py` was not used anywhere** (not imported, not run).

## Verdicts (summary)

| Axis | Verdict |
|---|---|
| Correctness, β = 0.07 configuration | **REPRODUCED** |
| Correctness, β = 0.08 boundary / "ceiling = 0.07" | **NOT REPRODUCED** — the β = 0.08 failure is an artefact of the Phase-26 machinery at one point; the continuum inner-edge NEC at β = 0.08 is **positive** |
| Correctness, claim as a whole | **REPRODUCED WITH RESTATEMENT** (exact wording in §5) |
| Novelty | **PARTIALLY KNOWN** (exact known parts cited in §4) |
| **GATE VERDICT** | **UPLOAD-READY AFTER RESTATEMENT** |

---

## 1. My independent second path

Phase 26's deciding machinery was `verify_metric.einstein_at_points`: 4th-order FD on the metric → Christoffel symbols at shifted points → a second 4th-order FD applied to Γ (nested stencils).

Mine (`wa_auditor.py`) is a different discretisation in kind, not just in order:

- **2nd-order central FD for first AND second metric derivatives directly** (diagonal ∂²: (f₊ − 2f + f₋)/h²; mixed ∂²: 4-point stencil /4h²).
- **∂Γ computed algebraically** from ∂g, ∂²g and ∂g⁻¹ = −g⁻¹(∂g)g⁻¹. No nested Γ stencil exists anywhere in the code.
- Fresh Eulerian-tetrad transform, fresh Hawking–Ellis eigenvalue margin code, fresh Fibonacci sampled-null NEC cross-check (162 directions).

### Anchors (run FIRST; all passed before any β = 0.07 number was read)

1. **Minkowski control:** max |G| = 0.0 exactly.
2. **Static (β = 0) spherical exact anchor** — my Cartesian-FD eigenvalues vs `shell.py`'s exact 1-D spherical T (ρ_ex, p_r, p_t) for the claim's own profile, at r = 12, 15, 20, 25, 28:
   - ρ relative error ≤ 3.1e-03 at h = 0.3, ≤ 7.6e-04 at h = 0.15 (clean ~h² scaling, as a 2nd-order code should show);
   - principal-pressure absolute error ≤ 9.2e-08 (h = 0.3), ≤ 2.3e-08 (h = 0.15) — i.e. ≲ 1% of the smallest core margin in dispute;
   - Type-I at every anchor point.
3. **Finalist A positivity** (M = 2.0, (10,20), β = 0.02, full fine-style point set, h = 0.3): whole-volume worst margin **+2.14e-07** (positive), Type-I fraction **1.000**, core NEC +3.08e-05 @ r = 10.25 — same signs, same site class, same orders as the Phase-1/26 record (their whole-volume worst +1.11e-07, tail-limited).

The auditor is therefore validated on an exact solution and on a stored positive anchor before use.

## 2. β = 0.07 — my deciding numbers (1,404 pts, 26 Fibonacci directions, radii step 0.5 + inner-edge cluster, same set/threshold convention as Phase 26's fine audit)

| Quantity | Claim (Phase 26) | Mine h = 0.3 | Mine h = 0.15 |
|---|---|---|---|
| Whole-volume worst (SEC, r = 37.0 tail) | +2.591e-07 / +2.593e-07 | **+2.580e-07** | **+2.590e-07** |
| Whole NEC / WEC / DEC (r = 37.0) | +4.349e-07 / +4.350e-07 | +3.611e-07 | +4.166e-07 |
| Core NEC (r = 10.25) | +3.756e-05 / +3.280e-05 | **+3.730e-05** | **+3.729e-05** |
| Core WEC (r = 10.25) | +3.525e-05 / +3.280e-05 (ledger values) | **+3.513e-05** | **+3.513e-05** |
| Core DEC (r = 10.25) | +1.974e-05 / +1.779e-05 | **+1.943e-05** | **+1.965e-05** |
| Type-I fraction (significant set) | 1.000 | **1.000** | **1.000** |
| Core sampled-null NEC min | +1.238e-05 / +9.31e-06 | **+1.223e-05** | **+1.223e-05** |
| FD floor (my non-significant-point median \|NEC\|) | 2.6e-08 (theirs) | 1.6e-08 | 2.3e-08 |

Agreement: same signs everywhere; whole-volume worst within 0.4%; core margins within the claim's own h-pair spread (Phase 26's core NEC itself moved 3.76e-05 → 3.28e-05 between h = 0.3 and 0.15; mine is h-stable at 3.73e-05). Worst margin ≈ 10–16× my measured FD floor. **β = 0.07: REPRODUCED.**

(Record note: the checkpoint text quotes core WEC +3.28e-05 at h = 0.3; the ledger's h = 0.3 core WEC is +3.525e-05 and +3.28e-05 is the h = 0.15 core NEC/WEC. My numbers track the ledger, not the checkpoint's rounding mix-up. No physics consequence.)

## 3. THE β = 0.08 BOUNDARY — settled: 0.08 PASSES; the Phase-26 ceiling is wrong

### 3.1 The h-ladder (inner edge, radii 9.75–11.50 step 0.25, 26 directions, minimum NEC over the region)

| h | β = 0.08 min NEC (eigenvalue) | β = 0.08 min sampled NEC | β = 0.07 min NEC (control) |
|---|---|---|---|
| 0.3 | +1.7723e-05 | +2.8635e-06 | +3.7302e-05 |
| 0.15 | +1.7697e-05 | +2.8653e-06 | +3.7292e-05 |
| 0.075 | +1.7675e-05 | +2.8587e-06 | +3.7284e-05 |
| 0.0375 | +1.7670e-05 | +2.8571e-06 | +3.7282e-05 |
| **Richardson h→0** | **+1.7668e-05** | **+2.857e-06** | +3.7281e-05 |

The minimum sits at r = 10.25 at every h. Richardson pairs (h, h/2) extrapolate to +1.7688e-05, +1.76679e-05, +1.76679e-05 — the two finest pairs agree to 4e-11. **Continuum inner-edge NEC at β = 0.08 = +1.767e-05 ± 1e-07 (conservative), i.e. POSITIVE, ~34× larger in magnitude than, and opposite in sign to, Phase 26's −5.26e-07.** Per-radius minima are positive at every radius 9.75–11.50 and every h (worst radius is 10.25 throughout).

### 3.2 Point-level confrontation at Phase 26's exact suspect point (−1.2926, 9.9753, −1.9712), r = 10.25, β = 0.08

Phase 26 (h = 0.15) found this point **non-Type-I** with sampled-fallback NEC **−5.26e-07** — the single point on which the β = 0.08 failure, and hence the 0.07 ceiling, rests. With two different discretisations of my own:

| Method | h = 0.3 | h = 0.15 | h = 0.075 |
|---|---|---|---|
| My 2nd-order direct-∂² auditor: NEC | +2.160e-05 | +1.942e-05 | +1.943e-05 |
| My 4th-order direct-∂² variant (`wa_diag.py`): NEC | +5.895e-06 | +1.861e-05 | +1.943e-05 |
| Type-I (both methods, all h) | yes | yes | yes |
| Sampled NEC (2nd-order, h = 0.075) | — | — | +3.379e-06 |

Both of my methods converge to NEC ≈ **+1.94e-05**, Type-I, at that point. The Phase-26 value does not reproduce under either discretisation, at any h. It is an artefact of the Phase-1 nested-Γ-stencil machinery at that single point (the mechanism inside their code was not further diagnosed — `verify_metric.py` was off-limits to this gate — but two independent discretisations plus an h-ladder leave no continuum feature there to explain).

### 3.3 β = 0.08 whole-volume audit (same 1,404-pt set as §2)

| | Mine h = 0.3 | Mine h = 0.15 |
|---|---|---|
| Whole-volume worst (SEC, r = 37.0) | +2.580e-07 | +2.590e-07 |
| Core NEC / WEC (r = 10.25) | +1.772e-05 | +1.770e-05 |
| Core DEC (r = 10.25) | +1.279e-05 | +1.307e-05 |
| Type-I fraction | 1.000 | 1.000 |
| Core sampled-null NEC min | +2.864e-06 | +2.865e-06 |

**Verdict on 0.08, stated plainly: β = 0.08 PASSES the full audit on the independent second path. The Phase-26 ceiling "β = 0.07" is wrong; the H-a ceiling is ≥ 0.08.** Follow-up owed (out of this gate's scope): Phase 26's β = 0.09 fine row failed at the *same suspect point* (−1.10e-06, h = 0.15) and should be re-audited before any ceiling above 0.08 is quoted either way; β = 0.10's failure was mid-shell and h-stable and is not impeached by this finding.

## 4. Novelty

### 4.1 Search log (every query verbatim; sources: web search over arXiv / IOP / publisher pages, arXiv abstract + HTML full text, academia.edu; INSPIRE-HEP and Semantic Scholar were reached via the arXiv records' linked indexes — no separate native INSPIRE/Semantic-Scholar session was available in this environment, noted as a coverage limit)

1. `Fuchs et al 2024 constant velocity physical warp drive solution positive energy shell`
2. `warp drive satisfies all energy conditions NEC WEC SEC DEC subluminal positive energy`
3. `Bobrick Martire 2021 introducing physical warp drives energy conditions arXiv 2102.06824`
4. `arXiv 2405.02709 Fuchs constant velocity warp drive shell velocity ADM mass parameters`
5. `Fell Heisenberg 2021 positive energy warp drive Lentz solitons energy conditions critique`
6. `Warp Factory arXiv 2404.03095 analyzing warp drive spacetimes energy conditions toolkit`
7. `Santiago Schuster Visser generic warp drives violate null energy condition arXiv 2105.03079`
8. `Lentz 2021 breaking the warp barrier hyper-fast solitons positive energy densities arXiv`
9. `warp drive velocity scan maximum speed energy conditions satisfied shell compactness optimization`
10. `"warp drive" shell thickness compactness velocity 0.07c OR 0.08c energy conditions numerical`
11. `INSPIRE-HEP Semantic Scholar positive energy warp shell subluminal all energy conditions 2025 2026`
12. `Procaccia optimized positive-energy warp shell beta 0.1363 energy conditions`
13. `"warp shell" optimized shift source first failure energy conditions 0.1363 companion`
Plus: full-text read of Fuchs et al. (arXiv HTML) and of the Procaccia certificate paper's text as indexed.

### 4.2 What is in the literature

- **The class itself is published.** Fuchs, Helmerich, Bobrick, Sellers, Melcher & Martire, "Constant velocity physical warp drive solution," *Class. Quantum Grav.* **41** (2024) 095013, **arXiv:2405.02709**: a constant-velocity subluminal matter shell + Alcubierre-like shift satisfying **all** energy conditions, positive ADM mass — the very construction `shell.py` implements (Fuchs §3). Their exhibited example is slow (v_s = 0.02 per Le's matched re-verification, arXiv:2602.18023 §3.6; a secondary survey quotes the EC-clearing member at 0.04c, shell 10–20 m, 4.49e27 kg). Framework: Bobrick & Martire, *CQG* **38** (2021) 105009, **arXiv:2102.06824** (first general subluminal positive-energy spherically symmetric warp-drive model). Toolkit: Helmerich et al., "Analyzing warp drive spacetimes with Warp Factory," **arXiv:2404.03095**.
- **"EC-legal above β = 0.05" is also published — and goes much higher.** F. Procaccia, "Continuum Energy-Condition Certificates for an Optimized Positive-Energy Warp Shell" (publicly posted **Oct 30, 2026**, academia.edu; unrefereed, no arXiv ID found) plus its companion optimisation paper: a Fuchs-form warp shell, **(R_in, R_out) = (10, 20) m, M = 6.0 geom (compactness 0.60), step density box-smoothed, zero radial pressure, spline-optimised radial shift source**, certified (interval/matrix certificates, 466,491 points; continuum cover of 4.6M cells in (r, θ, β)) to satisfy NEC/WEC/SEC/DEC at **every β from 0 to 0.1363**, with first failure bisected to β ∈ [0.1363285, 0.1363286] and a proven DEC+NEC violation at 0.1364. This predates Phase 26 (2026-11-21) and anticipates both "past 0.05" and "past 0.07" in a neighbouring design. (Its standard differs from ours — no TOV matter model is claimed, by the author's own scope note — but as prior art for the *existence and velocity reach* of EC-legal shells it is decisive.)
- **The 2021 positive-energy claims do not anticipate this claim:** Lentz, *CQG* **38** (2021) 075015, **arXiv:2006.07125**, and Fell & Heisenberg, *CQG* **38** (2021) 155020, **arXiv:2104.06488**, claim positive Eulerian energy density (WEC for one observer class), not all-observer all-EC legality; Santiago, Schuster & Visser, *Phys. Rev. D* **105** (2022) 064038, **arXiv:2105.03079**, prove generic Natário-class drives violate WEC/SEC/DEC (and NEC under subsidiary conditions) — a no-go for the unit-lapse flat-slice class that the non-unit-lapse, curved-slice shell family (Fuchs; ours) sits outside.
- **Independent 2026 scrutiny cuts the other way and must be carried as a caveat, not a novelty item:** Le, "On the boundary cost of source-consistent warp shells," **arXiv:2605.25417** — frame-independent re-verification of the Fuchs shell confirms interior EC compliance but reports Hawking–Ellis Type-IV violations in the smoothing tail beyond the nominal shell, and a 600-configuration compactness/thickness scan finds no admissible configuration in two *source-first* ansatz classes under a stricter five-criterion source-consistency standard. That standard (explicit matter model + constraint satisfaction) is stricter than the prescribed-geometry audit standard used by Fuchs, Phase 26, and this gate alike; it does not refute the claim under its own stated standard, but any upload should cite it.

### 4.3 Novelty verdict: PARTIALLY KNOWN

Known: (i) fully-EC-legal subluminal warp shells (Fuchs et al. 2024); (ii) EC legality at β > 0.05, indeed to β = 0.1363, in an optimised (10,20) design (Procaccia 2026). Not found anywhere in the searched literature: the specific configuration audited here — a **TOV-constructed thick shell (W = 2R₁), compactness 0.80, edge-peaked density, cosine shift** — nor its margin ledger, nor a β-ladder mapped inside the TOV/Fuchs named family.

**The novel part, in one quotable sentence:** "What is new is only the specific thick-shell TOV configuration — (R₁,R₂) = (10,30), M = 8.0 geometric units at compactness 0.80, edge-peaked density with cosine shift — shown by two independent discretisations to satisfy all four energy conditions at β = 0.07 and β = 0.08; EC-legal subluminal shells as a class, and EC legality above β = 0.05, are already in the literature."

## 5. Exact restated wording (the form in which the claim survives)

> "Within the Fuchs et al. (2024) TOV-shell family, the thick-shell configuration (R₁,R₂) = (10,30), ADM mass M = 8.0 geometric units = 1.0773×10²⁸ kg (compactness M/R₁ = 0.80), edge-peaked density (wd = 6.0, floor = 0.2), Gaussian smoothing (s_rho, s_P) = (4.0, 2.32), cosine shift on [10,30], satisfies NEC, WEC, SEC and DEC at every audited point (1,404 points, Hawking–Ellis Type-I fraction 1.000, whole-volume worst margin SEC +2.59e-07 in the exterior tail at r = 37.0, core margins NEC +3.73e-05 / DEC +1.94e-05 at r = 10.25) at β = 0.07 — and, on independent re-audit with an h-ladder to h = 0.0375 (continuum inner-edge NEC +1.767e-05), also at β = 0.08, so β = 0.07 is not the family ceiling. Fully EC-legal subluminal shells are known (Fuchs et al. 2024, arXiv:2405.02709), and a certified all-EC shell reaching β = 0.1363 in a different (zero-radial-pressure, shift-optimised (10,20)) design was publicly posted by Procaccia (Oct 2026); the novel content of this result is the specific TOV thick-shell configuration and its margin ledger, not the existence of EC-legal shells above β = 0.05."

## 6. Gate verdict

**UPLOAD-READY AFTER RESTATEMENT** — in the §5 wording only. The β = 0.07 configuration is independently reproduced; the "ceiling = 0.07" and any "first past 0.05" framing are both dead (the first by my §3 computation, the second by Procaccia 2026). Recommended follow-ups before any upload: (1) re-audit the β = 0.09 row, whose Phase-26 failure rests on the same impeached point; (2) cite Le arXiv:2605.25417's tail/source-consistency caveat alongside the claim.
