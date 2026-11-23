"""W-C fresh dynamic l=0 Galerkin quotient-spectrum implementation.

Method (shared definition from p382_memo.md / p711_memo.md, code fresh):
metric in log components ds^2 = -e^{2a}dt^2 + e^{2b}dr^2 + e^{2c}r^2 dOmega^2;
background a = Phi(r), b = -0.5 ln(1 - r^{p-1}), c = 0 (r0 = 1).
Quadratic Weyl action density Q = sqrt(-g) C^2 from wc_symq.py's fresh
symbolic expression. For each trial component X in {a,b,c} and pair XY,
F_XY(w) = (1/2) d^2/deps^2 int Q dr dt-avg at eps=0 for the perturbation
eps*P(r) cos(w t) added to the named log components (5-point FD in eps).
M(w^2) is built from F_X and F_XY; fits: averaged branch through
w = 1,2,3 and snapshot branch through w = 0,1,2 (both conventions
carried, per the factor-2 snapshot anatomy). Quotient scan: eigenvalues
of M on w^2 in [-5,0] (2001 points); the gauge eigenvalue is the one
whose eigenvector aligns with (1,1,1)/sqrt(3); the other two are the
physical eigenvalues. det M and bare determinant signs are NEVER read.
"""
import json, os, sys, time
import numpy as np, sympy as sp

GATE = os.path.expanduser('~/workspace/warp-pilot/gate9')
D = json.load(open(os.path.join(GATE, 'wc_symq_expr.json')))
_names = D['names']; _syms = sp.symbols(' '.join(_names))
_Q = sp.lambdify(_syms, sp.sympify(D['Q']), 'numpy')

def Q_fast(st):
    args = [st['r']]
    for x in 'abc':
        args += [st[x], st['d'+x][:, 0], st['d'+x][:, 1],
                 st['d2'+x][:, 0], st['d2'+x][:, 1], st['d2'+x][:, 2]]
    return np.asarray(_Q(*args), dtype=float)

def bg_state(r, p, phi_kind, A=0.277734):
    r = np.asarray(r, float); N = r.shape[0]; z = np.zeros(N)
    q = p - 1.0; rq = r**q; f = 1.0 - rq
    fp = -q*r**(q-1); fpp = -q*(q-1)*r**(q-2)
    blog = -0.5*np.log(f); blogp = -0.5*fp/f; blogpp = -0.5*(fpp/f - (fp/f)**2)
    if phi_kind == 'zero':
        a = z.copy(); ap = z.copy(); app = z.copy()
    else:
        L = np.log(r); a = A*L/(1+L); ap = A/(r*(1+L)**2); app = -A*(L+3)/(r**2*(1+L)**3)
    da = np.zeros((N, 2)); da[:, 1] = ap
    db = np.zeros((N, 2)); db[:, 1] = blogp
    d2a = np.zeros((N, 3)); d2a[:, 2] = app
    d2b = np.zeros((N, 3)); d2b[:, 2] = blogpp
    return {'r': r, 'a': a, 'b': blog, 'c': z.copy(), 'da': da, 'db': db,
            'dc': np.zeros((N, 2)), 'd2a': d2a, 'd2b': d2b, 'd2c': np.zeros((N, 3))}

def profile(expr):
    rs = sp.symbols('r'); e = sp.sympify(expr)
    return tuple(sp.lambdify(rs, sp.diff(e, rs, k), 'numpy') for k in range(3))

def make_state(rgrid, tgrid, w, eps, dyn_modes, bgkw):
    Rg, Tg = np.meshgrid(rgrid, tgrid, indexing='ij')
    Rf, Tf = Rg.ravel(), Tg.ravel()
    st = bg_state(Rf, **bgkw); cw, sw = np.cos(w*Tf), np.sin(w*Tf)
    names = ['a', 'b', 'c']
    for comp, (pf, pf1, pf2) in dyn_modes:
        nm = names[comp]; P, P1, P2 = pf(Rf), pf1(Rf), pf2(Rf)
        st[nm] = st[nm] + eps*P*cw
        st['d'+nm] = st['d'+nm] + np.stack([-eps*P*w*sw, eps*P1*cw], axis=1)
        st['d2'+nm] = st['d2'+nm] + np.stack([-eps*P*w*w*cw, -eps*P1*w*sw, eps*P2*cw], axis=1)
    return st, Rg.shape

def F_of_w(dyn_modes, wv, R_out, bgkw, Nr=1000, h=1e-3, nt=8):
    s = np.linspace(0, 1, Nr); rgrid = 1.0005 + (R_out-1.0005)*s**3
    if wv == 0.0:
        tgrid = np.array([0.0]); tw = np.array([1.0])
    else:
        tgrid = np.linspace(0, 2*np.pi/wv, nt+1)[:-1]; tw = np.full(nt, 1/nt)
    Qs = {}
    for e in (-2*h, -h, 0.0, h, 2*h):
        st, shape = make_state(rgrid, tgrid, wv, e, dyn_modes, bgkw)
        Qs[e] = Q_fast(st).reshape(shape)
    q2 = (-Qs[2*h] + 16*Qs[h] - 30*Qs[0.0] + 16*Qs[-h] - Qs[-2*h])/(12*h*h)/2
    tavg = (q2*tw[None, :]).sum(axis=1)
    return float(np.trapezoid(tavg, rgrid))

def fit(Fs, ws):
    M = np.array([[w**4, w**2, 1.0] for w in ws]); rhs = np.array([Fs[w] for w in ws])
    A4, A2, A0 = np.linalg.solve(M, rhs)
    return {'A4': float(A4), 'A2': float(A2), 'A0': float(A0)}

KEYS = ['A', 'B', 'C', 'AB', 'AC', 'BC']
def combos(P):
    return {'A': [(0, P)], 'B': [(1, P)], 'C': [(2, P)],
            'AB': [(0, P), (1, P)], 'AC': [(0, P), (2, P)], 'BC': [(1, P), (2, P)]}

def analyse_block(P, R_out, bgkw, Nr=1000):
    cb = combos(P); blk = {}
    for k in KEYS:
        dyn = cb[k]; Fs = {0.0: F_of_w(dyn, 0.0, R_out, bgkw, Nr=Nr)}
        for w in (0.5, 1.0, 1.5, 2.0, 3.0):
            if k in ('AB', 'AC', 'BC') and w in (0.5, 1.5): continue
            Fs[w] = F_of_w(dyn, w, R_out, bgkw, Nr=Nr)
        avg = fit(Fs, (1.0, 2.0, 3.0)); snap = fit(Fs, (0.0, 1.0, 2.0))
        chk = {}
        for w in (0.5, 1.5):
            if w in Fs:
                pred = avg['A4']*w**4 + avg['A2']*w**2 + avg['A0']
                chk[str(w)] = float(abs(pred-Fs[w])/max(1e-30, abs(Fs[w])))
        blk[k] = {'F_at_w': {str(w): v for w, v in Fs.items()},
                  'averaged_fit': avg, 'snapshot_fit': snap,
                  'heldout_rel_resid': chk,
                  'snapshot_over_avgF0_ratio': float(Fs[0.0]/avg['A0']) if avg['A0'] != 0 else None}
    return blk

def quotient_scan(blk):
    out = {}
    for fk in ('averaged_fit', 'snapshot_fit'):
        def Fd(d, x):
            f = d[fk]; return f['A4']*x**2 + f['A2']*x + f['A0']
        xs = np.linspace(-5.0, 0.0, 2001)
        lam = []; crossings = []; prev = None
        null_max = 0.0; detmax = 0.0; align_min = 1.0; nneg = 0
        u = np.ones(3)/np.sqrt(3)
        for x in xs:
            FA, FB, FC = Fd(blk['A'], x), Fd(blk['B'], x), Fd(blk['C'], x)
            FAB, FAC, FBC = Fd(blk['AB'], x), Fd(blk['AC'], x), Fd(blk['BC'], x)
            M = np.array([[FA, (FAB-FA-FB)/2, (FAC-FA-FC)/2],
                          [(FAB-FA-FB)/2, FB, (FBC-FB-FC)/2],
                          [(FAC-FA-FC)/2, (FBC-FB-FC)/2, FC]])
            null_max = max(null_max, float(np.max(np.abs(M @ np.ones(3)))))
            detmax = max(detmax, abs(float(np.linalg.det(M))))
            w, V = np.linalg.eigh(M)
            kk = int(np.argmax(np.abs(V.T @ u)))
            align_min = min(align_min, float(abs(V[:, kk] @ u)))
            phys = sorted(float(w[i]) for i in range(3) if i != kk)
            lam.append(phys[0]); nneg += int(phys[0] < 0)
            if prev is not None and prev[1]*phys[0] < 0: crossings.append([prev[0], float(x)])
            prev = (float(x), phys[0])
        lam = np.array(lam)
        out[fk] = {'null_rowsum_resid_max_over_scan': null_max,
                   'det_max_abs_over_scan': detmax,
                   'null_eigvec_alignment_min': align_min,
                   'smallest_physical_eigenvalue_min': float(np.min(lam)),
                   'smallest_physical_eigenvalue_at_x0': float(lam[-1]),
                   'smallest_physical_eigenvalue_at_x-5': float(lam[0]),
                   'physical_eigenvalue_zero_crossings_in_[-5,0]': crossings,
                   'n_scan_points_lambda_phys_negative': int(nneg)}
    return out

PROFILES = {'P1': '(r-1)**2/r**4', 'P2': '(r-1)**2/r**5'}

def run(tag, bgkw, Rs=(10, 20, 30)):
    res = {}
    for pn, pexpr in PROFILES.items():
        P = profile(pexpr)
        for R in Rs:
            t0 = time.time()
            blk = analyse_block(P, R, bgkw)
            res[f'{pn}_R{R}'] = quotient_scan(blk)
            res[f'{pn}_R{R}']['fits'] = {k: {'averaged_fit': blk[k]['averaged_fit'],
                                            'snapshot_fit': blk[k]['snapshot_fit'],
                                            'heldout_rel_resid': blk[k]['heldout_rel_resid'],
                                            'snapshot_over_avgF0_ratio': blk[k]['snapshot_over_avgF0_ratio']}
                                        for k in KEYS}
            print(tag, pn, R, 'min phys avg', res[f'{pn}_R{R}']['averaged_fit']['smallest_physical_eigenvalue_min'],
                  'snap', res[f'{pn}_R{R}']['snapshot_fit']['smallest_physical_eigenvalue_min'],
                  f'{time.time()-t0:.1f}s', flush=True)
            json.dump(res, open(os.path.join(GATE, 'results', f'wc_dyn_{tag}.json'), 'w'), indent=1)
    return res

if __name__ == '__main__':
    which = sys.argv[1]
    if which == 'tb':
        run('tb', {'p': 0.5, 'phi_kind': 'zero'})
    elif which == 'jm':
        run('jm', {'p': 0.1, 'phi_kind': 'Phi2'})
    print('DONE', which, flush=True)
