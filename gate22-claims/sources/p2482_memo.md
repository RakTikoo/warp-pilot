# P248-2 (Item 2 — THE DRIFT ANATOMY + κ-TRIM TRANSFER) — memo

Worker W248-2, 2026-11-24. Registration (written BEFORE any
deciding computation; one amendment, A-1, recorded in it after
the Part A fits were printed but before any Part B march — see
§2): `phase248/work/p2482_registration.md`. Driver:
`phase248/work/p2482_run.py`; checker:
`phase248/work/p2482_check.py` (**ALL PASS, 23/23**, including
fresh spot recomputation of both trimmed bracket instants at
diff 0.0); numbers: `phase248/results/p2482_results.json`,
`phase248/results/p2482_verify.json`. Frame of record: Phase
166 pin, Gate-19-corrected tensor, venv python, float64. Total
stress = G/8π (GR) — the NO-EXOTIC total-stress standard is
the read itself. Datum ≠ construction. INTERNAL only; no
ledger append, no launches, nobody contacted; nothing outside
`phase248/` edited (protected-file md5s identical
before/after, checker-verified live).

## Verdict (registered form 1, verbatim in substance)

**SAME FORCED MODE — TRIM TRANSFERS AT A PRICE** — Part A
identifies the composed failure as the P169-1 μ-drift forced
mode (§§1–3: decomposition exact at 0.0, forced-t² fit
evidence priced, rotation's coefficient effect exactly 0.0).
The trimmed arm's refined bracket is **(0.525, 0.53125]**,
carrier NEC_φ = DEC_φ — an extension of **+0.0375** past the
untrimmed composed (0.4875, 0.49375], but it does **not**
reach the wound pose's certified (0.55625, 0.5625] (short by
≥ 0.025). The price: the law's coefficient is so large that
the |a| ≤ 0.8 cap **clamps at t = 0.23897** and the arm runs
at the cap (a = −0.8, peak |a| = 0.8, **cap headroom left:
0.0**) for the entire approach to the crossing. The wound
line's stabilisability result is therefore transferred AS A
PRICED READ at this datum — the open-loop t² trim does buy
real lifetime — not as a certificate (certification would be
a successor), and the priced read itself shows the transfer
is cap-limited, not law-limited, past t ≈ 0.24.

## 1. Part A1 — the failure decomposes exactly

composed NEC_φ,min(t) = headline NEC_φ,min(t) + lift(t) at
all 41 stored sampled instants: **max deviation 0.0**. There
is no decomposition discrepancy to price. At the refined
bracket the identity reads, arithmetically:

| t | headline | + lift | = composed |
|---|---|---|---|
| 0.4875 | −0.542734 | +0.551248 | **+0.008513** |
| 0.49375 | −0.585516 | +0.549606 | **−0.035909** |

Between the bracket ends the headline drift term falls by
0.042781 while the lift erodes by only 0.001641: **the term
whose growth carries NEC_φ through zero is the headline
drift itself** (96% of the bracket-interval drop), the lift
being nearly constant there. Both arms' NEC_φ argmin sits at
index 90 (θ*) at both bracket instants and at every sampled
instant of the holding intervals — no argmin migration, no
new locus.

## 2. Part A2 — mode identification, fits priced

Least-squares fits of NEC_φ,min(t) (full / forced-t² /
linear; coefficients, RMS residuals):

**Headline arm, window [0, 0.375]** (its holding interval):
- full: c₀ = +0.585128, c₁ = +0.280588, c₂ = −4.629047;
  RMS 0.005709, max |resid| 0.012013.
- forced-t²: c₀ = +0.604014, c₂ = −3.932798; RMS 0.010259
  (1.80× the full form's), max |resid| 0.023588.
- linear: c₀ = +0.686389, c₁ = −1.455304; RMS 0.054962
  (9.6× the full form's) — decisively rejected.
- The forced fit's crossing root is **t = 0.391898**, inside
  the stored sampled bracket (0.375, 0.400]. The linear
  term's window contribution (0.105) is 16% of the quadratic
  term's (0.651).

**Composed arm, window [0, 0.475]:**
- full: c₀ = +1.191968, c₁ = +0.651959, **c₂ = q₂ =
  −6.062835**; RMS 0.017171.
- forced-t²: c₀ = +1.248084, c₂ = −4.783825; RMS 0.029946
  (1.74× full).
- linear: RMS 0.113573 (6.6× full) — rejected.

**Lift(t), window [0, 0.475]:**
- full: c₀ = +0.625709, c₁ = −0.018405, c₂ = −0.280631;
  RMS 0.000404 — the lift is fit almost exactly.
- forced-t²: c₀ = +0.624125, c₂ = −0.316739; RMS 0.000802.
- Classification (registered rule): **T²-ERODING, weakly** —
  over the window the linear term contributes 0.0087 and the
  t² term 0.0633, against a lift level of ≈ 0.625: total
  erosion ≈ 0.072 (12%) over [0, 0.475], carried by the t²
  term. The lift is neither constant nor the crossing's
  driver; the drift outruns it by an order of magnitude.

**Amendment A-1, on the face.** The registration's original
forced-form sub-criterion (|c₁|·t_max ≤ 3 × RMS(full))
compared the linear term against the fit-noise scale and
fails the headline form on that clause alone (0.1052 vs bound
0.0171), while the RMS clause (1.80 ≤ 2) and the crossing
criterion both pass. A-1 — recorded in the registration after
the fits were printed and BEFORE any Part B computation —
replaced that sub-criterion with the scale-correct one
(|c₁|·t_max ≤ 0.25 × |c₂|·t_max²; headline: 0.105 ≤ 0.163
✓). Under the amended rule the forced-t² form is supported
for both arms; under the original rule it is not, and that
fact is part of this record. The verdict does not rest on the
fit form alone: it rests jointly on the exact decomposition
(§1), the bit-identity to P169-1 (§3), and the forced root
landing in the sampled bracket.

## 3. Part A3 — same mode, priced against the wound record

- The headline datum IS the P169-1 compensated datum:
  Item 1's CTRL-1/CTRL-3 chain gives NEC_φ first fail 0.400,
  worst −0.6297872673028908 at t = 0.5, bit-identical across
  ω_a = 0 / 0.2 (Phases 245 C3, 246 CTRL-3). Direct check
  here: Item 1's headline NEC_φ,min trajectory vs Phase
  245's stored ω_a = 0 baseline (`p2452_results.json`,
  `/main_read/wa0_baseline`): **max diff 0.0 over [0, 0.5]** —
  rotation's effect on the drift coefficients is exactly
  0.0, as expected (Phase 245 §4 face fact 1: the carrier is
  rotation-neutral; the NEC_φ argmin sits at θ* throughout).
- Against the wound line's own characterisation
  (`phase208/results/p2085_memo.md` §2): the failure is the
  particular solution, not an instability — μ(·,t) ≈
  (t²/2)·ũ(θ) growing along the ũ profile while A(θ*,t)
  shrinks 0.8 → 0.6859, carrying NEC_φ(θ*) through zero
  between 0.375 (+0.027376) and 0.400 (−0.072157); the march
  spectrum is neutral (no eigenvalue with real part > 1e-9).
  The fitted headline trajectory is exactly that shape: a
  t²-dominated decline (forced-fit c₂ = −3.93, root 0.3919)
  on the same datum, same carrier clause, same argmin locus.
  (`phase169/results/p1691_memo.md`: the μ-frozen isolation
  +0.170956 at 0.425 names the μ-drift as the carrier on this
  datum.) **Same forced mode.**

## 4. Part B — the trim, priced

**Controls (run first; all PASS).** (iii) Static pin:
S(θ*) = −4.0625, NEC_ρ min = −4.0625, identity dev ≤
8.9×10⁻¹⁶. (i) c_trim = 0 arm reproduces Item 1's composed
stored reads at **diff 0.0** on [0, 0.5] (all seven clauses,
all statistics, 21 instants). (ii) One trimmed march length
(T_END = 1.0), per registration B4(ii): Item 1's CTRL-2
covers this machinery class, and here the T_END = 1.0 march's
MU/U rows 0–200 are bit-identical to the T_END = 0.5 march's
(the Auu law is a read-level offset downstream of the march
state); the checker spot-recomputed both bracket instants
fresh at diff 0.0.

**Coefficient (fixed formula, registration B1).**
q₂ = −6.062835 (composed full fit, §2); s̄ = 1.154083 (mean
of Phase 246's stored gain-signed Auu sensitivities at the
argmin: 1.207062 / 1.146183 / 1.109004);
**c_trim = −q₂/s̄ = +5.253378**. Unclamped, the law
a(t) = −0.5 − 5.253378 t² would reach |a| = 1.81 at t = 0.5;
the cap binds at **t_clamp = √(0.3/c_trim) = 0.238969**, and
a(t) = −0.8 from there on. **PR-φ (adapted) PASS 41/41**:
offset extraction returns the law's (clamped) value exactly
at every instant; mom residuals ≤ 1.3×10⁻¹⁵ class; liveness
> 1e-3 everywhere.

**Trimmed read.** Sampled bracket (0.525, 0.55]; ladder
(0.5375 fails, 0.53125 fails) → **refined bracket
(0.525, 0.53125]**, width 0.00625, carrier NEC_φ = DEC_φ at
both ends (margins +0.042998 → −0.012405; next clause NEC_ρ
≥ +1.82). Auxiliary-march (h_t = 0.00125) price at the
sampled ends ≤ 4.8×10⁻¹⁰, as in Item 1. Margin trajectory of
the carrier (trimmed): +0.425791 (0.475) → +0.246943 (0.5) →
+0.042998 (0.525) → −0.190449 (0.55).

**Three-bracket table:**

| datum | first-crossing bracket | carrier |
|---|---|---|
| Untrimmed composed (Item 1) | (0.4875, 0.49375] | NEC_φ = DEC_φ |
| **Trimmed, P-PHI-TRIM-248 (this item)** | **(0.525, 0.53125]** | NEC_φ = DEC_φ |
| Wound pose, certified (Phase 243) | (0.55625, 0.5625] | NEC_φ = DEC_φ |

**Why the extension stops where it does (priced).** Past the
clamp instant the "trim" is a flat a = −0.8 channel: the
extra lift over the untrimmed datum is the constant
0.3 × (local sensitivity ≈ 1.1) ≈ +0.33, while the drift
keeps its t² growth — by t = 0.55 the headline deficit is
−1.046, beyond what any capped flat amplitude repays.
Descriptive flat price (stored rows only, registration B5):
carrying the untrimmed crossing to 0.5625 would need the
flat amplitude **a\* = −1.517513** (headline deficit at
0.5625, interpolated, D = 1.174294, over s̄) — **outside the
|a| ≤ 0.8 cap by 0.72**. The transfer's limit at this datum
is the cap, stated plainly: the wound line's κ had cap
headroom (κ_req(0.5) = 0.2978 against κ ≤ 1); this datum's
analogue dial does not.

## 5. Scope fences

Jet scope; sampled/refined-instant reads; the trimmed arm is
a NEW posed datum under a law fixed in advance (Item 1's
datum and verdict untouched); no certificate is claimed for
any bracket here (Phase 243's covers the wound pose only);
open-loop trim ≠ the closed-loop stabilisability proof of
Phase 208 (and Phase 217's closed-loop V2 in fact failed) —
the transfer tested is of the priced effect, stated as such.
Datum ≠ construction. Total stress = G/8π is the read itself
(NO-EXOTIC standard).

## Files

- `phase248/work/p2482_registration.md` — registration +
  Amendment A-1 + P-PHI-TRIM-248 + controls + verdict forms,
  written before computation (A-1 before Part B).
- `phase248/work/p2482_run.py` — driver (Part A fits, controls,
  trimmed march, PR-φ, ladder, verdict).
- `phase248/work/p2482_check.py` — checker, ALL PASS (23/23).
- `phase248/results/p2482_results.json` — full reads.
- `phase248/results/p2482_verify.json` — checker record.
- `phase248/results/p2482_memo.md` — this memo.
