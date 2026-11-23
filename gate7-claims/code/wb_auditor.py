"""wb_auditor.py — W-B Gate-7 G7-2 numeric auditor on the SYMBOLIC tensor.

Loads the lambdified Einstein tensor from wb_symbolic.py (wb_tensor.pkl),
feeds it ANALYTIC derivatives only:
  * a(r), b(r): CubicSpline of shell.py's build_shell profiles (the shared
    definition), differentiated by the spline itself (nu=1, 2).
  * S(r): cosine in closed form, or the K=5 clamped cubic spline rebuilt
    from the stored z_final via the phase's stick-break convention
    (re-implemented here; knot values verified against spline_diag).
Transforms the spherical-coordinate tensor to the Cartesian frame with the
exact Jacobian, builds the Eulerian orthonormal-frame tensor That with
fresh code, and computes Hawking-Ellis margins / Type-I / sampled-null NEC
(162 Fibonacci directions) with fresh code. No FD stencil anywhere.

Python: system python3 (numpy 2.2.6 / scipy 1.14.1), float64.
Usage: python3 wb_auditor.py   -> writes results/wb_g72_numbers.json
"""
import json, pickle, sys, time
import numpy as np
from scipy.interpolate import CubicSpline

sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
import shell as sh

G7 = '/home/hatch/workspace/warp-pilot/gate7'
P50 = '/home/hatch/workspace/warp-pilot/phase50/results'
DTYPE = np.float64
sys.path.insert(0, G7)
import wb_symbolic as _ws  # W-B's own derivation, rebuilt on import (~35 s)
Gfun, gfun = _ws.Gfun, _ws.gfun

# ------------------------------------------------------------------ helpers
def fib_dirs(n):
    i = np.arange(n, dtype=DTYPE)
    phi = np.arccos(1 - 2 * (i + 0.5) / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], axis=1)

def fine_pts(R1, R2, ndir=26):
    rad = np.concatenate([np.arange(0.3 * R1, R1 - 0.74, 1.0),
                          np.arange(R1 - 0.75, R2 + 0.01, 0.5),
                          np.arange(R2 + 1.0, 1.35 * R2 + 0.01, 2.0)])
    D = fib_dirs(ndir)
    pts = np.concatenate([D * r for r in rad]).astype(DTYPE)
    return pts, np.linalg.norm(pts, axis=1)

def robust_pts(R1, R2):
    rad = np.concatenate([np.arange(9.75, 11.50 + 1e-9, 0.125),
                          np.arange(32.0, 40.0 + 1e-9, 0.5)])
    D = fib_dirs(52)
    pts = np.concatenate([D * r for r in rad]).astype(DTYPE)
    return pts, np.linalg.norm(pts, axis=1)

# ------------------------------------------------- S(r) representations
def stick_break_values(z):
    """Phase-50 convention, re-implemented: z (K+1) -> interior knot values."""
    z = np.asarray(z, dtype=DTYPE); K = len(z) - 1
    w = np.zeros(K + 1, dtype=DTYPE); rem = 1.0
    for j in range(K):
        w[j] = rem * z[j]; rem -= w[j]
    w[K] = rem
    return 1.0 - np.cumsum(w)[:K]

class SplineS:
    def __init__(self, R1, R2, K, z):
        v = stick_break_values(z)
        self.knot_r = np.linspace(R1, R2, K + 2)
        self.knot_v = np.concatenate([[1.0], v, [0.0]])
        self.spl = CubicSpline(self.knot_r, self.knot_v,
                               bc_type=((1, 0.0), (1, 0.0)))
        self.R1, self.R2 = R1, R2
    def eval(self, r):
        S = np.where(r <= self.R1, 1.0, 0.0)
        S1 = np.zeros_like(r); S2 = np.zeros_like(r)
        mid = (r > self.R1) & (r < self.R2)
        S[mid] = self.spl(r[mid])
        S1[mid] = self.spl(r[mid], 1)
        S2[mid] = self.spl(r[mid], 2)
        at1 = (r == self.R1); at2 = (r == self.R2)
        S[at1] = 1.0; S[at2] = 0.0
        return S, S1, S2

class CosS:
    def __init__(self, R1, R2):
        self.R1, self.R2 = R1, R2
    def eval(self, r):
        W = self.R2 - self.R1
        u = np.clip((r - self.R1) / W, 0.0, 1.0)
        S = np.where((r <= self.R1), 1.0, np.where(r >= self.R2, 0.0,
                     0.5 * (1 + np.cos(np.pi * u))))
        mid = (r > self.R1) & (r < self.R2)
        S1 = np.zeros_like(r); S2 = np.zeros_like(r)
        S1[mid] = -0.5 * np.sin(np.pi * u[mid]) * np.pi / W
        S2[mid] = -0.5 * np.cos(np.pi * u[mid]) * (np.pi / W) ** 2
        return S, S1, S2

# ------------------------------------------------- tensor evaluation
def tensors_at(pts, prof, Sobj, beta):
    """Return G_cart (P,4,4), g_cart (P,4,4) from the symbolic tensor."""
    a_s = CubicSpline(prof['r'], prof['a']); b_s = CubicSpline(prof['r'], prof['b'])
    rmax = prof['r'][-1]
    r = np.linalg.norm(pts, axis=1)
    rc = np.clip(r, 1e-9, rmax)
    th = np.arccos(np.clip(pts[:, 2] / np.maximum(r, 1e-300), -1, 1))
    ph = np.arctan2(pts[:, 1], pts[:, 0])
    a = a_s(rc); a1 = a_s(rc, 1); a2 = a_s(rc, 2)
    b = b_s(rc); b1 = b_s(rc, 1); b2 = b_s(rc, 2)
    S, S1, S2 = Sobj.eval(rc)
    def _mat_out(raw, P):
        arr = np.empty((P, 4, 4), dtype=DTYPE)
        for i in range(4):
            for j in range(4):
                arr[:, i, j] = np.broadcast_to(np.asarray(raw[i][j], dtype=DTYPE), (P,))
        return arr
    Gs = _mat_out(Gfun(rc, th, ph, a, a1, a2, b, b1, b2, S, S1, S2, beta), len(pts))
    # metric in spherical coords, built directly from its definition
    gs = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    st_, ct_ = np.sin(th), np.cos(th); sp_, cp_ = np.sin(ph), np.cos(ph)
    gs[:, 0, 0] = -np.exp(2 * a)
    gs[:, 0, 1] = gs[:, 1, 0] = -beta * S * st_ * cp_
    gs[:, 0, 2] = gs[:, 2, 0] = -beta * S * rc * ct_ * cp_
    gs[:, 0, 3] = gs[:, 3, 0] = beta * S * rc * st_ * sp_
    gs[:, 1, 1] = np.exp(2 * b); gs[:, 2, 2] = rc ** 2; gs[:, 3, 3] = rc ** 2 * st_ ** 2
    # Jacobian d(x_sph)/d(x_cart), rows: t, r, th, ph ; cols: t, x, y, z
    st, ct = np.sin(th), np.cos(th); sp, cp = np.sin(ph), np.cos(ph)
    rsafe = np.maximum(r, 1e-300)
    J = np.zeros((len(pts), 4, 4), dtype=DTYPE)
    J[:, 0, 0] = 1.0
    J[:, 1, 1] = st * cp; J[:, 1, 2] = st * sp; J[:, 1, 3] = ct
    J[:, 2, 1] = ct * cp / rsafe; J[:, 2, 2] = ct * sp / rsafe; J[:, 2, 3] = -st / rsafe
    J[:, 3, 1] = -sp / (rsafe * np.maximum(st, 1e-300)); J[:, 3, 2] = cp / (rsafe * np.maximum(st, 1e-300))
    Gc = np.einsum('pia,pab,pjb->pij', J, Gs, J)
    gc = np.einsum('pia,pab,pjb->pij', J, gs, J)
    return 0.5 * (Gc + np.swapaxes(Gc, -1, -2)), 0.5 * (gc + np.swapaxes(gc, -1, -2))

def eulerian_that(g, Tcov):
    gamma = g[:, 1:, 1:]; bcov = g[:, 0, 1:]
    ginv = np.linalg.inv(gamma)
    bup = np.einsum('pij,pj->pi', ginv, bcov)
    alpha = np.sqrt(np.maximum(-g[:, 0, 0] + np.einsum('pi,pi->p', bcov, bup), 1e-300))
    lam, V = np.linalg.eigh(gamma)
    E = np.zeros_like(g)
    E[:, 0, 0] = 1.0 / alpha
    E[:, 1:, 0] = -bup / alpha[:, None]
    for i in range(3):
        E[:, 1:, i + 1] = V[:, :, i] / np.sqrt(lam[:, i])[:, None]
    That = np.einsum('pma,pnb,pmn->pab', E, E, Tcov)
    return 0.5 * (That + np.swapaxes(That, -1, -2))

def margins(That):
    flat = That
    Np = flat.shape[0]
    M = flat.copy(); M[:, 0, :] *= -1.0
    evals, evecs = np.linalg.eig(M)
    scale = np.maximum(np.max(np.abs(evals.real), axis=1), 1e-300)
    real_ok = np.max(np.abs(evals.imag), axis=1) < 1e-8 * scale
    ev2 = np.abs(evecs) ** 2
    norms = -ev2[:, 0, :] + ev2[:, 1, :] + ev2[:, 2, :] + ev2[:, 3, :]
    cand = norms < -1e-6
    typeI = real_ok & (cand.sum(axis=1) == 1)
    k = np.argmax(cand, axis=1); ar = np.arange(Np)
    rho = np.where(typeI, -evals[ar, k].real, np.nan)
    mask = np.ones((Np, 4), bool); mask[ar, k] = False
    ps = np.where(typeI[:, None], evals.real[mask].reshape(Np, 3), np.nan)
    with np.errstate(invalid='ignore'):
        nec = np.where(typeI, np.min(rho[:, None] + ps, axis=1), np.nan)
        wec = np.where(typeI, np.minimum(rho, np.min(rho[:, None] + ps, axis=1)), np.nan)
        sec = np.where(typeI, np.minimum(np.min(rho[:, None] + ps, axis=1),
                                         rho + np.sum(ps, axis=1)), np.nan)
        dec = np.where(typeI, np.minimum(rho, rho - np.max(np.abs(ps), axis=1)), np.nan)
    return {'rho': rho, 'p': ps, 'typeI': typeI, 'nec': nec, 'wec': wec,
            'sec': sec, 'dec': dec}

def sampled_nec(That, n_dir=162):
    D = fib_dirs(n_dir)
    T00 = That[:, 0, 0]; T0i = That[:, 0, 1:]; Tij = That[:, 1:, 1:]
    quad = np.einsum('pjk,nj,nk->pn', Tij, D, D)
    vals = T00[:, None] + 2.0 * (T0i @ D.T) + quad
    return vals.min(axis=1)

def audit(pts, radp, prof, Sobj, beta, R1=10.0, R2=30.0):
    G, g = tensors_at(pts, prof, Sobj, beta)
    That = eulerian_that(g, G / (8 * np.pi))
    m = margins(That)
    m['That'] = That; m['sampled'] = sampled_nec(That)
    scale = np.max(np.abs(That), axis=(1, 2))
    rho_peak = float(np.max(That[:, 0, 0]))
    thr = max(1e-9 * (10.0 / R1) ** 2, 1e-3 * abs(rho_peak))
    out = {'rho_peak': rho_peak, 'thr': thr, 'n_pts': int(len(pts))}
    for reg, m0 in (('all_sig', np.ones(len(pts), bool)),
                    ('core', (radp >= R1) & (radp <= R2)),
                    ('cavity', radp < R1), ('exterior', radp > R2)):
        mask = m0 & (scale > thr)
        d = {}
        for kk in ('nec', 'wec', 'sec', 'dec'):
            v = m[kk][mask]; i = int(np.nanargmin(v)); idx = int(np.where(mask)[0][i])
            d[kk] = float(v[i]); d[kk + '_r'] = float(radp[idx])
            d[kk + '_pt'] = [float(x) for x in pts[idx]]
        d['worst'] = min(d[kk] for kk in ('nec', 'wec', 'sec', 'dec'))
        d['worst_kind'] = min(('nec', 'wec', 'sec', 'dec'), key=lambda kk: d[kk])
        d['typeI_frac'] = float(np.mean(m['typeI'][mask])); d['n'] = int(mask.sum())
        out[reg] = d
    cm = (radp >= R1) & (radp <= R2) & (scale > thr)
    out['core_sampled_nec_min'] = float(np.min(m['sampled'][cm]))
    i = int(np.argmin(m['sampled'][cm])); idx = int(np.where(cm)[0][i])
    out['core_sampled_nec_r'] = float(radp[idx])
    ns = scale <= thr
    out['nonsig_median_abs_nec'] = float(np.nanmedian(np.abs(m['nec'][ns]))) if ns.sum() > 10 else None
    out['_m'] = m
    return out

def strip(o):
    return {k: v for k, v in o.items() if not k.startswith('_')}

# ------------------------------------------------------------------ main
def main():
    res = {'python': sys.executable, 'path': 'symbolic radial-reduction (wb_symbolic.py, own derivation)'}
    prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked',
                          params={'wd': 6.0, 'floor': 0.2}, s_rho=4.0, s_P=2.32, Nr=4001)

    # ---- Anchor (i) Minkowski numeric: a=b=S=0 via zero profile
    rng = np.random.default_rng(7)
    pts_m = rng.normal(size=(8, 3)) * 8
    class ZeroS:
        def eval(self, r):
            z = np.zeros_like(r); return z, z, z
    prof0 = dict(prof); prof0['a'] = np.zeros_like(prof['a']); prof0['b'] = np.zeros_like(prof['b'])
    Gm, _ = tensors_at(pts_m, prof0, ZeroS(), 0.37)
    res['anchor_i_minkowski_maxAbsG'] = float(np.max(np.abs(Gm)))

    # ---- Anchor (ii) beta=0 vs shell.py exact spherical T
    from scipy.interpolate import interp1d
    ex = {k: interp1d(prof['r'], prof[k]) for k in ('rho_ex', 'p_r', 'p_t')}
    rows = []
    cosS = CosS(10.0, 30.0)
    for r in (12.0, 15.0, 20.0, 25.0, 28.0):
        p = np.array([[r, 0.37, -0.21]]); p = p * (r / np.linalg.norm(p))
        G, g = tensors_at(p, prof, cosS, 0.0)
        That = eulerian_that(g, G / (8 * np.pi))
        mm = margins(That)
        ps = np.sort(mm['p'][0]); exact = np.sort([float(ex['p_r'](r)), float(ex['p_t'](r)), float(ex['p_t'](r))])
        rows.append({'r': r, 'rho_mine': float(mm['rho'][0]), 'rho_exact': float(ex['rho_ex'](r)),
                     'rho_rel_err': float(abs(mm['rho'][0] - ex['rho_ex'](r)) / max(abs(ex['rho_ex'](r)), 1e-300)),
                     'p_max_abs_err': float(np.max(np.abs(ps - exact))), 'typeI': bool(mm['typeI'][0])})
    res['anchor_ii_static_rows'] = rows
    res['anchor_ii_max_rho_rel_err'] = max(x['rho_rel_err'] for x in rows)
    res['anchor_ii_max_p_abs_err'] = max(x['p_max_abs_err'] for x in rows)
    print('anchors i/ii:', res['anchor_i_minkowski_maxAbsG'], res['anchor_ii_max_rho_rel_err'],
          res['anchor_ii_max_p_abs_err'], flush=True)

    pts, radp = fine_pts(10.0, 30.0)
    assert len(pts) == 1404, len(pts)

    # ---- Anchor (iii) Gate-6 champion, beta=0.08, cosine, full smoothing
    t0 = time.time()
    a3 = audit(pts, radp, prof, cosS, 0.08)
    res['anchor_iii_champion_b0.08'] = strip(a3)
    print('anchor iii:', a3['all_sig']['worst'], a3['all_sig']['typeI_frac'], f"{time.time()-t0:.0f}s", flush=True)

    # ---- spline verification vs stored spline_diag
    finals = {}
    for tag, fn in (('primary_b0.10', 'p503_pol_B_b0.10_K5.json'),
                    ('second_b0.1363', 'p503_pol_B_b0.1363_K5.json')):
        d = json.load(open(f'{P50}/{fn}'))
        so = SplineS(10.0, 30.0, 5, d['z_final'])
        kv_stored = np.array(d['spline_diag']['knot_v']); kr_stored = np.array(d['spline_diag']['knot_r'])
        finals[tag] = {'file': fn, 'z_final': d['z_final'],
                       'knot_r_maxdiff': float(np.max(np.abs(so.knot_r - kr_stored))),
                       'knot_v_maxdiff': float(np.max(np.abs(so.knot_v - kv_stored))),
                       'knot_v': [float(x) for x in so.knot_v], '_S': so}
    res['spline_reconstruction'] = {k: {kk: vv for kk, vv in v.items() if not kk.startswith('_')}
                                    for k, v in finals.items()}
    print('spline knot diffs:', [(k, v['knot_v_maxdiff']) for k, v in finals.items()], flush=True)

    # ---- deciding set, both finalists at beta=0.10
    for tag in finals:
        t0 = time.time()
        o = audit(pts, radp, prof, finals[tag]['_S'], 0.10)
        res[f'deciding_{tag}_b0.10'] = strip(o)
        print(tag, 'worst', o['all_sig']['worst'], o['all_sig']['worst_kind'], '@', o['all_sig'][o['all_sig']['worst_kind'] + '_r'],
              'coreWorst', o['core']['worst'], 'tI', o['all_sig']['typeI_frac'],
              'samp', o['core_sampled_nec_min'], f"{time.time()-t0:.0f}s", flush=True)
        # robustness set
        rp, rr = robust_pts(10.0, 30.0)
        ro = audit(rp, rr, prof, finals[tag]['_S'], 0.10)
        res[f'robust_{tag}_b0.10'] = strip(ro)
        print(tag, 'robust worst', ro['all_sig']['worst'], 'tI', ro['all_sig']['typeI_frac'], flush=True)

    json.dump(res, open(G7 + '/results/wb_g72_numbers.json', 'w'), indent=1, default=float)
    print('DONE', flush=True)

if __name__ == '__main__':
    main()
