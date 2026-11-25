"""GATE-12 checker: pass/fail over the gate's own result files only."""
import json
W = "/home/hatch/workspace/warp-pilot/gate12/results/"
le = json.load(open(W + "g12_le_numbers.json"))
en = json.load(open(W + "g12_endowed_numbers.json"))
fu = json.load(open(W + "g12_followups.json"))
rs = json.load(open(W + "g12_c_rescale.json"))
checks = []
def chk(name, ok, detail=""):
    checks.append({"name": name, "pass": bool(ok), "detail": str(detail)})

# G12-1 anchors
for k, v in le["anchors"].items():
    chk(f"anchor {k}", abs(v["diff"]) < 5e-7, v["diff"])
chk("anchors_pass flag", le["anchors_pass"])
d = le["deciding_audit_x0.7"]
chk("G12-1 closure FD audit < 2.0e-3 bar", d["closure_max_h_resid"] <= 2.0e-3, d["closure_max_h_resid"])
chk("G12-1 closure near phase FD 1.9891e-3 (5%)", abs(d["closure_max_h_resid"] / 1.9890869033112324e-3 - 1) < 0.05, d["closure_max_h_resid"])
chk("G12-1 zero non-finite rows of 221", d["n_nonfinite_rows"] == 0 and d["n_grid"] == 221, d["n_nonfinite_rows"])
chk("G12-1 Type-I everywhere", d["all_type_I_with_finiteness"])
chk("G12-1 worst DEC margin > 0, near phase +1.3460e-2 (5%)",
    d["worst_margin"] > 0 and abs(d["worst_margin"] / 1.3459808823127563e-2 - 1) < 0.05, d["worst_margin"])
chk("G12-1 fm_min > 0 near phase +4.288e-3 (5%)", d["fm_min"] > 0 and abs(d["fm_min"] / 4.287696086926001e-3 - 1) < 0.05, d["fm_min"])
chk("G12-1 sampled DEC at bind > 0", d["sampled_dec_at_bind"] > 0, d["sampled_dec_at_bind"])
chk("G12-1 ladder spread class 2.9e-4", d["ladder_spread"] < 6e-4, d["ladder_spread"])
a = le["audit_x0.7_fromA"]
chk("G12-1 from-A anatomy: exactly 1 non-finite row", a["n_nonfinite_rows"] == 1, a["n_nonfinite_rows"])
chk("G12-1 from-A fm dip near -5.69e-5 (20%)", abs(a["fm_min"] / -5.690805126665035e-5 - 1) < 0.2, a["fm_min"])
f = le["x0.5_floor_reads"]
chk("G12-1 x0.5 L8 floor closure reproduces 1.606e-2 (1%)",
    abs(f["x0.5_L8_fromZeros_best_feasible"]["closure_dense61"] / 1.6061428007274302e-2 - 1) < 0.01,
    f["x0.5_L8_fromZeros_best_feasible"]["closure_dense61"])
chk("G12-1 x0.5 L8 floor >> bar (still uncloseable)", f["x0.5_L8_fromZeros_best_feasible"]["closure_dense61"] > 8 * 2.0e-3)
chk("G12-1 x0.5 L6 floor reproduces 1.757e-2 (1%)",
    abs(f["x0.5_L6_fromZeros_best_feasible"]["closure_dense61"] / 1.757489916231357e-2 - 1) < 0.01,
    f["x0.5_L6_fromZeros_best_feasible"]["closure_dense61"])
fr = fu["frames_phase88_A_x0.5_lam0.14_L6"]
chk("G12-1 x0.5 A-set shared frame spacelike (F0 < 0)", fr["F0"]["margin"] < -0.5, fr["F0"]["margin"])
chk("G12-1 x0.5 A-set tilted frames all spacelike (F2,F3,F4 < 0)",
    all(fr[k]["margin"] < 0 for k in ("F2", "F3", "F4")))
chk("G12-1 x0.5 A-set pure-time frame at FD floor (|F1| < 1e-3)", abs(fr["F1"]["margin"]) < 1e-3, fr["F1"]["margin"])
fr7 = le["frames_x0.7_confirming_set"]
chk("G12-1 x0.7 confirming set: all five frames timelike", all(v["margin"] > 0 for v in fr7.values()),
    {k: v["margin"] for k, v in fr7.items()})

# G12-2
chk("G12-2 Ktt0 reproduces (1e-9)", abs(en["K_sympy"]["Ktt0"] / 4.436998542787459e-06 - 1) < 1e-9, en["K_sympy"]["Ktt0"])
chk("G12-2 Kth0 reproduces (1e-12)", abs(en["K_sympy"]["Kth0"] / 0.0009990018707114773 - 1) < 1e-12, en["K_sympy"]["Kth0"])
chk("G12-2 w0 reproduces (1e-9)", abs(en["admissibility"]["w0"] / 0.002220715832908041 - 1) < 1e-9, en["admissibility"]["w0"])
chk("G12-2 dust inadmissible (residual = -Ktt0 != 0)", abs(en["admissibility"]["dust_residual_over_sigma0"]) > 1e-7)
chk("G12-2 D_Rn reproduces (1e-6)", abs(en["strain"]["D_Rn"] / 1.8844230755847662e-05 - 1) < 1e-6, en["strain"]["D_Rn"])
chk("G12-2 strain ratio reproduces (1e-6)", abs(en["strain"]["ratio"] / 0.6177473545394297 - 1) < 1e-6, en["strain"]["ratio"])
chk("G12-2 phase-C spectrum reproduces at mp40 (sign +)",
    en["spectrum_mp40"]["sign_omega2_at_w0"] == "+" and abs(float(en["spectrum_mp40"]["omega2_at_w0"]) / 7.893779445769137e-10 - 1) < 1e-9,
    en["spectrum_mp40"]["omega2_at_w0"])
chk("G12-2 phase-C omega2(0) negative", float(en["spectrum_mp40"]["omega2_at_0"]) < 0, en["spectrum_mp40"]["omega2_at_0"])
chk("G12-2 threshold reproduces (1e-9)", abs(float(en["spectrum_mp40"]["threshold"]) / 0.0020611430310261847 - 1) < 1e-9,
    en["spectrum_mp40"]["threshold"])
# the C catch: trajectory + brute force
tin = en["C"]["trajectory_path"]["in"]; tex = en["C"]["trajectory_path"]["ex"]
chk("CATCH: trajectory C_in = sqrt(B) not sqrt(B)/A (5%)",
    abs(tin["C_slope"] / 1.0009991265459912 - 1) < 0.05 and abs(tin["C_slope"] / tin["C_formula"] - 1) > 0.3,
    tin["C_slope"])
chk("CATCH: rescaled proper-time omega2(w0) > 0 at 40 digits", float(rs["omega2_proper_at_w0"]) > 0, rs["omega2_proper_at_w0"])
chk("CATCH: rescaled proper-time omega2(0) < 0", float(rs["omega2_proper_at_0"]) < 0, rs["omega2_proper_at_0"])
chk("CATCH: rescale factor = C_phase/sqrt(B) ~ 0.80878", abs(float(rs["rescale_factor"]) / 0.8087789742548871 - 1) < 1e-9,
    rs["rescale_factor"])

npass = sum(c["pass"] for c in checks)
out = dict(checks=checks, n_pass=npass, n_total=len(checks), all_pass=npass == len(checks))
try:
    with open(W + "g12_check.json", "w") as fh:
        json.dump(out, fh, indent=1)
except PermissionError:
    print("CHECKJSON-BEGIN")
    print(json.dumps(out, indent=1))
    print("CHECKJSON-END")
for c in checks:
    print(("PASS " if c["pass"] else "FAIL ") + c["name"] + "  " + c["detail"])
print(f"{npass}/{len(checks)} PASS")
