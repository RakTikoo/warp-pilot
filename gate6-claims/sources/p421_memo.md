# P42-1 — Φ ≠ 0 FLUX-FIRST THROAT ALGEBRA: memo

**Verdict: INERTNESS SURVIVES Φ ≠ 0** — p_r,dem(r₀) = −F₀/(8πr₀²) still carries
no F′₀ and no F″₀ for every Φ′₀ in both registered families. The protection that
survives is named exactly in §2: every Φ′-coupled term in the demanded channels
is multiplied by the throat factor A = 1 − b/r itself, and the one AΦ′F′ term
that reaches □F is cancelled identically by ∇^t∇_tF. Scope: Morris–Thorne
throats with Φ(r₀) = 0 and finite Φ′₀, Φ″₀ — both registered families, and by
the A-factor structure any Φ with those throat data. No row passes the
configuration test (0/192 primary, 0/32 controls), so nothing here is even a
scan signal; there is no survivor and no second-path question on any row.
C12 accounting in §5.

## 1. Throat algebra (from the action; two derivations agree symbolically)

Full record in `p421_run_record.md`. Headline formulas (r₀ general, β := b′(r₀)):

- ρ_dem(r₀) = F₀β/(8πr₀²) − (1−β)F′₀/(16πr₀) — canonical Φ = 0 pair, unchanged.
- p_r,dem(r₀) = −F₀/(8πr₀²) — canonical, unchanged.
- General r: 8πp_r,dem = −Fb/r³ + A[F′Φ′ + 2FΦ′/r + 2F′/r];
  8πρ_dem = Fb′/r² − AF″ − 2AF′/r − A′F′/2.
- Φ ≠ 0 throat scalar EoM: (1−β)φ′₀/(2r₀) + F_φ0[2β − (1−β)Φ′₀r₀]/(16πr₀²) − V′₀ = 0.
  φ″₀ is not fixed by it (its coefficient is A), so F″₀ admits no throat EoM
  reduction — and needs none, since F″₀ enters neither demanded channel.

Gates: shared GR gate exact (−1/(8π), −1/(4π)); a = 0 control reproduces the
canonical pair exactly on both shapes; five P13-3 sign checks (S1–S5) pass at
named sample points before the scan was read.

## 2. PROTECTION LEDGER (the headline; registered expectations tested)

- **(i) 2(1−b/r)F′/r still vanishes at r₀ — SURVIVES.** Its factor is A, a
  b-only quantity; Φ does not touch it. At general r it is the last term of the
  p_r flux bracket A[F′Φ′ + 2FΦ′/r + 2F′/r].
- **(ii) Φ′₀-coupled terms enter p_r,dem unsuppressed — REFUTED.** The candidate
  structures exist at general r but every one carries A: Φ′F′ enters as
  AΦ′F′ (from □F − ∇^r∇_rF), and Φ′F enters as 2AFΦ′/r (the Φ′ piece of G^r_r
  is likewise 2AΦ′/r). In ρ_dem the candidate AΦ′F′ in □F is cancelled
  identically by ∇^t∇_tF = AΦ′F′. No Φ′₀-coupled term reaches either demanded
  channel at r₀, suppressed or otherwise — the (1−b/r) protection does not
  break; it extends over the new terms, because each new term is built from
  the same radial-derivative structure that A multiplies.
- **(iii) F″₀ re-enters a channel — REFUTED.** F″₀'s coefficients are A in
  ρ_dem (via □F) and identically cancelling in p_r,dem (□F vs ∇^r∇_rF, at
  general r, for any Φ). F″₀ enters neither channel, exactly as at Φ = 0.
- **(iv) Supply cone unchanged — SURVIVES exactly.** The scalar kinetic term is
  g^rr(φ′)² = A(φ′)²; Φ never enters it. A(r₀) = 0 still gives ρ_φ(r₀) = V₀,
  p_r,φ(r₀) = −V₀; the primary anti-diagonal ray and the dust wedge
  (ρ + p_r ≥ 0, p_r ≤ 0) are unchanged in shape.

**What Φ′ actually moves** (the precise boundary of the protection): the scalar
EoM, through R(r₀) = 2β/r₀² − (1−β)Φ′₀/r₀ — the −A′Φ′ cross term in R, the sole
Φ′ survivor at the throat (Φ″₀ and Φ′₀² enter R only A-multiplied and cancel
at r₀; Φ″₀ enters no throat quantity at all, which is why the two registered
families, differing only in Φ″₀ and in Φ(∞), are throat-identical). Φ′ also
moves G^θ_θ(r₀) = (1−β)(1 + Φ′₀r₀)/(2r₀²), which no registered channel reads.
So the Phase-40 premise — "with Φ′(r₀) ≠ 0 the (1−b/r) protection is claimed
to break" — is **false for the demanded pair**: the protection is not a Φ = 0
accident, it is the A-factor structure of every radial-derivative term in the
field equations. The reopening happens one level down, in the EoM's R₀, and
§3 shows it is not enough.

## 3. Configuration test (192 primary rows + 32 controls; 0 pass)

Throat system per row: p_r equation V₀ = F₀/(8π); ρ equation (primary cone
F′₀ = −2F₀/r₀; secondary ρ_d = ρ_dem − V₀ ≥ 0); scalar EoM for φ′₀; health
F₀ > 0, K = 1/F₀ + 3F_φ0²/(2F₀²) > 0, c_T² = 1 (F multiplies R only — unchanged
by Φ). Checker (`p421_check.py`) recomputed every row from stored throat data.

- **V = 0 rows (96 primary + 16 control):** die at the p_r channel, as at
  Φ = 0 — supply p_r = 0 (dust cannot help, its p_r = 0) vs demand
  −F₀/(8π) ≤ −1/(8π) < 0 for every φ₀. Φ′ changes nothing here.
- **Mass rows (96 primary + 16 control):** p_r fixes φ₀² = 1/(4π − ξ)
  (F₀ = 1.041, 1.086, 1.189, 1.661 for ξ = 0.5, 1, 2, 5; health clean on every
  row, K > 0). The EoM then forces **F′₀ > 0 on every row and branch**, while
  the cone needs F′₀ = −2F₀ < 0: primary cone residual F′₀ + 2F₀ ranges
  +2.16…+8.61, and the secondary dust demand ρ_d = ρ_dem − V₀ < 0 everywhere.
  The new R₀ lever moves F′₀'s magnitude substantially — Ellis ξ = 5:
  F′₀ = 0.796 (a = −2) → 2.899 (a = +2); √-shape ξ = 5: 3.183 → 5.287 — but
  never its sign, on either shape, either family, or either φ₀ branch.
  Mechanism: at cone data the EoM's V′₀ and F_φ0R₀ terms keep φ₀φ′₀ > 0 for
  all |a| ≤ 2 in the grid; a enters F′₀ affinely with slope F_φ0²/(8π) > 0,
  so within the registered a-range the sign is unreachable.
- **Controls (a = 0, 32):** 0 pass — the P40-1 outcome reproduced row-for-row
  in throat quantities, as the gate requires.
- **Families:** throat outcomes are identical between families 1 and 2 on
  every row (Φ″₀ enters nothing at the throat; Φ(∞) = a vs a/2 is a time
  rescaling and is stated as such — it labels no row, since no row survives).
- **Full-domain audit:** owed only on throat-passing rows (shared bars);
  survivors = 0, so no integration was run and no row is labelled
  throat-local. Asymptotic-GR read is vacuous for the same reason.
  Solution-grade residuals: the throat system is exact algebra; the deciding
  residuals above are O(1), nowhere near the 0.02 bar.

## 4. Verdict

**INERTNESS SURVIVES Φ ≠ 0.** p_r,dem at r₀ carries no F′₀/F″₀ for all Φ′₀ in
the registered families; the surviving protection is the A-factor structure
itself — every radial-derivative term in the t–t and r–r field equations,
including all Φ′-coupled ones, is multiplied by A or cancels against its
∇^t∇_t / ∇^r∇_r partner, and A(r₀) = 0 is the throat condition. The FLUX
UN-PROTECTED and CHANNEL OPENS forms are both excluded: no Φ′-coupled
derivative term enters p_r,dem at r₀ (named terms: AΦ′₀F′₀, 2AF₀Φ′₀/r₀ —
both A-suppressed), and no row survives anyway. The single genuine Φ′ effect
in the whole throat system is the EoM shift via R₀, and on the registered
grid it moves only the magnitude of the already-wrong-signed EoM flux.

## 5. C12 accounting

All configurations here are static, pre-existing throats — no formation
mechanism is computed and **no transport claim is made or implied** by this
verdict.

## 6. Follow-ups (Failure Protocol)

1. **Continuous-a root (mechanism-suggested by §3's affine structure):**
   F′₀(a) is affine in a with slope F_φ0²/(8π) > 0, so the EoM + cone system
   F′₀ = −2F₀ has exactly one real root per (ξ, shape) on the mass branch —
   e.g. a* ≈ −9.8 (Ellis, ξ = 5) and a* ≈ −14.4 (√-shape, ξ = 5), far outside
   the registered grid and at large negative Φ(∞) (a strong time rescaling).
   Pre-register those a* rows: if the throat system closes there, the row
   owes the full-domain audit, including whether Φ → a* at ∞ and the
   e^{2Φ} redshift remain regular on [r₀, 10³r₀]. This is the one door the
   present algebra leaves open, and it is a door in the EoM, not in p_r.
2. **Singular-Φ′ classes are outside this proof's scope:** the A-suppression
   argument assumes AΦ′ → 0 at r₀. A family with Φ′ diverging at the throat
   (e.g. Φ′ ~ (r−r₀)^{−1/2}) could leave a finite AΦ′F′ residue in p_r,dem —
   test as its own pre-registered item, with regularity of e^{2Φ} itself
   audited first.
