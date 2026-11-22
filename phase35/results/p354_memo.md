# P35-4 — ξφ²T scalar–torsion (NEW THEORY) — memo

Worker P35-4, Phase 35. Script: `phase35/p354_scalar_torsion.py`
(sympy symbolic limits + float64 numerics). Results:
`phase35/results/p354_results.json`. CHECKPOINT35.md not edited.

## Verdict: **IDENTITY BREAKS — DECOUPLING ONLY**

- **Identity breaks, by:** the ρ-equation's S·∂F term,
  $D_\rho=\lim_{r\to r_0}\frac{s(1-s)}{r}F'=\dfrac{2\xi\,\varphi(r_0)\,L}{r_0}$,
  $L:=\lim s\,\varphi'(r)$ ($s=\sqrt{1-r_0^2/r^2}$, $r_0=1$ in the run),
  finite and generically nonzero on the scalar's own EoM solutions.
  The throat totals become
  $4\pi\rho_{\rm tot}(r_0)=-F(r_0)/2+D_\rho$ and
  $4\pi(\rho+p_r)_{\rm tot}(r_0)=-F(r_0)+D_\rho$
  (and $D_{p_t}=-D_\rho/2$ in the $p_t$ equation) — not the P33-4 totals.
- **Legality+health side still fails, independently, by:** the
  $p_r$ equation. BHL Eq. (14) contains **no** derivative term at any
  $r$, so $4\pi p_r(r_0)=-F(r_0)/2$ exactly, while a canonical scalar
  supplies $4\pi p_{r,\varphi}(r_0)=4\pi(K_0+V_0)\ge 0$. Health
  ($F(r_0)>0$) demands $p_r(r_0)<0$ — impossible for every grid row,
  every throat datum. The two sides now fail independently: that is
  decoupling without a pass.

## Conventions and background (run record, stated before solving)

Theory (fixed): $f(T,\varphi)=-(1-\xi\varphi^2)T$, i.e.
$F(\varphi):=\partial f/\partial T=-(1-\xi\varphi^2)=\xi\varphi^2-1$,
canonical scalar, $V\in\{0,\tfrac12 m^2\varphi^2,\ mr_0=1\}$,
$\xi\in\{0.1,0.5,1,2,5\}$. Matter in the 4π units of the P33-4
record; $r_0=1$. Background: T≡0 BHL Ellis family, tetrad of record
(`phase20/p202b_ft.py`; BHL arXiv:1110.5756 off-diagonal tetrad),
$\beta=r_0^2/r$, $e^{a}=(1+s)/2$; T≡0 re-verified symbolically in-run
($T$ simplifies to 0 exactly). **Background note:** with this tetrad
T≡0 *forces* $a'(r)=(s-1)/r\neq0$ (BHL Eq. (25)); a literal
$\Phi\equiv0$ ($a=0$) background has $T\neq0$ and is outside the
registered T≡0 class — the checkpoint's "Φ = 0" is read as the
Gate-5/P20-2 background of record, which is the one used here.

**GATE (ξ = 0): PASSED.** $F=-1$: tensor kinetic ratio −1.0,
$c_T^2=1$, $D_\rho=0$, throat totals $4\pi\rho_{\rm tot}=+0.500$,
$4\pi(\rho+p_r)_{\rm tot}=+1.000$ — Gate-5 G5-1 / P33-4 exactly.

## Screen — C1–C12 clause by clause (before scan budget)

- **C1 (relocation identity) — DECIDING, outcome split.** The
  ρ/NEC1 relocation identity does **not** survive: $D_\rho\neq0$
  moves both totals (below). But a *new* lock appears in its place
  in the $p_r$ channel (no ∂F term there), so the item's question
  is answered "identity breaks, pass does not follow."
- **C2 (same-sign-jump identity):** not applicable — no shell/jump
  in this item; nothing in the derivation is a sum of same-sign roots.
- **C3 (protected cancellation):** checked, does not occur. The
  naive cancellation ($s\to0$ kills the S·∂F coefficient) is only
  apparent: a throat-regular scalar has $\varphi'\sim L/s$, so
  $sF'\to2\xi\varphi_0L\neq0$. Numeric limit check in the JSON:
  Eq. (13) coefficient → 1.820 vs exact $D_\rho=1.820$; Eq. (15)
  coefficient → −0.910 vs exact $-D_\rho/2=-0.910$ (test values
  $\xi=0.7,\ \varphi=1.3,\ L=1$, algebra check only).
- **C4 (rank + direction):** not deciding — this is a theory test
  on a fixed throat background, not a wall-supply construction;
  no direction field is asked to be sustained.
- **C5 (simultaneity) — DECIDING.** The configuration test is
  exactly a simultaneity test (EoM + conservation + full EC +
  throat algebra + tensor health, jointly). It fails jointly at
  the throat $p_r$ equation; no sector is designer-sustained —
  the scalar profiles exhibited are EoM solutions (flux family /
  IVP), not prescribed stress-energy.
- **C6 (screening without leaks / data):** not deciding at this
  gate. ξ is an always-on coupling, but on the T≡0 background its
  only background-level lever is through $F(\varphi(r))$; no
  solar-system/PPN read is registered for this item and none is
  claimed. Flagged for any next gate: an O(1) ξ with
  $\varphi\sim\xi^{-1/2}$ cosmologically would need a data audit.
- **C7 (full-EC + conservation decide) — DECIDING (with C5).**
  NEC1 alone *can* now be made positive on the healthy branch
  (that is the decoupling); the kill comes from the full system —
  the $p_r$ field equation against the scalar's $p_{r,\varphi}
  =K+V\ge0$ — with conservation holding on-background (coupling
  force $\propto T\,\partial\varphi=0$).
- **C8 (auxiliary non-degeneracy):** not applicable — no auxiliary
  metric / no $f_R$-type factor; $F(r_0)=0$ is the marginal row and
  is reported as zero kinetic coefficient (strong-coupling point),
  not counted as healthy.
- **C9 ($T^t{}_t=T^r{}_r$ identity):** not the mechanism here.
  The scalar has $\rho_\varphi-p_{r,\varphi}=-2V$; for $V=0$,
  $p_{r,\varphi}=\rho_\varphi=K$, and it is precisely this
  non-negative $p_r$ that the un-shifted Eq. (14) cannot accept
  on the healthy branch.
- **C10 (scalar ghost lock) — scoped.** The scalar itself is
  canonical: no scalar-sector ghost for any grid row, and C10's
  hybrid-Palatini lock (kinetic sign tied to the NEC-buying
  field value) does not apply to the scalar sector. What C10
  does **not** cover is the *effective tensor* coefficient
  $F(\varphi(r))$, which is field-dependent here: its sign at
  the throat is $\mathrm{sgn}(\xi\varphi_0^2-1)$, a background
  datum, not a scalar-kinetic sign. The ghost question migrates
  to the tensor sector and is answered in Computation (1).
- **C11 (anti-scaling / windows):** noted, not deciding.
  $D_\rho\propto\sqrt{K_0}$ grows sublinearly against demands
  $\propto\xi\varphi_0^2$; and the $p_r$ obstruction is
  scale-free (a sign, at every $r_0$). No observational window
  is invoked.
- **C12 (fronts / setup accounting):** no superluminal claim;
  $c_T^2=1$ exactly wherever $F\neq0$ (kinetic = gradient
  coefficient, both $F(r)$). The throat is static and
  pre-existing; no formation/transport claim.

No clause kills the item on paper: C1's question is genuinely
open until the ∂F limits are computed, so the scan budget was spent.

## Computation (1) — tensor sector, from the action

For TT perturbations $\delta_1T=0$ (Gate-5's result, structural:
$T$'s linear variation is a scalar-sector quantity), and
$\delta\varphi$ is a scalar-sector perturbation that cannot mix
with TT modes at quadratic order on a spherical background.
$F$ depends on $\varphi$ *algebraically* (no derivatives), so
expanding $e\,F(\varphi)T$ to quadratic order in tensor modes
gives, pointwise in $r$,

$$S^{(2)}_{\rm tensor}=F(\varphi_{\rm bg}(r))\times
S^{(2)}_{\rm tensor,TEGR},\qquad
F(r)=-(1-\xi\varphi(r)^2).$$

Yes — the kinetic coefficient **is** $-(1-\xi\varphi(r)^2)$
evaluated on the background profile: a position-dependent
kinetic (and gradient) coefficient, $c_T^2=1$ wherever
$F\neq0$. Sign at the throat: healthy iff
$F(r_0)=\xi\varphi_0^2-1>0$, i.e. $\xi\varphi_0^2>1$ — a
condition on throat data, satisfiable in principle (the
exhibits below use $\varphi_0=2/\sqrt\xi$, $F(r_0)=+3$ for
every ξ). The tensor sector alone no longer locks legality:
that lock is what Computation (2) re-examines.

## Computation (2) — throat algebra with F′ ≠ 0

BHL's Eq. (9) carries $S_i{}^{\mu\nu}\partial_\mu f_T$; for
$f(T,\varphi)$ on a T≡0 background,
$\partial_r f_T=f_{T\varphi}\varphi'=F'=2\xi\varphi\varphi'$.
Substituting $T'f_{TT}\to F'$, $f\to0$, $f_T\to F(r)$ in BHL
Eqs. (13)–(15), and taking $r\to r_0$ (sympy limits in-run;
the $e^{-b}(rb'-1)$ limit is $-2$, giving the familiar $-F/2$):

$$4\pi\rho_{\rm tot}(r_0)=-\frac{F(r_0)}{2}+D_\rho,\qquad
4\pi p_{r,\rm tot}(r_0)=-\frac{F(r_0)}{2},\qquad
4\pi p_{t,\rm tot}(r_0)=\frac{3}{8}F(r_0)-\frac{D_\rho}{2},$$

$$D_\rho=\frac{2\xi\,\varphi_0\,L}{r_0},\qquad
L=\lim_{r\to r_0}s\,\varphi'(r),\qquad
4\pi(\rho+p_r)_{\rm tot}(r_0)=-F(r_0)+D_\rho .$$

**Exactly which term breaks the identity:** the Eq. (13)
$S\cdot\partial F$ term $\frac{s(1-s)}{r}F'$. Its coefficient
vanishes like $s$, but the scalar EoM
$(e^{(a-b)/2}r^2\varphi')'=e^{(a+b)/2}r^2V'(\varphi)$ (the
$\xi\varphi T$ force vanishes on the T≡0 background) makes
$\varphi'\sim L/s$ with $L=J_0/(e^{a_0/2}r_0^2)$ the throat
flux — finite, and $L\neq0$ for any flux-carrying solution —
so the product has the finite nonzero limit above. If
$L=0$ (zero throat flux), $D_\rho=0$ and the P33-4 identity
is restored verbatim with $F(r_0)$ in place of $f_T(0)$:
the breaking is carried entirely by throat-flux
configurations. Eq. (14) has no such term at all — the
asymmetry between the ρ and $p_r$ equations is the whole story.

## Computation (3) — configuration test

Scalar throat data: $K_0=\tfrac12L^2\ge0$, $V_0\in\{0,\varphi_0^2/2\}$,
$\rho_\varphi=K_0-V_0$, $p_{r,\varphi}=K_0+V_0$,
$p_{t,\varphi}=V_0-K_0$ (P33-4 audit; EC-legal iff the usual
canonical conditions, DEC saturated at $V=0$). Throat algebra
for the scalar as the *only* matter requires simultaneously

$$\text{(A)}\quad 4\pi(K_0+V_0)=-\frac{F(r_0)}{2},
\qquad
\text{(B)}\quad 4\pi(K_0-V_0)=-\frac{F(r_0)}{2}+D_\rho .$$

(A) alone decides it: LHS $\ge0$ always; RHS $<0$ iff
$F(r_0)>0$. **No grid row — indeed no $(\xi,V,\varphi_0,K_0,
\mathrm{sgn}\,L)$ at all — admits a throat configuration with
throat algebra satisfied and tensor coefficient $>0$.** The
fine scan in the script (φ₀ ∈ [0,6], √K₀ ∈ [0,4], all 10
(ξ, V) rows) finds 0 healthy solutions; the Eq. (A) residual
is $\ge F(r_0)/2$ for every healthy row, vanishing only at
the marginal $F(r_0)=0$, where (A) forces $K_0=V_0=0$ and
the tensor coefficient is zero, not healthy. Shortfall,
named: on the exhibits below the geometry demands
$4\pi p_r(r_0)=-1.500$ while the scalar supplies
$4\pi p_{r,\varphi}(r_0)=+6.283$ ($K_0=\tfrac12$, $V=0$) —
a shortfall of $7.783$ in 4π units, in the $p_r$ channel,
which no legal scalar data can close because
$p_{r,\varphi}\ge0$ identically. No second component was
added; per registration a row needing one would not count,
and none is needed to reach this verdict.

**Decoupling exhibits (the identity really does break).**
Exact EoM solutions, $V=0$ flux family (flux
$J=1/\sqrt2=\,$const is the integrated EoM; in proper-length
coordinate $l$, $K=\tfrac12(d\varphi/dl)^2$, regular at the
throat, $\varphi$ finite at infinity, EC-legal everywhere:
$\rho=K\ge0$, NEC1 $=2K$, NEC2 $=0$, DEC saturated), with
$\varphi_0=2/\sqrt\xi$ ($F(r_0)=+3$, tensor-healthy),
$L=1$, $K_0=\tfrac12$:

| ξ | $D_\rho$ (4π) | $4\pi\rho$ demanded | P33-4 identity would give | $4\pi$NEC1 demanded | identity would give |
|---|---|---|---|---|---|
| 0.1 | 1.265 | −0.235 | −1.500 | −1.735 | −3.000 |
| 0.5 | 2.828 | +1.328 | −1.500 | −0.172 | −3.000 |
| 1 | 4.000 | +2.500 | −1.500 | +1.000 | −3.000 |
| 2 | 5.657 | +4.157 | −1.500 | +2.657 | −3.000 |
| 5 | 8.944 | +7.444 | −1.500 | +5.944 | −3.000 |

For ξ ≥ 0.5 even the demanded ρ is positive on a
tensor-healthy row, and for ξ ≥ 1 the demanded NEC1 is too —
the totals identity is genuinely gone. Every one of these
rows still fails (A): demanded $4\pi p_r=-1.500$ vs scalar
$\ge0$. Massive-$V$ local EoM solutions (IVP in $l$ from the
same throat data) have the identical $D_\rho$ at the throat;
their global EC is not needed, since (A) is algebraic and
covers the massive rows directly ($V_0=\varphi_0^2/2$ only
raises the LHS of (A)).

## Scope of the verdict (exact)

The G5-1/P33-4 identity, as an identity on the *totals*
$4\pi\rho_{\rm tot}(r_0)=-f_T(0)/2$,
$4\pi(\rho+p_r)_{\rm tot}(r_0)=-f_T(0)$, **ends at
non-minimal coupling**, as registered — but only for
throat-flux configurations ($L\neq0$); at $L=0$ it survives
with $F(r_0)$ substituted. The legality⟺ghost *conclusion*
nevertheless survives on this background for this theory,
via a different, narrower mechanism: the derivative-free
$p_r$ equation (BHL Eq. (14)) plus $p_{r,\varphi}=K+V\ge0$
for a canonical scalar. That mechanism is specific to
(i) couplings whose $f$ is linear in $T$ with
$\varphi$-dependent coefficient (so Eq. (14) acquires no
∂F term), and (ii) matter with $p_r\ge0$ at the throat.
It is a scan-level result for the next gate, not a
candidate; the row carries no FTL/transport claim.

## Follow-up experiments (Failure Protocol, ≥1)

1. **Derivative torsion coupling (aimed at the deciding
   term):** add a coupling that *does* enter Eq. (14) —
   e.g. $\varphi\,T$ with a derivative structure, or
   $f(T,\varphi)$ nonlinear in $T$ ($f_{TT}\neq0$ with
   $T'\neq0$ off the T≡0 class), and compute whether the
   $p_r$ throat equation acquires a ∂F-type term with a
   coefficient whose throat limit is finite against the
   same $L$. The anatomy says the pass, if any, lives
   exactly there: a theory whose Eq. (14)-analogue is
   shifted by $\sim\xi\varphi_0L/r_0$ reopens (A).
2. **Non-canonical scalar sign check:** a scalar with
   $p_{r,\varphi}$ able to go negative at the throat while
   EC-legal elsewhere (e.g. a potential-dominated throat
   datum in a theory where (B) can offset it) — test
   whether (A)+(B) jointly admit $F(r_0)>0$ for *any*
   $(K_0,V_0)$ once $p_{r,\varphi}=K_0+V_0$ is replaced by
   the non-canonical relation; the algebra above shows
   canonical $K+V\ge0$ is the load-bearing assumption.
3. **$L=0$ sector audit:** zero-flux configurations restore
   the totals identity with $F(r_0)$ — verify the scalar/
   Lorentz-sector health at $F(r_0)<0$, $L=0$ is exactly the
   standing P20-2 (F-b) $f_{TT}$ obstruction transplanted,
   or whether the φ-dependence fixes what pure $f(T)$ left
   free.
