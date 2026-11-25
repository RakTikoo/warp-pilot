# CHECKPOINT 288 — THE AXIS A MEMBER'S MARCH: BRACKET (0.575, 0.58125] (LONGER THAN J1, SHORTER THAN THE SUCCESSOR); DIRECTOR DRIFT IDENTICAL TO J1's, WITH THE CLOSED FORM'S APPLICABILITY ON THE NEW BACKGROUND PROVEN BY RE-DERIVATION (Q(θ) NEVER ENTERS THE THROAT TENSION)

**FULL-STATE CHECKPOINT (Phase 278 rule):**
`phase288/work/p288_member_state.npz` — MU, U, MTT at
ALL 1601 steps (no subsampling) + times + th_f, written
by the driver before any read; Phase 289's §4b read runs
on this file. (442,789,092 bytes.)

Frame: Phase 166 pin; Gate-19-corrected tensor; float64;
protected engines byte-identical (p1692 1781b544…,
p167 9db35c0b…, p1621 1f12ec29…). Registration
`phase288/work/p288_registration.md` (binding, before
any deciding computation; §1 the subject and the
one-march-two-read-layers adaptation, §2 controls C-PROF
/ C-LIB / C-J1 / C-TAU / C-Q, §3–§4 verdict forms, §5
checkpoint, §6 fences). Machinery:
`phase288/work/p288_lib.py` (the adapted read layer —
`comp_jets_A` / `read_arm_A` / `bracket_scan_A` — plus
p281_lib's incumbent march and τ helpers, imported, not
copied), driver `phase288/work/p288_run.py`, checker
`phase288/work/p288_check.py`. Total wall 71.8 s.

**ITEM 1 — BRACKET AT (0.575, 0.58125], carriers
NEC_φ = DEC_φ.** The member (𝒜(θ) = 0.2 + (−0.5 +
0.15·cos 2θ); J DERIVED through the TOV identity,
audit-clean per Phase 287) was marched under the coupled
evolution — the J1 construction verbatim (G4, seed
μ ≡ +0.25 flat as posed, no projection, incumbent att),
the background change confined to the read layer (Auu
slot := 𝒜(θ); jpose's static content := J_derived(θ);
profiles loaded once from
`phase287/work/p287_built_profiles_amended.npz` and
frozen). First failing sampled instant t = 0.600
(NEC_φ −0.213688); refinement NEC_φ = +0.061311 at
0.575, −0.003551 at 0.58125. **The build's bracket
table:** θ-flat repair (0.53125, 0.5375] · J1
(0.55, 0.55625] · **Axis A member (0.575, 0.58125]** ·
successor att₁ (0.71875, 0.725]. The lengthening over
J1 is broad (binding margin at t = 0.55: +0.297803 vs
J1's +0.047417; at t = 0.5: +0.675101 vs +0.423166).
t = 0 swaps (march slice, diagnostics): NEC_φ neither
+1.384159, 𝒜-only +1.426287 (+0.042128), J-only
+1.557146 (+0.172987), both +1.644910 (+0.260751; the
two replacements cooperate, +0.045636 beyond the sum).
POSE FAILS EARLY does not fire. Memo:
`phase288/results/p288_item1_memo.md`.

**ITEM 2 — DRIFT, IDENTICAL TO J1's; APPLICABILITY
PROVEN, NOT ASSUMED.** The C-Q check re-ran the SymPy
Bochner derivation with Q a FUNCTION of θ:
**the member derivation's input list is [A0pp, A0p, A0,
Mp, M] — identical to the constant-Q list; neither Q
nor Q′ survives throat extraction.** The throat tension
is blind to the areal-radius profile's ρ² coefficient,
θ-dependent or not. The member evaluator (at 𝒜(θ),
𝒜′(θ) = −0.3·sin 2θ) equals the constant-Q evaluator at
diff 0.0 at all four spots (t = 0.25/0.5/0.75/1.0) and
agrees with the closed form to ≤ 1.03×10⁻¹⁴. The closed
form |τ| = |sinφ·cosφ|·M′²/A0² therefore carries to the
new background by derivation, and the drift read on it
is J1's own: onset t = 0.050; window maxima 0.027612 /
0.042164 / 1.245852 at t = 0.5 / 0.55 / 1.0 (successor's:
0.015987 / 0.024292 / 0.643088 — the member does NOT
inherit the halving; that was att₁'s). Mechanism: the
∂_θμ channel alone (registered agreement rule fired at
10⁻¹⁴ class); the derived-J/𝒜 background contributes
nothing to τ — it cannot, per C-Q. The member's director
caveat is the incumbent's, in full. Memo:
`phase288/results/p288_item2_memo.md`.

**CONTROLS — ALL PASS, BEFORE THE MEMBER WAS READ.**
C-PROF: `Auu_new` = the family formula at diff 0.0,
`Auu_inc` ≡ −0.3 at 0.0, J_derived finite on all 181
points (npz md5 39cc4c57…). C-LIB: adapted jets at the
posed corner vs `E.comp_jets` at 0.0; adapted read arm
at the control corner vs p281's `read_arm_k` (k=2) at
all 41 instants at 0.0. **C-J1 (the control): the
adapted machinery at Δ = 0 (𝒜 ≡ −0.3, POSED J)
reproduces J1's bracket (0.55, 0.55625] with carriers
exactly {NEC_φ, DEC_φ}, and MU/U/MTT [::40] equal Phase
269's stored J1 state at diff 0.0** — the background
change is provably the only change (the tasking's
blocker form did not arise). C-TAU: closed-form onset
0.050 exactly; targets 2.76e-2/4.22e-2/1.246 matched to
rel errs ≤ 8.5×10⁻⁴; constant-Q evaluator spot at
t = 0.5 vs closed form 9.27×10⁻¹⁵. C-MD5 identical.
**Independent checker: 11/11 PASS** (checkpoint
keys/shapes; MU[::40] vs p2691 at 0.0; control and
member brackets, all 41+3 rows, the t = 0 swaps, and the
τ window maxima recomputed FROM THE ON-DISK CHECKPOINT
at diff 0.0; protected md5s identical) —
`phase288/results/p288_verify.json`.

**WHAT THIS PHASE ESTABLISHES.** (i) The first throat
pose on a background built through the TOV identity
sustains under the coupled evolution LONGER than the
incumbent pose on the audit-failed background — the
Axis A redesign's t = 0 gain (+24.7% binding at datum
scope) survives the march and converts into bracket
length (+0.025 of right edge over J1), with the
J-derivation the larger single contributor at both
scopes. (ii) The director's drift is provably
background-independent in the Auu slot: the Q(θ)
re-derivation closes the applicability question Phase
281's constant-Q derivation left open — τ at the throat
contains no areal-profile jet, so no background repair
of this family can move the director's on-shellness;
the drift is the evolution's μ-field θ-structure, full
stop. (iii) The §4b question is now cleanly posed: this
phase's checkpoint holds a march whose background is
audit-clean, so Phase 289's §4b read on it is the
decisive test of whether the five-row §4b invariance
(Phases 268–283) was background-borne (Phase 285's
candidate contributor) or lives in the evolved geometry
itself.

**FENCES.** Read grade only — no certification claimed;
the member's own Gate-23-pattern re-certification debt
rides this bracket in full (the successor's bracket is
likewise read-grade). §4b NOT computed here (Phase 289,
on this checkpoint). The director's south-pole defect
domain fence rides every director statement. The march
was not tuned against any judging read; the member's
profiles were inputs, never re-derived. Slice fence:
march-slice and datum-slice numbers are never joined
(Phase 287's +1.015422 is the datum-slice binding
margin; this phase's t = 0 march row reads NEC_φ
+1.644910 — orderings and attributions transfer, values
do not). p1592 still gates programme-level sustainment
wording. INTERNAL only.
