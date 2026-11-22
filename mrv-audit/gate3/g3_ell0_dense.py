"""
Gate-3 follow-up, deliverable 2: DENSE corrected (K0, G0, M0) profiles for
the MRV wormhole l=0 sector, and a direct Sturm-Liouville re-solve on the
dense coefficients (settles the G3-4 open item: the claimed soft
throat-localised near-zero mode at om^2 ~ +0.00021).

Route: F4-2b's from-action machinery (phase4/p42b_ell0_indep.py) used in
its grid mode (ops_on_grid shares one jet-Hessian per grid point instead
of elim_at's 45), extended to also return M0 = -Rop[(0,0)]/2 (the same
Rop construction elim_at uses).  Covariant normalisation throughout
(F4-2 Appendix-B coefficients are 2x these; om^2 and M0/K0 are
normalisation-free).

Validations:
  * dense values at the 31 stored elim_at profile radii vs
    phase4/results/p42b_ell0_indep.json (FD-level agreement);
  * elim_at re-run at 5 radii vs the dense grid at the same radii;
  * M0/K0 samples vs F4-3's stored samples (p43_tachyon.json);
  * Liouville V samples vs F4-3's stored V samples.

Solve: -(G0 chi')' + M0 chi = om^2 K0 chi on [-60, 60], Dirichlet,
flux form (F4-3's ell0_solve discretisation), at h = 0.02, 0.01, 0.005
(F4-3's own spacings) with coefficients computed natively at each h
(no interpolation anywhere).  Grids are offset by h/2 so no node sits
at r = 0, where the true K0 vanishes quadratically and the computed
value is a signed FD artefact (measured -9.3e-6 at h=0.05 on-node).
Richardson extrapolation in h^2 for the lowest eigenvalue;
localisation by K0-weighted norm fractions.
float64 everywhere.  Nothing uploaded.
"""
import json
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase4')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase3')
import p42b_ell0_indep as p42b  # noqa: E402

t0 = time.time()


def log(*a):
    print(f'[{time.time() - t0:8.1f}s]', *a, flush=True)


# ---------------------------------------------------------------------------
# grid profiles: p42b.ops_on_grid extended to M0
# ---------------------------------------------------------------------------
def profiles_on_grid(rgrid):
    """(K0, G0, M0) on a uniform grid, F4-2b grid route + M0.
    Valid (non-NaN) on the interior where the 5-point stencils close."""
    d = rgrid[1] - rgrid[0]
    n = len(rgrid)
    Hs = []
    for r in rgrid:
        _, H = p42b.grad_hess_vec(float(r))
        Hs.append(H)
    Ms = {}
    for i in range(2, n - 2):
        Hs5 = {0: Hs[i], 1: Hs[i + 1], -1: Hs[i - 1],
               2: Hs[i + 2], -2: Hs[i - 2]}
        gs5 = {k: np.zeros(p42b.NJ) for k in Hs5}
        _, M, _ = p42b.M_from_Hs(Hs5, gs5, d)
        Ms[i] = M

    def fd1(arr, i):
        return (-arr[i + 2] + 8 * arr[i + 1] - 8 * arr[i - 1]
                + arr[i - 2]) / (12 * d)

    idxs = sorted(Ms)
    p = np.full(n, np.nan)
    q = np.full(n, np.nan)
    for i in idxs:
        M = Ms[i]
        Qb = p42b.get(M, 'C', 'B', (1, 0))
        p[i] = -p42b.get(M, 'C', 'P', (1, 1)) / Qb
        q[i] = -p42b.get(M, 'C', 'P', (1, 0)) / Qb
    S1c = {}
    for i in idxs:
        if i - 2 < idxs[0] or i + 2 > idxs[-1]:
            continue
        M = Ms[i]
        pp = fd1(p, i)
        qq = fd1(q, i)
        mB = p42b.get(M, 'B', 'A', (0, 1))
        subB, _ = p42b.subst_B({g: c for g, c in M[('B', 'B')].items()},
                               p[i], q[i], pp, qq)
        rest = p42b.add_ops({g: c for g, c in M[('B', 'P')].items()}, subB)
        S1c[i] = p42b.scale_op(rest, -1.0 / mB)
    K0 = np.full(n, np.nan)
    G0 = np.full(n, np.nan)
    M0 = np.full(n, np.nan)
    for i in idxs:
        if any(j not in S1c for j in (i - 2, i - 1, i, i + 1, i + 2)):
            continue
        M = Ms[i]
        pp = fd1(p, i)
        qq = fd1(q, i)
        S1p = {}
        for g in set().union(*[S1c[j] for j in
                               (i - 2, i - 1, i, i + 1, i + 2)]):
            v = {2: S1c[i + 2].get(g, 0.0), 1: S1c[i + 1].get(g, 0.0),
                 -1: S1c[i - 1].get(g, 0.0), -2: S1c[i - 2].get(g, 0.0)}
            S1p[g] = (-v[2] + 8 * v[1] - 8 * v[-1] + v[-2]) / (12 * d)
        S1r = p42b.Dr_op(S1c[i], S1p)
        u = p42b.get(M, 'P', 'A', (0, 1))
        w = p42b.get(M, 'P', 'A', (0, 2))
        subBP, _ = p42b.subst_B({g: c for g, c in M[('P', 'B')].items()},
                                p[i], q[i], pp, qq)
        Rop = p42b.add_ops(p42b.scale_op(S1c[i], u),
                           p42b.scale_op(S1r, w),
                           {g: c for g, c in M[('P', 'P')].items()}, subBP)
        K0[i] = -Rop.get((2, 0), 0.0) / 2
        G0[i] = Rop.get((0, 2), 0.0) / 2
        M0[i] = -Rop.get((0, 0), 0.0) / 2
    return K0, G0, M0


def flux_solve(r, K0, G0, M0, k=8):
    """F4-3's ell0_solve discretisation: flux-form tridiagonal
    generalised eigenproblem, Dirichlet box, shift-invert at 0."""
    h = r[1] - r[0]
    Gh = 0.5 * (G0[1:] + G0[:-1])
    main = (Gh[1:] + Gh[:-1]) / h**2 + M0[1:-1]
    off = -Gh[1:-1] / h**2
    A = sparse.diags([main, off, off], [0, 1, -1]).tocsc()
    Bm = sparse.diags([K0[1:-1]], [0]).tocsc()
    vals, vecs = eigsh(A, M=Bm, k=k, sigma=0.0, which='LM', tol=1e-11)
    order = np.argsort(vals)
    return vals[order], vecs[:, order]


def liouville_V(r, K, G, M):
    """F4-3's liouville_V: V in the rho coordinate (diagnostic only)."""
    L = np.log(np.sqrt(K * G))
    fac = np.sqrt(G / K)
    rho = np.concatenate([[0.0], np.cumsum(0.5 * (fac[1:] + fac[:-1])
                                           * np.diff(r))])
    Lr = np.gradient(L, r)
    Lrho = fac * Lr
    Lrhorho = fac * np.gradient(Lrho, r)
    V = M / K + 0.5 * Lrhorho + 0.25 * Lrho**2
    return rho, V


def main():
    res = {'task': 'G3-4 follow-up: dense corrected (K0,G0,M0) profiles '
                   'and direct l=0 mode re-solve',
           'route': 'F4-2b from-action grid route extended to M0; '
                    'flux-form Sturm-Liouville solve on native grids',
           'normalisation': 'covariant (F4-2 App-B = 2x); om^2 and '
                            'M0/K0 normalisation-free'}

    with open('/home/hatch/workspace/warp-pilot/phase4/results/'
              'p42b_ell0_indep.json') as fh:
        p42b_stored = json.load(fh)
    prof_stored = p42b_stored['profile']
    rs_stored = np.array(sorted(float(k) for k in prof_stored))
    with open('/home/hatch/workspace/warp-pilot/phase4/results/'
              'p43_tachyon.json') as fh:
        p43 = json.load(fh)

    grids = {}
    solves = {}
    for h in (0.02, 0.01, 0.005):
        rgrid = np.arange(-62.0 + 0.5 * h, 62.0, h)
        log(f'computing coefficients at h={h} ({len(rgrid)} points)...')
        K0, G0, M0 = profiles_on_grid(rgrid)
        ok = ~np.isnan(K0)
        r_ok, K_ok, G_ok, M_ok = rgrid[ok], K0[ok], G0[ok], M0[ok]
        log(f'  valid r in [{r_ok[0]}, {r_ok[-1]}], '
            f'K0 min {np.min(K_ok):.6g}, G0 min {np.min(G_ok):.6g}')
        grids[h] = (r_ok, K_ok, G_ok, M_ok)
        # solve on [-60, 60]
        m = (r_ok >= -60.0 - 1e-9) & (r_ok <= 60.0 + 1e-9)
        r, K, G, M = r_ok[m], K_ok[m], G_ok[m], M_ok[m]
        vals, vecs = flux_solve(r, K, G, M, k=8)
        solves[h] = (r, K, G, M, vals, vecs)
        log(f'  h={h}: lowest om2 = {vals[:4]}')

    # ---- validation 1: dense grid (h=0.01) vs stored elim_at profile
    r05, K05, G05, M05 = grids[0.01]
    val1 = {}
    for name, arr in (('K0', K05), ('G0', G05), ('M0', M05)):
        mine = np.interp(rs_stored, r05, arr)
        ref = np.array([prof_stored[f'{r:.1f}'][name] for r in rs_stored])
        rel = np.abs(mine - ref) / np.maximum(np.abs(ref), 1e-9)
        val1[name] = dict(max_rel_dev=float(np.max(rel)),
                          median_rel_dev=float(np.median(rel)),
                          worst_r=float(rs_stored[int(np.argmax(rel))]))
    res['validation_vs_stored_elim_at_profile'] = val1
    log('validation vs stored profile:', val1)

    # ---- validation 2: fresh elim_at at 5 radii vs dense grid
    val2 = {}
    for r0 in (-20.0, -5.0, 0.5, 5.0, 20.0):
        o = p42b.elim_at(r0)
        row = {}
        for name, arr in (('K0', K05), ('G0', G05), ('M0', M05)):
            mine = float(np.interp([r0], r05, arr)[0])
            row[name] = dict(elim_at=o[name], dense=mine,
                             rel_dev=abs(mine - o[name])
                             / max(abs(o[name]), 1e-9))
        val2[str(r0)] = row
    res['validation_elim_at_spot'] = val2
    log('validation elim_at spots done')

    # ---- validation 3: M0/K0 and Liouville V vs F4-3 stored samples
    f43_m0k0 = p43['ell0']['M0_over_K0_samples']
    val3 = {}
    for key, ref in f43_m0k0.items():
        rr = float(key.split('=')[1])
        mine = float(np.interp([rr], r05, M05 / K05)[0])
        val3[key] = dict(f43=ref, dense_covariant_ratio=mine,
                         note='F4-3 used App-B normalisation (2x) for '
                              'both M0 and K0, so the ratio is '
                              'directly comparable')
    res['validation_M0_over_K0_vs_F43'] = val3
    rho, V = liouville_V(r05, K05, G05, M05)
    f43_V = {'r=-5': -0.0016685018600028638, 'r=-1': 0.17298025481214196,
             'r=-0.5': 0.2630553123627415, 'r=0.5': 0.8412875048441331,
             'r=1': 2.2694958580197273, 'r=3': 0.7562330581548916,
             'r=5': 0.08398620455463687, 'r=20': 0.007429552326386509}
    val4 = {}
    for key, ref in f43_V.items():
        rr = float(key.split('=')[1])
        mine = float(np.interp([rr], r05, V)[0])
        val4[key] = dict(f43=ref, dense=mine,
                         rel_dev=abs(mine - ref) / max(abs(ref), 1e-9))
    res['validation_liouville_V_vs_F43'] = val4
    log('validation vs F4-3 done')

    # ---- eigenvalue convergence + extrapolation
    w = {h: float(solves[h][4][0]) for h in (0.02, 0.01, 0.005)}
    # Richardson in h^2 from the two finest, and from the coarser pair
    w_ex21 = (4 * w[0.005] - w[0.01]) / 3
    w_ex32 = (4 * w[0.01] - w[0.02]) / 3
    res['lowest_om2_by_h'] = {str(h): w[h] for h in w}
    res['lowest_om2_richardson'] = {'from_0.01_0.005': float(w_ex21),
                                    'from_0.02_0.01': float(w_ex32)}
    res['claimed_F43'] = {
        'grids': {f'h{h}': p43['ell0'][f'lowest_om2_h{h}']
                  for h in (0.02, 0.01, 0.005)},
        'richardson_h2_limit': p43['ell0'][
            'lowest_om2_richardson_h2_limit'],
        'route': 'F4-2 (Appendix-B, pair-corrected) coefficients, '
                 'same flux discretisation'}
    log('lowest om2 by h:', w, 'richardson:', w_ex21, w_ex32)

    # ---- localisation of the lowest mode (finest grid)
    r, K, G, M, vals, vecs = solves[0.005]
    chi = np.zeros(len(r))
    chi[1:-1] = vecs[:, 0]
    dens = K * chi**2
    tot = np.trapezoid(dens, r)
    rstar = 1.772437990426927

    def frac(lo, hi):
        m = (r >= lo) & (r <= hi)
        return float(np.trapezoid(dens[m], r[m]) / tot)

    res['lowest_mode_localisation'] = {
        'peak_r': float(r[int(np.argmax(np.abs(chi)))]),
        'frac_0_to_rstar': frac(0.0, rstar),
        'frac_abs_r_lt_2': frac(-2.0, 2.0),
        'frac_abs_r_gt_10': frac(10.0, 60.0) + frac(-60.0, -10.0),
        'note': 'K0-weighted norm fractions, finest grid (h=0.005)'}
    res['second_om2_by_h'] = {str(h): float(solves[h][4][1])
                              for h in (0.02, 0.01, 0.005)}

    # ---- continuum threshold: M0/K0 at large |r| from the dense data
    thr = {}
    for rr in (30.0, 40.0, 50.0, 59.0, -30.0, -40.0, -50.0, -59.0):
        thr[str(rr)] = float(np.interp([rr], r05, M05 / K05)[0])
    res['M0_over_K0_exterior'] = thr
    res['threshold_note'] = ('continuum threshold = lim M0/K0 as '
                             '|r| -> inf; V3 quoted 2.61e-4')

    # ---- positivity on the dense grid
    res['positivity'] = {
        'K0_min_h0.01': float(np.min(K05)),
        'G0_min_h0.01': float(np.min(G05)),
        'K0_over_r2_at_throat': {
            str(rr): float(np.interp([rr], r05, K05)[0] / rr**2)
            for rr in (0.1, -0.1, 0.2, -0.2)}}

    # ---- store the dense profiles (h=0.01) in full
    out = {'r': r05.tolist(), 'K0': K05.tolist(), 'G0': G05.tolist(),
           'M0': M05.tolist(),
           'meta': 'covariant normalisation; F4-2b grid route; '
                   'h=0.01 grid offset by h/2; valid on [-61.98, 61.98]'}
    with open('/home/hatch/workspace/warp-pilot/gate3/results/'
              'g3_ell0_dense_profiles.json', 'w') as fh:
        json.dump(out, fh)
    with open('/home/hatch/workspace/warp-pilot/gate3/results/'
              'g3_ell0_dense.json', 'w') as fh:
        json.dump(res, fh, indent=2, default=str)
    log('done')
    print(json.dumps(res, indent=2, default=str))


if __name__ == '__main__':
    main()
