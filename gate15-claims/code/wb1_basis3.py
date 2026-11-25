"""W-B1 final basis + classification anatomy (run after wb1_basis2.py for
wb1_basis_meta.json). Rebuilds the basis from wb1_projected.npz with the
settled dimensions, adds:
 - ell=1 gauge rotation: the 4-dim pure-gauge subspace (Y-polynomial family,
   X = -f r^2 Y') split from the 6-dim (e) quotient;
 - ell=2 gauge negative control (gauge triples NOT in the nullspace);
 - named ell=0 ID-space distances (settled span from wb1_nullspaces.npz).
Overwrites gate15/results/wb1_basis_jets.json and merges anatomy into
wb1_basis_meta.json.
"""
import numpy as np, json, sys
from math import comb
base = __file__.rsplit('/', 1)[0]
KMAX = 8; NS = KMAX + 1; RS = 1000.0
SETTLED = {0: 7, 1: 10, 2: 8, 3: 8}
P_ = np.load(base + '/wb1_projected.npz')
NZ = np.load(base + '/wb1_nullspaces.npz')

def build_M(P1, Pord, mmax=4):
    idx = [m + 6 for m in range(-mmax, mmax + 1)]
    ms = np.arange(-mmax, mmax + 1, dtype=float)
    V = np.stack([ms**p for p in range(Pord + 1)], axis=1)
    Fit = np.linalg.pinv(V)
    sub = P1[idx]
    return np.concatenate([Fit @ sub[:, ci, :] for ci in range(P1.shape[1])], axis=0)

def nullspace(M, cutrel=1e-6):
    norms = np.linalg.norm(M, axis=1)
    Ms = M[norms > 0] / norms[norms > 0, None]
    U, s, Vt = np.linalg.svd(Ms, full_matrices=True)
    rank = int(np.sum(s > cutrel * s[0]))
    return Vt[rank:].T

def id_idx(ell):
    nb = 2 if ell == 0 else 3
    return [blk * NS + k for blk in range(nb) for k in range(4)]

# series helpers
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
def sder(a):
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
finv = sinv(f_ser); finv2 = smul(finv, finv)
fp = sder(f_ser); finv_p = sder(finv)
named = {}
for nm, dA in [('dbeta', -3 * gamma - (2 - 6 * beta * gamma) * inv_r),
               ('dgamma', -3 * beta + 3 * beta**2 * inv_r + r_ser),
               ('dk', -r2_ser)]:
    dA = np.array(dA, dtype=float)
    named[nm] = np.concatenate([dA, smul(-dA, finv2)])
named['rescaling'] = np.concatenate([f_ser, np.zeros(NS)])

def gauge_vec(ell, j):
    Y = np.zeros(NS); Y[j] = 1.0
    Yp = sder(Y)
    X = -smul(smul(f_ser, r2_ser), Yp)
    Xp = sder(X)
    U = smul(fp, X)
    V = smul(X, finv_p) + 2 * smul(Xp, finv)
    Th = smul(X, 2 * inv_r) - ell * (ell + 1) * Y
    return np.concatenate([U, V, Th])

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
def pack(vec, ell):
    scale = 1.0 / np.max(np.abs(vec)); vec = vec * scale
    return dict(scale_applied=float(scale), taylor_coeffs=coeffs_of(vec, ell),
                jet_at_Sigma=jets_of(vec, ell))

meta = json.load(open(base + '/wb1_basis_meta.json'))
# named ID distances vs settled span (1e-8-cut Z)
Z0 = NZ['ell0_r1000_route1_P4_Z']; idx0 = id_idx(0)
U0, sv0, _ = np.linalg.svd(Z0[idx0, :], full_matrices=False)
Q0 = U0[:, :7]
meta['named_ell0_ID_dists'] = {}
for nm, v in named.items():
    gj = v[idx0]
    meta['named_ell0_ID_dists'][nm] = float(
        np.linalg.norm(gj - Q0 @ (Q0.T @ gj)) / np.linalg.norm(gj))
# ell=2 gauge negative control vs generous nullspace
Z2 = nullspace(build_M(P_['ell2_r1000_P1'], 4, 4))
dists2 = []
for j in range(4):
    gv = gauge_vec(2, j)
    coef, *_ = np.linalg.lstsq(Z2, gv, rcond=None)
    dists2.append(float(np.linalg.norm(Z2 @ coef - gv) / np.linalg.norm(gv)))
meta['gauge_ell2_negative_control_dists'] = dists2

out = {'normalisation': ("Nullspace from W-B1 route-1 prolonged system at "
        "Sigma (P=4, K=8, generous cut 1e-6 on row-equilibrated svals); "
        "basis rotated so ID-space projections (u_0..u_3, v_0..v_3, "
        "w_0..w_3 of scaled Taylor coefficients at Sigma) are orthonormal, "
        "taking the settled dimensions (solution space: ell0=7, ell1=10, "
        "ell2=8, ell3=8). ell=0 (e) elements are ID-orthogonal to the named "
        "span; ell=1 basis is split into a 4-dim pure-gauge part (class (a), "
        "the E_1=0 degeneracy) and a 6-dim (e) quotient. Each element is "
        "finally rescaled to unit max |Taylor coefficient| over k=0..8 "
        "(scale recorded). Jets: U,U',U'',U''',V,V',V'',Theta,Theta' at "
        "r=1000 of the rescaled element, U(r)=sum_k u_k ((r-1000)/1000)^k."),
       'modes': {}}
for ell in [0, 1, 2, 3]:
    Z = nullspace(build_M(P_[f'ell{ell}_r1000_P1'], 4, 4))
    idx = id_idx(ell)
    Pz = Z[idx, :]
    U_, sv, _ = np.linalg.svd(Pz, full_matrices=False)
    d = SETTLED[ell]
    Qid = U_[:, :d]
    C = np.linalg.pinv(Pz) @ Qid
    Bfull = Z @ C
    entry = dict(dimension_solution_space=d, id_svals=[float(x) for x in sv])
    if ell == 0:
        Nid = np.stack([named[nm][idx] for nm in
                        ['dbeta', 'dgamma', 'dk', 'rescaling']], axis=1)
        Nid = Nid / np.linalg.norm(Nid, axis=0)
        coords = Qid.T @ Nid
        _, _, Vt = np.linalg.svd(coords.T, full_matrices=True)
        Efull = Bfull @ Vt[4:].T
        entry['e_basis'] = [pack(Efull[:, j], 0) for j in range(Efull.shape[1])]
        out['ell0_e_basis'] = entry['e_basis']
        entry['named'] = {nm: dict(
            taylor_coeffs=coeffs_of(named[nm] / np.max(np.abs(named[nm])), 0),
            jet_at_Sigma=jets_of(named[nm] / np.max(np.abs(named[nm])), 0))
            for nm in named}
    elif ell == 1:
        Gid = np.stack([gauge_vec(1, j)[idx] for j in range(4)], axis=1)
        # gauge ID basis inside the settled span: project + orthonormalise
        Pg = Qid.T @ Gid                       # d x 4 coordinates in span
        Ug, svg, _ = np.linalg.svd(Pg, full_matrices=False)
        gdim = int(np.sum(svg > 1e-6 * svg[0]))
        Qg = Ug[:, :gdim]                      # span coords of gauge subspace
        entry['gauge_dim_in_span'] = gdim
        entry['gauge_id_svals_in_span'] = [float(x) for x in svg]
        Gfull = Bfull @ Qg
        entry['gauge_basis_class_a'] = [pack(Gfull[:, j], 1)
                                        for j in range(Gfull.shape[1])]
        # (e) quotient: span coords orthogonal to Qg
        _, _, Vtg = np.linalg.svd(Qg.T, full_matrices=True)
        Qe = Vtg[gdim:].T
        Efull = Bfull @ Qe
        entry['e_basis'] = [pack(Efull[:, j], 1) for j in range(Efull.shape[1])]
        entry['dimension_e_quotient'] = int(Efull.shape[1])
    else:
        entry['e_basis'] = [pack(Bfull[:, j], ell) for j in range(Bfull.shape[1])]
    out['modes'][f'ell{ell}'] = entry

with open('/home/hatch/workspace/warp-pilot/gate15/results/wb1_basis_jets.json', 'w') as fh:
    json.dump(out, fh, indent=1)
with open(base + '/wb1_basis_meta.json', 'w') as fh:
    json.dump(meta, fh, indent=1)
print('named ID dists:', meta['named_ell0_ID_dists'])
print('gauge ell2 control dists:', [round(x, 4) for x in dists2])
print('ell1 gauge_dim_in_span:', out['modes']['ell1']['gauge_dim_in_span'],
      'e quotient:', out['modes']['ell1']['dimension_e_quotient'])
