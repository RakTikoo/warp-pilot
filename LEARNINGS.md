# What this programme has learned — methods, artefacts, and self-corrections

This is a living methods record. It contains **no discovery claims**. Every result claim made by this programme lives in its claims packs and passed the programme's novelty-and-verification gate before publication; this document has a different job. It records what the search taught us about doing computational warp and metric searches honestly, so that other people running similar searches can avoid our mistakes — including the two times our own red teams caught inflated or false results before anything based on them was published.

The pattern behind most of the lessons is simple: a number is not a result until we know what produced it, what directions and regions it did **not** test, whether the configuration solves the equations it is supposed to solve, and whether the same answer survives an independently built calculation. The sections below state each lesson in plain language first, then give the episode and the standing rule it produced.

---

## 1. The 8π lesson

**Plain language:** a small units mistake can make every result in a scan look better by the same factor. If only one derived quantity is checked, the error can survive for a long time because all the wrong numbers agree with each other.

**The episode.** The pre-registered coverage definition was

\[
\mathrm{supply\ ratio}=\frac{C(k^*,k^*)/8\pi}{D},
\qquad
D=-(G/8\pi)(k^*,k^*),
\]

where \(D\) is the positive general-relativistic deficit at a binding point. The scan code divided the **raw** correction \(C(k,k)\) by the already-divided deficit. Every stored ratio was therefore exactly \(8\pi\) times the consistent ratio. The factor was verified point by point: stored ÷ true \(=25.13274122871835=8\pi\).

The most visible casualty was a Phase 7 row whose stored full/partial coverage was **0.980 / 0.984**. In consistent units it is **full 0.829 / partial 0.880**. The programme's full-alignment bar was 0.90, so the “alignment shown” verdict was retracted internally. Recomputing Phase 6 also deflated its best crossing row from stored partial/full **0.586 / 0.530** to true **0.319 / 0.251**; the maximum true partial coverage in any Phase 6 row was 0.375 and the maximum true full coverage was 0.363. The Phase 6 negative verdict became stronger, not weaker, but its quantitative anatomy had to be corrected.

**Standing rule:** define ratios in consistent units, and do not let any verdict rest on a ratio until a **ratio-free cross-check** agrees exactly. In this programme the cross-check counts binding points directly — for example, the counted fraction with \(T_{\rm req}(k^*,k^*)\ge 0\) for full coverage — rather than recomputing the same ratio in a second cosmetic form.

---

## 2. The fitted-tensor lesson: the f(T) case study

**Plain language:** a calculation can manufacture an exciting signal if the formula being evaluated was fitted during an identification step, if the configuration is not actually a solution of the theory, and if the scan reads only the directions in which the answer looks good. The f(T) episode combined all three failure modes. It is the centrepiece of this document because it shows why the programme's red-team stage is not optional.

**The episode.** In Phase 10, an exponential-family f(T) teleparallel scan produced the programme's first scan-level alignment read: with the recorded health gate passing, full coverage was **0.9048 at \(\beta=1.1\)** and **0.9175 at \(\beta=1.5\)**; partial coverage was **0.9147 / 0.9310**, and the median supply ratios were **4199.3 / 180529.5**. Those numbers were labelled only as a **scan signal under attack**. The configuration was never published as a claim.

Phase 11's red team first reproduced the stored signal exactly, then attacked it under pre-registered criteria:

- **Point-hunt:** minimising the required matter's null contraction continuously over directions and the full wall volume gave worst NEC values of **\(-1.221\times10^{12}\)** at \(\beta=1.1\) and **\(-1.262\times10^{20}\)** at \(\beta=1.5\), against a problem deficit of only about \(3\times10^{-3}\).
- **Full-volume audit:** NEC was violated on **82.6%** of the wall volume at \(\beta=1.1\) and **82.5%** at \(\beta=1.5\). The Hawking–Ellis Type-I fractions were only **0.167 / 0.169**.
- **Field equations:** the antisymmetric f(T) equations had relative median residuals **0.789 / 0.668**, and the required matter's conservation residuals were **0.440 / 0.455**. The prescribed tetrad and metric were therefore designer-sustained on the moving bed, not a solution of the theory there.
- **Independent path:** a from-scratch calculation using the **published** form of the key \(W\) tensor reversed the supply's sign. Full coverage became **0.000 / 0.000**, with median ratios **−2065 / −71493**. The stored signal lived entirely in the gate-fitted \(W_2\) tensor form used by the earlier scan.
- **Overshoot anatomy:** at **63.9% / 72.2%** of binding points, a positive binding-direction contraction coexisted with a worst-direction NEC below \(-100\) times the local deficit. The spatial quadratic part of \(W\) along the binding direction was carried **0.996–1.000** by a single large negative eigen-component, while the positive read came from mixed components amplified by \(f_{TT}\sim1.2\times10^{15}\) / \(2.4\times10^{21}\) at mid-wall.

One attack did **not** land: the tetrad attack was inconclusive because the transformed tetrads were not good on that bed either, and a covariant reading did not collapse the coverage. That did not rescue the signal. Four independent killing attacks were enough, and the signal was retired internally.

**Standing rules:**

1. Use **published tensor forms** for verdict-carrying calculations. A form fitted to pass an identification gate is a hypothesis about the implementation, not a substitute for the theory's published equations.
2. Treat **field-equation residuals as first-class verdict components**. A prescribed metric, tetrad, scalar, or matter field held in place by unspecified physics is designer-sustained, not a solution.
3. Put a **full-volume, all-directions NEC read inside every scan**, not only in a later red team. A scan that cannot see most of its own volume cannot call its output a signal.

---

## 3. Binding-direction blindness

**Plain language:** if a scan scores only the null direction that binds hardest in general relativity, a correction can look helpful there while being catastrophic in another direction. Coverage along one chosen direction is a diagnostic, not an energy-condition audit.

**The episodes.** In the Phase 7 canonical-scalar case, the binding-point read was blind to the full tensor: over the full wall volume, NEC was violated at **41.1%** of points for the leading row, and at the binding points themselves NEC over **all** null directions held at only **34.7%** of points. The scalar could help along its gradient while remaining essentially neutral orthogonally, so the shell's own deficits passed through almost unchanged; the worst-site NEC was repaired by only about **4.5%**.

The \(G_{4X}\) sector showed the sharper spike version. Its best partial coverage anywhere was **0.375**, from a control row with the sector off. Turning the sector on drove the worst binding NEC from **\(-1.8\times10^{-4}\)** at \(c_3=0\) to **\(-6.4\times10^{-2}\)** at \(|c_3|=2\) and **\(-3.4\times10^{-1}\) / \(-3.6\times10^{-1}\)** at \(c_3=\mp8\) — roughly **2000× worse than general relativity**, and grid-converged rather than a finite-difference artefact. The f(T) anatomy in Section 2 is the same phenomenon at exponential scale.

**Standing rule:** every coverage number must be accompanied by the **worst-direction NEC**, a Type-I fraction, and a full-volume violation fraction. If those companions are absent, the coverage number is only a clue about where to audit next.

---

## 4. Artefacts we now catalogue

**Plain language:** most false positives in this kind of search are not exotic physics. They are ways for a finite grid, a finite sample, or a badly chosen threshold to hide the point that would have failed.

The programme now treats the following as named artefact classes:

- **Radial sampling hole** — *Signature:* a configuration passes on the sampled radii, then fails when fresh or denser radii find a narrow violation between them.
- **Angular pocket** — *Signature:* a localised violation sits in an angular sector or null direction that a coarse or symmetry-assuming sample never visits.
- **Stencil-scale exploitation** — *Signature:* a design passes at one finite-difference spacing and fails at half that spacing; in the recorded case, rows passed at \(h=0.3\) with **\(+6.60\times10^{-7}\) / \(+6.75\times10^{-7}\)** and failed at \(h=0.15\) with **\(-1.02\times10^{-4}\) / \(-1.34\times10^{-5}\)**.
- **Threshold poisoning** — *Signature:* one out-of-domain point with \(|\hat T|\sim10^{297}\) inflates a significance threshold computed over all points and silently empties the verdict set, producing blank or NaN rows.
- **Edge-stencil contamination at a shell's inner edge** — *Signature:* the worst “cavity” sample is a single point at \(r_{\rm rel}=8.90\), one step inside an edge-peaked shell; it collapsed **72×** from \(h=0.1\) to \(h=0.05\), to **\(-2.29\times10^{-6}\) / \(-2.02\times10^{-6}\)**, and appeared even when auditing an exact isolated shell because the auditor's stencil reached across the density onset while the cavity interior was clean to \(\le1.1\times10^{-15}\).

**Standing rule:** audit on fresh points, at more than one resolution, with domain masks and thresholds stated in advance. A worst point must be classified as physics, boundary effect, or stencil artefact before it is allowed to carry a verdict.

---

## 5. Superposition is not solving

**Plain language:** adding a known shell to a known background is not the same as finding the shell that is in equilibrium **in that background**. The interaction terms are part of the problem, and they can be the same size as the margins being tested.

**The episode.** In Phase 1, a shell superposed on a Schwarzschild background failed even at zero velocity: the static total worst margin at \(M_{\rm bg}=1\) was **\(-9.9\times10^{-5}\)**. In Phase 5, the shell was instead re-solved in the total geometry. The corresponding static configuration passed: core NEC **\(+4.77\times10^{-5}\)** and core worst margin, DEC, **\(+3.57\times10^{-5}\)**; an exact one-dimensional read gave core NEC **\(+4.32\times10^{-5}\)**. The earlier failure was therefore a property of the superposition construction, not a general verdict on shells in that background.

A later moving-shell investigation found the same lesson one level deeper. A core failure in a Painlevé–Gullstrand embedding was traced to an inconsistent lapse for the superposed shift: the stationary core read **\(-9.626\times10^{-5}\)** in the inconsistent build and **\(+4.11\times10^{-5}\)** after the total-lapse-consistent rebuild. The sign flip came from making the embedding internally consistent, not from changing the physical prescription being tested.

**Standing rule:** verdicts about composite spacetimes require **re-equilibrated configurations** in the total geometry, with lapse, shift, and matter prescriptions solved or transformed consistently. A superposition can be a useful first estimate, but its failure does not close the re-solved problem and its pass would not establish one.

---

## 6. Closures can be variable artefacts

**Plain language:** if a derivation divides by a quantity that goes to zero, the resulting blow-up may belong to the variables rather than to the physics. A closure based on that blow-up is not structural until the same question has been asked in variables that remain regular.

**The episode.** A wormhole margin closure rested partly on behaviour near \(r\approx3.41\), where a variable \(\tilde\xi\) is defined through division by \(Dt\) and \(Dt\) vanishes. Phase 10 rebuilt the perturbation system in regular variables,

\[
S := Dt^2\mathcal P_1,
\qquad
R_1 := Dt^2(2\mathcal P_1-\mathcal F),
\]

which never divide by \(Dt\). At the refined crossing \(r_c=3.4199111162\), the physical quantities passed through smoothly: \(\det\mathcal K\to-8.105\times10^{-3}\) from both sides, no eigenvalue diverged or flipped, and the second radial sound speed had the finite two-sided limit \(c_{s2}^2\to+0.4930\). The singularity was carried by \(\tilde\xi\) alone.

That did **not** turn the episode into a positive result. The finite content at the crossing was real and negative, \(R_1(r_c)=-2038.37\). Phase 11 then mapped the regular-variable margin over the full domain: \(R_1<0\) on \([0,7.812]\), \([17.84,47.84]\), and the endpoint segment, with minimum **−8534**. The tested levers did not remove it; at the crossing, the best prefactor row shallowed the value to about **−1520**, and halving the \(F_4\) amplitude still left **−759**. The direction therefore re-closed, but now on finite content checked in regular variables rather than on a pole in a singular representation.

**Standing rule:** before calling a closure structural, re-ask it in variables that do not divide by the vanishing quantity. If the obstruction dissolves, reopen only the part that depended on it. If finite negative content remains, exhibit that content and close on that instead.

---

## 7. Embedding-dependence is not slicing-dependence

**Plain language:** two calculations can disagree because they use different coordinates for the **same** spacetime, or because they built **different approximate spacetimes** that merely share a prescription. Those are different statements with different physics, and the words used in a claim must not blur them.

**The episode.** The moving-shell record initially used “slicing-dependence” for a pass/fail split between an areal build and a total-lapse-consistent Painlevé–Gullstrand build. The gate required the wording to be corrected to **embedding/ansatz-dependence**. The two builds are different ansatz spacetimes; there is no exact transform between them in the two-centre construction. The obstruction is concrete: the two-centre areal metric has rank-2 structure where a time reparametrisation supplies only rank-1 freedom.

The numerical split is part of the episode, not a detail to be hidden. In the areal embedding, the moving audit's cavity values were **\(-2.75\times10^{-8}\)** at \(d=50\) and **\(-1.48\times10^{-8}\)** at \(d=100\), with passing cores. In the PG embedding, the configuration passed at \(d=100\) and failed at \(d=50\); the gate's independent path reproduced the \(d=50\) moving core's sign in the range **\(-1.5\times10^{-6}\) to \(-3.4\times10^{-6}\)**, rather than as a precision value.

**Standing rule:** say **slicing** only when an exact coordinate relationship to one spacetime is established. Otherwise name both embeddings or ansätze, state both outcomes, and carry the failure beside the pass in every summary of the claim.

---

## 8. Data gates are kill criteria, not afterthoughts

**Plain language:** a mathematically interesting supply is not viable if the theory parameters it needs are already excluded by observation. Observational gates belong in the pre-registration, beside the health gates, not in a paragraph added after a scan looks promising.

**The episode.** Einstein-aether rows produced a strongly speed-asymmetric binding-point supply: health-passing partial coverage was **0.813 at \(\beta=1.1\)** and **0.791 at \(\beta=1.5\)**, while full coverage was only **0.218 / 0.449**. Even before any question of alignment, the solar-system PPN gates were decisive: **0 of 327 rows** passed the data gates.

The gate's independent check also corrected the programme's first explanation of the exclusion. The original mechanism sentence said that tuning \(\alpha_2=0\) forced \(c_2<0\) and made \(s_0^2<0\). That sentence was false. On the \(c_{13}=0\) slice, \(\alpha_1=-4c_{14}\) exactly, the \(\alpha_2=0\) curve is

\[
c_2=\frac{c_{14}}{1-2c_{14}},
\]

and \(s_0^2\equiv1\) along that curve, so the tuning is health-compatible. The verified exclusion mechanism is a scaling conflict: \(\alpha_1=-4c_{14}\) caps \(c_{14}\le2.5\times10^{-5}\), while the supply's useful tail lives at \(c_{14}\sim O(1)\). The best health- and data-passing row in the later 180-row attack reached only **partial 0.030 / full 0.000**. The \(\alpha_2\) gate used in the record was \(|\alpha_2|\le4\times10^{-7}\).

**Standing rule:** pre-register observational gates — PPN parameters, gravitational-wave speed, laboratory or astrophysical bounds, as applicable — with the same status as ghost, gradient, and sound-speed health gates. A row that needs observationally excluded parameters is excluded, however interesting its coverage read may be.

---

## 9. The gate itself

**Plain language:** the final protection is procedural. A result should not become public merely because the team that produced it believes it. Someone must separately ask, “Has this already been published?” and someone else must rebuild the deciding calculation by a different path.

**The system.** This programme's gate has two independent axes:

- **Novelty:** a documented literature search, with queries and sources recorded, returning **NOVEL**, **PARTIALLY KNOWN** with the known part exactly delimited and cited, or **KNOWN**, in which case the result dies as “ours” and credit belongs to its real authors.
- **Correctness:** an independent second path returns **REPRODUCED** within stated margins, **NOT YET** with the missing piece named, or **FAILS**, in which case an anatomy is required.

Only a claim with its novel part delimited and its deciding computations reproduced can be upload-ready. Gate 1 also produced an intermediate outcome that became standard practice: **upload-ready after restatement**. A seven-case classification, for example, could not be published as one literal rank statement applying uniformly to all seven cases; the published form separates the five strict instances from the two structural analogies and flags the unexamined health premise where it applies.

**What the gate caught.** Gate 2 reproduced the deciding numbers for the aether claim but disproved its exclusion-mechanism sentence, as detailed in Section 8: the **0/327** exclusion stood, while its explanation had to be replaced. The same gate caught a grid-unstable torus motion headline: the coarse-grid value **\(-3.78\times10^{-4}\) at \(h=0.3\)** was stencil-unstable in both judges and was replaced by the converged **\(-1.51\times10^{-4}\) at \(h=0.075\)**, identical in the two independent judges. It also imposed the embedding-versus-slicing wording correction in Section 7.

**Standing rule:** publish the correction **with** the claim, and append dated errata to the internal records rather than silently absorbing them. A restatement is not a cosmetic edit; it is part of the scientific record showing which sentence was wrong, what replaced it, and which numbers survived independent checking.

---

## Reuse, citation, and error reports

This methods document is released under the **MIT License**, the same licence as the repository. You may reuse its checklists, wording, and procedures, with attribution to the Warp Pilot repository and the relevant release or claims pack where a specific episode is cited. If you cite an episode's numbers in your own work, please cite the underlying checkpoint or claims-pack source as well as this summary, so that readers can inspect the full audit trail.

If you find an error — a wrong number, a missing prior source, an artefact class we have mischaracterised, or a lesson that does not follow from its episode — please report it through the repository's GitHub issues: <https://github.com/RakTikoo/warp-pilot>. Corrections that change a number or a conclusion will be recorded as dated errata, not quietly rewritten.
