#!/usr/bin/env python3
"""P35-3 COUNTER-ROTATING SHELL CURRENTS (Phase 35). float64; sympy derivations.

RUN RECORD (stated BEFORE solving, per CHECKPOINT35 §P35-3):
Baseline: sum-glued thin-shell throat (wormhole topology ONLY; difference
gluing is P24-1 scope, NOT this item). Per side i: metric
ds^2=-f_i dt^2+dr^2/f_i+r^2 dOm^2, f_i=1-2M_i/r+Q_i^2/r^2, s_i=sqrt(f_i(a)),
t_i := s_i(1+A_i) = (1-M_i/a)/s_i (RN/Schw; Minkowski M_i=0 gives t_i=1).
Lanczos (P23-1/P33-1): sigma_L = -(s_+ + s_-)/(4 pi a),
P_L = (t_+ + t_-)/(8 pi a)  [isotropic: P_theta = P_phi = P_L for spherical bulks].
Admissible domain: a > r_{+,i} for both sides (so f_i(a)>0, a > M_i).

STREAM MODEL (registered): two equal counter-rotating dust streams,
speeds +-v tangentially, equal rest surface densities sigma0/2 each,
sigma0 = TOTAL rest surface density, gamma=1/sqrt(1-v^2), net S^t_phi=0.
 M1 (streams along phi-hat): sigma_s = sigma0 gamma^2,
     P_parallel(=P_phi) = sigma_s v^2, P_perp(=P_theta) = 0.
 M2 (isotropised counter-rotating pairs): sigma_s = sigma0 gamma^2,
     P_theta = P_phi = sigma_s v^2.
MATCHING: Lanczos equations imposed as EQUATIONS on (sigma0>0, v<=0.5):
 sigma_s = sigma_L AND P-equation (M1: phi-phi eq; M1's theta-theta
 Lanczos pressure P_L vs its demanded 0 is the inconsistency measure;
 M2: both tangential equations coincide). A row passes only if ONE
 (sigma0, v) pair satisfies both.

BETA0^2 PRESCRIPTION (stated BEFORE solving): Poisson-Visser stability
with the stream EoS along the stream family at FIXED v (v is the family
parameter). On that family P = v^2 * sigma_s exactly (linear), so
 beta0^2 := dP/d sigma_s |_{v fixed} = v^2 in [0, 0.25] for v<=0.5.
 (The registered general form v^2 + sigma_s d(v^2)/d sigma_s reduces to
 v^2 under this fixed-v prescription, since d(v^2)/d sigma_s = 0.)
Stability read: V''(a0) from the P33-1 symbolic structure (gated below
against P23-1's closed form at Q=0), evaluated at beta0^2 = v^2.
Window-intersection clause: V''(a0) > 0 for some beta0^2 in [0,0.25]
(the stream-attainable subset of [0,1]).
"""
import json, os
import numpy as np
import sympy as sp

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)
R = {"item": "P35-3 counter-rotating shell currents",
     "prescription_beta0sq": "fixed-v stream family: P = v^2 sigma_s exactly, beta0^2 = v^2 in [0,0.25]"}

# ============ 1. SYMPY: Lanczos + stream tensor + limits ============
a, M, Q, v, s0 = sp.symbols('a M Q v sigma0', positive=True)
gam = 1/sp.sqrt(1-v**2)
f_RN = 1 - 2*M/a + Q**2/a**2
sig_sym = -sp.sqrt(f_RN)/(2*sp.pi*a)                      # symmetric: -(s+s)/(4 pi a)
P_sym = (1 - M/a)/(4*sp.pi*a*sp.sqrt(f_RN))
# Q->0 limit vs P23-1 (sigma=-sqrt(1-2M/a)/(2 pi a), P=(1-M/a)/(4 pi a sqrt(1-2M/a)))
R['sympy'] = {
 'Q0_check': bool(sp.simplify(sig_sym.subs(Q, 0) + sp.sqrt(1-2*M/a)/(2*sp.pi*a)) == 0
                  and sp.simplify(P_sym.subs(Q, 0) - (1-M/a)/(4*sp.pi*a*sp.sqrt(1-2*M/a))) == 0),
 # stream tensor from two dust streams: each (sigma0/2) gamma^2 (energy), (sigma0/2) gamma^2 v^2 (phi pressure)
 'stream_sigma_s': str(sp.simplify(2*(s0/2)*gam**2)),                    # sigma0/(1-v^2)
 'stream_P_parallel': str(sp.simplify(2*(s0/2)*gam**2*v**2)),            # sigma0 v^2/(1-v^2)
 'ratio_P_over_sigma': str(sp.simplify((s0*gam**2*v**2)/(s0*gam**2))),   # v^2
 'v0_limit': {'sigma_s(v=0)': str((s0*gam**2).subs(v, 0)), 'P(v=0)': str((s0*gam**2*v**2).subs(v, 0))},
 # matching algebra: sigma-eq demands sigma0 = sigma_L / gamma^2 = sigma_L (1-v^2);
 # P-eq demands v^2 = P_L / sigma_L. Both stated symbolically for the symmetric row:
 'sigma0_required_symmetric': str(sp.simplify(sig_sym*(1-v**2))),
 'v2_required_symmetric': str(sp.simplify(P_sym/sig_sym)),
}
# sign of v2_required on admissible domain a>r+ (=> a>M, f>0): P_sym>0, sig_sym<0 => ratio<0
R['sympy']['v2_required_sign'] = ('P_L>0 and sigma_L<0 on a>r+ (a>M_i both sides, t_i>0) '
                                  '=> v2_required = P_L/sigma_L < 0: no real v, at any sigma0 sign')

# ============ helpers (float64) ============
def f_val(Mv, Qv, av): return 1.0 - 2.0*Mv/av + Qv**2/av**2
def lanczos(f1, M1v, f2, M2v, av):
    s1, s2 = np.sqrt(f1), np.sqrt(f2)
    sig = -(s1 + s2)/(4*np.pi*av)
    P = ((1-M1v/av)/s1 + (1-M2v/av)/s2)/(8*np.pi*av)
    return sig, P
def stream_ecs(sig_s, Ppar, Pperp):
    """ECs of S=diag(-sig_s,0,Pperp,Ppar)-type surface tensor (radial pressure 0)."""
    return {'NEC': bool(sig_s >= 0 and sig_s+Ppar >= 0 and sig_s+Pperp >= 0),
            'WEC': bool(sig_s >= 0 and sig_s+Ppar >= 0 and sig_s+Pperp >= 0),
            'SEC': bool(sig_s+Ppar >= 0 and sig_s+Pperp >= 0 and sig_s+Ppar+Pperp >= 0),
            'DEC': bool(sig_s >= 0 and abs(Ppar) <= sig_s and abs(Pperp) <= sig_s)}
def scan(spec, yvals, xvals, label):
    """spec(y) -> (f1, M1, f2, M2, rp_overall) arrays/scalars for charge parameter y."""
    tot = 0; n_sig_neg = n_P_pos = n_ratio_neg = n_sol = 0
    min_ratio, max_ratio = 1e300, -1e300; min_sig = 1e300; min_P = 1e300; max_P = -1e300
    for y in yvals:
        f1, M1v, f2, M2v, rp = spec(y, xvals)
        xs = xvals[xvals > rp*1.000001]
        if len(xs) == 0: continue
        keep = xvals > rp*1.000001
        sig, P = lanczos(f1[keep], M1v, f2[keep], M2v, xs)
        tot += len(xs)
        n_sig_neg += int(np.sum(sig < 0)); n_P_pos += int(np.sum(P > 0))
        ratio = P/sig
        n_ratio_neg += int(np.sum(ratio < 0))
        # solution test: need sigma0 = sig*(1-v^2) > 0 AND v^2 = ratio in [0, 0.25]
        n_sol += int(np.sum((sig > 0) & (ratio >= 0) & (ratio <= 0.25)))
        min_ratio = min(min_ratio, float(np.min(ratio))); max_ratio = max(max_ratio, float(np.max(ratio)))
        min_sig = min(min_sig, float(np.min(sig))); min_P = min(min_P, float(np.min(P))); max_P = max(max_P, float(np.max(P)))
    return {'grid': label, 'points': int(tot), 'sigma_L<0': int(n_sig_neg), 'P_L>0': int(n_P_pos),
            'ratio_P/sigma<0': int(n_ratio_neg), 'stream_solutions_both_eqs': int(n_sol),
            'ratio_min': min_ratio, 'ratio_max': max_ratio, 'min_sigma_L_times_M': min_sig,
            'P_L_times_M_range': [min_P, max_P],
            'M1_theta_inconsistency': 'P_theta,Lanczos - 0 = P_L (never 0 on grid; range in P_L_times_M_range)'}

yvals = np.linspace(0.0, 0.999, 400); xvals = np.linspace(1.001, 50.0, 800)
def rp_of(Qv): return 1.0 + np.sqrt(max(0.0, 1-Qv*Qv))   # r_+/M for M=1
R['grids'] = {
 'symmetric_Schwarzschild_Q0': scan(lambda y, x: (f_val(1.0, 0.0, x), 1.0, f_val(1.0, 0.0, x), 1.0, 2.0), [0.0], xvals, 'sym Schw'),
 'symmetric_RN': scan(lambda y, x: (f_val(1.0, y, x), 1.0, f_val(1.0, y, x), 1.0, rp_of(y)), yvals, xvals, 'sym RN'),
 'asym_RN-Schw': scan(lambda y, x: (f_val(1.0, y, x), 1.0, f_val(1.0, 0.0, x), 1.0, max(rp_of(y), 2.0)), yvals[::2], xvals, 'RN-Schw'),
 'asym_RN-Mink': scan(lambda y, x: (f_val(1.0, y, x), 1.0, np.ones_like(x), 0.0, rp_of(y)), yvals[::2], xvals, 'RN-Mink'),
 'asym_RN-RNdQ': scan(lambda y, x: (f_val(1.0, y, x), 1.0, f_val(1.0, 0.5*y, x), 1.0, max(rp_of(y), rp_of(0.5*y))), yvals[::2], xvals, 'RN-RN(0.5Q)'),
}

# ============ 2. v=0 CONTROL: static identity reproduced exactly ============
xs = np.linspace(2.000001, 50.0, 2000)
sig_c, P_c = lanczos(f_val(1.0, 0.0, xs), 1.0, f_val(1.0, 0.0, xs), 1.0, xs)
sig_P23 = -np.sqrt(1-2.0/xs)/(2*np.pi*xs)   # M=1: sigma=-s/(2 pi a), s=sqrt(1-2M/a)
R['v0_control'] = {'max_abs_err_sigma_vs_P23_identity': float(np.max(np.abs(sig_c - sig_P23))),
 'sigma0_required_at_v0': 'sigma_L < 0 on all 2000 control points (static failure reproduced)',
 'sigma_L<0_count': int(np.sum(sig_c < 0)), 'points': int(len(xs)),
 'P_mismatch_at_v0': 'streams give P=0; Lanczos demands P_L>0 on all control points',
 'P_L>0_count': int(np.sum(P_c > 0))}

# ============ 3. STREAM-TENSOR ECs (sigma0>0, v<=0.5) ============
ec = {}
for model in ['M1', 'M2']:
    allpass = True; worst = {}
    for vv in np.linspace(0.0, 0.5, 51):
        g2 = 1.0/(1.0-vv*vv); ss = 1.0*g2  # sigma0=1
        Pp = ss*vv*vv; Pt = 0.0 if model == 'M1' else ss*vv*vv
        e = stream_ecs(ss, Pp, Pt)
        allpass &= all(e.values())
        worst = {'v': float(vv), 'sigma_s/sigma0': float(ss), 'P_parallel/sigma_s': float(vv*vv), **e}
    ec[model] = {'all_EC_pass_all_v_in_[0,0.5]_sigma0>0': bool(allpass), 'sample_v=0.5': worst}
R['stream_ECs'] = ec
# ECs of the tensor Lanczos actually demands (sigma_L, P_L): fails NEC/WEC/DEC since sigma_L<0
R['lanczos_tensor_ECs'] = 'fail on every grid point: sigma_L<0 violates NEC (sigma>=0 clause), WEC, DEC'

# ============ 4. POISSON-VISSER STABILITY, beta0^2 = v^2 (P33-1 machinery, gated) ============
def Vpp_RN(a0v, Mv, Qv, beta2v):
    f = f_val(Mv, Qv, a0v); fp = 2*Mv/a0v**2 - 2*Qv**2/a0v**3; fpp = -4*Mv/a0v**3 + 6*Qv**2/a0v**4
    s = np.sqrt(f); sig0 = -s/(2*np.pi*a0v); P0v = (1-Mv/a0v)/(4*np.pi*a0v*s)
    sigp = -2*(sig0+P0v)/a0v; gp = -2*np.pi*(sig0+2*P0v)
    sigpp = -2*sigp*(1+beta2v)/a0v + 2*(sig0+P0v)/a0v**2; gpp = -2*np.pi*sigp*(1+2*beta2v)
    return fpp - 2*(gp**2 + (-s)*gpp)
def Vpp_P23(x, b2): return (-4*(2*x-3)*(x-1)*b2 - (4*x*x-6*x+3))/(2*x*(x-1))
gate = max(abs(((2*xv)**2)*Vpp_RN(2*xv, 1.0, 0.0, bv) - Vpp_P23(xv, bv))
           for xv in [1.1, 1.5, 2.0, 3.0, 5.0, 10.0] for bv in [0.0, 0.13, 0.25, 1.0])
stab = {'Q0_gate_vs_P23_max_abs_err': float(gate), 'rows': {}}
v2_stream = np.linspace(0.0, 0.25, 11)   # beta0^2 = v^2, v<=0.5
for Qv in [0.0, 0.5, 0.9, 0.99]:
    rp = 1.0 + np.sqrt(max(0.0, 1-Qv*Qv)); nrows = nstab = 0; best = -1e300
    for a0v in np.linspace(rp*1.001, 20.0, 120):
        nrows += 1
        mx = max(Vpp_RN(float(a0v), 1.0, Qv, float(b2)) for b2 in v2_stream)
        best = max(best, float(a0v)**2 * mx)
        if mx > 0: nstab += 1
    stab['rows'][f'Q/M={Qv}'] = {'a0_rows': nrows, 'rows_with_Vpp>0_for_some_stream_beta0sq_in_[0,0.25]': int(nstab),
                                 'max_a0^2_Vpp_over_stream_betas': best}
R['stability_stream_EoS'] = stab

# ============ 5. a=1 m reference rows + scale-free statement ============
c, G = 299792458.0, 6.67430e-11
refs = {}
for (lbl, Qv) in [('Q=0', 0.0), ('Q=0.9', 0.9)]:
    av, Mv = 1.0, 0.25   # x = a/(2M) = 2
    f = f_val(Mv, Qv*Mv, av); sig, P = lanczos(f, Mv, f, Mv, av)
    refs[lbl] = {'a_m': 1.0, 'x': 2.0, 'sigma_L_geom_per_m': float(sig), 'P_L_geom_per_m': float(P),
                 'sigma_L_kg_per_m2': float(sig*c*c/G), 'ratio_P/sigma': float(P/sig),
                 'sigma0_required(v=0.5)_kg_per_m2': float(sig*(1-0.25)*c*c/G),
                 'v2_required': float(P/sig)}
R['a_eq_1m_rows'] = refs
R['scale_free'] = ('sigma_L*M and P_L*M depend only on (a/M, Q/M): the sign failure '
                   '(sigma_L<0, P_L/sigma_L<0) is scale-free; a=1 m rows are instances, not a scale effect.')

R['verdict'] = 'FAIL'
R['deciding_combination'] = (
 'BOTH Lanczos equations fail independently, in both models M1 and M2, on every grid point: '
 '(1) sigma-equation: sigma_L = -(sqrt(f_+)+sqrt(f_-))/(4 pi a) < 0 demands sigma_s<0, but streams give '
 'sigma_s = sigma0 gamma^2 >= 0 for sigma0>0 (sigma0 required = sigma_L(1-v^2) < 0 for all v in [0,0.5]); '
 '(2) pressure/ratio equation: streams require P/sigma_s = v^2 >= 0 (and <=0.25), but the throat pair has '
 'P_L/sigma_L < 0 on every grid point (P_L>0, sigma_L<0) -- v^2_required is negative, no real v exists '
 'even if the sigma sign were waived. M1 additionally fails theta-theta: P_theta,Lanczos = P_L > 0 vs demanded 0. '
 'Stream tensor itself is EC-legal for sigma0>0 (all four ECs, both models, all v<=0.5): the failure is '
 'purely the Lanczos matching. Stability moot (no solution sequence) and independently empty: Vpp>0 on 0 rows '
 'for stream beta0^2=v^2 in [0,0.25].')

with open(os.path.join(OUT, "p353_results.json"), "w") as fh: json.dump(R, fh, indent=1)
print(json.dumps({k: R[k] for k in ['sympy', 'v0_control', 'verdict']}, indent=1)[:1500])
print("grids:", {k: (g['points'], g['stream_solutions_both_eqs'], g['ratio_max']) for k, g in R['grids'].items()})
print("stab:", R['stability_stream_EoS']['Q0_gate_vs_P23_max_abs_err'],
      {k: v2['rows_with_Vpp>0_for_some_stream_beta0sq_in_[0,0.25]'] for k, v2 in R['stability_stream_EoS']['rows'].items()})
print("stream ECs pass:", {k: v2['all_EC_pass_all_v_in_[0,0.5]_sigma0>0'] for k, v2 in R['stream_ECs'].items()})
