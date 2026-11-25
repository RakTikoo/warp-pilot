# PHASE 303 — REGISTRATION: THE SPIN-1 FULL AUDIT

**Charge:** ledger entry 750 (Phase 298's charged successor; the
Phase 291→292 pattern executed for the Einstein-aether spin-1 /
vector mode). Written before any computation. This registration
is binding: verdict forms, controls, fiducial definitions and
the method ladder are fixed here, not chosen after results.

**Background (inputs, not re-derived):** Phase 298 Row 2
(`phase298/results/p298_memo.md` §3, `phase298/work/
p298_row2.py`): on the GW slice c₁₃ = 0, c_V² = c₁/c₁₄ and
α₁ = −4c₁₄ exactly (OMW Eq. 3.4 ≡ Jacobson Eq. 10, sympy-
verified); α₂ is exactly c₁-independent on the slice. Applied
fence (Phase 298 legs V1–V6): GW |c₁₃| ≤ 10⁻¹⁵ (sets the
slice); solar |α₁| ≤ 10⁻⁴ ⇒ 0 < c₁₄ ≤ 2.5×10⁻⁵; solar
|α₂| ≤ 10⁻⁷ (c₁-independent on the slice — constrains the
(c₂, c₁₄) plane only); BBN |G_cos/G_N − 1| ≤ 1/8 ((c₂, c₁₄)
plane only); Čerenkov c_V² ≥ 1 ⇒ c₁ ≥ c₁₄ (upward only);
stability q_V = c₁₄ > 0, q_S > 0, q_T > 0, mode-energy signs
> 0. Recorded-NOT-applied in Phase 298 (legs V7/V8): pulsar
α̂₁/α̂₂ (OMW Eqs. 3.8–3.9, 3.24–3.25; bounds |α̂₁| ≤ 10⁻⁵,
|α̂₂| ≤ 10⁻⁹, Shao–Wex 95%) and the binary-pulsar dipole /
orbital-decay maps (YBBY) — both run through Einstein-aether
sensitivities σ_æ that OMW state are not known in the post-GW
corner and defer explicitly; YBBY's (c₊, c₋) bands are pre-GW
with sensitivity fits over c₊ ∈ 3×(10⁻⁴, 10⁻¹),
c₋ ∈ 3×(10⁻⁵, 10⁻³), which do not cover the c₁₃ ≈ 0 slice.
Reference corners under the applied fence: **Corner A** —
(c₁, c₂, c₃, c₄) = (0.1, 2.500125×10⁻⁵, −0.1, −0.099975),
c₁₄ = 2.5×10⁻⁵ saturating solar α₁, c₂ on the α₂ = 0
branch-(ii) line, c_S = 1 exactly, **c_V = 63.2456**, carrying
c₋ = 2c₁ = 0.2; **Corner B** — c₁₄ = 7.9×10⁻⁹, c₁ = 0.08293104,
c₂ = 2/21 (BBN binding), **c_V = 3240 exactly** (parity with
the spin-0 row's fastest corner value).

## Controls (run first; a control failure stops the phase)

- **C-A:** re-running Phase 298's `p298_row2.py` fence
  evaluation reproduces Corner A (c_V = 63.2456, α₁ saturating
  at −10⁻⁴, α₂ = 0, all applied legs pass) and Corner B
  (c_V = 3240, BBN binding) at diff-0-class tolerance (same
  script, same frame — exact or last-digit agreement).
- **C-B:** the symbolic identities this phase builds on are
  re-verified in this phase's own script: c_V² = c₁/c₁₄ on
  the slice; the α̂ forms of OMW Eq. 3.9 reducing on the slice
  to the Eq. 3.24 forms with the slice's α₁, α₂ (the reduction
  Phase 292 verified for the khronometric reading — here
  re-verified as an identity in (c₁, c₂, c₁₄), since the
  spin-1 sector's σ_æ is a different function of the couplings
  even where the α̂ forms coincide).

## Item 1 — σ_æ for the spin-1 sector

Compute the neutron-star sensitivity as it enters dipole
radiation into the vector mode, in the post-GW corner
(c₁₃ = 0 slice), following Phase 292's method discipline.

**Method ladder (registered order, as in Phase 292):**
- Rung 1 — retrieval: the published Einstein-aether
  sensitivity formalism at primary-source grade (YBBY's EA
  sector; OMW; Jacobson §6), retrieved in full; every form
  used is quoted with its source equation number.
- Rung 2 — structural read: the weak-field anchor (the
  published s^wf form in the theory's α₁, α₂) evaluated on
  the slice; the published strong-field material (numerical
  TOV results / fitting formulas) used ONLY inside its
  stated validity region — any evaluation outside a fit's
  region is labelled an extrapolation on its face, exactly
  as Phase 292 labelled its Table I edge use; strong-field
  corrections carried as a bracket (Phase 292's f ∈ [0.5, 2]
  discipline, replaced by the EA literature's own stated
  deviation where it publishes one).
- Rung 3 — fresh TOV integration of the published EA system:
  only if rungs 1–2 do not decide the Item 2 questions at the
  bracket's width, and the phase states that it is running
  rung 3 and why before doing so.

**Structural difference, to be derived not assumed:** in the
khronometric sector σ_æ is a function of (c₁₄, c₂) on the
slice (Phase 292: σ_æ ≈ κ·c₁₄, κ = 2.2·C_*, no c₁ exists).
In the full theory the stellar structure couples to c₋ = 2c₁
on the slice (and to c₊ = c₁₃ off it), so σ_æ^EA is a priori
a function of (c₁, c₂, c₁₄; C_*). Where the weak-field anchor
is c₁-independent (it runs through α₁, α₂ only), the phase
states that as a derived weak-field fact and identifies which
published strong-field terms carry the c₁-dependence, with
their size at Corners A and B. If the computation cannot be
closed from published forms, the phase reports exactly where
it opens, and Items 2–3 proceed with σ_æ as a bracketed
unknown over the widest defensible range, every downstream
number stated as conditional on that range.

## Item 2 — the completed fence

Apply legs V7 (α̂₁, α̂₂ via OMW's exact forms with Item 1's
σ_æ; the isolated-pulsar α̂₂ bound's own caveat — YBBY decline
its direct mapping for want of the timed pulsars' masses —
carried exactly as Phase 292 carried it) and V8 (the YBBY
binary-pulsar dipole/orbital-decay analysis, applied at the
slice only to the extent its published forms reach the slice
without extrapolation; where a band rests on a fit outside
its region, that status is stated on the number, not buried).
Decide:
- **Corner A:** survives / shrinks (the new corner and the
  binding leg stated) / dies (the killing leg and the
  mechanism stated).
- **Corner B:** re-decided under the same completed fence.

## Item 3 — the channel priced

At the completed corner(s), in Phase 294/296's conventions
verbatim:
- **Fiducials (Phase 294's definitions, not re-chosen):**
  Hulse–Taylor class — m₁ = 1.44 M☉, m₂ = 1.39 M☉,
  P_b = 7.75 h, e_orb = 0.617, both stars at R = 12 km
  (ΔC_* from the fixed-radius compactness difference; equal
  compactness ⇒ dipole exactly 0, stated); GR quadrupole by
  Peters, computed (7.7808×10²⁴ W is the Phase 294 value the
  control must reproduce). NS–BH bound class — Phase 294's
  labelled maximal-asymmetry bound-class system, its Peters
  quadrupole computed (1.2696×10²⁵ W, circular).
- **Emission forms:** the spin-1 sector's own published flux
  forms (YBBY's Einstein-aether dissipative sector — the
  dipole coefficient runs through the vector mode speed
  w₁ = c_V and the scalar w₀ = c_S as published; the
  khronometric 𝒞 of Phase 292 is NOT reused, since it is the
  spin-0-only coefficient).
- **Rows:** the completed corner(s) at their own speed(s);
  spot rows at c_V ∈ {2, 10} — maximise the dipole ratio
  subject to c_V ≥ c* over the completed fence (Phase 296's
  pattern: the speed floor as an exact constraint on the
  couplings, binding legs named per row).
- Central model + envelope (the σ_æ bracket and the Δσ
  factor carried as Phase 294 carried them).

## Verdict forms (ledger 750, verbatim)

- **SURVIVES COMPLETED** — corner + prices stated; the memo
  enumerates what, if anything, remains recorded-not-applied.
- **SHRINKS AT COMPLETION** — the new corner and the binding
  leg stated.
- **DIES AT COMPLETION** — the killing leg and the mechanism
  stated.
Per-item verdicts are allowed where the items land
differently; the row's overall standing is stated in one
sentence at the memo's head.

## Standing rules

Registration + verdict forms before computation (this file);
controls first (above); published forms only, primary-source
grade; corner values never quoted as maxima of anything;
every caveat that prices a number rides on its face; the
leg-9-equivalent tolerance character of any dipole-map bound
used is stated where it binds. DESK: one-line summary in the
memo reporting the completed-fence outcome for the row.
Wording fence: signalling channel only — no transport,
cargo, or drive content; ratios are theory-space-corner
values for stated systems, never detection or detectability
claims. No ledger append, no launches, no user contact.
Deliverable: `phase303/CHECKPOINT303.md` +
`phase303/results/p303_memo.md`.
