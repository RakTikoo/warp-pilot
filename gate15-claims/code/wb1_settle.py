"""W-B1 prolonged-system settlement.

Per mode ell in {0,1,2,3} and centre r0 in {11, 1000}:
 unknowns = scaled Taylor coefficients (u_k, v_k, w_k), k=0..Kmax (Kmax=8),
   U(r) = sum u_k ((r-r0)/r0)^k etc. (w absent at ell=0, areal gauge).
 Route 1 (Taylor/stencil): linearised Bach at r0 + m*delta, m=-4..4,
   delta = 0.01*r0, at 4 generic thetas, projected onto the mode's angular
   basis per component; Taylor coefficients in hhat=m to order P.
 Route 2 (collocation): linearised Bach at 9 distinct radii
   r0*(1 + 0.013*(m+0.31)), m=-4..4, same projection; rows are the
   projected values themselves.
 Dimension = rank of the projection of the prolonged nullspace onto the
 initial-data space (u_0..u_3, v_0..v_3, w_0..w_3).
Rows are equilibrated (unit norm) before SVD; the cut is read from the
singular-value spectrum and reported, with a fixed 1e-8 relative cut used
for the headline rank and the neighbouring singular values stored.
"""
import numpy as np, json, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from wb1_engine import bach_at, legendre_P, legendre_theta_derivs

KMAX = 8
THETAS = [0.7, 1.1, 1.9, 2.6]

def comp_names(ell):
    names = ['tt', 'rr', 'ang_trace']
    if ell >= 1:
        names.append('rth')
    if ell >= 2:
        names.append('ang_diff')
    return names

def projected(ell, r0, radii):
    """Returns array (len(radii), ncomp, N) of projected linearised-Bach
    coefficients (derivative channels only). Component angular bases:
    tt, rr, ang_trace=B^th_th+B^ph_ph on P_ell; rth on dP_ell/dth;
    ang_diff=B^th_th-B^ph_ph on E_ell = P_ell'' - cot(th) P_ell'
    (the tracefree angular harmonic; identically zero for ell<2, and
    B^th_th-B^ph_ph and B^r_th vanish identically for ell=0)."""
    nblocks = 2 if ell == 0 else 3
    N = nblocks * (KMAX + 1)
    names = comp_names(ell)
    Pv = np.array([legendre_P(ell, np.cos(t)) for t in THETAS])
    dPv = np.array([legendre_theta_derivs(ell, t)[1] for t in THETAS])
    Ev = np.array([legendre_theta_derivs(ell, t)[2]
                   - (np.cos(t) / np.sin(t)) * legendre_theta_derivs(ell, t)[1]
                   for t in THETAS])
    bases = {'tt': Pv, 'rr': Pv, 'ang_trace': Pv, 'rth': dPv, 'ang_diff': Ev}
    out = np.zeros((len(radii), len(names), N))
    for ri, r in enumerate(radii):
        vals = {n: np.zeros((len(THETAS), N)) for n in names}
        for ti, th in enumerate(THETAS):
            B = bach_at(r, th, ell=ell, center=r0, K=KMAX, nunk=N)
            raw = {'tt': B[0, 0, 1:], 'rr': B[1, 1, 1:],
                   'ang_trace': B[2, 2, 1:] + B[3, 3, 1:],
                   'rth': B[1, 2, 1:], 'ang_diff': B[2, 2, 1:] - B[3, 3, 1:]}
            for n in names:
                vals[n][ti] = raw[n]
        for ci, n in enumerate(names):
            basis = bases[n]
            w = basis / np.sum(basis**2)
            out[ri, ci] = w @ vals[n]
    return out

def analyse(M, N, ell, id_idx=None):
    """Row-equilibrate, SVD, nullspace, ID-projection rank."""
    norms = np.linalg.norm(M, axis=1)
    Ms = M[norms > 0] / norms[norms > 0, None]
    U, s, Vt = np.linalg.svd(Ms, full_matrices=True)
    smax = s[0] if len(s) else 0.0
    cut = 1e-8
    rank = int(np.sum(s > cut * smax))
    Z = Vt[rank:].T  # N x nullity
    if id_idx is None:
        nblocks = 2 if ell == 0 else 3
        id_idx = []
        for blk in range(nblocks):
            id_idx += [blk * (KMAX + 1) + k for k in range(4)]
    Pz = Z[id_idx, :] if Z.shape[1] else np.zeros((len(id_idx), 0))
    if Pz.shape[1]:
        sz = np.linalg.svd(Pz, compute_uv=False)
        id_rank = int(np.sum(sz > 1e-8 * (sz[0] if len(sz) else 1.0)))
    else:
        sz = np.array([]); id_rank = 0
    return dict(rank=int(rank), nullity=int(N - rank), svals=[float(x) for x in s],
                id_rank=id_rank, id_svals=[float(x) for x in sz],
                Z=Z, id_idx=id_idx)

def main():
    t0 = time.time()
    import os
    jpath = __file__.rsplit('/', 1)[0] + '/wb1_settlement.json'
    npath = __file__.rsplit('/', 1)[0] + '/wb1_nullspaces.npz'
    results = {}
    npz = {}
    if os.path.exists(jpath):
        prev = json.load(open(jpath))
        results.update(prev)
    if os.path.exists(npath):
        npz.update(dict(np.load(npath)))
    for ell in [0, 1, 2, 3]:
        nblocks = 2 if ell == 0 else 3
        N = nblocks * (KMAX + 1)
        for r0 in [11.0, 1000.0]:
            key = f'ell{ell}_r{int(r0)}'
            if key in results and 'route2' in results[key]:
                print(key, 'skipped (checkpoint)', flush=True)
                continue
            delta = 0.01 * r0
            radii1 = [r0 + m * delta for m in range(-4, 5)]
            radii2 = [r0 * (1 + 0.013 * (m + 0.31)) for m in range(-4, 5)]
            P1 = projected(ell, r0, radii1)   # (9,5,N)
            P2 = projected(ell, r0, radii2)
            entry = {}
            # Route 1 for each P: fit polynomial in m (=-4..4) per comp
            ms = np.arange(-4, 5, dtype=float)
            for Pord in [3, 4, 5]:
                V = np.stack([ms**p for p in range(Pord + 1)], axis=1)
                F, *_ = np.linalg.lstsq(V, np.eye(9), rcond=None)  # not used directly
                # coefficients: c_p = sum_m Fit[p,m] P1[m]; Fit = pinv(V)
                Fit = np.linalg.pinv(V)
                rows = []
                for ci in range(P1.shape[1]):
                    rows.append(Fit @ P1[:, ci, :])
                M = np.concatenate(rows, axis=0)
                a = analyse(M, N, ell)
                entry[f'route1_P{Pord}'] = {k: a[k] for k in
                    ('rank', 'nullity', 'svals', 'id_rank', 'id_svals')}
                if r0 == 1000.0 and Pord == 4:
                    entry['route1_P4_Z'] = a['Z']
            # Route 2
            M2 = P2.reshape(-1, N)
            a2 = analyse(M2, N, ell)
            entry['route2'] = {k: a2[k] for k in
                ('rank', 'nullity', 'svals', 'id_rank', 'id_svals')}
            if r0 == 1000.0:
                entry['route2_Z'] = a2['Z']
            # K=7 subselection: drop k=8 channels
            keep = [i for i in range(N) if (i % (KMAX + 1)) != KMAX]
            pos = {orig: n for n, orig in enumerate(keep)}
            id7 = [pos[blk * (KMAX + 1) + k] for blk in range(nblocks)
                   for k in range(4)]
            V = np.stack([ms**p for p in range(5)], axis=1)
            Fit = np.linalg.pinv(V)
            rows = [Fit @ P1[:, ci, :][:, keep] for ci in range(P1.shape[1])]
            M = np.concatenate(rows, axis=0)
            a7 = analyse(M, len(keep), ell, id_idx=id7)
            entry['route1_P4_K7'] = {k: a7[k] for k in
                ('rank', 'nullity', 'svals', 'id_rank', 'id_svals')}
            M2k = P2.reshape(-1, N)[:, keep]
            a7b = analyse(M2k, len(keep), ell, id_idx=id7)
            entry['route2_K7'] = {k: a7b[k] for k in
                ('rank', 'nullity', 'svals', 'id_rank', 'id_svals')}
            results[key] = entry
            # checkpoint after every key
            clean = {}
            for kk_, entry_ in results.items():
                clean[kk_] = {}
                for k, v in entry_.items():
                    if k.endswith('_Z'):
                        npz[f'{kk_}_{k}'] = v
                    else:
                        clean[kk_][k] = v
            np.savez(npath, **npz)
            with open(jpath, 'w') as f:
                json.dump(clean, f, indent=1)
            print(key, 'done', round(time.time() - t0, 1), 's', flush=True)
    print('ALL DONE', round(time.time() - t0, 1))

if __name__ == '__main__':
    main()
