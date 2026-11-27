"""
g53_laptop.py — Gate-53 laptop admission control. Runs on the
laptop pool (~/work/venv, numpy 2.5.5 / scipy 1.18.1 — the frame
of record) with the gate's own builder + the wa instrument:
chain reads for A-6 and RW-5, and the wa audit of A-6 at
beta = 0.193359375, h = 0.0375, on the registered set. The
parent compares the deciding digits against the VM gate reads;
admission = agreement at the 1e-9 level or better on the
deciding margins. Usage: python g53_laptop.py vectors.json
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/spark/work/g53")
import g53_lib as G
from g53_lib import GradedBuilder, audit_chunked, summarise, \
    pts_1020_control, DTYPE
import wa_auditor as wa

vecs = json.load(open(sys.argv[1]))
out = {}
t0 = time.time()
for name, nc in (("A-6", 16), ("RW-5", 12)):
    b = GradedBuilder(np.array(vecs[name], dtype=DTYPE), n_c=nc)
    out[name] = {"chain_reads": b.chain_reads()}
    print(name, "chain done", time.time() - t0, flush=True)
    if name == "A-6":
        pts, radp = pts_1020_control()
        gf = b.metric_factory(0.193359375)
        m = audit_chunked(gf, pts, 0.0375, wa.audit)
        s = summarise(m, pts, radp)
        al = s["all_sig"]
        out[name]["wa_h0.0375_beta0.193359375"] = {
            "worst": al["worst"], "worst_kind": al["worst_kind"],
            "worst_r": al[al["worst_kind"] + "_r"],
            "per_ec": {k: al[k] for k in ("nec", "wec", "sec", "dec")},
            "typeI_frac": al["typeI_frac"],
            "sampled_nec_min": al["sampled_nec_min"],
            "floor_proxy": s["floor_proxy_nonsig_median_abs_nec"],
        }
        print("A-6 wa:", out[name]["wa_h0.0375_beta0.193359375"], flush=True)
out["wall_s"] = time.time() - t0
json.dump(out, open("/home/spark/work/g53/g53_laptop_out.json", "w"), indent=1)
print("LAPTOP DONE")
