# P287 ITEM 2 MEMO — THE POSE TEST

**Phase 287, Item 2** (Axis A of the Phase 283 geometry-level
redesign spec). Registration `phase287/work/p287_registration.md`
§5 (+ Amendment A1, which governs only the Item 1 build solver).
The member (Δ = +0.15) was audit-clean under the guarded gate
(Item 1 memo), so the Phase 280-pattern t = 0 pose test ran
under full joint accounting. **Verdict: POSE HOLDS AT t = 0 —
the Axis A kill does not fire.** No §4b value was computed or
used anywhere in this phase.

## 1. The row

Joint accounting (director T2 channels + flat δμ = +0.25 +
incumbent ũ/att + member 𝒜(θ) + derived J_derived), all seven
clause minima over the 181-point θ grid:

| clause | member | argmin θ | incumbent (P264) | departure |
|---|---|---|---|---|
| NEC_ρ | **+1.613597** | 1.570796 (θ*) | +1.386148 | +0.227449 |
| NEC_θ | **+1.562131** | 1.553565 | +1.355900 | +0.206231 |
| NEC_φ | **+1.015422** | 1.398486 | **+0.814164** | **+0.201258** |
| WEC | **+1.790154** | 0.020000 | +2.017421 | −0.227267 |
| DEC_ρ | **+1.478577** | 0.020000 | +1.386148 | +0.092429 |
| DEC_θ | **+1.506306** | 0.020000 | +1.355900 | +0.150406 |
| DEC_φ | **+1.015422** | 1.398486 | +0.814164 | +0.201258 |

**Binding clause: NEC_φ = +1.0154216858733955** — 24.7% ABOVE
the incumbent's binding margin (+0.814164). Every clause is
positive; the pose does not merely hold, it holds with a wider
binding margin than the incumbent pose on the incumbent
background. The one falling clause is WEC (−0.227267, its
argmin moved to the pole θ = 0.02), still at +1.79.

## 2. On-shell groups (all in their registered forms)

- **G1 τ(n) ≡ 0**: symbolic exactly 0.0 (p264b's evaluator
  verbatim); FD interior median 0.006502, at θ* 0.004578,
  interior max 0.052419 — the same numerical class as Phase
  264's own read (0.006566 / 0.004718 / 0.051513). The
  director's south-pole defect fence rides this statement, as
  registered.
- **G2 δμ/lock compatibility**: analytic residual **exactly
  0.0** (the flat field, unchanged); fd4-form compatibilities
  0.0.
- **G3 momentum maxima**: **exactly 0.0** from the pose's own
  channels (bar 0.02) — the pose starts on-shell in the
  momentum constraints as posed, as the incumbent did.

## 3. Attribution (diagnostics, not gates)

**J-attribution swap** (member background, POSED j_prof in
place of J_derived): NEC_φ = +0.921533, NEC_θ = +1.469625,
DEC_φ = +0.921533; NEC_ρ, WEC, DEC_ρ minima **identical** to
the built row. So of the binding clause's +0.201258 gain,
**+0.107369 is carried by the deformation profile alone** (the
fixed-mean redistribution, read at the posed J) and a further
**+0.093889 by the J-derivation** (building the background
through the identity is worth margin in its own right, on top
of making the background consistent). The ρρ/WEC minima are
J-insensitive at their argmins.

**Factorial cross-term**: the R×Φ cross-term on NEC_ρ and WEC
equals the registered closed-form prediction
cross_pred(θ) = (𝒜(θ) − 0.2)·(−2/A)·(e^{−2M} − 1) **exactly**
(driver deviation 0.0; independent checker 6.7×10⁻¹⁶) — Phase
262's linearity in Auu survives both the θ-dependent profile
and J_derived carried in both pieces. On NEC_θ/NEC_φ the
registered "half of cross_pred" heuristic deviates (max
0.213897, median −0.097995): the half was a stated guess, not a
derived form, and the tangential cross-term's true profile
(range [−0.3876, −0.2893]) is now on record for any successor
registration. All director pairings (D×R, D×Φ, triple) are
pointwise-linear to ≤ 1.9×10⁻¹² on the headline clauses.

## 4. Verdict and consequence

**POSE HOLDS AT t = 0.** Per the registration, the member
**earns a march registration**: the Axis A member — a throat
pose on a background built through the TOV identity, audit-
clean at every θ, holding at t = 0 with binding margin
+1.015422 — is the first redesign-axis product to survive its
kill. Its march's §4b read becomes the **decisive test of the
background-inconsistency explanation of the §4b line's
invariance** (Phase 285's candidate contributor: every §4b
subject to date stood on a background proven O(1)
TOV-inconsistent; this one does not). No march is launched by
this phase (registration discipline: launches are the parent's;
§4b was not computed here in any form).

What this does NOT do: it does not reopen Axis B (the
extension count stands as Phase 284 counted it — the deficit
is one scalar relation per radial order, and this phase
consumed exactly the throat-order instance of that pattern for
the background, not the extension); it does not certify a
sustainment bracket for the new member (that is the march's
own read); it does not touch p1592 or any programme-level
sustainment wording; Gate-23's verdicts stand for their own
pose. The incumbent record (Phases 264–285) is untouched.

Independent checker: `phase287/results/p287_verify.json` —
ALL PASS (incumbent row at ≤ 5×10⁻⁷, gate re-run identical,
pose row at diff 0.0, G2 analytic zero, G3 = 0.0, factorial
identity 6.7×10⁻¹⁶, swap row at diff 0.0, md5s identical).
