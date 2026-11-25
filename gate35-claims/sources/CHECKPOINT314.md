# CHECKPOINT 314 — THE POINTWISE PUSH

## FTL verdict (leading)

**POINTWISE MEMBER.** The extended (three-function)
class produces members whose required density is
non-negative EVERYWHERE on the posed volume (SET-244,
6642 points, SAMPLER-M), with both hard bars held.
Five members confirmed at full protocol; headline:

**ramp m₀ = +4.00, rise [9, 20.5]** (M = 1 + 4·[U(r;9,20.5)
− U(r;21,24)], Gate-30 winner (S,N) verbatim, β = 1.1):
SET-244 ρ min **+8.272455×10⁻⁵** (0 negative points;
argmin at the outermost node r = 19.878, transverse,
carried by R1/(16π) = +8.053×10⁻⁵ against
Q_K/(16π) = −4.57×10⁻¹⁰); depth (SAMPLER-M polished)
**−5.327659×10⁻⁴**, past the −0.0034 bar; binding-site
ρ_req ≥ 0 at all four sites (min +1.172278×10⁻⁴ at S4).

Other confirmed pointwise members: ramp (4.25, [9,20])
+8.161643×10⁻⁵; ramp (4.00, [9,20]) +8.066120×10⁻⁵;
ramp (4.00, [9,19.5]) +8.055642×10⁻⁵; edges m₀ = +3.00
(plateau M ≡ 4; confirmed under the E3 extent label,
E1/E2 screen-identical) +4.613988×10⁻⁵, depth
−2.407065×10⁻⁴.

FENCE: a density statement about the target only. The
headline member's SET EC reads (SAMPLER-M) remain
violated — NEC min −1.170007×10⁻³, WEC min
−1.044069×10⁻², DEC min −1.000003 — and depth is a
negative NEC read. No spinor match run (parent's
charge); no joint pass or drive claimed.

## Controls (all passed before verdicts)

- **K1 PASS, exact:** Phase 312's five winners re-read
  under this phase's machinery (p312_lib copied
  byte-identical, md5 504a941734e895ba8919b2630ba99358):
  SET-244 ρ min, depth, min site ρ_req all at **diff
  0.0** vs stored (bar 1e-9).
- **K2 (starting pockets):** broad +1.0's pocket is at
  r = 10.3659, M ≡ 1, M′ ≡ 0 (inside the rise's start),
  pure Q_K = −7.561×10⁻⁸, 324 negative points; edges
  +1.0's is at r = 15.4878 on the plateau, R1 +8.294×10⁻⁵
  vs Q_K −1.501×10⁻⁴ (both /(16π)), 1000 negative points.

## Mechanism (one paragraph)

Height cannot reach the broad base's pocket (at
r1 = 10.5, m₀ ∈ {1.25…4} all read the identical
−7.561242×10⁻⁸ — the pocket sits where M ≡ 1 upstream
of the rise). PLACEMENT closes it: starting the rise at
r1 = 9.0 puts M > 1 over the whole volume; the minimum
migrates to the outer rim (r = 19.878), where S, S′ ≈ 0
kill Q_K and the floor is R1's (1−1/M)/r² term — positive,
improving slowly with height (saturation) and width
(r2 → 20.5 keeps M′ > 0 at the rim, adding R2). The
edges family closes by height alone (crossing between
m₀ = +1.5 and +2.0; the mid-radius transverse R1-vs-Q_K
contest). The broad base never stalled (round gain
+8.28×10⁻⁵ vs the 10⁻⁸ threshold), so the registered
early-base fallback was not run. Landscape: 25 screened
points, 10 confirmations, all stored.

## Three goals

FTL: pointwise-density members found in the extended
class (above; spinor match is the parent's charge, not
run). Wormhole: standings untouched. Subluminal record:
standings untouched (Procaccia 0.1363 / verified 0.10).
**DESK: NO DATA CONTACT.**

Registration: `phase314/work/p314_registration.md`
(written before computation). Results:
`phase314/results/p314_results.json` (assembled),
`p314_controls.json`, `p314_screens.json`,
`p314_confirmed.json`, `p314_opt_log.json`; memo
`phase314/results/p314_memo.md`. No ledger append, no
launches, no external contact. Writes inside
phase314/ only.
