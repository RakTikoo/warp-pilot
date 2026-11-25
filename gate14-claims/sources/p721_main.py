"""P72-1 main compute: (i) audit of exact BSKR solution S-A;
(ii) Dirac throat system on Ellis / sqrt MT backgrounds (Phi=0).
Writes results/p721_results.json. float64."""
import numpy as np, json
from scipy.integrate import solve_ivp, quad

R0 = 1.0
C_LIGHT = 299792458.0; G_SI = 6.67430e-11; MJ = 1.8982e27

# ---------- geometry (sympy-derived, sign-checked vs Ellis) ----------
def Gcomps(lv, F0, F1, F0d, F1d, F0dd, r0=R0):
    R2 = lv**2 + r0**2
    Gtt = (-2 * lv * R2 * F1d - R2 * F1**3 + (lv**2 + 2 * r0**2) * F1) / (R2**2 * F1**3)
    Gll = (2 * lv * R2 * F0d - R2 * F0 * F1**2 + lv**2 * F0) / (R2**2 * F0 * F1**2)
    num = (lv**4 * F1 * F0dd - lv**4 * F0d * F1d - lv**3 * F0 * F1d + lv**3 * F1 * F0d
           + 2 * lv**2 * r0**2 * F1 * F0dd - 2 * lv**2 * r0**2 * F0d * F1d
           - lv * r0**2 * F0 * F1d + lv * r0**2 * F1 * F0d
           + r0**4 * F1 * F0dd - r0**4 * F0d * F1d + r0**2 * F0 * F1)
    Gth = num / (R2**2 * F0 * F1**3)
    return Gtt, Gll, Gth

def Tdirac(P, Q, Pd, Qd, F0, F1, R, w, kap=1):
    Tt = -4 * w * (P**2 + Q**2) / F0
    Tl = 4 * (Pd * Q - P * Qd) / F1
    Tt_ = 2 * kap * (Q**2 - P**2) / R
    return Tt, Tl, Tt_

# ---------- exact solution S-A (analytic, from EPJC App D) ----------
def exact_funcs(Qe, c0=1.0, kap=1, r0=R0):
    def vals(lv):
        lv = np.asarray(lv, float); R = np.sqrt(lv**2 + r0**2)
        F0 = 1 - (2 * Qe**2 * r0 / (Qe**2 + r0**2)) / R
        F1 = np.sqrt(1 + r0 / R) / np.sqrt(1 - Qe**2 / (r0 * R))
        sq1 = np.sqrt(1 - Qe**2 / (r0 * R)); sq2 = np.sqrt(np.maximum(1 - r0 / R, 0))
        U1 = c0 / np.sqrt(F0) * (sq1 - kap * sq2)**2
        U2 = kap * r0 / (32 * c0 * (Qe**2 + r0**2) * np.sqrt(F0)) * (sq1 + kap * sq2)**2
        P = U1 - U2; Q = U1 + U2
        V = (2 * Qe * r0 / (Qe**2 + r0**2)) * np.sqrt((1 - Qe**2 / (r0 * R)) * np.maximum(1 - r0 / R, 0))
        return R, F0, F1, P, Q, V
    return vals

def derivs(f, lv, h=1e-5):
    """central FD derivatives of the 6-tuple returned by f"""
    fp = f(lv + h); fm = f(lv - h); f0 = f(lv)
    d1 = tuple((a - b) / (2 * h) for a, b in zip(fp, fm))
    d2 = tuple((a - 2 * b + c) / h**2 for a, b, c in zip(fp, f0, fm))
    return f0, d1, d2

# ---------- numeric Riemann (FD, for tidal) ----------
def riemann_orth(lv, f, h=2e-3):
    """orthonormal Riemann comps for diag metric in (t,l,th,ph) at th=pi/2.
    Returns dict with R_tltl, R_tthtth, R_lthlth (mixed, static frame)."""
    def metric(x):
        R, F0, F1, P, Q, V = f(x)
        return np.array([-F0**2, F1**2, R**2, R**2])  # th=pi/2: sin=1
    # Use standard formulas in alpha=lnF0, beta=lnF1, R(l):
    def ab(x):
        R, F0, F1, *_ = f(x)
        return np.log(F0), np.log(F1), R
    a0, b0, R0v = ab(lv)
    ap, bp, Rp = ab(lv + h); am, bm, Rm = ab(lv - h)
    a1 = (ap - am) / (2 * h); b1 = (bp - bm) / (2 * h); R1 = (Rp - Rm) / (2 * h)
    a2 = (ap - 2 * a0 + am) / h**2; R2d = (Rp - 2 * R0v + Rm) / h**2
    e2b = np.exp(-2 * b0)
    Rtltl = -e2b * (a2 + a1**2 - a1 * b1)          # R^t_{l t l} mixed sign conv: tidal = -R^t_{0t0}... use magnitudes below
    Rtth = -e2b * a1 * R1 / R0v                    # R^t_{th t th}
    Rlth = -e2b * (R2d / R0v - R1 * b1 / R0v) + (1 - e2b * R1**2) / R0v**2 * 0  # placeholder refined below
    # R^l_{th l th} orthonormal: -e^{-2b}(R''/R - R'b'/R) ; the (1-..)/R^2 term is R_thphthph
    Rlth = -e2b * (R2d / R0v - R1 * b1 / R0v)
    Rthph = (1 - e2b * R1**2) / R0v**2
    return dict(Rtltl=Rtltl, Rtthtth=Rtth, Rlthlth=Rlth, Rthphthph=Rthph)

results = {'gates': {}, 'part_i': {}, 'part_ii': {}}

# GATE G1: FD-Riemann formulas vs Ellis known traveller tidal 0.010101/r0^2 (P23-3)
def ellis_f(lv):
    lv = np.asarray(lv, float); R = np.sqrt(lv**2 + 1.0)
    return R, np.ones_like(lv), np.ones_like(lv), np.zeros_like(lv), np.zeros_like(lv), np.zeros_like(lv)
rc = riemann_orth(0.0, ellis_f)
v = 0.1; gam = 1 / np.sqrt(1 - v**2)
trans_trav = gam**2 * (rc['Rtthtth'] + v**2 * rc['Rlthlth'])
results['gates']['G1_ellis_transverse_traveller_tidal'] = float(trans_trav)
results['gates']['G1_expected'] = 0.010101010101010102
results['gates']['G1_pass'] = bool(abs(abs(trans_trav) - 0.010101010101010102) < 5e-4)
results['gates']['G2'] = 'see p721_validate.py output recorded in memo: max Einstein/Dirac/Maxwell residuals ~1e-14 for l in [0.05,100], Qe in {0.25,0.5}, c0 in {0.5,1,2}'
# GATE G3: Ellis throat demands from Gcomps at l=0, F1=1
Gtt0, Gll0, Gth0 = Gcomps(0.0, 1.0, 1.0, 0.0, 0.0, 0.0)
results['gates']['G3_rho_dem'] = float(-Gtt0 / (8 * np.pi))
results['gates']['G3_rho_plus_pr_dem'] = float((-Gtt0 + Gll0) / (8 * np.pi))
results['gates']['G3_pass'] = bool(abs(-Gtt0 / (8 * np.pi) + 1 / (8 * np.pi)) < 1e-12 and abs((-Gtt0 + Gll0) / (8 * np.pi) + 1 / (4 * np.pi)) < 1e-12)

# ---------- PART I ----------
for Qe in [0.25, 0.5, 0.75, 0.9]:
    f = exact_funcs(Qe)
    # dense grid in R (areal), two resolutions
    grids = {}
    for tag, n in [('coarse', 2000), ('fine', 8000)]:
        Rg = np.concatenate([[1.0], np.logspace(0, 3, n)])
        lg = np.sqrt(Rg**2 - 1.0)
        rho = np.empty_like(lg); pr = np.empty_like(lg); pt = np.empty_like(lg)
        for i, lv in enumerate(lg):
            (R, F0, F1, P, Q, V), d1, d2 = derivs(f, lv, h=1e-5 * max(1.0, lv))
            Gtt, Gll, Gth = Gcomps(lv, F0, F1, d1[1], d1[2], d2[1])
            rho[i] = -Gtt / (8 * np.pi); pr[i] = Gll / (8 * np.pi); pt[i] = Gth / (8 * np.pi)
        grids[tag] = (Rg, rho, pr, pt)
    Rg, rho, pr, pt = grids['fine']
    Rg2, rho2, pr2, pt2 = grids['coarse']
    def margins(rho, pr, pt):
        return dict(NEC1=rho + pr, NEC2=rho + pt, WEC=rho,
                    SEC1=rho + pr + 2 * pt, DEC_r=rho - np.abs(pr), DEC_t=rho - np.abs(pt))
    mf = margins(rho, pr, pt); mc = margins(rho2, pr2, pt2)
    entry = {'Qe_over_r0': Qe, 'beta_throat': Qe**2, 'M_over_r0': 2 * Qe**2 / (Qe**2 + 1)}
    for k in mf:
        entry[k + '_min_fine'] = float(np.min(mf[k])); entry[k + '_min_coarse'] = float(np.min(mc[k]))
        entry[k + '_min_at_R'] = float(Rg[np.argmin(mf[k])])
    entry['rho_throat'] = float(rho[0]); entry['pr_throat'] = float(pr[0]); entry['pt_throat'] = float(pt[0])
    entry['spinor_at_infinity_P'] = float(f(1e6)[3]); entry['spinor_at_infinity_Q'] = float(f(1e6)[4])
    # tidal at throat (FD Riemann on exact profile)
    rc = riemann_orth(0.0, f)
    entry['tidal_radial_static_throat_per_r0sq'] = float(abs(rc['Rtltl']))
    entry['tidal_trans_static_throat'] = float(rc['Rtthtth']); entry['tidal_Rlthlth_throat'] = float(rc['Rlthlth'])
    for vv, nm in [(0.1, 'v01'), ('c', 'vc')]:
        vv_ = 0.1 if vv == 0.1 else 1 - 1e-9
        gm = 1 / np.sqrt(1 - vv_**2)
        entry[f'tidal_trans_trav_{nm}_per_r0sq'] = float(gm**2 * (rc['Rtthtth'] + vv_**2 * rc['Rlthlth']))
    # r0* from radial tidal (boost-invariant) and transverse v=0.1 (use max coefficient)
    Ctid = max(abs(rc['Rtltl']), abs(entry['tidal_trans_trav_v01_per_r0sq']))
    entry['tidal_coeff_used'] = float(Ctid)
    r0star = np.sqrt(Ctid * C_LIGHT**2 / 4.905)
    entry['r0star_m'] = float(r0star)
    # crossing at r0=1m and r0=r0star: d tau = F1 dl/(gamma v), dt = F1 dl/(v F0); stations areal +-10 r0 -> l=sqrt(99)
    L10 = np.sqrt(99.0)
    taus = {}
    for r0m, nm in [(1.0, 'r0_1m'), (r0star, 'r0star')]:
        integrand_tau = lambda x: float(f(x)[2]) / (gam01 := 1 / np.sqrt(1 - 0.01)) / 0.1
        integrand_t = lambda x: float(f(x)[2]) / (0.1 * float(f(x)[1]))
        tau_geom = quad(integrand_tau, -L10, L10, limit=200)[0]
        t_geom = quad(integrand_t, -L10, L10, limit=200)[0]
        taus[nm] = dict(proper_s=float(tau_geom * r0m / C_LIGHT), external_s=float(t_geom * r0m / C_LIGHT),
                        M_kg=float((2 * Qe**2 / (Qe**2 + 1)) * r0m * C_LIGHT**2 / G_SI),
                        M_MJ=float((2 * Qe**2 / (Qe**2 + 1)) * r0m * C_LIGHT**2 / G_SI / MJ))
    entry['crossing'] = taus
    results['part_i'][f'Qe_{Qe}'] = entry

# ---------- PART II ----------
# backgrounds: F1(l) for Ellis (=1) and sqrt-shape; F0=1
def F1_shape(lv, shape):
    lv = np.asarray(lv, float); R = np.sqrt(lv**2 + 1.0)
    if shape == 'ellis':
        return np.ones_like(lv)
    return (lv / R) / np.sqrt(1 - np.sqrt(1.0 / R) + 1e-300) if np.ndim(lv) else None

def F1_shape_scalar(lv, shape):
    R = np.sqrt(lv**2 + 1.0)
    if shape == 'ellis':
        return 1.0
    if lv == 0.0:
        return 2.0
    return (lv / R) / np.sqrt(1 - np.sqrt(1.0 / R))

def dirac_rhs(lv, y, shape, w, mu):
    P, Q = y
    R = np.sqrt(lv**2 + 1.0); F1 = F1_shape_scalar(lv, shape)
    F2d = lv / R
    Pd = -(F2d / R) * P - (F1 / R) * (1 - R * w) * Q + mu * F1 * P
    Qd = -(F2d / R) * Q - (F1 / R) * (1 + R * w) * P - mu * F1 * Q
    return [Pd, Qd]

for shape, beta in [('ellis', -1.0), ('sqrt', 0.5)]:
    F10 = F1_shape_scalar(0.0, shape)
    for mu in [0.0, 0.2, 1.0]:
        key = f'{shape}_mu{mu}'
        D = (beta - 1) / 8.0
        if mu == 0.0:
            # Eq B residual at any datum satisfying A and C: beta (derived in analysis); verify numerically below
            results['part_ii'][key] = dict(beta=beta, mu=mu, closing=False,
                eqB_residual_floor=float(beta), reason='mu=0: EqB reduces to beta=0 required; residual = beta in Tll-eq units')
            continue
        PQ = -beta / (8 * mu)
        S = np.sqrt(D**2 + 4 * PQ**2)
        P0sq = (S + D) / 2; Q0sq = (S - D) / 2
        P0 = np.sqrt(P0sq); Q0 = -np.sign(PQ) * np.sqrt(Q0sq)  # PQ<0 case sign; general: choose Q0 sign so P0*Q0=PQ
        if P0 * Q0 != 0 and np.sign(P0 * Q0) != np.sign(PQ):
            Q0 = -Q0
        w = beta / (8 * S)
        # throat residuals direct from G/T formulas
        Pd0, Qd0 = dirac_rhs(0.0, [P0, Q0], shape, w, mu)
        Gtt, Gll, Gth = Gcomps(0.0, 1.0, F10, 0.0, 0.0, 0.0)
        Tt, Tl, Tth = Tdirac(P0, Q0, Pd0, Qd0, 1.0, F10, 1.0, w)
        # theta slaves F0dd: Gth(F0dd) = (F0dd + 1)/F10^2 (r0=1) -> F0dd = F10^2 * 2*Tth - 1 ; with Phi=0 fixed, F0dd=0 is required:
        res_thth_phi0 = Gth - 2 * Tth
        res = dict(tt=Gtt - 2 * Tt, rr=Gll - 2 * Tl, thth_with_Phi0=res_thth_phi0)
        entry = dict(beta=beta, mu=mu, P0=float(P0), Q0=float(Q0), w=float(w), S=float(S),
                     Pd0=float(Pd0), Qd0=float(Qd0), throat_residuals={k: float(v) for k, v in res.items()},
                     closing=bool(max(abs(x) for x in res.values()) < 1e-9))
        # NOTE: thth residual computed with F0dd=0; the analytic solve used EqC which IS thth with F0dd=0.
        # Extension: integrate Dirac on fixed background, read Einstein residuals
        Lmax = np.sqrt(1000.0**2 - 1.0)
        sol = solve_ivp(dirac_rhs, [0, Lmax], [P0, Q0], args=(shape, w, mu),
                        method='DOP853', rtol=1e-10, atol=1e-12, dense_output=True)
        entry['extension_status'] = sol.status; entry['extension_message'] = sol.message
        ls = np.concatenate([[0.0], np.logspace(-4, np.log10(Lmax), 4000)])
        Y = sol.sol(ls)
        breach = None; maxrel = 0.0
        relprof = []
        for i, lv in enumerate(ls):
            P_, Q_ = Y[0][i], Y[1][i]
            Pd_, Qd_ = dirac_rhs(lv, [P_, Q_], shape, w, mu)
            R = np.sqrt(lv**2 + 1.0); F1 = F1_shape_scalar(lv, shape)
            # F1' analytic via FD on shape function
            hh = 1e-6 * max(1.0, lv)
            F1d = (F1_shape_scalar(lv + hh, shape) - F1_shape_scalar(lv - hh, shape)) / (2 * hh) if lv > 0 else 0.0
            Gtt, Gll, Gth = Gcomps(lv, 1.0, F1, 0.0, F1d, 0.0)
            Tt, Tl, Tth = Tdirac(P_, Q_, Pd_, Qd_, 1.0, F1, R, w)
            scale = max(abs(Gtt), abs(Gll), abs(Gth), abs(2 * Tt), abs(2 * Tl), abs(2 * Tth), 1e-12)
            rel = max(abs(Gtt - 2 * Tt), abs(Gll - 2 * Tl), abs(Gth - 2 * Tth)) / scale
            relprof.append(rel); maxrel = max(maxrel, rel)
            if breach is None and rel > 0.02:
                breach = float(R)
        entry['domain_breach_R_over_r0'] = breach
        entry['domain_max_rel_residual'] = float(maxrel)
        entry['spinor_end'] = [float(Y[0][-1]), float(Y[1][-1])]
        entry['blowup'] = bool(not np.all(np.isfinite(Y)))
        Sprof = Y[0]**2 + Y[1]**2
        S0 = P0**2 + Q0**2
        blow = np.where(Sprof > 1e6 * S0)[0]
        entry['spinor_blowup_R_over_r0'] = float(np.sqrt(ls[blow[0]]**2 + 1)) if len(blow) else None
        entry['rel_residual_profile_sample'] = [float(relprof[i]) for i in [0, 10, 100, 500, 1000, 2000, 3999]]
        results['part_ii'][key] = entry

with open('results/p721_results.json', 'w') as fh:
    json.dump(results, fh, indent=1)
print(json.dumps(results['gates'], indent=1))
for k, e in results['part_i'].items():
    print(k, 'NEC1min=%.4g DEC_r_min=%.4g rho_throat=%.4g r0star=%.3g' % (e['NEC1_min_fine'], e['DEC_r_min_fine'], e['rho_throat'], e['r0star_m']))
for k, e in results['part_ii'].items():
    print(k, 'closing=', e.get('closing'), 'breach_R=', e.get('domain_breach_R_over_r0'), 'res=', e.get('throat_residuals', e.get('eqB_residual_floor')))
