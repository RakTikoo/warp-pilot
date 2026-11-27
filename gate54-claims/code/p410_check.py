#!/usr/bin/env python3
"""
p410_check.py -- independent checker for Phase 410.
Re-derives the deciding numbers from the stored records on a
separate path: targets rebuilt from p405_lib at the stored
site points and compared to p410_targets.json; the primary
solutions' direct-path residuals recomputed from the stored
pvecs/avecs; the channel decomposition of T_req recomputed
from the stored tensors; the verdict re-derived from the
registered forms (registration SS7). Spinor machinery: the
same verbatim block as the driver (spliced at build time).
"""
import json, sys
import numpy as np

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, WP)
sys.path.insert(0, f'{WP}/phase235/work')
sys.path.insert(0, f'{WP}/phase258/work')
sys.path.insert(0, f'{WP}/phase312/work')
sys.path.insert(0, f'{WP}/phase405/work')
import verify_metric as vm  # noqa: E402
import p405_lib as L405  # noqa: E402
from p2352_run import margins_chunked  # noqa: E402

DTYPE = np.float64
CHK = {}

# ============ MACHINERY (Phase 320 verbatim in content) ============
# =====================================================================
# Spinor machinery (Phase 253/257/261/293, verbatim in content)
# =====================================================================
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex); Z2 = np.zeros((2, 2), dtype=complex)
gamma = [np.block([[I2, Z2], [Z2, -I2]])] + [
    np.block([[Z2, s], [-s, Z2]]) for s in (s1, s2, s3)]
gamma_cov = [gamma[0], -gamma[1], -gamma[2], -gamma[3]]  # gamma_a
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
def slash_cov(kcov):
    return sum(gamma[a] * kcov[a] for a in range(4))
def lower(v): return ETA @ v

def u_spinor(pvec, m, chi):
    E = np.sqrt(pvec @ pvec + m * m)
    if m == 0.0:
        denom = np.sqrt(E)
        top = denom * chi
        bot = (s1 * pvec[0] + s2 * pvec[1] + s3 * pvec[2]) @ chi / denom
    else:
        denom = np.sqrt(E + m)
        top = denom * chi
        bot = (s1 * pvec[0] + s2 * pvec[1] + s3 * pvec[2]) @ chi / denom
    return np.concatenate([top, bot]), E

def dirac_residual(u, pvec, m):
    E = np.sqrt(pvec @ pvec + m * m)
    p = np.concatenate([[E], pvec])
    return slash_cov(lower(p)) @ u - m * u

def fields_at_point(modes):
    m = modes[0][3]
    psi = sum(c * u for c, u, pv, _ in modes)
    dpsi = []
    for a in range(4):
        acc = np.zeros(4, dtype=complex)
        for c, u, pv, _ in modes:
            E = np.sqrt(pv @ pv + m * m)
            pa = E if a == 0 else -pv[a - 1]
            acc += c * (-1j * pa) * u
        dpsi.append(acc)
    return psi, dpsi

def T_bilinear(modes, uvec, vvec):
    psi, dpsi = fields_at_point(modes)
    psibar = psi.conj() @ gamma[0]
    dpsibar = [d.conj() @ gamma[0] for d in dpsi]
    def gam(vec): return slash_cov(lower(vec))
    def D(vec): return sum(vec[a] * dpsi[a] for a in range(4))
    def Db(vec): return sum(vec[a] * dpsibar[a] for a in range(4))
    val = (1j / 4) * (psibar @ gam(uvec) @ D(vvec)
                      + psibar @ gam(vvec) @ D(uvec)
                      - Db(uvec) @ gam(vvec) @ psi
                      - Db(vvec) @ gam(uvec) @ psi)
    return float(val.real), psi

def stress_at_point(modes):
    T = np.zeros((4, 4)); psi = None
    for a in range(4):
        for b in range(4):
            va = np.zeros(4); va[a] = 1.0
            vb = np.zeros(4); vb[b] = 1.0
            T[a, b], psi = T_bilinear(modes, va, vb)
    return T, psi

def pairwise_S(modes_pm):
    n = len(modes_pm); S = np.zeros((n, n, 4, 4), dtype=complex)
    pcov = []
    for u, pv, m in modes_pm:
        E = np.sqrt(pv @ pv + m * m)
        pcov.append(np.concatenate([[E], -pv]))
    for i in range(n):
        ui = modes_pm[i][0]; ubar_i = ui.conj() @ gamma[0]
        for j in range(n):
            uj = modes_pm[j][0]
            J = np.array([ubar_i @ gamma_cov[b] @ uj for b in range(4)])
            psum = pcov[i] + pcov[j]
            S[i, j] = 0.25 * (np.outer(psum, J) + np.outer(J, psum))
    return S

def T_from_S(S, c):
    return np.einsum('i,ijab,j->ab', c.conj(), S, c).real

def modes_at_point(pvecs, avecs, m, x):
    modes = []
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        modes.append((np.exp(1j * float(pv @ x)), U, pv, m))
    return modes

def T_direct(pvecs, avecs, m, x):
    T, _ = stress_at_point(modes_at_point(pvecs, avecs, m, x))
    return T

def S_of(pvecs, avecs, m):
    modes_pm = []
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        modes_pm.append((U, pv, m))
    return pairwise_S(modes_pm)

GAMMA_COV_ARR = np.array(gamma_cov)  # (4,4,4)

def S_of_vec(pvecs, avecs, m):
    pvecs = np.asarray(pvecs, dtype=float)
    Us = []
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        Us.append(U)
    U = np.array(Us)                                   # (N,4)
    E = np.sqrt(np.sum(pvecs ** 2, axis=1) + m * m)
    pcov = np.concatenate([E[:, None], -pvecs], axis=1)  # (N,4)
    ubar = U.conj() @ gamma[0]                         # (N,4)
    GU = np.einsum('bac,jc->bja', GAMMA_COV_ARR, U)    # gamma_cov[b] @ U_j
    J = np.einsum('ic,bjc->bij', ubar, GU)             # J[b,i,j]
    psum = pcov[:, None, :] + pcov[None, :, :]         # (i,j,a)
    S = 0.25 * (psum[:, :, :, None] * J.transpose(1, 2, 0)[:, :, None, :]
                + J.transpose(1, 2, 0)[:, :, :, None] * psum[:, :, None, :])
    return S

def T_pairwise(S, pvecs, x):
    ph = np.exp(1j * (pvecs @ x))
    return T_from_S(S, ph)

def segre(T):
    """Phase 257's classifier, verbatim."""
    M = ETA @ T
    ev, evec = np.linalg.eig(M)
    max_im = float(np.max(np.abs(ev.imag))) if np.any(np.abs(ev.imag) > 0) else 0.0
    out = {"eigs": [[float(z.real), float(z.imag)] for z in ev],
           "max_abs_imag": max_im}
    scale = max(1e-30, float(np.max(np.abs(ev.real))))
    if max_im > 1e-9 * scale and max_im > 1e-12:
        out["type"] = "IV (complex pair)"
        return out
    timelike = False
    for idx in range(4):
        v = evec[:, idx].real
        n2 = float(v @ ETA @ v)
        if n2 > 1e-9 * float(v @ v):
            timelike = True
    cond = float(np.linalg.cond(evec))
    out["timelike_eigenvector"] = timelike
    out["evec_cond"] = cond
    if timelike and cond < 1e8:
        out["type"] = "I"
    else:
        out["type"] = "II/III-degenerate (real spectrum, no timelike eigenvector or defective)"
    return out

IU = [(a, b) for a in range(4) for b in range(a, 4)]

# ============ end MACHINERY ============

res = json.load(open('phase410/results/p410_results.json'))
tg = json.load(open('phase410/work/p410_targets.json'))
vS = np.array(tg['winner_vS'], dtype=DTYPE)

# --- targets rebuilt independently -----------------------------------
def That_at(pt):
    T, g = L405.T_at405(vS, 9, np.asarray(pt, dtype=DTYPE)[None, :])
    return vm.eulerian_that(g, T)[0]

max_dThat = 0.0
for grp in ('sitesA', 'sitesB'):
    for s in tg[grp]:
        That2 = That_at(np.array(s['point']))
        max_dThat = max(max_dThat,
                        float(np.max(np.abs(That2 - np.array(s['That'])))))
CHK['targets_max_diff'] = max_dThat
CHK['targets_pass'] = bool(max_dThat <= 1e-12)

# --- primary solutions' direct residuals, recomputed ------------------
def load_primary(lbl):
    d = json.load(open(f'phase410/work/p410_{lbl}_primary.json'))
    pv = np.array(d['pvecs'])
    av = np.array([[complex(*z) for z in row] for row in d['avecs']])
    return d, pv, av

chk_prim = {}
for lbl, grp in (('fitA', 'sitesA'), ('fitB', 'sitesB')):
    d, pv, av = load_primary(lbl)
    Rs = []
    for s in tg[grp]:
        T = T_direct(pv, av, 1.0, np.array(s['point']))
        Rs.append(float(np.linalg.norm(T - np.array(s['That']))))
    chk_prim[lbl] = {'N': d['N'], 'Rs': Rs, 'maxR': max(Rs),
                     'maxR_stored': d['maxR'],
                     'dmaxR': abs(max(Rs) - d['maxR'])}
CHK['primaries'] = chk_prim
CHK['primaries_pass'] = bool(all(v['dmaxR'] <= 1e-12
                                 for v in chk_prim.values()))

# --- decomposition of T_req recomputed --------------------------------
def channels_of(T, nhat):
    sg = segre(T)
    if sg['type'] != 'I':
        return {'segre_type': sg['type']}
    ev, evec = np.linalg.eig(ETA @ T)
    ev = ev.real; evec = evec.real
    tl = None
    for idx in range(4):
        v = evec[:, idx]
        if float(v @ ETA @ v) > 1e-9 * float(v @ v):
            tl = idx
    rho = float(ev[tl])
    ps = []
    for idx in range(4):
        if idx == tl:
            continue
        v = evec[:, idx]
        align = abs(float(v[1:4] @ nhat)) / max(
            float(np.linalg.norm(v[1:4])), 1e-300)
        ps.append((float(-ev[idx]), align))
    ir = int(np.argmax([a for _, a in ps]))
    p_r = ps[ir][0]
    p_ts = [ps[i][0] for i in range(3) if i != ir]
    return {'segre_type': 'I', 'rho': rho, 'p_r': p_r, 'p_t': p_ts,
            'SEC_trace': rho + p_r + sum(p_ts),
            'SEC_min': float(min(rho + p_r + sum(p_ts), rho + p_r,
                                 min(rho + p for p in p_ts))),
            'joint_min': float(min(rho + p_r,
                                   min(rho + p for p in p_ts), rho,
                                   rho - abs(p_r),
                                   min(rho - abs(p) for p in p_ts),
                                   rho - float(np.linalg.norm(T[0, 1:4]))))}

max_dSEC = 0.0
for lbl, grp in (('fitA', 'sitesA'), ('fitB', 'sitesB')):
    dec = res[f'decomposition_{lbl}']
    for s in tg[grp]:
        T = np.array(s['That'])
        nhat = np.array(s['point']) / s['r']
        c = channels_of(T, nhat)
        stored = dec[s['key']]['req']
        if 'channels' in stored:
            max_dSEC = max(max_dSEC,
                           abs(c['SEC_min'] - stored['SEC_min_channel']),
                           abs(c['joint_min'] - stored['joint_min_channel']))
CHK['decomposition_max_diff'] = max_dSEC
CHK['decomposition_pass'] = bool(max_dSEC <= 1e-9)

# --- verdict re-derived ----------------------------------------------
BAR = 1e-9
fitA_ok = res['fitA_diagnostics']['direct']['maxR'] <= BAR
expected = 'SUPPLIES AT THE SITES' if fitA_ok else None
if expected is None:
    v2 = True
    for e in res['decomposition_fitA'].values():
        if 'channel_margin_diffs' not in e:
            v2 = False
            break
        d = e['channel_margin_diffs']
        if abs(d['joint_min']) > 1e-6 or abs(d['SEC_min']) <= 1e-6:
            v2 = False
    expected = ('SUPPLIES THE JOINT CHANNELS BUT NOT SEC' if v2
                else 'DOES NOT SUPPLY')
CHK['verdict_stored'] = res['verdict']['form']
CHK['verdict_expected'] = expected
CHK['verdict_pass'] = bool(expected == res['verdict']['form'])
CHK['all_pass'] = bool(CHK['targets_pass'] and CHK['primaries_pass']
                       and CHK['decomposition_pass'] and CHK['verdict_pass'])
json.dump(CHK, open('phase410/results/p410_check_results.json', 'w'),
          indent=1, default=str)
print(json.dumps(CHK, indent=1, default=str))
