# P35-1 Run Record — stated BEFORE solving (per CHECKPOINT35 §P35-1)

Worker P35-1. float64, system python3 (numpy/scipy/sympy). Rows (fixed):
primary f=0.75, w=1/3; cross-checks f=0.5, w=1/3 and f=0.6, w=0;
κ=−1, r0=0.70711 (sqrt(0.5)), x=0.5, domain [r0, 1e3 r0], P33-3
construction verbatim (component profiles rho_i = C_i/(r^4 + C_i/2),
own-density EoSs, separately conserved, Phi solved from fluid-2
conservation: Phi = -(w/(1+w)) ln(rho2/rho2(r0)), Phi(r0)=0).

## GATE (before any new number)
Recompute the three rows from the P33-3 construction and compare to
phase33/results/p333_results.json: kappa*rho_tot(r0) = -1,
c1t2(r0) = 2f-1 to <=1e-9, total conservation residual in the
<=1e-12 class, all-EC pass (totals), det Omega(r0) = 0.

## STEP B — system stated in full before solving
Frame choice: the throat is stated in the g frame, and the matter
profiles live on the g-areal radius r (their conservation equations
are the g-frame ones). The reconstruction therefore uses r = g-areal
radius throughout; the q metric is carried in the SAME coordinate r
(its areal radius is S(r) = r*sqrt(omega_theta), NOT used as a
coordinate — this is the P25-2 H-cusp warning, honoured by not
adopting the q-areal coordinate).
Inputs (known functions of r): totals rho_tot, p_r,tot, p_t,tot;
a = 1+kappa*rho_tot, b_om = 1-kappa*p_r,tot, c_om = 1-kappa*p_t,tot;
tau = 1/sqrt(a*b_om*c_om^2) (Eq.(7) pattern of P20-2 generalised to
general totals); Omega eigenvalues (q = g Omega, mixed):
  omega_t = c_om*sqrt(b_om/a),  omega_r = c_om*sqrt(a/b_om),
  omega_theta = omega_phi = sqrt(a*b_om),  det Omega = c_om^2*a*b_om.
One-fluid limit: p_r,tot = -rho_tot gives b_om = a, omega_t = omega_r
= c_om, omega_theta = a — P20-2's eigenvalues; checked against
P20-2/P33-3 gate values in the gate step.
Solved for: the g shape function via u(r) := 1 - b_g(r)/r
(g metric: ds_g^2 = -exp(2Phi) dt^2 + dr^2/u + r^2 dOmega^2, Phi
INPUT from fluid-2 conservation, normalised Phi(r0)=0).
Equations: the EiBI defining relation q_{mu nu} = g_{mu nu} +
kappa R_{mu nu}(q), with q components Q_t = omega_t exp(2Phi),
Q_r = omega_r/u, Q_theta = omega_theta r^2, and R_{mu nu}(q) the
Ricci tensor of the metric -Q_t dt^2 + Q_r dr^2 + S^2 dOmega^2,
S = r*(a*b_om)^{1/4} (standard static-spherical Ricci formulas,
re-derived with sympy in-run). Three component equations (t, r,
theta) for one unknown u(r): the t equation is a first-order ODE
for u; the r and theta equations are independent residuals that a
reconstruction must ALSO satisfy. Method: exact epsilon = r-r0
series (sympy, rational profile functions) for the throat balance,
which decides existence before any ODE integration; if the series
admits a balance, integrate the t ODE outward and audit all
residuals against the <=1e-8 relative bar.
Bars: residuals <=1e-8 rel; b_g(r0)=r0; b_g'(r0)<1; u>0 on domain
(no horizon); Phi finite. Asymptotics read exactly: Phi tail
coefficient c_Phi vs predicted 4w/(1+w); b_g/r -> 0 or tail named.

## STEP C — prescriptions stated in full before solving
Layer [r0, r0+delta]. Both prescriptions impose a_reg(r0) = eta
(a = 1+kappa*rho_tot; a_reg >= eta in the layer) and agree with the
original totals at r = r0+delta.
 (i) HARD-FLOOR BLEND: a_reg(r) = eta + (a(r)-eta)*t^2,
     t=(r-r0)/delta, in the layer; b_om, c_om unmodified.
     (The registered floor rho_reg = min(rho_tot,(1-eta)/|kappa|)
     is a_reg = max(a,eta); the quadratic blend is its layer
     realisation, stated here.) Layer EC status: reported from
     rho_reg = (a_reg-1)/kappa with the unmodified pressures.
 (ii) SMOOTH INTERPOLATION: totals (rho, p_r, p_t) interpolated by
     the smoothstep s(t)=3t^2-2t^3 between a regular interior
     profile at r0 — (rho*, p_r*, p_t*) = (1-eta, p_r,tot(r0),
     p_t,tot(r0)) (constant in the layer's inner value) — and the
     original totals at r0+delta. a_reg, b_reg, c_reg from the
     interpolated totals. Layer EC status reported.
Ladder (fixed grid, 9 pairs >= 6): delta/r0 in {1e-1, 1e-2, 1e-3}
x eta in {1e-2, 1e-4, 1e-6}; the diagonal is delta/r0 = eta^{1/2}.
Sector posing level (stated, P25-3 honesty pattern): PRINCIPAL
SYMBOL + FROBENIUS/RADIAL-OPERATOR level — NOT a full quadratic
action. On each regularised background the radial operator of a
mode on q is D[Psi] = Psi'' + 2 (S_reg'/S_reg) Psi' -
l(l+1)/S_reg^2 Psi = 0, l=2, S_reg = r*(a_reg*b_reg)^{1/4}
(b_reg = b_om for prescription (i)). Both sectors share this
radial operator at this level (their principal symbol is the q
null cone, P25-2 off-throat read); they differ in regular throat
data: EVEN (polar/angular-trace): Psi(r0)=1, Psi'(r0)=0;
ODD (axial): Psi(r0)=0, Psi'(r0)=1. Extracted per rung: the
logarithmic derivative L = Psi'/Psi at r = r0+delta for each
sector (plus Psi, Psi' separately), and health signs on
[r0+delta, 10 r0] on the ORIGINAL background: kinetic sign
sign(sqrt(det Omega)) and gradient/cone signs (radial cone ratio^2
= omega_t/omega_r = b_om/a > 0; angular cone ratio^2 =
omega_t/omega_theta > 0).
CERTIFIABLE iff BOTH sectors' L AND health signs converge:
relative change <1% across the last diagonal ladder step AND
across the two prescriptions at matched (delta,eta), with healthy
converged signs. Otherwise OBSTRUCTED with partial scope stated.

## Universality read (required either way)
Omega eigen-structure in epsilon: orders of a, b_om, c_om,
omega_t, omega_r, omega_theta, det Omega, S, from analytic values
at r0 plus log-log fits on epsilon in [1e-8, 1e-3]; term-by-term
comparison with P25-2's one-fluid anatomy (B=1+kappa*rho linear,
det Omega ~ eps^2, rank 2/4, omega_t finite); the omega_t pole
question (P33-3) confirmed or refuted with its order.

## STEP D (scoping only)
One paragraph in the memo; no computation.
