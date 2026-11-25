"""P108-5 primary evaluation: Xun & Ren arXiv:2410.04919 N-qubit QET
under P72-2/P106-3 inherited accounting. Definitions fixed in
p1085_definitions.md BEFORE this computation.
Path: printed closed forms (Eqs.6,11) for E_in/E_out; E_prep^(marg)
closed form 4k^2/D derived from the printed H and |g>; tau from the
sector-energy evolution S(t), computed by exact 2x2 complement-pair
block decomposition of the printed H (H and the sector operator are
block-diagonal in |x>,|xbar> pairs). float64."""
import numpy as np, itertools, json
import numpy.linalg as la
from scipy.optimize import brentq
COEFF = 3/(32*np.pi**2)
CONFIGS = [(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(6,1),(8,1),(10,1)]
RS = [0.5,1.0,2.0]

def closed(N,m,h,k):
    D=np.sqrt(N**2*h**2+4*k**2)
    Eout=(N*m*h**2+4*k**2)/D*(np.sqrt(1+(2*(N-m)*h*k)**2/(N*m*h**2+4*k**2)**2)-1)
    Ein=(N-m)*N*h**2/D
    Eprep=4*k**2/D
    return float(Eout),float(Ein),float(Eprep)

def taus(N,m,h,k,tmax=30.0):
    dim=2**N; D=np.sqrt(N**2*h**2+4*k**2)
    a=np.sqrt((1-N*h/D)/2); b=np.sqrt((1+N*h/D)/2)
    n_in=N-m; outs=list(range(n_in,N))
    A=N*m*h**2+4*k**2; B=2*(N-m)*h*k
    theta=0.5*np.arccos(A/np.sqrt(A**2+B**2))
    g=np.zeros(dim,complex); g[0]=a; g[-1]=-b
    gt=g.reshape([2]*N); psi_list=[]
    for alpha in itertools.product([1,-1],repeat=n_in):
        t=gt.copy()
        for j,al in enumerate(alpha): t=0.5*(t+al*np.flip(t,axis=j))
        ap=int(np.prod(alpha)); Gt=t.copy()
        for i in outs[1:]: Gt=np.flip(Gt,axis=i)
        f=np.flip(Gt,axis=outs[0]); ph=np.ones([2]*N,complex); sl=[slice(None)]*N
        sl[outs[0]]=0; ph[tuple(sl)]=-1j; sl[outs[0]]=1; ph[tuple(sl)]=1j
        psi_list.append((np.cos(theta)*t-1j*ap*np.sin(theta)*(f*ph)).reshape(-1))
    bits=np.array([[(x>>(N-1-i))&1 for i in range(N)] for x in range(dim)])
    signs=1-2*bits; d_all=h*signs.sum(axis=1); dsec_all=h*signs[:,outs].sum(axis=1)
    Csec=m*N*h**2/D + 4*k**2/D; gaps=[]; coeffs=[]
    for x in range(dim//2):
        xc=dim-1-x
        Hb=np.array([[d_all[x]+D,2*k],[2*k,d_all[xc]+D]],complex)
        Sb=np.array([[dsec_all[x]+Csec,2*k],[2*k,dsec_all[xc]+Csec]],complex)
        rb=np.zeros((2,2),complex)
        for psi in psi_list:
            v=np.array([psi[x],psi[xc]]); rb+=np.outer(v,v.conj())
        if abs(rb).max()<1e-14: continue
        w,U=la.eigh(Hb); re=U.conj().T@rb@U; se=U.conj().T@Sb@U; Mx=re*se.T
        for p in range(2):
            for q in range(2):
                if abs(Mx[p,q])>1e-13: gaps.append(w[p]-w[q]); coeffs.append(Mx[p,q])
    gaps=np.array(gaps); coeffs=np.array(coeffs)
    def S(t): return float(np.sum(coeffs*np.exp(-1j*gaps*t)).real)
    Eprep=4*k**2/D
    ts=np.linspace(0,tmax,6001); vals=np.empty(len(ts))
    for s in range(0,len(ts),500):
        tt=ts[s:s+500]; vals[s:s+500]=np.real(np.exp(-1j*np.outer(tt,gaps))@coeffs)
    def cross(level):
        idx=np.where((vals[:-1]<level)&(vals[1:]>=level))[0]
        if len(idx)==0: return None
        i=int(idx[0]); return float(brentq(lambda t:S(t)-level,ts[i],ts[i+1],xtol=1e-12))
    return -S(0.0), cross(0.0), cross(Eprep)

rows=[]
# N=2 control first
for (N,m) in [(2,1)]+CONFIGS:
    for r in RS:
        Eo_c,Ei,Ep = closed(N,m,1.0,r)
        Eo_t,t0,tm = taus(N,m,1.0,r)
        assert abs(Eo_c-Eo_t)<1e-9, (N,m,r,Eo_c,Eo_t)
        net=Ep-Eo_c; neg=max(0.0,-net)
        rows.append(dict(N=N,m=m,r=r,E_out=Eo_c,E_in=Ei,E_prep_marg=Ep,E_net_B=net,
            tau0=t0,tau_marg=tm,
            R_tau0=(neg*t0/COEFF if t0 else None),
            R_tau_marg=(neg*tm/COEFF if tm else None),
            R_net_primary=(neg*tm/COEFF if (neg>0 and tm) else (0.0 if neg==0 else None)),
            price_per_unit_marg=(Ep+Ei)/Eo_c))
        print(rows[-1],flush=True)
json.dump(dict(model="Xun & Ren arXiv:2410.04919, N-qubit QET (Eqs.1-14, App.A/B)",
  accounting="P72-2 run record / P106-3 inherited verbatim; see work/p1085_definitions.md",
  coeff_FR=COEFF, rows=rows), open("../results/p1085_results.json","w"), indent=1)
print("WROTE results/p1085_results.json")
