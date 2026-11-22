"""Gate5 W-D fresh Lentz verification. float64. Independent FD Einstein."""
import numpy as np, json, itertools, math
np.set_printoptions(suppress=False)
VS=2.0; R=1.0; SIG=3.0
def fshape(r):
    return (np.tanh(SIG*(r+R))-np.tanh(SIG*(r-R)))/(2*np.tanh(SIG*R))
def Phi(p):
    x,y,z=p; r=np.sqrt(x*x+y*y+z*z)
    return VS*z*fshape(r)
def beta(p):
    # analytic gradient via complex? use central FD on Phi with tiny step (analytic function, not metric FD)
    h=1e-6; out=np.zeros(3)
    for i in range(3):
        dp=np.zeros(3); dp[i]=h; dm=np.zeros(3); dm[i]=-h
        out[i]=(Phi(np.array(p)+dp)-Phi(np.array(p)+dm))/(2*h)
    return out
def metric(p):
    b=beta(p); g=np.zeros((4,4))
    g[0,0]=-1.0+np.dot(b,b)
    for i in range(3):
        g[0,1+i]=b[i]; g[1+i,0]=b[i]; g[1+i,1+i]=1.0
    return g
def einstein(p,h):
    # 4th-order central FD for spatial derivatives (stationary)
    pts={}
    # derivatives dg[mu,nu,dir]
    dg=np.zeros((4,4,3))
    d2g=np.zeros((4,4,3,3))
    coeff1=[(1,-2,1/12),(-1,-1,-1/12),(2,1,-2/3),(-2,2,2/3)] # offset, weight denom h: use standard
    # standard 4th order first deriv weights: f' = (-f(x+2h)+8f(x+h)-8f(x-h)+f(x-2h))/(12h)
    w1={2:-1/12,1:8/12,-1:-8/12,-2:1/12}
    w2={2:-1/12,1:16/12,0:-30/12,-1:16/12,-2:-1/12} # /h^2
    for d in range(3):
        e=np.zeros(3); e[d]=1.0
        vals={}
        for off in (-2,-1,0,1,2):
            vals[off]=metric(np.array(p,float)+off*h*e)
        for off,w in w1.items(): dg[:,:,d]+=w*vals[off]/h
        for off,w in w2.items(): d2g[:,:,d,d]+=w*vals[off]/(h*h)
    # mixed second derivatives: 4th-order? use 2nd-order central for mixed (sufficient? use product of 1st deriv operators 4th via tensor)
    for d in range(3):
        for e_ in range(d+1,3):
            # apply w1 in both directions
            acc=np.zeros((4,4))
            ed=np.zeros(3); ed[d]=1; ee=np.zeros(3); ee[e_]=1
            for od,wd in w1.items():
                for oe,we in w1.items():
                    acc+=wd*we*metric(np.array(p,float)+od*h*ed+oe*h*ee)/(h*h)
            d2g[:,:,d,e_]=acc; d2g[:,:,e_,d]=acc
    g=metric(p); ginv=np.linalg.inv(g)
    # Gamma^a_bc, a,b,c in 0..3, derivatives only spatial (dir index 1..3 for x_a)
    Gam=np.zeros((4,4,4))
    dg_full=np.zeros((4,4,4)) # dg[mu,nu,alpha]
    dg_full[:,:,1:]=dg
    d2_full=np.zeros((4,4,4,4))
    d2_full[:,:,1:,1:]=d2g
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam[a,b,c]=0.5*np.sum(ginv[a,:]*(dg_full[:,c,b]+dg_full[:,b,c]-dg_full[b,c,:]))
    # Ricci R_{bd}= d_a Gam^a_{bd} - d_d Gam^a_{ba} + Gam Gam - ...
    # derivative of Gamma: need deriv of ginv and dg: compute Gam at offset points instead (FD on Gamma) - simpler & independent
    return None

def einstein_via_gamma_fd(p,h):
    # compute Gamma field by analytic-in-g FD at stencil points, then FD Gamma
    def gamma_at(q):
        g=metric(q); ginv=np.linalg.inv(g)
        dg=np.zeros((4,4,3))
        w1={2:-1/12,1:8/12,-1:-8/12,-2:1/12}
        for d in range(3):
            e=np.zeros(3); e[d]=1
            for off,w in w1.items(): dg[:,:,d]+=w*metric(np.array(q,float)+off*h*e)/h
        dgf=np.zeros((4,4,4)); dgf[:,:,1:]=dg
        Gam=np.zeros((4,4,4))
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    Gam[a,b,c]=0.5*np.sum(ginv[a,:]*(dgf[:,c,b]+dgf[:,b,c]-dgf[b,c,:]))
        return Gam,g,ginv
    Gam0,g,ginv=gamma_at(p)
    dGam=np.zeros((4,4,4,4)) # dGam[deriv_alpha, a,b,c]
    w1={2:-1/12,1:8/12,-1:-8/12,-2:1/12}
    for d in range(3):
        e=np.zeros(3); e[d]=1
        for off,w in w1.items():
            Gd,_ ,_=gamma_at(np.array(p,float)+off*h*e)
            dGam[d+1]+=w*Gd/h
    Ric=np.zeros((4,4))
    for b in range(4):
        for d_ in range(4):
            val=0.0
            for a in range(4):
                val+=dGam[a,a,b,d_] - dGam[d_,a,b,a]
                for e_ in range(4):
                    val+=Gam0[a,a,e_]*Gam0[e_,b,d_] - Gam0[a,d_,e_]*Gam0[e_,b,a]
            Ric[b,d_]=val
    Rscal=np.sum(ginv*Ric)
    G= Ric-0.5*Rscal*g
    return G/(8*np.pi), g

def that_eulerian(p,h):
    T,g=einstein_via_gamma_fd(p,h)
    b=beta(p)
    tet=np.zeros((4,4)) # tet[hat, mu]
    tet[0,0]=1.0; tet[0,1:]=-b
    for i in range(3): tet[1+i,1+i]=1.0
    That=tet@T@tet.T
    return That

def rho_formula(p):
    # Lentz printed: rho=(K^2-trK^2)/16pi, K_ij = Hessian Phi (sign irrelevant)
    hh=1e-4; H=np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            ei=np.zeros(3); ei[i]=hh; ej=np.zeros(3); ej[j]=hh
            if i==j:
                H[i,j]=(Phi(np.array(p)+ei)-2*Phi(np.array(p))+Phi(np.array(p)-ei))/(hh*hh)
            else:
                H[i,j]=(Phi(np.array(p)+ei+ej)-Phi(np.array(p)+ei-ej)-Phi(np.array(p)-ei+ej)+Phi(np.array(p)-ei-ej))/(4*hh*hh)
    K=H
    return (np.trace(K)**2-np.sum(K*K))/(16*np.pi), K

def nec_bruteforce(That, ndir=2000):
    # min over null dirs (1,n): That00+2 That0i n_i+ Thatij ni nj ; fibonacci sphere + local refine
    idx=np.arange(ndir); phi=np.arccos(1-2*(idx+0.5)/ndir); theta=np.pi*(1+np.sqrt(5))*idx
    dirs=np.stack([np.cos(theta)*np.sin(phi),np.sin(theta)*np.sin(phi),np.cos(phi)],axis=1)
    vals=That[0,0]+2*dirs@That[0,1:]+np.einsum('ni,ij,nj->n',dirs,That[1:,1:],dirs)
    k=np.argmin(vals); best=vals[k]; bd=dirs[k]
    # local hill climb
    step=0.1
    for it in range(200):
        improved=False
        for ax in range(3):
            for s in (-step,step):
                d=bd.copy(); d[ax]+=s; d/=np.linalg.norm(d)
                v=That[0,0]+2*d@That[0,1:]+d@That[1:,1:]@d
                if v<best: best=v; bd=d; improved=True
        if not improved: step*=0.5
    return best,bd

if __name__=="__main__":
    rng=np.random.default_rng(7)
    # sample points r<=2.6
    pts=[]
    while len(pts)<800:
        q=rng.uniform(-2.6,2.6,3)
        if np.linalg.norm(q)<=2.6: pts.append(q)
    pts=np.array(pts)
    for h in (0.04,0.02):
        rhos=[]; diffs=[]
        for q in pts[:400]:
            Th=that_eulerian(q,h); rhos.append(Th[0,0])
            rf,_=rho_formula(q); diffs.append(abs(Th[0,0]-rf))
        rhos=np.array(rhos)
        print(f"h={h} rho_min={rhos.min():.4f} rho_max={rhos.max():.4f} frac_neg={np.mean(rhos<-1e-3):.3f} formula_maxdiff(400pts)={max(diffs):.5f}")
    # worst site from claim + axis sites, detailed at h=0.02 and 0.01
    sites=[np.array([0.0817974157896659,-0.02879600795873346,-0.8393509521377898]),
           np.array([0.,0.,-0.8]), np.array([0.,0.,0.8]),
           np.array([-0.06432929178376731,0.11108478718494076,1.2358688852137403]),
           np.array([1.,0.,0.])]
    for s in sites:
        for h in (0.02,0.01):
            Th=that_eulerian(s,h)
            nec,bd=nec_bruteforce(Th)
            # Type-I approx if flux small: eigenvalues of spatial vs rho
            print(f"site {np.round(s,3)} h={h} rho={Th[0,0]:.4f} fluxmax={np.abs(Th[0,1:]).max():.4f} NECbrute={nec:.4f} dir={np.round(bd,3)} That_spatial_eig={np.round(np.linalg.eigvalsh(Th[1:,1:]),3)}")
    # scan for NEC min over grid shell r in [0.5,1.3]
    best=(1e9,None,None)
    cand=[]
    for th in np.linspace(0,np.pi,13):
        for ph in np.linspace(0,2*np.pi,24,endpoint=False):
            for rr in np.linspace(0.5,1.3,9):
                q=np.array([rr*np.sin(th)*np.cos(ph),rr*np.sin(th)*np.sin(ph),rr*np.cos(th)])
                cand.append(q)
    for q in cand:
        Th=that_eulerian(q,0.02); nec,_=nec_bruteforce(Th,ndir=500)
        if nec<best[0]: best=(nec,q,Th[0,0])
    print("scan NEC min",best[0],"at",best[1],"rho",best[2])
    # divergence identity: grid integral of analytic rho over box [-2.8,2.8]^3
    N=56; xs=np.linspace(-2.8,2.8,N); dv=(xs[1]-xs[0])**3; tot=0.0; tota=0.0
    for x in xs:
        for y in xs:
            for z in xs:
                rf,_=rho_formula(np.array([x,y,z])); tot+=rf; tota+=abs(rf)
    print(f"box integral rho={tot*dv:.4f} abs={tota*dv:.4f} ratio={abs(tot/tota)*100:.3f}%")
