#!/usr/bin/env python
"""GATE-22 attack line (a): INDEPENDENT re-derivation of the wound
director's (grad n)^2 in the t-dependent throat geometry, from
scratch (no Phase 202/205 driver code imported or copied).

Geometry (fixed t): dl^2 = drho^2 + R(rho,th)^2 (dth^2 + sin^2 th dph^2),
with R(rho,th) = A(th) + rho^2 B(th)  -- so R_,rho(0,th) = 0 identically
(the throat condition of the pose), A(th) = R(0,th) generic.
Director: n = cos(m ph) phi-hat + sin(m ph) theta-hat.

Computes, symbolically:
  - Christoffels of the 3-metric, covariant derivatives of n,
    orthonormal-frame components D[a][b] = (nabla_{e_a} n)^{e_b};
  - (grad n)^2 = sum_{a,b} D[a][b]^2  (phi-independent?);
  - the Ericksen gradient tensor G_ab = sum_c D[a][c] D[b][c],
    phi-averaged: diagonal? <G_rhorho> = <G_thth> = 0?
    <G_phph> = (grad n)^2? off-diagonals zero?
  - compares (grad n)^2 against the P-DIR-T2 closed form
        [(m - cos th) - (A'/A) sin th]^2 / (sin^2 th * A^2)
    and against the refused P-DIR-T1 form (m - cos th)^2/(sin^2 th A^2).
Runs for m = 1 and m = 2. float64/symbolic exact. GATE-22 internal.
"""
import sympy as sp

rho, th, ph = sp.symbols('rho th ph', real=True)
A = sp.Function('A')(th)
Bf = sp.Function('B')(th)
R = A + rho**2 * Bf
coords = [rho, th, ph]

results = {}
for m in (1, 2):
    g = sp.diag(1, R**2, R**2 * sp.sin(th)**2)
    ginv = g.inv()
    # Christoffel Gamma^k_ij
    dg = [[[sp.diff(g[i, j], coords[k]) for k in range(3)]
           for j in range(3)] for i in range(3)]
    Gam = [[[sp.Integer(0)] * 3 for _ in range(3)] for _ in range(3)]
    for k in range(3):
        for i in range(3):
            for j in range(3):
                Gam[k][i][j] = sp.simplify(sum(
                    ginv[k, l] * (dg[l][j][i] + dg[l][i][j] - dg[i][j][l])
                    for l in range(3)) / 2)
    # director, contravariant coordinate components
    n = [sp.Integer(0), sp.sin(m * ph) / R, sp.cos(m * ph) / (R * sp.sin(th))]
    dn = [[sp.diff(n[k], coords[i]) for k in range(3)] for i in range(3)]
    cov = [[sp.simplify(dn[i][k] + sum(Gam[k][i][j] * n[j]
                                       for j in range(3)))
            for k in range(3)] for i in range(3)]
    # orthonormal frame components: D[a][b] = sqrt(g_bb/g_aa) * cov[a][b]
    sq = [sp.sqrt(g[i, i]) for i in range(3)]
    D = [[sp.simplify(sq[b] / sq[a] * cov[a][b]) for b in range(3)]
         for a in range(3)]
    D0 = [[sp.simplify(x.subs(rho, 0)) for x in row] for row in D]
    grad2 = sp.simplify(sum(D0[a][b] ** 2 for a in range(3)
                            for b in range(3)))
    # phi-dependence of (grad n)^2: d/dph must vanish
    dphi = sp.simplify(sp.diff(grad2, ph))
    # Ericksen G_ab and its phi average
    G = [[sp.simplify(sum(D0[a][c] * D0[b][c] for c in range(3)))
          for b in range(3)] for a in range(3)]
    Gavg = [[sp.simplify(sp.integrate(G[a][b], (ph, 0, 2 * sp.pi))
                         / (2 * sp.pi)) for b in range(3)]
            for a in range(3)]
    Ap = sp.diff(A, th)
    T2 = ((m - sp.cos(th)) - (Ap / A) * sp.sin(th)) ** 2 \
        / (sp.sin(th) ** 2 * A ** 2)
    T1 = (m - sp.cos(th)) ** 2 / (sp.sin(th) ** 2 * A ** 2)
    diff_T2 = sp.simplify(sp.together(grad2 - T2))
    diff_T1 = sp.simplify(sp.together(grad2 - T1))
    nav_rho_zero = all(sp.simplify(x) == 0 for x in D0[0])
    nav_th_zero = all(sp.simplify(x) == 0 for x in D0[1])
    results[m] = {
        'grad2': str(grad2),
        'dphi_grad2': str(dphi),
        'diff_vs_T2': str(diff_T2),
        'diff_vs_T1_zero': bool(diff_T1 == 0),
        'nabla_rho_n_zero_at_throat': bool(nav_rho_zero),
        'nabla_th_n_zero_at_throat': bool(nav_th_zero),
        'Gavg': [[str(Gavg[a][b]) for b in range(3)] for a in range(3)],
        'Gavg_diag': [str(Gavg[i][i]) for i in range(3)],
        'Gavg_offdiag_all_zero': bool(all(
            sp.simplify(Gavg[a][b]) == 0
            for a in range(3) for b in range(3) if a != b)),
        'Gavg_phph_equals_grad2': bool(sp.simplify(Gavg[2][2] - grad2) == 0),
        'Gavg_rhorho_zero': bool(sp.simplify(Gavg[0][0]) == 0),
        'Gavg_thth_zero': bool(sp.simplify(Gavg[1][1]) == 0),
    }
    print('m =', m)
    print('  (grad n)^2            =', grad2)
    print('  d/dph (grad n)^2      =', dphi)
    print('  (grad n)^2 - T2 form  =', diff_T2)
    print('  equals T1 form?       ', bool(diff_T1 == 0))
    print('  nabla_rho n = 0       ', nav_rho_zero)
    print('  nabla_th  n = 0       ', nav_th_zero)
    print('  <G> diag              =', results[m]['Gavg_diag'])
    print('  <G> offdiag all zero  ', results[m]['Gavg_offdiag_all_zero'])
    print('  <G_phph> = (grad n)^2 ', results[m]['Gavg_phph_equals_grad2'])

import json
with open('/home/hatch/workspace/warp-pilot/gate22/work/'
          'g22_sym_results.json', 'w') as f:
    json.dump(results, f, indent=1)
print('written g22_sym_results.json')
