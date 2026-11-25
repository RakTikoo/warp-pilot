# P108-5 evaluation definitions — fixed BEFORE any tau computation
Candidate: Xun & Ren, arXiv:2410.04919 (N-qubit QET, Eqs.1-14 + App.A/B).
Accounting: inherited verbatim from P72-2 run record / P106-3.
- h=1, r=k/h in {0.5,1,2}. Configs: (N,m) in {(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(10,1)}; N=2,m=1 control vs P72-2.
- Delivered E_B := E_out of the paper (sector = output qubits' H_i + V, paper Eqs.28/39 pattern).
- E_prep^(marg) := sector energy of marginal-product state (product of |g>'s single-qubit marginals) above ground sector value = 4k^2/D, D=sqrt(N^2 h^2+4k^2) (closed form; matrix-verified).
- E_net,B = E_prep^(marg) - E_out. R_net = 0 iff E_net,B >= 0.
- If E_net,B < 0: FR-net ratio per P72-2 S4 "same read with resource on books":
  primary R_net = (E_out - E_prep^(marg)) * tau_marg / (3/(32 pi^2)), tau_marg = first t>0 at which sector energy S(t)=<sector>(t) under H-evolution of post-protocol state returns to the marginal-reference level (+E_prep^(marg)).
  Conservative companion R_tau0 uses tau_0 = first return of S(t) to ground zero (P72-2's literal tau_pulse). Both reported; a bar claim requires the conservative one > 1 as well, or is flagged convention-sensitive.
- E_in (paper Eq.6) and price line (E_prep+E_in)/E_out also reported. Classical leg >= 0 omitted (lower bound).
- Second path: independent dense-matrix simulation (Kronecker construction), must agree on E_out, E_prep, tau.
