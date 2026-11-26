#!/usr/bin/env python3
"""Gate-43 diagnostic (NOT a deciding read): localise
the sampled-margin differences at non-Type-I points.
Compares the gate's That against the lineage's That
at the specific points involved (the Gate-41 C-8
protocol: diagnostic comparison only), and reads the
gate's margins at the STORED argmin points.
Output: gate43/results/g43_diag.json."""
import json
import sys

import numpy as np

sys.path.insert(0, '/home/hatch/workspace/warp-pilot/gate43/work')
import g43_lib as G  # noqa: E402

RES = '/home/hatch/workspace/warp-pilot/gate43/results'
MIX = (0.9323593026620368, 1.1444417317708335, 1.1445068359375)
out = {}

STORED_ARGMIN = {
    'centre_111': {
        'triple': (1.0, 1.0, 1.0), 'clamp': False,
        'pt': [12.330081871976182, -2.9640809161871493,
               -10.112165010538996],
        'nec_stored': -1.9422459891767227e-4,
        'worst_null_stored': -1.9432881962794707e-4},
    'mixed': {
        'triple': MIX, 'clamp': False,
        'pt': [-1.9470056065537118, -10.702464686683815,
               6.28048780487805],
        'nec_stored': -0.00017570735537945242,
        'worst_null_stored': -0.00017703703917379307},
}


def gate_side(name, triple, clamp):
    s, aux = G.set_read(*triple, clamp=clamp)
    R = aux['R']
    nec, tI = R['nec'], R['typeI']
    i = int(np.argmin(nec))
    rec = {'set_nec_min': float(nec[i]),
           'set_nec_argmin_typeI': bool(tI[i]),
           'set_nec_argmin_r': float(G.R_NODES[i // 162]),
           'set_nec_argmin_point': (
               G.DIRS162[i % 162] * G.R_NODES[i // 162]).tolist(),
           'typeI_nec_min': float(np.min(nec[tI])),
           'joint_raw': float(min(s['nec']['min'],
                                  s['dec']['min'])),
           'joint_typeI_nec_dec': float(min(
               float(np.min(nec[tI])), s['dec']['min']))}
    sa = STORED_ARGMIN.get(name)
    if sa and not clamp:
        pt = np.array(sa['pt'], dtype=float)
        nec_pt, ti_pt, That = G.nec_at(*triple, pt)
        _, q_full, _ = G.worst_null(That)
        rec['at_stored_argmin'] = {
            'nec_gate': nec_pt, 'typeI_gate': ti_pt,
            'nec_diff': nec_pt - sa['nec_stored'],
            'worst_null_gate': float(q_full),
            'worst_null_diff': float(q_full)
            - sa['worst_null_stored']}
    out[name + ('_clamped' if clamp else '')] = rec
    print('DIAG', name, 'clamp', clamp, json.dumps(rec),
          flush=True)
    return rec


gate_side('centre_111', (1.0, 1.0, 1.0), False)
gate_side('mix_383pt', (1.225, 1.30, 1.30), False)
gate_side('mixed', MIX, False)
gate_side('centre_111', (1.0, 1.0, 1.0), True)
gate_side('mixed', MIX, True)

# ---- lineage comparison at the gate's (1,1,1) NEC
# argmin point (diagnostic only)
sys.path.insert(0, '/home/hatch/workspace/warp-pilot')
sys.path.insert(0, '/home/hatch/workspace/warp-pilot/phase389/work')
try:
    import p389_lib as L389  # noqa: E402
    import p316_lib as L316  # noqa: E402
    import verify_metric as vm  # noqa: E402
    from p2352_run import margins_chunked  # noqa: E402
    pt = np.array(out['centre_111']['set_nec_argmin_point'],
                  dtype=float)
    _, _, That_g = G.nec_at(1.0, 1.0, 1.0, pt)
    _, _, That_l = L389.nec_at389(1.0, 1.0, 1.0, pt)
    m_l = margins_chunked(That_l[None, :, :])
    m_g = G.margins(That_g[None, :, :])
    _, q_l, _ = L316.worst_null(That_l)
    _, q_g, _ = G.worst_null(That_g)
    out['lineage_cmp_111_argmin'] = {
        'point': pt.tolist(),
        'That_max_abs_diff': float(np.max(np.abs(That_g - That_l))),
        'nec_sampled_lineage': float(m_l['nec'][0]),
        'nec_sampled_gate': float(m_g['nec'][0]),
        'typeI_lineage': bool(m_l['typeI'][0]),
        'worst_null_lineage_That': float(q_l),
        'worst_null_gate_That': float(q_g)}
    print('DIAG lineage_cmp', json.dumps(
        out['lineage_cmp_111_argmin']), flush=True)
except Exception as e:  # diagnostic only; record failure
    out['lineage_cmp_error'] = repr(e)
    print('DIAG lineage_cmp FAILED', repr(e), flush=True)

with open(f'{RES}/g43_diag.json', 'w') as f:
    json.dump(out, f, indent=1)
print('DIAG DONE', flush=True)
