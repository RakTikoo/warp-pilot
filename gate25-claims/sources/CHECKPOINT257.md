# CHECKPOINT 257 — THE SPINOR SOURCING ATTEMPT

Phase 253 broke Phase 31's sign identity on spinor
interference and fenced what remained for a sourcing
attempt: full tensor match, EC health, budget/QI — in that
order. This phase ran the three legs in order, registration
and verdict forms before computation
(work/p257_registration.md), controls first. Item memos:
results/p2571_memo.md (Leg 1), results/p2572_memo.md
(Leg 2), results/p2573_memo.md (Leg 3). Drivers, checker,
results under work/ and results/.

## FTL VERDICT (leading): NO — but the sourcing obstruction loses its second leg

No grouped joint pass anywhere; Frontier A unchanged; drive
step 1 remains unachieved. What changed: the drive's
required stress at its worst site can now be matched, in
full, by a healthy classical field sector — the first sector
in the library of which that is true. The remaining
obstructions are size and duration (budget, QI) and global
existence, not algebra.

## LEG 1 — FULL MATCH AT THE SITE

Controls ALL PASS (C1 Phase 253 deciding configuration
exact; C2 stored rows exact; C3 floor recomputed; C4 the
pairwise full-tensor second path agrees with the bilinear
builder to 5.3×10⁻¹⁵).

**Type derivation.** Single Dirac modes are Type-I
(T_ab = p_(a j_b), both factors future causal; verified by
Segre classification of the probe modes). Superpositions
are NOT type-confined: their cross terms carry complex
transition currents, and in a 300-draw scan of the
registered family, **40 draws (13.3%) have a complex
mixed-eigenvalue pair (Type IV)**. The universal
real-spectrum floor (8.201×10⁻⁴ = 34.2% of |T_req|_F,
Phase 235 D3) therefore does not bind spinor
superpositions — the same interference that broke the sign
identity (Phase 253) breaks the type confinement.

**Fits.** Mode count is the sharp dial: N = 3 (Phase 253's
deciding set) and N = 4 stall at 3.13× / 1.84× the floor;
**N = 6 closes: constrained residual R = 1.767×10⁻¹⁶**
(contraction held to 6×10⁻¹⁴ relative), N = 8 / N = 12
confirm at 4.2×10⁻¹² / 6.1×10⁻¹¹. The winning six-mode
configuration (m = 1, positive-frequency, on shell;
persisted at work/p257_bestfit.json) reproduces T_req's
mixed eigenvalues (0.000676 ± 0.000820 i, 0.000113,
0.001042) — the Dirac field at the site IS the drive's
non-Type-I tensor. Independent checker (bilinear builder,
separate path): R = 1.768×10⁻¹⁶, all checks PASS.
Phase 244's named exit — "a healthy sector producing
non-Type-I stress, none in the registered libraries" — is
met at pointwise tangent-frame scope by the sector that
was in the library all along.

## LEG 2 — EC HEALTH: NET POSITION WORSE OR EQUAL (registered form; presupposition disclosed)

The audited configuration (Leg-1 winner, unit-normalised,
scaled by s² = 0.0078841 to carry the deficit) IS T_req at
the site (diff 1.8×10⁻¹⁶), so its own clause profile there
is the drive's: NEC −0.0038018, DEC violated, ρ negative.
Two substantive findings stand independent of framing:
(i) the tensor-matching configuration has NEGATIVE density
(ρ_unit = −0.0124) — Phase 253's positive-density property
belongs to the sign-only configuration; no configuration
here carries both legs; (ii) over a tangent patch the
field's stress oscillates off the match (patch NEC min
−0.0223, 5.9× the site deficit; ρ up to +0.092) — the match
is a point match, and the global-existence cost is not
retired.

The registered net sum (T_req + s²T_Dirac) is 2·T_req by
construction under a full match — its "worse" verdict
prices the double-count, disclosed on the memo's face. The
sourcing-semantics remainder T_req − s²T_Dirac is zero at
float64 class (‖·‖_F = 1.8×10⁻¹⁶): at the site, nothing is
left for other matter to supply. Sampler disclosure: this
phase's all-boost WEC read finds −0.188 for T_req vs the
record's restricted-observer margins read −0.0362; both
reported, within-phase comparisons use one sampler.

## LEG 3 — BUDGET/QI SKETCH: THE LINE DOESN'T MOVE

Per-site amplitudes: s² = 0.00788 / 0.00779 / 0.00340 /
0.01012 at the four sites (22.6× the sign-only
configuration's amplitude² at the worst site — the tensor
leg costs amplitude and the positive density). A
shell-wide realisation would carry exactly the drive's
budget (−2.5903) by definition — the spinor adds no
reservoir and needs none at pointwise scope; no shell-wide
field is constructed. QI: R_diff prices the total stress,
whoever supplies it: **2852.41 → 2852.41, unchanged
identically.**

## SYNTHESIS

- The drive's sourcing problem had four legs: sign (Phase
  253: broken, spinors), type (this phase, Leg 1: matched
  in full at the worst site), health/global existence
  (Leg 2: pointwise profile = T_req's own; patch and
  on-background existence still open and priced), and
  budget/QI (Leg 3: unmoved — they price T_req itself).
  The two ALGEBRAIC legs are retired at pointwise scope;
  the two SIZE legs are untouched, and they were always
  the larger numbers.
- What a spinor drive would still need: a global on-shell
  Dirac field on the Alcubierre background whose stress
  tracks T_req through the shell (the pointwise fits are
  per-site tangent data; the patch read prices the local
  oscillation such a field must suppress), and a QI/budget
  answer that no sourcing sector can supply, because both
  price the target tensor itself.
- Net for the drive line: the "cannot be sourced by any
  healthy sector" statement is dead — it survives only as
  "cannot be afforded": budget ≈ 2.21–2.59 geometric units
  and R_diff ≈ 2852 stand exactly as Phase 235/244 left
  them, now attributable to a concrete classical field
  configuration at the deciding site instead of to no
  field at all.

## NAMED FOLLOW-UPS (none launched)

(i) Global existence: extend the per-site fits to an
on-shell Dirac field on the whole background (spin
connection, mode mixing — Phase 253 fence (b); the patch
oscillation priced in Leg 2 is its local face).
(ii) Multi-site simultaneous fit: one configuration
matching T_req at all four deciding sites at once (the
Leg-3 sketch applied the worst-site configuration in each
site's frame; a joint fit is the honest version).
(iii) Gate-grade re-judgement of the Leg-1 full match, if
the parent wants the type-leg retirement at gate scope.

Nothing was appended to NEW_PHYSICS_LEDGER.md; nothing
external was launched; writes are inside phase257/ only.
