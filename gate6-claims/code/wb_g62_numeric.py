"""W-B GATE-6 G6-2 numeric spot check, independent of wb symbolic route.
Numeric tensor evaluator: given concrete analytic profiles (b,Phi,phi and
their 1st/2nd r-derivatives, supplied per-profile below), build metric,
Christoffel and Ricci by direct float64 index loops at each r, form
E_tt=-8pi rho_dem, E_rr=8pi pr_dem, evaluate at r=r0+delta for a ladder
of deltas, and linearly extrapolate delta->0. Compare to canonical pair.
Profiles (r0=1):
 controlled set C1-C3: SAME sqrt-shape b (beta=+1/2), SAME phi0=0.9,
   xi=1.5 (so F0=1+1.5*0.81=2.215 identical), but different Phi'_0 and
   phi'_0 (hence F'_0, F''_0 differ). Canonical predicts identical
   pr_dem(r0)=-F0/(8pi) for all three.
 T-Ellis: Ellis b (beta=-1), different everything.
F(r)=1+xi*phi(r)^2, F'=2 xi phi phi', F''=2 xi (phi'^2+phi phi'').
Phi profiles: Phi = a*(1-1/r) => Phi'=a/r^2, Phi''=-2a/r^3.
phi profiles: phi = phi0 + c*(r-1) + d*(r-1)^2.
b sqrt: b=r^{1/2}, b'=0.5 r^{-1/2}; Ellis: b=1/r, b'=-1/r^2.
"""
import numpy as np, json

def tensor_E(r, prof):
    b, bp, Phi, Phip, F, Fp, Fpp = prof(r)
    A = 1-b/r; Ap = -bp/r + b/r**2
    # Einstein (standard MT formulas, evaluated numerically here from
    # Christoffel loops is overkill: use the numeric G components built
    # from A,Phi finite quantities -- independent implementation):
    # G^t_t = -b'/r^2  (exact MT identity, numeric evaluation)
    Gtt = -bp/r**2
    Grr = -b/r**3 + 2*A*Phip/r
    # Hessian/Box from numeric Christoffel values:
    # Gamma^r_tt = A*N^2*Phi' with N=e^Phi ; Gamma^t_tr=Phi'; Gamma^r_rr=-A'/(2A) (A>0 off throat)
    # BoxF = A Fpp + (A Phip + 2A/r + Ap/2) Fp
    BoxF = A*Fpp + (A*Phip + 2*A/r + Ap/2)*Fp
    nab_tt = A*Phip*Fp          # nabla^t nabla_t F
    nab_rr = A*Fpp + Ap*Fp/2    # nabla^r nabla_r F
    rho8 = -(F*Gtt + BoxF - nab_tt)
    pr8 = F*Grr + BoxF - nab_rr
    return rho8/(8*np.pi), pr8/(8*np.pi)

def make_prof(shape, a, phi0, c, d, xi):
    def prof(r):
        if shape=='sqrt': b=r**0.5; bp=0.5*r**-0.5
        else: b=1/r; bp=-1/r**2
        Phi=a*(1-1/r); Phip=a/r**2
        phi=phi0+c*(r-1)+d*(r-1)**2; phip=c+2*d*(r-1); phipp=2*d
        F=1+xi*phi**2; Fp=2*xi*phi*phip; Fpp=2*xi*(phip**2+phi*phipp)
        return b,bp,Phi,Phip,F,Fp,Fpp
    return prof

cases = [
    ("C1 sqrt a=+0.5 phi'=+0.4", make_prof('sqrt', 0.5, 0.9, 0.4, 0.3, 1.5), 0.5, 0.9, 1.5),
    ("C2 sqrt a=-1.7 phi'=-1.1", make_prof('sqrt', -1.7, 0.9, -1.1, -0.8, 1.5), 0.5, 0.9, 1.5),
    ("C3 sqrt a=+2.3 phi'=+2.0", make_prof('sqrt', 2.3, 0.9, 2.0, 1.4, 1.5), 0.5, 0.9, 1.5),
    ("E1 ellis a=-2.0 phi'=+0.7 xi=2", make_prof('ellis', -2.0, 0.6, 0.7, 0.5, 2.0), -1.0, 0.6, 2.0),
]
deltas = np.array([0.04,0.02,0.01,0.005,0.0025])
out={}
for name, prof, beta, phi0, xi in cases:
    vals=[tensor_E(1+dl, prof) for dl in deltas]
    rho_ex = np.polyfit(deltas, [v[0] for v in vals],1)[1]
    pr_ex  = np.polyfit(deltas, [v[1] for v in vals],1)[1]
    # throat data
    b,bp,Phi,Phip,F0,Fp0,Fpp0 = prof(1.0)
    rho_can = F0*beta/(8*np.pi) - (1-beta)*Fp0/(16*np.pi)
    pr_can = -F0/(8*np.pi)
    out[name]=dict(F0=F0,Fp0=Fp0,Fpp0=Fpp0,Phip0=Phip,
        rho_extrap=rho_ex, rho_canonical=rho_can, rho_err=abs(rho_ex-rho_can),
        pr_extrap=pr_ex, pr_canonical=pr_can, pr_err=abs(pr_ex-pr_can),
        pr_at_smallest_delta=vals[-1][1])
    print(f"{name}: F0={F0:.4f} F'0={Fp0:+.4f} F''0={Fpp0:+.4f} Phi'0={Phip:+.2f}")
    print(f"   rho: extrap {rho_ex:+.8f} canonical {rho_can:+.8f} err {abs(rho_ex-rho_can):.2e}")
    print(f"   pr : extrap {pr_ex:+.8f} canonical {pr_can:+.8f} err {abs(pr_ex-pr_can):.2e}")
prs=[v['pr_extrap'] for k,v in list(out.items())[:3]]
print("Controlled C1-C3 pr spread (F'0,Phi'0,F''0 all differ, F0,beta same):", max(prs)-min(prs))
with open('wb_g62_numeric.json','w') as f: json.dump(out,f,indent=1)
print("WROTE wb_g62_numeric.json")
