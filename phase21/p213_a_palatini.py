"""
P21-3(a) PALATINI f(R) WORMHOLE AUDIT  (v2)
Paper: Bambi, Cardenas-Avendano, Olmo, Rubiera-Garcia,
"Wormholes and nonsingular space-times in Palatini f(R) gravity",
PRD 93, 064016 (2016), arXiv:1511.03755.
Model (transcribed, eq. numbers from arXiv text):
  Palatini f(R) = R - gamma R^2, Born-Infeld electrodynamics source.
  f_R = 1 - alpha*eta(z)                                   (11)
  eta(z) = (z^2-sqrt(1+z^4))^2/(z^2 sqrt(1+z^4))           (13)
  z_c = (1+2a-sqrt(1+4a))/(2 sqrt(1+4a))                   (16)  [f_R(z_c)=0]
  x^2 = f_R z^2                                            (8)
  dG/dz = z^2/(4 f_R^{3/2})(f~ + phi~/(4pi))(f_R + z f_R'/2)  (7)
  A = 1 - (1+delta1 G)/(delta2 z f_R^{1/2})                (6)
  ds_g^2 = (1/f_R)(-A dt^2 + dx^2/A + x^2 dOm^2)           (5)   [physical g]
  ds_q^2 = -A dt^2 + dx^2/A + x^2 dOm^2                          [auxiliary q=h]
  K ~ 1/(z-z_c)^2                                          (20) [paper's claim]
  radial null: E dlam/dz = (1 + z f_R'/(2 f_R))/sqrt(f_R)  (29)
  BI matter: T^mu_nu=(1/8pi)diag[phi-2X phi_X, phi-2X phi_X, phi, phi] (4)
float64. Kretschmann computed numerically (finite-difference Christoffel/
Riemann at theta=pi/2, where all theta-derivative terms vanish) from the
FULL transcribed functions A(z), f_R(z), x(z) -- not from a truncated series.
"""
import json, os
import numpy as np
import sympy as sp
from scipy.integrate import cumulative_trapezoid, quad

OUT = os.path.join(os.path.dirname(__file__), "results", "p213_results.json")
alpha = 1.0

# eta(z): the ar5iv rendering of eq.(13),
#   eta = (z^2-sqrt(1+z^4))^2/(z^2 sqrt(1+z^4)),
# is INCONSISTENT with the paper's own eqs.(16)/(18): it gives
# eta(z_c)=32.31 at alpha=1, whereas eq.(18) requires eta(z_c)=1/alpha.
# eta is therefore DERIVED from the unambiguous equations: the BI trace
# T=(1/2pi)(phi-X phi_X) with phi_X F^{tr}=q/r^2 gives, with
# w=sqrt(1+z^-4) (= sqrt(1+D^2/beta^2), D=q/r^2, r_c^4=4pi r_q^2 l_beta^2),
# phi-X phi_X = 2 beta^2 (1-w), R=-kappa^2 T, f_R=1-2 gamma R, i.e.
#   eta(z) = 2(w-1),  f_R = 1 - alpha*eta(z)   [eq.(11) form]
# and eq.(12) phi~(z)=2(1-1/w) is reproduced exactly, confirming w.
# The derived f_R zero is z*=[4a^2/(4a+1)]^{1/4}=0.9457 at alpha=1,
# NOT the rendered eq.(16) value 0.1708: logged as a transcription
# discrepancy in the fetched rendering (Das-Paul precedent); every
# verdict-relevant conclusion below is alpha- and z*-value independent.
def w_of(z): return np.sqrt(1.0 + np.asarray(z, dtype=float)**-4)
def eta(z): return 2.0*(w_of(z) - 1.0)
def fR(z): return 1.0 - alpha * eta(z)
def fRp(z):
    z = np.asarray(z, dtype=float)
    return 4.0*alpha*z**-5/w_of(z)

res = {}
zc = (4*alpha**2/(4*alpha + 1))**0.25   # derived f_R zero (see header note)
res["zc_derived_fR_zero_alpha1"] = float(zc)
res["zc_rendered_eq16_alpha1"] = float((1 + 2*alpha - np.sqrt(1 + 4*alpha)) / (2*np.sqrt(1 + 4*alpha)))
res["eta_rendered_eq13_at_rendered_zc"] = 32.314263722522114
res["fR_at_zc"] = float(fR(zc))
res["c_alpha_fRprime_at_zc"] = float(fRp(zc))
res["fR_samples"] = {f"z={z}": float(fR(z)) for z in (0.95, 1.0, 2.0, 5.0, 10.0)}
R_, g_ = sp.symbols("R gamma")
f_ = R_ - g_*R_**2
res["trace_eq_fR_R_minus_2f"] = str(sp.expand(sp.diff(f_, R_)*R_ - 2*f_))  # -R => R=-k^2 T

# ---- G(z): G' is an explicit function of z (eq.7); G(inf)=0 ------------------
def tphi(z): return 2.0*(1.0 - 1.0/w_of(z))          # eq.(12)
def tf(z):
    e = eta(z); return e/(2*np.pi)*(1.0 - alpha*e/2.0)  # eq.(10)
def Gprime(z):
    fr = fR(z)
    return z**2/(4.0*fr**1.5)*(tf(z) + tphi(z)/(4*np.pi))*(fr + 0.5*z*fRp(z))

zgrid = np.geomspace(zc*1.0002, 400.0, 20000)
gp = Gprime(zgrid)
# G(z) = -int_z^inf G' dz ; tail beyond 400 by quad
tail, _ = quad(lambda t: float(Gprime(np.array(t))), 400.0, np.inf, limit=200)
int_from_z = cumulative_trapezoid(gp[::-1], zgrid[::-1], initial=0.0)[::-1]
Ggrid = int_from_z - tail  # int_from_z = int_400^z G' (reversed-axis trapezoid) = -int_z^400
G_at = lambda z: float(np.interp(z, zgrid, Ggrid))
res["G_asymptotic_check"] = {}
for z in (20.0, 50.0, 100.0):
    res["G_asymptotic_check"][f"z={z}"] = {
        "G_numeric": G_at(z), "minus_1_over_16pi_z": -1.0/(16*np.pi*z),
        "ratio_numeric_over_eq15_implied": float(G_at(z)/(-1.0/(16*np.pi*z)))}
res["G_asymptotic_note"] = ("G(z) from eq.(7) with eqs.(10)/(12) as audited is "
  "~3x the coefficient implied by the paper's own RN expansion eq.(15) "
  "(factor 1+eta-coefficient): a normalization inconsistency in the rendered "
  "eqs.(7)/(10)/(13) cluster, logged, not repaired.")
delta1 = delta2 = 1.0
def A_at(z): return 1.0 - (1.0 + delta1*G_at(z))/(delta2*z*np.sqrt(fR(z)))
res["A_samples_delta1=delta2=1"] = {f"z={z}": float(A_at(z)) for z in (1.0, 2.0, 5.0, 20.0)}
# a(alpha): G ~ -a/sqrt(z-z_c)
eps_arr = zgrid[:2000] - zc
a_arr = -Ggrid[:2000]*np.sqrt(eps_arr)
res["a_alpha_fit_eps_in_1e-3..1e-2"] = float(np.median(a_arr[(eps_arr > 1e-3) & (eps_arr < 1e-2)]))
res["throat_areal_radius_over_rc"] = float(zc)
res["throat_area_over_4pi_rc2"] = float(zc**2)

# ---- numeric Kretschmann for ds^2 = -a(z)dt^2 + b(z)dz^2 + R(z)^2 dOm^2 -----
def kretschmann_numeric(a, b, Rr, z):
    N = len(z)
    g = np.zeros((N, 4, 4)); gi = np.zeros((N, 4, 4))
    g[:, 0, 0] = -a; g[:, 1, 1] = b; g[:, 2, 2] = Rr**2; g[:, 3, 3] = Rr**2
    gi[:, 0, 0] = -1/a; gi[:, 1, 1] = 1/b; gi[:, 2, 2] = 1/Rr**2; gi[:, 3, 3] = 1/Rr**2
    dg = np.zeros((N, 4, 4))            # d/dz of g (only z-derivatives at equator)
    for i in range(4):
        dg[:, i, i] = np.gradient(g[:, i, i], z)
    Gam = np.zeros((N, 4, 4, 4))        # Gam[lam,a,b]
    for lam in range(4):
        for aa in range(4):
            for bb in range(4):
                # 1/2 g^{lam mu}(d_a g_{b mu} + d_b g_{a mu} - d_mu g_{ab}); only mu=z terms
                # survive except the mu=lam diagonal pieces with a or b = z.
                expr = np.zeros(N)
                for mu in range(4):
                    if abs(gi[0, lam, mu]) < 1e-300 and lam != mu: continue
                    t1 = dg[:, bb, mu] if aa == 1 else np.zeros(N)
                    t2 = dg[:, aa, mu] if bb == 1 else np.zeros(N)
                    t3 = dg[:, aa, bb] if mu == 1 else np.zeros(N)
                    expr += gi[:, lam, mu]*(t1 + t2 - t3)
                Gam[:, lam, aa, bb] = 0.5*expr
    dGam = np.zeros_like(Gam)
    for lam in range(4):
        for aa in range(4):
            for bb in range(4):
                dGam[:, lam, aa, bb] = np.gradient(Gam[:, lam, aa, bb], z)
    K = np.zeros(N)
    Riem_up = np.zeros((N, 4, 4, 4, 4))  # R^lam_{a b c}: d_b Gam^lam_{a c} - d_c Gam^lam_{a b} + ...
    for lam in range(4):
        for aa in range(4):
            for bb in range(4):
                for cc in range(4):
                    e = (dGam[:, lam, aa, cc] if bb == 1 else 0.0) - (dGam[:, lam, aa, bb] if cc == 1 else 0.0)
                    e = np.broadcast_to(np.asarray(e, dtype=float), (N,)).copy()
                    for mu in range(4):
                        e += Gam[:, lam, bb, mu]*Gam[:, mu, aa, cc] - Gam[:, lam, cc, mu]*Gam[:, mu, aa, bb]
                    Riem_up[:, lam, aa, bb, cc] = e
    for lam in range(4):
        for aa in range(4):
            for bb in range(4):
                for cc in range(4):
                    Rlow = g[:, lam, lam]*Riem_up[:, lam, aa, bb, cc]
                    K += Rlow**2 * gi[:, lam, lam]*gi[:, aa, aa]*gi[:, bb, bb]*gi[:, cc, cc]
    return K

# grids approaching the throat
zk = np.geomspace(zc + 2e-4, 3.0, 3000)
frk = fR(zk); xk = zk*np.sqrt(frk)
Ak = np.array([A_at(z) for z in zk])
xpk = np.gradient(xk, zk)
# q metric in z-coords: a=A, b=x'^2/A, R=x
Kq = kretschmann_numeric(Ak, xpk**2/Ak, xk, zk)
# g metric in z-coords: a=A/f_R, b=x'^2/(A f_R), R=z
Kg = kretschmann_numeric(Ak/frk, xpk**2/(Ak*frk), zk, zk)
epsk = zk - zc
for name, K in (("q", Kq), ("g", Kg)):
    m = (epsk > 3e-3) & (epsk < 5e-2) & np.isfinite(K) & (K > 0)
    slope, intercept = np.polyfit(np.log(epsk[m]), np.log(K[m]), 1)
    res[f"K_{name}_near_throat"] = {
        "loglog_slope_vs_eps": float(slope),
        "K_at_eps_0.01": float(np.interp(0.01, epsk, K)),
        "K_at_eps_0.001": float(K[np.argmin(np.abs(epsk - 1e-3))]),
        "note": "paper eq.(20) claims K ~ eps^-2 for the physical metric"}
res["fR_at_throat_limit"] = 0.0
res["q_metric_degeneracy"] = ("q = f_R g with f_R(z_c)=0 exactly: the auxiliary "
    "metric degenerates (det q -> 0) at the throat surface.")

# ---- radial null geodesics (eq.29): affine parameter to the throat ----------
def dlam_dz(z):
    fr = float(fR(np.array(z)))
    return (1.0 + z*float(fRp(np.array(z)))/(2*fr))/np.sqrt(fr)
for zstart in (2.0, 5.0):
    pts = []
    for eps in (1e-1, 1e-2, 1e-3, 1e-4):
        val, _ = quad(dlam_dz, zc + eps, zstart, limit=400)
        pts.append({"eps": eps, "Delta_lambda_times_E": float(val),
                    "val_times_sqrt_eps": float(val*np.sqrt(eps))})
    res[f"radial_null_lambda_from_z{zstart}"] = pts
res["lambda_asymptote_expected_zc_over_sqrt_c"] = float(zc/np.sqrt(float(fRp(zc))))

# ---- BI matter ECs (eq.4; s=1/z^4, X/beta^2=s/(1+s), phi_X=sqrt(1+s)) -------
def matter(z):
    s = 1.0/z**4
    phi_hat = 1.0 - (1+s)**-0.5
    tt = phi_hat - 2*(s/(1+s))*np.sqrt(1+s)
    return -tt, tt, phi_hat     # rho, p_r, p_t (common positive prefactor dropped)
zg = np.geomspace(zc*1.0001, 1e3, 800)
rho, pr, pt = matter(zg)
res["matter_EC_minima_full_domain"] = {
    "rho": float(rho.min()), "rho+pr": float((rho+pr).min()),
    "rho+pt": float((rho+pt).min()), "rho+pr+2pt": float((rho+pr+2*pt).min()),
    "rho-|pr|": float((rho-np.abs(pr)).min()), "rho-|pt|": float((rho-np.abs(pt)).min()),
    "note": "minima are the infimum 0 approached at infinity; all six combos >= 0 everywhere"}
res["matter_at_throat"] = {"rho": float(rho[0]), "pr": float(pr[0]), "pt": float(pt[0])}
res["conservation"] = ("nabla^g T = 0 identically for the sourceless BI field "
    "(paper Sec.IV: T is conserved w.r.t. the Levi-Civita connection of g).")

data = {}
if os.path.exists(OUT):
    data = json.load(open(OUT))
data["a_palatini_fR_bambi2016"] = res
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(data, open(OUT, "w"), indent=1)
print(json.dumps(res, indent=1))
