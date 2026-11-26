#!/usr/bin/env python3
"""
g41_audit.py -- Gate-41 deciding reads (VM, frame of record;
run only after g41_calibrate.py passes).

A. Centre zero-displacement reads at mu = 1.1125 (H1) and
   mu = 1.15 (H2) vs Phase 374's bottom identities, plus the
   centres' N/M floor minima on FINE_R.
B. Incumbent reads: H1 and H2 final incumbents (K = 17
   vectors from p379_confirmation.json) -- SET read,
   adversary-polish depth, exact worst-null at the SET NEC
   argmin; margins against the centre bars and L_ceil.
C. H2 end-clamp re-read (first/last knots of all three
   correction vectors zeroed).
"""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate41/work')
import g41_lib as G  # noqa: E402

L_CEIL = -0.0002099385079591706
BAR = {'H1': -0.0002099385079591706, 'H2': -0.000203181133812098}
IDENT = {   # Phase 374 bottom identities (charge / Gate-40 S3)
    'H1': {'nec': -0.0002099385079591706,
           'dec': -0.00019410812223900952,
           'rho': 8.764071936094003e-05},
    'H2': {'nec': -0.000203181133812098,
           'dec': -0.00018546990569430298,
           'rho': 8.801281960223608e-05},
}
FLOOR_TGT = {'H1': {'N': 1.1125340342235222, 'M': 1.1206906539640158},
             'H2': {'N': 1.1500351814445395, 'M': 1.1247588782549376}}
MU = {'H1': G.MU_H1, 'H2': G.MU_H2}
OUT = {}


def rec(name, **kw):
    OUT[name] = kw
    print(name, json.dumps(kw, default=str)[:700], flush=True)


# ---------------- A: centres
for c in ('H1', 'H2'):
    mu = MU[c]
    s, _ = G.set_read(mu, None, None, None, 17)
    pr = G.centre_profiles(mu, G.FINE_R)
    Nmin = float(np.min(pr[3])); Mmin = float(np.min(pr[6]))
    rec(f'A_centre_{c}', mu=mu,
        nec=s['nec']['min'], dec=s['dec']['min'], rho=s['rho']['min'],
        diffs={k: float(s[k]['min'] - IDENT[c][k])
               for k in ('nec', 'dec', 'rho')},
        typeI_count=s['typeI_count'],
        N_min_FINE_R=Nmin, M_min_FINE_R=Mmin,
        floor_diffs={'N': Nmin - FLOOR_TGT[c]['N'],
                     'M': Mmin - FLOOR_TGT[c]['M']})

# ---------------- B: incumbents
for c in ('H1', 'H2'):
    mu = MU[c]
    ent = G.load_379_incumbent(c)
    vS = np.array(ent['vS'], dtype=G.DTYPE)
    vN = np.array(ent['vN'], dtype=G.DTYPE)
    vM = np.array(ent['vM'], dtype=G.DTYPE)
    K = int(ent['K'])
    s, aux = G.set_read(mu, vS, vN, vM, K)
    pol = G.adversary_polish(mu, vS, vN, vM, K, aux)
    argmin_pt = np.array(s['nec_argmin_point'], dtype=G.DTYPE)
    _, _, That = G.nec_at(mu, vS, vN, vM, K, argmin_pt)
    wn, wnf = G.worst_null(That)
    joint = min(s['nec']['min'], s['dec']['min'])
    rec(f'B_incumbent_{c}', K=K,
        nec=s['nec']['min'], dec=s['dec']['min'], rho=s['rho']['min'],
        wec=s['wec']['min'], sec=s['sec']['min'], joint=joint,
        nec_argmin_r=s['nec_argmin_r'], dec_argmin_r=s['dec_argmin_r'],
        dec_argmin_typeI=s['dec_argmin_typeI'],
        typeI_count=s['typeI_count'],
        stored={'nec': ent['set']['nec']['min'],
                'dec': ent['set']['dec']['min'],
                'rho': ent['set']['rho']['min'],
                'wec': ent['set']['wec']['min'],
                'sec': ent['set']['sec']['min'],
                'typeI_count': ent['set']['typeI_count'],
                'depth': ent['depth_SAMPLER-M_polished'],
                'worst_null': ent['worst_null_at_set_nec_argmin']},
        diffs={'nec': float(s['nec']['min'] - ent['set']['nec']['min']),
               'dec': float(s['dec']['min'] - ent['set']['dec']['min']),
               'rho': float(s['rho']['min'] - ent['set']['rho']['min']),
               'wec': float(s['wec']['min'] - ent['set']['wec']['min']),
               'sec': float(s['sec']['min'] - ent['set']['sec']['min'])},
        depth=pol['in_region_worst_nec_SAMPLER-M'],
        depth_diff=float(pol['in_region_worst_nec_SAMPLER-M']
                         - ent['depth_SAMPLER-M_polished']),
        depth_source=pol['source'],
        worst_null=wn, worst_null_fib=wnf,
        worst_null_diff=float(wn - ent['worst_null_at_set_nec_argmin']),
        margin_over_centre_bar=float(joint - BAR[c]),
        margin_over_L_ceil=float(joint - L_CEIL),
        boundary={'S': [float(vS[0]), float(vS[-1])],
                  'N': [float(vN[0]), float(vN[-1])],
                  'M': [float(vM[0]), float(vM[-1])]})

# ---------------- C: H2 end-clamp
ent = G.load_379_incumbent('H2')
vS = np.array(ent['vS'], dtype=G.DTYPE)
vN = np.array(ent['vN'], dtype=G.DTYPE)
vM = np.array(ent['vM'], dtype=G.DTYPE)
for v in (vS, vN, vM):
    v[0] = 0.0; v[-1] = 0.0
s, _ = G.set_read(G.MU_H2, vS, vN, vM, int(ent['K']))
joint = min(s['nec']['min'], s['dec']['min'])
st = {'nec_min': -0.00019562414497796698,
      'dec_min': -0.0002087299309761311,
      'rho_min': 8.793529206482093e-05,
      'pure': -0.0002087299309761311}
rec('C_endclamp_H2', nec=s['nec']['min'], dec=s['dec']['min'],
    rho=s['rho']['min'], joint=joint, stored=st,
    diffs={'nec': float(s['nec']['min'] - st['nec_min']),
           'dec': float(s['dec']['min'] - st['dec_min']),
           'rho': float(s['rho']['min'] - st['rho_min']),
           'joint': float(joint - st['pure'])},
    clamped_margin_over_L_ceil=float(joint - L_CEIL),
    clamped_margin_over_H2_centre_bar=float(joint - BAR['H2']))

with open('/home/hatch/workspace/warp-pilot/gate41/results/'
          'g41_numbers.json', 'w') as fh:
    json.dump(OUT, fh, indent=1)
print('audit written')
