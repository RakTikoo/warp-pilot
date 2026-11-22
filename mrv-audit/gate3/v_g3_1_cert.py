"""
Gate-3 follow-up: BRANCH-INDEPENDENT, ACTION-LEVEL CERTIFICATION of the
sign of det K (even sector, l=2) for the MRV wormhole
(arXiv:1811.05832), at r = -20, -5, +5, +20.

WHY THIS ROUTE (see GATE3.md, Claim G3-1 verdict): V1's third route
reproduced the claimed signs on the distinguished regular EOM-row
elimination branch, but PROVED EOM-row elimination is branch-dependent
in sign (exact identity detK(elim k) = C_c(r) * detK(elim c); GR
control healthy on one branch, ghost-like on another).  EOM-row
elimination is an equivalence transformation, not a congruence, so
Sylvester's law does not protect it.  V1's named missing piece was the
action-level (congruence) reduction; its jet-space Schur complement
stalled on the skew odd-dimensional Wronskian (t,tr) block.

THIS ROUTE never enters jet space.  It works with the 5x5 action/EOM
symbol D(om) at k_r = 0 (V1's validated eom_coeffs; for a quadratic
action the EOM operator is its Hessian operator, so Schur complements
of D(om) are action-level eliminations).  Measured structure of the
symbol (both theories, all radii; see results JSON):
  * row a is om^0-ONLY (E1[a,:] = E2[a,:] = 0): a's equation is the
    Hamiltonian constraint.  In the designer theory D_aa = 0 to
    1e-10 (a is a strict Lagrange multiplier); in the GR control
    D_aa = 12.7 (a background-density self-term) -- immaterial here,
    because the reduction below uses only the row's om^0 character.
  * D_bb(om) = const != 0 (3.0 designer, 53.8 GR): b is a genuine
    auxiliary, eliminated by a 1x1 block Schur complement -- the same
    first step V1 took, and the only elimination performed.
  * the constraint row is untouched by b's elimination (D[a,b] = 0).
REDUCTION: K_phys := (the (i om)^2 coefficient of the b-eliminated
symbol's (c,k,x) block) RESTRICTED to the constraint surface
gamma^perp, gamma = the constraint row's (c,k,x) part.  Restricting a
quadratic form to a subspace is a congruence operation; every
parametrisation of the surface (solve the constraint for c, for k, or
for x; or an orthonormal basis) gives the same det sign, because any
two bases of the surface differ by an invertible R and det picks up
(det R)^2 > 0.  There is no branch.  The symmetric part of the
(i om)^2 coefficient is the action's kinetic form (the antisymmetric
part is the P_A Wronskian remnant of the frozen EOM normal form,
compensated in the full operator by (2,1)-sector terms); the raw
(nonsymmetrised) restriction is reported alongside and agrees in
sign at every point.

BRANCH-INDEPENDENCE IS DEMONSTRATED, not asserted:
  (a) all three solved-field parametrisations (the action-level
      images of V1's three EOM branches) give the same det sign at
      every radius, designer and GR -- including r = -20, where
      V1's elim-c branch flipped (-338.26 against the claim) and
      where the restriction in c-parametrisation gives +185.0;
  (b) random congruences preserving the sector structure (random
      invertible 3x3 mixing of (c,k,x); random nonzero rescalings
      of a and b) leave every det sign invariant;
  (c) the GR + canonical-scalar control returns a POSITIVE-DEFINITE
      K_phys at r = -5, +5 (healthy), on the same substrate where
      V1's row elimination gave +6717.02 / -6817.65 by branch;
  (d) the bordered-determinant identity det(Z^T K3 Z) =
      -det[[0, gamma^T],[gamma, K3]] / |gamma|^2 is verified
      numerically at every point (ties the restriction to a
      basis-free determinant);
  (e) FD-step variation of the substrate (h = 0.02, 0.04, 0.08)
      leaves every sign invariant.

SUBSTRATE: V1's angular-integrated Hessian (cached, work_cert/
Hint.pkl; 194 entries) via V1's Hderivs_fast/eom_coeffs; substrate
identity is re-proven in-run by reproducing V1's stored branch
det K values.  Designer functions are definitions from
phase3/p31_horndeski.py only, as in V1.  Symbol Schur complements in
exact rational arithmetic (sympy Rational, denominators limited to
1e12 -- far below the substrate's FD noise).  float64 inputs.
Nothing uploaded.
"""
import json
import os
import pickle
import sys
import time

import numpy as np
import sympy as sp

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate3')
os.chdir('/home/hatch/workspace/warp-pilot/gate3')
import v_g3_1 as v1  # noqa: E402

t0 = time.time()
FIELDS = v1.FIELDS  # ['a','b','c','k','x']
IA, IB = 0, 1
OM = sp.Symbol('om')


def log(*a):
    print(f'[{time.time() - t0:7.1f}s]', *a, flush=True)


# ---------------------------------------------------------------------------
# substrate
# ---------------------------------------------------------------------------
def load_hint():
    with open('work_cert/Hint.pkl', 'rb') as fh:
        raw = pickle.load(fh)
    by_name = {str(s): s for s in v1.JETS}
    return {(by_name[sa], by_name[sb]): e for (sa, sb), e in raw.items()}


Hint = load_hint()
Hfast = v1.make_Hfast(Hint)


def coeffs_at(r, subs_extra=None, h=0.04):
    Hs = v1.Hderivs_fast(Hfast, r, subs_extra=subs_extra, h=h)
    return v1.eom_coeffs(list(Hs))


def symbol_mats(e):
    """(E0, E1, E2) real 5x5, D(om) = E0 + (i om) E1 + (i om)^2 E2
    at k_r = 0."""
    return tuple(np.array([[e[(f, g, p, 0)] for g in FIELDS]
                           for f in FIELDS], dtype=np.float64)
                 for p in range(3))


# ---------------------------------------------------------------------------
# exact-rational symbol machinery
# ---------------------------------------------------------------------------
def rat(x):
    return sp.Rational(float(x)).limit_denominator(10**12)


def sym_of_mats(E):
    M = sp.zeros(5, 5)
    for i in range(5):
        for j in range(5):
            M[i, j] = (rat(E[0][i, j]) + sp.I * OM * rat(E[1][i, j])
                       - OM**2 * rat(E[2][i, j]))
    return M


def schur_block(M, keep, elim):
    P = M.extract(elim, elim)
    Pinv = P.inv()
    return sp.simplify(M.extract(keep, keep)
                       - M.extract(keep, elim) * Pinv
                       * M.extract(elim, keep))


def poly3(e):
    """(om^0, om^1, om^2) coefficients of a polynomial symbol entry
    (complex floats); asserts the denominator is constant."""
    e = sp.together(e)
    num, den = sp.fraction(e)
    pn, pd = sp.Poly(num, OM), sp.Poly(den, OM)
    assert pd.degree() == 0, f'denominator degree {pd.degree()}'
    return tuple(complex(pn.nth(p) / pd.nth(0)) if pn.degree() >= p
                 else 0.0j for p in range(3))


def laurent_iom2(e):
    """Coefficient of (i om)^2 in the Laurent expansion at infinity
    (= - coefficient of om^2).  Returns (real, imag)."""
    e = sp.together(e)
    num, den = sp.fraction(e)
    pn, pd = sp.Poly(num, OM), sp.Poly(den, OM)
    dn, dd = pn.degree(), pd.degree()
    if dn - dd < 2:
        return 0.0, 0.0
    if dn - dd > 2:
        raise RuntimeError(f'entry degree {dn-dd} > 2')
    c = complex(pn.nth(dn) / pd.nth(dd))
    return -c.real, -c.imag


# ---------------------------------------------------------------------------
# the reduction
# ---------------------------------------------------------------------------
def reduce_symbol(E):
    """Branch-independent reduction of the symbol coefficient
    matrices E = (E0, E1, E2).  Returns a diagnostics dict."""
    M = sym_of_mats(E)
    diag = {}
    diag['row_a_E1_max'] = float(np.max(np.abs(E[1][IA])))
    diag['row_a_E2_max'] = float(np.max(np.abs(E[2][IA])))
    diag['D_aa_E0'] = float(E[0][IA, IA])
    diag['D_bb_E0'] = float(E[0][IB, IB])
    diag['D_bb_E1'] = float(E[1][IB, IB])
    diag['D_bb_E2'] = float(E[2][IB, IB])
    # step 1: eliminate b (index 1) by 1x1 block Schur complement
    keep = [0, 2, 3, 4]                      # a, c, k, x
    M4 = schur_block(M, keep, [IB])
    # step 2: constraint row (row a of M4): om^0 part on (c,k,x);
    # record the om^1 / om^2 leakage
    gamma = np.zeros(3)
    leak = 0.0
    for j in range(3):
        c0, c1, c2 = poly3(M4[0, j + 1])
        gamma[j] = c0.real
        leak = max(leak, abs(c1), abs(c2))
    diag['gamma'] = gamma.tolist()
    diag['constraint_row_leakage'] = float(leak)
    diag['constraint_row_a_a'] = [complex(z) for z in poly3(M4[0, 0])]
    # step 3: K3 = (i om)^2 coefficient of the (c,k,x) block
    K3 = np.zeros((3, 3))
    imax = 0.0
    for i in range(3):
        for j in range(3):
            re, im = laurent_iom2(M4[i + 1, j + 1])
            K3[i, j] = re
            imax = max(imax, abs(im))
    diag['laurent_imag_max'] = float(imax)
    K3s = 0.5 * (K3 + K3.T)
    diag['K3_raw'] = K3.tolist()
    diag['K3_sym'] = K3s.tolist()
    diag['K3_antisym_max'] = float(np.max(np.abs(K3 - K3.T)) / 2)
    # step 4: restriction to gamma^perp (orthonormal basis via SVD)
    _, _, Vt = np.linalg.svd(gamma.reshape(1, 3))
    Z = Vt[1:].T
    Kp_sym = Z.T @ K3s @ Z
    Kp_raw = Z.T @ K3 @ Z
    diag['K_phys_sym'] = Kp_sym.tolist()
    diag['K_phys_eigs'] = np.linalg.eigvalsh(Kp_sym).tolist()
    diag['det'] = float(np.linalg.det(Kp_sym))
    diag['det_raw'] = float(np.linalg.det(Kp_raw))
    diag['sign'] = 'negative' if diag['det'] < 0 else 'positive'
    diag['sign_raw'] = 'negative' if diag['det_raw'] < 0 else 'positive'
    # step 5: solved-field parametrisations of the same surface
    par = {}
    names = ['c', 'k', 'x']
    for fstar in range(3):
        if abs(gamma[fstar]) < 1e-3 * np.max(np.abs(gamma)):
            par[names[fstar]] = None
            continue
        idx = [i for i in range(3) if i != fstar]
        Zs = np.zeros((3, 2))
        for c_, i_ in enumerate(idx):
            Zs[i_, c_] = 1.0
            Zs[fstar, c_] = -gamma[i_] / gamma[fstar]
        d = float(np.linalg.det(Zs.T @ K3s @ Zs))
        par[names[fstar]] = dict(det=d,
                                 sign='negative' if d < 0 else 'positive')
    diag['parametrisations'] = par
    # step 6: bordered-determinant identity
    B = np.zeros((4, 4))
    B[0, 1:] = gamma
    B[1:, 0] = gamma
    B[1:, 1:] = K3s
    lhs = diag['det']
    rhs = -float(np.linalg.det(B)) / float(gamma @ gamma)
    diag['bordered_identity'] = dict(lhs=lhs, rhs=rhs,
                                     rel_dev=abs(lhs - rhs)
                                     / max(abs(lhs), 1e-30))
    return diag


def det_symbol_leading(E, omegas=(2000.0, 4000.0)):
    """Leading behaviour of det D(om): det / om^4 at large om
    (2 physical DOF -> om^4).  Returns the stabilised real value."""
    vals = []
    for om in omegas:
        D = E[0] + 1j * om * E[1] - om**2 * E[2]
        vals.append(np.linalg.det(D) / om**4)
    return vals


def transform_coeffs(E, S):
    return tuple(S.T @ Ep @ S for Ep in E)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    res = {'task': 'G3-1 certification follow-up: branch-independent '
                   'action-level sign of det K (even sector, l=2)',
           'route': 'b eliminated by block Schur complement of the '
                    'action/EOM symbol; (i om)^2 coefficient '
                    'restricted to the Hamiltonian-constraint '
                    'surface; exact rational arithmetic',
           'radii': {}}
    stored = json.load(open('results/v_g3_1.json'))

    # ---- substrate identity: reproduce V1's branch values
    log('substrate identity check vs V1 stored JSON...')
    ident = {}
    for r in (-20.0, -5.0, 5.0, 20.0):
        e = coeffs_at(r)
        dk, pair, piv = v1.detK_branch(e, 'k')
        ref = stored['points'][str(int(r))]['x_eliminated_k']['detK']
        ident[str(int(r))] = dict(mine=dk, v1_stored=ref,
                                  rel_dev=abs(dk - ref) / abs(ref))
        log(f'  r={r:+.0f}: elim-k detK mine {dk:+.10g} vs stored '
            f'{ref:+.10g}')
    res['substrate_identity'] = ident

    claimed = {-20.0: 'positive', -5.0: 'negative', 5.0: 'negative',
               20.0: 'positive'}

    # ---- certification at the four radii (designer theory)
    for r in (-20.0, -5.0, 5.0, 20.0):
        E = symbol_mats(coeffs_at(r))
        out = reduce_symbol(E)
        out['claimed_sign'] = claimed[r]
        out['matches_claim'] = (out['sign'] == claimed[r])
        out['det_symbol_over_om4'] = [
            complex(z) for z in det_symbol_leading(E)]
        res['radii'][str(int(r))] = out
        log(f'r={r:+.0f}: det K_phys = {out["det"]:+.8g} '
            f'(raw {out["det_raw"]:+.8g}), eigs '
            f'{np.round(out["K_phys_eigs"], 4)}, '
            f'sign {out["sign"]} (claim {claimed[r]})')

    # ---- GR control
    gr = {}
    for r in (-5.0, 5.0):
        E = symbol_mats(coeffs_at(r, subs_extra=v1.GR_SUBS))
        out = reduce_symbol(E)
        out['positive_definite'] = bool(np.all(
            np.array(out['K_phys_eigs']) > 0))
        gr[str(int(r))] = out
        log(f'GR r={r:+.0f}: det {out["det"]:+.8g}, eigs '
            f'{np.round(out["K_phys_eigs"], 4)}, posdef '
            f'{out["positive_definite"]}')
    res['GR_control'] = gr

    # ---- congruence invariance within the sector structure
    rng = np.random.default_rng(20261121)
    cong = {}

    def rand_sector_S():
        while True:
            T = np.eye(3) + 0.7 * rng.standard_normal((3, 3))
            if np.linalg.cond(T) < 20:
                break
        S = np.eye(5)
        S[0, 0] = rng.uniform(0.5, 2.0) * rng.choice([-1, 1])
        S[1, 1] = rng.uniform(0.5, 2.0) * rng.choice([-1, 1])
        S[2:, 2:] = T
        return S

    for tag, subs, radii in (('designer', None, (-20.0, -5.0, 5.0, 20.0)),
                             ('GR', v1.GR_SUBS, (-5.0, 5.0))):
        for r in radii:
            E = symbol_mats(coeffs_at(r, subs_extra=subs))
            base = (res['radii'][str(int(r))] if tag == 'designer'
                    else res['GR_control'][str(int(r))])
            rows = []
            for trial in range(3):
                S = rand_sector_S()
                out = reduce_symbol(transform_coeffs(E, S))
                rows.append(dict(
                    trial=trial, det=out['det'], sign=out['sign'],
                    invariant=(out['sign'] == base['sign'])))
                log(f'  cong {tag} r={r:+.0f} t{trial}: det '
                    f'{out["det"]:+.8g} sign {out["sign"]} '
                    f'(base {base["sign"]})')
            cong[f'{tag}{int(r)}'] = rows
    res['congruence_invariance'] = cong
    res['congruence_all_invariant'] = bool(all(
        row['invariant'] for rows in cong.values() for row in rows))

    # ---- FD-step robustness
    hrob = {}
    for r in (-20.0, -5.0, 5.0, 20.0):
        rows = {}
        for h in (0.02, 0.08):
            E = symbol_mats(coeffs_at(r, h=h))
            out = reduce_symbol(E)
            rows[str(h)] = dict(det=out['det'], sign=out['sign'],
                                invariant=(out['sign']
                                           == res['radii']
                                           [str(int(r))]['sign']))
            log(f'  h={h} r={r:+.0f}: det {out["det"]:+.8g} '
                f'sign {out["sign"]}')
        hrob[str(int(r))] = rows
    res['h_robustness'] = hrob
    res['h_all_invariant'] = bool(all(
        row['invariant'] for rows in hrob.values() for row in
        rows.values()))

    signs_ok = all(res['radii'][str(int(r))]['matches_claim']
                   for r in (-20.0, -5.0, 5.0, 20.0))
    gr_ok = all(res['GR_control'][str(int(r))]['positive_definite']
                for r in (-5.0, 5.0))
    par_ok = all(
        p is None or p['sign'] == res['radii'][str(int(r))]['sign']
        for r in (-20.0, -5.0, 5.0, 20.0)
        for p in res['radii'][str(int(r))]['parametrisations'].values())
    par_ok = par_ok and all(
        p is None or p['sign'] == res['GR_control'][str(int(r))]['sign']
        for r in (-5.0, 5.0)
        for p in res['GR_control'][str(int(r))]
        ['parametrisations'].values())
    res['parametrisations_all_invariant'] = bool(par_ok)
    res['verdict'] = (
        'CERTIFIED' if (signs_ok and gr_ok and par_ok
                        and res['congruence_all_invariant']
                        and res['h_all_invariant'])
        else 'NOT CERTIFIED — see per-item results')
    log('verdict:', res['verdict'])
    with open('results/v_g3_1_cert.json', 'w') as fh:
        json.dump(res, fh, indent=2, default=str)
    return res


if __name__ == '__main__':
    main()
