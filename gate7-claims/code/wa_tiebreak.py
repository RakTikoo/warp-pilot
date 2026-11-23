"""
wa_tiebreak.py — corroboration of the inner-edge DEC layer found by the
symbolic path on the robustness set (NOT a deciding read):
  * symbolic DEC minima on rings r = 10.05..10.25 (layer thickness);
  * at the symbolic worst point near r=10.05, the Gate-6 FD auditor
    (wa_auditor, 2nd-order direct-d2) at h = 0.15/0.075/0.0375 reads the
    same point — does a different discretisation see the layer?
System python3, float64. Output: results/wa_tiebreak.json
"""
import json, sys
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate7')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate6')
import shell as sh
import wa_eval as ev
import wa_auditor as wa

out = {}
prof = sh.build_shell(10.0, 30.0, 8.0, kind='edgepeaked', params={'wd': 6.0, 'floor': 0.2},
                      s_rho=2.0, s_P=1.16, Nr=4001)
DIRS = ev.fib_dirs(52)
for beta in (0.10, 0.09):
    rows = []
    for rr in (10.02, 10.05, 10.08, 10.10, 10.15, 10.20, 10.25):
        m = ev.audit_symbolic(DIRS * rr, prof, beta)
        i = int(np.nanargmin(m['dec']))
        rows.append({'r': rr, 'dec_min': float(m['dec'][i]),
                     'dec_pt': [float(x) for x in (DIRS * rr)[i]],
                     'typeI_frac': float(np.mean(m['typeI'])),
                     'sampled_nec_min': float(np.min(m['sampled_nec']))})
        print(f"b={beta} r={rr}: DECmin {rows[-1]['dec_min']:+.4e} typeI {rows[-1]['typeI_frac']:.3f} "
              f"sampNEC {rows[-1]['sampled_nec_min']:+.4e}", flush=True)
    out[f'layer_b{beta}'] = rows

# FD read at the symbolic worst point, beta=0.10, r=10.05 ring worst dir
row = min(out['layer_b0.1'], key=lambda x: x['dec_min'])
pt = np.array([row['dec_pt']])
gf = sh.shell_point_factory(prof, 0.10, 'cos', 1.0, [10.0, 30.0])
fd = {}
for h in (0.15, 0.075, 0.0375):
    mf = wa.audit(gf, pt, h)
    fd[f'h{h}'] = {'dec': float(mf['dec'][0]), 'nec': float(mf['nec'][0]),
                   'typeI': bool(mf['typeI'][0]), 'sampled_nec': float(mf['sampled_nec'][0])}
    print(f"FD h={h} at {pt[0]}: DEC {fd[f'h{h}']['dec']:+.4e} NEC {fd[f'h{h}']['nec']:+.4e} "
          f"typeI {fd[f'h{h}']['typeI']}", flush=True)
out['FD_at_symbolic_worst_r10.05_b0.10'] = {'pt': [float(x) for x in pt[0]], 'symbolic_dec': row['dec_min'], 'FD': fd}
json.dump(out, open('/home/hatch/workspace/warp-pilot/gate7/results/wa_tiebreak.json', 'w'), indent=1, default=float)
print('TIEBREAK DONE', flush=True)
