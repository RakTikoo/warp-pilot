"""Gate-14 fresh evaluation of Xun & Ren arXiv:2410.04919 N-qubit QET.

Written for Gate-14 from the published paper's equations only:
  H  Eqs.(1)-(2); ground state Eq.(3); projectors Eq.(4);
  E_in Eq.(6); conditional unitary Eq.(7); optimal theta Eq.(10);
  E_out Eq.(11) (closed-form cross-check of the explicit simulation).
Accounting inherited verbatim (Phase 72 S3-S4 via Phase 106/108):
  sector = output qubits' H_i + V entire; E_prep^(marg) = sector energy
  of the marginal-product state above the ground sector value (0);
  E_net,B = E_prep^(marg) - E_out; R = |E_net,B| * tau / (3/(32 pi^2))
  when E_net,B < 0 else 0; tau0 = first t>0 with S(t)=0;
  tau_marg = first t>0 with S(t)=+E_prep^(marg) (search t<=30).
No Phase 108/119 code is used.
"""
import json, math, itertools
import numpy as np
from scipy.optimize import brentq

I2 = np.eye(2)
X = np.array([[0., 1.], [1., 0.]])
Y = np.array([[0., -1j], [1j, 0.]])
Z = np.diag([1., -1.])
FR = 3.0 / (32.0 * math.pi ** 2)

def kron_all(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out

def single(N, i, P):
    return kron_all([P if j == i else I2 for j in range(N)])

def build(N, h, k):
    D = math.sqrt(N * N * h * h + 4 * k * k)
    dim = 2 ** N
    Hi = []
    for i in range(N):
        Hi.append(h * single(N, i, Z) + (N * h * h / D) * np.eye(dim))
    Vall = 2 * k * kron_all([X] * N) + (4 * k * k / D) * np.eye(dim)
    H = sum(Hi) + Vall
    return D, Hi, Vall, H

def ground_state(N, h, D):
    dim = 2 ** N
    g = np.zeros(dim, dtype=complex)
    g[0] = math.sqrt(1 - N * h / D) / math.sqrt(2)
    g[dim - 1] = -math.sqrt(1 + N * h / D) / math.sqrt(2)
    return g

def sector_op(N, m, Hi, Vall):
    S = Vall.copy()
    for i in range(N - m, N):
        S = S + Hi[i]
    return S

def e_prep_marg(N, h, D, S_op):
    p0 = (1 - N * h / D) / 2.0
    p1 = (1 + N * h / D) / 2.0
    rho1 = np.diag([p0, p1]).astype(complex)
    rho = kron_all([rho1] * N)
    return float(np.real(np.trace(rho @ S_op)))

def run_row(N, m, r):
    h = 1.0
    k = r * h
    D, Hi, Vall, H = build(N, h, k)
    dim = 2 ** N
    g = ground_state(N, h, D)
    evals, evecs = np.linalg.eigh(H.real)
    e_ground = float(evals[0])
    g_eig = evecs[:, 0]
    if np.dot(g_eig, g.real) < 0:
        g_eig = -g_eig
    overlap = abs(np.vdot(g_eig, g)) ** 2
    S_op = sector_op(N, m, Hi, Vall)
    Ep_marg_matrix = e_prep_marg(N, h, D, S_op)
    Ep_marg = 4 * k * k / D
    # optimal theta, Eq.(10)
    A = N * m * h * h + 4 * k * k
    B = 2 * (N - m) * h * k
    norm = math.hypot(A, B)
    cos2, sin2 = A / norm, B / norm
    theta = 0.5 * math.atan2(sin2, cos2)
    # explicit protocol simulation: Eq.(4) projectors and the Eq.(7)
    # conditional unitary applied axis-wise to the state tensor
    # (identical operators; application route only).
    n_in = N - m
    rho_post = np.zeros((dim, dim), dtype=complex)
    E_in_sim = 0.0
    E_out_sim = 0.0
    def apply_1q(vec, q, mat):
        t = vec.reshape([2] * N)
        t = np.tensordot(mat, t, axes=([1], [q]))
        t = np.moveaxis(t, 0, q)
        return t.reshape(dim)
    for alpha in itertools.product([1, -1], repeat=n_in):
        psi = g.copy()
        for j, a in enumerate(alpha):
            psi = apply_1q(psi, j, 0.5 * (I2 + a * X))
        E_in_sim += float(np.real(np.vdot(psi, H @ psi)))
        aprod = int(np.prod(alpha))
        mvec = apply_1q(psi, n_in, Y)
        for i in range(n_in + 1, N):
            mvec = apply_1q(mvec, i, X)
        psi2 = math.cos(theta) * psi - 1j * aprod * math.sin(theta) * mvec
        E_out_sim -= float(np.real(np.vdot(psi2, S_op @ psi2)))
        rho_post += np.outer(psi2, psi2.conj())
    # closed forms, Eqs.(6),(11)
    E_in = (N - m) * N * h * h / D
    E_out = (A / D) * (math.sqrt(1 + (B / A) ** 2) - 1)
    E_net = Ep_marg - E_out
    # S(t): exact exponentiation via H eigenbasis, frequency-grouped
    W = evecs
    Arot = W.T @ rho_post.real @ W
    Brot = W.T @ S_op.real @ W
    C = Arot * Brot.T
    freqs = np.round((evals[:, None] - evals[None, :]).ravel(), 8)
    coeffs = C.ravel()
    uf, inv = np.unique(freqs, return_inverse=True)
    gc = np.zeros(len(uf))
    np.add.at(gc, inv, coeffs)
    def S(t):
        return float(np.dot(gc, np.cos(uf * t)))
    S0 = S(0.0)
    def first_return(target, tmax=30.0, dt=0.002):
        t_prev, v_prev = dt, S(dt) - target
        t = 2 * dt
        while t <= tmax + 1e-12:
            v = S(t) - target
            if v == 0.0:
                return float(t)
            if v_prev < 0 and v >= 0:
                return float(brentq(lambda x: S(x) - target, t_prev, t,
                                     xtol=1e-13, rtol=1e-13))
            t_prev, v_prev = t, v
            t += dt
        return None
    tau0 = first_return(0.0)
    tau_marg = first_return(Ep_marg)
    R0 = abs(E_net) * tau0 / FR if (E_net < 0 and tau0 is not None) else 0.0
    Rm = abs(E_net) * tau_marg / FR if (E_net < 0 and tau_marg is not None) else 0.0
    price_marg = (Ep_marg + E_in) / E_out
    return {
        "N": N, "m": m, "r": r, "h": h, "k": k, "D": D,
        "E_ground_eig": e_ground, "ground_overlap_eq3": float(overlap),
        "E_in": E_in, "E_in_sim": E_in_sim,
        "E_out": E_out, "E_out_sim": E_out_sim,
        "E_prep_marg": Ep_marg, "E_prep_marg_matrix": Ep_marg_matrix,
        "E_net_B": E_net, "S0": S0, "S0_plus_E_out_sim": S0 + E_out_sim,
        "tau0": tau0, "tau_marg": tau_marg,
        "R_tau0": R0, "R_tau_marg": Rm,
        "price_per_unit_marg": price_marg,
    }

def sep_min(N, r, n_starts=240, seed=1414):
    """Gate's own separable-minimum certificate for h=1:
    min over product states of <H> = sum_i (z_i) + N^2/D + 2k prod_i x_i + 4k^2/D,
    Bloch parametrisation x_i=sin(th_i), z_i=cos(th_i) (y drops out of H).
    Multi-start L-BFGS-B + the all-z=-1 corner candidate."""
    from scipy.optimize import minimize
    h = 1.0; k = r
    D = math.sqrt(N * N + 4 * k * k)
    const = (N * N + 4 * k * k) / D
    def E(th):
        return float(np.sum(np.cos(th)) + 2 * k * np.prod(np.sin(th)) + const)
    corner = E(np.full(N, math.pi))
    rng = np.random.default_rng(seed + N * 10 + int(r * 2))
    best = corner
    for s in range(n_starts):
        th0 = rng.uniform(-math.pi, math.pi, size=N) if s else np.full(N, math.pi)
        res = minimize(E, th0, method="L-BFGS-B")
        if res.fun < best:
            best = float(res.fun)
    return {"N": N, "r": r, "E_sep_multistart": best,
            "E_sep_corner_D_minus_N": float(D - N), "n_starts": n_starts}

def main():
    # RECOVERY COMPLETION (Gate-14 recovery coordinator, disclosed in
    # GATE14.md): the original main() covered only the 21 m=1 rows; the
    # registered row set is all 30 rows of p1085_results.json, which adds
    # (3,2), (4,2), (4,3). run_row is already m-general and every added
    # row carries the same internal cross-checks (simulation vs
    # Eqs.(6)/(11), Eq.(3) overlap, marginal matrix vs 4k^2/D).
    # RECOVERY RESILIENCE (same disclosure): two daemon/VM restarts
    # killed full runs before the single end-of-run JSON write. main()
    # now checkpoints results/g14_numbers.json after every row and
    # every SEP certificate and resumes from it, skipping completed
    # items. Numerics untouched: same run_row / sep_min, same SEP seed,
    # so resumed values are bit-identical to a single-run execution
    # (verified against the run2/run3 printed lines for the rows and
    # SEP certificates those runs completed).
    import os
    path = "results/g14_numbers.json"
    done_rows, done_sep = {}, {}
    if os.path.exists(path):
        prev = json.load(open(path))
        done_rows = {(r_["N"], r_["m"], r_["r"]): r_ for r_ in prev.get("rows", [])}
        done_sep = {tuple(s_["row"]): s_ for s_ in prev.get("sep_certificate", [])}

    def dump(rows_, sep_):
        prices_ = [s_["Pi_sep"] for s_ in sep_]
        out_ = {"model": "Gate-14 fresh machinery from Xun & Ren arXiv:2410.04919 Eqs.(1)-(11)",
                "FR_coef": FR, "rows": rows_, "sep_certificate": sep_,
                "price_deciding_range_sep": [min(prices_), max(prices_)] if prices_ else None}
        with open(path, "w") as f:
            json.dump(out_, f, indent=1)
        return out_

    rows = []
    configs = [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3),
               (5, 1), (6, 1), (8, 1), (10, 1)]
    for (N, m) in configs:
        for r in (0.5, 1.0, 2.0):
            if (N, m, r) in done_rows:
                row = done_rows[(N, m, r)]
                print(N, m, r, "RESUMED", flush=True)
            else:
                row = run_row(N, m, r)
            rows.append(row)
            print(N, m, r, "E_out", row["E_out"], "E_net", row["E_net_B"],
                  "tau0", row["tau0"], "tau_marg", row["tau_marg"],
                  "R0", row["R_tau0"], "Rmarg", row["R_tau_marg"], flush=True)
            dump(rows, [])
    neg = [row for row in rows if row["E_net_B"] < 0]
    sep = []
    prices = []
    for row in neg:
        key = (row["N"], row["m"], row["r"])
        if key in done_sep:
            s = done_sep[key]
            print("SEP", s["row"], "RESUMED", flush=True)
        else:
            s = sep_min(row["N"], row["r"])
            s["E_prep_sep"] = s["E_sep_multistart"]
            s["Pi_sep"] = (s["E_prep_sep"] + row["E_in"]) / row["E_out"]
            s["row"] = [row["N"], row["m"], row["r"]]
        sep.append(s); prices.append(s["Pi_sep"])
        print("SEP", s["row"], s["E_prep_sep"], "corner", s["E_sep_corner_D_minus_N"],
              "Pi_sep", s["Pi_sep"], flush=True)
        dump(rows, sep)
    out = dump(rows, sep)
    print("WROTE results/g14_numbers.json; price range", out["price_deciding_range_sep"])

if __name__ == "__main__":
    main()
