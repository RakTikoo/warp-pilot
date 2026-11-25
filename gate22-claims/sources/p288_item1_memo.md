# P288 ITEM 1 MEMO — THE AXIS A MEMBER'S BRACKET

**Phase 288, Item 1.** Registration
`phase288/work/p288_registration.md` (binding, written
before any deciding computation). Frame of record: Phase
166 pin, Gate-19-corrected tensor, float64. **Verdict:
BRACKET AT (0.575, 0.58125]**, carriers NEC_φ = DEC_φ —
longer than J1's (0.55, 0.55625] and the θ-flat repair's
(0.53125, 0.5375], shorter than the successor's
(0.71875, 0.725]. Independent checker 11/11 PASS
(recomputed from the on-disk checkpoint at diff 0.0).

## 1. The adaptation (registration §1)

One march, two read layers. The evolution is the J1
construction verbatim (G4: N_θ = 11521, h_t = 0.000625,
T_END = 1.0, RK4 through the true lock, seed μ ≡ +0.25
flat, no projection, incumbent att at every att-bearing
site); it takes no Auu/Fuu input, so the Axis A
background change lives entirely in the read layer, in
exactly the two slots Phase 287 replaced in the datum
jets, transported to the march slice's corresponding
slots: **Auu := 𝒜(θ)** (the saved `Auu_new` profile) and
**jpose's static content := J_derived(θ)** (the saved
profile in `B.j_prof`'s place inside
Fuu = exp(2μ)·(jprof + exp(−2Φ₀)·Mtt)). Both profiles
were loaded once from
`phase287/work/p287_built_profiles_amended.npz`
(md5 39cc4c57…) and frozen — never re-derived, never
adjusted. The march's FULL state is checkpointed at
`phase288/work/p288_member_state.npz` (MU/U/MTT at all
1601 steps; §5 of the registration).

## 2. Controls (all PASS, before the member was read)

- **C-PROF**: `Auu_new` equals the family formula
  0.2 + (−0.5 + 0.15·cos(2θ)) at diff **0.0**; `Auu_inc`
  ≡ −0.3 at deviation 0.0; J_derived finite on all 181
  points, range [−0.889383, −0.530265].
- **C-LIB**: the adapted jets at the posed corner vs
  `E.comp_jets` jet-for-jet at diff **0.0**; the adapted
  read arm at the control corner vs p281's `read_arm_k`
  (k=2) clause minima at all 41 sampled instants at diff
  **0.0**.
- **C-J1 (the control)**: the adapted machinery at the
  control corner (𝒜 ≡ −0.3, POSED J) reproduces the
  incumbent J1 bracket **(0.55, 0.55625]** with carriers
  exactly {NEC_φ, DEC_φ}, and the march state's MU[::40]
  equals Phase 269's stored J1 checkpoint at diff
  **0.0** (U and MTT likewise). The background change is
  provably the only change: the adaptation smuggled
  nothing in. (The tasking's blocker form did not arise:
  the Δ = 0 control posed in the adapted machinery
  without obstruction.)
- **C-TAU / C-Q**: see the Item 2 memo.

## 3. The bracket

Member sampled rows (march slice; NEC_φ is the binding
clause throughout the approach):

| t | NEC_ρ | NEC_φ (member) | NEC_φ (J1, same instants) |
|---|---|---|---|
| 0.000 | +1.613597 | **+1.644910** | +1.384159 |
| 0.500 | +0.948611 | +0.675101 | +0.423166 |
| 0.550 | +0.769052 | +0.297803 | +0.047417 |
| 0.575 | +0.669257 | +0.061311 | — (failed) |
| 0.600 | +0.562237 | **−0.213688** | — |

First failing sampled instant t = 0.600; refinement
(+10/+20/+30): NEC_φ = −0.003551 at 0.58125, −0.070924
at 0.5875, −0.140928 at 0.59375. **Refined bracket
(0.575, 0.58125], carriers NEC_φ = DEC_φ** (both clauses
narrow to the same bracket).

**The build's bracket table (march slice, read grade):**

| pose | bracket | right edge vs member |
|---|---|---|
| θ-flat repair (P269) | (0.53125, 0.5375] | member +0.04375 |
| J1 incumbent (P264) | (0.55, 0.55625] | member +0.025 |
| **Axis A member (P288)** | **(0.575, 0.58125]** | — |
| successor att₁ (P281) | (0.71875, 0.725] | member −0.14375 |

The member sustains LONGER than both incumbent-geometry
arms and SHORTER than the att₁ successor. The lengthening
over J1 is broad, not a near-miss at the crossing: at
t = 0.55 the member's binding margin is +0.297803 against
J1's +0.047417 (6.3×), and at t = 0.5, +0.675101 against
+0.423166. NEC_ρ also decays slightly more slowly than
J1's (+0.948611 vs +0.942761 at t = 0.5; +0.769052 vs
+0.763561 at 0.55). No other clause binds first.

## 4. Attribution — the t = 0 swap diagnostics

March-slice t = 0 rows (diagnostics, not gates; Phase
287 §3(b) pattern). NEC_φ column is the binding story:

| read | NEC_ρ | NEC_θ | NEC_φ | WEC |
|---|---|---|---|---|
| neither (control) | +1.386148 | +1.540024 | +1.384159 | +2.017421 |
| 𝒜 only | +1.613597 | +1.426391 | +1.426287 | +1.790154 |
| J only | +1.386148 | +1.831647 | +1.557146 | +2.017421 |
| both (member) | +1.613597 | +1.724058 | **+1.644910** | +1.790154 |

On the binding clause: the deformation profile alone
carries **+0.042128**, the J-derivation alone
**+0.172987**, and jointly **+0.260751** — the
J-derivation is the larger single contributor in the
march slice too (as at datum scope in Phase 287, where
it carried +0.093889 of +0.201258), and the joint gain
exceeds the sum of the separate gains by +0.045636 (the
two replacements cooperate on NEC_φ). On NEC_θ the two
pull opposite ways (𝒜 −0.113633, J +0.291623). NEC_ρ and
WEC are J-insensitive at their argmins (the 𝒜-only row
reproduces the member's exactly, and both reproduce
Phase 287's datum-slice values +1.613597 / +1.790154 —
the two slices agree on those clauses at t = 0).

Slice fence, as registered: the member's march t = 0
NEC_φ (+1.644910) is a march-slice number and is NOT
Phase 287's datum-slice +1.015422; no join is asserted.
What transfers across slices is the ordering: at both
scopes the member's binding margin exceeds the
incumbent's, and at both scopes the J-derivation carries
the larger share of the gain.

## 5. Verdict

**BRACKET AT (0.575, 0.58125]**, carriers NEC_φ =
DEC_φ. The Axis A member — the first throat pose on a
background built through the TOV identity — sustains
under the coupled evolution for longer than the
incumbent pose on the incumbent (audit-failed)
background, at read grade. POSE FAILS EARLY does not
fire (the t = 0 row is all-positive with the widest
binding margin of any incumbent-att arm); the derived-J
background's evolution is not implicated in any failure
— the evolution is background-blind by construction, and
the crossing, when it comes, arrives through the same
NEC_φ decay channel as every arm of this build, only
later. What this bracket does NOT yet decide: §4b on
this background (Phase 289's read on this phase's
checkpoint) — the decisive test of whether the five-row
§4b invariance was background-borne. Re-certification
debt (Gate-23 pattern) rides this bracket in full.

Fences: read grade only; no certification claimed; the
director's south-pole defect domain fence rides every
statement; p1592 still gates programme-level wording.
