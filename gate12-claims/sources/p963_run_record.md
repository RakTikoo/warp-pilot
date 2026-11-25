# P96-3 RUN RECORD — FU-P883-1/2/3
## Written BEFORE any Phase-96 P96-3 eigenvalue or deciding number was
## computed (the K-geometry exploration values in §3 are background
## geometry at Sigma, quoted as pose inputs, not eigenvalues).
## Searches in §2 were logged before the poses in §§3-5 were fixed.

Worker P96-3, Phase 96. Parent registration: CHECKPOINT96.md §P96-3
(binding, incl. verdict forms). Grounding read in full before this
file: CHECKPOINT96 §P96-3; p883_memo.md; p883_run_record.md;
p883_results.json; p883_compute.py; CHECKPOINT61 §P61-1 + closure;
p711_memo.md (P71-1 interior quotient machinery); p802_memo.md
(P80-2 exterior quotient machinery + shell counting).

LANGUAGE LOCK: throat OBJECT only. The word "traversable" appears
only in negations. No statement in this item is a traversability
claim, and nothing here makes the object traversable.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**
(V-b) rides verbatim on every statement this item produces.
INTERNAL only; nothing uploaded; nobody contacted. float64 (venv
python); 40-digit mpmath probes where Phase 88 used them.
phase88/, phase80/, phase61/ READ-ONLY; CHECKPOINT96.md not edited.

## 1. The object (fixed)

Joining member (p = 0.1, Phi2 profile, stored full-precision
a = 0.27773424114865775 — never the rounded 0.277734), joined at
r_Sigma = 1,000 r0 to the registered-gamma MK exterior
(beta_MK = 2.142611 r0, k = -2.28996e-9 r0^-2, gamma = 1e-28 per r0);
shell datum sigma0 = S0^0 = +0.02029144078829105 alpha0 (legal);
[Rtilde] = 0 and [Rtilde_,n] = -0.015218580591218289 at Sigma
(stored P61-1/P80-2, re-gated in-item by the Phase-88 pattern).
Interior stable (P71-1), exterior stable (P80-2); shell sector
UNPOSABLE UPGRADED in pure Weyl gravity (P88-3). Fixed-bulk slopes
(P88-3, re-used as pose inputs): D_R = -1.5233785879e-5,
D_Rn = +1.8844230756e-5.
**(V-b) UNDECIDED: Pais–Uhlenbeck spin-2 ghost vs Mannheim PT-symmetric quantisation — opposed literature positions, B3 NOT COMPUTABLE (Phase 32).**

## 2. SOURCE LOG — every query verbatim, logged BEFORE computing

P96-3(a) action search (2026-11-22, web search, in order):
 A1 "thin shell matter action variation surface perfect fluid relativistic elastic shell action"
 A2 "relativistic elastic thin shell action Carter Quintana surface stress energy variation"
 A3 "\"thin shell\" action \"-m\" integral proper time spherical shell Lagrangian equation of motion"
 A4 "\"elastic shell\" general relativity action strain energy surface elasticity equation motion"
 A5 "\"surface action\" shell matter \"sqrt\" induced metric perfect fluid Brown action shell"
 A6 "Berezin Dokuchaev Eroshenko conformal gravity shell action matter surface action variation"
Full text retrieved: Gladush, arXiv:gr-qc/0312067 (variational
principle and effective action for a spherical dust shell), §II,
eqs. (2.21)-(2.24). Also identified: Kijowski-Magli-Malafarina,
Phys. Rev. D 74 (2006) 084017 (variational principle for a
spherical shell of an arbitrary ideal fluid; Lagrangian derived
from first principles); Brown, Class. Quantum Grav. 10 (1993)
1579 (action functionals for relativistic perfect fluids:
matter Lagrangian density -epsilon(n) with n the particle
density, pressure p = n d(epsilon)/dn - epsilon).

P96-3(c) Route-2 reopening search (2026-11-22, web search, in
order; the six Phase-88 candidates are NOT re-run):
 C1 "conformal Weyl gravity junction regularity condition scalar invariant continuous thin shell"
 C2 "Mannheim Kazanas conformal gravity thin shell junction conditions regularity"
 C3 "Rosa junction conditions scalar degrees freedom Weyl squared gravity thin shell double layer"
 C4 "\"Weyl tensor\" junction conditions continuity Bach tensor thin shell quadratic gravity"
 C5 "\"conformal gravity\" \"junction conditions\" shell surface stress determined"
 C6 "Deruelle Sasaki Sendouda quadratic gravity junction Weyl Gauss-Bonnet thin shell regularity Ricci"
Sources named from these queries: Rosa, arXiv:2311.11752 /
Phys. Rev. D 109 (2024) 064018 (junction conditions in theories
f(X1,...,Xn) of scalar invariants); Rosa, arXiv:2103.11698
(junction conditions and thin shells in perfect-fluid f(R,T)
gravity — junction conditions force the radiation equation of
state sigma = 2 p_t); Deruelle-Germani-Kaneda / generalised
Darmois-Israel for higher-derivative gravity, Universe 8 (2022)
250 (regularisation of quadratic gravity, F(R), Euler densities);
Grumiller-Irakleidou-Lovrekovic-McNees, arXiv:1310.0819
(conformal gravity holography: (A)dS boundary conditions for
conformal gravity, weaker than Starobinsky, admitting the
Mannheim-Kazanas-Riegert solution); Kiefer-Nikolic,
arXiv:1702.04973 (conformal and Weyl-Einstein gravity: canonical
formulation with Einstein-Hilbert term + nonminimal scalar).

## 3. P96-3(a) — CHOSEN ACTION, POSE (before any eigenvalue)

CHOSEN ACTION (the registration's class: a surface perfect-fluid
action whose variation gives a genuine xi-double-dot equation).
The shell matter action is the Brown/Gladush surface-fluid
action restricted to the shell worldvolume Sigma:
  S_shell = - INT_Sigma epsilon(n_s) sqrt(-gamma) d^3y ,
where gamma is the determinant of the induced metric on Sigma,
n_s is the surface particle density, and epsilon(n_s) is the
surface energy density function of the fluid. Gladush's dust
case of exactly this action is quoted verbatim from the
retrieved source (arXiv:gr-qc/0312067, eq. (2.23)): "The dust on
the singular shell Sigma is described by the action
  I_m = c INT_Sigma sigma sqrt(-g) dSigma_n ^ dtheta ^ dalpha"
with the total action (his eq. (2.21)) "I_tot = I_EH + I_m +
I_Sigma + I_{dD} + I_0". Brown's fluid form gives, for a general
epsilon(n_s): surface density sigma = epsilon(n_s), surface
pressure p = n_s epsilon'(n_s) - epsilon(n_s), and the
linearised response dp = beta^2 dsigma with
beta^2 := dp/dsigma at the background — beta^2 is a parameter
of THE ACTION (through epsilon''), not fitted to any spectrum.
The object of every (a) read is named, in every sentence:
"the P61-1 shell endowed with the Brown-Gladush surface
perfect-fluid action" (short label in tables: ENDOWED OBJECT).
It is NOT the conformal member; no (a) read revises the member's
standing. Background (bulks, r_Sigma, sigma0) = the P61-1 values.

POSE (a). Unknowns (l=0): xi(t) — normal displacement of Sigma,
R(t) = r_Sigma + xi(t); delta sigma, delta p_t; the bulk
perturbations delta g-/delta g+ are HELD FIXED in the sector
posed here (the fixed-bulk sector, the same sector P88-3 used
for its slope read; the coupled-bulk question is (b), separately).
Equations:
 (A-J2) [delta Rtilde] = D_R . xi at fixed bulks — a constraint
      the bulk system must absorb in the coupled problem; in the
      fixed-bulk sector it is recorded, not imposed on xi.
 (A-J3) read-off -[delta Rtilde_,n] = (3/(4 alpha0)) delta sigma
      at fixed bulks: delta sigma = -(4 alpha0/3) D_Rn xi.
      CROSS-CHECK registered: this must agree with the action's
      own conservation strain law (A-C1) — two expressions for
      delta sigma/xi from independent inputs (junction slopes vs
      fluid conservation); their agreement/disagreement is a
      deciding consistency number, computed before eigenvalues.
 (A-C1) worldvolume conservation of the endowed fluid (particle
      number N = 4 pi R^2 n_s conserved; sigma = epsilon(n_s)):
      delta sigma = -2 (sigma0 + p0) xi / r_Sigma, delta p_t =
      beta^2 delta sigma.
 (A-EOM) the action's normal equation of motion — the equation
      the member lacks and the action supplies. Normal variation
      of S_shell in vacuum (no bulk flux, [T_nn] = 0) gives
        S^{ab} Kbar_{ab} = 0 ,
      Kbar = (K+ + K-)/2 the averaged extrinsic curvature of
      Sigma, S^a_b = diag(-sigma, p_t, p_t). In components:
        -sigma . Kbar^t_t + 2 p_t . Kbar^theta_theta = 0 .
      Kbar^theta_theta contains no time derivative;
      Kbar^t_t contains d^2R/dtau^2 (tau = shell proper time)
      linearly, with a coefficient computed from BOTH bulk
      metrics at Sigma. This is a genuine xi-double-dot equation
      whenever sigma0 != 0 and that coefficient != 0.
BACKGROUND ADMISSIBILITY (deciding, before eigenvalues): the
P61-1 background is a static solution of the endowed object only
if (A-EOM) holds at xi = 0, i.e. only if the action's fluid has
background pressure p0 = sigma0 . Kbar^t_t(0) / (2 Kbar^theta_theta(0)).
This condition FIXES p0 as a property of the chosen action
(it is the endowed object's own background equation of state,
read off its action + the P61-1 geometry — not a fit to a
spectrum). The dust sub-case (p = 0, Gladush's literal action)
satisfies it only if Kbar^t_t(0) = 0; its residual is computed
and reported either way.
SECTORS CLOSED (stated as registered): l = 0 posed in full in
the fixed-bulk sector above. l >= 1 NOT closed: the
Brown-Gladush surface-fluid action as posed here is a spherical
(radial) fluid action — it supplies no tangential surface
displacement variable and no surface shear modulus, so the
non-spherical sectors of the endowed object are not posed by
this action. Stated before computing.
DECIDING NUMBERS (a): Kbar^t_t(0), Kbar^theta_theta(0) and their
radial derivatives at Sigma from both sides (sympy, float64 +
40-digit); the xi-double-dot coefficient C_avg in Kbar^t_t;
p0/sigma0 from admissibility; the (A-J3) vs (A-C1) strain
consistency ratio; then omega^2(beta^2) from linearising
(A-EOM), evaluated at the named action choices (i) the linear
equation of state p = w sigma with w = p0/sigma0 (so
beta^2 = w), and (ii) beta^2 = 0. Second path: finite-difference
extraction of every K quantity and of the xi-double-dot
coefficient from accelerated trial trajectories.

## 4. P96-3(b) — POSE (before any eigenvalue)

DATUM CHOICE (stated before computing, as registered): BOTH
registered datums are posed, in this order: (1) the traceless
datum (delta S2^2 = -delta S0^0/2; strain law delta S0^0 =
-sigma0 xi/r_Sigma); (2) the barotropic family (delta S2^2 =
beta0^2 delta S0^0; strain law delta S0^0 = -2(sigma0+p0)
xi/r_Sigma, (p0, beta0^2) unfitted family parameters). Every
(b) sentence names its datum.
POSE (b). Bulk systems: interior linearised Bach system on
[r0, r_Sigma] (P71-1 machinery: static l=0 exact sector +
dynamic l=0 Galerkin quotient, smallest physical eigenvalue
>= 0.00121741, no crossings) and exterior linearised Bach
system on [r_Sigma, r_Sigma + L] (P80-2 machinery: smallest
physical quotient eigenvalue >= 8.3166e-5, no crossings).
Boundary condition at r_Sigma, in the named datum's form: the
strain law above, with xi entering as the boundary value the
bulk system supplies, and delta S0^0 simultaneously DEFINED by
the read-off (J3) from the bulk jump: imposing the strain law
is therefore the single scalar condition
  -(4 alpha0/3) [delta Rtilde_,n]_Sigma =
      (strain coefficient) . xi ,
with the fixed-bulk slopes D_R, D_Rn of P88-3 giving the
geometric side. Matching: interior regularity/non-degeneracy
at the throat (P71-1's registered trial behaviour); exterior
patch behaviour as in P80-2 (no condition at infinity is part
of either registered machinery — both are finite-patch
quotient reads; stated as a scope fact of the pose).
EIGENVALUE UNKNOWNS + COUNT (registered): unknowns are
{delta g-, delta g+, xi, omega^2}. The bulk quotient systems
contribute, per side, a 2-dimensional physical quotient space
per trial profile (3 components minus the exact conformal null
direction, P71-1 §3 / P80-2 §3). The Sigma conditions available
are: perturbed Darmois (2 scalar conditions), [delta Rtilde]=0
(1), and the strain-law condition (1) — against which xi is
itself one NEW unknown function value. The deciding structural
question, registered before computing: does the strain-law
condition, net of the new unknown xi it introduces, impose ANY
constraint on omega^2 — i.e. is the coupled system's eigenvalue
selected at all? The count and a direct linear-algebra test on
the stored quotient blocks (does any stored quotient eigenvalue
move when the strain condition is adjoined as a row, with xi
as a free column?) are the deciding computations.

## 5. P96-3(c) — CONDITION AND TEST (before computing)

CONDITION (verbatim-in-substance from the P88-3 registration):
the shell sector's unposability reopens if a sourced model
keeps the PURE Weyl action and adds only a regularity condition
at Sigma on a bulk scalar/invariant not already continuous here,
yielding a determining equation for S2^2 (background value and
perturbation law) whose premises ALL hold for the P61-1 shell
as registered.
TEST: premise-check every NEW candidate from the §2 C-search,
one by one, against: (i) pure Weyl action kept; (ii) no double
layer; (iii) no added Einstein-Hilbert term; (iv) the regularity
quantity not already continuous at this Sigma ([Rtilde] = 0 is
already imposed here, so Rtilde itself and any quantity
continuous by the P61-1 join are disqualified as the regularity
quantity); (v) premises true on BOTH sides of this shell
(interior Phi2 family: R varies with r; MK exterior: R varies
with r — both stored facts). If a candidate passes every
premise, S2^2 is computed from the bulk data under it (second
path required) before any standing revision.

*End of pre-computation record.*
