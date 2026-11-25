# P116-1 — THE β = 0.0725 BISECTION (FU-P962-1)

## VERDICT: CEILING TIGHTENED TO (0.0725, 0.075)

**Category: PAYLOAD TRANSPORT only.** The outer shell alone
at β = 0.0725 is legal at the ±0.10W span, and the composed
row built on it — inner β = 0.06, outer β = 0.0725, span
±0.10W — is legal under the full gate-standard audit at a
held-W payload of **0.0975831574914493c**, above the
Phase-88 row's 0.09556c. This is a phase-verified row in
the payload category; it is NOT gated. The standing
verified mark in this category remains **0.0799c** (Phase
46, Gate-8 restated scope) until a Gate rules on the
Phase-80/88/116 rows. Phase-verified rows now: 0.08745c
(Phase 80), 0.09556c (Phase 88, corroborated Phase 96),
0.09758c (this item, with an independent second path,
§3). No bare-shell comparison is made or implied (the
Procaccia 0.1363 mark is a different category).
Checker: `p1161_check.py`, **22/22 PASS**.

## Plain language

Phase 96 found the outer shell, run alone, breaks at speed
0.075 but survives at 0.07, and left one rung in between to
test: 0.0725. That rung survives — at the wider of the two
fade spans, the shell alone is fully legal, and only at
the tighter span does it fail, in one small patch at its
outer fade edge. Because the shell alone is legal at the
wide span, the two-shell payload row built on it could be
assembled, and it passes every legality test at payload
speed 0.0976c — a new best for this programme's
phase-verified payload rows, up from 0.0956c. It has not
been through a Gate, so the official verified mark stays
0.0799c. The speed ceiling for the outer shell alone is
now pinned between 0.0725 and 0.075.

## 1. Control (before any Phase-116 number) — PASS

Reproduced on this phase's copied machinery
(p1161_control.py; reference phase96/results/
p962_control.json):

- **(a) 0.0799 cosine cavity, Gate-8 settlement standard:**
  wa_diag 4th-order stencil-clear cavity DEC
  +1.623×10⁻⁴ / +2.010×10⁻⁴ / +1.977×10⁻⁴ (h = 0.15 /
  0.075 / 0.0375), Type-I 1.000 at every rung; raw
  near-edge reads negative and non-monotone in h;
  Minkowski max|G| = 0.0.
- **(b) 0.09556 composed row from stored vectors:**
  payload 0.0955573262914437c exactly; regional worsts at
  h = 0.15: payload +3.840×10⁻⁶, inner wall +1.190×10⁻³,
  outer wall +3.351×10⁻⁵, exterior +1.107×10⁻⁶ (the
  registered classes); Type-I 1.000; cavity decided by the
  settlement ladder (stencil-clear −1.527×10⁻⁴ →
  +9.50×10⁻⁵ → +1.631×10⁻⁴).
- **(c) Alone cells at ±0.10W from Phase-96 stored
  vectors:** β = 0.07 alone-legal (Type-I 1.000, sampled
  NEC −2.17×10⁻⁷, the fixed exterior floor read);
  β = 0.075 alone-illegal with Type-I 0.772 and sampled
  NEC −9.91×10⁻⁵ at h = 0.15 — the registered FAIL,
  including its fringe anatomy (interior Type-I 0.43,
  fringe_hi 0.54, wall and fringe_lo clean).

## 2. The q-read (registered substitution)

The Phase 88/96 audit lineage carries **no q channel**: its
auditor returns the Hawking–Ellis eigenvalue margins, the
Type-I classification, and the sampled-null NEC only (the
letter q in the lineage is the chain source's design
exponent, g0 = (rhohat ** q) · tanh((r_m−r)/0.05) ·
exp(Σ a_i B_i(r)) — a construction parameter, not a read).
Per the checkpoint's substitution clause, stated in the
run record BEFORE computing: the q-read for every new cell
is the sampled-null NEC — "Min over Fibonacci null
directions of That_ab k^a k^b, k=(1,n)" (162 directions) —
reported per cell and per fringe region, with the chain
block (λ, k, S_lo−1, S_hi, balance, monotonicity) as the
chain-flux anatomy. The polished vectors' q exponents are
x[12] = 1.12729 (±0.10W) and 1.13427 (±0.075W).

## 3. Registered cells — outer shell ALONE at β = 0.0725

Full gate-standard audit (Type-I + sampled-null + margins,
full volume) at h ∈ {0.3, 0.15, 0.075}; polish by
continuation in β from the stored β = 0.07 vector of the
same span (Phase-96 settings unchanged; scores
+1.555×10⁻⁴ / +1.559×10⁻⁴, the β = 0.07 class). Legality
under the standing Phase-88 criterion (p1161_common,
checker-recomputed):

| span | Type-I (h=0.15) | sampled NEC (h=0.15) | alone-legal |
|---|---|---|---|
| ±0.10W | 1.000 | −2.17×10⁻⁷ ‡ | **YES** |
| ±0.075W | 0.99445 | −8.86×10⁻⁶ | NO |

‡ the fixed exterior floor read, identical across β and
spans (worst DEC −5.01×10⁻⁷ in the exterior at h = 0.15,
flipping positive at h = 0.075: worst +5.31×10⁻⁷, sampled
NEC +6.01×10⁻⁷) — the Phase-80 artefact signature, carried
by the criterion's h-convergence clause exactly as at
β = 0.07.

**Fringe anatomy at h = 0.15** (Type-I / worst / q-read):

| region | ±0.10W | ±0.075W |
|---|---|---|
| interior | 1.000 / +7.64×10⁻⁷ / +6.50×10⁻⁷ | 1.000 / +7.72×10⁻⁷ / +6.69×10⁻⁷ |
| fringe_lo | 1.000 / +1.55×10⁻⁴ / +1.06×10⁻⁴ | 1.000 / +2.35×10⁻⁴ / +1.80×10⁻⁴ |
| wall | 1.000 / +1.40×10⁻⁴ / +3.24×10⁻⁵ | 1.000 / +1.40×10⁻⁴ / +2.68×10⁻⁵ |
| fringe_hi | 1.000 / +1.68×10⁻⁵ / +2.04×10⁻⁶ | **0.904 / +9.11×10⁻⁶ / −8.86×10⁻⁶** |
| exterior | 1.000 / −5.01×10⁻⁷ / −2.17×10⁻⁷ ‡ | 1.000 / −5.01×10⁻⁷ / −2.17×10⁻⁷ ‡ |

**The ±0.075W failure** is a single fringe_hi non-Type-I
patch: its eigenvalue worst stays positive (+9.11×10⁻⁶) —
what fails is the Type-I/sampled-null leg — and it does
NOT converge away with h (fringe_hi Type-I 0.904 →
0.865 and q-read −8.86×10⁻⁶ → −1.02×10⁻⁵ from h = 0.15 to
0.075), so the criterion's convergence clause cannot
carry it. Chains are clean at both spans (balance
≤ 2.1×10⁻¹⁶, monotonicity exact; ±0.10W: λ 0.95902,
S_lo−1 −4.335×10⁻³, S_hi +9.433×10⁻³; ±0.075W: λ 0.91676,
S_lo−1 −6.132×10⁻³, S_hi +1.321×10⁻²).

**Anatomy vs β = 0.075 (the registered question — does
the interior/fringe_hi split move with β or saturate?):**
it MOVES. At β = 0.075 the failure lived substantially in
interior-classified points (Type-I 0.43 at ±0.10W) plus
fringe_hi/exterior, with sampled NEC −9.91×10⁻⁵. At
β = 0.0725 the interior component is gone at both spans
(interior Type-I 1.000, worst in the +7.6×10⁻⁷ floor
class), the failure depth has shrunk by an order of
magnitude, and at ±0.10W nothing remains beyond the
settled exterior floor. The split is not saturated at the
0.075 pattern; the interior failure switches off between
0.075 and 0.0725, leaving a fringe_hi-only binding at the
tighter span.

## 4. Economics before legality, then the composed rows

Because β = 0.0725 is alone-legal at ±0.10W, the held-W
payload sums were frozen to `p1161_economics.json` BEFORE
any composed legality read (freeze timestamp carried into
the composed file; checker-verified; design vectors
bit-exact against the alone and Phase-80 stored vectors):
(0.0725, 0.06) = **0.0975831574914493c** and
(0.0725, 0.05) = 0.09118184734247374c at both outer spans;
the ±0.075W rows are frozen with alone_legal_outer =
False and were never audited as composed rows.

**Composed audit** (full gate standard over both shells
AND the cavity; cavity under the Gate-8 settlement
standard as re-derived in the control):

| row | payload | Type-I (h=0.15) | sampled NEC | payload / inner wall / outer wall / exterior worsts | ladder stencil-clear h=0.075 | legal |
|---|---|---|---|---|---|---|
| e0.10_o0.0725_i0.06 | **0.09758c** | 1.000 | +1.126×10⁻⁶ | +3.836×10⁻⁶ / +1.191×10⁻³ / +3.394×10⁻⁵ / +1.107×10⁻⁶ | +9.484×10⁻⁵ | **YES** |
| e0.10_o0.0725_i0.05 | 0.09118c | 1.000 | +1.126×10⁻⁶ | +3.847×10⁻⁶ / +1.039×10⁻³ / +3.394×10⁻⁵ / +1.107×10⁻⁶ | +9.491×10⁻⁵ | YES |

The deciding row's cavity: raw worst −1.131×10⁻⁴ (DEC at
r ≈ 4.527) at h = 0.15, decided by the settlement ladder
(stencil-clear −1.541×10⁻⁴ → +9.484×10⁻⁵ → +1.631×10⁻⁴;
focused −1.856×10⁻⁴ → +1.239×10⁻⁶ → +1.437×10⁻⁵; Type-I
1.000 on every rung) — the same settlement pattern as the
0.09556 row's. Conservation rel. median 0.0117 (i0.06) /
0.0146 (i0.05), in the Phase-96 rows' 0.0117–0.0167 class.

**Independent second path (deciding row, required before
integration):** two discretisations different in kind,
same point set, h = 0.15 — wa_diag 4th-order worst
−2.588×10⁻⁶ and Phase-1 judge worst −3.242×10⁻⁶, both
Type-I 1.000: the settled cavity floor class, the same
site class as the 0.09556 row's own second path in
Phase 96 (−2.20×10⁻⁶ / −2.84×10⁻⁶). Every other region
is positive on both paths.

**Payload consequence:** the alone pass stands as the
bracket read (0.0725, 0.075), and the composed row above
0.09556c at full legality, second-pathed, is the item's
payload result: **0.09758c, phase-verified, NOT gated.**

## 5. C12 accounting

All speeds subluminal; both shells are pre-existing
configurations (pre-arrangement by ≤ c signals);
construction-inclusive arrival ≥ D/c. No formation claim.
The result is a prescribed-geometry audit under the
programme's shell standard: the required source satisfies
the energy conditions; no matter model, stability, or
formation route is claimed. Category: payload transport
only. The row is phase-verified, NOT gated; the standing
verified mark in the category remains 0.0799c until a Gate
rules on the Phase-80/88/116 rows.

## 6. Follow-ups (Failure Protocol)

1. **FU-P1161-1 — Bisect (0.0725, 0.075) alone.** One rung
   remains: β = 0.07375 at both spans decides whether any
   of the (0.075, 0.06) prize's remaining headroom exists,
   and whether the fringe_hi-only binding at ±0.075W is
   the last component standing at 0.0725's tighter span.
2. **FU-P1161-2 — The ±0.075W fringe_hi patch at
   β = 0.0725.** The failure is a non-Type-I patch with
   positive eigenvalue margins whose sampled NEC does not
   converge in h; P116-3's stencil anatomy (same phase)
   bears directly on whether such patches are genuine or
   stencil-carried — its design rule should be read
   against this cell before any tighter-span rescue is
   attempted.
3. **FU-P1161-3 — Gate referral.** The 0.09758c row is a
   Gate candidate alongside the unaudited-by-a-Gate
   0.08745c/0.09556c rows; the Gate line is the parent's,
   and this item does not await it.

## Files

Scripts (`phase116/work/`): `p1161_lib.py`,
`p1161_common.py`, `p1161_control.py`, `p1161_alone.py`,
`p1161_compose.py`, `p1161_verify.py` (copied p962
lineage), plus the interim stdout drivers
`p1161_econ_stdout.py`, `p1161_compose_stdout.py`,
`p1161_verify_stdout.py` (environment-incident
workarounds, run record §4 D2 — the final stored result
files were produced by the original scripts).
Results (`phase116/results/`): `p1161_control.json` +
`.log`, `p1161_alone.json` + `p1161_alone_state.json` +
`.log`, `p1161_economics.json`, `p1161_composed.json`,
`p1161_verify_e0.10_o0.0725_i0.06.json`,
`p1161_check.py` + `p1161_check.json` (22/22 PASS),
`p1161_run_record.md`. INTERNAL only.
