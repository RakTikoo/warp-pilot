# P141-3 — THE ε ≤ 0.01 RE-PRICING

**Worker:** W-3. Implementation fixed in `work/p1413_runrecord.md`
before any deciding number was computed. Checker: 31/31 PASS
(`results/p1413_checker.json`, script `work/p1413_checker.py`,
independent recomputation from the Phase-133/122 source files).

## VERDICT: POSE STANDS AT SECOND ORDER AT D/r_Σ = 100

In plain language: at the one spacing where Phase 133 left the
pose alive — the two mouths 100 throat-widths apart (ε = 0.01) —
the pose still stands once the second-order terms are honestly
put back in, with Phase 133's *measured* high-mode tail instead
of the rough flat allowance Phase 133 used. The shell that holds
the join together keeps the right sign: its strength, which
starts at +0.02029 (in units of α₀), is cut by the second-order
correction to +0.00403 — smaller, but still positive, at both
mouths. The gains keep their error bars and stay far above the
break-even value of 1. And the second-order fix itself is not
bigger than the thing it fixes: it moves the exterior's β
parameter by about 13% of β itself, and the extra homogeneous
amplitude by about 3% of 1. So at this spacing the configuration
is a genuine second-order pose, not just a first-order one with
the corrections left off. The smaller spacings ε = 0.003 and
ε = 0.001 (extensions beyond the registered rows) stand more
comfortably still. The full assembled statement a future Gate
can carry verbatim is in §5.

Phase 122's milestones are cited here only as scan signals
under attack (Gate-15 pending), at their registered scope
(perturbative through the entering orders of modes ℓ ≤ 3;
D/r_Σ ∈ {10, 30, 100}; pre-existing configuration; (V-b)
UNDECIDED). Nothing here is a transport or FTL claim; every
transit number is **EFFECTIVE transit accounting (C12)** —
local light speed is never beaten anywhere, by any route.
Nothing here is called a traversable wormhole: traversability
additionally requires the traversal clauses, the formation
clause (standing: PRE-EXISTING ONLY), and the (V-b) clause
(standing: UNDECIDED), each stated in the same breath.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## 1. Dependency (stated first, as registered)

P141-1's integrated verdict is **LOAD IRREDUCIBLE IN THE
REGISTERED BASIS**, and its PRICE RE-READ did **not** trigger:
no swept setting moved the second-order load by more than
floor_J2 while keeping the prolonged row residual ≤ 10⁻²⁰.
Per §P141-3's registered dependency, this item therefore uses
P133-2's values throughout — Ŝ⁰⁰⁽²⁾ = −162.648 per unit ε²
(full stored precision −162.64802149771168) and the
representative amplitudes (δβ⁽²⁾, δk⁽²⁾, a_e⁽²⁾) =
(−2714.48, +2.61×10⁻⁵, −274.00) per unit ε² — and κ⁽²⁾ = 0
carried from P133-2 (at/below floor_J2 = 3.241 per unit ε²;
not decided nonzero).

**Scope reconciliation (registered):** P141-4, running in
parallel, prices the ℓ ≥ 1 shell contributions. This memo's
statement is the **ℓ = 0 sector's** statement. If P141-4's
summed correction at ε = 0.01 later moves this item's shell
read, the coordinator reconciles the two and states the
reconciliation; this item does not wait for P141-4 and does
not average it in.

## 2. Anchors (both PASS, before any deciding read)

- **A1 — PASS, exact.** From the stored components, with the
  flat tail carry as P133-2 computed it:
  +0.0202914453 − 162.64802149771168×(0.01)² − 2.7×10⁻⁶
  = **+0.0040239432**, reproducing P133-2's ε = 0.01 shell row
  +0.00402 within 5% (relative difference 9.8×10⁻⁴ against the
  registered rounded value; 0.0 against P133-2's stored
  full-precision value 0.00402394315022883).
- **A2 — PASS, exact.** From `p1333_results.json` row 100000:
  the gain intervals recomputed as (L_ext + ΔL)/(2L₁) and
  (E_ext + ΔE)/(2T₁) agree with P133-3's stored intervals with
  maximum relative difference **0.0** (tolerance applied:
  10⁻⁹, stricter than P133-3's own checker, whose gain checks
  were stored-identity plus `reaches_G1 == False`); the stored
  ΔL_ext⁽²⁾ interval is [−0.043758, +0.085286] r₀, i.e. the
  checkpoint's [−0.044, +0.085] r₀; and the tail construction
  of §3, evaluated at ε ∈ {0.1, 1/30, 0.01}, reproduces
  P133-3's stored shell tail contributions (2.178187×10⁻⁶,
  1.756691×10⁻⁸, 3.071531×10⁻¹⁰) with relative difference
  **0.0** at all three rows.

## 3. The measured tail (replacing the flat carry)

tail(ε) is built from P133-3's MEASURED ℓ ≥ 4 [R̃_,n]
coefficients exactly as P133-3 built its bound: for ℓ = 4
(powers ε³, ε⁴, ε⁵; coefficients +2.149182×10⁻⁴, ~10⁻¹⁷,
+1.014776×10⁻¹) and ℓ = 5 (powers ε⁴, ε⁵, ε⁶; coefficients
+4.922140×10⁻⁴, ~10⁻¹⁷, +2.548420×10⁻¹), the absolute
contributions A₄(ε), A₅(ε) are summed over powers, the
per-ε ratio q(ε) = A₅/A₄ is formed, the geometric sum
A₄/(1 − q) is taken, and the shell contribution is (4/3) of
that sum (P133-3's stored conversion). It is a
measured-pattern bound (two measured modes plus the source
projection's D-scaling), not a proof for all ℓ — stated as
such. Values: tail(0.01) = 3.071531×10⁻¹⁰,
tail(0.003) = 7.823709×10⁻¹², tail(0.001) = 2.873510×10⁻¹³.
Against the flat carry 2.7×10⁻⁶ this is the whole point of
the re-pricing at these rows: at ε ≤ 0.01 the true tail is
four-plus orders below the flat allowance, so the flat carry
was *understating* the surviving shell sign.

## 4. The re-pricing, per row

Shell sign at second order, Ŝ⁰⁰/α₀(ε) = +0.0202914453 +
Ŝ⁰⁰⁽²⁾ε² − tail(ε), at **both mouths** (the A↔B-symmetric
read of P122-1/P133-2):

| ε | D/r_Σ | Ŝ⁰⁰⁽²⁾ε² | tail(ε) (measured) | **Ŝ⁰⁰/α₀(ε)** | (flat-carry value, for comparison) |
|---|---|---|---|---|---|
| **0.01 (deciding)** | **100** | −0.0162648021 | 3.07×10⁻¹⁰ | **+0.00402664** | +0.00402394 |
| 0.003 (extension) | 333⅓ | −0.0014638243 | 7.82×10⁻¹² | +0.01882761 | +0.01882492 |
| 0.001 (extension) | 1000 | −0.0001626480 | 2.87×10⁻¹³ | +0.02012880 | +0.02012610 |

The ε = 0.003 and ε = 0.001 rows are **extensions beyond the
registered D-rows** {10, 30, 100}: the pose was posed at
D/r_Σ ∈ {10, 30, 100}, and these rows inherit the
construction's formulas, stated as such. They are not
deciding rows.

Perturbativity of the completion, per row (registered bar:
|δβ⁽²⁾|ε² < β_MK = 2.142611 r₀ AND |a_e⁽²⁾|ε² < 1 — the
excursion smaller than the quantity it corrects), with the
first-order excursions at the same rows alongside:

| ε | \|δβ⁽²⁾\|ε² (ratio to β_MK) | \|a_e⁽²⁾\|ε² (ratio to 1) | \|δβ⁽¹⁾\|ε | \|a_e⁽¹⁾\|ε | bar |
|---|---|---|---|---|---|
| 0.01 | 0.271448 (0.1267) | 0.027400 (0.0274) | 3.113×10⁻⁵ | 7.564×10⁻⁷ | **MET** |
| 0.003 | 0.024430 (0.0114) | 0.002466 (0.00247) | 9.339×10⁻⁶ | 2.269×10⁻⁷ | MET |
| 0.001 | 0.002714 (0.00127) | 0.000274 (0.000274) | 3.113×10⁻⁶ | 7.564×10⁻⁸ | MET |

(δk excursions, no registered bar: second order
2.61×10⁻⁹ / 2.35×10⁻¹⁰ / 2.61×10⁻¹¹; first order ≤ 8.9×10⁻¹⁴.)

One honest qualification, stated plainly because the numbers
show it: the second-order excursions, while smaller than the
quantities they correct (the registered bar, met), are NOT
smaller than the first-order excursions at the same row —
at ε = 0.01 the δβ second-order excursion is ~8.7×10³ times
the first-order one, and the a_e one ~3.6×10⁴ times. That
inverted order hierarchy is exactly P133-2's price (the
representative amplitudes per unit ε² are large); it is why
the shell sign is cut by 80% at this row even though the
completion remains perturbative in the registered sense. It
does not change the verdict form, whose deciding test is the
registered bar; it is recorded here so the assembled
statement is not read as claiming a small second-order term
in every sense.

**Gains with remainders at the deciding row** (EFFECTIVE
transit accounting, C12; propagated exactly as P133-3
propagated them, from ΔL_ext⁽²⁾ ⊂ [−0.043758, +0.085286] r₀
and ΔE_ext⁽²⁾ ⊂ [−0.010004, +0.018895] r₀ at D/r_Σ = 100):

- G_τ = 23.00840, remainder interval **[23.00838, 23.00844]**;
- G_t = 17.31288, remainder interval **[17.31288, 17.31290]**.

**Both remainder intervals exclude G = 1** — their lower
edges sit at 23.00838 and 17.31288, a factor ~17–23 above
break-even.

**Thresholds (FORMAL in every statement):** D*_τ = 4016.023 r₀
with FORMAL shift interval **[4016.005, 4016.034] r₀**;
D*_t = 3592.719 r₀ with FORMAL shift interval
**[3592.692, 3592.741] r₀**. These are FORMAL break-evens
below the construction domain D ≥ 10⁴ r₀, carried from
P133-3 with their intervals sorted ([4016.0051847409195,
4016.034070720703] and [3592.692431687301, 3592.7405422245474]
at full precision).

## 5. THE ASSEMBLED STATEMENT (deciding section; Gate-carryable verbatim)

> At D/r_Σ = 100 (ε = 0.01), the pose stands at second order
> in the ℓ = 0 sector as follows: posed through the entering
> orders of modes ℓ ≤ 3 (linearised; Phase 122, cited as a
> scan signal under attack with Gate-15 pending) with the
> second-order monopole residual κ⁽²⁾ = 0 per unit ε²
> (at/below floor_J2 = 3.241 per unit ε², P133-2) at the
> amplitude price (δβ⁽²⁾, δk⁽²⁾, a_e⁽²⁾)·ε² = (−0.271448,
> +2.61×10⁻⁹, −0.027400) — excursions of 0.1267 of
> β_MK = 2.142611 r₀ and 0.0274 of 1 respectively, so the
> registered perturbativity bar (each excursion smaller than
> the quantity it corrects) is met; the shell sign at second
> order, at both mouths, is Ŝ⁰⁰/α₀ = +0.0202914453
> (first-order margin) − 0.0162648021 (second order,
> Ŝ⁰⁰⁽²⁾ε² with Ŝ⁰⁰⁽²⁾ = −162.648 per unit ε²) −
> 3.07×10⁻¹⁰ (measured ℓ ≥ 4 tail, P133-3) = **+0.00402664
> > 0**; the EFFECTIVE transit gains (C12 accounting) with
> their O(ε²) remainders are G_τ = 23.00840 with remainder
> interval [23.00838, 23.00844] and G_t = 17.31288 with
> remainder interval [17.31288, 17.31290], from
> ΔL_ext⁽²⁾ ⊂ [−0.044, +0.085] r₀ — both intervals exclude
> G = 1; and the thresholds are D*_τ = 4016.023 r₀ with
> FORMAL shift interval [4016.005, 4016.034] r₀ and
> D*_t = 3592.719 r₀ with FORMAL shift interval
> [3592.692, 3592.741] r₀ (FORMAL: break-evens below the
> construction domain D ≥ 10⁴ r₀). Formation standing:
> PRE-EXISTING ONLY. **(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

Extension rows (not part of the deciding statement): at
ε = 0.003 the shell sign at second order is +0.01882761 and
at ε = 0.001 it is +0.02012880, with the perturbativity bar
met at both rows (§4).

## 6. Scope and named remainders

Second order in amplitude only; ℓ = 0 sector's price only
(P141-4 prices ℓ ≥ 1 — coordinator reconciliation if its
summed shell correction moves the ε = 0.01 read, per §1).
Third-order terms and modes ℓ ≥ 4 at second order are named
remainders (the ℓ ≥ 4 *tail bound* at first order in the
matching system is included above via P133-3's measured
coefficients; that is not a second-order ℓ ≥ 4 price). The
tail is a measured-pattern bound, not a proof for all ℓ.
Formation standing: PRE-EXISTING ONLY. INTERNAL only;
nothing uploaded; nobody contacted.

**Follow-ups:** none are required by this verdict (no read
failed, so the failure protocol's anatomy-plus-follow-up
clause is not triggered). The standing queue items that
touch this statement are P141-4's reconciliation (above)
and the phase's named remainders (third order; ℓ ≥ 4 at
second order).

## 7. Files

`results/p1413_results.json` (deciding record),
`results/p1413_checker.json` (31/31 PASS) from
`work/p1413_checker.py`; compute script
`work/p1413_compute.py`; implementation fixed in advance in
`work/p1413_runrecord.md`. CHECKPOINT141.md not edited.
