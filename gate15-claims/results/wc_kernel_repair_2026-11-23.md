# Gate-15 Kernel 2 (`g15-wc`) — v1 launch failure: diagnosis + repair (2026-11-23)

Repair-worker memo. The kernel is REPAIRED and re-validated at home;
it has NOT been relaunched (the parent launches). Relaunch spec at
the end.

## What happened

Kernel 2 (`g15-wc`, claim G15-2 transit audit) launched on Kaggle
2026-11-23 11:38:48 PST and failed after 10.3 s, in Stage 0, on its
first mpmath integral:

```
L1_m = mquad(L1_integrand_t_mp, [0, tm_mp])
  -> L1_integrand_t_mp: return 2 * t / msqrt(1 - r ** mpf("-0.9"))
  -> mpmath libmpf mpf_div: raise ZeroDivisionError
```

No Stage-0 check ran; no later stage ran. The float64 scipy path
had already completed (the traceback is at the mpmath line), so the
failure is specific to the mpmath evaluation of L₁ (and would have
hit T₁ identically).

## The integral and its singular point

Stage 0 re-verifies the member-interior controls

  L₁ = ∫₁^1000 dr / sqrt(1 − r^(−0.9)),   T₁ = ∫₁^1000 e^(−Φ₂(r)) dr / sqrt(1 − r^(−0.9))

(the P86-1/P122-2 interior proper-length / redshifted-time pair,
r_Σ = 1000 r₀). The factor sqrt(1 − r^(−0.9)) vanishes at the
throat r = 1 — an integrable square-root singularity at the lower
endpoint of the r-integration. Under the kernel's substitution
r = 1 + t² (t ∈ [0, √999]) the singularity moves to the endpoint
t = 0 and becomes removable: 1 − (1+t²)^(−0.9) = 0.9t² − 0.855t⁴ + …,
so both integrands have the finite limit 2/√0.9 ≈ 2.1081851067789197
at t = 0 (Φ₂(1) = 0). The defect is purely in how the v1 code
EVALUATED the integrand near that endpoint.

## Diagnosis — mechanism proven at home; environment exonerated

The v1 mpmath integrands computed the factor naively as
`msqrt(1 - r ** mpf("-0.9"))` with `r = 1 + t*t`. Reproduced at
home with the kernel's Stage-0 mpmath block copied verbatim
(home venv, mpmath 1.3.0 = the pinned version; also reproduced
under system mpmath 1.2.1):

- mpmath's tanh-sinh quadrature places nodes double-exponentially
  close to the interval endpoints. Instrumenting the integrand
  shows a node landing at **t = 1.845291673414244420945705e-36**
  (nonzero — an exact t == 0 evaluation never occurs).
- At dps = 40, t² ≈ 3.4051e-72 is ~32 orders of magnitude below
  the mpf ulp at 1.0 (~1e-40), so `r = 1 + t*t` rounds to exactly
  1, `1 - r**(-0.9)` is exactly 0, `msqrt(0) = 0`, while the
  numerator `2t ≠ 0` — division by exact zero raises
  ZeroDivisionError. Verified field-by-field at the raising node.

So the Kaggle failure is NOT an environment or version difference:
the v1 code fails identically at home under the pinned mpmath.
The kernel had never been executed at home before launch —
STATUS.md records it as "Compiles OK" only. The ≤1e-9 two-path
agreement of record for L₁/T₁ belongs to Phase 122's home
computation (`phase122/work/p1222_main.py`), not to this kernel.

## Why the home path did not fail

Phase 122's `mp_interior()` handled the endpoint by construction,
in three parts:

1. an explicit guard: at s == 0 the segment integrand returns the
   analytic limit `2/sqrt(0.9)` instead of evaluating the quotient;
2. a cancellation-free factor: `dl_sub(s) = 1/sqrt(-expm1(-0.9 *
   log1p(s*s)))` — expm1/log1p keep 1 − (1+s²)^(−0.9) accurate and
   strictly positive for every s > 0, however small;
3. an interval split: the substituted segment covers only
   s ∈ [0, 1] (r ∈ [1, 2]); the regular tail is integrated
   directly in r over [2, 1000].

The packaged kernel kept the substitution but dropped all three
protections and handed the whole [0, √999] to one mquad call.

## Repair (evaluation only — no deciding number, bar or fence changed)

In `gate15/kaggle/g15_wc_kernel.py` (header AMENDMENT note +
amendment block at the Stage-0 mpmath integrands):

- the throat factor is now computed as
  `_shape_denom_mp(t) = msqrt(-expm1(mpf("-0.9") * log1p(t * t)))`
  — strictly positive for every t > 0, by construction;
- `t == 0` returns the analytic limit `_LIM0_MP = 2/sqrt(0.9)`
  for both integrands (Φ₂(1) = 0, so T₁'s limit is the same);
- nothing else in the kernel changed: same substitution, same
  single-interval mquad call, same stored literals, same 1e-9
  bars, same fences.

Repaired file: 16,586 bytes, md5 f019009be40c4d290d6ed9db320fdc73,
`py_compile` OK.

## Re-validation at home (all with the shipped code)

1. Standalone repaired evaluation (dps = 40, single-interval
   mquad): L₁ = 1005.3728512079001909, T₁ = 794.19973329253437908.
   Against the stored literals (1005.3728512079 / 794.1997332925):
   rel 2.3e-16 / 4.3e-14 — inside the 1e-9 bar by ~7 orders.
   Against Phase 122's stored 40-digit values in
   `phase122/results/p1222_results.json` (1005.3728512079002 /
   794.1997332925343): agreement 0.0 at float64 print precision.
2. The repaired kernel's full Stage-0 control path, executed
   verbatim from the shipped file (everything through the Stage-0
   gate, home venv, scratch cwd): **4/4 CHECK PASS** —
   L1 two paths agree (float 1005.3728512078999, mp
   1005.3728512079001909), T1 two paths agree (float
   794.1997332925343, mp 794.19973329253437908), both vs stored
   literals PASS; Stage 0 completes and the gate does not abort.

## Relaunch spec (parent)

Same notebook `g15-wc` on Kaggle — save a NEW version on the
existing notebook (v1 there is the failed run above; do not
create a second notebook). File:
`gate15/kaggle/g15_wc_kernel.py` (repaired; md5 above). Settings
as before: Script, CPU (Accelerator None), Internet OFF,
Save & Run All (Commit). On completion: harvest `g15_out/`
(wc_results.json, wc_check.json, WC_PROGRESS.json) home for
fresh-process re-judging; in-kernel verdicts remain provisional
until then. Kernel 2 is independent of Kernel 1 as a computation,
but G15-2's verdict still rides on G15-1's (fence in the kernel
header).
