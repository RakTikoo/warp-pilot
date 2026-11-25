# =====================================================================
# GATE-15 KERNEL 1 — W-B2 COMPLETION (source / functionals / solve /
# shell sign), packaged under the 2026-11-23 standing order (heavy
# compute off the VM; parent launches on Kaggle, one at a time).
#
# Self-contained: all gate data and gate modules are embedded above
# (zlib/base85) and materialised into ./g15_home/ at start. The carried
# modules are Gate-15's OWN W-B2 code (written from scratch for this
# gate; NOT phase code), with exactly one adaptation: the home
# absolute path prefix replaced by the local g15_home/ path (counts
# asserted at build time and recorded in BUILD_INFO).
#
# CONTROL GATES FIRST (porting standard S5): Stage 0 recomputes the
# channel functionals and asserts (i) they match the home checkpoint,
# (ii) the A1 member cross-check reproduces the CORRECTED member
# control [Rt_,n]_0 = -0.0152185839536870246 (the phase-stored value,
# vindicated by W-B2's A1 diagnosis: Gate-15's W-A control worker had
# used a wrong A''' jet for the interior exp(2 Phi_2); the diagnosis
# is re-run and asserted in Stage 0), (iii) the A2 truncation anchors
# reproduce Phase 90/91's stored values within their registered bars.
# A failed control aborts loudly and voids everything after it.
#
# AMENDMENT (2026-11-23, repair of the v1 launch failure — NOT a bar
# move; no deciding read's bar is touched): v1 aborted at Stage 0 on
# the single check "A1 jump_R == 0" (|jump_R| < 1e-12), reading
# jump_R = +3.3617694518376954105565534120486498773929070783924e-9.
# Diagnosis (home, closed-form read, 50- and 80-digit): that value is
# digit-for-digit the HOME stored value (wb2_functionals.json) — the
# port is faithful and the environment is exonerated. [R~] = 0 is
# exact for the exact member (Gate-9 G9-2), but the member as stored
# carries beta_MK rounded to 7 significant figures (2.142611); with
# d[R~]/dbeta_MK = 0.012000000000 the stored residual is exactly the
# rounding propagation 0.012 x (beta_stored - beta*) with
# beta* = 2.14261071985254568... (jump_R(beta*) = 2.7e-50) inside the
# stored constant's rounding interval. Phase 90's record already
# documents this exact read: "[R~]_0 control residual +3.36e-9 (the
# rounded stored beta, k)", the Phase-90/91 control floor 3.4e-9.
# The 1e-12 bar sat ~3400x below the stored member's own floor, so
# the check could never pass on ANY faithful evaluation. The check
# is repaired to (i) agreement with the home stored control at the
# sibling A1 standard (rel < 1e-9) AND (ii) |jump_R| <= 1e-8, a bound
# derived from the evaluation's own error scale: full rounding
# excursion of the stored constants is 0.012 x 5e-7 = 6e-9 < 1e-8,
# and 1e-8 remains >5 orders below every deciding scale in this
# gate (dissolution bar 1e-5 per unit eps; jump_Rn = 1.5e-2). Full
# record: gate15/STATUS.md addendum of 2026-11-23.
#
# Stages (each writes its JSON to ./g15_out/ as it lands and prints a
# verdict line; PROGRESS.json is updated per stage):
#   0 controls (functionals + A1 + A3 diagnosis + A2 anchors)
#   1 primary source recomputation + home-checkpoint agreement +
#     entering-order fits + confrontation vs Phase-122 literals
#   2 second path (200-point Gauss-Legendre, float64) + 5% agreement
#   3 response matrices from W-B1's settled basis jets; ranks; solves
#     in the full space AND the correctly classified (e) sets
#     (ell=1: 10 full / 6 (e)-quotient; ell=2,3: 8 (e)); residuals and
#     amplitudes vs the registered bars (residual <= 1e-5 per unit
#     eps^entering; amplitudes <= 1e2); numpy float64 and mpmath
#     40-digit arithmetics as two solver paths
#   4 shell sign on both mouths, both solves, corrected interior
#     control (and W-A's erroneous control, for the record), tail
#     bound from the kernel's own ell=4 extraction
#   5 checker: wb2_results.json + wb2_check.json (every comparison)
#
# In-kernel judgements are PROVISIONAL until re-judged at home in a
# fresh process (porting standard S5). INTERNAL only.
# (V-b) UNDECIDED: Pais-Uhlenbeck spin-2 ghost vs Mannheim
# PT-symmetric quantisation — opposed literature positions, B3 NOT
# COMPUTABLE (Phase 32). Carried, not decided.
# =====================================================================
import json, os, subprocess, sys, time
from math import factorial

T0 = time.time()
HOME_DIR = os.path.join(os.getcwd(), "g15_home")
OUT_DIR = os.path.join(os.getcwd(), "g15_out")
os.makedirs(HOME_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)

def dump(name, obj):
    with open(os.path.join(OUT_DIR, name), "w") as fh:
        json.dump(obj, fh, indent=1)
    log(f"wrote g15_out/{name}")

def progress(stage, status):
    p = {"stage": stage, "status": status, "elapsed_s": time.time() - T0}
    with open(os.path.join(OUT_DIR, "PROGRESS.json"), "w") as fh:
        json.dump(p, fh, indent=1)
    log(f"STAGE {stage}: {status}")

def run_module(fname):
    log(f"running carried module {fname} ...")
    r = subprocess.run([sys.executable, os.path.join(HOME_DIR, fname)],
                       capture_output=True, text=True, cwd=os.getcwd())
    tail = "\n".join((r.stdout or "").splitlines()[-6:])
    log(f"{fname} stdout tail:\n{tail}")
    if r.returncode != 0:
        log(f"{fname} STDERR tail:\n" + "\n".join((r.stderr or "").splitlines()[-12:]))
        raise SystemExit(f"CONTROL GATE FAILED: carried module {fname} exited {r.returncode}")

def rel(a, b):
    a = float(a); b = float(b)
    return abs(a - b) / max(abs(b), 1e-300)

CHECKS = []
def check(name, ok, detail):
    CHECKS.append({"name": name, "pass": bool(ok), "detail": str(detail)})
    log(f"CHECK {'PASS' if ok else 'FAIL'}: {name} — {detail}")

# ---------------------------------------------------------------------
# STAGE 0 — controls
# ---------------------------------------------------------------------
progress(0, "running")
run_module("wb2_functionals.py")
func_new = json.load(open(os.path.join(HOME_DIR, "wb2_functionals.json")))
func_home = FUNC_HOME  # embedded home checkpoint (dict)
for key in ("LK_U_U1_V", "LR_U_U1_U2_V_V1", "LRn_U_U1_U2_U3_V_V1_V2"):
    worst = max(rel(x, y) for x, y in zip(func_new[key], func_home[key]))
    check(f"functionals {key} match home checkpoint", worst < 1e-9, f"max rel diff {worst:.3e}")
# A1 corrected control
JUMP_RN_CONTROL = -0.0152185839536870246
S00_CONTROL = 0.0202914452715827
jr = float(func_new["A1"]["jump_Rn"]); s00 = float(func_new["A1"]["S00_over_alpha0"])
check("A1 jump_Rn == corrected member control", rel(jr, JUMP_RN_CONTROL) < 1e-9,
      f"fresh {jr:.16f} vs control {JUMP_RN_CONTROL}")
check("A1 S00/a0 == corrected member control", rel(s00, S00_CONTROL) < 1e-9,
      f"fresh {s00:.16f} vs control {S00_CONTROL}")
# Amended 2026-11-23 (see header AMENDMENT): the original exact-zero
# check (|jump_R| < 1e-12) was miscalibrated against the stored
# member's documented 3.4e-9 control floor (rounded stored beta_MK).
# Repaired form: home-control agreement at the sibling A1 standard
# AND the floor-derived bound |jump_R| <= 1e-8.
jr_R = float(func_new["A1"]["jump_R"]); jr_R_home = float(func_home["A1"]["jump_R"])
check("A1 jump_R == home control, within stored-member floor",
      rel(jr_R, jr_R_home) < 1e-9 and abs(jr_R) <= 1e-8,
      f"jump_R {func_new['A1']['jump_R']} vs home stored {func_home['A1']['jump_R']} "
      f"(floor 3.4e-9: rounded stored beta_MK; amended bound 1e-8)")
# A3 diagnosis (documents + corrects the W-A control error)
run_module("wb2_a1_patch.py")
func_diag = json.load(open(os.path.join(HOME_DIR, "wb2_functionals.json")))
diag = func_diag["A1_diagnosis"]
check("A3 diagnosis: true-A3 jump == A1 control",
      rel(diag["jump_Rn_with_true_A3"], JUMP_RN_CONTROL) < 1e-9,
      f"{diag['jump_Rn_with_true_A3']}")
check("A3 diagnosis: W-A-A3 jump reproduces W-A's erroneous value",
      rel(diag["jump_Rn_with_WA_A3"], -0.01531714654192940335) < 1e-5,
      f"{diag['jump_Rn_with_WA_A3']} vs W-A stated -0.01531714654192940335 "
      "(W-A's +0.0204228620559 shell value was a W-A machinery error; corrected control stands)")
# A2 truncation anchors (registered bars: 5% / 5% / 5% / 1%)
a2 = func_new["A2_truncation"]
b0 = float(a2["ell0"]["0.1"]["B_per"]); b1 = float(a2["ell1"]["0.1"]["B_per"])
b2v = float(a2["ell2"]["0.1"]["B_per"]); b3 = float(a2["ell3"]["0.1"]["B_per"])
for nm, v in (("ell0", b0), ("ell1", b1), ("ell2", b2v), ("ell3", b3)):
    check(f"A2 [B] c {nm} within 5% of 4.302e-3", rel(v, 4.302e-3) < 0.05, f"{v:.10e}")
check("A2 D3 [K]1 within 5%", rel(float(a2["ell1"]["0.1"]["K_per"]), -4.270543e-6) < 0.05,
      a2["ell1"]["0.1"]["K_per"])
check("A2 D3 [Rtn]1 within 5%", rel(float(a2["ell1"]["0.1"]["Rn_per"]), 5.514561e-5) < 0.05,
      a2["ell1"]["0.1"]["Rn_per"])
check("A2 [Rt]3 within 5%", rel(float(a2["ell3"]["0.1"]["R_per"]), 8.570444e-3) < 0.05,
      a2["ell3"]["0.1"]["R_per"])
sid = func_new["S_identity"]
check("A2 S identity S0=-2,S1=0,S2=0,S3=-2 within 1%",
      abs(float(sid["S0"]) + 2) < 0.02 and abs(float(sid["S1"])) < 0.02
      and abs(float(sid["S2"])) < 0.02 and abs(float(sid["S3"]) + 2) < 0.02,
      json.dumps(sid))
if not all(c["pass"] for c in CHECKS):
    dump("wb2_check.json", {"stage0_controls": CHECKS, "verdict": "CONTROL GATE FAILED — all later stages void"})
    raise SystemExit("CONTROL GATE FAILED at Stage 0 — see g15_out/wb2_check.json")
progress(0, "complete — all controls pass")

# ---------------------------------------------------------------------
# STAGE 1 — primary source: recompute, home agreement, fits, confront
# ---------------------------------------------------------------------
progress(1, "running")
run_module("wb2_source.py")
src_new = json.load(open(os.path.join(HOME_DIR, "wb2_source.json")))
src_home = SRC_HOME
# resolve eps keys by float value (decimal-string forms vary with dps)
def by_eps(modes_rec):
    return {float(k): v for k, v in modes_rec.items()}
SRCN = {l: by_eps(rec) for l, rec in src_new["modes"].items()}
SRCH = {l: by_eps(rec) for l, rec in src_home["modes"].items()}
worst = 0.0; worst_at = None
for l, modes in SRCH.items():
    for eps, rec in modes.items():
        for ch, val in rec["channels"].items():
            nv = float(SRCN[l][eps]["channels"][ch])
            r = rel(nv, val) if abs(float(val)) > 1e-25 else abs(nv - float(val))
            if r > worst: worst, worst_at = r, (l, eps, ch)
check("primary source matches home checkpoint (all modes/eps/channels)",
      worst < 1e-6, f"max rel diff {worst:.3e} at {worst_at}")

from mpmath import mp, mpf
mp.dps = 40
EPSF = [0.1, 1 / 30, 0.01, 0.003, 0.001]
EPS_MPF = [mpf("0.1"), mpf(1) / 30, mpf("0.01"), mpf("0.003"), mpf("0.001")]
CHANS = ["B", "K", "Rt", "Rtn", "hth", "kth"]

def fit_channel(l, ch, table):
    """Model: v(eps) = c_main eps^(l+1) + c_tail eps^l (tail only l>=2).
    Exact 2-param (or 1-param) least squares in mpmath over the 5 rows.
    `table` maps float(eps) -> record (SRCN[str(l)])."""
    vs = [mpf(table[e]["channels"][ch]) for e in EPSF]
    if l >= 2:
        A = [[EPS_MPF[i] ** (l + 1), EPS_MPF[i] ** l] for i in range(5)]
        # normal equations 2x2
        s11 = sum(A[i][0] ** 2 for i in range(5)); s12 = sum(A[i][0] * A[i][1] for i in range(5))
        s22 = sum(A[i][1] ** 2 for i in range(5))
        t1 = sum(A[i][0] * vs[i] for i in range(5)); t2 = sum(A[i][1] * vs[i] for i in range(5))
        det = s11 * s22 - s12 ** 2
        cm = (t1 * s22 - t2 * s12) / det; ct = (s11 * t2 - s12 * t1) / det
        resid = max(abs(vs[i] - (cm * A[i][0] + ct * A[i][1])) for i in range(5))
        return cm, ct, resid
    else:
        s11 = sum(EPS_MPF[i] ** (2 * (l + 1)) for i in range(5))
        t1 = sum(EPS_MPF[i] ** (l + 1) * vs[i] for i in range(5))
        cm = t1 / s11
        resid = max(abs(vs[i] - cm * EPS_MPF[i] ** (l + 1)) for i in range(5))
        return cm, mpf(0), resid

fits = {}
for l in (1, 2, 3, 4):
    fits[str(l)] = {}
    for ch in CHANS:
        cm, ct, resid = fit_channel(l, ch, SRCN[str(l)])
        fits[str(l)][ch] = {"main_per_eps^(l+1)": str(cm), "tail_per_eps^l": str(ct),
                            "fit_max_resid": str(resid)}
dump("wb2_source_fits.json", fits)
log("entering-order fits: " + "; ".join(
    f"l{l} {ch} main={fits[str(l)][ch]['main_per_eps^(l+1)'][:14]} tail={fits[str(l)][ch]['tail_per_eps^l'][:14]}"
    for l in (1, 2, 3) for ch in ("B", "Rtn", "Rt")))
# Confrontation vs Phase-122 full-system literals (P122-3 dipole data + P122-1)
PHASE_SRC = {
    ("1", "B"): 6.014537e-3, ("1", "K"): -4.254506e-6, ("1", "Rtn"): 1.622818e-3,
    ("1", "Rt"): 1.552938e-3, ("2", "Rt"): -1.213920e-4,
}
for (l, ch), pv in PHASE_SRC.items():
    gv = float(fits[l][ch]["main_per_eps^(l+1)"])
    check(f"source {ch} l={l} main coeff vs Phase-122 literal {pv:+.6e}",
          rel(gv, pv) < 0.05, f"gate {gv:+.10e} (rel diff {rel(gv, pv):.3e}, bar 5%)")
b2tail = float(fits["2"]["B"]["tail_per_eps^l"])
check("source [B]2 tail coeff vs Phase-122 extracted -1.268835e-5",
      rel(b2tail, -1.268835e-5) < 0.05, f"gate {b2tail:+.10e}")
FLOOR = 3.4e-9
for l, ch in (("1", "Rt"), ("2", "Rt")):
    gv = abs(float(fits[l][ch]["main_per_eps^(l+1)"]))
    check(f"blindness: [Rt] l={l} decided nonzero in full system",
          gv >= 1e3 * FLOOR, f"|coeff| {gv:.6e} vs 1e3*floor {1e3*FLOOR:.1e} — (t,r) identity does NOT extend")
progress(1, "complete")

# ---------------------------------------------------------------------
# STAGE 2 — second path (GL-200 float64) + agreement
# ---------------------------------------------------------------------
progress(2, "running")
run_module("wb2_second.py")
sec = json.load(open(os.path.join(HOME_DIR, "wb2_second.json")))
sec_fits = {}
for l in (1, 2, 3, 4):
    sec_fits[str(l)] = {}
    for ch in CHANS:
        # float version of the same fit
        import numpy as np
        vs = np.array([float(sec["modes"][str(l)][e][ch]) for e in
                       ["0.1", "0.03333333333333333", "0.01", "0.003", "0.001"]])
        ep = np.array([0.1, 1 / 30, 0.01, 0.003, 0.001])
        if l >= 2:
            A = np.stack([ep ** (l + 1), ep ** l], axis=1)
            coef, *_ = np.linalg.lstsq(A, vs, rcond=None)
            sec_fits[str(l)][ch] = {"main": float(coef[0]), "tail": float(coef[1])}
        else:
            A = ep ** (l + 1)
            sec_fits[str(l)][ch] = {"main": float(np.sum(A * vs) / np.sum(A * A)), "tail": 0.0}
agree = {}
for l in ("1", "2", "3"):
    for ch in CHANS:
        gv = float(fits[l][ch]["main_per_eps^(l+1)"])
        sv = sec_fits[l][ch]["main"]
        agree[f"l{l}_{ch}"] = rel(sv, gv) if abs(gv) > 1e-12 else abs(sv - gv)
worst_agree = max(agree.values())
check("second path (GL-200) source agreement within 5% on deciding coefficients",
      worst_agree < 0.05, f"max rel diff {worst_agree:.3e}")
dump("wb2_second_fits.json", {"second_path_fits": sec_fits, "agreement_vs_primary": agree})
progress(2, "complete")

# ---------------------------------------------------------------------
# STAGE 3 — response matrices + solves (the deciding computation)
# ---------------------------------------------------------------------
progress(3, "running")
import numpy as np
LK = [mpf(x) for x in func_new["LK_U_U1_V"]]
LR = [mpf(x) for x in func_new["LR_U_U1_U2_V_V1"]]
LRn = [mpf(x) for x in func_new["LRn_U_U1_U2_U3_V_V1_V2"]]
Bm0 = mpf(func_new["background"]["Bm0"]); rS = mpf(1000)

def resp_vec(jet):
    U, U1, U2, U3 = (mpf(jet["U"]), mpf(jet["Uprime"]), mpf(jet["Upp"]), mpf(jet["Uppp"]))
    V, V1, V2 = mpf(jet["V"]), mpf(jet["Vprime"]), mpf(jet["Vpp"])
    Th, Th1 = mpf(jet["Theta"]), mpf(jet["Thetaprime"])
    return [V,
            LK[0] * U + LK[1] * U1 + LK[2] * V,
            LR[0] * U + LR[1] * U1 + LR[2] * U2 + LR[3] * V + LR[4] * V1,
            LRn[0] * U + LRn[1] * U1 + LRn[2] * U2 + LRn[3] * U3 + LRn[4] * V + LRn[5] * V1 + LRn[6] * V2,
            Th,
            Th1 / (2 * mp.sqrt(Bm0)) - V / (2 * rS * Bm0 ** mpf("1.5"))]

basis = BASIS_JETS["modes"]
SETS = {
    "ell1_full10": ("ell1", basis["ell1"]["gauge_basis_class_a"] + basis["ell1"]["e_basis"]),
    "ell1_e6": ("ell1", basis["ell1"]["e_basis"]),
    "ell2_e8": ("ell2", basis["ell2"]["e_basis"]),
    "ell3_e8": ("ell3", basis["ell3"]["e_basis"]),
}
solve_out = {}
for set_name, (ellkey, elems) in SETS.items():
    l = int(ellkey[3:])
    R = [[resp_vec(e["jet_at_Sigma"])[ch] for e in elems] for ch in range(6)]  # 6 x n mpmath
    Rf = np.array([[float(x) for x in row] for row in R])
    sv = np.linalg.svd(Rf, compute_uv=False)
    rank = int(np.sum(sv > 1e-8 * sv[0])) if sv[0] > 0 else 0
    entry = {"n_elems": len(elems), "rank": rank,
             "svals": [float(x) for x in sv], "solves": {}}
    for power, fitkey in (("main", "main_per_eps^(l+1)"), ("tail", "tail_per_eps^l")):
        if power == "tail" and l < 2:
            continue
        s = [mpf(fits[str(l)][ch][fitkey]) for ch in CHANS]
        # numpy path
        af, *_ = np.linalg.lstsq(Rf, np.array([float(x) for x in s]), rcond=None)
        resid_f = np.array([float(x) for x in s]) - Rf @ af
        # mpmath path: Moore-Penrose pseudoinverse (minimum-norm solve;
        # the residual is the unique projection residual even when the
        # system is underdetermined, e.g. 8 directions of rank 6)
        n = len(elems)
        try:
            a_mp = list(mp.pinv(mp.matrix(R)) * mp.matrix(s))
            resid_mp = [s[ch] - sum(R[ch][j] * a_mp[j] for j in range(n)) for ch in range(6)]
            amp_mp = max(abs(x) for x in a_mp)
        except Exception as exc:
            a_mp, resid_mp, amp_mp = None, None, None
            log(f"{set_name} {power}: mpmath solve failed: {exc}")
        entry["solves"][power] = {
            "source_vector": [str(x) for x in s],
            "numpy": {"amplitudes": [float(x) for x in af],
                      "max_abs_amplitude": float(np.max(np.abs(af))),
                      "residuals": [float(x) for x in resid_f],
                      "max_abs_residual": float(np.max(np.abs(resid_f)))},
            "mpmath": ({"amplitudes": [str(x) for x in a_mp],
                        "max_abs_amplitude": str(amp_mp),
                        "residuals": [str(x) for x in resid_mp],
                        "max_abs_residual": str(max(abs(x) for x in resid_mp))} if a_mp is not None else None),
        }
        log(f"{set_name} {power}: rank {rank}; numpy max|resid| "
            f"{entry['solves'][power]['numpy']['max_abs_residual']:.3e}, max|amp| "
            f"{entry['solves'][power]['numpy']['max_abs_amplitude']:.3e}")
    solve_out[set_name] = entry
    check(f"response rank {set_name} == 6 (full)", rank == 6, f"rank {rank}, svals {[f'{x:.2e}' for x in sv]}")
dump("wb2_solve.json", solve_out)
BAR_RESID, BAR_AMP = 1e-5, 1e2
for set_name in ("ell1_e6", "ell2_e8", "ell3_e8"):
    for power, sv_ in solve_out[set_name]["solves"].items():
        mr = sv_["numpy"]["max_abs_residual"]; ma = sv_["numpy"]["max_abs_amplitude"]
        check(f"CLOSE ({set_name}, {power}): residual <= 1e-5 and amplitudes <= 1e2",
              mr <= BAR_RESID and ma <= BAR_AMP, f"max|resid| {mr:.3e}, max|amp| {ma:.3e}")
for power, sv_ in solve_out["ell1_full10"]["solves"].items():
    mr = sv_["numpy"]["max_abs_residual"]
    log(f"ell1 full-10 {power} max|resid| {mr:.3e} (comparison record vs (e)-quotient)")
progress(3, "complete")

# ---------------------------------------------------------------------
# STAGE 4 — shell sign
# ---------------------------------------------------------------------
progress(4, "running")
def Ple(l, mu):
    if l == 0: return 1.0
    if l == 1: return mu
    if l == 2: return (3 * mu * mu - 1) / 2
    if l == 3: return (5 * mu ** 3 - 3 * mu) / 2

def rtn_resid(set_name, power):
    sv_ = solve_out[set_name]["solves"].get(power)
    return float(sv_["numpy"]["residuals"][3]) if sv_ else 0.0  # channel idx 3 = Rtn

EPS_ROWS = [0.1, 1 / 30, 0.01]
mus = [(-1.0 + 2.0 * i / 400) for i in range(401)]
# ell=4 tail bound from the kernel's own source extraction (raw values)
tail_bound = {e: 2.0 * abs(float(SRCN["4"][e]["channels"]["Rtn"])) for e in EPS_ROWS}
shell = {}
for label, jump0, setmap in (
    ("corrected_gate_control", JUMP_RN_CONTROL, {"1": "ell1_e6", "2": "ell2_e8", "3": "ell3_e8"}),
    ("corrected_gate_control_full10_L1", JUMP_RN_CONTROL, {"1": "ell1_full10", "2": "ell2_e8", "3": "ell3_e8"}),
    ("WA_erroneous_control_for_record", -0.01531714654192940335, {"1": "ell1_e6", "2": "ell2_e8", "3": "ell3_e8"}),
):
    shell[label] = {}
    for eps in EPS_ROWS:
        for mouth in ("A", "B"):
            vals = []
            for mu in mus:
                tot = jump0
                for l in (1, 2, 3):
                    sgn = 1.0 if (mouth == "A" or l % 2 == 0) else -1.0
                    tot += sgn * rtn_resid(setmap[str(l)], "main") * eps ** (l + 1) * Ple(l, mu)
                    if l >= 2:
                        tot += sgn * rtn_resid(setmap[str(l)], "tail") * eps ** l * Ple(l, mu)
                vals.append(-(4.0 / 3.0) * tot)
            mn = min(vals)
            shell[label][f"eps={eps}"] = shell[label].get(f"eps={eps}", {})
            shell[label][f"eps={eps}"][mouth] = {
                "min_S00_over_alpha0": mn,
                "min_minus_tail_bound": mn - (4.0 / 3.0) * tail_bound[eps],
                "tail_bound_on_Rtn": tail_bound[eps]}
    log(f"shell {label}: " + "; ".join(
        f"eps={e} A {shell[label][f'eps={e}']['A']['min_S00_over_alpha0']:.10f} "
        f"B {shell[label][f'eps={e}']['B']['min_S00_over_alpha0']:.10f}" for e in EPS_ROWS))
dump("wb2_shell.json", shell)
prim = shell["corrected_gate_control"]
for e in EPS_ROWS:
    for mouth in ("A", "B"):
        check(f"shell sign > 0 (corrected control, eps={e}, mouth {mouth})",
              prim[f"eps={e}"][mouth]["min_minus_tail_bound"] > 0,
              f"min {prim[f'eps={e}'][mouth]['min_S00_over_alpha0']:.10f}, "
              f"after tail bound {prim[f'eps={e}'][mouth]['min_minus_tail_bound']:.10f}")
mn01 = min(prim[f"eps={e}"][m]["min_S00_over_alpha0"] for e in EPS_ROWS for m in ("A", "B"))
check("shell minimum vs Phase-122 claimed +0.0202914453 (5% confrontation)",
      rel(mn01, 0.0202914453) < 0.05, f"gate min {mn01:.10f}")
log(f"tail bounds on [Rt_,n] by eps: {tail_bound} — Phase-122 stored-table bound 2.06e-6 at eps=0.1; "
    f"Phase-133 corrected total 2.459e-6 (gate's own ell=4 extraction gives {tail_bound[0.1]:.4e})")
progress(4, "complete")

# ---------------------------------------------------------------------
# STAGE 5 — checker assembly
# ---------------------------------------------------------------------
progress(5, "running")
results = {
    "kernel": "g15_wb2_kernel", "build_info": BUILD_INFO,
    "controls_stage0": "see wb2_check.json",
    "source_fits": fits, "second_path_fits": sec_fits,
    "second_path_agreement": agree, "solve": solve_out, "shell": shell,
    "tail_bound": {str(k): v for k, v in tail_bound.items()},
    "note": "In-kernel judgements provisional until re-judged at home in a fresh process.",
}
dump("wb2_results.json", results)
npass = sum(1 for c in CHECKS if c["pass"]); nfail = len(CHECKS) - npass
dump("wb2_check.json", {"checks": CHECKS, "n_pass": npass, "n_fail": nfail,
                        "verdict": f"{npass}/{len(CHECKS)} PASS"})
log(f"CHECKER: {npass}/{len(CHECKS)} PASS")
progress(5, "complete — kernel 1 finished")
print("G15_WB2_KERNEL_DONE", flush=True)
