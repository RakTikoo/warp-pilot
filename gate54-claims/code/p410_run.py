#!/usr/bin/env python
"""P410 driver — SOURCE THE CANDIDATE: the spinor supplier at the
Phase 405 winner's sites. Registration:
phase410/work/p410_registration.md (written before this run).
Spinor side: Phase 320's driver machinery verbatim in content
(itself Phase 313/293/261 verbatim), spliced in below between
the MACHINERY markers. Target side: Phase 405's own assembly
(p405_lib, the frame of record for the winner). Controls first:
CTRL-320 and CTRL-313 (the stored matings rebuilt on this
machinery copy: direct residuals + FD-Jacobian sigma_min),
CTRL-TGT-410 (the winner's target extraction against the
stored record). Then Item 1 (sites + targets), Item 2
(Fit A named sites; Fit B stencil tracking), Item 3 (channel
decomposition + the supplier's own accounting), verdict.
Run from ~/workspace/warp-pilot/ with the programme venv python.
"""
import json, sys, time
import numpy as np
from scipy.optimize import least_squares

t_start = time.time()
rng = np.random.default_rng(4101)
OUT = {"phase": 410}

WP = '/home/hatch/workspace/warp-pilot'
sys.path.insert(0, WP)
sys.path.insert(0, f'{WP}/phase235/work')
sys.path.insert(0, f'{WP}/phase258/work')
sys.path.insert(0, f'{WP}/phase267/work')
sys.path.insert(0, f'{WP}/phase274/work')
sys.path.insert(0, f'{WP}/phase312/work')
sys.path.insert(0, f'{WP}/phase405/work')
import verify_metric as vm  # noqa: E402
import p312_lib as L312  # noqa: E402
import p405_lib as L405  # noqa: E402
from p2352_run import margins_chunked, fib_dirs  # noqa: E402
from p258_lib import R_NODES, DIRS162  # noqa: E402

DTYPE = np.float64

# Phase 257 best fit — the lineage warm start (folded amplitudes,
# Phase 320's construction verbatim).
bf257 = json.load(open("phase257/work/p257_bestfit.json"))
bf_modes = []
for md in bf257["modes"]:
    u = np.array([complex(a, b) for a, b in md["u"]])
    bf_modes.append((complex(*md["c"]), u, np.array(md["pvec"]), 1.0))
bf_pvecs = np.array([pv for _, _, pv, _ in bf_modes])
bf_avecs = []
for c, u, pv, m in bf_modes:
    E = np.sqrt(pv @ pv + m * m)
    chi = u[:2] / np.sqrt(E + m)
    bf_avecs.append(c * chi)
bf_avecs = np.array(bf_avecs)

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

# =====================================================================
# Generic fit machinery over an arbitrary site list (Phase 320's
# ITEM 2 pattern, generalised from 4 sites to ns sites)
# =====================================================================
def unpack(theta, N):
    pvecs = theta[:3 * N].reshape(N, 3)
    avecs = (theta[3 * N:5 * N] + 1j * theta[5 * N:7 * N]).reshape(N, 2)
    return pvecs, avecs


def pack(pvecs, avecs):
    return np.concatenate([pvecs.ravel(), avecs.real.ravel(),
                           avecs.imag.ravel()])


def make_resid(XS, THATS, FROBS):
    ns = len(XS)

    def resid_vec(theta, N, m):
        pvecs, avecs = unpack(theta, N)
        S = S_of(pvecs, avecs, m)
        r = np.empty(10 * ns)
        for si in range(ns):
            T = T_pairwise(S, pvecs, XS[si])
            d = T - THATS[si]
            r[si * 10:(si + 1) * 10] = np.array([d[a, b] for a, b in IU]) / FROBS[si]
        return r
    return resid_vec


def site_residuals(pvecs, avecs, m, XS, THATS, KSTARS, direct=False):
    Rs, tkks, rhos = [], [], []
    if direct:
        for si in range(len(XS)):
            T = T_direct(pvecs, avecs, m, XS[si])
            Rs.append(float(np.linalg.norm(T - THATS[si])))
            tkks.append(float(KSTARS[si] @ T @ KSTARS[si]))
            rhos.append(float(T[0, 0]))
    else:
        S = S_of(pvecs, avecs, m)
        for si in range(len(XS)):
            T = T_pairwise(S, pvecs, XS[si])
            Rs.append(float(np.linalg.norm(T - THATS[si])))
            tkks.append(float(KSTARS[si] @ T @ KSTARS[si]))
            rhos.append(float(T[0, 0]))
    return Rs, tkks, rhos


def rand_theta(N, m, rng_, a_scale=0.03):
    pvecs = []
    for _ in range(N):
        d = rng_.normal(size=3); d /= np.linalg.norm(d)
        pvecs.append(rng_.uniform(0.05, 6.0) * d)
    avecs = (rng_.normal(size=(N, 2)) + 1j * rng_.normal(size=(N, 2))) * a_scale
    return pack(np.array(pvecs), avecs)


def warm_theta(N, rng_):
    pvecs = list(bf_pvecs); avecs = list(bf_avecs)
    while len(pvecs) < N:
        d = rng_.normal(size=3); d /= np.linalg.norm(d)
        pvecs.append(rng_.uniform(0.05, 6.0) * d)
        avecs.append((rng_.normal(size=2) + 1j * rng_.normal(size=2)) * 0.01)
    return pack(np.array(pvecs[:N]), np.array(avecs[:N]))


def run_fits(N, m, XS, THATS, FROBS, KSTARS, starts, max_nfev, label):
    # Per-start persistence + resume (recovery amendment, Phase 320
    # precedent): every completed start is appended to a JSONL file
    # as it finishes; on a re-run, starts already in the file are
    # loaded, not re-run.
    import os
    tag = label.replace(" ", "_")
    cfile = f"phase410/work/p410_cands_{tag}.jsonl"
    done = {}
    if os.path.exists(cfile):
        for line in open(cfile):
            rec = json.loads(line)
            pv = np.array(rec["pvecs"])
            av = np.array([[complex(*z) for z in row]
                           for row in rec["avecs"]])
            Rs, tkks, rhos = site_residuals(pv, av, m, XS, THATS, KSTARS)
            done[rec["start"]] = {"start": rec["start"],
                                  "theta": pack(pv, av), "pvecs": pv,
                                  "avecs": av, "Rs": Rs, "tkks": tkks,
                                  "rhos": rhos, "maxR": max(Rs),
                                  "cost_time_s": rec["cost_time_s"],
                                  "nfev": rec["nfev"]}
    _trunc = ((tag == "fitB_N6" and os.environ.get("P410_TRUNC_FITB_N6"))
              or (tag == "fitB_N8"
                  and os.environ.get("P410_TRUNC_FITB_N8")))
    if _trunc:
        # Recovery amendments 2/3: arm truncated at the starts
        # already persisted.
        starts = [s for s in starts if s[0] in done]
        print(f"  [{label}] arm TRUNCATED at {len(starts)} persisted "
              f"starts (recovery amendments 2/3)", flush=True)
    resid_vec = make_resid(XS, THATS, FROBS)
    cands = []
    for name, th0 in starts:
        if name in done:
            cands.append(done[name])
            print(f"  [{label}] start={name} RESUMED "
                  f"maxR={done[name]['maxR']:.3e}", flush=True)
            continue
        t0 = time.time()
        sol = least_squares(resid_vec, th0, args=(N, m), method="trf",
                            max_nfev=max_nfev)
        pvecs, avecs = unpack(sol.x, N)
        Rs, tkks, rhos = site_residuals(pvecs, avecs, m, XS, THATS, KSTARS)
        cand = {"start": name, "theta": sol.x, "pvecs": pvecs,
                "avecs": avecs, "Rs": Rs, "tkks": tkks, "rhos": rhos,
                "maxR": max(Rs), "cost_time_s": time.time() - t0,
                "nfev": int(sol.nfev)}
        cands.append(cand)
        with open(cfile, "a") as fh:
            fh.write(json.dumps(
                {"start": name, "maxR": cand["maxR"], "Rs": Rs,
                 "tkks": tkks, "rhos": rhos, "nfev": cand["nfev"],
                 "cost_time_s": cand["cost_time_s"],
                 "pvecs": pvecs.tolist(),
                 "avecs": [[[float(z.real), float(z.imag)] for z in row]
                           for row in avecs]}) + "\n")
        print(f"  [{label}] start={name} maxR={max(Rs):.3e} "
              f"Rs={['%.2e' % r for r in Rs]} nfev={sol.nfev} "
              f"({time.time() - t0:.1f}s)", flush=True)
    cands.sort(key=lambda c: c["maxR"])
    return cands


def fd_jacobian(resid_vec, theta_d, N, m, ns):
    J = np.empty((10 * ns, 7 * N))
    for j in range(7 * N):
        h = 1e-6 * max(1.0, abs(theta_d[j]))
        tp = theta_d.copy(); tp[j] += h
        tm = theta_d.copy(); tm[j] -= h
        J[:, j] = (resid_vec(tp, N, m) - resid_vec(tm, N, m)) / (2.0 * h)
    return J


def jacobian_report(resid_vec, theta_d, N, m, ns):
    J = fd_jacobian(resid_vec, theta_d, N, m, ns)
    sv = np.linalg.svd(J, compute_uv=False)
    blocks = {}
    for si in range(ns):
        svb = np.linalg.svd(J[si * 10:(si + 1) * 10, :], compute_uv=False)
        blocks[str(si)] = {"sigma_min": float(svb[-1]),
                           "sigma_max": float(svb[0]),
                           "rank_tol_1e-10_rel": int(np.sum(svb > 1e-10 * svb[0]))}
    return {"shape": [10 * ns, int(7 * N)],
            "singular_values": [float(v) for v in sv],
            "rank_tol_1e-10_rel": int(np.sum(sv > 1e-10 * sv[0])),
            "sigma_min": float(sv[-1]), "sigma_max": float(sv[0]),
            "per_site_blocks": blocks}


def dirac_max_residual(pvecs, avecs, m):
    mx = 0.0
    for pv, av in zip(pvecs, avecs):
        U, _ = u_spinor(pv, m, av)
        r = dirac_residual(U, pv, m)
        mx = max(mx, float(np.max(np.abs(r))))
    return mx


# =====================================================================
# CONTROLS — CTRL-320 / CTRL-313: the stored matings rebuilt on
# this machinery copy (direct residuals + FD-Jacobian sigma_min)
# =====================================================================
def control_stored_match(phase_dir, stored_sigma, label):
    tg = json.load(open(f"{phase_dir}/work/p{label}_targets.json"))
    bf = json.load(open(f"{phase_dir}/work/p{label}_joint_bestfit.json"))
    m = float(bf["m"]); N = int(bf["N"])
    pvecs = np.array([md["pvec"] for md in bf["modes"]])
    avecs = np.array([[complex(*z) for z in md["a"]] for md in bf["modes"]])
    XS = [np.array(s["point"]) for s in tg["sites"]]
    THATS = [np.array(s["That"]) for s in tg["sites"]]
    FROBS = np.array([float(np.linalg.norm(t)) for t in THATS])
    KSTARS = [np.array(s["kstar"]) for s in tg["sites"]]
    Rs, tkks, rhos = site_residuals(pvecs, avecs, m, XS, THATS, KSTARS,
                                    direct=True)
    stored_Rs = [float(v) for v in bf["Rs_direct"]]
    theta = pack(pvecs, avecs)
    resid_vec = make_resid(XS, THATS, FROBS)
    jac = jacobian_report(resid_vec, theta, N, m, len(XS))
    rep = {"N": N, "m": m, "Rs": Rs, "Rs_stored": stored_Rs,
           "maxR": max(Rs), "maxR_stored": max(stored_Rs),
           "sigma_min": jac["sigma_min"],
           "sigma_min_stored": stored_sigma,
           "sigma_rel_diff": abs(jac["sigma_min"] - stored_sigma) / stored_sigma,
           "rank": jac["rank_tol_1e-10_rel"], "jac_shape": jac["shape"]}
    return rep


c320 = control_stored_match("phase320", 3.994300907411277e-04, "320")
c320["pass"] = bool(c320["maxR"] <= 2 * c320["maxR_stored"]
                    and c320["maxR"] <= 1e-12
                    and c320["sigma_rel_diff"] <= 0.01)
OUT["CTRL320"] = c320
print("CTRL-320:", json.dumps({k: c320[k] for k in
      ("maxR", "maxR_stored", "sigma_min", "sigma_min_stored",
       "sigma_rel_diff", "pass")}, default=str), flush=True)

c313 = control_stored_match("phase313", 0.0272, "313")
# Amended CTRL-313 sigma leg (registration amendment): the record's
# 0.0272 is Gate-34's value at Gate-34's OWN refit solution, with
# Gate-34's forward-difference FD. Evaluate it exactly there.
_g34 = json.load(open("gate34/results/g34_item3a.json"))
_th_g34 = np.array(_g34["N6_winner"]["theta"])
_tg313 = json.load(open("phase313/work/p313_targets.json"))
_XS313 = [np.array(s["point"]) for s in _tg313["sites"]]
_TH313 = [np.array(s["That"]) for s in _tg313["sites"]]
_FR313 = np.array([float(np.linalg.norm(t)) for t in _TH313])
_rv313 = make_resid(_XS313, _TH313, _FR313)
_f0 = _rv313(_th_g34, 6, 1.0)
_Jf = np.empty((40, len(_th_g34)))
for _j in range(len(_th_g34)):
    _h = 1e-6 * max(1.0, abs(_th_g34[_j]))
    _tp = _th_g34.copy(); _tp[_j] += _h
    _Jf[:, _j] = (_rv313(_tp, 6, 1.0) - _f0) / _h
_svf = np.linalg.svd(_Jf, compute_uv=False)
c313["sigma_min_gate34_theta_forwardFD"] = float(_svf[-1])
c313["sigma_max_gate34_theta_forwardFD"] = float(_svf[0])
c313["sigma_gate34_stored"] = 0.027165249637030254
c313["sigma_gate34_rel_diff"] = abs(float(_svf[-1])
                                    - 0.027165249637030254) \
    / 0.027165249637030254
c313["sigma_note"] = ("sigma_min is per-solution (G36-C): at 313's "
                      "stored solution this build reads "
                      f"{c313['sigma_min']:.6e}; the record's 0.0272 is "
                      "Gate-34's, at Gate-34's refit solution, "
                      "reproduced above.")
c313["pass"] = bool(c313["maxR"] <= 2 * c313["maxR_stored"]
                    and c313["maxR"] <= 1e-12
                    and c313["sigma_gate34_rel_diff"] <= 0.02)
OUT["CTRL313"] = c313
print("CTRL-313:", json.dumps({k: c313[k] for k in
      ("maxR", "maxR_stored", "sigma_min", "sigma_min_stored",
       "sigma_rel_diff", "pass")}, default=str), flush=True)

if not (c320["pass"] and c313["pass"]):
    OUT["aborted"] = "CONTROL BLOCKER: stored mating not reproduced"
    json.dump(OUT, open("phase410/results/p410_results.json", "w"),
              indent=1, default=str)
    raise SystemExit("CONTROL BLOCKER — see results json")

# =====================================================================
# CTRL-TGT-410 + ITEM 1 — the winner and its sites
# =====================================================================
st405 = json.load(open("phase405/results/p405_state.json"))
screens405 = [json.loads(l) for l in
              open("phase405/results/p405_screens.jsonl")]
by_id405 = {r['id']: r for r in screens405}
dC = [r for r in st405['D']['C']['curve']
      if abs(r['peak_target'] - L405.SS7_BAR) < 1e-12][0]
vS_win = np.array(by_id405[dC['screen_id']]['vS_scaled'], dtype=DTYPE)
K_WIN = 9

g50in = json.load(open("gate50/results/g50_stored_inputs.json"))
knots_gate = np.array(g50in["conf405"]["shapeC_knots_at_criterion"])
knot_diff = float(np.max(np.abs(vS_win - knots_gate)))

s_read, aux_read = L405.set_read405(vS_win, K_WIN)
joint_read = L405.joint_of_read(s_read)
ctrl_tgt = {
    "knot_max_diff_vs_gate50": knot_diff,
    "joint": joint_read, "joint_stored": 1.2273852081052888e-06,
    "joint_diff": abs(joint_read - 1.2273852081052888e-06),
    "sec_min": s_read["sec"]["min"],
    "sec_min_stored": -2.2135565049905559e-04,
    "sec_min_diff": abs(s_read["sec"]["min"] - (-2.2135565049905559e-04)),
}
# A1 cross-checks (frame-invariant deciding values at a Type-I point)
A1_POINT = np.array([-17.827002016737087, 0.1739363226225222,
                     1.8812104787714563])
nec_A1, typeI_A1, That_A1_pre = L405.nec_at405(vS_win, K_WIN, A1_POINT)
wn_A1 = L405.worst_null_at405(vS_win, K_WIN, A1_POINT)
ctrl_tgt.update({
    "nec_A1": nec_A1, "nec_A1_stored": 1.2273852081052888e-06,
    "nec_A1_diff": abs(nec_A1 - 1.2273852081052888e-06),
    "typeI_A1": bool(typeI_A1),
    "worst_null_A1": float(wn_A1[0]) if isinstance(wn_A1, (tuple, list))
                     else float(wn_A1),
    "worst_null_A1_stored": 7.282191364112375e-07,
})
ctrl_tgt["worst_null_A1_diff"] = abs(ctrl_tgt["worst_null_A1"]
                                    - 7.282191364112375e-07)
ctrl_tgt["pass"] = bool(knot_diff == 0.0
                        and ctrl_tgt["joint_diff"] <= 1e-12
                        and ctrl_tgt["sec_min_diff"] <= 1e-12
                        and ctrl_tgt["nec_A1_diff"] <= 1e-9
                        and ctrl_tgt["worst_null_A1_diff"] <= 1e-9)
OUT["CTRL_TGT410"] = ctrl_tgt
print("CTRL-TGT-410:", json.dumps(ctrl_tgt, default=str), flush=True)
if not ctrl_tgt["pass"]:
    OUT["aborted"] = "CTRL-TGT-410 BLOCKER: winner target not reproduced"
    json.dump(OUT, open("phase410/results/p410_results.json", "w"),
              indent=1, default=str)
    raise SystemExit("CTRL-TGT-410 BLOCKER — see results json")

# --- Sites -------------------------------------------------------------
R_A1 = 17.926829268292682
n1 = A1_POINT / R_A1
# A2: SEC argmin of the winner's own SET-244 read
Rsec = aux_read['R']['sec']
i_sec = int(np.argmin(Rsec))
ir_sec, id_sec = divmod(i_sec, 162)
A2_POINT = DIRS162[id_sec] * R_NODES[ir_sec]
R_A2 = float(R_NODES[ir_sec])
# A3: peak site on the x-axis phys row
A3_POINT = np.array([10.0, 0.0, 0.0])
# B: radial stencil along n1
STENCIL_R = [R_A1 + d for d in (-1.0, -0.5, 0.0, 0.5, 1.0)]


def That_at(pt):
    T, g = L405.T_at405(vS_win, K_WIN, np.asarray(pt, dtype=DTYPE)[None, :])
    return vm.eulerian_that(g, T)[0]


def site_record(key, pt):
    That = That_at(pt)
    pt = np.asarray(pt, dtype=DTYPE)
    r = float(np.linalg.norm(pt))
    n_star, nec_exact, nec_fib = L312.worst_null(That)
    kstar = np.concatenate([[1.0], np.asarray(n_star, dtype=DTYPE)])
    mm = margins_chunked(That[None, :, :])
    return {"key": key, "point": pt, "r": r, "That": That,
            "rho": float(That[0, 0]), "frob": float(np.linalg.norm(That)),
            "kstar": kstar, "nec_min_exact": float(nec_exact),
            "nec_fib": float(nec_fib),
            "samplerM": {k: float(mm[k][0]) for k in
                         ("nec", "wec", "dec", "sec")},
            "segre": segre(That)}


sitesA = [site_record("A1_joint_argmin", A1_POINT),
          site_record("A2_sec_argmin", A2_POINT),
          site_record("A3_peak", A3_POINT)]
sitesB = [site_record(f"B_stencil_{d:+.1f}", n1 * rr)
          for d, rr in zip((-1.0, -0.5, 0.0, 0.5, 1.0), STENCIL_R)]

targets_out = {"winner_vS": [float(x) for x in vS_win], "K": K_WIN,
               "sitesA": [], "sitesB": []}
for s in sitesA + sitesB:
    rec = {"key": s["key"], "point": s["point"].tolist(), "r": s["r"],
           "That": s["That"].tolist(), "rho": s["rho"], "frob": s["frob"],
           "kstar": s["kstar"].tolist(),
           "nec_min_exact": s["nec_min_exact"], "nec_fib": s["nec_fib"],
           "samplerM": s["samplerM"], "segre_type": s["segre"]["type"]}
    (targets_out["sitesA"] if s in sitesA else targets_out["sitesB"]).append(rec)
json.dump(targets_out, open("phase410/work/p410_targets.json", "w"), indent=1)
OUT["item1_sitesA"] = [{k: s[k] for k in ("key", "r", "rho", "frob",
                                          "nec_min_exact")}
                       for s in sitesA]
OUT["item1_sitesB"] = [{k: s[k] for k in ("key", "r", "rho", "frob",
                                          "nec_min_exact")}
                       for s in sitesB]
OUT["item1_A2"] = {"point": A2_POINT.tolist(), "r": R_A2,
                   "sec_min": s_read["sec"]["min"]}
json.dump(OUT, open("phase410/results/p410_results.json", "w"),
          indent=1, default=str)
print("ITEM 1 extraction persisted. A2 r =", R_A2, flush=True)


# =====================================================================
# ITEM 2 — the fits
# =====================================================================
def run_fit(sites, ladder, label):
    XS = [s["point"] for s in sites]
    THATS = [s["That"] for s in sites]
    FROBS = np.array([s["frob"] for s in sites])
    KSTARS = [s["kstar"] for s in sites]
    report = {}
    cands_by_N = {}
    for N, kind, max_nfev in ladder:
        if kind == "full":
            starts = [("warm", warm_theta(N, rng))]
            starts += [(f"rand{i}", rand_theta(N, 1.0, rng))
                       for i in range(8)]
        else:
            starts = [(f"rand{i}", rand_theta(N, 1.0, rng))
                      for i in range(6)]
        cands = run_fits(N, 1.0, XS, THATS, FROBS, KSTARS, starts,
                         max_nfev, f"{label} N{N}")
        cands_by_N[N] = cands
        b = cands[0]
        report[str(N)] = {
            "best_maxR": b["maxR"], "best_Rs": b["Rs"],
            "best_start": b["start"],
            "all_starts": [{"start": c["start"], "maxR": c["maxR"],
                            "Rs": c["Rs"], "nfev": c["nfev"]}
                           for c in cands]}
        json.dump({"N": N, "m": 1.0, "maxR": b["maxR"], "Rs": b["Rs"],
                   "tkks": b["tkks"], "rhos": b["rhos"], "start": b["start"],
                   "pvecs": b["pvecs"].tolist(),
                   "avecs": [[[float(z.real), float(z.imag)] for z in row]
                             for row in b["avecs"]]},
                  open(f"phase410/work/p410_{label}_best_N{N}.json", "w"),
                  indent=1)
        json.dump(OUT, open("phase410/results/p410_results.json", "w"),
                  indent=1, default=str)
    return cands_by_N, report, (XS, THATS, FROBS, KSTARS)


ladderA = [(4, "below", 900), (5, "below", 900), (6, "full", 900),
           (8, "full", 1300), (12, "full", 2000)]
candsA, reportA, packA = run_fit(sitesA, ladderA, "fitA")
OUT["fitA_arms"] = reportA

ladderB = [(6, "below", 1300), (8, "full", 1300), (12, "full", 2000)]
candsB, reportB, packB = run_fit(sitesB, ladderB, "fitB")
OUT["fitB_arms"] = reportB
json.dump(OUT, open("phase410/results/p410_results.json", "w"),
          indent=1, default=str)

# m=0 secondary — only if every m=1 arm of Fit A stalls > 1e-6
bestA_overall = min((candsA[N][0] for N in candsA), key=lambda c: c["maxR"])
m0_report = None
if bestA_overall["maxR"] > 1e-6:
    Nb = int(round((len(bestA_overall["theta"]) ) / 7))
    XS, THATS, FROBS, KSTARS = packA
    starts0 = [(f"rand{i}", rand_theta(Nb, 0.0, rng)) for i in range(5)]
    cands0 = run_fits(Nb, 0.0, XS, THATS, FROBS, KSTARS, starts0, 1300,
                      f"fitA N{Nb} m0")
    b0 = cands0[0]
    m0_report = {"N": Nb, "best_maxR": b0["maxR"], "best_Rs": b0["Rs"]}
    OUT["fitA_m0_secondary"] = m0_report
    print(f"m=0 secondary: best maxR={b0['maxR']:.3e}", flush=True)


def primary_of(cands_by_N, preferred):
    if preferred in cands_by_N and cands_by_N[preferred][0]["maxR"] <= 1e-9:
        return preferred, cands_by_N[preferred][0]
    bestN = min(cands_by_N, key=lambda N: cands_by_N[N][0]["maxR"])
    return bestN, cands_by_N[bestN][0]


primA_N, primA = primary_of(candsA, 6)
primB_N, primB = primary_of(candsB, 8)
OUT["primary"] = {"fitA_N": int(primA_N), "fitA_maxR": primA["maxR"],
                  "fitB_N": int(primB_N), "fitB_maxR": primB["maxR"]}
for lbl, prim, NN in (("fitA", primA, primA_N), ("fitB", primB, primB_N)):
    json.dump({"N": int(NN), "m": 1.0, "maxR": prim["maxR"],
               "Rs": prim["Rs"], "tkks": prim["tkks"], "rhos": prim["rhos"],
               "start": prim["start"], "pvecs": prim["pvecs"].tolist(),
               "avecs": [[[float(z.real), float(z.imag)] for z in row]
                         for row in prim["avecs"]]},
              open(f"phase410/work/p410_{lbl}_primary.json", "w"), indent=1)
print(f"PRIMARY fitA: N={primA_N} maxR={primA['maxR']:.3e}; "
      f"fitB: N={primB_N} maxR={primB['maxR']:.3e}", flush=True)


# =====================================================================
# Diagnostics per fit: D-a, Jacobian, perturbation ladder, pricing
# =====================================================================
def diagnostics(sites, packS, prim, N, label, pert_eps):
    XS, THATS, FROBS, KSTARS = packS
    ns = len(sites)
    bp, ba = prim["pvecs"], prim["avecs"]
    resid_vec = make_resid(XS, THATS, FROBS)
    diag = {}
    # direct-path verification
    Rs_d, tkks_d, rhos_d = site_residuals(bp, ba, 1.0, XS, THATS, KSTARS,
                                          direct=True)
    diag["direct"] = {"Rs": Rs_d, "maxR": max(Rs_d), "rhos": rhos_d,
                      "tkks": tkks_d}
    diag["dirac_max_residual"] = dirac_max_residual(bp, ba, 1.0)
    # D-a: per-site amplitude refits
    da = {}
    for si in range(ns):
        def resid_a(y, si=si):
            alpha = np.empty(N, dtype=complex)
            alpha[0] = y[0]
            alpha[1:] = y[1:N] + 1j * y[N:]
            av = alpha[:, None] * ba
            S = S_of(bp, av, 1.0)
            T = T_pairwise(S, bp, XS[si])
            d = T - THATS[si]
            return np.array([d[a, b] for a, b in IU]) / FROBS[si]
        y0 = np.concatenate([[1.0], np.ones(N - 1), np.zeros(N - 1)])
        sol = least_squares(resid_a, y0, method="trf", max_nfev=600)
        alpha = np.empty(N, dtype=complex)
        alpha[0] = sol.x[0]; alpha[1:] = sol.x[1:N] + 1j * sol.x[N:]
        S = S_of(bp, alpha[:, None] * ba, 1.0)
        T = T_pairwise(S, bp, XS[si])
        da[sites[si]["key"]] = {
            "R": float(np.linalg.norm(T - THATS[si])),
            "alpha": [[float(z.real), float(z.imag)] for z in alpha]}
    diag["D_a"] = {"per_site": da,
                   "all_close_1e-9": bool(all(v["R"] <= 1e-9
                                              for v in da.values()))}
    # pricing (Phase 320 pattern)
    a_norm2 = float(np.sum(np.abs(ba) ** 2))
    ba_unit = ba / np.sqrt(a_norm2)
    s2_sites = {}
    for si in range(ns):
        T_unit = T_direct(bp, ba_unit, 1.0, XS[si])
        tkk_unit = float(KSTARS[si] @ T_unit @ KSTARS[si])
        tkk_tgt = float(KSTARS[si] @ THATS[si] @ KSTARS[si])
        s2_sites[sites[si]["key"]] = {
            "s2_implied": abs(tkk_tgt) / abs(tkk_unit) if tkk_unit != 0
                          else None,
            "tkk_target": tkk_tgt, "tkk_unit": tkk_unit}
    diag["pricing"] = {"global_amplitude_scale_abs_a2": a_norm2,
                       "per_site_s2_implied": s2_sites}
    # structural Jacobian
    theta_d = pack(bp, ba)
    diag["jacobian"] = jacobian_report(resid_vec, theta_d, N, 1.0, ns)
    print(f"[{label}] JACOBIAN sigma_min={diag['jacobian']['sigma_min']:.4e} "
          f"rank={diag['jacobian']['rank_tol_1e-10_rel']}", flush=True)
    # perturbation ladder
    rng_p = np.random.default_rng(4102 if label == "fitA" else 4103)
    pert = {}
    for eps in pert_eps:
        rung = []
        for draw in range(2):
            thats_p, frobs_p = [], []
            for si in range(ns):
                U = rng_p.uniform(-1.0, 1.0, (4, 4))
                U = 0.5 * (U + U.T)
                thats_p.append(THATS[si] + eps * FROBS[si] * U)
                frobs_p.append(float(np.linalg.norm(thats_p[-1])))
            resid_p = make_resid(XS, thats_p, frobs_p)
            bestp = None
            for nm, th0 in [("warm", theta_d),
                            ("fresh", rand_theta(N, 1.0, rng_p))]:
                sol = least_squares(resid_p, th0, args=(N, 1.0),
                                    method="trf", max_nfev=900)
                pv2, av2 = unpack(sol.x, N)
                Rs_p, rhos_p = [], []
                for si in range(ns):
                    T = T_direct(pv2, av2, 1.0, XS[si])
                    Rs_p.append(float(np.linalg.norm(T - thats_p[si])))
                    rhos_p.append(float(T[0, 0]))
                cand = {"start": nm, "maxR_direct": max(Rs_p),
                        "Rs_direct": Rs_p, "rhos_fit": rhos_p,
                        "nfev": int(sol.nfev)}
                if bestp is None or cand["maxR_direct"] < bestp["maxR_direct"]:
                    bestp = cand
            bestp["rhos_target_perturbed"] = [float(t[0, 0]) for t in thats_p]
            rung.append(bestp)
            print(f"  [{label} pert eps={eps:.0e} draw={draw}] best maxR="
                  f"{bestp['maxR_direct']:.3e} ({bestp['start']})", flush=True)
        pert[str(eps)] = rung
    diag["perturbation_ladder"] = pert
    return diag


diagA = diagnostics(sitesA, packA, primA, primA_N, "fitA",
                    (1e-12, 1e-9, 1e-6, 1e-4))
OUT["fitA_diagnostics"] = diagA
json.dump(OUT, open("phase410/results/p410_results.json", "w"),
          indent=1, default=str)
diagB = diagnostics(sitesB, packB, primB, primB_N, "fitB", (1e-9, 1e-6))
OUT["fitB_diagnostics"] = diagB
json.dump(OUT, open("phase410/results/p410_results.json", "w"),
          indent=1, default=str)


# =====================================================================
# ITEM 3 — channel decomposition + the supplier's own accounting
# =====================================================================
def decompose(T, nhat):
    out = {}
    sg = segre(T)
    out["segre_type"] = sg["type"]
    mm = margins_chunked(T[None, :, :])
    out["samplerM"] = {k: float(mm[k][0]) for k in ("nec", "wec", "dec", "sec")}
    out["flux_norm"] = float(np.linalg.norm(T[0, 1:4]))
    out["rho"] = float(T[0, 0])
    out["components"] = {f"T{a}{b}": float(T[a, b]) for a, b in IU}
    if sg["type"] == "I":
        ev, evec = np.linalg.eig(ETA @ T)
        ev = ev.real; evec = evec.real
        # timelike eigenvector -> rho; others -> -p_i
        tl = None
        for idx in range(4):
            v = evec[:, idx]
            if float(v @ ETA @ v) > 1e-9 * float(v @ v):
                tl = idx
        if tl is not None:
            rho = float(ev[tl])
            ps = []
            for idx in range(4):
                if idx == tl:
                    continue
                v = evec[:, idx]
                align = abs(float(v[1:4] @ nhat)) / max(
                    float(np.linalg.norm(v[1:4])), 1e-300)
                ps.append({"p": float(-ev[idx]), "nhat_align": align})
            ir = int(np.argmax([p["nhat_align"] for p in ps]))
            p_r = ps[ir]["p"]
            p_ts = [ps[i]["p"] for i in range(3) if i != ir]
            chans = {"rho": rho, "p_r": p_r, "p_t": p_ts,
                     "NEC_r": rho + p_r,
                     "NEC_t": [rho + p for p in p_ts],
                     "WEC": rho,
                     "DEC_r": rho - abs(p_r),
                     "DEC_t": [rho - abs(p) for p in p_ts],
                     "DEC_flux": rho - out["flux_norm"],
                     "SEC_trace": rho + p_r + sum(p_ts),
                     "SEC_r": rho + p_r,
                     "SEC_t": [rho + p for p in p_ts]}
            out["channels"] = chans
            out["SEC_min_channel"] = float(min(
                chans["SEC_trace"], chans["SEC_r"], min(chans["SEC_t"])))
            out["joint_min_channel"] = float(min(
                chans["NEC_r"], min(chans["NEC_t"]), chans["WEC"],
                chans["DEC_r"], min(chans["DEC_t"]), chans["DEC_flux"]))
    return out


def decomposition_for(sites, prim):
    bp, ba = prim["pvecs"], prim["avecs"]
    per = {}
    for si, s in enumerate(sites):
        nhat = s["point"] / s["r"]
        Tsup = T_direct(bp, ba, 1.0, s["point"])
        d_req = decompose(s["That"], nhat)
        d_sup = decompose(Tsup, nhat)
        entry = {"r": s["r"], "req": d_req, "sup": d_sup,
                 "rho_sup": float(Tsup[0, 0]),
                 "rho_sup_sign": "positive" if Tsup[0, 0] > 0 else
                                 ("negative" if Tsup[0, 0] < 0 else "zero"),
                 "component_max_diff": float(np.max(np.abs(
                     Tsup - s["That"]))),
                 "R": float(np.linalg.norm(Tsup - s["That"]))}
        if "channels" in d_req and "channels" in d_sup:
            entry["channel_margin_diffs"] = {
                "NEC_r": d_sup["channels"]["NEC_r"] - d_req["channels"]["NEC_r"],
                "WEC": d_sup["channels"]["WEC"] - d_req["channels"]["WEC"],
                "SEC_trace": d_sup["channels"]["SEC_trace"]
                             - d_req["channels"]["SEC_trace"],
                "SEC_min": d_sup["SEC_min_channel"] - d_req["SEC_min_channel"],
                "joint_min": d_sup["joint_min_channel"]
                             - d_req["joint_min_channel"]}
        per[s["key"]] = entry
    return per


decompA = decomposition_for(sitesA, primA)
decompB = decomposition_for(sitesB, primB)
OUT["decomposition_fitA"] = decompA
OUT["decomposition_fitB"] = decompB
json.dump(OUT, open("phase410/results/p410_results.json", "w"),
          indent=1, default=str)
print("ITEM 3 decomposition persisted.", flush=True)

# =====================================================================
# VERDICT (registered forms, SS7)
# =====================================================================
BAR = 1e-9
fitA_ok = bool(diagA["direct"]["maxR"] <= BAR)
fitB_ok = bool(diagB["direct"]["maxR"] <= BAR)
jacA = diagA["jacobian"]
pertA_ok = all(r["maxR_direct"] <= BAR
               for rung in diagA["perturbation_ladder"].values()
               for r in rung)
if fitA_ok:
    verdict = "SUPPLIES AT THE SITES"
else:
    # V2 test: joint-channel margins agree within 1e-6 at every Fit A
    # site while the SEC channel disagrees by more than 1e-6.
    v2 = True
    for key, e in decompA.items():
        if "channel_margin_diffs" not in e:
            v2 = False
            break
        d = e["channel_margin_diffs"]
        if abs(d["joint_min"]) > 1e-6 or abs(d["SEC_min"]) <= 1e-6:
            v2 = False
    verdict = ("SUPPLIES THE JOINT CHANNELS BUT NOT SEC" if v2
               else "DOES NOT SUPPLY")
OUT["verdict"] = {
    "form": verdict,
    "fitA_direct_maxR": diagA["direct"]["maxR"], "fitA_ok": fitA_ok,
    "fitB_direct_maxR": diagB["direct"]["maxR"], "fitB_ok": fitB_ok,
    "fitA_jacobian_sigma_min": jacA["sigma_min"],
    "fitA_per_site_sigma_min": {sitesA[int(k)]["key"]: v["sigma_min"]
                                for k, v in
                                jacA["per_site_blocks"].items()},
    "fitB_jacobian_sigma_min": diagB["jacobian"]["sigma_min"],
    "fitB_per_site_sigma_min": {sitesB[int(k)]["key"]: v["sigma_min"]
                                for k, v in
                                diagB["jacobian"]["per_site_blocks"].items()},
    "perturbation_ladder_fitA_all_reclose": bool(pertA_ok),
    "gate_referral": bool(verdict == "SUPPLIES AT THE SITES"),
}
OUT["wall_time_s"] = time.time() - t_start
json.dump(OUT, open("phase410/results/p410_results.json", "w"),
          indent=1, default=str)
print("VERDICT:", verdict, flush=True)
print(f"wall {OUT['wall_time_s']:.0f}s", flush=True)
