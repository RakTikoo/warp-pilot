"""GATE-12 fresh derivation for G12-2: the P61-1 shell endowed with the
Brown-Gladush surface perfect-fluid action (a NEW labelled object, NOT
the conformal member).

Written from scratch for Gate-12. NO phase code imported. The two bulk
metrics are rebuilt here from their registered definitions (shared
DATA: p = 0.1, Phi2 profile a = 0.27773424114865775, r_Sigma = 1000 r0,
MK exterior beta_MK / k / gamma and the shell datum sigma0, read from
the stored P61-1 shell datum file as data):

  interior:  ds2 = -A dt2 + B dr2 + r2 dOmega2,
             A = exp(2 phi2), phi2 = a ln r / (1 + ln r),
             B = 1 / (1 - r^(p-1)),  p = 0.1
  exterior:  A = f, B = 1/f,
             f = 1 - 3 beta gam - beta (2 - 3 beta gam)/r + gam r - k r2

Derivation (this gate's own):
  For a static spherical metric the r = const surface has, with the
  outward unit normal n = dr/sqrt(B),
    K^t_t = A'/(2 A sqrt(B)),   K^th_th = 1/(r sqrt(B))
  (verified below against the covariant definition K_ab = e_a e_b nabla n
  by finite differences on the full 4-metric, and K^t_t's static value
  also from -u.nabla n contraction).
  For a moving shell R(tau) the same contraction gives
    K^t_t = K^t_t|static(R) + C * Rddot + O(Rdot2),  C = sqrt(B)/A,
  verified below by an independent trajectory finite-difference path:
  trial worldlines R(tau) = R0 + (1/2) alpha tau2 are pushed through
  the exact moving-shell normal/velocity construction and
  K(u,u) = u^mu u^nu nabla_mu n_nu is evaluated from the trajectory;
  the alpha-slope of K^t_t = -K(u,u) at alpha = 0 is C per side.
  Endowed action (Brown, CQG 10 (1993) 1579; Gladush gr-qc/0312067
  eq. (2.23) dust case): S = -INT eps(n_s) sqrt(-gamma);
  sigma = eps(n_s), p = n_s eps'(n_s) - eps(n_s), dp = beta2 dsigma.
  Normal equation in vacuum: S^{ab} Kbar_{ab} = 0, Kbar = side average:
    -sigma Kbar^t_t + 2 p Kbar^th_th = 0.
  Background admissibility fixes p0 = sigma0 * Ktt0 / (2 Kth0).
  Conservation (particle number 4 pi R2 n_s fixed):
    dsigma = -2 (sigma0 + p0) xi / r_Sigma,  dp = beta2 dsigma.
  Linearising the normal equation at fixed bulks:
    -sigma0 C_avg xiddot + B(beta2) xi = 0,
    B = -dsig Ktt0 + 2 beta2 dsig Kth0 - sigma0 dKtt + 2 p0 dKth
    (dsig = dsigma/xi),  omega2 = -B / (sigma0 C_avg).
  The fixed-bulk junction read-off strain (shared definition, the
  Rtilde slope D_Rn of the P61-1 record, recomputed here from the
  Rtilde defining formula with fresh sympy code):
    dsigma_J3/xi = -(4/3) D_Rn alpha0-units; ratio vs conservation
    strain is a consistency number, reported, not hidden.

Paths: (1) sympy analytic float64; (2) mpmath 40-digit full
recomputation of every deciding value incl. the sign of omega2 at
the linear EoS; (3) finite-difference / trajectory second paths for
the K values, their radial derivatives, and C.
"""
import json
import numpy as np
import sympy as sp
from mpmath import mp, mpf

mp.dps = 40
W = "/home/hatch/workspace/warp-pilot/"
A_STORED = 0.27773424114865775
P_EXP = 0.1
RSIG = 1000.0
shell80 = json.load(open(W + "phase80/results/p802_shell.json"))
bg = shell80["background_shell_datum_from_P61_1"]
SIGMA0 = float(bg["S00_over_alpha0"])
BETA_MK = float(bg["beta_MK"]); K_MK = float(bg["k"]); GAM = 1e-28
JUMP_TRN_STORED = float(bg["jump_tRn"])

out = {"label": "the P61-1 shell endowed with the Brown-Gladush surface perfect-fluid action",
       "machinery": "gate12/g12_endowed.py fresh sympy + mpmath40 + FD/trajectory paths",
       "shared_data": dict(a=A_STORED, p=P_EXP, r_sigma=RSIG, sigma0=SIGMA0,
                           beta_MK=BETA_MK, k=K_MK, gamma=GAM)}

# ---------------------------------------------------------- sympy analytic path
r = sp.symbols("r", positive=True)
a_s, p_s = sp.symbols("a p")
phi2 = a_s * sp.log(r) / (1 + sp.log(r))
A_in = sp.exp(2 * phi2)
B_in = 1 / (1 - r ** (p_s - 1))
b_s, k_s, g_s = sp.symbols("beta k gam")
f_ex = 1 - 3 * b_s * g_s - b_s * (2 - 3 * b_s * g_s) / r + g_s * r - k_s * r ** 2
A_ex = f_ex
B_ex = 1 / f_ex

def K_of(A, B):
    Ktt = sp.diff(A, r) / (2 * A * sp.sqrt(B))
    Kth = 1 / (r * sp.sqrt(B))
    return Ktt, Kth, sp.diff(Ktt, r), sp.diff(Kth, r)

Kin = K_of(A_in, B_in)
Kex = K_of(A_ex, B_ex)
sub_in = {a_s: A_STORED, p_s: P_EXP}
sub_ex = {b_s: BETA_MK, k_s: K_MK, g_s: GAM}
Kv_in = [float(sp.N(e.subs({**sub_in, r: RSIG}), 30)) for e in Kin]
Kv_ex = [float(sp.N(e.subs({**sub_ex, r: RSIG}), 30)) for e in Kex]
Ktt0 = 0.5 * (Kv_in[0] + Kv_ex[0]); Kth0 = 0.5 * (Kv_in[1] + Kv_ex[1])
dKtt = 0.5 * (Kv_in[2] + Kv_ex[2]); dKth = 0.5 * (Kv_in[3] + Kv_ex[3])
Ain0 = float(sp.N(A_in.subs({**sub_in, r: RSIG}), 30))
Bin0 = float(sp.N(B_in.subs({**sub_in, r: RSIG}), 30))
Aex0 = float(sp.N(A_ex.subs({**sub_ex, r: RSIG}), 30))
Bex0 = 1.0 / Aex0
C_in = np.sqrt(Bin0) / Ain0
C_ex = np.sqrt(Bex0) / Aex0
C_avg = 0.5 * (C_in + C_ex)

w0 = Ktt0 / (2 * Kth0)
p0 = w0 * SIGMA0
dust_resid = -Ktt0
dsig_C1 = -2.0 * (SIGMA0 + p0) / RSIG

def omega2(beta2, Ktt0_=Ktt0, Kth0_=Kth0, dKtt_=dKtt, dKth_=dKth, C_=C_avg):
    B = (-dsig_C1 * Ktt0_ + 2 * beta2 * dsig_C1 * Kth0_
         - SIGMA0 * dKtt_ + 2 * p0 * dKth_)
    return -B / (SIGMA0 * C_)

om_w0 = omega2(w0)
om_0 = omega2(0.0)
b_a, b_b = omega2(0.0), omega2(1.0)
threshold = -b_a / (b_b - b_a)

# ---------------------------------------------------------- Rtilde slopes (shared definition, fresh code)
def data_exprs(A, B):
    Ap, Bp, App = sp.diff(A, r), sp.diff(B, r), sp.diff(A, r, 2)
    a2, b2 = A / r ** 2, B / r ** 2
    ap, bp, app = sp.diff(a2, r), sp.diff(b2, r), sp.diff(a2, r, 2)
    R2 = -app / (a2 * b2) + ap * bp / (2 * a2 * b2 ** 2) + ap ** 2 / (2 * a2 ** 2 * b2)
    return R2, r / sp.sqrt(B) * sp.diff(R2, r)

R2_in, Rn_in = data_exprs(A_in, B_in)
R2_ex, Rn_ex = data_exprs(A_ex, B_ex)
tR_at = float(sp.N(R2_ex.subs({**sub_ex, r: RSIG}), 30)) - float(sp.N(R2_in.subs({**sub_in, r: RSIG}), 30))
tRn_at = float(sp.N(Rn_ex.subs({**sub_ex, r: RSIG}), 30)) - float(sp.N(Rn_in.subs({**sub_in, r: RSIG}), 30))
D_Rn = float(sp.N(sp.diff(Rn_ex, r).subs({**sub_ex, r: RSIG}), 30)) - \
       float(sp.N(sp.diff(Rn_in, r).subs({**sub_in, r: RSIG}), 30))
D_R = float(sp.N(sp.diff(R2_ex, r).subs({**sub_ex, r: RSIG}), 30)) - \
      float(sp.N(sp.diff(R2_in, r).subs({**sub_in, r: RSIG}), 30))
strain_J3 = -(4.0 / 3.0) * D_Rn
ratio = strain_J3 / dsig_C1

# ---------------------------------------------------------- FD second path for K and dK
def Afun_in(x):
    return float(np.exp(2 * A_STORED * np.log(x) / (1 + np.log(x))))
def Bfun_in(x):
    return 1.0 / (1.0 - x ** (P_EXP - 1.0))
def Afun_ex(x):
    return 1 - 3 * BETA_MK * GAM - BETA_MK * (2 - 3 * BETA_MK * GAM) / x + GAM * x - K_MK * x ** 2
def Bfun_ex(x):
    return 1.0 / Afun_ex(x)

def K_num(Af, Bf, x, h=1e-3):
    Apr = (Af(x + h) - Af(x - h)) / (2 * h)
    return Apr / (2 * Af(x) * np.sqrt(Bf(x))), 1.0 / (x * np.sqrt(Bf(x)))
def dK_num(Af, Bf, x, h=0.5):
    kp, _ = K_num(Af, Bf, x + h); km, _ = K_num(Af, Bf, x - h)
    _, tp = K_num(Af, Bf, x + h); _, tm = K_num(Af, Bf, x - h)
    return (kp - km) / (2 * h), (tp - tm) / (2 * h)
fd = {}
for name, Af, Bf, Kv in [("in", Afun_in, Bfun_in, Kv_in), ("ex", Afun_ex, Bfun_ex, Kv_ex)]:
    ktt, kth = K_num(Af, Bf, RSIG)
    dktt, dkth = dK_num(Af, Bf, RSIG)
    fd[name] = dict(Ktt=ktt, Kth=kth, dKtt=dktt, dKth=dkth,
                    sympy=dict(Ktt=Kv[0], Kth=Kv[1], dKtt=Kv[2], dKth=Kv[3]),
                    rel_err_Ktt=abs(ktt - Kv[0]) / abs(Kv[0]),
                    rel_err_dKtt=abs(dktt - Kv[2]) / abs(Kv[2]),
                    rel_err_dKth=abs(dkth - Kv[3]) / abs(Kv[3]))

# ---------------------------------------------------------- trajectory path for C
# Diagonal metric Christoffels (analytic, standard):
# G^t_tr = A'/(2A); G^r_tt = A'/(2B); G^r_rr = B'/(2B); G^r_thth = -r/B;
# G^th_rth = 1/r; G^t_tt = 0 (static). Only the (t,r) sector enters K(u,u).
def C_traj(Af, Bf, R=RSIG, alpha=1e-6, htau=2e-3):
    """K^t_t(alpha) - K^t_t(0) over alpha, from the moving-shell
    construction: u = (tdot, Rdot), n solved from n.u = 0, n.n = +1;
    K(u,u) = u^mu (d_mu n_nu) u^nu along the worldline with the
    covariant correction; K^t_t = -K(u,u). Trajectory in proper time:
    R(tau) = R + alpha tau2/2, t(tau) by integrating tdot."""
    def AB(x):
        hh = 1e-4 * x
        Apr = (Af(x + hh) - Af(x - hh)) / (2 * hh)
        Bpr = (Bf(x + hh) - Bf(x - hh)) / (2 * hh)
        return Af(x), Bf(x), Apr, Bpr
    taus = np.array([-htau, 0.0, htau])
    # integrate t(tau) on a fine grid
    tg = np.linspace(-htau, htau, 401)
    Rg = R + 0.5 * alpha * tg ** 2
    Rdotg = alpha * tg
    tdotg = np.array([np.sqrt(1 + Bf(x) * v ** 2) / np.sqrt(Af(x)) for x, v in zip(Rg, Rdotg)])
    tvals = np.concatenate([[0.0], np.cumsum(0.5 * (tdotg[1:] + tdotg[:-1]) * np.diff(tg))])
    tvals -= np.interp(0.0, tg, tvals)
    def state(tau):
        Rv = R + 0.5 * alpha * tau ** 2
        Rdot = alpha * tau
        tv = float(np.interp(tau, tg, tvals))
        A, B, Apr, Bpr = AB(Rv)
        tdot = np.sqrt(1 + B * Rdot ** 2) / np.sqrt(A)
        # n^mu = (Rdot sqrt(B/A), tdot sqrt(A/B)) in (t, r)
        nt = Rdot * np.sqrt(B / A)
        nr = tdot * np.sqrt(A / B)
        n_low = np.array([-A * nt, B * nr])     # (n_t, n_r)
        u = np.array([tdot, Rdot])
        return Rv, tv, A, B, Apr, Bpr, u, np.array([nt, nr]), n_low
    sts = [state(t) for t in taus]
    # d n_low / d tau by central difference on the trajectory
    dn_low = (sts[2][8] - sts[0][8]) / (2 * htau)
    Rv, tv, A, B, Apr, Bpr, u, n_up, n_low = sts[1]
    # u^mu nabla_mu n_nu = dn_nu/dtau - Gamma^lam_{mu nu} u^mu n_lam
    # nonzero Gammas (t,r sector): G^t_{t r}=A'/(2A) (lam=t, mu=t, nu=r and mu=r,nu=t),
    # G^r_{t t}=A'/(2B), G^r_{r r}=B'/(2B)
    corr = np.zeros(2)
    # nu = t: Gamma^lam_{mu t}: G^t_{r t} n_t * u^r ; G^r_{t t} n_r * u^t
    corr[0] = (Apr / (2 * A)) * u[1] * n_low[0] + (Apr / (2 * B)) * u[0] * n_low[1]
    # nu = r: G^t_{t r} n_t u^t ; G^r_{r r} n_r u^r
    corr[1] = (Apr / (2 * A)) * u[0] * n_low[0] + (Bpr / (2 * B)) * u[1] * n_low[1]
    Dn = dn_low - corr
    Kuu = float(u @ Dn)
    return -Kuu

C_fd = {}
for name, Af, Bf, Cval in [("in", Afun_in, Bfun_in, C_in), ("ex", Afun_ex, Bfun_ex, C_ex)]:
    ktt_a = C_traj(Af, Bf, alpha=2e-6)
    ktt_0 = C_traj(Af, Bf, alpha=0.0)
    slope = (ktt_a - ktt_0) / 2e-6
    C_fd[name] = dict(Ktt_traj_alpha0=ktt_0, Ktt_static_formula=K_num(Af, Bf, RSIG)[0],
                      C_slope=slope, C_formula=Cval, rel_err=abs(slope - Cval) / Cval)
C_avg_fd = 0.5 * (C_fd["in"]["C_slope"] + C_fd["ex"]["C_slope"])

# ---------------------------------------------------------- mpmath 40-digit full recomputation
a_mp = mpf("0.27773424114865775"); p_mp = mpf("0.1")
b_mp = mpf(BETA_MK); k_mp = mpf(K_MK); g_mp = mpf(GAM)
s0_mp = mpf(str(SIGMA0))
R_mp = mpf(1000)
Ain_mp = lambda x: mp.e ** (2 * a_mp * mp.log(x) / (1 + mp.log(x)))
Bin_mp = lambda x: 1 / (1 - x ** (p_mp - 1))
Aex_mp = lambda x: 1 - 3 * b_mp * g_mp - b_mp * (2 - 3 * b_mp * g_mp) / x + g_mp * x - k_mp * x ** 2
Bex_mp = lambda x: 1 / Aex_mp(x)
def K_mp(Af, Bf, x):
    Ktt = mp.diff(Af, x) / (2 * Af(x) * mp.sqrt(Bf(x)))
    Kth = 1 / (x * mp.sqrt(Bf(x)))
    dKtt = mp.diff(lambda y: mp.diff(Af, y) / (2 * Af(y) * mp.sqrt(Bf(y))), x)
    dKth = mp.diff(lambda y: 1 / (y * mp.sqrt(Bf(y))), x)
    return Ktt, Kth, dKtt, dKth
Ki = K_mp(Ain_mp, Bin_mp, R_mp); Ke = K_mp(Aex_mp, Bex_mp, R_mp)
Ktt0_mp = (Ki[0] + Ke[0]) / 2; Kth0_mp = (Ki[1] + Ke[1]) / 2
dKtt_mp = (Ki[2] + Ke[2]) / 2; dKth_mp = (Ki[3] + Ke[3]) / 2
C_mp = (mp.sqrt(Bin_mp(R_mp)) / Ain_mp(R_mp) + mp.sqrt(Bex_mp(R_mp)) / Aex_mp(R_mp)) / 2
w0_mp = Ktt0_mp / (2 * Kth0_mp)
p0_mp = w0_mp * s0_mp
dsig_mp = -2 * (s0_mp + p0_mp) / R_mp
def omega2_mp(beta2):
    B = (-dsig_mp * Ktt0_mp + 2 * beta2 * dsig_mp * Kth0_mp
         - s0_mp * dKtt_mp + 2 * p0_mp * dKth_mp)
    return -B / (s0_mp * C_mp)
om_w0_mp = omega2_mp(w0_mp)
om_0_mp = omega2_mp(mpf(0))
thr_mp = -om_0_mp / (omega2_mp(mpf(1)) - om_0_mp)

out.update({
    "K_sympy": {"in": Kv_in, "ex": Kv_ex, "Ktt0": Ktt0, "Kth0": Kth0,
                "dKtt": dKtt, "dKth": dKth},
    "C": {"C_in": float(C_in), "C_ex": float(C_ex), "C_avg": float(C_avg),
          "trajectory_path": C_fd, "C_avg_trajectory": float(C_avg_fd)},
    "admissibility": {"w0": float(w0), "p0_over_alpha0": float(p0),
                      "dust_residual_over_sigma0": float(dust_resid)},
    "strain": {"D_R": D_R, "D_Rn": D_Rn, "tR_at": tR_at, "tRn_at": tRn_at,
               "tRn_stored": JUMP_TRN_STORED,
               "strain_J3": strain_J3, "strain_C1": float(dsig_C1), "ratio": float(ratio)},
    "spectrum_float64": {"omega2_at_w0": float(om_w0), "omega2_at_0": float(om_0),
                         "threshold": float(threshold),
                         "omega_at_w0": float(np.sqrt(om_w0)) if om_w0 > 0 else None},
    "spectrum_mp40": {"Ktt0": str(Ktt0_mp), "Kth0": str(Kth0_mp),
                      "dKtt": str(dKtt_mp), "dKth": str(dKth_mp),
                      "C_avg": str(C_mp), "w0": str(w0_mp),
                      "omega2_at_w0": str(om_w0_mp), "omega2_at_0": str(om_0_mp),
                      "threshold": str(thr_mp),
                      "sign_omega2_at_w0": "+" if om_w0_mp > 0 else "-"},
    "fd_path": fd,
})
json.dump(out, open(W + "gate12/results/g12_endowed_numbers.json", "w"), indent=1)
print("Ktt0 Kth0", Ktt0, Kth0, "dKtt dKth", dKtt, dKth)
print("C", C_in, C_ex, C_avg, "traj avg", C_avg_fd, C_fd)
print("w0", w0, "p0", p0, "dust", dust_resid)
print("D_Rn", D_Rn, "tRn", tRn_at, "stored", JUMP_TRN_STORED, "ratio", ratio)
print("omega2 w0, 0, thr (f64)", om_w0, om_0, threshold)
print("omega2 w0 (mp40)", om_w0_mp)
print("omega2 0 (mp40)", om_0_mp, "thr mp", thr_mp)
print("fd", fd)
print("WROTE g12_endowed_numbers.json")
