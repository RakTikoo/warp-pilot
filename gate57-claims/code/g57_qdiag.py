"""
g57_qdiag.py — DIAGNOSTIC ONLY (not a deciding read): why does the
gate's q_max for B-4 (0.995342, p417 geometry) differ from the
phase's stored 0.997179 (p416 geometry)? Compares the wa tensor
That at the r = 19.75 and r = 23.0 shells between the two geometry
organisations, and the per-point q values from the identical
q formula. Writes gate57/results/g57_qdiag.json.
"""
import json, sys
import numpy as np

WP = "/home/hatch/workspace/warp-pilot"
sys.path.insert(0, f"{WP}/phase417/work")
import p417_lib as P
from p417_lib import GradedBuilder as GB417, DIRS26, DIRS162, DTYPE
import wa_auditor as wa

v416 = json.load(open(f"{WP}/phase416/results/p416_verdicts.json"))
y = np.array(v416["subjects"]["B-4"]["y"], dtype=DTYPE)
BETA = 0.194140625


def q_of(That):
    T00 = That[:, 0, 0]; T0i = That[:, 0, 1:]; Tij = That[:, 1:, 1:]
    quad = np.einsum('njk,ij,ik->ni', Tij, DIRS162, DIRS162)
    vals = T00[:, None] + 2.0 * (T0i @ DIRS162.T) + quad
    jmin = np.argmin(vals, axis=1)
    nmin = DIRS162[jmin]
    T0n = np.einsum('ij,ij->i', T0i, nmin)
    Tnn = np.einsum('ij,ijk,ik->i', nmin, Tij, nmin)
    denom = T00 + Tnn
    return np.where(denom > 0,
                    2.0 * np.abs(T0n) / np.maximum(denom, 1e-300), np.inf)


out = {}
gf417 = GB417(y, n_c=16).metric_factory(BETA)
for r in (19.75, 23.0):
    pts = (DIRS26 * r).astype(DTYPE)
    m417 = wa.audit(gf417, pts, 0.0375)
    out[f"r{r}"] = {"p417_q": [float(x) for x in q_of(m417["That"])],
                    "p417_q_max": float(np.max(q_of(m417["That"]))),
                    "p417_That": m417["That"].tolist()}
    print("p417 r", r, "q_max", out[f"r{r}"]["p417_q_max"], flush=True)

# phase geometry, diagnostic only
sys.path.insert(0, f"{WP}/phase416/work")
import p416_lib16 as L16
gf416 = L16.GradedProcaccia16(y).metric_factory(BETA)
for r in (19.75, 23.0):
    pts = (DIRS26 * r).astype(DTYPE)
    m416 = wa.audit(gf416, pts, 0.0375)
    q416 = q_of(m416["That"])
    T417 = np.array(out[f"r{r}"]["p417_That"])
    dT = np.abs(m416["That"] - T417)
    denom = np.maximum(np.abs(T417), 1e-300)
    out[f"r{r}"].update({
        "p416_q": [float(x) for x in q416],
        "p416_q_max": float(np.max(q416)),
        "That_max_abs_diff": float(np.max(dT)),
        "That_max_rel_diff_sig": float(np.max(dT / denom)),
        "argmax_dir_idx_p416": int(np.argmax(q416)),
        "argmax_dir_idx_p417": int(np.argmax(out[f"r{r}"]["p417_q"]))})
    print("p416 r", r, "q_max", out[f"r{r}"]["p416_q_max"],
          "That max abs diff", out[f"r{r}"]["That_max_abs_diff"], flush=True)

json.dump(out, open(f"{WP}/gate57/results/g57_qdiag.json", "w"), indent=1)
print("DIAG DONE")
