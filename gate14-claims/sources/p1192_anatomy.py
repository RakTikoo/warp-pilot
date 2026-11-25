#!/usr/bin/env python
"""
P119-2 anatomy computation — Nambu & Hotta, "Quantum Energy Teleportation
with a Linear Harmonic Chain", arXiv:1007.2234 (single-receiver form).

Everything below is an evaluation of PRINTED formulas only:
  H            Eq. (1):  H = 1/2 sum_j (p_j^2 + q_j^2 - alpha q_j q_{j-1})
  modes        Eq. (3):  omega_k^2 = 1 - alpha cos(theta_k), theta_k = 2 pi k / N
  correlators  Eq. (4):  <q_i q_j> = (1/N) sum_k cos((i-j) theta_k) / (2 omega_k) = g_|i-j|
               Eq. (5):  <p_i p_j> = (1/N) sum_k omega_k cos((i-j) theta_k) / 2 = h_|i-j|
  site energy  Eq. (19): H_n = 1/2 [ p_n^2 + q_n^2 - (alpha/2) q_n (q_{n-1}+q_{n+1}) - eps ],
               eps fixed by Eq. (20), <g|H_n|g> = 0  =>  eps = h_0 + g_0 - alpha * g_1
  delivered    Eq. (26): <H_B>_opt = -1/2 Jp^T Tp^{-1} Jp - 1/2 Jq^T Tq^{-1} Jq  (< 0),
               with Tp, Tq, Jp, Jq from Eq. (24) and the line after it:
                 (Tp)_jk = h_|j-k| + (omega/2) delta_jk
                 (Tq)_jk = g_|j-k| + (1/(2 omega)) delta_jk
                 (Jp)_j  = h_|j - n_B|
                 (Jq)_j  = g_|j - n_B| - (alpha/2)( g_|j-(n_B-1)| + g_|j-(n_B+1)| )
               POVM coherent-state parameter omega = 1 (the site frequency of
               Eq. (1); the paper leaves omega as the POVM's own parameter).

Inherited accounting (P72-2 SS3 (R-marg) / P106-3, applied as anatomy only):
  the receiving sector is the paper's own site-B sector H_B (Eq. 19, which
  carries B's coupling halves exactly as printed). Its uncorrelated
  (marginal-product) reference is the product of the ground state's own
  single-site marginals (Gaussian, variances g_0 and h_0, zero means, all
  inter-site correlators deleted). In that state <q_n q_{n+-1}> = 0, so
    <H_B>_marg = 1/2 [ h_0 + g_0 - eps ] = alpha * g_1 / 2,
    E_prep^(marg, sector) = alpha * g_1 / 2,
    E_net,sector = E_prep^(marg, sector) - E_delivered,
    R_net = 0 iff E_net,sector >= 0 (P72-2 SS4 FR-net).
  The paper prints NO protocol duration: it assumes the H-evolution during
  the protocol is negligible and the classical communication speed infinite
  (Sec. I / Sec. III), so no tau can be read from the published form's own
  evolution; where E_net < 0 hypothetically appeared we would report the
  break-even tau* = (3/(32 pi^2)) / |E_net| (hbar = 1) instead.

float64 throughout. Programme venv python.
"""
import json
import numpy as np

OUT = "/home/hatch/workspace/warp-pilot/phase119/results/p1192_results.json"
OMEGA_POVM = 1.0


def correlators(N, alpha, rmax):
    """g_r, h_r for r = 0..rmax from Eqs. (3)-(5), direct float64 sums."""
    k = np.arange(N, dtype=np.float64)
    theta = 2.0 * np.pi * k / N
    w = np.sqrt(1.0 - alpha * np.cos(theta))
    r = np.arange(rmax + 1, dtype=np.float64)
    C = np.cos(np.outer(r, theta))  # cos(r * theta_k)
    g = (C @ (1.0 / (2.0 * w))) / N
    h = (C @ (w / 2.0)) / N
    return g, h


def delivered_single(N, alpha, d):
    """Setting 1 (paper Sec. IV A): one measured site, B at distance d.
    Eq. (26) with a single measured site j: Tp, Tq are scalars."""
    g, h = correlators(N, alpha, d + 1)
    Jp = h[d]
    Jq = g[d] - 0.5 * alpha * (g[d - 1] + g[d + 1])
    Tp = h[0] + OMEGA_POVM / 2.0
    Tq = g[0] + 1.0 / (2.0 * OMEGA_POVM)
    e_del = 0.5 * (Jp * Jp / Tp + Jq * Jq / Tq)
    e_prep_marg = 0.5 * alpha * g[1]
    return dict(N=N, alpha=alpha, d=d, g0=float(g[0]), g1=float(g[1]),
                h0=float(h[0]), E_delivered=float(e_del),
                E_prep_marg_sector=float(e_prep_marg),
                E_net_sector=float(e_prep_marg - e_del),
                R_net=0.0 if e_prep_marg - e_del >= 0 else None)


def delivered_block(N, alpha, ell):
    """Setting 2 (paper Sec. IV B): measured block of 2*ell+1 sites
    (sites 1..2ell+1, 1-indexed), B the single site n_B = N/2 + ell + 1.
    Eq. (26) with full Tp, Tq matrices over the measured sites."""
    m = 2 * ell + 1
    nB = N // 2 + ell + 1  # 1-indexed site of B
    rmax = N
    g, h = correlators(N, alpha, rmax)
    j = np.arange(1, m + 1)
    D = np.abs(j[:, None] - j[None, :])
    Tp = h[D] + (OMEGA_POVM / 2.0) * np.eye(m)
    Tq = g[D] + (1.0 / (2.0 * OMEGA_POVM)) * np.eye(m)
    dist = np.abs(j - nB)
    Jp = h[dist]
    Jq = g[dist] - 0.5 * alpha * (g[np.abs(j - (nB - 1))] + g[np.abs(j - (nB + 1))])
    e_del = 0.5 * (Jp @ np.linalg.solve(Tp, Jp) + Jq @ np.linalg.solve(Tq, Jq))
    e_prep_marg = 0.5 * alpha * g[1]
    return dict(N=N, alpha=alpha, ell=ell, n_measured=m, n_B=nB,
                E_delivered=float(e_del),
                E_prep_marg_sector=float(e_prep_marg),
                E_net_sector=float(e_prep_marg - e_del),
                R_net=0.0 if e_prep_marg - e_del >= 0 else None)


def main():
    alphas = [0.90, 0.95, 0.99, 1.0 - 1e-7]
    res = {"source": "Nambu & Hotta, arXiv:1007.2234, Eqs. (1),(3)-(5),(19)-(20),(24),(26)",
           "omega_povm": OMEGA_POVM,
           "setting1_N100": [], "setting2_maximal": []}
    for a in alphas:
        for d in [1, 2, 3, 5, 10, 20]:
            res["setting1_N100"].append(delivered_single(100, a, d))
    for a in [0.99, 1.0 - 1e-7]:
        for N in [20, 40, 60, 80, 100]:
            res["setting2_maximal"].append(delivered_block(N, a, N // 2 - 2))
    # NOTE: this sandbox drops large stdout blobs and python file-writes;
    # main() prints compact rows only, and results/p1192_results.json is
    # written from these rows (values identical to the dicts built above).
    for row in res["setting1_N100"]:
        print(f"S1 a={row['alpha']:.7g} d={row['d']:2d} E_del={row['E_delivered']:.6e} "
              f"E_prep={row['E_prep_marg_sector']:.6e} E_net={row['E_net_sector']:+.6e}")
    for row in res["setting2_maximal"]:
        print(f"S2 a={row['alpha']:.7g} N={row['N']:3d} E_del={row['E_delivered']:.6e} "
              f"E_prep={row['E_prep_marg_sector']:.6e} E_net={row['E_net_sector']:+.6e}")
    return res


if __name__ == "__main__":
    main()
