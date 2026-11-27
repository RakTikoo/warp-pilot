"""Gate-55 laptop admission driver — runs on the laptop pool
mirror. Recomputes the deciding reads of claims (a), (b), (c)
on g55_lib and writes g55_laptop_results.json beside itself.
VM reads remain deciding; this is the admission control."""
import json
import sys
import numpy as np

sys.path.insert(0, '/home/spark/work/g55root')
import g55_lib as G

ROOT = '/home/spark/work/g55root'


def load(p):
    with open(p) as f:
        return json.load(f)


t420 = load(f'{ROOT}/p420_targets.json')
fitCA = load(f'{ROOT}/p420_fitCA_primary.json')
fitCB = load(f'{ROOT}/p420_fitCB_primary.json')

sitesA = t420['sitesA']
sitesB = t420['sitesB']
ptsA = [np.array(s['point']) for s in sitesA]
ptsB = [np.array(s['point']) for s in sitesB]
nhA = [p / np.linalg.norm(p) for p in ptsA]
TreqA = [np.array(s['T_req']) for s in sitesA]
TreqB = [np.array(s['T_req']) for s in sitesB]
Tcorr_stored = [np.array(s['T_corr']) for s in sitesA]

out = {}
# claim (a): delta rebuild
mx = 0.0
Tcorr_gate = []
for i in range(3):
    delta, info = G.build_delta(TreqA[i])
    Tc = TreqA[i] + delta
    Tcorr_gate.append(Tc)
    mx = max(mx, float(np.max(np.abs(Tc - Tcorr_stored[i]))))
out['claim_a_Tcorr_rebuild_maxdiff'] = mx


def blocks_of(sol):
    bl = [(np.array(sol['pvecs1']), G.avecs_from_json(sol['avecs1']),
           float(sol['m1']))]
    if sol['N2'] > 0:
        bl.append((np.array(sol['pvecs2']),
                   G.avecs_from_json(sol['avecs2']), float(sol['m2'])))
    return bl


def direct_residuals(blocks, points, targets):
    f = G.field_from_blocks(blocks)
    return [float(np.linalg.norm(f.stress(p) - t))
            for p, t in zip(points, targets)]


blkCA = blocks_of(fitCA)
out['claim_b_fitCA_Rs'] = direct_residuals(blkCA, ptsA, Tcorr_gate)
blkCB = blocks_of(fitCB)
out['claim_b_fitCB_Rs'] = direct_residuals(blkCB, ptsB, TreqB)

fCA = G.field_from_blocks(blkCA)
cc = {}
for i, s in enumerate(sitesA):
    Tsup = fCA.stress(ptsA[i])
    d = G.decompose(Tsup, nhA[i])
    cc[s['key']] = {'T00': float(Tsup[0, 0]),
                    'rho_eigen': d['channels']['rho'],
                    'SEC_trace': d['channels']['SEC_trace'],
                    'min_all': float(min(
                        G.joint_channel_values(d['channels']) + [
                            d['channels']['SEC_trace'],
                            d['channels']['SEC_r']]
                        + list(d['channels']['SEC_t'])))}
out['claim_c'] = cc
with open(f'{ROOT}/g55_laptop_results.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
