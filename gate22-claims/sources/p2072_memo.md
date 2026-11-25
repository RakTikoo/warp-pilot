# P207-2 MEMO — p2052 home re-judgement

Item: Phase 207 item 2. Registration:
phase207/REGISTRATION207.md item 2 (questions and verdict
forms fixed BEFORE computation); original registration
phase205/work/p2052_registration.md. Frame of record:
Phase 166 pin, Gate-19-corrected tensor, venv python.
Driver: phase207/work/p2072_driver.py (home frame's own
machinery, the phase205/work/p2052_verify.py pattern — NOT
the laptop bundle's stored metrics). Checker:
phase207/work/p2072_checker.py. Results:
phase207/results/p2072_results.json, p2072_check.json.
Deciding rows re-read independently FROM THEIR STORED
PARAMETERS (c, a, b) in
phase205/kaggle/p2052_laptop_results.json; no stored metric
field was used as a read. All grouped maxima/medians and
legality fractions below are SET READS on their registered
point sets. No ledger append, no launch, no contact.

## 1. CONTROLS FIRST (fresh home process — ALL PASS, diff 0.0)

- (i) c188, ξ′≡0: grouped max 0.3735926852617199 (median
  0.15219929922850717, worst idx 53), subset-56 legality
  0.5892857142857143 / binding-504 0.5555555555555556 —
  diffs 0.0 / 0.0 / 0.0 (bar ≤1e-12).
- (ii) Phase 200 quadratic point (222.40517306235458,
  −448.0125455002431): grouped max 0.33214607022582865
  (median 0.11913572005098905, worst idx 53), legality
  0.42857142857142855 / 0.3888888888888889 — diffs 0.0.
- (iii) s1881: grouped max 0.4599716785662495 (median
  0.17463003161535146, worst idx 53), legality
  0.5892857142857143 / 0.5515873015873016 — diffs 0.0.
  R-DISC: grouped max 0.32211152871575427 (median
  0.20843104373044163, worst idx 46), legality
  0.6071428571428571 / 0.5674603174603174 — diffs 0.0.
- Local floor (a), stored (c188, a=209.73203489424677,
  b=−402.19460466740816): grouped max 0.33360189190103595
  (median 0.13428727646913516, worst idx 53), legality
  0.5357142857142857 / 0.5218253968253969 — diffs 0.0.
- Local floor (b), stored (c, a=261.6275603873349,
  b=−448.00737249436514): grouped max 0.3112672647133272
  (median 0.15044286159123524, worst idx 53), legality
  0.5535714285714286 / 0.5317460317460317 — diffs 0.0.

## 2. DENSIFIED BASE (recomputed at home, c188 profile)

Home base on the registered 112-point interleaved set:
grouped max 0.5823609867395406 (median 0.1489623186637289,
worst idx 73) — diff 0.0 vs the registered value. The
laptop JSON's B2 densified block quotes a base of
0.8873403305593545: that number is NOT a c188 base — the
kernel's densified construction (p2052 densified_read)
computes its "base" with the CANDIDATE's own braiding
profile at ξ′=0, which for B2's moved profile reads
0.8873403305593545. The home c188 base 0.5823609867395406
governs, and every candidate densified read below is my
own home re-read of the candidate on the same 112-point
set. (For A2, whose profile IS c188, the kernel's quoted
base coincides with the home base.)

## 3. DECIDING ROWS — HOME RE-READS (set reads)

### A2 best feasible (fixed c188 profile; a=209.77147156834883, b=−402.337211727546)
- Grouped max 0.33359735790526734, median
  0.13420781142863725, worst idx 47. (Kernel stored:
  0.33359735790527, worst idx 53; diff 2.7×10⁻¹⁵. The
  worst index is a near-tie: rel at idx 53 reads
  0.3335973579051624, only 1.05×10⁻¹³ below the idx-47
  max — the argmax flips at cross-machine noise level;
  the max VALUE confirms.)
- Subset-56 legality 0.5357142857142857; binding-504
  0.5218253968253969 (both identical to kernel).
- Discipline: rel52 0.29347568087394627 < 0.9458528915590193
  (also ≤ stored cap 0.8200684930282758); rel53
  0.3335973579051624 < 0.9980872152899012 (also ≤ stored
  cap 0.8668214090756287); C* worsening
  0.0018527208039951643 ≤ 0.05; shadow worsening
  0.023567700182683636 ≤ 0.05; coverage 8/8; λmin
  +0.6476300825127849 > 0; budget violations pp
  +6.5×10⁻¹⁵ / p −0.005435608687861318 (max ≤ 1e-9 pass);
  disciplined_eom and feasible188 both true.
- Densified (112-pt): grouped max 0.5660981137016052
  (median 0.12445208360264444, worst idx 73), densified
  subset legality 0.5535714285714286 — identical to the
  kernel's candidate read; < home base 0.5823609867395406,
  and subset gain not inverted (0.3336 < 0.3735926852617199):
  densified survival YES.

### A1 best feasible (cross-check; fixed c188 profile; a=209.73203489424677, b=−402.19460466740816)
- Grouped max 0.33360189190103595, median
  0.13428727646913516, worst idx 53 — this is exactly the
  local floor (a) point; kernel stored grouped max
  0.3336018919011436, diff 1.08×10⁻¹³ (the kernel's own
  control noise class).
- Subset-56 0.5357142857142857; binding-504
  0.5218253968253969.
- Discipline: rel52 0.293482655511474, rel53
  0.33360189190103595 (both under pair caps and stored
  caps); C* worsening 0.0019360858774776328 ≤ 0.05;
  shadow 0.023483854116929416 ≤ 0.05; coverage 8/8; λmin
  +0.6476300825127849 > 0; budget pp +6.5×10⁻¹⁵ / p
  −0.005435608687861318; disciplined, feasible188.
- Densified: grouped max 0.566244521072677 (median
  0.12441108918926154, worst idx 73), densified subset
  legality 0.5535714285714286 — survives vs home base.

### B2 best disciplined-legal joint point (stored c=[−9.001901322475181, −10.895113820524866, −12.521738750623996, −12.752001138272155, −14.127922207160722, −15.07682510452481, −18.72100046508755, −20.919525016876772, −28.266833740516887, −21.779773880277563], a=264.76201780516345, b=−448.01250001545833)
- Grouped max 0.30988004951050263, median
  0.143465342493379, worst idx 53. (Kernel stored:
  0.3098800495106134; diff 1.11×10⁻¹³, again the kernel's
  own control-noise class — its laptop controls showed
  diffs up to 1.2×10⁻¹³ against home values.)
- Subset-56 legality 0.5535714285714286; binding-504
  0.5317460317460317 (both identical to kernel).
- Discipline: rel52 0.2636467694970357 < 0.9458528915590193
  (≤ stored cap 0.8200684930282758); rel53
  0.30988004951050263 < 0.9980872152899012 (≤ stored cap
  0.8668214090756287); C* worsening 0.046519787871726774
  ≤ 0.05; shadow worsening 0.046963092632364006 ≤ 0.05;
  coverage 8/8; λmin +0.6482910476508038 > 0; budget
  violations pp −6.763866530851148×10⁻⁵ / p
  −0.005449936611976805 (≤ 1e-9 pass); disciplined_eom
  and feasible188 both true.
- Densified (112-pt, home re-read): grouped max
  0.5686747891261495 (median 0.13555998041461398, worst
  idx 73), densified subset legality 0.5446428571428571
  — identical to the kernel's candidate read, and
  0.5686747891261495 < home c188 base 0.5823609867395406
  with subset gain not inverted: densified survival YES
  under the governing home base (not merely under the
  kernel's candidate-profile base 0.8873403305593545).

## 4. THE THREE REGISTERED QUESTIONS

(1) Feasible floors confirmed? YES, as home set reads:
direction (a) full-scan floor grouped max
0.33359735790526734 (A2; A1 cross-check 0.33360189190103595);
direction (b) full-scan floor grouped max
0.30988004951050263 (B2). All home diffs vs kernel stored
grouped maxima ≤ 1.11×10⁻¹³; legalities, discipline
clauses and densified candidate reads identical.

(2) Did full scan depth beat the local floors? Direction
(a): local 0.33360189190103595 → full 0.33359735790526734,
gain 4.533995768607468×10⁻⁶ — effectively nothing; the
full A scan re-found the local floor's neighbourhood.
Direction (b): local 0.3112672647133272 → full
0.30988004951050263, gain 0.0013872152028245877 — real
but small. Neither gain crosses any bar.

(3) Headline test (grouped max <0.30 AND both legalities
≥0.518 AND all discipline clauses AND densified
survival)? NOT MET by any re-read point. A2, A1 and B2
each satisfy legality, every discipline clause and
densified survival; each fails ONLY the grouped-max
conjunct. Closest is B2 at 0.30988004951050263, short of
0.30 by 0.00988004951050263. The kernel's provisional
verdict (NO HEADLINE POINT AT FULL SCAN DEPTH) stands.

## 5. CHECKER

p2072_checker.py recomputed every verdict-carrying number
from p2072_results.json (controls, densified base, all
three deciding rows incl. discipline fields and densified
reads, both gains, headline booleans): 72/72 PASS
(p2072_check.json).

## 6. VERDICT (registered form 1, verbatim)

**RE-JUDGEMENT CONFIRMS**

Full-scan floors as home set reads: direction (a)
0.33359735790526734 (gain over local floor
0.33360189190103595: 4.533995768607468×10⁻⁶ — no
material gain); direction (b) 0.30988004951050263 (gain
over local floor 0.3112672647133272:
0.0013872152028245877 — small). No headline point at
full scan depth; B2 misses grouped max <0.30 by
0.00988004951050263 with every other conjunct met.

No ledger append, no launch, no pass claimed; health
(cr2) and the 0.02 bar are untouched by this item.
