#!/usr/bin/env python3
"""W-D G9-4 fresh audit. Loads ONLY the jet formulas derived by W-D's own
wd_derive.py (gate9/wd_generic_bach.json). No phase script is imported;
the Class-B read-off definition (shared text from p712_memo/p614_memo) is
re-implemented here from its statement:
  - frozen slice at radius R: ECs = F(r/R)/R^4, F the unit-radius read;
  - common-domain increment at step Ra->Rb: Delta = new slice - old slice
    on [Rb, 1000 Rb];
  - grown shell: the NEW slice's closed form evaluated on [Ra, Rb]
    (extended inside its own throat, x_b = r/Rb < 1);
  - pricing (P61-4 pattern): integrated negative NEC1 of T = 4 alpha_g B
    (alpha_g = 1), converted at c^4/G, against
    E_legal(L) = (3/(32 pi^2)) hbar c / L at L = Rb
    (E_legal definition re-derived from the P61-4 record).
Conventions: EC combos in the P61-1 B-convention (rho=-Bt, pr=Br, pt=Bth):
rho, NEC1=rho+pr, NEC2=rho+pt, SEC=rho+pr+2pt, DECr=rho-|pr|, DECt=rho-|pt|.
Run with ~/workspace/warp-pilot/venv/bin/python."""
import json, math
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

HBAR = 1.054571817e-34; C = 299792458.0; G_N = 6.67430e-11
C4oG = C**4 / G_N
P = 0.1; A = 0.277734
OUT = {"worker": "W-D", "claim": "G9-4", "engine": "W-D fresh wd_derive.py jet formulas"}

# ---------- load W-D jet formulas ----------
Gj = json.load(open('/home/hatch/workspace/warp-pilot/gate9/wd_generic_bach.json'))
r, b0, b1, b2, b3, b4, P1, P2, P3, P4 = sp.symbols('r b0 b1 b2 b3 b4 P1 P2 P3 P4')
syms = (r, b0, b1, b2, b3, b4, P1, P2, P3, P4)
exprs = {nm: sp.parse_expr(Gj[nm], local_dict={str(s): s for s in syms}) for nm in ['Bt', 'Br', 'Bth']}
Bf_np = {nm: sp.lambdify(syms, exprs[nm], 'numpy') for nm in exprs}
Bf_mp = {nm: sp.lambdify(syms, exprs[nm], 'mpmath') for nm in exprs}
OUT['trace_symbolic_from_derivation'] = Gj['trace']

def ecs_np(Bt, Br, Bth):
    rho, pr, pt = -Bt, Br, Bth
    return dict(rho=rho, NEC1=rho+pr, NEC2=rho+pt, SEC=rho+pr+2*pt,
                DECr=rho-np.abs(pr), DECt=rho-np.abs(pt))

# ---------- ANCHORS (must pass before any claim number) ----------
anch = {}
# (i) Schwarzschild in MT coordinates: b = rs (const), e^{2Phi} = 1 - rs/r
#     (Phi = (1/2) ln(1-rs/r), NOT zero) -> B = 0
_rz = sp.symbols('_rz', positive=True)
mx = 0.0
for rs, rr in [(2.0, 3.0), (2.0, 10.0), (1.0, 1.5)]:
    PhS = sp.log(1-rs/_rz)/2
    pv = [float(sp.lambdify(_rz, sp.diff(PhS, _rz, i), 'numpy')(rr)) for i in range(1, 5)]
    vals = [float(Bf_np[nm](rr, rs, 0, 0, 0, 0, *pv)) for nm in ['Bt', 'Br', 'Bth']]
    mx = max(mx, max(abs(v) for v in vals))
anch['schwarzschild_max_abs_B'] = mx
# (ii) Mannheim-Kazanas: A(r) = 1 - beta(2-3 beta gam)/r - 3 beta gam + gam r - kk r^2
#      e^{2Phi} = A, 1 - b/r = A. Generic beta, gam, kk -> B = 0.
beta_, gam_, kk_ = 2.0, 0.01, 0.001
rsym = sp.symbols('rsym', positive=True)
Aexpr = 1 - beta_*(2-3*beta_*gam_)/rsym - 3*beta_*gam_ + gam_*rsym - kk_*rsym**2
Phiexpr = sp.log(Aexpr)/2
bexpr = rsym*(1 - Aexpr)
jetf = [sp.lambdify(rsym, sp.diff(e, rsym, i), 'numpy')
        for e in [bexpr] for i in range(5)]
phif = [sp.lambdify(rsym, sp.diff(Phiexpr, rsym, i), 'numpy') for i in range(1, 5)]
mx = 0.0; scale = 0.0
for rr in [5.0, 10.0, 20.0]:
    bv = [float(f(rr)) for f in jetf]; pv = [float(f(rr)) for f in phif]
    vals = [float(Bf_np[nm](rr, *bv, *pv)) for nm in ['Bt', 'Br', 'Bth']]
    mx = max(mx, max(abs(v) for v in vals)); scale = max(scale, rr**-4)
anch['MK_max_abs_B'] = mx; anch['MK_scale_r^-4'] = scale
# (iii) T-b closed forms (P61-4 memo, T = 4 alpha_g B, alpha_g=1):
# rho_T = (5/6)(3u-1)/x^5, pr_T = -(5/12)(4u-1)/x^5, pt_T = (5/24)(10u-3)/x^5, u=sqrt(x)
def tb_B(x):
    bv = (x**0.5, 0.5*x**-0.5, -0.25*x**-1.5, 0.375*x**-2.5, -0.9375*x**-3.5)
    return tuple(float(Bf_np[nm](x, *bv, 0, 0, 0, 0)) for nm in ['Bt', 'Br', 'Bth'])
devs = []
for x in [1.0, 2.0, 10.0, 100.0]:
    u = math.sqrt(x)
    rhoT, prT, ptT = (5/6)*(3*u-1)/x**5, -(5/12)*(4*u-1)/x**5, (5/24)*(10*u-3)/x**5
    Bt, Br, Bth = tb_B(x)
    mine = (4*(-Bt), 4*Br, 4*Bth)  # T-convention from my B
    devs.append(max(abs(mine[i]-[rhoT, prT, ptT][i])/abs([rhoT, prT, ptT][i]) for i in range(3)))
anch['Tb_closed_form_max_rel_dev'] = max(devs)
anch['Tb_throat_NEC1_Bconvention'] = float(ecs_np(*[np.float64(v) for v in tb_B(1.0)])['NEC1'])
anch['PASS'] = bool(mx < 1e-9 and anch['schwarzschild_max_abs_B'] < 1e-12 and max(devs) < 1e-9)
OUT['anchors'] = anch
print('ANCHORS', anch, flush=True)
assert anch['PASS'], 'anchor failure = machinery failure, stop'

# ---------- Phi2 family jets (scaled x, r0 = 1) ----------
xsym = sp.symbols('xsym', positive=True)
Lexpr = sp.log(xsym)
Ph2 = A*Lexpr/(1+Lexpr)
phi_np = [sp.lambdify(xsym, sp.diff(Ph2, xsym, i), 'numpy') for i in range(1, 5)]
phi_mp = [sp.lambdify(xsym, sp.diff(Ph2, xsym, i), 'mpmath') for i in range(1, 5)]
def bvals_np(x):
    return (x**P, P*x**(P-1), P*(P-1)*x**(P-2), P*(P-1)*(P-2)*x**(P-3),
            P*(P-1)*(P-2)*(P-3)*x**(P-4))
def F_np(x):
    """Unit-radius B-convention EC combos at scaled radius x (vectorised)."""
    x = np.asarray(x, dtype=float)
    bv = bvals_np(x); pv = tuple(f(x) for f in phi_np)
    return ecs_np(Bf_np['Bt'](x, *bv, *pv), Bf_np['Br'](x, *bv, *pv), Bf_np['Bth'](x, *bv, *pv))
def F1(x):
    return {k: float(v) for k, v in F_np(np.array([x])).items()} if False else \
           {k: float(np.atleast_1d(v)[0]) for k, v in F_np(np.array([float(x)])).items()}

# frozen cross-check at r0=1 (W-A owns the legality read; this is supporting)
xg = np.exp(np.linspace(0, np.log(1000.0), 4001))
E = F_np(xg)
OUT['frozen_r0=1_minima_supporting'] = {k: float(np.min(E[k])) for k in E}
OUT['frozen_r0=1_all_positive_supporting'] = bool(all(np.min(E[k]) > 0 for k in E))

# ---------- (a) SCALE COVARIANCE by DIRECT physical evaluation ----------
# Phi(r; R0) = a ln(r/R0)/(1+ln(r/R0)); b(r; R0) = R0 (r/R0)^p; jets in r.
rr_, R0_ = sp.symbols('rr R0', positive=True)
Lphys = sp.log(rr_/R0_)
Phiphys = A*Lphys/(1+Lphys)
bphys = R0_*(rr_/R0_)**sp.Float(P)
bj = [sp.lambdify((rr_, R0_), sp.diff(bphys, rr_, i), 'numpy') for i in range(5)]
pj = [sp.lambdify((rr_, R0_), sp.diff(Phiphys, rr_, i), 'numpy') for i in range(1, 5)]
def direct_EC(rphys, R0):
    bv = [float(f(rphys, R0)) for f in bj]; pv = [float(f(rphys, R0)) for f in pj]
    Bt, Br, Bth = (float(Bf_np[nm](rphys, *bv, *pv)) for nm in ['Bt', 'Br', 'Bth'])
    return {k: float(v) for k, v in ecs_np(np.float64(Bt), np.float64(Br), np.float64(Bth)).items()}
cov = {}
for R0 in [10.0, 1000.0]:
    mx = 0.0
    for x in [1.0, 1.3, 3.0, 7.0, 30.0, 100.0, 1000.0]:
        d = direct_EC(R0*x, R0); s = F1(x)
        for k in s:
            ref = s[k]/R0**4
            mx = max(mx, abs(d[k]-ref)/abs(ref))
    cov[f'r0={R0:g}'] = mx
OUT['clause_a_covariance_max_rel_dev'] = cov
OUT['clause_a_PASS'] = bool(max(cov.values()) < 1e-9)
print('COVARIANCE', cov, flush=True)

# ---------- (b) INCREMENT (fresh Class-B read-off), decade step ----------
def delta_EC(xb, q=10.0):
    """Delta EC combos in Rb^-4 units, decade step Ra -> Rb = q*Ra:
    Delta(xb) = F(xb) - F(q*xb) * q^4, since the old slice's value at r is
    F(r/Ra)/Ra^4 = F(q*xb) * q^4 in Rb^-4 units."""
    xb = np.asarray(xb, dtype=float)
    Fn = F_np(xb); Fo = F_np(q*xb)
    # old slice physical value = F(q xb)/Ra^4 ; divide by Rb^-4 = multiply by Rb^4:
    # = F(q xb) * (Rb/Ra)^4 = F(q xb) * q^4   [in Rb^-4 units]
    return {k: Fn[k] - Fo[k]*q**4 for k in Fn}
xg1 = np.exp(np.linspace(0, np.log(1000.0), 20001))
D = delta_EC(xg1)
dmin = {k: float(np.min(D[k])) for k in D}
OUT['clause_b_delta_minima_Rb^-4'] = dmin
OUT['clause_b_dNEC1_min_scaled'] = dmin['NEC1']
# crossing of Delta NEC1 = 0 above x=1 (bisection)
def dNEC1(x): return float(np.atleast_1d(delta_EC(np.array([x]))['NEC1'])[0])
lo, hi = 1.0, 1.1
assert dNEC1(lo) < 0 < dNEC1(hi)
for _ in range(80):
    mid = 0.5*(lo+hi)
    if dNEC1(mid) < 0: lo = mid
    else: hi = mid
xc = 0.5*(lo+hi)
OUT['clause_b_layer'] = [1.0, xc]
# which combos fail anywhere on common domain
OUT['clause_b_failing_combos'] = [k for k in D if dmin[k] < 0]
# layer price: integrate negative Delta NEC1 (T conv = 4x) over r in [Rb, xc*Rb], Rb=10
Rb = 10.0
xl = np.linspace(1.0, xc, 20001)
dnec = np.atleast_1d(delta_EC(xl)['NEC1'])/Rb**4*4.0
integ = float(np.trapezoid(np.minimum(dnec, 0.0)*4*np.pi*(xl*Rb)**2, xl*Rb))
Elegal10 = (3.0/(32*np.pi**2))*HBAR*C/Rb
OUT['clause_b_layer_integral_code_per_m'] = integ
OUT['clause_b_E_legal_at_10m_J'] = Elegal10
OUT['clause_b_layer_price_ratio'] = abs(integ)*C4oG/Elegal10
OUT['clause_b_PASS'] = bool(abs(xc-1.00348)/1.00348 < 0.05 and abs(dmin['NEC1']-(-0.016680))/0.016680 < 0.05
                            and 0.5 < OUT['clause_b_layer_price_ratio']/5.83e68 < 2.0)
print('INCREMENT', dmin, 'xc', xc, 'price', OUT['clause_b_layer_price_ratio'], flush=True)

# ---------- (c) POLE anatomy ----------
OUT['clause_c_analytic'] = "Phi2 = a*L/(1+L), L=ln(xb); denominator 1+L=0 at L=-1, i.e. xb=e^-1 exactly."
def F_mp(x):
    pp = mp.mpf('0.1')
    bv = (x**pp, pp*x**(pp-1), pp*(pp-1)*x**(pp-2), pp*(pp-1)*(pp-2)*x**(pp-3),
          pp*(pp-1)*(pp-2)*(pp-3)*x**(pp-4))
    pv = tuple(f(x) for f in phi_mp)
    Bt = Bf_mp['Bt'](x, *bv, *pv); Br = Bf_mp['Br'](x, *bv, *pv); Bth = Bf_mp['Bth'](x, *bv, *pv)
    rho, pr, pt = -Bt, Br, Bth
    return dict(rho=rho, NEC1=rho+pr, NEC2=rho+pt, SEC=rho+pr+2*pt, DECr=rho-abs(pr), DECt=rho-abs(pt))
probes = {}
for lbl, xv in [('e^-1(1-1e-3)', mp.e**-1*(1-mp.mpf('1e-3'))),
                ('e^-1(1-1e-6)', mp.e**-1*(1-mp.mpf('1e-6'))),
                ('0.99', mp.mpf('0.99'))]:
    probes[lbl] = mp.nstr(F_mp(xv)['NEC1'], 12)
OUT['clause_c_NEC1_probes_40digit'] = probes
# pole order: log-log fit of |NEC1| vs delta = |1+ln x| on the minus side
ds = np.array([1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5])
vals = np.array([abs(F1(float(np.exp(-1)*(1-d)))['NEC1']) for d in ds])
dd = np.abs(1+np.log(np.exp(-1)*(1-ds)))
slope, _ = np.polyfit(np.log(dd), np.log(vals), 1)
OUT['clause_c_pole_order_fit'] = float(-slope)
OUT['clause_c_pole_fit_points'] = {f'{d:g}': float(v) for d, v in zip(ds, vals)}
# shell price lower bounds at the three exclusions (decade step 1->10)
def shell_price(Ra, Rb, eps):
    q = Rb/Ra; lo = 1.0/q
    xg = np.exp(np.linspace(np.log(lo), 0, 60001))
    xg = xg[np.abs(1+np.log(xg)) > eps]
    nec1_T = 4.0*np.atleast_1d(F_np(xg)['NEC1'])/Rb**4
    rp = xg*Rb
    return float(np.trapezoid(np.minimum(nec1_T, 0.0)*4*np.pi*rp**2, rp))
prices = {}
for eps in [1e-2, 1e-3, 1e-4]:
    integ = shell_price(1.0, 10.0, eps)
    El = (3.0/(32*np.pi**2))*HBAR*C/10.0
    prices[f'eps={eps:g}'] = {"integral_code_per_m": integ, "ratio_lower_bound": abs(integ)*C4oG/El}
OUT['clause_c_shell_price_lower_bounds'] = prices
stored = [6.925e84, 7.327e90, 1.711e96]
mine = [prices[f'eps={e:g}']['ratio_lower_bound'] for e in [1e-2, 1e-3, 1e-4]]
OUT['clause_c_price_factors_vs_stored'] = [m/s for m, s in zip(mine, stored)]
OUT['clause_c_strictly_increasing'] = bool(mine[0] < mine[1] < mine[2])
p1 = float(probes['e^-1(1-1e-3)']); p2 = float(probes['e^-1(1-1e-6)'])
OUT['clause_c_PASS'] = bool(p1 < 0 and abs(p1/(-6.58e21)) < 3 and abs(p1/(-6.58e21)) > 1/3
    and p2 < 0 and abs(p2/(-6.65e42)) < 3 and abs(p2/(-6.65e42)) > 1/3
    and 6.0 <= OUT['clause_c_pole_order_fit'] <= 8.0
    and all(0.1 < f < 10 for f in OUT['clause_c_price_factors_vs_stored'])
    and OUT['clause_c_strictly_increasing'])
print('POLE', probes, 'order', OUT['clause_c_pole_order_fit'], 'prices', mine, flush=True)

json.dump(OUT, open('/home/hatch/workspace/warp-pilot/gate9/wd_audit_raw.json', 'w'), indent=1)
print('WROTE wd_audit_raw.json')
