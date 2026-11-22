"""Gate5 W-D vectorised fresh Einstein computation for Lentz + Krasnikov. float64."""
import numpy as np, json
W1={2:-1/12,1:8/12,-1:-8/12,-2:1/12}
def einstein_vec(metric_func, pts, h):
    pts=np.asarray(pts,float); N=len(pts)
    def gamma(PP):
        g=metric_func(PP); ginv=np.linalg.inv(g); dg=np.zeros((len(PP),4,4,4))
        for d in range(3):
            e=np.zeros(3); e[d]=1
            for off,w in W1.items(): dg[:,:,:,d+1]+=w*metric_func(PP+off*h*e)/h
        Gam=np.einsum('nae,nbec->nabc',ginv,0.5*(np.transpose(dg,(0,3,1,2))+np.transpose(dg,(0,2,1,3))-np.transpose(dg,(0,1,2,3))*0)) # placeholder replaced below
        # explicit loop over a,b,c (64) vectorised over N
        Gam=np.zeros((len(PP),4,4,4))
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    Gam[:,a,b,c]=0.5*np.sum(ginv[:,a,:]*(dg[:,:,c,b]+dg[:,:,b,c]-dg[:,b,c,:]),axis=1)
        return Gam,g,ginv
    Gam0,g,ginv=gamma(pts); dGam=np.zeros((N,4,4,4,4))
    for d in range(3):
        e=np.zeros(3); e[d]=1
        for off,w in W1.items():
            Gd,_,_=gamma(pts+off*h*e); dGam[:,d+1]+=w*Gd/h
    Ric=np.zeros((N,4,4))
    for b in range(4):
        for dd in range(4):
            v=np.zeros(N)
            for a in range(4):
                v+=dGam[:,a,a,b,dd]-dGam[:,dd,a,b,a]
                v+=np.sum(Gam0[:,a,a,:]*Gam0[:,:,b,dd],axis=1)-np.sum(Gam0[:,a,dd,:]*Gam0[:,:,b,a],axis=1)
            Ric[:,b,dd]=v
    Rs=np.einsum('nij,nij->n',ginv,Ric)
    G=Ric-0.5*Rs[:,None,None]*g
    return G/(8*np.pi), g
def nec_bf(That,ndir=600):
    idx=np.arange(ndir); ph=np.arccos(1-2*(idx+.5)/ndir); th=np.pi*(1+np.sqrt(5))*idx
    D=np.stack([np.cos(th)*np.sin(ph),np.sin(th)*np.sin(ph),np.cos(ph)],1)
    v=That[0,0]+2*D@That[0,1:]+np.einsum('ni,ij,nj->n',D,That[1:,1:],D)
    k=np.argmin(v); best=float(v[k]); bd=D[k]; step=.1
    for _ in range(100):
        imp=False
        for ax in range(3):
            for s in (-step,step):
                d=bd.copy(); d[ax]+=s; d/=np.linalg.norm(d)
                vv=That[0,0]+2*d@That[0,1:]+d@That[1:,1:]@d
                if vv<best: best=float(vv); bd=d; imp=True
        if not imp: step*=.5
    return best,bd

# ---------- LENTZ ----------
VS=2.0; RR=1.0; SIG=3.0
def lentz_beta(PP):
    PP=np.atleast_2d(np.asarray(PP,float)); x,y,z=PP[:,0],PP[:,1],PP[:,2]; r=np.sqrt(x*x+y*y+z*z); r=np.where(r<1e-12,1e-12,r)
    a=np.tanh(SIG*(r+RR)); b=np.tanh(SIG*(r-RR)); den=2*np.tanh(SIG*RR)
    f=(a-b)/den; fp=(SIG*(1-a*a)-SIG*(1-b*b))/den
    g=(VS*z*fp)[:,None]*(PP/r[:,None]); g[:,2]+=VS*f; return g
def lentz_metric(PP):
    PP=np.atleast_2d(np.asarray(PP,float)); N=len(PP); b=lentz_beta(PP); g=np.zeros((N,4,4))
    g[:,0,0]=-1+np.sum(b*b,axis=1); g[:,0,1:]=b; g[:,1:,0]=b
    for i in range(3): g[:,1+i,1+i]=1
    return g
def lentz_rho_formula(PP):
    PP=np.atleast_2d(np.asarray(PP,float)); hh=1e-5; out=[]
    for j in range(3):
        e=np.zeros(3); e[j]=hh
        out.append((lentz_beta(PP+e)-lentz_beta(PP-e))/(2*hh))
    H=np.stack(out,axis=2)  # H[:,i,j]=d_j beta_i
    tr=np.trace(H,axis1=1,axis2=2)
    return (tr*tr-np.einsum('nij,nij->n',H,H))/(16*np.pi)
def lentz_that(pts,h):
    T,g=einstein_vec(lentz_metric,pts,h); b=lentz_beta(pts); N=len(pts); tet=np.zeros((N,4,4)); tet[:,0,0]=1; tet[:,0,1:]=-b
    for i in range(3): tet[:,1+i,1+i]=1
    return np.einsum('nab,nbc,ncd->nad',tet,T,np.transpose(tet,(0,2,1)))

# ---------- KRASNIKOV ----------
DELTA=0.01; EPS=1.0; RHOMAX=10.0; D=100.0
def theta_eps(xi):
    return 0.5*(np.tanh(2*(2*xi/EPS-1))+1)
def k_of(PP,t=None):
    PP=np.atleast_2d(np.asarray(PP,float)); x=PP[:,0]; rho=np.sqrt(PP[:,1]**2+PP[:,2]**2)
    if t is None: bracket=theta_eps(x)-theta_eps(x+EPS-D); front=np.ones_like(x)
    else: front=theta_eps(t-x-rho); bracket=theta_eps(x)-theta_eps(x+EPS-D)
    return 1-(2-DELTA)*theta_eps(RHOMAX-rho)*front*bracket, rho
def kras_metric(PP):
    PP=np.atleast_2d(np.asarray(PP,float)); N=len(PP); k,_=k_of(PP); g=np.zeros((N,4,4))
    g[:,0,0]=-1; g[:,0,1]=(1-k)/2; g[:,1,0]=(1-k)/2; g[:,1,1]=k; g[:,2,2]=1; g[:,3,3]=1; return g
def kras_that_static(pts,h):
    T,g=einstein_vec(kras_metric,pts,h); k,_=k_of(pts); N=len(pts); tet=np.zeros((N,4,4))
    tet[:,0,0]=1
    tet[:,1,0]=(1-k)/(1+k); tet[:,1,1]=2/(1+k)
    tet[:,2,2]=1; tet[:,3,3]=1
    return np.einsum('nab,nbc,ncd->nad',tet,T,np.transpose(tet,(0,2,1))), k
def kras_rho_analytic(rho):
    # ER Eq (T): Ttt = [32pi(1+k)^2]^-1[-4(1+k)k'/rho +3 k'^2 -4(1+k)k'']
    hh=1e-4
    def kk(r):
        PP=np.array([[50.0,r,0.0]]); return k_of(PP)[0][0]
    rs=np.asarray(rho,float); out=[]
    for r in rs:
        k0=kk(r); kp=(kk(r+hh)-kk(r-hh))/(2*hh); kpp=(kk(r+hh)-2*k0+kk(r-hh))/(hh*hh)
        out.append((-4*(1+k0)*kp/r+3*kp*kp-4*(1+k0)*kpp)/(32*np.pi*(1+k0)**2))
    return np.array(out)

if __name__=="__main__":
    res={}
    rng=np.random.default_rng(7); pts=[]
    while len(pts)<300:
        q=rng.uniform(-2.6,2.6,3)
        if np.linalg.norm(q)<=2.6: pts.append(q)
    pts=np.array(pts)
    for h in (0.04,0.02):
        Th=lentz_that(pts,h); rho=Th[:,0,0]; rf=lentz_rho_formula(pts)
        print(f"LENTZ h={h} rho_min={rho.min():.4f} rho_max={rho.max():.4f} frac_neg={np.mean(rho<-1e-3):.3f} formula_maxdiff={np.max(np.abs(rho-rf)):.5f}",flush=True)
        res[f"lentz_h{h}"]={"rho_min":float(rho.min()),"rho_max":float(rho.max()),"frac_neg":float(np.mean(rho<-1e-3)),"formula_maxdiff":float(np.max(np.abs(rho-rf)))}
    sites=np.array([[0.0817974157896659,-0.02879600795873346,-0.8393509521377898],[0,0,-0.8],[0,0,0.8],[-0.06432929178376731,0.11108478718494076,1.2358688852137403],[1,0,0]])
    res["lentz_sites"]=[]
    for h in (0.02,0.01):
        Th=lentz_that(sites,h)
        for i,s in enumerate(sites):
            nec,bd=nec_bf(Th[i]); eig=np.linalg.eigvalsh(Th[i,1:,1:])
            rec={"h":h,"site":s.tolist(),"rho":float(Th[i,0,0]),"nec":float(nec),"dir":bd.tolist(),"eig":eig.tolist(),"fluxmax":float(np.abs(Th[i,0,1:]).max())}
            res["lentz_sites"].append(rec); print("L site",rec,flush=True)
    # shell scan NEC
    cand=[]
    for th_ in np.linspace(0.15,np.pi-0.15,9):
        for ph_ in np.linspace(0,2*np.pi,16,endpoint=False):
            for rr in (0.6,0.8,0.9,1.0,1.2):
                cand.append([rr*np.sin(th_)*np.cos(ph_),rr*np.sin(th_)*np.sin(ph_),rr*np.cos(th_)])
    cand=np.array(cand); Th=lentz_that(cand,0.02); necs=np.array([nec_bf(Th[i],300)[0] for i in range(len(cand))])
    i=np.argmin(necs); print("L scan NEC min",float(necs[i]),cand[i],float(Th[i,0,0]),flush=True)
    res["lentz_scan"]={"nec":float(necs[i]),"site":cand[i].tolist(),"rho":float(Th[i,0,0])}
    # hunt h=0.01 around claimed worst
    rng2=np.random.default_rng(3); hunt=sites[0]+rng2.uniform(-0.15,0.15,(40,3)); Th=lentz_that(hunt,0.01); hn=np.array([nec_bf(Th[i],300)[0] for i in range(40)])
    print("L hunt h0.01 NEC min",float(hn.min()),flush=True); res["lentz_hunt_h001"]=float(hn.min())
    # WEC/SEC/DEC at worst site via Type-I eig (flux small): margins
    Th=lentz_that(sites[:1],0.02)[0]; eig=np.linalg.eigvalsh(Th[1:,1:]); rho=float(Th[0,0])
    res["lentz_worst_margins_typeI"]={"NEC":float(rho+eig.min()),"WEC":float(min(rho,rho+eig.min())),"SEC":float(min(rho+eig.min(),rho+np.sum(eig))),"DEC":float(rho-np.max(np.abs(eig)))}
    print("L worst TypeI margins",res["lentz_worst_margins_typeI"],flush=True)
    # box integral analytic
    N=30; xs=np.linspace(-2.8,2.8,N); dv=(xs[1]-xs[0])**3; grid=np.array([[x,y,z] for x in xs for y in xs for z in xs]); rf=lentz_rho_formula(grid)
    print(f"L box int={rf.sum()*dv:.4f} abs={np.abs(rf).sum()*dv:.4f} ratio%={abs(rf.sum()/np.abs(rf).sum())*100:.3f}",flush=True)
    res["lentz_box"]={"int":float(rf.sum()*dv),"abs":float(np.abs(rf).sum()*dv)}
    # ---- Krasnikov wall scan ----
    rhos=np.linspace(7.5,11.5,33); wpts=np.array([[50.0,r,0.0] for r in rhos])
    res["kras"]={}
    for h in (0.05,0.025):
        Th,k=kras_that_static(wpts,h); necs=np.array([nec_bf(Th[i],400)[0] for i in range(len(rhos))])
        # WEC brute-ish: min over timelike velocities sampled: use NEC as lower bound proxy + rho_static reported; also sampled WEC
        i=np.argmin(necs)
        print(f"K h={h} NECmin={necs[i]:.4f} at rho={rhos[i]:.3f} rho_static={Th[i,0,0]:.4f} flux={Th[i,0,1]:.4f}",flush=True)
        res["kras"][f"h{h}"]={"nec_min":float(necs[i]),"rho_at":float(rhos[i]),"rho_static_worst":float(Th[i,0,0])}
        if h==0.025:
            res["kras"]["That_worst"]=Th[i].tolist()
            # Type-I-only NEC scan: points with small flux relative
            ti=[]
            for j in range(len(rhos)):
                if abs(Th[j,0,1])<1e-6 and np.max(np.abs(Th[j,0,2:]))<1e-6:
                    eig=np.linalg.eigvalsh(Th[j,1:,1:]); ti.append(float(Th[j,0,0]+eig.min()))
            res["kras"]["typeI_nec_min_approx"]=float(min(ti)) if ti else None
    # analytic profile
    rr=np.linspace(8.0,12.0,801); ra=kras_rho_analytic(rr); neg=np.minimum(ra,0); pos=np.maximum(ra,0)
    Ineg=np.trapezoid(2*np.pi*rr*neg,rr); Ipos=np.trapezoid(2*np.pi*rr*pos,rr)
    print(f"K analytic peak_rho={ra.min():.4f} at {rr[np.argmin(ra)]:.3f} Ineg/L={Ineg:.3f} Ipos/L={Ipos:.3f} net={Ineg+Ipos:.3f} rho@rhomax-eps={ra[np.argmin(np.abs(rr-9.0))]:.4f}",flush=True)
    res["kras_profile"]={"peak":float(ra.min()),"peak_rho":float(rr[np.argmin(ra)]),"Ineg":float(Ineg),"Ipos":float(Ipos),"net":float(Ineg+Ipos)}
    # judge Ttt vs analytic at wall pts h=0.025
    Th,_=kras_that_static(wpts,0.025)
    # Ttt covariant coordinate: That static tet inverse: T_tt = That_tt (e_t = tet0) since tet0=(1,0,0,0) => Ttt_coord = That[0,0]
    ana=kras_rho_analytic(rhos); rel=np.abs(Th[:,0,0]-ana)/np.maximum(np.abs(ana),1e-9)
    print("K Ttt vs analytic max rel (where |ana|>0.05)",float(rel[np.abs(ana)>0.05].max()),flush=True)
    res["kras_Ttt_maxrel"]=float(rel[np.abs(ana)>0.05].max())
    # QI recomputation: import stored profile totals (allowed) + my Ford-Roman machinery
    stored=json.load(open("../phase22/results/p222_audit.json"))
    hbar=1.054571817e-34; c=299792458.0; G=6.67430e-11
    Elegal=lambda L: 3/(32*np.pi**2)*hbar*c/L
    Eneg_per_m=stored["ledger"]["E_neg_per_metre_J"]
    for Dlab,Dval in (("1m",1.0),("1ly",9.4607e15)):
        Etot=Eneg_per_m*Dval
        print(f"QI D={Dlab} Etot={Etot:.3e} ratio_eps={Etot/Elegal(0.1):.3e} ratio_a={Etot/Elegal(1.0):.3e}",flush=True)
        res[f"qi_{Dlab}"]={"ratio_eps":float(Etot/Elegal(0.1)),"ratio_a":float(Etot/Elegal(1.0))}
    peakSI=stored["ledger"]["peak_rho_neg_SI_Jm3"]; tau=0.1/c; bound=3/(32*np.pi**2)*hbar/(c**3*tau**4)
    print(f"QI peak ratio={peakSI/bound:.3e} bound={bound:.3e}",flush=True); res["qi_peak_ratio"]=float(peakSI/bound)
    # ER rescaling check: Eneg/L ∝1/eps -> at eps_ER=1.616e-31 m
    Eneg_at_ER=Eneg_per_m*(0.1/1.6162550239285498e-31)  # J per m tube, D=1m
    Mgal_kg=2e42  # order galactic mass kg (ER rough) - report in kg and solar masses instead
    print(f"ER rescale: Eneg(1m tube at eps bound)={Eneg_at_ER:.3e} J = {Eneg_at_ER/c**2:.3e} kg = {Eneg_at_ER/c**2/1.988e30:.3e} Msun",flush=True)
    res["er_rescale_kg"]=float(Eneg_at_ER/c**2)
    # travel: return photon ODE dt/dx=-k(t,x,0) from (t=100,x=100) going left, tanh thetas with t
    def return_time(eps_scale=1.0):
        # integrate in x from 100 to 0, dt/dx = -k(t,x,0); k with front theta(t-x)
        t=100.0; x=100.0; dx=-0.05
        while x>0:
            PP=np.array([[x,0.0,0.0]]); rho=np.array([0.0])
            front=theta_eps(t-x-0.0); brack=theta_eps(x)-theta_eps(x+EPS-D); kk=1-(2-DELTA)*theta_eps(RHOMAX)*front*brack
            t+= -kk*dx if False else 0
            # dt/dx = -k  => dt = -k*dx (dx negative)
            t += (-kk)*dx; x+=dx
        return t
    t_ret=return_time(); print(f"K return arrival t_E numeric ODE={t_ret:.3f} Delta_t_r={t_ret-100:.3f} (paper asymp t_E=1, Dt=-99)",flush=True)
    res["kras_return"]={"t_E":float(t_ret),"Dt":float(t_ret-100)}
    # construction support scan: at x=D, earliest t with |k-1|>0.01
    ts=np.linspace(0,130,1301); ks=[]
    for t in ts:
        PP=np.array([[100.0,0.0,0.0]]); front=theta_eps(t-100.0); brack=theta_eps(100.0)-theta_eps(100.0+EPS-D); ks.append(1-(2-DELTA)*theta_eps(RHOMAX)*front*brack)
    ks=np.array(ks); idx=np.where(np.abs(ks-1)>0.01)[0]
    print("K support at B: earliest t |k-1|>0.01 =",float(ts[idx[0]]) if len(idx) else None,flush=True)
    res["kras_support_tB"]=float(ts[idx[0]]) if len(idx) else None
    json.dump(res,open("results/wd_vec.json","w"),indent=1)
    print("DONE")
