#!/usr/bin/env python
"""P119-1 fresh evaluation machinery, written from Xun & Ren arXiv:2410.04919.

Dense Kronecker construction of H from Eqs.(1)-(2); ground state by
eigendecomposition AND Eq.(3); protocol simulated explicitly (projectors
Eq.(4) on the N-m input qubits, conditional unitaries Eq.(7) with optimal
theta Eq.(10)); E_out cross-checked against closed form Eq.(11); E_in
Eq.(6) cross-checked by simulation; S(t) by exact exponentiation via the
eigendecomposition, frequency-grouped. float64 throughout.
Does NOT read any Phase 108 code or results.
"""
import itertools, json, sys
import numpy as np
from scipy.optimize import brentq

FR = 3.0/(32.0*np.pi**2)
sx = np.array([[0.,1.],[1.,0.]]); sy = np.array([[0.,-1j],[1j,0.]])
sz = np.array([[1.,0.],[0.,-1.]]); I2 = np.eye(2)

def op_on(single, j, N):
    out = np.array([[1.0]])
    for q in range(N):
        out = np.kron(out, single if q==j else I2)
    return out

def prod_op(singles, N):
    out = np.array([[1.0]])
    for q in range(N):
        out = np.kron(out, singles[q])
    return out

def build(N, h, k):
    # H, H_i, V are real symmetric in the paper's Eqs.(1)-(2) (only
    # sigma^z and products of sigma^x appear); build them in float64.
    D = np.sqrt(N**2*h**2 + 4*k**2)
    dim = 2**N
    Hi = []
    for i in range(N):
        Hi.append(h*op_on(sz, i, N).real + (N*h**2/D)*np.eye(dim))
    V = 2*k*prod_op([sx]*N, N).real + (4*k**2/D)*np.eye(dim)
    H = sum(Hi) + V
    return H, Hi, V, D

def ground_eq3(N, h, k, D):
    g = np.zeros(2**N, dtype=complex)
    a = np.sqrt(1 - N*h/D)/np.sqrt(2); b = np.sqrt(1 + N*h/D)/np.sqrt(2)
    g[0] = a; g[-1] = -b
    return g

def run_row(N, m, r, tmax=30.0):
    h = 1.0; k = r*h
    H, Hi, V, D = build(N, h, k)
    dim = 2**N
    evals, evecs = np.linalg.eigh(H)
    E_ground = float(evals[0])
    g_eig = evecs[:, 0]
    g = ground_eq3(N, h, k, D)
    overlap = abs(np.vdot(g_eig, g))**2
    # align phase and compare directly too
    # sector: output qubits' H_i + V (paper App. pattern, Eqs.28/39)
    outputs = list(range(N-m, N)); inputs = list(range(0, N-m))
    Sop = sum(Hi[i] for i in outputs) + V
    # closed forms
    E_in_cf = (N-m)*N*h**2/D
    A = N*m*h**2 + 4*k**2
    E_out_cf = A/D*(np.sqrt(1 + (2*(N-m)*h*k)**2/A**2) - 1)
    # optimal theta Eq.(10)
    den = np.sqrt(A**2 + (2*(N-m)*h*k)**2)
    c2, s2 = A/den, 2*(N-m)*h*k/den
    theta = 0.5*np.arctan2(s2, c2)
    # (the Eq.(7) unitary's action is applied tensor-wise below)
    # protocol simulation: projectors Eq.(4) and unitary Eq.(7) applied
    # explicitly as tensor (axis) operations on the state -- the same
    # operators as the dense matrices, applied axis-wise for speed.
    gt = np.zeros([2]*N, dtype=complex)
    gt[(0,)*N] = g[0]; gt[(1,)*N] = g[-1]
    def apply_P(t, j, aj):
        return 0.5*(t + aj*np.flip(t, axis=j))
    def apply_O(t):
        # sigma^y on first output axis, sigma^x on remaining output axes
        u = np.flip(t, axis=outputs[0])
        # sy: new[..0..] = -i*old[..1..], new[..1..] = i*old[..0..]
        sl0 = [slice(None)]*N; sl1 = [slice(None)]*N
        sl0[outputs[0]] = 0; sl1[outputs[0]] = 1
        w = np.empty_like(u)
        w[tuple(sl0)] = -1j*u[tuple(sl0)]; w[tuple(sl1)] = 1j*u[tuple(sl1)]
        for o in outputs[1:]:
            w = np.flip(w, axis=o)
        return w
    comps_meas, comps_post = [], []
    for alpha in itertools.product([1,-1], repeat=N-m):
        phi_t = gt
        for j, aj in zip(inputs, alpha):
            phi_t = apply_P(phi_t, j, aj)
        phi = phi_t.reshape(-1)
        comps_meas.append(phi)
        atot = int(np.prod(alpha))
        psi = np.cos(theta)*phi - 1j*atot*np.sin(theta)*apply_O(phi_t).reshape(-1)
        comps_post.append(psi)
    prob = sum(float(np.vdot(p,p).real) for p in comps_meas)
    Pm = np.array(comps_meas).T
    E_in_sim = float(np.sum(np.conj(Pm)*(H @ Pm)).real)
    Pp = np.array(comps_post).T
    S0 = float(np.sum(np.conj(Pp)*(Sop @ Pp)).real)
    E_out_sim = -S0
    # E_prep^(marg): marginal-product state, matrix form
    a2 = (1 - N*h/D)/2; b2 = (1 + N*h/D)/2
    rho1 = np.diag([a2, b2]).astype(complex)
    rho_marg = np.array([[1.0+0j]])
    for _ in range(N):
        rho_marg = np.kron(rho_marg, rho1)
    E_prep_mat = float(np.trace(rho_marg @ Sop).real)
    E_prep_cf = 4*k**2/D
    E_prep = E_prep_cf
    E_net = E_prep - E_out_cf
    # S(t): grouped frequencies in eigenbasis
    Sop_e = evecs.T @ Sop @ evecs
    Psi = np.array(comps_post).T  # dim x ncomp
    Cmat = evecs.T @ Psi
    M = Sop_e * (np.conj(Cmat) @ Cmat.T)
    freqs = {}
    Ea = evals
    F = Ea[:, None] - Ea[None, :]
    keys = np.round(F, 8)
    # group via dict on unique keys
    uniq, inv = np.unique(keys, return_inverse=True)
    coeff = np.zeros(len(uniq), dtype=complex)
    np.add.at(coeff, inv.ravel(), M.ravel())
    def S(t):
        return float(np.real(np.sum(coeff*np.exp(1j*uniq*t))))
    assert abs(S(0.0) - S0) < 1e-8*max(1, abs(S0)), (S(0.0), S0)
    def first_return(level, tmax):
        ts = np.arange(1e-4, tmax+1e-12, 0.002)
        vals = np.real(np.exp(1j*np.outer(uniq, ts)).T @ coeff) - level
        sgn = np.sign(vals)
        idx = np.nonzero(sgn[:-1]*sgn[1:] <= 0)[0]
        # exclude sign changes that are just touching zero at a gridpoint with same sign both sides:
        for i in idx:
            if vals[i] == 0.0:
                return float(ts[i])
            if (vals[i] < 0) != (vals[i+1] < 0):
                return float(brentq(lambda x: S(x)-level, ts[i], ts[i+1], xtol=1e-13, rtol=1e-13))
        return None
    tau0 = first_return(0.0, tmax)
    tau_marg = first_return(E_prep, tmax)
    def Rof(tau):
        if E_net >= 0 or tau is None:
            return 0.0
        return abs(E_net)*tau/FR
    return {
        "N": N, "m": m, "r": r, "h": h, "k": k,
        "E_ground_eig": E_ground, "ground_overlap_eq3": float(overlap),
        "prob_sum": prob,
        "E_in": E_in_cf, "E_in_sim": E_in_sim,
        "E_out": E_out_cf, "E_out_sim": E_out_sim,
        "E_prep_marg": E_prep, "E_prep_marg_matrix": E_prep_mat,
        "E_net_B": E_net,
        "tau0": tau0, "tau_marg": tau_marg,
        "R_tau0": Rof(tau0), "R_tau_marg": Rof(tau_marg),
        "price_per_unit": (E_prep + E_in_cf)/E_out_cf,
        "S0": S0,
    }

CONFIGS = [(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(6,1),(8,1),(10,1)]
if __name__ == "__main__":
    # usage: p1191_eval.py OUTFILE [N:m ...]  (default: all configs)
    outfile = sys.argv[1] if len(sys.argv) > 1 else "/tmp/p1191_fresh.json"
    if len(sys.argv) > 2:
        CONFIGS = [tuple(int(x) for x in s.split(":")) for s in sys.argv[2:]]
    rows = []
    for (N, m) in CONFIGS:
        for r in (0.5, 1.0, 2.0):
            row = run_row(N, m, r)
            rows.append(row)
            print(f"N={N} m={m} r={r}: E_out={row['E_out']:.12g} sim={row['E_out_sim']:.12g} "
                  f"E_prep={row['E_prep_marg']:.12g} mat={row['E_prep_marg_matrix']:.12g} "
                  f"E_net={row['E_net_B']:.12g} tau0={row['tau0']} taum={row['tau_marg']} "
                  f"R0={row['R_tau0']:.6g} Rm={row['R_tau_marg']:.6g} "
                  f"Egr={row['E_ground_eig']:.2e} ovl={row['ground_overlap_eq3']:.12f}", flush=True)
    with open(outfile, "w") as f:
        json.dump({"rows": rows}, f, indent=1)
    print("WROTE", outfile)
