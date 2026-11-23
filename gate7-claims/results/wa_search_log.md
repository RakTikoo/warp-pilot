# G7-1 novelty search log — W-A (2026-11-22)

Question searched: does the Fuchs-family / warp-shell literature state
that reducing profile smoothing width raises the EC-legal β ceiling,
or report a smoothing-width scan at all?

All searches run 2026-11-22 via the browser search tool (general web
index) unless a page open is noted. Queries verbatim:

1. `warp drive shell smoothing width energy conditions Fuchs positive energy warp shell smoothing`
   Sources returned/checked: Le arXiv:2605.25417 (abstract), Procaccia
   certificates paper (academia.edu), Fuchs et al. IOP page
   (DOI 10.1088/1361-6382/ad26aa), Le "Steering a warp drive"
   arXiv:2606.22531. No smoothing-width scan in any.
2. `"smoothing" warp shell "energy conditions" shift profile velocity ceiling beta`
   Sources: Procaccia certificates (academia.edu), Le arXiv:2605.25417
   (abstract + overfitted.cloud full-text mirror), Rodal Springer paper
   (DOI 10.1007/s10714-025-03495-x; its Appendix D holds smoothing FIXED
   for a vorticity ablation — the opposite design: smoothing is the
   controlled variable, not the scanned one).
3. `arXiv 2405.02709 Fuchs warp drive shell smoothing moving average density profile`
   Sources: Fuchs et al. arXiv HTML full text (opened and read, see
   below), IOP page. 
4. `"Gaussian smoothing" warp drive shell density pressure profile`
   Sources: Warp Factory arXiv:2404.03095, Rodal Springer paper,
   Sherrington "Irrotational Warp Metrics" (Zenodo, Jan 2026 — scans
   wall sharpness σ, velocity v, radius ρ for NEGATIVE-energy
   requirements of Alcubierre-class irrotational metrics; not a
   Fuchs-family shell, not an EC-legal ceiling).
5. `INSPIRE-HEP Fuchs constant velocity physical warp drive smoothing parameter scan velocity`
   Sources: Fuchs full text (archive.org PDF extract), IOP, Warp
   Factory arXiv:2404.03095. (See gap note: INSPIRE's own interface
   was not queried directly.)
6. `Semantic Scholar warp drive shell thickness smoothing width maximum velocity energy conditions study`
   Sources: Pfenning & Ford gr-qc/9702026, Jusufi & Lobo
   arXiv:2609.05554, theses/NTRS. Nothing on Fuchs-family smoothing
   width. (See gap note.)
7. `Procaccia optimized positive-energy warp shell box convolution width smoothing scan shift amplitude`
   Sources: Procaccia certificates paper (academia.edu, read in
   extract), Le arXiv:2605.25417. Procaccia's smoothing is a FIXED
   4× box convolution (W = 3.6328174 m); his scanned/optimised
   variable is the shift source, not the smoothing width.
8. `inspirehep.net "Constant velocity physical warp drive" Fuchs smoothing`
   Sources: Fuchs full text, secondary reviews. No scan.
9. `semanticscholar.org warp drive Fuchs shell smoothing fsmooth density pressure iteration`
   Sources: Le papers, Rodal. No scan. (See gap note.)
10. `"wall thickness" OR "wall sharpness" warp drive energy condition violations parameter scan sigma Alcubierre`
    Sources: Pfenning & Ford (gr-qc/9702026; wall thickness bounded by
    quantum inequalities for the Alcubierre metric), Le warpax
    arXiv:2602.18023 (ablation sweeps incl. wall thickness σ for
    Rodal/Alcubierre-class metrics), White "Warp Field Mechanics 101"
    (thicker Alcubierre walls reduce peak negative density). All
    Alcubierre-class: sharpness there controls NEGATIVE-energy
    magnitude, in the opposite spirit, and none concerns a
    positive-energy shell's legal-β ceiling.

Primary-source read (opened in full): Fuchs et al. 2024,
arXiv:2405.02709 (HTML v1), §3–§4 and §6. What it actually says
about smoothing: density/pressure discontinuities are softened by a
moving-average f_smooth; "Selecting the smoothing function
coefficients is found iteratively until the solution has no
violations of the Null, Weak, Dominant, and Strong energy
conditions"; span ratio s_ρ/s_P ≈ 1.72 "found by trial and error",
moving average applied four times; the warp design is reported at
β_warp = 0.02 ("likely not an upper limit as optimizations could be
considered"); §6 outlook: "The metric construction process of
smoothing can be replaced by a direct 1D optimization of the radial
profiles … possibly reducing required mass." No smoothing-width
values scanned against velocity; no statement that narrower
smoothing raises (or lowers) a legal-β ceiling; smoothing is tuned
once, at fixed design/velocity, to remove boundary violations.

Le arXiv:2605.25417 (abstract + full-text mirror read): reproduces
the Fuchs construction "via iterative Gaussian-kernel smoothing",
finds Hawking–Ellis Type-IV violations in the smoothing TAIL, and
scans compactness and THICKNESS (600 configurations) for his own
source-first S/T shells — thickness of the shell, not the smoothing
width of a Fuchs-family profile, and no β-ceiling-vs-smoothing
statement.

COVERAGE GAPS (stated plainly):
- INSPIRE-HEP was NOT queried through its own search interface in
  this session; it was reached only via general web search and via
  the index links listed on arXiv abstract pages. A record indexed
  only in INSPIRE could have been missed.
- Semantic Scholar was NOT queried through its own search interface
  either; same route as INSPIRE (general web search + arXiv-page
  index links only). A record indexed only there could have been
  missed.
- Procaccia's companion optimisation paper full text was not
  retrieved (abstract + code archives were, in Phase 50); the
  certificates paper was read via the academia.edu page extract.
  A smoothing-width discussion appearing only in the companion
  paper's full text would be missed by this search.
These are gaps, not negative results.
