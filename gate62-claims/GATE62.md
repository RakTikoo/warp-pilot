# GATE-62 REPORT — Phase 479's member at the wide pose
# (the DEC-constrained fit's Arm A / F0 object)

**Verdict: PASS WITH RIDER (G62-R1).** Phase 479's
member survives independent re-judgement in full:
the base reproduces at diff **0.0** on every
deciding field (§2); the member's DEFENDED triple
and six node values reproduce at diff **0.0**, with
the frame-invariance property confirmed on the
gate's own read (§3); the non-vacuity control
fires exactly as charged — 474's F1 object
reproduces at diff 0.0 and the constraint set
excludes it (§4); and the set residue, read
independently by the gate from the per-point
record, is **−6.459908493210403×10⁻⁶ at
r = 17.04878048780488, Type-I**, diff 0.0 against
the phase value (§5). The single rider (G62-R1,
§7) restates no value: it corrects the residue's
node **label** — in the gate's numbers, in the
same 0-based NODES indexing in which the basin
nodes are 8/9/10, that radius is node index **23**,
not the phase record's "node 25". The member
stands as a **DEFENDED member at the wide pose**,
quoted exactly as in §8 — never as a
four-condition pass.

Charge: ledger entry 1251. Claim under judgement:
ledger entry 1250 (Phase 479, CHECKPOINT479.md,
results/p479_memo.md). Ground records: entry 1240
(Phase 474), Phase 450's BOUGHT-MAXJOINT record as
carried in p460_lib §SS1.

**Wording discipline (in force on every number
below):** the member passes the wide-pose line's
DEFENDED bar (sampled joint ≥ 0 ∧ worst-null ≥ 0
∧ adversary Type-I NEC depth ≥ 0) with SEC cured
and DEC held at basin nodes 8/9/10, and carries a
set SEC residue. The programme's member bar — all
four conditions (NEC/WEC/DEC/SEC) at full audit
scope — is **not** met. No four-condition,
working-configuration, or drive language appears
in this report as a claim.

**The three goals:** (1) FTL drive — this gate's
home goal: GAP-3 at the wide pose now has a
gate-verified DEFENDED member with the basin
cured; the remaining distance to the programme's
member bar is exactly the outer SEC basin priced
in §5. (2) Functional wormhole — no contact.
(3) Subluminal record — no contact.

**DESK: NO DATA CONTACT.**

## 1. Machinery (the gate's own)

The gate's own driver (`work/g62_run.py`, under
registration `work/g62_registration.md`, filed
before any Gate-62 computation) drives the
lineage machinery — p479_lib → p474_lib →
p460_lib → p449_lib; SET-244 / SAMPLER-M,
eulerian_that association, float64, VM,
Phase-166 pin, programme venv — and computes the
§5 set read from the read's per-point record
(aux R: four channels + rho over 41 nodes × 162
directions, with Type-I flags) in its own code.
Three fresh evaluates (base, member, 474-F1)
plus worst-null and adversary instruments on the
base and the member. The gate's independent
checker (`work/g62_check.py`, stored records and
the gate's results file only, no machinery)
ran **21/21 PASS** and derives the verdict from
the numbers. All deciding reads are VM reads
(frame of record). The sampled SET reads
themselves are this claim's deciding reads in
the lineage's gate practice; they are reproduced
bit-exactly or the difference is stated — every
diff below is 0.0.

## 2. (a) The base — BOUGHT-MAXJOINT at diff 0.0

The base (x27 = 0; GN450 only) re-read on the
gate's path reproduces p460_lib's stored
deciding record (Phase 450's confirmation
record) at **diff 0.0 on all 17 DECIDING_FIELDS**:
nec_min / wec_min +4.224285347572982×10⁻⁹,
dec_min / joint +2.820462654076372×10⁻⁹,
sec_min −9.112743683512697×10⁻⁶, rho_min
+4.815542106782363×10⁻⁵, argmin radii, typeI
count/fraction, floors, pen
2.0000000000000004×10⁻⁷. Worst-null at the NEC
argmin **+1.149158092307544×10⁻⁹** (diff 0.0);
adversary Type-I NEC depth
**+2.333817817820605×10⁻¹³** (diff 0.0). Base
node values on the gate's read (nodes 8/9/10):
SEC −6.818999180673762×10⁻⁶ /
−9.112743683512697×10⁻⁶ /
−8.419173524140114×10⁻⁶; DEC
+4.891134573994601×10⁻⁵ /
+3.4415205649943894×10⁻⁵ /
+2.443058510603023×10⁻⁵ — 479's CTL-479-1
record, reproduced.

## 3. (b) The member — triple and six at diff 0.0,
## frame-invariance confirmed

The gate's member x (B window = W474B as
charged) **equals 479's stored member x
exactly**. On the gate's fresh read:

- **DEFENDED triple (all diff 0.0 vs 479's
  stored confirmation record):** joint
  **+2.820462654076372×10⁻⁹** (DEC-bound at
  r = 27.29268292682927, the base's own home);
  worst-null **+1.149158092307544×10⁻⁹**;
  adversary Type-I NEC depth
  **+2.333817817820605×10⁻¹³**. All three
  reproduce the bought base's values exactly —
  the joint was spent nowhere. DEFENDED: TRUE.
- **Six node values (all diff 0.0):** SEC
  +2.4404440032471187×10⁻⁵ /
  +2.4411976531644726×10⁻⁵ /
  +2.4396443055148438×10⁻⁵; DEC
  +4.894587722725915×10⁻⁵ /
  +3.441160723921305×10⁻⁵ /
  +2.4396443055148438×10⁻⁵ (nodes 8/9/10).
  Six-constraint deficit d6 =
  −2.4396443055148438×10⁻⁵.
- **Frame-invariance, confirmed on the gate's
  read:** at each of nodes 8/9/10, for both
  SEC and DEC, the sampled node minimum
  **equals** the Type-I-restricted node
  minimum — the deciding values sit at Type-I
  points and are frame-invariant statistics
  (C-10 discipline).
- pen **2.004145258222042×10⁻⁷** (diff 0.0).

## 4. (c) The non-vacuity control — fires as charged

474's F1 object (x from p474_fit.json,
rungs.F1.best.x) re-read through the widened
machinery on the gate's path: screen at
**diff 0.0 on all DECIDING_FIELDS** vs 474's
stored F1 confirmation screen; node SECs at
8/9/10 at diff 0.0 (+6.267279330478097×10⁻⁵ /
+2.674867695063221×10⁻⁵ /
+2.3917830480463622×10⁻⁵); node-10 DEC
**−5.375277493220288×10⁻⁴**, equal to the
object's screen dec_min, diff 0.0. The six
constraints evaluated on the gate's read of
that object: SEC8/9/10 all ≥ 0 (474's cure)
and DEC10 < 0 (indeed DEC8
−2.3511239265981872×10⁻⁴ and DEC9
−4.1363589306668655×10⁻⁴ are also negative) —
**the constraint set excludes the very object
474 produced**, demonstrated on the gate's own
read before the member's numbers were believed.

## 5. (d) The set residue — the gate's own
## SET-244 read of the member

Computed by the gate from the member read's
per-point record; cross-checked against the
same read's screen record at **diff 0.0 on all
five channels**. The claim's exact scope, in
the gate's numbers:

| channel | set min | node | r | argmin Type-I? | Type-I-restricted set min |
|---|---|---|---|---|---|
| NEC | +4.224285347572982×10⁻⁹ | 36 | 25.926829268292686 | yes | +4.224285347572982×10⁻⁹ @ 36 |
| WEC | +4.224285347572982×10⁻⁹ | 36 | 25.926829268292686 | yes | +4.224285347572982×10⁻⁹ @ 36 |
| DEC | +2.820462654076372×10⁻⁹ | 38 | 27.29268292682927 | **no** | +4.224285347572982×10⁻⁹ @ 36 |
| SEC | **−6.459908493210403×10⁻⁶** | **23** | **17.04878048780488** | yes | −6.459908493210403×10⁻⁶ @ 23 |
| RHO | +4.815542106782363×10⁻⁵ | 40 | 28.658536585365855 | yes | +4.815542106782363×10⁻⁵ @ 40 |

- The SEC residue equals the phase value at
  diff 0.0, at the phase radius, Type-I — and
  its Type-I-restricted set minimum is the
  same value at the same point: **the residue
  is a frame-invariant statistic**, not a
  frame-convention artefact.
- The residue is an outer basin on the
  gate's per-node SEC profile — six
  consecutive negative nodes, deepest at
  node 23: node 22
  −3.2120017402823117×10⁻⁶, node 23
  −6.459908493210403×10⁻⁶ (the argmin),
  node 24 −4.732424560343392×10⁻⁶, node 25
  −3.293564937848059×10⁻⁶, node 26
  −9.996766852402668×10⁻⁷, node 27
  −1.3276201480991287×10⁻⁷ (nodes 21 and 28
  are positive). Every other channel's set
  minimum is positive; the member's only
  failing condition at full SET-244 scope
  is SEC, on this basin.
- The DEC set minimum's argmin point is not
  Type-I (stated plainly, as a scope fact):
  the sampled joint — the DEFENDED statistic —
  is DEC-bound there; the Type-I-restricted
  DEC set minimum is +4.224285347572982×10⁻⁹.
  Both are positive; no DEFENDED clause is
  affected.

## 6. (e) The mechanism claim — consistent

On the stored records (479's fit and
confirmation files), verified by the gate:
Arm A and Arm B best x are **identical at
every rung** (F0/F1/F2), in both the fit
records and the confirmation records. The
LP-promise vs exact-read agreement, |lp_t −
exact_d6| per arm/rung round 1 (identical
across arms): F0 8.117984553012553×10⁻¹¹,
F1 **4.46882862712003×10⁻¹¹**, F2
4.448785615815561×10⁻¹¹; maximum
8.117984553012553×10⁻¹¹. The phase memo's
"~4.5×10⁻¹¹" was its F1 figure; it is
confirmed exactly at F1, and the gate fixes
the full table — the promises are the reads
at every rung, at the 10⁻¹¹ level, against
474's ~100× overstatement. The member's
largest step |dx| = 0.002009452499039281 ≤
0.00201, far inside both trust regions
(0.06 / 0.03), consistent with Arm B's
roughness price being inert and the two
arms landing on one vertex. The mechanism
claim — the wall was the constraint set,
not the class — is consistent with every
number the gate read.

## 7. Rider G62-R1 — the residue's node label

The phase record (entries 1240/1250; the
474 and 479 memos) names the set SEC argmin
"node 25 (r = 17.04878048780488)". In the
gate's own numbers, in the same 0-based
NODES indexing in which those same records'
basin nodes are 8/9/10 (NODES[8] =
6.8048780487804885, NODES[9] =
7.487804878048781, NODES[10] =
8.170731707317074 — all reproduced at diff
0.0 by this gate), r = 17.04878048780488 is
**node index 23**. NODES[25]
(r = 18.414634146341466) carries SEC
−3.293564937848059×10⁻⁶ on the member —
itself negative, inside the same outer
basin — so the correction is to the label
only, and no relabelling makes the locus
clean. The residue's value, radius, Type-I
status and frame-invariance are exact at
diff 0.0. Every quotation of the claim
carries the locus as: **node index 23,
r = 17.04878048780488** (479's follow-up
(iii) address and Phase 481's target are
this locus, by radius).

## 8. The quotable claim set (the only
## quotable form)

**G62-A (the member).** *The object 450's
BOUGHT-MAXJOINT + W474B =
[0, −0.0014031443466063713, 0, 0,
−0.0013795539861294259, 0, 0,
−0.002009452499039281, 0] (Phase 479, Arm A,
rung F0) is a DEFENDED member at the wide
pose: it passes the sampled joint
(+2.820462654076372×10⁻⁹), worst-null
(+1.149158092307544×10⁻⁹) and adversary
Type-I NEC depth (+2.333817817820605×10⁻¹³)
bars — all three reproducing the bought
base's values exactly — with SEC cured and
DEC held at basin nodes 8/9/10 (SEC
+2.440444/+2.441198/+2.439644 ×10⁻⁵; DEC
+4.894588/+3.441161/+2.439644 ×10⁻⁵;
sampled = Type-I-restricted, frame-invariant
statistics), AND it carries a set SEC
residue of −6.459908493210403×10⁻⁶ at node
index 23 (r = 17.04878048780488, Type-I,
frame-invariant; rider G62-R1). Gate-62
re-judged every figure at diff 0.0.*

**G62-B (the scope).** *At full SET-244
scope the member's only failing condition
is SEC, on an outer basin of six negative
nodes (22–27), deepest at node 23:
−6.459908493210403×10⁻⁶ (node 24
−4.732424560343392×10⁻⁶; node 25
−3.293564937848059×10⁻⁶); NEC, WEC, DEC and
RHO set minima are all positive (DEC set
min +2.820462654076372×10⁻⁹ at a non-Type-I
point, Type-I-restricted
+4.224285347572982×10⁻⁹). The programme's
member bar — all four conditions at full
audit scope — is not met; the distance is
exactly this basin.*

**G62-C (the mechanism).** *474's DEC bill
was the constraint set's blindness, not the
class's shape: with SEC and DEC carried as
node constraints, the basin cure costs DEC
~1.4×10⁻⁸ of slack (DEC10 +2.4431×10⁻⁵ →
+2.4396×10⁻⁵), the optimum is a
|dx| ≤ 0.00201 step found identically by
both registered arms, and the LP's promises
match the exact reads to ≤ 8.12×10⁻¹¹
(F1: 4.47×10⁻¹¹). The constraint set is
demonstrated non-vacuous: it excludes
474's F1 object (node-10 DEC
−5.375277493220288×10⁻⁴), reproduced by
Gate-62 at diff 0.0.*

**Fence (on every quotation):** G62-A/B/C
are quoted together; the residue travels
with the member wherever it is quoted; no
quotation calls the member a
four-condition pass, a working
configuration, or a drive.

## 9. Disclosures

No amendments to the gate registration; no
incidents. The gate driver was launched
detached after a harness output-drain note
on its first launch command (the process
ran to completion; no computation was
affected or repeated). Spend: 3 fresh
SET-244 evaluates + 2 worst-null/adversary
instrument sets, all VM, frame of record;
the checker is a separate stored-records
pass at 21/21. The gate disturbed no stored
read, appended no ledger entry, launched no
successor, and does not push: on this PASS
WITH RIDER the publication bundle is
assembled under `gate62/bundle/` and handed
back — the parent assigns the version at
push time by landing order and pushes.

DESK: NO DATA CONTACT.
