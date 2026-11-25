# CHECKPOINT 289 — THE DECISIVE READ IS TAKEN: §4b
# FAILS UNMOVED ON A BACKGROUND CONSISTENT BY
# CONSTRUCTION (median 0.169177 / max 808,773.48).
# THE BACKGROUND-BORNE EXPLANATION OF THE FIVE-ROW
# INVARIANCE DIES — THE CARRIER IS THE CONFIGURATION
# CLASS ITSELF. THE SIX-ROW TABLE IS CLOSED.

Phase 289 takes the §4b read (Gate-18 §4(b): rel_c
median AND max ≤ 0.02, Phase 164 point set) on the
Axis A member's march — the first §4b subject whose
background is TOV-consistent by construction (Phase
287: J derived through the identity, audit-clean at
all 181 θ). Registration `work/p289_registration.md`
(verdict forms + the materiality threshold fixed
before computation). Frame of record: Phase 166 pin,
Gate-19-corrected tensor, venv python, float64.
Independent checker 14/14 PASS. Protected engines
md5-identical throughout (p1692 1781b544…, p167
9db35c0b…, p1621 1f12ec29…). Driver walls: controls
52.1 s, deciding + sensitivity 79.3 s, checker 44.4 s.
Nothing outside `phase289/` written. No ledger
append, no launches, no contact.

## CONTROLS (all PASS, before the deciding read)

- C-S4B-J1: the verbatim p278 lib on the stored J1
  full state reproduces Phase 268's deciding read at
  diff **0.0** (median 0.16762395022464124, max
  715629.9865333225).
- C-S4B-M0: the member-parametrised lib at Δ = 0 with
  posed J reproduces that read at **per-point diff
  0.0** (1991 records). The lib differs from the
  verbatim p278 lib at exactly the two registered
  background-bearing sites: SITE A (A_vec's base —
  the Phase 287 family 𝒜(θ;Δ) = −0.3 + Δ·cos 2θ for
  the incumbent Auu ≡ −0.3) and SITE J (profiles_vec's
  jpose — J_bg for B.j_prof: posed J on the control
  arm, J_derived via PCHIP on the member arm).
- C-PROF-M: 𝒜(θ; +0.15) vs Phase 287's saved Auu_new
  at max diff 5.6×10⁻¹⁷; PCHIP reproduces J_derived
  at its nodes at 0.0; J_derived range
  [−0.889383, −0.530265].
- C-STATE-M / C-MD5: as registered.

## ITEM 1 — §4b FAILS UNMOVED
## (memo: results/p289_item1_memo.md)

Deciding read on `phase288/work/p288_member_state.npz`
(1991 points; hs = (0.025, 0.05, H_AUD)): **median
0.16917676136946494, max 808773.4788442705** (bar
0.02 / 0.02); 30/1991 points ≤ 0.02; no instant passes
(per-instant medians 0.127–0.200, U-shaped in t).
Companion (halved stencils): 0.1530062103196459 /
76.58760054403888. Interior: 0.1676070101062429 /
17.656918970165584; the headline max is the
pole-adjacent θ = 0.02 statistic, as in every row.

**THE SIX-ROW TABLE IS CLOSED** (bar 0.02 / 0.02):
prescribed J1 (throat) 0.167624 / 715,629.99 ·
att-solved (NOT a throat) 0.091008 / 714,294.11 ·
projected θ-flat (throat) 0.203356 / 658,563.27 ·
successor att₁ (throat) 0.196485 / 750,246.02 ·
projected successor (throat) 0.242321 / 633,905.82 ·
**Axis A member (throat, consistent background)
0.169177 / 808,773.48**. The member's median sits
inside the throat band, 0.93% above its lowest row.

**THE ANATOMY.** Every geometry-carried term group
fell under the background repair (member vs J1:
gamma_trace ×0.380, deriv_th ×0.750, gamma_second
×0.762, deriv_u ×0.779; the director group innocent,
0.000320, as in all six rows) — and the deciding
statistic did not follow: the groups' reductions do
not compose into the summed divergence's max-norm,
which re-forms at the table's level. The same
non-composition Phase 282 showed from the att side,
now confirmed from the background side.

**TWO FACTS OF RECORD.** (i) The member march's
MU/U/MTT are **bit-identical** to the J1 march's
(the evolution is deformation-blind; the background
change is confined to the read layer — Phase 288's
design): the last two rows are a pure background
swap on one evolved state, and zero of the 1991
rel_c values coincide between the reads. (ii) The
verdict is **interpolant-independent**: PCHIP /
natural cubic spline / piecewise-linear J give the
identical median at full precision and the same
verdict form (registration §5 diagnostic).

**VERDICT (registered §6, in order): §4b FAILS
UNMOVED.** The background-borne explanation of the
five-row invariance (Phase 285's candidate) DIES:
with the inconsistency removed — on the same evolved
state — the failure stands at full strength. The
priced residue: the inconsistent background carried
term-level residue (gamma_trace above all) but was
not the failure's carrier. **The carrier is the
configuration class itself** — §4b's failure is now
invariant under pose, evolution law, att shape,
projection, and background consistency.

## STANDING AFTER PHASE 289

Stage D form 2 stands for the Axis A family as for
the incumbent and successor families. The Phase 283
redesign programme has spent all three axes: B dead
at counting cost (Phase 284), C dead at audit cost
(Phase 285), A run its full course — it produced the
class's best pose (audit-clean background, +24.7%
t = 0 binding margin, bracket (0.575, 0.58125]) and
did not move §4b. The member's gains stand at read
grade, untouched by this verdict. Remaining, in
order: (1) Gate-23-pattern certification of the
member's bracket — completeness, insufficient alone
while §4b fails for every subject in the class;
(2) p1592 — unchanged, gates programme-level
sustainment wording; (3) Gap 1's extension (Phase
260) — the outer debt, its deficit standing at one
scalar constitutive relation per radial order.
Any further §4b progress requires leaving this
configuration class, not another variation within
it.

## FILES

- `work/p289_registration.md` — registration
  (pre-computation; verdict forms + threshold).
- `work/p289_s4b_lib_member.py` — the
  member-parametrised §4b lib (two registered sites
  vs the verbatim p278 lib).
- `work/p289_run1.py` (controls) / `work/
  p289_run2.py` (deciding read + sensitivity) —
  drivers; `work/p289_check.py` (14/14 PASS) —
  independent checker; `work/
  p289_controls_arrays.npz`,
  `work/p289_item1_records.json`, driver logs.
- `results/p289_controls.json`,
  `results/p289_item1.json`,
  `results/p289_verify.json`,
  `results/p289_item1_memo.md` (Item 1). This
  checkpoint. No ledger append, no launch, nothing
  outside `phase289/` written.

## FENCES

Read grade only; the read judged only (no tuning of
the member, background, march, interpolants, point
set, or stencils against the read; the sensitivity
arms are diagnostics, not verdict inputs); no
certification claimed and the member's
Gate-23-pattern debt rides in full; the director's
south-pole defect domain fence rides every inherited
τ statement; no traversability, construction, or
programme-level wording.
