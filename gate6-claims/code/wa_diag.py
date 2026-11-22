"""wa_diag.py — point-level confrontation at the Phase-26 suspect point.
My 2nd-order auditor + a 4th-order variant of MY OWN direct-derivative
method (tensor-product 4th-order first-derivative coeffs applied twice;
dGamma still algebraic). No verify_metric anywhere."""
import sys
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
import shell as sh
import wa_auditor as wa

SUSPECT = np.array([[-1.2926479638607493, 9.975275121835967, -1.9711538461538465]])
GOOD = np.array([[0.528352406242398, 6.020303156466841, 8.278846153846153]])

# ---- 4th-order direct-derivative Einstein (my variant) ----
C4 = np.array([1.0, -8.0, 0.0, 8.0, -1.0]) / 12.0   # offsets -2..2, first deriv /h
OFF = np.array([-2, -1, 0, 1, 2])

def derivs4(gfunc, pts, h):
    P = pts.shape[0]
    g0 = gfunc(pts)
    # first derivs: eval at +-h,+-2h per axis
    dg = [np.zeros_like(g0) for _ in range(4)]
    cache = {}
    for a in range(3):
        acc = np.zeros_like(g0)
        for k, o in enumerate(OFF):
            if o == 0: continue
            p = pts.copy(); p[:, a] += o*h
            cache[(a, o)] = gfunc(p)
            acc += C4[k]*cache[(a, o)]
        dg[a+1] = acc/h
    d2 = [[np.zeros_like(g0) for _ in range(4)] for _ in range(4)]
    for a in range(3):
        acc = np.zeros_like(g0)
        for k, o in enumerate(OFF):
            f = g0 if o == 0 else cache[(a, o)]
            # second deriv: apply coeff twice along same axis needs f at o1+o2; use
            # standard 4th-order 5-point second-derivative stencil instead:
            pass
        # 5-point 4th-order second derivative: (-f+2 +16f+1 -30f0 +16f-1 -f-2)/(12h^2)
        fp2 = cache[(a, 2)]; fp1 = cache[(a, 1)]; fm1 = cache[(a, -1)]; fm2 = cache[(a, -2)]
        d2[a+1][a+1] = (-fp2 + 16*fp1 - 30*g0 + 16*fm1 - fm2) / (12*h*h)
    for a in range(3):
        for b in range(a+1, 3):
            acc = np.zeros_like(g0)
            for ka, oa in enumerate(OFF):
                for kb, ob in enumerate(OFF):
                    if C4[ka] == 0 or C4[kb] == 0: continue
                    p = pts.copy(); p[:, a] += oa*h; p[:, b] += ob*h
                    acc += C4[ka]*C4[kb]*gfunc(p)
            d2[a+1][b+1] = acc/(h*h); d2[b+1][a+1] = d2[a+1][b+1]
    return g0, dg, d2

def einstein4(gfunc, pts, h):
    g, dg, d2 = derivs4(gfunc, pts, h)
    ginv = np.linalg.inv(g)
    dginv = [np.zeros_like(g) for _ in range(4)]
    for e in range(1, 4):
        dginv[e] = -np.einsum('...ad,...de,...eb->...ab', ginv, dg[e], ginv)
    Gamma = np.zeros(g.shape[:1] + (4, 4, 4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                term = np.stack([dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c] for d in range(4)], axis=-1)
                Gamma[..., a, b, c] = 0.5*np.einsum('...d,...d->...', ginv[..., a, :], term)
    dGamma = [np.zeros_like(Gamma) for _ in range(4)]
    for e in range(1, 4):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    t1 = np.stack([dg[b][..., d, c] + dg[c][..., d, b] - dg[d][..., b, c] for d in range(4)], axis=-1)
                    dt = np.stack([d2[e][b][..., d, c] + d2[e][c][..., d, b] - d2[e][d][..., b, c] for d in range(4)], axis=-1)
                    dGamma[e][..., a, b, c] = 0.5*(np.einsum('...d,...d->...', dginv[e][..., a, :], t1)
                                                   + np.einsum('...d,...d->...', ginv[..., a, :], dt))
    Ricci = np.zeros(g.shape[:1] + (4, 4))
    for b_ in range(4):
        for d_ in range(4):
            v = np.zeros(g.shape[:1])
            for a in range(4):
                v += dGamma[a][..., a, b_, d_] - dGamma[d_][..., a, b_, a]
                for e in range(4):
                    v += Gamma[..., a, a, e]*Gamma[..., e, b_, d_] - Gamma[..., a, d_, e]*Gamma[..., e, b_, a]
            Ricci[..., b_, d_] = v
    R = np.einsum('...ab,...ab->...', ginv, Ricci)
    G = Ricci - 0.5*R[..., None, None]*g
    return G, g

prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked', params={'wd': 6.0, 'floor': 0.2},
                      s_rho=4.0, s_P=2.32, Nr=4001)
for beta in (0.08, 0.07):
    gf = sh.shell_point_factory(prof, beta, 'cos', 1.0, [10.0, 30.0])
    for name, pt in (('SUSPECT', SUSPECT), ('GOOD', GOOD)):
        for h in (0.3, 0.15, 0.075):
            m2 = wa.audit(gf, pt, h)
            G4, g4 = einstein4(gf, pt, h)
            That4 = wa.eulerian_that(g4, G4/wa.EIGHT_PI)
            m4 = wa.margins_from_that(That4)
            print(f"b={beta} {name} h={h}: 2nd NEC={m2['nec'][0]:+.4e} WEC={m2['wec'][0]:+.4e} "
                  f"typeI={m2['typeI'][0]} sampNEC={m2['sampled_nec'][0]:+.4e} rho={m2['rho'][0]:+.4e} || "
                  f"4th NEC={m4['nec'][0]:+.4e} typeI={m4['typeI'][0]} rho={m4['rho'][0]:+.4e}", flush=True)
