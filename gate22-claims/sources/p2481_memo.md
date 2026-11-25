# P248-1 (Item 1 — THE MARCH) — HOW LONG DOES THE COMPOSED
# COMBINED-CLASS DATUM LIVE?: memo

Worker W248-1, 2026-11-24. Registration (written BEFORE any
deciding computation): `phase248/work/p2481_registration.md`.
Driver: `phase248/work/p2481_run.py`; checker:
`phase248/work/p2481_check.py` (**ALL PASS, 37/37**, including
fresh spot recomputation of both bracket instants at diff 0.0);
numbers: `phase248/results/p2481_results.json`,
`phase248/results/p2481_verify.json`. Frame of record: Phase 166
pin, Gate-19-corrected tensor, venv python, float64. Total
stress = G/8π (GR) — the NO-EXOTIC total-stress standard is the
read itself. Datum ≠ construction. INTERNAL only; no ledger
append, no launches, nobody contacted; nothing outside
`phase248/` edited (protected-file md5s identical before/after,
checker-verified live).

## Verdict (registered form 2, verbatim in substance)

**OUTLIVED BY THE WOUND POSE** — the composed combined-class
datum's refined first-crossing bracket is **(0.4875, 0.49375]**,
carrier **NEC_φ = DEC_φ** at both ends, and it falls short of
the wound pose's Gate-23-certified bracket (0.55625, 0.5625] by
more than 0.06 in t — no overlap, no straddle. The
combined-class line's value therefore stands as the **NEC_ρ pin
break (Phase 245)**, not sustainment: the CH-PHI-Auu channel
buys the datum a large NEC_φ lift and a much larger NEC_ρ
margin, but the μ-drift carrier still crosses zero before
t = 0.5, earlier than the wound pose's certified crossing.

## 1. The datum marched

Phase 245's combined-class datum (P167 compensated pose, true
lock P169-1 engine, gauge u(0,t) = 0, lock h_t = 0.0025, fine
grid 2881, audit grid 181, rotation ω₀ = 0.2 sin²θ, W₁ = 0)
composed with the φ-channel under **P-PHI-FROZEN-246 carried
exactly as Phase 246 posed it**: flat Auu offset a = −0.5 on
every instant's jet dict, after `comp_jets` + rotation jets,
before the pointwise Wuu solve from mom_φ = 0; no feedback
into the lock, the march, or Fuu; no per-instant adjustment;
no amplitude sweep in this item. The march was extended to
T_END = 1.0 (41 sampled instants every 0.025), i.e. a full 0.5
past the first sampled crossing — the ≥ 0.1 continuation rule
is met five times over. The headline (no-channel) arm was
marched alongside as the lift baseline.

**PR-φ at every sampled instant of the extension: PASS**
(41/41): offset extraction exact (PR-φ-1), mom_φ residual
after the Wuu re-solve ≤ 1.30×10⁻¹⁵ and mom_ρ/mom_θ maxima
≤ 1.78×10⁻¹⁵ (PR-φ-2, 1e-9 class), liveness max clause diff
> 1e-3 at every instant (PR-φ-3).

## 2. Controls (run first; all PASS)

- **CTRL-1 — Phase 246 reproduction at its own length
  (T_END = 0.5): PASS, diff 0.0 everywhere.** Per-instant
  clause minima of the composed primary arm and the headline
  arm reproduce `p2462_results.json` at max diff **0.0**
  (full composed profiles also 0.0). Named anchors: worst
  over [0, 0.475] NEC_φ = DEC_φ = **+0.09308944759980875 at
  t = 0.475**; NEC_ρ worst over [0, 0.475] **+1.295071336714695
  at 0.475**; first failure t = 0.5 at NEC_φ = DEC_φ =
  **−0.08183078979932734**; headline arm NEC_φ first fail
  0.400, worst −0.6297872673028908 at 0.5.
- **CTRL-3 — static pin: PASS.** S(θ*) = −4.0625 (ω_a = 0)
  and NEC_ρ min = −4.0625 (ω_a = 0.2, Wuu solved),
  channel-vs-identity ≤ 8.9×10⁻¹⁶, mom_φ residual
  1.8×10⁻¹⁶.
- **CTRL-2 — march-length invariance: PASS on every
  verdict-carrying read, with one priced footnote.** The
  T_END = 1.0 extension march reproduces the [0, 0.5]
  composed reads at **exactly 0.0** in every per-instant
  clause statistic (min/median/max/argmin, all seven clauses,
  all 21 instants), in S(θ*), in the θ* identity
  decompositions, and in the momentum maxima. The ONLY
  nonzero diffs anywhere are **54 individual clause-profile
  entries at t = 0.5, each ±1–2 ulp (max 4.440892098500626×10⁻¹⁶)**,
  in NEC_θ/NEC_φ/DEC_θ/DEC_φ, moving no statistic. Anatomy
  (the Phase 240 class, priced, stored in the results JSON):
  between the two marches the MU and U rows 0–200 are
  bit-identical and the MTT rows 0–199 are bit-identical;
  MTT at row 200 (t = 0.5) differs by up to
  1.5413×10⁻⁵ on the fine grid — the short march's final-index
  one-sided stencil vs the long march's centred stencil,
  exactly the Phase 240/243 mechanism. MTT feeds only the
  Fuu jet (`comp_jets`), and its propagation into the
  diagonal clause pipeline at t = 0.5 is at roundoff, as
  priced. Disclosed plainly: under a profile-bitwise reading
  of CTRL-2 those 54 ulp entries would fail the gate; under
  the registration's own definition of the reads (CTRL-1's:
  per-instant clause minima and the statistics built on
  them) the gate passes at 0.0, and no bracket-carrying
  number is within 10¹³ of the diff scale. The bracket
  instants themselves (§3) sit at t < 0.5 in the primary
  march's interior or are independently priced (§3, aux
  price), so the t = 0.5 stencil point carries no verdict
  weight.
- **Cost rule: does not fire.** CTRL-1 march wall 3.9 s
  (driver total 23.4 s including the auxiliary refinement
  march); projection for T_END = 1.0 was 38.9 s ≤ 900 s. No
  kernel spec was owed.

## 3. The bracket

Sampled bracket (extension march, composed arm): all seven
clauses hold at every sampled instant of [0, 0.475]; first
sampled failure at **t = 0.5**, carriers NEC_φ = DEC_φ =
−0.081831, every other clause still ≥ +1.21. Halving ladder:

| t | source | NEC_φ = DEC_φ min | all seven hold? |
|---|---|---|---|
| 0.475 | primary march (sampled) | +0.093089 | yes |
| 0.4875 | primary march (step 195) | **+0.008513** | yes |
| 0.49375 | auxiliary march h_t = 0.00125 (step 395) | **−0.035909** | **no — NEC_φ = DEC_φ** |
| 0.5 | primary march (sampled) | −0.081831 | no |

**Refined bracket: (0.4875, 0.49375], width 0.00625.**
Bracket-end margins: at 0.4875 the binding margin is
NEC_φ = DEC_φ = +0.008513 (next-smallest clause NEC_ρ =
+1.255470); at 0.49375 NEC_φ = DEC_φ = −0.035909 (NEC_ρ =
+1.235080). Carrier at both ends: NEC_φ = DEC_φ, the A
branch's known μ-drift carrier — the same carrier as the
wound pose's certified bracket.

Auxiliary-march price (on the face): odd multiples of
0.00625 are not stored steps of the h_t = 0.0025 march, so
t = 0.49375 was read from an auxiliary march at
h_t = 0.00125, same engine and discipline; its clause-min
reads at the two sampled bracket ends differ from the
primary march by ≤ 6.1×10⁻¹¹ (NEC_ρ) and ≤ 1.9×10⁻¹³
(NEC_φ) — four-plus orders below every bracket-end margin.
The checker re-ran both bracket instants fresh (primary
march for 0.4875, auxiliary march for 0.49375) and
reproduced the stored clause minima at diff 0.0.

Margin trajectory of the carrier (composed arm, grid min of
NEC_φ = DEC_φ): +1.218750 (t = 0) → +0.093089 (0.475) → +0.008513 (0.4875) →
−0.035909 (0.49375) → −0.081831 (0.5) → −0.511139 (0.55) →
−1.852161 (0.65) → −4.431065 (0.75) → −39.451831 (1.0). The
decline is monotone at sampled instants from 0.475 on and
steepens; no sampled instant after 0.5 recovers. The channel's
lift over the headline arm at the worst region is large and
persistent (composed-minus-headline NEC_φ grid-min lift
+0.547957 at t = 0.5, full per-instant lift table in the
results JSON), but the headline arm's own drift is faster
than the flat channel's constant lift past ≈ 0.49.

## 4. The one-table comparison (form 2)

| datum | t = 0 worst margin (binding) | first-crossing bracket | binding carrier |
|---|---|---|---|
| **Composed combined-class datum** (this item) | +1.218750 (NEC_φ = DEC_φ) | **(0.4875, 0.49375]** | NEC_φ = DEC_φ |
| Headline combined datum, no channel (this item, baseline arm) | +0.431250 (NEC_ρ, at θ*) | sampled (0.375, 0.400] (NEC_φ first fail 0.400; not ladder-refined — baseline only) | NEC_φ = DEC_φ |
| **Wound pose**, three-channel (Phase 234 record; certified Phase 243) | +1.455548 (NEC_φ = DEC_φ) | **(0.55625, 0.5625]** | NEC_φ = DEC_φ |

Reading of the table: composition with CH-PHI-Auu moves the
combined datum's crossing from the headline's sampled
(0.375, 0.400] to (0.4875, 0.49375] — a real extension of
≈ +0.09 — but it does not reach the wound pose's certified
bracket; the gap at the bracket level is ≥ 0.0625 in t. Same
carrier in all three rows: the μ-drift NEC_φ/DEC_φ mode is
what ends every one of these data, and at this datum the
flat Auu channel's constant lift is outrun by it before
t = 0.5.

## 5. Past 0.5 on the record (march discipline rows)

The extension was marched to T_END = 1.0 regardless, and the
full trajectories are stored for Item 2. Headline facts past
the crossing: NEC_ρ (composed) stays positive at sampled
instants through t = 0.725 (+0.124693) and first fails at
t = 0.75 (−0.052917); S(θ*) peaks at +2.1540 (t = 0.5) and
turns negative by t = 0.775 (−0.0650); the R_,tt identity
term at θ* stays positive throughout but decays
(+2.1797 at 0.5 → +0.2073 at 1.0) while the cross-term and
angular parts erode S(θ*) — the identity decomposition at
θ*(t) is stored per instant for both arms, channel-vs-identity
grid deviation ≤ 3.6×10⁻¹⁵ at every sampled instant. By
t = 1.0 every clause has failed in the composed arm (worst
DEC_ρ −41.108 at 1.0). None of this changes the verdict,
which reads the FIRST crossing at the worst instant.

## 6. Scope fences

Jet scope; per-instant diagonal ZAMO reads at
sampled/refined instants; datum ≠ construction (no global
solution, no EOM claim). The Phase 243 certification covers
the wound pose only — nothing here inherits it, and even
form 1 would have been a READ, not a certificate
(certification would have been its named successor).
March-slice reads at this datum and wound-pose reads are
distinct poses — the comparison in §4 is of crossing
brackets under each pose's own discipline, stated as such.
A posed jet entry is posed jet data in this machinery, not
a derived derivative of a posed field (sector superposition
fence, as in Phases 229/234/246). Total stress = G/8π is
the read itself (NO-EXOTIC standard).

## 7. Item-2 handoff

`p2481_results.json` carries the full per-instant margin
trajectories for the anatomy worker: composed AND headline
arms (41 sampled instants each: per-clause min/median/max,
argmins, full clause profiles, θ* identity decompositions,
momentum maxima, Wuu residuals), the composed-minus-headline
lift per clause per instant, the refinement rows at 0.4875
and 0.49375 for both arms, the PR-φ per-instant record, and
the CTRL-2 anatomy block. No re-march is needed to fit the
drift mode from these rows.

## Files

- `phase248/work/p2481_registration.md` — registration +
  prescription + controls + bracket/cost discipline +
  verdict forms, written before computation.
- `phase248/work/p2481_run.py` — driver (CTRL-3, CTRL-1,
  cost probe, extension march, PR-φ, CTRL-2 gate, sampled
  bracket, halving ladder, verdict).
- `phase248/work/p2481_check.py` — independent checker,
  ALL PASS (37/37).
- `phase248/results/p2481_results.json` — full reads
  (see §7).
- `phase248/results/p2481_verify.json` — checker record.
- `phase248/results/p2481_memo.md` — this memo.
