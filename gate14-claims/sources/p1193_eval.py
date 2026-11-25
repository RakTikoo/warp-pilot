"""P119-3 evaluation: separable-minimum price reference for the Xun-Ren Hamiltonian.

H (arXiv:2410.04919 Eqs.(1)-(2), h=1):
  H = sum_i [ h sigma_i^z + N h^2 / D ] + 2k prod_i sigma_i^x + 4k^2/D,
  D = sqrt(N^2 h^2 + 4k^2).  Total constant = D.  E_ground = 0.

Product-state expectation (derived in run record):
  <H> = h * sum_i z_i + 2k * prod_i x_i + D,  (x_i,z_i Bloch components)

Analytic reduction: min = min{ D - N h (corner, all theta=0),
                               symmetric interior critical values }
(see run record for the proof). Numerical certificate: multi-start
L-BFGS-B over the full Bloch product manifold + random sampling.

Usage: p1193_eval.py UNIT   UNIT in {c0,c1,c2,d,1..8}; each unit writes
work/p1193_unit_<UNIT>.json.  p1193_eval.py merge  combines them into
results/p1193_results.json.
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize, brentq

H_ = 1.0
RNG = np.random.default_rng(20261123)
BASE = "/home/hatch/workspace/warp-pilot"

def D_of(N, k, h=H_):
    return np.sqrt(N**2 * h**2 + 4 * k**2)

def E_formula(bloch_x, bloch_z, N, k, h=H_):
    return h * np.sum(bloch_z) + 2 * k * np.prod(bloch_x) + D_of(N, k, h)

# ---------- analytic certificate ----------
def analytic_min(N, k, h=H_):
    D = D_of(N, k, h)
    g = lambda th: -N * h * np.cos(th) - 2 * k * np.sin(th) ** N + D
    cands = [{"kind": "corner_all_z=-1", "theta": 0.0, "E": float(g(0.0))}]
    if N == 2:
        f = lambda th: 2 * k * np.cos(th) - h
    else:
        f = lambda th: 2 * k * np.sin(th) ** (N - 2) * np.cos(th) - h
    ths = np.linspace(1e-13, np.pi / 2 - 1e-13, 50001)
    fv = f(ths)
    for i in range(len(ths) - 1):
        if fv[i] * fv[i + 1] < 0:
            r = brentq(f, ths[i], ths[i + 1], xtol=1e-15, rtol=8.881784197001252e-16)
            cands.append({"kind": "symmetric_interior_critical", "theta": float(r), "E": float(g(r))})
    best = min(cands, key=lambda c: c["E"])
    return best, cands

# ---------- numerical certificate: full Bloch manifold ----------
def E_bloch(v, N, k, h=H_):
    th = v[:N]; ph = v[N:]
    x = np.sin(th) * np.cos(ph); z = np.cos(th)
    P = np.prod(x)
    f = h * np.sum(z) + 2 * k * P + D_of(N, k, h)
    cth = np.cos(th); sth = np.sin(th)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(np.abs(x) > 1e-300, P / np.where(x == 0, 1.0, x), 0.0)
    gth = -h * sth + 2 * k * (ratio * cth * np.cos(ph))
    gph = 2 * k * (ratio * (-sth * np.sin(ph)))
    return f, np.concatenate([gth, gph])

def numeric_cert(N, k, n_starts=220, n_random=110000, h=H_):
    best = np.inf
    for s in range(n_starts):
        v0 = np.concatenate([np.arccos(RNG.uniform(-1, 1, N)), RNG.uniform(0, 2 * np.pi, N)])
        res = minimize(E_bloch, v0, args=(N, k, h), jac=True, method="L-BFGS-B",
                       bounds=[(0, np.pi)] * N + [(0, 2 * np.pi)] * N,
                       options={"ftol": 1e-16, "gtol": 1e-10, "maxiter": 80})
        if res.fun < best:
            best = float(res.fun)
    th = np.arccos(RNG.uniform(-1, 1, (n_random, N)))
    ph = RNG.uniform(0, 2 * np.pi, (n_random, N))
    x = np.sin(th) * np.cos(ph); z = np.cos(th)
    vals = h * z.sum(axis=1) + 2 * k * np.prod(x, axis=1) + D_of(N, k, h)
    return {"multistart_best": best, "random_min": float(vals.min()),
            "n_starts": n_starts, "n_random": n_random}

# ---------- dense-H sanity ----------
def dense_check(N, k, h=H_, trials=200):
    sx = np.array([[0, 1], [1, 0]], float); sz = np.array([[1, 0], [0, -1]], float)
    I = np.eye(2)
    def op(single, i):
        out = np.array([[1.0]])
        for j in range(N):
            out = np.kron(out, single if j == i else I)
        return out
    D = D_of(N, k, h)
    Hm = sum(h * op(sz, i) + N * h**2 / D * np.eye(2**N) for i in range(N))
    V = np.array([[1.0]])
    for j in range(N):
        V = np.kron(V, sx)
    Hm = Hm + 2 * k * V + 4 * k**2 / D * np.eye(2**N)
    ev = np.linalg.eigvalsh(Hm)
    maxerr = 0.0
    for _ in range(trials):
        th = np.arccos(RNG.uniform(-1, 1, N)); ph = RNG.uniform(0, 2 * np.pi, N)
        psi = None
        for j in range(N):
            q = np.array([np.cos(th[j] / 2), np.exp(1j * ph[j]) * np.sin(th[j] / 2)], complex)
            psi = q if psi is None else np.kron(psi, q)
        e_dense = float(np.real(np.vdot(psi, Hm @ psi)))
        e_form = E_formula(np.sin(th) * np.cos(ph), np.cos(th), N, k, h)
        maxerr = max(maxerr, abs(e_dense - e_form))
    return {"N": N, "k": k, "ground_eig_min": float(ev[0]), "max_formula_err": maxerr}

REGISTERED = [(5, 1, 0.5), (6, 1, 0.5), (6, 1, 1.0), (8, 1, 0.5), (8, 1, 1.0),
              (10, 1, 0.5), (10, 1, 1.0), (10, 1, 2.0)]

def unit_control(idx):
    p72 = json.load(open(f"{BASE}/phase72/results/p722_results.json"))
    r = (0.5, 1.0, 2.0)[idx]
    target = {p["r"]: p["E_prep_sep"] for p in p72["points"]}[r]
    best, cands = analytic_min(2, r)
    nc = numeric_cert(2, r)
    rec = {"N": 2, "r": r, "E_sep_analytic": best["E"], "analytic_kind": best["kind"],
           "theta_star": best["theta"], "E_sep_multistart": nc["multistart_best"],
           "E_sep_random_min": nc["random_min"], "stored_p722_E_prep_sep": target,
           "abs_err_vs_stored": abs(best["E"] - target), "candidates": cands, "numeric": nc}
    print(f"control r={r}: analytic={best['E']:.16f} stored={target:.16f} err={rec['abs_err_vs_stored']:.3e} "
          f"ms={nc['multistart_best']:.12f} rand={nc['random_min']:.12f}", flush=True)
    return {"control": [rec]}

def unit_row(idx):
    p108 = json.load(open(f"{BASE}/phase108/results/p1085_results.json"))
    stored = {(r["N"], r["m"], r["r"]): r for r in p108["rows"]}
    (N, m, r) = REGISTERED[idx]
    k = r
    best, cands = analytic_min(N, k)
    nc = numeric_cert(N, k)
    s = stored[(N, m, r)]
    E_sep = best["E"]; E_marg = s["E_prep_marg"]; E_in = s["E_in"]; E_out = s["E_out"]
    Pi_sep = (E_sep + E_in) / E_out; Pi_marg = (E_marg + E_in) / E_out
    row = {"N": N, "m": m, "r": r, "D": D_of(N, k),
           "E_sep": E_sep, "E_prep_sep": E_sep, "analytic_kind": best["kind"],
           "theta_star": best["theta"], "candidates": cands, "numeric": nc,
           "E_prep_marg_stored": E_marg, "E_in_stored": E_in, "E_out_stored": E_out,
           "stored_source": "phase108/results/p1085_results.json",
           "Pi_sep": Pi_sep, "Pi_marg": Pi_marg, "Pi_marg_over_Pi_sep": Pi_marg / Pi_sep,
           "deciding_reference": "sep" if E_sep <= E_marg else "marg",
           "Pi_deciding": min(Pi_sep, Pi_marg),
           "Pi_marg_crosscheck_vs_stored_price": abs(Pi_marg - s["price_per_unit_marg"])}
    print(f"row {(N,m,r)}: Esep={E_sep:.12f} ({best['kind']}) Pi_sep={Pi_sep:.6f} Pi_marg={Pi_marg:.6f} "
          f"ratio={Pi_marg/Pi_sep:.6f} ms={nc['multistart_best']:.12f} rand={nc['random_min']:.12f}", flush=True)
    return {"rows": [row]}

def main():
    unit = sys.argv[1]
    t0 = time.time()
    if unit == "merge":
        out = {"item": "P119-3", "model": "Xun & Ren arXiv:2410.04919 Eqs.(1)-(2), h=1",
               "control": [], "rows": [], "dense_checks": []}
        for u in ["c0", "c1", "c2", "d", "1", "2", "3", "4", "5", "6", "7", "8"]:
            d = json.load(open(f"{BASE}/phase119/work/p1193_unit_{u}.json"))
            out["control"].extend(d.get("control", []))
            out["rows"].extend(d.get("rows", []))
            out["dense_checks"].extend(d.get("dense_checks", []))
        json.dump(out, open(f"{BASE}/phase119/results/p1193_results.json", "w"), indent=1)
        print("MERGED", len(out["control"]), "control,", len(out["rows"]), "rows,", len(out["dense_checks"]), "dense", flush=True)
        return
    if unit.startswith("c"):
        out = unit_control(int(unit[1]))
    elif unit == "d":
        out = {"dense_checks": [dense_check(N, k) for (N, k) in [(2, 0.5), (3, 1.0), (5, 0.5)]]}
        for dc in out["dense_checks"]:
            print(f"dense N={dc['N']} k={dc['k']}: ground={dc['ground_eig_min']:.3e} err={dc['max_formula_err']:.3e}", flush=True)
    else:
        out = unit_row(int(unit) - 1)
    out["elapsed_s"] = time.time() - t0
    json.dump(out, open(f"{BASE}/phase119/work/p1193_unit_{unit}.json", "w"), indent=1)
    print("WROTE unit", unit, "elapsed", out["elapsed_s"], flush=True)

if __name__ == "__main__":
    main()
