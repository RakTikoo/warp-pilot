"""Gate5 W-D fresh Lentz v2: analytic beta, own FD Einstein (Gamma-FD). float64."""
import numpy as np, json
VS=2.0; R=1.0; SIG=3.0
def f_and_fp(r):
    # f and df/dr analytic
    a=np.tanh(SIG*(r+R)); b=np.tanh(SIG*(r-R)); den=2*np.tanh(SIG*R)
    f=(a-b)/den
    fp=(SIG*(1-a*a)-SIG*(1-b*b))/den
    return f,fp
def beta(p):
    p=np.asarray(p,float); x,y,z=p; r=np.sqrt(x*x+y*y+z*z)
    if r<1e-12: return np.array([0.,0.,VS*1.0])  # f(0)=1
    f,fp=f_and_fp(r)
    # Phi=VS*z*f(r); grad = VS*z*fp * rhat ; z-comp += VS*f
    g=VS*z*fp*p/r; g[2]+=VS*f
    return g
def metric(p):
    b=beta(p); g=np.diag([0.,1.,1.,1.]); g[0,0]=-1+np.dot(b,b)
    g[0,1:]=b; g[1:,0]=b; return g
W1={2:-1/12,1:8/12,-1:-8/12,-2:1/12}
def gamma_at(q,h):
    g=metric(q); ginv=np.linalg.inv(g); dg=np.zeros((4,4,4))
    for d in range(3):
        e=np.zeros(3); e[d]=1
        for off,w in W1.items(): dg[:,:,d+1]+=w*metric(q+off*h*e)/h
    Gam=np.zeros((4,4,4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam[a,b,c]=0.5*np.sum(ginv[a,:]*(dg[:,c,b]+dg[:,b,c]-dg[b,c,:]))
    return Gam,g,ginv
def einstein(p,h):
    p=np.asarray(p,float); Gam0,g,ginv=gamma_at(p,h); dGam=np.zeros((4,4,4,4))
    for d in range(3):
        e=np.zeros(3); e[d]=1
        for off,w in W1.items():
            Gd,_,_=gamma_at(p+off*h*e,h); dGam[d+1]+=w*Gd/h
    Ric=np.zeros((4,4))
    for b in range(4):
        for dd in range(4):
            v=0.0
            for a in range(4):
                v+=dGam[a,a,b,dd]-dGam[dd,a,b,a]
                v+=np.sum(Gam0[a,a,:]*Gam0[:,b,dd])-np.sum(Gam0[a,dd,:]*Gam0[:,b,a])
            Ric[b,dd]=v
    Rs=np.sum(ginv*Ric); return (Ric-0.5*Rs*g)/(8*np.pi)
def that(p,h):
    T=einstein(p,h); b=beta(p); tet=np.zeros((4,4)); tet[0,0]=1; tet[0,1:]=-b
    for i in range(3): tet[1+i,1+i]=1
    return tet@T@tet.T
def rho_formula(p):
    # Hessian of Phi via FD on analytic beta (grad Phi = beta): K=-Hess, squares sign-free
    hh=1e-5; H=np.zeros((3,3))
    for j in range(3):
        e=np.zeros(3); e[j]=hh
        H[:,j]=(beta(np.asarray(p)+e)-beta(np.asarray(p)-e))/(2*hh)
    return (np.trace(H)**2-np.sum(H*H))/(16*np.pi)
def nec_bf(That,ndir=800):
    idx=np.arange(ndir); ph=np.arccos(1-2*(idx+.5)/ndir); th=np.pi*(1+np.sqrt(5))*idx
    D=np.stack([np.cos(th)*np.sin(ph),np.sin(th)*np.sin(ph),np.cos(ph)],1)
    v=That[0,0]+2*D@That[0,1:]+np.einsum('ni,ij,nj->n',D,That[1:,1:],D)
    k=np.argmin(v); best=v[k]; bd=D[k]; step=.1
    for _ in range(120):
        imp=False
        for ax in range(3):
            for s in (-step,step):
                d=bd.copy(); d[ax]+=s; d/=np.linalg.norm(d)
                vv=That[0,0]+2*d@That[0,1:]+d@That[1:,1:]@d
                if vv<best: best,bd=vv,d; imp=True
        if not imp: step*=.5
    return best,bd

if __name__=="__main__":
    out={}
    rng=np.random.default_rng(7); pts=[]
    while len(pts)<250:
        q=rng.uniform(-2.6,2.6,3)
        if np.linalg.norm(q)<=2.6: pts.append(q)
    for h in (0.04,0.02):
        rhos=np.array([that(q,h)[0,0] for q in pts])
        diffs=[abs(that(q,h)[0,0]-rho_formula(q)) for q in pts[:80]]
        print(f"h={h} rho_min={rhos.min():.4f} rho_max={rhos.max():.4f} frac_neg={np.mean(rhos<-1e-3):.3f} formula_maxdiff80={max(diffs):.5f}",flush=True)
        out[f"h{h}"]={"rho_min":float(rhos.min()),"rho_max":float(rhos.max()),"frac_neg":float(np.mean(rhos<-1e-3)),"formula_maxdiff80":float(max(diffs))}
    sites=[[0.0817974157896659,-0.02879600795873346,-0.8393509521377898],[0,0,-0.8],[0,0,0.8],[-0.06432929178376731,0.11108478718494076,1.2358688852137403],[1,0,0]]
    out["sites"]=[]
    for s in sites:
        for h in (0.02,0.01):
            Th=that(s,h); nec,bd=nec_bf(Th)
            rec={"site":s,"h":h,"rho":float(Th[0,0]),"nec_bf":float(nec),"dir":bd.tolist(),"spatial_eig":np.linalg.eigvalsh(Th[1:,1:]).tolist(),"fluxmax":float(np.abs(Th[0,1:]).max())}
            out["sites"].append(rec); print(rec,flush=True)
    # scan shell for NEC min
    best=(1e9,None,None)
    for th_ in np.linspace(0.15,np.pi-0.15,9):
        for ph_ in np.linspace(0,2*np.pi,16,endpoint=False):
            for rr in (0.6,0.8,0.9,1.0,1.2):
                q=np.array([rr*np.sin(th_)*np.cos(ph_),rr*np.sin(th_)*np.sin(ph_),rr*np.cos(th_)])
                Th=that(q,0.02); nec,_=nec_bf(Th,400)
                if nec<best[0]: best=(float(nec),q.tolist(),float(Th[0,0]))
    print("scan NEC min",best,flush=True); out["scan_nec"]={"nec":best[0],"site":best[1],"rho":best[2]}
    # hunt around worst site h=0.01 small ball
    rng2=np.random.default_rng(3); ws=np.array(sites[0]); bh=1e9
    for i in range(60):
        q=ws+rng2.uniform(-0.15,0.15,3); Th=that(q,0.01); nec,_=nec_bf(Th,400); bh=min(bh,float(nec))
    print("hunt h0.01 min NEC",bh,flush=True); out["hunt_h001"]=bh
    # box integral analytic (vectorised per z-slice using FD Hessian on beta grid? use rho_formula on coarse grid 28^3)
    N=28; xs=np.linspace(-2.8,2.8,N); dv=(xs[1]-xs[0])**3; tot=tota=0.0
    for x in xs:
        for y in xs:
            for z in xs:
                rf=rho_formula(np.array([x,y,z])); tot+=rf; tota+=abs(rf)
    print(f"box int rho={tot*dv:.4f} abs={tota*dv:.4f} ratio%={abs(tot/tota)*100:.3f}",flush=True)
    out["box"]={"int":float(tot*dv),"abs":float(tota*dv)}
    json.dump(out,open("results/wd_lentz.json","w"),indent=1)
