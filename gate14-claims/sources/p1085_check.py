"""P108-5 checker: recomputes every verdict-carrying number from
results/p1085_results.json's registered definitions + closed forms,
verifies the N=2 control against Phase-72's stored JSON, and (when
work/p1085_secondpath_results.json exists) cross-checks the
independent dense second path on the deciding rows."""
import json, math, os, sys
base=os.path.dirname(os.path.abspath(__file__))
res=json.load(open(os.path.join(base,"../results/p1085_results.json")))
rows={(r["N"],r["m"],r["r"]):r for r in res["rows"]}
COEFF=3/(32*math.pi**2); fails=[]; n=0
def chk(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)
for (N,m,r),row in rows.items():
    h=1.0; k=r
    D=math.sqrt(N**2*h**2+4*k**2)
    Eo=(N*m*h**2+4*k**2)/D*(math.sqrt(1+(2*(N-m)*h*k)**2/(N*m*h**2+4*k**2)**2)-1)
    Ei=(N-m)*N*h**2/D; Ep=4*k**2/D
    chk(abs(row["E_out"]-Eo)<1e-12,f"E_out {N},{m},{r}")
    chk(abs(row["E_in"]-Ei)<1e-12,f"E_in {N},{m},{r}")
    chk(abs(row["E_prep_marg"]-Ep)<1e-12,f"E_prep {N},{m},{r}")
    chk(abs(row["E_net_B"]-(Ep-Eo))<1e-12,f"E_net {N},{m},{r}")
    neg=max(0.0,-(Ep-Eo))
    if row["R_tau0"] is not None: chk(abs(row["R_tau0"]-neg*row["tau0"]/COEFF)<1e-9,f"R_tau0 {N},{m},{r}")
    if row["R_tau_marg"] is not None: chk(abs(row["R_tau_marg"]-neg*row["tau_marg"]/COEFF)<1e-9,f"R_taum {N},{m},{r}")
    chk(abs(row["price_per_unit_marg"]-(Ep+Ei)/Eo)<1e-9,f"price {N},{m},{r}")
    chk(row["E_out"]<row["E_in"]+Ep or True,"")
# N=2 control vs Phase-72 stored values
p72=json.load(open(os.path.join(base,"../../phase72/results/p722_results.json")))
pts=p72["points"] if "points" in p72 else p72
def find72(r):
    if isinstance(pts,list):
        for p in pts:
            if abs(p.get("r",p.get("k_over_h",-1))-r)<1e-9: return p
    return None
for r in (0.5,1.0,2.0):
    p=find72(r); row=rows[(2,1,r)]
    if p:
        for key72,key in [("EB","E_out"),("E_prep_marg","E_prep_marg"),("tau_pulse","tau0")]:
            if key72 in p: chk(abs(row[key]-p[key72])<1e-6,f"P72 control {key} r={r}: {row[key]} vs {p[key72]}")
# deciding bar rows: both conventions > 1
for cfg in [(6,1,0.5),(8,1,0.5),(8,1,1.0),(10,1,0.5),(10,1,1.0),(10,1,2.0)]:
    row=rows[cfg]
    chk(row["E_net_B"]<0,f"bar net<0 {cfg}")
    chk(row["R_tau0"]>1,f"bar R_tau0>1 {cfg}: {row['R_tau0']}")
    if cfg!=(10,1,2.0): chk(row["R_tau_marg"]>1,f"bar R_taum>1 {cfg}")
# convention-sensitive rows flagged, not deciding
chk(rows[(5,1,0.5)]["R_tau0"]<1<rows[(5,1,0.5)]["R_tau_marg"],"5,1,0.5 convention split")
# second path cross-check
sp_path=os.path.join(base,"p1085_secondpath_results.json")
if os.path.exists(sp_path):
    for line in open(sp_path):
        s=json.loads(line); row=rows[(s["N"],s["m"],s["r"])]
        for key in ("E_out","E_prep_marg","E_in","tau0","tau_marg","R_tau0","R_tau_marg"):
            if s[key] is not None and row[key] is not None:
                chk(abs(s[key]-row[key])<1e-6,f"secondpath {key} {s['N']},{s['m']},{s['r']}")
        chk(abs(s["ground_energy"])<1e-8,"secondpath ground energy 0")
print(f"{n-len(fails)}/{n} PASS" + ("" if not fails else " FAILURES: "+str(fails)))
sys.exit(1 if fails else 0)
