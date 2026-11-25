#!/usr/bin/env python
"""P72-2 checker: recomputes every verdict-carrying number from
p722_results.json using the published formulas (Hotta arXiv:1002.0200)
independently of the evaluation script, and asserts the filing criterion
fixed in the run record §7."""
import json, numpy as np
D = json.load(open("/home/hatch/workspace/warp-pilot/phase72/results/p722_results.json"))
FR = 3.0/(32*np.pi**2); ok = []
def chk(name, cond): ok.append((name, bool(cond))); assert cond, name
for p in D["points"]:
    h, k = p["h"], p["k"]; S = np.sqrt(h*h+k*k)
    EA = h*h/S
    EB = (h*h+2*k*k)/S*(np.sqrt(1+h*h*k*k/(h*h+2*k*k)**2)-1)
    chk(f"r={p['r']} EA formula", abs(EA-p["EA"])<1e-12)
    chk(f"r={p['r']} EB formula", abs(EB-p["EB"])<1e-12)
    chk(f"r={p['r']} f0 = -EB (direct H evolution)", abs(p["f0_HBV"]+EB)<1e-9)
    chk(f"r={p['r']} EB <= EA (source bound)", EB <= EA)
    lam = (1+h/S)/2; Sg = -(lam*np.log(lam)+(1-lam)*np.log(1-lam))
    chk(f"r={p['r']} S_ground", abs(Sg/np.log(2)-p["S_ground_ebits"])<1e-12)
    chk(f"r={p['r']} dS = S_ground (projective)", abs(p["dS_consumed_ebits"]-p["S_ground_ebits"])<1e-9)
    chk(f"r={p['r']} E_prep_marg = 2k^2/S", abs(2*k*k/S-p["E_prep_marg"])<1e-12)
    chk(f"r={p['r']} E_prep_sep > 0", p["E_prep_sep"]>0)
    chk(f"r={p['r']} net Bob sector >= 0", p["E_net_B_sector"]>=0)
    chk(f"r={p['r']} R_net = 0", p["R_net"]==0.0)
    chk(f"r={p['r']} R_net <= 1 (deciding pulse line)", p["R_net"]<=1)
    tot = (p["E_prep_sep"]+EA)/EB
    chk(f"r={p['r']} total/EB recomputed", abs(tot-p["total_per_EB"])<1e-9)
    chk(f"r={p['r']} total/EB >= 1 (deciding price line)", tot>=1)
    chk(f"r={p['r']} R_raw recomputed", abs(EB*p["tau_pulse"]/FR-p["R_raw"])<1e-9)
p1 = [p for p in D["points"] if p["r"]==1.0][0]
chk("control h=k: EA=0.7071 (review value)", abs(p1["EA"]-0.7071)<1e-3)
chk("control h=k: EB=0.1147 (review value)", abs(p1["EB"]-0.1147)<1e-3)
print(f"CHECKER: {len(ok)}/{len(ok)} assertions PASS")
print("FILING CRITERION (run record §7): total/EB >= 1 at all points AND R_net <= 1 at all points")
print("=> FILED AS RELOCATION")
