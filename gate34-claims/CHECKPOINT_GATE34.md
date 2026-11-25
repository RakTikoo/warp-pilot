# CHECKPOINT GATE-34 — RE-JUDGEMENT OF THE
# POSITIVE-DENSITY PAIR (PHASES 312 + 313)

**VERDICT: ALL FOUR CLAIMS SURVIVE.** Full record:
`gate34/GATE34.md` (quotable claim set §5).

## Controls (all PASS before any re-judgement read)

- **C1** M ≡ 1 limit vs Phase 295 factorisation:
  max diff 3.2×10⁻¹⁹ (bar 1e-12).
- **C2** FD guard: analytic vs FD That 7.4×10⁻⁷ at
  h = 0.01; 2.7×10⁻⁷ Richardson-extrapolated — FD
  truncation class, no conceptual error.
- **C3** R/Q_K split vs Phase 312 stored: diff 0.0;
  split total vs gate ρ: 3.0×10⁻¹⁹.
- **C4** Gate spinor builder on Phase 313's stored
  winner: spinors at diff 0.0, residuals ≤ 9.2×10⁻¹⁷,
  densities ≤ 2.1×10⁻¹⁶, Dirac ≤ 8.5×10⁻¹⁷,
  pairwise-vs-direct 1.1×10⁻¹⁶.
- Record reproduction: gate That vs
  `p313_targets.json` ≤ 8.7×10⁻¹⁹ per component.

## Item 1 — member re-read: NOTHING MOVES

Gate SET-244 = stored on every statistic (Type-I
1336 exact; NEC min −0.0031268695933069223; ρ min
−7.561242105046518×10⁻⁸ identical). Gate polish
lands on the identical S1 point; gate-derived
S2/S3/S4 = stored sites point-for-point. Depth gate
−0.0011802747430460965 vs stored
−0.0011802747430460956. Per-site ρ_req / both NEC
reads / Type-I / splits identical at ≤ 1×10⁻¹⁷.
ρ_req: +2.168496×10⁻⁴ / +1.521832×10⁻⁴ /
+2.161432×10⁻⁴ / +6.498030×10⁻⁵, R-carried at all
four sites.

## Item 2 — site-rule attack: CERTIFIED

Dense scan 129,042 pts: ρ < 0 only at r ∈ [10, 10.5]
(M ≡ 1 strip), 6,431 pts, |ρ| ≤ 2.49×10⁻⁷ (polished
volume min −2.552×10⁻⁷ at r = 10.506). SAMPLER-M on
EVERY ρ < 0 locus: most binding −4.876×10⁻⁴.
Threshold hits: (a) SAMPLER-M ≤ −3.126870×10⁻³: 0;
(b) exact NEC ≤ −3.517021×10⁻³: 0 (best fib
−4.885×10⁻⁴); (c) Type-I + SAMPLER-M ≤ depth: 0
(best −1.616×10⁻⁴). Continuum SAMPLER-M polish
reaches only −3.071×10⁻³ (ρ > 0 there) — does not
beat S2. Certified scope in GATE34 §5 (G34-B): no
binding-grade ρ < 0 locus exists in the volume at
the registered grades. NOT pointwise positivity —
fence 1 stands (gate's denser volume min
−2.55×10⁻⁷ reported beside the SET-244
−7.561×10⁻⁸).

## Item 3 — match: REPRODUCED, STRUCTURAL

Gate optimiser (own builder/starts): N = 6 fits at
max R = 3.0×10⁻¹⁶ (stage A, 1/6, tight tolerances)
and 7.1×10⁻¹⁶ (stage B, 7/8, protocol tolerances);
Phase 313's stored best 3.253×10⁻¹³. Densities at
the gate match = the targets' positive values.
Sweep: N=4 best 1.537×10⁻³ (0/6), N=5 best
2.470×10⁻⁴ (0/6), N=6 7/8, N=7 7/7 (4.578×10⁻¹⁴),
N=8 7/7 (1.119×10⁻¹³) — transition exactly at the
counting threshold (7N−1 ≥ 40 first at N=6).
Jacobian at the gate solution: full row rank 40,
σ_min = 0.0272. Perturbation ladder: bar
re-achieved at ε = 1×10⁻¹² / 1×10⁻⁹ / 1×10⁻⁶ /
1×10⁻⁴ (best max R ≤ 3.6×10⁻¹⁴), densities tracking
the perturbed targets, positive throughout.
**Structural, not knife-edge.**

## Claim set (GATE34.md §5 is the only quotable form)

- G34-A (member existence/values) SURVIVES.
- G34-B (binding-site positivity, certified scope)
  SURVIVES.
- G34-C (match + residuals) SURVIVES.
- G34-D (density-at-match positivity) SURVIVES.
- Fences carried verbatim: full-volume (SET-244 ρ
  min −7.561×10⁻⁸; gate's denser read −2.55×10⁻⁷
  beside it), NEC (depth a negative read, both
  sampler forms), QI (absent for the extended
  class; none quoted).

## Not done / not re-judged

Fence (b) extent construction (stands open, at
positive density); QI for the M(r) class; the other
Phase 312 positive-density members (stand at Phase
312's grade). No ledger append, no launches, no
publication, no user contact.

**DESK: NO DATA CONTACT.**

## Files

- Registration: `gate34/work/g34_registration.md`
- Machinery: `gate34/work/g34_lib.py`,
  `g34_fd.py`, `g34_spinor.py`
- Runs: `g34_controls.py`, `g34_item1.py`,
  `g34_item2.py`, `g34_item3a.py`, `g34_item3b.py`,
  `g34_item3c.py`
- Results: `gate34/results/g34_controls.json`,
  `g34_c2_richardson.json`, `g34_item1.json`,
  `g34_item2.json`, `g34_item2_scan.npz`,
  `g34_item2_sampler_audit.json`, `g34_item3a.json`,
  `g34_item3b.json`, `g34_item3c.json`
- Record: `gate34/GATE34.md`
