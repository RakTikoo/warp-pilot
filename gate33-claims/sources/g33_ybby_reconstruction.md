# Gate-33 — YBBY reconstruction from its own text

Source: `~/workspace/warp-pilot/gate33/work/ybby_src/paper.tex` (3,779 lines), LaTeX source of
Yagi, Yunes, … (YBBY), arXiv:1311.7144, PRD 89, 084067 (2014).
All line numbers below are tex line numbers in that file. Quotes are verbatim (LaTeX markup retained).
No verdicts, no new computations — extraction only.

**Figure identification (needed throughout).** The tex contains, in order, only these figure labels:
`fig:Pdot-constraint-summary` (L429), `fig:MR-AE`, `fig:sens-alpha1`, `fig:sens-c-`,
`fig:sens-core-boundary`, `fig:sens-C-HL`, `fig:Pdot-EA` (L3124), `fig:Pdot-HL` (L3155).
Therefore:

- `fig:Pdot-constraint-summary` — the **first** figure in the paper, in §I.B Executive Summary,
  including `EA-constraints` (left) and `KG-constraints` (right) — is **Fig. 1**:
  > L426–L427: `\includegraphics[width=8.0cm,clip=true]{EA-constraints}` / `& \includegraphics[width=8.0cm,clip=true]{KG-constraints}`
- `fig:Pdot-EA` — the four-panel Einstein-æther constraint figure in §VII C.1, including
  `Pdot-constraint-NSWD-Bhat`, `Pdot-constraint-NSWD-Antoniadis`, `Pdot-constraint-NSNS`,
  `alpha-constraint-NSWD` (L3120–L3123) — is **Fig. 7**.
- `fig:Pdot-HL` is the khronometric analogue (Fig. 8).

§VII in the published numbering = `\section{Pulsar Constraints}` (L2965, `\label{sec:Constraints}`);
VII A = L2971, VII B = L3025, VII C = L3041 (`\label{alpha-hat-sec}`),
VII C.1 = `\subsubsection{Einstein-\AE ther Theory}` (L3111).

---

## 1. Eqs. (188)–(195): exact forms and what each bounds

The published numbers (188)–(195) correspond, in tex order in §VII A–C, to the labels
`obs`, `pred`, (unlabelled), `eq-used`, `flux-AE`, `A-AE`, `SF-alpha1`, `SF-alpha2`.
(The tex itself carries no printed numbers; the mapping is by sequence and by content —
(191) is the operative band equation `eq-used`, (194)–(195) are the æther $\hat\alpha$ mapping.)

### Eq. (188) — `obs` (L2992–L2995): the observed decay rate, stated as GR ± errors
> `\left(\frac{\dot{P}_{b}}{P_{b}}\right)_{\obs} = \left(\frac{\dot{P}_{b}}{P_{b}}\right)_{\GR} \left(1 \pm \delta_{\obs} \pm \delta_{\inferred}\right),`

What the errors are (L2997):
> "up to the observational uncertainty $\delta_{\obs}$ in $\dot{P}_{b}$ and the inferred error $\delta_{\inferred}$ induced in the predicted value of $\dot{P}_{b}/P_{b}$ due to the error that propagates from the individual masses."

### Eq. (189) — `pred` (L3001–L3004): the æther/khronometric prediction
> `\left(\frac{\dot{P}_{b}}{P_{b}}\right)_{\AE,kh} = \left(\frac{\dot{P}_{b}}{P_{b}}\right)_{\GR} \left(1 + \delta \dot{P}_{\AE,kh} \right)\,,`

where (L3006) "$\delta \dot{P}_{\AE, kh}$ is the fractional difference in the prediction."

### Eq. (190) — unlabelled (L3010–L3012): the "most conservative" bound
> `\left| \delta \dot{P}_{\AE,kh} \right| \leq \delta_{\obs} + \delta_{\inferred} = {\cal{O}}(10 \%)\,.`

Introduced (L3008): "Comparing Eqs.~\eqref{obs} to~\eqref{pred}, one then finds that the most conservative constraint comes from demanding"

### Eq. (191) — `eq-used` (L3016–L3019): **the operative band equation actually used**
> `\delta \dot{P}_{\AE,kh}(m_{A}+\delta m_{A}, P_{b} +\delta P_{b}, \kappa^{i}_{\AE,kh},{\rm{EoS}}) \leq \delta_{\obs}\,,`

Introduced (L3014): "In what follows, we will instead use the equivalent relation"

Note, verbatim-level: as printed, Eq. (191) has **no absolute value** and its right-hand side is
$\delta_{\obs}$ alone (not $\delta_{\obs}+\delta_{\inferred}$); the mass/period errors appear instead
inside the argument list. What it bounds / its variables (L3021–L3022):
> "to place constraints on the coupling constants $\kappa^{i}_{\AE,kh}$, where $\kappa^{i}_{\AE} = (c_{+},c_{-})$ in Einstein-\AE ther theory and $\kappa^{i}_{kh} = (\lambda,\beta)$ in khronometric theory."
> "Here $m_{A}$ and $P_{b}$ are the best-fit parameter for the (inferred) individual masses and the orbital period, while $\delta m_{A}$ and $\delta P_{b}$ are their associated statistical errors.  Recall that, in these theories, the non-GR correction to the prediction of the orbital decay rate not only depends on the individual masses and the orbital period, but also on the EoS through the sensitivities. Thus, we will search for the region in the two-dimensional coupling parameter space where Eq.~\eqref{eq-used} is satisfied, with $\delta \dot{P}_{\AE,kh}$ evaluated within $m_{A} \pm \delta m_{A}$, $P_{b} \pm \delta P_{b}$ and various values of the sensitivities, determined by the EoS and the individual masses. Let us emphasize that Eq.~\eqref{eq-used} does not lead to a line in the two-dimensional coupling parameter space, but rather a two-dimensional region." (L3022)

$\delta\dot P$ itself is built from Eqs. (192)–(193) below via
$\dot P_b/P_b \propto \langle\mathcal A\rangle$; §VII C.1 (L3113): "The predicted rate of orbital decay is given by Eq.~\eqref{A-AE} with $(\mathcal{C},\mathcal{A}_{1},\mathcal{A}_{2},\mathcal{A}_{3})$ functions of the coupling constants $(c_{+},c_{-})$".

### Eq. (192) — `flux-AE` (L3058–L3061 in the read at offset 3055; label at L3060 approx. — see tex `\label{flux-AE}` immediately after the displayed equation)
> `\frac{\dot{P}_{b}}{P_{b}} = - \frac{192 \pi}{5} \left(\frac{2 \pi G_{N} m}{P_{b}}\right)^{5/3} \left(\frac{\m}{m}\right) \frac{1}{P_{b}} \left<\mathcal{A}\right>\,,`

Introduced: "After orbit-averaging, the orbital decay rate to leading PN order reduces to" — for "a binary system with non-spinning components in a circular orbit in either Einstein-\AE ther or khronometric theory."

### Eq. (193) — `A-AE` (the `\begin{align}` labelled `A-AE` following Eq. (192))
> `\left<\mathcal{A}\right> \equiv &`
> `\frac{5(1-c_{14}/2)}{32} \left(s_1 - s_2\right)^2  \left( \frac{P_b}{2 \pi G_N m} \right)^{2/3} \mathcal{C}`
> `\times \left[ 1 + {\cal{O}} \left( \frac{v^{2}}{c^{2}}, \frac{V_{CM}^{2}}{c^{2}},(s_{1}-s_{2})^{-1} \frac{V_{CM} v}{c^{2}} \right) \right]`
> `+  \left( 1-\frac{c_{14}}{2} \right)\left[\left(1 - s_{1}\right) \left(1 - s_{2}\right)\right]^{2/3}`
> `\times \left( \mathcal{A}_1 + \mathcal{S} \mathcal{A}_2 + \mathcal{S}^{2} \mathcal{A}_3  \right) \left[ 1 + {\cal{O}} \left( \frac{v^{2}}{c^{2}} \right) \right]\,.`

First term = dipolar (proportional to $\mathcal C$ and $(s_1-s_2)^2$); second term = quadrupolar.
Text: "notice that the first term in Eq.~\eqref{A-AE} (the one proportional to ${\cal{C}}$) leads to dipolar radiation, which scales as $(v/c)^{-2}$ relative to the GR quadrupole term."
Here $s_A$ are the sensitivities (denoted $\sigma_A$ in the $\hat\alpha$ equations).

### Eq. (194) — `SF-alpha1` (L3090–L3092, `\label{SF-alpha1}`)
> `\hat{\alpha}_{1}^{\AE} &= \alpha_1^{\AE} + \frac{c_{-} (8+\alpha_1^{\AE}) \sigma_A^{\AE}}{2 c_1}\,,`

### Eq. (195) — `SF-alpha2` (L3093–L3095, `\label{SF-alpha2}`)
> `\hat{\alpha}_{2}^{\AE} &= \alpha_2^{\AE} + \frac{c_{-} (8 + \alpha_1^{\AE} ) \sigma_A^{\AE}}{4 c_{1}} - \frac{  (c_{14} -2)  (\alpha_1^{\AE} - 2 \alpha_2^{\AE}) \sigma_A^{\AE}}{2  (c_{14} - 2 c_{+})}\,,`

What (194)–(195) are / how obtained (text immediately before them, §VII C):
> "The mapping can be obtained by replacing $\alpha_{1} \mapsto \hat{\alpha}_{1}$, $\alpha_{2} \mapsto \hat{\alpha}_{2}$, $s_{1} \mapsto 0$ and $s_{2} \mapsto 0$ in Eq.~\eqref{B-AE}. By equating the latter to Eq.~\eqref{B-AE} without these replacements, we can read off the relation between the strong-field PPN coefficients and the standard PPN coefficients and sensitivities."
> "Observe that both of these quantities depend not only on the weak-field values of the PPN parameters $(\alpha_{1},\alpha_{2})$, but also on the sensitivities of the NSs, which depend on the masses; this is why we use observations of PSRs J1012+5307 and J1738+0333, since we know the NS masses for these systems. Saturating the Solar System constraints on the weak-field parameters $(\alpha_{1},\alpha_{2})$, and using the strong-field constraints on $(\hat{\alpha}_{1},\hat{\alpha}_{2})$, one can place constraints on $(c_{-},c_{+})$ and $(\lambda,\beta)$." (L3108)

The weak-field $\alpha_{1,2}^{\AE}$ entering (194)–(195) are defined earlier (L1086–L1089):
> `\alpha^{\AE}_1 &=& -\frac{8(c_3^2+c_1c_4)}{2c_1-c_{+} c_{-}}\,,`
> `\alpha^{\AE}_2 &=& \frac{\alpha^{\AE}_1}{2} - \frac{(c_1+2c_3-c_4) (2c_1+3c_2+c_3+c_4)}{(2-c_{14})c_{123}}\,,`
with $c_\pm \equiv c_1\pm c_3$, $c_{14}\equiv c_1+c_4$ (L1094–L1099, labels `cpm`/`c14`).

The observed $\hat\alpha$ bounds these are compared against (§VII B, L3036):
> "Using data from pulsar-white dwarf binaries with known three-dimensional velocity, PSRs J1012+5307 and J1738+0333, Shao and Wex placed the constraints $\hat{\alpha}_{2} < 1.8 \times 10^{-4}$ and $\hat{\alpha}_{1} \lesssim 10^{-5}$ at $95\%$ confidence."

(Khronometric analogues `SF-alpha1-HL`/`SF-alpha2-HL` follow immediately after (195) in the tex.)

---

## 2. The band-construction algorithm as STATED (§VII C.1)

### The controlling passage — Fig. 7 (`fig:Pdot-EA`) description, L3116 (single long sentence, verbatim)
> "Figure~\ref{fig:Pdot-EA} shows these constraints. The area below and to the right of the solid black line is the allowed $(c_{+},c_{-})$ region after imposing Cherenkov and stability constraints. The green-shaded area with red dotted borders is the allowed $(c_{+},c_{-})$ region after imposing constraints from observations of PSR J1141-6545 (top, left panel), PSR J0348+0432 (top, right panel),  PSR J0737-3039 (bottom left panel) and PSR J1738+0333 (bottom right panel). **As discussed earlier, Eq.~\eqref{eq-used} must be evaluated varying over $(c_{+},c_{-})$, but also allowing for the inferred error in the masses, the observational error in the orbital decay rate, the allowed range on $(\alpha_{1}^{\AE},\alpha_{2}^{\AE})$ given Solar System constraints, and various NS sensitivities associated with different EoSs. Similarly,  Eqs.~\eqref{SF-alpha1} and~\eqref{SF-alpha2} must be evaluated by trying different values of $\alpha_{1}^{\AE}$ and $\alpha_{2}^{\AE}$ within the Solar System constraints, as well as different values of the sensitivities for different EoSs. The result, thus, is not a line in $(c_{+},c_{-})$ space, but rather a two-dimensional region, as shown in the figures.**"

### The Fig. 7 caption, L3124 (verbatim)
> "(Color online) Constraints on Einstein-\AE ther theory from binary pulsar observations. The green-shaded regions correspond to those allowed after imposing constraints from the observation of PSR J1141-6545 (top, left panel), PSR J0348+0432 (top, right panel), PSR J0737-3039 (bottom left panel) and PSR J1738+0333 (bottom right panel). **The first three panels use observations of the orbital decay rate through Eq.~\eqref{eq-used}, allowing for inferred error in the masses, observational error in the orbital period, the allowed range of the PPN parameters $(\alpha_{1}^{\AE},\alpha_{2}^{\AE})$ given Solar System constraints, and different sensitivities given different EoSs. The last panel uses constraints on the strong-field PPN parameters and Eqs.~\eqref{SF-alpha1} and~\eqref{SF-alpha2}.** For comparison, we also plot the allowed $(c_{+},c_{-})$ region after imposing Cherenkov and stability constraints (below and to the right of the solid black line), as well as the values of $(c_{+},c_{-})$ required for the orbital decay rate to agree exactly with the GR prediction in the zero-sensitivity limit. Observe that the new, strong-field constraints are much more stringent than the Cherenkov/stability bounds."

Note the caption/body discrepancy, preserved verbatim: caption says "observational error in the **orbital period**"; body L3116 says "the observational error in the **orbital decay rate**". §VII A (L3022) lists both $m_A\pm\delta m_A$ and $P_b\pm\delta P_b$.

### Per-panel assignment (from L3113–L3114, L3116, L3124)
- **J1141−6545 (top left), J0348+0432 (top right), J0737−3039 (bottom left):** Eq. (191) (`eq-used`),
  i.e. $\dot P_b$ via Eqs. (192)–(193).
  L3113: "Comparing the prediction of the orbital decay rate to observations of PSR J1141-6545, PSR J0348+0432 and PSR J0737-3039, we can then place constraints on the $(c_{+},c_{-})$ coupling parameter space of this theory."
- **J1738+0333 (bottom right):** Eqs. (194)–(195) (`SF-alpha1`/`SF-alpha2`) against the
  $\hat\alpha$ constraints from that system.
  L3113–L3114: "Comparing the prediction of $(\hat{\alpha}_{1}^{\AE},\hat{\alpha}_{2}^{\AE})$ to the constraint on these quantities derived from observations of PSR J1738+0333, we can also place constraints on this parameter space."
  Explicit exclusions (L3114): "We do not consider constraints derived from the orbital decay rate of PSR J1738+0333 and from the $(\hat{\alpha}_{1}^{\AE},\hat{\alpha}_{2}^{\AE})$ constraint of PSR J1012+5307 because they are weaker than constraints derived with the systems described above."

### VARIED (as stated)
1. $(c_+,c_-)$ itself — the plane being scanned: "Eq.~\eqref{eq-used} must be evaluated **varying over $(c_{+},c_{-})$**" (L3116).
2. Masses within inferred error: "allowing for the **inferred error in the masses**" (L3116, L3124); §VII A: "evaluated within $m_{A} \pm \delta m_{A}$" (L3022).
3. Orbital period / decay-rate error: "$P_{b} \pm \delta P_{b}$" (L3022); "the observational error in the orbital decay rate" (L3116) / "observational error in the orbital period" (caption, L3124).
4. $\alpha_1^{\AE},\alpha_2^{\AE}$ over their Solar-System-allowed range: "the **allowed range** on $(\alpha_{1}^{\AE},\alpha_{2}^{\AE})$ given Solar System constraints" (L3116); for the $\hat\alpha$ panel, "**trying different values** of $\alpha_{1}^{\AE}$ and $\alpha_{2}^{\AE}$ **within the Solar System constraints**" (L3116). The Solar-System ranges themselves are stated at L653–L654 (§II): "in the weak-field, Solar System observations constrain these parameters to very small values $|\alpha_1|\lesssim 10^{-4}$ and $|\alpha_2| \lesssim 10^{-7}$".
5. Sensitivities over EoSs: "**various NS sensitivities associated with different EoSs**" (L3116); "different sensitivities given different EoSs" (L3124); §VII A: "various values of the sensitivities, determined by the EoS and the individual masses" (L3022).

### Held FIXED (as stated)
The tex states **no** quantity as held fixed for the Fig. 7 bands other than the identity of each
system (its best-fit masses, $P_b$, and its $\delta_{\obs}$ entering Eq. (191)).
In particular, §VII C.1 does **not** state that $\alpha_{1,2}$ are held at fixed values for the bands,
and does **not** state that sensitivities are held at one EoS. (The fixed values
$\alpha_1^{\AE}=10^{-4}$, $\alpha_2^{\AE}=4\times10^{-7}$ appear only in §VI, for generating the
sensitivity *fit* data — see §6 below.)
Other stated modelling fixings for §VII C: eccentricity neglected ("In all cases, the eccentricity is small and will thus be neglected", §VII C opening; corrections are ${\cal O}(e^2)$ and "negligible in Eq.~\eqref{eq-used}"), spins neglected (slow-rotation argument, §VII C), non-spinning circular orbit for Eqs. (192)–(193).

### Executive Summary restatement of the same variation (L452)
> "Binary pulsar constraints lead to {\textit{regions}} of viable coupling parameter space. This is because in deriving these constraints one has to allow for different values of the coupling constants (within the Solar System constraints) and the sensitivities (because of the different possible EoSs), and account for the observational error in the orbital decay rate and the orbital period, as well as the error in the inferred masses of the binary."

---

## 3. Projection vs fixed sub-family vs point-by-point TOV sensitivities

### What the tex's language decides: an existential / "some choice passes" construction
The stated construction is (i) in its wording — a point of the $(c_+,c_-)$ plane is in the shaded
region if Eq. (191) [or (194)–(195)] is satisfied for **some** choice of the varied quantities
within their stated ranges:

- L3022: "we will **search for the region** in the two-dimensional coupling parameter space **where Eq.~\eqref{eq-used} is satisfied, with** $\delta \dot{P}_{\AE,kh}$ **evaluated within** $m_{A} \pm \delta m_{A}$, $P_{b} \pm \delta P_{b}$ **and various values of the sensitivities**, determined by the EoS and the individual masses."
- L3116: "Eq.~\eqref{eq-used} **must be evaluated varying over** $(c_{+},c_{-})$, **but also allowing for** the inferred error in the masses, the observational error in the orbital decay rate, **the allowed range** on $(\alpha_{1}^{\AE},\alpha_{2}^{\AE})$ … and **various NS sensitivities associated with different EoSs**."
- L3116 ($\hat\alpha$ panel): "must be evaluated by **trying different values** of $\alpha_{1}^{\AE}$ and $\alpha_{2}^{\AE}$ **within the Solar System constraints**, as well as **different values of the sensitivities for different EoSs**."
- L3134–L3135: "the width of the allowed region is not controlled just by the observational error in the orbital decay rate, but also by the inferred error in the individual masses, the observational error in the orbital decay rate, the allowed range of $(\alpha_{1}^{\AE},\alpha_{2}^{\AE})$ given Solar System constraints, and also the different NS sensitivities that depend on the EoS … **one must vary over all such parameters to obtain the correct allowed region**."

The tex never uses the word "projection", and never states a formal quantifier ($\exists$ vs $\forall$);
the existential reading rests entirely on the "search for the region where … is satisfied, with …
evaluated within … / allowing for … / trying different values" wording above. That is all the tex says.

### What the tex does NOT decide: (ii) vs (iii) — how $\sigma$/$s$ is obtained inside Eq. (191)
**No sentence in §VII (A, B or C/C.1) states how the sensitivity entering Eq. (191)/(193) or
Eqs. (194)–(195) is evaluated at a given $(c_+,c_-)$** — i.e. the tex does not say, for the Fig. 7 bands,
whether $s$ is (a) recomputed numerically (TOV) point-by-point in $(c_+,c_-)$, (b) taken from the
Eq. `s-fit` / Appendix-C fits, or (c) taken in weak-field form. Specifically:

- §VII only calls them "various values of the sensitivities, determined by the EoS and the individual masses" (L3022) / "various NS sensitivities associated with different EoSs" (L3116).
- The weak-field form is explicitly **not** what the paper claims to use in general: Eq. `eq:weak-field-AE-s` (§VI) is presented as an approximation that "becomes highly inaccurate, with errors of roughly $15$--$30\%$ for realistic NS compactnesses" and the zero-sensitivity/weak-field curve is plotted in Fig. 7 only "for comparison" (L3124).
- The fixed values $\alpha_{1}^{\AE} = 10^{-4}$, $\alpha_{2}^{\AE} = 4 \times 10^{-7}$ are stated
  **only** as the choice made when *generating the numerical data for the fit* in §VI (L2723, §6 below).
  They are **not** stated anywhere in §VII as the values used for the Fig. 7 bands; §VII instead says
  $\alpha_{1,2}$ are varied over their allowed range (L3116). Any claim that the Fig. 7 bands were
  computed on the fixed-$\alpha$ sub-family therefore has **no support in §VII's text**.
- §VI's general claim about the sensitivities' provenance (Executive Summary, L415–L420 approx.):
  "With this at hand, we use the numerical solutions that we obtained to compute the sensitivities for isolated NSs for the first time in the theories under consideration. We then construct fitting functions that allow us to analytically model the sensitivities as a function of the compactness of the star and the coupling constants of the theory."
  This states both steps exist (numerical computation, then fitting functions) but does not state which one feeds Fig. 7.

**Bottom line for Q3:** from the tex alone, (i) is the stated shading rule; the (ii)/(iii)
distinction — fit-evaluated $\sigma(c_+,c_-,\alpha_1,\alpha_2,\mathrm{EoS},C_*)$ vs TOV-recomputed
$\sigma$ at each plane point — is **not answered by any sentence in the tex**. The only
$\sigma$-evaluation recipe with fixed $\alpha_{1,2}$ stated anywhere is the fit-data generation in §VI.

---

## 4. The combined region (Fig. 1) and the "almost a box" passage

### How Fig. 1 is formed — caption, L429–L430 (verbatim)
> "Constraints on the $(c_{+},c_{-})$ plane in \AE ther theory (left) and $(\lambda,\beta)$ plane in khronometric theory (right) **obtained by combining constraints derived from observations of  PSR J1141-6545, PSR J0348+0432, PSR J0737-3039 and PSR J1738+0333. The areas outside the (allowed) shaded regions are ruled out by stability/Cherenkov considerations (light blue), BBN (dark orange) and the combined binary pulsar constraints (dark purple).** The red dotted line corresponds to the values of the coupling constants required for the orbital decay rate to agree with the GR prediction in the zero-sensitivity/weak-field limit. Observe that the new constraints are much more stringent than all others."

### Executive Summary text, L443–L450 (verbatim)
> "Combining all of these constraints, we obtain the allowed coupling parameter space shown in Fig.~\ref{fig:Pdot-constraint-summary} (Einstein-\AE ther theory in the left panel and khronometric theory in the right panel).  **The colored regions are those allowed after requiring stability and absence of gravitational Cherenkov radiation (light blue), BBN constraints (dark orange) and binary pulsar constraints (dark purple).** The red dashed line corresponds to the values of the coupling constants for which the orbital decay rate equals the GR prediction, assuming the sensitivities vanish and working at leading-order in a weak-field expansion. Observe that the new constraints obtained here are much stronger than all other constraints. The constraint found in this paper is consistent with the order of magnitude estimate of Foster's in the small coupling region, but  the constraint on $c_{-}$ found here is slightly stronger."

So, as stated: Fig. 1 overlays **three** allowed sets — stability/Cherenkov, BBN, and the combined
binary-pulsar set. (For Einstein-æther, §II states BBN adds essentially nothing once
Eqs. `eq:Aecons`/`eq:Aecons2` hold: "$G_N \approx G_C$ up to terms of ${\cal{O}}(10^{-4})$, and thus, cosmological observations do not significantly reduce the viable region defined by Eqs.~\eqref{cp_constraint} and~\eqref{cm_constraint}" — see §7.)

### The intersection statement — §VII C.1, L3137 (FULL verbatim passage)
> "Reference~\cite{Foster:2007gr} argues that current tests will be satisfied if the weak field conditions are imposed and the coupling constants satisfy $(c_{+},c_{-}) \leq {\cal{O}}(10^{-2})$. **For any given system, we find that the allowed region is not a box with sides of ${\cal{O}}(10^{-2})$ but rather a band with width ${\cal{O}}(10^{-3})$. However, when we combine all of these allowed regions in the left panel of Fig.~\ref{fig:Pdot-constraint-summary}, their intersection is indeed almost a box with width of ${\cal{O}}(10^{-3})$ in the $c_{-}$ direction and ${\cal{O}}(10^{-2})$ in the $c_{+}$ direction. The change in shape of the combined allowed region is because different observations lead to allowed bands with different average slopes, which in turn is because for some systems dipolar radiation dominates, while for others it does not. The width of the box is determined by the smallest width of the bands, which is of ${\cal{O}}(10^{-3})$.** All together, these constraints constitute the first, accurate strong-field test of Einstein-\AE ther theory." (L3137–L3138)

Context that disambiguates "width in the $c_-$ direction":
- The sentence's subject is "**their intersection**" — "all of these allowed regions" = the per-system
  Fig. 7 bands. The box is the intersection object itself, so "width of ${\cal O}(10^{-3})$ in the
  $c_{-}$ direction and ${\cal O}(10^{-2})$ in the $c_{+}$ direction" is predicated of **the box**
  (the combined region), i.e. its extent/side length in each direction — in the same breath as the
  contrast "not a box **with sides of** ${\cal O}(10^{-2})$".
- The preceding sentence gives the per-system quantity separately: a single system's region is
  "a band with **width** ${\cal O}(10^{-3})$", and the closing sentence ties them: "**The width of the
  box is determined by the smallest width of the bands**, which is of ${\cal O}(10^{-3})$."
- The word "intersection" is used **only** for the combination of the per-system pulsar bands in
  this passage. The passage does not say the box is also intersected with the Cherenkov/stability
  or BBN sets; those appear in Fig. 1 as separately coloured allowed regions (L430, L445–L447).
  (For the khronometric analogue, L3162: "When we combine all the panels of Fig.~\ref{fig:Pdot-HL}, one obtains the right panel of Fig.~\ref{fig:Pdot-constraint-summary}. Observe that binary pulsar observations further constrain the parameter region previously allowed by stability and BBN considerations.")

### Width context from the preceding paragraph, L3134–L3135 (verbatim)
> "Moreover, the width of the allowed region is not controlled just by the observational error in the orbital decay rate, but also by the inferred error in the individual masses, the observational error in the orbital decay rate, the allowed range of $(\alpha_{1}^{\AE},\alpha_{2}^{\AE})$ given Solar System constraints, and also the different NS sensitivities that depend on the EoS, all of which depend strongly on the system that is observed. As we discussed earlier, one must vary over all such parameters to obtain the correct allowed region, **which as shown in Fig.~\ref{fig:Pdot-EA} is between ${\cal{O}}(0.1\%)$ and ${\cal{O}}(1 \%)$**."

### Plotted axis ranges
**Not in the tex.** No caption, axis label, or text in `paper.tex` states any axis range for
Fig. 7 or Fig. 1. The ranges below are read from the **figure PDF files** in the same source
directory (via `pdftotext -layout`), i.e. figure-file evidence, not tex evidence:

- Fig. 7, all four panels (`Pdot-constraint-NSWD-Bhat.pdf`, `Pdot-constraint-NSWD-Antoniadis.pdf`,
  `Pdot-constraint-NSNS.pdf`, `alpha-constraint-NSWD.pdf`): log–log, $c_+$ from $10^{-3}$ to $10^{0}$,
  $c_-$ from $10^{-3}$ to $10^{-1}$; panel legends read "allowed region / stability / weak-field" and
  "$\dot P$, J1141-6545", "$\dot P$, J0348+0432", "$\dot P$, J0737-3039", "$\hat\alpha$, J1738+0333" respectively.
- Fig. 1, left panel (`EA-constraints.pdf`): main axes linear, $c_+$ from 0.0 to 1.0, $c_-$ from 0.0 to 1.0,
  with an inset zoom showing $c_-$ ticks 0, 0.002, 0.004 and $c_+$ ticks 0, 0.01, 0.03;
  legends "Stability/Cherenkov", "Binary pulsars". (The BBN colour named in the caption is the
  khronometric panel's; in the EA panel text extraction only Stability/Cherenkov and Binary pulsars appear.)

---

## 5. Behaviour at large $c_-$ ($c_- \sim 0.1$–$0.2$); any explicit $c_-$ upper bound

**No statement in §VII C.1 (or elsewhere in §VII) addresses the allowed region's behaviour at
$c_- \sim 0.1$–$0.2$, and no explicit numerical upper bound on $c_-$ from the pulsar bands is stated
anywhere in the tex.** What the tex does contain:

1. The only $c_-$ bound stated as an inequality is the stability/Cherenkov one (§II, §7 below):
   $0 \le c_- \le c_+/[3(1-c_+)]$ — which at large $c_+$ permits large $c_-$.
2. The only pulsar-derived $c_-$ size statements are the order-of-magnitude ones in L3137:
   per-system band width ${\cal O}(10^{-3})$; combined box width ${\cal O}(10^{-3})$ in the $c_-$
   direction, ${\cal O}(10^{-2})$ in the $c_+$ direction; and Foster's earlier estimate quoted there,
   "$(c_{+},c_{-}) \leq {\cal{O}}(10^{-2})$".
3. Executive Summary (L450): "The constraint found in this paper is consistent with the order of magnitude estimate of Foster's in the small coupling region, but  **the constraint on $c_{-}$ found here is slightly stronger**." — "slightly stronger" than Foster's ${\cal O}(10^{-2})$ estimate; no number given.
4. §VI (not §VII): sensitivity-vs-$c_-$ numerics were run at large couplings for illustration —
   L2682–L2684: "Figure~\ref{fig:sens-c-} shows the absolute magnitude of the sensitivity as a function of $c_{-}$ for $c_{+} = 1$ and $c_{+} = 0.1$, saturating the Solar System constraint for $\alpha_{1}^{\AE}$ and $\alpha_{2}^{\AE}$. Observe that the sensitivity increases monotonically with $c_{-}$ and $c_{+}$." This is a statement about $s_{\AE}$, not about the allowed region.
5. Fig. 7's plotted $c_-$ axis stops at $10^{-1}$ (figure-file evidence, §4 above); the tex gives no
   statement about whether the bands close, open, or continue beyond the plotted range.

---

## 6. The Eq. (186) / Appendix C sensitivity FITS vs the Fig. 7 bands

Published Eq. (186) = tex Eq. `s-fit` (§VI, L2737–L2740 approx.; `\label{s-fit}`):
> `s_{\AE} = \sum_{\ell,m,n=0}^{2} c_{\ell, m, n} c_{+}^{\ell} c_{-}^{m} C_{*}^{n}\,.`

Appendix C = `\section{High-Order Fit of the Neutron Star Sensitivity in Einstein-\AE ther Theory}` (`\label{app:fit}`, L3541), with the 120-term version Eq. `s-fit2` (L3550–L3553):
> `s_{\AE} = \sum_{\ell=0}^{5} \sum_{m=0}^{3} \sum_{n=0}^{4} c_{\ell, m, n} c_{+}^{\ell} c_{-}^{m} C_{*}^{n}\,.`
> "The function Eq.~\eqref{s-fit} used to fit the numerical results for the NS sensitivities in Einstein-\AE ther theory contained only $27$ terms, which thus led to an $r^{2}$ value of approximately $0.96$. In this Appendix, we repeat the fit but with a function that contains $120$ terms, thus yielding an $r^{2}$ value closer to $0.999$." (L3544–L3549)

### The fits' stated region and generating choices — §VI, L2723–L2729 (verbatim, key passage)
> "Figures~\ref{fig:sens-alpha1} and~\ref{fig:sens-c-} show that the sensitivities in Einstein-\AE ther theory do not depend strongly on the EoS. Because of this, it is natural to develop an EoS-independent fitting formula. **First, we choose the LS220 EoS as a representative EoS with which to compute sensitivities and we set $\alpha_{1}^{\AE} = 10^{-4}$ and $\alpha_{2}^{\AE} = 4 \times 10^{-7}$, thus saturating Solar System constraints. With this, we then numerically compute the sensitivity in the range $c_{+} \in 3 \times (10^{-4},10^{-1})$, $c_{-} \in 3 \times  (10^{-5},10^{-3})$ and $C_{*} \in (0.11,0.28)$ for a total of $10^{3}$ points. We choose this region in the parameters $(c_{+},c_{-})$ as it will still be allowed after imposing binary pulsar constraints (see Fig.~\ref{fig:Pdot-constraint-summary}).**"

Fit quality / caveat (following lines, §VI):
> "We fit the data described above with Eq.~\eqref{s-fit}, using the fact that each numerical point is known to at least a fractional numerical accuracy of $1\%$. The fit returns an $r^{2}$ value of $0.959$, with fitted coefficients given in Table~\ref{fitting-table}."
> "Note that $c_{0,0,0}  = {\cal{O}}(\alpha_{1,2}^{\AE}) \neq 0$, because we have chosen $\alpha_{1,2}^{\AE}$ such that Solar System constraints are saturated. Thus, the fitting function does not go to zero as $c_{+} \to 0$ and $c_{-} \to 0$."

### Connection / separation between the fits and the Fig. 7 bands
- The **only** sentence connecting the fit region to the constraint figures is the one quoted above:
  the fit region was *chosen because* "it will still be allowed after imposing binary pulsar
  constraints (see Fig.~\ref{fig:Pdot-constraint-summary})" — i.e. the fit region is justified
  **by reference to** the (already-computed) allowed region, not stated to be the domain over
  which the bands were computed.
- **No sentence in §VII states that the Fig. 7 bands were computed using Eq. `s-fit`/`s-fit2`,
  nor that they were restricted to the fit region** $c_- \in 3\times(10^{-5},10^{-3})$,
  $c_+ \in 3\times(10^{-4},10^{-1})$. §VII's band description (L3116, L3124) mentions only
  "various/different sensitivities … for different EoSs", with no reference to `s-fit`, to LS220-only,
  or to the fit's fixed $\alpha_{1,2}$ values.
- Conversely, the fit is explicitly a **single-EoS (LS220), fixed-$\alpha_{1,2}$** object
  ("we choose the LS220 EoS as a representative EoS … and we set $\alpha_{1}^{\AE} = 10^{-4}$ and
  $\alpha_{2}^{\AE} = 4 \times 10^{-7}$"), whereas the bands are explicitly described as varying
  over EoSs and over the $\alpha_{1,2}$ range. As written, the two descriptions are of **different
  procedures**; the tex nowhere reconciles them or states that one was used to produce the other.
- Note also the scale mismatch visible in the tex itself: Fig. 7's plotted plane
  ($c_+$ to $10^{0}$, $c_-$ to $10^{-1}$, figure-file evidence) extends well beyond the fit region
  ($c_+$ to $3\times10^{-1}$, $c_-$ to $3\times10^{-3}$).

---

## 7. The Cherenkov/stability line in the panels

### What condition it is — Einstein-æther (§II, L682–L690 approx.; labels `cp_constraint`/`cm_constraint`)
Stated requirements (text preceding the equations):
> "Further constraints on $c_{\pm}$ come from **requiring that perturbations about a Minkowski background are stable and have positive energy, and that matter does not emit gravitational Cherenkov radiation**. Such radiation would be emitted if the speed of the \AE ther's and metric's propagating modes were smaller than the speed of light. These requirements result in the bounds"
> `0\leq c_+\leq 1\,,` (`\label{cp_constraint}`)
> `0\leq c_-\leq \frac{c_+}{3(1-c_+)}\,,` (`\label{cm_constraint}`)
> "to leading order in $\alpha_{1}$ and $\alpha_{2}$."

These follow the small-$\alpha$ reduction (L669–L677, labels `eq:Aecons`/`eq:Aecons2`):
$c_2=(-2c_1^2-c_1c_3+c_3^2)/(3c_1)$, $c_4=-c_3^2/c_1$, leaving "The only free parameters in Einstein-\AE ther theory are then $c_\pm\equiv c_1\pm c_3$."

BBN for æther (§II, following the bounds): "once Eqs.~\eqref{eq:Aecons} and~\eqref{eq:Aecons2} are satisfied, $G_N \approx G_C$ up to terms of ${\cal{O}}(10^{-4})$, and thus, **cosmological observations do not significantly reduce the viable region defined by Eqs.~\eqref{cp_constraint} and~\eqref{cm_constraint}**."

### How it is drawn / whether the combined region includes it
- Fig. 7 (§VII C.1, L3116): "**The area below and to the right of the solid black line is the allowed $(c_{+},c_{-})$ region after imposing Cherenkov and stability constraints.**" Caption (L3124): "For comparison, we also plot the allowed $(c_{+},c_{-})$ region after imposing Cherenkov and stability constraints (below and to the right of the solid black line)". The line is plotted **for comparison** in each panel; the green pulsar bands are described separately.
- Fig. 1 (caption L430): the shaded areas are partitioned by which set rules them out — "The areas **outside** the (allowed) shaded regions are ruled out by stability/Cherenkov considerations (light blue), BBN (dark orange) and the combined binary pulsar constraints (dark purple)" — and the Executive Summary (L445–L447) describes the coloured regions as "those allowed **after requiring** stability and absence of gravitational Cherenkov radiation (light blue), BBN constraints (dark orange) and binary pulsar constraints (dark purple)".
- The "almost a box" passage (L3137) defines the box as the **intersection of the per-system pulsar
  allowed regions only** ("when we combine all of these allowed regions … their intersection is
  indeed almost a box"); it does not state that the box is additionally intersected with the
  Cherenkov/stability (or BBN) set. Whether the final physically-allowed set is the box ∩
  Cherenkov/stability region is therefore **not stated in that passage**; Fig. 1's caption/summary
  language ("allowed after requiring …") presents all three requirements as simultaneously imposed
  on the figure as a whole, without an explicit set-intersection formula.
- Khronometric analogue for completeness: stability/Cherenkov conditions are Eqs. `con1`–`con3`
  (L819–L822), e.g. `0<\beta<1/3, \quad \lambda > \frac{\beta (\beta+1)}{1-3\beta}` etc., and in
  Fig. `fig:Pdot-HL` the allowed side is "above and to the left of the solid black line" (L3146, L3155).

---

## Explicitly unanswerable from the tex
1. **Axis ranges** of Fig. 7 / Fig. 1 — absent from the tex; values in §4 come from the figure PDFs.
2. **How $\sigma$ is evaluated inside Eq. (191) for the Fig. 7 bands** (TOV point-by-point vs `s-fit`
   vs other) — no sentence in §VII states it (§3 above).
3. **Formal quantifier** for the shading (existential vs otherwise) — only the "search for the region
   where … is satisfied, with … evaluated within / allowing for / trying different values" wording (§3).
4. **Any $c_-$ statement at $c_-\sim0.1$–$0.2$ or explicit pulsar $c_-$ upper bound** — none exists in the tex (§5).
5. Printed equation numbers — the tex source carries labels only; the (188)–(195) mapping in §1 is by sequence/content.
