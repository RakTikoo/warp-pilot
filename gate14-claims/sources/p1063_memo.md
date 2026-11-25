# P106-3 — Memo (FU-P833-2: Multi-Party QET Net Reads)

## Verdict (registered form only)

**NET NON-POSITIVE IN ALL REGISTERED MULTI-PARTY FORMS**

Per-sector and aggregate net ≤ 0 in V1–V3 at every registered scale
and evaluated point, R_net = 0 throughout; V4's artefact crossings
are exhibited below with their registered caveat. The QET line
therefore closes in BOTH forms (single-window, Phase 83;
multi-party, here), with the count stated in §4. Scope stated
exactly: compositions of the published two-qubit Hotta protocol
(arXiv:1002.0200) under the accounting inherited verbatim from
P72-2; a genuinely multipartite published Hamiltonian with
evaluable formulas would be a new item under the same reopening
bar, not a resurrection of these forms.

Reopening bar (inherited verbatim): any variant (V1–V3) with
R_net > 1 resource-counted. **Not met — the maximum R_net read in
V1–V3 is 0.0.**

All numbers below were recomputed from
`../../phase72/results/p722_results.json`'s stored point fields
(never quoted from prose), float64, per the definitions fixed in
`p1063_run_record.md` before any Phase-106 number was computed.

## 1. The single-copy accounting every variant inherits (h = 1, gap units)

| r = k/h | E_B | E_A | E_prep^(sep) | E_prep^(marg) | E_net,B = E_prep^(marg) − E_B | net delivered / sector = −E_net,B | R_net | price/unit (sep) | price/unit (marg) |
|---|---|---|---|---|---|---|---|---|---|
| 0.5 | 0.0725727759 | 0.8944271910 | 0.2360679775 | 0.4472135955 | 0.3746408196 | −0.3746408196 | 0 | 15.577400 | 18.486833 |
| 1.0 | 0.1147476339 | 0.7071067812 | 0.3284271247 | 1.4142135624 | 1.2994659284 | −1.2994659284 | 0 | 9.024447 | 18.486833 |
| 2.0 | 0.0981832661 | 0.4472135955 | 0.2221359550 | 3.5777087640 | 3.4795254979 | −3.4795254979 | 0 | 6.817349 | 40.993975 |

The stored `E_net_B_sector`, `total_per_EB` and
`total_per_EB_marg` fields of the Phase-72 JSON reproduce from
these raw fields at every point (checker-verified). The binding
term is the marginal-product correlation energy
E_prep^(marg) = 2k²/√(h²+k²): it exceeds the delivered E_B at
every evaluated point, by the smallest margin at r = 0.5
(net delivered −0.3746408196 per sector — the worst case, i.e.
the read closest to crossing, anywhere in V1–V3).

## 2. Per-variant deciding numbers

**V1 — Parallel parties** (M ∈ {1, 2, 4, 8, 16, 64, 1024}
independent pairs). Per-sector E_net,B and R_net are exactly the
§1 values at each point (R_net = 0 at all 21 reads). Aggregate net
delivered = M·(E_B − E_prep^(marg)) — strictly negative and
linear in M: the least negative aggregate anywhere is
−0.3746408196 (r = 0.5, M = 1) and the most negative is
−3563.0341098308 (r = 2, M = 1024). Total price per unit
delivered is M-invariant and equals the §1 single-copy prices at
both references (sep: 15.577400 / 9.024447 / 6.817349; marg:
18.486833 / 18.486833 / 40.993975 at r = 0.5 / 1 / 2). Distributing
copies in parallel scales the deficit; it does not dilute it,
because each copy carries its own per-sector resource.

**V2 — Star / fan-out** (one Alice, M pairs, same M set). Reads
identical to V1 in every deciding line: per-sector R_net = 0 at
all 21 reads, aggregate net = M·(E_B − E_prep^(marg)) ≤ 0, same
prices per unit at both references. Alice's aggregate injection
M·E_A is on the books (per point, E_A as in §1; e.g. at r = 1 it
runs from 0.7071067812 at M = 1 to 724.0773439350 at M = 1024).
No saving was granted: each pair is separately prepared and
separately measured — a shared single measurement across pairs
is not the published protocol and was not granted — so the star
topology changes who holds the pairs, not what each pair costs.

**V3 — Relay chains** (L ∈ {2, 4, 8} hops in series; only the
final sector receives). Final-sector E_net,B and R_net are the
§1 single-copy values (R_net = 0 at all 9 reads; final-sector net
delivered −0.3746408196 / −1.2994659284 / −3.4795254979 at
r = 0.5 / 1 / 2). With ALL upstream preparation + injection
counted, the total price per unit delivered at the final sector
is L× the single-copy price:

| r | L = 2 (sep / marg) | L = 4 (sep / marg) | L = 8 (sep / marg) |
|---|---|---|---|
| 0.5 | 31.1548 / 36.9737 | 62.3096 / 73.9473 | 124.6192 / 147.8947 |
| 1.0 | 18.0489 / 36.9737 | 36.0978 / 73.9473 | 72.1956 / 147.8947 |
| 2.0 | 13.6347 / 81.9880 | 27.2694 / 163.9759 | 54.5388 / 327.9518 |

Relaying makes the delivered unit more expensive, never cheaper:
upstream hops add positive cost and cannot subtract from the
final sector's reference energy.

## 3. V4 — Adversarial accounting bound (LABELLED ARTEFACT — not a protocol, not an R_net read)

Grant, most favourably to a loophole, that M receiving sectors
share ONE pair's preparation and ONE injection (cost paid once,
delivery M·E_B). The granted accounting crosses zero at:

| r | V4-total read — cost paid once = E_prep + E_A: crossing M (sep ref) | crossing M (marg ref) | V4-sector read — cost paid once = E_prep only: crossing M (sep ref) | crossing M (marg ref) |
|---|---|---|---|---|
| 0.5 | 16 | 19 | 4 | 7 |
| 1.0 | 10 | 19 | 3 | 13 |
| 2.0 | 7 | 41 | 3 | 37 |

**Registered caveat (binding wherever V4 is reported):** the
uncorrelated reference against which R_net is defined is PER
RECEIVING SECTOR — each sector's marginal-product correlation
energy is its own — so these crossings are artefacts of deleting
per-sector resources from the books, not R_net reads; **V4
cannot fire the reopening bar.** No R_net is assigned to V4. The
artefact's purpose is exactly this exhibition: any claimed
multi-party QET gain of this family would have to delete the
per-sector preparation of all but one receiving sector — a
bookkeeping deletion, not a protocol step — and the table prices
how large M would have to be for that deletion alone to fake a
positive net.

## 4. Closure count, anatomy, verification

- **Count read:** 3 protocol forms (V1, V2, V3) × scales
  (V1: 7 M values; V2: 7 M values; V3: 3 L values = 17
  form–scale combinations) × 3 evaluated points = **51 net
  reads** (V1: 21, V2: 21, V3: 9), plus 12 V4 bound reads
  (3 points × 2 references × 2 granted reads) exhibited as
  artefacts only. Net ≤ 0 and R_net = 0 at all 51 protocol reads.
- **Anatomy of the closure (structural, not a failed search):**
  the net is a per-sector identity, E_B − E_prep^(marg), that is
  negative at every evaluated point; every registered composition
  either multiplies it by a positive integer (V1, V2 — sign
  invariant under M), leaves the final sector's copy of it
  untouched while adding positive upstream cost (V3), or obtains
  a positive sign only by deleting the per-sector term from the
  books (V4, artefact). No composition of copies can change the
  sign of a quantity each copy carries separately. Reopening
  condition: a variant — of these forms or a genuinely
  multipartite published Hamiltonian with evaluable formulas —
  exhibiting R_net > 1 resource-counted under this same
  accounting.
- **Independent second path:** `../work/p1063_secondpath.py`,
  written from scratch (no eval-script functions; deciding lines
  recomputed directly from the Phase-72 JSON's raw point fields,
  V4 crossings found by direct search rather than the floor
  formula), agrees on every deciding line: worst per-sector net
  delivered −0.3746408196, worst R_net 0.0, all 12 V4 crossings
  identical.
- **Checker:** `../work/p1063_check.py` recomputes every number
  in `p1063_results.json` from the Phase-72 JSON + the registered
  definitions and cross-checks the second path:
  **726 PASS, 0 FAIL.**

## 5. Follow-ups (≥1, mechanism-suggested)

1. **FU-P1063-1 — genuinely multipartite Hamiltonian (new item,
   not a resurrection):** if a published multipartite QET model
   with evaluable formulas (a single shared resource state whose
   per-sector marginal-product reference is not simply M copies
   of the pair reference) is identified, pose it as a new item
   under this same accounting and the same reopening bar
   (R_net > 1 resource-counted). This is the only route the
   anatomy leaves open: the closure above is a statement about
   compositions of the pair protocol, whose per-sector resource
   is separable by construction.
2. **FU-P1063-2 — shared-measurement protocol, if published:**
   V2 granted no shared measurement because the published pair
   protocol has one measurement per pair. If a published
   fan-out variant with a single joint measurement exists, its
   injection/preparation bookkeeping can be read under the same
   definitions; until such a source is on the record, the
   variant is NOT POSED, not assumed.

## 6. C12 line

C12: an accounting verdict on a sourcing scheme; no throat, no
transport, nothing FTL is claimed by any outcome of this item.
Classical-leg energy ≥ 0 was omitted throughout, so every price
ratio stated is a lower bound. INTERNAL ONLY — nothing uploaded,
nobody contacted.
