"""W-B1 kappa anchor: reproduce kappa_full (restricted set) and
kappa_enlarged = 0 from Phase 91's STORED data (phase91/results/
p911_results.json + phase91/work/p911_functionals.json) using this
worker's own solve code (mpmath, 40 digits), plus the (e)-basis response
columns computed from W-B1's own settled basis jets at Sigma
(wb1_basis_jets.json, produced by wb1_basis.py) through the stored
linearised channel functionals LR / LK / [B]=V.
Writes wb1_kappa.json."""
import json, sys
from mpmath import mp, mpf, matrix as mpmatrix
mp.dps = 40
base = __file__.rsplit('/', 1)[0]
stored = json.load(open('/home/hatch/workspace/warp-pilot/phase91/results/p911_results.json'))
func = json.load(open('/home/hatch/workspace/warp-pilot/phase91/work/p911_functionals.json'))

# stored response matrix (rows [B],[K],[Rt]; cols beta, k) - stored data
Mstored = stored['anchors']['A1_truncation_control']['stored_response_matrix']
M = mpmatrix(3, 2)
for i in range(3):
    for j in range(2):
        M[i, j] = mpf(str(Mstored[i][j]))
# stored full-system jump vector per unit eps (eps=0.01 row, string data)
jv = stored['deciding']['jumps_full_per_eps']['0.01']
j = mpmatrix([mpf(x) for x in jv])

# restricted solve: (beta,k) from ([B],[K]) exactly, residual on [Rt]
A = mpmatrix(2, 2); A[0, 0], A[0, 1] = M[0, 0], M[0, 1]
A[1, 0], A[1, 1] = M[1, 0], M[1, 1]
sol = mpmatrix([mpf(0), mpf(0)])
# Cramer
det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
sol[0] = (-j[0] * A[1, 1] + j[1] * A[0, 1]) / det
sol[1] = (-A[0, 0] * j[1] + A[1, 0] * j[0]) / det
kappa_full = j[2] + M[2, 0] * sol[0] + M[2, 1] * sol[1]

out = dict(kappa_full_recomputed=float(kappa_full),
           kappa_full_stored=stored['verdict']['kappa_full_per_eps'],
           dbeta_restricted=float(sol[0]), dk_restricted=float(sol[1]),
           rel_diff=float(abs(kappa_full / mpf(str(stored['verdict']['kappa_full_per_eps'])) - 1)))

# enlarged: columns (beta, k) + W-B1's three ell=0 (e) basis responses
try:
    basis = json.load(open('/home/hatch/workspace/warp-pilot/gate15/results/wb1_basis_jets.json'))
    LR, LK = func['LR'], func['LK']
    def response(jet):
        U = [jet['U'], jet['Uprime'], jet['Upp'], jet['Uppp']]
        V = [jet['V'], jet['Vprime']]
        Bch = jet['V']
        Kch = LK['U0'] * U[0] + LK['U1'] * U[1] + LK['V0'] * V[0]
        Rch = (LR['U0'] * U[0] + LR['U1'] * U[1] + LR['U2'] * U[2]
               + LR['V0'] * V[0] + LR['V1'] * V[1])
        return [Bch, Kch, Rch]
    cols = [[float(M[i, 0]) for i in range(3)], [float(M[i, 1]) for i in range(3)]]
    for e in basis['ell0_e_basis']:
        cols.append(response(e['jet_at_Sigma']))
    import numpy as np
    R = np.array(cols).T  # 3 x 5
    jn = np.array([float(x) for x in jv])
    coef, res, rank, sv = np.linalg.lstsq(R, -jn, rcond=None)
    resid = jn + R @ coef
    # headline: exact 3x3 solve with (beta, k, first (e) direction)
    A3 = R[:, [0, 1, 2]]
    sol3 = np.linalg.solve(A3, -jn)
    resid3 = jn + A3 @ sol3
    out['enlarged'] = dict(response_rank=int(rank),
                           response_svals=[float(x) for x in sv],
                           lstsq_solve_residual=[float(x) for x in resid],
                           lstsq_residual_norm=float(np.linalg.norm(resid)),
                           exact_3x3=dict(
                               amplitudes=dict(dbeta=float(sol3[0]),
                                               dk=float(sol3[1]),
                                               e0=float(sol3[2])),
                               residual=[float(x) for x in resid3],
                               kappa_enlarged=float(resid3[2])),
                           kappa_enlarged=float(resid3[2]))
except FileNotFoundError:
    out['enlarged'] = 'wb1_basis_jets.json not yet present'
with open(base + '/wb1_kappa.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1)[:2000])
