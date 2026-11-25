"""W-B1 basis extraction at Sigma from the settled nullspaces
(wb1_nullspaces.npz, route-1 P=4 K=8 at r0=1000).

Normalisation (stated exactly): for each mode, the nullspace basis is first
rotated so that its projections onto the initial-data space
(u_0..u_3, v_0..v_3, w_0..w_3) (scaled Taylor coefficients at Sigma) are
orthonormal (SVD of the ID projection). At ell=0 the three (e) elements are
then rotated within the settled 7-dim space to be ID-orthogonal to the four
named vectors (3 MK tangents + constant rescaling). Finally each basis
element is rescaled so that its largest |Taylor coefficient| over all
blocks k=0..8 equals 1 (the scale factor is recorded; jets are those of the
rescaled element).
Writes wb1_basis_jets.json (in gate15/results/) and wb1_basis_meta.json.
"""
import numpy as np, json, sys
import sympy as sp
base = __file__.rsplit('/', 1)[0]
KMAX = 8
RS = 1000.0

Z = np.load(base + '/wb1_nullspaces.npz')

def id_idx(ell):
    nb = 2 if ell == 0 else 3
    return [blk * (KMAX + 1) + k for blk in range(nb) for k in range(4)]

def jets_of(vec, ell):
    nb = 2 if ell == 0 else 3
    u = vec[0 * (KMAX + 1):1 * (KMAX + 1)]
    v = vec[1 * (KMAX + 1):2 * (KMAX + 1)]
    w = vec[2 * (KMAX + 1):3 * (KMAX + 1)] if nb == 3 else np.zeros(KMAX + 1)
    return dict(U=float(u[0]), Uprime=float(u[1] / RS), Upp=float(2 * u[2] / RS**2),
                Uppp=float(6 * u[3] / RS**3),
                V=float(v[0]), Vprime=float(v[1] / RS), Vpp=float(2 * v[2] / RS**2),
                Theta=float(w[0]), Thetaprime=float(w[1] / RS))

def coeffs_of(vec, ell):
    nb = 2 if ell == 0 else 3
    out = {}
    for blk, nm in enumerate(['U', 'V', 'W']):
        if blk < nb:
            out[nm] = [float(x) for x in vec[blk * (KMAX + 1):(blk + 1) * (KMAX + 1)]]
    return out

# ---- named ell=0 vectors: analytic power series in x=(r-1000)/1000 ----
beta, gamma, kk = 2.142611, 1e-28, -2.28996e-9
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
inv_r = np.array([(-1.0)**k / RS for k in range(NS)])       # 1/r, r=RS(1+x)
r_ser = np.zeros(NS); r_ser[0] = RS; r_ser[1] = RS          # r
r2_ser = np.zeros(NS); r2_ser[0] = RS**2; r2_ser[1] = 2 * RS**2; r2_ser[2] = RS**2
Cpar = beta * (2 - 3 * beta * gamma)
f_ser = -Cpar * inv_r + gamma * r_ser - kk * r2_ser
f_ser[0] += 1 - 3 * beta * gamma
finv2 = smul(sinv(f_ser), sinv(f_ser))
named = {}
for nm, dA in [('dbeta', -3 * gamma - (2 - 6 * beta * gamma) * inv_r),
               ('dgamma', -3 * beta + 3 * beta**2 * inv_r + r_ser),
               ('dk', -r2_ser)]:
    dA = np.array(dA, dtype=float)
    named[nm] = np.concatenate([dA, smul(-dA, finv2)])
named['rescaling'] = np.concatenate([f_ser, np.zeros(NS)])

out = {'normalisation': ("Basis constructed by orthonormalising the ID-space "
        "(u_0..u_3,v_0..v_3,w_0..w_3) projections of the settled nullspace "
        "(route-1, P=4, K=8, r0=Sigma); ell=0 (e) elements rotated to be "
        "ID-orthogonal to the named span; each element then rescaled to unit "
        "max |Taylor coefficient| over k=0..8 (scale recorded). Jets are "
        "U,U',U'',U''' ,V,V',V'',Theta,Theta' at r=1000 of the rescaled element, "
        "with U(r)=sum_k u_k ((r-1000)/1000)^k."),
       'modes': {}}
meta = {'named_ell0': {}}

for ell in [0, 1, 2, 3]:
    Zn = Z[f'ell{ell}_r1000_route1_P4_Z']  # N x nullity
    idx = id_idx(ell)
    Pz = Zn[idx, :]
    U_, sv, _ = np.linalg.svd(Pz, full_matrices=False)
    d = int(np.sum(sv > 1e-8 * sv[0]))
    Qid = U_[:, :d]
    C = np.linalg.pinv(Pz) @ Qid
    Bfull = Zn @ C  # ID projections are Qid (orthonormal)
    entry = dict(dimension=d, id_svals=[float(s) for s in sv])
    if ell == 0:
        # named identification
        named_id = {}
        for nm, vec in named.items():
            # distance of the named vector to the nullspace (full space)
            coef, *_ = np.linalg.lstsq(Zn, vec, rcond=None)
            dist = float(np.linalg.norm(Zn @ coef - vec) / np.linalg.norm(vec))
            named_id[nm] = dict(nullspace_dist=dist,
                                jet_at_Sigma=jets_of(vec / np.max(np.abs(vec)), 0))
        meta['named_ell0'] = named_id
        # (e) rotation: ID-orthogonal to named ID span inside Qid span
        Nid = np.stack([named[nm][idx] for nm in
                        ['dbeta', 'dgamma', 'dk', 'rescaling']], axis=1)
        Nid = Nid / np.linalg.norm(Nid, axis=0)
        coords = Qid.T @ Nid  # d x 4
        _, _, Vt = np.linalg.svd(coords.T, full_matrices=True)
        R = Vt[4:].T  # d x (d-4): ID-orthogonal complement directions
        Efull = Bfull @ R
        eb = []
        for j in range(Efull.shape[1]):
            vec = Efull[:, j]
            scale = 1.0 / np.max(np.abs(vec))
            vec = vec * scale
            eb.append(dict(scale_applied=float(scale),
                           taylor_coeffs=coeffs_of(vec, 0),
                           jet_at_Sigma=jets_of(vec, 0)))
        entry['e_basis'] = eb
        out['ell0_e_basis'] = eb
        # named jets (unit-max normalised) also exported
        entry['named'] = {nm: dict(taylor_coeffs=coeffs_of(
            named[nm] / np.max(np.abs(named[nm])), 0),
            jet_at_Sigma=jets_of(named[nm] / np.max(np.abs(named[nm])), 0))
            for nm in named}
    else:
        eb = []
        for j in range(Bfull.shape[1]):
            vec = Bfull[:, j]
            scale = 1.0 / np.max(np.abs(vec))
            vec = vec * scale
            eb.append(dict(scale_applied=float(scale),
                           taylor_coeffs=coeffs_of(vec, ell),
                           jet_at_Sigma=jets_of(vec, ell)))
        entry['e_basis'] = eb
    out['modes'][f'ell{ell}'] = entry

with open('/home/hatch/workspace/warp-pilot/gate15/results/wb1_basis_jets.json', 'w') as fh:
    json.dump(out, fh, indent=1)
with open(base + '/wb1_basis_meta.json', 'w') as fh:
    json.dump(meta, fh, indent=1)
print('basis done; named dists:',
      {k: v['nullspace_dist'] for k, v in meta['named_ell0'].items()})
print('dims:', {k: out['modes'][k]['dimension'] for k in out['modes']})
