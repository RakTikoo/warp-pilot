"""W-C fresh flat-patch principal-symbol verification (the controlling
computation behind P61-3, re-derived independently).

Linearised Bach operator on Minkowski, plane wave along z,
h_mn = e_mn exp(i(k z - w t)). On flat space the Ricci coupling term in
the Bach tensor vanishes at linear order (background Ricci = 0), so the
symbol is B_mn = -(k^a k^b) C^(1)_{a m b n} up to the overall sign from
(d d -> -k k), with C^(1) the linearised Weyl tensor. We build the
10x10 symbol matrix M(e) exactly (sympy, rational in w, k), verify:
 (i) gauge nullspace: e = k_m xi_n + k_n xi_m (4 diffeo) and e = eta_mn
     (1 conformal) are exact null directions for all (w,k);
 (ii) rank M = 5 off the cone;
 (iii) sector quotient eigenvalues: TT (x2), vector (x2), scalar (x1),
       each proportional to Q^2 with Q = w^2 - k^2, and the quotient
       determinant (product of the five physical eigenvalues);
 (iv) hence every physical dispersion is w^2 = k^2 with multiplicity
       two per polarisation in the (Box)^2 sense (double light cone):
       no tachyon branch, no c^2 != 1 branch.
Normalisation: the overall sign/scale of M follows the convention
B = nabla nabla C + ... as coded; sector RATIOS and the Q^2
factorisation are normalisation-free.
"""
import sympy as sp, json, os
w, k = sp.symbols('w k')
eta = sp.diag(-1, 1, 1, 1)
kcov = sp.Matrix([-w, 0, 0, k])              # k_m = d_m phase
kcon = eta * kcov                            # k^m
basis = []
for i in range(4):
    for j in range(i, 4):
        e = sp.zeros(4); e[i, j] = 1; e[j, i] = 1
        basis.append(((i, j), e))
def lin_weyl(e):
    # R^(1)_{abcd} = 1/2 (k_c k_b e_ad + k_d k_a e_bc - k_d k_b e_ac - k_c k_a e_bd)
    # with d_m -> i k_m, products give -k k; the overall -1 is kept in B below.
    R = [[[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    R[a][b][c][d] = sp.Rational(1, 2)*(
                        kcov[c]*kcov[b]*e[a, d] + kcov[d]*kcov[a]*e[b, c]
                        - kcov[d]*kcov[b]*e[a, c] - kcov[c]*kcov[a]*e[b, d])
    Ric = [[sum(eta[a, a]*R[a][b][a][d] for a in range(4)) for d in range(4)] for b in range(4)]
    Rsc = sum(eta[i, i]*Ric[i][i] for i in range(4))
    C = [[[[sp.Integer(0)]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    v = R[a][b][c][d]
                    v -= sp.Rational(1, 2)*(eta[a, c]*Ric[b][d] - eta[a, d]*Ric[b][c]
                                            - eta[b, c]*Ric[a][d] + eta[b, d]*Ric[a][c])
                    v += Rsc/6*(eta[a, c]*eta[b, d] - eta[a, d]*eta[b, c])
                    C[a][b][c][d] = sp.expand(v)
    return C
def bach_symbol(e):
    C = lin_weyl(e)
    B = sp.zeros(4)
    for m in range(4):
        for n in range(4):
            B[m, n] = sum(kcon[a]*kcon[b]*C[a][m][b][n] for a in range(4) for b in range(4))
    return B
# 10x10 matrix
M = sp.zeros(10)
for j, (_, e) in enumerate(basis):
    B = bach_symbol(e)
    for i, ((a, b), _e) in enumerate(basis):
        M[i, j] = sp.expand(B[a, b] * (1 if a == b else 1))
# NOTE: B is symmetric; coefficient of basis element (a,b), a<b, in B is B[a,b] itself.
out = {}
# (i) gauge nullspace, symbolic
xi = sp.symbols('xi0:4'); sg = sp.symbols('sg')
gauge_vecs = []
for mu in range(4):
    xv = [xi[i] if i == mu else 0 for i in range(4)]
    e = sp.Matrix(4, 4, lambda i, j: kcov[i]*xv[j] + kcov[j]*xv[i])
    gauge_vecs.append(e)
gauge_vecs.append(eta * sg)
null_checks = []
for e in gauge_vecs:
    B = bach_symbol(e)
    null_checks.append(bool(all(sp.expand(B[i, j]) == 0 for i in range(4) for j in range(4))))
out['gauge_null_directions_exact'] = null_checks  # 4 diffeo + 1 conformal, with symbolic amplitudes
# (ii)+(iii) numeric-symbolic point off cone: w=2, k=1 (Q=3), and w=3, k=1 (Q=8)
pts = {}
for (wv, kv) in [(2, 1), (3, 1), (2, 2)]:
    Mn = M.subs({w: wv, k: kv})
    ev = Mn.eigenvals()
    pts[f'w{wv}_k{kv}'] = {'rank': Mn.rank(),
                          'eigenvalues': {str(sp.nsimplify(key, rational=True)): int(val) for key, val in ev.items()},
                          'Q': wv*wv - kv*kv}
out['points'] = pts
# sector eigenvalues: TT e_xy and e_xx-e_yy ; vector e_xz ; scalar sector subspace
def sector_eig(e, label):
    B = bach_symbol(e)
    # find lambda with B = lambda * e on the support (check proportionality)
    lam = None; ok = True
    for i in range(4):
        for j in range(4):
            if e[i, j] != 0:
                l = sp.simplify(B[i, j]/e[i, j])
                if lam is None: lam = l
                elif sp.simplify(l - lam) != 0: ok = False
            elif sp.expand(B[i, j]) != 0: ok = False
    return label, (sp.factor(lam) if lam is not None else None), ok
res = {}
e_xy = sp.zeros(4); e_xy[1, 2] = 1; e_xy[2, 1] = 1
e_tt2 = sp.zeros(4); e_tt2[1, 1] = 1; e_tt2[2, 2] = -1
e_xz = sp.zeros(4); e_xz[1, 3] = 1; e_xz[3, 1] = 1
for e, lab in [(e_xy, 'TT_xy'), (e_tt2, 'TT_xx-yy'), (e_xz, 'vector_xz')]:
    lab2, lam, ok = sector_eig(e, lab)
    res[lab2] = {'eigenvalue': str(lam), 'is_eigenvector': ok}
out['sectors_direct'] = res
# scalar sector: invariant subspace spanned by tt, tz, zz, s=xx+yy (sym basis vecs)
idx = {ij: n for n, (ij, _) in enumerate(basis)}
scalar_basis_idx = [idx[(0, 0)], idx[(0, 3)], idx[(3, 3)], idx[(1, 1)], idx[(2, 2)]]
# use basis tt, tz, zz, xx+yy: build restricted matrix in that (non-orthonormal) basis
import itertools
def vec_of(e):
    return sp.Matrix([e[a, b] for (a, b), _ in basis])
def mat_of(v):
    e = sp.zeros(4)
    for n, ((a, b), _e) in enumerate(basis): e[a, b] = v[n]; e[b, a] = v[n]
    return e
sb = []
e_tt = sp.zeros(4); e_tt[0, 0] = 1
e_tz = sp.zeros(4); e_tz[0, 3] = 1; e_tz[3, 0] = 1
e_zz = sp.zeros(4); e_zz[3, 3] = 1
e_s = sp.zeros(4); e_s[1, 1] = 1; e_s[2, 2] = 1
sb = [e_tt, e_tz, e_zz, e_s]
P = sp.Matrix.hstack(*[vec_of(e) for e in sb])
Ms = sp.zeros(4)
for j, e in enumerate(sb):
    col = M * vec_of(e)
    sol = P.gauss_jordan_solve(col) if False else None
    # solve P x = col in least sense: P has rank 4 in 10-dim; use (P^T P)^{-1} P^T
    x = (P.T * P).inv() * P.T * col
    for i in range(4): Ms[i, j] = sp.expand(x[i])
out['scalar_sector_matrix'] = [[str(sp.factor(Ms[i, j])) for j in range(4)] for i in range(4)]
out['scalar_sector_eigenvalues'] = {str(sp.factor(key)): int(val) for key, val in Ms.eigenvals().items()}
out['scalar_sector_rank_generic_point'] = Ms.subs({w: 2, k: 1}).rank()
json.dump(out, open(os.path.expanduser('~/workspace/warp-pilot/gate9/results/wc_symbol.json'), 'w'), indent=1)
print(json.dumps(out, indent=1)[:3000], flush=True)
print('DONE', flush=True)
