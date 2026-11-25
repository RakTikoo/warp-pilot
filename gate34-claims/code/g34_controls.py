#!/usr/bin/env python3
"""
g34_controls.py -- Gate-34 controls C1-C3 + record
reproduction, run BEFORE any re-judgement read is quoted.

C1: M == 1 limit vs Phase 295's factorisation (bar 1e-12).
C2: FD guard at the 4 sites + 12 off-site points.
C3: R/Q_K split vs Phase 312's stored per-site values
    (bar 1e-12); split total vs 16 pi * gate rho (1e-15).
REC: gate That at the 4 sites vs p313_targets.json.
"""
import json
import numpy as np
import sys

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate34/work')
import g34_lib as G
import g34_fd as FD

OUT = {}

# ---- stored records -------------------------------------------------
p312 = json.load(open('/home/hatch/workspace/warp-pilot/'
                      'phase312/results/p312_results.json'))
member = [m for m in p312['members']
          if m['label'] == 'ramp_broad_m+1.00'][0]
sites312 = member['sites']
pts_sites = np.array([s['point'] for s in sites312])
t313 = json.load(open('/home/hatch/workspace/warp-pilot/'
                      'phase313/work/p313_targets.json'))
That313 = np.array([s['That'] for s in t313['sites']])
p293t = json.load(open('/home/hatch/workspace/warp-pilot/'
                       'phase293/work/p293_targets.json'))
pts293 = np.array([s['point'] for s in p293t['sites']])

# ---- C1: M == 1 vs Phase 295 factorisation --------------------------
T1, g1 = G.einstein(pts293, m0=0.0)
That1 = G.eulerian_that(g1, T1)
rho_gate = That1[:, 0, 0]
r = np.linalg.norm(pts293, axis=1)
nx = pts293[:, 0] / r
_, S, Sp, _, N, _, _, _, _, _ = G.profiles_at(pts293, m0=0.0)
alpha2 = N ** 2 + G.BETA ** 2 * S ** 2
rho_fact = (-G.BETA ** 2 * Sp ** 2 * (1.0 - nx ** 2)
            / (32.0 * np.pi * alpha2))
c1_diff = np.abs(rho_gate - rho_fact)
OUT['C1'] = {'rho_gate': rho_gate.tolist(),
             'rho_factorisation': rho_fact.tolist(),
             'max_abs_diff': float(np.max(c1_diff)),
             'bar': 1e-12, 'pass': bool(np.max(c1_diff) <= 1e-12)}
# also vs Phase 293's stored site rho values
rho293_stored = np.array([-5.395995e-5, -8.753311e-5,
                          -5.050545e-5, -9.342707e-5])
OUT['C1']['diff_vs_stored_293_rho'] = np.abs(
    rho_gate - rho293_stored).tolist()

# ---- C3: split audit at the winner's sites --------------------------
sp = G.rho_split(pts_sites)
Tg, gg = G.einstein(pts_sites)
Thatg = G.eulerian_that(gg, Tg)
rho_g = Thatg[:, 0, 0]
keys = ['R_over_16pi', 'R1_over_16pi', 'R2_over_16pi', 'QK_over_16pi']
c3 = {}
maxd = 0.0
for i, s in enumerate(sites312):
    for k in keys:
        d = abs(float(sp[k][i]) - float(s[k]))
        maxd = max(maxd, d)
    c3[s['key']] = {k: float(sp[k][i]) for k in keys}
split_tot_diff = np.abs(sp['rho_split'] - rho_g)
OUT['C3'] = {'per_site': c3, 'max_abs_diff_vs_stored': float(maxd),
             'bar': 1e-12, 'pass': bool(maxd <= 1e-12),
             'split_total_vs_gate_rho_maxdiff':
             float(np.max(split_tot_diff)),
             'split_total_bar': 1e-15}

# ---- REC: gate That vs stored That (p313 targets) -------------------
rec_diff = np.abs(Thatg - That313)
OUT['REC'] = {'max_component_diff': float(np.max(rec_diff)),
              'per_site_max': [float(np.max(rec_diff[i]))
                               for i in range(4)],
              'rho_gate': rho_g.tolist(),
              'rho_stored': [float(That313[i][0, 0])
                             for i in range(4)],
              'rho_normal_check': np.abs(
                  G.rho_normal(Tg, gg) - rho_g).tolist()}

# ---- C2: FD guard ----------------------------------------------------
rng = np.random.default_rng(3401)
extra = []
while len(extra) < 12:
    rr = rng.uniform(10.2, 19.8)
    d = rng.normal(size=3); d /= np.linalg.norm(d)
    extra.append(rr * d)
sample_pts = np.vstack([pts_sites, np.array(extra)])
Ta, ga = G.einstein(sample_pts)
Thata = G.eulerian_that(ga, Ta)
fd = FD.fd_that(sample_pts,
                lambda P: G.metric_only(P),
                G.eulerian_that, hs=(0.02, 0.01))
c2 = {}
for h, Thatf in fd.items():
    c2[f'h={h}'] = {
        'max_component_diff_vs_analytic':
        float(np.max(np.abs(Thatf - Thata))),
        'max_rho_diff': float(np.max(np.abs(
            Thatf[:, 0, 0] - Thata[:, 0, 0])))}
OUT['C2'] = c2

print(json.dumps(OUT, indent=1))
json.dump(OUT, open('/home/hatch/workspace/warp-pilot/gate34/'
                    'results/g34_controls.json', 'w'), indent=1)
