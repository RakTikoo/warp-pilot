"""
W-A G9-1 deciding run: the audited member
  b(r) = r^{1/10}            (r0 = 1, p = 0.1)
  Phi2 = a ln r / (1 + ln r), a = 0.27773424114865775 (audited point,
  p611_ecaudit.json; claim statement rounds to 0.277734)
Fresh engine (wa_engine.py, registered x2 Bach convention).
Stage 1: float64 grid, 2500 log-spaced points on [1, 1000].
Stage 2: 40+ digit probes at the throat (extrapolated limit and
1+1e-9) and the tail r = 1000.
B-combinations: rho=-Bt, pr=Br, pt=Bth; DEC_i = rho - |p_i| (the
phase convention that reproduces the stored numbers); the gate-bar
forms rho - p_i are also recorded.
Writes results/wa_member_grid.json and results/wa_member_probes.json.
"""
import sys, json, time, pickle
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate9')
import sympy as sp
import numpy as np
from wa_engine import build_bach, r, th

A = sp.Rational(27773424114865775, 10**17)
t0 = time.time()
out = build_bach(r**sp.Rational(1, 10), A * sp.log(r) / (1 + sp.log(r)),
                 final_simplify=False)
print('build_s', time.time() - t0, flush=True)
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_member_exprs.pkl', 'wb') as fh:
    pickle.dump({k: sp.srepr(out[k]) for k in ('Bt', 'Br', 'Bth')}, fh)
for k in ('Bt', 'Br', 'Bth'):
    print(k, 'count_ops', sp.count_ops(out[k]), flush=True)

Bt = out['Bt'].subs(th, 1)
Br = out['Br'].subs(th, 1)
Bth = out['Bth'].subs(th, 1)

# ---------- Stage 1: float64 grid ----------
fBt = sp.lambdify(r, Bt, modules='numpy', cse=True)
fBr = sp.lambdify(r, Br, modules='numpy', cse=True)
fBth = sp.lambdify(r, Bth, modules='numpy', cse=True)
grid = np.logspace(0, 3, 2500)
bt = np.asarray(fBt(grid), dtype=float)
br = np.asarray(fBr(grid), dtype=float)
bth = np.asarray(fBth(grid), dtype=float)
rho, pr, pt = -bt, br, bth
combos = {
    'rho': rho,
    'NEC1': rho + pr,
    'NEC2': rho + pt,
    'DEC_r': rho - np.abs(pr),
    'DEC_t': rho - np.abs(pt),
    'SEC': rho + pr + 2 * pt,
    'DEC_r_gateform_rho_minus_pr': rho - pr,
    'DEC_t_gateform_rho_minus_pt': rho - pt,
    'trace': -rho + pr + 2 * pt,
}
gres = {'n_points': int(grid.size), 'nan_counts': {}, 'minima': {}}
for name, arr in combos.items():
    gres['nan_counts'][name] = int(np.isnan(arr).sum())
    i = int(np.nanargmin(arr))
    gres['minima'][name] = {'value': float(arr[i]), 'at_r': float(grid[i])}
gres['pr_sign'] = {'min': float(np.nanmin(pr)), 'max': float(np.nanmax(pr))}
gres['pt_sign'] = {'min': float(np.nanmin(pt)), 'max': float(np.nanmax(pt))}
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_member_grid.json', 'w') as fh:
    json.dump(gres, fh, indent=1)
print('grid minima', json.dumps(gres['minima']), flush=True)

# ---------- Stage 2: high-precision probes ----------
def probe(rr, digits=50):
    sub = {r: rr, th: 1}
    bt_, br_, bth_ = (sp.N(out['Bt'].subs(sub), digits),
                      sp.N(out['Br'].subs(sub), digits),
                      sp.N(out['Bth'].subs(sub), digits))
    rho_, pr_, pt_ = -bt_, br_, bth_
    return {
        'rho': str(rho_), 'pr': str(pr_), 'pt': str(pt_),
        'NEC1': str(rho_ + pr_), 'NEC2': str(rho_ + pt_),
        'DEC_r': str(rho_ - abs(pr_)), 'DEC_t': str(rho_ - abs(pt_)),
        'SEC': str(rho_ + pr_ + 2 * pt_),
        'DEC_r_gateform': str(rho_ - pr_), 'DEC_t_gateform': str(rho_ - pt_),
    }

pres = {}
for tag, rr in (('tail_1000', sp.Integer(1000)),
                ('throat_1+1e-9', 1 + sp.Rational(1, 10**9)),
                ('throat_1+1e-6', 1 + sp.Rational(1, 10**6)),
                ('throat_1+1e-8', 1 + sp.Rational(1, 10**8)),
                ('throat_1+1e-10', 1 + sp.Rational(1, 10**10))):
    pres[tag] = probe(rr)
    print('probe', tag, 'NEC1', pres[tag]['NEC1'], flush=True)
# quadratic extrapolation in delta -> throat limit for NEC1 / DEC_t
import mpmath as mp
mp.mp.dps = 50
ds = [mp.mpf(10)**-6, mp.mpf(10)**-8, mp.mpf(10)**-10]
for key in ('NEC1', 'DEC_t', 'rho'):
    ys = [mp.mpf(pres[t][key]) for t in
          ('throat_1+1e-6', 'throat_1+1e-8', 'throat_1+1e-10')]
    # quadratic Lagrange extrapolation to delta=0
    lim = mp.mpf(0)
    for i in range(3):
        li = mp.mpf(1)
        for j in range(3):
            if i != j:
                li *= (0 - ds[j]) / (ds[i] - ds[j])
        lim += ys[i] * li
    pres.setdefault('throat_limit_extrapolated', {})[key] = str(lim)
    print('limit', key, lim, flush=True)
with open('/home/hatch/workspace/warp-pilot/gate9/results/wa_member_probes.json', 'w') as fh:
    json.dump(pres, fh, indent=1)
print('total_s', time.time() - t0)
