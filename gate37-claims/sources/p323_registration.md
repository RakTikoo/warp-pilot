# Phase 323 registration — THE A-THROAT EVALUATION

Filed before any Phase 323 computation. Successor to Phase 318
(CHECKPOINT318 / p318_memo), executing the last named datum of the
semiclassical identification (FU-P237-1a inheritance, ledger 803).

## The datum owed

Phase 318's fully arbitrated assembly passes the Ellis gate and the
whole Ellis core at all powers, and its throat ξ⁰ read is (0, 0, 0)
exact. The final read is blocked at exactly one core background —
the A-family throat — because no derived H{2,0}(3) evaluation exists
on the A background: the A background enters the Phase 259 harness
through `solve_Rjet_throat` (an R(l)-jet recursion), while the
∇-sector engine (`p2591_engine_d.py`) consumes a metric Taylor jet
in local coordinates. Phase 259's standing A-throat ξ⁰ read (Phase
318 FULL assembly) is (Tt, Tr, Tθ) = (0.0, +2.0, −7.0) bracket units.

**Registered prediction (Phase 318, carried verbatim):** if the
A-throat residual is likewise carried wholly by H{2,0}(3) (with
print (3),(4) = derived there), the derived H{2,0}(3) at the A
throat in DF print units is **(9/4, 3/4, 21/4)**; the implied print
value there is (9/4, 25/12, 7/12).

## Frame

venv python; Phase 259 engines unmodified
(`phase259/work/p2591_engine_d.py`; the Phase 318 g0-patched copy
`phase318/work/h203/p2591_engine_d_g0.py` where g(0) ≠ η, exactly as
Phase 318 used it); Phase 259 harness for cross-checks and pattern
evaluation; exact-rational (Fraction) arithmetic wherever
Phases 259/318 used it. Bridge: print H = −E[invariant]; Eq. (3.14)
weights and prefactor 210 as audited in Phase 318.

## Controls (must pass before any A-background read is quoted)

- **C(i) — Phase 318's final read reproduced from stored
  artefacts.** Exact Fraction arithmetic from the stored triples:
  REST_print(throat) = (44/135, 4/27, 100/189); derived H{2,0}(3) =
  (80, 16, 112), H(3) = (32, 8, 44), H(4) = (4, 4, 16); Phase 259
  FULL throat ξ⁰ residual (0, +16, 0). Required outcomes: derived
  REST = (1/140)(80,16,112) − (8/945)(32,8,44) + (2/315)(4,4,16);
  substitution delta 210·(REST_der − REST_print) = (0, −16, 0);
  substituted residual (0, 0, 0); gate coefficient: stored
  P(ξ) = [203, −1806, 5460, −4200] with ξ⁰ 203 → 187.
- **C(ii) — route validation on Ellis backgrounds** (where derived
  H{2,0}(3) values are already known):
  - the metric-jet builder + unpatched engine_d at the Ellis
    throat must reproduce E2 programme mixed diag
    (−80, −16, −112) **exactly**, divergence exactly (0,0,0,0);
  - the builder + g0-patched engine at Ellis ℓ=1 must reproduce
    the exact record (47/8, 1/8, 55/8) programme mixed, divergence
    exactly 0;
  - the float builder path at Ellis R = 1.5/2/3 must reproduce
    Phase 318's stored off-throat E2 values
    (`p318_ellis_e2_offthroat.json`) to ≤ 1e-12;
  - the exact-rational R-jet solves (families A, C, D) must match
    the driver's float `solve_Rjet_throat` to ≤ 1e-13 per
    coefficient.

## Route (a) — extend the ∇-sector evaluation to the A background

The A metric is ds² = −dt² + dl² + R(l)² dΩ² (Φ ≡ 0), R the
`solv
...[truncated 3903 chars]