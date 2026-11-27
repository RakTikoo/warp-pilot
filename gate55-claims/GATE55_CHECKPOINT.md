# GATE-55 CHECKPOINT — INDEPENDENT RE-JUDGEMENT OF PHASE 420

Charge: ledger entry 1103. Deliverable: `gate55/GATE55.md`
(quotable set §1: G55-A…G55-D, riders G55-R1…R3; fences §0).
**Verdict: THE PHASE 420 SET SURVIVES, AS FENCED** — claims
(a), (b), (c) survive; the C-S context arm (d) is CONFIRMED
and scopes the set via rider G55-R1; claim (c) carries the
density-naming rider G55-R2; Amendments 1–3 all SOUND.

## Machinery

`gate55/work/g55_lib.py` (this gate's own, written from the
registration): γ by Kronecker products (Dirac representation);
the composite as an explicit field function ψ(X) with per-mode
masses and analytic derivatives; T_ab the canonical
symmetrised bilinear on the total field (Phase 420 SS2's
defined object), computed from ψ and ∂ψ — no pairwise
S-matrix in any deciding path (Phase 420's fits ran pairwise;
its direct path exists but its Jacobians/fits are pairwise —
the gate's deciding path is the field function throughout,
including its Jacobians). A separately written pairwise
assembly is present only as the C1 cross-check. Own
Hawking–Ellis classifier + channel decomposition (Phase 410
SS4(ii) definitions, gate code); own δ construction; own
central-FD Jacobians (h_j = 1×10⁻⁶·max(1,|θ_j|)). Registration
`gate55/work/g55_registration.md` predates all computation;
bars fixed there. Driver `gate55/work/g55_run.py`; records
`gate55/results/g55_results.json`.

## Controls (all before claim reads)

- C1 PASS: field vs pairwise cross-check, random mixed-mass
  superposition, 5 random points: max rel diff 2.1×10⁻¹⁶
  (bar 1×10⁻¹²). Mode health on the four stored primaries:
  Dirac ≤ 5.3×10⁻¹⁷, norm dev ≤ 6.9×10⁻¹⁸ (bar 1×10⁻¹²).
- C2 PASS (420's CTRL-420-A on gate machinery): residuals
  ratios 0.9986 / 1.00002 / 1.00000 of stored; σ_min
  0.38576181687555705 vs 0.3857618146636974 (rel 5.7×10⁻⁹);
  rank 30.
- C3 PASS (CTRL-420-B): ratios 0.99992–1.00019; σ_min
  0.015432480413708932 vs 0.015432479500623982 (rel 5.9×10⁻⁸);
  rank 50.
- Record identity: Phase 420's stored T_req vs Phase 410's
  stored That at the A sites: max diff 0.0 (gate re-checked).

## Reads (deciding, VM)

- (a) δ rebuild from stored T_req: gate T_corr vs stored
  T_corr max abs diff **0.0 at all 8 sites**. Δ_A2 =
  2.213556504990559×10⁻⁴, Δ_A3 = 3.3884134221257565×10⁻⁴;
  SEC_trace(T_corr) = 1.08×10⁻¹⁹ (A2), 0.0 (A3). Joint
  channels all rise at A2/A3 (min diff +2.84×10⁻⁵ at A2's
  DEC_flux; +8.29×10⁻⁵ at A3); all principal pressures of
  T_req negative at both sites (the mechanism). A2 joint
  1.384623×10⁻⁴ → 2.491401×10⁻⁴.
- (b) C-A primary vs gate T_corr: residuals bit-identical to
  stored [4.057×10⁻¹², 7.640×10⁻¹², 3.496×10⁻¹⁰]; σ_min gate
  30.12132520520076 (rel 1.3×10⁻¹¹ vs stored), rank 30/30,
  blocks agree ~10⁻¹¹ rel. C-B: max residual bit-identical
  3.565×10⁻¹⁵; σ_min rel 1.2×10⁻⁷; rank 50/50.
- (c) T_sup Type-I, all channels ≥ 0 at A1/A2/A3. Minima:
  A1 joint/SEC +1.227388×10⁻⁶; A2 SEC_trace
  +2.7471977600765363×10⁻¹² (stored exactly), joint
  +2.491401×10⁻⁴; A3 SEC_trace +2.2765634169474858×10⁻¹⁰
  (stored exactly), joint +1.049917368373495×10⁻³.
  Densities positive both ways: T[0,0] bit-identical to the
  phase checker's record; eigenvalue ρ identical to the
  phase driver's diagnostics record — the two records use
  one symbol for two definitions (rider G55-R2). Prices
  bit-identical (0.029172052178672605 / 2.0362442383995038×10⁻⁶;
  410 comparison 0.029266406597128584). A2 family split
  (T[0,0]): +5.933751538533417×10⁻⁴ / +2.7608764575874975×10⁻⁶ /
  interference −1.3893955858578413×10⁻⁴.
- (d) C-S stored N = 6 warm-A solution vs gate T_corr: max
  residual 1.468495007452498×10⁻¹¹ (stored
  1.468495745267423×10⁻¹¹; rel 5.0×10⁻⁷) — CONFIRMED; rider
  G55-R1. Context σ_min at that solution (gate): 0.3133085549618151.

## Amendment audits

- A1 SOUND: stored 410 Fit A max residual
  2.9659878908312287×10⁻¹² > the registered 1×10⁻¹² cap —
  ill-posed as charged; corrected bar (≤ 2× stored, max
  ≤ 1×10⁻¹¹) met by the phase's reads and by gate C2/C3.
- A2 SOUND: the gate's own spinor is non-finite at
  (p = 0, m = 0) — the singularity is real and
  implementation-independent; guard trigger (code read) =
  exactly-zero massless momenta only; exactly-zero momenta
  in the stored deciding solutions (C-A, C-B, C-S): none —
  the guard is inert on every deciding read.
- A3 SOUND: original ladder ε = 10⁻⁶ draw 0 stalled at
  3.2820674985370054×10⁻⁹, sibling reclosed at
  6.667373216443225×10⁻¹⁰; completed ladder (seed 4203,
  tolerances 1×10⁻¹³, bar unchanged 1×10⁻⁹) recloses at all
  four rungs, max 1.2781931870247612×10⁻¹⁴; phase checker
  agrees; the as-first-computed "DOES NOT SUPPLY" string is
  preserved in the record.

## Laptop admission

Staged `/home/spark/work/g55root` (g55_lib.py md5
781e9385b1187e865eae84000378de52 both sides; laptop numpy
2.5.5 / scipy 1.18.1). ADMITTED as corroboration for (a),
(b), (c): (a) rebuild max diff 1.2×10⁻¹⁹ (VM 0.0); C-A
residuals agree ≤ 5.2×10⁻¹⁷ abs; C-B ≤ 1.4×10⁻¹⁸; (c)
quantities ≤ 4.1×10⁻¹⁷, all channels positive on laptop
reads too. Deciding reads remain the VM's. Records:
`gate55/results/g55_laptop_results.json`,
`gate55/results/g55_admission.json`; driver
`gate55/work/g55_laptop.py`.

## Incidents (disclosed)

Two staging attempts for the laptop mirror failed on shell
quoting in the rsync/ssh options (no data transferred; the
successful staging was md5-verified file-by-file as above).
No gate-side numerical incident: no bug was found in the
gate machinery after C1–C3 passed, and no deciding read was
re-taken.

## Files

- `gate55/GATE55.md` — the quotable set.
- `gate55/work/` — g55_registration.md, g55_lib.py,
  g55_run.py, g55_laptop.py.
- `gate55/results/` — g55_results.json,
  g55_laptop_results.json, g55_admission.json.

No ledger append, no publication, no user contact — per the
charge. DESK: NO DATA CONTACT.
