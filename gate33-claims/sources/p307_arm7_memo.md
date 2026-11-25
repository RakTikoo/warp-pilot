# PHASE 307 — ARM 7 MEMO: POLARISATION CONTENT (red team)

Registration: `phase307/work/p307_registration.md`, Arm 7.
Charge: applicability first. Retrieve what GW polarisation-
content tests actually bound, decide whether they bound the
spin-1 mode's emission from the fiducial binaries or the mode's
coupling constants, and apply a bound to the flat maximisers
only if one genuinely translates.
All sources retrieved 2026-11-24.

## VERDICT: NOT APPLICABLE — weak HOLD

Wording, as registered: the polarisation-content tests are
**NOT APPLICABLE** to the tested points, for the reasons in
§2, and Arm 7 therefore closes as a **weak HOLD** on the
distance-0 statement's fence completeness — worded as such:
the fence is not shown incomplete by this bound class; the
bound class is shown not to reach the channel. No retrieved
polarisation result is stated as, or translates into, a bound
on c₁, c₋, or any EA coupling, and none bounds extra-
polarisation emission from binaries radiating at ~10⁻⁵ Hz.

## 1. What the tests bound (primary sources)

### 1.1 GW170814 — Abbott et al. (LIGO–Virgo), PRL 119, 141101 (2017)

- **Observable:** the polarisation content of ONE detected
  signal — a binary-black-hole coalescence (30.5 + 25.3 M☉,
  network SNR 18) seen coherently in LIGO Hanford, LIGO
  Livingston and Virgo. The test is geometric: the three
  detectors' different antenna-pattern responses to tensor,
  vector and scalar modes project the same incoming wave
  differently, and the data's projection is compared across
  hypotheses.
- **Hypothesis structure:** pure alternatives only. "We perform
  a test comparing the tensor-only mode with scalar-only and
  vector-only modes. We find that purely tensor polarization
  is strongly favored over purely scalar or vector
  polarizations." Reported Bayes factors: tensor over pure
  vector ≈ 200, tensor over pure scalar ≈ 1000
  (log₁₀ B ≈ 2.3 and 3.0, as restated in Takeda et al.,
  PRD 103, 064037 (2021), §I).
- **Band:** the LIGO/Virgo observing band, of order
  10–10³ Hz; the analysed signal is a stellar-mass merger
  sweeping through the tens-to-hundreds-of-Hz range.
- **What is NOT in the paper:** any mixed-content amplitude
  bound, any upper limit on a vector/scalar strain fraction,
  and any statement about a theory's coupling constants. The
  result is a model-selection odds between pure hypotheses
  for that signal.

### 1.2 GW170817-era and GWTC-1/2 pure tests

Same structure, catalog-wide: Bayesian model selection between
GR-tensor and pure-scalar / pure-vector alternatives for the
same detected signals (GW170817's version strengthened by the
electromagnetic sky-position prior; Takeda et al. 2021
reanalysis: log Bayes factors 21.078 (vector) and 44.544
(scalar) for GW170817 with the location prior). Still pure-vs-
pure, still per-signal content, still no coupling bound.

### 1.3 GWTC-3 — Abbott et al. (LVK), PRD 112, 084080 (2025), §VII

The strongest and most careful statement retrieved, and the
one that adds mixed hypotheses:

- **Method:** null-stream projection. The strain is projected
  onto the subspace orthogonal to a chosen basis of
  polarisation beam patterns; hypotheses T, V, S and the mixed
  TS, TV, VS, TVS are compared by combined log₁₀ Bayes factors
  against the pure-tensor hypothesis, marginalising over each
  extra mode's **relative amplitude and phase with respect to
  the basis mode(s)** (their Table VIII). Events: all
  eligible events of the first three observing runs
  (FAR < 10⁻³ yr⁻¹), 2- and 3-detector.
- **Results (L = 1 basis, combined, their Table IX):**
  log₁₀ B^S_T = −4.24 ± 0.30; log₁₀ B^V_T = −1.70 ± 0.30;
  log₁₀ B^VS_T = −1.73 ± 0.30 — pure-scalar, pure-vector and
  vector–scalar are "significantly disfavored". The mixed
  hypotheses involving tensor: log₁₀ B^TS_T = +0.20 ± 0.30,
  log₁₀ B^TV_T = +0.31 ± 0.30, log₁₀ B^TVS_T = −0.08 ± 0.30 —
  in the paper's words, mixed tensor hypotheses "**cannot be
  ruled out conclusively**", and they carry an Occam penalty
  from their larger prior volume rather than an amplitude
  exclusion. (L = 2 basis, 3-detector events, Table X: mixed
  hypotheses more strongly disfavoured, log₁₀ B from −0.98
  (TS) to −1.29 (TVS) — still evidence ratios, not amplitude
  limits.)
- **What is NOT in §VII:** no upper limit on the amplitude of
  any extra mode, no fractional-strain bound, and no bound on
  any theory parameter. The section's output is a table of
  Bayes factors between signal-content hypotheses for
  detected compact-binary signals in the LIGO/Virgo band.

### 1.4 The one amplitude-style statement in the class

Cheung et al., ApJ 1001, 130 (2026) (Gaussian-process null-
stream search over 42 three-detector GWTC-3 events): no
significant nonstandard polarisation (highest ln B = 1.5,
insignificant against background); **90% credible upper
limits on the fractional deviation in GW strain from 0.28 to
11.30, median 1.32**. Even taken at face value this is (a) a
statement about extra strain *in the same detected signals*,
in the detector band; (b) weak — a median limit of 1.32
permits extra-polarisation strain comparable to the tensor
strain itself; (c) not a coupling bound: no map from a
fractional-strain limit for stellar-mass mergers at
~10² Hz to (c₁, c₂, c₁₄) exists in the paper or, per §3, in
any retrieved source.

## 2. Applicability to the tested channel — four independent failures

1. **Frequency / source-class mismatch (deciding).** The
   fiducial systems whose dipole emission the fence prices
   radiate at their orbital frequency: Hulse–Taylor,
   P_b = 7.75 h → f_orb = 3.584×10⁻⁵ Hz (quadrupole GW at
   7.17×10⁻⁵ Hz); PSR J1738+0333, P_b = 8.5 h →
   f_orb = 3.268×10⁻⁵ Hz. The dipole piece the channel is
   priced on is emitted at f_orb. The polarisation tests
   analyse signals at ~10–10³ Hz. The gap is **5.45 orders of
   magnitude** to the bottom of the detector band (10 Hz) and
   ~6.5 orders to its middle — the registration's "five-plus
   orders" confirmed arithmetically. No detector in the
   analyses has any response at 10⁻⁵ Hz; the tests contain no
   information, direct or extrapolated, about emission there.
   (The sources also differ in kind: the tests' signals are
   the final seconds of stellar-mass mergers; the fiducials
   are detached, slowly inspiralling pulsar binaries whose
   merger is ~10⁸ years away.)
2. **Observable mismatch.** The tests bound the polarisation
   *content of a detected signal* — which antenna-pattern
   mixture fits strain data already recorded at high SNR.
   The channel's claim is a flux *ratio* (dipole/GR-quadrupole
   = 2.8044×10⁻⁵ for HT) for systems no GW detector observes.
   A Bayes factor against a pure-vector *replacement* of the
   tensor signal says nothing about a vector admixture at the
   10⁻⁵ flux level in a different source at a different
   frequency; and GWTC-3's mixed analysis, the only one that
   even poses the admixture question, cannot rule the mixed
   hypotheses out (§1.3) and quotes no amplitude limit.
3. **No coupling translation exists.** No retrieved source
   states a bound on a coupling constant, and none supplies a
   map (c₁, c₂, c₁₄) → (polarisation content of a LIGO-band
   merger signal) that could be inverted. Producing such a
   map would require an EA waveform model for merging
   binaries in the detector band — sensitivities, dipole and
   mode fluxes at relativistic compactness, mode speeds
   (the tested points have c_V = 1, 2, 10 and Corner B's
   3240, so the EA modes do not even co-propagate with the
   tensor mode at the shared arrival time/sky-location the
   null-stream construction assumes). That is a research
   programme, not a retrieved bound; the arm does not invent
   it. Takeda et al.'s "waveforms consistent with modified
   theories" are generic pure-polarisation templates, not an
   EA coupling analysis.
4. **Even the strongest amplitude statement does not reach.**
   Cheung et al.'s median 90% fractional-strain limit (1.32)
   is ~5 orders of magnitude above the channel's HT dipole
   ratio (2.8×10⁻⁵) in spirit — and it is a strain fraction
   for different sources in a different band, so the
   comparison is illustrative only, not an application.

Any one of (1)–(3) alone suffices for NOT APPLICABLE; all
four hold independently.

## 3. What would have to exist for this arm to break a point

A published analysis that either (a) bounds extra-polarisation
content of a signal at ~10⁻⁵ Hz (e.g. a pulsar-timing or
binary-pulsar polarisation test stated as a flux/amplitude
limit — none retrieved; the binary-pulsar constraints that
do exist for EA are the fence's own L7–L9 legs, a different
bound class), or (b) computes EA polarisation content for
LIGO-band mergers as a function of the c_i and confronts it
with GW170814/GWTC data (none retrieved). Until one exists,
the polarisation bound class leaves the fence exactly as
complete as Phase 303 left it, and the distance-0 statement
inherits nothing from this arm in either direction.

## 4. Retrieval limits (on the face of this memo)

Retrieved in full text: Abbott et al. GW170814, PRL 119,
141101 (2017) (publisher PDF via NSF/Strathclyde mirrors);
Abbott et al. GWTC-3 tests of GR, PRD 112, 084080 (2025),
§VII read in full incl. Tables VIII–X (Caltech authors'
library PDF). Abstract/full-text grade: Takeda et al.
arXiv:2010.14538 (Bayes-factor restatements and framework);
Cheung et al., ApJ 1001, 130 (2026) (abstract + introduction;
the fractional-strain limits are from its abstract). No
strain data were re-analysed; no catalog likelihoods were
touched. The applicability decision rests on the sources'
stated observables, bands and hypothesis structures, all of
which were retrieved at primary grade.

DESK (Arm 7): GW catalog data contacted at the level of
published analyses only (GW170814, GWTC-3 §VII, GWTC-3
null-stream search) — no applicable bound found, because the
tests bound detected-signal content at 10–10³ Hz, not
couplings and not 10⁻⁵ Hz emission: **NOT APPLICABLE = weak
HOLD**, worded as such.
