#!/usr/bin/env python3
"""
p152_eom.py -- Phase 15 SA-2 verdict components (C4, C5, C6 of
CHECKPOINT15.md continuation), per beta, from the cached scan
bases (results/p152_bases_beta*.npz) and the scan's best rows.

C6 chi-EOM residual: box chi by FD on the solved chi field
     (chi re-solved pointwise from Q at offset points), h in
     {0.3, 0.15}; fraction |box chi| / |lambda Q chi| at open
     binding points (bar 0.10), h-convergence reported.
C4 conservation read: nabla_a Chat^{ab} by FD on the ASSEMBLED
     Chat field of the best row (offsets share one basis
     evaluation), Gamma-corrected; reported absolutely and
     relative to |Chat|_F / L_wall, L_wall = 10.  This is the
     numerical size of the labelled "u-EOM residual open".
C5 completeness diagnostic: C_extra = C_chi + C_int^expl at
     binding points.  C_chi is exact (canonical scalar:
     C = -1/2 g L_chi - 1/2 dchi dchi).  C_int^expl is the
     explicit-metric part of the interaction term's variation
     (pointwise FD in g^{ab} at fixed Dm, u, chi; the
     derivative/Mdiv-type part is NOT bounded by this
     diagnostic and is labelled a red-team derivation item).
     Trigger: |C_extra| >= 0.25 |Chat_best| at any binding
     point (norm sqrt(T_ab T^ab)).

float64.  System python3.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase15')
import p152_lib as L          # noqa: E402
import p93_tensor as tn       # noqa: E402
import verify_metric as vm    # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/phase15/results'
STEN = ((-2, 1.0), (-1, -8.0), (1, 8.0), (2, -1.0))


def chi_at(gf, pts, qc):
    Q, _, _ = L.Q_at(gf, pts)
    chi, _ = L.chi_S(Q, qc)
    return chi, Q


def box_chi(gf, centers, qc, h):
    """box chi at centers via FD on the re-solved chi field."""
    P = len(centers)
    # gather all offset points in one batch
    offs = {}   # (kind, e, k) -> slice
    pts_all = [centers]
    idx = {}
    pos = P
    for e in range(3):
        for k, _w in STEN:
            o = np.zeros(3)
            o[e] = k * h
            idx[('ax', e, k)] = slice(pos, pos + P)
            pts_all.append(centers + o)
            pos += P
    for (e, f) in ((0, 1), (0, 2), (1, 2)):
        for se in (-1, 1):
            for sf in (-1, 1):
                o = np.zeros(3)
                o[e] = se * h
                o[f] = sf * h
                idx[('mix', e, f, se, sf)] = slice(pos, pos + P)
                pts_all.append(centers + o)
                pos += P
    allpts = np.concatenate(pts_all)
    chi_all, _ = chi_at(gf, allpts, qc)
    chi0 = chi_all[:P]
    D1 = np.zeros((P, 4))
    D2 = np.zeros((P, 4, 4))
    for e in range(3):
        cp2 = chi_all[idx[('ax', e, 2)]]
        cp1 = chi_all[idx[('ax', e, 1)]]
        cm1 = chi_all[idx[('ax', e, -1)]]
        cm2 = chi_all[idx[('ax', e, -2)]]
        D1[:, e + 1] = (-cp2 + 8 * cp1 - 8 * cm1 + cm2) / (12 * h)
        D2[:, e + 1, e + 1] = (-cp2 + 16 * cp1 - 30 * chi0
                               + 16 * cm1 - cm2) / (12 * h * h)
    for (e, f) in ((0, 1), (0, 2), (1, 2)):
        cpp = chi_all[idx[('mix', e, f, 1, 1)]]
        cpm = chi_all[idx[('mix', e, f, 1, -1)]]
        cmp_ = chi_all[idx[('mix', e, f, -1, 1)]]
        cmm = chi_all[idx[('mix', e, f, -1, -1)]]
        D2[:, e + 1, f + 1] = (cpp - cpm - cmp_ + cmm) / (4 * h * h)
        D2[:, f + 1, e + 1] = D2[:, e + 1, f + 1]
    Gamma, g, ginv = vm._gamma_at(gf, centers, 0.3)
    # Gamma[p,a,b,c] = Gamma^c_{ab}; box = g^ab (D2_ab - G^c_ab D1_c)
    corr = np.einsum('pabc,pc->pab', Gamma, D1)
    box = np.einsum('pab,pab->p', ginv, D2 - corr)
    return box, D1, chi0


def Q_of_ginv(ginv, Dm, u_up):
    """Q(ginv, Dm, u) for the interaction explicit variation."""
    g = np.linalg.inv(ginv)
    u_cov = np.einsum('pab,pb->pa', g, u_up)
    Dcov = np.einsum('pbc,pac->pab', g, Dm)
    Pmix = np.eye(4)[None] + np.einsum('pa,pb->pab', u_up, u_cov)
    M = np.einsum('pca,pcd,pdb->pab', Pmix, Dcov, Pmix)
    Q1 = np.einsum('pab,pcd,pac,pbd->p', M, M, ginv, ginv)
    a_up = np.einsum('pa,pac->pc', u_up, Dm)
    a_cov = np.einsum('pab,pb->pa', g, a_up)
    Q2 = np.einsum('pa,pa->p', a_up, a_cov)
    return Q1 + Q2


def expl_fd_Lint(fc, chi, eps=1e-5):
    """E_expl of L_int = +1/2 lam chi^2 Q at fixed Dm, u, chi."""
    ginv, Dm, u_up = fc['ginv'], fc['Dm'], fc['u_up']
    P = len(Dm)
    E = np.zeros((P, 4, 4))
    for m in range(4):
        for n in range(m, 4):
            gp = ginv.copy()
            gm = ginv.copy()
            gp[:, m, n] += eps
            gm[:, m, n] -= eps
            if n != m:
                gp[:, n, m] += eps
                gm[:, n, m] -= eps
            Lp = 0.5 * L.LAM * chi**2 * Q_of_ginv(gp, Dm, u_up)
            Lm = 0.5 * L.LAM * chi**2 * Q_of_ginv(gm, Dm, u_up)
            fac = 2.0 * eps if m == n else 4.0 * eps
            E[:, m, n] = (Lp - Lm) / fac
            E[:, n, m] = E[:, m, n]
    return E


def tnorm(T, g, ginv):
    Tup = np.einsum('pac,pcd,pdb->pab', ginv, T, ginv)
    return np.sqrt(np.maximum(
        np.einsum('pab,pab->p', T, Tup), 0.0))


def run_beta(beta, qc, best_c0):
    t0 = time.time()
    bd = L.bed(beta)
    z = np.load(f'{RES}/p152_bases_beta{beta}.npz')
    Sb, chib, Qb = z['S_b'], z['chi_b'], z['Q_b']
    basis_b = list(z['basis_b'])
    out = dict(beta=beta, best_c0=list(best_c0))

    # ---- C6: chi residual at two h ----
    res = {}
    D1_03 = None
    for h in (0.3, 0.15):
        box, D1, chi0 = box_chi(bd['gf'], bd['pts_b'], qc, h)
        if h == 0.3:
            D1_03 = D1
        open_ = chi0 > 0
        denom = np.abs(L.LAM * Qb * chi0)
        frac = np.where(open_ & (denom > 0),
                        np.abs(box) / np.maximum(denom, 1e-300),
                        np.nan)
        res[str(h)] = dict(
            frac_max_open=float(np.nanmax(frac)),
            frac_med_open=float(np.nanmedian(frac)),
            box_absmax=float(np.max(np.abs(box))),
            box_absmax_open=float(np.max(np.abs(box[open_]))))
        print(f'beta={beta} C6 h={h}: frac max '
              f'{res[str(h)]["frac_max_open"]:.3e} med '
              f'{res[str(h)]["frac_med_open"]:.3e} '
              f'({time.time()-t0:.0f}s)', flush=True)
    out['chi_residual'] = res

    # ---- C5: C_extra at binding points ----
    fc = tn.field(bd['gf'], bd['pts_b'], 0.3, L.U_TILT,
                  (0.0, 0.0, 0.0, 0.0), h_fd=0.15)
    g, ginv = fc['g'], fc['ginv']
    m2 = qc
    mu = 2.0 * qc / L.CHI_V**2
    V = 0.5 * m2 * chib**2 + 0.25 * mu * chib**4
    Xchi = np.einsum('pab,pa,pb->p', ginv, D1_03, D1_03)
    Lchi = -0.5 * Xchi - V
    C_chi = -0.5 * g * Lchi[:, None, None] \
        - 0.5 * np.einsum('pa,pb->pab', D1_03, D1_03)
    Lint = 0.5 * L.LAM * chib**2 * Qb
    C_int = -0.5 * g * Lint[:, None, None] + expl_fd_Lint(fc, chib)
    C_extra = C_chi + C_int
    cs0 = np.array(L.cs_of(*best_c0))
    Chat_b = sum((Sb * cs0[i])[:, None, None] * basis_b[i]
                 for i in range(4))
    # sizes as Frobenius norms of the orthonormal-frame tensors
    That_extra = vm.eulerian_that(g, C_extra)
    n_extra = np.sqrt(np.einsum('pab,pab->p', That_extra,
                                That_extra))
    n_chat = np.sqrt(np.einsum('pab,pab->p', Chat_b, Chat_b))
    ratio = n_extra / np.maximum(n_chat, 1e-300)
    out['C_extra'] = dict(
        ratio_max=float(np.max(ratio)),
        ratio_med=float(np.median(ratio)),
        frac_pts_ge_0p25=float(np.mean(ratio >= 0.25)),
        trigger=bool(np.max(ratio) >= 0.25),
        note='explicit-metric part of C_int only; Mdiv-type part '
             'not bounded by this diagnostic')
    print(f'beta={beta} C5: |C_extra|/|Chat| max '
          f'{out["C_extra"]["ratio_max"]:.3f} med '
          f'{out["C_extra"]["ratio_med"]:.3f} '
          f'({time.time()-t0:.0f}s)', flush=True)

    # ---- C4: conservation of assembled Chat (best row) ----
    centers = bd['pts_b'][::3]
    sl = np.arange(0, len(bd['pts_b']), 3)
    h = 0.3
    pts_all = [centers]
    idx = {}
    pos = len(centers)
    for e in range(3):
        for k, _w in STEN:
            o = np.zeros(3)
            o[e] = k * h
            idx[(e, k)] = slice(pos, pos + len(centers))
            pts_all.append(centers + o)
            pos += len(centers)
    allpts = np.concatenate(pts_all)
    Qall, _, _ = L.Q_at(bd['gf'], allpts)
    _call, Sall = L.chi_S(Qall, qc)
    Chat_all = np.zeros((len(allpts), 4, 4))
    for i in range(4):
        Ci = tn.C_aether(bd['gf'], allpts, 0.3, L.U_TILT,
                         tuple(1.0 if j == i else 0.0
                               for j in range(4)),
                         lam_sign=-1.0, h_fd=0.15)
        Chat_all += (Sall * cs0[i])[:, None, None] * Ci
    gall = bd['gf'](allpts)
    ginvall = np.linalg.inv(gall)
    Tup_all = np.einsum('pac,pcd,pdb->pab', ginvall, Chat_all,
                        ginvall)
    Pc = len(centers)
    dT = np.zeros((Pc, 4, 4, 4))   # dT[:, e, a, b] = d_e T^{ab}
    for e in range(3):
        acc = np.zeros((Pc, 4, 4))
        for k, w in STEN:
            acc += w * Tup_all[idx[(e, k)]]
        dT[:, e + 1] = acc / (12 * h)
    Gamma, gc, ginvc = vm._gamma_at(bd['gf'], centers, 0.3)
    Tup_c = Tup_all[:Pc]
    # nabla_a T^{ab} = d_a T^{ab} + Gamma^a_{ac} T^{cb}
    #                  + Gamma^b_{ac} T^{ac},
    # Gamma[p,i,j,k] = Gamma^k_{ij} (vm convention, cf. tn.field)
    div = np.einsum('peeb->pb', dT) \
        + np.einsum('paca,pcb->pb', Gamma, Tup_c) \
        + np.einsum('pacb,pac->pb', Gamma, Tup_c)
    div_norm = np.sqrt(np.maximum(
        np.einsum('pab,pa,pb->p', gc, div, div), 0.0))
    Chat_c = vm.eulerian_that(gc, Chat_all[:Pc])
    nchat_c = np.sqrt(np.einsum('pab,pab->p', Chat_c, Chat_c))
    rel = div_norm / np.maximum(nchat_c / 10.0, 1e-300)
    out['conservation'] = dict(
        div_absmax=float(np.max(div_norm)),
        div_med=float(np.median(div_norm)),
        rel_max=float(np.max(rel)), rel_med=float(np.median(rel)),
        subset='binding[::3]', h=h,
        note='nabla_a Chat^{ab} of the assembled best-row field; '
             'the numerical size of the u-EOM open component')
    print(f'beta={beta} C4: |div Chat| max '
          f'{out["conservation"]["div_absmax"]:.3e} rel med '
          f'{out["conservation"]["rel_med"]:.3e} '
          f'({time.time()-t0:.0f}s)', flush=True)
    out['runtime_s'] = time.time() - t0
    return out


def main():
    qc, _ = L.q_crit()
    scan = json.load(open(f'{RES}/p152_scan.json'))
    out = dict(item='P15 SA-2 EOM/conservation/completeness',
               Q_crit=qc, betas=[])
    for b in scan['betas']:
        beta = b['beta']
        best = max(b['rows'],
                   key=lambda r: r['bands']['all']['frac_full'])
        out['betas'].append(run_beta(beta, qc, best['c0']))
    with open(f'{RES}/p152_eom.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print('WROTE results/p152_eom.json', flush=True)


if __name__ == '__main__':
    main()
