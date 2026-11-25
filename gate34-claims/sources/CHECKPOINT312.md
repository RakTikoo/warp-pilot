# CHECKPOINT 312 — ONE-SIGN M′

## FTL verdict (leading)

**POSITIVE-DENSITY MEMBER at registered scope.** Five of 36
registered members (four distinct reads) have depth past the
material bar (−0.0034, SAMPLER-M adversary-polished) AND
ρ_req ≥ 0 at ALL four binding sites (Phase 293 site rule):

| member | depth (SAMPLER-M polished) | min ρ_req (binding sites) |
|---|---|---|
| ramp broad (10.5,19.5), m₀ = +0.5 | −1.278702×10⁻³ | +2.146340×10⁻⁵ |
| ramp broad (10.5,19.5), m₀ = +1.0 | −1.180275×10⁻³ | +6.498030×10⁻⁵ |
| ramp early (10.5,14.5), m₀ = +1.0 | −5.922334×10⁻⁴ | +1.665425×10⁻⁵ |
| edges E1, m₀ = +1.0 | −6.232242×10⁻⁴ | +1.665425×10⁻⁵ |
| edges E2, m₀ = +1.0 | −6.232242×10⁻⁴ | +1.665425×10⁻⁵ |

At every winner's every binding site the density is R-carried:
R/(16π) positive and larger than |Q_K/(16π)| (e.g. edges
m₀=+1.0, M ≡ 2, M′ ≡ 0: pure (1−1/M) piece R1 = +6.36×10⁻⁵ at
the worst site vs Q_K = −4.70×10⁻⁵). Phase 308's edge-sign
failure mechanism is defeated as designed: with no falling
edge inside [10,20], the M′ piece poisons nothing at positive
m₀, and what replaces it as the binding failure everywhere
else is Q_K (the negated-square remnant) — which the broad
ramp's R growth and the edges-out plateau both outgrow at the
top of the grid.

Fences on the headline: the verdict is the registered
binding-site verdict, NOT pointwise positivity — every
winner's SET-244 ρ minimum is still negative (worst case
edges +1.0: −6.714×10⁻⁵; ramp broad +1.0: −7.561×10⁻⁸). Depth
(NEC) remains negative at the polished sites; no spinor match
was run (parent's charge); no joint pass or drive is claimed.

## Controls (all passed before verdicts)

- **C1 (M ≡ 1):** PASS, all diffs 0.0 (depth
  −0.001386956608122417, SET NEC min −0.004079744835667814,
  Type-I 1245 exact, polish r 12.369476376022238, four site
  ρ_req exact vs stored).
- **C2 (Phase 308 m₀=+0.25 near-miss via p308_lib as
  stored):** PASS, all diffs 0.0 (depth −1.031034×10⁻³,
  min ρ_req −1.680665×10⁻⁴, per-site ρ_req exact).
- **C3 (split formula audit):** PASS, max diff 4.07×10⁻¹⁹ vs
  stored anatomy split (bar 1e-12); at M ≡ 1, R = 0 exactly
  and the Phase 295 factorisation value matched to
  ≤ 5.15×10⁻¹⁹. The split also reproduces the assembly's
  ρ_req at all 144 recorded binding sites to ≤ 1.52×10⁻¹⁸.
- **E1/E2 identity audit (registered prediction):** CONFIRMED
  EXACTLY — max diff 0.0 over depth, SET NEC min, Type-I
  count, and every site read, at all six m₀. No machinery
  defect.

## Headline numbers

- Trade curve (36 members): depth improves monotonically
  with m₀ in both families (worst −3.411601×10⁻³, ramp broad
  m₀=−0.5, the only member failing the depth bar; best
  −5.922334×10⁻⁴, ramp early m₀=+1.0). min ρ_req crosses zero
  only at positive m₀ and only where the rise covers the
  binding sites.
- Anatomy answers: (a) one-signed M′ at positive m₀ fixes the
  falling-edge poisoning (Phase 308's S4 R = −9.12×10⁻⁵ →
  broad-ramp S4 R = +5.61×10⁻⁵ at the same m₀ = +0.25);
  Q_K replaces it as decider at every surviving positive
  failure (29 of 36 worst sites overall are Q_K-decided;
  R2 decides 5, all negative-m₀ ramps; R1 decides 2). The
  late window never engages (binding sites sit where M ≡ 1;
  reads are the winner's verbatim). Negative-m₀ ramps make
  the whole band a falling edge: sites migrate to
  r ≈ 17.7–18.2 and R2 poisons globally. (b) The pure
  (1−1/M) term comes all the way: at plateau M = 2 its
  +6.36×10⁻⁵ at the worst site beats Q_K's −4.70×10⁻⁵; the
  crossing is between m₀ = +0.5 (net −2.05×10⁻⁵) and +1.0.
- Full tables, winner site reads, and splits:
  `phase312/results/p312_memo.md` and
  `phase312/results/p312_results.json`.

## Three goals

FTL: positive-density members found in the extended class
(see above; spinor match is the parent's charge, not run).
Wormhole: standings untouched — no read bears on them.
Subluminal record: standings untouched (Procaccia 0.1363 /
verified 0.10 unchanged). **DESK: NO DATA CONTACT.**

Registration: `phase312/work/p312_registration.md` (written
before computation). No ledger append, no launches, no
external contact. Writes inside phase312/ only.
