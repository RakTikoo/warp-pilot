#!/usr/bin/env python3
"""
p214_gate.py -- P21-4 CONTROL GATE (runs BEFORE any scan number;
bars in results/p214_run_record.md):
 (a) B_sign for B_b = 2 nabla.T^mu: chosen so B_b matches
     R - t with R = -tr_g G (12 binding points, beta=1.1);
 (b) Z_t identity: the lib's superpotential contraction with
     grad T vs p111_d torsion_T_W's published W (h=0.1);
 (c) GR control: fam='GR' gives H == G exactly (algebraic);
 (d) B3 CONTROL GATE: H_cov for B3 (kappa in {-5,1,20}) vs the
     textbook f(R) LHS (BBW Eq. 40) computed independently
     from (G, R, grad R, Hess R), at beta in {1.1, 1.5},
     12 binding points; PASS iff median rel. Frobenius
     difference <= 0.05 at both betas.
float64, system python3.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase21')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase11')
import verify_metric as vm    # noqa: E402
import p111_d as D            # noqa: E402
import p214_lib as L          # noqa: E402

HERE = '/home/hatch/workspace/warp-pilot/phase21/results/'


def rel_fro(A, B):
    num = np.linalg.norm((A - B).reshape(len(A), -1), axis=1)
    den = np.maximum(np.linalg.norm(B.reshape(len(B), -1), axis=1),
                     1e-300)
    return num / den


def main():
    t0 = time.time()
    out = dict(item='P21-4 control gate (pre-scan)', checks={})
    # ---- (a) B_sign determination at beta=1.1, sample points
    import p103_lib as lib
    bd = lib.bed(1.1)
    gf = L.gf_of(1.1)
    pts = bd['pts_b'][:12]
    G, _, _ = vm.einstein_at_points(gf, pts, h=0.1)
    g = gf(pts)
    ginv = np.linalg.inv(g)
    R_metric = -np.einsum('pab,pab->p', ginv, G)
    res = {}
    for sgn in (1.0, -1.0):
        T, Bb, R = L.scalar_fields(gf, pts, 0.1, B_sign=sgn)
        target = R_metric - T          # B_b should equal R - t
        err = np.abs(Bb - target) / np.maximum(np.abs(target), 1e-12)
        res[str(sgn)] = dict(med_rel_err=float(np.median(err)),
                             T_med=float(np.median(T)),
                             Bb_med=float(np.median(Bb)),
                             target_med=float(np.median(target)))
    B_sign = 1.0 if res['1.0']['med_rel_err'] <= res['-1.0']['med_rel_err'] \
        else -1.0
    out['checks']['B_sign'] = dict(results=res, chosen=B_sign,
                                   passed=bool(res[str(B_sign)]['med_rel_err'] <= 0.05))
    print(f"(a) B_sign: {res} -> chosen {B_sign}", flush=True)

    # ---- (b) Z_t identity vs p111_d W at beta=1.1 (h=0.1)
    _, T_w, W = D.torsion_T_W(gf, pts, h=0.1)
    F = L.fields_for_set(gf, pts, 0.1, B_sign=B_sign)
    rel = rel_fro(F['Zt'], W)
    out['checks']['Zt_vs_W'] = dict(rel_med=float(np.median(rel)),
                                    rel_max=float(np.max(rel)),
                                    T_rel_med=float(np.median(
                                        np.abs(F['T'] - T_w)
                                        / np.maximum(np.abs(T_w), 1e-12))),
                                    passed=bool(np.median(rel) <= 0.02))
    print(f"(b) Zt vs W: rel_med={np.median(rel):.2e}", flush=True)

    # ---- (c) GR control (algebraic, same F)
    H, _ = L.H_cov(F, 'GR', None)
    gr_err = float(np.max(np.abs(H - F['G'])))
    out['checks']['GR_control'] = dict(max_abs_H_minus_G=gr_err,
                                       passed=bool(gr_err == 0.0))
    print(f"(c) GR control: max|H-G| = {gr_err}", flush=True)

    # ---- (d) B3 gate at beta in {1.1, 1.5}
    gate_rows = {}
    allpass = True
    for beta in (1.1, 1.5):
        bd_b = lib.bed(beta)
        gf_b = L.gf_of(beta)
        pts_b = bd_b['pts_b'][:12]
        Fb = L.fields_for_set(gf_b, pts_b, 0.1, B_sign=B_sign)
        for kap in (-5.0, 1.0, 20.0):
            H, _ = L.H_cov(Fb, 'B3', kap)
            R = Fb['R']
            u = kap * L.LW**2 * R
            E = np.exp(u)
            F1 = E * (1 + u)
            F2 = kap * L.LW**2 * E * (2 + u)
            F3 = (kap * L.LW**2) ** 2 * E * (3 + u)
            Fval = R * E
            Ric = Fb['G'] + 0.5 * R[:, None, None] * Fb['g']
            # nabla nabla F1 = F2 * Hess R + F3 * gradR x gradR
            HessF = F2[:, None, None] * Fb['HessR'] \
                + F3[:, None, None] * np.einsum(
                'pa,pb->pab', Fb['gradR'], Fb['gradR'])
            BoxF = np.einsum('pab,pab->p', Fb['ginv'], HessF)
            LHS = F1[:, None, None] * Ric \
                - 0.5 * Fval[:, None, None] * Fb['g'] \
                + Fb['g'] * BoxF[:, None, None] - HessF
            rel = rel_fro(H, LHS)
            gate_rows[f'{beta}|{kap}'] = dict(
                rel_med=float(np.median(rel)), rel_max=float(np.max(rel)))
            ok = float(np.median(rel)) <= 0.05
            allpass = allpass and ok
            print(f'(d) B3 beta={beta} kappa={kap}: rel_med='
                  f'{np.median(rel):.3e} pass={ok}', flush=True)
    out['checks']['B3_gate'] = dict(rows=gate_rows, passed=bool(allpass),
                                    bar_med_rel=0.05)
    out['B_sign'] = B_sign
    out['gate_passed'] = bool(out['checks']['B_sign']['passed']
                              and out['checks']['Zt_vs_W']['passed']
                              and out['checks']['GR_control']['passed']
                              and allpass)
    out['runtime_s'] = time.time() - t0
    with open(HERE + 'p214_gate.json', 'w') as fh:
        json.dump(out, fh, indent=2)
    print(f"gate_passed = {out['gate_passed']}  ({out['runtime_s']:.0f}s)",
          flush=True)


if __name__ == '__main__':
    main()
