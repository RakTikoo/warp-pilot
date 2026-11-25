# Gate-14 novelty audit — search log (2026-11-23)

Claim scoped for the audit (the programme's claim is ONLY this):
the ACCOUNTING RESULT on the Xun & Ren N-qubit QET model
(arXiv:2410.04919) — under the inherited Phase 72/106 accounting
(receiving sector = output qubits' H_i + V; resource = the sector's
energy in the marginal-product/uncorrelated reference,
E_prep^(marg) = 4k^2/D; net E_net,B = E_prep^(marg) - E_out;
Ford-Roman ratio R = |E_net,B| * tau / (3/(32 pi^2))), the receiving
sector delivers NET NEGATIVE energy (E_net,B < 0) at eight rows,
first at (N,m) = (5,1), with R > 1 at the deciding rows — i.e. the
extracted energy exceeds the correlation (preparation) energy of
the sector's own uncorrelated reference, with the entanglement
resource fully counted. The MODEL is Xun & Ren's; no priority over
the model is claimed.

## Sources and queries (verbatim)

1. arXiv abstract + full-text HTML of the source paper itself:
   https://arxiv.org/abs/2410.04919 and https://arxiv.org/html/2410.04919v1
   — the paper's own framing is transfer efficiency eta = E_out/E_in
   and its correlation with ground-state entanglement. It contains
   no uncorrelated-reference netting, no E_prep^(marg) comparison,
   and no Ford-Roman ratio.
2. Semantic Scholar citation graph:
   GET https://api.semanticscholar.org/graph/v1/paper/arXiv:2410.04919/citations?fields=title,year,externalIds&limit=100
   — returned {"offset": 0, "data": []}: ZERO citing papers indexed.
3. INSPIRE-HEP record: https://inspirehep.net/api/arxiv/2410.04919
   — "citation_count": 0, "citation_count_without_self_citations": 0.
4. Web search: "Xun Ren multipartite quantum energy teleportation
   negative energy accounting"
5. Web search: "\"quantum energy teleportation\" Ford-Roman bound
   net negative energy preparation cost counted"
6. Web search: "\"2410.04919\" OR \"multipartite\" Xun Ren quantum
   energy teleportation cited"
7. Web search: "quantum energy teleportation \"net\" negative energy
   \"uncorrelated\" OR \"marginal\" reference preparation energy sector"
8. Web search: "\"energy teleportation\" N-qubit extracted energy
   exceeds correlation energy ground state net sector negative"

## Near neighbours found (none carries the claimed result)

- Hotta, QET foundations (e.g. arXiv:0803.0348; arXiv:0911.3430):
  negative energy density is defined relative to the ENTANGLED
  GROUND state's zero; the resource is not netted against an
  uncorrelated (marginal-product) reference, and no Ford-Roman
  net ratio is computed for a multipartite spin model.
- Funai & Martin-Martinez, Phys. Rev. D 96, 025014 (2017)
  (arXiv:1701.03805): field/detector QET engineered to saturate
  the quantum-interest conjecture — a different model class
  (Unruh-DeWitt detectors + field); its accounting is the field
  protocol's stress-energy, not the marginal-product netting on
  the Xun-Ren spin model.
- Ragula & Martin-Martinez, review of QET applications
  (arXiv:2505.04689): surveys negative stress-energy engineering
  via QET; contains no net-of-preparation accounting result for
  the Xun-Ren model.
- Ikeda, Phys. Rev. D 114, 045016 (2026): QET across lattice and
  continuum (Thirring/sine-Gordon) — different model, different
  question (lattice-continuum correspondence).

## Coverage gaps (stated)

- English-language sources only.
- No direct Google Scholar query (not exposed to this tooling);
  general web search used instead, which indexes Scholar partially.
- Subscription literature checked at abstract level only.
- Citation indexes (Semantic Scholar, INSPIRE-HEP) read on
  2026-11-23; both may lag, but with zero citations in both, no
  citing work can carry the result as of the check date.
- The source paper's full text was read via the arXiv HTML; its
  appendices' sector-energy pattern (the origin of the 4k^2/D
  sector form) is part of the model, not of the accounting claim.

## Grade

NOVEL — the accounting result as scoped above was not found in
any published source searched; the model it is computed on is
Xun & Ren's (arXiv:2410.04919) and is cited as theirs.
