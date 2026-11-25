# Gate-15 — STATUS (2026-11-23; G15-1 COMPLETE, G15-2 PENDING)

**The gate record is `GATE15.md` — read it for the verdicts.**
G15-1: **SURVIVES IN RESTATED WORDING** (Kernel 1 harvested to
`kaggle/outputs/v2/` and re-judged fresh at home: closure and
shell legality confirmed in the full solution space; the
claim's dimension clause, its [R̃]₂ coefficient, and its
uniform amplitude bound corrected; closure inside the
(e)-quotient representatives fails the amplitude bar at ℓ=1 —
carried on the restated wording's face). G15-1 joins the
publication queue in the restated wording. G15-2: **NO
VERDICT** — Kernel 2 (`g15-wc`) failed at its Stage-0 control
gate (quadrature singularity in the L₁ integrand); repair in
flight; verdict only on harvest + home re-judgement. The
interim record below is retained for provenance.

Gate: independent re-computation + novelty audit of Phase 122's
two claims (G15-1 posed two-mouth configuration; G15-2 measured
shortcut). The deciding reads for the solve/shell-sign (G15-1)
and the transit numbers (G15-2) were packaged as Kaggle
kernels (see `kaggle/README.md`) under the 2026-11-23
standing order; verdicts follow home re-judging of the kernel
outputs.

## Complete at home
- **W-A (controls): COMPLETE, but its headline value was WRONG
  and has been corrected by W-B2 (below).** W-A's Bach-flatness
  and Darmois-solve results stand; its member shell value does
  not (see correction).
- **W-B1 (engine + settlement): COMPLETE.** Own jet-algebra Bach
  engine; κ anchor reproduces (κ_full = −2.76430892×10⁻⁵,
  κ_enlarged = 0 exactly). **Dimension correction to the phase:**
  prolonged-system settlement gives ℓ=0: 7 ✓, ℓ=1: **10** (phase
  claimed 9 — at ℓ=1 the tracefree angular basis E₁ ≡ 0 makes G
  metrically vacuous; a verified 4-dim pure-gauge family sits in
  the 10, so the (e) quotient is **6**), ℓ=2: **8**, ℓ=3: **8**
  (claimed 7 each; the +1 at ℓ≥2 is a genuine non-gauge
  direction). Settled basis jets: `results/wb1_basis_jets.json`.
- **W-D (novelty): COMPLETE.** G15-1: **PARTIALLY KNOWN**;
  G15-2: **PARTIALLY KNOWN** (exact poses not found in any index
  reached; all ingredients published). Log:
  `results/wd_search_log.md`, grades: `results/wd_novelty.md`.
- **Phase-133 flags** folded into the record:
  `results/gate15_p133_flags.md`.

## Correction (material): the member shell control
W-A reported the member's Ŝ⁰⁰/α₀ = +0.0204228620559, a 0.65%
offset from the phase-stored control +0.0202914453. **W-B2's A1
cross-check found the error was W-A's**: W-A's interior A‴ jet
for exp(2Φ₂) used a printed expression that expands with a
spurious 4Φ₁Φ₂A₀ term. With the true A‴, two independent routes
(sympy jets in `work_b2/wb2_functionals.py`; the mpmath.diff
diagnosis in `work_b2/wb2_a1_patch.py`) give
[R̃_,n]₀ = **−0.0152185839537**, Ŝ⁰⁰/α₀ = **+0.0202914452716** —
the phase-stored control (−0.0152185840 / +0.0202914453)
**REPRODUCES**. (Gate-9's W-B recorded the same +0.0204228620559
value and the same 0.65% offset inside its 2% bar — the same
erroneous jet appears to have been inherited there; flagging
for the parent's Gate-9 record, not re-litigating its verdict,
which the offset did not move.) Kernel 1 Stage 0 re-runs this
diagnosis as a control gate.

## W-B2 — stopped mid-flight by the standing order
Last good checkpoint on disk (`gate15/work_b2/`, 2026-11-23
18:25 UTC): channel functionals computed and stored
(`wb2_functionals.json`, incl. A1/A2 anchors — A2 PASSES:
c = 0.0043023736 at all ℓ, D3 triple and [R̃]₃ within their
bars, S identity exact); primary source extraction COMPLETE
(`wb2_source.json`, modes ℓ=1–4, all ε rows); second-path
script written (`wb2_second.py`, not run to completion).
NOT done when stopped: entering-order fits/confrontation,
second-path run, response matrices, solves, shell sign,
wb2_results/memo/check. No gate15 processes remain running
on this VM (verified by ps).

## Packaged (parent launches on Kaggle, one at a time)
- `kaggle/g15_wb2_kernel.py` — G15-1 deciding reads (controls
  first; solves full-vs-(e); shell sign; checker). Built by
  `kaggle/build_kernel1.py` from `kaggle/driver_wb2.py`;
  packaging smoke-tested at home (header decode + module
  materialisation verified; full compile OK).
- `kaggle/g15_wc_kernel.py` — G15-2 transit numbers
  (L₁/T₁ control gates first; route integrals, thresholds,
  gains, T4, tides; checker). Compiles OK.
- Details: `kaggle/README.md`.

## Unpackageable
Nothing. The final checker integration and GATE15.md are
home-side short verification + writing by design, not heavy
compute.

## Addendum (2026-11-23): Kernel 1 v1 launch failure — diagnosis + repair

**What happened.** Kernel 1 (`g15-wb2`) launched on Kaggle
2026-11-23 11:06 PT and aborted at its Stage-0 control gate after
14.9 s: 15/16 checks PASS; the single failure was
`A1 jump_R == 0` — jump_R read
+3.3617694518376954105565534120486498773929070783924×10⁻⁹ against
the check's |jump_R| < 1e-12 bar. No later stage ran.

**Diagnosis — class (a), mechanism identified; (b) and (c)
excluded on evidence.** jump_R = [R̃] = R̃_ext − R̃_int at
r_Σ = 10³ r₀ on the stored member jets. It is analytically zero
for the exact member (Gate-9 G9-2: [R̃] = 0, 40-digit second path
0.0). But:

- The Kaggle value is **digit-for-digit identical** to the home
  stored value in `work_b2/wb2_functionals.json` (computed at home
  before packaging), and the functionals matched home at max rel
  diff 0.000e+00 — the port is faithful and the environment is
  exonerated: NOT (c) a port discrepancy, NOT (b) an
  environment/frame difference.
- A home closed-form re-read (mpmath) gives jump_R unchanged to
  ~41 significant digits between dps = 50 and dps = 80 — not
  evaluation noise. Sensitivity: ∂[R̃]/∂β_MK = 0.012000000000,
  ∂[R̃]/∂k ≈ 0 at this scale. The member as stored carries
  β_MK = 2.142611 (7 significant figures). Root-solve at dps = 50:
  jump_R(β*) = 2.7×10⁻⁵⁰ at β* = 2.14261071985254568…, i.e.
  β* − β_stored = −2.801×10⁻⁷, **inside** the stored constant's
  rounding interval (half-width 5×10⁻⁷), and
  0.012 × 2.8014745×10⁻⁷ = 3.36176945×10⁻⁹ reproduces the read
  exactly. The residual is the deterministic propagation of the
  stored β_MK rounding.
- The programme's own record already documents this exact floor:
  Phase 90 (`phase90/results/p901_memo.md`): "[R̃]₀ control
  residual +3.36×10⁻⁹ (the rounded stored β, k)"; the
  Phase-90/91 control floor is 3.4×10⁻⁹ (also
  `phase122/CHECKPOINT122.md`).

So the defect was in the check, not the computation: the
packaging step asserted |jump_R| < 1e-12, ~3400× tighter than the
stored member's documented evaluation floor, so the check could
not pass on ANY faithful evaluation, in any environment.

**Repair (dated amendment, on the record — no deciding bar
moved).** In `kaggle/driver_wb2.py` (header AMENDMENT note +
check site), the check is now two-part: (i) agreement with the
home stored control at the sibling A1 standard (rel < 1e-9) AND
(ii) |jump_R| ≤ 1e-8. The 1e-8 bound is derived from the
evaluation's own error scale: the full rounding excursion of the
stored constants is 0.012 × 5×10⁻⁷ = 6×10⁻⁹ < 1e-8, and 1e-8
remains >5 orders of magnitude below every deciding scale in
this gate (dissolution bar 1e-5 per unit ε; jump_Rn = 1.5×10⁻²).
jump_R is a member-join CONTROL, not a G15-1 deciding read; all
deciding bars (Stage-3 residuals ≤ 1e-5, amplitudes ≤ 1e2, 5%
second-path agreement) are untouched. Kernel rebuilt with
`kaggle/build_kernel1.py` (66,018 bytes; embedded data and
carried-module hashes identical to v1 — only the driver
changed). **Local control-only smoke run of the rebuilt kernel's
shipped Stage-0 code: 16/16 checks PASS** (34.8 s, home venv).

**Relaunch spec (parent).** Same notebook `g15-wb2` on Kaggle —
save a NEW version on the existing notebook (v1 there is the
failed run above; do not create a second notebook). File:
`gate15/kaggle/g15_wb2_kernel.py` (repaired). Settings as before:
Script, CPU (Accelerator None), Internet OFF, Save & Run All
(Commit). On completion: harvest `g15_out/` (wb2_results.json,
wb2_check.json, PROGRESS.json) home for fresh-process
re-judging; in-kernel verdicts remain provisional until then.

## Addendum (2026-11-23): Kernel 2 v1 launch failure — diagnosis + repair

**What happened.** Kernel 2 (`g15-wc`) launched on Kaggle
2026-11-23 11:38:48 PST and failed after 10.3 s in Stage 0, on
its first mpmath integral: `mquad(L1_integrand_t_mp, [0, tm_mp])`
raised ZeroDivisionError inside
`2 * t / msqrt(1 - r ** mpf("-0.9"))` (r = 1 + t²). No Stage-0
check ran; the float64 path had already completed.

**Diagnosis — evaluation defect in the packaged integrand, NOT
an environment difference.** The throat factor sqrt(1 − r^(−0.9))
vanishes at the endpoint t = 0 (the r = 1 throat singularity
under the x = 1+t² substitution; removable, limit 2/√0.9).
mpmath's tanh-sinh rule places a node at t = 1.8453e-36
(nonzero); at dps = 40, t² ≈ 3.4e-72 is far below the mpf ulp
at 1.0, so r = 1 + t² rounds to exactly 1, the factor is exactly
0 while 2t ≠ 0, and the division raises. Reproduced at home
verbatim under the pinned mpmath 1.3.0 (and 1.2.1) — v1 had been
compile-checked only, never executed at home. Phase 122's home
path (`p1222_main.py: mp_interior`), which produced the ≤1e-9
agreement of record, never failed because it guards the
endpoint by construction (analytic-limit value at s == 0,
expm1/log1p factor, [0,1] + [2,1000] split); the packaged
kernel dropped all three protections. Full evidence:
`results/wc_kernel_repair_2026-11-23.md`.

**Repair (evaluation only — no deciding number, bar or fence
moved).** In `kaggle/g15_wc_kernel.py` (header AMENDMENT note +
amendment block at the integrands): the factor is computed as
`msqrt(-expm1(mpf("-0.9") * log1p(t * t)))` (strictly positive
for every t > 0) and t == 0 returns the analytic limit
2/sqrt(0.9) — Phase 122's rule ported to the kernel's
integrands. Repaired file: 16,586 bytes, md5
f019009be40c4d290d6ed9db320fdc73, compiles OK. **Home
re-validation with the shipped code: Stage 0 runs verbatim,
4/4 checks PASS** (mp L₁ = 1005.3728512079001909, T₁ =
794.19973329253437908; rel vs stored literals 2.3e-16 /
4.3e-14; agreement with Phase 122's stored 40-digit values 0.0
at print precision).

**Relaunch spec (parent).** Same notebook `g15-wc` on Kaggle —
save a NEW version on the existing notebook (v1 there is the
failed run above; do not create a second notebook). File:
`gate15/kaggle/g15_wc_kernel.py` (repaired). Settings as before:
Script, CPU (Accelerator None), Internet OFF, Save & Run All
(Commit). On completion: harvest `g15_out/` (wc_results.json,
wc_check.json, WC_PROGRESS.json) home for fresh-process
re-judging; in-kernel verdicts remain provisional until then.
