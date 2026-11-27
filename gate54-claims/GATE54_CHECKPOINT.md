# GATE-54 CHECKPOINT — WORKING RECORD

Independent re-judgement of the Phase 410 claim set, charged at
ledger entry 1095 (2026-11-27). Deliverable claim set:
`gate54/GATE54.md` (§6 quotable: G54-A…G54-D, riders
G54-R1…G54-R3). This checkpoint is the working record: machinery,
controls, reads, admission, incidents. No ledger append, no
publication, no user contact by this gate — the verdict returns
to the parent (publication follows survival at the next free
version, v1.45.0).

## 1. Registration and frame

- Registration `gate54/work/g54_registration.md` written before
  any Gate-54 computation; ruling bars fixed in advance:
  (a) residuals ≤ 1×10⁻⁹ and σ_min rel diff ≤ 1×10⁻² per fit;
  (b) max |channel diff| ≤ 2×10⁻¹² with A2 SEC_min and A3
  SEC_trace diffs individually ≤ 1×10⁻¹²; (c) all densities
  positive and |a|² rel diff ≤ 1×10⁻⁹; (d) Gate-34-θ σ_min rel
  diff ≤ 2×10⁻² under at least one FD variant, 313-θ σ_min rel
  diff ≤ 1×10⁻² vs 0.0347527502565207; quotable-form ruling
  follows G36-C regardless of the numbers.
- Frame of record: VM `~/workspace/warp-pilot/venv`
  (numpy 2.5.5 / scipy 1.18.1) + Phase 166 pin, float64.
  Deciding reads on the VM.

## 2. Machinery (fresh organisation)

`gate54/work/g54_lib.py`, written for this gate alone:

- γ matrices in the Dirac representation by Kronecker products
  (γ⁰ = σ₃⊗I₂, γⁱ = iσ₂⊗σᵢ) — a different construction from the
  phases' np.block assembly.
- The superposition as an explicit FIELD FUNCTION ψ(X) with
  analytic mode-by-mode derivatives. NO pairwise S-matrix, NO
  T_from_S einsum, NO folded-amplitude shortcut in any deciding
  path (Phase 410 ran on the pairwise path). A separately
  written pairwise assembly exists only as the C1 cross-check.
- T_ab from the canonical symmetrised formula with L computed
  honestly, not assumed zero: |L| at the sites — Fit A
  [2.46×10⁻¹⁸, −2.07×10⁻¹⁸, 3.07×10⁻¹⁸]; Fit B ≤ 1.8×10⁻¹⁹.
- Own Hawking–Ellis classifier; own eigen-channel decomposition
  using Phase 410 SS4(ii)'s channel definitions (definitions are
  the claim's content; code is the gate's).
- Own FD Jacobians of the gate's own residual map: central
  h_j = 1×10⁻⁶·max(1,|θ_j|); forward variant for the Gate-34
  leg; h-stability spot check (h×10, h÷10) at Fit A.
- Driver `gate54/work/g54_run.py` (log `g54_run.log`); results
  `gate54/results/g54_results.json`. Laptop driver
  `gate54/work/g54_laptop.py`.

## 3. Controls (all before any claim read was believed)

- **C1 PASS.** Field-vs-pairwise max rel diff
  1.0238289108497418×10⁻¹³ ≤ 1×10⁻¹². Mode health: norm dev
  ≤ 6.9×10⁻¹⁸ (after the u†u = 2E|χ|² correction — §6);
  Dirac residuals 5.1577036902917074×10⁻¹⁷ (Fit A) /
  2.7755575615628914×10⁻¹⁷ (Fit B), exactly the phase's stored
  values (after the slash fix — §6).
- **C2 PASS.** Stored 320 winner: gate Rs
  [7.0105917748102985×10⁻¹⁵, 7.801736139349803×10⁻¹⁴,
  8.230855248120619×10⁻¹⁴, 1.2959002164511548×10⁻¹⁵], maxR
  8.230855248120619×10⁻¹⁴; σ_min gate 0.000399430073426119 vs
  stored 3.994300907411277×10⁻⁴ (rel 4.33×10⁻⁸); rank 40.
- **C3 PASS.** Stored 313 winner: gate maxR
  3.253291635019471×10⁻¹³ vs stored 3.253339860306391×10⁻¹³
  (abs diff 4.82×10⁻¹⁸).

## 4. Claim reads (VM, deciding)

**(a) Reproduction — SURVIVES.** Fit A gate residuals
[8.144×10⁻¹⁵, 2.763×10⁻¹³, 2.966×10⁻¹²] (stored
[8.146×10⁻¹⁵, 2.763×10⁻¹³, 2.966×10⁻¹²]); maxR gate
2.965982516552786×10⁻¹² vs stored 2.9659839407219894×10⁻¹².
σ_min gate 0.3857618160623069 vs stored 0.3857618146636974
(rel 3.6×10⁻⁹); σ_max 14944.163562989306; rank 30/30; blocks
202.7882 / 80.6668 / 35.2925 (all printed digits agree);
h-stability 0.3857618344922747 (h×10) / 0.385761815433645
(h÷10). Fit B gate residuals [9.110×10⁻¹⁵, 1.692×10⁻¹⁴,
2.305×10⁻¹⁴, 2.095×10⁻¹⁴, 7.928×10⁻¹⁵]; maxR
2.305490336342112×10⁻¹⁴ vs stored 2.3054719412020823×10⁻¹⁴.
σ_min gate 0.015432480949901446 vs stored
0.015432479500623982 (rel 9.4×10⁻⁸); rank 50/50; blocks
198.9305 / 209.3959 / 232.0209 / 258.7224 / 292.2305.

**(b) Decomposition — SURVIVES.** Max |channel diff| over all
channels × all eight reads: 1.3366521431357192×10⁻¹² (A3,
tangential channel). Per-site maxima: A1 2.57×10⁻¹⁵ · A2
3.85×10⁻¹³ · A3 1.34×10⁻¹² · B−1.0 1.07×10⁻¹⁴ · B−0.5
1.13×10⁻¹⁴ · B+0.0 3.71×10⁻¹⁴ · B+0.5 2.09×10⁻¹⁴ · B+1.0
1.40×10⁻¹⁴. A2 SEC_min diff +3.9×10⁻¹³ (value
−2.213557×10⁻⁴); A3 SEC_trace diff −9.0×10⁻¹³ (value
−3.388413×10⁻⁴). Both tensors Type-I at all eight reads on
the gate's classifier. Quotable bound: ≤ 1.34×10⁻¹² (the
phase checkpoint's own bound; gate 1.337×10⁻¹²).

**(c) Accounting — SURVIVES.** Densities positive at all 8
reads, matching the phase's to all printed digits (Fit A
+1.238993×10⁻⁴ / +3.956517×10⁻⁴ / +1.859720×10⁻³; stencil
+1.405987×10⁻⁴ / +1.319327×10⁻⁴ / +1.238993×10⁻⁴ /
+1.166924×10⁻⁴ / +1.101573×10⁻⁴). |a|² rel diff 0.0
(0.029266406597128584 / 0.021228149358339266). Per-site
implied s² agrees with |a|² to ≤ ~1×10⁻⁹ relative; gate s²
matches stored to 9 digits.

**(d) CTRL-313 — CONFIRMED; ruling in GATE54.md §5 / G54-D.**
Gate-34 θ: forward σ_min 0.027165249779697535 vs stored
0.027165249637030254 (rel 5.25×10⁻⁹; σ_max rel 9.7×10⁻¹³);
central 0.027173817559233707 (matches Phase 410's central
0.027173817517817934 at 1.5×10⁻⁹). 313 θ: gate
0.03475275259383748 vs Phase 410's 0.0347527502565207 (rel
6.7×10⁻⁸) and Gate-36 CTRL-S2's 0.034753; rank 40; σ_max
6389.649857481197. The grep audit of "0.0272" across the repo
(ledger entries 794, 798, 1070, 1094; GATE34.md §4/§5;
CHECKPOINT_GATE34.md; phase320 memo/checkpoint; g36
registration) grounds the ruling: exactly one standing
claim-form changes (G34-C's parenthetical must carry the
per-solution attribution when quoted); GATE34.md §4 body,
entry 794 and Gate-36 already attribute correctly; entry
1070's compressed line is superseded by 410 Amendment 1 +
1094 + this gate; historical charge text is not rewritten.
No published claim's deciding number changes (full row rank,
σ_min bounded away from zero at both solutions: 0.0272 /
0.0348).

## 5. Laptop admission

Staged root `/home/spark/work/g54root` (gate lib, laptop
driver, targets/primaries JSONs). Laptop venv numpy 2.5.5 /
scipy 1.18.1 (VM frame). Residuals VM↔laptop ≤ 2.7×10⁻¹⁸
absolute; σ_min ≤ 1.6×10⁻⁸ relative (Fit A laptop
0.3857618165948743, Fit B 0.015432480700342604); densities
≤ 2.8×10⁻¹⁸; Fit A max channel diff laptop
1.3366523599761537×10⁻¹² vs VM 1.3366521431357192×10⁻¹².
**ADMITTED for claims (a) and (b) deciding reads; deciding
reads remain the VM's.** Records:
`gate54/results/g54_laptop_results.json`,
`gate54/results/g54_admission.json`. (Staging note: rsync
needed the explicit key in its `-e` string passed as one
quoted argument; an eval-assembled string mangled it once —
direct invocation worked.)

## 6. Incidents and gate-side bugs (disclosed)

1. **C1 cross-check casting bug.** The pairwise cross-check
   accumulator was created with a real dtype, silently
   discarding imaginary parts. Caught by C1 itself before any
   claim read; fixed (complex accumulator); C1 then passed at
   1.02×10⁻¹³. No deciding read used the pairwise path.
2. **Mode-health Dirac slash double-lowering.** The diagnostic
   initially contracted covariant momenta with covariant γ
   matrices, giving spurious ~0.4 Dirac residuals. Fixed to
   γ^a p_a. Diagnostic only — T, residuals and Jacobians never
   used it. After the fix, Dirac residuals reproduce the
   phase's stored values exactly.
3. **Norm health-check correction.** The stored χ carry the
   fit amplitudes; the correct health identity is
   u†u = 2E|χ|², not u†u = 2E. Corrected before the control
   was judged; final norm deviations ≤ 6.9×10⁻¹⁸.
4. **SIGPIPE truncation.** An early run of the driver piped
   through `head -4` was SIGPIPE-killed and left a results
   JSON containing controls only. The driver was re-run
   untruncated; the full record regenerated with identical
   values. The on-disk `g54_results.json` is complete.

## 7. Fences carried

Site mating ≠ extent coverage (no coverage claim). Sourcing
≠ curing — the sourced tensor violates SEC as it stands; NO
no-exotic-matter claim for any sourced design. Novelty NONE
for the method (Martín-Moruno & Visser 2021, Gate-25).
σ_min per-solution only (G36-C).

DESK: NO DATA CONTACT.
