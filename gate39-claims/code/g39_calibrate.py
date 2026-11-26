#!/usr/bin/env python3
"""Gate-39 calibrations C-1..C-7 (C-8 frame admission handled separately
and merged into the same JSON). Stops are reported, not hidden."""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate39/work')
import g39_lib as G  # noqa: E402

BASE = '/home/hatch/workspace/warp-pilot/'
OUT = BASE + 'gate39/results/g39_calibration.json'
TGT = {'nec': -2.319453132752996e-4, 'dec': -2.2336932044559818e-4,
       'wec': -2.1092144017509297e-3, 'sec': -2.379031965576834e-3,
       'rho': 8.638077678074035e-5}
DEPTH_TGT = -2.2644422911711972e-4

cal = {}


def load(p):
    with open(BASE + p) as f:
        return json.load(f)


conf344 = load('phase344/results/p344_confirmation.json')
a2 = [e for e in conf344['confirmations'] if e['point'] == 'A2'][0]
state = load('phase344/results/p344_state_A2.json')['final_incumbent']

# ---- C-1 vectors
md = max(float(np.max(np.abs(np.array(a2[k]) - np.array(state[k]))))
         for k in ('vS', 'vN', 'vM'))
cal['C-1'] = {'max_diff': md, 'pass': bool(md == 0.0)}
print('C-1 max diff', md, flush=True)

centre = G.Centre(a2['vS'], a2['vN'], a2['vM'], 33, m_r2=20.0)
centre_alt = G.Centre(a2['vS'], a2['vN'], a2['vM'], 33, m_r2=19.5)

# ---- C-2 waveform
shapes = [(0.50, 0.0), (0.75, 0.0), (0.875, 0.0), (0.75, 0.50), (0.75, 0.75)]
grid = np.linspace(0.0, 2.0 * np.pi, 4096, endpoint=False)
h = 5.0e-5
c2 = {}
c2_pass = True
for D, m in shapes:
    mu, mup, mupp = G.dwelling_mu(grid, 0.30, D, m)

    def mu_of(x):
        return G.dwelling_mu(x, 0.30, D, m)[0]
    fd1 = (mu_of(grid - 2 * h) - 8 * mu_of(grid - h) + 8 * mu_of(grid + h)
           - mu_of(grid + 2 * h)) / (12.0 * h)
    fd2 = (-mu_of(grid + 2 * h) + 16 * mu_of(grid + h) - 30 * mu_of(grid)
           + 16 * mu_of(grid - h) - mu_of(grid - 2 * h)) / (12.0 * h ** 2)
    e1 = float(np.max(np.abs(fd1 - mup)))
    e2 = float(np.max(np.abs(fd2 - mupp)))
    b1 = 1e-5 * (1.0 + float(np.max(np.abs(mup))))
    b2 = 1e-3 * (1.0 + float(np.max(np.abs(mupp))))
    per = float(np.max(np.abs(mu_of(grid + 2 * np.pi) - mu)))
    lo_t, hi_t = 1 + 0.30 * (2 * m - 1), 1 + 0.30
    range_err = max(abs(float(np.min(mu)) - lo_t), abs(float(np.max(mu)) - hi_t))
    ok = bool(e1 <= b1 and e2 <= b2 and per <= 1e-12 and range_err <= 1e-3 * 0.30)
    c2_pass &= ok
    c2[f'D{D}_m{m}'] = {'fd_err_mu_phi': e1, 'bar_mu_phi': b1,
                        'fd_err_mu_phiphi': e2, 'bar_mu_phiphi': b2,
                        'periodicity_max_diff': per, 'periodicity_bar': 1e-12,
                        'range_endpoints_target': [lo_t, hi_t],
                        'range_min': float(np.min(mu)), 'range_max': float(np.max(mu)),
                        'range_err': range_err, 'pass': ok}
cal['C-2'] = {'shapes': c2, 'pass': bool(c2_pass)}
print('C-2 pass', c2_pass, flush=True)

# ---- C-3 stationary anchor (r2=20.0 primary; r2=19.5 alternative recorded)
def anchor_reads(c):
    out, aux = G.set_read(c, None, 0.0)
    return out, aux
out, aux = anchor_reads(centre)
diffs = {k: float(out[k]['min'] - TGT[k]) for k in TGT}
c3_pass = all(abs(diffs[k]) <= 1e-9 for k in TGT)
pol = G.adversary_polish(centre, None, 0.0, aux)
depth = pol['in_region_worst_nec_SAMPLER-M']
depth_diff = float(depth - DEPTH_TGT)
c3_pass = bool(c3_pass and abs(depth_diff) <= 1e-7)
out_alt, _ = anchor_reads(centre_alt)
diffs_alt = {k: float(out_alt[k]['min'] - TGT[k]) for k in TGT}
cal['C-3'] = {'reads': {k: out[k]['min'] for k in TGT},
              'diffs': diffs,
              'argmin_r': {'nec': out['nec_argmin_r'], 'dec': out['dec_argmin_r']},
              'polished_depth': depth, 'polished_r': pol['r'],
              'polished_depth_diff': depth_diff,
              'm_ramp_r2_used': 20.0,
              'alternative_r2_19.5_diffs': diffs_alt,
              'pass': bool(c3_pass)}
print('C-3 diffs', diffs, 'depth diff', depth_diff, 'pass', c3_pass, flush=True)

# ---- C-4 flat limit
mem_flat = {'subset': 'SNM', 'a': 0.30, 'Om': 2 * np.pi / 40.0,
            'D': 0.75, 'm': 0.0, 'id': 'flat'}
pts = G.DIRS162 * 15.0
Tf, gf = G.T_at(centre, pts, mem_flat, 2.6, flat=True)
mx = float(np.max(np.abs(Tf)))
cal['C-4'] = {'max_abs_T': mx, 'pass': bool(mx <= 1e-14),
              'note': 'bar: exactly 0.0 or <=1e-14'}
print('C-4 max|T|', mx, flush=True)

# ---- C-5 reduction: anchor member at all 32 instants
anchor_mem = {'subset': 'ANCHOR', 'a': 0.0, 'Om': 2 * np.pi / 40.0,
              'D': 0.75, 'm': 0.0, 'id': 'ANCHOR'}
maxd = 0.0
per_inst = []
for j in range(32):
    phi = 2 * np.pi * j / 32
    o, _ = G.set_read(centre, anchor_mem, phi, want_aux=False)
    d = max(abs(o[k]['min'] - TGT[k]) for k in TGT)
    maxd = max(maxd, d)
    per_inst.append({'j': j, 'phi': phi, 'max_diff': float(d)})
cal['C-5'] = {'max_diff_over_instants': float(maxd), 'per_instant': per_inst,
              'pass': bool(maxd <= 1e-9)}
print('C-5 max diff', maxd, flush=True)

# ---- C-6 FD cross-check
mem_t2 = {'subset': 'SNM', 'a': 0.30, 'Om': 2 * np.pi / 40.0,
          'D': 0.75, 'm': 0.0, 'id': 'CTL-T2'}
direction = np.array(a2['set']['nec_argmin_point'], dtype=float)
direction = direction / np.linalg.norm(direction)
rows = []
rel_all = 0.0; abs_small = 0.0; spread_all = 0.0
for phi in (2.6, 3.5):
    t = phi / mem_t2['Om']
    for rr in (12.3, 16.2, 19.4):
        pt = direction * rr
        Ta, ga = G.T_at(centre, pt[None, :], mem_t2, phi)
        pts4 = np.concatenate([[t], pt])[None, :]
        Th, _ = G.einstein_fd(centre, mem_t2, pts4, 0.0125)
        Th2, _ = G.einstein_fd(centre, mem_t2, pts4, 0.00625)
        Ta = Ta[0]; Th = Th[0]; Th2 = Th2[0]
        big = np.abs(Ta) >= 1e-6
        rel = float(np.max(np.abs(Ta - Th2)[big] / np.abs(Th2)[big])) if np.any(big) else 0.0
        rel_h = float(np.max(np.abs(Ta - Th)[big] / np.abs(Th)[big])) if np.any(big) else 0.0
        asm = float(np.max(np.abs(Ta - Th2)[~big])) if np.any(~big) else 0.0
        big2 = np.abs(Th2) >= 1e-6
        spread = float(np.max(np.abs(Th - Th2)[big2] / np.abs(Th2)[big2])) if np.any(big2) else 0.0
        rel_all = max(rel_all, rel); abs_small = max(abs_small, asm)
        spread_all = max(spread_all, spread)
        rows.append({'phi': phi, 'r': rr, 'rel_h0.00625': rel,
                     'rel_h0.0125': rel_h, 'abs_small': asm,
                     'fd_self_spread': spread})
cal['C-6'] = {'pairs': rows, 'rel_max': rel_all, 'abs_small_max': abs_small,
              'fd_self_spread_max': spread_all,
              'pass': bool(rel_all <= 1e-3 and abs_small <= 1e-8
                           and spread_all <= 2e-4)}
print('C-6 rel', rel_all, 'abs_small', abs_small, 'spread', spread_all, flush=True)

# ---- C-7 sinusoidal cross-check vs phase349 stored records
s349 = load('phase349/results/p349_scan.json')
tgt_worst = s349['M_a0.05_T160']['L_worst']
mem_s = {'subset': 'M', 'a': 0.05, 'Om': 2 * np.pi / 160.0, 'id': 'M_a0.05_T160'}
Lw = np.inf
for j in range(32):
    phi = 2 * np.pi * j / 32
    o, _ = G.set_read(centre, mem_s, phi, mode='sine', want_aux=False)
    Lw = min(Lw, min(o['nec']['min'], o['dec']['min']))
d_worst = float(Lw - tgt_worst)
mem_s2 = {'subset': 'SNM', 'a': 0.30, 'Om': 2 * np.pi / 40.0, 'id': 'SNM_a0.30_T40'}
inst0 = s349['SNM_a0.30_T40']['instants'][0]
inst8 = s349['SNM_a0.30_T40']['instants'][8]
assert abs(inst0['phi']) < 1e-15 and abs(inst8['phi'] - np.pi / 2) < 1e-12
o0, _ = G.set_read(centre, mem_s2, 0.0, mode='sine', want_aux=False)
L0 = min(o0['nec']['min'], o0['dec']['min'])
op, _ = G.set_read(centre, mem_s2, np.pi / 2, mode='sine', want_aux=False)
Lp = min(op['nec']['min'], op['dec']['min'])
d0 = float(L0 - inst0['L']); dp = float(Lp - inst8['L'])
c7_pass = bool(abs(d_worst) <= 2e-6 and abs(d0) <= 2e-6 and abs(dp) <= 2e-6)
cal['C-7'] = {'M_a0.05_T160_worst': {'mine': float(Lw), 'stored': tgt_worst,
                                     'diff': d_worst},
              'SNM_a0.30_T40_L_phi0': {'mine': float(L0), 'stored': inst0['L'],
                                       'diff': d0},
              'SNM_a0.30_T40_L_phi_pi2': {'mine': float(Lp), 'stored': inst8['L'],
                                          'diff': dp},
              'pass': c7_pass}
print('C-7 diffs', d_worst, d0, dp, flush=True)

# ---- SYM: sympy spot-check of the generic Christoffel/Ricci algebra
try:
    import sympy as sp
    t, x, y, z = sp.symbols('t x y z')
    coords = [t, x, y, z]
    # a generic (non-metric-form) symmetric polynomial metric
    gsym = sp.zeros(4, 4)
    base = [[-1 - sp.Rational(1, 10) * x ** 2 - sp.Rational(1, 20) * t * y,
             sp.Rational(1, 30) * x * y + sp.Rational(1, 50) * t,
             sp.Rational(1, 40) * z, sp.Rational(1, 60) * x * t],
            [None, 1 + sp.Rational(1, 15) * y ** 2 + sp.Rational(1, 25) * t * z,
             sp.Rational(1, 35) * x * z, sp.Rational(1, 45) * y],
            [None, None, 1 + sp.Rational(1, 12) * x * t + sp.Rational(1, 20) * z ** 2,
             sp.Rational(1, 55) * x],
            [None, None, None, 1 + sp.Rational(1, 18) * x ** 2 - sp.Rational(1, 30) * t]]
    for i in range(4):
        for j in range(4):
            gsym[i, j] = base[i][j] if base[i][j] is not None else base[j][i]
    ginv_s = gsym.inv()
    dg_s = [[[sp.diff(gsym[mu, nu], coords[e]) for nu in range(4)]
             for mu in range(4)] for e in range(4)]
    Gam_s = [[[sum(ginv_s[a, d] * (dg_s[b][d][c] + dg_s[c][d][b] - dg_s[d][b][c])
                   for d in range(4)) / 2 for c in range(4)]
              for b in range(4)] for a in range(4)]
    Ric_s = sp.zeros(4, 4)
    for b in range(4):
        for d in range(4):
            v = 0
            for a in range(4):
                v += sp.diff(Gam_s[a][b][d], coords[a]) - sp.diff(Gam_s[a][b][a], coords[d])
                for e in range(4):
                    v += Gam_s[a][a][e] * Gam_s[e][b][d] - Gam_s[a][d][e] * Gam_s[e][b][a]
            Ric_s[b, d] = v
    Rs_s = sum(ginv_s[i, j] * Ric_s[i, j] for i in range(4) for j in range(4))
    G_s = Ric_s - Rs_s * gsym / 2
    pt = {t: 0.7, x: 1.3, y: -0.6, z: 2.1}
    Gnum = np.array(G_s.subs(pt), dtype=float) / (8 * np.pi)
    gv = np.array(gsym.subs(pt), dtype=float)
    dgv = np.zeros((1, 4, 4, 4)); ddgv = np.zeros((1, 4, 4, 4, 4))
    for e in range(4):
        dgv[0, e] = np.array([[sp.diff(gsym[mu, nu], coords[e]).subs(pt)
                               for nu in range(4)] for mu in range(4)], dtype=float)
        for f_ in range(4):
            ddgv[0, e, f_] = np.array(
                [[sp.diff(gsym[mu, nu], coords[e], coords[f_]).subs(pt)
                  for nu in range(4)] for mu in range(4)], dtype=float)
    Gmine = G.einstein_from_gdg(gv[None], dgv, ddgv)[0]
    sym_diff = float(np.max(np.abs(Gnum - Gmine)))
    cal['SYM'] = {'max_abs_diff_vs_sympy_generic_metric': sym_diff,
                  'pass': bool(sym_diff <= 1e-10)}
    print('SYM diff', sym_diff, flush=True)
except Exception as exc:  # recorded, not hidden
    cal['SYM'] = {'error': repr(exc), 'pass': False}
    print('SYM error', exc, flush=True)

cal['ALL_C1_C7_PASS'] = bool(all(cal[k]['pass'] for k in
                                 ('C-1', 'C-2', 'C-3', 'C-4', 'C-5', 'C-6', 'C-7')))
with open(OUT, 'w') as f:
    json.dump(cal, f, indent=1)
print('ALL', cal['ALL_C1_C7_PASS'], flush=True)
