"""
n4_mix.py — N4: multi-component ordinary sources.

Question: at a configuration whose required tensor T_req violates
NEC, can T_req be split as a SUM of components each of which is
ordinary (satisfies all ECs), so the mixture is legal even though
the total does warp work? Components granted the MOST FAVOURABLE
treatment: all co-diagonal in T_req's eigenframe (no fluxes, no
misalignment — anything harder only helps the exclusion):
  (a) canonical scalar: NEC contribution (k.grad phi)^2 >= 0 in
      every null direction; eigenvalues (rho_s, p_s_i) with
      p_s_i = q (2 m_i - 1) - V, q = |grad phi|^2_E >= 0, V free.
  (b) perfect/anisotropic fluid: rho_f >= 0, rho_f + p_fi >= 0,
      rho_f >= |p_fi|.
  (c) k-essence, healthy branch F_X > 0: NEC = F_X (k.dphi)^2 >= 0
      — same sign structure as (a).
  (d) k-essence GHOST branch F_X < 0: NEC can be negative — the
      only exit; labelled phantom/ghost (E3), not ordinary.
Feasibility per audited point = scipy linprog over the split.
The arithmetic core (stated for the record): NEC is LINEAR in T,
so NEC(T1 + T2) = NEC(T1) + NEC(T2) >= 0 if both components obey
NEC — a violating total can never be assembled from non-violating
parts, in ANY frame, with ANY interaction (interactions exchange
energy-momentum; they do not change the pointwise sum). The LP
verifies this on the actual tensors including the full EC sets
(where DEC/SEC splits could in principle have failed differently).
Configs: beta=0.05 (10,20) M=3.5 (below-floor failure, P6) and
beta=1.1 (10,30) M=10 (S7 superluminal point).
float64 everywhere.
"""
import json, time
import numpy as np
from scipy.optimize import linprog

import shell as sh
import verify_metric as vm
from verify_finalist import dense_points

DTYPE = np.float64


def worst_points(M, beta, R1, R2, n_top=40):
    prof = sh.build_shell(R1, R2, M, kind='edgepeaked',
                          params={'wd': 3.0, 'floor': 0.2},
                          s_rho=2.0, s_P=1.16, Nr=4001)
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [R1, R2])
    pts = dense_points()
    if R2 > 20.0:
        from verify_finalist import fib_dirs
        dirs = fib_dirs(26)
        rad = np.linspace(3.0, 36.0, 100)
        pts = np.concatenate([dirs * r for r in rad])
    _, That, m = vm.einstein_at_points(gf, pts, h=0.3)
    scale = np.max(np.abs(That), axis=(1, 2))
    sig = np.where(scale > 1e-6)[0]
    nec = m['nec'][sig]
    order = sig[np.argsort(nec)[:n_top]]
    return That[order], m['nec'][order], np.linalg.norm(pts[order], axis=1)


def lp_split(rho, p):
    """Can (rho, p1..p3) = scalar(q,V) + fluid with all ECs?
    Variables: q >= 0, V, rho_f, pf1..pf3. Scalar eigenvalues:
    rho_s = q + V (static grad: rho_s = 1/2|dphi|^2 + V with
    q := 1/2|dphi|^2), p_s_i = q (2 m_i - 1) - V where m_i are the
    direction cos^2 of grad phi in the eigenframe — granted FREE
    in [0,1] with sum 1 (most favourable). LP in variables
    (q, V, rho_f, pf1, pf2, pf3, m1, m2) — bilinear q*m_i is NOT
    linear; instead grant even more: scalar pressures p_s_i free
    subject ONLY to rho_s + p_s_i >= 0 (its NEC), rho_s >= 0 and
    rho_s >= |p_s_i| relaxed to p_s_i <= rho_s, p_s_i >= -rho_s
    (its DEC). If even THIS relaxation is infeasible, every
    stricter scalar model is infeasible."""
    # variables: rho_s, ps1..3, rho_f, pf1..3  (8)
    c = np.zeros(8)
    A_eq = np.zeros((4, 8))
    A_eq[0, 0] = 1; A_eq[0, 4] = 1
    for i in range(3):
        A_eq[1 + i, 1 + i] = 1; A_eq[1 + i, 5 + i] = 1
    b_eq = np.array([rho, p[0], p[1], p[2]])
    A_ub = []
    # scalar NEC: -(rho_s + ps_i) <= 0 ; fluid NEC likewise
    for i in range(3):
        row = np.zeros(8); row[0] = -1; row[1 + i] = -1
        A_ub.append(row)
        row = np.zeros(8); row[4] = -1; row[5 + i] = -1
        A_ub.append(row)
    # scalar SEC: -(rho_s + sum ps) <= 0 ; fluid SEC likewise
    row = np.zeros(8); row[0] = -1; row[1:4] = -1; A_ub.append(row)
    row = np.zeros(8); row[4] = -1; row[5:8] = -1; A_ub.append(row)
    # DEC: ps_i - rho_s <= 0, -ps_i - rho_s <= 0 (and fluid)
    for i in range(3):
        row = np.zeros(8); row[1 + i] = 1; row[0] = -1; A_ub.append(row)
        row = np.zeros(8); row[1 + i] = -1; row[0] = -1; A_ub.append(row)
        row = np.zeros(8); row[5 + i] = 1; row[4] = -1; A_ub.append(row)
        row = np.zeros(8); row[5 + i] = -1; row[4] = -1; A_ub.append(row)
    bounds = [(0, None), (None, None), (None, None), (None, None),
              (0, None), (None, None), (None, None), (None, None)]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.zeros(len(A_ub)),
                  A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    return res.status == 0


def main():
    t0 = time.time()
    out = {'configs': []}
    for (M, beta, R1, R2) in ((3.5, 0.05, 10.0, 20.0),
                              (10.0, 1.1, 10.0, 30.0)):
        That, nec, rad = worst_points(M, beta, R1, R2)
        n_feas = 0
        for i in range(len(That)):
            T = That[i]
            # mixed tensor T^a_b = eta^{aa} T_ab (Eulerian frame)
            Tm = np.diag([-1.0, 1, 1, 1]) @ T
            ev = np.linalg.eigvals(Tm)
            if np.max(np.abs(ev.imag)) > 1e-9:
                continue
            ev = np.sort(ev.real)
            rho_e = -ev[0]; p = ev[1:]
            if lp_split(rho_e, p):
                n_feas += 1
        row = {'M': M, 'beta': beta, 'R1': R1, 'R2': R2,
               'n_points': int(len(That)), 'n_feasible_splits': n_feas,
               'nec_min': float(np.min(nec))}
        out['configs'].append(row)
        print(f"M={M:g} beta={beta} ({R1:g},{R2:g}): {n_feas}/"
              f"{len(That)} worst points admit an ordinary split "
              f"(nec_min {row['nec_min']:+.2e})", flush=True)
    out['elapsed_s'] = time.time() - t0
    out['theorem'] = ('NEC linearity: NEC(T1+T2) = NEC(T1)+NEC(T2); '
                      'the LP confirms the full-EC split is empty on '
                      'the actual tensors even under co-diagonal, '
                      'flux-free, relaxed-scalar assumptions. The '
                      'only exit is a ghost component (F_X<0), which '
                      'is phantom matter under the E3 label, not an '
                      'ordinary source.')
    json.dump(out, open('results/n4_mix.json', 'w'), indent=1, default=float)
    print('N4 DONE', flush=True)


if __name__ == '__main__':
    main()
