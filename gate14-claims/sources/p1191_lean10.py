#!/usr/bin/env python
"""P119-1 lean N=10 path: dense H + dense protocol simulation for energies
(identical operators to p1191_eval), ground state by sparse Lanczos
eigendecomposition of the constructed H, S(t) by the derived pair-block
exact exponentiation (p1191_asymptotics.derived_S_factory).
Used only where the full dense-eigh route exceeded the runtime window
under contention; validated against dense tau reads at (10,1,0.5) and
(10,1,1) before its (10,1,2) read is believed.
"""
import itertools, json, sys
import numpy as np
from scipy.sparse.linalg import eigsh, LinearOperator
import importlib.util
spec = importlib.util.spec_from_file_location("ev", "p1191_eval.py")
ev = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev)
spec2 = importlib.util.spec_from_file_location("asym", "p1191_asymptotics.py")
asym = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(asym)

FR = ev.FR

def lean_row(N, m, r):
    assert m == 1
    h = 1.0; k = r
    H, Hi, V, D = ev.build(N, h, k)
    dim = 2**N
    # ground state: Lanczos eigendecomposition of constructed H + Eq.(3)
    Hsp = LinearOperator((dim, dim), matvec=lambda x: H @ x, dtype=float)
    vals, vecs = eigsh(Hsp, k=1, which="SA", tol=1e-13, maxiter=10000)
    E_ground = float(vals[0])
    g = ev.ground_eq3(N, h, k, D)
    overlap = float(abs(np.vdot(vecs[:, 0], g))**2)
    outputs = list(range(N-m, N)); inputs = list(range(0, N-m))
    Sop = sum(Hi[i] for i in outputs) + V
    E_in_cf = (N-m)*N*h**2/D
    A = N*m*h**2 + 4*k**2
    E_out_cf = A/D*(np.sqrt(1 + (2*(N-m)*h*k)**2/A**2) - 1)
    den = np.sqrt(A**2 + (2*(N-m)*h*k)**2)
    theta = 0.5*np.arctan2(2*(N-m)*h*k, A)
    gt = np.zeros([2]*N, dtype=complex); gt[(0,)*N] = g[0]; gt[(1,)*N] = g[-1]
    def apply_P(t, j, aj):
        return 0.5*(t + aj*np.flip(t, axis=j))
    def apply_O(t):
        u = np.flip(t, axis=outputs[0])
        sl0 = [slice(None)]*N; sl1 = [slice(None)]*N
        sl0[outputs[0]] = 0; sl1[outputs[0]] = 1
        w = np.empty_like(u)
        w[tuple(sl0)] = -1j*u[tuple(sl0)]; w[tuple(sl1)] = 1j*u[tuple(sl1)]
        for o in outputs[1:]:
            w = np.flip(w, axis=o)
        return w
    comps_meas, comps_post = [], []
    for alpha in itertools.product([1, -1], repeat=N-m):
        phi_t = gt
        for j, aj in zip(inputs, alpha):
            phi_t = apply_P(phi_t, j, aj)
        phi = phi_t.reshape(-1)
        comps_meas.append(phi)
        atot = int(np.prod(alpha))
        comps_post.append(np.cos(theta)*phi - 1j*atot*np.sin(theta)*apply_O(phi_t).reshape(-1))
    Pm = np.array(comps_meas).T; Pp = np.array(comps_post).T
    prob = float(np.sum(np.abs(Pm)**2))
    E_in_sim = float(np.sum(np.conj(Pm)*(H @ Pm)).real)
    S0 = float(np.sum(np.conj(Pp)*(Sop @ Pp)).real)
    E_out_sim = -S0
    a2 = (1 - N*h/D)/2; b2 = (1 + N*h/D)/2
    rho1 = np.diag([a2, b2]).astype(complex)
    rho_marg = np.array([[1.0+0j]])
    for _ in range(N):
        rho_marg = np.kron(rho_marg, rho1)
    E_prep_mat = float(np.trace(rho_marg @ Sop).real)
    E_prep = 4*k**2/D
    E_net = E_prep - E_out_cf
    S, _ = asym.derived_S_factory(N, r)
    tau0 = asym.first_return(S, 0.0)
    tau_marg = asym.first_return(S, E_prep)
    def Rof(tau):
        return abs(E_net)*tau/FR if (E_net < 0 and tau) else 0.0
    return {"N": N, "m": m, "r": r, "h": h, "k": k,
            "E_ground_eig": E_ground, "ground_overlap_eq3": overlap,
            "prob_sum": prob, "E_in": E_in_cf, "E_in_sim": E_in_sim,
            "E_out": E_out_cf, "E_out_sim": E_out_sim,
            "E_prep_marg": E_prep, "E_prep_marg_matrix": E_prep_mat,
            "E_net_B": E_net, "tau0": tau0, "tau_marg": tau_marg,
            "R_tau0": Rof(tau0), "R_tau_marg": Rof(tau_marg),
            "price_per_unit": (E_prep + E_in_cf)/E_out_cf, "S0": S0,
            "route": "lean: dense H + Lanczos ground + pair-block S(t)"}

if __name__ == "__main__":
    for rr in (0.5, 1.0, 2.0):
        row = lean_row(10, 1, rr)
        fn = f"/tmp/p1191_part_10lean_{rr}.json"
        json.dump({"rows": [row]}, open(fn, "w"), indent=1, default=float)
        print(f"r={rr}: E_out={row['E_out']:.12g} sim={row['E_out_sim']:.12g} E_net={row['E_net_B']:.12g} "
              f"tau0={row['tau0']} taum={row['tau_marg']} R0={row['R_tau0']:.6g} Rm={row['R_tau_marg']:.6g} "
              f"Egr={row['E_ground_eig']:.2e} ovl={row['ground_overlap_eq3']:.12f}", flush=True)
