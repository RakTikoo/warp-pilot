# P35-2 run record

Script: `phase35/p352_kappa_window.py` (float64, unattended,
single run, exit 0). Outputs: `results/p352_results.json`,
`results/p352_memo.md`, this record. CHECKPOINT35.md not edited.

## Pre-solve statements (registered before computing)

- Tidal bar (Phase 23, from `phase23/p233_ledger.py`): traveller
  gradient ≤ 4.905 s⁻² at v = 0.1 c; gradient = c²·Cmax/|κ|;
  Cmax = max(|radial|, |γ²v²·R_lθlθ|) at the throat; scaling
  family x = r₀²/|κ| = 0.5; |κ|* = c²·Cmax/4.905;
  r₀* = √(x·|κ|*).
- Mixture coefficient at PROFILE level (P35-1 Step B not landed;
  `phase35/results/` checked empty of P35-1 output before the
  run): C_rad = −(F′(r₀)/2)·Φ′(r₀), F′(r₀) = 2(1−x)/r₀ (Shaikh
  Eq. 41), Φ′(r₀) = [w/(1+w)]·2(2−f)/r₀ from the P33-3
  construction (fluid-2 conservation), giving
  C_rad(f, w) = −2w(2−f)/(1+w); transverse boosted coefficient
  −γ²v²·F′(r₀)/(2r₀) = −0.010101 per |κ|.
- Sign checks (P13-3), run before the grid: f = 0 with Phase 23's
  Φ_r = −√2 → C_rad = +1.000 (fluid value ✓); w = 0 → Φ′ = 0 →
  C_rad = 0 ✓ (prose: dust fluid 2 contributes no redshift slope).
- Grid: f ∈ {0 (gate), 0.5, 0.6, 0.75, 0.9} × w ∈ {0, 1/3, 1/2, 1}.

## Gate result

|κ|* recomputed 1.8323245×10¹⁶ m² vs stored 1.8323243×10¹⁶
(rel. err 1.5×10⁻⁷); r₀* 9.5716365×10⁷ m vs stored 9.5716358×10⁷
(7.3×10⁻⁸); gradient at 1 m 4.4937759×10¹⁶ vs 4.4937752×10¹⁶ s⁻².
PASS (≤1%). Φ′ formula vs all 28 stored P33-3 rows: max abs err
4.4×10⁻¹⁶.

## Bound-audit sources (fetched in-run)

- Feng, Geng & Luo, arXiv:1810.06753v4 (Phase 3's Buchdahl
  source; abstract quoted in `phase3/results/p32_modgrav.json`):
  full text read — κ > 0 restriction (Sec. IIA), theorem
  assumptions (κ-energy condition ab ≥ 1; ρ̃, ρ_eff monotonic),
  10⁹ m² for typical NS, 10⁸ m² only for a future ~3 M⊙ NS.
- Avelino, PRD 85 (2012) 104053 (abstract via APS/search):
  existence-of-NS constraint; sign-blind |κ| form via
  l_f = √|κ| (Avelino 1207.4730 text), quoted by Sham et al.,
  ApJ 781 (2014) 66, as |8πκρ₀| ≲ 0.1 with both signs in use.
