"""GATE-12 runner for G12-1. Anchors FIRST (a failed anchor stops the
run as a machinery failure); then the deciding audit of the stored
confirming set; then the (0.5, 0.14) open-clause reads (constrained
floor sets' closure + frame margins; alternative-frame probe on the
degenerate strategy-A set and on the confirming set as control).
All machinery is gate12/g12_le.py (fresh). Coefficient sets and
anchor targets are imported as DATA only."""
import json, time
import numpy as np
import g12_le as G

W = "/home/hatch/workspace/warp-pilot/"
OUT = W + "gate12/results/g12_le_numbers.json"
out = {"machinery": "gate12/g12_le.py fresh numpy FD auditor (no phase imports)",
       "venv": "~/workspace/warp-pilot/venv/bin/python"}
def save():
    json.dump(out, open(OUT, "w"), indent=1)

t00 = time.time()
# ---------------------------------------------------------------- anchors
anchors = {}
regate = json.load(open(W + "phase96/results/p961_regate.json"))
for x, lam, key in [(0.1, 0.19, "dipole_pole_x0.1"), (0.3, 0.19, "dipole_pole_x0.3")]:
    dof = regate[key]["dof"]
    p = np.zeros(5)
    p[0] = dof["rho1"]; p[1] = dof["At1"]; p[2] = dof["w1"]
    r = G.sample(x, lam, p, 1, np.array([np.pi]), h=0.01)
    s = G.lanczos(r["KP"][0], r["KM"][0])
    m, t = G.phi_HE(*s)
    anchors[key] = dict(margin=float(m), type=int(t), target=regate[key]["target"],
                        diff=float(m - regate[key]["target"]))
    print(f"anchor {key}: {m:+.8e} target {regate[key]['target']:+.4e} diff {m-regate[key]['target']:+.2e}", flush=True)
solve80 = json.load(open(W + "phase80/results/p801_solve.json"))
for key, th, name in [("x0.1_lam0.19_L6", np.pi, "x0.1_L6_rear_pole"),
                      ("x0.3_lam0.19_L6", 0.0, "x0.3_L6_front_pole")]:
    rec = solve80[key]
    r = G.sample(rec["x"], rec["lam"], np.array(rec["p"]), rec["L"], np.array([th]), h=0.01)
    s = G.lanczos(r["KP"][0], r["KM"][0])
    m, t = G.phi_HE(*s)
    anchors[name] = dict(margin=float(m), type=int(t), target=regate[name]["target"],
                         diff=float(m - regate[name]["target"]))
    print(f"anchor {name}: {m:+.8e} target {regate[name]['target']:+.4e} diff {m-regate[name]['target']:+.2e}", flush=True)
anchors_pass = all(abs(v["diff"]) < 5e-7 for v in anchors.values())
out["anchors"] = anchors; out["anchors_pass"] = bool(anchors_pass); save()
print("ANCHORS", "PASS" if anchors_pass else "FAIL", flush=True)
if not anchors_pass:
    raise SystemExit("anchor failure = machinery failure, stop")

# ---------------------------------------------------------------- deciding audit
solve96 = json.load(open(W + "phase96/results/p961_solve.json"))
audit96 = json.load(open(W + "phase96/results/p961_audit.json"))

def full_audit(rec, tag):
    grid = G.audit_grid()
    r = G.sample(rec["x"], rec["lam"], np.array(rec["p"]), rec["L"], grid, h=0.01)
    dh = r["hP"] - r["hM"]
    resid = np.max(np.abs(dh[:, [0, 0, 1], [0, 1, 1]]))   # [tt, tth, thth] of record
    rows = []
    worst = np.inf; ibind = None; allI = True; n_nonfinite = 0
    min_disc = np.inf; min_eig = np.inf
    for i, th in enumerate(grid):
        s = G.lanczos(r["KP"][i], r["KM"][i])
        finite = bool(np.all(np.isfinite(s)))
        if not finite:
            n_nonfinite += 1
        m, t = G.phi_HE(*s)
        em, disc = G.eig_margins(*s)
        allI = allI and (t == 1)
        if np.isfinite(disc):
            min_disc = min(min_disc, disc)
        if np.isfinite(em):
            min_eig = min(min_eig, em)
        if np.isfinite(m) and m < worst:
            worst, ibind = m, i
        rows.append((float(th), s, float(m), int(t), finite))
    th_bind = float(grid[ibind]); s_bind = rows[ibind][1]
    samp = G.sampled_dec_min(*s_bind, n=2000, seed=12)
    ladder = {}
    for h, order in [(0.02, 2), (0.01, 2), (0.005, 2), (0.01, 4)]:
        rr = G.sample(rec["x"], rec["lam"], np.array(rec["p"]), rec["L"],
                      np.array([th_bind]), h=h, order=order)
        ss = G.lanczos(rr["KP"][0], rr["KM"][0])
        mm, tt = G.phi_HE(*ss)
        ladder[f"h{h}_o{order}"] = dict(margin=float(mm), type=int(tt))
    lm = [v["margin"] for v in ladder.values()]
    fm = np.minimum(-r["hP"][:, 0, 0], -r["hM"][:, 0, 0])
    res = dict(tag=tag, n_grid=int(len(grid)), closure_max_h_resid=float(resid),
               closure_max_h_full3x3=float(np.max(np.abs(dh))),
               worst_margin=float(worst), theta_bind=th_bind,
               n_nonfinite_rows=int(n_nonfinite),
               all_type_I=bool(allI), all_type_I_with_finiteness=bool(allI and n_nonfinite == 0),
               min_disc=float(min_disc), min_eig_margin=float(min_eig),
               fm_min=float(np.min(fm)), fm_theta_at_min=float(grid[int(np.argmin(fm))]),
               rear_pole_margin=rows[-1][2], rear_pole_type=rows[-1][3],
               front_pole_margin=rows[0][2], front_pole_type=rows[0][3],
               sampled_dec_at_bind=float(samp), ladder=ladder,
               ladder_spread=float(max(lm) - min(lm)))
    print(f"AUDIT {tag}: closure={resid:.6e} worst={worst:+.6e} at {th_bind:.4f} "
          f"nonfinite={n_nonfinite} TypeI={allI} fm_min={res['fm_min']:+.4e} "
          f"samp={samp:+.4e} ladder_spread={res['ladder_spread']:.2e}", flush=True)
    return res

rec = solve96["x0.7_L6_fromZeros"]
dec = full_audit(rec, "x0.7_L6_fromZeros")
dec["phase96_stored"] = audit96["x0.7_L6_fromZeros"]
out["deciding_audit_x0.7"] = dec; save()

# corroborating anatomy: the from-A set at the same pin (phase: 1 non-finite row)
recA = solve96["x0.7_L6_fromA"]
decA = full_audit(recA, "x0.7_L6_fromA")
decA["phase96_stored"] = audit96["x0.7_L6_fromA"]
out["audit_x0.7_fromA"] = decA; save()

# ---------------------------------------------------------------- (0.5) open clause
DENSE61 = np.linspace(0.12, np.pi - 0.12, 61)
def closure_honly(x, lam, p, L, thetas):
    best = 0.0; fm_min = np.inf
    for th in thetas:
        cvec, Rt, (At_e, w_e), (At_i, w_i) = G.frame_values(x, lam, p, L, th)
        a = lam / G.R0; M = x * G.R0 / 2.0
        Xp = G.exterior_point(a, M, th, Rt)
        Xm = np.array([0.0, Rt * np.cos(th), Rt * np.sin(th), 0.0])
        hP, _ = G.induced_and_K(lambda Y: G.metric_ext(Y, a, M), lambda Y: G.areal_ext(Y, a),
                                cvec, Xp, th, At_e, w_e, need_K=False)
        hM, _ = G.induced_and_K(lambda Y: G.metric_int(Y, a), G.areal_int,
                                cvec, Xm, th, At_i, w_i, need_K=False)
        dh = hP - hM
        best = max(best, float(np.max(np.abs(dh[[0, 0, 1], [0, 1, 1]]))))
        fm_min = min(fm_min, float(min(-hP[0, 0], -hM[0, 0])))
    return float(best), float(fm_min)

floor = {}
ck8 = json.load(open(W + "phase96/results/p961_ckpt_x0.5_L8_fromZeros.json"))
p8 = np.array(ck8["best_feasible"]["p"])
c8, f8 = closure_honly(0.5, 0.14, p8, 8, DENSE61)
floor["x0.5_L8_fromZeros_best_feasible"] = dict(closure_dense61=c8, fm_min_dense61=f8,
                                                phase96_value=ck8["best_feasible"]["max_h_dense61"])
print(f"x0.5 L8 floor set: closure={c8:.6e} (phase {ck8['best_feasible']['max_h_dense61']:.6e}) fm_min={f8:+.3e}", flush=True)
rec5 = solve96["x0.5_L6_fromZeros"]
# p961_solve stores the FINAL iterate for fromZeros; the best-feasible iterate is in its ckpt
ck6 = json.load(open(W + "phase96/results/p961_ckpt_x0.5_L6_fromZeros.json"))
p6 = np.array(ck6["best_feasible"]["p"])
c6, f6 = closure_honly(0.5, 0.14, p6, 6, DENSE61)
floor["x0.5_L6_fromZeros_best_feasible"] = dict(closure_dense61=c6, fm_min_dense61=f6,
                                                phase96_value=ck6["best_feasible"]["max_h_dense61"])
print(f"x0.5 L6 floor set: closure={c6:.6e} (phase {ck6['best_feasible']['max_h_dense61']:.6e}) fm_min={f6:+.3e}", flush=True)
out["x0.5_floor_reads"] = floor; save()

# alternative frames on the degenerate A set (x=0.5) + confirming set control (x=0.7)
GRID57 = np.linspace(0.05, np.pi - 0.05, 57)
recA5 = solve96["x0.5_L6_fromA"]
fr5 = G.frame_margins(0.5, 0.14, np.array(recA5["p"]), 6, GRID57)
print("frames x0.5 A set:", {k: round(v["margin"], 6) for k, v in fr5.items()}, flush=True)
fr7 = G.frame_margins(0.7, 0.09, np.array(rec["p"]), 6, GRID57)
print("frames x0.7 confirming set:", {k: round(v["margin"], 6) for k, v in fr7.items()}, flush=True)
out["frames_x0.5_A_set"] = fr5
out["frames_x0.7_confirming_set"] = fr7
out["seconds"] = time.time() - t00
save()
print("G12-LE DONE", out["seconds"], flush=True)
