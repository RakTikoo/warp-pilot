# P245-1 MEMO — PHASE 245 ITEM 1 (C1): THE CAPS AUDIT

Item: Phase 245 item 1. Registration:
`phase245/work/p2451_registration.md` (audit questions, control,
probes, verdict forms fixed BEFORE any deciding computation).
Driver: `phase245/work/p2451_driver.py`; continuation:
`phase245/work/p2451_continuation.py`; independent checker:
`phase245/work/p2451_check.py` — **ALL PASS** (12/12, from the
results files alone). Machine-readable record:
`phase245/results/p2451_results.json` +
`p2451_continuation.json`. Frame of record: Phase 166 pin,
Gate-19-corrected tensor, venv python, float64. Bounded local
work only (driver 80 s / 42 true re-reads; continuation 44 s);
no ledger append; no launches; no user contact.

## VERDICT (registered form, verbatim)

**A CAP WAS CONSERVATIVE**

Named cap: **the discipline worsening cap W(d) ≤ 0.05** — the
single scalar cap over the 39 C*/shadow discipline indices
(subset indices [14..44, 48..55]) that binds at the Phase 238
floor point. Its true boundary: **there is no finite boundary
of any protected condition at or near 0.05 in this machinery**
— the conditions the cap could be proxying (dual EC legality)
remain satisfied at W = 0.6696, 13.4× the cap (fresh true
re-read, §4 P1), and the cap measurably stops pricing anything
beyond W ≈ 0.13–0.14 (§4 P2 saturation). Intrinsically rel_i ≤ 1
by the triangle inequality on the entry sum, so the cap set at
its true boundary is **no cap** (level 1.00, inactive). The
floor re-priced under it (same polish method, all other
discipline intact, every point decided by hard TRUE re-read):

**grouped max 0.238804** (median 0.167003; W = 0.1240; subset
0.5536 / binding 0.5417) — below the standing floor
0.2928769624517242 by **0.054073**. The wall was partly our own
caution: of the 0.2929 floor, ≈ 0.054 is the 0.05 cap's price
under this method; the remainder is priced by the in-cell /
margin-proxy plateau (§4), not by the caps. On the face: the
re-priced point's median (0.1670) is *worse* than the floor
point's (0.1478) — the max improved, the median did not, the
same pattern as Phase 238. No front pass is claimed (§6).

## 1. CONTROL (mandatory, first — PASS, exact)

Fresh TRUE re-read of the Phase 238 floor point (coordinates
loaded from `phase238/results/p2383_results.json`, not
transcribed), caps at standing levels:

| quantity | stored | fresh | err |
|---|---|---|---|
| grouped max | 0.2928769624517242 | 0.2928769624517242 | ≤1e-9 ✓ |
| grouped median | 0.14783526362245453 | 0.14783526362245453 | ≤1e-9 ✓ |
| W | 0.0499999999994145 | 0.0499999999994145 | ≤1e-9 ✓ |
| subset / binding | 0.5536 / 0.5377 | identical | ≤1e-12 ✓ |

All seven control reads pass (bed d=0, Exhibits A/B seeds and
Phase-238 terminals, Phase 223 11111 witness — §3 table). The
audit proceeds on a reproduced floor.

## 2. WHAT THE CAP IS AND WHAT IT PROTECTS (Q1)

**Form.** W(d) = max_i (rel_i(d) − control_rel_i) ≤ 0.05 at 39
indices, rel_i = |tot_i|/(D_i + 1e-12) over the 12 grouped
entry keys; control_rel_i is the fixed Phase 173 control
(CTRL_CSTAR_REL / CTRL_REL_ALL via the Phase 175 machinery),
inherited through Phases 179/188/205 into the Phase 223 cone,
Phase 230 X4's exact form, and Phase 238 Item 3's hard
acceptance §1(a). It is ONE scalar cap, not 39: a single
uniform +0.05 allowance over per-index control levels.

**What it protects.** Provenance, from the registrations:
Phase 164's earning criterion ("no C* worsening > 0.05 AND
shadow max worsening ≤ 0.05"), carried verbatim by Phase 173-1,
Phase 175, Phase 180 (clauses D2/D3), Phase 188, Phase 205,
223, 230, 238. Its function in every one of those registrations
is **anti-collateral discipline on the grouped score itself**:
a perturbation may not buy grouped depth (or opposition) at
its target points by worsening the grouped ratio at the other
critical points (C* = {14, 37, 40, 44, 50, 51, 52, 55}) or at
their φ-neighbours (the shadow set) by more than +0.05 over the
Phase 173 control pose.

**What it does NOT protect.** No phase in the chain derives
0.05 from, or ties it to, a ghost, gradient, or health
condition:
- Ghost/symbol: definiteness (λmin) is a separate clause,
  outside the 223/230/238 items entirely (read still owed on
  every point in this line, including the re-priced one).
- Gradient/sound-speed: the Phase 183 D5 gap and Phase 188's
  entry caps (|t_braidpp| ≤ D5 etc.) are separate disciplines
  of different item families; the entry caps are NOT in the
  Phase 238 hard acceptance test. (At the Phase 211 floor —
  the other point the task names — the extended entry cap was
  in fact *slack*: bviol_XX = −0.0524, per CHECKPOINT211.)
- EC legality: carried by its own hard clauses in the same
  acceptance test (dual fractions ≥ 0.518; margin rows as the
  proposal proxy). The cap is at most a *sufficient proxy* for
  "the pose has not drifted far from the control's grouped
  profile" — a bookkeeping discipline, adopted as a round
  number in Phase 164 and never re-derived since.

## 3. WHERE IT BINDS (anatomy, fresh true reads)

Per-index worsening at the **floor point**: three indices sit
at the cap simultaneously —

| subset idx | rel | control | worsening |
|---|---|---|---|
| **37 (argmax)** | 0.073540 | 0.023540 | **0.050000** |
| 43 | 0.097982 | 0.047982 | 0.050000 |
| 49 | 0.164840 | 0.114840 | 0.050000 |
| 21 | 0.121444 | 0.073952 | 0.047492 |
| 42 | 0.093227 | 0.046222 | 0.047005 |

(full 39-index table in `p2451_results.json:cap_anatomy`).

Elsewhere: bed d=0 — W at cap, argmax idx 21 (the bed pose was
itself selected at this cap, Phase 205). Exhibit A seed — at
cap, idx 21 (idx 16 also 0.050000). Exhibit B seed — at cap,
idx 21. Exhibit A Phase-238 terminal — caps **slack**
(W = 0.046638, idx 21): its plateau is not cap-priced, exactly
as Phase 238's anatomy said. Exhibit B terminal — at cap,
argmax idx 49. Phase 223 11111 witness — W = 0.669635, idx 49.

Non-cap discipline at the floor point (inventoried per
registration §1): dual legality 0.5536 / 0.5377 — **not
binding** (bar 0.518); trust region — not binding
(|dc|max = 3.283 < 5; da = −2.400, db = +3.324 ≪ 500);
margin-preservation rows — max violation −2.4e-10 in the
linearised proxy (the point carries 1 binding-set preserved-
margin violation of −4.9e-7 under the stricter true column,
the Phase 238 sensitivity note, unchanged); mu2 = kap =
pih = 0 sit on their non-negativity bounds, which are the
amplitude definitions of the cuscuton/ray sectors, not caps
with levels. **The worsening cap is the only discipline cap
that binds at the floor point.**

## 4. IS 0.05 THE BOUNDARY? (Q2/Q3 — no; true boundary and re-pricing)

**(P1) Legality survives 13.4× past the cap.** The Phase 223
11111 max-t witness, fresh true re-read: W = 0.669635, grouped
max 0.846885, median 0.196717, subset 0.5536 / binding 0.5298
— dual-legal, both fractions at the bed's own levels. Whatever
the cap protects, EC legality is not lost anywhere near 0.05,
nor at 0.67. (Its grouped depth is terrible — that is the
objective's own business, priced separately, not a legality
boundary.)

**(P2) Re-pricing ladder** (Phase 238 polish verbatim, bed
seed, hard TRUE re-read acceptance at each level; all other
discipline intact):

| cap level W ≤ | terminal grouped max | median | terminal W | sub / bind |
|---|---|---|---|---|
| 0.05 (standing) | 0.292877 | 0.147835 | 0.0500 | .5536 / .5377 |
| 0.10 | 0.241627 | 0.167400 | 0.1000 | .5536 / .5496 |
| 0.15 | 0.244739 | 0.162876 | 0.1299 | .5536 / .5694 |
| 0.25 | 0.244739 | 0.163750 | 0.1299 | .5536 / .5694 |
| 0.50 | 0.244739 | 0.162876 | 0.1299 | .5536 / .5694 |
| 1.00 (no cap) | 0.244739 | 0.163732 | 0.1299 | .5536 / .5694 |
| 1.00, continued from the 0.10 terminal | **0.238804** | 0.167003 | 0.1240 | .5536 / .5417 |

Reading of the ladder: (i) doubling the cap buys −0.0513 of
grouped max — the local price is steep (≈ 5× Phase 238's
+0.01-headroom probe slope, because the ladder re-polishes
rather than taking one in-cell step). (ii) **Saturation:**
from level 0.15 up, every run terminates at W = 0.1299–0.1405
along its trajectory and never uses more; the no-cap
continuation of the 0.10 terminal reaches W = 0.1240 and
plateaus with all rejects *no-improvement* (in-cell LP /
margin-proxy plateau — no step in any relaxed run was ever
rejected on legality or caps). The cap therefore has **no
pricing power beyond W ≈ 0.14** in this machinery: set there
or anywhere above, it is not the wall. (iii) The two distinct
terminals (0.2416-path vs 0.2447-path) are cell-path
dependence of the bounded polish, stated as such; the
re-priced floor of record is the best hard-true-read terminal,
**0.238804**, whose coordinates are in
`p2451_continuation.json` (dc = [−0.921, −1.348, −1.165,
−1.589, −1.251, −1.330, −2.404, −5.0, −5.0, +4.125],
da = −7.324602, db = +12.568248, mu2 = 0, kap = 0.000881,
pih = 0). At that point the cap argmax (idx 49,
rel = 0.238804) *is* the grouped max — the former cap index
has become the objective's own binding point, which is where
a no-regression allowance stops meaning anything separate
from the score.

**True boundary, stated precisely.** The protected condition
in its literal form — "no worsening beyond the allowance" —
has its boundary at the allowance *by definition*; the audit
question is whether 0.05 marks any *underlying* condition's
edge, and it does not: not legality's (P1: intact at 0.6696),
not the objective's (rel ≤ 1 intrinsically; the pass bar is
0.02, far below every control rel the cap references), not
any ghost/gradient condition's (none is attached to it in any
registration). The cap is a conservative sufficient bound for
profile-drift discipline whose underlying hard conditions are
all separately enforced and separately satisfied far beyond
it. Its effective boundary — where it stops pricing — is
measured at W ≈ 0.13–0.14; its formal removal (level 1.00)
changes nothing beyond that, and the floor under it is
0.238804.

## 5. WHAT THIS DOES AND DOES NOT RETIRE

The verdict retires the *level*, not the discipline's
usefulness as a reporting column: W remains a meaningful
drift measure, and the standing floor 0.2928769624517242
remains the floor *under the standing discipline* — the
record now carries both numbers with the price of the
difference named (0.054073, under this bounded method).
Whether the programme *adopts* the relaxed discipline is a
framing decision above this item; this memo only prices it.
The re-priced point is an in-cell-plateau terminal of a
bounded polish, not a global floor proof, and it inherits
every fence of the point it displaces.

## 6. FENCES

Set reads on the subset-56 frame; grouped values are set
reads, not continuum bounds. Symbol discipline (λmin) is
outside this item — the re-priced point owes that read before
any use as a front candidate, exactly as the Phase 238 point
does. No front pass is claimed: 0.238804 is nowhere near the
0.02 bar. NO-EXOTIC total-stress standard: all legality reads
here are the front bed's full-stress EC machinery of record
(Phases 223/230/238); no throat/payload legality wording is
issued. Phase 230's census acquittal is untouched and
consistent: the caps never blocked *patterns*; this audit
adds that their level was also never a *condition's* boundary
— it was pricing depth all along, at a rate the programme set
by convention in Phase 164.

No ledger append; no launches; no external contact.
