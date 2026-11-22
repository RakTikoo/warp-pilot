#!/usr/bin/env python3
"""P33-1 CHARGED THIN SHELLS (Phase 33). float64 numerics; sympy for derivations.
Conventions: metric per side ds^2=-f_i dt^2+dr^2/f_i+r^2 dOm^2, f_i=1-2M_i/r+Q_i^2/r^2,
Phi_i=(1/2)ln f_i, s_i=sqrt(f_i(a)), A_i=a Phi_i'(a).
Wormhole (two exteriors) gluing: sigma=-(s1+s2)/(4 pi a),
P=[s1(1+A1)+s2(1+A2)]/(8 pi a).  Difference (one-mouth) gluing flips one sign.
"""
import json, os
import numpy as np
import sympy as sp

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)
R = {}

# ---------------- 1. SYMBOLIC DERIVATION ----------------
a, M, Q, M1, Q1, M2, Q2 = sp.symbols('a M Q M1 Q1 M2 Q2', positive=True)
def fexpr(Mv, Qv): return 1 - 2*Mv/a + Qv**2/a**2
def term(Mv, Qv):
    """s_i(1+A_i) = (2 f + a f')/(2 sqrt(f)); for RN/Schw = (1-M/a)/sqrt(f)."""
    f = fexpr(Mv, Qv)
    fp = sp.diff(f, a)
    t = (2*f + a*fp)/(2*sp.sqrt(f))
    return sp.simplify(t - (1 - Mv/a)/sp.sqrt(f)), sp.simplify(t)

chk1, t_rn = term(M, Q)
sigma_sym = -sp.sqrt(fexpr(M, Q))/(2*sp.pi*a)
P_sym = (1 - M/a)/(4*sp.pi*a*sp.sqrt(fexpr(M, Q)))
R['symbolic'] = {
 's(1+A)_minus_(1-M/a)/sqrt(f)_RN': str(chk1),  # expect 0: charge cancels in 2f+af'
 'sigma_symmetric_RN': 'sigma = -sqrt(1-2M/a+Q^2/a^2)/(2*pi*a)',
 'P_symmetric_RN': 'P = (1-M/a)/(4*pi*a*sqrt(1-2M/a+Q^2/a^2))',
 'sigma_general_wormhole': 'sigma = -(sqrt(f1(a))+sqrt(f2(a)))/(4*pi*a)',
 'P_general_wormhole': 'P = (1/(8*pi*a))*[ (1-M1/a)/sqrt(f1) + (1-M2/a)/sqrt(f2) ]  (each side RN/Schw/Mink: (1-Mi/a)/sqrt(fi); Mink Mi=0 gives 1)',
}
# Q->0 sign check vs P23-1: sigma -> -s/(2 pi a), s=sqrt(1-q), q=2M/a; P -> (1-M/a)/(4 pi a sqrt(1-2M/a))
q = sp.symbols('q', positive=True)
sig0 = sp.simplify(sigma_sym.subs(Q, 0))
P0 = sp.simplify(P_sym.subs(Q, 0))
R['symbolic']['Q0_sigma'] = str(sig0)
R['symbolic']['Q0_P'] = str(P0)
R['symbolic']['Q0_matches_P23'] = bool(
    sp.simplify(sig0 + sp.sqrt(1-2*M/a)/(2*sp.pi*a)) == 0 and
    sp.simplify(P0 - (1-M/a)/(4*sp.pi*a*sp.sqrt(1-2*M/a))) == 0)
# Difference-gluing limit vs P24-1: flip side-2 orientation -> sigma=-(s1-s2)/(4 pi a); smooth limit s1=s2 -> 0
R['symbolic']['difference_limit'] = ('sigma_diff=-(s_out-s_in)/(4*pi*a); smooth s_out=s_in -> 0 (P24-1 check i); '
    'mirror flip of side 2 in the wormhole sum recovers the sum form; P24-1 sigma_diff formula reproduced by construction')

# EM bulk legality (radial E field): u=Q^2/(8 pi r^4)>=0, T=diag(-u,-u,+u,+u) in (t,r,th,ph) mixed form
R['em_bulk'] = {'rho': 'u=Q^2/(8*pi*r^4)>=0', 'p_r': '-u', 'p_t': '+u',
 'NEC': 'rho+p_r=0 (saturated), rho+p_t=2u>=0', 'SEC': 'rho+p_r+2p_t=2u>=0',
 'DEC': '|p_r|=|p_t|=u=rho (saturated)', 'traceless': True,
 'note': 'Maxwell bulk is EC-legal everywhere outside the shell; rho+p_r=0 also makes the flux-free shell conservation law exact for RN sides (P24-1 F-S1 pattern).'}

# ---------------- helpers (float64) ----------------
def f_val(Mv, Qv, av): return 1.0 - 2.0*Mv/av + Qv**2/av**2
def sigma_P(f1, M1v, f2, M2v, av):
    s1, s2 = np.sqrt(f1), np.sqrt(f2)
    sig = -(s1 + s2)/(4*np.pi*av)
    P = ((1-M1v/av)/s1 + (1-M2v/av)/s2)/(8*np.pi*av)
    return sig, P
def ecs(sig, P):
    return {'NEC': bool(sig >= 0 and sig+P >= 0), 'WEC': bool(sig >= 0 and sig+P >= 0),
            'SEC': bool(sig+P >= 0 and sig+2*P >= 0), 'DEC': bool(sig >= 0 and abs(P) <= sig),
            'ALL': bool(sig >= 0 and sig+P >= 0 and sig+2*P >= 0 and abs(P) <= sig)}

# ---------------- 2. GRIDS: symmetric RN ----------------
# scale-free: M=1, a/M in grid with a>r_+(Q) strictly; Q/M in [0,0.999]
yvals = np.linspace(0.0, 0.999, 400)          # Q/M
xvals = np.linspace(1.001, 50.0, 800)         # a/M (filtered per-row by a>r+)
tot = legal = sig_nonneg = 0
min_sig = 1e300; max_P_over_abs_sig = 0.0
sec_only = 0
worst = None
for y in yvals:
    rp = 1.0 + np.sqrt(max(0.0, 1-y*y))       # r_+/M
    xs = xvals[xvals > rp*1.000001]
    if len(xs) == 0: continue
    av = xs; Mv = 1.0; Qv = y
    f = f_val(Mv, Qv, av)
    sig, P = sigma_P(f, Mv, f, Mv, av)
    tot += len(xs)
    sig_nonneg += int(np.sum(sig >= 0))
    e = [ecs(s, p) for s, p in zip(sig, P)]
    legal += sum(ee['ALL'] for ee in e); sec_only += sum(ee['SEC'] and not ee['ALL'] for ee in e)
    i = int(np.argmin(sig))
    if sig[i] < min_sig: min_sig = float(sig[i]); worst = {'Q/M': float(y), 'a/M': float(xs[i]), 'sigma*M': float(sig[i]), 'P*M': float(P[i])}
    max_P_over_abs_sig = max(max_P_over_abs_sig, float(np.max(P/np.abs(sig))))
R['symmetric_RN_grid'] = {'points': int(tot), 'sigma_ge_0': int(sig_nonneg), 'all_EC_legal': int(legal),
 'SEC_only': int(sec_only), 'min_sigma_times_M': min_sig, 'worst_row': worst,
 'max_P_over_|sigma|': max_P_over_abs_sig,
 'note': 'M=1 geometric units; sigma*M and P*M are the scale-free values (a=1 m rows: M=a/x, sigma_phys = (sigma*M)/M in m^-1 geometric).'}

# ---------------- 3. ASYMMETRIC wormhole grids ----------------
def asym_grid(kind):
    tot = legal = snn = 0; min_sig = 1e300
    for y in yvals[::2]:
        rp = 1.0 + np.sqrt(max(0.0, 1-y*y))
        # wormhole topology: a must exceed the outer horizon of BOTH sides
        rp_other = {'RN-Schw': 2.0, 'RN-Mink': 0.0, 'RN-RN-diffQ': 1.0+np.sqrt(max(0.0, 1-(0.5*y)**2))}[kind]
        xs = xvals[xvals > max(rp, rp_other)*1.000001]
        if len(xs) == 0: continue
        av = xs
        f1 = f_val(1.0, y, av)
        if kind == 'RN-Schw':   f2, M2v = f_val(1.0, 0.0, av), 1.0
        elif kind == 'RN-Mink': f2, M2v = np.ones_like(av), 0.0
        elif kind == 'RN-RN-diffQ': f2, M2v = f_val(1.0, 0.5*y, av), 1.0
        sig, P = sigma_P(f1, 1.0, f2, M2v, av)
        tot += len(xs); snn += int(np.sum(sig >= 0))
        legal += sum(ecs(s, p)['ALL'] for s, p in zip(sig, P))
        min_sig = min(min_sig, float(np.min(sig)))
    return {'points': int(tot), 'sigma_ge_0': int(snn), 'all_EC_legal': int(legal), 'min_sigma_times_M': min_sig}
R['asymmetric_grids'] = {k: asym_grid(k) for k in ['RN-Schw', 'RN-Mink', 'RN-RN-diffQ']}

# ---------------- 4. POISSON-VISSER STABILITY WITH CHARGE ----------------
# V(a)=f(a)-(2 pi a sigma(a))^2, sigma(a) extended by conservation sigma'=-2(sigma+P)/a,
# P'(a0)=beta0^2 sigma'(a0). Derive V''(a0) symbolically for general f, then specialise.
av_, b2 = sp.symbols('a0 beta2', real=True)
f0, f1_, f2_ = sp.symbols('f0 fp0 fpp0', real=True)
# equilibrium values (RN): sigma0=-sqrt(f0)/(2 pi a0); P0 from Lanczos
sig0e = -sp.sqrt(f0)/(2*sp.pi*av_)
# use general P0 symbol p0, then substitute RN value
p0 = sp.symbols('p0', real=True)
sigp = -2*(sig0e + p0)/av_                       # sigma'(a0)
gp = -2*sp.pi*(sig0e + 2*p0)                     # g=2 pi a sigma ; g'=-2 pi (sigma+2P)
sigpp = -2*(sigp + b2*sigp)/av_ + 2*(sig0e + p0)/av_**2
gpp = -2*sp.pi*(sigp + 2*b2*sigp)
Vpp = f2_ - 2*(gp**2 + (-sp.sqrt(f0))*gpp)        # g(a0) = -sqrt(f0)
Vpp = sp.expand(Vpp)
# coefficient structure: V'' = C_beta * beta2 + C_0  (linear in beta2)
C_beta = sp.simplify(sp.diff(Vpp, b2)); C_0 = sp.simplify(Vpp.subs(b2, 0))
R['stability_derivation'] = {'V': 'V(a)=f(a)-(2*pi*a*sigma(a))^2,  adot^2+V(a)=0',
 'Vpp_linear_in_beta2': True, 'C_beta_symbolic': str(C_beta), 'C_0_symbolic': str(C_0)}

def Vpp_RN(a0v, Mv, Qv, beta2v):
    """numeric V''(a0) for symmetric RN using the symbolic structure."""
    f = f_val(Mv, Qv, a0v)
    fp = 2*Mv/a0v**2 - 2*Qv**2/a0v**3
    fpp = -4*Mv/a0v**3 + 6*Qv**2/a0v**4
    s = np.sqrt(f)
    sig0 = -s/(2*np.pi*a0v); P0v = (1-Mv/a0v)/(4*np.pi*a0v*s)
    sigp = -2*(sig0+P0v)/a0v
    gp = -2*np.pi*(sig0+2*P0v)
    sigpp = -2*sigp*(1+beta2v)/a0v + 2*(sig0+P0v)/a0v**2
    gpp = -2*np.pi*sigp*(1+2*beta2v)
    return fpp - 2*(gp**2 + (-s)*gpp)

# GATE: Q=0 must reproduce P23-1's a0^2 V'' = [-4(2x-3)(x-1) b2 -(4x^2-6x+3)]/(2x(x-1)), x=a0/(2M)
def Vpp_P23(x, beta2v): return (-4*(2*x-3)*(x-1)*beta2v - (4*x*x-6*x+3))/(2*x*(x-1))
gate_err = 0.0
for xv in [1.1, 1.5, 2.0, 3.0, 5.0, 10.0]:
    for bv in [0.0, 0.37, 1.0]:
        num = ( (2*xv)**2 ) * Vpp_RN(2*xv, 1.0, 0.0, bv)   # a0=2x M, M=1 -> a0^2 V''
        gate_err = max(gate_err, abs(num - Vpp_P23(xv, bv)))
R['stability_derivation']['Q0_gate_vs_P23_max_abs_err'] = float(gate_err)

# FD validation of V'' via integrating sigma(a) ODE with a linear EoS P = P0 + b2 (sigma-sigma0), b2=0.37
def Vpp_FD(a0v, Mv, Qv, beta2v):
    from scipy.integrate import solve_ivp
    f0v = f_val(Mv, Qv, a0v); s0 = np.sqrt(f0v)
    sig0 = -s0/(2*np.pi*a0v); P0v = (1-Mv/a0v)/(4*np.pi*a0v*s0)
    def rhs(av, sv):
        Pv = P0v + beta2v*(sv[0]-sig0)
        return [-2*(sv[0]+Pv)/av]
    h = 1e-4*a0v; xs_ = np.linspace(a0v-3*h, a0v+3*h, 7)
    sol = solve_ivp(rhs, [a0v, a0v+3*h], [sig0], dense_output=True, rtol=1e-12, atol=1e-14)
    sol2 = solve_ivp(rhs, [a0v, a0v-3*h], [sig0], dense_output=True, rtol=1e-12, atol=1e-14)
    sig_all = np.array([ (sol2.sol(x)[0] if x < a0v else sol.sol(x)[0] if x > a0v else sig0) for x in xs_])
    V = f_val(Mv, Qv, xs_) - (2*np.pi*xs_*sig_all)**2
    return float((V[4]-2*V[3]+V[2])/h**2) if False else float(( -V[5]+16*V[4]-30*V[3]+16*V[2]-V[1])/(12*h*h))
fd_rows = []
for (a0v, Qv) in [(3.0, 0.0), (3.0, 0.5), (3.0, 0.9), (5.0, 0.99)]:
    ana = Vpp_RN(a0v, 1.0, Qv, 0.37); fd = Vpp_FD(a0v, 1.0, Qv, 0.37)
    fd_rows.append({'a0/M': a0v, 'Q/M': Qv, 'analytic': ana, 'FD': fd, 'rel_err': abs(ana-fd)/max(abs(ana), 1e-30)})
R['stability_derivation']['FD_validation'] = fd_rows

# beta2 window: V''>0 linear in beta2 -> solve per (a0/M, Q/M); intersect [0,1]
def beta_window(a0v, Mv, Qv):
    v0 = Vpp_RN(a0v, Mv, Qv, 0.0); v1 = Vpp_RN(a0v, Mv, Qv, 1.0)
    slope = v1 - v0
    if abs(slope) < 1e-14: return None
    crit = -v0/slope
    # V''>0 on beta2>crit if slope>0 else beta2<crit
    lo, hi = (crit, np.inf) if slope > 0 else (-np.inf, crit)
    inter = (max(lo, 0.0), min(hi, 1.0))
    return {'beta_crit': float(crit), 'slope_sign': int(np.sign(slope)),
            'window_intersects_[0,1]': bool(inter[0] < inter[1]), 'intersection': [float(inter[0]), float(inter[1])]}
stab = {}
for Qv in [0.0, 0.3, 0.5, 0.7, 0.9, 0.99, 0.999]:
    rp = 1.0 + np.sqrt(max(0.0, 1-Qv*Qv))
    rows = []
    for a0v in np.linspace(rp*1.001, 20.0, 60):
        w = beta_window(float(a0v), 1.0, Qv)
        if w: rows.append({'a0/M': float(a0v), **w})
    n_inter = sum(r['window_intersects_[0,1]'] for r in rows)
    crits = [r['beta_crit'] for r in rows]
    stab[f'Q/M={Qv}'] = {'rows': len(rows), 'intersect_count': int(n_inter),
        'beta_crit_min': float(np.min(crits)) if crits else None, 'beta_crit_max': float(np.max(crits)) if crits else None,
        'sample': rows[::20]}
R['stability_windows'] = stab

# ---------------- 5. WHAT CHARGE BUYS (pricing) ----------------
price = []
for xv in [1.5, 2.0, 3.0, 5.0, 10.0]:   # a/M, M=1
    row = {'a/M': xv}
    for y in [0.0, 0.5, 0.9, 0.99]:
        rp = 1+np.sqrt(max(0.0, 1-y*y))
        if xv <= rp: row[f'Q/M={y}'] = 'a<=r+ (excluded)'; continue
        f = f_val(1.0, y, xv); sig, P = sigma_P(f, 1.0, f, 1.0, xv)
        w = beta_window(xv, 1.0, y)
        row[f'Q/M={y}'] = {'sigma*M': float(sig), 'P*M': float(P), '|sigma|_ratio_vs_Q0': None,
                           'P/|sigma|': float(P/abs(sig)), 'sigma+P (x M)': float(sig+P), 'beta_crit': w['beta_crit'] if w else None}
    s0_ = row.get('Q/M=0.0')
    if isinstance(s0_, dict):
        for y in [0.5, 0.9, 0.99]:
            if isinstance(row.get(f'Q/M={y}'), dict):
                row[f'Q/M={y}']['|sigma|_ratio_vs_Q0'] = float(abs(row[f'Q/M={y}']['sigma*M'])/abs(s0_['sigma*M']))
    price.append(row)
R['pricing_fixed_a_over_M'] = price

# Follow-up F1: fixed a/r+ (charge shrinks r+; is any |sigma| relief a parametrisation artefact?)
fu1 = []
for k in [1.05, 1.5, 2.0, 5.0]:   # a/r+
    row = {'a/r+': k}
    for y in [0.0, 0.5, 0.9, 0.99, 0.999]:
        rp = 1+np.sqrt(max(0.0, 1-y*y)); av = k*rp
        f = f_val(1.0, y, av); sig, P = sigma_P(f, 1.0, f, 1.0, av)
        row[f'Q/M={y}'] = {'a/M': float(av), 'sigma*M': float(sig), 'P*M': float(P)}
    fu1.append(row)
R['followup_F1_fixed_a_over_rplus'] = fu1

# Follow-up F2: near-horizon / extremal limits (a -> r+ along Q fixed; and extremal a->M, Q->M)
lim = []
for y in [0.0, 0.5, 0.9]:
    rp = 1+np.sqrt(1-y*y)
    for eps in [1e-2, 1e-4, 1e-6]:
        av = rp*(1+eps); f = f_val(1.0, y, av); sig, P = sigma_P(f, 1.0, f, 1.0, av)
        lim.append({'limit': 'a->r+ fixed Q', 'Q/M': y, 'eps': eps, 'sigma*M': float(sig), 'P*M': float(P)})
for eps in [1e-2, 1e-4, 1e-6]:  # extremal diagonal: Q=M*(1-eps), a=r+*(1+eps)
    y = 1-eps; rp = 1+np.sqrt(max(0.0, 1-y*y)); av = rp*(1+eps)
    f = f_val(1.0, y, av); sig, P = sigma_P(f, 1.0, f, 1.0, av)
    lim.append({'limit': 'extremal diagonal', 'Q/M': y, 'eps': eps, 'sigma*M': float(sig), 'P*M': float(P)})
R['followup_F2_limits'] = lim

# Follow-up F3: ONE-MOUTH difference gluing (NOT A THROAT): RN exterior vs Minkowski interior ball
om = []
for y in [0.0, 0.5, 0.9, 0.99]:
    rp = 1+np.sqrt(max(0.0, 1-y*y))
    for av in [rp*1.05, 2.0, 3.0, 5.0]:
        if av <= rp: continue
        s_out = np.sqrt(f_val(1.0, y, av)); s_in = 1.0
        sig_d = -(s_out - s_in)/(4*np.pi*av)
        P_d = ( (1-1.0/av)/s_out - 1.0 )/(8*np.pi*av)
        om.append({'Q/M': y, 'a/M': float(av), 'sigma_diff*M': float(sig_d), 'P_diff*M': float(P_d),
                   'shell_ECs': ecs(float(sig_d), float(P_d)), 'label': 'NOT A THROAT'})
R['followup_F3_one_mouth_NOT_A_THROAT'] = om

# a=1 m reference row (symmetric, x=2 i.e. a=2M, Q/M=0.9): geometric sigma in m^-1 -> kg/m^2 via c^2/G
G, c = 6.674e-11, 2.99792458e8
av_m = 1.0; Mv_m = 0.5; y = 0.9; Qv_m = y*Mv_m
f = f_val(Mv_m, Qv_m, av_m); sig, P = sigma_P(f, Mv_m, f, Mv_m, av_m)
R['a_eq_1m_row'] = {'a_m': 1.0, 'M_over_a': 0.5, 'Q/M': y, 'f': float(f), 'sigma_geom_per_m': float(sig),
 'sigma_kg_per_m2': float(sig*c*c/G), 'P_geom_per_m': float(P), 'shell_mass_kg': float(4*np.pi*av_m**2*sig*c*c/G)}

R['verdict'] = {'label': 'AUGMENTED-FAIL',
 'deciding_term': 'sigma = -(sqrt(f_+(a)) + sqrt(f_-(a)))/(4*pi*a) < 0: a sum of two strictly positive roots (f_i(a)>0 for a>r_+). Charge enters only inside the roots (f_RN = 1-2M/a+Q^2/a^2 > f_Schw), so it makes sigma MORE negative at fixed (M,a) and cannot flip the sign for any sub-extremal Q/M<1, symmetric or asymmetric.',
 'pass_rows': 0}

with open(os.path.join(OUT, 'p331_results.json'), 'w') as fh: json.dump(R, fh, indent=1)
print('Q0 gate err:', gate_err)
print('sym grid:', R['symmetric_RN_grid'])
print('asym:', R['asymmetric_grids'])
print('stab intersects:', {k: v['intersect_count'] for k, v in stab.items()})
print('FD:', fd_rows)
print('one-mouth sample:', om[:3])
print('1m row:', R['a_eq_1m_row'])
