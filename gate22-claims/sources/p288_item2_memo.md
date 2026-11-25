# P288 ITEM 2 MEMO — THE DIRECTOR ALONG THE MEMBER'S MARCH

**Phase 288, Item 2.** Registration
`phase288/work/p288_registration.md` §2 (C-Q) and §4.
**Verdict: DRIFT** — onset t = 0.050, growth IDENTICAL to
the incumbent J1's at every measured instant (window
maxima 0.027612 / 0.042164 / 1.245852 at t = 0.5 / 0.55 /
1.0), and the identity is not an assumption: the
closed form's applicability on the new background was
CHECKED by re-derivation with Q a function of θ, and the
throat tension provably does not contain Q or Q′ at all.
The member therefore inherits the incumbent's director
caveat in full — NOT the successor's halved rate (that
halving was att₁'s work; the member carries the
incumbent att, per the registration).

## 1. C-Q — the applicability check (the phase's new content)

Phase 281's derivation input list was [θ, φ, A0pp, A0p,
A0, Mp, M]: Q (= Auu) did not survive throat extraction
for constant Q. Whether that survives 𝒜(θ) — a genuine
θ-dependent deformation — was checked, not assumed:
the SymPy Bochner derivation was re-run with
A = A0(θ) + (ρ²/2)·Q(θ), Q a SymPy function of θ, all
else identical.

**Member derivation input list: [A0pp, A0p, A0, Mp, M] —
identical to the constant-Q list.** Neither Q nor Q′
appears in any throat-extracted τ component. The slice
tension at the throat is blind to the areal-radius
profile's ρ² coefficient whether or not that coefficient
varies with θ. Consequences, all verified numerically:

- The member evaluator (lambdified member derivation,
  evaluated at Q := 𝒜(θ), Q′ := −0.3·sin(2θ)) equals the
  constant-Q evaluator at diff **0.0** at every spot
  (t = 0.25 / 0.5 / 0.75 / 1.0) — the identity check the
  registration required.
- The closed form
  |τ| = |sinφ·cosφ|·M′(θ,t)²/A0(θ,t)² therefore
  CARRIES to the new background, and the reason is now
  derivation-level, not empirical: τ contains no Auu
  jet, and A0(θ,t) = R00 + (t²/2)·att(θ) involves the
  evolution, not the background's 𝒜.
- Evaluator vs closed form at the spots: max window
  difference ≤ **1.03×10⁻¹⁴** (FD class) — the closed
  form exhausts τ on this background.

## 2. The drift read

Closed-form series on the marched states (41 sampled
instants; window θ ∈ [0.3, 2.6], φ ∈ {0, π/6, π/3,
π/2}, bar_τ = 10⁻⁶), corroborated by the member
evaluator at the four spots (evaluator window maxima
identical to the closed form's to the digits shown):

| t | window max \|τ\| | vs J1 | vs successor |
|---|---|---|---|
| 0.050 | 2.33×10⁻⁶ (onset) | same onset | same onset |
| 0.25 | 1.510×10⁻³ | = J1 | — |
| 0.50 | **0.027612** | = J1 (0.027612) | succ 0.015987 |
| 0.55 | **0.042164** | = J1 (0.042164) | succ 0.024292 |
| 0.75 | 0.188540 | = J1 | — |
| 1.00 | **1.245852** | = J1 (1.245852) | succ 0.643088 |

ON-SHELL THROUGHOUT does not fire (the window maximum
exceeds the 10⁻⁶ bar from t = 0.050 on). Mechanism
diagnostics (fine grid): max|M′| = 0.0019 at onset era,
0.1853 at t = 0.5, 0.8005 at t = 1.0; μ's θ-spread grows
0 → 0.1427 (t = 0.5) → 0.6212 (t = 1.0) — the same
developed θ-structure as J1's march (identical state:
MU[::40] diff 0.0 against Phase 269's stored J1).

## 3. Mechanism

Per the registered rule: evaluator/closed-form agreement
(≤ 10⁻⁴, here ≤ 10⁻¹⁴) at every spot ⇒ **τ is exhausted
by the ∂_θμ channel** — the single closed-form mechanism
of Phases 268/281 (|τ| = |sinφ·cosφ|·M′²/A0², sole
driver ∂_θμ via Γ^ρ_ρθ = M′). No second channel exists
on the new background; in particular the derived-J /
𝒜(θ) background contributes NOTHING to the director's
off-shell drift — it cannot, by the C-Q derivation: the
throat tension never sees the profile that changed. The
director's drift on the Axis A member is the incumbent
pose's drift, carried by the incumbent evolution, at the
incumbent rate. The Axis A redesign repaired the
background's audit inconsistency and lengthened the
bracket (Item 1); it does not touch the director's
on-shellness, and nothing in this phase's machinery
could have — the two defects live in different slots of
the construction (background jets vs the evolved μ
field's θ-structure).

## 4. Verdict

**DRIFT** — onset t = 0.050; window maxima 0.027612 /
0.042164 / 1.245852 at t = 0.5 / 0.55 / 1.0, identical
to J1's and roughly twice the successor's at every
compared instant; mechanism the ∂_θμ channel alone,
with the closed form's applicability on the new
background PROVEN by the Q(θ) re-derivation (input list
identical; member evaluator = constant-Q evaluator at
diff 0.0; evaluator vs closed form ≤ 1.03×10⁻¹⁴). The
member's director standing is exactly the incumbent's:
off-shell from t = 0.050 under this evolution, a standing
caveat on the bracket of Item 1 — the pose sustains
longer on a consistent background, and its director
still drifts at the old rate. (As in Phases 281/282, the
projection that would kill the drift exactly is a
different arm with its own bracket price; it was not
run here — the registration's primary arm is the posed
flat seed, no projection.)
