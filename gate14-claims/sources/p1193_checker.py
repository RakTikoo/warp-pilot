"""P119-3 independent checker.

Independence: builds H densely (Kronecker) from Eqs.(1)-(2); computes
product-state expectations from the state TENSOR (probabilities and the
all-bit-flip overlap), never from the evaluation script's Bloch formula;
re-derives each minimum with its own random sampling (>=1e5 states) and
its own multi-start optimisation (Powell, tensor objective); recomputes
every price ratio from p1193_results.json + stored Phase 108 values.
"""
import json, sys
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(987654321)
FAIL = []

def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg, flush=True)
    if not cond:
        FAIL.append(msg)

def dense_H(N, k, h=1.0):
    sx = np.array([[0, 1], [1, 0]], float); sz = np.array([[1, 0], [0, -1]], float)
    I = np.eye(2); D = np.sqrt(N**2 * h**2 + 4 * k**2)
    def op(single, i):
        out = np.array([[1.0]])
        for j in range(N):
            out = np.kron(out, single if j == i else I)
        return out
    Hm = sum(h * op(sz, i) for i in range(N)) + D * np.eye(2**N)
    X = np.array([[1.0]])
    for _ in range(N):
        X = np.kron(X, sx)
    return Hm + 2 * k * X

def tensor_expectation(psi, N, k, h=1.0):
    """<H> from the state vector directly: sum_i h<Z_i> + 2k<prod X> + D."""
    D = np.sqrt(N**2 * h**2 + 4 * k**2)
    p = np.abs(psi) ** 2
    idx = np.arange(2**N)
    zsum = 0.0
    for i in range(N):
        bit = (idx >> (N - 1 - i)) & 1
        zsum += np.sum(p * (1 - 2 * bit))
    flip = idx ^ (2**N - 1)
    xprod = np.real(np.sum(np.conj(psi) * psi[flip]))
    return h * zsum + 2 * k * xprod + D

def product_psi(thetas, phis):
    psi = None
    for th, ph in zip(thetas, phis):
        q = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)], complex)
        psi = q if psi is None else np.kron(psi, q)
    return psi

def batch_expectations(thetas, phis, N, k, h=1.0):
    """Vectorised tensor expectations for a batch of product states."""
    B = thetas.shape[0]
    psi = np.ones((B, 1), complex)
    for j in range(N):
        q = np.stack([np.cos(thetas[:, j] / 2),
                      np.exp(1j * phis[:, j]) * np.sin(thetas[:, j] / 2)], axis=1)  # (B,2)
        psi = (psi[:, :, None] * q[:, None, :]).reshape(B, -1)
    D = np.sqrt(N**2 * h**2 + 4 * k**2)
    p = np.abs(psi) ** 2
    idx = np.arange(2**N)
    S = np.stack([1 - 2 * ((idx >> (N - 1 - i)) & 1) for i in range(N)], axis=1).astype(float)
    zsum = p @ S.sum(axis=1)
    flip = idx ^ (2**N - 1)
    xprod = np.real(np.sum(np.conj(psi) * psi[:, flip], axis=1))
    return h * zsum + 2 * k * xprod + D

def own_minimum(N, k, n_starts=60, n_random=100000):
    best = np.inf
    remaining = n_random
    while remaining > 0:
        b = min(5000, remaining); remaining -= b
        th = np.arccos(rng.uniform(-1, 1, (b, N))); ph = rng.uniform(0, 2 * np.pi, (b, N))
        vals = batch_expectations(th, ph, N, k)
        best = min(best, float(vals.min()))
    # own multi-start L-BFGS-B (numerical gradient) on the tensor objective
    idx = np.arange(2**N); flip = idx ^ (2**N - 1)
    bits = np.stack([1 - 2 * ((idx >> (N - 1 - i)) & 1) for i in range(N)], axis=1).astype(float)
    D = np.sqrt(N**2 + 4 * k**2)
    def obj(v):
        psi = product_psi(v[:N], v[N:])
        p = np.abs(psi) ** 2
        return float(p @ bits.sum(axis=1) + 2 * k * np.real(np.sum(np.conj(psi) * psi[flip])) + D)
    for s in range(n_starts):
        v0 = np.concatenate([np.arccos(rng.uniform(-1, 1, N)), rng.uniform(0, 2 * np.pi, N)])
        res = minimize(obj, v0, method="L-BFGS-B",
                       bounds=[(0, np.pi)] * N + [(0, 2 * np.pi)] * N,
                       options={"ftol": 1e-16, "maxiter": 150})
        if res.fun < best: best = float(res.fun)
    return best

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"  # control | 1..8 (row idx) | final
    res = json.load(open("/home/hatch/workspace/warp-pilot/phase119/results/p1193_results.json"))
    p108 = json.load(open("/home/hatch/workspace/warp-pilot/phase108/results/p1085_results.json"))
    stored = {(r["N"], r["m"], r["r"]): r for r in p108["rows"]}
    targets72 = {0.5: 0.2360679774997898, 1.0: 0.3284271247461903, 2.0: 0.2221359549995796}

    # control re-derivation (dense, N=2)
    for c in (res["control"] if mode in ("all", "control") else []):
        r = c["r"]
        check(abs(c["E_sep_analytic"] - targets72[r]) <= 1e-9, f"control r={r} eval vs P72-2 stored")
        Hm = dense_H(2, r)
        g = np.linalg.eigvalsh(Hm)[0]
        check(abs(g) <= 1e-12, f"control r={r} dense ground energy 0 (got {g:.2e})")
        own = own_minimum(2, r, n_starts=30, n_random=20000)
        check(abs(own - targets72[r]) <= 1e-7, f"control r={r} checker own min {own:.12f} vs stored")
        print(f"  control r={r}: checker own min = {own:.12f}", flush=True)

    # registered rows
    rows = res["rows"] if mode in ("all", "final") else ([res["rows"][int(mode) - 1]] if mode.isdigit() else [])
    for row in rows:
        N, m, r = row["N"], row["m"], row["r"]; k = r
        s = stored[(N, m, r)]
        check(row["E_in_stored"] == s["E_in"] and row["E_out_stored"] == s["E_out"]
              and row["E_prep_marg_stored"] == s["E_prep_marg"],
              f"row {(N,m,r)} stored Phase108 values quoted exactly")
        # candidate state expectation via dense H: theta_star symmetric state
        # (corner: all |1>; interior: symmetric Bloch state with x<0 on qubit 1 pattern)
        th = row["theta_star"]
        if th == 0.0:
            psi = product_psi(np.full(N, np.pi), np.zeros(N))
        else:
            # symmetric optimum: z=-cos th, |x|=sin th, product of x negative
            phis = np.zeros(N); phis[0] = np.pi  # x_1 = -sin th, others +sin th... via phi: x=sin(th_polar)cos(phi)
            pol = np.full(N, np.pi - th)  # polar angle: cos = -cos th, sin = sin th
            psi = product_psi(pol, phis)
        e_dense = tensor_expectation(psi, N, k)
        check(abs(e_dense - row["E_sep"]) <= 1e-9,
              f"row {(N,m,r)} candidate state dense expectation {e_dense:.12f} == E_sep")
        if mode != "final":
            own = own_minimum(N, k, n_starts=20, n_random=30000)
            check(own >= row["E_sep"] - 1e-7, f"row {(N,m,r)} checker found nothing lower (own min {own:.12f})")
            check(abs(own - row["E_sep"]) <= 1e-6, f"row {(N,m,r)} checker own min matches E_sep")
            print(f"  row {(N,m,r)}: checker own min = {own:.12f}, E_sep = {row['E_sep']:.12f}", flush=True)
        Pi_sep = (row["E_prep_sep"] + s["E_in"]) / s["E_out"]
        Pi_marg = (s["E_prep_marg"] + s["E_in"]) / s["E_out"]
        check(abs(Pi_sep - row["Pi_sep"]) <= 1e-9 * Pi_sep, f"row {(N,m,r)} Pi_sep recomputed")
        check(abs(Pi_marg - row["Pi_marg"]) <= 1e-9 * Pi_marg, f"row {(N,m,r)} Pi_marg recomputed")
        check(abs(Pi_marg / Pi_sep - row["Pi_marg_over_Pi_sep"]) <= 1e-9, f"row {(N,m,r)} ratio recomputed")
        check(abs(row["Pi_deciding"] - min(Pi_sep, Pi_marg)) <= 1e-9, f"row {(N,m,r)} deciding price = min-ref")

    # verdict thresholds
    if mode in ("all", "final"):
        moves = any(row["Pi_deciding"] <= 1.0 or row["Pi_marg_over_Pi_sep"] >= 2.0 for row in res["rows"])
        print("VERDICT THRESHOLD: moves =", moves, flush=True)
        check(not moves, "price line stands thresholds (no deciding price <=1, no ratio >=2)")
    print("CHECKER RESULT:", "ALL PASS" if not FAIL else f"{len(FAIL)} FAILURES", flush=True)
    sys.exit(1 if FAIL else 0)

if __name__ == "__main__":
    main()
