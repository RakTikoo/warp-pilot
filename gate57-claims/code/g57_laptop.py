"""
g57_laptop.py — Gate-57 laptop admission control (corroboration
only; deciding reads are the VM's). Runs on the laptop pool with
Phase 417's staged builder + the wa instrument (the gate's
machinery): B-4 chain reads, the registered-set wa audit at
h = 0.0375 at beta = 0.194140625, and point reads at the VM
dense worst point (h = 0.009375 and 0.0375). Admission bar:
agreement at the 1e-9 level or better on the deciding margins.
Usage: python g57_laptop.py job.json
job.json: {"y": [...], "n_c": 16, "beta": f, "worst_point": [x,y,z]}
"""
import json, sys, time
import numpy as np

sys.path.insert(0, "/home/spark/work/p417")
import p417_lib as P
from p417_lib import GradedBuilder, audit_chunked, summarise, \
    pts_1020_control, DTYPE
import wa_auditor as wa

job = json.load(open(sys.argv[1]))
t0 = time.time()
b = GradedBuilder(np.array(job["y"], dtype=DTYPE), n_c=job["n_c"])
out = {"chain_reads": b.chain_reads()}
pts, radp = pts_1020_control()
gf = b.metric_factory(job["beta"])
m = audit_chunked(gf, pts, 0.0375, wa.audit)
s = summarise(m, pts, radp)
al = s["all_sig"]
out["wa_h0.0375_registered"] = {
    "worst": al["worst"], "worst_kind": al["worst_kind"],
    "worst_r": al[al["worst_kind"] + "_r"],
    "per_ec": {k: al[k] for k in ("nec", "wec", "sec", "dec")},
    "typeI_frac": al["typeI_frac"],
    "shell_sampled_nec_min": s["shell"]["sampled_nec_min"],
    "floor_proxy": s["floor_proxy_nonsig_median_abs_nec"]}
pt = np.array([job["worst_point"]], dtype=DTYPE)
reads = {}
for h in (0.009375, 0.0375):
    mm = wa.audit(gf, pt, h)
    reads[f"h{h}"] = {k: float(mm[k][0])
                      for k in ("nec", "wec", "sec", "dec")}
    reads[f"h{h}"]["typeI"] = bool(mm["typeI"][0])
    reads[f"h{h}"]["sampled_nec"] = float(mm["sampled_nec"][0])
out["worst_point_reads"] = reads
out["wall_s"] = time.time() - t0
json.dump(out, open("/home/spark/work/p417/g57_laptop_out.json", "w"),
          indent=1)
print("G57 LAPTOP DONE", out["wall_s"])
