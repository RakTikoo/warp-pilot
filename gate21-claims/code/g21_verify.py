#!/usr/bin/env python3
"""GATE-21 verification driver -- written for this gate from the
registrations (Phases 171/176/178/186, Gate-20). Arranges every
evaluation itself; the exact reads run through the registered
gate-path primitives (p186_common on p1763_common/p1711_common),
priced on GATE21.md's face as at Gate-20. SPECULATIVE throughout.
Frame of record: project venv + Phase 166 pin.
"""
import json, sys
import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, WP + '/phase186/work')
sys.path.insert(0, WP + '/phase176/work')
sys.path.insert(0, WP + '/phase171/work')
import p186_common as P186
import p1763_common as X
import p1711_common as C

SIG_CUT = 23.491427444171965
LAM_VAL = 0.019992372183091776
out = {}

# ---------- load stored artefacts ----------
S = np.load(WP + '/phase186/work/p186_J_coupled_lam010.npz')
res0, scales, J = S['res0'], S['scales'], S['J']
G = np.load(WP + '/phase186/work/p186_grad_lam010.npz')
g41, g44, GD, D0 = G['g41'], G['g44'], G['GD'], G['D0']
ST = np.load(WP + '/phase186/work/p186_opt_lam010_state.npz')
d_fin = ST['d_final']; d_mint = ST['d_mint_063']
basis = X.BASES['Ea']
Cu, Ca, Cb = X.field_value_contribs(basis)

def stats(d, U, sv, Vt):
    y = Vt @ d
    return dict(norm=float(np.linalg.norm(d)),
                max_coeff=float(np.max(np.abs(d))),
                max_field_value=float(max(np.abs(Cu @ d).max(),
                                          np.abs(Ca @ d).max(),
                                          np.abs(Cb @ d).max())),
                frac_below_sigcut=float(np.sum(y[sv < SIG_CUT] ** 2) /
                                        np.sum(y ** 2)))

def exact_all(d, lam, sc, qref=None):
    cl = P186.exact_closure(d, lam, sc)
    gf = X.make_gf_enriched(np.asarray(d, dtype=np.float64), basis)
    fr = P186.reads_lam(gf, lam)
    r = dict(closure=cl, q41=float(fr['q_r'][41]), q44=float(fr['q_r'][44]),
             typeI_sites=[bool(fr['typeI'][41]), bool(fr['typeI'][44])],
             count=int(np.sum(fr['typeI'])),
             D41=float(fr['D_r'][41]), D44=float(fr['D_r'][44]),
             typeI_full=[bool(x) for x in fr['typeI']],
             D_full=[float(x) for x in fr['D_r']])
    if qref is not None:
        r['dq41'] = r['q41'] - qref[0]; r['dq44'] = r['q44'] - qref[1]
    return r

# ---------- (c) spectrum + singular content at lambda=0.10 ----------
U, sv, Vt = np.linalg.svd(J, full_matrices=False)
resid = res0 - U @ (U.T @ res0)
floor = float(np.sqrt(np.mean(resid ** 2)))
out['spectrum'] = dict(smax=float(sv[0]), smin=float(sv[-1]),
                       n_below_sigcut=int(np.sum(sv < SIG_CUT)),
                       subcut_svals=[float(x) for x in sv[sv < SIG_CUT]],
                       LS_floor=floor)
out['witness_stats'] = stats(d_fin, U, sv, Vt)
out['mint063_stats'] = stats(d_mint, U, sv, Vt)

# ---------- path control: Gate-20's lambda_val pass through my path ----
res0v, scalesv = P186.res0_scales_at(LAM_VAL)
d178 = np.load(WP + '/phase178/work/p1781_state.npz')['d_final']
out['path_control_lamval'] = dict(
    res0_scales_recomputed=True,
    closure_178witness_through_g21_path=float(
        P186.exact_closure(d178, LAM_VAL, scalesv)),
    claimed=0.6232117059867903)

# ---------- (a) exact reads of the lambda=0.10 witness ------------------
fr0_010 = P186.reads_lam(X.make_gf_enriched(np.zeros(72), basis), 0.10)
QREF = [float(fr0_010['q_r'][41]), float(fr0_010['q_r'][44])]
out['QREF_recomputed'] = QREF
out['witness_exact'] = exact_all(d_fin, 0.10, scales, QREF)

# ---------- (d) min_t@0.63 field: linearised constraint status ---------
def lin(d):
    return dict(lin_closure=float(np.sqrt(np.mean((res0 + J @ d) ** 2))),
                lin_dq41=float(g41 @ d), lin_dq44=float(g44 @ d),
                lin_count_ok=bool(np.all(np.sign(D0 + GD @ d) == np.sign(D0))),
                lin_count_min_margin=float(np.min(np.sign(D0) * (D0 + GD @ d))))
out['mint063_linearised'] = lin(d_mint)
out['witness_linearised'] = lin(d_fin)

# ---------- (b) d=0 probes across the bracket ---------------------------
probes = {}
for lam in (0.10, 0.11, 0.12, 0.1452):
    fr = P186.reads_lam(X.make_gf_enriched(np.zeros(72), basis), lam)
    D = np.asarray(fr['D_r'], dtype=np.float64)
    probes[str(lam)] = dict(
        q41=float(fr['q_r'][41]), q44=float(fr['q_r'][44]),
        typeI_sites=[bool(fr['typeI'][41]), bool(fr['typeI'][44])],
        count=int(np.sum(fr['typeI'])), D44=float(D[44]), D41=float(D[41]),
        min_abs_D=float(np.min(np.abs(D))), argmin_abs_D=int(np.argmin(np.abs(D))),
        typeI_full=[bool(x) for x in fr['typeI']])
out['d0_probes'] = probes
t10 = probes['0.1']['typeI_full']; t1452 = probes['0.1452']['typeI_full']
out['typeI_flips_010_vs_01452'] = [i for i in range(56) if t10[i] != t1452[i]]

# ---------- robustness of the witness (Gate-20's probe, rescaled) -------
rng = np.random.default_rng(20261123)
rob = {}
for scale in (1e-4, 1e-3):
    for trial in range(2):
        p = rng.standard_normal(72); p *= scale / np.linalg.norm(p)
        r = exact_all(d_fin + p, 0.10, scales, QREF)
        rob[f'{scale}_{trial}'] = dict(
            closure=r['closure'], dq41=r['dq41'], dq44=r['dq44'],
            typeI_sites=r['typeI_sites'], count=r['count'])
out['robustness'] = rob

# linearised flip-distance estimate at the witness (labelled estimate):
# min_i |D_i^exact(witness)| / ||GD_i|| using d=0 gradients
Dw = np.array(out['witness_exact']['D_full'])
gdn = np.linalg.norm(GD, axis=1)
out['lin_flip_distance_est'] = dict(
    min_ratio=float(np.min(np.abs(Dw) / gdn)),
    argmin=int(np.argmin(np.abs(Dw) / gdn)),
    site44_ratio=float(abs(Dw[44]) / gdn[44]))

json.dump(out, open(WP + '/gate21/work/g21_verify_out.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
print('G21 VERIFY DONE')
