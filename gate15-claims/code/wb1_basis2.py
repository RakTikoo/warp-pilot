"""W-B1 offline analysis from wb1_projected.npz:
- rank/cut sensitivity of the prolonged systems at Sigma (route1 P=3..6,
  route2), with a generous nullspace cut (svals < 1e-6 * smax);
- ell=0 named-vector distances to the generous nullspace;
- cross-centre test: Sigma basis profiles re-expanded about r=900 and
  measured against the r=900 system's ID span;
- ell=1 gauge-family test (Y-polynomial gauge directions in RW gauge);
- final basis construction -> gate15/results/wb1_basis_jets.json,
  wb1_basis_meta.json (this dir).
Settled dimensions used for the basis (stable reads): ell0=7, ell1=10,
ell2=8, ell3=8.
"""
import numpy as np, json, sys
base = __file__.rsplit('/', 1)[0]
KMAX = 8
RS = 1000.0
SETTLED = {0: 7, 1: 10, 2: 8, 3: 8}
P_ = np.load(base + '/wb1_projected.npz')

def build_M(P1, Pord, mmax=4):
    idx = [m + 6 for m in range(-mmax, mmax + 1)]
    ms = np.arange(-mmax, mmax + 1, dtype=float)
    V = np.stack([ms**p for p in range(Pord + 1)], axis=1)
    Fit = np.linalg.pinv(V)
    sub = P1[idx]
    rows = [Fit @ sub[:, ci, :] for ci in range(P1.shape[1])]
    return np.concatenate(rows, axis=0)

def nullspace(M, cutrel=1e-6):
    norms = np.linalg.norm(M, axis=1)
    Ms = M[norms > 0] / norms[norms > 0, None]
    U, s, Vt = np.linalg.svd(Ms, full_matrices=True)
    rank = int(np.sum(s > cutrel * s[0]))
    return Vt[rank:].T, s, rank

def id_idx(ell):
    nb = 2 if ell == 0 else 3
    return [blk * (KMAX + 1) + k for blk in range(nb) for k in range(4)]

def id_rank_of(Z, ell, cutrel=1e-8):
    if Z.shape[1] == 0:
        return 0, np.array([])
    Pz = Z[id_idx(ell), :]
    sz = np.linalg.svd(Pz, compute_uv=False)
    return int(np.sum(sz > cutrel * sz[0])), sz

# ---------- series helpers (x = (r-1000)/1000) ----------
NS = KMAX + 1
def smul(a, b):
    out = np.zeros(NS)
    for i in range(NS):
        for j in range(NS - i):
            out[i + j] += a[i] * b[j]
    return out
def sinv(a):
    out = np.zeros(NS); out[0] = 1.0 / a[0]
    for n in range(1, NS):
        out[n] = -sum(a[k] * out[n - k] for k in range(1, n + 1)) / a[0]
    return out
def sder(a):  # d/dr of a series in x, r = RS(1+x): coeff_k = (k+1) a_{k+1} / RS
    out = np.zeros(NS)
    for k in range(NS - 1):
        out[k] = (k + 1) * a[k + 1] / RS
    return out
beta, gamma, kk = 2.142611, 1e-28, -2.28996e-9
inv_r = np.array([(-1.0)**k / RS for k in range(NS)])
r_ser = np.zeros(NS); r_ser[0] = RS; r_ser[1] = RS
r2_ser = np.zeros(NS); r2_ser[0] = RS**2; r2_ser[1] = 2 * RS**2; r2_ser[2] = RS**2
Cpar = beta * (2 - 3 * beta * gamma)
f_ser = -Cpar * inv_r + gamma * r_ser - kk * r2_ser
f_ser[0] += 1 - 3 * beta * gamma
finv = sinv(f_ser)
finv2 = smul(finv, finv)
named = {}
for nm, dA in [('dbeta', -3 * gamma - (2 - 6 * beta * gamma) * inv_r),
               ('dgamma', -3 * beta + 3 * beta**2 * inv_r + r_ser),
               ('dk', -r2_ser)]:
    dA = np.array(dA, dtype=float)
    named[nm] = np.concatenate([dA, smul(-dA, finv2)])
named['rescaling'] = np.concatenate([f_ser, np.zeros(NS)])

meta = {'cut_sensitivity': {}, 'named_ell0_generous': {}, 'cross_centre': {},
        'gauge_ell1': {}}
bases_full = {}

for ell in [0, 1, 2, 3]:
    P1 = P_[f'ell{ell}_r1000_P1']
    P2 = P_[f'ell{ell}_r1000_P2']
    ent = {}
    for Pord, mm in [(3, 4), (4, 4), (5, 4), (6, 6)]:
        M = build_M(P1, Pord, mm)
        Z, s, rank = nullspace(M)
        ir, sz = id_rank_of(Z, ell)
        ent[f'route1_P{Pord}'] = dict(rank=rank, nullity=int(Z.shape[1]),
                                      id_rank=ir, id_svals=[float(x) for x in sz],
                                      svals=[float(x) for x in s])
    M2 = P2.reshape(-1, P2.shape[2])
    Z2, s2, rank2 = nullspace(M2)
    ir2, sz2 = id_rank_of(Z2, ell)
    ent['route2'] = dict(rank=rank2, nullity=int(Z2.shape[1]), id_rank=ir2,
                         id_svals=[float(x) for x in sz2],
                         svals=[float(x) for x in s2])
    meta['cut_sensitivity'][f'ell{ell}'] = ent
    # primary basis system: route1 P4, generous cut
    M = build_M(P1, 4, 4)
    Z, s, rank = nullspace(M)
    bases_full[ell] = Z
    if ell == 0:
        for nm, vec in named.items():
            coef, *_ = np.linalg.lstsq(Z, vec, rcond=None)
            meta['named_ell0_generous'][nm] = float(
                np.linalg.norm(Z @ coef - vec) / np.linalg.norm(vec))

# ---------- cross-centre test (r0=900, route1 P4) ----------
for ell in [1, 2, 3]:
    P1 = P_[f'ell{ell}_r900_P1']
    M = build_M(P1, 4, 4)
    Z900, _, _ = nullspace(M)
    idx = id_idx(ell)
    Pz900 = Z900[idx, :]
    U900, sv900, _ = np.linalg.svd(Pz900, full_matrices=False)
    d900 = int(np.sum(sv900 > 1e-8 * sv900[0]))
    Q900 = U900[:, :d900]
    # Sigma basis ID vectors (from bases_full, ID-orthonormalised, settled d)
    Z = bases_full[ell]
    Pz = Z[idx, :]
    U_, sv_, _ = np.linalg.svd(Pz, full_matrices=False)
    d = SETTLED[ell]
    Qid = U_[:, :d]
    C = np.linalg.pinv(Pz) @ Qid
    Bfull = Z @ C
    dists = []
    for j in range(Bfull.shape[1]):
        vec = Bfull[:, j]
        # re-expand each block polynomial about 900: xS = -0.1 + 0.9 x9
        nb = 3
        newid = []
        for blk in range(nb):
            a = vec[blk * NS:(blk + 1) * NS]
            b = np.zeros(NS)
            for k in range(NS):
                # (-0.1 + 0.9 x)^k
                for jj in range(k + 1):
                    from math import comb
                    b[jj] += a[k] * comb(k, jj) * (-0.1)**(k - jj) * 0.9**jj
            newid += [b[0], b[1], b[2], b[3]]
        newid = np.array(newid)
        dist = float(np.linalg.norm(newid - Q900 @ (Q900.T @ newid)) /
                     np.linalg.norm(newid))
        dists.append(dist)
    meta['cross_centre'][f'ell{ell}'] = dict(d_at_900=d900, basis_dists=dists)

# ---------- ell=1 gauge family ----------
ell = 1
Z = bases_full[1]
idx = id_idx(1)
fp = sder(f_ser)                      # f'
finv_p = sder(finv)                   # (1/f)'
gauge_vecs = []
for j in range(4):
    Y = np.zeros(NS); Y[j] = 1.0
    Yp = sder(Y)
    X = -smul(smul(f_ser, r2_ser), Yp)     # X = -f r^2 Y'
    Xp = sder(X)
    U = smul(fp, X)
    V = smul(X, finv_p) + 2 * smul(Xp, finv)
    Th = 2 * X / RS - 2 * Y               # 2X/r series: X * (2/r); 2/r = 2*inv_r*? r=RS(1+x): 2/r = 2*inv_r
    Th = smul(X, 2 * inv_r) - 2 * Y
    gauge_vecs.append(np.concatenate([U, V, Th]))
G = np.stack(gauge_vecs, axis=1)
dists = []
for j in range(4):
    coef, *_ = np.linalg.lstsq(Z, G[:, j], rcond=None)
    dists.append(float(np.linalg.norm(Z @ coef - G[:, j]) / np.linalg.norm(G[:, j])))
Gid = G[idx, :]
meta['gauge_ell1'] = dict(
    dists_to_nullspace=dists,
    gauge_id_rank=int(np.linalg.svd(Gid, compute_uv=False).tolist().__len__() and
                      np.sum(np.linalg.svd(Gid, compute_uv=False) > 1e-8 *
                             np.linalg.svd(Gid, compute_uv=False)[0])),
    gauge_id_svals=[float(x) for x in np.linalg.svd(Gid, compute_uv=False)])

# ---------- final basis ----------
def jets_of(vec, ell):
    u = vec[0:NS]; v = vec[NS:2 * NS]
    w = vec[2 * NS:3 * NS] if ell >= 1 else np.zeros(NS)
    return dict(U=float(u[0]), Uprime=float(u[1] / RS), Upp=float(2 * u[2] / RS**2),
                Uppp=float(6 * u[3] / RS**3),
                V=float(v[0]), Vprime=float(v[1] / RS), Vpp=float(2 * v[2] / RS**2),
                Theta=float(w[0]), Thetaprime=float(w[1] / RS))
def coeffs_of(vec, ell):
    out = {'U': [float(x) for x in vec[0:NS]], 'V': [float(x) for x in vec[NS:2 * NS]]}
    if ell >= 1:
        out['W'] = [float(x) for x in vec[2 * NS:3 * NS]]
    return out

out = {'normalisation': ("Nullspace from W-B1 route-1 prolonged system at "
        "Sigma (P=4, K=8) with generous cut (row-equilibrated svals < 1e-6 "
        "relative); basis rotated so ID-space projections (u_0..u_3, "
        "v_0..v_3, w_0..w_3 of the scaled Taylor coefficients at Sigma) are "
        "orthonormal, taking the settled dimension (ell0=7 incl. named span, "
        "ell1=10, ell2=8, ell3=8); ell=0 (e) elements rotated within the "
        "settled space to be ID-orthogonal to the named span (3 MK tangents "
        "+ rescaling). Each element finally rescaled to unit max |Taylor "
        "coefficient| over k=0..8 (scale recorded). Jets: U,U',U'',U''', "
        "V,V',V'',Theta,Theta' at r=1000 of the rescaled element, with "
        "U(r)=sum_k u_k ((r-1000)/1000)^k."),
       'modes': {}}
for ell in [0, 1, 2, 3]:
    Z = bases_full[ell]
    idx = id_idx(ell)
    Pz = Z[idx, :]
    U_, sv, _ = np.linalg.svd(Pz, full_matrices=False)
    d = SETTLED[ell]
    Qid = U_[:, :d]
    C = np.linalg.pinv(Pz) @ Qid
    Bfull = Z @ C
    entry = dict(dimension=d, id_svals=[float(x) for x in sv])
    if ell == 0:
        Nid = np.stack([named[nm][idx] for nm in
                        ['dbeta', 'dgamma', 'dk', 'rescaling']], axis=1)
        Nid = Nid / np.linalg.norm(Nid, axis=0)
        coords = Qid.T @ Nid
        _, _, Vt = np.linalg.svd(coords.T, full_matrices=True)
        R = Vt[4:].T
        Efull = Bfull @ R
        eb = []
        for j in range(Efull.shape[1]):
            vec = Efull[:, j]
            scale = 1.0 / np.max(np.abs(vec)); vec = vec * scale
            eb.append(dict(scale_applied=float(scale),
                           taylor_coeffs=coeffs_of(vec, 0),
                           jet_at_Sigma=jets_of(vec, 0)))
        entry['e_basis'] = eb
        out['ell0_e_basis'] = eb
        entry['named'] = {nm: dict(
            taylor_coeffs=coeffs_of(named[nm] / np.max(np.abs(named[nm])), 0),
            jet_at_Sigma=jets_of(named[nm] / np.max(np.abs(named[nm])), 0))
            for nm in named}
    else:
        eb = []
        for j in range(Bfull.shape[1]):
            vec = Bfull[:, j]
            scale = 1.0 / np.max(np.abs(vec)); vec = vec * scale
            eb.append(dict(scale_applied=float(scale),
                           taylor_coeffs=coeffs_of(vec, ell),
                           jet_at_Sigma=jets_of(vec, ell)))
        entry['e_basis'] = eb
    out['modes'][f'ell{ell}'] = entry

with open('/home/hatch/workspace/warp-pilot/gate15/results/wb1_basis_jets.json', 'w') as fh:
    json.dump(out, fh, indent=1)
with open(base + '/wb1_basis_meta.json', 'w') as fh:
    json.dump(meta, fh, indent=1)
print('named dists (generous):', meta['named_ell0_generous'])
print('cross-centre:', {k: (v['d_at_900'], [round(x, 6) for x in v['basis_dists']])
                         for k, v in meta['cross_centre'].items()})
print('gauge ell1:', meta['gauge_ell1'])
for ell in [0, 1, 2, 3]:
    print('ell', ell, {k: (v['id_rank'], v['nullity']) for k, v in
                       meta['cut_sensitivity'][f'ell{ell}'].items()})
