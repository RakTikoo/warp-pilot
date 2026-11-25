#!/usr/bin/env python
"""P119-1 tau(N) asymptotics: derived evolution for m=1, any N.

Derivation (from the paper's Eqs.(1)-(3),(7),(10), stated in run record):
H couples only complementary basis pairs {s, ~s}: in that basis
H = D*I + [[d, 2k],[2k, -d]], d = h(N-2|s|), Omega = sqrt(d^2+4k^2),
so evolution inside a pair is a closed 2x2 rotation and every pair's
sector expectation is a trig polynomial q0 + qc cos(2 Om t) + qs sin(2 Om t).
The post-protocol amplitudes for outcome alpha are, with x the input-bit
config, chi_x(alpha) = prod_{j in x} alpha_j, a' = a 2^{-(N-1)}, b' likewise:
  A0(x) = a' chi_x,  A1(x) = -b' chi_{~x}  (pre-unitary amplitudes)
and the conditional unitary collapses these to B0(x) = u chi_x,
B1(x) = v chi_{~x} with u = a' cos(theta) + b' sin(theta),
v = a' sin(theta) - b' cos(theta), independent of x.
Summing the quadratic S(t) over all alpha kills every chi_x chi_{~x}
cross term (sum_alpha chi_full = 0) and gives sum_alpha chi_x^2 =
2^{N-1}; the surviving coefficients depend on x only through w = |x|,
so S(t) is an O(N) sum over w with binomial weights C(N-1, w).
Validated against the dense machinery (p1191_eval) at several N.
"""
import json
import numpy as np
from scipy.optimize import brentq
from math import comb

FR = 3.0/(32.0*np.pi**2)

def _pair_trig(d1, sd1, sd2, k, vgroups):
    """Return (Om, q0, qc, qs): sum over v-groups of v^dag U(t)^dag Sop U(t) v
    as q0 + qc cos(2 Om t) + qs sin(2 Om t). Extracted from Q(0), Q(pi/(4 Om)),
    Q(pi/(2 Om)) of the exact 2x2 evolution."""
    Om = np.sqrt(d1**2 + 4*k**2)
    def Q(t):
        c = np.cos(Om*t); s = np.sin(Om*t)/Om
        U = np.array([[c - 1j*s*d1, -1j*s*2*k], [-1j*s*2*k, c + 1j*s*d1]])
        Sop = np.array([[sd1, 2*k], [2*k, sd2]], dtype=complex)
        Mt = U.conj().T @ Sop @ U
        tot = 0.0
        for v in vgroups:
            vv = np.array(v, dtype=complex)
            tot += float(np.real(vv.conj() @ Mt @ vv))
        return tot
    Q0 = Q(0.0); Q1 = Q(np.pi/(4*Om)); Q2 = Q(np.pi/(2*Om))
    q0 = 0.5*(Q0 + Q2); qc = 0.5*(Q0 - Q2); qs = Q1 - q0
    return Om, q0, qc, qs

def derived_S_factory(N, r):
    h = 1.0; k = r
    D = np.sqrt(N**2 + 4*k**2)
    a = np.sqrt(1 - N/D)/np.sqrt(2); b = np.sqrt(1 + N/D)/np.sqrt(2)
    A = N + 4*k**2
    theta = 0.5*np.arctan2(2*(N-1)*k, A)
    ct, st = np.cos(theta), np.sin(theta)
    Cs = N/D + 4*k**2/D
    E_prep = 4*k**2/D
    # Projector amplitudes (Eq.(4) on Eq.(3)): A0(x) = a' chi_x,
    # A1(x) = -b' chi_{~x} with a' = a 2^{-(N-1)}, b' = b 2^{-(N-1)}.
    # The Eq.(7) unitary (alpha_tot = chi_full) collapses these to
    #   B0(x) = u chi_x,  B1(x) = v chi_{~x},
    #   u = a' ct + b' st,  v = a' st - b' ct  (w-independent).
    ap = a*2**(-(N-1)); bp = b*2**(-(N-1))
    u = ap*ct + bp*st; v = ap*st - bp*ct
    const = 0.0
    terms = {}  # freq (2*Om) -> [qc, qs]
    for w in range(N):
        cnt = comb(N-1, w)
        # P1: (x,0)/(~x,1), amplitudes chi_x (u, v); d1 = N-2w; diag (+1+Cs, -1+Cs)
        Om, q0, qc, qs = _pair_trig(float(N-2*w), 1.0+Cs, -1.0+Cs, k, ((u, v),))
        const += cnt*q0
        e = terms.setdefault(2*Om, [0.0, 0.0]); e[0] += cnt*qc; e[1] += cnt*qs
        # P2: (x,1)/(~x,0), amplitudes chi_{~x} (v, u); d1 = N-2(w+1); diag (-1+Cs, +1+Cs)
        Om, q0, qc, qs = _pair_trig(float(N-2*(w+1)), -1.0+Cs, 1.0+Cs, k, ((v, u),))
        const += cnt*q0
        e = terms.setdefault(2*Om, [0.0, 0.0]); e[0] += cnt*qc; e[1] += cnt*qs
    scale = 0.5 * (2**(N-1))
    freqs = np.array(sorted(terms.keys()))
    qcs = np.array([terms[f][0] for f in freqs])*scale
    qss = np.array([terms[f][1] for f in freqs])*scale
    const = const*scale
    def S(t):
        t = np.asarray(t, dtype=float)
        ph = np.outer(freqs, t.ravel())
        vals = const + qcs @ np.cos(ph) + qss @ np.sin(ph)
        return float(vals.flat[0]) if np.ndim(t) == 0 else vals.reshape(np.shape(t))
    return S, E_prep

def first_return(S, level, tmax=30.0, step=0.002):
    ts = np.arange(1e-4, tmax+1e-12, step)
    vals = S(ts) - level
    for i in range(len(ts)-1):
        if vals[i] == 0.0:
            return float(ts[i])
        if (vals[i] < 0) != (vals[i+1] < 0):
            return float(brentq(lambda x: S(x)-level, ts[i], ts[i+1], xtol=1e-13, rtol=1e-13))
    return None

def closed(N, r):
    D = np.sqrt(N**2 + 4*r**2)
    E_prep = 4*r**2/D
    A = N + 4*r**2
    E_out = A/D*(np.sqrt(1 + (2*(N-1)*r)**2/A**2) - 1)
    return E_prep, E_out, E_prep - E_out

if __name__ == "__main__":
    out = {"validation": [], "asymptotics": []}
    for (N, r) in [(3, 0.5), (5, 1.0), (8, 0.5), (10, 0.5), (10, 1.0)]:
        S, E_prep = derived_S_factory(N, r)
        Ep, Eo, En = closed(N, r)
        err0 = abs(S(0.0) - (-Eo))
        rec = {"N": N, "r": r, "S0_minus_negEout": err0,
               "tau0_derived": first_return(S, 0.0),
               "tau_marg_derived": first_return(S, E_prep)}
        out["validation"].append(rec)
        print(f"validate N={N} r={r}: |S(0)+E_out|={err0:.3e} tau0={rec['tau0_derived']} taum={rec['tau_marg_derived']}", flush=True)
    for r in (0.5, 1.0):
        for N in [2,3,4,5,6,8,10,12,16,20,30,50,80,120,200]:
            S, E_prep = derived_S_factory(N, r)
            Ep, Eo, En = closed(N, r)
            t0 = first_return(S, 0.0); tm = first_return(S, E_prep)
            R0 = abs(En)*t0/FR if (En < 0 and t0) else 0.0
            Rm = abs(En)*tm/FR if (En < 0 and tm) else 0.0
            row = {"N": N, "r": r, "E_prep": Ep, "E_out": Eo, "E_net_B": En,
                   "tau0": t0, "tau_marg": tm, "R_tau0": R0, "R_tau_marg": Rm}
            out["asymptotics"].append(row)
            print(f"asym N={N} r={r}: E_net={En:.6g} tau0={t0} taum={tm} R0={R0:.4g} Rm={Rm:.4g}", flush=True)
    with open("/tmp/p1191_asym.json", "w") as f:
        json.dump(out, f, indent=1)
    print("WROTE /tmp/p1191_asym.json")
